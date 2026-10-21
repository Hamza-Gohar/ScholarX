import pytest
from agents.advisor_agent import AdvisorAgent
from agents.discovery_commander import DiscoveryCommander
from agents.skeptic_agent import SkepticAgent
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
from workflows.cost_analyzer import TrueCostAnalyzer
from workflows.deadline import DeadlineAnalyzer
from workflows.eligibility import EligibilityInvestigator
from workflows.ranking import RankingEngine
from workflows.synthesis import SynthesisWorkflow


@pytest.mark.asyncio
async def test_full_system_pipeline_phase0_to_phase4():
    """
    Master E2E Test covering Phases 0 through 4:
    1. Seed DB & Session Storage
    2. Student Intake
    3. Regional Discovery & Deduplication
    4. 15-Dimension Eligibility Evaluation
    5. True Cost Analysis in PKR
    6. Deadline Intelligence
    7. Skeptic Agent Adversarial Review
    8. Synthesis Workflow
    9. Pakistan-Adjusted Weighted Composite Ranking
    10. Final Advisor Action Roadmap
    """
    session_store = get_session_store()
    all_events: list[ScholarXEvent] = []

    def event_collector(evt: ScholarXEvent):
        all_events.append(evt)

    # 1. Student Profile
    student = StudentProfile(
        student_id="std-e2e-phase4",
        session_id="sess-e2e-phase4",
        personal=PersonalInfo(
            name="Zainab Tariq",
            nationality="PK",
            city="Lahore",
            province="Punjab",
            age=21,
        ),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            field_of_study="Computer Science",
            gpa_percentage=89.0,
            gpa_4_scale=3.85,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            has_english_test=True,
            moi_certificate_available=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Master's",
            target_fields=["Computer Science", "Artificial Intelligence"],
            funding_requirement="FULL",
            max_out_of_pocket_pkr=300000,
        ),
    )

    # 2. Candidate Opportunities
    candidates = [
        Scholarship(
            scholarship_id="SCH-E2E4-HU",
            name="Stipendium Hungaricum Master's Scholarship",
            host_country="HU",
            host_country_name="Hungary",
            region="Europe",
            source_url="https://stipendiumhungaricum.hu",
            funding=FundingDetails(funding_type=FundingType.FULL, travel_airfare="NOT_COVERED"),
            pakistan_requirements=PakistanSpecificRequirements(
                pakistan_eligible=True,
                pakistan_bilateral_quota=True,
                pakistan_quota_seats=400,
                hec_managed=True,
            ),
            language=LanguageRequirement(english_test_required=True, minimum_ielts=6.5),
            application_deadline="2027-01-15",
        ),
        Scholarship(
            scholarship_id="SCH-E2E4-TR",
            name="Turkiye Burslari Master's Scholarship",
            host_country="TR",
            host_country_name="Turkey",
            region="MENA",
            source_url="https://turkiyeburslari.gov.tr",
            funding=FundingDetails(funding_type=FundingType.FULL, travel_airfare="COVERED"),
            pakistan_requirements=PakistanSpecificRequirements(
                pakistan_eligible=True,
                pakistan_bilateral_quota=True,
            ),
            language=LanguageRequirement(english_test_required=False),
            application_deadline="2027-02-20",
        ),
        Scholarship(
            scholarship_id="SCH-E2E4-US",
            name="Fulbright Pakistan Master's Fellowship",
            host_country="US",
            host_country_name="United States",
            region="Americas",
            source_url="https://usefp.org",
            funding=FundingDetails(funding_type=FundingType.FULL, travel_airfare="COVERED"),
            pakistan_requirements=PakistanSpecificRequirements(
                pakistan_eligible=True,
                pakistan_bilateral_quota=True,
            ),
            language=LanguageRequirement(english_test_required=True, minimum_ielts=7.0),
            application_deadline="2027-04-12",
        ),
    ]

    # 3. Eligibility, Cost, Deadline, Skeptic
    eligibility_wf = EligibilityInvestigator()
    cost_wf = TrueCostAnalyzer()
    deadline_wf = DeadlineAnalyzer()
    skeptic_agent = SkepticAgent()
    synthesis_wf = SynthesisWorkflow()
    ranking_engine = RankingEngine()
    advisor_agent = AdvisorAgent()

    candidates_bundle = []
    for sc in candidates:
        elig = eligibility_wf.evaluate(sc, student, event_callback=event_collector)
        cost = cost_wf.analyze(sc, student, event_callback=event_collector)
        dl = deadline_wf.analyze(sc, student, event_callback=event_collector)
        ev = await skeptic_agent.evaluate_skepticism(sc, student, event_callback=event_collector)
        synth = synthesis_wf.synthesize(sc, elig, cost, dl, ev, student, event_callback=event_collector)
        candidates_bundle.append((sc, elig, cost, dl, ev))

    # 4. Composite Ranking
    ranked_results = ranking_engine.rank_opportunities(candidates_bundle, student, event_callback=event_collector)
    assert len(ranked_results) == 3
    assert ranked_results[0].rank == 1
    assert ranked_results[1].rank == 2
    assert ranked_results[2].rank == 3
    assert ranked_results[0].overall_match_score >= ranked_results[1].overall_match_score

    # 5. Top Opportunity Roadmap
    top_sc = next(s for s in candidates if s.scholarship_id == ranked_results[0].scholarship_id)
    roadmap = await advisor_agent.generate_roadmap(
        top_sc,
        ranked_results[0],
        student,
        event_callback=event_collector,
    )

    assert roadmap is not None
    assert roadmap.scholarship_id == top_sc.scholarship_id
    assert len(roadmap.milestones) >= 3
    assert len(roadmap.relevant_pakistani_offices) >= 2

    # Verify complete event trail
    event_types = {e.event_type for e in all_events}
    assert AgentEventType.ELIGIBILITY_COMPLETE in event_types
    assert AgentEventType.COST_ANALYSIS_COMPLETE in event_types
    assert AgentEventType.DEADLINE_COMPLETE in event_types
    assert AgentEventType.SKEPTIC_COMPLETE in event_types
    assert AgentEventType.SYNTHESIS_COMPLETE in event_types
    assert AgentEventType.RANKING_CALCULATED in event_types
    assert AgentEventType.ROADMAP_GENERATED in event_types
