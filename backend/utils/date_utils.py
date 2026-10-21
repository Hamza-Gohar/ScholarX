from datetime import date, datetime
from typing import List, Optional, Tuple
from schemas.scholarship import Scholarship
from schemas.scoring import DeadlineAnalysisResult
from schemas.student import StudentProfile


def calculate_pakistan_preparation_days(
    scholarship: Scholarship,
    student: StudentProfile,
) -> Tuple[int, List[str]]:
    """
    Computes realistic preparation lead times for Pakistani students.
    Considers parallel workflows (e.g. IELTS preparation happens while waiting for HEC attestation).
    """
    timeline_recommendations: List[str] = []
    
    # Base application drafting & motivation letter: 14 days
    critical_path_days = 14
    timeline_recommendations.append("Draft Statement of Purpose & CV: ~14 days")

    # If IELTS needed
    if scholarship.language.english_test_required and not student.language.has_english_test:
        # 14 days prep + test booking + 13 days for result TRF = 27 days
        critical_path_days = max(critical_path_days, 28)
        timeline_recommendations.append("Book and take IELTS Exam + await TRF certificate: ~28 days")

    # If HEC attestation needed
    if scholarship.pakistan_requirements.hec_attestation_required and not student.academic.hec_attestation_done:
        critical_path_days = max(critical_path_days, 21)
        timeline_recommendations.append("HEC Degree Attestation (online booking + regional center drop): ~21 days")

    # If IBCC equivalence needed
    if scholarship.pakistan_requirements.ibcc_equivalence_required and not student.academic.ibcc_equivalence_done:
        critical_path_days = max(critical_path_days, 14)
        timeline_recommendations.append("IBCC Intermediate Equivalence Verification: ~14 days")

    # Recommendation letters from Pakistani professors: 14-21 days
    critical_path_days = max(critical_path_days, 18)
    timeline_recommendations.append("Request and secure 2 Academic Recommendation Letters: ~18 days")

    return critical_path_days, timeline_recommendations


def parse_date_robust(date_str: Optional[str]) -> Optional[date]:
    """
    Parses various date string formats including ISO 8601, slash/hyphen, and text dates.
    Returns date object or None if unparseable/rolling.
    """
    if not date_str or not isinstance(date_str, str):
        return None

    clean = date_str.strip()
    if clean.lower() in ("rolling", "open", "tba", "tbd", "ongoing", "none", "n/a"):
        return None

    # Handle ISO timestamps with T or Z
    if "t" in clean.lower():
        try:
            return datetime.fromisoformat(clean.replace("Z", "+00:00")).date()
        except Exception:
            pass

    formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%m/%d/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d %b %Y",
        "%Y.%m.%d",
        "%d.%m.%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt).date()
        except ValueError:
            continue

    return None


def evaluate_deadline_risk(
    scholarship: Scholarship,
    student: StudentProfile,
    current_date: Optional[date] = None,
) -> DeadlineAnalysisResult:
    """
    Evaluates deadline feasibility and assigns risk tier based on preparation requirements.
    """
    today = current_date or date.today()

    if not scholarship.application_deadline:
        # No fixed deadline / rolling admission
        return DeadlineAnalysisResult(
            deadline_date="Rolling / Open",
            days_remaining=180,
            prep_days_needed_pakistan=28,
            slack_days=152,
            risk_level="LOW",
            is_feasible=True,
            deadline_score=95.0,
            action_timeline_recommendation=["Rolling applications accepted; submit early for best consideration."],
        )

    deadline = parse_date_robust(scholarship.application_deadline)
    if deadline is None:
        raw_clean = scholarship.application_deadline.strip().lower()
        if raw_clean in ("rolling", "open", "ongoing", "tba", "tbd"):
            return DeadlineAnalysisResult(
                deadline_date=scholarship.application_deadline,
                days_remaining=180,
                prep_days_needed_pakistan=28,
                slack_days=152,
                risk_level="LOW",
                is_feasible=True,
                deadline_score=95.0,
                action_timeline_recommendation=["Rolling applications accepted; submit early for best consideration."],
            )
        # Unparseable format - do NOT naively assume 90 days feasible
        return DeadlineAnalysisResult(
            deadline_date=scholarship.application_deadline,
            days_remaining=0,
            prep_days_needed_pakistan=28,
            slack_days=-28,
            risk_level="HIGH",
            is_feasible=False,
            deadline_score=30.0,
            action_timeline_recommendation=[
                f"Deadline '{scholarship.application_deadline}' could not be automatically verified. Immediate manual check of official portal required."
            ],
        )

    days_diff = (deadline - today).days
    days_remaining = max(0, days_diff)
    prep_days, recommendations = calculate_pakistan_preparation_days(scholarship, student)
    buffer_days = 7
    slack_days = days_remaining - prep_days - buffer_days

    if days_diff <= 0:
        if getattr(scholarship, "is_recurring_annual", True):
            next_deadline = deadline
            while next_deadline <= today:
                try:
                    next_deadline = next_deadline.replace(year=next_deadline.year + 1)
                except ValueError:
                    next_deadline = next_deadline.replace(year=next_deadline.year + 1, day=28)
            next_days = (next_deadline - today).days
            next_slack = next_days - prep_days - buffer_days
            risk_level = "NEXT_CYCLE"
            is_feasible = True
            deadline_score = 75.0
            recommendations.insert(
                0,
                f"Current cycle deadline ({deadline.isoformat()}) has passed. Projected next annual cycle deadline: {next_deadline.isoformat()} ({next_days} days away). Highly feasible for advance preparation.",
            )
            return DeadlineAnalysisResult(
                deadline_date=f"{next_deadline.isoformat()} (Next Cycle)",
                days_remaining=next_days,
                prep_days_needed_pakistan=prep_days,
                slack_days=next_slack,
                risk_level=risk_level,
                is_feasible=is_feasible,
                deadline_score=deadline_score,
                action_timeline_recommendation=recommendations,
            )
        else:
            risk_level = "IMPOSSIBLE"
            is_feasible = False
            deadline_score = 0.0
            recommendations.insert(0, "Application deadline has already passed for the current cycle.")
    elif slack_days < 0:
        risk_level = "VERY_HIGH"
        is_feasible = False
        deadline_score = 25.0
        recommendations.insert(0, f"Critical timeline deficit ({abs(slack_days)} days shortage). Extremely risky unless documents are already in hand.")
    elif slack_days <= 14:
        risk_level = "HIGH"
        is_feasible = True
        deadline_score = 60.0
        recommendations.insert(0, "Tight deadline window. Must initiate document attestations and test booking today.")
    elif slack_days <= 35:
        risk_level = "MODERATE"
        is_feasible = True
        deadline_score = 85.0
        recommendations.insert(0, "Feasible timeline with comfortable preparation buffer.")
    else:
        risk_level = "LOW"
        is_feasible = True
        deadline_score = 100.0
        recommendations.insert(0, "Generous preparation window; ideal for polishing SOP and references.")

    return DeadlineAnalysisResult(
        deadline_date=scholarship.application_deadline,
        days_remaining=max(0, days_remaining),
        prep_days_needed_pakistan=prep_days,
        slack_days=slack_days,
        risk_level=risk_level,
        is_feasible=is_feasible,
        deadline_score=deadline_score,
        action_timeline_recommendation=recommendations,
    )
