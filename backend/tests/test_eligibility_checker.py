import pytest
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import (
    EligibilityCriteria,
    FundingDetails,
    FundingType,
    LanguageRequirement,
    PakistanSpecificRequirements,
    Scholarship,
)
from schemas.scoring import DimensionStatus
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
from workflows.eligibility import EligibilityInvestigator, EligibilityResult


@pytest.fixture
def sample_student() -> StudentProfile:
    return StudentProfile(
        student_id="std-001",
        session_id="sess-001",
        personal=PersonalInfo(
            name="Ali Khan",
            nationality="PK",
            country_of_residence="PK",
            city="Lahore",
            province="Punjab",
            age=19,
        ),
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            years_of_education=12,
            field_of_study="Computer Science",
            gpa_percentage=87.5,
            gpa_4_scale=3.7,
            hec_attestation_done=False,
            ibcc_equivalence_done=False,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.0,
            has_english_test=True,
            moi_certificate_available=True,
        ),
        standardized_tests=StandardizedTests(
            hec_usat=None,
            hec_hat=None,
        ),
        preferences=Preferences(
            target_degree_level="Bachelor's",
            target_fields=["Computer Science", "Artificial Intelligence"],
            funding_requirement="FULL",
            max_out_of_pocket_pkr=200000,
        ),
    )


@pytest.fixture
def sample_scholarship() -> Scholarship:
    return Scholarship(
        scholarship_id="SCH-EU-001",
        name="Stipendium Hungaricum Scholarship Programme",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        funding=FundingDetails(
            funding_type=FundingType.FULL,
            tuition="100% Waived",
            monthly_stipend="HUF 43,700",
            health_insurance="COVERED",
        ),
        pakistan_requirements=PakistanSpecificRequirements(
            pakistan_eligible=True,
            pakistan_bilateral_quota=True,
            pakistan_quota_seats=400,
            hec_managed=True,
            hec_usat_required=True,
            hec_attestation_required=True,
            accepts_moi_certificate=True,
        ),
        language=LanguageRequirement(
            english_test_required=True,
            minimum_ielts=5.5,
        ),
        eligibility=EligibilityCriteria(
            degree_levels=["Bachelor's", "Master's", "PhD"],
            eligible_fields=["Computer Science", "Engineering", "Natural Sciences"],
            min_gpa_percentage=70.0,
            min_years_education=12,
            age_limit_undergrad=22,
        ),
        application_deadline="2027-01-15",
    )


def test_eligibility_fully_eligible_student(sample_student, sample_scholarship):
    investigator = EligibilityInvestigator()
    result: EligibilityResult = investigator.evaluate(sample_scholarship, sample_student)

    assert result.is_eligible is True
    assert result.eligibility_score >= 85.0
    assert len(result.blocking_issues) == 0
    assert len(result.dimension_results) >= 10
    
    # Bilateral quota should be BONUS
    quota_dim = next((d for d in result.dimension_results if "Quota" in d.dimension_name or "Bilateral" in d.dimension_name), None)
    assert quota_dim is not None
    assert quota_dim.status == DimensionStatus.BONUS
    assert "400" in quota_dim.details or "bilateral" in quota_dim.details.lower()

    # HEC USAT is required but student hasn't taken it -> action required
    assert any("HEC USAT" in action for action in result.action_required)
    assert any("400" in adv or "quota" in adv.lower() for adv in result.pakistan_advantages)


def test_eligibility_fails_on_degree_level_mismatch(sample_student, sample_scholarship):
    # Scholarship only offers PhD
    sample_scholarship.eligibility.degree_levels = ["PhD"]
    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sample_scholarship, sample_student)

    assert result.is_eligible is False
    assert result.eligibility_score < 50.0
    assert any("degree level" in issue.lower() for issue in result.blocking_issues)


def test_eligibility_fails_on_age_limit(sample_student, sample_scholarship):
    # Student age is 25, undergrad age limit is 22
    sample_student.personal.age = 25
    sample_scholarship.eligibility.age_limit_undergrad = 22

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sample_scholarship, sample_student)

    assert result.is_eligible is False
    assert any("age" in issue.lower() for issue in result.blocking_issues)


def test_eligibility_fails_on_insufficient_gpa(sample_student, sample_scholarship):
    sample_student.academic.gpa_percentage = 60.0
    sample_scholarship.eligibility.min_gpa_percentage = 75.0

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sample_scholarship, sample_student)

    assert result.is_eligible is False
    assert any("gpa" in issue.lower() or "marks" in issue.lower() for issue in result.blocking_issues)


def test_eligibility_moi_waiver_when_no_ielts(sample_student, sample_scholarship):
    # Student has no IELTS test but has MOI certificate
    sample_student.language.english_proficiency_test = EnglishTestType.NONE
    sample_student.language.has_english_test = False
    sample_student.language.moi_certificate_available = True
    sample_scholarship.pakistan_requirements.accepts_moi_certificate = True

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sample_scholarship, sample_student)

    assert result.is_eligible is True
    eng_dim = next((d for d in result.dimension_results if "English" in d.dimension_name or "Language" in d.dimension_name), None)
    assert eng_dim is not None
    assert eng_dim.status in (DimensionStatus.PASS, DimensionStatus.WARNING)
    assert "moi" in eng_dim.details.lower() or "medium of instruction" in eng_dim.details.lower()


def test_eligibility_requires_ielts_when_moi_not_accepted(sample_student, sample_scholarship):
    sample_student.language.english_proficiency_test = EnglishTestType.NONE
    sample_student.language.has_english_test = False
    sample_scholarship.pakistan_requirements.accepts_moi_certificate = False
    sample_scholarship.language.english_test_required = True
    sample_scholarship.language.minimum_ielts = 6.5

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sample_scholarship, sample_student)

    # Missing mandatory IELTS when MOI is rejected flags warning / action required
    assert any("IELTS" in action or "English" in action for action in result.action_required)
    eng_dim = next((d for d in result.dimension_results if "English" in d.dimension_name or "Language" in d.dimension_name), None)
    assert eng_dim is not None
    assert eng_dim.status in (DimensionStatus.ACTION_REQUIRED, DimensionStatus.WARNING)


def test_eligibility_postgrad_hec_hat_requirement(sample_student, sample_scholarship):
    # Switch to Master's student and postgrad scholarship
    sample_student.preferences.target_degree_level = "Master's"
    sample_student.academic.years_of_education = 16
    sample_scholarship.pakistan_requirements.hec_hat_required = True
    sample_scholarship.pakistan_requirements.hec_usat_required = False

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sample_scholarship, sample_student)

    assert any("HEC HAT" in action for action in result.action_required)


def test_eligibility_events_emission(sample_student, sample_scholarship):
    events: list[ScholarXEvent] = []
    investigator = EligibilityInvestigator()
    
    result = investigator.evaluate(
        sample_scholarship,
        sample_student,
        event_callback=lambda evt: events.append(evt),
    )

    assert len(events) >= 2
    event_types = [e.event_type for e in events]
    assert AgentEventType.ELIGIBILITY_CHECK_STARTED in event_types
    assert AgentEventType.ELIGIBILITY_COMPLETE in event_types
    assert result.scholarship_id == sample_scholarship.scholarship_id


def test_eligibility_batch_evaluation(sample_student, sample_scholarship):
    sc2 = sample_scholarship.model_copy(deep=True)
    sc2.scholarship_id = "SCH-ASIA-002"
    sc2.name = "Chinese Government Scholarship (CSC Type A)"
    sc2.host_country = "CN"
    sc2.host_country_name = "China"
    sc2.region = "Asia"

    investigator = EligibilityInvestigator()
    results = investigator.evaluate_all([sample_scholarship, sc2], sample_student)

    assert len(results) == 2
    assert results[0].scholarship_id == "SCH-EU-001"
    assert results[1].scholarship_id == "SCH-ASIA-002"
