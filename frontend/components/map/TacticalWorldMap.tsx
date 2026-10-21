"use client";

import React, { useMemo } from "react";
import { geoEquirectangular, geoPath } from "d3-geo";
import { feature } from "topojson-client";
import worldData from "world-atlas/countries-110m.json";
import { useCommandStore } from "@/lib/store";
import { Region } from "@/lib/types";
import { sound } from "@/lib/sound-fx";

// Key Geocoordinates [longitude, latitude]
const COORDS = {
  PAKISTAN: [69.3451, 30.3753] as [number, number],
  EUROPE: [13.405, 52.52] as [number, number], // Berlin / Central EU
  ASIA: [116.4074, 39.9042] as [number, number], // Beijing / East Asia
  AMERICAS: [-77.0369, 38.9072] as [number, number], // Washington
  MENA: [46.6753, 24.7136] as [number, number], // Riyadh / Gulf
  OCEANIA: [149.13, -35.2809] as [number, number], // Canberra
};

const REGION_HUBS: Record<Region, [number, number]> = {
  Europe: COORDS.EUROPE,
  Asia: COORDS.ASIA,
  Americas: COORDS.AMERICAS,
  MENA: COORDS.MENA,
  Oceania: COORDS.OCEANIA,
};

export const TacticalWorldMap: React.FC = () => {
  const {
    scouts,
    candidates,
    setSelectedScholarship,
    setOverlayView,
    mapVisualMode,
  } = useCommandStore();

  const width = 1000;
  const height = 540;

  // D3 Geo Projection for 16:9 panoramic tactical display
  const projection = useMemo(() => {
    return geoEquirectangular()
      .scale(158)
      .translate([width / 2, height / 2 + 30]);
  }, [width, height]);

  const pathGenerator = useMemo(() => geoPath().projection(projection), [projection]);

  // Extract land features
  const countries = useMemo(() => {
    // @ts-ignore
    const countriesFeature = feature(worldData as any, worldData.objects.countries);
    // @ts-ignore
    return countriesFeature.features || [];
  }, []);

  const pakistanProjected = useMemo(
    () => projection(COORDS.PAKISTAN) || [width / 2, height / 2],
    [projection, width, height]
  );

  // Generate curved flight arcs from Pakistan to each active scout
  const activeArcs = useMemo(() => {
    return (Object.keys(REGION_HUBS) as Region[]).map((region) => {
      const dest = projection(REGION_HUBS[region]);
      if (!dest) return null;

      const [x1, y1] = pakistanProjected;
      const [x2, y2] = dest;

      // Calculate control point for high-arching bezier
      const dx = x2 - x1;
      const dy = y2 - y1;
      const cx = (x1 + x2) / 2 - dy * 0.22;
      const cy = (y1 + y2) / 2 + dx * 0.15 - 45;

      const pathData = `M ${x1} ${y1} Q ${cx} ${cy} ${x2} ${y2}`;
      const isActive = scouts[region]?.status !== "IDLE";
      const count = scouts[region]?.itemsFound || 0;

      return {
        region,
        pathData,
        destX: x2,
        destY: y2,
        isActive,
        count,
      };
    }).filter(Boolean);
  }, [scouts, pakistanProjected, projection]);

  return (
    <div className="relative w-full h-full flex items-center justify-center overflow-hidden bg-obsidian-950/80">
      {/* Radar sweep background visual */}
      <div className="absolute inset-0 pointer-events-none flex items-center justify-center opacity-25">
        <div className="w-[620px] h-[620px] rounded-full border border-cyber-cyan/20 animate-pulse-slow" />
        <div className="w-[420px] h-[420px] rounded-full border border-cyber-cyan/15" />
        <div className="w-[220px] h-[220px] rounded-full border border-cyber-cyan/10" />
      </div>

      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="w-full h-full max-h-[700px] select-none"
        preserveAspectRatio="xMidYMid meet"
      >
        <defs>
          <linearGradient id="arcGlow" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#00FF88" stopOpacity="0.9" />
            <stop offset="70%" stopColor="#00F0FF" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#9D4EDD" stopOpacity="0.6" />
          </linearGradient>

          <radialGradient id="beaconGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#00FF88" stopOpacity="1" />
            <stop offset="40%" stopColor="#00FF88" stopOpacity="0.5" />
            <stop offset="100%" stopColor="#00FF88" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Tactical Latitude/Longitude Coordinate Grid */}
        <g className="stroke-white/[0.04] stroke-[0.5] fill-none">
          {[-60, -30, 0, 30, 60].map((lat) => (
            <line
              key={`lat-${lat}`}
              x1={0}
              y1={projection([0, lat])?.[1] || 0}
              x2={width}
              y2={projection([0, lat])?.[1] || 0}
              strokeDasharray="4 6"
            />
          ))}
          {[-120, -60, 0, 60, 120].map((lon) => (
            <line
              key={`lon-${lon}`}
              x1={projection([lon, 0])?.[0] || 0}
              y1={0}
              x2={projection([lon, 0])?.[0] || 0}
              y2={height}
              strokeDasharray="4 6"
            />
          ))}
        </g>

        {/* Land Masses */}
        <g className="fill-[#1F3759] stroke-[#38BDF8]/60 stroke-[1.1]">
          {countries.map((country: any, idx: number) => {
            const isPakistan = country.id === "586";
            return (
              <path
                key={`cntry-${idx}`}
                d={pathGenerator(country) || ""}
                className={`transition-colors duration-500 ${
                  isPakistan
                    ? "fill-pakistan-deep/80 stroke-pakistan-emerald/80 stroke-[1.5]"
                    : "hover:fill-obsidian-800"
                }`}
              />
            );
          })}
        </g>

        {/* Dynamic Curved Vector Flight Arcs (Active in DEPLOYMENT & DISCOVERY modes) */}
        {mapVisualMode !== "INTELLIGENCE" &&
          activeArcs.map((arc) => {
            if (!arc) return null;
            return (
              <g key={`arc-${arc.region}`}>
                <path
                  d={arc.pathData}
                  fill="none"
                  stroke={arc.isActive ? "url(#arcGlow)" : "rgba(255, 255, 255, 0.08)"}
                  strokeWidth={arc.isActive ? 2 : 1}
                  strokeDasharray={arc.isActive ? "6 4" : "2 4"}
                  className={arc.isActive ? "opacity-90" : "opacity-30"}
                />

                {arc.isActive && (
                  <path
                    d={arc.pathData}
                    fill="none"
                    stroke="#00F0FF"
                    strokeWidth={3}
                    strokeDasharray="12 180"
                    className="animate-pulse"
                  >
                    <animate
                      attributeName="stroke-dashoffset"
                      values="192;0"
                      dur="2.5s"
                      repeatCount="indefinite"
                    />
                  </path>
                )}

                <circle
                  cx={arc.destX}
                  cy={arc.destY}
                  r={arc.isActive ? 5 : 3}
                  className={arc.isActive ? "fill-cyber-cyan" : "fill-white/30"}
                />
                <circle
                  cx={arc.destX}
                  cy={arc.destY}
                  r={arc.isActive ? 12 : 6}
                  fill="none"
                  stroke={arc.isActive ? "#00F0FF" : "transparent"}
                  strokeWidth={0.75}
                  className={arc.isActive ? "animate-ping opacity-60" : ""}
                />
                <text
                  x={arc.destX}
                  y={arc.destY - 10}
                  textAnchor="middle"
                  className="fill-cyber-cyan/80 text-[10px] font-mono tracking-wider font-semibold pointer-events-none"
                >
                  {arc.region.toUpperCase()} {arc.count > 0 ? `(${arc.count})` : ""}
                </text>
              </g>
            );
          })}

        {/* Pakistan Mission Origin Beacon */}
        <g>
          <circle
            cx={pakistanProjected[0]}
            cy={pakistanProjected[1]}
            r={24}
            fill="url(#beaconGlow)"
            className="animate-pulse"
          />
          <circle
            cx={pakistanProjected[0]}
            cy={pakistanProjected[1]}
            r={16}
            fill="none"
            stroke="#00FF88"
            strokeWidth={1}
            className="animate-ping"
          />
          <circle
            cx={pakistanProjected[0]}
            cy={pakistanProjected[1]}
            r={5}
            className="fill-pakistan-emerald shadow-glow-emerald"
          />
          <text
            x={pakistanProjected[0]}
            y={pakistanProjected[1] + 16}
            textAnchor="middle"
            className="fill-pakistan-emerald font-mono text-[10px] font-bold tracking-widest pointer-events-none drop-shadow"
          >
            ORIGIN: PAKISTAN
          </text>
        </g>

        {/* Candidate Pins (Recent 12 or High-Value Opportunities) */}
        {candidates.slice(0, 16).map((c, i) => {
          const hub = REGION_HUBS[c.region] || COORDS.EUROPE;
          const jitterX = Math.sin(i * 1.5) * 45;
          const jitterY = Math.cos(i * 1.5) * 35;
          const pinPos = projection(hub) || [0, 0];
          const px = pinPos[0] + jitterX;
          const py = pinPos[1] + jitterY;

          const isHec = c.pakistan_requirements.pakistan_bilateral_quota;

          return (
            <g
              key={c.scholarship_id}
              className="cursor-pointer group"
              onClick={() => {
                sound.playClick();
                setSelectedScholarship(c);
                setOverlayView("AUDIT");
              }}
            >
              <circle
                cx={px}
                cy={py}
                r={isHec ? 5 : 4}
                className={`${
                  isHec ? "fill-pakistan-emerald" : "fill-cyber-cyan"
                } group-hover:scale-125 transition-transform`}
              />
              <circle
                cx={px}
                cy={py}
                r={isHec ? 12 : 8}
                fill="none"
                stroke={isHec ? "#00FF88" : "#00F0FF"}
                strokeWidth={0.75}
                className="group-hover:stroke-pakistan-emerald transition-colors opacity-70 animate-ping"
              />

              {/* In INTELLIGENCE mode, display rich callout labels */}
              {mapVisualMode === "INTELLIGENCE" && (
                <g className="pointer-events-none">
                  <rect
                    x={px - 40}
                    y={py - 22}
                    width={80}
                    height={16}
                    rx={3}
                    fill="rgba(5, 11, 20, 0.85)"
                    stroke={isHec ? "#00FF88" : "#00F0FF"}
                    strokeWidth={0.5}
                  />
                  <text
                    x={px}
                    y={py - 11}
                    textAnchor="middle"
                    className="fill-white font-mono text-[8px] font-bold tracking-tight"
                  >
                    {c.confidence_score || 94}% {c.name.substring(0, 9)}..
                  </text>
                </g>
              )}

              <title>{`${c.name} (${c.host_country_name}) - Match: ${c.confidence_score || 94}%`}</title>
            </g>
          );
        })}
      </svg>

      {/* Floating Tactical Coordinates Overlay */}
      <div className="absolute top-3 left-4 font-mono text-[9px] text-cyber-cyan/60 pointer-events-none space-y-0.5">
        <div>PROJECTION: EQUIRECTANGULAR // D3-GEO</div>
        <div>ORIGIN_COORD: 30.3753° N, 69.3451° E (PAKISTAN)</div>
        <div>TACTICAL_MODE: {mapVisualMode}</div>
      </div>
    </div>
  );
};
