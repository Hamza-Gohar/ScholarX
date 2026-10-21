# scripts/dossiers_batch19.py
"""
Batch 19: 10 Distinguished European Scholarships & Fellowships
- SCH-EU-013: SBW Berlin International Scholarship for Social Development (Germany)
- SCH-EU-027: Norwegian Directorate (HK-dir) / NORPART Postgraduate Research Grants (Norway)
- SCH-EU-033: Technical University of Darmstadt Graduate Research Fellowships & Assistantships (Germany)
- SCH-EU-034: University of Oulu International Master's Scholarship & Finland Scholarship (Finland)
- SCH-EU-035: Warsaw University of Technology & NAWA Stefan Banach Scholarship Programme (Poland)
- SCH-EU-040: Friedrich Naumann Foundation for Freedom (FNF) International Scholarship (Germany)
- SCH-EU-044: University of Bologna International Talents @Unibo Scholarships & Tuition Fee Waivers (Italy)
- SCH-EU-045: University of Turku International Master's Scholarship & Finland Scholarship (Finland)
- SCH-EU-046: Rosa Luxemburg Foundation (RLS) International Graduate Scholarship (Germany)
- SCH-EU-048: Erasmus Mundus Joint Master in Big Data Management and Analytics (BDMA) (EU)
"""

from scripts.batch19_p1 import DATA_P1
from scripts.batch19_p2 import DATA_P2
from scripts.batch19_p3 import DATA_P3

DOSSIERS_BATCH19 = {}
DOSSIERS_BATCH19.update(DATA_P1)
DOSSIERS_BATCH19.update(DATA_P2)
DOSSIERS_BATCH19.update(DATA_P3)

if __name__ == "__main__":
    from schemas.scholarship import DeepScholarshipDossier
    print(f"Loaded {len(DOSSIERS_BATCH19)} dossiers in Batch 19.")
    for sid, data in DOSSIERS_BATCH19.items():
        validated = DeepScholarshipDossier(**data)
        print(f"  [OK] {sid}: {validated.basic_details.scholarship_name}")
    print("Batch 19 100% Validated!")
