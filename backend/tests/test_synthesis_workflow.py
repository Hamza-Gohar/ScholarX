import pytest
from schemas.events import AgentEventType, ScholarXEvent
from schemas.evidence import EvidenceTrail, SkepticChallenge, DebateTopic, VerificationVerdict
from schemas.scholarship import (
    FundingDetails,
    FundingType,
    LanguageRequirement,
    PakistanSpecificRequirements,
    Scholarship,
)
from schemas.scoring import CostAnalysisResult, CostPhaseItem, DeadlineAnalysisResult, DimensionScore, DimensionStatus
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
from workflows.eligibility import EligibilityResult
from workflows.synthesis import SynthesisWorkflow, SynthesizedOpportunity


@pytest.fixture
def sample_student() -> StudentProfile:
    return StudentProfile(
        student_id="std-synth-01",
        session_id="sess-synth-01",
        personal=PersonalInfo(name="Hamza", age=21),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            gpa_percentage=85.0,
            gpa_4_scale=3.7,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            has_english_test=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Master's",
            max_out_of_pocket_pkr=300000,
        ),
    )


@pytest.fixture
def sample_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-EU-042",
        name="Stipendium Hungaricum Master's Programme",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            travel_airfare="NOT_COVERED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=True,
            pakistan_quota_seats=400,
            hec_managed=True,
        ),
        language=LanguageRequirement(english_test_required=True),
    )


def test_synthesis_workflow_reconciles_all_signals(sample_student, sample_scholarship):
    eligibility = EligibilityResult(
        scholarship_id=sample_scholarship.scholarship_id,
        scholarship_name=sample_scholarship.name,
        is_eligible=True,
        eligibility_score=92.0,
        dimension_results=[
            DimensionScore(dimension_name="Degree Match", score=100.0, weight=0.2, status=DimensionStatus.PASS),
        ],
        pakistan_advantages=["400 bilateral seats reserved for Pakistan."],
    )

    cost = CostAnalysisResult(
        total_out_of_pocket_pkr=230000,
        total_out_of_pocket_usd=821,
        is_within_budget=True,
        funding_score=90.0,
        cost_items=[CostPhaseItem(item_name="Flight", cost_pkr=180000)],
    )

    deadline = DeadlineAnalysisResult(
        deadline_date="2027-01-15",
        days_remaining=130,
        prep_days_needed_pakistan=28,
        slack_days=95,
        risk_level="LOW",
        is_feasible=True,
        deadline_score=100.0,
    )

    evidence = EvidenceTrail(
        scholarship_id=sample_scholarship.scholarship_id,
        overall_verdict=VerificationVerdict.HEC_CONFIRMED,
        confidence_score=0.90,
        skeptic_challenges=[
            SkepticChallenge(
                challenge_id="chk-01",
                category="HIDDEN_COST",
                title="Airfare not covered",
                description="Ticket is out-of-pocket",
                severity="MEDIUM",
            )
        ],
        debate_summary=[
            DebateTopic(topic="Cost vs Benefit", advocate_point="Full tuition", skeptic_counterpoint="Flight cost", verdict="Viable")
        ],
    )

    workflow = SynthesisWorkflow()
    synthesized: SynthesizedOpportunity = workflow.synthesize(
        scholarship=sample_scholarship,
        eligibility=eligibility,
        cost=cost,
        deadline=deadline,
        evidence=evidence,
        student=sample_student,
    )

    assert synthesized.scholarship_id == sample_scholarship.scholarship_id
    assert synthesized.is_eligible is True
    assert synthesized.is_bilateral_quota is True
    assert synthesized.total_out_of_pocket_pkr == 230000
    assert synthesized.deadline_risk_level == "LOW"
    assert len(synthesized.critical_warnings) >= 1
    assert any("airfare" in w.lower() or "flight" in w.lower() for w in synthesized.critical_warnings)
    assert len(synthesized.pakistan_advantages) >= 1


def test_synthesis_workflow_events_emission(sample_student, sample_scholarship):
    events: list[ScholarXEvent] = []
    workflow = SynthesisWorkflow()

    eligibility = EligibilityResult(
        scholarship_id=sample_scholarship.scholarship_id,
        scholarship_name=sample_scholarship.name,
        is_eligible=True,
        eligibility_score=85.0,
    )
    cost = CostAnalysisResult(total_out_of_pocket_pkr=150000)
    deadline = DeadlineAnalysisResult(
        deadline_date="2027-01-15",
        days_remaining=100,
        prep_days_needed_pakistan=20,
        slack_days=80,
        risk_level="LOW",
    )
    evidence = EvidenceTrail(scholarship_id=sample_scholarship.scholarship_id)

    res = workflow.synthesize(
        scholarship=sample_scholarship,
        eligibility=eligibility,
        cost=cost,
        deadline=deadline,
        evidence=evidence,
        student=sample_student,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(events) >= 2
    event_types = [e.event_type for e in events]
    assert AgentEventType.SYNTHESIS_STARTED in event_types
    assert AgentEventType.SYNTHESIS_COMPLETE in event_types
    assert res.scholarship_id == sample_scholarship.scholarship_id
