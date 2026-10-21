import pytest
from datetime import date
from schemas.scholarship import (
    Scholarship,
    FundingDetails,
    FundingType,
    PakistanSpecificRequirements,
    LanguageRequirement,
)
from schemas.student import (
    StudentProfile,
    PersonalInfo,
    AcademicRecord,
    LanguageProficiency,
    Preferences,
    StandardizedTests,
    EducationLevel,
    EnglishTestType,
)
from graph.nodes import skeptic_node, ranking_node, synthesis_node
from graph.state import ScholarXState
from utils.date_utils import parse_date_robust
from utils.pakistan_costs import calculate_pakistan_costs


@pytest.fixture
def sample_student() -> StudentProfile:
    return StudentProfile(
        student_id="std-test-edge",
        session_id="sess-edge-01",
        personal=PersonalInfo(name="Sara Khan", age=22),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            years_of_education=16,
            hec_attestation_done=True,
            ibcc_equivalence_done=True,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            has_english_test=True,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Master's",
            max_out_of_pocket_pkr=500000,
            target_countries=["Germany", "Turkey"],
        ),
    )


@pytest.mark.asyncio
async def test_candidate_pool_preservation_over_10(sample_student):
    """Verify that having >10 candidates does not silently drop candidates 11..N from ranking."""
    candidates = []
    for i in range(15):
        candidates.append(
            Scholarship(
                scholarship_id=f"SCH-POOL-{i:03d}",
                name=f"International Scholarship #{i}",
                host_country="TR",
                host_country_name="Turkey",
                region="MENA",
                source_url=f"https://example.com/sch-{i}",
                funding=FundingDetails(
                    funding_type=FundingType.FULL,
                    tuition="100% Waived",
                    travel_airfare="COVERED",
                ),
                pakistan_requirements=PakistanSpecificRequirements(
                    pakistan_eligible=True,
                    is_hec_recognized=True,
                ),
                language=LanguageRequirement(english_test_required=False),
            )
        )

    from workflows.eligibility import EligibilityInvestigator
    from workflows.cost_analyzer import TrueCostAnalyzer
    from workflows.deadline import DeadlineAnalyzer

    elig_engine = EligibilityInvestigator()
    cost_engine = TrueCostAnalyzer()
    deadline_engine = DeadlineAnalyzer()

    elig_map = {c.scholarship_id: elig_engine.evaluate(c, sample_student) for c in candidates}
    cost_map = {c.scholarship_id: cost_engine.analyze(c, sample_student) for c in candidates}
    deadline_map = {c.scholarship_id: deadline_engine.analyze(c, sample_student) for c in candidates}

    state: ScholarXState = {
        "session_id": "sess-edge-01",
        "student_id": sample_student.student_id,
        "student_profile": sample_student,
        "candidate_scholarships": candidates,
        "eligibility_results": elig_map,
        "cost_results": cost_map,
        "deadline_results": deadline_map,
        "evidence_trails": {},
        "events_queue": [],
    }

    skeptic_res = await skeptic_node(state)
    state["evidence_trails"] = skeptic_res["evidence_trails"]

    assert len(state["evidence_trails"]) == 15
    for c in candidates:
        assert c.scholarship_id in state["evidence_trails"]

    synthesis_res = await synthesis_node(state)
    assert synthesis_res["active_phase"] == "RANKING"

    ranking_res = await ranking_node(state)
    ranked = ranking_res["ranked_results"]

    assert len(ranked) == 15
    ranked_ids = {r.scholarship_id for r in ranked}
    for c in candidates:
        assert c.scholarship_id in ranked_ids


def test_german_tuition_waiver_requires_sperrkonto(sample_student):
    """Verify that a German scholarship without full living stipend requires a Blocked Account (Sperrkonto)."""
    tuition_only_de = Scholarship(
        scholarship_id="SCH-DE-TUITION-01",
        name="Technical University of Munich Tuition Waiver",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://tum.de",
        funding=FundingDetails(
            funding_type=FundingType.TUITION_ONLY,
            tuition="100% Waived",
            monthly_stipend="None",
            travel_airfare="NOT_COVERED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(),
        language=LanguageRequirement(english_test_required=True),
    )

    cost_res = calculate_pakistan_costs(tuition_only_de, sample_student)

    sperrkonto_items = [i for i in cost_res.cost_items if "Sperrkonto" in i.item_name]
    assert len(sperrkonto_items) == 1
    assert sperrkonto_items[0].cost_pkr > 3000000

    assert any("Sperrkonto" in w for w in cost_res.risk_warnings)
    assert cost_res.is_within_budget is False


def test_date_utils_robust_parsing():
    """Verify ISO 8601 timestamps and unparseable dates behave correctly."""
    d1 = parse_date_robust("2026-12-15T23:59:59Z")
    assert d1 == date(2026, 12, 15)

    d2 = parse_date_robust("15-12-2026")
    assert d2 == date(2026, 12, 15)

    d3 = parse_date_robust("December 15, 2026")
    assert d3 == date(2026, 12, 15)

    assert parse_date_robust("Rolling / Open") is None
    assert parse_date_robust("Contact Department for Details") is None
