"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { 
  X, 
  FileText, 
  Coins, 
  Building2, 
  Calendar, 
  CheckCircle2, 
  Printer, 
  Download,
  MapPin, 
  ExternalLink,
  Clock,
  Sparkles
} from "lucide-react";
import { sound } from "@/lib/sound-fx";

interface PakistaniOfficeItem {
  name: string;
  type: string;
  city: string;
  address: string;
  feePkr: number;
  turnaroundDays: number;
  proTip: string;
}

const PAKISTANI_OFFICES: PakistaniOfficeItem[] = [
  {
    name: "HEC Regional Center Lahore",
    type: "HEC Attestation",
    city: "Lahore",
    address: "55-B/II, Gulberg III, Lahore, Punjab",
    feePkr: 8000,
    turnaroundDays: 14,
    proTip: "Apply online at eservices.hec.gov.pk first; choose urgent walk-in appointment for faster processing.",
  },
  {
    name: "IBCC Secretariat Islamabad",
    type: "IBCC Equivalence",
    city: "Islamabad",
    address: "Plot No. 25, Street 38, G-10/4, Islamabad",
    feePkr: 6000,
    turnaroundDays: 10,
    proTip: "Matric and FSc certificates must be verified by your respective BISE / FBISE board before submitting to IBCC.",
  },
  {
    name: "Ministry of Foreign Affairs (MOFA)",
    type: "Apostille / Legalization",
    city: "Islamabad / Camp Offices",
    address: "Constitution Avenue, G-5/1, Islamabad (Camp offices in Lahore, Karachi, Peshawar, Quetta)",
    feePkr: 2500,
    turnaroundDays: 5,
    proTip: "Use TCS or Gerry's postal courier service for MOFA attestation to avoid standing in long queues.",
  },
  {
    name: "Gerry's Visa Drop Box / VFS Global",
    type: "Visa Application Center",
    city: "Islamabad / Lahore / Karachi",
    address: "Park Road, Chattha Bakhtawar, Islamabad / Bahria Town Lahore",
    feePkr: 35000,
    turnaroundDays: 21,
    proTip: "Book your appointment immediately after receiving the scholarship award letter; slots fill up 2 months in advance.",
  },
  {
    name: "Approved Panel Clinics (IOM / Wilcare)",
    type: "Medical Examination",
    city: "Major Cities",
    address: "IOM Migration Health Assessment Center, Islamabad / Lahore",
    feePkr: 18000,
    turnaroundDays: 4,
    proTip: "Fast for 8 hours prior to test; bring 4 passport-size photos with white background and original passport.",
  },
];

const ROADMAP_PHASES = [
  {
    phase: "PHASE 1: ACADEMIC CREDENTIALS & TESTS (DAYS 1 - 20)",
    items: [
      { name: "BISE / FBISE Board Verification of Matric / FSc", costPkr: 4000, done: true },
      { name: "IBCC Equivalence Certificate", costPkr: 6000, done: true },
      { name: "HEC Online Degree Attestation (BS / MS)", costPkr: 8000, done: false },
      { name: "IELTS Academic Test (British Council / AEO)", costPkr: 58000, done: false },
    ],
  },
  {
    phase: "PHASE 2: DOSSIER & MOTIVATION LETTERS (DAYS 21 - 30)",
    items: [
      { name: "Statement of Purpose & Research Proposal", costPkr: 0, done: false },
      { name: "Two Academic Recommendation Letters", costPkr: 0, done: false },
      { name: "HEC HAT / USAT Test (if applicable)", costPkr: 2000, done: false },
    ],
  },
  {
    phase: "PHASE 3: EMBASSY VISA & ATTESTATIONS (DAYS 31 - 40)",
    items: [
      { name: "MOFA Legalization of Degrees", costPkr: 2500, done: false },
      { name: "National Police Clearance Certificate", costPkr: 1000, done: false },
      { name: "Medical Fitness & TB Chest X-ray", costPkr: 18000, done: false },
      { name: "Embassy Visa Fee & Gerry's Processing", costPkr: 35000, done: false },
    ],
  },
  {
    phase: "PHASE 4: PRE-DEPARTURE (DAYS 41 - 45)",
    items: [
      { name: "International Student Health Insurance Buffer", costPkr: 20000, done: false },
      { name: "Pre-departure Initial Cash Allowance", costPkr: 50000, done: false },
    ],
  },
];

export const PakistanRoadmapOverlay: React.FC = () => {
  const { overlayView, setOverlayView, studentProfile } = useCommandStore();

  if (overlayView !== "ROADMAP") return null;

  const totalEstimatedCostPkr = ROADMAP_PHASES.reduce(
    (acc, phase) => acc + phase.items.reduce((pAcc, item) => pAcc + item.costPkr, 0),
    0
  );

  return (
    <div className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-2 sm:p-6 animate-in fade-in duration-200">
      <div className="relative w-full max-w-6xl h-[92vh] sm:h-[88vh] bg-obsidian-900 border border-pakistan-emerald/40 rounded-lg shadow-glow-emerald flex flex-col overflow-hidden corner-bracket">
        {/* Header */}
        <div className="flex flex-wrap items-center justify-between px-3.5 sm:px-6 py-3 sm:py-3.5 bg-obsidian-950 border-b border-white/10 select-none gap-2">
          <div className="flex items-center space-x-2.5 sm:space-x-3 min-w-0">
            <FileText className="w-5 h-5 text-pakistan-emerald shrink-0" />
            <div className="min-w-0">
              <h2 className="font-mono text-xs sm:text-sm font-bold tracking-wider text-white truncate">
                PAKISTAN EXECUTION ROADMAP // PKR EXPENSE & LOCAL OFFICES
              </h2>
              <p className="font-mono text-[9px] sm:text-[10px] text-white/40 truncate">
                HEC & IBCC ATTESTATION • PKR OUT-OF-POCKET BUDGET • EMBASSY CLEARANCE
              </p>
            </div>
          </div>

          <div className="flex items-center space-x-2 shrink-0">
            <button
              onClick={() => {
                sound.playClick();
                const link = document.createElement("a");
                link.href = `/api/download/pdf?id=primary&name=Hamza_Gohar`;
                link.download = "ScholarX_Pakistan_Roadmap_Hamza_Gohar.pdf";
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
              }}
              className="flex items-center space-x-1.5 px-2.5 sm:px-3 py-1.5 rounded font-mono text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition-colors cursor-pointer"
            >
              <Download className="w-3.5 h-3.5" />
              <span className="hidden xs:inline">DOWNLOAD ROADMAP</span>
              <span className="xs:hidden">DOWNLOAD</span>
            </button>

            <button
              onClick={() => {
                sound.playClick();
                setOverlayView("NONE");
              }}
              className="p-1.5 rounded hover:bg-white/10 text-white/50 hover:text-white transition-colors cursor-pointer"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Body Content */}
        <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 gap-5 p-3.5 sm:p-5 overflow-y-auto touch-scroll">
          {/* Left Column (7 cols): Step-by-Step Milestones & PKR Cost Breakdown */}
          <div className="lg:col-span-7 flex flex-col space-y-4 overflow-y-auto pr-1">
            {/* PKR Financial Summary Bar */}
            <div className="command-panel p-3.5 sm:p-4 rounded border border-pakistan-emerald/30 flex items-center justify-between">
              <div>
                <span className="font-mono text-[10px] text-white/50 block">TOTAL ESTIMATED PREPARATION BUDGET</span>
                <span className="font-mono text-lg sm:text-xl font-black text-pakistan-emerald">
                  PKR {totalEstimatedCostPkr.toLocaleString()}
                </span>
              </div>
              <div className="text-right">
                <span className="font-mono text-[10px] text-white/50 block">STUDENT MAX OUT-OF-POCKET</span>
                <span className="font-mono text-base font-bold text-cyber-cyan">
                  PKR {(studentProfile.financial.max_out_of_pocket_pkr).toLocaleString()}
                </span>
                <span className="font-mono text-[10px] text-pakistan-emerald block">
                  {studentProfile.financial.max_out_of_pocket_pkr >= totalEstimatedCostPkr
                    ? "✓ WITHIN BUDGET"
                    : "⚠️ EXPENSE SHORTFALL"}
                </span>
              </div>
            </div>

            {/* Phases List */}
            <div className="space-y-3 font-mono text-xs">
              {ROADMAP_PHASES.map((phaseGroup, idx) => (
                <div key={idx} className="command-panel p-3.5 rounded border border-white/10 space-y-2">
                  <div className="font-bold text-cyber-cyan text-xs tracking-wider flex items-center justify-between border-b border-white/5 pb-1.5">
                    <span>{phaseGroup.phase}</span>
                  </div>

                  <div className="space-y-1.5">
                    {phaseGroup.items.map((item, itemIdx) => (
                      <div
                        key={itemIdx}
                        className="flex items-center justify-between p-2 rounded bg-obsidian-950 border border-white/5"
                      >
                        <div className="flex items-center space-x-2">
                          <CheckCircle2
                            className={`w-4 h-4 ${
                              item.done ? "text-pakistan-emerald" : "text-white/20"
                            }`}
                          />
                          <span className={item.done ? "line-through text-white/40" : "text-white/90"}>
                            {item.name}
                          </span>
                        </div>
                        <span className="font-bold text-warning-amber">
                          {item.costPkr > 0 ? `PKR ${item.costPkr.toLocaleString()}` : "FREE"}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Right Column (5 cols): Pakistani Office Directory */}
          <div className="lg:col-span-5 flex flex-col space-y-3 overflow-y-auto pr-1">
            <span className="font-mono text-xs font-bold text-white/60 tracking-wider flex items-center space-x-1.5">
              <Building2 className="w-4 h-4 text-cyber-cyan" />
              <span>KEY PAKISTANI ATTESTATION & VISA OFFICES</span>
            </span>

            {PAKISTANI_OFFICES.map((off, i) => (
              <div
                key={i}
                className="command-panel p-3 rounded border border-white/10 font-mono text-xs space-y-1.5 hover:border-cyber-cyan/40 transition-colors"
              >
                <div className="flex items-center justify-between">
                  <span className="font-bold text-white">{off.name}</span>
                  <span className="text-[10px] px-1.5 py-0.5 rounded bg-white/10 text-cyber-cyan font-bold">
                    {off.type}
                  </span>
                </div>

                <div className="flex items-center space-x-1 text-white/50 text-[10px]">
                  <MapPin className="w-3 h-3 text-white/30" />
                  <span>{off.address}</span>
                </div>

                <div className="flex items-center justify-between text-[10px] text-white/60 pt-1 border-t border-white/5">
                  <span>Fee: <strong className="text-warning-amber">PKR {off.feePkr.toLocaleString()}</strong></span>
                  <span>Turnaround: <strong className="text-white">{off.turnaroundDays} Days</strong></span>
                </div>

                <div className="text-[10px] text-pakistan-emerald bg-pakistan-deep/40 p-1.5 rounded border border-pakistan-emerald/20">
                  💡 <strong>Pro Tip:</strong> {off.proTip}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
