// Master Presentation Architecture (§13, §19, Appendix E)
// Separates the raw backend event timing from human-comprehensible theatre presentation.

export type PresentationPriority = "HERO" | "SUPPORTING" | "BACKGROUND" | "AMBIENT";

export type PresentationLayer =
  | "BACKGROUND"
  | "ATMOSPHERE"
  | "WORLD"
  | "SECONDARY_OBJECTS"
  | "PRIMARY_OBJECTS"
  | "FOCUS"
  | "OVERLAY"
  | "SYSTEM";

export type SceneIntent =
  | "OVERVIEW"
  | "COMMAND"
  | "REGIONAL_DISCOVERY"
  | "RESEARCH"
  | "VERIFICATION"
  | "SKEPTIC_ARENA"
  | "RANKING"
  | "DOSSIER";

export interface PresentationDuration {
  minimumDisplayMs: number;
  holdAfterMs: number;
  coalesceKey?: string;
}

export interface MasterPresentationEvent {
  presentationEventId: string;
  missionId: string;
  timestamp: number;
  sourceEventId?: string;
  eventType: string;
  importance: PresentationPriority;
  phase: string;
  sourceEntityId: string;
  targetEntityId?: string;
  regionId?: string;
  scholarshipId?: string;
  payload: Record<string, any>;
  minimumDisplayMs: number;
  holdAfterMs: number;
  coalesceKey?: string;
  focusTarget?: string;
  cameraMode?: "global" | "regional" | "entity" | "cinema";
}

export interface PresentationQueueContract {
  enqueue: (event: MasterPresentationEvent) => void;
  setSpeed: (speed: number) => void;
  pause: () => void;
  resume: () => void;
  clear: () => void;
  getPendingCount: () => number;
}
