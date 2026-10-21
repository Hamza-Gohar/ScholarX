"""
ScholarX Publication-Grade PDF Generator
Enterprise-grade PDF Generator compiling verified scholarship intelligence dossiers.
Features anti-AI slop typography, high information density, and complete coverage across
the ScholarX database using modern WeasyPrint CSS Paged Media.
"""

import os
import sys
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "backend"))

from utils.dossier_normalizer import load_all_normalized_dossiers
from generate_all_scholarships_catalog import (
    generate_master_catalog_html,
    compile_pdf_from_html,
)

DEFAULT_OUTPUT_PATH = "/home/hamza/.gemini/antigravity/brain/412ce3ab-ae9a-433b-a9b1-e3340a2b51fd/ScholarX_Pakistan_Scholarship_Dossier_2026_2027.pdf"
MASTER_GLOBAL_OUTPUT_PATH = REPO_ROOT / "data" / "ScholarX_Global_Master_Scholarship_Dossier_2026_2027.pdf"


def generate_pdf(output_path: Optional[str] = None, limit: Optional[int] = None) -> str:
    target_path = Path(output_path or os.environ.get("SCHOLARX_PDF_OUTPUT") or DEFAULT_OUTPUT_PATH)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading scholarship intelligence from database (Total: 310)...")
    dossiers = load_all_normalized_dossiers(REPO_ROOT)
    
    if limit and limit > 0:
        dossiers = dossiers[:limit]
        print(f"Limiting to first {limit} scholarships for targeted briefing.")

    print(f"Compiling publication HTML for {len(dossiers)} scholarships with enterprise CSS...")
    html_content = generate_master_catalog_html(
        dossiers,
        title="ScholarX Official Scholarship Intelligence Dossier"
    )

    # Save HTML alongside PDF
    html_path = target_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")
    print(f"Saved standalone HTML view at: {html_path}")

    # Compile vector PDF via WeasyPrint
    compile_pdf_from_html(html_content, target_path)
    print(f"Publication-Grade PDF successfully generated at {target_path}")
    return str(target_path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else None
    lim = None
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            lim = int(sys.argv[idx + 1])
            
    generate_pdf(out, limit=lim)
