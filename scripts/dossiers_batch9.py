"""
scripts/dossiers_batch9.py
Merges Batch 9A and 9B:
Contains 8 European Scholarships:
1. SCH-EU-019: Radboud Scholarship Programme (Netherlands)
2. SCH-EU-024: University of Geneva Excellence Master Fellowships (Switzerland)
3. SCH-EU-025: Vrije Universiteit Amsterdam Fellowship Programme (VUFP) (Netherlands)
4. SCH-EU-026: TU Wien & Vienna Applied Data Science Excellence Grants (Austria)
5. SCH-EU-028: Estonian Government Master & Doctoral Scholarship (Harno, Estonia)
6. SCH-EU-032: Bocconi Graduate Merit & International Awards (Italy)
7. SCH-EU-036: Uppsala University Global Scholarship (Sweden)
8. SCH-EU-037: Lund University Global Scholarship (LUGS) (Sweden)
"""

from dossiers_batch9a import DOSSIERS_BATCH9A
from dossiers_batch9b import DOSSIERS_BATCH9B

DOSSIERS_BATCH9 = {**DOSSIERS_BATCH9A, **DOSSIERS_BATCH9B}
