import { Region } from "../types";
import { CameraShot, CameraTransform, MapState } from "./types";
import { REGIONAL_ANCHORS, PAKISTAN_ANCHOR } from "./anchors";
import { STAGE_WIDTH, STAGE_HEIGHT } from "./coordinates";

export const CAMERA_PRESETS: Record<CameraShot, CameraTransform> = {
  GLOBAL: {
    x: 0,
    y: 0,
    scale: 1,
    opacity: 1,
  },
  DEPLOYMENT: {
    x: 0,
    y: -15,
    scale: 1.05,
    opacity: 1,
  },
  REGIONAL: {
    x: -160,
    y: 70,
    scale: 1.45,
    opacity: 1,
  },
  AGENT: {
    x: -180,
    y: 90,
    scale: 1.6,
    opacity: 1,
  },
  EVIDENCE: {
    x: -210,
    y: 110,
    scale: 1.8,
    opacity: 1,
  },
  DOSSIER: {
    x: 0,
    y: 0,
    scale: 0.95,
    opacity: 0.55,
  },
};

export function getCameraTransformForFocus(
  shot: CameraShot,
  focusRegion: Region | "Pakistan" | null = null,
  mapState: MapState = "DEPLOYMENT"
): CameraTransform {
  if (mapState === "DOSSIER") {
    return CAMERA_PRESETS.DOSSIER;
  }

  if (mapState === "DORMANT") {
    return {
      x: 0,
      y: 0,
      scale: 1,
      opacity: 0.85,
    };
  }

  if (shot === "REGIONAL" && focusRegion && focusRegion !== "Pakistan") {
    const targetAnchor = REGIONAL_ANCHORS[focusRegion];
    if (targetAnchor) {
      // Calculate delta to center the region in view
      const targetX = (STAGE_WIDTH / 2 - targetAnchor.scenePosition.x) * 0.45;
      const targetY = (STAGE_HEIGHT / 2 - targetAnchor.scenePosition.y) * 0.45;
      return {
        x: targetX,
        y: targetY,
        scale: 1.45,
        opacity: 1,
      };
    }
  }

  if (shot === "REGIONAL" && focusRegion === "Pakistan") {
    const targetX = (STAGE_WIDTH / 2 - PAKISTAN_ANCHOR.scenePosition.x) * 0.45;
    const targetY = (STAGE_HEIGHT / 2 - PAKISTAN_ANCHOR.scenePosition.y) * 0.45;
    return {
      x: targetX,
      y: targetY,
      scale: 1.4,
      opacity: 1,
    };
  }

  return CAMERA_PRESETS[shot] || CAMERA_PRESETS.GLOBAL;
}
