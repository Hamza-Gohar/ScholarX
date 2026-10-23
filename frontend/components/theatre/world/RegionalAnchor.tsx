"use client";

import React from "react";
import { motion } from "framer-motion";
import { GeographicAnchor, MapState } from "@/lib/spatial/types";

export interface RegionalAnchorProps {
  anchor: GeographicAnchor;
  mapState: MapState;
  isFocused?: boolean;
  onSelect?: () => void;
}

export const RegionalAnchor: React.FC<RegionalAnchorProps> = ({
  anchor,
  mapState,
  isFocused = false,
  onSelect,
}) => {
  const { scenePosition, label, sublabel, quotaCount } = anchor;
  const isDormant = mapState === "DORMANT";
  const isMission = mapState === "MISSION";
  const isDossier = mapState === "DOSSIER";

  // In Dormant state, regional anchors are very quiet
  const opacity = isDormant
    ? 0.25
    : isDossier
    ? 0.2
    : isFocused
    ? 1
    : isMission
    ? 0.65
    : 0.9;

  return (
    <g
      transform={`translate(${scenePosition.x}, ${scenePosition.y})`}
      opacity={opacity}
      className="cursor-pointer transition-opacity duration-500"
      onClick={onSelect}
    >
      {/* Focused Regional Attention Halo */}
      {isFocused && (
        <motion.circle
          r="48"
          fill="rgba(56, 189, 248, 0.08)"
          animate={{
            r: [40, 60, 40],
            opacity: [0.2, 0.45, 0.2],
          }}
          transition={{
            duration: 2.8,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        />
      )}

      {/* Target Ring */}
      <circle
        r={isFocused ? "18" : "14"}
        fill="none"
        stroke={
          isFocused
            ? "rgba(56, 189, 248, 0.7)"
            : "rgba(180, 210, 225, 0.25)"
        }
        strokeWidth="1.2"
        strokeDasharray={isFocused ? undefined : "3 3"}
      />

      {/* Center Beacon (Pure vector without filter drop-shadow) */}
      <circle
        r={isFocused ? "5.5" : "4"}
        fill={isFocused ? "#38BDF8" : "rgba(56, 189, 248, 0.75)"}
        stroke={isFocused ? "#7DD3FC" : undefined}
        strokeWidth={isFocused ? "1.5" : undefined}
      />

      {/* Regional Destination Card (Hardware-friendly solid obsidian fill) */}
      <g
        transform={
          anchor.region === "Americas" || anchor.id.includes("americas")
            ? "translate(-175, -20)"
            : "translate(18, -26)"
        }
      >
        <rect
          x="0"
          y="0"
          width="155"
          height="40"
          rx="6"
          fill="rgba(8, 12, 18, 0.94)"
          stroke={
            isFocused
              ? "rgba(56, 189, 248, 0.55)"
              : "rgba(180, 210, 225, 0.14)"
          }
          strokeWidth="1"
        />

        {/* Region Name */}
        <text
          x="10"
          y="16"
          fill={isFocused ? "#38BDF8" : "#F8FAFC"}
          fontSize="10"
          fontWeight="700"
          letterSpacing="0.12em"
          fontFamily="monospace"
        >
          {label}
        </text>

        {/* Subtitle / Grant Count */}
        <text
          x="10"
          y="30"
          fill="#94A3B8"
          fontSize="8"
          fontFamily="monospace"
          letterSpacing="0.08em"
        >
          {sublabel}
        </text>

        {/* Quota Badge */}
        {quotaCount && (
          <g transform="translate(95, 6)">
            <rect
              x="0"
              y="0"
              width="50"
              height="13"
              rx="3"
              fill={
                isFocused
                  ? "rgba(56, 189, 248, 0.2)"
                  : "rgba(255, 255, 255, 0.05)"
              }
              stroke={
                isFocused
                  ? "rgba(56, 189, 248, 0.4)"
                  : "rgba(255, 255, 255, 0.1)"
              }
              strokeWidth="0.8"
            />
            <text
              x="25"
              y="9.5"
              fill={isFocused ? "#7DD3FC" : "#CBD5E1"}
              fontSize="7"
              fontWeight="600"
              textAnchor="middle"
              fontFamily="monospace"
            >
              {quotaCount} SEATS
            </text>
          </g>
        )}
      </g>
    </g>
  );
};
