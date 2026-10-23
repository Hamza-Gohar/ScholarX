"use client";

import React, { useState } from "react";
import { RoadmapPhaseBlock, RoadmapActionItem } from "@/lib/ranking/types";
import { 
  Building2, 
  Clock, 
  Coins, 
  AlertCircle, 
  CheckCircle2, 
  MapPin, 
  ExternalLink,
  ChevronRight,
  ShieldAlert,
  Calendar
} from "lucide-react";

export interface RoadmapJourneyProps {
  phases: RoadmapPhaseBlock[];
  totalPrepDays: number;
  totalBudgetPkr: number;
  className?: string;
}

export const RoadmapJourney: React.FC<RoadmapJourneyProps> = ({
  phases,
  totalPrepDays,
  totalBudgetPkr,
  className = "",
}) => {
  const [selectedPhaseIdx, setSelectedPhaseIdx] = useState<number>(0);
  const activePhase = phases[selectedPhaseIdx] || phases[0];

  return (
    <div
      className={`w-full max-w-[1240px] mx-auto rounded-xl border border-white/[0.12] bg-black/85 backdrop-blur-xl p-4 shadow-2xl transition-all duration-300 pointer-events-auto ${className}`}
    >
      {/* Top Banner: Final Advisor Strategy */}
      <div className="flex flex-col md:flex-row md:items-center justify-between border-b border-white/[0.08] pb-3 mb-3 gap-2">
        <div className="flex items-center space-x-2.5">
          <div className="w-7 h-7 rounded-lg bg-sx-verified/20 border border-sx-verified/40 flex items-center justify-center text-sx-verified shadow-[0_0_12px_rgba(16,185,129,0.25)]">
            <Building2 className="w-4 h-4" />
          </div>
          <div>
            <div className="text-[10px] font-mono text-sx-text-tertiary uppercase tracking-wider flex items-center gap-1.5">
              <span>FINAL ADVISOR AGENT</span>
              <span className="text-white/20">{"//"}</span>
              <span className="text-sx-verified font-semibold">PAKISTAN APPLICATION STRATEGY</span>
            </div>
            <div className="text-sm font-sans font-semibold text-white">
              Personalized Pakistan Execution Roadmap & Institutional Pathway
            </div>
          </div>
        </div>

        {/* Global Strategy Metrics */}
        <div className="flex items-center justify-between sm:justify-end space-x-4 text-left sm:text-right pt-1 sm:pt-0">
          <div>
            <div className="text-[9px] font-mono text-sx-text-tertiary uppercase">TOTAL TIMELINE</div>
            <div className="text-sm font-mono font-bold text-white flex items-center sm:justify-end gap-1">
              <Calendar className="w-3.5 h-3.5 text-sx-ice" />
              <span>{totalPrepDays} DAYS</span>
            </div>
          </div>
          <div>
            <div className="text-[9px] font-mono text-sx-text-tertiary uppercase">TOTAL BUDGET NEEDED</div>
            <div className="text-sm font-mono font-bold text-sx-gold flex items-center sm:justify-end gap-1">
              <Coins className="w-3.5 h-3.5" />
              <span>PKR {(totalBudgetPkr / 1000).toFixed(0)}k</span>
            </div>
          </div>
        </div>
      </div>

      {/* 6-Phase Linear Journey Scrubber (§17, §19) */}
      <div className="flex items-stretch gap-1.5 overflow-x-auto no-scrollbar pb-1 md:grid md:grid-cols-6 mb-3.5 touch-scroll">
        {phases.map((p, idx) => {
          const isCurrent = idx === selectedPhaseIdx;
          const hasBlocking = p.actions.some((a) => a.isBlocking);

          return (
            <button
              key={p.phase}
              onClick={() => setSelectedPhaseIdx(idx)}
              className={`text-left p-2 rounded-lg border transition-all text-[10px] font-mono relative overflow-hidden cursor-pointer min-w-[130px] shrink-0 md:shrink md:min-w-0 ${
                isCurrent
                  ? "bg-white/[0.08] border-sx-gold/60 text-white shadow-[0_0_15px_rgba(212,175,55,0.15)] ring-1 ring-sx-gold/30"
                  : "bg-black/50 border-white/[0.06] text-sx-text-tertiary hover:border-white/[0.15] hover:text-white/80"
              }`}
            >
              <div className="flex items-center justify-between mb-1">
                <span className={`font-bold ${isCurrent ? "text-sx-gold" : "text-white/50"}`}>
                  {p.phaseLabel}
                </span>
                {hasBlocking && (
                  <span className="w-1.5 h-1.5 rounded-full bg-sx-challenge animate-pulse" title="Contains blocking steps" />
                )}
              </div>
              <div className="text-[9px] truncate font-sans font-medium text-white/90">
                {p.title.split("&")[0]}
              </div>
              <div className="text-[8px] text-sx-text-tertiary mt-0.5">{p.timelineDaysRange}</div>
            </button>
          );
        })}
      </div>

      {/* Active Phase Detailed Actions Panel */}
      <div className="bg-white/[0.02] border border-white/[0.06] rounded-xl p-3 sm:p-3.5 mb-2">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between mb-2 pb-2 border-b border-white/[0.04] gap-1">
          <div className="flex flex-wrap items-center space-x-2">
            <span className="text-xs font-mono font-bold text-sx-gold">{activePhase.phaseLabel}:</span>
            <span className="text-xs font-sans font-bold text-white">{activePhase.title}</span>
            <span className="text-[10px] font-mono text-white/40">({activePhase.timelineDaysRange})</span>
          </div>
          <div className="text-[10px] font-mono text-sx-text-tertiary">
            Phase Estimated Cost: <span className="text-sx-gold font-bold">PKR {activePhase.totalCostPkr.toLocaleString()}</span>
          </div>
        </div>

        {/* Phase Critical Advisory */}
        {activePhase.criticalAdvisory && (
          <div className="flex items-start space-x-2 text-[10px] font-mono text-sx-amber/90 bg-sx-amber/10 border border-sx-amber/20 rounded-lg p-2 mb-3">
            <AlertCircle className="w-3.5 h-3.5 shrink-0 mt-0.5 text-sx-amber" />
            <span>ADVISOR DIRECTIVE: {activePhase.criticalAdvisory}</span>
          </div>
        )}

        {/* Actions List */}
        <div className="space-y-2">
          {activePhase.actions.map((act) => {
            const isBlocking = act.isBlocking;

            return (
              <div
                key={act.id}
                className="rounded-lg bg-black/60 border border-white/[0.08] p-2.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 text-xs"
              >
                {/* Left: Action Title & Details */}
                <div className="flex-1 min-w-0">
                  <div className="flex flex-wrap items-center gap-1.5 mb-1">
                    {/* Severity Badge */}
                    <span
                      className={`text-[9px] font-mono font-bold px-1.5 py-0.5 rounded border ${
                        act.severity === "BLOCKING"
                          ? "bg-sx-challenge/15 text-sx-challenge border-sx-challenge/30"
                          : act.severity === "REQUIRED"
                          ? "bg-sx-amber/15 text-sx-amber border-sx-amber/30"
                          : "bg-white/[0.06] text-white/60 border-white/[0.1]"
                      }`}
                    >
                      {act.severity}
                    </span>

                    <span className="font-sans font-semibold text-white/95">{act.title}</span>

                    {act.isPakistanSpecific && (
                      <span className="text-[9px] font-mono text-sx-verified bg-sx-verified/10 px-1 py-0.2 rounded border border-sx-verified/20">
                        PAKISTAN SPECIFIC
                      </span>
                    )}
                  </div>

                  <div className="text-[10px] font-sans text-sx-text-tertiary">
                    {act.purpose}
                  </div>

                  {act.assignedOffice && (
                    <div className="flex items-center space-x-1 text-[9px] font-mono text-sx-ice/80 mt-1">
                      <MapPin className="w-3 h-3 shrink-0" />
                      <span className="truncate">{act.assignedOffice}</span>
                    </div>
                  )}
                </div>

                {/* Right: Timing & Cost */}
                <div className="flex items-center justify-between sm:justify-end space-x-3 shrink-0 text-left sm:text-right text-[10px] font-mono pt-1.5 sm:pt-0 border-t sm:border-t-0 border-white/[0.04]">
                  <div className="text-sx-text-secondary flex items-center gap-1">
                    <Clock className="w-3 h-3 text-white/40 shrink-0" />
                    <span>{act.timingLabel}</span>
                  </div>

                  <div className="min-w-[80px]">
                    <span className="text-sx-text-tertiary block text-[9px]">EST. EXPENSE</span>
                    <span className="font-bold text-sx-gold">
                      {act.estimatedCostPkr === 0 ? "FREE" : `PKR ${act.estimatedCostPkr.toLocaleString()}`}
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Footer Navigation Tip */}
      <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary">
        <span>Click any phase above to inspect institutional prerequisites & office details.</span>
        <span>MANDATORY GATES: HEC DAS ATTESTATION // USAT TEST // DUAL DREAMAPPLY RECORD</span>
      </div>
    </div>
  );
};
