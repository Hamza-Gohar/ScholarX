import { NextResponse } from "next/server";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || process.env.BACKEND_URL;
const canFetchBackend = Boolean(
  BACKEND_URL &&
    (process.env.NODE_ENV === "development" ||
      (!BACKEND_URL.includes("127.0.0.1") && !BACKEND_URL.includes("localhost")))
);

export async function GET() {
  let backendReady = false;
  if (canFetchBackend && BACKEND_URL) {
    try {
      const res = await fetch(`${BACKEND_URL}/api/health`, {
        cache: "no-store",
        signal: AbortSignal.timeout(2000),
      });
      if (res.ok) {
        backendReady = true;
      }
    } catch (err) {
      // Backend offline
    }
  }

  return NextResponse.json({
    ready: true,
    degraded: !backendReady,
    backend: backendReady ? "ONLINE" : "OFFLINE",
    timestamp: new Date().toISOString(),
  });
}
