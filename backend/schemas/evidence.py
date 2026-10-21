from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class VerificationVerdict(str, Enum):
    VERIFIED = "VERIFIED"
    PARTIALLY_VERIFIED = "PARTIALLY_VERIFIED"
    SUSPICIOUS = "SUSPICIOUS"
    OUTDATED = "OUTDATED"
    HEC_CONFIRMED = "HEC_CONFIRMED"


class SourceCitation(BaseModel):
    url: str = Field(..., description="Absolute source URL")
    title: str = Field(default="Official Portal", description="Webpage or document title")
    domain: str = Field(default="", description="Source domain (e.g. stipendiumhungaricum.hu, hec.gov.pk)")
    source_type: str = Field(
        default="GOVERNMENT_PORTAL",
        description="GOVERNMENT_PORTAL, UNIVERSITY_PORTAL, EMBASSY_SITE, SCHOLARSHIP_BODY, NEWS"
    )
    snippet: str = Field(default="", description="Relevant textual quote extracted from page")
    verified_at: Optional[str] = Field(default=None, description="ISO timestamp of verification")
    is_official_hec: bool = Field(default=False, description="Whether source is official HEC Pakistan")


class SkepticChallenge(BaseModel):
    challenge_id: str = Field(..., description="Unique challenge ID")
    category: str = Field(
        default="HIDDEN_COST",
        description="HIDDEN_COST, VISA_RISK, RETURN_OBLIGATION, DEADLINE_RISK, COMPETITION, STIPEND_DEVALUATION"
    )
    title: str = Field(..., description="Short summary of the skepticism")
    description: str = Field(..., description="Detailed argument raised by Skeptic Agent")
    severity: str = Field(default="MEDIUM", description="LOW, MEDIUM, HIGH, CRITICAL")
    suggested_mitigation: Optional[str] = Field(default=None, description="Action the student can take")
    resolved: bool = Field(default=False, description="Whether the defense answered this challenge")


class DebateTopic(BaseModel):
    topic: str
    advocate_point: str = Field(..., description="Why this scholarship is strong for the student")
    skeptic_counterpoint: str = Field(..., description="Why the student might struggle or face hidden barriers")
    verdict: str = Field(..., description="Synthesized objective outcome")


class EvidenceTrail(BaseModel):
    scholarship_id: str
    overall_verdict: VerificationVerdict = Field(default=VerificationVerdict.PARTIALLY_VERIFIED)
    confidence_score: float = Field(default=0.8, ge=0.0, le=1.0)
    sources: List[SourceCitation] = Field(default_factory=list)
    skeptic_challenges: List[SkepticChallenge] = Field(default_factory=list)
    debate_summary: List[DebateTopic] = Field(default_factory=list)
    last_verified_timestamp: Optional[str] = None
    verification_notes: Optional[str] = None
