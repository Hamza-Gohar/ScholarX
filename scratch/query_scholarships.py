import json
import sqlite3
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))
from schemas.scholarship import Scholarship
from schemas.student import (
    StudentProfile, PersonalInfo, AcademicRecord, LanguageProficiency,
    Preferences, EducationLevel, EnglishTestType
)
from workflows.eligibility import EligibilityInvestigator
from workflows.cost_analyzer import TrueCostAnalyzer
from workflows.ranking import RankingEngine

conn = sqlite3.connect("data/scholarx_sessions.db")
c = conn.cursor()
c.execute("SELECT data_json FROM scholarships_cache")
rows = c.fetchall()

print(f"Total scholarships in DB: {len(rows)}")

all_scholarships = [Scholarship.model_validate(json.loads(r[0])) for r in rows]

# Filter for Bachelor's / Undergrad + Fully Funded
undergrad_fully_funded = []
for sc in all_scholarships:
    degrees = [d.lower() for d in sc.eligibility.degree_levels]
    is_undergrad = any("bachelor" in d or "undergrad" in d or "bs" in d for d in degrees)
    if not is_undergrad:
        continue
    if sc.funding.funding_type != "FULL":
        continue
    undergrad_fully_funded.append(sc)

print(f"Total Undergrad Fully Funded: {len(undergrad_fully_funded)}")

def matches_cs_ai(sc: Scholarship) -> bool:
    fields = sc.eligibility.eligible_fields
    if not fields or any("all" in f.lower() for f in fields):
        return True
    for f in fields:
        f_low = f.lower()
        if any(term in f_low for term in [
            "computer", "ai", "artificial intelligence", "software", "stem", 
            "engineering", "technology", "informatics", "data science", "information"
        ]):
            return True
    return False

cs_ai_undergrad = [sc for sc in undergrad_fully_funded if matches_cs_ai(sc)]
print(f"Undergrad Fully Funded in CS/AI/STEM/All: {len(cs_ai_undergrad)}")

no_ielts_options = []
for sc in cs_ai_undergrad:
    lang = sc.language
    pk = sc.pakistan_requirements
    
    no_test = not lang.english_test_required
    accepts_moi = pk.accepts_moi_certificate
    host_prep = lang.host_language_prep
    
    if no_test or accepts_moi or host_prep:
        no_ielts_options.append((sc, {
            "no_test_required": no_test,
            "accepts_moi": accepts_moi,
            "host_prep": host_prep,
            "notes": lang.notes,
            "min_ielts": lang.minimum_ielts,
            "min_toefl": lang.minimum_toefl
        }))

print(f"Undergrad Fully Funded CS/AI + No IELTS/TOEFL (or MOI / Prep): {len(no_ielts_options)}")

for sc, lang_info in no_ielts_options:
    print("=" * 60)
    print(f"ID: {sc.scholarship_id} | Name: {sc.name}")
    print(f"Country: {sc.host_country_name} ({sc.host_country}) | Region: {sc.region}")
    print(f"Eligible Fields: {sc.eligibility.eligible_fields}")
    print(f"Degrees: {sc.eligibility.degree_levels}")
    print(f"Lang Info: NoTest={lang_info['no_test_required']}, AcceptsMOI={lang_info['accepts_moi']}, HostPrep={lang_info['host_prep']}")
    print(f"Lang Notes: {lang_info['notes']}")
    print(f"Funding: Tuition={sc.funding.tuition}, Stipend={sc.funding.monthly_stipend} (~PKR {sc.funding.monthly_stipend_pkr_approx}), Dorm={sc.funding.accommodation}, Airfare={sc.funding.travel_airfare}")
    print(f"Pakistan: BilateralQuota={sc.pakistan_requirements.pakistan_bilateral_quota} (Seats: {sc.pakistan_requirements.pakistan_quota_seats}), HEC={sc.pakistan_requirements.hec_managed}, USAT_Req={sc.pakistan_requirements.hec_usat_required}")
    print(f"Deadline: {sc.application_deadline} | Intake: {sc.academic_intake}")
    print(f"URL: {sc.source_url}")
