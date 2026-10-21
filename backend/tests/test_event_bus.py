import asyncio
import pytest
from events.bus import EventBus, get_event_bus
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent


@pytest.mark.asyncio
async def test_event_bus_publish_and_subscribe():
    bus = EventBus()
    session_id = "sess-bus-01"

    # Subscriber queue
    subscriber = bus.subscribe(session_id, replay_history=False)

    test_event = ScholarXEvent(
        session_id=session_id,
        event_type=AgentEventType.MISSION_INITIATED,
        agent_id="test_agent",
        agent_display_name="Test Agent",
        component_type="AGENT",
        phase="INTAKE",
        payload={"msg": "Hello Bus"},
    )

    # Publish
    await bus.publish(test_event)

    # Receive
    received = await asyncio.wait_for(anext(subscriber), timeout=2.0)
    assert received.event_id == test_event.event_id
    assert received.session_id == session_id
    assert received.payload["msg"] == "Hello Bus"


@pytest.mark.asyncio
async def test_event_bus_history_replay():
    bus = EventBus()
    session_id = "sess-bus-replay"

    # Publish 3 events before subscriber connects
    for i in range(3):
        evt = ScholarXEvent(
            session_id=session_id,
            event_type=AgentEventType.DIMENSION_EVALUATED,
            payload={"index": i},
        )
        await bus.publish(evt)

    # Late subscriber with replay_history=True
    subscriber = bus.subscribe(session_id, replay_history=True)

    replayed = []
    for _ in range(3):
        replayed.append(await asyncio.wait_for(anext(subscriber), timeout=2.0))

    assert len(replayed) == 3
    assert [e.payload["index"] for e in replayed] == [0, 1, 2]


@pytest.mark.asyncio
async def test_event_bus_session_isolation():
    bus = EventBus()
    sess_a = "sess-a"
    sess_b = "sess-b"

    sub_a = bus.subscribe(sess_a, replay_history=False)
    sub_b = bus.subscribe(sess_b, replay_history=False)

    evt_a = ScholarXEvent(session_id=sess_a, event_type=AgentEventType.SCOUT_DEPLOYED)
    evt_b = ScholarXEvent(session_id=sess_b, event_type=AgentEventType.HEC_CONFIRMED)

    await bus.publish(evt_a)
    await bus.publish(evt_b)

    rec_a = await asyncio.wait_for(anext(sub_a), timeout=2.0)
    rec_b = await asyncio.wait_for(anext(sub_b), timeout=2.0)

    assert rec_a.session_id == sess_a
    assert rec_a.event_type == AgentEventType.SCOUT_DEPLOYED
    assert rec_b.session_id == sess_b
    assert rec_b.event_type == AgentEventType.HEC_CONFIRMED


@pytest.mark.asyncio
async def test_event_bus_singleton():
    bus1 = get_event_bus()
    bus2 = get_event_bus()
    assert bus1 is bus2
