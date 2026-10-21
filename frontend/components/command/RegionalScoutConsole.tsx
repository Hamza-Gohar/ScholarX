"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { Region } from "@/lib/types";
import { Radio, Search, Database, Globe, ChevronRight, Zap, ExternalLink } from "lucide-react";
import { sound } from "@/lib/sound-fx";

interface ScoutConfig {
  region: Region;
  title: string;
  flag: string;
  themeColor: string;
  textColor: string;
  borderColor: string;
  primaryKeyPrograms: string[];
  targetCountries: string;
}

const SCOUT_CONFIGS: ScoutConfig[] = [
  {
    region: "Europe",
    title: "EUROPE SCOUT",
    flag: "🇪🇺",
    themeColor: "#00F0FF",
    textColor: "text-cyber-cyan",
    borderColor: "border-cyber-cyan/30",
    primaryKeyPrograms: ["DAAD (DE)", "Stipendium Hungaricum", "Erasmus+ Mundus", "SI Sweden"],
    targetCountries: "Germany • Hungary • Italy • Sweden • France",
  },
  {
    region: "Asia",
    title: "ASIA SCOUT",
    flag: "🇯🇵",
    themeColor: "#F43F5E",
    textColor: "text-rose-400",
    borderColor: "border-rose-500/30",
    primaryKeyPrograms: ["MEXT Embassy (JP)", "CSC Bilateral (CN)", "GKS Korean Govt", "Taiwan MOE"],
    targetCountries: "Japan • China • South Korea • Taiwan • Singapore",
  },
  {
    region: "Americas",
    title: "AMERICAS SCOUT",
    flag: "🇺🇸",
    themeColor: "#6366F1",
    textColor: "text-indigo-400",
    borderColor: "border-indigo-500/30",
    primaryKeyPrograms: ["Fulbright USEFP (US)", "Vanier CGS (CA)", "OAS Fellowships", "Colfuturo"],
    targetCountries: "United States • Canada • Brazil • Mexico",
  },
  {
    region: "MENA",
    title: "MENA SCOUT",
    flag: "🇸🇦",
    themeColor: "#00FF88",
    textColor: "text-pakistan-emerald",
    borderColor: "border-pakistan-emerald/30",
    primaryKeyPrograms: ["Turkiye Burslari", "KAUST Fellowship", "Qatar Foundation", "KFUPM Master's"],
    targetCountries: "Turkey • Saudi Arabia • UAE • Qatar",
  },
  {
    region: "Oceania",
    title: "OCEANIA SCOUT",
    flag: "🇦🇺",
    themeColor: "#FFB800",
    textColor: "text-warning-amber",
    borderColor: "border-warning-amber/30",
    primaryKeyPrograms: ["Australia Awards", "Melbourne Research (RTP)", "Manaaki New Zealand"],
    targetCountries: "Australia • New Zealand",
  },
];

export const RegionalScoutConsole: React.FC = () => {
  const {
    scouts,
    candidates,
    setSelectedScholarship,
    setOverlayView,
    setFocusedAgent,
    events,
  } = useCommandStore();

  const handleFocusScout = (cfg: ScoutConfig) => {
    sound.playClick();
    const scout = scouts[cfg.region];
    setFocusedAgent({
      agentId: `${cfg.region.toLowerCase()}_scout`,
      title: `${cfg.title} // REGIONAL AUTONOMOUS SCOUT`,
      role: `Deep Web Discovery for ${cfg.region}`,
      status: scout?.status || "STANDBY",
      region: cfg.region,
      task: scout?.currentQuery || `Scanning official ${cfg.region} ministries, HEC quotas, and university portals`,
      toolsUsed: ["Tavily Multi-Key (7 keys)", "Firecrawl Scraper (3 keys)", "Jina Reader", "Groq Qwen-3.8-27B"],
      queriesExecuted: [
        scout?.currentQuery || `fully funded scholarship pakistani students ${cfg.region}`,
        `HEC bilateral quota seats ${cfg.region} 2026 2027`,
        `university tuition waiver IELTS MOI certificate ${cfg.region}`,
      ],
      recentEvents: events.filter((e) => e.payload.region === cfg.region).slice(0, 10),
    });
  };

  return (
    <div className="flex flex-col space-y-2 h-full select-none">
      {/* Console Header */}
      <div className="flex items-center justify-between px-1">
        <div className="flex items-center space-x-2">
          <Globe className="w-3.5 h-3.5 text-cyber-cyan" />
          <span className="font-mono text-[10px] font-extrabold tracking-widest text-white/50">
            REGIONAL SCOUT CONSOLES
          </span>
        </div>
        <span className="font-mono text-[9px] px-1.5 py-0.2 rounded bg-white/5 text-cyber-cyan border border-cyber-cyan/30">
          5 LIVE OPERATORS
        </span>
      </div>

      {/* 5 Regional Scout Hardware Panels */}
      <div className="grid grid-cols-1 gap-2 flex-1 overflow-y-auto pr-1">
        {SCOUT_CONFIGS.map((cfg) => {
          const scout = scouts[cfg.region];
          const isActive = scout?.status === "ACTIVE" || scout?.status === "SCRAPING";
          const count = scout?.itemsFound || 0;
          const regionalCandidates = candidates.filter((c) => c.region === cfg.region);

          return (
            <div
              key={cfg.region}
              onClick={() => handleFocusScout(cfg)}
              className={`command-panel corner-bracket rounded-lg p-2.5 transition-all group flex flex-col justify-between border cursor-pointer ${
                isActive
                  ? "border-cyber-cyan/50 bg-obsidian-850 shadow-glow-cyan"
                  : "border-white/10 hover:border-white/20 bg-obsidian-900/80"
              }`}
            >
              {/* Header */}
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <span className="text-sm">{cfg.flag}</span>
                  <span className={`font-mono text-xs font-black tracking-wider ${cfg.textColor}`}>
                    {cfg.title}
                  </span>
                </div>

                <div className="flex items-center space-x-1.5">
                  <span
                    className={`w-2 h-2 rounded-full ${
                      isActive
                        ? "bg-pakistan-emerald animate-ping"
                        : count > 0
                        ? "bg-cyber-cyan"
                        : "bg-white/20"
                    }`}
                  />
                  <span className="font-mono text-[9px] text-white/50 uppercase font-semibold">
                    {scout?.status || "STANDBY"}
                  </span>
                </div>
              </div>

              {/* Target Countries */}
              <div className="text-[9px] font-mono text-white/40 truncate mt-1">
                TARGET: <span className="text-white/60">{cfg.targetCountries}</span>
              </div>

              {/* Pipeline Progression Indicators: SEARCH -> SCRAPE -> EXTRACT */}
              <div className="my-1 flex items-center justify-between bg-obsidian-950/80 px-2 py-1 rounded border border-white/5 font-mono text-[8px]">
                <span className={isActive ? "text-cyber-cyan font-bold" : "text-white/30"}>SEARCH</span>
                <span className="text-white/20">→</span>
                <span className={scout?.status === "SCRAPING" ? "text-warning-amber font-bold animate-pulse" : "text-white/30"}>SCRAPE</span>
                <span className="text-white/20">→</span>
                <span className={count > 0 ? "text-pakistan-emerald font-bold" : "text-white/30"}>EXTRACT</span>
                <span className="text-white/20">→</span>
                <span className={count > 0 ? "text-purple-400 font-bold" : "text-white/30"}>NORMALIZE</span>
              </div>

              {/* Live Query / Activity Ticker */}
              <div className="my-0.5 px-2 py-1 rounded bg-obsidian-950 border border-white/5 font-mono text-[10px] text-white/70 truncate flex items-center space-x-1.5">
                <Search className="w-3 h-3 text-white/40 flex-shrink-0" />
                <span className="truncate italic">
                  {scout?.currentQuery || scout?.lastActivity || "Standing by for target dispatch..."}
                </span>
              </div>

              {/* Bottom Metrics: Found & Inspect */}
              <div className="flex items-center justify-between pt-1 border-t border-white/5 font-mono text-[10px]">
                <div className="flex items-center space-x-1.5 text-white/60">
                  <Database className="w-3 h-3 text-white/40" />
                  <span>FOUND:</span>
                  <span className="font-bold text-white px-1.5 py-0.2 rounded bg-white/5">
                    {count}
                  </span>
                </div>

                {regionalCandidates.length > 0 && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      sound.playClick();
                      setSelectedScholarship(regionalCandidates[0]);
                      setOverlayView("AUDIT");
                    }}
                    className="flex items-center space-x-1 text-cyber-cyan hover:underline text-[9px] font-semibold"
                  >
                    <span>AUDIT ({regionalCandidates.length})</span>
                    <ChevronRight className="w-3 h-3" />
                  </button>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
