import asyncio
import logging
import time
from typing import Any, Dict, List, Optional, Set
from config import get_settings

logger = logging.getLogger("scholarx.api_keys")


class AllKeysExhaustedError(Exception):
    """Raised when all API keys for a given provider have failed or hit rate limits."""
    pass


class KeyHealth:
    def __init__(self, key: str):
        self.key = key
        self.failure_count: int = 0
        self.last_failure_time: float = 0.0
        self.is_healthy: bool = True
        self.total_requests: int = 0
        self.total_successes: int = 0

    def mark_success(self):
        self.total_requests += 1
        self.total_successes += 1
        self.failure_count = 0
        self.is_healthy = True

    def mark_failure(self, cooldown_seconds: float = 60.0):
        self.total_requests += 1
        self.failure_count += 1
        self.last_failure_time = time.time()
        self.is_healthy = False
        logger.warning(
            f"API Key masked {self.key[:6]}...{self.key[-4:] if len(self.key)>10 else ''} "
            f"marked failed (count={self.failure_count}). Cooldown={cooldown_seconds}s"
        )

    def check_recovery(self, cooldown_seconds: float = 60.0) -> bool:
        if not self.is_healthy:
            if (time.time() - self.last_failure_time) > cooldown_seconds:
                self.is_healthy = True
                logger.info(f"API Key masked {self.key[:6]}... recovered from cooldown.")
                return True
            return False
        return True


class APIKeyRotator:
    def __init__(self, provider_name: str, keys: List[str], cooldown_seconds: float = 60.0):
        self.provider_name = provider_name
        self.raw_keys = [k for k in keys if k and k.strip() and not k.startswith("your_")]
        self.key_healths: List[KeyHealth] = [KeyHealth(k) for k in self.raw_keys]
        self.current_index: int = 0
        self.cooldown_seconds = cooldown_seconds
        self._lock = asyncio.Lock()

    @property
    def total_keys(self) -> int:
        return len(self.raw_keys)

    @property
    def has_keys(self) -> bool:
        return len(self.raw_keys) > 0

    async def get_key(self) -> str:
        async with self._lock:
            if not self.has_keys:
                raise AllKeysExhaustedError(
                    f"No valid API keys configured for provider '{self.provider_name}'. Please update .env."
                )

            # Check if any cooling keys have recovered
            for kh in self.key_healths:
                kh.check_recovery(self.cooldown_seconds)

            # Look for next healthy key starting from current index
            for _ in range(len(self.key_healths)):
                idx = self.current_index % len(self.key_healths)
                kh = self.key_healths[idx]
                if kh.is_healthy:
                    # Advance current_index immediately so the NEXT request uses the NEXT key
                    self.current_index = (idx + 1) % len(self.key_healths)
                    return kh.key
                self.current_index = (self.current_index + 1) % len(self.key_healths)

            # If all are cooling down, raise AllKeysExhaustedError
            raise AllKeysExhaustedError(
                f"All {len(self.raw_keys)} API keys for provider '{self.provider_name}' are exhausted/cooling down."
            )

    async def report_failure(self, failed_key: str, error_code: Optional[int] = None):
        async with self._lock:
            # 429 Rate limit: 60s cooldown; 401/403 Invalid: long cooldown (3600s)
            cooldown = 3600.0 if error_code in (401, 403) else self.cooldown_seconds
            for idx, kh in enumerate(self.key_healths):
                if kh.key == failed_key:
                    kh.mark_failure(cooldown)
                    self.current_index = (idx + 1) % len(self.key_healths)
                    logger.info(
                        f"Rotated '{self.provider_name}' key to index {self.current_index} after failure."
                    )
                    break

    async def report_success(self, successful_key: str):
        async with self._lock:
            for kh in self.key_healths:
                if kh.key == successful_key:
                    kh.mark_success()
                    break

    def get_status_summary(self) -> Dict[str, Any]:
        return {
            "provider": self.provider_name,
            "total_keys": len(self.raw_keys),
            "healthy_keys": sum(1 for kh in self.key_healths if kh.is_healthy),
            "current_index": self.current_index,
            "stats": [
                {
                    "masked_key": f"{kh.key[:4]}...{kh.key[-4:]}" if len(kh.key) > 8 else "***",
                    "is_healthy": kh.is_healthy,
                    "failure_count": kh.failure_count,
                    "requests": kh.total_requests,
                    "successes": kh.total_successes,
                }
                for kh in self.key_healths
            ],
        }


class KeyManager:
    """Singleton manager that coordinates key rotators for all ScholarX cloud services."""
    _instance: Optional["KeyManager"] = None

    def __init__(self):
        settings = get_settings()
        self.gemini = APIKeyRotator("Gemini", settings.gemini_keys, cooldown_seconds=60.0)
        self.groq = APIKeyRotator("Groq", settings.groq_keys, cooldown_seconds=45.0)
        self.tavily = APIKeyRotator("Tavily", settings.tavily_keys, cooldown_seconds=60.0)
        self.firecrawl = APIKeyRotator("Firecrawl", settings.firecrawl_keys, cooldown_seconds=60.0)
        self.jina = APIKeyRotator("Jina", [settings.JINA_API_KEY] if settings.JINA_API_KEY else [], cooldown_seconds=60.0)

    @classmethod
    def get_instance(cls) -> "KeyManager":
        if cls._instance is None:
            cls._instance = KeyManager()
        return cls._instance


def get_key_manager() -> KeyManager:
    return KeyManager.get_instance()
