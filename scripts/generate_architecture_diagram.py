#!/usr/bin/env python3
"""
SCHOLARX System Architecture Diagram Generator
Generates a clean, simple, highly readable Excalidraw diagram representing
the 4-layer architecture of the SCHOLARX System.
"""

import json
import os
import random

# Seed for deterministic generation
random.seed(42)

def gen_id():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choices(chars, k=16))

class ExcalidrawBuilder:
    def __init__(self):
        self.elements = []

    def add_rect(
        self,
        x,
        y,
        width,
        height,
        bg_color="transparent",
        stroke_color="#1e1e1e",
        stroke_width=1.5,
        stroke_style="solid",
        fill_style="solid",
        roughness=0,
        opacity=100,
        rounded=True,
    ):
        elem = {
            "id": gen_id(),
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "angle": 0,
            "strokeColor": stroke_color,
            "backgroundColor": bg_color,
            "fillStyle": fill_style,
            "strokeWidth": stroke_width,
            "strokeStyle": stroke_style,
            "roughness": roughness,
            "opacity": opacity,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 3} if rounded else None,
            "seed": random.randint(1000, 999999),
            "version": 1,
            "versionNonce": random.randint(1000, 999999),
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
        }
        self.elements.append(elem)
        return elem

    def add_text(
        self,
        x,
        y,
        text,
        font_size=14,
        font_family=1,
        color="#1e1e1e",
        text_align="left",
        width=None,
        line_height=1.25,
    ):
        lines = text.split("\n")
        max_line_len = max(len(l) for l in lines) if lines else 1
        calc_width = int(max_line_len * (font_size * 0.58))
        if width is not None:
            w = width
        else:
            w = max(calc_width, 40)
        h = int(len(lines) * font_size * line_height)

        elem_x = x
        if text_align == "center":
            elem_x = x - w / 2

        elem = {
            "id": gen_id(),
            "type": "text",
            "x": elem_x,
            "y": y,
            "width": w,
            "height": h,
            "angle": 0,
            "strokeColor": color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "seed": random.randint(1000, 999999),
            "version": 1,
            "versionNonce": random.randint(1000, 999999),
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
            "text": text,
            "fontSize": font_size,
            "fontFamily": font_family,
            "textAlign": text_align,
            "verticalAlign": "top",
            "baseline": font_size,
            "containerId": None,
            "originalText": text,
            "lineHeight": line_height,
        }
        self.elements.append(elem)
        return elem

    def add_arrow(
        self,
        x1,
        y1,
        x2,
        y2,
        color="#495057",
        stroke_width=2,
        stroke_style="solid",
        label=None,
        label_offset_y=-18,
    ):
        dx = x2 - x1
        dy = y2 - y1
        elem = {
            "id": gen_id(),
            "type": "arrow",
            "x": x1,
            "y": y1,
            "width": abs(dx),
            "height": abs(dy),
            "angle": 0,
            "strokeColor": color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": stroke_width,
            "strokeStyle": stroke_style,
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 2},
            "seed": random.randint(1000, 999999),
            "version": 1,
            "versionNonce": random.randint(1000, 999999),
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
            "points": [[0, 0], [dx, dy]],
            "lastCommittedPoint": None,
            "startBinding": None,
            "endBinding": None,
            "startArrowhead": None,
            "endArrowhead": "arrow",
        }
        self.elements.append(elem)

        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + label_offset_y
            self.add_text(
                mid_x,
                mid_y,
                label,
                font_size=12,
                font_family=1,
                color=color,
                text_align="center",
            )
        return elem

    def build_doc(self):
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "viewBackgroundColor": "#ffffff",
                "gridSize": None,
            },
            "files": {},
        }


def create_scholarx_diagram():
    b = ExcalidrawBuilder()

    # Layout constants
    CANVAS_X = 80
    CANVAS_W = 1340
    CENTER_X = CANVAS_X + CANVAS_W / 2  # 750

    # ---------------------------------------------------------
    # 0. HEADER BANNER
    # ---------------------------------------------------------
    HEADER_Y = 40
    HEADER_H = 85
    b.add_rect(
        CANVAS_X,
        HEADER_Y,
        CANVAS_W,
        HEADER_H,
        bg_color="#182234",
        stroke_color="#0f172a",
        stroke_width=2,
        rounded=True,
    )

    b.add_text(
        CENTER_X,
        HEADER_Y + 16,
        "SCHOLARX — Autonomous Scholarship Intelligence Network",
        font_size=22,
        font_family=1,
        color="#ffffff",
        text_align="center",
    )
    b.add_text(
        CENTER_X,
        HEADER_Y + 50,
        "System Architecture: 4-Layer Autonomous Intelligence Network for Pakistani Students",
        font_size=13,
        font_family=1,
        color="#94a3b8",
        text_align="center",
    )

    # ---------------------------------------------------------
    # 1. PRESENTATION LAYER (Next.js 15 UI) - Blue
    # ---------------------------------------------------------
    L1_Y = 160
    L1_H = 220
    b.add_rect(
        CANVAS_X,
        L1_Y,
        CANVAS_W,
        L1_H,
        bg_color="#e7f5ff",
        stroke_color="#1971c2",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        CANVAS_X + 24,
        L1_Y + 14,
        "1. PRESENTATION LAYER (Next.js 15 App Router)",
        font_size=17,
        font_family=1,
        color="#1864ab",
    )

    # 3 Sub-Cards for Layer 1
    # Positions: 115, 555, 995
    c_w = 390
    c_h = 145
    c_y = L1_Y + 50

    # L1 - Card 1: Student Intake & Profile Presets
    c1_x = 115
    b.add_rect(c1_x, c_y, c_w, c_h, bg_color="#ffffff", stroke_color="#74c0fc", stroke_width=1.5)
    b.add_text(c1_x + 16, c_y + 12, "Student Intake & Profile Presets", font_size=15, color="#1971c2")
    b.add_text(
        c1_x + 16,
        c_y + 36,
        "• Academic Profile: Degree level, major, CGPA\n"
        "• Pakistan Tests: HEC HAT, USAT, IELTS, MOI waivers\n"
        "• Domicile & HEC Bilateral quota tag matching\n"
        "• 3 Instant Exhibition Presets (Lahore, Karachi, Quetta)",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # L1 - Card 2: Live Command Theatre
    c2_x = 555
    b.add_rect(c2_x, c_y, c_w, c_h, bg_color="#ffffff", stroke_color="#74c0fc", stroke_width=1.5)
    b.add_text(c2_x + 16, c_y + 12, "Live Command Theatre", font_size=15, color="#1971c2")
    b.add_text(
        c2_x + 16,
        c_y + 36,
        "• 1920x1080 Spatial Canvas interactive floor\n"
        "• Real-time SSE streaming event visualizer\n"
        "• Central Commander Console (6 tactical states)\n"
        "• Quadratic Bezier data packet intelligence conduits",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # L1 - Card 3: Canonical Web Dossier & PDF Export
    c3_x = 995
    b.add_rect(c3_x, c_y, c_w, c_h, bg_color="#ffffff", stroke_color="#74c0fc", stroke_width=1.5)
    b.add_text(c3_x + 16, c_y + 12, "Canonical Web Dossier & Export", font_size=15, color="#1971c2")
    b.add_text(
        c3_x + 16,
        c_y + 36,
        "• 10-Section Canonical Web Scholarship Dossier\n"
        "• 8-Factor composite match scorecard display\n"
        "• Publication-grade vector PDF export & print view\n"
        "• 310+ deep catalog browser & local session history",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # Arrow L1 -> L2
    b.add_arrow(
        CENTER_X,
        L1_Y + L1_H,
        CENTER_X,
        L1_Y + L1_H + 50,
        color="#1971c2",
        label="REST API Requests & Real-Time SSE Streams",
    )

    # ---------------------------------------------------------
    # 2. API & ORCHESTRATION LAYER (FastAPI & LangGraph) - Cyan
    # ---------------------------------------------------------
    L2_Y = L1_Y + L1_H + 50  # 430
    L2_H = 220
    b.add_rect(
        CANVAS_X,
        L2_Y,
        CANVAS_W,
        L2_H,
        bg_color="#e3fafc",
        stroke_color="#0c8599",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        CANVAS_X + 24,
        L2_Y + 14,
        "2. API & ORCHESTRATION LAYER (FastAPI & LangGraph)",
        font_size=17,
        font_family=1,
        color="#0b7285",
    )

    # 2 Sub-Cards for Layer 2
    l2_cw = 610
    l2_ch = 145
    l2_cy = L2_Y + 50

    # L2 - Card 1: FastAPI REST API & SSE EventBus
    l2_c1_x = 115
    b.add_rect(l2_c1_x, l2_cy, l2_cw, l2_ch, bg_color="#ffffff", stroke_color="#66d9e8", stroke_width=1.5)
    b.add_text(l2_c1_x + 16, l2_cy + 12, "FastAPI REST API & SSE EventBus (Port 8000)", font_size=15, color="#0c8599")
    b.add_text(
        l2_c1_x + 16,
        l2_cy + 36,
        "• Routes: /api/discover, /api/profile, /api/scholarships, /api/sessions\n"
        "• Session-isolated async EventBus pub/sub event channels\n"
        "• 500-event circular replay buffer (zero-loss SSE reconnects)\n"
        "• KeyManager: 30 API keys round-robin with 60s cooldown & failure telemetry",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # L2 - Card 2: LangGraph StateGraph Coordinator
    l2_c2_x = 775
    b.add_rect(l2_c2_x, l2_cy, l2_cw, l2_ch, bg_color="#ffffff", stroke_color="#66d9e8", stroke_width=1.5)
    b.add_text(l2_c2_x + 16, l2_cy + 12, "LangGraph StateGraph Engine", font_size=15, color="#0c8599")
    b.add_text(
        l2_c2_x + 16,
        l2_cy + 36,
        "• Centralized ScholarXState TypedDict state machine\n"
        "• Compiles & coordinates the 10-node intelligence pipeline\n"
        "• Dual execution engine: LIVE stream vs DEMO 12-stage replay engine\n"
        "• Node transition telemetry, error boundaries & state persistence",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # Arrow L2 -> L3
    b.add_arrow(
        CENTER_X,
        L2_Y + L2_H,
        CENTER_X,
        L2_Y + L2_H + 50,
        color="#0c8599",
        label="Compiles & Coordinates 10-Node Intelligence Pipeline",
    )

    # ---------------------------------------------------------
    # 3. MULTI-AGENT & WORKFLOW CLUSTER - Green / Purple
    # ---------------------------------------------------------
    L3_Y = L2_Y + L2_H + 50  # 700
    L3_H = 370
    b.add_rect(
        CANVAS_X,
        L3_Y,
        CANVAS_W,
        L3_H,
        bg_color="#f4fce3",
        stroke_color="#2f9e44",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        CANVAS_X + 24,
        L3_Y + 14,
        "3. MULTI-AGENT & WORKFLOW CLUSTER (10-Node Intelligence Pipeline)",
        font_size=17,
        font_family=1,
        color="#2b8a3e",
    )

    # 4 Stage Columns inside Layer 3
    # 115, 442, 769, 1096
    col_w = 295
    col_h = 290
    col_y = L3_Y + 55

    # Stage A: Discovery Stage
    s1_x = 115
    b.add_rect(s1_x, col_y, col_w, col_h, bg_color="#e6fcf5", stroke_color="#099268", stroke_width=1.5)
    b.add_text(s1_x + 14, col_y + 12, "DISCOVERY STAGE", font_size=14, color="#087f5b")
    # Sub box: Profile Analyst
    b.add_rect(s1_x + 10, col_y + 36, col_w - 20, 56, bg_color="#ffffff", stroke_color="#63e6be", stroke_width=1)
    b.add_text(s1_x + 18, col_y + 42, "Profile Analyst (LLM)", font_size=12, color="#087f5b")
    b.add_text(s1_x + 18, col_y + 58, "Normalizes CGPA, grading scales,\nPakistani marks & test conversions", font_size=10, color="#495057", line_height=1.2)
    # Sub box: Discovery Commander
    b.add_rect(s1_x + 10, col_y + 98, col_w - 20, 56, bg_color="#ffffff", stroke_color="#63e6be", stroke_width=1)
    b.add_text(s1_x + 18, col_y + 104, "Discovery Commander", font_size=12, color="#087f5b")
    b.add_text(s1_x + 18, col_y + 120, "Translates intake criteria to targeted\nqueries & dispatches regional scouts", font_size=10, color="#495057", line_height=1.2)
    # Sub box: 5 Regional Scouts
    b.add_rect(s1_x + 10, col_y + 160, col_w - 20, 115, bg_color="#ffffff", stroke_color="#63e6be", stroke_width=1)
    b.add_text(s1_x + 18, col_y + 166, "5 Regional Scouts (Parallel)", font_size=12, color="#087f5b")
    b.add_text(
        s1_x + 18,
        col_y + 184,
        "• Europe Scout (DAAD, Eiffel, Erasmus)\n"
        "• Asia Scout (MEXT, CSC, KGSP, Turkey)\n"
        "• Americas Scout (Fulbright, Vanier)\n"
        "• MENA Scout (KFUPM, KAUST, Qatar)\n"
        "• Oceania Scout (Australia Awards)",
        font_size=10,
        color="#495057",
        line_height=1.3,
    )

    # Arrow Stage 1 -> Stage 2
    b.add_arrow(s1_x + col_w, col_y + col_h / 2, s1_x + col_w + 32, col_y + col_h / 2, color="#099268")

    # Stage B: Investigation Stage
    s2_x = 442
    b.add_rect(s2_x, col_y, col_w, col_h, bg_color="#ebfbee", stroke_color="#2b8a3e", stroke_width=1.5)
    b.add_text(s2_x + 14, col_y + 12, "INVESTIGATION (Deterministic)", font_size=14, color="#2b8a3e")
    # Sub box: Eligibility Investigator
    b.add_rect(s2_x + 10, col_y + 36, col_w - 20, 75, bg_color="#ffffff", stroke_color="#8ce99a", stroke_width=1)
    b.add_text(s2_x + 18, col_y + 42, "Eligibility Investigator", font_size=12, color="#2b8a3e")
    b.add_text(s2_x + 18, col_y + 58, "Deterministic 15-dimension audit:\n• HEC accreditation & 16-yr equivalence\n• Pakistani nationality & provincial quota\n• Age limits & minimum CGPA cutoff", font_size=10, color="#495057", line_height=1.2)
    # Sub box: True Cost Analyzer
    b.add_rect(s2_x + 10, col_y + 118, col_w - 20, 78, bg_color="#ffffff", stroke_color="#8ce99a", stroke_width=1)
    b.add_text(s2_x + 18, col_y + 124, "True Cost Analyzer (PKR)", font_size=12, color="#2b8a3e")
    b.add_text(s2_x + 18, col_y + 140, "Calculates 4-phase out-of-pocket costs:\n• Upfront tests, MOFA/IBCC attestations\n• FBR Section 236Y advance card tax\n• Airfare & initial settling-in deficit in PKR", font_size=10, color="#495057", line_height=1.2)
    # Sub box: Deadline Intelligence
    b.add_rect(s2_x + 10, col_y + 203, col_w - 20, 72, bg_color="#ffffff", stroke_color="#8ce99a", stroke_width=1)
    b.add_text(s2_x + 18, col_y + 209, "Deadline Intelligence", font_size=12, color="#2b8a3e")
    b.add_text(s2_x + 18, col_y + 225, "Computes preparation runway & slack:\n• Dual-gate lead times (HEC + Embassy)\n• VFS Gerry's appointment backlogs", font_size=10, color="#495057", line_height=1.2)

    # Arrow Stage 2 -> Stage 3
    b.add_arrow(s2_x + col_w, col_y + col_h / 2, s2_x + col_w + 32, col_y + col_h / 2, color="#2b8a3e")

    # Stage C: Verification Stage
    s3_x = 769
    b.add_rect(s3_x, col_y, col_w, col_h, bg_color="#f3f0ff", stroke_color="#7950f2", stroke_width=1.5)
    b.add_text(s3_x + 14, col_y + 12, "VERIFICATION (Adversarial)", font_size=14, color="#6741d9")
    # Sub box: Skeptic Agent
    b.add_rect(s3_x + 10, col_y + 36, col_w - 20, 115, bg_color="#ffffff", stroke_color="#b197fc", stroke_width=1)
    b.add_text(s3_x + 18, col_y + 44, "Skeptic Agent (Adversarial LLM)", font_size=12, color="#6741d9")
    b.add_text(
        s3_x + 18,
        col_y + 64,
        "Adversarial red-team auditor:\n"
        "• Uncovers return-to-home bond traps\n"
        "• Identifies hidden university bench fees\n"
        "• Flags cost-of-living vs stipend deficits\n"
        "• Detects predatory conditional offers",
        font_size=10,
        color="#495057",
        line_height=1.3,
    )
    # Sub box: Synthesis Engine
    b.add_rect(s3_x + 10, col_y + 160, col_w - 20, 115, bg_color="#ffffff", stroke_color="#b197fc", stroke_width=1)
    b.add_text(s3_x + 18, col_y + 168, "Synthesis Engine", font_size=12, color="#6741d9")
    b.add_text(
        s3_x + 18,
        col_y + 188,
        "Reconciliation & risk weighting:\n"
        "• Merges deterministic facts with skeptic alerts\n"
        "• Weighs financial risks vs career reward\n"
        "• Generates comprehensive risk scorecard\n"
        "• Formulates mitigation requirements",
        font_size=10,
        color="#495057",
        line_height=1.3,
    )

    # Arrow Stage 3 -> Stage 4
    b.add_arrow(s3_x + col_w, col_y + col_h / 2, s3_x + col_w + 32, col_y + col_h / 2, color="#7950f2")

    # Stage D: Output Stage
    s4_x = 1096
    b.add_rect(s4_x, col_y, col_w, col_h, bg_color="#f8f0fc", stroke_color="#ae3ec9", stroke_width=1.5)
    b.add_text(s4_x + 14, col_y + 12, "OUTPUT & ROADMAP STAGE", font_size=14, color="#9c36b5")
    # Sub box: Ranking Engine
    b.add_rect(s4_x + 10, col_y + 36, col_w - 20, 115, bg_color="#ffffff", stroke_color="#e599f7", stroke_width=1)
    b.add_text(s4_x + 18, col_y + 44, "Ranking Engine (Deterministic)", font_size=12, color="#9c36b5")
    b.add_text(
        s4_x + 18,
        col_y + 64,
        "8-Factor scoring index (0-100 pts):\n"
        "• Eligibility Match & Acceptance Odds\n"
        "• Net PKR Expense Burden\n"
        "• Preparation Runway & Slack Days\n"
        "• Skeptic Risk Penalty Weight",
        font_size=10,
        color="#495057",
        line_height=1.3,
    )
    # Sub box: Final Advisor Agent
    b.add_rect(s4_x + 10, col_y + 160, col_w - 20, 115, bg_color="#ffffff", stroke_color="#e599f7", stroke_width=1)
    b.add_text(s4_x + 18, col_y + 168, "Final Advisor Agent (LLM)", font_size=12, color="#9c36b5")
    b.add_text(
        s4_x + 18,
        col_y + 188,
        "Strategic narrative generation:\n"
        "• Tailors actionable 12-month timeline\n"
        "• HEC & MOFA attestation milestones\n"
        "• SOP / Motivation Letter positioning\n"
        "• Contingency backup safety plans",
        font_size=10,
        color="#495057",
        line_height=1.3,
    )

    # Arrow L3 -> L4
    b.add_arrow(
        CENTER_X,
        L3_Y + L3_H,
        CENTER_X,
        L3_Y + L3_H + 50,
        color="#2b8a3e",
        label="Persists Session State, Retrieves Seed Catalog & Queries External APIs",
    )

    # ---------------------------------------------------------
    # 4. DATA & EXTERNAL SERVICES LAYER - Amber
    # ---------------------------------------------------------
    L4_Y = L3_Y + L3_H + 50  # 1120
    L4_H = 220
    b.add_rect(
        CANVAS_X,
        L4_Y,
        CANVAS_W,
        L4_H,
        bg_color="#fff9db",
        stroke_color="#f59f00",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        CANVAS_X + 24,
        L4_Y + 14,
        "4. DATA & EXTERNAL SERVICES (Hybrid Local-First Storage & Cloud API Pool)",
        font_size=17,
        font_family=1,
        color="#e67700",
    )

    # 2 Sub-Cards for Layer 4
    l4_cw = 610
    l4_ch = 145
    l4_cy = L4_Y + 50

    # L4 - Card 1: Local Storage & Seed Catalog
    l4_c1_x = 115
    b.add_rect(l4_c1_x, l4_cy, l4_cw, l4_ch, bg_color="#ffffff", stroke_color="#ffe066", stroke_width=1.5)
    b.add_text(l4_c1_x + 16, l4_cy + 12, "Local Storage: SQLite Database & Seed Catalog", font_size=15, color="#e67700")
    b.add_text(
        l4_c1_x + 16,
        l4_cy + 36,
        "• SQLite Database (WAL mode, 6 normalized tables, async batch queue)\n"
        "• 310+ Pre-Seeded Deep Scholarship Catalog with full criteria & cost breakdowns\n"
        "• Local seed cache & deterministic 12-stage exhibition demo replay fixtures\n"
        "• Zero-cloud fallback: complete offline operational guarantee",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # L4 - Card 2: External APIs & Rotated Key Pool
    l4_c2_x = 775
    b.add_rect(l4_c2_x, l4_cy, l4_cw, l4_ch, bg_color="#ffffff", stroke_color="#ffe066", stroke_width=1.5)
    b.add_text(l4_c2_x + 16, l4_cy + 12, "External APIs: Cloud LLMs & Live Search / Scrapers", font_size=15, color="#e67700")
    b.add_text(
        l4_c2_x + 16,
        l4_cy + 36,
        "• LLMs: Groq (13 keys, Qwen 2.5 72B / 3.8 27B) + Gemini (3 keys, Flash)\n"
        "• Web Search: Tavily Search API (7 keys, academic & government domain discovery)\n"
        "• Deep Scraping: Firecrawl (6 keys, JS portal render) + Jina Reader (1 key direct URL)\n"
        "• Automatic failover, multi-provider key rotation & 60s cooldown manager",
        font_size=12,
        color="#495057",
        line_height=1.35,
    )

    # ---------------------------------------------------------
    # 5. LEGEND & FOOTER
    # ---------------------------------------------------------
    LEG_Y = L4_Y + L4_H + 35  # 1375
    LEG_H = 50
    b.add_rect(
        CANVAS_X,
        LEG_Y,
        CANVAS_W,
        LEG_H,
        bg_color="#f8f9fa",
        stroke_color="#ced4da",
        stroke_width=1,
        rounded=True,
    )
    b.add_text(
        CENTER_X,
        LEG_Y + 16,
        "Architecture Legend:  [Blue] Next.js 15 UI  |  [Cyan] FastAPI & LangGraph  |  [Green] Discovery & Investigation  |  [Purple] Verification & Output  |  [Amber] Data & APIs",
        font_size=12,
        font_family=1,
        color="#495057",
        text_align="center",
    )

    return b.build_doc()


if __name__ == "__main__":
    doc = create_scholarx_diagram()

    target_paths = [
        "/mnt/windows/AntiGravity/SCHOLARX/docs/scholarx_architecture.excalidraw.json",
        "/mnt/windows/AntiGravity/SCHOLARX/scholarx_architecture.excalidraw.json",
    ]

    for path in target_paths:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2)
        print(f"Saved Excalidraw diagram to: {path}")

    # Validation
    for path in target_paths:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data["type"] == "excalidraw"
            assert data["version"] == 2
            assert len(data["elements"]) > 0
            print(f"Validated {path}: successfully loaded {len(data['elements'])} elements.")
