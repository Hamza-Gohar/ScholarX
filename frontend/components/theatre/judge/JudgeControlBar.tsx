"use client";

import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Play,
  Pause,
  RotateCcw,
  FileText,
  Printer,
  Download,
  ChevronDown,
  ChevronUp,
  Layers,
  User,
  ShieldAlert,
  Radio,
  Activity,
  CheckCircle2,
  AlertCircle,
  HelpCircle,
  X,
} from "lucide-react";
import { DEMO_STAGES_LIST } from "@/lib/theatre/snapshots";
import { DEMO_PROFILES, DemoProfileId, DemoScenario } from "@/lib/presentation/demoEventPlayer";

export interface JudgeControlBarProps {
  executionMode: "DEMO" | "LIVE";
  isDemoPlaying: boolean;
  activeStageIndex: number;
  currentProfileId: DemoProfileId;
  currentScenario: DemoScenario;
  isExhibitionReady: boolean;
  isDegraded: boolean;
  canOpenDossier: boolean;
  canOpenPdf: boolean;
  // Live SSE streaming telemetry & controls
  liveStatus?: "STANDBY" | "RUNNING" | "PAUSED" | "COMPLETE" | "ERROR";
  liveConnectionState?: string;
  liveNarrative?: string;
  liveEventCount?: number;
  liveSpeed?: number;
  onLaunchLiveHunt?: () => void;
  onSetSpeed?: (multiplier: number) => void;
  // Actions
  onToggleExecutionMode: (mode: "DEMO" | "LIVE") => void;
  onStartDemo: () => void;
  onPauseDemo: () => void;
  onResumeDemo: () => void;
  onRestartDemo: () => void;
  onReset: () => void;
  onSkipToStage: (stageIndex: number) => void;
  onSelectProfile: (profileId: DemoProfileId) => void;
  onSelectScenario: (scenario: DemoScenario) => void;
  onOpenDossier: () => void;
  onOpenPdf: () => void;
}

export const JudgeControlBar: React.FC<JudgeControlBarProps> = ({
  executionMode,
  isDemoPlaying,
  activeStageIndex,
  currentProfileId,
  currentScenario,
  isExhibitionReady,
  isDegraded,
  canOpenDossier,
  canOpenPdf,
  liveStatus = "STANDBY",
  liveConnectionState = "DISCONNECTED",
  liveNarrative,
  liveEventCount = 0,
  liveSpeed = 1.0,
  onLaunchLiveHunt,
  onSetSpeed,
  onToggleExecutionMode,
  onStartDemo,
  onPauseDemo,
  onResumeDemo,
  onRestartDemo,
  onReset,
  onSkipToStage,
  onSelectProfile,
  onSelectScenario,
  onOpenDossier,
  onOpenPdf,
}) => {
  const [isCollapsed, setIsCollapsed] = useState<boolean>(executionMode === "LIVE");
  const [showStageMenu, setShowStageMenu] = useState<boolean>(false);
  const [showProfileMenu, setShowProfileMenu] = useState<boolean>(false);
  const [showScenarioMenu, setShowScenarioMenu] = useState<boolean>(false);
  const [showHelpModal, setShowHelpModal] = useState<boolean>(false);

  const handleDirectDownload = () => {
    const link = document.createElement("a");
    link.href = `/api/download/pdf?id=primary&name=Hamza_Gohar`;
    link.download = "ScholarX_Intelligence_Dossier_Hamza_Gohar.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  useEffect(() => {
    setIsCollapsed(executionMode === "LIVE");
  }, [executionMode]);

  // Keyboard shortcut listener (§54)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (
        e.target instanceof HTMLInputElement ||
        e.target instanceof HTMLTextAreaElement ||
        e.target instanceof HTMLSelectElement
      ) {
        return;
      }

      if (e.code === "Space") {
        e.preventDefault();
        if (executionMode === "DEMO") {
          if (isDemoPlaying) {
            onPauseDemo();
          } else {
            onResumeDemo();
          }
        } else if (executionMode === "LIVE" && liveStatus !== "RUNNING" && onLaunchLiveHunt) {
          onLaunchLiveHunt();
        }
      } else if (e.key === "r" || e.key === "R") {
        e.preventDefault();
        onRestartDemo();
      } else if (e.key === "d" || e.key === "D") {
        e.preventDefault();
        onToggleExecutionMode(executionMode === "DEMO" ? "LIVE" : "DEMO");
      } else if (e.key === "j" || e.key === "J") {
        e.preventDefault();
        setIsCollapsed((prev) => !prev);
      } else if (e.key === "?" || e.key === "/") {
        e.preventDefault();
        setShowHelpModal((prev) => !prev);
      } else if (e.key >= "1" && e.key <= "9") {
        const num = parseInt(e.key, 10);
        if (num <= 12) {
          onSkipToStage(num);
        }
      } else if (e.key === "0") {
        onSkipToStage(0);
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [
    isDemoPlaying,
    executionMode,
    liveStatus,
    onLaunchLiveHunt,
    onPauseDemo,
    onResumeDemo,
    onRestartDemo,
    onToggleExecutionMode,
    onSkipToStage,
  ]);

  const activeStage = DEMO_STAGES_LIST.find((s) => s.stageIndex === activeStageIndex) || DEMO_STAGES_LIST[0];
  const activeProfile = DEMO_PROFILES[currentProfileId] || DEMO_PROFILES.PROFILE_A_ICS;
  const isSseConnected = liveConnectionState === "CONNECTED";
  const isSseConnecting = liveConnectionState === "CONNECTING" || liveConnectionState === "RECONNECTING";

  return (
    <>
      {/* Collapsed Pill Floating Surface */}
      {isCollapsed ? (
        <motion.div
          initial={{ y: 24, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: 24, opacity: 0 }}
          className="fixed bottom-3 right-4 z-50 flex items-center space-x-2 px-3.5 py-2 rounded-full bg-[#0C0A09]/92 border border-white/[0.14] backdrop-blur-xl shadow-2xl font-mono text-[11px] pointer-events-auto cursor-pointer hover:border-white/30 transition-all select-none"
          onClick={() => setIsCollapsed(false)}
          title="Expand Exhibition Controller [J]"
        >
          <div className="flex items-center space-x-1.5">
            <span
              className={`w-2 h-2 rounded-full ${
                executionMode === "LIVE"
                  ? isSseConnected
                    ? "bg-emerald-400 animate-pulse"
                    : "bg-amber-400"
                  : "bg-amber-400"
              }`}
            />
            <span className="font-bold text-white tracking-wider uppercase">
              LIVE THEATRE
            </span>
          </div>

          <span className="text-zinc-600">&bull;</span>
          <span className="text-zinc-400">
            {liveEventCount > 0 ? `${liveEventCount} LIVE EVENTS` : "AUTONOMOUS STREAM"}
          </span>

          <span className="text-zinc-600">&bull;</span>
          <span className="text-emerald-400 font-semibold">[J] TELEMETRY</span>
          <ChevronUp className="w-3.5 h-3.5 text-zinc-400 ml-0.5" />
        </motion.div>
      ) : (
        /* Full Unified Exhibition Control Surface */
        <footer className="w-full bg-[#0C0A09]/92 backdrop-blur-xl border-t border-white/[0.08] px-5 py-2 pointer-events-auto z-50 transition-all font-mono select-none">
          <div className="flex items-center justify-between text-xs gap-3">
            {/* Left: Mode Badge & Exhibition Readiness & Active Stage / Live SSE */}
            <div className="flex items-center space-x-3 shrink-0">
              {/* Autonomous Mode Badge */}
              <div className="flex items-center space-x-2 px-3 py-1 rounded-md bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 text-[11px] font-bold">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span>{executionMode === "DEMO" ? "AUTONOMOUS REPLAY" : "LIVE AUTONOMOUS STREAM"}</span>
              </div>

              {/* Exhibition Readiness Status Indicator */}
              <div
                className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-full border text-[10px] tracking-widest ${
                  isExhibitionReady
                    ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-400"
                    : "bg-amber-500/10 border-amber-500/30 text-amber-400"
                }`}
                title={isExhibitionReady ? "All demo profiles & fixtures verified" : "Safeguard offline cache active"}
              >
                <span className={`w-1.5 h-1.5 rounded-full ${isExhibitionReady ? "bg-emerald-400 animate-pulse" : "bg-amber-400"}`} />
                <span className="font-bold">{isExhibitionReady ? "READY" : "DEGRADED"}</span>
              </div>

              {/* In DEMO mode: Stage Selector Dropdown */}
              {executionMode === "DEMO" ? (
                <div className="relative">
                  <button
                    onClick={() => {
                      setShowStageMenu((p) => !p);
                      setShowProfileMenu(false);
                      setShowScenarioMenu(false);
                    }}
                    className="flex items-center space-x-1.5 px-3 py-1 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.1] text-zinc-200 text-[11px] transition-all cursor-pointer"
                  >
                    <Layers className="w-3.5 h-3.5 text-amber-400" />
                    <span className="font-semibold text-white/90 truncate max-w-[170px]">
                      {activeStage.stageName}
                    </span>
                    <ChevronDown className="w-3 h-3 text-zinc-400" />
                  </button>

                  <AnimatePresence>
                    {showStageMenu && (
                      <motion.div
                        initial={{ opacity: 0, y: 6 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: 6 }}
                        className="absolute bottom-full left-0 mb-2 w-72 max-h-80 overflow-y-auto bg-[#1C1917] border border-white/20 rounded-xl shadow-2xl p-1.5 z-50 text-[11px]"
                      >
                        <div className="px-2 py-1 text-[10px] text-zinc-400 uppercase tracking-wider font-bold border-b border-white/[0.08] mb-1">
                          SKIP TO STAGE (0-12)
                        </div>
                        {DEMO_STAGES_LIST.map((stage) => (
                          <button
                            key={stage.stageIndex}
                            onClick={() => {
                              onSkipToStage(stage.stageIndex);
                              setShowStageMenu(false);
                            }}
                            className={`w-full text-left px-2.5 py-1.5 rounded-lg flex items-center justify-between transition-all cursor-pointer ${
                              activeStageIndex === stage.stageIndex
                                ? "bg-amber-500/20 text-amber-300 font-bold"
                                : "text-zinc-300 hover:bg-white/[0.06] hover:text-white"
                            }`}
                          >
                            <span>{stage.stageName}</span>
                            {activeStageIndex === stage.stageIndex && (
                              <CheckCircle2 className="w-3 h-3 text-amber-400" />
                            )}
                          </button>
                        ))}
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              ) : (
                /* In LIVE mode: Live SSE Connection State & Event Counter */
                <div className="flex items-center space-x-2">
                  <div className="flex items-center space-x-1.5 px-2.5 py-1 rounded-full border border-white/[0.08] bg-white/[0.03] text-[10px]">
                    {isSseConnected ? (
                      <>
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                        <span className="text-emerald-400 font-bold tracking-wider">SSE: CONNECTED</span>
                      </>
                    ) : isSseConnecting ? (
                      <>
                        <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-ping" />
                        <span className="text-amber-400 font-bold tracking-wider">SSE: CONNECTING...</span>
                      </>
                    ) : (
                      <>
                        <span className="w-1.5 h-1.5 rounded-full bg-zinc-500" />
                        <span className="text-zinc-400 tracking-wider">SSE: STANDBY</span>
                      </>
                    )}
                  </div>
                  <div className="px-2 py-0.5 rounded bg-white/[0.04] text-[10px] text-zinc-300">
                    {liveEventCount} EVENTS
                  </div>
                </div>
              )}
            </div>

            {/* Center: Playback & Live Execution Controls */}
            <div className="flex items-center space-x-2 shrink-0">
              {executionMode === "DEMO" ? (
                <>
                  {!isDemoPlaying ? (
                    <button
                      onClick={onStartDemo}
                      className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-emerald-500 text-black font-sans font-bold text-xs hover:bg-emerald-400 transition-all duration-150 shadow-[0_0_15px_rgba(16,185,129,0.35)] cursor-pointer"
                      title="Start Deterministic Walkthrough [Space]"
                    >
                      <Play className="w-3.5 h-3.5 fill-current" />
                      <span>START DEMO</span>
                    </button>
                  ) : (
                    <button
                      onClick={onPauseDemo}
                      className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-amber-500 text-black font-sans font-bold text-xs hover:bg-amber-400 transition-all duration-150 shadow-[0_0_15px_rgba(245,158,11,0.35)] cursor-pointer"
                      title="Pause Presentation [Space]"
                    >
                      <Pause className="w-3.5 h-3.5 fill-current" />
                      <span>PAUSE</span>
                    </button>
                  )}

                  <button
                    onClick={onRestartDemo}
                    className="flex items-center space-x-1 px-2.5 py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.1] text-zinc-300 hover:text-white transition-all text-xs cursor-pointer"
                    title="Restart from Stage 0 [R]"
                  >
                    <RotateCcw className="w-3 h-3" />
                    <span>RESTART</span>
                  </button>
                </>
              ) : (
                /* LIVE Mode Playback */
                <>
                  {liveStatus !== "RUNNING" ? (
                    <button
                      onClick={onLaunchLiveHunt}
                      className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-emerald-500 text-black font-sans font-bold text-xs hover:bg-emerald-400 transition-all duration-150 shadow-[0_0_15px_rgba(16,185,129,0.35)] cursor-pointer"
                      title="Launch Autonomous Live Intelligence Hunt [Space]"
                    >
                      <Play className="w-3.5 h-3.5 fill-current" />
                      <span>LAUNCH LIVE HUNT</span>
                    </button>
                  ) : (
                    <div className="flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-mono text-xs">
                      <Radio className="w-3.5 h-3.5 animate-spin" />
                      <span>LIVE COMPUTATION STREAMING...</span>
                    </div>
                  )}

                  {/* Pacing Speed Multipliers in Live Mode */}
                  {onSetSpeed && (
                    <div className="flex items-center space-x-0.5 border border-white/[0.08] bg-black/40 rounded-lg p-0.5 text-[10px]">
                      {[0.5, 1.0, 2.0].map((s) => (
                        <button
                          key={s}
                          onClick={() => onSetSpeed(s)}
                          className={`px-1.5 py-0.5 rounded transition-all ${
                            liveSpeed === s
                              ? "bg-white/20 text-white font-bold"
                              : "text-zinc-400 hover:text-white"
                          }`}
                        >
                          {s}x
                        </button>
                      ))}
                    </div>
                  )}
                </>
              )}

              {/* Authoritative Reset */}
              <button
                onClick={onReset}
                className="flex items-center space-x-1 px-2.5 py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.1] text-zinc-300 hover:text-white transition-all text-xs cursor-pointer"
                title="Authoritative Reset to Standby State"
              >
                <X className="w-3 h-3" />
                <span>RESET</span>
              </button>
            </div>

            {/* Right: Profiles / Narrative, Artifacts, Shortcuts & Collapse */}
            <div className="flex items-center space-x-2 shrink-0">
              {executionMode === "DEMO" ? (
                <>
                  {/* Student Profile Dropdown */}
                  <div className="relative hidden md:block">
                    <button
                      onClick={() => {
                        setShowProfileMenu((p) => !p);
                        setShowStageMenu(false);
                        setShowScenarioMenu(false);
                      }}
                      className="flex items-center space-x-1 px-2.5 py-1 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.1] text-zinc-300 text-[11px] transition-all cursor-pointer"
                      title="Change Student Profile Scenario"
                    >
                      <User className="w-3 h-3 text-cyan-400" />
                      <span className="truncate max-w-[100px]">{activeProfile.name}</span>
                      <ChevronDown className="w-3 h-3 text-zinc-400" />
                    </button>

                    <AnimatePresence>
                      {showProfileMenu && (
                        <motion.div
                          initial={{ opacity: 0, y: 6 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: 6 }}
                          className="absolute bottom-full right-0 mb-2 w-72 bg-[#1C1917] border border-white/20 rounded-xl shadow-2xl p-1.5 z-50 text-[11px]"
                        >
                          <div className="px-2 py-1 text-[10px] text-zinc-400 uppercase tracking-wider font-bold border-b border-white/[0.08] mb-1">
                            PAKISTANI DEMO PROFILES
                          </div>
                          {Object.values(DEMO_PROFILES).map((p) => (
                            <button
                              key={p.id}
                              onClick={() => {
                                onSelectProfile(p.id);
                                setShowProfileMenu(false);
                              }}
                              className={`w-full text-left p-2 rounded-lg transition-all cursor-pointer ${
                                currentProfileId === p.id
                                  ? "bg-cyan-500/20 text-cyan-300 border border-cyan-500/30"
                                  : "text-zinc-300 hover:bg-white/[0.06] hover:text-white"
                              }`}
                            >
                              <div className="font-bold">{p.name} ({p.marks})</div>
                              <div className="text-[10px] text-zinc-400">{p.degree} &bull; {p.field}</div>
                            </button>
                          ))}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>

                  {/* Resilience Demo Scenario Selector */}
                  <div className="relative hidden lg:block">
                    <button
                      onClick={() => {
                        setShowScenarioMenu((p) => !p);
                        setShowStageMenu(false);
                        setShowProfileMenu(false);
                      }}
                      className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg border text-[11px] transition-all cursor-pointer ${
                        currentScenario === "STANDARD"
                          ? "bg-white/[0.04] border-white/[0.1] text-zinc-300"
                          : "bg-amber-500/10 border-amber-500/30 text-amber-300"
                      }`}
                      title="Select Resilience Demonstration"
                    >
                      <ShieldAlert className="w-3 h-3 text-amber-400" />
                      <span className="truncate max-w-[100px]">
                        {currentScenario === "STANDARD"
                          ? "Normal Demo"
                          : currentScenario === "SEARCH_FAILOVER"
                          ? "Failover"
                          : "Partial"}
                      </span>
                      <ChevronDown className="w-3 h-3 text-zinc-400" />
                    </button>

                    <AnimatePresence>
                      {showScenarioMenu && (
                        <motion.div
                          initial={{ opacity: 0, y: 6 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: 6 }}
                          className="absolute bottom-full right-0 mb-2 w-64 bg-[#1C1917] border border-white/20 rounded-xl shadow-2xl p-1.5 z-50 text-[11px]"
                        >
                          <div className="px-2 py-1 text-[10px] text-zinc-400 uppercase tracking-wider font-bold border-b border-white/[0.08] mb-1">
                            EXHIBITION SCENARIOS
                          </div>
                          <button
                            onClick={() => {
                              onSelectScenario("STANDARD");
                              setShowScenarioMenu(false);
                            }}
                            className={`w-full text-left p-2 rounded-lg transition-all cursor-pointer ${
                              currentScenario === "STANDARD"
                                ? "bg-white/10 text-white font-bold"
                                : "text-zinc-300 hover:bg-white/[0.06]"
                            }`}
                          >
                            <div className="font-bold">Standard Walkthrough</div>
                            <div className="text-[10px] text-zinc-400">Normal flawless intelligence run</div>
                          </button>
                          <button
                            onClick={() => {
                              onSelectScenario("SEARCH_FAILOVER");
                              setShowScenarioMenu(false);
                            }}
                            className={`w-full text-left p-2 rounded-lg transition-all cursor-pointer ${
                              currentScenario === "SEARCH_FAILOVER"
                                ? "bg-amber-500/20 text-amber-300 font-bold"
                                : "text-zinc-300 hover:bg-white/[0.06]"
                            }`}
                          >
                            <div className="font-bold text-amber-400">Search Failover</div>
                            <div className="text-[10px] text-zinc-400">Tavily fails &rarr; Verified cache failover</div>
                          </button>
                          <button
                            onClick={() => {
                              onSelectScenario("PARTIAL_FLEET");
                              setShowScenarioMenu(false);
                            }}
                            className={`w-full text-left p-2 rounded-lg transition-all cursor-pointer ${
                              currentScenario === "PARTIAL_FLEET"
                                ? "bg-rose-500/20 text-rose-300 font-bold"
                                : "text-zinc-300 hover:bg-white/[0.06]"
                            }`}
                          >
                            <div className="font-bold text-rose-400">Partial Fleet</div>
                            <div className="text-[10px] text-zinc-400">Americas scout fails &rarr; 4 scouts continue</div>
                          </button>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                </>
              ) : (
                /* LIVE Mode Narrative Readout */
                liveNarrative && (
                  <div className="hidden md:flex items-center space-x-1.5 px-2.5 py-1 rounded-lg bg-white/[0.03] border border-white/[0.06] text-[11px] max-w-[220px] lg:max-w-[280px]">
                    <Activity className="w-3 h-3 text-emerald-400 shrink-0 animate-pulse" />
                    <span className="text-zinc-300 truncate italic">{liveNarrative}</span>
                  </div>
                )
              )}

              {/* Artifact Actions: Web Dossier, PDF & Download */}
              <button
                onClick={onOpenDossier}
                className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg border text-[11px] font-bold transition-all cursor-pointer ${
                  canOpenDossier
                    ? "bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-300 border-cyan-500/30"
                    : "bg-white/[0.02] border-white/[0.05] text-zinc-500 cursor-not-allowed"
                }`}
                title="Open Editorial Web Dossier Modal"
              >
                <FileText className="w-3 h-3" />
                <span>WEB DOSSIER</span>
              </button>

              <button
                onClick={handleDirectDownload}
                className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg border text-[11px] font-bold transition-all shadow-sm ${
                  canOpenPdf
                    ? "bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border-emerald-500/40 cursor-pointer"
                    : "bg-white/[0.02] border-white/[0.05] text-zinc-500 pointer-events-none opacity-40"
                }`}
                title="Download Candidate Scholarship Intelligence Dossier"
              >
                <Download className="w-3 h-3 stroke-[2.5]" />
                <span>DOWNLOAD DOSSIER</span>
              </button>

              {/* Presenter Shortcuts Help Button */}
              <button
                onClick={() => setShowHelpModal(true)}
                className="p-1 rounded-lg text-zinc-400 hover:text-white hover:bg-white/[0.08] transition-all cursor-pointer"
                title="Presenter Shortcuts [?]"
              >
                <HelpCircle className="w-3.5 h-3.5" />
              </button>

              {/* Collapse Button */}
              <button
                onClick={() => setIsCollapsed(true)}
                className="p-1 rounded-lg text-zinc-400 hover:text-white hover:bg-white/[0.08] transition-all cursor-pointer"
                title="Collapse Controller [J]"
              >
                <ChevronDown className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        </footer>
      )}

      {/* Presenter Shortcuts Reference Modal */}
      <AnimatePresence>
        {showHelpModal && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="w-full max-w-sm bg-[#1C1917] border border-white/20 rounded-2xl p-5 shadow-2xl text-white font-mono text-xs"
            >
              <div className="flex items-center justify-between border-b border-white/10 pb-3 mb-3">
                <span className="font-bold text-amber-400 tracking-wider">
                  JUDGE MODE // PRESENTER SHORTCUTS
                </span>
                <button
                  onClick={() => setShowHelpModal(false)}
                  className="text-zinc-400 hover:text-white cursor-pointer"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              <div className="space-y-2.5 text-zinc-300">
                <div className="flex items-center justify-between">
                  <kbd className="px-2 py-0.5 rounded bg-white/10 text-white font-bold">Space</kbd>
                  <span>Play / Pause Demo or Live Hunt</span>
                </div>
                <div className="flex items-center justify-between">
                  <kbd className="px-2 py-0.5 rounded bg-white/10 text-white font-bold">R</kbd>
                  <span>Restart Demo from Beginning</span>
                </div>
                <div className="flex items-center justify-between">
                  <kbd className="px-2 py-0.5 rounded bg-white/10 text-white font-bold">D</kbd>
                  <span>Toggle Live / Demo Mode</span>
                </div>
                <div className="flex items-center justify-between">
                  <kbd className="px-2 py-0.5 rounded bg-white/10 text-white font-bold">J</kbd>
                  <span>Collapse / Expand Control Bar</span>
                </div>
                <div className="flex items-center justify-between">
                  <kbd className="px-2 py-0.5 rounded bg-white/10 text-white font-bold">1 – 9</kbd>
                  <span>Jump Directly to Stage 1 – 9</span>
                </div>
                <div className="flex items-center justify-between">
                  <kbd className="px-2 py-0.5 rounded bg-white/10 text-white font-bold">0</kbd>
                  <span>Reset to Standby (Stage 0)</span>
                </div>
              </div>

              <div className="mt-4 pt-3 border-t border-white/10 text-[10px] text-zinc-400 leading-relaxed">
                Judge Mode guarantees deterministic visual continuity without exposing developer diagnostics or internal keys.
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </>
  );
};
