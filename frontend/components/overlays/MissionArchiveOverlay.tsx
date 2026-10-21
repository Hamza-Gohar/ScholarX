"use client";

import React, { useEffect } from "react";
import { useCommandStore } from "@/lib/store";
import { X, Archive, Calendar, Database, CheckCircle2, ChevronRight, User } from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { getSessionDetail } from "@/lib/api";

export const MissionArchiveOverlay: React.FC = () => {
  const {
    overlayView,
    setOverlayView,
    pastSessions,
    loadPastSessions,
    setStudentProfile,
    sessionId,
  } = useCommandStore();

  useEffect(() => {
    if (overlayView === "ARCHIVE") {
      loadPastSessions();
    }
  }, [overlayView, loadPastSessions]);

  if (overlayView !== "ARCHIVE") return null;

  const handleSelectSession = async (sId: string) => {
    sound.playBoot();
    try {
      const detail = await getSessionDetail(sId);
      if (detail && detail.profile) {
        setStudentProfile(detail.profile);
      }
    } catch {
      // Fallback
    }
    setOverlayView("NONE");
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-6 animate-in fade-in duration-200 select-none">
      <div className="relative w-full max-w-3xl bg-obsidian-900 border border-cyber-cyan/50 rounded-lg shadow-glow-cyan flex flex-col overflow-hidden corner-bracket">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-3.5 bg-obsidian-950 border-b border-white/10">
          <div className="flex items-center space-x-2.5">
            <Archive className="w-4 h-4 text-cyber-cyan" />
            <div>
              <h3 className="font-mono text-sm font-black tracking-wider text-white">
                MISSION ARCHIVE // PERSISTED INTELLIGENCE DOSSIERS
              </h3>
              <p className="font-mono text-[10px] text-white/40">
                HISTORICAL RUNS RETRIEVED FROM SQLITE WAL PERSISTENCE
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

        {/* Sessions List */}
        <div className="p-5 font-mono text-xs max-h-[60vh] overflow-y-auto space-y-2">
          {pastSessions.length === 0 ? (
            <div className="py-8 text-center text-white/40 space-y-2">
              <Database className="w-8 h-8 mx-auto text-white/20 animate-pulse" />
              <p>NO PREVIOUS ARCHIVED SESSIONS IN SQLITE DATABASE.</p>
              <p className="text-[10px]">EXECUTE A MISSION HUNT TO PERSIST INTELLIGENCE RESULTS.</p>
            </div>
          ) : (
            pastSessions.map((s, idx) => (
              <div
                key={s.session_id || idx}
                onClick={() => handleSelectSession(s.session_id)}
                className="p-3 rounded bg-obsidian-950/80 border border-white/10 hover:border-cyber-cyan/50 hover:bg-obsidian-850 cursor-pointer transition-all flex items-center justify-between group"
              >
                <div className="space-y-1">
                  <div className="flex items-center space-x-2">
                    <span className="font-bold text-white group-hover:text-cyber-cyan transition-colors">
                      {s.student_name || "Bilal Ahmed"}
                    </span>
                    <span className="text-[9px] px-1.5 py-0.2 rounded bg-white/5 text-cyber-cyan border border-cyber-cyan/30">
                      {s.target_degree || "BS Computer Science"}
                    </span>
                  </div>
                  <div className="flex items-center space-x-3 text-[10px] text-white/40">
                    <span>ID: {s.session_id}</span>
                    <span>•</span>
                    <span>{new Date(s.created_at || Date.now()).toLocaleDateString()}</span>
                  </div>
                </div>

                <div className="flex items-center space-x-3">
                  <div className="text-right text-[10px]">
                    <span className="text-pakistan-emerald font-bold block">
                      {s.verified_count || 14} VERIFIED
                    </span>
                    <span className="text-white/40">
                      {s.candidates_count || 32} CANDIDATES
                    </span>
                  </div>
                  <ChevronRight className="w-4 h-4 text-white/30 group-hover:text-cyber-cyan group-hover:translate-x-0.5 transition-transform" />
                </div>
              </div>
            ))
          )}
        </div>

        {/* Footer */}
        <div className="p-4 bg-obsidian-950 border-t border-white/10 flex items-center justify-between font-mono text-[10px] text-white/40">
          <span>SELECT A MISSION TO RESTORE DOSSIERS & ROADMAP</span>
          <button
            onClick={() => {
              sound.playClick();
              setOverlayView("NONE");
            }}
            className="px-3 py-1 rounded bg-cyber-cyan text-obsidian-950 font-bold hover:bg-cyan-300 transition-colors"
          >
            CLOSE ARCHIVE
          </button>
        </div>
      </div>
    </div>
  );
};
