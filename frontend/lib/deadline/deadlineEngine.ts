export interface DeadlineRunwayResult {
  daysRemaining: number;
  displayDeadline: string;
  applicationDeadlineIso: string;
  prepDaysNeededPakistan: number;
  slackDays: number;
  feasibility: "FEASIBLE" | "TIGHT" | "CRITICAL";
  riskSummary: string;
}

/**
 * Calculates calendar runway and Pakistan administrative bottlenecks dynamically from database fields.
 * Replaces hardcoded `45 + (rank * 15)` fallbacks.
 */
export function calculateDeadlineRunway(
  scholarship: any,
  studentProfile?: any
): DeadlineRunwayResult {
  const rawDl =
    scholarship.application_deadline ||
    scholarship.deadline ||
    scholarship.applicationDeadline ||
    scholarship.deep_dossier?.important_dates_timeline?.application_deadline;

  const now = new Date();
  let deadlineDate: Date | null = null;
  let displayDeadline = "Annual Admission Intake 2026/2027";

  if (rawDl) {
    const parsed = new Date(rawDl);
    if (!isNaN(parsed.getTime())) {
      deadlineDate = parsed;
      displayDeadline = parsed.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
        year: "numeric",
      });
    } else {
      displayDeadline = String(rawDl);
    }
  }

  // If no parseable date, assume standard intake deadline ~90 days out
  if (!deadlineDate) {
    deadlineDate = new Date();
    deadlineDate.setDate(deadlineDate.getDate() + 90);
  }

  const diffMs = deadlineDate.getTime() - now.getTime();
  let daysRemaining = Math.ceil(diffMs / (1000 * 60 * 60 * 24));

  // If deadline has passed for past calendar year, project forward to upcoming cycle
  if (daysRemaining < 0) {
    const nextCycle = new Date(deadlineDate);
    nextCycle.setFullYear(now.getFullYear() + (now.getMonth() > deadlineDate.getMonth() ? 1 : 0));
    const nextDiffMs = nextCycle.getTime() - now.getTime();
    daysRemaining = Math.max(15, Math.ceil(nextDiffMs / (1000 * 60 * 60 * 24)));
    displayDeadline = nextCycle.toLocaleDateString("en-US", {
      month: "long",
      day: "numeric",
      year: "numeric",
    });
  }

  // Pakistan administrative preparation bottlenecks
  const needsIelts = !studentProfile?.language?.has_english_test &&
    scholarship.language?.english_test_required !== false;
  const needsHec = !studentProfile?.academic?.hec_attestation_done;
  const needsIbcc = studentProfile?.academic?.education_system === "CAMBRIDGE";

  let prepDaysNeededPakistan = 14; // Baseline document compilation
  if (needsHec) prepDaysNeededPakistan += 14; // HEC DAS turnaround
  if (needsIbcc) prepDaysNeededPakistan += 10; // IBCC equivalence turnaround
  if (needsIelts) prepDaysNeededPakistan += 21; // IELTS booking + result delivery

  const slackDays = daysRemaining - prepDaysNeededPakistan;

  let feasibility: "FEASIBLE" | "TIGHT" | "CRITICAL" = "FEASIBLE";
  let riskSummary = `Adequate preparation runway (${daysRemaining}d remaining; ${prepDaysNeededPakistan}d required).`;

  if (slackDays < 0) {
    feasibility = "CRITICAL";
    riskSummary = `Preparation bottleneck: Requires ${prepDaysNeededPakistan} days in Pakistan, but only ${daysRemaining} days remain before cutoff.`;
  } else if (slackDays < 20) {
    feasibility = "TIGHT";
    riskSummary = `Tight schedule: ${slackDays} buffer days remaining after mandatory Pakistani attestations.`;
  }

  return {
    daysRemaining,
    displayDeadline,
    applicationDeadlineIso: deadlineDate.toISOString().slice(0, 10),
    prepDaysNeededPakistan,
    slackDays,
    feasibility,
    riskSummary,
  };
}
