import logging
from typing import List, Tuple
from schemas.student import (
    StudentProfile,
    EducationLevel,
    EducationSystem,
    EnglishTestType,
)
from utils.gpa_converter import GpaConverter

logger = logging.getLogger("scholarx.utils.validator")


class ProfileValidator:
    def __init__(self):
        self.gpa_converter = GpaConverter()

    def validate_and_enrich(self, profile: StudentProfile) -> StudentProfile:
        """
        Validates the student profile, enriches GPA and degree classification,
        calculates profile completeness, and identifies missing required/optional fields and warnings.
        """
        warnings: List[str] = []
        missing_req: List[str] = []
        missing_opt: List[str] = []

        # 1. Academic Record Validation & Enrichment
        acad = profile.academic

        # Cambridge O/A-Levels Equivalence Calculation
        if (
            acad.education_system == EducationSystem.CAMBRIDGE
            or (acad.a_level_grades and len(acad.a_level_grades) > 0)
        ):
            if acad.a_level_grades and len(acad.a_level_grades) > 0:
                ibcc_res = self.gpa_converter.calculate_cambridge_ibcc_equivalence(
                    acad.a_level_grades,
                    acad.o_level_grades,
                )
                acad.ibcc_equivalence_percentage = ibcc_res["percentage"]
                acad.ibcc_total_marks = ibcc_res["total_marks"]
                acad.gpa_percentage = ibcc_res["percentage"]
                acad.gpa_4_scale = ibcc_res["equivalent_gpa_4"]

        if acad.gpa_percentage > 100.0 or acad.gpa_percentage < 0.0:
            warnings.append(f"Invalid GPA percentage: {acad.gpa_percentage}%. Must be between 0% and 100%.")

        if acad.gpa_4_scale > 4.0 or acad.gpa_4_scale < 0.0:
            warnings.append(f"Invalid GPA on 4.0 scale: {acad.gpa_4_scale}. Must be between 0.0 and 4.0.")

        # Enrich GPA and UK classification if percentage or GPA scale is available
        if acad.gpa_percentage > 0:
            if acad.gpa_4_scale <= 0.0:
                acad.gpa_4_scale = round(self.gpa_converter.percentage_to_4_scale(acad.gpa_percentage), 2)
            if not acad.uk_classification or acad.uk_classification == "First Class":
                acad.uk_classification = self.gpa_converter.get_uk_classification(acad.gpa_percentage)
        elif acad.gpa_4_scale > 0:
            acad.gpa_percentage = round(self.gpa_converter.gpa_4_to_percentage(acad.gpa_4_scale), 1)
            if not acad.uk_classification or acad.uk_classification == "First Class":
                acad.uk_classification = self.gpa_converter.get_uk_classification(acad.gpa_percentage)
        else:
            missing_req.append("Academic Marks / GPA")

        if not acad.field_of_study or acad.field_of_study.strip() == "":
            missing_req.append("Current Field of Study")

        # 2. Degree Progression & Sanity Checks
        pref = profile.preferences
        if not pref.target_degree_level or pref.target_degree_level.strip() == "":
            missing_req.append("Target Degree Level")
        else:
            target_deg = pref.target_degree_level.lower()
            current_deg = acad.current_level

            # Check: Intermediate student targeting PhD directly
            if current_deg in (EducationLevel.MATRIC, EducationLevel.INTERMEDIATE) and "phd" in target_deg:
                warnings.append("Target Degree Level is PhD, but current level is Intermediate/Matric. A Bachelor's degree (16 years) is required first.")

            # Check: Master's graduate targeting Bachelor's
            if current_deg == EducationLevel.MASTERS and "bachelor" in target_deg:
                warnings.append("Target Degree Level is Bachelor's, but student already holds a Master's degree.")

        if not pref.target_fields or len(pref.target_fields) == 0:
            missing_req.append("Target Fields of Study")

        # 3. Language Proficiency Checks
        lang = profile.language
        if lang.has_english_test and lang.english_proficiency_test == EnglishTestType.NONE:
            warnings.append("Language inconsistency: has_english_test is True, but English proficiency test is set to NONE.")

        # 4. Missing Optional Documents
        docs = profile.documents
        if not docs.cv.uploaded:
            missing_opt.append("CV / Resume")
        if not docs.transcript.uploaded:
            missing_opt.append("Academic Transcript")
        if not docs.ielts_certificate.uploaded and not lang.has_english_test:
            missing_opt.append("IELTS / English Test Certificate")
        if not docs.passport.uploaded:
            missing_opt.append("Passport Copy")

        # 5. Completeness Score Calculation (0 to 100%)
        score = 0

        # Personal Info (max 15%)
        if profile.personal.name and profile.personal.name != "Student":
            score += 5
        if profile.personal.city:
            score += 5
        if profile.personal.cnic or profile.personal.passport_number:
            score += 5

        # Academic Record (max 40%)
        if acad.field_of_study:
            score += 10
        if acad.board_university:
            score += 10
        if acad.gpa_percentage > 0:
            score += 20

        # Language (max 15%)
        if lang.has_english_test or lang.english_proficiency_test != EnglishTestType.NONE or lang.moi_certificate_available:
            score += 15

        # Preferences (max 20%)
        if pref.target_degree_level:
            score += 10
        if pref.target_fields:
            score += 10

        # Documents (max 10%)
        if docs.cv.uploaded or docs.transcript.uploaded or docs.ielts_certificate.uploaded:
            score += 10

        profile.profile_completeness = min(100, max(0, score))
        profile.missing_required = missing_req
        profile.missing_optional = missing_opt
        profile.extraction_warnings = warnings

        return profile
