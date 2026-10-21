# scripts/dossiers_batch22.py
# Aggregator for Batch 22 (10 Deep Scholarship Dossiers - MENA & Oceania)
# SCH-ME-018: King Khalid University International Student Scholarship (Saudi Arabia)
# SCH-ME-019: Najran University International Student Scholarship (Saudi Arabia)
# SCH-ME-020: Majmaah University International Student Scholarship (Saudi Arabia)
# SCH-ME-021: University of Ha'il International Student Scholarship (Saudi Arabia)
# SCH-ME-022: University of Tabuk International Student Scholarship (Saudi Arabia)
# SCH-ME-032: Zayed University Graduate Merit Scholarships (UAE)
# SCH-ME-033: Hamad Bin Khalifa University Graduate Research Grants (Qatar)
# SCH-ME-035: Sultan Qaboos University Postgraduate Scholarships (Oman)
# SCH-OC-017: Griffith University International Postgraduate Research Scholarship (Australia)
# SCH-OC-020: Victoria University of Wellington Doctoral Scholarship (New Zealand)

from scripts.batch22_p1 import DATA_P1
from scripts.batch22_p2 import DATA_P2
from scripts.batch22_p3 import DATA_P3

DOSSIERS_BATCH22 = {}
DOSSIERS_BATCH22.update(DATA_P1)
DOSSIERS_BATCH22.update(DATA_P2)
DOSSIERS_BATCH22.update(DATA_P3)

if __name__ == "__main__":
    from backend.schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH22)} dossiers in Batch 22.")
    for sid, data in DOSSIERS_BATCH22.items():
        try:
            dossier = DeepScholarshipDossier(**data)
            print(f"  [OK] {sid}: {dossier.basic_details.scholarship_name}")
        except Exception as e:
            print(f"  [ERR] {sid}: {e}")
            raise
    print(f"All {len(DOSSIERS_BATCH22)} dossiers in Batch 22 validated successfully!")
