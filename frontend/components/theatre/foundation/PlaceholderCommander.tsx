"use client";

import React from "react";
import { motion } from "framer-motion";
import { GlassPanel } from "@/components/ui/glass/GlassPanel";
import { GlassInset } from "@/components/ui/glass/GlassInset";
import { surfaceReveal } from "@/lib/motion/variants";

export interface PlaceholderCommanderProps {
  className?: string;
}

export const PlaceholderCommander: React.FC<PlaceholderCommanderProps> = ({
  className = "w-full max-w-xl",
}) => {
  return (
    <motion.div
      variants={surfaceReveal}
      initial="visible"
      animate="visible"
      className={className}
    >
      <GlassPanel
        variant="strong"
        elevation="floating"
        accentBorder="command"
        className="border-sx-border/60"
        header={
          <div className="flex items-center justify-between w-full">
            <div className="flex items-center space-x-2.5">
              <span className="w-2 h-2 rounded-full bg-sx-command shadow-[0_0_8px_rgba(212,175,55,0.6)]" />
              <span className="font-mono text-xs tracking-[0.2em] uppercase text-sx-command-light font-semibold">
                Command Core // Strategic Advisory
              </span>
            </div>
            <span className="font-mono text-[11px] text-sx-text-tertiary">
              COMMAND ADVISOR
            </span>
          </div>
        }
        footer={
          <div className="flex items-center justify-between text-xs font-mono text-sx-text-tertiary">
            <span className="flex items-center space-x-2">
              <span className="w-1.5 h-1.5 rounded-full bg-sx-command/60" />
              <span>DIRECTIVE: GLOBAL INTELLIGENCE SWEEP</span>
            </span>
            <span>PACING: THEATRE REALTIME</span>
          </div>
        }
      >
        <div className="space-y-4">
          <div>
            <h1 className="text-2xl font-semibold tracking-tight text-sx-text-primary">
              Discovery Commander
            </h1>
            <p className="text-sm text-sx-text-secondary mt-1 leading-relaxed">
              Coordinates 5 regional scout workflows, initiates multi-source scraping, and directs verification pipelines for Pakistani academic candidates.
            </p>
          </div>

          <GlassInset subtle className="space-y-2">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-sx-text-tertiary">Operational State</span>
              <span className="text-sx-command-light font-medium">AWAITING MISSION INTAKE</span>
            </div>
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-sx-text-tertiary">Execution Graph</span>
              <span className="text-sx-text-secondary">Autonomous Multi-Agent Intelligence</span>
            </div>
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-sx-text-tertiary">Quota Coverage</span>
              <span className="text-sx-text-secondary">HEC, Bilateral (Europe/Asia/Americas/MENA/Oceania)</span>
            </div>
          </GlassInset>
        </div>
      </GlassPanel>
    </motion.div>
  );
};
