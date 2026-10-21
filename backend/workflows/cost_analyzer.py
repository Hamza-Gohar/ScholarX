import logging
from typing import Callable, List, Optional
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.scholarship import Scholarship
from schemas.scoring import CostAnalysisResult
from schemas.student import StudentProfile
from utils.pakistan_costs import calculate_pakistan_costs

logger = logging.getLogger("scholarx.workflows.cost")


class TrueCostAnalyzer:
    """
    Deterministic True Cost Analyzer workflow.
    Calculates 4-phase out-of-pocket expenses for Pakistani students in PKR and USD.
    """

    def analyze(
        self,
        scholarship: Scholarship,
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> CostAnalysisResult:
        session_id = student.session_id
        events: List[ScholarXEvent] = []

        def emit(event_type: AgentEventType, payload: dict, severity: EventSeverity = EventSeverity.INFO):
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=event_type,
                agent_id="cost_analyzer",
                agent_display_name="True Cost Analyzer",
                component_type="WORKFLOW",
                phase="COST",
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
            AgentEventType.COST_ANALYSIS_STARTED,
            {
                "scholarship_id": scholarship.scholarship_id,
                "scholarship_name": scholarship.name,
                "student_max_budget_pkr": student.preferences.max_out_of_pocket_pkr,
            },
            EventSeverity.INFO,
        )

        cost_result = calculate_pakistan_costs(scholarship, student)

        emit(
            AgentEventType.PKR_BREAKDOWN_CALCULATED,
            {
                "scholarship_id": scholarship.scholarship_id,
                "total_out_of_pocket_pkr": cost_result.total_out_of_pocket_pkr,
                "total_out_of_pocket_usd": cost_result.total_out_of_pocket_usd,
                "pre_application_pkr": cost_result.pre_application_pkr,
                "application_pkr": cost_result.application_pkr,
                "visa_travel_pkr": cost_result.visa_travel_pkr,
                "settlement_pkr": cost_result.settlement_pkr,
                "funding_score": cost_result.funding_score,
            },
            EventSeverity.INFO,
        )

        if cost_result.is_within_budget:
            emit(
                AgentEventType.COST_WITHIN_BUDGET,
                {
                    "scholarship_id": scholarship.scholarship_id,
                    "total_pkr": cost_result.total_out_of_pocket_pkr,
                    "budget_pkr": cost_result.student_max_budget_pkr,
                },
                EventSeverity.SUCCESS,
            )
        else:
            emit(
                AgentEventType.COST_EXCEEDS_BUDGET,
                {
                    "scholarship_id": scholarship.scholarship_id,
                    "total_pkr": cost_result.total_out_of_pocket_pkr,
                    "budget_pkr": cost_result.student_max_budget_pkr,
                    "shortfall_pkr": cost_result.shortfall_pkr,
                },
                EventSeverity.WARNING,
            )

        emit(
            AgentEventType.COST_ANALYSIS_COMPLETE,
            {
                "scholarship_id": scholarship.scholarship_id,
                "funding_score": cost_result.funding_score,
                "total_items_counted": len(cost_result.cost_items),
            },
            EventSeverity.INFO,
        )

        return cost_result

    def analyze_all(
        self,
        scholarships: List[Scholarship],
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> List[CostAnalysisResult]:
        """Runs cost calculation across all candidate scholarships."""
        return [self.analyze(sc, student, event_callback) for sc in scholarships]
