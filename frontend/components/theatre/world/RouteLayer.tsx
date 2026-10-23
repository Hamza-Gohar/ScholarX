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
      </defs>

      {routes.map((route, idx) => {
        const isFocused = focusedRegion === route.targetRegion;
        const isAnyFocused = Boolean(focusedRegion && focusedRegion !== "Pakistan");
        const opacity = isFocused ? 1 : isAnyFocused ? 0.2 : 0.65;
        const strokeWidth = isFocused ? 2 : 1.2;
        // In high-efficiency rendering, only animate traveling energy on the focused route or primary paths
        const shouldAnimate = !isAnyFocused || isFocused;

        return (
          <g key={route.id} opacity={opacity} className="transition-opacity duration-300">
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

            {/* Traveling Energy Packet Particle (GPU-friendly without software Gaussian filter stalls) */}
            {shouldAnimate && (
              <>
                <circle r={isFocused ? "3.5" : "2.5"} fill="#FFFFFF">
                  <animateMotion
                    dur={`${2.6 + idx * 0.4}s`}
                    repeatCount="indefinite"
                    path={route.pathData}
                    keyPoints="0;1"
                    keyTimes="0;1"
                  />
                </circle>

                {/* Subtle Luminous Trail Particle */}
                <circle
                  r={isFocused ? "2" : "1.5"}
                  fill={isFocused ? "#38BDF8" : "#10B981"}
                  opacity="0.7"
                >
                  <animateMotion
                    dur={`${2.6 + idx * 0.4}s`}
                    begin={`${0.3 + idx * 0.1}s`}
                    repeatCount="indefinite"
                    path={route.pathData}
                    keyPoints="0;1"
                    keyTimes="0;1"
                  />
                </circle>
              </>
            )}
          </g>
        );
      })}
    </g>
  );
};
