from typing import List
from workflows.scouts.base_scout import BaseScout


class AsiaScout(BaseScout):
    region_name: str = "Asia"
    default_domains: List[str] = [
        "campuschina.org",
        "studyinjapan.go.jp",
        "studyinkorea.go.kr",
        "anso.org.cn",
        "hec.gov.pk",
    ]
    default_queries: List[str] = [
        "Chinese Government Scholarship CSC Type A Pakistani students HEC 2027",
        "MEXT Japanese Government scholarship embassy track Pakistan 2027",
        "Global Korea Scholarship GKS KGSP Pakistani students 2027",
        "ANSO scholarship Chinese Academy of Sciences Pakistan",
    ]
