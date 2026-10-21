# 📐 Slide Archetypes Catalog

The Korean Minimalist Presentation Engine provides 7 distinct slide archetypes. Each archetype is engineered for a specific narrative function, ensuring maximum visual balance, information density, and aesthetic elegance.

---

## 1. `hero_cover` — Impactful Cover / Title Slide

### When to Use
Opening slides, section title dividers, product launch keynotes, and high-level mission statements.

### Visual Architecture
- **Top Category Tag**: 11pt bold uppercase mocha tag (`#7D6652`).
- **Hero Title**: 44pt bold split headline (`#1F1F1F` + `#7D6652`).
- **Mission Statement**: 13–14pt body text explaining the core purpose.
- **Bottom Highlights**: 3 horizontal rounded cards (`width: 2.65"`, `height: 1.6"`, `gap: 0.22"`) featuring pebble badges (`01`, `02`, `03`), bold feature titles, and concise descriptions.

```
+---------------------------------------------------------------+
|  CATEGORY TAG                                                 |
|  HERO TITLE ACCENT                                            |
|  Comprehensive mission statement paragraph...                 |
|                                                               |
|  +---------------+  +---------------+  +---------------+      |
|  | [01]          |  | [02]          |  | [03]          |      |
|  | Feature Title |  | Feature Title |  | Feature Title |      |
|  | Description   |  | Description   |  | Description   |      |
|  +---------------+  +---------------+  +---------------+      |
+---------------------------------------------------------------+
```

---

## 2. `concept_split` — Core Definition & 4-Pillar Grid

### When to Use
Introducing a complex conceptual model (e.g. *What is an AI Agent?*, *What is a Workflow?*, *Core Technology Pillars*).

### Visual Architecture
- **Left Column (`3.6" x 3.25"`)**: Large highlighted definition container containing a sub-tag, an impact headline (14pt bold), and a comprehensive narrative definition (10.5pt).
- **Right Column (`4.55" width`)**: A 2x2 grid of mini-cards (`2.15" x 1.52"`), each carrying an asymmetric pebble badge (`01` to `04`), a pillar title, and a supporting explanation.

```
+---------------------------------------------------------------+
|  CATEGORY | SPLIT TITLE                                       |
|  Subtitle explaining the concept                              |
|                                                               |
|  +---------------------+   +-----------+  +-----------+       |
|  | CORE ESSENCE        |   | [01]      |  | [02]      |       |
|  | Bold Headline       |   | Pillar 1  |  | Pillar 2  |       |
|  | Deep narrative text |   +-----------+  +-----------+       |
|  | explaining the      |   +-----------+  +-----------+       |
|  | foundational        |   | [03]      |  | [04]      |       |
|  | definition...       |   | Pillar 3  |  | Pillar 4  |       |
|  +---------------------+   +-----------+  +-----------+       |
+---------------------------------------------------------------+
```

---

## 3. `comparison_matrix` — Side-by-Side Evaluation & Synergy

### When to Use
Comparing two contrasting paradigms (e.g. *Agents vs. Workflows*, *Old Method vs. New Solution*, *Traditional vs. AI*), followed by a unifying synergy summary.

### Visual Architecture
- **Side-by-Side Cards (`4.1" x 2.25"` each)**:
  - Left card: Topic A (badge, subtitle, 4 clean bullet items with taupe bullet marks).
  - Right card: Topic B (badge, subtitle, 4 clean bullet items with taupe bullet marks).
- **Bottom Synergy Banner (`8.4" x 0.85"`)**: Full-width soft sage container (`#DDE2D8`) with bold title and description synthesizing the combined formula.

```
+---------------------------------------------------------------+
|  CATEGORY | SPLIT TITLE                                       |
|  Subtitle text                                                |
|                                                               |
|  +-------------------------+   +-------------------------+    |
|  | [BADGE A] Subtitle      |   | [BADGE B] Subtitle      |    |
|  | • Characteristic 1      |   | • Characteristic 1      |    |
|  | • Characteristic 2      |   | • Characteristic 2      |    |
|  | • Characteristic 3      |   | • Characteristic 3      |    |
|  +-------------------------+   +-------------------------+    |
|  +-------------------------------------------------------+    |
|  | The Synergy Formula: How A + B work together in sync. |    |
|  +-------------------------------------------------------+    |
+---------------------------------------------------------------+
```

---

## 4. `innovation_showcase` — 4-Quadrant Differentiators

### When to Use
Highlighting key competitive advantages, world-first innovations, unique value propositions, or core product pillars.

### Visual Architecture
- **2x2 Balanced Grid**: 4 equal-sized cards (`4.1" x 1.52"`), with `0.2"` horizontal and vertical gaps.
- **Card Hierarchy**:
  - Top-left: Asymmetric pebble badge (`01`, `02`, `03`, `04`).
  - Title: 11pt bold charcoal.
  - Body: 9pt muted gray description with generous line spacing.

---

## 5. `architecture_topology` — Multi-Tier Stack Hierarchy

### When to Use
System architecture diagrams, software layer stacks, multi-agent networks, or organizational hierarchies.

### Visual Architecture
- **Stacked Horizontal Tiers**: 4 horizontal tier containers (`8.4" x 0.72"`), spaced with `0.12"` gaps.
- **Left Tag**: Distinct pastel pebble tag (`1.8" x 0.44"`) defining the tier level (`ORCHESTRATION`, `PERCEPTION`, `VERIFICATION`, `STRATEGY`).
- **Right Content**: Tier component name in 11pt bold charcoal + role description in 9pt muted gray.

```
+---------------------------------------------------------------+
|  CATEGORY | SPLIT TITLE                                       |
|  Subtitle text                                                |
|                                                               |
|  +---------------------------------------------------------+  |
|  | [ TIER 1 ]  Component Name — Role & responsibilities... |  |
|  +---------------------------------------------------------+  |
|  +---------------------------------------------------------+  |
|  | [ TIER 2 ]  Component Name — Role & responsibilities... |  |
|  +---------------------------------------------------------+  |
|  +---------------------------------------------------------+  |
|  | [ TIER 3 ]  Component Name — Role & responsibilities... |  |
|  +---------------------------------------------------------+  |
|  +---------------------------------------------------------+  |
|  | [ TIER 4 ]  Component Name — Role & responsibilities... |  |
|  +---------------------------------------------------------+  |
+---------------------------------------------------------------+
```

---

## 6. `workflow_pipeline` — Connected Horizontal Process Timeline

### When to Use
Step-by-step user journeys, algorithmic pipelines, data flow pipelines, or chronological milestones.

### Visual Architecture
- **Continuous Connector Line**: 2pt horizontal line in `#C48D80` running behind the step badges.
- **6 Circular Step Nodes**: 48px round badges (`01` to `06`) with alternating pastel fills.
- **Step Text**: Centered title (10pt bold) and description (8pt muted gray) positioned directly below each node.

```
+---------------------------------------------------------------+
|  CATEGORY | SPLIT TITLE                                       |
|  Subtitle text                                                |
|                                                               |
|     (01)--------(02)--------(03)--------(04)--------(05)      |
|    Step 1      Step 2      Step 3      Step 4      Step 5     |
|    Desc text   Desc text   Desc text   Desc text   Desc text  |
+---------------------------------------------------------------+
```

---

## 7. `benefits_impact` — High-Impact Metrics & Proof Points

### When to Use
Key performance indicators (KPIs), ROI summaries, student outcomes, case study results, or market traction.

### Visual Architecture
- **3 Tall Metric Cards**: (`2.65" x 3.25"`), spaced with `0.22"` gaps.
- **Pebble Chip**: Top-left indicator (`01`, `02`, `03`).
- **Massive Statistic**: 20pt bold mocha typography (e.g. `PKR 300,000+`, `600+ SEATS`, `100% PROVEN`).
- **Benefit Title**: 12pt bold charcoal.
- **Impact Description**: 9.5pt explanatory text.

---

## 8. `team_credits` — Creators & Academic Leadership

### When to Use
Showcasing the creators, software engineers, and academic supervisors behind a project.

### Visual Architecture
- **Top Half (2 Developer Cards)**: Side-by-side cards (`4.1" x 2.15"` each) featuring pebble badges (`01`, `02`), uppercase role tags, 15pt bold developer names, and detailed responsibilities.
- **Bottom Half (Supervision Banner)**: Full-width container (`8.4" x 0.95"`) with a mocha border and warm stone fill, featuring a `SUPERVISED BY` chip on the left, the supervisor's name (`Sir Kaleem`), role tag, and academic advisory guidance.

```
+---------------------------------------------------------------+
|  CATEGORY | SPLIT TITLE                                       |
|  Subtitle text                                                |
|                                                               |
|  +-------------------------+   +-------------------------+    |
|  | [01] ROLE TAG           |   | [02] ROLE TAG           |    |
|  | Developer Name          |   | Developer Name          |    |
|  | System responsibilities |   | System responsibilities |    |
|  +-------------------------+   +-------------------------+    |
|  +-------------------------------------------------------+    |
|  | [SUPERVISED BY]  Supervisor Name • Role — Guidance... |    |
|  +-------------------------------------------------------+    |
+---------------------------------------------------------------+
```

