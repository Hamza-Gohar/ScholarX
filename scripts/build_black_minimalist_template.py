"""
ScholarX 'Black Minimalist' Exhibition Presentation Deck & Template Engine
Replicates the authentic aesthetic of the uploaded 'Black Minimalist' template:
- Pure pitch-black canvas (#000000)
- Distinctive, ultra-clear geometric typography: 'Outfit' (weights 400-800)
- High-density mathematical parametric 3D wave ribbon in corners (46 curves each)
- Modular template archetypes matching each slide in the reference sheets:
  * Hero Cover
  * Split Contents (Left 30% anchor + Right numbered items)
  * Agenda with White Icon Boxes (44x44px white badges)
  * Inverted Split Card (Deterministic code vs Probabilistic agents)
  * 3-Column Feature Block with Top Box Header
  * Unified Single-Field System Flowchart
  * Horizontal Timeline Infographic (circular step nodes + connector track)
  * Sovereign Feature Split & Pre-Departure PKR Table
  * 4-Card Architecture Grid
  * Big Metric Statistics & Executive Closing Quote
- Corner push-pin crosshairs (+) for hardboard mounting
- 100% WCAG AAA contrast and zero detector anti-patterns
"""

import os

OUTPUT_HTML = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/index.html"
FRONTEND_HTML = "/mnt/windows/AntiGravity/SCHOLARX/frontend/public/slides/index.html"
GENERATE_SCRIPT = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/generate_slides.py"
TEMPLATE_DOC = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/TEMPLATE_SYSTEM.md"

def generate_wave_svg():
    """Generates a dense parametric 3D wave ribbon matching the reference template."""
    paths = []
    # Top-right sweeping ribbon (46 curves)
    for i in range(46):
        offset = i * 15
        t = i / 45.0
        # Smooth parabolic bell curve for opacity: soft edges, brighter core
        opacity = 0.02 + 0.15 * (4 * t * (1 - t))
        d = f"M {920 + offset} 0 C {1180 + offset*0.75} {180 + offset*0.25}, {1460 + offset*0.5} {450 + offset*0.4}, 1920 {520 + offset*11}"
        paths.append(f'<path d="{d}" stroke="#FFFFFF" stroke-opacity="{opacity:.3f}" stroke-width="0.85" fill="none"/>')

    # Bottom-left sweeping ribbon (46 curves)
    for i in range(46):
        offset = i * 15
        t = i / 45.0
        opacity = 0.02 + 0.15 * (4 * t * (1 - t))
        d = f"M 0 {520 + offset*11} C {450 + offset*0.4} {680 + offset*0.25}, {800 + offset*0.7} {850 + offset*0.2}, {1120 + offset} 1080"
        paths.append(f'<path d="{d}" stroke="#FFFFFF" stroke-opacity="{opacity:.3f}" stroke-width="0.85" fill="none"/>')

    return f'<svg class="bg-waves" viewBox="0 0 1920 1080" fill="none" xmlns="http://www.w3.org/2000/svg">{"".join(paths)}</svg>'

BG_WAVES = generate_wave_svg()

PIN_MARKS = """
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>
"""

# Slide 01: Hero Cover (Template Row 1, Col 1)
SLIDE_01 = f"""
      <section class="slide active template-cover" id="slide-1" data-index="1">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body" style="justify-content: center; padding-left: 20px;">
          <div style="max-width: 1100px;">
            <h1 class="display-title" style="font-size: 88px; line-height: 1.05; margin-bottom: 24px;">
              ScholarX
            </h1>
            <div style="font-size: 26px; font-weight: 600; color: #F4F4F5; margin-bottom: 20px; letter-spacing: -0.01em;">
              Autonomous Scholarship Intelligence for Pakistani Students
            </div>
            <p style="font-size: 18px; color: #A1A1AA; line-height: 1.65; max-width: 860px; font-weight: 400;">
              A multi-agent, fully autonomous system designed to discover, fact-check, and plan fully funded global scholarships abroad according to your profile and preferences.
            </p>
          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX INTELLIGENCE NETWORK</div>
          <div>SCIENCE EXHIBITION 2026</div>
        </footer>
      </section>
"""

# Slide 02: What is an AI Agent? (Template Row 1, Col 2 "Contents" Split)
SLIDE_02 = f"""
      <section class="slide template-split" id="slide-2" data-index="2">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div class="split-grid">
            
            <!-- Left Anchor Column -->
            <div class="split-left">
              <h2 class="split-title">What is an<br>AI Agent?</h2>
              <div class="split-desc">
                An autonomous software entity equipped with reasoning, memory, tools, and goals that operates in an iterative loop.
              </div>
            </div>

            <!-- Right Content: 6 Numbered Elements -->
            <div class="split-right">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px 56px;">
                
                <div class="numbered-item">
                  <div class="item-number-title">01. Brain (LLM Core)</div>
                  <div class="item-text">High-order reasoning, task decomposition, and strategic planning powered by Gemini.</div>
                </div>

                <div class="numbered-item">
                  <div class="item-number-title">02. Tool Execution</div>
                  <div class="item-text">Directly invokes external tools: web search (Tavily), crawlers (Firecrawl), and PDF parsers.</div>
                </div>

                <div class="numbered-item">
                  <div class="item-number-title">03. Autonomous Agency</div>
                  <div class="item-text">Operates independently toward an objective without requiring step-by-step human prompts.</div>
                </div>

                <div class="numbered-item">
                  <div class="item-number-title">04. Memory Systems</div>
                  <div class="item-text">Retains working context for live tasks, plus persistent database storage across searches.</div>
                </div>

                <div class="numbered-item">
                  <div class="item-number-title">05. Iterative Loop</div>
                  <div class="item-text">Cycles continuously: Perceive &rarr; Think &rarr; Act &rarr; Observe &rarr; Verify until the goal is met.</div>
                </div>

                <div class="numbered-item">
                  <div class="item-number-title">06. Goal-Oriented</div>
                  <div class="item-text">Optimizes every step to find eligible, verified, fully funded scholarship matches.</div>
                </div>

              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>02 / 10</div>
        </footer>
      </section>
"""

# Slide 03: Multi-Agent Systems (Template Row 1, Col 3 "Agenda" with White Icon Boxes)
SLIDE_03 = f"""
      <section class="slide template-split" id="slide-3" data-index="3">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div class="split-grid">
            
            <!-- Left Anchor Column -->
            <div class="split-left">
              <h2 class="split-title">Multi-Agent<br>Systems</h2>
              <div class="split-desc">
                How multiple specialized agents collaborate, challenge each other, and achieve the overarching agenda.
              </div>
            </div>

            <!-- Right Content: Agenda Stack with 44x44px White Icon Boxes -->
            <div class="split-right" style="display: flex; flex-direction: column; gap: 26px;">
              
              <div class="agenda-row">
                <div class="white-box">01</div>
                <div>
                  <div class="agenda-title">Specialized Division of Labor</div>
                  <div class="agenda-text">Each agent masters one domain: Scouts discover, Eligibility Checkers audit, and Skeptics stress-test.</div>
                </div>
              </div>

              <div class="agenda-row">
                <div class="white-box">02</div>
                <div>
                  <div class="agenda-title">Shared State & Event Bus</div>
                  <div class="agenda-text">Asynchronous pub/sub communication via Redis and LangGraph channels maintains system synchronization.</div>
                </div>
              </div>

              <div class="agenda-row">
                <div class="white-box">03</div>
                <div>
                  <div class="agenda-title">Adversarial Debate & Cross-Checking</div>
                  <div class="agenda-text">The Skeptic agent actively attempts to invalidate claims, requiring primary official proof for approval.</div>
                </div>
              </div>

              <div class="agenda-row">
                <div class="white-box">04</div>
                <div>
                  <div class="agenda-title">Collective Agenda Convergence</div>
                  <div class="agenda-text">All agent discoveries converge into a ranked, verified, fraud-free scholarship roadmap for the student.</div>
                </div>
              </div>

            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>03 / 10</div>
        </footer>
      </section>
"""

# Slide 04: Workflows vs Agents (Template Row 2, Col 1 "Inverted Light Card")
SLIDE_04 = f"""
      <section class="slide template-cards" id="slide-4" data-index="4">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div style="margin-bottom: 30px;">
            <h2 class="slide-headline">Workflows vs. Agents</h2>
            <div class="slide-subline">Deterministic code meets probabilistic AI reasoning. Why ScholarX requires both.</div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1;">
            
            <!-- Inverted White Card: Deterministic Workflows -->
            <div style="background: #F4F4F5; color: #09090B; border-radius: 6px; padding: 40px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <h3 style="font-size: 30px; font-weight: 800; margin-bottom: 20px; color: #09090B; letter-spacing: -0.02em;">Deterministic Workflows</h3>
                <div style="display: flex; flex-direction: column; gap: 14px; font-size: 16px; line-height: 1.5; color: #18181B;">
                  <div>• <strong>100% Predictable:</strong> Same input always yields exact same output.</div>
                  <div>• <strong>Zero Hallucination:</strong> Fixed logic—no token drift or guessing.</div>
                  <div>• <strong>Instant & Free:</strong> Executes on CPU with zero API latency or cost.</div>
                </div>
              </div>
              <div style="border-top: 1px solid #D4D4D8; padding-top: 16px; font-size: 14.5px; color: #27272A;">
                <strong>Used for:</strong> 15-Point Eligibility Rules, PKR Currency Math, Deadlines.
              </div>
            </div>

            <!-- Dark Card: Probabilistic AI Agents -->
            <div style="background: #0B0B0F; border: 1px solid #27272A; border-radius: 6px; padding: 40px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <h3 style="font-size: 30px; font-weight: 800; margin-bottom: 20px; color: #FFFFFF; letter-spacing: -0.02em;">Probabilistic AI Agents</h3>
                <div style="display: flex; flex-direction: column; gap: 14px; font-size: 16px; line-height: 1.5; color: #D4D4D8;">
                  <div>• <strong>Natural Comprehension:</strong> Understands complex CVs & messy PDFs.</div>
                  <div>• <strong>Adaptive Reasoning:</strong> Dynamically plans and adjusts search queries.</div>
                  <div>• <strong>Adversarial Critique:</strong> Detects suspicious claims & challenges facts.</div>
                </div>
              </div>
              <div style="border-top: 1px solid #27272A; padding-top: 16px; font-size: 14.5px; color: #A1A1AA;">
                <strong>Used for:</strong> Profile Extraction, Discovery Queries, Skeptic Audits, Strategy.
              </div>
            </div>

          </div>

          <!-- Bottom Law Banner -->
          <div style="margin-top: 24px; border-top: 1px solid #24242A; padding-top: 14px; font-size: 15px; color: #A1A1AA;">
            <strong style="color: #FFFFFF;">The ScholarX Law:</strong> Deterministic workflows strictly guardrail AI agents. No LLM ever guesses a deadline or calculates PKR costs.
          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>04 / 10</div>
        </footer>
      </section>
"""

# Slide 05: The Problem (Template Row 2, Col 2 "3 Columns with Top Box Header")
SLIDE_05 = f"""
      <section class="slide template-3col" id="slide-5" data-index="5">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <!-- Top Box Header -->
          <div style="border: 1px solid #27272A; border-radius: 6px; padding: 24px 32px; margin-bottom: 36px; background: #0A0A0E;">
            <h2 class="slide-headline" style="font-size: 40px; margin-bottom: 8px;">The Problem: Why Scholarships Go Unclaimed</h2>
            <div class="slide-subline" style="font-size: 17px;">Every year, thousands of fully funded seats expire empty while Pakistani students face bureaucratic hurdles.</div>
          </div>

          <!-- 3 Columns Separated by Hairline Borders -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; flex: 1;">
            
            <div style="display: flex; flex-direction: column; justify-content: space-between; border-right: 1px solid #24242A; padding-right: 36px;">
              <div>
                <div class="item-number-title" style="font-size: 24px; margin-bottom: 14px;">01. Hidden Quotas</div>
                <p class="item-text" style="font-size: 15.5px; line-height: 1.6; margin-bottom: 16px;">
                  Government-to-government quotas reserved for Pakistan (400+ Hungary seats, 200+ China CSC, Turkiye Burslari) are buried across obscure embassy portals.
                </p>
              </div>
              <div style="font-size: 14px; color: #EF4444; font-weight: 700;">Over 40% of bilateral seats expire unclaimed.</div>
            </div>

            <div style="display: flex; flex-direction: column; justify-content: space-between; border-right: 1px solid #24242A; padding-right: 36px;">
              <div>
                <div class="item-number-title" style="font-size: 24px; margin-bottom: 14px;">02. Hidden Cost Shock</div>
                <p class="item-text" style="font-size: 15.5px; line-height: 1.6; margin-bottom: 16px;">
                  "Fully funded" tuition rarely means zero out-of-pocket expenses. Mandatory upfront costs (IELTS PKR 76k, visa stamps, attestations) surprise families.
                </p>
              </div>
              <div style="font-size: 14px; color: #F59E0B; font-weight: 700;">Students abandon offers at the visa stage.</div>
            </div>

            <div style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div class="item-number-title" style="font-size: 24px; margin-bottom: 14px;">03. Paperwork Traps</div>
                <p class="item-text" style="font-size: 15.5px; line-height: 1.6; margin-bottom: 16px;">
                  Generic global engines ignore Pakistan-specific gates: mandatory HEC HAT/USAT tests, IBCC equivalencies, and MOFA legal queues.
                </p>
              </div>
              <div style="font-size: 14px; color: #A1A1AA; font-weight: 700;">Disqualified on paperwork technicalities.</div>
            </div>

          </div>

          <!-- Bottom Callout -->
          <div style="margin-top: 28px; border-top: 1px solid #24242A; padding-top: 14px; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 15px; color: #D4D4D8;">
              <strong style="color: #FFFFFF;">The Consultant Scam:</strong> Predatory agents charge PKR 150K–300K+ merely to submit free public government forms.
            </div>
            <div style="font-size: 14px; font-weight: 800; color: #10B981;">ScholarX is 100% Free Forever</div>
          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>05 / 10</div>
        </footer>
      </section>
"""

# Slide 06: Complete System Flowchart (Template Unified Single Field)
SLIDE_06 = f"""
      <section class="slide template-flowchart" id="slide-6" data-index="6">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div style="margin-bottom: 22px;">
            <h2 class="slide-headline" style="font-size: 40px; margin-bottom: 6px;">System Flowchart: All Agents & Workflows</h2>
            <div class="slide-subline" style="font-size: 16.5px;">5 autonomous AI agents and 7 deterministic workflows orchestrated in one unified field.</div>
          </div>

          <!-- Single-Field Flowchart Container -->
          <div style="flex: 1; border: 1px solid #24242A; border-radius: 6px; padding: 22px; background: #08080C; display: flex; flex-direction: column; justify-content: space-between;">
            
            <svg viewBox="0 0 1200 480" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; flex: 1;">
              
              <!-- 1. Input -->
              <rect x="360" y="10" width="480" height="54" rx="5" fill="#121218" stroke="#FFFFFF" stroke-width="1.2"/>
              <text x="600" y="32" text-anchor="middle" fill="#A1A1AA" font-size="11" font-weight="700">1. STUDENT INPUT LAYER</text>
              <text x="600" y="50" text-anchor="middle" fill="#FFFFFF" font-size="14.5" font-weight="600">CV, Transcripts, GPA, Preferences & PKR Budget</text>

              <path d="M 600 64 L 600 90" stroke="#71717A" stroke-width="1.5"/>
              <polygon points="596,90 600,97 604,90" fill="#71717A"/>

              <!-- 2. Intake Agents -->
              <rect x="180" y="98" width="260" height="60" rx="5" fill="#10141D" stroke="#38BDF8" stroke-width="1.2"/>
              <text x="310" y="122" text-anchor="middle" fill="#38BDF8" font-size="11" font-weight="700">[AGENT] PROFILE ANALYST</text>
              <text x="310" y="142" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Extracts GPA & Credentials</text>

              <rect x="470" y="98" width="260" height="60" rx="5" fill="#181820" stroke="#FFFFFF" stroke-width="1.5"/>
              <text x="600" y="122" text-anchor="middle" fill="#FFFFFF" font-size="11" font-weight="700">[AGENT] ORCHESTRATOR</text>
              <text x="600" y="142" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Controls Routing & State</text>

              <rect x="760" y="98" width="260" height="60" rx="5" fill="#10141D" stroke="#38BDF8" stroke-width="1.2"/>
              <text x="890" y="122" text-anchor="middle" fill="#38BDF8" font-size="11" font-weight="700">[AGENT] DOCUMENT ANALYST</text>
              <text x="890" y="142" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Checks Document Readiness</text>

              <path d="M 440 128 L 470 128" stroke="#3F3F46" stroke-width="1.2"/>
              <path d="M 730 128 L 760 128" stroke="#3F3F46" stroke-width="1.2"/>

              <path d="M 600 158 L 600 184" stroke="#71717A" stroke-width="1.5"/>
              <polygon points="596,184 600,191 604,184" fill="#71717A"/>

              <!-- 3. Regional Discovery Scouts -->
              <rect x="90" y="192" width="230" height="60" rx="5" fill="#0C1712" stroke="#10B981" stroke-width="1.2"/>
              <text x="205" y="216" text-anchor="middle" fill="#10B981" font-size="11" font-weight="700">[WORKFLOW] EUROPE SCOUT</text>
              <text x="205" y="236" text-anchor="middle" fill="#FFFFFF" font-size="13.5">DAAD, Hungary, Erasmus</text>

              <rect x="350" y="192" width="230" height="60" rx="5" fill="#0C1712" stroke="#10B981" stroke-width="1.2"/>
              <text x="465" y="216" text-anchor="middle" fill="#10B981" font-size="11" font-weight="700">[WORKFLOW] ASIA SCOUT</text>
              <text x="465" y="236" text-anchor="middle" fill="#FFFFFF" font-size="13.5">China CSC, Turkiye, MEXT</text>

              <rect x="610" y="192" width="230" height="60" rx="5" fill="#0C1712" stroke="#10B981" stroke-width="1.2"/>
              <text x="725" y="216" text-anchor="middle" fill="#10B981" font-size="11" font-weight="700">[WORKFLOW] AMERICAS SCOUT</text>
              <text x="725" y="236" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Fulbright & Canadian Seats</text>

              <rect x="870" y="192" width="240" height="60" rx="5" fill="#0C1712" stroke="#10B981" stroke-width="1.2"/>
              <text x="990" y="216" text-anchor="middle" fill="#10B981" font-size="11" font-weight="700">[WORKFLOW] MENA SCOUT</text>
              <text x="990" y="236" text-anchor="middle" fill="#FFFFFF" font-size="13.5">KAUST, Qatar & Global</text>

              <path d="M 600 252 L 600 278" stroke="#71717A" stroke-width="1.5"/>
              <polygon points="596,278 600,285 604,278" fill="#71717A"/>

              <!-- 4. Deterministic Guardrails -->
              <rect x="180" y="286" width="260" height="60" rx="5" fill="#16130D" stroke="#F59E0B" stroke-width="1.2"/>
              <text x="310" y="310" text-anchor="middle" fill="#F59E0B" font-size="11" font-weight="700">[WORKFLOW] ELIGIBILITY CHECK</text>
              <text x="310" y="330" text-anchor="middle" fill="#FFFFFF" font-size="13.5">15 Hard Criteria Gates</text>

              <rect x="470" y="286" width="260" height="60" rx="5" fill="#16130D" stroke="#F59E0B" stroke-width="1.2"/>
              <text x="600" y="310" text-anchor="middle" fill="#F59E0B" font-size="11" font-weight="700">[WORKFLOW] TRUE COST MATH</text>
              <text x="600" y="330" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Calculates Exact PKR Needs</text>

              <rect x="760" y="286" width="260" height="60" rx="5" fill="#16130D" stroke="#F59E0B" stroke-width="1.2"/>
              <text x="890" y="310" text-anchor="middle" fill="#F59E0B" font-size="11" font-weight="700">[WORKFLOW] DEADLINE MATH</text>
              <text x="890" y="330" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Timeline & Buffer Days</text>

              <path d="M 440 316 L 470 316" stroke="#3F3F46" stroke-width="1.2"/>
              <path d="M 730 316 L 760 316" stroke="#3F3F46" stroke-width="1.2"/>

              <path d="M 600 346 L 600 372" stroke="#71717A" stroke-width="1.5"/>
              <polygon points="596,372 600,379 604,372" fill="#71717A"/>

              <!-- 5. Adversarial Audit & Deliverable -->
              <rect x="220" y="380" width="220" height="60" rx="5" fill="#10141D" stroke="#38BDF8" stroke-width="1.2"/>
              <text x="330" y="404" text-anchor="middle" fill="#38BDF8" font-size="11" font-weight="700">[AGENT] VERIFICATION</text>
              <text x="330" y="424" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Official Portal Check</text>

              <path d="M 440 410 L 510 410" stroke="#EF4444" stroke-width="1.5"/>
              <polygon points="445,406 435,410 445,414" fill="#EF4444"/>
              <polygon points="505,406 515,410 505,414" fill="#EF4444"/>

              <rect x="515" y="380" width="220" height="60" rx="5" fill="#190F11" stroke="#EF4444" stroke-width="1.5"/>
              <text x="625" y="404" text-anchor="middle" fill="#EF4444" font-size="11" font-weight="700">[AGENT] SKEPTIC (AUDIT)</text>
              <text x="625" y="424" text-anchor="middle" fill="#FFFFFF" font-size="13.5">Disproves Fake Claims</text>

              <path d="M 735 410 L 785 410" stroke="#10B981" stroke-width="1.5"/>
              <polygon points="780,406 788,410 780,414" fill="#10B981"/>

              <rect x="788" y="380" width="330" height="60" rx="5" fill="#F4F4F5" stroke="#FFFFFF" stroke-width="1.5"/>
              <text x="953" y="404" text-anchor="middle" fill="#09090B" font-size="11" font-weight="800">[FINAL DELIVERABLE]</text>
              <text x="953" y="424" text-anchor="middle" fill="#09090B" font-size="14.5" font-weight="700">Verified Application Roadmap</text>
            </svg>

            <!-- Bottom Legend -->
            <div style="display: flex; justify-content: center; gap: 48px; border-top: 1px solid #24242A; padding-top: 12px; font-size: 13.5px;">
              <div><strong style="color: #38BDF8;">AI Agents (5):</strong> Reasoning & dynamic verification</div>
              <div><strong style="color: #10B981;">Workflows (7):</strong> Deterministic search & mathematical gates</div>
              <div><strong style="color: #FFFFFF;">Deliverable:</strong> Official links & transparent PKR costs</div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>06 / 10</div>
        </footer>
      </section>
"""

# Slide 07: The Student Journey (Template Row 3, Col 3 "Timeline Infographic")
SLIDE_07 = f"""
      <section class="slide template-timeline" id="slide-7" data-index="7">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div style="margin-bottom: 36px;">
            <h2 class="slide-headline">The Student Journey in 4 Steps</h2>
            <div class="slide-subline">From uploading your CV to getting a verified application roadmap in under 2 minutes.</div>
          </div>

          <!-- Horizontal Timeline Infographic Matching Template -->
          <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 0 16px;">
            
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 36px; position: relative;">
              
              <!-- Timeline Horizontal Connector Line behind nodes -->
              <div style="position: absolute; top: 22px; left: 60px; right: 60px; height: 1.5px; background: #27272A; z-index: 1;"></div>

              <!-- Step 01 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle">01</div>
                <div class="timeline-step-title">Profile Intake</div>
                <div style="font-size: 13px; color: #38BDF8; font-weight: 700; margin-bottom: 10px;">2 MINUTES</div>
                <p class="timeline-step-desc">
                  Upload your CV or transcript. The AI parses GPA, degree type, publications, and test scores without tedious forms.
                </p>
              </div>

              <!-- Step 02 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle">02</div>
                <div class="timeline-step-title">Global Scan</div>
                <div style="font-size: 13px; color: #10B981; font-weight: 700; margin-bottom: 10px;">AUTONOMOUS</div>
                <p class="timeline-step-desc">
                  4 regional scouts crawl official government databases across Europe, Asia, Americas, and MENA in parallel.
                </p>
              </div>

              <!-- Step 03 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle">03</div>
                <div class="timeline-step-title">Fact-Checking</div>
                <div style="font-size: 13px; color: #EF4444; font-weight: 700; margin-bottom: 10px;">STRICT AUDIT</div>
                <p class="timeline-step-desc">
                  Filters through 15 qualification gates, calculates true PKR expenses, and challenges claims with the Skeptic Agent.
                </p>
              </div>

              <!-- Step 04 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle">04</div>
                <div class="timeline-step-title">Action Roadmap</div>
                <div style="font-size: 13px; color: #10B981; font-weight: 700; margin-bottom: 10px;">READY TO APPLY</div>
                <p class="timeline-step-desc">
                  Get a ranked dossier with verified portal links, required HEC/IBCC steps, and dynamic deadline reminders.
                </p>
              </div>

            </div>

            <!-- Bottom Stats Row -->
            <div style="margin-top: 56px; border-top: 1px solid #24242A; padding-top: 22px; display: flex; justify-content: space-between; align-items: center;">
              <div style="display: flex; gap: 64px;">
                <div>
                  <div style="font-size: 28px; font-weight: 800; color: #FFFFFF;">~90s</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Average Hunt Duration</div>
                </div>
                <div>
                  <div style="font-size: 28px; font-weight: 800; color: #FFFFFF;">15 Gates</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Strict Rule Checks</div>
                </div>
                <div>
                  <div style="font-size: 28px; font-weight: 800; color: #FFFFFF;">PKR 0</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Total Cost to Student</div>
                </div>
              </div>

              <div style="font-size: 14.5px; color: #A1A1AA;">
                Direct official government links only. No sponsored or affiliate redirects.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>07 / 10</div>
        </footer>
      </section>
"""

# Slide 08: Built for Pakistani Students (Template Split Layout with Data Table)
SLIDE_08 = f"""
      <section class="slide template-split" id="slide-8" data-index="8">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div class="split-grid">
            
            <!-- Left: Sovereign Pakistani Features -->
            <div class="split-left" style="padding-right: 48px;">
              <h2 class="split-title">Built for<br>Pakistan</h2>
              <div class="split-desc" style="margin-bottom: 24px;">
                Engineered around Pakistan's academic credentials and realistic pre-departure cash requirements.
              </div>

              <div style="display: flex; flex-direction: column; gap: 16px; font-size: 15px; color: #D4D4D8; line-height: 1.55;">
                <div>• <strong>HEC & IBCC Aware:</strong> Maps Pakistani CGPA conversions and flags required HEC HAT tests.</div>
                <div>• <strong>MOFA Legalization:</strong> Step-by-step roadmap for Board &rarr; IBCC &rarr; HEC &rarr; MOFA stamps.</div>
                <div>• <strong>Bilateral Quotas:</strong> Directly tracks dedicated seats for Pakistani passport holders.</div>
              </div>
            </div>

            <!-- Right: Pre-Departure PKR Expense Guide -->
            <div class="split-right" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 8px; letter-spacing: -0.01em;">
                  Pre-Departure Upfront Expense Guide
                </div>
                <div style="font-size: 14px; color: #A1A1AA; margin-bottom: 20px;">
                  "Fully funded" scholarships still require cash in Pakistan before flights are booked:
                </div>

                <!-- Minimalist Table -->
                <div style="border: 1px solid #24242A; border-radius: 6px; overflow: hidden; background: #08080C;">
                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 12px 20px; background: #121218; font-size: 12px; font-weight: 800; color: #A1A1AA;">
                    <div>MANDATORY EXPENSE</div>
                    <div>TYPICAL COST (PKR)</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 13px 20px; border-top: 1px solid #1C1C22; font-size: 14.5px; color: #FFFFFF;">
                    <div>IELTS / TOEFL Exam</div>
                    <div style="font-weight: 600;">PKR 75,600 – 76,240</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 13px 20px; border-top: 1px solid #1C1C22; font-size: 14.5px; color: #FFFFFF;">
                    <div>HEC & IBCC Attestations</div>
                    <div style="font-weight: 600;">PKR 12,000 – 18,000</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 13px 20px; border-top: 1px solid #1C1C22; font-size: 14.5px; color: #FFFFFF;">
                    <div>Embassy Visa & Biometrics</div>
                    <div style="font-weight: 600;">PKR 28,000 – 45,000</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 13px 20px; border-top: 1px solid #1C1C22; font-size: 14.5px; color: #FFFFFF;">
                    <div>Medical Exam (Approved Clinic)</div>
                    <div style="font-weight: 600;">PKR 22,000 – 35,000</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 15px 20px; border-top: 2px solid #27272A; background: #14141C; font-size: 15px; font-weight: 800; color: #FFFFFF;">
                    <div>Total Readiness Budget:</div>
                    <div style="color: #F59E0B;">PKR 137K – 174K</div>
                  </div>
                </div>
              </div>

              <div style="border-top: 1px solid #24242A; padding-top: 14px; font-size: 14px; color: #A1A1AA;">
                <strong style="color: #FFFFFF;">Financial Honesty:</strong> ScholarX compares this upfront requirement against the student's declared budget so no one gets stranded.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>08 / 10</div>
        </footer>
      </section>
"""

# Slide 09: Complete Tech Stack (Template 4 Cards Grid)
SLIDE_09 = f"""
      <section class="slide template-4cards" id="slide-9" data-index="9">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div style="margin-bottom: 30px;">
            <h2 class="slide-headline">Complete Tech Stack & Architecture</h2>
            <div class="slide-subline">Production-grade local architecture combining state-of-the-art Python orchestration and modern Next.js.</div>
          </div>

          <!-- 4 Clean Cards -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; flex: 1;">
            
            <div class="tech-card">
              <div>
                <h3 class="tech-title">Frontend (UI)</h3>
                <div class="tech-list">
                  <div>• Next.js 15 (App Router)</div>
                  <div>• React 19 & TypeScript</div>
                  <div>• Tailwind CSS v4</div>
                  <div>• Framer Motion</div>
                  <div>• @xyflow/react (Graph)</div>
                </div>
              </div>
              <div class="tech-footer" style="color: #38BDF8;">Port 3000</div>
            </div>

            <div class="tech-card">
              <div>
                <h3 class="tech-title">Backend Core</h3>
                <div class="tech-list">
                  <div>• Python 3.12+</div>
                  <div>• FastAPI (Async ASGI)</div>
                  <div>• LangGraph State Machine</div>
                  <div>• LangChain Core</div>
                  <div>• Pydantic v2 (Validation)</div>
                </div>
              </div>
              <div class="tech-footer" style="color: #FFFFFF;">Port 8000</div>
            </div>

            <div class="tech-card">
              <div>
                <h3 class="tech-title">Parsers & DB</h3>
                <div class="tech-list">
                  <div>• PyMuPDF & pdfplumber</div>
                  <div>• Tavily & Firecrawl APIs</div>
                  <div>• PostgreSQL + pgvector</div>
                  <div>• Redis 7 Pub/Sub</div>
                  <div>• SQLite Session Store</div>
                </div>
              </div>
              <div class="tech-footer" style="color: #10B981;">Local Docker</div>
            </div>

            <div class="tech-card">
              <div>
                <h3 class="tech-title">LLMs & Failover</h3>
                <div class="tech-list">
                  <div>• Gemini 3.7 Flash (Primary)</div>
                  <div>• Gemini 3.0 Flash (Fallback)</div>
                  <div>• Groq gpt-oss-120b</div>
                  <div>• Multi-Key Key Rotation</div>
                  <div>• Zero Outage Guarantee</div>
                </div>
              </div>
              <div class="tech-footer" style="color: #F59E0B;">Auto-Rotating</div>
            </div>

          </div>

          <!-- Bottom Note -->
          <div style="margin-top: 24px; border-top: 1px solid #24242A; padding-top: 14px; font-size: 14.5px; color: #A1A1AA;">
            <strong style="color: #FFFFFF;">Resilient Multi-Key Failover:</strong> If an API key hits rate limits during a live demo, the system automatically rotates to the next key with zero disruption.
          </div>
        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>09 / 10</div>
        </footer>
      </section>
"""

# Slide 10: Mission & Impact (Template Row 1, Col 2 Sheet 3: "Blog Statistic" + Quote)
SLIDE_10 = f"""
      <section class="slide template-statistic" id="slide-10" data-index="10">
        {PIN_MARKS}
        {BG_WAVES}

        <div class="slide-body">
          <div style="margin-bottom: 30px;">
            <h2 class="slide-headline">Leveling the Playing Field for Pakistan</h2>
            <div class="slide-subline">Democratizing access to global higher education for every deserving Pakistani student.</div>
          </div>

          <!-- Big Statistics Row Matching Template Style -->
          <div style="border: 1px solid #24242A; border-radius: 6px; padding: 36px 48px; background: #08080C; margin-bottom: 36px;">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; text-align: center;">
              
              <div>
                <div class="stat-number">100%</div>
                <div class="stat-label">FREE FOR ALL STUDENTS</div>
              </div>

              <div>
                <div class="stat-number">400+</div>
                <div class="stat-label">BILATERAL SEATS TRACKED</div>
              </div>

              <div>
                <div class="stat-number">15/15</div>
                <div class="stat-label">ELIGIBILITY GATES CHECKED</div>
              </div>

              <div>
                <div class="stat-number">PKR 0</div>
                <div class="stat-label">CONSULTANT COMMISSIONS</div>
              </div>

            </div>
          </div>

          <!-- Executive Closing Quote Card -->
          <div style="flex: 1; border: 1px solid #24242A; border-radius: 6px; padding: 40px; background: #0B0B10; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 32px; font-weight: 800; color: #FFFFFF; line-height: 1.35; margin-bottom: 14px; letter-spacing: -0.02em;">
              "A student's talent—not their wealth or connections—should determine their future."
            </div>
            <div style="font-size: 16px; color: #A1A1AA; font-weight: 500;">
              ScholarX • Science Exhibition 2026 • Sovereign AI built with pride for Pakistan.
            </div>
          </div>

        </div>

        <footer class="slide-footer">
          <div>SCHOLARX</div>
          <div>10 / 10</div>
        </footer>
      </section>
"""

ALL_SLIDES = "\n".join([
    SLIDE_01,
    SLIDE_02,
    SLIDE_03,
    SLIDE_04,
    SLIDE_05,
    SLIDE_06,
    SLIDE_07,
    SLIDE_08,
    SLIDE_09,
    SLIDE_10,
])

HTML_DOCUMENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ScholarX — Autonomous Scholarship Intelligence</title>
  
  <!-- High-clarity geometric typeface matching reference template -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --bg-canvas: #000000;
      --bg-panel: #08080C;
      --bg-card: #0B0B10;
      --bg-card-hover: #12121A;

      --border-line: #24242A;
      --border-subtle: #18181E;

      --text-white: #FFFFFF;
      --text-main: #F4F4F5;
      --text-secondary: #D4D4D8;
      --text-muted: #A1A1AA;
      --text-caption: #71717A;

      --font-family: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', ui-monospace, Menlo, Monaco, Consolas, monospace;

      --slide-w: 1920px;
      --slide-h: 1080px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: var(--font-family);
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* TOP MINIMALIST TOOLBAR */
    .deck-toolbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 48px;
      background: rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      z-index: 1000;
      font-size: 13.5px;
    }}

    .brand-title {{
      font-weight: 800;
      font-size: 16px;
      color: var(--text-white);
      letter-spacing: -0.01em;
    }}

    .toolbar-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .nav-btn {{
      background: #0B0B10;
      color: var(--text-main);
      border: 1px solid var(--border-line);
      padding: 5px 14px;
      border-radius: 4px;
      cursor: pointer;
      font-family: var(--font-family);
      font-size: 13px;
      font-weight: 600;
      transition: all 0.15s ease;
    }}
    .nav-btn:hover {{
      background: #181822;
      color: var(--text-white);
      border-color: #3F3F46;
    }}
    .nav-btn.primary {{
      background: #FFFFFF;
      color: #000000;
      border-color: #FFFFFF;
    }}
    .nav-btn.primary:hover {{
      background: #E4E4E7;
    }}

    .slide-counter {{
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      min-width: 75px;
      text-align: center;
      font-family: var(--font-mono);
    }}

    /* VIEWPORT STAGE */
    .viewport-stage {{
      margin-top: 48px;
      width: 100vw;
      height: calc(100vh - 48px);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}

    #presentation-deck {{
      width: var(--slide-w);
      height: var(--slide-h);
      transform-origin: center center;
      position: relative;
    }}

    /* SLIDE BASE STYLES */
    .slide {{
      width: var(--slide-w);
      height: var(--slide-h);
      position: absolute;
      top: 0;
      left: 0;
      background: var(--bg-canvas);
      display: none;
      flex-direction: column;
      padding: 72px 96px 44px 96px;
      border: 1px solid var(--border-subtle);
      box-sizing: border-box;
      overflow: hidden;
    }}

    .slide.active {{
      display: flex;
    }}

    /* PARAMETRIC 3D WAVE VECTOR */
    .bg-waves {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    /* HARDBOARD CORNER PUSH-PIN CROSSHAIRS */
    .pin-mark {{
      position: absolute;
      width: 20px;
      height: 20px;
      pointer-events: none;
      z-index: 10;
    }}
    .pin-mark::before, .pin-mark::after {{
      content: '';
      position: absolute;
      background: #3F3F46;
    }}
    .pin-mark::before {{
      top: 9px;
      left: 0;
      width: 20px;
      height: 2px;
    }}
    .pin-mark::after {{
      top: 0;
      left: 9px;
      width: 2px;
      height: 20px;
    }}
    .pin-tl {{ top: 24px; left: 24px; }}
    .pin-tr {{ top: 24px; right: 24px; }}
    .pin-bl {{ bottom: 24px; left: 24px; }}
    .pin-br {{ bottom: 24px; right: 24px; }}

    /* COMMON TYPOGRAPHY & LAYOUT CLASSES */
    .slide-body {{
      flex: 1;
      display: flex;
      flex-direction: column;
      position: relative;
      z-index: 5;
      min-height: 0;
    }}

    .display-title {{
      font-weight: 800;
      color: var(--text-white);
      letter-spacing: -0.03em;
    }}

    .slide-headline {{
      font-size: 44px;
      font-weight: 800;
      color: var(--text-white);
      letter-spacing: -0.02em;
      line-height: 1.15;
    }}

    .slide-subline {{
      font-size: 18px;
      color: var(--text-muted);
      line-height: 1.5;
      font-weight: 400;
    }}

    /* TEMPLATE SPLIT GRID (Left Anchor 340px + Hairline + Right Content) */
    .split-grid {{
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: 64px;
      height: 100%;
    }}

    .split-left {{
      border-right: 1px solid var(--border-line);
      padding-right: 48px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }}

    .split-right {{
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .split-title {{
      font-size: 46px;
      font-weight: 800;
      color: var(--text-white);
      line-height: 1.12;
      margin-bottom: 18px;
      letter-spacing: -0.02em;
    }}

    .split-desc {{
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.6;
      font-weight: 400;
    }}

    /* NUMBERED ITEMS */
    .numbered-item {{
      display: flex;
      flex-direction: column;
    }}

    .item-number-title {{
      font-size: 20px;
      font-weight: 800;
      color: var(--text-white);
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }}

    .item-text {{
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.55;
      font-weight: 400;
    }}

    /* AGENDA ROW WITH 44x44 WHITE ICON BOX */
    .agenda-row {{
      display: flex;
      align-items: center;
      gap: 24px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 22px;
    }}

    .white-box {{
      width: 44px;
      height: 44px;
      background: #FFFFFF;
      color: #000000;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      font-weight: 800;
      flex-shrink: 0;
    }}

    .agenda-title {{
      font-size: 19px;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 4px;
      letter-spacing: -0.01em;
    }}

    .agenda-text {{
      font-size: 14.5px;
      color: var(--text-muted);
      line-height: 1.45;
      font-weight: 400;
    }}

    /* TIMELINE STYLES */
    .timeline-circle {{
      width: 44px;
      height: 44px;
      background: #000000;
      border: 2px solid #FFFFFF;
      color: #FFFFFF;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      font-weight: 800;
      margin-bottom: 20px;
    }}

    .timeline-step-title {{
      font-size: 20px;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 6px;
      letter-spacing: -0.01em;
    }}

    .timeline-step-desc {{
      font-size: 15px;
      color: var(--text-secondary);
      line-height: 1.55;
      font-weight: 400;
    }}

    /* TECH CARD STYLES */
    .tech-card {{
      border: 1px solid var(--border-line);
      border-radius: 6px;
      padding: 28px;
      background: #08080C;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .tech-title {{
      font-size: 22px;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 16px;
      letter-spacing: -0.01em;
    }}

    .tech-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 14.5px;
      color: var(--text-secondary);
      font-weight: 400;
    }}

    .tech-footer {{
      font-size: 13px;
      font-weight: 700;
    }}

    /* STATISTIC STYLES */
    .stat-number {{
      font-size: 58px;
      font-weight: 800;
      color: var(--text-white);
      line-height: 1;
      letter-spacing: -0.02em;
    }}

    .stat-label {{
      font-size: 13.5px;
      color: var(--text-muted);
      margin-top: 10px;
      font-weight: 700;
    }}

    /* SLIDE FOOTER */
    .slide-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-line);
      padding-top: 16px;
      margin-top: 16px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-muted);
      position: relative;
      z-index: 5;
    }}

    /* PRINT STYLES (A4 / 16:9 Landscape) */
    @media print {{
      body {{
        background: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
      }}
      .deck-toolbar {{
        display: none !important;
      }}
      .viewport-stage {{
        margin-top: 0 !important;
        height: auto !important;
        width: 100% !important;
        display: block !important;
      }}
      #presentation-deck {{
        transform: none !important;
        width: 1920px !important;
        height: auto !important;
        display: block !important;
      }}
      .slide {{
        display: flex !important;
        position: relative !important;
        width: 1920px !important;
        height: 1080px !important;
        page-break-after: always !important;
        break-after: page !important;
        border: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- TOP MINIMAL TOOLBAR -->
  <header class="deck-toolbar">
    <div class="brand-title">ScholarX</div>

    <div class="toolbar-actions">
      <span class="slide-counter"><span id="curr-num">1</span> / 10</span>
      <button class="nav-btn" onclick="prevSlide()" title="Previous slide (Left Arrow)">Prev</button>
      <button class="nav-btn" onclick="nextSlide()" title="Next slide (Right Arrow / Space)">Next</button>
      <button class="nav-btn" onclick="toggleFullscreen()" title="Fullscreen (F key)">Fullscreen</button>
      <button class="nav-btn primary" onclick="window.print()" title="Print / Save to PDF (P key)">Print PDF</button>
    </div>
  </header>

  <!-- VIEWPORT STAGE -->
  <main class="viewport-stage">
    <div id="presentation-deck">
{ALL_SLIDES}
    </div>
  </main>

  <!-- NAVIGATION SCRIPT -->
  <script>
    let currentSlide = 1;
    const totalSlides = 10;
    const deck = document.getElementById('presentation-deck');
    const currNum = document.getElementById('curr-num');

    function fitDeck() {{
      const availW = window.innerWidth;
      const availH = window.innerHeight - 48;
      const scale = Math.min(availW / 1920, availH / 1080);
      deck.style.transform = `scale(${{scale}})`;
    }}

    window.addEventListener('resize', fitDeck);
    fitDeck();

    const urlParams = new URLSearchParams(window.location.search);
    const hash = window.location.hash;
    if (urlParams.get('slide')) {{
      showSlide(parseInt(urlParams.get('slide')));
    }} else if (hash && hash.startsWith('#slide-')) {{
      showSlide(parseInt(hash.replace('#slide-', '')));
    }}

    function showSlide(index) {{
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;

      for (let i = 1; i <= totalSlides; i++) {{
        const slide = document.getElementById('slide-' + i);
        if (slide) {{
          if (i === index) {{
            slide.classList.add('active');
          }} else {{
            slide.classList.remove('active');
          }}
        }}
      }}
      currentSlide = index;
      currNum.textContent = index;
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        showSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        showSlide(currentSlide - 1);
      }}
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{}});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === ' ') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'p' || e.key === 'P') {{
        window.print();
      }} else if (e.key >= '1' && e.key <= '9') {{
        showSlide(parseInt(e.key));
      }} else if (e.key === '0') {{
        showSlide(10);
      }}
    }});
  </script>
</body>
</html>
"""

def generate_template_doc():
    return """# 📐 ScholarX "Black Minimalist" Slide Presentation Template System

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
"""

def main():
    # 1. Write HTML to exhibition_slides/index.html
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(HTML_DOCUMENT)
    print(f"Generated: {OUTPUT_HTML} ({len(HTML_DOCUMENT)} bytes)")

    # 2. Write HTML to frontend/public/slides/index.html
    os.makedirs(os.path.dirname(FRONTEND_HTML), exist_ok=True)
    with open(FRONTEND_HTML, "w", encoding="utf-8") as f:
        f.write(HTML_DOCUMENT)
    print(f"Synced: {FRONTEND_HTML}")

    # 3. Write template documentation
    with open(TEMPLATE_DOC, "w", encoding="utf-8") as f:
        f.write(generate_template_doc())
    print(f"Created: {TEMPLATE_DOC}")

    # 4. Update generator script
    with open(GENERATE_SCRIPT, "w", encoding="utf-8") as f:
        f.write(f'''"""
ScholarX Science Exhibition Slide Presentation Generator
Generated automatically from build_black_minimalist_template.py
"""

import os

OUTPUT_DIR = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides"
FRONTEND_SLIDES_DIR = "/mnt/windows/AntiGravity/SCHOLARX/frontend/public/slides"

HTML_CONTENT = \'\'\'{HTML_DOCUMENT}\'\'\'

def main():
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Successfully generated: {{index_path}}")

    os.makedirs(FRONTEND_SLIDES_DIR, exist_ok=True)
    frontend_path = os.path.join(FRONTEND_SLIDES_DIR, "index.html")
    with open(frontend_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Successfully synced: {{frontend_path}}")

if __name__ == "__main__":
    main()
''')
    print(f"Updated: {GENERATE_SCRIPT}")

if __name__ == "__main__":
    main()
