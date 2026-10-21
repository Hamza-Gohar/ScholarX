"""
Native PowerPoint Presentation Generator
Creates the 8-slide ScholarX Exhibition Deck using the Korean Minimalist Aesthetic.
"""

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

# Color Definitions
CLR_DARK = RGBColor(31, 31, 31)         # #1F1F1F
CLR_MOCHA = RGBColor(125, 102, 82)      # #7D6652
CLR_MUTED = RGBColor(95, 95, 95)        # #5F5F5F
CLR_BODY = RGBColor(50, 50, 50)         # #323232
CLR_LINE = RGBColor(196, 141, 128)      # #C48D80
CLR_CARD_BG = RGBColor(252, 250, 247)   # Very light warm ivory
CLR_CARD_BORDER = RGBColor(230, 224, 218)

PEBBLE_COLORS = [
    {"bg": RGBColor(221, 226, 216), "text": RGBColor(65, 78, 62)},   # Sage
    {"bg": RGBColor(245, 229, 224), "text": RGBColor(128, 70, 62)},  # Blush
    {"bg": RGBColor(234, 230, 224), "text": RGBColor(85, 82, 76)},   # Warm Stone
    {"bg": RGBColor(240, 234, 225), "text": RGBColor(112, 98, 82)},  # Oat Sand
    {"bg": RGBColor(237, 224, 212), "text": RGBColor(105, 78, 62)},  # Clay
    {"bg": RGBColor(225, 230, 232), "text": RGBColor(68, 85, 92)},   # Slate
]


def add_header(slide, category, title_dark, title_accent, subtitle, title_size=23):
    """
    Adds a unified Korean minimalist slide header in a single text frame.
    Prevents any text overlap between category, title, and subtitle.
    """
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(8.4), Inches(1.35))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    # Category tag
    p_cat = tf.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.name = "Arial"
    p_cat.font.size = Pt(9.5)
    p_cat.font.bold = True
    p_cat.font.color.rgb = CLR_MOCHA
    p_cat.space_after = Pt(4)

    # Main Split Title
    p_t = tf.add_paragraph()
    run_dark = p_t.add_run()
    run_dark.text = title_dark + " "
    run_dark.font.name = "Arial"
    run_dark.font.size = Pt(title_size)
    run_dark.font.bold = True
    run_dark.font.color.rgb = CLR_DARK
    
    run_acc = p_t.add_run()
    run_acc.text = title_accent
    run_acc.font.name = "Arial"
    run_acc.font.size = Pt(title_size)
    run_acc.font.bold = True
    run_acc.font.color.rgb = CLR_MOCHA
    p_t.space_after = Pt(4)

    # Subtitle
    if subtitle:
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = CLR_MUTED


def build_slide_1_hero(slide, data):
    """Builds Slide 1: Hero / Introductory Cover."""
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.05), Inches(8.4), Inches(1.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p_cat = tf.paragraphs[0]
    p_cat.text = data["category"].upper()
    p_cat.font.name = "Arial"
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = CLR_MOCHA
    p_cat.space_after = Pt(8)
    
    p_t = tf.add_paragraph()
    r_dark = p_t.add_run()
    r_dark.text = data["title_dark"]
    r_dark.font.name = "Arial"
    r_dark.font.size = Pt(44)
    r_dark.font.bold = True
    r_dark.font.color.rgb = CLR_DARK
    
    r_acc = p_t.add_run()
    r_acc.text = data["title_accent"]
    r_acc.font.name = "Arial"
    r_acc.font.size = Pt(44)
    r_acc.font.bold = True
    r_acc.font.color.rgb = CLR_MOCHA
    p_t.space_after = Pt(12)
    
    p_sub = tf.add_paragraph()
    p_sub.text = data["subtitle"]
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = CLR_BODY

    # 3 Highlight Cards at the bottom
    card_w = Inches(2.65)
    card_h = Inches(1.6)
    start_x = Inches(0.8)
    gap = Inches(0.22)
    top_y = Inches(3.4)

    for i, h in enumerate(data["highlights"]):
        x = start_x + i * (card_w + gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top_y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CLR_CARD_BG
        card.line.color.rgb = CLR_CARD_BORDER
        card.line.width = Pt(1)
        card.adjustments[0] = 0.12

        # Pebble badge
        pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.18), top_y + Inches(0.18), Inches(0.48), Inches(0.32))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.fill.background()
        pb.adjustments[0] = 0.35
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = h["badge"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(10)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        # Text inside card
        tb = slide.shapes.add_textbox(x + Inches(0.18), top_y + Inches(0.58), card_w - Inches(0.36), card_h - Inches(0.65))
        tf_c = tb.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = tf_c.margin_bottom = 0
        
        p1 = tf_c.paragraphs[0]
        p1.text = h["title"]
        p1.font.name = "Arial"
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = CLR_DARK
        p1.space_after = Pt(4)
        
        p2 = tf_c.add_paragraph()
        p2.text = h["desc"]
        p2.font.name = "Arial"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = CLR_MUTED


def build_slide_concept_split(slide, data):
    """Builds Slide 2 (AI Agent) & Slide 3 (Workflow): 2-Column Split Concept."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=25)

    left_x = Inches(0.8)
    left_y = Inches(1.85)
    left_w = Inches(3.6)
    left_h = Inches(3.25)

    bg_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, left_y, left_w, left_h)
    bg_box.fill.solid()
    bg_box.fill.fore_color.rgb = CLR_CARD_BG
    bg_box.line.color.rgb = CLR_CARD_BORDER
    bg_box.line.width = Pt(1)
    bg_box.adjustments[0] = 0.08

    tb_left = slide.shapes.add_textbox(left_x + Inches(0.25), left_y + Inches(0.25), left_w - Inches(0.5), left_h - Inches(0.5))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = 0

    p_tag = tf_l.paragraphs[0]
    p_tag.text = "CORE FOUNDATION"
    p_tag.font.name = "Arial"
    p_tag.font.size = Pt(9)
    p_tag.font.bold = True
    p_tag.font.color.rgb = CLR_MOCHA
    p_tag.space_after = Pt(8)

    p_h = tf_l.add_paragraph()
    p_h.text = data["core_definition"]["headline"]
    p_h.font.name = "Arial"
    p_h.font.size = Pt(14)
    p_h.font.bold = True
    p_h.font.color.rgb = CLR_DARK
    p_h.space_after = Pt(10)

    p_desc = tf_l.add_paragraph()
    p_desc.text = data["core_definition"]["text"]
    p_desc.font.name = "Arial"
    p_desc.font.size = Pt(10.5)
    p_desc.font.color.rgb = CLR_BODY

    # Right Column: 4 Pillars (2x2 mini cards)
    right_x = Inches(4.65)
    col_w = Inches(2.15)
    row_h = Inches(1.52)
    gap_x = Inches(0.25)
    gap_y = Inches(0.2)

    for i, p in enumerate(data["pillars"]):
        col = i % 2
        row = i // 2
        x = right_x + col * (col_w + gap_x)
        y = left_y + row * (row_h + gap_y)

        mc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, col_w, row_h)
        mc.fill.solid()
        mc.fill.fore_color.rgb = CLR_CARD_BG
        mc.line.color.rgb = CLR_CARD_BORDER
        mc.line.width = Pt(1)
        mc.adjustments[0] = 0.12

        pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.12), y + Inches(0.12), Inches(0.42), Inches(0.28))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.fill.background()
        pb.adjustments[0] = 0.35
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = p["badge"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(9.5)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        tb = slide.shapes.add_textbox(x + Inches(0.12), y + Inches(0.46), col_w - Inches(0.24), row_h - Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = p["title"]
        p1.font.name = "Arial"
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = CLR_DARK
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = p["desc"]
        p2.font.name = "Arial"
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = CLR_MUTED


def build_slide_comparison(slide, data):
    """Builds Slide 4: Agents vs Workflows (Comparison Matrix & Synergy)."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=23)

    card_w = Inches(4.1)
    card_h = Inches(2.25)
    start_y = Inches(1.85)

    # Left: AI Agents
    c_left = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), start_y, card_w, card_h)
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = CLR_CARD_BG
    c_left.line.color.rgb = CLR_CARD_BORDER
    c_left.line.width = Pt(1)
    c_left.adjustments[0] = 0.08

    tb_l = slide.shapes.add_textbox(Inches(1.0), start_y + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = 0

    p_lh = tf_l.paragraphs[0]
    p_lh.text = data["agent_side"]["badge"]
    p_lh.font.name = "Arial"
    p_lh.font.size = Pt(13)
    p_lh.font.bold = True
    p_lh.font.color.rgb = CLR_DARK
    p_lh.space_after = Pt(2)

    p_lsub = tf_l.add_paragraph()
    p_lsub.text = data["agent_side"]["subtitle"]
    p_lsub.font.name = "Arial"
    p_lsub.font.size = Pt(9.5)
    p_lsub.font.color.rgb = CLR_MOCHA
    p_lsub.space_after = Pt(6)

    for pt in data["agent_side"]["points"]:
        p = tf_l.add_paragraph()
        p.text = "• " + pt
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.color.rgb = CLR_BODY
        p.space_after = Pt(2.5)

    # Right: Workflows
    c_right = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.1), start_y, card_w, card_h)
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = CLR_CARD_BG
    c_right.line.color.rgb = CLR_CARD_BORDER
    c_right.line.width = Pt(1)
    c_right.adjustments[0] = 0.08

    tb_r = slide.shapes.add_textbox(Inches(5.3), start_y + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = tf_r.margin_bottom = 0

    p_rh = tf_r.paragraphs[0]
    p_rh.text = data["workflow_side"]["badge"]
    p_rh.font.name = "Arial"
    p_rh.font.size = Pt(13)
    p_rh.font.bold = True
    p_rh.font.color.rgb = CLR_DARK
    p_rh.space_after = Pt(2)

    p_rsub = tf_r.add_paragraph()
    p_rsub.text = data["workflow_side"]["subtitle"]
    p_rsub.font.name = "Arial"
    p_rsub.font.size = Pt(9.5)
    p_rsub.font.color.rgb = CLR_MOCHA
    p_rsub.space_after = Pt(6)

    for pt in data["workflow_side"]["points"]:
        p = tf_r.add_paragraph()
        p.text = "• " + pt
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.color.rgb = CLR_BODY
        p.space_after = Pt(2.5)

    # Bottom Synergy Banner
    syn_y = Inches(4.25)
    syn_w = Inches(8.4)
    syn_h = Inches(0.85)

    syn_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), syn_y, syn_w, syn_h)
    syn_box.fill.solid()
    syn_box.fill.fore_color.rgb = PEBBLE_COLORS[0]["bg"]
    syn_box.line.color.rgb = CLR_MOCHA
    syn_box.line.width = Pt(1)
    syn_box.adjustments[0] = 0.12

    tb_s = slide.shapes.add_textbox(Inches(1.0), syn_y + Inches(0.1), syn_w - Inches(0.4), syn_h - Inches(0.2))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_right = tf_s.margin_top = tf_s.margin_bottom = 0

    p_st = tf_s.paragraphs[0]
    p_st.text = data["synergy_callout"]["title"]
    p_st.font.name = "Arial"
    p_st.font.size = Pt(11)
    p_st.font.bold = True
    p_st.font.color.rgb = CLR_DARK
    p_st.space_after = Pt(2)

    p_sd = tf_s.add_paragraph()
    p_sd.text = data["synergy_callout"]["desc"]
    p_sd.font.name = "Arial"
    p_sd.font.size = Pt(9.5)
    p_sd.font.color.rgb = CLR_BODY


def build_slide_innovation(slide, data):
    """Builds Slide 5: World-First Innovation for Pakistan (4 Cards)."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=23)

    card_w = Inches(4.1)
    card_h = Inches(1.52)
    gap_x = Inches(0.2)
    gap_y = Inches(0.2)
    start_x = Inches(0.8)
    start_y = Inches(1.85)

    for i, c in enumerate(data["cards"]):
        col = i % 2
        row = i // 2
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CLR_CARD_BG
        card.line.color.rgb = CLR_CARD_BORDER
        card.line.width = Pt(1)
        card.adjustments[0] = 0.1

        pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.15), y + Inches(0.14), Inches(0.42), Inches(0.28))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.fill.background()
        pb.adjustments[0] = 0.35
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = c["badge"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(9.5)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        tb = slide.shapes.add_textbox(x + Inches(0.15), y + Inches(0.46), card_w - Inches(0.3), card_h - Inches(0.52))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = c["title"]
        p1.font.name = "Arial"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = CLR_DARK
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = c["desc"]
        p2.font.name = "Arial"
        p2.font.size = Pt(9)
        p2.font.color.rgb = CLR_MUTED


def build_slide_architecture(slide, data):
    """Builds Slide 6: System Architecture Topology (4 Stacked Tiers)."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=23)

    start_x = Inches(0.8)
    start_y = Inches(1.85)
    tier_w = Inches(8.4)
    tier_h = Inches(0.72)
    gap_y = Inches(0.12)

    for i, t in enumerate(data["tiers"]):
        y = start_y + i * (tier_h + gap_y)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, start_x, y, tier_w, tier_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CLR_CARD_BG
        card.line.color.rgb = CLR_CARD_BORDER
        card.line.width = Pt(1)
        card.adjustments[0] = 0.15

        pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, start_x + Inches(0.15), y + Inches(0.14), Inches(1.8), Inches(0.44))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.fill.background()
        pb.adjustments[0] = 0.25
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = t["level"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(8.5)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        tb = slide.shapes.add_textbox(start_x + Inches(2.1), y + Inches(0.1), tier_w - Inches(2.25), tier_h - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = t["name"]
        p1.font.name = "Arial"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = CLR_DARK

        p2 = tf.add_paragraph()
        p2.text = t["role"]
        p2.font.name = "Arial"
        p2.font.size = Pt(9)
        p2.font.color.rgb = CLR_MUTED


def build_slide_workflow(slide, data):
    """Builds Slide 7: System Workflow Pipeline (6 Connected Steps)."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=23)

    start_x = Inches(0.8)
    total_w = Inches(8.4)
    step_w = Inches(1.3)
    gap_x = (total_w - (step_w * 6)) / 5
    start_y = Inches(2.35)

    line_y = start_y + Inches(0.35)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, start_x + Inches(0.4), line_y, total_w - Inches(0.8), Pt(2))
    line.fill.solid()
    line.fill.fore_color.rgb = CLR_LINE
    line.line.fill.background()

    for i, s in enumerate(data["steps"]):
        x = start_x + i * (step_w + gap_x)

        pb = slide.shapes.add_shape(MSO_SHAPE.OVAL, x + (step_w - Inches(0.7))/2, start_y, Inches(0.7), Inches(0.7))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.color.rgb = CLR_CARD_BORDER
        pb.line.width = Pt(1)
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = s["step"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(13)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        tb = slide.shapes.add_textbox(x, start_y + Inches(0.85), step_w, Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = s["title"]
        p1.alignment = PP_ALIGN.CENTER
        p1.font.name = "Arial"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = CLR_DARK
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = s["desc"]
        p2.alignment = PP_ALIGN.CENTER
        p2.font.name = "Arial"
        p2.font.size = Pt(8)
        p2.font.color.rgb = CLR_MUTED


def build_slide_benefits(slide, data):
    """Builds Slide 8: Student Benefits & Impact (3 Stat Cards)."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=24)

    start_x = Inches(0.8)
    card_w = Inches(2.65)
    gap_x = Inches(0.22)
    start_y = Inches(1.85)
    card_h = Inches(3.25)

    for i, b in enumerate(data["benefits"]):
        x = start_x + i * (card_w + gap_x)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, start_y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CLR_CARD_BG
        card.line.color.rgb = CLR_CARD_BORDER
        card.line.width = Pt(1)
        card.adjustments[0] = 0.08

        pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.2), start_y + Inches(0.2), Inches(0.48), Inches(0.32))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.fill.background()
        pb.adjustments[0] = 0.35
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = b["badge"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(10)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        tb = slide.shapes.add_textbox(x + Inches(0.2), start_y + Inches(0.68), card_w - Inches(0.4), card_h - Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p_stat = tf.paragraphs[0]
        p_stat.text = b["stat"]
        p_stat.font.name = "Arial"
        p_stat.font.size = Pt(20)
        p_stat.font.bold = True
        p_stat.font.color.rgb = CLR_MOCHA
        p_stat.space_after = Pt(6)

        p_title = tf.add_paragraph()
        p_title.text = b["title"]
        p_title.font.name = "Arial"
        p_title.font.size = Pt(12)
        p_title.font.bold = True
        p_title.font.color.rgb = CLR_DARK
        p_title.space_after = Pt(8)

        p_desc = tf.add_paragraph()
        p_desc.text = b["desc"]
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = CLR_MUTED


def build_slide_team_credits(slide, data):
    """Builds Slide 9: Creators & Academic Leadership (2 Developer Cards + 1 Supervisor Banner)."""
    add_header(slide, data["category"], data["title_dark"], data["title_accent"], data["subtitle"], title_size=24)

    card_w = Inches(4.1)
    card_h = Inches(2.15)
    start_y = Inches(1.85)

    # 2 Developer Cards
    for i, dev in enumerate(data["developers"]):
        x = Inches(0.8) if i == 0 else Inches(5.1)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, start_y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CLR_CARD_BG
        card.line.color.rgb = CLR_CARD_BORDER
        card.line.width = Pt(1)
        card.adjustments[0] = 0.08

        # Pebble badge
        pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.2), start_y + Inches(0.18), Inches(0.48), Inches(0.32))
        pb.fill.solid()
        pb.fill.fore_color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["bg"]
        pb.line.fill.background()
        pb.adjustments[0] = 0.35
        p_tf = pb.text_frame
        p_tf.margin_left = p_tf.margin_right = p_tf.margin_top = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.text = dev["badge"]
        pp.alignment = PP_ALIGN.CENTER
        pp.font.name = "Arial"
        pp.font.size = Pt(10)
        pp.font.bold = True
        pp.font.color.rgb = PEBBLE_COLORS[i % len(PEBBLE_COLORS)]["text"]

        # Content
        tb = slide.shapes.add_textbox(x + Inches(0.2), start_y + Inches(0.6), card_w - Inches(0.4), card_h - Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        # Role Tag
        p_role = tf.paragraphs[0]
        p_role.text = dev["role_tag"].upper()
        p_role.font.name = "Arial"
        p_role.font.size = Pt(8.5)
        p_role.font.bold = True
        p_role.font.color.rgb = CLR_MOCHA
        p_role.space_after = Pt(2)

        # Name
        p_name = tf.add_paragraph()
        p_name.text = dev["name"]
        p_name.font.name = "Arial"
        p_name.font.size = Pt(15)
        p_name.font.bold = True
        p_name.font.color.rgb = CLR_DARK
        p_name.space_after = Pt(6)

        # Description
        p_desc = tf.add_paragraph()
        p_desc.text = dev["desc"]
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = CLR_BODY

    # Supervisor Banner
    sup_y = Inches(4.18)
    sup_w = Inches(8.4)
    sup_h = Inches(0.95)

    sup_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), sup_y, sup_w, sup_h)
    sup_box.fill.solid()
    sup_box.fill.fore_color.rgb = PEBBLE_COLORS[2]["bg"]
    sup_box.line.color.rgb = CLR_MOCHA
    sup_box.line.width = Pt(1)
    sup_box.adjustments[0] = 0.12

    # Left Badge
    badge_w = Inches(1.5)
    badge_h = Inches(0.42)
    s_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), sup_y + Inches(0.26), badge_w, badge_h)
    s_badge.fill.solid()
    s_badge.fill.fore_color.rgb = CLR_CARD_BG
    s_badge.line.color.rgb = CLR_MOCHA
    s_badge.line.width = Pt(1)
    s_badge.adjustments[0] = 0.25
    s_tf = s_badge.text_frame
    s_tf.margin_left = s_tf.margin_right = s_tf.margin_top = s_tf.margin_bottom = 0
    sp_p = s_tf.paragraphs[0]
    sp_p.text = data["supervisor"]["badge"]
    sp_p.alignment = PP_ALIGN.CENTER
    sp_p.font.name = "Arial"
    sp_p.font.size = Pt(8.5)
    sp_p.font.bold = True
    sp_p.font.color.rgb = CLR_MOCHA

    # Supervisor Details
    tb_sup = slide.shapes.add_textbox(Inches(2.65), sup_y + Inches(0.12), sup_w - Inches(1.95), sup_h - Inches(0.24))
    tf_sup = tb_sup.text_frame
    tf_sup.word_wrap = True
    tf_sup.margin_left = tf_sup.margin_right = tf_sup.margin_top = tf_sup.margin_bottom = 0

    p_sname = tf_sup.paragraphs[0]
    r_name = p_sname.add_run()
    r_name.text = data["supervisor"]["name"] + "  "
    r_name.font.name = "Arial"
    r_name.font.size = Pt(13)
    r_name.font.bold = True
    r_name.font.color.rgb = CLR_DARK

    r_srole = p_sname.add_run()
    r_srole.text = "•  " + data["supervisor"]["role_tag"]
    r_srole.font.name = "Arial"
    r_srole.font.size = Pt(9.5)
    r_srole.font.bold = True
    r_srole.font.color.rgb = CLR_MOCHA
    p_sname.space_after = Pt(2)

    p_sdesc = tf_sup.add_paragraph()
    p_sdesc.text = data["supervisor"]["desc"]
    p_sdesc.font.name = "Arial"
    p_sdesc.font.size = Pt(9)
    p_sdesc.font.color.rgb = CLR_BODY


def generate_pptx_deck(template_path, output_path, slides_data):
    """
    Builds the presentation using the Korean minimalist master template.
    Preserves original vector blobs and layouts while clearing default text.
    """
    prs = pptx.Presentation(template_path)
    
    # Selected slide indices from 84-slide template with ideal layouts
    chosen_indices = [0, 15, 6, 34, 2, 26, 25, 12, 27]
    
    # If slides_data has more or fewer slides, dynamically slice or match
    if len(slides_data) < len(chosen_indices):
        chosen_indices = chosen_indices[:len(slides_data)]
    
    sldIdLst = prs.slides._sldIdLst
    all_sldIds = list(sldIdLst)
    
    for idx, sldId in enumerate(all_sldIds):
        if idx not in chosen_indices:
            sldIdLst.remove(sldId)
    
    for idx, slide in enumerate(prs.slides):
        for shape in list(slide.shapes):
            sp = shape._element
            sp.getparent().remove(sp)
        
        slide_info = slides_data[idx]
        stype = slide_info["type"]
        
        if stype == "hero_cover":
            build_slide_1_hero(slide, slide_info)
        elif stype == "concept_split":
            build_slide_concept_split(slide, slide_info)
        elif stype == "comparison_matrix":
            build_slide_comparison(slide, slide_info)
        elif stype == "innovation_showcase":
            build_slide_innovation(slide, slide_info)
        elif stype == "architecture_topology":
            build_slide_architecture(slide, slide_info)
        elif stype == "workflow_pipeline":
            build_slide_workflow(slide, slide_info)
        elif stype == "benefits_impact":
            build_slide_benefits(slide, slide_info)
        elif stype == "team_credits":
            build_slide_team_credits(slide, slide_info)
    
    prs.save(output_path)
    print(f"Successfully generated PPTX: {output_path}")
    return output_path

