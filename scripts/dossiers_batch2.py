"""
scripts/dossiers_batch2.py
Merges Batch 2A and 2B:
Contains 8 scholarships:
1. SCH-OC-004: University of Sydney International Scholarship (USydIS, Australia)
2. SCH-OC-005: Australian National University (ANU) AGRTP International Postgraduate Award (Australia)
3. SCH-EU-008: Eiffel Excellence Scholarship Programme (Campus France, France)
4. SCH-EU-009: Swedish Institute Scholarships for Global Professionals (SISGP, Sweden)
5. SCH-EU-012: Romanian Government ARICE / MFA Scholarship Programme (Romania)
6. SCH-EU-015: Politecnico di Milano Merit-Based Scholarships (Italy)
7. SCH-EU-016: ETH Zurich Excellence Scholarship & Opportunity Programme (ESOP, Switzerland)
8. SCH-EU-022: Government of Ireland International Education Scholarship (GOI-IES, Ireland)
"""

from dossiers_batch2a import DOSSIERS_BATCH2A
from dossiers_batch2b import DOSSIERS_BATCH2B

DOSSIERS_BATCH2 = {**DOSSIERS_BATCH2A, **DOSSIERS_BATCH2B}
