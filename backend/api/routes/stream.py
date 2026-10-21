import asyncio
import logging
from typing import Optional
from fastapi import APIRouter, Query, Request
from fastapi.responses import StreamingResponse
from events.bus import get_event_bus

logger = logging.getLogger("scholarx.api.stream")

router = APIRouter(tags=["stream"])


async def _generate_sse_stream(session_id: str):
    """Async generator yielding formatted SSE frames with periodic keepalive heartbeats."""
    bus = get_event_bus()
    subscription = bus.subscribe(session_id, replay_history=True)
    try:
        while not subscription._closed:
            try:
                # Wait up to 15s for next event, else send keepalive comment
                event = await asyncio.wait_for(subscription.__anext__(), timeout=15.0)
                yield event.to_sse_format()
                await asyncio.sleep(0)
            except asyncio.TimeoutError:
                # SSE keepalive comment per §46 (keeps connection alive through reverse proxies)
                yield ": keepalive\n\n"
            except StopAsyncIteration:
                break
    except (asyncio.CancelledError, GeneratorExit):
        logger.info(f"SSE client disconnected from session: {session_id}")
    finally:
        subscription.close()


@router.get("/stream/{session_id}")
async def stream_events(session_id: str, request: Request = None):
    """
    Canonical Server-Sent Events (SSE) streaming endpoint for reactive UI rendering.
    Streams real-time agent updates, scout discoveries, skeptic challenges,
    ranking scores, and roadmaps directly to the browser.
    """
    if request is not None:
        from utils.security import verify_session_ownership
        clean_sid = await verify_session_ownership(session_id, request)
    else:
        from utils.security import sanitize_session_id
        clean_sid = sanitize_session_id(session_id)

    return StreamingResponse(
        _generate_sse_stream(clean_sid),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache, no-transform",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/stream")
async def stream_events_query(request: Request = None, session_id: Optional[str] = Query(None)):
    """Fallback endpoint supporting query-parameter session_id (?session_id=...)."""
    sid = session_id or "default-session"
    from utils.security import verify_session_ownership
    clean_sid = await verify_session_ownership(sid, request)

    return StreamingResponse(
        _generate_sse_stream(clean_sid),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache, no-transform",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
