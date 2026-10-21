"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { TacticalWorldMap } from "./TacticalWorldMap";
import { Orbital3DGlobe } from "./Orbital3DGlobe";
import { CommanderConsole } from "@/components/command/CommanderConsole";
import { CandidatePipelineStream } from "@/components/command/CandidatePipelineStream";
import { Globe, Compass, Activity, Crosshair, Radar, Layers } from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { MapVisualMode } from "@/lib/types";

export const MapContainer: React.FC = () => {
  const {
    mapMode,
    setMapMode,
    mapVisualMode,
    setMapVisualMode,
    candidates,
    scouts,
  } = useCommandStore();

  const totalCandidates = candidates.length;
  const activeScoutsCount = Object.values(scouts).filter((s) => s.status !== "IDLE").length;

  return (
    <div className="relative w-full h-full flex flex-col space-y-2 overflow-hidden select-none">
      {/* 1. Top Section: Central Commander Console */}
      <div className="flex-shrink-0">
        <CommanderConsole />
      </div>

      {/* 2. Middle Section: World Operations Map Theater */}
      <div className="flex-1 relative command-panel corner-bracket rounded-lg overflow-hidden border border-white/10 flex flex-col min-h-0 bg-obsidian-950/80">
        {/* Map Header Bar */}
        <div className="flex items-center justify-between px-3 py-1.5 bg-obsidian-900/90 border-b border-white/10 z-10">
          <div className="flex items-center space-x-2.5">
            <Crosshair className="w-3.5 h-3.5 text-cyber-cyan animate-spin" style={{ animationDuration: "14s" }} />
            <span className="font-mono text-[11px] font-bold tracking-wider text-white">
              CENTRAL OPERATIONS THEATER
            </span>
            <span className="text-white/20 text-xs">|</span>
            <div className="flex items-center space-x-1.5 font-mono text-[10px] text-white/60">
              <span className="w-2 h-2 rounded-full bg-pakistan-emerald animate-ping" />
              <span>ORIGIN: PAKISTAN</span>
            </div>
          </div>

          {/* Tactical Visual Modes Selector (DEPLOYMENT, DISCOVERY, INTELLIGENCE) */}
          <div className="flex items-center space-x-2">
            <div className="flex items-center bg-obsidian-950 rounded border border-white/10 p-0.5">
              {(["DEPLOYMENT", "DISCOVERY", "INTELLIGENCE"] as MapVisualMode[]).map((mode) => (
                <button
                  key={mode}
                  onClick={() => {
                    sound.playClick();
                    setMapVisualMode(mode);
                  }}
                  className={`px-2 py-0.5 rounded font-mono text-[9px] font-bold transition-all ${
                    mapVisualMode === mode
                      ? "bg-cyber-cyan text-obsidian-950 shadow-glow-cyan"
                      : "text-white/50 hover:text-white"
                  }`}
                >
                  {mode}
                </button>
              ))}
            </div>

            {/* 2D / 3D Toggle */}
            <div className="flex items-center bg-obsidian-950 rounded border border-cyber-cyan/30 p-0.5">
              <button
                onClick={() => {
                  sound.playClick();
                  setMapMode("2D_TACTICAL");
                }}
                className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[9px] font-semibold transition-all ${
                  mapMode === "2D_TACTICAL"
                    ? "bg-cyber-cyan text-obsidian-950 shadow-glow-cyan"
                    : "text-white/60 hover:text-white"
                }`}
              >
                <Compass className="w-2.5 h-2.5" />
                <span>2D</span>
              </button>
              <button
                onClick={() => {
                  sound.playClick();
                  setMapMode("3D_GLOBE");
                }}
                className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[9px] font-semibold transition-all ${
                  mapMode === "3D_GLOBE"
                    ? "bg-cyber-cyan text-obsidian-950 shadow-glow-cyan"
                    : "text-white/60 hover:text-white"
                }`}
              >
                <Globe className="w-2.5 h-2.5" />
                <span>3D</span>
              </button>
            </div>
          </div>
        </div>

        {/* Viewport */}
        <div className="relative flex-1 w-full h-full min-h-[300px]">
          {mapMode === "2D_TACTICAL" ? <TacticalWorldMap /> : <Orbital3DGlobe />}
        </div>
      </div>

      {/* 3. Lower Section: Live Candidate Intelligence Dossier Stream */}
      <div className="flex-shrink-0">
        <CandidatePipelineStream />
      </div>
    </div>
  );
};
