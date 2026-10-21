
from workflows.field_matching import is_field_match, get_field_categories

def test_exact_field_matching():
    # Direct match in CS
    match, score = is_field_match(["Computer Science"], ["Computer Science", "Information Systems"])
    assert match is True
    assert score == 1.0

    # Direct match in Civil Engineering
    match, score = is_field_match(["Civil & Environmental Engineering"], ["Civil Engineering", "Structural Engineering"])
    assert match is True
    assert score == 1.0

    # Direct match in Business
    match, score = is_field_match(["Business Administration & Management"], ["Business", "Finance"])
    assert match is True
    assert score == 1.0

def test_cognate_field_matching():
    # AI -> CS cognate
    match, score = is_field_match(["Artificial Intelligence & Machine Learning"], ["Computer Science", "Information Technology"])
    assert match is True
    assert score >= 0.95

    # Business -> Economics cognate
    match, score = is_field_match(["Business Administration & Management"], ["Economics", "Public Policy"])
    assert match is True
    assert score >= 0.90

def test_universal_bilateral_flagship():
    # Bilateral scholarships covering All Fields
    match, score = is_field_match(["Civil & Environmental Engineering"], ["All Fields", "Computer Science"])
    assert match is True
    assert score >= 0.85

    # Türkiye Bursları name check
    match, score = is_field_match(["Mechanical & Mechatronics Engineering"], ["Engineering"], scholarship_name="Türkiye Bursları Scholarship Program")
    assert match is True
    assert score >= 0.85

def test_strict_discipline_mismatch():
    # Civil Engineering student vs strictly CS/AI scholarship
    match, score = is_field_match(["Civil & Environmental Engineering"], ["Computer Science", "Artificial Intelligence", "Data Science"])
    assert match is False
    assert score == 0.0

    # Business student vs strictly Medical Sciences
    match, score = is_field_match(["Business Administration & Management"], ["Medicine", "Surgery", "Clinical Pharmacy"])
    assert match is False
    assert score == 0.0


def test_pakistani_acronym_expansion():
    # CS -> Computer Science
    match, score = is_field_match(["CS"], ["Computer Science", "Information Systems"])
    assert match is True
    assert score == 1.0

    # SE -> Software Engineering
    match, score = is_field_match(["SE"], ["Software Engineering"])
    assert match is True
    assert score == 1.0

    # EE -> Electrical Engineering
    match, score = is_field_match(["EE"], ["Electrical Engineering"])
    assert match is True
    assert score == 1.0

    # ME -> Mechanical Engineering
    match, score = is_field_match(["ME"], ["Mechanical Engineering"])
    assert match is True
    assert score == 1.0

    # BBA -> Business Administration
    match, score = is_field_match(["BBA"], ["Business Administration"])
    assert match is True
    assert score == 1.0

    # MBBS -> Medicine
    match, score = is_field_match(["MBBS"], ["Medicine", "Clinical Medicine"])
    assert match is True
    assert score == 1.0

    # DS -> Data Science
    match, score = is_field_match(["DS"], ["Data Science"])
    assert match is True
    assert score == 1.0

