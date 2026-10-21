from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from schemas.scholarship import Scholarship


class PersonalizedMatch(BaseModel):
    scholarship: Scholarship
    match_score: float = Field(ge=0.0, le=100.0)
    score_breakdown: Dict[str, float] = Field(default_factory=dict)
    match_reasons: List[str] = Field(default_factory=list)
    risk_flags: List[str] = Field(default_factory=list)
    data_source: str = "VERIFIED_DATABASE"
    source_url: Optional[str] = None
    verified_at: Optional[str] = None


class PersonalizedSearchResponse(BaseModel):
    matches: List[PersonalizedMatch]
    scholarships: List[Scholarship]
    total: int
    profile_summary: Dict[str, Any]
    database: Dict[str, Any]
