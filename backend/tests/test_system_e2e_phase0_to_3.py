import pytest
from db.session_store import get_session_store
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
from workflows.eligibility import EligibilityInvestigator
from workflows.cost_analyzer import TrueCostAnalyzer
from workflows.deadline import DeadlineAnalyzer
from agents.skeptic_agent import SkepticAgent


@pytest.mark.asyncio
async def test_full_system_pipeline_phase0_to_phase3():
    """
    Master E2E Test covering Phase 0 through Phase 3:
    1. Student Profile & Seed DB (Phase 0 & 1)
    2. Regional Discovery (Phase 2)
    3. Eligibility Investigator 15-dim evaluation (Phase 3)
    4. True Cost Analyzer PKR calculations (Phase 3)
    5. Deadline Intelligence (Phase 3)
    6. Skeptic Agent Adversarial Review & Debate (Phase 3)
    """
    session_store = get_session_store()
    all_events: list[ScholarXEvent] = []

    def event_collector(evt: ScholarXEvent):
        all_events.append(evt)

    # 1. Setup Pakistani student profile
    student = StudentProfile(
        student_id="std-e2e-phase3",
        session_id="sess-e2e-phase3",
        personal=PersonalInfo(
            name="Zubair Ahmed",
            nationality="PK",
            city="Rawalpindi",
            province="Punjab",
            age=22,
        ),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            field_of_study="Computer Science",
            gpa_percentage=86.0,
            gpa_4_scale=3.8,
            hec_attestation_done=False,
            ibcc_equivalence_done=False,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            has_english_test=True,
            moi_certificate_available=True,
        ),
        standardized_tests=StandardizedTests(
            hec_hat=68.0,
        ),
        preferences=Preferences(
            target_degree_level="Master's",
            target_fields=["Computer Science", "Artificial Intelligence"],
            funding_requirement="FULL",
            max_out_of_pocket_pkr=250000,
        ),
    )

    # 2. Candidate scholarships pool (mix of Europe, Asia, Americas)
    candidates = [
        Scholarship(
            scholarship_id="SCH-E2E-HU",
            name="Stipendium Hungaricum Master's Scholarship",
            host_country="HU",
            host_country_name="Hungary",
            region="Europe",
            source_url="https://stipendiumhungaricum.hu",
            funding=FundingDetails(
                funding_type=FundingType.FULL,
                tuition="100% Waived",
                travel_airfare="NOT_COVERED",
                monthly_stipend="HUF 43,700",
            ),
            pakistan_requirements=PakistanSpecificRequirements(
                pakistan_eligible=True,
                pakistan_bilateral_quota=True,
                pakistan_quota_seats=400,
                hec_managed=True,
                hec_hat_required=True,
                hec_attestation_required=True,
                accepts_moi_certificate=True,
            ),
            language=LanguageRequirement(english_test_required=True, minimum_ielts=6.5),
            application_deadline="2027-01-15",
        ),
        Scholarship(
            scholarship_id="SCH-E2E-US",
            name="Fulbright Pakistan Master's Fellowship",
            host_country="US",
            host_country_name="United States",
            region="Americas",
            source_url="https://usefp.org",
            funding=FundingDetails(
                funding_type=FundingType.FULL,
                tuition="100% Covered",
                travel_airfare="COVERED",
                monthly_stipend="USD 2,000",
            ),
            pakistan_requirements=PakistanSpecificRequirements(
                pakistan_eligible=True,
                pakistan_bilateral_quota=True,
                hec_attestation_required=True,
            ),
            language=LanguageRequirement(english_test_required=True, minimum_ielts=7.0),
            application_deadline="2027-04-12",
        ),
        Scholarship(
            scholarship_id="SCH-E2E-CN",
            name="Chinese Government Scholarship (CSC Type B)",
            host_country="CN",
            host_country_name="China",
            region="Asia",
            source_url="https://campuschina.org",
            funding=FundingDetails(
                funding_type=FundingType.FULL,
                tuition="100% Waived",
                travel_airfare="NOT_COVERED",
                monthly_stipend="CNY 3,000",
            ),
            pakistan_requirements=PakistanSpecificRequirements(
                pakistan_eligible=True,
                pakistan_bilateral_quota=False,
                accepts_moi_certificate=True,
            ),
            language=LanguageRequirement(english_test_required=False),
            application_deadline="2027-03-31",
        ),
    ]

    # Step 3: Run Eligibility Investigator
    eligibility_worker = EligibilityInvestigator()
    eligibility_results = []
    for c in candidates:
        res = eligibility_worker.evaluate(c, student, event_callback=event_collector)
        eligibility_results.append(res)
        assert res.is_eligible is True
        assert res.eligibility_score > 70.0

    # Step 4: Run True Cost Analyzer
    cost_worker = TrueCostAnalyzer()
    cost_results = []
    for c in candidates:
        cost_res = cost_worker.analyze(c, student, event_callback=event_collector)
        cost_results.append(cost_res)
        assert cost_res.total_out_of_pocket_pkr > 0
        assert cost_res.funding_score > 0

    # Step 5: Run Deadline Intelligence
    deadline_worker = DeadlineAnalyzer()
    deadline_results = []
    for c in candidates:
        dl_res = deadline_worker.analyze(c, student, event_callback=event_collector)
        deadline_results.append(dl_res)
        assert dl_res.is_feasible is True

    # Step 6: Run Skeptic Agent on candidates
    skeptic = SkepticAgent()
    evidence_trails = []
    for c in candidates:
        evidence = await skeptic.evaluate_skepticism(c, student, event_callback=event_collector)
        evidence_trails.append(evidence)
        assert len(evidence.skeptic_challenges) >= 1
        assert len(evidence.debate_summary) >= 1

    # Verify Event Streaming
    assert len(all_events) >= 10
    event_types = {e.event_type for e in all_events}
    assert AgentEventType.ELIGIBILITY_CHECK_STARTED in event_types
    assert AgentEventType.ELIGIBILITY_COMPLETE in event_types
    assert AgentEventType.COST_ANALYSIS_STARTED in event_types
    assert AgentEventType.COST_ANALYSIS_COMPLETE in event_types
    assert AgentEventType.DEADLINE_EVALUATED in event_types or AgentEventType.DEADLINE_COMPLETE in event_types
    assert AgentEventType.SKEPTIC_CHALLENGE_RAISED in event_types
    assert AgentEventType.SKEPTIC_COMPLETE in event_types
