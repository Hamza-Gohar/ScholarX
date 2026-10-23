"""
Test suite to verify that SCHOLARX functions 100% offline and is fully resilient
to typos/misspellings when online spelling-correction/Groq is unavailable.
"""

import pytest
import os
from config import get_settings
from workflows.field_matching import is_field_match, get_field_categories
from db.session_store import get_session_store
from tools.document_extractor import DocumentExtractor


def test_typo_academic_field_matching():
    """Verify that typos and misspellings correctly map to target fields without Groq."""
    typo_cases = [
        (["compter scince"], ["Computer Science"], True),
        (["machne lerning"], ["Artificial Intelligence & Machine Learning"], True),
        (["electrcial engr"], ["Electrical Engineering"], True),
        (["bussines admistration"], ["Business Administration & Management"], True),
        (["finence"], ["Finance", "Economics"], True),
        (["biomdical"], ["Biomedical Engineering"], True),
        (["civiil enginering"], ["Civil & Environmental Engineering"], True),
        (["data scence"], ["Data Science & Analytics"], True),
    ]

    for student_field, target_fields, expected_match in typo_cases:
        match, score = is_field_match(student_field, target_fields)
        assert match is expected_match, f"Failed match for {student_field} against {target_fields}"
        assert score > 0.0, f"Expected non-zero score for {student_field}"


def test_unrecognized_field_fallback():
    """Verify unclassifiable fields still match universal / bilateral opportunities offline."""
    weird_field = ["completely unknown interdisciplinary discipline"]
    match, score = is_field_match(weird_field, ["All Fields", "General"])
    assert match is True
    assert score >= 0.75


@pytest.mark.asyncio
async def test_offline_query_scholarships_with_typo():
    """Verify that store.query_scholarships retrieves results even with misspelled queries."""
    store = get_session_store()
    items, total = await store.query_scholarships(search="compter scince", limit=10)
    assert total > 0 or len(items) > 0, "Expected scholarships to be found for misspelled query 'compter scince'"

    items_ee, total_ee = await store.query_scholarships(search="electrcial", limit=10)
    assert total_ee > 0 or len(items_ee) > 0, "Expected scholarships for 'electrcial'"


@pytest.mark.asyncio
async def test_offline_search_scholarships_for_profile():
    """Verify that search_scholarships_for_profile_detailed retrieves scholarships with typo profile."""
    store = get_session_store()
    profile = {
        "field_of_study": "compter scince and machne lerning",
        "degree_level": "Masters",
        "gpa": "3.6",
        "target_countries": ["Germany", "United States", "United Kingdom"],
        "nationality": "Pakistan"
    }

    results = await store.search_scholarships_for_profile_detailed(profile, limit=15)
    assert len(results) > 0, "Expected detailed search to return scholarships for student with typos"


def test_offline_deterministic_document_extraction():
    """Verify offline extraction extracts profile information without network/LLM calls."""
    cv_text = """
    CURRICULUM VITAE
    Name: Muhammad Ali
    City: Lahore
    Education:
    Bachelor of Science in Computer Science
    FAST NUCES, Lahore (2020-2024)
    CGPA: 3.82 / 4.0
    Test Scores:
    IELTS Overall: 7.5
    Research Interests: Machine Learning
    """

    extractor = DocumentExtractor()
    data = extractor._extract_deterministic_offline(cv_text)
    assert data["personal"]["name"] == "Muhammad Ali"
    assert data["personal"]["city"] == "Lahore"
    assert data["academic"]["gpa_4_scale"] == 3.82
    assert data["language"]["ielts_overall"] == 7.5
    assert data["academic"]["field_of_study"] == "Computer Science"
    assert data["preferences"]["target_degree_level"] in ["Bachelor's", "Master's"]


def test_offline_chat_extraction():
    """Verify offline chat response generator parses updates and responds sensibly."""
    extractor = DocumentExtractor()
    chat_message = "Hi, my marks are 85% and I want to study for my Master's in compter scince. I also have an IELTS score of 7.0."
    res = extractor._extract_chat_deterministic_offline(chat_message)

    updates = res["extracted_updates"]
    reply = res["assistant_reply"]

    assert updates["academic"]["field_of_study"] == "Computer Science"
    assert updates["language"]["ielts_overall"] == 7.0
    assert "Computer Science" in reply or "IELTS" in reply
