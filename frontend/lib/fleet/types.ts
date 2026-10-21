// Phase 5: Global AI Research Fleet & Tool Activity Types (§7, §8, §12, §13, Agents.md)
import { Region } from "../types";
import type {
  DiscoveredSource,
  ScholarshipCandidateSummary,
  SectorReportSummary,
  PhysicalPacket,
} from "../communication/types";

export type {
  DiscoveredSource,
  ScholarshipCandidateSummary,
  SectorReportSummary,
  PhysicalPacket,
};
import { CommanderState, CommanderDirective } from "../agents/types";

// 14 Required Scout States (§8)
export type ScoutState =
  | "IDLE"
  | "DEPLOYING"
  | "RECEIVING_COMMAND"
  | "ACKNOWLEDGING"
  | "SEARCHING"
  | "FILTERING"
  | "SCRAPING"
  | "EXTRACTING"
  | "NORMALIZING"
  | "DISCOVERING"
  | "ASSEMBLING_REPORT"
  | "REPORT_READY"
  | "RETURNING"
  | "COMPLETE"
  | "FAILED"
  | "RECOVERING"
  | "FALLBACK"
  | "UNAVAILABLE";

// 6 Required Research Tools (§12, §13)
export type ResearchToolType =
  | "TAVILY_SEARCH"
  | "FIRECRAWL"
  | "JINA_READER"
  | "CRAWL4AI"
  | "GEMINI_EXTRACTION"
  | "CANONICAL_NORMALIZER";

export interface ToolActivityMeta {
  type: ResearchToolType;
  displayName: string;
  actionLabel: string;
  color: string;
  iconName: string;
  targetDomain?: string;
  executionNote?: string;
}

export interface RegionalScoutData {
  scoutId: string;
  region: Region;
  displayName: string;
  role: string;
  mission: string;
  coordinates: [number, number]; // [lon, lat]
  scenePosition: { x: number; y: number };
  state: ScoutState;
  progress: number; // 0 to 100
  activeTool: ToolActivityMeta | null;
  activeQuery?: string;
  currentOperation: string;
  finding: string;
  sources: DiscoveredSource[];
  candidates: ScholarshipCandidateSummary[];
  report: SectorReportSummary | null;
  reportReady: boolean;
  pakistanQuotaSeats: number;
}

export interface GlobalFleetStats {
  scoutsDeployed: number;
  activeScoutsCount: number;
  reportsReceived: number;
  totalSourcesDiscovered: number;
  totalCandidatesExtracted: number;
  pakistanQuotaSeatsTotal: number;
  operationalStatus: string;
}

export type Phase5Step =
  | "FLEET_INIT"
  | "DIRECTIVES_FORMED"
  | "STAGGERED_DISPATCH"
  | "SCOUTS_ACKNOWLEDGE"
  | "PARALLEL_SEARCH_START"
  | "DIVERGENT_TOOL_OPERATIONS"
  | "SOURCES_DISCOVERED"
  | "CANDIDATE_EMERGENCE"
  | "REGIONAL_REPORTS_ASSEMBLED"
  | "STAGGERED_REPORT_RETURN"
  | "COMMANDER_AGGREGATION"
  | "FLEET_COMPLETE";

export interface Phase5StepMeta {
  step: Phase5Step;
  index: number;
  label: string;
  narrative: string;
  durationMs: number;
  cameraShot: "GLOBAL" | "DEPLOYMENT" | "REGIONAL";
  focusedRegion: Region | "Pakistan" | null;
  focusedEntity: "COMMANDER" | Region | "FLEET";
}

export interface FleetSnapshot {
  step: Phase5Step;
  stepMeta: Phase5StepMeta;
  commander: {
    state: CommanderState;
    mission: string;
    headline: string;
    currentDecision: string | null;
    activeDirectives: CommanderDirective[];
    receivedReports: SectorReportSummary[];
  };
  scouts: Record<Region, RegionalScoutData>;
  activePackets: PhysicalPacket[];
  globalStats: GlobalFleetStats;
  focusedRegion: Region | "Pakistan" | null;
  focusedEntity: "COMMANDER" | Region | "FLEET";
}
