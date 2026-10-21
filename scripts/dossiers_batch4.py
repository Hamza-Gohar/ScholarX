"""
scripts/dossiers_batch4.py
Merges Batch 4A and 4B:
Contains 6 scholarships:
1. SCH-AS-012: KAIST International Student Scholarship (South Korea)
2. SCH-ME-002: KAUST Fellowship (King Abdullah University of Science and Technology, Saudi Arabia)
3. SCH-ME-004: Hamad Bin Khalifa University (HBKU) Scholarship (Qatar)
4. SCH-ME-005: King Abdulaziz University (KAU) International Scholarship (Saudi Arabia)
5. SCH-ME-006: Islamic Development Bank (IsDB) Scholarship Programme (International / Saudi Arabia)
6. SCH-ME-008: Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) Scholarship (UAE)
"""

from dossiers_batch4a import DOSSIERS_BATCH4A
from dossiers_batch4b import DOSSIERS_BATCH4B

DOSSIERS_BATCH4 = {**DOSSIERS_BATCH4A, **DOSSIERS_BATCH4B}
