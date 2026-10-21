"use client";

import React, { Component, ErrorInfo, ReactNode } from "react";
import { AlertTriangle, RefreshCw } from "lucide-react";

interface Props {
  children: ReactNode;
  subsystemName?: string;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class TheatreErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null,
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.warn(`[Theatre Subsystem Error Boundary] in ${this.props.subsystemName || "Subsystem"}:`, error, errorInfo);
  }

  private handleReset = () => {
    this.setState({ hasError: false, error: null });
  };

  public render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback;
      }

      return (
        <div className="w-full h-full min-h-[140px] flex items-center justify-center p-4">
          <div className="max-w-md w-full bg-[#1C1917]/90 border border-amber-500/30 rounded-xl p-4 backdrop-blur-md text-center shadow-lg font-mono">
            <div className="flex items-center justify-center space-x-2 text-amber-400 mb-2">
              <AlertTriangle className="w-4 h-4" />
              <span className="text-xs font-bold tracking-wider uppercase">
                {this.props.subsystemName || "THEATRE SUBSYSTEM"} {"//"} ISOLATED
              </span>
            </div>
            <p className="text-[11px] text-zinc-300 mb-3 leading-relaxed">
              Localized presentation fault caught gracefully. The autonomous intelligence organisation continues running.
            </p>
            <button
              onClick={this.handleReset}
              className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-md bg-white/[0.08] hover:bg-white/[0.15] border border-white/[0.1] text-xs text-white transition-all duration-150 cursor-pointer"
            >
              <RefreshCw className="w-3 h-3" />
              <span>RECOVER SUBSYSTEM</span>
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
