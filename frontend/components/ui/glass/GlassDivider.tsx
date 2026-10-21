import React from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface GlassDividerProps {
  orientation?: "horizontal" | "vertical";
  className?: string;
}

export const GlassDivider: React.FC<GlassDividerProps> = ({
  orientation = "horizontal",
  className,
}) => {
  if (orientation === "vertical") {
    return (
      <div
        className={twMerge(
          clsx(
            "w-px self-stretch bg-gradient-to-b from-transparent via-white/[0.12] to-transparent",
            className
          )
        )}
      />
    );
  }

  return (
    <div
      className={twMerge(
        clsx(
          "h-px w-full bg-gradient-to-r from-transparent via-white/[0.12] to-transparent",
          className
        )
      )}
    />
  );
};
