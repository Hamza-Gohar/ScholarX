"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ToolActivityMeta } from "@/lib/fleet/types";
import { Search, Globe, FileText, Cpu, Sparkles, CheckCircle } from "lucide-react";

export interface ScoutToolActivityProps {
  tool: ToolActivityMeta | null;
  className?: string;
}

export const ScoutToolActivity: React.FC<ScoutToolActivityProps> = ({
  tool,
  className = "",
}) => {
  if (!tool) return null;

  const renderIcon = () => {
    const props = { className: "w-3 h-3" };
    switch (tool.iconName) {
      case "Search":
        return <Search {...props} />;
      case "Globe":
        return <Globe {...props} />;
      case "FileText":
        return <FileText {...props} />;
      case "Cpu":
        return <Cpu {...props} />;
      case "Sparkles":
        return <Sparkles {...props} />;
      case "CheckCircle":
        return <CheckCircle {...props} />;
      default:
        return <Search {...props} />;
    }
  };

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={tool.displayName}
        initial={{ opacity: 0, y: 3, scale: 0.95 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        exit={{ opacity: 0, y: -3, scale: 0.95 }}
        transition={{ duration: 0.25 }}
        className={`inline-flex items-center space-x-2 px-2.5 py-1 rounded-md border text-[10px] font-mono select-none backdrop-blur-md shadow-sm ${className}`}
        style={{
          borderColor: `${tool.color}50`,
          backgroundColor: `${tool.color}15`,
          color: tool.color,
          boxShadow: `0 0 14px ${tool.color}25`,
        }}
      >
        {/* Pulsing Computational Status Dot */}
        <span className="relative flex h-2 w-2">
          <motion.span
            className="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
            style={{ backgroundColor: tool.color }}
          />
          <span
            className="relative inline-flex rounded-full h-2 w-2"
            style={{ backgroundColor: tool.color }}
          />
        </span>

        {/* Dynamic Tool Icon */}
        <span className="shrink-0">{renderIcon()}</span>

        {/* Action Phase + Tool Name */}
        <span className="font-semibold tracking-wider uppercase">
          {tool.actionLabel}: <strong className="text-white/90">{tool.displayName}</strong>
        </span>
      </motion.div>
    </AnimatePresence>
  );
};
