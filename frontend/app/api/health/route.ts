import { NextResponse } from "next/server";
import { SEED_SCHOLARSHIPS } from "@/lib/seed-data";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || process.env.BACKEND_URL;
const canFetchBackend = Boolean(
  BACKEND_URL &&
    (process.env.NODE_ENV === "development" ||
      (!BACKEND_URL.includes("127.0.0.1") && !BACKEND_URL.includes("localhost")))
);

export async function GET() {
  if (canFetchBackend && BACKEND_URL) {
    try {
      const res = await fetch(`${BACKEND_URL}/api/health`, {
        cache: "no-store",
        signal: AbortSignal.timeout(3000),
      });

      if (res.ok) {
        const data = await res.json();
        return NextResponse.json({
          status: data.status || "HEALTHY",
          backend: "CONNECTED",
          api_keys: data.api_keys,
          timestamp: new Date().toISOString(),
        });
      }
    } catch (err) {
      // Backend offline or unreachable
    }
  }

  return NextResponse.json({
    status: "DEGRADED",
    backend: "OFFLINE",
    mode: "NEXTJS_LOCAL_FALLBACK",
    timestamp: new Date().toISOString(),
    scholarships_count: SEED_SCHOLARSHIPS.length,
  });
}
