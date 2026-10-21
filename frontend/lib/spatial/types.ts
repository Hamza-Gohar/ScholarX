import { Region } from "../types";

export type MapState =
  | "DORMANT"
  | "MISSION"
  | "DEPLOYMENT"
  | "RESEARCH"
  | "EVIDENCE"
  | "DOSSIER";

export type CameraShot =
  | "GLOBAL"
  | "DEPLOYMENT"
  | "REGIONAL"
  | "AGENT"
  | "EVIDENCE"
  | "DOSSIER";

export type GeographicCoordinates = [longitude: number, latitude: number];

export interface ScenePoint {
  x: number;
  y: number;
}

export interface GeographicAnchor {
  id: string;
  name: string;
  region?: Region;
  isOrigin?: boolean;
  coordinates: GeographicCoordinates;
  scenePosition: ScenePoint;
  label: string;
  sublabel: string;
  quotaCount?: number;
  accentColor: "command" | "flow" | "verified" | "warning" | "challenge";
}

export interface SpatialRoute {
  id: string;
  sourceAnchorId: string;
  targetAnchorId: string;
  sourceRegion: "Pakistan";
  targetRegion: Region;
  pathData: string;
  startPoint: ScenePoint;
  endPoint: ScenePoint;
  controlPoint: ScenePoint;
  isActive: boolean;
  itemCount: number;
}

export interface CameraTransform {
  x: number;
  y: number;
  scale: number;
  opacity: number;
}

export interface SpatialFocus {
  activeRegion: Region | "Pakistan" | null;
  targetEntityId: string | null;
  cameraShot: CameraShot;
  mapState: MapState;
}
