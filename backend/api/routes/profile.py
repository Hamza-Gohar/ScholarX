import logging
import os
from pathlib import Path
import tempfile
from typing import Optional
from fastapi import APIRouter, File, Form, HTTPException, Request, Response, UploadFile, status
from pydantic import BaseModel
from agents.profile_agent import ProfileAgent
from db.session_store import get_session_store
from events.bus import get_event_bus
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.student import StudentProfile
from tools.document_extractor import DocumentExtractor
from tools.document_parser import DocumentParserTool
from utils.rate_limiter import chat_limiter, upload_limiter
from utils.security import create_signed_session_token, sanitize_session_id, verify_session_ownership

logger = logging.getLogger("scholarx.api.profile")

router = APIRouter(prefix="/profile", tags=["profile"])

MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB limit
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt"}


class ProfileChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/upload")
async def upload_student_document(
    request: Request,
    response: Response,
    session_id: str = Form(...),
    file: UploadFile = File(...),
):
    """
    Ingests and parses academic transcripts, CVs, or English certificates.
    Enforces maximum file size, magic byte verification, and session ownership.
    """
    await upload_limiter.check(request)
    # Upload is the bootstrap flow for a new session; later mutations require its token.
    clean_sid = await verify_session_ownership(session_id, request, allow_unbound=True)

    # Validate file extension
    raw_filename = file.filename or "doc.txt"
    suffix = Path(raw_filename).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file format '{suffix}'. Allowed formats: PDF, DOCX, DOC, TXT.",
        )

    # Validate file size (chunked read up to MAX_UPLOAD_SIZE + 1)
    content = await file.read(MAX_UPLOAD_SIZE + 1)
    if len(content) > MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Uploaded file exceeds maximum allowed size of 10MB.",
        )
    if len(content) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty.",
        )

    # Verify magic bytes for binary formats
    if suffix == ".pdf" and not content.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid PDF file: corrupted header or incorrect magic signature.",
        )
    if suffix in (".docx",) and not content.startswith(b"PK\x03\x04"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid DOCX file: corrupted header or incorrect magic signature.",
        )

    store = get_session_store()
    bus = get_event_bus()

    # Load or initialize student profile
    student = await store.get_student_profile(clean_sid)
    if not student:
        student = StudentProfile(
            student_id=f"std-{clean_sid[-8:]}",
            session_id=clean_sid,
        )

    # Save uploaded file temporarily for parsing
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        parser = DocumentParserTool()
        parsed_doc = parser.parse_file(tmp_path)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    if not parsed_doc.clean_text or not parsed_doc.clean_text.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Could not extract text from document. Please ensure the document contains selectable text (e.g. not a scanned image or password-protected).",
        )

    # Extract structured data
    extractor = DocumentExtractor()
    extracted_data = await extractor.extract_from_text(parsed_doc.clean_text, parsed_doc.doc_type.value)

    # Apply updates via ProfileAgent
    agent = ProfileAgent()
    agent._apply_extracted_updates(student, extracted_data)
    student = agent.validator.validate_and_enrich(student)

    # Save to SQLite
    await store.save_student_profile(student)

    # Issue signed session token
    token = create_signed_session_token(clean_sid)
    response.headers["X-Session-Token"] = token

    # Emit real-time events to EventBus
    evt_upload = ScholarXEvent(
        session_id=clean_sid,
        event_type=AgentEventType.DOCUMENT_UPLOADED,
        agent_id="profile_agent",
        agent_display_name="Profile Intake Agent",
        component_type="AGENT",
        phase="INTAKE",
        payload={"filename": raw_filename, "doc_type": parsed_doc.doc_type.value, "char_count": parsed_doc.char_count},
        severity=EventSeverity.INFO,
    )
    await bus.publish(evt_upload)

    evt_profile = ScholarXEvent(
        session_id=clean_sid,
        event_type=AgentEventType.PROFILE_UPDATED,
        agent_id="profile_agent",
        agent_display_name="Profile Intake Agent",
        component_type="AGENT",
        phase="INTAKE",
        payload={
            "student_name": student.personal.name,
            "completeness": student.profile_completeness,
            "gpa": student.academic.gpa_percentage,
            "ielts": student.language.ielts_overall,
        },
        severity=EventSeverity.SUCCESS,
    )
    await bus.publish(evt_profile)

    return {
        "session_id": clean_sid,
        "doc_type": parsed_doc.doc_type.value,
        "profile": student,
        "session_token": token,
    }


@router.post("/chat")
async def profile_conversational_chat(req: ProfileChatRequest, request: Request, response: Response):
    """Multi-turn admissions counselor chat to clarify preferences, budgets, and gaps."""
    await chat_limiter.check(request)
    clean_sid = await verify_session_ownership(req.session_id, request)

    store = get_session_store()
    bus = get_event_bus()

    student = await store.get_student_profile(clean_sid)
    if not student:
        student = StudentProfile(
            student_id=f"std-{clean_sid[-8:]}",
            session_id=clean_sid,
        )

    agent = ProfileAgent()
    reply, updated_student = await agent.process_student_message(student, req.message)
    await store.save_student_profile(updated_student)

    token = create_signed_session_token(clean_sid)
    response.headers["X-Session-Token"] = token

    evt_chat = ScholarXEvent(
        session_id=clean_sid,
        event_type=AgentEventType.PROFILE_UPDATED,
        agent_id="profile_agent",
        agent_display_name="Profile Intake Agent",
        component_type="AGENT",
        phase="INTAKE",
        payload={"message": req.message, "reply": reply[:100], "completeness": updated_student.profile_completeness},
        severity=EventSeverity.INFO,
    )
    await bus.publish(evt_chat)

    return {
        "reply": reply,
        "response": reply,
        "session_id": clean_sid,
        "profile": updated_student,
        "session_token": token,
    }


@router.get("/{session_id}")
async def get_profile(session_id: str, request: Request):
    """Retrieves current student profile for a session."""
    clean_sid = await verify_session_ownership(session_id, request)
    store = get_session_store()
    student = await store.get_student_profile(clean_sid)
    if not student:
        raise HTTPException(status_code=404, detail="Student profile not found for this session")
    return {"session_id": clean_sid, "profile": student}


@router.put("/{session_id}")
async def update_profile(session_id: str, profile: StudentProfile, request: Request, response: Response):
    """Directly updates a student profile after verifying session authorization."""
    clean_sid = await verify_session_ownership(session_id, request)
    store = get_session_store()
    agent = ProfileAgent()
    existing = await store.get_student_profile(clean_sid)
    if existing:
        # student_id is server-owned and must not be used as an upsert key supplied by clients.
        profile.student_id = existing.student_id
    else:
        profile.student_id = f"std-{clean_sid[-8:]}"
    profile.session_id = clean_sid
    enriched = agent.validator.validate_and_enrich(profile)
    enriched.session_id = clean_sid
    enriched.student_id = enriched.student_id or f"std-{clean_sid[-8:]}"
    await store.save_student_profile(enriched)
    await store.create_session(clean_sid, enriched.student_id)

    token = create_signed_session_token(clean_sid)
    response.headers["X-Session-Token"] = token

    return {"session_id": clean_sid, "profile": enriched, "session_token": token}
