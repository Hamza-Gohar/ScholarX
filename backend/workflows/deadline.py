from datetime import date
import logging
from typing import Callable, List, Optional
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.scholarship import Scholarship
from schemas.scoring import DeadlineAnalysisResult
from schemas.student import StudentProfile
from utils.date_utils import evaluate_deadline_risk

logger = logging.getLogger("scholarx.workflows.deadline")


class DeadlineAnalyzer:
    """
    Deterministic Deadline Intelligence workflow.
    Calculates preparation slack and risk tier factoring in Pakistani documentation bottlenecks.
    """

    def analyze(
        self,
        scholarship: Scholarship,
        student: StudentProfile,
        current_date: Optional[date] = None,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> DeadlineAnalysisResult:
        session_id = student.session_id
        events: List[ScholarXEvent] = []

        def emit(event_type: AgentEventType, payload: dict, severity: EventSeverity = EventSeverity.INFO):
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=event_type,
                agent_id="deadline_analyzer",
                agent_display_name="Deadline Intelligence",
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

        result = evaluate_deadline_risk(scholarship, student, current_date=current_date)

        emit(
            AgentEventType.DEADLINE_EVALUATED,
            {
                "scholarship_id": scholarship.scholarship_id,
                "deadline_date": result.deadline_date,
                "days_remaining": result.days_remaining,
                "slack_days": result.slack_days,
                "risk_level": result.risk_level,
                "is_feasible": result.is_feasible,
            },
            EventSeverity.INFO,
        )

        if result.risk_level in ("HIGH", "VERY_HIGH", "IMPOSSIBLE"):
            emit(
                AgentEventType.DEADLINE_RISK_HIGH,
                {
                    "scholarship_id": scholarship.scholarship_id,
                    "risk_level": result.risk_level,
                    "slack_days": result.slack_days,
                },
                EventSeverity.WARNING if result.is_feasible else EventSeverity.ERROR,
            )
        else:
            emit(
                AgentEventType.DEADLINE_RISK_LOW,
                {
                    "scholarship_id": scholarship.scholarship_id,
                    "risk_level": result.risk_level,
                    "slack_days": result.slack_days,
                },
                EventSeverity.SUCCESS,
            )

        emit(
            AgentEventType.DEADLINE_COMPLETE,
            {
                "scholarship_id": scholarship.scholarship_id,
                "deadline_score": result.deadline_score,
            },
            EventSeverity.INFO,
        )

        return result

    def analyze_all(
        self,
        scholarships: List[Scholarship],
        student: StudentProfile,
        current_date: Optional[date] = None,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> List[DeadlineAnalysisResult]:
        """Evaluates deadlines across all candidate scholarships."""
        return [self.analyze(sc, student, current_date, event_callback) for sc in scholarships]
