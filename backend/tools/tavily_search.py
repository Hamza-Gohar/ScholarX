import logging
from typing import Any, Dict, List, Optional
import httpx
from pydantic import BaseModel, Field
from tavily import AsyncTavilyClient
from utils.api_keys import get_key_manager, AllKeysExhaustedError

logger = logging.getLogger("scholarx.tools.tavily")


class SearchResultItem(BaseModel):
    title: str = Field(default="")
    url: str = Field(...)
    content: str = Field(default="")
    score: float = Field(default=0.8)
    raw_content: Optional[str] = None


class TavilySearchTool:
    def __init__(self):
        self.key_manager = get_key_manager()

    async def search(
        self,
        query: str,
        max_results: int = 7,
        include_domains: Optional[List[str]] = None,
        search_depth: str = "advanced",
    ) -> List[SearchResultItem]:
        """
        Executes web search using Tavily API with automatic multi-key rotation and failover.
        """
        from config import get_settings
        settings = get_settings()
        if getattr(settings, "OFFLINE_MODE", False) or self.key_manager.tavily.total_keys == 0:
            logger.info("Offline mode active or no Tavily keys configured; skipping live web search.")
            return []

        attempts = 0
        max_attempts = max(1, self.key_manager.tavily.total_keys)

        while attempts < max_attempts:
            attempts += 1
            try:
                api_key = await self.key_manager.tavily.get_key()
            except AllKeysExhaustedError as e:
                logger.error(f"All Tavily keys exhausted: {e}")
                return []

            try:
                client = AsyncTavilyClient(api_key=api_key)
                search_kwargs: Dict[str, Any] = {
                    "query": query,
                    "max_results": max_results,
                    "search_depth": search_depth,
                }
                if include_domains:
                    search_kwargs["include_domains"] = include_domains

                import asyncio
                response = await asyncio.wait_for(client.search(**search_kwargs), timeout=3.5)
                await self.key_manager.tavily.report_success(api_key)

                results: List[SearchResultItem] = []
                raw_results = response.get("results", []) if isinstance(response, dict) else []
                for item in raw_results:
                    results.append(
                        SearchResultItem(
                            title=item.get("title", ""),
                            url=item.get("url", ""),
                            content=item.get("content", ""),
                            score=float(item.get("score", 0.8)),
                            raw_content=item.get("raw_content"),
                        )
                    )
                return results

            except Exception as exc:
                err_msg = str(exc).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                status_code = 429 if ("429" in err_msg or "rate limit" in err_msg or "quota" in err_msg) else 500
                logger.warning(f"Tavily search attempt {attempts} failed with error: {exc}.")
                await self.key_manager.tavily.report_failure(api_key, error_code=status_code)

                # If connection / network error (no internet or offline), don't waste time rotating keys
                if is_net_error:
                    logger.info("Network connection unavailable. Transitioning immediately to offline database retrieval.")
                    break

        logger.info(f"Tavily search completed with fallback after {attempts} attempts.")
        return []
