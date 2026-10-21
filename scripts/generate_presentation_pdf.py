#!/usr/bin/env python3
"""
ScholarX Presentation Deck PDF Generator
Renders all 10 slides in 1920x1080 high-resolution using headless Firefox in clean export mode,
then compiles them into a landscape presentation PDF.
"""

import os
import sys
import tempfile
import subprocess
from PIL import Image

BASE_DIR = "/mnt/windows/AntiGravity/SCHOLARX"
HTML_PATH = f"file://{BASE_DIR}/exhibition_slides/index.html"
RENDERS_DIR = f"{BASE_DIR}/exhibition_slides/renders"
PDF_PATH = f"{BASE_DIR}/exhibition_slides/ScholarX_Exhibition_Deck.pdf"
FRONTEND_PDF = f"{BASE_DIR}/frontend/public/ScholarX_Exhibition_Deck.pdf"
SLIDES_PUBLIC_PDF = f"{BASE_DIR}/frontend/public/slides/ScholarX_Exhibition_Deck.pdf"
BRAIN_PDF = "/home/hamza/.gemini/antigravity/brain/ae096eb2-fe75-42c2-b2b8-7f8470fe8900/ScholarX_Exhibition_Deck.pdf"

TOTAL_SLIDES = 10

def main():
    os.makedirs(RENDERS_DIR, exist_ok=True)
    slide_images = []

    print(f"=== Rendering {TOTAL_SLIDES} Slides to 1920x1080 High-Res Images ===")
    
    for i in range(1, TOTAL_SLIDES + 1):
        out_img = os.path.join(RENDERS_DIR, f"slide_{i:02d}.png")
        tmp_prof = tempfile.mkdtemp()
        url = f"{HTML_PATH}?slide={i}&export=1"
        cmd = [
            "firefox",
            "--headless",
            "--profile", tmp_prof,
            "--screenshot", out_img,
            "--window-size=1920,1080",
            url
        ]
        
        print(f"[{i:02d}/{TOTAL_SLIDES}] Capturing Slide {i:02d}...", end=" ", flush=True)
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
            if os.path.exists(out_img) and os.path.getsize(out_img) > 10000:
                print(f"DONE ({os.path.getsize(out_img):,} bytes)")
                slide_images.append(out_img)
            else:
                print(f"FAILED (Empty or missing output)")
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            subprocess.run(["rm", "-rf", tmp_prof])

    if len(slide_images) != TOTAL_SLIDES:
        print(f"ERROR: Expected {TOTAL_SLIDES} slides, but only captured {len(slide_images)}")
        sys.exit(1)

    print(f"\n=== Assembling {len(slide_images)} Slides into Master Landscape PDF ===")
    pil_images = []
    for img_path in slide_images:
        img = Image.open(img_path).convert("RGB")
        pil_images.append(img)

    # Save to Master PDF
    first_image = pil_images[0]
    first_image.save(
        PDF_PATH,
        save_all=True,
        append_images=pil_images[1:],
        resolution=150.0,
        quality=95
    )
    print(f"  -> Generated Master PDF: {PDF_PATH} ({os.path.getsize(PDF_PATH):,} bytes)")

    # Copy to destinations
    import shutil
    os.makedirs(os.path.dirname(FRONTEND_PDF), exist_ok=True)
    shutil.copy2(PDF_PATH, FRONTEND_PDF)
    print(f"  -> Copied to: {FRONTEND_PDF}")

    os.makedirs(os.path.dirname(SLIDES_PUBLIC_PDF), exist_ok=True)
    shutil.copy2(PDF_PATH, SLIDES_PUBLIC_PDF)
    print(f"  -> Copied to: {SLIDES_PUBLIC_PDF}")

    os.makedirs(os.path.dirname(BRAIN_PDF), exist_ok=True)
    shutil.copy2(PDF_PATH, BRAIN_PDF)
    print(f"  -> Copied to Brain: {BRAIN_PDF}")

    print("\n[SUCCESS] ScholarX Presentation PDF successfully compiled and published.")

if __name__ == "__main__":
    main()
