from typing import Annotated, Any, Dict, List, Optional, TypedDict
from schemas.evidence import EvidenceTrail, SkepticChallenge
from schemas.events import ScholarXEvent
from schemas.roadmap import ApplicationRoadmap
from schemas.scholarship import Scholarship
from schemas.scoring import CompositeScoreResult, CostAnalysisResult, DeadlineAnalysisResult
from schemas.student import StudentProfile


def merge_lists(left: List[Any], right: List[Any]) -> List[Any]:
    """Reducer that combines lists without duplicates where applicable."""
    if not left:
        return right or []
    if not right:
        return left or []
    return left + right


def merge_dicts(left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
    """Reducer that merges dictionary mappings."""
    merged = dict(left or {})
    merged.update(right or {})
    return merged


class ScholarXState(TypedDict, total=False):
    # Core Mission & Session IDs
    session_id: str
    student_id: str
    active_phase: str
    
    # Ingested Profile & Documents
    student_profile: Optional[StudentProfile]
    raw_documents: List[Dict[str, Any]]
    mission_constraints: List[str]
    
    # Discovery Pool (Fan-out aggregation)
    candidate_scholarships: Annotated[List[Scholarship], merge_lists]
    
    # Analysis & Verification State
    eligibility_results: Annotated[Dict[str, Any], merge_dicts]
    cost_results: Annotated[Dict[str, CostAnalysisResult], merge_dicts]
    deadline_results: Annotated[Dict[str, DeadlineAnalysisResult], merge_dicts]
    evidence_trails: Annotated[Dict[str, EvidenceTrail], merge_dicts]
    skeptic_challenges: Annotated[Dict[str, List[SkepticChallenge]], merge_dicts]
    
    # Synthesis & Final Outputs
    ranked_results: List[CompositeScoreResult]
    final_roadmap: Optional[ApplicationRoadmap]
    
    # Real-time Events Stream Buffer
    events_queue: Annotated[List[ScholarXEvent], merge_lists]
    
    # Resilience & Control
    errors: Annotated[List[str], merge_lists]
    human_approval_required: bool
    human_approved: bool
