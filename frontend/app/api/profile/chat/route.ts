import { NextRequest, NextResponse } from "next/server";
import { attachSessionToken, backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";

export const dynamic = "force-dynamic";

export async function POST(request: NextRequest) {
  if (!backendConfigured()) {
    return NextResponse.json({ error: "Cloud counselor is not configured." }, { status: 503 });
  }
  try {
    const body = await request.json();
    const response = await fetch(`${BACKEND_URL}/api/profile/chat`, {
      method: "POST",
      headers: backendHeaders(request, { "Content-Type": "application/json" }),
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(15000),
    });
    const data = await response.json().catch(() => ({}));
    return attachSessionToken(NextResponse.json(data, { status: response.status }), data?.session_token || response.headers.get("X-Session-Token"));
  } catch {
    return NextResponse.json({ error: "Cloud counselor is unavailable." }, { status: 503 });
  }
}
