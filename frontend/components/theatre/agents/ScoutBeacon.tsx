"use client";

import React from "react";
import { motion } from "framer-motion";
import { GlassSurface } from "@/components/ui/glass/GlassSurface";
import { RegionalScoutData, ScoutState } from "@/lib/fleet/types";
import { ScoutToolActivity } from "./ScoutToolActivity";

export interface ScoutBeaconProps {
  scout: RegionalScoutData;
  isFocused?: boolean;
  onSelect?: () => void;
  className?: string;
}

export const ScoutBeacon: React.FC<ScoutBeaconProps> = ({
  scout,
  isFocused = false,
  onSelect,
  className = "",
}) => {
  const {
    region,
    displayName,
    state,
    progress,
    activeTool,
    currentOperation,
    sources,
    candidates,
    reportReady,
    pakistanQuotaSeats,
  } = scout;

  // Determine State Color & Pulse Styling
  const getStateMeta = (scoutState: ScoutState) => {
    switch (scoutState) {
      case "IDLE":
        return {
          label: "STANDBY",
          color: "rgba(180, 210, 225, 0.4)",
          pulse: false,
          glow: "none",
        };
      case "DEPLOYING":
        return {
          label: "DEPLOYING",
          color: "#7DD3FC",
          pulse: true,
          glow: "0 0 14px rgba(125, 211, 252, 0.4)",
        };
      case "RECEIVING_COMMAND":
        return {
          label: "RECEIVING COMMAND",
          color: "#38BDF8",
          pulse: true,
          glow: "0 0 16px rgba(56, 189, 248, 0.4)",
        };
      case "ACKNOWLEDGING":
        return {
          label: "ACKNOWLEDGED",
          color: "#10B981",
          pulse: true,
          glow: "0 0 16px rgba(16, 185, 129, 0.4)",
        };
      case "SEARCHING":
      case "FILTERING":
        return {
          label: "SEARCHING PORTALS",
          color: "#38BDF8",
          pulse: true,
          glow: "0 0 18px rgba(56, 189, 248, 0.45)",
        };
      case "SCRAPING":
        return {
          label: "SCRAPING DOM",
          color: "#F97316",
          pulse: true,
          glow: "0 0 18px rgba(249, 115, 22, 0.4)",
        };
      case "EXTRACTING":
      case "NORMALIZING":
        return {
          label: "EXTRACTING DATA",
          color: "#D4AF37",
          pulse: true,
          glow: "0 0 20px rgba(212, 175, 55, 0.4)",
        };
      case "DISCOVERING":
        return {
          label: "SOURCES DISCOVERED",
          color: "#34D399",
          pulse: true,
          glow: "0 0 16px rgba(52, 211, 153, 0.35)",
        };
      case "ASSEMBLING_REPORT":
      case "REPORT_READY":
        return {
          label: "REPORT ASSEMBLED",
          color: "#D4AF37",
          pulse: true,
          glow: "0 0 22px rgba(212, 175, 55, 0.45)",
        };
      case "RETURNING":
        return {
          label: "REPORT TRANSMITTING",
          color: "#D4AF37",
          pulse: true,
          glow: "0 0 20px rgba(212, 175, 55, 0.4)",
        };
      case "COMPLETE":
        return {
          label: "SECTOR RESOLVED",
          color: "#10B981",
          pulse: false,
          glow: "0 0 14px rgba(16, 185, 129, 0.3)",
        };
      case "FALLBACK":
        return {
          label: "FALLBACK SEARCH ACTIVE",
          color: "#F59E0B",
          pulse: true,
          glow: "0 0 18px rgba(245, 158, 11, 0.45)",
        };
      case "RECOVERING":
        return {
          label: "RECOVERING",
          color: "#38BDF8",
          pulse: true,
          glow: "0 0 16px rgba(56, 189, 248, 0.4)",
        };
      case "FAILED":
      case "UNAVAILABLE":
        return {
          label: "SECTOR UNAVAILABLE (ISOLATED)",
          color: "#F43F5E",
          pulse: false,
          glow: "0 0 14px rgba(244, 63, 94, 0.35)",
        };
      default:
        return {
          label: scoutState,
          color: "#94A3B8",
          pulse: false,
          glow: "none",
        };
    }
  };

  const meta = getStateMeta(state);

  return (
    <motion.div
      onClick={onSelect}
      initial={{ opacity: 0.9, scale: 0.98 }}
      animate={{
        opacity: isFocused ? 1 : 0.88,
        scale: isFocused ? 1.02 : 1,
      }}
      whileHover={{ scale: 1.03, opacity: 1 }}
      transition={{ duration: 0.25 }}
      className={`cursor-pointer select-none group pointer-events-auto ${className}`}
    >
      <GlassSurface
        elevation={isFocused ? "elevated" : "flat"}
        className={`p-3.5 rounded-xl border backdrop-blur-xl transition-all duration-300 w-[270px] ${
          isFocused
            ? "border-sx-ice/60 shadow-[0_0_24px_rgba(56,189,248,0.25)] ring-1 ring-sx-ice/40 bg-black/80"
            : "border-white/[0.12] bg-black/60 hover:border-white/[0.22] hover:bg-black/75"
        }`}
      >
        {/* Top Header: Region Title, Status Beacon & Focus Prompt */}
        <div className="flex items-center justify-between gap-2 mb-2">
          <div className="flex items-center space-x-2 truncate">
            {/* Pulsing Regional Beacon Dot */}
            <span className="relative flex h-2 w-2 shrink-0">
              {meta.pulse && (
                <motion.span
                  className="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
                  style={{ backgroundColor: meta.color }}
                />
              )}
              <span
                className="relative inline-flex rounded-full h-2 w-2"
                style={{ backgroundColor: meta.color }}
              />
            </span>

            <div className="truncate">
              <span className="text-xs font-mono tracking-wider text-white font-bold uppercase truncate block">
                {region} SCOUT
              </span>
              <span className="text-[10px] font-mono text-zinc-400 block mt-0.5">
                AUTONOMOUS FLEET
              </span>
            </div>
          </div>

          <div
            className="px-2 py-0.5 rounded text-[10px] font-mono tracking-wider font-semibold uppercase shrink-0"
            style={{
              borderColor: `${meta.color}40`,
              backgroundColor: `${meta.color}15`,
              color: meta.color,
              borderWidth: 1,
            }}
          >
            {meta.label}
          </div>
        </div>

        {/* Active Tool Chip Context (§12, §13) */}
        {activeTool ? (
          <div className="my-1.5">
            <ScoutToolActivity tool={activeTool} className="w-full justify-center" />
          </div>
        ) : (
          <div className="text-[11px] font-mono text-zinc-300 truncate bg-white/[0.04] px-2 py-1 rounded border border-white/[0.06] my-1.5">
            {currentOperation}
          </div>
        )}

        {/* Discovery Summary Stats: Sources & Candidates Badges */}
        <div className="flex items-center justify-between gap-1.5 pt-1.5 border-t border-white/[0.08] text-[10px] font-mono">
          <div className="flex items-center space-x-1 text-zinc-400 truncate">
            <span className="text-emerald-400 font-semibold">{sources.length}</span>
            <span>SOURCES</span>
          </div>

          <div className="flex items-center space-x-1 text-zinc-400 truncate">
            <span className="text-amber-300 font-bold">{candidates.length}</span>
            <span>CANDIDATES</span>
          </div>

          {pakistanQuotaSeats > 0 && (
            <div className="text-amber-400 font-semibold truncate">
              {pakistanQuotaSeats} SEATS
            </div>
          )}
        </div>

        {/* Mini Progress Bar */}
        <div className="w-full h-1 bg-white/[0.08] rounded-full overflow-hidden mt-2">
          <motion.div
            className="h-full bg-sx-ice"
            animate={{ width: `${progress}%` }}
            transition={{ duration: 0.6, ease: "easeOut" }}
          />
        </div>
      </GlassSurface>
    </motion.div>
  );
};
