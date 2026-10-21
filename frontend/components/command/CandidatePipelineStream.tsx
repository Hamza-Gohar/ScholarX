"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { Scholarship } from "@/lib/types";
import { Database, ShieldCheck, ChevronRight, Sparkles, AlertTriangle, ArrowRight } from "lucide-react";
import { sound } from "@/lib/sound-fx";

export const CandidatePipelineStream: React.FC = () => {
  const {
    candidates,
    setSelectedScholarship,
    setOverlayView,
    scoreMutations,
  } = useCommandStore();

  if (candidates.length === 0) return null;

  return (
    <div className="w-full bg-obsidian-950/95 border-t border-white/10 px-3 py-2 flex items-center space-x-3 select-none backdrop-blur-md">
      {/* Stream Label */}
      <div className="flex items-center space-x-2 flex-shrink-0 font-mono text-[10px]">
        <div className="w-2 h-2 rounded-full bg-cyber-cyan animate-pulse" />
        <span className="font-extrabold tracking-widest text-white/50">
          INTELLIGENCE PIPELINE
        </span>
        <span className="px-1.5 py-0.2 rounded bg-white/5 text-cyber-cyan border border-cyber-cyan/30 font-bold">
          {candidates.length} CANDIDATES
        </span>
      </div>

      <span className="text-white/20">|</span>

      {/* Horizontally scrolling scholarship intelligence dossiers */}
      <div className="flex-1 flex items-center space-x-2.5 overflow-x-auto py-0.5 pr-2">
        {candidates.map((c) => {
          // Check if this candidate had a score mutation
          const mutation = scoreMutations.find((m) => m.scholarshipId === c.scholarship_id);

          return (
            <div
              key={c.scholarship_id}
              onClick={() => {
                sound.playClick();
                setSelectedScholarship(c);
                setOverlayView("AUDIT");
              }}
              className="flex-shrink-0 command-panel rounded px-2.5 py-1.5 border border-white/10 hover:border-cyber-cyan/50 hover:bg-obsidian-850 cursor-pointer transition-all flex items-center space-x-3 group"
            >
              {/* Score Badge with Mutation animation */}
              <div className="flex flex-col items-center justify-center font-mono">
                <span className="text-[8px] text-white/40">MATCH</span>
                <span
                  className={`text-xs font-black px-1.5 py-0.2 rounded ${
                    mutation
                      ? "text-warning-amber bg-warning-amber/10 border border-warning-amber/40 animate-pulse"
                      : "text-pakistan-emerald bg-pakistan-emerald/10 border border-pakistan-emerald/30"
                  }`}
                >
                  {mutation ? mutation.newScore : c.confidence_score || 94}%
                </span>
              </div>

              {/* Identity & Details */}
              <div className="flex flex-col min-w-0 max-w-[190px]">
                <div className="flex items-center space-x-1.5">
                  <span className="font-mono text-xs font-bold text-white truncate group-hover:text-cyber-cyan transition-colors">
                    {c.name}
                  </span>
                </div>
                <div className="flex items-center space-x-1.5 font-mono text-[9px] text-white/50 truncate">
                  <span>{c.host_country_name}</span>
                  <span>•</span>
                  <span className="text-pakistan-emerald font-semibold">
                    {c.funding.funding_type === "FULL" ? "Fully Funded" : c.funding.funding_type}
                  </span>
                  {c.pakistan_requirements.pakistan_bilateral_quota && (
                    <span className="text-cyber-cyan font-bold">• HEC QUOTA</span>
                  )}
                </div>
              </div>

              {/* Status indicator / Inspect */}
              <div className="flex items-center space-x-1 font-mono text-[9px] text-white/40 group-hover:text-cyber-cyan transition-colors pl-1 border-l border-white/5">
                <span className="hidden sm:inline">DOSSIER</span>
                <ChevronRight className="w-3 h-3 group-hover:translate-x-0.5 transition-transform" />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
