"use client";

import React from "react";
import { motion } from "framer-motion";
import { InvestigationTarget, TargetKnowledgeState, ResolvedTrace } from "@/lib/investigation/types";
import { Award, ShieldCheck, CheckCircle2, Clock, DollarSign, AlertTriangle, FileText, Check } from "lucide-react";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";

export interface InvestigationTargetObjectProps {
  target: InvestigationTarget;
  activeSpecialist: string | null;
  onSelectTrace?: (trace: ResolvedTrace) => void;
  className?: string;
}

export const InvestigationTargetObject: React.FC<InvestigationTargetObjectProps> = ({
  target,
  activeSpecialist,
  onSelectTrace,
  className = "",
}) => {
  // Knowledge state styling & badge
  const getKnowledgeBadge = (state: TargetKnowledgeState) => {
    switch (state) {
      case "UNINVESTIGATED":
        return {
          label: "AWAITING SPECIALIST DISPATCH",
          color: "#94A3B8",
          bg: "rgba(148, 163, 184, 0.1)",
          border: "rgba(148, 163, 184, 0.25)",
        };
      case "PROFILE_MATCHED":
        return {
          label: "PROFILE ELIGIBILITY MATCHED (13/15)",
          color: "#10B981",
          bg: "rgba(16, 185, 129, 0.15)",
          border: "rgba(16, 185, 129, 0.4)",
        };
      case "READINESS_KNOWN":
        return {
          label: "DOCUMENT READINESS ASSESSED (62%)",
          color: "#F59E0B",
          bg: "rgba(245, 158, 11, 0.15)",
          border: "rgba(245, 158, 11, 0.4)",
        };
      case "COST_UNDERSTOOD":
        return {
          label: "REAL PKR OUT-OF-POCKET CALCULATED",
          color: "#EF4444",
          bg: "rgba(239, 68, 68, 0.15)",
          border: "rgba(239, 68, 68, 0.4)",
        };
      case "TIMELINE_ASSESSED":
        return {
          label: "DEADLINE RUNWAY VERIFIED (37D SLACK)",
          color: "#38BDF8",
          bg: "rgba(56, 189, 248, 0.15)",
          border: "rgba(56, 189, 248, 0.4)",
        };
      case "EVIDENCE_CONFIRMED":
        return {
          label: "OFFICIAL EVIDENCE CONFIRMED // HEC LISTED",
          color: "#10B981",
          bg: "rgba(16, 185, 129, 0.2)",
          border: "rgba(16, 185, 129, 0.5)",
        };
      case "RISKS_CHALLENGED":
        return {
          label: "ADVERSARIAL RISKS AUDITED // 2 QUALIFIED",
          color: "#D4AF37",
          bg: "rgba(212, 175, 55, 0.2)",
          border: "rgba(212, 175, 55, 0.5)",
        };
      case "INVESTIGATION_COMPLETE":
        return {
          label: "INVESTIGATION COMPLETE // SYNTHESIZED INTELLIGENCE",
          color: "#C084FC",
          bg: "rgba(192, 132, 252, 0.2)",
          border: "rgba(192, 132, 252, 0.5)",
        };
    }
  };

  const badge = getKnowledgeBadge(target.knowledgeState);

  return (
    <motion.div
      initial={false}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.2 }}
      className={`relative rounded-2xl border border-white/[0.12] bg-black/85 backdrop-blur-2xl p-3.5 sm:p-5 shadow-[0_0_50px_rgba(0,0,0,0.8)] pointer-events-auto transition-all duration-300 w-full max-w-[720px] ${className}`}
      style={{
        boxShadow:
          target.knowledgeState === "INVESTIGATION_COMPLETE"
            ? "0 0 60px rgba(168, 85, 247, 0.25), inset 0 0 20px rgba(168, 85, 247, 0.1)"
            : "0 0 45px rgba(0, 0, 0, 0.75)",
      }}
    >
      {/* Top subtle highlight gradient */}
      <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-white/30 to-transparent" />

      {/* Header Bar */}
      <div className="flex items-center justify-between gap-3 mb-2.5">
        <div className="flex items-center space-x-2">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-sx-ice opacity-75" />
            <span className="relative inline-flex rounded-full h-2 w-2 bg-sx-ice" />
          </span>
          <span className="text-[10px] font-mono tracking-[0.2em] uppercase font-bold text-sx-text-tertiary">
            INVESTIGATION TARGET // OBJECT UNDER INQUIRY
          </span>
        </div>

        {/* Dedicated Quota Badge */}
        <div className="flex items-center space-x-1.5 px-2.5 py-0.5 rounded-full border border-sx-emerald/40 bg-sx-emerald/10 text-[10px] font-mono font-bold text-sx-emerald shadow-[0_0_12px_rgba(16,185,129,0.25)]">
          <Award className="w-3 h-3 text-sx-emerald" />
          <span>{target.quotaSeats} BILATERAL SEATS (PAKISTAN HEC)</span>
        </div>
      </div>

      {/* Main Title & Institution */}
      <div className="space-y-0.5 mb-2.5">
        <h2 className="text-xl font-sans font-bold text-white tracking-tight flex items-center gap-2">
          <CountryFlagLogo country={target.hostCountry} name={target.name} size="md" className="shrink-0" />
          <span>{target.name}</span>
          <span className="text-xs font-mono font-normal px-2 py-0.5 rounded bg-white/[0.06] border border-white/[0.08] text-sx-gold">
            {target.hostCountry}
          </span>
        </h2>
        <div className="text-xs font-sans text-sx-text-secondary flex items-center space-x-2">
          <span className="text-white/90 font-medium">{target.degreeLevel}</span>
          <span className="text-white/30">&bull;</span>
          <span className="text-sx-ice">{target.fieldOfStudy}</span>
          <span className="text-white/30">&bull;</span>
          <span className="text-white/60">{target.fundingLabel}</span>
        </div>
      </div>

      {/* Applicant Context Strip */}
      <div className="flex items-center justify-between p-2 rounded-lg bg-white/[0.03] border border-white/[0.06] mb-3 text-[11px] font-mono text-sx-text-tertiary">
        <div className="flex items-center space-x-2">
          <span className="text-sx-gold font-semibold">STUDENT APPLICANT:</span>
          <span className="text-white/80">{target.applicantContext}</span>
        </div>
        <div className="flex items-center space-x-1 text-sx-ice">
          <ShieldCheck className="w-3.5 h-3.5" />
          <span>HEC BILATERAL PATHWAY</span>
        </div>
      </div>

      {/* Dynamic Knowledge State Banner */}
      <div
        className="flex items-center justify-between px-3 py-1.5 rounded-lg border text-xs font-mono mb-3 transition-all duration-300"
        style={{
          backgroundColor: badge.bg,
          borderColor: badge.border,
          color: badge.color,
        }}
      >
        <div className="flex items-center space-x-2">
          <span
            className="w-1.5 h-1.5 rounded-full"
            style={{ backgroundColor: badge.color }}
          />
          <span className="font-bold tracking-wider uppercase text-[10px]">
            INTELLIGENCE STATE:
          </span>
          <span className="font-semibold text-[11px]">{badge.label}</span>
        </div>

        <span className="text-[10px] opacity-75 font-mono">
          {target.resolvedTraces.length} / 6 STREAMS AUDITED
        </span>
      </div>

      {/* Resolved Intelligence Traces Grid (§52, §53, §54) */}
      <div className="pt-2 border-t border-white/[0.08]">
        <div className="text-[9px] font-mono tracking-wider uppercase text-sx-text-tertiary mb-1.5 flex items-center justify-between">
          <span>ACCUMULATED RESOLVED FINDINGS</span>
          <span>PERSISTENT AUDIT TRACES</span>
        </div>

        {target.resolvedTraces.length === 0 ? (
          <div className="py-2 text-center text-[10px] font-mono text-white/30 italic">
            Investigation initiated. Specialist processes evaluating criteria...
          </div>
        ) : (
          <div className="grid grid-cols-3 gap-2">
            {target.resolvedTraces.map((trace) => (
              <div
                key={trace.id}
                onClick={() => onSelectTrace && onSelectTrace(trace)}
                className="p-1.5 rounded border border-white/[0.08] bg-white/[0.02] hover:bg-white/[0.05] transition-all cursor-pointer flex flex-col space-y-0.5"
                style={{
                  borderLeftColor: trace.color,
                  borderLeftWidth: "3px",
                }}
              >
                <div className="flex items-center justify-between text-[9px] font-mono">
                  <span className="font-bold text-white/80">{trace.label}</span>
                  <span
                    className="px-1 rounded text-[8px] font-bold"
                    style={{
                      color: trace.color,
                      backgroundColor: `${trace.color}20`,
                    }}
                  >
                    {trace.badge}
                  </span>
                </div>
                <div className="text-[10px] font-sans text-white/60 truncate leading-tight">
                  {trace.summary}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </motion.div>
  );
};
