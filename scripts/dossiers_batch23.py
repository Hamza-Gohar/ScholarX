# scripts/dossiers_batch23.py
# Aggregator for Batch 23 (10 Deep Scholarship Dossiers - Americas Part 1: Canadian & Top US Fellowships)
# SCH-AM-048: University of Alberta Graduate Entrance Scholarship & Centenary Award (Canada)
# SCH-AM-049: Simon Fraser University (SFU) Graduate Research Fellowship (Canada)
# SCH-AM-050: Western University International President's Entrance Scholarship (Canada)
# SCH-AM-051: Dalhousie University International Research Award (Canada)
# SCH-AM-052: Hubert H. Humphrey Fellowship Program for Pakistan (USA)
# SCH-AM-053: Rotary Peace Fellowship (Duke University & UNC Chapel Hill) (USA)
# SCH-AM-054: Harvard University Center for the Environment Graduate Fellowships (USA)
# SCH-AM-055: MIT Presidential Graduate Fellowship (USA)
# SCH-AM-056: Princeton University Doctoral Fellowship (USA)
# SCH-AM-057: Yale University Graduate School Doctoral Fellowship (USA)

from scripts.batch23_p1 import DATA_P1
from scripts.batch23_p2 import DATA_P2
from scripts.batch23_p3 import DATA_P3

DOSSIERS_BATCH23 = {}
DOSSIERS_BATCH23.update(DATA_P1)
DOSSIERS_BATCH23.update(DATA_P2)
DOSSIERS_BATCH23.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH23)} dossiers in Batch 23.")
    for sid, data in DOSSIERS_BATCH23.items():
        try:
            dossier = DeepScholarshipDossier(**data)
            print(f"  [OK] {sid}: {dossier.basic_details.scholarship_name}")
        except Exception as e:
            print(f"  [ERR] {sid}: {e}")
            raise
    print(f"All {len(DOSSIERS_BATCH23)} dossiers in Batch 23 validated successfully!")
