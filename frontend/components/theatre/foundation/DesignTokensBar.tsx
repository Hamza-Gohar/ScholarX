"use client";

import React from "react";

export const DesignTokensBar: React.FC = () => {
  const tokens = [
    { label: "COMMAND", color: "bg-sx-command", text: "text-sx-command-light", desc: "Authority & Orchestration" },
    { label: "FLOW", color: "bg-sx-flow", text: "text-sx-flow-light", desc: "Data Transfer & Queries" },
    { label: "VERIFIED", color: "bg-sx-verified", text: "text-emerald-400", desc: "Evidence & Eligibility Pass" },
    { label: "WARNING", color: "bg-sx-warning", text: "text-amber-400", desc: "Deadline & Cost Risk" },
    { label: "CHALLENGE", color: "bg-sx-challenge", text: "text-rose-400", desc: "Skeptic Adversarial Audit" },
  ];

  return (
    <div className="flex items-center justify-between w-full px-8 py-3 border-t border-white/[0.04] bg-black/30 backdrop-blur-md z-theatre-system">
      <div className="flex items-center space-x-6">
        <span className="text-[11px] font-mono tracking-widest text-sx-text-tertiary uppercase">
          SEMANTIC TOKENS:
        </span>
        <div className="flex items-center space-x-5">
          {tokens.map((t) => (
            <div key={t.label} className="flex items-center space-x-2">
              <span className={`w-2 h-2 rounded-full ${t.color}`} />
              <span className={`text-[11px] font-mono tracking-wider uppercase font-semibold ${t.text}`}>
                {t.label}
              </span>
              <span className="text-[10px] text-sx-text-quaternary hidden md:inline">
                ({t.desc})
              </span>
            </div>
          ))}
        </div>
      </div>

      <div className="text-[11px] font-mono text-sx-text-quaternary">
        STAGE COORDINATE SYSTEM // 1920x1080 TARGET
      </div>
    </div>
  );
};
