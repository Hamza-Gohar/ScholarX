"use client";

import React from "react";
import { SSEConnectionState } from "@/lib/hooks/useSSEStream";
import { LiveVisualPhase } from "@/lib/theatre/theatreDirectorStore";
import {
  Play,
  RotateCcw,
  Wifi,
  WifiOff,
  Activity,
  FileText,
  ExternalLink,
  CheckCircle2,
  AlertCircle,
  Radio,
} from "lucide-react";

export interface Phase8LiveDirectorProps {
  connectionState: SSEConnectionState;
  visualPhase: LiveVisualPhase;
  missionStatus: "STANDBY" | "RUNNING" | "PAUSED" | "COMPLETE" | "ERROR";
  activeNarrative: string;
  sessionId: string;
  eventCount: number;
  speed: number;
  onLaunchLiveHunt: () => void;
  onReset: () => void;
  onSetSpeed: (multiplier: number) => void;
  onOpenWebDossier?: () => void;
  onOpenPdfDossier?: () => void;
}

const PHASE_LABELS: Record<LiveVisualPhase, string> = {
  INITIALIZING: "01 // SYSTEM READY",
  FLEET_DISCOVERY: "02 // GLOBAL FLEET ACTIVE",
  SPECIALIST_INVESTIGATION: "03 // DEEP INVESTIGATION",
  RANKING_EVALUATION: "04 // RANKING ENGINE",
  ROADMAP_ASSEMBLY: "05 // ADVISOR ROADMAP",
  DOSSIER_BUILD: "06 // DOSSIER ASSEMBLY",
  MISSION_COMPLETE: "07 // MISSION COMPLETE",
};

export const Phase8LiveDirector: React.FC<Phase8LiveDirectorProps> = ({
  connectionState,
  visualPhase,
  missionStatus,
  activeNarrative,
  sessionId,
  eventCount,
  speed,
  onLaunchLiveHunt,
  onReset,
  onSetSpeed,
  onOpenWebDossier,
  onOpenPdfDossier,
}) => {
  const isConnected = connectionState === "CONNECTED";
  const isConnecting = connectionState === "CONNECTING" || connectionState === "RECONNECTING";

  return (
    <footer className="w-full bg-black/75 backdrop-blur-md border-t border-white/[0.08] px-6 py-2.5 flex flex-col space-y-2 pointer-events-auto z-50">
      {/* Top Telemetry Row */}
      <div className="flex items-center justify-between text-[11px] font-mono">
        <div className="flex items-center space-x-3">
          {/* Live SSE Status Indicator */}
          <div className="flex items-center space-x-1.5 px-2.5 py-1 rounded-full border border-white/[0.08] bg-white/[0.03]">
            {isConnected ? (
              <>
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span className="text-emerald-400 font-bold tracking-wider">LIVE SSE: CONNECTED</span>
              </>
            ) : isConnecting ? (
              <>
                <span className="w-2 h-2 rounded-full bg-amber-400 animate-ping" />
                <span className="text-amber-400 font-bold tracking-wider">SSE: CONNECTING...</span>
              </>
            ) : (
              <>
                <span className="w-2 h-2 rounded-full bg-zinc-500" />
                <span className="text-zinc-400 tracking-wider">SSE: DISCONNECTED</span>
              </>
            )}
          </div>

          {/* Active Phase Badge */}
          <div className="px-2.5 py-1 rounded-full border border-white/[0.08] bg-black/50 text-amber-400 font-medium">
            {PHASE_LABELS[visualPhase]}
          </div>

          {/* Session Identifier */}
          <div className="text-zinc-400 hidden md:inline">
            SESSION: <span className="text-white/80 font-mono">{sessionId.slice(0, 16)}</span>
          </div>

          {/* Event Counter */}
          <div className="px-2 py-0.5 rounded bg-white/[0.04] text-[10px] text-zinc-300">
            {eventCount} EVENTS CONSUMED
          </div>
        </div>

        {/* Narrative Readout */}
        <div className="flex items-center space-x-2 overflow-hidden text-right max-w-[55%]">
          <Activity className="w-3.5 h-3.5 text-emerald-400 shrink-0 animate-pulse" />
          <span className="text-white/90 truncate italic">{activeNarrative}</span>
        </div>
      </div>

      {/* Bottom Controls Row */}
      <div className="flex items-center justify-between pt-1">
        {/* Playback Controls & Action */}
        <div className="flex items-center space-x-3">
          {missionStatus !== "RUNNING" ? (
            <button
              onClick={onLaunchLiveHunt}
              className="flex items-center space-x-1.5 px-4 py-1.5 rounded-lg bg-emerald-500 text-black font-sans font-bold text-xs hover:bg-emerald-400 transition-all duration-200 shadow-[0_0_18px_rgba(16,185,129,0.45)] cursor-pointer"
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

          <button
            onClick={onReset}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-white/[0.1] bg-white/[0.03] text-zinc-300 hover:text-white hover:bg-white/[0.06] text-xs font-mono transition-all duration-200"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>RESET</span>
          </button>

          {/* Pacing Speed Multiplier (§21) */}
          <div className="flex items-center space-x-1 border border-white/[0.08] bg-black/40 rounded-lg p-0.5 text-[10px] font-mono">
            {[0.5, 1.0, 2.0].map((s) => (
              <button
                key={s}
                onClick={() => onSetSpeed(s)}
                className={`px-2 py-0.5 rounded transition-all duration-150 ${
                  speed === s
                    ? "bg-white/20 text-white font-bold"
                    : "text-zinc-400 hover:text-zinc-200"
                }`}
              >
                {s}x
              </button>
            ))}
          </div>
        </div>

        {/* Deliverable Action Buttons upon completion */}
        <div className="flex items-center space-x-2.5">
          {visualPhase === "MISSION_COMPLETE" ? (
            <>
              <button
                onClick={onOpenWebDossier}
                className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 border border-white/20 text-white font-mono text-xs transition-all duration-200 shadow-sm"
              >
                <ExternalLink className="w-3.5 h-3.5" />
                <span>OPEN WEB DOSSIER</span>
              </button>
              <button
                onClick={onOpenPdfDossier}
                className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-sx-gold/20 hover:bg-sx-gold/30 border border-sx-gold/40 text-sx-gold font-mono text-xs font-bold transition-all duration-200 shadow-[0_0_10px_rgba(212,175,55,0.25)]"
              >
                <FileText className="w-3.5 h-3.5" />
                <span>VIEW / PRINT PDF</span>
              </button>
            </>
          ) : (
            <div className="text-[10px] font-mono text-zinc-500 uppercase tracking-widest hidden sm:inline">
              LIVE EVENT-DRIVEN THEATRE // AUTONOMOUS BACKEND TRUTH
            </div>
          )}
        </div>
      </div>
    </footer>
  );
};
