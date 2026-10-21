# 🌸 Minimalist Korean Presentation Template System

> A fast, declarative, and repeatable presentation engine that builds editorial **Minimalist Korean Aesthetic** slide decks in native **PowerPoint (.pptx)**, responsive **Web/HTML5 (`index.html`)**, and high-resolution **PDF**.

---

## 🎨 The Korean Minimalist Design System

This system embodies the Korean **"감성" (Gamseong)** editorial aesthetic extracted directly from high-end design pitch decks:

1. **Warm Canvas Background**: `#F8F6F2` (Warm Ivory / Paper Cream) — never stark white nor sterile grey.
2. **Two-Tone Typography**: Split headers pairing **Charcoal Black (`#1F1F1F`)** with **Warm Roasted Mocha (`#7D6652`)**.
3. **Organic Vector Shapes**: Soft, flowing background blobs in muted blush terracotta (`#F4DDD6`), sage grey (`#D9DDD6`), and warm stone (`#EFECE6`).
4. **Delicate Contour Lines**: Continuous 1.5px organic curved line art (`#C48D80`) framing slide margins.
5. **Asymmetric Pebble Badges**: Soft rounded chips (`01`, `02`, `03`...) with organic curvature holding numbers, icons, and categories.

---

## 🚀 Quick Start (1-Command Generation)

To generate all formats (`.pptx`, `.html`, `.pdf`, and PNG renders), run:

```bash
python exhibition_slides/build_deck.py
```

### Generated Deliverables:
- **`ScholarX_Korean_Deck.pptx`**: Native Microsoft PowerPoint presentation with original master vector layouts, fully editable shapes, and text boxes.
- **`index.html`**: Standalone, interactive web presentation deck with SVG vector art, smooth slide transitions, and keyboard controls.
- **`ScholarX_Korean_Deck.pdf`**: High-resolution, vector-crisp printable presentation.
- **`renders/slide-*.png`**: 150 DPI preview images for immediate visual inspection.

---

## 📁 Project Structure

```
exhibition_slides/
├── Minimalist Korean Aesthetic Pitch Deck XL by Slidesgo.pptx  # Base master template
├── deck_manifest.py         # Declarative slide content (edit this to change content!)
├── build_deck.py            # Master CLI build script
├── engine/
│   ├── tokens.py            # Design tokens (colors, fonts, pebble palette)
│   ├── pptx_builder.py      # Native PowerPoint deck generator
│   └── html_builder.py      # Interactive Web presentation generator
├── index.html               # Compiled interactive web deck
├── ScholarX_Korean_Deck.pptx# Compiled PowerPoint deck
├── ScholarX_Korean_Deck.pdf # Compiled vector PDF
└── renders/                 # Exported slide PNGs (slide-1.png to slide-8.png)
```

---

## 🛠️ How to Customize or Add New Slides

Anyone can add, modify, or reorder slides without writing complex PowerPoint or HTML code. Simply edit `deck_manifest.py`:

### Example: Adding a 2-Column Concept Slide
```python
{
    "slide_number": 2,
    "type": "concept_split",
    "category": "FOUNDATIONAL INTELLIGENCE",
    "title_dark": "WHAT IS AN",
    "title_accent": "AI AGENT?",
    "subtitle": "Autonomous, goal-driven problem solvers.",
    "core_definition": {
        "headline": "Goal-Driven Autonomy with Tool Use & Reasoning",
        "text": "An AI Agent is an autonomous software entity..."
    },
    "pillars": [
        {"badge": "01", "title": "Perception", "desc": "Ingests messy documents."},
        {"badge": "02", "title": "Reasoning", "desc": "Formulates multi-step plans."},
        {"badge": "03", "title": "Tools", "desc": "Executes live web searches."},
        {"badge": "04", "title": "Memory", "desc": "Recalls previous hunts."}
    ]
}
```

### Available Slide Archetypes (`type`):
- `hero_cover`: Impactful title slide with large split typography and 3 bottom highlight cards.
- `concept_split`: Definition box on the left, 4 pebble cards in a 2x2 grid on the right.
- `comparison_matrix`: Side-by-side comparison cards (e.g. Agents vs Workflows) + bottom synergy banner.
- `innovation_showcase`: 4 distinct feature / innovation cards with pebble badges.
- `architecture_topology`: Stacked multi-tier architectural hierarchy diagram.
- `workflow_pipeline`: 6-step horizontal connected pipeline with numbered pebble nodes.
- `benefits_impact`: 3 large metric cards with massive statistics (`PKR 300,000+`) and descriptions.

---

## ⌨️ Web Deck Controls (`index.html`)

Open `index.html` in any browser or launch in an exhibition kiosk:
- **`→` / `Space` / `PageDown`**: Next slide
- **`←` / `PageUp`**: Previous slide
- **`F`**: Toggle fullscreen presentation mode
- **`Ctrl + P`**: Print or save directly to PDF
