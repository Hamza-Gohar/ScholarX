import json
from pathlib import Path
import pytest
from schemas.student import StudentProfile, EducationLevel, EnglishTestType
from schemas.scholarship import Scholarship, FundingType, ScholarshipStatus
from schemas.events import ScholarXEvent, AgentEventType, EventSeverity
from schemas.scoring import CompositeScoreResult, CostAnalysisResult, DeadlineAnalysisResult

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def test_student_profile_schema():
    profile = StudentProfile(
        student_id="test-std-01",
        session_id="test-sess-01",
    )
    assert profile.personal.nationality == "PK"
    assert profile.academic.current_level == EducationLevel.INTERMEDIATE
    assert profile.language.english_proficiency_test == EnglishTestType.NONE
    assert profile.preferences.funding_requirement == "FULL"

    dumped = profile.model_dump_json()
    loaded = StudentProfile.model_validate_json(dumped)
    assert loaded.student_id == "test-std-01"


def test_scholarship_schema():
    sc = Scholarship(
        scholarship_id="TEST-001",
        name="Test Bilateral Award",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://example.com/scholarship",
    )
    assert sc.pakistan_requirements.pakistan_eligible is True
    assert sc.funding.funding_type == FundingType.FULL
    assert sc.status == ScholarshipStatus.DISCOVERED


def test_events_schema_sse():
    event = ScholarXEvent(
        session_id="sess-123",
        event_type=AgentEventType.MISSION_INITIATED,
        agent_id="orchestrator",
        agent_display_name="Orchestrator",
        payload={"task": "Initialize mission"},
        severity=EventSeverity.INFO,
    )
    sse_str = event.to_sse_format()
    assert "event: MISSION_INITIATED" in sse_str
    assert "sess-123" in sse_str
