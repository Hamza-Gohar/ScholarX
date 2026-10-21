/**
 * Universal Country Flag and Identity Utility for ScholarX
 * Maps any country name, institution, or ISO code directly to:
 * 1. 2-letter ISO country code for high-res vector flag rendering
 * 2. Official national flag emoji
 * 3. Canonical English country name
 * Eliminates all generic globe emojis (🌍) and classical temple (🏛️) glyphs.
 */

// Normalized mapping dictionary (lower-case, diacritics stripped)
const COUNTRY_LOOKUP: Record<string, { code: string; flag: string; name: string }> = {
  // Flagship destinations
  turkey: { code: "tr", flag: "🇹🇷", name: "Türkiye" },
  turkiye: { code: "tr", flag: "🇹🇷", name: "Türkiye" },
  tr: { code: "tr", flag: "🇹🇷", name: "Türkiye" },
  italy: { code: "it", flag: "🇮🇹", name: "Italy" },
  italia: { code: "it", flag: "🇮🇹", name: "Italy" },
  it: { code: "it", flag: "🇮🇹", name: "Italy" },
  china: { code: "cn", flag: "🇨🇳", name: "China" },
  cn: { code: "cn", flag: "🇨🇳", name: "China" },
  hungary: { code: "hu", flag: "🇭🇺", name: "Hungary" },
  hu: { code: "hu", flag: "🇭🇺", name: "Hungary" },
  germany: { code: "de", flag: "🇩🇪", name: "Germany" },
  deutschland: { code: "de", flag: "🇩🇪", name: "Germany" },
  de: { code: "de", flag: "🇩🇪", name: "Germany" },
  pakistan: { code: "pk", flag: "🇵🇰", name: "Pakistan" },
  pk: { code: "pk", flag: "🇵🇰", name: "Pakistan" },
  "united states": { code: "us", flag: "🇺🇸", name: "United States" },
  "united states of america": { code: "us", flag: "🇺🇸", name: "United States" },
  usa: { code: "us", flag: "🇺🇸", name: "United States" },
  us: { code: "us", flag: "🇺🇸", name: "United States" },
  "united kingdom": { code: "gb", flag: "🇬🇧", name: "United Kingdom" },
  uk: { code: "gb", flag: "🇬🇧", name: "United Kingdom" },
  gb: { code: "gb", flag: "🇬🇧", name: "United Kingdom" },
  britain: { code: "gb", flag: "🇬🇧", name: "United Kingdom" },
  england: { code: "gb", flag: "🇬🇧", name: "United Kingdom" },
  scotland: { code: "gb", flag: "🇬🇧", name: "United Kingdom" },
  australia: { code: "au", flag: "🇦🇺", name: "Australia" },
  au: { code: "au", flag: "🇦🇺", name: "Australia" },
  canada: { code: "ca", flag: "🇨🇦", name: "Canada" },
  ca: { code: "ca", flag: "🇨🇦", name: "Canada" },
  japan: { code: "jp", flag: "🇯🇵", name: "Japan" },
  jp: { code: "jp", flag: "🇯🇵", name: "Japan" },
  korea: { code: "kr", flag: "🇰🇷", name: "South Korea" },
  "south korea": { code: "kr", flag: "🇰🇷", name: "South Korea" },
  "republic of korea": { code: "kr", flag: "🇰🇷", name: "South Korea" },
  kr: { code: "kr", flag: "🇰🇷", name: "South Korea" },
  "saudi arabia": { code: "sa", flag: "🇸🇦", name: "Saudi Arabia" },
  saudi: { code: "sa", flag: "🇸🇦", name: "Saudi Arabia" },
  sa: { code: "sa", flag: "🇸🇦", name: "Saudi Arabia" },
  qatar: { code: "qa", flag: "🇶🇦", name: "Qatar" },
  qa: { code: "qa", flag: "🇶🇦", name: "Qatar" },
  "united arab emirates": { code: "ae", flag: "🇦🇪", name: "United Arab Emirates" },
  uae: { code: "ae", flag: "🇦🇪", name: "United Arab Emirates" },
  ae: { code: "ae", flag: "🇦🇪", name: "United Arab Emirates" },
  romania: { code: "ro", flag: "🇷🇴", name: "Romania" },
  ro: { code: "ro", flag: "🇷🇴", name: "Romania" },
  sweden: { code: "se", flag: "🇸🇪", name: "Sweden" },
  se: { code: "se", flag: "🇸🇪", name: "Sweden" },
  switzerland: { code: "ch", flag: "🇨🇭", name: "Switzerland" },
  ch: { code: "ch", flag: "🇨🇭", name: "Switzerland" },
  france: { code: "fr", flag: "🇫🇷", name: "France" },
  fr: { code: "fr", flag: "🇫🇷", name: "France" },
  netherlands: { code: "nl", flag: "🇳🇱", name: "Netherlands" },
  holland: { code: "nl", flag: "🇳🇱", name: "Netherlands" },
  nl: { code: "nl", flag: "🇳🇱", name: "Netherlands" },
  ireland: { code: "ie", flag: "🇮🇪", name: "Ireland" },
  ie: { code: "ie", flag: "🇮🇪", name: "Ireland" },
  austria: { code: "at", flag: "🇦🇹", name: "Austria" },
  at: { code: "at", flag: "🇦🇹", name: "Austria" },
  malaysia: { code: "my", flag: "🇲🇾", name: "Malaysia" },
  my: { code: "my", flag: "🇲🇾", name: "Malaysia" },
  "new zealand": { code: "nz", flag: "🇳🇿", name: "New Zealand" },
  nz: { code: "nz", flag: "🇳🇿", name: "New Zealand" },
  singapore: { code: "sg", flag: "🇸🇬", name: "Singapore" },
  sg: { code: "sg", flag: "🇸🇬", name: "Singapore" },
  poland: { code: "pl", flag: "🇵🇱", name: "Poland" },
  pl: { code: "pl", flag: "🇵🇱", name: "Poland" },
  czechia: { code: "cz", flag: "🇨🇿", name: "Czech Republic" },
  "czech republic": { code: "cz", flag: "🇨🇿", name: "Czech Republic" },
  cz: { code: "cz", flag: "🇨🇿", name: "Czech Republic" },
  finland: { code: "fi", flag: "🇫🇮", name: "Finland" },
  fi: { code: "fi", flag: "🇫🇮", name: "Finland" },
  norway: { code: "no", flag: "🇳🇴", name: "Norway" },
  no: { code: "no", flag: "🇳🇴", name: "Norway" },
  denmark: { code: "dk", flag: "🇩🇰", name: "Denmark" },
  dk: { code: "dk", flag: "🇩🇰", name: "Denmark" },
  spain: { code: "es", flag: "🇪🇸", name: "Spain" },
  es: { code: "es", flag: "🇪🇸", name: "Spain" },
  portugal: { code: "pt", flag: "🇵🇹", name: "Portugal" },
  pt: { code: "pt", flag: "🇵🇹", name: "Portugal" },
  belgium: { code: "be", flag: "🇧🇪", name: "Belgium" },
  be: { code: "be", flag: "🇧🇪", name: "Belgium" },
  greece: { code: "gr", flag: "🇬🇷", name: "Greece" },
  gr: { code: "gr", flag: "🇬🇷", name: "Greece" },
  russia: { code: "ru", flag: "🇷🇺", name: "Russia" },
  ru: { code: "ru", flag: "🇷🇺", name: "Russia" },
  kuwait: { code: "kw", flag: "🇰🇼", name: "Kuwait" },
  kw: { code: "kw", flag: "🇰🇼", name: "Kuwait" },
  oman: { code: "om", flag: "🇴🇲", name: "Oman" },
  om: { code: "om", flag: "🇴🇲", name: "Oman" },
  taiwan: { code: "tw", flag: "🇹🇼", name: "Taiwan" },
  tw: { code: "tw", flag: "🇹🇼", name: "Taiwan" },
  thailand: { code: "th", flag: "🇹🇭", name: "Thailand" },
  th: { code: "th", flag: "🇹🇭", name: "Thailand" },
  brunei: { code: "bn", flag: "🇧🇳", name: "Brunei" },
  bn: { code: "bn", flag: "🇧🇳", name: "Brunei" },
  brazil: { code: "br", flag: "🇧🇷", name: "Brazil" },
  br: { code: "br", flag: "🇧🇷", name: "Brazil" },
  azerbaijan: { code: "az", flag: "🇦🇿", name: "Azerbaijan" },
  az: { code: "az", flag: "🇦🇿", name: "Azerbaijan" },
  estonia: { code: "ee", flag: "🇪🇪", name: "Estonia" },
  ee: { code: "ee", flag: "🇪🇪", name: "Estonia" },
  "hong kong": { code: "hk", flag: "🇭🇰", name: "Hong Kong" },
  hk: { code: "hk", flag: "🇭🇰", name: "Hong Kong" },
  luxembourg: { code: "lu", flag: "🇱🇺", name: "Luxembourg" },
  lu: { code: "lu", flag: "🇱🇺", name: "Luxembourg" },
  "european union": { code: "eu", flag: "🇪🇺", name: "European Union" },
  eu: { code: "eu", flag: "🇪🇺", name: "European Union" },
};

// Common institutional and program keyword aliases
const ALIAS_RULES: Array<{ match: (text: string) => boolean; code: string; flag: string; name: string }> = [
  // Turkey
  {
    match: (t) => t.includes("turk") || t.includes("burslari") || t.includes("ytb"),
    code: "tr", flag: "🇹🇷", name: "Türkiye",
  },
  // Italy
  {
    match: (t) => t.includes("ital") || t.includes("polimi") || t.includes("politecnico") || t.includes("dsu") || t.includes("edisu") || t.includes("padua") || t.includes("bologna"),
    code: "it", flag: "🇮🇹", name: "Italy",
  },
  // China
  {
    match: (t) => t.includes("chin") || t.includes("csc") || t.includes("cgsp") || t.includes("tsinghua") || t.includes("peking") || t.includes("beijing") || t.includes("zhejiang") || t.includes("anso"),
    code: "cn", flag: "🇨🇳", name: "China",
  },
  // Hungary
  {
    match: (t) => t.includes("hungar") || t.includes("stipendium") || t.includes("tempus") || t.includes("elte") || t.includes("budapest"),
    code: "hu", flag: "🇭🇺", name: "Hungary",
  },
  // Germany
  {
    match: (t) => t.includes("germ") || t.includes("daad") || t.includes("deutsch") || t.includes("berlin") || t.includes("sbw") || t.includes("munich") || t.includes("tum"),
    code: "de", flag: "🇩🇪", name: "Germany",
  },
  // Pakistan
  {
    match: (t) => t.includes("paki") || t.includes("hec") || t.includes("nust") || t.includes("bise") || t.includes("fast") || t.includes("giki"),
    code: "pk", flag: "🇵🇰", name: "Pakistan",
  },
  // United Kingdom
  {
    match: (t) => t.includes("kingd") || t.includes("brit") || t.includes("chevening") || t.includes("commonwealth") || t.includes("oxford") || t.includes("cambridge") || t.includes("scotland"),
    code: "gb", flag: "🇬🇧", name: "United Kingdom",
  },
  // United States
  {
    match: (t) => t.includes("americ") || t.includes("unit") || t.includes("fulbright") || t.includes("ugrad") || t.includes("stanford") || t.includes("mit") || t.includes("harvard") || t.includes("usa"),
    code: "us", flag: "🇺🇸", name: "United States",
  },
  // Australia
  {
    match: (t) => t.includes("austral") || t.includes("sydney") || t.includes("melbourne") || t.includes("unsw") || t.includes("anu"),
    code: "au", flag: "🇦🇺", name: "Australia",
  },
  // Canada
  {
    match: (t) => t.includes("cana") || t.includes("pearson") || t.includes("waterloo") || t.includes("toronto") || t.includes("calgary") || t.includes("mcgill") || t.includes("vanier"),
    code: "ca", flag: "🇨🇦", name: "Canada",
  },
  // Japan
  {
    match: (t) => t.includes("japan") || t.includes("mext") || t.includes("kyoto") || t.includes("tokyo") || t.includes("osaka"),
    code: "jp", flag: "🇯🇵", name: "Japan",
  },
  // South Korea
  {
    match: (t) => t.includes("korea") || t.includes("gks") || t.includes("kgsp") || t.includes("kaist") || t.includes("seoul"),
    code: "kr", flag: "🇰🇷", name: "South Korea",
  },
  // Saudi Arabia
  {
    match: (t) => t.includes("saud") || t.includes("kaust") || t.includes("kfupm") || t.includes("riyadh"),
    code: "sa", flag: "🇸🇦", name: "Saudi Arabia",
  },
  // Qatar
  {
    match: (t) => t.includes("qata") || t.includes("hbku") || t.includes("doha"),
    code: "qa", flag: "🇶🇦", name: "Qatar",
  },
  // UAE
  {
    match: (t) => t.includes("emir") || t.includes("uae") || t.includes("dubai") || t.includes("abu dhabi"),
    code: "ae", flag: "🇦🇪", name: "United Arab Emirates",
  },
  // Romania
  {
    match: (t) => t.includes("romani") || t.includes("arice") || t.includes("bucharest"),
    code: "ro", flag: "🇷🇴", name: "Romania",
  },
  // France
  {
    match: (t) => t.includes("fran") || t.includes("eiffel") || t.includes("paris") || t.includes("sorbonne"),
    code: "fr", flag: "🇫🇷", name: "France",
  },
  // Sweden
  {
    match: (t) => t.includes("swed") || t.includes("kth") || t.includes("lund") || t.includes("uppsala"),
    code: "se", flag: "🇸🇪", name: "Sweden",
  },
  // Netherlands
  {
    match: (t) => t.includes("nether") || t.includes("dutch") || t.includes("twente") || t.includes("delft") || t.includes("amsterdam"),
    code: "nl", flag: "🇳🇱", name: "Netherlands",
  },
];

function normalize(str: string): string {
  return str
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[🏛️🌍🎓]/g, "")
    .trim()
    .toLowerCase();
}

/**
 * Converts a 2-letter ISO country code (e.g. AU, DE, PK) to a flag emoji.
 */
export function isoCodeToFlag(code: string): string {
  if (!code || code.length !== 2) return "🎓";
  const upper = code.toUpperCase();
  if (!/^[A-Z]{2}$/.test(upper)) return "🎓";
  const codePoints = [...upper].map((char) => 127397 + char.charCodeAt(0));
  return String.fromCodePoint(...codePoints);
}

/**
 * Resolves 2-letter lowercase ISO country code for any country, scholarship name, or code.
 */
export function getCountryCode(countryOrName?: string | null): string {
  if (!countryOrName) return "un";
  const raw = normalize(countryOrName);
  if (!raw) return "un";

  // 1. Direct dictionary match
  if (COUNTRY_LOOKUP[raw]) {
    return COUNTRY_LOOKUP[raw].code;
  }

  // 2. Direct 2-letter ISO code conversion
  if (raw.length === 2 && /^[a-z]{2}$/.test(raw)) {
    return raw;
  }

  // 3. Substring rules
  for (const rule of ALIAS_RULES) {
    if (rule.match(raw)) {
      return rule.code;
    }
  }

  return "un";
}

/**
 * Returns the exact national flag emoji for any country name, nationality, or code.
 * Guaranteed to never return a generic globe emoji or temple glyph.
 */
export function getCountryFlag(countryInput?: string | null): string {
  if (!countryInput) return "🎓";
  const raw = normalize(countryInput);
  if (!raw) return "🎓";

  if (COUNTRY_LOOKUP[raw]) {
    return COUNTRY_LOOKUP[raw].flag;
  }

  if (raw.length === 2 && /^[a-z]{2}$/.test(raw)) {
    return isoCodeToFlag(raw);
  }

  for (const rule of ALIAS_RULES) {
    if (rule.match(raw)) {
      return rule.flag;
    }
  }

  const code = getCountryCode(countryInput);
  return code !== "un" ? isoCodeToFlag(code) : "🎓";
}

/**
 * Returns clean canonical country display name.
 */
export function getCountryName(countryInput?: string | null): string {
  if (!countryInput) return "International";
  const raw = normalize(countryInput);
  if (!raw) return "International";

  if (COUNTRY_LOOKUP[raw]) {
    return COUNTRY_LOOKUP[raw].name;
  }

  for (const rule of ALIAS_RULES) {
    if (rule.match(raw)) {
      return rule.name;
    }
  }

  return countryInput.trim();
}

const REGION_OR_GENERIC = new Set([
  "europe",
  "asia",
  "americas",
  "america",
  "oceania",
  "mena",
  "africa",
  "international",
  "global",
  "various",
  "un",
  "unknown",
  "none",
]);

/**
 * Robustly resolves the 2-letter ISO country code from hostCountry or scholarship name.
 * If hostCountry is generic (e.g. "Europe", "Asia", "International", "un"), it resolves from the scholarship name.
 */
export function resolveCountryCode(country?: string | null, name?: string | null): string {
  if (country) {
    const raw = normalize(country);
    if (!REGION_OR_GENERIC.has(raw)) {
      const code = getCountryCode(country);
      if (code !== "un") return code;
    }
  }

  if (name) {
    const code = getCountryCode(name);
    if (code !== "un") return code;
  }

  // Region fallback: European programs default to EU flag
  if (country) {
    const raw = normalize(country);
    if (raw === "europe") return "eu";
  }

  return "un";
}

/**
 * Robustly resolves the full English country name from hostCountry or scholarship name.
 */
export function resolveCountryName(country?: string | null, name?: string | null): string {
  const code = resolveCountryCode(country, name);
  if (code !== "un" && COUNTRY_LOOKUP[code]) {
    return COUNTRY_LOOKUP[code].name;
  }
  if (country) {
    const raw = normalize(country);
    if (!REGION_OR_GENERIC.has(raw)) {
      const nameFromCountry = getCountryName(country);
      if (nameFromCountry !== "International" && nameFromCountry !== "Unknown") {
        return nameFromCountry;
      }
    }
  }
  if (name) {
    const nameFromName = getCountryName(name);
    if (nameFromName !== "International" && nameFromName !== "Unknown") {
      return nameFromName;
    }
  }
  return country?.trim() || "International";
}

/**
 * Robustly resolves the official flag emoji from hostCountry or scholarship name.
 */
export function resolveCountryFlag(country?: string | null, name?: string | null): string {
  const code = resolveCountryCode(country, name);
  if (code !== "un") {
    return isoCodeToFlag(code);
  }
  return getCountryFlag(country || name);
}

