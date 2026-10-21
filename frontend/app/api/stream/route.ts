import { NextRequest } from "next/server";
import { handleSSEStream } from "@/lib/streaming/streamGenerator";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const sessionId = searchParams.get("session_id") || "sess-live-stream";
  return handleSSEStream(req, sessionId);
}
