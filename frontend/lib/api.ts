import { ScholarXEvent, StudentProfile, Scholarship } from "./types";
import { SEED_SCHOLARSHIPS, searchScholarshipsForProfile } from "./seed-data";

const API_BASE = ""; // Relative path leveraging Next.js rewrites to localhost:8000

/**
 * Fast health check for FastAPI backend on port 8000.
 * Uses AbortSignal timeout to never freeze the UI.
 */
export async function checkBackendHealth(): Promise<{ online: boolean; data: any | null }> {
  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${API_BASE}/api/health`, {
      method: "GET",
      cache: "no-store",
      signal: controller.signal,
    });
    clearTimeout(timer);

    if (!res.ok) return { online: false, data: null };
    const data = await res.json();
    return { online: data?.status === "HEALTHY" || data?.status === "ONLINE", data };
  } catch {
    return { online: false, data: null };
  }
}

export async function uploadDocument(
  sessionId: string,
  file: File
): Promise<{ profile: StudentProfile; doc_type: string }> {
  const formData = new FormData();
  formData.append("session_id", sessionId);
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/api/profile/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error(`Upload failed with status ${res.status}`);
  }

  return await res.json();
}

export async function sendCounselorChat(
  sessionId: string,
  message: string
): Promise<{ reply: string; profile: StudentProfile }> {
  const res = await fetch(`${API_BASE}/api/profile/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, message }),
  });

  if (!res.ok) {
    throw new Error(`Counselor chat failed with status ${res.status}`);
  }

  return await res.json();
}

/**
 * Launch autonomous discovery mission with auto-retry and zero-crash return value.
 * Never throws unhandled runtime exceptions into Next.js dev error overlays.
 */
export async function launchDiscoveryMission(
  sessionId: string,
  profile?: any
): Promise<{ ok: boolean; session_id?: string; status?: string; message?: string; error?: string }> {
  const payload: any = { session_id: sessionId };
  if (profile) {
    payload.profile = profile;
  }

  // Auto-retry up to 2 times with 600ms backoff if backend is momentarily starting
  const maxAttempts = 2;
  let lastError = "Unable to connect to backend";

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 8000);

      const res = await fetch(`${API_BASE}/api/discover`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        signal: controller.signal,
      });
      clearTimeout(timer);

      if (res.ok) {
        const data = await res.json();
        return { ok: true, ...data };
      }

      // Backend returned HTTP error status
      const errText = await res.text().catch(() => "");
      lastError = `Server returned status ${res.status}: ${errText.slice(0, 120)}`;
    } catch (err: any) {
      lastError = err?.message || "Backend unreachable on port 8000";
    }

    if (attempt < maxAttempts) {
      await new Promise((r) => setTimeout(r, 600));
    }
  }

  return {
    ok: false,
    session_id: sessionId,
    status: "OFFLINE_FALLBACK",
    error: lastError,
  };
}

const KNOWN_SSE_EVENTS = [
  "scholarx",
  "MISSION_INITIATED",
  "PHASE_TRANSITION",
  "AGENT_SPAWNED",
  "AGENT_COMPLETED",
  "PIPELINE_ERROR",
  "PIPELINE_RECOVERED",
  "MISSION_COMPLETE",
  "DOCUMENT_UPLOADED",
  "DOCUMENT_PARSE_STARTED",
  "DOCUMENT_PARSE_FAILED",
  "DOCUMENT_PARSED",
  "EXTRACTION_FIELD_FOUND",
  "EXTRACTION_LOW_CONFIDENCE",
  "DOCUMENT_MISSING_REQUIRED",
  "DOCUMENT_MISSING_OPTIONAL",
  "USER_INPUT_REQUESTED",
  "USER_INPUT_RECEIVED",
  "CLARIFICATION_REQUESTED",
  "DOCUMENT_REUPLOAD_REQUESTED",
  "PROFILE_UPDATED",
  "PROFILE_COMPLETE",
  "PROFILE_VALIDATION_ERROR",
  "PROFILE_SAVED_TO_SESSION",
  "SCOUT_DEPLOYED",
  "SEARCH_QUERY_EXECUTED",
  "API_KEY_ROTATED",
  "API_KEY_EXHAUSTED",
  "FALLBACK_TOOL_USED",
  "PRIMARY_SEARCH_UNAVAILABLE",
  "FALLBACK_SEARCH_ACTIVE",
  "RESEARCH_RESUMED",
  "SCOUT_FAILED",
  "SCOUT_RECOVERING",
  "PARTIAL_DISCOVERY",
  "SOURCE_FOUND",
  "PAGE_SCRAPED",
  "CANDIDATE_EXTRACTED",
  "SCOUT_PROGRESS",
  "SCOUT_COMPLETE",
  "DISCOVERY_AGGREGATION_COMPLETE",
  "DUPLICATE_DETECTED",
  "PREVIOUS_RESEARCH_LOADED",
  "ELIGIBILITY_CHECK_STARTED",
  "DIMENSION_EVALUATED",
  "ELIGIBILITY_WARNING",
  "ELIGIBILITY_PASS",
  "CRITICAL_BARRIER_DETECTED",
  "ELIGIBILITY_COMPLETE",
  "COST_ANALYSIS_STARTED",
  "PKR_BREAKDOWN_CALCULATED",
  "COST_ANALYSIS_COMPLETE",
  "DEADLINE_EVALUATED",
  "DEADLINE_COMPLETE",
  "DOCUMENT_CHECK_STARTED",
  "DOCUMENT_VERIFIED",
  "DOCUMENT_CHECK_COMPLETE",
  "VERIFICATION_INCOMPLETE",
  "SKEPTIC_CHALLENGE_RAISED",
  "SKEPTIC_DEBATE_CLASH",
  "SKEPTIC_COMPLETE",
  "SYNTHESIS_STARTED",
  "SYNTHESIS_COMPLETE",
  "SPECIALIST_FAILED",
  "RANKING_CALCULATED",
  "ROADMAP_GENERATED",
  "ARTIFACT_FAILED",
  "SESSION_CREATED",
  "SESSION_LOADED",
  "SESSION_SAVED",
  "CACHE_HIT",
  "CACHE_MISS",
] as const;

export function subscribeToEventStream(
  sessionId: string,
  onEvent: (evt: ScholarXEvent) => void,
  onError?: (err: any) => void
): () => void {
  const eventSource = new EventSource(`${API_BASE}/api/stream?session_id=${encodeURIComponent(sessionId)}`);

  const handleMessage = (e: MessageEvent) => {
    try {
      if (!e.data || !e.data.trim()) return;
       const data = JSON.parse(e.data);
       if (data?.event_id && seenEventIds.has(data.event_id)) return;
       if (data?.event_id) seenEventIds.add(data.event_id);
       onEvent(data);
    } catch (err) {
      console.warn("Error parsing SSE event data:", err);
    }
  };

  const seenEventIds = new Set<string>();

  eventSource.onmessage = handleMessage;
  KNOWN_SSE_EVENTS.forEach((eventType) => {
    eventSource.addEventListener(eventType, handleMessage);
  });

  eventSource.onerror = (err) => {
    if (onError) onError(err);
    eventSource.close();
  };

  return () => {
    KNOWN_SSE_EVENTS.forEach((eventType) => {
      eventSource.removeEventListener(eventType, handleMessage);
    });
    eventSource.close();
  };
}

export async function listSessions(limit = 50): Promise<{ sessions: any[] }> {
  try {
    const res = await fetch(`${API_BASE}/api/sessions?limit=${limit}`);
    if (!res.ok) return { sessions: [] };
    return await res.json();
  } catch {
    return { sessions: [] };
  }
}

export async function getSessionDetail(sessionId: string, profile?: any): Promise<any> {
  try {
    let url = `${API_BASE}/api/sessions/${encodeURIComponent(sessionId)}`;
    const targetProf = profile || (typeof window !== "undefined" ? (() => {
      try {
        const raw = localStorage.getItem(`scholarx_profile_${sessionId}`) || localStorage.getItem("scholarx_last_profile");
        return raw ? JSON.parse(raw) : null;
      } catch { return null; }
    })() : null);

    if (targetProf) {
      const deg = targetProf.preferences?.target_degree_level || targetProf.academic?.degree_level;
      const fld = targetProf.preferences?.target_fields?.[0] || targetProf.academic?.field_of_study;
      const nm = targetProf.personal?.name;
      const gpa = targetProf.academic?.percentage || targetProf.academic?.gpa_percentage;
      const rawRegs =
        targetProf.preferences?.preferred_regions ||
        targetProf.preferences?.preferredRegions ||
        targetProf.personal?.target_regions ||
        targetProf.personal?.targetRegions;
      const params = new URLSearchParams();
      if (deg) params.set("degree", deg);
      if (fld) params.set("field", fld);
      if (nm) params.set("name", nm);
      if (gpa) params.set("gpa", String(gpa));
      if (Array.isArray(rawRegs) && rawRegs.length > 0) {
        params.set("regions", rawRegs.join(","));
      }
      const qs = params.toString();
      if (qs) url += `?${qs}`;
    }

    const res = await fetch(url);
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

export async function deleteSession(sessionId: string): Promise<{ ok: boolean }> {
  try {
    const res = await fetch(`${API_BASE}/api/sessions/${sessionId}`, {
      method: "DELETE",
    });
    return { ok: res.ok };
  } catch {
    return { ok: false };
  }
}

export async function saveStudentProfile(sessionId: string, profile: any): Promise<{ ok: boolean; data?: any }> {
  try {
    const res = await fetch(`${API_BASE}/api/profile/${sessionId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profile),
    });
    if (!res.ok) return { ok: false };
    const data = await res.json();
    return { ok: true, data };
  } catch {
    return { ok: false };
  }
}

export async function getStudentProfile(sessionId: string): Promise<any> {
  try {
    const res = await fetch(`${API_BASE}/api/profile/${sessionId}`);
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

export async function getDiscoveryStatus(sessionId: string): Promise<any> {
  try {
    const res = await fetch(`${API_BASE}/api/discover/${sessionId}/status`);
    if (!res.ok) return { status: "IDLE", phase: "NONE" };
    return await res.json();
  } catch {
    return { status: "IDLE", phase: "NONE" };
  }
}

export interface FetchScholarshipsOptions {
  region?: string;
  country?: string;
  search?: string;
  degree_level?: string;
  funding_type?: string;
  limit?: number;
  offset?: number;
}

/**
 * Query scholarships directly from backend database cache with filtering.
 * Gracefully falls back to local pre-compiled datasets if backend is offline.
 */
export async function fetchScholarships(
  options: FetchScholarshipsOptions = {}
): Promise<{ scholarships: Scholarship[]; total: number; source: "database" | "local_fallback" }> {
  const { region, country, search, degree_level, funding_type, limit = 50, offset = 0 } = options;
  const params = new URLSearchParams();
  if (region) params.append("region", region);
  if (country) params.append("country", country);
  if (search) params.append("search", search);
  if (degree_level) params.append("degree_level", degree_level);
  if (funding_type) params.append("funding_type", funding_type);
  params.append("limit", String(limit));
  params.append("offset", String(offset));

  try {
    const res = await fetch(`${API_BASE}/api/scholarships?${params.toString()}`, {
      cache: "no-store",
    });
    if (res.ok) {
      const data = await res.json();
      return {
        scholarships: data.scholarships || [],
        total: data.total || 0,
        source: "database",
      };
    }
  } catch (err) {
    console.warn("Backend scholarship query failed, using local seed fallback:", err);
  }

  // Fallback to local SEED_SCHOLARSHIPS
  let filtered = [...SEED_SCHOLARSHIPS];
  if (region) filtered = filtered.filter((s) => s.region.toLowerCase() === region.toLowerCase());
  if (country) {
    const cLower = country.toLowerCase();
    filtered = filtered.filter(
      (s) => s.host_country.toLowerCase() === cLower || s.host_country_name.toLowerCase().includes(cLower)
    );
  }
  if (degree_level) {
    const degreeLower = degree_level.toLowerCase();
    filtered = filtered.filter((s) =>
      (s.eligibility?.degree_levels || []).some((level) => level.toLowerCase().includes(degreeLower))
    );
  }
  if (funding_type) {
    const fundingLower = funding_type.toLowerCase();
    filtered = filtered.filter((s) => (s.funding?.funding_type || "").toLowerCase() === fundingLower);
  }
  if (search) {
    const sLower = search.toLowerCase();
    filtered = filtered.filter(
      (s) =>
        s.name.toLowerCase().includes(sLower) ||
        (s.host_institution && s.host_institution.toLowerCase().includes(sLower)) ||
        (s.description && s.description.toLowerCase().includes(sLower))
    );
  }
  return {
    scholarships: filtered.slice(offset, offset + limit),
    total: filtered.length,
    source: "local_fallback",
  };
}

/**
 * Fetch a single scholarship with its complete 11-dimension deep dossier from the database.
 * Falls back to local compiled dataset if backend is unreachable.
 */
export async function fetchScholarshipById(
  scholarshipId: string
): Promise<{ scholarship: Scholarship | null; source: "database" | "local_fallback" }> {
  const cleanId = scholarshipId.trim();
  try {
    const res = await fetch(`${API_BASE}/api/scholarships/${encodeURIComponent(cleanId)}`, {
      cache: "no-store",
    });
    if (res.ok) {
      const data = await res.json();
      if (data?.scholarship) {
        return { scholarship: data.scholarship, source: "database" };
      }
    }
  } catch (err) {
    console.warn(`Backend fetch for scholarship '${cleanId}' failed, falling back to local dataset:`, err);
  }

  const found = SEED_SCHOLARSHIPS.find((s) => s.scholarship_id.toLowerCase() === cleanId.toLowerCase()) || null;
  return { scholarship: found, source: "local_fallback" };
}

/**
 * Fetch catalog and database health statistics from backend.
 */
export async function fetchScholarshipStats(): Promise<{
  total_scholarships: number;
  by_region: Record<string, number>;
  with_deep_dossiers: number;
  coverage_percent: number;
  total_profiles_seeded: number;
  total_sessions_recorded: number;
  database_status: string;
} | null> {
  try {
    const res = await fetch(`${API_BASE}/api/scholarships/stats/summary`, {
      cache: "no-store",
    });
    if (res.ok) {
      return await res.json();
    }
  } catch {
    // Backend offline
  }
  return null;
}

/**
 * Match scholarships against institutional database according to student profile.
 */
export async function matchScholarshipsForProfile(
  profile: any,
  regions?: string[],
  limit: number = 25
): Promise<{ ok: boolean; total_matched: number; results: Scholarship[] }> {
  try {
    const res = await fetch(`${API_BASE}/api/scholarships/match`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ profile, regions, limit }),
    });
    if (res.ok) {
      return await res.json();
    }
  } catch (err) {
    console.warn("Match endpoint failed, falling back to local query:", err);
  }
  const results = searchScholarshipsForProfile(profile, limit);
  return { ok: true, total_matched: results.length, results };
}
