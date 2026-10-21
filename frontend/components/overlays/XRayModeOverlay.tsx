"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { X, Network, Cpu, ArrowDown, Database, CheckCircle2, CircleDashed, Terminal, Wrench } from "lucide-react";
import { sound } from "@/lib/sound-fx";

const PIPELINE_STAGES = [
  { id: "orchestrator", label: "01. STRATEGIC COMMAND", role: "Autonomous Multi-Agent Director", agent: "MissionCommander", tool: "Async State Manager" },
  { id: "profile", label: "02. PROFILE INTAKE", role: "Document Parser & Schema Validator", agent: "ProfileAgent", tool: "PyPDF + Groq Qwen-3.8" },
  { id: "commander", label: "03. DISCOVERY COMMANDER", role: "Synthesis of Regional Query Strategies", agent: "DiscoveryCommander", tool: "Token-set Jaccard De-duplication" },
  { id: "scouts", label: "04. 5x REGIONAL SCOUTS", role: "Parallel Scout Pipelines (EU, AS, AM, ME, OC)", agent: "ScoutWorkflows", tool: "Tavily (7 keys) + Firecrawl (3 keys) + Jina" },
  { id: "eligibility", label: "05. ELIGIBILITY INVESTIGATOR", role: "15-Dimension Criterion Evaluator", agent: "EligibilityChecker", tool: "HEC HAT/USAT + BISE/FBISE Rules Engine" },
  { id: "costs", label: "06. TRUE COST ANALYZER", role: "PKR 4-Phase Out-of-Pocket Breakdown", agent: "CostAnalyzer", tool: "Pakistani Expense Matrix" },
  { id: "deadline", label: "07. DEADLINE INTELLIGENCE", role: "Preparation Lead Times & Risk Tiering", agent: "DeadlineAnalyzer", tool: "HEC/IBCC Turnaround Intelligence" },
  { id: "skeptic", label: "08. SKEPTIC DEBATE ARENA", role: "Adversarial Pakistani Friction Analysis", agent: "SkepticAgent", tool: "Asyncio.gather Concurrent Challenger" },
  { id: "ranking", label: "09. WEIGHTED RANKING ENGINE", role: "Composite Score Formula Integration", agent: "RankingEngine", tool: "Pakistan-Adjusted Multi-Factor Weights" },
  { id: "advisor", label: "10. FINAL ADVISOR AGENT", role: "Personalized Roadmap & Office Directory", agent: "AdvisorAgent", tool: "HEC / IBCC / Gerry's Office Matrix" },
];

export const XRayModeOverlay: React.FC = () => {
  const {
    overlayView,
    setOverlayView,
    missionPhase,
    missionStatus,
    events,
    sessionId,
    backendConnected,
  } = useCommandStore();

  if (overlayView !== "XRAY") return null;

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
    <div className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-6 animate-in fade-in duration-200 select-none">
      <div className="relative w-full max-w-5xl max-h-[90vh] bg-obsidian-900 border border-cyber-cyan/50 rounded-lg shadow-glow-cyan flex flex-col overflow-hidden corner-bracket">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-3.5 bg-obsidian-950 border-b border-white/10">
          <div className="flex items-center space-x-3">
            <Network className="w-5 h-5 text-cyber-cyan animate-pulse" />
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="font-mono text-sm font-black tracking-wider text-white">
                  X-RAY MODE // MULTI-AGENT ARCHITECTURE MAP
                </h3>
                <span className="font-mono text-[9px] px-2 py-0.5 rounded bg-cyber-cyan/20 text-cyber-cyan font-bold border border-cyber-cyan/40">
                  {backendConnected ? "LIVE FASTAPI INTELLIGENCE" : "HIGH-FIDELITY SIMULATOR"}
                </span>
              </div>
              <p className="font-mono text-[10px] text-white/40">
                TECHNICAL ARCHITECTURE • STATE PROPAGATION • TOOL LATENCIES • PUB/SUB EVENTBUS
              </p>
            </div>
          </div>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView("NONE");
            }}
            className="p-1 rounded hover:bg-white/10 text-white/50 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 grid grid-cols-12 gap-4 p-5 overflow-hidden font-mono text-xs">
          {/* Left Column (7 cols): The 10-Agent Intelligence Pipeline */}
          <div className="col-span-7 flex flex-col overflow-hidden bg-obsidian-950/80 rounded border border-white/10 p-3">
            <span className="text-[10px] font-bold text-cyber-cyan tracking-widest block mb-2">
              INTELLIGENCE EXECUTION PIPELINE (SESSION: {sessionId})
            </span>
            <div className="flex-1 overflow-y-auto space-y-1.5 pr-2">
              {PIPELINE_STAGES.map((node, idx) => {
                const isPassed = currentIdx > idx + 1 || missionPhase === "MISSION_COMPLETE";
                const isActive = currentIdx === idx + 1 && missionStatus === "RUNNING";

                return (
                  <div
                    key={node.id}
                    className={`p-2.5 rounded border transition-all ${
                      isActive
                        ? "bg-cyber-cyan/15 border-cyber-cyan text-white shadow-glow-cyan"
                        : isPassed
                        ? "bg-obsidian-900 border-pakistan-emerald/30 text-white/80"
                        : "bg-obsidian-900/50 border-white/5 text-white/40"
                    }`}
                  >
                    <div className="flex items-center justify-between mb-1">
                      <div className="flex items-center space-x-2">
                        {isPassed ? (
                          <CheckCircle2 className="w-3.5 h-3.5 text-pakistan-emerald" />
                        ) : isActive ? (
                          <CircleDashed className="w-3.5 h-3.5 text-cyber-cyan animate-spin" />
                        ) : (
                          <span className="w-3.5 h-3.5 rounded-full border border-white/20 inline-block" />
                        )}
                        <span className="font-bold text-xs">{node.label}</span>
                      </div>
                      <span className="text-[9px] px-1.5 py-0.2 rounded bg-white/5 font-semibold text-white/60">
                        {node.agent}
                      </span>
                    </div>

                    <div className="text-[10px] text-white/60 pl-5">
                      {node.role}
                    </div>
                    <div className="text-[9px] text-cyber-cyan/80 pl-5 pt-0.5 flex items-center space-x-1">
                      <Wrench className="w-2.5 h-2.5" />
                      <span>{node.tool}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Right Column (5 cols): Technical Environment, Key Pool, & SSE Raw Schema */}
          <div className="col-span-5 flex flex-col space-y-3 overflow-y-auto">
            {/* 27 Cloud Keys Rotation Engine */}
            <div className="p-3 rounded bg-obsidian-950/80 border border-white/10 space-y-1.5">
              <span className="text-[10px] font-bold text-pakistan-emerald tracking-widest block uppercase">
                RESILIENT KEY POOL (27 KEYS)
              </span>
              <div className="space-y-1 text-[10px] text-white/70">
                <div className="flex justify-between">
                  <span>Groq Cloud (Qwen-3.8-27b):</span>
                  <span className="text-white font-bold">13 Keys (Round-Robin)</span>
                </div>
                <div className="flex justify-between">
                  <span>Tavily Search:</span>
                  <span className="text-white font-bold">7 Keys (Round-Robin)</span>
                </div>
                <div className="flex justify-between">
                  <span>Google Gemini Flash:</span>
                  <span className="text-white font-bold">3 Keys (Failover)</span>
                </div>
                <div className="flex justify-between">
                  <span>Firecrawl Web Scraper:</span>
                  <span className="text-white font-bold">3 Keys (Failover)</span>
                </div>
                <div className="flex justify-between">
                  <span>Jina Reader:</span>
                  <span className="text-white font-bold">1 Key (Markdown Extractor)</span>
                </div>
              </div>
            </div>

            {/* SSE Streaming Event Contract */}
            <div className="p-3 rounded bg-obsidian-950/80 border border-white/10 space-y-1.5 flex-1 flex flex-col">
              <span className="text-[10px] font-bold text-cyber-cyan tracking-widest block uppercase">
                FASTAPI SSE EVENT CONTRACT
              </span>
              <pre className="p-2 rounded bg-black/60 text-[9px] text-white/60 font-mono overflow-x-auto flex-1 border border-white/5">
{`{
  "event_id": "evt-uuid",
  "session_id": "${sessionId}",
  "event_type": "CANDIDATE_EXTRACTED",
  "agent_id": "europe_scout",
  "component_type": "WORKFLOW",
  "phase": "${missionPhase}",
  "severity": "SUCCESS",
  "payload": {
    "scholarship_id": "sch-eu-0042",
    "name": "Stipendium Hungaricum",
    "bilateral_quota": true
  }
}`}
              </pre>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-2.5 bg-obsidian-950 border-t border-white/10 flex items-center justify-between font-mono text-[10px] text-white/40">
          <span>PRESS &apos;X&apos; OR ESC TO TOGGLE X-RAY VIEW</span>
          <button
            onClick={() => {
              sound.playClick();
              setOverlayView("NONE");
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
