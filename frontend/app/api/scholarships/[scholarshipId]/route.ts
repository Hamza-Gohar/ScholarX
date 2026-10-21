import { NextRequest, NextResponse } from "next/server";
import { getScholarshipByIdFromDb } from "@/lib/db/sqliteClient";
import { getScholarshipById as getSeedScholarshipById } from "@/lib/seed-data";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || process.env.BACKEND_URL;
const canFetchBackend = Boolean(
  BACKEND_URL &&
    (process.env.NODE_ENV === "development" ||
      (!BACKEND_URL.includes("127.0.0.1") && !BACKEND_URL.includes("localhost")))
);

export async function GET(
  req: NextRequest,
  props: { params: Promise<{ scholarshipId: string }> }
) {
  const { scholarshipId } = await props.params;
  const cleanId = decodeURIComponent(scholarshipId).trim();

  // 1. Try FastAPI backend if online
  if (canFetchBackend && BACKEND_URL) {
    try {
      const backendRes = await fetch(`${BACKEND_URL}/api/scholarships/${encodeURIComponent(cleanId)}`, {
        next: { revalidate: 0 },
        signal: AbortSignal.timeout(3000),
      });
      if (backendRes.ok) {
        return NextResponse.json(await backendRes.json());
      }
    } catch {
      // Backend offline -> fallback to database
    }
  }

  // 2. Query SQLite database
  try {
    const dbSc = getScholarshipByIdFromDb(cleanId);
    if (dbSc) {
      return NextResponse.json({
        scholarship: dbSc,
        source: "database",
      });
    }
  } catch (err) {
    console.warn(`[API] SQLite fetch error for scholarship '${cleanId}':`, err);
  }

  // 3. Fallback to seed data
  const seedSc = getSeedScholarshipById(cleanId);
  if (seedSc) {
    return NextResponse.json({
      scholarship: seedSc,
      source: "local_fallback",
    });
  }

  return NextResponse.json({ error: "Scholarship not found" }, { status: 404 });
}
