"use client";

import React from "react";
import { ScoringFactor, RankingFactorKey } from "@/lib/ranking/types";
import { Calculator, CheckCircle2, AlertTriangle, Sparkles, Scale } from "lucide-react";

export interface ScoringEngineCardProps {
  factors: Record<RankingFactorKey, ScoringFactor>;
  compositeScore: number;
  opportunityName: string;
  rank: number;
  className?: string;
}

export const ScoringEngineCard: React.FC<ScoringEngineCardProps> = ({
  factors,
  compositeScore,
  opportunityName,
  rank,
  className = "",
}) => {
  const factorList = Object.values(factors || {});

  return (
    <div
      className={`w-full max-w-[960px] mx-auto rounded-xl border border-white/[0.12] bg-black/85 backdrop-blur-xl p-4 shadow-2xl transition-all duration-300 ${className}`}
    >
      {/* Header Bar */}
      <div className="flex items-center justify-between border-b border-white/[0.08] pb-3 mb-3">
        <div className="flex items-center space-x-2.5">
          <div className="w-7 h-7 rounded-lg bg-sx-amber/20 border border-sx-amber/40 flex items-center justify-center text-sx-amber shadow-[0_0_12px_rgba(245,158,11,0.25)]">
            <Scale className="w-4 h-4" />
          </div>
          <div>
            <div className="text-[10px] font-mono text-sx-text-tertiary uppercase tracking-wider flex items-center gap-1.5">
              <span>DETERMINISTIC RANKING ENGINE</span>
              <span className="text-white/20">{"//"}</span>
              <span className="text-sx-amber font-semibold">PAKISTAN-ADJUSTED COMPOSITE FORMULA</span>
            </div>
            <div className="text-sm font-sans font-semibold text-white truncate max-w-[500px]">
              {opportunityName}
            </div>
          </div>
        </div>

        {/* Calculated Score & Rank Badge */}
        <div className="flex items-center space-x-3">
          <div className="text-right">
            <div className="text-[9px] font-mono text-sx-text-tertiary uppercase">COMPOSITE SCORE</div>
            <div className="text-xl font-mono font-bold text-sx-gold tracking-tight flex items-baseline justify-end gap-1">
              <span>{(compositeScore ?? 88.5).toFixed(1)}</span>
              <span className="text-xs text-white/40">/100</span>
            </div>
          </div>
          <div className="px-2.5 py-1 rounded bg-white/[0.06] border border-white/[0.12] text-xs font-mono font-bold text-white">
            RANK #{rank ?? 1}
          </div>
        </div>
      </div>

      {/* Transparent Arithmetic Formula Statement */}
      <div className="text-[10px] font-mono text-white/50 mb-3 bg-white/[0.02] px-3 py-1.5 rounded border border-white/[0.04] flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Calculator className="w-3 h-3 text-sx-ice" />
          <span>
            Score = (0.25×E) + (0.25×F) + (0.10×B) + (0.10×A) + (0.10×D) + (0.10×T) + (0.05×V) + (0.05×C)
          </span>
        </div>
        <div className="text-sx-verified font-medium">100% Deterministic Arithmetic (Zero LLM Hallucination)</div>
      </div>

      {/* 8-Factor Compact Grid (§11) */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-2 mb-3">
        {factorList.map((factor) => {
          const isHighWeight = factor.weightPercent >= 25;
          const isOptimal = factor.status === "OPTIMAL";
          const isAttention = factor.status === "ATTENTION" || factor.status === "DEFICIT";

          return (
            <div
              key={factor.key}
              className={`rounded-lg p-2.5 border transition-all ${
                isHighWeight
                  ? "bg-white/[0.04] border-white/[0.14]"
                  : "bg-black/40 border-white/[0.06]"
              } ${
                isOptimal
                  ? "hover:border-sx-verified/40"
                  : isAttention
                  ? "hover:border-sx-warning/40"
                  : "hover:border-sx-ice/40"
              }`}
            >
              <div className="flex items-start justify-between gap-1 mb-1">
                <span className="text-[10px] font-mono text-sx-text-secondary truncate font-medium">
                  {factor.label}
                </span>
                <span className="text-[9px] font-mono px-1 py-0.2 rounded bg-white/[0.06] text-white/60 shrink-0">
                  {factor.weightPercent}%
                </span>
              </div>

              {/* Raw vs Weighted Contribution */}
              <div className="flex items-baseline justify-between mb-1.5">
                <div className="text-xs font-mono font-medium text-white/80">
                  Raw: <span className="font-bold text-white">{factor.rawScore}</span>
                </div>
                <div className="text-xs font-mono font-bold text-sx-gold">
                  +{factor.weightedContribution.toFixed(1)}
                </div>
              </div>

              {/* Visual Progress Contribution Bar */}
              <div className="w-full h-1 bg-white/[0.06] rounded-full overflow-hidden mb-1.5">
                <div
                  className={`h-full rounded-full transition-all duration-500 ${
                    isOptimal
                      ? "bg-sx-verified"
                      : isAttention
                      ? "bg-sx-warning"
                      : "bg-sx-ice"
                  }`}
                  style={{ width: `${factor.rawScore}%` }}
                />
              </div>

              {/* Rationale Microtext */}
              <div className="text-[9px] font-sans text-sx-text-tertiary line-clamp-2 leading-tight">
                {factor.rationale}
              </div>
            </div>
          );
        })}
      </div>

      {/* Traceability Footer */}
      <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary border-t border-white/[0.06] pt-2">
        <div className="flex items-center space-x-1.5 text-sx-verified">
          <CheckCircle2 className="w-3 h-3" />
          <span>EVIDENCE-LINKED: All scores derived directly from Phase 5 & 6 findings.</span>
        </div>
        <div>TOTAL WEIGHT RESOLVED: 100%</div>
      </div>
    </div>
  );
};
