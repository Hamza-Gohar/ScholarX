# scripts/dossiers_batch18.py
"""
Batch 18: 10 Prestigious Americas (Canada) Scholarships & Fellowships
- SCH-AM-029: University of Calgary Graduate Research Scholarship & Teaching Assistantship in Computer Science (Canada)
- SCH-AM-030: Western University Graduate Research Scholarship & TA in Computer Science (Canada)
- SCH-AM-033: McMaster University International Excellence Graduate Award & Teaching Assistantship in Computing (Canada)
- SCH-AM-034: University of Victoria (UVic) Graduate Fellowship & Teaching Assistantship in Computer Science (Canada)
- SCH-AM-037: Concordia University Graduate Fellowship & International Tuition Award in Computer Science (Canada)
- SCH-AM-038: Dalhousie University Faculty of Computer Science Graduate Research Scholarship (FGS & CS) (Canada)
- SCH-AM-041: Carleton University Graduate Scholarship & Assistantship in Computer Science (Canada)
- SCH-AM-042: York University Lassonde Graduate Fellowship in CS & Engineering (Canada)
- SCH-AM-045: University of British Columbia (UBC) Karen McKellin International Leader Award (Canada)
- SCH-AM-047: University of Waterloo International Master's & Doctoral Award (IMAE/IDSA) (Canada)
"""

from scripts.batch18_p1 import DATA_P1
from scripts.batch18_p2 import DATA_P2
from scripts.batch18_p3 import DATA_P3

DOSSIERS_BATCH18 = {}
DOSSIERS_BATCH18.update(DATA_P1)
DOSSIERS_BATCH18.update(DATA_P2)
DOSSIERS_BATCH18.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH18)} dossiers in Batch 18.")
    for sid, data in DOSSIERS_BATCH18.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 18 100% Validated!")
