"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import { GlassSurface } from "@/components/ui/glass/GlassSurface";
import { GlassInset } from "@/components/ui/glass/GlassInset";
import { GlassDivider } from "@/components/ui/glass/GlassDivider";
import { AgentEntity } from "@/lib/agents/types";
import { DiscoveredSource, ScholarshipCandidateSummary } from "@/lib/communication/types";
import { ToolActivityMeta } from "@/lib/fleet/types";
import { ResearchWorkspace } from "./ResearchWorkspace";

export interface AgentCardProps {
  agent: AgentEntity;
  isFocused?: boolean;
  onFocus?: () => void;
  className?: string;
  activeQuery?: string;
  activeTool?: ToolActivityMeta | null;
  sources?: DiscoveredSource[];
  candidates?: ScholarshipCandidateSummary[];
  reportReady?: boolean;
}

export const AgentCard: React.FC<AgentCardProps> = ({
  agent,
  isFocused = false,
  onFocus,
  className = "",
  activeQuery,
  activeTool,
  sources,
  candidates,
  reportReady = false,
}) => {
  const {
    displayName,
    entityType,
    parentId,
    region,
    mission,
    state,
    currentOperation,
    finding,
    progress,
    spawnPhase = "SETTLED",
  } = agent;

  // Determine state indicator color & pulse across all 14 lifecycle states (§8)
  const getStateMeta = (lifecycleState: string) => {
    switch (lifecycleState) {
      case "IDLE":
        return {
          label: "STANDBY",
          color: "rgba(180, 210, 225, 0.4)",
          pulse: false,
          glow: "none",
        };
      case "RECEIVING":
      case "RECEIVING_COMMAND":
        return {
          label: "RECEIVING DIRECTIVE",
          color: "#38BDF8",
          pulse: true,
          glow: "0 0 16px rgba(56, 189, 248, 0.4)",
        };
      case "ACKNOWLEDGING":
        return {
          label: "DIRECTIVE ACKNOWLEDGED",
          color: "#10B981",
          pulse: true,
          glow: "0 0 18px rgba(16, 185, 129, 0.4)",
        };
      case "DEPLOYING":
        return {
          label: "DEPLOYING IN SECTOR",
          color: "#7DD3FC",
          pulse: true,
          glow: "0 0 18px rgba(125, 211, 252, 0.4)",
        };
      case "WORKING":
      case "SEARCHING":
      case "FILTERING":
        return {
          label: "SEARCHING PORTALS",
          color: "#38BDF8",
          pulse: true,
          glow: "0 0 20px rgba(56, 189, 248, 0.45)",
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
          label: "EXTRACTING SCHEMAS",
          color: "#D4AF37",
          pulse: true,
          glow: "0 0 20px rgba(212, 175, 55, 0.45)",
        };
      case "DISCOVERING":
        return {
          label: "SOURCES DISCOVERED",
          color: "#34D399",
          pulse: true,
          glow: "0 0 18px rgba(52, 211, 153, 0.4)",
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
          glow: "0 0 16px rgba(16, 185, 129, 0.3)",
        };
      case "FAILED":
        return {
          label: "SECTOR FAULT",
          color: "#EF4444",
          pulse: false,
          glow: "0 0 16px rgba(239, 68, 68, 0.3)",
        };
      default:
        return {
          label: lifecycleState,
          color: "#94A3B8",
          pulse: false,
          glow: "none",
        };
    }
  };

  const meta = getStateMeta(state);

  // Dynamic Spawn Rendering
  if (spawnPhase === "SEED") {
    return (
      <div className="flex items-center justify-center p-8">
        <div className="w-5 h-5 rounded-full bg-sx-ice shadow-[0_0_24px_rgba(56,189,248,0.9)] animate-pulse" />
      </div>
    );
  }

  if (spawnPhase === "SURFACE") {
    return (
      <div className="w-[340px] h-[160px] rounded-lg border border-sx-ice/50 bg-black/70 backdrop-blur-md flex flex-col items-center justify-center p-6 shadow-[0_0_36px_rgba(56,189,248,0.25)] space-y-3">
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-sx-ice animate-ping" />
          <span className="w-2.5 h-2.5 rounded-full bg-sx-ice" />
        </div>
        <div className="text-[11px] font-mono text-sx-ice tracking-[0.2em] uppercase font-bold text-center">
          DYNAMIC SPAWN // FORMING REGIONAL WORKSPACE
        </div>
        <div className="text-[9px] font-mono text-sx-text-tertiary">
          SECTOR: {region.toUpperCase()} &bull; TYPE: WORKFLOW
        </div>
      </div>
    );
  }

  return (
    <motion.div
      onClick={onFocus}
      initial={{ opacity: 1, scale: 1, y: 0 }}
      animate={{
        opacity: isFocused ? 1 : 0.88,
        scale: isFocused ? 1 : 0.98,
        y: 0,
      }}
      transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
      className={`relative transition-all duration-300 cursor-pointer ${className}`}
    >
      <GlassSurface
        elevation={isFocused ? "elevated" : "flat"}
        className={`relative overflow-hidden p-5 transition-all duration-300 ${
          state === "RECEIVING" || state === "RECEIVING_COMMAND"
            ? "border-sx-ice shadow-[0_0_36px_rgba(56,189,248,0.45)] ring-1 ring-sx-ice/50"
            : isFocused
            ? "border-sx-ice/50 shadow-[0_0_32px_rgba(56,189,248,0.2)]"
            : "border-white/[0.12]"
        }`}
      >
        {/* Subtle Receiving/Working Inner Highlight */}
        {["RECEIVING", "RECEIVING_COMMAND", "ACKNOWLEDGING", "WORKING", "SEARCHING", "EXTRACTING", "REPORTING", "DISCOVERING"].includes(
          state
        ) && (
          <motion.div
            className="absolute inset-0 pointer-events-none bg-radial-gradient from-[rgba(56,189,248,0.08)] to-transparent"
            animate={{ opacity: [0.3, 0.65, 0.3] }}
            transition={{ duration: 2.8, repeat: Infinity, ease: "easeInOut" }}
          />
        )}

        {/* LAYER 1: IDENTITY */}
        <div className="flex items-start justify-between gap-3 mb-3">
          <div className="space-y-0.5">
            <div className="flex items-center space-x-2">
              <span className="relative flex h-2 w-2">
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
              <span className="text-[10px] font-mono tracking-[0.2em] text-sx-ice uppercase font-medium">
                REGIONAL FLEET // {region}
              </span>
            </div>
            <h3 className="text-lg font-sans font-bold tracking-tight text-sx-text-primary">
              {displayName}
            </h3>
          </div>

          <div className="flex flex-col items-end space-y-1">
            <div className="flex items-center space-x-1.5">
              <div
                className="px-2 py-0.5 rounded border text-[9px] font-mono tracking-wider uppercase font-semibold"
                style={{
                  borderColor: `${meta.color}40`,
                  backgroundColor: `${meta.color}15`,
                  color: meta.color,
                  boxShadow: meta.glow,
                }}
              >
                {meta.label}
              </div>
            </div>
            <div className="flex items-center space-x-1.5 text-[9px] font-mono text-sx-text-tertiary">
              <span className="px-1.5 py-0.2 rounded bg-white/[0.05] border border-white/[0.08] text-sx-text-secondary">
                {entityType}
              </span>
              <span>PARENT: {parentId ? "COMMANDER" : "ROOT"}</span>
            </div>
          </div>
        </div>

        <GlassDivider />

        {/* LAYER 2: MISSION */}
        <div className="my-3">
          <div className="text-[9px] font-mono uppercase tracking-wider text-sx-text-tertiary mb-1">
            ASSIGNED DIRECTIVE
          </div>
          <p className="text-xs font-sans text-sx-text-primary leading-relaxed font-medium">
            {mission}
          </p>
        </div>

        {/* LAYER 3: CURRENT OPERATION */}
        <GlassInset className="p-2.5 my-3">
          <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary mb-1">
            <span>CURRENT OPERATION</span>
            <span className="text-sx-ice">{region.toUpperCase()} SECTOR</span>
          </div>
          <div className="text-xs font-mono font-medium text-sx-text-secondary truncate">
            {currentOperation}
          </div>
        </GlassInset>

        {/* LAYER 4: FINDINGS & RESEARCH WORKSPACE */}
        <div className="my-3">
          <div className="text-[9px] font-mono uppercase tracking-wider text-sx-text-tertiary mb-1">
            SECTOR FINDINGS
          </div>
          {activeQuery ||
          activeTool ||
          (sources && sources.length > 0) ||
          (candidates && candidates.length > 0) ||
          reportReady ? (
            <ResearchWorkspace
              activeQuery={activeQuery}
              activeTool={activeTool}
              sources={sources || []}
              candidates={candidates || []}
              reportReady={reportReady}
            />
          ) : (
            <div className="p-2.5 rounded border border-white/[0.06] bg-black/40 text-xs font-mono text-sx-text-secondary">
              {finding}
            </div>
          )}
        </div>

        {/* LAYER 5: PROGRESS */}
        <div className="mt-3 pt-2 border-t border-white/[0.06]">
          <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary mb-1.5">
            <span>LIFECYCLE PROGRESS</span>
            <span className="font-semibold text-sx-text-primary">{progress}%</span>
          </div>
          <div className="w-full h-1 bg-white/[0.08] rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-sx-ice"
              initial={{ width: 0 }}
              animate={{ width: `${progress}%` }}
              transition={{ duration: 0.6, ease: "easeOut" }}
            />
          </div>
        </div>
      </GlassSurface>
    </motion.div>
  );
};
