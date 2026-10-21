# 🎨 Korean Minimalist Design System & Visual Grammar

The **Gamseong (감성) Minimalist Design System** blends modern editorial typography with soft organic geometry, asymmetric balance, and muted natural palettes. Extracted from premier Korean design agencies and exhibition pitch decks, this system achieves visual serenity and high informational clarity.

---

## 1. Color Palette & Alpha Blending

The palette avoids stark white (`#FFFFFF`) or harsh black (`#000000`). Every tone is grounded in organic, paper, or roasted earth pigments.

### 1.1 Base Canvas & Text Hierarchy
| Token Name | Hex Code | RGB | Purpose |
|:---|:---|:---|:---|
| `BG_IVORY` | `#F8F6F2` | `(248, 246, 242)` | Canvas background; creates warm, breathable paper texture. |
| `TEXT_DARK` | `#1F1F1F` | `(31, 31, 31)` | Obsidian charcoal; primary titles, bold metrics, and headings. |
| `TEXT_MOCHA` | `#7D6652` | `(125, 102, 82)` | Roasted warm earth; secondary split title, category tracking tags. |
| `TEXT_BODY` | `#323232` | `(50, 50, 50)` | Deep slate; high-contrast, easily readable body copy. |
| `TEXT_MUTED` | `#5F5F5F` | `(95, 95, 95)` | Neutral warm gray; subtitles, secondary explanations, footnotes. |

### 1.2 Translucent Background Blobs (Gouache Accents)
The master PowerPoint template uses DrawingML `custGeom` shapes with alpha blending over the `#F8F6F2` canvas:
- **Terracotta Blush (`#F4DDD6`)**: Alpha 46% (`<a:alpha val="46370"/>`). Placed at top-right or lower-left corners to add warmth.
- **Muted Sage Slate (`#D9DDD6`)**: Alpha 26–33% (`<a:alpha val="33520"/>`). Balances the warm terracotta with a calming earthen hue.
- **Oatmeal Stone (`#EFECE6`)**: Alpha 40–50% (`<a:alpha val="50000"/>`). Subtle central mass providing structural depth.
- **Warm Shadow (`#F2EBE5`)**: Alpha 13% (`<a:alpha val="12850"/>`). Soft grounding gradient.

### 1.3 Asymmetric Pebble Badges
Pebble chips use muted pastel fills with high-contrast earthy text:
- **`01` Sage**: Fill `#DDE2D8` (`RGB(221, 226, 216)`), Text `#465042` (`RGB(70, 80, 66)`)
- **`02` Blush**: Fill `#F5E5E0` (`RGB(245, 229, 224)`), Text `#7A4C46` (`RGB(122, 76, 70)`)
- **`03` Stone**: Fill `#EAE6E0` (`RGB(234, 230, 224)`), Text `#57544F` (`RGB(87, 84, 79)`)
- **`04` Sand**: Fill `#F0EAE1` (`RGB(240, 234, 225)`), Text `#6E6252` (`RGB(110, 98, 82)`)
- **`05` Clay**: Fill `#EDE0D4` (`RGB(237, 224, 212)`), Text `#6D5344` (`RGB(109, 83, 68)`)
- **`06` Slate**: Fill `#E1E6E8` (`RGB(225, 230, 232)`), Text `#475960` (`RGB(71, 89, 96)`)

---

## 2. Geometry & Asymmetric Curves

### 2.1 The Pebble Curvature Formula
Standard rounded rectangles feel mechanical. The Gamseong aesthetic employs an organic, non-uniform curve radius:

```css
/* CSS Pebble Badge */
border-radius: 48% 52% 54% 46% / 46% 54% 46% 54%;
```

In PowerPoint DrawingML, this is achieved using `MSO_SHAPE.ROUNDED_RECTANGLE` with an adjustment parameter:
```python
shape.adjustments[0] = 0.35  # Subtle squircle curvature
```

### 2.2 Organic Contour Line Art
A defining characteristic of Korean editorial decks is the **single continuous organic contour line**:
- **Color**: `#C48D80` (`RGB(196, 141, 128)`)
- **Stroke Width**: `1.5pt` (PowerPoint) / `1.5px` (SVG)
- **Path Geometry**: A cubic bezier path starting off-canvas, sweeping smoothly across the upper perimeter, and dipping gently behind cards:
  ```svg
  <path d="M-50 180 C280 150 550 420 850 320 C1150 220 1380 480 1680 420"
        stroke="#C48D80" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.75"/>
  ```

---

## 3. Typography Hierarchy & Splitting Rules

### 3.1 Two-Tone Split Title Treatment
Never set the entire headline in a single flat color. Every slide title is split into two complementary segments:
- **Segment 1 (`title_dark`)**: Bold Charcoal (`#1F1F1F`) — establishes the core noun or verb (e.g. `WHAT IS AN`, `AGENTS VS. WORKFLOWS`).
- **Segment 2 (`title_accent`)**: Bold Warm Mocha (`#7D6652`) — highlights the subject or outcome (e.g. `AI AGENT?`, `THE HYBRID FORMULA`).

### 3.2 Spacing & Type Scale (16:9 Canvas)
- **Slide Width**: 10.0 in (960 pt)
- **Slide Height**: 5.625 in (540 pt)
- **Horizontal Margins**: 0.8 in (76.8 pt) on Left and Right
- **Usable Width**: 8.4 in (806.4 pt)

```
+-------------------------------------------------------------------+
| 0.8" Margin                                                       |
|   [CATEGORY TAG]       Arial 9.5pt | Bold | Uppercase | #7D6652    |
|   [SPLIT TITLE]        Arial 23-28pt | Bold | #1F1F1F + #7D6652   |
|   [SUBTITLE]           Arial 11-12pt | Regular | #5F5F5F          |
|                                                                   |
|   [CONTENT CANVAS]     Top Y = 1.85", Height = 3.25"              |
|                                                                   |
+-------------------------------------------------------------------+
```

### 3.3 Card Container Specifications
- **Background**: Translucent warm cream `#FCFAF7`
- **Border**: `1pt` solid `#E6E0DA`
- **Padding**: `0.15in` to `0.25in`
- **Corner Radius**: `shape.adjustments[0] = 0.08` to `0.12`
