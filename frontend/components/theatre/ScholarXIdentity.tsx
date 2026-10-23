"use client";

import React from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { softPulse } from "@/lib/motion/variants";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface ScholarXIdentityProps {
  className?: string;
  actionSlot?: React.ReactNode;
}

export const ScholarXIdentity: React.FC<ScholarXIdentityProps> = ({
  className,
  actionSlot,
}) => {
  return (
    <div
      className={twMerge(
        clsx(
          "flex items-center justify-between w-full px-3 sm:px-6 md:px-8 py-2.5 sm:py-3.5 pt-safe z-theatre-system pointer-events-auto border-b border-white/[0.06] bg-black/40 backdrop-blur-md",
          className
        )
      )}
    >
      {/* Brand & Mission Statement */}
      <div className="flex items-center space-x-2.5 sm:space-x-4 min-w-0">
        <div className="flex flex-col min-w-0">
          <div className="flex items-center space-x-2 sm:space-x-2.5">
            <span className="text-lg sm:text-2xl font-bold tracking-[0.14em] sm:tracking-[0.18em] text-white uppercase font-sans">
              ScholarX
            </span>
            <span className="px-2 py-0.5 rounded text-[9px] sm:text-[10px] font-mono tracking-wider uppercase border border-amber-500/30 bg-amber-500/10 text-amber-300 font-semibold shadow-[0_0_10px_rgba(245,158,11,0.2)] shrink-0">
              Theatre
            </span>
          </div>
          <span className="text-[10px] sm:text-xs font-mono tracking-[0.1em] sm:tracking-[0.2em] text-zinc-400 uppercase mt-0.5 font-medium truncate max-w-[170px] xs:max-w-[240px] sm:max-w-none">
            Autonomous Scholarship AI
          </span>
        </div>
      </div>

      {/* Action Slot & Stage Status Indicator */}
      <div className="flex items-center space-x-2 sm:space-x-3 shrink-0">
        {actionSlot}

        <Link
          href="/catalog"
          className="flex items-center space-x-1 px-2.5 sm:px-3 py-1.5 rounded-full border border-cyan-500/30 bg-cyan-950/40 hover:bg-cyan-900/60 text-cyan-300 hover:text-white text-xs font-mono tracking-wider transition-all"
          title="Browse 310+ International Scholarships Directory"
        >
          <span className="hidden xs:inline">Directory</span>
          <span className="xs:hidden">Dir</span>
          <span className="text-cyan-400 font-bold">(310)</span>
        </Link>

        <div className="hidden sm:flex items-center space-x-2 px-3 py-1.5 rounded-full border border-white/[0.08] bg-black/40 backdrop-blur-md">
          <motion.span
            variants={softPulse}
            animate="active"
            className="w-1.5 h-1.5 rounded-full bg-sx-verified"
          />
          <span className="text-xs font-mono tracking-wider text-sx-text-secondary uppercase">
            Active
          </span>
        </div>
      </div>
    </div>
  );
};

