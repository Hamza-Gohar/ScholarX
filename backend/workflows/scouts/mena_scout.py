from typing import List
from workflows.scouts.base_scout import BaseScout


class MenaScout(BaseScout):
    region_name: str = "MENA"
    default_domains: List[str] = [
        "turkiyeburslari.gov.tr",
        "kaust.edu.sa",
        "kfupm.edu.sa",
        "hbku.edu.qa",
    ]
    default_queries: List[str] = [
        "Turkiye Burslari scholarship Pakistan application requirements 2027",
        "KAUST fellowship Saudi Arabia full funding Pakistani students",
        "KFUPM graduate fellowship computer science Pakistan",
        "Hamad Bin Khalifa University Qatar scholarship Pakistani students",
    ]
