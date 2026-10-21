"use client";

import React from "react";
import { motion } from "framer-motion";

export interface DelegationBridgeProps {
  sourcePos: { x: number; y: number };
  targetPos: { x: number; y: number };
  visible: boolean;
  statusLabel?: string;
}

export const DelegationBridge: React.FC<DelegationBridgeProps> = ({
  sourcePos,
  targetPos,
  visible,
  statusLabel = "DELEGATED CHILD PROCESS",
}) => {
  if (!visible) return null;

  // Compute curved Bezier control points
  const dx = targetPos.x - sourcePos.x;
  const dy = targetPos.y - sourcePos.y;
  const cx1 = sourcePos.x + dx * 0.45;
  const cy1 = sourcePos.y - 40;
  const cx2 = sourcePos.x + dx * 0.55;
  const cy2 = targetPos.y - 40;

  const pathData = `M ${sourcePos.x} ${sourcePos.y} C ${cx1} ${cy1}, ${cx2} ${cy2}, ${targetPos.x} ${targetPos.y}`;
  const midX = (sourcePos.x + targetPos.x) / 2;
  const midY = (sourcePos.y + targetPos.y) / 2 - 35;

  return (
    <svg
      className="absolute inset-0 w-full h-full pointer-events-none z-theatre-secondary"
      style={{ overflow: "visible" }}
    >
      <defs>
        <linearGradient id="delegationGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#D4AF37" stopOpacity="0.6" />
          <stop offset="100%" stopColor="#38BDF8" stopOpacity="0.8" />
        </linearGradient>
      </defs>

      {/* Outer subtle glow line */}
      <motion.path
        d={pathData}
        fill="none"
        stroke="url(#delegationGrad)"
        strokeWidth="1.8"
        strokeDasharray="4 6"
        initial={{ opacity: 0 }}
        animate={{ opacity: [0.35, 0.7, 0.35] }}
        transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
      />

      {/* Floating delegation tag at midpoint */}
      <g transform={`translate(${midX}, ${midY})`}>
        <rect
          x="-90"
          y="-11"
          width="180"
          height="22"
          rx="4"
          fill="rgba(5, 7, 10, 0.85)"
          stroke="rgba(180, 210, 225, 0.18)"
          strokeWidth="0.8"
          className="backdrop-blur-sm"
        />
        <text
          x="0"
          y="3.5"
          fill="#94A3B8"
          fontSize="9"
          fontWeight="600"
          fontFamily="monospace"
          textAnchor="middle"
          letterSpacing="0.1em"
        >
          {statusLabel}
        </text>
      </g>
    </svg>
  );
};
