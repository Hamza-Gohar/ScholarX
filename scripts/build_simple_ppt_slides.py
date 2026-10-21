"""
ScholarX Simple PowerPoint-Style Exhibition Slide Deck Generator
- 16:9 widescreen layout (1920x1080)
- Pure pitch-black OLED canvas (#000000)
- Classic PowerPoint styling, fonts, and clean alignment
- High information density, low word count, punchy bullets
- Clear, highly legible vector SVG diagrams
- Corner push-pin crosshairs (+) for hardboard mounting
- Audited with impeccable detect (0 anti-patterns)
"""

import os
import shutil

OUTPUT_HTML = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/index.html"
FRONTEND_HTML = "/mnt/windows/AntiGravity/SCHOLARX/frontend/public/slides/index.html"
GENERATE_SCRIPT = "/mnt/windows/AntiGravity/SCHOLARX/exhibition_slides/generate_slides.py"

SLIDE_01 = """
      <!-- SLIDE 01: INTRODUCTION -->
      <section class="slide active" id="slide-1" data-index="1">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">ScholarX: Autonomous Scholarship Intelligence</h1>
          <p class="slide-subheadline">A multi-agent, fully autonomous system for Pakistani students to find and win fully funded scholarships abroad.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; height: 100%;">
            
            <!-- Left: Plain English Overview -->
            <div class="card-box" style="padding: 32px; justify-content: space-between;">
              <div>
                <h2 style="font-size: 26px; font-weight: 700; color: #FFFFFF; margin-bottom: 18px;">Built for Pakistani Students</h2>
                <p style="font-size: 17px; color: #D1D5DB; line-height: 1.6; margin-bottom: 24px;">
                  Securing international scholarships from Pakistan is broken: portals are scattered, quotas are hidden, and consultants charge hundreds of thousands in fees. ScholarX automates the entire search, audit, and roadmap.
                </p>

                <div style="display: flex; flex-direction: column; gap: 14px; font-size: 16px;">
                  <div style="display: flex; align-items: center; gap: 12px; color: #E5E7EB;">
                    <span style="color: #10B981; font-weight: 800; font-size: 18px;">•</span>
                    <span><strong>100% Free & Open:</strong> Zero agent fees, zero paywalls.</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 12px; color: #E5E7EB;">
                    <span style="color: #38BDF8; font-weight: 800; font-size: 18px;">•</span>
                    <span><strong>6 Continents Scanned:</strong> Europe, Asia, Americas, and MENA.</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 12px; color: #F59E0B; font-weight: 700;">
                    <span style="color: #F59E0B; font-weight: 800; font-size: 18px;">•</span>
                    <span><strong>Pakistan Grounded:</strong> Calibrated for HEC, IBCC, and true PKR costs.</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 12px; color: #E5E7EB;">
                    <span style="color: #10B981; font-weight: 800; font-size: 18px;">•</span>
                    <span><strong>Verified Facts Only:</strong> Multi-source proof with zero hallucinations.</span>
                  </div>
                </div>
              </div>

              <div style="background: #16161D; border: 1px solid #2B2B36; border-radius: 8px; padding: 14px 18px; font-size: 14px; color: #9CA3AF;">
                <strong style="color: #FFFFFF;">Key Coverage:</strong> Hungary Stipendium (400+ seats), China CSC (200+ seats), Turkiye Burslari, DAAD & Global STEM.
              </div>
            </div>

            <!-- Right: Simple 3-Box Flow Diagram -->
            <div class="card-box" style="padding: 28px; justify-content: space-between;">
              <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">How ScholarX Operates</h2>
              
              <svg viewBox="0 0 650 480" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; flex: 1;">
                <!-- Step 1 -->
                <rect x="50" y="20" width="550" height="95" rx="8" fill="#14141B" stroke="#38BDF8" stroke-width="1.5"/>
                <text x="80" y="55" fill="#38BDF8" font-size="14" font-weight="700">1. STUDENT INPUT</text>
                <text x="80" y="85" fill="#FFFFFF" font-size="17" font-weight="600">CV, GPA, Degree Field, Target Countries & Budget</text>

                <!-- Arrow 1 -> 2 -->
                <path d="M 325 115 L 325 155" stroke="#38BDF8" stroke-width="2"/>
                <polygon points="320,155 325,165 330,155" fill="#38BDF8"/>

                <!-- Step 2 -->
                <rect x="50" y="165" width="550" height="135" rx="8" fill="#14141B" stroke="#10B981" stroke-width="1.5"/>
                <text x="80" y="198" fill="#10B981" font-size="14" font-weight="700">2. AUTONOMOUS MULTI-AGENT ENGINE</text>
                <text x="80" y="228" fill="#FFFFFF" font-size="17" font-weight="600">Parallel Global Search across Official Portals</text>
                <text x="80" y="258" fill="#9CA3AF" font-size="14.5">• 15-Point Eligibility Audit • True PKR Cost Math • Skeptic Validation</text>
                <text x="80" y="282" fill="#9CA3AF" font-size="14.5">• Cross-Checks Hungarian, Chinese, and European Government Agreements</text>

                <!-- Arrow 2 -> 3 -->
                <path d="M 325 300 L 325 340" stroke="#10B981" stroke-width="2"/>
                <polygon points="320,340 325,350 330,340" fill="#10B981"/>

                <!-- Step 3 -->
                <rect x="50" y="350" width="550" height="100" rx="8" fill="#0D1E16" stroke="#10B981" stroke-width="2"/>
                <text x="80" y="385" fill="#10B981" font-size="14" font-weight="700">3. STUDENT ROADMAP & DELIVERABLE</text>
                <text x="80" y="415" fill="#FFFFFF" font-size="17" font-weight="700">Ranked Matches + Official Links + Exact PKR Budget Guide</text>
              </svg>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">System Introduction</div>
          <div class="footer-num">Slide 1 of 10</div>
        </footer>
      </section>
"""

SLIDE_02 = """
      <!-- SLIDE 02: WHAT IS AN AI AGENT? -->
      <section class="slide" id="slide-2" data-index="2">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">What is an AI Agent? The 6 Core Elements</h1>
          <p class="slide-subheadline">Unlike passive chatbots that only reply to prompts, an AI agent acts autonomously in an iterative loop to fulfill a goal.</p>
        </header>

        <div class="slide-canvas">
          <!-- 6 Grid Cards (3x2) -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; height: 100%;">
            
            <div class="card-box" style="padding: 26px; justify-content: space-between;">
              <div>
                <span class="badge-tag badge-blue" style="margin-bottom: 12px;">Element 1</span>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">LLM as the Brain</h2>
                <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                  Uses a high-intelligence language model (Gemini 3.7 Flash) for reasoning, decomposing complex tasks, and strategic planning.
                </p>
              </div>
              <div style="font-size: 13.5px; color: #38BDF8; font-weight: 600;">Plans actions & analyzes text</div>
            </div>

            <div class="card-box" style="padding: 26px; justify-content: space-between;">
              <div>
                <span class="badge-tag badge-green" style="margin-bottom: 12px;">Element 2</span>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Tool Access</h2>
                <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                  Equipped with real tools: web search (Tavily), site scrapers (Firecrawl), PDF extractors (PyMuPDF), and local database queries.
                </p>
              </div>
              <div style="font-size: 13.5px; color: #10B981; font-weight: 600;">Interacts with external data</div>
            </div>

            <div class="card-box" style="padding: 26px; justify-content: space-between;">
              <div>
                <span class="badge-tag badge-slate" style="margin-bottom: 12px;">Element 3</span>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Autonomy</h2>
                <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                  Works independently without requiring human guidance at every step. Handles errors, retries failed steps, and adapts.
                </p>
              </div>
              <div style="font-size: 13.5px; color: #94A3B8; font-weight: 600;">Executes multi-step missions</div>
            </div>

            <div class="card-box" style="padding: 26px; justify-content: space-between;">
              <div>
                <span class="badge-tag badge-amber" style="margin-bottom: 12px;">Element 4</span>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Memory Systems</h2>
                <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                  Maintains short-term working context for live tasks, plus long-term database storage (SQLite & vector search) across search sessions.
                </p>
              </div>
              <div style="font-size: 13.5px; color: #F59E0B; font-weight: 600;">Remembers research & profile</div>
            </div>

            <div class="card-box" style="padding: 26px; justify-content: space-between;">
              <div>
                <span class="badge-tag badge-rose" style="margin-bottom: 12px;">Element 5</span>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Iterative Loop</h2>
                <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                  Operates in a continuous cycle: <strong>Perceive &rarr; Think &rarr; Act &rarr; Observe &rarr; Verify</strong> until the objective is reached.
                </p>
              </div>
              <div style="font-size: 13.5px; color: #EF4444; font-weight: 600;">Closed-loop execution</div>
            </div>

            <div class="card-box" style="padding: 26px; justify-content: space-between;">
              <div>
                <span class="badge-tag badge-green" style="margin-bottom: 12px;">Element 6</span>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Goal-Oriented</h2>
                <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                  Optimizes every action toward a clear student outcome: finding eligible, verified, fully funded scholarship matches.
                </p>
              </div>
              <div style="font-size: 13.5px; color: #10B981; font-weight: 600;">Target-driven delivery</div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">AI Agent Fundamentals</div>
          <div class="footer-num">Slide 2 of 10</div>
        </footer>
      </section>
"""

SLIDE_03 = """
      <!-- SLIDE 03: MULTI-AGENT AI -->
      <section class="slide" id="slide-3" data-index="3">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Multi-Agent AI: Collaborative Intelligence</h1>
          <p class="slide-subheadline">Multiple specialized agents collaborate, challenge each other, and achieve complex goals together.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 3 Core Collaboration Principles -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
              <div class="card-box" style="padding: 24px;">
                <div style="font-size: 18px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">1. Division of Labor</div>
                <p style="font-size: 15px; color: #D1D5DB; line-height: 1.5;">
                  Instead of one generic agent doing everything, specialized agents master individual tasks: scouts search, checkers audit, and skeptics test.
                </p>
              </div>

              <div class="card-box" style="padding: 24px;">
                <div style="font-size: 18px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">2. Shared Event Bus</div>
                <p style="font-size: 15px; color: #D1D5DB; line-height: 1.5;">
                  Agents communicate asynchronously using Redis Pub/Sub and LangGraph state. Discovery events instantly trigger verification pipelines.
                </p>
              </div>

              <div class="card-box" style="padding: 24px;">
                <div style="font-size: 18px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">3. Adversarial Fact-Checking</div>
                <p style="font-size: 15px; color: #D1D5DB; line-height: 1.5;">
                  A dedicated Skeptic Agent actively challenges claims. An opportunity is rejected unless primary official proof is produced.
                </p>
              </div>
            </div>

            <!-- Visual Flowchart of Multi-Agent Team -->
            <div class="card-box" style="padding: 24px; flex: 1; justify-content: center;">
              <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px; text-align: center;">
                How Agents Collaborate to Achieve the Goal
              </div>

              <svg viewBox="0 0 1100 240" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto;">
                <!-- Box 1: Scout -->
                <rect x="20" y="40" width="220" height="150" rx="8" fill="#14141B" stroke="#38BDF8" stroke-width="1.5"/>
                <text x="130" y="75" text-anchor="middle" fill="#38BDF8" font-size="14" font-weight="700">REGIONAL SCOUTS</text>
                <text x="130" y="105" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="600">Discovers Opportunities</text>
                <text x="130" y="135" text-anchor="middle" fill="#9CA3AF" font-size="13">Scans government databases</text>
                <text x="130" y="155" text-anchor="middle" fill="#9CA3AF" font-size="13">across 6 continents</text>

                <!-- Arrow 1 -> 2 -->
                <path d="M 240 115 L 300 115" stroke="#38BDF8" stroke-width="2"/>
                <polygon points="295,110 305,115 295,120" fill="#38BDF8"/>

                <!-- Box 2: Checker -->
                <rect x="305" y="40" width="230" height="150" rx="8" fill="#14141B" stroke="#F59E0B" stroke-width="1.5"/>
                <text x="420" y="75" text-anchor="middle" fill="#F59E0B" font-size="14" font-weight="700">ELIGIBILITY CHECKER</text>
                <text x="420" y="105" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="600">15 Strict Rule Checks</text>
                <text x="420" y="135" text-anchor="middle" fill="#9CA3AF" font-size="13">GPA, Pakistani nationality,</text>
                <text x="420" y="155" text-anchor="middle" fill="#9CA3AF" font-size="13">major fit, and age limits</text>

                <!-- Arrow 2 -> 3 -->
                <path d="M 535 115 L 595 115" stroke="#F59E0B" stroke-width="2"/>
                <polygon points="590,110 600,115 590,120" fill="#F59E0B"/>

                <!-- Box 3: Skeptic -->
                <rect x="600" y="40" width="220" height="150" rx="8" fill="#14141B" stroke="#EF4444" stroke-width="1.5"/>
                <text x="710" y="75" text-anchor="middle" fill="#EF4444" font-size="14" font-weight="700">SKEPTIC AGENT</text>
                <text x="710" y="105" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="600">Adversarial Challenge</text>
                <text x="710" y="135" text-anchor="middle" fill="#9CA3AF" font-size="13">Attempts to disprove claims;</text>
                <text x="710" y="155" text-anchor="middle" fill="#9CA3AF" font-size="13">demands primary proof</text>

                <!-- Arrow 3 -> 4 -->
                <path d="M 820 115 L 880 115" stroke="#10B981" stroke-width="2"/>
                <polygon points="875,110 885,115 875,120" fill="#10B981"/>

                <!-- Box 4: Advisor -->
                <rect x="880" y="40" width="200" height="150" rx="8" fill="#0D1E16" stroke="#10B981" stroke-width="2"/>
                <text x="980" y="75" text-anchor="middle" fill="#10B981" font-size="14" font-weight="700">FINAL ADVISOR</text>
                <text x="980" y="105" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700">Action Plan</text>
                <text x="980" y="135" text-anchor="middle" fill="#D1FAE5" font-size="13">Verified matches, real PKR</text>
                <text x="980" y="155" text-anchor="middle" fill="#D1FAE5" font-size="13">costs, and application steps</text>
              </svg>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">Multi-Agent Collaboration</div>
          <div class="footer-num">Slide 3 of 10</div>
        </footer>
      </section>
"""

SLIDE_04 = """
      <!-- SLIDE 04: WORKFLOWS VS AGENTS -->
      <section class="slide" id="slide-4" data-index="4">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Workflows vs. Agents: Why We Need Both</h1>
          <p class="slide-subheadline">Workflows guarantee mathematical certainty. Agents provide cognitive flexibility. ScholarX combines both.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- Side-by-Side Comparison -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px; flex: 1;">
              
              <!-- Left: Deterministic Workflows -->
              <div class="card-box" style="padding: 30px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-green">Deterministic</span>
                    <span style="font-size: 13.5px; color: #10B981; font-weight: 600;">Code & Math</span>
                  </div>
                  <h2 style="font-size: 24px; font-weight: 700; color: #FFFFFF; margin-bottom: 16px;">Deterministic Workflows</h2>

                  <div style="display: flex; flex-direction: column; gap: 14px; font-size: 16px; color: #E5E7EB;">
                    <div>• <strong>100% Predictable:</strong> Same input always yields the exact same output.</div>
                    <div>• <strong>Zero Hallucination:</strong> Fixed code logic—no guessing or drifting.</div>
                    <div>• <strong>Instant & Free:</strong> Executes on CPU in milliseconds with zero API token cost.</div>
                  </div>
                </div>

                <div style="background: #102018; border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 14px 18px; margin-top: 18px;">
                  <span style="font-size: 13px; color: #10B981; font-weight: 700;">Used in ScholarX for:</span>
                  <div style="font-size: 14px; color: #FFFFFF; margin-top: 4px;">
                    15-Point Eligibility Rules • PKR Currency Conversions • Deadline Math • Weighted Scoring
                  </div>
                </div>
              </div>

              <!-- Right: Probabilistic Agents -->
              <div class="card-box" style="padding: 30px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-blue">Probabilistic</span>
                    <span style="font-size: 13.5px; color: #38BDF8; font-weight: 600;">LLM Reasoning</span>
                  </div>
                  <h2 style="font-size: 24px; font-weight: 700; color: #FFFFFF; margin-bottom: 16px;">Probabilistic AI Agents</h2>

                  <div style="display: flex; flex-direction: column; gap: 14px; font-size: 16px; color: #E5E7EB;">
                    <div>• <strong>Natural Comprehension:</strong> Understands complex CVs and messy PDFs.</div>
                    <div>• <strong>Adaptive Reasoning:</strong> Generates smart search queries when blocked.</div>
                    <div>• <strong>Adversarial Critique:</strong> Evaluates nuance and challenges suspicious claims.</div>
                  </div>
                </div>

                <div style="background: #141820; border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 14px 18px; margin-top: 18px;">
                  <span style="font-size: 13px; color: #38BDF8; font-weight: 700;">Used in ScholarX for:</span>
                  <div style="font-size: 14px; color: #FFFFFF; margin-top: 4px;">
                    Student Profile Extraction • Discovery Query Generation • Skeptic Audits • Application Strategy
                  </div>
                </div>
              </div>

            </div>

            <!-- Bottom: The ScholarX Law -->
            <div class="card-box" style="padding: 22px 28px;">
              <div style="font-size: 17px; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">
                The ScholarX Rule: Deterministic Guardrails Constrain AI Agents
              </div>
              <p style="font-size: 15px; color: #D1D5DB; line-height: 1.5;">
                AI agents are powerful but can make mistakes with arithmetic or dates. <strong>ScholarX uses workflows to check every calculation.</strong> No AI ever guesses a deadline or calculates PKR costs.
              </p>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">System Design Philosophy</div>
          <div class="footer-num">Slide 4 of 10</div>
        </footer>
      </section>
"""

SLIDE_05 = """
      <!-- SLIDE 05: THE PROBLEM -->
      <section class="slide" id="slide-5" data-index="5">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">The Problem: Why Scholarships Go Unclaimed</h1>
          <p class="slide-subheadline">Every year, thousands of fully funded seats expire empty while talented Pakistani students face hidden hurdles.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 3 Core Crisis Pillars -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; flex: 1;">
              
              <!-- Problem 1 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-rose" style="margin-bottom: 14px;">40%+ Quotas Expire Empty</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">1. Information is Hidden</h2>
                  <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                    Government bilateral quotas reserved for Pakistan (400+ Hungary Stipendium, 200+ China CSC, Turkiye Burslari) are buried in obscure embassy PDFs.
                  </p>
                </div>
                <div style="background: #1C1215; border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px 16px; font-size: 13.5px; color: #EF4444;">
                  Result: Talented students never know these quotas exist.
                </div>
              </div>

              <!-- Problem 2 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-amber" style="margin-bottom: 14px;">PKR 150K+ Shock</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">2. The Hidden Cost Shock</h2>
                  <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                    "Fully funded" tuition does not mean zero out-of-pocket costs. Upfront fees (IELTS PKR 75k+, embassy visas, attestations) blindsight applicants.
                  </p>
                </div>
                <div style="background: #1C1710; border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 12px 16px; font-size: 13.5px; color: #F59E0B;">
                  Result: Students drop out at the final visa stage due to surprise costs.
                </div>
              </div>

              <!-- Problem 3 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-slate" style="margin-bottom: 14px;">Paperwork Traps</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">3. Bureaucratic Roadblocks</h2>
                  <p style="font-size: 15.5px; color: #D1D5DB; line-height: 1.55;">
                    Generic global portals ignore Pakistani realities: mandatory HEC HAT/USAT tests, IBCC equivalencies, and MOFA attestation queues.
                  </p>
                </div>
                <div style="background: #141720; border: 1px solid rgba(148, 163, 184, 0.3); border-radius: 8px; padding: 12px 16px; font-size: 13.5px; color: #94A3B8;">
                  Result: Disqualified on technicalities before international review.
                </div>
              </div>

            </div>

            <!-- Bottom: The Predatory Reality -->
            <div class="card-box" style="padding: 20px 28px; background: #111116;">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                  <span style="font-size: 16px; font-weight: 700; color: #FFFFFF;">The Consultant Scam:</span>
                  <span style="font-size: 15px; color: #D1D5DB; margin-left: 8px;">Agents charge PKR 150,000–300,000+ just to submit free public forms.</span>
                </div>
                <span class="badge-tag badge-green">ScholarX is 100% Free</span>
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">The Real-World Problem</div>
          <div class="footer-num">Slide 5 of 10</div>
        </footer>
      </section>
"""

SLIDE_06 = """
      <!-- SLIDE 06: UNIFIED SYSTEM FLOWCHART -->
      <section class="slide" id="slide-6" data-index="6">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">ScholarX Flowchart: All Agents & Workflows</h1>
          <p class="slide-subheadline">The entire intelligence system operating in one unified, easy-to-read field.</p>
        </header>

        <div class="slide-canvas">
          <div class="card-box" style="padding: 20px; flex: 1; justify-content: space-between;">
            
            <!-- Clean, High-Legibility Flowchart -->
            <svg viewBox="0 0 1200 520" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; flex: 1;">
              
              <!-- Level 1: Input -->
              <rect x="350" y="10" width="500" height="60" rx="8" fill="#141822" stroke="#38BDF8" stroke-width="1.5"/>
              <text x="600" y="36" text-anchor="middle" fill="#38BDF8" font-size="13" font-weight="700">1. STUDENT INPUT</text>
              <text x="600" y="56" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="600">CV, Transcripts, GPA, Preferences & PKR Budget</text>

              <!-- Connector 1 -> 2 -->
              <path d="M 600 70 L 600 95" stroke="#38BDF8" stroke-width="2"/>
              <polygon points="595,95 600,103 605,95" fill="#38BDF8"/>

              <!-- Level 2: Intake Agents -->
              <g id="flow-intake">
                <rect x="180" y="105" width="260" height="65" rx="8" fill="#14141B" stroke="#38BDF8" stroke-width="1.5"/>
                <text x="310" y="132" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="700">[AGENT] PROFILE ANALYST</text>
                <text x="310" y="153" text-anchor="middle" fill="#FFFFFF" font-size="14">Extracts GPA & Credentials</text>

                <rect x="470" y="105" width="260" height="65" rx="8" fill="#14141B" stroke="#38BDF8" stroke-width="2"/>
                <text x="600" y="132" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="700">[AGENT] ORCHESTRATOR</text>
                <text x="600" y="153" text-anchor="middle" fill="#FFFFFF" font-size="14">Controls Routing & State</text>

                <rect x="760" y="105" width="260" height="65" rx="8" fill="#14141B" stroke="#38BDF8" stroke-width="1.5"/>
                <text x="890" y="132" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="700">[AGENT] DOCUMENT ANALYST</text>
                <text x="890" y="153" text-anchor="middle" fill="#FFFFFF" font-size="14">Checks Document Readiness</text>

                <path d="M 440 137 L 470 137" stroke="#3F3F46" stroke-width="1.5"/>
                <path d="M 730 137 L 760 137" stroke="#3F3F46" stroke-width="1.5"/>
              </g>

              <!-- Connector 2 -> 3 -->
              <path d="M 600 170 L 600 195" stroke="#10B981" stroke-width="2"/>
              <polygon points="595,195 600,203 605,195" fill="#10B981"/>

              <!-- Level 3: Discovery Scouts -->
              <g id="flow-discovery">
                <rect x="80" y="205" width="240" height="65" rx="8" fill="#0E1A14" stroke="#10B981" stroke-width="1.5"/>
                <text x="200" y="232" text-anchor="middle" fill="#10B981" font-size="12" font-weight="700">[WORKFLOW] EUROPE SCOUT</text>
                <text x="200" y="253" text-anchor="middle" fill="#FFFFFF" font-size="14">DAAD, Hungary, Erasmus</text>

                <rect x="350" y="205" width="240" height="65" rx="8" fill="#0E1A14" stroke="#10B981" stroke-width="1.5"/>
                <text x="470" y="232" text-anchor="middle" fill="#10B981" font-size="12" font-weight="700">[WORKFLOW] ASIA SCOUT</text>
                <text x="470" y="253" text-anchor="middle" fill="#FFFFFF" font-size="14">China CSC, Turkiye, MEXT</text>

                <rect x="610" y="205" width="240" height="65" rx="8" fill="#0E1A14" stroke="#10B981" stroke-width="1.5"/>
                <text x="730" y="232" text-anchor="middle" fill="#10B981" font-size="12" font-weight="700">[WORKFLOW] AMERICAS SCOUT</text>
                <text x="730" y="253" text-anchor="middle" fill="#FFFFFF" font-size="14">Fulbright & Canadian Seats</text>

                <rect x="870" y="205" width="250" height="65" rx="8" fill="#0E1A14" stroke="#10B981" stroke-width="1.5"/>
                <text x="995" y="232" text-anchor="middle" fill="#10B981" font-size="12" font-weight="700">[WORKFLOW] MENA SCOUT</text>
                <text x="995" y="253" text-anchor="middle" fill="#FFFFFF" font-size="14">KAUST, Qatar & Global</text>
              </g>

              <!-- Connector 3 -> 4 -->
              <path d="M 600 270 L 600 295" stroke="#F59E0B" stroke-width="2"/>
              <polygon points="595,295 600,303 605,295" fill="#F59E0B"/>

              <!-- Level 4: Deterministic Guardrails -->
              <g id="flow-guardrails">
                <rect x="180" y="305" width="260" height="65" rx="8" fill="#16130C" stroke="#F59E0B" stroke-width="1.5"/>
                <text x="310" y="332" text-anchor="middle" fill="#F59E0B" font-size="12" font-weight="700">[WORKFLOW] ELIGIBILITY CHECK</text>
                <text x="310" y="353" text-anchor="middle" fill="#FFFFFF" font-size="14">15 Hard Criteria Gates</text>

                <rect x="470" y="305" width="260" height="65" rx="8" fill="#16130C" stroke="#F59E0B" stroke-width="1.5"/>
                <text x="600" y="332" text-anchor="middle" fill="#F59E0B" font-size="12" font-weight="700">[WORKFLOW] TRUE COST MATH</text>
                <text x="600" y="353" text-anchor="middle" fill="#FFFFFF" font-size="14">Calculates Exact PKR Needs</text>

                <rect x="760" y="305" width="260" height="65" rx="8" fill="#16130C" stroke="#F59E0B" stroke-width="1.5"/>
                <text x="890" y="332" text-anchor="middle" fill="#F59E0B" font-size="12" font-weight="700">[WORKFLOW] DEADLINE MATH</text>
                <text x="890" y="353" text-anchor="middle" fill="#FFFFFF" font-size="14">Timeline & Buffer Days</text>

                <path d="M 440 337 L 470 337" stroke="#3F3F46" stroke-width="1.5"/>
                <path d="M 730 337 L 760 337" stroke="#3F3F46" stroke-width="1.5"/>
              </g>

              <!-- Connector 4 -> 5 -->
              <path d="M 600 370 L 600 395" stroke="#EF4444" stroke-width="2"/>
              <polygon points="595,395 600,403 605,395" fill="#EF4444"/>

              <!-- Level 5: Adversarial Audit & Final Delivery -->
              <g id="flow-audit">
                <rect x="220" y="405" width="220" height="65" rx="8" fill="#141822" stroke="#38BDF8" stroke-width="1.5"/>
                <text x="330" y="432" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="700">[AGENT] VERIFICATION</text>
                <text x="330" y="453" text-anchor="middle" fill="#FFFFFF" font-size="14">Official Portal Check</text>

                <!-- Double Sided Arrow: Debate -->
                <path d="M 440 437 L 510 437" stroke="#EF4444" stroke-width="2"/>
                <polygon points="445,432 435,437 445,442" fill="#EF4444"/>
                <polygon points="505,432 515,437 505,442" fill="#EF4444"/>

                <rect x="515" y="405" width="220" height="65" rx="8" fill="#1C1012" stroke="#EF4444" stroke-width="2"/>
                <text x="625" y="432" text-anchor="middle" fill="#EF4444" font-size="12" font-weight="700">[AGENT] SKEPTIC (AUDIT)</text>
                <text x="625" y="453" text-anchor="middle" fill="#FFFFFF" font-size="14">Disproves Fake Claims</text>

                <!-- Arrow Skeptic -> Deliverable -->
                <path d="M 735 437 L 780 437" stroke="#10B981" stroke-width="2"/>
                <polygon points="775,432 785,437 775,442" fill="#10B981"/>

                <rect x="785" y="405" width="330" height="65" rx="8" fill="#0D1E16" stroke="#10B981" stroke-width="2"/>
                <text x="950" y="432" text-anchor="middle" fill="#10B981" font-size="12" font-weight="700">[FINAL DELIVERABLE]</text>
                <text x="950" y="453" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">Verified Application Roadmap</text>
              </g>

            </svg>

            <!-- Legend -->
            <div style="display: flex; align-items: center; justify-content: center; gap: 40px; border-top: 1px solid #27272A; padding-top: 10px; font-size: 13.5px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(56,189,248,0.2); border: 1.5px solid #38BDF8;"></span>
                <span style="color: #FFFFFF; font-weight: 600;">AI Agents (5):</span>
                <span style="color: #9CA3AF;">LLM-powered reasoning & verification</span>
              </div>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(16,185,129,0.2); border: 1.5px solid #10B981;"></span>
                <span style="color: #FFFFFF; font-weight: 600;">Workflows (7):</span>
                <span style="color: #9CA3AF;">Deterministic code & 100% accurate math</span>
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">Full System Flowchart</div>
          <div class="footer-num">Slide 6 of 10</div>
        </footer>
      </section>
"""

SLIDE_07 = """
      <!-- SLIDE 07: THE STUDENT JOURNEY -->
      <section class="slide" id="slide-7" data-index="7">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">The Student Journey in 4 Simple Steps</h1>
          <p class="slide-subheadline">From uploading your CV to getting a verified application roadmap in under 2 minutes.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 4 Linear Step Cards -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
              
              <!-- Step 1 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-blue" style="margin-bottom: 14px;">Step 1: 2 Mins</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Profile Intake</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Upload your CV or transcript. The AI parses GPA, degree type, publications, and test scores without filling long forms.
                  </p>
                </div>
                <div style="background: #141820; border: 1px solid #2B2B36; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #38BDF8;">
                  Fast extraction from PDF
                </div>
              </div>

              <!-- Step 2 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-green" style="margin-bottom: 14px;">Step 2: Auto</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Global Scan</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    4 regional scouts crawl official government databases across Europe, Asia, Americas, and MENA in parallel.
                  </p>
                </div>
                <div style="background: #0E1A14; border: 1px solid #2B2B36; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #10B981;">
                  Scans Hungary, China, DAAD, etc.
                </div>
              </div>

              <!-- Step 3 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-rose" style="margin-bottom: 14px;">Step 3: Strict</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Fact-Checking</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Checks 15 qualification rules, calculates true PKR pre-departure expenses, and challenges claims with the Skeptic Agent.
                  </p>
                </div>
                <div style="background: #1A1012; border: 1px solid #2B2B36; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #EF4444;">
                  Zero false hopes & zero fraud
                </div>
              </div>

              <!-- Step 4 -->
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-green" style="margin-bottom: 14px;">Step 4: Action</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Action Roadmap</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Receive a ranked list of matched scholarships with official application links, document checklists, and deadlines.
                  </p>
                </div>
                <div style="background: #0E1A14; border: 1px solid #2B2B36; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #10B981;">
                  Ready to apply directly
                </div>
              </div>

            </div>

            <!-- Bottom Stats -->
            <div class="card-box" style="padding: 18px 30px; display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
              <div style="display: flex; gap: 48px;">
                <div>
                  <div style="font-size: 24px; font-weight: 700; color: #10B981;">~90 Seconds</div>
                  <div style="font-size: 13px; color: #9CA3AF;">Total Hunt Time</div>
                </div>
                <div>
                  <div style="font-size: 24px; font-weight: 700; color: #FFFFFF;">15 Gates</div>
                  <div style="font-size: 13px; color: #9CA3AF;">Eligibility Checked</div>
                </div>
                <div>
                  <div style="font-size: 24px; font-weight: 700; color: #38BDF8;">PKR 0</div>
                  <div style="font-size: 13px; color: #9CA3AF;">Cost to Student</div>
                </div>
              </div>

              <div style="font-size: 14px; color: #D1D5DB;">
                Direct links to official portals only. No affiliate redirections.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">The Student Journey</div>
          <div class="footer-num">Slide 7 of 10</div>
        </footer>
      </section>
"""

SLIDE_08 = """
      <!-- SLIDE 08: BUILT FOR PAKISTANI STUDENTS -->
      <section class="slide" id="slide-8" data-index="8">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Built for Pakistani Students</h1>
          <p class="slide-subheadline">Engineered around Pakistan's educational standards and realistic pre-departure expenses.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; height: 100%;">
            
            <!-- Left: Pakistani Bureaucracy Features -->
            <div style="display: flex; flex-direction: column; gap: 20px;">
              <div class="card-box" style="padding: 24px; flex: 1;">
                <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">HEC HAT & IBCC Awareness</h2>
                <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                  Understands Pakistani CGPAs (4.0 & 5.0 scales) and percentage conversions. Automatically flags required HEC Higher Education Aptitude Tests (HAT-I through IV) and IBCC equivalencies.
                </p>
              </div>

              <div class="card-box" style="padding: 24px; flex: 1;">
                <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Attestation Roadmap</h2>
                <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                  Foreign embassies require strict verification. ScholarX maps out the sequence: Board attestation &rarr; IBCC equivalence &rarr; HEC verification &rarr; MOFA legal stamp.
                </p>
              </div>

              <div class="card-box" style="padding: 24px; flex: 1;">
                <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Bilateral Quota Discovery</h2>
                <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                  Directly monitors government-to-government scholarship quotas reserved exclusively for Pakistani passport holders (Hungary 400+, China 200+, Turkiye, Romania).
                </p>
              </div>
            </div>

            <!-- Right: Pre-Departure PKR Calculator -->
            <div class="card-box" style="padding: 28px; justify-content: space-between;">
              <div>
                <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Pre-Departure Upfront Expense Guide</h2>
                <p style="font-size: 14.5px; color: #9CA3AF; line-height: 1.5; margin-bottom: 18px;">
                  Even a 100% "fully funded" scholarship requires upfront cash in Pakistan before flights are booked. ScholarX itemizes this in advance:
                </p>

                <!-- Cost Table -->
                <div style="background: #121218; border: 1px solid #2B2B36; border-radius: 8px; overflow: hidden; margin-bottom: 18px;">
                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 10px 16px; background: #181822; font-size: 12.5px; font-weight: 700; color: #9CA3AF;">
                    <div>Mandatory Expense</div>
                    <div>Typical Cost (PKR)</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 12px 16px; border-top: 1px solid #22222B; font-size: 14px; color: #E5E7EB;">
                    <div>IELTS / TOEFL Exam</div>
                    <div style="font-weight: 600; color: #FFFFFF;">PKR 75,600 – 76,240</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 12px 16px; border-top: 1px solid #22222B; font-size: 14px; color: #E5E7EB;">
                    <div>HEC & IBCC Attestations</div>
                    <div style="font-weight: 600; color: #FFFFFF;">PKR 12,000 – 18,000</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 12px 16px; border-top: 1px solid #22222B; font-size: 14px; color: #E5E7EB;">
                    <div>Embassy Visa & Biometrics</div>
                    <div style="font-weight: 600; color: #FFFFFF;">PKR 28,000 – 45,000</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 12px 16px; border-top: 1px solid #22222B; font-size: 14px; color: #E5E7EB;">
                    <div>Medical Exam (Approved Clinic)</div>
                    <div style="font-weight: 600; color: #FFFFFF;">PKR 22,000 – 35,000</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 14px 16px; border-top: 2px solid #3F3F46; background: #161622; font-size: 14.5px; font-weight: 700; color: #FFFFFF;">
                    <div>Total Readiness Budget:</div>
                    <div style="color: #F59E0B; font-size: 15px;">PKR 137K – 174K</div>
                  </div>
                </div>
              </div>

              <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px; padding: 12px 16px; font-size: 13.5px; color: #D1D5DB;">
                <strong style="color: #F59E0B;">Financial Honesty:</strong> ScholarX checks if this matches your declared budget so you never hit a financial dead-end.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">Pakistani Realities</div>
          <div class="footer-num">Slide 8 of 10</div>
        </footer>
      </section>
"""

SLIDE_09 = """
      <!-- SLIDE 09: COMPLETE TECH STACK -->
      <section class="slide" id="slide-9" data-index="9">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Complete Tech Stack & Architecture</h1>
          <p class="slide-subheadline">Production-grade local architecture combining state-of-the-art Python orchestration and modern Next.js.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 4 Architecture Cards -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
              
              <!-- Card 1: Frontend -->
              <div class="card-box" style="padding: 24px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-blue" style="margin-bottom: 12px;">UI Layer</span>
                  <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Frontend</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 14.5px; color: #D1D5DB;">
                    <div>• <strong>Next.js 15</strong> (App Router)</div>
                    <div>• <strong>React 19</strong></div>
                    <div>• <strong>TypeScript 5.7</strong></div>
                    <div>• <strong>Tailwind CSS v4</strong></div>
                    <div>• <strong>Framer Motion</strong></div>
                    <div>• <strong>@xyflow/react</strong> (Graph)</div>
                  </div>
                </div>
                <div style="font-size: 13px; color: #38BDF8; font-weight: 600;">Runs on localhost:3000</div>
              </div>

              <!-- Card 2: Backend -->
              <div class="card-box" style="padding: 24px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-slate" style="margin-bottom: 12px;">Engine</span>
                  <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Backend Core</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 14.5px; color: #D1D5DB;">
                    <div>• <strong>Python 3.12+</strong></div>
                    <div>• <strong>FastAPI</strong> (Async API)</div>
                    <div>• <strong>LangGraph</strong> (State Machine)</div>
                    <div>• <strong>LangChain Core</strong></div>
                    <div>• <strong>Pydantic v2</strong> (Validation)</div>
                    <div>• <strong>Uvicorn ASGI Server</strong></div>
                  </div>
                </div>
                <div style="font-size: 13px; color: #94A3B8; font-weight: 600;">Runs on localhost:8000</div>
              </div>

              <!-- Card 3: Parsers & Data -->
              <div class="card-box" style="padding: 24px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-green" style="margin-bottom: 12px;">Data & Search</span>
                  <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Parsers & DB</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 14.5px; color: #D1D5DB;">
                    <div>• <strong>PyMuPDF & pdfplumber</strong></div>
                    <div>• <strong>Tavily Search API</strong></div>
                    <div>• <strong>Firecrawl API</strong></div>
                    <div>• <strong>PostgreSQL + pgvector</strong></div>
                    <div>• <strong>Redis 7</strong> (Pub/Sub)</div>
                    <div>• <strong>SQLite</strong> (Local Sessions)</div>
                  </div>
                </div>
                <div style="font-size: 13px; color: #10B981; font-weight: 600;">Local data storage</div>
              </div>

              <!-- Card 4: AI & Failover -->
              <div class="card-box" style="padding: 24px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-amber" style="margin-bottom: 12px;">Inference</span>
                  <h2 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">LLMs & Failover</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 14.5px; color: #D1D5DB;">
                    <div>• <strong>Gemini 3.7 Flash</strong> (Main)</div>
                    <div>• <strong>Gemini 3.0 Flash</strong> (Safe)</div>
                    <div>• <strong>Groq gpt-oss-120b</strong></div>
                    <div>• <strong>Automatic Key Rotation:</strong></div>
                    <div style="padding-left: 12px; font-size: 13px; color: #9CA3AF;">3 Gemini • 4 Groq • 5 Tavily</div>
                    <div>• <strong>Zero Token Outage</strong></div>
                  </div>
                </div>
                <div style="font-size: 13px; color: #F59E0B; font-weight: 600;">Multi-key resiliency</div>
              </div>

            </div>

            <!-- Bottom Note -->
            <div class="card-box" style="padding: 18px 28px; background: #111116;">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="font-size: 15px; color: #E5E7EB;">
                  <strong>Multi-Key Failover:</strong> If an API key hits rate limits during a live demo, the system automatically rotates to the next key with zero downtime.
                </div>
                <span class="badge-tag badge-green">Production Ready</span>
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">Engineering Stack</div>
          <div class="footer-num">Slide 9 of 10</div>
        </footer>
      </section>
"""

SLIDE_10 = """
      <!-- SLIDE 10: MISSION & IMPACT -->
      <section class="slide" id="slide-10" data-index="10">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Leveling the Playing Field for Pakistan</h1>
          <p class="slide-subheadline">Democratizing access to global higher education for every deserving Pakistani student.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 4 Impact Cards -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
              
              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-green" style="margin-bottom: 14px;">100% Free Forever</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Zero Agent Fees</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Eliminates exploitative educational middlemen who charge PKR 200,000+ for public information.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #10B981; font-weight: 600;">Democratic Access</div>
              </div>

              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-slate" style="margin-bottom: 14px;">Local & Private</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Data Sovereignty</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Runs locally on student hardware. Academic transcripts, CNICs, and records remain completely private.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #94A3B8; font-weight: 600;">Zero Data Leakage</div>
              </div>

              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-blue" style="margin-bottom: 14px;">National Reach</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Every Province</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Reaching talent across Gilgit-Baltistan, Balochistan, KPK, Sindh, and Punjab equally.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #38BDF8; font-weight: 600;">Equal Opportunity</div>
              </div>

              <div class="card-box" style="padding: 28px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-rose" style="margin-bottom: 14px;">Zero Hallucinations</span>
                  <h2 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Verified Truth</h2>
                  <p style="font-size: 15px; color: #D1D5DB; line-height: 1.55;">
                    Adversarial checks ensure students never waste non-refundable test fees on expired or fake scholarships.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #EF4444; font-weight: 600;">Evidence-Backed</div>
              </div>

            </div>

            <!-- Closing Statement -->
            <div class="card-box" style="padding: 26px 36px; background: #0E0E14; display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
              <div>
                <div style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">
                  "A student's talent—not their wealth or connections—should determine their future."
                </div>
                <div style="font-size: 15px; color: #9CA3AF;">
                  ScholarX • Science Exhibition 2026 • Built with pride for Pakistani students.
                </div>
              </div>

              <span class="badge-tag badge-green" style="font-size: 13px; padding: 6px 14px;">Open Source</span>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-brand">ScholarX</div>
          <div class="footer-topic">Our Mission</div>
          <div class="footer-num">Slide 10 of 10</div>
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
  <style>
    :root {{
      --bg-canvas: #000000;
      --bg-panel: #0D0D11;
      --bg-card: #131318;
      
      --border-strong: #27272A;
      --border-subtle: #1E1E22;

      --text-white: #FFFFFF;
      --text-main: #F3F4F6;
      --text-muted: #9CA3AF;

      --accent-green: #10B981;
      --accent-blue: #38BDF8;
      --accent-slate: #94A3B8;
      --accent-amber: #F59E0B;
      --accent-rose: #EF4444;

      --font-family: 'Segoe UI', Calibri, Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
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
    }}

    /* TOP TOOLBAR */
    .deck-toolbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 52px;
      background: rgba(5, 5, 8, 0.95);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 36px;
      z-index: 1000;
      font-size: 14px;
    }}

    .brand-title {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 15px;
      color: var(--text-white);
    }}
    .brand-dot {{
      width: 8px;
      height: 8px;
      background: var(--accent-green);
      border-radius: 50%;
    }}

    .toolbar-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .nav-btn {{
      background: #14141B;
      color: var(--text-main);
      border: 1px solid var(--border-strong);
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-family: var(--font-family);
      font-size: 13px;
      font-weight: 600;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .nav-btn:hover {{
      background: #202028;
      color: var(--text-white);
      border-color: #3F3F46;
    }}
    .nav-btn.primary {{
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.4);
      color: var(--accent-green);
    }}
    .nav-btn.primary:hover {{
      background: var(--accent-green);
      color: #000000;
    }}

    .slide-counter {{
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      min-width: 85px;
      text-align: center;
    }}
    .counter-highlight {{
      color: var(--text-white);
      font-weight: 700;
    }}

    /* VIEWPORT STAGE */
    .viewport-stage {{
      margin-top: 52px;
      width: 100vw;
      height: calc(100vh - 52px);
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
      padding: 64px 88px 48px 88px;
      border: 1px solid var(--border-subtle);
      box-sizing: border-box;
      overflow: hidden;
    }}

    .slide.active {{
      display: flex;
    }}

    /* CORNER PUSH-PIN CROSSHAIRS FOR HARDBOARD MOUNTING */
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

    /* POWERPOINT HEADER */
    .slide-header {{
      margin-bottom: 28px;
      position: relative;
      z-index: 5;
    }}

    .slide-headline {{
      font-size: 46px;
      font-weight: 700;
      color: var(--text-white);
      line-height: 1.15;
      margin-bottom: 10px;
    }}

    .slide-subheadline {{
      font-size: 20px;
      font-weight: 400;
      color: var(--text-muted);
      line-height: 1.45;
      max-width: 1400px;
    }}

    /* SLIDE CANVAS */
    .slide-canvas {{
      flex: 1;
      display: flex;
      flex-direction: column;
      position: relative;
      z-index: 5;
      min-height: 0;
    }}

    /* POWERPOINT FOOTER */
    .slide-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      padding-top: 16px;
      margin-top: 20px;
      font-size: 14px;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .footer-brand {{
      color: var(--text-white);
      font-weight: 700;
    }}
    .footer-num {{
      font-family: var(--font-family);
      font-weight: 600;
      color: var(--text-white);
    }}

    /* POWERPOINT CARD STYLES */
    .card-box {{
      background: var(--bg-panel);
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      padding: 24px;
      display: flex;
      flex-direction: column;
    }}

    /* BADGES */
    .badge-tag {{
      font-family: var(--font-family);
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      width: fit-content;
    }}
    .badge-green {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    .badge-slate {{
      background: rgba(148, 163, 184, 0.15);
      color: var(--accent-slate);
      border: 1px solid rgba(148, 163, 184, 0.3);
    }}
    .badge-blue {{
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-blue);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}
    .badge-amber {{
      background: rgba(245, 158, 11, 0.15);
      color: var(--accent-amber);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .badge-rose {{
      background: rgba(239, 68, 68, 0.15);
      color: var(--accent-rose);
      border: 1px solid rgba(239, 68, 68, 0.3);
    }}

    /* PRINT STYLES */
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

  <!-- TOP TOOLBAR -->
  <header class="deck-toolbar">
    <div class="brand-title">
      <div class="brand-dot"></div>
      <span>ScholarX — Autonomous Scholarship Intelligence</span>
    </div>

    <div class="toolbar-actions">
      <span class="slide-counter"><span class="counter-highlight" id="curr-num">1</span> of 10</span>
      <button class="nav-btn" onclick="prevSlide()" title="Previous slide (Left Arrow)">Previous</button>
      <button class="nav-btn" onclick="nextSlide()" title="Next slide (Right Arrow / Space)">Next</button>
      <button class="nav-btn" onclick="toggleFullscreen()" title="Fullscreen (F key)">Fullscreen</button>
      <button class="nav-btn primary" onclick="window.print()" title="Print / Save to PDF (P key)">Print Slides (PDF)</button>
    </div>
  </header>

  <!-- VIEWPORT STAGE -->
  <main class="viewport-stage">
    <div id="presentation-deck">
{ALL_SLIDES}
    </div>
  </main>

  <!-- PRESENTATION SCRIPT -->
  <script>
    let currentSlide = 1;
    const totalSlides = 10;
    const deck = document.getElementById('presentation-deck');
    const currNum = document.getElementById('curr-num');

    function fitDeck() {{
      const availW = window.innerWidth;
      const availH = window.innerHeight - 52;
      const scale = Math.min(availW / 1920, availH / 1080);
      deck.style.transform = `scale(${{scale}})`;
    }}

    window.addEventListener('resize', fitDeck);
    fitDeck();

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

def main():
    # Write to exhibition_slides/index.html
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(HTML_DOCUMENT)
    print(f"Generated {OUTPUT_HTML} (size: {len(HTML_DOCUMENT)} bytes)")

    # Ensure destination directory for frontend exists
    os.makedirs(os.path.dirname(FRONTEND_HTML), exist_ok=True)
    with open(FRONTEND_HTML, "w", encoding="utf-8") as f:
        f.write(HTML_DOCUMENT)
    print(f"Copied to {FRONTEND_HTML}")

    # Update generator script
    with open(GENERATE_SCRIPT, "w", encoding="utf-8") as f:
        f.write(f'''"""
ScholarX Science Exhibition Slide Presentation Generator
Generated automatically from build_simple_ppt_slides.py
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
    print(f"Updated {GENERATE_SCRIPT}")

if __name__ == "__main__":
    main()
