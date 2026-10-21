"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ScholarshipCandidateSummary } from "@/lib/communication/types";

export interface CandidateStackProps {
  candidates: ScholarshipCandidateSummary[];
  className?: string;
}

export const CandidateStack: React.FC<CandidateStackProps> = ({
  candidates,
  className = "",
}) => {
  const [selectedIndex, setSelectedIndex] = useState(0);

  if (!candidates || candidates.length === 0) return null;

  const activeCandidate = candidates[selectedIndex] || candidates[0];
  const otherCandidates = candidates.filter((_, idx) => idx !== selectedIndex);

  return (
    <div className={`space-y-2 select-none ${className}`}>
      {/* Header with Total Count and Stack Indicator */}
      <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary">
        <span className="flex items-center space-x-1.5">
          <span className="w-1.5 h-1.5 rounded-full bg-sx-gold animate-pulse" />
          <span className="font-semibold text-sx-gold">
            EMERGING CANDIDATES ({candidates.length})
          </span>
        </span>
        <span className="text-white/60">
          SHOWING #{selectedIndex + 1} OF {candidates.length}
        </span>
      </div>

      {/* Primary Highlighted Candidate Card (Crystallized Discovery) */}
      <AnimatePresence mode="wait">
        <motion.div
          key={activeCandidate.id}
          initial={{ opacity: 0, scale: 0.96, y: 4 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.96, y: -4 }}
          transition={{ duration: 0.3 }}
          className="rounded-lg border border-sx-gold/40 bg-gradient-to-br from-black/85 via-[rgba(26,20,8,0.9)] to-[rgba(212,175,55,0.08)] p-3 shadow-[0_0_20px_rgba(212,175,55,0.15)] space-y-2"
        >
          {/* Top Title & Funding Badge */}
          <div className="flex items-start justify-between gap-2">
            <div className="space-y-0.5 min-w-0">
              <h4 className="text-xs font-sans font-bold text-white tracking-tight leading-snug truncate">
                {activeCandidate.title}
              </h4>
              <div className="text-[10px] font-mono text-sx-text-tertiary flex items-center space-x-1.5 truncate">
                <span className="text-sx-ice">{activeCandidate.country}</span>
                <span>&bull;</span>
                <span className="truncate">{activeCandidate.degreeLevel}</span>
              </div>
            </div>

            <span className="px-2 py-0.5 rounded border border-sx-emerald/40 bg-sx-emerald/15 text-[9px] font-mono font-bold text-sx-emerald shrink-0">
              {activeCandidate.fundingType.toUpperCase()}
            </span>
          </div>

          {/* Key Scholarship Coverage Fields */}
          <div className="grid grid-cols-2 gap-2 pt-1.5 border-t border-white/[0.08] text-[10px] font-mono">
            <div className="p-1 rounded bg-black/40 border border-white/[0.04]">
              <div className="text-sx-text-tertiary text-[9px]">LIVING STIPEND</div>
              <div className="text-sx-text-secondary truncate font-medium">
                {activeCandidate.monthlyStipend}
              </div>
            </div>

            {activeCandidate.pakistanQuotaSeats ? (
              <div className="p-1 rounded bg-sx-gold/10 border border-sx-gold/25">
                <div className="text-sx-gold text-[9px] font-semibold">PAKISTAN QUOTA</div>
                <div className="text-sx-gold font-bold truncate">
                  {activeCandidate.pakistanQuotaSeats} DEDICATED SEATS
                </div>
              </div>
            ) : (
              <div className="p-1 rounded bg-black/40 border border-white/[0.04]">
                <div className="text-sx-text-tertiary text-[9px]">TUITION COVERAGE</div>
                <div className="text-sx-emerald truncate font-medium">
                  {activeCandidate.tuitionCoverage}
                </div>
              </div>
            )}
          </div>
        </motion.div>
      </AnimatePresence>

      {/* Progressive Disclosure Stack: Compact Clickable Pills for Remaining Opportunities */}
      {candidates.length > 1 && (
        <div className="flex flex-wrap gap-1.5 pt-0.5">
          {candidates.map((cand, idx) => (
            <button
              key={cand.id}
              onClick={() => setSelectedIndex(idx)}
              className={`px-2 py-1 rounded text-[9px] font-mono transition-all duration-200 border truncate max-w-[170px] ${
                idx === selectedIndex
                  ? "border-sx-gold/60 bg-sx-gold/20 text-sx-gold font-bold shadow-[0_0_8px_rgba(212,175,55,0.25)]"
                  : "border-white/[0.08] bg-black/50 text-sx-text-tertiary hover:text-sx-text-secondary hover:border-white/[0.16]"
              }`}
            >
              + {cand.title.split(" ")[0]} {cand.country ? `(${cand.country})` : ""}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};
