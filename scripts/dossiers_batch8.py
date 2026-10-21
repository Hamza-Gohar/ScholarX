"""
scripts/dossiers_batch8.py
Merges Batch 8A and 8B:
Contains 6 scholarships (2 MENA + 4 Oceania):
25. SCH-ME-009: Qatar University International Student Scholarships (Qatar)
26. SCH-ME-011: Princess Nourah bint Abdulrahman University (PNU) International Scholarship (Saudi Arabia)
27. SCH-OC-006: University of Queensland Graduate School Scholarship (UQGSS) (Australia)
28. SCH-OC-007: Monash University Graduate Research Scholarship (MGRS) / Research Training Program (RTP) (Australia)
29. SCH-OC-008: University of Western Australia (UWA) Forrest Research Foundation PhD Scholarship & RTP (Australia)
30. SCH-OC-009: University of Adelaide Research Scholarship (ADRS) / AGRTP (Australia)
"""

from dossiers_batch8a import DOSSIERS_BATCH8A
from dossiers_batch8b import DOSSIERS_BATCH8B

DOSSIERS_BATCH8 = {**DOSSIERS_BATCH8A, **DOSSIERS_BATCH8B}
