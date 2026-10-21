"use client";

import React from "react";
import { motion } from "framer-motion";
import { useCommandStore } from "@/lib/store";
import { Sliders, Filter } from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { Region } from "@/lib/types";

export const JudgeControlBar: React.FC = () => {
  const {
    judgeParams,
    setJudgeParams,
    redeployWithModifier,
    setOverlayView,
    addVisualMessage,
    updateCommanderDirective,
  } = useCommandStore();

  const handleToggleFullFunding = () => {
    sound.playClick();
    const nextVal = !judgeParams.fullFundingOnly;
    setJudgeParams({ fullFundingOnly: nextVal });

    addVisualMessage({
      from: "JUDGE / EVALUATOR",
      to: "COMMANDER",
      type: "COMMAND",
      title: "CONSTRAINT OVERRIDE",
      summary: nextVal ? "MANDATE: Full Funding Only" : "ALLOW: Partial / Tuition-Only",
    });

    updateCommanderDirective(
      nextVal
        ? "Constraint changed: FULL FUNDING MANDATED // Re-evaluating candidate pool"
        : "Constraint changed: ALL FUNDING TIERS PERMITTED // Expanding search vectors"
    );

    redeployWithModifier();
  };

  const handleToggleEuropeOnly = () => {
    sound.playClick();
    const isEuropeOnly =
      judgeParams.activeRegions.Europe &&
      !judgeParams.activeRegions.Asia &&
      !judgeParams.activeRegions.Americas &&
      !judgeParams.activeRegions.MENA &&
      !judgeParams.activeRegions.Oceania;

    const nextRegions: Record<Region, boolean> = isEuropeOnly
      ? { Europe: true, Asia: true, Americas: true, MENA: true, Oceania: true }
      : { Europe: true, Asia: false, Americas: false, MENA: false, Oceania: false };

    setJudgeParams({ activeRegions: nextRegions });

    addVisualMessage({
      from: "JUDGE / EVALUATOR",
      to: "COMMANDER",
      type: "COMMAND",
      title: "REGIONAL FOCUS OVERRIDE",
      summary: isEuropeOnly ? "DEPLOY ALL 5 REGIONS" : "FOCUS EXCLUSIVELY ON EUROPE",
    });

    updateCommanderDirective(
      isEuropeOnly
        ? "Constraint changed: GLOBAL FLEET RESTORED // Re-dispatching 5 regional scouts"
        : "Constraint changed: EUROPE FOCUS RESTRICTED // Re-routing all compute to Europe"
    );

    redeployWithModifier();
  };

  const handleToggleNoIelts = () => {
    sound.playClick();
    const nextVal = !judgeParams.ieltsRequired;
    setJudgeParams({ ieltsRequired: nextVal });

    addVisualMessage({
      from: "JUDGE / EVALUATOR",
      to: "COMMANDER",
      type: "COMMAND",
      title: "LANGUAGE CRITERIA OVERRIDE",
      summary: nextVal ? "REQUIRE STRICT IELTS EXAM" : "ACCEPT PAKISTANI MOI (NO IELTS)",
    });

    updateCommanderDirective(
      nextVal
        ? "Constraint changed: STRICT IELTS ENFORCED // Filtering non-compliant programs"
        : "Constraint changed: ENGLISH MEDIUM ACCEPTED // Prioritizing MOI waiver programs"
    );

    redeployWithModifier();
  };

  const isEuropeOnly =
    judgeParams.activeRegions.Europe &&
    !judgeParams.activeRegions.Asia &&
    !judgeParams.activeRegions.Americas &&
    !judgeParams.activeRegions.MENA &&
    !judgeParams.activeRegions.Oceania;

  return (
    <motion.div
      initial={{ y: 20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      className="fixed bottom-3 right-4 z-40 flex items-center space-x-2 px-3.5 py-1.5 rounded-full glass-console border-white/15 shadow-2xl font-mono text-[9px] pointer-events-auto"
    >
      <div className="flex items-center space-x-1 text-theatre-muted border-r border-white/10 pr-2 mr-1">
        <Filter className="w-3 h-3 text-command-gold" />
        <span className="font-bold text-white uppercase tracking-wider">JUDGE MODE (§30)</span>
      </div>

      {/* Quick Toggle 1: Full Funding Only */}
      <button
        onClick={handleToggleFullFunding}
        className={`px-2.5 py-1 rounded-full border transition-all ${
          judgeParams.fullFundingOnly
            ? "bg-pakistan-emerald/20 border-pakistan-emerald text-pakistan-emerald font-bold"
            : "bg-white/5 border-white/10 text-theatre-muted hover:text-white"
        }`}
      >
        FULL FUNDING {judgeParams.fullFundingOnly ? "✓" : "○"}
      </button>

      {/* Quick Toggle 2: Europe Only */}
      <button
        onClick={handleToggleEuropeOnly}
        className={`px-2.5 py-1 rounded-full border transition-all ${
          isEuropeOnly
            ? "bg-cyber-cyan/20 border-cyber-cyan text-cyber-cyan font-bold"
            : "bg-white/5 border-white/10 text-theatre-muted hover:text-white"
        }`}
      >
        EUROPE ONLY {isEuropeOnly ? "✓" : "○"}
      </button>

      {/* Quick Toggle 3: No IELTS (MOI Accepted) */}
      <button
        onClick={handleToggleNoIelts}
        className={`px-2.5 py-1 rounded-full border transition-all ${
          !judgeParams.ieltsRequired
            ? "bg-command-gold/20 border-command-gold text-command-gold font-bold"
            : "bg-white/5 border-white/10 text-theatre-muted hover:text-white"
        }`}
      >
        NO IELTS {(!judgeParams.ieltsRequired) ? "✓" : "○"}
      </button>

      {/* Advanced Modifier Launcher */}
      <button
        onClick={() => {
          sound.playClick();
          setOverlayView("MODIFIER");
        }}
        className="p-1 rounded-full hover:bg-white/10 text-white/50 hover:text-white transition-colors ml-1"
        title="Open Full Parameter Modifier"
      >
        <Sliders className="w-3.5 h-3.5" />
      </button>
    </motion.div>
  );
};
