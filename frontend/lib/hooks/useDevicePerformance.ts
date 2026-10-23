"use client";

import { useState, useEffect, useCallback } from "react";

export interface DevicePerformanceState {
  isLowEnd: boolean;
  isEcoMode: boolean;
  isTabVisible: boolean;
  isMobile: boolean;
  isTouchDevice: boolean;
  toggleEcoMode: () => void;
}

const STORAGE_KEY = "scholarx_eco_mode";

export function useDevicePerformance(): DevicePerformanceState {
  const [isEcoMode, setIsEcoMode] = useState<boolean>(false);
  const [isLowEnd, setIsLowEnd] = useState<boolean>(false);
  const [isTabVisible, setIsTabVisible] = useState<boolean>(true);
  const [isMobile, setIsMobile] = useState<boolean>(false);
  const [isTouchDevice, setIsTouchDevice] = useState<boolean>(false);

  // Initialize hardware, mobile & touch detection & stored preferences
  useEffect(() => {
    if (typeof window === "undefined") return;

    // Mobile & Touch detection
    const checkMobile = () => {
      const mobileWidth = window.innerWidth < 1024;
      setIsMobile(mobileWidth);
    };

    const hasTouch = "ontouchstart" in window || navigator.maxTouchPoints > 0;
    setIsTouchDevice(hasTouch);
    checkMobile();

    window.addEventListener("resize", checkMobile);
    window.addEventListener("orientationchange", checkMobile);

    let lowEndDetected = false;

    // 1. Hardware concurrency (cores <= 4 typically denotes budget mobile/laptop)
    if (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4) {
      lowEndDetected = true;
    }

    // 2. Device memory API (RAM <= 4GB)
    // @ts-ignore - navigator.deviceMemory is available in Chromium-based browsers
    if (navigator.deviceMemory && (navigator as any).deviceMemory <= 4) {
      lowEndDetected = true;
    }

    // 3. User prefers reduced motion
    const prefersReducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;
    if (prefersReducedMotion) {
      lowEndDetected = true;
    }

    setIsLowEnd(lowEndDetected);

    // 4. Stored user preference
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored !== null) {
      setIsEcoMode(stored === "true");
    } else if (lowEndDetected) {
      // Auto-enable Eco Mode by default on low-end devices for butter-smooth experience
      setIsEcoMode(true);
    }

    return () => {
      window.removeEventListener("resize", checkMobile);
      window.removeEventListener("orientationchange", checkMobile);
    };
  }, []);

  // Listen to tab visibility changes to hibernate background rendering & preserve battery
  useEffect(() => {
    if (typeof document === "undefined") return;

    const handleVisibilityChange = () => {
      const isVisible = document.visibilityState === "visible";
      setIsTabVisible(isVisible);
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);
    return () => {
      document.removeEventListener("visibilitychange", handleVisibilityChange);
    };
  }, []);

  // Sync data attribute to <html> for global CSS optimizations
  useEffect(() => {
    if (typeof document === "undefined") return;
    const root = document.documentElement;
    if (isEcoMode || isLowEnd) {
      root.setAttribute("data-eco-mode", "true");
    } else {
      root.removeAttribute("data-eco-mode");
    }
  }, [isEcoMode, isLowEnd]);

  const toggleEcoMode = useCallback(() => {
    setIsEcoMode((prev) => {
      const next = !prev;
      try {
        localStorage.setItem(STORAGE_KEY, String(next));
      } catch {}
      return next;
    });
  }, []);

  return {
    isLowEnd,
    isEcoMode,
    isTabVisible,
    isMobile,
    isTouchDevice,
    toggleEcoMode,
  };
}
