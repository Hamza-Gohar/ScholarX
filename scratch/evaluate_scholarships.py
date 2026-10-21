import json
import sqlite3
import sys
from pathlib import Path
from datetime import date

# Add backend to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))
from schemas.scholarship import Scholarship
from schemas.student import (
    StudentProfile, PersonalInfo, AcademicRecord, LanguageProficiency,
    Preferences, EducationLevel, EnglishTestType
)
from schemas.evidence import EvidenceTrail, SourceCitation
from workflows.eligibility import EligibilityInvestigator
from workflows.cost_analyzer import TrueCostAnalyzer
from workflows.deadline import DeadlineAnalyzer
from workflows.ranking import RankingEngine

# Create profile for an ICS student with NO IELTS / NO TOEFL
ics_student = StudentProfile(
    student_id="std-ics-user",
    session_id="sess-ics-query",
    personal=PersonalInfo(
        name="ICS Graduate",
        nationality="PK",
        country_of_residence="PK",
        city="Lahore",
        province="Punjab",
        age=19
    ),
    academic=AcademicRecord(
        current_level=EducationLevel.INTERMEDIATE,
        education_system="Pakistani",
        years_of_education=12,
        field_of_study="Computer Science",
        board_university="BISE Lahore / Intermediate Board",
        gpa_percentage=86.0,
        gpa_4_scale=3.8,
        uk_classification="First Class Honours",
        graduation_year=2026,
        subjects=["Computer Science", "Mathematics", "Physics", "English"],
        relevant_courses=["Programming Fundamentals", "Database Basics"],
        hec_attestation_done=False,
        ibcc_equivalence_done=False
    ),
    language=LanguageProficiency(
        english_proficiency_test=EnglishTestType.NONE,
        ielts_overall=None,
        toefl_score=None,
        duolingo_score=None,
        medium_of_instruction_english=True,
        moi_certificate_available=True,
        has_english_test=False
    ),
    preferences=Preferences(
        target_degree_level="Bachelor's",
        target_fields=["Computer Science", "Artificial Intelligence", "Software Engineering"],
        funding_requirement="FULL",
        budget_tier="LOW",
        max_out_of_pocket_pkr=250000,
        willing_to_relocate=True,
        preferred_regions=[],
        excluded_regions=[]
    )
)

conn = sqlite3.connect("data/scholarx_sessions.db")
c = conn.cursor()
c.execute("SELECT data_json FROM scholarships_cache")
rows = c.fetchall()

all_scholarships = [Scholarship.model_validate(json.loads(r[0])) for r in rows]

elig_inv = EligibilityInvestigator()
cost_ana = TrueCostAnalyzer()
dead_ana = DeadlineAnalyzer()
rank_eng = RankingEngine()

results = []

for sc in all_scholarships:
    deg_norm = [d.lower() for d in sc.eligibility.degree_levels]
    if not any("bachelor" in d or "undergrad" in d or "bs" in d for d in deg_norm):
        continue
    if sc.funding.funding_type != "FULL":
        continue
        
    fields = sc.eligibility.eligible_fields
    cs_match = not fields or any("all" in f.lower() for f in fields) or any(
        any(k in f.lower() for k in ["computer", "ai", "artificial", "software", "stem", "engineering", "technology", "data", "informatics"])
        for f in fields
    )
    if not cs_match:
        continue

    # Evaluate
    elig_res = elig_inv.evaluate(sc, ics_student)
    cost_res = cost_ana.analyze(sc, ics_student)
    dead_res = dead_ana.analyze(sc, ics_student, current_date=date(2026, 10, 2))
    
    evidence = EvidenceTrail(
        scholarship_id=sc.scholarship_id,
        confidence_score=sc.confidence_score,
        sources=[SourceCitation(url=sc.source_url, domain=sc.host_country_name)],
        verification_notes="ScholarX Verified Knowledge Base"
    )
    
    comp_score = rank_eng.calculate_composite_score(
        scholarship=sc,
        eligibility=elig_res,
        cost=cost_res,
        deadline=dead_res,
        evidence=evidence,
        student=ics_student
    )
    
    # We want scholarships where student does not need IELTS/TOEFL to be eligible or where MOI/Prep/Internal test is valid
    # Check if there are blocking issues specifically about English:
    lang_blocked = any("IELTS" in b or "English" in b or "TOEFL" in b for b in elig_res.blocking_issues)
    
    results.append({
        "scholarship": sc,
        "eligibility": elig_res,
        "cost": cost_res,
        "deadline": dead_res,
        "composite": comp_score,
        "lang_blocked": lang_blocked
    })

results.sort(key=lambda x: x["composite"].overall_match_score, reverse=True)

print(f"Total Evaluated Undergrad CS/AI Opportunities: {len(results)}\n")

for i, r in enumerate(results[:25], 1):
    sc = r["scholarship"]
    el = r["eligibility"]
    co = r["cost"]
    de = r["deadline"]
    cp = r["composite"]
    
    print(f"#{i} [{sc.scholarship_id}] {sc.name}")
    print(f"    Country: {sc.host_country_name} ({sc.region}) | Match Score: {cp.overall_match_score}/100 | Recommended: {cp.is_recommended}")
    print(f"    Eligibility Score: {el.eligibility_score} | Funding Score: {co.funding_score} | Upfront PKR: {co.total_out_of_pocket_pkr:,}")
    print(f"    Language: NoTestReq={not sc.language.english_test_required} | AcceptsMOI={sc.pakistan_requirements.accepts_moi_certificate} | HostPrep={sc.language.host_language_prep}")
    print(f"    Lang Notes: {sc.language.notes}")
    print(f"    Monthly Stipend: {sc.funding.monthly_stipend} (~PKR {sc.funding.monthly_stipend_pkr_approx}) | Airfare: {sc.funding.travel_airfare}")
    print(f"    Bilateral Quota: {sc.pakistan_requirements.pakistan_bilateral_quota} (Seats: {sc.pakistan_requirements.pakistan_quota_seats}) | HEC Managed: {sc.pakistan_requirements.hec_managed}")
    print(f"    Blocking Issues: {el.blocking_issues}")
    print(f"    Actions Required: {el.action_required}")
    print(f"    Pakistan Advantages: {el.pakistan_advantages}")
    print(f"    URL: {sc.source_url}")
    print("-" * 75)
