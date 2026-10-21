"""Batch 27 Aggregator: 10 Deep Scholarship Dossiers (Singapore, Hong Kong, Malaysia, Thailand Elite Awards)
Aggregates batch27_p1 (3 awards), batch27_p2 (3 awards), and batch27_p3 (4 awards).
"""

from scripts.batch27_p1 import DATA_P1
from scripts.batch27_p2 import DATA_P2
from scripts.batch27_p3 import DATA_P3

DOSSIERS_BATCH27 = {}
DOSSIERS_BATCH27.update(DATA_P1)
DOSSIERS_BATCH27.update(DATA_P2)
DOSSIERS_BATCH27.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Validating Batch 27 ({len(DOSSIERS_BATCH27)} awards)...")
    for s_id, data in DOSSIERS_BATCH27.items():
        DeepScholarshipDossier(**data)
        print(f"  [OK] {s_id}: {data['basic_details']['scholarship_name']}")
    print(f"Batch 27 Complete & Validated: {len(DOSSIERS_BATCH27)}/10 awards.")
