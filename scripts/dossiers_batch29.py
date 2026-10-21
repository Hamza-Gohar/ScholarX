"""Batch 29 Consolidated: European Flagship & Research Fellowships (10 awards)
SCH-EU-066: Erasmus Mundus Master in Microelectronics & Photonics (RADMEP) (Europe)
SCH-EU-068: Swedish Institute Scholarship for Global Professionals (SISGP) (Sweden)
SCH-EU-070: TU Delft Justus & Louise van Effen Excellence Scholarship
SCH-EU-075: University College Dublin (UCD) Global Excellence Scholarship
SCH-EU-077: Imperial College London President's PhD Scholarships
SCH-EU-078: University of Bristol Think Big Postgraduate Scholarships
SCH-EU-079: University of Edinburgh Edinburgh Global Research Scholarship
SCH-EU-081: Gran Sasso Science Institute (GSSI) PhD Fellowships
SCH-EU-082: SISSA International School for Advanced Studies PhD Fellowship
SCH-EU-083: Sant'Anna School of Advanced Studies International PhD Fellowships
"""

from scripts.batch29_p1 import DATA_P1
from scripts.batch29_p2 import DATA_P2
from scripts.batch29_p3 import DATA_P3

DOSSIERS_BATCH29 = {}
DOSSIERS_BATCH29.update(DATA_P1)
DOSSIERS_BATCH29.update(DATA_P2)
DOSSIERS_BATCH29.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH29)} dossiers in Batch 29.")
    for sid, data in DOSSIERS_BATCH29.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  ✓ {sid}: {validated.basic_details.scholarship_name}")
    print(f"All {len(DOSSIERS_BATCH29)} Batch 29 dossiers validated successfully!")
