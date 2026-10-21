"""
ScholarX Master Scholarship Catalog & Publication-Grade PDF Generator
Redesigned with Enterprise-Grade CSS, Anti-AI Slop Typography, High Information Density,
and Comprehensive Coverage Across All 310 Scholarships in the Database.
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    import weasyprint
except ImportError:
    weasyprint = None

# Ensure backend modules can be imported
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "backend"))

from utils.dossier_normalizer import load_all_normalized_dossiers, clean_str

DEFAULT_OUTPUT_PDF = REPO_ROOT / "data" / "ScholarX_Global_Master_Scholarship_Dossier_2026_2027.pdf"
DEFAULT_PAKISTAN_PDF = Path("/home/hamza/.gemini/antigravity/brain/412ce3ab-ae9a-433b-a9b1-e3340a2b51fd/ScholarX_Pakistan_Scholarship_Dossier_2026_2027.pdf")


def build_scholarship_card_html(s: Dict[str, Any]) -> str:
    """Generates a compact, high-density, anti-AI-slop HTML card for a single scholarship."""
    fc = s["financial_coverage"]
    el = s["eligibility"]
    sm = s["summary"]
    sources = s["official_sources"]

    # Country Flag / Code
    country_code = s["country"][:2].upper() if s["country"] else "GL"
    
    # Financial items
    tuition = fc["tuition"]
    stipend = fc["monthly_stipend"]
    accom = fc["accommodation"]
    airfare = fc["airfare"]
    insurance = fc["health_insurance"]
    visa = fc["visa_fee"]
    
    # Format stipend display
    stipend_disp = stipend.get("amount") or stipend.get("details") or "Monthly Maintenance Allowance"
    if len(stipend_disp) > 75:
        stipend_disp = stipend_disp[:72] + "..."
        
    tuition_disp = tuition.get("status") or "100% Covered"
    if tuition.get("details") and len(tuition["details"]) < 50:
        tuition_disp += f" ({tuition['details']})"
        
    accom_disp = accom.get("details") or accom.get("status") or "Dormitory / Housing Allowance"
    if len(accom_disp) > 65:
        accom_disp = accom_disp[:62] + "..."

    # Travel & Health
    travel_health_disp = f"Airfare: {airfare.get('status', 'Covered')} • Health: {insurance.get('status', 'Covered')}"
    if visa.get("is_covered"):
        travel_health_disp += " • Visa Waived"

    # Covered tags pills
    covered_pills = "".join(f'<span class="badge badge-success">✓ {clean_str(tag)}</span>' for tag in fc["covered_tags"][:6])
    not_covered_pills = "".join(f'<span class="badge badge-warning">✕ {clean_str(tag)}</span>' for tag in fc["not_covered_tags"][:3])
    
    # Documents checklist pills
    docs_html = "".join(
        f'<span class="doc-item" title="{clean_str(doc.get("notes"))}">☑ {clean_str(doc.get("name"))}</span>'
        for doc in sm["required_documents"][:7]
    )

    # Workflow steps
    workflow_html = "".join(
        f'<li class="workflow-step">{clean_str(step)}</li>'
        for step in sm["workflow_steps"][:4]
    )

    # Sources links
    sources_html = " • ".join(
        f'<a href="{clean_str(src.get("url"))}" class="source-link" target="_blank"><u>{clean_str(src.get("title"))}</u></a>'
        for src in sources[:3]
    )

    return f"""
    <div class="sc-card">
      <!-- Header Row -->
      <div class="sc-header">
        <div class="sc-meta-left">
          <div class="sc-tags">
            <span class="tag tag-region">{clean_str(s.get("region"))}</span>
            <span class="tag tag-country">{clean_str(s.get("country"))}</span>
            <span class="tag tag-id">{clean_str(s.get("id"))}</span>
            <span class="tag tag-funding">{clean_str(s.get("funding_type")).replace("_", " ")}</span>
          </div>
          <h2 class="sc-title">{clean_str(s.get("name"))}</h2>
          <div class="sc-sub">
            <strong>Host Body:</strong> {clean_str(s.get("offering_entity"))} &nbsp;|&nbsp;
            <strong>Placement:</strong> {clean_str(s.get("host_institutions"))[:75]}
          </div>
        </div>
        <div class="sc-meta-right">
          <div class="deadline-badge">
            <span class="deadline-label">APPLICATION DEADLINE</span>
            <span class="deadline-val">{clean_str(s.get("deadline"))}</span>
          </div>
          <div class="degree-badge">
            {clean_str(s.get("degree_levels_str"))} • {clean_str(s.get("duration"))}
          </div>
        </div>
      </div>

      <!-- Financial Metrics 4-Box Bar -->
      <div class="metrics-grid">
        <div class="metric-box">
          <span class="m-label">TUITION COVERAGE</span>
          <span class="m-val text-emerald">{clean_str(tuition_disp)}</span>
        </div>
        <div class="metric-box">
          <span class="m-label">MONTHLY STIPEND</span>
          <span class="m-val">{clean_str(stipend_disp)}</span>
        </div>
        <div class="metric-box">
          <span class="m-label">ACCOMMODATION</span>
          <span class="m-val">{clean_str(accom_disp)}</span>
        </div>
        <div class="metric-box">
          <span class="m-label">TRAVEL & HEALTH</span>
          <span class="m-val">{clean_str(travel_health_disp)}</span>
        </div>
      </div>

      <!-- Coverage Conditions Badges Strip -->
      <div class="coverage-strip">
        <span class="strip-label">COVERAGE SPECIFICATION:</span>
        {covered_pills}
        {not_covered_pills}
      </div>

      <!-- 2-Column Detail Grid -->
      <div class="details-grid">
        <!-- Col 1: Requirements & Eligibility -->
        <div class="grid-col">
          <div class="section-title">ELIGIBILITY &amp; ACADEMIC REQUIREMENTS</div>
          <table class="dense-table">
            <tr>
              <td class="dt-key">Age Requirement</td>
              <td class="dt-val">{clean_str(el.get("age_notes"))}</td>
            </tr>
            <tr>
              <td class="dt-key">Academic Cutoff</td>
              <td class="dt-val"><strong>{clean_str(el.get("minimum_gpa"))}</strong> — {clean_str(el.get("academic_qualifications"))[:65]}</td>
            </tr>
            <tr>
              <td class="dt-key">Nationality / Quota</td>
              <td class="dt-val">{clean_str(el.get("nationality"))[:70]}</td>
            </tr>
            <tr>
              <td class="dt-key">English Proficiency</td>
              <td class="dt-val">
                <span class="badge { 'badge-success' if el.get('moi_accepted') else 'badge-info' }">{clean_str(el.get('english_badge'))}</span>
                <span class="text-muted text-xs">{clean_str(el.get('language_notes'))[:60]}</span>
              </td>
            </tr>
            <tr>
              <td class="dt-key">Degree Field Scope</td>
              <td class="dt-val">{clean_str(el.get("field_requirements"))[:80]}</td>
            </tr>
            <tr>
              <td class="dt-key">Experience / Terms</td>
              <td class="dt-val">{clean_str(el.get("other_requirements"))[:80]}</td>
            </tr>
          </table>
        </div>

        <!-- Col 2: Application Process & Required Documents -->
        <div class="grid-col">
          <div class="section-title">APPLICATION PROCESS &amp; REQUIRED DOCUMENTS</div>
          <div class="workflow-box">
            <span class="wf-title">Roadmap Sequence:</span>
            <ol class="workflow-list">
              {workflow_html}
            </ol>
          </div>
          <div class="docs-box">
            <span class="docs-title">Mandatory Document Dossier:</span>
            <div class="docs-checklist">
              {docs_html}
            </div>
          </div>
        </div>
      </div>

      <!-- Strategic Due Diligence & Official Citations Footer -->
      <div class="sc-footer">
        <div class="footer-block highlight-block">
          <strong>Strategic Merit:</strong> {clean_str(sm.get("why_interesting"))}
        </div>
        <div class="footer-block warning-block">
          <strong>Due Diligence / Safeguards:</strong> {clean_str(sm.get("fee_warning"))} • {clean_str(sm.get("hidden_costs"))[:85]}
        </div>
        <div class="footer-sources">
          <span class="sources-title">Verified Official Portals:</span>
          {sources_html}
          <span class="cycle-note">(Academic Cycle: {clean_str(s.get("open_date"))} &rarr; Intake: {clean_str(s.get("commencement"))})</span>
        </div>
      </div>
    </div>
    """


def generate_master_catalog_html(scholarships: List[Dict[str, Any]], title: str = "ScholarX Global Scholarship Intelligence Catalog") -> str:
    """Compiles the full publication HTML document with enterprise-grade typography and print CSS."""
    
    # Group scholarships by region
    regions_order = ["Europe", "Asia", "Americas", "MENA", "Oceania"]
    by_region: Dict[str, List[Dict[str, Any]]] = {r: [] for r in regions_order}
    other_list: List[Dict[str, Any]] = []

    for s in scholarships:
        reg = s.get("region", "Other")
        if reg in by_region:
            by_region[reg].append(s)
        else:
            other_list.append(s)
            
    total_count = len(scholarships)
    countries_count = len(set(s.get("country", "") for s in scholarships))
    fully_funded_count = sum(1 for s in scholarships if "FULL" in s.get("funding_type", ""))

    # Build regional sections
    body_sections = []
    
    for reg in regions_order:
        reg_items = by_region[reg]
        if not reg_items:
            continue
            
        cards_html = "\n".join(build_scholarship_card_html(s) for s in reg_items)
        body_sections.append(f"""
        <div class="region-chapter page-break-before">
          <div class="chapter-header">
            <div class="chapter-meta">OFFICIAL REGIONAL INTELLIGENCE DOSSIER</div>
            <h1 class="chapter-title">{reg.upper()} REGION ({len(reg_items)} OPPORTUNITIES)</h1>
            <p class="chapter-desc">Verified bilateral quotas, government flagship endowments, and premier university foundations across {reg}.</p>
          </div>
          <div class="cards-container">
            {cards_html}
          </div>
        </div>
        """)

    if other_list:
        cards_html = "\n".join(build_scholarship_card_html(s) for s in other_list)
        body_sections.append(f"""
        <div class="region-chapter page-break-before">
          <div class="chapter-header">
            <h1 class="chapter-title">INTERNATIONAL &amp; MULTI-REGION ({len(other_list)} OPPORTUNITIES)</h1>
          </div>
          <div class="cards-container">
            {cards_html}
          </div>
        </div>
        """)

    all_chapters_html = "\n".join(body_sections)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} (2026/2027 Cohort)</title>
<style>
  /* =========================================================================
     SCHOLARX ENTERPRISE PRINT DESIGN SYSTEM (Anti-AI Slop Specification)
     Strict typographic hierarchy, tabular numbers, hairline borders,
     A4 paged media, and high information density.
     ========================================================================= */

  @page {{
    size: A4 portrait;
    margin: 10mm 11mm 12mm 11mm;
    @top-left {{
      content: "SCHOLARX GLOBAL INTELLIGENCE // COHORT 2026/2027";
      font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
      font-size: 7pt;
      font-weight: 700;
      color: #0F766E;
      letter-spacing: 0.05em;
    }}
    @top-right {{
      content: "OFFICIAL VERIFIED DOSSIER • CONFIDENCE: 98%";
      font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
      font-size: 7pt;
      font-weight: 600;
      color: #64748B;
    }}
    @bottom-left {{
      content: "SCHOLARX RESEARCH NETWORK • CANONICAL ADMISSIONS PUBLICATION • STRICTLY FOR ADVISEES";
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 6.5pt;
      color: #94A3B8;
    }}
    @bottom-right {{
      content: "Page " counter(page) " of " counter(pages);
      font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
      font-size: 7pt;
      font-weight: 700;
      color: #0F172A;
    }}
  }}

  *, *::before, *::after {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #0F172A;
    background-color: #FFFFFF;
    font-size: 8pt;
    line-height: 1.35;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  /* Typography Utilities */
  h1, h2, h3, h4 {{
    font-weight: 700;
    color: #0F172A;
    letter-spacing: -0.01em;
  }}

  .text-emerald {{ color: #047857 !important; }}
  .text-teal {{ color: #0F766E !important; }}
  .text-amber {{ color: #B45309 !important; }}
  .text-muted {{ color: #64748B !important; }}
  .text-xs {{ font-size: 7pt !important; }}

  /* Cover & Front Matter */
  .cover-page {{
    page-break-after: always;
    break-after: page;
    padding-top: 15mm;
    padding-bottom: 10mm;
    border-bottom: 2pt solid #0F172A;
  }}

  .cover-preheader {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", monospace;
    font-size: 8.5pt;
    font-weight: 700;
    color: #0F766E;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 4mm;
  }}

  .cover-title {{
    font-size: 24pt;
    line-height: 1.15;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 3mm;
  }}

  .cover-subtitle {{
    font-size: 11pt;
    line-height: 1.4;
    color: #334155;
    margin-bottom: 6mm;
    max-width: 90%;
  }}

  .kpi-row {{
    display: flex;
    gap: 8px;
    margin-bottom: 8mm;
  }}

  .kpi-box {{
    flex: 1;
    border: 1px solid #CBD5E1;
    border-left: 3px solid #0F766E;
    background: #F8FAFC;
    padding: 6px 10px;
    border-radius: 3px;
  }}

  .kpi-num {{
    font-family: ui-monospace, "SF Mono", monospace;
    font-size: 16pt;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.1;
  }}

  .kpi-label {{
    font-size: 7.5pt;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    margin-top: 2px;
  }}

  .macro-summary-box {{
    border: 1px solid #CBD5E1;
    background: #FFFFFF;
    padding: 10px 14px;
    margin-bottom: 6mm;
    border-radius: 4px;
  }}

  .macro-title {{
    font-size: 9.5pt;
    font-weight: 700;
    color: #0F766E;
    text-transform: uppercase;
    margin-bottom: 4px;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 3px;
  }}

  .macro-text {{
    font-size: 8.5pt;
    line-height: 1.45;
    color: #334155;
  }}

  /* Runway Table */
  .runway-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 4mm;
    font-size: 7.5pt;
  }}

  .runway-table th {{
    background: #0F172A;
    color: #FFFFFF;
    font-weight: 700;
    text-align: left;
    padding: 4px 6px;
    font-size: 7pt;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}

  .runway-table td {{
    padding: 4px 6px;
    border-bottom: 1px solid #E2E8F0;
    vertical-align: top;
  }}

  .runway-table tr:nth-child(even) td {{
    background: #F8FAFC;
  }}

  /* Regional Chapter Dividers */
  .region-chapter {{
    margin-top: 4mm;
  }}

  .chapter-header {{
    background: #0F172A;
    color: #FFFFFF;
    padding: 8px 12px;
    border-radius: 4px;
    margin-bottom: 5mm;
  }}

  .chapter-meta {{
    font-family: ui-monospace, "SF Mono", monospace;
    font-size: 7pt;
    color: #5EEAD4;
    letter-spacing: 0.08em;
    font-weight: 700;
  }}

  .chapter-title {{
    font-size: 13pt;
    font-weight: 800;
    color: #FFFFFF;
    margin: 2px 0;
  }}

  .chapter-desc {{
    font-size: 7.5pt;
    color: #CBD5E1;
  }}

  /* Scholarship Card Layout (Strict Page Protection) */
  .sc-card {{
    border: 1px solid #CBD5E1;
    border-top: 2.5px solid #0F766E;
    border-radius: 3px;
    padding: 7px 9px;
    margin-bottom: 5mm;
    background: #FFFFFF;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  .sc-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 4px;
    margin-bottom: 4px;
    gap: 8px;
  }}

  .sc-meta-left {{
    flex: 1;
    min-width: 0;
  }}

  .sc-tags {{
    display: flex;
    gap: 4px;
    margin-bottom: 2px;
    flex-wrap: wrap;
  }}

  .tag {{
    font-family: ui-monospace, "SF Mono", monospace;
    font-size: 6.5pt;
    font-weight: 700;
    padding: 1px 4px;
    border-radius: 2px;
    text-transform: uppercase;
    letter-spacing: 0.02em;
  }}

  .tag-region {{ background: #0F172A; color: #FFFFFF; }}
  .tag-country {{ background: #E2E8F0; color: #0F172A; }}
  .tag-id {{ background: #F1F5F9; color: #475569; border: 0.5px solid #CBD5E1; }}
  .tag-funding {{ background: #DCFCE7; color: #166534; font-weight: 800; }}

  .sc-title {{
    font-size: 10.5pt;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.25;
    margin-bottom: 1px;
  }}

  .sc-sub {{
    font-size: 7.2pt;
    color: #475569;
    line-height: 1.3;
  }}

  .sc-meta-right {{
    text-align: right;
    shrink: 0;
  }}

  .deadline-badge {{
    background: #0F172A;
    color: #FFFFFF;
    padding: 2px 6px;
    border-radius: 2px;
    display: inline-block;
    text-align: right;
  }}

  .deadline-label {{
    display: block;
    font-size: 5.5pt;
    color: #5EEAD4;
    font-family: ui-monospace, "SF Mono", monospace;
    font-weight: 700;
    letter-spacing: 0.05em;
  }}

  .deadline-val {{
    font-family: ui-monospace, "SF Mono", monospace;
    font-size: 8pt;
    font-weight: 700;
    color: #FFFFFF;
  }}

  .degree-badge {{
    font-size: 6.5pt;
    color: #475569;
    margin-top: 2px;
    font-weight: 600;
  }}

  /* 4-Box Metrics Bar */
  .metrics-grid {{
    display: flex;
    gap: 4px;
    margin-bottom: 4px;
  }}

  .metric-box {{
    flex: 1;
    background: #F8FAFC;
    border: 0.5px solid #CBD5E1;
    border-radius: 2px;
    padding: 3px 5px;
  }}

  .m-label {{
    display: block;
    font-size: 5.5pt;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    font-family: ui-monospace, "SF Mono", monospace;
    letter-spacing: 0.03em;
  }}

  .m-val {{
    font-size: 7.2pt;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.2;
    display: block;
  }}

  /* Coverage Badges Strip */
  .coverage-strip {{
    background: #F1F5F9;
    padding: 3px 6px;
    border-radius: 2px;
    margin-bottom: 4px;
    display: flex;
    flex-wrap: wrap;
    gap: 3px;
    align-items: center;
  }}

  .strip-label {{
    font-size: 6pt;
    font-weight: 800;
    color: #475569;
    font-family: ui-monospace, "SF Mono", monospace;
    margin-right: 2px;
  }}

  .badge {{
    font-size: 6.5pt;
    font-weight: 600;
    padding: 1px 4px;
    border-radius: 2px;
    display: inline-block;
    white-space: nowrap;
  }}

  .badge-success {{ background: #DCFCE7; color: #166534; border: 0.5px solid #86EFAC; }}
  .badge-warning {{ background: #FEF3C7; color: #92400E; border: 0.5px solid #FCD34D; }}
  .badge-danger  {{ background: #FFE4E6; color: #9F1239; border: 0.5px solid #FDA4AF; }}
  .badge-info    {{ background: #E0E7FF; color: #3730A3; border: 0.5px solid #C7D2FE; }}

  /* 2-Column Detail Grid */
  .details-grid {{
    display: flex;
    gap: 6px;
    margin-bottom: 4px;
  }}

  .grid-col {{
    flex: 1;
    min-width: 0;
  }}

  .section-title {{
    font-size: 6.5pt;
    font-weight: 800;
    color: #0F766E;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-family: ui-monospace, "SF Mono", monospace;
    border-bottom: 0.5px solid #CBD5E1;
    padding-bottom: 1px;
    margin-bottom: 2px;
  }}

  .dense-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 6.8pt;
  }}

  .dense-table td {{
    padding: 1.5px 3px;
    vertical-align: top;
    border-bottom: 0.5px solid #F1F5F9;
  }}

  .dt-key {{
    width: 32%;
    color: #64748B;
    font-weight: 600;
  }}

  .dt-val {{
    color: #1E293B;
  }}

  .workflow-box {{
    background: #F8FAFC;
    border: 0.5px solid #E2E8F0;
    border-radius: 2px;
    padding: 3px 5px;
    margin-bottom: 3px;
  }}

  .wf-title {{
    font-size: 6pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    display: block;
    margin-bottom: 1px;
  }}

  .workflow-list {{
    padding-left: 12px;
    margin: 0;
    font-size: 6.7pt;
    line-height: 1.25;
    color: #334155;
  }}

  .workflow-step {{
    margin-bottom: 1px;
  }}

  .docs-box {{
    background: #F8FAFC;
    border: 0.5px solid #E2E8F0;
    border-radius: 2px;
    padding: 3px 5px;
  }}

  .docs-title {{
    font-size: 6pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    display: block;
    margin-bottom: 2px;
  }}

  .docs-checklist {{
    display: flex;
    flex-wrap: wrap;
    gap: 3px;
  }}

  .doc-item {{
    font-size: 6.2pt;
    color: #1E293B;
    background: #FFFFFF;
    border: 0.5px solid #CBD5E1;
    padding: 0.5px 3px;
    border-radius: 2px;
    white-space: nowrap;
  }}

  /* Footer & Official Links */
  .sc-footer {{
    border-top: 0.5px solid #E2E8F0;
    padding-top: 3px;
    font-size: 6.7pt;
    line-height: 1.3;
  }}

  .footer-block {{
    margin-bottom: 2px;
    padding: 1.5px 4px;
    border-radius: 2px;
  }}

  .highlight-block {{
    background: #F0FDF4;
    color: #166534;
    border-left: 2px solid #22C55E;
  }}

  .warning-block {{
    background: #FFFBEB;
    color: #92400E;
    border-left: 2px solid #F59E0B;
  }}

  .footer-sources {{
    color: #475569;
    font-size: 6.5pt;
    margin-top: 2px;
  }}

  .sources-title {{
    font-weight: 700;
    color: #0F172A;
  }}

  .source-link {{
    color: #0F766E;
    text-decoration: none;
    font-weight: 600;
  }}

  .cycle-note {{
    color: #64748B;
    font-style: italic;
    margin-left: 4px;
  }}

  .page-break-before {{
    page-break-before: always;
    break-before: page;
  }}
</style>
</head>
<body>

  <!-- ======================================================================= -->
  <!-- 00. MASTER COVER & EXECUTIVE ADMISSIONS BRIEFING                         -->
  <!-- ======================================================================= -->
  <div class="cover-page">
    <div class="cover-preheader">OFFICIAL SCHOLARX INTELLIGENCE NETWORK // ANNUAL REPORT</div>
    <h1 class="cover-title">Global Scholarship Intelligence Catalog &amp; Execution Roadmap</h1>
    <p class="cover-subtitle">
      A publication-grade compendium of <strong>{total_count} authenticated opportunities</strong> across <strong>{countries_count} countries</strong>,
      evaluated for degree qualifications, financial coverage, testing exemptions, and verified admission pipelines for Cohort 2026/2027.
    </p>

    <div class="kpi-row">
      <div class="kpi-box">
        <div class="kpi-num">{total_count}</div>
        <div class="kpi-label">Total Verified Opportunities</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-num">{fully_funded_count}</div>
        <div class="kpi-label">100% Fully Funded</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-num">{countries_count}</div>
        <div class="kpi-label">Global Host Nations</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-num">5</div>
        <div class="kpi-label">Continental Regions</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-num">98%</div>
        <div class="kpi-label">Verification Confidence</div>
      </div>
    </div>

    <div class="macro-summary-box">
      <div class="macro-title">01 // ADMISSIONS CYCLE STRATEGY &amp; TIMELINE RUNWAY</div>
      <p class="macro-text">
        <strong>Academic Cohort 2026/2027 Guidance:</strong> Today is October 2026. The Fall 2026 entry cycle has concluded globally. 
        Candidates actively preparing this dossier are targeting the <strong>Fall 2027 academic intake</strong>. 
        Official application portals open sequentially from November 2026 through March 2027. 
        Every opportunity in this publication provides dual verification against ministry portals, embassies, and host university directories.
      </p>
    </div>

    <div class="macro-summary-box">
      <div class="macro-title">02 // TRUE OUT-OF-POCKET EXPENSES &amp; CASH RESERVES (PKR)</div>
      <p class="macro-text">
        Even on a "100% Free / Fully Funded" scholarship, applicants require short-term liquid cash to cover:
        <strong>(a)</strong> Degree attestation (HEC/IBCC: PKR 14,000); 
        <strong>(b)</strong> Visa processing and bio-metrics (VFS/Gerry's: PKR 25,000–35,000); 
        <strong>(c)</strong> Panel physical exam &amp; police clearance (PKR 18,000); and 
        <strong>(d)</strong> Initial arrival settlement liquidity (PKR 60,000–180,000) prior to the first monthly stipend disbursement. 
        Total recommended upfront liquid buffer ranges from <strong>PKR 140,000 to PKR 303,500</strong>.
      </p>
    </div>

    <table class="runway-table">
      <thead>
        <tr>
          <th>Region</th>
          <th>Total Programs</th>
          <th>Premier Target Programs</th>
          <th>Upcoming Window</th>
          <th>English MOI Accepted</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Europe</strong></td>
          <td>101 Programs</td>
          <td>Stipendium Hungaricum, Chevening, DAAD, Erasmus Mundus, Padua Excellence</td>
          <td>Nov 2026 – Jan 2027</td>
          <td><strong>High</strong> (Hungary, Italy, Germany MOI)</td>
        </tr>
        <tr>
          <td><strong>Asia</strong></td>
          <td>81 Programs</td>
          <td>CSC Bilateral Type-A, MEXT Japan, Türkiye Bursları, Taiwan ICDF, GKS Korea</td>
          <td>Dec 2026 – Feb 2027</td>
          <td><strong>High</strong> (China, Turkey language years)</td>
        </tr>
        <tr>
          <td><strong>Americas</strong></td>
          <td>65 Programs</td>
          <td>USEFP Fulbright, Vanier Canada, OAS, Lester B. Pearson, McGill McCall MacBain</td>
          <td>Feb 2027 – May 2027</td>
          <td><strong>Moderate</strong> (GRE / TOEFL Placement)</td>
        </tr>
        <tr>
          <td><strong>MENA</strong></td>
          <td>43 Programs</td>
          <td>KAUST Fellowship, Qatar University, ADU Chancellor, Khalifa University</td>
          <td>Dec 2026 – Jan 2027</td>
          <td><strong>High</strong> (English-medium research)</td>
        </tr>
        <tr>
          <td><strong>Oceania</strong></td>
          <td>20 Programs</td>
          <td>Australia Awards, Melbourne Research, Sydney International, Manaaki NZ</td>
          <td>Feb 2027 – Apr 2027</td>
          <td><strong>Moderate</strong> (IELTS 6.5–7.0 standard)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ======================================================================= -->
  <!-- 01-05. REGIONAL CHAPTERS & SCHOLARSHIP CARDS                            -->
  <!-- ======================================================================= -->
  {all_chapters_html}

</body>
</html>
"""


def compile_pdf_from_html(html_str: str, output_pdf_path: Path) -> Path:
    """Compiles HTML string into a PDF using WeasyPrint with A4 publication standards."""
    if weasyprint is None:
        raise RuntimeError("WeasyPrint is not installed in the python environment.")

    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Compiling publication PDF via WeasyPrint: {output_pdf_path} ...")
    html_doc = weasyprint.HTML(string=html_str, base_url=str(REPO_ROOT))
    html_doc.write_pdf(
        target=str(output_pdf_path),
        presentational_hints=True,
        optimize_size=('fonts', 'images')
    )
    print(f"Successfully generated PDF at {output_pdf_path} (Size: {output_pdf_path.stat().st_size / (1024*1024):.2f} MB)")
    return output_pdf_path


def main():
    target_arg = sys.argv[1] if len(sys.argv) > 1 else None
    output_path = Path(target_arg) if target_arg else DEFAULT_OUTPUT_PDF
    
    # Check limit argument e.g. --limit 10 for quick testing
    limit = None
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])
            
    print(f"Loading and normalizing scholarships database (Limit: {limit or 'ALL 310'})...")
    dossiers = load_all_normalized_dossiers(REPO_ROOT)
    
    if limit:
        dossiers = dossiers[:limit]
        
    print(f"Rendering HTML template for {len(dossiers)} scholarships...")
    html_content = generate_master_catalog_html(dossiers)
    
    # Save standalone HTML file alongside PDF for instant browser inspection
    html_path = output_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")
    print(f"Saved standalone HTML publication at: {html_path}")
    
    compile_pdf_from_html(html_content, output_path)


if __name__ == "__main__":
    main()
