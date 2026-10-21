"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import { GlassSurface } from "@/components/ui/glass/GlassSurface";
import { GlassInset } from "@/components/ui/glass/GlassInset";
import { GlassDivider } from "@/components/ui/glass/GlassDivider";
import { CommanderState, CommanderDirective } from "@/lib/agents/types";
import { SectorReportSummary } from "@/lib/communication/types";
import { GlobalFleetStats } from "@/lib/fleet/types";

export interface CommanderConsoleProps {
  state: CommanderState;
  mission: string;
  constraints: string[];
  availableActions: string[];
  nextDecision: string;
  currentDecision: string | null;
  activeDirective: CommanderDirective | null;
  incomingReport?: SectorReportSummary | null;
  receivedReports?: SectorReportSummary[];
  globalFleetStats?: GlobalFleetStats;
  isFocused?: boolean;
  onFocus?: () => void;
  className?: string;
}

export const CommanderConsole: React.FC<CommanderConsoleProps> = ({
  state,
  mission,
  constraints,
  availableActions,
  nextDecision,
  currentDecision,
  activeDirective,
  incomingReport,
  receivedReports = [],
  globalFleetStats,
  isFocused = true,
  onFocus,
  className = "",
}) => {
  // Determine state styling and badge details
  const getStateMeta = () => {
    switch (state) {
      case "IDLE":
        return {
          label: "STANDBY",
          pulse: false,
          color: "rgba(180, 210, 225, 0.4)",
          glow: "none",
        };
      case "THINKING":
        return {
          label: "EVALUATING MISSION",
          pulse: true,
          color: "#D4AF37",
          glow: "0 0 16px rgba(212, 175, 55, 0.25)",
        };
      case "DECIDING":
        return {
          label: "FORMING DECISION",
          pulse: true,
          color: "#D4AF37",
          glow: "0 0 20px rgba(212, 175, 55, 0.35)",
        };
      case "DIRECTING":
        return {
          label: "ISSUING DIRECTIVE",
          pulse: true,
          color: "#38BDF8",
          glow: "0 0 24px rgba(56, 189, 248, 0.35)",
        };
      case "WAITING":
        return {
          label: "AWAITING FLEET INTELLIGENCE",
          pulse: true,
          color: "#38BDF8",
          glow: "0 0 16px rgba(56, 189, 248, 0.25)",
        };
      case "RECEIVING":
        return {
          label: "RECEIVING REPORT",
          pulse: true,
          color: "#10B981",
          glow: "0 0 20px rgba(16, 185, 129, 0.3)",
        };
      case "SYNTHESIZING":
        return {
          label: "SYNTHESIZING GLOBAL FLEET",
          pulse: true,
          color: "#F59E0B",
          glow: "0 0 24px rgba(245, 158, 11, 0.35)",
        };
      case "COMPLETE":
        return {
          label: "GLOBAL MISSION RESOLVED",
          pulse: false,
          color: "#10B981",
          glow: "0 0 18px rgba(16, 185, 129, 0.25)",
        };
    }
  };

  const meta = getStateMeta();

  return (
    <div
      onClick={onFocus}
      className={`relative transition-all duration-300 cursor-pointer ${
        isFocused ? "opacity-100 scale-100" : "opacity-85 scale-[0.98]"
      } ${className}`}
    >
      <GlassSurface
        elevation="elevated"
        className={`relative overflow-hidden p-5 transition-all duration-500 rounded-2xl ${
          state === "RECEIVING"
            ? "border-sx-emerald shadow-[0_0_36px_rgba(16,185,129,0.35)] ring-1 ring-sx-emerald/40"
            : state === "SYNTHESIZING"
            ? "border-sx-gold shadow-[0_0_40px_rgba(212,175,55,0.4)] ring-1 ring-sx-gold/50"
            : isFocused
            ? "border-sx-gold/50 shadow-[0_0_32px_rgba(212,175,55,0.2)]"
            : "border-white/[0.14]"
        }`}
      >
        {/* State Atmospheric Illumination Backlight */}
        {state === "THINKING" && (
          <motion.div
            className="absolute inset-0 pointer-events-none bg-radial-gradient from-[rgba(212,175,55,0.08)] to-transparent"
            animate={{ opacity: [0.3, 0.7, 0.3] }}
            transition={{ duration: 3.2, repeat: Infinity, ease: "easeInOut" }}
          />
        )}
        {state === "DIRECTING" && (
          <motion.div
            className="absolute inset-0 pointer-events-none bg-radial-gradient from-[rgba(56,189,248,0.1)] to-transparent"
            animate={{ opacity: [0.4, 0.8, 0.4] }}
            transition={{ duration: 2.4, repeat: Infinity, ease: "easeInOut" }}
          />
        )}
        {state === "RECEIVING" && (
          <motion.div
            className="absolute inset-0 pointer-events-none bg-radial-gradient from-[rgba(16,185,129,0.12)] to-transparent"
            animate={{ opacity: [0.4, 0.85, 0.4] }}
            transition={{ duration: 2.0, repeat: Infinity, ease: "easeInOut" }}
          />
        )}
        {state === "SYNTHESIZING" && (
          <motion.div
            className="absolute inset-0 pointer-events-none bg-radial-gradient from-[rgba(212,175,55,0.14)] to-transparent"
            animate={{ opacity: [0.4, 0.9, 0.4] }}
            transition={{ duration: 2.4, repeat: Infinity, ease: "easeInOut" }}
          />
        )}

        {/* Header: Authority Identity & Node Status */}
        <div className="flex items-start justify-between gap-4 mb-2.5">
          <div className="space-y-1">
            <div className="flex items-center space-x-2">
              <span className="relative flex h-2.5 w-2.5">
                {meta.pulse && (
                  <motion.span
                    className="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
                    style={{ backgroundColor: meta.color }}
                  />
                )}
                <span
                  className="relative inline-flex rounded-full h-2.5 w-2.5"
                  style={{ backgroundColor: meta.color }}
                />
              </span>
              <span className="text-[10px] font-mono tracking-[0.2em] text-sx-gold uppercase font-medium">
                CENTRAL INTELLIGENCE // ORIGIN: PAKISTAN
              </span>
            </div>
            <h2 className="text-xl font-sans font-bold tracking-tight text-sx-text-primary">
              ScholarX Commander
            </h2>
          </div>

          <div className="flex flex-col items-end space-y-1">
            <div
              className="px-2.5 py-1 rounded border text-[10px] font-mono tracking-wider uppercase font-semibold"
              style={{
                borderColor: `${meta.color}40`,
                backgroundColor: `${meta.color}15`,
                color: meta.color,
                boxShadow: meta.glow,
              }}
            >
              {meta.label}
            </div>
            <span className="text-[10px] font-mono text-zinc-400">
              STATUS: ACTIVE INTELLIGENCE
            </span>
          </div>
        </div>

        <GlassDivider />

        {/* Dynamic State Machine Body */}
        <div className="my-2.5 min-h-[140px]">
          <AnimatePresence mode="wait">
            {/* 1. IDLE State */}
            {state === "IDLE" && (
              <motion.div
                key="idle"
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -4 }}
                transition={{ duration: 0.35 }}
                className="space-y-3"
              >
                <div className="text-xs font-mono uppercase tracking-wider text-sx-text-tertiary">
                  ACTIVE MISSION OBJECTIVE
                </div>
                <p className="text-sm font-sans text-sx-text-primary leading-relaxed font-medium">
                  {mission}
                </p>
                <GlassInset className="p-3">
                  <div className="text-[10px] font-mono uppercase text-sx-text-tertiary mb-1">
                    PIPELINE READINESS
                  </div>
                  <div className="text-xs font-sans text-sx-text-secondary">
                    Standby for Student Intake Document Ingestion (Matric/Intermediate, IELTS, HEC transcript).
                  </div>
                </GlassInset>
              </motion.div>
            )}

            {/* 2. THINKING State */}
            {state === "THINKING" && (
              <motion.div
                key="thinking"
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -4 }}
                transition={{ duration: 0.35 }}
                className="space-y-3"
              >
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-sx-gold animate-pulse" />
                  <div className="text-sm font-sans font-semibold text-sx-gold">
                    FORMULATING GLOBAL DISCOVERY SWEEP
                  </div>
                </div>

                <div className="space-y-1.5">
                  <div className="text-[10px] font-mono uppercase tracking-wider text-sx-text-tertiary">
                    ACTIVE PAKISTAN CONSTRAINTS
                  </div>
                  <ul className="space-y-1 text-xs font-sans text-sx-text-secondary">
                    {constraints.slice(0, 3).map((c, i) => (
                      <li key={i} className="flex items-start space-x-1.5">
                        <span className="text-sx-gold font-mono">&bull;</span>
                        <span>{c}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </motion.div>
            )}

            {/* 3. DIRECTING State */}
            {state === "DIRECTING" && (
              <motion.div
                key="directing"
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -4 }}
                transition={{ duration: 0.35 }}
                className="space-y-3"
              >
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-sx-ice animate-ping" />
                  <div className="text-sm font-sans font-bold text-sx-ice">
                    DEPLOYING 5 REGIONAL RESEARCH SCOUTS
                  </div>
                </div>

                <GlassInset className="p-3 space-y-2 border-sx-ice/30">
                  <div className="flex items-center justify-between text-[10px] font-mono text-sx-text-tertiary">
                    <span>FLEET DEPLOYMENT</span>
                    <span className="text-sx-ice font-semibold">5 CONTINENTS TARGETED</span>
                  </div>
                  <p className="text-xs font-sans text-sx-text-primary leading-relaxed font-medium">
                    Europe, Asia, Americas, MENA, and Oceania workflows initialized with Pakistan-optimized queries.
                  </p>
                </GlassInset>
              </motion.div>
            )}

            {/* 4. WAITING State */}
            {state === "WAITING" && (
              <motion.div
                key="waiting"
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -4 }}
                transition={{ duration: 0.35 }}
                className="space-y-3"
              >
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-sx-ice animate-pulse" />
                  <div className="text-sm font-sans font-semibold text-sx-ice">
                    MONITORING 5 PARALLEL RESEARCH WORKFLOWS
                  </div>
                </div>

                <GlassInset className="p-3 space-y-2 border-sx-ice/20">
                  <div className="flex items-center justify-between text-[10px] font-mono text-sx-text-tertiary">
                    <span>COORDINATED FLEET STATUS</span>
                    <span className="text-sx-ice font-semibold">ACTIVE EXECUTION</span>
                  </div>
                  <p className="text-xs font-sans text-sx-text-secondary leading-relaxed">
                    Scouts actively utilizing Tavily Search, Firecrawl, Jina Reader, and Crawl4AI across continental registries.
                  </p>
                </GlassInset>
              </motion.div>
            )}

            {/* 5. RECEIVING State */}
            {state === "RECEIVING" && (
              <motion.div
                key="receiving"
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -4 }}
                transition={{ duration: 0.35 }}
                className="space-y-3"
              >
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-sx-emerald animate-ping" />
                  <div className="text-sm font-sans font-bold text-sx-emerald">
                    INCOMING REGIONAL TRANSMISSIONS
                  </div>
                </div>

                <GlassInset className="p-3 space-y-2 border-sx-emerald/30">
                  <div className="flex items-center justify-between text-[10px] font-mono text-sx-text-tertiary">
                    <span>REPORT PACKETS DOCKING</span>
                    <span className="text-sx-emerald font-semibold">CURVED FLIGHT ARCS</span>
                  </div>
                  <p className="text-xs font-sans text-sx-text-primary leading-relaxed font-medium">
                    Regional report packages arriving at Pakistan origin node with verified quota seats.
                  </p>
                </GlassInset>
              </motion.div>
            )}

            {/* 6. SYNTHESIZING State (§35, §36 Global Aggregation) */}
            {(state === "SYNTHESIZING" || state === "COMPLETE") && (
              <motion.div
                key="synthesizing"
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -4 }}
                transition={{ duration: 0.35 }}
                className="space-y-3"
              >
                <div className="flex items-center space-x-2">
                  <span className="w-2 h-2 rounded-full bg-sx-gold animate-ping" />
                  <div className="text-sm font-sans font-bold text-sx-gold">
                    {state === "COMPLETE"
                      ? "GLOBAL DISCOVERY SYNTHESIS COMPLETE"
                      : "SYNTHESIZING GLOBAL FLEET INTELLIGENCE"}
                  </div>
                </div>

                <GlassInset className="p-3.5 space-y-2.5 border-sx-gold/30 bg-black/60">
                  <div className="flex items-center justify-between text-[11px] font-mono text-zinc-400">
                    <span className="uppercase tracking-wider">GLOBAL SYNTHESIS REPORT</span>
                    <span className="text-sx-gold font-semibold">5 CONTINENTS AUDITED</span>
                  </div>

                  <p className="text-xs font-sans text-zinc-200 leading-relaxed font-medium">
                    {state === "COMPLETE"
                      ? "Discovery completed across all regional registries. 13 high-confidence opportunities verified with 960+ bilateral Pakistan quota seats."
                      : "Aggregating regional candidate packages into centralized Pakistan eligibility pool with verified quota attribution."}
                  </p>

                  <div className="pt-2 border-t border-white/[0.08] space-y-1">
                    <div className="text-[10px] font-mono text-zinc-400 uppercase tracking-wider">
                      COMMAND DECISION // OPERATIONAL DISPATCH
                    </div>
                    <div className="text-xs font-sans font-bold text-white leading-snug">
                      {currentDecision || "DISPATCH TO SPECIALIST FLEET // 15-DIMENSION ELIGIBILITY & SKEPTIC SCRUTINY"}
                    </div>
                  </div>
                </GlassInset>
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        <GlassDivider />

        {/* Footer: Central Advisory Architecture Specs */}
        <div className="mt-3 flex items-center justify-between text-[10px] font-mono text-sx-text-tertiary">
          <span>INTELLIGENCE: CENTRAL ADVISORY COMMAND</span>
          <span>GLOBAL REACH: 5 CONTINENTS MONITORED</span>
        </div>
      </GlassSurface>
    </div>
  );
};
