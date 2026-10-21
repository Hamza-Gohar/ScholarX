"""
scripts/dossiers_batch12.py
Merges Batch 12A and 12B:
Contains 8 Scholarships:
MENA (4):
23. SCH-ME-010: Abu Dhabi University (ADU) Academic & Chairman Scholarship (UAE)
24. SCH-ME-012: Imam Mohammad Ibn Saud Islamic University Full Scholarship (Saudi Arabia)
25. SCH-ME-013: Qassim University International Student Scholarship (Saudi Arabia)
26. SCH-ME-014: Umm Al-Qura University International Student Scholarship (Makkah, Saudi Arabia)
Oceania (4):
27. SCH-OC-010: University of Technology Sydney (UTS) International Research Scholarship (IRS) / RTP (Australia)
28. SCH-OC-011: UNSW Sydney Scientia PhD Scholarship & Australian Government RTP (Australia)
29. SCH-OC-014: University of Newcastle Research Scholarship (UNIPRS) & RTP (Australia)
30. SCH-OC-018: University of Auckland International Student Excellence Scholarship (New Zealand)
"""

from dossiers_batch12a import DOSSIERS_BATCH12A
from dossiers_batch12b import DOSSIERS_BATCH12B

DOSSIERS_BATCH12 = {**DOSSIERS_BATCH12A, **DOSSIERS_BATCH12B}
