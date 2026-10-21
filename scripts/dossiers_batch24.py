# scripts/dossiers_batch24.py
# Aggregator for Batch 24 (10 Deep Scholarship Dossiers - Americas Part 2: US Elite Doctoral Fellowships)
# SCH-AM-058: Columbia University Presidential Fellowships (USA)
# SCH-AM-059: Cornell University Graduate School Fellowships (USA)
# SCH-AM-060: University of Chicago Graduate Fellowship in Physical Sciences (USA)
# SCH-AM-061: Northwestern University Graduate School Fellowship (USA)
# SCH-AM-062: Carnegie Mellon University School of Computer Science Graduate Assistantships (USA)
# SCH-AM-063: Georgia Tech Graduate Research Assistantship (GRA) (USA)
# SCH-AM-064: Purdue University Doctoral Fellowship (USA)
# SCH-AM-065: University of Washington Graduate Teaching & Research Assistantships (USA)
# SCH-AM-066: University of Texas at Austin Graduate School Fellowships (USA)
# SCH-AM-067: Rice University Doctoral Fellowships (USA)

from scripts.batch24_p1 import DATA_P1
from scripts.batch24_p2 import DATA_P2
from scripts.batch24_p3 import DATA_P3

DOSSIERS_BATCH24 = {}
DOSSIERS_BATCH24.update(DATA_P1)
DOSSIERS_BATCH24.update(DATA_P2)
DOSSIERS_BATCH24.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH24)} dossiers in Batch 24.")
    for sid, data in DOSSIERS_BATCH24.items():
        try:
            dossier = DeepScholarshipDossier(**data)
            print(f"  [OK] {sid}: {dossier.basic_details.scholarship_name}")
        except Exception as e:
            print(f"  [ERR] {sid}: {e}")
            raise
    print(f"All {len(DOSSIERS_BATCH24)} dossiers in Batch 24 validated successfully!")
