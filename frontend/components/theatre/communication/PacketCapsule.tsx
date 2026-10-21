"use client";

import React from "react";
import { motion } from "framer-motion";
import { PhysicalPacket } from "@/lib/communication/types";

export interface PacketCapsuleProps {
  packet: PhysicalPacket;
  className?: string;
  isDocked?: boolean;
}

export const PacketCapsule: React.FC<PacketCapsuleProps> = ({
  packet,
  className = "",
  isDocked = false,
}) => {
  const { type, senderName, receiverName, summary, priority, payload } = packet;

  // Visual tokens by packet type
  const getTypeMeta = () => {
    switch (type) {
      case "COMMAND":
        return {
          label: "COMMAND PACKET",
          accentColor: "#38BDF8",
          borderColor: "rgba(56, 189, 248, 0.6)",
          bgColor: "rgba(8, 20, 32, 0.92)",
          shadow: "0 0 28px rgba(56, 189, 248, 0.4)",
          tagBg: "rgba(56, 189, 248, 0.15)",
          tagText: "#7DD3FC",
        };
      case "ACKNOWLEDGEMENT":
        return {
          label: "ACKNOWLEDGEMENT",
          accentColor: "#10B981",
          borderColor: "rgba(16, 185, 129, 0.6)",
          bgColor: "rgba(6, 26, 18, 0.92)",
          shadow: "0 0 28px rgba(16, 185, 129, 0.4)",
          tagBg: "rgba(16, 185, 129, 0.15)",
          tagText: "#34D399",
        };
      case "REPORT":
        return {
          label: "SECTOR REPORT",
          accentColor: "#D4AF37",
          borderColor: "rgba(212, 175, 55, 0.65)",
          bgColor: "rgba(26, 22, 10, 0.94)",
          shadow: "0 0 32px rgba(212, 175, 55, 0.45)",
          tagBg: "rgba(212, 175, 55, 0.18)",
          tagText: "#FCD34D",
        };
      case "EVIDENCE":
        return {
          label: "OFFICIAL EVIDENCE",
          accentColor: "#10B981",
          borderColor: "rgba(16, 185, 129, 0.7)",
          bgColor: "rgba(5, 24, 18, 0.94)",
          shadow: "0 0 32px rgba(16, 185, 129, 0.45)",
          tagBg: "rgba(16, 185, 129, 0.2)",
          tagText: "#34D399",
        };
      case "CHALLENGE":
        return {
          label: "SKEPTIC CHALLENGE",
          accentColor: "#F59E0B",
          borderColor: "rgba(245, 158, 11, 0.75)",
          bgColor: "rgba(30, 18, 5, 0.94)",
          shadow: "0 0 32px rgba(245, 158, 11, 0.45)",
          tagBg: "rgba(245, 158, 11, 0.2)",
          tagText: "#FBBF24",
        };
      case "RESOLUTION":
        return {
          label: "EVIDENCE RESOLUTION",
          accentColor: "#A855F7",
          borderColor: "rgba(168, 85, 247, 0.7)",
          bgColor: "rgba(24, 10, 36, 0.94)",
          shadow: "0 0 32px rgba(168, 85, 247, 0.45)",
          tagBg: "rgba(168, 85, 247, 0.2)",
          tagText: "#C084FC",
        };
      default:
        return {
          label: type,
          accentColor: "#94A3B8",
          borderColor: "rgba(148, 163, 184, 0.4)",
          bgColor: "rgba(15, 23, 42, 0.9)",
          shadow: "0 0 16px rgba(148, 163, 184, 0.2)",
          tagBg: "rgba(148, 163, 184, 0.1)",
          tagText: "#CBD5E1",
        };
    }
  };

  const meta = getTypeMeta();

  return (
    <motion.div
      initial={{ scale: 0.92, opacity: 0.9 }}
      animate={{ scale: isDocked ? 1.03 : 1, opacity: 1 }}
      transition={{ duration: 0.3 }}
      className={`relative rounded-xl border backdrop-blur-xl p-2 select-none pointer-events-auto shadow-2xl transition-all duration-300 w-[215px] ${className}`}
      style={{
        backgroundColor: meta.bgColor,
        borderColor: meta.borderColor,
        boxShadow: meta.shadow,
      }}
    >
      {/* Top subtle highlight */}
      <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-white/30 to-transparent" />

      {/* Header: Type Badge & Routing Path */}
      <div className="flex items-center justify-between gap-1.5 mb-1">
        <div className="flex items-center space-x-1">
          <span
            className="w-1.5 h-1.5 rounded-full animate-ping"
            style={{ backgroundColor: meta.accentColor }}
          />
          <span
            className="px-1.5 py-0.2 rounded text-[8px] font-mono tracking-wider font-bold uppercase"
            style={{
              backgroundColor: meta.tagBg,
              color: meta.tagText,
              border: `1px solid ${meta.accentColor}33`,
            }}
          >
            {meta.label}
          </span>
        </div>

        <div className="text-[8px] font-mono tracking-wider text-sx-text-tertiary">
          <span className="font-semibold text-sx-text-secondary">{priority}</span>
        </div>
      </div>

      {/* Routing line: SENDER -> RECEIVER */}
      <div className="flex items-center space-x-1 text-[8px] font-mono text-sx-text-tertiary mb-1 border-b border-white/[0.08] pb-1">
        <span className="text-sx-text-secondary font-medium truncate max-w-[85px]">
          {senderName.replace(" Regional Scout", " Scout").replace("ScholarX ", "")}
        </span>
        <span className="text-white/40">→</span>
        <span className="text-sx-text-secondary font-medium truncate max-w-[85px]">
          {receiverName.replace(" Regional Scout", " Scout").replace("ScholarX ", "")}
        </span>
      </div>

      {/* Primary Payload Summary */}
      <div className="text-[11px] font-sans font-bold text-sx-text-primary tracking-tight leading-tight truncate">
        {summary}
      </div>

      {/* Payload Sub-details */}
      {payload?.directive && (
        <div className="mt-1.5 pt-1.5 border-t border-white/[0.06] text-[10px] font-mono text-sx-text-tertiary">
          <div className="truncate text-sx-ice/90">
            OBJECTIVE: {payload.directive.objective}
          </div>
        </div>
      )}

      {payload?.report && (
        <div className="mt-1.5 pt-1.5 border-t border-white/[0.06] flex items-center justify-between text-[10px] font-mono text-sx-text-secondary">
          <span className="text-sx-gold">
            {payload.report.candidatesCount} CANDIDATES DISCOVERED
          </span>
          <span className="text-sx-emerald">
            {payload.report.pakistanQuotaSeats} QUOTA SEATS
          </span>
        </div>
      )}

      {/* Subtle Docking State Glow Indicator */}
      {isDocked && (
        <motion.div
          className="absolute -inset-1 rounded-xl border border-sx-ice/50 pointer-events-none"
          animate={{ opacity: [0.3, 0.8, 0.3], scale: [1, 1.02, 1] }}
          transition={{ duration: 1.6, repeat: Infinity }}
        />
      )}
    </motion.div>
  );
};
