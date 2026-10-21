import { NextRequest, NextResponse } from "next/server";
import { saveProfileToStore, getSessionFromStore } from "@/lib/sessionStore";
import { attachSessionToken, backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";

export async function PUT(
  req: NextRequest,
  props: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await props.params;
  const profile = await req.json();

  // 1. Try FastAPI backend
  if (backendConfigured()) {
    try {
      const res = await fetch(`${BACKEND_URL}/api/profile/${sessionId}`, {
        method: "PUT",
        headers: backendHeaders(req, { "Content-Type": "application/json" }),
        body: JSON.stringify(profile),
        signal: AbortSignal.timeout(2000),
      });
      if (res.ok) {
        const data = await res.json();
        saveProfileToStore(sessionId, profile);
        return attachSessionToken(NextResponse.json(data), data?.session_token || res.headers.get("X-Session-Token"));
      }
    } catch {
      // Backend offline; store in local session cache
    }
  }

  saveProfileToStore(sessionId, profile);
  return NextResponse.json({ ok: true, data: profile });
}

export async function GET(
  req: NextRequest,
  props: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await props.params;

  if (backendConfigured()) {
    try {
      const res = await fetch(`${BACKEND_URL}/api/profile/${sessionId}`, {
        headers: backendHeaders(req),
        cache: "no-store",
        signal: AbortSignal.timeout(2000),
      });
      if (res.ok) {
        return NextResponse.json(await res.json());
      }
    } catch {
      // Backend offline
    }
  }

  const stored = getSessionFromStore(sessionId);
  if (stored?.profile) {
    return NextResponse.json({ profile: stored.profile });
  }

  return NextResponse.json({ error: "Profile not found" }, { status: 404 });
}
