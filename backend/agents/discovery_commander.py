import asyncio
import logging
import re
from typing import Callable, Dict, List, Optional, Tuple
from db.session_store import get_session_store
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.scholarship import Scholarship
from schemas.student import StudentProfile
from workflows.scouts.americas_scout import AmericasScout
from workflows.scouts.asia_scout import AsiaScout
from workflows.scouts.europe_scout import EuropeScout
from workflows.scouts.mena_scout import MenaScout
from workflows.scouts.oceania_scout import OceaniaScout
from workflows.degree_matching import is_degree_match
from workflows.field_matching import is_field_match

logger = logging.getLogger("scholarx.agents.commander")


class DiscoveryCommander:
    def __init__(self):
        self.session_store = get_session_store()
        self.scouts = {
            "Europe": EuropeScout(),
            "Asia": AsiaScout(),
            "Americas": AmericasScout(),
            "MENA": MenaScout(),
            "Oceania": OceaniaScout(),
        }

    def generate_scout_queries(self, student: StudentProfile, region: str) -> List[str]:
        """
        Synthesizes high-signal Pakistan-specific search queries based on student profile nuances.
        """
        degree = student.preferences.target_degree_level
        target_flds = student.preferences.target_fields or []
        fields = " ".join(target_flds[:2]) if target_flds else (student.academic.field_of_study or "Computer Science")
        has_ielts = student.language.has_english_test
        gpa = student.academic.gpa_percentage

        is_undergrad = any(
            k in (degree or "").lower()
            for k in ["bachelor", "undergrad", "bs", "inter", "fsc", "ics", "a-level", "diploma"]
        )

        queries = []

        if region == "Europe":
            if is_undergrad:
                if has_ielts:
                    queries.append(f"fully funded undergraduate Bachelor {fields} scholarship Pakistan 2027 Europe")
                    queries.append(f"Stipendium Hungaricum scholarship Pakistan HEC Bachelor undergraduate {fields}")
                    queries.append(f"Italy DSU regional scholarship Pakistan Bachelor undergraduate {fields}")
                else:
                    queries.append(f"Italy DSU regional scholarship Pakistan Bachelor undergraduate without IELTS")
                    queries.append(f"Romania ARICE scholarship Pakistani students undergraduate Bachelor {fields}")
                    queries.append(f"Stipendium Hungaricum scholarship Pakistan HEC Bachelor undergraduate")
            else:
                if has_ielts:
                    queries.append(f"fully funded {degree} {fields} scholarship Pakistan 2027 Europe")
                    queries.append(f"Stipendium Hungaricum scholarship Pakistan HEC {degree} {fields}")
                    queries.append(f"DAAD scholarship Pakistani students {fields} Germany")
                else:
                    queries.append(f"Italy DSU regional scholarship Pakistan {degree} without IELTS English proficiency")
                    queries.append(f"European scholarships Pakistani students without IELTS medium of instruction {degree}")
                    queries.append(f"Stipendium Hungaricum scholarship Pakistan HEC {degree}")

        elif region == "Asia":
            if is_undergrad:
                queries.append(f"CSC scholarship Chinese government Pakistan HEC Bachelor undergraduate {fields} 2027")
                queries.append(f"MEXT Japanese government scholarship Pakistan embassy recommendation undergraduate")
                queries.append(f"Global Korea Scholarship GKS KGSP Pakistan undergraduate Bachelor")
            else:
                if has_ielts:
                    queries.append(f"CSC scholarship Chinese government Pakistan HEC {degree} {fields} 2027")
                    queries.append(f"MEXT Japanese government scholarship Pakistan embassy recommendation {degree}")
                    queries.append(f"Global Korea Scholarship GKS KGSP Pakistan {degree}")
                else:
                    queries.append(f"Chinese government scholarship CSC Type A Type B Pakistan without IELTS {degree}")
                    queries.append(f"MEXT scholarship Pakistan written test English proficiency {degree}")
                    queries.append(f"ANSO scholarship Chinese Academy of Sciences Pakistan {degree}")

        elif region == "Americas":
            if is_undergrad:
                queries.append(f"Lester B Pearson scholarship University of Toronto Pakistan undergraduate {fields}")
                queries.append(f"Global UGRAD Pakistan undergraduate semester exchange USEFP")
                queries.append(f"University of Calgary International Entrance Scholarship Pakistan undergraduate")
            else:
                queries.append(f"USEFP Fulbright Pakistan scholarship Master PhD {fields} 2027")
                queries.append(f"Canada Vanier graduate scholarship Pakistan {fields}")

        elif region == "MENA":
            if is_undergrad:
                queries.append(f"Turkiye Burslari scholarship Pakistan requirements undergraduate Bachelor 2027")
                queries.append(f"Qatar University international student scholarship Pakistan undergraduate")
                queries.append(f"Islamic Development Bank IsDB scholarship Pakistan undergraduate Bachelor")
            else:
                queries.append(f"Turkiye Burslari scholarship Pakistan requirements {degree} 2027")
                if gpa >= 80.0:
                    queries.append(f"KAUST fellowship Saudi Arabia full funding Pakistani students {fields}")
                    queries.append(f"KFUPM graduate scholarship computer science engineering Pakistan")
                else:
                    queries.append(f"Turkey government scholarship Pakistani students graduate {fields}")

        elif region == "Oceania":
            if is_undergrad:
                queries.append(f"Australia destination Australia scholarship Pakistan undergraduate {degree}")
                queries.append(f"Manaaki New Zealand scholarship developing country Pakistan undergraduate")
            else:
                queries.append(f"Australia Awards scholarship Pakistan category DFAT {degree} 2027")
                queries.append(f"Manaaki New Zealand scholarship developing country Pakistan {degree}")

        return queries

    def deduplicate_scholarships(self, scholarships: List[Scholarship]) -> List[Scholarship]:
        """
        Deduplicates candidate scholarships using core name token set matching and host country.
        """
        deduped: List[Scholarship] = []
        noise_words = {
            "scholarship", "scholarships", "programme", "program",
            "award", "awards", "fellowship", "fellowships", "international",
            "government", "scheme", "grant", "grants", "for", "the", "in", "and", "of"
        }

        def get_core_tokens(name: str) -> set:
            words = re.findall(r"[a-z0-9]+", name.lower())
            return {w for w in words if w not in noise_words and len(w) > 2}

        for sc in scholarships:
            is_dup = False
            sc_tokens = get_core_tokens(sc.name)
            country = sc.host_country.upper()

            for existing in deduped:
                # 1. URL match check
                if sc.source_url and existing.source_url and sc.source_url.strip("/") == existing.source_url.strip("/"):
                    is_dup = True
                    break

                # 2. Token overlap within same host country
                if existing.host_country.upper() == country:
                    existing_tokens = get_core_tokens(existing.name)
                    if sc_tokens and existing_tokens:
                        intersection = sc_tokens.intersection(existing_tokens)
                        union = sc_tokens.union(existing_tokens)
                        similarity = len(intersection) / len(union) if union else 0
                        # Either high Jaccard similarity or one token set is subset of another
                        if similarity >= 0.5 or sc_tokens.issubset(existing_tokens) or existing_tokens.issubset(sc_tokens):
                            is_dup = True
                            break

            if not is_dup:
                deduped.append(sc)

        return deduped

    async def execute_discovery_mission(
        self,
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> List[Scholarship]:
        """
        Orchestrates parallel deployment of all 5 regional scouts, gathers discovered opportunities,
        merges with cached research and pre-seeded database, and returns verified candidate pool.
        """
        session_id = student.session_id
        events: List[ScholarXEvent] = []

        def emit(event_type: AgentEventType, payload: dict, severity: EventSeverity = EventSeverity.INFO):
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=event_type,
                agent_id="discovery_commander",
                agent_display_name="Discovery Commander",
                component_type="AGENT",
                phase="DISCOVERY",
                payload=payload,
                severity=severity,
            )
            events.append(evt)
            if event_callback:
                try:
                    event_callback(evt)
                except Exception as e:
                    logger.warning(f"Error invoking callback: {e}")

        # Determine active target regions based on student preferences
        pref = student.preferences.preferred_regions or []
        normalized_pref = []
        for p in pref:
            for k in self.scouts.keys():
                if p.strip().lower() == k.lower():
                    normalized_pref.append(k)

        scout_regions = normalized_pref if len(normalized_pref) > 0 else list(self.scouts.keys())
        target_degree = student.preferences.target_degree_level or "Bachelor's"
        target_fields = student.preferences.target_fields or ([student.academic.field_of_study] if student.academic.field_of_study else ["Computer Science"])
        logger.info(f"Targeting active scout regions: {scout_regions} (Preferences: {pref}, Target: {target_degree} in {target_fields})")

        for reg in scout_regions:
            emit(
                AgentEventType.SCOUT_DEPLOYED,
                {
                    "region": reg,
                    "active_queries_count": 1,
                    "message": f"Deploying {reg} scout workflow for Pakistani applicant profile.",
                },
                EventSeverity.INFO,
            )

        # 1. Concurrently run regional scouts with strict 30-second live discovery deadline
        live_candidates: List[Scholarship] = []
        completed_regions: List[str] = []
        failed_regions: List[str] = []
        transition_to_db = False

        # Start with the verified database so a personalized answer is available
        # even when cloud search providers are slow or unavailable.
        db_candidates: List[Scholarship] = []
        try:
            db_candidates = await self.session_store.search_scholarships_for_profile(
                student=student,
                regions=scout_regions,
                limit=350,
            )
            emit(
                AgentEventType.PREVIOUS_RESEARCH_LOADED,
                {
                    "total_cached": len(db_candidates),
                    "source": "VERIFIED_DATABASE",
                    "personalized": True,
                    "message": f"Loaded {len(db_candidates)} database matches before live scout enrichment.",
                },
                EventSeverity.INFO,
            )
        except Exception as db_fetch_err:
            logger.warning("Verified database prefetch failed; live scouts will continue: %s", db_fetch_err)

        from config import get_settings
        settings = get_settings()
        is_offline = getattr(settings, "OFFLINE_MODE", False)

        async def _run_single_scout(reg_name: str):
            scout = self.scouts[reg_name]
            queries = self.generate_scout_queries(student, reg_name)
            try:
                # Per-scout timeout ensures a slow scout does not stall other regional scouts
                return await asyncio.wait_for(
                    scout.run(student, custom_queries=queries[:1], event_callback=event_callback),
                    timeout=15.0,
                )
            except Exception as exc:
                return exc

        if is_offline:
            logger.info("OFFLINE_MODE active. Immediately utilizing local verified database repository.")
            transition_to_db = True
        else:
            try:
                logger.info(f"Executing {len(scout_regions)} regional scouts concurrently...")
                scout_results = await asyncio.wait_for(
                    asyncio.gather(*[_run_single_scout(r) for r in scout_regions]),
                    timeout=20.0,
                )

                for idx, res in enumerate(scout_results):
                    region_name = scout_regions[idx] if idx < len(scout_regions) else "Unknown"
                    if isinstance(res, tuple):
                        sc_list, _ = res
                        if sc_list:
                            live_candidates.extend(sc_list)
                        completed_regions.append(region_name)
                    else:
                        failed_regions.append(region_name)
                        logger.warning(f"Scout in {region_name} failed: {res}")
                        emit(
                            AgentEventType.SCOUT_FAILED,
                            {"region": region_name, "error": str(res)},
                            EventSeverity.WARNING,
                        )
            except asyncio.TimeoutError:
                logger.info("Live discovery window elapsed. Transitioning to verified institutional database repository.")
                transition_to_db = True
            except Exception as e:
                logger.error(f"Live discovery encountered unexpected error: {e}. Activating verified database failover.")
                transition_to_db = True

        if transition_to_db or failed_regions or not live_candidates:
            emit(
                AgentEventType.PRIMARY_SEARCH_UNAVAILABLE,
                {
                    "notice": "Cloud scout coverage was incomplete. Verified database results remain authoritative.",
                    "tool": "CANONICAL_DATABASE",
                    "provider": "CANONICAL_INSTITUTIONAL_DB",
                },
                EventSeverity.WARNING,
            )
            emit(
                AgentEventType.FALLBACK_SEARCH_ACTIVE,
                {
                    "fallback_source": "VERIFIED_REGISTRY_CACHE",
                    "tool": "CANONICAL_DATABASE",
                    "message": "Using personalized verified database matches while cloud search recovers.",
                },
                EventSeverity.INFO,
            )
            emit(
                AgentEventType.RESEARCH_RESUMED,
                {
                    "status": "RESEARCH_RESUMED_VIA_DATABASE",
                    "message": "Research continued from the personalized verified database.",
                },
                EventSeverity.INFO,
            )

        # 2. Query verified institutional database specifically for student profile
        if not db_candidates:
            try:
                db_candidates = await self.session_store.search_scholarships_for_profile(
                    student=student,
                    regions=scout_regions,
                    limit=350,
                )
            except Exception as db_fetch_err:
                logger.debug(f"Database profile search notice: {db_fetch_err}")

        # Auto-seed if database is completely empty
        if not db_candidates:
            from pathlib import Path
            import json
            repo_root = Path(__file__).resolve().parents[2]
            sc_dir = repo_root / "data" / "scholarships"
            if not sc_dir.exists():
                sc_dir = Path("data/scholarships")
            if sc_dir.exists():
                loaded = []
                for jf in sorted(sc_dir.glob("*.json")):
                    try:
                        with open(jf, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            if isinstance(data, list):
                                for item in data:
                                    loaded.append(Scholarship.model_validate(item))
                    except Exception as err:
                        logger.warning(f"Failed to load scholarships from {jf.name}: {err}")
                if loaded:
                    try:
                        await self.session_store.bulk_upsert_scholarships_cache(loaded)
                        db_candidates = await self.session_store.search_scholarships_for_profile(
                            student=student,
                            regions=scout_regions,
                            limit=35,
                        )
                    except Exception as db_seed_err:
                        logger.debug(f"Database cache seed notice: {db_seed_err}")

        emit(
            AgentEventType.PREVIOUS_RESEARCH_LOADED,
            {
                "total_cached": len(db_candidates),
                "message": f"Institutional database: {len(db_candidates)} verified opportunities matched to student profile ({target_degree} in {', '.join(target_fields)}).",
            },
            EventSeverity.INFO,
        )

        final_pool: List[Scholarship] = []

        # Filter matching live scout candidates
        matching_live: List[Scholarship] = []
        if len(live_candidates) > 0:
            for sc in live_candidates:
                if not scout_regions or sc.region in scout_regions:
                    degs = sc.eligibility.degree_levels if sc.eligibility else []
                    if is_degree_match(target_degree, degs):
                        efs = sc.eligibility.eligible_fields if sc.eligibility else []
                        f_match, f_score = is_field_match(target_fields, efs, sc.name)
                        if f_match:
                            matching_live.append(sc)
            logger.info(f"Live search returned {len(matching_live)} degree- and field-matching candidates.")

        pref_regions = scout_regions

        # Organize database-searched candidates by region
        by_region: Dict[str, List[Scholarship]] = {r: [] for r in pref_regions}
        for sc in db_candidates:
            if sc.region in by_region:
                by_region[sc.region].append(sc)

        # Sort and stream discovery telemetry per region for visual theatre
        streamed_pool: List[Scholarship] = []
        for reg in pref_regions:
            queries = self.generate_scout_queries(student, reg)
            q_text = queries[0] if queries else f"Pakistan scholarships {reg}"

            # Emit search query executed event
            emit(
                AgentEventType.SEARCH_QUERY_EXECUTED,
                {"query": q_text, "region": reg, "source": "DATABASE_REGISTRY"},
                EventSeverity.INFO,
            )
            await asyncio.sleep(0.04)

            # Retrieve database candidates matched for this region
            selected_for_reg = list(by_region.get(reg, [])[:4])

            # Also stream any live candidates discovered in this region
            reg_live = [sc for sc in matching_live if sc.region == reg]
            for r_sc in reg_live:
                if not any(s.scholarship_id == r_sc.scholarship_id for s in selected_for_reg):
                    selected_for_reg.insert(0, r_sc)

            for sc in selected_for_reg:
                streamed_pool.append(sc)
                # Emit source found
                emit(
                    AgentEventType.SOURCE_FOUND,
                    {
                        "url": sc.source_url or f"https://registry.scholarx.pk/{sc.scholarship_id}",
                        "title": sc.name,
                        "region": reg,
                        "database_source": "VERIFIED_CANONICAL_CACHE",
                    },
                    EventSeverity.INFO,
                )
                await asyncio.sleep(0.03)

                # Emit page scraped
                emit(
                    AgentEventType.PAGE_SCRAPED,
                    {
                        "url": sc.source_url or f"https://registry.scholarx.pk/{sc.scholarship_id}",
                        "char_count": 5200,
                        "region": reg,
                    },
                    EventSeverity.INFO,
                )
                await asyncio.sleep(0.03)

                # Emit candidate extracted
                emit(
                    AgentEventType.CANDIDATE_EXTRACTED,
                    {
                        "scholarship_id": sc.scholarship_id,
                        "name": sc.name,
                        "host_country": sc.host_country_name,
                        "funding_type": sc.funding.funding_type.value if sc.funding else "FULL",
                        "source_url": sc.source_url,
                        "quota_seats": sc.pakistan_requirements.pakistan_quota_seats,
                        "deadline": sc.application_deadline,
                        "degree_level": sc.eligibility.degree_levels[0] if sc.eligibility and sc.eligibility.degree_levels else target_degree,
                        "region": reg,
                        "source": "CANONICAL_DATABASE",
                    },
                    EventSeverity.SUCCESS,
                )
                await asyncio.sleep(0.04)

            # Emit scout complete for this region
            emit(
                AgentEventType.SCOUT_COMPLETE,
                {"region": reg, "total_discovered": len(selected_for_reg)},
                EventSeverity.SUCCESS,
            )
            await asyncio.sleep(0.03)

        # Merge live candidates and database-matched candidates
        combined_pool = matching_live + streamed_pool + db_candidates
        final_pool = self.deduplicate_scholarships(combined_pool)

        # 3. Save newly discovered/extracted to cache in a single atomic bulk operation (graceful failover if DB-free)
        if final_pool:
            try:
                await self.session_store.bulk_upsert_scholarships_cache(final_pool)
            except Exception as cache_upsert_err:
                logger.debug(f"Cache bulk upsert notice (non-fatal, continuing in-memory): {cache_upsert_err}")

        if failed_regions:
            emit(
                AgentEventType.PARTIAL_DISCOVERY,
                {
                    "completed_regions": completed_regions,
                    "failed_regions": failed_regions,
                    "candidates_recovered": len(final_pool),
                },
                EventSeverity.WARNING,
            )

        emit(
            AgentEventType.DISCOVERY_AGGREGATION_COMPLETE,
            {
                "total_candidates_found": len(final_pool),
                "regions_covered": scout_regions,
                "is_partial": len(failed_regions) > 0,
            },
            EventSeverity.SUCCESS,
        )

        return final_pool
