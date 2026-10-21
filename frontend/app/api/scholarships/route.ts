import { NextRequest, NextResponse } from "next/server";
import { SEED_SCHOLARSHIPS } from "@/lib/seed-data";
import { queryScholarshipsFromDb } from "@/lib/db/sqliteClient";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || process.env.BACKEND_URL;
const canFetchBackend = Boolean(
  BACKEND_URL &&
    (process.env.NODE_ENV === "development" ||
      (!BACKEND_URL.includes("127.0.0.1") && !BACKEND_URL.includes("localhost")))
);

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);

  // 1. Try to fetch from FastAPI backend SQLite relational database if reachable
  if (canFetchBackend && BACKEND_URL) {
    try {
      const backendRes = await fetch(`${BACKEND_URL}/api/scholarships?${searchParams.toString()}`, {
        next: { revalidate: 0 },
        signal: AbortSignal.timeout(3000),
      });
      if (backendRes.ok) {
        const data = await backendRes.json();
        return NextResponse.json(data);
      }
    } catch {
      // Backend offline; fallback to direct SQLite query
    }
  }

  const search = (searchParams.get("search") || searchParams.get("q") || "").toLowerCase().trim();
  const region = searchParams.get("region") || undefined;
  const country = (searchParams.get("country") || "").trim() || undefined;
  const fundingType = (searchParams.get("funding_type") || "").trim() || undefined;
  const degreeLevel = (searchParams.get("degree_level") || "").trim() || undefined;
  const hecOnly = searchParams.get("hec_only") === "true";
  const moiOnly = searchParams.get("moi_only") === "true";
  const sortBy = searchParams.get("sort_by") || "name";
  const sortOrder = (searchParams.get("sort_order") || "asc").toLowerCase() as "asc" | "desc";
  const rawLimit = parseInt(searchParams.get("limit") || "50", 10);
  const rawOffset = parseInt(searchParams.get("offset") || "0", 10);
  const limit = isNaN(rawLimit) ? 50 : Math.max(1, Math.min(100, rawLimit));
  const offset = isNaN(rawOffset) ? 0 : Math.max(0, rawOffset);

  // 2. Query direct from SQLite database
  try {
    const dbResult = queryScholarshipsFromDb({
      search: search || undefined,
      region,
      country,
      funding_type: fundingType,
      degree_level: degreeLevel,
      hec_only: hecOnly,
      moi_only: moiOnly,
      sort_by: sortBy,
      sort_order: sortOrder,
      limit,
      offset,
    });

    if (dbResult && dbResult.scholarships.length > 0) {
      return NextResponse.json({
        scholarships: dbResult.scholarships,
        total: dbResult.total,
        limit,
        offset,
        sort_by: sortBy,
        sort_order: sortOrder,
        source: "database",
      });
    }
  } catch (err) {
    console.warn("[API] SQLite scholarships query notice:", err);
  }

  // 3. Fallback to in-memory SEED_SCHOLARSHIPS if SQLite is unavailable
  let filtered = [...SEED_SCHOLARSHIPS];

  if (region && region !== "ALL") {
    filtered = filtered.filter((s) => s.region.toLowerCase() === region.toLowerCase());
  }

  if (country) {
    const cLower = country.toLowerCase();
    filtered = filtered.filter(
      (s) =>
        s.host_country.toLowerCase() === cLower ||
        s.host_country_name.toLowerCase().includes(cLower)
    );
  }

  if (search) {
    filtered = filtered.filter(
      (s) =>
        s.name.toLowerCase().includes(search) ||
        s.scholarship_id.toLowerCase().includes(search) ||
        s.host_country_name.toLowerCase().includes(search) ||
        (s.host_institution && s.host_institution.toLowerCase().includes(search)) ||
        (s.description && s.description.toLowerCase().includes(search))
    );
  }

  if (fundingType && fundingType !== "ALL") {
    filtered = filtered.filter((s) => (s.funding?.funding_type || "").toUpperCase() === fundingType.toUpperCase());
  }

  if (degreeLevel && degreeLevel !== "ALL") {
    filtered = filtered.filter((s) =>
      (s.eligibility?.degree_levels || []).some((d) => d.toLowerCase().includes(degreeLevel.toLowerCase()))
    );
  }

  if (hecOnly) {
    filtered = filtered.filter(
      (s) =>
        Boolean(s.pakistan_requirements?.hec_managed) ||
        Boolean(s.pakistan_requirements?.pakistan_bilateral_quota)
    );
  }

  if (moiOnly) {
    filtered = filtered.filter(
      (s) =>
        Boolean(s.pakistan_requirements?.accepts_moi_certificate) ||
        Boolean((s as any)?.deep_dossier?.eligibility_requirements?.moi_certificate_accepted)
    );
  }

  const paginated = filtered.slice(offset, offset + limit);

  return NextResponse.json({
    scholarships: paginated,
    total: filtered.length,
    limit,
    offset,
    sort_by: sortBy,
    sort_order: sortOrder,
    source: "local_fallback",
  });
}
