import asyncio
import logging
from typing import Any, Dict, List
from agents.advisor_agent import AdvisorAgent
from agents.discovery_commander import DiscoveryCommander
from agents.skeptic_agent import SkepticAgent
from events.bus import get_event_bus
from graph.state import ScholarXState
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.scholarship import Scholarship
from workflows.cost_analyzer import TrueCostAnalyzer
from workflows.deadline import DeadlineAnalyzer
from workflows.degree_matching import get_degree_scholarship_limit
from workflows.eligibility import EligibilityInvestigator
from workflows.ranking import RankingEngine
from workflows.synthesis import SynthesisWorkflow

logger = logging.getLogger("scholarx.graph.nodes")


_LIVE_TASKS: set = set()


def _dispatch_live(evt: ScholarXEvent):
    """Dispatches event immediately to global EventBus in real time."""
    try:
        bus = get_event_bus()
        loop = asyncio.get_running_loop()
        task = loop.create_task(bus.publish(evt))
        _LIVE_TASKS.add(task)
        task.add_done_callback(_LIVE_TASKS.discard)
    except Exception as e:
        logger.debug(f"EventBus live dispatch skipped: {e}")


async def orchestrator_node(state: ScholarXState) -> Dict[str, Any]:
    """Root node that initializes the mission and checks session continuity."""
    session_id = state.get("session_id", "default-session")
    logger.info(f"Orchestrator node activated for session: {session_id}")

    init_event = ScholarXEvent(
        session_id=session_id,
        event_type=AgentEventType.MISSION_INITIATED,
        agent_id="orchestrator",
        agent_display_name="Mission Orchestrator",
        component_type="AGENT",
        phase="ORCHESTRATION",
        payload={"message": "ScholarX intelligence network activated for Pakistani student profile."},
        severity=EventSeverity.INFO,
    )
    _dispatch_live(init_event)

    return {
        "active_phase": "PROFILE_ANALYSIS",
        "events_queue": [init_event],
    }


async def profile_analyzer_node(state: ScholarXState) -> Dict[str, Any]:
    """Node that validates and prepares the student profile."""
    session_id = state.get("session_id", "default-session")
    profile = state.get("student_profile")
    
    event = ScholarXEvent(
        session_id=session_id,
        event_type=AgentEventType.PROFILE_COMPLETE,
        agent_id="profile_agent",
        agent_display_name="Profile Analyst",
        component_type="AGENT",
        phase="INTAKE",
        payload={
            "student_name": profile.personal.name if profile else "Unknown",
            "gpa": profile.academic.gpa_percentage if profile else 0,
            "target_degree": profile.preferences.target_degree_level if profile else "Bachelor's",
        },
        severity=EventSeverity.SUCCESS,
    )
    _dispatch_live(event)

    return {
        "active_phase": "DISCOVERY",
        "events_queue": [event],
    }


async def discovery_commander_node(state: ScholarXState) -> Dict[str, Any]:
    """Node that executes concurrent regional discovery and candidate pool aggregation."""
    session_id = state.get("session_id", "default-session")
    profile = state.get("student_profile")

    if not profile:
        logger.error("No student profile found in state for discovery.")
        return {
            "active_phase": "DISCOVERY",
            "errors": ["Missing student profile for discovery"],
        }

    # If candidate scholarships were already passed in initial_state, keep them
    existing_candidates = state.get("candidate_scholarships") or []
    if existing_candidates:
        return {
            "active_phase": "ELIGIBILITY_ANALYSIS",
            "candidate_scholarships": existing_candidates,
        }

    commander = DiscoveryCommander()
    events_collected: List[ScholarXEvent] = []

    def event_collector(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    candidates = await commander.execute_discovery_mission(
        student=profile,
        event_callback=event_collector,
    )

    return {
        "active_phase": "ELIGIBILITY_ANALYSIS",
        "candidate_scholarships": candidates,
        "events_queue": events_collected,
    }


async def eligibility_node(state: ScholarXState) -> Dict[str, Any]:
    """Evaluates candidate pool across 15 eligibility dimensions."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    if not profile or not candidates:
        return {"active_phase": "COST_ANALYSIS"}

    investigator = EligibilityInvestigator()
    events_collected: List[ScholarXEvent] = []
    elig_results_dict = {}

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    for sc in candidates:
        res = investigator.evaluate(sc, profile, event_callback=cb)
        elig_results_dict[sc.scholarship_id] = res

    return {
        "active_phase": "COST_ANALYSIS",
        "eligibility_results": elig_results_dict,
        "events_queue": events_collected,
    }


async def cost_analyzer_node(state: ScholarXState) -> Dict[str, Any]:
    """Calculates 4-phase out-of-pocket expenses in PKR."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    if not profile or not candidates:
        return {"active_phase": "DEADLINE_ANALYSIS"}

    cost_analyzer = TrueCostAnalyzer()
    events_collected: List[ScholarXEvent] = []
    cost_results_dict = {}

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    for sc in candidates:
        res = cost_analyzer.analyze(sc, profile, event_callback=cb)
        cost_results_dict[sc.scholarship_id] = res

    return {
        "active_phase": "DEADLINE_ANALYSIS",
        "cost_results": cost_results_dict,
        "events_queue": events_collected,
    }


async def deadline_analyzer_node(state: ScholarXState) -> Dict[str, Any]:
    """Evaluates application deadlines and preparation lead times."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    if not profile or not candidates:
        return {"active_phase": "SKEPTIC_ANALYSIS"}

    deadline_analyzer = DeadlineAnalyzer()
    events_collected: List[ScholarXEvent] = []
    deadline_results_dict = {}

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    for sc in candidates:
        res = deadline_analyzer.analyze(sc, profile, event_callback=cb)
        deadline_results_dict[sc.scholarship_id] = res

    return {
        "active_phase": "SKEPTIC_ANALYSIS",
        "deadline_results": deadline_results_dict,
        "events_queue": events_collected,
    }


async def skeptic_node(state: ScholarXState) -> Dict[str, Any]:
    """Executes adversarial challenge review on candidates."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    if not profile or not candidates:
        return {"active_phase": "SYNTHESIS"}

    skeptic = SkepticAgent()
    events_collected: List[ScholarXEvent] = []
    elig_dict = state.get("eligibility_results", {})
    
    # Prioritize top 3 candidates for deep adversarial scrutiny, rule-based for the rest
    def get_elig_score(c):
        res = elig_dict.get(c.scholarship_id)
        return getattr(res, "overall_score", 0.0) if res else 0.0

    sorted_candidates = sorted(candidates, key=get_elig_score, reverse=True)
    eval_pool = sorted_candidates[:3]

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    async def evaluate_single(sc):
        try:
            ev = await asyncio.wait_for(
                skeptic.evaluate_skepticism(sc, profile, event_callback=cb),
                timeout=5.0,
            )
            return sc.scholarship_id, ev
        except Exception as exc:
            logger.debug(f"Skeptic LLM fallback to rule-based for {sc.name}: {exc}")
            ev = skeptic._generate_rule_based_evidence_trail(sc, profile)
            return sc.scholarship_id, ev

    results = await asyncio.gather(*[evaluate_single(sc) for sc in eval_pool])
    evidence_dict = dict(results)

    # Generate complete rule-based evidence trails for remaining candidates
    for sc in candidates:
        if sc.scholarship_id not in evidence_dict or evidence_dict[sc.scholarship_id] is None:
            evidence_dict[sc.scholarship_id] = skeptic._generate_rule_based_evidence_trail(sc, profile)

    return {
        "active_phase": "SYNTHESIS",
        "evidence_trails": evidence_dict,
        "events_queue": events_collected,
    }


async def synthesis_node(state: ScholarXState) -> Dict[str, Any]:
    """Synthesizes candidate signals into unified DNA cards."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    elig_dict = state.get("eligibility_results", {})
    cost_dict = state.get("cost_results", {})
    deadline_dict = state.get("deadline_results", {})
    evidence_dict = state.get("evidence_trails", {})

    if not profile or not candidates:
        return {"active_phase": "RANKING"}

    synthesis_wf = SynthesisWorkflow()
    events_collected: List[ScholarXEvent] = []

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    from schemas.evidence import EvidenceTrail, VerificationVerdict

    for sc in candidates:
        elig = elig_dict.get(sc.scholarship_id)
        cost = cost_dict.get(sc.scholarship_id)
        dl = deadline_dict.get(sc.scholarship_id)
        ev = evidence_dict.get(sc.scholarship_id)
        if elig and cost and dl:
            if not ev:
                ev = EvidenceTrail(
                    scholarship_id=sc.scholarship_id,
                    overall_verdict=VerificationVerdict.PARTIALLY_VERIFIED,
                    confidence_score=0.6,
                    verification_notes="Provisional baseline evidence trail.",
                )
            synthesis_wf.synthesize(sc, elig, cost, dl, ev, profile, event_callback=cb)

    return {
        "active_phase": "RANKING",
        "events_queue": events_collected,
    }


async def ranking_node(state: ScholarXState) -> Dict[str, Any]:
    """Calculates weighted composite ranking across all candidates."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    elig_dict = state.get("eligibility_results", {})
    cost_dict = state.get("cost_results", {})
    deadline_dict = state.get("deadline_results", {})
    evidence_dict = state.get("evidence_trails", {})

    if not profile or not candidates:
        return {"active_phase": "ADVISOR"}

    ranking_engine = RankingEngine()
    events_collected: List[ScholarXEvent] = []

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    from schemas.evidence import EvidenceTrail, VerificationVerdict

    bundles = []
    for sc in candidates:
        elig = elig_dict.get(sc.scholarship_id)
        cost = cost_dict.get(sc.scholarship_id)
        dl = deadline_dict.get(sc.scholarship_id)
        ev = evidence_dict.get(sc.scholarship_id)
        if elig and cost and dl:
            if not ev:
                ev = EvidenceTrail(
                    scholarship_id=sc.scholarship_id,
                    overall_verdict=VerificationVerdict.PARTIALLY_VERIFIED,
                    confidence_score=0.6,
                    verification_notes="Provisional baseline evidence trail.",
                )
            bundles.append((sc, elig, cost, dl, ev))

    target_deg = profile.preferences.target_degree_level if profile and profile.preferences else None
    output_limit = get_degree_scholarship_limit(target_deg)

    ranked = ranking_engine.rank_opportunities(bundles, profile, event_callback=cb)
    qualified_ranked = [r for r in ranked if r.overall_match_score > 50.0]
    if len(qualified_ranked) > output_limit:
        qualified_ranked = qualified_ranked[:output_limit]
    qualified_ids = {r.scholarship_id for r in qualified_ranked}
    qualified_candidates = [sc for sc in candidates if sc.scholarship_id in qualified_ids]

    return {
        "active_phase": "ADVISOR",
        "ranked_results": qualified_ranked,
        "candidate_scholarships": qualified_candidates,
        "events_queue": events_collected,
    }


async def advisor_node(state: ScholarXState) -> Dict[str, Any]:
    """Generates personalized Pakistan roadmap for top opportunity."""
    profile = state.get("student_profile")
    candidates = state.get("candidate_scholarships", [])
    ranked = state.get("ranked_results", [])

    if not profile or not candidates or not ranked:
        return {"active_phase": "MISSION_COMPLETE"}

    top_result = ranked[0]
    top_sc = next((sc for sc in candidates if sc.scholarship_id == top_result.scholarship_id), candidates[0])

    advisor = AdvisorAgent()
    events_collected: List[ScholarXEvent] = []

    def cb(evt: ScholarXEvent):
        events_collected.append(evt)
        _dispatch_live(evt)

    roadmap = await advisor.generate_roadmap(
        top_sc,
        top_result,
        profile,
        event_callback=cb,
    )

    return {
        "active_phase": "MISSION_COMPLETE",
        "final_roadmap": roadmap,
        "events_queue": events_collected,
    }
