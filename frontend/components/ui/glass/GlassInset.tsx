import React from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface GlassInsetProps extends React.HTMLAttributes<HTMLDivElement> {
  subtle?: boolean;
}

export const GlassInset: React.FC<GlassInsetProps> = ({
  subtle = false,
  className,
  children,
  ...props
}) => {
  return (
    <div
      className={twMerge(
        clsx(
          "rounded-lg border border-white/[0.04]",
          subtle
            ? "bg-black/20"
            : "bg-black/40 shadow-[inset_0_2px_4px_rgba(0,0,0,0.5)]",
          "p-3.5 text-sx-text-secondary text-sm",
          className
        )
      )}
      {...props}
    >
      {children}
    </div>
  );
};
