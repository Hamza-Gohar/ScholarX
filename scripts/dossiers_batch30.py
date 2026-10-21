"""Batch 30 Consolidated: Central European, Biomedical & Advanced Erasmus Mundus Fellowships (10 awards)
SCH-EU-084: University of Vienna Uni:Docs Fellowship Programme
SCH-EU-085: Friedrich Ebert Foundation (FES) International Scholarships
SCH-EU-086: Charles University Faculty of Mathematics and Physics Fellowship
SCH-EU-087: Boehringer Ingelheim Fonds (BIF) PhD Fellowships
SCH-EU-088: Erasmus Mundus Master in Cybersecurity (CYBERUS)
SCH-EU-089: Erasmus Mundus Master in Artificial Intelligence (EMAI)
SCH-EU-090: Erasmus Mundus Master in Cloud Computing and Services (MSc Cloud)
SCH-EU-091: Erasmus Mundus Master in Nanomedicine (NANOMED)
SCH-EU-092: Erasmus Mundus Master in Renewable Energy in the Marine Environment (REM PLUS)
SCH-EU-093: University of Sheffield International Postgraduate Taught Merit Scholarship
"""

from scripts.batch30_p1 import DATA_P1
from scripts.batch30_p2 import DATA_P2
from scripts.batch30_p3 import DATA_P3

DOSSIERS_BATCH30 = {}
DOSSIERS_BATCH30.update(DATA_P1)
DOSSIERS_BATCH30.update(DATA_P2)
DOSSIERS_BATCH30.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH30)} dossiers in Batch 30.")
    for sid, data in DOSSIERS_BATCH30.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  ✓ {sid}: {validated.basic_details.scholarship_name}")
    print(f"All {len(DOSSIERS_BATCH30)} Batch 30 dossiers validated successfully!")
