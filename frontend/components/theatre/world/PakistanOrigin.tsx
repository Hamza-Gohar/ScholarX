"use client";

import React from "react";
import { motion } from "framer-motion";
import { PAKISTAN_ANCHOR } from "@/lib/spatial/anchors";
import { MapState } from "@/lib/spatial/types";

export interface PakistanOriginProps {
  mapState: MapState;
  isFocused?: boolean;
}

export const PakistanOrigin: React.FC<PakistanOriginProps> = ({
  mapState,
  isFocused = false,
}) => {
  const { scenePosition, label, sublabel, quotaCount } = PAKISTAN_ANCHOR;
  const isDormant = mapState === "DORMANT";
  const isDossier = mapState === "DOSSIER";

  return (
    <g
      transform={`translate(${scenePosition.x}, ${scenePosition.y})`}
      className="pointer-events-none select-none"
    >
      {/* Outer Atmospheric Pulse Halo */}
      {!isDormant && !isDossier && (
        <motion.circle
          r="36"
          fill="rgba(16, 185, 129, 0.08)"
          animate={{
            r: [30, 48, 30],
            opacity: [0.15, 0.35, 0.15],
          }}
          transition={{
            duration: 3.2,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        />
      )}

      {/* Secondary Focus Ring */}
      <circle
        r={isDormant ? "14" : "18"}
        fill="none"
        stroke={isDormant ? "rgba(16, 185, 129, 0.2)" : "rgba(16, 185, 129, 0.45)"}
        strokeWidth="1.2"
        strokeDasharray={isDormant ? "3 3" : undefined}
      />

      {/* Target Crosshairs */}
      {!isDormant && (
        <g stroke="rgba(16, 185, 129, 0.4)" strokeWidth="1">
          <line x1="-22" y1="0" x2="-14" y2="0" />
          <line x1="14" y1="0" x2="22" y2="0" />
          <line x1="0" y1="-22" x2="0" y2="-14" />
          <line x1="0" y1="14" x2="0" y2="22" />
        </g>
      )}

      {/* Origin Center Beacon */}
      <circle
        r={isDormant ? "4" : "6"}
        fill={isDormant ? "#064E3B" : "#10B981"}
        className="filter drop-shadow-[0_0_8px_rgba(16,185,129,0.8)]"
      />
      <circle r="2" fill="#FFFFFF" />

      {/* Origin Identity Card / Label */}
      <g transform="translate(24, -28)">
        <rect
          x="0"
          y="0"
          width="180"
          height="44"
          rx="6"
          fill="rgba(5, 7, 10, 0.88)"
          stroke={
            isFocused || !isDormant
              ? "rgba(16, 185, 129, 0.45)"
              : "rgba(180, 210, 225, 0.12)"
          }
          strokeWidth="1"
          className="backdrop-blur-md"
        />

        {/* Origin Title */}
        <text
          x="12"
          y="17"
          fill="#F8FAFC"
          fontSize="11"
          fontWeight="700"
          letterSpacing="0.12em"
          fontFamily="monospace"
        >
          {label}
        </text>

        {/* Subtitle / Coordinates */}
        <text
          x="12"
          y="32"
          fill="#94A3B8"
          fontSize="8.5"
          fontFamily="monospace"
          letterSpacing="0.08em"
        >
          {isDormant ? "STANDBY ORIGIN" : sublabel}
        </text>

        {/* Quota Tag */}
        {!isDormant && (
          <g transform="translate(100, 7)">
            <rect
              x="0"
              y="0"
              width="68"
              height="14"
              rx="3"
              fill="rgba(16, 185, 129, 0.18)"
              stroke="rgba(16, 185, 129, 0.35)"
              strokeWidth="0.8"
            />
            <text
              x="34"
              y="10.5"
              fill="#34D399"
              fontSize="7.5"
              fontWeight="600"
              textAnchor="middle"
              fontFamily="monospace"
            >
              {quotaCount}+ SEATS
            </text>
          </g>
        )}
      </g>
    </g>
  );
};
