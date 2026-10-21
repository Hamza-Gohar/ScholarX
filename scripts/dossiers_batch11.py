"""
scripts/dossiers_batch11.py
Merges Batch 11A and 11B:
Contains 7 Asia Scholarships:
16. SCH-AS-015: DGIST Graduate Fellowship (South Korea)
17. SCH-AS-016: SOKENDAI Graduate University for Advanced Studies Fellowship (Japan)
18. SCH-AS-019: Tokyo Institute of Technology (Institute of Science Tokyo) IGP MEXT Fellowship (Japan)
19. SCH-AS-020: Osaka University Special Integrated Science Course (SISC) Fellowship (Japan)
20. SCH-AS-024: Tsinghua University Chinese Government Scholarship (CSC / CGS) (China)
21. SCH-AS-025: Zhejiang University (ZJU) Asian Future Leaders & CSC Scholarship (China)
22. SCH-AS-026: NTHU International Student Scholarship (National Tsing Hua University, Taiwan)
"""

from dossiers_batch11a import DOSSIERS_BATCH11A
from batch11b import DOSSIERS_BATCH11B

DOSSIERS_BATCH11 = {**DOSSIERS_BATCH11A, **DOSSIERS_BATCH11B}
