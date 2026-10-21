import json
import sqlite3
import urllib.request
import urllib.error

# Connect to database
DB_PATH = "scholarships_database.db"

profiles = [
    {
        "id": "profile_1_ai_quantum",
        "name": "Dr. Zayd Tariq",
        "degree": "PhD",
        "field": "Artificial Intelligence & Quantum Computing",
        "gpa_4": 3.90,
        "percentage": 90,
        "ielts": 8.0,
        "regions": ["Europe", "Asia"],
        "institution": "National University of Sciences and Technology (NUST), Islamabad",
        "budget": 100000,
        "has_ielts": True
    },
    {
        "id": "profile_2_biotech",
        "name": "Dr. Ayesha Noor",
        "degree": "PhD",
        "field": "Biotechnology & Molecular Medicine",
        "gpa_4": 3.82,
        "percentage": 86,
        "ielts": 7.5,
        "regions": ["Europe", "Americas"],
        "institution": "Aga Khan University (AKU), Karachi",
        "budget": 120000,
        "has_ielts": True
    },
    {
        "id": "profile_3_aerospace",
        "name": "Dr. Bilal Farooq",
        "degree": "PhD",
        "field": "Aerospace & Mechanical Engineering",
        "gpa_4": 3.75,
        "percentage": 82,
        "ielts": 7.0,
        "regions": ["Asia", "Europe"],
        "institution": "Ghulam Ishaq Khan Institute (GIKI), Topi",
        "budget": 80000,
        "has_ielts": True
    },
    {
        "id": "profile_4_climate",
        "name": "Dr. Maryam Khan",
        "degree": "PhD",
        "field": "Environmental Engineering & Climate Science",
        "gpa_4": 3.65,
        "percentage": 78,
        "ielts": 6.5,
        "regions": ["Asia", "Europe", "Oceania"],
        "institution": "University of Engineering and Technology (UET), Lahore",
        "budget": 75000,
        "has_ielts": True
    },
    {
        "id": "profile_5_economics",
        "name": "Dr. Usman Qureshi",
        "degree": "PhD",
        "field": "Development Economics & Quantitative Policy",
        "gpa_4": 3.85,
        "percentage": 88,
        "ielts": 8.0,
        "regions": ["Europe", "Americas", "Asia"],
        "institution": "Lahore University of Management Sciences (LUMS), Lahore",
        "budget": 150000,
        "has_ielts": True
    }
]

print("=" * 80)
print("TEST 1: Direct Database Evaluation for 5 PhD Profiles")
print("=" * 80)

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

results_summary = []

for p in profiles:
    print(f"\nEvaluating Profile: {p['name']} ({p['field']})")
    print(f"Degree: {p['degree']} | GPA: {p['gpa_4']} ({p['percentage']}%) | IELTS: {p['ielts']} | Regions: {p['regions']}")
    
    # 1. Query scholarships matching Regions and PhD degree
    placeholders = ",".join(["?"] * len(p["regions"]))
    query = f"""
        SELECT * FROM scholarships 
        WHERE region IN ({placeholders}) COLLATE NOCASE
        AND (LOWER(degree_levels) LIKE '%phd%' OR LOWER(degree_levels) LIKE '%doctor%')
    """
    cursor.execute(query, p["regions"])
    rows = [dict(r) for r in cursor.fetchall()]
    total_region_phd = len(rows)
    
    # 2. Filter by GPA
    gpa_passed = [
        r for r in rows 
        if (p["percentage"] >= (r.get("min_gpa_percentage") or 60.0) or 
            p["gpa_4"] >= (r.get("min_gpa_4_scale") or 2.5))
    ]
    
    # 3. Filter by Language
    lang_passed = [
        r for r in gpa_passed
        if (bool(r.get("accepts_moi_certificate")) or 
            (p["has_ielts"] and p["ielts"] >= (r.get("ielts_minimum") or 0)))
    ]
    
    # 4. Filter by Subject/Field match against Subjects_included
    field_keywords = [w.lower() for w in p["field"].replace("&", " ").replace("/", " ").split() if len(w) > 3]
    subject_matched = []
    
    for r in lang_passed:
        subj_text = str(r.get("Subjects_included") or "").lower()
        name_text = str(r.get("name") or "").lower()
        
        # General scholarships accepting all fields
        is_general = any(g in subj_text for g in ["all academic", "all field", "all discipline", "open to all"]) or not subj_text
        
        # Direct keyword match
        has_field_match = any(kw in subj_text or kw in name_text for kw in field_keywords)
        
        if is_general or has_field_match:
            # Score the match
            match_type = "SPECIALIZED_FIELD_MATCH" if has_field_match else "GENERAL_DISCIPLINE_MATCH"
            r["_match_type"] = match_type
            subject_matched.append(r)
            
    # Score and rank matching scholarships
    def calculate_score(row):
        success_rate = float(row.get("success_rate_pakistan_percent") or 8.0)
        seats = float(row.get("pakistan_quota_seats") or (30.0 if row.get("pakistan_bilateral_quota") else 0.0))
        stipend = float(row.get("monthly_stipend_pkr_approx") or (120000.0 if row.get("funding_type") == "FULL" else 40000.0))
        comp = str(row.get("competition_level") or "MODERATE").upper()
        
        f_success = min(100.0, (success_rate / 35.0) * 100.0)
        f_seats = min(100.0, 45.0 + (seats / 280.0) * 55.0) if seats > 0 else 30.0
        f_stipend = min(100.0, (stipend / 300000.0) * 100.0)
        f_comp = 95.0 if comp == "LOW" else (85.0 if comp == "MODERATE" else (72.0 if comp == "HIGH" else 60.0))
        
        score = 0.35 * f_success + 0.25 * f_seats + 0.25 * f_stipend + 0.15 * f_comp
        if row.get("_match_type") == "SPECIALIZED_FIELD_MATCH":
            score += 5.0 # Field alignment bonus
        return round(score, 1)

    for r in subject_matched:
        r["_final_score"] = calculate_score(r)
        
    subject_matched.sort(key=lambda x: x["_final_score"], reverse=True)
    top_5 = subject_matched[:5]
    
    print(f"-> Region & Degree Pool: {total_region_phd} | GPA Filtered: {len(gpa_passed)} | Lang Filtered: {len(lang_passed)} | Subject Matched: {len(subject_matched)}")
    print("Top 3 Recommendations:")
    for i, top in enumerate(top_5[:3]):
        stipend_pkr = top.get('monthly_stipend_pkr_approx') or 120000
        print(f"  {i+1}. [{top['scholarship_id']}] {top['name']} ({top['host_country_name']}) - Score: {top['_final_score']} - Type: {top['_match_type']} - Stipend: PKR {stipend_pkr:,.0f}/mo")
        print(f"     Subjects: {str(top.get('Subjects_included'))[:90]}...")
        
    results_summary.append({
        "profile": p,
        "total_matched": len(subject_matched),
        "top_id": top_5[0]["scholarship_id"] if top_5 else None,
        "top_name": top_5[0]["name"] if top_5 else None,
        "top_score": top_5[0]["_final_score"] if top_5 else 0,
        "top_type": top_5[0]["_match_type"] if top_5 else None,
        "top_country": top_5[0]["host_country_name"] if top_5 else None,
    })

print("\n" + "=" * 80)
print("TEST 2: Calling Live System API (/api/scholarships/match) for All 5 Profiles")
print("=" * 80)

for p in profiles:
    url = "http://localhost:3000/api/scholarships/match"
    payload = {
        "personal": {
            "name": p["name"],
            "city": "Islamabad",
            "intended_degree": "PhD",
            "target_fields": [p["field"]],
            "target_regions": p["regions"]
        },
        "academic": {
            "degree_level": "PhD",
            "field_of_study": p["field"],
            "gpa_4_scale": p["gpa_4"],
            "percentage": p["percentage"],
            "institution": p["institution"]
        },
        "language": {
            "has_english_test": p["has_ielts"],
            "english_proficiency_test": "IELTS Academic",
            "ielts_overall": p["ielts"]
        },
        "preferences": {
            "target_degree_level": "PhD",
            "target_fields": [p["field"]],
            "preferred_regions": p["regions"],
            "max_out_of_pocket_pkr": p["budget"]
        },
        "limit": 5
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"\n[API MATCH] {p['name']} ({p['field']}):")
            print(f"  Status: {data.get('ok')} | Total Matched: {data.get('total_matched')}")
            for m in data.get("matches", [])[:3]:
                sc = m.get("scholarship", {})
                print(f"  * [{sc.get('id')}] {sc.get('name')} ({sc.get('country')}) - Score: {m.get('match_score')}")
    except Exception as e:
        print(f"API Error for {p['name']}: {e}")

