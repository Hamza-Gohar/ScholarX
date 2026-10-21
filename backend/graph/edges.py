from typing import Literal
from graph.state import ScholarXState


def route_after_profile(state: ScholarXState) -> Literal["discovery", "profile_incomplete"]:
    """Determines whether profile has mandatory fields or requires user intervention."""
    profile = state.get("student_profile")
    if not profile or len(profile.missing_required) > 0:
        return "profile_incomplete"
    return "discovery"


def route_after_verification(state: ScholarXState) -> Literal["skeptic_debate", "synthesis"]:
    """Routes high-confidence candidates into skeptic challenge or straight to synthesis."""
    evidence = state.get("evidence_trails", {})
    if len(evidence) > 0:
        return "skeptic_debate"
    return "synthesis"
