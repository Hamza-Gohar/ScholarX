"use client";

import React, { useState } from "react";
import { useCommandStore } from "@/lib/store";
import { 
  X, 
  ShieldAlert, 
  CheckCircle2, 
  ExternalLink, 
  AlertTriangle, 
  Coins, 
  Calendar, 
  Award, 
  Sparkles, 
  Building2, 
  FileCheck,
  DollarSign,
  MapPin,
  Clock,
  Compass,
  FileText,
  HelpCircle,
  AlertOctagon,
  BookOpen,
  UserCheck,
  ShieldCheck,
  Briefcase
} from "lucide-react";
import { sound } from "@/lib/sound-fx";

type DossierTab = 
  | "OVERVIEW"
  | "FINANCIAL"
  | "ROADMAP"
  | "DOCUMENTS"
  | "TIMELINE"
  | "SELECTION"
  | "OBLIGATIONS"
  | "SOURCES";

export const ScholarshipAuditModal: React.FC = () => {
  const {
    overlayView,
    setOverlayView,
    selectedScholarship,
    candidates,
    setSelectedScholarship,
  } = useCommandStore();

  const [activeTab, setActiveTab] = useState<DossierTab>("OVERVIEW");

  if (overlayView !== "AUDIT") return null;

  const current = selectedScholarship || candidates[0];

  if (!current) {
    return (
      <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-6">
        <div className="command-panel p-6 rounded-lg text-center font-mono text-sm text-white/60 space-y-4">
          <div>No scholarship currently selected for audit.</div>
          <button
            onClick={() => setOverlayView("NONE")}
            className="px-4 py-1.5 rounded bg-cyber-cyan text-obsidian-950 font-bold"
          >
            RETURN TO COMMAND ROOM
          </button>
        </div>
      </div>
    );
  }

  const deep = current.deep_dossier;

  // Pre-seed realistic Skeptic challenges based on scholarship details
  const isFulbright = current.name.toLowerCase().includes("fulbright");
  const isGermany = current.name.toLowerCase().includes("daad");

  return (
    <div className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-6 animate-in fade-in duration-200">
      <div className="relative w-full max-w-6xl h-[90vh] bg-obsidian-900 border border-skeptic-rose/40 rounded-lg shadow-glow-rose flex flex-col overflow-hidden corner-bracket">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-3 bg-obsidian-950 border-b border-white/10 select-none">
          <div className="flex items-center space-x-3">
            <ShieldAlert className="w-5 h-5 text-skeptic-rose" />
            <div>
              <div className="flex items-center space-x-2">
                <h2 className="font-mono text-sm font-bold tracking-wider text-white">
                  SCHOLARSHIP DNA & SKEPTIC ARENA // DEEP VERIFICATION THEATER
                </h2>
                <span className="font-mono text-[9px] px-2 py-0.5 rounded bg-pakistan-deep text-pakistan-emerald font-bold border border-pakistan-emerald/30">
                  {current.status}
                </span>
                {deep && (
                  <span className="font-mono text-[9px] px-2 py-0.5 rounded bg-cyber-cyan/20 text-cyber-cyan font-bold border border-cyber-cyan/40">
                    11-DIMENSION VERIFIED DOSSIER
                  </span>
                )}
              </div>
              <p className="font-mono text-[10px] text-white/40">
                OFFICIAL SOURCE AUDIT • HEC BILATERAL QUOTA • ADVERSARIAL CHALLENGES • ZERO-SCAM REPORT
              </p>
            </div>
          </div>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView("NONE");
            }}
            className="p-1 rounded hover:bg-white/10 text-white/50 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 grid grid-cols-12 gap-4 p-4 overflow-hidden">
          {/* Left Column (3 cols): Discovered Candidates List for Fast Switching */}
          <div className="col-span-3 command-panel rounded border border-white/10 p-3 flex flex-col overflow-hidden">
            <span className="font-mono text-[10px] font-bold text-cyber-cyan tracking-widest block mb-2">
              SCHOLARSHIP COHORT ({candidates.length})
            </span>
            <div className="flex-1 overflow-y-auto space-y-1.5 pr-1">
              {candidates.map((c) => {
                const isSelected = c.scholarship_id === current.scholarship_id;
                const hasDeep = !!c.deep_dossier;
                return (
                  <button
                    key={c.scholarship_id}
                    onClick={() => {
                      sound.playClick();
                      setSelectedScholarship(c);
                    }}
                    className={`w-full text-left p-2 rounded font-mono text-xs border transition-all ${
                      isSelected
                        ? "bg-skeptic-rose/15 border-skeptic-rose text-white shadow-glow-rose"
                        : "bg-obsidian-950 border-white/5 text-white/70 hover:border-white/20 hover:text-white"
                    }`}
                  >
                    <div className="font-bold truncate text-[11px] flex items-center justify-between">
                      <span className="truncate">{c.name}</span>
                      {hasDeep && <span className="w-1.5 h-1.5 rounded-full bg-cyber-cyan ml-1 flex-shrink-0" title="11-Dimension Verified" />}
                    </div>
                    <div className="flex items-center justify-between text-[9px] text-white/40 mt-1">
                      <span>{c.host_country_name}</span>
                      <span className="text-pakistan-emerald font-bold">
                        {c.funding.funding_type}
                      </span>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Right Column (9 cols): Deep Audit View with Tabs */}
          <div className="col-span-9 flex flex-col space-y-3 overflow-hidden">
            {/* Title & Core Details Card */}
            <div className="command-panel p-3.5 rounded border border-white/10 space-y-2.5 flex-shrink-0">
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="font-mono text-base font-bold text-white flex items-center space-x-2">
                    <span>{current.name}</span>
                  </h3>
                  <div className="flex items-center space-x-2 font-mono text-xs text-white/50 mt-0.5">
                    <Building2 className="w-3.5 h-3.5 text-cyber-cyan" />
                    <span>{current.host_institution || current.host_country_name}</span>
                    <span>•</span>
                    <span>{current.academic_intake || "Fall 2026/2027"}</span>
                    {deep && (
                      <>
                        <span>•</span>
                        <span className="text-cyber-cyan">{deep.basic_details.duration_of_scholarship}</span>
                      </>
                    )}
                  </div>
                </div>

                {/* Direct Action Link */}
                <div className="flex items-center space-x-2">
                  {current.source_url && (
                    <a
                      href={current.source_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center space-x-1 px-3 py-1.5 rounded font-mono text-xs font-bold bg-cyber-cyan/20 hover:bg-cyber-cyan/30 text-cyber-cyan border border-cyber-cyan/40 transition-colors"
                    >
                      <span>OFFICIAL PORTAL</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </a>
                  )}
                </div>
              </div>

              {/* Navigation Tabs Bar */}
              <div className="flex items-center space-x-1 overflow-x-auto pt-2 border-t border-white/10 font-mono text-[10px]">
                <button
                  onClick={() => setActiveTab("OVERVIEW")}
                  className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                    activeTab === "OVERVIEW"
                      ? "bg-cyber-cyan text-obsidian-950 font-bold"
                      : "text-white/60 hover:text-white hover:bg-white/5"
                  }`}
                >
                  OVERVIEW & AUDIT
                </button>
                {deep && (
                  <>
                    <button
                      onClick={() => setActiveTab("FINANCIAL")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "FINANCIAL"
                          ? "bg-cyber-cyan text-obsidian-950 font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      FINANCIAL (11 BENEFITS)
                    </button>
                    <button
                      onClick={() => setActiveTab("ROADMAP")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "ROADMAP"
                          ? "bg-cyber-cyan text-obsidian-950 font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      ZERO-TO-SUBMISSION ROADMAP
                    </button>
                    <button
                      onClick={() => setActiveTab("DOCUMENTS")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "DOCUMENTS"
                          ? "bg-cyber-cyan text-obsidian-950 font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      DOCUMENTS CHECKLIST
                    </button>
                    <button
                      onClick={() => setActiveTab("TIMELINE")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "TIMELINE"
                          ? "bg-cyber-cyan text-obsidian-950 font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      DATES & TIMELINE
                    </button>
                    <button
                      onClick={() => setActiveTab("SELECTION")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "SELECTION"
                          ? "bg-cyber-cyan text-obsidian-950 font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      SELECTION & STATS
                    </button>
                    <button
                      onClick={() => setActiveTab("OBLIGATIONS")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "OBLIGATIONS"
                          ? "bg-skeptic-rose text-white font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      OBLIGATIONS & SCAMS
                    </button>
                    <button
                      onClick={() => setActiveTab("SOURCES")}
                      className={`px-2.5 py-1 rounded transition-colors whitespace-nowrap font-bold ${
                        activeTab === "SOURCES"
                          ? "bg-pakistan-emerald text-obsidian-950 font-bold"
                          : "text-white/60 hover:text-white hover:bg-white/5"
                      }`}
                    >
                      SOURCES & MISSING DATA
                    </button>
                  </>
                )}
              </div>
            </div>

            {/* Scrollable Tab Content Area */}
            <div className="flex-1 overflow-y-auto space-y-3 pr-1">
              {/* TAB 1: OVERVIEW */}
              {activeTab === "OVERVIEW" && (
                <div className="space-y-3">
                  {/* Funding & Pakistan Quota Highlight Grid */}
                  <div className="grid grid-cols-3 gap-2.5 font-mono text-xs">
                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5">
                      <span className="text-[10px] text-white/40 block">TUITION & HOUSING</span>
                      <span className="font-bold text-pakistan-emerald">
                        {current.funding.tuition}
                      </span>
                      <span className="text-[10px] text-white/60 block mt-0.5">
                        {current.funding.accommodation}
                      </span>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5">
                      <span className="text-[10px] text-white/40 block">MONTHLY STIPEND</span>
                      <span className="font-bold text-cyber-cyan">
                        {current.funding.monthly_stipend || "Full Living Allowance"}
                      </span>
                      {current.funding.monthly_stipend_pkr_approx && (
                        <span className="text-[10px] text-pakistan-emerald block mt-0.5">
                          ~PKR {(current.funding.monthly_stipend_pkr_approx).toLocaleString()} /mo
                        </span>
                      )}
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5">
                      <span className="text-[10px] text-white/40 block">PAKISTAN BILATERAL QUOTA</span>
                      <span className="font-bold text-warning-amber">
                        {current.pakistan_requirements.pakistan_bilateral_quota
                          ? `YES (${current.pakistan_requirements.pakistan_quota_seats || "Bilateral"} Seats)`
                          : "General International"}
                      </span>
                      <span className="text-[10px] text-white/60 block mt-0.5">
                        {current.pakistan_requirements.hec_managed ? "Routed via HEC Portal" : "Direct University Portal"}
                      </span>
                    </div>
                  </div>

                  {/* 15-Dimension Eligibility Check Matrix */}
                  <div className="command-panel p-3.5 rounded border border-white/10 space-y-2.5">
                    <span className="font-mono text-xs font-bold text-cyber-cyan tracking-wider flex items-center space-x-1.5">
                      <FileCheck className="w-4 h-4 text-cyber-cyan" />
                      <span>15-DIMENSION ELIGIBILITY VERIFICATION</span>
                    </span>

                    <div className="grid grid-cols-2 gap-2 font-mono text-xs">
                      <div className="flex items-center space-x-2 p-2 rounded bg-obsidian-950 border border-white/5">
                        <CheckCircle2 className="w-4 h-4 text-pakistan-emerald flex-shrink-0" />
                        <div>
                          <span className="text-white/80 block">Degree Level: {current.eligibility.degree_levels.join(", ")}</span>
                          <span className="text-[9px] text-white/40">16-year BS / 18-year MS verified</span>
                        </div>
                      </div>

                      <div className="flex items-center space-x-2 p-2 rounded bg-obsidian-950 border border-white/5">
                        <CheckCircle2 className="w-4 h-4 text-pakistan-emerald flex-shrink-0" />
                        <div>
                          <span className="text-white/80 block">GPA Cutoff: {current.eligibility.min_gpa_percentage || 60}% Marks</span>
                          <span className="text-[9px] text-white/40">Pakistani grading conversion verified</span>
                        </div>
                      </div>

                      <div className="flex items-center space-x-2 p-2 rounded bg-obsidian-950 border border-white/5">
                        <CheckCircle2 className="w-4 h-4 text-pakistan-emerald flex-shrink-0" />
                        <div>
                          <span className="text-white/80 block">
                            {current.language.english_test_required
                              ? `IELTS ${current.language.minimum_ielts || 6.5} Required`
                              : "MOI Certificate Accepted"}
                          </span>
                          <span className="text-[9px] text-white/40">English proficiency verified</span>
                        </div>
                      </div>

                      <div className="flex items-center space-x-2 p-2 rounded bg-obsidian-950 border border-white/5">
                        <CheckCircle2 className="w-4 h-4 text-pakistan-emerald flex-shrink-0" />
                        <div>
                          <span className="text-white/80 block">
                            {current.pakistan_requirements.hec_attestation_required
                              ? "HEC & IBCC Attestation Required"
                              : "Standard Transcripts Accepted"}
                          </span>
                          <span className="text-[9px] text-white/40">Document readiness verified</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Polite Ineligibility & Need-Based Alternatives Feedback */}
                  {(current.polite_rejection_notice || (current.need_based_alternatives && current.need_based_alternatives.length > 0)) && (
                    <div className="command-panel p-3.5 rounded border border-warning-amber/40 bg-warning-amber/10 space-y-2">
                      <span className="font-mono text-xs font-bold text-warning-amber tracking-wider flex items-center space-x-1.5">
                        <AlertOctagon className="w-4 h-4 text-warning-amber" />
                        <span>ACADEMIC ELIGIBILITY GUIDANCE & NEED-BASED ALTERNATIVES</span>
                      </span>
                      {current.polite_rejection_notice && (
                        <p className="text-white/80 text-xs font-mono leading-relaxed">
                          {current.polite_rejection_notice}
                        </p>
                      )}
                      {current.need_based_alternatives && current.need_based_alternatives.length > 0 && (
                        <div className="pt-1.5 border-t border-warning-amber/20 space-y-1">
                          <span className="text-[10px] font-mono text-pakistan-emerald font-bold tracking-wider block">
                            RECOMMENDED ALTERNATIVE PATHWAYS & NEED-BASED GRANTS:
                          </span>
                          <ul className="list-disc list-inside text-[11px] font-mono text-white/70 space-y-1">
                            {current.need_based_alternatives.map((alt, idx) => (
                              <li key={idx}>{alt}</li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </div>
                  )}

                  {/* Skeptic Agent Adversarial Challenges */}
                  <div className="command-panel p-3.5 rounded border border-skeptic-rose/30 space-y-2">
                    <span className="font-mono text-xs font-bold text-skeptic-rose tracking-wider flex items-center space-x-1.5">
                      <AlertTriangle className="w-4 h-4 text-skeptic-rose" />
                      <span>SKEPTIC AGENT ADVERSARIAL CHALLENGES & RISKS</span>
                    </span>

                    <div className="space-y-2 font-mono text-xs">
                      {isFulbright && (
                        <div className="p-2.5 rounded bg-skeptic-rose/10 border border-skeptic-rose/30 space-y-1">
                          <div className="flex items-center justify-between text-skeptic-rose font-bold">
                            <span>J-1 VISA 2-YEAR HOME RESIDENCY REQUIREMENT</span>
                            <span className="text-[9px] px-1.5 py-0.5 rounded bg-skeptic-rose text-white">HIGH SEVERITY</span>
                          </div>
                          <p className="text-white/70 text-[11px]">
                            Students cannot transition to H-1B or US permanent residency immediately after graduation; must return to Pakistan for 2 years.
                          </p>
                        </div>
                      )}

                      {isGermany && (
                        <div className="p-2.5 rounded bg-skeptic-rose/10 border border-skeptic-rose/30 space-y-1">
                          <div className="flex items-center justify-between text-skeptic-rose font-bold">
                            <span>MANDATORY 2-YEAR POST-GRADUATION WORK EXPERIENCE</span>
                            <span className="text-[9px] px-1.5 py-0.5 rounded bg-warning-amber text-obsidian-950">STRICT CRITERIA</span>
                          </div>
                          <p className="text-white/70 text-[11px]">
                            DAAD EPOS strictly requires 2 full years of professional experience acquired AFTER completing your bachelor degree.
                          </p>
                        </div>
                      )}

                      <div className="p-2 rounded bg-obsidian-950 border border-white/5 space-y-1">
                        <div className="flex items-center justify-between text-warning-amber font-bold text-[11px]">
                          <span>DOCUMENT ATTESTATION TIMELINE (HEC / MOFA)</span>
                          <span className="text-[9px] px-1.5 py-0.5 rounded bg-warning-amber/20 text-warning-amber">STANDARD LEAD TIME</span>
                        </div>
                        <p className="text-white/70 text-[11px]">
                          HEC degree attestation and MOFA courier in Pakistan takes 2-4 weeks during peak admissions.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 2: FINANCIAL BREAKDOWN */}
              {activeTab === "FINANCIAL" && deep && (
                <div className="command-panel p-4 rounded border border-white/10 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-cyber-cyan text-sm flex items-center space-x-2">
                      <Coins className="w-4 h-4 text-cyber-cyan" />
                      <span>EXHAUSTIVE FINANCIAL COVERAGE BREAKDOWN</span>
                    </span>
                    {deep.financial_coverage_breakdown.total_estimated_value_usd_per_year && (
                      <span className="text-pakistan-emerald font-bold text-xs px-2 py-0.5 rounded bg-pakistan-deep border border-pakistan-emerald/30">
                        ESTIMATED VALUE: ~${deep.financial_coverage_breakdown.total_estimated_value_usd_per_year.toLocaleString()} USD / YEAR
                      </span>
                    )}
                  </div>

                  <div className="grid grid-cols-2 gap-2.5">
                    {Object.entries(deep.financial_coverage_breakdown).map(([key, item]) => {
                      if (key === "total_estimated_value_usd_per_year" || typeof item !== "object" || !item) return null;
                      const benefit = item as any;
                      const isCovered = benefit.status.includes("COVERED") || benefit.status.includes("FREE") || benefit.status.includes("WAIVED") || benefit.status.includes("REIMBURSED");
                      return (
                        <div key={key} className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                          <div className="flex items-center justify-between">
                            <span className="text-[10px] text-white/50 uppercase font-bold tracking-wider">
                              {key.replace(/_/g, " ")}
                            </span>
                            <span className={`text-[9px] px-1.5 py-0.5 rounded font-bold ${
                              isCovered
                                ? "bg-pakistan-emerald/20 text-pakistan-emerald border border-pakistan-emerald/30"
                                : "bg-skeptic-rose/20 text-skeptic-rose border border-skeptic-rose/30"
                            }`}>
                              {benefit.status}
                            </span>
                          </div>
                          <p className="text-white/80 text-[11px] leading-relaxed">
                            {benefit.details}
                          </p>
                          {benefit.amount && (
                            <span className="text-cyber-cyan font-bold text-[10px] block mt-1">
                              Allowance: {benefit.amount}
                            </span>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}

              {/* TAB 3: ROADMAP */}
              {activeTab === "ROADMAP" && deep && (
                <div className="command-panel p-4 rounded border border-white/10 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-cyber-cyan text-sm flex items-center space-x-2">
                      <Compass className="w-4 h-4 text-cyber-cyan" />
                      <span>APPLICATION ROADMAP (ZERO TO SUBMISSION)</span>
                    </span>
                    <span className="text-white/50 text-[10px]">
                      Portal: {deep.application_process_roadmap.portal_system_name}
                    </span>
                  </div>

                  {/* Submission routing info */}
                  <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                    <span className="text-warning-amber font-bold text-[10px] block">ROUTING ARCHITECTURE</span>
                    <p className="text-white/80 text-[11px]">
                      {deep.application_process_roadmap.university_vs_scholarship_routing}
                    </p>
                  </div>

                  {/* Step by step workflow */}
                  <div className="space-y-1.5 pt-1">
                    <span className="text-[10px] font-bold text-cyber-cyan tracking-wider block">CHRONOLOGICAL STEP-BY-STEP WORKFLOW</span>
                    <div className="space-y-1.5">
                      {deep.application_process_roadmap.step_by_step_workflow.map((step, idx) => (
                        <div key={idx} className="flex items-start space-x-2.5 p-2 rounded bg-obsidian-950 border border-white/5 text-[11px]">
                          <span className="px-1.5 py-0.5 rounded bg-cyber-cyan/20 text-cyber-cyan font-bold text-[9px] flex-shrink-0">
                            STEP {idx + 1}
                          </span>
                          <span className="text-white/80 leading-relaxed">{step}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Esssays & Interview details */}
                  <div className="grid grid-cols-2 gap-2.5 pt-2 border-t border-white/5">
                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                      <span className="text-[10px] text-white/40 block font-bold">PERSONAL STATEMENT & ESSAYS</span>
                      <p className="text-white/80 text-[11px] leading-relaxed">
                        {deep.application_process_roadmap.personal_statement_prompts}
                      </p>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                      <span className="text-[10px] text-white/40 block font-bold">INTERVIEW & SELECTION TEST</span>
                      <p className="text-white/80 text-[11px] leading-relaxed">
                        {deep.application_process_roadmap.interviews_conducted
                          ? `Conducted: ${deep.application_process_roadmap.interview_format_details}`
                          : "No interview conducted; 100% paper/dossier evaluation."}
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 4: DOCUMENTS */}
              {activeTab === "DOCUMENTS" && deep && (
                <div className="command-panel p-4 rounded border border-white/10 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-cyber-cyan text-sm flex items-center space-x-2">
                      <FileText className="w-4 h-4 text-cyber-cyan" />
                      <span>REQUIRED DOCUMENTS CHECKLIST</span>
                    </span>
                    <span className="text-white/50 text-[10px]">
                      {deep.required_documents_checklist.length} Documents Required
                    </span>
                  </div>

                  <div className="space-y-2">
                    {deep.required_documents_checklist.map((doc, idx) => (
                      <div key={idx} className="p-2.5 rounded bg-obsidian-950 border border-white/5 flex items-start justify-between space-x-3">
                        <div className="space-y-1 flex-1">
                          <div className="flex items-center space-x-2">
                            <span className="font-bold text-white text-[12px]">{doc.document_name}</span>
                            <span className={`text-[9px] px-1.5 py-0.2 rounded font-bold ${
                              doc.mandatory
                                ? "bg-skeptic-rose/20 text-skeptic-rose border border-skeptic-rose/30"
                                : "bg-white/10 text-white/60"
                            }`}>
                              {doc.mandatory ? "MANDATORY" : "OPTIONAL / CONDITIONAL"}
                            </span>
                          </div>
                          <p className="text-white/70 text-[11px]">
                            {doc.specification}
                          </p>
                          <div className="text-[10px] text-pakistan-emerald flex items-center space-x-1">
                            <span className="font-bold">Pakistan Specific:</span>
                            <span>{doc.pakistan_specific_instruction}</span>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* TAB 5: TIMELINE */}
              {activeTab === "TIMELINE" && deep && (
                <div className="command-panel p-4 rounded border border-white/10 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-cyber-cyan text-sm flex items-center space-x-2">
                      <Calendar className="w-4 h-4 text-cyber-cyan" />
                      <span>ANNUAL CYCLE DATES & TIMELINE</span>
                    </span>
                  </div>

                  <div className="grid grid-cols-2 gap-2.5">
                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-0.5">
                      <span className="text-[10px] text-white/40 block font-bold">APPLICATION OPEN</span>
                      <span className="text-white font-bold text-xs">{deep.important_dates_timeline.application_open_date}</span>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-skeptic-rose/30 space-y-0.5">
                      <span className="text-[10px] text-skeptic-rose block font-bold">APPLICATION DEADLINE</span>
                      <span className="text-skeptic-rose font-bold text-xs">{deep.important_dates_timeline.application_deadline}</span>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-0.5">
                      <span className="text-[10px] text-white/40 block font-bold">INTERVIEW PERIOD</span>
                      <span className="text-white font-bold text-xs">{deep.important_dates_timeline.interview_period || "N/A"}</span>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-0.5">
                      <span className="text-[10px] text-white/40 block font-bold">SHORTLIST / RESULTS</span>
                      <span className="text-cyber-cyan font-bold text-xs">{deep.important_dates_timeline.shortlist_announcement || "Standard notification"}</span>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-0.5">
                      <span className="text-[10px] text-white/40 block font-bold">VISA APPLICATION WINDOW</span>
                      <span className="text-white font-bold text-xs">{deep.important_dates_timeline.visa_application_window || "Summer before intake"}</span>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-0.5">
                      <span className="text-[10px] text-white/40 block font-bold">SEMESTER COMMENCES</span>
                      <span className="text-pakistan-emerald font-bold text-xs">{deep.important_dates_timeline.semester_commencement || "Fall session"}</span>
                    </div>
                  </div>

                  <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                    <span className="text-[10px] font-bold text-warning-amber block">ANNUAL CYCLE STRATEGIC NOTES</span>
                    <p className="text-white/80 text-[11px] leading-relaxed">
                      {deep.important_dates_timeline.annual_cycle_notes}
                    </p>
                  </div>
                </div>
              )}

              {/* TAB 6: SELECTION & STATS */}
              {activeTab === "SELECTION" && deep && (
                <div className="command-panel p-4 rounded border border-white/10 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-cyber-cyan text-sm flex items-center space-x-2">
                      <Award className="w-4 h-4 text-cyber-cyan" />
                      <span>SELECTION RUBRIC & COMPETITIVENESS PROFILE</span>
                    </span>
                    <span className={`px-2 py-0.5 rounded font-bold text-[9px] ${
                      deep.competitiveness_profile.competitiveness_tier === "EXTREME"
                        ? "bg-skeptic-rose/20 text-skeptic-rose border border-skeptic-rose/30"
                        : "bg-warning-amber/20 text-warning-amber border border-warning-amber/30"
                    }`}>
                      TIER: {deep.competitiveness_profile.competitiveness_tier}
                    </span>
                  </div>

                  <div className="grid grid-cols-2 gap-3">
                    {/* Left: Weights */}
                    <div className="space-y-2">
                      <span className="text-[10px] font-bold text-cyber-cyan uppercase block">Evaluation Weights & Priority</span>
                      <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1.5 text-[11px]">
                        <div><span className="text-white/50">Academic Merit:</span> <span className="text-white font-bold">{deep.selection_process_and_weights.academic_weight}</span></div>
                        <div><span className="text-white/50">Leadership & Civic:</span> <span className="text-white font-bold">{deep.selection_process_and_weights.extracurricular_and_leadership_weight}</span></div>
                        <div><span className="text-white/50">Research Quality:</span> <span className="text-white font-bold">{deep.selection_process_and_weights.research_experience_weight}</span></div>
                        <div><span className="text-white/50">Work Experience:</span> <span className="text-white font-bold">{deep.selection_process_and_weights.work_experience_weight}</span></div>
                        <div><span className="text-white/50">Personal Statement:</span> <span className="text-white font-bold">{deep.selection_process_and_weights.personal_statement_weight}</span></div>
                        <div><span className="text-white/50">Interview Weight:</span> <span className="text-white font-bold">{deep.selection_process_and_weights.interview_weight}</span></div>
                        <div className="pt-1 border-t border-white/5 text-[10px] text-white/70">
                          <span className="text-white/50 block">Panel:</span> {deep.selection_process_and_weights.selection_panel_composition}
                        </div>
                      </div>
                    </div>

                    {/* Right: Competitiveness */}
                    <div className="space-y-2">
                      <span className="text-[10px] font-bold text-pakistan-emerald uppercase block">Admission Statistics & Acceptance</span>
                      <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1.5 text-[11px]">
                        <div><span className="text-white/50">Total Applicants:</span> <span className="text-white font-bold">{deep.competitiveness_profile.total_annual_applicants}</span></div>
                        <div><span className="text-white/50">Total Awards:</span> <span className="text-white font-bold">{deep.competitiveness_profile.total_scholarships_awarded}</span></div>
                        <div><span className="text-white/50">Acceptance Rate (PK):</span> <span className="text-pakistan-emerald font-bold">{deep.competitiveness_profile.acceptance_rate_pakistan}</span></div>
                        <div><span className="text-white/50">Typical GPA:</span> <span className="text-cyber-cyan font-bold">{deep.competitiveness_profile.typical_successful_applicant_gpa}</span></div>
                        <div className="pt-1 border-t border-white/5 text-[10px] text-white/70">
                          <span className="text-white/50 block">Common Winner Backgrounds:</span> {deep.competitiveness_profile.common_backgrounds_of_winners}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 7: OBLIGATIONS & WARNINGS */}
              {activeTab === "OBLIGATIONS" && deep && (
                <div className="command-panel p-4 rounded border border-skeptic-rose/30 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-skeptic-rose text-sm flex items-center space-x-2">
                      <AlertOctagon className="w-4 h-4 text-skeptic-rose" />
                      <span>SCHOLARSHIP OBLIGATIONS & RED FLAG WARNINGS</span>
                    </span>
                  </div>

                  {/* Red flags & Scam warnings */}
                  <div className="p-3 rounded bg-skeptic-rose/10 border border-skeptic-rose/30 space-y-2">
                    <span className="font-bold text-skeptic-rose text-[11px] block flex items-center space-x-1.5">
                      <AlertTriangle className="w-4 h-4 text-skeptic-rose" />
                      <span>VERIFIED SCAM WARNINGS & AGENT ALERTS</span>
                    </span>
                    <ul className="list-disc list-inside space-y-1 text-white/80 text-[11px]">
                      {deep.red_flags_and_warnings.fake_websites_and_scams.map((scam, idx) => (
                        <li key={idx}>{scam}</li>
                      ))}
                    </ul>
                    <div className="text-[10px] text-warning-amber pt-1">
                      {deep.red_flags_and_warnings.application_fee_warning}
                    </div>
                  </div>

                  {/* Hidden costs */}
                  <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1.5">
                    <span className="text-[10px] font-bold text-warning-amber block">ITEMIZED REALISTIC OUT-OF-POCKET EXPENSES</span>
                    <ul className="list-disc list-inside space-y-1 text-white/70 text-[11px]">
                      {deep.red_flags_and_warnings.hidden_costs_breakdown.map((cost, idx) => (
                        <li key={idx}>{cost}</li>
                      ))}
                    </ul>
                  </div>

                  {/* Post-Award Obligations */}
                  <div className="grid grid-cols-2 gap-2.5 pt-1">
                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                      <span className="text-[10px] text-white/40 block font-bold">HOME COUNTRY RETURN OBLIGATION</span>
                      <p className="text-white/80 text-[11px]">
                        {deep.scholarship_obligations_and_terms.home_country_return_obligation}
                      </p>
                    </div>

                    <div className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1">
                      <span className="text-[10px] text-white/40 block font-bold">WORK RESTRICTIONS DURING STUDY</span>
                      <p className="text-white/80 text-[11px]">
                        {deep.scholarship_obligations_and_terms.work_restrictions_during_study}
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 8: SOURCES & MISSING DATA */}
              {activeTab === "SOURCES" && deep && (
                <div className="command-panel p-4 rounded border border-pakistan-emerald/30 space-y-3 font-mono text-xs">
                  <div className="flex items-center justify-between pb-2 border-b border-white/10">
                    <span className="font-bold text-pakistan-emerald text-sm flex items-center space-x-2">
                      <ShieldCheck className="w-4 h-4 text-pakistan-emerald" />
                      <span>OFFICIAL SOURCES & TRANSPARENCY AUDIT</span>
                    </span>
                  </div>

                  {/* Official Sources List */}
                  <div className="space-y-2">
                    <span className="text-[10px] font-bold text-cyber-cyan uppercase block">Verified Primary Official Sources</span>
                    {deep.official_sources_verified.map((src, idx) => (
                      <div key={idx} className="p-2.5 rounded bg-obsidian-950 border border-white/5 space-y-1.5">
                        <div className="flex items-center justify-between">
                          <span className="font-bold text-white text-[11px]">{src.source_name}</span>
                          <span className="text-[9px] px-1.5 py-0.5 rounded bg-pakistan-deep text-pakistan-emerald font-bold border border-pakistan-emerald/30">
                            {src.source_type}
                          </span>
                        </div>
                        <a
                          href={src.source_url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-cyber-cyan hover:underline text-[10px] flex items-center space-x-1"
                        >
                          <span className="truncate">{src.source_url}</span>
                          <ExternalLink className="w-3 h-3 flex-shrink-0" />
                        </a>

                        {/* Missing or unpublished data points */}
                        {src.data_points_missing_or_unpublished_by_source && src.data_points_missing_or_unpublished_by_source.length > 0 && (
                          <div className="mt-2 p-2 rounded bg-warning-amber/10 border border-warning-amber/20 space-y-1">
                            <span className="text-warning-amber font-bold text-[9px] block">
                              DATA MISSING OR UNPUBLISHED BY OFFICIAL PORTAL:
                            </span>
                            <ul className="list-disc list-inside space-y-0.5 text-white/70 text-[10px]">
                              {src.data_points_missing_or_unpublished_by_source.map((item, iIdx) => (
                                <li key={iIdx}>{item}</li>
                              ))}
                            </ul>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
