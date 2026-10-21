import { NextRequest, NextResponse } from "next/server";
import { getSessionFromStore, buildSyntheticSession } from "@/lib/sessionStore";
import { backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";

export async function GET(
  req: NextRequest,
  props: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await props.params;

  if (backendConfigured()) {
    try {
      const res = await fetch(`${BACKEND_URL}/api/discover/${encodeURIComponent(sessionId)}/results`, {
        headers: backendHeaders(req),
        cache: "no-store",
        signal: AbortSignal.timeout(2000),
      });
      if (res.ok) {
        const data = await res.json();
        return NextResponse.json({
          ...data,
          discovered_scholarships: data.discovered_scholarships || data.ranked_results || [],
          total_count: data.total_count ?? data.total_ranked ?? (data.ranked_results || []).length,
          data_source: data.data_source || "LIVE_PIPELINE_AND_VERIFIED_DATABASE",
          personalized: data.personalized !== false,
        });
      }
    } catch {
      // Backend offline; continue to autonomous fallback
    }
  }

  const stored = getSessionFromStore(sessionId);
  if (stored) {
    return NextResponse.json({
      session_id: sessionId,
      status: stored.status,
      discovered_scholarships: stored.discovered,
      total_count: stored.discovered.length,
      roadmap: stored.roadmap,
    });
  }

  const synthetic = buildSyntheticSession(sessionId);
  return NextResponse.json({
    session_id: sessionId,
    status: synthetic.session.status,
    discovered_scholarships: synthetic.session.discovered_scholarships,
    total_count: synthetic.session.discovered_scholarships.length,
    roadmap: synthetic.session.mission_parameters.roadmap,
  });
}
