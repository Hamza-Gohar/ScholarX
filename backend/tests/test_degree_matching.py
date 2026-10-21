import pytest
from workflows.degree_matching import is_degree_match


def test_undergraduate_degree_matching():
    # Undergraduate target degrees
    targets = ["Bachelor's", "BS", "Undergraduate", "Intermediate / ICS / FSc / FA", "A-Levels"]
    
    for t in targets:
        assert is_degree_match(t, ["Bachelor's"]) is True
        assert is_degree_match(t, ["Bachelor's", "Master's", "PhD"]) is True
        assert is_degree_match(t, ["Bachelor's Exchange (Semester)"]) is True
        # Must never match Master's or PhD only
        assert is_degree_match(t, ["Master's"]) is False
        assert is_degree_match(t, ["MS Thesis", "PhD"]) is False
        assert is_degree_match(t, ["PhD", "Postdoctoral"]) is False


def test_graduate_degree_matching():
    # Graduate / Master's target degrees
    targets = ["Master's", "MS", "MSc", "MPhil", "Postgraduate"]
    
    for t in targets:
        assert is_degree_match(t, ["Master's"]) is True
        assert is_degree_match(t, ["MS Thesis"]) is True
        assert is_degree_match(t, ["Bachelor's", "Master's"]) is True
        # Must never match Bachelor's only
        assert is_degree_match(t, ["Bachelor's"]) is False
        assert is_degree_match(t, ["Diploma"]) is False


def test_phd_degree_matching():
    assert is_degree_match("PhD", ["PhD"]) is True
    assert is_degree_match("PhD", ["Bachelor's", "Master's", "PhD"]) is True
    assert is_degree_match("PhD", ["Bachelor's"]) is False
    assert is_degree_match("PhD", ["Master's"]) is False


def test_empty_or_none():
    assert is_degree_match(None, ["Bachelor's"]) is False
    assert is_degree_match("Bachelor's", None) is False
    assert is_degree_match("Bachelor's", []) is False
