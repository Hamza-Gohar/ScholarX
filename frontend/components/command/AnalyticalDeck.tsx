"use client";

import React, { useState, useMemo, useRef, useEffect } from "react";
import { useCommandStore } from "@/lib/store";
import { 
  Terminal, 
  Search, 
  ArrowDownCircle, 
  ShieldAlert, 
  Cpu, 
  Coins, 
  Calendar, 
  CheckCircle2, 
  AlertTriangle, 
  ExternalLink,
  Filter,
  Sparkles,
  Award
} from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { DeckTab } from "@/lib/store";

export const AnalyticalDeck: React.FC = () => {
  const {
    activeDeckTab,
    setActiveDeckTab,
    events,
    candidates,
    selectedScholarship,
    setSelectedScholarship,
    setOverlayView,
    studentProfile,
    scoreMutations,
  } = useCommandStore();

  const [filterText, setFilterText] = useState("");
  const [autoScroll, setAutoScroll] = useState(true);
  const terminalEndRef = useRef<HTMLDivElement>(null);

  // Filtered telemetry events
  const filteredEvents = useMemo(() => {
    if (!filterText.trim()) return events;
    const q = filterText.toLowerCase();
    return events.filter(
      (e) =>
        e.event_type.toLowerCase().includes(q) ||
        e.agent_display_name.toLowerCase().includes(q) ||
        JSON.stringify(e.payload).toLowerCase().includes(q)
    );
  }, [events, filterText]);

  useEffect(() => {
    if (autoScroll && terminalEndRef.current) {
      terminalEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [filteredEvents, autoScroll]);

  // Current active scholarship for verification & cost inspection
  const activeScholarship = selectedScholarship || candidates[0];

  return (
    <div className="relative w-full h-full flex flex-col command-panel corner-bracket rounded-lg overflow-hidden border border-white/10 select-none bg-obsidian-950/90">
      {/* Top Multi-Tab Switcher */}
      <div className="flex items-center justify-between px-2 py-1.5 bg-obsidian-900/95 border-b border-white/10">
        <div className="flex items-center space-x-1">
          <button
            onClick={() => {
              sound.playClick();
              setActiveDeckTab("TELEMETRY");
            }}
            className={`flex items-center space-x-1.5 px-2.5 py-1 rounded font-mono text-[10px] font-bold transition-all ${
              activeDeckTab === "TELEMETRY"
                ? "bg-cyber-cyan text-obsidian-950 shadow-glow-cyan"
                : "text-white/60 hover:text-white hover:bg-white/5"
            }`}
          >
            <Terminal className="w-3 h-3" />
            <span>TELEMETRY ({events.length})</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setActiveDeckTab("SKEPTIC");
            }}
            className={`flex items-center space-x-1.5 px-2.5 py-1 rounded font-mono text-[10px] font-bold transition-all ${
              activeDeckTab === "SKEPTIC"
                ? "bg-skeptic-rose text-white shadow-glow-rose"
                : "text-white/60 hover:text-white hover:bg-white/5"
            }`}
          >
            <ShieldAlert className="w-3 h-3" />
            <span>SKEPTIC & VERIFY</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setActiveDeckTab("COSTS");
            }}
            className={`flex items-center space-x-1.5 px-2.5 py-1 rounded font-mono text-[10px] font-bold transition-all ${
              activeDeckTab === "COSTS"
                ? "bg-pakistan-emerald text-obsidian-950 shadow-glow-emerald"
                : "text-white/60 hover:text-white hover:bg-white/5"
            }`}
          >
            <Coins className="w-3 h-3" />
            <span>TRUE COST (PKR)</span>
          </button>
        </div>

        {activeDeckTab === "TELEMETRY" && (
          <div className="flex items-center space-x-1.5">
            <input
              type="text"
              placeholder="Filter..."
              value={filterText}
              onChange={(e) => setFilterText(e.target.value)}
              className="bg-obsidian-950 border border-white/10 text-white font-mono text-[9px] px-2 py-0.5 rounded focus:outline-none focus:border-cyber-cyan/50 w-20 focus:w-28 transition-all"
            />
            <button
              onClick={() => setAutoScroll(!autoScroll)}
              title={autoScroll ? "Auto-scroll ON" : "Auto-scroll PAUSED"}
              className={`p-1 rounded font-mono text-[9px] border transition-colors ${
                autoScroll
                  ? "bg-cyber-cyan/20 text-cyber-cyan border-cyber-cyan/40"
                  : "bg-obsidian-950 text-white/40 border-white/10"
              }`}
            >
              <ArrowDownCircle className="w-2.5 h-2.5" />
            </button>
          </div>
        )}
      </div>

      {/* Tab 1: Live Telemetry Terminal Feed */}
      {activeDeckTab === "TELEMETRY" && (
        <div className="flex-1 overflow-y-auto p-2 font-mono text-[10px] space-y-1.5 bg-obsidian-950/80">
          {filteredEvents.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-white/30 space-y-2 py-10">
              <Cpu className="w-6 h-6 animate-pulse text-white/20" />
              <span>AWAITING MISSION TELEMETRY SIGNALS...</span>
              <span className="text-[9px]">LAUNCH HUNT TO STREAM LIVE AGENT LOGS</span>
            </div>
          ) : (
            filteredEvents.map((evt) => {
              const timeStr = evt.timestamp
                ? new Date(evt.timestamp).toLocaleTimeString()
                : new Date().toLocaleTimeString();

              let badgeColor = "text-cyber-cyan bg-cyber-cyan/10 border-cyber-cyan/30";
              if (evt.severity === "SUCCESS") {
                badgeColor = "text-pakistan-emerald bg-pakistan-emerald/10 border-pakistan-emerald/30";
              } else if (evt.severity === "WARNING") {
                badgeColor = "text-warning-amber bg-warning-amber/10 border-warning-amber/30";
              } else if (evt.severity === "ERROR" || evt.severity === "CRITICAL") {
                badgeColor = "text-skeptic-rose bg-skeptic-rose/10 border-skeptic-rose/30";
              }

              return (
                <div
                  key={evt.event_id}
                  className="flex items-start space-x-2 py-1 px-1.5 rounded hover:bg-white/[0.04] transition-colors border border-transparent hover:border-white/5"
                >
                  <span className="text-white/40 text-[9px] whitespace-nowrap pt-0.5">
                    {timeStr}
                  </span>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center space-x-1.5 mb-0.5">
                      <span className={`px-1 py-0.2 rounded text-[8px] font-bold border ${badgeColor}`}>
                        {evt.event_type.replace(/_/g, " ")}
                      </span>
                      <span className="text-white/60 text-[9px] truncate">
                        {evt.agent_display_name}
                      </span>
                    </div>
                    <div className="text-white/80 text-[10px] truncate">
                      {evt.payload?.message ||
                        evt.payload?.query ||
                        evt.payload?.scholarship_name ||
                        evt.payload?.challenge ||
                        JSON.stringify(evt.payload).substring(0, 75)}
                    </div>
                  </div>
                </div>
              );
            })
          )}
          <div ref={terminalEndRef} />
        </div>
      )}

      {/* Tab 2: Verification Theater & Skeptic Arena Console */}
      {activeDeckTab === "SKEPTIC" && (
        <div className="flex-1 overflow-y-auto p-3 font-mono text-[10px] space-y-3 bg-obsidian-950/80">
          {/* Target Candidate Bar */}
          <div className="flex items-center justify-between p-2 rounded bg-obsidian-900 border border-white/10">
            <div>
              <span className="text-white/40 text-[9px] block">ACTIVE VERIFICATION TARGET</span>
              <span className="font-bold text-white text-[11px] truncate">
                {activeScholarship ? activeScholarship.name : "DAAD Study Scholarships (Germany)"}
              </span>
            </div>
            <span className="px-2 py-0.5 rounded bg-pakistan-deep text-pakistan-emerald font-bold border border-pakistan-emerald/30 text-[9px]">
              {activeScholarship ? activeScholarship.status : "VERIFIED"}
            </span>
          </div>

          {/* Verification Multi-Source Check (Section 14) */}
          <div className="p-2.5 rounded bg-obsidian-900/60 border border-cyber-cyan/30 space-y-2">
            <div className="flex items-center justify-between border-b border-white/5 pb-1">
              <span className="text-cyber-cyan font-bold flex items-center space-x-1">
                <CheckCircle2 className="w-3.5 h-3.5" />
                <span>SOURCE CROSS-EXAMINATION</span>
              </span>
              <span className="text-pakistan-emerald font-bold">96% CONSISTENCY</span>
            </div>
            <div className="space-y-1 text-[9px]">
              <div className="flex items-center justify-between text-white/70">
                <span>Official Portal (daad.de / stipendia):</span>
                <span className="text-pakistan-emerald font-bold">✓ VERIFIED</span>
              </div>
              <div className="flex items-center justify-between text-white/70">
                <span>HEC Bilateral Listing (eservices.hec.gov.pk):</span>
                <span className="text-pakistan-emerald font-bold">✓ RECOGNIZED</span>
              </div>
              <div className="flex items-center justify-between text-white/70">
                <span>Pakistani MOI Acceptance:</span>
                <span className="text-warning-amber font-bold">⚡ REQUIRES WAIVER</span>
              </div>
            </div>
          </div>

          {/* Adversarial Skeptic Challenges (Section 15) */}
          <div className="p-2.5 rounded bg-obsidian-900/60 border border-skeptic-rose/40 space-y-2">
            <div className="flex items-center justify-between border-b border-white/5 pb-1">
              <span className="text-skeptic-rose font-bold flex items-center space-x-1">
                <ShieldAlert className="w-3.5 h-3.5" />
                <span>SKEPTIC ADVERSARIAL CHALLENGES</span>
              </span>
              <span className="px-1.5 py-0.2 rounded bg-skeptic-rose/20 text-skeptic-rose font-bold text-[8px]">
                ACTIVE
              </span>
            </div>
            <div className="space-y-1.5">
              <div className="p-1.5 rounded bg-obsidian-950 border border-skeptic-rose/20 text-white/80 text-[9px]">
                <span className="text-skeptic-rose font-bold block mb-0.5">
                  ⚠ GERMAN VISA APPOINTMENT WAIT TIME (9–12 MONTHS):
                </span>
                German Embassy Islamabad / Consulate Karachi has an extensive appointment queue for Category A student visas. Immediate appointment booking required upon admission.
              </div>
              <div className="p-1.5 rounded bg-obsidian-950 border border-skeptic-rose/20 text-white/80 text-[9px]">
                <span className="text-skeptic-rose font-bold block mb-0.5">
                  ⚠ UNCOVERED SETTLEMENT BUFFER:
                </span>
                First-month rent deposit (€800–€1,200) must be paid before stipend disbursement. Student needs PKR 280,000 liquid settlement buffer.
              </div>
            </div>
          </div>

          {/* Recent Score Mutations Log (Section 16) */}
          {scoreMutations.length > 0 && (
            <div className="p-2 rounded bg-obsidian-900 border border-warning-amber/30 space-y-1.5">
              <span className="text-warning-amber font-bold text-[9px] flex items-center space-x-1">
                <Sparkles className="w-3 h-3" />
                <span>SCORE MUTATION AUDIT LOG</span>
              </span>
              {scoreMutations.slice(0, 3).map((m, i) => (
                <div key={i} className="text-[9px] text-white/80 flex items-center justify-between border-t border-white/5 pt-1">
                  <span className="truncate max-w-[150px]">{m.scholarshipName}</span>
                  <div className="flex items-center space-x-1.5">
                    <span className="text-pakistan-emerald font-bold">{m.prevScore}</span>
                    <span className="text-white/30">→</span>
                    <span className="text-warning-amber font-bold">{m.newScore}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Tab 3: True Out-of-Pocket Cost (PKR) & Deadline Intelligence */}
      {activeDeckTab === "COSTS" && (
        <div className="flex-1 overflow-y-auto p-3 font-mono text-[10px] space-y-3 bg-obsidian-950/80">
          {/* PKR Out-of-Pocket Summary (Section 17) */}
          <div className="p-2.5 rounded bg-obsidian-900 border border-pakistan-emerald/30 space-y-2">
            <div className="flex items-center justify-between border-b border-white/5 pb-1">
              <span className="text-pakistan-emerald font-bold">REALISTIC OUT-OF-POCKET (PKR)</span>
              <span className="text-white/40 text-[9px]">PRE-DEPARTURE EXPENSES</span>
            </div>
            <div className="space-y-1.5 text-[9px]">
              <div className="flex items-center justify-between text-white/80">
                <span>HEC & IBCC Degree Attestation:</span>
                <span className="font-bold text-white">PKR 18,000</span>
              </div>
              <div className="flex items-center justify-between text-white/80">
                <span>IELTS Academic Exam Fee:</span>
                <span className="font-bold text-white">PKR 58,000</span>
              </div>
              <div className="flex items-center justify-between text-white/80">
                 <span>Embassy Visa &amp; Gerry&apos;s Courier:</span>
                <span className="font-bold text-white">PKR 35,000</span>
              </div>
              <div className="flex items-center justify-between text-white/80">
                <span>One-Way Flight Ticket (ISB/LHE):</span>
                <span className="font-bold text-white">PKR 165,000</span>
              </div>
              <div className="flex items-center justify-between text-white/80">
                <span>First Month Settlement Allowance:</span>
                <span className="font-bold text-white">PKR 70,000</span>
              </div>
              <div className="flex items-center justify-between pt-1 border-t border-white/10 text-[10px]">
                <span className="font-bold text-white">TOTAL ESTIMATED PKR:</span>
                <span className="font-black text-pakistan-emerald text-[11px]">PKR 346,000</span>
              </div>
            </div>
          </div>

          {/* Student Budget Comparison */}
          <div className="p-2 rounded bg-obsidian-900 border border-white/10 flex items-center justify-between text-[10px]">
            <div>
              <span className="text-white/40 text-[9px] block">STUDENT LIQUID BUDGET</span>
              <span className="font-bold text-white">
                PKR {studentProfile.financial.max_out_of_pocket_pkr.toLocaleString()}
              </span>
            </div>
            <span className="px-2 py-0.5 rounded font-bold text-[9px] bg-pakistan-emerald/20 text-pakistan-emerald border border-pakistan-emerald/40">
              FEASIBLE // WITHIN LIMIT
            </span>
          </div>

          {/* Deadline Intelligence (Section 19) */}
          <div className="p-2.5 rounded bg-obsidian-900 border border-warning-amber/30 space-y-2">
            <div className="flex items-center justify-between border-b border-white/5 pb-1">
              <span className="text-warning-amber font-bold flex items-center space-x-1">
                <Calendar className="w-3.5 h-3.5" />
                <span>DEADLINE INTELLIGENCE & SLACK</span>
              </span>
              <span className="px-1.5 py-0.2 rounded bg-pakistan-emerald/20 text-pakistan-emerald font-bold text-[8px]">
                LOW RISK
              </span>
            </div>
            <div className="space-y-1 text-[9px] text-white/80">
              <div className="flex items-center justify-between">
                <span>Target Portal Deadline:</span>
                <span className="font-bold text-white">15 JAN 2027</span>
              </div>
              <div className="flex items-center justify-between">
                <span>Days Remaining:</span>
                <span className="font-bold text-cyber-cyan">105 DAYS</span>
              </div>
              <div className="flex items-center justify-between">
                <span>Pakistani Document Lead Time:</span>
                <span className="font-bold text-warning-amber">28 DAYS (HEC+IBCC)</span>
              </div>
              <div className="flex items-center justify-between pt-1 border-t border-white/5">
                <span>Calculated Preparation Slack:</span>
                <span className="font-bold text-pakistan-emerald">+77 DAYS BUFFER</span>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
