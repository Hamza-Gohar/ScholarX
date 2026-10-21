# 🛠️ Troubleshooting & Production Runbook

This document details known edge cases, common pitfalls, and resolution strategies when working with the Korean Minimalist Presentation Engine.

---

## 1. Text Overlapping & Header Collision

### Symptom
The slide subtitle or category tag overlaps with the main headline when the title wraps onto two lines.

### Root Cause
Creating separate `add_textbox()` shapes for the category tag, main title, and subtitle using fixed Y coordinates (e.g. `top=0.68"` and `top=1.35"`). When the title exceeds one line, it expands downward and collides with the subtitle box.

### The Solution: Unified Header Text Frame
Always place the category, title, and subtitle as paragraphs within a **single unified text frame**:

```python
# CORRECT: Unified text frame with automated paragraph flow
header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(8.4), Inches(1.35))
tf = header_box.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

# Paragraph 1: Category Tag
p_cat = tf.paragraphs[0]
p_cat.text = category.upper()
p_cat.space_after = Pt(4)

# Paragraph 2: Split Title
p_t = tf.add_paragraph()
# Add dark run + mocha run
p_t.space_after = Pt(4)

# Paragraph 3: Subtitle
p_sub = tf.add_paragraph()
p_sub.text = subtitle
```

PowerPoint will automatically calculate the vertical offset dynamically based on line wrap, guaranteeing zero collisions.

---

## 2. Python-PPTX Slice Indexing Error

### Symptom
```python
AttributeError: 'list' object has no attribute 'rId'
```

### Root Cause
In `python-pptx`, `prs.slides` is a custom `Slides` collection object. Slicing it with `prs.slides[:10]` causes `__getitem__` to pass `slice(0, 10)` directly to internal `_sldIdLst`, returning a `list` instead of an XML element.

### The Solution
Always access slides by explicit integer index (`prs.slides[i]`) or iterate with a standard loop:
```python
# INCORRECT:
for slide in prs.slides[:8]: ...

# CORRECT:
for i, slide in enumerate(prs.slides):
    if i >= 8: break
```

---

## 3. Duplicate Slide Part Name Warning

### Symptom
```python
UserWarning: Duplicate name: 'ppt/slides/slide1.xml'
```

### Root Cause
Calling `prs.slides.add_slide()` repeatedly after attempting to clear slides without updating the package relationship mapping.

### The Solution
Use the **Pruning Strategy** detailed in `docs/engine-architecture.md`:
1. Start with the 84-slide master template.
2. Select the 8 slide indices you wish to use.
3. Remove unselected slide IDs directly from `prs.slides._sldIdLst`.
4. Clear child shapes in-place using `sp.getparent().remove(sp)`.

This creates zero new slide parts and guarantees 100% clean OpenXML output.

---

## 4. LibreOffice Headless Java Warning

### Symptom
```
Warning: failed to launch javaldx - java may not function correctly
```

### Explanation
This is a benign informational warning emitted by LibreOffice when a Java Runtime Environment (JRE) is not configured in the Linux shell. LibreOffice does not require Java for PDF conversions of presentation slides. The command exits with code `0` and generates pristine vector PDFs.

---

## 5. Linux Font Fallbacks

### Symptom
Subtle font rendering differences between macOS/Windows PowerPoint and Linux headless PDF export.

### Resolution
- The master template uses standard **Arial**, which is universally available on all platforms.
- On Linux servers, ensure `ttf-mscorefonts-installer` or `fonts-liberation` is present:
  ```bash
  sudo apt-get install fonts-liberation
  ```
- In the HTML web deck, Google Font `'Plus Jakarta Sans'` is loaded automatically via Google Fonts CDN, with fallback to `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.
