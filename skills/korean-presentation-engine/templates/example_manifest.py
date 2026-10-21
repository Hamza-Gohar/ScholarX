"""
Starter Manifest Template
Copy and edit this file to generate a new Korean Minimalist presentation.
"""

DECK_METADATA = {
    "title": "My Presentation",
    "theme": "Minimalist Korean Aesthetic",
    "target_audience": "General Audience / Pitch Evaluators",
    "aspect_ratio": "16:9",
}

SLIDES = [
    {
        "slide_number": 1,
        "type": "hero_cover",
        "category": "PROJECT CATEGORY",
        "title_dark": "PRIMARY",
        "title_accent": "TITLE",
        "subtitle": "A concise mission statement explaining what the system accomplishes.",
        "highlights": [
            {"badge": "01", "title": "Core Feature", "desc": "Concise factual description of feature 1."},
            {"badge": "02", "title": "Fast & Reliable", "desc": "Concise factual description of feature 2."},
            {"badge": "03", "title": "Proven Impact", "desc": "Concise factual description of feature 3."}
        ]
    },
    {
        "slide_number": 2,
        "type": "concept_split",
        "category": "FOUNDATIONAL INTELLIGENCE",
        "title_dark": "WHAT IS THE",
        "title_accent": "CORE SYSTEM?",
        "subtitle": "Deep breakdown of the system principles and execution capabilities.",
        "core_definition": {
            "headline": "Autonomous High-Speed Architecture",
            "text": "Explain the core definition and foundational mechanism of your project here in clear, compelling, professional language."
        },
        "pillars": [
            {"badge": "01", "title": "First Pillar", "desc": "Detailed breakdown of the first pillar."},
            {"badge": "02", "title": "Second Pillar", "desc": "Detailed breakdown of the second pillar."},
            {"badge": "03", "title": "Third Pillar", "desc": "Detailed breakdown of the third pillar."},
            {"badge": "04", "title": "Fourth Pillar", "desc": "Detailed breakdown of the fourth pillar."}
        ]
    },
    {
        "slide_number": 3,
        "type": "benefits_impact",
        "category": "OUTCOMES & TRACTION",
        "title_dark": "MEASURABLE",
        "title_accent": "RESULTS",
        "subtitle": "Quantified outcomes and tangible real-world impact.",
        "benefits": [
            {
                "badge": "01",
                "stat": "10x FASTER",
                "title": "Speed Acceleration",
                "desc": "Delivers instant execution compared to traditional manual workflows."
            },
            {
                "badge": "02",
                "stat": "99.9%",
                "title": "Deterministic Accuracy",
                "desc": "Eliminates guessing with verified algorithmic precision."
            },
            {
                "badge": "03",
                "stat": "$0 SURPRISES",
                "title": "Transparent Cost",
                "desc": "Full visibility into every line item and out-of-pocket requirement."
            }
        ]
    }
]
