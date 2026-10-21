from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class RoadmapPhase(str, Enum):
    DOCUMENT_PREPARATION = "DOCUMENT_PREPARATION"
    HEC_IBCC_ATTESTATION = "HEC_IBCC_ATTESTATION"
    STANDARDIZED_TESTS = "STANDARDIZED_TESTS"
    ONLINE_PORTAL_APPLICATION = "ONLINE_PORTAL_APPLICATION"
    EMBASSY_INTERVIEW_VISA = "EMBASSY_INTERVIEW_VISA"
    PRE_DEPARTURE_TRAVEL = "PRE_DEPARTURE_TRAVEL"


class PakistaniOffice(BaseModel):
    office_name: str = Field(..., description="e.g. HEC Regional Center Lahore, IBCC Islamabad")
    office_type: str = Field(..., description="HEC, IBCC, MOFA, BRITISH_COUNCIL, VFS_GERRYS, EMBASSY, PANEL_CLINIC")
    city: str
    address: str
    website_or_portal: Optional[str] = None
    fee_pkr: int = 0
    estimated_turnaround_days: int = 14
    required_documents: List[str] = Field(default_factory=list)
    pro_tips: List[str] = Field(default_factory=list)


class MilestoneAction(BaseModel):
    action_id: str
    description: str
    estimated_days: int
    estimated_cost_pkr: int = 0
    is_blocking: bool = True
    assigned_office: Optional[str] = None
    completed: bool = False


class RoadmapMilestone(BaseModel):
    milestone_id: str
    title: str
    phase: RoadmapPhase
    target_timeline_days: str = Field(..., description="e.g. Day 1 to Day 14")
    total_phase_cost_pkr: int = 0
    actions: List[MilestoneAction] = Field(default_factory=list)
    guidance_notes: Optional[str] = None


class ApplicationRoadmap(BaseModel):
    scholarship_id: str
    scholarship_name: str
    host_country: str
    target_intake: str = "Fall 2026"
    total_preparation_days_estimated: int = 45
    total_budget_needed_pkr: int = 250000
    milestones: List[RoadmapMilestone] = Field(default_factory=list)
    relevant_pakistani_offices: List[PakistaniOffice] = Field(default_factory=list)
    urgent_next_actions: List[str] = Field(default_factory=list)
