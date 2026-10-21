# SCHOLARX
# NEW FRONTEND DESIGN GUIDE
## AI COMMAND THEATRE + MOTION SYSTEM + EXHIBITION BUILD SPECIFICATION

**Document purpose:** This is the master frontend design specification for recreating ScholarX from the existing repository.

**Implementation model:** Build exactly one phase at a time. Do not begin the next phase until the current phase passes its hard gate.

**Primary audience:** A judge standing several meters away from a large 1920x1080 or larger display.

**Primary product statement:** ScholarX is a visible autonomous intelligence organization. The interface must show the organization working, not merely show a dashboard reporting that work happened.

---

# 0. SOURCE OF TRUTH AND DESIGN CONTRACT

## 0.1 Authoritative project documents

The coding agent must understand the current project before touching the frontend.

Read these files in this order:

1. `/Agents.md`
2. `/docs/ARCHITECTURE.md`
3. `/docs/DECISIONS.md`
4. `/docs/Design_Guide.md`
5. `/docs/KNOWN_ISSUES.md`
6. `/docs/STATUS.md`
7. `/docs/FRONTEND_IMPLEMENTATION_PLAN.md`, when present

The existing `Agents.md` defines ScholarX as an autonomous scholarship intelligence network for Pakistani students, with a central Orchestrator, a Discovery Commander, regional scout workflows, deterministic analysis workflows, Verification, Skeptic, Synthesis, Ranking, and Final Advisor responsibilities. It also defines a local event system that publishes agent/workflow events through Redis and exposes them to the frontend through SSE. The regional scouts use a deterministic `search -> scrape -> extract -> normalize -> return` flow. This visual guide must represent that architecture truthfully.

## 0.2 What this document controls

This document controls:

- frontend composition
- visual hierarchy
- card design
- world stage
- agent lifecycle visuals
- communication visuals
- map motion
- animation timing
- presentation pacing
- attention management
- research visualization
- verification visualization
- dossier assembly
- PDF experience
- exhibition mode
- debug mode
- quality gates

## 0.3 What this document does NOT authorize

This document does not authorize the frontend to redefine backend business logic.

Do not change:

- eligibility rules
- ranking formula
- scholarship data schema
- event semantics
- agent/workflow responsibilities
- source verification policy
- persistence semantics

unless a separate architecture decision is made and documented.

## 0.4 The most important rule

> **Preserve the intelligence system. Rebuild the presentation system.**

The existing frontend may contain useful API code, type definitions, SSE utilities, data adapters, or reusable primitives. Reuse them when useful. Do not preserve a visual layout merely because it already exists.

---

# 1. WHY WE ARE REBUILDING THE FRONTEND

## 1.1 The previous failure pattern

Several iterations converged on a conventional enterprise dashboard.

Symptoms included:

- three-column layout
- permanent scout cards
- telemetry sidebar
- tiny world map
- metric counters
- bottom pipeline rail
- excessive labels
- several accent colors competing for attention
- small text
- developer test controls visible in exhibition mode
- static cards that behaved like analytics widgets
- fake or weak communication animations
- no clear Commander -> Agent -> Report story

The problem was not primarily code quality. The problem was the interaction model.

The interface answered:

> "What information does the system currently contain?"

when it needed to answer:

> "What is the AI organization doing right now?"

## 1.2 The new rule

The screen is not a dashboard.

The screen is a stage.

The user does not inspect the stage to understand the system.

The system performs a visible sequence on the stage so the user understands the system automatically.

## 1.3 The one-sentence experience test

If a person watches ScholarX for twenty seconds with the sound muted and without being given an explanation, they should be able to infer:

1. there is a Commander
2. the Commander delegates work
3. agents receive tasks
4. agents go to different regions
5. agents research
6. agents return findings
7. the findings are analyzed
8. the system eventually creates a result

If this cannot be inferred, the design has failed regardless of implementation quality.

---

# 2. DESIGN NORTH STAR

## 2.1 The visual sentence

> **A central AI Commander deploys an autonomous research organization across the world, receives reports, challenges evidence, synthesizes intelligence, and turns the result into a polished scholarship dossier.**

Every major visual decision should reinforce that sentence.

## 2.2 The audience should feel

- curiosity
- movement
- intelligence
- coordination
- trust
- sophistication
- anticipation

The audience should NOT feel:

- they are reading an admin dashboard
- they are looking at developer logs
- they need to understand technical jargon before the story starts
- the system is overloaded
- every element is competing for attention

## 2.3 Visual metaphor

Use the metaphor of a premium autonomous intelligence theatre.

It can borrow the spatial drama of:

- mission control rooms
- intelligence operations centers
- advanced research environments
- air-traffic coordination
- cinematic command interfaces

But do not imitate a military interface literally.

No camouflage.
No faux radar clutter.
No gratuitous tactical language.
No decorative military insignia.

The product is an educational intelligence network.

---

# 3. TEN-PHASE IMPLEMENTATION MODEL

The frontend is divided into exactly ten design phases.

Each phase has:

- purpose
- scope
- non-goals
- components
- visual rules
- interaction rules
- animation rules
- implementation notes
- acceptance tests
- screenshot review
- stop conditions

## Phase 1
### Visual Reset and Theatre Foundation

Establish the new visual language and remove dashboard assumptions.

## Phase 2
### Spatial World Stage and Camera System

Make the world map the actual spatial coordinate system.

## Phase 3
### Commander and Agent Lifecycle System

Create the Commander, universal AgentCard, and agent state choreography.

## Phase 4
### Communication Packets and First Proof

Implement the complete Commander -> Europe Scout -> Report interaction.

## Phase 5
### Global Research Fleet and Tool Activity

Deploy five regional scouts and visualize real research operations.

## Phase 6
### Analysis, Verification, Skeptic, and Evidence

Turn discovered scholarships into visible reasoning and evidence processes.

## Phase 7
### Ranking, Synthesis, Dossier, Web Artifact, and PDF

Turn intelligence into an impressive final deliverable.

## Phase 8
### Real Event Integration and Presentation Engine

Connect the theatre to real SSE while preserving human-readable pacing.

## Phase 9
### Judge Mode, Resilience, Performance, and Exhibition Controls

Make the system interactive, robust, and understandable during the competition.

## Phase 10
### Final Art Direction, QA, Rehearsal, and Exhibition Lock

Treat the frontend as a finished show, not an unfinished software project.

---

# 4. GLOBAL RULES THAT APPLY TO ALL TEN PHASES

## 4.1 No dashboard regression

Never introduce:

- permanent left sidebar for primary information
- permanent right telemetry sidebar
- bottom pipeline rail
- metric wall
- full-page table as the main experience
- three-column dashboard as the default composition
- grid of equal cards

Temporary overlays are allowed.

## 4.2 No component-first thinking

Do not start by asking:

> "Which components do we need?"

Start by asking:

> "What should the audience see happen?"

Then derive the components from that scene.

## 4.3 No decorative animation

Animation must explain:

- command
- relationship
- state change
- discovery
- evidence
- decision
- progression

If an animation does not communicate anything, remove it.

## 4.4 No fake intelligence

Never create fake activity that looks like real agent work in live mode.

Demo mode may use recorded deterministic events, but it must feed the same presentation engine as live events.

## 4.5 No unexplained technical density

Technical detail belongs in contextual surfaces, not as a constant flood of raw logs.

The audience should first see:

> Europe Scout is searching.

Then, if they inspect:

> Tavily search executed with query X.

## 4.6 No microscopic text

Anything necessary for the story must remain readable at exhibition distance.

Technical microtext may be smaller, but it must never contain the only explanation of a major action.

## 4.7 One primary action at a time

At any moment there is one hero event.

Everything else is supporting activity or ambience.

## 4.8 The backend clock and theatre clock are separate

Backend execution may be fast.

Presentation must be understandable.

Never sacrifice comprehension to mirror raw backend speed.

---

# 5. GLOBAL SPATIAL MODEL

## 5.1 The screen is an infinite theatre inside a bounded 16:9 viewport

Target:

- 1920x1080
- 2560x1440
- large TV
- external exhibition monitor
- projector where contrast permits

The main theatre uses a responsive coordinate system derived from the 16:9 scene.

## 5.2 Recommended conceptual zones

These are spatial zones, not permanent panels.

### Zone A. Command Core

Upper-center or center-left depending on scene.

Contains the currently active Commander or parent agent.

### Zone B. Global World Field

The world map occupies the majority of the stage when global discovery is active.

### Zone C. Active Agent Field

Agent cards appear geographically or logically near their active region.

### Zone D. Communication Field

Packets travel through empty space between agents.

### Zone E. Research Field

Transient source objects, candidate objects, and tool activity appear close to the active agent.

### Zone F. Temporary Focus Surface

A selected agent, scholarship, evidence chain, or dossier can expand into a glass overlay without becoming a permanent sidebar.

## 5.3 Composition priority

At a global mission moment:

1. Commander
2. World map
3. active deployment path
4. active scout
5. secondary scouts
6. evidence objects
7. subtle mission chrome

At a research moment:

1. active scout
2. research objects
3. source chain
4. world context
5. Commander in background

At a verification moment:

1. candidate
2. verifier
3. skeptic
4. evidence
5. Commander background

At dossier time:

1. dossier page
2. build process
3. section completion
4. final PDF control

---

# 6. PHASE 1. VISUAL RESET AND THEATRE FOUNDATION

## 6.1 Objective

Create the visual foundation before building any complex workflow.

The goal is not to make the entire system look complete.

The goal is to create the visual material system from which everything else can be built.

## 6.2 Phase 1 non-goals

Do not implement:

- real multi-agent communication
- five-scout deployment
- ranking
- dossier generation
- real SSE choreography
- full judge mode

## 6.3 Repository actions

Before modifying code:

1. inspect the existing frontend
2. identify legacy dashboard layout components
3. identify reusable API/state modules
4. identify CSS tokens that can be removed
5. identify existing font imports
6. identify existing animation library usage
7. identify map dependencies

Do not delete backend code.

## 6.4 Visual reset

Establish:

- obsidian background
- glass surfaces
- restrained edge lighting
- premium typography
- controlled shadows
- subtle depth
- soft atmospheric world lighting

## 6.5 Background

Recommended visual hierarchy:

Base:

`#05070A`

Secondary deep surface:

`#080C10`

Elevated surface:

`#0B1117`

Glass surface:

`rgba(12,18,24,0.58)`

Use additional transparent layers for elevation rather than brighter fills.

## 6.6 Glass recipe

Glass should contain:

- translucent dark surface
- background blur
- 1px low-opacity border
- soft top-edge highlight
- soft inner shadow
- subtle outer shadow
- optional local color tint

Avoid obvious shiny gradients.

## 6.7 Color system

Use a restrained semantic palette.

### Neutral

Black and blue-black for structure.

### Command authority

Warm muted gold.

Use only for Commander authority, major decisions, and final control.

### Information flow

Cool cyan.

Use for communication packets and active information transfer.

### Verified truth

Emerald.

Use for verified evidence and successful verification.

### Warning

Amber.

Use for uncertainty, deadline pressure, incomplete documents, or uncovered costs.

### Challenge

Muted crimson.

Use only for Skeptic and hard failures.

Do not simultaneously flood the screen with all semantic colors.

## 6.8 Typography

The theatre UI needs a modern premium sans-serif.

Recommended family:

- Inter or another highly legible modern UI sans
- JetBrains Mono or equivalent for short technical identifiers
- an editorial serif only inside the dossier where appropriate

Avoid faux-futuristic fonts.

Avoid heavy military display fonts.

Avoid making everything uppercase.

## 6.9 Motion primitives

Create reusable primitives:

- fade-in
- fade-out
- spring scale
- glass reveal
- light sweep
- packet launch
- packet travel
- packet docking
- state pulse
- focus dim
- focus brighten
- soft camera zoom
- map route draw
- source pop-in
- report assembly

Do not create one-off timing values everywhere.

Centralize them.

## 6.10 Phase 1 deliverables

Expected outputs:

- new global tokens
- new glass surface primitives
- typography system
- spacing system
- elevation system
- motion token registry
- theatre root canvas
- no final data logic yet

## 6.11 Phase 1 acceptance test

A static theatre canvas with placeholder Commander and placeholder Agent must look premium.

A person should NOT see a normal dashboard.

## 6.12 Phase 1 screenshot checklist

Check at 1920x1080:

- background feels deep
- glass feels transparent
- text is readable
- there is enough breathing room
- colors feel restrained
- no visible dashboard columns
- no permanent telemetry
- no cyberpunk clutter

## 6.13 Phase 1 stop condition

Do not proceed if the visual foundation still resembles the old UI.

---

# 7. PHASE 2. SPATIAL WORLD STAGE AND CAMERA SYSTEM

## 7.1 Objective

Make the world map the actual spatial coordinate system.

This is the moment when ScholarX becomes a theatre rather than a panel layout.

## 7.2 World map requirements

The map must be:

- large
- legible
- low contrast
- visually rich enough to locate regions
- bright enough to remain visible at exhibition distance
- integrated with the glass environment
- responsive to mission state

The map must never be a tiny widget in a panel.

## 7.3 Pakistan origin

Pakistan is the mission origin.

Use the project's configured Pakistan anchor.

Represent it with:

- subtle emerald glow
- origin ring
- tiny label
- soft geographic halo

Do not use a giant glowing dot.

## 7.4 Regional coordinates

Define stable scene coordinates for:

- Europe
- Asia
- MENA
- Americas
- Oceania

Coordinate mapping should be consistent across scenes.

## 7.5 Map states

### Dormant map

Very low contrast.

### Mission map

Origin becomes active.

### Deployment map

Regional destinations illuminate.

### Research map

Active region receives an attention halo.

### Evidence map

Specific country or institution may become active.

### Dossier map

Map fades away as the document becomes primary.

## 7.6 Camera language

There is no need for a literal 3D camera at all times.

Camera behavior can be simulated through:

- viewport translation
- scale
- focus blur
- local brightness
- background dimming
- map zoom
- agent enlargement

## 7.7 Camera shots

### Global

Full world visible.

### Deployment

Pakistan plus regional destinations visible.

### Regional

One continent dominates.

### Agent

One agent card and local workspace dominate.

### Evidence

Candidate plus sources dominate.

### Dossier

Document fills the stage.

## 7.8 Map route animation

Routes should be curved.

They should have:

- start point
- route arc
- moving particle
- subtle trail
- destination pulse

The route is a communication visual, not decorative map artwork.

## 7.9 Phase 2 deliverables

- full world stage
- spatial coordinate system
- geographic anchor registry
- map rendering
- route animation infrastructure
- camera/focus primitives

## 7.10 Phase 2 acceptance test

A judge must be able to see Pakistan and understand that a deployed task is travelling toward a particular region.

## 7.11 Phase 2 stop condition

Do not proceed if the map is still visually secondary.

---

# 8. PHASE 3. COMMANDER AND AGENT LIFECYCLE SYSTEM

## 8.1 Objective

Make agents the main visual actors.

## 8.2 The Commander

The Commander is not a normal card.

It is the current authority node of the stage.

The Commander should show:

- role
- current mission
- decision state
- current delegated task
- current report
- current decision

## 8.3 Commander states

IDLE

THINKING

DECIDING

DIRECTING

WAITING

RECEIVING

SYNTHESIZING

COMPLETE

## 8.4 Commander thinking

Do not animate fake AI brain text endlessly.

Use a concise decision surface:

MISSION

CONSTRAINTS

AVAILABLE ACTIONS

NEXT DECISION

Then transition to the decision.

## 8.5 Universal AgentCard

Every agent and workflow gets the same foundational visual language.

### Layer 1. Identity

- name
- type
- parent
- status light

### Layer 2. Mission

One short directive.

### Layer 3. Current operation

Current tool or activity.

### Layer 4. Findings

Current discovery or state.

### Layer 5. Progress

Pipeline and progress.

## 8.6 Agent types

Use visual language to distinguish:

### Agent

LLM-powered decision/judgment component.

### Workflow

Deterministic execution component.

The distinction must be visible but subtle.

Do not falsely call every entity an AI agent.

## 8.7 Lifecycle states

IDLE

RECEIVING

ACKNOWLEDGING

DEPLOYING

SEARCHING

READING

EXTRACTING

NORMALIZING

ANALYZING

VERIFYING

REPORTING

RETURNING

COMPLETE

BLOCKED

FAILED

RECOVERING

CACHED

## 8.8 Lifecycle animation

### Receiving

Glass brightens from the destination edge inward.

### Acknowledging

Short pulse.

### Working

Internal activity indicator.

### Finding

New finding object appears.

### Reporting

Card compresses findings into a report block.

### Returning

Report packet detaches.

## 8.9 Dynamic spawn

Do not render all agents simultaneously.

When an agent is invoked:

1. parent emits command
2. destination location is identified
3. glass seed appears
4. identity resolves
5. card expands
6. agent becomes active

This prevents the stage from looking like a dashboard.

## 8.10 Phase 3 acceptance test

The Commander and one child agent can exist on stage without looking like two dashboard widgets.

They must feel like two entities with a relationship.

---

# 9. PHASE 4. COMMUNICATION PACKETS AND FIRST PROOF

## 9.1 Objective

This is the most important phase in the entire guide.

Build one complete interaction:

> Commander -> Europe Scout -> acknowledgement -> research -> report -> Commander.

Nothing else matters until this feels excellent.

## 9.2 Communication model

No generic connecting lines.

Use physical messages.

Types:

- COMMAND
- ACKNOWLEDGEMENT
- REPORT
- EVIDENCE
- CHALLENGE
- RESOLUTION

## 9.3 Command packet anatomy

A packet contains:

- sender
- receiver
- packet type
- short mission summary
- optional priority

Example:

`COMMAND / COMMANDER -> EUROPE SCOUT / FIND FUNDED CS OPPORTUNITIES`

## 9.4 Command animation

1. Commander enters DIRECTING state.
2. Directive text appears.
3. Packet forms from the Commander.
4. Packet acquires destination.
5. Route highlights.
6. Packet travels.
7. Destination card receives glow.
8. Packet docks.
9. Child becomes RECEIVING.
10. Child becomes ACKNOWLEDGING.

## 9.5 Acknowledgement

Text should be short:

`COMMAND RECEIVED`

`DEPLOYING EUROPE SCOUT`

Packet returns to parent.

## 9.6 Search operation

Europe Scout transitions:

RECEIVING
-> ACKNOWLEDGING
-> WORKING
-> SEARCHING

Display the active query.

Do not dump raw logs.

## 9.7 Source discovery

The first source should appear visually.

Examples:

- official portal
- university
- HEC
- government
- scholarship portal

## 9.8 Candidate emergence

When the research returns a scholarship candidate, the candidate should be born from the research area.

It should not teleport into a random card list.

## 9.9 Report assembly

Raw findings should visually compress into:

REPORT READY

- candidates discovered
- high relevance count
- verification needs
- important findings

## 9.10 Report return

The report physically returns to the Commander.

The Commander changes state to RECEIVING.

Then SYNTHESIZING.

Then it decides the next action.

## 9.11 Phase 4 hard gate

The 3-meter test is mandatory.

At three meters, an observer must understand:

- Commander gave a task
- Europe Scout received it
- Europe Scout worked
- Europe Scout found something
- Europe Scout returned a report
- Commander received the report

No verbal explanation.

## 9.12 Phase 4 stop condition

If the screenshot looks like two cards plus an animated line, stop.

The interaction itself must be visually obvious.

---

# 10. PHASE 5. GLOBAL RESEARCH FLEET AND TOOL ACTIVITY

## 10.1 Objective

Expand the single-agent proof into a believable autonomous research fleet.

## 10.2 Fleet

Five regional scout workflows:

- Europe
- Asia
- MENA
- Americas
- Oceania

These are deterministic workflows in the system architecture. Visually, represent them as research specialists/workflows, not as independent LLM personas.

## 10.3 Fleet deployment sequence

Do not spawn all five at exactly the same frame.

Recommended choreography:

1. Discovery Commander receives authorization.
2. Europe command dispatched.
3. short pause
4. Asia command dispatched
5. short pause
6. MENA command dispatched
7. short pause
8. Americas command dispatched
9. short pause
10. Oceania command dispatched

Then allow controlled overlap.

## 10.4 Fleet map motion

Each route starts from Pakistan.

Each route uses a different curvature to avoid overlap.

Each destination receives a pulse.

## 10.5 Regional workspace

When a Scout arrives, create a local workspace around it.

The workspace includes:

- current query
- source objects
- extraction objects
- candidate objects
- progress

## 10.6 Search stage

Visualize:

query formation
search dispatch
results arriving
relevance filtering

## 10.7 Scrape stage

Visualize one page becoming active.

Show:

URL/domain
source type
read status

## 10.8 Extract stage

Show structured fields being formed:

country
funding
eligibility
deadline
application portal

## 10.9 Normalize stage

The raw source collapses into canonical scholarship data.

## 10.10 Report stage

Candidates group into a report packet.

## 10.11 Tool visibility rule

The tool chain should be visible enough to demonstrate that real work happened, but not so visible that it looks like raw logging.

Preferred language:

`SEARCH`
`READ SOURCE`
`EXTRACT`
`NORMALIZE`
`REPORT`

Use technical provider names as secondary metadata.

## 10.12 Parallelism

When multiple scouts are active, use attention cycling.

One region is primary.

The others remain subtly animated in the background.

Do not make five simultaneous scenes equally bright.

## 10.13 Phase 5 acceptance test

The judge must understand that the system has deployed multiple regional research specialists, not simply displayed five cards.

---

# 11. PHASE 6. ANALYSIS, VERIFICATION, SKEPTIC, AND EVIDENCE

## 11.1 Objective

Turn research findings into visible reasoning.

## 11.2 Candidate handoff

When a candidate becomes promising, it should be selected from the discovery field and move toward the analysis pipeline.

Do not teleport it into a results grid.

## 11.3 Eligibility Investigator

The workflow checks the defined 15 Pakistan-aware dimensions.

Visual representation:

- criteria list
- current criterion highlighted
- result state
- action required when applicable

## 11.4 Eligibility animation

Criteria should reveal sequentially.

Example:

Pakistan eligible ✓
Degree level ✓
Field match ✓
Academic threshold ✓
Language ✓
HEC requirement ⚠
Deadline ✓

Do not reveal all 15 checks instantly.

## 11.5 True Cost Analyzer

The system must visually dismantle the idea of "free".

Use a cost waterfall.

Example:

TUITION
covered

ACCOMMODATION
covered

STIPEND
covered

TRAVEL
uncovered

ATTESTATION
uncovered

INITIAL RESERVE
required

TOTAL OUT-OF-POCKET
PKR value

## 11.6 Deadline Intelligence

Use a timeline runway.

Show:

application deadline
preparation time
buffer
slack
risk

Use Pakistan-specific preparation timelines from the backend.

## 11.7 Verification Agent

Verification should look like investigation.

Show:

claim
source
source quality
status
resolution

Possible states:

VERIFIED
PARTIALLY VERIFIED
SUSPICIOUS / OUTDATED
HEC LISTED

## 11.8 Skeptic Agent

The Skeptic should challenge specific claims.

Avoid long fake chat transcripts.

Use structured challenge cards.

Example:

`CHALLENGE`

"Funding is described as full, but travel and pre-departure costs are not covered."

## 11.9 Challenge packet

Skeptic -> Verification

The challenge physically travels.

Verification researches.

Evidence returns.

## 11.10 Resolution packet

Verification -> Synthesis

State:

resolved
partially resolved
unresolved

## 11.11 Evidence graph

Evidence should connect:

claim
-> source
-> extracted fact
-> verification result
-> final conclusion

The graph is secondary to comprehension.

Never let the evidence graph become a huge decorative network.

## 11.12 Phase 6 acceptance test

A judge can identify:

- what was claimed
- who challenged it
- which source was checked
- what changed
- whether the candidate remained credible

without opening a debug panel.

---

# 12. PHASE 7. RANKING, SYNTHESIS, DOSSIER, WEB ARTIFACT, AND PDF

## 12.1 Objective

Turn the result of all intelligence work into a polished human artifact.

## 12.2 Synthesis

The synthesis workflow aggregates deterministic outputs into a coherent Scholarship DNA representation.

Visually:

candidate
+
eligibility
+
funding
+
deadline
+
verification
+
skeptic
=
Scholarship Intelligence Object

## 12.3 Ranking

Ranking is a decision visualization, not a static leaderboard.

When a score changes, show why.

Example:

VERIFICATION CONFIRMED

Score:

84 -> 91

Rank:

#4 -> #2

Animate the movement.

## 12.4 Ranking animation

Use spring movement.

Affected candidate moves.

Other candidates shift around it.

Avoid perpetual pulsing.

The movement should occur only when actual state changes occur.

## 12.5 Final Advisor

Once ranking is complete, the Final Advisor produces the personalized roadmap.

This includes Pakistan-specific administrative steps as defined by the architecture.

## 12.6 Dossier transition

The theatre gradually quiets.

Research objects collapse.

Commander becomes a small source authority marker.

The selected scholarship expands into a document surface.

## 12.7 Dossier builder

The dossier should look like a premium professional document.

Use a light page against the dark theatre only when appropriate.

The transition should feel like:

`intelligence -> artifact`

## 12.8 Dossier sections

At minimum:

1. scholarship identity
2. host country
3. institution
4. degree/program
5. executive summary
6. candidate fit
7. eligibility criteria
8. Pakistan eligibility
9. funding breakdown
10. true out-of-pocket costs
11. required documents
12. Pakistan-specific administrative requirements
13. deadline
14. preparation timeline
15. official application portal
16. how to apply
17. evidence and verification
18. skeptic findings
19. risks and cautions
20. personalized action plan
21. source references

## 12.9 Live web page generation

The dossier should be visibly assembled.

Show section cards on the left or around the document only during the build process.

Example sequence:

`IDENTITY` complete

`EXECUTIVE SUMMARY` complete

`ELIGIBILITY` complete

`FUNDING` complete

`DEADLINE` complete

`PORTAL` complete

`ACTION PLAN` complete

The actual page should fill field-by-field.

## 12.10 Field injection animation

The AI-generated value should appear in the target field.

Examples:

`Country -> Hungary`

`Funding -> Tuition + Dormitory + Stipend`

`Deadline -> 15 January`

`Portal -> official URL`

Do not make the typing effect absurdly slow.

Use chunked insertion.

## 12.11 PDF generation

Generate a real PDF from HTML/CSS.

Do not screenshot the page.

The PDF should preserve:

- typography
- tables
- badges
- page breaks
- backgrounds where appropriate
- headers
- footers
- source references

## 12.12 Phase 7 acceptance test

The final artifact should be something a student would actually want to download and read.

It must not feel like an AI transcript.

---

# 13. PHASE 8. REAL EVENT INTEGRATION AND PRESENTATION ENGINE

## 13.1 Objective

Connect the theatrical frontend to real ScholarX event streams without losing human-readable pacing.

## 13.2 Three execution layers

### Layer 1. Intelligence

Actual backend LangGraph execution.

### Layer 2. Event

Redis event transport and SSE.

### Layer 3. Theatre

Frontend presentation orchestration.

Never collapse these responsibilities into one layer.

## 13.3 Event pipeline

Use:

`raw backend event`

-> `event normalizer`

-> `mission state reducer`

-> `agent lifecycle store`

-> `presentation queue`

-> `theatre director`

-> `animation choreography`

-> `visual scene`

## 13.4 Event normalizer

Convert backend events into stable frontend event types.

Example:

`SEARCH_QUERY_EXECUTED`

becomes:

`SCOUT_SEARCH_ACTIVITY`

`SOURCE_FOUND`

becomes:

`SOURCE_DISCOVERED`

The normalizer prevents backend schema churn from leaking into visual components.

## 13.5 Agent Lifecycle Store

Maintain current state for every active entity.

Example:

Commander:

`DIRECTING`

Europe Scout:

`SEARCHING`

Asia Scout:

`WAITING`

Verification:

`IDLE`

## 13.6 Presentation Queue

This is not a normal event queue.

It is a human-comprehension queue.

Each event receives:

- importance
- visual type
- minimum display time
- hold time
- optional coalescing key
- target entity
- target region
- focus priority

## 13.7 Importance levels

### Hero

Mission decision

Command

Agent spawn

Report

Verification challenge

Ranking change

Dossier completion

### Supporting

Source found

tool activity

candidate extraction

minor state transitions

### Ambient

cached result

secondary source

low-priority telemetry

## 13.8 Two clocks

### Intelligence clock

Real execution.

### Presentation clock

Human-readable sequence.

The presentation clock may be slower.

## 13.9 Coalescing

If twenty source results arrive:

Do not animate twenty source cards.

Show a representative set.

Display:

`18 sources scanned`

and visually animate perhaps three meaningful sources.

## 13.10 Slow mode

Create a global presentation speed:

1x

2x

0.5x

or equivalent.

Default exhibition mode should prioritize comprehension.

## 13.11 Pause

Pause should freeze presentation transitions without destroying backend state.

The system can continue collecting backend events into the queue if configured.

## 13.12 Real event vs presentation event

Example:

Backend event:

`SOURCE_FOUND`

Presentation events:

`SOURCE_FOCUS`

`SOURCE_CARD_APPEAR`

`SOURCE_STATUS_CONFIRM`

`RETURN_TO_AGENT`

The UI should be designed around presentation events.

## 13.13 Phase 8 acceptance test

The same visual experience must work with:

- demo event stream
- real SSE stream

without rewriting the visual components.

---

# 14. PHASE 9. JUDGE MODE, RESILIENCE, PERFORMANCE, AND EXHIBITION CONTROLS

## 14.1 Objective

Make the system reliable under public demonstration conditions.

## 14.2 Judge Mode

A small floating control surface may appear only when activated.

Do not permanently place judge controls around the theatre.

Possible modifiers:

- full funding only
- Europe only
- no IELTS
- maximum out-of-pocket budget
- degree level
- field

## 14.3 Constraint injection

The judge changes a constraint.

Example:

`NO IELTS`

The theatre should show:

Commander receives new constraint.

Then a visible ripple moves through the relevant decision chain.

Do not pretend the entire backend instantly reruns if it does not.

## 14.4 Demo mode

Create deterministic demo profiles.

At least one primary profile should be a Pakistani ICS/CS student matching the architecture's stated demo profile.

## 14.5 Cached intelligence

If live search fails:

show a tasteful state:

`LIVE SOURCE UNAVAILABLE`

`USING VERIFIED CACHE`

Then continue the theatre.

Do not show raw exceptions.

## 14.6 Error states

Errors are part of the story.

A tool failure should look like a professional operational transition.

Example:

`EUROPE SEARCH SOURCE UNAVAILABLE`

then:

`FAILOVER: JINA READER`

then:

`RESUMING`

The actual backend failover architecture should determine what can truthfully be shown.

## 14.7 Sound

Optional.

Use sparse cues:

- command dispatched
- agent spawned
- report received
- verification passed
- challenge
- mission complete

Mute must always be available.

## 14.8 Performance

Target 60fps where practical.

Avoid:

- uncontrolled DOM growth
- hundreds of permanent animated elements
- expensive map redraws
- continuous unnecessary particle systems
- large shadow stacks

Use canvas/WebGL where appropriate.

## 14.9 Exhibition hardware

Assume:

- laptop with at least 16GB RAM
- external 1920x1080 display or larger
- reliable local network/internet for live mode
- cached demo fallback

## 14.10 Phase 9 acceptance test

A judge can interact with the mission without exposing developer tools.

The experience remains intelligible when the network or an API fails.

---

# 15. PHASE 10. FINAL ART DIRECTION, QA, REHEARSAL, AND EXHIBITION LOCK

## 15.1 Objective

Treat the frontend as a finished exhibition piece.

No new major UI patterns after this phase.

## 15.2 Full mission sequence

Recommended showcase flow:

### Scene 1. Silence

Minimal world stage.

### Scene 2. Mission arrival

Student context appears.

### Scene 3. Commander thinking

Short planning state.

### Scene 4. Discovery Commander handoff

Visible parent-child command.

### Scene 5. Fleet deployment

Five regions activated.

### Scene 6. Research

Multiple scouts work with controlled focus cycling.

### Scene 7. Candidate convergence

Promising scholarships enter analysis.

### Scene 8. Verification

Verifier and Skeptic interact.

### Scene 9. Ranking change

New evidence causes a visible ranking update.

### Scene 10. Dossier generation

The selected scholarship becomes a professional web document.

### Scene 11. PDF generation

The document becomes downloadable.

### Scene 12. Completion

Mission complete.

## 15.3 Visual freeze rule

Do not continue adding features because they are technically possible.

Once the visual story is coherent, freeze it.

## 15.4 3-meter test

Run at least three rehearsals:

### Test A. 3 meters

Can a person understand the story?

### Test B. 1 meter

Can the person inspect agent details?

### Test C. Developer close-up

Can the team inspect event and technical details?

The experience must work at all three distances without changing into a dashboard.

## 15.5 Non-developer comprehension test

Show the system to someone who has never seen ScholarX.

Ask:

1. What is the Commander doing?
2. Where did the first agent go?
3. What did it do?
4. What did it send back?
5. What happens after research?
6. Why did the system trust or reject the scholarship?

Do not explain the system before the test.

## 15.6 Exhibition failure classification

If the viewer cannot understand the sequence, classify the failure:

- hierarchy failure
- timing failure
- text failure
- animation failure
- map failure
- communication failure
- visual overload
- state ambiguity

Fix the category, not the symptom.

## 15.7 Phase 10 acceptance

The system passes only when:

- story is understandable
- map is visible
- agents are distinct
- command packets are obvious
- report packets are obvious
- research process is visible
- evidence process is visible
- ranking changes are intelligible
- dossier is beautiful
- PDF is real
- fallback works
- performance remains stable

---

# 16. AGENT CARD MASTER SPECIFICATION

This section applies across all phases.

## 16.1 Card anatomy

Every agent card contains:

### Header

Name
Type
Status
Parent relationship

### Mission

One sentence.

### Current operation

Short human-readable state.

### Tool activity

Current tool or operation.

### Evidence/finding

Only the most relevant current result.

### Progress

Pipeline stage plus progress.

### Optional detail

More technical metadata can appear on selection.

## 16.2 Card proportions

Do not make cards overly tall.

Do not cram seven rows of telemetry into every card.

The card needs breathing room.

## 16.3 Glass depth

Use three elevation levels:

Tier 1:
background glass

Tier 2:
active agent glass

Tier 3:
hero Commander glass

## 16.4 Hover

Subtle lift.

Do not dramatically scale cards.

## 16.5 Selection

Selection should increase:

- local contrast
- edge visibility
- information detail

while dimming unrelated elements.

---

# 17. PACKET SYSTEM MASTER SPECIFICATION

## 17.1 Packet types

COMMAND

ACK

REPORT

EVIDENCE

CHALLENGE

RESOLUTION

## 17.2 Packet lifecycle

CREATED

ROUTED

TRAVELLING

ARRIVING

DOCKED

CONSUMED

## 17.3 Packet appearance

Small but legible.

Should feel physical.

Should have a soft trail.

Should have a sender/receiver indication.

## 17.4 Packet motion

Never use a straight line by default.

Use curved paths.

Use slight acceleration and deceleration.

Avoid overshoot.

## 17.5 Packet timing

Command:

900ms to 1400ms depending on distance.

Ack:

500ms to 900ms.

Report:

900ms to 1500ms.

Critical event:

Hold on arrival before moving to next event.

---

# 18. ANIMATION BIBLE

## 18.1 Principles

Animation should:

- create causality
- show hierarchy
- show ownership
- show location
- show state
- show change

## 18.2 Easing

Use:

- fast easing for UI state changes
- soft cinematic easing for spatial travel
- spring for card arrangement
- controlled linear travel for packets

Avoid:

- constant bouncing
- large elastic overshoot
- random floating
- excessive parallax

## 18.3 Spawn animation

Sequence:

1. location seed
2. light pulse
3. glass materialization
4. identity reveal
5. mission text
6. active state

## 18.4 Working animation

Internal subtle movement.

Possible:

- progress line
- query cursor
- soft scan
- source object entry

The working animation must remain quiet enough that text stays readable.

## 18.5 Report animation

Findings collapse into a report block.

Report block detaches.

Packet route activates.

Report travels.

Destination agent enters RECEIVING.

## 18.6 Debate animation

Skeptic challenge appears.

Challenge packet travels.

Verification agent highlights source.

Evidence enters.

Resolution emerges.

## 18.7 Ranking animation

Candidate score changes.

Rank badge updates.

Candidate moves.

Affected neighbors shift smoothly.

No sudden teleportation.

---

# 19. PRESENTATION ENGINE MASTER SPECIFICATION

## 19.1 PresentationQueue responsibilities

The queue controls:

- order
- minimum display time
- concurrency
- focus
- coalescing
- pause
- slow mode
- replay

## 19.2 TheatreDirector responsibilities

The TheatreDirector decides:

- which entities become primary
- which agents become secondary
- which objects should be hidden
- when the camera focuses
- when to spawn a packet
- when to hold a result
- when to transition scenes

## 19.3 TheatreDirector does NOT decide

It does not determine:

- eligibility
- ranking
- verification truth
- scholarship data

Those come from the backend.

## 19.4 Focus policy

Use three levels:

Hero

Supporting

Ambient

At most two hero entities unless the mission specifically requires a comparison.

---

# 20. RESEARCH VISUALIZATION MASTER SPECIFICATION

## 20.1 Search

Show the query.

Do not show a wall of raw URLs.

## 20.2 Source

Show representative source cards.

Source card should include:

- title/domain
- source class
- region
- state

## 20.3 Extraction

Show structured fields appearing from a source.

Examples:

`Funding -> Full`

`Degree -> Bachelor's`

`Pakistan Eligible -> Yes`

`Deadline -> date`

## 20.4 Normalization

Show raw source compressing into the canonical scholarship object.

## 20.5 Candidate emergence

Candidate object appears and receives an identity.

It then waits for downstream analysis.

---

# 21. SCHOLARSHIP CANDIDATE MASTER SPECIFICATION

## 21.1 Candidate states

DISCOVERED

POTENTIAL

ELIGIBILITY_REVIEW

COST_REVIEW

DEADLINE_REVIEW

VERIFICATION

CHALLENGED

VERIFIED

RANKED

REJECTED

SELECTED

## 21.2 Candidate identity

Show:

- scholarship name
- host country
- degree level
- field
- funding class

## 21.3 Candidate movement

Candidate should move between stages.

Movement should be meaningful.

Do not create arbitrary bouncing cards.

---

# 22. EVIDENCE AND VERIFICATION MASTER SPECIFICATION

## 22.1 Evidence object

Evidence should include:

source
claim
extracted fact
verification status
confidence

## 22.2 Trust hierarchy

Follow the project's backend verification rules.

Do not hardcode frontend trust decisions that conflict with backend semantics.

## 22.3 Evidence presentation

When selected:

claim
-> evidence
-> source
-> verification
-> conclusion

## 22.4 Skeptic

The Skeptic is a challenger, not a villain.

Use structured skepticism.

The Skeptic should ask:

- What is missing?
- What conflicts?
- What could invalidate this recommendation?
- What would materially affect a Pakistani applicant?

---

# 23. DOSSIER WEB PAGE MASTER SPECIFICATION

## 23.1 Visual split

The theatre is dark.

The final document may be light and editorial.

This contrast is deliberate.

## 23.2 Dossier hierarchy

Cover

Executive summary

Eligibility

Funding

Costs

Requirements

Deadline

Official portal

How to apply

Pakistan pathway

Verification evidence

Risks

Personalized roadmap

Sources

## 23.3 Dossier generation sequence

1. identity
2. summary
3. fit
4. eligibility
5. funding
6. cost
7. documents
8. deadline
9. portal
10. application steps
11. Pakistan pathway
12. evidence
13. risk
14. roadmap
15. final review

## 23.4 Final artifact

The final dossier should resemble a premium professional report, not a chat transcript.

---

# 24. PDF MASTER SPECIFICATION

## 24.1 Real HTML/CSS

The PDF must come from the actual dossier document.

## 24.2 Print requirements

A4

consistent margins

page breaks

header/footer

legible tables

page numbering

source references

## 24.3 PDF validation

After generation:

- verify page count
- verify no clipped text
- verify tables fit
- verify colors remain readable
- verify hyperlinks where supported
- verify the document title

## 24.4 Download

Provide:

`DOWNLOAD PDF`

with a real file.

Do not fake the interaction.

---

# 25. DEMO MODE

## 25.1 Why demo mode exists

Live APIs are not reliable enough to be the only exhibition path.

Demo mode is a deterministic visual scenario using the same presentation engine.

## 25.2 Demo event source

Create a structured event sequence.

It must use the same frontend event types as live mode.

## 25.3 Demo profile

Use the project's primary Pakistani ICS/CS profile.

## 25.4 Demo scenario

The demo should produce:

- global deployment
- multiple discoveries
- one strong candidate
- one skeptical challenge
- one verification resolution
- ranking change
- dossier creation

## 25.5 Demo speed

Do not speed-run the entire pipeline.

The first minute is about comprehension.

The later section can accelerate slightly.

---

# 26. DEBUG MODE VS SHOWCASE MODE

## 26.1 Showcase mode

Visible:

- Commander
- map
- agents
- communication
- research
- evidence
- ranking
- dossier
- minimal controls

Hidden:

- raw JSON
- API key information
- raw SSE logs
- developer test controls
- test script buttons
- latency diagnostics

## 26.2 Debug mode

May expose:

- raw event stream
- event payload
- agent lifecycle
- presentation queue
- scene state
- packet coordinates
- timing
- backend connection state

Debug mode is for development only.

---

# 27. NO-SIDEBAR PRINCIPLE

There are no permanent left or right information columns in the theatre.

Temporary overlays are allowed.

When the viewer selects a source or candidate:

use a floating glass detail surface.

When they close it:

the world stage becomes visible again.

The default screen remains the theatre.

---

# 28. ATTENTION MANAGEMENT

## 28.1 Hero event

The most important event gets:

- stronger contrast
- larger scale
- sharper text
- brighter glass
- more motion

## 28.2 Supporting event

Keep active but quieter.

## 28.3 Ambient event

Can remain as subtle motion or small state indicators.

## 28.4 Event limit

Never show every event.

Summarize or coalesce large batches.

---

# 29. 3-METER TEST SPECIFICATION

## 29.1 Setup

Display at 1920x1080.

Observer at approximately three meters.

No explanation.

No mouse control required.

## 29.2 Test

Show first 20 to 30 seconds of Commander -> Europe interaction.

## 29.3 Questions

Ask observer:

1. Who is in charge?
2. What did it send?
3. Which region received the task?
4. What is that region doing?
5. What happened after the research?

## 29.4 Failure responses

If observer says:

"I don't know"

identify whether the cause is:

- weak packet visibility
- weak card state
- bad map visibility
- poor typography
- bad timing
- too many competing elements

Fix the design.

---

# 30. ANIMATION REVIEW CHECKLIST

Every animation must answer one question.

### Packet

Where is information going?

### Spawn

Who has become active?

### Pulse

What has changed?

### Route

Where is the agent operating?

### Source arrival

What was discovered?

### Report return

What did the child send back?

### Ranking move

What decision changed?

### Dossier generation

What intelligence became an artifact?

If the answer is unclear, the animation is not good enough.

---

# 31. LIBRARY AND TECHNOLOGY POLICY

The frontend team is explicitly allowed to use high-quality third-party libraries.

Do not reinvent:

- complex motion systems
- map rendering
- graph rendering
- PDF rendering
- document pagination
- advanced spring physics

Potential tools include:

- Motion for React
- GSAP
- React Flow
- MapLibre GL JS
- D3 Geo
- React Three Fiber
- Playwright for PDF generation

Choose libraries based on outcome quality, maintainability, and exhibition performance.

Do not add libraries without purpose.

---

# 32. STATE ARCHITECTURE FOR THE THEATRE

## 32.1 Raw state

Backend event state.

## 32.2 Mission state

Current mission phase.

## 32.3 Agent state

Lifecycle state for every entity.

## 32.4 Presentation state

Currently staged visual action.

## 32.5 Scene state

Spatial positions and focus.

## 32.6 Artifact state

Dossier build state.

These layers should not all live in one giant React component.

---

# 33. COMPONENT ARCHITECTURE

Suggested conceptual tree:

```text
frontend/
  app/
    page.tsx
    hunt/
    dossier/

  components/
    theatre/
      TheatreViewport
      TheatreDirector
      PresentationQueue
      CameraController

    world/
      WorldStage
      OriginBeacon
      DeploymentRoute
      RegionAnchor

    commander/
      CommanderCard
      CommandComposer
      DecisionState

    agents/
      AgentCard
      AgentLifecycle
      AgentWorkspace
      AgentReport

    communication/
      PacketCanvas
      CommandPacket
      AckPacket
      ReportPacket
      EvidencePacket
      ChallengePacket

    research/
      SearchActivity
      SourceCard
      ExtractionFields
      CandidateObject

    analysis/
      EligibilityInvestigator
      TrueCostAnalyzer
      DeadlineIntelligence

    verification/
      VerificationArena
      SkepticChallenge
      EvidenceGraph
      ResolutionCard

    ranking/
      RankingStack
      RankTransition

    dossier/
      DossierBuilder
      DossierPage
      PdfControls

    controls/
      JudgeMode
      TheatreControls

    debug/
      EventInspector
      LifecycleInspector
```

The exact names may differ.

The architectural separation matters more than file names.

---

# 34. EVENT TO VISUAL MAPPING

## Mission events

`MISSION_INITIATED`

-> Commander wakes

`PHASE_TRANSITION`

-> subtle phase shift

`AGENT_SPAWNED`

-> agent materialization

`MISSION_COMPLETE`

-> completion state

## Discovery events

`SCOUT_DEPLOYED`

-> route + spawn

`SEARCH_QUERY_EXECUTED`

-> query display

`PAGE_SCRAPED`

-> source activity

`CANDIDATE_EXTRACTED`

-> candidate emergence

## Verification events

`VERIFICATION_STARTED`

-> verifier activation

`SKEPTIC_CHALLENGE`

-> challenge packet

`CHALLENGE_RESOLVED`

-> resolution animation

## Session events

`CACHE_HIT`

-> tasteful cached intelligence indicator

`FALLBACK_TOOL_USED`

-> recovery visual

---

# 35. INFORMATION DENSITY RULES

## 35.1 Agent limit

Do not show more active hero cards than the audience can distinguish.

## 35.2 Source limit

Animate a small representative subset.

## 35.3 Candidate limit

Use a clear funnel.

Do not display fifty candidates as fifty equal cards.

## 35.4 Technical logs

Never let raw logs become the visual focus.

---

# 36. VISUAL QUALITY BAR

## Composition

- world map visible
- Commander obvious
- active agent obvious
- empty space available for communication
- no dashboard grid

## Typography

- readable at distance
- strong hierarchy
- no faux military fonts
- no microscopic main text

## Glass

- believable transparency
- subtle depth
- restrained borders
- no generic template look

## Color

- black dominant
- cyan information
- emerald verification
- amber warning
- muted red challenge
- gold command authority

## Animation

- causality obvious
- no gratuitous motion
- packets travel
- reports return
- state changes have meaning

## Story

- viewer understands sequence without explanation

---

# 37. IMPLEMENTATION RULE FOR THE CODING AGENT

When implementing any phase:

1. Read the current phase fully.
2. Inspect the existing code relevant to the phase.
3. Do not implement later phases.
4. Do not invent UI unrelated to the phase.
5. Keep the previous phase working.
6. Run the required checks.
7. Produce a visual screenshot at 1920x1080.
8. Review the screenshot against the phase acceptance criteria.
9. Only then request approval for the next phase.

## Forbidden behavior

Do not say:

> "I implemented the whole frontend because the design is now understood."

Do not skip phases.

Do not silently redesign accepted phases.

Do not add permanent dashboards.

---

# 38. PHASE PROMPT PROTOCOL

The master guide is divided into ten phases because the coding agent should receive one phase at a time.

For each phase, the operator should provide:

```text
Read /docs/new_design_guide.md.

You are implementing PHASE N ONLY.

Do not implement later phases.

First inspect the existing code relevant to Phase N.

Then make the smallest architectural changes needed.

After implementation:

1. run type check
2. run build if applicable
3. run tests relevant to the phase
4. launch the frontend
5. inspect the result at 1920x1080
6. provide a concise implementation report
7. provide known issues
8. provide a screenshot path

STOP after Phase N.
```

The operator then reviews the visual result before authorizing the next phase.

---

# 39. PHASE-SPECIFIC APPROVAL GATES

## Gate 1

Visual language accepted.

## Gate 2

World stage accepted.

## Gate 3

Commander and agent lifecycle accepted.

## Gate 4

Commander -> Europe Scout interaction accepted at three meters.

## Gate 5

Five-scout deployment accepted.

## Gate 6

Research and verification accepted.

## Gate 7

Ranking and dossier accepted.

## Gate 8

Live event system accepted.

## Gate 9

Judge mode and resilience accepted.

## Gate 10

Exhibition lock approved.

---

# 40. DO NOT REPEAT THESE PREVIOUS MISTAKES

## Mistake 1

Making the world map a small widget.

### Correction

The world is the stage.

## Mistake 2

Making agents metric cards.

### Correction

Agents are active operational entities.

## Mistake 3

Making telemetry the experience.

### Correction

Telemetry is secondary context.

## Mistake 4

Showing every phase permanently.

### Correction

Phases unfold in the theatre.

## Mistake 5

Using many colors at once.

### Correction

Use a small semantic palette.

## Mistake 6

Starting with full functionality.

### Correction

Start with one flawless visual interaction.

## Mistake 7

Implementing animations as decoration.

### Correction

Animation communicates causality.

## Mistake 8

Building everything before reviewing screenshots.

### Correction

Every phase ends with visual review.

## Mistake 9

Letting the old dashboard architecture shape the new theatre.

### Correction

Treat the legacy presentation layer as replaceable.

## Mistake 10

Letting backend speed determine frontend speed.

### Correction

Use a presentation clock.

## Mistake 11

Showing developer controls to judges.

### Correction

Separate showcase and debug modes.

## Mistake 12

Trying to communicate the entire system simultaneously.

### Correction

Use attention management.

---

# 41. MASTER DEMO CHOREOGRAPHY

A high-quality presentation sequence should feel intentional.

## 00:00 - 00:05

Silence.

Dark world.

Pakistan origin only.

## 00:05 - 00:12

Student mission appears.

Commander materializes.

## 00:12 - 00:20

Commander decides.

## 00:20 - 00:30

Discovery Commander receives command.

## 00:30 - 00:55

Regional fleet deployment.

## 00:55 - 01:30

Research activity.

## 01:30 - 02:00

Candidate emergence.

## 02:00 - 02:30

Eligibility, cost, deadline.

## 02:30 - 03:05

Verification and Skeptic.

## 03:05 - 03:30

Resolution.

## 03:30 - 03:50

Ranking change.

## 03:50 - 04:40

Dossier build.

## 04:40 - 05:00

PDF generation.

## 05:00 - 05:20

Judge interaction.

---

# 42. FINAL NORTH STAR

SCHOLARX should not look like software that has been decorated to look futuristic.

It should feel like the visual interface of an autonomous intelligence organization.

The most important visual object is not the card.

It is not the map.

It is not the dashboard.

It is the **relationship between agents**.

A Commander gives a mission.

A child acknowledges.

A child travels.

A child investigates.

A child returns evidence.

The Commander reacts.

The organization expands.

The organization challenges itself.

The organization changes its mind when evidence changes.

Then the organization turns its conclusion into something useful for a human.

That is ScholarX.

---

# 43. FINAL EXHIBITION RULES

1. No generic dashboard.
2. No permanent telemetry wall.
3. No tiny map.
4. No equal grid of cards.
5. No fake communication.
6. No giant uncontrolled text blocks.
7. No excessive neon.
8. No faux-military typography.
9. No unexplained developer controls.
10. No phase skipping.
11. No large implementation jump without screenshot review.
12. No moving to the next phase unless the current phase passes its hard gate.
13. No sacrificing readability for complexity.
14. No sacrificing causality for decoration.
15. No treating the frontend as a status display.
16. The interface must visibly show autonomous work.
17. Every important animation must communicate something.
18. The world map must remain legible.
19. The first four phases must establish the visual DNA of the whole project.
20. The final question is always:

> **Can a stranger understand what the AI organization is doing by watching the screen?**

If not, the design is not finished.

---

# 44. FINAL IMPLEMENTATION CHECKLIST

## Phase 1

[ ] Visual reset complete
[ ] Glass system complete
[ ] Typography complete
[ ] Motion primitives complete
[ ] No dashboard regression
[ ] Screenshot approved

## Phase 2

[ ] World stage complete
[ ] Pakistan origin visible
[ ] Regional coordinates stable
[ ] Map readable at distance
[ ] Camera/focus system working
[ ] Screenshot approved

## Phase 3

[ ] Commander complete
[ ] AgentCard complete
[ ] Lifecycle states complete
[ ] Dynamic spawn complete
[ ] Screenshot approved

## Phase 4

[ ] Command packet
[ ] Ack packet
[ ] Search sequence
[ ] Source discovery
[ ] Candidate emergence
[ ] Report assembly
[ ] Report return
[ ] Commander reaction
[ ] 3-meter test passed

## Phase 5

[ ] Europe
[ ] Asia
[ ] MENA
[ ] Americas
[ ] Oceania
[ ] Fleet choreography
[ ] Research workspaces
[ ] Screenshot approved

## Phase 6

[ ] Eligibility
[ ] Cost
[ ] Deadline
[ ] Verification
[ ] Skeptic
[ ] Evidence
[ ] Resolution

## Phase 7

[ ] Synthesis
[ ] Ranking
[ ] Rank movement
[ ] Dossier page
[ ] Field injection
[ ] PDF

## Phase 8

[ ] Event normalizer
[ ] Lifecycle store
[ ] Presentation queue
[ ] TheatreDirector
[ ] Demo/live parity
[ ] Real SSE

## Phase 9

[ ] Judge mode
[ ] Constraint injection
[ ] Error handling
[ ] Cache fallback
[ ] Performance budget
[ ] Showcase/debug separation

## Phase 10

[ ] 3-meter test repeated
[ ] Non-developer test
[ ] Full demo rehearsal
[ ] PDF validation
[ ] No dashboard regression
[ ] Visual lock
[ ] Exhibition-ready

---

# 45. OFFICIAL BUILDING PRINCIPLE

Build one phase.

Inspect it.

Show it.

Correct it.

Lock it.

Then continue.

Do not let the coding agent disappear for hours and return with the entire application changed.

The quality of ScholarX will come from controlled visual iteration.

**Phase by phase. Scene by scene. Interaction by interaction.**

---

# END OF NEW DESIGN GUIDE

---

# APPENDIX A. PHASE DELIVERY CONTRACTS

This appendix converts the ten phases into concrete contracts the coding agent can execute one at a time.

## A.1 Phase 1 delivery contract

### Inputs

- current frontend
- current global CSS
- existing component primitives

### Outputs

- theatre root
- visual tokens
- glass primitive
- type system
- animation token registry

### Must not change

- backend
- event schema
- ranking logic
- scholarship data

### Required screenshot

One static Commander and one static child agent over the dark world environment.

### Approval question

Does this look like a premium AI theatre rather than a SaaS dashboard?

---

## A.2 Phase 2 delivery contract

### Inputs

Phase 1 visual system.

### Outputs

- world stage
- map projection
- Pakistan anchor
- regional anchor system
- route system
- camera/focus system

### Required screenshot

Pakistan at center of a visually dominant world map with empty space for future agent activity.

### Approval question

Does the map feel like the environment in which the AI operates?

---

## A.3 Phase 3 delivery contract

### Outputs

- Commander
- AgentCard
- lifecycle state engine
- spawn animation
- focus behavior

### Required screenshot

Commander plus one child agent, both active, with visible parent-child relationship.

### Approval question

Can a viewer identify the authority and the subordinate without reading a technical diagram?

---

## A.4 Phase 4 delivery contract

### Outputs

- PacketCanvas
- command
- acknowledgement
- report
- complete proof sequence

### Required video/screen recording

20 to 40 seconds showing the complete interaction.

### Hard gate

3-meter test.

### Approval question

Can a stranger describe what happened after watching it once?

---

## A.5 Phase 5 delivery contract

### Outputs

- five regional workflows represented spatially
- deployment sequence
- research workspaces
- controlled parallelism

### Required screenshot

All five regions visibly active without producing dashboard clutter.

### Approval question

Does the organization feel larger without becoming less understandable?

---

## A.6 Phase 6 delivery contract

### Outputs

- candidate flow
- eligibility
- cost
- deadline
- verification
- skeptic
- evidence

### Required screenshot

A candidate being challenged and resolved.

### Approval question

Can a judge understand why the recommendation changed?

---

## A.7 Phase 7 delivery contract

### Outputs

- ranking
- dossier builder
- generated webpage
- PDF

### Required artifact

A real downloaded PDF.

### Approval question

Would a real student want to receive this document?

---

## A.8 Phase 8 delivery contract

### Outputs

- live SSE adapter
- event normalizer
- lifecycle store
- presentation queue
- TheatreDirector

### Required test

Demo events and real events produce the same visual sequence.

### Approval question

Can the backend run faster without causing the story to become unreadable?

---

## A.9 Phase 9 delivery contract

### Outputs

- Judge Mode
- cached fallback
- failure states
- performance optimization
- debug/showcase modes

### Required test

Interrupt a live mission and show graceful recovery.

### Approval question

Would the system survive a real exhibition environment?

---

## A.10 Phase 10 delivery contract

### Outputs

- final art direction
- final timing
- final typography
- final sound behavior
- final rehearsal build

### Required test

Complete mock judging session.

### Approval question

Would we be comfortable showing this without explaining every screen ourselves?

---

# APPENDIX B. MASTER ANIMATION TIMING TABLE

The exact duration may vary with scene scale, but the relative rhythm should remain stable.

| Interaction | Typical duration | Purpose |
|---|---:|---|
| Commander wake | 500-800ms | establish authority |
| Commander decision reveal | 900-1400ms | allow reading |
| Command packet form | 350-550ms | establish message |
| Short command travel | 700-1000ms | spatial relation |
| Long command travel | 1000-1500ms | geography |
| Agent receive pulse | 300-450ms | confirm reception |
| Acknowledgement reveal | 450-700ms | establish causality |
| Ack return | 500-900ms | close command loop |
| Agent work transition | 400-700ms | state change |
| Query reveal | 500-900ms | show task |
| Source arrival | 350-600ms | show discovery |
| Candidate emergence | 500-900ms | create object |
| Report assembly | 900-1600ms | summarize work |
| Report return | 900-1500ms | show parent communication |
| Parent reaction | 700-1100ms | decision point |
| Region deployment | 800-1400ms | geographic movement |
| Rank transition | 600-1200ms | decision change |
| Dossier section injection | 500-900ms | artifact creation |
| Dossier transition | 1200-2000ms | switch worlds |
| PDF preparation | 1000-1800ms | completion |

## B.1 Timing rule

Never choose animation duration merely because it looks smooth.

Choose duration based on how much information the audience must understand during that motion.

## B.2 Reading hold

After an important result arrives, reserve a reading hold.

Example:

`REPORT RECEIVED`

Hold 1100ms.

Only then move to the next event.

---

# APPENDIX C. MASTER AGENT STATE TABLE

| State | Visual treatment | Card message | Packet allowed | Focus |
|---|---|---|---|---|
| IDLE | dim glass | waiting | no | ambient |
| RECEIVING | edge glow | command received | yes | secondary |
| ACKNOWLEDGING | soft pulse | task accepted | yes | primary |
| DEPLOYING | travel emphasis | deploying | yes | primary |
| SEARCHING | internal activity | searching | no | primary |
| READING | source highlight | reading source | no | primary |
| EXTRACTING | field reveal | extracting | no | primary |
| NORMALIZING | field collapse | normalizing | no | primary |
| ANALYZING | controlled pulse | analyzing | optional | primary |
| VERIFYING | evidence glow | verifying | yes | primary |
| REPORTING | card compresses | report ready | yes | primary |
| RETURNING | report packet | returning | yes | primary |
| COMPLETE | soft stable glow | complete | optional | supporting |
| BLOCKED | amber lock | blocked | yes | primary |
| FAILED | muted red edge | failed | yes | primary |
| RECOVERING | amber to cyan | recovering | yes | primary |
| CACHED | restrained violet-gray marker | cache used | optional | secondary |

---

# APPENDIX D. MASTER PACKET SPECIFICATION

## D.1 Command packet data

```text
packetId
sessionId
senderId
receiverId
type
priority
timestamp
summary
payloadRef
presentationDuration
```

## D.2 Acknowledgement packet data

```text
packetId
senderId
receiverId
type
accepted
summary
```

## D.3 Report packet data

```text
packetId
senderId
receiverId
type
candidateCount
verifiedCount
highRelevanceCount
keyFinding
reportRef
```

## D.4 Visual rules

The packet must always expose sender and receiver when selected.

Do not encode too much information into the packet itself.

The packet is a visual messenger, not a database view.

---

# APPENDIX E. MASTER PRESENTATION EVENT SCHEMA

The theatre layer should normalize backend activity into a stable presentation schema.

```text
presentationEventId
missionId
timestamp
sourceEventId
eventType
importance
phase
sourceEntityId
targetEntityId
regionId
scholarshipId
payload
minimumDisplayMs
holdAfterMs
coalesceKey
focusTarget
cameraMode
```

## E.1 Example

```json
{
  "eventType": "COMMAND_TRAVEL",
  "importance": "HERO",
  "sourceEntityId": "commander",
  "targetEntityId": "europe_scout",
  "regionId": "europe",
  "minimumDisplayMs": 900,
  "holdAfterMs": 400,
  "focusTarget": "europe_scout",
  "cameraMode": "regional"
}
```

This is intentionally a presentation model, not a backend model.

---

# APPENDIX F. MASTER EVENT MAPPING

| Backend concept | Theatre representation |
|---|---|
| MISSION_INITIATED | Commander wakes |
| PHASE_TRANSITION | mission atmosphere shifts |
| AGENT_SPAWNED | agent materializes |
| AGENT_COMPLETED | agent settles |
| SCOUT_DEPLOYED | regional route launches |
| SEARCH_QUERY_EXECUTED | query active |
| PAGE_SCRAPED | source object appears |
| CANDIDATE_EXTRACTED | scholarship object emerges |
| DUPLICATE_DETECTED | candidate merges |
| ELIGIBILITY_CHECK_STARTED | analysis node opens |
| DIMENSION_EVALUATED | criterion resolves |
| ELIGIBILITY_PASS | criterion locks green |
| ELIGIBILITY_FAIL | criterion locks red |
| DOCUMENT_REQUIREMENT_PARSED | requirement enters dossier |
| READINESS_SCORE_CALCULATED | readiness meter updates |
| VERIFICATION_STARTED | verification node activates |
| SKEPTIC_CHALLENGE | challenge packet launches |
| CHALLENGE_RESOLVED | evidence closes loop |
| SCORE_UPDATED | candidate score animates |
| MISSION_COMPLETE | completion state |

The exact backend event names must come from the actual project implementation.

Never invent an event name in the live adapter without checking the backend contract.

---

# APPENDIX G. MASTER SCENE STATE MODEL

```text
SceneState
  mission
  globalFocus
  worldMode
  commander
  activeAgents[]
  routes[]
  packets[]
  sources[]
  candidates[]
  analyses[]
  debates[]
  rankings[]
  dossier
  queue
  presentationSpeed
  paused
  showcaseMode
```

## G.1 Principle

Scene state is a projection of intelligence and presentation state.

Do not put raw backend response objects everywhere in components.

---

# APPENDIX H. VISUAL TOKEN STARTING POINT

The following are starting points, not absolute values.

## H.1 Surface tokens

```text
--sx-black: #05070A
--sx-deep: #080C10
--sx-panel: #0B1117
--sx-glass: rgba(12,18,24,0.58)
--sx-glass-strong: rgba(12,18,24,0.76)
--sx-border: rgba(180,210,225,0.14)
--sx-border-active: rgba(110,225,255,0.34)
```

## H.2 Semantic tokens

```text
--sx-command: muted warm gold
--sx-flow: cool cyan
--sx-verified: emerald
--sx-warning: amber
--sx-challenge: muted crimson
--sx-text: high-contrast neutral
--sx-muted: subdued cool gray
```

Exact final values should be tuned visually.

## H.3 Radius

Use moderate radius.

Avoid both extreme sharpness and overly rounded SaaS cards.

## H.4 Shadow

Prefer large soft shadows.

Avoid dark hard outlines that make every card look like a separate box.

---

# APPENDIX I. TYPOGRAPHY SCALE AT 1920X1080

These are starting points.

### Mission title

40-56px.

### Commander name

28-38px.

### Agent name

22-30px.

### Mission statement

17-22px.

### Operational state

15-19px.

### Technical metadata

11-14px.

### Micro metadata

10-12px only when non-essential.

## I.1 Typography rule

If a judge must squint to understand the core story, the type is too small.

---

# APPENDIX J. CARD CONTENT RULES

## J.1 Maximum core content

An active agent card should usually display no more than:

1 identity line

1 mission line

1 current operation

1 tool/query block

1 finding block

1 progress state

Everything else belongs behind inspection.

## J.2 Empty states

Do not show empty dashboards with `0` metrics.

Use language:

`AWAITING TASK`

`NO ACTIVE MISSION`

rather than a wall of zeros.

---

# APPENDIX K. RESEARCH WORKSPACE DETAILS

## K.1 Tool chip

Shows:

- tool name
- current state
- operation summary

## K.2 Source chip

Shows:

- domain
- source class
- relevance

## K.3 Extraction field

Shows:

- field
- value
- confidence when relevant

## K.4 Candidate object

Shows:

- scholarship name
- country
- funding
- initial relevance

## K.5 Workspace cleanup

Once a report is finalized, transient search objects fade or collapse.

Do not leave every past source floating forever.

This is essential to prevent scene overload.

---

# APPENDIX L. INFORMATION LIFETIME MODEL

Every visual object has a lifetime.

### Persistent

Commander

world

mission identity

selected agent

### Session-persistent

selected scholarship

major findings

ranked result

### Temporary

packet

source chip

search pulse

tool operation

candidate emergence animation

### Ephemeral

hover effect

highlight

micro pulse

This hierarchy prevents the screen from accumulating clutter.

---

# APPENDIX M. CARD MOVEMENT RULES

## M.1 Do not teleport

Cards should animate into meaningful locations.

## M.2 Do not endlessly float

Once a card arrives, it should stabilize.

## M.3 Repositioning

Use spring motion when the stage must accommodate new entities.

## M.4 Focus movement

When a new hero object appears:

- dim unrelated region
- reposition gently if needed
- bring new object into visual prominence

Do not snap the entire scene unless the mission state truly changes.

---

# APPENDIX N. SIMULTANEOUS AGENT RULES

When five scouts work simultaneously:

### Hero scout

100% visual strength.

### Secondary scouts

60-75% strength.

### Background scouts

30-45% strength.

The exact values depend on the visual result.

## N.1 Focus rotation

Use controlled focus cycling.

Example:

Europe 4 seconds

Asia 3 seconds

MENA 3 seconds

Return to Europe on important result.

The viewer should never lose the overall stage.

---

# APPENDIX O. DOSSIER CONTENT VALIDATION

Before allowing PDF generation, verify:

[ ] scholarship identity
[ ] country
[ ] institution
[ ] degree
[ ] field
[ ] funding
[ ] eligibility
[ ] Pakistan eligibility
[ ] documents
[ ] deadline
[ ] official portal
[ ] how to apply
[ ] costs
[ ] evidence
[ ] verification status
[ ] skeptic result
[ ] roadmap

If a field is unavailable, explicitly label it as unavailable or unconfirmed.

Never fabricate missing information just to make the dossier look complete.

---

# APPENDIX P. DEMO EVENT SCRIPT TEMPLATE

The following is a template for deterministic presentation testing.

```text
00.000 MISSION_INITIATED
02.000 COMMANDER_THINKING
05.000 COMMANDER_DECISION
07.000 COMMAND_ISSUED
08.000 COMMAND_PACKET_FORMED
09.000 COMMAND_PACKET_DEPARTS
10.100 COMMAND_RECEIVED
11.000 ACK_CREATED
11.500 ACK_DEPARTS
12.300 ACK_RECEIVED
14.000 SEARCH_STARTED
16.000 SEARCH_QUERY_VISIBLE
18.000 SOURCE_DISCOVERED
20.000 SOURCE_READ
22.000 CANDIDATE_EXTRACTED
24.000 SECOND_SOURCE_DISCOVERED
26.000 NORMALIZATION_STARTED
28.000 REPORT_ASSEMBLY_STARTED
31.000 REPORT_READY
32.000 REPORT_PACKET_FORMED
33.000 REPORT_DEPARTS
34.400 REPORT_RECEIVED
36.000 COMMANDER_SYNTHESIZING
38.000 NEXT_TASK_ISSUED
```

This is not the live backend timeline.

It is a presentation test fixture.

---

# APPENDIX Q. VISUAL DEBUG CHECKLIST

When a scene feels wrong, check in this order.

## Q.1 Composition

Is the hero object clear?

## Q.2 Scale

Is the map too small?

## Q.3 Spacing

Are cards too close?

## Q.4 Typography

Is there too much text?

## Q.5 Color

Are too many semantic colors active?

## Q.6 Motion

Does motion explain causality?

## Q.7 Timing

Is there enough time to read?

## Q.8 Attention

Are too many objects competing?

## Q.9 Story

Can a stranger describe what happened?

---

# APPENDIX R. CODE REVIEW CHECKLIST

Before accepting a phase:

[ ] no unnecessary dependencies
[ ] TypeScript strictness preserved
[ ] no unbounded animation loops
[ ] no hidden network calls from visual components
[ ] no API keys in frontend
[ ] no direct business logic in presentational components
[ ] no duplicated event parsing
[ ] no accidental backend semantics changed
[ ] responsive viewport handled
[ ] reduced-motion behavior considered
[ ] debug instrumentation available
[ ] screenshot reviewed

---

# APPENDIX S. ANIMATION ANTI-PATTERNS

Never do the following.

## S.1 Glowing for no reason

If everything glows, nothing has emphasis.

## S.2 Constant movement

A calm agent at rest should look calm.

## S.3 Random particles

Particles do not substitute for a communication model.

## S.4 Giant map pulses

The map should communicate geography, not act like a loading spinner.

## S.5 Card bouncing

Avoid playful bouncing.

## S.6 Terminal typing everywhere

Not everything needs a typewriter effect.

## S.7 Excessive camera motion

Camera movement should clarify the story.

## S.8 Simultaneous hero events

Do not make five major events happen with equal visual force.

---

# APPENDIX T. THE FINAL CREATIVE STANDARD

Ask these questions before accepting any screen.

### Is it beautiful?

If not, improve the composition.

### Is it understandable?

If not, simplify.

### Is it believable?

If not, connect the visual to real state.

### Is it distinctive?

If not, remove generic dashboard conventions.

### Does it show intelligence?

If not, expose a meaningful relationship or decision.

### Does it work from three meters?

If not, increase hierarchy and reduce noise.

### Does it feel premium?

If not, reduce effects and improve typography, spacing, and materials.

---

# FINAL OPERATIONAL RULE

**Only one phase is active at a time.**

The coding agent receives the master guide plus the explicit phase number.

The coding agent:

1. audits the current code for that phase
2. implements only that phase
3. runs checks
4. launches the frontend
5. captures a 1920x1080 screenshot
6. reports what changed
7. reports what remains
8. stops

The human reviews the screen.

If approved, the next phase begins.

If rejected, the same phase is revised.

No phase is considered complete because code compiles.

A phase is complete only when its **visual, behavioral, and exhibition acceptance criteria** pass.

---

# END

SCHOLARX should ultimately make the audience think:

> **"I am not watching a dashboard. I am watching an AI organization work."**

That is the standard this document is designed to enforce.
