import json
from pathlib import Path
import pytest
from schemas.scholarship import Scholarship
from schemas.student import StudentProfile

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def test_seed_scholarships_validity():
    scholarships_dir = DATA_DIR / "scholarships"
    assert scholarships_dir.exists()

    json_files = list(scholarships_dir.glob("*.json"))
    assert len(json_files) >= 5  # Europe, Asia, Americas, MENA, Oceania

    total_scholarships = 0
    for file in json_files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert isinstance(data, list)
            for sc_dict in data:
                # Validate against Pydantic schema
                sc = Scholarship.model_validate(sc_dict)
                assert sc.scholarship_id.startswith("SCH-")
                assert sc.host_country != ""
                assert sc.source_url.startswith("http")
                total_scholarships += 1

    assert total_scholarships >= 15


def test_seed_profiles_validity():
    profiles_dir = DATA_DIR / "profiles"
    assert profiles_dir.exists()

    profile_files = list(profiles_dir.glob("*.json"))
    assert len(profile_files) >= 5  # 5 demo profiles

    for file in profile_files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            profile = StudentProfile.model_validate(data)
            assert profile.personal.nationality == "PK"
            assert profile.academic.gpa_percentage > 0


def test_seed_costs_and_education_validity():
    costs_file = DATA_DIR / "pakistan_costs.json"
    edu_file = DATA_DIR / "pakistan_education.json"

    assert costs_file.exists()
    assert edu_file.exists()

    with open(costs_file, "r", encoding="utf-8") as f:
        costs_data = json.load(f)
        assert "pre_application" in costs_data
        assert "visa_and_travel" in costs_data

    with open(edu_file, "r", encoding="utf-8") as f:
        edu_data = json.load(f)
        assert "boards_of_intermediate_and_secondary_education" in edu_data
        assert len(edu_data["boards_of_intermediate_and_secondary_education"]) >= 20
