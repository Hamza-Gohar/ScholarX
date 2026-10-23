"use client";

import React from "react";
import { motion } from "framer-motion";
import { PhysicalPacket } from "@/lib/communication/types";
import { PacketCapsule } from "./PacketCapsule";

export interface PacketCanvasProps {
  packet?: PhysicalPacket | null;
  packets?: PhysicalPacket[];
  className?: string;
}

export const PacketCanvas: React.FC<PacketCanvasProps> = ({
  packet,
  packets,
  className = "",
}) => {
  // Merge singular and array inputs
  const packetList: PhysicalPacket[] = packets
    ? packets
    : packet
    ? [packet]
    : [];

  if (packetList.length === 0) return null;

  return (
    <div
      className={`absolute inset-0 pointer-events-none z-theatre-focus overflow-visible ${className}`}
    >
      <svg
        className="w-full h-full absolute inset-0 overflow-visible z-theatre-routes"
        viewBox="0 0 1920 1080"
        preserveAspectRatio="none"
      >
        {packetList.map((pkt) => {
          const { sourcePos: p0, targetPos: p1, type, state, id } = pkt;

          // Arc calculation based on distance
          const dx = p1.x - p0.x;
          const dy = p1.y - p0.y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          const arcLift = Math.min(80, Math.max(30, distance * 0.12));

          const pc = {
            x: (p0.x + p1.x) / 2 - dy * 0.1,
            y: Math.min(p0.y, p1.y) - arcLift,
          };

          const trackColor =
            type === "COMMAND"
              ? "#38BDF8"
              : type === "ACKNOWLEDGEMENT"
              ? "#10B981"
              : type === "REPORT"
              ? "#D4AF37"
              : "#94A3B8";

          const isDocked = state === "DOCKED";

          return (
            <g key={`track-${id}`}>
              {/* Dynamic Trajectory Arc (Clean vector without GPU filter raster stalls) */}
              <path
                d={`M ${p0.x} ${p0.y} Q ${pc.x} ${pc.y} ${p1.x} ${p1.y}`}
                fill="none"
                stroke={trackColor}
                strokeWidth="1.8"
                strokeDasharray="4,4"
                strokeOpacity="0.85"
              />

              {/* Source Anchor Node */}
              <circle
                cx={p0.x}
                cy={p0.y}
                r="3.5"
                fill={trackColor}
                opacity="0.8"
              />

              {/* Target Anchor Node */}
              <circle
                cx={p1.x}
                cy={p1.y}
                r="3.5"
                fill={trackColor}
                opacity="0.8"
              />

              {isDocked && (
                <circle
                  cx={p1.x}
                  cy={p1.y}
                  r="12"
                  fill="none"
                  stroke={trackColor}
                  strokeWidth="1.5"
                  opacity="0.8"
                  className="animate-ping"
                />
              )}
            </g>
          );
        })}
      </svg>

      {/* Floating Physical Capsules */}
      {packetList.map((pkt) => {
        const { sourcePos: p0, targetPos: p1, progress, state, id } = pkt;
        const dx = p1.x - p0.x;
        const dy = p1.y - p0.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        const arcLift = Math.min(80, Math.max(30, distance * 0.12));

        const pc = {
          x: (p0.x + p1.x) / 2 - dy * 0.1,
          y: Math.min(p0.y, p1.y) - arcLift,
        };

        const t = Math.max(0, Math.min(1, progress));
        const currentX =
          (1 - t) * (1 - t) * p0.x + 2 * (1 - t) * t * pc.x + t * t * p1.x;
        const currentY =
          (1 - t) * (1 - t) * p0.y + 2 * (1 - t) * t * pc.y + t * t * p1.y;

        const isDocked = state === "DOCKED";

        return (
          <div
            key={`capsule-${id}`}
            className="absolute transition-transform duration-100 ease-out -translate-x-1/2 -translate-y-1/2"
            style={{
              left: `${currentX}px`,
              top: `${currentY}px`,
            }}
          >
            <PacketCapsule packet={pkt} isDocked={isDocked} />
          </div>
        );
      })}
    </div>
  );
};
