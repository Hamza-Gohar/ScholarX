import pytest
from api.routes.stream import stream_events
from events.bus import get_event_bus
from schemas.events import AgentEventType, ScholarXEvent


@pytest.mark.asyncio
async def test_sse_stream_endpoint_receives_events():
    session_id = "sess-stream-test"
    bus = get_event_bus()

    # Pre-publish an event to replay
    evt = ScholarXEvent(
        session_id=session_id,
        event_type=AgentEventType.MISSION_INITIATED,
        payload={"status": "started"},
    )
    await bus.publish(evt)

    # Call endpoint directly
    response = await stream_events(session_id)
    assert response.status_code == 200
    assert response.media_type == "text/event-stream"
    assert "Cache-Control" in response.headers

    # Consume the first event chunk from body_iterator
    first_chunk = await anext(response.body_iterator)
    assert "event: MISSION_INITIATED" in first_chunk
    assert "started" in first_chunk
