import type { Metadata } from "next";
import { CommandTheatreClient } from "@/components/theatre/CommandTheatreClient";
import { Phase3Scenario } from "@/lib/agents/types";
import { Phase4Step } from "@/lib/communication/types";
import { Phase5Step } from "@/lib/fleet/types";
import { Phase6Step } from "@/lib/investigation/types";
import { Phase7Step } from "@/lib/ranking/types";
import { LiveVisualPhase } from "@/lib/theatre/theatreDirectorStore";
import { MapState } from "@/lib/spatial/types";
import { Region } from "@/lib/types";

export const metadata: Metadata = {
  title: "ScholarX AI — Scholarships for Pakistani Students | Fully Funded Programs",
  description: "ScholarX AI is Pakistan's premier autonomous scholarship intelligence platform. Discover 310+ fully funded international scholarships for Pakistani students, bilateral quotas (Fulbright, Chevening, DAAD, CSC, Stipendium Hungaricum, MEXT, Turkiye Burslari), and HEC attestation roadmaps.",
  keywords: [
    "ScholarX",
    "ScholarX AI",
    "Scholar X",
    "scholarx-ai",
    "scholarships for pakistani students",
    "scholarships for pakistan students",
    "fully funded scholarships for pakistani students",
    "hec foreign scholarships",
    "stipendium hungaricum scholarship pakistan",
    "turkiye burslari scholarship pakistan",
    "chinese government scholarship csc pakistan",
    "daad scholarship germany pakistan",
    "fulbright scholarship pakistan",
    "chevening scholarship pakistan",
  ],
  alternates: {
    canonical: "./",
  },
  openGraph: {
    title: "ScholarX AI — Scholarships for Pakistani Students",
    description: "Discover 310+ fully funded international scholarships and bilateral quota seats for Pakistani students.",
    url: "/",
    siteName: "ScholarX AI",
    images: [{ url: "/opengraph-image", width: 1200, height: 630, alt: "ScholarX AI" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "ScholarX AI — Scholarships for Pakistani Students",
    description: "Discover 310+ fully funded international scholarships and bilateral quota seats for Pakistani students.",
    images: ["/opengraph-image"],
  },
};


const VALID_LIVE_PHASES: LiveVisualPhase[] = [
  "INITIALIZING",
  "FLEET_DISCOVERY",
  "SPECIALIST_INVESTIGATION",
  "RANKING_EVALUATION",
  "ROADMAP_ASSEMBLY",
  "DOSSIER_BUILD",
  "MISSION_COMPLETE",
];

const VALID_PHASE_7_STEPS: Phase7Step[] = [
  "POOL_INSPECTION",
  "SCORING_INIT",
  "FACTOR_EVALUATION",
  "SCORE_RESOLUTION",
  "SPATIAL_COMPARISON",
  "PRIMARY_SELECTION",
  "ADVISOR_ENGAGEMENT",
  "ROADMAP_GENERATION",
  "DOSSIER_ASSEMBLY",
  "WEB_BUILDER_ACTIVE",
  "PDF_BUILDER_ACTIVE",
  "ARTIFACTS_DELIVERED",
];

const VALID_PHASE_6_STEPS: Phase6Step[] = [
  "TARGET_SELECTION",
  "INVESTIGATION_INIT",
  "ELIGIBILITY_ACTIVE",
  "ELIGIBILITY_DOCKED",
  "DOCUMENT_ACTIVE",
  "DOCUMENT_DOCKED",
  "COST_ACTIVE",
  "COST_DOCKED",
  "DEADLINE_ACTIVE",
  "DEADLINE_DOCKED",
  "VERIFICATION_ACTIVE",
  "SKEPTIC_ACTIVE",
  "CHALLENGE_RESOLVED",
  "SYNTHESIS_COMPLETE",
];

const VALID_PHASE_5_STEPS: Phase5Step[] = [
  "FLEET_INIT",
  "DIRECTIVES_FORMED",
  "STAGGERED_DISPATCH",
  "SCOUTS_ACKNOWLEDGE",
  "PARALLEL_SEARCH_START",
  "DIVERGENT_TOOL_OPERATIONS",
  "SOURCES_DISCOVERED",
  "CANDIDATE_EMERGENCE",
  "REGIONAL_REPORTS_ASSEMBLED",
  "STAGGERED_REPORT_RETURN",
  "COMMANDER_AGGREGATION",
  "FLEET_COMPLETE",
];

const VALID_PHASE_4_STEPS: Phase4Step[] = [
  "DIRECTING",
  "COMMAND_FLIGHT",
  "SCOUT_RECEIVING",
  "ACK_FLIGHT",
  "SEARCHING",
  "SOURCES_FOUND",
  "CANDIDATE_EMERGENCE",
  "REPORT_ASSEMBLY",
  "REPORT_FLIGHT",
  "COMMANDER_SYNTHESIS",
];

export default async function CommandTheatrePage(props: {
  searchParams?: Promise<{
    mode?: string;
    session_id?: string;
    sessionId?: string;
    stage?: string;
    profile?: string;
    scenario?: string;
    livePhase?: string;
    phase7Step?: string;
    phase6Step?: string;
    phase5Step?: string;
    phase4Step?: string;
    phase3State?: string;
    step?: string;
    state?: string;
    region?: string;
  }>;
}) {
  const params = await props.searchParams;

  const rawMode = params?.mode?.toUpperCase();
  const initialMode: "LIVE" | "DEMO" | "PHASE3" | "PHASE4" | "PHASE5" | "PHASE6" | "PHASE7" | undefined =
    rawMode === "LIVE" ||
    rawMode === "DEMO" ||
    rawMode === "PHASE3" ||
    rawMode === "PHASE4" ||
    rawMode === "PHASE5" ||
    rawMode === "PHASE6" ||
    rawMode === "PHASE7"
      ? (rawMode as "LIVE" | "DEMO" | "PHASE3" | "PHASE4" | "PHASE5" | "PHASE6" | "PHASE7")
      : undefined;

  const initialStageIndex = params?.stage !== undefined ? parseInt(params.stage, 10) : undefined;
  const initialProfile = params?.profile;
  const initialScenario = params?.scenario;

  const initialSessionId = params?.sessionId || params?.session_id;

  const rawLive = (params?.livePhase || (rawMode === "LIVE" ? params?.step : undefined))?.toUpperCase() as
    | LiveVisualPhase
    | undefined;
  const livePhase: LiveVisualPhase | undefined =
    rawLive && VALID_LIVE_PHASES.includes(rawLive) ? rawLive : undefined;

  const rawPhase7 = (params?.phase7Step || params?.step)?.toUpperCase() as
    | Phase7Step
    | undefined;
  const phase7Step: Phase7Step | undefined =
    rawPhase7 && VALID_PHASE_7_STEPS.includes(rawPhase7) ? rawPhase7 : undefined;

  const rawPhase6 = (params?.phase6Step || (!phase7Step ? params?.step : undefined))?.toUpperCase() as
    | Phase6Step
    | undefined;
  const phase6Step: Phase6Step | undefined =
    rawPhase6 && VALID_PHASE_6_STEPS.includes(rawPhase6) ? rawPhase6 : undefined;

  const rawPhase5 = (params?.phase5Step || (!phase6Step && !phase7Step ? params?.step : undefined))?.toUpperCase() as
    | Phase5Step
    | undefined;
  const phase5Step: Phase5Step | undefined =
    rawPhase5 && VALID_PHASE_5_STEPS.includes(rawPhase5) ? rawPhase5 : undefined;

  const rawPhase4 = (params?.phase4Step)?.toUpperCase() as
    | Phase4Step
    | undefined;
  const phase4Step: Phase4Step | undefined =
    rawPhase4 && VALID_PHASE_4_STEPS.includes(rawPhase4) ? rawPhase4 : undefined;

  const rawPhase3 = params?.phase3State?.toUpperCase() as Phase3Scenario | undefined;
  const phase3Scenario: Phase3Scenario | undefined =
    rawPhase3 &&
    ["IDLE", "THINKING", "DIRECTING", "SPAWN", "ACTIVE", "WORKING"].includes(rawPhase3)
      ? rawPhase3
      : undefined;

  const rawState = params?.state?.toUpperCase() as MapState | undefined;
  const mapState: MapState | undefined =
    rawState &&
    ["DORMANT", "MISSION", "DEPLOYMENT", "RESEARCH", "EVIDENCE", "DOSSIER"].includes(rawState)
      ? rawState
      : undefined;

  const rawRegion = params?.region;
  const focusedRegion: Region | "Pakistan" | null | undefined =
    rawRegion === "Pakistan"
      ? "Pakistan"
      : ["Europe", "Asia", "Americas", "MENA", "Oceania"].includes(rawRegion || "")
      ? (rawRegion as Region)
      : undefined;

  const homeFaqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: [
      {
        "@type": "Question",
        name: "What is ScholarX AI?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "ScholarX AI is Pakistan's premier autonomous scholarship intelligence platform designed to discover, verify, and match Pakistani students with 310+ fully funded international scholarships and bilateral quota seats.",
        },
      },
      {
        "@type": "Question",
        name: "Where can Pakistani students find fully funded international scholarships?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "ScholarX AI provides an exhaustive, verified directory of 310+ fully funded opportunities across Europe, Asia, the Americas, MENA, and Oceania, including USEFP Fulbright (USA), Chevening (UK), DAAD (Germany), Stipendium Hungaricum (Hungary), Chinese Government Scholarship CSC (China), MEXT (Japan), and Turkiye Burslari.",
        },
      },
      {
        "@type": "Question",
        name: "How does ScholarX AI help Pakistani students apply for bilateral quota scholarships?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "ScholarX AI details exact bilateral quota allocations reserved for Pakistani nationals, document requirements (HEC degree attestation, IBCC equivalence), Medium of Instruction (MOI) acceptance, and consulate visa issuance roadmaps.",
        },
      },
      {
        "@type": "Question",
        name: "Does ScholarX AI charge consultation fees for scholarship discovery?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "No, ScholarX AI is completely free to browse. All official application links point directly to host government and university portals without third-party agent markups.",
        },
      },
    ],
  };

  return (
    <main className="relative min-h-screen">
      {/* Semantic crawlable content for search engines (ScholarX, ScholarX AI, scholarships for pakistan students) */}
      <article className="sr-only">
        <h1>ScholarX AI — The Premier Autonomous Scholarship Intelligence Platform for Pakistani Students</h1>
        <p>
          ScholarX AI (also known as ScholarX or Scholar X) is an autonomous multi-agent intelligence network
          built specifically for Pakistani students seeking fully funded international scholarships, bilateral quota seats,
           and institutional financial aid for Bachelor&apos;s, Master&apos;s, PhD, and Postdoctoral programs.
        </p>
        <h2>Fully Funded Scholarships for Pakistani Students</h2>
        <p>
          Explore over 310 verified international scholarship opportunities abroad with comprehensive Pakistan eligibility audits,
          HEC degree attestation roadmaps, and IBCC equivalence procedures:
        </p>
        <ul>
           <li>USEFP Fulbright Foreign Student Program (United States) — Premier Master&apos;s and PhD award for Pakistan</li>
           <li>Chevening &amp; Commonwealth Scholarships (United Kingdom) — Fully funded master&apos;s and doctoral awards</li>
          <li>DAAD Development-Related Postgraduate Courses (EPOS, Germany) — Tuition-free higher education with monthly stipends</li>
          <li>Stipendium Hungaricum (Hungary) — 400 reserved bilateral quota seats for Pakistani citizens via HEC</li>
          <li>Chinese Government Scholarship (CSC Type A & Type B, China) — Bilateral university programs with full waivers</li>
          <li>MEXT Japanese Government Scholarship (Japan) — Embassy and university recommended degree programs</li>
          <li>Global Korea Scholarship (GKS / KGSP, South Korea) — Funded undergraduate and graduate studies</li>
          <li>Türkiye Bursları Government Scholarship (Turkey) — Complete tuition, accommodation, and stipend support</li>
          <li>Australia Awards for Pakistan — High-impact development scholarships</li>
          <li>Erasmus Mundus Joint Master Degrees (EMJM, European Union) — Prestigious multi-country funded degrees</li>
        </ul>
      </article>

      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(homeFaqSchema) }}
      />

      <CommandTheatreClient
        initialMode={initialMode}
        initialSessionId={initialSessionId}
        initialStageIndex={initialStageIndex}
        initialProfileId={initialProfile}
        initialScenario={initialScenario}
        initialLivePhase={livePhase}
        initialPhase7Step={phase7Step}
        initialPhase6Step={phase6Step}
        initialPhase5Step={phase5Step}
        initialPhase4Step={phase4Step}
        initialPhase3Scenario={phase3Scenario}
        initialMapState={mapState}
        initialFocusedRegion={focusedRegion}
      />
    </main>
  );
}
