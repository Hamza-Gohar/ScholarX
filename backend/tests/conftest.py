import asyncio
import pytest


@pytest.fixture(autouse=True)
async def cleanup_db_connections():
    """Autouse fixture ensuring session store background flusher and sqlite connections
    are cleanly terminated before pytest-asyncio destroys the test event loop.
    """
    yield
    try:
        from db.session_store import _global_session_store
        if _global_session_store is not None:
            # If there are pending items, give them a slice to flush or cancel
            await asyncio.sleep(0.01)
            await _global_session_store.close()
    except Exception:
        pass
