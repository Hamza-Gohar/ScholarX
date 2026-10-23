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

      {/* Ambient spatial haze in upper command/world zone (Zero-cost GPU gradient without blur filter) */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse 900px 500px at 50% -5%, rgba(56, 189, 248, 0.13) 0%, rgba(14, 116, 144, 0.06) 40%, rgba(5, 7, 10, 0) 75%)",
        }}
      />

      {/* Depth anchor in lower world stage (Zero-cost GPU gradient without blur filter) */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse 1000px 450px at 50% 105%, rgba(212, 175, 55, 0.08) 0%, rgba(30, 41, 59, 0.04) 45%, rgba(5, 7, 10, 0) 75%)",
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
