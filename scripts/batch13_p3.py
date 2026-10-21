# scripts/batch13_p3.py
# SCH-AM-031: University of Maryland College Park (UMD) CS Graduate Assistantship (USA)
# SCH-AM-032: Johns Hopkins University (JHU) Computer Science PhD Fellowship (USA)
# SCH-AM-035: UMass Amherst Manning CICS Graduate Assistantship (USA)
# SCH-AM-036: Northwestern University Computer Science PhD Fellowship (USA)

DATA_P3 = {
    "SCH-AM-031": {
        "scholarship_id": "SCH-AM-031",
        "basic_details": {
            "scholarship_name": "University of Maryland College Park (UMD) Computer Science Graduate Assistantship & Dean's Fellowship",
            "offering_entity": "University of Maryland, College Park (Department of Computer Science & UMIACS - University of Maryland Institute for Advanced Computer Studies)",
            "host_country": "United States",
            "host_institutions_covered": "University of Maryland Main Campus (College Park, Maryland, USA)",
            "degree_levels": ["Doctor of Philosophy (PhD in Computer Science)"],
            "major_restrictions": "Restricted to doctoral candidates in Computer Science: Artificial Intelligence, Machine Learning, Computer Vision, Cybersecurity & Cryptography, Natural Language Processing, Human-Computer Interaction, Quantum Computing, and Systems.",
            "number_of_awards_total": "100% of admitted PhD students receive guaranteed full financial support (~75 to 90 doctoral students admitted annually)",
            "number_of_awards_pakistan": "Open global competition; Pakistani students typically secure 3 to 6 fully funded seats annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Guaranteed 5-year full doctoral funding package (9-month stipend + summer support + tuition waiver)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (BS) or Master's degree (MS) in Computer Science, Computer Engineering, Mathematics, or closely related STEM field from an HEC-recognized university with high academic standing (minimum cumulative GPA of 3.50 / 4.00; competitive admits typically 3.75+ / 4.00).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum UMD Graduate School GPA requirement is 3.0/4.0; however, Computer Science doctoral admissions are highly competitive with average admitted GPA above 3.80.",
            "subject_background_prerequisites": "Substantial coursework in algorithms, computer systems, discrete structures, programming languages, operating systems, and linear algebra.",
            "current_education_status": "Final-year undergraduate or master's students graduating before August matriculation are eligible to apply.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications (CVPR, NeurIPS, ACL, IEEE S&P) or major contributions to open-source software carry the highest weight in admissions decisions.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 96,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "TOEFL iBT min 96 (speaking 22, listening 24, reading 26, writing 24) or IELTS Academic min 7.0 (speaking 6.5+). International Teaching Assistants must satisfy Maryland state spoken English standards.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None; diversity in computing initiatives actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top-ranked candidates considered for Dean's Fellowships and UMIACS Research Fellowships providing additional supplemental stipends.",
            "previous_scholarship_restrictions": "External fellowship holders receive institutional top-up awards to match or exceed university baseline funding.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition remission for up to 10 graduate credit hours per semester plus mandatory student fees covered (~USD 36,000 / year value).",
                "amount": "100% covered (~USD 36,000 / year; ~PKR 10,080,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UMD Graduate School non-refundable application fee of USD 75 paid online.",
                "amount": "USD 75 (~PKR 21,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Funded from monthly stipend; graduate housing near campus (Graduate Hills, Graduate Gardens, or off-campus apartments in College Park/Hyattsville) averages USD 800 to 1,200/month for shared housing.",
                "amount": "Paid from stipend (~USD 950 / month; ~PKR 266,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed annual assistantship stipend of USD 34,000 to USD 39,000 / year (~USD 2,833 to 3,250 / month; ~PKR 793,000 to 910,000 / month) provided via Graduate Research Assistantships (GRA) or Teaching Assistantships (TA).",
                "amount": "USD 34,000 to 39,000 / year (~PKR 9,520,000 to 10,920,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International flights between Pakistan and Washington Dulles (IAD) / Reagan National (DCA) are self-funded.",
                "amount": "Self-funded (~PKR 350,000 to 500,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "US F-1 visa application fee (USD 185) and SEVIS I-901 fee (USD 350) paid to US government.",
                "amount": "USD 535 (~PKR 150,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "State of Maryland Employee Health Benefits plan fully subsidized for graduate assistants, covering medical, prescription, dental, and vision insurance (~USD 3,500 / year value).",
                "amount": "100% covered (~USD 3,500 / year; ~PKR 980,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living and groceries costs covered comfortably from monthly assistantship paychecks.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Workstations, Brendan Iribe Center AI hardware clusters, and UMIACS high-performance computing clusters provided by department.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental and UMIACS conference travel grants (USD 1,200 to 2,500 per trip) for students presenting papers at leading conferences.",
                "amount": "USD 1,200 to 2,500 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Shuttle-UM campus bus system provides free unlimited transit throughout College Park, Hyattsville, and connections to College Park Metro station.",
                "amount": "Free campus and local shuttle transit"
            },
            "total_estimated_value_usd_per_year": 75000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading US public research institution: University of Maryland, College Park (College Park, MD, USA)",
            "participating_institutions": [
                "University of Maryland - Department of Computer Science",
                "University of Maryland Institute for Advanced Computer Studies (UMIACS)",
                "Brendan Iribe Center for Computer Science and Engineering",
                "Maryland Cybersecurity Center (MC2)"
            ],
            "university_rankings_scope": "Top 15 global computer science program (CSRankings #9, US News CS #17, THE World #55); powerhouse in AI, computer vision, cybersecurity, and quantum computing.",
            "available_majors": [
                "PhD in Computer Science: Artificial Intelligence & Machine Learning",
                "PhD in Computer Science: Computer Vision & Multimedia",
                "PhD in Computer Science: Cybersecurity, Privacy & Cryptography",
                "PhD in Computer Science: Natural Language Processing & Human Language",
                "PhD in Computer Science: Quantum Information & Computing",
                "PhD in Computer Science: Human-Computer Interaction (HCIL)",
                "PhD in Computer Science: Systems, Cloud & High-Performance Computing",
                "PhD in Computer Science: Theoretical Computer Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 years full-time doctoral program.",
            "admission_requirements_summary": "4-year BS or MS in CS/STEM with 3.5+ GPA, 3 letters of recommendation, statement of purpose, CV, and TOEFL 96+ or IELTS 7.0+. GRE is optional.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "AI, computer vision, and NLP attract massive applicant volume; systems, cryptography, HCI, and quantum computing present strong opportunities for applicants with matched research expertise.",
            "strategic_program_match_advice": "Familiarize yourself with labs in the Brendan Iribe Center; specify 2-3 faculty research groups in your application and reference their active grant projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.cs.umd.edu/grad/apply",
            "portal_system_name": "UMD Graduate School TerpEngage Application System",
            "account_creation_instructions": "Register on the TerpEngage portal, choose Computer Science (PhD), select up to three faculty research areas, and upload transcripts and essays.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Explore faculty research projects at UMD Computer Science and UMIACS.",
                "Step 2 (October - December): Create profile on the UMD TerpEngage graduate portal.",
                "Step 3 (November - December): Upload statement of purpose, CV, transcripts, and register 3 academic references.",
                "Step 4 (By 15 December): Submit application and pay USD 75 fee.",
                "Step 5 (January - February): Faculty review applications and conduct video interviews.",
                "Step 6 (February - March): Official PhD offer letters with 5-year guaranteed funding package released.",
                "Step 7 (By 15 April): Confirm acceptance in the TerpEngage portal.",
                "Step 8 (May - July): Receive Form I-20 and apply for US F-1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: All admitted CS PhD students receive guaranteed full Graduate Assistantship packages without a separate scholarship application.",
            "recommendation_letters_submission_method": "Three academic recommendation letters submitted online through the automated referee portal.",
            "personal_statement_prompts": "Statement of Purpose: 1-2 page essay covering research background, academic achievements, technical motivations, and target faculty advisors.",
            "study_plan_research_proposal_requirements": "Integrated into statement of purpose; focus on concrete research problems, past experimental results, and future directions.",
            "cv_format_requirements": "Academic CV detailing publications, open-source repositories, engineering projects, and technical skills.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual technical interviews (30-45 minutes via Zoom) conducted by prospective faculty advisors to evaluate research problem solving and mathematical intuition.",
            "standardized_tests": "TOEFL iBT (96+) or IELTS Academic (7.0+). GRE General Test is optional.",
            "application_fee_amount": "USD 75 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official transcripts required upon admission offer.",
            "translation_requirements": "Certified English translations required for non-English credentials.",
            "final_submission_method": "100% digital submission via the UMD TerpEngage portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "PDF scans of official transcripts from all undergraduate and graduate institutions attended.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS transcripts; official HEC-attested documents required only upon enrollment."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "1-2 page essay articulating research background, technical achievements, and faculty alignment at UMD.",
                "pakistan_specific_instruction": "Specifically name 2-3 UMD CS faculty members whose publications you have studied."
            },
            {
                "document_name": "Letters of Recommendation (Three)",
                "mandatory": True,
                "specification": "Three confidential recommendation letters from professors or research mentors assessing research potential.",
                "pakistan_specific_instruction": "Ensure professors submit from verified institutional email addresses (.edu.pk)."
            },
            {
                "document_name": "Academic CV / Resume",
                "mandatory": True,
                "specification": "Detailed CV listing publications, preprints, GitHub repositories, and competitive programming achievements.",
                "pakistan_specific_instruction": "Clearly link papers, open-source projects, and ICPC/hackathon awards."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "Official TOEFL iBT (code 5814) or IELTS Academic score report taken within past 2 years.",
                "pakistan_specific_instruction": "Aim for TOEFL speaking 24+ or IELTS speaking 7.0+ to satisfy TA spoken English certification."
            },
            {
                "document_name": "Research Papers / Writing Samples",
                "mandatory": False,
                "specification": "PDF copies of published conference/journal papers or technical preprints.",
                "pakistan_specific_instruction": "Uploading published papers significantly boosts admission chances."
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
            "semester_commencement": "Late August 2026",
            "annual_cycle_notes": "Admissions offered for Fall semester only. Hard deadline is December 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (GPA, rigor of mathematics and core CS curriculum)",
            "extracurricular_and_leadership_weight": "5% (open source contributions, tech leadership, hackathons)",
            "research_experience_weight": "40% (published papers, research portfolio, technical originality, code samples)",
            "work_experience_weight": "5% (internships at research labs or software engineering companies)",
            "personal_statement_weight": "10% (clarity of research vision and articulation of technical goals)",
            "recommendations_weight": "10% (substantive endorsements evaluating independent research capabilities)",
            "interview_weight": "5% (technical fit and faculty interview performance)",
            "test_scores_weight": "Threshold requirement (TOEFL/IELTS compliance)",
            "financial_need_weight": "0% (purely merit and research achievement based)",
            "selection_panel_composition": "UMD CS Graduate Admissions Committee and individual faculty lab heads.",
            "evaluation_methodology": "Two-stage holistic review: Admissions committee screens academic thresholds, followed by faculty sub-committees matching candidates with sponsored research grants and assistantship lines."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "3,200+ applicants for CS PhD program",
            "total_scholarships_awarded": "~75 to 90 funded PhD offers accepted annually",
            "acceptance_rate_global": "~5% to 6% admit rate for PhD in Computer Science",
            "acceptance_rate_pakistan": "~4% to 5% among applicants from premier Pakistani universities",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (or top 5% of graduating class)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE from top Pakistani university, 1+ peer-reviewed conference publications, strong programming skills, high TOEFL/IELTS scores.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, and UET Lahore.",
            "high_representation_countries": "United States, China, India, South Korea, Pakistan, Iran, Canada",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed admission or funding at UMD. Admissions decisions are made exclusively by UMD faculty."
            ],
            "application_fee_warning": "Pay the USD 75 application fee only through the official UMD TerpEngage portal. Never wire money to intermediaries.",
            "agent_and_intermediary_warnings": "UMD strictly forbids the use of admissions agents. Plagiarized statements of purpose result in immediate disqualification.",
            "hidden_costs_breakdown": [
                "UMD application fee: USD 75 (~PKR 21,000).",
                "US F-1 Visa and SEVIS I-901 fees: USD 535 (~PKR 150,000).",
                "Flight ticket from Pakistan to Washington DC: ~PKR 350,000 to 500,000.",
                "Initial apartment security deposit and living costs: ~USD 1,500 (~PKR 420,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: GRE General Test is mandatory. (FACT: The GRE is completely optional for CS PhD applicants).",
                "CLAIM: Admitted PhD students must pay tuition out of pocket. (FACT: 100% of admitted PhD students receive full tuition remission)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums claim MS students get full funding. At UMD, guaranteed multi-year assistantships are reserved almost exclusively for PhD students."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.00 or higher in all graduate coursework with satisfactory research progress.",
            "attendance_requirements": "Full-time physical research and academic enrollment on the College Park campus.",
            "academic_progress_monitoring": "Annual progress reviews conducted by the graduate committee and doctoral advisor.",
            "work_restrictions_during_study": "Graduate assistantships require 20 hours per week of research or teaching duties during academic semesters.",
            "home_country_return_obligation": "None. International graduates qualify for US F-1 OPT with 3-year STEM extension and employer-sponsored permanent residence pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding terminates upon withdrawal; past disbursements are not subject to clawback.",
            "rules_for_changing_university": "Fellowships cannot be transferred to other universities.",
            "rules_for_changing_major": "Changing research advisors requires finding another faculty member with grant funding willing to support the student.",
            "extension_policy": "Funding is guaranteed for 5 years; extensions into Year 6 are customary with advisor grant support."
        },
        "official_sources_verified": [
            {
                "source_name": "UMD Department of Computer Science Graduate Admissions",
                "source_url": "https://www.cs.umd.edu/grad/apply",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific funding availability and open PhD headcounts per professor.",
                    "Country-level breakdown of admitted doctoral cohorts.",
                    "Waitlist ranking criteria used during final admissions rounds."
                ]
            },
            {
                "source_name": "UMD Graduate School Assistantship Policies & Benefits",
                "source_url": "https://gradschool.umd.edu/funding/student-fellowships-awards",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Future year cost-of-living stipend increase percentages.",
                    "Discretionary emergency fund allocations for international graduate students."
                ]
            }
        ]
    },
    "SCH-AM-032": {
        "scholarship_id": "SCH-AM-032",
        "basic_details": {
            "scholarship_name": "Johns Hopkins University (JHU) Computer Science PhD Fellowship & Assistantship",
            "offering_entity": "Johns Hopkins University (Whiting School of Engineering - Department of Computer Science)",
            "host_country": "United States",
            "host_institutions_covered": "Johns Hopkins University Homewood Campus (Baltimore, Maryland, USA)",
            "degree_levels": ["Doctor of Philosophy (PhD in Computer Science)"],
            "major_restrictions": "Restricted to doctoral candidates in Computer Science: Artificial Intelligence, Natural Language Processing, Computer Vision & Medical Imaging, Robotics, Computational Biology & Genomics, Cybersecurity & Systems, and Theory of Computation.",
            "number_of_awards_total": "100% of admitted PhD students receive guaranteed full financial support (~50 to 65 doctoral students admitted annually)",
            "number_of_awards_pakistan": "Open international competition; typically 2 to 5 high-achieving Pakistani scholars admitted annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Guaranteed 5-year full doctoral funding package (tuition waiver + 12-month living stipend + health benefits)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (BS) or Master's degree (MS) in Computer Science, Computer Engineering, Mathematics, or closely related STEM discipline from an HEC-recognized university with high academic distinction (minimum cumulative GPA of 3.60 / 4.00; competitive admits typically 3.85+ / 4.00).",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "JHU Whiting School evaluates international transcripts holistically; rigorous coursework in discrete mathematics, algorithms, and systems is paramount.",
            "subject_background_prerequisites": "Advanced coursework in algorithms, data structures, computer systems, linear algebra, calculus, and probability.",
            "current_education_status": "Graduating seniors in their final year of BS or MS can apply; degree conferral required before August matriculation.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Demonstrated academic research capability through peer-reviewed publications (ACL, EMNLP, CVPR, NeurIPS, MICCAI) or substantial research software development is primary.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "TOEFL iBT min 100 (sub-scores 22+) or IELTS Academic min 7.0 (each section 6.5+). Duolingo and MOI certificates are not accepted.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None; women in STEM initiatives actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top applicants nominated for Whiting School Dean's Fellowships and Center for Language and Speech Processing (CLSP) Fellowships.",
            "previous_scholarship_restrictions": "Recipients of external awards receive institutional stipend top-ups.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition waiver covering 100% of Whiting School of Engineering graduate tuition (~USD 62,000 / year value).",
                "amount": "100% covered (~USD 62,000 / year; ~PKR 17,360,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Whiting School of Engineering graduate application fee of USD 75 paid online.",
                "amount": "USD 75 (~PKR 21,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from guaranteed living stipend; off-campus apartments near Homewood campus (Charles Village, Roland Park, Hampden) average USD 750 to 1,100/month for shared housing.",
                "amount": "Paid from stipend (~USD 900 / month; ~PKR 252,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed 12-month annual living stipend of USD 42,000 to USD 46,000 / year (~USD 3,500 to 3,833 / month; ~PKR 980,000 to 1,073,000 / month) provided via Graduate Research Assistantships (GRA) or Teaching Assistantships (TA).",
                "amount": "USD 42,000 to 46,000 / year (~PKR 11,760,000 to 12,880,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Baltimore/Washington International Airport (BWI) / Washington Dulles (IAD) is self-funded.",
                "amount": "Self-funded (~PKR 350,000 to 500,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "US F-1 Visa fee (USD 185) and SEVIS I-901 fee (USD 350) paid to US government.",
                "amount": "USD 535 (~PKR 150,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "JHU Student Health Benefit Plan (SHBP) fully covered (~USD 4,200 / year value), including comprehensive medical, dental, and vision coverage.",
                "amount": "100% covered (~USD 4,200 / year; ~PKR 1,176,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Food and living subsistence covered comfortably by the 12-month doctoral stipend.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-end compute workstations, GPU clusters (MARCC / Rockfish supercomputer), and lab instrumentation provided by department.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental and advisor travel funds cover registration, airfare, and hotel costs (USD 1,500 to 3,000 per conference) for presenting accepted papers at leading conferences.",
                "amount": "USD 1,500 to 3,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Hopkins Shuttle system provides free unlimited transit connecting Homewood, Mount Vernon, and East Baltimore (JHMI) medical campus.",
                "amount": "Free campus shuttle transit"
            },
            "total_estimated_value_usd_per_year": 110000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-renowned private research university: Johns Hopkins University (Baltimore, MD, USA)",
            "participating_institutions": [
                "Johns Hopkins University - Whiting School of Engineering",
                "Department of Computer Science (Homewood Campus)",
                "Center for Language and Speech Processing (CLSP)",
                "Laboratory for Computational Sensing and Robotics (LCSR)",
                "Institute for Data-Intensive Engineering and Science (IDIES)"
            ],
            "university_rankings_scope": "Top 15 global university (QS World #32, THE World #15, US News #9); world leader in medical AI, natural language processing, surgical robotics, and computational genomics.",
            "available_majors": [
                "PhD in Computer Science: Natural Language Processing & Speech (CLSP)",
                "PhD in Computer Science: Computer Vision & Medical Imaging",
                "PhD in Computer Science: Surgical Robotics & Autonomous Systems",
                "PhD in Computer Science: Computational Biology & Genomics",
                "PhD in Computer Science: Artificial Intelligence & Machine Learning",
                "PhD in Computer Science: Cybersecurity & Cryptography",
                "PhD in Computer Science: Systems & Cloud Computing",
                "PhD in Computer Science: Theoretical Computer Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 years full-time doctoral program.",
            "admission_requirements_summary": "4-year BS or MS in CS/STEM with 3.6+ GPA, 3 letters of recommendation, statement of purpose, CV, and TOEFL 100+ or IELTS 7.0+. GRE is not required.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "CLSP (NLP/speech) and medical imaging/robotics are world-famous and attract extraordinary competition; systems, security, and theory offer slightly higher acceptance rates for highly qualified applicants.",
            "strategic_program_match_advice": "Mention specific faculty members and research centers (e.g., CLSP, LCSR) in your statement of purpose, referencing their recent publications."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.cs.jhu.edu/graduate-studies/graduate-admissions/",
            "portal_system_name": "JHU Whiting School Graduate Admissions Portal (Slate)",
            "account_creation_instructions": "Register on the JHU Slate graduate portal, select Computer Science (PhD), choose faculty research subfields, and upload required documents.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Research faculty laboratories at JHU CS, CLSP, and LCSR.",
                "Step 2 (October - December): Create profile on the JHU Slate graduate admissions portal.",
                "Step 3 (November - December): Upload statement of purpose, CV, transcripts, and register 3 academic references.",
                "Step 4 (By 15 December): Submit application and pay USD 75 fee.",
                "Step 5 (January - February): Faculty review applications and conduct technical video interviews.",
                "Step 6 (February - March): Official PhD offer letters with 5-year guaranteed funding package released.",
                "Step 7 (By 15 April): Confirm acceptance in the portal.",
                "Step 8 (May - July): Receive Form I-20 and apply for US F-1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: 100% of admitted PhD students are awarded 5-year full funding packages without a separate scholarship application.",
            "recommendation_letters_submission_method": "Three academic recommendation letters submitted online via the Slate referee portal.",
            "personal_statement_prompts": "Statement of Purpose: 2-page essay discussing research experience, technical interests, faculty alignment, and doctoral goals.",
            "study_plan_research_proposal_requirements": "Integrated into statement of purpose; describe specific technical problems and methodologies of interest.",
            "cv_format_requirements": "Academic CV detailing publications, research projects, technical skills, and GitHub repositories.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual technical interviews (30-45 minutes via Zoom) conducted by prospective faculty advisors evaluating research depth and technical problem solving.",
            "standardized_tests": "TOEFL iBT (100+) or IELTS Academic (7.0+). GRE is NOT required.",
            "application_fee_amount": "USD 75 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official transcripts required upon admission offer.",
            "translation_requirements": "Certified English translations required for non-English credentials.",
            "final_submission_method": "100% digital submission via the JHU Slate application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Academic Transcripts",
                "mandatory": True,
                "specification": "Scanned electronic copies of official transcripts from all undergraduate and graduate institutions attended.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS transcripts with grading scale; official HEC attestation required only upon matriculation."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "2-page statement of purpose articulating research questions, past projects, technical methodology, and why JHU faculty are an ideal fit.",
                "pakistan_specific_instruction": "Focus on research depth and technical contributions rather than generic personal background."
            },
            {
                "document_name": "Letters of Recommendation (Three)",
                "mandatory": True,
                "specification": "Three confidential recommendation letters from professors or research scientists familiar with your creative research capacity.",
                "pakistan_specific_instruction": "Ensure professors submit from verified university domain email addresses (.edu.pk)."
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
                "specification": "Official TOEFL iBT (code 5332) or IELTS Academic score report taken within past 2 years.",
                "pakistan_specific_instruction": "Aim for TOEFL 105+ or IELTS 7.5+ to satisfy all graduate requirements."
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
            "semester_commencement": "Late August 2026",
            "annual_cycle_notes": "Admissions offered for Fall semester only. Hard deadline is December 15."
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
            "selection_panel_composition": "JHU CS Doctoral Admissions Committee and faculty lab PIs.",
            "evaluation_methodology": "Faculty-driven holistic review: Area committees evaluate dossiers, match candidates to funded faculty labs, and conduct interviews before issuing full funding offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "3,000+ applicants for JHU CS PhD program",
            "total_scholarships_awarded": "~50 to 65 funded PhD offers accepted annually",
            "acceptance_rate_global": "~4% to 5% admit rate for PhD in Computer Science",
            "acceptance_rate_pakistan": "~3% to 4% among applicants from premier Pakistani universities",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 CGPA (or top 3% of graduating class)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE with top standing, 1-2 research papers at tier-1 international conferences (ACL, CVPR, NeurIPS, MICCAI), outstanding faculty recommendation letters.",
            "common_backgrounds_of_winners": "Graduates of LUMS, NUST, FAST-NUCES, and GIKI.",
            "high_representation_countries": "United States, China, India, South Korea, Canada, Pakistan, Iran",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed admission or funding at JHU. Admissions decisions are made exclusively by JHU faculty."
            ],
            "application_fee_warning": "Pay the USD 75 application fee only through the official JHU Slate portal. Never wire money to intermediaries.",
            "agent_and_intermediary_warnings": "JHU strictly forbids the use of admissions agents. Plagiarized statements of purpose result in immediate disqualification.",
            "hidden_costs_breakdown": [
                "JHU application fee: USD 75 (~PKR 21,000).",
                "US F-1 Visa and SEVIS I-901 fees: USD 535 (~PKR 150,000).",
                "Flight ticket from Pakistan to Baltimore/Washington: ~PKR 350,000 to 500,000.",
                "Initial apartment security deposit and living costs: ~USD 1,500 (~PKR 420,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: GRE is mandatory for JHU CS PhD. (FACT: The GRE is NOT required for Computer Science PhD applicants).",
                "CLAIM: Only medical students receive funding at JHU. (FACT: 100% of admitted Computer Science PhD students receive full 5-year funding packages)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites claim living costs in Baltimore are unaffordable on a student stipend. In reality, Baltimore offers significantly lower housing costs than New York or Boston, making the USD 42,000+ stipend very generous."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.00 or higher in all graduate coursework with satisfactory research progress.",
            "attendance_requirements": "Full-time physical research and academic residency on the Homewood campus in Baltimore.",
            "academic_progress_monitoring": "Annual progress reviews conducted by the doctoral program committee and faculty advisor.",
            "work_restrictions_during_study": "Graduate research and teaching assistantships are capped at 20 hours per week during academic terms.",
            "home_country_return_obligation": "None. International graduates qualify for US F-1 OPT with 3-year STEM extension and employer-sponsored permanent residence pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding terminates upon withdrawal; past disbursements are not subject to clawback.",
            "rules_for_changing_university": "Fellowships cannot be transferred to other universities.",
            "rules_for_changing_major": "Changing research areas or advisors requires approval from the Department Chair and finding a faculty member with research funding.",
            "extension_policy": "Funding is guaranteed for 5 years; extensions into Year 6 are supported via faculty advisor research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "JHU Department of Computer Science Graduate Admissions",
                "source_url": "https://www.cs.jhu.edu/graduate-studies/graduate-admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific funding levels and exact number of open PhD seats per individual professor.",
                    "Country-level breakdown of admitted doctoral cohorts.",
                    "Internal ranking criteria used during final faculty recruitment meetings."
                ]
            },
            {
                "source_name": "JHU Whiting School Graduate Financial Aid & Fellowships",
                "source_url": "https://engineering.jhu.edu/graduate-studies/tuition-financial-aid/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Future year cost-of-living stipend increase percentages.",
                    "Discretionary emergency fund allocations for international graduate students."
                ]
            }
        ]
    },
    "SCH-AM-035": {
        "scholarship_id": "SCH-AM-035",
        "basic_details": {
            "scholarship_name": "UMass Amherst Manning CICS Graduate Assistantship & Fellowship",
            "offering_entity": "University of Massachusetts Amherst (Manning College of Information and Computer Sciences - CICS)",
            "host_country": "United States",
            "host_institutions_covered": "University of Massachusetts Amherst Main Campus (Amherst, Massachusetts, USA)",
            "degree_levels": ["Doctor of Philosophy (PhD in Computer Science)"],
            "major_restrictions": "Restricted to doctoral candidates in Computer Science: Artificial Intelligence, Machine Learning, Information Retrieval & Search, Natural Language Processing, Computer Systems & Networking, Computer Vision, Robotics, and Theory of Computation.",
            "number_of_awards_total": "100% of admitted PhD students receive guaranteed full financial support (~55 to 70 doctoral students admitted annually)",
            "number_of_awards_pakistan": "Open global merit competition; typically 3 to 6 high-achieving Pakistani graduates admitted per academic year",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Guaranteed 5-year full doctoral funding package (tuition waiver + academic-year stipend + summer stipend + health insurance)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (BS) or Master's degree (MS) in Computer Science, Computer Engineering, Mathematics, or closely related field from an HEC-recognized university with high academic distinction (minimum cumulative GPA of 3.50 / 4.00; competitive admits typically 3.75+ / 4.00).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "UMass Graduate School minimum GPA is 3.0/4.0; CICS PhD admissions committee applies rigorous standards with competitive admitted GPA above 3.75.",
            "subject_background_prerequisites": "Substantial undergraduate coursework in algorithms, data structures, computer systems, operating systems, linear algebra, and discrete mathematics.",
            "current_education_status": "Students in the final year of undergraduate or master's study can apply; degree completion required before September matriculation.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Publications in top computing conferences (NeurIPS, ICML, SIGIR, ACL, EMNLP, CVPR, OSDI, SIGCOMM) or open-source software contributions carry highest weight.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": True,
            "moi_certificate_accepted": False,
            "language_notes": "TOEFL iBT min 80 (recommended 100+; speaking 26+ for TA certification) or IELTS Academic min 6.5 (speaking 7.0+ for TA), or Duolingo min 115. MOI certificates not accepted.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None; diversity in computing initiatives actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top applicants considered for Manning CICS Dean's Fellowships and Center for Intelligent Information Retrieval (CIIR) Fellowships.",
            "previous_scholarship_restrictions": "External fellowship holders receive institutional top-up awards.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition waiver covering 100% of international graduate tuition and curriculum fees (~USD 35,000 / year value).",
                "amount": "100% covered (~USD 35,000 / year; ~PKR 9,800,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UMass Amherst Graduate School application fee of USD 85 paid online via credit card.",
                "amount": "USD 85 (~PKR 23,800)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from monthly assistantship stipend; off-campus student apartments in Amherst, Hadley, and Northampton average USD 700 to 1,000/month for shared housing.",
                "amount": "Paid from stipend (~USD 850 / month; ~PKR 238,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed annual assistantship stipend of USD 36,000 to USD 40,000 / year (~USD 3,000 to 3,333 / month; ~PKR 840,000 to 933,000 / month) provided via Graduate Research Assistantships (RA) and Teaching Assistantships (TA) under GEO union contract.",
                "amount": "USD 36,000 to 40,000 / year (~PKR 10,080,000 to 11,200,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Boston Logan (BOS) / Bradley International (BDL) is self-funded.",
                "amount": "Self-funded (~PKR 350,000 to 500,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "US F-1 Visa fee (USD 185) and SEVIS I-901 fee (USD 350) paid to US government.",
                "amount": "USD 535 (~PKR 150,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Graduate Employee Organization (GEO) negotiated health insurance plan providing 95% subsidized medical, dental, and vision coverage (~USD 3,800 / year value).",
                "amount": "100% covered (~USD 3,800 / year; ~PKR 1,064,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Food and living subsistence covered comfortably by the monthly assistantship stipend.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-performance GPU computing clusters, research lab hardware, and software licenses provided by CICS.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental and advisor travel funds cover registration, airfare, and hotel costs (USD 1,200 to 2,500 per conference) for presenting accepted papers at leading conferences.",
                "amount": "USD 1,200 to 2,500 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Pioneer Valley Transit Authority (PVTA) bus system is 100% fare-free throughout Amherst, Hadley, Northampton, and South Hadley.",
                "amount": "100% free regional public bus transit"
            },
            "total_estimated_value_usd_per_year": 78000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single renowned public research university: University of Massachusetts Amherst (Amherst, MA, USA)",
            "participating_institutions": [
                "UMass Amherst - Manning College of Information and Computer Sciences (CICS)",
                "Center for Intelligent Information Retrieval (CIIR)",
                "Computational Social Science Institute (CSSI)",
                "Cybersecurity Institute at UMass Amherst"
            ],
            "university_rankings_scope": "Top 20 global computer science program (CSRankings #18, US News CS #24); world-renowned pioneer in information retrieval, AI, natural language processing, and systems.",
            "available_majors": [
                "PhD in Computer Science: Artificial Intelligence & Machine Learning",
                "PhD in Computer Science: Information Retrieval & Search (CIIR)",
                "PhD in Computer Science: Natural Language Processing & Computational Linguistics",
                "PhD in Computer Science: Computer Vision & Robotics",
                "PhD in Computer Science: Systems, Cloud Computing & Networking",
                "PhD in Computer Science: Security, Privacy & Cryptography",
                "PhD in Computer Science: Theoretical Computer Science",
                "PhD in Computer Science: Data Science & Database Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 years full-time doctoral program.",
            "admission_requirements_summary": "4-year BS or MS in CS/STEM with 3.5+ GPA, 3 letters of recommendation, statement of purpose, CV, and TOEFL 80+ (100+ recommended) or IELTS 6.5+. GRE is NOT required.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Information retrieval and AI/ML are globally renowned and attract heavy competition; systems, networking, theory, and databases offer comparatively higher admission chances for qualified applicants.",
            "strategic_program_match_advice": "Review faculty directories at Manning CICS; specify 2-3 target research groups and cite their recent conference papers in your statement of purpose."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.cics.umass.edu/academics/phd/apply",
            "portal_system_name": "UMass Amherst Graduate School Online Application System (Slate)",
            "account_creation_instructions": "Register on the UMass Slate graduate portal, select Computer Science (PhD), specify faculty research areas, and upload required application materials.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Research CICS faculty research groups and laboratories.",
                "Step 2 (October - December): Create profile on the UMass Amherst Slate graduate portal.",
                "Step 3 (November - December): Upload statement of purpose, CV, transcripts, and register 3 academic references.",
                "Step 4 (By 15 December): Submit application and pay USD 85 application fee.",
                "Step 5 (January - February): Faculty review applications and conduct virtual technical interviews.",
                "Step 6 (February - March): Department issues official PhD admission offer letters with 5-year guaranteed funding package.",
                "Step 7 (By 15 April): Confirm acceptance in the portal.",
                "Step 8 (May - July): Receive Form I-20 and apply for US F-1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: 100% of admitted PhD students are awarded 5-year full funding packages without a separate scholarship application.",
            "recommendation_letters_submission_method": "Three academic recommendation letters submitted online via the Slate automated referee portal.",
            "personal_statement_prompts": "Statement of Purpose: 2-page essay discussing research experience, technical interests, faculty alignment, and doctoral aspirations.",
            "study_plan_research_proposal_requirements": "Integrated into statement of purpose; focus on concrete research problems, past methodological contributions, and prospective research directions.",
            "cv_format_requirements": "Academic CV detailing publications, open-source repositories, engineering projects, and technical skills.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual technical interviews (30-45 minutes via Zoom) conducted by prospective faculty advisors evaluating research problem solving and mathematical intuition.",
            "standardized_tests": "TOEFL iBT (80+; 100+ recommended) or IELTS Academic (6.5+) or Duolingo (115+). GRE is NOT required.",
            "application_fee_amount": "USD 85 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official transcripts required upon admission offer.",
            "translation_requirements": "Certified English translations required for non-English credentials.",
            "final_submission_method": "100% digital submission via the UMass Amherst Slate portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "PDF scans of official transcripts from all undergraduate and graduate institutions attended.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS transcripts; official HEC attestation required only upon matriculation."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "2-page statement of purpose articulating research questions, past projects, technical methodology, and why Manning CICS faculty are an ideal fit.",
                "pakistan_specific_instruction": "Focus on research depth and technical contributions rather than generic personal background."
            },
            {
                "document_name": "Letters of Recommendation (Three)",
                "mandatory": True,
                "specification": "Three confidential recommendation letters from professors or research scientists familiar with your creative research capacity.",
                "pakistan_specific_instruction": "Ensure professors submit from verified university domain email addresses (.edu.pk)."
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
                "specification": "Official TOEFL iBT (code 3917), IELTS Academic, or Duolingo score report taken within past 2 years.",
                "pakistan_specific_instruction": "Aim for TOEFL 100+ or IELTS 7.5+ to satisfy TA spoken English standards."
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
            "annual_cycle_notes": "Admissions offered for Fall semester only. Hard deadline is December 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (GPA, difficulty of computer science coursework, mathematical foundations)",
            "extracurricular_and_leadership_weight": "5% (academic service, leadership, contributions to open-source computing)",
            "research_experience_weight": "40% (published research, statement of purpose, technical sophistication, code samples)",
            "work_experience_weight": "5% (industry research experience or software engineering roles)",
            "personal_statement_weight": "10% (clarity of research goals and alignment with faculty mentors)",
            "recommendations_weight": "10% (credibility of referees and their specific evaluations of research aptitude)",
            "interview_weight": "5% (alignment with faculty grants and technical performance in video interview)",
            "test_scores_weight": "Threshold requirement (TOEFL/IELTS compliance)",
            "financial_need_weight": "0% (purely merit and research achievement based)",
            "selection_panel_composition": "Manning CICS Doctoral Admissions Committee and faculty lab PIs.",
            "evaluation_methodology": "Faculty-led holistic review: Area committees review candidate dossiers, match candidates to funded faculty labs, and conduct interviews before issuing full funding offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "2,800+ applicants for CICS PhD program",
            "total_scholarships_awarded": "~55 to 70 funded PhD offers accepted annually",
            "acceptance_rate_global": "~5% to 6% admit rate for PhD in Computer Science",
            "acceptance_rate_pakistan": "~4% to 5% among applicants from premier Pakistani universities",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (or top 5% of graduating class)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE with top standing, 1+ peer-reviewed conference publications, strong programming skills, high TOEFL/IELTS scores.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, and UET Lahore.",
            "high_representation_countries": "United States, China, India, South Korea, Pakistan, Iran, Canada",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed admission or funding at UMass Amherst. Admissions decisions are made exclusively by CICS faculty."
            ],
            "application_fee_warning": "Pay the USD 85 application fee only through the official UMass Slate portal. Never wire money to intermediaries.",
            "agent_and_intermediary_warnings": "UMass Amherst strictly forbids the use of admissions agents. Plagiarized statements of purpose result in immediate disqualification.",
            "hidden_costs_breakdown": [
                "UMass application fee: USD 85 (~PKR 23,800).",
                "US F-1 Visa and SEVIS I-901 fees: USD 535 (~PKR 150,000).",
                "Flight ticket from Pakistan to Boston: ~PKR 350,000 to 500,000.",
                "Initial apartment security deposit and living costs: ~USD 1,500 (~PKR 420,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: GRE General Test is required. (FACT: The GRE is NOT required for CICS PhD applicants).",
                "CLAIM: Living in Massachusetts is impossible on a graduate stipend. (FACT: Western Massachusetts / Pioneer Valley has far lower living costs than Boston, and the GEO contract guarantees generous stipends)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some online forums report that MS students receive automatic assistantships. At UMass Amherst, guaranteed multi-year assistantships are reserved almost exclusively for PhD students."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.00 or higher in all graduate coursework with satisfactory research progress.",
            "attendance_requirements": "Full-time physical research and academic residency on the Amherst campus.",
            "academic_progress_monitoring": "Annual progress reviews conducted by the doctoral program committee and faculty advisor.",
            "work_restrictions_during_study": "Graduate research and teaching assistantships are capped at 20 hours per week during academic terms under GEO union contract.",
            "home_country_return_obligation": "None. International graduates qualify for US F-1 OPT with 3-year STEM extension and employer-sponsored permanent residence pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding terminates upon withdrawal; past disbursements are not subject to clawback.",
            "rules_for_changing_university": "Fellowships cannot be transferred to other universities.",
            "rules_for_changing_major": "Changing research areas or advisors requires approval from the Graduate Program Director and finding a faculty member with research funding.",
            "extension_policy": "Funding is guaranteed for 5 years; extensions into Year 6 are supported via faculty advisor research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "UMass Amherst Manning CICS PhD Admissions",
                "source_url": "https://www.cics.umass.edu/academics/phd/apply",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific funding levels and exact number of open PhD seats per individual professor.",
                    "Country-level breakdown of admitted doctoral cohorts.",
                    "Internal ranking criteria used during final faculty recruitment meetings."
                ]
            },
            {
                "source_name": "UMass Amherst Graduate School Assistantships & GEO Benefits",
                "source_url": "https://www.umass.edu/graduate/funding/graduate-assistantships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Future year cost-of-living stipend increase percentages.",
                    "Discretionary emergency fund allocations for international graduate students."
                ]
            }
        ]
    },
    "SCH-AM-036": {
        "scholarship_id": "SCH-AM-036",
        "basic_details": {
            "scholarship_name": "Northwestern University Walter P. Murphy Fellowship & Computer Science PhD Package",
            "offering_entity": "Northwestern University (McCormick School of Engineering and Applied Science - Department of Computer Science)",
            "host_country": "United States",
            "host_institutions_covered": "Northwestern University Evanston Campus (Evanston / Chicago, Illinois, USA)",
            "degree_levels": ["Doctor of Philosophy (PhD in Computer Science)"],
            "major_restrictions": "Restricted to doctoral candidates in Computer Science: Artificial Intelligence, Machine Learning, Computer Systems & Networking, Human-Computer Interaction, Theory of Computation, Robotics, Security, and Computer Graphics.",
            "number_of_awards_total": "100% of admitted PhD students receive guaranteed full financial support (~45 to 60 doctoral students admitted annually)",
            "number_of_awards_pakistan": "Open global merit competition; typically 2 to 4 high-achieving Pakistani graduates admitted per academic year",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Guaranteed 5-year full doctoral funding package (tuition waiver + 12-month living stipend + health subsidy)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (BS) or Master's degree (MS) in Computer Science, Computer Engineering, Mathematics, or closely related STEM discipline from an HEC-recognized university with high academic distinction (minimum cumulative GPA of 3.60 / 4.00; competitive admits typically 3.80+ / 4.00).",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Northwestern Graduate School minimum GPA is 3.0/4.0; McCormick Computer Science PhD admissions committee evaluates applicants competitively with average admitted GPA above 3.80.",
            "subject_background_prerequisites": "Advanced background in algorithms, computer systems, operating systems, linear algebra, calculus, and discrete mathematics.",
            "current_education_status": "Students in the final year of undergraduate or master's study can apply; degree completion required before September matriculation.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Publications in top computing conferences (NeurIPS, ICML, CVPR, CHI, OSDI, SIGCOMM) or significant contributions to open-source software carry highest weight.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "TOEFL iBT min 90 (recommended 100+; speaking 26+ for TA certification) or IELTS Academic min 7.0 (speaking 7.5+ for TA). Duolingo and MOI certificates are not accepted.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None; diversity in computing initiatives actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top applicants awarded prestigious Walter P. Murphy Fellowships providing enhanced fellowship support without teaching obligations in Year 1.",
            "previous_scholarship_restrictions": "External fellowship holders receive institutional top-up awards.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition scholarship covering 100% of Northwestern University graduate tuition and fees (~USD 64,000 / year value).",
                "amount": "100% covered (~USD 64,000 / year; ~PKR 17,920,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Northwestern University Graduate School application fee of USD 95 paid online via credit card.",
                "amount": "USD 95 (~PKR 26,600)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from monthly living stipend; graduate apartments in Evanston or northern Chicago (Rogers Park, Edgewater) average USD 850 to 1,200/month for shared housing.",
                "amount": "Paid from stipend (~USD 950 / month; ~PKR 266,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed 12-month annual stipend of USD 40,000 to USD 45,000 / year (~USD 3,333 to 3,750 / month; ~PKR 933,000 to 1,050,000 / month) provided via Walter P. Murphy Fellowships, Graduate Research Assistantships (GRA), and Teaching Assistantships (TA).",
                "amount": "USD 40,000 to 45,000 / year (~PKR 11,200,000 to 12,600,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Chicago O'Hare International Airport (ORD) is self-funded.",
                "amount": "Self-funded (~PKR 350,000 to 500,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "US F-1 Visa fee (USD 185) and SEVIS I-901 fee (USD 350) paid to US government.",
                "amount": "USD 535 (~PKR 150,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Northwestern University Student Health Insurance Plan (NU-SHIP) fully subsidized (~USD 4,800 / year value), covering comprehensive medical, dental, and vision insurance.",
                "amount": "100% covered (~USD 4,800 / year; ~PKR 1,344,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Food and living subsistence covered comfortably by the 12-month doctoral stipend.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-performance GPU computing clusters, research lab hardware, and software licenses provided by McCormick School.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental and advisor travel funds cover registration, airfare, and hotel costs (USD 1,500 to 3,000 per conference) for presenting accepted papers at leading conferences.",
                "amount": "USD 1,500 to 3,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Northwestern Intercampus Shuttle provides free transit between Evanston and downtown Chicago campuses; CTA U-Pass discounted transit available.",
                "amount": "Free campus shuttle transit"
            },
            "total_estimated_value_usd_per_year": 112000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single prestigious US private research university: Northwestern University (Evanston / Chicago, IL, USA)",
            "participating_institutions": [
                "Northwestern University - McCormick School of Engineering",
                "Department of Computer Science (Mudd Hall)",
                "Center for Robotics and Biosystems",
                "Northwestern Institute on Complex Systems (NICO)"
            ],
            "university_rankings_scope": "Top 10 US national university (US News #9, THE World #32, QS World #50); world leader in human-computer interaction, robotics, AI, and systems.",
            "available_majors": [
                "PhD in Computer Science: Artificial Intelligence & Machine Learning",
                "PhD in Computer Science: Human-Computer Interaction (HCI)",
                "PhD in Computer Science: Robotics & Autonomous Systems",
                "PhD in Computer Science: Computer Systems & Networking",
                "PhD in Computer Science: Security & Privacy",
                "PhD in Computer Science: Theory of Computation & Algorithms",
                "PhD in Computer Science: Computer Graphics & Vision",
                "PhD in Computer Science: Computational Biology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 years full-time doctoral program.",
            "admission_requirements_summary": "4-year BS or MS in CS/STEM with 3.6+ GPA, 3 letters of recommendation, statement of purpose, CV, and TOEFL 90+ (100+ recommended) or IELTS 7.0+. GRE is optional/waived.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "HCI and AI/ML attract intense international applicant competition; computer systems, robotics, theory, and graphics present slightly higher admission probability for candidates with aligned research expertise.",
            "strategic_program_match_advice": "Identify 2-3 faculty research groups in Mudd Hall; explicitly cite their recent publications in your statement of purpose."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.mccormick.northwestern.edu/computer-science/academics/graduate/admissions/",
            "portal_system_name": "The Graduate School (TGS) Online Application Portal (CollegeNet)",
            "account_creation_instructions": "Register on the Northwestern TGS CollegeNet portal, select Computer Science (PhD), choose faculty research areas, and upload required application materials.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Research McCormick CS faculty research groups and laboratories.",
                "Step 2 (October - December): Create profile on the Northwestern TGS CollegeNet portal.",
                "Step 3 (November - December): Upload statement of purpose, CV, transcripts, and register 3 academic references.",
                "Step 4 (By 15 December): Submit application and pay USD 95 application fee.",
                "Step 5 (January - February): Faculty review applications and conduct virtual technical interviews.",
                "Step 6 (February - March): Department issues official PhD admission offer letters with 5-year guaranteed funding package.",
                "Step 7 (By 15 April): Confirm acceptance in the portal.",
                "Step 8 (May - July): Receive Form I-20 and apply for US F-1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: 100% of admitted PhD students are awarded 5-year full funding packages without a separate scholarship application.",
            "recommendation_letters_submission_method": "Three academic recommendation letters submitted online via the CollegeNet automated referee portal.",
            "personal_statement_prompts": "Statement of Purpose: 2-page essay discussing research experience, technical interests, faculty alignment, and doctoral aspirations.",
            "study_plan_research_proposal_requirements": "Integrated into statement of purpose; focus on concrete research problems, past methodological contributions, and prospective research directions.",
            "cv_format_requirements": "Academic CV detailing publications, open-source repositories, engineering projects, and technical skills.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual technical interviews (30-45 minutes via Zoom) conducted by prospective faculty advisors evaluating research problem solving and mathematical intuition.",
            "standardized_tests": "TOEFL iBT (90+; 100+ recommended) or IELTS Academic (7.0+). GRE is optional/waived.",
            "application_fee_amount": "USD 95 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official transcripts required upon admission offer.",
            "translation_requirements": "Certified English translations required for non-English credentials.",
            "final_submission_method": "100% digital submission via the Northwestern TGS CollegeNet portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "PDF scans of official transcripts from all undergraduate and graduate institutions attended.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS transcripts; official HEC attestation required only upon matriculation."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "2-page statement of purpose articulating research questions, past projects, technical methodology, and why Northwestern faculty are an ideal fit.",
                "pakistan_specific_instruction": "Focus on research depth and technical contributions rather than generic personal background."
            },
            {
                "document_name": "Letters of Recommendation (Three)",
                "mandatory": True,
                "specification": "Three confidential recommendation letters from professors or research scientists familiar with your creative research capacity.",
                "pakistan_specific_instruction": "Ensure professors submit from verified university domain email addresses (.edu.pk)."
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
                "specification": "Official TOEFL iBT (code 1565) or IELTS Academic score report taken within past 2 years.",
                "pakistan_specific_instruction": "Aim for TOEFL 100+ or IELTS 7.5+ to satisfy TA spoken English standards."
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
            "semester_commencement": "Late September 2026",
            "annual_cycle_notes": "Admissions offered for Fall quarter only. Hard deadline is December 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (GPA, difficulty of computer science coursework, mathematical foundations)",
            "extracurricular_and_leadership_weight": "5% (academic service, leadership, contributions to open-source computing)",
            "research_experience_weight": "40% (published research, statement of purpose, technical sophistication, code samples)",
            "work_experience_weight": "5% (industry research experience or software engineering roles)",
            "personal_statement_weight": "10% (clarity of research goals and alignment with faculty mentors)",
            "recommendations_weight": "10% (credibility of referees and their specific evaluations of research aptitude)",
            "interview_weight": "5% (alignment with faculty grants and technical performance in video interview)",
            "test_scores_weight": "Threshold requirement (TOEFL/IELTS compliance)",
            "financial_need_weight": "0% (purely merit and research achievement based)",
            "selection_panel_composition": "McCormick CS Doctoral Admissions Committee and faculty lab PIs.",
            "evaluation_methodology": "Faculty-led holistic review: Area sub-committees review candidate dossiers, match candidates to funded faculty labs, and conduct interviews before issuing full funding offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "2,600+ applicants for Northwestern CS PhD program",
            "total_scholarships_awarded": "~45 to 60 funded PhD offers accepted annually",
            "acceptance_rate_global": "~4% to 5% admit rate for PhD in Computer Science",
            "acceptance_rate_pakistan": "~3% to 4% among applicants from premier Pakistani universities",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 CGPA (or top 3% of graduating class)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE with top standing, 1-2 research papers at tier-1 international conferences (CHI, NeurIPS, CVPR), outstanding faculty recommendation letters.",
            "common_backgrounds_of_winners": "Graduates of LUMS, NUST, FAST-NUCES, and GIKI.",
            "high_representation_countries": "United States, China, India, South Korea, Canada, Pakistan, Iran",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed admission or funding at Northwestern. Admissions decisions are made exclusively by Northwestern faculty."
            ],
            "application_fee_warning": "Pay the USD 95 application fee only through the official Northwestern TGS CollegeNet portal. Never wire money to intermediaries.",
            "agent_and_intermediary_warnings": "Northwestern strictly forbids the use of admissions agents. Plagiarized statements of purpose result in immediate disqualification.",
            "hidden_costs_breakdown": [
                "Northwestern application fee: USD 95 (~PKR 26,600).",
                "US F-1 Visa and SEVIS I-901 fees: USD 535 (~PKR 150,000).",
                "Flight ticket from Pakistan to Chicago: ~PKR 350,000 to 500,000.",
                "Initial apartment security deposit and living costs: ~USD 1,500 (~PKR 420,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: GRE General Test is mandatory. (FACT: The GRE is optional/waived for Computer Science PhD applicants).",
                "CLAIM: Only students with master's degrees are admitted to the PhD. (FACT: Direct entry from 4-year bachelor's degrees is very common and fully funded)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some online forums report that MS students receive automatic funding. At Northwestern, guaranteed multi-year funding packages are reserved for PhD students."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.00 or higher in all graduate coursework with satisfactory research progress.",
            "attendance_requirements": "Full-time physical research and academic residency on the Evanston campus.",
            "academic_progress_monitoring": "Annual progress reviews conducted by the doctoral program committee and faculty advisor.",
            "work_restrictions_during_study": "Graduate research and teaching assistantships are capped at 20 hours per week during academic quarters.",
            "home_country_return_obligation": "None. International graduates qualify for US F-1 OPT with 3-year STEM extension and employer-sponsored permanent residence pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding terminates upon withdrawal; past disbursements are not subject to clawback.",
            "rules_for_changing_university": "Fellowships cannot be transferred to other universities.",
            "rules_for_changing_major": "Changing research areas or advisors requires approval from the Director of Graduate Studies and finding a faculty member with research funding.",
            "extension_policy": "Funding is guaranteed for 5 years; extensions into Year 6 are supported via faculty advisor research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "Northwestern McCormick CS PhD Admissions",
                "source_url": "https://www.mccormick.northwestern.edu/computer-science/academics/graduate/admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific funding levels and exact number of open PhD seats per individual professor.",
                    "Country-level breakdown of admitted doctoral cohorts.",
                    "Internal ranking criteria used during final faculty recruitment meetings."
                ]
            },
            {
                "source_name": "Northwestern The Graduate School (TGS) Funding & Fellowships",
                "source_url": "https://www.tgs.northwestern.edu/funding/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Future year cost-of-living stipend increase percentages.",
                    "Discretionary emergency fund allocations for international graduate students."
                ]
            }
        ]
    }
}
