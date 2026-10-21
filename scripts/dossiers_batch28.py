"""Batch 28 Consolidated: European Flagship & Foundation Scholarships (10 awards)
SCH-EU-056: Hans Böckler Foundation International Fellowships (Germany)
SCH-EU-057: LUT University Master's Scholarship (Finland)
SCH-EU-058: University of Luxembourg Guillaume Dupaix Master's Award (Luxembourg)
SCH-EU-059: Erasmus Mundus Master in Applied Cybersecurity (CyberMACS)
SCH-EU-060: Erasmus Mundus Master in Data Intelligence & Mining (DMIN)
SCH-EU-061: Ernst Ludwig Ehrlich Studienwerk (ELES) International Scholarship (Germany)
SCH-EU-062: Avicenna Studienwerk International Fellowship (Germany)
SCH-EU-063: University of Eastern Finland (UEF) Master's Scholarship (Finland)
SCH-EU-064: Vrije Universiteit Brussel (VUB) Grand Établissement Excellence Scholarship (Belgium)
SCH-EU-065: Erasmus Mundus Master in Distributed & Big Data Engineering (DEDS) (Europe)
"""

from scripts.batch28_p1 import DATA_P1
from scripts.batch28_p2 import DATA_P2
from scripts.batch28_p3 import DATA_P3

DOSSIERS_BATCH28 = {}
DOSSIERS_BATCH28.update(DATA_P1)
DOSSIERS_BATCH28.update(DATA_P2)
DOSSIERS_BATCH28.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH28)} dossiers in Batch 28.")
    for sid, data in DOSSIERS_BATCH28.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  ✓ {sid}: {validated.basic_details.scholarship_name}")
    print(f"All {len(DOSSIERS_BATCH28)} Batch 28 dossiers validated successfully!")
