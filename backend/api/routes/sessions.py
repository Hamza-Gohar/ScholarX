import logging
from fastapi import APIRouter, HTTPException, Query, Request, Response
from db.session_store import get_session_store
from utils.security import create_signed_session_token, verify_session_ownership, get_authenticated_session_id

logger = logging.getLogger("scholarx.api.sessions")

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("")
async def list_sessions(request: Request, limit: int = Query(50, ge=1, le=100)):
    """Lists only the authenticated caller's session."""
    clean_sid = get_authenticated_session_id(request)
    store = get_session_store()
    session = await store.get_session_detail(clean_sid)
    return {"sessions": [session] if session else []}


@router.get("/{session_id}")
async def get_session_detail(session_id: str, request: Request, response: Response):
    """Retrieves full detail of a research session including student profile and discovered scholarships."""
    clean_id = await verify_session_ownership(session_id, request)
    store = get_session_store()
    session = await store.get_session_detail(clean_id)

    # Issue signed session token for caller convenience
    token = create_signed_session_token(clean_id)
    response.headers["X-Session-Token"] = token

    if not session:
        # Fallback to direct student profile check
        student = await store.get_student_profile(clean_id)
        if student:
            return {
                "session": {
                    "session_id": clean_id,
                    "student_id": student.student_id,
                    "status": "INITIATED",
                },
                "profile": student,
                "session_token": token,
            }
        raise HTTPException(status_code=404, detail="Session not found")

    return {
        "session": session,
        "profile": session.student_profile,
        "session_token": token,
    }


@router.delete("/{session_id}")
async def delete_session(session_id: str, request: Request):
    """Deletes a session and its associated logs and rankings after verifying ownership."""
    clean_id = await verify_session_ownership(session_id, request)
    store = get_session_store()
    await store.delete_session(clean_id)
    try:
        from events.bus import get_event_bus
        get_event_bus().cleanup_session(clean_id)
    except Exception as e:
        logger.debug(f"EventBus cleanup error on session delete: {e}")
    try:
        from api.routes.discover import evict_mission
        evict_mission(clean_id)
    except Exception as e:
        logger.debug(f"Mission eviction error on session delete: {e}")
    return {"session_id": clean_id, "status": "DELETED"}
