import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from tools.tavily_search import TavilySearchTool, SearchResultItem
from tools.firecrawl_scrape import FirecrawlScraperTool
from tools.jina_reader import JinaReaderTool


@pytest.mark.asyncio
async def test_search_result_item_model():
    item = SearchResultItem(
        title="Stipendium Hungaricum Scholarship",
        url="https://stipendiumhungaricum.hu",
        content="Full tuition and accommodation in Hungary for Pakistani students.",
        score=0.95,
    )
    assert item.title == "Stipendium Hungaricum Scholarship"
    assert item.url == "https://stipendiumhungaricum.hu"
    assert "Hungary" in item.content


@pytest.mark.asyncio
async def test_tavily_search_tool_mocked():
    tool = TavilySearchTool()

    mock_response = {
        "results": [
            {
                "title": "Stipendium Hungaricum 2027",
                "url": "https://stipendiumhungaricum.hu/apply",
                "content": "Official portal for Hungary scholarship programme. Open for Pakistan HEC.",
                "score": 0.98,
            }
        ]
    }

    with patch("tools.tavily_search.AsyncTavilyClient") as mock_client_cls:
        mock_instance = MagicMock()
        mock_instance.search = AsyncMock(return_value=mock_response)
        mock_client_cls.return_value = mock_instance

        results = await tool.search("scholarship Hungary Pakistan", max_results=5)
        assert len(results) == 1
        assert results[0].url == "https://stipendiumhungaricum.hu/apply"
        assert results[0].score == 0.98


@pytest.mark.asyncio
async def test_firecrawl_scrape_tool_mocked():
    tool = FirecrawlScraperTool()

    mock_scrape_res = {
        "markdown": "# Hungarian Scholarship\nFull tuition waiver and dorms provided for Pakistani students.",
        "metadata": {"title": "Hungary Portal", "sourceURL": "https://stipendiumhungaricum.hu"},
    }

    with patch.object(tool, "_scrape_with_key", new_callable=AsyncMock) as mock_scrape:
        mock_scrape.return_value = mock_scrape_res["markdown"]
        content = await tool.scrape_url("https://stipendiumhungaricum.hu")
        assert "Hungarian Scholarship" in content
        assert "Pakistani students" in content


@pytest.mark.asyncio
async def test_jina_reader_tool_mocked():
    tool = JinaReaderTool()

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = "# DAAD Scholarship Germany\nFree tuition at public universities for Pakistanis."
        mock_get.return_value = mock_resp

        markdown = await tool.read_url("https://www.daad.de/en")
        assert "DAAD Scholarship Germany" in markdown
