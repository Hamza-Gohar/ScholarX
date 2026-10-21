"""
Module containing the HTML generation for all 10 slides.
Strict Impeccable Design:
- Pure pitch-black OLED canvas (#000000)
- Zero AI-slop colors (no purple/violet)
- Clean, editorial palette: Emerald (#10B981), Amber (#F59E0B), Blue (#38BDF8), Rose (#EF4444), Slate (#94A3B8)
- No thick top borders on rounded cards
- No all-caps body text
- High contrast (> 7:1) for all secondary text (#A1A1AA)
"""

def get_slide_01():
    """Slide 01: ScholarX Introduction"""
    return """
      <!-- SLIDE 01: SCHOLARX INTRODUCTION -->
      <section class="slide active" id="slide-1" data-index="1">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">ScholarX: Autonomous Scholarship Intelligence</h1>
          <p class="slide-subheadline">A multi-agent, fully autonomous system designed for Pakistani students to find fully funded scholarships abroad according to profile and preferences very easily.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: grid; grid-template-columns: 1fr 1.05fr; gap: 32px; height: 100%;">
            
            <!-- Left Column: Core Value & Pillars -->
            <div style="display: flex; flex-direction: column; gap: 18px;">
              <div class="card-box" style="flex: 1; padding: 26px; justify-content: center; background: #0C0C0E;">
                <div class="badge-tag badge-green" style="margin-bottom: 12px;">Sovereign Local-First Architecture</div>
                <h2 style="font-size: 24px; font-weight: 800; color: #FFFFFF; line-height: 1.3; margin-bottom: 14px;">Bridging Pakistani Ambition to Global Opportunities</h2>
                <p style="font-size: 15.5px; color: #D4D4D8; line-height: 1.6; margin-bottom: 16px;">
                  Securing international higher education from Pakistan is plagued by obscure portals, missed bilateral quotas, and predatory consultants charging hundreds of thousands in fees. ScholarX replaces manual hunting with an autonomous multi-agent intelligence network running locally on your hardware.
                </p>
                <div style="font-size: 14px; color: #A1A1AA; line-height: 1.5; border-left: 2px solid var(--accent-green); padding-left: 14px;">
                  Investigates, verifies, ranks, and plans actionable application paths specifically calibrated for Pakistani academic backgrounds, test scores, and true PKR budgets.
                </div>
              </div>

              <!-- 4 Feature Cards Grid -->
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div class="card-box" style="padding: 16px;">
                  <span class="badge-tag badge-green" style="margin-bottom: 8px;">Zero Cost</span>
                  <div style="font-size: 15.5px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">100% Free & Open</div>
                  <div style="font-size: 13px; color: #A1A1AA; line-height: 1.45;">No hidden fees or consultant retainers. Sovereign AI for all students.</div>
                </div>

                <div class="card-box" style="padding: 16px;">
                  <span class="badge-tag badge-blue" style="margin-bottom: 8px;">Autonomous</span>
                  <div style="font-size: 15.5px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">6 Continents Scanned</div>
                  <div style="font-size: 13px; color: #A1A1AA; line-height: 1.45;">Continuous sweep across European, Asian, and American portals.</div>
                </div>

                <div class="card-box" style="padding: 16px;">
                  <span class="badge-tag badge-rose" style="margin-bottom: 8px;">Adversarial</span>
                  <div style="font-size: 15.5px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">15-Point Strict Audit</div>
                  <div style="font-size: 13px; color: #A1A1AA; line-height: 1.45;">Multi-source validation with skeptic challenges. Zero hallucinations.</div>
                </div>

                <div class="card-box" style="padding: 16px;">
                  <span class="badge-tag badge-amber" style="margin-bottom: 8px;">PKR Realities</span>
                  <div style="font-size: 15.5px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">True Out-of-Pocket Costs</div>
                  <div style="font-size: 13px; color: #A1A1AA; line-height: 1.45;">Full visibility into IELTS, embassy visa, and attestation expenses.</div>
                </div>
              </div>
            </div>

            <!-- Right Column: System Concept Diagram -->
            <div class="card-box" style="padding: 22px; display: flex; flex-direction: column; justify-content: space-between; background: #0A0A0C;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <div style="font-size: 16px; font-weight: 800; color: #FFFFFF;">ScholarX Autonomous Network Flow</div>
                <div class="badge-tag badge-green">Real-Time Execution</div>
              </div>

              <!-- Vector Diagram -->
              <svg viewBox="0 0 820 480" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; flex: 1;">
                <!-- Student Input Box -->
                <rect x="20" y="30" width="220" height="190" rx="10" fill="#121216" stroke="#27272A" stroke-width="1.5"/>
                <text x="40" y="65" fill="#38BDF8" font-size="13" font-weight="700">STUDENT PROFILE INPUT</text>
                <text x="40" y="95" fill="#FFFFFF" font-size="15" font-weight="700">Academic Background</text>
                <text x="40" y="120" fill="#A1A1AA" font-size="13">• GPA, Degree, Major</text>
                <text x="40" y="142" fill="#A1A1AA" font-size="13">• Test Scores (IELTS, GRE)</text>
                <text x="40" y="164" fill="#A1A1AA" font-size="13">• Field & Country Preferences</text>
                <text x="40" y="186" fill="#A1A1AA" font-size="13">• Available Upfront PKR Budget</text>

                <!-- Arrow Input -> Orchestrator -->
                <path d="M 240 125 L 300 125" stroke="#38BDF8" stroke-width="2" stroke-dasharray="4 4"/>
                <polygon points="300,121 310,125 300,129" fill="#38BDF8"/>

                <!-- Autonomous Core Box -->
                <rect x="310" y="20" width="480" height="280" rx="12" fill="#111116" stroke="#27272A" stroke-width="1.5"/>
                <text x="330" y="55" fill="#FFFFFF" font-size="14" font-weight="800">AUTONOMOUS MULTI-AGENT CORE</text>

                <!-- Orchestrator Box inside Core -->
                <rect x="330" y="75" width="210" height="70" rx="8" fill="#181820" stroke="#38BDF8"/>
                <text x="345" y="102" fill="#FFFFFF" font-size="15" font-weight="700">Orchestrator Commander</text>
                <text x="345" y="125" fill="#A1A1AA" font-size="12">Task Routing & State Machine</text>

                <!-- Discovery & Scouts inside Core -->
                <rect x="560" y="75" width="210" height="70" rx="8" fill="#181820" stroke="#10B981"/>
                <text x="575" y="102" fill="#FFFFFF" font-size="15" font-weight="700">Regional Scouts (6 Continents)</text>
                <text x="575" y="125" fill="#A1A1AA" font-size="12">Europe, Asia, Americas, MENA</text>

                <!-- Arrow Orchestrator <-> Scouts -->
                <path d="M 540 110 L 560 110" stroke="#10B981" stroke-width="2"/>

                <!-- Strict Verification & Skeptic inside Core -->
                <rect x="330" y="175" width="210" height="75" rx="8" fill="#181820" stroke="#EF4444"/>
                <text x="345" y="202" fill="#FFFFFF" font-size="15" font-weight="700">Skeptic Agent (Adversarial)</text>
                <text x="345" y="225" fill="#A1A1AA" font-size="12">Fraud & Criteria Challenge</text>

                <!-- Deterministic Workflows inside Core -->
                <rect x="560" y="175" width="210" height="75" rx="8" fill="#181820" stroke="#F59E0B"/>
                <text x="575" y="202" fill="#FFFFFF" font-size="15" font-weight="700">Deterministic Calculations</text>
                <text x="575" y="225" fill="#A1A1AA" font-size="12">PKR Math, Dates & HEC Rules</text>

                <!-- Arrows inside Core -->
                <path d="M 665 145 L 665 175" stroke="#F59E0B" stroke-width="2"/>
                <path d="M 560 212 L 540 212" stroke="#EF4444" stroke-width="2"/>

                <!-- Arrow Core -> Deliverable -->
                <path d="M 550 300 L 550 340" stroke="#10B981" stroke-width="2.5"/>
                <polygon points="545,340 550,350 555,340" fill="#10B981"/>

                <!-- Student Deliverable Box -->
                <rect x="180" y="350" width="610" height="110" rx="10" fill="#0D1A14" stroke="#10B981" stroke-width="1.5"/>
                <text x="210" y="380" fill="#10B981" font-size="13" font-weight="800">STUDENT ACTIONABLE DELIVERABLE</text>
                <text x="210" y="405" fill="#FFFFFF" font-size="16" font-weight="700">Verified Scholarship Matches & Action Roadmap</text>
                <text x="210" y="432" fill="#A1A1AA" font-size="13">
                  100% Verified Eligibility • Itemized PKR Costs • Official Direct Portals • Step-by-Step HEC/IBCC Guide
                </text>
              </svg>

              <!-- Bottom Notification Banner -->
              <div style="background: #121216; border: 1px solid var(--border-strong); border-radius: 8px; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10B981;"></span>
                  <span style="font-size: 13.5px; color: #FFFFFF; font-weight: 600;">Government Quotas Monitored:</span>
                  <span style="font-size: 13px; color: #A1A1AA;">Hungary Stipendium (400+), Chinese CSC (200+), Turkiye Burslari</span>
                </div>
                <span class="badge-tag badge-blue">Local & Private</span>
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">System Introduction</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">01 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_02():
    """Slide 02: What is an AI Agent? (The 6 Fundamental Pillars)"""
    return """
      <!-- SLIDE 02: WHAT IS AN AI AGENT? -->
      <section class="slide" id="slide-2" data-index="2">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">What is an AI Agent? The 6 Foundational Pillars</h1>
          <p class="slide-subheadline">An AI agent is not a chatbot. It is an autonomous software entity equipped with reasoning, memory, tools, and goals that operates in an iterative closed loop.</p>
        </header>

        <div class="slide-canvas">
          <!-- 6 Pillars in a 3x2 Grid -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 20px;">
            
            <!-- Pillar 1: LLM Brain -->
            <div class="card-box" style="padding: 22px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span class="badge-tag badge-slate">Pillar 01</span>
                <span style="font-size: 12px; font-family: var(--font-mono); color: #A1A1AA;">Cognitive Core</span>
              </div>
              <h2 class="card-title">LLM as the Brain</h2>
              <p class="card-desc">
                High-order cognitive reasoning, context decomposition, and strategic planning. Uses Gemini 3.7 Flash for deep multi-step logic and Gemini 3.0 Flash for resilient fallback.
              </p>
              <div style="margin-top: 12px; font-size: 13px; color: #FFFFFF; font-weight: 600;">
                Understands intent & plans actions
              </div>
            </div>

            <!-- Pillar 2: Tool Execution -->
            <div class="card-box" style="padding: 22px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span class="badge-tag badge-blue">Pillar 02</span>
                <span style="font-size: 12px; font-family: var(--font-mono); color: #A1A1AA;">Physical Hands</span>
              </div>
              <h2 class="card-title">Tool Execution</h2>
              <p class="card-desc">
                Direct capability to take real-world action — calling web search engines (Tavily, Firecrawl), extracting text from complex PDFs (PyMuPDF, Docling), and querying vector databases.
              </p>
              <div style="margin-top: 12px; font-size: 13px; color: #38BDF8; font-weight: 600;">
                Interacts with the outside world
              </div>
            </div>

            <!-- Pillar 3: Autonomy -->
            <div class="card-box" style="padding: 22px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span class="badge-tag badge-green">Pillar 03</span>
                <span style="font-size: 12px; font-family: var(--font-mono); color: #A1A1AA;">Self-Direction</span>
              </div>
              <h2 class="card-title">Autonomous Agency</h2>
              <p class="card-desc">
                Executes multi-step missions independently without requiring human micro-prompts. Navigates ambiguous errors, tries alternative queries, and self-directs toward completion.
              </p>
              <div style="margin-top: 12px; font-size: 13px; color: #10B981; font-weight: 600;">
                Independent problem solving
              </div>
            </div>

            <!-- Pillar 4: Memory -->
            <div class="card-box" style="padding: 22px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span class="badge-tag badge-amber">Pillar 04</span>
                <span style="font-size: 12px; font-family: var(--font-mono); color: #A1A1AA;">Context & Persistence</span>
              </div>
              <h2 class="card-title">Memory Systems</h2>
              <p class="card-desc">
                Short-term working context for live execution state; long-term vector (pgvector/ChromaDB) and SQLite session memory across hunts. Remembers research to avoid duplicate work.
              </p>
              <div style="margin-top: 12px; font-size: 13px; color: #F59E0B; font-weight: 600;">
                Retains facts across sessions
              </div>
            </div>

            <!-- Pillar 5: Iterative Loop -->
            <div class="card-box" style="padding: 22px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span class="badge-tag badge-rose">Pillar 05</span>
                <span style="font-size: 12px; font-family: var(--font-mono); color: #A1A1AA;">Dynamic Cycle</span>
              </div>
              <h2 class="card-title">Iterative Execution Loop</h2>
              <p class="card-desc">
                Never stops at the first guess. Operates in an active feedback loop: Perceive &rarr; Think &rarr; Act &rarr; Observe &rarr; Reflect until the objective is either fully satisfied or proven unfeasible.
              </p>
              <div style="margin-top: 12px; font-size: 13px; color: #EF4444; font-weight: 600;">
                Closed-loop trial and verification
              </div>
            </div>

            <!-- Pillar 6: Goal-Oriented -->
            <div class="card-box" style="padding: 22px;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <span class="badge-tag badge-green">Pillar 06</span>
                <span style="font-size: 12px; font-family: var(--font-mono); color: #A1A1AA;">Target Bound</span>
              </div>
              <h2 class="card-title">Goal-Oriented Optimization</h2>
              <p class="card-desc">
                Driven by a measurable outcome (e.g. find 5 fully funded verified master's programs in Europe matching GPA 3.4). Constantly measures progress against this target to prevent drift.
              </p>
              <div style="margin-top: 12px; font-size: 13px; color: #10B981; font-weight: 600;">
                Focused objective fulfillment
              </div>
            </div>

          </div>

          <!-- Bottom: Iterative Execution Loop Diagram -->
          <div class="card-box" style="padding: 20px 28px; background: #0C0C10; display: flex; flex-direction: column;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
              <span style="font-size: 15px; font-weight: 700; color: #FFFFFF;">The Agentic Execution Loop in Action</span>
              <span style="font-size: 13px; color: #A1A1AA;">Continuous Perceive &rarr; Think &rarr; Act Cycle</span>
            </div>

            <svg viewBox="0 0 1700 80" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto;">
              <!-- Step 1: Goal -->
              <rect x="10" y="10" width="220" height="60" rx="8" fill="#14141A" stroke="#27272A" stroke-width="1.5"/>
              <text x="120" y="38" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">1. Define Goal</text>
              <text x="120" y="56" text-anchor="middle" fill="#A1A1AA" font-size="12">Target Criteria & Budget</text>

              <path d="M 230 40 L 290 40" stroke="#3F3F46" stroke-width="2"/>
              <polygon points="290,36 300,40 290,44" fill="#3F3F46"/>

              <!-- Step 2: Perceive -->
              <rect x="300" y="10" width="230" height="60" rx="8" fill="#14141A" stroke="#38BDF8" stroke-width="1.5"/>
              <text x="415" y="38" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">2. Perceive State</text>
              <text x="415" y="56" text-anchor="middle" fill="#A1A1AA" font-size="12">Read Environment & Data</text>

              <path d="M 530 40 L 590 40" stroke="#3F3F46" stroke-width="2"/>
              <polygon points="590,36 600,40 590,44" fill="#3F3F46"/>

              <!-- Step 3: Think & Reason -->
              <rect x="600" y="10" width="230" height="60" rx="8" fill="#14141A" stroke="#94A3B8" stroke-width="1.5"/>
              <text x="715" y="38" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">3. Think & Plan</text>
              <text x="715" y="56" text-anchor="middle" fill="#A1A1AA" font-size="12">LLM Cognitive Reasoning</text>

              <path d="M 830 40 L 890 40" stroke="#3F3F46" stroke-width="2"/>
              <polygon points="890,36 900,40 890,44" fill="#3F3F46"/>

              <!-- Step 4: Act with Tools -->
              <rect x="900" y="10" width="230" height="60" rx="8" fill="#14141A" stroke="#10B981" stroke-width="1.5"/>
              <text x="1015" y="38" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">4. Act via Tools</text>
              <text x="1015" y="56" text-anchor="middle" fill="#A1A1AA" font-size="12">Crawlers, Parsers, DBs</text>

              <path d="M 1130 40 L 1190 40" stroke="#3F3F46" stroke-width="2"/>
              <polygon points="1190,36 1200,40 1190,44" fill="#3F3F46"/>

              <!-- Step 5: Observe Feedback -->
              <rect x="1200" y="10" width="230" height="60" rx="8" fill="#14141A" stroke="#F59E0B" stroke-width="1.5"/>
              <text x="1315" y="38" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">5. Observe & Reflect</text>
              <text x="1315" y="56" text-anchor="middle" fill="#A1A1AA" font-size="12">Evaluate Findings vs Target</text>

              <path d="M 1430 40 L 1490 40" stroke="#10B981" stroke-width="2"/>
              <polygon points="1490,36 1500,40 1490,44" fill="#10B981"/>

              <!-- Step 6: Goal Met -->
              <rect x="1500" y="10" width="190" height="60" rx="8" fill="#0E1E16" stroke="#10B981" stroke-width="2"/>
              <text x="1595" y="38" text-anchor="middle" fill="#10B981" font-size="15" font-weight="800">Goal Satisfied</text>
              <text x="1595" y="56" text-anchor="middle" fill="#D1FAE5" font-size="12">Dossier Generated</text>
            </svg>
          </div>

        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">Fundamentals of AI Agents</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">02 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_03():
    """Slide 03: Multi-Agent AI (How Multiple Agents Achieve the Main Agenda)"""
    return """
      <!-- SLIDE 03: MULTI-AGENT AI -->
      <section class="slide" id="slide-3" data-index="3">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Multi-Agent AI: Collaborative Intelligence in Action</h1>
          <p class="slide-subheadline">Complex goals overwhelm single agents. Multi-agent systems achieve the main agenda through specialized division of labor, state synchronization, and adversarial debate.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 32px; height: 100%;">
            
            <!-- Left Column: The 4 Multi-Agent Mechanics -->
            <div style="display: flex; flex-direction: column; gap: 16px; justify-content: space-between;">
              
              <div class="card-box" style="padding: 20px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF;">1. Specialized Division of Labor</h2>
                  <span class="badge-tag badge-slate">Domain Experts</span>
                </div>
                <p class="card-desc">
                  Instead of one generic agent doing everything poorly, agents specialize: Profile Analyst parses credentials, Regional Scouts crawl global portals, and the Skeptic audits claims.
                </p>
              </div>

              <div class="card-box" style="padding: 20px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF;">2. Shared State & Event-Driven Bus</h2>
                  <span class="badge-tag badge-blue">Pub/Sub Backbone</span>
                </div>
                <p class="card-desc">
                  Agents communicate asynchronously via Redis Pub/Sub and LangGraph typed state channels. When a Scout discovers a scholarship, it emits an event that awakens the Investigator and Skeptic.
                </p>
              </div>

              <div class="card-box" style="padding: 20px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF;">3. Adversarial Debate & Cross-Checking</h2>
                  <span class="badge-tag badge-rose">Zero Trust</span>
                </div>
                <p class="card-desc">
                  Productive disagreement prevents hallucinations. The Skeptic Agent actively challenges every discovery: <em>"Show primary source proof that Pakistani applicants are eligible for this stipend."</em>
                </p>
              </div>

              <div class="card-box" style="padding: 20px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF;">4. Collective Agenda Convergence</h2>
                  <span class="badge-tag badge-green">Goal Alignment</span>
                </div>
                <p class="card-desc">
                  All individual agent activities strictly converge toward the student's overarching goal: generating a ranked, verified, fraud-free scholarship roadmap calibrated to their exact background.
                </p>
              </div>

            </div>

            <!-- Right Column: Visual Diagram of Multi-Agent Interaction -->
            <div class="card-box" style="padding: 22px; display: flex; flex-direction: column; justify-content: space-between; background: #0A0A0C;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <div style="font-size: 16px; font-weight: 800; color: #FFFFFF;">Inter-Agent Event Bus & Convergence Architecture</div>
                <span class="badge-tag badge-slate">LangGraph + Redis</span>
              </div>

              <!-- SVG Diagram -->
              <svg viewBox="0 0 850 500" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; flex: 1;">
                
                <!-- Central Event Bus & State Hub -->
                <rect x="250" y="190" width="350" height="120" rx="14" fill="#141418" stroke="#38BDF8" stroke-width="2"/>
                <text x="425" y="230" text-anchor="middle" fill="#FFFFFF" font-size="17" font-weight="800">SHARED SYSTEM STATE</text>
                <text x="425" y="254" text-anchor="middle" fill="#38BDF8" font-size="13" font-weight="600">Redis Pub/Sub Event Bus & LangGraph Memory</text>
                <text x="425" y="280" text-anchor="middle" fill="#A1A1AA" font-size="12">Profile Context • Discovered Opportunities • Audit Status</text>

                <!-- Top Left: Orchestrator Agent -->
                <rect x="50" y="30" width="220" height="90" rx="10" fill="#181820" stroke="#94A3B8" stroke-width="1.5"/>
                <text x="160" y="65" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">Orchestrator Agent</text>
                <text x="160" y="88" text-anchor="middle" fill="#A1A1AA" font-size="12.5">Task Routing & Planning</text>
                <path d="M 180 120 L 290 190" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4 4"/>

                <!-- Top Right: Discovery Scouts -->
                <rect x="580" y="30" width="220" height="90" rx="10" fill="#181820" stroke="#10B981" stroke-width="1.5"/>
                <text x="690" y="65" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">Regional Scouts</text>
                <text x="690" y="88" text-anchor="middle" fill="#A1A1AA" font-size="12.5">Global Portal Crawlers</text>
                <path d="M 670 120 L 560 190" stroke="#10B981" stroke-width="2"/>
                <polygon points="562,185 550,196 565,195" fill="#10B981"/>

                <!-- Left Middle: Verification Agent -->
                <rect x="20" y="205" width="190" height="90" rx="10" fill="#181820" stroke="#38BDF8" stroke-width="1.5"/>
                <text x="115" y="245" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">Verification Agent</text>
                <text x="115" y="268" text-anchor="middle" fill="#A1A1AA" font-size="12">Official Source Cross-Check</text>
                <path d="M 210 250 L 250 250" stroke="#38BDF8" stroke-width="2"/>
                <polygon points="245,245 255,250 245,255" fill="#38BDF8"/>

                <!-- Right Middle: Skeptic Agent (Adversarial) -->
                <rect x="640" y="205" width="190" height="90" rx="10" fill="#181820" stroke="#EF4444" stroke-width="2"/>
                <text x="735" y="245" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">Skeptic Agent</text>
                <text x="735" y="268" text-anchor="middle" fill="#EF4444" font-size="12">Adversarial Stress-Testing</text>
                <path d="M 640 250 L 600 250" stroke="#EF4444" stroke-width="2"/>
                <polygon points="605,245 595,250 605,255" fill="#EF4444"/>

                <!-- Adversarial Loop Arrow between Skeptic and Bus -->
                <path d="M 735 205 C 735 150, 425 150, 425 190" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 3"/>
                <text x="580" y="150" fill="#EF4444" font-size="11" font-weight="700">Challenges Claims</text>

                <!-- Bottom Convergence: Synthesis & Advisor -->
                <path d="M 425 310 L 425 370" stroke="#10B981" stroke-width="2.5"/>
                <polygon points="420,370 425,380 430,370" fill="#10B981"/>

                <rect x="220" y="380" width="410" height="95" rx="12" fill="#0D1E16" stroke="#10B981" stroke-width="2"/>
                <text x="425" y="415" text-anchor="middle" fill="#10B981" font-size="16" font-weight="800">MAIN AGENDA ACHIEVED</text>
                <text x="425" y="438" text-anchor="middle" fill="#FFFFFF" font-size="14.5" font-weight="700">Fully Verified & Ranked Scholarship Roadmap</text>
                <text x="425" y="458" text-anchor="middle" fill="#A1A1AA" font-size="12">Zero Hallucinations • Pakistani Calibrated • Actionable Steps</text>
              </svg>

              <!-- Footer Tip -->
              <div style="font-size: 13px; color: #A1A1AA; border-top: 1px solid var(--border-muted); padding-top: 10px;">
                <strong style="color: #FFFFFF;">Why this works:</strong> Agents hold each other accountable through debate. The student never receives speculative or out-of-date scholarship claims.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">Multi-Agent Collaboration</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">03 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_04():
    """Slide 04: Workflows vs Agents (Deterministic Code vs Probabilistic LLM)"""
    return """
      <!-- SLIDE 04: WORKFLOWS VS AGENTS -->
      <section class="slide" id="slide-4" data-index="4">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Workflows vs. Agents: Deterministic Code Meets Probabilistic AI</h1>
          <p class="slide-subheadline">High-stakes systems require mathematical certainty alongside cognitive flexibility. ScholarX enforces deterministic guardrails around probabilistic agents.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- Side-by-Side Comparison Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px; flex: 1;">
              
              <!-- Left: Deterministic Workflows -->
              <div class="card-box" style="padding: 28px; background: #0A0F0D; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-green">Pure Code & Rules</span>
                    <span style="font-family: var(--font-mono); font-size: 13px; color: #10B981; font-weight: 700;">Deterministic</span>
                  </div>
                  <h2 style="font-size: 24px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Deterministic Workflows</h2>
                  <p style="font-size: 15px; color: #A1A1AA; line-height: 1.55; margin-bottom: 20px;">
                    Sequential code that guarantees identical outputs for identical inputs. Eliminates hallucinations in high-stakes mathematical, temporal, and rule-based steps.
                  </p>

                  <div style="display: flex; flex-direction: column; gap: 10px; font-size: 14.5px;">
                    <div style="display: flex; align-items: center; gap: 10px; color: #E4E4E7;">
                      <span style="color: #10B981; font-weight: 800;">✓</span> <strong>Zero Hallucination:</strong> Fixed logic, zero token drift or guessing.
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; color: #E4E4E7;">
                      <span style="color: #10B981; font-weight: 800;">✓</span> <strong>Microsecond Execution:</strong> Native Python speed with zero API latency.
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; color: #E4E4E7;">
                      <span style="color: #10B981; font-weight: 800;">✓</span> <strong>Zero Token Cost:</strong> Pure computation performed on local CPU.
                    </div>
                  </div>
                </div>

                <div style="background: #141E18; border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 14px 18px; margin-top: 20px;">
                  <div style="font-size: 12px; color: #10B981; font-weight: 700; margin-bottom: 6px;">Used in ScholarX For:</div>
                  <div style="font-size: 13.5px; color: #E4E4E7; line-height: 1.5;">
                    15-Point Eligibility Rules • PKR Currency Calculations • Visa Fee Tables • Deadline Day Math • Weighted Multi-Factor Ranking
                  </div>
                </div>
              </div>

              <!-- Right: Probabilistic Agents -->
              <div class="card-box" style="padding: 28px; background: #0E0E14; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-slate">LLM Reasoning</span>
                    <span style="font-family: var(--font-mono); font-size: 13px; color: #FFFFFF; font-weight: 700;">Probabilistic</span>
                  </div>
                  <h2 style="font-size: 24px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Probabilistic AI Agents</h2>
                  <p style="font-size: 15px; color: #A1A1AA; line-height: 1.55; margin-bottom: 20px;">
                    Cognitive models that reason over messy, ambiguous, unstructured real-world environments. Understands nuanced context and formulates creative strategies.
                  </p>

                  <div style="display: flex; flex-direction: column; gap: 10px; font-size: 14.5px;">
                    <div style="display: flex; align-items: center; gap: 10px; color: #E4E4E7;">
                      <span style="color: #38BDF8; font-weight: 800;">✓</span> <strong>Deep Comprehension:</strong> Understands complex CVs & messy PDFs.
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; color: #E4E4E7;">
                      <span style="color: #38BDF8; font-weight: 800;">✓</span> <strong>Adaptive Querying:</strong> Invents alternative search queries when blocked.
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; color: #E4E4E7;">
                      <span style="color: #38BDF8; font-weight: 800;">✓</span> <strong>Adversarial Critique:</strong> Detects suspicious claims & tests credibility.
                    </div>
                  </div>
                </div>

                <div style="background: #161820; border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 14px 18px; margin-top: 20px;">
                  <div style="font-size: 12px; color: #38BDF8; font-weight: 700; margin-bottom: 6px;">Used in ScholarX For:</div>
                  <div style="font-size: 13.5px; color: #E4E4E7; line-height: 1.5;">
                    Messy Student CV Extraction • Dynamic Discovery Generation • Skeptic Adversarial Audits • Tailored Application Strategy Advisory
                  </div>
                </div>
              </div>

            </div>

            <!-- Bottom: The ScholarX Hybrid Synthesis Architecture -->
            <div class="card-box" style="padding: 22px 30px; background: #0E0E12; border: 1px solid var(--border-strong);">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <div style="display: flex; align-items: center; gap: 14px;">
                  <span class="badge-tag badge-green">The ScholarX Law</span>
                  <span style="font-size: 16px; font-weight: 800; color: #FFFFFF;">Why We Need Both: Deterministic Guardrails Constrain Probabilistic Agents</span>
                </div>
                <span style="font-size: 13px; color: #A1A1AA; font-family: var(--font-mono);">Workflow-First Philosophy</span>
              </div>
              <p style="font-size: 15px; color: #E4E4E7; line-height: 1.6;">
                Pure agents run wild, cost unnecessary tokens, and hallucinate on arithmetic or dates. Pure workflows fail whenever data is unstructured or subjective. <strong>ScholarX pairs probabilistic discovery with deterministic verification gates.</strong> No LLM ever calculates a PKR exchange rate, checks a passport expiry date, or ranks scholarship scores.
              </p>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">System Design Philosophy</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">04 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_05():
    """Slide 05: The Problem: The Pakistani Scholarship Maze"""
    return """
      <!-- SLIDE 05: THE PROBLEM -->
      <section class="slide" id="slide-5" data-index="5">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">The Problem: Why Scholarships Go Unclaimed in Pakistan</h1>
          <p class="slide-subheadline">Every year, thousands of fully funded seats expire empty while talented Pakistani students remain stranded by fragmented information and unexpected costs.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 3 Core Crisis Pillars -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; flex: 1;">
              
              <!-- Trap 1 -->
              <div class="card-box" style="padding: 26px; background: #0E090B; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-rose">Hidden Quotas</span>
                    <span style="font-family: var(--font-mono); font-size: 13px; color: #EF4444;">40%+ Unclaimed</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 14px;">1. Scattered Bilateral Quotas</h2>
                  <p style="font-size: 14.5px; color: #A1A1AA; line-height: 1.6; margin-bottom: 18px;">
                    Government-to-government quotas reserved exclusively for Pakistani citizens (400+ Hungary Stipendium, 200+ Chinese CSC seats, Turkiye Burslari, Romania) are buried across embassy PDFs and outdated portals.
                  </p>
                </div>
                <div style="background: #180F12; border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 8px; padding: 12px 16px;">
                  <span style="font-size: 12.5px; color: #EF4444; font-weight: 700;">Consequence:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">Massive quotas expire empty every single intake because students simply never hear about them.</div>
                </div>
              </div>

              <!-- Trap 2 -->
              <div class="card-box" style="padding: 26px; background: #0E0C09; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-amber">Hidden Out-of-Pocket</span>
                    <span style="font-family: var(--font-mono); font-size: 13px; color: #F59E0B;">PKR 250K+ Shock</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 14px;">2. The Hidden Cost Shock</h2>
                  <p style="font-size: 14.5px; color: #A1A1AA; line-height: 1.6; margin-bottom: 18px;">
                    "Fully funded" tuition rarely means zero out-of-pocket expenses. Mandatory pre-departure costs blindsight students after months of effort: IELTS/TOEFL (PKR 75,600+), embassy biometric visas, medical exams, and attestation fees.
                  </p>
                </div>
                <div style="background: #1A140C; border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px; padding: 12px 16px;">
                  <span style="font-size: 12.5px; color: #F59E0B; font-weight: 700;">Consequence:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">Students abandon approved admissions at the final visa stage due to unbudgeted upfront PKR expenses.</div>
                </div>
              </div>

              <!-- Trap 3 -->
              <div class="card-box" style="padding: 26px; background: #080C10; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-blue">Local Bureaucracy</span>
                    <span style="font-family: var(--font-mono); font-size: 13px; color: #38BDF8;">Paperwork Gates</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 14px;">3. Bureaucratic Disqualification</h2>
                  <p style="font-size: 14.5px; color: #A1A1AA; line-height: 1.6; margin-bottom: 18px;">
                    Generic global engines ignore Pakistan-specific gates: HEC Higher Education Aptitude Test (HAT/USAT), IBCC equivalence formulas, and complex Ministry of Foreign Affairs (MOFA) attestation queues.
                  </p>
                </div>
                <div style="background: #0E1620; border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 8px; padding: 12px 16px;">
                  <span style="font-size: 12.5px; color: #38BDF8; font-weight: 700;">Consequence:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">Deserving applicants disqualified instantly on technical document errors before international review.</div>
                </div>
              </div>

            </div>

            <!-- Bottom: The Predatory Reality vs ScholarX Solution -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
              
              <div class="card-box" style="padding: 20px 24px; border: 1px solid #3F2025; background: #120A0C;">
                <div style="font-size: 13.5px; font-weight: 800; color: #EF4444; margin-bottom: 6px;">The Exploitative Status Quo</div>
                <div style="font-size: 14.5px; color: #E4E4E7; line-height: 1.5;">
                  Predatory educational agents charge PKR 150,000–300,000+ merely to fill out public forms, steering students toward low-grade private colleges that pay high agent commissions instead of merit-based fully funded quotas.
                </div>
              </div>

              <div class="card-box" style="padding: 20px 24px; border: 1px solid #1A3E2A; background: #0A140F;">
                <div style="font-size: 13.5px; font-weight: 800; color: #10B981; margin-bottom: 6px;">The ScholarX Resolution</div>
                <div style="font-size: 14.5px; color: #E4E4E7; line-height: 1.5;">
                  Autonomous multi-agent discovery scans 100% of official government and university sources directly. Zero middleman markup, 100% verified facts, completely free and open for every Pakistani student.
                </div>
              </div>

            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">The Pakistan Scholarship Maze</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">05 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_06():
    """Slide 06: Complete System Flowchart (All Agents & Workflows in ONE Unified Field)"""
    return """
      <!-- SLIDE 06: UNIFIED SYSTEM FLOWCHART -->
      <section class="slide" id="slide-6" data-index="6">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Complete System Flowchart: All Agents & Workflows</h1>
          <p class="slide-subheadline">The entire ScholarX intelligence engine operating in a single unified field: 5 specialized AI agents and 7 deterministic workflows orchestrated seamlessly.</p>
        </header>

        <div class="slide-canvas">
          <div class="card-box" style="padding: 18px; flex: 1; background: #08080A; display: flex; flex-direction: column; justify-content: space-between;">
            
            <!-- Complete High-Density Vector Flowchart -->
            <svg viewBox="0 0 1760 760" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; flex: 1;">
              
              <!-- ROW 1: STUDENT INPUT LAYER -->
              <rect x="500" y="10" width="760" height="60" rx="8" fill="#121820" stroke="#38BDF8" stroke-width="1.5"/>
              <text x="880" y="38" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="800">STUDENT INPUT LAYER</text>
              <text x="880" y="56" text-anchor="middle" fill="#A1A1AA" font-size="12">Academic Records (CV, Transcripts, GPA) • Field of Study • Destination Preferences • PKR Upfront Budget</text>

              <!-- Connector Row 1 -> Row 2 -->
              <path d="M 880 70 L 880 100" stroke="#38BDF8" stroke-width="2"/>
              <polygon points="876,100 880,108 884,100" fill="#38BDF8"/>

              <!-- ROW 2: INTAKE & PLANNING AGENTS -->
              <g id="row2-intake">
                <!-- Profile Analyst (Agent) -->
                <rect x="180" y="110" width="380" height="70" rx="8" fill="#14141A" stroke="#94A3B8" stroke-width="1.5"/>
                <rect x="195" y="122" width="65" height="20" rx="4" fill="rgba(148,163,184,0.2)"/>
                <text x="227" y="136" text-anchor="middle" fill="#CBD5E1" font-size="10" font-weight="700">AGENT</text>
                <text x="270" y="137" fill="#FFFFFF" font-size="15" font-weight="700">Profile Analyst Agent</text>
                <text x="195" y="162" fill="#A1A1AA" font-size="12">Extracts GPA, degree, publications from messy CVs & PDFs</text>

                <!-- Orchestrator (Commander Agent) -->
                <rect x="690" y="110" width="380" height="70" rx="8" fill="#14141A" stroke="#38BDF8" stroke-width="2"/>
                <rect x="705" y="122" width="65" height="20" rx="4" fill="rgba(56,189,248,0.2)"/>
                <text x="737" y="136" text-anchor="middle" fill="#38BDF8" font-size="10" font-weight="700">AGENT</text>
                <text x="780" y="137" fill="#FFFFFF" font-size="16" font-weight="800">Orchestrator (Commander)</text>
                <text x="705" y="162" fill="#A1A1AA" font-size="12">LangGraph cyclic state graph, error recovery, execution routing</text>

                <!-- Document Analyst (Agent) -->
                <rect x="1200" y="110" width="380" height="70" rx="8" fill="#14141A" stroke="#94A3B8" stroke-width="1.5"/>
                <rect x="1215" y="122" width="65" height="20" rx="4" fill="rgba(148,163,184,0.2)"/>
                <text x="1247" y="136" text-anchor="middle" fill="#CBD5E1" font-size="10" font-weight="700">AGENT</text>
                <text x="1290" y="137" fill="#FFFFFF" font-size="15" font-weight="700">Document Analyst Agent</text>
                <text x="1215" y="162" fill="#A1A1AA" font-size="12">Assesses SOP/FRC readiness & detects Pakistan paperwork gaps</text>

                <!-- Connecting Lines Row 2 -->
                <path d="M 560 145 L 690 145" stroke="#3F3F46" stroke-width="1.5"/>
                <path d="M 1070 145 L 1200 145" stroke="#3F3F46" stroke-width="1.5"/>
              </g>

              <!-- Connector Row 2 -> Row 3 -->
              <path d="M 880 180 L 880 215" stroke="#38BDF8" stroke-width="2"/>
              <polygon points="876,215 880,223 884,215" fill="#38BDF8"/>

              <!-- ROW 3: DISCOVERY CLUSTER (1 Agent + 4 Workflows) -->
              <g id="row3-discovery">
                <!-- Discovery Commander (Agent) -->
                <rect x="690" y="225" width="380" height="65" rx="8" fill="#14141A" stroke="#38BDF8" stroke-width="1.5"/>
                <rect x="705" y="235" width="65" height="18" rx="4" fill="rgba(56,189,248,0.2)"/>
                <text x="737" y="248" text-anchor="middle" fill="#38BDF8" font-size="10" font-weight="700">AGENT</text>
                <text x="780" y="249" fill="#FFFFFF" font-size="15" font-weight="700">Discovery Commander Agent</text>
                <text x="705" y="272" fill="#A1A1AA" font-size="12">Generates optimized search queries tailored to student profile</text>

                <!-- Fan-out to 4 Regional Scouts (Deterministic Workflows) -->
                <path d="M 880 290 L 880 310" stroke="#10B981" stroke-width="2"/>
                <path d="M 230 310 L 1530 310" stroke="#10B981" stroke-width="1.5"/>

                <!-- Scout 1: Europe -->
                <path d="M 230 310 L 230 325" stroke="#10B981" stroke-width="1.5"/>
                <rect x="80" y="325" width="300" height="65" rx="8" fill="#0E1A14" stroke="#10B981"/>
                <rect x="95" y="335" width="80" height="18" rx="4" fill="rgba(16,185,129,0.2)"/>
                <text x="135" y="348" text-anchor="middle" fill="#10B981" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="185" y="349" fill="#FFFFFF" font-size="14" font-weight="700">Europe Scout</text>
                <text x="95" y="372" fill="#A1A1AA" font-size="11.5">DAAD, Erasmus, Hungary Stipendium</text>

                <!-- Scout 2: Asia -->
                <path d="M 660 310 L 660 325" stroke="#10B981" stroke-width="1.5"/>
                <rect x="510" y="325" width="300" height="65" rx="8" fill="#0E1A14" stroke="#10B981"/>
                <rect x="525" y="335" width="80" height="18" rx="4" fill="rgba(16,185,129,0.2)"/>
                <text x="565" y="348" text-anchor="middle" fill="#10B981" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="615" y="349" fill="#FFFFFF" font-size="14" font-weight="700">Asia Scout</text>
                <text x="525" y="372" fill="#A1A1AA" font-size="11.5">China CSC, MEXT Japan, Turkiye Burslari</text>

                <!-- Scout 3: Americas -->
                <path d="M 1100 310 L 1100 325" stroke="#10B981" stroke-width="1.5"/>
                <rect x="950" y="325" width="300" height="65" rx="8" fill="#0E1A14" stroke="#10B981"/>
                <rect x="965" y="335" width="80" height="18" rx="4" fill="rgba(16,185,129,0.2)"/>
                <text x="1005" y="348" text-anchor="middle" fill="#10B981" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="1055" y="349" fill="#FFFFFF" font-size="14" font-weight="700">Americas Scout</text>
                <text x="965" y="372" fill="#A1A1AA" font-size="11.5">Fulbright, OAS, Canadian Provincial</text>

                <!-- Scout 4: MENA & Oceania -->
                <path d="M 1530 310 L 1530 325" stroke="#10B981" stroke-width="1.5"/>
                <rect x="1380" y="325" width="300" height="65" rx="8" fill="#0E1A14" stroke="#10B981"/>
                <rect x="1395" y="335" width="80" height="18" rx="4" fill="rgba(16,185,129,0.2)"/>
                <text x="1435" y="348" text-anchor="middle" fill="#10B981" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="1485" y="349" fill="#FFFFFF" font-size="14" font-weight="700">MENA & Oceania Scout</text>
                <text x="1395" y="372" fill="#A1A1AA" font-size="11.5">KAUST, Qatar Foundation, Australia Awards</text>
              </g>

              <!-- Connector Scouts Fan-in -> Row 4 -->
              <path d="M 230 390 L 230 410" stroke="#10B981" stroke-width="1.5"/>
              <path d="M 660 390 L 660 410" stroke="#10B981" stroke-width="1.5"/>
              <path d="M 1100 390 L 1100 410" stroke="#10B981" stroke-width="1.5"/>
              <path d="M 1530 390 L 1530 410" stroke="#10B981" stroke-width="1.5"/>
              <path d="M 230 410 L 1530 410" stroke="#10B981" stroke-width="1.5"/>
              <path d="M 880 410 L 880 430" stroke="#10B981" stroke-width="2"/>
              <polygon points="876,430 880,438 884,430" fill="#10B981"/>

              <!-- ROW 4: DETERMINISTIC GUARDRAIL PIPELINES -->
              <g id="row4-guardrails">
                <!-- Eligibility Investigator (Workflow) -->
                <rect x="150" y="440" width="460" height="70" rx="8" fill="#14120A" stroke="#F59E0B" stroke-width="1.5"/>
                <rect x="165" y="452" width="80" height="18" rx="4" fill="rgba(245,158,11,0.2)"/>
                <text x="205" y="465" text-anchor="middle" fill="#F59E0B" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="255" y="466" fill="#FFFFFF" font-size="15" font-weight="700">Eligibility Investigator</text>
                <text x="165" y="492" fill="#A1A1AA" font-size="12">15 hard qualification checks: nationality, GPA cutoff, degree match, age limit</text>

                <!-- True Cost Analyzer (Workflow) -->
                <rect x="650" y="440" width="460" height="70" rx="8" fill="#14120A" stroke="#F59E0B" stroke-width="1.5"/>
                <rect x="665" y="452" width="80" height="18" rx="4" fill="rgba(245,158,11,0.2)"/>
                <text x="705" y="465" text-anchor="middle" fill="#F59E0B" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="755" y="466" fill="#FFFFFF" font-size="15" font-weight="700">True Cost Analyzer</text>
                <text x="665" y="492" fill="#A1A1AA" font-size="12">Deterministic PKR arithmetic: IELTS, visa, attestations, flight, deposits</text>

                <!-- Deadline Intelligence (Workflow) -->
                <rect x="1150" y="440" width="460" height="70" rx="8" fill="#14120A" stroke="#F59E0B" stroke-width="1.5"/>
                <rect x="1165" y="452" width="80" height="18" rx="4" fill="rgba(245,158,11,0.2)"/>
                <text x="1205" y="465" text-anchor="middle" fill="#F59E0B" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="1255" y="466" fill="#FFFFFF" font-size="15" font-weight="700">Deadline Intelligence</text>
                <text x="1165" y="492" fill="#A1A1AA" font-size="12">Date delta calculations, Pakistani prep buffer, urgency risk scores</text>

                <!-- Internal Flow Row 4 -->
                <path d="M 610 475 L 650 475" stroke="#F59E0B" stroke-width="1.5"/>
                <path d="M 1110 475 L 1150 475" stroke="#F59E0B" stroke-width="1.5"/>
              </g>

              <!-- Connector Row 4 -> Row 5 -->
              <path d="M 880 510 L 880 540" stroke="#F59E0B" stroke-width="2"/>
              <polygon points="876,540 880,548 884,540" fill="#F59E0B"/>

              <!-- ROW 5: ADVERSARIAL AUDIT & SKEPTIC CHALLENGE -->
              <g id="row5-adversarial">
                <!-- Verification Agent -->
                <rect x="350" y="550" width="460" height="70" rx="8" fill="#121820" stroke="#38BDF8" stroke-width="1.5"/>
                <rect x="365" y="562" width="65" height="18" rx="4" fill="rgba(56,189,248,0.2)"/>
                <text x="397" y="575" text-anchor="middle" fill="#38BDF8" font-size="10" font-weight="700">AGENT</text>
                <text x="440" y="576" fill="#FFFFFF" font-size="15" font-weight="700">Verification Agent</text>
                <text x="365" y="602" fill="#A1A1AA" font-size="12">Validates official university URLs, current academic year guidelines</text>

                <!-- Double Sided Arrow: Debate -->
                <path d="M 810 585 L 950 585" stroke="#EF4444" stroke-width="2"/>
                <polygon points="815,580 805,585 815,590" fill="#EF4444"/>
                <polygon points="945,580 955,585 945,590" fill="#EF4444"/>
                <text x="880" y="575" text-anchor="middle" fill="#EF4444" font-size="11" font-weight="800">ADVERSARIAL DEBATE</text>

                <!-- Skeptic Agent -->
                <rect x="950" y="550" width="460" height="70" rx="8" fill="#1C1012" stroke="#EF4444" stroke-width="2"/>
                <rect x="965" y="562" width="65" height="18" rx="4" fill="rgba(239,68,68,0.2)"/>
                <text x="997" y="575" text-anchor="middle" fill="#EF4444" font-size="10" font-weight="700">AGENT</text>
                <text x="1040" y="576" fill="#FFFFFF" font-size="15" font-weight="700">Skeptic Agent (Adversary)</text>
                <text x="965" y="602" fill="#A1A1AA" font-size="12">Actively attempts to disqualify: checks quota cuts, hidden catches, fraud</text>
              </g>

              <!-- Connector Row 5 -> Row 6 -->
              <path d="M 880 620 L 880 645" stroke="#10B981" stroke-width="2"/>
              <polygon points="876,645 880,653 884,645" fill="#10B981"/>

              <!-- ROW 6: SYNTHESIS, RANKING & FINAL ADVISOR -->
              <g id="row6-delivery">
                <!-- Synthesis (Workflow) -->
                <rect x="180" y="655" width="360" height="65" rx="8" fill="#0E1A14" stroke="#10B981"/>
                <rect x="195" y="667" width="80" height="18" rx="4" fill="rgba(16,185,129,0.2)"/>
                <text x="235" y="680" text-anchor="middle" fill="#10B981" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="285" y="681" fill="#FFFFFF" font-size="14" font-weight="700">Synthesis Engine</text>
                <text x="195" y="704" fill="#A1A1AA" font-size="11.5">Deduplication, evidence trail binding</text>

                <!-- Ranking Engine (Workflow) -->
                <rect x="580" y="655" width="360" height="65" rx="8" fill="#0E1A14" stroke="#10B981"/>
                <rect x="595" y="667" width="80" height="18" rx="4" fill="rgba(16,185,129,0.2)"/>
                <text x="635" y="680" text-anchor="middle" fill="#10B981" font-size="10" font-weight="700">WORKFLOW</text>
                <text x="685" y="681" fill="#FFFFFF" font-size="14" font-weight="700">Ranking Engine</text>
                <text x="595" y="704" fill="#A1A1AA" font-size="11.5">Multi-factor weighted scoring formula</text>

                <!-- Final Advisor (Agent) -->
                <rect x="980" y="655" width="360" height="65" rx="8" fill="#14141A" stroke="#94A3B8" stroke-width="1.5"/>
                <rect x="995" y="667" width="65" height="18" rx="4" fill="rgba(148,163,184,0.2)"/>
                <text x="1027" y="680" text-anchor="middle" fill="#CBD5E1" font-size="10" font-weight="700">AGENT</text>
                <text x="1070" y="681" fill="#FFFFFF" font-size="14" font-weight="700">Final Advisor Agent</text>
                <text x="995" y="704" fill="#A1A1AA" font-size="11.5">Actionable strategy narrative & roadmaps</text>

                <!-- Student Deliverable -->
                <rect x="1380" y="655" width="320" height="65" rx="8" fill="#0D1E16" stroke="#10B981" stroke-width="2"/>
                <text x="1540" y="683" text-anchor="middle" fill="#10B981" font-size="15" font-weight="800">STUDENT DELIVERABLE</text>
                <text x="1540" y="704" text-anchor="middle" fill="#D1FAE5" font-size="12">Ranked, Verified & Actionable Dossier</text>

                <!-- Connectors Row 6 -->
                <path d="M 540 687 L 580 687" stroke="#10B981" stroke-width="1.5"/>
                <path d="M 940 687 L 980 687" stroke="#10B981" stroke-width="1.5"/>
                <path d="M 1340 687 L 1380 687" stroke="#10B981" stroke-width="2"/>
                <polygon points="1375,683 1383,687 1375,691" fill="#10B981"/>
              </g>

            </svg>

            <!-- Bottom Flowchart Legend -->
            <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--border-subtle); padding-top: 12px; margin-top: 6px; font-size: 13px;">
              <div style="display: flex; align-items: center; gap: 28px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(56,189,248,0.2); border: 1.5px solid #38BDF8;"></span>
                  <span style="color: #FFFFFF; font-weight: 600;">AI Agents (5):</span>
                  <span style="color: #A1A1AA;">Orchestrator, Profile Analyst, Document Analyst, Skeptic, Final Advisor</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(16,185,129,0.2); border: 1.5px solid #10B981;"></span>
                  <span style="color: #FFFFFF; font-weight: 600;">Deterministic Workflows (7):</span>
                  <span style="color: #A1A1AA;">4 Regional Scouts, Eligibility Check, Cost Analyzer, Deadline Math, Synthesis, Ranking</span>
                </div>
              </div>
              <div style="color: #A1A1AA; font-family: var(--font-mono); font-size: 12.5px;">
                Architecture Source: Agents.md
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">Full System Flowchart</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">06 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_07():
    """Slide 07: What ScholarX Does: The Student Journey"""
    return """
      <!-- SLIDE 07: THE STUDENT JOURNEY -->
      <section class="slide" id="slide-7" data-index="7">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">What ScholarX Does: The 4-Stage Student Journey</h1>
          <p class="slide-subheadline">From messy academic records to verified global scholarship applications in minutes, completely free and local-first.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 4 Step Journey Cards Horizontal -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
              
              <!-- Stage 1 -->
              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-blue">Stage 01</span>
                    <span style="font-family: var(--font-mono); font-size: 12px; color: #A1A1AA;">2 Minutes</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Intake & Extraction</h2>
                  <p class="card-desc">
                    Drag and drop your Pakistani university CV, transcript, or type background. Profile Analyst parses GPA, degree type, publications, and test scores with zero tedious forms.
                  </p>
                </div>
                <div style="background: #141820; border: 1px solid var(--border-strong); border-radius: 8px; padding: 12px 14px; margin-top: 16px;">
                  <span style="font-size: 12px; color: #38BDF8; font-weight: 700;">Extracted Data:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">BS CS (3.52 CGPA), FAST-NUCES, IELTS 7.0, Budget: PKR 150K</div>
                </div>
              </div>

              <!-- Stage 2 -->
              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-slate">Stage 02</span>
                    <span style="font-family: var(--font-mono); font-size: 12px; color: #A1A1AA;">Parallel Sweep</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Autonomous Hunt</h2>
                  <p class="card-desc">
                    Discovery Commander generates targeted queries. 4 Regional Scouts simultaneously crawl live government databases, embassy websites, and university portals across 6 continents.
                  </p>
                </div>
                <div style="background: #161820; border: 1px solid var(--border-strong); border-radius: 8px; padding: 12px 14px; margin-top: 16px;">
                  <span style="font-size: 12px; color: #38BDF8; font-weight: 700;">Portals Scanned:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">Stipendium Hungaricum, China CSC, DAAD, Erasmus, KAUST</div>
                </div>
              </div>

              <!-- Stage 3 -->
              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-rose">Stage 03</span>
                    <span style="font-family: var(--font-mono); font-size: 12px; color: #A1A1AA;">Zero Trust</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Adversarial Audit</h2>
                  <p class="card-desc">
                    Eligibility Investigator tests 15 strict criteria. True Cost Analyzer calculates upfront PKR expenses. The Skeptic Agent challenges every program with rigorous adversarial stress tests.
                  </p>
                </div>
                <div style="background: #1C1012; border: 1px solid var(--border-strong); border-radius: 8px; padding: 12px 14px; margin-top: 16px;">
                  <span style="font-size: 12px; color: #EF4444; font-weight: 700;">Audit Gates:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">Pakistani Eligibility Verified • Real PKR Costs Computed • Links Live</div>
                </div>
              </div>

              <!-- Stage 4 -->
              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <span class="badge-tag badge-green">Stage 04</span>
                    <span style="font-family: var(--font-mono); font-size: 12px; color: #A1A1AA;">Ready to Apply</span>
                  </div>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Action Roadmap</h2>
                  <p class="card-desc">
                    Ranking Engine scores opportunities by financial security, prestige, and match fit. Final Advisor creates a customized application dossier with HEC/IBCC steps and deadline timelines.
                  </p>
                </div>
                <div style="background: #0E1A14; border: 1px solid var(--border-strong); border-radius: 8px; padding: 12px 14px; margin-top: 16px;">
                  <span style="font-size: 12px; color: #10B981; font-weight: 700;">Final Output:</span>
                  <div style="font-size: 13px; color: #E4E4E7; margin-top: 4px;">Tailored Application Strategy • Official Links • Zero Hallucinations</div>
                </div>
              </div>

            </div>

            <!-- Bottom: Real-Time Performance & Integrity Guarantees -->
            <div class="card-box" style="padding: 20px 30px; background: #0C0C10; display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
              <div style="display: flex; align-items: center; gap: 36px;">
                <div>
                  <div style="font-size: 26px; font-weight: 800; color: #10B981; font-family: var(--font-mono);">~90s</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Average Hunt Duration</div>
                </div>
                <div style="height: 36px; width: 1px; background: var(--border-strong);"></div>
                <div>
                  <div style="font-size: 26px; font-weight: 800; color: #FFFFFF; font-family: var(--font-mono);">15/15</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Eligibility Criteria Checked</div>
                </div>
                <div style="height: 36px; width: 1px; background: var(--border-strong);"></div>
                <div>
                  <div style="font-size: 26px; font-weight: 800; color: #38BDF8; font-family: var(--font-mono);">100%</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Primary Source Traceability</div>
                </div>
                <div style="height: 36px; width: 1px; background: var(--border-strong);"></div>
                <div>
                  <div style="font-size: 26px; font-weight: 800; color: #F59E0B; font-family: var(--font-mono);">PKR 0</div>
                  <div style="font-size: 13px; color: #A1A1AA;">Total Cost to the Student</div>
                </div>
              </div>

              <div style="font-size: 13.5px; color: #A1A1AA; max-width: 480px; text-align: right; line-height: 1.5;">
                Every recommendation links directly to official government or university portals. No affiliate redirects, no sponsored promotions.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">The Student Experience</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">07 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_08():
    """Slide 08: Built for Pakistani Students: Sovereign Bureaucratic Intelligence"""
    return """
      <!-- SLIDE 08: BUILT FOR PAKISTANI STUDENTS -->
      <section class="slide" id="slide-8" data-index="8">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Built for Pakistani Students: Bureaucratic Intelligence</h1>
          <p class="slide-subheadline">Generic global platforms ignore local Pakistani realities. ScholarX is natively engineered around Pakistan's educational and financial structures.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; height: 100%;">
            
            <!-- Left: 3 Bureaucratic Intelligence Pillars -->
            <div style="display: flex; flex-direction: column; gap: 18px; justify-content: space-between;">
              
              <div class="card-box" style="padding: 22px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <h2 style="font-size: 19px; font-weight: 800; color: #FFFFFF;">HEC HAT & IBCC Equivalence Engine</h2>
                  <span class="badge-tag badge-green">Local Grading</span>
                </div>
                <p class="card-desc">
                  Understands Pakistani university CGPAs (4.0 and 5.0 scales), percentage calculations, and board division systems. Automatically identifies required HEC Higher Education Aptitude Tests (HAT-I through HAT-IV) and IBCC equivalencies.
                </p>
              </div>

              <div class="card-box" style="padding: 22px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <h2 style="font-size: 19px; font-weight: 800; color: #FFFFFF;">Attestation & MOFA Sequence Planning</h2>
                  <span class="badge-tag badge-blue">Paperwork Roadmap</span>
                </div>
                <p class="card-desc">
                  Foreign embassies require strict document legalization. ScholarX generates step-by-step guidance for Board attestation &rarr; IBCC equivalence &rarr; HEC degree verification &rarr; Ministry of Foreign Affairs (MOFA) stamps.
                </p>
              </div>

              <div class="card-box" style="padding: 22px;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <h2 style="font-size: 19px; font-weight: 800; color: #FFFFFF;">Bilateral Quota Tracking (G2G)</h2>
                  <span class="badge-tag badge-slate">Guaranteed Seats</span>
                </div>
                <p class="card-desc">
                  Directly tracks government-to-government scholarship quotas specifically allocated for Pakistani passport holders: Hungary Stipendium (400+ seats), China CSC (200+ seats), Turkiye Burslari, and Romanian government seats.
                </p>
              </div>

            </div>

            <!-- Right: True Out-of-Pocket PKR Cost Engine Table -->
            <div class="card-box" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between; background: #0C0C10;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                  <div style="font-size: 17px; font-weight: 800; color: #FFFFFF;">True Out-of-Pocket Pre-Departure PKR Calculator</div>
                  <span class="badge-tag badge-amber">No Surprises</span>
                </div>
                <p style="font-size: 14.5px; color: #A1A1AA; line-height: 1.5; margin-bottom: 18px;">
                  Even a 100% "fully funded" scholarship requires upfront capital in Pakistan before flight tickets are issued. ScholarX itemizes every expected rupee:
                </p>

                <!-- Cost Table -->
                <div style="background: #121216; border: 1px solid var(--border-strong); border-radius: 8px; overflow: hidden; margin-bottom: 16px;">
                  <div style="display: grid; grid-template-columns: 2fr 1.2fr 1fr; padding: 10px 16px; background: #181820; font-size: 12px; font-weight: 700; color: #A1A1AA;">
                    <div>Pre-Departure Expense</div>
                    <div>Typical Cost (PKR)</div>
                    <div>Timing</div>
                  </div>
                  
                  <div style="display: grid; grid-template-columns: 2fr 1.2fr 1fr; padding: 12px 16px; border-top: 1px solid var(--border-muted); font-size: 13.5px; color: #E4E4E7;">
                    <div>IELTS / TOEFL Exam Registration</div>
                    <div style="font-family: var(--font-mono); font-weight: 600; color: #FFFFFF;">PKR 75,600 – 76,240</div>
                    <div style="color: #A1A1AA;">Month -4</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr 1fr; padding: 12px 16px; border-top: 1px solid var(--border-muted); font-size: 13.5px; color: #E4E4E7;">
                    <div>HEC & IBCC Degree Attestation</div>
                    <div style="font-family: var(--font-mono); font-weight: 600; color: #FFFFFF;">PKR 12,000 – 18,000</div>
                    <div style="color: #A1A1AA;">Month -3</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr 1fr; padding: 12px 16px; border-top: 1px solid var(--border-muted); font-size: 13.5px; color: #E4E4E7;">
                    <div>Embassy Biometric Visa & VFS Processing</div>
                    <div style="font-family: var(--font-mono); font-weight: 600; color: #FFFFFF;">PKR 28,000 – 45,000</div>
                    <div style="color: #A1A1AA;">Month -2</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr 1fr; padding: 12px 16px; border-top: 1px solid var(--border-muted); font-size: 13.5px; color: #E4E4E7;">
                    <div>Medical Examination (IOM / Approved Clinic)</div>
                    <div style="font-family: var(--font-mono); font-weight: 600; color: #FFFFFF;">PKR 22,000 – 35,000</div>
                    <div style="color: #A1A1AA;">Month -1</div>
                  </div>

                  <div style="display: grid; grid-template-columns: 2fr 1.2fr 1fr; padding: 14px 16px; border-top: 2px solid var(--border-strong); background: #16161E; font-size: 14px; font-weight: 700; color: #FFFFFF;">
                    <div>Estimated Upfront Readiness Total:</div>
                    <div style="font-family: var(--font-mono); color: #F59E0B; font-size: 15px;">PKR 137,600 – 174,240</div>
                    <div style="color: #10B981; font-size: 12px;">Recoverable</div>
                  </div>
                </div>
              </div>

              <!-- Clarity Callout -->
              <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px; padding: 12px 16px; font-size: 13.5px; color: #D4D4D8; line-height: 1.5;">
                <strong style="color: #F59E0B;">Financial Reality:</strong> ScholarX compares this upfront requirement against the student's declared budget to ensure no Pakistani student gets stuck halfway through their journey.
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">Pakistani Bureaucratic Alignment</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">08 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_09():
    """Slide 09: Complete Tech Stack & Architecture"""
    return """
      <!-- SLIDE 09: COMPLETE TECH STACK -->
      <section class="slide" id="slide-9" data-index="9">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Complete Tech Stack & Engineering Architecture</h1>
          <p class="slide-subheadline">A robust, local-first engineering architecture combining state-of-the-art Python orchestration, modern React interfaces, and resilient multi-key failover.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 20px; height: 100%;">
            
            <!-- 5 Architectural Tiers in 5 Columns -->
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; flex: 1;">
              
              <!-- Tier 1: Frontend -->
              <div class="card-box" style="padding: 20px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span class="badge-tag badge-blue">UI Layer</span>
                    <span style="font-family: var(--font-mono); font-size: 11px; color: #A1A1AA;">Port: 3000</span>
                  </div>
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Frontend Client</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; color: #D4D4D8;">
                    <div>• <strong>Next.js 15</strong> (App Router)</div>
                    <div>• <strong>React 19</strong></div>
                    <div>• <strong>TypeScript 5.7</strong></div>
                    <div>• <strong>Tailwind CSS v4</strong></div>
                    <div>• <strong>Framer Motion</strong></div>
                    <div>• <strong>@xyflow/react</strong> (Graph)</div>
                    <div>• <strong>Lucide React</strong></div>
                    <div>• <strong>Zustand</strong> (State)</div>
                  </div>
                </div>
                <div style="font-size: 11.5px; color: #38BDF8; font-family: var(--font-mono); margin-top: 12px;">
                  High-FPS Graph Canvas
                </div>
              </div>

              <!-- Tier 2: Backend -->
              <div class="card-box" style="padding: 20px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span class="badge-tag badge-slate">Engine</span>
                    <span style="font-family: var(--font-mono); font-size: 11px; color: #A1A1AA;">Port: 8000</span>
                  </div>
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Backend Core</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; color: #D4D4D8;">
                    <div>• <strong>Python 3.12+</strong></div>
                    <div>• <strong>FastAPI</strong> (Async ASGI)</div>
                    <div>• <strong>LangGraph</strong> (State Graph)</div>
                    <div>• <strong>LangChain Core</strong></div>
                    <div>• <strong>Pydantic v2</strong> (Schemas)</div>
                    <div>• <strong>Uvicorn</strong> (Server)</div>
                    <div>• <strong>Tenacity</strong> (Retry logic)</div>
                    <div>• <strong>SSE</strong> (Real-time events)</div>
                  </div>
                </div>
                <div style="font-size: 11.5px; color: #FFFFFF; font-family: var(--font-mono); margin-top: 12px;">
                  Cyclic State Orchestrator
                </div>
              </div>

              <!-- Tier 3: Parsing & Crawlers -->
              <div class="card-box" style="padding: 20px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span class="badge-tag badge-green">Extraction</span>
                    <span style="font-family: var(--font-mono); font-size: 11px; color: #A1A1AA;">Local + APIs</span>
                  </div>
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Parsers & Scrapers</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; color: #D4D4D8;">
                    <div>• <strong>PyMuPDF4LLM</strong> (CVs)</div>
                    <div>• <strong>pdfplumber</strong> (Tables)</div>
                    <div>• <strong>Docling</strong> (Complex docs)</div>
                    <div>• <strong>Tavily Search API</strong></div>
                    <div>• <strong>Firecrawl API</strong></div>
                    <div>• <strong>Jina Reader API</strong></div>
                    <div>• <strong>Crawl4AI</strong> (Headless)</div>
                    <div>• <strong>pypdf</strong> (Fast scan)</div>
                  </div>
                </div>
                <div style="font-size: 11.5px; color: #10B981; font-family: var(--font-mono); margin-top: 12px;">
                  Multi-Modal PDF & Web
                </div>
              </div>

              <!-- Tier 4: Data Store -->
              <div class="card-box" style="padding: 20px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span class="badge-tag badge-amber">Storage</span>
                    <span style="font-family: var(--font-mono); font-size: 11px; color: #A1A1AA;">Docker Local</span>
                  </div>
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Data & Memory</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; color: #D4D4D8;">
                    <div>• <strong>PostgreSQL 16</strong></div>
                    <div>• <strong>pgvector</strong> (Embeddings)</div>
                    <div>• <strong>Redis 7</strong> (Pub/Sub)</div>
                    <div>• <strong>ChromaDB</strong> (Vector store)</div>
                    <div>• <strong>SQLite</strong> (Sessions)</div>
                    <div>• <strong>aiosqlite</strong> (Async DB)</div>
                    <div>• <strong>JSONL</strong> (Event logs)</div>
                    <div>• <strong>Local Cache</strong></div>
                  </div>
                </div>
                <div style="font-size: 11.5px; color: #F59E0B; font-family: var(--font-mono); margin-top: 12px;">
                  Persistent Local State
                </div>
              </div>

              <!-- Tier 5: LLMs & Failover -->
              <div class="card-box" style="padding: 20px; justify-content: space-between;">
                <div>
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <span class="badge-tag badge-rose">Inference</span>
                    <span style="font-family: var(--font-mono); font-size: 11px; color: #A1A1AA;">Multi-Key</span>
                  </div>
                  <h2 style="font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">LLMs & Fallback</h2>
                  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; color: #D4D4D8;">
                    <div>• <strong>Gemini 3.7 Flash</strong> (Main)</div>
                    <div>• <strong>Gemini 3.0 Flash</strong> (Safe)</div>
                    <div>• <strong>Groq gpt-oss-120b</strong></div>
                    <div>• <strong>3 Gemini Keys</strong> (Rotated)</div>
                    <div>• <strong>4 Groq Keys</strong> (Rotated)</div>
                    <div>• <strong>5 Tavily Keys</strong> (Rotated)</div>
                    <div>• <strong>3 Firecrawl Keys</strong></div>
                    <div>• <strong>Zero Token Outage</strong></div>
                  </div>
                </div>
                <div style="font-size: 11.5px; color: #EF4444; font-family: var(--font-mono); margin-top: 12px;">
                  Automated Rotation
                </div>
              </div>

            </div>

            <!-- Bottom: Multi-Key Failover Strategy Flow Diagram -->
            <div class="card-box" style="padding: 18px 24px; background: #0C0C10; display: flex; flex-direction: column;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <span style="font-size: 14.5px; font-weight: 700; color: #FFFFFF;">Zero-Downtime Multi-Key Failover Architecture</span>
                <span style="font-size: 12.5px; color: #A1A1AA;">Ensures uninterrupted hunts even during live science exhibition demos</span>
              </div>

              <svg viewBox="0 0 1700 50" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto;">
                <rect x="10" y="5" width="280" height="40" rx="6" fill="#14141A" stroke="#10B981"/>
                <text x="150" y="30" text-anchor="middle" fill="#FFFFFF" font-size="13" font-weight="700">Tavily Key 1 (Primary)</text>

                <path d="M 290 25 L 350 25" stroke="#EF4444" stroke-width="1.5"/>
                <text x="320" y="18" text-anchor="middle" fill="#EF4444" font-size="10">Rate Limit</text>

                <rect x="350" y="5" width="280" height="40" rx="6" fill="#14141A" stroke="#38BDF8"/>
                <text x="490" y="30" text-anchor="middle" fill="#FFFFFF" font-size="13" font-weight="700">Tavily Key 2..5 (Auto Rotate)</text>

                <path d="M 630 25 L 690 25" stroke="#EF4444" stroke-width="1.5"/>
                <text x="660" y="18" text-anchor="middle" fill="#EF4444" font-size="10">Exhausted</text>

                <rect x="690" y="5" width="280" height="40" rx="6" fill="#14141A" stroke="#F59E0B"/>
                <text x="830" y="30" text-anchor="middle" fill="#FFFFFF" font-size="13" font-weight="700">Firecrawl (3 Key Rotation)</text>

                <path d="M 970 25 L 1030 25" stroke="#F59E0B" stroke-width="1.5"/>
                <text x="1000" y="18" text-anchor="middle" fill="#F59E0B" font-size="10">Fallback</text>

                <rect x="1030" y="5" width="280" height="40" rx="6" fill="#14141A" stroke="#94A3B8"/>
                <text x="1170" y="30" text-anchor="middle" fill="#FFFFFF" font-size="13" font-weight="700">Jina Reader & Crawl4AI</text>

                <path d="M 1310 25 L 1370 25" stroke="#10B981" stroke-width="1.5"/>
                <text x="1340" y="18" text-anchor="middle" fill="#10B981" font-size="10">Offline</text>

                <rect x="1370" y="5" width="310" height="40" rx="6" fill="#0D1E16" stroke="#10B981" stroke-width="2"/>
                <text x="1525" y="30" text-anchor="middle" fill="#10B981" font-size="13" font-weight="800">Pre-Seeded Vector Cache</text>
              </svg>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">Engineering & Tech Stack</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">09 / 10</span>
          </div>
        </footer>
      </section>
    """


def get_slide_10():
    """Slide 10: Mission & Global Impact: Leveling the Global Playing Field"""
    return """
      <!-- SLIDE 10: MISSION & GLOBAL IMPACT -->
      <section class="slide" id="slide-10" data-index="10">
        <div class="pin-mark pin-tl"></div>
        <div class="pin-mark pin-tr"></div>
        <div class="pin-mark pin-bl"></div>
        <div class="pin-mark pin-br"></div>

        <header class="slide-header">
          <h1 class="slide-headline">Leveling the Global Playing Field for Pakistan</h1>
          <p class="slide-subheadline">Transforming international educational access from a privileged luxury into an open, sovereign, merit-based right for every Pakistani student.</p>
        </header>

        <div class="slide-canvas">
          <div style="display: flex; flex-direction: column; gap: 24px; height: 100%;">
            
            <!-- 4 Impact Metric Cards -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
              
              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-green" style="margin-bottom: 12px;">100% Free Forever</span>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">Zero Agent Fees</h2>
                  <p class="card-desc">
                    Eliminates exploitative educational middlemen who charge PKR 200,000+ for public information. Puts direct power into students' hands.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #10B981; font-weight: 700; border-top: 1px solid var(--border-muted); padding-top: 10px;">
                  Democratic Educational Access
                </div>
              </div>

              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-slate" style="margin-bottom: 12px;">Sovereignty</span>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">Local & Private AI</h2>
                  <p class="card-desc">
                    Runs on the student's local machine. Academic transcripts, CNIC data, and personal research statements remain completely private and secure.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #CBD5E1; font-weight: 700; border-top: 1px solid var(--border-muted); padding-top: 10px;">
                  100% Student Data Privacy
                </div>
              </div>

              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-blue" style="margin-bottom: 12px;">National Reach</span>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">Every Province</h2>
                  <p class="card-desc">
                    Reaching students in Gilgit-Baltistan, Balochistan, Khyber Pakhtunkhwa, Sindh, and Punjab who lack access to expensive consultancy centers.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #38BDF8; font-weight: 700; border-top: 1px solid var(--border-muted); padding-top: 10px;">
                  Equal Opportunity Everywhere
                </div>
              </div>

              <div class="card-box" style="padding: 26px; justify-content: space-between;">
                <div>
                  <span class="badge-tag badge-rose" style="margin-bottom: 12px;">Zero Hallucinations</span>
                  <h2 style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">Verified Truth</h2>
                  <p class="card-desc">
                    Adversarial cross-checking ensures students never waste non-refundable test and visa fees on expired or fake scholarship announcements.
                  </p>
                </div>
                <div style="font-size: 13.5px; color: #EF4444; font-weight: 700; border-top: 1px solid var(--border-muted); padding-top: 10px;">
                  Evidence-Backed Applications
                </div>
              </div>

            </div>

            <!-- Bottom: Authoritative Closing Callout -->
            <div class="card-box" style="padding: 26px 36px; background: #0C0C10; border: 1px solid var(--border-strong); display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
              <div style="max-width: 1200px;">
                <div style="font-size: 20px; font-weight: 800; color: #FFFFFF; line-height: 1.4; margin-bottom: 8px;">
                  "ScholarX does not merely search. It investigates. It verifies. It empowers."
                </div>
                <div style="font-size: 15px; color: #A1A1AA; line-height: 1.5;">
                  Built with pride for Pakistan's next generation of scientists, engineers, scholars, and innovators.
                </div>
              </div>

              <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
                <span class="badge-tag badge-green" style="font-size: 12px; padding: 6px 12px;">Science Exhibition 2026</span>
                <span style="font-size: 13px; color: #A1A1AA; font-family: var(--font-mono);">github.com/scholarx</span>
              </div>
            </div>

          </div>
        </div>

        <footer class="slide-footer">
          <div class="footer-left">
            <span class="footer-brand">ScholarX</span>
            <span class="footer-dot"></span>
            <span class="footer-topic">Our Mission & Global Vision</span>
          </div>
          <div class="footer-right">
            <span class="footer-num">10 / 10</span>
          </div>
        </footer>
      </section>
    """
