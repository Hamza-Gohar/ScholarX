import urllib.request
import json
import sqlite3

BASE_URL = "http://localhost:3000"

profiles = [
    {
        "id": "dr_zayd_ai",
        "name": "Dr. Zayd Tariq",
        "degree": "PhD",
        "field": "Artificial Intelligence & Quantum Computing",
        "gpa": 3.90,
        "pct": 90,
        "ielts": 8.0,
        "regions": ["Europe", "Asia"],
        "inst": "NUST Islamabad"
    },
    {
        "id": "dr_ayesha_biotech",
        "name": "Dr. Ayesha Noor",
        "degree": "PhD",
        "field": "Biotechnology & Molecular Medicine",
        "gpa": 3.82,
        "pct": 86,
        "ielts": 7.5,
        "regions": ["Europe", "Americas"],
        "inst": "Aga Khan University"
    },
    {
        "id": "dr_bilal_aerospace",
        "name": "Dr. Bilal Farooq",
        "degree": "PhD",
        "field": "Aerospace & Mechanical Engineering",
        "gpa": 3.75,
        "pct": 82,
        "ielts": 7.0,
        "regions": ["Asia", "Europe"],
        "inst": "GIKI"
    },
    {
        "id": "dr_maryam_climate",
        "name": "Dr. Maryam Khan",
        "degree": "PhD",
        "field": "Environmental Engineering & Climate Science",
        "gpa": 3.65,
        "pct": 78,
        "ielts": 6.5,
        "regions": ["Asia", "Europe", "Oceania"],
        "inst": "UET Lahore"
    },
    {
        "id": "dr_usman_econ",
        "name": "Dr. Usman Qureshi",
        "degree": "PhD",
        "field": "Development Economics & Quantitative Policy",
        "gpa": 3.85,
        "pct": 88,
        "ielts": 8.0,
        "regions": ["Europe", "Americas", "Asia"],
        "inst": "LUMS"
    }
]

print("================================================================================")
print("TESTING 5 PhD PROFILES ACROSS END-TO-END MATCHING PIPELINE")
print("================================================================================")

for p in profiles:
    session_id = f"sess-phd-{p['id']}"
    payload = {
        "session_id": session_id,
        "profile": {
            "personal": {
                "name": p["name"],
                "city": "Islamabad",
                "intended_degree": p["degree"],
                "target_fields": [p["field"]],
                "target_regions": p["regions"]
            },
            "academic": {
                "current_level": "Master's / MS / MSc / MPhil",
                "degree_level": p["degree"],
                "field_of_study": p["field"],
                "gpa_4_scale": p["gpa"],
                "percentage": p["pct"],
                "institution": p["inst"]
            },
            "language": {
                "has_english_test": True,
                "english_proficiency_test": "IELTS",
                "ielts_overall": p["ielts"]
            },
            "preferences": {
                "target_degree_level": p["degree"],
                "target_fields": [p["field"]],
                "preferred_regions": p["regions"],
                "max_out_of_pocket_pkr": 100000
            }
        },
        "limit": 5
    }
    
    # 1. Initialize mission via /api/discover
    disc_req = urllib.request.Request(
        f"{BASE_URL}/api/discover",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(disc_req) as resp:
        disc_res = json.loads(resp.read().decode("utf-8"))
        
    # 2. Query matches via /api/scholarships/match
    match_req = urllib.request.Request(
        f"{BASE_URL}/api/scholarships/match",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(match_req) as resp:
        match_res = json.loads(resp.read().decode("utf-8"))
        
    print(f"\n[PROFILE]: {p['name']} | Degree: {p['degree']} | Field: {p['field']}")
    print(f"  Regions: {p['regions']} | GPA: {p['gpa']} | IELTS: {p['ielts']}")
    print(f"  /api/discover Session Status: {disc_res.get('status')} | Mode: {disc_res.get('mode')} | Engine: {disc_res.get('data_source')}")
    print(f"  /api/scholarships/match Total Matched: {match_res.get('total_matched')} | Eligible: {match_res.get('ok')}")
    print(f"  Message: {match_res.get('message')}")
    
    matches = match_res.get("matches", [])
    print("  Top 3 Tailored Scholarships:")
    for idx, m in enumerate(matches[:3]):
        sc = m.get("scholarship", {})
        score = m.get("match_score")
        cost = m.get("funding_summary", {})
        stipend = cost.get("monthlyStipendPkr", 0)
        reasons = m.get("match_reasons", [])
        academic_reason = reasons[2] if len(reasons) > 2 else "All Fields"
        print(f"    {idx+1}. [{sc.get('id')}] {sc.get('name')} ({sc.get('country')})")
        print(f"       Score: {score}% | Monthly Living Allowance: PKR {stipend:,.0f} | Status: {cost.get('budgetStatus', 'N/A')}")
        print(f"       {academic_reason}")

