---
name: korean-presentation-engine
description: Autonomous presentation engine and repeatable design system for generating editorial Korean Minimalist ("감성" - Gamseong) slide decks. Builds native PowerPoint (.pptx), responsive interactive Web decks (HTML5/SVG), and high-resolution PDFs. Covers 7 slide archetypes, exact color math, organic vector blobs, asymmetric pebble badges, and layout automation.
---

# 🌸 Korean Minimalist Presentation Engine (Gamseong Design System)

An autonomous presentation engine and repeatable design system that generates pitch decks and exhibition slides inspired by modern Korean minimalist editorial design.

This skill equips any AI agent or human designer to generate:
1. **Native PowerPoint Presentations (`.pptx`)**: Built using genuine master vector layouts with non-overlapping typography, editable text boxes, and authentic organic curves.
2. **Interactive Responsive Web Decks (`index.html`)**: HTML5 + pure SVG presentations featuring keyboard navigation (`←`/`→`, `F` for fullscreen), responsive aspect ratio framing, and `@media print` PDF support.
3. **High-Resolution Vector PDFs (`.pdf`)**: Headless compilation producing vector-crisp documents for printing or distribution.
4. **150 DPI Visual Verification Images (`renders/*.png`)**: Automatic slide-by-slide image captures for instantaneous visual quality audits.

---

## 📑 Multi-Page Documentation & References

This skill includes 5 comprehensive reference guides in [`docs/`](./docs/):

1. **[Design System & Visual Grammar](./docs/design-system.md)**:
   - The Gamseong (감성) aesthetic philosophy.
   - Exact hex colors, alpha-blended background blobs, and contour line art.
   - Pebble badge math, asymmetric border-radii, and monoline icon standards.
   - Editorial typography hierarchy and two-tone title splitting rules.

2. **[Slide Archetypes Catalog](./docs/slide-archetypes.md)**:
   - Detailed visual schemas and layout rules for all 7 archetypes:
     - `hero_cover`: Impactful title cover with bottom highlight cards.
     - `concept_split`: 2-column layout (definition card + 4-pillar grid).
     - `comparison_matrix`: Side-by-side comparison + synergy callout banner.
     - `innovation_showcase`: 4-card grid for world-first differentiators.
     - `architecture_topology`: Stacked multi-tier architectural hierarchy.
     - `workflow_pipeline`: 6-step horizontal connected timeline.
     - `benefits_impact`: High-impact metric cards with bold statistics.

3. **[Manifest Schema & Data Contract](./docs/manifest-schema.md)**:
   - Declarative JSON and Python dictionary schemas for defining slides.
   - Validation rules, character limits, line-height constraints, and badges.

4. **[Engine Architecture & Pipelines](./docs/engine-architecture.md)**:
   - How `pptx_builder.py` clones and purges reference master layouts without XML part duplication.
   - Headless LibreOffice vector PDF compilation pipeline.
   - Sub-second `pdftoppm` PNG rendering and visual QA automation.

5. **[Troubleshooting & Production Runbook](./docs/troubleshooting.md)**:
   - Text wrapping and single-line title fitting formulas.
   - Headless environment fixes (missing fonts, libreoffice java warnings).
   - Python-pptx package part conflicts and slice indexing traps.

---

## 🎨 Quick Color Tokens

```python
# Primary Canvas & Editorial Text
BG_IVORY      = "#F8F6F2"  # Warm ivory paper cream (never sterile white)
TEXT_DARK     = "#1F1F1F"  # Charcoal black (high contrast headers)
TEXT_MOCHA    = "#7D6652"  # Roasted earthy taupe (secondary split title)
TEXT_MUTED    = "#5F5F5F"  # Slate grey for subtitles
TEXT_BODY     = "#323232"  # Readable charcoal for body paragraphs

# Asymmetric Pebble Badges
PEBBLE_SAGE   = "#DDE2D8"  # Badge 01 (Text: #465042)
PEBBLE_BLUSH  = "#F5E5E0"  # Badge 02 (Text: #7A4C46)
PEBBLE_STONE  = "#EAE6E0"  # Badge 03 (Text: #57544F)
PEBBLE_SAND   = "#F0EAE1"  # Badge 04 (Text: #6E6252)
PEBBLE_CLAY   = "#EDE0D4"  # Badge 05 (Text: #6D5344)
PEBBLE_SLATE  = "#E1E6E8"  # Badge 06 (Text: #475960)

# Delicate Vector Contours & Cards
CONTOUR_LINE  = "#C48D80"  # 1.5px organic curved line
CARD_BG       = "#FCFAF7"  # Soft translucent white/ivory
CARD_BORDER   = "#E6E0DA"  # 1px minimal border
```

---

## ⚡ How to Generate a Deck (30-Second Workflow)

### 1. Define Slides in `deck_manifest.py`
Create or edit `deck_manifest.py`:

```python
SLIDES = [
    {
        "slide_number": 1,
        "type": "hero_cover",
        "category": "YOUR PRODUCT CATEGORY",
        "title_dark": "PRODUCT",
        "title_accent": "NAME",
        "subtitle": "High-impact summary statement explaining what the system accomplishes.",
        "highlights": [
            {"badge": "01", "title": "Feature 1", "desc": "Concise factual description."},
            {"badge": "02", "title": "Feature 2", "desc": "Concise factual description."},
            {"badge": "03", "title": "Feature 3", "desc": "Concise factual description."}
        ]
    },
    # Add additional slides using any of the 7 archetypes...
]
```

### 2. Run the Build CLI
Execute the build command:

```bash
python scripts/build_deck.py --manifest deck_manifest.py --outdir output/
```

### 3. Output Generated
In under 10 seconds, the compiler creates:
- `output/presentation.pptx`
- `output/index.html`
- `output/presentation.pdf`
- `output/renders/slide-1.png` ... `slide-N.png`

---

## 🤖 Agent Execution Rules

When an AI agent is tasked with creating or modifying a presentation using this skill:
1. **Always split headers into two tones**: Title Dark (Charcoal `#1F1F1F`) + Title Accent (Warm Mocha `#7D6652`).
2. **Never place category, title, and subtitle in separate unlinked text boxes**: Always use a unified text frame with `space_after` to guarantee zero overlapping text when titles wrap.
3. **Respect character limits per line**: Titles should not exceed 42 characters at 24pt across an 8.4-inch text box to prevent unintended wrapping.
4. **Enforce the 16:9 widescreen canvas**: Slide width `10.0 inches` (7,200,000 EMU), height `5.625 inches` (4,050,000 EMU).
5. **Always verify visually**: Check the rendered PNGs with image viewing tools to confirm aesthetic balance, pebble badge curvature, and whitespace margins.
