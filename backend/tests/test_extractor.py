import pytest
from unittest.mock import AsyncMock, patch
from schemas.scholarship import Scholarship, FundingType, ScholarshipStatus
from tools.extractor import ScholarshipExtractor


@pytest.mark.asyncio
async def test_scholarship_extractor_parsing():
    raw_markdown = """
    # Stipendium Hungaricum Scholarship 2027
    Country: Hungary
    The Stipendium Hungaricum Scholarship Programme was launched by the Hungarian Government.
    Coverage: Full tuition fee exemption, monthly stipend of HUF 43,700 for bachelor and master students,
    dormitory placement or housing allowance of HUF 40,000/month, and health insurance.
    Eligibility: Open to Pakistani citizens through Higher Education Commission (HEC) Pakistan bilateral quota of 400 seats.
    Target fields: Computer Science, Engineering, AI, Medicine.
    Deadline: 15 January 2027.
    English requirement: IELTS 5.5 minimum.
    """

    extractor = ScholarshipExtractor()

    # Mock LLM response
    mock_extracted_scholarship = Scholarship(
        scholarship_id="SCH-EXTRACTED-001",
        name="Stipendium Hungaricum Scholarship",
        host_country="HU",
        host_country_name="Hungary",
        region="Europe",
        source_url="https://stipendiumhungaricum.hu",
        funding={
            "funding_type": "FULL",
            "tuition": "100% Exemption",
            "accommodation": "Free Dormitory or HUF 40,000 allowance",
            "monthly_stipend": "HUF 43,700",
            "travel_airfare": "NOT_COVERED",
            "health_insurance": "Full TAJ coverage",
        },
        pakistan_requirements={
            "pakistan_eligible": True,
            "pakistan_bilateral_quota": True,
            "pakistan_quota_seats": 400,
            "hec_managed": True,
            "hec_usat_required": True,
        },
        language={
            "english_test_required": True,
            "minimum_ielts": 5.5,
        },
        eligibility={
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "eligible_fields": ["Computer Science", "Engineering", "AI"],
            "eligible_nationalities": ["Pakistan", "PK"],
        },
        application_deadline="2027-01-15",
        status=ScholarshipStatus.DISCOVERED,
    )

    with patch.object(extractor, "extract_scholarship", new_callable=AsyncMock) as mock_extract:
        mock_extract.return_value = mock_extracted_scholarship

        sc = await extractor.extract_scholarship(
            raw_text=raw_markdown,
            source_url="https://stipendiumhungaricum.hu",
            region="Europe",
        )

        assert sc is not None
        assert sc.name == "Stipendium Hungaricum Scholarship"
        assert sc.host_country == "HU"
        assert sc.pakistan_requirements.pakistan_bilateral_quota is True
        assert sc.funding.funding_type == FundingType.FULL
        assert sc.language.minimum_ielts == 5.5
