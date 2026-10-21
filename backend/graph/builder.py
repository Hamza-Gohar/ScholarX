import logging
from langgraph.graph import StateGraph, START, END
from graph.state import ScholarXState
from graph.nodes import (
    orchestrator_node,
    profile_analyzer_node,
    discovery_commander_node,
    eligibility_node,
    cost_analyzer_node,
    deadline_analyzer_node,
    skeptic_node,
    synthesis_node,
    ranking_node,
    advisor_node,
)

logger = logging.getLogger("scholarx.graph")


def build_scholarx_graph():
    """
    Constructs and compiles the complete 10-stage ScholarX LangGraph StateGraph.
    Pipeline:
      START -> Orchestrator -> Profile Analyzer -> Discovery Commander ->
      Eligibility -> True Cost -> Deadline Intelligence -> Skeptic Agent ->
      Synthesis -> Ranking Engine -> Final Advisor -> END
    """
    graph = StateGraph(ScholarXState)

    # 1. Register All Nodes
    graph.add_node("orchestrator", orchestrator_node)
    graph.add_node("profile_analyzer", profile_analyzer_node)
    graph.add_node("discovery_commander", discovery_commander_node)
    graph.add_node("eligibility_analyzer", eligibility_node)
    graph.add_node("cost_analyzer", cost_analyzer_node)
    graph.add_node("deadline_analyzer", deadline_analyzer_node)
    graph.add_node("skeptic_agent", skeptic_node)
    graph.add_node("synthesis_engine", synthesis_node)
    graph.add_node("ranking_engine", ranking_node)
    graph.add_node("advisor_agent", advisor_node)

    # 2. Sequential Edges
    graph.add_edge(START, "orchestrator")
    graph.add_edge("orchestrator", "profile_analyzer")
    graph.add_edge("profile_analyzer", "discovery_commander")
    graph.add_edge("discovery_commander", "eligibility_analyzer")
    graph.add_edge("eligibility_analyzer", "cost_analyzer")
    graph.add_edge("cost_analyzer", "deadline_analyzer")
    graph.add_edge("deadline_analyzer", "skeptic_agent")
    graph.add_edge("skeptic_agent", "synthesis_engine")
    graph.add_edge("synthesis_engine", "ranking_engine")
    graph.add_edge("ranking_engine", "advisor_agent")
    graph.add_edge("advisor_agent", END)

    compiled = graph.compile()
    logger.info("Complete ScholarX 10-node LangGraph StateGraph compiled successfully.")
    return compiled
