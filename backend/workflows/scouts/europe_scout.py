from typing import List
from workflows.scouts.base_scout import BaseScout


class EuropeScout(BaseScout):
    region_name: str = "Europe"
    default_domains: List[str] = [
        "stipendiumhungaricum.hu",
        "daad.de",
        "campusfrance.org",
        "eacea.ec.europa.eu",
        "hec.gov.pk",
        "polimi.it",
    ]
    default_queries: List[str] = [
        "Stipendium Hungaricum scholarship Pakistan HEC application requirements 2027",
        "DAAD scholarship Pakistani students full funding Germany 2027",
        "Italian DSU regional scholarship tuition fee waiver Pakistani students 2026 2027",
        "Erasmus Mundus scholarship catalogue Pakistan eligibility",
    ]
