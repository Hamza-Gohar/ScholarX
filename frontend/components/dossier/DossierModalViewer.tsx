"use client";

import React, { useState, useEffect } from "react";
import { createPortal } from "react-dom";
import { motion, AnimatePresence } from "framer-motion";
import { CanonicalDossier } from "@/lib/ranking/types";
import { WebDossierView } from "./WebDossierView";
import { X, Printer, Globe, ExternalLink, Download, FileCheck } from "lucide-react";
import { sound } from "@/lib/sound-fx";

export interface DossierModalViewerProps {
  dossier: CanonicalDossier;
  isOpen: boolean;
  onClose: () => void;
  initialTab?: "WEB" | "PDF";
}

export const DossierModalViewer: React.FC<DossierModalViewerProps> = ({
  dossier,
  isOpen,
  onClose,
  initialTab = "WEB",
}) => {
  const [mounted, setMounted] = useState(false);
  const [activeTab, setActiveTab] = useState<"WEB" | "PDF">(initialTab);

  useEffect(() => {
    setMounted(true);
  }, []);

  // Synchronize activeTab when initialTab prop updates
  useEffect(() => {
    setActiveTab(initialTab);
  }, [initialTab]);

  // Lock background body scroll while modal is active
  useEffect(() => {
    if (isOpen && mounted) {
      const prev = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      return () => {
        document.body.style.overflow = prev;
      };
    }
  }, [isOpen, mounted]);

  // Keyboard shortcut listener for Escape key
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
      }
    };
    if (isOpen) {
      window.addEventListener("keydown", handleKeyDown);
    }
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  const scholarshipId = dossier?.opportunity?.id || dossier?.scholarshipId || "opportunity";

  // Native Vector Print & PDF Download: Invokes browser's print engine which produces
  // the exact 11-dimension dossier with pristine vector graphics, styled cards, and zero void.
  const handleDownloadDossier = () => {
    sound.playClick();
    if (typeof window !== "undefined") {
      window.print();
    }
  };

  if (!mounted) return null;

  return createPortal(
    <AnimatePresence>
      {isOpen && (
        <div
          className="fixed inset-0 z-[1000] flex items-center justify-center p-0 sm:p-4 md:p-6 bg-black/85 backdrop-blur-xl dossier-modal-backdrop"
          onClick={(e) => {
            if (e.target === e.currentTarget) {
              onClose();
            }
          }}
        >
          <motion.div
            initial={{ opacity: 0, scale: 0.98, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.98, y: 10 }}
            transition={{ duration: 0.16 }}
            className="relative w-full max-w-[1140px] h-full sm:h-[93vh] max-h-[100dvh] sm:max-h-[93vh] bg-[#FAFAF9] rounded-none sm:rounded-2xl shadow-2xl flex flex-col min-h-0 overflow-hidden border-0 sm:border sm:border-white/20 z-[1001] select-text dossier-modal-window"
          >
            {/* Top Modal Header */}
            <div className="bg-[#1C1917] text-white px-3 sm:px-6 py-2.5 sm:py-3 flex flex-wrap items-center justify-between shrink-0 border-b border-white/10 z-[1002] gap-2 no-print">
              <div className="flex items-center space-x-2 sm:space-x-3 min-w-0">
                <span className="text-[10px] sm:text-xs font-bold px-2 py-0.5 rounded bg-sx-ice/20 text-sx-ice border border-sx-ice/40 font-sans shrink-0">
                  SCHOLARX
                </span>
                <span className="text-xs text-white/70 font-sans truncate max-w-[140px] xs:max-w-[200px] sm:max-w-none">
                  {dossier?.opportunity?.shortName || "Dossier"} • {dossier?.version || "Cohort 2026/27"}
                </span>
              </div>

              {/* Middle Mode Switcher */}
              <div className="flex items-center space-x-1 bg-white/10 p-1 rounded-lg text-xs font-sans">
                <button
                  type="button"
                  onClick={() => setActiveTab("WEB")}
                  className={`px-2.5 sm:px-3 py-1 rounded font-medium flex items-center space-x-1 sm:space-x-1.5 transition-all cursor-pointer ${
                    activeTab === "WEB"
                      ? "bg-white text-black shadow-sm font-bold"
                      : "text-white/70 hover:text-white"
                  }`}
                >
                  <Globe className="w-3.5 h-3.5" />
                  <span className="hidden xs:inline">WEB DOSSIER</span>
                  <span className="xs:hidden">WEB</span>
                </button>

                <button
                  type="button"
                  onClick={() => setActiveTab("PDF")}
                  className={`px-2.5 sm:px-3 py-1 rounded font-medium flex items-center space-x-1 sm:space-x-1.5 transition-all cursor-pointer ${
                    activeTab === "PDF"
                      ? "bg-white text-black shadow-sm font-bold"
                      : "text-white/70 hover:text-white"
                  }`}
                >
                  <Printer className="w-3.5 h-3.5" />
                  <span className="hidden xs:inline">PRINT / PDF</span>
                  <span className="xs:hidden">PDF</span>
                </button>
              </div>

              {/* Right: Actions & Prominent Close Button */}
              <div className="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
                <button
                  type="button"
                  onClick={handleDownloadDossier}
                  className="px-2.5 sm:px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-sans font-bold flex items-center space-x-1.5 transition-all shadow-md cursor-pointer"
                  title="Print or Save official candidate dossier as publication PDF"
                >
                  <Download className="w-3.5 h-3.5 stroke-[2.5]" />
                  <span className="hidden xs:inline">DOWNLOAD PDF</span>
                  <span className="xs:hidden">PDF</span>
                </button>

                <a
                  href={`/dossier/${scholarshipId}`}
                  target="_blank"
                  rel="noreferrer"
                  className="p-1.5 rounded-lg bg-white/10 hover:bg-white/15 text-white/80 hover:text-white text-xs font-sans flex items-center transition-all"
                  title="Open standalone document in new browser tab"
                >
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>

                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    onClose();
                  }}
                  className="px-3.5 py-1.5 rounded-lg bg-red-600 hover:bg-red-700 active:scale-95 text-white border border-red-500 text-xs font-sans font-bold flex items-center space-x-1.5 transition-all cursor-pointer shadow-md ml-1"
                  title="Exit Dossier Viewer (Esc)"
                >
                  <X className="w-4 h-4 stroke-[2.5]" />
                  <span>EXIT DOSSIER</span>
                </button>
              </div>
            </div>

            {/* Sub-Header Bar when in PDF View Mode */}
            {activeTab === "PDF" && (
              <div className="bg-[#292524] text-white/90 px-4 sm:px-6 py-2 flex flex-wrap items-center justify-between text-xs font-mono border-b border-stone-700 gap-2 shrink-0 no-print">
                <div className="flex items-center space-x-2">
                  <FileCheck className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span className="font-bold text-white">A4 PUBLICATION PREVIEW</span>
                  <span className="text-white/40">•</span>
                  <span className="text-stone-300">Portrait 210 × 297 mm • Multi-Page Paginated • Vector Grade</span>
                </div>
                <div className="flex items-center space-x-2">
                  <button
                    type="button"
                    onClick={handleDownloadDossier}
                    className="px-3 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold flex items-center space-x-1.5 transition-all cursor-pointer shadow-sm text-xs"
                    title="Print or Save official candidate dossier as publication PDF"
                  >
                    <Printer className="w-3.5 h-3.5 stroke-[2.5]" />
                    <span>PRINT / SAVE AS PDF</span>
                  </button>
                </div>
              </div>
            )}

            {/* Scrollable Document Content Area with min-h-0 and momentum scrolling */}
            <div
              className="flex-1 min-h-0 h-full overflow-y-auto overscroll-contain dossier-scroll touch-pan-y"
              tabIndex={0}
              style={{ WebkitOverflowScrolling: "touch" }}
            >
              {activeTab === "PDF" ? (
                /* A4 Simulation Preview on Dark Desk Canvas */
                <div className="bg-[#18181B] py-6 sm:py-8 px-2 sm:px-6 flex justify-center min-h-full print:bg-white print:p-0 print:block">
                  <div className="w-full max-w-[880px] bg-[#FAFAF9] shadow-2xl rounded-sm border border-stone-400/30 overflow-visible print:border-none print:shadow-none print:max-w-none print:w-full print:p-0 relative">
                    <WebDossierView
                      dossier={dossier}
                      isPrintMode={true}
                      hideHeader={true}
                      onTriggerPrint={handleDownloadDossier}
                      onClose={onClose}
                    />
                  </div>
                </div>
              ) : (
                /* Standard Web Dossier View */
                <WebDossierView
                  dossier={dossier}
                  isPrintMode={false}
                  hideHeader={true}
                  onTriggerPrint={handleDownloadDossier}
                  onClose={onClose}
                />
              )}
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>,
    document.body
  );
};
