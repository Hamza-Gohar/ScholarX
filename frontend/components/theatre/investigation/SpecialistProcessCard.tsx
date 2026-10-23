"use client";

import React from "react";
import { motion } from "framer-motion";
import {
  SpecialistType,
  SpecialistCategory,
  SpecialistState,
  EligibilityResult,
  DocumentAnalysisResult,
  TrueCostResult,
  DeadlineRunway,
  VerificationResult,
  SkepticResult,
  InvestigationSummary,
} from "@/lib/investigation/types";
import {
  CheckCircle2,
  AlertTriangle,
  Clock,
  DollarSign,
  ShieldCheck,
  FileText,
  AlertCircle,
  ExternalLink,
  ChevronRight,
  TrendingDown,
  Calendar,
  Layers,
  Sparkles,
  Cpu,
} from "lucide-react";

export interface SpecialistProcessCardProps {
  type: SpecialistType;
  category: SpecialistCategory;
  displayName: string;
  state: SpecialistState;
  actionLabel: string;
  color: string;
  eligibilityData: EligibilityResult;
  documentData: DocumentAnalysisResult;
  costData: TrueCostResult;
  deadlineData: DeadlineRunway;
  verificationData: VerificationResult;
  skepticData: SkepticResult;
  synthesisSummary: InvestigationSummary;
  className?: string;
}

export const SpecialistProcessCard: React.FC<SpecialistProcessCardProps> = ({
  type,
  category,
  displayName,
  state,
  actionLabel,
  color,
  eligibilityData,
  documentData,
  costData,
  deadlineData,
  verificationData,
  skepticData,
  synthesisSummary,
  className = "",
}) => {
  return (
    <motion.div
      initial={false}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -15 }}
      transition={{ duration: 0.2 }}
      className={`relative rounded-2xl border border-white/[0.12] bg-black/90 backdrop-blur-2xl p-3.5 sm:p-5 shadow-[0_0_50px_rgba(0,0,0,0.85)] pointer-events-auto transition-all duration-300 w-full max-w-[720px] max-h-[85vh] sm:max-h-[420px] flex flex-col justify-between overflow-y-auto sm:overflow-hidden touch-scroll ${className}`}
      style={{
        borderTopColor: color,
        borderTopWidth: "3px",
      }}
    >
      {/* Top subtle highlight */}
      <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-white/30 to-transparent" />

      {/* Header: Specialist Identity & Category Badge */}
      <div className="flex items-center justify-between gap-3 mb-2 shrink-0">
        <div className="flex items-center space-x-2">
          {category === "WORKFLOW" ? (
            <div className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-white/[0.05] border border-white/[0.1] text-[9px] font-mono text-sx-ice font-bold">
              <Cpu className="w-3 h-3 text-sx-ice" />
              <span>DETERMINISTIC WORKFLOW</span>
            </div>
          ) : (
            <div className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-sx-gold/10 border border-sx-gold/30 text-[9px] font-mono text-sx-gold font-bold">
              <Sparkles className="w-3 h-3 text-sx-gold" />
              <span>LLM REASONING AGENT</span>
            </div>
          )}

          <span className="text-[11px] font-mono font-bold text-white tracking-wider">
            {displayName}
          </span>
        </div>

        {/* State Pill */}
        <div
          className="flex items-center space-x-1.5 px-2 py-0.5 rounded text-[9px] font-mono font-bold"
          style={{
            backgroundColor: `${color}18`,
            color: color,
            border: `1px solid ${color}40`,
          }}
        >
          <span className="w-1.5 h-1.5 rounded-full animate-ping" style={{ backgroundColor: color }} />
          <span>{state}</span>
        </div>
      </div>

      {/* Action Sub-header */}
      <div className="text-[10px] font-mono text-sx-text-tertiary mb-2.5 truncate shrink-0">
        OPERATIONAL STATUS: <span className="text-white/90 font-medium">{actionLabel}</span>
      </div>

      {/* Specialized Internal Body by Type */}
      <div className="flex-1 overflow-y-auto pr-1 text-xs">
        {/* ========================================================================= */}
        {/* 1. ELIGIBILITY INVESTIGATOR WORKFLOW (§10, §11)                           */}
        {/* ========================================================================= */}
        {type === "ELIGIBILITY" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-white/[0.03] border border-white/[0.06] text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-sx-emerald font-bold">DIMENSION AUDIT:</span>
                <span className="text-white/80">13 OF 15 MATCHED // 400 BILATERAL SEATS</span>
              </div>
              <span className="text-sx-gold font-bold">HEC USAT REQUIRED</span>
            </div>

            <div className="grid grid-cols-2 gap-1.5 max-h-[190px] overflow-y-auto pr-1">
              {eligibilityData.criteria.slice(0, 8).map((crit) => (
                <div
                  key={crit.id}
                  className="p-1.5 rounded border border-white/[0.06] bg-white/[0.02] flex items-start justify-between gap-1 text-[10px] font-mono"
                >
                  <div className="truncate pr-1">
                    <div className="text-white/90 font-medium truncate">{crit.dimensionName}</div>
                    <div className="text-white/50 text-[9px] truncate">{crit.studentValue}</div>
                  </div>
                  <span
                    className={`px-1.5 py-0.2 rounded text-[8px] font-bold shrink-0 ${
                      crit.status === "PASS"
                        ? "bg-sx-emerald/20 text-sx-emerald border border-sx-emerald/30"
                        : crit.status === "BONUS"
                        ? "bg-sx-gold/20 text-sx-gold border border-sx-gold/30"
                        : "bg-sx-amber/20 text-sx-amber border border-sx-amber/30"
                    }`}
                  >
                    {crit.status}
                  </span>
                </div>
              ))}
            </div>

            <div className="p-1.5 rounded bg-sx-amber/10 border border-sx-amber/30 text-[10px] font-mono text-sx-amber flex items-center space-x-1.5">
              <AlertTriangle className="w-3.5 h-3.5 shrink-0" />
              <span className="truncate">ACTION REQUIRED: {eligibilityData.actionRequired}</span>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* 2. DOCUMENT ANALYST AGENT (§12, §13)                                      */}
        {/* ========================================================================= */}
        {type === "DOCUMENT" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-white/[0.03] border border-white/[0.06] text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-sx-amber font-bold">READINESS STATUS:</span>
                <span className="text-white/80">{documentData.readinessScore}% READY // {documentData.readyCount} OF {documentData.totalRequired} VERIFIED</span>
              </div>
              <span className="text-sx-ice font-bold">{documentData.totalPrepDays} DAYS PREP TIME</span>
            </div>

            <div className="grid grid-cols-2 gap-1.5 max-h-[190px] overflow-y-auto pr-1">
              {documentData.documents.map((doc) => (
                <div
                  key={doc.id}
                  className="p-1.5 rounded border border-white/[0.06] bg-white/[0.02] flex items-start justify-between gap-1 text-[10px] font-mono"
                >
                  <div className="truncate pr-1">
                    <div className="text-white/90 font-medium truncate">{doc.documentName}</div>
                    <div className="text-white/50 text-[9px] truncate">
                      {doc.pakistanLeadDays > 0 ? `${doc.pakistanLeadDays}d lead time` : "Instant verification"}
                    </div>
                  </div>
                  <span
                    className={`px-1.5 py-0.2 rounded text-[8px] font-bold shrink-0 ${
                      doc.status === "READY"
                        ? "bg-sx-emerald/20 text-sx-emerald border border-sx-emerald/30"
                        : doc.status === "REQUIRED"
                        ? "bg-sx-rose/20 text-sx-rose border border-sx-rose/30"
                        : "bg-sx-amber/20 text-sx-amber border border-sx-amber/30"
                    }`}
                  >
                    {doc.status}
                  </span>
                </div>
              ))}
            </div>

            <div className="p-1.5 rounded bg-white/[0.04] border border-white/[0.08] text-[10px] font-mono text-white/70 flex items-center justify-between">
              <span>CRITICAL GAPS: {documentData.criticalMissing.join(" • ")}</span>
              <span className="text-sx-gold">EST. PKR {documentData.totalPrepCostPkr.toLocaleString()}</span>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* 3. TRUE COST ANALYZER WORKFLOW (§14, §15)                                  */}
        {/* ========================================================================= */}
        {type === "COST" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-sx-rose/10 border border-sx-rose/30 text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-sx-rose font-bold">REAL OUT-OF-POCKET:</span>
                <span className="text-white font-bold text-xs">PKR {costData.totalOutOfPocketPkr.toLocaleString()} (~${costData.totalOutOfPocketUsd})</span>
              </div>
              <span className="text-sx-amber font-bold">DEFICIT: PKR {costData.shortfallPkr.toLocaleString()}</span>
            </div>

            {/* Cost Waterfall */}
            <div className="grid grid-cols-4 gap-2 text-[10px] font-mono">
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06] text-center">
                <div className="text-white/50 text-[9px]">TUITION & DORM</div>
                <div className="text-sx-emerald font-bold my-0.5">100% WAIVED</div>
                <div className="text-white/40 text-[8px]">Covered by MoU</div>
              </div>
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06] text-center">
                <div className="text-white/50 text-[9px]">PRE-APPLICATION</div>
                <div className="text-white font-bold my-0.5">PKR 8,500</div>
                <div className="text-white/40 text-[8px]">HEC USAT + Attest</div>
              </div>
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06] text-center">
                <div className="text-white/50 text-[9px]">AIRFARE & MEDICAL</div>
                <div className="text-sx-rose font-bold my-0.5">PKR 235,000</div>
                <div className="text-white/40 text-[8px]">Flight Uncovered</div>
              </div>
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06] text-center">
                <div className="text-white/50 text-[9px]">SETTLEMENT CASH</div>
                <div className="text-sx-amber font-bold my-0.5">PKR 60,000</div>
                <div className="text-white/40 text-[8px]">Pre-Stipend Reserve</div>
              </div>
            </div>

            <div className="p-1.5 rounded bg-white/[0.03] border border-white/[0.06] text-[10px] font-mono text-white/70">
              <span className="text-sx-gold font-bold">BUDGET RISK: </span>
              <span>Student savings (PKR {costData.studentMaxBudgetPkr.toLocaleString()}) insufficient for flight. Requires supplementary funding.</span>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* 4. DEADLINE INTELLIGENCE WORKFLOW (§16, §17)                               */}
        {/* ========================================================================= */}
        {type === "DEADLINE" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-sx-ice/10 border border-sx-ice/30 text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-sx-ice font-bold">TEMPORAL RUNWAY:</span>
                <span className="text-white font-bold">{deadlineData.daysRemaining} DAYS REMAINING (DEADLINE: {deadlineData.deadlineDisplay})</span>
              </div>
              <span className="text-sx-emerald font-bold">{deadlineData.feasibility} ({deadlineData.availableSlackDays}D SLACK)</span>
            </div>

            {/* Horizontal Runway Progress Indicator */}
            <div className="p-2.5 rounded bg-white/[0.02] border border-white/[0.06] space-y-1.5 text-[10px] font-mono">
              <div className="flex items-center justify-between text-[9px] text-white/60">
                <span>TODAY</span>
                <span>PREP: 28 DAYS</span>
                <span>BUFFER: 7 DAYS</span>
                <span className="text-sx-ice font-bold">SLACK: 37 DAYS</span>
                <span>15 JAN 2027</span>
              </div>

              <div className="w-full h-3 rounded-full bg-white/[0.08] overflow-hidden flex">
                <div className="h-full bg-sx-amber/70" style={{ width: "38%" }} title="Preparation Path: 28 Days" />
                <div className="h-full bg-white/20" style={{ width: "10%" }} title="Buffer Margin: 7 Days" />
                <div className="h-full bg-sx-emerald/70" style={{ width: "52%" }} title="Available Slack: 37 Days" />
              </div>
            </div>

            {/* Lead Time Offices Table */}
            <div className="grid grid-cols-2 gap-1.5 text-[9px] font-mono">
              {deadlineData.leadTimeItems.slice(0, 4).map((item, idx) => (
                <div key={idx} className="p-1.5 rounded bg-white/[0.02] border border-white/[0.05] flex items-center justify-between">
                  <span className="text-white/80 truncate">{item.process}</span>
                  <span className="text-sx-ice font-bold">{item.durationDays}d lead</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* 5. VERIFICATION AGENT (§20, §21, §22)                                     */}
        {/* ========================================================================= */}
        {type === "VERIFICATION" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-sx-emerald/10 border border-sx-emerald/30 text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-sx-emerald font-bold">VERIFICATION VERDICT:</span>
                <span className="text-white font-bold">{verificationData.status} {"//"} {verificationData.confidenceScore}% CONFIDENCE</span>
              </div>
              <span className="text-white/60">{verificationData.sourcesCrossChecked} AUTHORITATIVE SOURCES CHECKED</span>
            </div>

            <div className="space-y-1.5 max-h-[190px] overflow-y-auto pr-1">
              {verificationData.claims.map((claim) => (
                <div
                  key={claim.id}
                  className="p-2 rounded border border-white/[0.08] bg-white/[0.02] space-y-1 text-[10px] font-mono"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-white/90 font-bold truncate max-w-[480px]">{claim.claim}</span>
                    <span
                      className={`px-1.5 py-0.2 rounded text-[8px] font-bold ${
                        claim.verdict === "CONFIRMED"
                          ? "bg-sx-emerald/20 text-sx-emerald border border-sx-emerald/30"
                          : "bg-sx-gold/20 text-sx-gold border border-sx-gold/30"
                      }`}
                    >
                      {claim.verdict}
                    </span>
                  </div>

                  <div className="text-[9px] text-white/50 flex items-center space-x-2">
                    <span className="text-sx-ice">{claim.primarySource.name}</span>
                    <span>&bull;</span>
                    <span className="text-white/40">{claim.primarySource.domain}</span>
                  </div>

                  {claim.hasConflict && claim.conflictDetails && (
                    <div className="p-1.5 rounded bg-sx-gold/10 border border-sx-gold/20 text-[9px] text-sx-gold mt-1">
                      <div className="font-bold">CONFLICT DETECTED & RESOLVED:</div>
                      <div className="text-white/80">{claim.conflictDetails.resolution}</div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* 6. SKEPTIC AGENT (§24, §25, §26, §28)                                     */}
        {/* ========================================================================= */}
        {type === "SKEPTIC" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-sx-gold/10 border border-sx-gold/30 text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-sx-gold font-bold">ADVERSARIAL CHALLENGES:</span>
                <span className="text-white font-bold">{skepticData.totalChallengesRaised} RAISED // {skepticData.resolvedChallengesCount} AUDITED</span>
              </div>
              <span className="text-sx-amber font-bold">{skepticData.criticalRisksFlagged} RISKS QUALIFIED</span>
            </div>

            <div className="space-y-2 max-h-[190px] overflow-y-auto pr-1">
              {skepticData.challenges.map((c) => (
                <div
                  key={c.id}
                  className="p-2 rounded border border-white/[0.08] bg-white/[0.02] space-y-1 text-[10px] font-mono"
                >
                  <div className="flex items-center justify-between text-sx-gold font-bold">
                    <span>{c.title}</span>
                    <span className="px-1.5 py-0.2 rounded text-[8px] bg-sx-gold/20 text-sx-gold border border-sx-gold/30">
                      {c.status}
                    </span>
                  </div>
                  <div className="text-white/80 text-[10px] font-sans leading-tight">
                    {c.challengeText}
                  </div>
                  <div className="p-1.5 rounded bg-white/[0.04] text-[9px] text-sx-emerald">
                    <span className="font-bold">EVIDENCE RESOLUTION: </span>
                    <span>{c.impactSummary}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* 7. SYNTHESIS WORKFLOW SUMMARY (§30, §31, §32)                             */}
        {/* ========================================================================= */}
        {type === "SYNTHESIS" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between p-2 rounded bg-purple-500/15 border border-purple-500/35 text-[10px] font-mono">
              <div className="flex items-center space-x-2">
                <span className="text-purple-400 font-bold">INVESTIGATION SUMMARY:</span>
                <span className="text-white font-bold">UNIFIED CANDIDATE INTELLIGENCE READY</span>
              </div>
              <span className="text-sx-emerald font-bold">EMPIRICALLY VERIFIED</span>
            </div>

            <div className="grid grid-cols-3 gap-2 text-[10px] font-mono">
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06]">
                <div className="text-white/50 text-[9px]">ELIGIBILITY</div>
                <div className="text-sx-emerald font-bold my-0.5 truncate">{synthesisSummary.overallEligibility}</div>
                <div className="text-white/40 text-[8px]">400 Quota Seats</div>
              </div>
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06]">
                <div className="text-white/50 text-[9px]">READINESS & TIME</div>
                <div className="text-sx-amber font-bold my-0.5 truncate">{synthesisSummary.documentReadiness}</div>
                <div className="text-white/40 text-[8px]">28 Days Lead Needed</div>
              </div>
              <div className="p-2 rounded bg-white/[0.02] border border-white/[0.06]">
                <div className="text-white/50 text-[9px]">TRUE PKR COST</div>
                <div className="text-sx-rose font-bold my-0.5">PKR {synthesisSummary.realInitialOutlayPkr.toLocaleString()}</div>
                <div className="text-white/40 text-[8px]">Airfare Deficit Noted</div>
              </div>
            </div>

            <div className="p-2 rounded bg-white/[0.03] border border-white/[0.06] text-[10px] font-mono text-white/80">
              <div className="text-sx-gold font-bold mb-0.5">ADVISORY ASSESSMENT:</div>
              <div className="font-sans leading-relaxed text-white/90">{synthesisSummary.criticalAdvisory}</div>
            </div>
          </div>
        )}
      </div>
    </motion.div>
  );
};
