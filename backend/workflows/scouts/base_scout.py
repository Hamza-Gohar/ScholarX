import asyncio
import logging
from typing import Callable, List, Optional, Tuple
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.scholarship import Scholarship
from schemas.student import StudentProfile
from tools.extractor import ScholarshipExtractor
from tools.firecrawl_scrape import FirecrawlScraperTool
from tools.jina_reader import JinaReaderTool
from tools.tavily_search import TavilySearchTool
from workflows.degree_matching import is_degree_match

logger = logging.getLogger("scholarx.workflows.scout")


class BaseScout:
    region_name: str = "Global"
    default_domains: List[str] = []
    default_queries: List[str] = []

    def __init__(self, region: Optional[str] = None, region_name: Optional[str] = None):
        if region:
            self.region_name = region
        elif region_name:
            self.region_name = region_name
        self.search_tool = TavilySearchTool()
        self.firecrawl_tool = FirecrawlScraperTool()
        self.jina_tool = JinaReaderTool()
        self.extractor = ScholarshipExtractor()

    async def run_scout_pipeline(
        self,
        student: StudentProfile,
        queries: List[str],
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> Tuple[List[Scholarship], List[ScholarXEvent]]:
        """
        Deterministic scout pipeline execution:
        1. Deploy -> 2. Search -> 3. Filter -> 4. Scrape -> 5. Extract -> 6. Complete
        """
        session_id = student.session_id
        agent_id = f"{self.region_name.lower()}_scout"
        display_name = f"{self.region_name} Scout"
        events: List[ScholarXEvent] = []

        def emit(event_type: AgentEventType, payload: dict, severity: EventSeverity = EventSeverity.INFO):
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=event_type,
                agent_id=agent_id,
                agent_display_name=display_name,
                component_type="WORKFLOW",
                phase="DISCOVERY",
                payload=payload,
                severity=severity,
            )
            events.append(evt)
            if event_callback:
                try:
                    event_callback(evt)
                except Exception as e:
                    logger.warning(f"Error invoking event callback: {e}")

        emit(
            AgentEventType.SCOUT_DEPLOYED,
            {"region": self.region_name, "active_queries_count": len(queries)},
            EventSeverity.INFO,
        )

        discovered_scholarships: List[Scholarship] = []
        found_urls: set = set()
        target_deg = student.preferences.target_degree_level or "Bachelor's"

        try:
            # Step 1: Execute Tavily searches with failover
            for query in queries[:3]:  # Top 3 tailored queries
                emit(AgentEventType.SEARCH_QUERY_EXECUTED, {"query": query, "region": self.region_name})
                search_results = await self.search_tool.search(
                    query=query,
                    max_results=2,
                    include_domains=self.default_domains if self.default_domains else None,
                )

                # Tool failover check (§18, §57): if search returns 0 results, fall back to verified cache
                if not search_results:
                    emit(
                        AgentEventType.PRIMARY_SEARCH_UNAVAILABLE,
                        {
                            "provider": "Tavily",
                            "region": self.region_name,
                            "query": query,
                            "notice": "Primary search source unavailable. Transitioning to fallback intelligence.",
                        },
                        EventSeverity.WARNING,
                    )
                    emit(
                        AgentEventType.FALLBACK_SEARCH_ACTIVE,
                        {
                            "fallback_source": "VERIFIED_REGISTRY_CACHE",
                            "region": self.region_name,
                            "tool": "CANONICAL_DATABASE",
                        },
                        EventSeverity.INFO,
                    )

                    # Query local verified scholarships database for this region
                    from db.session_store import get_session_store
                    store = get_session_store()
                    regional_cached = await store.search_scholarships_for_profile(
                        student=student,
                        regions=[self.region_name],
                        limit=3,
                    )
                    target_deg = student.preferences.target_degree_level or "Bachelor's"

                    for sc in regional_cached[:2]:
                        if sc.scholarship_id not in [x.scholarship_id for x in discovered_scholarships]:
                            discovered_scholarships.append(sc)
                            emit(
                                AgentEventType.CANDIDATE_EXTRACTED,
                                {
                                    "scholarship_id": sc.scholarship_id,
                                    "name": sc.name,
                                    "host_country": sc.host_country_name,
                                    "funding_type": sc.funding.funding_type.value,
                                    "source": "VERIFIED_CACHE",
                                    "source_url": sc.source_url,
                                    "quota_seats": sc.pakistan_requirements.pakistan_quota_seats,
                                    "deadline": sc.application_deadline,
                                    "degree_level": sc.eligibility.degree_levels[0] if sc.eligibility.degree_levels else target_deg,
                                    "region": self.region_name,
                                },
                                EventSeverity.SUCCESS,
                            )

                    emit(
                        AgentEventType.RESEARCH_RESUMED,
                        {"region": self.region_name, "status": "RESEARCH_RESUMED_VIA_FALLBACK"},
                        EventSeverity.INFO,
                    )

                for result in search_results:
                    if result.url and result.url not in found_urls:
                        found_urls.add(result.url)
                        emit(
                            AgentEventType.SOURCE_FOUND,
                            {"url": result.url, "title": result.title, "relevance_score": result.score},
                        )

                        # Step 2: Scrape page content
                        scraped_text = ""
                        # Try Jina Reader first (fast), fallback to Firecrawl
                        try:
                            scraped_text = await self.jina_tool.read_url(result.url)
                        except Exception:
                            pass

                        if not scraped_text or len(scraped_text) < 150:
                            try:
                                scraped_text = await self.firecrawl_tool.scrape_url(result.url)
                            except Exception:
                                pass

                        # If still empty, use snippet from search
                        if not scraped_text:
                            scraped_text = f"# {result.title}\n{result.content}"

                        emit(
                            AgentEventType.PAGE_SCRAPED,
                            {"url": result.url, "char_count": len(scraped_text)},
                        )

                        # Step 3: Extract structured scholarship data
                        try:
                            sc = await self.extractor.extract_scholarship(
                                raw_text=scraped_text,
                                source_url=result.url,
                                region=self.region_name,
                            )
                            if sc and sc.pakistan_requirements.pakistan_eligible and is_degree_match(target_deg, sc.eligibility.degree_levels if sc.eligibility else []):
                                discovered_scholarships.append(sc)
                                emit(
                                    AgentEventType.CANDIDATE_EXTRACTED,
                                    {
                                        "scholarship_id": sc.scholarship_id,
                                        "name": sc.name,
                                        "host_country": sc.host_country_name,
                                        "funding_type": sc.funding.funding_type.value,
                                        "source_url": sc.source_url,
                                        "quota_seats": sc.pakistan_requirements.pakistan_quota_seats,
                                        "deadline": sc.application_deadline,
                                        "degree_level": sc.eligibility.degree_levels[0] if sc.eligibility.degree_levels else "Bachelor's",
                                        "region": self.region_name,
                                    },
                                    EventSeverity.SUCCESS,
                                )
                        except Exception as exc:
                            logger.warning(f"Extraction failed for {result.url}: {exc}")

            emit(
                AgentEventType.SCOUT_COMPLETE,
                {"region": self.region_name, "total_discovered": len(discovered_scholarships)},
                EventSeverity.SUCCESS,
            )

        except Exception as scout_err:
            logger.error(f"Scout workflow fault in {self.region_name}: {scout_err}", exc_info=True)
            emit(
                AgentEventType.SCOUT_FAILED,
                {
                    "region": self.region_name,
                    "error": str(scout_err),
                    "status": "UNAVAILABLE",
                    "notice": f"{self.region_name} Scout encountered an error. Regional impact isolated.",
                },
                EventSeverity.WARNING,
            )

        return discovered_scholarships, events

    async def run(
        self,
        student: StudentProfile,
        custom_queries: Optional[List[str]] = None,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> Tuple[List[Scholarship], List[ScholarXEvent]]:
        queries = custom_queries if custom_queries else self.default_queries
        return await self.run_scout_pipeline(student, queries, event_callback)
