"use client";

import React from "react";
import { motion } from "framer-motion";
import { INVESTIGATION_ANCHORS } from "@/lib/investigation/investigationStore";
import { SpecialistType } from "@/lib/investigation/types";

export interface InvestigationConduitsProps {
  activeSpecialist: SpecialistType | null;
  className?: string;
}

export const InvestigationConduits: React.FC<InvestigationConduitsProps> = ({
  activeSpecialist,
  className = "",
}) => {
  const pCommander = INVESTIGATION_ANCHORS.commander;
  const pTarget = INVESTIGATION_ANCHORS.target;
  const pSpecialistStage = INVESTIGATION_ANCHORS.specialistStage;

  return (
    <div className={`absolute inset-0 pointer-events-none z-theatre-routes overflow-visible ${className}`}>
      <svg
        className="w-full h-full absolute inset-0 overflow-visible"
        viewBox="0 0 1920 1080"
        preserveAspectRatio="none"
      >
        <defs>
          <marker
            id="invArrowGreen"
            viewBox="0 0 10 10"
            refX="6"
            refY="5"
            markerWidth="6"
            markerHeight="6"
            orient="auto-start-reverse"
          >
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10B981" opacity="0.9" />
          </marker>
          <marker
            id="invArrowGold"
            viewBox="0 0 10 10"
            refX="6"
            refY="5"
            markerWidth="6"
            markerHeight="6"
            orient="auto-start-reverse"
          >
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#D4AF37" opacity="0.9" />
          </marker>

          <filter id="investigationGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>

          <linearGradient id="cmdToTargetGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#38BDF8" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#10B981" stopOpacity="0.9" />
          </linearGradient>

          <linearGradient id="targetToSpecialistGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#10B981" stopOpacity="0.9" />
            <stop offset="100%" stopColor="#D4AF37" stopOpacity="0.9" />
          </linearGradient>
        </defs>

        {/* 1. Primary Authority Conduit: Commander -> Target with animated flow & arrow */}
        <motion.line
          x1={pCommander.x}
          y1={pCommander.y + 40}
          x2={pTarget.x}
          y2={pTarget.y - 100}
          stroke="url(#cmdToTargetGrad)"
          strokeWidth="2.5"
          strokeDasharray="6,6"
          markerEnd="url(#invArrowGreen)"
          filter="url(#investigationGlow)"
          animate={{
            strokeDashoffset: [0, -48],
            opacity: [0.75, 1, 0.75],
          }}
          transition={{
            strokeDashoffset: { duration: 1.6, repeat: Infinity, ease: "linear" },
            opacity: { duration: 2, repeat: Infinity, ease: "easeInOut" },
          }}
        />

        {/* Traveling pulse on Commander -> Target */}
        <motion.circle
          r="4"
          fill="#10B981"
          filter="drop-shadow(0 0 8px #10B981)"
          animate={{
            cx: [pCommander.x, pTarget.x],
            cy: [pCommander.y + 40, pTarget.y - 100],
            opacity: [0, 1, 1, 0],
          }}
          transition={{
            duration: 1.8,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        />

        {/* 2. Investigation Inquiry Conduit: Target -> Specialist Stage */}
        {activeSpecialist && (
          <>
            <motion.line
              x1={pTarget.x}
              y1={pTarget.y + 110}
              x2={pSpecialistStage.x}
              y2={pSpecialistStage.y - 120}
              stroke="url(#targetToSpecialistGrad)"
              strokeWidth="2.5"
              strokeDasharray="5,5"
              markerEnd="url(#invArrowGold)"
              filter="url(#investigationGlow)"
              animate={{
                strokeDashoffset: [0, -40],
                opacity: [0.8, 1, 0.8],
              }}
              transition={{
                strokeDashoffset: { duration: 1.5, repeat: Infinity, ease: "linear" },
                opacity: { duration: 1.8, repeat: Infinity, ease: "easeInOut" },
              }}
            />

            {/* Traveling pulse on Target -> Specialist */}
            <motion.circle
              r="4"
              fill="#D4AF37"
              filter="drop-shadow(0 0 8px #D4AF37)"
              animate={{
                cx: [pTarget.x, pSpecialistStage.x],
                cy: [pTarget.y + 110, pSpecialistStage.y - 120],
                opacity: [0, 1, 1, 0],
              }}
              transition={{
                duration: 1.6,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 0.3,
              }}
            />
          </>
        )}

        {/* Anchor Pulsing Rings */}
        <circle cx={pTarget.x} cy={pTarget.y} r="5" fill="#10B981" opacity="0.9" />
        <circle cx={pTarget.x} cy={pTarget.y} r="14" fill="none" stroke="#10B981" strokeWidth="1" opacity="0.4" className="animate-ping" />
      </svg>
    </div>
  );
};
