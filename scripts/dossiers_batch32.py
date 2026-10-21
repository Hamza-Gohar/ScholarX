#!/usr/bin/env python3
"""
ScholarX - Dossiers Batch 32 Compilation
Combines Part 1, Part 2, and Part 3 into DOSSIERS_BATCH32 (10 scholarships).
"""
import sys
from pathlib import Path

# Add project root and backend to python path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from backend.schemas.scholarship import DeepScholarshipDossier
from scripts.batch32_p1 import DOSSIERS_BATCH32_P1
from scripts.batch32_p2 import DOSSIERS_BATCH32_P2
from scripts.batch32_p3 import DOSSIERS_BATCH32_P3

DOSSIERS_BATCH32 = {}
DOSSIERS_BATCH32.update(DOSSIERS_BATCH32_P1)
DOSSIERS_BATCH32.update(DOSSIERS_BATCH32_P2)
DOSSIERS_BATCH32.update(DOSSIERS_BATCH32_P3)

if __name__ == "__main__":
    print(f"Validating complete Batch 32 ({len(DOSSIERS_BATCH32)} awards)...")
    assert len(DOSSIERS_BATCH32) == 10, f"Expected 10 awards, got {len(DOSSIERS_BATCH32)}"
    for s_id, d in DOSSIERS_BATCH32.items():
        validated = DeepScholarshipDossier(**d)
        print(f"  [OK] {s_id}: {validated.scholarship_id}")
    print(f"Batch 32 Complete & Validated: {len(DOSSIERS_BATCH32)}/10 awards.")
