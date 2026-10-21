import { Scholarship, StudentProfile, Region } from "@/lib/types";

export interface CostBreakdownItem {
  itemName: string;
  costPkr: number;
  costUsd: number;
  isMandatory: boolean;
  notes?: string;
}

export interface PakistanCostResult {
  preApplicationPkr: number;
  applicationPkr: number;
  visaTravelPkr: number;
  settlementPkr: number;
  totalOutOfPocketPkr: number;
  monthlyStipendPkr: number;
  airfareCovered: boolean;
  dormitoryCovered: boolean;
  costItems: CostBreakdownItem[];
  riskWarnings: string[];
  isWithinBudget: boolean;
}

const EXCHANGE_RATES: Record<string, number> = {
  USD: 280,
  EUR: 305,
  GBP: 360,
  HUF: 0.77,
  TRY: 8.5,
  CNY: 39.0,
  AUD: 182,
  CAD: 204,
  JPY: 1.85,
};

/**
 * Calculates authentic out-of-pocket costs for a Pakistani student applying to a specific scholarship.
 * Replaces hardcoded regional ternary defaults with dynamic itemized arithmetic.
 */
export function calculatePakistanCosts(
  scholarship: any,
  studentProfile?: any
): PakistanCostResult {
  const region = (scholarship.region as Region) || "Asia";
  const hostCountry = String(
    scholarship.host_country_name || scholarship.hostCountry || scholarship.host_country || ""
  ).toUpperCase();
  const scName = String(scholarship.name || "").toLowerCase();

  const items: CostBreakdownItem[] = [];
  const warnings: string[] = [];

  let preAppPkr = 0;
  let appPkr = 0;
  let visaTravelPkr = 0;
  let settlePkr = 75000; // Standard 1st month settlement reserve

  // 1. Language Testing
  const studentHasTest = Boolean(
    studentProfile?.language?.has_english_test ||
    (studentProfile?.language?.english_proficiency_test &&
      !/none|not available/i.test(studentProfile.language.english_proficiency_test))
  );
  const moiAccepted = Boolean(
    scholarship.pakistan_requirements?.accepts_moi_certificate ||
    scholarship.deep_dossier?.eligibility_requirements?.moi_certificate_accepted
  );

  if (!studentHasTest && !moiAccepted) {
    const ieltsPkr = 76000;
    preAppPkr += ieltsPkr;
    items.push({
      itemName: "IELTS Academic Exam Fee (British Council / AEO Pakistan)",
      costPkr: ieltsPkr,
      costUsd: Math.round(ieltsPkr / EXCHANGE_RATES.USD),
      isMandatory: true,
      notes: "Computer-delivered academic test across major Pakistani cities.",
    });
  }

  // 2. HEC / IBCC Credentials Attestation
  const isCambridge = studentProfile?.academic?.education_system === "CAMBRIDGE" ||
    Boolean(studentProfile?.academic?.a_level_grades?.length);

  if (isCambridge) {
    const ibccPkr = 6000;
    preAppPkr += ibccPkr;
    items.push({
      itemName: "IBCC Foreign Equivalence Certificate (A-Levels to FSc)",
      costPkr: ibccPkr,
      costUsd: Math.round(ibccPkr / EXCHANGE_RATES.USD),
      isMandatory: true,
      notes: "Mandatory IBCC formula equivalence for foreign Cambridge credentials.",
    });
  } else {
    const hecAttestationPkr = 3000;
    preAppPkr += hecAttestationPkr;
    items.push({
      itemName: "HEC Degree / Transcript e-Attestation (DAS 1-Link)",
      costPkr: hecAttestationPkr,
      costUsd: Math.round(hecAttestationPkr / EXCHANGE_RATES.USD),
      isMandatory: true,
      notes: "Online digital attestation certificate on HEC portal.",
    });
  }

  // 3. Application Phase
  if (hostCountry.includes("GERMAN") || hostCountry === "DE") {
    const uniAssistPkr = 22875; // EUR 75
    appPkr += uniAssistPkr;
    items.push({
      itemName: "Uni-Assist Germany Application Fee (€75)",
      costPkr: uniAssistPkr,
      costUsd: Math.round(uniAssistPkr / EXCHANGE_RATES.USD),
      isMandatory: true,
      notes: "Standard German university preliminary verification dossier fee.",
    });
  }

  // 4. Visa & Medical & Character Clearance
  const vfsBiometricsPkr = 20000;
  const medicalExamPkr = 18000;
  const policeCertPkr = 3000;

  visaTravelPkr += vfsBiometricsPkr + medicalExamPkr + policeCertPkr;
  items.push({
    itemName: "VFS Global / Gerry's Biometric & Consular Appointment Service",
    costPkr: vfsBiometricsPkr,
    costUsd: Math.round(vfsBiometricsPkr / EXCHANGE_RATES.USD),
    isMandatory: true,
  });
  items.push({
    itemName: "Approved Panel Clinic Medical Examination (TB/Blood Screening)",
    costPkr: medicalExamPkr,
    costUsd: Math.round(medicalExamPkr / EXCHANGE_RATES.USD),
    isMandatory: true,
  });
  items.push({
    itemName: "Police Character Clearance Certificate (SSP Office)",
    costPkr: policeCertPkr,
    costUsd: Math.round(policeCertPkr / EXCHANGE_RATES.USD),
    isMandatory: true,
  });

  // Country-Specific Visa Fees
  const isVisaWaived =
    scName.includes("stipendium hungaricum") ||
    scName.includes("turkiye burslari") ||
    scName.includes("csc") ||
    scName.includes("chinese government") ||
    scName.includes("mext") ||
    scName.includes("romanian government");

  if (!isVisaWaived) {
    if (hostCountry.includes("UNITED KINGDOM") || hostCountry === "GB" || hostCountry === "UK") {
      const ukVisaPkr = 200880; // £558
      visaTravelPkr += ukVisaPkr;
      items.push({
        itemName: "UK Student Visa Application Fee (£558)",
        costPkr: ukVisaPkr,
        costUsd: Math.round(ukVisaPkr / EXCHANGE_RATES.USD),
        isMandatory: true,
      });
    } else if (hostCountry.includes("UNITED STATES") || hostCountry === "US" || hostCountry === "USA") {
      const usVisaPkr = 51800 + 98000; // DS-160 + SEVIS
      visaTravelPkr += usVisaPkr;
      items.push({
        itemName: "US DS-160 Visa Fee & SEVIS I-901 Fee ($535)",
        costPkr: usVisaPkr,
        costUsd: Math.round(usVisaPkr / EXCHANGE_RATES.USD),
        isMandatory: true,
      });
    } else if (region === "Europe") {
      const schengenPkr = 27450; // EUR 90
      visaTravelPkr += schengenPkr;
      items.push({
        itemName: "Schengen National Type-D Visa Fee (€90)",
        costPkr: schengenPkr,
        costUsd: Math.round(schengenPkr / EXCHANGE_RATES.USD),
        isMandatory: true,
      });
    }
  }

  // 5. Airfare Coverage
  const travelCoverage = String(scholarship.funding?.travel_airfare || "").toUpperCase();
  const deepAirfare = String(
    scholarship.deep_dossier?.financial_coverage_breakdown?.airfare?.status || ""
  ).toUpperCase();

  const isAirfareCovered =
    travelCoverage === "FULL" ||
    travelCoverage === "ROUND_TRIP" ||
    travelCoverage === "ANNUAL" ||
    deepAirfare.includes("COVERED") ||
    scName.includes("mext") ||
    scName.includes("fulbright") ||
    scName.includes("turkiye burslari");

  if (!isAirfareCovered) {
    let flightCostPkr = 180000;
    if (region === "Europe") flightCostPkr = 210000;
    else if (region === "Americas") flightCostPkr = 280000;
    else if (region === "Oceania") flightCostPkr = 310000;
    else if (region === "MENA") flightCostPkr = 140000;

    visaTravelPkr += flightCostPkr;
    items.push({
      itemName: `One-Way Commercial Airfare to ${region} from Pakistan`,
      costPkr: flightCostPkr,
      costUsd: Math.round(flightCostPkr / EXCHANGE_RATES.USD),
      isMandatory: true,
      notes: "Airfare is not included in this scholarship scheme.",
    });
    warnings.push(`International flight to ${hostCountry || region} (approx PKR ${flightCostPkr.toLocaleString()}) must be self-funded.`);
  }

  // 6. Monthly Stipend & Outlay Sum
  const rawStipend =
    scholarship.funding?.monthly_stipend_pkr_approx ||
    scholarship.monthly_stipend_pkr_approx ||
    scholarship.monthlyStipendPkr ||
    scholarship.monthly_stipend_pkr;

  let monthlyStipendPkr = typeof rawStipend === "number" && rawStipend > 0 ? rawStipend : 0;
  if (!monthlyStipendPkr) {
    if (scName.includes("chinese government") || scName.includes("csc")) {
      monthlyStipendPkr = 120000;
    } else if (scName.includes("stipendium hungaricum")) {
      monthlyStipendPkr = 35000;
    } else if (scName.includes("mext")) {
      monthlyStipendPkr = 270000;
    } else if (scName.includes("turkiye burslari")) {
      monthlyStipendPkr = 65000;
    } else if (scName.includes("romanian government") || scName.includes("arice")) {
      monthlyStipendPkr = 25000;
    } else if (scholarship.funding?.funding_type === "FULL" || scholarship.funding_type === "FULL") {
      monthlyStipendPkr = region === "Asia" ? 120000 : region === "Europe" ? 140000 : 250000;
    }
  }

  const totalOutOfPocketPkr = preAppPkr + appPkr + visaTravelPkr + settlePkr;
  const userBudget = Number(studentProfile?.preferences?.max_out_of_pocket_pkr || 250000);

  return {
    preApplicationPkr: preAppPkr,
    applicationPkr: appPkr,
    visaTravelPkr,
    settlementPkr: settlePkr,
    totalOutOfPocketPkr,
    monthlyStipendPkr,
    airfareCovered: isAirfareCovered,
    dormitoryCovered: Boolean(scholarship.deep_dossier?.financial_coverage_breakdown?.accommodation?.status?.includes("FREE")),
    costItems: items,
    riskWarnings: warnings,
    isWithinBudget: totalOutOfPocketPkr <= userBudget,
  };
}
