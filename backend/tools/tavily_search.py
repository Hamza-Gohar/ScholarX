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

                response = await client.search(**search_kwargs)
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
                status_code = 429 if ("429" in err_msg or "rate limit" in err_msg or "quota" in err_msg) else 500
                logger.warning(f"Tavily search attempt {attempts} failed with error: {exc}. Rotating key...")
                await self.key_manager.tavily.report_failure(api_key, error_code=status_code)

        logger.error(f"Failed to execute Tavily search after {max_attempts} attempts.")
        return []
