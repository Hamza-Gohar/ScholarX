import { NextRequest, NextResponse } from "next/server";
import { correctStudentInputDeterministically } from "@/lib/ai/spellingCorrector";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const result = await correctStudentInputDeterministically({
      fieldOfStudy: body.fieldOfStudy || body.field,
      studentName: body.studentName || body.name,
      city: body.city,
      institution: body.institution,
      targetDegree: body.targetDegree || body.degree,
    });

    return NextResponse.json({
      success: true,
      ...result,
    });
  } catch (err: any) {
    return NextResponse.json(
      {
        success: false,
        error: err?.message || "Failed to normalize profile inputs",
      },
      { status: 500 }
    );
  }
}
