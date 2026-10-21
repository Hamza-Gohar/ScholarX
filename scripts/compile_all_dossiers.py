#!/usr/bin/env python3
"""
scripts/compile_all_dossiers.py
Validates, bundles, and integrates the 20 comprehensive 11-dimension scholarship dossiers.
- Validates all 20 dossiers against Pydantic schema DeepScholarshipDossier
- Saves individual JSON dossiers in data/deep_dossiers/ and frontend/lib/data/deep_dossiers/
- Saves unified bundle in data/scholarships_deep_dossiers.json and frontend/lib/data/
- Injects deep_dossier into data/scholarships/*.json and frontend/lib/data/scholarships/*.json
- Re-seeds SQLite database via backend.db.seed
"""

import json
import os
import shutil
import sys
from pathlib import Path

# Add backend directory to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "backend"))

from schemas.scholarship import DeepScholarshipDossier
from scripts.dossiers_part1 import DOSSIERS_PART1
from scripts.dossiers_part2 import DOSSIERS_PART2
from scripts.dossiers_part3 import DOSSIERS_PART3
from scripts.dossiers_batch1 import DOSSIERS_BATCH1
from scripts.dossiers_batch1b import DOSSIERS_BATCH1B
from scripts.dossiers_batch2 import DOSSIERS_BATCH2
from scripts.dossiers_batch3 import DOSSIERS_BATCH3
from scripts.dossiers_batch4 import DOSSIERS_BATCH4
from scripts.dossiers_batch5 import DOSSIERS_BATCH5
from scripts.dossiers_batch6 import DOSSIERS_BATCH6
from scripts.dossiers_batch7 import DOSSIERS_BATCH7
from scripts.dossiers_batch8 import DOSSIERS_BATCH8
from scripts.dossiers_batch9 import DOSSIERS_BATCH9
from scripts.dossiers_batch10 import DOSSIERS_BATCH10
from scripts.dossiers_batch11 import DOSSIERS_BATCH11
from scripts.dossiers_batch12 import DOSSIERS_BATCH12
from scripts.dossiers_batch13 import DOSSIERS_BATCH13
from scripts.dossiers_batch14 import DOSSIERS_BATCH14
from scripts.dossiers_batch15 import DOSSIERS_BATCH15
from scripts.dossiers_batch16 import DOSSIERS_BATCH16
from scripts.dossiers_batch17 import DOSSIERS_BATCH17
from scripts.dossiers_batch18 import DOSSIERS_BATCH18
from scripts.dossiers_batch19 import DOSSIERS_BATCH19
from scripts.dossiers_batch20 import DOSSIERS_BATCH20
from scripts.dossiers_batch21 import DOSSIERS_BATCH21
from scripts.dossiers_batch22 import DOSSIERS_BATCH22
from scripts.dossiers_batch23 import DOSSIERS_BATCH23
from scripts.dossiers_batch24 import DOSSIERS_BATCH24
from scripts.dossiers_batch25 import DOSSIERS_BATCH25
from scripts.dossiers_batch26 import DOSSIERS_BATCH26
from scripts.dossiers_batch27 import DOSSIERS_BATCH27
from scripts.dossiers_batch28 import DOSSIERS_BATCH28
from scripts.dossiers_batch29 import DOSSIERS_BATCH29
from scripts.dossiers_batch30 import DOSSIERS_BATCH30
from scripts.dossiers_batch31 import DOSSIERS_BATCH31
from scripts.dossiers_batch32 import DOSSIERS_BATCH32

ALL_DOSSIERS = {}
ALL_DOSSIERS.update(DOSSIERS_PART1)
ALL_DOSSIERS.update(DOSSIERS_PART2)
ALL_DOSSIERS.update(DOSSIERS_PART3)
ALL_DOSSIERS.update(DOSSIERS_BATCH1)
ALL_DOSSIERS.update(DOSSIERS_BATCH1b if 'DOSSIERS_BATCH1b' in locals() else DOSSIERS_BATCH1B)
ALL_DOSSIERS.update(DOSSIERS_BATCH2)
ALL_DOSSIERS.update(DOSSIERS_BATCH3)
ALL_DOSSIERS.update(DOSSIERS_BATCH4)
ALL_DOSSIERS.update(DOSSIERS_BATCH5)
ALL_DOSSIERS.update(DOSSIERS_BATCH6)
ALL_DOSSIERS.update(DOSSIERS_BATCH7)
ALL_DOSSIERS.update(DOSSIERS_BATCH8)
ALL_DOSSIERS.update(DOSSIERS_BATCH9)
ALL_DOSSIERS.update(DOSSIERS_BATCH10)
ALL_DOSSIERS.update(DOSSIERS_BATCH11)
ALL_DOSSIERS.update(DOSSIERS_BATCH12)
ALL_DOSSIERS.update(DOSSIERS_BATCH13)
ALL_DOSSIERS.update(DOSSIERS_BATCH14)
ALL_DOSSIERS.update(DOSSIERS_BATCH15)
ALL_DOSSIERS.update(DOSSIERS_BATCH16)
ALL_DOSSIERS.update(DOSSIERS_BATCH17)
ALL_DOSSIERS.update(DOSSIERS_BATCH18)
ALL_DOSSIERS.update(DOSSIERS_BATCH19)
ALL_DOSSIERS.update(DOSSIERS_BATCH20)
ALL_DOSSIERS.update(DOSSIERS_BATCH21)
ALL_DOSSIERS.update(DOSSIERS_BATCH22)
ALL_DOSSIERS.update(DOSSIERS_BATCH23)
ALL_DOSSIERS.update(DOSSIERS_BATCH24)
ALL_DOSSIERS.update(DOSSIERS_BATCH25)
ALL_DOSSIERS.update(DOSSIERS_BATCH26)
ALL_DOSSIERS.update(DOSSIERS_BATCH27)
ALL_DOSSIERS.update(DOSSIERS_BATCH28)
ALL_DOSSIERS.update(DOSSIERS_BATCH29)
ALL_DOSSIERS.update(DOSSIERS_BATCH30)
ALL_DOSSIERS.update(DOSSIERS_BATCH31)
ALL_DOSSIERS.update(DOSSIERS_BATCH32)

print(f"Total dossiers loaded for validation: {len(ALL_DOSSIERS)}")

# 1. Validate against Pydantic schema
validated_count = 0
for s_id, raw_data in ALL_DOSSIERS.items():
    try:
        validated = DeepScholarshipDossier.model_validate(raw_data)
        validated_count += 1
    except Exception as e:
        print(f"❌ Validation failed for {s_id}: {e}")
        sys.exit(1)

print(f"✅ All {validated_count}/{len(ALL_DOSSIERS)} dossiers successfully validated against Pydantic schema!")

# 2. Setup directories
BACKEND_DEEP_DIR = PROJECT_ROOT / "data" / "deep_dossiers"
FRONTEND_DEEP_DIR = PROJECT_ROOT / "frontend" / "lib" / "data" / "deep_dossiers"
BACKEND_DEEP_DIR.mkdir(parents=True, exist_ok=True)
FRONTEND_DEEP_DIR.mkdir(parents=True, exist_ok=True)

# 3. Write individual JSON files
for s_id, raw_data in ALL_DOSSIERS.items():
    backend_file = BACKEND_DEEP_DIR / f"{s_id}.json"
    frontend_file = FRONTEND_DEEP_DIR / f"{s_id}.json"
    with open(backend_file, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2, ensure_ascii=False)
    with open(frontend_file, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2, ensure_ascii=False)

print(f"✅ Wrote {len(ALL_DOSSIERS)} individual JSON dossiers to data/deep_dossiers/ and frontend.")

# 4. Write master unified bundle
master_bundle_backend = PROJECT_ROOT / "data" / "scholarships_deep_dossiers.json"
master_bundle_frontend = PROJECT_ROOT / "frontend" / "lib" / "data" / "scholarships_deep_dossiers.json"
with open(master_bundle_backend, "w", encoding="utf-8") as f:
    json.dump(ALL_DOSSIERS, f, indent=2, ensure_ascii=False)
with open(master_bundle_frontend, "w", encoding="utf-8") as f:
    json.dump(ALL_DOSSIERS, f, indent=2, ensure_ascii=False)

print("✅ Saved master dossier bundles in backend and frontend data directories.")

# 5. Enrich regional scholarship JSON files
REGIONS = ["americas", "asia", "europe", "mena", "oceania"]
enriched_count = 0

for region in REGIONS:
    file_path = PROJECT_ROOT / "data" / "scholarships" / f"{region}.json"
    if not file_path.exists():
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        scholarships = json.load(f)
    
    modified = False
    for sc in scholarships:
        sid = sc.get("scholarship_id")
        if sid in ALL_DOSSIERS:
            sc["deep_dossier"] = ALL_DOSSIERS[sid]
            enriched_count += 1
            modified = True
    
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(scholarships, f, indent=2, ensure_ascii=False)
        # Mirror to frontend
        frontend_reg_file = PROJECT_ROOT / "frontend" / "lib" / "data" / "scholarships" / f"{region}.json"
        frontend_reg_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, frontend_reg_file)

print(f"✅ Enriched regional scholarship files with {enriched_count} deep dossiers and mirrored to frontend.")

# 6. Re-seed SQLite database
import asyncio
from db.seed import load_and_seed_scholarships

total = asyncio.run(load_and_seed_scholarships())
print(f"✅ Database re-seeded successfully with {total} scholarships (including updated deep dossiers)!")

