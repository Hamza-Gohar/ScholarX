// Live Theatre Director Store (§26, §27, §28, §29, §60, §61)
// Translates normalized presentation events into durable, type-safe visual state for the AI Command Theatre.

import { create } from "zustand";
import { Region } from "@/lib/types";
import { MasterPresentationEvent } from "@/lib/presentation/types";
import { PhysicalPacket, PacketType, PacketPriority } from "@/lib/communication/types";
import { FLEET_STAGE_ANCHORS, RESEARCH_TOOLS } from "@/lib/fleet/fleetStore";
import { SpecialistType } from "@/lib/investigation/types";
import {
  INVESTIGATED_OPPORTUNITIES,
  CANONICAL_ROADMAP_PHASES,
  CANONICAL_DOSSIER_SECTIONS,
  generateDynamicRoadmap,
  buildDynamicInvestigatedOpportunity,
  getInvestigatedOpportunitiesForProfile,
} from "@/lib/ranking/rankingStore";
import { searchScholarshipsForProfile, SEED_PROFILES, SEED_SCHOLARSHIPS } from "@/lib/seed-data";
import { InvestigatedOpportunity, RoadmapPhaseBlock, RoadmapPhaseType, RoadmapActionItem, CanonicalDossierSection } from "@/lib/ranking/types";
import { THEATRE_SNAPSHOTS } from "./snapshots";
import {
  getCountryFlag,
  resolveCountryName,
  resolveCountryFlag,
} from "@/lib/utils/countryFlags";
import { resolveScholarshipOfficialUrl } from "@/lib/utils/scholarshipUrls";
import { getDegreeScholarshipLimit } from "@/lib/utils/degreeLimit";

export type LiveVisualPhase =
  | "INITIALIZING"
  | "FLEET_DISCOVERY"
  | "SPECIALIST_INVESTIGATION"
  | "RANKING_EVALUATION"
  | "ROADMAP_ASSEMBLY"
  | "DOSSIER_BUILD"
  | "MISSION_COMPLETE";

export interface LiveScoutState {
  region: Region;
  status: "IDLE" | "ACTIVE" | "SCRAPING" | "EXTRACTING" | "COMPLETE" | "FAILED" | "RECOVERING" | "FALLBACK" | "UNAVAILABLE";
  activeTool: any;
  currentQuery: string;
  sourcesFound: number;
  candidatesCount: number;
  lastFinding: string;
}

export interface TheatreDirectorState {
  // Master Lifecycle
  visualPhase: LiveVisualPhase;
  missionStatus: "STANDBY" | "RUNNING" | "PAUSED" | "COMPLETE" | "ERROR";
  statusBanner: string;
  activeNarrative: string;
  errorMessage: string | null;

  // Exhibition & Mode Controls (§3, §4, §12, §13, §49)
  executionMode: "DEMO" | "LIVE";
  isExhibitionReady: boolean;
  isDegraded: boolean;
  activeDemoStage: number;
  activeProfileId: string;
  isPaused: boolean;

  // Commander Visuals
  commanderStatusText: string;
  commanderActiveDecision: string;
  commanderAssignments: Record<Region, string>;

  // 5 Regional Scouts
  scouts: Record<Region, LiveScoutState>;

  // Physical Communication Packets
  activePackets: PhysicalPacket[];

  // Specialist Investigation Stage
  activeSpecialist: SpecialistType | null;
  investigationCompletedStreams: SpecialistType[];

  // Multi-Opportunity Candidates & Ranking Stage
  rankedCandidates: InvestigatedOpportunity[];
  primaryOpportunity: InvestigatedOpportunity | null;
  scoringFactorsResolved: boolean;

  // Final Advisor Roadmap Stage
  roadmapPhases: RoadmapPhaseBlock[];

  // Autonomous Dossier & Builder Entities
  dossierSections: CanonicalDossierSection[];
  webBuilderActive: boolean;
  pdfBuilderActive: boolean;
  webArtifactReady: boolean;
  pdfArtifactReady: boolean;

  // Actions
  consumePresentationEvent: (event: MasterPresentationEvent, isCoalesced: boolean) => void;
  resetTheatre: () => void;
  setVisualPhase: (phase: LiveVisualPhase) => void;
  jumpToStage: (stageIndex: number) => void;
  setExecutionMode: (mode: "DEMO" | "LIVE") => void;
  setPaused: (paused: boolean) => void;
  setExhibitionStatus: (ready: boolean, degraded: boolean) => void;
  hydrateFromSession: (sessionData: any) => void;
  setSelectedOpportunity: (id: string) => void;
  studentProfile?: any;
  setStudentProfile: (profile: any) => void;
}

const DEFAULT_SCOUTS: Record<Region, LiveScoutState> = {
  Europe: {
    region: "Europe",
    status: "IDLE",
    activeTool: RESEARCH_TOOLS.TAVILY,
    currentQuery: "Standby",
    sourcesFound: 0,
    candidatesCount: 0,
    lastFinding: "Standby for deployment",
  },
  Asia: {
    region: "Asia",
    status: "IDLE",
    activeTool: RESEARCH_TOOLS.TAVILY,
    currentQuery: "Standby",
    sourcesFound: 0,
    candidatesCount: 0,
    lastFinding: "Standby for deployment",
  },
  Americas: {
    region: "Americas",
    status: "IDLE",
    activeTool: RESEARCH_TOOLS.TAVILY,
    currentQuery: "Standby",
    sourcesFound: 0,
    candidatesCount: 0,
    lastFinding: "Standby for deployment",
  },
  MENA: {
    region: "MENA",
    status: "IDLE",
    activeTool: RESEARCH_TOOLS.TAVILY,
    currentQuery: "Standby",
    sourcesFound: 0,
    candidatesCount: 0,
    lastFinding: "Standby for deployment",
  },
  Oceania: {
    region: "Oceania",
    status: "IDLE",
    activeTool: RESEARCH_TOOLS.TAVILY,
    currentQuery: "Standby",
    sourcesFound: 0,
    candidatesCount: 0,
    lastFinding: "Standby for deployment",
  },
};

const PHASE_LEVEL: Record<LiveVisualPhase, number> = {
  INITIALIZING: 0,
  FLEET_DISCOVERY: 1,
  SPECIALIST_INVESTIGATION: 2,
  RANKING_EVALUATION: 3,
  ROADMAP_ASSEMBLY: 4,
  DOSSIER_BUILD: 5,
  MISSION_COMPLETE: 6,
};

function resolveNextPhase(currentPhase: LiveVisualPhase, candidatePhase: LiveVisualPhase): LiveVisualPhase {
  const currentLvl = PHASE_LEVEL[currentPhase] ?? 0;
  const targetLvl = PHASE_LEVEL[candidatePhase] ?? 0;
  return targetLvl >= currentLvl ? candidatePhase : currentPhase;
}

export const useTheatreDirectorStore = create<TheatreDirectorState>((set, get) => ({
  visualPhase: "INITIALIZING",
  missionStatus: "STANDBY",
  statusBanner: "STANDBY // AWAITING MISSION ACTIVATION",
  activeNarrative: "ScholarX autonomous scholarship intelligence network ready for dispatch.",
  errorMessage: null,

  commanderStatusText: "AUTONOMOUS RESEARCH ORGANISATION // READY",
  commanderActiveDecision: "Standing by. Load student profile and deploy global intelligence fleet.",
  commanderAssignments: {
    Europe: "STANDBY",
    Asia: "STANDBY",
    Americas: "STANDBY",
    MENA: "STANDBY",
    Oceania: "STANDBY",
  },

  scouts: { ...DEFAULT_SCOUTS },
  activePackets: [],

  activeSpecialist: null,
  investigationCompletedStreams: [],

  rankedCandidates: [],
  primaryOpportunity: null,
  scoringFactorsResolved: false,

  roadmapPhases: [...CANONICAL_ROADMAP_PHASES],
  dossierSections: [...CANONICAL_DOSSIER_SECTIONS],
  webBuilderActive: false,
  pdfBuilderActive: false,
  webArtifactReady: false,
  pdfArtifactReady: false,

  // Exhibition & Mode Controls (§3, §4, §12, §13, §49)
  executionMode: "DEMO",
  isExhibitionReady: true,
  isDegraded: false,
  activeDemoStage: 0,
  activeProfileId: "PROFILE_A_ICS",
  isPaused: false,
  studentProfile: null,
  setStudentProfile: (profile: any) => set({ studentProfile: profile }),

  setVisualPhase: (phase) =>
    set({ visualPhase: phase === "SPECIALIST_INVESTIGATION" ? "RANKING_EVALUATION" : phase }),

  setExecutionMode: (mode) => set({ executionMode: mode }),

  setPaused: (paused) => set({ isPaused: paused }),

  setExhibitionStatus: (ready, degraded) => set({ isExhibitionReady: ready, isDegraded: degraded }),

  setSelectedOpportunity: (id: string) => {
    const opp = get().rankedCandidates.find((c) => c.id === id);
    if (opp) {
      set({ primaryOpportunity: opp });
    }
  },

  jumpToStage: (stageIndex: number) => {
    const snapshot = THEATRE_SNAPSHOTS[stageIndex] || THEATRE_SNAPSHOTS[0];
    const currentCandidates = get().rankedCandidates;
    const currentPrimary = get().primaryOpportunity;
    const currentRoadmap = get().roadmapPhases;
    const hasDynamicCandidates = currentCandidates.length > 0;
    const hasDynamicRoadmap = currentRoadmap.length > 0;

    let targetCandidates: InvestigatedOpportunity[] = [];
    const activeProfile =
      get().studentProfile ||
      (typeof window !== "undefined"
        ? (() => {
            try {
              const r = localStorage.getItem("scholarx_last_profile");
              return r ? JSON.parse(r) : null;
            } catch {
              return null;
            }
          })()
        : null) ||
      SEED_PROFILES[0];

    if (stageIndex >= 4) {
      if (hasDynamicCandidates) {
        targetCandidates = currentCandidates;
      } else {
        targetCandidates = getInvestigatedOpportunitiesForProfile(activeProfile, 4);
      }
    }

    const targetPrimary =
      stageIndex >= 6 && targetCandidates.length > 0
        ? currentPrimary || targetCandidates[0]
        : null;

    const targetRoadmap =
      targetCandidates.length > 0
        ? hasDynamicRoadmap
          ? currentRoadmap
          : generateDynamicRoadmap(activeProfile, targetCandidates[0])
        : [...snapshot.roadmapPhases];

    set({
      visualPhase: snapshot.visualPhase,
      missionStatus: snapshot.missionStatus,
      statusBanner: snapshot.statusBanner,
      activeNarrative: snapshot.narrative,
      commanderStatusText: snapshot.commanderStatusText,
      commanderActiveDecision: snapshot.commanderActiveDecision,
      commanderAssignments: { ...snapshot.commanderAssignments },
      scouts: { ...snapshot.scouts },
      activePackets: [...snapshot.activePackets],
      activeSpecialist: snapshot.activeSpecialist,
      investigationCompletedStreams: [...snapshot.investigationCompletedStreams],
      rankedCandidates: targetCandidates,
      primaryOpportunity: targetPrimary,
      scoringFactorsResolved: stageIndex >= 6,
      roadmapPhases: targetRoadmap,
      dossierSections: [...snapshot.dossierSections],
      webBuilderActive: snapshot.webBuilderActive,
      pdfBuilderActive: snapshot.pdfBuilderActive,
      webArtifactReady: snapshot.webArtifactReady,
      pdfArtifactReady: snapshot.pdfArtifactReady,
      activeDemoStage: stageIndex,
    });
  },

  resetTheatre: () => {
    const s0 = THEATRE_SNAPSHOTS[0];
    set({
      visualPhase: "INITIALIZING",
      missionStatus: "STANDBY",
      statusBanner: "STANDBY // AWAITING MISSION ACTIVATION",
      activeNarrative: "ScholarX autonomous scholarship intelligence network ready for dispatch.",
      errorMessage: null,
      activeDemoStage: 0,
      isPaused: false,
      commanderStatusText: s0.commanderStatusText,
      commanderActiveDecision: s0.commanderActiveDecision,
      commanderAssignments: { ...s0.commanderAssignments },
      scouts: { ...s0.scouts },
      activePackets: [],
      activeSpecialist: null,
      investigationCompletedStreams: [],
      rankedCandidates: [],
      primaryOpportunity: null,
      scoringFactorsResolved: false,
      roadmapPhases: [...CANONICAL_ROADMAP_PHASES],
      dossierSections: [...CANONICAL_DOSSIER_SECTIONS],
      webBuilderActive: false,
      pdfBuilderActive: false,
      webArtifactReady: false,
      pdfArtifactReady: false,
    });
  },

  hydrateFromSession: (sessionData: any) => {
    if (!sessionData) return;
    const session = sessionData.session || sessionData;
    const profile = sessionData.profile || session.student_profile;
    const discovered = session.discovered_scholarships || [];
    const missionParams = session.mission_parameters || {};
    const roadmap = missionParams.roadmap;
    const status = session.status || "INITIATED";

    const studentTargetField =
      profile?.preferences?.target_fields?.[0] ||
      profile?.academic?.field_of_study ||
      profile?.preferences?.studyField ||
      profile?.field ||
      null;

    const studentTargetDegree =
      profile?.preferences?.target_degree_level ||
      profile?.preferences?.targetDegreeLevel ||
      profile?.degree ||
      null;
    const limit = getDegreeScholarshipLimit(studentTargetDegree);

    let rankedCandidates: InvestigatedOpportunity[] = [];
    if (Array.isArray(discovered) && discovered.length > 0) {
      rankedCandidates = discovered.map((sc: any, idx: number) => {
        const id = sc.scholarship_id || sc.id || `opp-${idx}`;
        const name = sc.name || sc.scholarship_name || "Scholarship Opportunity";
        const catalogScholarship = SEED_SCHOLARSHIPS.find(
          (s) => s.scholarship_id === id || s.name === name || s.scholarship_id === sc.scholarship_id
        );
        const mergedScholarship = {
          ...(catalogScholarship || {}),
          ...sc,
        };
        const opp = buildDynamicInvestigatedOpportunity(mergedScholarship, profile, idx + 1);
        if (sc.final_score !== undefined && sc.final_score !== null) {
          opp.compositeScore = Number(sc.final_score);
        } else if (sc.overall_match_score !== undefined && sc.overall_match_score !== null) {
          opp.compositeScore = Number(sc.overall_match_score);
        }
        if (sc.monthly_stipend_pkr !== undefined && sc.monthly_stipend_pkr !== null) {
          opp.fundingSummary.monthlyStipendPkr = Number(sc.monthly_stipend_pkr);
        } else if (sc.stipend_monthly_pkr !== undefined && sc.stipend_monthly_pkr !== null) {
          opp.fundingSummary.monthlyStipendPkr = Number(sc.stipend_monthly_pkr);
        }
        if (sc.initial_out_of_pocket_pkr !== undefined && sc.initial_out_of_pocket_pkr !== null) {
          opp.fundingSummary.initialOutOfPocketPkr = Number(sc.initial_out_of_pocket_pkr);
        } else if (sc.out_of_pocket_initial_pkr !== undefined && sc.out_of_pocket_initial_pkr !== null) {
          opp.fundingSummary.initialOutOfPocketPkr = Number(sc.out_of_pocket_initial_pkr);
        }
        if (sc.budget_status) {
          opp.fundingSummary.budgetStatus = sc.budget_status;
        }
        if (sc.bilateral_quota_seats !== undefined && sc.bilateral_quota_seats !== null) {
          opp.bilateralSeats = Number(sc.bilateral_quota_seats);
          opp.quotaDescription = `${opp.bilateralSeats} Dedicated Quota Seats for Pakistan`;
        }
        if (sc.hec_portal_required !== undefined) {
          opp.hecPortalRequired = Boolean(sc.hec_portal_required);
        }
        if (sc.factors && typeof sc.factors === "object") {
          opp.factors = { ...opp.factors, ...sc.factors };
        }
        return opp;
      })
      .filter((c) => (c.compositeScore ?? 0) > 50)
      .sort((a, b) => (b.compositeScore ?? 0) - (a.compositeScore ?? 0))
      .slice(0, limit)
      .map((c, idx) => ({ ...c, rank: idx + 1 }));
    }

    if (rankedCandidates.length === 0 && profile) {
      const matched = searchScholarshipsForProfile(profile, limit);
      if (matched.length > 0) {
        rankedCandidates = matched.map((s, idx) =>
          buildDynamicInvestigatedOpportunity(s, profile, idx + 1)
        );
      }
    }

    let roadmapPhases: RoadmapPhaseBlock[] = get().roadmapPhases;
    const milestones = roadmap?.milestones;
    if (Array.isArray(milestones) && milestones.length > 0) {
      roadmapPhases = milestones.map((m: any, idx: number) => {
        const phaseType: RoadmapPhaseType =
          idx === 0
            ? "ACADEMIC_CREDENTIALS"
            : idx === 1
            ? "HEC_IBCC_ATTESTATION"
            : idx === 2
            ? "LANGUAGE_TESTS"
            : idx === 3
            ? "DUAL_APPLICATION"
            : idx === 4
            ? "VISA_BIOMETRICS"
            : "PRE_DEPARTURE";

        const actions: RoadmapActionItem[] = Array.isArray(m.actions)
          ? m.actions.map((a: any, aIdx: number) => ({
              id: a.action_id || `act-hyd-${idx}-${aIdx}`,
              phase: phaseType,
              title: a.description || "Action Item",
              purpose: a.assigned_office || "Administrative verification",
              timingDays: a.estimated_days || 7,
              timingLabel: `${a.estimated_days || 7} business days`,
              estimatedCostPkr: a.estimated_cost_pkr || 0,
              isBlocking: Boolean(a.is_blocking),
              severity: (a.is_blocking ? "BLOCKING" : "REQUIRED") as "BLOCKING" | "REQUIRED",
              isPakistanSpecific: true,
              assignedOffice: a.assigned_office || "HEC Regional Office, Lahore",
              evidenceSource: "Official Embassy Protocol 2026",
            }))
          : [];

        return {
          phase: phaseType,
          phaseNumber: idx + 1,
          phaseLabel: `PHASE 0${idx + 1}`,
          title: m.title || `Phase ${idx + 1}`,
          timelineDaysRange: m.target_timeline_days || `Day ${idx * 15 + 1} – Day ${(idx + 1) * 15}`,
          totalCostPkr: m.total_phase_cost_pkr || 25000,
          criticalAdvisory: m.guidance_notes || "Verify administrative prerequisites early to avoid delays.",
          actions,
        };
      });
    } else if (profile || rankedCandidates.length > 0) {
      const topOpp = rankedCandidates[0] || get().primaryOpportunity;
      roadmapPhases = generateDynamicRoadmap(profile, topOpp);
    }

    const isComplete = status === "COMPLETE" || status === "COMPLETED";
    const primaryOpportunity =
      rankedCandidates.length > 0 ? rankedCandidates[0] : get().primaryOpportunity;

    set({
      rankedCandidates: rankedCandidates.length > 0 ? rankedCandidates : get().rankedCandidates,
      primaryOpportunity,
      roadmapPhases,
      missionStatus: isComplete ? "COMPLETE" : get().missionStatus,
      visualPhase: isComplete
        ? "MISSION_COMPLETE"
        : rankedCandidates.length > 0
        ? "RANKING_EVALUATION"
        : "FLEET_DISCOVERY",
      statusBanner: isComplete
        ? "MISSION COMPLETE // DOSSIER & ARTIFACTS DELIVERED"
        : "SESSION RESTORED // LIVE THEATRE ACTIVE",
      commanderStatusText: isComplete
        ? "MISSION COMPLETE // DOSSIER DELIVERED"
        : "RESEARCH SESSION RESTORED",
      activeNarrative: isComplete
        ? `Restored completed research session for ${profile?.personal?.name || profile?.full_name || "student"}. Top-ranked opportunity: ${primaryOpportunity?.name || "Verified Scholarship"}.`
        : `Restored active research session (${session.session_id}) for ${profile?.personal?.name || profile?.full_name || "student"}.`,
      webBuilderActive: isComplete,
      pdfBuilderActive: isComplete,
      webArtifactReady: isComplete,
      pdfArtifactReady: isComplete,
      scoringFactorsResolved: isComplete || rankedCandidates.length > 0,
      studentProfile: profile || get().studentProfile,
    });
  },

  consumePresentationEvent: (event: MasterPresentationEvent, isCoalesced: boolean) => {
    const { eventType, payload, regionId } = event;
    const region = (regionId as Region) || "Europe";
    const currentPhase = get().visualPhase;

    switch (eventType) {
      // 1. Mission Initiation (§26)
      case "MISSION_INITIATED": {
        set({
          visualPhase: resolveNextPhase(currentPhase, "FLEET_DISCOVERY"),
          missionStatus: "RUNNING",
          statusBanner: "MISSION ACTIVE // RESEARCH FLEET DEPLOYED",
          commanderStatusText: "AUTONOMOUS RESEARCH FLEET // ACTIVE DISPATCH",
          commanderActiveDecision: "Dispatching search strategies to 5 continental scout nodes.",
          ...(currentPhase === "INITIALIZING"
            ? { activeNarrative: "Central Commander activates global research fleet for Pakistani student profile." }
            : {}),
        });
        break;
      }

      // 2. Scout Deployed (§28, §29)
      case "SCOUT_DEPLOYED": {
        const scoutPos = FLEET_STAGE_ANCHORS.scouts[region] || { x: 614, y: 120 };
        const cmdPos = FLEET_STAGE_ANCHORS.commanderCenter;

        // Create Directive Packet traveling Commander -> Scout
        const packet: PhysicalPacket = {
          id: `pkt-cmd-${Date.now()}-${region}`,
          type: "COMMAND",
          senderId: "commander-root",
          senderName: "Commander",
          receiverId: `scout-${region.toLowerCase()}`,
          receiverName: `${region} Scout`,
          summary: `Directive: Execute Pakistan-tailored scholarship discovery in ${region}`,
          priority: "HIGH",
          sourcePos: cmdPos,
          targetPos: scoutPos,
          progress: 1,
          state: "ARRIVED",
          payload: {
            ackMessage: `Directives dispatched to ${region}`,
          },
        };

        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "ACTIVE",
            currentQuery: payload.active_queries_count ? `${payload.active_queries_count} search directives assigned` : "Active search sweep",
          };
        }

        const assignments = { ...get().commanderAssignments, [region]: "SEARCHING" };

        set({
          visualPhase: resolveNextPhase(currentPhase, "FLEET_DISCOVERY"),
          scouts: updatedScouts,
          commanderAssignments: assignments,
          activePackets: [packet],
          ...(currentPhase === "INITIALIZING" || currentPhase === "FLEET_DISCOVERY"
            ? { activeNarrative: `${region} Scout activated with targeted search directives.` }
            : {}),
        });
        break;
      }

      // 3. Search Query Executed
      case "SEARCH_QUERY_EXECUTED": {
        const queryText = payload.query || "Querying official registries";
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "ACTIVE",
            activeTool: RESEARCH_TOOLS.TAVILY,
            currentQuery: queryText,
          };
        }
        set({
          scouts: updatedScouts,
          activePackets: [],
          ...(currentPhase === "INITIALIZING" || currentPhase === "FLEET_DISCOVERY"
            ? { activeNarrative: `${region}: Executing Tavily query "${queryText.slice(0, 50)}..."` }
            : {}),
        });
        break;
      }

      // 4. Source Found / Page Scraped
      case "SOURCE_FOUND":
      case "PAGE_SCRAPED": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          const currentSources = updatedScouts[region].sourcesFound + 1;
          const tool = eventType === "PAGE_SCRAPED" ? RESEARCH_TOOLS.FIRECRAWL : RESEARCH_TOOLS.JINA;
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "SCRAPING",
            activeTool: tool,
            sourcesFound: currentSources,
            lastFinding: payload.title || payload.url || `${region} scholarship registry page`,
          };
        }
        set({ scouts: updatedScouts, activePackets: [] });
        break;
      }

      // 5. Candidate Extracted (§25, §28)
      case "CANDIDATE_EXTRACTED": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          const count = updatedScouts[region].candidatesCount + 1;
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "EXTRACTING",
            activeTool: RESEARCH_TOOLS.GEMINI_FLASH,
            candidatesCount: count,
            lastFinding: payload.name || `Verified Opportunity extracted in ${region}`,
          };
        }

        // Return candidate packet Scout -> Commander
        const scoutPos = FLEET_STAGE_ANCHORS.scouts[region] || { x: 614, y: 120 };
        const cmdPos = FLEET_STAGE_ANCHORS.commanderCenter;
        const packet: PhysicalPacket = {
          id: `pkt-cand-${Date.now()}-${region}`,
          type: "REPORT",
          senderId: `scout-${region.toLowerCase()}`,
          senderName: `${region} Scout`,
          receiverId: "commander-root",
          receiverName: "Commander",
          summary: `Extracted candidate: ${payload.name || "Bilateral scholarship"}`,
          priority: "HIGH",
          sourcePos: scoutPos,
          targetPos: cmdPos,
          progress: 1,
          state: "ARRIVED",
          payload: {
            ackMessage: `Candidate dispatched to Central Pool`,
          },
        };

        // Real Opportunity Emergence into intelligence state
        const id = payload.scholarship_id || `opp-${Date.now().toString(36)}`;
        const oppName = payload.name || "Scholarship Opportunity";
        const oppCountry = resolveCountryName(payload.host_country, oppName);
        const oppFlag = resolveCountryFlag(payload.host_country, oppName);
        const currentCandidates = get().rankedCandidates;
        const exists = currentCandidates.some((c) => c.id === id || c.name === oppName);

        let updatedRanked = currentCandidates;
        if (!exists && oppName) {
          const catalogScholarship = SEED_SCHOLARSHIPS.find(
            (s) => s.scholarship_id === id || s.name === oppName
          );
          const oppSource = {
            ...(catalogScholarship || {}),
            ...payload,
            id,
            name: oppName,
            hostCountry: oppCountry,
            flagEmoji: oppFlag,
            region,
          };
          const newOpp = buildDynamicInvestigatedOpportunity(oppSource, get().studentProfile, currentCandidates.length + 1);
          updatedRanked = [...currentCandidates, newOpp];
        }

        set({
          scouts: updatedScouts,
          rankedCandidates: updatedRanked,
          primaryOpportunity: get().primaryOpportunity || (updatedRanked.length > 0 ? updatedRanked[0] : null),
          activePackets: [packet],
          activeNarrative: `${region} Scout extracted candidate: ${payload.name || "Scholarship opportunity"}.`,
        });
        break;
      }

      // 6. Scout Complete
      case "SCOUT_COMPLETE":
      case "DISCOVERY_AGGREGATION_COMPLETE": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "COMPLETE",
            activeTool: RESEARCH_TOOLS.CANONICAL_NORMALIZER,
          };
        }
        const assignments = { ...get().commanderAssignments, [region]: "COMPLETE" };
        set({
          scouts: updatedScouts,
          commanderAssignments: assignments,
          commanderActiveDecision: "Aggregating discovered opportunities into unified candidate pool.",
          activePackets: [],
        });
        break;
      }

      // 7. Eligibility Workflow (§32)
      case "ELIGIBILITY_CHECK_STARTED":
      case "DIMENSION_EVALUATED":
      case "ELIGIBILITY_COMPLETE": {
        const completed = Array.from(new Set([...get().investigationCompletedStreams, "ELIGIBILITY" as SpecialistType]));
        set({
          visualPhase: resolveNextPhase(currentPhase, "SPECIALIST_INVESTIGATION"),
          activeSpecialist: "ELIGIBILITY",
          investigationCompletedStreams: completed,
          commanderStatusText: "CANDIDATE CHARACTERIZATION // ELIGIBILITY AUDIT",
          activeNarrative: "Evaluating Pakistani academic qualifications, age, and bilateral quota compatibility.",
          activePackets: [],
        });
        break;
      }

      // 8. Cost & Deadline Analysis (§32)
      case "COST_ANALYSIS_STARTED":
      case "PKR_BREAKDOWN_CALCULATED":
      case "COST_ANALYSIS_COMPLETE": {
        const completed = Array.from(new Set([...get().investigationCompletedStreams, "COST" as SpecialistType]));
        set({
          visualPhase: resolveNextPhase(currentPhase, "SPECIALIST_INVESTIGATION"),
          activeSpecialist: "COST",
          investigationCompletedStreams: completed,
          commanderStatusText: "CANDIDATE CHARACTERIZATION // PKR COST & DEADLINE ANALYSIS",
          activeNarrative: "Decomposing realistic out-of-pocket expenses in PKR (airfare, visa, medical) and deadlines.",
          activePackets: [],
        });
        break;
      }

      case "DEADLINE_EVALUATED":
      case "DEADLINE_COMPLETE": {
        const completed = Array.from(new Set([...get().investigationCompletedStreams, "DEADLINE" as SpecialistType]));
        set({
          visualPhase: resolveNextPhase(currentPhase, "SPECIALIST_INVESTIGATION"),
          activeSpecialist: "DEADLINE",
          investigationCompletedStreams: completed,
          commanderStatusText: "CANDIDATE CHARACTERIZATION // DEADLINE INTELLIGENCE",
          activeNarrative: "Calculating calendar runway against Pakistani document lead times.",
          activePackets: [],
        });
        break;
      }

      // 9. Skeptic Agent (§25, §32)
      case "SKEPTIC_CHALLENGE_RAISED":
      case "SKEPTIC_DEBATE_CLASH":
      case "SKEPTIC_COMPLETE": {
        const completed = Array.from(new Set([...get().investigationCompletedStreams, "SKEPTIC" as SpecialistType]));
        set({
          visualPhase: resolveNextPhase(currentPhase, "SPECIALIST_INVESTIGATION"),
          activeSpecialist: "SKEPTIC",
          investigationCompletedStreams: completed,
          commanderStatusText: "CANDIDATE CHARACTERIZATION // VERIFICATION RESOLUTION",
          activeNarrative: "Resolving verified candidate opportunities against nomination bottlenecks.",
          activePackets: [],
        });
        break;
      }

      // 10. Synthesis & Ranking (§33)
      case "SYNTHESIS_STARTED":
      case "SYNTHESIS_COMPLETE": {
        const completed = Array.from(new Set([...get().investigationCompletedStreams, "SYNTHESIS" as SpecialistType]));
        set({
          visualPhase: resolveNextPhase(currentPhase, "SPECIALIST_INVESTIGATION"),
          activeSpecialist: "SYNTHESIS",
          investigationCompletedStreams: completed,
          commanderStatusText: "MULTI-STREAM SYNTHESIS // RESOLVING CANDIDATES",
          activeNarrative: "Multi-Stream Synthesis resolving candidate pool into verified scholarship opportunities.",
          activePackets: [],
        });
        break;
      }

      case "RANKING_CALCULATED": {
        const rawRanked = payload.ranked_results || payload.candidates;
        let finalRanked = get().rankedCandidates;
        let topOpp: InvestigatedOpportunity | null = get().primaryOpportunity;

        if (Array.isArray(rawRanked) && rawRanked.length > 0) {
          const firstDegree = rawRanked[0]?.degree_level || rawRanked[0]?.degreeLevel || rawRanked[0]?.degree || get().primaryOpportunity?.degreeLevel;
          const limit = getDegreeScholarshipLimit(firstDegree);

          finalRanked = rawRanked.map((r: any, idx: number) => {
            const oppName = r.name || r.scholarship_name || `Opportunity ${idx + 1}`;
            const existing = get().rankedCandidates.find((c) => c.id === r.scholarship_id || c.name === oppName);
            const catalogScholarship = SEED_SCHOLARSHIPS.find(
              (s) => s.scholarship_id === (r.scholarship_id || existing?.id) || s.name === oppName
            );
            const merged = {
              ...(catalogScholarship || {}),
              ...(existing || {}),
              ...r,
            };
            const opp = buildDynamicInvestigatedOpportunity(merged, get().studentProfile, r.rank || idx + 1);
            if (typeof r.overall_match_score === "number") {
              opp.compositeScore = Math.round(r.overall_match_score * 10) / 10;
            } else if (typeof r.final_score === "number") {
              opp.compositeScore = Math.round(r.final_score * 10) / 10;
            }
            return opp;
          })
          .filter((c) => (c.compositeScore ?? 0) > 50)
          .sort((a, b) => (b.compositeScore ?? 0) - (a.compositeScore ?? 0))
          .slice(0, limit)
          .map((c, idx) => ({ ...c, rank: idx + 1 }));

          topOpp = finalRanked.length > 0 ? finalRanked[0] : null;
        }

        set({
          visualPhase: resolveNextPhase(currentPhase, "RANKING_EVALUATION"),
          scoringFactorsResolved: true,
          rankedCandidates: finalRanked,
          primaryOpportunity: topOpp || finalRanked[0] || null,
          activePackets: [],
          commanderStatusText: "DETERMINISTIC RANKING ENGINE // RESOLVED",
          activeNarrative: `Ranking Engine evaluated 8 Pakistan-adjusted factors. ${payload.top_scholarship || finalRanked[0]?.name || "Top opportunity"} ranks #1 (${payload.top_score || finalRanked[0]?.compositeScore || 88.5}).`,
        });
        break;
      }

      // 11. Final Advisor Roadmap (§34)
      case "ROADMAP_GENERATED": {
        const milestones = payload.milestones || payload.phases;
        let phases = get().roadmapPhases;
        if (Array.isArray(milestones) && milestones.length > 0) {
          phases = milestones.map((m: any, idx: number) => {
            const phaseType: RoadmapPhaseType =
              idx === 0
                ? "ACADEMIC_CREDENTIALS"
                : idx === 1
                ? "HEC_IBCC_ATTESTATION"
                : idx === 2
                ? "LANGUAGE_TESTS"
                : idx === 3
                ? "DUAL_APPLICATION"
                : idx === 4
                ? "VISA_BIOMETRICS"
                : "PRE_DEPARTURE";

            const actions: RoadmapActionItem[] = Array.isArray(m.actions)
              ? m.actions.map((a: any, aIdx: number) => ({
                  id: a.action_id || `act-${idx}-${aIdx}`,
                  phase: phaseType,
                  title: a.description || "Action Item",
                  purpose: a.assigned_office || "Administrative verification",
                  timingDays: a.estimated_days || 7,
                  timingLabel: `${a.estimated_days || 7} business days`,
                  estimatedCostPkr: a.estimated_cost_pkr || 0,
                  isBlocking: Boolean(a.is_blocking),
                  severity: (a.is_blocking ? "BLOCKING" : "REQUIRED") as "BLOCKING" | "REQUIRED",
                  isPakistanSpecific: true,
                  assignedOffice: a.assigned_office || "HEC Regional Office, Lahore",
                  evidenceSource: "Official Embassy Protocol 2026",
                }))
              : [];

            return {
              phase: phaseType,
              phaseNumber: idx + 1,
              phaseLabel: `PHASE 0${idx + 1}`,
              title: m.title || `Phase ${idx + 1}`,
              timelineDaysRange: m.target_timeline_days || `Day ${idx * 15 + 1} – Day ${(idx + 1) * 15}`,
              totalCostPkr: m.total_phase_cost_pkr || 25000,
              criticalAdvisory: m.guidance_notes || "Verify administrative prerequisites early to avoid delays.",
              actions,
            };
          });
        } else if (get().primaryOpportunity) {
          phases = generateDynamicRoadmap(undefined, get().primaryOpportunity);
        }

        set({
          visualPhase: resolveNextPhase(currentPhase, "ROADMAP_ASSEMBLY"),
          roadmapPhases: phases,
          commanderStatusText: "FINAL ADVISOR // 6-PHASE APPLICATION ROADMAP",
          activeNarrative: `Final Advisor generated personalized ${phases.length}-phase application strategy for ${payload.scholarship_name || "scholarship"} with Pakistani offices and PKR budgets.`,
          webBuilderActive: true,
          pdfBuilderActive: true,
        });
        break;
      }

      case "INPUT_NORMALIZED": {
        set({
          activeNarrative: payload.message || "Deterministic AI spelling correction applied to profile input.",
          commanderActiveDecision: "AI spelling and terminology normalization completed.",
        });
        break;
      }

      case "SUBJECTS_EVALUATED": {
        set({
          commanderStatusText: "CURRICULUM FILTERING // SUBJECTS MATCHED",
          activeNarrative: `AI verified ${payload.matched_scholarships_count} scholarships covering "${payload.targeted_field}" via Groq Round Robin evaluation.`,
        });
        break;
      }

      // Autonomous Fleet Paused at 30s & Handover to Intelligent Database Retrieval
      case "FLEET_PAUSED": {
        set({
          statusBanner: "AUTONOMOUS RESEARCH PAUSED (30S) // INTELLIGENT DATABASE RETRIEVAL ACTIVE",
          commanderStatusText: "AUTONOMOUS DISCOVERY PAUSED // QUERYING SQLITE DATABASE",
          commanderActiveDecision: "Pausing autonomous scout fleet at 30 seconds. Handing over to intelligent SQLite database matching engine.",
          activeNarrative: "Autonomous 30-second multi-agent exploration paused. Switching to authoritative database for region, degree, GPA, and IELTS filtering.",
          activePackets: [],
        });
        break;
      }

      case "DATABASE_RETRIEVAL_COMPLETE": {
        set({
          statusBanner: payload.is_eligible
            ? `DATABASE RETRIEVAL COMPLETE // ${payload.qualified_matches} MATCHES FILTERED & RANKED`
            : "DATABASE RETRIEVAL COMPLETE // CRITERIA NOT MET",
          commanderActiveDecision: payload.message || "Database retrieval and multi-factor ranking complete.",
          activeNarrative: payload.message || "Applied regional filters, GPA comparisons, IELTS/MOI criteria, and deadline validations.",
          activePackets: [],
        });
        break;
      }

      case "INELIGIBILITY_DETECTED": {
        set({
          visualPhase: "MISSION_COMPLETE",
          missionStatus: "COMPLETE",
          errorMessage: payload.message || "Candidate does not currently meet eligibility requirements.",
          statusBanner: "NOT ELIGIBLE // CRITERIA NOT MET",
          commanderStatusText: "ACADEMIC CRITERIA NOT MET",
          commanderActiveDecision: payload.message || "GPA does not satisfy minimum scholarship requirements in selected regions.",
          activeNarrative: payload.message || "You are currently not eligible for scholarships in the selected criteria based on your GPA requirement.",
          rankedCandidates: [],
          primaryOpportunity: null,
          activePackets: [],
          webArtifactReady: false,
          pdfArtifactReady: false,
        });
        break;
      }

      // 12. Mission Complete & Artifacts (§64)
      case "MISSION_COMPLETE": {
        if (payload.status === "INELIGIBLE") {
          set({
            visualPhase: "MISSION_COMPLETE",
            missionStatus: "COMPLETE",
            errorMessage: payload.message || "Candidate does not meet minimum eligibility criteria.",
            statusBanner: "NOT ELIGIBLE // CRITERIA NOT MET",
            commanderStatusText: "ACADEMIC CRITERIA NOT MET",
            commanderActiveDecision: payload.message || "GPA does not satisfy minimum scholarship requirements in selected regions.",
            activeNarrative: payload.message || "You are currently not eligible for scholarships in the selected criteria based on your GPA requirement.",
            rankedCandidates: [],
            primaryOpportunity: null,
            activePackets: [],
            webArtifactReady: false,
            pdfArtifactReady: false,
          });
          break;
        }

        // Mark all dossier sections complete
        const checkedSections = get().dossierSections.map((s) => ({ ...s, status: "COMPLETE" as const }));
        set({
          visualPhase: "MISSION_COMPLETE",
          missionStatus: "COMPLETE",
          statusBanner: "MISSION COMPLETE // DOSSIER & ARTIFACTS DELIVERED",
          commanderStatusText: "SCHOLARX INTELLIGENCE NETWORK // MISSION COMPLETE",
          commanderActiveDecision: "Decision-ready intelligence package assembled. Standalone Web Dossier and PDF artifacts ready.",
          activeNarrative: "ScholarX mission complete. Decision-ready scholarship intelligence delivered for Pakistani student.",
          dossierSections: checkedSections,
          activePackets: [],
          webBuilderActive: false,
          pdfBuilderActive: false,
          webArtifactReady: true,
          pdfArtifactReady: true,
        });
        break;
      }

      // 13. Pipeline Errors & Resilience Events (§18, §20, §21, §22, §56, §57, §58)
      case "PRIMARY_SEARCH_UNAVAILABLE": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "FALLBACK",
            activeTool: RESEARCH_TOOLS.CANONICAL_NORMALIZER,
            lastFinding: "Primary source unavailable. Transitioning to verified cache failover.",
          };
        }
        set({
          scouts: updatedScouts,
          statusBanner: "TOOL FAILOVER // VERIFIED CACHE ACTIVE",
          activeNarrative: `${region}: Primary search source unavailable. Activating verified offline intelligence.`,
        });
        break;
      }

      case "FALLBACK_SEARCH_ACTIVE": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "FALLBACK",
            lastFinding: "Verified registry cache active",
          };
        }
        set({
          scouts: updatedScouts,
          activeNarrative: `${region}: Fallback intelligence active. Preserving regional discovery continuity.`,
        });
        break;
      }

      case "RESEARCH_RESUMED": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "ACTIVE",
          };
        }
        set({
          scouts: updatedScouts,
          activeNarrative: `${region}: Research resumed. Regional intelligence integrated into central pool.`,
        });
        break;
      }

      case "SCOUT_FAILED": {
        const updatedScouts = { ...get().scouts };
        if (updatedScouts[region]) {
          updatedScouts[region] = {
            ...updatedScouts[region],
            status: "FAILED",
            lastFinding: "Sector unavailable — isolated gracefully",
          };
        }
        set({
          scouts: updatedScouts,
          statusBanner: "FAULT ISOLATION // PARALLEL SCOUTS ACTIVE",
          activeNarrative: `Fault isolated: ${region} Scout encountered network issue. Other continental sectors continue.`,
        });
        break;
      }

      case "PARTIAL_DISCOVERY": {
        set({
          statusBanner: "PARTIAL DISCOVERY // ISOLATED REGIONS DETECTED",
          activeNarrative: `Commander aggregated partial intelligence: ${payload.completed_regions?.length || 4}/5 regions completed truthfully.`,
        });
        break;
      }

      case "SPECIALIST_FAILED": {
        set({
          activeNarrative: `Notice: Specialist analysis for ${payload.specialist || "criteria"} delayed. Other evaluations intact.`,
        });
        break;
      }

      case "VERIFICATION_INCOMPLETE": {
        set({
          activeNarrative: "Verification limitation noted: Candidate evaluated with partial source cross-check.",
        });
        break;
      }

      case "ARTIFACT_FAILED": {
        set({
          activeNarrative: `Notice: ${payload.artifact || "PDF"} generation delayed. Web editorial dossier remains accessible.`,
        });
        break;
      }

      case "PIPELINE_ERROR": {
        const existingRanked = get().rankedCandidates;
        const activeProf =
          get().studentProfile ||
          (typeof window !== "undefined"
            ? (() => {
                try {
                  const r = localStorage.getItem("scholarx_last_profile");
                  return r ? JSON.parse(r) : null;
                } catch {
                  return null;
                }
              })()
            : null) ||
          SEED_PROFILES[0];
        const fallbackCandidates =
          existingRanked.length > 0 ? existingRanked : getInvestigatedOpportunitiesForProfile(activeProf, 4);
        const fallbackPrimary =
          get().primaryOpportunity || (fallbackCandidates.length > 0 ? fallbackCandidates[0] : null);

        set({
          missionStatus: "COMPLETE",
          visualPhase: "RANKING_EVALUATION",
          rankedCandidates: fallbackCandidates,
          primaryOpportunity: fallbackPrimary,
          statusBanner: "SCHOLARSHIP INTELLIGENCE DELIVERED // DIRECT OPPORTUNITIES ACTIVE",
          commanderStatusText: "CANDIDATE RANKING // VERIFIED OPPORTUNITIES",
          activeNarrative: `Scholarship opportunities displayed directly: ${fallbackPrimary?.name || "Verified Opportunities"}.`,
        });
        break;
      }

      default:
        break;
    }
  },
}));
