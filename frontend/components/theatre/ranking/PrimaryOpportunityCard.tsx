"use client";

import React from "react";
import { motion } from "framer-motion";
import { InvestigatedOpportunity } from "@/lib/ranking/types";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";
import { ShieldCheck, CheckCircle2, ArrowRight, Compass, Sparkles } from "lucide-react";

export interface PrimaryOpportunityCardProps {
  opportunity: InvestigatedOpportunity;
  onProceedToAdvisor?: () => void;
  className?: string;
}

export const PrimaryOpportunityCard: React.FC<PrimaryOpportunityCardProps> = ({
  opportunity,
  onProceedToAdvisor,
  className = "",
}) => {
  return (
    <motion.div
      initial={false}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.4 }}
      className={`w-full max-w-[860px] mx-auto rounded-2xl border border-sx-gold/50 bg-black/90 backdrop-blur-2xl p-5 shadow-[0_0_40px_rgba(212,175,55,0.18)] ${className}`}
    >
      {/* Top Pre-header */}
      <div className="flex items-center justify-between border-b border-white/[0.08] pb-3 mb-4">
        <div className="flex items-center space-x-2">
          <div className="w-2.5 h-2.5 rounded-full bg-sx-gold animate-pulse" />
          <span className="text-[11px] font-mono font-bold text-sx-gold tracking-widest uppercase">
            PRIMARY OPPORTUNITY // SELECTED FOR DEEPER PLANNING
          </span>
        </div>
        <div className="flex items-center space-x-2 text-[10px] font-mono text-white/50">
          <span>RANK #1 OF 4</span>
          <span>•</span>
          <span className="text-sx-gold font-bold">{opportunity.compositeScore.toFixed(1)}/100 PTS</span>
        </div>
      </div>

      {/* Main Title & Metadata */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
        <div>
          <div className="flex items-center space-x-2 mb-1.5">
            <CountryFlagLogo country={opportunity.hostCountry} name={opportunity.name} size="md" />
            <span className="text-xs font-mono font-bold text-sx-ice uppercase tracking-wider">
              {opportunity.hostCountry} • {opportunity.region}
            </span>
          </div>
          <h2 className="text-xl font-sans font-bold text-white tracking-tight">
            {opportunity.name}
          </h2>
          <div className="text-xs font-mono text-sx-text-secondary mt-1 flex items-center gap-1.5 flex-wrap">
            <span>{opportunity.degreeLevel}</span>
            <span className="text-white/30">•</span>
            <span
              className="text-sx-ice font-semibold truncate max-w-[280px]"
              title={opportunity.fieldOfStudy}
            >
              {opportunity.fieldOfStudy?.includes(",")
                ? opportunity.fieldOfStudy.toLowerCase().includes("all fields")
                  ? "All Academic Disciplines"
                  : opportunity.fieldOfStudy.split(",")[0].trim() + " & More"
                : opportunity.fieldOfStudy || "All Academic Disciplines"}
            </span>
          </div>
        </div>

        {/* 3 Status Pillars */}
        <div className="flex items-center gap-2">
          <div className="px-3 py-2 rounded-xl bg-white/[0.03] border border-white/[0.08] text-center min-w-[100px]">
            <div className="text-[9px] font-mono text-sx-text-tertiary uppercase">INVESTIGATION</div>
            <div className="text-[11px] font-mono font-bold text-sx-verified mt-0.5">COMPLETE</div>
          </div>
          <div className="px-3 py-2 rounded-xl bg-white/[0.03] border border-white/[0.08] text-center min-w-[100px]">
            <div className="text-[9px] font-mono text-sx-text-tertiary uppercase">RANKING</div>
            <div className="text-[11px] font-mono font-bold text-sx-gold mt-0.5">RESOLVED</div>
          </div>
          <div className="px-3 py-2 rounded-xl bg-white/[0.03] border border-white/[0.08] text-center min-w-[100px]">
            <div className="text-[9px] font-mono text-sx-text-tertiary uppercase">STRATEGY</div>
            <div className="text-[11px] font-mono font-bold text-sx-ice mt-0.5">READY</div>
          </div>
        </div>
      </div>

      {/* Grounded Highlights Bar */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-2.5 p-3 rounded-xl bg-white/[0.02] border border-white/[0.06] text-[10px] font-mono mb-4">
        <div>
          <span className="text-sx-text-tertiary block">BILATERAL ALLOCATION:</span>
          <span className="text-white font-semibold">{opportunity.quotaDescription}</span>
        </div>
        <div>
          <span className="text-sx-text-tertiary block">DEADLINE RUNWAY:</span>
          <span className="text-white font-semibold">
            {opportunity.deadlineSummary.applicationDeadline} ({opportunity.deadlineSummary.daysRemaining}d remaining)
          </span>
        </div>
        <div>
          <span className="text-sx-text-tertiary block">INITIAL PKR OUTLAY:</span>
          <span className="text-sx-warning font-semibold">
            PKR {opportunity.fundingSummary.initialOutOfPocketPkr.toLocaleString()} (Flight & Visa)
          </span>
        </div>
      </div>

      {/* Footer Advisory */}
      <div className="flex items-center justify-between text-[11px] font-mono pt-1 text-sx-text-secondary">
        <div className="flex items-center space-x-1.5 text-sx-verified">
          <ShieldCheck className="w-4 h-4" />
          <span>Handing off to Final Advisor for personalized Pakistani institutional roadmap...</span>
        </div>
      </div>
    </motion.div>
  );
};
