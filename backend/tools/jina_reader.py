import logging
from typing import Optional
import httpx
from utils.api_keys import get_key_manager

logger = logging.getLogger("scholarx.tools.jina")


class JinaReaderTool:
    def __init__(self):
        self.key_manager = get_key_manager()
        self.base_url = "https://r.jina.ai/"

    async def read_url(self, url: str) -> str:
        """
        Converts any URL directly to LLM-ready markdown using Jina Reader API.
        """
        jina_url = f"{self.base_url}{url}"
        headers = {
            "Accept": "text/markdown",
            "X-With-Generated-Alt": "true",
        }
        
        try:
            api_key = await self.key_manager.jina.get_key()
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"
        except Exception:
            pass

        try:
            async with httpx.AsyncClient(timeout=25.0) as client:
                response = await client.get(jina_url, headers=headers)
                if response.status_code == 200:
                    return response.text
                logger.warning(f"Jina Reader returned status {response.status_code} for {url}")
        except Exception as e:
            logger.warning(f"Jina Reader failed for {url}: {e}")

        # Direct HTTP fallback if Jina fails
        try:
            async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                resp = await client.get(url, headers=headers)
                if resp.status_code == 200:
                    return resp.text[:15000]
        except Exception as e:
            logger.error(f"Direct fallback fetch failed for {url}: {e}")

        return ""
