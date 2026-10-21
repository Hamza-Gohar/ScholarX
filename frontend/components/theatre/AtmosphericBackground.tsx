"use client";

import React from "react";

export const AtmosphericBackground: React.FC = () => {
  return (
    <div
      className="absolute inset-0 pointer-events-none overflow-hidden z-theatre-atmosphere"
      aria-hidden="true"
    >
      {/* Base Obsidian Foundation */}
      <div className="absolute inset-0 bg-[#05070A]" />

      {/* Ambient spatial haze in upper command/world zone */}
      <div
        className="absolute top-[-10%] left-1/2 -translate-x-1/2 w-[1200px] h-[700px] rounded-full blur-[140px] opacity-[0.14]"
        style={{
          background:
            "radial-gradient(circle, rgba(56, 189, 248, 0.85) 0%, rgba(14, 116, 144, 0.4) 50%, transparent 80%)",
        }}
      />

      {/* Depth anchor in lower world stage */}
      <div
        className="absolute bottom-[-15%] left-1/2 -translate-x-1/2 w-[1400px] h-[500px] rounded-full blur-[160px] opacity-[0.10]"
        style={{
          background:
            "radial-gradient(circle, rgba(212, 175, 55, 0.6) 0%, rgba(30, 41, 59, 0.5) 60%, transparent 80%)",
        }}
      />

      {/* Soft cinematic vignette around viewport borders */}
      <div
        className="absolute inset-0"
        style={{
          background:
            "radial-gradient(ellipse at 50% 50%, transparent 75%, rgba(3, 5, 8, 0.45) 100%)",
        }}
      />
    </div>
  );
};
