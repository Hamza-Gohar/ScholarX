import pytest
from unittest.mock import AsyncMock, patch
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import Scholarship, ScholarshipStatus, FundingDetails, PakistanSpecificRequirements
from schemas.student import StudentProfile
from tools.tavily_search import SearchResultItem
from workflows.scouts.base_scout import BaseScout
from workflows.scouts.europe_scout import EuropeScout
from workflows.scouts.asia_scout import AsiaScout
from workflows.scouts.americas_scout import AmericasScout
from workflows.scouts.mena_scout import MenaScout
from workflows.scouts.oceania_scout import OceaniaScout


@pytest.fixture
def sample_student():
    return StudentProfile(
        student_id="std-test-scout",
        session_id="sess-test-scout",
        academic={"current_level": "Intermediate / ICS / FSc / FA", "field_of_study": "Computer Science", "gpa_percentage": 87.0},
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science", "Artificial Intelligence"]},
    )


@pytest.mark.asyncio
async def test_all_scout_configurations():
    """Validates that all 5 regional scout classes are properly configured with distinct regions, domains, and queries."""
    scouts = {
        "Europe": EuropeScout(),
        "Asia": AsiaScout(),
        "Americas": AmericasScout(),
        "MENA": MenaScout(),
        "Oceania": OceaniaScout(),
    }

    for region, scout in scouts.items():
        assert scout.region_name == region
        assert len(scout.default_domains) >= 3
        assert len(scout.default_queries) >= 3
        assert any("Pakistan" in q or "Pakistani" in q for q in scout.default_queries)


@pytest.mark.asyncio
async def test_base_scout_pipeline_jina_success(sample_student):
    """Tests complete deterministic pipeline when Jina Reader succeeds."""
    scout = EuropeScout()
    events = []

    def on_event(e: ScholarXEvent):
        events.append(e)

    mock_search_result = SearchResultItem(
        title="Stipendium Hungaricum Programme for Pakistan",
        url="https://stipendiumhungaricum.hu/apply-pk",
        content="Full scholarship covering tuition, dorms, and monthly stipend for Pakistani students.",
        score=0.95,
    )

    mock_scholarship = Scholarship(
        scholarship_id="SCH-TEST-001",
        name="Stipendium Hungaricum Test",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu/apply-pk",
        status=ScholarshipStatus.DISCOVERED,
        funding=FundingDetails(tuition="100% Free Tuition"),
        pakistan_requirements=PakistanSpecificRequirements(pakistan_eligible=True),
    )

    scout.search_tool.search = AsyncMock(return_value=[mock_search_result])
    scout.jina_tool.read_url = AsyncMock(return_value="Detailed markdown content about Stipendium Hungaricum for Pakistan..." * 10)
    scout.extractor.extract_scholarship = AsyncMock(return_value=mock_scholarship)

    scholarships, emitted = await scout.run(
        student=sample_student,
        custom_queries=["Stipendium Hungaricum Pakistan 2027"],
        event_callback=on_event,
    )

    assert len(scholarships) == 1
    assert scholarships[0].scholarship_id == "SCH-TEST-001"
    assert scholarships[0].name == "Stipendium Hungaricum Test"

    # Verify event trail
    event_types = [e.event_type for e in events]
    assert AgentEventType.SCOUT_DEPLOYED in event_types
    assert AgentEventType.SEARCH_QUERY_EXECUTED in event_types
    assert AgentEventType.SOURCE_FOUND in event_types
    assert AgentEventType.PAGE_SCRAPED in event_types
    assert AgentEventType.CANDIDATE_EXTRACTED in event_types
    assert AgentEventType.SCOUT_COMPLETE in event_types


@pytest.mark.asyncio
async def test_base_scout_pipeline_firecrawl_fallback(sample_student):
    """Tests pipeline fallback to Firecrawl when Jina Reader fails."""
    scout = AsiaScout()
    events = []

    mock_search_result = SearchResultItem(
        title="Chinese Government Scholarship CSC",
        url="https://campuschina.org/csc-pk",
        content="CSC scholarship for Pakistani students.",
        score=0.92,
    )

    mock_scholarship = Scholarship(
        scholarship_id="SCH-TEST-CSC",
        name="CSC Scholarship Test",
        host_country="CN",
        host_country_name="China",
        region="Asia",
        source_url="https://campuschina.org/csc-pk",
        status=ScholarshipStatus.DISCOVERED,
        pakistan_requirements=PakistanSpecificRequirements(pakistan_eligible=True),
    )

    scout.search_tool.search = AsyncMock(return_value=[mock_search_result])
    scout.jina_tool.read_url = AsyncMock(side_effect=Exception("Jina Rate Limit"))
    scout.firecrawl_tool.scrape_url = AsyncMock(return_value="Scraped page content from Firecrawl markdown engine..." * 10)
    scout.extractor.extract_scholarship = AsyncMock(return_value=mock_scholarship)

    scholarships, emitted = await scout.run(
        student=sample_student,
        custom_queries=["CSC Scholarship Pakistan 2027"],
        event_callback=lambda e: events.append(e),
    )

    assert len(scholarships) == 1
    assert scholarships[0].host_country == "CN"
    scout.firecrawl_tool.scrape_url.assert_called_once_with("https://campuschina.org/csc-pk")


@pytest.mark.asyncio
async def test_base_scout_pipeline_snippet_fallback(sample_student):
    """Tests pipeline fallback to search snippet when both Jina and Firecrawl fail."""
    scout = AmericasScout()
    events = []

    mock_search_result = SearchResultItem(
        title="Fulbright Pakistan Program",
        url="https://usefp.org/fulbright",
        content="USEFP Fulbright full funding for Pakistani scholars.",
        score=0.99,
    )

    mock_scholarship = Scholarship(
        scholarship_id="SCH-TEST-FULBRIGHT",
        name="Fulbright Pakistan Test",
        host_country="US",
        host_country_name="United States",
        region="Americas",
        source_url="https://usefp.org/fulbright",
        status=ScholarshipStatus.DISCOVERED,
        pakistan_requirements=PakistanSpecificRequirements(pakistan_eligible=True),
    )

    scout.search_tool.search = AsyncMock(return_value=[mock_search_result])
    scout.jina_tool.read_url = AsyncMock(side_effect=Exception("Jina error"))
    scout.firecrawl_tool.scrape_url = AsyncMock(side_effect=Exception("Firecrawl error"))
    scout.extractor.extract_scholarship = AsyncMock(return_value=mock_scholarship)

    scholarships, emitted = await scout.run(
        student=sample_student,
        custom_queries=["Fulbright Pakistan 2027"],
        event_callback=lambda e: events.append(e),
    )

    assert len(scholarships) == 1
    scout.extractor.extract_scholarship.assert_called_once()
    call_args = scout.extractor.extract_scholarship.call_args[1]
    assert "USEFP Fulbright full funding" in call_args["raw_text"]


@pytest.mark.asyncio
async def test_base_scout_non_pakistan_filtered(sample_student):
    """Ensures opportunities where Pakistani students are not eligible are rejected from the candidate pool."""
    scout = MenaScout()

    mock_search_result = SearchResultItem(
        title="Domestic Only University Award",
        url="https://domestic.sa/award",
        content="Scholarship for domestic residents only.",
        score=0.85,
    )

    mock_scholarship = Scholarship(
        scholarship_id="SCH-NON-PK",
        name="Domestic Scholarship",
        host_country="SA",
        host_country_name="Saudi Arabia",
        region="MENA",
        source_url="https://domestic.sa/award",
        status=ScholarshipStatus.DISCOVERED,
        pakistan_requirements=PakistanSpecificRequirements(pakistan_eligible=False),
    )

    scout.search_tool.search = AsyncMock(return_value=[mock_search_result])
    scout.jina_tool.read_url = AsyncMock(return_value="Some text...")
    scout.extractor.extract_scholarship = AsyncMock(return_value=mock_scholarship)

    scholarships, emitted = await scout.run(
        student=sample_student,
        custom_queries=["Saudi scholarships"],
    )

    assert len(scholarships) == 0


@pytest.mark.asyncio
async def test_scout_default_queries_execution(sample_student):
    """Tests that scout runs default queries if custom queries are not provided."""
    scout = OceaniaScout()
    scout.search_tool.search = AsyncMock(return_value=[])

    scholarships, emitted = await scout.run(student=sample_student)

    assert scout.search_tool.search.call_count == min(3, len(scout.default_queries))
