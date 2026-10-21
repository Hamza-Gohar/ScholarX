# scripts/dossiers_batch13.py
"""
Batch 13: 10 Highly Competitive North American Graduate Awards (Americas)
- SCH-AM-018: University of Alberta Computing Science Graduate Award & Amii AI Fellowship (Canada)
- SCH-AM-022: Simon Fraser University (SFU) Computing Science Graduate Award (Canada)
- SCH-AM-025: University of Ottawa International Doctoral Differential Scholarship (Canada)
- SCH-AM-026: Queen's University Graduate Award & International Doctoral Fellowship (Canada)
- SCH-AM-027: UC San Diego (UCSD) CSE Graduate Fellowship & Assistantship (USA)
- SCH-AM-028: Columbia University Computer Science Doctoral Fellowship (USA)
- SCH-AM-031: University of Maryland College Park (UMD) CS Graduate Assistantship (USA)
- SCH-AM-032: Johns Hopkins University (JHU) Computer Science PhD Fellowship (USA)
- SCH-AM-035: UMass Amherst Manning CICS Graduate Assistantship (USA)
- SCH-AM-036: Northwestern University Walter P. Murphy Fellowship & CS PhD (USA)
"""

from scripts.batch13_p1 import DATA_P1
from scripts.batch13_p2 import DATA_P2
from scripts.batch13_p3 import DATA_P3

DOSSIERS_BATCH13 = {}
DOSSIERS_BATCH13.update(DATA_P1)
DOSSIERS_BATCH13.update(DATA_P2)
DOSSIERS_BATCH13.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH13)} dossiers in Batch 13.")
    for sid, data in DOSSIERS_BATCH13.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 13 100% Validated!")
