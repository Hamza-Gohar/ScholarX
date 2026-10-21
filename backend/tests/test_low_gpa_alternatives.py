"""
Automated Tests for Low-GPA Polite Ineligibility & Need-Based Grant Recommendations.
Validates respectful candidate feedback and constructive alternative pathway routing.
"""

import pytest
from schemas.student import StudentProfile
from schemas.scholarship import Scholarship
from schemas.evidence import EvidenceTrail
from schemas.scoring import CompositeScoreResult, CostAnalysisResult, DeadlineAnalysisResult
from workflows.eligibility import EligibilityInvestigator
from workflows.synthesis import SynthesisWorkflow
from agents.advisor_agent import AdvisorAgent


def test_eligibility_polite_ineligibility_and_alternatives():
    """Test that students below cutoff receive constructive feedback and need-based options."""
    profile = StudentProfile(
        student_id="std-low-gpa-01",
        personal={"name": "Usman Tariq", "city": "Faisalabad", "nationality": "PK"},
        academic={
            "current_level": "Bachelor's",
            "field_of_study": "Computer Science",
            "gpa_percentage": 54.0,
            "gpa_4_scale": 2.2,
        },
        preferences={"target_degree_level": "Master's", "target_fields": ["Computer Science"]},
    )

    scholarship = Scholarship(
        scholarship_id="TEST-DAAD-STRICT",
        name="DAAD Helmut-Schmidt Programme",
        host_country="DE",
        host_country_name="Germany",
        region="Europe",
        source_url="https://daad.de",
    )
    scholarship.eligibility.min_gpa_percentage = 70.0
    scholarship.eligibility.degree_levels = ["Master's"]
    scholarship.eligibility.eligible_fields = ["Computer Science"]

    investigator = EligibilityInvestigator()
    result = investigator.evaluate(scholarship, profile)

    assert result.is_eligible is False
    assert len(result.action_required) > 0

    # Verify polite rejection explanation
    rejection_item = next((a for a in result.action_required if "below the official cutoff" in a), None)
    assert rejection_item is not None
    assert "54.0%" in rejection_item
    assert "70.0%" in rejection_item

    # Verify need-based grant suggestions
    grant_item = next((a for a in result.action_required if "Italian DSU" in a or "Need-Based" in a), None)
    assert grant_item is not None
    assert "Italian DSU Regional Grants" in grant_item


def test_synthesis_workflow_populates_polite_notice_and_alternatives():
    """Test that SynthesisWorkflow attaches polite_rejection_notice and need_based_alternatives."""
    profile = StudentProfile(
        student_id="std-low-gpa-02",
        personal={"name": "Sara Khan", "city": "Peshawar", "nationality": "PK"},
        academic={
            "current_level": "Intermediate",
            "field_of_study": "Pre-Engineering",
            "gpa_percentage": 52.0,
            "gpa_4_scale": 2.1,
        },
        preferences={"target_degree_level": "Bachelor's", "target_fields": ["Software Engineering"]},
    )

    scholarship = Scholarship(
        scholarship_id="TEST-HUNGARY-STRICT",
        name="Stipendium Hungaricum Bachelor",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
    )
    scholarship.eligibility.min_gpa_percentage = 65.0
    scholarship.eligibility.degree_levels = ["Bachelor's"]
    scholarship.eligibility.eligible_fields = ["Software Engineering"]

    investigator = EligibilityInvestigator()
    eligibility_result = investigator.evaluate(scholarship, profile)

    cost_result = CostAnalysisResult(
        pre_application_pkr=25000,
        application_pkr=0,
        visa_travel_pkr=60000,
        settlement_pkr=50000,
        total_out_of_pocket_pkr=135000,
        total_out_of_pocket_usd=480,
        student_max_budget_pkr=200000,
        shortfall_pkr=0,
        is_within_budget=True,
        funding_score=90.0,
        cost_items=[],
        risk_warnings=[],
    )

    deadline_result = DeadlineAnalysisResult(
        deadline_date="2026-12-15",
        days_remaining=120,
        prep_days_needed_pakistan=45,
        slack_days=75,
        risk_level="LOW",
        is_feasible=True,
        deadline_score=90.0,
        action_timeline_recommendation=[],
    )

    evidence = EvidenceTrail(
        scholarship_id=scholarship.scholarship_id,
        overall_verdict="VERIFIED",
        confidence_score=0.9,
    )

    synthesis = SynthesisWorkflow()
    synthesized = synthesis.synthesize(
        scholarship=scholarship,
        eligibility=eligibility_result,
        cost=cost_result,
        deadline=deadline_result,
        evidence=evidence,
        student=profile,
    )

    assert synthesized.is_eligible is False
    assert synthesized.polite_rejection_notice is not None
    assert "52.0%" in synthesized.polite_rejection_notice
    assert len(synthesized.need_based_alternatives) >= 2
    assert any("Italian DSU" in alt for alt in synthesized.need_based_alternatives)
    assert any("China CSC" in alt for alt in synthesized.need_based_alternatives)


@pytest.mark.asyncio
async def test_advisor_agent_includes_low_gpa_urgent_action():
    """Test that Advisor Agent adds need-based urgent actions for students with marks < 60%."""
    profile = StudentProfile(
        student_id="std-low-gpa-adv",
        personal={"name": "Hamza Tariq", "city": "Rawalpindi", "nationality": "PK"},
        academic={
            "current_level": "Bachelor's",
            "field_of_study": "Information Technology",
            "gpa_percentage": 58.0,
            "gpa_4_scale": 2.35,
        },
        preferences={"target_degree_level": "Master's", "target_fields": ["Information Technology"]},
    )

    scholarship = Scholarship(
        scholarship_id="TEST-SCHOLARSHIP-ROADMAP",
        name="European IT Grant",
        host_country="IT",
        host_country_name="Italy",
        region="Europe",
        source_url="https://dsu.regione.lombardia.it",
    )

    mock_score = CompositeScoreResult(
        scholarship_id=scholarship.scholarship_id,
        scholarship_name=scholarship.name,
        overall_match_score=75.0,
        rank=1,
        eligibility_score=70.0,
        true_funding_score=90.0,
        bilateral_bonus_score=0.0,
        academic_fit_score=80.0,
        doc_readiness_score=80.0,
        deadline_score=85.0,
        verification_score=80.0,
        competition_score=70.0,
        dimensions=[],
        cost_analysis=CostAnalysisResult(
            pre_application_pkr=20000,
            application_pkr=0,
            visa_travel_pkr=60000,
            settlement_pkr=40000,
            total_out_of_pocket_pkr=120000,
            total_out_of_pocket_usd=420,
            student_max_budget_pkr=250000,
            shortfall_pkr=0,
            is_within_budget=True,
            funding_score=90.0,
            cost_items=[],
            risk_warnings=[],
        ),
        blocking_reasons=[],
        pakistan_specific_advantages=[],
        is_recommended=True,
    )

    advisor = AdvisorAgent()
    roadmap = await advisor.generate_roadmap(scholarship, mock_score, profile)

    # Check urgent next actions contains low-GPA guidance
    assert any("Target Need-Based Grants" in action for action in roadmap.urgent_next_actions)
    assert any("Italian DSU Regional Grants" in action for action in roadmap.urgent_next_actions)
