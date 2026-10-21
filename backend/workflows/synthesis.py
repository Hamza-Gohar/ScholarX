import logging
from typing import Callable, List, Optional
from pydantic import BaseModel, Field
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.evidence import EvidenceTrail
from schemas.scholarship import Scholarship
from schemas.scoring import CostAnalysisResult, DeadlineAnalysisResult
from schemas.student import StudentProfile
from workflows.eligibility import EligibilityResult

logger = logging.getLogger("scholarx.workflows.synthesis")


class SynthesizedOpportunity(BaseModel):
    """Unified Scholarship DNA Card synthesizing all analysis dimensions."""
    scholarship_id: str
    scholarship_name: str
    host_country: str
    host_country_name: str
    region: str
    source_url: str
    is_eligible: bool = True
    is_bilateral_quota: bool = False
    quota_seats: Optional[int] = None
    total_out_of_pocket_pkr: int = 0
    total_out_of_pocket_usd: int = 0
    is_within_budget: bool = True
    days_until_deadline: int = 180
    deadline_risk_level: str = "LOW"
    verification_verdict: str = "VERIFIED"
    verification_confidence: float = 0.85
    critical_warnings: List[str] = Field(default_factory=list)
    pakistan_advantages: List[str] = Field(default_factory=list)
    action_items: List[str] = Field(default_factory=list)
    polite_rejection_notice: Optional[str] = None
    need_based_alternatives: List[str] = Field(default_factory=list)
    synthesis_summary: str = ""


class SynthesisWorkflow:
    """
    Deterministic Synthesis Workflow.
    Aggregates discovery, eligibility, PKR costs, deadline lead-times, and skeptic challenges
    into a cohesive, conflict-resolved Opportunity DNA Card.
    """

    def synthesize(
        self,
        scholarship: Scholarship,
        eligibility: EligibilityResult,
        cost: CostAnalysisResult,
        deadline: DeadlineAnalysisResult,
        evidence: EvidenceTrail,
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> SynthesizedOpportunity:
        session_id = student.session_id or "sess-default"
        events: List[ScholarXEvent] = []

        def emit(event_type: AgentEventType, payload: dict, severity: EventSeverity = EventSeverity.INFO):
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=event_type,
                agent_id="synthesis_workflow",
                agent_display_name="Synthesis Engine",
                component_type="WORKFLOW",
                phase="SYNTHESIS",
                related_scholarship_id=scholarship.scholarship_id,
                payload=payload,
                severity=severity,
            )
            events.append(evt)
            if event_callback:
                try:
                    event_callback(evt)
                except Exception as e:
                    logger.warning(f"Failed to invoke event callback: {e}")

        emit(
            AgentEventType.SYNTHESIS_STARTED,
            {"scholarship_id": scholarship.scholarship_id, "name": scholarship.name},
            EventSeverity.INFO,
        )

        # Conflict resolution and warnings reconciliation
        warnings: List[str] = []
        for w in cost.risk_warnings:
            if w not in warnings:
                warnings.append(w)

        for b in eligibility.blocking_issues:
            if b not in warnings:
                warnings.append(f"Eligibility Block: {b}")

        # Check Skeptic challenges for risks
        for chk in evidence.skeptic_challenges:
            warning_text = f"Skeptic Challenge ({chk.category}): {chk.title}"
            if warning_text not in warnings:
                warnings.append(warning_text)

        if scholarship.funding.travel_airfare != "COVERED" and not any("airfare" in w.lower() or "flight" in w.lower() for w in warnings):
            warnings.append("Airfare is not covered by scholarship.")

        # Advantages reconciliation
        advantages: List[str] = list(eligibility.pakistan_advantages)
        if scholarship.pakistan_requirements.pakistan_bilateral_quota and not advantages:
            advantages.append(f"Dedicated quota for Pakistan ({scholarship.pakistan_requirements.pakistan_quota_seats or 'Bilateral'} seats).")

        # Action items compilation
        actions: List[str] = list(eligibility.action_required)
        for act in deadline.action_timeline_recommendation:
            if act not in actions:
                actions.append(act)

        # Extract polite rejection and need-based alternative guidance
        polite_rejection = None
        need_based_alts = []
        if not eligibility.is_eligible:
            for b in eligibility.blocking_issues:
                if "Ineligible for Merit Award" in b or "marks" in b.lower() or "gpa" in b.lower():
                    polite_rejection = b
                    need_based_alts = [
                        "Italian DSU Regional Need-Based Grant (100% Tuition Waiver + €7,000 living stipend based on family income, not GPA).",
                        "China CSC & Chinese Provincial Government Type-B Scholarship (Covers full tuition & dormitory with passing marks).",
                        "Hungarian State-Subsidized Partial Fee Reductions & ERASMUS+ Mobility Pathways.",
                        "Pre-University Foundation / Studienkolleg upgrade pathways.",
                    ]
                    break

        summary = (
            f"{scholarship.name} ({scholarship.host_country_name}) — "
            f"{'Eligible' if eligibility.is_eligible else 'Ineligible'}, "
            f"PKR {cost.total_out_of_pocket_pkr:,} out-of-pocket ({'Within Budget' if cost.is_within_budget else 'Exceeds Budget'}). "
            f"Deadline in {deadline.days_remaining} days ({deadline.risk_level} risk)."
        )

        opportunity = SynthesizedOpportunity(
            scholarship_id=scholarship.scholarship_id,
            scholarship_name=scholarship.name,
            host_country=scholarship.host_country,
            host_country_name=scholarship.host_country_name,
            region=scholarship.region,
            source_url=scholarship.source_url,
            is_eligible=eligibility.is_eligible,
            is_bilateral_quota=scholarship.pakistan_requirements.pakistan_bilateral_quota,
            quota_seats=scholarship.pakistan_requirements.pakistan_quota_seats,
            total_out_of_pocket_pkr=cost.total_out_of_pocket_pkr,
            total_out_of_pocket_usd=cost.total_out_of_pocket_usd,
            is_within_budget=cost.is_within_budget,
            days_until_deadline=deadline.days_remaining,
            deadline_risk_level=deadline.risk_level,
            verification_verdict=evidence.overall_verdict.value,
            verification_confidence=evidence.confidence_score,
            critical_warnings=warnings,
            pakistan_advantages=advantages,
            action_items=actions,
            polite_rejection_notice=polite_rejection,
            need_based_alternatives=need_based_alts,
            synthesis_summary=summary,
        )

        emit(
            AgentEventType.SYNTHESIS_COMPLETE,
            {
                "scholarship_id": scholarship.scholarship_id,
                "is_eligible": opportunity.is_eligible,
                "is_within_budget": opportunity.is_within_budget,
                "warnings_count": len(warnings),
            },
            EventSeverity.INFO,
        )

        return opportunity
