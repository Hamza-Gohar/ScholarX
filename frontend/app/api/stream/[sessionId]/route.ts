import { NextRequest } from "next/server";
import { handleSSEStream } from "@/lib/streaming/streamGenerator";

export const dynamic = "force-dynamic";

export async function GET(
  req: NextRequest,
  context: { params: Promise<{ sessionId: string }> }
) {
  const { sessionId } = await context.params;
  return handleSSEStream(req, sessionId || "sess-live-stream");
}
