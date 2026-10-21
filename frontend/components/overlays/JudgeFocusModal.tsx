"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { X, Cpu, Search, Terminal, Database, Wrench, ShieldCheck, Activity } from "lucide-react";
import { sound } from "@/lib/sound-fx";

export const JudgeFocusModal: React.FC = () => {
  const { focusedAgent, setFocusedAgent } = useCommandStore();

  if (!focusedAgent) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-6 animate-in fade-in duration-200 select-none">
      <div className="relative w-full max-w-4xl max-h-[85vh] bg-obsidian-900 border border-cyber-cyan/50 rounded-lg shadow-glow-cyan flex flex-col overflow-hidden corner-bracket">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-3 bg-obsidian-950 border-b border-white/10">
          <div className="flex items-center space-x-3">
            <Cpu className="w-5 h-5 text-cyber-cyan animate-pulse" />
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="font-mono text-sm font-black tracking-wider text-white">
                  {focusedAgent.title}
                </h3>
                <span className="font-mono text-[9px] px-2 py-0.5 rounded bg-pakistan-deep text-pakistan-emerald font-bold border border-pakistan-emerald/30">
                  {focusedAgent.status}
                </span>
              </div>
              <p className="font-mono text-[10px] text-white/50">
                {focusedAgent.role} • DEEP AGENT INSPECTION MODE
              </p>
            </div>
          </div>

          <button
            onClick={() => {
              sound.playClick();
              setFocusedAgent(null);
            }}
            className="p-1 rounded hover:bg-white/10 text-white/50 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body Content */}
        <div className="flex-1 overflow-y-auto p-5 font-mono text-xs space-y-4">
          {/* Current Task Description */}
          <div className="p-3 rounded bg-obsidian-950 border border-white/10 space-y-1">
            <span className="text-[10px] text-cyber-cyan font-bold tracking-widest block uppercase">
              ACTIVE TASK DIRECTIVE
            </span>
            <p className="text-white text-xs leading-relaxed">
              {focusedAgent.task}
            </p>
          </div>

          {/* Tools & Models Employed */}
          <div className="space-y-1.5">
            <span className="text-[10px] text-white/50 font-bold tracking-widest block uppercase">
              CONNECTED TOOLS & REASONING ENGINES
            </span>
            <div className="flex flex-wrap gap-2">
              {focusedAgent.toolsUsed.map((t, idx) => (
                <div
                  key={idx}
                  className="flex items-center space-x-1.5 px-2.5 py-1 rounded bg-white/[0.04] border border-white/10 text-white/80 text-[11px]"
                >
                  <Wrench className="w-3 h-3 text-cyber-cyan" />
                  <span>{t}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Real Queries Dispatched */}
          <div className="space-y-1.5">
            <span className="text-[10px] text-white/50 font-bold tracking-widest block uppercase">
              RECENTLY EXECUTED QUERIES & DIRECTIVES
            </span>
            <div className="space-y-1">
              {focusedAgent.queriesExecuted.map((q, idx) => (
                <div
                  key={idx}
                  className="flex items-center space-x-2 p-2 rounded bg-obsidian-950/70 border border-white/5 text-[11px] text-white/90"
                >
                  <Search className="w-3 h-3 text-cyber-cyan flex-shrink-0" />
                  <span className="truncate italic">&quot;{q}&quot;</span>
                </div>
              ))}
            </div>
          </div>

          {/* Event Stream Trace */}
          {focusedAgent.recentEvents.length > 0 && (
            <div className="space-y-1.5">
              <span className="text-[10px] text-white/50 font-bold tracking-widest block uppercase">
                AGENT TELEMETRY TRACE ({focusedAgent.recentEvents.length})
              </span>
              <div className="space-y-1 max-h-48 overflow-y-auto pr-1">
                {focusedAgent.recentEvents.map((evt) => (
                  <div
                    key={evt.event_id}
                    className="p-1.5 rounded bg-obsidian-950 border border-white/5 text-[10px] flex items-center justify-between text-white/70"
                  >
                    <div className="flex items-center space-x-2">
                      <span className="text-cyber-cyan font-bold">[{evt.event_type}]</span>
                      <span className="truncate max-w-[400px]">
                        {evt.payload?.message || evt.payload?.query || JSON.stringify(evt.payload)}
                      </span>
                    </div>
                    <span className="text-white/30 text-[9px]">
                      {new Date(evt.timestamp).toLocaleTimeString()}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-5 py-2.5 bg-obsidian-950 border-t border-white/10 flex items-center justify-between font-mono text-[10px] text-white/40">
          <span>PRESS ESC OR CLICK OUTSIDE TO CLOSE</span>
          <button
            onClick={() => {
              sound.playClick();
              setFocusedAgent(null);
            }}
            className="px-3 py-1 rounded bg-cyber-cyan text-obsidian-950 font-bold hover:bg-cyan-300 transition-colors"
          >
            RETURN TO COMMAND ROOM
          </button>
        </div>
      </div>
    </div>
  );
};
