import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from schemas.evidence import EvidenceTrail, SkepticChallenge, DebateTopic, VerificationVerdict
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import (
    FundingDetails,
    FundingType,
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
from agents.skeptic_agent import SkepticAgent


@pytest.fixture
def sample_student() -> StudentProfile:
    return StudentProfile(
        student_id="std-005",
        session_id="sess-005",
        personal=PersonalInfo(name="Tariq", age=22),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            field_of_study="Electrical Engineering",
            gpa_percentage=82.0,
            gpa_4_scale=3.5,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.0,
            has_english_test=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Master's",
            max_out_of_pocket_pkr=200000,
            constraints=["Cannot show proof of funds > PKR 1,500,000"],
        ),
    )


@pytest.fixture
def fulbright_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-US-001",
        name="USEFP Fulbright Master's and PhD Program",
        host_country="US",
        host_country_name="United States",
        region="Americas",
        source_url="https://usefp.org/scholarships/fulbright-degree.cfm",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            tuition="100% Covered",
            travel_airfare="COVERED",
            monthly_stipend="USD 1,800 - 2,500",
            health_insurance="COVERED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=True,
            hec_attestation_required=True,
        ),
        language=LanguageRequirement(english_test_required=True),
    )


@pytest.fixture
def german_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-DE-002",
        name="DAAD Development-Related Postgraduate Courses (EPOS)",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de/epos",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            tuition="100% Waived",
            monthly_stipend="EUR 934",
            travel_airfare="REIMBURSED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            hec_attestation_required=True,
        ),
        language=LanguageRequirement(english_test_required=True),
    )


@pytest.mark.asyncio
async def test_skeptic_agent_deterministic_challenges_fulbright(sample_student, fulbright_scholarship):
    agent = SkepticAgent()
    # Explicitly test heuristic fallback / rule-based challenges
    with patch.object(agent, "_call_llm_structured", return_value=None):
        evidence: EvidenceTrail = await agent.evaluate_skepticism(fulbright_scholarship, sample_student)

        assert evidence.scholarship_id == fulbright_scholarship.scholarship_id
        assert len(evidence.skeptic_challenges) >= 1
        
        # Must identify the strict Fulbright 2-year home return obligation (J-1 212e clause)
        return_challenge = next((c for c in evidence.skeptic_challenges if c.category == "RETURN_OBLIGATION" or "return" in c.title.lower()), None)
        assert return_challenge is not None
        assert "return" in return_challenge.description.lower() or "2 years" in return_challenge.description.lower() or "home" in return_challenge.description.lower()

        # Must contain debate topics
        assert len(evidence.debate_summary) >= 1
        debate = evidence.debate_summary[0]
        assert debate.advocate_point != ""
        assert debate.skeptic_counterpoint != ""
        assert debate.verdict != ""


@pytest.mark.asyncio
async def test_skeptic_agent_challenges_german_blocked_account(sample_student, german_scholarship):
    agent = SkepticAgent()
    with patch.object(agent, "_call_llm_structured", return_value=None):
        evidence: EvidenceTrail = await agent.evaluate_skepticism(german_scholarship, sample_student)

        # Germany raises German visa appointment bottleneck (VFS/Embassy waiting time) or blocked account considerations
        assert len(evidence.skeptic_challenges) >= 1
        categories = [c.category for c in evidence.skeptic_challenges]
        assert any(cat in ("VISA_RISK", "HIDDEN_COST", "COMPETITION") for cat in categories)


@pytest.mark.asyncio
async def test_skeptic_agent_events_emission(sample_student, fulbright_scholarship):
    events: list[ScholarXEvent] = []
    agent = SkepticAgent()

    evidence = await agent.evaluate_skepticism(
        fulbright_scholarship,
        sample_student,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(events) >= 2
    event_types = [e.event_type for e in events]
    assert AgentEventType.SKEPTIC_CHALLENGE_RAISED in event_types
    assert AgentEventType.SKEPTIC_COMPLETE in event_types
    assert evidence.confidence_score > 0.0


@pytest.mark.asyncio
async def test_skeptic_agent_llm_generation_mocked(sample_student, fulbright_scholarship):
    agent = SkepticAgent()

    mock_llm_response = """
    {
      "challenges": [
        {
          "category": "RETURN_OBLIGATION",
          "title": "Strict 2-Year Home Country Return Obligation",
          "description": "Fulbright J-1 visa imposes a mandatory 2-year physical return to Pakistan with no immediate H-1B or PR options.",
          "severity": "HIGH",
          "suggested_mitigation": "Align 2-year Pakistani contribution into long-term academic or career roadmap."
        }
      ],
      "debates": [
        {
          "topic": "Prestige vs Freedom of Relocation",
          "advocate_point": "Fulbright is world-renowned and covers full tuition and living expenses.",
          "skeptic_counterpoint": "Mandatory return limits immediate post-study international employment.",
          "verdict": "Exceptional opportunity if the candidate intends to build a leadership career in Pakistan."
        }
      ],
      "confidence_score": 0.92
    }
    """

    with patch.object(agent, "_call_llm_structured", return_value=mock_llm_response):
        evidence = await agent.evaluate_skepticism(fulbright_scholarship, sample_student)
        assert len(evidence.skeptic_challenges) == 1
        assert evidence.skeptic_challenges[0].category == "RETURN_OBLIGATION"
        assert evidence.confidence_score == 0.92
        assert len(evidence.debate_summary) == 1
