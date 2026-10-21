#!/usr/bin/env python3
"""
ScholarX Korean Minimalist Presentation Builder
One-command builder that compiles:
- Native PowerPoint Presentation (.pptx)
- Interactive Responsive Web Deck (index.html)
- High-Resolution Printable PDF (.pdf)
- PNG Slide Renders (renders/slide-*.png) for instant visual QA
"""

import os
import sys
import subprocess
import time

# Ensure exhibition_slides directory is in path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from deck_manifest import SLIDES, DECK_METADATA
from engine.pptx_builder import generate_pptx_deck
from engine.html_builder import generate_html_deck


def main():
    print("=" * 65)
    print(" 🌸 ScholarX — Minimalist Korean Aesthetic Presentation Builder")
    print("=" * 65)
    
    template_pptx = os.path.join(BASE_DIR, "Minimalist Korean Aesthetic Pitch Deck XL by Slidesgo.pptx")
    out_pptx = os.path.join(BASE_DIR, "ScholarX_Korean_Deck.pptx")
    out_html = os.path.join(BASE_DIR, "index.html")
    renders_dir = os.path.join(BASE_DIR, "renders")
    os.makedirs(renders_dir, exist_ok=True)

    if not os.path.exists(template_pptx):
        print(f"❌ Error: Reference template not found at: {template_pptx}")
        sys.exit(1)

    t0 = time.time()

    # Step 1: Generate Native PPTX
    print("\n[1/4] Generating Native PowerPoint (.pptx)...")
    generate_pptx_deck(template_pptx, out_pptx, SLIDES)

    # Step 2: Generate Interactive HTML Deck
    print("\n[2/4] Generating Interactive Web Deck (index.html)...")
    generate_html_deck(SLIDES, out_html)

    # Step 3: Convert PPTX to PDF via LibreOffice
    print("\n[3/4] Exporting High-Resolution PDF via LibreOffice...")
    cmd_pdf = ["libreoffice", "--headless", "--convert-to", "pdf", out_pptx, "--outdir", BASE_DIR]
    res_pdf = subprocess.run(cmd_pdf, capture_output=True, text=True)
    if res_pdf.returncode != 0:
        print(f"⚠️ Warning: LibreOffice PDF conversion returned code {res_pdf.returncode}: {res_pdf.stderr}")
    else:
        print("  -> PDF export successful: ScholarX_Korean_Deck.pdf")

    # Step 4: Render High-Resolution PNG Images via pdftoppm
    pdf_path = os.path.join(BASE_DIR, "ScholarX_Korean_Deck.pdf")
    if os.path.exists(pdf_path):
        print("\n[4/4] Rendering PNG Slide Images (150 DPI)...")
        # Remove old slide renders to keep fresh
        for f in os.listdir(renders_dir):
            if f.startswith("slide-") and f.endswith(".png"):
                try:
                    os.remove(os.path.join(renders_dir, f))
                except Exception:
                    pass

        cmd_ppm = ["pdftoppm", "-png", "-r", "150", pdf_path, os.path.join(renders_dir, "slide")]
        res_ppm = subprocess.run(cmd_ppm, capture_output=True, text=True)
        if res_ppm.returncode == 0:
            rendered = sorted([f for f in os.listdir(renders_dir) if f.startswith("slide-") and f.endswith(".png")])
            print(f"  -> Generated {len(rendered)} PNG slide captures in {renders_dir}/")
        else:
            print(f"⚠️ Warning: pdftoppm failed: {res_ppm.stderr}")

    elapsed = round(time.time() - t0, 2)
    print("\n" + "=" * 65)
    print(f"✨ Build Complete in {elapsed}s!")
    print(f"📁 Deliverables:")
    print(f"   • PPTX: {out_pptx}")
    print(f"   • HTML: {out_html}")
    print(f"   • PDF:  {pdf_path}")
    print(f"   • PNGs: {renders_dir}/")
    print("=" * 65)


if __name__ == "__main__":
    main()
