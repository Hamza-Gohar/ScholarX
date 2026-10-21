from datetime import date, timedelta
import pytest
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import (
    LanguageRequirement,
    PakistanSpecificRequirements,
    Scholarship,
)
from schemas.student import (
    AcademicRecord,
    EducationLevel,
    EnglishTestType,
    LanguageProficiency,
    PersonalInfo,
    Preferences,
    StandardizedTests,
    StudentProfile,
)
from workflows.deadline import DeadlineAnalyzer


@pytest.fixture
def student_needing_all_prep() -> StudentProfile:
    return StudentProfile(
        student_id="std-004",
        session_id="sess-004",
        personal=PersonalInfo(name="Khadija", age=20),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            hec_attestation_done=False,
            ibcc_equivalence_done=False,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.NONE,
            has_english_test=False,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(target_degree_level="Bachelor's"),
    )


@pytest.fixture
def sample_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-EU-010",
        name="Romanian Government Scholarship",
        host_country="RO",
        host_country_name="Romania",
        region="Europe",
        source_url="https://mae.ro",
        pakistan_requirements=PakistanSpecificRequirements(
            hec_attestation_required=True,
            ibcc_equivalence_required=True,
        ),
        language=LanguageRequirement(english_test_required=True),
    )


def test_deadline_analyzer_generous_deadline(student_needing_all_prep, sample_scholarship):
    today = date(2026, 9, 1)
    # Deadline 6 months away
    sample_scholarship.application_deadline = (today + timedelta(days=180)).isoformat()

    analyzer = DeadlineAnalyzer()
    res = analyzer.analyze(sample_scholarship, student_needing_all_prep, current_date=today)

    assert res.is_feasible is True
    assert res.risk_level == "LOW"
    assert res.deadline_score == 100.0
    assert res.days_remaining == 180
    assert res.slack_days > 35


def test_deadline_analyzer_tight_deadline(student_needing_all_prep, sample_scholarship):
    today = date(2026, 9, 1)
    # Prep days needed for IELTS + HEC + IBCC is ~28 days + 7 days buffer = 35 days
    # If deadline is in 40 days, slack is ~5 days -> HIGH risk
    sample_scholarship.application_deadline = (today + timedelta(days=40)).isoformat()

    analyzer = DeadlineAnalyzer()
    res = analyzer.analyze(sample_scholarship, student_needing_all_prep, current_date=today)

    assert res.is_feasible is True
    assert res.risk_level in ("HIGH", "MODERATE")
    assert res.deadline_score < 80.0


def test_deadline_analyzer_past_deadline(student_needing_all_prep, sample_scholarship):
    today = date(2026, 9, 1)
    sample_scholarship.application_deadline = (today - timedelta(days=5)).isoformat()
    sample_scholarship.is_recurring_annual = False

    analyzer = DeadlineAnalyzer()
    res = analyzer.analyze(sample_scholarship, student_needing_all_prep, current_date=today)

    assert res.is_feasible is False
    assert res.risk_level == "IMPOSSIBLE"
    assert res.deadline_score == 0.0
    assert res.days_remaining == 0


def test_deadline_analyzer_recurring_annual_past_deadline(student_needing_all_prep, sample_scholarship):
    today = date(2026, 9, 1)
    # Passed 5 days ago, but is recurring annual program
    sample_scholarship.application_deadline = (today - timedelta(days=5)).isoformat()
    sample_scholarship.is_recurring_annual = True

    analyzer = DeadlineAnalyzer()
    res = analyzer.analyze(sample_scholarship, student_needing_all_prep, current_date=today)

    assert res.is_feasible is True
    assert res.risk_level == "NEXT_CYCLE"
    assert res.deadline_score == 75.0
    assert res.days_remaining > 350
    assert "Next Cycle" in res.deadline_date


def test_deadline_analyzer_rolling_deadline(student_needing_all_prep, sample_scholarship):
    sample_scholarship.application_deadline = None

    analyzer = DeadlineAnalyzer()
    res = analyzer.analyze(sample_scholarship, student_needing_all_prep)

    assert res.is_feasible is True
    assert res.risk_level == "LOW"
    assert res.deadline_score >= 90.0


def test_deadline_analyzer_events_emission(student_needing_all_prep, sample_scholarship):
    today = date(2026, 9, 1)
    sample_scholarship.application_deadline = (today + timedelta(days=90)).isoformat()
    events: list[ScholarXEvent] = []

    analyzer = DeadlineAnalyzer()
    res = analyzer.analyze(
        sample_scholarship,
        student_needing_all_prep,
        current_date=today,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(events) >= 1
    event_types = [e.event_type for e in events]
    assert AgentEventType.DEADLINE_EVALUATED in event_types or AgentEventType.DEADLINE_COMPLETE in event_types
    assert res.is_feasible is True
