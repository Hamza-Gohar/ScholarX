# scripts/dossiers_batch21.py
"""
Batch 21: 10 Distinguished Asian Scholarships & Fellowships
- SCH-AS-036: Hokkaido University President's Fellowship & MEXT Special Program (Japan)
- SCH-AS-037: Chung-Ang University (CAU) Graduate Global Scholarship (South Korea)
- SCH-AS-038: Universiti Putra Malaysia (UPM) Graduate Research Fellowship (Malaysia)
- SCH-AS-039: Harbin Institute of Technology (HIT) Chinese Government Scholarship (China)
- SCH-AS-040: Xi'an Jiaotong University (XJTU) Silk Road CSC Scholarship (China)
- SCH-AS-043: Universiti Kebangsaan Malaysia (UKM) Graduate Research Fellowship (Malaysia)
- SCH-AS-045: Wuhan University (WHU) Chinese Government & Belt and Road Award (China)
- SCH-AS-046: Kobe University System Informatics MEXT Award (Japan)
- SCH-AS-047: Ajou University International Graduate Scholarship (South Korea)
- SCH-AS-048: Universiti Tenaga Nasional (UNITEN) Postgraduate Excellence Award (Malaysia)
"""

from scripts.batch21_p1 import DATA_P1
from scripts.batch21_p2 import DATA_P2
from scripts.batch21_p3 import DATA_P3

DOSSIERS_BATCH21 = {}
DOSSIERS_BATCH21.update(DATA_P1)
DOSSIERS_BATCH21.update(DATA_P2)
DOSSIERS_BATCH21.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH21)} dossiers in Batch 21.")
    for sid, data in DOSSIERS_BATCH21.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 21 100% Validated!")
