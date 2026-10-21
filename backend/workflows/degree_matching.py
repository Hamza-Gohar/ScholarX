"""
Deterministic Degree Matching Utility.
Ensures strict partitioning between:
- Undergraduate / Bachelor's (including Intermediate, FSc, ICS, A-Levels, BS)
- Graduate / Master's (including MS, MSc, MPhil, MASc, MCS)
- Doctorate / PhD (including Postdoctoral)
"""

from typing import List, Optional


def is_degree_match(target_degree: Optional[str], offered_degrees: Optional[List[str]]) -> bool:
    """
    Returns True if target_degree matches at least one degree in offered_degrees.
    Zero-tolerance for degree mismatches: an undergraduate applicant will never match
    a scholarship that exclusively offers Master's or PhD degrees.
    """
    if not target_degree or not offered_degrees:
        return False

    t_lower = target_degree.lower().strip()
    is_undergrad_target = any(
        k in t_lower
        for k in [
            "bachelor", "undergrad", "bs", "bba", "b.e", "be", "b.com", "bcom", "ll.b", "llb",
            "inter", "fsc", "ics", "fa", "a-level", "diploma", "12", "mbbs", "bds", "pharm-d", "pharmd", "dpt"
        ]
    ) or ("doctor of pharmacy" in t_lower)

    is_phd_target = any(k in t_lower for k in ["phd", "doctorate", "postdoc"]) or (
        "doctor" in t_lower and not any(p in t_lower for p in ["pharm-d", "pharmd", "pharmacy", "mbbs", "bds", "physical therapy", "dpt"])
    )

    is_master_target = (
        not is_undergrad_target
        and not is_phd_target
        and any(
            k in t_lower
            for k in [
                "master", "ms", "msc", "mphil", "postgrad", "masc", "mcs", "mba", "emba",
                "ll.m", "llm", "m.ed", "med", "m.eng", "meng", "16", "18"
            ]
        )
    )

    for od in offered_degrees:
        o_lower = od.lower().strip()
        if is_undergrad_target:
            if any(k in o_lower for k in ["bachelor", "undergrad", "bs", "diploma", "bba", "ll.b", "llb", "b.e", "be", "bcom", "b.com"]):
                return True
        elif is_phd_target:
            if any(k in o_lower for k in ["phd", "doctor", "postdoc"]):
                return True
        elif is_master_target:
            if any(k in o_lower for k in ["master", "ms", "msc", "mphil", "masc", "mcs", "mba", "llm", "ll.m"]):
                return True

    return False


def get_degree_scholarship_limit(target_degree: Optional[str]) -> int:
    """
    Returns the maximum number of scholarships to output based on target degree level:
    - PhD / Doctorate: 30
    - Master's / Graduate: 20
    - Bachelor's / Undergraduate: 15
    Defaults to 15 if unspecified or undergraduate.
    """
    if not target_degree:
        return 15

    t_lower = target_degree.lower().strip()
    if any(k in t_lower for k in ["phd", "doctorate", "postdoc"]) and not any(p in t_lower for p in ["pharm-d", "pharmd", "pharmacy", "mbbs", "bds", "dpt"]):
        return 30
    if any(k in t_lower for k in ["master", "ms", "msc", "mphil", "postgrad", "masc", "mcs", "mba", "emba", "ll.m", "llm", "18"]):
        return 20
    if any(k in t_lower for k in ["bachelor", "undergrad", "bs", "bba", "b.e", "be", "b.com", "bcom", "ll.b", "llb", "inter", "fsc", "ics", "fa", "a-level", "diploma", "12", "16", "mbbs", "bds", "pharm-d", "pharmd", "dpt"]):
        return 15

    return 15

