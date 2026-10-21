"""
Script to assemble and write ScholarX Exhibition Slides.
Authentic Human & Editorial Edition with Pure Pitch-Black OLED Canvas (#000000)
"""

import os
import shutil
import sys

# Add scripts directory to path
sys.path.insert(0, '/mnt/windows/AntiGravity/SCHOLARX/scripts')
import generate_slide_content

OUTPUT_HTML = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/index.html"
FRONTEND_HTML = "/mnt/windows/AntiGravity/SCHOLARX/frontend/public/slides/index.html"
GENERATE_SCRIPT = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/generate_slides.py"

SLIDES = [
    generate_slide_content.get_slide_01(),
    generate_slide_content.get_slide_02(),
    generate_slide_content.get_slide_03(),
    generate_slide_content.get_slide_04(),
    generate_slide_content.get_slide_05(),
    generate_slide_content.get_slide_06(),
    generate_slide_content.get_slide_07(),
    generate_slide_content.get_slide_08(),
    generate_slide_content.get_slide_09(),
    generate_slide_content.get_slide_10(),
]

ALL_SLIDES_HTML = "\n".join(SLIDES)

HTML_DOC = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ScholarX — Autonomous Scholarship Intelligence</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-canvas: #000000;
      --bg-panel: #0A0A0C;
      --bg-card: #111114;
      --bg-card-subtle: #16161A;

      --border-strong: #27272A;
      --border-subtle: #1E1E22;
      --border-muted: #141416;

      --text-white: #FFFFFF;
      --text-main: #F4F4F5;
      --text-muted: #A1A1AA;

      --accent-green: #10B981;
      --accent-blue: #38BDF8;
      --accent-slate: #94A3B8;
      --accent-amber: #F59E0B;
      --accent-rose: #EF4444;

      --font-family: 'Manrope', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      --slide-w: 1920px;
      --slide-h: 1080px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: var(--font-family);
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      -webkit-font-smoothing: antialiased;
    }}

    /* TOP TOOLBAR */
    .deck-toolbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 52px;
      background: rgba(5, 5, 6, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 36px;
      z-index: 1000;
      font-size: 13.5px;
      font-weight: 500;
    }}

    .brand-title {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 15px;
      color: var(--text-white);
    }}
    .brand-dot {{
      width: 8px;
      height: 8px;
      background: var(--accent-green);
      border-radius: 50%;
    }}

    .toolbar-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .nav-btn {{
      background: #121215;
      color: var(--text-main);
      border: 1px solid var(--border-strong);
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-family: var(--font-family);
      font-size: 13px;
      font-weight: 600;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .nav-btn:hover {{
      background: #1E1E24;
      color: var(--text-white);
      border-color: #3F3F46;
    }}
    .nav-btn.primary {{
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.4);
      color: var(--accent-green);
    }}
    .nav-btn.primary:hover {{
      background: var(--accent-green);
      color: #000000;
      border-color: var(--accent-green);
    }}

    .slide-counter {{
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      min-width: 85px;
      text-align: center;
    }}
    .counter-highlight {{
      color: var(--text-white);
      font-weight: 700;
    }}

    /* VIEWPORT STAGE */
    .viewport-stage {{
      margin-top: 52px;
      width: 100vw;
      height: calc(100vh - 52px);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}

    #presentation-deck {{
      width: var(--slide-w);
      height: var(--slide-h);
      transform-origin: center center;
      position: relative;
    }}

    /* SLIDE BASE STYLES */
    .slide {{
      width: var(--slide-w);
      height: var(--slide-h);
      position: absolute;
      top: 0;
      left: 0;
      background: var(--bg-canvas);
      display: none;
      flex-direction: column;
      padding: 60px 76px 40px 76px;
      border: 1px solid var(--border-subtle);
      box-sizing: border-box;
      overflow: hidden;
    }}

    .slide.active {{
      display: flex;
    }}

    /* CORNER PUSH-PIN CROSSHAIRS FOR HARDBOARD MOUNTING */
    .pin-mark {{
      position: absolute;
      width: 20px;
      height: 20px;
      pointer-events: none;
      z-index: 10;
    }}
    .pin-mark::before, .pin-mark::after {{
      content: '';
      position: absolute;
      background: #3F3F46;
    }}
    .pin-mark::before {{
      top: 9px;
      left: 0;
      width: 20px;
      height: 2px;
    }}
    .pin-mark::after {{
      top: 0;
      left: 9px;
      width: 2px;
      height: 20px;
    }}
    .pin-tl {{ top: 20px; left: 20px; }}
    .pin-tr {{ top: 20px; right: 20px; }}
    .pin-bl {{ bottom: 20px; left: 20px; }}
    .pin-br {{ bottom: 20px; right: 20px; }}

    /* SLIDE HEADER */
    .slide-header {{
      margin-bottom: 22px;
      position: relative;
      z-index: 5;
    }}

    .slide-headline {{
      font-size: 40px;
      font-weight: 800;
      color: var(--text-white);
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 8px;
    }}

    .slide-subheadline {{
      font-size: 17.5px;
      font-weight: 500;
      color: var(--text-muted);
      line-height: 1.45;
      max-width: 1400px;
    }}

    /* SLIDE CANVAS */
    .slide-canvas {{
      flex: 1;
      display: flex;
      flex-direction: column;
      position: relative;
      z-index: 5;
      min-height: 0;
    }}

    /* SLIDE FOOTER */
    .slide-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      padding-top: 14px;
      margin-top: 16px;
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .footer-left {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .footer-brand {{
      color: var(--text-white);
      font-weight: 700;
      letter-spacing: -0.01em;
    }}
    .footer-dot {{
      width: 4px;
      height: 4px;
      background: #52525B;
      border-radius: 50%;
    }}
    .footer-num {{
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--text-white);
      font-size: 14px;
    }}

    /* COMMON CARD STYLES (No thick top borders that clash with rounded corners) */
    .card-box {{
      background: var(--bg-panel);
      border: 1px solid var(--border-strong);
      border-radius: 12px;
      padding: 24px;
      display: flex;
      flex-direction: column;
    }}
    .card-title {{
      font-size: 19px;
      font-weight: 800;
      color: var(--text-white);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .card-desc {{
      font-size: 14.5px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* BADGES */
    .badge-tag {{
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      width: fit-content;
    }}
    .badge-green {{
      background: rgba(16, 185, 129, 0.12);
      color: var(--accent-green);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    .badge-slate {{
      background: rgba(148, 163, 184, 0.12);
      color: var(--accent-slate);
      border: 1px solid rgba(148, 163, 184, 0.3);
    }}
    .badge-blue {{
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-blue);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}
    .badge-amber {{
      background: rgba(245, 158, 11, 0.12);
      color: var(--accent-amber);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .badge-rose {{
      background: rgba(239, 68, 68, 0.12);
      color: var(--accent-rose);
      border: 1px solid rgba(239, 68, 68, 0.3);
    }}

    /* PRINT STYLES FOR PDF EXPORT */
    @media print {{
      body {{
        background: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
      }}
      .deck-toolbar {{
        display: none !important;
      }}
      .viewport-stage {{
        margin-top: 0 !important;
        height: auto !important;
        width: 100% !important;
        display: block !important;
      }}
      #presentation-deck {{
        transform: none !important;
        width: 1920px !important;
        height: auto !important;
        display: block !important;
      }}
      .slide {{
        display: flex !important;
        position: relative !important;
        width: 1920px !important;
        height: 1080px !important;
        page-break-after: always !important;
        break-after: page !important;
        border: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- TOP TOOLBAR -->
  <header class="deck-toolbar">
    <div class="brand-title">
      <div class="brand-dot"></div>
      <span>ScholarX — Autonomous Scholarship Intelligence</span>
    </div>

    <div class="toolbar-actions">
      <span class="slide-counter"><span class="counter-highlight" id="curr-num">1</span> of 10</span>
      <button class="nav-btn" onclick="prevSlide()" title="Previous slide (Left Arrow)">Previous</button>
      <button class="nav-btn" onclick="nextSlide()" title="Next slide (Right Arrow / Space)">Next</button>
      <button class="nav-btn" onclick="toggleFullscreen()" title="Fullscreen (F key)">Fullscreen</button>
      <button class="nav-btn primary" onclick="window.print()" title="Print / Save to PDF (P key)">Print Slides (PDF)</button>
    </div>
  </header>

  <!-- VIEWPORT STAGE -->
  <main class="viewport-stage">
    <div id="presentation-deck">
{ALL_SLIDES_HTML}
    </div>
  </main>

  <!-- PRESENTATION SCRIPT -->
  <script>
    let currentSlide = 1;
    const totalSlides = 10;
    const deck = document.getElementById('presentation-deck');
    const currNum = document.getElementById('curr-num');

    function fitDeck() {{
      const availW = window.innerWidth;
      const availH = window.innerHeight - 52;
      const scale = Math.min(availW / 1920, availH / 1080);
      deck.style.transform = `scale(${{scale}})`;
    }}

    window.addEventListener('resize', fitDeck);
    fitDeck();

    function showSlide(index) {{
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;

      for (let i = 1; i <= totalSlides; i++) {{
        const slide = document.getElementById('slide-' + i);
        if (slide) {{
          if (i === index) {{
            slide.classList.add('active');
          }} else {{
            slide.classList.remove('active');
          }}
        }}
      }}
      currentSlide = index;
      currNum.textContent = index;
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        showSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        showSlide(currentSlide - 1);
      }}
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{}});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === ' ') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'p' || e.key === 'P') {{
        window.print();
      }} else if (e.key >= '1' && e.key <= '9') {{
        showSlide(parseInt(e.key));
      }} else if (e.key === '0') {{
        showSlide(10);
      }}
    }});
  </script>
</body>
</html>
"""

# Write to exhibition_slides/index.html
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(HTML_DOC)
print(f"Generated {OUTPUT_HTML} (size: {len(HTML_DOC)} bytes)")

# Ensure destination directory for frontend exists
os.makedirs(os.path.dirname(FRONTEND_HTML), exist_ok=True)
with open(FRONTEND_HTML, "w", encoding="utf-8") as f:
    f.write(HTML_DOC)
print(f"Copied to {FRONTEND_HTML}")

# Also update exhibition_slides/generate_slides.py to keep it in sync
with open(GENERATE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(f'''"""
ScholarX Science Exhibition Slide Presentation Generator
Generated automatically from build_full_slides.py
"""

import os
import shutil

OUTPUT_DIR = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides"
FRONTEND_SLIDES_DIR = "/mnt/windows/AntiGravity/SCHOLARX/frontend/public/slides"

HTML_CONTENT = \'\'\'{HTML_DOC}\'\'\'

def main():
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Successfully generated: {{index_path}}")

    os.makedirs(FRONTEND_SLIDES_DIR, exist_ok=True)
    frontend_path = os.path.join(FRONTEND_SLIDES_DIR, "index.html")
    with open(frontend_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Successfully synced: {{frontend_path}}")

if __name__ == "__main__":
    main()
''')
print(f"Updated generator script: {GENERATE_SCRIPT}")
