"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { Gauge, CheckCircle2, CircleDashed, Flame, Sparkles } from "lucide-react";
import { sound } from "@/lib/sound-fx";

const PIPELINE_NODES = [
  { id: "orchestrator", label: "01. STRATEGIC COMMAND", phase: "ORCHESTRATION" },
  { id: "profile", label: "02. INTAKE", phase: "INTAKE" },
  { id: "commander", label: "03. DISCOVERY", phase: "DISCOVERY" },
  { id: "scouts", label: "04. 5x SCOUTS", phase: "DISCOVERY" },
  { id: "eligibility", label: "05. 15-DIM VERIFY", phase: "VERIFICATION" },
  { id: "costs", label: "06. PKR COSTS", phase: "VERIFICATION" },
  { id: "deadlines", label: "07. DEADLINE RISK", phase: "VERIFICATION" },
  { id: "skeptic", label: "08. SKEPTIC ARENA", phase: "VERIFICATION" },
  { id: "ranking", label: "09. RANKING", phase: "SYNTHESIS" },
  { id: "roadmap", label: "10. ROADMAP", phase: "MISSION_COMPLETE" },
];

export const PipelineRail: React.FC = () => {
  const {
    missionPhase,
    missionStatus,
    progressPercent,
    replaySpeed,
    setReplaySpeed,
    candidates,
    studentProfile,
  } = useCommandStore();

  const getPhaseIndex = (phase: string) => {
    switch (phase) {
      case "ORCHESTRATION": return 1;
      case "INTAKE": return 2;
      case "DISCOVERY": return 4;
      case "VERIFICATION": return 8;
      case "SYNTHESIS": return 9;
      case "MISSION_COMPLETE": return 10;
      default: return 0;
    }
  };

  const currentIdx = getPhaseIndex(missionPhase);

  return (
    <footer className="w-full bg-obsidian-900/95 border-t border-white/10 px-4 py-2 flex items-center justify-between select-none z-20 backdrop-blur-md">
      {/* 10-Node Pipeline Progression */}
      <div className="flex items-center space-x-1 overflow-x-auto max-w-[65%]">
        {PIPELINE_NODES.map((node, i) => {
          const isDone = currentIdx > i + 1 || missionPhase === "MISSION_COMPLETE";
          const isActive = currentIdx === i + 1 && missionStatus === "RUNNING";

          return (
            <div key={node.id} className="flex items-center space-x-1 flex-shrink-0">
              <div
                className={`flex items-center space-x-1.5 px-2 py-1 rounded font-mono text-[10px] font-semibold border transition-all ${
                  isActive
                    ? "bg-cyber-cyan text-obsidian-950 border-cyber-cyan shadow-glow-cyan animate-pulse"
                    : isDone
                    ? "bg-obsidian-950 text-pakistan-emerald border-pakistan-emerald/40"
                    : "bg-obsidian-950 text-white/30 border-white/5"
                }`}
              >
                {isDone ? (
                  <CheckCircle2 className="w-3 h-3 text-pakistan-emerald" />
                ) : isActive ? (
                  <CircleDashed className="w-3 h-3 animate-spin text-obsidian-950" />
                ) : (
                  <span className="w-1.5 h-1.5 rounded-full bg-white/20" />
                )}
                <span>{node.label}</span>
              </div>
              {i < PIPELINE_NODES.length - 1 && (
                <div
                  className={`w-2 h-[1px] ${
                    isDone ? "bg-pakistan-emerald/60" : "bg-white/10"
                  }`}
                />
              )}
            </div>
          );
        })}
      </div>

      {/* Progress & Speed Controls */}
      <div className="flex items-center space-x-4">
        {/* Progress Bar */}
        <div className="flex items-center space-x-2 font-mono text-[11px]">
          <span className="text-white/40">COMPLETION:</span>
          <div className="w-24 h-2 bg-obsidian-950 rounded-full overflow-hidden border border-white/10">
            <div
              className="h-full bg-gradient-to-r from-cyber-cyan to-pakistan-emerald transition-all duration-300"
              style={{ width: `${progressPercent}%` }}
            />
          </div>
          <span className="font-bold text-white w-8 text-right">
            {progressPercent}%
          </span>
        </div>

        {/* Speed Multipliers */}
        <div className="flex items-center space-x-1 font-mono text-[10px] bg-obsidian-950 p-0.5 rounded border border-white/10">
          <span className="text-white/40 px-1.5">SPEED:</span>
          {[1, 2, 5].map((speed) => (
            <button
              key={speed}
              onClick={() => {
                sound.playClick();
                setReplaySpeed(speed);
              }}
              className={`px-1.5 py-0.5 rounded font-bold transition-colors ${
                replaySpeed === speed
                  ? "bg-cyber-cyan text-obsidian-950"
                  : "text-white/50 hover:text-white"
              }`}
            >
              {speed}x
            </button>
          ))}
        </div>
      </div>
    </footer>
  );
};
