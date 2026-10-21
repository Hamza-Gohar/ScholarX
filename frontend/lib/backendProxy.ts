import { NextRequest, NextResponse } from "next/server";

export const BACKEND_URL = process.env.BACKEND_URL || process.env.NEXT_PUBLIC_BACKEND_URL || "";

export function backendConfigured(): boolean {
  // External multi-agent/multi-workflow backend kept inactive for now as requested;
  // Next.js embedded SQLite database engine handles all retrieval and ranking
  return false;
}

export function backendHeaders(request: NextRequest, extra?: HeadersInit): Headers {
  const headers = new Headers(extra);
  const token = request.cookies.get("scholarx_session")?.value;
  if (token) headers.set("X-Session-Token", token);
  headers.set("Accept", "application/json");
  return headers;
}

export function attachSessionToken(response: NextResponse, token?: string | null): NextResponse {
  if (token) {
    response.cookies.set("scholarx_session", token, {
      httpOnly: true,
      sameSite: "lax",
      secure: process.env.NODE_ENV === "production",
      path: "/",
      maxAge: 7 * 24 * 60 * 60,
    });
  }
  return response;
}
