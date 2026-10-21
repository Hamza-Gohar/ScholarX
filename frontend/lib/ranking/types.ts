// Phase 7: Multi-Opportunity Ranking, Scoring Engine, Final Advisor & Dossier Types
// (§7, §8, §11, §14, §16-§32, Agents.md §4, §11)

import { PhysicalPacket } from "../communication/types";
import { Region } from "../types";

export type RankingFactorKey =
  | "ELIGIBILITY_MATCH"
  | "TRUE_FUNDING"
  | "PAKISTAN_BILATERAL"
  | "ACADEMIC_FIT"
  | "DOC_READINESS"
  | "DEADLINE_FEASIBILITY"
  | "VERIFICATION_CONFIDENCE"
  | "COMPETITION_ESTIMATE";

export interface ScoringFactor {
  key: RankingFactorKey;
  label: string;
  weightPercent: number; // e.g., 25 for 25%
  weightDecimal: number; // 0.25
  rawScore: number; // 0-100
  weightedContribution: number; // e.g., +23.0
  rationale: string;
  evidenceAnchor: string;
  status: "OPTIMAL" | "STRONG" | "ATTENTION" | "DEFICIT";
}

export interface InvestigatedOpportunity {
  id: string;
  name: string;
  shortName: string;
  hostCountry: string;
  flagEmoji: string;
  degreeLevel: string;
  fieldOfStudy: string;
  region: Region;
  quotaDescription: string;
  bilateralSeats: number | null;
  officialPortalUrl: string;
  hecPortalRequired: boolean;

  // 8 Pakistan-Adjusted Scoring Factors
  factors: Record<RankingFactorKey, ScoringFactor>;
  compositeScore: number; // Exact calculated score (0-100)
  rank: number; // 1, 2, 3, 4

  // Grounded Intelligence Summaries (Inherited from Phase 5 & 6)
  eligibilitySummary: {
    dimensionsMatched: number;
    totalDimensions: number;
    statusText: string;
    criticalRequirement: string;
  };
  fundingSummary: {
    coverageType: string;
    tuitionCovered: boolean;
    monthlyStipendPkr: number;
    initialOutOfPocketPkr: number;
    budgetStatus: "WITHIN_BUDGET" | "DEFICIT_WARNING";
  };
  readinessSummary: {
    scorePercent: number;
    prepDaysNeeded: number;
    criticalGaps: string[];
  };
  deadlineSummary: {
    applicationDeadline: string;
    daysRemaining: number;
    prepDaysNeeded: number;
    slackDays: number;
    feasibility: "FEASIBLE" | "TIGHT" | "CRITICAL";
  };
  verificationSummary: {
    confidencePercent: number;
    authoritativeSourcesCount: number;
    verifiedDomains: string[];
    conflictStatus: "NONE" | "RESOLVED_HEC_PRIMARY";
  };
  skepticSummary: {
    challengesRaised: number;
    resolvedCount: number;
    topFlag: string;
  };
}

// Final Advisor Personalized Roadmap Types
export type RoadmapPhaseType =
  | "ACADEMIC_CREDENTIALS"
  | "HEC_IBCC_ATTESTATION"
  | "LANGUAGE_TESTS"
  | "DUAL_APPLICATION"
  | "VISA_BIOMETRICS"
  | "PRE_DEPARTURE";

export interface RoadmapActionItem {
  id: string;
  phase: RoadmapPhaseType;
  title: string;
  purpose: string;
  timingDays: number;
  timingLabel: string;
  estimatedCostPkr: number;
  dependency?: string;
  isBlocking: boolean;
  severity: "BLOCKING" | "REQUIRED" | "RECOMMENDED";
  isPakistanSpecific: boolean;
  assignedOffice?: string;
  officeAddress?: string;
  officialPortalUrl?: string;
  evidenceSource?: string;
}

export interface RoadmapPhaseBlock {
  phase: RoadmapPhaseType;
  phaseNumber: number;
  phaseLabel: string;
  title: string;
  timelineDaysRange: string;
  totalCostPkr: number;
  actions: RoadmapActionItem[];
  criticalAdvisory: string;
}

// Canonical Dossier State (§21-§28)
export interface CanonicalDossierSection {
  id: string;
  title: string;
  status: "PENDING" | "ASSEMBLING" | "VERIFIED" | "COMPLETE";
  summary: string;
  evidenceSourcesCount: number;
}

export type DossierLifecycleState = "DRAFT" | "ASSEMBLING" | "COMPLETE";
export type ArtifactGenerationStatus = "PENDING" | "GENERATING" | "READY" | "ERROR";

export interface CanonicalDossier {
  scholarshipId: string;
  title: string;
  country: string;
  degreeLevel: string;
  field: string;
  generatedAt: string;
  version: string;
  executiveSummary: string;
  opportunity: InvestigatedOpportunity;
  candidateProfile?: any;
  rankedOpportunities?: InvestigatedOpportunity[];
  roadmapPhases: RoadmapPhaseBlock[];
  totalPrepDaysEstimated: number;
  totalBudgetNeededPkr: number;
  sections: CanonicalDossierSection[];
  state: DossierLifecycleState;
  webArtifactStatus: ArtifactGenerationStatus;
  pdfArtifactStatus: ArtifactGenerationStatus;
}

// Phase 7 Discrete Step Progression (12 Scenes)
export type Phase7Step =
  | "POOL_INSPECTION"       // 01: 4 investigated scholarships isolated from Phase 5/6
  | "SCORING_INIT"          // 02: Deterministic Ranking Engine activates
  | "FACTOR_EVALUATION"     // 03: 8 Pakistan-adjusted factors evaluated sequentially
  | "SCORE_RESOLUTION"      // 04: Transparent contribution points computed
  | "SPATIAL_COMPARISON"    // 05: Multi-opportunity spatial comparison resolves
  | "PRIMARY_SELECTION"     // 06: Stipendium Hungaricum emerges as PRIMARY OPPORTUNITY
  | "ADVISOR_ENGAGEMENT"    // 07: Final Advisor process activates
  | "ROADMAP_GENERATION"    // 08: 6-phase application journey synthesized
  | "DOSSIER_ASSEMBLY"      // 09: Dossier sections stream in and check off
  | "WEB_BUILDER_ACTIVE"    // 10: Web Artifact Builder composes standalone editorial page
  | "PDF_BUILDER_ACTIVE"    // 11: PDF Builder typesets paginated publication
  | "ARTIFACTS_DELIVERED";   // 12: Calm Mission Complete state with open/view triggers

export interface Phase7StepMeta {
  step: Phase7Step;
  index: number;
  label: string;
  narrative: string;
  durationMs: number;
  activeEntity: "COMMANDER" | "RANKING_ENGINE" | "FINAL_ADVISOR" | "DOSSIER_BUILDER" | "WEB_BUILDER" | "PDF_BUILDER";
  focusOpportunityId?: string;
}

export interface Phase7Snapshot {
  step: Phase7Step;
  stepMeta: Phase7StepMeta;
  opportunities: InvestigatedOpportunity[];
  primaryOpportunity: InvestigatedOpportunity;
  activeOpportunity: InvestigatedOpportunity;
  dossier: CanonicalDossier;
  activePackets: PhysicalPacket[];
  builderActivity?: {
    builderName: "WEB_BUILDER" | "PDF_BUILDER" | "DOSSIER_BUILDER";
    actionLabel: string;
    progressPercent: number;
  };
}
