"""
scripts/dossiers_batch3.py
Merges Batch 3A and 3B:
Contains 8 scholarships:
1. SCH-EU-023: Gates Cambridge Scholarship (University of Cambridge, UK)
2. SCH-EU-030: Clarendon Fund Scholarships (University of Oxford, UK)
3. SCH-AS-004: ANSO Scholarship for Young Talents (CAS/USTC/UCAS, China)
4. SCH-AS-005: Hong Kong PhD Fellowship Scheme (HKPFS, Hong Kong)
5. SCH-AS-006: Singapore International Graduate Award (SINGA, Singapore)
6. SCH-AS-007: Taiwan ICDF International Higher Education Scholarship (Taiwan)
7. SCH-AS-008: Government of Brunei Darussalam Scholarship (BDGS, Brunei)
8. SCH-AS-009: Asian Development Bank - Japan Scholarship Program (ADB-JSP)
"""

from dossiers_batch3a import DOSSIERS_BATCH3A
from dossiers_batch3b import DOSSIERS_BATCH3B

DOSSIERS_BATCH3 = {**DOSSIERS_BATCH3A, **DOSSIERS_BATCH3B}
