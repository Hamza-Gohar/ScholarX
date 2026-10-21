"use client";

import React from "react";
import { MapState, CameraShot } from "@/lib/spatial/types";
import { Region } from "@/lib/types";

export interface MapStateControllerProps {
  currentMapState: MapState;
  currentCameraShot: CameraShot;
  focusedRegion: Region | "Pakistan" | null;
  onSetMapState: (state: MapState) => void;
  onSetCameraShot: (shot: CameraShot) => void;
  onSetFocusedRegion: (region: Region | "Pakistan" | null) => void;
}

export const MapStateController: React.FC<MapStateControllerProps> = ({
  currentMapState,
  currentCameraShot,
  focusedRegion,
  onSetMapState,
  onSetCameraShot,
  onSetFocusedRegion,
}) => {
  const mapStates: { state: MapState; label: string; desc: string }[] = [
    { state: "DORMANT", label: "DORMANT", desc: "Quiet World" },
    { state: "MISSION", label: "MISSION", desc: "Pakistan Active" },
    { state: "DEPLOYMENT", label: "DEPLOYMENT", desc: "5 Regional Routes" },
    { state: "RESEARCH", label: "RESEARCH", desc: "Europe Focus" },
    { state: "EVIDENCE", label: "EVIDENCE", desc: "Hungary Focus" },
    { state: "DOSSIER", label: "DOSSIER", desc: "Map Recedes" },
  ];

  const handleStateClick = (state: MapState) => {
    onSetMapState(state);
    if (state === "DORMANT") {
      onSetCameraShot("GLOBAL");
      onSetFocusedRegion(null);
    } else if (state === "MISSION") {
      onSetCameraShot("GLOBAL");
      onSetFocusedRegion("Pakistan");
    } else if (state === "DEPLOYMENT") {
      onSetCameraShot("DEPLOYMENT");
      onSetFocusedRegion(null);
    } else if (state === "RESEARCH") {
      onSetCameraShot("REGIONAL");
      onSetFocusedRegion("Europe");
    } else if (state === "EVIDENCE") {
      onSetCameraShot("EVIDENCE");
      onSetFocusedRegion("Europe");
    } else if (state === "DOSSIER") {
      onSetCameraShot("DOSSIER");
      onSetFocusedRegion(null);
    }
  };

  return (
    <div className="flex items-center space-x-2 px-3 py-1.5 rounded-full border border-white/[0.08] bg-black/60 backdrop-blur-xl z-theatre-system select-none pointer-events-auto shadow-2xl">
      <span className="text-[10px] font-mono tracking-widest text-sx-text-tertiary uppercase pl-2 pr-1 border-r border-white/10">
        STAGE:
      </span>

      <div className="flex items-center space-x-1">
        {mapStates.map(({ state, label }) => {
          const isActive = currentMapState === state;
          return (
            <button
              key={state}
              onClick={() => handleStateClick(state)}
              className={`px-2.5 py-1 rounded-full text-[10.5px] font-mono tracking-wider transition-all ${
                isActive
                  ? "bg-sx-flow/20 text-sx-flow-light border border-sx-flow/40 shadow-[0_0_12px_rgba(56,189,248,0.25)] font-bold"
                  : "text-sx-text-secondary hover:text-sx-text-primary hover:bg-white/5 border border-transparent"
              }`}
            >
              {label}
            </button>
          );
        })}
      </div>
    </div>
  );
};
