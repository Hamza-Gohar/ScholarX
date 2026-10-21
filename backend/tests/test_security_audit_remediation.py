import pytest
import io
from fastapi import HTTPException
from fastapi.testclient import TestClient
from main import app
from utils.security import (
    create_signed_session_token,
    verify_signed_session_token,
    sanitize_session_id,
    verify_session_ownership,
)
from utils.rate_limiter import RateLimiter
from utils.dossier_normalizer import clean_html_str
from utils.pdf_service import get_or_generate_scholarship_pdf


client = TestClient(app)


def test_health_check_sanitized():
    """Verify GET /api/health does not leak keys, masked strings, or key counts."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert "providers" in data
    # Ensure sensitive fields are completely absent
    content_str = response.text
    assert "masked_key" not in content_str
    assert "stats" not in content_str
    assert "current_index" not in content_str
    assert "gsk_" not in content_str
    assert "AIzaSy" not in content_str
    assert "tvly-" not in content_str


def test_session_token_cryptography():
    """Verify HMAC token generation, verification, and tamper detection."""
    session_id = "test-session-12345"
    token = create_signed_session_token(session_id)
    assert token.startswith(session_id)

    # Valid token verification
    verified_id = verify_signed_session_token(token)
    assert verified_id == session_id

    # Tampered token verification
    tampered = token[:-4] + "abcd"
    assert verify_signed_session_token(tampered) is None

    # Invalid structure verification
    assert verify_signed_session_token("invalid.token") is None
    assert verify_signed_session_token("") is None


def test_session_id_sanitization():
    """Verify session ID sanitization rejects traversal and injection patterns."""
    assert sanitize_session_id("valid_session-123") == "valid_session-123"

    with pytest.raises(HTTPException) as exc_info:
        sanitize_session_id("../../../etc/passwd")
    assert exc_info.value.status_code == 400

    with pytest.raises(HTTPException):
        sanitize_session_id("session; DROP TABLE students;--")


@pytest.mark.asyncio
async def test_idor_session_authorization():
    """Verify cross-session access is blocked when a caller presents another session's token."""
    from starlette.requests import Request

    token_a = create_signed_session_token("session-alice")

    # Mock request bearing Alice's token
    scope = {
        "type": "http",
        "headers": [(b"x-session-token", token_a.encode("utf-8"))],
    }
    request = Request(scope)

    # Accessing Alice's own session succeeds
    authorized_id = await verify_session_ownership("session-alice", request)
    assert authorized_id == "session-alice"

    # Attempting to access Bob's session with Alice's token raises 403 Forbidden
    with pytest.raises(HTTPException) as exc_info:
        await verify_session_ownership("session-bob", request)
    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_rate_limiter_enforcement():
    """Verify sliding-window rate limiter raises 429 when threshold exceeded."""
    from starlette.requests import Request

    limiter = RateLimiter(max_requests=3, window_seconds=10, name="test-limiter")
    scope = {"type": "http", "client": ("192.0.2.1", 1234), "headers": []}
    request = Request(scope)

    # 3 allowed requests
    for _ in range(3):
        await limiter.check(request)

    # 4th request must trigger HTTP 429 Too Many Requests
    with pytest.raises(HTTPException) as exc_info:
        await limiter.check(request)
    assert exc_info.value.status_code == 429
    assert "Retry-After" in exc_info.value.headers


def test_pdf_path_traversal_prevention():
    """Verify get_or_generate_scholarship_pdf prevents escaping single_dossiers directory."""
    with pytest.raises(ValueError) as exc_info:
        get_or_generate_scholarship_pdf("../../../../etc/passwd")
    # Sanitized ID fallback or directory confinement assertion
    assert "path traversal" in str(exc_info.value).lower() or "not found" in str(exc_info.value).lower()


def test_html_escaping_in_clean_str():
    """Verify clean_html_str sanitizes XSS and HTML injection payloads."""
    payload = '<script>alert("XSS")</script>&foo'
    escaped = clean_html_str(payload)
    assert "<script>" not in escaped
    assert "&lt;script&gt;" in escaped
    assert "&amp;foo" in escaped


def test_upload_security_validation():
    """Verify file upload endpoint rejects invalid extensions, empty files, and invalid magic bytes."""
    # 1. Invalid extension (.sh)
    response = client.post(
        "/api/profile/upload",
        data={"session_id": "upload-sec-test"},
        files={"file": ("exploit.sh", b"echo hacked", "text/plain")},
    )
    assert response.status_code == 400
    assert "Unsupported file format" in response.json()["detail"]

    # 2. Corrupted PDF (missing %PDF- magic bytes)
    response = client.post(
        "/api/profile/upload",
        data={"session_id": "upload-sec-test"},
        files={"file": ("fake.pdf", b"NOT_A_REAL_PDF_HEADER", "application/pdf")},
    )
    assert response.status_code == 400
    assert "magic signature" in response.json()["detail"]

    # 3. Empty file
    response = client.post(
        "/api/profile/upload",
        data={"session_id": "upload-sec-test"},
        files={"file": ("empty.pdf", b"", "application/pdf")},
    )
    assert response.status_code == 400
    assert "empty" in response.json()["detail"]
