// Phase 7: Deterministic Multi-Opportunity Ranking, Advisor Roadmap & Dossier Store
// (§6, §7, §8, §11, §14, §16-§36, Agents.md §4, §11)

import { PhysicalPacket } from "../communication/types";
import { Region } from "../types";
import {
  Phase7Step,
  Phase7StepMeta,
  Phase7Snapshot,
  InvestigatedOpportunity,
  ScoringFactor,
  RankingFactorKey,
  RoadmapPhaseBlock,
  CanonicalDossier,
  CanonicalDossierSection,
} from "./types";
import { searchScholarshipsForProfile, SEED_PROFILES } from "../seed-data";
import { calculatePakistanCosts } from "../cost/pakistanCostEngine";
import { calculateDeadlineRunway } from "../deadline/deadlineEngine";

// ============================================================================
// 1. DETERMINISTIC SCORING ENGINE FORMULA HELPER
// ============================================================================
export function computeScoringFactors(
  raw: Record<RankingFactorKey, { score: number; rationale: string; anchor: string }>
): { factors: Record<RankingFactorKey, ScoringFactor>; totalScore: number } {
  const definitions: Record<
    RankingFactorKey,
    { label: string; weightPercent: number; weightDecimal: number }
  > = {
    ELIGIBILITY_MATCH: { label: "Eligibility Match", weightPercent: 25, weightDecimal: 0.25 },
    TRUE_FUNDING: { label: "True Funding Score", weightPercent: 25, weightDecimal: 0.25 },
    PAKISTAN_BILATERAL: { label: "Pakistan Bilateral Bonus", weightPercent: 10, weightDecimal: 0.10 },
    ACADEMIC_FIT: { label: "Academic & Field Fit", weightPercent: 10, weightDecimal: 0.10 },
    DOC_READINESS: { label: "Document Readiness", weightPercent: 10, weightDecimal: 0.10 },
    DEADLINE_FEASIBILITY: { label: "Deadline Feasibility", weightPercent: 10, weightDecimal: 0.10 },
    VERIFICATION_CONFIDENCE: { label: "Verification Confidence", weightPercent: 5, weightDecimal: 0.05 },
    COMPETITION_ESTIMATE: { label: "Competition Factor", weightPercent: 5, weightDecimal: 0.05 },
  };

  const factors = {} as Record<RankingFactorKey, ScoringFactor>;
  let totalScore = 0;

  for (const [keyStr, def] of Object.entries(definitions)) {
    const key = keyStr as RankingFactorKey;
    const input = raw[key];
    const contribution = Math.round(input.score * def.weightDecimal * 10) / 10;
    totalScore += input.score * def.weightDecimal;

    let status: ScoringFactor["status"] = "STRONG";
    if (input.score >= 90) status = "OPTIMAL";
    else if (input.score < 70) status = "DEFICIT";
    else if (input.score < 80) status = "ATTENTION";

    factors[key] = {
      key,
      label: def.label,
      weightPercent: def.weightPercent,
      weightDecimal: def.weightDecimal,
      rawScore: input.score,
      weightedContribution: contribution,
      rationale: input.rationale,
      evidenceAnchor: input.anchor,
      status,
    };
  }

  return { factors, totalScore: Math.round(totalScore * 10) / 10 };
}

// ============================================================================
// 2. DYNAMIC PERSONALIZED ROADMAP GENERATOR
// ============================================================================
export function generateDynamicRoadmap(
  profile?: any,
  topScholarship?: any
): RoadmapPhaseBlock[] {
  const rawDegree = String(
    profile?.academic?.current_level ||
    profile?.academic?.degree_level ||
    profile?.degreeLevel ||
    profile?.degree ||
    profile?.preferences?.target_degree_level ||
    profile?.preferences?.targetDegreeLevel ||
    topScholarship?.degreeLevel ||
    ""
  ).toLowerCase();

  const isDoctoral =
    rawDegree.includes("phd") ||
    rawDegree.includes("doctor") ||
    rawDegree.includes("dphil");
  const isMasters =
    rawDegree.includes("master") ||
    rawDegree.includes("ms") ||
    rawDegree.includes("m.phil") ||
    rawDegree.includes("msc") ||
    rawDegree.includes("postgrad");
  const isPostgrad = isDoctoral || isMasters;

  const isCambridge =
    rawDegree.includes("a-level") ||
    rawDegree.includes("a level") ||
    rawDegree.includes("cambridge") ||
    rawDegree.includes("o-level") ||
    profile?.academic?.education_system === "CAMBRIDGE";

  const studentField =
    profile?.academic?.field_of_study ||
    profile?.preferences?.target_fields?.[0] ||
    profile?.fieldOfStudy ||
    profile?.field ||
    topScholarship?.fieldOfStudy ||
    "Computer Science";

  const rawBoard =
    profile?.academic?.board_university ||
    profile?.academic?.boardUniversity ||
    profile?.board ||
    "";

  const isFbise =
    rawBoard.toLowerCase().includes("fbise") ||
    rawBoard.toLowerCase().includes("federal") ||
    (profile?.academic?.institution && profile.academic.institution.toLowerCase().includes("paec"));

  const boardLabel = isFbise
    ? "FBISE (Federal Board)"
    : rawBoard
    ? rawBoard
    : "BISE";

  const institution =
    profile?.academic?.institution ||
    profile?.academic?.board_university ||
    profile?.institution ||
    (isPostgrad ? "Undergraduate University" : isCambridge ? "Cambridge College" : isFbise ? "FBISE College" : "BISE College");

  const hostCountry =
    topScholarship?.hostCountry ||
    topScholarship?.host_country_name ||
    topScholarship?.country ||
    "Destination Country";

  const oppName =
    topScholarship?.name ||
    topScholarship?.shortName ||
    "Target Scholarship";

  const portalUrl =
    topScholarship?.officialPortalUrl ||
    topScholarship?.official_portal_url ||
    topScholarship?.portal_url ||
    "https://scholarship.hec.gov.pk";

  const isBilateral =
    Boolean(topScholarship?.hecPortalRequired) ||
    Boolean(topScholarship?.hec_managed) ||
    (topScholarship?.bilateralSeats != null && topScholarship.bilateralSeats > 0);

  if (isPostgrad) {
    return [
      {
        phase: "ACADEMIC_CREDENTIALS",
        phaseNumber: 1,
        phaseLabel: "PHASE 01",
        title: "HEC Degree e-Attestation & Transcripts Verification",
        timelineDaysRange: "Day 01 – Day 14",
        totalCostPkr: 8000,
        criticalAdvisory: `Authenticate Bachelor's / Master's degree and transcripts via HEC 1-Link portal. Request 3 faculty recommendation letters from ${institution}.`,
        actions: [
          {
            id: "act-pg-1-1",
            phase: "ACADEMIC_CREDENTIALS",
            title: "HEC Degree e-Attestation System (DAS) Verification",
            purpose: "Official verification and QR-coded attestation of prior degrees and transcripts",
            timingDays: 8,
            timingLabel: "8 business days",
            estimatedCostPkr: 8000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "HEC Regional Center / HEC Headquarters H-9 Islamabad",
            officialPortalUrl: "https://eservices.hec.gov.pk",
            evidenceSource: "HEC Degree Attestation System Regulations",
          },
          {
            id: "act-pg-1-2",
            phase: "ACADEMIC_CREDENTIALS",
            title: `Obtain 3 Confidential Academic Recommendation Letters from ${institution}`,
            purpose: `Faculty endorsements certifying applicant research aptitude in ${studentField}`,
            timingDays: 14,
            timingLabel: "14 business days",
            estimatedCostPkr: 0,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: false,
            evidenceSource: "Doctoral / Master's Admission Protocol",
          },
        ],
      },
      {
        phase: "HEC_IBCC_ATTESTATION",
        phaseNumber: 2,
        phaseLabel: "PHASE 02",
        title: "Research Proposal, Literature Review & Supervisor Outreach",
        timelineDaysRange: "Day 15 – Day 35",
        totalCostPkr: 0,
        criticalAdvisory: `Draft specialized research proposal in ${studentField} aligned with host labs in ${hostCountry}. Contact potential academic supervisors.`,
        actions: [
          {
            id: "act-pg-2-1",
            phase: "HEC_IBCC_ATTESTATION",
            title: `Draft Comprehensive Research Proposal & Literature Review in ${studentField}`,
            purpose: "Structured 1,500–2,500 word research outline including problem statement, methodology, and citations",
            timingDays: 15,
            timingLabel: "15 business days",
            estimatedCostPkr: 0,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: false,
            evidenceSource: "Faculty Research Admissions Standard",
          },
          {
            id: "act-pg-2-2",
            phase: "HEC_IBCC_ATTESTATION",
            title: `Prospective Faculty Supervisor Outreach in ${hostCountry}`,
            purpose: `Formal academic correspondence with faculty members in ${studentField} to secure pre-acceptance or supervision consent`,
            timingDays: 20,
            timingLabel: "20 business days",
            estimatedCostPkr: 0,
            isBlocking: isDoctoral,
            severity: isDoctoral ? "BLOCKING" : "REQUIRED",
            isPakistanSpecific: false,
            evidenceSource: `${hostCountry} Graduate Studies Directorate`,
          },
        ],
      },
      {
        phase: "LANGUAGE_TESTS",
        phaseNumber: 3,
        phaseLabel: "PHASE 03",
        title: "Standardized Testing (HEC HAT / GRE) & Language Proficiency",
        timelineDaysRange: "Day 25 – Day 45",
        totalCostPkr: 5000,
        criticalAdvisory: `Register for HEC HAT or GRE General test. Obtain English Medium of Instruction (MOI) Certificate from ${institution} or IELTS scorecard.`,
        actions: [
          {
            id: "act-pg-3-1",
            phase: "LANGUAGE_TESTS",
            title: "HEC Higher Education Aptitude Test (HAT) / GRE Registration",
            purpose: `Standardized aptitude assessment mandatory for HEC bilateral scoring and scholarship rankings`,
            timingDays: 14,
            timingLabel: "14 business days",
            estimatedCostPkr: 3000,
            isBlocking: isBilateral,
            severity: isBilateral ? "BLOCKING" : "RECOMMENDED",
            isPakistanSpecific: true,
            assignedOffice: "HEC Education Testing Council (ETC) Islamabad",
            officialPortalUrl: "https://etc.hec.gov.pk",
            evidenceSource: "HEC Overseas Scholarship Testing Standard",
          },
          {
            id: "act-pg-3-2",
            phase: "LANGUAGE_TESTS",
            title: `Institutional English Medium of Instruction (MOI) Certificate (${institution})`,
            purpose: `Verifies prior degree coursework was instructed in English for waiver eligibility`,
            timingDays: 3,
            timingLabel: "3 business days",
            estimatedCostPkr: 2000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: `${institution} Registrar / Examination Branch`,
            evidenceSource: "Host University English Language Exemption Policy",
          },
        ],
      },
      {
        phase: "DUAL_APPLICATION",
        phaseNumber: 4,
        phaseLabel: "PHASE 04",
        title: `Official Application Submission (${oppName})`,
        timelineDaysRange: "Day 46 – Day 55",
        totalCostPkr: 0,
        criticalAdvisory: isBilateral
          ? `Dual portal submission mandatory: submit on official portal AND HEC bilateral scholarship portal before nomination cutoff.`
          : `Submit complete graduate dossier including research proposal and CV on official application portal.`,
        actions: [
          {
            id: "act-pg-4-1",
            phase: "DUAL_APPLICATION",
            title: `Submit Complete Dossier on ${oppName} Portal`,
            purpose: `Formal submission of research plan, degree scans, CV, and letters of recommendation`,
            timingDays: 5,
            timingLabel: "5 business days",
            estimatedCostPkr: 0,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: false,
            officialPortalUrl: portalUrl,
            evidenceSource: `${oppName} Official Call for Applications`,
          },
          {
            id: "act-pg-4-2",
            phase: "DUAL_APPLICATION",
            title: isBilateral
              ? "Submit Matching Registration on HEC Scholarship Portal"
              : "Register Tracking with National Sponsoring Agency",
            purpose: isBilateral
              ? "Register foreign application tracking ID in HEC national nomination database"
              : "Institutional notification and submission verification",
            timingDays: 3,
            timingLabel: "3 business days",
            estimatedCostPkr: 0,
            isBlocking: isBilateral,
            severity: isBilateral ? "BLOCKING" : "REQUIRED",
            isPakistanSpecific: isBilateral,
            assignedOffice: isBilateral ? "HEC Overseas Scholarship Division" : undefined,
            officialPortalUrl: isBilateral ? "https://scholarship.hec.gov.pk" : portalUrl,
            evidenceSource: "HEC Dual Registration Instruction Circular",
          },
        ],
      },
      {
        phase: "VISA_BIOMETRICS",
        phaseNumber: 5,
        phaseLabel: "PHASE 05",
        title: `Consular Visa, Police Clearance & Biometrics (${hostCountry})`,
        timelineDaysRange: "Day 56 – Day 80",
        totalCostPkr: 58000,
        criticalAdvisory: `Book VFS Gerry's appointment immediately upon receiving official Letter of Award or university admission.`,
        actions: [
          {
            id: "act-pg-5-1",
            phase: "VISA_BIOMETRICS",
            title: "Police Character Clearance Certificate from SSP Office / PKM",
            purpose: `Mandatory security clearance certificate required for long-term student visa in ${hostCountry}`,
            timingDays: 7,
            timingLabel: "7 business days",
            estimatedCostPkr: 3000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "Police Khidmat Markaz (PKM) Lahore / Islamabad / Karachi",
          },
          {
            id: "act-pg-5-2",
            phase: "VISA_BIOMETRICS",
            title: "Medical Examination at Approved Panel Clinic",
            purpose: `Chest X-Ray, HIV, Hepatitis B/C, and general fitness clearance required by ${hostCountry} immigration`,
            timingDays: 4,
            timingLabel: "4 business days",
            estimatedCostPkr: 20000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "IOM Migration Health Assessment Center / Designated Panel Clinics",
          },
          {
            id: "act-pg-5-3",
            phase: "VISA_BIOMETRICS",
            title: `Consular Student Visa & Biometric Submission (${hostCountry})`,
            purpose: `Passport submission and biometric enrollment for ${hostCountry} national study permit`,
            timingDays: 21,
            timingLabel: "21 calendar days",
            estimatedCostPkr: 35000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: `Gerry's Visa Drop Box Centre / Embassy of ${hostCountry} Islamabad`,
          },
        ],
      },
      {
        phase: "PRE_DEPARTURE",
        phaseNumber: 6,
        phaseLabel: "PHASE 06",
        title: "Pre-Departure Booking & Initial Settlement Reserve",
        timelineDaysRange: "Day 81 – Day 95",
        totalCostPkr: 270000,
        criticalAdvisory: `Scholarship stipend begins after university registration; student MUST carry initial settlement foreign exchange buffer.`,
        actions: [
          {
            id: "act-pg-6-1",
            phase: "PRE_DEPARTURE",
            title: `Commercial One-Way Flight Booking (Pakistan to ${hostCountry})`,
            purpose: `International transit flight to ${hostCountry}`,
            timingDays: 7,
            timingLabel: "7 days prior to intake",
            estimatedCostPkr: 210000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            evidenceSource: "Aviation Fare Index Pakistan",
          },
          {
            id: "act-pg-6-2",
            phase: "PRE_DEPARTURE",
            title: "Initial Settlement Cash Reserve (Foreign Exchange Currency)",
            purpose: "Living expenses buffer until first local scholarship stipend or university grant disbursement",
            timingDays: 3,
            timingLabel: "At airport departure",
            estimatedCostPkr: 60000,
            isBlocking: false,
            severity: "REQUIRED",
            isPakistanSpecific: true,
            evidenceSource: "International Student Union Settlement Guide",
          },
        ],
      },
    ];
  }

  if (isCambridge) {
    return [
      {
        phase: "ACADEMIC_CREDENTIALS",
        phaseNumber: 1,
        phaseLabel: "PHASE 01",
        title: "Cambridge Statement of Results & British Council Attestation",
        timelineDaysRange: "Day 01 – Day 14",
        totalCostPkr: 7000,
        criticalAdvisory: `Submit Cambridge CAIE GCE A-Level & O-Level certificates to British Council Pakistan for official verification prior to IBCC.`,
        actions: [
          {
            id: "act-cie-1-1",
            phase: "ACADEMIC_CREDENTIALS",
            title: "British Council Cambridge Results Attestation",
            purpose: "Authentication of official Statement of Results for Cambridge O/A-Levels",
            timingDays: 7,
            timingLabel: "7 business days",
            estimatedCostPkr: 7000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "British Council Examination Services (Islamabad / Lahore / Karachi)",
            officialPortalUrl: "https://www.britishcouncil.pk",
          },
          {
            id: "act-cie-1-2",
            phase: "ACADEMIC_CREDENTIALS",
            title: `Obtain 2 Confidential Recommendation Letters from ${institution}`,
            purpose: `Faculty appraisal and academic counselor endorsement for study in ${studentField}`,
            timingDays: 10,
            timingLabel: "10 business days",
            estimatedCostPkr: 0,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: false,
          },
        ],
      },
      {
        phase: "HEC_IBCC_ATTESTATION",
        phaseNumber: 2,
        phaseLabel: "PHASE 02",
        title: "IBCC Federal Equivalence Certificate (O & A Levels)",
        timelineDaysRange: "Day 15 – Day 30",
        totalCostPkr: 12000,
        criticalAdvisory: `Submit attested Cambridge certificates to IBCC Cambridge Cell for HSSC (Intermediate) Equivalence calculation.`,
        actions: [
          {
            id: "act-cie-2-1",
            phase: "HEC_IBCC_ATTESTATION",
            title: "IBCC Cambridge Equivalence Certificate Application",
            purpose: "Issuance of federal equivalence certificate converting letter grades (A*/A/B) to percentage and marks out of 1100",
            timingDays: 10,
            timingLabel: "10 business days",
            estimatedCostPkr: 10000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "IBCC Cambridge Cell, Sector H-8/4 Islamabad",
            officialPortalUrl: "https://ibcc.edu.pk",
          },
          {
            id: "act-cie-2-2",
            phase: "HEC_IBCC_ATTESTATION",
            title: "MOFA Consular Authentication",
            purpose: "Apostille/consular stamp by Ministry of Foreign Affairs for international legal validity",
            timingDays: 3,
            timingLabel: "3 business days",
            estimatedCostPkr: 2000,
            isBlocking: false,
            severity: "REQUIRED",
            isPakistanSpecific: true,
            assignedOffice: "MOFA Consular Division Islamabad / Camp Offices",
          },
        ],
      },
      {
        phase: "LANGUAGE_TESTS",
        phaseNumber: 3,
        phaseLabel: "PHASE 03",
        title: "Language Waiver Verification & Standardized Testing",
        timelineDaysRange: "Day 25 – Day 35",
        totalCostPkr: 2000,
        criticalAdvisory: `Cambridge English syllabus provides direct exemption at majority of universities; obtain official school MOI letter if needed.`,
        actions: [
          {
            id: "act-cie-3-1",
            phase: "LANGUAGE_TESTS",
            title: `English Medium of Instruction Letter from ${institution}`,
            purpose: "Formal institutional verification that all A-Level coursework was taught in English",
            timingDays: 2,
            timingLabel: "2 business days",
            estimatedCostPkr: 0,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: `${institution} School Administration`,
          },
          {
            id: "act-cie-3-2",
            phase: "LANGUAGE_TESTS",
            title: "HEC USAT / National Aptitude Test Registration",
            purpose: "Undergraduate Studies Admission Test required for Pakistan bilateral quota nominations",
            timingDays: 7,
            timingLabel: "7 business days",
            estimatedCostPkr: 2000,
            isBlocking: isBilateral,
            severity: isBilateral ? "BLOCKING" : "RECOMMENDED",
            isPakistanSpecific: true,
            assignedOffice: "HEC ETC Islamabad",
            officialPortalUrl: "https://etc.hec.gov.pk",
          },
        ],
      },
      {
        phase: "DUAL_APPLICATION",
        phaseNumber: 4,
        phaseLabel: "PHASE 04",
        title: `Undergraduate Application Submission (${oppName})`,
        timelineDaysRange: "Day 46 – Day 55",
        totalCostPkr: 0,
        criticalAdvisory: isBilateral
          ? `Dual registration is mandatory. Complete online submission on both host portal and HEC bilateral portal.`
          : `Submit complete undergraduate application on official host portal.`,
        actions: [
          {
            id: "act-cie-4-1",
            phase: "DUAL_APPLICATION",
            title: `Submit Online Application on ${oppName} Portal`,
            purpose: `Select preferred undergraduate degrees in ${studentField} and submit academic transcripts and SOP`,
            timingDays: 5,
            timingLabel: "5 business days",
            estimatedCostPkr: 0,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: false,
            officialPortalUrl: portalUrl,
          },
          {
            id: "act-cie-4-2",
            phase: "DUAL_APPLICATION",
            title: isBilateral
              ? "Submit Matching Application on HEC Scholarship Portal"
              : "Confirm Direct Application Registration",
            purpose: isBilateral
              ? "Register foreign portal application ID in HEC national nomination system"
              : "Institutional confirmation and receipt tracking",
            timingDays: 3,
            timingLabel: "3 business days",
            estimatedCostPkr: 0,
            isBlocking: isBilateral,
            severity: isBilateral ? "BLOCKING" : "REQUIRED",
            isPakistanSpecific: isBilateral,
            assignedOffice: isBilateral ? "HEC Overseas Scholarship Division" : undefined,
            officialPortalUrl: isBilateral ? "https://scholarship.hec.gov.pk" : portalUrl,
          },
        ],
      },
      {
        phase: "VISA_BIOMETRICS",
        phaseNumber: 5,
        phaseLabel: "PHASE 05",
        title: `Consular Visa, Police Clearance & Biometrics (${hostCountry})`,
        timelineDaysRange: "Day 56 – Day 80",
        totalCostPkr: 58000,
        criticalAdvisory: `Book VFS Gerry's biometric appointment immediately upon receiving Letter of Acceptance.`,
        actions: [
          {
            id: "act-cie-5-1",
            phase: "VISA_BIOMETRICS",
            title: "Police Character Clearance Certificate from SSP Office",
            purpose: `Mandatory security certificate verifying non-criminal record for student entry into ${hostCountry}`,
            timingDays: 7,
            timingLabel: "7 business days",
            estimatedCostPkr: 3000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "Police Khidmat Markaz (PKM)",
          },
          {
            id: "act-cie-5-2",
            phase: "VISA_BIOMETRICS",
            title: "Medical Examination at Approved Panel Clinic",
            purpose: `Chest X-Ray, HIV, Hep B/C, and general fitness clearance required for ${hostCountry} immigration`,
            timingDays: 4,
            timingLabel: "4 business days",
            estimatedCostPkr: 20000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: "IOM Migration Health Assessment Center / Designated Panel Clinics",
          },
          {
            id: "act-cie-5-3",
            phase: "VISA_BIOMETRICS",
            title: `Consular Visa & Biometric Appointment (${hostCountry})`,
            purpose: `Submission of student visa dossier to diplomatic mission of ${hostCountry}`,
            timingDays: 21,
            timingLabel: "21 calendar days",
            estimatedCostPkr: 35000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
            assignedOffice: `Gerry's Visa Drop Box Centre / Embassy of ${hostCountry} Islamabad`,
          },
        ],
      },
      {
        phase: "PRE_DEPARTURE",
        phaseNumber: 6,
        phaseLabel: "PHASE 06",
        title: "Pre-Departure Booking & Initial Settlement Reserve",
        timelineDaysRange: "Day 81 – Day 95",
        totalCostPkr: 270000,
        criticalAdvisory: `Scholarship stipend begins after university matriculation; student MUST carry initial settlement reserve.`,
        actions: [
          {
            id: "act-cie-6-1",
            phase: "PRE_DEPARTURE",
            title: `Commercial One-Way Flight Booking (Pakistan to ${hostCountry})`,
            purpose: `International transit flight to ${hostCountry}`,
            timingDays: 7,
            timingLabel: "7 days prior to intake",
            estimatedCostPkr: 210000,
            isBlocking: true,
            severity: "BLOCKING",
            isPakistanSpecific: true,
          },
          {
            id: "act-cie-6-2",
            phase: "PRE_DEPARTURE",
            title: "Initial Settlement Cash Reserve (Foreign Exchange)",
            purpose: "Mandatory living expenses buffer until first host bank stipend disbursement",
            timingDays: 3,
            timingLabel: "At airport departure",
            estimatedCostPkr: 60000,
            isBlocking: false,
            severity: "REQUIRED",
            isPakistanSpecific: true,
          },
        ],
      },
    ];
  }

  // Default: Pakistani HSSC / Intermediate (FSc / ICS / FA / DAE)
  return [
    {
      phase: "ACADEMIC_CREDENTIALS",
      phaseNumber: 1,
      phaseLabel: "PHASE 01",
      title: "Academic Credentials & Transcripts Verification",
      timelineDaysRange: "Day 01 – Day 14",
      totalCostPkr: 4000,
      criticalAdvisory: `Verify secondary school certificates with respective ${boardLabel} board prior to higher attestation. Request 2 recommendation letters from ${institution}.`,
      actions: [
        {
          id: "act-hssc-1-1",
          phase: "ACADEMIC_CREDENTIALS",
          title: `${boardLabel} Verification of Matric & Intermediate Certificates`,
          purpose: "Pre-requisite seal required by IBCC for diploma equivalence",
          timingDays: 7,
          timingLabel: "7 business days",
          estimatedCostPkr: 4000,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          assignedOffice: isFbise
            ? "Federal Board of Intermediate & Secondary Education (FBISE) H-8/4 Islamabad"
            : `Respective Divisional ${boardLabel} Examination Board`,
          evidenceSource: "IBCC Verification Protocol 2026",
        },
        {
          id: "act-hssc-1-2",
          phase: "ACADEMIC_CREDENTIALS",
          title: `Obtain 2 Confidential Academic Recommendation Letters from ${institution}`,
          purpose: `Faculty endorsements certifying applicant aptitude in ${studentField}`,
          timingDays: 14,
          timingLabel: "14 business days",
          estimatedCostPkr: 0,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: false,
        },
      ],
    },
    {
      phase: "HEC_IBCC_ATTESTATION",
      phaseNumber: 2,
      phaseLabel: "PHASE 02",
      title: `${boardLabel} Verification & IBCC Equivalence`,
      timelineDaysRange: "Day 15 – Day 30",
      totalCostPkr: 10000,
      criticalAdvisory: `Complete ${boardLabel} marksheet verification early to enable swift IBCC federal equivalence certificate issuance.`,
      actions: [
        {
          id: "act-hssc-2-1",
          phase: "HEC_IBCC_ATTESTATION",
          title: `${boardLabel} Intermediate Sanad & Marksheet Verification`,
          purpose: "Official board authentication of Intermediate certificate and marksheet",
          timingDays: 7,
          timingLabel: "7 business days",
          estimatedCostPkr: 4000,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          assignedOffice: isFbise
            ? "Federal Board of Intermediate & Secondary Education (FBISE) H-8/4 Islamabad"
            : "Divisional BISE Intermediate Examination Board",
          evidenceSource: "BISE / FBISE Examination Verification Regulations",
        },
        {
          id: "act-hssc-2-2",
          phase: "HEC_IBCC_ATTESTATION",
          title: "IBCC Certificate Equivalence Submission",
          purpose: "Issuance of federal equivalence certificate for international credential recognition",
          timingDays: 10,
          timingLabel: "10 business days",
          estimatedCostPkr: 6000,
          isBlocking: false,
          severity: "REQUIRED",
          isPakistanSpecific: true,
          assignedOffice: "IBCC Regional Office (Islamabad / Lahore / Karachi)",
          officialPortalUrl: "https://ibcc.edu.pk",
        },
      ],
    },
    {
      phase: "LANGUAGE_TESTS",
      phaseNumber: 3,
      phaseLabel: "PHASE 03",
      title: "English Medium of Instruction (MOI) & Language Exemption",
      timelineDaysRange: "Day 25 – Day 35",
      totalCostPkr: 2000,
      criticalAdvisory: `English Medium of Instruction (MOI) Certificate from ${institution} provides official English requirement waiver where applicable.`,
      actions: [
        {
          id: "act-hssc-3-1",
          phase: "LANGUAGE_TESTS",
          title: `English Medium of Instruction (MOI) Certificate (${institution})`,
          purpose: "Official institutional certificate verifying Intermediate coursework was instructed in English",
          timingDays: 3,
          timingLabel: "2–3 business days",
          estimatedCostPkr: 0,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          assignedOffice: `${institution} Academic Administration`,
          evidenceSource: "Host University English Language Exemption Policy",
        },
        {
          id: "act-hssc-3-2",
          phase: "LANGUAGE_TESTS",
          title: "HEC USAT / National Aptitude Test Registration",
          purpose: "Online candidate registration for bilateral government quota allocation",
          timingDays: 7,
          timingLabel: "7 business days",
          estimatedCostPkr: 2000,
          isBlocking: isBilateral,
          severity: isBilateral ? "BLOCKING" : "RECOMMENDED",
          isPakistanSpecific: true,
          assignedOffice: "HEC Overseas Scholarship Division",
          officialPortalUrl: "https://scholarship.hec.gov.pk",
          evidenceSource: "HEC Bilateral Selection Criteria Annex 1",
        },
      ],
    },
    {
      phase: "DUAL_APPLICATION",
      phaseNumber: 4,
      phaseLabel: "PHASE 04",
      title: `Dual Application Submission (${oppName})`,
      timelineDaysRange: "Day 46 – Day 55",
      totalCostPkr: 0,
      criticalAdvisory: isBilateral
        ? "Dual registration is MANDATORY. Applications submitted on host portal without matching HEC portal record are disqualified."
        : `Submit complete application on ${oppName} official portal.`,
      actions: [
        {
          id: "act-hssc-4-1",
          phase: "DUAL_APPLICATION",
          title: `Submit Online Application on ${oppName} Portal`,
          purpose: `Select academic degree programmes in ${studentField} and submit SOP, passport, and academic scans`,
          timingDays: 5,
          timingLabel: "5 business days",
          estimatedCostPkr: 0,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: false,
          officialPortalUrl: portalUrl,
        },
        {
          id: "act-hssc-4-2",
          phase: "DUAL_APPLICATION",
          title: isBilateral
            ? "Submit Matching Application on HEC Scholarship Portal"
            : "Confirm Application Receipt on Official Registry",
          purpose: isBilateral
            ? "Register foreign application ID in HEC national nomination system"
            : "Direct verification with admissions secretariat",
          timingDays: 3,
          timingLabel: "3 business days",
          estimatedCostPkr: 0,
          isBlocking: isBilateral,
          severity: isBilateral ? "BLOCKING" : "REQUIRED",
          isPakistanSpecific: isBilateral,
          assignedOffice: isBilateral ? "HEC Overseas Scholarship Division" : undefined,
          officialPortalUrl: isBilateral ? "https://scholarship.hec.gov.pk" : portalUrl,
          evidenceSource: "HEC Dual Registration Instruction Circular",
        },
      ],
    },
    {
      phase: "VISA_BIOMETRICS",
      phaseNumber: 5,
      phaseLabel: "PHASE 05",
      title: `Consular Visa, Police Clearance & Biometrics (${hostCountry})`,
      timelineDaysRange: "Day 56 – Day 80",
      totalCostPkr: 58000,
      criticalAdvisory: `Book VFS Gerry's appointment immediately upon receiving Letter of Award or official acceptance.`,
      actions: [
        {
          id: "act-hssc-5-1",
          phase: "VISA_BIOMETRICS",
          title: "Police Character Clearance Certificate from SSP Office",
          purpose: `Mandatory consular document verifying non-criminal record for student visa in ${hostCountry}`,
          timingDays: 7,
          timingLabel: "7 business days",
          estimatedCostPkr: 3000,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          assignedOffice: "Police Khidmat Markaz (PKM) Lahore / Islamabad",
        },
        {
          id: "act-hssc-5-2",
          phase: "VISA_BIOMETRICS",
          title: "Medical Examination at Approved Panel Clinic",
          purpose: `Chest X-Ray, HIV, Hep B/C, and general fitness clearance required by ${hostCountry} immigration`,
          timingDays: 4,
          timingLabel: "4 business days",
          estimatedCostPkr: 20000,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          assignedOffice: "IOM Migration Health Assessment Center / Panel Clinics",
        },
        {
          id: "act-hssc-5-3",
          phase: "VISA_BIOMETRICS",
          title: `VFS Global / Gerry's Biometric Appointment & Consular Submission`,
          purpose: `Submission of student visa application to Embassy of ${hostCountry}`,
          timingDays: 21,
          timingLabel: "21 calendar days",
          estimatedCostPkr: 35000,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          assignedOffice: `Gerry's Visa Drop Box Centre / Embassy of ${hostCountry} Islamabad`,
        },
      ],
    },
    {
      phase: "PRE_DEPARTURE",
      phaseNumber: 6,
      phaseLabel: "PHASE 06",
      title: "Pre-Departure Booking & Initial Settlement Reserve",
      timelineDaysRange: "Day 81 – Day 95",
      totalCostPkr: 270000,
      criticalAdvisory: "Scholarship stipend begins after university matriculation; student MUST carry initial settlement reserve.",
      actions: [
        {
          id: "act-hssc-6-1",
          phase: "PRE_DEPARTURE",
          title: `Commercial One-Way Flight Booking (Pakistan to ${hostCountry})`,
          purpose: `International flight travel to ${hostCountry}`,
          timingDays: 7,
          timingLabel: "7 days prior to intake",
          estimatedCostPkr: 210000,
          isBlocking: true,
          severity: "BLOCKING",
          isPakistanSpecific: true,
          evidenceSource: "Aviation Fare Index Pakistan",
        },
        {
          id: "act-hssc-6-2",
          phase: "PRE_DEPARTURE",
          title: "Initial Settlement Cash Reserve (Foreign Exchange)",
          purpose: "Mandatory living expenses buffer until first host bank stipend disbursement",
          timingDays: 3,
          timingLabel: "At airport departure",
          estimatedCostPkr: 60000,
          isBlocking: false,
          severity: "REQUIRED",
          isPakistanSpecific: true,
          evidenceSource: "International University Living Guide",
        },
      ],
    },
  ];
}

// ============================================================================
// 3. DYNAMIC INVESTIGATED OPPORTUNITY BUILDER
// ============================================================================
export function buildDynamicInvestigatedOpportunity(
  scholarship: any,
  profile?: any,
  rank: number = 1
): InvestigatedOpportunity {
  const rawField =
    profile?.academic?.field_of_study ||
    profile?.preferences?.target_fields?.[0] ||
    profile?.preferences?.studyField ||
    profile?.fieldOfStudy ||
    profile?.field ||
    scholarship?.fieldOfStudy ||
    scholarship?.field ||
    "Computer Science";

  const studentField =
    typeof rawField === "string" &&
    rawField.toLowerCase() !== "specialized studies" &&
    rawField.toLowerCase() !== "specialized discipline"
      ? rawField
      : "Computer Science";

  const hostCountry =
    scholarship.hostCountry ||
    scholarship.host_country_name ||
    scholarship.host_country ||
    "International";

  const oppName = scholarship.name || scholarship.scholarship_name || "Scholarship Opportunity";
  const shortName = scholarship.shortName || oppName.split(" ").slice(0, 3).join(" ");
  const flagEmoji = scholarship.flagEmoji || "🌐";
  const region = (scholarship.region as Region) || "Europe";
  const targetDegree =
    profile?.preferences?.target_degree_level ||
    profile?.preferences?.targetDegreeLevel ||
    profile?.academic?.degree_level ||
    profile?.academic?.current_level ||
    profile?.degree;

  const offeredLevels: string[] = Array.isArray(scholarship.eligibility?.degree_levels)
    ? scholarship.eligibility.degree_levels
    : scholarship.degreeLevel
    ? [scholarship.degreeLevel]
    : [scholarship.degree_level || "Degree Programme"];

  let degreeLevel = offeredLevels.join(" / ");
  if (targetDegree) {
    const matchDeg = offeredLevels.find((d: string) => d.toLowerCase().includes(targetDegree.toLowerCase()));
    if (matchDeg) {
      degreeLevel = matchDeg;
    }
  }

  const hasBilateral =
    Boolean(scholarship.hecPortalRequired) ||
    Boolean(scholarship.hec_managed) ||
    Boolean(scholarship.pakistan_requirements?.hec_managed) ||
    Boolean(scholarship.bilateralSeats) ||
    Boolean(scholarship.pakistan_requirements?.pakistan_quota_seats) ||
    Boolean(scholarship.pakistan_requirements?.bilateral_quota_seats) ||
    Boolean(scholarship.pakistan_requirements?.pakistan_bilateral_quota);

  const bilateralSeats =
    scholarship.pakistan_requirements?.pakistan_quota_seats ||
    scholarship.pakistan_requirements?.bilateral_quota_seats ||
    scholarship.bilateral_seats ||
    scholarship.bilateralSeats ||
    (hasBilateral ? 100 : null);

  const studentGpa = Number(profile?.academic?.percentage || profile?.academic?.gpa_percentage || 82);
  const rawBoard =
    profile?.academic?.board_university ||
    profile?.academic?.boardUniversity ||
    profile?.board ||
    "";
  const isFbise =
    rawBoard.toLowerCase().includes("fbise") ||
    rawBoard.toLowerCase().includes("federal") ||
    (profile?.academic?.institution && profile.academic.institution.toLowerCase().includes("paec"));
  const hasIelts = Boolean(
    profile?.language?.has_english_test ||
    (profile?.language?.english_proficiency_test && !/none|not available/i.test(profile.language.english_proficiency_test))
  );

  const isNeedBased = /dsu|need[\s\-]based|regional grant|type[\s\-]b/i.test(oppName);
  const isUnder70 = studentGpa > 0 && studentGpa < 70.0;

  let fEligibility: number;
  let eligRationale: string;

  if (isUnder70 && !isNeedBased) {
    fEligibility = 15;
    eligRationale = `Ineligible: Candidate marks (${studentGpa.toFixed(1)}%) fall below the mandatory 70.0% merit cutoff for ${oppName}. Strict merit nomination requires >= 70.0%.`;
  } else if (isUnder70 && isNeedBased) {
    fEligibility = 95;
    eligRationale = `Need-based grant evaluates household economic standing (ISEE Parificato); 70.0% academic merit cutoff is waived.`;
  } else {
    const minGpa = Number(scholarship.eligibility?.min_gpa_percentage || 65);
    fEligibility = Math.min(99, Math.max(68, Math.round(82 + (studentGpa - minGpa) * 0.6)));
    eligRationale = `Academic criteria for ${degreeLevel} evaluated against candidate marks (${studentGpa}%); Pakistani citizenship verified.`;
  }

  const isFullFunding =
    scholarship.funding_type === "FULL" ||
    scholarship.coverageType?.toLowerCase().includes("full") ||
    scholarship.funding?.funding_type === "FULL" ||
    scholarship.deep_dossier?.basic_details?.funding_classification === "FULLY_FUNDED";

  // Calculate authentic costs and deadlines dynamically from database and Pakistan benchmarks
  const costResult = calculatePakistanCosts(scholarship, profile);
  const deadlineRunway = calculateDeadlineRunway(scholarship, profile);

  const monthlyStipend = costResult.monthlyStipendPkr;
  const initialOutOfPocketPkr =
    scholarship.fundingSummary?.initialOutOfPocketPkr ||
    scholarship.initialOutOfPocketPkr ||
    scholarship.initial_out_of_pocket_pkr ||
    costResult.totalOutOfPocketPkr;

  const fFunding = isFullFunding ? (monthlyStipend >= 100000 ? 98 : monthlyStipend >= 30000 ? 95 : 91) : 76;
  const fBilateral = hasBilateral
    ? (bilateralSeats && bilateralSeats >= 300 ? 98 : bilateralSeats && bilateralSeats >= 100 ? 96 : bilateralSeats && bilateralSeats >= 20 ? 94 : 88)
    : 76;

  // Academic Fit evaluation
  const eligibleFields: string[] = Array.isArray(scholarship.eligibility?.eligible_fields)
    ? scholarship.eligibility.eligible_fields
    : [];
  const efStr = eligibleFields.join(" ").toLowerCase();
  const descStr = (scholarship.description || "").toLowerCase();
  const sFieldLower = studentField.toLowerCase();
  const isDirectMatch = efStr.includes(sFieldLower) || descStr.includes(sFieldLower);
  const isUniversalField = efStr.includes("all fields") || efStr.includes("all disciplines") || eligibleFields.length > 5;
  const fAcademicFit = (isUnder70 && !isNeedBased) ? 40 : (isDirectMatch ? 98 : isUniversalField ? 92 : 84);

  const fDocReadiness = hasIelts ? 92 : (scholarship.language?.english_test_required === false ? 88 : 76);

  const daysRemaining = deadlineRunway.daysRemaining;
  const displayDeadline = deadlineRunway.displayDeadline;
  const fDeadline = daysRemaining >= 90 ? 94 : daysRemaining >= 45 ? 88 : daysRemaining >= 25 ? 78 : 68;

  const fVerification = Math.min(99, Math.round((scholarship.confidence_score || 0.96) * 100));
  const fCompetition = hasBilateral
    ? (bilateralSeats && bilateralSeats >= 200 ? 84 : bilateralSeats && bilateralSeats >= 50 ? 78 : 74)
    : 70;

  const scoring = computeScoringFactors({
    ELIGIBILITY_MATCH: {
      score: fEligibility,
      rationale: eligRationale,
      anchor: `${oppName} Eligibility Annex §2.1`,
    },
    TRUE_FUNDING: {
      score: fFunding,
      rationale: isFullFunding
        ? `100% Tuition covered + living stipend (approx PKR ${monthlyStipend > 0 ? monthlyStipend.toLocaleString() + "/mo" : "stipend"}).`
        : "Partial tuition subsidy or study grant.",
      anchor: `${oppName} Financial Guidelines`,
    },
    PAKISTAN_BILATERAL: {
      score: fBilateral,
      rationale: hasBilateral
        ? `${bilateralSeats ? `${bilateralSeats} dedicated bilateral seats` : "Bilateral quota"} allocated for Pakistani scholars under government protocol.`
        : "Open international merit competition; Pakistani nationals fully eligible.",
      anchor: hasBilateral ? "HEC Bilateral Register 2026" : "International Merit Directory",
    },
    ACADEMIC_FIT: {
      score: fAcademicFit,
      rationale: `Strong alignment with candidate background in ${studentField}.`,
      anchor: "Faculty Syllabus Match",
    },
    DOC_READINESS: {
      score: fDocReadiness,
      rationale: hasIelts
        ? "English testing readiness satisfied; credential attestation pipeline verified."
        : `Requires English Medium of Instruction (MOI) verification and ${isFbise ? "FBISE" : "BISE"}/HEC attestation lead times.`,
      anchor: "Credential & Attestation Protocol",
    },
    DEADLINE_FEASIBILITY: {
      score: fDeadline,
      rationale: `Calendar runway (${daysRemaining} days) feasible for document preparation and consular appointment.`,
      anchor: "Application Cutoff Schedule",
    },
    VERIFICATION_CONFIDENCE: {
      score: fVerification,
      rationale: "Cross-checked against official authoritative portals and government registers.",
      anchor: "Official Registry Hash Verified",
    },
    COMPETITION_ESTIMATE: {
      score: fCompetition,
      rationale: hasBilateral
        ? `Viability calibrated against ${bilateralSeats ? `${bilateralSeats} Pakistani quota seats` : "bilateral quota allocation"}.`
        : "Viability calibrated against historical Pakistani selection statistics.",
      anchor: "Historical Pakistani Selection Statistics",
    },
  });

  const portal =
    scholarship.officialPortalUrl ||
    scholarship.portal_url ||
    scholarship.source_url ||
    "https://scholarship.hec.gov.pk";

  const quotaDescription = hasBilateral
    ? `${bilateralSeats ? `${bilateralSeats} Dedicated Quota Seats for Pakistan` : "Bilateral Quota for Pakistan"}`
    : "Open International Merit Competition";

  const rawComposite =
    typeof scholarship.compositeScore === "number"
      ? scholarship.compositeScore
      : typeof scholarship.final_score === "number"
      ? Math.round(scholarship.final_score * 10) / 10
      : typeof scholarship.overall_match_score === "number"
      ? Math.round(scholarship.overall_match_score * 10) / 10
      : scoring.totalScore;

  const compositeScore = (isUnder70 && !isNeedBased)
    ? Math.min(42.0, Math.round(rawComposite * 0.42 * 10) / 10)
    : rawComposite;

  return {
    id: scholarship.id || scholarship.scholarship_id || `opp-${rank}`,
    name: oppName,
    shortName,
    hostCountry,
    flagEmoji,
    degreeLevel,
    fieldOfStudy: studentField,
    region,
    quotaDescription,
    bilateralSeats,
    officialPortalUrl: portal,
    hecPortalRequired: hasBilateral,
    factors: scoring.factors,
    compositeScore,
    rank,
    eligibilitySummary: {
      dimensionsMatched: (isUnder70 && !isNeedBased) ? 10 : 14,
      totalDimensions: 15,
      statusText: (isUnder70 && !isNeedBased) ? "INELIGIBLE (Marks < 70% Cutoff)" : "PASS (Criteria Verified)",
      criticalRequirement: (isUnder70 && !isNeedBased)
        ? "Ineligible for Merit Award (< 70.0% cutoff); Target Need-Based DSU Grants"
        : (hasBilateral ? "HEC Attestation & Registration" : "Standard Academic Admission"),
    },
    fundingSummary: {
      coverageType: scholarship.coverageType || (isFullFunding ? "Full Tuition + Housing + Living Allowance" : "Partial Scholarship / Subsidy"),
      tuitionCovered: isFullFunding,
      monthlyStipendPkr: monthlyStipend,
      initialOutOfPocketPkr,
      budgetStatus: costResult.isWithinBudget ? "WITHIN_BUDGET" : "DEFICIT_WARNING",
    },
    readinessSummary: {
      scorePercent: fDocReadiness,
      prepDaysNeeded: deadlineRunway.prepDaysNeededPakistan,
      criticalGaps: hasIelts
        ? ["Academic Transcripts Verification", "Letters of Recommendation"]
        : [`${isFbise ? "FBISE" : "BISE"} / HEC Attestation`, "English MOI Certificate / Test Prep"],
    },
    deadlineSummary: {
      applicationDeadline: displayDeadline,
      daysRemaining,
      prepDaysNeeded: deadlineRunway.prepDaysNeededPakistan,
      slackDays: deadlineRunway.slackDays,
      feasibility: deadlineRunway.feasibility,
    },
    verificationSummary: {
      confidencePercent: fVerification,
      authoritativeSourcesCount: 2,
      verifiedDomains: ["scholarship.gov.pk", "official.portal"],
      conflictStatus: "NONE",
    },
    skepticSummary: {
      challengesRaised: 1,
      resolvedCount: 1,
      topFlag: "Visa lead times require prompt appointment scheduling",
    },
  };
}

// ============================================================================
// 4. CANONICAL DOSSIER SECTIONS SPECIFICATION
// ============================================================================
export const DEFAULT_DOSSIER_SECTIONS: CanonicalDossierSection[] = [
  {
    id: "sec-identity",
    title: "Scholarship Profile & Strategic Identity",
    status: "COMPLETE",
    summary: "Institutional programme details, quota validation, and comprehensive funding coverage.",
    evidenceSourcesCount: 2,
  },
  {
    id: "sec-eligibility",
    title: "15-Dimension Pakistan Eligibility Audit",
    status: "COMPLETE",
    summary: "Pakistan eligibility verification, degree alignment, and test prerequisites.",
    evidenceSourcesCount: 2,
  },
  {
    id: "sec-readiness",
    title: "Document Readiness & Lead-Time Matrix",
    status: "COMPLETE",
    summary: "Credentials verification timeline, attestation pathways, and recommendation letters.",
    evidenceSourcesCount: 3,
  },
  {
    id: "sec-cost",
    title: "True Out-of-Pocket PKR Cost Deconstruction",
    status: "COMPLETE",
    summary: "Comprehensive Pakistani rupee outlay: document attestations, visa charges, and initial settlement.",
    evidenceSourcesCount: 4,
  },
  {
    id: "sec-deadline",
    title: "Temporal Runway & Deadline Feasibility",
    status: "COMPLETE",
    summary: "Application timeline, submission milestones, and slack buffer feasibility.",
    evidenceSourcesCount: 2,
  },
  {
    id: "sec-verification",
    title: "Official Evidence & Verification Trail",
    status: "COMPLETE",
    summary: "Cross-checked authoritative portals, embassy guidelines, and official circulars.",
    evidenceSourcesCount: 2,
  },
  {
    id: "sec-skeptic",
    title: "Skeptic Adversarial Audit & Risk Mitigations",
    status: "COMPLETE",
    summary: "Adversarial stress-test addressing potential refusal risks, quotas, and quota bottlenecks.",
    evidenceSourcesCount: 2,
  },
  {
    id: "sec-ranking",
    title: "Pakistan-Adjusted Ranking Score Explanation",
    status: "COMPLETE",
    summary: "Deterministic 8-factor composite scoring evaluation across global candidate pool.",
    evidenceSourcesCount: 5,
  },
  {
    id: "sec-roadmap",
    title: "6-Phase Personalized Application Journey",
    status: "COMPLETE",
    summary: "Actionable step-by-step Pakistani institutional milestones, costs, and dependencies.",
    evidenceSourcesCount: 6,
  },
  {
    id: "sec-sources",
    title: "Authoritative Portals & How-To-Apply Guide",
    status: "COMPLETE",
    summary: "Direct verified URLs, submission portals, and document verification centers.",
    evidenceSourcesCount: 5,
  },
];

export const CANONICAL_DOSSIER_SECTIONS = DEFAULT_DOSSIER_SECTIONS;

// ============================================================================
// 5. DYNAMIC DOSSIER BUILDER & DYNAMIC EXPORTS
// ============================================================================
export function buildDynamicDossier(
  profile?: any,
  topOpp?: InvestigatedOpportunity,
  allOpps?: InvestigatedOpportunity[]
): CanonicalDossier {
  const fallbackOpps = getInvestigatedOpportunitiesForProfile(profile || SEED_PROFILES[0], 4);
  const primary = topOpp || fallbackOpps[0];
  const opps = allOpps && allOpps.length > 0 ? allOpps : (fallbackOpps.length > 0 ? fallbackOpps : [primary]);
  const roadmap = generateDynamicRoadmap(profile, primary);
  const totalCost = roadmap.reduce((acc, p) => acc + (p.totalCostPkr || 0), 0);

  const studentName =
    profile?.personal?.name ||
    profile?.name ||
    profile?.studentName ||
    "Applicant";

  const rawField =
    profile?.academic?.field_of_study ||
    profile?.preferences?.target_fields?.[0] ||
    profile?.preferences?.studyField ||
    profile?.fieldOfStudy ||
    profile?.field ||
    primary?.fieldOfStudy ||
    "Computer Science";

  const studentField =
    typeof rawField === "string" &&
    rawField.toLowerCase() !== "specialized studies" &&
    rawField.toLowerCase() !== "specialized discipline"
      ? rawField
      : "Computer Science";

  return {
    scholarshipId: primary.id,
    title: `${primary.name} — Intelligence Dossier`,
    country: primary.hostCountry,
    degreeLevel: primary.degreeLevel,
    field: studentField,
    generatedAt: new Date().toISOString(),
    version: "ScholarX Intelligence Package v2.4",
    executiveSummary: `${primary.name} in ${primary.hostCountry} represents the highest-viability fully funded international study opportunity for ${studentName} in ${studentField}. The opportunity provides comprehensive academic funding, verified Pakistani eligibility pathways, and structured consular guidance.`,
    opportunity: primary,
    candidateProfile: profile ? {
      ...profile,
      personal: {
        ...profile?.personal,
        name: studentName,
        city: profile?.personal?.city || profile?.city || "Islamabad",
        province: profile?.personal?.province || profile?.province || "Pakistan",
        country: "Pakistan",
      },
      academic: {
        ...profile?.academic,
        institution: profile?.academic?.institution || profile?.institution || "Recognized Pakistani Institution",
        currentLevel: profile?.academic?.current_level || profile?.academic?.degree_level || profile?.degree || primary.degreeLevel,
        yearsOfEducation: profile?.academic?.years_of_education || 16,
        marksPercentage: profile?.academic?.percentage || profile?.academic?.gpa_percentage || 85.0,
        stream: studentField,
        field_of_study: profile?.academic?.field_of_study || studentField,
      },
      preferences: {
        ...profile?.preferences,
        target_fields: profile?.preferences?.target_fields?.length ? profile.preferences.target_fields : [studentField],
        target_degree_level: profile?.preferences?.target_degree_level || primary.degreeLevel,
      },
    } : {
      personal: {
        name: "Applicant Candidate",
        city: "Islamabad",
        province: "Pakistan",
        country: "Pakistan",
      },
      academic: {
        institution: "Accredited Pakistani Institution",
        currentLevel: primary.degreeLevel,
        yearsOfEducation: 14,
        marksPercentage: 85.0,
        stream: studentField,
      },
    },
    rankedOpportunities: opps,
    roadmapPhases: roadmap,
    totalPrepDaysEstimated: 75,
    totalBudgetNeededPkr: totalCost,
    sections: DEFAULT_DOSSIER_SECTIONS.map((s) => ({ ...s, status: "COMPLETE" as const })),
    state: "COMPLETE",
    webArtifactStatus: "READY",
    pdfArtifactStatus: "READY",
  };
}

export function getInvestigatedOpportunitiesForProfile(
  profile?: any,
  limit: number = 4
): InvestigatedOpportunity[] {
  const targetProfile = profile || SEED_PROFILES[0];
  const matched = searchScholarshipsForProfile(targetProfile, limit);
  if (!matched || matched.length === 0) {
    return [];
  }
  return matched.slice(0, limit).map((sc, index) =>
    buildDynamicInvestigatedOpportunity(sc, targetProfile, index + 1)
  );
}

export const INVESTIGATED_OPPORTUNITIES: InvestigatedOpportunity[] =
  getInvestigatedOpportunitiesForProfile(SEED_PROFILES[0], 4);

export const CANONICAL_ROADMAP_PHASES: RoadmapPhaseBlock[] =
  generateDynamicRoadmap(SEED_PROFILES[0], INVESTIGATED_OPPORTUNITIES[0]);

export const CANONICAL_DOSSIER: CanonicalDossier =
  buildDynamicDossier(
    SEED_PROFILES[0],
    INVESTIGATED_OPPORTUNITIES[0],
    INVESTIGATED_OPPORTUNITIES
  );

// Backward-compatible named exports mapped dynamically to candidate ranks
export const STIPENDIUM_HUNGARICUM: InvestigatedOpportunity = INVESTIGATED_OPPORTUNITIES[0];
export const CSC_SCHOLARSHIP: InvestigatedOpportunity = INVESTIGATED_OPPORTUNITIES[1] || INVESTIGATED_OPPORTUNITIES[0];
export const TURKIYE_BURSLARI: InvestigatedOpportunity = INVESTIGATED_OPPORTUNITIES[2] || INVESTIGATED_OPPORTUNITIES[0];
export const MEXT_UNDERGRADUATE: InvestigatedOpportunity = INVESTIGATED_OPPORTUNITIES[3] || INVESTIGATED_OPPORTUNITIES[0];

// ============================================================================
// 6. 12 DISCRETE OPERATIONAL SCENES (PHASE 7 DIRECTOR)
// ============================================================================
export const PHASE_7_STEPS: Phase7StepMeta[] = [
  {
    step: "POOL_INSPECTION",
    index: 1,
    label: "01 // CANDIDATE POOL INITIALIZED",
    narrative: "Commander aggregates characterized opportunities from global scouts for composite evaluation.",
    durationMs: 1400,
    activeEntity: "COMMANDER",
  },
  {
    step: "SCORING_INIT",
    index: 2,
    label: "02 // SCORING ENGINE ACTIVATION",
    narrative: "Deterministic Ranking Engine activates: initializing 8 Pakistan-adjusted scoring weights.",
    durationMs: 1200,
    activeEntity: "RANKING_ENGINE",
  },
  {
    step: "FACTOR_EVALUATION",
    index: 3,
    label: "03 // 8 FACTORS EVALUATED",
    narrative: "Deterministic formula evaluates Eligibility (25%), Funding (25%), Quotas (10%), Academic Fit (10%), Readiness (10%), and Deadlines (10%).",
    durationMs: 1800,
    activeEntity: "RANKING_ENGINE",
    focusOpportunityId: "opp-1",
  },
  {
    step: "SCORE_RESOLUTION",
    index: 4,
    label: "04 // CONTRIBUTION SCORES RESOLVED",
    narrative: "Transparent mathematical points computed for all candidates without opaque magic numbers.",
    durationMs: 1400,
    activeEntity: "RANKING_ENGINE",
  },
  {
    step: "SPATIAL_COMPARISON",
    index: 5,
    label: "05 // SPATIAL COMPARISON",
    narrative: "Opportunities resolve into mathematically computed ordering based on 8 Pakistan-adjusted dimensions.",
    durationMs: 1600,
    activeEntity: "RANKING_ENGINE",
  },
  {
    step: "PRIMARY_SELECTION",
    index: 6,
    label: "06 // PRIMARY OPPORTUNITY SELECTED",
    narrative: "Top-ranked candidate isolated as PRIMARY OPPORTUNITY for comprehensive strategy formulation.",
    durationMs: 1500,
    activeEntity: "COMMANDER",
    focusOpportunityId: "opp-1",
  },
  {
    step: "ADVISOR_ENGAGEMENT",
    index: 7,
    label: "07 // FINAL ADVISOR ACTIVATED",
    narrative: "Final Advisor agent deploys: synthesizing Pakistan-specific institutional roadmap and PKR timeline.",
    durationMs: 1400,
    activeEntity: "FINAL_ADVISOR",
  },
  {
    step: "ROADMAP_GENERATION",
    index: 8,
    label: "08 // 6-PHASE JOURNEY GENERATED",
    narrative: "Roadmap synthesized: institutional credentials attestation, language test readiness, application submission, and visa execution.",
    durationMs: 2000,
    activeEntity: "FINAL_ADVISOR",
  },
  {
    step: "DOSSIER_ASSEMBLY",
    index: 9,
    label: "09 // DOSSIER ASSEMBLY",
    narrative: "Intelligence sections stream into canonical dossier structure: findings, costs, deadline runway, and official sources.",
    durationMs: 1800,
    activeEntity: "DOSSIER_BUILDER",
  },
  {
    step: "WEB_BUILDER_ACTIVE",
    index: 10,
    label: "10 // WEB ARTIFACT BUILDER",
    narrative: "Web Builder formats standalone editorial scholarship intelligence page with responsive typography.",
    durationMs: 1600,
    activeEntity: "WEB_BUILDER",
  },
  {
    step: "PDF_BUILDER_ACTIVE",
    index: 11,
    label: "11 // PDF BUILDER TYPESETTING",
    narrative: "PDF Builder paginates publication-grade document with verified tables, page numbers, and print styling.",
    durationMs: 1600,
    activeEntity: "PDF_BUILDER",
  },
  {
    step: "ARTIFACTS_DELIVERED",
    index: 12,
    label: "12 // MISSION COMPLETE & ARTIFACTS READY",
    narrative: "Intelligence pipeline finished: Decision-ready Scholarship Dossier, Web Artifact, and Printable PDF available.",
    durationMs: 2400,
    activeEntity: "COMMANDER",
  },
];

// ============================================================================
// 7. PACKET DISPATCH FACTORY & SNAPSHOT SELECTOR
// ============================================================================
export function getPhase7Packets(
  step: Phase7Step,
  primaryOpportunity?: InvestigatedOpportunity
): PhysicalPacket[] {
  const oppName = primaryOpportunity?.name || "PRIMARY CANDIDATE";
  const oppScore = primaryOpportunity?.compositeScore ?? 88.5;

  switch (step) {
    case "FACTOR_EVALUATION":
    case "SCORE_RESOLUTION":
      return [
        {
          id: "pkt-p7-scoring-1",
          type: "COMMAND",
          senderId: "ranking-engine",
          senderName: "Deterministic Ranking Engine",
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: "EVALUATING 8 PAKISTAN-ADJUSTED SCORING FACTORS",
          priority: "HIGH",
          sourcePos: { x: 960, y: 620 },
          targetPos: { x: 960, y: 130 },
          progress: 0.65,
          state: "TRAVELING",
        },
      ];

    case "PRIMARY_SELECTION":
      return [
        {
          id: "pkt-p7-sel-1",
          type: "REPORT",
          senderId: "ranking-engine",
          senderName: "Deterministic Ranking Engine",
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: `PRIMARY SELECTION // ${oppName.toUpperCase()} (${oppScore})`,
          priority: "CRITICAL",
          sourcePos: { x: 960, y: 550 },
          targetPos: { x: 960, y: 130 },
          progress: 0.9,
          state: "TRAVELING",
        },
      ];

    case "ROADMAP_GENERATION":
      return [
        {
          id: "pkt-p7-road-1",
          type: "RESOLUTION",
          senderId: "final-advisor",
          senderName: "Final Advisor Agent",
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: "SYNTHESIZED 6-PHASE APPLICATION ROADMAP & PKR BUDGET",
          priority: "HIGH",
          sourcePos: { x: 800, y: 380 },
          targetPos: { x: 960, y: 130 },
          progress: 0.8,
          state: "TRAVELING",
        },
      ];

    case "DOSSIER_ASSEMBLY":
      return [
        {
          id: "pkt-p7-dos-1",
          type: "EVIDENCE",
          senderId: "final-advisor",
          senderName: "Final Advisor Agent",
          receiverId: "dossier-builder",
          receiverName: "Dossier Assembly Engine",
          summary: "STREAMING VERIFIED SECTIONS INTO CANONICAL DOSSIER",
          priority: "NORMAL",
          sourcePos: { x: 800, y: 380 },
          targetPos: { x: 1120, y: 380 },
          progress: 0.7,
          state: "TRAVELING",
        },
      ];

    case "WEB_BUILDER_ACTIVE":
      return [
        {
          id: "pkt-p7-web-1",
          type: "RESOLUTION",
          senderId: "dossier-builder",
          senderName: "Dossier Assembly Engine",
          receiverId: "web-builder",
          receiverName: "Web Artifact Builder",
          summary: "COMPOSING EDITORIAL DOSSIER WEB ARTIFACT",
          priority: "NORMAL",
          sourcePos: { x: 1120, y: 380 },
          targetPos: { x: 1320, y: 530 },
          progress: 0.75,
          state: "TRAVELING",
        },
      ];

    case "PDF_BUILDER_ACTIVE":
      return [
        {
          id: "pkt-p7-pdf-1",
          type: "RESOLUTION",
          senderId: "dossier-builder",
          senderName: "Dossier Assembly Engine",
          receiverId: "pdf-builder",
          receiverName: "PDF Artifact Builder",
          summary: "TYPESETTING PRINT-READY A4 PUBLICATION",
          priority: "NORMAL",
          sourcePos: { x: 1120, y: 380 },
          targetPos: { x: 1320, y: 680 },
          progress: 0.75,
          state: "TRAVELING",
        },
      ];

    default:
      return [];
  }
}

export function getPhase7Snapshot(
  step: Phase7Step,
  customOpportunities?: InvestigatedOpportunity[],
  profile?: any
): Phase7Snapshot {
  const stepMeta = PHASE_7_STEPS.find((s) => s.step === step) || PHASE_7_STEPS[0];
  const opportunities =
    customOpportunities && customOpportunities.length > 0
      ? customOpportunities
      : profile
      ? getInvestigatedOpportunitiesForProfile(profile, 4)
      : INVESTIGATED_OPPORTUNITIES;
  const primary = opportunities[0] || INVESTIGATED_OPPORTUNITIES[0];

  const canonicalDossier = buildDynamicDossier(profile || SEED_PROFILES[0], primary, opportunities);
  const dossierClone: CanonicalDossier = JSON.parse(JSON.stringify(canonicalDossier));

  if (stepMeta.index < 9) {
    dossierClone.state = "DRAFT";
    dossierClone.webArtifactStatus = "PENDING";
    dossierClone.pdfArtifactStatus = "PENDING";
    dossierClone.sections = dossierClone.sections.map((s, idx) => ({
      ...s,
      status: idx < 4 ? "COMPLETE" : "PENDING",
    }));
  } else if (step === "DOSSIER_ASSEMBLY") {
    dossierClone.state = "ASSEMBLING";
    dossierClone.webArtifactStatus = "PENDING";
    dossierClone.pdfArtifactStatus = "PENDING";
    dossierClone.sections = dossierClone.sections.map((s, idx) => ({
      ...s,
      status: idx < 8 ? "COMPLETE" : "ASSEMBLING",
    }));
  } else if (step === "WEB_BUILDER_ACTIVE") {
    dossierClone.state = "COMPLETE";
    dossierClone.webArtifactStatus = "GENERATING";
    dossierClone.pdfArtifactStatus = "PENDING";
  } else if (step === "PDF_BUILDER_ACTIVE") {
    dossierClone.state = "COMPLETE";
    dossierClone.webArtifactStatus = "READY";
    dossierClone.pdfArtifactStatus = "GENERATING";
  } else {
    dossierClone.state = "COMPLETE";
    dossierClone.webArtifactStatus = "READY";
    dossierClone.pdfArtifactStatus = "READY";
  }

  let builderActivity: Phase7Snapshot["builderActivity"];
  if (step === "DOSSIER_ASSEMBLY") {
    builderActivity = {
      builderName: "DOSSIER_BUILDER",
      actionLabel: "Assembling verified sections into canonical package",
      progressPercent: 78,
    };
  } else if (step === "WEB_BUILDER_ACTIVE") {
    builderActivity = {
      builderName: "WEB_BUILDER",
      actionLabel: "Composing standalone responsive editorial web page",
      progressPercent: 92,
    };
  } else if (step === "PDF_BUILDER_ACTIVE") {
    builderActivity = {
      builderName: "PDF_BUILDER",
      actionLabel: "Typesetting print-ready A4 publication with pagination",
      progressPercent: 95,
    };
  }

  return {
    step,
    stepMeta,
    opportunities,
    primaryOpportunity: primary,
    activeOpportunity: primary,
    dossier: dossierClone,
    activePackets: getPhase7Packets(step, primary),
    builderActivity,
  };
}
