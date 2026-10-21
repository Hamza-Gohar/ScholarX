"use client";

import React from "react";
import { motion } from "framer-motion";
import { CanonicalDossier, CanonicalDossierSection } from "@/lib/ranking/types";
import { 
  FileText, 
  CheckCircle2, 
  Globe, 
  Printer, 
  Download,
  ArrowUpRight, 
  Sparkles, 
  Cpu, 
  Layers, 
  ShieldCheck,
  ExternalLink
} from "lucide-react";
import { sound } from "@/lib/sound-fx";

export interface DossierAssemblyTheatreProps {
  dossier: CanonicalDossier;
  activeStep: string;
  builderActivity?: {
    builderName: "WEB_BUILDER" | "PDF_BUILDER" | "DOSSIER_BUILDER";
    actionLabel: string;
    progressPercent: number;
  };
  onOpenWebDossier: () => void;
  onOpenPdfViewer: () => void;
  className?: string;
}

export const DossierAssemblyTheatre: React.FC<DossierAssemblyTheatreProps> = ({
  dossier,
  activeStep,
  builderActivity,
  onOpenWebDossier,
  onOpenPdfViewer,
  className = "",
}) => {
  const isComplete = activeStep === "ARTIFACTS_DELIVERED";
  const isWebActive = activeStep === "WEB_BUILDER_ACTIVE" || isComplete;
  const isPdfActive = activeStep === "PDF_BUILDER_ACTIVE" || isComplete;

  const handleDownloadDossier = () => {
    sound.playClick();
    const sid = dossier.opportunity?.id || dossier.scholarshipId || "primary";
    const candidateName = dossier.candidateProfile?.name || "Hamza_Gohar";
    const cleanName = candidateName.replace(/[^a-zA-Z0-9_-]/g, "_");
    const downloadUrl = `/api/download/pdf?id=${encodeURIComponent(sid)}&name=${encodeURIComponent(cleanName)}`;
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = `ScholarX_Intelligence_Dossier_${cleanName}.pdf`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div
      className={`w-full max-w-[1240px] mx-auto rounded-xl border border-white/[0.12] bg-black/85 backdrop-blur-xl p-4 shadow-2xl transition-all duration-300 pointer-events-auto ${className}`}
    >
      {/* Top Header */}
      <div className="flex items-center justify-between border-b border-white/[0.08] pb-3 mb-3">
        <div className="flex items-center space-x-2.5">
          <div className="w-7 h-7 rounded-lg bg-sx-ice/20 border border-sx-ice/40 flex items-center justify-center text-sx-ice shadow-[0_0_12px_rgba(56,189,248,0.25)]">
            <Layers className="w-4 h-4" />
          </div>
          <div>
            <div className="text-[10px] font-mono text-sx-text-tertiary uppercase tracking-wider flex items-center gap-1.5">
              <span>AUTONOMOUS DOSSIER ASSEMBLY</span>
              <span className="text-white/20">{"//"}</span>
              <span className="text-sx-ice font-semibold">CANONICAL INTELLIGENCE PACKAGE</span>
            </div>
            <div className="text-sm font-sans font-semibold text-white">
              {dossier.title}
            </div>
          </div>
        </div>

        {/* Lifecycle Status */}
        <div className="flex items-center space-x-2">
          <div className="text-right text-[10px] font-mono">
            <span className="text-sx-text-tertiary block">PACKAGE STATE:</span>
            <span className={`font-bold ${isComplete ? "text-sx-verified" : "text-sx-gold"}`}>
              {isComplete ? "MISSION COMPLETE // READY" : "COMPOSING ARTIFACTS"}
            </span>
          </div>
        </div>
      </div>

      {/* Main Grid: Left = 10 Section Checklist; Right = Builder Entities & Deliverables */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-3.5 mb-3">
        {/* Left Column (7 cols): 10 Streaming Canonical Sections (§23) */}
        <div className="md:col-span-7 bg-white/[0.02] border border-white/[0.06] rounded-xl p-3">
          <div className="text-[10px] font-mono text-sx-text-tertiary uppercase tracking-wider mb-2 flex items-center justify-between">
            <span>CANONICAL DOSSIER SECTIONS (DERIVED FROM PHASES 5 & 6)</span>
            <span className="text-sx-verified font-bold">
              {dossier.sections.filter((s) => s.status === "COMPLETE").length} / {dossier.sections.length} VERIFIED
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
            {dossier.sections.map((sec, idx) => {
              const isChecked = sec.status === "COMPLETE";

              return (
                <div
                  key={sec.id}
                  className={`rounded-lg p-2 border transition-all text-xs flex items-start space-x-2 ${
                    isChecked
                      ? "bg-black/60 border-white/[0.08]"
                      : "bg-black/30 border-white/[0.04] opacity-50"
                  }`}
                >
                  <div className="mt-0.5 shrink-0">
                    {isChecked ? (
                      <CheckCircle2 className="w-3.5 h-3.5 text-sx-verified" />
                    ) : (
                      <div className="w-3.5 h-3.5 rounded-full border border-white/20 animate-spin border-t-sx-ice" />
                    )}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="text-[11px] font-sans font-semibold text-white/95 truncate">
                      {sec.title}
                    </div>
                    <div className="text-[9px] font-mono text-sx-text-tertiary truncate">
                      {sec.summary}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Right Column (5 cols): Active Builder Processes & Final Artifact Hand-offs (§35, §36, §40, §41) */}
        <div className="md:col-span-5 flex flex-col justify-between space-y-2.5">
          {/* Active Builder Status Card */}
          {builderActivity && !isComplete && (
            <div className="bg-black/60 border border-sx-ice/40 rounded-xl p-3 text-xs font-mono shadow-[0_0_20px_rgba(56,189,248,0.12)]">
              <div className="flex items-center space-x-2 text-sx-ice font-bold uppercase mb-1.5">
                <Cpu className="w-3.5 h-3.5 animate-spin" />
                <span>{builderActivity.builderName} ACTIVE</span>
              </div>
              <div className="text-white/80 text-[11px] font-sans mb-2">
                {builderActivity.actionLabel}
              </div>
              <div className="w-full h-1.5 bg-white/[0.08] rounded-full overflow-hidden">
                <div
                  className="h-full bg-sx-ice rounded-full transition-all duration-300"
                  style={{ width: `${builderActivity.progressPercent}%` }}
                />
              </div>
            </div>
          )}

          {/* Generated Artifacts Access Cards */}
          <div className="grid grid-cols-2 gap-2">
            {/* Artifact 1: Standalone Editorial Web Page */}
            <div
              className={`rounded-xl p-3 border transition-all ${
                isWebActive
                  ? "bg-white/[0.04] border-sx-flow/50 shadow-[0_0_15px_rgba(56,189,248,0.15)]"
                  : "bg-black/40 border-white/[0.06] opacity-50"
              }`}
            >
              <div className="flex items-center justify-between mb-1.5">
                <div className="w-6 h-6 rounded-lg bg-sx-flow/20 text-sx-flow flex items-center justify-center">
                  <Globe className="w-3.5 h-3.5" />
                </div>
                <span
                  className={`text-[9px] font-mono px-1.5 py-0.2 rounded font-bold ${
                    isWebActive ? "bg-sx-verified/20 text-sx-verified" : "bg-white/[0.06] text-white/40"
                  }`}
                >
                  {isWebActive ? "READY" : "PENDING"}
                </span>
              </div>
              <div className="text-xs font-sans font-bold text-white mb-0.5">
                Editorial Web Dossier
              </div>
              <div className="text-[9px] font-mono text-sx-text-tertiary mb-2.5">
                Clean CSS intelligence page
              </div>
              <button
                disabled={!isWebActive}
                onClick={onOpenWebDossier}
                className="w-full py-1.5 rounded-lg bg-sx-ice/20 border border-sx-ice/50 text-sx-ice hover:bg-sx-ice/30 text-[10px] font-mono font-bold tracking-wider flex items-center justify-center space-x-1 transition-all disabled:opacity-30 disabled:pointer-events-none"
              >
                <span>OPEN DOSSIER</span>
                <ArrowUpRight className="w-3 h-3" />
              </button>
            </div>

            {/* Artifact 2: Printable PDF Publication */}
            <div
              className={`rounded-xl p-3 border transition-all ${
                isPdfActive
                  ? "bg-white/[0.04] border-sx-gold/50 shadow-[0_0_15px_rgba(212,175,55,0.15)]"
                  : "bg-black/40 border-white/[0.06] opacity-50"
              }`}
            >
              <div className="flex items-center justify-between mb-1.5">
                <div className="w-6 h-6 rounded-lg bg-sx-gold/20 text-sx-gold flex items-center justify-center">
                  <Printer className="w-3.5 h-3.5" />
                </div>
                <span
                  className={`text-[9px] font-mono px-1.5 py-0.2 rounded font-bold ${
                    isPdfActive ? "bg-sx-verified/20 text-sx-verified" : "bg-white/[0.06] text-white/40"
                  }`}
                >
                  {isPdfActive ? "READY" : "PENDING"}
                </span>
              </div>
              <div className="text-xs font-sans font-bold text-white mb-0.5">
                Printable PDF Dossier
              </div>
              <div className="text-[9px] font-mono text-sx-text-tertiary mb-2.5">
                Paginated A4 student publication
              </div>
              <div className="flex flex-col gap-1.5">
                <button
                  disabled={!isPdfActive}
                  onClick={handleDownloadDossier}
                  className={`w-full py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-[10px] font-mono font-bold tracking-wider flex items-center justify-center space-x-1 transition-all shadow-md ${
                    !isPdfActive ? "opacity-30 pointer-events-none" : "cursor-pointer"
                  }`}
                >
                  <Download className="w-3 h-3 stroke-[2.5]" />
                  <span>DOWNLOAD DOSSIER</span>
                </button>
              </div>
            </div>
          </div>

          {/* Calm Mission Complete Status (§41, §67) */}
          {isComplete && (
            <div className="rounded-xl bg-white/[0.02] border border-white/[0.08] p-2.5 text-[10px] font-mono text-sx-text-secondary flex items-center justify-between">
              <div className="flex items-center space-x-2 text-sx-verified font-bold">
                <CheckCircle2 className="w-4 h-4" />
                <span>MISSION COMPLETE</span>
              </div>
              <div className="text-white/60">
                1 CANONICAL STATE // DUAL ARTIFACT OUTPUT
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Footer Audit Quote */}
      <div className="flex items-center justify-between text-[9px] font-mono text-sx-text-tertiary border-t border-white/[0.06] pt-2">
        <span>ARTIFACT INTEGRITY: Driven from canonical dataset; Web & PDF tell the identical story.</span>
        <span>STANDALONE URL: /dossier/{dossier.opportunity?.id || "primary"}</span>
      </div>
    </div>
  );
};
