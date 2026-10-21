"use client";

import React, { useEffect } from "react";
import Link from "next/link";
import { useCommandStore } from "@/lib/store";
import { 
  ShieldAlert, 
  Terminal, 
  Volume2, 
  VolumeX, 
  Tv, 
  Play, 
  Pause, 
  RotateCcw, 
  UserCheck, 
  FileText, 
  Server,
  Sparkles,
  Sliders,
  Network,
  Archive
} from "lucide-react";
import { sound } from "@/lib/sound-fx";

export const TopCommandBar: React.FC = () => {
  const {
    sessionId,
    missionStatus,
    missionPhase,
    overlayView,
    setOverlayView,
    scanlinesEnabled,
    setScanlinesEnabled,
    audioMuted,
    toggleAudio,
    backendConnected,
    checkBackendHealth,
    startMission,
    pauseMission,
    resetMission,
    studentProfile,
  } = useCommandStore();

  useEffect(() => {
    checkBackendHealth();
    const interval = setInterval(checkBackendHealth, 15000);
    return () => clearInterval(interval);
  }, [checkBackendHealth]);

  return (
    <header className="w-full bg-obsidian-900/95 border-b border-white/10 px-4 py-2 flex items-center justify-between select-none z-30 backdrop-blur-md">
      {/* Left: Brand, Mission Code & Gateway Connectivity */}
      <div className="flex items-center space-x-3">
        <div className="flex items-center space-x-2.5">
          <div className="w-3 h-3 rounded-sm bg-pakistan-emerald shadow-glow-emerald animate-pulse" />
          <div className="flex flex-col">
            <div className="flex items-center space-x-2">
              <span className="font-mono text-base font-black tracking-widest text-white">
                SCHOLAR<span className="text-cyber-cyan">X</span>
              </span>
              <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-pakistan-deep text-pakistan-emerald font-bold border border-pakistan-emerald/30">
                COMMAND ROOM 2.0
              </span>
            </div>
            <span className="font-mono text-[8px] text-white/40 tracking-wider">
              PAKISTAN SCHOLARSHIP INTELLIGENCE
            </span>
          </div>
        </div>

        <span className="text-white/20">|</span>

        {/* Backend Connectivity Status */}
        <div className="flex items-center space-x-1.5 font-mono text-[10px] px-2 py-0.5 rounded bg-obsidian-950 border border-white/10">
          <Server className={`w-3 h-3 ${backendConnected ? "text-pakistan-emerald" : "text-warning-amber"}`} />
          <span className="text-white/40">GW:</span>
          <span className={`font-semibold ${backendConnected ? "text-pakistan-emerald" : "text-warning-amber"}`}>
            {backendConnected ? "FASTAPI LIVE (8000)" : "AUTONOMOUS SIM"}
          </span>
        </div>

        {/* Active Student Pill */}
        <button
          onClick={() => {
            sound.playClick();
            setOverlayView("INTAKE");
          }}
          className="flex items-center space-x-1.5 font-mono text-[10px] px-2.5 py-0.5 rounded bg-obsidian-950 hover:bg-obsidian-800 border border-white/10 hover:border-cyber-cyan/40 transition-colors"
        >
          <UserCheck className="w-3 h-3 text-cyber-cyan" />
          <span className="text-white/50">STUDENT:</span>
          <span className="font-bold text-white max-w-[120px] truncate">
            {studentProfile.personal.name}
          </span>
          <span className="text-[8px] px-1 py-0.2 rounded bg-white/10 text-cyber-cyan font-bold">
            {(studentProfile.academic?.degree_level || "Bachelor's").split(" ")[0]}
          </span>
        </button>
      </div>

      {/* Center: Mission Control Action Triggers */}
      <div className="flex items-center space-x-2">
        {missionStatus === "RUNNING" ? (
          <button
            onClick={() => {
              sound.playClick();
              pauseMission();
            }}
            className="flex items-center space-x-1.5 px-4 py-1 rounded font-mono text-xs font-bold bg-warning-amber/20 hover:bg-warning-amber/30 text-warning-amber border border-warning-amber/40 transition-all shadow-glow-amber"
          >
            <Pause className="w-3 h-3 fill-current" />
            <span>PAUSE HUNT</span>
          </button>
        ) : (
          <button
            onClick={() => {
              sound.playClick();
              startMission();
            }}
            className="flex items-center space-x-1.5 px-5 py-1 rounded font-mono text-xs font-bold bg-cyber-cyan hover:bg-cyan-300 text-obsidian-950 border border-cyber-cyan transition-all shadow-glow-cyan"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>LAUNCH HUNT</span>
          </button>
        )}

        <button
          onClick={() => {
            sound.playClick();
            resetMission();
          }}
          title="Reset Session & Cache"
          className="p-1 rounded font-mono text-xs bg-obsidian-950 hover:bg-obsidian-800 text-white/50 hover:text-white border border-white/10 transition-colors"
        >
          <RotateCcw className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Right: Tactical Overlays & Hardware Toggles */}
      <div className="flex items-center space-x-2">
        {/* Navigation Overlays Switcher */}
        <div className="flex items-center bg-obsidian-950 p-0.5 rounded border border-white/10">
          <button
            onClick={() => {
              sound.playClick();
              setOverlayView(overlayView === "INTAKE" ? "NONE" : "INTAKE");
            }}
            className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-medium transition-all ${
              overlayView === "INTAKE"
                ? "bg-cyber-cyan text-obsidian-950 font-bold"
                : "text-white/60 hover:text-white"
            }`}
          >
            <UserCheck className="w-3 h-3" />
            <span>INTAKE</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView(overlayView === "AUDIT" ? "NONE" : "AUDIT");
            }}
            className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-medium transition-all ${
              overlayView === "AUDIT"
                ? "bg-skeptic-rose text-white font-bold shadow-glow-rose"
                : "text-white/60 hover:text-white"
            }`}
          >
            <ShieldAlert className="w-3 h-3" />
            <span>AUDIT</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView(overlayView === "ROADMAP" ? "NONE" : "ROADMAP");
            }}
            className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-medium transition-all ${
              overlayView === "ROADMAP"
                ? "bg-pakistan-emerald text-obsidian-950 font-bold shadow-glow-emerald"
                : "text-white/60 hover:text-white"
            }`}
          >
            <FileText className="w-3 h-3" />
            <span>ROADMAP</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView(overlayView === "MODIFIER" ? "NONE" : "MODIFIER");
            }}
            title="Live Mission Modifier (M)"
            className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-medium transition-all ${
              overlayView === "MODIFIER"
                ? "bg-warning-amber text-obsidian-950 font-bold shadow-glow-amber"
                : "text-white/60 hover:text-white"
            }`}
          >
            <Sliders className="w-3 h-3" />
            <span>MODIFIER</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView(overlayView === "XRAY" ? "NONE" : "XRAY");
            }}
            title="Architecture X-Ray Mode (X)"
            className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-medium transition-all ${
              overlayView === "XRAY"
                ? "bg-purple-500 text-white font-bold shadow-glow-purple"
                : "text-white/60 hover:text-white"
            }`}
          >
            <Network className="w-3 h-3" />
            <span>X-RAY</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView(overlayView === "ARCHIVE" ? "NONE" : "ARCHIVE");
            }}
            title="Session Archive (H)"
            className={`flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-medium transition-all ${
              overlayView === "ARCHIVE"
                ? "bg-white/20 text-white font-bold"
                : "text-white/60 hover:text-white"
            }`}
          >
            <Archive className="w-3 h-3" />
            <span>ARCHIVE</span>
          </button>

          <Link
            href="/catalog"
            title="Search 310+ Verified Scholarships"
            className="flex items-center space-x-1 px-2 py-0.5 rounded font-mono text-[10px] font-bold text-cyber-cyan hover:text-white bg-cyber-cyan/10 hover:bg-cyber-cyan/20 border border-cyber-cyan/30 transition-all"
          >
            <Sparkles className="w-3 h-3" />
            <span>CATALOG (310)</span>
          </Link>
        </div>

        {/* CRT Scanline Atmospheric Toggle */}
        <button
          onClick={() => {
            sound.playClick();
            setScanlinesEnabled(!scanlinesEnabled);
          }}
          title="Toggle CRT Scanline Texture"
          className={`p-1.5 rounded font-mono text-xs border transition-colors ${
            scanlinesEnabled
              ? "bg-cyber-cyan/15 text-cyber-cyan border-cyber-cyan/40"
              : "bg-obsidian-950 text-white/30 border-white/10"
          }`}
        >
          <Tv className="w-3.5 h-3.5" />
        </button>

        {/* Audio Mute/Unmute Toggle */}
        <button
          onClick={() => toggleAudio()}
          title={audioMuted ? "Sound Muted (Click to Enable Audio)" : "Tactical Sound Enabled"}
          className={`p-1.5 rounded font-mono text-xs border transition-colors ${
            !audioMuted
              ? "bg-pakistan-emerald/15 text-pakistan-emerald border-pakistan-emerald/40 shadow-glow-emerald"
              : "bg-obsidian-950 text-white/30 border-white/10"
          }`}
        >
          {audioMuted ? <VolumeX className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5 animate-pulse" />}
        </button>
      </div>
    </header>
  );
};
