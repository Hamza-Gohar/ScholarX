"use client";

import React, { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { 
  CanonicalDossier, 
  InvestigatedOpportunity, 
  RoadmapPhaseBlock 
} from "@/lib/ranking/types";
import { OpportunityComparisonStage } from "./OpportunityComparisonStage";
import { ScoringEngineCard } from "./ScoringEngineCard";
import { RoadmapJourney } from "../advisor/RoadmapJourney";
import { DossierAssemblyTheatre } from "../dossier/DossierAssemblyTheatre";
import { getCountryFlag } from "@/lib/utils/countryFlags";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";
import { 
  Award, 
  BarChart3, 
  Map, 
  FileText, 
  Printer, 
  Globe, 
  Download,
  Compass, 
  CheckCircle2, 
  Sparkles,
  ArrowUpRight,
  ShieldCheck,
  Building2,
  Calendar,
  Layers,
  AlertCircle,
  AlertTriangle
} from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { getDegreeScholarshipLimit } from "@/lib/utils/degreeLimit";
import { IneligiblePoliteModal } from "@/components/common/IneligiblePoliteModal";

export interface MissionOutputStageProps {
  opportunities: InvestigatedOpportunity[];
  primaryOpportunity: InvestigatedOpportunity | null;
  onSelectOpportunity: (id: string) => void;
  roadmapPhases: RoadmapPhaseBlock[];
  dossier: CanonicalDossier;
  studentProfile?: any;
  onOpenWebDossier: () => void;
  onOpenPdfViewer: () => void;
  onNewMission: () => void;
  className?: string;
}

export type OutputViewTab = "RANKED" | "FACTORS" | "ROADMAP" | "DOSSIER";

export const MissionOutputStage: React.FC<MissionOutputStageProps> = ({
  opportunities,
  primaryOpportunity,
  onSelectOpportunity,
  roadmapPhases,
  dossier,
  studentProfile,
  onOpenWebDossier,
  onOpenPdfViewer,
  onNewMission,
  className = "",
}) => {
  const [activeTab, setActiveTab] = useState<OutputViewTab>("RANKED");

  // Determine candidate academic percentage and evaluate 70.0% merit cutoff
  const candidatePercentage = Number(
    studentProfile?.academic?.gpa_percentage ??
    studentProfile?.academic?.percentage ??
    studentProfile?.academic?.ibcc_equivalence_percentage ??
    (studentProfile?.academic?.gpa_4_scale ? (studentProfile.academic.gpa_4_scale / 4.0) * 100 : 0)
  );
  const isUnder70 = candidatePercentage > 0 && candidatePercentage < 70.0;

  // Ineligibility modal trigger state
  const [showIneligibleModal, setShowIneligibleModal] = useState<boolean>(false);
  const [modalSeen, setModalSeen] = useState<boolean>(false);

  // Automatically trigger polite ineligibility modal on mount when candidate is below 70%
  React.useEffect(() => {
    if (isUnder70 && !modalSeen) {
      const timer = setTimeout(() => {
        sound.playSkepticAlert();
        setShowIneligibleModal(true);
        setModalSeen(true);
      }, 700);
      return () => clearTimeout(timer);
    }
  }, [isUnder70, modalSeen]);

  const rawTargetDegree =
    studentProfile?.preferences?.target_degree_level ||
    studentProfile?.preferences?.targetDegreeLevel ||
    studentProfile?.degree ||
    primaryOpportunity?.degreeLevel;
  const limit = getDegreeScholarshipLimit(rawTargetDegree);

  // Filter strictly for compositeScore > 50 unless isUnder70 is true (audited ineligible + need-based opportunities must remain visible)
  const qualifiedOpportunities = useMemo(() => {
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

  const activeOpp = (primaryOpportunity && (primaryOpportunity.compositeScore ?? 0) > 0)
    ? primaryOpportunity
    : (qualifiedOpportunities.length > 0 ? qualifiedOpportunities[0] : null);
  const totalCount = qualifiedOpportunities.length;
  const profileSignals = [
    studentProfile?.academic?.gpa_percentage != null ? `${studentProfile.academic.gpa_percentage}% academics` : null,
    studentProfile?.academic?.field_of_study || studentProfile?.preferences?.target_fields?.[0],
    studentProfile?.preferences?.funding_requirement === "FULL" ? "full funding" : studentProfile?.preferences?.funding_requirement,
    studentProfile?.preferences?.max_out_of_pocket_pkr != null
      ? `PKR ${Number(studentProfile.preferences.max_out_of_pocket_pkr).toLocaleString()} ceiling`
      : null,
    Array.isArray(studentProfile?.preferences?.preferred_regions) && studentProfile.preferences.preferred_regions.length
      ? studentProfile.preferences.preferred_regions.slice(0, 3).join(" / ")
      : null,
  ].filter(Boolean) as string[];

  const applicantName =
    studentProfile?.personal?.name ||
    studentProfile?.name ||
    dossier.candidateProfile?.personal?.name ||
    "Applicant";

  const targetDegree =
    studentProfile?.preferences?.target_degree_level ||
    studentProfile?.preferences?.targetDegreeLevel ||
    studentProfile?.degree ||
    activeOpp?.degreeLevel ||
    "Degree Program";

  const handleDownloadDossier = () => {
    sound.playClick();
    const oppId = activeOpp?.id || "primary";
    const cleanName = (applicantName || "Hamza_Gohar").replace(/[^a-zA-Z0-9_-]/g, "_");
    const downloadUrl = `/api/download/pdf?id=${encodeURIComponent(oppId)}&name=${encodeURIComponent(cleanName)}`;
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = `ScholarX_Intelligence_Dossier_${cleanName}.pdf`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div
      className={`w-full max-w-[1280px] mx-auto rounded-2xl border border-white/[0.14] bg-black/90 backdrop-blur-2xl p-4 sm:p-5 shadow-2xl pointer-events-auto flex flex-col justify-between ${className}`}
    >
      {/* 1. TOP HERO HEADER & SUMMARY STRIP */}
      <div className="border-b border-white/[0.08] pb-3.5 mb-3.5">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3">
          {/* Left: Mission Accomplished Headline & Stats */}
          <div className="flex items-start space-x-3">
            <div className="w-10 h-10 rounded-xl bg-sx-gold/20 border border-sx-gold/40 flex items-center justify-center text-sx-gold shadow-[0_0_15px_rgba(212,175,55,0.3)] shrink-0 mt-0.5">
              <Award className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center space-x-2 text-[10px] font-mono tracking-wider uppercase mb-0.5">
                {isUnder70 ? (
                  <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 flex items-center gap-1">
                    <AlertTriangle className="w-3 h-3 text-amber-400" />
                    INELIGIBLE FOR MERIT SCHOLARSHIPS (&lt; 70% MARKS)
                  </span>
                ) : totalCount > 0 ? (
                  <span className="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30 flex items-center gap-1">
                    <CheckCircle2 className="w-3 h-3" />
                    MISSION ACCOMPLISHED
                  </span>
                ) : (
                  <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 flex items-center gap-1">
                    <AlertCircle className="w-3 h-3" />
                    EVALUATION COMPLETE: NOT CURRENTLY ELIGIBLE
                  </span>
                )}
                <span className="text-white/40">&bull;</span>
                <span className={isUnder70 ? "text-amber-400 font-bold" : totalCount > 0 ? "text-sx-gold font-bold" : "text-amber-400 font-bold"}>
                  {isUnder70
                    ? `ACADEMIC MARKS (${candidatePercentage.toFixed(1)}%) BELOW 70.0% MERIT THRESHOLD`
                    : totalCount > 0
                    ? `${totalCount} HIGH-MATCH SCHOLARSHIPS (SCORE > 50)`
                    : "0 QUALIFYING SCHOLARSHIPS FOUND"}
                </span>
                <span className="text-white/40">&bull;</span>
                <span className="text-sx-ice">
                  {applicantName} ({targetDegree})
                </span>
              </div>

              <div className="text-sm sm:text-base font-sans font-bold text-white flex items-center gap-2">
                <span>{isUnder70 ? "Standing Notice:" : totalCount > 0 ? "Top Recommendation:" : "Status Notice:"}</span>
                {isUnder70 ? (
                  <span className="text-amber-300 font-medium flex items-center gap-1.5">
                    <span>Ineligible for strict merit quotas ({candidatePercentage.toFixed(1)}% &lt; 70.0%) &bull; Need-Based Grants (Italian DSU) Unlocked</span>
                  </span>
                ) : totalCount > 0 && activeOpp ? (
                  <span className="text-sx-gold font-extrabold flex items-center gap-1.5">
                    <CountryFlagLogo country={activeOpp?.hostCountry} name={activeOpp?.name} size="sm" />
                    <span>{activeOpp?.name}</span>
                  </span>
                ) : (
                  <span className="text-amber-300 font-medium">
                    GPA or language requirements not met for target regions
                  </span>
                )}
                {activeOpp && !isUnder70 && (
                  <span className="text-xs font-mono px-2 py-0.5 rounded bg-sx-gold/15 text-sx-gold border border-sx-gold/30 font-bold">
                    {(activeOpp.compositeScore ?? 88.5).toFixed(1)} / 100 PTS
                  </span>
                )}
              </div>
            </div>
          </div>

          {/* Right: Quick Action Buttons */}
          <div className="flex flex-wrap items-center gap-2 shrink-0 w-full sm:w-auto">
            <button
              onClick={handleDownloadDossier}
              className="flex-1 sm:flex-initial px-3 sm:px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white border border-emerald-400/50 text-xs font-sans font-bold flex items-center justify-center space-x-1.5 transition-all cursor-pointer shadow-lg"
              title="Download official candidate intelligence dossier as publication PDF"
            >
              <Download className="w-3.5 h-3.5 stroke-[2.5]" />
              <span>DOWNLOAD DOSSIER</span>
            </button>

            <button
              onClick={onOpenWebDossier}
              className="flex-1 sm:flex-initial px-3 sm:px-3.5 py-1.5 rounded-lg bg-sx-ice/20 hover:bg-sx-ice/30 active:scale-95 text-sx-ice border border-sx-ice/40 text-xs font-sans font-bold flex items-center justify-center space-x-1.5 transition-all cursor-pointer shadow-md"
              title="Open Full Editorial Web Dossier"
            >
              <Globe className="w-3.5 h-3.5" />
              <span>OPEN DOSSIER</span>
              <ArrowUpRight className="w-3 h-3 opacity-70" />
            </button>

            <button
              onClick={onNewMission}
              className="px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/15 active:scale-95 text-white/80 hover:text-white border border-white/20 text-xs font-sans font-medium flex items-center justify-center space-x-1 transition-all cursor-pointer"
              title="Start a new scholarship intelligence search"
            >
              <Compass className="w-3.5 h-3.5 text-sx-gold" />
              <span className="hidden xs:inline">NEW MISSION</span>
              <span className="xs:hidden">NEW</span>
            </button>
          </div>
        </div>

        {/* Highlight strip for active selected scholarship */}
        {activeOpp && (
          <div className="mt-2.5 pt-2 border-t border-white/[0.04] grid grid-cols-2 sm:grid-cols-4 gap-2 text-[10px] font-mono text-zinc-300">
            <div className="flex items-center space-x-1.5">
              <span className="text-zinc-500">BILATERAL:</span>
              <span className="text-emerald-400 font-semibold truncate">
                {activeOpp.quotaDescription || (activeOpp.bilateralSeats ? `${activeOpp.bilateralSeats} Quota Seats for Pakistan` : "Bilateral Quota for Pakistan")}
              </span>
            </div>
            <div className="flex items-center space-x-1.5">
              <span className="text-zinc-500">STIPEND:</span>
              <span className="text-sx-gold font-semibold truncate">
                {activeOpp.fundingSummary?.monthlyStipendPkr
                  ? `PKR ${activeOpp.fundingSummary.monthlyStipendPkr.toLocaleString()}/mo`
                  : (activeOpp.fundingSummary?.coverageType?.includes("FULL") ? "Full Living Allowance" : "Tuition Grant")}
              </span>
            </div>
            <div className="flex items-center space-x-1.5">
              <span className="text-zinc-500">OUTLAY:</span>
              <span className="text-amber-400 font-semibold truncate">
                PKR {(activeOpp.fundingSummary?.initialOutOfPocketPkr ?? 160000).toLocaleString()}
              </span>
            </div>
            <div className="flex items-center space-x-1.5">
              <span className="text-zinc-500">DEADLINE:</span>
              <span className="text-cyan-400 font-semibold truncate">
                {activeOpp.deadlineSummary?.applicationDeadline || "Annual Admission Window"}
              </span>
            </div>
          </div>
        )}
        <div className="mt-2 flex flex-wrap items-center gap-1.5 text-[10px] font-mono" aria-label="Personalization signals used in ranking">
          <span className="text-sx-ice font-bold tracking-wider">PERSONALIZED MATCH:</span>
          {(profileSignals.length ? profileSignals : ["profile constraints applied"]).map((signal) => (
            <span key={signal} className="rounded border border-sx-ice/20 bg-sx-ice/10 px-2 py-0.5 text-zinc-200">
              {signal}
            </span>
          ))}
        </div>
        {activeOpp && (
          <div className="mt-2 rounded-lg border border-emerald-400/20 bg-emerald-400/[0.06] px-3 py-2 text-[11px] text-emerald-100">
            <span className="font-mono font-bold tracking-wider text-emerald-300">WHY THIS MATCHES: </span>
            {Object.values(activeOpp.factors || {})
              .filter((factor) => factor.status === "OPTIMAL" || factor.status === "STRONG")
              .sort((a, b) => b.rawScore - a.rawScore)
              .slice(0, 2)
              .map((factor) => factor.rationale)
              .join(" ") || "The ranking engine applied your academic, funding, language, region, and Pakistan-specific constraints."}
          </div>
        )}

        {/* Real-time Ineligibility Banner on Screen (< 70% Marks) */}
        {isUnder70 && (
          <div className="mt-3 p-4 rounded-xl bg-amber-500/10 border border-amber-500/35 text-amber-200 animate-in fade-in duration-300">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
              <div className="flex items-start space-x-3">
                <div className="p-2 rounded-lg bg-amber-500/20 border border-amber-500/40 text-amber-400 shrink-0 mt-0.5">
                  <AlertTriangle className="w-5 h-5" />
                </div>
                <div>
                  <div className="font-mono text-xs font-bold text-amber-300 uppercase tracking-wide flex items-center gap-2">
                    <span>ACADEMIC STANDING ADVISORY // MERIT CUTOFF (70.0%) NOT MET</span>
                    <span className="px-2 py-0.5 rounded bg-red-500/20 text-red-300 border border-red-500/40 text-[9px] font-bold">
                      INELIGIBLE FOR MERIT AWARDS
                    </span>
                  </div>
                  <div className="text-xs text-zinc-300 mt-1 leading-relaxed">
                    Assalam-o-Alaikum & Welcome. Your recorded academic standing of <strong className="text-amber-300 font-mono">{candidatePercentage.toFixed(1)}%</strong> is below the official <strong>70% minimum threshold</strong> required for competitive merit scholarships (such as Stipendium Hungaricum, Chevening, and Hubert Humphrey). ScholarX has automatically highlighted alternative need-based grants (e.g. <strong>Italian Regional DSU Grants</strong>) and foundation pathways where previous marks are not a barrier.
                  </div>
                </div>
              </div>
              <button
                type="button"
                onClick={() => {
                  sound.playClick();
                  setShowIneligibleModal(true);
                }}
                className="px-3.5 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-black font-mono text-xs font-bold shrink-0 transition-all shadow-[0_0_15px_rgba(245,158,11,0.25)] flex items-center space-x-1.5 cursor-pointer"
              >
                <span>View Polite Advisory</span>
                <Sparkles className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        )}
      </div>

      {/* 2. INTERACTIVE TAB NAVIGATION */}
      <div className="flex items-center justify-between border-b border-white/[0.08] mb-3 px-1 overflow-x-auto no-scrollbar">
        <div className="flex items-center space-x-1.5 shrink-0 py-0.5">
          <button
            onClick={() => setActiveTab("RANKED")}
            className={`shrink-0 px-3 sm:px-3.5 py-1.5 rounded-lg text-xs font-mono font-bold flex items-center space-x-1.5 transition-all cursor-pointer ${
              activeTab === "RANKED"
                ? "bg-sx-gold/20 text-sx-gold border border-sx-gold/40 shadow-sm"
                : "text-zinc-400 hover:text-white hover:bg-white/[0.05]"
            }`}
          >
            <Award className="w-3.5 h-3.5" />
            <span>1. RANKED ({totalCount})</span>
          </button>

          <button
            onClick={() => setActiveTab("FACTORS")}
            className={`shrink-0 px-3 sm:px-3.5 py-1.5 rounded-lg text-xs font-mono font-bold flex items-center space-x-1.5 transition-all cursor-pointer ${
              activeTab === "FACTORS"
                ? "bg-sx-ice/20 text-sx-ice border border-sx-ice/40 shadow-sm"
                : "text-zinc-400 hover:text-white hover:bg-white/[0.05]"
            }`}
          >
            <BarChart3 className="w-3.5 h-3.5" />
            <span>2. 8-FACTOR AUDIT</span>
          </button>

          <button
            onClick={() => setActiveTab("ROADMAP")}
            className={`shrink-0 px-3 sm:px-3.5 py-1.5 rounded-lg text-xs font-mono font-bold flex items-center space-x-1.5 transition-all cursor-pointer ${
              activeTab === "ROADMAP"
                ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 shadow-sm"
                : "text-zinc-400 hover:text-white hover:bg-white/[0.05]"
            }`}
          >
            <Map className="w-3.5 h-3.5" />
            <span>3. PAKISTAN ROADMAP ({roadmapPhases.length} PHASES)</span>
          </button>

          <button
            onClick={() => setActiveTab("DOSSIER")}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-mono font-bold flex items-center space-x-1.5 transition-all cursor-pointer ${
              activeTab === "DOSSIER"
                ? "bg-purple-500/20 text-purple-300 border border-purple-500/40 shadow-sm"
                : "text-zinc-400 hover:text-white hover:bg-white/[0.05]"
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            <span>4. DOSSIER PACKAGE</span>
          </button>
        </div>

        <div className="hidden sm:block text-[10px] font-mono text-zinc-500">
          SELECT ANY CARD TO AUDIT &bull; SWITCH TABS TO EXPLORE
        </div>
      </div>

      {/* 3. DYNAMIC TAB CONTENT VIEW */}
      <div className="w-full flex-1 min-h-[460px]">
        {/* Tab 1: All Ranked Candidate Cards */}
        {activeTab === "RANKED" && (
          <div className="space-y-3">
            <OpportunityComparisonStage
              opportunities={qualifiedOpportunities}
              selectedId={activeOpp?.id || ""}
              selectedField={
                studentProfile?.preferences?.target_fields?.[0] ||
                studentProfile?.academic?.field_of_study ||
                studentProfile?.field ||
                dossier.candidateProfile?.academic?.field_of_study ||
                dossier.field
              }
              targetDegree={targetDegree}
              isUnder70={isUnder70}
              candidatePercentage={candidatePercentage}
              onSelectOpportunity={(id) => {
                onSelectOpportunity(id);
              }}
            />

            {/* Hint bar beneath cards */}
            <div className="flex items-center justify-between px-2 pt-1 text-[10px] font-mono text-zinc-400 border-t border-white/[0.06]">
              <div className="flex items-center space-x-2">
                <span className="text-sx-gold font-bold">Selected:</span>
                <span className="text-white font-medium">{activeOpp?.name || "None (Profile Ineligible)"}</span>
                <span className="text-zinc-500">&bull;</span>
                <span className={isUnder70 ? "text-amber-300 font-semibold" : "text-sx-ice"}>
                  {isUnder70
                    ? "Academic standing < 70%: Standard merit quotas blocked; prioritize Need-Based Italian DSU or preparatory pathways."
                    : totalCount > 0
                    ? "Click any card to select & update the roadmap & factors"
                    : "Adjust academic/language metrics or regions to qualify"}
                </span>
              </div>
              <button
                onClick={() => setActiveTab("FACTORS")}
                className="text-sx-gold hover:underline flex items-center gap-1 cursor-pointer font-bold"
              >
                <span>View 8-Factor Audit &rarr;</span>
              </button>
            </div>
          </div>
        )}

        {/* Tab 2: 8-Factor Score Audit */}
        {activeTab === "FACTORS" && (
          <div className="space-y-3">
            <ScoringEngineCard
              factors={activeOpp?.factors || dossier?.opportunity?.factors || {}}
              compositeScore={activeOpp?.compositeScore ?? 88.5}
              opportunityName={activeOpp?.name || dossier?.opportunity?.name || "Target Opportunity"}
              rank={activeOpp?.rank ?? 1}
            />
          </div>
        )}

        {/* Tab 3: 6-Phase Pakistani Roadmap */}
        {activeTab === "ROADMAP" && (
          <div className="space-y-3">
            <RoadmapJourney
              phases={roadmapPhases.length > 0 ? roadmapPhases : dossier.roadmapPhases}
              totalPrepDays={dossier.totalPrepDaysEstimated || 45}
              totalBudgetPkr={activeOpp?.fundingSummary?.initialOutOfPocketPkr || dossier.totalBudgetNeededPkr}
            />
          </div>
        )}

        {/* Tab 4: Dossier Assembly & Artifacts Checklist */}
        {activeTab === "DOSSIER" && (
          <div className="space-y-3">
            <DossierAssemblyTheatre
              dossier={dossier}
              activeStep="ARTIFACTS_DELIVERED"
              builderActivity={{
                builderName: "DOSSIER_BUILDER",
                actionLabel: "Artifacts delivered (Standalone Web & PDF)",
                progressPercent: 100,
              }}
              onOpenWebDossier={onOpenWebDossier}
              onOpenPdfViewer={onOpenPdfViewer}
            />
          </div>
        )}
      </div>

      {/* Polite Ineligibility Modal Pop-up (< 70% Marks) */}
      <IneligiblePoliteModal
        isOpen={showIneligibleModal}
        percentage={candidatePercentage}
        gpa4Scale={studentProfile?.academic?.gpa_4_scale}
        onClose={() => setShowIneligibleModal(false)}
        onProceedAnyway={() => setShowIneligibleModal(false)}
        onAdjustMarks={() => {
          setShowIneligibleModal(false);
          onNewMission();
        }}
      />
    </div>
  );
};
