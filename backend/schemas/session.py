from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from schemas.student import StudentProfile
from schemas.scholarship import Scholarship
from schemas.scoring import CompositeScoreResult


class SessionStatus(str, Enum):
    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    PAUSED = "PAUSED"


class SessionCreate(BaseModel):
    student_profile: StudentProfile
    mission_parameters: Dict[str, Any] = Field(default_factory=dict)


class SessionSummary(BaseModel):
    session_id: str
    student_id: str
    student_name: str
    target_degree: str
    created_at: str
    completed_at: Optional[str] = None
    total_scanned: int = 0
    total_verified: int = 0
    top_scholarship_name: Optional[str] = None
    top_match_score: Optional[float] = None
    status: SessionStatus = Field(default=SessionStatus.INITIATED)


class SessionDetail(BaseModel):
    session_id: str
    student_id: str
    student_profile: StudentProfile
    mission_parameters: Dict[str, Any] = Field(default_factory=dict)
    status: SessionStatus = Field(default=SessionStatus.INITIATED)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    completed_at: Optional[str] = None
    
    total_scanned: int = 0
    total_verified: int = 0
    
    discovered_scholarships: List[Scholarship] = Field(default_factory=list)
    ranked_results: List[CompositeScoreResult] = Field(default_factory=list)
    execution_timeline: List[Dict[str, Any]] = Field(default_factory=list)
    sources_visited: List[str] = Field(default_factory=list)


class CachedScholarshipRecord(BaseModel):
    scholarship_id: str
    name: str
    country: str
    region: str
    data_json: str
    discovered_at: str
    verified_at: Optional[str] = None
    ttl_seconds: int = 604800  # 7 days default
    source_urls: List[str] = Field(default_factory=list)
