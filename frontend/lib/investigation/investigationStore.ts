// Phase 6: Deep Opportunity Investigation Store & Fixtures (§8-§35, Agents.md)
import {
  Phase6Step,
  Phase6StepMeta,
  Phase6Snapshot,
  InvestigationTarget,
  EligibilityResult,
  DocumentAnalysisResult,
  TrueCostResult,
  DeadlineRunway,
  VerificationResult,
  SkepticResult,
  InvestigationSummary,
  SpecialistType,
  SpecialistCategory,
  SpecialistState,
  ResolvedTrace,
} from "./types";
import { PhysicalPacket } from "../communication/types";

// Stage Coordinates & Spatial Anchors for Investigation Theatre (1920x1080 stage)
export const INVESTIGATION_ANCHORS = {
  // Top: Central Commander Console
  commander: { x: 960, y: 110 },
  // Center: The Investigation Target (Selected Scholarship Object)
  target: { x: 960, y: 350 },
  // Primary Active Specialist Stage
  specialistStage: { x: 960, y: 645 },
  // Specialist Orbit Anchors (for packet routing & visual delegation)
  specialists: {
    ELIGIBILITY: { x: 420, y: 560 },
    DOCUMENT: { x: 420, y: 720 },
    COST: { x: 1500, y: 560 },
    DEADLINE: { x: 1500, y: 720 },
    VERIFICATION: { x: 700, y: 780 },
    SKEPTIC: { x: 1220, y: 780 },
    SYNTHESIS: { x: 960, y: 645 },
  } as Record<SpecialistType, { x: number; y: number }>,
};

// 14 Discrete Operational Scenes
export const PHASE_6_STEPS: Phase6StepMeta[] = [
  {
    step: "TARGET_SELECTION",
    index: 1,
    label: "01 // CANDIDATE ISOLATED",
    narrative: "Commander isolates Stipendium Hungaricum from Phase 5 European sector for deep empirical investigation.",
    durationMs: 1400,
    activeSpecialist: null,
    cameraShot: "OPPORTUNITY_SELECTED",
  },
  {
    step: "INVESTIGATION_INIT",
    index: 2,
    label: "02 // DISPATCH SPECIALISTS",
    narrative: "Commander dispatches multi-process investigation directive to evaluate student fit, true PKR cost, and official evidence.",
    durationMs: 1200,
    activeSpecialist: null,
    cameraShot: "OPPORTUNITY_SELECTED",
  },
  {
    step: "ELIGIBILITY_ACTIVE",
    index: 3,
    label: "03 // ELIGIBILITY WORKFLOW",
    narrative: "Deterministic engine sequentially evaluates 15 Pakistan-aware dimensions against candidate criteria.",
    durationMs: 1600,
    activeSpecialist: "ELIGIBILITY",
    cameraShot: "ELIGIBILITY_FOCUS",
  },
  {
    step: "ELIGIBILITY_DOCKED",
    index: 4,
    label: "04 // ELIGIBILITY MATCHED",
    narrative: "Eligibility result docks: 13/15 matched with 400 bilateral seats. HEC USAT registration flagged as mandatory.",
    durationMs: 1100,
    activeSpecialist: "ELIGIBILITY",
    cameraShot: "ELIGIBILITY_FOCUS",
  },
  {
    step: "DOCUMENT_ACTIVE",
    index: 5,
    label: "05 // DOCUMENT ANALYST AGENT",
    narrative: "LLM agent assesses uploaded documents against Hungarian Tempus and HEC Pakistani bilateral requirements.",
    durationMs: 1600,
    activeSpecialist: "DOCUMENT",
    cameraShot: "DOCUMENT_FOCUS",
  },
  {
    step: "DOCUMENT_DOCKED",
    index: 6,
    label: "06 // READINESS GAP ANALYSIS",
    narrative: "Document readiness: PARTIAL (62%). Critical path identifies 28 days needed for HEC attestation and references.",
    durationMs: 1100,
    activeSpecialist: "DOCUMENT",
    cameraShot: "DOCUMENT_FOCUS",
  },
  {
    step: "COST_ACTIVE",
    index: 7,
    label: "07 // TRUE COST DECONSTRUCTION",
    narrative: "Dismantling 'free' funding: calculating mandatory pre-application, consular, medical, flight, and initial settlement out-of-pocket in PKR.",
    durationMs: 1600,
    activeSpecialist: "COST",
    cameraShot: "COST_FOCUS",
  },
  {
    step: "COST_DOCKED",
    index: 8,
    label: "08 // PKR OUT-OF-POCKET RESULT",
    narrative: "True cost result: PKR 303,500 initial outlay needed. Stated savings of PKR 150,000 creates PKR 153,500 deficit risk.",
    durationMs: 1100,
    activeSpecialist: "COST",
    cameraShot: "COST_FOCUS",
  },
  {
    step: "DEADLINE_ACTIVE",
    index: 9,
    label: "09 // DEADLINE INTELLIGENCE",
    narrative: "Date math engine projects administrative runway: deadline vs Pakistani regional processing lead times.",
    durationMs: 1500,
    activeSpecialist: "DEADLINE",
    cameraShot: "DEADLINE_FOCUS",
  },
  {
    step: "DEADLINE_DOCKED",
    index: 10,
    label: "10 // TEMPORAL SLACK FEASIBLE",
    narrative: "Deadline feasibility: FEASIBLE. 72 days remaining with 37 days of slack buffer after 28 days of HEC/IBCC preparation.",
    durationMs: 1100,
    activeSpecialist: "DEADLINE",
    cameraShot: "DEADLINE_FOCUS",
  },
  {
    step: "VERIFICATION_ACTIVE",
    index: 11,
    label: "11 // MULTI-SOURCE EVIDENCE VERIFICATION",
    narrative: "Verification Agent cross-checks claims against Tempus portal and HEC bilateral agreement, resolving English waiver conflict.",
    durationMs: 1700,
    activeSpecialist: "VERIFICATION",
    cameraShot: "VERIFICATION_FOCUS",
  },
  {
    step: "SKEPTIC_ACTIVE",
    index: 12,
    label: "12 // SKEPTIC ADVERSARIAL CHALLENGE",
    narrative: "Skeptic raises adversarial challenges: uncovered flight expenses exceeding budget & dual-gate HEC rejection risks.",
    durationMs: 1600,
    activeSpecialist: "SKEPTIC",
    cameraShot: "SKEPTIC_FOCUS",
  },
  {
    step: "CHALLENGE_RESOLVED",
    index: 13,
    label: "13 // EVIDENCE RESOLUTION",
    narrative: "Official evidence qualifies challenges: dual application dependency flagged; funding risk marked for student budget guidance.",
    durationMs: 1400,
    activeSpecialist: "SKEPTIC",
    cameraShot: "SKEPTIC_FOCUS",
  },
  {
    step: "SYNTHESIS_COMPLETE",
    index: 14,
    label: "14 // UNIFIED INVESTIGATION SUMMARY",
    narrative: "Synthesis converges all 6 findings into unified intelligence: candidate is deeply verified, highly viable, with clear action prerequisites.",
    durationMs: 2000,
    activeSpecialist: "SYNTHESIS",
    cameraShot: "SYNTHESIS_FOCUS",
  },
];

// 1. Authentic Pakistani Eligibility Dimensions Fixture (§10, §11, Agents.md §4)
export const ELIGIBILITY_FIXTURE: EligibilityResult = {
  overallScore: 87,
  status: "CONDITIONAL",
  matchedCount: 13,
  totalEvaluated: 15,
  bilateralSeats: 400,
  actionRequired: "Mandatory HEC USAT registration required before Pakistani nomination cutoff",
  criteria: [
    {
      id: "crit-1",
      dimensionNumber: 1,
      dimensionName: "Nationality Eligibility",
      status: "PASS",
      studentValue: "Pakistan (Citizen / Resident)",
      requirementValue: "Bilateral Partner Countries (Pakistan Included)",
      detail: "Pakistan is an official bilateral partner state with dedicated quotas",
      isPakistanSpecific: true,
    },
    {
      id: "crit-2",
      dimensionNumber: 2,
      dimensionName: "Bilateral Quota Allocation",
      status: "BONUS",
      studentValue: "Pakistani Applicant",
      requirementValue: "400 Seats via Government Agreement",
      detail: "Dedicated 400+ annual seats allocated exclusively for Pakistani students",
      isPakistanSpecific: true,
    },
    {
      id: "crit-3",
      dimensionNumber: 3,
      dimensionName: "Degree Level Compatibility",
      status: "PASS",
      studentValue: "Bachelor's / Master's CS",
      requirementValue: "BSc / MSc / PhD Offered",
      detail: "Computer Science curriculum offered at BME, ELTE, and Debrecen",
      isPakistanSpecific: false,
    },
    {
      id: "crit-4",
      dimensionNumber: 4,
      dimensionName: "Field of Study Alignment",
      status: "PASS",
      studentValue: "Computer Science / AI",
      requirementValue: "STEM & Computer Science Eligible",
      detail: "Computer Science is a prioritized STEM discipline under bilateral pact",
      isPakistanSpecific: false,
    },
    {
      id: "crit-5",
      dimensionNumber: 5,
      dimensionName: "Academic Marks Threshold",
      status: "PASS",
      studentValue: "87.0% (GPA 3.7 / 4.0)",
      requirementValue: "Minimum 70% for HEC Nomination",
      detail: "Student's 87% places them well above competitive historical cutoff (~78%)",
      isPakistanSpecific: true,
    },
    {
      id: "crit-6",
      dimensionNumber: 6,
      dimensionName: "Age Limit Compliance",
      status: "PASS",
      studentValue: "19 Years Old",
      requirementValue: "Under 35 Years at Cutoff",
      detail: "Fully within permissible age bracket for undergraduate/graduate entry",
      isPakistanSpecific: false,
    },
    {
      id: "crit-7",
      dimensionNumber: 7,
      dimensionName: "English Language Proficiency",
      status: "PASS",
      studentValue: "IELTS Academic 7.0 Overall",
      requirementValue: "Minimum IELTS 5.5 / B2 CEFR",
      detail: "Exceeds Hungarian university requirement (5.5) and HEC nomination standard",
      isPakistanSpecific: false,
    },
    {
      id: "crit-8",
      dimensionNumber: 8,
      dimensionName: "HEC USAT / Standardized Test",
      status: "CONDITIONAL",
      studentValue: "Not Yet Registered",
      requirementValue: "HEC USAT Mandated for Undergrad",
      detail: "HEC requires USAT registration for shortlisting; next exam slot is in 3 weeks",
      isPakistanSpecific: true,
    },
    {
      id: "crit-9",
      dimensionNumber: 9,
      dimensionName: "Prior Education Validation",
      status: "PASS",
      studentValue: "12 Years (Intermediate / ICS)",
      requirementValue: "12 Years Completed",
      detail: "12 years of formal education complete; requires IBCC equivalence certificate",
      isPakistanSpecific: true,
    },
    {
      id: "crit-10",
      dimensionNumber: 10,
      dimensionName: "HEC Degree Attestation",
      status: "CONDITIONAL",
      studentValue: "Pending Submission",
      requirementValue: "HEC e-Attestation Mandatory",
      detail: "Certificates must undergo online DAS 1-Link attestation before final interview",
      isPakistanSpecific: true,
    },
    {
      id: "crit-11",
      dimensionNumber: 11,
      dimensionName: "Funding Level Match",
      status: "PASS",
      studentValue: "Seeking 100% Tuition Waiver",
      requirementValue: "Full Tuition + Housing + Stipend",
      detail: "Program covers 100% university tuition fees directly",
      isPakistanSpecific: false,
    },
    {
      id: "crit-12",
      dimensionNumber: 12,
      dimensionName: "Living Subsidy Coverage",
      status: "PASS",
      studentValue: "Requires Accommodation",
      requirementValue: "Free Dormitory or HUF 40,000",
      detail: "Free university dormitory bed provided or HUF 40,000 monthly allowance",
      isPakistanSpecific: false,
    },
    {
      id: "crit-13",
      dimensionNumber: 13,
      dimensionName: "Health Insurance",
      status: "PASS",
      studentValue: "Full Medical Required",
      requirementValue: "HUF 65,000 Annual Policy",
      detail: "Full Hungarian national health insurance provided for duration of study",
      isPakistanSpecific: false,
    },
    {
      id: "crit-14",
      dimensionNumber: 14,
      dimensionName: "Proof of Funds Obligation",
      status: "PASS",
      studentValue: "Cannot Show > PKR 1.5M",
      requirementValue: "Exempt for SH Recipients",
      detail: "Hungarian Embassy waives massive blocked account requirement for quota recipients",
      isPakistanSpecific: true,
    },
    {
      id: "crit-15",
      dimensionNumber: 15,
      dimensionName: "Return-to-Home Obligation",
      status: "PASS",
      studentValue: "Willing to Return to PK",
      requirementValue: "HEC Deed of Undertaking",
      detail: "HEC requires bond to return to Pakistan upon graduation; aligns with student goals",
      isPakistanSpecific: true,
    },
  ],
};

// 2. Authentic Document Readiness Fixture (§12, §13, Agents.md §5)
export const DOCUMENT_FIXTURE: DocumentAnalysisResult = {
  readinessScore: 62,
  overallStatus: "PARTIAL",
  readyCount: 4,
  totalRequired: 8,
  criticalMissing: ["HEC Attestation", "Academic Recommendation Letters (2)"],
  totalPrepDays: 28,
  totalPrepCostPkr: 14500,
  documents: [
    {
      id: "doc-1",
      documentName: "Academic Transcript & Marksheet",
      status: "READY",
      quality: "VERIFIED",
      pakistanLeadDays: 0,
      estimatedCostPkr: 0,
      isBlocking: false,
      notes: "High-resolution scan of Lahore Board intermediate transcript uploaded",
    },
    {
      id: "doc-2",
      documentName: "IELTS Academic TRF (7.0)",
      status: "READY",
      quality: "VERIFIED",
      pakistanLeadDays: 0,
      estimatedCostPkr: 0,
      isBlocking: false,
      notes: "British Council electronic verification code authenticated",
    },
    {
      id: "doc-3",
      documentName: "Passport (Valid to 2032)",
      status: "READY",
      quality: "VERIFIED",
      pakistanLeadDays: 0,
      estimatedCostPkr: 0,
      isBlocking: false,
      notes: "Valid Pakistani machine-readable passport with >5 years validity",
    },
    {
      id: "doc-4",
      documentName: "CV / Academic Resume",
      status: "READY",
      quality: "GOOD",
      pakistanLeadDays: 0,
      estimatedCostPkr: 0,
      isBlocking: false,
      notes: "Europass format structured with programming and extracurricular achievements",
    },
    {
      id: "doc-5",
      documentName: "HEC Degree / Certificate Attestation",
      status: "REQUIRED",
      quality: "PENDING",
      pakistanLeadDays: 21,
      estimatedCostPkr: 6000,
      isBlocking: true,
      notes: "Must submit to HEC Lahore regional center; 21-28 business days lead time",
    },
    {
      id: "doc-6",
      documentName: "Two Academic Recommendation Letters",
      status: "MISSING",
      quality: "PENDING",
      pakistanLeadDays: 14,
      estimatedCostPkr: 0,
      isBlocking: true,
      notes: "Must obtain signed, official institutional letterhead letters from college lecturers",
    },
    {
      id: "doc-7",
      documentName: "Motivation Letter / Statement of Purpose",
      status: "PARTIAL",
      quality: "DRAFT",
      pakistanLeadDays: 4,
      estimatedCostPkr: 0,
      isBlocking: false,
      notes: "Draft 1 requires refinement to address specific Hungarian research faculty interests",
    },
    {
      id: "doc-8",
      documentName: "Medical Panel Certificate (HIV, Hep B/C, TB)",
      status: "REQUIRED",
      quality: "PENDING",
      pakistanLeadDays: 7,
      estimatedCostPkr: 8500,
      isBlocking: false,
      notes: "Required upon preliminary nomination from approved diagnostic lab",
    },
  ],
};

// 3. Authentic Pakistan True Cost Database Fixture (§14, §15, Agents.md §6)
export const COST_FIXTURE: TrueCostResult = {
  totalOutOfPocketPkr: 303500,
  totalOutOfPocketUsd: 1090,
  studentMaxBudgetPkr: 150000,
  budgetStatus: "EXCEEDS_BUDGET",
  shortfallPkr: 153500,
  breakdown: {
    baseFunding: [
      {
        id: "cost-base-1",
        phase: "BASE_FUNDING",
        category: "Tuition",
        item: "BSc/MSc University Tuition (3 Years)",
        amountPkr: 0,
        amountDisplay: "100% WAIVED",
        coverage: "COVERED",
        notes: "EUR 7,000/yr value paid directly by Hungarian Government",
      },
      {
        id: "cost-base-2",
        phase: "BASE_FUNDING",
        category: "Housing",
        item: "University Dormitory Bed",
        amountPkr: 0,
        amountDisplay: "FREE / HUF 40,000",
        coverage: "COVERED",
        notes: "Free on-campus room or monthly housing allowance",
      },
      {
        id: "cost-base-3",
        phase: "BASE_FUNDING",
        category: "Stipend",
        item: "Monthly Living Allowance",
        amountPkr: 0,
        amountDisplay: "HUF 43,700 / mo",
        coverage: "COVERED",
        notes: "Disbursed to Hungarian bank account post-registration (~PKR 35,000/mo)",
      },
      {
        id: "cost-base-4",
        phase: "BASE_FUNDING",
        category: "Insurance",
        item: "Hungarian National Health Insurance",
        amountPkr: 0,
        amountDisplay: "HUF 65,000 / yr",
        coverage: "COVERED",
        notes: "Full medical coverage in Hungarian public health system",
      },
    ],
    preApplication: [
      {
        id: "cost-pre-1",
        phase: "PRE_APPLICATION",
        category: "HEC Attestation",
        item: "HEC Online e-Attestation (DAS 1-Link)",
        amountPkr: 6000,
        amountDisplay: "PKR 6,000",
        coverage: "UNCOVERED",
        notes: "PKR 3,000 per document (Transcript + Certificate)",
      },
      {
        id: "cost-pre-2",
        phase: "PRE_APPLICATION",
        category: "Standardized Exam",
        item: "HEC USAT Registration Fee",
        amountPkr: 2500,
        amountDisplay: "PKR 2,500",
        coverage: "UNCOVERED",
        notes: "Mandatory screening exam fee for Pakistani nomination",
      },
    ],
    application: [
      {
        id: "cost-app-1",
        phase: "APPLICATION",
        category: "Application Fee",
        item: "DreamApply Hungary Submission",
        amountPkr: 0,
        amountDisplay: "PKR 0 (WAIVED)",
        coverage: "COVERED",
        notes: "No fee for official Stipendium Hungaricum quota applicants",
      },
      {
        id: "cost-app-2",
        phase: "APPLICATION",
        category: "Courier",
        item: "HEC Hardcopy Dossier Dispatch",
        amountPkr: 0,
        amountDisplay: "PKR 0",
        coverage: "COVERED",
        notes: "Digital upload via HEC e-portal; physical courier not required in Phase 1",
      },
    ],
    visaTravel: [
      {
        id: "cost-visa-1",
        phase: "VISA_TRAVEL",
        category: "Consular Visa",
        item: "Hungarian D-Type Student Visa",
        amountPkr: 0,
        amountDisplay: "PKR 0 (GRATIS)",
        coverage: "COVERED",
        notes: "Consular visa fee EUR 90 is waived for Stipendium scholars",
      },
      {
        id: "cost-visa-2",
        phase: "VISA_TRAVEL",
        category: "Medical Exam",
        item: "Approved Panel Diagnostic Screening",
        amountPkr: 25000,
        amountDisplay: "PKR 25,000",
        coverage: "UNCOVERED",
        notes: "Chest X-Ray, HIV, Hepatitis B/C, and physical verification in Lahore",
      },
      {
        id: "cost-visa-3",
        phase: "VISA_TRAVEL",
        category: "Flight Ticket",
        item: "One-Way Airfare (LHE/ISB to BUD)",
        amountPkr: 210000,
        amountDisplay: "PKR 210,000",
        coverage: "UNCOVERED",
        notes: "Commercial airfare is NOT covered by Hungarian government or HEC base quota",
      },
    ],
    settlement: [
      {
        id: "cost-settle-1",
        phase: "SETTLEMENT",
        category: "Initial Reserve",
        item: "First Month Living Expenses in Budapest",
        amountPkr: 60000,
        amountDisplay: "PKR 60,000",
        coverage: "REQUIRED_RESERVE",
        notes: "Cash required on arrival before Hungarian bank account & stipend activate (3-4 weeks)",
      },
    ],
  },
  keyRisks: [
    "Flight airfare (~PKR 210,000) is completely uncovered and payable upfront",
    "First-month reserve (~PKR 60,000) needed in cash before stipend disbursement",
    "Net initial outlay exceeds student stated budget of PKR 150,000 by PKR 153,500",
  ],
};

// 4. Authentic Pakistan Deadline Intelligence Runway Fixture (§16, §17, Agents.md §7)
export const DEADLINE_FIXTURE: DeadlineRunway = {
  applicationDeadline: "2027-01-15",
  deadlineDisplay: "15 JAN 2027",
  daysRemaining: 72,
  criticalPathDays: 28,
  bufferDays: 7,
  availableSlackDays: 37,
  feasibility: "FEASIBLE",
  leadTimeItems: [
    {
      process: "HEC Degree e-Attestation",
      durationDays: 21,
      pakistanOffice: "HEC Regional Center Lahore / Islamabad",
    },
    {
      process: "HEC USAT Test & Result",
      durationDays: 24,
      pakistanOffice: "HEC Education Testing Council (ETC)",
    },
    {
      process: "Recommendation Letters (2)",
      durationDays: 14,
      pakistanOffice: "Faculty Lecturers / College Dept",
    },
    {
      process: "Police Character Certificate",
      durationDays: 14,
      pakistanOffice: "Police Khidmat Markaz (PKM)",
    },
    {
      process: "Panel Medical Examination",
      durationDays: 7,
      pakistanOffice: "Approved Diagnostic Hospital Lahore",
    },
  ],
};

// 5. Authentic Multi-Source Verification Fixture (§20, §21, §22, Agents.md §8)
export const VERIFICATION_FIXTURE: VerificationResult = {
  status: "HEC_LISTED",
  confidenceScore: 98,
  verifiedClaimsCount: 3,
  sourcesCrossChecked: 3,
  claims: [
    {
      id: "claim-1",
      claim: "400 Bilateral Quota Seats Dedicated for Pakistani Applicants",
      verdict: "CONFIRMED",
      primarySource: {
        id: "src-gov-1",
        name: "Tempus Public Foundation (Hungary)",
        domain: "stipendiumhungaricum.hu",
        sourceType: "GOVERNMENT",
        trustLevel: "AUTHORITATIVE",
        url: "https://stipendiumhungaricum.hu/partners/pakistan",
      },
      secondarySource: {
        id: "src-hec-1",
        name: "Higher Education Commission (HEC Pakistan)",
        domain: "scholarship.hec.gov.pk",
        sourceType: "HEC_PORTAL",
        trustLevel: "AUTHORITATIVE",
        url: "https://www.hec.gov.pk/english/scholarships/bilateral/hungary",
      },
      evidenceQuote: "Under the Memorandum of Understanding between Hungary and Pakistan, up to 400 Pakistani students are nominated annually across Bachelor's, Master's, and PhD cycles.",
    },
    {
      id: "claim-2",
      claim: "100% Tuition Waiver & Free University Dormitory Housing",
      verdict: "CONFIRMED",
      primarySource: {
        id: "src-gov-1",
        name: "Tempus Public Foundation (Call for Applications §3.1)",
        domain: "stipendiumhungaricum.hu",
        sourceType: "GOVERNMENT",
        trustLevel: "AUTHORITATIVE",
        url: "https://stipendiumhungaricum.hu/call-for-applications-2026-2027",
      },
      evidenceQuote: "Exemption from tuition fees. Free dormitory place or monthly housing allowance of HUF 40,000 for the entire duration of the study program.",
    },
    {
      id: "claim-3",
      claim: "English Test Requirement vs Medium of Instruction (MOI) Exemption",
      verdict: "CONFLICT_RESOLVED",
      primarySource: {
        id: "src-uni-1",
        name: "Budapest University of Technology & Economics (BME)",
        domain: "bme.hu",
        sourceType: "UNIVERSITY",
        trustLevel: "CONFIRMED",
        url: "https://bme.hu/international/stipendium-admissions",
      },
      secondarySource: {
        id: "src-hec-1",
        name: "HEC Pakistan Bilateral Portal",
        domain: "scholarship.hec.gov.pk",
        sourceType: "HEC_PORTAL",
        trustLevel: "AUTHORITATIVE",
        url: "https://www.hec.gov.pk/english/scholarships/bilateral/hungary",
      },
      hasConflict: true,
      conflictDetails: {
        sourceA: "bme.hu: 'English MOI certificate accepted if previous degree was in English.'",
        claimA: "MOI Certificate accepted as English proof",
        sourceB: "hec.gov.pk: 'All Pakistani candidates MUST submit valid IELTS or HEC USAT score.'",
        claimB: "IELTS or HEC USAT strictly required for Pakistani nomination",
        resolution: "CONFLICT RESOLVED: HEC bilateral nomination gateway rules supersede Hungarian university waiver for Pakistani applicants.",
      },
      evidenceQuote: "While Hungarian universities accept MOI, HEC Pakistan mandates standardized test metrics (IELTS 5.5+ or USAT) to generate the official national merit list.",
    },
  ],
};

// 6. Authentic Skeptic Adversarial Challenge Fixture (§24, §25, §26, §28, Agents.md §9)
export const SKEPTIC_FIXTURE: SkepticResult = {
  totalChallengesRaised: 2,
  resolvedChallengesCount: 2,
  criticalRisksFlagged: 2,
  challenges: [
    {
      id: "skep-1",
      title: "CHALLENGE // Hidden Pre-Arrival Expenditure Deficit",
      challengeText: "The scholarship claims 'Fully Funded' status, but one-way international airfare (~PKR 210,000) and first-month settlement reserve (~PKR 60,000) are totally uncovered. With student's stated budget of PKR 150,000, there is a serious PKR 153,500 deficit.",
      category: "FINANCIAL_RISK",
      evidenceRequested: "Requesting cost verification from Hungarian Tempus guidelines & HEC travel subsidy policies.",
      evidenceResponse: "Tempus Call §4.2 confirms airfare is non-reimbursable. However, HEC offers a need-based travel grant for top 10% provincial merit holders.",
      status: "RESOLVED_QUALIFIED",
      impactSummary: "QUALIFIED RISK: Candidate is financially viable ONLY if student secures supplementary PKR 153,500 family bridge funding or qualifies for HEC need-based airfare support.",
    },
    {
      id: "skep-2",
      title: "CHALLENGE // Dual-Gate Rejection Bottleneck",
      challengeText: "Securing admission at Budapest University of Technology is meaningless if HEC Pakistan rejects the preliminary nomination. Many Pakistani students fail to register simultaneously on both portals.",
      category: "PROCEDURAL_BOTTLENECK",
      evidenceRequested: "Cross-checking procedural requirements between DreamApply and HEC portal.",
      evidenceResponse: "HEC procedural bulletin confirms dual registration is mandatory: Failure to submit on HEC e-portal before 15 Jan voids the DreamApply application completely.",
      status: "RESOLVED_QUALIFIED",
      impactSummary: "PROCEDURAL PREREQUISITE FLAGGED: Dual application workflow logged into timeline as a synchronized priority step.",
    },
  ],
};

// 7. Authentic Synthesis Unified Summary Fixture (§30, §31, §32, Agents.md §10)
export const SYNTHESIS_FIXTURE: InvestigationSummary = {
  scholarshipTitle: "Stipendium Hungaricum Scholarship 2025/2026",
  hostCountry: "Hungary (BME / ELTE / Debrecen)",
  quotaSeats: 400,
  overallEligibility: "MATCHED (13/15 Dimensions · HEC USAT Action Required)",
  documentReadiness: "PARTIAL (62% Ready · 28 Days Lead Time)",
  realInitialOutlayPkr: 303500,
  deadlineFeasibility: "FEASIBLE (72 Days Remaining · 37 Days Temporal Slack)",
  verificationBadge: "VERIFIED & HEC LISTED (Official Bilateral MoU Confirmed)",
  skepticStatus: "2 AUDIT CHALLENGES RESOLVED & QUALIFIED",
  criticalAdvisory: "High-probability match under dedicated 400-seat Pakistan bilateral quota. Mandatory immediate actions: Register for HEC USAT and submit transcript for HEC attestation.",
  investigationCompletedAt: "2026-10-03T10:00:00Z",
};

// Helper: Get Snapshot for Any Phase 6 Step
export function getPhase6Snapshot(step: Phase6Step): Phase6Snapshot {
  const meta = PHASE_6_STEPS.find((s) => s.step === step)!;

  // Derive resolved traces based on step progression
  const traces: ResolvedTrace[] = [];

  const hasEligibilityPassed =
    step !== "TARGET_SELECTION" &&
    step !== "INVESTIGATION_INIT" &&
    step !== "ELIGIBILITY_ACTIVE";

  const hasDocumentPassed =
    hasEligibilityPassed &&
    step !== "ELIGIBILITY_DOCKED" &&
    step !== "DOCUMENT_ACTIVE";

  const hasCostPassed =
    hasDocumentPassed &&
    step !== "DOCUMENT_DOCKED" &&
    step !== "COST_ACTIVE";

  const hasDeadlinePassed =
    hasCostPassed &&
    step !== "COST_DOCKED" &&
    step !== "DEADLINE_ACTIVE";

  const hasVerificationPassed =
    hasDeadlinePassed &&
    step !== "DEADLINE_DOCKED" &&
    step !== "VERIFICATION_ACTIVE";

  const hasSkepticPassed =
    hasVerificationPassed &&
    step !== "SKEPTIC_ACTIVE" &&
    step !== "CHALLENGE_RESOLVED";

  if (hasEligibilityPassed) {
    traces.push({
      id: "trace-elig",
      specialist: "ELIGIBILITY",
      label: "ELIGIBILITY",
      badge: "MATCHED",
      color: "#10B981",
      summary: "13/15 Matched · 400 Bilateral Seats · HEC USAT Required",
      timestamp: Date.now() - 45000,
    });
  }

  if (hasDocumentPassed) {
    traces.push({
      id: "trace-doc",
      specialist: "DOCUMENT",
      label: "DOCUMENTS",
      badge: "PARTIAL (62%)",
      color: "#F59E0B",
      summary: "4/8 Ready · 28 Days Lead Time for HEC Attestation",
      timestamp: Date.now() - 35000,
    });
  }

  if (hasCostPassed) {
    traces.push({
      id: "trace-cost",
      specialist: "COST",
      label: "TRUE COST",
      badge: "PKR 303,500",
      color: "#EF4444",
      summary: "Flight & reserve uncovered · Exceeds base savings by 153.5k",
      timestamp: Date.now() - 25000,
    });
  }

  if (hasDeadlinePassed) {
    traces.push({
      id: "trace-dl",
      specialist: "DEADLINE",
      label: "DEADLINE",
      badge: "FEASIBLE (37D SLACK)",
      color: "#38BDF8",
      summary: "72d to 15 Jan · 28d prep path · 37d comfortable buffer",
      timestamp: Date.now() - 18000,
    });
  }

  if (hasVerificationPassed) {
    traces.push({
      id: "trace-verif",
      specialist: "VERIFICATION",
      label: "VERIFICATION",
      badge: "HEC LISTED",
      color: "#10B981",
      summary: "Official MoU confirmed on stipendiumhungaricum.hu & hec.gov.pk",
      timestamp: Date.now() - 10000,
    });
  }

  if (hasSkepticPassed) {
    traces.push({
      id: "trace-skep",
      specialist: "SKEPTIC",
      label: "SKEPTIC AUDIT",
      badge: "2 QUALIFIED",
      color: "#D4AF37",
      summary: "Dual application bottleneck & travel subsidy risks factored in",
      timestamp: Date.now() - 4000,
    });
  }

  // Derive target knowledge state
  let knowledgeState: import("./types").TargetKnowledgeState = "UNINVESTIGATED";
  if (step === "ELIGIBILITY_DOCKED") knowledgeState = "PROFILE_MATCHED";
  else if (step === "DOCUMENT_DOCKED") knowledgeState = "READINESS_KNOWN";
  else if (step === "COST_DOCKED") knowledgeState = "COST_UNDERSTOOD";
  else if (step === "DEADLINE_DOCKED") knowledgeState = "TIMELINE_ASSESSED";
  else if (step === "VERIFICATION_ACTIVE") knowledgeState = "EVIDENCE_CONFIRMED";
  else if (step === "SKEPTIC_ACTIVE" || step === "CHALLENGE_RESOLVED") knowledgeState = "RISKS_CHALLENGED";
  else if (step === "SYNTHESIS_COMPLETE") knowledgeState = "INVESTIGATION_COMPLETE";
  else if (traces.length > 0) knowledgeState = "PROFILE_MATCHED";

  const target: InvestigationTarget = {
    id: "cand-eu-1",
    name: "Stipendium Hungaricum Scholarship 2025/2026",
    hostCountry: "Hungary",
    degreeLevel: "Bachelor's / Master's (BSc / MSc)",
    fieldOfStudy: "Computer Science & Engineering",
    applicantContext: "Pakistani Applicant (19 yrs, 87% marks, IELTS 7.0)",
    quotaSeats: 400,
    fundingLabel: "Fully Funded (Bilateral Quota)",
    knowledgeState,
    resolvedTraces: traces,
  };

  // Derive active specialist metadata
  let specialistMeta: Phase6Snapshot["specialistMeta"] = null;
  if (meta.activeSpecialist === "ELIGIBILITY") {
    specialistMeta = {
      type: "ELIGIBILITY",
      category: "WORKFLOW",
      displayName: "ELIGIBILITY INVESTIGATOR",
      state: step === "ELIGIBILITY_ACTIVE" ? "ANALYZING" : "RESOLVED",
      actionLabel: step === "ELIGIBILITY_ACTIVE" ? "EVALUATING 15 CRITERIA" : "MATCH REPORT GENERATED",
      color: "#10B981",
    };
  } else if (meta.activeSpecialist === "DOCUMENT") {
    specialistMeta = {
      type: "DOCUMENT",
      category: "AGENT",
      displayName: "DOCUMENT ANALYST",
      state: step === "DOCUMENT_ACTIVE" ? "ANALYZING" : "RESOLVED",
      actionLabel: step === "DOCUMENT_ACTIVE" ? "ASSESSING PROFILE TRANSCRIPTS & GAPS" : "READINESS REPORT DOCKED",
      color: "#F59E0B",
    };
  } else if (meta.activeSpecialist === "COST") {
    specialistMeta = {
      type: "COST",
      category: "WORKFLOW",
      displayName: "TRUE COST ANALYZER",
      state: step === "COST_ACTIVE" ? "ANALYZING" : "RESOLVED",
      actionLabel: step === "COST_ACTIVE" ? "DECONSTRUCTING PAKISTAN PKR OUTLAY" : "OUT-OF-POCKET CALCULATED",
      color: "#EF4444",
    };
  } else if (meta.activeSpecialist === "DEADLINE") {
    specialistMeta = {
      type: "DEADLINE",
      category: "WORKFLOW",
      displayName: "DEADLINE INTELLIGENCE",
      state: step === "DEADLINE_ACTIVE" ? "ANALYZING" : "RESOLVED",
      actionLabel: step === "DEADLINE_ACTIVE" ? "CALCULATING ADMINISTRATIVE RUNWAY & SLACK" : "FEASIBILITY DETERMINED",
      color: "#38BDF8",
    };
  } else if (meta.activeSpecialist === "VERIFICATION") {
    specialistMeta = {
      type: "VERIFICATION",
      category: "AGENT",
      displayName: "VERIFICATION AGENT",
      state: "CROSS_CHECKING",
      actionLabel: "CROSS-CHECKING CLAIMS ACROSS OFFICIAL .GOV & HEC PORTALS",
      color: "#10B981",
    };
  } else if (meta.activeSpecialist === "SKEPTIC") {
    specialistMeta = {
      type: "SKEPTIC",
      category: "AGENT",
      displayName: "SKEPTIC AGENT",
      state: step === "SKEPTIC_ACTIVE" ? "CHALLENGING" : "RESOLVED",
      actionLabel: step === "SKEPTIC_ACTIVE" ? "AUDITING DEFICITS & DUAL APPLICATION RISKS" : "EVIDENCE REBUTTAL AUDITED",
      color: "#D4AF37",
    };
  } else if (meta.activeSpecialist === "SYNTHESIS") {
    specialistMeta = {
      type: "SYNTHESIS",
      category: "WORKFLOW",
      displayName: "SYNTHESIS WORKFLOW",
      state: "COMPLETED",
      actionLabel: "AGGREGATING 6 INDEPENDENT FINDINGS INTO UNIFIED SUMMARY",
      color: "#A855F7",
    };
  }

  // Derive active physical packets in flight
  const activePackets: PhysicalPacket[] = [];

  if (step === "INVESTIGATION_INIT") {
    activePackets.push({
      id: "pkt-init-cmd",
      type: "COMMAND",
      senderId: "commander-root",
      senderName: "ScholarX Commander",
      receiverId: "investigation-target",
      receiverName: "Stipendium Hungaricum",
      summary: "DEPLOY MULTI-PROCESS INVESTIGATION DIRECTIVE",
      priority: "CRITICAL",
      sourcePos: INVESTIGATION_ANCHORS.commander,
      targetPos: INVESTIGATION_ANCHORS.target,
      progress: 0.65,
      state: "TRAVELING",
    });
  } else if (step === "ELIGIBILITY_DOCKED") {
    activePackets.push({
      id: "pkt-elig-result",
      type: "REPORT",
      senderId: "specialist-elig",
      senderName: "Eligibility Investigator",
      receiverId: "investigation-target",
      receiverName: "Stipendium Hungaricum",
      summary: "13/15 MATCHED // 400 BILATERAL SEATS",
      priority: "HIGH",
      sourcePos: INVESTIGATION_ANCHORS.specialists.ELIGIBILITY,
      targetPos: INVESTIGATION_ANCHORS.target,
      progress: 1.0,
      state: "DOCKED",
    });
  } else if (step === "DOCUMENT_DOCKED") {
    activePackets.push({
      id: "pkt-doc-result",
      type: "REPORT",
      senderId: "specialist-doc",
      senderName: "Document Analyst",
      receiverId: "investigation-target",
      receiverName: "Stipendium Hungaricum",
      summary: "DOC READINESS 62% // 28 DAYS LEAD TIME",
      priority: "NORMAL",
      sourcePos: INVESTIGATION_ANCHORS.specialists.DOCUMENT,
      targetPos: INVESTIGATION_ANCHORS.target,
      progress: 1.0,
      state: "DOCKED",
    });
  } else if (step === "COST_DOCKED") {
    activePackets.push({
      id: "pkt-cost-result",
      type: "REPORT",
      senderId: "specialist-cost",
      senderName: "True Cost Analyzer",
      receiverId: "investigation-target",
      receiverName: "Stipendium Hungaricum",
      summary: "PKR 303,500 INITIAL OUT-OF-POCKET",
      priority: "HIGH",
      sourcePos: INVESTIGATION_ANCHORS.specialists.COST,
      targetPos: INVESTIGATION_ANCHORS.target,
      progress: 1.0,
      state: "DOCKED",
    });
  } else if (step === "DEADLINE_DOCKED") {
    activePackets.push({
      id: "pkt-dl-result",
      type: "REPORT",
      senderId: "specialist-deadline",
      senderName: "Deadline Intelligence",
      receiverId: "investigation-target",
      receiverName: "Stipendium Hungaricum",
      summary: "DEADLINE 15 JAN // 37 DAYS SLACK",
      priority: "NORMAL",
      sourcePos: INVESTIGATION_ANCHORS.specialists.DEADLINE,
      targetPos: INVESTIGATION_ANCHORS.target,
      progress: 1.0,
      state: "DOCKED",
    });
  } else if (step === "SKEPTIC_ACTIVE") {
    activePackets.push({
      id: "pkt-skep-challenge",
      type: "CHALLENGE",
      senderId: "specialist-skeptic",
      senderName: "Skeptic Agent",
      receiverId: "specialist-verification",
      receiverName: "Verification Agent",
      summary: "CHALLENGE: UNCOVERED FLIGHT & AIRFARE DEFICIT",
      priority: "CRITICAL",
      sourcePos: INVESTIGATION_ANCHORS.specialists.SKEPTIC,
      targetPos: INVESTIGATION_ANCHORS.specialists.VERIFICATION,
      progress: 0.7,
      state: "TRAVELING",
    });
  } else if (step === "CHALLENGE_RESOLVED") {
    activePackets.push({
      id: "pkt-verif-response",
      type: "RESOLUTION",
      senderId: "specialist-verification",
      senderName: "Verification Agent",
      receiverId: "specialist-skeptic",
      receiverName: "Skeptic Agent",
      summary: "OFFICIAL TEMPUS RULES QUALIFIED // HEC DUAL GATE CONFIRMED",
      priority: "CRITICAL",
      sourcePos: INVESTIGATION_ANCHORS.specialists.VERIFICATION,
      targetPos: INVESTIGATION_ANCHORS.specialists.SKEPTIC,
      progress: 1.0,
      state: "DOCKED",
    });
  } else if (step === "SYNTHESIS_COMPLETE") {
    activePackets.push({
      id: "pkt-synth-final",
      type: "RESOLUTION",
      senderId: "specialist-synthesis",
      senderName: "Synthesis Workflow",
      receiverId: "commander-root",
      receiverName: "ScholarX Commander",
      summary: "INVESTIGATION COMPLETE // EVIDENCE SYNTHESIZED",
      priority: "CRITICAL",
      sourcePos: INVESTIGATION_ANCHORS.target,
      targetPos: INVESTIGATION_ANCHORS.commander,
      progress: 1.0,
      state: "DOCKED",
    });
  }

  // Focus entity derivation
  const focusedEntity = meta.activeSpecialist || "TARGET";

  return {
    step,
    stepMeta: meta,
    target,
    activeSpecialist: meta.activeSpecialist,
    specialistMeta,
    eligibilityData: ELIGIBILITY_FIXTURE,
    documentData: DOCUMENT_FIXTURE,
    costData: COST_FIXTURE,
    deadlineData: DEADLINE_FIXTURE,
    verificationData: VERIFICATION_FIXTURE,
    skepticData: SKEPTIC_FIXTURE,
    synthesisSummary: SYNTHESIS_FIXTURE,
    activePackets,
    focusedEntity,
  };
}
