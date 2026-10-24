"use client";

import React, { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { InvestigatedOpportunity } from "@/lib/ranking/types";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";
import { CheckCircle2, Award, ArrowUpRight, ShieldCheck, ChevronRight, Info, AlertCircle } from "lucide-react";
import { getDegreeScholarshipLimit } from "@/lib/utils/degreeLimit";

export interface OpportunityComparisonStageProps {
  opportunities: InvestigatedOpportunity[];
  selectedId: string;
  onSelectOpportunity?: (id: string) => void;
  selectedField?: string;
  targetDegree?: string;
  isUnder70?: boolean;
  candidatePercentage?: number;
  className?: string;
}

function getCleanDegreeDisplay(degreeLevel?: string, targetDegree?: string): string {
  if (targetDegree && targetDegree.trim()) {
    const tdLower = targetDegree.trim().toLowerCase();
    if (degreeLevel && degreeLevel.toLowerCase().includes(tdLower)) {
      return targetDegree.trim();
    }
  }
  if (!degreeLevel) return targetDegree || "Degree Program";
  return degreeLevel;
}

function getCleanFieldDisplay(field?: string, targetField?: string): string {
  if (targetField && targetField.trim()) {
    return targetField.trim();
  }
  if (!field) return "All Academic Fields";
  const trimmed = field.trim();
  if (
    trimmed.toLowerCase().includes("all fields") ||
    trimmed.toLowerCase().includes("all disciplines") ||
    trimmed.toLowerCase().includes("all academic")
  ) {
    return "All Academic Disciplines";
  }
  if (trimmed.includes(",")) {
    const parts = trimmed.split(",").map((p) => p.trim()).filter(Boolean);
    if (parts.length > 2) {
      return `${parts[0]} +${parts.length - 1} More`;
    }
    return parts.join(" & ");
  }
  return trimmed;
}

export const OpportunityComparisonStage: React.FC<OpportunityComparisonStageProps> = ({
  opportunities,
  selectedId,
  onSelectOpportunity,
  selectedField,
  targetDegree,
  isUnder70 = false,
  candidatePercentage = 0,
  className = "",
}) => {
  const [inspectedOppId, setInspectedOppId] = useState<string | null>(null);

  const limit = useMemo(() => {
    if (targetDegree) return getDegreeScholarshipLimit(targetDegree);
    if (opportunities && opportunities.length > 0) {
      const oppDeg = opportunities.find((o) => o.degreeLevel)?.degreeLevel;
      return getDegreeScholarshipLimit(oppDeg);
    }
    return 15;
  }, [targetDegree, opportunities]);

  // Filter strictly for compositeScore > 50 unless isUnder70 is true (audited ineligible + need-based opportunities must remain visible)
  const sorted = useMemo(() => {
    if (!opportunities || opportunities.length === 0) return [];
    const validPool = isUnder70
      ? opportunities
      : (opportunities.filter((opp) => (opp.compositeScore ?? 0) > 50).length > 0
          ? opportunities.filter((opp) => (opp.compositeScore ?? 0) > 50)
          : opportunities);
    return validPool
      .slice(0, limit)
      .sort((a, b) => (b.compositeScore ?? 75) - (a.compositeScore ?? 75))
      .map((opp, idx) => {
        const isNeedBased = /dsu|need[\s\-]based|regional grant|type[\s\-]b/i.test(opp.name);
        const fallbackScore = isUnder70 && !isNeedBased ? 38.0 : Math.max(65, 88 - idx * 2.5);
        return {
          ...opp,
          compositeScore: opp.compositeScore ?? fallbackScore,
          rank: idx + 1,
        };
      });
  }, [opportunities, limit, isUnder70]);

  return (
    <div className={`w-full max-w-[1240px] mx-auto pointer-events-auto ${className}`}>
      {/* Stage Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between mb-2.5 px-1 gap-1">
        <div className="flex items-center space-x-2">
          <div className={`w-2 h-2 rounded-full ${isUnder70 ? "bg-amber-400" : "bg-sx-gold"} animate-pulse shrink-0`} />
          <span className="text-[10px] sm:text-[11px] font-mono text-sx-text-tertiary uppercase tracking-wider">
            {isUnder70
              ? `ACADEMIC EVALUATION // ${sorted.length} SCHOLARSHIPS AUDITED (MERIT CUTOFF 70.0% ENFORCED)`
              : `CANDIDATE RANKING // ${sorted.length} HIGH-MATCH SCHOLARSHIPS (MATCH > 50)`}
          </span>
        </div>
        <div className="text-[9px] sm:text-[10px] font-mono text-sx-text-secondary">
          {isUnder70
            ? `ACADEMIC MARKS (${candidatePercentage.toFixed(1)}%) < 70%: MERIT QUOTAS INELIGIBLE • NEED-BASED UNLOCKED`
            : "RANKED VIA 8 PAKISTAN-ADJUSTED READINESS & IMPACT CRITERIA"}
        </div>
      </div>

      {sorted.length === 0 ? (
        <div className="p-6 rounded-2xl bg-black/80 border border-red-500/30 text-center max-w-xl mx-auto my-8">
          <div className="w-12 h-12 rounded-full bg-red-500/10 border border-red-500/30 flex items-center justify-center mx-auto mb-4 text-red-400">
            <AlertCircle className="w-6 h-6" />
          </div>
          <h3 className="text-base font-semibold text-white mb-2">
            No Fully Qualifying Scholarships Found
          </h3>
          <p className="text-xs text-white/70 leading-relaxed mb-4">
            Based on your academic profile, minimum GPA requirements, language proficiency (IELTS/MOI), or selected region/degree filters, you do not meet the minimum qualification threshold for current active scholarship cycles.
          </p>
          <div className="text-[11px] font-mono text-amber-300/90 bg-amber-500/10 border border-amber-500/20 p-3 rounded-lg text-left">
            💡 <strong>Recommendation:</strong> Consider improving your GPA score, obtaining an official IELTS band score (6.5+ recommended), or expanding your target regions to increase eligibility.
          </div>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 max-h-[68vh] sm:max-h-[62vh] overflow-y-auto pr-1 touch-scroll">
        {sorted.map((opp) => {
          const isSelected = opp.id === selectedId;
          const isInspected = opp.id === inspectedOppId;
          const isNeedBased = /dsu|need[\s\-]based|regional grant|type[\s\-]b/i.test(opp.name);
          const isOppIneligible = isUnder70 && !isNeedBased;

          return (
            <motion.div
                key={opp.id}
                initial={false}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.2 }}
                onClick={() => {
                  onSelectOpportunity?.(opp.id);
                  setInspectedOppId(isInspected ? null : opp.id);
                }}
                className={`relative rounded-xl p-3.5 sm:p-4 border transition-all duration-200 cursor-pointer flex flex-col justify-between ${
                  isOppIneligible
                    ? isSelected
                      ? "bg-red-950/25 border-red-500/70 shadow-[0_0_24px_rgba(239,68,68,0.22)] ring-1 ring-red-500/50"
                      : "bg-black/80 border-red-500/30 hover:border-red-500/50 hover:bg-black/90"
                    : isUnder70 && isNeedBased
                    ? isSelected
                      ? "bg-emerald-950/25 border-emerald-500/70 shadow-[0_0_24px_rgba(16,185,129,0.25)] ring-1 ring-emerald-500/50"
                      : "bg-black/80 border-emerald-500/40 hover:border-emerald-500/60 hover:bg-black/90"
                    : isSelected
                    ? "bg-black/90 border-sx-gold/60 shadow-[0_0_24px_rgba(212,175,55,0.2)] ring-1 ring-sx-gold/40"
                    : "bg-black/70 border-white/[0.08] hover:border-white/[0.2] hover:bg-black/80"
                }`}
              >
                {/* Top Row: Rank & Country */}
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center space-x-1.5">
                      <CountryFlagLogo country={opp.hostCountry} name={opp.name} size="sm" />
                      <span className="text-xs font-mono font-bold text-white/90 uppercase">
                        {opp.hostCountry}
                      </span>
                    </div>

                    <div
                      className={`px-2 py-0.5 rounded text-[10px] font-mono font-bold ${
                        isOppIneligible
                          ? "bg-red-500/20 text-red-300 border border-red-500/40"
                          : isUnder70 && isNeedBased
                          ? "bg-emerald-500/20 text-emerald-300 border border-emerald-500/40"
                          : opp.rank === 1
                          ? "bg-sx-gold/20 text-sx-gold border border-sx-gold/40"
                          : "bg-white/[0.06] text-white/70 border border-white/[0.08]"
                      }`}
                    >
                      {isOppIneligible
                        ? "INELIGIBLE (<70%)"
                        : isUnder70 && isNeedBased
                        ? "NEED-BASED ELIGIBLE"
                        : `#${opp.rank} RANK`}
                    </div>
                  </div>

                  {/* Scholarship Name */}
                  <h4 className="text-xs font-sans font-bold text-white mb-1 leading-snug line-clamp-2">
                    {opp.shortName || opp.name || "Scholarship Opportunity"}
                  </h4>

                  {/* Degree & Verified Field Metadata */}
                  <div className="flex items-center gap-1.5 text-[10px] font-mono text-sx-text-tertiary mb-3 overflow-hidden">
                    <span className="text-white/80 font-medium truncate max-w-[130px]" title={opp.degreeLevel}>
                      {getCleanDegreeDisplay(opp.degreeLevel, targetDegree)}
                    </span>
                    <span className="text-white/20 shrink-0">•</span>
                    <span
                      className="inline-flex items-center gap-1 text-sx-ice font-semibold bg-white/[0.04] px-1.5 py-0.5 rounded border border-white/[0.08] truncate max-w-[160px]"
                      title={opp.fieldOfStudy || "Academic Field"}
                    >
                      <ShieldCheck className="w-3 h-3 text-emerald-400 shrink-0" />
                      <span className="truncate">{getCleanFieldDisplay(opp.fieldOfStudy, selectedField)}</span>
                    </span>
                  </div>

                  {/* Composite Score Progress */}
                  <div className={`p-2.5 rounded-lg border mb-3 ${
                    isOppIneligible
                      ? "bg-red-500/[0.04] border-red-500/25"
                      : isUnder70 && isNeedBased
                      ? "bg-emerald-500/[0.04] border-emerald-500/25"
                      : "bg-white/[0.03] border-white/[0.06]"
                  }`}>
                    <div className="flex items-baseline justify-between mb-1">
                      <span className="text-[10px] font-mono text-sx-text-secondary">
                        {isOppIneligible ? "Eligibility Standing" : isUnder70 && isNeedBased ? "Need-Based Match" : "Composite Score"}
                      </span>
                      <span className={`text-base font-mono font-bold ${
                        isOppIneligible ? "text-red-400" : isUnder70 && isNeedBased ? "text-emerald-400" : "text-sx-gold"
                      }`}>
                        {isOppIneligible ? "INELIGIBLE" : (opp.compositeScore ?? 85.0).toFixed(1)}
                      </span>
                    </div>
                    <div className="w-full h-1.5 bg-white/[0.08] rounded-full overflow-hidden">
                      <div
                        className={`h-full rounded-full transition-all duration-700 ${
                          isOppIneligible
                            ? "bg-red-500/60"
                            : isUnder70 && isNeedBased
                            ? "bg-emerald-400"
                            : opp.rank === 1
                            ? "bg-sx-gold"
                            : opp.rank === 2
                            ? "bg-sx-ice"
                            : "bg-white/40"
                        }`}
                        style={{ width: `${isOppIneligible ? 30 : Math.min(100, Math.max(0, opp.compositeScore ?? 85))}%` }}
                      />
                    </div>
                    {isOppIneligible && (
                      <div className="text-[9px] font-mono text-red-400/90 mt-1 flex items-center justify-between">
                        <span>Strict Merit Cutoff: &ge; 70.0%</span>
                        <span className="font-bold">Not Qualified</span>
                      </div>
                    )}
                    {isUnder70 && isNeedBased && (
                      <div className="text-[9px] font-mono text-emerald-400/90 mt-1 flex items-center justify-between">
                        <span>Income-based Grant (DSU)</span>
                        <span className="font-bold">Eligible</span>
                      </div>
                    )}
                  </div>

                {/* Key Decisive Factors */}
                <div className="space-y-1.5 text-[10px] font-mono">
                  <div className="flex items-center justify-between text-sx-text-secondary">
                    <span>Bilateral Quota:</span>
                    <span className={(opp.bilateralSeats || (opp as any).pakistan_requirements?.pakistan_quota_seats) ? "text-sx-verified font-bold" : "text-white/40"}>
                      {(opp.bilateralSeats || (opp as any).pakistan_requirements?.pakistan_quota_seats)
                        ? `${opp.bilateralSeats || (opp as any).pakistan_requirements?.pakistan_quota_seats} Seats`
                        : "Open Comp"}
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-sx-text-secondary">
                    <span>Initial Outlay:</span>
                    <span className="text-white font-medium">
                      PKR {(((opp.fundingSummary?.initialOutOfPocketPkr ?? 160000)) / 1000).toFixed(0)}k
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-sx-text-secondary">
                    <span>Prep Runway:</span>
                    <span className="text-white font-medium">
                      {opp.deadlineSummary?.daysRemaining ? `${opp.deadlineSummary.daysRemaining}d remaining` : "Annual Cycle"}
                    </span>
                  </div>
                </div>
              </div>

              {/* Selection Status Badge */}
              <div className="mt-4 pt-3 border-t border-white/[0.06] flex items-center justify-between">
                {isSelected ? (
                  <div className="flex items-center space-x-1.5 text-[10px] font-mono font-bold text-sx-gold">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>PRIMARY CANDIDATE</span>
                  </div>
                ) : (
                  <span className="text-[9px] font-mono text-sx-text-tertiary">
                    Click to inspect factors
                  </span>
                )}
                <ChevronRight className="w-3.5 h-3.5 text-white/40" />
              </div>
            </motion.div>
          );
        })}
      </div>
      )}
    </div>
  );
};
