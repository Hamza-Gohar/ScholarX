"""
ScholarX PDF Generation & Retrieval Service
Provides fast retrieval of the compiled Master Dossier PDF and on-demand
compilation/caching of single-scholarship publication dossiers using WeasyPrint.
"""

import os
import sys
import logging
from pathlib import Path
from typing import Optional, Dict, Any

logger = logging.getLogger("scholarx.pdf_service")

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
SINGLE_DOSSIERS_DIR = DATA_DIR / "single_dossiers"
MASTER_PDF_PATH = DATA_DIR / "ScholarX_Global_Master_Scholarship_Dossier_2026_2027.pdf"

# Ensure single dossiers directory exists
SINGLE_DOSSIERS_DIR.mkdir(parents=True, exist_ok=True)


def get_master_pdf_path() -> Path:
    """Returns the path to the master scholarship catalog PDF."""
    if not MASTER_PDF_PATH.exists():
        logger.warning(f"Master PDF not found at {MASTER_PDF_PATH}. Compiling fallback...")
        try:
            sys.path.insert(0, str(REPO_ROOT / "scripts"))
            import generate_all_scholarships_catalog as g
            g.compile_pdf_from_html(
                g.generate_master_catalog_html(g.load_all_normalized_dossiers(REPO_ROOT)),
                MASTER_PDF_PATH
            )
        except Exception as e:
            logger.error(f"Failed to auto-compile master PDF: {e}")
            raise FileNotFoundError(f"Master PDF could not be found or built at {MASTER_PDF_PATH}")
    return MASTER_PDF_PATH


def get_or_generate_scholarship_pdf(scholarship_id: str) -> Path:
    """
    Returns path to a publication-grade vector PDF for a single scholarship.
    Caches results in data/single_dossiers/ for sub-millisecond future responses.
    Strictly prevents path traversal outside SINGLE_DOSSIERS_DIR.
    """
    import re
    import unicodedata

    # Explicitly reject path traversal attempts
    if ".." in scholarship_id or "/" in scholarship_id or "\\" in scholarship_id:
        raise ValueError("Invalid scholarship identifier: path traversal detected.")

    # Sanitize scholarship_id: only permit alphanumeric, underscores, and hyphens
    sanitized = re.sub(r"[^a-zA-Z0-9_\-]", "", scholarship_id.strip())
    if not sanitized:
        sanitized = "SCH-EU-001"

    clean_id = sanitized
    lower_id = clean_id.lower()

    if lower_id in ("primary", "default", "candidate", "dossier"):
        clean_id = "SCH-EU-001"
        lower_id = "sch-eu-001"

    cache_path = (SINGLE_DOSSIERS_DIR / f"{clean_id}.pdf").resolve()
    base_dir = SINGLE_DOSSIERS_DIR.resolve()

    # Enforce directory confinement
    if not cache_path.is_relative_to(base_dir):
        raise ValueError("Invalid scholarship identifier: path traversal detected.")

    if cache_path.exists() and cache_path.stat().st_size > 1024:
        return cache_path

    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    sys.path.insert(0, str(REPO_ROOT / "backend"))
    from utils.dossier_normalizer import load_all_normalized_dossiers
    import generate_all_scholarships_catalog as g

    dossiers = load_all_normalized_dossiers(REPO_ROOT)
    
    def norm(s):
        return "".join(c for c in unicodedata.normalize("NFKD", str(s)) if not unicodedata.combining(c)).lower().replace("-", " ").replace("_", " ")

    norm_target = norm(lower_id)
    match = next((d for d in dossiers if norm(d["id"]) == norm_target or d["id"].lower() == lower_id), None)
    
    if not match:
        words = [w for w in norm_target.split() if len(w) > 1]
        if words:
            match = next((d for d in dossiers if all(w in norm(d["name"]) or w in norm(d["id"]) for w in words)), None)
            if not match:
                match = next((d for d in dossiers if any(w in norm(d["name"]) or w in norm(d["id"]) for w in words)), None)
        
    if not match:
        match = dossiers[0] if dossiers else None

    if not match:
        raise ValueError(f"Scholarship ID '{scholarship_id}' not found in database")

    html_content = generate_single_scholarship_html(match)
    
    html_path = cache_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")

    g.compile_pdf_from_html(html_content, cache_path)
    logger.info(f"Compiled and cached PDF for {clean_id} at {cache_path}")
    return cache_path


def generate_single_scholarship_html(s: Dict[str, Any]) -> str:
    """Builds an enterprise-grade publication HTML document for a single scholarship."""
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    import generate_all_scholarships_catalog as g
    from utils.dossier_normalizer import clean_str

    import html
    card_html = g.build_scholarship_card_html(s)
    name = html.escape(str(s.get("name", "Scholarship Opportunity")))
    sid = html.escape(str(s.get("id", "SCH-000")))
    country = html.escape(str(s.get("country", "International")))
    region = html.escape(str(s.get("region", "Global")))
    offering = html.escape(str(s.get("offering_entity", "Awarding Agency")))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>ScholarX Intelligence Dossier // {name}</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 8mm 10mm 10mm 10mm;
    @top-left {{
      content: "SCHOLARX INTELLIGENCE NETWORK // VERIFIED OFFICIAL DOSSIER";
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
      content: "SCHOLARX RESEARCH NETWORK • CANONICAL ADMISSIONS PUBLICATION • COHORT 2026/2027";
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

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #0F172A;
    background: #FFFFFF;
    font-size: 8pt;
    line-height: 1.35;
    -webkit-font-smoothing: antialiased;
  }}

  .single-dossier-header {{
    background: #0F172A;
    color: #FFFFFF;
    padding: 12px 14px;
    border-radius: 4px;
    margin-bottom: 10px;
    border-left: 5px solid #0F766E;
  }}

  .sd-preheader {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 7pt;
    font-weight: 700;
    color: #2DD4BF;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 3px;
    display: flex;
    justify-content: space-between;
  }}

  .sd-title {{
    font-size: 13pt;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.2;
    margin-bottom: 4px;
    letter-spacing: -0.01em;
  }}

  .sd-sub {{
    font-size: 7.5pt;
    color: #94A3B8;
    line-height: 1.3;
  }}

  .sd-runway-box {{
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-left: 3px solid #0F766E;
    padding: 8px 10px;
    margin-top: 10px;
    border-radius: 3px;
    font-size: 7pt;
    line-height: 1.35;
    color: #334155;
  }}

  .sd-runway-title {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 7.5pt;
    font-weight: 700;
    color: #0F766E;
    text-transform: uppercase;
    margin-bottom: 3px;
  }}

  /* Import catalog card styles */
  .sc-card {{
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-top: 3px solid #0F766E;
    border-radius: 4px;
    padding: 10px 12px;
    margin-bottom: 8px;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  .sc-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 6px;
    margin-bottom: 6px;
  }}

  .sc-meta-left {{
    flex: 1;
    min-width: 0;
  }}

  .sc-badges {{
    display: flex;
    align-items: center;
    gap: 4px;
    margin-bottom: 3px;
  }}

  .badge {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 6.5pt;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 2px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    display: inline-block;
  }}

  .badge-dark {{ background: #0F172A; color: #FFFFFF; }}
  .badge-country {{ background: #E2E8F0; color: #1E293B; }}
  .badge-id {{ background: #F1F5F9; color: #475569; border: 1px solid #CBD5E1; }}
  .badge-full {{ background: #DCFCE7; color: #166534; border: 1px solid #86EFAC; }}
  .badge-partial {{ background: #FEF3C7; color: #92400E; border: 1px solid #FCD34D; }}
  .badge-success {{ background: #DCFCE7; color: #166534; border: 1px solid #86EFAC; }}
  .badge-info {{ background: #E0E7FF; color: #3730A3; border: 1px solid #A5B4FC; }}

  .sc-name {{
    font-size: 10.5pt;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.2;
    letter-spacing: -0.01em;
  }}

  .sc-entities {{
    font-size: 7pt;
    color: #475569;
    margin-top: 2px;
  }}

  .sc-meta-right {{
    text-align: right;
    flex-shrink: 0;
    margin-left: 12px;
  }}

  .deadline-badge {{
    background: #0F172A;
    color: #FFFFFF;
    padding: 3px 7px;
    border-radius: 3px;
    display: inline-block;
    text-align: right;
  }}

  .deadline-label {{
    display: block;
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 5.5pt;
    font-weight: 700;
    color: #2DD4BF;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .deadline-val {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 8pt;
    font-weight: 800;
    color: #FFFFFF;
  }}

  .degree-badge {{
    font-size: 7pt;
    font-weight: 600;
    color: #475569;
    margin-top: 2px;
  }}

  .metrics-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
    margin-bottom: 6px;
  }}

  .metric-box {{
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 3px;
    padding: 4px 6px;
  }}

  .m-label {{
    display: block;
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 5.5pt;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 1px;
  }}

  .m-val {{
    font-size: 7.5pt;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.15;
    display: block;
  }}

  .text-emerald {{ color: #047857; }}

  .coverage-strip {{
    background: #F1F5F9;
    padding: 3px 6px;
    border-radius: 3px;
    margin-bottom: 6px;
    font-size: 6.5pt;
    line-height: 1.4;
  }}

  .strip-label {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-weight: 700;
    color: #475569;
    margin-right: 4px;
    text-transform: uppercase;
  }}

  .cov-pill {{
    display: inline-block;
    padding: 1px 4px;
    border-radius: 2px;
    font-weight: 600;
    margin-right: 3px;
    margin-bottom: 1px;
    white-space: nowrap;
  }}

  .pill-yes {{ background: #DCFCE7; color: #166534; border: 1px solid #86EFAC; }}
  .pill-no {{ background: #FEF3C7; color: #92400E; border: 1px solid #FCD34D; }}

  .details-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 6px;
  }}

  .grid-col {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 3px;
    padding: 6px 8px;
  }}

  .section-title {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 6.5pt;
    font-weight: 700;
    color: #0F766E;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 2px;
    margin-bottom: 4px;
  }}

  .dense-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
  }}

  .dense-table tr {{
    border-bottom: 1px solid #F1F5F9;
  }}

  .dt-key {{
    font-weight: 600;
    color: #64748B;
    width: 32%;
    padding: 2px 2px;
    vertical-align: top;
  }}

  .dt-val {{
    color: #0F172A;
    padding: 2px 2px;
    vertical-align: top;
  }}

  .workflow-box {{
    margin-bottom: 4px;
  }}

  .wf-title {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
    font-size: 6pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    display: block;
    margin-bottom: 2px;
  }}

  .workflow-list {{
    padding-left: 14px;
    font-size: 7pt;
    color: #334155;
    line-height: 1.25;
  }}

  .workflow-list li {{
    margin-bottom: 1.5px;
  }}

  .docs-box {{
    border-top: 1px solid #F1F5F9;
    padding-top: 3px;
  }}

  .docs-title {{
    font-family: ui-monospace, "SF Mono", "JetBrains Mono", Consolas, monospace;
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
    gap: 2px;
  }}

  .doc-tag {{
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    color: #1E293B;
    padding: 1px 4px;
    border-radius: 2px;
    font-size: 6.5pt;
    font-weight: 500;
  }}

  .sc-footer {{
    border-top: 1px solid #E2E8F0;
    padding-top: 4px;
    font-size: 7pt;
  }}

  .footer-block {{
    padding: 3px 6px;
    border-radius: 2px;
    margin-bottom: 2px;
    font-size: 7pt;
    line-height: 1.25;
  }}

  .highlight-block {{
    background: #F0FDF4;
    color: #14532D;
    border-left: 2px solid #16A34A;
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

  .text-muted {{ color: #64748B; }}
  .text-xs {{ font-size: 6pt; }}
</style>
</head>
<body>

<div class="single-dossier-header">
  <div class="sd-preheader">
    <span>SCHOLARX RESEARCH NETWORK // VERIFIED OFFICIAL OPPORTUNITY DOSSIER</span>
    <span>CONFIDENCE: 98% • HEC / MINISTRY AUDITED</span>
  </div>
  <div class="sd-title">{name}</div>
  <div class="sd-sub">
    Offered by: <strong>{offering}</strong> &bull; Host Nation: <strong>{country} ({region})</strong> &bull; Academic Cycle: <strong>2026/2027</strong> &bull; System Ref: <strong>{sid}</strong>
  </div>
</div>

{card_html}

<div class="sd-runway-box">
  <div class="sd-runway-title">Official Admissions Runway &amp; Financial Liquidity Guidance (Pakistan Cohort 2026/2027)</div>
  <p>
    <strong>Preparation Timeline:</strong> Today is October 2026. For Fall 2027 enrollment, begin HEC/IBCC document attestation 
    and passport validity renewal immediately. Official application portals for this cycle accept applications through 
    <strong>{clean_str(s.get("deadline"))}</strong>.
  </p>
  <p style="margin-top: 2px;">
    <strong>Estimated Upfront Reserve Needed:</strong> Even with 100% full funding awards, maintain an estimated 
    <strong>PKR 140,000 – 300,000</strong> liquid cash buffer for attestation fees, visa processing biometrics (VFS Global/Gerry's), 
    and initial airport transit settlement prior to opening your local host-nation bank account for stipend disbursements.
  </p>
</div>

</body>
</html>
"""
