"use client";

import React, { useEffect } from "react";
import { Play, Pause, RotateCcw, ChevronRight } from "lucide-react";
import { Phase7Step } from "@/lib/ranking/types";
import { PHASE_7_STEPS } from "@/lib/ranking/rankingStore";

export interface Phase7DirectorProps {
  currentStep: Phase7Step;
  onSelectStep: (step: Phase7Step) => void;
  isPlaying: boolean;
  onTogglePlay: () => void;
  onReset: () => void;
  className?: string;
}

export const Phase7Director: React.FC<Phase7DirectorProps> = ({
  currentStep,
  onSelectStep,
  isPlaying,
  onTogglePlay,
  onReset,
  className = "",
}) => {
  const currentMeta = PHASE_7_STEPS.find((s) => s.step === currentStep) || PHASE_7_STEPS[0];
  const currentIndex = PHASE_7_STEPS.findIndex((s) => s.step === currentStep);

  // Auto-play timeline progression
  useEffect(() => {
    if (!isPlaying) return;

    const timer = setTimeout(() => {
      const nextIndex = (currentIndex + 1) % PHASE_7_STEPS.length;
      onSelectStep(PHASE_7_STEPS[nextIndex].step);
    }, currentMeta.durationMs);

    return () => clearTimeout(timer);
  }, [isPlaying, currentIndex, currentMeta, onSelectStep]);

  return (
    <div
      className={`w-full max-w-[1380px] mx-auto rounded-xl border border-white/[0.1] bg-black/75 backdrop-blur-xl p-2.5 shadow-2xl transition-all duration-300 pointer-events-auto ${className}`}
    >
      {/* Top Controller Bar */}
      <div className="flex items-center justify-between gap-3 mb-2">
        {/* Play/Pause & Reset Controls */}
        <div className="flex items-center space-x-2">
          <button
            onClick={onTogglePlay}
            className={`px-3 py-1 rounded border font-mono text-[10px] font-bold tracking-wider flex items-center space-x-1.5 transition-all shadow-md ${
              isPlaying
                ? "bg-sx-amber/20 border-sx-amber text-sx-amber shadow-[0_0_12px_rgba(245,158,11,0.3)]"
                : "bg-sx-ice/20 border-sx-ice text-sx-ice shadow-[0_0_12px_rgba(56,189,248,0.25)] hover:bg-sx-ice/30"
            }`}
            title={isPlaying ? "Pause timeline" : "Play continuous Phase 7 sequence"}
          >
            {isPlaying ? <Pause className="w-3 h-3 fill-current" /> : <Play className="w-3 h-3 fill-current" />}
            <span>{isPlaying ? "PAUSE AUTO-PLAY" : "RUN PHASE 7 SEQUENCE"}</span>
          </button>

          <button
            onClick={onReset}
            className="p-1 rounded border border-white/[0.08] bg-white/[0.04] text-sx-text-tertiary hover:text-white transition-all"
            title="Reset to Scene 01 (Candidate Pool Initialized)"
          >
            <RotateCcw className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Live Step Label & Narrative */}
        <div className="flex-1 flex items-center space-x-3 px-3 py-1 rounded bg-white/[0.03] border border-white/[0.06] overflow-hidden">
          <div className="flex items-center space-x-1.5 shrink-0 text-sx-gold text-[10px] font-mono font-bold">
            <span className="w-1.5 h-1.5 rounded-full bg-sx-gold animate-pulse" />
            <span>{currentMeta.label}</span>
            <ChevronRight className="w-3 h-3 text-white/40" />
          </div>
          <div className="text-[11px] font-sans text-sx-text-secondary truncate font-normal">
            {currentMeta.narrative}
          </div>
        </div>

        {/* Milestone Quick Jumps */}
        <div className="flex items-center space-x-1 text-[9px] font-mono">
          <span className="text-white/40 uppercase mr-1">JUMP:</span>
          {[
            { label: "POOL", step: "POOL_INSPECTION" as Phase7Step },
            { label: "RANKING", step: "FACTOR_EVALUATION" as Phase7Step },
            { label: "PRIMARY", step: "PRIMARY_SELECTION" as Phase7Step },
            { label: "ROADMAP", step: "ROADMAP_GENERATION" as Phase7Step },
            { label: "DOSSIER", step: "DOSSIER_ASSEMBLY" as Phase7Step },
            { label: "COMPLETE", step: "ARTIFACTS_DELIVERED" as Phase7Step },
          ].map((item) => {
            const isCurrent = currentStep === item.step;
            return (
              <button
                key={item.label}
                onClick={() => onSelectStep(item.step)}
                className={`px-1.5 py-0.5 rounded transition-all ${
                  isCurrent
                    ? "bg-sx-gold/30 text-sx-gold font-bold border border-sx-gold/50"
                    : "text-white/50 hover:text-white hover:bg-white/[0.06]"
                }`}
              >
                {item.label}
              </button>
            );
          })}
        </div>
      </div>

      {/* 12-Segment Scrubber Track */}
      <div className="grid grid-cols-12 gap-1.5 pt-1 border-t border-white/[0.06]">
        {PHASE_7_STEPS.map((meta, idx) => {
          const isSelected = meta.step === currentStep;
          const isPast = idx < currentIndex;

          return (
            <button
              key={meta.step}
              onClick={() => onSelectStep(meta.step)}
              className="group flex flex-col items-center focus:outline-none"
              title={`${meta.label}: ${meta.narrative}`}
            >
              <div
                className={`w-full h-1.5 rounded-full transition-all duration-300 ${
                  isSelected
                    ? "bg-sx-gold shadow-[0_0_8px_rgba(212,175,55,0.6)]"
                    : isPast
                    ? "bg-sx-ice/60 hover:bg-sx-ice"
                    : "bg-white/[0.1] hover:bg-white/[0.2]"
                }`}
              />
              <span
                className={`text-[8px] font-mono mt-1 transition-all ${
                  isSelected
                    ? "text-sx-gold font-bold"
                    : isPast
                    ? "text-white/60"
                    : "text-white/30"
                }`}
              >
                {meta.label.split("//")[0].trim()}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
