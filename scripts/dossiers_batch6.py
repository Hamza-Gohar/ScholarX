"""
scripts/dossiers_batch6.py
Merges Batch 6A and 6B:
Contains 8 scholarships:
9. SCH-AM-005: University of Waterloo International Doctoral Award (IDSA) (Canada)
10. SCH-AM-006: Rotary Peace Fellowship (USA / The Rotary Foundation & Duke/UNC)
11. SCH-AM-007: University of Calgary International Entrance Scholarship (Canada)
12. SCH-AM-011: Banting Postdoctoral Fellowships (Canada / CIHR, NSERC, SSHRC)
13. SCH-AM-012: Carnegie Mellon University (CMU) SCS Graduate Assistantship (USA)
14. SCH-AM-017: UBC Four Year Doctoral Fellowship (4YF) (Canada)
15. SCH-AM-019: Georgia Tech Graduate Assistantship & Fellowships (USA)
16. SCH-AS-010: Kyoto University iUP (International Undergraduate Program, Japan)
"""

from dossiers_batch6a import DOSSIERS_BATCH6A
from dossiers_batch6b import DOSSIERS_BATCH6B

DOSSIERS_BATCH6 = {**DOSSIERS_BATCH6A, **DOSSIERS_BATCH6B}
