import asyncio
import logging
from typing import Any, Dict, Optional
import httpx
from utils.api_keys import get_key_manager, AllKeysExhaustedError

logger = logging.getLogger("scholarx.tools.firecrawl")


class FirecrawlScraperTool:
    def __init__(self):
        self.key_manager = get_key_manager()
        self.endpoint = "https://api.firecrawl.dev/v1/scrape"

    async def _scrape_with_key(self, url: str, api_key: str) -> str:
        async with httpx.AsyncClient(timeout=3.5) as client:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "url": url,
                "formats": ["markdown"],
                "onlyMainContent": True,
            }
            response = await client.post(self.endpoint, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    return data.get("data", {}).get("markdown", "")
                return data.get("markdown", "")
            else:
                response.raise_for_status()
                return ""

    async def scrape_url(self, url: str) -> str:
        """
        Deep-scrapes a webpage and converts it into clean markdown via Firecrawl API with multi-key failover.
        """
        from config import get_settings
        settings = get_settings()
        if getattr(settings, "OFFLINE_MODE", False) or self.key_manager.firecrawl.total_keys == 0:
            return ""

        attempts = 0
        max_attempts = max(1, self.key_manager.firecrawl.total_keys)

        while attempts < max_attempts:
            attempts += 1
            try:
                api_key = await self.key_manager.firecrawl.get_key()
            except AllKeysExhaustedError as e:
                logger.error(f"All Firecrawl keys exhausted: {e}")
                return ""

            try:
                markdown = await self._scrape_with_key(url, api_key)
                await self.key_manager.firecrawl.report_success(api_key)
                return markdown
            except Exception as exc:
                err_msg = str(exc).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                status_code = 429 if ("429" in err_msg or "rate limit" in err_msg or "quota" in err_msg) else 500
                logger.warning(f"Firecrawl scrape attempt {attempts} failed for {url}: {exc}.")
                await self.key_manager.firecrawl.report_failure(api_key, error_code=status_code)
                if is_net_error:
                    break

        return ""
