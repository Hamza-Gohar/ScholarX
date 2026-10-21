# scripts/dossiers_batch15.py
"""
Batch 15: 10 Distinguished Global Fellowships & Scholarships (Europe & Asia)
- SCH-EU-071: Leiden University Excellence Scholarship (LExS) (Netherlands)
- SCH-EU-072: Utrecht Excellence Scholarships (UES) (Netherlands)
- SCH-EU-073: University of Amsterdam Amsterdam Excellence Scholarship (AES) (Netherlands)
- SCH-EU-074: Trinity College Dublin Global Excellence Postgraduate Scholarship (Ireland)
- SCH-EU-076: University of Warwick Chancellor's International Scholarship (UK)
- SCH-EU-080: Scuola Normale Superiore PhD Scholarship (Italy)
- SCH-AS-027: NYCU International Graduate Scholarship (Taiwan)
- SCH-AS-029: Peking University (PKU) Chinese Government Scholarship (China)
- SCH-AS-030: Fudan University Chinese Government Scholarship (China)
- SCH-AS-031: Nagoya University NUPACE & IGP MEXT Fellowship (Japan)
"""

from scripts.batch15_p1 import DATA_P1
from scripts.batch15_p2 import DATA_P2
from scripts.batch15_p3 import DATA_P3

DOSSIERS_BATCH15 = {}
DOSSIERS_BATCH15.update(DATA_P1)
DOSSIERS_BATCH15.update(DATA_P2)
DOSSIERS_BATCH15.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH15)} dossiers in Batch 15.")
    for sid, data in DOSSIERS_BATCH15.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 15 100% Validated!")
