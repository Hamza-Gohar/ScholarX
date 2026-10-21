# 🌸 Korean Minimalist Presentation Engine (Skill Package)

> A self-contained agent skill and standalone presentation generator for crafting high-end **Minimalist Korean Aesthetic** slide decks in PowerPoint (`.pptx`), Web (`index.html`), and PDF.

---

## 📦 What's Inside This Skill

```
korean-presentation-engine/
├── SKILL.md                 # Agent Skill definition with YAML frontmatter
├── README.md                # Portable usage instructions (this file)
├── docs/                    # In-depth architectural & design documentation
│   ├── design-system.md     # Gamseong aesthetic, color math, pebble geometry
│   ├── slide-archetypes.md  # The 7 slide layout specs & visual guidelines
│   ├── manifest-schema.md   # Data contract, field validation & character budgets
│   ├── engine-architecture.md# PPTX layout cloning & PDF rendering pipeline
│   └── troubleshooting.md   # Pitfall resolutions, font fallbacks & wrap fixes
├── scripts/                 # Core engine implementation
│   ├── tokens.py            # Design tokens & color constants
│   ├── pptx_builder.py      # Native PowerPoint deck compiler
│   ├── html_builder.py      # Interactive Web presentation compiler
│   └── build_deck.py        # Master CLI build script
└── templates/
    ├── minimal-pitch-deck-ref.pptx  # Master layout reference (54 vector layouts)
    └── example_manifest.py  # Starter boilerplate manifest
```

---

## 🚀 How to Send & Install This Skill

### Option 1: Use with Google Antigravity or AI Agents
To install this skill globally for your AI agent, simply copy this folder into your agent's skill directory:
```bash
cp -r korean-presentation-engine ~/.gemini/config/skills/
```
The agent will automatically discover the skill and can be invoked anytime with:
> *"Create a Korean-style presentation about [My Project] using the korean-presentation-engine skill."*

### Option 2: Standalone Use (Without AI Agents)
You can use this engine on any machine with Python 3.10+:

1. Install requirements:
   ```bash
   pip install python-pptx
   ```
2. Copy `templates/example_manifest.py` to `my_deck.py` and customize your slide content.
3. Run the generator:
   ```bash
   python scripts/build_deck.py --manifest my_deck.py
   ```

---

## 🎨 Supported Slide Archetypes

1. **`hero_cover`**: Title slide with split typography and 3 bottom highlight cards.
2. **`concept_split`**: Core definition box + 2x2 grid of 4 pillar cards.
3. **`comparison_matrix`**: Side-by-side comparison cards + synergy banner.
4. **`innovation_showcase`**: 4 balanced differentiator cards.
5. **`architecture_topology`**: Stacked multi-tier architecture diagram.
6. **`workflow_pipeline`**: 6-step horizontal connected timeline.
7. **`benefits_impact`**: 3 large metric cards with massive statistics.

For full schema details, see [`docs/manifest-schema.md`](./docs/manifest-schema.md).
