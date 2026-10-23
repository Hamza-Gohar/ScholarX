"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  AlertTriangle,
  GraduationCap,
  Sparkles,
  ArrowRight,
  RotateCcw,
  X,
  Compass,
  CheckCircle2,
  HeartHandshake,
  Building2,
  Globe2,
} from "lucide-react";
import { sound } from "@/lib/sound-fx";

export interface IneligiblePoliteModalProps {
  isOpen: boolean;
  percentage: number;
  gpa4Scale?: number;
  onClose: () => void;
  onProceedAnyway: () => void;
  onAdjustMarks: () => void;
}

export const IneligiblePoliteModal: React.FC<IneligiblePoliteModalProps> = ({
  isOpen,
  percentage,
  gpa4Scale,
  onClose,
  onProceedAnyway,
  onAdjustMarks,
}) => {
  if (!isOpen) return null;

  const displayGpa = gpa4Scale ? gpa4Scale.toFixed(2) : ((percentage / 100) * 4.0).toFixed(2);
  const marks1100 = Math.round((percentage / 100) * 1100);

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/85 backdrop-blur-md animate-in fade-in duration-200">
        <motion.div
          initial={{ opacity: 0, scale: 0.94, y: 16 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 10 }}
          transition={{ duration: 0.25, ease: "easeOut" }}
          className="relative w-full max-w-2xl bg-[#090D14] border border-amber-500/40 rounded-2xl shadow-[0_0_60px_rgba(245,158,11,0.22)] overflow-hidden flex flex-col"
        >
          {/* Top Amber Status Bar */}
          <div className="px-5 py-3.5 bg-amber-500/10 border-b border-amber-500/20 flex items-center justify-between">
            <div className="flex items-center space-x-2.5">
              <div className="p-1.5 rounded-lg bg-amber-500/20 border border-amber-500/40 text-amber-400">
                <AlertTriangle className="w-4 h-4" />
              </div>
              <div>
                <div className="font-mono text-xs font-bold tracking-wider text-amber-300 uppercase">
                  ACADEMIC STANDING ADVISORY // MERIT ELIGIBILITY
                </div>
                <div className="font-mono text-[10px] text-zinc-400">
                  STANDARD BILATERAL & INTERNATIONAL MERIT CUTOFF: 70.0% MARKS
                </div>
              </div>
            </div>

            <button
              onClick={() => {
                sound.playClick();
                onClose();
              }}
              className="p-1 rounded-lg hover:bg-white/10 text-zinc-400 hover:text-white transition-colors"
              aria-label="Close"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Modal Content */}
          <div className="p-6 space-y-5 overflow-y-auto max-h-[75vh]">
            {/* Candidate Score Highlight */}
            <div className="p-4 rounded-xl bg-black/60 border border-white/10 flex items-center justify-between">
              <div>
                <span className="text-[10px] font-mono uppercase text-zinc-400 block mb-0.5">
                  YOUR CURRENT RECORDED MARKS
                </span>
                <div className="flex items-baseline space-x-2">
                  <span className="text-2xl font-bold font-mono text-amber-400">
                    {percentage.toFixed(1)}%
                  </span>
                  <span className="text-xs font-mono text-zinc-400">
                    ({marks1100}/1,100 Marks • CGPA {displayGpa}/4.0)
                  </span>
                </div>
              </div>

              <div className="px-3 py-1.5 rounded-lg bg-red-500/15 border border-red-500/30 text-right">
                <span className="text-[9px] font-mono text-red-400 font-bold tracking-wider block">
                  MERIT STATUS
                </span>
                <span className="text-xs font-bold text-red-300 font-mono">
                  INELIGIBLE (&lt; 70%)
                </span>
              </div>
            </div>

            {/* Polite & Empathetic Message */}
            <div className="space-y-2 text-xs font-sans text-zinc-200 leading-relaxed">
              <p className="text-sm font-semibold text-white">
                Assalam-o-Alaikum & Greetings,
              </p>
              <p>
                Based on your entered academic standing of <strong className="text-amber-300">{percentage.toFixed(1)}% marks</strong>, 
                our evaluation engine indicates that you are currently below the standard 
                <strong className="text-white"> 70% minimum threshold</strong> required for highly competitive, 
                merit-based international programs (such as DAAD Germany, Fulbright USA, Commonwealth, and Turkish Burslari merit seats).
              </p>
              <p className="text-zinc-300">
                Please do not be disheartened — academic percentage is only one dimension of global education. 
                ScholarX has automatically unlocked alternative, high-probability pathways designed to support students with your profile.
              </p>
            </div>

            {/* Recommended Alternative Pathways */}
            <div className="p-4 rounded-xl bg-emerald-500/[0.07] border border-emerald-500/30 space-y-2.5">
              <div className="flex items-center space-x-2 text-emerald-400 font-mono text-xs font-bold tracking-wide">
                <Sparkles className="w-4 h-4 text-emerald-400" />
                <span>UNLOCKED ALTERNATIVE PATHWAYS & NEED-BASED GRANTS</span>
              </div>

              <div className="space-y-2 font-mono text-[11px] text-zinc-300">
                <div className="flex items-start space-x-2.5 p-2 rounded bg-black/40 border border-white/5">
                  <span className="text-emerald-400 text-sm leading-none shrink-0 mt-0.5">🇮🇹</span>
                  <div>
                    <strong className="text-white block">Italian DSU Regional Need-Based Grants</strong>
                    <span className="text-zinc-400 text-[10px]">
                      100% Tuition Waiver + up to €7,000/year living stipend. Awarded based purely on family household income (ISEE Parificato), NOT your previous GPA.
                    </span>
                  </div>
                </div>

                <div className="flex items-start space-x-2.5 p-2 rounded bg-black/40 border border-white/5">
                  <span className="text-emerald-400 text-sm leading-none shrink-0 mt-0.5">🇨🇳</span>
                  <div>
                    <strong className="text-white block">China CSC & Provincial Type-B Grants</strong>
                    <span className="text-zinc-400 text-[10px]">
                      Full tuition and subsidized university housing available for Pakistani candidates meeting basic passing criteria (55%+).
                    </span>
                  </div>
                </div>

                <div className="flex items-start space-x-2.5 p-2 rounded bg-black/40 border border-white/5">
                  <span className="text-emerald-400 text-sm leading-none shrink-0 mt-0.5">🇭🇺</span>
                  <div>
                    <strong className="text-white block">Hungarian State-Subsidized Partial Fee Reductions</strong>
                    <span className="text-zinc-400 text-[10px]">
                      Accessible admission pathways with opportunity to transition to Erasmus+ mobility grants after Semester 1.
                    </span>
                  </div>
                </div>

                <div className="flex items-start space-x-2.5 p-2 rounded bg-black/40 border border-white/5">
                  <span className="text-emerald-400 text-sm leading-none shrink-0 mt-0.5">🇩🇪</span>
                  <div>
                    <strong className="text-white block">German Studienkolleg / Foundation Year</strong>
                    <span className="text-zinc-400 text-[10px]">
                      1-year preparatory bridge program that resets your qualifying German grade (Feststellungsprüfung) prior to university matriculation.
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Modal Action Buttons */}
          <div className="p-4 bg-black/80 border-t border-white/10 flex flex-col sm:flex-row items-center justify-end gap-2.5">
            <button
              onClick={() => {
                sound.playClick();
                onAdjustMarks();
              }}
              className="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-white/20 bg-white/5 hover:bg-white/10 text-white font-mono text-xs font-semibold flex items-center justify-center space-x-2 transition-all"
            >
              <RotateCcw className="w-3.5 h-3.5 text-zinc-400" />
              <span>Adjust / Re-enter Marks</span>
            </button>

            <button
              onClick={() => {
                sound.playClick();
                onProceedAnyway();
              }}
              className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-black font-mono text-xs font-bold flex items-center justify-center space-x-2 shadow-[0_0_20px_rgba(16,185,129,0.35)] transition-all"
            >
              <span>Explore Need-Based Opportunities</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
};
