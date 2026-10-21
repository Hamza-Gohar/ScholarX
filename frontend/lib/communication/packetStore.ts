// Phase 4 Communication Fixtures and Sequence State Machine (§9, Appendix A.4)
import {
  DiscoveredSource,
  ScholarshipCandidateSummary,
  SectorReportSummary,
  PhysicalPacket,
  Phase4Step,
  Phase4StepMeta,
} from "./types";
import { CommanderState, AgentLifecycleState } from "@/lib/agents/types";

export const STAGE_ANCHORS = {
  commanderRight: { x: 428, y: 330 },
  scoutLeft: { x: 788, y: 330 },
};

export const CANONICAL_SOURCES: DiscoveredSource[] = [
  {
    id: "src-hungary",
    domain: "stipendiumhungaricum.hu",
    title: "Tempus Public Foundation / Hungarian Bilateral Quotas",
    sourceType: "GOVERNMENT",
    verificationStatus: "VERIFIED",
    quotaSeats: 400,
    country: "Hungary",
  },
  {
    id: "src-daad",
    domain: "daad.de",
    title: "German Academic Exchange Service (DAAD) Development Master Portal",
    sourceType: "PORTAL",
    verificationStatus: "VERIFIED",
    country: "Germany",
  },
];

export const CANONICAL_CANDIDATES: ScholarshipCandidateSummary[] = [
  {
    id: "cand-stipendium",
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
    id: "cand-daad",
    title: "DAAD Helmut-Schmidt Programme / Development Studies",
    country: "Germany",
    degreeLevel: "Master of Science (Informatics & Applied CS)",
    fundingType: "Fully Funded",
    tuitionCoverage: "100% Full Tuition Waiver",
    monthlyStipend: "€934 / month + Health & Travel Cover",
    pakistanQuotaSeats: 25,
    hecAttestationRequired: true,
    confidenceScore: 94,
  },
];

export const CANONICAL_REPORT: SectorReportSummary = {
  sector: "Europe",
  candidatesCount: 2,
  highRelevanceCount: 2,
  pakistanQuotaSeats: 400,
  verificationNeeds: [
    "HEC Degree Attestation",
    "IBCC Equivalence Confirmation",
    "English Proficiency Certification",
  ],
  keyFinding:
    "400 bilateral government quota seats verified for Pakistani students with zero tuition and living allowance.",
  candidates: CANONICAL_CANDIDATES,
};

export const PHASE_4_STEPS: Phase4StepMeta[] = [
  {
    step: "DIRECTING",
    index: 0,
    label: "01. Directive Formed",
    narrative: "Commander enters DIRECTING state, formulating concrete research mission.",
    durationMs: 1400,
    cameraShot: "GLOBAL",
    focusedRegion: "Pakistan",
    focusedEntity: "COMMANDER",
  },
  {
    step: "COMMAND_FLIGHT",
    index: 1,
    label: "02. Command Packet Flight",
    narrative: "Command capsule travels physically across the stage to Europe Scout.",
    durationMs: 1200,
    cameraShot: "DEPLOYMENT",
    focusedRegion: "Europe",
    focusedEntity: "COMMANDER",
  },
  {
    step: "SCOUT_RECEIVING",
    index: 2,
    label: "03. Scout Receiving & Dock",
    narrative: "Europe Scout docks command packet, receiving mission constraints.",
    durationMs: 1000,
    cameraShot: "REGIONAL",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "ACK_FLIGHT",
    index: 3,
    label: "04. ACK Packet Return",
    narrative: "Acknowledgement packet returns physically to Commander: 'COMMAND RECEIVED'.",
    durationMs: 950,
    cameraShot: "DEPLOYMENT",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "SEARCHING",
    index: 4,
    label: "05. Active Query Search",
    narrative: "Europe Scout executes active search query across European academic registries.",
    durationMs: 1300,
    cameraShot: "REGIONAL",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "SOURCES_FOUND",
    index: 5,
    label: "06. Sources Discovered",
    narrative: "Institutional portals discovered: stipendiumhungaricum.hu & daad.de verified.",
    durationMs: 1300,
    cameraShot: "REGIONAL",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "CANDIDATE_EMERGENCE",
    index: 6,
    label: "07. Candidate Emergence",
    narrative: "Scholarship candidates emerge directly from research workspace with Pakistan quotas.",
    durationMs: 1500,
    cameraShot: "REGIONAL",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "REPORT_ASSEMBLY",
    index: 7,
    label: "08. Report Compressed",
    narrative: "Scout compresses raw findings into high-density transmission report package.",
    durationMs: 1400,
    cameraShot: "REGIONAL",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "REPORT_FLIGHT",
    index: 8,
    label: "09. Report Packet Flight",
    narrative: "Report capsule travels physically across stage back to Root Commander.",
    durationMs: 1200,
    cameraShot: "GLOBAL",
    focusedRegion: "Europe",
    focusedEntity: "SCOUT",
  },
  {
    step: "COMMANDER_SYNTHESIS",
    index: 9,
    label: "10. Commander Synthesis",
    narrative: "Commander receives report, synthesizes sector intelligence, and formulates next action.",
    durationMs: 2000,
    cameraShot: "GLOBAL",
    focusedRegion: "Pakistan",
    focusedEntity: "COMMANDER",
  },
];

export interface Phase4StateSnapshot {
  step: Phase4Step;
  commander: {
    state: CommanderState;
    mission: string;
    currentDecision: string | null;
    activeDirectiveSummary: string;
  };
  scout: {
    state: AgentLifecycleState;
    currentOperation: string;
    finding: string;
    progress: number;
    activeQuery?: string;
    sources: DiscoveredSource[];
    candidates: ScholarshipCandidateSummary[];
    reportReady: boolean;
  };
  activePacket: PhysicalPacket | null;
}

export const getPhase4Snapshot = (step: Phase4Step): Phase4StateSnapshot => {
  const cPos = STAGE_ANCHORS.commanderRight;
  const sPos = STAGE_ANCHORS.scoutLeft;

  switch (step) {
    case "DIRECTING":
      return {
        step,
        commander: {
          state: "DIRECTING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "DISPATCH DIRECTIVE TO EUROPE SCOUT",
          activeDirectiveSummary: "FIND FUNDED CS OPPORTUNITIES // PAKISTAN QUOTAS PRIORITIZED",
        },
        scout: {
          state: "DEPLOYING",
          currentOperation: "AWAITING MISSION DIRECTIVE",
          finding: "STANDBY FOR TARGET VECTOR",
          progress: 15,
          sources: [],
          candidates: [],
          reportReady: false,
        },
        activePacket: {
          id: "pkt-cmd-01",
          type: "COMMAND",
          senderId: "commander-root",
          senderName: "ScholarX Commander",
          receiverId: "scout-eu",
          receiverName: "Europe Regional Scout",
          summary: "FIND FUNDED CS OPPORTUNITIES",
          priority: "HIGH",
          sourcePos: cPos,
          targetPos: sPos,
          progress: 0.05,
          state: "FORMING",
          payload: {
            directive: {
              objective: "Discover fully funded CS opportunities for Pakistani applicants",
              expectedOutput: "Normalized scholarship candidates with bilateral quotas",
              constraints: [
                "Zero Out-of-Pocket / Full Living Stipend",
                "HEC Attestation & IBCC Equivalence Compatible",
                "Pakistani Bilateral Quota Prioritized",
              ],
            },
          },
        },
      };

    case "COMMAND_FLIGHT":
      return {
        step,
        commander: {
          state: "DIRECTING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "COMMAND PACKET DISPATCHED",
          activeDirectiveSummary: "FIND FUNDED CS OPPORTUNITIES // PACKET IN TRANSIT",
        },
        scout: {
          state: "DEPLOYING",
          currentOperation: "RECEIVING INCOMING TRANSMISSION VECTOR",
          finding: "PACKET INCOMING FROM ROOT COMMANDER",
          progress: 20,
          sources: [],
          candidates: [],
          reportReady: false,
        },
        activePacket: {
          id: "pkt-cmd-01",
          type: "COMMAND",
          senderId: "commander-root",
          senderName: "ScholarX Commander",
          receiverId: "scout-eu",
          receiverName: "Europe Regional Scout",
          summary: "FIND FUNDED CS OPPORTUNITIES",
          priority: "HIGH",
          sourcePos: cPos,
          targetPos: sPos,
          progress: 0.52,
          state: "TRAVELING",
          payload: {
            directive: {
              objective: "Discover fully funded CS opportunities for Pakistani applicants",
              expectedOutput: "Normalized scholarship candidates with bilateral quotas",
              constraints: [
                "Zero Out-of-Pocket / Full Living Stipend",
                "HEC Attestation & IBCC Equivalence Compatible",
              ],
            },
          },
        },
      };

    case "SCOUT_RECEIVING":
      return {
        step,
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "AWAITING SCOUT HANDSHAKE",
          activeDirectiveSummary: "DIRECTIVE DELIVERED TO EUROPE SECTOR",
        },
        scout: {
          state: "RECEIVING",
          currentOperation: "DIRECTIVE INGESTED // VERIFYING PARAMETERS",
          finding: "COMMAND PACKET DOCKED AND VALIDATED",
          progress: 30,
          sources: [],
          candidates: [],
          reportReady: false,
        },
        activePacket: {
          id: "pkt-cmd-01",
          type: "COMMAND",
          senderId: "commander-root",
          senderName: "ScholarX Commander",
          receiverId: "scout-eu",
          receiverName: "Europe Regional Scout",
          summary: "FIND FUNDED CS OPPORTUNITIES",
          priority: "HIGH",
          sourcePos: cPos,
          targetPos: sPos,
          progress: 1.0,
          state: "DOCKED",
        },
      };

    case "ACK_FLIGHT":
      return {
        step,
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "WAITING FOR CHILD EXECUTION",
          activeDirectiveSummary: "AWAITING CONFIRMATION RECEIPT",
        },
        scout: {
          state: "ACKNOWLEDGING",
          currentOperation: "DISPATCHING ACKNOWLEDGEMENT // INITIALIZING EXTRACTORS",
          finding: "CONFIRMED: ZERO TUITION + PAKISTAN QUOTAS TARGETED",
          progress: 38,
          sources: [],
          candidates: [],
          reportReady: false,
        },
        activePacket: {
          id: "pkt-ack-01",
          type: "ACKNOWLEDGEMENT",
          senderId: "scout-eu",
          senderName: "Europe Regional Scout",
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: "COMMAND RECEIVED // DEPLOYING EUROPE SCOUT",
          priority: "NORMAL",
          sourcePos: sPos,
          targetPos: cPos,
          progress: 0.55,
          state: "TRAVELING",
          payload: {
            ackMessage: "COMMAND RECEIVED // DEPLOYING EUROPE SCOUT",
          },
        },
      };

    case "SEARCHING":
      return {
        step,
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "CHILD WORKFLOW RUNNING DETERMINISTIC RETRIEVAL",
          activeDirectiveSummary: "MONITORING EUROPE SECTOR OPERATION",
        },
        scout: {
          state: "SEARCHING",
          currentOperation: "QUERYING EUROPEAN GOVERNMENT & UNIVERSITY REGISTRIES",
          finding: "ACTIVE RETRIEVAL IN PROGRESS",
          progress: 50,
          activeQuery:
            'DAAD OR "Stipendium Hungaricum" "Computer Science" master fully funded "Pakistan" quota 2025',
          sources: [],
          candidates: [],
          reportReady: false,
        },
        activePacket: null,
      };

    case "SOURCES_FOUND":
      return {
        step,
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "SOURCES IDENTIFIED IN TARGET REGION",
          activeDirectiveSummary: "2 AUTHORITATIVE PORTALS RESOLVED",
        },
        scout: {
          state: "WORKING",
          currentOperation: "ANALYZING VERIFIED INSTITUTIONAL SCHOLARSHIP PORTALS",
          finding: "2 OFFICIAL SOURCES DISCOVERED (HUNGARY + GERMANY)",
          progress: 65,
          activeQuery:
            'DAAD OR "Stipendium Hungaricum" "Computer Science" master fully funded "Pakistan" quota 2025',
          sources: CANONICAL_SOURCES,
          candidates: [],
          reportReady: false,
        },
        activePacket: null,
      };

    case "CANDIDATE_EMERGENCE":
      return {
        step,
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "CANDIDATES EXTRACTED FROM EUROPE SECTOR",
          activeDirectiveSummary: "2 HIGH-CONFIDENCE MATCHES DETECTED",
        },
        scout: {
          state: "EXTRACTING",
          currentOperation: "PARSING BILATERAL QUOTAS & STIPEND SCHEDULES",
          finding: "2 CANDIDATES EMERGED: 400 PAKISTANI SEATS IDENTIFIED",
          progress: 80,
          activeQuery:
            'DAAD OR "Stipendium Hungaricum" "Computer Science" master fully funded "Pakistan" quota 2025',
          sources: CANONICAL_SOURCES,
          candidates: CANONICAL_CANDIDATES,
          reportReady: false,
        },
        activePacket: null,
      };

    case "REPORT_ASSEMBLY":
      return {
        step,
        commander: {
          state: "WAITING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "AWAITING COMPRESSED SECTOR REPORT",
          activeDirectiveSummary: "FINALIZING RESEARCH PACKAGE",
        },
        scout: {
          state: "REPORTING",
          currentOperation: "COMPRESSING RESEARCH PAYLOAD FOR COMMANDER",
          finding: "REPORT READY: 2 CANDIDATES, 400 BILATERAL SEATS",
          progress: 92,
          sources: CANONICAL_SOURCES,
          candidates: CANONICAL_CANDIDATES,
          reportReady: true,
        },
        activePacket: null,
      };

    case "REPORT_FLIGHT":
      return {
        step,
        commander: {
          state: "RECEIVING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "INCOMING SECTOR DATA PACKET",
          activeDirectiveSummary: "RECEIVING COMPREHENSIVE REGIONAL REPORT",
        },
        scout: {
          state: "RETURNING",
          currentOperation: "REPORT DISPATCHED TO COMMANDER",
          finding: "REPORT DELIVERED // RETURNING TELEMETRY",
          progress: 98,
          sources: CANONICAL_SOURCES,
          candidates: CANONICAL_CANDIDATES,
          reportReady: true,
        },
        activePacket: {
          id: "pkt-rep-01",
          type: "REPORT",
          senderId: "scout-eu",
          senderName: "Europe Regional Scout",
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: "EUROPE SECTOR REPORT // 2 CANDIDATES (400 BILATERAL SEATS)",
          priority: "HIGH",
          sourcePos: sPos,
          targetPos: cPos,
          progress: 0.52,
          state: "TRAVELING",
          payload: {
            report: CANONICAL_REPORT,
          },
        },
      };

    case "COMMANDER_SYNTHESIS":
      return {
        step,
        commander: {
          state: "SYNTHESIZING",
          mission: "Discover fully funded CS opportunities for Pakistani applicants",
          currentDecision: "EVALUATE PAKISTANI ELIGIBILITY & DISPATCH GLOBAL SATELLITES",
          activeDirectiveSummary: "SECTOR REPORT INGESTED // 2 OPPORTUNITIES SYNTHESIZED",
        },
        scout: {
          state: "COMPLETE",
          currentOperation: "SECTOR MISSION ACCOMPLISHED // PERSISTED TO MEMORY",
          finding: "SYNTHESIS CONFIRMED BY COMMANDER",
          progress: 100,
          sources: CANONICAL_SOURCES,
          candidates: CANONICAL_CANDIDATES,
          reportReady: true,
        },
        activePacket: {
          id: "pkt-rep-01",
          type: "REPORT",
          senderId: "scout-eu",
          senderName: "Europe Regional Scout",
          receiverId: "commander-root",
          receiverName: "ScholarX Commander",
          summary: "EUROPE SECTOR REPORT // 2 CANDIDATES (400 BILATERAL SEATS)",
          priority: "HIGH",
          sourcePos: sPos,
          targetPos: cPos,
          progress: 1.0,
          state: "DOCKED",
          payload: {
            report: CANONICAL_REPORT,
          },
        },
      };
  }
};
