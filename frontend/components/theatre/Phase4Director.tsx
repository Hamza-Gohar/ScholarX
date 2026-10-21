"use client";

import React, { useEffect } from "react";
import { motion } from "framer-motion";
import { GlassSurface } from "@/components/ui/glass/GlassSurface";
import { Phase4Step, Phase4StepMeta } from "@/lib/communication/types";
import { PHASE_4_STEPS } from "@/lib/communication/packetStore";

export interface Phase4DirectorProps {
  currentStep: Phase4Step;
  onSelectStep: (step: Phase4Step) => void;
  isPlaying: boolean;
  onTogglePlay: () => void;
  onReset: () => void;
  className?: string;
}

export const Phase4Director: React.FC<Phase4DirectorProps> = ({
  currentStep,
  onSelectStep,
  isPlaying,
  onTogglePlay,
  onReset,
  className = "",
}) => {
  const currentStepIndex = PHASE_4_STEPS.findIndex((s) => s.step === currentStep);
  const currentStepMeta: Phase4StepMeta =
    PHASE_4_STEPS[currentStepIndex] || PHASE_4_STEPS[0];

  const handlePrev = () => {
    if (currentStepIndex > 0) {
      onSelectStep(PHASE_4_STEPS[currentStepIndex - 1].step);
    }
  };

  const handleNext = () => {
    if (currentStepIndex < PHASE_4_STEPS.length - 1) {
      onSelectStep(PHASE_4_STEPS[currentStepIndex + 1].step);
    }
  };

  // Auto-play timer effect
  useEffect(() => {
    if (!isPlaying) return;

    const timer = setTimeout(() => {
      if (currentStepIndex < PHASE_4_STEPS.length - 1) {
        onSelectStep(PHASE_4_STEPS[currentStepIndex + 1].step);
      } else {
        // Loop back or pause at end
        onTogglePlay();
      }
    }, currentStepMeta.durationMs);

    return () => clearTimeout(timer);
  }, [isPlaying, currentStepIndex, currentStepMeta, onSelectStep, onTogglePlay]);

  return (
    <div className={`w-full max-w-4xl mx-auto pointer-events-auto select-none ${className}`}>
      <GlassSurface
        elevation="elevated"
        className="px-5 py-2.5 rounded-2xl border-white/[0.14] shadow-2xl flex flex-col md:flex-row items-center justify-between gap-3"
      >
        {/* Playback Controls & Scrubber */}
        <div className="flex items-center space-x-2 shrink-0">
          <button
            onClick={onTogglePlay}
            className={`px-3 py-1 rounded-lg text-xs font-mono font-bold tracking-wider uppercase transition-all duration-200 border ${
              isPlaying
                ? "bg-sx-emerald/20 text-sx-emerald border-sx-emerald/50 shadow-[0_0_12px_rgba(16,185,129,0.3)]"
                : "bg-white/[0.08] hover:bg-white/[0.15] text-sx-text-primary border-white/[0.12]"
            }`}
          >
            {isPlaying ? "⏸ PAUSE" : "▶ PLAY PROOF"}
          </button>

          <button
            onClick={handlePrev}
            disabled={currentStepIndex === 0}
            className="p-1.5 rounded-lg border border-white/[0.08] bg-black/40 text-sx-text-secondary hover:text-white disabled:opacity-30 disabled:pointer-events-none transition-all"
            title="Previous Step"
          >
            ◀
          </button>

          <button
            onClick={handleNext}
            disabled={currentStepIndex === PHASE_4_STEPS.length - 1}
            className="p-1.5 rounded-lg border border-white/[0.08] bg-black/40 text-sx-text-secondary hover:text-white disabled:opacity-30 disabled:pointer-events-none transition-all"
            title="Next Step"
          >
            ▶
          </button>

          <button
            onClick={onReset}
            className="px-2 py-1 rounded-lg border border-white/[0.08] bg-black/30 hover:bg-white/[0.08] text-[10px] font-mono text-sx-text-tertiary hover:text-sx-text-primary transition-all"
            title="Reset to Step 1"
          >
            ↺ RESET
          </button>
        </div>

        {/* 10 Step Interactive Buttons */}
        <div className="flex items-center space-x-1 overflow-x-auto py-0.5">
          {PHASE_4_STEPS.map((s, idx) => {
            const isCurrent = s.step === currentStep;
            const isCompleted = idx < currentStepIndex;

            return (
              <button
                key={s.step}
                onClick={() => onSelectStep(s.step)}
                className={`w-7 h-7 rounded-lg text-[10px] font-mono font-bold transition-all duration-200 flex items-center justify-center border ${
                  isCurrent
                    ? "bg-sx-ice/25 text-sx-ice border-sx-ice shadow-[0_0_14px_rgba(56,189,248,0.4)] scale-105"
                    : isCompleted
                    ? "bg-white/[0.06] text-sx-emerald border-emerald-500/30 hover:border-emerald-500/60"
                    : "bg-black/30 text-sx-text-tertiary border-white/[0.06] hover:text-white hover:border-white/[0.2]"
                }`}
                title={`${s.label}: ${s.narrative}`}
              >
                {String(idx + 1).padStart(2, "0")}
              </button>
            );
          })}
        </div>

        {/* Step Narrative Badge */}
        <div className="flex items-center space-x-2 text-right shrink-0 truncate max-w-[320px]">
          <span className="w-2 h-2 rounded-full bg-sx-ice animate-pulse shrink-0" />
          <div className="truncate text-left">
            <div className="text-[10px] font-mono tracking-wider text-sx-ice uppercase font-semibold truncate">
              {currentStepMeta.label}
            </div>
            <div className="text-[10px] font-sans text-sx-text-secondary truncate">
              {currentStepMeta.narrative}
            </div>
          </div>
        </div>
      </GlassSurface>
    </div>
  );
};
