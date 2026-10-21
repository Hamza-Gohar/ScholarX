// Communication Subsystem Types (§9, Appendix A.4, Agents.md)

export type PacketType =
  | "COMMAND"
  | "ACKNOWLEDGEMENT"
  | "REPORT"
  | "EVIDENCE"
  | "CHALLENGE"
  | "RESOLUTION";

export type PacketState = "FORMING" | "TRAVELING" | "ARRIVED" | "DOCKED";

export type PacketPriority = "CRITICAL" | "HIGH" | "NORMAL";

export interface DiscoveredSource {
  id: string;
  domain: string;
  title: string;
  sourceType: "PORTAL" | "GOVERNMENT" | "UNIVERSITY";
  verificationStatus: "VERIFIED" | "PENDING";
  quotaSeats?: number;
  country: string;
}

export interface ScholarshipCandidateSummary {
  id: string;
  title: string;
  country: string;
  degreeLevel: string;
  fundingType: "Fully Funded" | "Tuition + Stipend";
  tuitionCoverage: string;
  monthlyStipend: string;
  pakistanQuotaSeats?: number;
  hecAttestationRequired: boolean;
  confidenceScore: number;
}

export interface SectorReportSummary {
  sector: string;
  candidatesCount: number;
  highRelevanceCount: number;
  pakistanQuotaSeats: number;
  verificationNeeds: string[];
  keyFinding: string;
  candidates: ScholarshipCandidateSummary[];
}

export interface PhysicalPacket {
  id: string;
  type: PacketType;
  senderId: string;
  senderName: string;
  receiverId: string;
  receiverName: string;
  summary: string;
  priority: PacketPriority;
  sourcePos: { x: number; y: number };
  targetPos: { x: number; y: number };
  progress: number; // 0 to 1
  state: PacketState;
  payload?: {
    directive?: {
      objective: string;
      expectedOutput: string;
      constraints: string[];
    };
    ackMessage?: string;
    report?: SectorReportSummary;
  };
}

export type Phase4Step =
  | "DIRECTING"
  | "COMMAND_FLIGHT"
  | "SCOUT_RECEIVING"
  | "ACK_FLIGHT"
  | "SEARCHING"
  | "SOURCES_FOUND"
  | "CANDIDATE_EMERGENCE"
  | "REPORT_ASSEMBLY"
  | "REPORT_FLIGHT"
  | "COMMANDER_SYNTHESIS";

export interface Phase4StepMeta {
  step: Phase4Step;
  index: number;
  label: string;
  narrative: string;
  durationMs: number;
  cameraShot: "GLOBAL" | "DEPLOYMENT" | "REGIONAL";
  focusedRegion: "Europe" | "Pakistan" | null;
  focusedEntity: "COMMANDER" | "SCOUT" | null;
}
