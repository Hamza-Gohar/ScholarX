"use client";

import React, { useState } from "react";
import {
  resolveCountryCode,
  resolveCountryName,
  resolveCountryFlag,
} from "@/lib/utils/countryFlags";

export interface CountryFlagLogoProps {
  country?: string | null;
  name?: string | null;
  className?: string;
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  showName?: boolean;
  nameClassName?: string;
}

const SIZE_MAP = {
  xs: { w: 16, h: 11, aspect: "w-4 h-2.5" },
  sm: { w: 20, h: 14, aspect: "w-5 h-3.5" },
  md: { w: 24, h: 17, aspect: "w-6 h-4" },
  lg: { w: 32, h: 22, aspect: "w-8 h-5.5" },
  xl: { w: 40, h: 28, aspect: "w-10 h-7" },
};

/**
 * High-definition Country Flag Logo Badge.
 * Renders authentic, full-color national flag logos across all web browsers
 * and printable PDF documents using FlagCDN vector/raster badges with offline fallback.
 * Eliminates all blank glyphs, monochrome building icons (🏛️), and generic globe emojis.
 */
export const CountryFlagLogo: React.FC<CountryFlagLogoProps> = ({
  country,
  name,
  className = "",
  size = "sm",
  showName = false,
  nameClassName = "text-xs font-mono font-bold text-white/90 uppercase",
}) => {
  const [imgError, setImgError] = useState(false);
  const code = resolveCountryCode(country, name);
  const countryDisplayName = resolveCountryName(country, name);
  const emojiFallback = resolveCountryFlag(country, name);

  const dim = SIZE_MAP[size] || SIZE_MAP.sm;

  const flagContent = (
    <span
      className={`inline-flex items-center justify-center shrink-0 overflow-hidden rounded-[2.5px] border border-white/20 shadow-sm print:shadow-none print:border-gray-400 bg-white/5 ${dim.aspect} ${className}`}
      style={{
        printColorAdjust: "exact",
        WebkitPrintColorAdjust: "exact",
      }}
      title={countryDisplayName}
    >
      {code !== "un" && !imgError ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={`https://flagcdn.com/w40/${code}.png`}
          srcSet={`https://flagcdn.com/w80/${code}.png 2x`}
          alt={`${countryDisplayName} Flag`}
          width={dim.w}
          height={dim.h}
          loading="eager"
          crossOrigin="anonymous"
          onError={() => setImgError(true)}
          className="w-full h-full object-cover"
          style={{
            printColorAdjust: "exact",
            WebkitPrintColorAdjust: "exact",
          }}
        />
      ) : (
        <span className="text-[11px] leading-none select-none flex items-center justify-center font-mono font-bold">
          {emojiFallback && emojiFallback !== "🎓" ? (
            <span className="text-[13px]">{emojiFallback}</span>
          ) : code !== "un" ? (
            <span className="text-[9px] font-black tracking-tight text-white bg-emerald-900/80 px-1 py-0.5 rounded border border-emerald-500/30">
              {code.toUpperCase()}
            </span>
          ) : (
            <span>🎓</span>
          )}
        </span>
      )}
    </span>
  );

  if (showName) {
    return (
      <span className="inline-flex items-center space-x-1.5 align-middle">
        {flagContent}
        <span className={nameClassName}>{countryDisplayName}</span>
      </span>
    );
  }

  return flagContent;
};
