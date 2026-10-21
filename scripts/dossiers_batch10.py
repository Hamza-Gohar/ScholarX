"""
scripts/dossiers_batch10.py
Merges Batch 10A and 10B:
Contains 7 Americas Scholarships:
9. SCH-AM-013: Purdue University CS Graduate Assistantship (USA)
10. SCH-AM-015: Cornell University CS Graduate Assistantship (USA - Ivy League)
11. SCH-AM-016: University of Michigan Ann Arbor CSE Graduate Fellowship (USA)
12. SCH-AM-020: University of Texas at Austin (UT Austin) CS Graduate Fellowship (USA)
13. SCH-AM-021: University of Waterloo Cheriton School of CS Doctoral Fellowship (Canada)
14. SCH-AM-023: University of Illinois Urbana-Champaign (UIUC) CS Graduate Assistantship (USA)
15. SCH-AM-024: University of Washington (UW) Paul G. Allen CS Assistantship (USA)
"""

from dossiers_batch10a import DOSSIERS_BATCH10A
from batch10b import DOSSIERS_BATCH10B

DOSSIERS_BATCH10 = {**DOSSIERS_BATCH10A, **DOSSIERS_BATCH10B}
