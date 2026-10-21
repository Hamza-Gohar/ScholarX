# scripts/dossiers_batch17.py
"""
Batch 17: 12 Distinguished Middle East, North Africa (MENA) & Oceania Fellowships & Scholarships
- SCH-ME-015: Taibah University International Student Scholarship (Saudi Arabia)
- SCH-ME-016: King Faisal University International Student Scholarship (Saudi Arabia)
- SCH-ME-017: Jazan University International Student Scholarship (Saudi Arabia)
- SCH-ME-028: New York University Abu Dhabi (NYUAD) Global Leaders Fellowship (UAE)
- SCH-ME-029: Doha Institute for Graduate Studies (Tamim & Sanad Scholarships) (Qatar)
- SCH-ME-030: United Arab Emirates University (UAEU) PhD Full Scholarship (UAE)
- SCH-ME-031: American University of Sharjah (AUS) Chancellor's & Graduate Assistantship (UAE)
- SCH-OC-012: UNSW University International Postgraduate Award (UIPA) (Australia)
- SCH-OC-013: University of Wollongong Postgraduate Research Scholarship (UPRS) (Australia)
- SCH-OC-015: Curtin University Australian Government Research Training Program (RTP) (Australia)
- SCH-OC-016: Deakin University Postgraduate Research Scholarship (DUPRS) (Australia)
- SCH-OC-019: University of Otago International Doctoral Research Scholarships (New Zealand)
"""

from scripts.batch17_p1 import DATA_P1
from scripts.batch17_p2 import DATA_P2
from scripts.batch17_p3 import DATA_P3

DOSSIERS_BATCH17 = {}
DOSSIERS_BATCH17.update(DATA_P1)
DOSSIERS_BATCH17.update(DATA_P2)
DOSSIERS_BATCH17.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH17)} dossiers in Batch 17.")
    for sid, data in DOSSIERS_BATCH17.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 17 100% Validated!")
