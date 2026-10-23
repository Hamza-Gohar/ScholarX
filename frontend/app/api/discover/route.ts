import { NextRequest, NextResponse } from "next/server";
import { saveSessionToStore, startSessionDbAnalysis } from "@/lib/sessionStore";
import { attachSessionToken, backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";
import { saveSessionToDb } from "@/lib/db/sqliteClient";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const sessionId = body.session_id || `session-pk-${Date.now().toString(36)}`;
    const profile = body.profile || null;

    // Immediately kick off the intelligent database analysis process when mission is initialized
    if (profile) {
      startSessionDbAnalysis(sessionId, profile);
    }

    // 1. Try FastAPI backend if reachable
    if (backendConfigured()) {
      try {
        const res = await fetch(`${BACKEND_URL}/api/discover`, {
          method: "POST",
          headers: backendHeaders(req, { "Content-Type": "application/json" }),
          body: JSON.stringify(body),
          signal: AbortSignal.timeout(2500),
        });
        if (res.ok) {
          const data = await res.json();
          if (profile) {
            saveSessionToStore(sessionId, { profile });
            saveSessionToDb({
              sessionId,
              profile,
              status: "INITIATED",
            });
          }
          const response = NextResponse.json(data);
          return attachSessionToken(response, data?.session_token || res.headers.get("X-Session-Token"));
        }
      } catch {
        // Backend offline; continue to autonomous simulation
      }
    }

    // 2. Persist initial active session state to DB (discovering, no mock data)
    try {
      saveSessionToStore(sessionId, {
        profile,
        discovered: [],
        roadmap: null,
        status: "DISCOVERING",
      });
      saveSessionToDb({
        sessionId,
        profile,
        discovered: [],
        roadmap: null,
        status: "DISCOVERING",
      });
    } catch (e) {
      console.warn("[API/discover] Notice: SQLite persistence failed:", e);
    }

    return NextResponse.json({
      ok: true,
      session_id: sessionId,
      status: "INITIATED",
      mode: "AUTONOMOUS",
      data_source: "DATABASE_DYNAMIC_ENGINE",
      cloud_backend_configured: backendConfigured(),
      message: `Autonomous discovery mission initialized for ${profile?.personal?.name || "applicant"}.`,
    });
  } catch (err: any) {
    return NextResponse.json(
      { ok: false, error: err?.message || "Failed to launch discovery mission" },
      { status: 500 }
    );
  }
}
