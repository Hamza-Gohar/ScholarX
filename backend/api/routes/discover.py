import asyncio
import logging
from typing import Any, Dict, Optional
from fastapi import APIRouter, BackgroundTasks, HTTPException, Request, Response
from pydantic import BaseModel
from db.session_store import get_session_store
from events.bus import get_event_bus
from graph.builder import build_scholarx_graph
from graph.state import ScholarXState
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.student import StudentProfile

logger = logging.getLogger("scholarx.api.discover")

router = APIRouter(prefix="/discover", tags=["discover"])

# In-memory mission registry to track background runs (bounded to prevent leaks)
_ACTIVE_MISSIONS: Dict[str, Dict[str, Any]] = {}
_MAX_MISSIONS = 100


def _register_mission(session_id: str, status: Dict[str, Any]) -> None:
    if len(_ACTIVE_MISSIONS) >= _MAX_MISSIONS and session_id not in _ACTIVE_MISSIONS:
        oldest_key = next(iter(_ACTIVE_MISSIONS))
        _ACTIVE_MISSIONS.pop(oldest_key, None)
    _ACTIVE_MISSIONS[session_id] = status


def evict_mission(session_id: str) -> None:
    """Removes a mission from active tracking registry."""
    _ACTIVE_MISSIONS.pop(session_id, None)


class DiscoverRequest(BaseModel):
    session_id: str
    profile: Optional[StudentProfile] = None


async def _run_discovery_pipeline_background(session_id: str, profile: StudentProfile):
    """Executes the master 10-node LangGraph pipeline in the background, streaming events."""
    bus = get_event_bus()
    store = get_session_store()
    _register_mission(session_id, {"status": "RUNNING", "phase": "ORCHESTRATION"})

    try:
        graph = build_scholarx_graph()

        # Custom event streamer callback that pushes directly to EventBus
        def stream_event_to_bus(evt: ScholarXEvent):
            asyncio.create_task(bus.publish(evt))

        initial_state: ScholarXState = {
            "session_id": session_id,
            "student_id": profile.student_id or f"std-{session_id[-8:]}",
            "student_profile": profile,
            "events_queue": [],
        }

        # Run pipeline (all 10 nodes stream events live to EventBus during execution)
        final_state = await graph.ainvoke(initial_state)

        # Upsert all candidate scholarships to cache in bulk safely
        candidates = final_state.get("candidate_scholarships", [])
        if candidates:
            try:
                await store.bulk_upsert_scholarships_cache(candidates)
            except Exception as cache_err:
                logger.warning(f"Scholarship cache bulk upsert notice (non-fatal): {cache_err}")

        # Save ranked scholarships and roadmap to SQLite session
        ranked = final_state.get("ranked_results", [])
        if ranked:
            try:
                await store.save_ranked_results(session_id, ranked)
            except Exception as rank_err:
                logger.warning(f"Save ranked results notice: {rank_err}")

        roadmap = final_state.get("final_roadmap")
        if roadmap:
            try:
                await store.save_roadmap(session_id, roadmap)
            except Exception as rd_err:
                logger.warning(f"Save roadmap notice: {rd_err}")

        _register_mission(
            session_id,
            {
                "status": "COMPLETE",
                "phase": "MISSION_COMPLETE",
                "total_ranked": len(ranked),
                "has_roadmap": roadmap is not None,
                "ranked_results": ranked,
                "final_roadmap": roadmap,
                "data_source": "LIVE_PIPELINE_AND_VERIFIED_DATABASE",
                "personalized": True,
            },
        )

        # Emit completion event
        evt_done = ScholarXEvent(
            session_id=session_id,
            event_type=AgentEventType.MISSION_COMPLETE,
            agent_id="orchestrator",
            agent_display_name="Mission Orchestrator",
            component_type="AGENT",
            phase="ORCHESTRATION",
            payload={"total_ranked": len(ranked), "has_roadmap": roadmap is not None},
            severity=EventSeverity.SUCCESS,
        )
        await bus.publish(evt_done)

    except Exception as e:
        logger.error(f"Error in background discovery mission for session {session_id}: {e}", exc_info=True)
        _register_mission(
            session_id,
            {
                "status": "ERROR",
                "phase": "ERROR",
                "error": "Mission pipeline encountered an internal error.",
                "data_source": "ERROR",
                "personalized": True,
            },
        )
        evt_err = ScholarXEvent(
            session_id=session_id,
            event_type=AgentEventType.PIPELINE_ERROR,
            agent_id="orchestrator",
            agent_display_name="Mission Orchestrator",
            component_type="AGENT",
            phase="ORCHESTRATION",
            payload={"error": "An unexpected error occurred during discovery mission orchestration."},
            severity=EventSeverity.CRITICAL,
        )
        await bus.publish(evt_err)


@router.post("")
async def launch_discovery_mission(
    req: DiscoverRequest,
    background_tasks: BackgroundTasks,
    request: Request,
    response: Response,
):
    """
    Launches autonomous 10-node discovery, verification, ranking, and roadmap generation.
    Protected with sliding-window rate limiting and session ownership verification.
    """
    from utils.rate_limiter import discover_limiter
    from utils.security import create_signed_session_token, verify_session_ownership

    await discover_limiter.check(request)
    # Session creation is intentionally bootstrap-friendly; the response issues a token.
    clean_sid = await verify_session_ownership(req.session_id, request, allow_unbound=True)

    store = get_session_store()
    student = req.profile
    if student:
        student.session_id = clean_sid
        try:
            await store.save_student_profile(student)
            await store.create_session(clean_sid, student.student_id)
        except Exception as store_err:
            logger.debug(f"Student store save skipped (non-fatal, DB-free mode): {store_err}")
    else:
        try:
            student = await store.get_student_profile(clean_sid)
        except Exception as store_err:
            logger.debug(f"Student profile store fetch skipped: {store_err}")
    if not student:
        # Load default canonical Pakistani student profile (Hamza Gohar, Intermediate)
        import json
        from pathlib import Path
        repo_root = Path(__file__).resolve().parents[3]
        default_file = repo_root / "data" / "profiles" / "ics_student.json"
        if not default_file.exists():
            default_file = Path(__file__).resolve().parents[2] / "data" / "profiles" / "ics_student.json"
        if default_file.exists():
            try:
                with open(default_file, "r", encoding="utf-8") as f:
                    p_data = json.load(f)
                    p_data["session_id"] = clean_sid
                    student = StudentProfile.model_validate(p_data)
                    try:
                        await store.save_student_profile(student)
                    except Exception as store_err:
                        logger.debug(f"Default student profile store save skipped: {store_err}")
            except Exception as e:
                logger.warning(f"Failed to auto-seed profile: {e}")

    if not student:
        raise HTTPException(
            status_code=400,
            detail="No student profile found for this session. Please upload a CV or create a profile first.",
        )

    # Initialize session record in SQLite if available
    try:
        await store.create_session(clean_sid, student.student_id or f"std-{clean_sid[-8:]}")
    except Exception as store_err:
        logger.debug(f"Session record initialization in DB skipped (DB-free mode): {store_err}")

    # Launch background task
    background_tasks.add_task(_run_discovery_pipeline_background, clean_sid, student)

    token = create_signed_session_token(clean_sid)
    response.headers["X-Session-Token"] = token

    return {
        "session_id": clean_sid,
        "status": "STARTED",
        "message": "Discovery mission activated. Connect to /api/stream/{session_id} for live event streaming.",
        "session_token": token,
    }


@router.get("/{session_id}/status")
async def get_discovery_status(session_id: str, request: Request):
    """Checks the status and active phase of a running discovery mission."""
    from utils.security import verify_session_ownership
    clean_sid = await verify_session_ownership(session_id, request)
    mission_info = _ACTIVE_MISSIONS.get(clean_sid, {"status": "IDLE", "phase": "NONE"})
    return {
        "session_id": clean_sid,
        "status": mission_info.get("status", "IDLE"),
        "active_phase": mission_info.get("phase", "NONE"),
        "error": mission_info.get("error"),
    }


@router.get("/{session_id}/results")
async def get_discovery_results(session_id: str, request: Request):
    """Retrieves live ranked results and roadmap for a completed discovery mission."""
    from utils.security import verify_session_ownership
    clean_sid = await verify_session_ownership(session_id, request)
    mission_info = _ACTIVE_MISSIONS.get(clean_sid)
    if mission_info and "ranked_results" in mission_info:
        return {
            "session_id": clean_sid,
            "status": mission_info.get("status", "COMPLETE"),
            "total_ranked": mission_info.get("total_ranked", 0),
            "ranked_results": mission_info.get("ranked_results", []),
            "roadmap": mission_info.get("final_roadmap"),
            "data_source": mission_info.get("data_source", "LIVE_PIPELINE_AND_VERIFIED_DATABASE"),
            "personalized": mission_info.get("personalized", True),
        }

    # Fallback to store if not found in active RAM registry
    store = get_session_store()
    try:
        session = await store.get_session_detail(clean_sid)
        if session:
            return {
                "session_id": clean_sid,
                "status": session.status.value,
                "total_ranked": len(session.discovered_scholarships),
                "ranked_results": session.discovered_scholarships,
                "roadmap": session.mission_parameters.get("roadmap") if session.mission_parameters else None,
                "data_source": "VERIFIED_DATABASE",
                "personalized": True,
            }
    except Exception as e:
        logger.debug(f"Store lookup failed for results: {e}")

    raise HTTPException(status_code=404, detail="Mission results not found or still processing.")
