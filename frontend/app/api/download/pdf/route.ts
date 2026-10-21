import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const rawId = searchParams.get("id") || searchParams.get("scholarshipId") || "SCH-EU-001";
    const rawCandidateName = searchParams.get("name") || "Hamza_Gohar";

    // Strict sanitization: alphanumeric, hyphens, and underscores only
    const cleanId = rawId.replace(/[^a-zA-Z0-9_\-]/g, "") || "SCH-EU-001";
    const cleanName = rawCandidateName.replace(/[^a-zA-Z0-9_\-]/g, "_") || "Hamza_Gohar";

    // Redirect to the authentic, full vector print page with autoprint triggered
    // This renders the full 11-dimension dossier and automatically opens the native vector print/PDF dialog
    const targetUrl = new URL(
      `/dossier/${encodeURIComponent(cleanId)}/print?autoprint=true&name=${encodeURIComponent(cleanName)}`,
      request.url
    );
    return NextResponse.redirect(targetUrl, 307);
  } catch (error) {
    console.error("Error redirecting to dossier print:", error);
    return new NextResponse("Failed to redirect to dossier print view", { status: 500 });
  }
}
