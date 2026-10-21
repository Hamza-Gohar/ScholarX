import asyncio
import time
import logging
from collections import defaultdict
from typing import Dict, List, Optional
from fastapi import HTTPException, Request, status

logger = logging.getLogger("scholarx.rate_limiter")


class RateLimiter:
    """
    Sliding-window in-memory rate limiter per client IP or session.
    Automatically purges expired windows to prevent memory leaks.
    """
    def __init__(self, max_requests: int = 20, window_seconds: int = 60, name: str = "default"):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.name = name
        self._history: Dict[str, List[float]] = defaultdict(list)
        self._lock = asyncio.Lock()
        self._last_purge = time.time()

    def _get_client_key(self, request: Request) -> str:
        """Determines unique client identity from headers or IP."""
        # Check reverse proxy forwarded header first
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            client_ip = forwarded.split(",")[0].strip()
        elif request.client and request.client.host:
            client_ip = request.client.host
        else:
            client_ip = "127.0.0.1"

        # If a session token is present, bind to session as well
        session_token = request.headers.get("X-Session-Token") or request.cookies.get("scholarx_session")
        if session_token:
            return f"{client_ip}:{session_token[:16]}"
        return client_ip

    async def check(self, request: Request) -> None:
        """
        Enforces rate limits. Raises HTTPException(429) if exceeded.
        """
        now = time.time()
        client_key = self._get_client_key(request)

        async with self._lock:
            # Periodic cleanup of keys inactive for more than 5 minutes
            if now - self._last_purge > 300:
                self._purge_stale(now)
                self._last_purge = now

            timestamps = self._history[client_key]
            cutoff = now - self.window_seconds

            # Filter out entries older than current sliding window
            valid_timestamps = [ts for ts in timestamps if ts > cutoff]
            self._history[client_key] = valid_timestamps

            if len(valid_timestamps) >= self.max_requests:
                oldest = valid_timestamps[0]
                retry_after = int(self.window_seconds - (now - oldest)) + 1
                logger.warning(
                    f"Rate limit exceeded for '{client_key}' on '{self.name}': "
                    f"{len(valid_timestamps)}/{self.max_requests} in {self.window_seconds}s. Retry after {retry_after}s"
                )
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail=f"Rate limit exceeded on {self.name}. Please wait {retry_after} seconds before retrying.",
                    headers={"Retry-After": str(retry_after)},
                )

            # Record this request
            self._history[client_key].append(now)

    def _purge_stale(self, now: float) -> None:
        cutoff = now - (self.window_seconds * 2)
        keys_to_delete = [
            key for key, timestamps in self._history.items()
            if not timestamps or timestamps[-1] < cutoff
        ]
        for key in keys_to_delete:
            del self._history[key]


# Global rate limiter instances for sensitive operations
discover_limiter = RateLimiter(max_requests=10, window_seconds=60, name="discovery-pipeline")
chat_limiter = RateLimiter(max_requests=30, window_seconds=60, name="profile-chat")
upload_limiter = RateLimiter(max_requests=10, window_seconds=60, name="document-upload")
pdf_limiter = RateLimiter(max_requests=15, window_seconds=60, name="pdf-generation")
