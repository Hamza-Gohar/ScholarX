// Centralized Agent and Commander Lifecycle Types (§8, Appendix A.3, Agents.md)

export type CommanderState =
  | "IDLE"
  | "THINKING"
  | "DECIDING"
  | "DIRECTING"
  | "WAITING"
  | "RECEIVING"
  | "SYNTHESIZING"
  | "COMPLETE";

export type AgentLifecycleState =
  | "IDLE"
  | "RECEIVING"
  | "RECEIVING_COMMAND"
  | "ACKNOWLEDGING"
  | "DEPLOYING"
  | "WORKING"
  | "SEARCHING"
  | "FILTERING"
  | "SCRAPING"
  | "READING"
  | "EXTRACTING"
  | "NORMALIZING"
  | "DISCOVERING"
  | "ASSEMBLING_REPORT"
  | "REPORT_READY"
  | "ANALYZING"
  | "VERIFYING"
  | "REPORTING"
  | "RETURNING"
  | "COMPLETE"
  | "BLOCKED"
  | "FAILED"
  | "RECOVERING"
  | "CACHED";

export type SpawnPhase =
  | "UNSPAWNED"
  | "SEED"
  | "SURFACE"
  | "IDENTITY"
  | "EXPANSION"
  | "MISSION_REVEAL"
  | "ACTIVE"
  | "SETTLED";

export type EntityType = "AGENT" | "WORKFLOW";

export interface CommanderDirective {
  targetId: string;
  targetName: string;
  targetType: EntityType;
  objective: string;
  expectedOutput: string;
  constraints: string[];
  issuedAt?: number;
}

export interface AgentEntity {
  agentId: string;
  displayName: string;
  entityType: EntityType;
  parentId: string | null;
  region: string;
  mission: string;
  state: AgentLifecycleState;
  stateSince: number;
  currentOperation: string;
  finding: string;
  progress: number; // 0 to 100
  spawnedAt: number | null;
  spawnPhase: SpawnPhase;
  coordinates?: [number, number]; // [lon, lat]
}

export type Phase3Scenario =
  | "IDLE"
  | "THINKING"
  | "DIRECTING"
  | "SPAWN"
  | "ACTIVE"
  | "WORKING";
