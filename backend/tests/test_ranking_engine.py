import pytest
from schemas.events import AgentEventType, ScholarXEvent
from schemas.evidence import EvidenceTrail, VerificationVerdict
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
    PersonalInfo,
    Preferences,
    StudentProfile,
)
from workflows.eligibility import EligibilityResult
from workflows.ranking import RankingEngine


@pytest.fixture
def sample_student() -> StudentProfile:
    return StudentProfile(
        student_id="std-rank-01",
        session_id="sess-rank-01",
        personal=PersonalInfo(name="Ayesha", age=20),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            gpa_percentage=88.0,
            gpa_4_scale=3.8,
        ),
        preferences=Preferences(target_degree_level="Master's", max_out_of_pocket_pkr=300000),
    )


@pytest.fixture
def high_match_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-HIGH-01",
        name="Top Bilateral Scholarship (Hungary)",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        funding=FundingDetails(funding_type=FundingType.FULL),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=True,
            pakistan_quota_seats=400,
        ),
    )


@pytest.fixture
def lower_match_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-LOW-02",
        name="Partial Tuition Grant (Private University)",
        host_country="US",
        host_country_name="United States",
        region="Americas",
        source_url="https://example.edu",
        funding=FundingDetails(funding_type=FundingType.PARTIAL),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=False,
        ),
    )


def test_ranking_engine_scoring_and_ordering(sample_student, high_match_scholarship, lower_match_scholarship):
    engine = RankingEngine()

    high_elig = EligibilityResult(
        scholarship_id=high_match_scholarship.scholarship_id,
        scholarship_name=high_match_scholarship.name,
        is_eligible=True,
        eligibility_score=95.0,
    )
    high_cost = CostAnalysisResult(funding_score=95.0, total_out_of_pocket_pkr=180000)
    high_deadline = DeadlineAnalysisResult(
        deadline_date="2027-01-15",
        days_remaining=120,
        prep_days_needed_pakistan=20,
        slack_days=100,
        risk_level="LOW",
        deadline_score=100.0,
    )
    high_evidence = EvidenceTrail(
        scholarship_id=high_match_scholarship.scholarship_id,
        overall_verdict=VerificationVerdict.HEC_CONFIRMED,
        confidence_score=0.95,
    )

    low_elig = EligibilityResult(
        scholarship_id=lower_match_scholarship.scholarship_id,
        scholarship_name=lower_match_scholarship.name,
        is_eligible=True,
        eligibility_score=70.0,
    )
    low_cost = CostAnalysisResult(funding_score=40.0, total_out_of_pocket_pkr=600000, is_within_budget=False)
    low_deadline = DeadlineAnalysisResult(
        deadline_date="2026-10-15",
        days_remaining=30,
        prep_days_needed_pakistan=25,
        slack_days=5,
        risk_level="HIGH",
        deadline_score=60.0,
    )
    low_evidence = EvidenceTrail(
        scholarship_id=lower_match_scholarship.scholarship_id,
        overall_verdict=VerificationVerdict.PARTIALLY_VERIFIED,
        confidence_score=0.70,
    )

    candidates_data = [
        (lower_match_scholarship, low_elig, low_cost, low_deadline, low_evidence),
        (high_match_scholarship, high_elig, high_cost, high_deadline, high_evidence),
    ]

    ranked: list[CompositeScoreResult] = engine.rank_opportunities(candidates_data, sample_student)

    assert len(ranked) == 2
    # High match must be rank 1
    assert ranked[0].scholarship_id == high_match_scholarship.scholarship_id
    assert ranked[0].rank == 1
    assert ranked[0].overall_match_score > ranked[1].overall_match_score

    # Low match must be rank 2
    assert ranked[1].scholarship_id == lower_match_scholarship.scholarship_id
    assert ranked[1].rank == 2


def test_ranking_engine_events_emission(sample_student, high_match_scholarship):
    events: list[ScholarXEvent] = []
    engine = RankingEngine()

    high_elig = EligibilityResult(scholarship_id=high_match_scholarship.scholarship_id, scholarship_name=high_match_scholarship.name, is_eligible=True, eligibility_score=90.0)
    high_cost = CostAnalysisResult(funding_score=90.0)
    high_deadline = DeadlineAnalysisResult(deadline_date="2027-01-15", days_remaining=100, prep_days_needed_pakistan=20, slack_days=80, risk_level="LOW", deadline_score=100.0)
    high_evidence = EvidenceTrail(scholarship_id=high_match_scholarship.scholarship_id)

    ranked = engine.rank_opportunities(
        [(high_match_scholarship, high_elig, high_cost, high_deadline, high_evidence)],
        sample_student,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(ranked) == 1
    assert any(e.event_type == AgentEventType.RANKING_CALCULATED for e in events)


def test_ranking_engine_filters_scores_under_or_equal_50(sample_student, high_match_scholarship, lower_match_scholarship):
    engine = RankingEngine()

    high_elig = EligibilityResult(scholarship_id=high_match_scholarship.scholarship_id, scholarship_name=high_match_scholarship.name, is_eligible=True, eligibility_score=90.0)
    high_cost = CostAnalysisResult(funding_score=90.0)
    high_deadline = DeadlineAnalysisResult(deadline_date="2027-01-15", days_remaining=100, prep_days_needed_pakistan=20, slack_days=80, risk_level="LOW", deadline_score=100.0)
    high_evidence = EvidenceTrail(scholarship_id=high_match_scholarship.scholarship_id)

    # Very low scores producing composite <= 50.0
    poor_elig = EligibilityResult(scholarship_id=lower_match_scholarship.scholarship_id, scholarship_name=lower_match_scholarship.name, is_eligible=False, eligibility_score=10.0)
    poor_cost = CostAnalysisResult(funding_score=10.0, is_within_budget=False)
    poor_deadline = DeadlineAnalysisResult(deadline_date="2026-09-01", days_remaining=0, prep_days_needed_pakistan=30, slack_days=0, risk_level="CRITICAL", deadline_score=10.0)
    poor_evidence = EvidenceTrail(scholarship_id=lower_match_scholarship.scholarship_id, confidence_score=0.2)

    ranked = engine.rank_opportunities(
        [
            (high_match_scholarship, high_elig, high_cost, high_deadline, high_evidence),
            (lower_match_scholarship, poor_elig, poor_cost, poor_deadline, poor_evidence),
        ],
        sample_student,
    )

    # Only high match (> 50) is returned
    assert len(ranked) == 1
    assert ranked[0].scholarship_id == high_match_scholarship.scholarship_id
    assert ranked[0].overall_match_score > 50.0


def test_ranking_engine_caps_by_degree_level(sample_student):
    """Verify that output limit is capped to 30 for PhD, 20 for Master's, and 15 for Bachelor's."""
    engine = RankingEngine()

    def make_candidate_bundle(n: int):
        candidates_data = []
        for i in range(n):
            sc = Scholarship(
                scholarship_id=f"SCH-CAP-{i:03d}",
                name=f"Scholarship Option {i}",
                host_country="DE",
                host_country_name="Germany",
                region="Europe",
                source_url=f"https://example.com/sch-{i}",
                funding=FundingDetails(funding_type=FundingType.FULL),
                pakistan_requirements=PakistanSpecificRequirements(pakistan_eligible=True),
            )
            elig = EligibilityResult(
                scholarship_id=sc.scholarship_id,
                scholarship_name=sc.name,
                is_eligible=True,
                eligibility_score=60.0 + (i * 0.5),
            )
            cost = CostAnalysisResult(funding_score=70.0, is_within_budget=True)
            deadline = DeadlineAnalysisResult(
                deadline_date="2027-01-15",
                days_remaining=100,
                prep_days_needed_pakistan=20,
                slack_days=80,
                risk_level="LOW",
                deadline_score=80.0,
            )
            ev = EvidenceTrail(scholarship_id=sc.scholarship_id, confidence_score=0.9)
            candidates_data.append((sc, elig, cost, deadline, ev))
        return candidates_data

    # 1. PhD: 40 candidates -> capped at 30
    sample_student.preferences.target_degree_level = "PhD"
    ranked_phd = engine.rank_opportunities(make_candidate_bundle(40), sample_student)
    assert len(ranked_phd) == 30
    assert ranked_phd[0].rank == 1
    assert ranked_phd[-1].rank == 30

    # 2. Master's: 40 candidates -> capped at 20
    sample_student.preferences.target_degree_level = "Master's"
    ranked_master = engine.rank_opportunities(make_candidate_bundle(40), sample_student)
    assert len(ranked_master) == 20
    assert ranked_master[0].rank == 1
    assert ranked_master[-1].rank == 20

    # 3. Bachelor's: 40 candidates -> capped at 15
    sample_student.preferences.target_degree_level = "Bachelor's"
    ranked_bachelor = engine.rank_opportunities(make_candidate_bundle(40), sample_student)
    assert len(ranked_bachelor) == 15
    assert ranked_bachelor[0].rank == 1
    assert ranked_bachelor[-1].rank == 15


def test_ineligible_candidate_scoring_and_filtering(sample_student, high_match_scholarship):
    engine = RankingEngine()
    ineligible_elig = EligibilityResult(
        scholarship_id=high_match_scholarship.scholarship_id,
        scholarship_name=high_match_scholarship.name,
        is_eligible=False,
        eligibility_score=25.0,
        blocking_issues=["Academic score 67.5% below cutoff 70.0%"],
    )
    cost = CostAnalysisResult(funding_score=100.0, total_out_of_pocket_pkr=100000, is_within_budget=True)
    deadline = DeadlineAnalysisResult(
        deadline_date="2027-01-15",
        days_remaining=120,
        prep_days_needed_pakistan=20,
        slack_days=100,
        is_feasible=True,
        deadline_score=100.0,
    )
    evidence = EvidenceTrail(scholarship_id=high_match_scholarship.scholarship_id, confidence_score=0.95)

    score_res = engine.calculate_composite_score(
        high_match_scholarship, ineligible_elig, cost, deadline, evidence, sample_student
    )

    # Ineligible composite score must be penalized below 40.0 and not recommended
    assert score_res.overall_match_score <= 38.0
    assert score_res.is_recommended is False
    assert len(score_res.blocking_reasons) > 0

    # In rank_opportunities, candidates with score <= 50.0 should be filtered out
    candidates = [(high_match_scholarship, ineligible_elig, cost, deadline, evidence)]
    ranked = engine.rank_opportunities(candidates, sample_student)
    assert len(ranked) == 0
