import pytest
from schemas.student import (
    StudentProfile,
    PersonalInfo,
    AcademicRecord,
    LanguageProficiency,
    Preferences,
    EducationLevel,
    EnglishTestType,
    DocumentsUploaded,
    DocumentItem,
    DocumentQuality,
)
from utils.profile_validator import ProfileValidator


@pytest.fixture
def validator():
    return ProfileValidator()


def test_empty_profile_completeness(validator):
    profile = StudentProfile(
        student_id="std-empty",
        session_id="sess-empty",
        personal=PersonalInfo(name=""),
        academic=AcademicRecord(field_of_study="", gpa_percentage=0.0),
        preferences=Preferences(target_degree_level="", target_fields=[]),
        language=LanguageProficiency(english_proficiency_test=EnglishTestType.NONE, has_english_test=False),
    )
    validated = validator.validate_and_enrich(profile)
    assert validated.profile_completeness < 30
    assert len(validated.missing_required) > 0
    assert "Academic Marks / GPA" in validated.missing_required or "Target Degree Level" in validated.missing_required


def test_fully_complete_profile_completeness(validator):
    profile = StudentProfile(
        student_id="std-full",
        session_id="sess-full",
        personal=PersonalInfo(name="Hamza Tariq", age=21, city="Lahore", province="Punjab", cnic="35202-1234567-1"),
        academic=AcademicRecord(
            current_level=EducationLevel.BACHELORS,
            field_of_study="Computer Science",
            board_university="FAST-NUCES Lahore",
            gpa_percentage=85.0,
            gpa_4_scale=3.7,
            graduation_year=2026,
            hec_attestation_done=True,
        ),
        language=LanguageProficiency(
            english_proficiency_test=EnglishTestType.IELTS,
            ielts_overall=7.5,
            ielts_subbands={"L": 8.0, "R": 7.5, "W": 7.0, "S": 7.5},
            has_english_test=True,
        ),
        preferences=Preferences(
            target_degree_level="Master's",
            target_fields=["Computer Science", "Artificial Intelligence"],
            preferred_regions=["Europe", "Asia"],
            max_out_of_pocket_pkr=200000,
        ),
        documents=DocumentsUploaded(
            cv=DocumentItem(uploaded=True, quality=DocumentQuality.EXCELLENT),
            transcript=DocumentItem(uploaded=True, quality=DocumentQuality.EXCELLENT),
            ielts_certificate=DocumentItem(uploaded=True, quality=DocumentQuality.GOOD),
            passport=DocumentItem(uploaded=True, quality=DocumentQuality.GOOD),
        ),
    )
    validated = validator.validate_and_enrich(profile)
    assert validated.profile_completeness >= 90
    assert len(validated.missing_required) == 0


def test_gpa_synchronization_and_enrichment(validator):
    profile = StudentProfile(
        student_id="std-gpa-test",
        session_id="sess-gpa-test",
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            field_of_study="Pre-Engineering",
            gpa_percentage=88.0,
            gpa_4_scale=0.0,  # Unset
            uk_classification="",  # Unset
        ),
    )
    validated = validator.validate_and_enrich(profile)
    assert validated.academic.gpa_4_scale > 3.5
    assert "First Class" in validated.academic.uk_classification


def test_discrepancy_and_sanity_warnings(validator):
    # Student with FSc wanting direct PhD (invalid in Pakistan/international pipelines without Bachelor's)
    profile = StudentProfile(
        student_id="std-discrepancy",
        session_id="sess-discrepancy",
        academic=AcademicRecord(
            current_level=EducationLevel.INTERMEDIATE,
            gpa_percentage=85.0,
        ),
        preferences=Preferences(
            target_degree_level="PhD",  # Target PhD directly from Inter
        ),
        language=LanguageProficiency(
            has_english_test=True,
            english_proficiency_test=EnglishTestType.NONE,  # Contradiction
        ),
    )
    validated = validator.validate_and_enrich(profile)
    assert len(validated.extraction_warnings) >= 2
    assert any("phd" in w.lower() or "degree level" in w.lower() for w in validated.extraction_warnings)
    assert any("language" in w.lower() or "inconsistency" in w.lower() for w in validated.extraction_warnings)
