# ⚙️ Engine Architecture & Compilation Pipeline

This document explains the internal mechanics of the **Korean Minimalist Presentation Engine**, detailing how it manipulates OpenXML presentations, generates pixel-perfect HTML5/SVG web decks, and compiles vector PDFs in headless environments.

---

## 1. High-Level Compilation Flow

```
                  +----------------------+
                  |   deck_manifest.py   |
                  +----------+-----------+
                             |
             +---------------+---------------+
             v                               v
    +-----------------+             +-----------------+
    | pptx_builder.py |             | html_builder.py |
    +--------+--------+             +--------+--------+
             |                               |
             v                               v
  ScholarX_Korean_Deck.pptx              index.html
             |
             v (LibreOffice Headless)
  ScholarX_Korean_Deck.pdf
             |
             v (pdftoppm 150 DPI)
   renders/slide-*.png
```

---

## 2. PPTX Engine (`pptx_builder.py`)

Generating native PowerPoint presentations that look professionally designed is notoriously difficult because generating complex vector bezier shapes from scratch programmatically produces flat, uninspired art.

The engine solves this using **Master Template Layout Cloning**:

### 2.1 The Reference Template
The engine uses `Minimalist Korean Aesthetic Pitch Deck XL by Slidesgo.pptx`, which contains 54 distinct master layouts with:
- 10+ layered DrawingML `custGeom` vector curves.
- Translucent alpha blending (`46%` terracotta, `30%` sage, `50%` oatmeal).
- Built-in theme fonts and palettes.

### 2.2 XML Part Preservation & Layout Pruning
If you delete slides using naive `prs.slides.add_slide()`, python-pptx can duplicate package parts (`ppt/slides/slide1.xml`), resulting in corrupted `.pptx` archives.

The engine avoids this by pruning the slide ID list (`_sldIdLst`) directly:

```python
prs = pptx.Presentation(template_path)

# Map desired archetypes to specific template slide indices:
# 0: Title, 15: Two-Col, 6: Title & Two-Col, 34: Matrix, 2: 4-Pebble, 26: 4-Cards, 25: Timeline, 12: 3-Col
chosen_indices = [0, 15, 6, 34, 2, 26, 25, 12]

sldIdLst = prs.slides._sldIdLst
all_sldIds = list(sldIdLst)

# Remove all unselected slide IDs from the presentation XML
for idx, sldId in enumerate(all_sldIds):
    if idx not in chosen_indices:
        sldIdLst.remove(sldId)
```

### 2.3 Non-Destructive Content Clearing
After pruning, exactly 8 slides remain. The engine then strips out the default placeholder text while leaving the slide's master background layers and relationships intact:

```python
for shape in list(slide.shapes):
    sp = shape._element
    sp.getparent().remove(sp)
```

### 2.4 DrawingML Shape Injection
New shapes and text frames are added using exact mathematical positioning:
- **Rounded Rectangles**: `slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)`.
- **Corner Curvature**: `card.adjustments[0] = 0.12` (subtle card curvature) or `0.35` (organic pebble chip).
- **Text Margins**: Hard zeroed (`tf.margin_left = tf.margin_top = 0`) to prevent text box drift across different PowerPoint versions.

---

## 3. HTML5 / SVG Web Engine (`html_builder.py`)

The HTML engine creates a standalone web presentation without external JavaScript dependencies:

### 3.1 Mathematical SVG Vector Background
Rather than relying on raster images, the HTML engine renders the exact organic blobs and contour lines via an inline SVG:

```html
<svg class="bg-svg" viewBox="0 0 1600 900" fill="none">
  <!-- Terracotta Blob -->
  <path d="M1100 -120 C1320 -150 1680 80 1650 380 C1620 680 1350 780 1150 720 Z" fill="#F4DDD6" opacity="0.5"/>
  <!-- Muted Sage Blob -->
  <path d="M-150 480 C80 420 320 540 380 750 C440 960 220 1080 -50 1040 Z" fill="#D9DDD6" opacity="0.45"/>
  <!-- Organic Contour Line -->
  <path d="M-50 180 C280 150 550 420 850 320 C1150 220 1380 480 1680 420" stroke="#C48D80" stroke-width="2" fill="none" opacity="0.75"/>
</svg>
```

### 3.2 Responsive 16:9 Viewport Scaling
```css
.slide-viewport {
  width: min(94vw, 167.1vh);
  height: min(52.88vw, 94vh);
  background-color: var(--bg-ivory);
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.35);
}
```
This CSS math guarantees the slide maintains a strict 16:9 widescreen ratio regardless of browser window dimensions, mobile screens, or widescreen projector setups.

---

## 4. Headless Compilation & Visual QA

### 4.1 Headless LibreOffice PDF Export
```bash
libreoffice --headless --convert-to pdf presentation.pptx --outdir output/
```
- Converts OpenXML slides to vector PDF in ~2.5 seconds.
- Preserves all fonts, vectors, transparent fills, and line weights.

### 4.2 High-Resolution `pdftoppm` PNG Rendering
```bash
pdftoppm -png -r 150 presentation.pdf output/renders/slide
```
- Compiles each PDF page into a 150 DPI PNG image (`slide-1.png` to `slide-8.png`).
- Enables immediate automated or visual inspection of all rendered slides.
