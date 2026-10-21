"""
Deterministic Discipline & Field Matching Engine.
Matches student target disciplines to scholarship eligible fields with zero tolerance
for cross-faculty hallucinations while honoring multi-disciplinary and bilateral quotas.
"""

import re
from typing import List, Optional, Set, Tuple

# Field Category Taxonomies & Synonyms across All Major Academic Faculties
FIELD_TAXONOMY = {
    "cs_it": {
        "keywords": {
            "computer", "computing", "software", "informatics", "information technology",
            "information systems", "it", "web", "programming", "cloud", "systems", "distributed"
        },
        "display": "Computer Science & IT",
    },
    "ai_ds": {
        "keywords": {
            "artificial intelligence", "ai", "machine learning", "deep learning",
            "data science", "data analytics", "robotics", "intelligent systems",
            "computer vision", "natural language processing", "nlp", "big data"
        },
        "display": "Artificial Intelligence & Data Science",
    },
    "cybersecurity": {
        "keywords": {
            "cyber", "cybersecurity", "cyber security", "information security",
            "network security", "cryptography", "systems & security"
        },
        "display": "Cyber Security",
    },
    "medicine_health": {
        "keywords": {
            "medicine", "medical", "clinical", "surgery", "surgical", "dentistry",
            "dental", "pharmacy", "pharmacology", "nursing", "public health",
            "epidemiology", "toxicology", "health informatics", "health sciences",
            "biomedical", "biomedical sciences", "oncology"
        },
        "display": "Medicine & Clinical Health Sciences",
    },
    "physics_math": {
        "keywords": {
            "physics", "quantum", "theoretical physics", "astrophysics", "optics",
            "condensed matter", "high energy physics", "mathematics", "applied mathematics",
            "pure mathematics", "statistics", "actuarial", "mathematical"
        },
        "display": "Physics & Mathematical Sciences",
    },
    "chemistry_biochem": {
        "keywords": {
            "chemistry", "chemical", "organic chemistry", "inorganic chemistry",
            "biochemistry", "analytical chemistry", "polymer", "chemical biology",
            "chemical engineering"
        },
        "display": "Chemistry & Chemical Sciences",
    },
    "biology_lifesciences": {
        "keywords": {
            "biology", "biological", "molecular biology", "genetics", "biotechnology",
            "bioinformatics", "microbiology", "immunology", "cellular biology",
            "life science", "life sciences", "zoology", "botany", "genomics"
        },
        "display": "Biological & Life Sciences",
    },
    "mechanical_aero": {
        "keywords": {
            "mechanical", "mechatronics", "aerospace", "aeronautical", "automotive",
            "manufacturing", "thermal", "robotics & control"
        },
        "display": "Mechanical & Aerospace Engineering",
    },
    "civil_env": {
        "keywords": {
            "civil", "structural", "construction", "infrastructure", "transportation",
            "water resources", "environmental engineering", "urban planning"
        },
        "display": "Civil & Structural Engineering",
    },
    "electrical_electronics": {
        "keywords": {
            "electrical", "electronics", "telecommunications", "telecom", "embedded",
            "semiconductor", "microelectronics", "power engineering", "signal processing"
        },
        "display": "Electrical & Electronics Engineering",
    },
    "materials_petro": {
        "keywords": {
            "materials science", "materials engineering", "metallurgy", "petroleum",
            "petroleum engineering", "mining", "nuclear engineering", "nanotechnology"
        },
        "display": "Materials & Petroleum Engineering",
    },
    "arts_humanities_design": {
        "keywords": {
            "arts", "fine arts", "visual arts", "design", "architecture",
            "interior design", "fashion", "music", "literature", "linguistics",
            "history", "philosophy", "humanities", "performing arts", "cultural studies"
        },
        "display": "Arts, Humanities, Architecture & Design",
    },
    "business_mgmt": {
        "keywords": {
            "business", "management", "administration", "mba", "commerce", "finance",
            "marketing", "supply chain", "accounting", "entrepreneurship"
        },
        "display": "Business Administration & Management",
    },
    "economics_policy": {
        "keywords": {
            "economics", "economy", "public policy", "policy", "international relations",
            "governance", "social sciences", "development studies", "political science"
        },
        "display": "Economics & Public Policy",
    },
    "law_legal": {
        "keywords": {
            "law", "llm", "legal", "human rights", "international law",
            "humanitarian law", "jurisprudence", "justice"
        },
        "display": "Law & Legal Studies",
    },
    "agriculture_vet_env": {
        "keywords": {
            "agriculture", "agricultural", "agronomy", "horticulture", "forestry",
            "veterinary", "plant sciences", "animal sciences", "food science",
            "soil science", "environmental sciences", "climate", "sustainability"
        },
        "display": "Agriculture, Veterinary & Environmental Sciences",
    },
}

# Cross-disciplinary affinity matrix: pairs that share substantial coursework
COGNATE_CATEGORIES = {
    ("cs_it", "ai_ds"): 0.95,
    ("cs_it", "cybersecurity"): 0.95,
    ("ai_ds", "cybersecurity"): 0.90,
    ("electrical_electronics", "cs_it"): 0.88,
    ("electrical_electronics", "mechanical_aero"): 0.88,
    ("mechanical_aero", "ai_ds"): 0.85,  # Robotics/Mechatronics
    ("mechanical_aero", "materials_petro"): 0.88,
    ("chemistry_biochem", "biology_lifesciences"): 0.92,
    ("chemistry_biochem", "materials_petro"): 0.88,
    ("biology_lifesciences", "medicine_health"): 0.92,
    ("physics_math", "electrical_electronics"): 0.88,
    ("physics_math", "mechanical_aero"): 0.85,
    ("physics_math", "cs_it"): 0.82,
    ("business_mgmt", "economics_policy"): 0.92,
    ("law_legal", "economics_policy"): 0.85,
    ("civil_env", "agriculture_vet_env"): 0.82,
    ("biology_lifesciences", "agriculture_vet_env"): 0.88,
}


# Pakistani Academic Acronym Expansion Map
PAKISTANI_ACADEMIC_ACRONYMS = {
    "cs": "computer science",
    "se": "software engineering",
    "ee": "electrical engineering",
    "ce": "civil engineering computer engineering",
    "me": "mechanical engineering",
    "bba": "business administration",
    "mba": "business administration",
    "mbbs": "medicine surgery",
    "bds": "dentistry",
    "ds": "data science",
    "ai": "artificial intelligence",
    "it": "information technology",
    "ir": "international relations",
    "llb": "law",
    "llm": "law",
    "dpt": "physical therapy",
    "pharm-d": "pharmacy",
    "pharma-d": "pharmacy",
    "b.arch": "architecture",
    "arch": "architecture",
    "fin": "finance",
    "econ": "economics",
    "biotech": "biotechnology",
}


def expand_field_acronyms(text: str) -> str:
    """Expands common Pakistani academic degree and discipline acronyms using whole-word matching."""
    if not text:
        return ""
    words = text.split()
    expanded_words = []
    for w in words:
        clean_w = re.sub(r"[^\w\.-]", "", w.lower())
        if clean_w in PAKISTANI_ACADEMIC_ACRONYMS:
            expanded_words.append(PAKISTANI_ACADEMIC_ACRONYMS[clean_w])
        else:
            expanded_words.append(w)
    return " ".join(expanded_words)


def _clean_tokens(text: str) -> Set[str]:
    """Extracts alphanumeric words in lower case after expanding acronyms."""
    expanded = expand_field_acronyms(text)
    return set(re.findall(r"\b[a-z]{2,}\b", expanded.lower()))


def get_field_categories(field_str: str) -> Set[str]:
    """Identifies taxonomy category keys for a given field string."""
    expanded = expand_field_acronyms(field_str)
    f_lower = expanded.lower()
    categories = set()
    for cat_key, cat_data in FIELD_TAXONOMY.items():
        for kw in cat_data["keywords"]:
            if kw in f_lower:
                categories.add(cat_key)
                break
    return categories


def is_field_match(
    target_fields: Optional[List[str]],
    eligible_fields: Optional[List[str]],
    scholarship_name: str = "",
) -> Tuple[bool, float]:
    """
    Evaluates compatibility between applicant target field(s) and scholarship eligible fields.
    Returns (is_match, compatibility_score: 0.0 to 1.0).

    Scoring Tiers:
    - 1.00: Exact or direct keyword match in designated field.
    - 0.95: Close cognate discipline (e.g. AI student applying to CS program).
    - 0.90: Broad Engineering / STEM match if target is in an engineering discipline.
    - 0.85: Open / Bilateral Quota program offering \"All Fields\" or general scholarship.
    - 0.00: Non-compatible discipline (e.g. Civil Engineering student applying to strictly AI Lab fellowship).
    """
    # If no target fields specified, open to everything
    if not target_fields:
        return True, 1.0

    clean_targets = [expand_field_acronyms(t.strip()) for t in target_fields if t and t.strip()]
    if not clean_targets:
        return True, 1.0

    ef_list = eligible_fields or []
    ef_text = " ".join(ef_list).lower()
    name_lower = scholarship_name.lower()

    # 1. Universal / Bilateral Open Programs
    universal_markers = [
        "all fields", "all disciplines", "any discipline", "open to all",
        "all academic", "any field", "general quota"
    ]
    if any(m in ef_text for m in universal_markers) or any(m in name_lower for m in ["bilateral program", "government scholarship", "bursları", "burslari", "hungaricum"]):
        return True, 0.88

    # If eligible_fields is empty, treat as general
    if not ef_list:
        return True, 0.85

    # 2. Extract categories
    target_categories: Set[str] = set()
    for t in clean_targets:
        target_categories.update(get_field_categories(t))

    eligible_categories: Set[str] = set()
    for e in ef_list:
        eligible_categories.update(get_field_categories(e))

    # 3. Direct Category Intersection
    direct_common = target_categories.intersection(eligible_categories)
    if direct_common:
        return True, 1.0

    # 4. Token Overlap Check
    target_tokens: Set[str] = set()
    for t in clean_targets:
        target_tokens.update(_clean_tokens(t))

    generic_stop = {"and", "for", "with", "the", "degree", "studies", "department", "school"}
    meaningful_target = target_tokens - generic_stop

    for e in ef_list:
        e_tokens = _clean_tokens(e) - generic_stop
        overlap = meaningful_target.intersection(e_tokens)
        if overlap:
            if overlap == {"engineering"} or overlap == {"science"}:
                return True, 0.90
            return True, 1.0

    # 5. Cognate Category Check
    best_cognate_score = 0.0
    for tc in target_categories:
        for ec in eligible_categories:
            pair = (tc, ec) if (tc, ec) in COGNATE_CATEGORIES else (ec, tc)
            if pair in COGNATE_CATEGORIES:
                score = COGNATE_CATEGORIES[pair]
                if score > best_cognate_score:
                    best_cognate_score = score

    if best_cognate_score > 0.0:
        return True, best_cognate_score

    # 6. Broad Engineering catch-all
    is_target_engineering = any("engineering" in t.lower() for t in clean_targets)
    is_eligible_engineering = any("engineering" in e.lower() for e in ef_list)
    if is_target_engineering and is_eligible_engineering:
        return True, 0.88

    return False, 0.0
