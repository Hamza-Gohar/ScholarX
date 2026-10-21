"use client";

import React from "react";
import {
  DiscoveredSource,
  ScholarshipCandidateSummary,
} from "@/lib/communication/types";
import { ToolActivityMeta } from "@/lib/fleet/types";
import { ScoutToolActivity } from "./ScoutToolActivity";
import { CandidateStack } from "./CandidateStack";

export interface ResearchWorkspaceProps {
  activeQuery?: string;
  activeTool?: ToolActivityMeta | null;
  sources: DiscoveredSource[];
  candidates: ScholarshipCandidateSummary[];
  reportReady?: boolean;
  className?: string;
}

export const ResearchWorkspace: React.FC<ResearchWorkspaceProps> = ({
  activeQuery,
  activeTool,
  sources,
  candidates,
  reportReady = false,
  className = "",
}) => {
  return (
    <div className={`space-y-2.5 ${className}`}>
      {/* 0. Contextual Computational Tool Indicator (§12, §13) */}
      {activeTool && (
        <div className="flex items-center justify-between">
          <ScoutToolActivity tool={activeTool} className="w-full" />
        </div>
      )}

      {/* 1. Active Query Stream (Clean search operation, no raw log dump) */}
      {activeQuery && (
        <div className="rounded border border-sx-ice/30 bg-black/60 p-2 text-[10px] font-mono space-y-1">
          <div className="flex items-center justify-between text-sx-ice font-bold">
            <span className="flex items-center space-x-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-sx-ice animate-ping" />
              <span>ACTIVE RESEARCH QUERY</span>
            </span>
            <span className="text-[9px] px-1.5 py-0.2 rounded bg-sx-ice/15 border border-sx-ice/30 text-sx-ice font-semibold">
              TAVILY + ACADEMIC REGISTRY
            </span>
          </div>
          <div className="text-sx-text-primary text-[11px] font-mono leading-tight font-medium bg-black/40 px-2 py-1.5 rounded border border-white/[0.06] select-all">
            {activeQuery}
          </div>
        </div>
      )}

      {/* 2. Discovered Sources (Institutional Portals appearing visually) */}
      {sources.length > 0 && (
        <div className="space-y-1">
          <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary">
            <span>DISCOVERED SOURCES ({sources.length})</span>
            <span className="text-sx-emerald font-semibold">GOVERNMENT & PORTALS</span>
          </div>

          <div className="grid grid-cols-1 gap-1.5">
            {sources.map((src) => (
              <div
                key={src.id}
                className="flex items-center justify-between px-2.5 py-1.5 rounded border border-white/[0.08] bg-white/[0.02] text-[10px] font-mono"
              >
                <div className="flex items-center space-x-2 truncate">
                  <span className="w-1.5 h-1.5 rounded-full bg-sx-emerald" />
                  <span className="text-sx-text-primary font-medium truncate">
                    {src.domain}
                  </span>
                  <span className="text-sx-text-tertiary text-[9px]">
                    ({src.country})
                  </span>
                </div>
                {src.quotaSeats && (
                  <span className="px-1.5 py-0.5 rounded bg-sx-gold/15 border border-sx-gold/30 text-[9px] text-sx-gold font-bold shrink-0">
                    {src.quotaSeats} SEATS QUOTA
                  </span>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 3. Candidate Emergence & Progressive Disclosure Stack (§16, §17) */}
      {candidates.length > 0 && (
        <CandidateStack candidates={candidates} />
      )}

      {/* 4. Report Compression / Assembly Surface */}
      {reportReady && (
        <div className="rounded-lg border border-sx-gold/60 bg-gradient-to-r from-[rgba(212,175,55,0.15)] to-[rgba(212,175,55,0.05)] p-2.5 space-y-1.5 shadow-[0_0_24px_rgba(212,175,55,0.2)]">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-1.5">
              <span className="w-2 h-2 rounded-full bg-sx-gold animate-ping" />
              <span className="text-[10px] font-mono font-bold uppercase text-sx-gold">
                REPORT ASSEMBLED // READY FOR TRANSMISSION
              </span>
            </div>
            <span className="text-[9px] font-mono px-1.5 py-0.5 rounded bg-sx-gold/20 text-sx-gold font-semibold">
              COMPRESSED
            </span>
          </div>

          <div className="text-[10px] font-sans text-sx-text-secondary leading-snug">
            {candidates.length} Verified Candidates &bull; Pakistani Bilateral Quotas Confirmed. Ready for transmission to Root Commander.
          </div>
        </div>
      )}
    </div>
  );
};
