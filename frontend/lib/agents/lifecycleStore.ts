// Centralized Agent Lifecycle State Store (§8, Appendix A.3)
import {
  CommanderState,
  AgentLifecycleState,
  SpawnPhase,
  EntityType,
  AgentEntity,
  CommanderDirective,
  Phase3Scenario,
} from "./types";

export interface LifecycleState {
  scenario: Phase3Scenario;
  commander: {
    state: CommanderState;
    mission: string;
    constraints: string[];
    availableActions: string[];
    nextDecision: string;
    currentDecision: string | null;
    activeDirective: CommanderDirective | null;
    stateSince: number;
  };
  europeScout: AgentEntity | null;
  focusedEntity: "COMMANDER" | "SCOUT" | null;
}

export const INITIAL_DIRECTIVE: CommanderDirective = {
  targetId: "scout-eu",
  targetName: "Europe Regional Scout",
  targetType: "WORKFLOW",
  objective: "Discover fully funded CS opportunities for Pakistani applicants.",
  expectedOutput: "Normalized scholarship candidates.",
  constraints: [
    "HEC Attestation and IBCC Equivalence Compatible",
    "Zero Tuition / Living Stipend Covered",
    "Pakistani Bilateral Quota Prioritized",
  ],
};

export const createScenarioState = (scenario: Phase3Scenario): LifecycleState => {
  const now = Date.now();

  switch (scenario) {
    case "IDLE":
      return {
        scenario: "IDLE",
        commander: {
          state: "IDLE",
          mission: "National Scholarship Intelligence Orchestration",
          constraints: ["Awaiting Mission Intake", "Pakistan Candidate Context"],
          availableActions: ["Initialize Global Intelligence", "Configure Regional Quotas"],
          nextDecision: "Standby for Intake Directive",
          currentDecision: null,
          activeDirective: null,
          stateSince: now,
        },
        europeScout: null,
        focusedEntity: "COMMANDER",
      };

    case "THINKING":
      return {
        scenario: "THINKING",
        commander: {
          state: "THINKING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          constraints: [
            "HEC Attestation & IBCC Equivalence Compatible",
            "Zero Out-of-Pocket / Living Stipend Covered",
            "Bilateral Quotas Prioritized (DAAD, Erasmus, Stipendium)",
          ],
          availableActions: [
            "Deploy Global Fleet (5 Regions)",
            "Activate Europe Regional Scout",
            "Audit Pakistan Quota Allocations",
          ],
          nextDecision: "Evaluate target region for deterministic scan",
          currentDecision: "Evaluating Sector Quotas",
          activeDirective: null,
          stateSince: now,
        },
        europeScout: null,
        focusedEntity: "COMMANDER",
      };

    case "DIRECTING":
      return {
        scenario: "DIRECTING",
        commander: {
          state: "DIRECTING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          constraints: [
            "HEC Attestation & IBCC Equivalence Compatible",
            "Zero Out-of-Pocket / Living Stipend Covered",
          ],
          availableActions: ["Deploying Directive to Workflow"],
          nextDecision: "Issue Directive to Europe Scout",
          currentDecision: "ACTIVATE EUROPE SCOUT",
          activeDirective: INITIAL_DIRECTIVE,
          stateSince: now,
        },
        europeScout: null,
        focusedEntity: "COMMANDER",
      };

    case "SPAWN":
      return {
        scenario: "SPAWN",
        commander: {
          state: "DIRECTING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          constraints: ["Autonomous Directive In Flight"],
          availableActions: ["Awaiting Workflow Surface Formation"],
          nextDecision: "Confirm Regional Seed Resolution",
          currentDecision: "ACTIVATE EUROPE SCOUT",
          activeDirective: INITIAL_DIRECTIVE,
          stateSince: now,
        },
        europeScout: {
          agentId: "scout-eu",
          displayName: "Europe Regional Scout",
          entityType: "WORKFLOW",
          parentId: "commander-root",
          region: "Europe",
          mission: "Scanning DAAD, Erasmus Mundus, and Stipendium Hungaricum quotas.",
          state: "DEPLOYING",
          stateSince: now,
          currentOperation: "RESOLVING REGIONAL WORKSPACE",
          finding: "NO FINDINGS YET",
          progress: 15,
          spawnedAt: now,
          spawnPhase: "SURFACE",
          coordinates: [13.405, 52.52],
        },
        focusedEntity: "SCOUT",
      };

    case "ACTIVE":
      return {
        scenario: "ACTIVE",
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          constraints: ["Directive Delegated to Child Process"],
          availableActions: ["Monitor Workflow Execution"],
          nextDecision: "Awaiting child workflow response",
          currentDecision: "DIRECTIVE DISPATCHED",
          activeDirective: INITIAL_DIRECTIVE,
          stateSince: now,
        },
        europeScout: {
          agentId: "scout-eu",
          displayName: "Europe Regional Scout",
          entityType: "WORKFLOW",
          parentId: "commander-root",
          region: "Europe",
          mission: "Discover fully funded CS opportunities for Pakistani applicants.",
          state: "ACKNOWLEDGING",
          stateSince: now,
          currentOperation: "DIRECTIVE ACKNOWLEDGED // INITIALIZING EXTRACTORS",
          finding: "NO FINDINGS YET",
          progress: 30,
          spawnedAt: now - 3000,
          spawnPhase: "ACTIVE",
          coordinates: [13.405, 52.52],
        },
        focusedEntity: "SCOUT",
      };

    case "WORKING":
      return {
        scenario: "WORKING",
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          constraints: ["Autonomous Child Process Active in Sector"],
          availableActions: ["Awaiting Normalized Candidates"],
          nextDecision: "Standby for candidate extraction stream",
          currentDecision: "AWAITING CHILD RESULT",
          activeDirective: INITIAL_DIRECTIVE,
          stateSince: now,
        },
        europeScout: {
          agentId: "scout-eu",
          displayName: "Europe Regional Scout",
          entityType: "WORKFLOW",
          parentId: "commander-root",
          region: "Europe",
          mission: "Discover fully funded CS opportunities for Pakistani applicants.",
          state: "WORKING",
          stateSince: now,
          currentOperation: "DETERMINISTIC PIPELINE RUNNING",
          finding: "NO FINDINGS YET",
          progress: 55,
          spawnedAt: now - 8000,
          spawnPhase: "SETTLED",
          coordinates: [13.405, 52.52],
        },
        focusedEntity: "SCOUT",
      };
  }
};
