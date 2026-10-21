/**
 * Determines the maximum scholarship output cap based on target degree level:
 * - PhD / Doctorate: 30
 * - Master's / Graduate: 20
 * - Bachelor's / Undergraduate: 15
 * Defaults to 15 if unspecified or undergraduate.
 */
export function getDegreeScholarshipLimit(targetDegree?: string | null): number {
  if (!targetDegree) return 15;

  const tLower = targetDegree.toLowerCase().trim();
  if (tLower.includes("phd") || tLower.includes("doctor") || tLower.includes("postdoc")) {
    return 30;
  }
  if (
    tLower.includes("master") ||
    tLower.includes("ms") ||
    tLower.includes("msc") ||
    tLower.includes("mphil") ||
    tLower.includes("postgrad") ||
    tLower.includes("masc") ||
    tLower.includes("mcs") ||
    tLower.includes("18")
  ) {
    return 20;
  }
  if (
    tLower.includes("bachelor") ||
    tLower.includes("undergrad") ||
    tLower.includes("bs") ||
    tLower.includes("inter") ||
    tLower.includes("fsc") ||
    tLower.includes("ics") ||
    tLower.includes("fa") ||
    tLower.includes("a-level") ||
    tLower.includes("diploma") ||
    tLower.includes("12") ||
    tLower.includes("16")
  ) {
    return 15;
  }

  return 15;
}
