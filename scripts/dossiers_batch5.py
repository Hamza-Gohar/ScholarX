"""
scripts/dossiers_batch5.py
Merges Batch 5A and 5B:
Contains 8 Europe scholarships:
1. SCH-EU-010: Stefan Banach Scholarship Programme (Poland NAWA & MFA)
2. SCH-EU-011: Finland Scholarship Programme (Finland EDUFI & Universities)
3. SCH-EU-014: Heinrich Böll Foundation Scholarships (Germany)
4. SCH-EU-017: University of Padua International Excellence Scholarship (Italy)
5. SCH-EU-018: University of Twente Scholarship (UTS) (Netherlands)
6. SCH-EU-020: Ghent University Master Grants & BOF Doctoral Scholarships (Belgium)
7. SCH-EU-021: KU Leuven Science@Leuven Scholarship (Belgium)
8. SCH-EU-031: EPFL Master Excellence Fellowships (Switzerland)
"""

from dossiers_batch5a import DOSSIERS_BATCH5A
from dossiers_batch5b import DOSSIERS_BATCH5B

DOSSIERS_BATCH5 = {**DOSSIERS_BATCH5A, **DOSSIERS_BATCH5B}
