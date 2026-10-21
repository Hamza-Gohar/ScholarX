<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ScholarX — Autonomous Scholarship Intelligence</title>
  
  <!-- Authentic fonts matching the reference template -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <style>
    :root {
      --font-display: 'Anton', sans-serif;
      --font-sans: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --slide-w: 1920px;
      --slide-h: 1080px;
      --frame-border: 1px solid rgba(255, 255, 255, 0.4);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
    }

    html, body {
      width: 100%;
      height: 100%;
      background: #000000;
      color: #FFFFFF;
      font-family: var(--font-sans);
      overflow-x: hidden;
      overflow-y: hidden;
    }

    .font-display { font-family: var(--font-display); }
    .font-sans { font-family: var(--font-sans); }
    .font-mono { font-family: var(--font-mono); }

    /* TOP MINIMAL CONTROL BAR */
    .deck-toolbar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 48px;
      background: rgba(0, 0, 0, 0.95);
      border-bottom: 1px solid #1C1C24;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 1000;
    }

    .brand-title {
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: #FFFFFF;
    }

    .toolbar-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .nav-btn {
      background: #111116;
      color: #FFFFFF;
      border: 1px solid #272730;
      padding: 5px 14px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.15s, border-color 0.15s;
    }
    .nav-btn:hover {
      background: #1C1C24;
      border-color: #3F3F4E;
    }
    .nav-btn.primary {
      background: #FFFFFF;
      color: #000000;
      border-color: #FFFFFF;
      font-weight: 600;
    }
    .nav-btn.primary:hover {
      background: #E4E4E7;
    }

    .slide-counter {
      color: #A1A1AA;
      font-size: 13px;
      font-weight: 600;
      min-width: 75px;
      text-align: center;
      font-family: var(--font-mono);
    }

    /* VIEWPORT STAGE */
    .viewport-stage {
      margin-top: 48px;
      width: 100vw;
      height: calc(100vh - 48px);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    #presentation-deck {
      width: var(--slide-w);
      height: var(--slide-h);
      transform-origin: center center;
      position: relative;
    }

    /* SLIDE BASE STYLES WITH 3D SLATTED BACKGROUND */
    .slide {
      width: var(--slide-w);
      height: var(--slide-h);
      position: absolute;
      top: 0;
      left: 0;
      background-color: #050507;
      background-image: url('assets/black_minimalist_bg.jpg');
      background-size: cover;
      background-position: center center;
      display: none;
      padding: 48px;
      box-sizing: border-box;
      overflow: hidden;
    }

    .slide.active {
      display: block;
    }

    /* CONTINUOUS 1PX ARCHITECTURAL FRAME */
    .slide-frame {
      width: 100%;
      height: 100%;
      border: var(--frame-border);
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      position: relative;
      z-index: 5;
      overflow: hidden;
    }

    /* HARDBOARD CORNER PUSH-PIN CROSSHAIRS */
    .pin-mark {
      position: absolute;
      width: 20px;
      height: 20px;
      pointer-events: none;
      z-index: 10;
    }
    .pin-mark::before, .pin-mark::after {
      content: '';
      position: absolute;
      background: #52525B;
    }
    .pin-mark::before {
      top: 9px;
      left: 0;
      width: 20px;
      height: 2px;
    }
    .pin-mark::after {
      top: 0;
      left: 9px;
      width: 2px;
      height: 20px;
    }
    .pin-tl { top: 24px; left: 24px; }
    .pin-tr { top: 24px; right: 24px; }
    .pin-bl { bottom: 24px; left: 24px; }
    .pin-br { bottom: 24px; right: 24px; }

    /* COVER LAYOUT */
    .cover-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px 100px;
    }

    /* FRAME FOOTER */
    .frame-footer {
      border-top: var(--frame-border);
      min-height: 56px;
      padding: 16px 48px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 13px;
      color: #A1A1AA;
      background: rgba(0, 0, 0, 0.4);
      box-sizing: border-box;
    }

    /* SPLIT FRAME (Left anchor + Right content) */
    .split-frame {
      flex: 1;
      display: grid;
      min-height: 0;
    }

    .split-col-left {
      border-right: var(--frame-border);
      padding: 56px 48px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .split-col-right {
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-height: 0;
    }

    /* NUMBERED ITEM HEADER (01. Title) */
    .item-header {
      display: flex;
      align-items: baseline;
      gap: 14px;
      margin-bottom: 8px;
    }

    .num-prefix {
      font-family: var(--font-display);
      font-size: 44px;
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1;
    }

    .num-title {
      font-family: var(--font-display);
      font-size: 30px;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: 0.02em;
    }

    .item-desc {
      font-family: var(--font-sans);
      font-size: 17px;
      color: #D4D4D8;
      line-height: 1.6;
    }

    /* AGENDA ROW WITH 52x52 SOLID WHITE ICON BOX */
    .agenda-row {
      display: flex;
      align-items: center;
      gap: 26px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      padding-bottom: 22px;
    }
    .agenda-row:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }

    .white-box {
      width: 52px;
      height: 52px;
      background: #FFFFFF;
      color: #000000;
      border-radius: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .agenda-title {
      font-family: var(--font-display);
      font-size: 30px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 4px;
      letter-spacing: 0.02em;
    }

    .agenda-desc {
      font-family: var(--font-sans);
      font-size: 17px;
      color: #D4D4D8;
      line-height: 1.5;
    }

    /* TOP HEADER FRAME */
    .top-header-frame {
      padding: 44px 56px;
      border-bottom: var(--frame-border);
    }

    /* THREE COLUMN FRAME */
    .three-col-frame {
      flex: 1;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      padding: 48px 56px;
    }

    .col-box {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* TIMELINE STYLES */
    .timeline-circle {
      width: 48px;
      height: 48px;
      background: #000000;
      border: 2px solid #FFFFFF;
      color: #FFFFFF;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: 800;
      margin-bottom: 20px;
    }

    .bottom-stats-bar {
      border-top: var(--frame-border);
      padding: 24px 56px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* TECH CARD LIST */
    .tech-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      font-size: 17px;
      color: #D4D4D8;
    }

    /* CLEAN EXPORT MODE */
    body.export-mode .deck-toolbar {
      display: none !important;
    }
    body.export-mode .viewport-stage {
      margin-top: 0 !important;
      width: 1920px !important;
      height: 1080px !important;
      overflow: hidden !important;
    }
    body.export-mode #presentation-deck {
      transform: none !important;
      width: 1920px !important;
      height: 1080px !important;
    }

    /* PRINT STYLES */
    @page {
      size: 1920px 1080px landscape;
      margin: 0;
    }

    @media print {
      body {
        background: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .deck-toolbar {
        display: none !important;
      }
      .viewport-stage {
        margin-top: 0 !important;
        height: auto !important;
        width: 100% !important;
        display: block !important;
      }
      #presentation-deck {
        transform: none !important;
        width: 1920px !important;
        height: auto !important;
        display: block !important;
      }
      .slide {
        display: block !important;
        position: relative !important;
        width: 1920px !important;
        height: 1080px !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        break-after: page !important;
        break-inside: avoid !important;
        border: none !important;
        margin: 0 !important;
        padding: 48px !important;
        box-sizing: border-box !important;
      }
      .slide:last-child {
        page-break-after: auto !important;
        break-after: auto !important;
      }
    }
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

      <section class="slide active" id="slide-1" data-index="1">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="cover-body">
            <div style="max-width: 1300px;">
              <h1 class="font-display" style="font-size: 148px; line-height: 0.95; margin-bottom: 28px; color: #FFFFFF; letter-spacing: 0.01em;">
                ScholarX
              </h1>
              <div class="font-sans" style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin-bottom: 24px; letter-spacing: -0.01em;">
                Autonomous Scholarship Intelligence for Pakistani Students
              </div>
              <p class="font-sans" style="font-size: 21px; color: #D4D4D8; line-height: 1.6; max-width: 920px;">
                A multi-agent, fully autonomous system designed to discover, fact-check, and plan fully funded global scholarships abroad according to your profile and preferences.
              </p>
            </div>
          </div>

          <div class="frame-footer" style="justify-content: space-between; min-height: 96px; padding: 24px 48px;">
            <div class="font-mono" style="font-size: 14px; color: #A1A1AA; letter-spacing: 0.05em;">SCHOLARX &bull; SOVEREIGN AI</div>
            <div class="font-display" style="font-size: 36px; font-weight: 700; color: #FFFFFF; letter-spacing: 0.02em;">
              ScholarX
            </div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-2" data-index="2">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="split-frame" style="grid-template-columns: 460px 1fr;">
            
            <!-- Left Anchor Column -->
            <div class="split-col-left">
              <h2 class="font-sans" style="font-size: 76px; font-weight: 900; color: #FFFFFF; line-height: 1.0; margin: 0; letter-spacing: -0.02em;">
                Contents
              </h2>
              <div>
                <div class="font-display" style="font-size: 34px; font-weight: 700; color: #FFFFFF; margin-bottom: 14px; line-height: 1.2;">
                  What is an AI Agent?
                </div>
                <div class="font-sans" style="font-size: 17px; color: #A1A1AA; line-height: 1.6;">
                  An autonomous software entity equipped with reasoning, memory, tools, and goals that operates in an iterative loop.
                </div>
              </div>
            </div>

            <!-- Right Content: 6 Numbered Items in Anton & Outfit -->
            <div class="split-col-right" style="padding: 56px 64px;">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px 64px;">
                
                <div>
                  <div class="item-header">
                    <span class="num-prefix">01.</span>
                    <span class="num-title">Brain (LLM Core)</span>
                  </div>
                  <div class="item-desc">High-order reasoning, task decomposition, and strategic planning powered by Gemini.</div>
                </div>

                <div>
                  <div class="item-header">
                    <span class="num-prefix">02.</span>
                    <span class="num-title">Tool Execution</span>
                  </div>
                  <div class="item-desc">Directly invokes external tools: web search (Tavily), crawlers (Firecrawl), and PDF parsers.</div>
                </div>

                <div>
                  <div class="item-header">
                    <span class="num-prefix">03.</span>
                    <span class="num-title">Autonomous Agency</span>
                  </div>
                  <div class="item-desc">Operates independently toward an objective without requiring step-by-step human prompts.</div>
                </div>

                <div>
                  <div class="item-header">
                    <span class="num-prefix">04.</span>
                    <span class="num-title">Memory Systems</span>
                  </div>
                  <div class="item-desc">Retains working context for live tasks, plus persistent database storage across searches.</div>
                </div>

                <div>
                  <div class="item-header">
                    <span class="num-prefix">05.</span>
                    <span class="num-title">Iterative Loop</span>
                  </div>
                  <div class="item-desc">Cycles continuously: Perceive &rarr; Think &rarr; Act &rarr; Observe &rarr; Verify until the goal is met.</div>
                </div>

                <div>
                  <div class="item-header">
                    <span class="num-prefix">06.</span>
                    <span class="num-title">Goal-Oriented</span>
                  </div>
                  <div class="item-desc">Optimizes every step to find eligible, verified, fully funded scholarship matches.</div>
                </div>

              </div>
            </div>

          </div>

          <div class="frame-footer">
            <div>SCHOLARX</div>
            <div>02 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-3" data-index="3">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="split-frame" style="grid-template-columns: 460px 1fr;">
            
            <!-- Left Anchor Column -->
            <div class="split-col-left">
              <h2 class="font-display" style="font-size: 84px; font-weight: 700; color: #FFFFFF; line-height: 1.0; margin: 0; letter-spacing: 0.01em;">
                Agenda
              </h2>
              <div>
                <div class="font-display" style="font-size: 34px; font-weight: 700; color: #FFFFFF; margin-bottom: 14px; line-height: 1.2;">
                  Multi-Agent Systems
                </div>
                <div class="font-sans" style="font-size: 17px; color: #A1A1AA; line-height: 1.6;">
                  How specialized agents collaborate, challenge each other, and achieve the overarching scholarship agenda.
                </div>
              </div>
            </div>

            <!-- Right Content: Agenda Stack with 52x52px Solid White Icon Boxes -->
            <div class="split-col-right" style="padding: 56px 64px; gap: 26px;">
              
              <div class="agenda-row">
                <div class="white-box">
                  <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#000000" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                    <circle cx="9" cy="7" r="4"/>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                  </svg>
                </div>
                <div>
                  <div class="agenda-title">Specialized Division of Labor</div>
                  <div class="agenda-desc">Each agent masters one domain: Scouts discover, Eligibility Checkers audit, and Skeptics stress-test.</div>
                </div>
              </div>

              <div class="agenda-row">
                <div class="white-box">
                  <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#000000" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="2" width="6" height="6" rx="1"/>
                    <rect x="16" y="2" width="6" height="6" rx="1"/>
                    <rect x="9" y="16" width="6" height="6" rx="1"/>
                    <path d="M5 8v3a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8"/>
                    <path d="M12 13v3"/>
                  </svg>
                </div>
                <div>
                  <div class="agenda-title">Shared State & Event Bus</div>
                  <div class="agenda-desc">Asynchronous pub/sub communication via Redis and LangGraph channels maintains system synchronization.</div>
                </div>
              </div>

              <div class="agenda-row">
                <div class="white-box">
                  <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#000000" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <path d="m9 12 2 2 4-4"/>
                  </svg>
                </div>
                <div>
                  <div class="agenda-title">Adversarial Debate & Cross-Checking</div>
                  <div class="agenda-desc">The Skeptic agent actively attempts to invalidate claims, requiring primary official proof for approval.</div>
                </div>
              </div>

              <div class="agenda-row">
                <div class="white-box">
                  <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#000000" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <circle cx="12" cy="12" r="6"/>
                    <circle cx="12" cy="12" r="2"/>
                  </svg>
                </div>
                <div>
                  <div class="agenda-title">Collective Agenda Convergence</div>
                  <div class="agenda-desc">All agent discoveries converge into a ranked, verified, fraud-free scholarship roadmap for the student.</div>
                </div>
              </div>

            </div>

          </div>

          <div class="frame-footer">
            <div>SCHOLARX</div>
            <div>03 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-4" data-index="4">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <!-- Top Box Header -->
          <div class="top-header-frame">
            <h2 class="font-display" style="font-size: 60px; font-weight: 700; color: #FFFFFF; letter-spacing: 0.02em; margin: 0 0 8px 0;">
              SECTION BREAK: WORKFLOWS VS. AGENTS
            </h2>
            <div class="font-sans" style="font-size: 20px; color: #D4D4D8;">
              Deterministic code meets probabilistic AI reasoning. Why ScholarX strictly requires both.
            </div>
          </div>

          <!-- 3 Columns Separated by Hairline Borders -->
          <div class="three-col-frame">
            
            <div class="col-box" style="border-right: 1px solid rgba(255, 255, 255, 0.4); padding-right: 48px;">
              <div>
                <div class="item-header" style="margin-bottom: 12px;">
                  <span class="num-prefix" style="font-size: 52px;">01.</span>
                  <span class="num-title" style="font-size: 30px;">Deterministic Code</span>
                </div>
                <p class="item-desc" style="font-size: 17px; line-height: 1.65;">
                  100% predictable with zero hallucination. Computes the 15 eligibility hard gates, currency conversion (PKR), and deadlines on the CPU with instant execution.
                </p>
              </div>
              <div class="font-sans" style="font-size: 15px; color: #FFFFFF; font-weight: 700; letter-spacing: 0.03em;">
                RULES, MATH & DEADLINES
              </div>
            </div>

            <div class="col-box" style="border-right: 1px solid rgba(255, 255, 255, 0.4); padding: 0 48px;">
              <div>
                <div class="item-header" style="margin-bottom: 12px;">
                  <span class="num-prefix" style="font-size: 52px;">02.</span>
                  <span class="num-title" style="font-size: 30px;">Probabilistic Agents</span>
                </div>
                <p class="item-desc" style="font-size: 17px; line-height: 1.65;">
                  Natural comprehension and adaptive search. Understands complex student CVs, discovers live opportunities, and challenges suspicious claims with LLM reasoning.
                </p>
              </div>
              <div class="font-sans" style="font-size: 15px; color: #FFFFFF; font-weight: 700; letter-spacing: 0.03em;">
                EXTRACTION & SKEPTIC AUDIT
              </div>
            </div>

            <div class="col-box" style="padding-left: 48px;">
              <div>
                <div class="item-header" style="margin-bottom: 12px;">
                  <span class="num-prefix" style="font-size: 52px;">03.</span>
                  <span class="num-title" style="font-size: 30px;">The ScholarX Law</span>
                </div>
                <p class="item-desc" style="font-size: 17px; line-height: 1.65;">
                  Deterministic workflows strictly guardrail AI agents. No LLM is ever allowed to guess a deadline or calculate PKR costs. Zero token hallucination on critical data.
                </p>
              </div>
              <div class="font-sans" style="font-size: 15px; color: #FFFFFF; font-weight: 700; letter-spacing: 0.03em;">
                ARCHITECTURAL GUARANTEE
              </div>
            </div>

          </div>

          <div class="frame-footer" style="justify-content: space-between;">
            <div>HYBRID DESIGN: LANGGRAPH STATE MACHINE + GEMINI REASONING</div>
            <div>04 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-5" data-index="5">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="split-frame" style="grid-template-columns: 520px 1fr;">
            
            <!-- Left: Problem Description -->
            <div class="split-col-left" style="padding: 56px 48px; justify-content: flex-start;">
              <div>
                <h2 class="font-display" style="font-size: 76px; font-weight: 700; color: #FFFFFF; line-height: 1.0; margin: 0 0 16px 0;">
                  The Problem
                </h2>
                <div class="font-sans" style="font-size: 19px; color: #D4D4D8; line-height: 1.55; margin-bottom: 28px;">
                  Every year, thousands of fully funded international seats reserved for Pakistan expire empty while families face opaque bureaucracy.
                </div>
              </div>

              <!-- Horizontal hairline divider matching media_1791620282203.png -->
              <div style="width: 100%; height: 1px; background: rgba(255, 255, 255, 0.4); margin-bottom: 28px;"></div>

              <div>
                <div class="font-display" style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin-bottom: 18px;">
                  Why Scholarships Go Unclaimed
                </div>

                <div style="display: flex; flex-direction: column; gap: 16px; font-size: 16px; color: #D4D4D8; margin-bottom: 28px;" class="font-sans">
                  <div>&bull; <strong style="color:#FFF;">Hidden Quotas:</strong> 40%+ of bilateral seats (Hungary, China CSC, Turkiye) expire unawares.</div>
                  <div>&bull; <strong style="color:#FFF;">Cost Shock:</strong> Surprise upfront PKR 150K+ fees for IELTS, visa, and legal stamps.</div>
                  <div>&bull; <strong style="color:#FFF;">Predatory Agents:</strong> Extorting PKR 150K–300K merely to file free public forms.</div>
                </div>

                <div class="font-sans" style="font-size: 15px; color: #FFFFFF; font-weight: 600;">
                  ScholarX is 100% free forever for every Pakistani student.
                </div>
              </div>
            </div>

            <!-- Right: Editorial Black & White Documentary Photograph (Pakistani Boy Student) -->
            <div style="padding: 40px; display: flex; align-items: center; justify-content: center;">
              <div style="width: 100%; height: 100%; position: relative; border: 1px solid rgba(255, 255, 255, 0.4); overflow: hidden; background: #08080C;">
                <img src="assets/pakistan_male_student_research.jpg" alt="Pakistani male student reviewing scholarship documents late at night" style="width: 100%; height: 100%; object-fit: cover; display: block; filter: contrast(1.05) brightness(0.95);"/>
                <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.92) 0%, transparent 100%); padding: 26px 32px;">
                  <div class="font-display" style="font-size: 28px; color: #FFFFFF; margin-bottom: 6px;">The Paperwork Maze</div>
                  <div class="font-sans" style="font-size: 15px; color: #D4D4D8;">HEC HAT tests, IBCC equivalencies, and MOFA legal queues disqualify eligible candidates.</div>
                </div>
              </div>
            </div>

          </div>

          <div class="frame-footer">
            <div>SCHOLARX</div>
            <div>05 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-6" data-index="6">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="top-header-frame">
            <h2 class="font-display" style="font-size: 54px; font-weight: 700; color: #FFFFFF; letter-spacing: 0.01em; margin: 0 0 6px 0;">
              SYSTEM FLOWCHART: ALL AGENTS & WORKFLOWS
            </h2>
            <div class="font-sans" style="font-size: 19px; color: #D4D4D8;">
              5 autonomous AI agents and 7 deterministic workflows orchestrated in one unified field.
            </div>
          </div>

          <!-- Flowchart Field -->
          <div style="flex: 1; padding: 20px 48px; display: flex; flex-direction: column; justify-content: center;">
            <svg viewBox="0 0 1200 480" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; max-height: 480px;">
              
              <!-- 1. Input -->
              <rect x="340" y="8" width="520" height="56" rx="2" fill="#14141E" stroke="#FFFFFF" stroke-width="1.4"/>
              <text x="600" y="30" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="12" font-weight="700">1. STUDENT INPUT LAYER</text>
              <text x="600" y="50" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="15.5" font-weight="700">CV, Transcripts, GPA, Preferences & PKR Budget</text>

              <path d="M 600 64 L 600 90" stroke="#FFFFFF" stroke-width="1.4"/>
              <polygon points="596,90 600,97 604,90" fill="#FFFFFF"/>

              <!-- 2. Intake Agents -->
              <rect x="160" y="98" width="280" height="64" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.7)" stroke-width="1.2"/>
              <text x="300" y="122" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[AGENT] PROFILE ANALYST</text>
              <text x="300" y="145" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Extracts GPA & Credentials</text>

              <rect x="460" y="98" width="280" height="64" rx="2" fill="#181824" stroke="#FFFFFF" stroke-width="1.8"/>
              <text x="600" y="122" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[AGENT] ORCHESTRATOR</text>
              <text x="600" y="145" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="14" font-weight="700">Controls Routing & State</text>

              <rect x="760" y="98" width="280" height="64" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.7)" stroke-width="1.2"/>
              <text x="900" y="122" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[AGENT] DOCUMENT ANALYST</text>
              <text x="900" y="145" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Checks Document Readiness</text>

              <path d="M 440 130 L 460 130" stroke="rgba(255,255,255,0.4)" stroke-width="1.2"/>
              <path d="M 740 130 L 760 130" stroke="rgba(255,255,255,0.4)" stroke-width="1.2"/>

              <path d="M 600 162 L 600 186" stroke="#FFFFFF" stroke-width="1.4"/>
              <polygon points="596,186 600,193 604,186" fill="#FFFFFF"/>

              <!-- 3. Regional Discovery Scouts -->
              <rect x="80" y="192" width="245" height="62" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.5)" stroke-width="1.2"/>
              <text x="202" y="216" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] EUROPE SCOUT</text>
              <text x="202" y="238" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">DAAD, Hungary, Erasmus</text>

              <rect x="345" y="192" width="245" height="62" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.5)" stroke-width="1.2"/>
              <text x="467" y="216" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] ASIA SCOUT</text>
              <text x="467" y="238" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">China CSC, Turkiye, MEXT</text>

              <rect x="610" y="192" width="245" height="62" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.5)" stroke-width="1.2"/>
              <text x="732" y="216" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] AMERICAS SCOUT</text>
              <text x="732" y="238" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Fulbright & Canadian Seats</text>

              <rect x="875" y="192" width="245" height="62" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.5)" stroke-width="1.2"/>
              <text x="997" y="216" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] MENA SCOUT</text>
              <text x="997" y="238" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">KAUST, Qatar & Global</text>

              <path d="M 600 254 L 600 278" stroke="#FFFFFF" stroke-width="1.4"/>
              <polygon points="596,278 600,285 604,278" fill="#FFFFFF"/>

              <!-- 4. Deterministic Guardrails -->
              <rect x="160" y="286" width="280" height="64" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.6)" stroke-width="1.2"/>
              <text x="300" y="310" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] ELIGIBILITY CHECK</text>
              <text x="300" y="333" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">15 Hard Criteria Gates</text>

              <rect x="460" y="286" width="280" height="64" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.6)" stroke-width="1.2"/>
              <text x="600" y="310" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] TRUE COST MATH</text>
              <text x="600" y="333" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Calculates Exact PKR Needs</text>

              <rect x="760" y="286" width="280" height="64" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.6)" stroke-width="1.2"/>
              <text x="900" y="310" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[WORKFLOW] DEADLINE MATH</text>
              <text x="900" y="333" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Timeline & Buffer Days</text>

              <path d="M 440 318 L 460 318" stroke="rgba(255,255,255,0.4)" stroke-width="1.2"/>
              <path d="M 740 318 L 760 318" stroke="rgba(255,255,255,0.4)" stroke-width="1.2"/>

              <path d="M 600 350 L 600 374" stroke="#FFFFFF" stroke-width="1.4"/>
              <polygon points="596,374 600,381 604,374" fill="#FFFFFF"/>

              <!-- 5. Adversarial Audit & Deliverable -->
              <rect x="180" y="380" width="240" height="64" rx="2" fill="#0A0A10" stroke="rgba(255,255,255,0.8)" stroke-width="1.2"/>
              <text x="300" y="404" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[AGENT] VERIFICATION</text>
              <text x="300" y="427" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Official Portal Check</text>

              <path d="M 420 412 L 490 412" stroke="#FFFFFF" stroke-width="1.6"/>
              <polygon points="425,408 415,412 425,416" fill="#FFFFFF"/>
              <polygon points="485,408 495,412 485,416" fill="#FFFFFF"/>

              <rect x="495" y="380" width="240" height="64" rx="2" fill="#0A0A10" stroke="#FFFFFF" stroke-width="1.6"/>
              <text x="615" y="404" text-anchor="middle" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-size="12" font-weight="800">[AGENT] SKEPTIC (AUDIT)</text>
              <text x="615" y="427" text-anchor="middle" fill="#A1A1AA" font-family="'Outfit', sans-serif" font-size="14">Disproves Fake Claims</text>

              <path d="M 735 412 L 775 412" stroke="#FFFFFF" stroke-width="1.6"/>
              <polygon points="770,408 778,412 770,416" fill="#FFFFFF"/>

              <rect x="778" y="380" width="345" height="64" rx="2" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.6"/>
              <text x="950" y="404" text-anchor="middle" fill="#000000" font-family="'Outfit', sans-serif" font-size="12" font-weight="900">[FINAL DELIVERABLE]</text>
              <text x="950" y="427" text-anchor="middle" fill="#000000" font-family="'Outfit', sans-serif" font-size="15.5" font-weight="800">Verified Application Roadmap</text>
            </svg>
          </div>

          <div class="frame-footer" style="justify-content: space-between;">
            <div>AI AGENTS (5): REASONING & VERIFICATION &bull; WORKFLOWS (7): DETERMINISTIC MATH GATES</div>
            <div>06 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-7" data-index="7">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="top-header-frame">
            <h2 class="font-display" style="font-size: 54px; font-weight: 700; color: #FFFFFF; letter-spacing: 0.01em; margin: 0 0 6px 0;">
              THE STUDENT JOURNEY IN 4 STEPS
            </h2>
            <div class="font-sans" style="font-size: 19px; color: #D4D4D8;">
              From uploading your CV to getting a verified application roadmap in under 2 minutes.
            </div>
          </div>

          <!-- Horizontal Timeline -->
          <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 0 48px;">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; position: relative;">
              
              <!-- Timeline Horizontal Connector Line -->
              <div style="position: absolute; top: 24px; left: 60px; right: 60px; height: 1.5px; background: rgba(255,255,255,0.3); z-index: 1;"></div>

              <!-- Step 01 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle font-sans">01</div>
                <div class="font-display" style="font-size: 30px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Profile Intake</div>
                <div class="font-sans" style="font-size: 14px; color: #FFFFFF; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.04em;">2 MINUTES</div>
                <p class="font-sans" style="font-size: 16.5px; color: #D4D4D8; line-height: 1.6;">
                  Upload your CV or transcript. The AI parses GPA, degree type, publications, and test scores without tedious forms.
                </p>
              </div>

              <!-- Step 02 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle font-sans">02</div>
                <div class="font-display" style="font-size: 30px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Global Scan</div>
                <div class="font-sans" style="font-size: 14px; color: #FFFFFF; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.04em;">AUTONOMOUS</div>
                <p class="font-sans" style="font-size: 16.5px; color: #D4D4D8; line-height: 1.6;">
                  4 regional scouts crawl official government databases across Europe, Asia, Americas, and MENA in parallel.
                </p>
              </div>

              <!-- Step 03 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle font-sans">03</div>
                <div class="font-display" style="font-size: 30px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Fact-Checking</div>
                <div class="font-sans" style="font-size: 14px; color: #FFFFFF; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.04em;">STRICT AUDIT</div>
                <p class="font-sans" style="font-size: 16.5px; color: #D4D4D8; line-height: 1.6;">
                  Filters through 15 qualification gates, calculates true PKR expenses, and challenges claims with the Skeptic Agent.
                </p>
              </div>

              <!-- Step 04 -->
              <div style="position: relative; z-index: 2;">
                <div class="timeline-circle font-sans">04</div>
                <div class="font-display" style="font-size: 30px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Action Roadmap</div>
                <div class="font-sans" style="font-size: 14px; color: #FFFFFF; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.04em;">READY TO APPLY</div>
                <p class="font-sans" style="font-size: 16.5px; color: #D4D4D8; line-height: 1.6;">
                  Get a ranked dossier with verified portal links, required HEC/IBCC steps, and dynamic deadline reminders.
                </p>
              </div>

            </div>
          </div>

          <!-- Bottom Stats Bar -->
          <div class="bottom-stats-bar">
            <div style="display: flex; gap: 64px;">
              <div>
                <div class="font-display" style="font-size: 42px; font-weight: 700; color: #FFFFFF;">~90s</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA;">Average Hunt Duration</div>
              </div>
              <div>
                <div class="font-display" style="font-size: 42px; font-weight: 700; color: #FFFFFF;">15 Gates</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA;">Strict Rule Checks</div>
              </div>
              <div>
                <div class="font-display" style="font-size: 42px; font-weight: 700; color: #FFFFFF;">PKR 0</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA;">Total Cost to Student</div>
              </div>
            </div>

            <div class="font-sans" style="font-size: 15.5px; color: #A1A1AA;">
              Direct official government links only. No sponsored or affiliate redirects.
            </div>
          </div>

          <div class="frame-footer">
            <div>SCHOLARX</div>
            <div>07 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-8" data-index="8">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="split-frame" style="grid-template-columns: 1fr 1fr;">
            
            <!-- Left: Sovereign Features & Cash Table -->
            <div class="split-col-left" style="padding: 56px 48px;">
              <div>
                <h2 class="font-display" style="font-size: 72px; font-weight: 700; color: #FFFFFF; line-height: 1.0; margin: 0 0 16px 0;">
                  Built for Pakistan
                </h2>
                <div class="font-sans" style="font-size: 18px; color: #D4D4D8; line-height: 1.55; margin-bottom: 24px;">
                  Engineered specifically around Pakistani academic credentials and real pre-departure cash realities.
                </div>

                <!-- Minimalist Table -->
                <div style="border: 1px solid rgba(255, 255, 255, 0.4); background: #08080C; margin-bottom: 20px;">
                  <div class="font-sans" style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 14px 20px; background: rgba(255,255,255,0.08); font-size: 13px; font-weight: 800; color: #A1A1AA; letter-spacing: 0.02em;">
                    <div>MANDATORY PRE-DEPARTURE EXPENSE</div>
                    <div>TYPICAL COST (PKR)</div>
                  </div>

                  <div class="font-sans" style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 14px 20px; border-top: 1px solid rgba(255, 255, 255, 0.2); font-size: 16px; color: #FFFFFF;">
                    <div>IELTS / TOEFL Exam</div>
                    <div style="font-weight: 700;">PKR 75,600 – 76,240</div>
                  </div>

                  <div class="font-sans" style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 14px 20px; border-top: 1px solid rgba(255, 255, 255, 0.2); font-size: 16px; color: #FFFFFF;">
                    <div>HEC & IBCC Attestations</div>
                    <div style="font-weight: 700;">PKR 12,000 – 18,000</div>
                  </div>

                  <div class="font-sans" style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 14px 20px; border-top: 1px solid rgba(255, 255, 255, 0.2); font-size: 16px; color: #FFFFFF;">
                    <div>Embassy Visa & Biometrics</div>
                    <div style="font-weight: 700;">PKR 28,000 – 45,000</div>
                  </div>

                  <div class="font-sans" style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 14px 20px; border-top: 1px solid rgba(255, 255, 255, 0.2); font-size: 16px; color: #FFFFFF;">
                    <div>Medical Exam (Approved Clinic)</div>
                    <div style="font-weight: 700;">PKR 22,000 – 35,000</div>
                  </div>

                  <div class="font-sans" style="display: grid; grid-template-columns: 2fr 1.2fr; padding: 16px 20px; border-top: 2px solid rgba(255, 255, 255, 0.4); background: rgba(255,255,255,0.06); font-size: 16.5px; font-weight: 900; color: #FFFFFF;">
                    <div>Total Readiness Budget:</div>
                    <div style="color: #FFFFFF;">PKR 137K – 174K</div>
                  </div>
                </div>
              </div>

              <div class="font-sans" style="font-size: 15px; color: #A1A1AA;">
                <strong style="color: #FFFFFF;">Financial Honesty:</strong> ScholarX factors upfront cash needs into match ranking so students are never blindsided.
              </div>
            </div>

            <!-- Right: Editorial Student Success Image (Pakistani Boy Student) -->
            <div style="padding: 40px; display: flex; align-items: center; justify-content: center;">
              <div style="width: 100%; height: 100%; position: relative; border: 1px solid rgba(255, 255, 255, 0.4); overflow: hidden; background: #08080C;">
                <img src="assets/pakistan_male_student_success.jpg" alt="Pakistani boy student scholarship winner on global campus quadrangle" style="width: 100%; height: 100%; object-fit: cover; display: block; filter: contrast(1.05) brightness(0.95);"/>
                <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.92) 0%, transparent 100%); padding: 26px 32px;">
                  <div class="font-display" style="font-size: 28px; color: #FFFFFF; margin-bottom: 6px;">Direct Bilateral Quotas</div>
                  <div class="font-sans" style="font-size: 15px; color: #D4D4D8;">Dedicated sovereign quotas: 400+ Hungary seats, 200+ China CSC, Turkiye Burslari.</div>
                </div>
              </div>
            </div>

          </div>

          <div class="frame-footer">
            <div>SCHOLARX</div>
            <div>08 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-9" data-index="9">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <div class="top-header-frame">
            <h2 class="font-display" style="font-size: 54px; font-weight: 700; color: #FFFFFF; letter-spacing: 0.01em; margin: 0 0 6px 0;">
              COMPLETE TECH STACK & ARCHITECTURE
            </h2>
            <div class="font-sans" style="font-size: 19px; color: #D4D4D8;">
              Production-grade local architecture combining state-of-the-art Python orchestration and modern Next.js.
            </div>
          </div>

          <!-- 4 Equal Columns Divided by 1px Hairlines -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); flex: 1;">
            
            <div class="col-box" style="border-right: 1px solid rgba(255, 255, 255, 0.4); padding: 48px 36px;">
              <div>
                <h3 class="font-display" style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin: 0 0 18px 0;">Frontend (UI)</h3>
                <div class="tech-list font-sans">
                  <div>&bull; Next.js 15 (App Router)</div>
                  <div>&bull; React 19 & TypeScript</div>
                  <div>&bull; Tailwind CSS v4</div>
                  <div>&bull; Framer Motion</div>
                  <div>&bull; @xyflow/react (Graph)</div>
                </div>
              </div>
              <div class="font-mono" style="font-size: 14px; color: #FFFFFF; font-weight: 600;">PORT 3000</div>
            </div>

            <div class="col-box" style="border-right: 1px solid rgba(255, 255, 255, 0.4); padding: 48px 36px;">
              <div>
                <h3 class="font-display" style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin: 0 0 18px 0;">Backend Core</h3>
                <div class="tech-list font-sans">
                  <div>&bull; Python 3.12+</div>
                  <div>&bull; FastAPI (Async ASGI)</div>
                  <div>&bull; LangGraph State Machine</div>
                  <div>&bull; LangChain Core</div>
                  <div>&bull; Pydantic v2 (Validation)</div>
                </div>
              </div>
              <div class="font-mono" style="font-size: 14px; color: #FFFFFF; font-weight: 600;">PORT 8000</div>
            </div>

            <div class="col-box" style="border-right: 1px solid rgba(255, 255, 255, 0.4); padding: 48px 36px;">
              <div>
                <h3 class="font-display" style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin: 0 0 18px 0;">Parsers & DB</h3>
                <div class="tech-list font-sans">
                  <div>&bull; PyMuPDF & pdfplumber</div>
                  <div>&bull; Tavily & Firecrawl APIs</div>
                  <div>&bull; PostgreSQL + pgvector</div>
                  <div>&bull; Redis 7 Pub/Sub</div>
                  <div>&bull; SQLite Session Store</div>
                </div>
              </div>
              <div class="font-mono" style="font-size: 14px; color: #FFFFFF; font-weight: 600;">LOCAL DOCKER</div>
            </div>

            <div class="col-box" style="padding: 48px 36px;">
              <div>
                <h3 class="font-display" style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin: 0 0 18px 0;">LLMs & Failover</h3>
                <div class="tech-list font-sans">
                  <div>&bull; Gemini 3.7 Flash (Primary)</div>
                  <div>&bull; Gemini 3.0 Flash (Fallback)</div>
                  <div>&bull; Groq gpt-oss-120b</div>
                  <div>&bull; Multi-Key Key Rotation</div>
                  <div>&bull; Zero Outage Guarantee</div>
                </div>
              </div>
              <div class="font-mono" style="font-size: 14px; color: #FFFFFF; font-weight: 600;">AUTO-ROTATING</div>
            </div>

          </div>

          <div class="frame-footer" style="justify-content: space-between;">
            <div>RESILIENT MULTI-KEY FAILOVER: AUTOMATIC KEY ROTATION PREVENTS DISRUPTIONS</div>
            <div>09 / 10</div>
          </div>
        </div>
      </section>


      <section class="slide" id="slide-10" data-index="10">
        
  <div class="pin-mark pin-tl"></div>
  <div class="pin-mark pin-tr"></div>
  <div class="pin-mark pin-bl"></div>
  <div class="pin-mark pin-br"></div>

        <div class="slide-frame">
          <!-- Big Statistics Row -->
          <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.4); padding: 44px 56px;">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; text-align: center;">
              
              <div>
                <div class="font-display" style="font-size: 92px; font-weight: 700; color: #FFFFFF; line-height: 1;">100%</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA; font-weight: 800; margin-top: 10px; letter-spacing: 0.04em;">FREE FOR ALL STUDENTS</div>
              </div>

              <div>
                <div class="font-display" style="font-size: 92px; font-weight: 700; color: #FFFFFF; line-height: 1;">400+</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA; font-weight: 800; margin-top: 10px; letter-spacing: 0.04em;">BILATERAL SEATS TRACKED</div>
              </div>

              <div>
                <div class="font-display" style="font-size: 92px; font-weight: 700; color: #FFFFFF; line-height: 1;">15/15</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA; font-weight: 800; margin-top: 10px; letter-spacing: 0.04em;">ELIGIBILITY GATES CHECKED</div>
              </div>

              <div>
                <div class="font-display" style="font-size: 92px; font-weight: 700; color: #FFFFFF; line-height: 1;">PKR 0</div>
                <div class="font-sans" style="font-size: 14px; color: #A1A1AA; font-weight: 800; margin-top: 10px; letter-spacing: 0.04em;">CONSULTANT COMMISSIONS</div>
              </div>

            </div>
          </div>

          <!-- Bottom Impact Dual Column -->
          <div style="flex: 1; display: grid; grid-template-columns: 1.2fr 1fr;">
            
            <div style="border-right: 1px solid rgba(255, 255, 255, 0.4); padding: 56px 48px; display: flex; flex-direction: column; justify-content: center;">
              <div class="font-display" style="font-size: 46px; font-weight: 700; color: #FFFFFF; line-height: 1.35; margin-bottom: 22px;">
                "A student's talent—not their wealth or connections—should determine their future."
              </div>
              <div class="font-sans" style="font-size: 17px; color: #A1A1AA; font-weight: 600;">
                ScholarX &bull; Science Exhibition 2026 &bull; Sovereign AI built with pride for Pakistan.
              </div>
            </div>

            <div style="padding: 56px 48px; display: flex; flex-direction: column; justify-content: center; gap: 20px;">
              <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.2); padding-bottom: 16px;">
                <div class="font-display" style="font-size: 26px; color: #FFFFFF; margin-bottom: 6px;">Autonomous Multi-Agent Intelligence</div>
                <div class="font-sans" style="font-size: 15.5px; color: #A1A1AA;">5 specialized AI agents + 7 deterministic Python workflows working in harmony.</div>
              </div>

              <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.2); padding-bottom: 16px;">
                <div class="font-display" style="font-size: 26px; color: #FFFFFF; margin-bottom: 6px;">Skeptical Proof Architecture</div>
                <div class="font-sans" style="font-size: 15.5px; color: #A1A1AA;">Every deadline and requirement audited against primary embassy portals.</div>
              </div>

              <div>
                <div class="font-display" style="font-size: 26px; color: #FFFFFF; margin-bottom: 6px;">Locally Deployable Stack</div>
                <div class="font-sans" style="font-size: 15.5px; color: #A1A1AA;">FastAPI backend, Next.js frontend, and persistent Redis/SQLite state.</div>
              </div>
            </div>

          </div>

          <div class="frame-footer">
            <div>ScholarX</div>
            <div>10 / 10</div>
          </div>
        </div>
      </section>

    </div>
  </main>

  <!-- NAVIGATION SCRIPT -->
  <script>
    let currentSlide = 1;
    const totalSlides = 10;
    const deck = document.getElementById('presentation-deck');
    const currNum = document.getElementById('curr-num');

    function fitDeck() {
      const availW = window.innerWidth;
      const availH = window.innerHeight - 48;
      const scale = Math.min(availW / 1920, availH / 1080);
      deck.style.transform = `scale(${scale})`;
    }

    window.addEventListener('resize', fitDeck);
    fitDeck();

    const urlParams = new URLSearchParams(window.location.search);
    const hash = window.location.hash;
    if (urlParams.get('export') === '1' || urlParams.get('clean') === '1') {
      document.body.classList.add('export-mode');
    }
    if (urlParams.get('slide')) {
      showSlide(parseInt(urlParams.get('slide')));
    } else if (hash && hash.startsWith('#slide-')) {
      showSlide(parseInt(hash.replace('#slide-', '')));
    }

    function showSlide(index) {
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;

      for (let i = 1; i <= totalSlides; i++) {
        const slide = document.getElementById('slide-' + i);
        if (slide) {
          if (i === index) {
            slide.classList.add('active');
          } else {
            slide.classList.remove('active');
          }
        }
      }
      currentSlide = index;
      currNum.textContent = index;
    }

    function nextSlide() {
      if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
      }
    }

    function prevSlide() {
      if (currentSlide > 1) {
        showSlide(currentSlide - 1);
      }
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {});
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullscreen();
      } else if (e.key === 'p' || e.key === 'P') {
        window.print();
      }
    });
  </script>
</body>
</html>
