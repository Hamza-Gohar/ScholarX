"use client";

import React, { useEffect } from "react";
import { GlassSurface } from "@/components/ui/glass/GlassSurface";
import { Phase5Step, Phase5StepMeta } from "@/lib/fleet/types";
import { PHASE_5_STEPS } from "@/lib/fleet/fleetStore";
import { Region } from "@/lib/types";

export interface Phase5DirectorProps {
  currentStep: Phase5Step;
  onSelectStep: (step: Phase5Step) => void;
  isPlaying: boolean;
  onTogglePlay: () => void;
  onReset: () => void;
  focusedRegion: Region | "Pakistan" | null;
  onSelectFocus: (focus: Region | "Pakistan" | null) => void;
  className?: string;
}

export const Phase5Director: React.FC<Phase5DirectorProps> = ({
  currentStep,
  onSelectStep,
  isPlaying,
  onTogglePlay,
  onReset,
  focusedRegion,
  onSelectFocus,
  className = "",
}) => {
  const currentStepIndex = PHASE_5_STEPS.findIndex((s) => s.step === currentStep);
  const currentStepMeta: Phase5StepMeta =
    PHASE_5_STEPS[currentStepIndex] || PHASE_5_STEPS[0];

  const handlePrev = () => {
    if (currentStepIndex > 0) {
      onSelectStep(PHASE_5_STEPS[currentStepIndex - 1].step);
    }
  };

  const handleNext = () => {
    if (currentStepIndex < PHASE_5_STEPS.length - 1) {
      onSelectStep(PHASE_5_STEPS[currentStepIndex + 1].step);
    }
  };

  // Auto-play timer effect
  useEffect(() => {
    if (!isPlaying) return;

    const timer = setTimeout(() => {
      if (currentStepIndex < PHASE_5_STEPS.length - 1) {
        onSelectStep(PHASE_5_STEPS[currentStepIndex + 1].step);
      } else {
        onTogglePlay();
      }
    }, currentStepMeta.durationMs);

    return () => clearTimeout(timer);
  }, [isPlaying, currentStepIndex, currentStepMeta, onSelectStep, onTogglePlay]);

  const regions: (Region | "Pakistan")[] = [
    "Europe",
    "Asia",
    "Americas",
    "MENA",
    "Oceania",
  ];

  return (
    <div className={`w-full max-w-6xl mx-auto pointer-events-auto select-none space-y-1.5 ${className}`}>
      {/* Top Bar: Playback Scrubber & Steps */}
      <GlassSurface
        elevation="elevated"
        className="px-5 py-2.5 rounded-2xl border-white/[0.14] shadow-2xl flex flex-col xl:flex-row items-center justify-between gap-3"
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
            {isPlaying ? "⏸ PAUSE" : "▶ PLAY FLEET"}
          </button>

          <button
            onClick={handlePrev}
            disabled={currentStepIndex === 0}
            className="p-1.5 rounded-lg border border-white/[0.08] bg-black/40 text-sx-text-secondary hover:text-white disabled:opacity-30 disabled:pointer-events-none transition-all"
            title="Previous Scene"
          >
            ◀
          </button>

          <button
            onClick={handleNext}
            disabled={currentStepIndex === PHASE_5_STEPS.length - 1}
            className="p-1.5 rounded-lg border border-white/[0.08] bg-black/40 text-sx-text-secondary hover:text-white disabled:opacity-30 disabled:pointer-events-none transition-all"
            title="Next Scene"
          >
            ▶
          </button>

          <button
            onClick={onReset}
            className="px-2 py-1 rounded-lg border border-white/[0.08] bg-black/30 hover:bg-white/[0.08] text-[10px] font-mono text-sx-text-tertiary hover:text-sx-text-primary transition-all"
            title="Reset to Scene 1"
          >
            ↺ RESET
          </button>
        </div>

        {/* 12 Interactive Scene Buttons */}
        <div className="flex items-center space-x-1 overflow-x-auto py-0.5">
          {PHASE_5_STEPS.map((s, idx) => {
            const isCurrent = s.step === currentStep;
            const isCompleted = idx < currentStepIndex;

            return (
              <button
                key={s.step}
                onClick={() => onSelectStep(s.step)}
                className={`w-7 h-7 rounded-lg text-[10px] font-mono font-bold transition-all duration-200 flex items-center justify-center border shrink-0 ${
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

        {/* Scene Narrative Badge */}
        <div className="flex items-center space-x-2 text-right shrink-0 truncate max-w-[340px]">
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

      {/* Bottom Sub-Bar: Fleet Attention & Focus Management (§18, §19) */}
      <div className="flex items-center justify-between px-3 text-[10px] font-mono text-sx-text-tertiary">
        <div className="flex items-center space-x-1.5">
          <span className="text-white/60 font-semibold uppercase tracking-wider text-[9px]">
            CAMERA & FLEET FOCUS:
          </span>
          <button
            onClick={() => onSelectFocus(null)}
            className={`px-2 py-0.5 rounded-full border transition-all ${
              focusedRegion === null
                ? "bg-sx-ice/20 text-sx-ice border-sx-ice/50 font-bold shadow-[0_0_8px_rgba(56,189,248,0.3)]"
                : "bg-black/40 text-sx-text-tertiary border-white/[0.08] hover:text-white"
            }`}
          >
            GLOBAL STAGE
          </button>
          <button
            onClick={() => onSelectFocus("Pakistan")}
            className={`px-2 py-0.5 rounded-full border transition-all ${
              focusedRegion === "Pakistan"
                ? "bg-sx-gold/20 text-sx-gold border-sx-gold/50 font-bold shadow-[0_0_8px_rgba(212,175,55,0.3)]"
                : "bg-black/40 text-sx-text-tertiary border-white/[0.08] hover:text-white"
            }`}
          >
            COMMANDER (PK)
          </button>

          {regions.map((reg) => (
            <button
              key={reg}
              onClick={() => onSelectFocus(reg)}
              className={`px-2 py-0.5 rounded-full border transition-all ${
                focusedRegion === reg
                  ? "bg-sx-ice/20 text-sx-ice border-sx-ice/50 font-bold shadow-[0_0_8px_rgba(56,189,248,0.3)]"
                  : "bg-black/40 text-sx-text-tertiary border-white/[0.08] hover:text-white"
              }`}
            >
              {reg.toUpperCase()}
            </button>
          ))}
        </div>

        <div className="hidden md:flex items-center space-x-2 text-[9px] text-sx-text-tertiary">
          <span>FLEET: 5 AUTONOMOUS WORKFLOWS</span>
          <span>&bull;</span>
          <span className="text-sx-emerald">TAVILY &bull; FIRECRAWL &bull; JINA &bull; CRAWL4AI &bull; GEMINI</span>
        </div>
      </div>
    </div>
  );
};
