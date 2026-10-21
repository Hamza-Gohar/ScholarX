import React from "react";
import { GlassSurface, GlassSurfaceProps } from "./GlassSurface";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface GlassPanelProps extends GlassSurfaceProps {
  header?: React.ReactNode;
  footer?: React.ReactNode;
  headerClassName?: string;
  bodyClassName?: string;
  footerClassName?: string;
}

export const GlassPanel: React.FC<GlassPanelProps> = ({
  header,
  footer,
  headerClassName,
  bodyClassName,
  footerClassName,
  className,
  children,
  ...props
}) => {
  return (
    <GlassSurface
      className={twMerge(clsx("flex flex-col", className))}
      {...props}
    >
      {header && (
        <div
          className={twMerge(
            clsx(
              "px-5 py-3.5 border-b border-white/[0.06] flex items-center justify-between",
              headerClassName
            )
          )}
        >
          {header}
        </div>
      )}
      <div className={twMerge(clsx("p-5 flex-1", bodyClassName))}>
        {children}
      </div>
      {footer && (
        <div
          className={twMerge(
            clsx(
              "px-5 py-3 border-t border-white/[0.06] bg-black/20",
              footerClassName
            )
          )}
        >
          {footer}
        </div>
      )}
    </GlassSurface>
  );
};
