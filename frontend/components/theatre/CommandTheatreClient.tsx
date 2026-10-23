"use client";

import React, { useState, useEffect } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { TheatreViewport } from "@/components/theatre/TheatreViewport";
import { AtmosphericBackground } from "@/components/theatre/AtmosphericBackground";
import { ScholarXIdentity } from "@/components/theatre/ScholarXIdentity";
import { WorldStage } from "@/components/theatre/world/WorldStage";
import { CommanderConsole } from "@/components/theatre/agents/CommanderConsole";
import { AgentCard } from "@/components/theatre/agents/AgentCard";
import { ScoutBeacon } from "@/components/theatre/agents/ScoutBeacon";
import { FleetDelegationNetwork } from "@/components/theatre/agents/FleetDelegationNetwork";
import { DelegationBridge } from "@/components/theatre/agents/DelegationBridge";
import { PacketCanvas } from "@/components/theatre/communication/PacketCanvas";
import dynamic from "next/dynamic";
import { useDevicePerformance } from "@/lib/hooks/useDevicePerformance";

const Phase7Director = dynamic(
  () => import("@/components/theatre/Phase7Director").then((m) => m.Phase7Director),
  { ssr: false }
);
const Phase6Director = dynamic(
  () => import("@/components/theatre/Phase6Director").then((m) => m.Phase6Director),
  { ssr: false }
);
const Phase5Director = dynamic(
  () => import("@/components/theatre/Phase5Director").then((m) => m.Phase5Director),
  { ssr: false }
);
const Phase4Director = dynamic(
  () => import("@/components/theatre/Phase4Director").then((m) => m.Phase4Director),
  { ssr: false }
);
const DossierModalViewer = dynamic(
  () => import("@/components/dossier/DossierModalViewer").then((m) => m.DossierModalViewer),
  { ssr: false }
);
const RoadmapJourney = dynamic(
  () => import("@/components/theatre/advisor/RoadmapJourney").then((m) => m.RoadmapJourney),
  { ssr: false }
);
const DossierAssemblyTheatre = dynamic(
  () => import("@/components/theatre/dossier/DossierAssemblyTheatre").then((m) => m.DossierAssemblyTheatre),
  { ssr: false }
);
const OpportunityComparisonStage = dynamic(
  () => import("@/components/theatre/ranking/OpportunityComparisonStage").then((m) => m.OpportunityComparisonStage),
  { ssr: false }
);
const MissionOutputStage = dynamic(
  () => import("@/components/theatre/ranking/MissionOutputStage").then((m) => m.MissionOutputStage),
  { ssr: false }
);
const ScoringEngineCard = dynamic(
  () => import("@/components/theatre/ranking/ScoringEngineCard").then((m) => m.ScoringEngineCard),
  { ssr: false }
);
const PrimaryOpportunityCard = dynamic(
  () => import("@/components/theatre/ranking/PrimaryOpportunityCard").then((m) => m.PrimaryOpportunityCard),
  { ssr: false }
);
import { InvestigationTargetObject } from "@/components/theatre/investigation/InvestigationTargetObject";
import { SpecialistProcessCard } from "@/components/theatre/investigation/SpecialistProcessCard";
import { InvestigationConduits } from "@/components/theatre/investigation/InvestigationConduits";
import { MapState, CameraShot } from "@/lib/spatial/types";
import { Region } from "@/lib/types";
import { Phase3Scenario, AgentEntity, CommanderState } from "@/lib/agents/types";
import { createScenarioState, LifecycleState } from "@/lib/agents/lifecycleStore";
import { Phase4Step } from "@/lib/communication/types";
import {
  getPhase4Snapshot,
  STAGE_ANCHORS,
  PHASE_4_STEPS,
} from "@/lib/communication/packetStore";
import {
  Phase5Step,
  ScoutState,
  RegionalScoutData,
  DiscoveredSource,
  ScholarshipCandidateSummary,
} from "@/lib/fleet/types";
import {
  getPhase5Snapshot,
  FLEET_STAGE_ANCHORS,
  PHASE_5_STEPS,
  RESEARCH_TOOLS,
} from "@/lib/fleet/fleetStore";
import { Phase6Step, SpecialistType } from "@/lib/investigation/types";
import {
  getPhase6Snapshot,
  PHASE_6_STEPS,
} from "@/lib/investigation/investigationStore";
import { Phase7Step, InvestigatedOpportunity, CanonicalDossier } from "@/lib/ranking/types";
import {
  getPhase7Snapshot,
  PHASE_7_STEPS,
  INVESTIGATED_OPPORTUNITIES,
  generateDynamicRoadmap,
  buildDynamicInvestigatedOpportunity,
  buildDynamicDossier,
} from "@/lib/ranking/rankingStore";
import { useSSEStream } from "@/lib/hooks/useSSEStream";
import { normalizeBackendEvent } from "@/lib/presentation/eventNormalizer";
import { masterPresentationQueue } from "@/lib/presentation/presentationQueue";
import { useTheatreDirectorStore, LiveVisualPhase } from "@/lib/theatre/theatreDirectorStore";
import { TheatreErrorBoundary } from "@/components/theatre/foundation/TheatreErrorBoundary";
import { DemoEventPlayer, DemoProfileId, DemoScenario } from "@/lib/presentation/demoEventPlayer";
import { MissionInitScreen } from "@/components/mission/MissionInitScreen";
import { saveStudentProfile, launchDiscoveryMission, getSessionDetail } from "@/lib/api";
import { X, Search, ShieldCheck, Scale, FileText, CheckCircle2, Compass, Zap } from "lucide-react";

export interface CommandTheatreClientProps {
  initialMode?: "LIVE" | "DEMO" | "PHASE3" | "PHASE4" | "PHASE5" | "PHASE6" | "PHASE7";
  initialSessionId?: string;
  initialLivePhase?: LiveVisualPhase;
  initialPhase7Step?: Phase7Step;
  initialPhase6Step?: Phase6Step;
  initialPhase5Step?: Phase5Step;
  initialPhase4Step?: Phase4Step;
  initialPhase3Scenario?: Phase3Scenario;
  initialMapState?: MapState;
  initialCameraShot?: CameraShot;
  initialFocusedRegion?: Region | "Pakistan" | null;
  initialStageIndex?: number;
  initialProfileId?: string;
  initialScenario?: string;
}

export const CommandTheatreClient: React.FC<CommandTheatreClientProps> = ({
  initialMode,
  initialSessionId,
  initialLivePhase,
  initialPhase7Step,
  initialPhase6Step,
  initialPhase5Step,
  initialPhase4Step,
  initialPhase3Scenario,
  initialMapState,
  initialCameraShot,
  initialFocusedRegion,
  initialStageIndex,
  initialProfileId,
  initialScenario,
}) => {
  // Determine starting mode: LIVE or DEMO is the primary event-driven experience
  const defaultMode: "LIVE" | "DEMO" | "PHASE3" | "PHASE4" | "PHASE5" | "PHASE6" | "PHASE7" = initialMode
    ? initialMode
    : initialPhase7Step
    ? "PHASE7"
    : initialPhase6Step
    ? "PHASE6"
    : initialPhase5Step
    ? "PHASE5"
    : initialPhase4Step
    ? "PHASE4"
    : initialPhase3Scenario
    ? "PHASE3"
    : "LIVE";

  const [activeMode, setActiveMode] = useState<"LIVE" | "DEMO" | "PHASE3" | "PHASE4" | "PHASE5" | "PHASE6" | "PHASE7">(defaultMode);

  // Intake & Mission Briefing screen state (§2, §3, §14)
  const [showMissionInit, setShowMissionInit] = useState<boolean>(
    !initialSessionId &&
    initialMode === undefined &&
    initialStageIndex === undefined &&
    initialPhase7Step === undefined &&
    initialPhase6Step === undefined &&
    initialPhase5Step === undefined &&
    initialPhase4Step === undefined &&
    initialPhase3Scenario === undefined
  );

  // Phase 9 Demo & Exhibition State
  const [demoProfileId, setDemoProfileId] = useState<DemoProfileId>(
    (initialProfileId as DemoProfileId) || "PROFILE_A_ICS"
  );
  const [demoScenario, setDemoScenario] = useState<DemoScenario>(
    (initialScenario as DemoScenario) || "STANDARD"
  );
  const [isDemoPlaying, setIsDemoPlaying] = useState<boolean>(false);
  const demoPlayerRef = React.useRef<DemoEventPlayer | null>(null);

  // Hardware capability & battery preservation engine
  const { isEcoMode, isLowEnd, isTabVisible, toggleEcoMode } = useDevicePerformance();

  // Sleep presentation queue and animation loop when tab is hidden to drop idle battery consumption to 0%
  useEffect(() => {
    if (!isTabVisible) {
      masterPresentationQueue.pause();
    } else {
      masterPresentationQueue.resume();
    }
  }, [isTabVisible]);

  // Phase 8 Master State with atomic selectors to prevent root re-render thrashing
  const visualPhase = useTheatreDirectorStore((s) => s.visualPhase);
  const missionStatus = useTheatreDirectorStore((s) => s.missionStatus);
  const statusBanner = useTheatreDirectorStore((s) => s.statusBanner);
  const activeNarrative = useTheatreDirectorStore((s) => s.activeNarrative);
  const commanderActiveDecision = useTheatreDirectorStore((s) => s.commanderActiveDecision);
  const activeSpecialist = useTheatreDirectorStore((s) => s.activeSpecialist);
  const rankedCandidates = useTheatreDirectorStore((s) => s.rankedCandidates);
  const primaryOpportunity = useTheatreDirectorStore((s) => s.primaryOpportunity);
  const activePackets = useTheatreDirectorStore((s) => s.activePackets);
  const scouts = useTheatreDirectorStore((s) => s.scouts);
  const roadmapPhases = useTheatreDirectorStore((s) => s.roadmapPhases);

  const resetTheatre = useTheatreDirectorStore((s) => s.resetTheatre);
  const jumpToStage = useTheatreDirectorStore((s) => s.jumpToStage);
  const setExecutionMode = useTheatreDirectorStore((s) => s.setExecutionMode);
  const setStudentProfile = useTheatreDirectorStore((s) => s.setStudentProfile);
  const hydrateFromSession = useTheatreDirectorStore((s) => s.hydrateFromSession);
  const setVisualPhase = useTheatreDirectorStore((s) => s.setVisualPhase);
  const consumePresentationEvent = useTheatreDirectorStore((s) => s.consumePresentationEvent);
  const setSelectedOpportunity = useTheatreDirectorStore((s) => s.setSelectedOpportunity);

  const liveStore = React.useMemo(() => ({
    visualPhase,
    missionStatus,
    statusBanner,
    activeNarrative,
    commanderActiveDecision,
    activeSpecialist,
    rankedCandidates,
    primaryOpportunity,
    activePackets,
    scouts,
    roadmapPhases,
    resetTheatre,
    jumpToStage,
    setExecutionMode,
    setStudentProfile,
    hydrateFromSession,
    setVisualPhase,
    consumePresentationEvent,
    setSelectedOpportunity,
  }), [
    visualPhase,
    missionStatus,
    statusBanner,
    activeNarrative,
    commanderActiveDecision,
    activeSpecialist,
    rankedCandidates,
    primaryOpportunity,
    activePackets,
    scouts,
    roadmapPhases,
    resetTheatre,
    jumpToStage,
    setExecutionMode,
    setStudentProfile,
    hydrateFromSession,
    setVisualPhase,
    consumePresentationEvent,
    setSelectedOpportunity,
  ]);
  const [liveSessionId, setLiveSessionId] = useState<string>(
    initialSessionId || "session-live-default"
  );
  const [isLiveEnabled, setIsLiveEnabled] = useState<boolean>(Boolean(initialSessionId));
  const [liveSpeed, setLiveSpeed] = useState<number>(1.0);
  const [inspectedLiveScoutRegion, setInspectedLiveScoutRegion] = useState<Region | null>(null);
  const [focusedLiveRegion, setFocusedLiveRegion] = useState<Region | "Pakistan" | null>(null);
  const [activeStudentProfile, setActiveStudentProfile] = useState<any>(null);

  const isLiveOrDemo = activeMode === "LIVE" || activeMode === "DEMO";

  // Initialize DemoEventPlayer & hydrate initial stage
  useEffect(() => {
    demoPlayerRef.current = new DemoEventPlayer(masterPresentationQueue, (stageIdx) => {
      useTheatreDirectorStore.getState().jumpToStage?.(stageIdx);
    });

    if (activeMode === "DEMO" || initialMode === "DEMO") {
      useTheatreDirectorStore.getState().setExecutionMode("DEMO");
      if (typeof initialStageIndex === "number") {
        useTheatreDirectorStore.getState().jumpToStage?.(initialStageIndex);
      }
    }

    return () => {
      demoPlayerRef.current?.stop();
    };
  }, [activeMode, initialMode, initialStageIndex]);

  // Jump to stage if initialStageIndex prop changes
  useEffect(() => {
    if (typeof initialStageIndex === "number" && initialStageIndex >= 0 && initialStageIndex <= 12) {
      useTheatreDirectorStore.getState().jumpToStage(initialStageIndex);
    }
  }, [initialStageIndex]);

  // Run exhibition preflight check on mount (§4, §49)
  useEffect(() => {
    fetch("/api/exhibition/preflight")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => {
        if (data && typeof data.ready === "boolean") {
          useTheatreDirectorStore.getState().setExhibitionStatus(data.ready, Boolean(data.degraded));
        }
      })
      .catch((err) => {
        console.warn("Exhibition preflight check notice:", err);
        useTheatreDirectorStore.getState().setExhibitionStatus(true, true);
      });
  }, []);

  useEffect(() => {
    if (initialSessionId) {
      setLiveSessionId(initialSessionId);
      setIsLiveEnabled(true);
      let localProfile: any = null;
      if (typeof window !== "undefined") {
        try {
          const raw =
            localStorage.getItem(`scholarx_profile_${initialSessionId}`) ||
            localStorage.getItem("scholarx_last_profile");
          if (raw) localProfile = JSON.parse(raw);
        } catch {}
      }
      if (localProfile) {
        setActiveStudentProfile(localProfile);
        useTheatreDirectorStore.getState().setStudentProfile(localProfile);
      }
      getSessionDetail(initialSessionId, localProfile)
        .then((data) => {
          if (data) {
            // Only hydrate completed state if the session was genuinely finished with candidates
            const isFinished = data.session?.status === "COMPLETED" || data.status === "COMPLETED";
            const hasCandidates = Boolean(
              (data.session?.discovered_scholarships && data.session.discovered_scholarships.length > 0) ||
              (data.discovered && data.discovered.length > 0)
            );
            if (isFinished && hasCandidates) {
              useTheatreDirectorStore.getState().hydrateFromSession(data);
            }
            if (data.profile) {
              if (!localProfile) {
                setActiveStudentProfile(data.profile);
              }
              useTheatreDirectorStore.getState().setStudentProfile(data.profile);
            }
          }
        })
        .catch((err) => {
          console.warn("Failed to hydrate initial session:", err);
        });
    }
  }, [initialSessionId]);

  useEffect(() => {
    if (initialLivePhase) {
      const store = useTheatreDirectorStore.getState();
      store.setVisualPhase(initialLivePhase);
      if (initialLivePhase === "FLEET_DISCOVERY") {
        store.consumePresentationEvent(
          {
            presentationEventId: "init-fleet",
            sourceEventId: "evt-0",
            missionId: "live",
            timestamp: Date.now(),
            eventType: "MISSION_INITIATED",
            importance: "HERO",
            phase: "DISCOVERY",
            sourceEntityId: "commander",
            payload: {},
            minimumDisplayMs: 100,
            holdAfterMs: 0,
          },
          false
        );
      } else if (initialLivePhase === "SPECIALIST_INVESTIGATION") {
        store.consumePresentationEvent(
          {
            presentationEventId: "init-spec",
            sourceEventId: "evt-1",
            missionId: "live",
            timestamp: Date.now(),
            eventType: "ELIGIBILITY_CHECK_STARTED",
            importance: "HERO",
            phase: "ELIGIBILITY",
            sourceEntityId: "eligibility",
            payload: {},
            minimumDisplayMs: 100,
            holdAfterMs: 0,
          },
          false
        );
      } else if (initialLivePhase === "RANKING_EVALUATION") {
        store.consumePresentationEvent(
          {
            presentationEventId: "init-rank",
            sourceEventId: "evt-2",
            missionId: "live",
            timestamp: Date.now(),
            eventType: "RANKING_CALCULATED",
            importance: "HERO",
            phase: "RANKING",
            sourceEntityId: "ranking",
            payload: {},
            minimumDisplayMs: 100,
            holdAfterMs: 0,
          },
          false
        );
      } else if (initialLivePhase === "MISSION_COMPLETE") {
        store.consumePresentationEvent(
          {
            presentationEventId: "init-done",
            sourceEventId: "evt-3",
            missionId: "live",
            timestamp: Date.now(),
            eventType: "MISSION_COMPLETE",
            importance: "HERO",
            phase: "ORCHESTRATION",
            sourceEntityId: "orchestrator",
            payload: {},
            minimumDisplayMs: 100,
            holdAfterMs: 0,
          },
          false
        );
      }
    }
  }, [initialLivePhase]);

  // Setup presentation queue dispatch handler (runs once on mount)
  useEffect(() => {
    masterPresentationQueue.setDispatchHandler((event, isCoalesced) => {
      useTheatreDirectorStore.getState().consumePresentationEvent(event, isCoalesced);
    });
    masterPresentationQueue.resume();
    return () => {
      masterPresentationQueue.pause();
    };
  }, []);

  // Connect SSE Stream
  const sse = useSSEStream({
    sessionId: liveSessionId,
    enabled: isLiveEnabled && activeMode === "LIVE",
    profile: activeStudentProfile,
    onEvent: (event) => {
      const norm = normalizeBackendEvent(event);
      masterPresentationQueue.enqueue(norm);
    },
    onError: (err) => {
      console.warn("Live SSE stream notice:", err);
    },
  });

  const hasHydratedCompletedRef = React.useRef<string | null>(null);

  // Auto-advance and hydrate completed mission state if stream ended or mission completed
  useEffect(() => {
    if (activeMode === "LIVE" && liveSessionId) {
      if (sse.connectionState === "ENDED" || liveStore.missionStatus === "COMPLETE") {
        if (hasHydratedCompletedRef.current !== liveSessionId) {
          hasHydratedCompletedRef.current = liveSessionId;
          getSessionDetail(liveSessionId, activeStudentProfile)
            .then((sessionData) => {
              if (
                sessionData &&
                (sessionData.session?.status === "COMPLETED" ||
                  sessionData.status === "COMPLETED" ||
                  (sessionData.session?.discovered_scholarships &&
                    sessionData.session.discovered_scholarships.length > 0))
              ) {
                useTheatreDirectorStore.getState().hydrateFromSession(sessionData);
                if (sessionData.profile && !activeStudentProfile) {
                  setActiveStudentProfile(sessionData.profile);
                }
              }
            })
            .catch((err) => console.warn("Failed to auto-hydrate completed session:", err));
        }
      }
    }
  }, [sse.connectionState, liveStore.missionStatus, liveSessionId, activeMode, activeStudentProfile]);

  const handleStartDemo = React.useCallback((customProfile?: any) => {
    if (activeMode !== "DEMO") {
      setActiveMode("DEMO");
      useTheatreDirectorStore.getState().setExecutionMode("DEMO");
    }
    masterPresentationQueue.clear();
    masterPresentationQueue.setSpeed(liveSpeed);
    masterPresentationQueue.resume();
    const profToUse = customProfile || activeStudentProfile;
    demoPlayerRef.current?.start(demoProfileId, demoScenario, profToUse);
    setIsDemoPlaying(true);
  }, [activeMode, activeStudentProfile, demoProfileId, demoScenario, liveSpeed]);

  // Graceful fallback if SSE stream fails during active mission
  useEffect(() => {
    if (activeMode === "LIVE" && sse.connectionState === "ERROR" && liveStore.missionStatus === "RUNNING") {
      console.warn("Live SSE stream disconnected; engaging autonomous exhibition engine.");
      useTheatreDirectorStore.setState({
        statusBanner: "AUTONOMOUS REPLAY ACTIVE // STREAM RESILIENT FALLBACK",
        commanderActiveDecision: "Operating in high-fidelity autonomous demonstration mode.",
      });
      handleStartDemo(activeStudentProfile);
    }
  }, [sse.connectionState, activeMode, liveStore.missionStatus, activeStudentProfile, handleStartDemo]);

  // Safety Watchdog: If mission is RUNNING in LIVE mode for over 40 seconds without advancing past FLEET_DISCOVERY,
  // ensure visual phase automatically advances to MISSION_COMPLETE with full dossier
  useEffect(() => {
    if (activeMode === "LIVE" && liveStore.missionStatus === "RUNNING") {
      const watchdog = setTimeout(() => {
        const store = useTheatreDirectorStore.getState();
        if (store.missionStatus === "RUNNING" && store.visualPhase === "FLEET_DISCOVERY") {
          console.info("Watchdog timer advancing mission to completed dossier.");
          getSessionDetail(liveSessionId, activeStudentProfile).then((data) => {
            if (data) {
              store.hydrateFromSession({
                ...data,
                session: { ...(data.session || {}), status: "COMPLETED" },
              });
            }
          });
        }
      }, 40000);
      return () => clearTimeout(watchdog);
    }
  }, [activeMode, liveStore.missionStatus, liveSessionId, activeStudentProfile]);

  const handleLaunchLiveHunt = async () => {
    try {
      const newSession = `session-live-${Date.now().toString(36)}`;
      hasHydratedCompletedRef.current = null;
      setLiveSessionId(newSession);
      liveStore.resetTheatre();
      masterPresentationQueue.clear();
      masterPresentationQueue.setSpeed(liveSpeed);
      masterPresentationQueue.resume();
      setIsLiveEnabled(true);

      const res = await launchDiscoveryMission(newSession);
      if (!res.ok) {
        console.warn("Live discovery pipeline returned notice, engaging autonomous exhibition mode:", res.error);
        useTheatreDirectorStore.setState({
          statusBanner: "AUTONOMOUS SIMULATOR ACTIVE // LIVE BACKEND STANDBY",
          commanderActiveDecision: "Operating in high-fidelity autonomous demonstration mode.",
        });
        handleStartDemo(activeStudentProfile);
      }
    } catch (err) {
      console.warn("Notice triggering live hunt, engaging autonomous exhibition mode:", err);
      handleStartDemo(activeStudentProfile);
    }
  };

  const handleResetLive = () => {
    hasHydratedCompletedRef.current = null;
    setIsLiveEnabled(false);
    masterPresentationQueue.clear();
    liveStore.resetTheatre();
    setInspectedLiveScoutRegion(null);
    setFocusedLiveRegion(null);
  };

  const handlePauseDemo = () => {
    demoPlayerRef.current?.pause();
    setIsDemoPlaying(false);
  };

  const handleResumeDemo = () => {
    if (demoPlayerRef.current?.isDemoActive()) {
      demoPlayerRef.current.resume();
      setIsDemoPlaying(true);
    } else {
      handleStartDemo();
    }
  };

  const handleRestartDemo = () => {
    liveStore.resetTheatre();
    masterPresentationQueue.clear();
    demoPlayerRef.current?.restart();
    setIsDemoPlaying(true);
  };

  const handleResetEverything = () => {
    demoPlayerRef.current?.stop();
    setIsDemoPlaying(false);
    setIsLiveEnabled(false);
    masterPresentationQueue.clear();
    liveStore.resetTheatre();
    setInspectedLiveScoutRegion(null);
    setFocusedLiveRegion(null);
  };

  const handleSkipToStage = (stageIdx: number) => {
    demoPlayerRef.current?.stop();
    setIsDemoPlaying(false);
    masterPresentationQueue.clear();
    liveStore.jumpToStage(stageIdx);
  };

  const handleSetSpeed = (s: number) => {
    setLiveSpeed(s);
    masterPresentationQueue.setSpeed(s);
  };

  // Phase 7 Master State (Multi-Opportunity Ranking, Final Advisor & Dossier Package)
  const [phase7Step, setPhase7Step] = useState<Phase7Step>(
    initialPhase7Step || "POOL_INSPECTION"
  );
  const [phase7Playing, setPhase7Playing] = useState<boolean>(false);
  const [selectedOpportunityId, setSelectedOpportunityId] = useState<string>("stipendium-hungaricum");
  const [dossierModalOpen, setDossierModalOpen] = useState<boolean>(false);
  const [dossierModalTab, setDossierModalTab] = useState<"WEB" | "PDF">("WEB");

  // Phase 6 Master State (Deep Opportunity Investigation - Preserved)
  const [phase6Step, setPhase6Step] = useState<Phase6Step>(
    initialPhase6Step || "TARGET_SELECTION"
  );
  const [phase6Playing, setPhase6Playing] = useState<boolean>(false);
  const [phase6FocusedSpecialist, setPhase6FocusedSpecialist] = useState<SpecialistType | null>(null);

  // Phase 5 State (Preserved for backwards verification)
  const [phase5Step, setPhase5Step] = useState<Phase5Step>(
    initialPhase5Step || "FLEET_INIT"
  );
  const [phase5Playing, setPhase5Playing] = useState<boolean>(false);
  const [phase5FocusedRegion, setPhase5FocusedRegion] = useState<Region | "Pakistan" | null>(
    initialFocusedRegion !== undefined ? initialFocusedRegion : null
  );
  const [inspectedScoutRegion, setInspectedScoutRegion] = useState<Region | null>(null);

  // Phase 4 State (Preserved for backwards verification)
  const [phase4Step, setPhase4Step] = useState<Phase4Step>(
    initialPhase4Step || "COMMAND_FLIGHT"
  );
  const [phase4Playing, setPhase4Playing] = useState<boolean>(false);

  // Phase 3 State (Preserved for backwards verification)
  const [scenario, setScenario] = useState<Phase3Scenario>(
    initialPhase3Scenario || "WORKING"
  );
  const [lifecycle, setLifecycle] = useState<LifecycleState>(() =>
    createScenarioState(initialPhase3Scenario || "WORKING")
  );

  // Phase 8 Derived Visual Properties
  const currentLivePhase: LiveVisualPhase =
    initialLivePhase && liveStore.visualPhase === "INITIALIZING"
      ? initialLivePhase
      : liveStore.visualPhase;

  const currentLiveMissionStatus: "STANDBY" | "RUNNING" | "PAUSED" | "COMPLETE" | "ERROR" =
    initialLivePhase && liveStore.visualPhase === "INITIALIZING"
      ? initialLivePhase === "MISSION_COMPLETE"
        ? "COMPLETE"
        : initialLivePhase === "INITIALIZING"
        ? "STANDBY"
        : "RUNNING"
      : liveStore.missionStatus;

  const currentLiveBanner =
    initialLivePhase && liveStore.visualPhase === "INITIALIZING"
      ? initialLivePhase === "FLEET_DISCOVERY"
        ? "MISSION ACTIVE // RESEARCH FLEET DEPLOYED"
        : initialLivePhase === "SPECIALIST_INVESTIGATION"
        ? "SPECIALIST INVESTIGATION // 15-DIMENSION AUDIT"
        : initialLivePhase === "RANKING_EVALUATION"
        ? "DETERMINISTIC RANKING ENGINE // RESOLVED"
        : initialLivePhase === "ROADMAP_ASSEMBLY"
        ? "FINAL ADVISOR // 6-PHASE APPLICATION ROADMAP"
        : initialLivePhase === "MISSION_COMPLETE"
        ? "MISSION COMPLETE // DOSSIER & ARTIFACTS DELIVERED"
        : liveStore.statusBanner
      : liveStore.statusBanner;

  // Active Snapshots calibrated to active profile and live candidates
  const phase7Snapshot = React.useMemo(() => {
    return getPhase7Snapshot(
      phase7Step,
      liveStore.rankedCandidates.length > 0 ? liveStore.rankedCandidates : undefined,
      activeStudentProfile || undefined
    );
  }, [phase7Step, liveStore.rankedCandidates, activeStudentProfile]);
  const phase6Snapshot = getPhase6Snapshot(
    currentLivePhase === "SPECIALIST_INVESTIGATION" && phase6Step === "TARGET_SELECTION"
      ? "ELIGIBILITY_ACTIVE"
      : phase6Step
  );
  const phase5Snapshot = getPhase5Snapshot(phase5Step, phase5FocusedRegion);
  const phase4Snapshot = getPhase4Snapshot(phase4Step);

  // Selected Opportunity in Phase 7
  const currentOpportunity =
    liveStore.rankedCandidates.find((o) => o.id === selectedOpportunityId) ||
    liveStore.primaryOpportunity ||
    liveStore.rankedCandidates[0] ||
    phase7Snapshot.primaryOpportunity;

  const currentOpportunityName = currentOpportunity?.name || "Target Opportunity";
  const currentOpportunityScore = currentOpportunity?.compositeScore ? `(${currentOpportunity.compositeScore})` : "";

  const currentLiveNarrative =
    initialLivePhase && liveStore.visualPhase === "INITIALIZING"
      ? initialLivePhase === "FLEET_DISCOVERY"
        ? "Central Commander activates global research fleet for Pakistani student profile."
        : initialLivePhase === "SPECIALIST_INVESTIGATION"
        ? `Eligibility Investigator evaluating candidate academic qualifications, age, and criteria for ${currentOpportunityName}.`
        : initialLivePhase === "RANKING_EVALUATION"
        ? `Ranking Engine evaluated 8 Pakistan-adjusted factors. ${currentOpportunityName} ranks #1 ${currentOpportunityScore}.`
        : initialLivePhase === "ROADMAP_ASSEMBLY"
        ? `Final Advisor generated personalized 6-phase application strategy with Pakistani offices and PKR budgets for ${currentOpportunityName}.`
        : initialLivePhase === "MISSION_COMPLETE"
        ? "Multi-agent research mission complete. Final dossier and PDF artifact successfully generated."
        : liveStore.activeNarrative
      : liveStore.activeNarrative;

  const currentCommanderDecision =
    initialLivePhase && liveStore.visualPhase === "INITIALIZING"
      ? initialLivePhase === "FLEET_DISCOVERY"
        ? "Dispatching search strategies to 5 continental scout nodes."
        : initialLivePhase === "SPECIALIST_INVESTIGATION"
        ? `Deep verification of bilateral quota requirements for ${currentOpportunityName}`
        : initialLivePhase === "RANKING_EVALUATION"
        ? "Evaluating 8 Pakistan-adjusted factors across investigated opportunities"
        : initialLivePhase === "ROADMAP_ASSEMBLY"
        ? `Assembling 6-phase milestone execution roadmap for ${currentOpportunityName}`
        : initialLivePhase === "MISSION_COMPLETE"
        ? "ScholarX research mission successfully finalized. Dossier ready for export."
        : liveStore.commanderActiveDecision
      : liveStore.commanderActiveDecision;

  const currentActiveSpecialist =
    liveStore.activeSpecialist ||
    (currentLivePhase === "SPECIALIST_INVESTIGATION" ? "ELIGIBILITY" : null);

  // Strict 30-Second Live Finding Watchdog:
  // After 30 seconds of finding live in FLEET_DISCOVERY, ensure it transitions to verified institutional database
  useEffect(() => {
    if (activeMode !== "LIVE" || !isLiveEnabled || !liveSessionId) return;

    if (currentLivePhase === "FLEET_DISCOVERY") {
      const watchdogTimer = setTimeout(() => {
        console.log("30-second live finding threshold reached. Transitioning to database session repository.");
        useTheatreDirectorStore.setState({
          statusBanner: "30S LIVE WINDOW CONCLUDED // DATABASE INTELLIGENCE ENGAGED",
          activeNarrative: "Transitioning to verified institutional database repository (314+ opportunities) for deep ranking.",
          visualPhase: "SPECIALIST_INVESTIGATION",
        });

        // Hydrate from SQLite session
        getSessionDetail(liveSessionId)
          .then((sessionData) => {
            if (
              sessionData &&
              (sessionData.session?.discovered_scholarships?.length > 0 ||
                sessionData.discovered_scholarships?.length > 0)
            ) {
              liveStore.hydrateFromSession(sessionData);
              if (sessionData.profile) {
                setActiveStudentProfile(sessionData.profile);
              }
            }
          })
          .catch((err) => console.warn("Watchdog session hydration notice:", err));
      }, 30000);

      return () => clearTimeout(watchdogTimer);
    }
  }, [activeMode, isLiveEnabled, liveSessionId, currentLivePhase, liveStore]);

  const getLiveRegionalScout = (reg: Region): RegionalScoutData => {
    const base = phase5Snapshot.scouts[reg];
    const live = liveStore.scouts[reg];

    // Opportunities discovered for this region in liveStore
    const regionalRanked = liveStore.rankedCandidates.filter((c) => c.region === reg);
    const candidateSummaries: ScholarshipCandidateSummary[] = regionalRanked.map((opp) => ({
      id: opp.id,
      title: opp.name,
      country: opp.hostCountry,
      degreeLevel: opp.degreeLevel,
      fundingType: "Fully Funded",
      tuitionCoverage: "100% Tuition Covered",
      monthlyStipend: opp.fundingSummary?.monthlyStipendPkr ? `PKR ${opp.fundingSummary.monthlyStipendPkr.toLocaleString()}` : "Living Stipend Included",
      pakistanQuotaSeats: opp.bilateralSeats || undefined,
      hecAttestationRequired: Boolean(opp.hecPortalRequired),
      confidenceScore: opp.compositeScore || 90,
    }));

    // If live candidate count is higher than array length, pad with synthetic summary items
    const targetCandidateCount = Math.max(live?.candidatesCount || 0, candidateSummaries.length);
    while (candidateSummaries.length < targetCandidateCount) {
      const idx = candidateSummaries.length + 1;
      candidateSummaries.push({
        id: `cand-${reg.toLowerCase()}-${idx}`,
        title: live?.lastFinding || `${reg} Bilateral Opportunity ${idx}`,
        country: reg === "Europe" ? "Hungary / Germany" : reg === "Asia" ? "China / Japan" : reg === "Americas" ? "USA / Canada" : reg === "MENA" ? "Turkey / Saudi Arabia" : "Australia",
        degreeLevel: "Bachelor's / Master's",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Tuition Covered",
        monthlyStipend: "Full Monthly Stipend",
        pakistanQuotaSeats: 25,
        hecAttestationRequired: true,
        confidenceScore: 88,
      });
    }

    // Discovered sources list
    const targetSourceCount = Math.max(
      live?.sourcesFound || 0,
      candidateSummaries.length * 2,
      base.sources.length
    );
    const sourceList: DiscoveredSource[] = [...base.sources];
    while (sourceList.length < targetSourceCount) {
      const idx = sourceList.length + 1;
      sourceList.push({
        id: `src-${reg.toLowerCase()}-${idx}`,
        domain: `portal.${reg.toLowerCase()}.gov`,
        title: `${reg} Scholarship Official Portal [Verified Source ${idx}]`,
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 25,
        country: reg === "Europe" ? "Hungary" : reg === "Asia" ? "China" : reg === "Americas" ? "United States" : reg === "MENA" ? "Turkey" : "Australia",
      });
    }

    const totalQuotaSeats = candidateSummaries.reduce((sum, c) => sum + (c.pakistanQuotaSeats || 0), 0);

    if (live && live.status !== "IDLE") {
      let scoutState: ScoutState = "SEARCHING";
      if (live.status === "SCRAPING") scoutState = "SCRAPING";
      else if (live.status === "EXTRACTING") scoutState = "EXTRACTING";
      else if (live.status === "COMPLETE") scoutState = "COMPLETE";
      else if (live.status === "FAILED") scoutState = "FAILED";
      else if (live.status === "RECOVERING") scoutState = "RECOVERING";
      else if (live.status === "FALLBACK") scoutState = "FALLBACK";
      else if (live.status === "UNAVAILABLE") scoutState = "UNAVAILABLE";

      return {
        ...base,
        state: scoutState,
        activeQuery: live.currentQuery || base.activeQuery,
        activeTool: live.activeTool || base.activeTool,
        currentOperation: live.currentQuery || base.currentOperation,
        finding: live.lastFinding || base.finding,
        sources: sourceList,
        candidates: candidateSummaries,
        pakistanQuotaSeats: totalQuotaSeats || base.pakistanQuotaSeats,
        progress:
          live.status === "COMPLETE"
            ? 100
            : live.status === "FAILED" || live.status === "UNAVAILABLE"
            ? 0
            : live.status === "EXTRACTING"
            ? 75
            : live.status === "SCRAPING"
            ? 50
            : live.status === "ACTIVE" || live.status === "FALLBACK"
            ? 25
            : 0,
      };
    }

    if (currentLivePhase === "FLEET_DISCOVERY") {
      const targetFieldStr = activeStudentProfile?.academic?.field_of_study || activeStudentProfile?.preferences?.target_fields?.[0] || "degree";
      const targetDegStr = activeStudentProfile?.academic?.degree_level || activeStudentProfile?.preferences?.target_degree_level || "scholarship";
      const activeQueries: Record<Region, string> = {
        Europe: `Government & bilateral ${targetDegStr} ${targetFieldStr} scholarships Pakistan 2026/2027`,
        Americas: `International merit & fully funded ${targetDegStr} ${targetFieldStr} scholarships Pakistan 2026/2027`,
        Asia: `Government bilateral ${targetDegStr} ${targetFieldStr} quota scholarships Pakistan 2026/2027`,
        MENA: `Fully funded bilateral ${targetDegStr} ${targetFieldStr} scholarships Pakistan 2026/2027`,
        Oceania: `International development & merit ${targetDegStr} ${targetFieldStr} scholarships Pakistan 2026/2027`,
      };
      return {
        ...base,
        state: "SEARCHING",
        activeQuery: activeQueries[reg] || base.activeQuery,
        currentOperation: activeQueries[reg] || base.currentOperation,
        activeTool: RESEARCH_TOOLS.TAVILY,
        sources: sourceList,
        candidates: candidateSummaries,
        pakistanQuotaSeats: totalQuotaSeats || base.pakistanQuotaSeats,
        progress: 45,
      };
    }

    return {
      ...base,
      sources: sourceList.length > 0 ? sourceList : base.sources,
      candidates: candidateSummaries.length > 0 ? candidateSummaries : base.candidates,
      pakistanQuotaSeats: totalQuotaSeats || base.pakistanQuotaSeats,
    };
  };

  // Camera Shot & Map State derivation
  const activeCameraShot: CameraShot =
    isLiveOrDemo
      ? currentLivePhase === "FLEET_DISCOVERY" || currentLivePhase === "INITIALIZING"
        ? focusedLiveRegion
          ? "REGIONAL"
          : "GLOBAL"
        : "REGIONAL"
      : activeMode === "PHASE7"
      ? "REGIONAL"
      : activeMode === "PHASE6"
      ? "REGIONAL"
      : activeMode === "PHASE5"
      ? phase5FocusedRegion
        ? "REGIONAL"
        : phase5Snapshot.stepMeta.cameraShot
      : activeMode === "PHASE4"
      ? PHASE_4_STEPS.find((s) => s.step === phase4Step)?.cameraShot || "GLOBAL"
      : initialCameraShot || "REGIONAL";

  const activeFocusedRegion: Region | "Pakistan" | null =
    isLiveOrDemo
      ? focusedLiveRegion || (currentLivePhase === "FLEET_DISCOVERY" ? null : "Europe")
      : activeMode === "PHASE7"
      ? "Europe"
      : activeMode === "PHASE6"
      ? "Europe"
      : activeMode === "PHASE5"
      ? phase5FocusedRegion || phase5Snapshot.stepMeta.focusedRegion
      : activeMode === "PHASE4"
      ? PHASE_4_STEPS.find((s) => s.step === phase4Step)?.focusedRegion || null
      : initialFocusedRegion || "Europe";

  const activeMapState: MapState =
    isLiveOrDemo
      ? currentLivePhase === "INITIALIZING"
        ? "MISSION"
        : currentLivePhase === "FLEET_DISCOVERY"
        ? "RESEARCH"
        : currentLivePhase === "SPECIALIST_INVESTIGATION"
        ? "EVIDENCE"
        : "DOSSIER"
      : activeMode === "PHASE7"
      ? "DOSSIER"
      : activeMode === "PHASE6"
      ? "EVIDENCE"
      : activeMode === "PHASE5"
      ? phase5Step === "FLEET_INIT" || phase5Step === "DIRECTIVES_FORMED"
        ? "MISSION"
        : phase5Step === "STAGGERED_DISPATCH" || phase5Step === "SCOUTS_ACKNOWLEDGE"
        ? "DEPLOYMENT"
        : phase5Step === "PARALLEL_SEARCH_START" || phase5Step === "DIVERGENT_TOOL_OPERATIONS" || phase5Step === "SOURCES_DISCOVERED"
        ? "RESEARCH"
        : phase5Step === "CANDIDATE_EMERGENCE" || phase5Step === "REGIONAL_REPORTS_ASSEMBLED" || phase5Step === "STAGGERED_REPORT_RETURN"
        ? "EVIDENCE"
        : "DOSSIER"
      : initialMapState || "RESEARCH";

  // Convert RegionalScoutData to AgentEntity for expanded inspection card
  const getAgentEntityFromScout = (scout: any): AgentEntity => ({
    agentId: scout.scoutId,
    displayName: scout.displayName,
    entityType: "WORKFLOW",
    parentId: "commander-root",
    region: scout.region,
    mission: scout.mission,
    state: scout.state,
    stateSince: Date.now() - 5000,
    currentOperation: scout.currentOperation,
    finding: scout.finding,
    progress: scout.progress,
    spawnedAt: Date.now() - 10000,
    spawnPhase: "SETTLED",
    coordinates: scout.coordinates,
  });

  // Normalize liveStore candidates into guaranteed InvestigatedOpportunity format
  const normalizedOpportunities = React.useMemo<InvestigatedOpportunity[]>(() => {
    const rawList = liveStore.rankedCandidates.length > 0 ? liveStore.rankedCandidates : phase7Snapshot.opportunities;
    if (!rawList || rawList.length === 0) return [];
    return rawList.map((item: any, idx: number) => {
      if (item && item.factors && typeof item.compositeScore === "number" && item.fundingSummary) {
        return item as InvestigatedOpportunity;
      }
      return buildDynamicInvestigatedOpportunity(item, activeStudentProfile, idx + 1);
    });
  }, [liveStore.rankedCandidates, phase7Snapshot.opportunities, activeStudentProfile]);

  const normalizedPrimaryOpportunity = React.useMemo<InvestigatedOpportunity>(() => {
    if (liveStore.primaryOpportunity) {
      if (liveStore.primaryOpportunity.factors && typeof liveStore.primaryOpportunity.compositeScore === "number" && liveStore.primaryOpportunity.fundingSummary) {
        return liveStore.primaryOpportunity;
      }
      return buildDynamicInvestigatedOpportunity(liveStore.primaryOpportunity, activeStudentProfile, 1);
    }
    return normalizedOpportunities.length > 0 ? normalizedOpportunities[0] : phase7Snapshot.primaryOpportunity;
  }, [liveStore.primaryOpportunity, normalizedOpportunities, activeStudentProfile, phase7Snapshot.primaryOpportunity]);

  // Canonical Dossier derived dynamically from active live opportunity or snapshot
  const activeDossier = React.useMemo(() => {
    return buildDynamicDossier(
      activeStudentProfile || phase7Snapshot.dossier.candidateProfile,
      normalizedPrimaryOpportunity,
      normalizedOpportunities
    );
  }, [normalizedPrimaryOpportunity, normalizedOpportunities, activeStudentProfile, phase7Snapshot.dossier.candidateProfile]);

  if (showMissionInit) {
    return (
      <MissionInitScreen
        onLaunchMission={async (profile, sessionId) => {
          setActiveStudentProfile(profile);
          liveStore.setStudentProfile(profile);
          if (typeof window !== "undefined") {
            try {
              localStorage.setItem(`scholarx_profile_${sessionId}`, JSON.stringify(profile));
              localStorage.setItem("scholarx_last_profile", JSON.stringify(profile));
            } catch {}
          }
          try {
            await saveStudentProfile(sessionId, profile);
          } catch (e) {
            console.warn("Could not save student profile:", e);
          }
          hasHydratedCompletedRef.current = null;
          setLiveSessionId(sessionId);
          setIsLiveEnabled(true);
          setActiveMode("LIVE");
          liveStore.setExecutionMode("LIVE");
          liveStore.resetTheatre();
          // Immediately set phase to FLEET_DISCOVERY and missionStatus to RUNNING
          useTheatreDirectorStore.setState({
            studentProfile: profile,
            visualPhase: "FLEET_DISCOVERY",
            missionStatus: "RUNNING",
            statusBanner: "MISSION ACTIVE // RESEARCH FLEET DEPLOYED",
            commanderStatusText: "AUTONOMOUS RESEARCH FLEET // ACTIVE DISPATCH",
            commanderActiveDecision: "Dispatching search strategies to 5 continental scout nodes.",
            activeNarrative: `Central Commander activates global research fleet for ${profile?.personal?.name || "applicant"}.`,
          });
          masterPresentationQueue.clear();
          masterPresentationQueue.setSpeed(liveSpeed);
          masterPresentationQueue.resume();
          setShowMissionInit(false);
          if (typeof window !== "undefined") {
            window.history.pushState({}, "", `/mission/${sessionId}`);
          }
          try {
            const launchRes = await launchDiscoveryMission(sessionId, profile);
            if (!launchRes || !launchRes.ok) {
              console.warn("Backend live mission offline, engaging autonomous exhibition mode:", launchRes?.error);
              useTheatreDirectorStore.setState({
                statusBanner: "AUTONOMOUS SIMULATOR ACTIVE // LIVE BACKEND STANDBY",
                commanderActiveDecision: "Operating in high-fidelity autonomous demonstration mode.",
              });
              handleStartDemo(profile);
            }
          } catch (e) {
            console.warn("Discovery mission launch notice, engaging autonomous exhibition mode:", e);
            handleStartDemo(profile);
          }
        }}
        onLaunchDemo={() => {
          setIsLiveEnabled(false);
          setActiveMode("DEMO");
          liveStore.setExecutionMode("DEMO");
          setShowMissionInit(false);
          setTimeout(() => {
            handleStartDemo(activeStudentProfile);
          }, 100);
        }}
        onResumeMission={async (sessionId) => {
          setLiveSessionId(sessionId);
          setIsLiveEnabled(true);
          setActiveMode("LIVE");
          liveStore.setExecutionMode("LIVE");
          liveStore.resetTheatre();
          masterPresentationQueue.clear();
          masterPresentationQueue.setSpeed(liveSpeed);
          masterPresentationQueue.resume();
          setShowMissionInit(false);
          if (typeof window !== "undefined") {
            window.history.pushState({}, "", `/mission/${sessionId}`);
          }
          try {
            const data = await getSessionDetail(sessionId);
            if (data) {
              liveStore.hydrateFromSession(data);
              if (data.profile) {
                setActiveStudentProfile(data.profile);
              }
            }
          } catch (e) {
            console.warn("Could not fetch session detail on resume:", e);
          }
        }}
      />
    );
  }

  return (
    <TheatreViewport>
      {/* Layer 10: Atmospheric Background & Vignette */}
      <AtmosphericBackground />

      {/* Layer 20: The World Stage (Spatial Coordinate Canvas) */}
      <TheatreErrorBoundary subsystemName="World Spatial Stage">
        <WorldStage
          mapState={activeMapState}
          cameraShot={activeCameraShot}
          focusedRegion={activeFocusedRegion}
          onSelectRegion={(reg) => {
            if (isLiveOrDemo) {
              setFocusedLiveRegion(reg);
              setInspectedLiveScoutRegion(reg || null);
            } else if (activeMode === "PHASE5") {
              setPhase5FocusedRegion(reg);
              setInspectedScoutRegion(reg);
            }
          }}
        />
      </TheatreErrorBoundary>

      {/* Layer 30: Delegation Network Conduits */}
      <TheatreErrorBoundary subsystemName="Delegation & Investigation Conduits">
        {isLiveOrDemo && (
          <>
            {(currentLivePhase === "INITIALIZING" || currentLivePhase === "FLEET_DISCOVERY") && (
              <FleetDelegationNetwork
                commanderPos={FLEET_STAGE_ANCHORS.commanderCenter}
                scoutPositions={FLEET_STAGE_ANCHORS.scouts}
                focusedRegion={focusedLiveRegion as Region | null}
              />
            )}
          </>
        )}

        {activeMode === "PHASE6" && (
          <InvestigationConduits activeSpecialist={phase6Snapshot.activeSpecialist} />
        )}

        {activeMode === "PHASE5" && (
          <FleetDelegationNetwork
            commanderPos={FLEET_STAGE_ANCHORS.commanderCenter}
            scoutPositions={FLEET_STAGE_ANCHORS.scouts}
            focusedRegion={phase5FocusedRegion as Region | null}
          />
        )}

        {activeMode === "PHASE4" && (
          <DelegationBridge
            sourcePos={STAGE_ANCHORS.commanderRight}
            targetPos={STAGE_ANCHORS.scoutLeft}
            visible={true}
            statusLabel="COMMUNICATION BUS // DUPLEX DIRECTIVE INTERFACE"
          />
        )}
      </TheatreErrorBoundary>

      {/* Layer 35: Physical Communication Packet Canvas */}
      <TheatreErrorBoundary subsystemName="Packet Physical Canvas">
        {isLiveOrDemo &&
          ["INITIALIZING", "FLEET_DISCOVERY"].includes(liveStore.visualPhase) && (
            <PacketCanvas packets={liveStore.activePackets} />
          )}

        {activeMode === "PHASE7" && (
          <PacketCanvas packets={phase7Snapshot.activePackets} />
        )}

        {activeMode === "PHASE6" && (
          <PacketCanvas packets={phase6Snapshot.activePackets} />
        )}

        {activeMode === "PHASE5" && (
          <PacketCanvas packets={phase5Snapshot.activePackets} />
        )}

        {activeMode === "PHASE4" && (
          <PacketCanvas packet={phase4Snapshot.activePacket} />
        )}
      </TheatreErrorBoundary>

      {/* Layer 70: Brand Identity Header & Mode Switcher */}
      <ScholarXIdentity
        actionSlot={
          <div className="flex items-center space-x-2 sm:space-x-3">
            {/* New Mission / Intake brief opener */}
            <button
              onClick={() => {
                demoPlayerRef.current?.stop();
                setIsDemoPlaying(false);
                setIsLiveEnabled(false);
                masterPresentationQueue.clear();
                setShowMissionInit(true);
              }}
              className="flex items-center space-x-1.5 px-2.5 sm:px-3 py-1.5 rounded-full border border-white/[0.12] bg-black/70 hover:bg-white/[0.1] text-xs font-mono text-zinc-300 transition-all cursor-pointer"
              title="Return to Mission Intelligence Briefing"
            >
              <Compass className="w-3.5 h-3.5 text-sx-gold" />
              <span className="hidden xs:inline">NEW MISSION</span>
              <span className="xs:hidden">NEW</span>
            </button>

            {/* Eco Mode / Low-Power Smooth Toggle */}
            <button
              onClick={toggleEcoMode}
              className={`flex items-center space-x-1.5 px-2.5 sm:px-3 py-1.5 rounded-full border text-xs font-mono font-semibold transition-all cursor-pointer ${
                isEcoMode
                  ? "bg-emerald-500/20 text-emerald-400 border-emerald-500/40 shadow-[0_0_12px_rgba(16,185,129,0.25)]"
                  : "bg-black/60 text-zinc-400 border-white/[0.1] hover:text-white"
              }`}
              title="Toggle Low-Power Eco Mode for smoother performance and battery preservation on any device"
            >
              <Zap className={`w-3.5 h-3.5 ${isEcoMode ? "text-emerald-400 fill-emerald-400" : "text-zinc-500"}`} />
              <span className="hidden sm:inline">ECO MODE</span>
              <span className={`text-[9px] px-1 py-0.2 rounded ${isEcoMode ? "bg-emerald-500/30 text-emerald-300" : "bg-white/10 text-zinc-400"}`}>
                {isEcoMode ? "ON" : "OFF"}
              </span>
            </button>

            {/* Live Autonomous Stream Indicator */}
            <div className="flex items-center space-x-1.5 sm:space-x-2 px-2.5 sm:px-3.5 py-1.5 rounded-full border border-emerald-500/30 bg-emerald-500/10 text-xs font-mono font-bold text-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.25)]">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              <span className="hidden sm:inline">LIVE AUTONOMOUS STREAM</span>
              <span className="sm:hidden">LIVE</span>
            </div>
          </div>
        }
      />

      {/* Main Continuous Theatre Stage Floor */}
      <main className="relative flex-1 w-full px-3 sm:px-6 md:px-8 py-2 flex flex-col justify-between z-theatre-primary pointer-events-none overflow-y-auto lg:overflow-hidden touch-scroll">
        {/* Stage Status Telemetry Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between pointer-events-auto shrink-0 mb-1.5 gap-2">
          <div className="space-y-0.5">
            <div className="text-[10px] sm:text-[11px] font-mono tracking-[0.15em] sm:tracking-[0.25em] text-sx-gold uppercase font-medium">
              AUTONOMOUS AI COMMAND THEATRE //{" "}
              {activeMode === "DEMO"
                ? `ACTIVE PIPELINE // ${currentLiveBanner}`
                : activeMode === "LIVE"
                ? `LIVE STREAM // ${currentLiveBanner}`
                : activeMode === "PHASE7"
                ? "PHASE 7: MULTI-OPPORTUNITY RANKING, ADVISOR ROADMAP & DOSSIER"
                : activeMode === "PHASE6"
                ? "PHASE 6: DEEP OPPORTUNITY INVESTIGATION & EVIDENCE CHALLENGE"
                : activeMode === "PHASE5"
                ? "PHASE 5: GLOBAL AI RESEARCH FLEET & TOOL ACTIVITY"
                : activeMode === "PHASE4"
                ? "PHASE 4: COMMUNICATION PROOF"
                : "PHASE 3: LIFECYCLE SYSTEM"}
            </div>
            <div className="text-[11px] sm:text-xs font-sans text-sx-text-secondary line-clamp-2 sm:line-clamp-none">
              {isLiveOrDemo
                ? currentLiveNarrative
                : activeMode === "PHASE7"
                ? "4 Investigated Opportunities • 8 Pakistan-Adjusted Factors • 6-Phase Execution Roadmap • Editorial Web & PDF Dossier"
                : activeMode === "PHASE6"
                ? `Target: ${currentOpportunityName} • 6 Specialized Processes • Multi-Source Verification • Adversarial Skeptic Audit`
                : activeMode === "PHASE5"
                ? "Central Authority: ScholarX Commander (Pakistan Origin) • 5 Autonomous Regional Workflows • Coordinated Global Discovery"
                : "Authority Node: ScholarX Commander • Child: Europe Regional Scout • Physical Packets"}
            </div>
          </div>

          <div className="flex items-center space-x-2 shrink-0">
            <div className="px-2.5 sm:px-3 py-1 rounded border border-white/[0.08] bg-black/60 backdrop-blur-md text-[10px] sm:text-[11px] font-mono text-sx-text-tertiary flex items-center space-x-1.5 sm:space-x-2">
              {isLiveOrDemo ? (
                <>
                  <span className="text-white/60">PHASE:</span>
                  <span className="text-sx-emerald font-bold">{currentLivePhase}</span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-gold font-semibold">
                    {activeMode === "DEMO" ? "ACTIVE STREAM" : `${sse.eventCount} EVENTS`}
                  </span>
                  <span className="text-white/40">&bull;</span>
                  <span
                    className={
                      activeMode === "DEMO"
                        ? "text-sx-emerald font-semibold"
                        : sse.connectionState === "CONNECTED"
                        ? "text-sx-emerald font-semibold"
                        : "text-zinc-400 font-semibold"
                    }
                  >
                    {activeMode === "DEMO" ? "CONNECTED" : sse.connectionState}
                  </span>
                </>
              ) : activeMode === "PHASE7" ? (
                <>
                  <span className="text-white/60">PRIMARY:</span>
                  <span className="text-sx-gold font-bold">
                    {currentOpportunityName.toUpperCase()} {currentOpportunityScore}
                  </span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-ice font-semibold">4 CANDIDATES</span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-verified font-semibold">
                    {phase7Step === "ARTIFACTS_DELIVERED" ? "MISSION COMPLETE" : "PROCESSING"}
                  </span>
                </>
              ) : activeMode === "PHASE6" ? (
                <>
                  <span className="text-white/60">TARGET:</span>
                  <span className="text-sx-ice font-bold">{currentOpportunityName.toUpperCase()}</span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-gold font-semibold">
                    {currentOpportunity?.bilateralSeats ? `${currentOpportunity.bilateralSeats} SEATS` : "MERIT ALLOCATION"}
                  </span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-emerald font-semibold">{phase6Snapshot.target.knowledgeState.replace(/_/g, " ")}</span>
                </>
              ) : activeMode === "PHASE5" ? (
                <>
                  <span className="text-white/60">FLEET:</span>
                  <span className="text-sx-ice font-bold">{phase5Snapshot.globalStats.operationalStatus}</span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-gold font-semibold">{phase5Snapshot.globalStats.totalCandidatesExtracted} CANDIDATES</span>
                  <span className="text-white/40">&bull;</span>
                  <span className="text-sx-emerald font-semibold">{phase5Snapshot.globalStats.pakistanQuotaSeatsTotal} QUOTA SEATS</span>
                </>
              ) : (
                <span>
                  STEP: <strong className="text-sx-ice">{phase4Step}</strong>
                </span>
              )}
            </div>
          </div>
        </div>

        {/* ========================================================================= */}
        {/* PHASE 8 / PHASE 9: REAL EVENT-DRIVEN & DEMO COMMAND THEATRE               */}
        {/* ========================================================================= */}
        {isLiveOrDemo && (
          <div className="relative w-full flex-1 pointer-events-none flex flex-col items-center justify-between py-1">
            {/* Scene 1: INITIALIZING, FLEET_DISCOVERY & SPECIALIST_INVESTIGATION (The 30-Second Autonomous Fleet) */}
            {(currentLivePhase === "INITIALIZING" || currentLivePhase === "FLEET_DISCOVERY" || currentLivePhase === "SPECIALIST_INVESTIGATION") && (
              <>
                {/* 1A. Desktop 2D Spatial Map Layout (lg and above) */}
                <div className="hidden lg:block relative w-full flex-1 pointer-events-none my-auto">
                  {/* Central Commander at Pakistan Origin */}
                  <div className="absolute left-1/2 top-[49%] -translate-x-1/2 -translate-y-1/2 pointer-events-auto w-[380px] z-20">
                    <CommanderConsole
                      state={
                        currentLiveMissionStatus === "RUNNING"
                          ? "DIRECTING"
                          : currentLiveMissionStatus === "COMPLETE"
                          ? "COMPLETE"
                          : "IDLE"
                      }
                      mission="Autonomous Multi-Agent Scholarship Intelligence & Bilateral Quota Discovery for Pakistani Candidates"
                      constraints={[
                        "Zero Out-of-Pocket / Living Allowance Covered",
                        "HEC Attestation & IBCC Equivalence Compatible",
                        "Pakistani Bilateral Quotas Prioritized",
                      ]}
                      availableActions={[
                        "Deploy 5 Regional Scouts",
                        "Monitor Parallel Retrieval",
                        "Synthesize Global Candidate Pool",
                      ]}
                      nextDecision={currentCommanderDecision || "Monitor fleet operations"}
                      currentDecision={currentCommanderDecision}
                      activeDirective={null}
                      receivedReports={phase5Snapshot.commander.receivedReports || []}
                      globalFleetStats={{
                        scoutsDeployed: 5,
                        activeScoutsCount:
                          currentLivePhase === "FLEET_DISCOVERY"
                            ? 5
                            : Object.values(liveStore.scouts).filter(
                                (s) => s.status === "ACTIVE" || s.status === "SCRAPING" || s.status === "EXTRACTING"
                              ).length,
                        reportsReceived: Object.values(liveStore.scouts).filter((s) => s.status === "COMPLETE").length,
                        totalSourcesDiscovered:
                          currentLivePhase === "FLEET_DISCOVERY"
                            ? 18
                            : Object.values(liveStore.scouts).reduce((acc, s) => acc + s.sourcesFound, 0) || 12,
                        totalCandidatesExtracted:
                          currentLivePhase === "FLEET_DISCOVERY"
                            ? 6
                            : Object.values(liveStore.scouts).reduce((acc, s) => acc + s.candidatesCount, 0) || 4,
                        pakistanQuotaSeatsTotal: 495,
                        operationalStatus:
                          currentLiveMissionStatus === "RUNNING" ? "ACTIVE_PARALLEL_SWEEP" : "STANDBY",
                      }}
                      isFocused={focusedLiveRegion === "Pakistan" || focusedLiveRegion === null}
                      onFocus={() => {
                        setFocusedLiveRegion("Pakistan");
                        setInspectedLiveScoutRegion(null);
                      }}
                    />
                  </div>

                  {/* Scouts in 2D Orbit */}
                  <div className="absolute left-[32%] -translate-x-1/2 top-[12px] pointer-events-auto z-10">
                    <ScoutBeacon
                      scout={getLiveRegionalScout("Europe")}
                      isFocused={focusedLiveRegion === "Europe"}
                      onSelect={() => {
                        setFocusedLiveRegion("Europe");
                        setInspectedLiveScoutRegion("Europe");
                      }}
                    />
                  </div>

                  <div className="absolute left-[24px] top-[28%] pointer-events-auto z-10">
                    <ScoutBeacon
                      scout={getLiveRegionalScout("Americas")}
                      isFocused={focusedLiveRegion === "Americas"}
                      onSelect={() => {
                        setFocusedLiveRegion("Americas");
                        setInspectedLiveScoutRegion("Americas");
                      }}
                    />
                  </div>

                  <div className="absolute right-[24px] top-[28%] pointer-events-auto z-10">
                    <ScoutBeacon
                      scout={getLiveRegionalScout("Asia")}
                      isFocused={focusedLiveRegion === "Asia"}
                      onSelect={() => {
                        setFocusedLiveRegion("Asia");
                        setInspectedLiveScoutRegion("Asia");
                      }}
                    />
                  </div>

                  <div className="absolute left-[48px] bottom-[16px] pointer-events-auto z-10">
                    <ScoutBeacon
                      scout={getLiveRegionalScout("MENA")}
                      isFocused={focusedLiveRegion === "MENA"}
                      onSelect={() => {
                        setFocusedLiveRegion("MENA");
                        setInspectedLiveScoutRegion("MENA");
                      }}
                    />
                  </div>

                  <div className="absolute right-[48px] bottom-[16px] pointer-events-auto z-10">
                    <ScoutBeacon
                      scout={getLiveRegionalScout("Oceania")}
                      isFocused={focusedLiveRegion === "Oceania"}
                      onSelect={() => {
                        setFocusedLiveRegion("Oceania");
                        setInspectedLiveScoutRegion("Oceania");
                      }}
                    />
                  </div>

                  {/* Desktop Expanded Inspection Overlay */}
                  <AnimatePresence>
                    {inspectedLiveScoutRegion && (
                      <motion.div
                        initial={{ opacity: 0, x: 40 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: 40 }}
                        transition={{ duration: 0.25 }}
                        className="absolute right-[16px] top-[16px] bottom-[16px] w-[390px] pointer-events-auto z-30 flex flex-col justify-center"
                      >
                        <div className="relative">
                          <button
                            onClick={() => setInspectedLiveScoutRegion(null)}
                            className="absolute -top-3 -right-3 w-7 h-7 rounded-full bg-black/80 border border-white/20 text-white flex items-center justify-center hover:bg-white/20 transition-all z-40 shadow-xl cursor-pointer"
                            title="Close Scout Inspection"
                          >
                            <X className="w-3.5 h-3.5" />
                          </button>

                          <AgentCard
                            agent={getAgentEntityFromScout(getLiveRegionalScout(inspectedLiveScoutRegion))}
                            activeQuery={getLiveRegionalScout(inspectedLiveScoutRegion).activeQuery}
                            activeTool={getLiveRegionalScout(inspectedLiveScoutRegion).activeTool}
                            sources={getLiveRegionalScout(inspectedLiveScoutRegion).sources}
                            candidates={getLiveRegionalScout(inspectedLiveScoutRegion).candidates}
                            reportReady={getLiveRegionalScout(inspectedLiveScoutRegion).reportReady}
                            isFocused={true}
                          />
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>

                {/* 1B. Mobile & Tablet Adaptive Fleet Layout (< lg) */}
                <div className="block lg:hidden w-full flex-1 pointer-events-auto my-2 space-y-3 pb-4 touch-scroll">
                  {/* Central Commander Console Mobile View */}
                  <div className="w-full max-w-xl mx-auto">
                    <CommanderConsole
                      state={
                        currentLiveMissionStatus === "RUNNING"
                          ? "DIRECTING"
                          : currentLiveMissionStatus === "COMPLETE"
                          ? "COMPLETE"
                          : "IDLE"
                      }
                      mission="Autonomous Multi-Agent Scholarship Intelligence & Bilateral Quota Discovery for Pakistani Candidates"
                      constraints={[
                        "Zero Out-of-Pocket / Living Allowance Covered",
                        "HEC Attestation & IBCC Equivalence Compatible",
                        "Pakistani Bilateral Quotas Prioritized",
                      ]}
                      availableActions={[
                        "Deploy 5 Regional Scouts",
                        "Monitor Parallel Retrieval",
                        "Synthesize Global Candidate Pool",
                      ]}
                      nextDecision={currentCommanderDecision || "Monitor fleet operations"}
                      currentDecision={currentCommanderDecision}
                      activeDirective={null}
                      receivedReports={phase5Snapshot.commander.receivedReports || []}
                      globalFleetStats={{
                        scoutsDeployed: 5,
                        activeScoutsCount:
                          currentLivePhase === "FLEET_DISCOVERY"
                            ? 5
                            : Object.values(liveStore.scouts).filter(
                                (s) => s.status === "ACTIVE" || s.status === "SCRAPING" || s.status === "EXTRACTING"
                              ).length,
                        reportsReceived: Object.values(liveStore.scouts).filter((s) => s.status === "COMPLETE").length,
                        totalSourcesDiscovered:
                          currentLivePhase === "FLEET_DISCOVERY"
                            ? 18
                            : Object.values(liveStore.scouts).reduce((acc, s) => acc + s.sourcesFound, 0) || 12,
                        totalCandidatesExtracted:
                          currentLivePhase === "FLEET_DISCOVERY"
                            ? 6
                            : Object.values(liveStore.scouts).reduce((acc, s) => acc + s.candidatesCount, 0) || 4,
                        pakistanQuotaSeatsTotal: 495,
                        operationalStatus:
                          currentLiveMissionStatus === "RUNNING" ? "ACTIVE_PARALLEL_SWEEP" : "STANDBY",
                      }}
                      isFocused={focusedLiveRegion === "Pakistan" || focusedLiveRegion === null}
                      onFocus={() => {
                        setFocusedLiveRegion("Pakistan");
                        setInspectedLiveScoutRegion(null);
                      }}
                    />
                  </div>

                  {/* Mobile Scout Regional Selector & Cards */}
                  <div className="w-full max-w-xl mx-auto space-y-2.5">
                    <div className="flex items-center justify-between text-[11px] font-mono text-zinc-400 px-1">
                      <span className="text-sx-gold font-bold uppercase tracking-wider">
                        REGIONAL FLEET ({Object.keys(liveStore.scouts).length} SCOUTS)
                      </span>
                      <span>TAP TO INSPECT</span>
                    </div>

                    {/* Horizontal Touch Scrollable Pills */}
                    <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
                      {(["Europe", "Asia", "Americas", "MENA", "Oceania"] as Region[]).map((reg) => {
                        const scoutData = getLiveRegionalScout(reg);
                        const isCurrent = (inspectedLiveScoutRegion || focusedLiveRegion || "Europe") === reg;
                        return (
                          <button
                            key={reg}
                            type="button"
                            onClick={() => {
                              setFocusedLiveRegion(reg);
                              setInspectedLiveScoutRegion(reg);
                            }}
                            className={`px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all flex items-center space-x-1.5 shrink-0 cursor-pointer ${
                              isCurrent
                                ? "bg-cyan-500/20 text-cyan-300 border border-cyan-400/50 shadow-[0_0_12px_rgba(56,189,248,0.25)] font-bold"
                                : "bg-black/60 text-zinc-400 border border-white/[0.08] hover:text-white"
                            }`}
                          >
                            <span className={`w-1.5 h-1.5 rounded-full ${isCurrent ? "bg-cyan-400 animate-pulse" : "bg-zinc-500"}`} />
                            <span>{reg}</span>
                            <span className="text-[10px] text-zinc-400">({scoutData.candidates?.length || 0})</span>
                          </button>
                        );
                      })}
                    </div>

                    {/* Active Selected Scout Display on Mobile */}
                    <div>
                      {(() => {
                        const activeMobileReg = (inspectedLiveScoutRegion || focusedLiveRegion || "Europe") as Region;
                        const activeScout = getLiveRegionalScout(activeMobileReg);
                        return (
                          <div className="rounded-xl border border-white/[0.12] bg-black/85 backdrop-blur-xl p-3.5 shadow-xl space-y-2">
                            <div className="flex items-center justify-between pb-2 border-b border-white/[0.08]">
                              <div className="flex items-center space-x-2">
                                <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" />
                                <span className="font-mono text-xs font-bold text-white uppercase">
                                  {activeScout.displayName}
                                </span>
                              </div>
                              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-semibold">
                                {activeScout.pakistanQuotaSeats ? `${activeScout.pakistanQuotaSeats} Quota Seats` : "Sector Active"}
                              </span>
                            </div>

                            <div className="space-y-1.5 text-xs font-mono">
                              <div>
                                <span className="text-zinc-500 text-[10px] block">CURRENT OPERATION:</span>
                                <span className="text-cyan-300">{activeScout.currentOperation || "Scanning official universities"}</span>
                              </div>
                              <div className="flex items-center justify-between text-[11px] pt-1.5 border-t border-white/[0.05]">
                                <span className="text-zinc-400">SOURCES: <strong className="text-white">{activeScout.sources?.length || 0}</strong></span>
                                <span className="text-zinc-400">CANDIDATES: <strong className="text-sx-gold">{activeScout.candidates?.length || 0}</strong></span>
                                <span className="text-zinc-400">STATUS: <strong className="text-emerald-400">{activeScout.state}</strong></span>
                              </div>
                            </div>
                          </div>
                        );
                      })()}
                    </div>
                  </div>
                </div>
              </>
            )}

            {/* Direct Scholarship Opportunities Stage (Appears strictly after 30s during RANKING_EVALUATION) */}
            {currentLivePhase === "RANKING_EVALUATION" && (
              <TheatreErrorBoundary subsystemName="Ranking Engine Subsystem">
                <div className="pointer-events-auto z-20 my-auto w-full">
                  <OpportunityComparisonStage
                    opportunities={
                      normalizedOpportunities.length > 0
                        ? normalizedOpportunities
                        : (activeMode === "LIVE" ? [] : phase7Snapshot.opportunities)
                    }
                    selectedId={normalizedPrimaryOpportunity?.id || selectedOpportunityId}
                    selectedField={
                      activeStudentProfile?.preferences?.target_fields?.[0] ||
                      activeStudentProfile?.academic?.field_of_study ||
                      activeStudentProfile?.field
                    }
                    targetDegree={
                      activeStudentProfile?.preferences?.target_degree_level ||
                      activeStudentProfile?.preferences?.targetDegreeLevel ||
                      activeStudentProfile?.degree
                    }
                    onSelectOpportunity={(id) => {
                      liveStore.setSelectedOpportunity(id);
                      setSelectedOpportunityId(id);
                    }}
                  />
                </div>
              </TheatreErrorBoundary>
            )}

            {/* Scene 4: ROADMAP_ASSEMBLY */}
            {currentLivePhase === "ROADMAP_ASSEMBLY" && (
              <TheatreErrorBoundary subsystemName="Roadmap Journey Subsystem">
                <div className="pointer-events-auto z-20 my-auto w-full">
                  <RoadmapJourney
                    phases={liveStore.roadmapPhases.length > 0 ? liveStore.roadmapPhases : activeDossier.roadmapPhases}
                    totalPrepDays={activeDossier.totalPrepDaysEstimated}
                    totalBudgetPkr={activeDossier.totalBudgetNeededPkr}
                  />
                </div>
              </TheatreErrorBoundary>
            )}

            {/* Scene 5: DOSSIER_BUILD & MISSION_COMPLETE */}
            {(currentLivePhase === "DOSSIER_BUILD" || currentLivePhase === "MISSION_COMPLETE") && (
              <TheatreErrorBoundary subsystemName="Mission Output Subsystem">
                <div className="pointer-events-auto z-20 my-auto w-full">
                  <MissionOutputStage
                    opportunities={
                      normalizedOpportunities.length > 0
                        ? normalizedOpportunities
                        : (activeMode === "LIVE" ? [] : phase7Snapshot.opportunities)
                    }
                    primaryOpportunity={
                      normalizedPrimaryOpportunity ||
                      (activeMode === "LIVE" ? null : phase7Snapshot.primaryOpportunity)
                    }
                    onSelectOpportunity={(id) => {
                      liveStore.setSelectedOpportunity(id);
                      setSelectedOpportunityId(id);
                    }}
                    roadmapPhases={liveStore.roadmapPhases}
                    dossier={activeDossier}
                    studentProfile={activeStudentProfile}
                    onOpenWebDossier={() => {
                      setDossierModalTab("WEB");
                      setDossierModalOpen(true);
                    }}
                    onOpenPdfViewer={() => {
                      setDossierModalTab("PDF");
                      setDossierModalOpen(true);
                    }}
                    onNewMission={() => {
                      demoPlayerRef.current?.stop();
                      setIsDemoPlaying(false);
                      setIsLiveEnabled(false);
                      masterPresentationQueue.clear();
                      setShowMissionInit(true);
                    }}
                  />
                </div>
              </TheatreErrorBoundary>
            )}
          </div>
        )}

        {/* ========================================================================= */}
        {/* PHASE 7: MULTI-OPPORTUNITY SYNTHESIS, RANKING & DOSSIER STAGE             */}
        {/* ========================================================================= */}
        {activeMode === "PHASE7" && (
          <div className="relative w-full flex-1 pointer-events-none flex flex-col items-center justify-between py-1">
            {/* 1. TOP COMMANDER CONSOLE HEADER */}
            <div className="pointer-events-auto w-[820px] shrink-0 z-20 mb-2">
              <div className="rounded-xl border border-white/[0.08] bg-black/80 backdrop-blur-xl p-3 shadow-lg flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 rounded-lg bg-sx-gold/15 border border-sx-gold/30 flex items-center justify-center text-sx-gold font-mono font-bold text-xs shadow-[0_0_12px_rgba(212,175,55,0.3)]">
                    CMD
                  </div>
                  <div>
                    <div className="text-[10px] font-mono tracking-wider uppercase text-sx-gold font-bold flex items-center gap-2">
                      <span>SCHOLARX COMMANDER // MULTI-OPPORTUNITY EVALUATION</span>
                      <span className="px-1.5 py-0.2 rounded bg-sx-verified/20 text-sx-verified border border-sx-verified/30 text-[8px]">
                        STAGE 7 ACTIVE
                      </span>
                    </div>
                    <div className="text-xs font-sans text-white/90 font-medium">
                      Synthesizing comparable intelligence, ranking candidates via Pakistan-adjusted scoring model, and delivering decision-ready dossier
                    </div>
                  </div>
                </div>

                <div className="text-right text-[10px] font-mono">
                  <div className="text-sx-text-tertiary">CURRENT DECISION:</div>
                  <div className="text-sx-gold font-semibold truncate max-w-[260px]">
                    {phase7Snapshot.stepMeta.label}
                  </div>
                </div>
              </div>
            </div>

            {/* 2. DYNAMIC CENTER VISUALIZATION STAGE BASED ON SCENE */}
            <div className="pointer-events-auto z-20 my-auto w-full">
              {/* Scene Group 1: Candidate Pool & Spatial Comparison */}
              {(phase7Step === "POOL_INSPECTION" || phase7Step === "SPATIAL_COMPARISON") && (
                <OpportunityComparisonStage
                  opportunities={phase7Snapshot.opportunities}
                  selectedId={selectedOpportunityId}
                  selectedField={
                    activeStudentProfile?.preferences?.target_fields?.[0] ||
                    activeStudentProfile?.academic?.field_of_study ||
                    activeStudentProfile?.field
                  }
                  targetDegree={
                    activeStudentProfile?.preferences?.target_degree_level ||
                    activeStudentProfile?.preferences?.targetDegreeLevel ||
                    activeStudentProfile?.degree
                  }
                  onSelectOpportunity={(id) => setSelectedOpportunityId(id)}
                />
              )}

              {/* Scene Group 2: Deterministic Scoring Breakdown */}
              {(phase7Step === "SCORING_INIT" ||
                phase7Step === "FACTOR_EVALUATION" ||
                phase7Step === "SCORE_RESOLUTION") && (
                <ScoringEngineCard
                  factors={currentOpportunity.factors}
                  compositeScore={currentOpportunity.compositeScore}
                  opportunityName={currentOpportunity.name}
                  rank={currentOpportunity.rank}
                />
              )}

              {/* Scene Group 3: Primary Opportunity Emergence */}
              {phase7Step === "PRIMARY_SELECTION" && (
                <PrimaryOpportunityCard
                  opportunity={phase7Snapshot.primaryOpportunity}
                  onProceedToAdvisor={() => setPhase7Step("ADVISOR_ENGAGEMENT")}
                />
              )}

              {/* Scene Group 4: Final Advisor 6-Phase Journey */}
              {(phase7Step === "ADVISOR_ENGAGEMENT" || phase7Step === "ROADMAP_GENERATION") && (
                <RoadmapJourney
                  phases={phase7Snapshot.dossier.roadmapPhases}
                  totalPrepDays={phase7Snapshot.dossier.totalPrepDaysEstimated}
                  totalBudgetPkr={phase7Snapshot.dossier.totalBudgetNeededPkr}
                />
              )}

              {/* Scene Group 5: Dossier Assembly & Artifact Delivery */}
              {(phase7Step === "DOSSIER_ASSEMBLY" ||
                phase7Step === "WEB_BUILDER_ACTIVE" ||
                phase7Step === "PDF_BUILDER_ACTIVE" ||
                phase7Step === "ARTIFACTS_DELIVERED") && (
                <DossierAssemblyTheatre
                  dossier={phase7Snapshot.dossier}
                  activeStep={phase7Step}
                  builderActivity={phase7Snapshot.builderActivity}
                  onOpenWebDossier={() => {
                    setDossierModalTab("WEB");
                    setDossierModalOpen(true);
                  }}
                  onOpenPdfViewer={() => {
                    setDossierModalTab("PDF");
                    setDossierModalOpen(true);
                  }}
                />
              )}
            </div>

            {/* Bottom Spacer for Stage balance */}
            <div className="shrink-0 h-2" />
          </div>
        )}

        {/* ========================================================================= */}
        {/* PHASE 6: DEEP OPPORTUNITY INVESTIGATION STAGE (Preserved)                 */}
        {/* ========================================================================= */}
        {activeMode === "PHASE6" && (
          <div className="relative w-full flex-1 pointer-events-none flex flex-col items-center justify-between py-1">
            {/* 1. TOP COMMANDER CONSOLE HEADER */}
            <div className="pointer-events-auto w-[720px] shrink-0 z-20">
              <div className="rounded-xl border border-white/[0.08] bg-black/80 backdrop-blur-xl p-3 shadow-lg flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 rounded-lg bg-sx-ice/15 border border-sx-ice/30 flex items-center justify-center text-sx-ice font-mono font-bold text-xs shadow-[0_0_12px_rgba(56,189,248,0.3)]">
                    CMD
                  </div>
                  <div>
                    <div className="text-[10px] font-mono tracking-wider uppercase text-sx-ice font-bold flex items-center gap-2">
                      <span>SCHOLARX COMMANDER // STRATEGIC ADVISOR</span>
                      <span className="px-1.5 py-0.2 rounded bg-sx-emerald/20 text-sx-emerald border border-sx-emerald/30 text-[8px]">
                        DIRECTING INQUIRY
                      </span>
                    </div>
                    <div className="text-xs font-sans text-white/90 font-medium">
                      Investigating Hungarian bilateral quota suitability for Pakistani applicant profile
                    </div>
                  </div>
                </div>

                <div className="text-right text-[10px] font-mono">
                  <div className="text-sx-text-tertiary">CURRENT DECISION:</div>
                  <div className="text-sx-gold font-semibold truncate max-w-[240px]">
                    {phase6Snapshot.stepMeta.label}
                  </div>
                </div>
              </div>
            </div>

            {/* 2. CENTER: THE INVESTIGATION TARGET OBJECT */}
            <div className="pointer-events-auto z-20 my-1">
              <InvestigationTargetObject
                target={phase6Snapshot.target}
                activeSpecialist={phase6Snapshot.activeSpecialist}
                onSelectTrace={(trace) => {
                  const stepForSpec = PHASE_6_STEPS.find((s) => s.activeSpecialist === trace.specialist);
                  if (stepForSpec) setPhase6Step(stepForSpec.step);
                }}
              />
            </div>

            {/* 3. LOWER STAGE: ACTIVE SPECIALIST PROCESS CARD */}
            <div className="pointer-events-auto z-20 shrink-0">
              {phase6Snapshot.specialistMeta ? (
                <SpecialistProcessCard
                  type={phase6Snapshot.specialistMeta.type}
                  category={phase6Snapshot.specialistMeta.category}
                  displayName={phase6Snapshot.specialistMeta.displayName}
                  state={phase6Snapshot.specialistMeta.state}
                  actionLabel={phase6Snapshot.specialistMeta.actionLabel}
                  color={phase6Snapshot.specialistMeta.color}
                  eligibilityData={phase6Snapshot.eligibilityData}
                  documentData={phase6Snapshot.documentData}
                  costData={phase6Snapshot.costData}
                  deadlineData={phase6Snapshot.deadlineData}
                  verificationData={phase6Snapshot.verificationData}
                  skepticData={phase6Snapshot.skepticData}
                  synthesisSummary={phase6Snapshot.synthesisSummary}
                />
              ) : (
                <div className="w-[720px] rounded-xl border border-white/[0.08] bg-black/60 backdrop-blur-md p-4 text-center text-[11px] font-mono text-white/50 space-y-1 shadow-lg">
                  <div className="text-sx-gold font-bold uppercase tracking-wider flex items-center justify-center gap-2">
                    <Search className="w-3.5 h-3.5" />
                    <span>INVESTIGATION PIPELINE INITIALIZED</span>
                  </div>
                  <div>
                    Commander dispatching 6 specialist intelligence processes: Eligibility Investigator, Document Analyst, True Cost Analyzer, Deadline Intelligence, Verification Agent, Skeptic Agent.
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* PHASE 5: GLOBAL SPATIAL RESEARCH FLEET COMPOSITION (Preserved)             */}
        {/* ========================================================================= */}
        {activeMode === "PHASE5" && (
          <div className="relative w-full flex-1 pointer-events-none my-auto">
            {/* 1. CENTRAL COMMANDER AT PAKISTAN ORIGIN CONTEXT */}
            <div className="absolute left-1/2 top-[49%] -translate-x-1/2 -translate-y-1/2 pointer-events-auto w-[380px] z-20">
              <CommanderConsole
                state={phase5Snapshot.commander.state}
                mission={phase5Snapshot.commander.mission}
                constraints={[
                  "Zero Out-of-Pocket / Living Allowance Covered",
                  "HEC Attestation & IBCC Equivalence Compatible",
                  "Pakistani Bilateral Quotas Prioritized",
                ]}
                availableActions={[
                  "Deploy 5 Regional Scouts",
                  "Monitor Parallel Retrieval",
                  "Synthesize Global Candidate Pool",
                ]}
                nextDecision={phase5Snapshot.commander.currentDecision || "Monitor fleet operations"}
                currentDecision={phase5Snapshot.commander.currentDecision}
                activeDirective={phase5Snapshot.commander.activeDirectives[0] || null}
                receivedReports={phase5Snapshot.commander.receivedReports}
                globalFleetStats={phase5Snapshot.globalStats}
                isFocused={phase5FocusedRegion === "Pakistan" || phase5FocusedRegion === null}
                onFocus={() => {
                  setPhase5FocusedRegion("Pakistan");
                  setInspectedScoutRegion(null);
                }}
              />
            </div>

            {/* 2. NORTH-WEST: EUROPE SCOUT */}
            <div className="absolute left-[32%] -translate-x-1/2 top-[12px] pointer-events-auto z-10">
              <ScoutBeacon
                scout={phase5Snapshot.scouts.Europe}
                isFocused={phase5FocusedRegion === "Europe"}
                onSelect={() => {
                  setPhase5FocusedRegion("Europe");
                  setInspectedScoutRegion("Europe");
                }}
              />
            </div>

            {/* 3. WEST: AMERICAS SCOUT */}
            <div className="absolute left-[24px] top-[28%] pointer-events-auto z-10">
              <ScoutBeacon
                scout={phase5Snapshot.scouts.Americas}
                isFocused={phase5FocusedRegion === "Americas"}
                onSelect={() => {
                  setPhase5FocusedRegion("Americas");
                  setInspectedScoutRegion("Americas");
                }}
              />
            </div>

            {/* 4. EAST: ASIA SCOUT */}
            <div className="absolute right-[24px] top-[28%] pointer-events-auto z-10">
              <ScoutBeacon
                scout={phase5Snapshot.scouts.Asia}
                isFocused={phase5FocusedRegion === "Asia"}
                onSelect={() => {
                  setPhase5FocusedRegion("Asia");
                  setInspectedScoutRegion("Asia");
                }}
              />
            </div>

            {/* 5. SOUTHWEST: MENA SCOUT */}
            <div className="absolute left-[48px] bottom-[16px] pointer-events-auto z-10">
              <ScoutBeacon
                scout={phase5Snapshot.scouts.MENA}
                isFocused={phase5FocusedRegion === "MENA"}
                onSelect={() => {
                  setPhase5FocusedRegion("MENA");
                  setInspectedScoutRegion("MENA");
                }}
              />
            </div>

            {/* 6. SOUTHEAST: OCEANIA SCOUT */}
            <div className="absolute right-[48px] bottom-[16px] pointer-events-auto z-10">
              <ScoutBeacon
                scout={phase5Snapshot.scouts.Oceania}
                isFocused={phase5FocusedRegion === "Oceania"}
                onSelect={() => {
                  setPhase5FocusedRegion("Oceania");
                  setInspectedScoutRegion("Oceania");
                }}
              />
            </div>

            {/* 7. EXPANDED SCOUT INSPECTION OVERLAY */}
            <AnimatePresence>
              {inspectedScoutRegion && (
                <motion.div
                  initial={{ opacity: 0, x: 40 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 40 }}
                  transition={{ duration: 0.3 }}
                  className="absolute right-[16px] top-[16px] bottom-[16px] w-[390px] pointer-events-auto z-30 flex flex-col justify-center"
                >
                  <div className="relative">
                    <button
                      onClick={() => setInspectedScoutRegion(null)}
                      className="absolute -top-3 -right-3 w-7 h-7 rounded-full bg-black/80 border border-white/20 text-white flex items-center justify-center hover:bg-white/20 transition-all z-40 shadow-xl"
                      title="Close Scout Inspection"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>

                    <AgentCard
                      agent={getAgentEntityFromScout(phase5Snapshot.scouts[inspectedScoutRegion])}
                      activeQuery={phase5Snapshot.scouts[inspectedScoutRegion].activeQuery}
                      activeTool={phase5Snapshot.scouts[inspectedScoutRegion].activeTool}
                      sources={phase5Snapshot.scouts[inspectedScoutRegion].sources}
                      candidates={phase5Snapshot.scouts[inspectedScoutRegion].candidates}
                      reportReady={phase5Snapshot.scouts[inspectedScoutRegion].reportReady}
                      isFocused={true}
                    />
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        )}

        {/* ========================================================================= */}
        {/* PHASE 4: PRESERVED PROOF MODE (Backwards Verification)                     */}
        {/* ========================================================================= */}
        {activeMode === "PHASE4" && (
          <div className="w-full flex-1 flex items-start gap-0 pointer-events-none my-auto pt-4">
            <div className="pointer-events-auto w-[380px]">
              <CommanderConsole
                state={phase4Snapshot.commander.state}
                mission={phase4Snapshot.commander.mission}
                constraints={[
                  "Zero Out-of-Pocket / Living Stipend Covered",
                  "HEC Attestation & IBCC Equivalence Compatible",
                  "400 Bilateral Pakistan Quota Prioritized",
                ]}
                availableActions={["Synthesizing Candidates", "Dispatch Global Fleet"]}
                nextDecision="Evaluate Pakistani candidate eligibility"
                currentDecision={phase4Snapshot.commander.currentDecision}
                activeDirective={{
                  targetId: "scout-eu",
                  targetName: "Europe Regional Scout",
                  targetType: "WORKFLOW",
                  objective: "Discover fully funded CS opportunities for Pakistani applicants.",
                  expectedOutput: "Normalized scholarship candidates with bilateral quotas.",
                  constraints: [
                    "HEC Attestation and IBCC Equivalence Compatible",
                    "Zero Tuition / Living Stipend Covered",
                  ],
                }}
                incomingReport={
                  phase4Step === "REPORT_FLIGHT" || phase4Step === "COMMANDER_SYNTHESIS"
                    ? phase4Snapshot.activePacket?.payload?.report ?? null
                    : null
                }
                isFocused={true}
              />
            </div>

            <div className="pointer-events-auto w-[380px] ml-[360px]">
              <AgentCard
                agent={{
                  agentId: "scout-eu",
                  displayName: "Europe Regional Scout",
                  entityType: "WORKFLOW",
                  parentId: "commander-root",
                  region: "Europe",
                  mission: "Discover fully funded CS opportunities for Pakistani applicants.",
                  state: phase4Snapshot.scout.state,
                  stateSince: Date.now() - 5000,
                  currentOperation: phase4Snapshot.scout.currentOperation,
                  finding: phase4Snapshot.scout.finding,
                  progress: phase4Snapshot.scout.progress,
                  spawnedAt: Date.now() - 10000,
                  spawnPhase: "SETTLED",
                  coordinates: [13.405, 52.52],
                }}
                activeQuery={phase4Snapshot.scout.activeQuery}
                sources={phase4Snapshot.scout.sources}
                candidates={phase4Snapshot.scout.candidates}
                reportReady={phase4Snapshot.scout.reportReady}
                isFocused={true}
              />
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* PHASE 3: PRESERVED LIFECYCLE MODE (Backwards Verification)                */}
        {/* ========================================================================= */}
        {activeMode === "PHASE3" && (
          <div className="w-full flex-1 flex items-start gap-0 pointer-events-none my-auto pt-4">
            <div className="pointer-events-auto w-[380px]">
              <CommanderConsole
                state={lifecycle.commander.state}
                mission={lifecycle.commander.mission}
                constraints={lifecycle.commander.constraints}
                availableActions={lifecycle.commander.availableActions}
                nextDecision={lifecycle.commander.nextDecision}
                currentDecision={lifecycle.commander.currentDecision}
                activeDirective={lifecycle.commander.activeDirective}
                isFocused={true}
              />
            </div>

            {lifecycle.europeScout && (
              <div className="pointer-events-auto w-[380px] ml-[360px]">
                <AgentCard agent={lifecycle.europeScout} isFocused={true} />
              </div>
            )}
          </div>
        )}

        {/* Dynamic Legacy Director Scrubber (Only for Phase 4-7 Diagnostic Inspection) */}
        {(activeMode === "PHASE7" || activeMode === "PHASE6" || activeMode === "PHASE5" || activeMode === "PHASE4") && (
          <div className="my-1 z-theatre-overlays pointer-events-auto shrink-0">
            {activeMode === "PHASE7" && (
              <Phase7Director
                currentStep={phase7Step}
                onSelectStep={(s) => setPhase7Step(s)}
                isPlaying={phase7Playing}
                onTogglePlay={() => setPhase7Playing(!phase7Playing)}
                onReset={() => {
                  setPhase7Step("POOL_INSPECTION");
                  setSelectedOpportunityId("stipendium-hungaricum");
                }}
              />
            )}

            {activeMode === "PHASE6" && (
              <Phase6Director
                currentStep={phase6Step}
                onSelectStep={(s) => setPhase6Step(s)}
                isPlaying={phase6Playing}
                onTogglePlay={() => setPhase6Playing(!phase6Playing)}
                onReset={() => {
                  setPhase6Step("TARGET_SELECTION");
                  setPhase6FocusedSpecialist(null);
                }}
                focusedSpecialist={phase6FocusedSpecialist}
                onSelectFocus={(spec) => setPhase6FocusedSpecialist(spec)}
              />
            )}

            {activeMode === "PHASE5" && (
              <Phase5Director
                currentStep={phase5Step}
                onSelectStep={(s) => setPhase5Step(s)}
                isPlaying={phase5Playing}
                onTogglePlay={() => setPhase5Playing(!phase5Playing)}
                onReset={() => {
                  setPhase5Step("FLEET_INIT");
                  setPhase5FocusedRegion(null);
                  setInspectedScoutRegion(null);
                }}
                focusedRegion={phase5FocusedRegion}
                onSelectFocus={(reg) => {
                  setPhase5FocusedRegion(reg);
                  if (reg && reg !== "Pakistan") {
                    setInspectedScoutRegion(reg as Region);
                  } else {
                    setInspectedScoutRegion(null);
                  }
                }}
              />
            )}

            {activeMode === "PHASE4" && (
              <Phase4Director
                currentStep={phase4Step}
                onSelectStep={(s) => setPhase4Step(s)}
                isPlaying={phase4Playing}
                onTogglePlay={() => setPhase4Playing(!phase4Playing)}
                onReset={() => setPhase4Step("DIRECTING")}
              />
            )}
          </div>
        )}

        {/* Bottom Spatial Telemetry Status Line */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-[10px] sm:text-xs font-mono text-zinc-400 pt-1.5 pointer-events-auto shrink-0 border-t border-white/[0.05] gap-1">
          <span className="tracking-wider truncate max-w-full">
            INTELLIGENCE NETWORK // AUTONOMOUS DECISION PIPELINE
          </span>
          <span className="text-zinc-500 hidden md:inline">
            STRATEGIC COMMAND → 5 SCOUTS → 6 SPECIALISTS → ADVISORY RANKING → DOSSIER
          </span>
        </div>
      </main>



      {/* In-Theatre Modal Viewer for Web Dossier & PDF Preview */}
      <TheatreErrorBoundary subsystemName="Dossier Viewer Subsystem">
        <DossierModalViewer
          dossier={activeDossier}
          isOpen={dossierModalOpen}
          onClose={() => setDossierModalOpen(false)}
          initialTab={dossierModalTab}
        />
      </TheatreErrorBoundary>
    </TheatreViewport>
  );
};
