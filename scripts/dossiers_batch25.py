"""Batch 25 Aggregator: 10 Deep Scholarship Dossiers (East Asia Part 1: China, Japan, South Korea, Malaysia)
Aggregates batch25_p1 (3 awards), batch25_p2 (3 awards), and batch25_p3 (4 awards).
"""

from scripts.batch25_p1 import DATA_P1
from scripts.batch25_p2 import DATA_P2
from scripts.batch25_p3 import DATA_P3

DOSSIERS_BATCH25 = {}
DOSSIERS_BATCH25.update(DATA_P1)
DOSSIERS_BATCH25.update(DATA_P2)
DOSSIERS_BATCH25.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Validating Batch 25 ({len(DOSSIERS_BATCH25)} awards)...")
    for s_id, data in DOSSIERS_BATCH25.items():
        DeepScholarshipDossier(**data)
        print(f"  [OK] {s_id}: {data['basic_details']['scholarship_name']}")
    print(f"Batch 25 Complete & Validated: {len(DOSSIERS_BATCH25)}/10 awards.")
