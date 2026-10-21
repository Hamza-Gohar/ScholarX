# scripts/dossiers_batch16.py
"""
Batch 16: 8 Premier Pan-Asian Fellowships & Scholarships
- SCH-AS-032: Tohoku University FGL Graduate Research Fellowship (Japan)
- SCH-AS-033: Universiti Sains Malaysia (USM) Graduate Research Assistant Scheme (Malaysia)
- SCH-AS-041: Kyushu University ISEE International Graduate Program (Japan)
- SCH-AS-042: Hanyang University International Graduate Scholarship (HISP) (South Korea)
- SCH-AS-044: Nanjing University Chinese Government Scholarship (CSC Type B) (China)
- SCH-AS-049: Beihang University Chinese Government & Postgrad Presidential Scholarship (China)
- SCH-AS-066: Seoul National University (SNU) Global Scholarship (South Korea)
- SCH-AS-072: Nanyang Technological University (NTU) Nanyang President's Graduate Scholarship (Singapore)
"""

from scripts.batch16_p1 import DATA_P1
from scripts.batch16_p2 import DATA_P2

DOSSIERS_BATCH16 = {}
DOSSIERS_BATCH16.update(DATA_P1)
DOSSIERS_BATCH16.update(DATA_P2)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH16)} dossiers in Batch 16.")
    for sid, data in DOSSIERS_BATCH16.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 16 100% Validated!")
