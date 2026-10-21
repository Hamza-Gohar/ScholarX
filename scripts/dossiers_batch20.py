# scripts/dossiers_batch20.py
"""
Batch 20: 10 Distinguished European & Asian Scholarships & Fellowships
- SCH-EU-049: Konrad Adenauer Foundation (KAS) International Graduate Scholarship (Germany)
- SCH-EU-051: Tampere University International Master's Scholarship & Finland Scholarship (Finland)
- SCH-EU-053: Erasmus Mundus Master in Green, Networked and Inspiring AI (GENIAL) (Europe)
- SCH-EU-054: Erasmus Mundus Joint Master in Image Processing and Computer Vision (IPCV) (Europe)
- SCH-EU-055: Cusanuswerk International Academic Scholarship (Germany)
- SCH-AS-017: Kyushu University Innovator Graduate Fellowship & MEXT Special Program (Japan)
- SCH-AS-023: Universiti Malaya (UM) Bright Sparks Research Fellowship (Malaysia)
- SCH-AS-028: Universiti Teknologi Malaysia (UTM) National Postgraduate Research Scholarship (Malaysia)
- SCH-AS-034: Shanghai Jiao Tong University (SJTU) Chinese Government Scholarship (China)
- SCH-AS-035: University of Science and Technology of China (USTC) Fellowship & CSC Scholarship (China)
"""

from scripts.batch20_p1 import DATA_P1
from scripts.batch20_p2 import DATA_P2
from scripts.batch20_p3 import DATA_P3

DOSSIERS_BATCH20 = {}
DOSSIERS_BATCH20.update(DATA_P1)
DOSSIERS_BATCH20.update(DATA_P2)
DOSSIERS_BATCH20.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH20)} dossiers in Batch 20.")
    for sid, data in DOSSIERS_BATCH20.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 20 100% Validated!")
