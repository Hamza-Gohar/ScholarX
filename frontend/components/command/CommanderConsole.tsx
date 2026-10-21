"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { Cpu, Terminal, ShieldAlert, Sparkles, Layers, ArrowRight, Activity, Zap } from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { Region } from "@/lib/types";

export const CommanderConsole: React.FC = () => {
  const {
    commander,
    missionPhase,
    missionStatus,
    studentProfile,
    scouts,
    setFocusedAgent,
    events,
  } = useCommandStore();

  const isRunning = missionStatus === "RUNNING";

  const getStatusColor = () => {
    switch (missionPhase) {
      case "DISCOVERY":
        return "text-cyber-cyan border-cyber-cyan/40 bg-cyber-cyan/10 shadow-glow-cyan";
      case "VERIFICATION":
        return "text-warning-amber border-warning-amber/40 bg-warning-amber/10 shadow-glow-amber";
      case "SYNTHESIS":
        return "text-purple-400 border-purple-400/40 bg-purple-400/10 shadow-glow-purple";
      case "MISSION_COMPLETE":
        return "text-pakistan-emerald border-pakistan-emerald/40 bg-pakistan-emerald/10 shadow-glow-emerald";
      default:
        return "text-white/40 border-white/10 bg-white/5";
    }
  };

  const handleOpenFocus = () => {
    sound.playClick();
    setFocusedAgent({
      agentId: "commander",
      title: "SCHOLARX COMMANDER // STRATEGIC ADVISOR",
      role: "Central Multi-Agent Coordination Brain",
      status: missionStatus === "RUNNING" ? missionPhase : "STANDBY",
      task: commander.activeDecision,
      toolsUsed: ["Autonomous Multi-Agent Network", "EventBus PubSub", "Groq Qwen-3.8-27B", "SQLite WAL"],
      queriesExecuted: commander.recentDecisions.map((d: any) => d.decisionText),
      recentEvents: events.filter((e) => e.agent_id === "orchestrator" || e.component_type === "AGENT").slice(0, 10),
    });
  };

  return (
    <div
      onClick={handleOpenFocus}
      className="command-panel corner-bracket rounded-lg p-3 border border-cyber-cyan/30 hover:border-cyber-cyan/60 transition-all cursor-pointer group bg-gradient-to-b from-obsidian-900/95 to-obsidian-950/95 shadow-xl select-none"
    >
      {/* Top Strip: Commander Identity + Status LED */}
      <div className="flex items-center justify-between border-b border-white/10 pb-2 mb-2.5">
        <div className="flex items-center space-x-2.5">
          <div className="relative flex items-center justify-center">
            <Cpu className="w-4 h-4 text-cyber-cyan animate-pulse" />
            <div className="absolute -inset-1 rounded-full bg-cyber-cyan/20 blur-sm pointer-events-none" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="font-mono text-xs font-black tracking-widest text-white">
                SCHOLARX COMMANDER
              </span>
              <span className="font-mono text-[9px] px-1.5 py-0.2 rounded bg-white/10 text-cyber-cyan border border-cyber-cyan/30 font-bold">
                STRATEGIC ADVISOR
              </span>
            </div>
            <span className="font-mono text-[9px] text-white/40 block">
              AUTONOMOUS MULTI-AGENT ADVISORY DIRECTOR
            </span>
          </div>
        </div>

        {/* Live Operational State Pill */}
        <div className="flex items-center space-x-2 font-mono text-[10px]">
          <div className={`px-2 py-0.5 rounded border flex items-center space-x-1.5 ${getStatusColor()}`}>
            <span
              className={`w-1.5 h-1.5 rounded-full ${
                isRunning ? "bg-cyber-cyan animate-ping" : "bg-white/30"
              }`}
            />
            <span className="font-bold tracking-wider">
              {isRunning ? commander.statusText : "STANDBY // IDLE"}
            </span>
          </div>
          <span className="text-[9px] text-white/30 group-hover:text-cyber-cyan transition-colors hidden md:inline">
            [CLICK TO INSPECT]
          </span>
        </div>
      </div>

      {/* Grid: Current Mission Context & Active Reasoner Decision */}
      <div className="grid grid-cols-12 gap-3 text-[11px] font-mono">
        {/* Left: Mission Parameters Brief (5 cols) */}
        <div className="col-span-5 bg-obsidian-950/80 rounded p-2 border border-white/5 space-y-1">
          <div className="text-[9px] text-white/40 font-bold uppercase tracking-wider flex items-center justify-between">
            <span>TARGET DIRECTIVE</span>
            <span className="text-pakistan-emerald font-bold">PK-OPT</span>
          </div>
          <div className="text-white font-semibold text-[11px] truncate text-cyber-cyan">
            {studentProfile.personal.name} • {studentProfile.academic.institution}
          </div>
          <div className="flex items-center justify-between text-[10px] text-white/70">
            <span>Degree: <span className="text-white font-bold">{studentProfile.academic.degree_level}</span></span>
            <span>GPA: <span className="text-pakistan-emerald font-bold">{studentProfile.academic.gpa_obtained || studentProfile.academic.percentage + "%"}</span></span>
          </div>
          <div className="flex items-center justify-between text-[10px] text-white/60 pt-0.5 border-t border-white/5">
            <span>Max Out-of-Pocket:</span>
            <span className="font-bold text-warning-amber">
              PKR {(studentProfile.financial.max_out_of_pocket_pkr).toLocaleString()}
            </span>
          </div>
        </div>

        {/* Right: Active Decision Stream & Regional Deployment Status (7 cols) */}
        <div className="col-span-7 bg-obsidian-950/80 rounded p-2 border border-white/5 flex flex-col justify-between">
          <div>
            <div className="text-[9px] text-white/40 font-bold uppercase tracking-wider flex items-center justify-between mb-1">
              <span className="flex items-center space-x-1">
                <Activity className="w-3 h-3 text-cyber-cyan" />
                <span>ACTIVE DECISION LOG</span>
              </span>
              <span className="text-cyber-cyan/70 text-[9px]">LIVE TELEMETRY</span>
            </div>
            <p className="text-white/90 text-[10px] leading-tight line-clamp-2">
              ↳ {commander.activeDecision}
            </p>
          </div>

          {/* Regional Scouts Micro-Matrix */}
          <div className="flex items-center justify-between pt-1.5 border-t border-white/5 text-[9px]">
            {(["Europe", "Asia", "Americas", "MENA", "Oceania"] as Region[]).map((r) => {
              const s = scouts[r];
              const isAct = s?.status === "ACTIVE" || s?.status === "SCRAPING";
              return (
                <div key={r} className="flex items-center space-x-1">
                  <span
                    className={`w-1.5 h-1.5 rounded-full ${
                      isAct ? "bg-pakistan-emerald animate-pulse" : s?.itemsFound > 0 ? "bg-cyber-cyan" : "bg-white/20"
                    }`}
                  />
                  <span className={`${isAct ? "text-white font-bold" : "text-white/50"}`}>
                    {r.substring(0, 2).toUpperCase()}:
                  </span>
                  <span className={s?.itemsFound > 0 ? "text-pakistan-emerald font-bold" : "text-white/30"}>
                    {s?.itemsFound || 0}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};
