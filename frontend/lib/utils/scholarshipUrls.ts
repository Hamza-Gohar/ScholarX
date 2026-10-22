import { SEED_SCHOLARSHIPS } from "@/lib/seed-data";
import deepDossiersBundle from "@/lib/data/scholarships_deep_dossiers.json";

const deepDossiers = deepDossiersBundle as Record<string, any>;

// Cache lookup maps for instant performance
const urlByIdMap = new Map<string, string>();
const urlByNameMap = new Map<string, string>();

function normalizeName(name: string): string {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

// Prepopulate cache from SEED_SCHOLARSHIPS
for (const s of SEED_SCHOLARSHIPS) {
  const url = s.portal_url || s.source_url;
  if (url && isValidPortalUrl(url)) {
    if (s.scholarship_id) {
      urlByIdMap.set(s.scholarship_id.toLowerCase(), url);
    }
    if (s.name) {
      urlByNameMap.set(normalizeName(s.name), url);
    }
  }
}

// Augment cache from deep dossiers
for (const [sid, dd] of Object.entries(deepDossiers)) {
  const portal =
    dd?.basic_details?.official_scholarship_portal ||
    dd?.application_process?.submission_portal_url ||
    dd?.official_sources_verified?.[0]?.source_url;

  if (portal && isValidPortalUrl(portal)) {
    const cleanSid = sid.toLowerCase();
    if (!urlByIdMap.has(cleanSid)) {
      urlByIdMap.set(cleanSid, portal);
    }
    const name = dd?.basic_details?.scholarship_name;
    if (name) {
      const norm = normalizeName(name);
      if (!urlByNameMap.has(norm)) {
        urlByNameMap.set(norm, portal);
      }
    }
  }
}

export function sanitizePortalUrl(url?: string | null): string | null {
  if (!url) return null;
  let clean = url.trim();
  if (clean.includes("apply.usefp.org")) {
    clean = clean.replace("apply.usefp.org", "applications.usefp.org");
  }
  if (clean.includes("adu.ac.ae/admissions/financial-resources/scholarships")) {
    clean = "https://www.adu.ac.ae/en/study/financials/scholarships";
  }
  if (clean.includes("adu.ac.ae/admissions/financial-support/scholarships")) {
    clean = "https://www.adu.ac.ae/en/study/financials/scholarships";
  }
  return clean;
}

function isValidPortalUrl(url?: string | null): boolean {
  if (!url) return false;
  const lower = url.toLowerCase().trim();
  if (
    lower === "https://scholarship.gov.pk" ||
    lower === "http://scholarship.gov.pk" ||
    lower === "https://scholarship.gov.pk/" ||
    lower === "n/a" ||
    lower === "#" ||
    lower === ""
  ) {
    return false;
  }
  return lower.startsWith("http://") || lower.startsWith("https://");
}

/**
 * Resolves the genuine official application portal URL for any scholarship.
 * Checks opportunity properties, ID matching, name fuzzy matching, and deep dossiers.
 */
export function resolveScholarshipOfficialUrl(sc: {
  id?: string | null;
  name?: string | null;
  officialPortalUrl?: string | null;
  source_url?: string | null;
  portal_url?: string | null;
  official_portal_url?: string | null;
}): string {
  // 1. Direct valid property check
  const official = sanitizePortalUrl(sc.officialPortalUrl);
  if (isValidPortalUrl(official)) {
    return official!;
  }
  const portal = sanitizePortalUrl(sc.portal_url);
  if (isValidPortalUrl(portal)) {
    return portal!;
  }
  const source = sanitizePortalUrl(sc.source_url);
  if (isValidPortalUrl(source)) {
    return source!;
  }
  const officialPortal = sanitizePortalUrl(sc.official_portal_url);
  if (isValidPortalUrl(officialPortal)) {
    return officialPortal!;
  }

  // 2. ID matching in catalog
  if (sc.id) {
    const idKey = sc.id.toLowerCase().trim();
    if (urlByIdMap.has(idKey)) {
      return urlByIdMap.get(idKey)!;
    }
    // Partial ID matching (e.g., 'KFUPM')
    for (const [key, url] of urlByIdMap.entries()) {
      if (key.includes(idKey) || idKey.includes(key)) {
        return url;
      }
    }
  }

  // 3. Name matching in catalog
  if (sc.name) {
    const norm = normalizeName(sc.name);
    if (urlByNameMap.has(norm)) {
      return urlByNameMap.get(norm)!;
    }
    // Fuzzy word overlap match
    for (const [nameKey, url] of urlByNameMap.entries()) {
      if (nameKey.includes(norm) || norm.includes(nameKey)) {
        return url;
      }
      // Check significant words (3+ letters)
      const queryWords = norm.split(" ").filter((w) => w.length >= 4);
      if (queryWords.length >= 2) {
        const matches = queryWords.filter((w) => nameKey.includes(w));
        if (matches.length >= 2) {
          return url;
        }
      }
    }
  }

  // 4. Fallback to official HEC bilateral portal
  return "https://scholarship.hec.gov.pk";
}

/**
 * Strips protocol and trailing slashes for clean, elegant typography.
 */
export function cleanPortalDisplayUrl(url: string): string {
  if (!url) return "official-portal";
  let display = url.replace(/^https?:\/\//i, "");
  display = display.replace(/\/+$/, "");
  return display;
}
