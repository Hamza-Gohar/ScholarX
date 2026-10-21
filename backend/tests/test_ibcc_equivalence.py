"""
Automated Tests for Cambridge O/A-Levels Equivalence Engine & IBCC Calculations.
Validates official IBCC conversions, student profile enrichment, and Cambridge advisor routing.
"""

import pytest
from utils.gpa_converter import (
    calculate_cambridge_ibcc_equivalence,
    GpaConverter,
)
from schemas.student import StudentProfile, EducationSystem, EducationLevel
from utils.profile_validator import ProfileValidator
from agents.advisor_agent import AdvisorAgent
from schemas.scholarship import Scholarship
from schemas.scoring import CompositeScoreResult, CostAnalysisResult


def test_cambridge_three_a_levels_conversion():
    """Test standard 3 A-Levels: A*, A, A -> 86.7%, 954/1100 marks, 4.0 GPA."""
    res = calculate_cambridge_ibcc_equivalence(a_level_grades=["A*", "A", "A"])
    assert res["percentage"] == pytest.approx(86.7, abs=0.1)
    assert res["ibcc_total_marks"] == 954
    assert res["gpa_4_scale"] == 4.0
    assert "Grade A1" in res["pakistan_equivalence_grade"]
    assert res["ibcc_marks_scale"] == 1100

    # Wrapper check
    res_wrapper = GpaConverter.calculate_cambridge_ibcc_equivalence(a_level_grades=["A*", "A", "A"])
    assert res_wrapper["percentage"] == res["percentage"]


def test_cambridge_o_and_a_levels_combined_conversion():
    """Test 8 O-Levels + 3 A-Levels combined standard (1100 marks total scale)."""
    o_levels = ["A*", "A*", "A*", "A*", "A", "A", "A", "B"]
    a_levels = ["A*", "A", "A"]
    res = calculate_cambridge_ibcc_equivalence(a_level_grades=a_levels, o_level_grades=o_levels)

    assert res["ibcc_marks_scale"] == 1100
    assert res["percentage"] > 85.0
    assert res["ibcc_total_marks"] > 940
    assert res["gpa_4_scale"] == 4.0


def test_cambridge_profile_auto_enrichment():
    """Test that StudentProfile auto-detects Cambridge stream and populates IBCC equivalence."""
    raw_profile = {
        "student_id": "std-cam-test",
        "personal": {"name": "Aisha Siddiqui", "city": "Karachi", "nationality": "PK"},
        "academic": {
            "current_level": "Intermediate",
            "education_system": "CAMBRIDGE",
            "field_of_study": "Pre-Engineering",
            "institution": "Karachi Grammar School",
            "a_level_grades": ["A*", "A", "A"],
        },
        "preferences": {"target_degree_level": "Bachelor's", "target_fields": ["Computer Science"]},
    }
    profile_dict = StudentProfile.normalize_frontend_profile(raw_profile)
    student = StudentProfile(**profile_dict)
    assert student.academic.education_system == EducationSystem.CAMBRIDGE

    validator = ProfileValidator()
    enriched = validator.validate_and_enrich(student)
    assert enriched.academic.ibcc_equivalence_percentage == pytest.approx(86.7, abs=0.2)
    assert enriched.academic.ibcc_total_marks == 954
    assert enriched.academic.gpa_percentage == pytest.approx(86.7, abs=0.2)
    assert enriched.academic.gpa_4_scale == 4.0


@pytest.mark.asyncio
async def test_advisor_agent_cambridge_specific_roadmap():
    """Test that Advisor Agent generates Cambridge-tailored attestation actions bypassing BISE."""
    student = StudentProfile(
        student_id="std-cam-adv",
        personal={"name": "Aisha Siddiqui", "city": "Karachi", "nationality": "PK"},
        academic={
            "current_level": "Intermediate",
            "education_system": "CAMBRIDGE",
            "field_of_study": "Pre-Engineering",
            "institution": "Karachi Grammar School",
            "a_level_grades": ["A*", "A", "A"],
            "gpa_percentage": 86.7,
            "gpa_4_scale": 4.0,
        },
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science"]},
    )

    scholarship = Scholarship(
        scholarship_id="TEST-HUNGARY-CAMBRIDGE",
        name="Stipendium Hungaricum Bachelor",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
    )
    scholarship.pakistan_requirements.hec_managed = True
    scholarship.pakistan_requirements.ibcc_equivalence_required = True

    advisor = AdvisorAgent()
    offices = advisor._get_pakistan_offices(city=student.personal.city, is_undergrad=True, is_cambridge=True)

    # Check that IBCC Cambridge Cell is listed
    ibcc_office = next((o for o in offices if "IBCC" in o.office_name), None)
    assert ibcc_office is not None
    assert "Cambridge" in ibcc_office.office_name
    assert "G-10/4, Islamabad" in ibcc_office.address

    # Check roadmap actions
    mock_score = CompositeScoreResult(
        scholarship_id=scholarship.scholarship_id,
        scholarship_name=scholarship.name,
        overall_match_score=88.5,
        rank=1,
        eligibility_score=90.0,
        true_funding_score=95.0,
        bilateral_bonus_score=10.0,
        academic_fit_score=90.0,
        doc_readiness_score=85.0,
        deadline_score=90.0,
        verification_score=85.0,
        competition_score=80.0,
        dimensions=[],
        cost_analysis=CostAnalysisResult(
            pre_application_pkr=30000,
            application_pkr=0,
            visa_travel_pkr=75000,
            settlement_pkr=50000,
            total_out_of_pocket_pkr=155000,
            total_out_of_pocket_usd=550,
            student_max_budget_pkr=300000,
            shortfall_pkr=0,
            is_within_budget=True,
            funding_score=95.0,
            cost_items=[],
            risk_warnings=[],
        ),
        blocking_reasons=[],
        pakistan_specific_advantages=[],
        is_recommended=True,
    )

    roadmap = await advisor.generate_roadmap(scholarship, mock_score, student)
    m1_action_descs = [a.description for a in roadmap.milestones[0].actions]
    
    # Must specifically mention Cambridge Statement of Results and IBCC Cambridge Cell
    assert any("Statement of Results" in desc and "IBCC" in desc for desc in m1_action_descs)
    # Must NOT mention local BISE verification
    assert not any("local BISE Board" in desc for desc in m1_action_descs)


def test_cambridge_ranking_priority_over_fsc():
    """Test that Cambridge A-Level candidate gets higher priority and direct-entry recognition over standard FSc."""
    from workflows.ranking import RankingEngine
    from workflows.eligibility import EligibilityInvestigator
    from schemas.scoring import CostAnalysisResult, DeadlineAnalysisResult
    from schemas.evidence import EvidenceTrail, VerificationVerdict

    scholarship = Scholarship(
        scholarship_id="TEST-GERMANY-UNDERGRAD",
        name="DAAD Undergrad Direct Entry",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
    )
    scholarship.eligibility.min_years_education = 12
    scholarship.pakistan_requirements.pakistan_eligible = True

    fsc_student = StudentProfile(
        student_id="std-fsc",
        personal={"name": "FSc Candidate", "city": "Lahore", "nationality": "PK"},
        academic={
            "current_level": "Intermediate",
            "education_system": "PAKISTANI_HSSC",
            "years_of_education": 12,
            "field_of_study": "Computer Science",
            "gpa_percentage": 86.7,
            "gpa_4_scale": 4.0,
        },
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science"]},
    )

    cambridge_student = StudentProfile(
        student_id="std-cam",
        personal={"name": "Aisha Siddiqui", "city": "Karachi", "nationality": "PK"},
        academic={
            "current_level": "Intermediate",
            "education_system": "CAMBRIDGE",
            "years_of_education": 12,
            "field_of_study": "Computer Science",
            "a_level_grades": ["A*", "A", "A"],
            "gpa_percentage": 86.7,
            "gpa_4_scale": 4.0,
        },
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Computer Science"]},
    )

    investigator = EligibilityInvestigator()
    fsc_elig = investigator.evaluate(scholarship, fsc_student)
    cam_elig = investigator.evaluate(scholarship, cambridge_student)

    # Cambridge advantages must include direct entry
    assert any("Direct Entry" in adv for adv in cam_elig.pakistan_advantages)

    cost = CostAnalysisResult(
        pre_application_pkr=20000,
        application_pkr=0,
        visa_travel_pkr=50000,
        settlement_pkr=50000,
        total_out_of_pocket_pkr=120000,
        total_out_of_pocket_usd=400,
        student_max_budget_pkr=300000,
        shortfall_pkr=0,
        is_within_budget=True,
        funding_score=90.0,
        cost_items=[],
        risk_warnings=[],
    )
    deadline = DeadlineAnalysisResult(
        deadline_date="2027-01-15",
        days_remaining=120,
        prep_days_needed_pakistan=45,
        slack_days=75,
        risk_level="LOW",
        deadline_score=90.0,
        is_feasible=True,
    )
    evidence = EvidenceTrail(
        scholarship_id=scholarship.scholarship_id,
        overall_verdict=VerificationVerdict.VERIFIED,
        confidence_score=0.95,
        sources_checked=[],
    )

    ranking_engine = RankingEngine()
    fsc_score = ranking_engine.calculate_composite_score(scholarship, fsc_elig, cost, deadline, evidence, fsc_student)
    cam_score = ranking_engine.calculate_composite_score(scholarship, cam_elig, cost, deadline, evidence, cambridge_student)

    # Cambridge student gets higher academic fit and composite score priority due to CIE direct entry recognition
    assert cam_score.academic_fit_score >= fsc_score.academic_fit_score
    assert cam_score.overall_match_score > fsc_score.overall_match_score
    assert any("Cambridge GCE Direct Entry" in adv for adv in cam_score.pakistan_specific_advantages)

