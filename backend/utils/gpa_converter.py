from typing import Dict, Any, List, Optional


def percentage_to_gpa_4(percentage: float) -> float:
    """
    Converts marks percentage to standard 4.0 GPA scale where 100% = 4.00 GPA.
    Formula: GPA = (percentage / 100.0) * 4.0
    Example: 93% = 3.72 GPA, 100% = 4.00 GPA
    """
    if percentage <= 0.0:
        return 0.0
    clamped = min(100.0, max(0.0, float(percentage)))
    return round((clamped / 100.0) * 4.0, 2)


def gpa_4_to_percentage(gpa: float) -> float:
    """
    Converts standard 4.0 scale GPA to percentage where 4.00 GPA = 100%.
    Formula: percentage = (GPA / 4.0) * 100.0
    Example: 3.72 GPA = 93.0%, 4.00 GPA = 100.0%
    """
    if gpa <= 0.0:
        return 0.0
    clamped = min(4.0, max(0.0, float(gpa)))
    return round((clamped / 4.0) * 100.0, 1)


def percentage_to_uk_honours(percentage: float) -> str:
    """
    Converts percentage to UK Honours classification used by Chevening, Commonwealth, and European scholarships.
    """
    if percentage >= 70.0:
        return "First Class Honours (1st)"
    elif percentage >= 60.0:
        return "Upper Second Class Honours (2:1)"
    elif percentage >= 50.0:
        return "Lower Second Class Honours (2:2)"
    elif percentage >= 40.0:
        return "Third Class Honours (3rd)"
    else:
        return "Fail / Unclassified"


def assess_pakistani_academic_standing(percentage: float, target_degree: str = "Bachelor's") -> Dict[str, Any]:
    """
    Evaluates competitive standing of a Pakistani student based on BISE / FBISE / HEC norms.
    """
    gpa = percentage_to_gpa_4(percentage)
    uk_class = percentage_to_uk_honours(percentage)

    if percentage >= 85.0:
        tier = "TIER_1_TOP_MERIT"
        evaluation = (
            f"Exceptional performance ({percentage}% | GPA {gpa}). Highly competitive for top government quotas "
            f"(Stipendium Hungaricum, CSC Type A, Turkiye Burslari, MEXT)."
        )
    elif percentage >= 75.0:
        tier = "TIER_2_STRONG_COMPETITIVE"
        evaluation = (
            f"Strong academic profile ({percentage}% | GPA {gpa}). Solid candidate for bilateral scholarships "
            f"and tuition-waiver European university programs (Italy DSU, Germany DAAD)."
        )
    elif percentage >= 60.0:
        tier = "TIER_3_ELIGIBLE_MERIT_REQUIRED"
        evaluation = (
            f"Eligible profile ({percentage}% | GPA {gpa}). Requires strong motivation letter, extracurriculars, "
            f"or dedicated bilateral quotas to maximize acceptance."
        )
    else:
        tier = "TIER_4_CHALLENGING"
        evaluation = (
            f"Profile ({percentage}% | GPA {gpa}) meets basic thresholds for selected countries, "
            f"but high-competition government quotas will be difficult without exceptional test scores."
        )

    return {
        "percentage": percentage,
        "gpa_4_scale": gpa,
        "uk_classification": uk_class,
        "tier": tier,
        "evaluation": evaluation,
    }


IBCC_GRADE_POINTS = {
    "A*": 90,
    "A": 85,
    "B": 75,
    "C": 65,
    "D": 55,
    "E": 45,
    "U": 0,
}


def ibcc_letter_grade_to_marks(grade: str) -> int:
    """Converts a Cambridge letter grade to official Pakistani IBCC benchmark marks."""
    clean = (grade or "").strip().upper()
    return IBCC_GRADE_POINTS.get(clean, 0)


def calculate_cambridge_ibcc_equivalence(
    a_level_grades: List[str],
    o_level_grades: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Computes official Pakistani Inter Boards Coordination Commission (IBCC) equivalence for Cambridge GCE qualifications.
    Official IBCC formula:
      - IBCC standardized conversion: A* = 90, A = 85, B = 75, C = 65, D = 55, E = 45.
      - Standard 3 A-Level principal subjects = max 300 marks.
      - If 8 O-Level subjects supplied (Pakistani national quota requirement): max 800 marks.
      - Total combined equivalence: standardized to 1,100 marks benchmark (matching FSc 1100 marks).
    """
    if not a_level_grades:
        return {
            "total_marks": 0,
            "max_marks": 1100,
            "percentage": 0.0,
            "equivalent_gpa_4": 0.0,
            "notes": "No Cambridge A-Level grades provided.",
        }

    a_marks = [ibcc_letter_grade_to_marks(g) for g in a_level_grades]
    a_total = sum(a_marks)
    a_max = len(a_marks) * 100

    if o_level_grades and len(o_level_grades) > 0:
        o_marks = [ibcc_letter_grade_to_marks(g) for g in o_level_grades]
        o_total = sum(o_marks)
        o_max = len(o_marks) * 100
        combined_total = o_total + a_total
        combined_max = o_max + a_max
        percentage = round((combined_total / combined_max) * 100.0, 1) if combined_max > 0 else 0.0
        scaled_1100 = round((percentage / 100.0) * 1100)
        equiv_gpa = percentage_to_gpa_4(percentage)
        grade_desc = (
            "Grade A1 (Exceptional)" if percentage >= 80.0
            else "Grade A (Excellent)" if percentage >= 70.0
            else "Grade B (Very Good)" if percentage >= 60.0
            else "Grade C (Good)" if percentage >= 50.0
            else "Grade D (Pass)" if percentage >= 40.0
            else "Grade F (Fail)"
        )
        return {
            "total_marks": scaled_1100,
            "ibcc_total_marks": scaled_1100,
            "max_marks": 1100,
            "ibcc_marks_scale": 1100,
            "percentage": percentage,
            "equivalent_gpa_4": equiv_gpa,
            "gpa_4_scale": equiv_gpa,
            "pakistan_equivalence_grade": grade_desc,
            "a_level_marks": a_total,
            "a_level_max": a_max,
            "o_level_marks": o_total,
            "o_level_max": o_max,
            "notes": f"Combined IBCC Equivalence: {len(o_marks)} O-Levels ({o_total}/{o_max}) + {len(a_marks)} A-Levels ({a_total}/{a_max}) = {scaled_1100}/1100 ({percentage}%, CGPA {equiv_gpa:.2f}).",
        }
    else:
        percentage = round((a_total / a_max) * 100.0, 1) if a_max > 0 else 0.0
        scaled_1100 = round((percentage / 100.0) * 1100)
        equiv_gpa = percentage_to_gpa_4(percentage)
        grade_desc = (
            "Grade A1 (Exceptional)" if percentage >= 80.0
            else "Grade A (Excellent)" if percentage >= 70.0
            else "Grade B (Very Good)" if percentage >= 60.0
            else "Grade C (Good)" if percentage >= 50.0
            else "Grade D (Pass)" if percentage >= 40.0
            else "Grade F (Fail)"
        )
        return {
            "total_marks": scaled_1100,
            "ibcc_total_marks": scaled_1100,
            "max_marks": 1100,
            "ibcc_marks_scale": 1100,
            "percentage": percentage,
            "equivalent_gpa_4": equiv_gpa,
            "gpa_4_scale": equiv_gpa,
            "pakistan_equivalence_grade": grade_desc,
            "a_level_marks": a_total,
            "a_level_max": a_max,
            "o_level_marks": None,
            "o_level_max": None,
            "notes": f"IBCC A-Level Principal Equivalence: {len(a_marks)} A-Levels ({a_total}/{a_max}) projected to {scaled_1100}/1100 ({percentage}%, CGPA {equiv_gpa:.2f}).",
        }


class GpaConverter:
    @staticmethod
    def percentage_to_4_scale(percentage: float) -> float:
        return percentage_to_gpa_4(percentage)

    @staticmethod
    def gpa_4_to_percentage(gpa: float) -> float:
        return gpa_4_to_percentage(gpa)

    @staticmethod
    def get_uk_classification(percentage: float) -> str:
        return percentage_to_uk_honours(percentage)

    @staticmethod
    def assess_standing(percentage: float, target_degree: str = "Bachelor's") -> Dict[str, Any]:
        return assess_pakistani_academic_standing(percentage, target_degree)

    @staticmethod
    def calculate_cambridge_ibcc_equivalence(
        a_level_grades: List[str],
        o_level_grades: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return calculate_cambridge_ibcc_equivalence(a_level_grades, o_level_grades)

