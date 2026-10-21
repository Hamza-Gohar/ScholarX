"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import { useCommandStore } from "@/lib/store";
import { CandidatePipelineStage, CandidateFlowItem } from "@/lib/types";
import { sound } from "@/lib/sound-fx";
import { ArrowRight, CheckCircle2, AlertTriangle, ShieldCheck } from "lucide-react";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";

const STAGES: { stage: CandidatePipelineStage; label: string; iconColor: string }[] = [
  { stage: "DISCOVERED", label: "DISCOVERED", iconColor: "text-cyber-cyan" },
  { stage: "ELIGIBILITY", label: "ELIGIBILITY", iconColor: "text-command-gold" },
  { stage: "COST", label: "TRUE COST", iconColor: "text-command-gold" },
  { stage: "DEADLINE", label: "DEADLINE", iconColor: "text-cyber-cyan" },
  { stage: "VERIFICATION", label: "VERIFIER", iconColor: "text-pakistan-green" },
  { stage: "SKEPTIC", label: "SKEPTIC", iconColor: "text-skeptic-rose" },
  { stage: "RANKING", label: "RANKED", iconColor: "text-pakistan-green" },
];

export const CandidateStage: React.FC = () => {
  const { activeCandidatesFlow, setSelectedScholarship, setOverlayView, candidates } = useCommandStore();

  if (activeCandidatesFlow.length === 0) return null;

  return (
    <div className="w-full max-w-4xl mx-auto px-4 py-2 pointer-events-auto">
      <div className="rounded-2xl border border-glass-border bg-[#080C10]/90 backdrop-blur-2xl p-3 shadow-2xl">
        <div className="flex items-center justify-between border-b border-white/10 pb-2 mb-2 font-mono text-[9.5px]">
          <div className="flex items-center space-x-2">
            <span className="w-2 h-2 rounded-full bg-cyber-cyan animate-pulse" />
            <span className="font-bold text-intel-text uppercase tracking-wider">
              CANDIDATE INTELLIGENCE PIPELINE FLOW (§12)
            </span>
          </div>
          <span className="text-intel-muted">
            {activeCandidatesFlow.length} CANDIDATE(S) IN ACTIVE FLIGHT
          </span>
        </div>

        {/* Pipeline Stage Headers */}
        <div className="grid grid-cols-7 gap-1 text-center font-mono text-[8px] text-intel-muted pb-1 mb-2 border-b border-white/5">
          {STAGES.map((s) => (
            <div key={s.stage} className="uppercase font-bold tracking-tight">
              {s.label}
            </div>
          ))}
        </div>

        {/* Active Flowing Candidate Cards */}
        <div className="space-y-1.5 max-h-36 overflow-y-auto">
          <AnimatePresence>
            {activeCandidatesFlow.map((cand) => {
              const currentStageIdx = STAGES.findIndex((s) => s.stage === cand.currentStage);
              const isChallenged = cand.status === "CHALLENGED";
              const isPassed = cand.status === "PASSED" || cand.status === "RESOLVED";

              return (
                <motion.div
                  key={cand.id}
                  initial={{ opacity: 0, y: 6 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{ duration: 0.4 }}
                  onClick={() => {
                    sound.playClick();
                    const full = candidates.find((c) => c.scholarship_id === cand.scholarshipId);
                    if (full) {
                      setSelectedScholarship(full);
                      setOverlayView("AUDIT");
                    }
                  }}
                  className={`p-2 rounded-xl border flex items-center justify-between cursor-pointer select-none transition-all ${
                    isChallenged
                      ? "border-skeptic-rose/40 bg-skeptic-rose/10 hover:border-skeptic-rose"
                      : isPassed
                      ? "border-pakistan-green/40 bg-pakistan-green/10 hover:border-pakistan-green"
                      : "border-glass-border bg-glass-surface/60 hover:border-glass-border-focus"
                  }`}
                >
                  {/* Candidate Identity */}
                  <div className="flex items-center space-x-2 min-w-[160px] truncate">
                    <span className="font-mono text-[9px] font-bold text-cyber-cyan">
                      #{cand.scholarshipId.slice(-6).toUpperCase()}
                    </span>
                    <CountryFlagLogo name={cand.name} size="xs" className="shrink-0" />
                    <span className="text-[11px] font-bold text-intel-text truncate">
                      {cand.name}
                    </span>
                  </div>

                  {/* Stage Progress Bar / Beads */}
                  <div className="flex-1 mx-4 flex items-center justify-between relative">
                    <div className="absolute left-0 right-0 top-1/2 -translate-y-1/2 h-0.5 bg-white/10" />
                    {STAGES.map((s, idx) => {
                      const isReached = idx <= currentStageIdx;
                      const isCurrent = idx === currentStageIdx;
                      return (
                        <div
                          key={s.stage}
                          className={`relative z-10 w-2.5 h-2.5 rounded-full transition-all ${
                            isCurrent
                              ? isChallenged
                                ? "bg-skeptic-rose ring-4 ring-skeptic-rose/25 animate-pulse"
                                : "bg-cyber-cyan ring-4 ring-cyber-cyan/25 animate-pulse"
                              : isReached
                              ? "bg-pakistan-green"
                              : "bg-[#18222D]"
                          }`}
                        />
                      );
                    })}
                  </div>

                  {/* Status Indicator */}
                  <div className="flex items-center space-x-1.5 min-w-[110px] justify-end font-mono text-[9px]">
                    {isChallenged ? (
                      <span className="text-skeptic-rose font-bold flex items-center space-x-1">
                        <AlertTriangle className="w-3 h-3" />
                        <span>CHALLENGED</span>
                      </span>
                    ) : isPassed ? (
                      <span className="text-pakistan-green font-bold flex items-center space-x-1">
                        <CheckCircle2 className="w-3 h-3" />
                        <span>VERIFIED</span>
                      </span>
                    ) : (
                      <span className="text-cyber-cyan font-semibold flex items-center space-x-1">
                        <span>{cand.currentStage}</span>
                        <ArrowRight className="w-2.5 h-2.5" />
                      </span>
                    )}
                  </div>
                </motion.div>
              );
            })}
          </AnimatePresence>
        </div>
      </div>
    </div>
  );
};
