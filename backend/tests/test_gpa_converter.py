import pytest
from utils.gpa_converter import (
    percentage_to_gpa_4,
    percentage_to_uk_honours,
    assess_pakistani_academic_standing,
)
from utils.pakistan_costs import calculate_pakistan_costs
from utils.date_utils import evaluate_deadline_risk
from schemas.student import StudentProfile
from schemas.scholarship import Scholarship, FundingType


def test_gpa_conversions():
    assert percentage_to_gpa_4(87.0) == 4.0
    assert percentage_to_gpa_4(82.0) == 3.82
    assert percentage_to_gpa_4(76.0) == 3.38
    assert percentage_to_gpa_4(65.0) == 2.75
    assert percentage_to_gpa_4(45.0) == 1.5


def test_uk_honours_conversions():
    assert percentage_to_uk_honours(85.0) == "First Class Honours (1st)"
    assert percentage_to_uk_honours(65.0) == "Upper Second Class Honours (2:1)"
    assert percentage_to_uk_honours(55.0) == "Lower Second Class Honours (2:2)"


def test_pakistan_cost_engine():
    profile = StudentProfile(student_id="std-cost-01", session_id="sess-cost-01")
    profile.preferences.max_out_of_pocket_pkr = 150000

    sc = Scholarship(
        scholarship_id="TEST-SC-01",
        name="Test Hungary",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
    )
    sc.funding.travel_airfare = "NOT_COVERED"

    cost_result = calculate_pakistan_costs(sc, profile)
    assert cost_result.total_out_of_pocket_pkr > 0
    assert cost_result.pre_application_pkr >= 65000  # IELTS test needed if no test provided


def test_deadline_intelligence():
    profile = StudentProfile(student_id="std-dl-01", session_id="sess-dl-01")
    sc = Scholarship(
        scholarship_id="TEST-SC-02",
        name="Test Open",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
        application_deadline="2027-01-15",
    )
    dl_result = evaluate_deadline_risk(sc, profile)
    assert dl_result.is_feasible is True


def test_gpa_4_to_percentage_conversions():
    from utils.gpa_converter import gpa_4_to_percentage, GpaConverter

    assert gpa_4_to_percentage(4.0) == 88.0
    assert abs(gpa_4_to_percentage(3.82) - 82.0) < 0.2
    assert abs(gpa_4_to_percentage(3.5) - 77.5) < 0.2
    assert abs(gpa_4_to_percentage(3.0) - 70.0) < 0.2
    assert abs(gpa_4_to_percentage(2.5) - 60.0) < 0.2
    assert abs(gpa_4_to_percentage(2.0) - 50.0) < 0.2
    assert abs(gpa_4_to_percentage(1.0) - 40.0) < 0.2

    # Test class method wrapper
    assert GpaConverter.gpa_4_to_percentage(4.0) == 88.0


def test_eligibility_with_gpa_4_scale_graduate():
    from workflows.eligibility import EligibilityInvestigator

    # Student graduated with CGPA 3.8 / 4.0 but percentage is 0.0
    profile = StudentProfile(
        student_id="std-gpa-01",
        personal={"full_name": "Hamza Ali", "city": "Karachi", "nationality": "Pakistan"},
        academic={"current_level": "Bachelor's", "field_of_study": "Computer Science", "gpa_4_scale": 3.8, "gpa_percentage": 0.0},
        preferences={"target_degree_level": "Master's", "target_fields": ["Computer Science"]}
    )

    sc_pass = Scholarship(
        scholarship_id="TEST-SC-GPA-PASS",
        name="Merit Scholarship",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
    )
    sc_pass.eligibility.min_gpa_percentage = 75.0
    sc_pass.eligibility.degree_levels = ["Master's"]
    sc_pass.eligibility.eligible_fields = ["Computer Science"]

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(sc_pass, profile)
    assert result.is_eligible is True

    # When requirement is 90% (which is above 3.8 -> 81.7%), should fail
    sc_fail = Scholarship(
        scholarship_id="TEST-SC-GPA-FAIL",
        name="Elite Merit Scholarship",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
    )
    sc_fail.eligibility.min_gpa_percentage = 90.0
    sc_fail.eligibility.degree_levels = ["Master's"]
    sc_fail.eligibility.eligible_fields = ["Computer Science"]

    result_fail = investigator.evaluate(sc_fail, profile)
    assert result_fail.is_eligible is False

