import { NextRequest, NextResponse } from "next/server";
import { getSessionFromStore, buildSyntheticSession } from "@/lib/sessionStore";
import { backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";
import { getSessionDetailFromDb, saveSessionToDb } from "@/lib/db/sqliteClient";

export async function GET(
  req: NextRequest,
  props: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await props.params;

  // 1. Try FastAPI backend if online
  if (backendConfigured()) {
    try {
      const res = await fetch(`${BACKEND_URL}/api/sessions/${sessionId}`, {
        headers: backendHeaders(req),
        cache: "no-store",
        signal: AbortSignal.timeout(2000),
      });
      if (res.ok) {
        const data = await res.json();
        if (data && (data.session || data.session_id)) {
          return NextResponse.json(data);
        }
      }
    } catch {
      // Backend offline; continue to autonomous database retrieval
    }
  }

  // 2. Retrieve directly from SQLite database
  try {
    const dbSession = getSessionDetailFromDb(sessionId);
    if (dbSession && (dbSession.session || dbSession.profile)) {
      return NextResponse.json(dbSession);
    }
  } catch (err) {
    console.warn(`[API] SQLite lookup failed for session '${sessionId}':`, err);
  }

  // 3. Check in-memory session store
  const stored = getSessionFromStore(sessionId);
  if (stored && (stored.profile || stored.discovered?.length)) {
    return NextResponse.json({
      session: {
        session_id: sessionId,
        status: stored.status,
        student_profile: stored.profile,
        discovered_scholarships: stored.discovered,
        mission_parameters: {
          roadmap: stored.roadmap,
        },
      },
      profile: stored.profile,
    });
  }

  // 4. Fallback: dynamically synthesize session matching profile and persist to SQLite
  const searchParams = req.nextUrl?.searchParams || new URL(req.url, "http://localhost").searchParams;
  const qDegree = searchParams.get("degree");
  const qField = searchParams.get("field");
  const qName = searchParams.get("name");
  const qGpa = searchParams.get("gpa");
  const qRegions = searchParams.get("regions");

  const parsedRegions = qRegions
    ? qRegions.split(",").map((r) => r.trim()).filter(Boolean)
    : undefined;

  const customProfile = (qDegree || qField || qName || qRegions) ? {
    personal: {
      name: qName || "Applicant Candidate",
      city: "Islamabad",
      nationality: "PK",
      target_regions: parsedRegions,
    },
    academic: {
      degree_level: qDegree || "Bachelor's",
      current_level: qDegree || "Undergraduate / Intermediate",
      field_of_study: qField || "All Academic Disciplines",
      percentage: qGpa ? Number(qGpa) : 85,
      gpa_percentage: qGpa ? Number(qGpa) : 85,
    },
    preferences: {
      target_degree_level: qDegree || "Bachelor's",
      target_fields: [qField || "All Academic Disciplines"],
      funding_requirement: "FULL",
      preferred_regions: parsedRegions,
    },
  } : null;

  // 4. Return new active session state (discovering) without hardcoded mock data
  return NextResponse.json({
    session: {
      session_id: sessionId,
      status: "DISCOVERING",
      student_profile: customProfile || null,
      discovered_scholarships: [],
      mission_parameters: {},
    },
    profile: customProfile || null,
  });
}

export async function DELETE(
  req: NextRequest,
  props: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await props.params;
  try {
    await fetch(`${BACKEND_URL}/api/sessions/${encodeURIComponent(sessionId)}`, {
      method: "DELETE",
      headers: backendHeaders(req),
      signal: AbortSignal.timeout(2000),
    });
  } catch {
    // Backend offline
  }
  return NextResponse.json({ ok: true, session_id: sessionId });
}
