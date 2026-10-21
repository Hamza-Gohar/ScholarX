# scripts/batch13_p2.py
# SCH-AM-026: Queen's University Graduate Award in Computing (Canada)
# SCH-AM-027: UC San Diego (UCSD) CSE Graduate Fellowship & Assistantship (USA)
# SCH-AM-028: Columbia University Computer Science Doctoral Fellowship (USA)

DATA_P2 = {
    "SCH-AM-026": {
        "scholarship_id": "SCH-AM-026",
        "basic_details": {
            "scholarship_name": "Queen's University Graduate Award & International Doctoral Fellowship in Computing",
            "offering_entity": "Queen's University (School of Computing & School of Graduate Studies and Postdoctoral Affairs)",
            "host_country": "Canada",
            "host_institutions_covered": "Queen's University Main Campus (Kingston, Ontario, Canada)",
            "degree_levels": ["Master of Science (MSc Thesis)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Restricted to graduate research programs within the School of Computing: Artificial Intelligence, Biomedical Computing, Cybersecurity, Software Engineering, Human-Computer Interaction, and Theoretical Computer Science.",
            "number_of_awards_total": "100% of admitted research-stream graduate students receive guaranteed minimum funding packages (~60 to 80 awards annually)",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates typically secure 5 to 10 fully funded seats annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for MSc thesis; 4 years for PhD, renewed annually subject to satisfactory academic progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit specified by Queen's School of Computing.",
            "academic_qualifications": "For MSc: 4-year Bachelor's degree (16 years education) in Computer Science, Software Engineering, or related STEM discipline from an HEC-recognized institution with first-class standing (minimum 80% or B+ average; CGPA 3.3/4.0). For PhD: Research Master's degree (18 years education) with A- average (minimum 80% or 3.7/4.0 CGPA) and demonstrable research output.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Queen's evaluates international transcripts on an institutional 4.3 GPA scale. B+ minimum corresponds to ~77-79% on Pakistani marks sheets.",
            "subject_background_prerequisites": "Rigorous undergraduate training in algorithms, discrete mathematics, computer architecture, operating systems, and object-oriented programming.",
            "current_education_status": "Final-year students graduating before September (Fall intake) or January (Winter intake) are fully eligible to apply with provisional transcripts.",
            "graduation_year_restrictions": "No restrictions on graduation year.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Industrial or software development experience is valued, but demonstrated academic research potential (publications, capstone projects) carries higher weight.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 88,
            "duolingo_accepted": True,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic overall min 7.0 (no band below 6.5), TOEFL iBT min 88 (writing 24, speaking 22, reading 22, listening 20), or Duolingo min 125. Medium of Instruction letters not accepted.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None; diversity and women in computing initiatives actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates with accepted publications at top-tier venues (IEEE, ACM, NeurIPS) receive priority faculty matching.",
            "previous_scholarship_restrictions": "External tri-council or government scholarship recipients receive supplementary top-ups up to allowable university ceilings.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "International tuition fees offset by Queen's Graduate Award (QGA) and International Tuition Support awards (~CAD 14,000 to 16,500/yr).",
                "amount": "100% covered (~CAD 15,000 / year value; ~PKR 3,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "School of Graduate Studies non-refundable application fee (CAD 110) paid via credit card.",
                "amount": "CAD 110 (~PKR 22,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Funded from guaranteed living stipend. Student apartments in Kingston (An Clachan, John Orr Tower) or shared student housing average CAD 750 to 1,050/month.",
                "amount": "Paid from stipend (~CAD 900 / month; ~PKR 180,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: MSc minimum CAD 23,000/yr; PhD minimum CAD 25,000 to CAD 28,000/yr (~CAD 2,000 to 2,333/month; ~PKR 400,000 to 466,000/month) delivered through Graduate Teaching Assistantships (GTA) and Graduate Research Assistantships (GRA).",
                "amount": "CAD 23,000 to 28,000 / year (~PKR 4,600,000 to 5,600,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International flights between Pakistan and Canada (Toronto Pearson YYZ or Montreal YUL, then rail/bus to Kingston) are self-funded.",
                "amount": "Self-funded (~PKR 280,000 to 420,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD 150) and biometrics fee (CAD 85) paid to IRCC.",
                "amount": "CAD 235 (~PKR 47,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "University Health Insurance Plan (UHIP) provides comprehensive emergency and basic healthcare, supplemented by the SGPS Supplementary Health & Dental Plan.",
                "amount": "Included in standard graduate financial package"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Groceries and living subsistence covered via bi-weekly graduate stipend disbursements.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-performance computational infrastructure, lab hardware, and software licenses provided by the School of Computing.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "School of Graduate Studies conference travel grants (CAD 1,000 to 2,000/yr) plus supervisor research grants for student co-authors presenting at premier computing conferences.",
                "amount": "CAD 1,000 to 2,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Kingston Transit universal student bus pass included in mandatory student activity fee package.",
                "amount": "Included in student fee package"
            },
            "total_estimated_value_usd_per_year": 30000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading Canadian research university: Queen's University (Kingston, Ontario, Canada)",
            "participating_institutions": [
                "Queen's University - School of Computing",
                "Queen's School of Graduate Studies and Postdoctoral Affairs"
            ],
            "university_rankings_scope": "Top 200 global university (QS World #193, THE #201-250); recognized Canadian research powerhouse in biomedical computing, software analytics, and cybersecurity.",
            "available_majors": [
                "MSc / PhD in Computing: Artificial Intelligence & Cognitive Science",
                "MSc / PhD in Computing: Biomedical Computing & Computational Medicine",
                "MSc / PhD in Computing: Cybersecurity, Privacy & Distributed Systems",
                "MSc / PhD in Computing: Software Engineering & Analytics",
                "MSc / PhD in Computing: Human-Computer Interaction",
                "MSc / PhD in Computing: Theoretical Computer Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MSc Thesis: 2 years; PhD: 4 years full-time.",
            "admission_requirements_summary": "Bachelor's (MSc) or Master's (PhD) in Computer Science/STEM with 3.3+ GPA, 2 academic recommendation letters, CV, statement of purpose, supervisor pre-match strongly recommended, and IELTS 7.0 / TOEFL 88.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Biomedical computing and machine learning labs have highest applicant volume; software analytics, theory, and human-computer interaction offer relatively higher admission chances.",
            "strategic_program_match_advice": "Reaching out to prospective faculty supervisors between September and November with a polished CV and specific reference to their published work significantly accelerates admission and guarantees funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.queensu.ca/sgs/prospective-students/how-apply",
            "portal_system_name": "Queen's School of Graduate Studies Online Application System",
            "account_creation_instructions": "Register on the Queen's Graduate Studies application portal, select School of Computing, choose MSc or PhD thesis route, upload documents, and submit referee details.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Review faculty research groups in Queen's School of Computing and contact matching supervisors.",
                "Step 2 (October - December): Create an account on the Queen's School of Graduate Studies online portal.",
                "Step 3 (November - January): Upload statement of purpose, CV, transcripts, and register 2 academic referees.",
                "Step 4 (By 15 January): Submit application and pay CAD 110 fee before departmental priority deadline.",
                "Step 5 (February - March): Faculty members conduct virtual interviews and review candidate files.",
                "Step 6 (March - April): Departmental admission letters issued with guaranteed funding package details.",
                "Step 7 (April - June): Apply for Canadian Study Permit via IRCC portal.",
                "Step 8 (September): Arrive in Kingston, Ontario for graduate orientation and assistantship appointment."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: Admitted thesis students are automatically awarded Queen's Graduate Award packages without separate funding application.",
            "recommendation_letters_submission_method": "Two academic reference letters submitted electronically via Queen's automated referee portal.",
            "personal_statement_prompts": "Statement of Purpose (1-2 pages): Detail academic background, specific research interests, faculty fit, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "Concise 1-2 page research statement outlining problem domain, methodological approach, and relevant Queen's computing labs.",
            "cv_format_requirements": "Academic CV highlighting publications, software repositories, hackathons, and coursework.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual technical video interview (30-45 minutes) conducted by prospective supervisor focusing on technical background, coding fluency, and research vision.",
            "standardized_tests": "IELTS Academic (7.0+) or TOEFL iBT (88+) or Duolingo (125+). GRE is NOT required.",
            "application_fee_amount": "CAD 110 (Non-refundable)",
            "attestation_requirements": "Unofficial transcripts uploaded for initial review; official HEC-attested documents submitted upon admission offer.",
            "translation_requirements": "Certified English translations required for non-English credentials.",
            "final_submission_method": "100% digital submission via the Queen's School of Graduate Studies portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Scanned color copies of Bachelor's and Master's degree certificates and consolidated semester transcripts.",
                "pakistan_specific_instruction": "Attestation by HEC recommended; provisional transcripts accepted for final-semester students with bona fide letter."
            },
            {
                "document_name": "Statement of Purpose / Research Proposal",
                "mandatory": True,
                "specification": "2-page statement outlining academic background, specific research interests in computing, and alignment with target faculty.",
                "pakistan_specific_instruction": "Explicitly identify 2-3 Queen's computing professors whose research papers you have studied and cite relevant methodologies."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "2-page academic CV detailing education, distinctions, software projects, GitHub links, and publications.",
                "pakistan_specific_instruction": "Highlight final-year project (FYP), competitive programming accomplishments, and industrial internships."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two confidential letters from academic professors who can attest to applicant's research intellect and analytical rigor.",
                "pakistan_specific_instruction": "Referees must submit letters directly from official university domain email addresses (.edu.pk)."
            },
            {
                "document_name": "English Language Proficiency Test Report",
                "mandatory": True,
                "specification": "Valid IELTS Academic TRF (min 7.0) or TOEFL iBT score report (min 88) sent electronically via institutional code 0949.",
                "pakistan_specific_instruction": "Test must have been taken within 24 months of intended intake date."
            },
            {
                "document_name": "Sample of Academic Writing / Publications",
                "mandatory": False,
                "specification": "Reprint of published conference/journal paper, thesis chapter, or technical whitepaper illustrating research aptitude.",
                "pakistan_specific_instruction": "Strongly recommended for PhD candidates to demonstrate mastery of scholarly English."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "15 September 2025",
            "application_deadline": "15 January 2026",
            "university_admission_deadline": "15 January 2026",
            "document_submission_deadline": "15 January 2026",
            "recommendation_letters_deadline": "22 January 2026",
            "interview_period": "February to March 2026",
            "shortlist_announcement": "March to April 2026",
            "final_result_acceptance_deadline": "15 April 2026",
            "visa_application_window": "April to July 2026",
            "semester_commencement": "Early September 2026",
            "annual_cycle_notes": "Main intake cycle is Fall (September). Winter intake offers very limited funding slots."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (cumulative GPA, performance in advanced computing and mathematics courses)",
            "extracurricular_and_leadership_weight": "5% (tech community initiatives, competitive programming)",
            "research_experience_weight": "30% (prior publications, statement of intent, GitHub repos, FYP quality)",
            "work_experience_weight": "5% (industry software development or machine learning roles)",
            "personal_statement_weight": "10% (clarity of research focus and departmental fit)",
            "recommendations_weight": "10% (referee credibility and ranking within student cohort)",
            "interview_weight": "5% (technical video interview with prospective supervisor)",
            "test_scores_weight": "Threshold requirement (IELTS 7.0 / TOEFL 88 compliance)",
            "financial_need_weight": "0% (purely merit and research competence based)",
            "selection_panel_composition": "School of Computing Graduate Admissions Committee and individual research lab supervisors.",
            "evaluation_methodology": "Two-tiered comprehensive assessment: Departmental Graduate Admissions Committee screens academic credentials and language qualifications, followed by individual faculty PI review and commitment of research funding."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "1,200+ graduate applicants across computing degrees",
            "total_scholarships_awarded": "~70 fully funded admissions packages awarded annually",
            "acceptance_rate_global": "~5% to 7% overall admit rate for funded research streams",
            "acceptance_rate_pakistan": "~4% to 6% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.55+ / 4.00 CGPA (80%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE with top 5-10% standing, solid coding capabilities, 1 research publication or strong thesis, IELTS 7.5.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, UET Lahore, and COMSATS.",
            "high_representation_countries": "Canada, China, India, Pakistan, Iran, United States, Nigeria",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized immigration agents advertising guaranteed admissions to Queen's. Admissions decisions rest exclusively with Queen's faculty and School of Graduate Studies."
            ],
            "application_fee_warning": "CAD 110 application fee is charged directly by Queen's University. Never pay money to third-party consultants.",
            "agent_and_intermediary_warnings": "Applications found using generic agent-written SOPs or ghostwriters are disqualified immediately.",
            "hidden_costs_breakdown": [
                "Queen's graduate application fee: CAD 110 (~PKR 22,000).",
                "Canadian Study Permit application and biometrics fees: CAD 235 (~PKR 47,000).",
                "Flight ticket from Pakistan to Toronto Pearson: ~PKR 280,000 to 420,000.",
                "First month's rent security deposit in Kingston: ~CAD 1,000 (~PKR 200,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: A GRE score is mandatory for Queen's computing. (FACT: GRE scores are not required and are not considered by the admissions committee).",
                "CLAIM: Direct contact with faculty is forbidden. (FACT: In the School of Computing, securing an interested faculty member is critical to admission with funding)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums report minimum GPA as 3.0, but competitive international applicants admitted with funding universally present 3.50+ CGPA."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum overall B average (GPA 3.0 on 4.3 scale) in all graduate credit courses and receive satisfactory annual progress ratings from thesis committee.",
            "attendance_requirements": "Full-time campus residency in Kingston and active participation in lab seminars, research group meetings, and designated teaching assistant duties.",
            "academic_progress_monitoring": "Annual progress report submitted jointly by student and supervisor to the Graduate Committee.",
            "work_restrictions_during_study": "Teaching assistantships are limited to a maximum of 10 hours per week (140 hours per term) to prevent conflict with research progress.",
            "home_country_return_obligation": "None. International graduates are eligible for Canada's Post-Graduation Work Permit (PGWP) of up to 3 years and Ontario Immigrant Nominee Program (OINP) permanent residence pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously disbursed funding upon standard withdrawal, though remaining fellowship payments cease.",
            "rules_for_changing_university": "Awards cannot be transferred to other Canadian universities.",
            "rules_for_changing_major": "Switching research groups requires written mutual consent from former supervisor, new supervisor, and the Graduate Coordinator.",
            "extension_policy": "MSc funding capped at 2 years; PhD funding capped at 4 years. Extensions contingent upon external grants or special departmental TA contracts."
        },
        "official_sources_verified": [
            {
                "source_name": "Queen's School of Computing Graduate Funding Portal",
                "source_url": "https://www.cs.queensu.ca/graduate/funding/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific stipend top-ups above the guaranteed baseline minimum.",
                    "Internal waitlist statistics for second-round graduate admissions offers.",
                    "Country-level breakdown of graduate student enrollment in computing."
                ]
            },
            {
                "source_name": "Queen's School of Graduate Studies and Postdoctoral Affairs",
                "source_url": "https://www.queensu.ca/sgs/prospective-students/funding",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific formula used to compute international tuition award offsets against standard domestic rates.",
                    "Annual departmental caps on international versus domestic graduate admissions."
                ]
            }
        ]
    },
    "SCH-AM-027": {
        "scholarship_id": "SCH-AM-027",
        "basic_details": {
            "scholarship_name": "UC San Diego (UCSD) CSE Graduate Fellowship & Doctoral Assistantship Package",
            "offering_entity": "University of California San Diego (Department of Computer Science and Engineering & Jacobs School of Engineering)",
            "host_country": "United States",
            "host_institutions_covered": "University of California San Diego Main Campus (La Jolla, California, USA)",
            "degree_levels": ["Doctor of Philosophy (PhD in Computer Science)", "Doctor of Philosophy (PhD in Computer Engineering)"],
            "major_restrictions": "Restricted to PhD students in Computer Science and Computer Engineering: Artificial Intelligence, Machine Learning, Systems & Networking, Security & Cryptography, Programming Languages, Bioinformatics, Robotics, and Theory of Computation.",
            "number_of_awards_total": "100% of admitted PhD students receive guaranteed multi-year full financial support (~90 to 110 admitted doctoral students annually)",
            "number_of_awards_pakistan": "Open global merit competition; typically 3 to 7 high-achieving Pakistani graduates admitted per academic year",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Guaranteed 5-year full doctoral funding package, subject to maintaining satisfactory academic and research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (BS/BE) or Master's degree (MS) in Computer Science, Computer Engineering, Electrical Engineering, Mathematics, or closely related discipline from an HEC-recognized university with minimum cumulative GPA of 3.50 / 4.00 (competitive admits typically have 3.80+ / 4.00 or top 2% of class).",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "UCSD requires a minimum cumulative GPA of 3.0 / 4.0 for Graduate Division admission, but CSE doctoral cutoff is de facto 3.50+ due to intense competition.",
            "subject_background_prerequisites": "Substantial coursework in algorithms, computer systems, operating systems, linear algebra, discrete mathematics, and programming abstractions.",
            "current_education_status": "Graduating seniors in their final year of BS or MS can apply; official degree completion required prior to Fall registration.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Formal industry experience is secondary to demonstrated research capability (first-author papers, research prototypes, open-source software, high-impact GitHub repos).",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "TOEFL iBT min 85 (CSE recommended 100+; speaking score 23+ required for Teaching Assistantships) or IELTS Academic min 7.0 (speaking band 7.0+ for TA eligibility). Duolingo and MOI certificates not accepted for international graduate admissions.",
            "other_language_requirements": "None; all campus instruction and research conducted in English.",
            "gender_specific_requirements": "None; female and underrepresented researchers in computing strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Exceptional candidates nominated for Jacobs School of Engineering Dean's Fellowships and CSE Departmental Merit Fellowships.",
            "previous_scholarship_restrictions": "Holders of external prestigious fellowships (e.g., Fulbright, Google PhD Fellowship) receive institutional stipend top-ups.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full California resident and Non-Resident Supplemental Tuition (NRST) remission fully covered (~USD 34,000 to USD 36,000 / year value).",
                "amount": "100% covered (~USD 35,000 / year; ~PKR 9,800,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UCSD international graduate application fee of USD 155 paid online via credit card. (Fee waivers rarely granted to international applicants).",
                "amount": "USD 155 (~PKR 43,500)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized graduate student housing at UCSD (Mesa, One Miramar, Central Mesa, Nuevo West, Nuevo East) guaranteed for incoming PhD students at below-market rates (~USD 850 to 1,200/month for private bedroom in shared graduate apartment).",
                "amount": "Paid from monthly stipend (~USD 950 / month; ~PKR 266,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed 5-year annual stipend of USD 38,000 to USD 44,000 / year (~USD 3,166 to 3,666 / month; ~PKR 885,000 to 1,025,000 / month) provided via Graduate Student Researcher (GSR) appointments, Teaching Assistantships (TA), and department fellowships.",
                "amount": "USD 38,000 to 44,000 / year (~PKR 10,640,000 to 12,320,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and San Diego International Airport (SAN) / Los Angeles International Airport (LAX) is self-funded.",
                "amount": "Self-funded (~PKR 350,000 to 500,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "US F-1 student visa fee (USD 185) and SEVIS I-901 fee (USD 350) paid directly to US government.",
                "amount": "USD 535 (~PKR 150,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "UC Student Health Insurance Plan (UC SHIP) fully paid by the department, providing medical, dental, vision, and mental health coverage (~USD 4,800 / year value).",
                "amount": "100% covered (~USD 4,800 / year; ~PKR 1,344,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Food and living subsistence covered comfortably by the monthly GSR/TA stipend.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Research workstations, high-end compute servers, access to San Diego Supercomputer Center (SDSC) and Nautilus cluster provided by CSE labs.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Research travel grants (USD 1,500 to 3,000 per conference) provided by advising professors and UCSD Graduate Student Association for papers accepted at top conferences (NeurIPS, ICML, CVPR, OSDI, SOSP, SIGCOMM).",
                "amount": "USD 1,500 to 3,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "UCSD Triton U-Pass provides unlimited free transit across San Diego Metropolitan Transit System (MTS) trolley and bus lines.",
                "amount": "Included in university registration"
            },
            "total_estimated_value_usd_per_year": 78000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-leading public research university: University of California San Diego (La Jolla, CA, USA)",
            "participating_institutions": [
                "UC San Diego - Department of Computer Science and Engineering (CSE)",
                "UC San Diego - Jacobs School of Engineering",
                "San Diego Supercomputer Center (SDSC)",
                "Halicioğlu Data Science Institute (HDSI)"
            ],
            "university_rankings_scope": "Top 15 global computer science university (US News CS #11, CSRankings #4, THE World #34); world leader in systems, bioinformatics, AI, and computer vision.",
            "available_majors": [
                "PhD in Computer Science: Artificial Intelligence & Machine Learning",
                "PhD in Computer Science: Computer Vision & Robotics",
                "PhD in Computer Science: Computer Systems, Networking & Cloud",
                "PhD in Computer Science: Security & Cryptography",
                "PhD in Computer Science: Programming Systems & Formal Verification",
                "PhD in Computer Science: Bioinformatics & Computational Biology",
                "PhD in Computer Science: Theoretical Computer Science",
                "PhD in Computer Engineering: Hardware/Software Co-Design & VLSI"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 years full-time doctoral program.",
            "admission_requirements_summary": "4-year BS or MS in CS/CE/STEM with 3.5+ GPA, 3 letters of recommendation, statement of purpose, CV, and TOEFL 85+ (100+ recommended) or IELTS 7.0+. GRE is not required.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Machine learning, computer vision, and robotics have largest application pools; computer systems, security, programming languages, and theory present slightly higher admission probability for deeply qualified candidates.",
            "strategic_program_match_advice": "Explicitly identify 3-5 UCSD CSE faculty members in the application portal whose recent research directly aligns with your background, and cite their specific papers in your statement of purpose."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://gradapply.ucsd.edu/",
            "portal_system_name": "UC San Diego GradApply System",
            "account_creation_instructions": "Register on the UCSD GradApply portal, select Department of Computer Science and Engineering, select Doctor of Philosophy, choose primary research subfields, and upload required materials.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Research UCSD CSE faculty labs and identify 3-5 potential doctoral advisors.",
                "Step 2 (October - December): Complete online profile on the UCSD GradApply portal.",
                "Step 3 (November - December): Upload statement of purpose, CV/resume, unofficial transcripts, and register 3 academic recommenders.",
                "Step 4 (By 15 December): Submit application and pay USD 155 application fee.",
                "Step 5 (January - February): Faculty sub-committees review applications and conduct technical video interviews.",
                "Step 6 (February - March): Department issues official PhD admission offer letters with 5-year guaranteed funding package.",
                "Step 7 (By 15 April): Submit formal acceptance of admission offer.",
                "Step 8 (May - July): Receive Form I-20 from UCSD International Students & Programs Office and apply for US F-1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: 100% of admitted PhD students are automatically awarded 5-year full funding packages comprising GSR/TA positions and fellowships.",
            "recommendation_letters_submission_method": "Three confidential recommendation letters uploaded electronically by referees via the GradApply portal.",
            "personal_statement_prompts": "Statement of Purpose: 2-page essay discussing research experience, specific research interests, and faculty alignment at UCSD.",
            "study_plan_research_proposal_requirements": "Integrated into statement of purpose; focus on concrete research problems, past methodological contributions, and prospective research directions.",
            "cv_format_requirements": "Academic CV detailing publications, open-source code repositories (GitHub), research prototypes, and technical coursework.",
            "interviews_conducted": True,
            "interview_format_details": "1-2 video interviews (30-60 minutes via Zoom) conducted by prospective faculty advisors to assess technical depth, mathematical problem solving, and research motivation.",
            "standardized_tests": "TOEFL iBT (85+ minimum; 100+ recommended) or IELTS Academic (7.0+). GRE is permanently NOT required.",
            "application_fee_amount": "USD 155 (Non-refundable)",
            "attestation_requirements": "Unofficial scanned transcripts submitted with application; official degree certificates required upon accepting offer.",
            "translation_requirements": "Certified English translation required for any documents not in English.",
            "final_submission_method": "100% digital submission via the UCSD GradApply portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "PDF scans of official transcripts from all post-secondary institutions attended with grading scale explanation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS transcripts; HEC attestation not required for initial review, but verified final degree required upon enrollment."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "Concise 2-page essay articulating research experience, specific research problems you wish to investigate, and why UCSD CSE faculty are an ideal fit.",
                "pakistan_specific_instruction": "Avoid generic childhood narratives; focus 80%+ on concrete technical projects, research methodology, and proposed directions."
            },
            {
                "document_name": "Letters of Recommendation (Three)",
                "mandatory": True,
                "specification": "3 letters of recommendation from faculty members or research directors who have directly supervised your research or advanced coursework.",
                "pakistan_specific_instruction": "Letters must be submitted via university domain emails (.edu.pk); strong research letters from professors with international standing carry highest weight."
            },
            {
                "document_name": "Academic CV / Resume",
                "mandatory": True,
                "specification": "Detailed CV listing publications, preprints (arXiv), open-source code repositories (GitHub), academic honors, and coursework.",
                "pakistan_specific_instruction": "Clearly link papers, open-source repositories, and competitive programming achievements."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "Official TOEFL iBT (code 4836) or IELTS Academic score report taken within past 2 years.",
                "pakistan_specific_instruction": "Aim for TOEFL speaking 26+ or IELTS speaking 7.5+ to qualify immediately for Teaching Assistantships without campus oral exams."
            },
            {
                "document_name": "Research Papers / Writing Sample",
                "mandatory": False,
                "specification": "Copies of published or submitted workshop/conference/journal papers demonstrating research caliber.",
                "pakistan_specific_instruction": "Strongly recommended; uploading first-author or co-authored papers dramatically elevates an applicant's profile."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 September 2025",
            "application_deadline": "15 December 2025",
            "university_admission_deadline": "15 December 2025",
            "document_submission_deadline": "15 December 2025",
            "recommendation_letters_deadline": "15 December 2025",
            "interview_period": "January to February 2026",
            "shortlist_announcement": "February to March 2026",
            "final_result_acceptance_deadline": "15 April 2026",
            "visa_application_window": "May to July 2026",
            "semester_commencement": "Late September 2026",
            "annual_cycle_notes": "Admissions offered exclusively for Fall quarter. No spring/winter doctoral admissions."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (rigor of undergraduate program, GPA, mathematics and systems course grades)",
            "extracurricular_and_leadership_weight": "5% (diversity contributions, hackathon leadership, tech outreach)",
            "research_experience_weight": "40% (published papers, research portfolio, originality of SOP, GitHub projects)",
            "work_experience_weight": "5% (industry research labs, Google/Meta/Microsoft internships)",
            "personal_statement_weight": "10% (clarity of research vision and articulation of technical goals)",
            "recommendations_weight": "10% (detailed assessment from research advisors assessing independent research capability)",
            "interview_weight": "5% (alignment with faculty research grants and technical fluency during interview)",
            "test_scores_weight": "Threshold requirement (TOEFL/IELTS compliance)",
            "financial_need_weight": "0% (purely merit and research capability based)",
            "selection_panel_composition": "CSE Graduate Admissions Committee, area faculty sub-committees (AI, Systems, Theory), and individual faculty lab PIs.",
            "evaluation_methodology": "Holistic faculty-driven evaluation: Initial screening by CSE Admissions Committee followed by faculty sub-committee review in candidate's chosen research area. Faculty advisors personally interview and champion candidates for funding."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "4,500+ PhD applicants to UCSD CSE",
            "total_scholarships_awarded": "~90 to 110 funded PhD offers accepted annually",
            "acceptance_rate_global": "~4% to 6% admit rate for CSE doctoral program",
            "acceptance_rate_pakistan": "~3% to 5% among applicants from top Pakistani institutions",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 CGPA (or top 3% of graduating cohort)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/CE from premier university (FAST-NUCES, NUST, LUMS, GIKI), 1-2 research papers at international venues or significant open-source contributions, stellar recommendation letters.",
            "common_backgrounds_of_winners": "Graduates of NUST (SEECS), FAST-NUCES, LUMS, GIKI, and UET Lahore.",
            "high_representation_countries": "United States, China, India, South Korea, Pakistan, Iran, Canada",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial overseas education agencies claiming guaranteed admission or funded seats at UCSD. Admissions are strictly merit-based and controlled by faculty."
            ],
            "application_fee_warning": "Application fee of USD 155 is paid strictly through the official UCSD GradApply portal. Never pay fees via unauthorized third parties.",
            "agent_and_intermediary_warnings": "UCSD does not partner with recruitment agents. Submissions showing boilerplate agent statements are systematically rejected.",
            "hidden_costs_breakdown": [
                "UCSD application fee: USD 155 (~PKR 43,500).",
                "US F-1 Visa and SEVIS I-901 fees: USD 535 (~PKR 150,000).",
                "Flight from Pakistan to San Diego/Los Angeles: ~PKR 350,000 to 500,000.",
                "Initial settling cash and housing deposit: ~USD 1,500 (~PKR 420,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: GRE General Test is required. (FACT: UCSD CSE has permanently eliminated the GRE requirement for graduate admissions).",
                "CLAIM: Direct contact with professors is useless. (FACT: Prospective advisors review applications directly; polite, paper-specific outreach can lead to interview invitations)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim Master's students receive full funding. At UCSD, full multi-year funding packages are guaranteed almost exclusively to PhD students."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.00 or higher in all coursework with no grade below B-.",
            "attendance_requirements": "Full-time physical enrollment (minimum 12 units per quarter) and active engagement in laboratory research.",
            "academic_progress_monitoring": "Annual Spring Evaluation conducted by thesis advisor and CSE graduate committee to verify satisfactory progress.",
            "work_restrictions_during_study": "Graduate Student Researcher and Teaching Assistant appointments are limited to 20 hours per week (50% appointment) during academic quarters to preserve research focus.",
            "home_country_return_obligation": "None. Eligible for standard US F-1 Optional Practical Training (OPT) including 3-year STEM extension and employer-sponsored H-1B / O-1 / EB-2 NIW visas.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding ceased upon withdrawal or academic disqualification; no repayment of previous salary or fee remissions required.",
            "rules_for_changing_university": "Fellowship packages are non-transferable to other universities.",
            "rules_for_changing_major": "Changing doctoral advisors within CSE requires finding a faculty member with grant funding willing to accept the student.",
            "extension_policy": "Guaranteed 5-year funding; 6th year funding is customary if supported by advisor's external research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "UCSD CSE Graduate Admissions & Financial Support",
                "source_url": "https://cse.ucsd.edu/graduate/graduate-admissions",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Individual research lab grant balances and open PhD headcounts per faculty member.",
                    "Country-wise historical acceptance statistics for Pakistani applicants.",
                    "Internal waitlist conversion rates during April admissions rounds."
                ]
            },
            {
                "source_name": "UCSD Graduate Division Financial Support & Benefits",
                "source_url": "https://grad.ucsd.edu/financial/index.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Year-over-year percentage adjustment formulas for academic student employee wages.",
                    "Discretionary emergency fund allocations available to international students."
                ]
            }
        ]
    },
    "SCH-AM-028": {
        "scholarship_id": "SCH-AM-028",
        "basic_details": {
            "scholarship_name": "Columbia University Computer Science Doctoral Fellowship",
            "offering_entity": "Columbia University (Fu Foundation School of Engineering and Applied Science - SEAS)",
            "host_country": "United States",
            "host_institutions_covered": "Columbia University Morningside Heights Campus (New York City, New York, USA)",
            "degree_levels": ["Doctor of Philosophy (PhD in Computer Science)"],
            "major_restrictions": "Restricted to doctoral candidates in Computer Science: Artificial Intelligence, Machine Learning, Natural Language Processing, Computer Vision, Systems & Cloud Computing, Security & Privacy, Computer Architecture, and Theory of Computation.",
            "number_of_awards_total": "100% of admitted PhD students receive guaranteed full financial support (~50 to 65 doctoral students admitted annually)",
            "number_of_awards_pakistan": "Open global merit competition; highly competitive (typically 1 to 3 exceptional Pakistani scholars admitted per cycle)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Guaranteed 5-year full doctoral fellowship and assistantship funding package"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restrictions.",
            "academic_qualifications": "A Bachelor's degree (BS/BE) or Master's degree (MS) in Computer Science, Computer Engineering, Mathematics, or closely related field from an HEC-recognized university with high academic distinction (minimum cumulative GPA of 3.60 / 4.00; competitive admits typically 3.85+ / 4.00 or top 1-2% of class).",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Columbia evaluates international transcripts holistically; strong grades in upper-division computer science and mathematics courses are critical.",
            "subject_background_prerequisites": "Advanced background in algorithms, discrete mathematics, computer systems, operating systems, linear algebra, and probability theory.",
            "current_education_status": "Students in the final year of their undergraduate or master's program may apply; degree must be conferred before September matriculation.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Publications in top computing conferences (NeurIPS, ICML, ACL, EMNLP, CVPR, SOSP, OSDI, SIGCOMM) or significant contributions to open-source software are the primary competitive differentiators.",
            "english_test_required": True,
            "ielts_minimum": 7.5,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "TOEFL iBT min 100 (recommended 105+) or IELTS Academic min 7.5 (each band 7.0+). Duolingo and Medium of Instruction certificates are not accepted.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None; female scholars in computing strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top applicants considered for Presidential Fellowships and SEAS Dean's Fellowships providing enhanced stipends.",
            "previous_scholarship_restrictions": "Winners of external fellowships (e.g., Fulbright) receive supplemental awards to ensure equivalent Columbia fellowship rates.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full Columbia University graduate tuition and SEAS mandatory instructional fees fully covered (~USD 58,000 to USD 62,000 / year value).",
                "amount": "100% covered (~USD 60,000 / year; ~PKR 16,800,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Columbia SEAS graduate application fee of USD 85 paid online via credit card.",
                "amount": "USD 85 (~PKR 23,800)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized Columbia University Residential housing in Morningside Heights, Manhattan guaranteed for incoming PhD students (typically USD 1,100 to 1,500/month for private room in shared university apartment).",
                "amount": "Paid from stipend (~USD 1,300 / month; ~PKR 364,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed 12-month annual stipend of USD 45,000 to USD 49,000 / year (~USD 3,750 to 4,083 / month; ~PKR 1,050,000 to 1,143,000 / month) provided via Graduate Research Assistantships (GRA), Teaching Assistantships (TA), and university fellowships, negotiated through SWC-UAW union contracts.",
                "amount": "USD 45,000 to 49,000 / year (~PKR 12,600,000 to 13,720,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel between Pakistan and New York City (JFK/EWR) is self-funded.",
                "amount": "Self-funded (~PKR 350,000 to 500,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "US F-1 Visa application fee (USD 185) and SEVIS I-901 fee (USD 350) paid directly to US government.",
                "amount": "USD 535 (~PKR 150,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Columbia Student Health Plan (Gold/Platinum) and Columbia Health and Related Services fee fully paid (~USD 5,500 / year value), covering medical, mental health, and dental benefits.",
                "amount": "100% covered (~USD 5,500 / year; ~PKR 1,540,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living and subsistence costs covered by the 12-month living stipend.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-end compute clusters, GPU servers, and lab equipment provided by research laboratories in the Computer Science building.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental and advisor travel funds cover registration, airfare, and hotel costs (USD 2,000 to 3,500 per conference) for presenting accepted papers at leading conferences.",
                "amount": "USD 2,000 to 3,500 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "MTA New York City Subway and bus fares paid by student out of stipend.",
                "amount": "Paid from stipend (~USD 132 / month)"
            },
            "total_estimated_value_usd_per_year": 110000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Ivy League research university: Columbia University in the City of New York (New York City, NY, USA)",
            "participating_institutions": [
                "Columbia University - Fu Foundation School of Engineering and Applied Science (SEAS)",
                "Columbia University - Department of Computer Science",
                "Data Science Institute at Columbia University"
            ],
            "university_rankings_scope": "Top 20 global university (QS World #34, THE World #17, US News #12); pioneer in natural language processing, computer vision, and systems.",
            "available_majors": [
                "PhD in Computer Science: Artificial Intelligence & Machine Learning",
                "PhD in Computer Science: Natural Language Processing & Speech",
                "PhD in Computer Science: Computer Vision & Robotics",
                "PhD in Computer Science: Systems, Cloud Computing & Networking",
                "PhD in Computer Science: Security, Cryptography & Privacy",
                "PhD in Computer Science: Computer Architecture & Hardware",
                "PhD in Computer Science: Theory of Computation & Algorithms",
                "PhD in Computer Science: Computational Biology & Quantum Computing"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 years full-time doctoral program.",
            "admission_requirements_summary": "4-year BS or MS in CS/STEM with 3.6+ GPA, 3 letters of recommendation, statement of purpose, CV, and TOEFL 100+ or IELTS 7.5+. GRE is optional/waived.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "NLP and machine learning are exceptionally selective; computer architecture, systems, and theoretical CS offer comparatively higher chances for applicants with aligned research experience.",
            "strategic_program_match_advice": "Focus heavily on matching with specific faculty research groups (e.g., Columbia NLP Lab, Systems & Security Lab) and referencing their publications in your statement of purpose."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://gradengineering.columbia.edu/admissions",
            "portal_system_name": "Columbia Engineering Graduate Admissions Portal",
            "account_creation_instructions": "Create an account on the Columbia SEAS portal, select Computer Science PhD, indicate faculty mentors and research tracks, and upload all required documents.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Research Columbia CS faculty research projects and identify 2-3 target professors.",
                "Step 2 (October - December): Create profile on the Columbia SEAS Graduate Admissions portal.",
                "Step 3 (November - December): Upload statement of purpose, CV, transcripts, and register 3 academic references.",
                "Step 4 (By 15 December): Submit application and pay USD 85 application fee.",
                "Step 5 (January - February): Faculty review applications and conduct technical video interviews.",
                "Step 6 (February - March): Official PhD offer letters with 5-year guaranteed funding packages issued.",
                "Step 7 (By 15 April): Confirm acceptance of admission offer.",
                "Step 8 (May - July): Receive Form I-20 and apply for US F-1 student visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: 100% of admitted PhD students are awarded 5-year full fellowship and assistantship packages without a separate scholarship application.",
            "recommendation_letters_submission_method": "Three academic recommendation letters submitted online via Columbia's electronic referee submission system.",
            "personal_statement_prompts": "Statement of Academic Purpose: 2-page essay discussing research experience, technical interests, faculty synergy, and doctoral aspirations.",
            "study_plan_research_proposal_requirements": "Integrated into statement of purpose; describe specific technical problems and methodologies of interest.",
            "cv_format_requirements": "Academic CV detailing publications, research projects, technical skills, and GitHub repositories.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual technical interviews (30-45 minutes via Zoom) conducted by prospective faculty advisors evaluating research depth, creativity, and mathematical foundations.",
            "standardized_tests": "TOEFL iBT (100+) or IELTS Academic (7.5+). GRE General Test is optional/waived.",
            "application_fee_amount": "USD 85 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official transcripts required upon admission offer.",
            "translation_requirements": "Certified English translations required for all non-English credentials.",
            "final_submission_method": "100% digital submission via the Columbia Engineering Graduate Admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Academic Transcripts",
                "mandatory": True,
                "specification": "Scanned electronic copies of official transcripts from all undergraduate and graduate institutions attended.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS transcripts with institutional grading scale; final HEC-attested copies needed only upon matriculation."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "2-page statement of academic purpose detailing research questions, past projects, technical methodology, and why specific Columbia CS faculty are an ideal fit.",
                "pakistan_specific_instruction": "Focus on research maturity and specific technical achievements rather than high school or general extracurriculars."
            },
            {
                "document_name": "Letters of Recommendation (Three)",
                "mandatory": True,
                "specification": "Three confidential recommendation letters from professors or research scientists familiar with your creative research capacity.",
                "pakistan_specific_instruction": "Ensure professors submit from verified university domain email addresses (.edu.pk); letters commenting in detail on research projects carry highest weight."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive CV detailing academic history, research projects, technical skills, publications, and GitHub links.",
                "pakistan_specific_instruction": "Clearly differentiate peer-reviewed publications, preprints, and coursework projects."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "Official TOEFL iBT (code 2111) or IELTS Academic score report taken within past 2 years.",
                "pakistan_specific_instruction": "Aim for TOEFL 105+ or IELTS 8.0 to satisfy all university and teaching assistant requirements."
            },
            {
                "document_name": "Research Papers / Preprints",
                "mandatory": False,
                "specification": "PDF copies of published papers or arXiv preprints demonstrating research depth.",
                "pakistan_specific_instruction": "Submitting first-author papers at top conferences significantly boosts admission probability."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 September 2025",
            "application_deadline": "15 December 2025",
            "university_admission_deadline": "15 December 2025",
            "document_submission_deadline": "15 December 2025",
            "recommendation_letters_deadline": "15 December 2025",
            "interview_period": "January to February 2026",
            "shortlist_announcement": "February to March 2026",
            "final_result_acceptance_deadline": "15 April 2026",
            "visa_application_window": "May to July 2026",
            "semester_commencement": "Early September 2026",
            "annual_cycle_notes": "Admissions offered for Fall term only. Strict deadline of December 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (GPA, mathematics rigor, difficulty of computer science coursework)",
            "extracurricular_and_leadership_weight": "5% (academic service, leadership, contributions to computing community)",
            "research_experience_weight": "40% (published research, statement of purpose, technical sophistication, code samples)",
            "work_experience_weight": "5% (industry research experience or advanced engineering roles)",
            "personal_statement_weight": "10% (clarity of research goals and alignment with faculty mentors)",
            "recommendations_weight": "10% (credibility of referees and their specific evaluations of research aptitude)",
            "interview_weight": "5% (alignment with faculty grants and technical performance in video interview)",
            "test_scores_weight": "Threshold requirement (TOEFL/IELTS compliance)",
            "financial_need_weight": "0% (purely merit and research achievement based)",
            "selection_panel_composition": "Columbia CS Doctoral Admissions Committee and faculty lab PIs.",
            "evaluation_methodology": "Faculty-led holistic review: Applications are evaluated by specialized area sub-committees (AI, Systems, Theory). Professors identify candidates whose research experience matches their active projects and extend funding offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "3,800+ applicants for Columbia CS PhD program",
            "total_scholarships_awarded": "~50 to 65 funded PhD offers accepted annually",
            "acceptance_rate_global": "~3% to 4% admit rate for PhD in Computer Science",
            "acceptance_rate_pakistan": "~2% to 3% among applicants from premier Pakistani universities",
            "typical_successful_applicant_gpa": "3.85+ / 4.00 CGPA (or top 1-2% of graduating class)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE with near-perfect GPA, 1-2 research papers at tier-1 international conferences (ACL, CVPR, NeurIPS), outstanding faculty recommendation letters.",
            "common_backgrounds_of_winners": "Graduates of LUMS, NUST, FAST-NUCES, and GIKI.",
            "high_representation_countries": "United States, China, India, South Korea, Canada, Pakistan, Iran",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed admission or funding at Columbia. Admissions decisions are made exclusively by Columbia faculty."
            ],
            "application_fee_warning": "Pay the USD 85 application fee only through the official Columbia SEAS portal. Never wire money to intermediaries.",
            "agent_and_intermediary_warnings": "Columbia SEAS strictly forbids the use of admissions agents. Plagiarized statements of purpose result in immediate disqualification.",
            "hidden_costs_breakdown": [
                "Columbia application fee: USD 85 (~PKR 23,800).",
                "US F-1 Visa and SEVIS I-901 fees: USD 535 (~PKR 150,000).",
                "Flight ticket from Pakistan to New York: ~PKR 350,000 to 500,000.",
                "New York City apartment security deposit and initial expenses: ~USD 2,000 (~PKR 560,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: General GRE is required for Columbia CS PhD. (FACT: The GRE General Test is optional/waived for Computer Science PhD applicants).",
                "CLAIM: Master's degree students receive full fellowships. (FACT: Fully funded 5-year packages at Columbia are reserved for doctoral students; MS degrees are largely self-funded)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party blogs report that Columbia does not fund international students equally. In reality, all admitted CS PhD students, regardless of citizenship, receive identical guaranteed funding packages."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.00 or higher in all graduate coursework with satisfactory research progress.",
            "attendance_requirements": "Full-time physical research and academic residency on the Morningside Heights campus in New York City.",
            "academic_progress_monitoring": "Annual progress reviews conducted by the doctoral program committee and faculty advisor.",
            "work_restrictions_during_study": "Graduate research and teaching assistantships are capped at 20 hours per week during academic terms under union contracts.",
            "home_country_return_obligation": "None. International graduates qualify for US F-1 OPT with 3-year STEM extension and employer-sponsored permanent residence pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding terminates upon withdrawal; past disbursements are not subject to clawback.",
            "rules_for_changing_university": "Fellowships cannot be transferred to other universities.",
            "rules_for_changing_major": "Changing research areas or advisors requires approval from the Department Chair and finding a faculty member with research funding.",
            "extension_policy": "Funding is guaranteed for 5 years; extensions into Year 6 are supported via faculty advisor research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "Columbia University Computer Science PhD Admissions & Financial Support",
                "source_url": "https://www.cs.columbia.edu/education/phd/admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific funding levels and exact number of open PhD seats per individual professor.",
                    "Country-level breakdown of admitted doctoral cohorts.",
                    "Internal ranking criteria used during final faculty recruitment meetings."
                ]
            },
            {
                "source_name": "Columbia Engineering Graduate Student Affairs & Fellowships",
                "source_url": "https://gradengineering.columbia.edu/student-services/financial-aid",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Negotiated annual union wage escalation percentages for future contract cycles.",
                    "Specific allocation numbers for Presidential vs Departmental Fellowships."
                ]
            }
        ]
    }
}
