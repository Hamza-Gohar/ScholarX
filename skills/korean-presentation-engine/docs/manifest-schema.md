# 📋 Manifest Schema & Data Contract

The Korean Minimalist Presentation Engine is driven by a declarative manifest file (`deck_manifest.py` or `manifest.json`). This document defines the exact schema, field types, and character budgets to ensure zero visual overflow.

---

## 1. Top-Level Structure

```python
DECK_METADATA = {
    "title": str,            # Human-readable title of the presentation
    "theme": str,            # "Minimalist Korean Aesthetic"
    "target_audience": str,  # Description of primary viewers
    "aspect_ratio": "16:9",  # Required: standard widescreen
}

SLIDES = [
    # List of slide dictionaries conforming to one of the 7 archetypes
]
```

---

## 2. Universal Header Fields

Every slide dictionary (except `hero_cover`) requires these standard header fields:

| Field | Type | Max Characters | Description |
|:---|:---|:---|:---|
| `slide_number` | `int` | — | 1-indexed slide sequence number. |
| `type` | `str` | — | One of the 7 archetype keys. |
| `category` | `str` | 40 chars | Small uppercase tracking tag (e.g. `FOUNDATIONAL INTELLIGENCE`). |
| `title_dark` | `str` | 24 chars | First half of the split title in charcoal black (`#1F1F1F`). |
| `title_accent` | `str` | 24 chars | Second half of the split title in warm mocha (`#7D6652`). |
| `subtitle` | `str` | 95 chars | High-level summary statement displayed directly beneath the title. |

> **⚠️ Single-Line Rule**: The sum of `title_dark` + `title_accent` should ideally stay under **42 characters** to fit comfortably on a single line at 24pt across the 8.4-inch text box.

---

## 3. Archetype Schemas & Budgets

### 3.1 `hero_cover`
```python
{
    "slide_number": 1,
    "type": "hero_cover",
    "category": str,        # Max 45 chars
    "title_dark": str,      # Max 15 chars (e.g. "SCHOLAR")
    "title_accent": str,    # Max 15 chars (e.g. "X")
    "subtitle": str,        # Max 150 chars (2-line mission statement)
    "highlights": [         # Exactly 3 highlight objects
        {
            "badge": str,   # "01", "02", "03"
            "title": str,   # Max 20 chars
            "desc": str     # Max 75 chars
        }
    ]
}
```

### 3.2 `concept_split`
```python
{
    "slide_number": int,
    "type": "concept_split",
    "category": str,
    "title_dark": str,
    "title_accent": str,
    "subtitle": str,
    "core_definition": {
        "headline": str,    # Max 45 chars
        "text": str         # Max 260 chars (foundational narrative)
    },
    "pillars": [            # Exactly 4 pillar objects (2x2 grid)
        {
            "badge": str,   # "01", "02", "03", "04"
            "title": str,   # Max 24 chars
            "desc": str     # Max 100 chars
        }
    ]
}
```

### 3.3 `comparison_matrix`
```python
{
    "slide_number": int,
    "type": "comparison_matrix",
    "category": str,
    "title_dark": str,
    "title_accent": str,
    "subtitle": str,
    "agent_side": {
        "badge": str,       # Max 15 chars (e.g. "AI AGENTS")
        "subtitle": str,    # Max 55 chars
        "points": [str]     # Exactly 4 bullet strings (Max 50 chars each)
    },
    "workflow_side": {
        "badge": str,       # Max 15 chars (e.g. "WORKFLOWS")
        "subtitle": str,    # Max 55 chars
        "points": [str]     # Exactly 4 bullet strings (Max 50 chars each)
    },
    "synergy_callout": {
        "title": str,       # Max 50 chars
        "desc": str         # Max 160 chars
    }
}
```

### 3.4 `innovation_showcase`
```python
{
    "slide_number": int,
    "type": "innovation_showcase",
    "category": str,
    "title_dark": str,
    "title_accent": str,
    "subtitle": str,
    "cards": [              # Exactly 4 card objects (2x2 grid)
        {
            "badge": str,   # "01", "02", "03", "04"
            "title": str,   # Max 30 chars
            "desc": str     # Max 140 chars
        }
    ]
}
```

### 3.5 `architecture_topology`
```python
{
    "slide_number": int,
    "type": "architecture_topology",
    "category": str,
    "title_dark": str,
    "title_accent": str,
    "subtitle": str,
    "tiers": [              # Exactly 4 tier objects (top-to-bottom stack)
        {
            "level": str,   # Max 25 chars (e.g. "ORCHESTRATION")
            "name": str,    # Max 45 chars (Component / Class name)
            "role": str     # Max 110 chars (Functional responsibility)
        }
    ]
}
```

### 3.6 `workflow_pipeline`
```python
{
    "slide_number": int,
    "type": "workflow_pipeline",
    "category": str,
    "title_dark": str,
    "title_accent": str,
    "subtitle": str,
    "steps": [              # Exactly 6 chronological step objects
        {
            "step": str,    # "01", "02", ... "06"
            "title": str,   # Max 18 chars
            "desc": str     # Max 65 chars
        }
    ]
}
```

### 3.7 `benefits_impact`
```python
{
    "slide_number": int,
    "type": "benefits_impact",
    "category": str,
    "title_dark": str,
    "title_accent": str,
    "subtitle": str,
    "benefits": [           # Exactly 3 impact cards
        {
            "badge": str,   # "01", "02", "03"
            "stat": str,    # Max 16 chars (e.g. "PKR 300,000+", "100% PROVEN")
            "title": str,   # Max 32 chars
            "desc": str     # Max 130 chars
        }
    ]
}
```
