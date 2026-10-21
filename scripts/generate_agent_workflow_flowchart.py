#!/usr/bin/env python3
"""
SCHOLARX Agent & Workflow Collaboration Flowchart Generator
Generates a valid, highly detailed Excalidraw flowchart illustrating how
Autonomous LLM Agents (Purple) and Deterministic Workflows (Green) collaborate
within the LangGraph StateGraph (ScholarXState) and stream live events to FastAPI EventBus.
"""

import json
import os
import random

# Seed for deterministic IDs
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
        label_offset_x=0,
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
            mid_x = (x1 + x2) / 2 + label_offset_x
            mid_y = (y1 + y2) / 2 + label_offset_y
            self.add_text(
                mid_x,
                mid_y,
                label,
                font_size=11,
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


def create_agent_workflow_flowchart():
    b = ExcalidrawBuilder()

    # -------------------------------------------------------------------------
    # CANVAS & GRID LAYOUT
    # -------------------------------------------------------------------------
    CANVAS_X = 70
    CANVAS_W = 1800
    CENTER_X = CANVAS_X + CANVAS_W / 2  # 970

    # -------------------------------------------------------------------------
    # 1. TITLE BANNER
    # -------------------------------------------------------------------------
    BANNER_Y = 40
    BANNER_H = 100
    b.add_rect(
        CANVAS_X,
        BANNER_Y,
        CANVAS_W,
        BANNER_H,
        bg_color="#182234",
        stroke_color="#0f172a",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        CENTER_X,
        BANNER_Y + 16,
        "SCHOLARX — Agent & Workflow Collaboration Flowchart",
        font_size=23,
        font_family=1,
        color="#ffffff",
        text_align="center",
    )
    b.add_text(
        CENTER_X,
        BANNER_Y + 48,
        "How Autonomous LLM Agents & Deterministic Workflows Partner in LangGraph (Workflow-First Architecture)",
        font_size=13,
        font_family=1,
        color="#94a3b8",
        text_align="center",
    )
    b.add_text(
        CENTER_X,
        BANNER_Y + 73,
        "🟣 LLM Agents: Semantic Reasoning & Strategy  │  🟢 Workflows: Zero-Hallucination Math & Rules  │  🔵 LangGraph StateGraph (ScholarXState)  │  ⚡ FastAPI SSE Stream",
        font_size=11.5,
        font_family=1,
        color="#38bdf8",
        text_align="center",
    )

    # -------------------------------------------------------------------------
    # 2. COLUMN TRACK HEADERS
    # -------------------------------------------------------------------------
    COL1_X = 70
    COL1_W = 530

    COL2_X = 640
    COL2_W = 530

    COL3_X = 1210
    COL3_W = 660

    TRACK_Y = 160
    TRACK_H = 42

    # Track 1: Agents
    b.add_rect(
        COL1_X,
        TRACK_Y,
        COL1_W,
        TRACK_H,
        bg_color="#f3e8ff",
        stroke_color="#7950f2",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        COL1_X + COL1_W / 2,
        TRACK_Y + 12,
        "🧠 LLM AUTONOMOUS AGENTS (Semantic Reasoning & Strategy)",
        font_size=13.5,
        font_family=1,
        color="#5f3dc4",
        text_align="center",
    )

    # Track 2: Workflows
    b.add_rect(
        COL2_X,
        TRACK_Y,
        COL2_W,
        TRACK_H,
        bg_color="#ebfbee",
        stroke_color="#2f9e44",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        COL2_X + COL2_W / 2,
        TRACK_Y + 12,
        "⚙️ DETERMINISTIC WORKFLOWS (Zero-Hallucination Math & Rules)",
        font_size=13.5,
        font_family=1,
        color="#2b8a3e",
        text_align="center",
    )

    # Track 3: Architecture & State
    b.add_rect(
        COL3_X,
        TRACK_Y,
        COL3_W,
        TRACK_H,
        bg_color="#edf2ff",
        stroke_color="#4263eb",
        stroke_width=2,
        rounded=True,
    )
    b.add_text(
        COL3_X + COL3_W / 2,
        TRACK_Y + 12,
        "📊 SHARED STATE MACHINE & SYSTEM ARCHITECTURE",
        font_size=13.5,
        font_family=1,
        color="#364fc7",
        text_align="center",
    )

    # -------------------------------------------------------------------------
    # 3. PIPELINE STEP CARDS (COLUMNS 1 & 2)
    # -------------------------------------------------------------------------

    # --- STEP 1: Orchestrator Node (Agent) ---
    S1_Y = 225
    S1_H = 110
    b.add_rect(COL1_X, S1_Y, COL1_W, S1_H, bg_color="#ffffff", stroke_color="#9333ea", stroke_width=2)
    b.add_rect(COL1_X + 12, S1_Y + 12, 45, 22, bg_color="#f3e8ff", stroke_color="#7950f2", stroke_width=1)
    b.add_text(COL1_X + 19, S1_Y + 15, "01", font_size=12, color="#5f3dc4")
    b.add_text(COL1_X + 68, S1_Y + 14, "Orchestrator Node", font_size=15, color="#6b21a8")
    b.add_text(COL1_X + COL1_W - 135, S1_Y + 15, "[Agent 🧠 - Root]", font_size=11, color="#7c3aed")
    b.add_text(
        COL1_X + 16,
        S1_Y + 42,
        "• Root StateGraph node initializing pipeline session & mission directives\n"
        "• Validates student context and checks continuity with previous research\n"
        "• Emits MISSION_INITIATED and phase transition telemetry to FastAPI EventBus\n"
        "• Governs fallback strategies, API rotation & human approval interrupt gates",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Arrow 1 -> 2
    b.add_arrow(
        COL1_X + COL1_W / 2,
        S1_Y + S1_H,
        COL1_X + COL1_W / 2,
        S1_Y + S1_H + 30,
        color="#7950f2",
        stroke_width=2,
        label="Session Initialized",
        label_offset_y=-14,
        label_offset_x=70,
    )

    # --- STEP 2: Profile Analyzer Node (Agent) ---
    S2_Y = S1_Y + S1_H + 30  # 365
    S2_H = 110
    b.add_rect(COL1_X, S2_Y, COL1_W, S2_H, bg_color="#ffffff", stroke_color="#9333ea", stroke_width=2)
    b.add_rect(COL1_X + 12, S2_Y + 12, 45, 22, bg_color="#f3e8ff", stroke_color="#7950f2", stroke_width=1)
    b.add_text(COL1_X + 19, S2_Y + 15, "02", font_size=12, color="#5f3dc4")
    b.add_text(COL1_X + 68, S2_Y + 14, "Profile Analyzer Node", font_size=15, color="#6b21a8")
    b.add_text(COL1_X + COL1_W - 145, S2_Y + 15, "[Agent 🧠 - Ingestion]", font_size=11, color="#7c3aed")
    b.add_text(
        COL1_X + 16,
        S2_Y + 42,
        "• Ingests messy Pakistani academic records (Matric, FSc, BS, HSSC transcripts)\n"
        "• Normalizes GPA/CGPA percentages across Pakistani universities (NUST, FAST, PU)\n"
        "• Identifies Pakistan test scores: HEC HAT, USAT, IELTS/TOEFL or MOI waivers\n"
        "• Maps provincial domicile (Balochistan, Punjab, Sindh, KPK) & quota tags",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Arrow 2 -> 3
    b.add_arrow(
        COL1_X + COL1_W / 2,
        S2_Y + S2_H,
        COL1_X + COL1_W / 2,
        S2_Y + S2_H + 30,
        color="#7950f2",
        stroke_width=2,
        label="Structured StudentProfile",
        label_offset_y=-14,
        label_offset_x=85,
    )

    # --- STEP 3: Discovery Commander Node (Agent) ---
    S3_Y = S2_Y + S2_H + 30  # 505
    S3_H = 115
    b.add_rect(COL1_X, S3_Y, COL1_W, S3_H, bg_color="#ffffff", stroke_color="#9333ea", stroke_width=2)
    b.add_rect(COL1_X + 12, S3_Y + 12, 45, 22, bg_color="#f3e8ff", stroke_color="#7950f2", stroke_width=1)
    b.add_text(COL1_X + 19, S3_Y + 15, "03", font_size=12, color="#5f3dc4")
    b.add_text(COL1_X + 68, S3_Y + 14, "Discovery Commander Node", font_size=15, color="#6b21a8")
    b.add_text(COL1_X + COL1_W - 140, S3_Y + 15, "[Agent 🧠 - Strategy]", font_size=11, color="#7c3aed")
    b.add_text(
        COL1_X + 16,
        S3_Y + 42,
        "• Contextual query formulation: generates multi-lingual semantic search matrices\n"
        "• Injects Pakistan-specific search qualifiers ('HEC bilateral quota', 'MOI waiver')\n"
        "• Formulates targeted exploration mandates across 5 continental regions\n"
        "• Dispatches concurrent scraping directives to downstream deterministic scouts",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Handoff Arrow 1: From Step 3 (Agent) to Step 4 (Workflow)
    b.add_arrow(
        COL1_X + COL1_W,
        S3_Y + S3_H / 2,
        COL2_X,
        680,
        color="#7950f2",
        stroke_width=2.5,
        label="HANDOFF 1: Regional Search Directives & Queries",
        label_offset_y=-18,
        label_offset_x=-10,
    )

    # --- STEP 4: Regional Scouts (Workflow - 5 Parallel Pipelines) ---
    S4_Y = 650
    S4_H = 150
    b.add_rect(COL2_X, S4_Y, COL2_W, S4_H, bg_color="#ffffff", stroke_color="#16a34a", stroke_width=2)
    b.add_rect(COL2_X + 12, S4_Y + 12, 45, 22, bg_color="#ebfbee", stroke_color="#2f9e44", stroke_width=1)
    b.add_text(COL2_X + 19, S4_Y + 15, "04", font_size=12, color="#2b8a3e")
    b.add_text(COL2_X + 68, S4_Y + 14, "Regional Scouts", font_size=15, color="#15803d")
    b.add_text(COL2_X + COL2_W - 165, S4_Y + 15, "[Workflow ⚙️ - Parallel]", font_size=11, color="#16a34a")

    # 5 Region Badges
    scout_names = ["Europe Scout", "Asia Scout", "Americas Scout", "MENA Scout", "Oceania Scout"]
    badge_w = 94
    for i, name in enumerate(scout_names):
        bx = COL2_X + 16 + i * 100
        by = S4_Y + 40
        b.add_rect(bx, by, badge_w, 24, bg_color="#dcfce7", stroke_color="#86efac", stroke_width=1)
        b.add_text(bx + badge_w / 2, by + 5, name, font_size=10, color="#166534", text_align="center")

    b.add_text(
        COL2_X + 16,
        S4_Y + 74,
        "• 5 parallel deterministic execution pipelines: Search → Scrape → Extract → Normalize\n"
        "• Scans official portals (Stipendium Hungaricum, CSC, DAAD, Turkiye Burslari, MEXT)\n"
        "• Validates raw fields against Scholarship Pydantic schema (zero LLM hallucination)\n"
        "• Merges results into state: candidate_scholarships via merge_lists reducer",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Arrow 4 -> 5
    b.add_arrow(
        COL2_X + COL2_W / 2,
        S4_Y + S4_H,
        COL2_X + COL2_W / 2,
        S4_Y + S4_H + 30,
        color="#2f9e44",
        stroke_width=2,
        label="Candidate Scholarship Pool",
        label_offset_y=-14,
        label_offset_x=85,
    )

    # --- STEP 5: Eligibility Investigator (Workflow) ---
    S5_Y = S4_Y + S4_H + 30  # 830
    S5_H = 115
    b.add_rect(COL2_X, S5_Y, COL2_W, S5_H, bg_color="#ffffff", stroke_color="#16a34a", stroke_width=2)
    b.add_rect(COL2_X + 12, S5_Y + 12, 45, 22, bg_color="#ebfbee", stroke_color="#2f9e44", stroke_width=1)
    b.add_text(COL2_X + 19, S5_Y + 15, "05", font_size=12, color="#2b8a3e")
    b.add_text(COL2_X + 68, S5_Y + 14, "Eligibility Investigator", font_size=15, color="#15803d")
    b.add_text(COL2_X + COL2_W - 145, S5_Y + 15, "[Workflow ⚙️ - 15-Dim]", font_size=11, color="#16a34a")
    b.add_text(
        COL2_X + 16,
        S5_Y + 42,
        "• Strict 15-dimension deterministic boolean gating & academic threshold audit\n"
        "• Verifies GPA cutoff, age ceiling, degree level compatibility & nationality rules\n"
        "• Pakistan criteria: HEC HAT minimums, USAT validity, IELTS/TOEFL waiver rules\n"
        "• Generates pass/fail verdict breakdown: eligibility_results via merge_dicts",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Arrow 5 -> 6
    b.add_arrow(
        COL2_X + COL2_W / 2,
        S5_Y + S5_H,
        COL2_X + COL2_W / 2,
        S5_Y + S5_H + 30,
        color="#2f9e44",
        stroke_width=2,
        label="15-Dimension Eligible Candidates",
        label_offset_y=-14,
        label_offset_x=95,
    )

    # --- STEP 6: True Cost Analyzer (Workflow) ---
    S6_Y = S5_Y + S5_H + 30  # 975
    S6_H = 120
    b.add_rect(COL2_X, S6_Y, COL2_W, S6_H, bg_color="#ffffff", stroke_color="#16a34a", stroke_width=2)
    b.add_rect(COL2_X + 12, S6_Y + 12, 45, 22, bg_color="#ebfbee", stroke_color="#2f9e44", stroke_width=1)
    b.add_text(COL2_X + 19, S6_Y + 15, "06", font_size=12, color="#2b8a3e")
    b.add_text(COL2_X + 68, S6_Y + 14, "True Cost Analyzer", font_size=15, color="#15803d")
    b.add_text(COL2_X + COL2_W - 145, S6_Y + 15, "[Workflow ⚙️ - PKR Math]", font_size=11, color="#16a34a")
    b.add_text(
        COL2_X + 16,
        S6_Y + 42,
        "• Strict 4-phase PKR out-of-pocket math: Pre-App, App, Pre-Departure, Post-Arrival\n"
        "• Multi-currency foreign exchange conversion at live bank rates (EUR/USD/CNY → PKR)\n"
        "• Calculates FBR Section 236Y advance tax on credit card payments & bank drafts\n"
        "• Itemizes medical exams, courier, attestation & visa fees: cost_results in state",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Arrow 6 -> 7
    b.add_arrow(
        COL2_X + COL2_W / 2,
        S6_Y + S6_H,
        COL2_X + COL2_W / 2,
        S6_Y + S6_H + 30,
        color="#2f9e44",
        stroke_width=2,
        label="PKR Cost Audited Opportunities",
        label_offset_y=-14,
        label_offset_x=95,
    )

    # --- STEP 7: Deadline Intelligence (Workflow) ---
    S7_Y = S6_Y + S6_H + 30  # 1125
    S7_H = 115
    b.add_rect(COL2_X, S7_Y, COL2_W, S7_H, bg_color="#ffffff", stroke_color="#16a34a", stroke_width=2)
    b.add_rect(COL2_X + 12, S7_Y + 12, 45, 22, bg_color="#ebfbee", stroke_color="#2f9e44", stroke_width=1)
    b.add_text(COL2_X + 19, S7_Y + 15, "07", font_size=12, color="#2b8a3e")
    b.add_text(COL2_X + 68, S7_Y + 14, "Deadline Intelligence", font_size=15, color="#15803d")
    b.add_text(COL2_X + COL2_W - 145, S7_Y + 15, "[Workflow ⚙️ - Dates]", font_size=11, color="#16a34a")
    b.add_text(
        COL2_X + 16,
        S7_Y + 42,
        "• Pure date arithmetic: computes exact days remaining, slack days & milestone gates\n"
        "• Evaluates dual-gate deadlines (e.g. HEC portal cutoff vs foreign university portal)\n"
        "• Factors Pakistani lead times: HEC attestation (21d), MOFA (7d), visa wait (45d)\n"
        "• Assigns deadline health tags (GREEN / AMBER / RED): deadline_results in state",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Handoff Arrow 2: From Step 7 (Workflow) to Step 8 (Agent)
    b.add_arrow(
        COL2_X,
        S7_Y + S7_H / 2,
        COL1_X + COL1_W,
        1310,
        color="#16a34a",
        stroke_width=2.5,
        label="HANDOFF 2: Candidates Ready for Adversarial Red-Team Challenge",
        label_offset_y=-18,
        label_offset_x=20,
    )

    # --- STEP 8: Skeptic Agent (Agent - Adversarial Red-Team) ---
    S8_Y = 1270
    S8_H = 125
    b.add_rect(COL1_X, S8_Y, COL1_W, S8_H, bg_color="#fdf4ff", stroke_color="#c026d3", stroke_width=2.5)
    b.add_rect(COL1_X + 12, S8_Y + 12, 45, 22, bg_color="#fae8ff", stroke_color="#c026d3", stroke_width=1)
    b.add_text(COL1_X + 19, S8_Y + 15, "08", font_size=12, color="#a21caf")
    b.add_text(COL1_X + 68, S8_Y + 14, "Skeptic Agent (Red-Team)", font_size=15, color="#a21caf")
    b.add_text(COL1_X + COL1_W - 150, S8_Y + 15, "[Agent 🧠 - Adversary]", font_size=11, color="#c026d3")
    b.add_text(
        COL1_X + 16,
        S8_Y + 42,
        "• Deliberate adversarial challenge agent designed to find disqualifying traps\n"
        "• Scrutinizes mandatory return bonds (e.g. 5-year HEC service bond or penalty)\n"
        "• Audits embassy visa queue backlogs (VFS appointments, Islamabad police cert)\n"
        "• Uncovers stipend deficits vs actual living cost inflation in host cities\n"
        "• Outputs skeptic_challenges & confidence evidence trails to state",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Handoff Arrow 3: From Step 8 (Agent) to Step 9 (Workflow)
    b.add_arrow(
        COL1_X + COL1_W,
        S8_Y + S8_H / 2,
        COL2_X,
        1445,
        color="#c026d3",
        stroke_width=2.5,
        label="HANDOFF 3: Adversarial Risk Flags & Evidence Trails",
        label_offset_y=-18,
        label_offset_x=-10,
    )

    # --- STEP 9: Synthesis Engine (Workflow) ---
    S9_Y = 1415
    S9_H = 110
    b.add_rect(COL2_X, S9_Y, COL2_W, S9_H, bg_color="#ffffff", stroke_color="#16a34a", stroke_width=2)
    b.add_rect(COL2_X + 12, S9_Y + 12, 45, 22, bg_color="#ebfbee", stroke_color="#2f9e44", stroke_width=1)
    b.add_text(COL2_X + 19, S9_Y + 15, "09", font_size=12, color="#2b8a3e")
    b.add_text(COL2_X + 68, S9_Y + 14, "Synthesis Engine", font_size=15, color="#15803d")
    b.add_text(COL2_X + COL2_W - 145, S9_Y + 15, "[Workflow ⚙️ - Evidence]", font_size=11, color="#16a34a")
    b.add_text(
        COL2_X + 16,
        S9_Y + 42,
        "• Deterministic evidence aggregation: compiles Eligibility + Cost + Deadline + Skeptic\n"
        "• Deduplicates identical scholarship entries and reconciles multi-source discrepancies\n"
        "• Binds official primary sources, university URLs & embassy application guidelines\n"
        "• Packages candidate bundles into immutable ScholarX DNA evidence cards",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # Arrow 9 -> 10
    b.add_arrow(
        COL2_X + COL2_W / 2,
        S9_Y + S9_H,
        COL2_X + COL2_W / 2,
        S9_Y + S9_H + 30,
        color="#2f9e44",
        stroke_width=2,
        label="Unified Opportunity Bundles",
        label_offset_y=-14,
        label_offset_x=85,
    )

    # --- STEP 10: Ranking Engine (Workflow) ---
    S10_Y = S9_Y + S9_H + 30  # 1555
    S10_H = 125
    b.add_rect(COL2_X, S10_Y, COL2_W, S10_H, bg_color="#ffffff", stroke_color="#16a34a", stroke_width=2)
    b.add_rect(COL2_X + 12, S10_Y + 12, 45, 22, bg_color="#ebfbee", stroke_color="#2f9e44", stroke_width=1)
    b.add_text(COL2_X + 19, S10_Y + 15, "10", font_size=12, color="#2b8a3e")
    b.add_text(COL2_X + 68, S10_Y + 14, "Ranking Engine", font_size=15, color="#15803d")
    b.add_text(COL2_X + COL2_W - 145, S10_Y + 15, "[Workflow ⚙️ - Formula]", font_size=11, color="#16a34a")
    b.add_text(
        COL2_X + 16,
        S10_Y + 42,
        "• Evaluates deterministic 8-factor composite formula on a strict 100-point index:\n"
        "  - Academic Match (20%) + Full Coverage (15%) + Out-of-Pocket PKR Feasibility (15%)\n"
        "  - Visa Feasibility (10%) + Deadline Slack (10%) + Bilateral Pakistan Quota (10%)\n"
        "  - Field Match (10%) + Skeptic Confidence Score (10%)\n"
        "• Zero hallucination sorting produces fully reproducible ranked_results",
        font_size=11,
        color="#334155",
        line_height=1.35,
    )

    # Handoff Arrow 4: From Step 10 (Workflow) to Step 11 (Agent)
    b.add_arrow(
        COL2_X,
        S10_Y + S10_H / 2,
        COL1_X + COL1_W,
        1735,
        color="#16a34a",
        stroke_width=2.5,
        label="HANDOFF 4: Top Ranked Matches (>50.0 Score)",
        label_offset_y=-18,
        label_offset_x=20,
    )

    # --- STEP 11: Final Advisor Agent (Agent) ---
    S11_Y = 1695
    S11_H = 125
    b.add_rect(COL1_X, S11_Y, COL1_W, S11_H, bg_color="#ffffff", stroke_color="#9333ea", stroke_width=2)
    b.add_rect(COL1_X + 12, S11_Y + 12, 45, 22, bg_color="#f3e8ff", stroke_color="#7950f2", stroke_width=1)
    b.add_text(COL1_X + 19, S11_Y + 15, "11", font_size=12, color="#5f3dc4")
    b.add_text(COL1_X + 68, S11_Y + 14, "Final Advisor Agent", font_size=15, color="#6b21a8")
    b.add_text(COL1_X + COL1_W - 140, S11_Y + 15, "[Agent 🧠 - Advisory]", font_size=11, color="#7c3aed")
    b.add_text(
        COL1_X + 16,
        S11_Y + 42,
        "• Synthesizes deep strategic counsel and tactical advice for top-ranked opportunity\n"
        "• Builds personalized 6-phase application roadmap with actionable preparation steps\n"
        "• Formulates Pakistan office action plan (HEC attestation, MOFA, IBCC, NADRA FRC)\n"
        "• Generates tailored SOP / Motivation Letter angle aligned with student profile\n"
        "• Saves final_roadmap to state & marks active_phase = MISSION_COMPLETE",
        font_size=11.5,
        color="#334155",
        line_height=1.35,
    )

    # --- STEP 12: Human in the Loop (Web Dossier & PDF Export) ---
    S12_Y = 1850
    S12_H = 125
    S12_W = COL1_W + 40 + COL2_W  # Spans both columns: 1100 px
    b.add_rect(COL1_X, S12_Y, S12_W, S12_H, bg_color="#f0fdf4", stroke_color="#0284c7", stroke_width=2.5)
    b.add_rect(COL1_X + 12, S12_Y + 12, 45, 22, bg_color="#e0f2fe", stroke_color="#0284c7", stroke_width=1)
    b.add_text(COL1_X + 19, S12_Y + 15, "12", font_size=12, color="#0369a1")
    b.add_text(COL1_X + 68, S12_Y + 14, "Human in the Loop & Canonical Dossier Export", font_size=16, color="#0369a1")
    b.add_text(COL1_X + S12_W - 200, S12_Y + 15, "[Human / UI 👤 - Deliverable]", font_size=11, color="#0284c7")

    # Step 12 internal descriptions
    b.add_text(
        COL1_X + 16,
        S12_Y + 44,
        "• Interactive Web Dossier: Student inspects 15-dim audit breakdown, verified evidence citations & PKR costs\n"
        "• Adversarial Review: Student reviews Skeptic Agent challenges (bond traps, stipend limits, visa bottlenecks)\n"
        "• Human Approval Gate: Student can pause/resume graph (interrupt), confirm target universities & select routes\n"
        "• Canonical 6-Page PDF Export: Renders executive intelligence report, Pakistani checklist & timeline to disk",
        font_size=11.5,
        color="#1e293b",
        line_height=1.4,
    )

    # Arrow 11 -> 12
    b.add_arrow(
        COL1_X + COL1_W / 2,
        S11_Y + S11_H,
        COL1_X + COL1_W / 2,
        S12_Y,
        color="#0284c7",
        stroke_width=2.5,
        label="Dossier & Strategic Roadmap Ready for Student Review",
        label_offset_y=-14,
        label_offset_x=130,
    )

    # -------------------------------------------------------------------------
    # 4. SIDEBARS (COLUMN 3 - X: 1210 to 1870, W: 660)
    # -------------------------------------------------------------------------

    # --- SIDEBAR 1: Why Split Agent vs Workflow? ---
    SB1_Y = 225
    SB1_H = 370
    b.add_rect(COL3_X, SB1_Y, COL3_W, SB1_H, bg_color="#fffbeb", stroke_color="#f59e0b", stroke_width=2)
    b.add_text(COL3_X + 16, SB1_Y + 14, "💡 Workflow-First Philosophy: Why Split Agent vs Workflow?", font_size=15, color="#b45309")
    b.add_text(
        COL3_X + 16,
        SB1_Y + 36,
        "Core Rule: 'Never use an LLM for arithmetic, dates, or boolean rules that code can execute with 100% precision.'",
        font_size=11,
        color="#78350f",
    )

    # Mini Card A: LLM Agents
    MCA_W = 300
    MCA_H = 225
    MCA_X = COL3_X + 16
    MCA_Y = SB1_Y + 62
    b.add_rect(MCA_X, MCA_Y, MCA_W, MCA_H, bg_color="#ffffff", stroke_color="#c084fc", stroke_width=1.5)
    b.add_text(MCA_X + 12, MCA_Y + 12, "🧠 Use LLM Agent When:", font_size=13, color="#6b21a8")
    b.add_text(
        MCA_X + 12,
        MCA_Y + 34,
        "• Natural language reasoning & unstructured text\n"
        "• Parsing messy transcripts & ambiguous grades\n"
        "• Contextual query formulation for discovery\n"
        "• Adversarial red-teaming (finding bond traps,\n"
        "  visa backlogs, and stipend shortfalls)\n"
        "• Strategic narrative synthesis & roadmapping\n"
        "• Tailored motivation letter & SOP advice",
        font_size=11,
        color="#334155",
        line_height=1.35,
    )

    # Mini Card B: Workflows
    MCB_W = 300
    MCB_H = 225
    MCB_X = COL3_X + 344
    MCB_Y = SB1_Y + 62
    b.add_rect(MCB_X, MCB_Y, MCB_W, MCB_H, bg_color="#ffffff", stroke_color="#86efac", stroke_width=1.5)
    b.add_text(MCB_X + 12, MCB_Y + 12, "⚙️ Use Workflow When:", font_size=13, color="#15803d")
    b.add_text(
        MCB_X + 12,
        MCB_Y + 34,
        "• Multi-currency foreign exchange to PKR\n"
        "• FBR Section 236Y advance tax math\n"
        "• Strict date arithmetic & dual-gate slack days\n"
        "• 15-dimension boolean eligibility gating\n"
        "• Evidence aggregation & exact deduplication\n"
        "• Deterministic 8-factor ranking on 100-pt index\n"
        "• 100% reproducible results (0% hallucination)",
        font_size=11,
        color="#334155",
        line_height=1.35,
    )

    # Bottom summary in SB1
    b.add_rect(COL3_X + 16, SB1_Y + 300, COL3_W - 32, 52, bg_color="#fef3c7", stroke_color="#fbbf24", stroke_width=1)
    b.add_text(
        COL3_X + 24,
        SB1_Y + 308,
        "Architectural Payoff: Combining deterministic code with LLM reasoning delivers\n"
        "10x higher execution speed, 85% lower token costs, and 100% mathematical integrity.",
        font_size=11.5,
        color="#92400e",
        line_height=1.3,
    )

    # --- SIDEBAR 2: Shared State Machine (ScholarXState) ---
    SB2_Y = 620
    SB2_H = 490
    b.add_rect(COL3_X, SB2_Y, COL3_W, SB2_H, bg_color="#eff6ff", stroke_color="#3b82f6", stroke_width=2)
    b.add_text(COL3_X + 16, SB2_Y + 14, "🔄 Shared State Machine (ScholarXState)", font_size=15, color="#1d4ed8")
    b.add_text(
        COL3_X + 16,
        SB2_Y + 36,
        "LangGraph StateGraph typed dictionary with built-in reducer functions for seamless multi-agent state merging:",
        font_size=11,
        color="#1e40af",
    )

    # Dark Code Block for Schema
    CODE_X = COL3_X + 16
    CODE_Y = SB2_Y + 58
    CODE_W = COL3_W - 32
    CODE_H = 245
    b.add_rect(CODE_X, CODE_Y, CODE_W, CODE_H, bg_color="#0f172a", stroke_color="#1e293b", stroke_width=1.5)
    
    code_snippet = (
        "class ScholarXState(TypedDict, total=False):\n"
        "    session_id:             str\n"
        "    student_profile:        Optional[StudentProfile]\n"
        "    candidate_scholarships: Annotated[List[Scholarship], merge_lists]\n"
        "    eligibility_results:    Annotated[Dict[str, Any], merge_dicts]\n"
        "    cost_results:           Annotated[Dict[str, CostResult], merge_dicts]\n"
        "    deadline_results:       Annotated[Dict[str, DeadlineResult], merge_dicts]\n"
        "    evidence_trails:        Annotated[Dict[str, EvidenceTrail], merge_dicts]\n"
        "    skeptic_challenges:     Annotated[Dict[str, List[Challenge]], merge_dicts]\n"
        "    ranked_results:         List[CompositeScoreResult]\n"
        "    final_roadmap:          Optional[ApplicationRoadmap]\n"
        "    events_queue:           Annotated[List[ScholarXEvent], merge_lists]"
    )
    b.add_text(
        CODE_X + 14,
        CODE_Y + 12,
        code_snippet,
        font_size=10.5,
        font_family=3,
        color="#38bdf8",
        line_height=1.35,
    )

    # Reducer Annotations in SB2
    b.add_text(
        COL3_X + 16,
        SB2_Y + 315,
        "State Reducer Principles:\n"
        "• merge_lists(left, right): Combines candidate pools and event queues from concurrent\n"
        "  regional scouts without overwriting peer data.\n"
        "• merge_dicts(left, right): Accumulates stage outputs (eligibility, PKR cost models,\n"
        "  deadline calculations, skeptic red-team trails) into a unified dictionary indexed by ID.\n"
        "• Checkpointed State: Enables instantaneous pause/resume, audit replays, and rollback.",
        font_size=11,
        color="#1e3a8a",
        line_height=1.35,
    )

    # --- SIDEBAR 3: Real-time EventBus Integration (FastAPI SSE) ---
    SB3_Y = 1135
    SB3_H = 340
    b.add_rect(COL3_X, SB3_Y, COL3_W, SB3_H, bg_color="#f0fdfa", stroke_color="#14b8a6", stroke_width=2)
    b.add_text(COL3_X + 16, SB3_Y + 14, "⚡ Real-time EventBus Stream (FastAPI SSE)", font_size=15, color="#0f766e")
    b.add_text(
        COL3_X + 16,
        SB3_Y + 36,
        "Asynchronous event dispatching decoupled from graph execution for 60 FPS live UI updates:",
        font_size=11,
        color="#115e59",
    )

    # Event Flow Mini Diagram
    EF_X = COL3_X + 16
    EF_Y = SB3_Y + 58
    EF_W = COL3_W - 32
    EF_H = 140
    b.add_rect(EF_X, EF_Y, EF_W, EF_H, bg_color="#ffffff", stroke_color="#5eead4", stroke_width=1.5)
    
    # Nodes box
    b.add_rect(EF_X + 12, EF_Y + 14, 150, 48, bg_color="#f3e8ff", stroke_color="#7950f2", stroke_width=1)
    b.add_text(EF_X + 87, EF_Y + 22, "Any Node / Agent", font_size=11, color="#6b21a8", text_align="center")
    b.add_text(EF_X + 87, EF_Y + 38, "_dispatch_live(evt)", font_size=9.5, color="#7c3aed", font_family=3, text_align="center")

    # Arrow to Bus
    b.add_arrow(EF_X + 162, EF_Y + 38, EF_X + 220, EF_Y + 38, color="#0d9488", stroke_width=1.5)

    # Bus box
    b.add_rect(EF_X + 220, EF_Y + 14, 160, 48, bg_color="#ccfbf1", stroke_color="#0d9488", stroke_width=1)
    b.add_text(EF_X + 300, EF_Y + 22, "FastAPI EventBus", font_size=11, color="#0f766e", text_align="center")
    b.add_text(EF_X + 300, EF_Y + 38, "InMemoryEventBus", font_size=9.5, color="#115e59", font_family=3, text_align="center")

    # Arrow to UI
    b.add_arrow(EF_X + 380, EF_Y + 38, EF_X + 440, EF_Y + 38, color="#0d9488", stroke_width=1.5)

    # UI box
    b.add_rect(EF_X + 440, EF_Y + 14, 170, 48, bg_color="#e0f2fe", stroke_color="#0284c7", stroke_width=1)
    b.add_text(EF_X + 525, EF_Y + 22, "Next.js 15 UI", font_size=11, color="#0369a1", text_align="center")
    b.add_text(EF_X + 525, EF_Y + 38, "EventSource / SSE", font_size=9.5, color="#0284c7", font_family=3, text_align="center")

    # Event types below
    b.add_text(
        EF_X + 14,
        EF_Y + 75,
        "Telemetry Events Dispatched in Real Time:\n"
        "• MISSION_INITIATED  • PROFILE_COMPLETE  • SCOUT_DISPATCHED  • SCHOLARSHIP_FOUND\n"
        "• ELIGIBILITY_EVALUATED  • COST_ANALYZED  • SKEPTIC_FLAGGED  • ROADMAP_GENERATED",
        font_size=10.5,
        color="#334155",
        line_height=1.35,
    )

    b.add_text(
        COL3_X + 16,
        SB3_Y + 215,
        "Key Benefits of Decoupled Streaming:\n"
        "• Zero pipeline blocking: LangGraph advances without waiting for frontend rendering.\n"
        "• Live Command Theatre: Displays active agent thoughts, candidate counters & radar updates.\n"
        "• Graceful degradation: If SSE client disconnects, graph execution continues unaffected.",
        font_size=11,
        color="#134e4a",
        line_height=1.35,
    )

    # --- SIDEBAR 4: Legend & Visual Notation ---
    SB4_Y = 1500
    SB4_H = 320
    b.add_rect(COL3_X, SB4_Y, COL3_W, SB4_H, bg_color="#f8fafc", stroke_color="#94a3b8", stroke_width=2)
    b.add_text(COL3_X + 16, SB4_Y + 14, "🏷️ Flowchart Legend & Node Classification", font_size=15, color="#334155")

    # 4 Legend Items
    # Item 1: Purple
    b.add_rect(COL3_X + 16, SB4_Y + 42, 28, 20, bg_color="#f3e8ff", stroke_color="#9333ea", stroke_width=1.5)
    b.add_text(COL3_X + 54, SB4_Y + 44, "LLM Autonomous Agent (Purple)", font_size=12, color="#6b21a8")
    b.add_text(
        COL3_X + 54,
        SB4_Y + 62,
        "Cognitive reasoning, prompt formulation, adversarial challenge & strategic roadmapping.",
        font_size=10.5,
        color="#64748b",
    )

    # Item 2: Green
    b.add_rect(COL3_X + 16, SB4_Y + 92, 28, 20, bg_color="#ebfbee", stroke_color="#16a34a", stroke_width=1.5)
    b.add_text(COL3_X + 54, SB4_Y + 94, "Deterministic Workflow (Green)", font_size=12, color="#15803d")
    b.add_text(
        COL3_X + 54,
        SB4_Y + 112,
        "Zero-hallucination Python code: 15-dim boolean audits, PKR math, date calculations & ranking.",
        font_size=10.5,
        color="#64748b",
    )

    # Item 3: Blue
    b.add_rect(COL3_X + 16, SB4_Y + 142, 28, 20, bg_color="#eff6ff", stroke_color="#3b82f6", stroke_width=1.5)
    b.add_text(COL3_X + 54, SB4_Y + 144, "LangGraph StateGraph & Reducers (Blue)", font_size=12, color="#1d4ed8")
    b.add_text(
        COL3_X + 54,
        SB4_Y + 162,
        "Immutable TypedDict shared state; uses merge_lists and merge_dicts for peer aggregation.",
        font_size=10.5,
        color="#64748b",
    )

    # Item 4: Cyan / Slate
    b.add_rect(COL3_X + 16, SB4_Y + 192, 28, 20, bg_color="#f0fdf4", stroke_color="#0284c7", stroke_width=1.5)
    b.add_text(COL3_X + 54, SB4_Y + 194, "Human in the Loop & Canonical Dossier (Cyan)", font_size=12, color="#0369a1")
    b.add_text(
        COL3_X + 54,
        SB4_Y + 212,
        "Interactive student inspection, approval gates, and authoritative 6-page PDF exports.",
        font_size=10.5,
        color="#64748b",
    )

    # Connectors explanation
    b.add_rect(COL3_X + 16, SB4_Y + 242, 28, 20, bg_color="#f8fafc", stroke_color="#475569", stroke_width=1.5)
    b.add_text(COL3_X + 54, SB4_Y + 244, "Connecting Arrows (Handoffs & State Transitions)", font_size=12, color="#334155")
    b.add_text(
        COL3_X + 54,
        SB4_Y + 262,
        "Solid arrows show LangGraph state execution order; diagonal arrows represent cross-paradigm handoffs.",
        font_size=10.5,
        color="#64748b",
    )

    # -------------------------------------------------------------------------
    # 5. DATA CONDUIT ARROWS (PIPELINE TO STATE & EVENTBUS)
    # -------------------------------------------------------------------------
    # Conduit 1: From Pipeline into Shared State Machine
    b.add_arrow(
        COL2_X + COL2_W,
        880,
        COL3_X,
        880,
        color="#3b82f6",
        stroke_width=2,
        stroke_style="dashed",
        label="State Updates via Reducers",
        label_offset_y=-14,
        label_offset_x=-20,
    )

    # Conduit 2: From Pipeline into FastAPI EventBus
    b.add_arrow(
        COL2_X + COL2_W,
        1300,
        COL3_X,
        1300,
        color="#14b8a6",
        stroke_width=2,
        stroke_style="dashed",
        label="Telemetry via EventBus.publish()",
        label_offset_y=-14,
        label_offset_x=-25,
    )

    # -------------------------------------------------------------------------
    # 6. FOOTER BANNER
    # -------------------------------------------------------------------------
    FOOTER_Y = 1995
    FOOTER_H = 50
    b.add_rect(
        CANVAS_X,
        FOOTER_Y,
        CANVAS_W,
        FOOTER_H,
        bg_color="#182234",
        stroke_color="#0f172a",
        stroke_width=1.5,
        rounded=True,
    )
    b.add_text(
        CENTER_X,
        FOOTER_Y + 16,
        "SCHOLARX Architectural Blueprint  │  LangGraph 0.2+ StateGraph  │  Workflow-First Philosophy  │  FastAPI EventBus  │  Next.js 15 UI",
        font_size=12,
        font_family=1,
        color="#94a3b8",
        text_align="center",
    )

    return b.build_doc()


if __name__ == "__main__":
    doc = create_agent_workflow_flowchart()

    target_paths = [
        "/mnt/windows/AntiGravity/SCHOLARX/docs/agent_workflow_flowchart.excalidraw.json",
        "/mnt/windows/AntiGravity/SCHOLARX/agent_workflow_flowchart.excalidraw.json",
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
