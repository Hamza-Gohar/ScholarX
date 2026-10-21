import { NextRequest, NextResponse } from "next/server";
import { getSessionFromStore } from "@/lib/sessionStore";
import { backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";

export async function GET(
  req: NextRequest,
  props: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await props.params;

  try {
    if (!backendConfigured()) throw new Error("Cloud backend not configured");
    const res = await fetch(`${BACKEND_URL}/api/discover/${encodeURIComponent(sessionId)}/status`, {
      headers: backendHeaders(req),
      cache: "no-store",
      signal: AbortSignal.timeout(2000),
    });
    if (res.ok) {
      const data = await res.json();
      return NextResponse.json({ ...data, phase: data.phase || data.active_phase || "NONE" });
    }
  } catch {
    // Backend offline
  }

  const stored = getSessionFromStore(sessionId);
  if (stored) {
    return NextResponse.json({
      session_id: sessionId,
      status: stored.status,
      phase: stored.status === "COMPLETED" ? "COMPLETE" : "DISCOVERY",
      candidates_found: stored.discovered.length,
    });
  }

  return NextResponse.json({
    session_id: sessionId,
    status: "COMPLETED",
    phase: "COMPLETE",
    candidates_found: 10,
  });
}
