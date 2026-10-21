"use client";

import React, { useMemo } from "react";
import { motion } from "framer-motion";
import { geoPath, geoGraticule } from "d3-geo";
import { feature } from "topojson-client";
import worldData from "world-atlas/countries-110m.json";
import {
  STAGE_WIDTH,
  STAGE_HEIGHT,
  worldProjection,
} from "@/lib/spatial/coordinates";
import { REGIONAL_ANCHORS } from "@/lib/spatial/anchors";
import {
  MapState,
  CameraShot,
} from "@/lib/spatial/types";
import { getCameraTransformForFocus } from "@/lib/spatial/camera";
import { PakistanOrigin } from "./PakistanOrigin";
import { RegionalAnchor } from "./RegionalAnchor";
import { RouteLayer } from "./RouteLayer";
import { Region } from "@/lib/types";

export interface WorldStageProps {
  mapState?: MapState;
  cameraShot?: CameraShot;
  focusedRegion?: Region | "Pakistan" | null;
  onSelectRegion?: (region: Region) => void;
  className?: string;
}

export const WorldStage: React.FC<WorldStageProps> = ({
  mapState = "DEPLOYMENT",
  cameraShot = "DEPLOYMENT",
  focusedRegion = null,
  onSelectRegion,
  className = "",
}) => {
  // Generate Geo Path from projection
  const pathGenerator = useMemo(
    () => geoPath().projection(worldProjection),
    []
  );

  // Extract TopoJSON country features
  const countries = useMemo(() => {
    // @ts-ignore
    const countriesFeature = feature(worldData as any, worldData.objects.countries);
    // @ts-ignore
    return countriesFeature.features || [];
  }, []);

  // Subtle graticule grid lines
  const graticuleLines = useMemo(() => {
    const graticule = geoGraticule().step([30, 30]);
    return pathGenerator(graticule());
  }, [pathGenerator]);

  // Compute 2D Camera Transform based on current shot and focus
  const camera = useMemo(
    () => getCameraTransformForFocus(cameraShot, focusedRegion, mapState),
    [cameraShot, focusedRegion, mapState]
  );

  const isDormant = mapState === "DORMANT";
  const isDossier = mapState === "DOSSIER";

  return (
    <div
      className={`absolute inset-0 w-full h-full overflow-hidden z-theatre-world flex items-center justify-center ${className}`}
      id="scholarx-world-stage"
    >
      <motion.div
        className="w-full h-full flex items-center justify-center origin-center"
        animate={{
          x: camera.x,
          y: camera.y,
          scale: camera.scale,
          opacity: camera.opacity,
        }}
        transition={{
          duration: 0.9,
          ease: [0.16, 1, 0.3, 1], // Smooth cinematic camera easing
        }}
      >
        <svg
          viewBox={`0 0 ${STAGE_WIDTH} ${STAGE_HEIGHT}`}
          className="w-full h-full select-none"
          preserveAspectRatio="xMidYMid meet"
        >
          <defs>
            {/* Luminous Landmass Shadow & Elevation */}
            <filter id="landmass-shadow" x="-5%" y="-5%" width="110%" height="110%">
              <feDropShadow dx="0" dy="2" stdDeviation="3" floodColor="#000000" floodOpacity="0.8" />
              <feDropShadow dx="0" dy="0" stdDeviation="6" floodColor="#38BDF8" floodOpacity="0.3" />
            </filter>

            {/* Rich Ocean Ambient Radial Glow */}
            <radialGradient
              id="world-stage-haze"
              cx="50%"
              cy="48%"
              r="68%"
              fx="50%"
              fy="45%"
            >
              <stop offset="0%" stopColor="#1E3F6F" stopOpacity="0.95" />
              <stop offset="35%" stopColor="#142C52" stopOpacity="0.85" />
              <stop offset="70%" stopColor="#0D1E38" stopOpacity="0.75" />
              <stop offset="100%" stopColor="#060C16" stopOpacity="0.55" />
            </radialGradient>

            {/* Clean Luminous Landmass Fill Gradient */}
            <linearGradient id="landmass-fill" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#2A4A76" />
              <stop offset="50%" stopColor="#203A60" />
              <stop offset="100%" stopColor="#172C4C" />
            </linearGradient>

            {/* Pakistan Origin Highlight Fill */}
            <linearGradient id="pakistan-highlight-fill" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#059669" />
              <stop offset="50%" stopColor="#10B981" />
              <stop offset="100%" stopColor="#047857" />
            </linearGradient>
          </defs>

          {/* Ocean Radial Illumination */}
          <rect
            width={STAGE_WIDTH}
            height={STAGE_HEIGHT}
            fill="url(#world-stage-haze)"
            opacity={isDormant ? 0.75 : isDossier ? 0.6 : 1.0}
          />

          {/* Graticule Latitude/Longitude Structure */}
          {!isDossier && graticuleLines && (
            <path
              d={graticuleLines}
              fill="none"
              stroke="rgba(56, 189, 248, 0.22)"
              strokeWidth="0.9"
              strokeDasharray="3 5"
            />
          )}

          {/* World Landmasses */}
          <g id="world-landmasses" filter="url(#landmass-shadow)" className="transition-opacity duration-700">
            {countries.map((geo: any, idx: number) => {
              const d = pathGenerator(geo);
              if (!d) return null;

              const isPakistan = geo.id === "586" || geo.id === 586;

              return (
                <path
                  key={geo.id || idx}
                  d={d}
                  fill={
                    isPakistan
                      ? "url(#pakistan-highlight-fill)"
                      : isDormant
                      ? "#1A2B42"
                      : "url(#landmass-fill)"
                  }
                  stroke={
                    isPakistan
                      ? "#34D399"
                      : isDormant
                      ? "rgba(125, 211, 252, 0.40)"
                      : "rgba(125, 211, 252, 0.70)"
                  }
                  strokeWidth={isPakistan ? "2.4" : isDormant ? "1.0" : "1.25"}
                  className="transition-colors duration-300 hover:fill-[#325688] hover:stroke-cyan-200"
                />
              );
            })}
          </g>

          {/* Dynamic Curved Route Flight Arcs (Pakistan -> Destinations) */}
          <RouteLayer mapState={mapState} focusedRegion={focusedRegion} />

          {/* Regional Destination Anchors */}
          <g id="regional-anchors">
            {(Object.keys(REGIONAL_ANCHORS) as Region[]).map((reg) => (
              <RegionalAnchor
                key={reg}
                anchor={REGIONAL_ANCHORS[reg]}
                mapState={mapState}
                isFocused={focusedRegion === reg}
                onSelect={() => onSelectRegion?.(reg)}
              />
            ))}
          </g>

          {/* Pakistan Mission Origin Anchor */}
          <PakistanOrigin
            mapState={mapState}
            isFocused={focusedRegion === "Pakistan"}
          />
        </svg>
      </motion.div>
    </div>
  );
};
