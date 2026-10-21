#!/usr/bin/env python3
"""
ScholarX - Dossiers Batch 31 Compilation
Combines Part 1, Part 2, and Part 3 into DOSSIERS_BATCH31 (10 scholarships).
"""
import sys
from pathlib import Path

# Add project root and backend to python path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from backend.schemas.scholarship import DeepScholarshipDossier
from scripts.batch31_p1 import DATA_P1 as DOSSIERS_BATCH31_P1
from scripts.batch31_p2 import DOSSIERS_BATCH31_P2
from scripts.batch31_p3 import DOSSIERS_BATCH31_P3

DOSSIERS_BATCH31 = {}
DOSSIERS_BATCH31.update(DOSSIERS_BATCH31_P1)
DOSSIERS_BATCH31.update(DOSSIERS_BATCH31_P2)
DOSSIERS_BATCH31.update(DOSSIERS_BATCH31_P3)

if __name__ == "__main__":
    print(f"Validating complete Batch 31 ({len(DOSSIERS_BATCH31)} awards)...")
    assert len(DOSSIERS_BATCH31) == 10, f"Expected 10 awards, got {len(DOSSIERS_BATCH31)}"
    for s_id, d in DOSSIERS_BATCH31.items():
        validated = DeepScholarshipDossier(**d)
        print(f"  [OK] {s_id}: {validated.scholarship_id}")
    print(f"Batch 31 Complete & Validated: {len(DOSSIERS_BATCH31)}/10 awards.")
