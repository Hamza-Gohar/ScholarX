import asyncio
from functools import lru_cache
import logging
from typing import AsyncIterator, Dict, List, Optional, Set
from schemas.events import ScholarXEvent

logger = logging.getLogger("scholarx.events.bus")


class EventSubscription:
    """
    Active subscription to a session event stream.
    Implements async iterator protocol.
    """

    def __init__(
        self,
        bus: "EventBus",
        session_id: str,
        queue: asyncio.Queue,
        history: List[ScholarXEvent],
    ):
        self._bus = bus
        self._session_id = session_id
        self._queue = queue
        self._history = list(history)
        self._seen_event_ids: Set[str] = {e.event_id for e in self._history}
        self._closed = False

    def __aiter__(self) -> "EventSubscription":
        return self

    async def __anext__(self) -> ScholarXEvent:
        if self._history:
            return self._history.pop(0)
        
        if self._closed:
            raise StopAsyncIteration

        while True:
            event = await self._queue.get()
            if event.event_id in self._seen_event_ids:
                continue
            self._seen_event_ids.add(event.event_id)
            return event

    def close(self) -> None:
        """Unregisters subscriber queue from bus."""
        if not self._closed:
            self._closed = True
            self._bus.unregister_queue(self._session_id, self._queue)

    async def aclose(self) -> None:
        self.close()

    async def __aenter__(self) -> "EventSubscription":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


class EventBus:
    """
    High-performance real-time Pub/Sub Event Bus for ScholarX.
    Supports session-isolated event distribution, replay buffer for late connections,
    and automatic subscriber lifecycle management.
    """

    def __init__(self, max_history_per_session: int = 500):
        self._max_history = max_history_per_session
        self._subscribers: Dict[str, Set[asyncio.Queue]] = {}
        self._history: Dict[str, List[ScholarXEvent]] = {}
        self._active_log_tasks: Set[asyncio.Task] = set()
        self._lock = asyncio.Lock()

    async def publish(self, event: ScholarXEvent) -> None:
        """Publishes an event to all active session subscribers and appends to replay buffer."""
        session_id = event.session_id
        async with self._lock:
            if session_id not in self._history:
                self._history[session_id] = []
            
            self._history[session_id].append(event)
            if len(self._history[session_id]) > self._max_history:
                self._history[session_id].pop(0)

            queues = list(self._subscribers.get(session_id, set()))

        for q in queues:
            try:
                await q.put(event)
            except Exception as e:
                logger.warning(f"Error dispatching event {event.event_id} to subscriber queue: {e}")

        # Persist event to SQLite events_log via batched async queue
        try:
            from db.session_store import get_session_store
            store = get_session_store()
            ev_type = event.event_type.value if hasattr(event.event_type, "value") else str(event.event_type)
            ev_sev = event.severity.value if hasattr(event.severity, "value") else str(event.severity)
            await store.enqueue_event_log(
                event_id=event.event_id,
                session_id=session_id,
                event_type=ev_type,
                agent_id=event.agent_id,
                payload=event.payload,
                severity=ev_sev,
            )
        except Exception as db_err:
            logger.debug(f"SQLite event log schedule error: {db_err}")

        # Optional Redis Pub/Sub bridge with graceful fallback
        if not getattr(self, "_redis_failed", False):
            try:
                if getattr(self, "_redis_client", None) is None:
                    import redis.asyncio as aioredis
                    from config import get_settings
                    cfg = get_settings()
                    self._redis_client = aioredis.Redis(
                        host=cfg.REDIS_HOST,
                        port=cfg.REDIS_PORT,
                        socket_connect_timeout=0.2,
                    )
                channel = f"scholarx:events:{session_id}"
                await self._redis_client.publish(channel, event.model_dump_json())
            except Exception as re_err:
                self._redis_failed = True
                self._redis_client = None
                logger.debug(f"Redis bus bridge unavailable (using in-memory): {re_err}")

    def subscribe(
        self,
        session_id: str,
        replay_history: bool = True,
    ) -> EventSubscription:
        """
        Immediately registers and returns an EventSubscription for the session.
        History is captured at subscription time and yielded first.
        """
        history_snapshot = list(self._history.get(session_id, [])) if replay_history else []
        q: asyncio.Queue[ScholarXEvent] = asyncio.Queue()

        if session_id not in self._subscribers:
            self._subscribers[session_id] = set()
        self._subscribers[session_id].add(q)

        return EventSubscription(self, session_id, q, history_snapshot)

    def unregister_queue(self, session_id: str, queue: asyncio.Queue) -> None:
        """Removes a queue from the active subscribers set."""
        if session_id in self._subscribers and queue in self._subscribers[session_id]:
            self._subscribers[session_id].remove(queue)
            if not self._subscribers[session_id]:
                del self._subscribers[session_id]

    def get_history(self, session_id: str) -> List[ScholarXEvent]:
        """Returns snapshot of events for a given session."""
        return list(self._history.get(session_id, []))

    def clear_history(self, session_id: str) -> None:
        """Clears cached history for a session."""
        if session_id in self._history:
            del self._history[session_id]

    def cleanup_session(self, session_id: str) -> None:
        """Fully cleans up memory caches and subscriber queues for a session."""
        self.clear_history(session_id)
        if session_id in self._subscribers:
            del self._subscribers[session_id]


_GLOBAL_EVENT_BUS: Optional[EventBus] = None


def get_event_bus() -> EventBus:
    """Singleton getter for global ScholarX EventBus."""
    global _GLOBAL_EVENT_BUS
    if _GLOBAL_EVENT_BUS is None:
        _GLOBAL_EVENT_BUS = EventBus()
    return _GLOBAL_EVENT_BUS
