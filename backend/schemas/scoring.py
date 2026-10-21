from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class DimensionStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"
    BONUS = "BONUS"
    ACTION_REQUIRED = "ACTION_REQUIRED"


class DimensionScore(BaseModel):
    dimension_name: str
    score: float = Field(..., ge=0.0, le=100.0)
    weight: float = Field(..., ge=0.0, le=1.0)
    status: DimensionStatus = Field(default=DimensionStatus.PASS)
    details: str = Field(default="")
    evidence_snippet: Optional[str] = None


class CostPhaseItem(BaseModel):
    item_name: str
    cost_pkr: int
    cost_usd: Optional[int] = None
    is_mandatory: bool = True
    pakistan_context: Optional[str] = None


class CostAnalysisResult(BaseModel):
    pre_application_pkr: int = 0
    application_pkr: int = 0
    visa_travel_pkr: int = 0
    settlement_pkr: int = 0
    total_out_of_pocket_pkr: int = 0
    total_out_of_pocket_usd: int = 0
    student_max_budget_pkr: int = 150000
    shortfall_pkr: int = 0
    is_within_budget: bool = True
    funding_score: float = Field(default=100.0, ge=0.0, le=100.0)
    cost_items: List[CostPhaseItem] = Field(default_factory=list)
    risk_warnings: List[str] = Field(default_factory=list)


class DeadlineAnalysisResult(BaseModel):
    deadline_date: str
    days_remaining: int
    prep_days_needed_pakistan: int
    slack_days: int
    risk_level: str = Field(default="LOW", description="LOW, MODERATE, HIGH, VERY_HIGH, IMPOSSIBLE")
    is_feasible: bool = True
    deadline_score: float = Field(default=100.0, ge=0.0, le=100.0)
    action_timeline_recommendation: List[str] = Field(default_factory=list)


class CompositeScoreResult(BaseModel):
    scholarship_id: str
    scholarship_name: str
    overall_match_score: float = Field(..., ge=0.0, le=100.0, description="Overall weighted score 0-100")
    rank: int = Field(default=1, ge=1)
    
    # Sub-component scores
    eligibility_score: float = Field(default=0.0, ge=0.0, le=100.0)
    true_funding_score: float = Field(default=0.0, ge=0.0, le=100.0)
    bilateral_bonus_score: float = Field(default=0.0, ge=0.0, le=100.0)
    academic_fit_score: float = Field(default=0.0, ge=0.0, le=100.0)
    doc_readiness_score: float = Field(default=0.0, ge=0.0, le=100.0)
    deadline_score: float = Field(default=0.0, ge=0.0, le=100.0)
    verification_score: float = Field(default=0.0, ge=0.0, le=100.0)
    competition_score: float = Field(default=0.0, ge=0.0, le=100.0)
    
    dimensions: List[DimensionScore] = Field(default_factory=list)
    cost_analysis: CostAnalysisResult = Field(default_factory=CostAnalysisResult)
    deadline_analysis: Optional[DeadlineAnalysisResult] = None
    
    blocking_reasons: List[str] = Field(default_factory=list)
    pakistan_specific_advantages: List[str] = Field(default_factory=list)
    is_recommended: bool = True
