"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { X, Sliders, Zap, Check, RotateCcw, AlertTriangle, ShieldCheck } from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { Region } from "@/lib/types";

export const MissionModifierOverlay: React.FC = () => {
  const {
    overlayView,
    setOverlayView,
    judgeParams,
    setJudgeParams,
    redeployWithModifier,
  } = useCommandStore();

  if (overlayView !== "MODIFIER") return null;

  const handleRegionToggle = (r: Region) => {
    sound.playClick();
    setJudgeParams({
      activeRegions: {
        ...judgeParams.activeRegions,
        [r]: !judgeParams.activeRegions[r],
      },
    });
  };

  const handleRedeploy = () => {
    sound.playBoot();
    redeployWithModifier();
    setOverlayView("NONE");
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-6 animate-in fade-in duration-200 select-none">
      <div className="relative w-full max-w-2xl bg-obsidian-900 border border-cyber-cyan/50 rounded-lg shadow-glow-cyan flex flex-col overflow-hidden corner-bracket">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-3.5 bg-obsidian-950 border-b border-white/10">
          <div className="flex items-center space-x-2.5">
            <Sliders className="w-4 h-4 text-cyber-cyan" />
            <div>
              <h3 className="font-mono text-sm font-black tracking-wider text-white">
                LIVE MISSION MODIFIER // JUDGE TACTICAL OVERRIDE
              </h3>
              <p className="font-mono text-[10px] text-white/40">
                INTERVENE IN REAL-TIME MISSION CONSTRAINTS & RE-ROUTE SCOUT QUERY VECTORS
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

        {/* Form Controls */}
        <div className="p-5 font-mono text-xs space-y-4">
          {/* Full Funding Toggle */}
          <div className="flex items-center justify-between p-3 rounded bg-obsidian-950 border border-white/10">
            <div>
              <span className="font-bold text-white block">FULL FUNDING COVERAGE ONLY</span>
              <span className="text-[10px] text-white/50">
                Filter out tuition-only scholarships; require accommodation + living stipend.
              </span>
            </div>
            <button
              onClick={() => {
                sound.playClick();
                setJudgeParams({ fullFundingOnly: !judgeParams.fullFundingOnly });
              }}
              className={`w-12 h-6 flex items-center rounded-full p-1 transition-colors ${
                judgeParams.fullFundingOnly ? "bg-pakistan-emerald justify-end" : "bg-white/20 justify-start"
              }`}
            >
              <div className="w-4 h-4 rounded-full bg-obsidian-950" />
            </button>
          </div>

          {/* Regional Scout Matrix Checkboxes */}
          <div className="space-y-1.5">
            <span className="text-[10px] text-white/50 font-bold uppercase tracking-wider block">
              ACTIVE REGIONAL TARGET FLEET
            </span>
            <div className="grid grid-cols-5 gap-2">
              {(["Europe", "Asia", "Americas", "MENA", "Oceania"] as Region[]).map((r) => {
                const active = judgeParams.activeRegions[r];
                return (
                  <button
                    key={r}
                    onClick={() => handleRegionToggle(r)}
                    className={`py-2 px-1 rounded border text-center transition-all ${
                      active
                        ? "bg-cyber-cyan/15 border-cyber-cyan text-cyber-cyan font-bold shadow-glow-cyan"
                        : "bg-obsidian-950 border-white/10 text-white/40"
                    }`}
                  >
                    <span className="block text-[10px]">{r.toUpperCase()}</span>
                    <span className="text-[9px] opacity-75">{active ? "ACTIVE" : "OFF"}</span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* IELTS English Waiver Toggle */}
          <div className="flex items-center justify-between p-3 rounded bg-obsidian-950 border border-white/10">
            <div>
              <span className="font-bold text-white block">STRICT IELTS REQUIREMENT</span>
              <span className="text-[10px] text-white/50">
                When OFF, prioritize scholarships accepting Pakistani English Medium of Instruction (MOI).
              </span>
            </div>
            <button
              onClick={() => {
                sound.playClick();
                setJudgeParams({ ieltsRequired: !judgeParams.ieltsRequired });
              }}
              className={`w-12 h-6 flex items-center rounded-full p-1 transition-colors ${
                judgeParams.ieltsRequired ? "bg-cyber-cyan justify-end" : "bg-white/20 justify-start"
              }`}
            >
              <div className="w-4 h-4 rounded-full bg-obsidian-950" />
            </button>
          </div>

          {/* Max Out-of-Pocket Budget Slider */}
          <div className="p-3 rounded bg-obsidian-950 border border-white/10 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-bold text-white">MAX OUT-OF-POCKET BUDGET CEILING</span>
              <span className="font-black text-warning-amber text-sm">
                PKR {judgeParams.maxBudgetPkr.toLocaleString()}
              </span>
            </div>
            <input
              type="range"
              min="50000"
              max="1000000"
              step="25000"
              value={judgeParams.maxBudgetPkr}
              onChange={(e) => setJudgeParams({ maxBudgetPkr: Number(e.target.value) })}
              className="w-full accent-cyber-cyan cursor-pointer"
            />
            <div className="flex justify-between text-[9px] text-white/40">
              <span>PKR 50,000 (Low-income)</span>
              <span>PKR 500,000</span>
              <span>PKR 1,000,000 (High buffer)</span>
            </div>
          </div>
        </div>

        {/* Action Button */}
        <div className="p-4 bg-obsidian-950 border-t border-white/10 flex items-center justify-between">
          <button
            onClick={() => {
              sound.playClick();
              setOverlayView("NONE");
            }}
            className="px-4 py-2 rounded text-white/60 hover:text-white font-mono text-xs transition-colors"
          >
            CANCEL
          </button>

          <button
            onClick={handleRedeploy}
            className="flex items-center space-x-2 px-5 py-2 rounded font-mono text-xs font-bold bg-cyber-cyan hover:bg-cyan-300 text-obsidian-950 border border-cyber-cyan shadow-glow-cyan transition-all"
          >
            <Zap className="w-3.5 h-3.5 fill-current" />
            <span>REDEPLOY INTELLIGENCE FLEET</span>
          </button>
        </div>
      </div>
    </div>
  );
};
