/**
 * Standard 4.0 GPA Conversion Scale (100% = 4.0 GPA).
 *
 * Direct Scale:
 * - 100.0% = 4.00 GPA
 * - 93.0%  = 3.72 GPA  ((93 / 100) * 4.0)
 * - 85.0%  = 3.40 GPA  ((85 / 100) * 4.0)
 * - 78.5%  = 3.14 GPA  ((78.5 / 100) * 4.0)
 * - 75.0%  = 3.00 GPA  ((75 / 100) * 4.0)
 * - 50.0%  = 2.00 GPA  ((50 / 100) * 4.0)
 */

export function percentageToGpa4(pct: number): number {
  if (isNaN(pct) || pct <= 0) return 0.0;
  const clamped = Math.min(100.0, Math.max(0.0, pct));
  const gpa = (clamped / 100.0) * 4.0;
  return parseFloat(gpa.toFixed(2));
}

export function gpaToPercentage(gpa: number): number {
  if (isNaN(gpa) || gpa <= 0) return 0.0;
  const clamped = Math.min(4.0, Math.max(0.0, gpa));
  const pct = (clamped / 4.0) * 100.0;
  return parseFloat(pct.toFixed(1));
}
