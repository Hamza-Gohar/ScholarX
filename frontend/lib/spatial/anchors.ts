import { Region } from "../types";
import { GEO_COORDINATES, projectGeoToScene, generateCurvedArc } from "./coordinates";
import { GeographicAnchor, SpatialRoute } from "./types";

export const PAKISTAN_ANCHOR: GeographicAnchor = {
  id: "origin-pakistan",
  name: "Pakistan",
  isOrigin: true,
  coordinates: GEO_COORDINATES.PAKISTAN,
  scenePosition: projectGeoToScene(GEO_COORDINATES.PAKISTAN),
  label: "PAKISTAN",
  sublabel: "MISSION ORIGIN // [69.3°E, 30.4°N]",
  quotaCount: 400,
  accentColor: "verified",
};

export const REGIONAL_ANCHORS: Record<Region, GeographicAnchor> = {
  Europe: {
    id: "anchor-europe",
    name: "Europe",
    region: "Europe",
    coordinates: GEO_COORDINATES.EUROPE,
    scenePosition: projectGeoToScene(GEO_COORDINATES.EUROPE),
    label: "EUROPE",
    sublabel: "69 SCHOLARSHIPS",
    quotaCount: 69,
    accentColor: "flow",
  },
  Asia: {
    id: "anchor-asia",
    name: "Asia",
    region: "Asia",
    coordinates: GEO_COORDINATES.ASIA,
    scenePosition: projectGeoToScene(GEO_COORDINATES.ASIA),
    label: "ASIA",
    sublabel: "57 SCHOLARSHIPS",
    quotaCount: 57,
    accentColor: "flow",
  },
  Americas: {
    id: "anchor-americas",
    name: "Americas",
    region: "Americas",
    coordinates: GEO_COORDINATES.AMERICAS,
    scenePosition: projectGeoToScene(GEO_COORDINATES.AMERICAS),
    label: "AMERICAS",
    sublabel: "42 SCHOLARSHIPS",
    quotaCount: 42,
    accentColor: "flow",
  },
  MENA: {
    id: "anchor-mena",
    name: "MENA",
    region: "MENA",
    coordinates: GEO_COORDINATES.MENA,
    scenePosition: projectGeoToScene(GEO_COORDINATES.MENA),
    label: "MENA",
    sublabel: "27 SCHOLARSHIPS",
    quotaCount: 27,
    accentColor: "flow",
  },
  Oceania: {
    id: "anchor-oceania",
    name: "Oceania",
    region: "Oceania",
    coordinates: GEO_COORDINATES.OCEANIA,
    scenePosition: projectGeoToScene(GEO_COORDINATES.OCEANIA),
    label: "OCEANIA",
    sublabel: "10 SCHOLARSHIPS",
    quotaCount: 10,
    accentColor: "flow",
  },
};

export function getSpatialRoutes(): SpatialRoute[] {
  const origin = PAKISTAN_ANCHOR.scenePosition;
  const regions: Region[] = ["Europe", "Asia", "Americas", "MENA", "Oceania"];

  return regions.map((region) => {
    const dest = REGIONAL_ANCHORS[region].scenePosition;
    const { pathData, controlPoint } = generateCurvedArc(origin, dest);

    return {
      id: `route-pk-${region.toLowerCase()}`,
      sourceAnchorId: PAKISTAN_ANCHOR.id,
      targetAnchorId: REGIONAL_ANCHORS[region].id,
      sourceRegion: "Pakistan",
      targetRegion: region,
      pathData,
      startPoint: origin,
      endPoint: dest,
      controlPoint,
      isActive: true,
      itemCount: REGIONAL_ANCHORS[region].quotaCount || 0,
    };
  });
}
