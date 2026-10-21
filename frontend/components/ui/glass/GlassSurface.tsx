import React, { forwardRef } from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface GlassSurfaceProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "subtle" | "default" | "strong";
  elevation?: "flat" | "elevated" | "floating";
  interactive?: boolean;
  accentBorder?: "none" | "command" | "flow" | "verified" | "warning" | "challenge";
}

export const GlassSurface = forwardRef<HTMLDivElement, GlassSurfaceProps>(
  (
    {
      variant = "default",
      elevation = "elevated",
      interactive = false,
      accentBorder = "none",
      className,
      children,
      ...props
    },
    ref
  ) => {
    const variantStyles = {
      subtle: "bg-sx-glass-subtle backdrop-blur-md border border-sx-border-subtle",
      default: "bg-sx-glass backdrop-blur-xl border border-sx-border",
      strong: "bg-sx-glass-strong backdrop-blur-2xl border border-sx-border",
    };

    const elevationStyles = {
      flat: "shadow-none",
      elevated: "shadow-sx-glass shadow-black/60",
      floating: "shadow-sx-glass-elevated shadow-black/80",
    };

    const accentBorderStyles = {
      none: "",
      command: "border-sx-command/35 shadow-[0_0_20px_-5px_rgba(212,175,55,0.15)]",
      flow: "border-sx-flow/35 shadow-[0_0_20px_-5px_rgba(56,189,248,0.15)]",
      verified: "border-sx-verified/35 shadow-[0_0_20px_-5px_rgba(16,185,129,0.15)]",
      warning: "border-sx-warning/35 shadow-[0_0_20px_-5px_rgba(245,158,11,0.15)]",
      challenge: "border-sx-challenge/35 shadow-[0_0_20px_-5px_rgba(239,68,68,0.15)]",
    };

    const interactiveStyles = interactive
      ? "transition-all duration-300 hover:border-sx-border-active hover:bg-sx-panel/85"
      : "";

    return (
      <div
        ref={ref}
        className={twMerge(
          clsx(
            "relative rounded-xl text-sx-text-primary",
            "box-border overflow-hidden",
            "before:absolute before:inset-x-0 before:top-0 before:h-px before:bg-gradient-to-r before:from-transparent before:via-white/10 before:to-transparent before:pointer-events-none",
            variantStyles[variant],
            elevationStyles[elevation],
            accentBorderStyles[accentBorder],
            interactiveStyles,
            className
          )
        )}
        {...props}
      >
        {children}
      </div>
    );
  }
);

GlassSurface.displayName = "GlassSurface";
