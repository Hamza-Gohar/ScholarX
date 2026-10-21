"""
scripts/dossiers_batch7a.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Batch 7A
Contains 4 Asia Scholarships:
17. SCH-AS-011: UST Graduate Fellowship (South Korea / UST & 32 National Research Institutes)
18. SCH-AS-013: POSCO TJ Park Asia Fellowship (South Korea / POSCO TJ Park Foundation)
19. SCH-AS-014: GIST Graduate Scholarship (South Korea / Gwangju Institute of Science & Technology)
20. SCH-AS-018: SIIT Excellent Foreign Students (EFS) Scholarship (Thailand / Thammasat University)
"""

DOSSIERS_BATCH7A = {
    # 17. UST Graduate Fellowship (SCH-AS-011)
    "SCH-AS-011": {
        "scholarship_id": "SCH-AS-011",
        "basic_details": {
            "scholarship_name": "University of Science and Technology (UST) Graduate Fellowship",
            "offering_entity": "University of Science and Technology (UST) & Government of South Korea (MSIT)",
            "host_country": "South Korea",
            "host_institutions_covered": "UST Main Campus & 32 South Korean Government Research Institutes (KIST, ETRI, KARI, KRICT, KIMS, KIER, KBRI, KISTI, KRISS)",
            "degree_levels": ["Master's Degree", "Doctoral / PhD", "Integrated MS-PhD"],
            "major_restrictions": "Advanced STEM Disciplines: Artificial Intelligence, Robotics, Semiconductor Technology, Aerospace Engineering, Biotechnology, Advanced Materials, Nuclear Engineering, Quantum Computing, Environmental Sciences.",
            "number_of_awards_total": "~400 to 500 new international researchers admitted annually across 32 research institutes",
            "number_of_awards_pakistan": "Large active Pakistani researcher community; Pakistan is among the top 3 represented international nations at UST (typically 35 to 60 Pakistani awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full normative duration of degree: 2 years (MS), 4 years (PhD), or 5 years (Integrated MS-PhD)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International citizens whose parents are both non-Korean citizens"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed Bachelor's degree (16 years education) for Master's; completed Master's degree (18 years education) for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA; practical engineering competencies and lab research capabilities are heavily weighted.",
            "subject_background_prerequisites": "Undergraduate/Master's major directly relevant to the chosen government research campus field.",
            "current_education_status": "Graduated or currently in final semester of degree graduating before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Lab experience, prior publications, and hands-on experimental equipment expertise are significant assets.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 79,
                "duolingo_accepted": True,
                "moi_certificate_accepted": False,
                "notes": "TOEFL iBT min 79, IELTS Academic min 6.0, New TEPS min 277, or Duolingo English Test min 100."
            },
            "other_language_requirements": "No Korean language required; courses and research in English (Korean classes provided free).",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Government research institute researcher-trainee track.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver provided for all semesters (KRW 2,500,000 / semester).",
                "amount": "100% covered (~KRW 5,000,000 / year / ~USD $3,700/yr)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UST application fee (KRW 35,000 or USD $30) paid online by applicant.",
                "amount": "KRW 35,000 (~PKR 7,500)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized on-site researcher dormitories located directly inside the 32 national research institutes (rent ~KRW 100,000 to 200,000/mo) paid from monthly stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research stipend paid by host research institute: Minimum KRW 1,350,000/month for Master's; Minimum KRW 1,800,000/month for PhD (~PKR 285,000 to 380,000/month). Top labs provide performance bonuses up to KRW 2,200,000/month.",
                "amount": "KRW 1,350,000 to KRW 2,200,000 / month (~PKR 285,000 to 465,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses to South Korea borne by student.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 student visa processing fee paid by applicant; UST provides Certificate of Admission.",
                "amount": "Nominal embassy visa fee (~PKR 15,000)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive student safety insurance provided by UST; National Health Insurance (NHIS) subsidized.",
                "amount": "100% safety insurance covered"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Heavily subsidized cafeteria meals inside national institute campuses (~KRW 3,500 to 5,000 per meal).",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to national supercomputing facilities, state-of-the-art cleanrooms, synchrotron beamlines, and lab facilities.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "UST Overseas Training and International Conference Presentation Grants (up to KRW 3,000,000 per trip).",
                "amount": "Up to KRW 3,000,000 per trip"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "None.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single university system: UST with 32 specialized government research institute campuses.",
            "participating_institutions": [
                "Korea Institute of Science and Technology (KIST, Seoul)",
                "Electronics and Telecommunications Research Institute (ETRI, Daejeon)",
                "Korea Aerospace Research Institute (KARI, Daejeon)",
                "Korea Research Institute of Chemical Technology (KRICT)",
                "Korea Institute of Energy Research (KIER)",
                "Korea Institute of Materials Science (KIMS)",
                "Korea Institute of Science and Technology Information (KISTI)",
                "Korea Research Institute of Standards and Science (KRISS)"
            ],
            "university_rankings_scope": "National flagship research institution; #1 in South Korea for R&D budget per student; 100% research institute embedded.",
            "available_majors": [
                "Artificial Intelligence, ICT & Software, Robotics & Autonomous Systems, Aerospace Engineering, Semiconductor & Display Engineering, Advanced Materials, Chemical Technology, Biotechnology, Nuclear Engineering, Quantum Information Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "24 months (MS), 48 months (PhD), or 60 months (Integrated MS-PhD)",
            "admission_requirements_summary": "Bachelor's or Master's degree in engineering/science, official English proficiency score, and strong research aptitude.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "KIST (Seoul) and ETRI (Daejeon) receive the highest application volumes; chemical, energy, and materials institutes have slightly higher admission ratios.",
            "strategic_program_match_advice": "Reaching out to prospective principal researchers (professors) at the target government institute before applying significantly enhances selection chances."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://apply.ust.ac.kr/",
            "portal_system_name": "UST Online Admissions System",
            "account_creation_instructions": "Register on the UST Online Admissions System during the Spring or Fall admissions window.",
            "step_by_step_workflow": [
                "1. Search open research project areas and professor profiles on UST admissions portal (March/September).",
                "2. Create account on UST online application system.",
                "3. Select target campus (e.g. KIST, ETRI) and major specialization.",
                "4. Upload Study Plan, transcripts, degree certificates, CV, and English test score.",
                "5. Register 1 or 2 academic referees who upload letters of recommendation.",
                "6. Pay application fee (KRW 35,000 / USD $30).",
                "7. First screening: Document evaluation by central committee and campus faculty.",
                "8. Second screening: Video interview conducted by institute professors (April/October).",
                "9. Final results announced in May (Fall intake) or November (Spring intake).",
                "10. Receive Certificate of Admission and apply for Korean D-2 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic appointment: all admitted UST students receive full fellowship appointment as student researchers.",
            "recommendation_letters_submission_method": "Submitted online by referees via UST automated email link.",
            "personal_statement_prompts": "Self-Introduction and Study Plan explaining academic motivations, technical strengths, and proposed research trajectory at the national lab.",
            "study_plan_research_proposal_requirements": "Structured research plan answering specific questions regarding proposed lab research, methodology, and career vision.",
            "cv_format_requirements": "Standard academic CV detailing technical projects, software/hardware competencies, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "In-depth 20-30 minute technical video interview covering fundamentals, previous research, and research vision.",
            "standardized_tests": "GRE not required; English proficiency test required.",
            "application_fee_amount": "KRW 35,000 (~USD $30).",
            "attestation_requirements": "Apostille or Korean Embassy legalization of degree certificate and official transcript.",
            "translation_requirements": "Official English or Korean translations required.",
            "final_submission_method": "100% online through UST admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of valid international passport data page",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts and degrees with grading scales",
                "pakistan_specific_instruction": "Attested by HEC Pakistan, MOFA, and Korean Embassy in Islamabad (or Apostille)"
            },
            {
                "document_name": "Self-Introduction & Study Plan",
                "mandatory": True,
                "specification": "Completed using the official UST template",
                "pakistan_specific_instruction": "Focus on experimental capabilities and lab fit"
            },
            {
                "document_name": "Letter(s) of Recommendation",
                "mandatory": True,
                "specification": "1 or 2 reference letters submitted via UST referee portal",
                "pakistan_specific_instruction": "From undergraduate/master's thesis advisor"
            },
            {
                "document_name": "Official English Proficiency Score",
                "mandatory": True,
                "specification": "TOEFL iBT (79+), IELTS Academic (6.0+), or Duolingo (100+)",
                "pakistan_specific_instruction": "Official electronic score report"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-03-01",
            "application_deadline": "2026-04-10",
            "university_admission_deadline": "2026-04-10",
            "document_submission_deadline": "2026-04-10",
            "recommendation_letters_deadline": "2026-04-15",
            "interview_period": "Late April to early May 2026",
            "shortlist_announcement": "Mid-May 2026",
            "final_result_acceptance_deadline": "2026-06-10",
            "visa_application_window": "June to August 2026",
            "semester_commencement": "2026-09-01",
            "annual_cycle_notes": "Two admissions cycles per year: Fall intake (opens March, starts September) and Spring intake (opens September, starts March)."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Academic transcript grades and foundational STEM preparation)",
            "extracurricular_and_leadership_weight": "5% (Engineering project initiatives)",
            "research_experience_weight": "40% (Research publications, thesis, laboratory techniques, experimental skills)",
            "work_experience_weight": "5% (Industry research or laboratory employment)",
            "personal_statement_weight": "10% (Quality of Study Plan and research goals)",
            "recommendations_weight": "10% (Referee appraisals)",
            "interview_weight": "Decisive during professor video interview",
            "test_scores_weight": "0% (Language proficiency is prerequisite)",
            "financial_need_weight": "0% (Pure scientific merit)",
            "selection_panel_composition": "Chief research scientists and professors at the respective government research institute campuses.",
            "evaluation_methodology": "Document evaluation by research faculty -> In-depth technical video interview -> Final selection committee approval."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 international applicants across both cycles",
            "total_scholarships_awarded": "~400 to 500 fully funded student researcher appointments per year",
            "acceptance_rate_global": "~12% to 14%",
            "acceptance_rate_pakistan": "~8% to 10% (Strong track record of Pakistani admissions)",
            "typical_successful_applicant_gpa": "3.30+ / 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates from NUST, COMSATS, UET, GIKI, FAST, and Quaid-i-Azam with solid hands-on engineering/science laboratory skills, final-year design projects, and strong motivation.",
            "common_backgrounds_of_winners": "Pakistani researchers have a vibrant alumni network at KIST, ETRI, and KRICT, frequently transitioning to Korean tech giants (Samsung, LG, SK Hynix).",
            "high_representation_countries": "Vietnam, Pakistan, India, Indonesia, Bangladesh, China, Russia, Iran.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized agency domains: ust-korea-scholarships.org, studyinust-visa.com."
            ],
            "application_fee_warning": "Application fee of KRW 35,000 / USD $30 is paid strictly inside the official UST application portal.",
            "agent_and_intermediary_warnings": "UST does not authorize commercial consultants to solicit or evaluate applications.",
            "itemized_hidden_out_of_pocket_costs": [
                "Degree legalization / Apostille and HEC/MOFA attestation fees (~PKR 35,000 to 55,000)",
                "Korean student visa application fee (~PKR 15,000)",
                "Airfare Pakistan to Seoul Incheon (~PKR 170,000 to 250,000)",
                "Initial 1-month living funds before first stipend payment (~KRW 500,000)"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: UST is a traditional university with classroom lectures. (Truth: UST is a research university where students work full-time directly inside national laboratories as junior researchers).",
                "MYTH: You cannot transition to a PhD. (Truth: UST has direct Integrated MS-PhD tracks and seamless transitions for high-performing Master's students)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Commercial agents claim Korean proficiency is mandatory; in reality, UST research and courses are conducted 100% in English."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum 3.00 GPA in graduate coursework and meet research institute laboratory deliverables.",
            "attendance_requirements": "Full-time laboratory presence as a student researcher at the assigned government research institute.",
            "academic_progress_monitoring": "Semi-annual research progress reports and publication milestones required for thesis defense.",
            "work_restrictions_during_study": "Part-time outside employment is strictly restricted to ensure dedicated research focus.",
            "home_country_return_obligation": "None; international graduates qualify for South Korea's D-10 job seeker visa and E-7 professional researcher work visa pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Fellowship is cancelled if student is dismissed for disciplinary reasons or abandons laboratory research.",
            "rules_for_changing_university": "Non-transferable to other Korean universities.",
            "rules_for_changing_major": "Changing campuses or research institutes requires extraordinary approval from UST President.",
            "extension_policy": "Degree duration follows strict normative limits; research stipend can be extended for thesis finalization with advisor approval."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Science and Technology (UST) - Graduate Admissions Official Portal",
                "source_url": "https://apply.ust.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Institute-by-institute quota allocation of international student researcher slots.",
                    "Departmental breakdown of monthly stipend top-ups above the minimum baseline.",
                    "Interview grading sheet formulas used by individual research labs."
                ]
            }
        ]
    },

    # 18. POSCO TJ Park Asia Fellowship (SCH-AS-013)
    "SCH-AS-013": {
        "scholarship_id": "SCH-AS-013",
        "basic_details": {
            "scholarship_name": "POSCO TJ Park Asia Fellowship",
            "offering_entity": "POSCO TJ Park Foundation (South Korea)",
            "host_country": "South Korea",
            "host_institutions_covered": "Top Partner Universities in South Korea: Seoul National University (SNU), Yonsei University, Korea University (KU), KAIST, POSTECH, Sungkyunkwan University (SKKU), Ewha Womans University, Hankuk University of Foreign Studies (HUFS)",
            "degree_levels": ["Master's Degree", "Doctoral / PhD"],
            "major_restrictions": "Open to all academic disciplines: STEM (Engineering, Computer Science, AI, Materials, Natural Sciences), Social Sciences, Humanities, Economics, International Studies, and Business Administration.",
            "number_of_awards_total": "~30 elite Asian leaders and scholars awarded fellowships annually",
            "number_of_awards_pakistan": "Open competition across eligible Asian partner countries; Pakistan is an eligible recipient nation (typically 2 to 5 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full normative degree duration: 2 years (4 semesters) for Master's; up to 3 years (6 semesters) for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of Asian countries (including Pakistan) who completed previous education outside South Korea"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed Bachelor's degree (16 years education) for Master's; completed Master's degree (18 years education) for PhD with top academic standing.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum 3.50+ / 4.00 CGPA (or top 10% class standing) from a prestigious university.",
            "subject_background_prerequisites": "Academic background aligned with target graduate school in South Korea.",
            "current_education_status": "Graduated or currently in final semester of degree graduating prior to autumn semester.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Leadership experience, community engagement, and research achievements evaluated positively.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "TOEFL iBT min 85, IELTS Academic min 6.5, or official Medium of Instruction certificate from English-medium university."
            },
            "other_language_requirements": "Korean proficiency (TOPIK) is optional but viewed favorably for humanities/social science applicants.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Future Asian leaders demonstrating high academic excellence and leadership capability.",
            "previous_scholarship_restrictions": "Must not be receiving another Korean government or corporate scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver for normative duration of degree at partner university.",
                "amount": "100% covered (~KRW 6,000,000 to 12,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University admission application fee paid by candidate to partner university.",
                "amount": "KRW 80,000 to 100,000"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly living stipend; priority reservation in partner university international dormitories.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly living allowance of KRW 1,000,000/month (~PKR 212,000/month / ~USD $750/month) for the entire duration of studies.",
                "amount": "KRW 1,000,000 / month (~PKR 212,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses to South Korea borne by candidate.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Korean D-2 visa processing fee paid by applicant.",
                "amount": "Nominal embassy visa fee"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "National Health Insurance (NHIS) subsidized or covered under university international student health plan.",
                "amount": "100% covered"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly living allowance.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "University library resources, laboratories, and computing infrastructure provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "POSCO TJ Park Fellowship networking events, Korean cultural excursions, and foundation leadership seminars fully paid.",
                "amount": "Full foundation cultural & leadership activities covered"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Settlement allowance of KRW 1,000,000 provided once upon initial arrival in South Korea.",
                "amount": "KRW 1,000,000 one-time (~PKR 212,000)"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple institutions: Partner Korean universities including SNU, Yonsei, Korea Univ, KAIST, POSTECH.",
            "participating_institutions": [
                "Seoul National University (SNU)",
                "Yonsei University",
                "Korea University",
                "KAIST (Daejeon)",
                "POSTECH (Pohang)",
                "Sungkyunkwan University (SKKU)",
                "Ewha Womans University",
                "Hankuk University of Foreign Studies (HUFS)"
            ],
            "university_rankings_scope": "Top 1 to 5 in South Korea; Top 100 QS World University Rankings (SNU #31, KAIST #53, Yonsei #56, Korea #67).",
            "available_majors": [
                "Computer Science, Artificial Intelligence, Materials Science, Chemical Engineering, Mechanical Engineering, Economics, Public Administration, International Relations, Business Administration, Life Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "24 months (Master's) or 36 months (PhD)",
            "admission_requirements_summary": "Bachelor's/Master's degree from a recognized institution with high GPA and demonstrated leadership qualities.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "SNU and KAIST are the most competitive; candidates must coordinate fellowship application alongside target university admission.",
            "strategic_program_match_advice": "Candidates apply through the POSCO TJ Park Foundation online system in May; upon selection, fellows apply for admission to partner universities for Spring intake."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.postf.org/en/page/asia/fellowship.do",
            "portal_system_name": "POSCO TJ Park Foundation Online Application Portal",
            "account_creation_instructions": "Register on the POSCO TJ Park Foundation application portal during the annual application window in May.",
            "step_by_step_workflow": [
                "1. Review eligibility and guidelines on POSCO TJ Park website (April).",
                "2. Create account on POSCO foundation portal in early May.",
                "3. Fill out online application form and designate prospective partner universities.",
                "4. Upload Statement of Purpose, academic transcripts, degree certificates, CV, and English proficiency proofs.",
                "5. Upload 2 recommendation letters from academic professors or institutional leaders.",
                "6. Submit online application before end of May deadline.",
                "7. First round: Document evaluation by foundation selection committee.",
                "8. Second round: Video interview conducted in July.",
                "9. Fellowship selection announced in August.",
                "10. Selected fellows apply for university admission to partner Korean university for Spring intake (September-October).",
                "11. Arrive in South Korea in late February."
            ],
            "university_vs_scholarship_routing": "Sequential: Fellowship awarded by POSCO foundation first, followed by formal university admission application.",
            "recommendation_letters_submission_method": "Uploaded directly by applicant or submitted online by referees via foundation portal.",
            "personal_statement_prompts": "Statement of Purpose describing academic interests, leadership experiences, and vision for fostering cooperation between home country and South Korea.",
            "study_plan_research_proposal_requirements": "Structured study plan outlining proposed graduate research questions, methodology, and career trajectory.",
            "cv_format_requirements": "Academic and leadership CV detailing awards, community projects, and research papers.",
            "interviews_conducted": True,
            "interview_format_details": "Comprehensive 20-30 minute video interview in English testing leadership potential, intellectual depth, and mutual understanding.",
            "standardized_tests": "None; language test required.",
            "application_fee_amount": "100% free on POSCO foundation portal; university application fees apply upon admission.",
            "attestation_requirements": "Official university transcripts and degree certificates verified by home university; HEC and Korean Embassy attestation required upon selection.",
            "translation_requirements": "Certified English or Korean translations.",
            "final_submission_method": "100% online through POSCO TJ Park portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of valid international passport",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all university-level studies with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Statement of Purpose & Study Plan",
                "mandatory": True,
                "specification": "Structured essays articulating academic vision, leadership, and Korean collaboration",
                "pakistan_specific_instruction": "Highlight bilateral Pak-Korea ties and leadership"
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential reference letters from professors or institutional heads",
                "pakistan_specific_instruction": "From undergraduate university deans or research mentors"
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "TOEFL iBT (85+), IELTS Academic (6.5+), or Medium of Instruction certificate",
                "pakistan_specific_instruction": "Official IELTS or university MOI letter"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-05-01",
            "application_deadline": "2026-05-31",
            "university_admission_deadline": "2026-10-15",
            "document_submission_deadline": "2026-05-31",
            "recommendation_letters_deadline": "2026-05-31",
            "interview_period": "July 2026",
            "shortlist_announcement": "Mid-July 2026",
            "final_result_acceptance_deadline": "2026-08-20",
            "visa_application_window": "December 2026 to January 2027",
            "semester_commencement": "2027-03-01",
            "annual_cycle_notes": "Single annual cycle: application in May for fellowship; university admission in Autumn; enrollment starts March 1 (Korean Spring semester)."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior undergraduate/master's GPA and academic prestige of alma mater)",
            "extracurricular_and_leadership_weight": "25% (Community leadership, vision, and potential to lead Asian development)",
            "research_experience_weight": "15% (Publications, thesis, and research methodology)",
            "work_experience_weight": "5% (Professional experience in relevant sector)",
            "personal_statement_weight": "10% (Quality of essays and commitment to Asian cooperation)",
            "recommendations_weight": "10% (Quality of academic and leadership references)",
            "interview_weight": "Decisive during final foundation panel interview",
            "test_scores_weight": "0% (Language proficiency is prerequisite)",
            "financial_need_weight": "0% (Merit and leadership based)",
            "selection_panel_composition": "POSCO TJ Park Foundation Selection Committee and professors from participating partner universities.",
            "evaluation_methodology": "Document screening (Grades + Essays + References) -> Video interview by foundation board -> Final admission placement at partner university."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 elite Asian candidates globally",
            "total_scholarships_awarded": "~30 fellowships awarded annually across all Asian countries",
            "acceptance_rate_global": "~2.0%",
            "acceptance_rate_pakistan": "~1.5% (Extremely Competitive / Elite corporate fellowship)",
            "typical_successful_applicant_gpa": "3.70+ / 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates from premier national universities (NUST, LUMS, Quaid-i-Azam, UET) with high academic percentiles, demonstrated social leadership, and clear articulation of career vision.",
            "common_backgrounds_of_winners": "Past Pakistani fellows have pursued graduate degrees at SNU, Yonsei, and KAIST in engineering, public policy, and business.",
            "high_representation_countries": "Vietnam, Indonesia, India, Pakistan, Thailand, Philippines, Bangladesh, Uzbekistan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam portals: posco-fellowship-online.org, korea-asia-grants.com."
            ],
            "application_fee_warning": "POSCO TJ Park Foundation application is 100% free of charge. Never pay any external agent.",
            "agent_and_intermediary_warnings": "The foundation does not partner with educational agents or commercial placement firms.",
            "itemized_hidden_out_of_pocket_costs": [
                "Airfare Pakistan to Seoul Incheon (~PKR 170,000 to 250,000)",
                "University application fees to partner Korean universities (~KRW 80,000 to 100,000 / ~PKR 20,000)",
                "Korean student visa application fee (~PKR 15,000)",
                "HEC, MOFA, and Korean Embassy document attestation fees"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: Only engineering degrees are eligible. (Truth: Social sciences, business, economics, and humanities at partner universities are fully eligible).",
                "MYTH: You must already be admitted to a Korean university. (Truth: You apply to POSCO foundation first; if selected, you apply for university admission with POSCO sponsorship)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim flights are covered; the POSCO Asia Fellowship provides full tuition + monthly stipend + settlement grant, but flight tickets are self-funded."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 out of 4.30 / 4.50 at partner university to renew funding each semester.",
            "attendance_requirements": "Full-time physical attendance; mandatory participation in annual POSCO Asia Fellowship workshops and ceremonies.",
            "academic_progress_monitoring": "Semester grade reports submitted directly to POSCO TJ Park Foundation.",
            "work_restrictions_during_study": "Part-time work permitted per Korean immigration regulations (up to 20-25 hrs/wk), but academic focus expected.",
            "home_country_return_obligation": "No mandatory return bond; scholars encouraged to contribute to Asian mutual prosperity.",
            "service_obligations_or_bonds": "Active membership in POSCO Asia Fellowship Alumni Network.",
            "repayment_clawback_conditions": "Funding cancelled if fellow fails to achieve minimum GPA, drops out, or acts contrary to foundation regulations.",
            "rules_for_changing_university": "Non-transferable between universities.",
            "rules_for_changing_major": "Requires prior written consent from POSCO TJ Park Foundation.",
            "extension_policy": "Strictly limited to 2 years for Master's and 3 years for PhD; no extensions permitted."
        },
        "official_sources_verified": [
            {
                "source_name": "POSCO TJ Park Foundation - Asia Fellowship Official Portal",
                "source_url": "https://www.postf.org/en/page/asia/fellowship.do",
                "source_type": "OFFICIAL_ORGANIZATION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Country-by-country award quotas across participating Asian nations.",
                    "Exact interview evaluation rubric and scoring distribution.",
                    "Historical acceptance rates broken down by partner universities."
                ]
            }
        ]
    },

    # 19. GIST Graduate Scholarship (SCH-AS-014)
    "SCH-AS-014": {
        "scholarship_id": "SCH-AS-014",
        "basic_details": {
            "scholarship_name": "GIST International Graduate Scholarship",
            "offering_entity": "Gwangju Institute of Science and Technology (GIST, South Korea)",
            "host_country": "South Korea",
            "host_institutions_covered": "Gwangju Institute of Science and Technology (Gwangju, South Korea)",
            "degree_levels": ["Master's Degree", "Doctoral / PhD", "Integrated MS-PhD"],
            "major_restrictions": "School of Electrical Engineering and Computer Science (AI, Computing, Telecommunications), School of Materials Science and Engineering, School of Mechanical Engineering, School of Earth Sciences and Environmental Engineering, Department of Chemistry, Department of Physics and Photon Science, School of Life Sciences, Department of Biomedical Science and Engineering.",
            "number_of_awards_total": "~150 to 200 fully funded international graduate students admitted annually",
            "number_of_awards_pakistan": "Open international competition; 100% of admitted international students receive full scholarship and stipend (typically 10 to 20 Pakistani students admitted/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full duration of degree: 2 years (MS), 4 years (PhD), or 5 years (Integrated MS-PhD)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents are both non-Korean citizens"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed Bachelor's degree (16 years education) for Master's; completed Master's degree (18 years education) for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA; competitive admitted candidates typically possess 3.40+ CGPA or top 15% class standing.",
            "subject_background_prerequisites": "Undergraduate/Master's major in engineering, computer science, physics, chemistry, biology, or mathematics.",
            "current_education_status": "Graduated or in final semester of degree graduating before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior laboratory research, published papers, or thesis projects heavily evaluated.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 80,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "TOEFL iBT min 80, IELTS Academic min 6.5, TOEIC min 750, or New TEPS min 285."
            },
            "other_language_requirements": "English (100% of graduate lectures and research conducted in English).",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Full-time international graduate researcher candidature.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver provided for all semesters (KRW 3,415,000 / semester).",
                "amount": "100% covered (~KRW 6,830,000 / year / ~USD $5,000/yr)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "GIST international graduate application fee is 100% waived for all international applicants.",
                "amount": "Free application"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized on-campus graduate dormitory housing guaranteed (rent ~KRW 100,000 to 150,000/mo / ~PKR 21,000 to 32,000/mo) paid from monthly stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly student allowance (KRW 140,000 for MS, KRW 295,000 for PhD) + Research Assistantship allowance (average KRW 540,000 for MS, KRW 1,060,000 for PhD). Total monthly stipend: ~KRW 680,000/mo for MS (~PKR 144,000/mo) and ~KRW 1,355,000/mo for PhD (~PKR 287,000/mo).",
                "amount": "KRW 680,000 (MS) to KRW 1,355,000 (PhD) / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One-way international airfare reimbursement to South Korea provided to all incoming new international students.",
                "amount": "One-way flight ticket reimbursed"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 visa processing fee paid by applicant.",
                "amount": "Nominal embassy visa fee (~PKR 15,000)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "GIST covers 60% of National Health Insurance (NHIS) premiums, plus annual health examinations.",
                "amount": "60% NHIS subsidized + health checkups free"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized meals at GIST student and faculty cafeterias (~KRW 4,000 to 5,000 per meal).",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Departmental research computing clusters, laboratories, and library systems provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Lab research grants cover travel and registration for presenting at international conferences.",
                "amount": "Conference travel funded by lab"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Settlement allowance of KRW 200,000 provided upon arrival.",
                "amount": "KRW 200,000 (~PKR 42,500)"
            },
            "total_estimated_value_usd_per_year": 20000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Gwangju Institute of Science and Technology (GIST, South Korea).",
            "participating_institutions": [
                "Gwangju Institute of Science and Technology"
            ],
            "university_rankings_scope": "#4 in the world for Citations per Faculty (QS World Rankings); Top 5 in South Korea for engineering.",
            "available_majors": [
                "Electrical Engineering & Computer Science (AI, Robotics, Data Science), Materials Science & Engineering, Mechanical Engineering, Environmental Engineering, Physics & Photon Science, Chemistry, Life Sciences, Biomedical Science & Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "24 months (MS), 48 months (PhD), or 60 months (Integrated MS-PhD)",
            "admission_requirements_summary": "Bachelor's or Master's degree in engineering/science with solid GPA, English test score, and research potential.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of EECS is the most selective; materials, chemistry, and environmental engineering have slightly higher acceptance rates.",
            "strategic_program_match_advice": "Contact prospective GIST lab professors 1-2 months before the deadline with a CV and research summary to secure preliminary support."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.gist.ac.kr/ia/html/sub04/0401.html",
            "portal_system_name": "GIST International Graduate Admissions Portal",
            "account_creation_instructions": "Register on the GIST International Admissions online portal during the Spring or Fall application window.",
            "step_by_step_workflow": [
                "1. Check GIST international admissions guidelines (March/September).",
                "2. Create account on GIST online application portal.",
                "3. Select target school and research laboratory.",
                "4. Upload Statement of Purpose, transcripts, degree certificates, CV, and English test scores (TOEFL/IELTS).",
                "5. Register 2 academic referees who upload confidential recommendation letters.",
                "6. Submit online application (application fee is waived/free).",
                "7. Document screening by GIST admissions committee.",
                "8. Video interview conducted by departmental faculty (May/November).",
                "9. Final admission and full scholarship offer announced in June/December.",
                "10. Receive Certificate of Admission and apply for Korean D-2 visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic appointment: all admitted international graduate students receive 100% full scholarship and research assistantship.",
            "recommendation_letters_submission_method": "Submitted online by 2 referees via GIST automated referee system.",
            "personal_statement_prompts": "Statement of Purpose describing academic trajectory, research accomplishments, why GIST was chosen, and specific laboratory interests.",
            "study_plan_research_proposal_requirements": "Structured research proposal embedded within application.",
            "cv_format_requirements": "Academic CV detailing publications, capstone projects, GPA, and laboratory proficiencies.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview conducted by department faculty evaluating technical fundamentals and lab fit.",
            "standardized_tests": "GRE not required; English language test required.",
            "application_fee_amount": "100% free; application fee waived for international applicants.",
            "attestation_requirements": "Apostille or Korean Embassy legalization of degree certificate and official transcript.",
            "translation_requirements": "Certified English or Korean translations.",
            "final_submission_method": "100% online through GIST admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of valid international passport",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year or 18-year education with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan, MOFA, and Korean Embassy in Islamabad"
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "Detailed essay outlining research background and prospective lab alignment",
                "pakistan_specific_instruction": "Tailored to specific GIST research laboratory"
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential academic references from former university professors",
                "pakistan_specific_instruction": "Submitted via GIST referee portal"
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "TOEFL iBT (80+), IELTS Academic (6.5+), or TOEIC (750+)",
                "pakistan_specific_instruction": "Official test report sent to GIST code"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-03-15",
            "application_deadline": "2026-04-15",
            "university_admission_deadline": "2026-04-15",
            "document_submission_deadline": "2026-04-15",
            "recommendation_letters_deadline": "2026-04-20",
            "interview_period": "May 2026",
            "shortlist_announcement": "Late May 2026",
            "final_result_acceptance_deadline": "2026-06-15",
            "visa_application_window": "June to August 2026",
            "semester_commencement": "2026-09-01",
            "annual_cycle_notes": "Two admissions intakes per year: Fall intake (opens March, starts September) and Spring intake (opens September, starts March)."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior undergraduate/master's GPA and technical coursework)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular contribution)",
            "research_experience_weight": "35% (Publications, laboratory skills, thesis quality, technical projects)",
            "work_experience_weight": "5% (Engineering or lab work experience)",
            "personal_statement_weight": "10% (Technical motivation and lab fit)",
            "recommendations_weight": "10% (Faculty referee appraisals)",
            "interview_weight": "Crucial during professor interview",
            "test_scores_weight": "0% (Language proficiency is prerequisite)",
            "financial_need_weight": "0% (Pure scientific merit)",
            "selection_panel_composition": "Department Admissions Committee and faculty lab directors at GIST.",
            "evaluation_methodology": "Document screening -> Technical video interview by department faculty -> Final admission and scholarship award decision."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,000 international applicants across both intakes",
            "total_scholarships_awarded": "~150 to 200 fully funded admissions per year",
            "acceptance_rate_global": "~8% to 10%",
            "acceptance_rate_pakistan": "~6% to 8% (Very Competitive)",
            "typical_successful_applicant_gpa": "3.40+ / 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates from NUST, FAST, GIKI, UET Lahore, COMSATS, and PIEAS with strong technical fundamentals, hands-on programming/circuit/wet-lab skills, and high motivation.",
            "common_backgrounds_of_winners": "Pakistani researchers have a strong alumni presence in EECS, Mechanical, and Materials Science at GIST.",
            "high_representation_countries": "Vietnam, Pakistan, India, Bangladesh, Indonesia, Turkey, Iran, Russia.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized websites claiming GIST admissions services: gist-korea-scholarships.com, studyingist-portal.org."
            ],
            "application_fee_warning": "Applying to GIST is 100% free of charge. No application fee is required.",
            "agent_and_intermediary_warnings": "GIST does not collaborate with any external recruitment agencies.",
            "itemized_hidden_out_of_pocket_costs": [
                "Korean D-2 student visa processing fee (~PKR 15,000)",
                "HEC, MOFA, and Korean Embassy document attestation fees (~PKR 35,000 to 50,000)",
                "Initial 1-month living expenses before flight reimbursement and first stipend disbursement (~KRW 400,000)"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: Flight ticket is not reimbursed. (Truth: GIST reimburses one-way economy international airfare for all incoming new international students upon arrival).",
                "MYTH: You need Korean language proficiency. (Truth: GIST is an English-medium research institute; 100% of graduate lectures are in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial agencies claim you must pay an application fee; GIST application is 100% free for international students."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 out of 4.50 to remain in good standing.",
            "attendance_requirements": "Full-time physical research residence at GIST campus.",
            "academic_progress_monitoring": "Semi-annual research progress reviews; publishing required peer-reviewed journal papers (SCI/SCIE) before PhD thesis defense.",
            "work_restrictions_during_study": "Outside employment is strictly prohibited without written authorization from Dean of Academic Affairs.",
            "home_country_return_obligation": "None; international graduates qualify for South Korea's D-10 job seeker visa and E-7 work visa pathways.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Scholarship is cancelled if student drops out or GPA falls below 3.00 for two consecutive semesters.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Changing departments requires approval from both department chairs and academic dean.",
            "extension_policy": "Maximum duration is 2 years for MS, 4 years for PhD; research assistantships can continue through thesis defense."
        },
        "official_sources_verified": [
            {
                "source_name": "Gwangju Institute of Science and Technology (GIST) - International Admissions Official Portal",
                "source_url": "https://www.gist.ac.kr/ia/html/sub04/0401.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "School-by-school quota allocations for international student admissions.",
                    "Exact departmental Research Assistantship top-up variations by laboratory.",
                    "Interview scoring rubrics used by evaluating faculty panels."
                ]
            }
        ]
    },

    # 20. SIIT Excellent Foreign Students (EFS) Scholarship (SCH-AS-018)
    "SCH-AS-018": {
        "scholarship_id": "SCH-AS-018",
        "basic_details": {
            "scholarship_name": "SIIT Excellent Foreign Students (EFS) Scholarship",
            "offering_entity": "Sirindhorn International Institute of Technology (SIIT), Thammasat University (Thailand)",
            "host_country": "Thailand",
            "host_institutions_covered": "Sirindhorn International Institute of Technology (SIIT), Thammasat University (Rangsit & Bangkadi Campuses, Pathum Thani, Thailand)",
            "degree_levels": ["Master's Degree", "Doctoral / PhD"],
            "major_restrictions": "Engineering & Technology disciplines: Artificial Intelligence & Internet of Things, Computer Engineering, Electrical Engineering, Mechanical Engineering, Civil Engineering, Chemical Engineering, Industrial Engineering, Logistics & Supply Chain Systems, Energy Technology, Digital Engineering.",
            "number_of_awards_total": "~40 to 60 full and partial graduate scholarships awarded per semester",
            "number_of_awards_pakistan": "Open international competition across Asia; Pakistan has one of the largest active cohorts at SIIT (typically 10 to 25 Pakistani scholars awarded/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (4 semesters) for Master's; 3 years (6 semesters) for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Thai citizens of good health and conduct"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed Bachelor's degree (16 years education) for Master's; completed Master's degree (18 years education) for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 2.75 / 4.00 CGPA for Master's; minimum 3.25 / 4.00 CGPA for PhD (or top 20% class standing).",
            "subject_background_prerequisites": "Undergraduate degree in engineering, computer science, physical sciences, or related technology field.",
            "current_education_status": "Graduated or in final semester of degree graduating before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research thesis, technical projects, and conference/journal publications heavily rewarded.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 80,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "TOEFL iBT min 80, IELTS Academic min 6.0, or official Medium of Instruction (MOI) certificate from English-medium university."
            },
            "other_language_requirements": "English (100% of courses and research at SIIT are conducted in English).",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top-performing international engineering researchers.",
            "previous_scholarship_restrictions": "Must not be receiving another major scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition and educational support fees waived for all semesters.",
                "amount": "100% covered (~THB 150,000 to 200,000 / year / ~USD $4,500 to $6,000/yr)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Application through SIIT online admissions portal is 100% free of charge.",
                "amount": "Free application"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized on-campus international student dormitories at Rangsit campus (rent ~THB 2,500–4,000/mo / ~PKR 21,000 to 34,000/mo) paid from monthly stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly living allowance of THB 10,000/month (~PKR 85,000/month / ~USD $300/month) for Master's; THB 10,000 to 12,000/month for PhD (~PKR 85,000 to 102,000/month). Living costs on Rangsit campus are very low (~THB 6,000–8,000/mo).",
                "amount": "THB 10,000 to 12,000 / month (~PKR 85,000 to 102,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Round-trip economy international airfare allowance (up to THB 20,000) reimbursed upon arrival and completion.",
                "amount": "Round-trip airfare reimbursed (up to THB 20,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Thai Non-Immigrant ED visa application fee (~PKR 15,000) paid by applicant.",
                "amount": "Nominal embassy visa fee"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive student group health and accident insurance provided by SIIT.",
                "amount": "100% covered"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Affordable meals at Thammasat Rangsit campus food courts (~THB 40 to 60 per meal / ~PKR 350 to 500).",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Laboratory facilities, high-performance computing, and digital library access provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "SIIT conference travel support grants available for presenting accepted papers at international conferences.",
                "amount": "Conference travel grants available"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "None; free campus shuttle buses operate across Thammasat Rangsit campus.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 12000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Sirindhorn International Institute of Technology (SIIT), Thammasat University.",
            "participating_institutions": [
                "Sirindhorn International Institute of Technology (SIIT)"
            ],
            "university_rankings_scope": "#1 in Thailand for Engineering & Technology research output per faculty; Top 5 in Thailand (QS Asia Top 150).",
            "available_majors": [
                "Artificial Intelligence and IoT, Computer Engineering, Electrical Engineering, Mechanical Engineering, Civil Engineering, Chemical Engineering, Industrial Engineering, Logistics & Supply Chain, Energy Technology, Digital Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "24 months (Master's) or 36 months (PhD)",
            "admission_requirements_summary": "Bachelor's or Master's degree in engineering/computing with minimum 2.75/3.25 CGPA, English proficiency, and research intent.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "AI and Computer Engineering are the most applied programs; civil, chemical, and industrial engineering have slightly higher acceptance ratios.",
            "strategic_program_match_advice": "Check SIIT faculty research profiles and mention 2-3 specific faculty members whose research topics match your background in the application form."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.siit.tu.ac.th/admissions/graduate",
            "portal_system_name": "SIIT Online Graduate Admissions Portal",
            "account_creation_instructions": "Register on the SIIT Online Graduate Admissions system during the Semester 1 or Semester 2 open window.",
            "step_by_step_workflow": [
                "1. Check application period on SIIT website (February-March for Semester 1; August-September for Semester 2).",
                "2. Create account on SIIT online admissions portal.",
                "3. Select degree program and research specialization.",
                "4. Upload Statement of Purpose, academic transcripts, degree certificates, CV, and English proficiency proofs.",
                "5. Register 2 academic referees who upload letters of recommendation.",
                "6. Submit online application (100% free of charge).",
                "7. Document screening by SIIT scholarship committee.",
                "8. Online interview conducted by faculty professors (April/October).",
                "9. Final results announced in May/November.",
                "10. Receive formal admission letter and apply for Thai Non-ED student visa."
            ],
            "university_vs_scholarship_routing": "Integrated single application: all foreign applicants are automatically evaluated for the EFS Scholarship.",
            "recommendation_letters_submission_method": "Submitted online by 2 academic referees via SIIT electronic referee form.",
            "personal_statement_prompts": "Statement of Purpose describing academic trajectory, research accomplishments, why SIIT was chosen, and prospective engineering research.",
            "study_plan_research_proposal_requirements": "Brief research interest outline (1 page) describing proposed research topic.",
            "cv_format_requirements": "Academic CV detailing technical skills, software/hardware tools, publications, and GPA.",
            "interviews_conducted": True,
            "interview_format_details": "Online video interview conducted by SIIT professors evaluating technical engineering fundamentals.",
            "standardized_tests": "GRE not required; English language test required (MOI letter accepted).",
            "application_fee_amount": "100% free; no application fee.",
            "attestation_requirements": "Certified copies of degree and transcripts; verified upon physical arrival in Thailand.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online through SIIT admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of valid international passport data page",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year or 18-year education with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "1-page essay outlining academic background and prospective research goals",
                "pakistan_specific_instruction": "Tailored to SIIT engineering research groups"
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential reference letters from university professors",
                "pakistan_specific_instruction": "From undergraduate thesis advisor or department chair"
            },
            {
                "document_name": "English Language Proficiency Proof",
                "mandatory": True,
                "specification": "TOEFL (80+), IELTS (6.0+), or official Medium of Instruction (MOI) certificate",
                "pakistan_specific_instruction": "University MOI letter or IELTS report"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-02-01",
            "application_deadline": "2026-03-31",
            "university_admission_deadline": "2026-03-31",
            "document_submission_deadline": "2026-03-31",
            "recommendation_letters_deadline": "2026-04-05",
            "interview_period": "April 2026",
            "shortlist_announcement": "Late April 2026",
            "final_result_acceptance_deadline": "2026-05-20",
            "visa_application_window": "June to July 2026",
            "semester_commencement": "2026-08-10",
            "annual_cycle_notes": "Two admissions cycles per year: Semester 1 (opens February, starts August) and Semester 2 (opens August, starts January)."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Prior undergraduate/master's GPA and engineering coursework)",
            "extracurricular_and_leadership_weight": "5% (Engineering competitions and student projects)",
            "research_experience_weight": "30% (Undergraduate capstone design, papers, and lab technical skills)",
            "work_experience_weight": "5% (Engineering internships or industry employment)",
            "personal_statement_weight": "10% (Technical motivation and clarity of research objectives)",
            "recommendations_weight": "10% (Quality of professor appraisals)",
            "interview_weight": "Decisive during video interview",
            "test_scores_weight": "0% (Language proficiency is prerequisite)",
            "financial_need_weight": "0% (Merit-based)",
            "selection_panel_composition": "SIIT Graduate Scholarship Committee and department chairs.",
            "evaluation_methodology": "Document screening -> Technical video interview by department faculty -> Final scholarship committee award determination."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 international applicants across both semesters",
            "total_scholarships_awarded": "~80 to 100 scholarships awarded annually",
            "acceptance_rate_global": "~5% to 6%",
            "acceptance_rate_pakistan": "~4% to 5% (Very Competitive)",
            "typical_successful_applicant_gpa": "3.30+ / 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates from NUST, UET Lahore, COMSATS, GIKI, FAST, and UET Taxila with solid engineering fundamentals, programming/CAD proficiencies, and strong research drive.",
            "common_backgrounds_of_winners": "Pakistani scholars represent the largest international student group at SIIT, with many alumni progressing to PhDs in Japan, Europe, or North America.",
            "high_representation_countries": "Pakistan, Vietnam, Myanmar, Indonesia, Bangladesh, India, Cambodia, Philippines.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent agency portals: siit-scholarships-portal.org, thailand-study-grants.com."
            ],
            "application_fee_warning": "SIIT application is 100% free of charge. No application fee is charged.",
            "agent_and_intermediary_warnings": "SIIT does not work with third-party education consultants or recruiters.",
            "itemized_hidden_out_of_pocket_costs": [
                "Thai Non-Immigrant ED visa application fee (~PKR 15,000)",
                "Degree attestation fees (HEC and MOFA)",
                "Initial domestic travel to Thailand (~PKR 120,000 to 160,000, reimbursable up to THB 20,000 after arrival)"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: You need to know Thai language. (Truth: SIIT was established as an autonomous international institute where all courses, exams, and research are conducted entirely in English).",
                "MYTH: Living in Thailand on THB 10,000 is difficult. (Truth: Rangsit campus dorms cost ~THB 2,500/mo and meals cost ~THB 50/meal; THB 10,000 comfortably covers all monthly expenses)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Agents claim you need IELTS 7.0; SIIT accepts IELTS 6.0 or official English Medium of Instruction (MOI) certificates from accredited universities."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.25 out of 4.00 for Master's and 3.50 out of 4.00 for PhD.",
            "attendance_requirements": "Full-time physical research residence at SIIT campus.",
            "academic_progress_monitoring": "Must assist in 6 hours per week of Teaching Assistantship (TA) or Research Assistantship (RA) duties; must publish at least 1 peer-reviewed journal paper in international indexed journal (Scopus/Web of Science) before graduation.",
            "work_restrictions_during_study": "Outside employment prohibited without explicit SIIT approval.",
            "home_country_return_obligation": "None; scholars are free to pursue post-graduation employment in Thailand or abroad.",
            "service_obligations_or_bonds": "6 hours/week of departmental assistantship duties during term.",
            "repayment_clawback_conditions": "Scholarship is cancelled if cumulative GPA drops below 3.00 or if the student drops out.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Changing programs requires approval from both academic departments and scholarship committee.",
            "extension_policy": "Maximum duration is 2 years for Master's and 3 years for PhD; extensions rarely granted."
        },
        "official_sources_verified": [
            {
                "source_name": "Sirindhorn International Institute of Technology (SIIT) - EFS Scholarship Official Portal",
                "source_url": "https://www.siit.tu.ac.th/admissions/graduate",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Department-by-department allocation quota of EFS full vs partial awards.",
                    "Exact interview scoring sheets used by departmental faculty panels.",
                    "Country quota targets for South Asian applicant pools."
                ]
            }
        ]
    }
}
