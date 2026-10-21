import hashlib
import hmac
import logging
import re
import secrets
import time
from typing import Optional
from fastapi import Header, HTTPException, Request, status
from config import get_settings

logger = logging.getLogger("scholarx.security")

# Allowed characters for session IDs: letters, digits, hyphen, underscore (max 64 chars)
SESSION_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_\-]{3,64}$")

# Fallback in-memory secret if none is configured
_EPHEMERAL_SECRET = secrets.token_hex(32)


def get_session_secret() -> bytes:
    settings = get_settings()
    secret = getattr(settings, "SESSION_SECRET", None) or _EPHEMERAL_SECRET
    return secret.encode("utf-8")


def sanitize_session_id(session_id: str) -> str:
    """Validates session ID format to prevent path traversal and injection."""
    if not session_id or not SESSION_ID_PATTERN.match(session_id.strip()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid session identifier format. Only alphanumeric characters, hyphens, and underscores are permitted.",
        )
    return session_id.strip()


def create_signed_session_token(session_id: str) -> str:
    """
    Creates a cryptographically signed session token: <session_id>.<timestamp>.<signature>
    """
    clean_id = sanitize_session_id(session_id)
    timestamp = str(int(time.time()))
    payload = f"{clean_id}.{timestamp}".encode("utf-8")
    signature = hmac.new(get_session_secret(), payload, hashlib.sha256).hexdigest()
    return f"{clean_id}.{timestamp}.{signature}"


def verify_signed_session_token(token: str, max_age_seconds: int = 7 * 86400) -> Optional[str]:
    """
    Verifies token signature and expiration. Returns the authenticated session_id if valid, or None.
    """
    if not token or "." not in token:
        return None
    parts = token.split(".")
    if len(parts) != 3:
        return None

    session_id, timestamp_str, signature = parts
    try:
        ts = int(timestamp_str)
        if time.time() - ts > max_age_seconds or ts > time.time() + 300:
            return None  # Expired or clock skew
    except (ValueError, TypeError):
        return None

    payload = f"{session_id}.{timestamp_str}".encode("utf-8")
    expected_sig = hmac.new(get_session_secret(), payload, hashlib.sha256).hexdigest()

    if hmac.compare_digest(signature, expected_sig):
        return session_id
    return None


def extract_session_token_from_request(request: Request) -> Optional[str]:
    """
    Extracts session token from:
    1. X-Session-Token header
    2. Authorization: Bearer <token>
    3. scholarx_session cookie
    """
    # 1. Custom Header
    custom_token = request.headers.get("X-Session-Token")
    if custom_token:
        return custom_token.strip()

    # 2. Authorization Bearer
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.lower().startswith("bearer "):
        return auth_header[7:].strip()

    # 3. Cookie
    cookie_token = request.cookies.get("scholarx_session")
    if cookie_token:
        return cookie_token.strip()

    return None


def get_authenticated_session_id(request: Request) -> str:
    """Returns the session bound to a valid request token or raises 401."""
    token = extract_session_token_from_request(request)
    authenticated_sid = verify_signed_session_token(token) if token else None
    if not authenticated_sid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return sanitize_session_id(authenticated_sid)


async def verify_session_ownership(session_id: str, request: Request, *, allow_unbound: bool = False) -> str:
    """
    Enforces authorization for session access and mutation.
    Prevents IDOR / BOLA by ensuring the caller owns the targeted session.
    """
    clean_id = sanitize_session_id(session_id)
    token = extract_session_token_from_request(request)

    if not token and allow_unbound:
        return clean_id

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    authenticated_sid = verify_signed_session_token(token)
    if not authenticated_sid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if authenticated_sid != clean_id:
        logger.warning(
            "Unauthorized session access attempt: token claims '%s', target is '%s'",
            authenticated_sid,
            clean_id,
        )
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: you do not have permission to access or modify this session.",
        )

    return clean_id
