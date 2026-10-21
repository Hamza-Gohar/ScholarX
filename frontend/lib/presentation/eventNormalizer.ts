// Master Event Normalizer (§18, §19, §23, §24, §25, §52)
// Converts raw backend ScholarXEvent into a typed MasterPresentationEvent with semantic priority,
// pacing duration, spatial routing anchors, and burst coalescing keys.

import { ScholarXEvent } from "@/lib/types";
import { MasterPresentationEvent, PresentationPriority, SceneIntent } from "./types";

export interface NormalizedSceneAction {
  sceneIntent: SceneIntent;
  description: string;
  badgeText: string;
  sourceAnchorId: string;
  targetAnchorId?: string;
  spawnPacket?: {
    kind: "DIRECTIVE" | "ACKNOWLEDGEMENT" | "REPORT" | "EVIDENCE" | "CHALLENGE" | "RESOLUTION";
    title: string;
    summary: string;
  };
}

export function normalizeBackendEvent(event: ScholarXEvent): MasterPresentationEvent {
  const eventType = event.event_type;
  const payload = event.payload || {};
  const region = payload.region || inferRegionFromAgent(event.agent_id);

  // 1. Determine Semantic Priority (§23)
  const importance = getEventPriority(eventType);

  // 2. Calculate Pacing & Display Duration (§21, §30)
  const { minDisplayMs, holdMs } = calculateDisplayPacing(eventType, importance);

  // 3. Assign Burst Coalescing Key (§22, §58)
  const coalesceKey = getCoalesceKey(eventType, region, event.related_scholarship_id || undefined);

  // 4. Resolve Spatial Anchors (§52)
  const sourceEntityId = resolveSourceEntity(event.agent_id, region);
  const targetEntityId = resolveTargetEntity(eventType, sourceEntityId, region);

  // 5. Derive Camera Shot & Focus (§19)
  const cameraMode = getCameraModeForEvent(eventType, region);
  const focusTarget = resolveFocusTarget(eventType, region, sourceEntityId);

  return {
    presentationEventId: `pres-${event.event_id}`,
    sourceEventId: event.event_id,
    missionId: event.session_id,
    timestamp: new Date(event.timestamp).getTime() || Date.now(),
    eventType: event.event_type,
    importance,
    phase: event.phase,
    sourceEntityId,
    targetEntityId,
    regionId: region,
    scholarshipId: event.related_scholarship_id || undefined,
    payload: sanitizePayload(payload),
    minimumDisplayMs: minDisplayMs,
    holdAfterMs: holdMs,
    coalesceKey,
    focusTarget,
    cameraMode,
  };
}

function getEventPriority(eventType: string): PresentationPriority {
  switch (eventType) {
    case "MISSION_INITIATED":
    case "MISSION_COMPLETE":
    case "FLEET_PAUSED":
    case "INELIGIBILITY_DETECTED":
    case "PIPELINE_ERROR":
    case "PIPELINE_RECOVERED":
    case "ELIGIBILITY_CHECK_STARTED":
    case "RANKING_CALCULATED":
    case "SKEPTIC_CHALLENGE_RAISED":
    case "SYNTHESIS_COMPLETE":
    case "ROADMAP_GENERATED":
    case "PRIMARY_SELECTION":
    case "SCOUT_FAILED":
    case "PARTIAL_DISCOVERY":
    case "SPECIALIST_FAILED":
    case "VERIFICATION_INCOMPLETE":
      return "HERO"; // Critical milestones & fault notices (§23, §56)

    case "SCOUT_DEPLOYED":
    case "CANDIDATE_EXTRACTED":
    case "SCOUT_COMPLETE":
    case "DATABASE_RETRIEVAL_COMPLETE":
    case "SUBJECTS_EVALUATED":
    case "INPUT_NORMALIZED":
    case "ELIGIBILITY_COMPLETE":
    case "COST_ANALYSIS_STARTED":
    case "COST_ANALYSIS_COMPLETE":
    case "DEADLINE_COMPLETE":
    case "SYNTHESIS_STARTED":
    case "VERIFICATION_COMPLETE":
    case "DISCOVERY_AGGREGATION_COMPLETE":
    case "PRIMARY_SEARCH_UNAVAILABLE":
    case "FALLBACK_SEARCH_ACTIVE":
    case "RESEARCH_RESUMED":
    case "SCOUT_RECOVERING":
    case "ARTIFACT_FAILED":
      return "SUPPORTING"; // High importance phase transitions & failover updates

    case "SEARCH_QUERY_EXECUTED":
    case "SOURCE_FOUND":
    case "PAGE_SCRAPED":
    case "DIMENSION_EVALUATED":
    case "PKR_BREAKDOWN_CALCULATED":
    case "DEADLINE_EVALUATED":
    case "PROFILE_COMPLETE":
      return "BACKGROUND"; // Normal work items

    case "API_KEY_ROTATED":
    case "API_KEY_EXHAUSTED":
    case "FALLBACK_TOOL_USED":
    case "CACHE_HIT":
    case "CACHE_MISS":
    default:
      return "AMBIENT"; // Low-key telemetry updates
  }
}

function calculateDisplayPacing(eventType: string, priority: PresentationPriority): { minDisplayMs: number; holdMs: number } {
  if (priority === "HERO") {
    return { minDisplayMs: 400, holdMs: 200 };
  }
  if (priority === "SUPPORTING") {
    return { minDisplayMs: 150, holdMs: 80 };
  }
  if (priority === "BACKGROUND") {
    return { minDisplayMs: 45, holdMs: 25 };
  }
  return { minDisplayMs: 25, holdMs: 15 };
}

function getCoalesceKey(eventType: string, region?: string, scholarshipId?: string): string | undefined {
  if (eventType === "SOURCE_FOUND") return `source-found-${region || "all"}`;
  if (eventType === "PAGE_SCRAPED") return `page-scraped-${region || "all"}`;
  if (eventType === "SEARCH_QUERY_EXECUTED") return `search-query-${region || "all"}`;
  if (eventType === "DIMENSION_EVALUATED") return `dimension-${scholarshipId || "all"}`;
  return undefined;
}

function inferRegionFromAgent(agentId: string): string | undefined {
  const lower = agentId.toLowerCase();
  if (lower.includes("europe")) return "Europe";
  if (lower.includes("asia")) return "Asia";
  if (lower.includes("americas")) return "Americas";
  if (lower.includes("mena")) return "MENA";
  if (lower.includes("oceania")) return "Oceania";
  return undefined;
}

function resolveSourceEntity(agentId: string, region?: string): string {
  const lower = agentId.toLowerCase();
  if (lower.includes("orchestrator") || lower.includes("commander")) return "commander-root";
  if (region) return `scout-${region.toLowerCase()}`;
  if (lower.includes("eligibility")) return "specialist-eligibility";
  if (lower.includes("cost")) return "specialist-cost";
  if (lower.includes("deadline")) return "specialist-deadline";
  if (lower.includes("skeptic")) return "specialist-skeptic";
  if (lower.includes("synthesis")) return "specialist-synthesis";
  if (lower.includes("ranking")) return "specialist-ranking";
  if (lower.includes("advisor")) return "specialist-advisor";
  return "commander-root";
}

function resolveTargetEntity(eventType: string, sourceEntity: string, region?: string): string | undefined {
  if (eventType === "SCOUT_DEPLOYED" && region) {
    return `scout-${region.toLowerCase()}`;
  }
  if (eventType === "SCOUT_COMPLETE" || eventType === "CANDIDATE_EXTRACTED") {
    return "commander-root";
  }
  if (eventType.includes("SKEPTIC")) {
    return "specialist-verification";
  }
  if (eventType.includes("RANKING")) {
    return "primary-opportunity";
  }
  return undefined;
}

function getCameraModeForEvent(eventType: string, region?: string): "global" | "regional" | "entity" | "cinema" {
  if (eventType === "MISSION_INITIATED" || eventType === "MISSION_COMPLETE") return "cinema";
  if (region) return "regional";
  if (eventType.includes("RANKING") || eventType.includes("DOSSIER")) return "entity";
  return "global";
}

function resolveFocusTarget(eventType: string, region?: string, sourceEntity?: string): string | undefined {
  if (region) return region;
  if (eventType.includes("ELIGIBILITY")) return "Eligibility Investigator";
  if (eventType.includes("COST")) return "True Cost Analyzer";
  if (eventType.includes("DEADLINE")) return "Deadline Intelligence";
  if (eventType.includes("SKEPTIC")) return "Adversarial Skeptic";
  if (eventType.includes("RANKING")) return "Ranking Engine";
  return sourceEntity;
}

// Strip any accidental sensitive tokens (§72)
function sanitizePayload(payload: Record<string, any>): Record<string, any> {
  const sanitized = { ...payload };
  delete sanitized.api_key;
  delete sanitized.secret;
  delete sanitized.token;
  delete sanitized.authorization;
  delete sanitized.password;
  return sanitized;
}
