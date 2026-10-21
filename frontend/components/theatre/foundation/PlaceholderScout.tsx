"use client";

import React from "react";
import { motion } from "framer-motion";
import { GlassPanel } from "@/components/ui/glass/GlassPanel";
import { GlassInset } from "@/components/ui/glass/GlassInset";
import { surfaceReveal } from "@/lib/motion/variants";

import { Region } from "@/lib/types";

export interface PlaceholderScoutProps {
  className?: string;
  region?: Region;
}

export const PlaceholderScout: React.FC<PlaceholderScoutProps> = ({
  className = "w-full max-w-lg",
  region = "Europe",
}) => {
  return (
    <motion.div
      variants={surfaceReveal}
      initial="visible"
      animate="visible"
      transition={{ delay: 0.15 }}
      className={className}
    >
      <GlassPanel
        variant="default"
        elevation="elevated"
        accentBorder="flow"
        className="border-sx-border/50"
        header={
          <div className="flex items-center justify-between w-full">
            <div className="flex items-center space-x-2.5">
              <span className="w-2 h-2 rounded-full bg-sx-flow shadow-[0_0_8px_rgba(56,189,248,0.6)]" />
              <span className="font-mono text-xs tracking-[0.2em] uppercase text-sx-flow-light font-semibold">
                Regional Fleet // Scout Node
              </span>
            </div>
            <span className="font-mono text-[11px] text-sx-text-tertiary">
              ID: SCOUT-EU
            </span>
          </div>
        }
        footer={
          <div className="flex items-center justify-between text-xs font-mono text-sx-text-tertiary">
            <span className="flex items-center space-x-2">
              <span className="w-1.5 h-1.5 rounded-full bg-sx-flow/60" />
              <span>REGION: EUROPE & UK</span>
            </span>
            <span>TARGET POOL: 69 GRANTS</span>
          </div>
        }
      >
        <div className="space-y-4">
          <div>
            <h2 className="text-xl font-semibold tracking-tight text-sx-text-primary">
              Europe Regional Scout
            </h2>
            <p className="text-sm text-sx-text-secondary mt-1 leading-relaxed">
              Deterministic search, scrape, and extraction pipeline scanning DAAD, Erasmus Mundus, Stipendium Hungaricum, and bilateral European quotas.
            </p>
          </div>

          <GlassInset subtle className="space-y-2">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-sx-text-tertiary">Status</span>
              <span className="text-sx-flow-light font-medium">DISPATCH READY</span>
            </div>
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-sx-text-tertiary">Scrape Targets</span>
              <span className="text-sx-text-secondary">Official Portals & Ministry Feeds</span>
            </div>
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-sx-text-tertiary">Verification Link</span>
              <span className="text-sx-text-secondary">HEC Attestation & IBCC Match</span>
            </div>
          </GlassInset>
        </div>
      </GlassPanel>
    </motion.div>
  );
};
