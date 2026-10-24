import logging
from typing import Callable, List, Optional, Tuple
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.evidence import EvidenceTrail
from schemas.scholarship import Scholarship
from schemas.scoring import CompositeScoreResult, CostAnalysisResult, DeadlineAnalysisResult
from schemas.student import StudentProfile, EducationSystem
from workflows.degree_matching import get_degree_scholarship_limit
from workflows.eligibility import EligibilityResult
from workflows.field_matching import is_field_match

logger = logging.getLogger("scholarx.workflows.ranking")


class RankingEngine:
    """
    Deterministic Pakistan-Adjusted Weighted Composite Ranking Engine.
    Formula:
      Score = (0.25 * Eligibility) + (0.25 * Funding) + (0.10 * BilateralBonus) +
              (0.10 * AcademicFit) + (0.10 * DocReadiness) + (0.10 * Deadline) +
              (0.05 * Verification) + (0.05 * Competition)
    """

    def calculate_composite_score(
        self,
        scholarship: Scholarship,
        eligibility: EligibilityResult,
        cost: CostAnalysisResult,
        deadline: DeadlineAnalysisResult,
        evidence: EvidenceTrail,
        student: StudentProfile,
    ) -> CompositeScoreResult:
        # 1. Eligibility Match (25%)
        elig_score = float(eligibility.eligibility_score)

        # 2. True Funding Score (25%)
        funding_score = float(cost.funding_score)

        # 3. Pakistan Bilateral Bonus (10%)
        if scholarship.pakistan_requirements.pakistan_bilateral_quota:
            bilateral_score = 100.0
        elif scholarship.pakistan_requirements.pakistan_eligible:
            bilateral_score = 50.0
        else:
            bilateral_score = 0.0

        # Check Cambridge Education Stream
        is_cambridge = (
            student.academic.education_system == EducationSystem.CAMBRIDGE
            or bool(student.academic.a_level_grades and len(student.academic.a_level_grades) > 0)
        )

        # 4. Academic & Field Fit (10%)
        gpa_score = min(100.0, max(50.0, float(student.academic.gpa_percentage)))
        target_fields = student.preferences.target_fields or ([student.academic.field_of_study] if student.academic.field_of_study else [])
        efs = scholarship.eligibility.eligible_fields if scholarship.eligibility else []
        f_match, f_score = is_field_match(target_fields, efs, scholarship.name)
        academic_score = round(min(100.0, (0.5 * gpa_score) + (0.5 * (f_score * 100.0))), 1)

        # Cambridge International Curriculum Rigor Bonus (+6.0 on academic fit)
        # Reflects globally standardized CIE examination grading vs local board grade variations
        if is_cambridge:
            academic_score = round(min(100.0, academic_score + 6.0), 1)

        # 5. Document Readiness (10%)
        # Cambridge students have CIE Statement of Results & certificates directly verified without local BISE board delays
        doc_readiness_score = 80.0 if (student.academic.hec_attestation_done or is_cambridge) else 65.0
        if student.language.has_english_test:
            doc_readiness_score += 15.0

        # 6. Deadline Feasibility (10%)
        deadline_score = float(deadline.deadline_score)

        # 7. Verification Confidence (5%)
        verif_score = float(evidence.confidence_score * 100.0)

        # 8. Competition Factor (5%)
        comp_map = {"LOW": 95.0, "MODERATE": 80.0, "HIGH": 65.0, "EXTREME": 50.0}
        competition_score = comp_map.get(scholarship.competition_level or "MODERATE", 80.0)

        # 9. Cambridge International Qualification Direct-Entry Priority
        # Cambridge GCE A-Levels candidates possess direct international standing for hard/competitive destinations
        # (UK, Germany, Netherlands, Switzerland, Singapore, Canada, USA, Europe, Americas, Oceania)
        # where 12-year local FSc students face mandatory Studienkolleg or foundation-year barriers.
        cambridge_priority_bonus = 0.0
        dest_country = (scholarship.host_country_name or scholarship.host_country or "").upper()
        hard_countries = {
            "GB", "UNITED KINGDOM", "UK", "DE", "GERMANY", "NL", "NETHERLANDS",
            "CH", "SWITZERLAND", "SG", "SINGAPORE", "CA", "CANADA", "US", "UNITED STATES",
            "SE", "SWEDEN", "IE", "IRELAND", "AT", "AUSTRIA", "AU", "AUSTRALIA", "FR", "FRANCE"
        }
        if is_cambridge and (any(hc in dest_country for hc in hard_countries) or scholarship.region in ("Europe", "Americas", "Oceania")):
            cambridge_priority_bonus = 5.0

        # Weighted Composite Score
        composite = (
            (0.25 * elig_score)
            + (0.25 * funding_score)
            + (0.10 * bilateral_score)
            + (0.10 * academic_score)
            + (0.10 * doc_readiness_score)
            + (0.10 * deadline_score)
            + (0.05 * verif_score)
            + (0.05 * competition_score)
            + cambridge_priority_bonus
        )

        final_match_score = round(max(0.0, min(100.0, composite)), 1)
        if not eligibility.is_eligible:
            final_match_score = round(min(38.0, composite * 0.4), 1)
        is_recommended = eligibility.is_eligible and cost.is_within_budget and deadline.is_feasible

        # Compile advantages
        advantages = list(eligibility.pakistan_advantages)
        if is_cambridge and cambridge_priority_bonus > 0:
            direct_entry_note = (
                f"Cambridge GCE Direct Entry: Direct undergraduate admission priority in "
                f"{scholarship.host_country_name or scholarship.host_country} (exempt from 1-year preparatory college / Studienkolleg)."
            )
            if direct_entry_note not in advantages:
                advantages.append(direct_entry_note)

        return CompositeScoreResult(
            scholarship_id=scholarship.scholarship_id,
            scholarship_name=scholarship.name,
            overall_match_score=final_match_score,
            rank=1,
            eligibility_score=elig_score,
            true_funding_score=funding_score,
            bilateral_bonus_score=bilateral_score,
            academic_fit_score=academic_score,
            doc_readiness_score=doc_readiness_score,
            deadline_score=deadline_score,
            verification_score=verif_score,
            competition_score=competition_score,
            cost_analysis=cost,
            deadline_analysis=deadline,
            blocking_reasons=list(eligibility.blocking_issues),
            pakistan_specific_advantages=advantages,
            is_recommended=is_recommended,
        )

    def rank_opportunities(
        self,
        candidates_data: List[Tuple[Scholarship, EligibilityResult, CostAnalysisResult, DeadlineAnalysisResult, EvidenceTrail]],
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> List[CompositeScoreResult]:
        session_id = student.session_id
        scored_results: List[CompositeScoreResult] = []

        for sc, elig, cost, dl, ev in candidates_data:
            res = self.calculate_composite_score(sc, elig, cost, dl, ev, student)
            scored_results.append(res)

        sc_map = {sc.scholarship_id: sc for sc, _, _, _, _ in candidates_data}
        pref_regions = [r.strip().lower() for r in (student.preferences.preferred_regions if student.preferences else []) if r.strip()]
        excl_regions = [r.strip().lower() for r in (student.preferences.excluded_regions if student.preferences else []) if r.strip()]

        # Defense-in-depth: Filter out scholarships where composite score <= 50.0
        # and enforce zero tolerance for degree mismatches or excluded regions
        filtered_results = []
        for r in scored_results:
            if r.overall_match_score <= 50.0:
                continue
            if any("Target degree level" in b or "Degree mismatch" in b for b in r.blocking_reasons):
                continue
            sc = sc_map.get(r.scholarship_id)
            if sc:
                sc_reg = (sc.region or "").strip().lower()
                if sc_reg and excl_regions and sc_reg in excl_regions:
                    continue
                if sc_reg and pref_regions and sc_reg not in pref_regions:
                    continue
            filtered_results.append(r)

        logger.info(
            f"RankingEngine evaluated {len(scored_results)} candidates: retained {len(filtered_results)} "
            f"with composite match score > 50.0 (filtered out {len(scored_results) - len(filtered_results)} low-scoring)."
        )
        scored_results = filtered_results

        # Sort descending by overall match score
        scored_results.sort(key=lambda r: r.overall_match_score, reverse=True)

        # Enforce degree-specific output cap:
        # PhD -> 30, Master's -> 20, Bachelor's -> 15
        target_deg = student.preferences.target_degree_level if student.preferences else None
        output_limit = get_degree_scholarship_limit(target_deg)

        if len(scored_results) > output_limit:
            logger.info(
                f"RankingEngine: {len(scored_results)} scholarships qualified (>50.0) for target degree '{target_deg}'. "
                f"Capping to top {output_limit}; {len(scored_results) - output_limit} lower-ranked opportunities will not be shown."
            )
            scored_results = scored_results[:output_limit]

        # Assign ranks
        for idx, item in enumerate(scored_results):
            item.rank = idx + 1

        if event_callback and scored_results:
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=AgentEventType.RANKING_CALCULATED,
                agent_id="ranking_engine",
                agent_display_name="Ranking Engine",
                component_type="WORKFLOW",
                phase="RANKING",
                payload={
                    "total_ranked": len(scored_results),
                    "top_scholarship": scored_results[0].scholarship_name,
                    "top_score": scored_results[0].overall_match_score,
                    "ranked_results": [
                        {
                            "scholarship_id": r.scholarship_id,
                            "name": r.scholarship_name,
                            "host_country": sc_map[r.scholarship_id].host_country if r.scholarship_id in sc_map else None,
                            "host_country_name": sc_map[r.scholarship_id].host_country_name if r.scholarship_id in sc_map else None,
                            "region": sc_map[r.scholarship_id].region if r.scholarship_id in sc_map else None,
                            "source_url": sc_map[r.scholarship_id].source_url if r.scholarship_id in sc_map else None,
                            "portal_url": sc_map[r.scholarship_id].portal_url if r.scholarship_id in sc_map else None,
                            "official_portal_url": (sc_map[r.scholarship_id].portal_url or sc_map[r.scholarship_id].source_url) if r.scholarship_id in sc_map else None,
                            "eligible_fields": sc_map[r.scholarship_id].eligibility.eligible_fields if r.scholarship_id in sc_map and sc_map[r.scholarship_id].eligibility else [],
                            "overall_match_score": r.overall_match_score,
                            "rank": r.rank,
                            "factors": {
                                "eligibility": r.eligibility_score,
                                "funding": r.true_funding_score,
                                "bilateral_bonus": r.bilateral_bonus_score,
                                "academic_fit": r.academic_fit_score,
                                "doc_readiness": r.doc_readiness_score,
                                "deadline": r.deadline_score,
                                "verification": r.verification_score,
                                "competition": r.competition_score,
                            },
                            "blocking_reasons": r.blocking_reasons,
                            "advantages": r.pakistan_specific_advantages,
                            "is_recommended": r.is_recommended,
                        }
                        for r in scored_results
                    ],
                },
                severity=EventSeverity.SUCCESS,
            )
            try:
                event_callback(evt)
            except Exception as e:
                logger.warning(f"Failed to invoke event callback: {e}")

        return scored_results
