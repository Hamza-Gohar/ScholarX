import asyncio
import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from events.bus import get_event_bus
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent


@pytest.mark.asyncio
async def test_event_bus_publish_and_subscribe():
    bus = get_event_bus()
    test_session = "test-live-session-1"

    sub = bus.subscribe(test_session, replay_history=False)

    event = ScholarXEvent(
        session_id=test_session,
        event_type=AgentEventType.MISSION_INITIATED,
        agent_id="orchestrator",
        agent_display_name="Mission Orchestrator",
        component_type="AGENT",
        phase="ORCHESTRATION",
        payload={"msg": "Test mission started"},
        severity=EventSeverity.INFO,
    )

    await bus.publish(event)

    received = await asyncio.wait_for(sub.__anext__(), timeout=2.0)
    assert received.event_id == event.event_id
    assert received.session_id == test_session
    assert received.event_type == AgentEventType.MISSION_INITIATED

    sub.close()


@pytest.mark.asyncio
async def test_sse_endpoint_format_and_streaming():
    from api.routes.stream import stream_events
    bus = get_event_bus()
    test_session = "test-live-session-sse"

    event = ScholarXEvent(
        session_id=test_session,
        event_type=AgentEventType.SCOUT_DEPLOYED,
        agent_id="europe_scout",
        agent_display_name="Europe Scout",
        component_type="WORKFLOW",
        phase="DISCOVERY",
        payload={"region": "Europe"},
        severity=EventSeverity.INFO,
    )
    await bus.publish(event)

    response = await stream_events(test_session)
    assert response.status_code == 200
    assert response.media_type == "text/event-stream"

    chunk = await anext(response.body_iterator)
    assert f"id: {event.event_id}" in chunk
    assert "event: SCOUT_DEPLOYED" in chunk
    assert "Europe Scout" in chunk
