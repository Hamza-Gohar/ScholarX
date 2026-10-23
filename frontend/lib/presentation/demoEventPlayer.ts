// Deterministic Demo Event Player (§10, §11, §14, §15, §57, §58)
// Plays curated, deterministic event streams for 3 Pakistani student profiles and resilience scenarios.
// Guarantees identical logical narrative and visual sequence on every replay without cloud access.

import { ScholarXEvent, EventSeverity, Region } from "@/lib/types";
import { MasterPresentationQueue } from "./presentationQueue";
import { normalizeBackendEvent } from "./eventNormalizer";
import { searchScholarshipsForProfile, SEED_SCHOLARSHIPS, SEED_PROFILES, normalizeProfile } from "@/lib/seed-data";
import { generateDynamicRoadmap } from "@/lib/ranking/rankingStore";

export type DemoProfileId = "PROFILE_A_ICS" | "PROFILE_B_FSC" | "PROFILE_C_BS" | "PROFILE_D_ALEVEL";
export type DemoScenario = "STANDARD" | "SEARCH_FAILOVER" | "PARTIAL_FLEET";

export interface DemoProfileMeta {
  id: DemoProfileId;
  name: string;
  degree: string;
  field: string;
  marks: string;
  city: string;
  notes: string;
}

export const DEMO_PROFILES: Record<DemoProfileId, DemoProfileMeta> = {
  PROFILE_A_ICS: {
    id: "PROFILE_A_ICS",
    name: "Hamza Gohar",
    degree: "Intermediate / ICS",
    field: "Computer Science",
    marks: "93.0%",
    city: "Lahore",
    notes: "IELTS 7.0, HEC USAT 78, Bilateral Focus",
  },
  PROFILE_B_FSC: {
    id: "PROFILE_B_FSC",
    name: "Zainab Bibi",
    degree: "Intermediate / FSc Pre-Eng",
    field: "Software Engineering",
    marks: "78.4%",
    city: "Multan",
    notes: "No IELTS (Medium of Instruction Waiver), Low Budget",
  },
  PROFILE_C_BS: {
    id: "PROFILE_C_BS",
    name: "Muhammad Usman",
    degree: "Bachelor of Science (BS)",
    field: "Artificial Intelligence",
    marks: "3.82 CGPA",
    city: "Islamabad",
    notes: "IELTS 7.5, NUST Graduate, Master's Target",
  },
  PROFILE_D_ALEVEL: {
    id: "PROFILE_D_ALEVEL",
    name: "Aisha Siddiqui",
    degree: "A-Levels (Cambridge CIE)",
    field: "Computer Science",
    marks: "3A* (87.2% IBCC • 959/1100)",
    city: "Karachi",
    notes: "IELTS 8.0, KGS Graduate, IBCC Cambridge Cell Routing",
  },
};

export class DemoEventPlayer {
  private queue: MasterPresentationQueue;
  private isRunning: boolean = false;
  private isPaused: boolean = false;
  private currentEventIndex: number = 0;
  private activeTimer: NodeJS.Timeout | null = null;
  private currentProfile: DemoProfileId = "PROFILE_A_ICS";
  private currentScenario: DemoScenario = "STANDARD";
  private customProfile: any = null;
  private onStageTransition?: (stageIndex: number) => void;

  constructor(queue: MasterPresentationQueue, onStageTransition?: (stageIndex: number) => void) {
    this.queue = queue;
    this.onStageTransition = onStageTransition;
  }

  public setStageTransitionHandler(handler: (stageIndex: number) => void) {
    this.onStageTransition = handler;
  }

  public getProfile(): DemoProfileId {
    return this.currentProfile;
  }

  public getScenario(): DemoScenario {
    return this.currentScenario;
  }

  public isPlaying(): boolean {
    return this.isRunning && !this.isPaused;
  }

  public isDemoActive(): boolean {
    return this.isRunning;
  }

  public start(profile: DemoProfileId = "PROFILE_A_ICS", scenario: DemoScenario = "STANDARD", customProfile?: any) {
    this.stop();
    this.currentProfile = profile;
    this.currentScenario = scenario;
    this.customProfile = customProfile || null;
    this.isRunning = true;
    this.isPaused = false;
    this.currentEventIndex = 0;
    this.playNextEvent();
  }

  public pause() {
    if (this.isRunning && !this.isPaused) {
      this.isPaused = true;
      if (this.activeTimer) {
        clearTimeout(this.activeTimer);
        this.activeTimer = null;
      }
      this.queue.pause();
    }
  }

  public resume() {
    if (this.isRunning && this.isPaused) {
      this.isPaused = false;
      this.queue.resume();
      this.playNextEvent();
    }
  }

  public restart() {
    const prof = this.currentProfile;
    const scen = this.currentScenario;
    const custom = this.customProfile;
    this.stop();
    this.start(prof, scen, custom);
  }

  public stop() {
    this.isRunning = false;
    this.isPaused = false;
    this.currentEventIndex = 0;
    if (this.activeTimer) {
      clearTimeout(this.activeTimer);
      this.activeTimer = null;
    }
  }

  private buildCuratedEventSequence(): ScholarXEvent[] {
    const profileMeta = DEMO_PROFILES[this.currentProfile] || DEMO_PROFILES.PROFILE_A_ICS;
    const sessionId = `demo-${this.currentProfile.toLowerCase()}-${Date.now().toString(36)}`;
    const events: ScholarXEvent[] = [];

    // Resolve profile object for database query
    let targetProfileObj: any;
    if (this.customProfile) {
      targetProfileObj = normalizeProfile(this.customProfile);
    } else if (this.currentProfile === "PROFILE_A_ICS") {
      targetProfileObj = SEED_PROFILES[0];
    } else if (this.currentProfile === "PROFILE_B_FSC") {
      targetProfileObj = SEED_PROFILES[1];
    } else if (this.currentProfile === "PROFILE_C_BS") {
      targetProfileObj = SEED_PROFILES[2];
    } else if (this.currentProfile === "PROFILE_D_ALEVEL") {
      targetProfileObj = SEED_PROFILES[5] || SEED_PROFILES[0];
    } else {
      targetProfileObj = SEED_PROFILES[0];
    }

    // Resolve profile regions
    const rawTargetRegions =
      targetProfileObj.preferences?.preferred_regions ||
      targetProfileObj.preferences?.preferredRegions ||
      targetProfileObj.personal?.target_regions ||
      targetProfileObj.personal?.targetRegions;
    const activeRegions: string[] = (Array.isArray(rawTargetRegions) ? rawTargetRegions : [])
      .map((r: string) => String(r).toLowerCase().trim())
      .filter(Boolean);

    // Query institutional database (311 verified records) for this active student profile
    const matchedScholarships = searchScholarshipsForProfile(targetProfileObj, 10);
    const allowedSeed = activeRegions.length > 0
      ? SEED_SCHOLARSHIPS.filter((s) => {
          const scR = s.region.toLowerCase().trim();
          return activeRegions.some((ar) => ar === scR || (ar === "europe" && scR.includes("europe")) || (ar === "asia" && scR.includes("asia")));
        })
      : SEED_SCHOLARSHIPS;

    const topCandidates = matchedScholarships.length >= 4 
      ? matchedScholarships.slice(0, 5) 
      : [...matchedScholarships, ...allowedSeed.filter(s => !matchedScholarships.some(m => m.scholarship_id === s.scholarship_id)).slice(0, 5 - matchedScholarships.length)];

    const cand1 = topCandidates[0] || allowedSeed[0] || SEED_SCHOLARSHIPS[0];
    const cand2 = topCandidates[1] || cand1;
    const cand3 = topCandidates[2] || cand1;
    const cand4 = topCandidates[3] || cand2;

    const studentName = targetProfileObj.personal?.name || profileMeta.name;
    const studentDegree = targetProfileObj.academic?.degree_level || profileMeta.degree;
    const studentField = targetProfileObj.academic?.field_of_study || profileMeta.field;
    const studentMarks = targetProfileObj.academic?.percentage 
      ? `${targetProfileObj.academic.percentage}%` 
      : (targetProfileObj.academic?.gpa_4_scale ? `${targetProfileObj.academic.gpa_4_scale} CGPA` : profileMeta.marks);
    const studentCity = targetProfileObj.personal?.city || profileMeta.city;
    const studentNotes = targetProfileObj.language?.test_type === "NONE"
      ? "MOI Waiver Eligible • Low Budget Optimization"
      : (profileMeta.notes || "Live Profile-Database Match");

    const makeEvt = (
      type: string,
      agentId: string,
      displayName: string,
      component: "AGENT" | "WORKFLOW",
      phase: string,
      payload: any,
      severity: EventSeverity = "INFO"
    ): ScholarXEvent => ({
      schema_version: 1,
      event_id: `evt-demo-${events.length + 1}`,
      session_id: sessionId,
      timestamp: new Date().toISOString(),
      event_type: type as any,
      agent_id: agentId,
      agent_display_name: displayName,
      component_type: component,
      phase,
      payload,
      severity,
    });

    // Stage 1: Mission Initiation
    events.push(
      makeEvt(
        "MISSION_INITIATED",
        "orchestrator",
        "Mission Commander",
        "AGENT",
        "ORCHESTRATION",
        {
          student_name: studentName,
          degree: studentDegree,
          field: studentField,
          marks: studentMarks,
          city: studentCity,
          notes: studentNotes,
        },
        "SUCCESS"
      )
    );

    // Stage 2: Target Fleet Deployment (Only user-selected continental sectors)
    const allRegions: Region[] = ["Europe", "Asia", "Americas", "MENA", "Oceania"];
    const targetDeployRegions: Region[] = activeRegions.length > 0
      ? (allRegions.filter((r) => activeRegions.includes(r.toLowerCase())) as Region[])
      : allRegions;
    const finalRegions = targetDeployRegions.length > 0 ? targetDeployRegions : allRegions;

    for (const r of finalRegions) {
      events.push(
        makeEvt(
          "SCOUT_DEPLOYED",
          `${r.toLowerCase()}_scout`,
          `${r} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          {
            region: r,
            active_queries_count: 3,
            message: `Scout deployed to ${r} sector with Pakistan-focused query matrix.`,
          }
        )
      );
    }

    // Stage 3: Fleet Searches & Scraping
    // Check for Resilience Scenario 1: Search Failover
    if (this.currentScenario === "SEARCH_FAILOVER") {
      events.push(
        makeEvt(
          "SEARCH_QUERY_EXECUTED",
          `${cand1.region.toLowerCase()}_scout`,
          `${cand1.region} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          { query: `${cand1.name} Pakistan HEC criteria`, region: cand1.region }
        )
      );
      events.push(
        makeEvt(
          "PRIMARY_SEARCH_UNAVAILABLE",
          `${cand1.region.toLowerCase()}_scout`,
          `${cand1.region} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          {
            provider: "Tavily",
            region: cand1.region,
            notice: "Primary search rate limit reached. Transitioning to fallback intelligence.",
          },
          "WARNING"
        )
      );
      events.push(
        makeEvt(
          "FALLBACK_SEARCH_ACTIVE",
          `${cand1.region.toLowerCase()}_scout`,
          `${cand1.region} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          {
            fallback_source: "VERIFIED_REGISTRY_CACHE",
            region: cand1.region,
            tool: "CANONICAL_DATABASE",
          },
          "INFO"
        )
      );
      events.push(
        makeEvt(
          "RESEARCH_RESUMED",
          `${cand1.region.toLowerCase()}_scout`,
          `${cand1.region} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          { region: cand1.region, status: "RESEARCH_RESUMED_VIA_FALLBACK" },
          "INFO"
        )
      );
    } else {
      events.push(
        makeEvt(
          "SEARCH_QUERY_EXECUTED",
          `${cand1.region.toLowerCase()}_scout`,
          `${cand1.region} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          { query: `${cand1.name} Pakistan requirements`, region: cand1.region }
        )
      );
    }

    events.push(
      makeEvt(
        "SEARCH_QUERY_EXECUTED",
        `${cand2.region.toLowerCase()}_scout`,
        `${cand2.region} Scout`,
        "WORKFLOW",
        "DISCOVERY",
        { query: `${cand2.name} bilateral Pakistan HEC`, region: cand2.region }
      )
    );

    events.push(
      makeEvt(
        "SEARCH_QUERY_EXECUTED",
        `${cand3.region.toLowerCase()}_scout`,
        `${cand3.region} Scout`,
        "WORKFLOW",
        "DISCOVERY",
        { query: `${cand3.name} eligible fields criteria`, region: cand3.region }
      )
    );

    // Sources found
    events.push(
      makeEvt(
        "SOURCE_FOUND",
        `${cand1.region.toLowerCase()}_scout`,
        `${cand1.region} Scout`,
        "WORKFLOW",
        "DISCOVERY",
        { 
          url: cand1.source_url || cand1.portal_url || "https://scholarships.gov.pk", 
          title: cand1.host_institution || cand1.name, 
          region: cand1.region 
        }
      )
    );
    events.push(
      makeEvt(
        "SOURCE_FOUND",
        `${cand2.region.toLowerCase()}_scout`,
        `${cand2.region} Scout`,
        "WORKFLOW",
        "DISCOVERY",
        { 
          url: cand2.source_url || cand2.portal_url || "https://scholarships.gov.pk", 
          title: cand2.host_institution || cand2.name, 
          region: cand2.region 
        }
      )
    );

    // Check for Resilience Scenario 2: Partial Fleet
    if (this.currentScenario === "PARTIAL_FLEET") {
      events.push(
        makeEvt(
          "SCOUT_FAILED",
          "americas_scout",
          "Americas Scout",
          "WORKFLOW",
          "DISCOVERY",
          {
            region: "Americas",
            error: "Connection timeout to regional portal",
            status: "UNAVAILABLE",
            notice: "Americas scout isolated. Remaining 4 continental scouts continuing.",
          },
          "WARNING"
        )
      );
    }

    // Stage 4: Candidates Extracted from Profile Matching
    topCandidates.slice(0, 4).forEach((c) => {
      const anyC = c as any;
      events.push(
        makeEvt(
          "CANDIDATE_EXTRACTED",
          `${c.region.toLowerCase()}_scout`,
          `${c.region} Scout`,
          "WORKFLOW",
          "DISCOVERY",
          {
            scholarship_id: c.scholarship_id,
            name: c.name,
            host_country: c.host_country_name,
            funding_type: anyC.funding_type || anyC.funding?.funding_type || "FULL",
            region: c.region,
            degree_level: (c.eligibility?.degree_levels || []).join(", ") || studentDegree,
            field_of_study: studentField,
            source_url: c.source_url || c.portal_url || "https://scholarships.gov.pk",
            quota_seats: anyC.pakistan_requirements?.pakistan_quota_seats || anyC.pakistan_requirements?.bilateral_quota_seats,
            hec_managed: Boolean(c.pakistan_requirements?.hec_attestation_required || c.pakistan_requirements?.hec_managed),
          },
          "SUCCESS"
        )
      );
    });

    events.push(
      makeEvt(
        "SCOUT_COMPLETE",
        `${cand1.region.toLowerCase()}_scout`,
        `${cand1.region} Scout`,
        "WORKFLOW",
        "DISCOVERY",
        { region: cand1.region, total_discovered: 2 },
        "SUCCESS"
      )
    );

    events.push(
      makeEvt(
        "SCOUT_COMPLETE",
        `${cand2.region.toLowerCase()}_scout`,
        `${cand2.region} Scout`,
        "WORKFLOW",
        "DISCOVERY",
        { region: cand2.region, total_discovered: 1 },
        "SUCCESS"
      )
    );

    if (this.currentScenario === "PARTIAL_FLEET") {
      events.push(
        makeEvt(
          "PARTIAL_DISCOVERY",
          "discovery_commander",
          "Discovery Commander",
          "AGENT",
          "DISCOVERY",
          {
            total_candidates_found: 3,
            completed_regions: ["Europe", "Asia", "MENA", "Oceania"],
            failed_regions: ["Americas"],
            is_partial: true,
            notice: "Partial discovery completed with 4/5 continental regions active.",
          },
          "WARNING"
        )
      );
    } else {
      events.push(
        makeEvt(
          "DISCOVERY_AGGREGATION_COMPLETE",
          "discovery_commander",
          "Discovery Commander",
          "AGENT",
          "DISCOVERY",
          {
            total_candidates_found: topCandidates.length,
            regions_covered: ["Europe", "Asia", "Americas", "MENA", "Oceania"],
            is_partial: false,
          },
          "SUCCESS"
        )
      );
    }

    // Stage 5: Specialist Investigation
    events.push(
      makeEvt(
        "ELIGIBILITY_CHECK_STARTED",
        "eligibility",
        "Eligibility Investigator",
        "WORKFLOW",
        "ELIGIBILITY",
        {
          scholarship_id: cand1.scholarship_id,
          candidate: cand1.name,
          evaluations: "15 Pakistan Dimensions",
        }
      )
    );

    const cand1Any = cand1 as any;
    const cand1Seats = cand1Any.pakistan_requirements?.pakistan_quota_seats || cand1Any.pakistan_requirements?.bilateral_quota_seats;

    events.push(
      makeEvt(
        "DIMENSION_EVALUATED",
        "eligibility",
        "Eligibility Investigator",
        "WORKFLOW",
        "ELIGIBILITY",
        {
          dimension: cand1Seats ? "Pakistan Bilateral Quota" : "Degree & Academic Criteria",
          verdict: "PASS",
          seats: cand1Seats || undefined,
          notes: cand1Seats 
            ? `Dedicated ${cand1Seats} seats reserved for Pakistani scholars.`
            : `Verified minimum GPA and degree eligibility requirements met for ${studentName}.`,
        }
      )
    );

    events.push(
      makeEvt(
        "ELIGIBILITY_COMPLETE",
        "eligibility",
        "Eligibility Investigator",
        "WORKFLOW",
        "ELIGIBILITY",
        {
          scholarship_id: cand1.scholarship_id,
          total_passed: 14,
          warnings: 1,
          fails: 0,
        },
        "SUCCESS"
      )
    );

    // Cost Breakdown
    events.push(
      makeEvt(
        "COST_ANALYSIS_STARTED",
        "cost_analyzer",
        "True Cost Analyzer",
        "WORKFLOW",
        "COST",
        { scholarship_id: cand1.scholarship_id }
      )
    );

    events.push(
      makeEvt(
        "PKR_BREAKDOWN_CALCULATED",
        "cost_analyzer",
        "True Cost Analyzer",
        "WORKFLOW",
        "COST",
        {
          tuition_covered_pkr: cand1Any.funding_type === "FULL" || cand1Any.funding?.funding_type === "FULL" ? 2800000 : 1200000,
          accommodation_covered_pkr: 960000,
          stipend_monthly_pkr: cand1Any.funding?.monthly_stipend_pkr_approx || 45000,
          out_of_pocket_initial_pkr: cand1Any.costs?.out_of_pocket_initial_pkr || 220000,
          airfare_deficit_flag: cand1Any.funding?.travel_airfare === "NONE",
        }
      )
    );

    events.push(
      makeEvt(
        "DEADLINE_EVALUATED",
        "deadline_analyzer",
        "Deadline Intelligence",
        "WORKFLOW",
        "DEADLINE",
        {
          deadline_date: cand1.application_deadline || cand1Any.deadlines?.application_deadline || "2026-12-31",
          days_remaining: 68,
          critical_prep_days: 28,
          slack_days: 40,
          feasibility: "FEASIBLE",
        }
      )
    );

    // Stage 6: Skeptic Challenge & Rebuttal
    events.push(
      makeEvt(
        "SKEPTIC_CHALLENGE_RAISED",
        "skeptic",
        "Adversarial Skeptic",
        "AGENT",
        "VERIFICATION",
        {
          challenge_type: cand1Any.funding?.travel_airfare === "NONE" ? "AIRFARE_DEFICIT" : "DOCUMENT_VERIFICATION",
          severity: "MEDIUM",
          summary: `${cand1.name} evaluation: Verify initial deposit / travel buffer and attested academic transcripts.`,
        },
        "WARNING"
      )
    );

    events.push(
      makeEvt(
        "SKEPTIC_DEBATE_CLASH",
        "skeptic",
        "Adversarial Skeptic",
        "AGENT",
        "VERIFICATION",
        {
          topic: "HEC Attestation & Quota Allocation",
          rebuttal: `Applicant credentials (${studentMarks}) fulfill standard institutional thresholds for ${cand1.host_country_name}.`,
          resolution: "Rebuttal accepted. Academic compatibility and visa lead times verified.",
        }
      )
    );

    events.push(
      makeEvt(
        "SKEPTIC_COMPLETE",
        "skeptic",
        "Adversarial Skeptic",
        "AGENT",
        "VERIFICATION",
        { status: "RESOLVED_WITH_QUALIFICATIONS" },
        "SUCCESS"
      )
    );

    // Stage 7: Ranking Engine
    events.push(
      makeEvt(
        "SYNTHESIS_COMPLETE",
        "synthesis",
        "Multi-Stream Synthesis",
        "WORKFLOW",
        "SYNTHESIS",
        { target: cand1.name, traces_resolved: 6 }
      )
    );

    const studentGpaNum = Number(
      targetProfileObj.academic?.percentage ||
      targetProfileObj.academic?.gpa_percentage ||
      80
    );
    const hasIeltsBool = Boolean(
      targetProfileObj.language?.has_english_test ||
      (targetProfileObj.language?.english_proficiency_test &&
        !/none|not available/i.test(targetProfileObj.language.english_proficiency_test))
    );

    const rankedResultsPayload = topCandidates.slice(0, 4).map((c, i) => {
      const anyCandidate = c as any;
      const seats =
        anyCandidate.pakistan_requirements?.pakistan_quota_seats ||
        anyCandidate.pakistan_requirements?.bilateral_quota_seats;
      const hasBilateral = Boolean(seats || anyCandidate.pakistan_requirements?.hec_managed);

      const fEligibility = Math.min(98, Math.max(65, Math.round(studentGpaNum * 0.95 + 10 - i * 2)));
      const isFull = anyCandidate.funding_type === "FULL" || anyCandidate.funding?.funding_type === "FULL";
      const fFunding = isFull ? Math.max(75, 96 - i * 2) : 78;
      const fBilateral = hasBilateral ? 96 : 74;
      const fAcademicFit = Math.min(96, Math.max(70, Math.round(studentGpaNum * 0.92 + 12 - i * 3)));
      const fDocReadiness = hasIeltsBool ? 90 : 76;
      const fDeadline = Math.max(68, 88 - i * 2);
      const fVerification = 95;
      const fCompetition = hasBilateral ? 78 : 70;

      const totalCalcScore = Math.round(
        (0.25 * fEligibility +
          0.25 * fFunding +
          0.10 * fBilateral +
          0.10 * fAcademicFit +
          0.10 * fDocReadiness +
          0.10 * fDeadline +
          0.05 * fVerification +
          0.05 * fCompetition) * 10
      ) / 10;

      const matchDeg = (c.eligibility?.degree_levels || []).find((d: string) => d.toLowerCase().includes(studentDegree.toLowerCase()));
      const finalDegree = matchDeg || studentDegree || (c.eligibility?.degree_levels || [])[0] || "Degree Programme";

      return {
        scholarship_id: c.scholarship_id,
        name: c.name,
        scholarship_name: c.name,
        host_country_name: c.host_country_name,
        host_country: c.host_country_name,
        region: c.region,
        degree_level: finalDegree,
        field_of_study: studentField,
        overall_match_score: totalCalcScore,
        portal_url: c.source_url || c.portal_url || "https://scholarships.gov.pk",
        official_portal_url: c.source_url || c.portal_url || "https://scholarships.gov.pk",
        hec_managed: Boolean(c.pakistan_requirements?.hec_attestation_required || c.pakistan_requirements?.hec_managed),
        factors: {
          eligibility: fEligibility,
          funding: fFunding,
          bilateral_bonus: fBilateral,
          academic_fit: fAcademicFit,
          doc_readiness: fDocReadiness,
          deadline: fDeadline,
          verification: fVerification,
          competition: fCompetition,
        },
        rank: i + 1,
      };
    });

    events.push(
      makeEvt(
        "RANKING_CALCULATED",
        "ranking_engine",
        "Ranking Engine",
        "WORKFLOW",
        "RANKING",
        {
          top_scholarship: cand1.name,
          top_score: 92.4,
          rank_1: `${cand1.name} (92.4)`,
          rank_2: `${cand2.name} (88.6)`,
          rank_3: `${cand3.name} (84.8)`,
          rank_4: `${cand4.name} (81.0)`,
          primary_selected: cand1.scholarship_id,
          ranked_results: rankedResultsPayload,
        },
        "SUCCESS"
      )
    );

    // Stage 8: Roadmap Generation
    const dynamicPhases = generateDynamicRoadmap(targetProfileObj, cand1);
    const milestonesPayload = dynamicPhases.map((phase) => ({
      title: phase.title,
      target_timeline_days: phase.timelineDaysRange,
      total_phase_cost_pkr: phase.totalCostPkr,
      guidance_notes: phase.criticalAdvisory,
      actions: phase.actions.map((act) => ({
        action_id: act.id,
        description: act.title,
        assigned_office: act.assignedOffice || act.purpose,
        estimated_days: act.timingDays,
        estimated_cost_pkr: act.estimatedCostPkr,
        is_blocking: act.isBlocking,
      })),
    }));

    events.push(
      makeEvt(
        "ROADMAP_GENERATED",
        "advisor",
        "Final Advisor",
        "AGENT",
        "ADVISOR",
        {
          target_scholarship: cand1.name,
          phases_count: dynamicPhases.length,
          milestones: milestonesPayload,
          pakistani_offices: Array.from(
            new Set(
              dynamicPhases
                .flatMap((p) => p.actions.map((a) => a.assignedOffice))
                .filter((off): off is string => Boolean(off))
            )
          ),
          action_items_total: dynamicPhases.reduce((acc, p) => acc + p.actions.length, 0),
        },
        "SUCCESS"
      )
    );

    // Stage 12: Mission Complete
    events.push(
      makeEvt(
        "MISSION_COMPLETE",
        "orchestrator",
        "Mission Commander",
        "AGENT",
        "ORCHESTRATION",
        {
          status: "SUCCESS",
          selected_opportunity: cand1.name,
          web_dossier_ready: true,
          pdf_ready: true,
          profile_id: this.currentProfile,
        },
        "SUCCESS"
      )
    );

    return events;
  }

  private playNextEvent() {
    if (!this.isRunning || this.isPaused) return;

    const eventList = this.buildCuratedEventSequence();
    if (this.currentEventIndex >= eventList.length) {
      this.isRunning = false;
      return;
    }

    const rawEvent = eventList[this.currentEventIndex];
    this.currentEventIndex += 1;

    // Enqueue normalized presentation event
    const normalized = normalizeBackendEvent(rawEvent);
    this.queue.enqueue(normalized);

    // Stage tracking callback
    const stageMap: Record<string, number> = {
      MISSION_INITIATED: 1,
      SCOUT_DEPLOYED: 2,
      SEARCH_QUERY_EXECUTED: 3,
      CANDIDATE_EXTRACTED: 4,
      ELIGIBILITY_CHECK_STARTED: 5,
      SKEPTIC_CHALLENGE_RAISED: 6,
      RANKING_CALCULATED: 7,
      ROADMAP_GENERATED: 8,
      MISSION_COMPLETE: 12,
    };
    if (stageMap[rawEvent.event_type] !== undefined) {
      this.onStageTransition?.(stageMap[rawEvent.event_type]);
    }

    // Schedule next event (pacing: scaled for ~17s demo mode sequence)
    const delay = rawEvent.event_type === "MISSION_COMPLETE" ? 900 : 580;
    this.activeTimer = setTimeout(() => {
      this.playNextEvent();
    }, delay);
  }
}
