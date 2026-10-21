import { NextRequest, NextResponse } from "next/server";
import { backendConfigured, BACKEND_URL, backendHeaders } from "@/lib/backendProxy";
import { listSessionsFromDb } from "@/lib/db/sqliteClient";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  const limit = parseInt(request.nextUrl.searchParams.get("limit") || "50", 10);

  // 1. Try FastAPI backend if configured
  if (backendConfigured()) {
    try {
      const response = await fetch(`${BACKEND_URL}/api/sessions?limit=${encodeURIComponent(String(limit))}`, {
        headers: backendHeaders(request),
        cache: "no-store",
        signal: AbortSignal.timeout(3000),
      });
      if (response.ok) {
        const data = await response.json();
        return NextResponse.json(data);
      }
    } catch {
      // Backend unavailable -> fallback to database
    }
  }

  // 2. Query SQLite database directly
  try {
    const dbSessions = listSessionsFromDb(limit);
    if (dbSessions && dbSessions.length > 0) {
      return NextResponse.json({
        sessions: dbSessions,
        total: dbSessions.length,
        source: "database",
      });
    }
  } catch (err) {
    console.error("[API] Failed to query sessions from SQLite database:", err);
  }

  return NextResponse.json({
    sessions: [],
    total: 0,
    source: "empty_fallback",
  });
}
