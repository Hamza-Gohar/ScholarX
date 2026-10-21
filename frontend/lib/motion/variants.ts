import { Variants } from "framer-motion";
import { motionDurations, motionEasings, motionSprings } from "./tokens";

export const fadeIn: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      duration: motionDurations.standard,
      ease: motionEasings.easeOut,
    },
  },
  exit: {
    opacity: 0,
    transition: {
      duration: motionDurations.fast,
      ease: motionEasings.easeIn,
    },
  },
};

export const rise: Variants = {
  hidden: { opacity: 0, y: 16 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: motionDurations.standard,
      ease: motionEasings.easeOut,
    },
  },
  exit: {
    opacity: 0,
    y: -8,
    transition: {
      duration: motionDurations.fast,
      ease: motionEasings.easeIn,
    },
  },
};

export const settle: Variants = {
  hidden: { opacity: 0, y: -12 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: motionDurations.standard,
      ease: motionEasings.easeOut,
    },
  },
};

export const scaleIn: Variants = {
  hidden: { opacity: 0, scale: 0.94 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: motionSprings.gentle,
  },
  exit: {
    opacity: 0,
    scale: 0.96,
    transition: {
      duration: motionDurations.fast,
      ease: motionEasings.easeIn,
    },
  },
};

export const surfaceReveal: Variants = {
  hidden: { opacity: 0, scale: 0.97, y: 10 },
  visible: {
    opacity: 1,
    scale: 1,
    y: 0,
    transition: motionSprings.authoritative,
  },
  exit: {
    opacity: 0,
    scale: 0.98,
    transition: {
      duration: motionDurations.fast,
      ease: motionEasings.easeIn,
    },
  },
};

export const contentReveal: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.08,
      delayChildren: 0.05,
    },
  },
};

export const softPulse: Variants = {
  idle: { opacity: 0.8 },
  active: {
    opacity: [0.7, 1, 0.7],
    transition: {
      duration: 2.8,
      repeat: Infinity,
      ease: motionEasings.easeInOut,
    },
  },
};

export const subtleFloat: Variants = {
  animate: {
    y: [-3, 3, -3],
    transition: {
      duration: 6,
      repeat: Infinity,
      ease: motionEasings.easeInOut,
    },
  },
};

// Ultra-light, lag-free mobile variants
export const mobileFadeIn: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      duration: motionDurations.mobileFade,
      ease: motionEasings.easeOut,
    },
  },
  exit: {
    opacity: 0,
    transition: {
      duration: motionDurations.mobileFade,
      ease: motionEasings.easeIn,
    },
  },
};

export const mobileSlideUp: Variants = {
  hidden: { opacity: 0, y: 8 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: motionDurations.mobileSnap,
      ease: motionEasings.easeOut,
    },
  },
  exit: {
    opacity: 0,
    y: -4,
    transition: {
      duration: motionDurations.mobileFade,
      ease: motionEasings.easeIn,
    },
  },
};

