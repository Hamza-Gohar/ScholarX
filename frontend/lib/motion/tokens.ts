// Master Design Guide Motion System (§6.9, §17)
// Motion communicates: state, hierarchy, focus, arrival, departure, attention.
// Motion is never decorative, random, or hyperactive.

export const motionDurations = {
  mobileSnap: 0.18,
  mobileFade: 0.15,
  instant: 0.15,
  fast: 0.25,
  standard: 0.4,
  deliberate: 0.7,
  theatre: 1.0,
  ambient: 4.0,
} as const;

export const motionEasings = {
  // Smooth, decelerating entrance
  easeOut: [0.16, 1, 0.3, 1],
  // Quick exit
  easeIn: [0.7, 0, 0.84, 0],
  // Balanced state transitions
  easeInOut: [0.4, 0, 0.2, 1],
  // Sharp mechanical precision
  precision: [0.25, 1, 0.5, 1],
} as const;

export const motionSprings = {
  // Non-bouncy, natural arrival
  gentle: {
    type: "spring",
    stiffness: 120,
    damping: 24,
    mass: 0.8,
  },
  // Responsive UI feedback
  snappy: {
    type: "spring",
    stiffness: 260,
    damping: 30,
    mass: 0.6,
  },
  // Heavy, authoritative presence (Commander, modals)
  authoritative: {
    type: "spring",
    stiffness: 90,
    damping: 22,
    mass: 1.2,
  },
} as const;
