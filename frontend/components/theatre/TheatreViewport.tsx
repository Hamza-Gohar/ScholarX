"use client";

import React from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface TheatreViewportProps {
  children: React.ReactNode;
  className?: string;
  enforce16x9?: boolean;
}

export const TheatreViewport: React.FC<TheatreViewportProps> = ({
  children,
  className,
  enforce16x9 = true,
}) => {
  return (
    <div
      className={twMerge(
        clsx(
          "relative w-full min-h-screen bg-sx-black select-none text-sx-text-primary",
          "flex items-center justify-center overflow-x-hidden",
          className
        )
      )}
      id="scholarx-theatre-viewport"
    >
      {/* Responsive Coordinate Stage: 16:9 on desktop, fluid vertical-scroll on mobile */}
      <div
        className={twMerge(
          clsx(
            "relative w-full h-full flex flex-col",
            enforce16x9
              ? "min-h-screen lg:min-h-0 lg:max-w-[1920px] lg:max-h-[1080px] lg:aspect-video overflow-y-auto lg:overflow-hidden touch-scroll"
              : "w-full min-h-screen overflow-y-auto touch-scroll"
          )
        )}
        id="scholarx-theatre-stage"
      >
        {children}
      </div>
    </div>
  );
};
