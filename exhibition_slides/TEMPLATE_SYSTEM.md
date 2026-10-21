# 📐 ScholarX "Black Minimalist" Slide Presentation Template System

> **A reusable, production-grade presentation template engine replicating high-end executive decks.**

---

## 1. Visual Design Principles

1. **Pure Pitch-Black Canvas (`#000000`)**: Deep black background with 0% clutter.
2. **Typography**: **`Outfit`** (weights 400 to 800) paired with **`JetBrains Mono`** for metadata counters. Razor-sharp optical clarity at every scale.
3. **Parametric 3D Wireframe Wave**: High-density SVG ribbon with 46 parallel cubic bezier curves curving through the top-right and bottom-left quadrants.
4. **Physical Exhibition Alignment**: Subtle push-pin crosshairs (`+`) at all 4 corners (`.pin-mark`).
5. **Color & Hierarchy**:
   - Headers: `#FFFFFF` (pure white, weight 800, tight tracking)
   - Primary Body: `#F4F4F5` / `#D4D4D8` (weights 400-600)
   - Secondary / Labels: `#A1A1AA` (weight 500-700)
   - Subtle Dividers: `#24242A` (1px hairlines)

---

## 2. Reusable Slide Archetypes

| Archetype Class | Layout Structure | Use Case |
|---|---|---|
| `.template-cover` | Large 88px title + subtitle + summary text + metadata footer | Cover / Hero introduction |
| `.template-split` | 340px Left Anchor + 1px hairline divider + Right 2-column or list content | Deep explanations, 6 pillars, Pakistani focus |
| `.template-cards` | Top headline + 2 large split cards (Inverted white vs dark card) | Architectural comparisons (Workflows vs Agents) |
| `.template-3col` | Top box container + 3 vertical columns with hairline dividers | The 3 core problems, 3 features |
| `.template-flowchart` | Single-field unified SVG diagram container with distinct node colors | System architecture, end-to-end pipeline |
| `.template-timeline` | 4 circular step nodes (`01`–`04`) + horizontal connecting track + summary stats | User journey, lifecycle phases |
| `.template-4cards` | 4 clean vertical cards with badges, titles, and item lists | Tech stack, module specifications |
| `.template-statistic` | Big metric numbers (`58px` weight 800) + executive closing quote card | Impact metrics, final takeaway |

---

## 3. Interactive Hotkeys

- **`Right Arrow` / `Space`**: Next slide
- **`Left Arrow`**: Previous slide
- **`F`**: Toggle browser fullscreen
- **`P`**: 1-Click Print / PDF Export
- **`1` – `9`, `0`**: Direct jump to slides 01 through 10
