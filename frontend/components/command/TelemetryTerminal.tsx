"use client";

import React, { useState, useMemo, useRef, useEffect } from "react";
import { useCommandStore } from "@/lib/store";
import { Terminal, Search, ArrowDownCircle, ShieldAlert, Cpu, Sparkles, Filter } from "lucide-react";
import { sound } from "@/lib/sound-fx";

export const TelemetryTerminal: React.FC = () => {
  const { events, clearEvents, setSelectedScholarship, setOverlayView } = useCommandStore();
  const [filterText, setFilterText] = useState("");
  const [autoScroll, setAutoScroll] = useState(true);
  const terminalEndRef = useRef<HTMLDivElement>(null);

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

  return (
    <div className="relative w-full h-full flex flex-col command-panel corner-bracket rounded-lg overflow-hidden border border-white/10 select-none">
      {/* Terminal Title Bar */}
      <div className="flex items-center justify-between px-3 py-2 bg-obsidian-900/90 border-b border-white/10">
        <div className="flex items-center space-x-2">
          <Terminal className="w-3.5 h-3.5 text-cyber-cyan" />
          <span className="font-mono text-xs font-bold tracking-wider text-white">
            TELEMETRY_LOG // LIVE EVENT FEED
          </span>
          <span className="font-mono text-[10px] px-1.5 py-0.5 rounded bg-white/5 text-white/50">
            {events.length} EVTS
          </span>
        </div>

        {/* Filter Input & Controls */}
        <div className="flex items-center space-x-2">
          <div className="relative flex items-center">
            <Search className="w-3 h-3 text-white/40 absolute left-2 pointer-events-none" />
            <input
              type="text"
              placeholder="Filter log..."
              value={filterText}
              onChange={(e) => setFilterText(e.target.value)}
              className="bg-obsidian-950 border border-white/10 text-white font-mono text-[10px] pl-6 pr-2 py-0.5 rounded focus:outline-none focus:border-cyber-cyan/50 w-28 focus:w-36 transition-all"
            />
          </div>

          <button
            onClick={() => setAutoScroll(!autoScroll)}
            title={autoScroll ? "Auto-scroll ON" : "Auto-scroll PAUSED"}
            className={`p-1 rounded font-mono text-[10px] border transition-colors ${
              autoScroll
                ? "bg-cyber-cyan/20 text-cyber-cyan border-cyber-cyan/40"
                : "bg-obsidian-950 text-white/40 border-white/10"
            }`}
          >
            <ArrowDownCircle className="w-3 h-3" />
          </button>
        </div>
      </div>

      {/* Terminal Feed Display */}
      <div className="flex-1 overflow-y-auto p-2.5 font-mono text-[11px] space-y-1.5 bg-obsidian-950/80">
        {filteredEvents.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-white/30 space-y-2 py-8">
            <Cpu className="w-6 h-6 animate-pulse text-white/20" />
            <span>AWAITING MISSION TELEMETRY SIGNALS...</span>
            <span className="text-[10px]">CLICK &apos;LAUNCH HUNT&apos; IN THE TOP COMMAND BAR</span>
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
                className="flex items-start space-x-2 py-1 px-1.5 rounded hover:bg-white/[0.03] transition-colors transition-colors group"
              >
                {/* Time */}
                <span className="text-white/30 text-[10px] flex-shrink-0 pt-0.5">
                  [{timeStr}]
                </span>

                {/* Agent Display Tag */}
                <span className={`px-1.5 py-0.2 rounded text-[10px] font-semibold border flex-shrink-0 ${badgeColor}`}>
                  {evt.agent_display_name}
                </span>

                {/* Event Type & Message */}
                <div className="flex-1 min-w-0">
                  <div className="flex items-center space-x-2">
                    <span className="text-white/90 font-bold text-[11px]">
                      {evt.event_type}
                    </span>
                    {evt.payload.region && (
                      <span className="text-[9px] px-1 rounded bg-white/10 text-white/60">
                        {evt.payload.region}
                      </span>
                    )}
                  </div>

                  {/* Context snippet */}
                  <div className="text-white/60 text-[10px] truncate">
                    {evt.payload.message ||
                      evt.payload.name ||
                      evt.payload.query ||
                      evt.payload.challenge ||
                      JSON.stringify(evt.payload).substring(0, 100)}
                  </div>
                </div>
              </div>
            );
          })
        )}
        <div ref={terminalEndRef} />
      </div>
    </div>
  );
};
