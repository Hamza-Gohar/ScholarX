// Phase 5: Global AI Research Fleet Store & Fixtures (§7, §8, §10, §12, §13, §27, §43, §44)
import { Region } from "../types";
import {
  DiscoveredSource,
  ScholarshipCandidateSummary,
  SectorReportSummary,
  PhysicalPacket,
} from "../communication/types";
import { CommanderDirective } from "../agents/types";
import {
  ScoutState,
  ToolActivityMeta,
  RegionalScoutData,
  Phase5Step,
  Phase5StepMeta,
  FleetSnapshot,
} from "./types";

// Stage Coordinates & Spatial Anchors (Calibrated for 1920x1080 stage)
export const FLEET_STAGE_ANCHORS = {
  // Commander Console Center (Center Stage, aligned with Pakistan origin)
  commanderCenter: { x: 960, y: 460 },
  // Regional Scout Anchors on 1920x1080 Spatial Theatre
  scouts: {
    Europe: { x: 614, y: 120 },      // North-West / Central Europe
    Americas: { x: 185, y: 360 },    // West / Americas
    Asia: { x: 1735, y: 360 },       // East / East Asia
    MENA: { x: 215, y: 780 },        // Southwest / Gulf & Middle East
    Oceania: { x: 1705, y: 780 },    // Southeast / Australasia
  } as Record<Region, { x: number; y: number }>,
};

// Reusable Research Tools (§12, §13)
export const RESEARCH_TOOLS: Record<string, ToolActivityMeta> = {
  TAVILY: {
    type: "TAVILY_SEARCH",
    displayName: "TAVILY SEARCH",
    actionLabel: "SEARCHING",
    color: "#38BDF8", // Ice blue
    iconName: "Search",
    executionNote: "Executing multi-domain query across official academic registries",
  },
  FIRECRAWL: {
    type: "FIRECRAWL",
    displayName: "FIRECRAWL",
    actionLabel: "SCRAPING",
    color: "#F97316", // Warm amber/orange
    iconName: "Globe",
    executionNote: "Deep DOM traversal and JavaScript portal rendering",
  },
  JINA_READER: {
    type: "JINA_READER",
    displayName: "JINA READER",
    actionLabel: "READING",
    color: "#10B981", // Emerald
    iconName: "FileText",
    executionNote: "Streaming high-speed markdown extraction",
  },
  CRAWL4AI: {
    type: "CRAWL4AI",
    displayName: "CRAWL4AI",
    actionLabel: "CRAWLING",
    color: "#A855F7", // Purple
    iconName: "Cpu",
    executionNote: "Parallel university funding directory crawling",
  },
  GEMINI_EXTRACTION: {
    type: "GEMINI_EXTRACTION",
    displayName: "GEMINI 3.7 FLASH",
    actionLabel: "EXTRACTING",
    color: "#D4AF37", // Gold
    iconName: "Sparkles",
    executionNote: "Structured schema extraction with strict Pakistani eligibility validation",
  },
  CANONICAL_NORMALIZER: {
    type: "CANONICAL_NORMALIZER",
    displayName: "NORMALIZER",
    actionLabel: "NORMALIZING",
    color: "#34D399", // Emerald tint
    iconName: "CheckCircle",
    executionNote: "Formatting into canonical Scholarship DNA data schema",
  },
};

// Authentic Pakistani Regional Scholarship Fixtures (§32, §43, Agents.md)
export const REGIONAL_FIXTURES: Record<
  Region,
  {
    query: string;
    sources: DiscoveredSource[];
    candidates: ScholarshipCandidateSummary[];
    report: SectorReportSummary;
    pakistanQuotaSeats: number;
  }
> = {
  Europe: {
    query: "Stipendium Hungaricum Pakistan HEC bilateral quota 2026 2027 fully funded",
    sources: [
      {
        id: "src-eu-1",
        domain: "stipendiumhungaricum.hu",
        title: "Tempus Public Foundation / Hungarian Bilateral Quotas",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 400,
        country: "Hungary",
      },
      {
        id: "src-eu-2",
        domain: "daad.de",
        title: "German Academic Exchange Service (DAAD) Helmut-Schmidt Portal",
        sourceType: "PORTAL",
        verificationStatus: "VERIFIED",
        quotaSeats: 25,
        country: "Germany",
      },
      {
        id: "src-eu-3",
        domain: "campusfrance.org",
        title: "Campus France / Eiffel Excellence Master Quotas",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        country: "France",
      },
    ],
    candidates: [
      {
        id: "cand-eu-1",
        title: "Stipendium Hungaricum Scholarship 2025/2026",
        country: "Hungary",
        degreeLevel: "Master of Science (MSc Computer Science)",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "HUF 43,700 / month + Free Dormitory",
        pakistanQuotaSeats: 400,
        hecAttestationRequired: true,
        confidenceScore: 98,
      },
      {
        id: "cand-eu-2",
        title: "DAAD Helmut-Schmidt Master Programme",
        country: "Germany",
        degreeLevel: "MSc Informatics & Applied Data Science",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "€934 / month + Health & Travel Cover",
        pakistanQuotaSeats: 25,
        hecAttestationRequired: true,
        confidenceScore: 94,
      },
      {
        id: "cand-eu-3",
        title: "Erasmus Mundus Joint Master (GENIAL)",
        country: "France / EU",
        degreeLevel: "Master of Science in Sustainable ICT & AI",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "€1,400 / month + Travel Allowance",
        hecAttestationRequired: true,
        confidenceScore: 91,
      },
    ],
    report: {
      sector: "Europe",
      candidatesCount: 3,
      highRelevanceCount: 3,
      pakistanQuotaSeats: 425,
      verificationNeeds: [
        "HEC Degree Attestation",
        "IBCC Equivalence Confirmation",
        "English Proficiency Certificate",
      ],
      keyFinding:
        "400 bilateral government quota seats verified for Pakistani students via HEC portal with zero tuition and dormitory provided.",
      candidates: [],
    },
    pakistanQuotaSeats: 425,
  },

  Asia: {
    query: "CSC Chinese Government Scholarship Pakistani students requirements CUCAS 2026",
    sources: [
      {
        id: "src-asia-1",
        domain: "campuschina.org",
        title: "China Scholarship Council (CSC) / Pakistan Bilateral Channel",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 200,
        country: "China",
      },
      {
        id: "src-asia-2",
        domain: "studyinkorea.go.kr",
        title: "National Institute for International Education (NIIED) - GKS",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 40,
        country: "South Korea",
      },
      {
        id: "src-asia-3",
        domain: "jasso.go.jp",
        title: "Japan Student Services Organization / MEXT Embassy & University",
        sourceType: "PORTAL",
        verificationStatus: "VERIFIED",
        country: "Japan",
      },
    ],
    candidates: [
      {
        id: "cand-asia-1",
        title: "Chinese Government Scholarship (CSC Type A)",
        country: "China",
        degreeLevel: "Master / PhD in Computer Science",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "RMB 3,000 - 3,500 / month + Campus Housing",
        pakistanQuotaSeats: 200,
        hecAttestationRequired: true,
        confidenceScore: 96,
      },
      {
        id: "cand-asia-2",
        title: "Global Korea Scholarship (GKS-G)",
        country: "South Korea",
        degreeLevel: "Master of Science in Artificial Intelligence",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "KRW 1,000,000 / month + Settlement Allowance",
        pakistanQuotaSeats: 40,
        hecAttestationRequired: true,
        confidenceScore: 93,
      },
      {
        id: "cand-asia-3",
        title: "MEXT University Recommendation Fellowship",
        country: "Japan",
        degreeLevel: "Master of Engineering (Computer Systems)",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "JPY 144,000 / month + Roundtrip Airfare",
        hecAttestationRequired: false,
        confidenceScore: 89,
      },
    ],
    report: {
      sector: "Asia",
      candidatesCount: 3,
      highRelevanceCount: 3,
      pakistanQuotaSeats: 240,
      verificationNeeds: [
        "HEC Online Registration & HAT Score",
        "Physical Examination Form (Foreigner)",
        "Police Character Clearance",
      ],
      keyFinding:
        "200+ direct bilateral quota seats allocated through HEC for CSC Type A; GKS adds 40 dedicated Pakistani seats.",
      candidates: [],
    },
    pakistanQuotaSeats: 240,
  },

  Americas: {
    query: "Fulbright Pakistan Master PhD computer science USEFP 2026 deadline",
    sources: [
      {
        id: "src-am-1",
        domain: "usefp.org",
        title: "United States Educational Foundation in Pakistan (USEFP)",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 150,
        country: "United States",
      },
      {
        id: "src-am-2",
        domain: "vanier.gc.ca",
        title: "Government of Canada / Vanier Graduate Scholarships",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        country: "Canada",
      },
      {
        id: "src-am-3",
        domain: "admissions.mit.edu",
        title: "Graduate Research Assistantships (EECS RA/TA)",
        sourceType: "UNIVERSITY",
        verificationStatus: "VERIFIED",
        country: "United States",
      },
    ],
    candidates: [
      {
        id: "cand-am-1",
        title: "Fulbright Foreign Student Program (Pakistan)",
        country: "United States",
        degreeLevel: "Master of Science in Computer Science",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition + Fees",
        monthlyStipend: "$2,200 - $2,600 / month + Comprehensive J-1 Cover",
        pakistanQuotaSeats: 150,
        hecAttestationRequired: true,
        confidenceScore: 97,
      },
      {
        id: "cand-am-2",
        title: "Vanier Canada Graduate Scholarship",
        country: "Canada",
        degreeLevel: "Doctor of Philosophy (PhD Computing Science)",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Tuition Waiver via University Top-up",
        monthlyStipend: "CAD $50,000 / year (3 years guaranteed)",
        hecAttestationRequired: true,
        confidenceScore: 90,
      },
    ],
    report: {
      sector: "Americas",
      candidatesCount: 2,
      highRelevanceCount: 2,
      pakistanQuotaSeats: 150,
      verificationNeeds: [
        "GRE General Exam (USEFP funded voucher)",
        "3 Academic Letters of Recommendation",
        "Statement of Purpose & Study Objectives",
      ],
      keyFinding:
        "World's largest Fulbright program active in Pakistan with 150 full grants covering all tuition, stipend, and airfare.",
      candidates: [],
    },
    pakistanQuotaSeats: 150,
  },

  MENA: {
    query: "Turkiye Burslari scholarship Pakistan HEC portal 2026 fully funded CS",
    sources: [
      {
        id: "src-mena-1",
        domain: "turkiyeburslari.gov.tr",
        title: "Presidency for Turks Abroad (YTB) / Turkiye Scholarships",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 120,
        country: "Turkey",
      },
      {
        id: "src-mena-2",
        domain: "kaust.edu.sa",
        title: "King Abdullah University of Science and Technology Fellowship",
        sourceType: "UNIVERSITY",
        verificationStatus: "VERIFIED",
        country: "Saudi Arabia",
      },
      {
        id: "src-mena-3",
        domain: "kfupm.edu.sa",
        title: "King Fahd University of Petroleum & Minerals Deanship Fellowship",
        sourceType: "UNIVERSITY",
        verificationStatus: "VERIFIED",
        country: "Saudi Arabia",
      },
    ],
    candidates: [
      {
        id: "cand-mena-1",
        title: "Türkiye Bursları Government Scholarship",
        country: "Turkey",
        degreeLevel: "Bachelor / Master in Computer Engineering",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "TRY 4,500 - 6,000 / month + Dormitory + Airfare",
        pakistanQuotaSeats: 120,
        hecAttestationRequired: true,
        confidenceScore: 96,
      },
      {
        id: "cand-mena-2",
        title: "KAUST Global Fellowship in AI & Robotics",
        country: "Saudi Arabia",
        degreeLevel: "Master / PhD in Computer Science",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "$25,000 - $30,000 / year + Free Housing",
        hecAttestationRequired: false,
        confidenceScore: 95,
      },
      {
        id: "cand-mena-3",
        title: "KFUPM Graduate Scholarship (CS & Data)",
        country: "Saudi Arabia",
        degreeLevel: "MSc Computer Networks & Software Systems",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "SAR 1,800 / month + Free Furnished Housing",
        hecAttestationRequired: false,
        confidenceScore: 92,
      },
    ],
    report: {
      sector: "MENA",
      candidatesCount: 3,
      highRelevanceCount: 3,
      pakistanQuotaSeats: 120,
      verificationNeeds: [
        "Family Registration Certificate (FRC)",
        "Equivalence Certificate from Turkish MEB",
        "HEC Attested Degree Copies",
      ],
      keyFinding:
        "Turkiye Burslari provides 120 zero-cost bilateral seats with waived visa fees; KAUST offers $30k stipend with full housing.",
      candidates: [],
    },
    pakistanQuotaSeats: 120,
  },

  Oceania: {
    query: "Australia Awards Pakistan priority fields computer science 2026",
    sources: [
      {
        id: "src-oc-1",
        domain: "australiaawards.gov.au",
        title: "DFAT Australia Awards / South Asia Bilateral Allocation",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        quotaSeats: 25,
        country: "Australia",
      },
      {
        id: "src-oc-2",
        domain: "mfat.govt.nz",
        title: "Manaaki New Zealand Scholarships Programme",
        sourceType: "GOVERNMENT",
        verificationStatus: "VERIFIED",
        country: "New Zealand",
      },
    ],
    candidates: [
      {
        id: "cand-oc-1",
        title: "Australia Awards Scholarship (Pakistan)",
        country: "Australia",
        degreeLevel: "Master of Information Technology & Cybersecurity",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "AUD $3,200 / month + Return Airfare + Establishment Allowance",
        pakistanQuotaSeats: 25,
        hecAttestationRequired: true,
        confidenceScore: 95,
      },
      {
        id: "cand-oc-2",
        title: "Manaaki New Zealand Development Scholarship",
        country: "New Zealand",
        degreeLevel: "Master of Science (Applied AI & Data Science)",
        fundingType: "Fully Funded",
        tuitionCoverage: "100% Full Tuition Waiver",
        monthlyStipend: "NZD $620 / week + Medical & Travel Insurance",
        hecAttestationRequired: true,
        confidenceScore: 91,
      },
    ],
    report: {
      sector: "Oceania",
      candidatesCount: 2,
      highRelevanceCount: 2,
      pakistanQuotaSeats: 25,
      verificationNeeds: [
        "Development Impact Plan for Pakistan",
        "Employer / Institutional Endorsement",
        "IELTS Academic Band 6.5 minimum",
      ],
      keyFinding:
        "Full developmental funding confirmed for Pakistani nationals; includes AUD 5,000 initial establishment grant upon arrival.",
      candidates: [],
    },
    pakistanQuotaSeats: 25,
  },
};

// 12 Cinematic Demonstration Scenes (§10, §47)
export const PHASE_5_STEPS: Phase5StepMeta[] = [
  {
    step: "FLEET_INIT",
    index: 0,
    label: "01. Global Mission Established",
    narrative: "Commander activates central intelligence: 'GLOBAL SCHOLARSHIP DISCOVERY'. Target: Zero out-of-pocket CS scholarships for Pakistani students.",
    durationMs: 1400,
    cameraShot: "GLOBAL",
    focusedRegion: "Pakistan",
    focusedEntity: "COMMANDER",
  },
  {
    step: "DIRECTIVES_FORMED",
    index: 1,
    label: "02. Directives Formulated",
    narrative: "Commander synthesizes 5 regional directives targeting bilateral quotas across Europe, Asia, Americas, MENA, and Oceania.",
    durationMs: 1200,
    cameraShot: "GLOBAL",
    focusedRegion: "Pakistan",
    focusedEntity: "COMMANDER",
  },
  {
    step: "STAGGERED_DISPATCH",
    index: 2,
    label: "03. Fleet Command Dispatch",
    narrative: "Commander dispatches command packets in a controlled staggered fan-out (Europe +0ms, Asia +180ms, MENA +320ms, Americas +500ms, Oceania +680ms).",
    durationMs: 1500,
    cameraShot: "DEPLOYMENT",
    focusedRegion: null,
    focusedEntity: "FLEET",
  },
  {
    step: "SCOUTS_ACKNOWLEDGE",
    index: 3,
    label: "04. Scouts Acknowledge Directives",
    narrative: "All five regional scouts dock command packets and transmit ACK confirmation packets back to Commander.",
    durationMs: 1200,
    cameraShot: "DEPLOYMENT",
    focusedRegion: null,
    focusedEntity: "FLEET",
  },
  {
    step: "PARALLEL_SEARCH_START",
    index: 4,
    label: "05. Parallel Web Discovery",
    narrative: "Five regional workflows initiate simultaneous searches using Tavily Search across continental academic registries.",
    durationMs: 1400,
    cameraShot: "REGIONAL",
    focusedRegion: "Europe",
    focusedEntity: "Europe",
  },
  {
    step: "DIVERGENT_TOOL_OPERATIONS",
    index: 5,
    label: "06. Divergent Tool Execution",
    narrative: "Scouts branch into specialized tools: Europe & MENA deep-scrape via Firecrawl, Asia & Oceania stream via Jina Reader, Americas crawls via Crawl4AI.",
    durationMs: 1500,
    cameraShot: "REGIONAL",
    focusedRegion: "Asia",
    focusedEntity: "Asia",
  },
  {
    step: "SOURCES_DISCOVERED",
    index: 6,
    label: "07. Institutional Sources Found",
    narrative: "Official government scholarship portals emerge visibly across all 5 sectors (stipendiumhungaricum.hu, campuschina.org, usefp.org, etc.).",
    durationMs: 1400,
    cameraShot: "REGIONAL",
    focusedRegion: "Americas",
    focusedEntity: "Americas",
  },
  {
    step: "CANDIDATE_EMERGENCE",
    index: 7,
    label: "08. Candidate Crystallization",
    narrative: "Gemini 3.7 Flash extracts and normalizes candidates: 13 fully funded opportunities emerge with verified Pakistani bilateral quotas.",
    durationMs: 1600,
    cameraShot: "REGIONAL",
    focusedRegion: "MENA",
    focusedEntity: "MENA",
  },
  {
    step: "REGIONAL_REPORTS_ASSEMBLED",
    index: 8,
    label: "09. Regional Reports Assembled",
    narrative: "Each scout compiles its discoveries into a high-density, compressed transmission report package.",
    durationMs: 1400,
    cameraShot: "REGIONAL",
    focusedRegion: "Oceania",
    focusedEntity: "Oceania",
  },
  {
    step: "STAGGERED_REPORT_RETURN",
    index: 9,
    label: "10. Staggered Report Flights",
    narrative: "Report capsules return physically along curved geographic arcs toward Commander (Europe arrives first, followed by Asia, MENA, Americas, Oceania).",
    durationMs: 1600,
    cameraShot: "GLOBAL",
    focusedRegion: null,
    focusedEntity: "FLEET",
  },
  {
    step: "COMMANDER_AGGREGATION",
    index: 10,
    label: "11. Commander Global Synthesis",
    narrative: "Commander absorbs incoming intelligence packets, synthesizing 13 verified opportunities and 960 dedicated Pakistani quota seats.",
    durationMs: 1800,
    cameraShot: "GLOBAL",
    focusedRegion: "Pakistan",
    focusedEntity: "COMMANDER",
  },
  {
    step: "FLEET_COMPLETE",
    index: 11,
    label: "12. Global Fleet Mission Resolved",
    narrative: "Autonomous fleet stands down into complete state. Global intelligence pool established and prepared for Phase 6 eligibility & skeptic challenge.",
    durationMs: 2200,
    cameraShot: "GLOBAL",
    focusedRegion: "Pakistan",
    focusedEntity: "COMMANDER",
  },
];

// Helper to construct in-flight physical packets dynamically based on scene step
function generatePacketsForStep(step: Phase5Step): PhysicalPacket[] {
  const pk = FLEET_STAGE_ANCHORS.commanderCenter;
  const regions: Region[] = ["Europe", "Asia", "Americas", "MENA", "Oceania"];

  switch (step) {
    case "STAGGERED_DISPATCH":
      // 5 Command packets fan out from Commander to 5 scouts with staggered progress
      return regions.map((region, idx) => {
        const dest = FLEET_STAGE_ANCHORS.scouts[region];
        const staggerProgress = [0.85, 0.7, 0.55, 0.4, 0.25][idx];
        return {
          id: `cmd-pkt-${region.toLowerCase()}`,
          type: "COMMAND",
          senderId: "commander-root",
          senderName: "ScholarX Commander",
          receiverId: `scout-${region.toLowerCase()}`,
          receiverName: `${region} Scout`,
          summary: `GLOBAL DIRECTIVE // ${region.toUpperCase()} SCOPE`,
          priority: "HIGH",
          sourcePos: pk,
          targetPos: dest,
          progress: staggerProgress,
          state: "TRAVELING",
          payload: {
            directive: {
              objective: `Discover fully funded CS scholarships in ${region} with Pakistani quotas.`,
              expectedOutput: "Normalized scholarship records with verified HEC criteria.",
              constraints: ["Zero Out-of-Pocket Preferred", "Living Allowance Covered"],
            },
          },
        };
      });

    case "SCOUTS_ACKNOWLEDGE":
      // 5 ACK packets returning from scouts to Commander
      return regions.map((region, idx) => {
        const src = FLEET_STAGE_ANCHORS.scouts[region];
        const staggerProgress = [0.9, 0.75, 0.65, 0.5, 0.35][idx];
        return {
          id: `ack-pkt-${region.toLowerCase()}`,
          type: "ACKNOWLEDGEMENT",
          senderId: `scout-${region.toLowerCase()}`,
          senderName: `${region} Scout`,
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: `${region.toUpperCase()} // DIRECTIVE ACKNOWLEDGED`,
          priority: "NORMAL",
          sourcePos: src,
          targetPos: pk,
          progress: staggerProgress,
          state: "TRAVELING",
          payload: {
            ackMessage: `${region} Scout initiated deterministic search pipeline.`,
          },
        };
      });

    case "STAGGERED_REPORT_RETURN":
      // 5 Sector report packets returning from scouts to Commander
      return regions.map((region, idx) => {
        const src = FLEET_STAGE_ANCHORS.scouts[region];
        const staggerProgress = [0.95, 0.8, 0.65, 0.45, 0.3][idx];
        const fixture = REGIONAL_FIXTURES[region];
        return {
          id: `report-pkt-${region.toLowerCase()}`,
          type: "REPORT",
          senderId: `scout-${region.toLowerCase()}`,
          senderName: `${region} Scout`,
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: `${region.toUpperCase()} REPORT // ${fixture.candidates.length} CANDIDATES`,
          priority: "CRITICAL",
          sourcePos: src,
          targetPos: pk,
          progress: staggerProgress,
          state: "TRAVELING",
          payload: {
            report: {
              ...fixture.report,
              candidates: fixture.candidates,
            },
          },
        };
      });

    default:
      return [];
  }
}

// Master deterministic snapshot generator for any Phase 5 scene (§27, §43, §44)
export function getPhase5Snapshot(
  step: Phase5Step,
  userFocusedRegion?: Region | "Pakistan" | null
): FleetSnapshot {
  const stepMeta = PHASE_5_STEPS.find((s) => s.step === step) || PHASE_5_STEPS[0];
  const regions: Region[] = ["Europe", "Asia", "Americas", "MENA", "Oceania"];

  // Determine Commander state and decisions
  let commanderState: any = "THINKING";
  let headline = "GLOBAL SCHOLARSHIP DISCOVERY";
  let currentDecision: string | null = null;

  switch (step) {
    case "FLEET_INIT":
      commanderState = "THINKING";
      headline = "GLOBAL SCHOLARSHIP DISCOVERY // INITIATING FLEET";
      currentDecision = "Formulating 5 continental search strategies for Pakistani applicants";
      break;
    case "DIRECTIVES_FORMED":
      commanderState = "DIRECTING";
      headline = "REGIONAL DIRECTIVES FORMULATED";
      currentDecision = "DISPATCHING 5 AUTONOMOUS REGIONAL SCOUTS";
      break;
    case "STAGGERED_DISPATCH":
      commanderState = "DIRECTING";
      headline = "COMMAND PACKETS IN FLIGHT";
      currentDecision = "Awaiting deployment confirmation from regional scouts";
      break;
    case "SCOUTS_ACKNOWLEDGE":
      commanderState = "WAITING";
      headline = "FLEET ACKNOWLEDGED // SCOUTS ENGAGED";
      currentDecision = "All 5 regional workflows active and researching in parallel";
      break;
    case "PARALLEL_SEARCH_START":
    case "DIVERGENT_TOOL_OPERATIONS":
    case "SOURCES_DISCOVERED":
    case "CANDIDATE_EMERGENCE":
      commanderState = "WAITING";
      headline = "FLEET CONDUCTING PARALLEL RESEARCH";
      currentDecision = "Monitoring concurrent data collection across 5 continents";
      break;
    case "REGIONAL_REPORTS_ASSEMBLED":
      commanderState = "WAITING";
      headline = "REGIONAL REPORTS ASSEMBLED";
      currentDecision = "Awaiting report transmission from regional workflows";
      break;
    case "STAGGERED_REPORT_RETURN":
      commanderState = "RECEIVING";
      headline = "INCOMING REGIONAL INTELLIGENCE";
      currentDecision = "Absorbing incoming sector report packages";
      break;
    case "COMMANDER_AGGREGATION":
      commanderState = "SYNTHESIZING";
      headline = "SYNTHESIZING GLOBAL CANDIDATE POOL";
      currentDecision = "Synthesizing 13 candidates & 960 bilateral quota seats";
      break;
    case "FLEET_COMPLETE":
      commanderState = "COMPLETE";
      headline = "GLOBAL DISCOVERY COMPLETE";
      currentDecision = "Candidate pool prepared for Phase 6 eligibility & skeptic challenge";
      break;
  }

  // Build Scout States for this step
  const scouts = {} as Record<Region, RegionalScoutData>;

  regions.forEach((region) => {
    const fixture = REGIONAL_FIXTURES[region];
    let scoutState: ScoutState = "IDLE";
    let progress = 0;
    let activeTool: ToolActivityMeta | null = null;
    let activeQuery: string | undefined = undefined;
    let currentOperation = "STANDBY";
    let finding = "NO FINDINGS YET";
    let sources: DiscoveredSource[] = [];
    let candidates: ScholarshipCandidateSummary[] = [];
    let report: SectorReportSummary | null = null;
    let reportReady = false;

    switch (step) {
      case "FLEET_INIT":
        scoutState = "IDLE";
        progress = 0;
        currentOperation = "STANDBY // AWAITING DIRECTIVE";
        break;

      case "DIRECTIVES_FORMED":
        scoutState = "DEPLOYING";
        progress = 10;
        currentOperation = "SECTOR INITIALIZATION";
        finding = "Directives formulated at Root Commander";
        break;

      case "STAGGERED_DISPATCH":
        scoutState = "RECEIVING_COMMAND";
        progress = 20;
        currentOperation = "RECEIVING COMMAND DIRECTIVE";
        finding = "Command capsule in flight";
        break;

      case "SCOUTS_ACKNOWLEDGE":
        scoutState = "ACKNOWLEDGING";
        progress = 25;
        currentOperation = "DIRECTIVE ACKNOWLEDGED // PREPARING SEARCH";
        finding = "Command docked. Initiating deterministic workflow.";
        break;

      case "PARALLEL_SEARCH_START":
        scoutState = "SEARCHING";
        progress = 40;
        activeTool = RESEARCH_TOOLS.TAVILY;
        activeQuery = fixture.query;
        currentOperation = `Searching ${region} official scholarship repositories`;
        finding = `Executing query via Tavily Search API across ${region} portals`;
        break;

      case "DIVERGENT_TOOL_OPERATIONS":
        // Controlled variation in tools per region (§11, §12)
        if (region === "Europe" || region === "MENA") {
          scoutState = "SCRAPING";
          activeTool = RESEARCH_TOOLS.FIRECRAWL;
          currentOperation = "Deep scraping dynamic scholarship portals";
          finding = "Firecrawl rendering JavaScript single-page portals";
        } else if (region === "Asia" || region === "Oceania") {
          scoutState = "FILTERING";
          activeTool = RESEARCH_TOOLS.JINA_READER;
          currentOperation = "Streaming and filtering government guidelines";
          finding = "Jina Reader extracting clean markdown from official notices";
        } else {
          // Americas
          scoutState = "SCRAPING";
          activeTool = RESEARCH_TOOLS.CRAWL4AI;
          currentOperation = "Crawling university funding directories";
          finding = "Crawl4AI parsing graduate assistantship eligibility tables";
        }
        progress = 55;
        activeQuery = fixture.query;
        break;

      case "SOURCES_DISCOVERED":
        scoutState = "DISCOVERING";
        progress = 70;
        activeTool = RESEARCH_TOOLS.GEMINI_EXTRACTION;
        currentOperation = `Verified ${fixture.sources.length} institutional scholarship sources`;
        finding = `Discovered: ${fixture.sources.map((s) => s.domain).join(", ")}`;
        sources = fixture.sources;
        activeQuery = fixture.query;
        break;

      case "CANDIDATE_EMERGENCE":
        scoutState = "EXTRACTING";
        progress = 85;
        activeTool = RESEARCH_TOOLS.CANONICAL_NORMALIZER;
        currentOperation = `Extracted ${fixture.candidates.length} high-fit candidates for Pakistani applicants`;
        finding = `Candidates: ${fixture.candidates.map((c) => c.title).slice(0, 2).join(" & ")}`;
        sources = fixture.sources;
        candidates = fixture.candidates;
        activeQuery = fixture.query;
        break;

      case "REGIONAL_REPORTS_ASSEMBLED":
        scoutState = "REPORT_READY";
        progress = 95;
        activeTool = null;
        currentOperation = "Sector transmission package compressed";
        finding = fixture.report.keyFinding;
        sources = fixture.sources;
        candidates = fixture.candidates;
        report = { ...fixture.report, candidates: fixture.candidates };
        reportReady = true;
        break;

      case "STAGGERED_REPORT_RETURN":
        scoutState = "RETURNING";
        progress = 98;
        currentOperation = "Transmitting report capsule to Root Commander";
        finding = "Report packet in flight along curved geographic trajectory";
        sources = fixture.sources;
        candidates = fixture.candidates;
        report = { ...fixture.report, candidates: fixture.candidates };
        reportReady = true;
        break;

      case "COMMANDER_AGGREGATION":
      case "FLEET_COMPLETE":
        scoutState = "COMPLETE";
        progress = 100;
        currentOperation = "SECTOR RESOLVED // STANDBY IN NETWORK";
        finding = fixture.report.keyFinding;
        sources = fixture.sources;
        candidates = fixture.candidates;
        report = { ...fixture.report, candidates: fixture.candidates };
        reportReady = true;
        break;
    }

    scouts[region] = {
      scoutId: `scout-${region.toLowerCase()}`,
      region,
      displayName: `${region} Regional Scout`,
      role: "REGIONAL DISCOVERY WORKFLOW",
      mission: `Discover high-fit CS opportunities for Pakistani students in ${region}.`,
      coordinates:
        region === "Europe"
          ? [13.405, 52.52]
          : region === "Asia"
          ? [116.4074, 39.9042]
          : region === "Americas"
          ? [-77.0369, 38.9072]
          : region === "MENA"
          ? [46.6753, 24.7136]
          : [149.13, -35.2809],
      scenePosition: FLEET_STAGE_ANCHORS.scouts[region],
      state: scoutState,
      progress,
      activeTool,
      activeQuery,
      currentOperation,
      finding,
      sources,
      candidates,
      report,
      reportReady,
      pakistanQuotaSeats: fixture.pakistanQuotaSeats,
    };
  });

  // Calculate fleet stats
  const reportsReceivedCount =
    step === "COMMANDER_AGGREGATION" || step === "FLEET_COMPLETE"
      ? 5
      : step === "STAGGERED_REPORT_RETURN"
      ? 2
      : 0;

  const totalSources = regions.reduce(
    (acc, reg) => acc + scouts[reg].sources.length,
    0
  );
  const totalCandidates = regions.reduce(
    (acc, reg) => acc + scouts[reg].candidates.length,
    0
  );
  const totalSeats = regions.reduce(
    (acc, reg) => acc + scouts[reg].pakistanQuotaSeats,
    0
  );

  const globalStats = {
    scoutsDeployed: 5,
    activeScoutsCount:
      step === "FLEET_INIT"
        ? 0
        : step === "COMMANDER_AGGREGATION" || step === "FLEET_COMPLETE"
        ? 5
        : 5,
    reportsReceived: reportsReceivedCount,
    totalSourcesDiscovered:
      totalSources ||
      (step === "COMMANDER_AGGREGATION" || step === "FLEET_COMPLETE" ? 14 : 0),
    totalCandidatesExtracted:
      totalCandidates ||
      (step === "COMMANDER_AGGREGATION" || step === "FLEET_COMPLETE" ? 13 : 0),
    pakistanQuotaSeatsTotal: totalSeats,
    operationalStatus:
      step === "FLEET_INIT"
        ? "INITIALIZING"
        : step === "STAGGERED_DISPATCH"
        ? "DISPATCHING FLEET"
        : step === "PARALLEL_SEARCH_START" || step === "DIVERGENT_TOOL_OPERATIONS"
        ? "PARALLEL RETRIEVAL ACTIVE"
        : step === "SOURCES_DISCOVERED" || step === "CANDIDATE_EMERGENCE"
        ? "DATA EXTRACTION ACTIVE"
        : step === "STAGGERED_REPORT_RETURN"
        ? "REPORTS IN FLIGHT"
        : step === "COMMANDER_AGGREGATION"
        ? "AGGREGATING INTELLIGENCE"
        : "FLEET MISSION COMPLETE",
  };

  const activePackets = generatePacketsForStep(step);

  const receivedReports: SectorReportSummary[] =
    step === "COMMANDER_AGGREGATION" || step === "FLEET_COMPLETE"
      ? regions.map((r) => ({
          ...REGIONAL_FIXTURES[r].report,
          candidates: REGIONAL_FIXTURES[r].candidates,
        }))
      : [];

  return {
    step,
    stepMeta,
    commander: {
      state: commanderState,
      mission:
        "Discover and verify fully funded educational opportunities for Pakistani students across 5 global regions.",
      headline,
      currentDecision,
      activeDirectives: regions.map((r) => ({
        targetId: `scout-${r.toLowerCase()}`,
        targetName: `${r} Regional Scout`,
        targetType: "WORKFLOW",
        objective: `Discover fully funded CS opportunities in ${r}.`,
        expectedOutput: "Normalized scholarship records with verified HEC bilateral criteria.",
        constraints: [
          "HEC Attestation & IBCC Equivalence Compatible",
          "Zero Out-of-Pocket / Living Stipend Covered",
          "Pakistani Bilateral Quota Prioritized",
        ],
      })),
      receivedReports,
    },
    scouts,
    activePackets,
    globalStats,
    focusedRegion: userFocusedRegion !== undefined ? userFocusedRegion : stepMeta.focusedRegion,
    focusedEntity:
      userFocusedRegion !== undefined
        ? userFocusedRegion === "Pakistan"
          ? "COMMANDER"
          : userFocusedRegion || "FLEET"
        : stepMeta.focusedEntity,
  };
}
