import { geoEquirectangular } from "d3-geo";
import { GeographicCoordinates, ScenePoint } from "./types";

export const STAGE_WIDTH = 1920;
export const STAGE_HEIGHT = 1080;

// Authoritative Geographic Coordinates [longitude, latitude] (§7.3, §7.4)
export const GEO_COORDINATES = {
  PAKISTAN: [69.3451, 30.3753] as GeographicCoordinates,
  EUROPE: [13.405, 52.52] as GeographicCoordinates, // Berlin / Central Europe
  ASIA: [116.4074, 39.9042] as GeographicCoordinates, // Beijing / East Asia
  AMERICAS: [-77.0369, 38.9072] as GeographicCoordinates, // Washington / North America
  MENA: [46.6753, 24.7136] as GeographicCoordinates, // Riyadh / Gulf
  OCEANIA: [149.13, -35.2809] as GeographicCoordinates, // Canberra / Australasia
  HUNGARY: [19.0402, 47.4979] as GeographicCoordinates, // Budapest / Stipendium Hungaricum
} as const;

// Equirectangular projection calibrated for 1920x1080 exhibition viewport
export const worldProjection = geoEquirectangular()
  .scale(305)
  .translate([STAGE_WIDTH / 2, STAGE_HEIGHT / 2 + 55]);

export function projectGeoToScene(coords: GeographicCoordinates): ScenePoint {
  const projected = worldProjection(coords);
  if (!projected) {
    return { x: STAGE_WIDTH / 2, y: STAGE_HEIGHT / 2 };
  }
  return { x: projected[0], y: projected[1] };
}

export function generateCurvedArc(
  start: ScenePoint,
  end: ScenePoint,
  arcHeightFactor = 0.22,
  verticalLift = 65
): { pathData: string; controlPoint: ScenePoint } {
  const dx = end.x - start.x;
  const dy = end.y - start.y;

  // Compute perpendicular offset for natural geographic curve
  const cx = (start.x + end.x) / 2 - dy * arcHeightFactor;
  const cy = (start.y + end.y) / 2 + dx * 0.12 - verticalLift;

  const controlPoint = { x: cx, y: cy };
  const pathData = `M ${start.x} ${start.y} Q ${cx} ${cy} ${end.x} ${end.y}`;

  return { pathData, controlPoint };
}
