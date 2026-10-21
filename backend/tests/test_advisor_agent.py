import pytest
from unittest.mock import patch
from schemas.events import AgentEventType, ScholarXEvent
from schemas.roadmap import ApplicationRoadmap, RoadmapPhase
from schemas.scholarship import (
    FundingDetails,
    FundingType,
    LanguageRequirement,
    PakistanSpecificRequirements,
    Scholarship,
)
from schemas.scoring import CompositeScoreResult, CostAnalysisResult, DeadlineAnalysisResult
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
from agents.advisor_agent import AdvisorAgent


@pytest.fixture
def sample_student() -> StudentProfile:
    return StudentProfile(
        student_id="std-adv-01",
        session_id="sess-adv-01",
        personal=PersonalInfo(name="Daniyal", city="Lahore", age=21),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            field_of_study="Computer Science",
            hec_attestation_done=False,
            ibcc_equivalence_done=False,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.NONE,
            has_english_test=False,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(target_degree_level="Master's"),
    )


@pytest.fixture
def top_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-EU-001",
        name="Stipendium Hungaricum Master's Scholarship",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=True,
            hec_managed=True,
            hec_hat_required=True,
            hec_attestation_required=True,
        ),
        language=LanguageRequirement(english_test_required=True, minimum_ielts=6.5),
        application_deadline="2027-01-15",
    )


@pytest.fixture
def top_ranked_score(top_scholarship) -> CompositeScoreResult:
    return CompositeScoreResult(
        scholarship_id=top_scholarship.scholarship_id,
        scholarship_name=top_scholarship.name,
        overall_match_score=94.5,
        rank=1,
        cost_analysis=CostAnalysisResult(total_out_of_pocket_pkr=220000),
        deadline_analysis=DeadlineAnalysisResult(deadline_date="2027-01-15", days_remaining=130, prep_days_needed_pakistan=28, slack_days=95, risk_level="LOW"),
    )


@pytest.mark.asyncio
async def test_advisor_agent_generates_pakistan_roadmap(sample_student, top_scholarship, top_ranked_score):
    agent = AdvisorAgent()
    roadmap: ApplicationRoadmap = await agent.generate_roadmap(
        scholarship=top_scholarship,
        score_result=top_ranked_score,
        student=sample_student,
    )

    assert roadmap.scholarship_id == top_scholarship.scholarship_id
    assert len(roadmap.milestones) >= 3
    assert len(roadmap.relevant_pakistani_offices) >= 2

    # Should locate Lahore HEC / British Council center since student is in Lahore
    office_names = [o.office_name.lower() for o in roadmap.relevant_pakistani_offices]
    assert any("hec" in o for o in office_names)
    assert any("british council" in o or "ielts" in o for o in office_names)

    # Should have urgent next actions
    assert len(roadmap.urgent_next_actions) >= 1
    assert any("hec" in a.lower() or "ielts" in a.lower() or "attestation" in a.lower() for a in roadmap.urgent_next_actions)


@pytest.mark.asyncio
async def test_advisor_agent_events_emission(sample_student, top_scholarship, top_ranked_score):
    events: list[ScholarXEvent] = []
    agent = AdvisorAgent()

    roadmap = await agent.generate_roadmap(
        scholarship=top_scholarship,
        score_result=top_ranked_score,
        student=sample_student,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(events) >= 1
    assert any(e.event_type == AgentEventType.ROADMAP_GENERATED for e in events)
    assert roadmap.total_budget_needed_pkr > 0
