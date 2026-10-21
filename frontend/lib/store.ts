import { create } from "zustand";
import { 
  StudentProfile, 
  Scholarship, 
  ScholarXEvent, 
  CompositeScoreResult, 
  ApplicationRoadmap, 
  Region,
  OverlayView,
  MapVisualMode,
  DataPacket,
  CommanderState,
  CommanderDecision,
  JudgeInterventionParams,
  AgentFocusTarget,
  PastSession,
  CandidateFlowItem
} from "./types";
import { SEED_PROFILES, SEED_SCHOLARSHIPS } from "./seed-data";
import { simulationEngine } from "./simulation-engine";
import { sound } from "./sound-fx";
import { launchDiscoveryMission, subscribeToEventStream, listSessions } from "./api";

export type MissionPhase = "IDLE" | "INTAKE" | "ORCHESTRATION" | "DISCOVERY" | "VERIFICATION" | "SYNTHESIS" | "MISSION_COMPLETE" | "ERROR";
export type MapMode = "2D_TACTICAL" | "3D_GLOBE";
export type DeckTab = "TELEMETRY" | "SKEPTIC" | "COSTS";

export interface ScoutStatus {
  region: Region;
  status: "IDLE" | "ACTIVE" | "SCRAPING" | "COMPLETE";
  currentQuery?: string;
  itemsFound: number;
  lastActivity: string;
}

export interface ScoreMutationRecord {
  scholarshipId: string;
  scholarshipName: string;
  prevScore: number;
  newScore: number;
  reason: string;
  timestamp: number;
}

interface CommandRoomState {
  // Session & Mission
  sessionId: string;
  missionStatus: "IDLE" | "RUNNING" | "PAUSED" | "COMPLETE" | "ERROR";
  missionPhase: MissionPhase;
  progressPercent: number;
  replaySpeed: number;
  missionElapsedTime: number;

  // Commander Visual Console
  commander: CommanderState;
  updateCommander: (update: Partial<CommanderState>) => void;
  addCommanderDecision: (decision: Omit<CommanderDecision, "id" | "timestamp">) => void;

  // Visible AI-to-AI Data Packets
  dataPackets: DataPacket[];
  pushDataPacket: (packet: Omit<DataPacket, "id" | "timestamp">) => void;
  clearOldPackets: () => void;

  // Student Profile
  studentProfile: StudentProfile;
  setStudentProfile: (profile: StudentProfile) => void;

  // UI Modes & Views
  overlayView: OverlayView;
  setOverlayView: (view: OverlayView) => void;
  mapMode: MapMode;
  setMapMode: (mode: MapMode) => void;
  mapVisualMode: MapVisualMode;
  setMapVisualMode: (mode: MapVisualMode) => void;
  scanlinesEnabled: boolean;
  setScanlinesEnabled: (enabled: boolean) => void;
  audioMuted: boolean;
  toggleAudio: () => boolean;

  // Deck Tabs & Focus Target
  activeDeckTab: DeckTab;
  setActiveDeckTab: (tab: DeckTab) => void;
  focusedAgent: AgentFocusTarget | null;
  setFocusedAgent: (target: AgentFocusTarget | null) => void;

  // Judge Live Intervention
  judgeParams: JudgeInterventionParams;
  setJudgeParams: (params: Partial<JudgeInterventionParams>) => void;
  redeployWithModifier: () => void;

  // Telemetry & Events
  events: ScholarXEvent[];
  addEvent: (event: ScholarXEvent) => void;
  clearEvents: () => void;

  // Scouts Status
  scouts: Record<Region, ScoutStatus>;
  updateScout: (region: Region, update: Partial<ScoutStatus>) => void;

  // Candidates & Results
  candidates: Scholarship[];
  selectedScholarship: Scholarship | null;
  setSelectedScholarship: (scholarship: Scholarship | null) => void;
  rankedResults: CompositeScoreResult[];
  roadmap: ApplicationRoadmap | null;
  scoreMutations: ScoreMutationRecord[];

  // Historical Sessions
  pastSessions: PastSession[];
  loadPastSessions: () => Promise<void>;

  // Backend Health & Live Stream
  backendConnected: boolean;
  backendChecking: boolean;
  checkBackendHealth: () => Promise<boolean>;
  sseUnsubscribe: (() => void) | null;

  // Mission Actions
  startMission: () => void;
  pauseMission: () => void;
  resetMission: () => void;
  setReplaySpeed: (speed: number) => void;

  // Candidate Stage Flow & Commander Directives
  activeCandidatesFlow: CandidateFlowItem[];
  addVisualMessage: (msg: any) => void;
  updateCommanderDirective: (directive: string) => void;
}

export const useCommandStore = create<CommandRoomState>((set, get) => ({
  sessionId: `sess-${Date.now().toString(36)}`,
  missionStatus: "IDLE",
  missionPhase: "IDLE",
  progressPercent: 0,
  replaySpeed: 2,
  missionElapsedTime: 0,

  commander: {
    missionGoal: "Autonomous multi-regional scholarship search for Pakistani candidates",
    activeDecision: "Standing by. Load profile and launch hunt to deploy regional fleet.",
    statusText: "STANDBY // READY FOR DISPATCH",
    activeAssignments: {
      Europe: "IDLE",
      Asia: "IDLE",
      Americas: "IDLE",
      MENA: "IDLE",
      Oceania: "IDLE",
    },
    recentDecisions: [],
  },
  updateCommander: (update) =>
    set((state) => ({ commander: { ...state.commander, ...update } })),
  addCommanderDecision: (decision) => {
    const newDec: CommanderDecision = {
      id: `dec-${Date.now().toString(36)}`,
      timestamp: new Date().toLocaleTimeString(),
      ...decision,
    };
    set((state) => ({
      commander: {
        ...state.commander,
        activeDecision: decision.decisionText,
        recentDecisions: [newDec, ...state.commander.recentDecisions].slice(0, 15),
      },
    }));
  },

  dataPackets: [],
  pushDataPacket: (packet) => {
    const id = `pkt-${Date.now().toString(36)}-${Math.random().toString(36).substring(2, 6)}`;
    const newPacket: DataPacket = {
      id,
      timestamp: Date.now(),
      ...packet,
    };
    set((state) => ({
      dataPackets: [...state.dataPackets, newPacket].slice(-10),
    }));

    sound.playTelemetryTick();

    setTimeout(() => {
      set((state) => ({
        dataPackets: state.dataPackets.filter((p) => p.id !== id),
      }));
    }, 3200);
  },
  clearOldPackets: () => set({ dataPackets: [] }),

  activeCandidatesFlow: [],
  addVisualMessage: () => {},
  updateCommanderDirective: (directive: string) => {
    set((state) => ({
      commander: {
        ...state.commander,
        activeDecision: directive,
      },
    }));
  },

  studentProfile: SEED_PROFILES[0],
  setStudentProfile: (profile) => {
    set({
      studentProfile: profile,
      commander: {
        ...get().commander,
        missionGoal: `Discover fully-funded ${profile.academic.field_of_study} opportunities for ${profile.personal.name} (${profile.academic.degree_level})`,
      },
    });
  },

  overlayView: "NONE",
  setOverlayView: (view) => set({ overlayView: view }),
  mapMode: "2D_TACTICAL",
  setMapMode: (mode) => set({ mapMode: mode }),
  mapVisualMode: "DEPLOYMENT",
  setMapVisualMode: (mode) => set({ mapVisualMode: mode }),
  scanlinesEnabled: true,
  setScanlinesEnabled: (enabled) => set({ scanlinesEnabled: enabled }),
  audioMuted: sound.isMuted(),
  toggleAudio: () => {
    const isMuted = sound.toggleMute();
    set({ audioMuted: isMuted });
    return isMuted;
  },

  activeDeckTab: "TELEMETRY",
  setActiveDeckTab: (tab) => set({ activeDeckTab: tab }),
  focusedAgent: null,
  setFocusedAgent: (target) => set({ focusedAgent: target }),

  judgeParams: {
    fullFundingOnly: true,
    activeRegions: {
      Europe: true,
      Asia: true,
      Americas: true,
      MENA: true,
      Oceania: true,
    },
    ieltsRequired: false,
    maxBudgetPkr: 250000,
    proofOfFundsLimitPkr: 1500000,
    targetField: "Computer Science",
  },
  setJudgeParams: (params) =>
    set((state) => ({ judgeParams: { ...state.judgeParams, ...params } })),
  redeployWithModifier: () => {
    sound.playBoot();
    const state = get();
    state.addCommanderDecision({
      phase: "DISCOVERY",
      decisionText: `REDEPLOYING FLEET: Filter full_funding=${state.judgeParams.fullFundingOnly}, max_pkr=${state.judgeParams.maxBudgetPkr.toLocaleString()}`,
      impact: "Re-calibrating regional query weights and out-of-pocket feasibility filters",
      status: "EXECUTING",
    });

    (Object.keys(state.judgeParams.activeRegions) as Region[]).forEach((reg) => {
      if (state.judgeParams.activeRegions[reg]) {
        state.pushDataPacket({
          source: "COMMANDER",
          target: `${reg.toUpperCase()} SCOUT`,
          type: "TASK",
          label: `RE-QUERY // ${reg.toUpperCase()}`,
          payloadSummary: `BUDGET < PKR ${state.judgeParams.maxBudgetPkr.toLocaleString()}`,
        });
      }
    });
  },

  events: [],
  addEvent: (event) => {
    const state = get();
    const newEvents = [event, ...state.events].slice(0, 400);

    let phase = state.missionPhase;
    if (event.event_type === "PHASE_TRANSITION" && event.payload.current_phase) {
      phase = event.payload.current_phase as MissionPhase;
      state.addCommanderDecision({
        phase,
        decisionText: `Phase transitioned to ${phase}. Orchestrating agent workflows.`,
        impact: `Transition to ${phase}`,
        status: "RESOLVED",
      });
    } else if (event.event_type === "MISSION_COMPLETE") {
      phase = "MISSION_COMPLETE";
      state.updateCommander({ statusText: "✓ MISSION COMPLETE // ROADMAP COMPILED" });
      state.setMapVisualMode("INTELLIGENCE");
    }

    if (event.event_type.includes("SCOUT_DEPLOYED")) {
      const reg = event.payload.region;
      if (reg) {
        state.pushDataPacket({
          source: "COMMANDER",
          target: `${reg.toUpperCase()} SCOUT`,
          type: "TASK",
          label: `DEPLOY // ${reg.toUpperCase()}`,
          payloadSummary: `${state.studentProfile.academic.field_of_study} (${state.studentProfile.academic.degree_level})`,
        });
      }
    } else if (event.event_type.includes("CANDIDATE_EXTRACTED")) {
      const reg = event.payload.region || "Europe";
      const scName = event.payload.scholarship_name || "Scholarship Found";
      state.pushDataPacket({
        source: `${reg.toUpperCase()} SCOUT`,
        target: "COMMANDER",
        type: "CANDIDATE",
        label: `EXTRACTED // ${scName.substring(0, 18)}...`,
        payloadSummary: `${reg} candidate normalized`,
      });
    } else if (event.event_type.includes("SKEPTIC_CHALLENGE")) {
      state.pushDataPacket({
        source: "SKEPTIC AGENT",
        target: "VERIFICATION THEATER",
        type: "CHALLENGE",
        label: `CHALLENGE // ${event.payload.category || "FRICTION POINT"}`,
        payloadSummary: event.payload.challenge || "Unbudgeted Pakistani settlement cost",
      });

      if (event.payload.scholarship_id) {
        const sc = state.candidates.find((c) => c.scholarship_id === event.payload.scholarship_id);
        if (sc) {
          const prev = sc.confidence_score || 92;
          const updated = Math.max(70, prev - 11);
          set((s) => ({
            scoreMutations: [
              {
                scholarshipId: sc.scholarship_id,
                scholarshipName: sc.name,
                prevScore: prev,
                newScore: updated,
                reason: event.payload.challenge || "Skeptic flagged hidden pre-departure cost",
                timestamp: Date.now(),
              },
              ...s.scoreMutations,
            ].slice(0, 10),
          }));
        }
      }
    }

    const region = event.payload.region as Region;
    if (region && state.scouts[region]) {
      const scout = { ...state.scouts[region] };
      if (event.event_type.includes("SCOUT_DEPLOYED") || event.event_type.includes("SEARCH")) {
        scout.status = "ACTIVE";
        scout.currentQuery = event.payload.query || scout.currentQuery;
      } else if (event.event_type.includes("SCRAPED")) {
        scout.status = "SCRAPING";
      } else if (event.event_type.includes("CANDIDATE")) {
        scout.itemsFound += 1;
      }
      scout.lastActivity = event.payload.message || event.event_type;

      state.updateScout(region, scout);
    }

    let newCandidates = state.candidates;
    if (event.event_type === "CANDIDATE_EXTRACTED") {
      const id = event.payload.scholarship_id;
      const found = SEED_SCHOLARSHIPS.find((s) => s.scholarship_id === id);
      if (found && !state.candidates.some((c) => c.scholarship_id === id)) {
        newCandidates = [found, ...state.candidates];
      }
    }

    set({
      events: newEvents,
      missionPhase: phase,
      candidates: newCandidates,
      progressPercent: simulationEngine.getProgress(),
    });
  },
  clearEvents: () => set({ events: [] }),

  scouts: {
    Europe: { region: "Europe", status: "IDLE", itemsFound: 0, lastActivity: "Standby" },
    Asia: { region: "Asia", status: "IDLE", itemsFound: 0, lastActivity: "Standby" },
    Americas: { region: "Americas", status: "IDLE", itemsFound: 0, lastActivity: "Standby" },
    MENA: { region: "MENA", status: "IDLE", itemsFound: 0, lastActivity: "Standby" },
    Oceania: { region: "Oceania", status: "IDLE", itemsFound: 0, lastActivity: "Standby" },
  },
  updateScout: (region, update) =>
    set((state) => ({
      scouts: {
        ...state.scouts,
        [region]: { ...state.scouts[region], ...update },
      },
    })),

  candidates: [],
  selectedScholarship: null,
  setSelectedScholarship: (scholarship) => set({ selectedScholarship: scholarship }),
  rankedResults: [],
  roadmap: null,
  scoreMutations: [],

  pastSessions: [],
  loadPastSessions: async () => {
    try {
      const data = await listSessions();
      if (data && data.sessions) {
        set({ pastSessions: data.sessions });
      }
    } catch {
      // Backend not running
    }
  },

  backendConnected: false,
  backendChecking: false,
  sseUnsubscribe: null,
  checkBackendHealth: async () => {
    set({ backendChecking: true });
    try {
      const res = await fetch("/api/health", { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        const connected = data.status === "HEALTHY" || data.status === "ONLINE";
        set({ backendConnected: connected, backendChecking: false });
        return connected;
      }
    } catch {
      // Backend not running
    }
    set({ backendConnected: false, backendChecking: false });
    return false;
  },

  startMission: async () => {
    const state = get();
    if (state.missionStatus === "RUNNING") return;

    sound.playBoot();

    const freshScouts = { ...state.scouts };
    (Object.keys(freshScouts) as Region[]).forEach((k) => {
      freshScouts[k] = { region: k, status: "ACTIVE", itemsFound: 0, lastActivity: "Deploying scout sweep..." };
    });

    set({
      missionStatus: "RUNNING",
      missionPhase: "ORCHESTRATION",
      scouts: freshScouts,
      candidates: [],
      scoreMutations: [],
      mapVisualMode: "DEPLOYMENT",
      commander: {
        ...state.commander,
        statusText: "DEPLOYING FLEET // REGIONAL SCOUTS ACTIVATED",
        activeDecision: "Deploying parallel regional discovery scouts across Europe, Asia, Americas, MENA, Oceania.",
        activeAssignments: {
          Europe: "SEARCHING",
          Asia: "SEARCHING",
          Americas: "SEARCHING",
          MENA: "SEARCHING",
          Oceania: "SEARCHING",
        },
      },
    });

    if (state.backendConnected) {
      try {
        const unsub = subscribeToEventStream(
          state.sessionId,
          (evt) => get().addEvent(evt),
          (err) => console.warn("SSE stream disconnected, falling back if needed", err)
        );
        set({ sseUnsubscribe: unsub });
         const launchRes = await launchDiscoveryMission(state.sessionId, state.studentProfile);
        if (launchRes && !launchRes.ok) {
          throw new Error(launchRes.error || "Mission start returned offline status");
        }
        return;
      } catch (err) {
         console.warn("FastAPI background mission failed, activating autonomous simulator:", err);
        const activeUnsubscribe = get().sseUnsubscribe;
        activeUnsubscribe?.();
        set({ sseUnsubscribe: null });
      }
    }

    simulationEngine.initMission(
      state.studentProfile,
      state.sessionId,
      (evt) => get().addEvent(evt),
      () => {
        set({
          missionStatus: "COMPLETE",
          missionPhase: "MISSION_COMPLETE",
          progressPercent: 100,
        });
      }
    );
    simulationEngine.setSpeed(state.replaySpeed);
    simulationEngine.start();
  },

  pauseMission: () => {
    simulationEngine.pause();
    set({
      missionStatus: "PAUSED",
      commander: {
        ...get().commander,
        statusText: "MISSION PAUSED BY OPERATOR",
      },
    });
  },

  resetMission: () => {
    const state = get();
    simulationEngine.stop();
    if (state.sseUnsubscribe) {
      state.sseUnsubscribe();
    }
    if (typeof window !== "undefined") {
      window.localStorage.removeItem(`scholarx_profile_${state.sessionId}`);
    }

    const freshScouts = { ...get().scouts };
    (Object.keys(freshScouts) as Region[]).forEach((k) => {
      freshScouts[k] = { region: k, status: "IDLE", itemsFound: 0, lastActivity: "Standby" };
    });

    set({
      sessionId: `sess-${Date.now().toString(36)}`,
      missionStatus: "IDLE",
      missionPhase: "IDLE",
      progressPercent: 0,
      events: [],
      candidates: [],
      scoreMutations: [],
      dataPackets: [],
      mapVisualMode: "DEPLOYMENT",
      scouts: freshScouts,
      sseUnsubscribe: null,
      commander: {
        missionGoal: `Discover fully-funded ${state.studentProfile.academic.field_of_study} opportunities for ${state.studentProfile.personal.name}`,
        activeDecision: "Standing by. Load profile and launch hunt to deploy regional fleet.",
        statusText: "STANDBY // READY FOR DISPATCH",
        activeAssignments: {
          Europe: "IDLE",
          Asia: "IDLE",
          Americas: "IDLE",
          MENA: "IDLE",
          Oceania: "IDLE",
        },
        recentDecisions: [],
      },
    });
  },

  setReplaySpeed: (speed) => {
    simulationEngine.setSpeed(speed);
    set({ replaySpeed: speed });
  },
}));
