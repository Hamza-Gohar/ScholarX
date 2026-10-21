import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Master Design Guide Foundation Tokens (§6, Appendix H)
        sx: {
          black: "#05070A",
          deep: "#080C10",
          panel: "#0B1117",
          surface: "#0F1722",
          border: {
            subtle: "rgba(180, 210, 225, 0.08)",
            neutral: "rgba(180, 210, 225, 0.14)",
            active: "rgba(110, 225, 255, 0.32)",
            focus: "rgba(229, 192, 123, 0.40)",
            success: "rgba(16, 185, 129, 0.35)",
            warning: "rgba(245, 158, 11, 0.35)",
            challenge: "rgba(239, 68, 68, 0.35)",
          },
          glass: {
            subtle: "rgba(12, 18, 24, 0.35)",
            DEFAULT: "rgba(12, 18, 24, 0.58)",
            strong: "rgba(12, 18, 24, 0.78)",
          },
          // Master Design Tokens
          gold: "#D4AF37",
          ice: "#38BDF8",
          // Restrained Semantic Accents
          command: {
            DEFAULT: "#D4AF37",
            light: "#E5C07B",
            muted: "#C5A059",
            glow: "rgba(212, 175, 55, 0.22)",
            dim: "rgba(212, 175, 55, 0.10)",
          },
          flow: {
            DEFAULT: "#38BDF8",
            light: "#7DD3FC",
            muted: "#0284C7",
            glow: "rgba(56, 189, 248, 0.22)",
            dim: "rgba(56, 189, 248, 0.10)",
          },
          verified: {
            DEFAULT: "#10B981",
            light: "#34D399",
            muted: "#059669",
            glow: "rgba(16, 185, 129, 0.22)",
            dim: "rgba(16, 185, 129, 0.10)",
          },
          warning: {
            DEFAULT: "#F59E0B",
            light: "#FBBF24",
            muted: "#D97706",
            glow: "rgba(245, 158, 11, 0.22)",
            dim: "rgba(245, 158, 11, 0.10)",
          },
          challenge: {
            DEFAULT: "#EF4444",
            light: "#F87171",
            muted: "#DC2626",
            glow: "rgba(239, 68, 68, 0.22)",
            dim: "rgba(239, 68, 68, 0.10)",
          },
          text: {
            primary: "#F8FAFC",
            secondary: "#94A3B8",
            tertiary: "#64748B",
            quaternary: "#475569",
          },
        },

        // Backward compatibility mappings for legacy components
        obsidian: {
          950: "#05070A",
          900: "#080C10",
          850: "#0B1117",
          800: "#101826",
          700: "#182438",
          600: "#22334F",
          500: "#32486D",
        },
        cyber: {
          cyan: "#38BDF8",
          glow: "rgba(56, 189, 248, 0.25)",
          dim: "#0284C7",
        },
        pakistan: {
          emerald: "#10B981",
          deep: "#064E3B",
          glow: "rgba(16, 185, 129, 0.25)",
        },
        skeptic: {
          rose: "#EF4444",
          glow: "rgba(239, 68, 68, 0.25)",
          crimson: "#B91C1C",
        },
        intel: {
          purple: "#818CF8",
          indigo: "#6366F1",
          glow: "rgba(99, 102, 241, 0.25)",
        },
      },
      fontFamily: {
        sans: [
          "var(--font-sans)",
          "Plus Jakarta Sans",
          "Outfit",
          "Inter",
          "-apple-system",
          "BlinkMacSystemFont",
          "system-ui",
          "Segoe UI",
          "Roboto",
          "sans-serif",
        ],
        display: [
          "var(--font-display)",
          "Outfit",
          "Plus Jakarta Sans",
          "-apple-system",
          "sans-serif",
        ],
        serif: [
          "var(--font-serif)",
          "Newsreader",
          "Lora",
          "Georgia",
          "serif",
        ],
        mono: [
          "var(--font-mono)",
          "Plus Jakarta Sans",
          "Inter",
          "-apple-system",
          "monospace",
        ],
        code: [
          "ui-monospace",
          "SFMono-Regular",
          "Menlo",
          "Monaco",
          "Consolas",
          "monospace",
        ],
      },
      boxShadow: {
        // Physical floating glass shadows & subtle edge highlights
        "sx-glass": "0 20px 40px -15px rgba(0, 0, 0, 0.7)",
        "sx-glass-elevated": "0 30px 60px -20px rgba(0, 0, 0, 0.85)",
        "sx-glass-highlight": "inset 0 1px 0 0 rgba(255, 255, 255, 0.08)",
        "sx-glass-highlight-subtle": "inset 0 1px 0 0 rgba(255, 255, 255, 0.04)",
        "panel": "inset 0 1px 0 0 rgba(255, 255, 255, 0.06), 0 16px 36px -10px rgba(0, 0, 0, 0.8)",
      },
      zIndex: {
        "theatre-bg": "0",
        "theatre-atmosphere": "10",
        "theatre-world": "20",
        "theatre-secondary": "30",
        "theatre-routes": "35",
        "theatre-primary": "40",
        "theatre-focus": "50",
        "theatre-overlays": "60",
        "theatre-overlay": "60",
        "theatre-system": "70",
      },
    },
  },
  plugins: [],
};

export default config;
