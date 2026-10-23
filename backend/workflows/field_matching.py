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

# Fast offline dictionary for common academic discipline typos and colloquial shorthand
FAST_ACADEMIC_TYPO_DICT = {
    "compter scince": "computer science",
    "computr scince": "computer science",
    "computer scence": "computer science",
    "computr science": "computer science",
    "comp science": "computer science",
    "compsci": "computer science",
    "softwre enginering": "software engineering",
    "softwre engineering": "software engineering",
    "software eng": "software engineering",
    "software engg": "software engineering",
    "soft eng": "software engineering",
    "artifcial intelgence": "artificial intelligence",
    "artificial intellegence": "artificial intelligence",
    "artifical intelligence": "artificial intelligence",
    "artifical inteligence": "artificial intelligence",
    "data scince": "data science",
    "data scence": "data science",
    "machne lerning": "machine learning",
    "machine lerning": "machine learning",
    "deep lerning": "deep learning",
    "cybr security": "cybersecurity",
    "cyber secrity": "cybersecurity",
    "cyber sec": "cybersecurity",
    "electrcial engenering": "electrical engineering",
    "electrcial engineering": "electrical engineering",
    "electrical engr": "electrical engineering",
    "electrical engg": "electrical engineering",
    "mechanical engg": "mechanical engineering",
    "mechanical engr": "mechanical engineering",
    "mechnical engineering": "mechanical engineering",
    "civil engg": "civil engineering",
    "civil engr": "civil engineering",
    "biomdical": "biomedical engineering",
    "biomedical engg": "biomedical engineering",
    "chemical engg": "chemical engineering",
    "chemical engr": "chemical engineering",
    "mechatronics engg": "mechatronics",
    "aeronautical engg": "aerospace engineering",
    "bussines admistration": "business administration",
    "business admistration": "business administration",
    "bussiness administration": "business administration",
    "business admin": "business administration",
    "electrcial": "electrical",
    "electrial": "electrical",
    "compter": "computer",
    "computr": "computer",
    "scince": "science",
    "scence": "science",
    "enginering": "engineering",
    "engenering": "engineering",
    "bussines": "business",
    "bussiness": "business",
    "admistration": "administration",
    "lerning": "learning",
    "finence": "finance",
    "econmics": "economics",
    "acounting": "accounting",
    "medecine": "medicine",
    "biotechnolgy": "biotechnology",
}

import difflib

# Precomputed canonical single-word keywords for fuzzy typo matching
ALL_CANONICAL_KEYWORDS: Set[str] = set()
for _cat in FIELD_TAXONOMY.values():
    for _kw in _cat["keywords"]:
        for _part in _kw.split():
            if len(_part) >= 4:
                ALL_CANONICAL_KEYWORDS.add(_part)
ALL_CANONICAL_KEYWORDS.update({"science", "engineering", "technology", "studies", "administration"})


def normalize_discipline_token(word: str) -> str:
    """Corrects single-word typos (e.g. 'compter' -> 'computer', 'scince' -> 'science') using SequenceMatcher."""
    w = word.lower().strip()
    if len(w) < 4:
        return w
    if w in ALL_CANONICAL_KEYWORDS:
        return w
    matches = difflib.get_close_matches(w, ALL_CANONICAL_KEYWORDS, n=1, cutoff=0.75)
    return matches[0] if matches else w


def normalize_field_offline(text: str) -> str:
    """Normalizes field of study offline using dictionary lookups and fuzzy typo correction."""
    if not text:
        return ""
    cleaned = text.strip().lower()
    if cleaned in FAST_ACADEMIC_TYPO_DICT:
        return FAST_ACADEMIC_TYPO_DICT[cleaned]
    
    # Check if a substring matches FAST_ACADEMIC_TYPO_DICT
    for typo, correction in FAST_ACADEMIC_TYPO_DICT.items():
        if typo in cleaned:
            cleaned = cleaned.replace(typo, correction)
            
    return cleaned


def expand_field_acronyms(text: str) -> str:
    """Expands common Pakistani academic degree and discipline acronyms using whole-word matching and typo tolerance."""
    if not text:
        return ""
    normalized = normalize_field_offline(text)
    words = normalized.split()
    expanded_words = []
    for w in words:
        clean_w = re.sub(r"[^\w\.-]", "", w.lower())
        if clean_w in PAKISTANI_ACADEMIC_ACRONYMS:
            expanded_words.append(PAKISTANI_ACADEMIC_ACRONYMS[clean_w])
        else:
            # Fuzzy match word against canonical academic keywords
            fuzzy_w = normalize_discipline_token(clean_w)
            expanded_words.append(fuzzy_w)
    return " ".join(expanded_words)


def _clean_tokens(text: str) -> Set[str]:
    """Extracts alphanumeric words in lower case after expanding acronyms and correcting typos."""
    expanded = expand_field_acronyms(text)
    tokens = set(re.findall(r"\b[a-z]{2,}\b", expanded.lower()))
    normalized_tokens = {normalize_discipline_token(t) for t in tokens}
    return normalized_tokens


def get_field_categories(field_str: str) -> Set[str]:
    """Identifies taxonomy category keys for a given field string with typo tolerance."""
    expanded = expand_field_acronyms(field_str)
    f_lower = expanded.lower()
    categories = set()
    for cat_key, cat_data in FIELD_TAXONOMY.items():
        for kw in cat_data["keywords"]:
            if kw in f_lower:
                categories.add(cat_key)
                break

    # If no category matched via substring, perform token-level check
    if not categories:
        tokens = _clean_tokens(field_str)
        for cat_key, cat_data in FIELD_TAXONOMY.items():
            cat_words = set()
            for kw in cat_data["keywords"]:
                cat_words.update(kw.split())
            if tokens.intersection(cat_words):
                categories.add(cat_key)

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
    - 0.85: Open / Bilateral Quota program offering "All Fields" or general scholarship.
    - 0.75: Resilient offline fallback for open programs when target field is unclassified.
    - 0.00: Non-compatible discipline.
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
        "all academic", "any field", "general quota", "various fields"
    ]
    if any(m in ef_text for m in universal_markers) or any(
        m in name_lower
        for m in [
            "bilateral program",
            "government scholarship",
            "bursları",
            "burslari",
            "hungaricum",
            "csc scholarship",
            "chinese government",
            "mext",
            "turkiye",
            "dsu regional",
            "arice",
            "commonwealth",
        ]
    ):
        return True, 0.88

    # If eligible_fields is empty, treat as general / open
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

    # 7. Resilient Fallback for Unclassified Target Fields:
    # If the student's field is misspelled or unclassified into our 16 taxonomies,
    # and the scholarship offers multiple broad fields, do not reject completely.
    if not target_categories and len(ef_list) >= 4:
        return True, 0.75

    return False, 0.0
