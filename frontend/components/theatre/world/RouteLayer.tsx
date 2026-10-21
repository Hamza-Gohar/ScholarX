"use client";

import React from "react";
import { getSpatialRoutes } from "@/lib/spatial/anchors";
import { MapState } from "@/lib/spatial/types";
import { Region } from "@/lib/types";

export interface RouteLayerProps {
  mapState: MapState;
  focusedRegion?: Region | "Pakistan" | null;
}

export const RouteLayer: React.FC<RouteLayerProps> = ({
  mapState,
  focusedRegion = null,
}) => {
  const routes = getSpatialRoutes();
  const isDormant = mapState === "DORMANT";
  const isMission = mapState === "MISSION";
  const isDossier = mapState === "DOSSIER";

  if (isDormant || isMission || isDossier) {
    return null;
  }

  return (
    <g className="pointer-events-none select-none">
      <defs>
        {/* Route Linear Gradients */}
        <linearGradient id="route-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#10B981" stopOpacity="0.75" />
          <stop offset="60%" stopColor="#38BDF8" stopOpacity="0.6" />
          <stop offset="100%" stopColor="#38BDF8" stopOpacity="0.8" />
        </linearGradient>

        {/* Glow Filter for Particles */}
        <filter id="route-particle-glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      {routes.map((route, idx) => {
        const isFocused = focusedRegion === route.targetRegion;
        const isAnyFocused = Boolean(focusedRegion && focusedRegion !== "Pakistan");
        const opacity = isFocused ? 1 : isAnyFocused ? 0.2 : 0.65;
        const strokeWidth = isFocused ? 2 : 1.2;

        return (
          <g key={route.id} opacity={opacity} className="transition-opacity duration-500">
            {/* Soft Ambient Glow Path */}
            <path
              d={route.pathData}
              fill="none"
              stroke={isFocused ? "#38BDF8" : "url(#route-gradient)"}
              strokeWidth={strokeWidth + 2}
              opacity={isFocused ? 0.35 : 0.15}
            />

            {/* Base Dashed Trajectory Arc */}
            <path
              id={`path-${route.id}`}
              d={route.pathData}
              fill="none"
              stroke="url(#route-gradient)"
              strokeWidth={strokeWidth}
              strokeDasharray={isFocused ? "6 4" : "4 4"}
            />

            {/* Traveling Energy Packet Particle along the Arc */}
            <circle r={isFocused ? "4" : "3"} fill="#FFFFFF" filter="url(#route-particle-glow)">
              <animateMotion
                dur={`${2.4 + idx * 0.4}s`}
                repeatCount="indefinite"
                path={route.pathData}
                keyPoints="0;1"
                keyTimes="0;1"
              />
            </circle>

            {/* Subtle Echo Particle */}
            <circle
              r="2"
              fill={isFocused ? "#38BDF8" : "#10B981"}
              opacity="0.6"
            >
              <animateMotion
                dur={`${2.4 + idx * 0.4}s`}
                begin={`${0.3 + idx * 0.1}s`}
                repeatCount="indefinite"
                path={route.pathData}
                keyPoints="0;1"
                keyTimes="0;1"
              />
            </circle>
          </g>
        );
      })}
    </g>
  );
};
