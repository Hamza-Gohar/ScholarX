import asyncio
import json
import logging
import time
from typing import Any, Dict, Optional
from config import get_settings

logger = logging.getLogger("scholarx.cache")


class MemoryCache:
    """Fast in-memory TTL cache for local single-process execution."""

    def __init__(self):
        self._store: Dict[str, Any] = {}
        self._expiry: Dict[str, float] = {}
        self._lock = asyncio.Lock()

    async def get(self, key: str) -> Optional[Any]:
        async with self._lock:
            if key not in self._store:
                return None
            if time.time() > self._expiry.get(key, 0):
                # Expired
                del self._store[key]
                del self._expiry[key]
                return None
            return self._store[key]

    async def set(self, key: str, value: Any, ttl_seconds: int = 3600):
        async with self._lock:
            self._store[key] = value
            self._expiry[key] = time.time() + ttl_seconds

    async def delete(self, key: str):
        async with self._lock:
            self._store.pop(key, None)
            self._expiry.pop(key, None)

    async def clear(self):
        async with self._lock:
            self._store.clear()
            self._expiry.clear()


_global_cache = MemoryCache()


def get_memory_cache() -> MemoryCache:
    return _global_cache
