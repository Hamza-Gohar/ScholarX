"""
scripts/dossiers_batch7.py
Merges Batch 7A and 7B:
Contains 8 scholarships:
17. SCH-AS-011: UST Graduate Fellowship (South Korea / UST & 32 National Research Institutes)
18. SCH-AS-013: POSCO TJ Park Asia Fellowship (South Korea / POSCO TJ Park Foundation)
19. SCH-AS-014: GIST Graduate Scholarship (South Korea / Gwangju Institute of Science & Technology)
20. SCH-AS-018: SIIT Excellent Foreign Students (EFS) Scholarship (Thailand / Thammasat University)
21. SCH-AS-021: National University of Singapore (NUS) Research Scholarship (Singapore)
22. SCH-AS-022: Nanyang Technological University (NTU) Research Scholarship (Singapore)
23. SCH-ME-003: KFUPM Graduate STEM Fellowship (Saudi Arabia)
24. SCH-ME-007: Khalifa University Graduate Scholarship (UAE)
"""

from dossiers_batch7a import DOSSIERS_BATCH7A
from dossiers_batch7b import DOSSIERS_BATCH7B

DOSSIERS_BATCH7 = {**DOSSIERS_BATCH7A, **DOSSIERS_BATCH7B}
