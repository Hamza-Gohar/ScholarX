import { NextRequest, NextResponse } from "next/server";
import { attachSessionToken, backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";

export const dynamic = "force-dynamic";

export async function POST(request: NextRequest) {
  if (!backendConfigured()) {
    return NextResponse.json({ error: "Cloud profile ingestion is not configured." }, { status: 503 });
  }
  try {
    const formData = await request.formData();
    const response = await fetch(`${BACKEND_URL}/api/profile/upload`, {
      method: "POST",
      headers: backendHeaders(request),
      body: formData,
      signal: AbortSignal.timeout(30000),
    });
    const data = await response.json().catch(() => ({}));
    return attachSessionToken(NextResponse.json(data, { status: response.status }), data?.session_token || response.headers.get("X-Session-Token"));
  } catch {
    return NextResponse.json({ error: "Cloud profile ingestion is unavailable." }, { status: 503 });
  }
}
