"use client";

import React, { useEffect } from "react";
import { Play, Pause, RotateCcw, ChevronRight } from "lucide-react";
import { Phase6Step, SpecialistType } from "@/lib/investigation/types";
import { PHASE_6_STEPS } from "@/lib/investigation/investigationStore";

export interface Phase6DirectorProps {
  currentStep: Phase6Step;
  onSelectStep: (step: Phase6Step) => void;
  isPlaying: boolean;
  onTogglePlay: () => void;
  onReset: () => void;
  focusedSpecialist: SpecialistType | null;
  onSelectFocus: (specialist: SpecialistType | null) => void;
  className?: string;
}

export const Phase6Director: React.FC<Phase6DirectorProps> = ({
  currentStep,
  onSelectStep,
  isPlaying,
  onTogglePlay,
  onReset,
  focusedSpecialist,
  onSelectFocus,
  className = "",
}) => {
  const currentMeta = PHASE_6_STEPS.find((s) => s.step === currentStep) || PHASE_6_STEPS[0];
  const currentIndex = PHASE_6_STEPS.findIndex((s) => s.step === currentStep);

  // Auto-play timeline progression
  useEffect(() => {
    if (!isPlaying) return;

    const timer = setTimeout(() => {
      const nextIndex = (currentIndex + 1) % PHASE_6_STEPS.length;
      onSelectStep(PHASE_6_STEPS[nextIndex].step);
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
            title={isPlaying ? "Pause timeline" : "Play continuous investigation sequence"}
          >
            {isPlaying ? <Pause className="w-3 h-3 fill-current" /> : <Play className="w-3 h-3 fill-current" />}
            <span>{isPlaying ? "PAUSE AUTO-PLAY" : "RUN INVESTIGATION"}</span>
          </button>

          <button
            onClick={onReset}
            className="p-1 rounded border border-white/[0.08] bg-white/[0.04] text-sx-text-tertiary hover:text-white transition-all"
            title="Reset to Scene 01 (Opportunity Selection)"
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

        {/* Quick Specialist Jump */}
        <div className="flex items-center space-x-1 text-[9px] font-mono">
          <span className="text-white/40 uppercase mr-1">JUMP:</span>
          {(["ELIGIBILITY", "DOCUMENT", "COST", "DEADLINE", "VERIFICATION", "SKEPTIC", "SYNTHESIS"] as SpecialistType[]).map(
            (spec) => {
              const isCurrent = currentMeta.activeSpecialist === spec;
              return (
                <button
                  key={spec}
                  onClick={() => {
                    const stepForSpec = PHASE_6_STEPS.find((s) => s.activeSpecialist === spec);
                    if (stepForSpec) onSelectStep(stepForSpec.step);
                  }}
                  className={`px-1.5 py-0.5 rounded transition-all ${
                    isCurrent
                      ? "bg-white/20 text-white font-bold border border-white/30"
                      : "text-white/50 hover:text-white"
                  }`}
                >
                  {spec.slice(0, 4)}
                </button>
              );
            }
          )}
        </div>
      </div>

      {/* 14-Step Scrubber Strip */}
      <div
        className="grid gap-1 pt-1 border-t border-white/[0.06]"
        style={{ gridTemplateColumns: "repeat(14, minmax(0, 1fr))" }}
      >
        {PHASE_6_STEPS.map((s, idx) => {
          const isActive = s.step === currentStep;
          const isPassed = idx < currentIndex;

          return (
            <button
              key={s.step}
              onClick={() => onSelectStep(s.step)}
              className={`py-1 px-0.5 rounded text-[8px] font-mono transition-all text-center flex flex-col items-center justify-center truncate ${
                isActive
                  ? "bg-sx-ice/25 border border-sx-ice text-white font-bold shadow-[0_0_10px_rgba(56,189,248,0.4)]"
                  : isPassed
                  ? "bg-white/[0.06] border border-white/[0.12] text-white/80 hover:bg-white/[0.1]"
                  : "bg-white/[0.02] border border-white/[0.04] text-white/40 hover:text-white/70"
              }`}
            >
              <span className="text-[7px] text-white/40 leading-none mb-0.5">
                {String(idx + 1).padStart(2, "0")}
              </span>
              <span className="truncate w-full font-bold">
                {s.step.replace("_ACTIVE", "").replace("_DOCKED", "").replace("_COMPLETE", "").slice(0, 7)}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
