"use client";

import React from "react";
import { motion } from "framer-motion";
import { Region } from "@/lib/types";

export interface FleetDelegationNetworkProps {
  commanderPos: { x: number; y: number };
  scoutPositions: Record<Region, { x: number; y: number }>;
  activeScouts?: Region[];
  focusedRegion?: Region | null;
  className?: string;
}

export const FleetDelegationNetwork: React.FC<FleetDelegationNetworkProps> = ({
  commanderPos,
  scoutPositions,
  activeScouts = ["Europe", "Asia", "Americas", "MENA", "Oceania"],
  focusedRegion = null,
  className = "",
}) => {
  const regions: Region[] = ["Europe", "Asia", "Americas", "MENA", "Oceania"];

  return (
    <svg
      className={`absolute inset-0 w-full h-full pointer-events-none z-theatre-routes overflow-visible ${className}`}
      viewBox="0 0 1920 1080"
      preserveAspectRatio="none"
    >
      <defs>
        <marker
          id="scoutArrow"
          viewBox="0 0 10 10"
          refX="6"
          refY="5"
          markerWidth="6"
          markerHeight="6"
          orient="auto-start-reverse"
        >
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38BDF8" opacity="0.85" />
        </marker>
        <marker
          id="scoutArrowGold"
          viewBox="0 0 10 10"
          refX="6"
          refY="5"
          markerWidth="7"
          markerHeight="7"
          orient="auto-start-reverse"
        >
          <path d="M 0 1 L 9 5 L 0 9 z" fill="#D4AF37" opacity="0.95" />
        </marker>

        <linearGradient id="fleetConduitGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#D4AF37" stopOpacity="0.6" />
          <stop offset="50%" stopColor="#38BDF8" stopOpacity="0.7" />
          <stop offset="100%" stopColor="#38BDF8" stopOpacity="0.4" />
        </linearGradient>

        <linearGradient id="fleetFocusConduitGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#D4AF37" stopOpacity="0.95" />
          <stop offset="100%" stopColor="#38BDF8" stopOpacity="1" />
        </linearGradient>
      </defs>

      {regions.map((reg, idx) => {
        const target = scoutPositions[reg];
        if (!target) return null;

        const isFocused = focusedRegion === reg;
        const isActive = activeScouts.includes(reg);

        // Calculate curved conduit
        const dx = target.x - commanderPos.x;
        const dy = target.y - commanderPos.y;
        const cx = (commanderPos.x + target.x) / 2 - dy * 0.15;
        const cy = (commanderPos.y + target.y) / 2 + dx * 0.08 - 40;

        const pathData = `M ${commanderPos.x} ${commanderPos.y} Q ${cx} ${cy} ${target.x} ${target.y}`;

        return (
          <g key={reg} className="transition-opacity duration-500">
            {/* Base curved line with animated dashing and arrow */}
            <motion.path
              d={pathData}
              fill="none"
              stroke={isFocused ? "url(#fleetFocusConduitGrad)" : "url(#fleetConduitGrad)"}
              strokeWidth={isFocused ? "2.2" : "1.4"}
              strokeDasharray="6,6"
              markerEnd={isFocused ? "url(#scoutArrowGold)" : "url(#scoutArrow)"}
              animate={{
                opacity: isFocused ? [0.7, 1, 0.7] : isActive ? 0.6 : 0.2,
                strokeDashoffset: [0, -48],
              }}
              transition={{
                opacity: { duration: 2.5, repeat: Infinity, ease: "easeInOut" },
                strokeDashoffset: { duration: 1.8, repeat: Infinity, ease: "linear" },
              }}
            />

            {/* Target node dot */}
            <circle
              cx={target.x}
              cy={target.y}
              r={isFocused ? "4" : "2.5"}
              fill={isFocused ? "#D4AF37" : "#38BDF8"}
              opacity={isActive ? 0.9 : 0.3}
            />

            {/* Traveling animated energy pulse towards scout */}
            {isActive && (
              <motion.circle
                r={isFocused ? "4" : "3"}
                fill={isFocused ? "#D4AF37" : "#38BDF8"}
                filter="drop-shadow(0 0 8px #38BDF8)"
                initial={{ opacity: 0 }}
                animate={{
                  opacity: [0, 0.95, 0.95, 0],
                  cx: [commanderPos.x, cx, target.x],
                  cy: [commanderPos.y, cy, target.y],
                }}
                transition={{
                  duration: 2.4,
                  repeat: Infinity,
                  ease: "easeInOut",
                  delay: (idx * 0.45) % 2.2,
                }}
              />
            )}
          </g>
        );
      })}
    </svg>
  );
};
