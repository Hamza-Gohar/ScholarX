import csv
import io
import logging
from typing import Optional
from fastapi import APIRouter, HTTPException, Query, Request, Response
from db.session_store import get_session_store
from schemas.student import StudentProfile
from schemas.search import PersonalizedSearchResponse

logger = logging.getLogger("scholarx.api.scholarships")

router = APIRouter(prefix="/scholarships", tags=["scholarships"])


@router.get("")
async def list_scholarships(
    region: Optional[str] = Query(None, description="Filter by region (e.g. Europe, Asia, Americas, MENA, Oceania)"),
    country: Optional[str] = Query(None, description="Filter by host country code or name (e.g. DE, Germany)"),
    search: Optional[str] = Query(None, description="Search keyword in scholarship name, institution, or description"),
    degree_level: Optional[str] = Query(None, description="Filter by degree level (e.g. Bachelor's, Master's, PhD)"),
    funding_type: Optional[str] = Query(None, description="Filter by funding type (e.g. FULL, PARTIAL, TUITION_ONLY)"),
    hec_only: Optional[bool] = Query(None, description="Filter for Pakistani Bilateral / HEC Quota only"),
    moi_only: Optional[bool] = Query(None, description="Filter for scholarships accepting MOI waiver (No IELTS)"),
    min_stipend_pkr: Optional[int] = Query(None, description="Minimum monthly stipend in PKR"),
    sort_by: Optional[str] = Query("name", description="Column to sort by: name, country, deadline, stipend_pkr, min_gpa, scholarship_id, region, funding_type"),
    sort_order: Optional[str] = Query("asc", description="Sort direction: asc or desc"),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    """
    Browse and search verified relational scholarships repository.
    Supports multi-facet filtering by region, country, search terms, degree level, funding type,
    HEC quota, MOI waiver, and custom column sorting.
    """
    store = get_session_store()
    scholarships, total = await store.query_scholarships(
        region=region,
        country=country,
        search=search,
        degree_level=degree_level,
        funding_type=funding_type,
        hec_only=hec_only,
        moi_only=moi_only,
        min_stipend_pkr=min_stipend_pkr,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
    )
    return {
        "scholarships": scholarships,
        "total": total,
        "limit": limit,
        "offset": offset,
        "sort_by": sort_by,
        "sort_order": sort_order,
    }


@router.get("/export/csv")
async def export_scholarships_csv(
    region: Optional[str] = Query(None),
    funding_type: Optional[str] = Query(None),
):
    """
    Exports the verified relational scholarships database into a clean CSV spreadsheet.
    Can be opened directly in Microsoft Excel, Google Sheets, or LibreOffice Calc.
    """
    store = get_session_store()
    scholarships, _ = await store.query_scholarships(
        region=region,
        funding_type=funding_type,
        limit=1000,
        offset=0,
    )

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Scholarship ID",
        "Name",
        "Host Country",
        "Region",
        "Host Institution",
        "Funding Type",
        "Degree Levels",
        "Min GPA (4.0)",
        "Min Percentage (%)",
        "IELTS Minimum",
        "MOI Waiver Accepted",
        "Monthly Stipend (Host)",
        "Monthly Stipend (PKR Approx)",
        "Pakistani Bilateral Quota",
        "Quota Seats",
        "HEC Managed",
        "Application Deadline",
        "Competition Level",
        "Source URL",
        "Portal URL",
    ])

    for sc in scholarships:
        writer.writerow([
            sc.scholarship_id,
            sc.name,
            sc.host_country_name or sc.host_country,
            sc.region,
            sc.host_institution or "Various Universities",
            sc.funding.funding_type.value if hasattr(sc.funding.funding_type, "value") else str(sc.funding.funding_type),
            ", ".join(sc.eligibility.degree_levels) if sc.eligibility else "",
            sc.eligibility.min_gpa_4_scale if sc.eligibility else "",
            sc.eligibility.min_gpa_percentage if sc.eligibility else "",
            sc.language.minimum_ielts if sc.language else "",
            "YES" if (sc.pakistan_requirements and sc.pakistan_requirements.accepts_moi_certificate) else "NO",
            sc.funding.monthly_stipend if sc.funding else "",
            sc.funding.monthly_stipend_pkr_approx if sc.funding else "",
            "YES" if (sc.pakistan_requirements and sc.pakistan_requirements.pakistan_bilateral_quota) else "NO",
            sc.pakistan_requirements.pakistan_quota_seats if sc.pakistan_requirements else "",
            "YES" if (sc.pakistan_requirements and sc.pakistan_requirements.hec_managed) else "NO",
            sc.application_deadline or "Annual Recurring",
            sc.competition_level.value if hasattr(sc.competition_level, "value") else str(sc.competition_level or "MODERATE"),
            sc.source_url,
            sc.portal_url or "",
        ])

    csv_data = output.getvalue()
    return Response(
        content=csv_data,
        media_type="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="ScholarX_310_Scholarships_Relational_Catalog.csv"'
        },
    )


@router.post("/match")
async def match_scholarships_for_profile(
    profile: StudentProfile,
    limit: int = Query(30, ge=1, le=100),
):
    """
    Searches the verified institutional database cache specifically matching a student's profile.
    Considers target degree level, field of study, Pakistani bilateral eligibility,
    minimum GPA requirements, English testing status (including MOI waiver programs), and budget.
    """
    store = get_session_store()
    matches = await store.search_scholarships_for_profile_detailed(student=profile, limit=limit)
    response = PersonalizedSearchResponse(
        matches=matches,
        scholarships=[item.scholarship for item in matches],
        total=len(matches),
        profile_summary={
            "name": profile.personal.name,
            "target_degree": profile.preferences.target_degree_level,
            "fields": profile.preferences.target_fields,
            "gpa_percentage": profile.academic.gpa_percentage,
            "max_out_of_pocket_pkr": profile.preferences.max_out_of_pocket_pkr,
            "preferred_regions": profile.preferences.preferred_regions,
            "english_test": profile.language.english_proficiency_test.value,
        },
        database={
            "source": "VERIFIED_DATABASE",
            "personalized": True,
            "explainable": True,
            "live_web_refresh": False,
        },
    )
    return response.model_dump(mode="json")


@router.get("/stats/summary")
async def get_scholarships_stats():
    """Returns real-time aggregated metrics of the active scholarship database cache."""
    store = get_session_store()
    return await store.get_scholarships_stats()


@router.get("/download/master-pdf")
async def download_master_pdf():
    """
    Downloads the complete publication-grade Master Scholarship Intelligence Dossier
    containing all 310 verified opportunities across 5 continental scouting divisions.
    """
    from fastapi.responses import FileResponse
    from utils.pdf_service import get_master_pdf_path

    try:
        pdf_path = get_master_pdf_path()
        return FileResponse(
            path=str(pdf_path),
            media_type="application/pdf",
            filename="ScholarX_Global_Master_Scholarship_Dossier_2026_2027.pdf",
            headers={
                "Content-Disposition": 'attachment; filename="ScholarX_Global_Master_Scholarship_Dossier_2026_2027.pdf"'
            }
        )
    except Exception as e:
        logger.error(f"Error serving master PDF: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve or generate master dossier PDF. Please try again later."
        )


@router.get("/{scholarship_id}")
async def get_scholarship(scholarship_id: str):
    """Retrieves full details for a single scholarship opportunity."""
    import re
    clean_id = re.sub(r"[^a-zA-Z0-9_\-]", "", scholarship_id.strip())
    store = get_session_store()
    scholarship = await store.get_scholarship_by_id(clean_id)
    if not scholarship:
        raise HTTPException(status_code=404, detail=f"Scholarship '{clean_id}' not found in database cache")
    return {"scholarship": scholarship}


@router.get("/{scholarship_id}/pdf")
async def download_scholarship_pdf(scholarship_id: str, request: Request, download: bool = False):
    """
    Retrieves or on-demand compiles an official publication-grade vector PDF dossier
    for a specific scholarship opportunity. Rate-limited and path-sanitized.
    """
    from fastapi.responses import FileResponse
    from utils.pdf_service import get_or_generate_scholarship_pdf
    from utils.rate_limiter import pdf_limiter
    import re

    await pdf_limiter.check(request)
    clean_id = re.sub(r"[^a-zA-Z0-9_\-]", "", scholarship_id.strip())
    if not clean_id:
        raise HTTPException(status_code=400, detail="Invalid scholarship identifier.")

    try:
        pdf_path = get_or_generate_scholarship_pdf(clean_id)
        disposition = "attachment" if download else "inline"
        filename = f"ScholarX_{clean_id}_Dossier_2026_2027.pdf"
        return FileResponse(
            path=str(pdf_path),
            media_type="application/pdf",
            filename=filename,
            headers={
                "Content-Disposition": f'{disposition}; filename="{filename}"'
            }
        )
    except ValueError as ve:
        raise HTTPException(status_code=404, detail="Requested scholarship dossier not found.")
    except Exception as e:
        logger.error(f"Error generating scholarship PDF for {clean_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to compile scholarship dossier PDF.")

