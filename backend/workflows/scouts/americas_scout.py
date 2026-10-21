from typing import List
from workflows.scouts.base_scout import BaseScout


class AmericasScout(BaseScout):
    region_name: str = "Americas"
    default_domains: List[str] = [
        "usefp.org",
        "future.utoronto.ca",
        "vanier.gc.ca",
        "fulbrightprogram.org",
    ]
    default_queries: List[str] = [
        "USEFP Fulbright Pakistan scholarship Master PhD eligibility 2027",
        "Global UGRAD Pakistan undergraduate semester exchange USEFP",
        "Lester B Pearson international scholarship University of Toronto Pakistan",
        "Canada Vanier graduate scholarship international students",
    ]
