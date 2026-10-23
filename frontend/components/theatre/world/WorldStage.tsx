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
import { useDevicePerformance } from "@/lib/hooks/useDevicePerformance";

export interface WorldStageProps {
  mapState?: MapState;
  cameraShot?: CameraShot;
  focusedRegion?: Region | "Pakistan" | null;
  onSelectRegion?: (region: Region) => void;
  className?: string;
  forceMobile?: boolean;
}

export const WorldStage: React.FC<WorldStageProps> = ({
  mapState = "DEPLOYMENT",
  cameraShot = "DEPLOYMENT",
  focusedRegion = null,
  onSelectRegion,
  className = "",
  forceMobile = false,
}) => {
  const { isMobile } = useDevicePerformance();
  const shouldRenderMobile = forceMobile || isMobile;

  // Generate Geo Path from projection
  const pathGenerator = useMemo(
    () => geoPath().projection(worldProjection),
    []
  );

  // Precompute and memoize all SVG country path strings once (only for desktop view)
  const memoizedCountryPaths = useMemo(() => {
    if (shouldRenderMobile) return [];
    // @ts-ignore
    const countriesFeature = feature(worldData as any, worldData.objects.countries);
    // @ts-ignore
    const feats = countriesFeature.features || [];
    return feats
      .map((geo: any, idx: number) => {
        const d = pathGenerator(geo);
        if (!d) return null;
        const isPakistan = geo.id === "586" || geo.id === 586;
        return {
          id: geo.id || `country-${idx}`,
          d,
          isPakistan,
        };
      })
      .filter(Boolean) as { id: string | number; d: string; isPakistan: boolean }[];
  }, [pathGenerator, shouldRenderMobile]);

  // Subtle graticule grid lines
  const graticuleLines = useMemo(() => {
    if (shouldRenderMobile) return null;
    const graticule = geoGraticule().step([30, 30]);
    return pathGenerator(graticule());
  }, [pathGenerator, shouldRenderMobile]);

  // Compute 2D Camera Transform based on current shot and focus
  const camera = useMemo(
    () => getCameraTransformForFocus(cameraShot, focusedRegion, mapState),
    [cameraShot, focusedRegion, mapState]
  );

  const isDormant = mapState === "DORMANT";
  const isDossier = mapState === "DOSSIER";

  // Dedicated Mobile Tactical Radar & Regional Command Hub
  if (shouldRenderMobile) {
    const sectors: { region: Region; label: string; x: number; y: number; seats: number; code: string }[] = [
      { region: "Europe", label: "EUROPE", x: 65, y: 175, seats: 400, code: "EU" },
      { region: "Americas", label: "AMERICAS", x: 105, y: 250, seats: 42, code: "AM" },
      { region: "MENA", label: "MENA", x: 180, y: 260, seats: 27, code: "ME" },
      { region: "Asia", label: "ASIA", x: 255, y: 250, seats: 57, code: "AS" },
      { region: "Oceania", label: "OCEANIA", x: 295, y: 175, seats: 10, code: "OC" },
    ];

    return (
      <div
        className={`absolute inset-0 w-full h-full overflow-hidden z-theatre-world flex items-center justify-center pointer-events-none ${className}`}
        id="scholarx-world-stage-mobile"
      >
        <div className="relative w-full max-w-[420px] aspect-[4/3] flex items-center justify-center pointer-events-auto">
          {/* Mobile Ambient Glow */}
          <div className="absolute inset-0 bg-radial-gradient from-emerald-950/20 via-sky-950/10 to-transparent pointer-events-none" />

          <svg
            viewBox="0 0 360 300"
            className="w-full h-full select-none"
            preserveAspectRatio="xMidYMid meet"
          >
            <defs>
              <linearGradient id="mob-radar-conduit" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#10B981" stopOpacity="0.8" />
                <stop offset="100%" stopColor="#38BDF8" stopOpacity="0.6" />
              </linearGradient>
              <radialGradient id="mob-center-glow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stopColor="#10B981" stopOpacity="0.5" />
                <stop offset="100%" stopColor="#10B981" stopOpacity="0" />
              </radialGradient>
            </defs>

            {/* Radar Circular Range Rings centered on Pakistan [180, 85] */}
            <circle cx="180" cy="85" r="45" fill="none" stroke="rgba(56, 189, 248, 0.12)" strokeWidth="1" strokeDasharray="3 3" />
            <circle cx="180" cy="85" r="90" fill="none" stroke="rgba(56, 189, 248, 0.15)" strokeWidth="1" strokeDasharray="3 3" />
            <circle cx="180" cy="85" r="140" fill="none" stroke="rgba(56, 189, 248, 0.10)" strokeWidth="1" strokeDasharray="4 4" />

            {/* Subtle Crosshair Axis */}
            <line x1="180" y1="20" x2="180" y2="280" stroke="rgba(255, 255, 255, 0.05)" strokeWidth="1" />
            <line x1="20" y1="85" x2="340" y2="85" stroke="rgba(255, 255, 255, 0.05)" strokeWidth="1" />

            {/* Conduits from Pakistan (180, 85) to each Sector */}
            {sectors.map((sec) => {
              const isSelected = focusedRegion === sec.region;
              const path = `M 180 85 Q ${(180 + sec.x) / 2} ${(85 + sec.y) / 2 - 15} ${sec.x} ${sec.y}`;
              return (
                <g key={sec.region}>
                  <path
                    d={path}
                    fill="none"
                    stroke={isSelected ? "#D4AF37" : "url(#mob-radar-conduit)"}
                    strokeWidth={isSelected ? "2" : "1.2"}
                    strokeDasharray={isSelected ? "4 4" : "3 3"}
                    opacity={isSelected ? 0.95 : 0.45}
                  />
                  {isSelected && (
                    <circle cx={sec.x} cy={sec.y} r="14" fill="none" stroke="#D4AF37" strokeWidth="1" opacity="0.6" className="animate-ping" />
                  )}
                </g>
              );
            })}

            {/* Pakistan Center Command Origin */}
            <g
              transform="translate(180, 85)"
              className="cursor-pointer pointer-events-auto"
              onClick={() => onSelectRegion?.("Asia")}
            >
              <circle r="22" fill="url(#mob-center-glow)" />
              <circle r="7" fill="#10B981" stroke="#34D399" strokeWidth="2" className="animate-pulse" />
              <circle r="3" fill="#ffffff" />
              <text y="-14" textAnchor="middle" fill="#34D399" fontSize="9" fontFamily="monospace" fontWeight="bold" letterSpacing="0.1em">
                PAKISTAN COMMAND
              </text>
              <text y="20" textAnchor="middle" fill="rgba(255,255,255,0.6)" fontSize="7" fontFamily="monospace">
                ORIGIN // ISLAMABAD
              </text>
            </g>

            {/* 5 Continental Regional Nodes */}
            {sectors.map((sec) => {
              const isSelected = focusedRegion === sec.region;
              return (
                <g
                  key={sec.region}
                  transform={`translate(${sec.x}, ${sec.y})`}
                  className="cursor-pointer pointer-events-auto transition-transform duration-200"
                  onClick={() => onSelectRegion?.(sec.region)}
                >
                  <circle
                    r={isSelected ? "18" : "14"}
                    fill={isSelected ? "rgba(212, 175, 55, 0.25)" : "rgba(8, 14, 22, 0.85)"}
                    stroke={isSelected ? "#D4AF37" : "rgba(56, 189, 248, 0.4)"}
                    strokeWidth={isSelected ? "2" : "1"}
                  />
                  <text
                    y="3"
                    textAnchor="middle"
                    fill={isSelected ? "#D4AF37" : "#38BDF8"}
                    fontSize="8"
                    fontFamily="monospace"
                    fontWeight="bold"
                  >
                    {sec.code}
                  </text>
                  <text
                    y="18"
                    textAnchor="middle"
                    fill={isSelected ? "#ffffff" : "rgba(255,255,255,0.7)"}
                    fontSize="7"
                    fontFamily="monospace"
                    fontWeight={isSelected ? "bold" : "normal"}
                  >
                    {sec.label}
                  </text>
                  <text
                    y="27"
                    textAnchor="middle"
                    fill="#10B981"
                    fontSize="6"
                    fontFamily="monospace"
                  >
                    {sec.seats} Seats
                  </text>
                </g>
              );
            })}
          </svg>
        </div>
      </div>
    );
  }

  return (
    <div
      className={`absolute inset-0 w-full h-full overflow-hidden z-theatre-world flex items-center justify-center ${className}`}
      id="scholarx-world-stage"
    >
      <motion.div
        className="w-full h-full flex items-center justify-center origin-center"
        style={{ willChange: "transform" }}
        animate={{
          x: camera.x,
          y: camera.y,
          scale: camera.scale,
          opacity: camera.opacity,
        }}
        transition={{
          duration: 0.85,
          ease: [0.16, 1, 0.3, 1], // Smooth cinematic camera easing
        }}
      >
        <svg
          viewBox={`0 0 ${STAGE_WIDTH} ${STAGE_HEIGHT}`}
          className="w-full h-full select-none"
          preserveAspectRatio="xMidYMid meet"
        >
          <defs>
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

          {/* World Landmasses (High-performance vector rendering without software SVG filter stalls) */}
          <g id="world-landmasses" className="transition-opacity duration-500">
            {memoizedCountryPaths.map((item) => {
              const { id, d, isPakistan } = item;

              return (
                <path
                  key={id}
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
                  className="transition-colors duration-200 hover:fill-[#325688] hover:stroke-cyan-200"
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
