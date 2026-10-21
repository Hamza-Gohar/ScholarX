import urllib.request
import json

BASE_URL = "https://scolarx.vercel.app"

profiles = [
    {
        "name": "Dr. Zayd Tariq",
        "degree": "PhD",
        "field": "Artificial Intelligence & Quantum Computing",
        "regions": ["Asia", "Europe"],
        "gpa": 3.9,
        "ielts": 8.0
    },
    {
        "name": "Dr. Ayesha Noor",
        "degree": "PhD",
        "field": "Biotechnology & Molecular Medicine",
        "regions": ["Europe", "Americas"],
        "gpa": 3.82,
        "ielts": 7.5
    },
    {
        "name": "Dr. Bilal Farooq",
        "degree": "PhD",
        "field": "Aerospace & Mechanical Engineering",
        "regions": ["Asia", "Europe"],
        "gpa": 3.75,
        "ielts": 7.0
    },
    {
        "name": "Dr. Maryam Khan",
        "degree": "PhD",
        "field": "Environmental Engineering & Climate Science",
        "regions": ["Asia", "Europe", "Oceania"],
        "gpa": 3.65,
        "ielts": 6.5
    },
    {
        "name": "Dr. Usman Qureshi",
        "degree": "PhD",
        "field": "Development Economics & Quantitative Policy",
        "regions": ["Europe", "Americas", "Asia"],
        "gpa": 3.85,
        "ielts": 8.0
    }
]

print("=" * 80)
print("TESTING 5 PhD PROFILES ON LIVE VERCEL PRODUCTION (https://scolarx.vercel.app)")
print("=" * 80)

for p in profiles:
    name = p["name"]
    field = p["field"]
    regions = p["regions"]
    gpa = p["gpa"]
    ielts = p["ielts"]
    
    payload = {
        "personal": {
            "name": name,
            "intended_degree": p["degree"],
            "target_fields": [field],
            "target_regions": regions
        },
        "academic": {
            "degree_level": p["degree"],
            "field_of_study": field,
            "gpa_4_scale": gpa,
            "percentage": int(gpa / 4.0 * 100)
        },
        "language": {
            "has_english_test": True,
            "english_proficiency_test": "IELTS",
            "ielts_overall": ielts
        },
        "preferences": {
            "target_degree_level": p["degree"],
            "target_fields": [field],
            "preferred_regions": regions
        },
        "limit": 3
    }
    
    req = urllib.request.Request(
        f"{BASE_URL}/api/scholarships/match",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print(f"\n[PROFILE]: {name} | Field: {field}")
        print(f"  Regions: {regions} | GPA: {gpa} | Total Matched: {data.get('total_matched')}")
        print(f"  Database Engine: {data.get('database', {}).get('source')}")
        
        for idx, m in enumerate(data.get("matches", [])):
            sc = m.get("scholarship", {})
            score = m.get("match_score")
            sc_id = sc.get("id") or sc.get("scholarship_id")
            sc_name = sc.get("name") or sc.get("scholarship_name")
            sc_country = sc.get("country") or sc.get("host_country_name")
            reasons = m.get("match_reasons", [])
            academic_reason = reasons[2] if len(reasons) > 2 else "All Fields"
            print(f"  {idx+1}. [{sc_id}] {sc_name} ({sc_country}) - Match Score: {score}%")
            print(f"     {academic_reason[:95]}...")

