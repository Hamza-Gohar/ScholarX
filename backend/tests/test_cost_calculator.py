import pytest
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


@pytest.fixture
def student_with_ielts() -> StudentProfile:
    return StudentProfile(
        student_id="std-002",
        session_id="sess-002",
        personal=PersonalInfo(name="Fatima Noor", age=21),
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
        ),
    )


@pytest.fixture
def student_without_ielts_low_budget() -> StudentProfile:
    return StudentProfile(
        student_id="std-003",
        session_id="sess-003",
        personal=PersonalInfo(name="Bilal Ahmed", age=19),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            years_of_education=12,
            hec_attestation_done=False,
            ibcc_equivalence_done=False,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.NONE,
            has_english_test=False,
        ),
        standardized_tests=StandardizedTests(),
        preferences=Preferences(
            target_degree_level="Bachelor's",
            max_out_of_pocket_pkr=100000,
        ),
    )


@pytest.fixture
def fully_funded_covered_airfare_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-TR-001",
        name="Turkiye Burslari Scholarship",
        host_country="TR",
        host_country_name="Turkey",
        region="MENA",
        source_url="https://turkiyeburslari.gov.tr",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            tuition="100% Waived",
            travel_airfare="COVERED",
            monthly_stipend="TRY 4,500",
            health_insurance="COVERED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=True,
            hec_attestation_required=True,
        ),
        language=LanguageRequirement(english_test_required=False),
    )


def test_cost_analyzer_fully_funded_zero_airfare(student_with_ielts, fully_funded_covered_airfare_scholarship):
    analyzer = TrueCostAnalyzer()
    cost_result = analyzer.analyze(fully_funded_covered_airfare_scholarship, student_with_ielts)

    assert cost_result.total_out_of_pocket_pkr > 0
    # Airfare is covered -> no airfare item in costs
    airfare_items = [i for i in cost_result.cost_items if "airfare" in i.item_name.lower() or "flight" in i.item_name.lower()]
    assert len(airfare_items) == 0
    # Turkish visa is exempt for scholars
    visa_items = [i for i in cost_result.cost_items if "visa fee" in i.item_name.lower()]
    assert any(i.cost_pkr == 0 for i in visa_items)
    # Student has 500k budget -> well within budget
    assert cost_result.is_within_budget is True
    assert cost_result.shortfall_pkr == 0
    assert cost_result.funding_score >= 95.0


def test_cost_analyzer_exceeds_budget_with_ielts_and_airfare(student_without_ielts_low_budget):
    # Scholarship requires IELTS and does NOT cover flight
    hungary_sch = Scholarship(
        scholarship_id="SCH-EU-001",
        name="Stipendium Hungaricum",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            travel_airfare="NOT_COVERED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(
            hec_attestation_required=True,
            hec_usat_required=True,
        ),
        language=LanguageRequirement(english_test_required=True),
    )

    analyzer = TrueCostAnalyzer()
    cost_result = analyzer.analyze(hungary_sch, student_without_ielts_low_budget)

    # Must include IELTS fee (76,000 PKR)
    ielts_items = [i for i in cost_result.cost_items if "IELTS" in i.item_name]
    assert len(ielts_items) == 1
    assert ielts_items[0].cost_pkr >= 75000

    # Must include HEC USAT fee (2,500 PKR)
    usat_items = [i for i in cost_result.cost_items if "USAT" in i.item_name]
    assert len(usat_items) == 1
    assert usat_items[0].cost_pkr == 2500

    # Must include flight ticket
    flight_items = [i for i in cost_result.cost_items if "airfare" in i.item_name.lower() or "flight" in i.item_name.lower()]
    assert len(flight_items) == 1
    assert flight_items[0].cost_pkr >= 180000

    # Student budget is 100,000 PKR, grand total will exceed 300,000 PKR
    assert cost_result.total_out_of_pocket_pkr > student_without_ielts_low_budget.preferences.max_out_of_pocket_pkr
    assert cost_result.is_within_budget is False
    assert cost_result.shortfall_pkr > 0
    assert len(cost_result.risk_warnings) >= 1


def test_cost_analyzer_german_uni_assist_and_schengen_fee(student_with_ielts):
    german_sch = Scholarship(
        scholarship_id="SCH-DE-001",
        name="DAAD Helmut-Schmidt-Programme",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            travel_airfare="REIMBURSED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(),
        language=LanguageRequirement(english_test_required=True),
    )

    analyzer = TrueCostAnalyzer()
    cost_result = analyzer.analyze(german_sch, student_with_ielts)

    # German Uni-Assist should be in application phase
    uni_assist = [i for i in cost_result.cost_items if "Uni-Assist" in i.item_name]
    assert len(uni_assist) == 1
    assert uni_assist[0].cost_pkr > 20000

    # Schengen visa fee should be present
    schengen = [i for i in cost_result.cost_items if "Schengen" in i.item_name]
    assert len(schengen) == 1
    assert schengen[0].cost_pkr > 25000


def test_cost_analyzer_events_emission(student_with_ielts, fully_funded_covered_airfare_scholarship):
    events: list[ScholarXEvent] = []
    analyzer = TrueCostAnalyzer()

    result = analyzer.analyze(
        fully_funded_covered_airfare_scholarship,
        student_with_ielts,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(events) >= 2
    event_types = [e.event_type for e in events]
    assert AgentEventType.COST_ANALYSIS_STARTED in event_types
    assert AgentEventType.PKR_BREAKDOWN_CALCULATED in event_types
    assert AgentEventType.COST_ANALYSIS_COMPLETE in event_types
    assert result.total_out_of_pocket_pkr > 0


def test_cost_analyzer_batch(student_with_ielts, fully_funded_covered_airfare_scholarship):
    sch2 = fully_funded_covered_airfare_scholarship.model_copy(deep=True)
    sch2.scholarship_id = "SCH-TR-002"

    analyzer = TrueCostAnalyzer()
    results = analyzer.analyze_all([fully_funded_covered_airfare_scholarship, sch2], student_with_ielts)

    assert len(results) == 2
    assert results[0].total_out_of_pocket_pkr == results[1].total_out_of_pocket_pkr


def test_cost_analyzer_fbr_section_236y_advance_tax():
    from utils.pakistan_costs import calculate_pakistan_costs, get_exchange_rates

    rates = get_exchange_rates()
    assert "USD" in rates
    assert rates["USD"] > 0

    # Scholarship in Germany requiring Uni-Assist (EUR 75)
    sch_de = Scholarship(
        scholarship_id="TEST-DE-COST",
        name="German DAAD",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
    )

    # 1. Tax Filer Profile
    filer_student = StudentProfile(
        student_id="std-filer",
        preferences=Preferences(is_tax_filer=True, max_out_of_pocket_pkr=500000)
    )
    filer_result = calculate_pakistan_costs(sch_de, filer_student)

    # Check FBR 236Y item present with 5%
    filer_tax_items = [i for i in filer_result.cost_items if "236Y" in i.item_name]
    assert len(filer_tax_items) == 1
    assert "5% Filer" in filer_tax_items[0].item_name
    expected_spend = round(75 * rates["EUR"])
    assert filer_tax_items[0].cost_pkr == round(expected_spend * 0.05)

    # Check 3.5% FX markup
    card_fx_items = [i for i in filer_result.cost_items if "3.5%" in i.item_name]
    assert len(card_fx_items) == 1
    assert card_fx_items[0].cost_pkr == round(expected_spend * 0.035)

    # 2. Non-Filer Profile
    non_filer_student = StudentProfile(
        student_id="std-non-filer",
        preferences=Preferences(is_tax_filer=False, max_out_of_pocket_pkr=500000)
    )
    non_filer_result = calculate_pakistan_costs(sch_de, non_filer_student)

    non_filer_tax_items = [i for i in non_filer_result.cost_items if "236Y" in i.item_name]
    assert len(non_filer_tax_items) == 1
    assert "10% Non-Filer" in non_filer_tax_items[0].item_name
    assert non_filer_tax_items[0].cost_pkr == round(expected_spend * 0.10)

    # Non-filer tax should be exactly double the filer tax
    assert non_filer_tax_items[0].cost_pkr == filer_tax_items[0].cost_pkr * 2
    assert non_filer_result.total_out_of_pocket_pkr > filer_result.total_out_of_pocket_pkr
