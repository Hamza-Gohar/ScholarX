"""
ScholarX Presentation Manifest
Declarative content definition for the 8 Exhibition Slides.
Designed using the Minimalist Korean Aesthetic Design System.
"""

DECK_METADATA = {
    "title": "ScholarX — Autonomous Scholarship Intelligence Network",
    "theme": "Minimalist Korean Aesthetic",
    "target_audience": "Exhibition Judges, Academic Evaluators, and Pakistani Students",
    "aspect_ratio": "16:9",
}

SLIDES = [
    {
        "slide_number": 1,
        "type": "hero_cover",
        "category": "AUTONOMOUS SCHOLARSHIP INTELLIGENCE NETWORK",
        "title_dark": "SCHOLAR",
        "title_accent": "X",
        "subtitle": "Discovering, verifying, and matching fully funded global opportunities for Pakistani students — with zero hidden cost surprises.",
        "highlights": [
            {
                "badge": "01",
                "title": "Pakistan-Aware",
                "desc": "Built for HEC HAT/USAT, IBCC equivalence & MOFA lead times."
            },
            {
                "badge": "02",
                "title": "Bilateral Quotas",
                "desc": "Unlocks 400+ Hungarian, 200+ Chinese & Turkiye seats."
            },
            {
                "badge": "03",
                "title": "True Cost (PKR)",
                "desc": "Real out-of-pocket costs: IELTS, visas, attestation, travel."
            }
        ]
    },
    {
        "slide_number": 2,
        "type": "concept_split",
        "category": "FOUNDATIONAL INTELLIGENCE",
        "title_dark": "WHAT IS AN",
        "title_accent": "AI AGENT?",
        "subtitle": "Beyond static chatbots: Autonomous, goal-driven digital problem solvers.",
        "core_definition": {
            "headline": "Goal-Driven Autonomy with Tool Use & Reasoning",
            "text": "An AI Agent is an autonomous software entity powered by a Large Language Model. Given a high-level mission, it perceives unstructured inputs, deliberates on next actions, interacts with live digital environments via tools, and self-corrects on failures without requiring continuous human prompting."
        },
        "pillars": [
            {
                "badge": "01",
                "title": "Perception & Ingestion",
                "desc": "Reads messy PDFs, transcripts, and foreign university portals to construct structured mental models."
            },
            {
                "badge": "02",
                "title": "Dynamic Deliberation",
                "desc": "Formulates multi-step plans, adjusts search queries on the fly, and recovers when a path fails."
            },
            {
                "badge": "03",
                "title": "Active Tool Execution",
                "desc": "Executes live web searches, scrapes portal tables, runs code, and calls external verification APIs."
            },
            {
                "badge": "04",
                "title": "Persistent Memory",
                "desc": "Remembers past student sessions, recalls previous scholarship audits, and compounds intelligence."
            }
        ]
    },
    {
        "slide_number": 3,
        "type": "concept_split",
        "category": "DETERMINISTIC RELIABILITY",
        "title_dark": "WHAT IS A",
        "title_accent": "WORKFLOW?",
        "subtitle": "Predictable, zero-hallucination pipelines engineered for precision.",
        "core_definition": {
            "headline": "Deterministic, High-Speed Sequential Logic",
            "text": "A Workflow is a rigid, programmatic sequence of predefined steps where every branch and transformation is governed by hardcoded business logic, database lookups, and deterministic arithmetic. Given identical inputs, a workflow guarantees identical, mathematically verifiable outputs."
        },
        "pillars": [
            {
                "badge": "01",
                "title": "Zero Hallucination",
                "desc": "Eliminates AI guessing in mission-critical criteria checks, eligibility rules, and financial math."
            },
            {
                "badge": "02",
                "title": "Sub-Millisecond Latency",
                "desc": "Executes data transforms, table joins, and date calculations without costly LLM roundtrips."
            },
            {
                "badge": "03",
                "title": "100% Reproducibility",
                "desc": "Guarantees consistent, audit-compliant outcomes every time for student eligibility verification."
            },
            {
                "badge": "04",
                "title": "Zero Token Cost",
                "desc": "Conserves expensive API tokens for creative reasoning by delegating logic to fast local code."
            }
        ]
    },
    {
        "slide_number": 4,
        "type": "comparison_matrix",
        "category": "THE ARCHITECTURAL PARADIGM",
        "title_dark": "AGENTS VS. WORKFLOWS",
        "title_accent": "THE HYBRID FORMULA",
        "subtitle": "Workflow-first philosophy: combining cognitive reasoning with deterministic precision.",
        "agent_side": {
            "badge": "AI AGENTS",
            "subtitle": "Use when judgment, fuzzy input, or dialogue is needed",
            "points": [
                "Parsing damaged, low-res matric & inter transcripts",
                "Formulating dynamic scout search strategies",
                "Adversarial verification & skeptic challenge",
                "Crafting personalized student guidance narratives"
            ]
        },
        "workflow_side": {
            "badge": "WORKFLOWS",
            "subtitle": "Use when logic is deterministic, arithmetic, or sequential",
            "points": [
                "Scrape -> Clean -> Normalize regional university data",
                "15-point strict eligibility qualification matrix",
                "Real PKR out-of-pocket budget calculations",
                "Deadline risk scoring formula & weighted ranking"
            ]
        },
        "synergy_callout": {
            "title": "The ScholarX Synergy (5 Agents + 7 Workflows)",
            "desc": "Agents provide cognitive perception and adversarial skepticism; Workflows provide lightning speed, mathematical truth, and zero hallucination. Coordinated seamlessly in LangGraph."
        }
    },
    {
        "slide_number": 5,
        "type": "innovation_showcase",
        "category": "GLOBAL EXCELLENCE",
        "title_dark": "A WORLD-FIRST INNOVATION",
        "title_accent": "FOR PAKISTAN",
        "subtitle": "No system on earth has ever combined multi-agent intelligence with Pakistan-specific realities.",
        "cards": [
            {
                "badge": "01",
                "title": "Pakistan Credential Context",
                "desc": "Understands HEC HAT/USAT benchmarks, IBCC 12-year equivalence rules, and MOFA seal requirements that generic platforms fail to recognize."
            },
            {
                "badge": "02",
                "title": "Unclaimed Bilateral Quotas",
                "desc": "Discovers 400+ Hungarian, 200+ Chinese CSC, and Romanian government seats allocated specifically for Pakistani nationals that go unnoticed."
            },
            {
                "badge": "03",
                "title": "True PKR Cost Deconstruction",
                "desc": "Unmasks the myth of '100% Free'. Calculates upfront PKR requirements (PKR 76k IELTS, visa fees, document attestation, medical tests)."
            },
            {
                "badge": "04",
                "title": "Adversarial Skeptic Audit",
                "desc": "First platform featuring a dedicated Skeptic Agent that actively attempts to disqualify matches, preventing students from scam application portals."
            }
        ]
    },
    {
        "slide_number": 6,
        "type": "architecture_topology",
        "category": "SYSTEM SPECIFICATION",
        "title_dark": "SYSTEM ARCHITECTURE",
        "title_accent": "MULTI-AGENT NETWORK",
        "subtitle": "Local-first orchestration combining 5 specialized agents with 7 deterministic workflows.",
        "tiers": [
            {
                "level": "ORCHESTRATION",
                "name": "Commander Orchestrator (LangGraph StateGraph)",
                "role": "Root mission controller, DAG execution manager, dynamic failure recovery & session persistence."
            },
            {
                "level": "PERCEPTION & SCOUTING",
                "name": "Profile Analyst Agent + Regional Scout Workflows",
                "role": "Multimodal PDF document extraction -> Parallel European, Asian, American & MENA scrapers."
            },
            {
                "level": "VERIFICATION & ADVERSARIAL",
                "name": "Eligibility Workflow + Skeptic Agent + Verification Agent",
                "role": "15-point criteria gatekeeper + Adversarial cross-examination challenging every scholarship claim."
            },
            {
                "level": "FINANCIAL & STRATEGY",
                "name": "True Cost (PKR) + Deadline Intelligence + Final Advisor",
                "role": "Deterministic fee calculations + Weighted ranking engine + Tailored action roadmap."
            }
        ]
    },
    {
        "slide_number": 7,
        "type": "workflow_pipeline",
        "category": "END-TO-END EXECUTION",
        "title_dark": "SYSTEM WORKFLOW",
        "title_accent": "THE SCHOLARSHIP PIPELINE",
        "subtitle": "How ScholarX turns raw student documents into an audited, personalized application roadmap.",
        "steps": [
            {
                "step": "01",
                "title": "Profile Ingestion",
                "desc": "Multimodal parsing of messy transcripts & documents."
            },
            {
                "step": "02",
                "title": "Scout Dispatch",
                "desc": "Parallel regional workflows scan Hungarian, Asian & EU portals."
            },
            {
                "step": "03",
                "title": "Eligibility Gate",
                "desc": "Deterministic 15-rule check (grades, age, HEC/IBCC limits)."
            },
            {
                "step": "04",
                "title": "Skeptic Audit",
                "desc": "Adversarial cross-check against fake & expired quotas."
            },
            {
                "step": "05",
                "title": "Cost & Risk Math",
                "desc": "True PKR fee computation & timeline countdown engine."
            },
            {
                "step": "06",
                "title": "Action Roadmap",
                "desc": "Evidence-backed ranking & personalized guidance plan."
            }
        ]
    },
    {
        "slide_number": 8,
        "type": "benefits_impact",
        "category": "STUDENT EMPOWERMENT",
        "title_dark": "STUDENT IMPACT",
        "title_accent": "TRANSFORMING ACCESS",
        "subtitle": "Democratizing global education access for Pakistan's next generation of scholars.",
        "benefits": [
            {
                "badge": "01",
                "stat": "PKR 300,000+",
                "title": "Saved in Consultant & Hidden Fees",
                "desc": "Protects middle-class Pakistani families from predatory educational agents and unbudgeted application costs."
            },
            {
                "badge": "02",
                "stat": "600+ SEATS",
                "title": "Unclaimed Bilateral Quotas Reclaimed",
                "desc": "Empowers talented students from small cities to claim reserved government quotas in Hungary, China, Turkey & Europe."
            },
            {
                "badge": "03",
                "stat": "100% PROVEN",
                "title": "Evidence-Backed Audit & Total Privacy",
                "desc": "Zero black-box recommendations. Every suggestion links directly to official circulars, running 100% locally on your machine."
            }
        ]
    },
    {
        "slide_number": 9,
        "type": "team_credits",
        "category": "THE MINDS BEHIND SCHOLARX",
        "title_dark": "THE CREATORS",
        "title_accent": "& LEADERSHIP",
        "subtitle": "The student innovators and academic mentorship behind Pakistan's first autonomous scholarship network.",
        "developers": [
            {
                "badge": "01",
                "role_tag": "LEAD CREATOR & SYSTEM ARCHITECT",
                "name": "M. Hamza Gohar",
                "desc": "Conceived, designed, and built ScholarX. Engineered the multi-agent LangGraph orchestration, autonomous scout pipelines, and backend intelligence network."
            },
            {
                "badge": "02",
                "role_tag": "FRONTEND & DESIGN CONTRIBUTOR",
                "name": "Malik Hassan",
                "desc": "Contributed to frontend interface implementation, user dashboard layout components, and visual styling."
            }
        ],

        "supervisor": {
            "badge": "SUPERVISED BY",
            "name": "Sir Kaleem",
            "role_tag": "ACADEMIC SUPERVISOR & RESEARCH ADVISOR",
            "desc": "Guided architectural direction, algorithmic rigor, and system validation to ensure high-impact innovation for Pakistani students."
        }
    }
]

