// Phase 6: Deep Opportunity Investigation Types (§8, §9, §10-§35, Agents.md)

export type SpecialistType =
  | "ELIGIBILITY"
  | "DOCUMENT"
  | "COST"
  | "DEADLINE"
  | "VERIFICATION"
  | "SKEPTIC"
  | "SYNTHESIS";

export type SpecialistCategory = "WORKFLOW" | "AGENT";

export type SpecialistState =
  | "IDLE"
  | "ACTIVE"
  | "ANALYZING"
  | "CROSS_CHECKING"
  | "CHALLENGING"
  | "RESOLVED"
  | "COMPLETED";

export type TargetKnowledgeState =
  | "UNINVESTIGATED"
  | "PROFILE_MATCHED"
  | "READINESS_KNOWN"
  | "COST_UNDERSTOOD"
  | "TIMELINE_ASSESSED"
  | "EVIDENCE_CONFIRMED"
  | "RISKS_CHALLENGED"
  | "INVESTIGATION_COMPLETE";

export interface InvestigationTarget {
  id: string;
  name: string;
  hostCountry: string;
  degreeLevel: string;
  fieldOfStudy: string;
  applicantContext: string;
  quotaSeats: number;
  fundingLabel: string;
  knowledgeState: TargetKnowledgeState;
  resolvedTraces: ResolvedTrace[];
}

export interface ResolvedTrace {
  id: string;
  specialist: SpecialistType;
  label: string;
  badge: string;
  color: string;
  summary: string;
  timestamp: number;
}

// 1. Eligibility Investigator (§10, §11)
export interface EligibilityCriterion {
  id: string;
  dimensionNumber: number;
  dimensionName: string;
  status: "PASS" | "CONDITIONAL" | "BONUS" | "FAIL";
  studentValue: string;
  requirementValue: string;
  detail: string;
  isPakistanSpecific: boolean;
}

export interface EligibilityResult {
  overallScore: number; // e.g. 87% (dimension match ratio, not a rank score)
  status: "MATCHED" | "CONDITIONAL";
  matchedCount: number;
  totalEvaluated: number;
  bilateralSeats: number;
  actionRequired: string;
  criteria: EligibilityCriterion[];
}

// 2. Document Analyst (§12, §13)
export interface DocumentReadinessItem {
  id: string;
  documentName: string;
  status: "READY" | "MISSING" | "PARTIAL" | "REQUIRED";
  quality?: "VERIFIED" | "GOOD" | "DRAFT" | "PENDING";
  pakistanLeadDays: number;
  estimatedCostPkr: number;
  isBlocking: boolean;
  notes: string;
}

export interface DocumentAnalysisResult {
  readinessScore: number; // 62%
  overallStatus: "PARTIAL" | "READY" | "BLOCKED";
  readyCount: number;
  totalRequired: number;
  criticalMissing: string[];
  totalPrepDays: number;
  totalPrepCostPkr: number;
  documents: DocumentReadinessItem[];
}

// 3. True Cost Analyzer (§14, §15)
export interface CostItem {
  id: string;
  phase: "BASE_FUNDING" | "PRE_APPLICATION" | "APPLICATION" | "VISA_TRAVEL" | "SETTLEMENT";
  category: string;
  item: string;
  amountPkr: number;
  amountDisplay: string;
  coverage: "COVERED" | "UNCOVERED" | "REQUIRED_RESERVE";
  notes: string;
}

export interface TrueCostResult {
  totalOutOfPocketPkr: number;
  totalOutOfPocketUsd: number;
  studentMaxBudgetPkr: number;
  budgetStatus: "EXCEEDS_BUDGET" | "WITHIN_BUDGET";
  shortfallPkr: number;
  breakdown: {
    baseFunding: CostItem[];
    preApplication: CostItem[];
    application: CostItem[];
    visaTravel: CostItem[];
    settlement: CostItem[];
  };
  keyRisks: string[];
}

// 4. Deadline Intelligence (§16, §17)
export interface DeadlineRunway {
  applicationDeadline: string;
  deadlineDisplay: string;
  daysRemaining: number;
  criticalPathDays: number;
  bufferDays: number;
  availableSlackDays: number;
  feasibility: "FEASIBLE" | "TIGHT" | "CRITICAL";
  leadTimeItems: {
    process: string;
    durationDays: number;
    pakistanOffice: string;
  }[];
}

// 5. Verification Agent & Evidence Objects (§20, §21, §22)
export interface EvidenceSource {
  id: string;
  name: string;
  domain: string;
  sourceType: "GOVERNMENT" | "HEC_PORTAL" | "UNIVERSITY";
  trustLevel: "AUTHORITATIVE" | "CONFIRMED";
  url: string;
}

export interface VerifiedClaim {
  id: string;
  claim: string;
  verdict: "CONFIRMED" | "PARTIALLY_VERIFIED" | "CONFLICT_RESOLVED";
  primarySource: EvidenceSource;
  secondarySource?: EvidenceSource;
  evidenceQuote: string;
  hasConflict?: boolean;
  conflictDetails?: {
    sourceA: string;
    claimA: string;
    sourceB: string;
    claimB: string;
    resolution: string;
  };
}

export interface VerificationResult {
  status: "VERIFIED" | "HEC_LISTED";
  confidenceScore: number;
  verifiedClaimsCount: number;
  sourcesCrossChecked: number;
  claims: VerifiedClaim[];
}

// 6. Skeptic Agent & Debate Sequence (§24, §25, §26, §28)
export interface SkepticChallenge {
  id: string;
  title: string;
  challengeText: string;
  category: "FINANCIAL_RISK" | "PROCEDURAL_BOTTLENECK" | "VISA_CONSTRAINT";
  evidenceRequested: string;
  evidenceResponse: string;
  status: "OPEN" | "EVIDENCE_REQUESTED" | "RESOLVED_QUALIFIED" | "ACCEPTED_RISK";
  impactSummary: string;
}

export interface SkepticResult {
  totalChallengesRaised: number;
  resolvedChallengesCount: number;
  criticalRisksFlagged: number;
  challenges: SkepticChallenge[];
}

// 7. Synthesis Workflow & Investigation Summary (§30, §31, §32)
export interface InvestigationSummary {
  scholarshipTitle: string;
  hostCountry: string;
  quotaSeats: number;
  overallEligibility: string;
  documentReadiness: string;
  realInitialOutlayPkr: number;
  deadlineFeasibility: string;
  verificationBadge: string;
  skepticStatus: string;
  criticalAdvisory: string;
  investigationCompletedAt: string;
}

// Phase 6 Step Progression (14 Discrete Operational Scenes)
export type Phase6Step =
  | "TARGET_SELECTION"        // 01: Stipendium Hungaricum isolated from Phase 5 discovery
  | "INVESTIGATION_INIT"      // 02: Commander dispatches deep investigation
  | "ELIGIBILITY_ACTIVE"      // 03: 15 Pakistan-aware dimensions evaluated sequentially
  | "ELIGIBILITY_DOCKED"      // 04: Eligibility result packet docked, trace recorded
  | "DOCUMENT_ACTIVE"         // 05: Document Analyst inspects transcript, gaps emerge
  | "DOCUMENT_DOCKED"         // 06: Document readiness packet docked, trace recorded
  | "COST_ACTIVE"             // 07: Real out-of-pocket costs calculated (PKR breakdown)
  | "COST_DOCKED"             // 08: Cost analysis packet docked, trace recorded
  | "DEADLINE_ACTIVE"         // 09: Runway timeline, prep vs slack calculated
  | "DEADLINE_DOCKED"         // 10: Deadline feasibility packet docked, trace recorded
  | "VERIFICATION_ACTIVE"     // 11: Official portals cross-checked, conflict resolved
  | "SKEPTIC_ACTIVE"          // 12: Skeptic raises adversarial challenges
  | "CHALLENGE_RESOLVED"      // 13: Evidence answers challenges, status qualified
  | "SYNTHESIS_COMPLETE";     // 14: Unified Investigation Summary emerges

export interface Phase6StepMeta {
  step: Phase6Step;
  index: number;
  label: string;
  narrative: string;
  durationMs: number;
  activeSpecialist: SpecialistType | null;
  cameraShot: "OPPORTUNITY_SELECTED" | "ELIGIBILITY_FOCUS" | "DOCUMENT_FOCUS" | "COST_FOCUS" | "DEADLINE_FOCUS" | "VERIFICATION_FOCUS" | "SKEPTIC_FOCUS" | "SYNTHESIS_FOCUS";
}

export interface Phase6Snapshot {
  step: Phase6Step;
  stepMeta: Phase6StepMeta;
  target: InvestigationTarget;
  activeSpecialist: SpecialistType | null;
  specialistMeta: {
    type: SpecialistType;
    category: SpecialistCategory;
    displayName: string;
    state: SpecialistState;
    actionLabel: string;
    color: string;
  } | null;
  // Specific data payloads
  eligibilityData: EligibilityResult;
  documentData: DocumentAnalysisResult;
  costData: TrueCostResult;
  deadlineData: DeadlineRunway;
  verificationData: VerificationResult;
  skepticData: SkepticResult;
  synthesisSummary: InvestigationSummary;
  // Communication
  activePackets: import("../communication/types").PhysicalPacket[];
  // Focus state
  focusedEntity: "TARGET" | "COMMANDER" | SpecialistType;
}
