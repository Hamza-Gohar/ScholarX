# scripts/dossiers_batch14.py
"""
Batch 14: 10 Elite Graduate Fellowships & Scholarships (Americas & Europe)
- SCH-AM-039: Rice University Computer Science Graduate Fellowship & Assistantship (USA)
- SCH-AM-040: University of Southern California (USC) Viterbi PhD Fellowship in CS (USA)
- SCH-EU-038: University of Helsinki Finland Scholarship Programme & Master's Grants (Finland)
- SCH-EU-039: Aalto University Full Merit Scholarship & Finland Scholarship (Finland)
- SCH-EU-041: CERN Doctoral Student Programme in Computing, Physics & Engineering (Switzerland)
- SCH-EU-042: KTH Royal Institute of Technology Master's Scholarship (Sweden)
- SCH-EU-043: Chalmers University of Technology IPOET Scholarship (Sweden)
- SCH-EU-047: Erasmus Mundus Master in Security and Cloud Computing (SECCLO) (Europe)
- SCH-EU-052: École Polytechnique Paris Master's Excellence Scholarship (IP Paris) (France)
- SCH-EU-067: Technical University of Denmark (DTU) PhD Fellowship in AI & Computing (Denmark)
"""

from scripts.batch14_p1 import DATA_P1
from scripts.batch14_p2 import DATA_P2
from scripts.batch14_p3 import DATA_P3

DOSSIERS_BATCH14 = {}
DOSSIERS_BATCH14.update(DATA_P1)
DOSSIERS_BATCH14.update(DATA_P2)
DOSSIERS_BATCH14.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH14)} dossiers in Batch 14.")
    for sid, data in DOSSIERS_BATCH14.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 14 100% Validated!")
