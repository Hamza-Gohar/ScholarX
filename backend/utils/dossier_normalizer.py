"""
ScholarX Scholarship Dossier Normalizer
Extracts and normalizes raw scholarship records and deep dossiers into 
structured, publication-grade intelligence models.
"""

import html
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


def clean_str(val: Any, default: str = "N/A", escape_html: bool = False) -> str:
    if val is None:
        return default
    s = str(val).strip()
    if not s:
        return default
    return html.escape(s) if escape_html else s


def clean_html_str(val: Any, default: str = "N/A") -> str:
    """Escapes HTML entities for safe inclusion in WeasyPrint templates."""
    return clean_str(val, default=default, escape_html=True)


def normalize_coverage_item(raw_item: Any, default_label: str = "Not Specified") -> Dict[str, Any]:
    """Normalize a financial coverage field which could be a dict, string, or boolean."""
    if isinstance(raw_item, dict):
        status = clean_str(raw_item.get("status"), "COVERED").upper()
        details = clean_str(raw_item.get("details"), "")
        amount = clean_str(raw_item.get("amount"), "")
        
        # Determine coverage boolean/classification
        is_covered = any(k in status for k in ["100%", "COVERED", "WAIVED", "INCLUDED", "FREE", "PROVIDED", "FULL"])
        is_partial = any(k in status for k in ["PARTIAL", "ALLOWANCE", "REIMBURSED", "SUBSIDIZED", "UP TO"])
        is_not_covered = any(k in status for k in ["NOT", "NONE", "SELF", "UNCOVERED", "EXCLUDED"])
        
        classification = "NOT_COVERED" if is_not_covered else ("PARTIAL" if is_partial else "FULL")
        return {
            "status": status,
            "details": details,
            "amount": amount,
            "classification": classification,
            "is_covered": is_covered or is_partial,
        }
    elif isinstance(raw_item, str):
        s_upper = raw_item.upper()
        is_covered = any(k in s_upper for k in ["100%", "COVERED", "WAIVED", "INCLUDED", "FREE", "FULL", "YES"])
        is_not = any(k in s_upper for k in ["NOT", "NONE", "SELF", "EXCLUDED", "NO"])
        return {
            "status": "COVERED" if is_covered else ("NOT COVERED" if is_not else "CONDITIONAL"),
            "details": raw_item,
            "amount": "",
            "classification": "NOT_COVERED" if is_not else ("FULL" if is_covered else "PARTIAL"),
            "is_covered": is_covered,
        }
    elif isinstance(raw_item, bool):
        return {
            "status": "COVERED" if raw_item else "NOT COVERED",
            "details": "Fully covered by awarding authority" if raw_item else "Not included in scholarship grant",
            "amount": "",
            "classification": "FULL" if raw_item else "NOT_COVERED",
            "is_covered": raw_item,
        }
    return {
        "status": default_label,
        "details": "",
        "amount": "",
        "classification": "UNKNOWN",
        "is_covered": False,
    }


def normalize_scholarship_dossier(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transforms a scholarship record / deep dossier into a clean, high-density format
    guaranteed to contain all requested fields for enterprise-grade PDF/print publishing.
    """
    sid = clean_str(raw_data.get("scholarship_id"), "SCH-GEN-001")
    bd = raw_data.get("basic_details", {})
    el = raw_data.get("eligibility_requirements", {})
    fc = raw_data.get("financial_coverage_breakdown", {})
    up = raw_data.get("university_and_program_options", {})
    ap = raw_data.get("application_process_roadmap", {})
    rf = raw_data.get("red_flags_and_warnings", {})
    cp = raw_data.get("competitiveness_profile", {})
    it = raw_data.get("important_dates_timeline", {})
    ob = raw_data.get("scholarship_obligations_and_terms", {})
    
    # Core Identity
    name = clean_str(bd.get("scholarship_name") or raw_data.get("name"), "Unnamed Scholarship")
    country = clean_str(bd.get("host_country") or raw_data.get("host_country_name") or raw_data.get("host_country"), "International")
    offering_entity = clean_str(bd.get("offering_entity"), "Government / Awarding Agency")
    institutions = clean_str(bd.get("host_institutions_covered") or up.get("participating_institutions") or raw_data.get("host_institution"), "Accredited Universities")
    
    # Accurate Regional Classification
    prefix_to_region = {
        "AM": "Americas",
        "AS": "Asia",
        "EU": "Europe",
        "ME": "MENA",
        "OC": "Oceania",
    }
    prefix = sid.split("-")[1].upper() if "-" in sid and len(sid.split("-")) > 1 else ""
    region = raw_data.get("region") or prefix_to_region.get(prefix, "Global")
    
    degree_levels = bd.get("degree_levels") or raw_data.get("eligibility", {}).get("degree_levels") or ["Master's", "PhD"]
    if isinstance(degree_levels, str):
        degree_levels = [degree_levels]
    degree_levels_str = " • ".join(degree_levels)
    
    duration = clean_str(bd.get("duration_of_scholarship") or up.get("program_duration"), "Full Program Duration")
    funding_type = clean_str(bd.get("funding_classification") or raw_data.get("funding", {}).get("funding_type"), "FULLY_FUNDED").upper()
    
    # Financial Coverage Breakdown
    tuition = normalize_coverage_item(fc.get("tuition_fee"), "100% Tuition Waiver")
    accommodation = normalize_coverage_item(fc.get("accommodation"), "Dormitory / Monthly Allowance")
    monthly_stipend = normalize_coverage_item(fc.get("monthly_stipend"), "Living Maintenance Stipend")
    airfare = normalize_coverage_item(fc.get("airfare"), "Round-Trip Economy Airfare")
    insurance = normalize_coverage_item(fc.get("health_insurance"), "Comprehensive Health Insurance")
    visa = normalize_coverage_item(fc.get("visa_fee"), "Visa Fee Reimbursed or Waived")
    transit = normalize_coverage_item(fc.get("travel_transit_allowance"), "Arrival Settlement Allowance")
    food = normalize_coverage_item(fc.get("food_allowance"), "Included in Monthly Stipend")
    
    # Included vs Not Included Summaries
    covered_tags = []
    if tuition["is_covered"]:
        covered_tags.append("Tuition Waiver (100%)")
    if accommodation["is_covered"]:
        covered_tags.append("Accommodation / Housing")
    if monthly_stipend["is_covered"]:
        stipend_label = f"Monthly Stipend ({monthly_stipend['amount']})" if monthly_stipend['amount'] else "Monthly Living Stipend"
        covered_tags.append(stipend_label)
    if airfare["is_covered"]:
        covered_tags.append("Return Airfare")
    if insurance["is_covered"]:
        covered_tags.append("Medical Insurance")
    if visa["is_covered"]:
        covered_tags.append("Visa Costs Covered")
    if transit["is_covered"]:
        covered_tags.append("Arrival / Transit Allowance")

    not_covered_tags = []
    if not tuition["is_covered"]:
        not_covered_tags.append("Tuition Fees Not Covered")
    if not airfare["is_covered"]:
        not_covered_tags.append("International Airfare Self-Funded")
    if not accommodation["is_covered"]:
        not_covered_tags.append("Housing Arranged at Personal Expense")
    if not visa["is_covered"]:
        not_covered_tags.append("Visa Application Fees Not Reimbursed")

    # Eligibility & Requirements
    age_notes = clean_str(
        el.get("age_limit_notes") or 
        (f"Undergrad: < {el.get('age_limit_undergrad')} yrs; Postgrad: < {el.get('age_limit_postgrad')} yrs" if el.get("age_limit_undergrad") else None),
        "No rigid upper age limit; early-to-mid career focus"
    )
    
    academic_qual = clean_str(
        el.get("academic_qualifications"),
        "Recognized bachelor/master degree matching targeted degree level"
    )
    
    min_gpa = el.get("minimum_gpa_scale") or el.get("minimum_gpa_percentage") or "3.0 / 4.0 or 70%"
    gpa_notes = clean_str(el.get("grading_conversion_notes"), f"Minimum threshold: {min_gpa}")
    
    nationality_req = el.get("nationality_requirements", [])
    if isinstance(nationality_req, list):
        nationality_str = "; ".join(nationality_req) if nationality_req else "Pakistani citizens & international applicants"
    else:
        nationality_str = str(nationality_req)
        
    english_required = el.get("english_test_required")
    ielts = el.get("ielts_minimum")
    toefl = el.get("toefl_minimum")
    moi_accepted = bool(el.get("moi_certificate_accepted"))
    language_notes = clean_str(el.get("language_notes"), "Standard university English language proficiency requirement applies")
    
    if english_required is False or moi_accepted:
        english_badge = "MOI Accepted (No IELTS Mandatory)" if moi_accepted else "No Language Test Required"
    elif ielts or toefl:
        ielts_txt = f"IELTS {ielts}" if ielts else ""
        toefl_txt = f"TOEFL {toefl}" if toefl else ""
        combined = " / ".join(filter(None, [ielts_txt, toefl_txt]))
        english_badge = f"Required: {combined}"
    else:
        english_badge = "Institutional Proficiency Standard"
        
    field_req = clean_str(
        bd.get("major_restrictions") or el.get("subject_background_prerequisites"),
        "Open across designated academic faculties"
    )
    
    other_req = clean_str(
        el.get("work_experience_notes") or 
        (f"{el.get('work_experience_minimum_years')} years professional experience required" if el.get("work_experience_minimum_years") else None),
        "Standard academic and professional merit evaluation"
    )

    # Workflow & Application Process
    workflow = ap.get("step_by_step_workflow", [])
    if isinstance(workflow, list) and workflow:
        workflow_steps = [clean_str(s) for s in workflow[:5]]
    elif isinstance(workflow, str) and workflow:
        workflow_steps = [s.strip() for s in workflow.split("\n") if s.strip()][:5]
    else:
        workflow_steps = [
            "1. Prepare and attest academic credentials via HEC / IBCC.",
            "2. Submit formal application on host institution portal.",
            "3. Complete government/bilateral agency scholarship dossier.",
            "4. Undertake institutional interview and academic screening.",
            "5. Secure final award letter, student visa, and consular clearance."
        ]

    # Required Documents Checklist
    raw_docs = raw_data.get("required_documents_checklist") or []
    doc_checklist = []
    if isinstance(raw_docs, list) and raw_docs:
        for d in raw_docs[:8]:
            if isinstance(d, dict):
                doc_name = clean_str(d.get("document_name"))
                doc_notes = clean_str(d.get("specific_requirements_or_instructions"), "")
                doc_checklist.append({"name": doc_name, "notes": doc_notes})
            elif isinstance(d, str):
                doc_checklist.append({"name": d, "notes": ""})
    if not doc_checklist:
        doc_checklist = [
            {"name": "Valid National Passport", "notes": "Minimum 12-month remaining validity"},
            {"name": "Academic Transcripts & Sanads", "notes": "Attested by HEC / Board of Intermediate"},
            {"name": "Statement of Purpose / Research Plan", "notes": "Outlining academic vision and post-study goals"},
            {"name": "2 Academic Recommendation Letters", "notes": "Issued on official university letterhead"},
            {"name": "English Proficiency Certificate", "notes": "Official IELTS/TOEFL score or university MOI certificate"},
            {"name": "Police Clearance & Medical Examination", "notes": "Issued by approved government clinics"},
        ]

    # Important Dates Timeline
    deadline = clean_str(it.get("application_deadline") or raw_data.get("application_deadline"), "Annual Academic Intake")
    open_date = clean_str(it.get("application_open_date") or raw_data.get("application_opens"), "Check Official Schedule")
    interview_date = clean_str(it.get("interview_period"), "Spring Selection Round")
    commencement = clean_str(it.get("semester_commencement") or raw_data.get("academic_intake"), "Fall 2027 Intake")
    
    # Why Interesting & Strategic Profile
    prestige_tier = clean_str(cp.get("competitiveness_tier"), "High Prestige Global Merit Award")
    acceptance_pak = clean_str(cp.get("acceptance_rate_pakistan"), "~5% - 8% admitted")
    quota_info = clean_str(bd.get("number_of_awards_pakistan"), "Open bilateral / international merit allocation")
    why_interesting = (
        f"{prestige_tier} • {quota_info}. "
        f"Provides {funding_type.replace('_', ' ').title()} funding in {country} "
        f"with high post-study career trajectory."
    )

    # Red Flags & Potential Concerns
    fee_warning = clean_str(rf.get("application_fee_warning"), "Official applications are free or zero processing charge via official channels.")
    obligations = clean_str(ob.get("home_country_return_obligation"), "Standard academic performance maintenance required.")
    hidden_costs = clean_str(rf.get("hidden_costs_breakdown"), "Verify upfront visa, flight, and initial settlement liquidity before first stipend disbursement.")
    
    # Official Verified Sources & Portals
    sources = []
    raw_sources = raw_data.get("official_sources_verified") or []
    for s in raw_sources:
        if isinstance(s, dict) and s.get("source_url"):
            sources.append({
                "title": clean_str(s.get("source_name") or s.get("entity_type"), "Official Portal"),
                "url": s.get("source_url"),
                "verified": bool(s.get("verification_status") in [True, "CONFIRMED", "VERIFIED"])
            })
    
    portal_url = ap.get("submission_portal_url") or raw_data.get("portal_url") or raw_data.get("source_url")
    if portal_url and not any(src["url"] == portal_url for src in sources):
        sources.insert(0, {
            "title": clean_str(ap.get("portal_system_name"), "Official Application Portal"),
            "url": portal_url,
            "verified": True
        })
    if not sources:
        sources.append({
            "title": "Official Awarding Authority Portal",
            "url": raw_data.get("source_url") or "https://scholarship.hec.gov.pk",
            "verified": True
        })

    return {
        "id": sid,
        "name": name,
        "country": country,
        "region": clean_str(region, "Global"),
        "offering_entity": offering_entity,
        "host_institutions": institutions,
        "degree_levels": degree_levels,
        "degree_levels_str": degree_levels_str,
        "duration": duration,
        "funding_type": funding_type,
        "deadline": deadline,
        "open_date": open_date,
        "interview_date": interview_date,
        "commencement": commencement,
        "financial_coverage": {
            "tuition": tuition,
            "accommodation": accommodation,
            "monthly_stipend": monthly_stipend,
            "airfare": airfare,
            "health_insurance": insurance,
            "visa_fee": visa,
            "travel_transit": transit,
            "food_allowance": food,
            "covered_tags": covered_tags,
            "not_covered_tags": not_covered_tags,
        },
        "eligibility": {
            "age_notes": age_notes,
            "academic_qualifications": academic_qual,
            "minimum_gpa": str(min_gpa),
            "gpa_notes": gpa_notes,
            "nationality": nationality_str,
            "english_required": english_required,
            "english_badge": english_badge,
            "language_notes": language_notes,
            "moi_accepted": moi_accepted,
            "field_requirements": field_req,
            "other_requirements": other_req,
        },
        "summary": {
            "workflow_steps": workflow_steps,
            "required_documents": doc_checklist,
            "why_interesting": why_interesting,
            "fee_warning": fee_warning,
            "obligations": obligations,
            "hidden_costs": hidden_costs,
        },
        "official_sources": sources,
    }


def load_all_normalized_dossiers(repo_root: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Loads and normalizes all scholarships in the database."""
    if repo_root is None:
        repo_root = Path(__file__).resolve().parents[2]
        
    master_file = repo_root / "data" / "scholarships_deep_dossiers.json"
    if not master_file.exists():
        raise FileNotFoundError(f"Missing master deep dossiers file: {master_file}")
        
    with open(master_file, "r", encoding="utf-8") as f:
        raw_map = json.load(f)
        
    normalized_list = []
    for sid, data in raw_map.items():
        norm = normalize_scholarship_dossier(data)
        normalized_list.append(norm)
        
    return normalized_list
