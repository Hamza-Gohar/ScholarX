"""Batch 26 Aggregator: 10 Deep Scholarship Dossiers (East Asia Part 2: Japan Elite Imperial/STEM & South Korea S&T Institutes)
Aggregates batch26_p1 (3 awards), batch26_p2 (3 awards), and batch26_p3 (4 awards).
"""

from scripts.batch26_p1 import DATA_P1
from scripts.batch26_p2 import DATA_P2
from scripts.batch26_p3 import DATA_P3

DOSSIERS_BATCH26 = {}
DOSSIERS_BATCH26.update(DATA_P1)
DOSSIERS_BATCH26.update(DATA_P2)
DOSSIERS_BATCH26.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Validating Batch 26 ({len(DOSSIERS_BATCH26)} awards)...")
    for s_id, data in DOSSIERS_BATCH26.items():
        DeepScholarshipDossier(**data)
        print(f"  [OK] {s_id}: {data['basic_details']['scholarship_name']}")
    print(f"Batch 26 Complete & Validated: {len(DOSSIERS_BATCH26)}/10 awards.")
