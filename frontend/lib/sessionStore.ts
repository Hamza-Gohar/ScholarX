// In-memory / Global Session Store for Next.js API Routes & Serverless Fallback
import { searchScholarshipsForProfile, normalizeProfile, SEED_PROFILES } from "./seed-data";
import { generateDynamicRoadmap } from "./ranking/rankingStore";

interface StoredSession {
  sessionId: string;
  profile: any;
  discovered: any[];
  roadmap: any;
  status: string;
  createdAt: number;
}

declare global {
  var __scholarx_sessions__: Map<string, StoredSession> | undefined;
}

const sessionsMap: Map<string, StoredSession> =
  globalThis.__scholarx_sessions__ || (globalThis.__scholarx_sessions__ = new Map());

export function saveSessionToStore(sessionId: string, data: Partial<StoredSession>) {
  const existing = sessionsMap.get(sessionId) || {
    sessionId,
    profile: null,
    discovered: [],
    roadmap: null,
    status: "COMPLETE",
    createdAt: Date.now(),
  };

  const updated: StoredSession = {
    ...existing,
    ...data,
    sessionId,
  };
  sessionsMap.set(sessionId, updated);
  return updated;
}

export function saveProfileToStore(sessionId: string, profile: any) {
  return saveSessionToStore(sessionId, { profile });
}

export function getSessionFromStore(sessionId: string) {
  return sessionsMap.get(sessionId) || null;
}

export function buildSyntheticSession(sessionId: string, customProfile?: any) {
  const profile = customProfile ? normalizeProfile(customProfile) : SEED_PROFILES[0];
  const matched = searchScholarshipsForProfile(profile, 10);
  const topOpp = matched[0];
  const phases = generateDynamicRoadmap(profile, topOpp);

  const milestones = phases.map((phase) => ({
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

  const sessionObj = {
    session: {
      session_id: sessionId,
      status: "COMPLETED",
      student_profile: profile,
      discovered_scholarships: matched,
      mission_parameters: {
        roadmap: {
          milestones,
          phases_count: phases.length,
          total_budget_pkr: phases.reduce((acc, p) => acc + p.totalCostPkr, 0),
        },
      },
    },
    profile,
  };

  saveSessionToStore(sessionId, {
    profile,
    discovered: matched,
    roadmap: sessionObj.session.mission_parameters.roadmap,
    status: "COMPLETED",
  });

  return sessionObj;
}
