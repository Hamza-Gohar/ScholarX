from typing import List
from workflows.scouts.base_scout import BaseScout


class OceaniaScout(BaseScout):
    region_name: str = "Oceania"
    default_domains: List[str] = [
        "dfat.gov.au",
        "nzscholarships.govt.nz",
        "unimelb.edu.au",
        "anu.edu.au",
    ]
    default_queries: List[str] = [
        "Australia Awards scholarships Pakistan category eligibility DFAT 2027",
        "Manaaki New Zealand scholarships developing country Pakistan",
        "University of Melbourne graduate research scholarship international",
    ]
