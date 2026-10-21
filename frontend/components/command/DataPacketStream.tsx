"use client";

import React from "react";
import { useCommandStore } from "@/lib/store";
import { ArrowRight, Send, Database, ShieldAlert, Cpu, Sparkles } from "lucide-react";
import { PacketType } from "@/lib/types";

export const DataPacketStream: React.FC = () => {
  const { dataPackets } = useCommandStore();

  if (dataPackets.length === 0) return null;

  const getPacketBadge = (type: PacketType) => {
    switch (type) {
      case "TASK":
        return {
          bg: "bg-cyber-cyan/15 border-cyber-cyan/50 text-cyber-cyan shadow-glow-cyan",
          icon: <Cpu className="w-3 h-3 text-cyber-cyan" />,
        };
      case "CANDIDATE":
        return {
          bg: "bg-pakistan-emerald/15 border-pakistan-emerald/50 text-pakistan-emerald shadow-glow-emerald",
          icon: <Database className="w-3 h-3 text-pakistan-emerald" />,
        };
      case "CHALLENGE":
        return {
          bg: "bg-skeptic-rose/15 border-skeptic-rose/50 text-skeptic-rose shadow-glow-rose",
          icon: <ShieldAlert className="w-3 h-3 text-skeptic-rose" />,
        };
      case "SCORE":
        return {
          bg: "bg-warning-amber/15 border-warning-amber/50 text-warning-amber shadow-glow-amber",
          icon: <Sparkles className="w-3 h-3 text-warning-amber" />,
        };
      default:
        return {
          bg: "bg-white/10 border-white/20 text-white",
          icon: <Send className="w-3 h-3 text-white/60" />,
        };
    }
  };

  return (
    <div className="absolute top-16 left-1/2 -translate-x-1/2 z-40 pointer-events-none flex flex-col items-center space-y-1.5 w-full max-w-xl px-4">
      {dataPackets.map((pkt) => {
        const badge = getPacketBadge(pkt.type);
        return (
          <div
            key={pkt.id}
            className={`flex items-center space-x-2.5 px-3 py-1.5 rounded-full border backdrop-blur-md font-mono text-[10px] animate-in fade-in slide-in-from-top-3 duration-300 ${badge.bg}`}
          >
            {badge.icon}
            <div className="flex items-center space-x-1.5 font-bold">
              <span className="text-white/70">{pkt.source}</span>
              <ArrowRight className="w-3 h-3 text-white/40" />
              <span className="text-white">{pkt.target}</span>
            </div>
            <span className="text-white/20">|</span>
            <span className="font-semibold uppercase tracking-wider">{pkt.label}</span>
            <span className="text-white/60 text-[9px] hidden sm:inline">
              ({pkt.payloadSummary})
            </span>
          </div>
        );
      })}
    </div>
  );
};
