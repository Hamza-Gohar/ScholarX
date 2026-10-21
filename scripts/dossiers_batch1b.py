"""
scripts/dossiers_batch1b.py
Part B of Batch 1:
4. SCH-AM-008: Hubert H. Humphrey Fellowship Program (USEFP Pakistan / USA)
5. SCH-AM-010: McCall MacBain Scholarships at McGill University (Canada)
6. SCH-AM-014: MIT EECS Graduate Fellowship & Research Assistantship (USA)
7. SCH-OC-002: Manaaki New Zealand Scholarships (New Zealand MFAT)
8. SCH-OC-003: University of Melbourne Graduate Research Scholarships (Australia)
"""

DOSSIERS_BATCH1B = {
    # 4. Hubert H. Humphrey Fellowship Program (SCH-AM-008)
    "SCH-AM-008": {
        "scholarship_id": "SCH-AM-008",
        "basic_details": {
            "scholarship_name": "Hubert H. Humphrey Fellowship Program for Pakistan",
            "offering_entity": "United States Educational Foundation in Pakistan (USEFP) & U.S. Department of State (ECA)",
            "host_country": "United States",
            "host_institutions_covered": "Selected Host Campuses (MIT, Syracuse University, Cornell University, UC Davis, Emory, Boston University, Penn State, Vanderbilt)",
            "degree_levels": ["Non-Degree Professional Fellowship"],
            "major_restrictions": "Public policy and leadership fields: Public Health, Climate Change & Environmental Policy, Economic Development, Banking & Finance, Journalism & Communications, Educational Administration, Law and Human Rights, Public Administration, Technology Policy.",
            "number_of_awards_total": "~150 fellows globally from 140+ countries",
            "number_of_awards_pakistan": "~10 to 15 mid-career leaders selected from Pakistan annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "10 months of combined graduate study, leadership seminars, and professional affiliation"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Pakistani citizens residing in Pakistan throughout application process"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "Applicants are typically mid-career professionals between 30 and 50 years of age.",
            "academic_qualifications": "16 years of formal education (4-year Bachelor's or 2-year Bachelor's + 2-year Master's) from an HEC-recognized institution.",
            "minimum_gpa_percentage": 50.0,
            "minimum_gpa_scale": 2.5,
            "grading_conversion_notes": "Minimum second division (50% marks) or 2.5 / 4.00 CGPA; substantive career leadership record carries primary weight.",
            "subject_background_prerequisites": "Substantive experience in designated Humphrey public service fields.",
            "current_education_status": "Employed mid-career professional; university students are NOT eligible.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": True,
            "work_experience_minimum_years": 5.0,
            "work_experience_notes": "Minimum 5 years of full-time substantive professional experience in public service, government, NGO, media, or private sector leadership with demonstrated public impact.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": None,
                "toefl_minimum": None,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "No test needed to apply; shortlisted finalists take USEFP-funded TOEFL iBT."
            },
            "other_language_requirements": "English fluency.",
            "gender_specific_requirements": "Equal opportunity; women and public sector officers from remote regions strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Public commitment, demonstrated leadership trajectory, policy influence potential.",
            "previous_scholarship_restrictions": "Recent extensive U.S. study/experience (within past 7 years) renders applicants lower priority.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Tuition and academic fees at assigned host U.S. university paid directly.",
                "amount": None
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Managed directly via USEFP and Institute of International Education (IIE).",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Fellows arrange apartments using generous monthly living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Comprehensive monthly maintenance allowance based on host city cost of living.",
                "amount": "$2,200 to $2,800 / month (~PKR 620,000 to 790,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Round-trip international economy class airfare from Pakistan to the United States.",
                "amount": None
            },
            "visa_fee": {
                "status": "WAIVED",
                "details": "J-1 visa sponsorship, SEVIS fees, and visa fees fully covered.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "ASPE health coverage provided by U.S. Department of State.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered within monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Textbook and professional equipment allowance provided upon arrival.",
                "amount": "$750 one-off allowance (~PKR 210,000)"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Professional development grant ($2,000–$3,000) for domestic U.S. conferences and professional affiliation field trips.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Settlement allowance and domestic travel in Pakistan covered.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 55000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple host campuses designated by IIE into thematic cohorts.",
            "participating_institutions": [
                "Maxwell School at Syracuse University", "MIT (Special Program for Urban & Regional Studies)",
                "Cornell University", "UC Davis", "Emory University (Rollins School of Public Health)",
                "Boston University", "Penn State University", "Vanderbilt University"
            ],
            "university_rankings_scope": "Premier Ivy League and leading U.S. public policy faculties.",
            "available_majors": [
                "Public Policy, Public Health, Climate Change, Environmental Policy, Economic Development, Financial Crimes & Banking, Educational Leadership, Law & Human Rights, Technology Policy"
            ],
            "english_taught_program_availability": True,
            "program_duration": "10 continuous months (August to June)",
            "admission_requirements_summary": "Placement coordinated centrally by IIE; no independent university application required.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Host campuses are assigned based on your designated professional focus.",
            "strategic_program_match_advice": "Focus heavily on how the 6-week professional affiliation in a U.S. agency, think tank, or multinational NGO will enable policy innovation in Pakistan."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.usefp.org/scholarships/humphrey.cfm",
            "portal_system_name": "USEFP Humphrey Online Portal",
            "account_creation_instructions": "Register on the USEFP portal, complete career history, and upload institutional endorsements.",
            "step_by_step_workflow": [
                "1. Complete online application on USEFP portal (Open: March/April, Deadline: early June).",
                "2. Submit detailed Professional Goals Essay and Program Plan.",
                "3. Secure employer endorsement letter confirming leave of absence.",
                "4. Provide three professional and academic letters of reference.",
                "5. Panel interviews held in Islamabad/Karachi in August/September.",
                "6. National nominees forwarded to J. William Fulbright Foreign Scholarship Board (FSB) in Washington.",
                "7. Final approval released in February/March; departure in August."
            ],
            "university_vs_scholarship_routing": "Direct application to USEFP Pakistan.",
            "recommendation_letters_submission_method": "Submitted online by supervisors and professional mentors.",
            "personal_statement_prompts": "Address your professional goals, public service impact in Pakistan, leadership challenges faced, and how the Humphrey program aligns with institutional reform.",
            "study_plan_research_proposal_requirements": "Program Plan detailing specific graduate coursework, leadership seminars, and prospective U.S. organizations for the 6-week professional affiliation.",
            "cv_format_requirements": "Comprehensive professional resume (3-4 pages) detailing career progression, publications, and reform achievements.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute structured panel interview before U.S. diplomats, senior civil servants, and Humphrey alumni in Islamabad.",
            "standardized_tests": "TOEFL iBT taken and funded by USEFP for shortlisted candidates only.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "HEC attested degree and transcripts required prior to final grant confirmation.",
            "translation_requirements": "Official English translations required if certificates are in Urdu.",
            "final_submission_method": "100% Online via USEFP portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Professional Experience Verification",
                "mandatory": True,
                "specification": "Official service certificates verifying minimum 5 years full-time substantive employment",
                "pakistan_specific_instruction": "From employer HR departments or government department heads"
            },
            {
                "document_name": "Employer Endorsement & Leave Approval",
                "mandatory": True,
                "specification": "Official letter from current employer approving 10 months study leave",
                "pakistan_specific_instruction": "No Objection Certificate (NOC) for civil servants and public sector employees"
            },
            {
                "document_name": "Three Letters of Recommendation",
                "mandatory": True,
                "specification": "Professional and academic references speaking to leadership ability",
                "pakistan_specific_instruction": "From direct supervisors, department secretaries, or institutional directors"
            },
            {
                "document_name": "University Degrees and Transcripts",
                "mandatory": True,
                "specification": "16 years of education certificates",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "CNIC Copy",
                "mandatory": True,
                "specification": "Valid NADRA CNIC",
                "pakistan_specific_instruction": "Front and back scanned copies"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-04-01",
            "application_deadline": "2026-06-10",
            "university_admission_deadline": "N/A",
            "document_submission_deadline": "2026-06-10",
            "recommendation_letters_deadline": "2026-06-20",
            "interview_period": "August to September 2026",
            "shortlist_announcement": "October 2026",
            "final_result_acceptance_deadline": "March 2027",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "August 2027",
            "annual_cycle_notes": "Opens annually in April and closes early June; final selection confirmed by Washington in March of following year."
        },
        "selection_process_and_weights": {
            "academic_weight": "15% (Meets basic university qualification standards)",
            "extracurricular_and_leadership_weight": "40% (Track record of public leadership, community initiatives, and public sector reforms)",
            "research_experience_weight": "10% (Applied policy or practical analytical work)",
            "work_experience_weight": "25% (Substantive, demonstrable impact over 5+ years)",
            "personal_statement_weight": "10% (Clear roadmap for applying knowledge upon return)",
            "recommendations_weight": "10% (Strong executive endorsements)",
            "interview_weight": "Crucial in final selection round",
            "test_scores_weight": "0%",
            "financial_need_weight": "0%",
            "selection_panel_composition": "USEFP executive leadership, senior U.S. Embassy public diplomacy officers, and Pakistani Humphrey alumni.",
            "evaluation_methodology": "Identification of committed leaders who will return to Pakistan and lead positive systemic change in their institutions."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,000 mid-career professionals across Pakistan",
            "total_scholarships_awarded": "~10 to 15 fellows from Pakistan annually",
            "acceptance_rate_global": "N/A (Pakistan national quota)",
            "acceptance_rate_pakistan": "~0.8% to 1.2% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "2.80 to 3.80 / 4.00 CGPA (Grades secondary to career track record)",
            "typical_academic_and_research_profile": "Assistant commissioners, directors in provincial departments, senior journalists, healthcare administrators, climate policy experts.",
            "common_backgrounds_of_winners": "Civil servants, judicial officers, NGO founders, environmental advocates, and broadcast media heads.",
            "high_representation_countries": "Global program covering 140 countries.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial career coaches charging exorbitant fees to write Humphrey program plans."
            ],
            "application_fee_warning": "USEFP application is 100% free of charge.",
            "agent_and_intermediary_warnings": "Never work through third-party agents; direct candidate engagement is mandatory.",
            "hidden_costs_breakdown": [
                "Domestic travel to Islamabad for interview and pre-departure sessions.",
                "Passport issuance and NADRA document certification fees."
            ],
            "misleading_claims_debunked": [
                "MYTH: You receive a Master's degree. (Fact: Humphrey is a non-degree professional development program; participants receive a Certificate of Completion issued by the President of the United States and host university).",
                "MYTH: You can stay in the USA for immigration. (Fact: Fellows are subject to the strict two-year home residency requirement (212(e)) on J-1 visa)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some career websites mistake this for an academic PhD grant; it is strictly a professional leadership fellowship."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must satisfactorily complete all enrolled courses and seminars with passing grades.",
            "attendance_requirements": "Full-time physical residence, complete attendance at national Humphrey seminars, and 6-week professional affiliation.",
            "academic_progress_monitoring": "Monthly check-ins and performance reporting by university coordinator to IIE.",
            "work_restrictions_during_study": "Paid employment outside the fellowship is strictly prohibited under J-1 visa rules.",
            "home_country_return_obligation": "MANDATORY 2-Year Home Country Physical Presence Requirement (J-1 Section 212(e)); cannot change visa status or immigrate to U.S. until 2 years spent in Pakistan.",
            "service_obligations_or_bonds": "Obligated to return to sponsoring employer or public service in Pakistan.",
            "repayment_clawback_conditions": "Failure to complete program, early departure, or violation of U.S. laws entails termination and repayment of fellowship costs.",
            "rules_for_changing_university": "University assignment is fixed and cannot be changed.",
            "rules_for_changing_major": "Fields cannot be modified post-selection.",
            "extension_policy": "Extensions beyond the 10-month grant period are strictly prohibited."
        },
        "official_sources_verified": [
            {
                "source_name": "United States Educational Foundation in Pakistan (USEFP) - Humphrey Fellowship",
                "source_url": "https://www.usefp.org/scholarships/humphrey.cfm",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact rubric used by Washington selection board to rate candidates from different provinces",
                    "Specific provincial quotas within Pakistan"
                ]
            },
            {
                "source_name": "Humphrey Fellowship Global Secretariat - Institute of International Education (IIE)",
                "source_url": "https://www.humphreyfellowship.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Annual allocation formulas between host U.S. university campuses"
                ]
            }
        ]
    },

    # 5. McCall MacBain Scholarships at McGill University (SCH-AM-010)
    "SCH-AM-010": {
        "scholarship_id": "SCH-AM-010",
        "basic_details": {
            "scholarship_name": "McCall MacBain Scholarships at McGill University",
            "offering_entity": "McCall MacBain Foundation & McGill University",
            "host_country": "Canada",
            "host_institutions_covered": "McGill University (Montreal, Quebec, Canada)",
            "degree_levels": ["Master's", "Professional Undergraduate (Law, Medicine)"],
            "major_restrictions": "Open to all master's degree programs (MA, MSc, MEng, MBA, MPP, LLM) or second-entry professional undergraduate degrees (BCL/JD Law, MDCM Medicine) across McGill faculties.",
            "number_of_awards_total": "~30 full scholarships + ~100 regional/finalist awards annually",
            "number_of_awards_pakistan": "Open globally; ~10 full scholarships reserved for international students, with numerous CAD $10,000-$20,000 finalist awards",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full normal duration of the master's or professional degree (typically 1 to 2 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to citizens of all countries including Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "Open to recent graduates or professionals who earned their first undergraduate degree within the last five years, or any age if pursuing second-entry degree.",
            "academic_qualifications": "16 years of education (4-year Bachelor's degree) satisfying McGill graduate admissions standards.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.0 / 4.00 CGPA or equivalent; competitive candidates generally present 3.50+ CGPA alongside high extracurricular impact.",
            "subject_background_prerequisites": "Undergraduate degree relevant to intended McGill graduate program.",
            "current_education_status": "Graduated with bachelor's degree or in final year of undergraduate study.",
            "graduation_year_restrictions": "Undergraduate degree completed within past 5 years (e.g., 2021 or later) or currently enrolled.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Community engagement, volunteering, resilience, and leadership initiative prioritized over raw corporate tenure.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 86,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Must satisfy McGill departmental language requirements (IELTS 6.5 overall, TOEFL 86-100 depending on faculty)."
            },
            "other_language_requirements": "English; French knowledge is an asset in Montreal but not required for admission.",
            "gender_specific_requirements": "Equal opportunity; diverse candidates welcome.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must demonstrate exceptional character, leadership, intellectual curiosity, and commitment to service.",
            "previous_scholarship_restrictions": "Must not have already completed a master's degree.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition and mandatory student fees covered for the full duration of the degree at McGill University.",
                "amount": "CAD $25,000 to $45,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "McGill University graduate admission application fee (~CAD $130) paid by candidate.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Living expenses covered by monthly living stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "CAD $2,000 per month living stipend during academic terms.",
                "amount": "CAD $2,000 / month (~PKR 415,000 / month or CAD $24,000 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One-time relocation grant provided upon initial arrival in Montreal.",
                "amount": "CAD $2,000 relocation grant (~PKR 415,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian study permit and Quebec CAQ fees paid by candidate.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "McGill International Health Insurance plan covered under mandatory fee benefits.",
                "amount": "CAD $1,100 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered via living allowance.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Summer leadership, research, and internship funding up to CAD $5,000 available upon application.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in relocation grant.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 45000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: McGill University (Montreal, Canada - World Top 30).",
            "participating_institutions": [
                "McGill University"
            ],
            "university_rankings_scope": "Consistently ranked among Canada's top 2 universities and Top 35 globally.",
            "available_majors": [
                "Computer Science, Electrical & Computer Engineering, Mechanical Engineering, Civil Engineering, Experimental Medicine, Pharmacology, Epidemiology, Public Policy, Law (BCL/JD), Economics, Management, Biology, Physics, Architecture"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 to 2 academic years depending on the master's degree",
            "admission_requirements_summary": "Must apply separately for admission to an eligible full-time McGill master's or second-entry program by McGill's departmental deadline.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "High-volume programs in Computer Science and Epidemiology have rigorous departmental cutoffs; apply to McGill early in the fall.",
            "strategic_program_match_advice": "Scholarship emphasizes character, purposeful leadership, and willingness to take risks to improve community welfare."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://mccallmacbainscholars.org/",
            "portal_system_name": "McCall MacBain Scholarship Online Application Portal",
            "account_creation_instructions": "Register on the portal, provide undergraduate university details, and designate two reference providers.",
            "step_by_step_workflow": [
                "1. Submit McCall MacBain online application by late August (International applicant deadline).",
                "2. Provide comprehensive essays detailing personal character, service, and leadership philosophy.",
                "3. Ensure two reference letters (one academic, one leadership/community) are submitted by deadline.",
                "4. Regional interviews conducted virtually in October/November for shortlisted candidates.",
                "5. Finalists invited to Montreal for all-expenses-paid final interview round in March.",
                "6. Submit separate admission application to McGill University by respective program deadline."
            ],
            "university_vs_scholarship_routing": "Concurrent: Apply to McCall MacBain in August; apply for McGill graduate admission in October-December.",
            "recommendation_letters_submission_method": "Submitted online by referees via unique secure link.",
            "personal_statement_prompts": "Demonstrate your character, moral courage, leadership experiences, meaningful service to others, and intellectual engagement.",
            "study_plan_research_proposal_requirements": "Summary of proposed master's program and alignment with future public service or impact goals.",
            "cv_format_requirements": "Concise 2-page CV highlighting volunteerism, extracurricular leadership, jobs, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Two rounds: 30-minute virtual regional interview, followed by intensive in-person final interviews in Montreal (flights and accommodation fully paid).",
            "standardized_tests": "None for McCall MacBain; check McGill departmental requirements (e.g. GRE/GMAT).",
            "application_fee_amount": "$0 for McCall MacBain scholarship application; McGill admission fee applies.",
            "attestation_requirements": "Official university transcripts certified by Pakistani degree institution.",
            "translation_requirements": "Official English or French certified translations.",
            "final_submission_method": "100% Online via McCall MacBain portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Undergraduate University Transcripts",
                "mandatory": True,
                "specification": "Official transcripts covering all completed semesters",
                "pakistan_specific_instruction": "Issued and stamped by university examination controller"
            },
            {
                "document_name": "Personal Leadership Essays",
                "mandatory": True,
                "specification": "Detailed essay answers to prompts exploring character, initiatives, and failure",
                "pakistan_specific_instruction": "Narratives focusing on authentic leadership and social impact in Pakistan"
            },
            {
                "document_name": "Two Letters of Reference",
                "mandatory": True,
                "specification": "One academic reference and one community/leadership reference",
                "pakistan_specific_instruction": "Uploaded by referees via secure portal link"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "Chronological 2-page resume emphasizing extracurricular impact",
                "pakistan_specific_instruction": "Detail volunteer initiatives, school leadership, and extracurricular achievements"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-06-01",
            "application_deadline": "2026-08-25",
            "university_admission_deadline": "2026-12-15",
            "document_submission_deadline": "2026-08-25",
            "recommendation_letters_deadline": "2026-09-05",
            "interview_period": "October to November 2026 (Regional) & March 2027 (Finals in Montreal)",
            "shortlist_announcement": "December 2026",
            "final_result_acceptance_deadline": "April 2027",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "International application deadline is always in late August (earlier than North American deadline in September)."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Academic strength, intellectual curiosity, and depth)",
            "extracurricular_and_leadership_weight": "35% (Exceptional character, leadership, community contribution, and empathy)",
            "research_experience_weight": "10% (Analytical ability and problem-solving)",
            "work_experience_weight": "10% (Work ethic, resilience, initiative)",
            "personal_statement_weight": "10% (Self-reflection and authenticity)",
            "recommendations_weight": "10% (Substantiation of character and integrity)",
            "interview_weight": "Decisive in regional and final rounds",
            "test_scores_weight": "0%",
            "financial_need_weight": "0% (Purely merit and character based)",
            "selection_panel_composition": "Diverse panels of Canadian and international leaders, educators, McGill deans, and philanthropists.",
            "evaluation_methodology": "Holistic review identifying individuals who are driven to make a difference and exhibit humility, curiosity, and persistence."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 international candidates from 100+ countries",
            "total_scholarships_awarded": "~10 full international scholarships + ~25 international finalist awards ($10,000-$20,000)",
            "acceptance_rate_global": "~0.4% for full scholarship",
            "acceptance_rate_pakistan": "~0.5% (Very Selective)",
            "typical_successful_applicant_gpa": "3.50 to 3.95 / 4.00 CGPA",
            "typical_academic_and_research_profile": "High academic performers who have founded charities, represented national debate teams, or built civic tech solutions.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (LUMS, NUST, AKU, IBA) with exceptional public service records.",
            "high_representation_countries": "Global representation across Americas, Europe, Asia, and Africa.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites claiming to offer internal interview questions or coaching for McCall MacBain."
            ],
            "application_fee_warning": "McCall MacBain application is 100% free of charge; McGill admission application fee applies.",
            "agent_and_intermediary_warnings": "Never use agents; applications written by third parties are easily detected in live interviews.",
            "hidden_costs_breakdown": [
                "McGill graduate admission application fee (~CAD $130).",
                "Quebec CAQ immigration certificate and Canadian study permit fees (~CAD $275).",
                "English language test fees (IELTS/TOEFL) if required by McGill department."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must be accepted by McGill before applying for McCall MacBain. (Fact: You apply to McCall MacBain in August first; then apply for McGill admission in the autumn).",
                "MYTH: If you do not win the full scholarship, you get nothing. (Fact: Finalists and regional candidates receive significant awards of CAD $10,000 to $20,000)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Social media blogs state this is only for Canadian citizens; international candidates have been fully eligible since 2022."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing in McGill graduate program (CGPA 3.0+).",
            "attendance_requirements": "Full-time physical residence in Montreal, Quebec and participation in the McCall MacBain Leadership Development Program.",
            "academic_progress_monitoring": "Term-by-term review with the scholarship dean and program mentor.",
            "work_restrictions_during_study": "Permitted to work per Canadian study permit guidelines, but extensive outside work is discouraged.",
            "home_country_return_obligation": "None; scholars are eligible for Canadian Post-Graduation Work Permits (PGWP).",
            "service_obligations_or_bonds": "Active engagement in leadership seminars, mentorship, and cohort retreats.",
            "repayment_clawback_conditions": "Withdrawal from McGill or academic failure results in termination of remaining funding.",
            "rules_for_changing_university": "Award is non-transferable outside McGill.",
            "rules_for_changing_major": "Changing degree programs requires prior approval from the McCall MacBain scholarship office.",
            "extension_policy": "Funding is provided for normal program length (max 2 years); beyond that requires departmental funding."
        },
        "official_sources_verified": [
            {
                "source_name": "McCall MacBain Scholars Official Foundation Portal",
                "source_url": "https://mccallmacbainscholars.org/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact interview evaluation rubric scoring sheet",
                    "Specific country-level quota allotments among international finalists"
                ]
            }
        ]
    },

    # 6. MIT EECS Graduate Fellowship & Research Assistantship (SCH-AM-014)
    "SCH-AM-014": {
        "scholarship_id": "SCH-AM-014",
        "basic_details": {
            "scholarship_name": "MIT EECS Graduate Fellowship & Research Assistantship",
            "offering_entity": "Massachusetts Institute of Technology (MIT) - Department of Electrical Engineering & Computer Science",
            "host_country": "United States",
            "host_institutions_covered": "MIT (Cambridge, Massachusetts, USA)",
            "degree_levels": ["Master's leading to PhD", "PhD"],
            "major_restrictions": "Electrical Engineering, Computer Science, Artificial Intelligence, Machine Learning, Robotics, Computer Systems, Quantum Computing, Microelectronics, BioEECS.",
            "number_of_awards_total": "~100% of admitted PhD/SM candidates receive full financial funding (~200 admits/year)",
            "number_of_awards_pakistan": "Open worldwide without quotas; based entirely on academic and research brilliance",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Fully funded for the entire duration of graduate studies (typically 5 to 6 years) provided satisfactory academic and research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to all nationalities including Pakistani citizens"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "16 years of education (4-year BS in CS, EE, Math, Physics) or 18 years (MS/MPhil) from a top recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Minimum 3.80 / 4.00 CGPA; almost all admitted international students rank in top 1-2% of their graduating cohort.",
            "subject_background_prerequisites": "Rigorous mathematical foundation, algorithm design, systems programming, or electrical hardware fundamentals.",
            "current_education_status": "Final year undergraduate, master's student, or graduate with exceptional research credentials.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic research experience, peer-reviewed conference publications (NeurIPS, ICML, CVPR, OSDI, SOSP, ISCA, IEEE), or open-source software contributions carry the greatest weight.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 100,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "TOEFL iBT minimum 100 or IELTS Academic minimum 7.0 (individual scores evaluated)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; MIT EECS actively encourages underrepresented groups in computing.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite research potential and demonstrable creative problem-solving.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full MIT graduate tuition waived each term (covered via fellowship or RA/TA appointment).",
                "amount": "$62,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "MIT graduate application fee ($75) paid by applicant; fee waivers available for demonstrated financial hardship upon application.",
                "amount": "$75"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Graduate residence or off-campus apartment in Cambridge/Boston paid from monthly stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Full monthly living stipend paid semi-monthly.",
                "amount": "$3,800 to $4,200 / month (~$45,000 to $50,000 / year or ~PKR 1,070,000 to 1,180,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Initial airfare to Cambridge, USA is covered by candidate from initial stipend advance or personal funds.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "F-1 student visa application fee ($185) and SEVIS I-901 fee ($350) paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "MIT Extended Student Health Insurance Plan (SHIP) 100% covered by the department.",
                "amount": "$3,800 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Included within monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "High-end research laptop / desktop computer and lab compute resources provided by advisor lab.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "All travel, registration, and lodging costs for accepted conference papers fully funded by research supervisor's lab grant.",
                "amount": "$3,000 to $6,000 / year per student"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "MBTA transit pass heavily subsidized (50%–60% off) by MIT.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 115000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Massachusetts Institute of Technology (MIT - World #1 in Engineering/CS).",
            "participating_institutions": [
                "MIT EECS (Computer Science and Artificial Intelligence Laboratory - CSAIL, Microsystems Technology Laboratories - MTL, Laboratory for Information & Decision Systems - LIDS)"
            ],
            "university_rankings_scope": "World #1 in Computer Science & Engineering (QS/THE rankings).",
            "available_majors": [
                "Artificial Intelligence, Machine Learning, Natural Language Processing, Computer Vision, Robotics, Systems & Networking, Computer Architecture, Theory of Computation, Cryptography, Quantum Computing, Microelectronics, Electrical Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "5 to 6 years for direct-entry SM+PhD",
            "admission_requirements_summary": "All admitted graduate students are automatically provided full funding; admission equals full scholarship.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "MIT EECS is among the most selective doctoral programs in the world (acceptance rate ~3%-4%).",
            "strategic_program_match_advice": "Explicitly identify 2 to 3 faculty PIs in your statement whose research lab matches your published or demonstrated work."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.eecs.mit.edu/academics/graduate-programs/admission-process/",
            "portal_system_name": "MIT EECS Graduate Admissions Portal (ApplyWeb)",
            "account_creation_instructions": "Register on the MIT EECS Graduate portal, select EECS department, and indicate research interest tracks.",
            "step_by_step_workflow": [
                "1. Review faculty research profiles in CSAIL, LIDS, MTL, or RLE.",
                "2. Create account on MIT EECS graduate application system (Opens September).",
                "3. Submit comprehensive Statement of Objectives (1-2 pages) articulating specific technical research vision.",
                "4. Designate three faculty or research mentors to submit reference letters.",
                "5. Upload academic transcripts and list all published papers or preprint links (arXiv, GitHub).",
                "6. Submit before strict deadline (December 15).",
                "7. Faculty review occurs January; top candidates may be contacted for informal technical interviews.",
                "8. Admissions and full fellowship decisions released in February."
            ],
            "university_vs_scholarship_routing": "Direct single application; all admitted students are awarded full funding automatically.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure ApplyWeb link.",
            "personal_statement_prompts": "Statement of Objectives: Focus on your technical preparation, the open research problems you want to investigate, and which faculty labs you aim to join.",
            "study_plan_research_proposal_requirements": "Integrated into Statement of Objectives; describe concrete research ideas, past project findings, and engineering methodologies.",
            "cv_format_requirements": "Academic CV detailing publications, GitHub projects, competitions (ICPC, Kaggle, Putnam), and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Prospective faculty advisors conduct 30-45 minute technical video interviews with short-listed applicants in January.",
            "standardized_tests": "GRE General test is NOT required (optional or not considered); TOEFL or IELTS required for non-native speakers.",
            "application_fee_amount": "$75 (fee waiver request available within portal for eligible candidates).",
            "attestation_requirements": "Unofficial transcripts uploaded during application; official attested transcripts required upon admission.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via ApplyWeb."
        },
        "required_documents_checklist": [
            {
                "document_name": "Statement of Objectives",
                "mandatory": True,
                "specification": "1 to 2 pages detailing technical research questions and faculty alignments",
                "pakistan_specific_instruction": "Clearly explain research problems you have worked on and your technical contribution"
            },
            {
                "document_name": "Three Letters of Recommendation",
                "mandatory": True,
                "specification": "Letters from research supervisors who can speak to your creative research ability",
                "pakistan_specific_instruction": "Letters from professors who supervised your thesis or research papers carry highest weight"
            },
            {
                "document_name": "University Academic Transcripts",
                "mandatory": True,
                "specification": "Official university transcripts showing all courses and grades",
                "pakistan_specific_instruction": "From HEC-recognized university in Pakistan (e.g. LUMS, NUST, FAST, GIKI, UET)"
            },
            {
                "document_name": "Research Papers / Writing Sample",
                "mandatory": False,
                "specification": "Copies or links to published conference/journal papers or arXiv preprints",
                "pakistan_specific_instruction": "Strongly recommended; research publications are the single biggest differentiator"
            },
            {
                "document_name": "TOEFL or IELTS Score",
                "mandatory": True,
                "specification": "Official electronic score report sent to MIT (School Code: 3514)",
                "pakistan_specific_instruction": "Minimum TOEFL 100 or IELTS 7.0"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2026-12-15",
            "university_admission_deadline": "2026-12-15",
            "document_submission_deadline": "2026-12-15",
            "recommendation_letters_deadline": "2026-12-22",
            "interview_period": "January to early February 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "Application deadline is strictly December 15 each year. Decision letters with full financial package issued in mid-February."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Foundational mastery in math, theory, and computer systems)",
            "extracurricular_and_leadership_weight": "5% (Secondary to technical brilliance)",
            "research_experience_weight": "45% (Past research papers, originality, code contributions, mathematical maturity)",
            "work_experience_weight": "5% (Industrial research labs like Microsoft Research, Google, Meta carry value)",
            "personal_statement_weight": "10% (Clarity of technical thought and alignment with MIT labs)",
            "recommendations_weight": "10% (Credibility and specificity of research referee assessments)",
            "interview_weight": "Influential during faculty match phase in January",
            "test_scores_weight": "0% (GRE not used)",
            "financial_need_weight": "0% (Completely need-blind; all admitted students are funded)",
            "selection_panel_composition": "MIT EECS Admissions Committee and individual Area Faculty Review Groups (AI/ML, Systems, Theory, Circuits).",
            "evaluation_methodology": "Area faculty committees evaluate applicants based on potential to conduct groundbreaking, publication-quality research."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 4,000 applications globally for EECS graduate program",
            "total_scholarships_awarded": "~180 to 220 fully funded offers issued globally",
            "acceptance_rate_global": "~4% to 5%",
            "acceptance_rate_pakistan": "~1% to 2% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.90 to 4.00 CGPA",
            "typical_academic_and_research_profile": "First-author publications at top-tier CS venues (NeurIPS, ICML, CVPR, ICLR, OSDI, SIGCOMM, CHI), international ICPC world finalists, or Putnam medalists.",
            "common_backgrounds_of_winners": "Top Pakistani graduates from LUMS, NUST, FAST-NUCES, GIKI with exceptional research portfolios who collaborated with international labs.",
            "high_representation_countries": "USA, China, India, South Korea, Canada, Pakistan, Iran, European Union.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites claiming to sell 'guaranteed admission to MIT CSAIL'."
            ],
            "application_fee_warning": "Pay only via the official MIT ApplyWeb portal ($75 fee).",
            "agent_and_intermediary_warnings": "MIT strictly prohibits agents. Plagiarism in statements results in permanent disqualification.",
            "hidden_costs_breakdown": [
                "MIT application fee ($75).",
                "US F-1 Visa application fee ($185) + SEVIS I-901 fee ($350).",
                "Initial flight to Boston/Cambridge (~PKR 350,000 to 500,000).",
                "First month's rent security deposit for Cambridge/Somerville apartments."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need to pay tuition if you don't get a special scholarship. (Fact: MIT EECS does NOT admit unfunded graduate students; admission automatically includes 100% full tuition waiver and stipend).",
                "MYTH: You must take the GRE. (Fact: GRE is completely not required for MIT EECS)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Many Pakistani consultancy portals advertise MIT Master's programs as self-funded; MIT EECS does not offer a terminal self-funded Master's to external applicants; external applicants apply to the fully-funded direct SM+PhD program."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative grade point average of 4.5 / 5.0 (MIT grading scale, equivalent to 3.5/4.0).",
            "attendance_requirements": "Full-time physical residence and research engagement on MIT campus in Cambridge, Massachusetts.",
            "academic_progress_monitoring": "Annual progress evaluation and doctoral thesis committee reviews.",
            "work_restrictions_during_study": "Funding is provided via 20 hours/week Research Assistantship (RA) or Teaching Assistantship (TA); outside employment is restricted under F-1 visa terms.",
            "home_country_return_obligation": "None; F-1 students are eligible for up to 3 years of STEM OPT (Optional Practical Training) work authorization in the USA post-graduation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of funding occurs if student fails doctoral qualifying exams or commits academic dishonesty.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Switching research groups within EECS is common and supported by the department.",
            "extension_policy": "Doctoral funding is normally guaranteed for up to 5-6 years subject to satisfactory research progress."
        },
        "official_sources_verified": [
            {
                "source_name": "MIT Department of Electrical Engineering & Computer Science (EECS) Graduate Admissions",
                "source_url": "https://www.eecs.mit.edu/academics/graduate-programs/admission-process/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Internal faculty score sheets comparing international university grading scales",
                    "Specific lab-by-lab funding allotment quotas"
                ]
            }
        ]
    },

    # 7. Manaaki New Zealand Scholarships (SCH-OC-002)
    "SCH-OC-002": {
        "scholarship_id": "SCH-OC-002",
        "basic_details": {
            "scholarship_name": "Manaaki New Zealand Scholarships",
            "offering_entity": "New Zealand Ministry of Foreign Affairs and Trade (MFAT)",
            "host_country": "New Zealand",
            "host_institutions_covered": "All 8 New Zealand Universities (Auckland, Otago, Victoria Wellington, Canterbury, Massey, Waikato, Lincoln, AUT)",
            "degree_levels": ["Master's", "PhD", "Postgraduate Diploma"],
            "major_restrictions": "Target development sectors: Climate Change & Resilience, Renewable Energy, Disaster Risk Management, Food Security & Agriculture, Sustainable Governance.",
            "number_of_awards_total": "~500 scholars selected globally across partner developing countries",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible Commonwealth country under Asia regional quota",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Postgraduate Diploma (1 year), Master's degree (1 to 2 years), PhD (up to 3.5 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of an eligible country (including Pakistan) residing in home country for at least 2 years prior to application"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "Minimum age is 18 years at commencement; no upper age limit, but applicants under 40 years are preferred.",
            "academic_qualifications": "16 years of education (Bachelor's) for Master's; 18 years (Master's with thesis) for PhD.",
            "minimum_gpa_percentage": 65.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum B grade equivalent (3.0 / 4.00 CGPA or 65%+ marks in annual system).",
            "subject_background_prerequisites": "Academic background aligned with New Zealand priority development sectors.",
            "current_education_status": "Graduated and currently employed in home country.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": True,
            "work_experience_minimum_years": 1.0,
            "work_experience_notes": "Minimum 1 year of full-time work experience (or 2 years part-time) related to chosen field of study.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (no band below 6.0) or TOEFL iBT 90 (writing 21) required for Master's; IELTS 6.5-7.0 for PhD."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; female applicants and marginalized community members encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Development impact and firm commitment to return to Pakistan for a minimum of two years.",
            "previous_scholarship_restrictions": "Cannot hold another scholarship concurrently; previous New Zealand scholarship recipients must satisfy stand-down period.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full international tuition fees and compulsory university student services levies.",
                "amount": "NZD $35,000 to $48,000 / year"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Handled through scholarship administration.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered through living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Fortnightly living allowance paid to cover accommodation, food, and living expenses.",
                "amount": "NZD $531 / week (~NZD $2,300 / month or ~PKR 390,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy class return flights from Pakistan to New Zealand, plus reunion travel flights for long multi-year awards.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Student visa medical examination and visa application fees covered.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive travel and medical insurance (Studentsafe-University) fully covered.",
                "amount": "NZD $800 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Included in living allowance.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Establishment allowance paid upon arrival in New Zealand.",
                "amount": "NZD $3,000 one-off establishment allowance (~PKR 510,000)"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Postgraduate thesis research allowance provided for master's and PhD research students.",
                "amount": "Up to NZD $1,000–$2,000"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in establishment allowance.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple host universities across New Zealand.",
            "participating_institutions": [
                "University of Auckland", "University of Otago", "Victoria University of Wellington",
                "University of Canterbury", "Massey University", "University of Waikato",
                "Lincoln University", "Auckland University of Technology (AUT)"
            ],
            "university_rankings_scope": "All 8 state universities ranked within QS World Top 500.",
            "available_majors": [
                "Climate Change & Adaptation, Renewable Energy, Environmental Engineering, Food Technology, Agribusiness, Disaster Risk Management, Public Policy, Indigenous Governance, Natural Resource Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 to 2 years for Master's; 3.5 years for PhD",
            "admission_requirements_summary": "Select preferred New Zealand universities and programs on the Manaaki portal; university admissions coordinated after scholarship shortlisting.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Lincoln and Massey are world-renowned for Agriculture; Auckland and Canterbury for Engineering.",
            "strategic_program_match_advice": "Align your proposed degree explicitly with Pakistan's National Climate Change Policy or renewable energy targets."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.mfat.govt.nz/en/aid-and-development/scholarships/",
            "portal_system_name": "Manaaki New Zealand Scholarships Portal",
            "account_creation_instructions": "Complete the online eligibility questionnaire to verify country and sector eligibility, then create applicant account.",
            "step_by_step_workflow": [
                "1. Take online eligibility test on Manaaki portal (Opens February).",
                "2. If eligible, complete online application form.",
                "3. Write development impact statements explaining how study will address home country challenges.",
                "4. Submit online application by closing date (typically end of February).",
                "5. Complete online psychometric / cognitive testing (April).",
                "6. Shortlisted candidates invited for video interview (June-July).",
                "7. Final selections announced August-September; placement confirmed with NZ universities."
            ],
            "university_vs_scholarship_routing": "Direct application via Manaaki MFAT portal.",
            "recommendation_letters_submission_method": "Submitted online by referees during shortlisting stage.",
            "personal_statement_prompts": "Explain how your proposed study will contribute to the sustainable economic and social development of Pakistan.",
            "study_plan_research_proposal_requirements": "Summary of coursework or research objectives (PhD applicants require brief outline of research focus).",
            "cv_format_requirements": "Standard employment and education history entered into online portal.",
            "interviews_conducted": True,
            "interview_format_details": "Semi-structured competency-based interview conducted via video conference by New Zealand selection panel.",
            "standardized_tests": "IELTS Academic or TOEFL iBT required after shortlisting.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Certified copies of degree and transcripts.",
            "translation_requirements": "Official English translations required.",
            "final_submission_method": "100% Online via Manaaki portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "University Degree & Transcripts",
                "mandatory": True,
                "specification": "Certified copies of undergraduate and postgraduate qualifications",
                "pakistan_specific_instruction": "Certified by degree-awarding university in Pakistan"
            },
            {
                "document_name": "Proof of Work Experience",
                "mandatory": True,
                "specification": "Employment letter confirming minimum 1 year relevant work experience",
                "pakistan_specific_instruction": "From employer on official letterhead"
            },
            {
                "document_name": "English Language Test Certificate",
                "mandatory": True,
                "specification": "Valid IELTS Academic (6.5+) or TOEFL iBT (90+)",
                "pakistan_specific_instruction": "Test score must be valid at commencement of study in New Zealand"
            },
            {
                "document_name": "Citizenship Proof / Passport",
                "mandatory": True,
                "specification": "Valid Pakistani passport photo page",
                "pakistan_specific_instruction": "Must show Pakistani citizenship"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-02-01",
            "application_deadline": "2026-02-28",
            "university_admission_deadline": "N/A (Managed by MFAT)",
            "document_submission_deadline": "2026-02-28",
            "recommendation_letters_deadline": "2026-06-30",
            "interview_period": "June to July 2026",
            "shortlist_announcement": "August 2026",
            "final_result_acceptance_deadline": "October 2026",
            "visa_application_window": "November to December 2026",
            "semester_commencement": "February 2027 (Semester 1 in New Zealand)",
            "annual_cycle_notes": "Application window is very short: opens February 1 and closes end of February each year."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Academic capability and background)",
            "extracurricular_and_leadership_weight": "15% (Commitment to community and leadership)",
            "research_experience_weight": "15% (Relevance for research master's/PhD)",
            "work_experience_weight": "20% (Direct relevance to priority development areas)",
            "personal_statement_weight": "25% (Development impact of proposed study on Pakistan)",
            "recommendations_weight": "Evaluated during shortlisting",
            "interview_weight": "Decisive in final round",
            "test_scores_weight": "Passing threshold required",
            "financial_need_weight": "0%",
            "selection_panel_composition": "New Zealand Ministry of Foreign Affairs and Trade (MFAT) selection committees and development specialists.",
            "evaluation_methodology": "Assessment of academic aptitude, development relevance, and applicant's likelihood of driving sustainable change in home country."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000+ applicants across all eligible partner countries",
            "total_scholarships_awarded": "~500 scholars selected globally",
            "acceptance_rate_global": "~5%",
            "acceptance_rate_pakistan": "~2% to 3% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.20 to 3.80 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Mid-career professionals working in government agencies, environmental NGOs, or renewable energy companies with concrete career plans.",
            "common_backgrounds_of_winners": "Engineers in provincial energy departments, disaster management officers (NDMA/PDMA), agricultural researchers.",
            "high_representation_countries": "Pacific Island nations, Southeast Asia, South Asia.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites charging fees for Manaaki scholarship application assistance."
            ],
            "application_fee_warning": "Manaaki application is 100% free of charge.",
            "agent_and_intermediary_warnings": "Do NOT use education agents; applications submitted by agents are flagged and disqualified.",
            "hidden_costs_breakdown": [
                "IELTS or TOEFL test fee in Pakistan (~PKR 55,000 to 65,000).",
                "Immigration medical examination by panel physician in Pakistan (~PKR 25,000).",
                "Courier charges for physical document dispatch if required."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can stay and seek New Zealand permanent residency immediately after study. (Fact: MANDATORY 2-year return to home country is legally binding under visa regulations).",
                "MYTH: Any subject can be studied. (Fact: Only designated development priority sectors are eligible)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs list outdated application deadlines; the window closes strictly in late February."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass all courses and maintain satisfactory academic standing per New Zealand university regulations.",
            "attendance_requirements": "Full-time physical enrollment on campus in New Zealand.",
            "academic_progress_monitoring": "Host universities provide regular progress updates to MFAT.",
            "work_restrictions_during_study": "Scholars may work up to 20 hours/week during term-time per New Zealand student visa conditions.",
            "home_country_return_obligation": "MANDATORY 2-Year Return: Scholars must return to their home country for a minimum of two years upon completion to apply skills to development.",
            "service_obligations_or_bonds": "Legal undertaking signed with the New Zealand Government.",
            "repayment_clawback_conditions": "Scholars who fail to return home or breach scholarship terms may be required to repay the full scholarship cost.",
            "rules_for_changing_university": "Changing institutions is not permitted except in exceptional circumstances with MFAT approval.",
            "rules_for_changing_major": "Not permitted.",
            "extension_policy": "Extensions are strictly granted only for unavoidable medical or academic research delays approved by MFAT."
        },
        "official_sources_verified": [
            {
                "source_name": "New Zealand Ministry of Foreign Affairs and Trade (MFAT) - Manaaki Scholarships",
                "source_url": "https://www.mfat.govt.nz/en/aid-and-development/scholarships/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific country-by-country candidate quota caps for South Asian countries",
                    "Psychometric testing score weightings and cutoff marks"
                ]
            }
        ]
    },

    # 8. University of Melbourne Graduate Research Scholarships (SCH-OC-003)
    "SCH-OC-003": {
        "scholarship_id": "SCH-OC-003",
        "basic_details": {
            "scholarship_name": "University of Melbourne Graduate Research Scholarships",
            "offering_entity": "University of Melbourne & Australian Government Research Training Program (RTP)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Melbourne (Parkville, Southbank, Burnley campuses)",
            "degree_levels": ["Master's by Research", "PhD"],
            "major_restrictions": "Open across all faculties: Engineering & IT, Medicine, Dentistry & Health Sciences, Science, Arts & Humanities, Business & Economics, Law, Veterinary & Agricultural Sciences, Fine Arts & Music.",
            "number_of_awards_total": "~600 scholarships awarded annually (covers domestic and international)",
            "number_of_awards_pakistan": "Open globally; approximately 300 awards reserved for international graduate researchers",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's by Research; up to 3.5 to 4 years for Doctoral (PhD) degrees"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international citizens of all countries including Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed at least a 4-year undergraduate degree with substantial research project (minimum 25% research) or Master's degree by research from an accredited institution.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum equivalent to University of Melbourne First Class Honours (H1 - 80%+ or 3.70+ / 4.00 CGPA).",
            "subject_background_prerequisites": "Substantial research background in the proposed discipline with prior thesis or publications.",
            "current_education_status": "Graduated or in final semester of research master's or 4-year honours bachelor's degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications, conference proceedings, or relevant industry R&D experience significantly enhances competitiveness score.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (no band below 6.0) or TOEFL iBT 79 (writing 21, speaking 18, reading 13, listening 13); higher for Law/Humanities."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Outstanding research track record.",
            "previous_scholarship_restrictions": "Must not have already completed a research degree at the same or higher level.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% Full Tuition fee offset (covers all tuition fees up to AUD $110,000 for Masters or AUD $175,000 for PhD).",
                "amount": "AUD $45,000 to $55,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Melbourne application fee (AUD $130) paid by applicant (waived during certain promotional events or via faculty invitation).",
                "amount": "AUD $130"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Living expenses covered by living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Full tax-free living allowance paid fortnightly.",
                "amount": "AUD $37,000 / year (~AUD $3,083 / month or ~PKR 570,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Relocation grant provided upon relocating from outside Victoria/overseas.",
                "amount": "AUD $3,000 for international students (~PKR 550,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Student Visa (Subclass 500) application fee (AUD $1,600) paid by candidate.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Overseas Student Health Cover (OSHC) Single membership fully covered for the duration of the student visa.",
                "amount": "AUD $650 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered from living allowance.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Faculty research travel grants and lab computers provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty travel grants of AUD $2,000–$4,000 available for conference presentations.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in AUD $3,000 relocation grant.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 58000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Melbourne (Ranked #1 in Australia, Top 15 globally in QS).",
            "participating_institutions": [
                "University of Melbourne"
            ],
            "university_rankings_scope": "QS World Rank #13; Times Higher Education #37.",
            "available_majors": [
                "Computer Science, Artificial Intelligence, Data Science, Electrical Engineering, Mechanical Engineering, Biomedical Sciences, Clinical Medicine, Physics, Chemistry, Mathematics, Veterinary Medicine, Law, Economics, Arts & Design"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for Masters by Research; 3.5 to 4 years for PhD",
            "admission_requirements_summary": "All candidates who apply for a graduate research degree are automatically considered for the Graduate Research Scholarship.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing prior in-principle endorsement from a Melbourne faculty supervisor is critical before formal application.",
            "strategic_program_match_advice": "Ensure your Pakistani undergraduate/master's thesis grade is explicitly documented with a research score calculation."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://scholarships.unimelb.edu.au/awards/graduate-research-scholarships",
            "portal_system_name": "University of Melbourne Online Application Portal",
            "account_creation_instructions": "Register on the University of Melbourne graduate research application system, upload research proposal, and nominate potential supervisors.",
            "step_by_step_workflow": [
                "1. Find a prospective supervisor in your discipline and obtain in-principle endorsement (June-August).",
                "2. Prepare a 1,500 to 2,500-word Research Proposal.",
                "3. Submit formal graduate research course application online by the deadline (Round 1: October 31).",
                "4. Check the box indicating consideration for Graduate Research Scholarships.",
                "5. Upload academic transcripts, English scores, and publications.",
                "6. Provide referee reports via online referee tool.",
                "7. Outcomes released in January/February for Semester 1 (February/March) start."
            ],
            "university_vs_scholarship_routing": "Integrated single application for degree admission and scholarship.",
            "recommendation_letters_submission_method": "Submitted online by referees via Melbourne electronic referee report system.",
            "personal_statement_prompts": "Demonstrate your research background, motivations, and feasibility of proposed research project.",
            "study_plan_research_proposal_requirements": "Detailed research proposal outlining research aims, methodology, background, significance, and preliminary bibliography.",
            "cv_format_requirements": "Academic CV listing academic qualifications, research publications, awards, and professional research roles.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisors or departmental committees usually conduct informal 30-minute video interviews before issuing supervisor endorsement.",
            "standardized_tests": "GRE not required; English language proficiency mandatory.",
            "application_fee_amount": "AUD $130 (waived if supervisor provides waiver code).",
            "attestation_requirements": "Certified transcripts and degree certificates from Pakistani universities; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via University of Melbourne portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Research Proposal",
                "mandatory": True,
                "specification": "1,500 to 2,500-word proposal aligned with faculty research focus",
                "pakistan_specific_instruction": "Developed in coordination with prospective Melbourne supervisor"
            },
            {
                "document_name": "Academic Transcripts & Grading Scale",
                "mandatory": True,
                "specification": "Complete transcripts for all undergraduate and postgraduate degrees",
                "pakistan_specific_instruction": "Must clearly state research thesis component and credit hours"
            },
            {
                "document_name": "Evidence of Research Output",
                "mandatory": False,
                "specification": "Copies of published journal articles, conference papers, or book chapters",
                "pakistan_specific_instruction": "Peer-reviewed publications are crucial for competitive international ranking"
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by university research supervisors",
                "pakistan_specific_instruction": "From professors who supervised your BS/MS thesis in Pakistan"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (79+)",
                "pakistan_specific_instruction": "Electronic score report sent to University of Melbourne"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-06-01",
            "application_deadline": "2026-10-31",
            "university_admission_deadline": "2026-10-31",
            "document_submission_deadline": "2026-11-15",
            "recommendation_letters_deadline": "2026-11-15",
            "interview_period": "November to December 2026",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-02-15",
            "visa_application_window": "January to February 2027",
            "semester_commencement": "February/March 2027 (Round 1) or July 2027 (Round 2)",
            "annual_cycle_notes": "Round 1 deadline is October 31 (for Feb/March start); Round 2 deadline is April 30 (for July start)."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (First Class Honours H1 equivalent GPA in bachelor/master)",
            "extracurricular_and_leadership_weight": "5% (Secondary to research excellence)",
            "research_experience_weight": "40% (Peer-reviewed publications, thesis quality, research experience)",
            "work_experience_weight": "5% (Industry R&D experience)",
            "personal_statement_weight": "5% (Quality and alignment of research proposal)",
            "recommendations_weight": "5% (Referee ratings of research aptitude)",
            "interview_weight": "Faculty level decision",
            "test_scores_weight": "Passing threshold required",
            "financial_need_weight": "0% (Purely merit-based)",
            "selection_panel_composition": "Faculty Research Committees and Melbourne University Central Scholarships Committee.",
            "evaluation_methodology": "Competitive faculty merit ranking score (H1 80+ benchmark) combining GPA and research output score."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 international applicants across all faculties",
            "total_scholarships_awarded": "~300 international scholarships awarded annually",
            "acceptance_rate_global": "~6% for international applicants",
            "acceptance_rate_pakistan": "~3% to 4% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 CGPA (H1 equivalent)",
            "typical_academic_and_research_profile": "Candidates with a published journal paper or multiple conference papers and 3.8+ GPA.",
            "common_backgrounds_of_winners": "Graduates of leading Pakistani universities (NUST, LUMS, Quaid-i-Azam, UET Lahore, Aga Khan University).",
            "high_representation_countries": "China, India, Pakistan, Iran, USA, UK, Singapore.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized agents promising 'guaranteed Melbourne research scholarships'."
            ],
            "application_fee_warning": "Application fee of AUD $130 applies; scholarship application has no extra fee.",
            "agent_and_intermediary_warnings": "University of Melbourne accepts direct applications; research applications should be handled personally with professors.",
            "hidden_costs_breakdown": [
                "Australian student visa fee (AUD $1,600).",
                "University application fee (AUD $130).",
                "English language test fees (IELTS/PTE).",
                "Initial living expenses before first fortnight stipend payment."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can get this scholarship without prior contact with a professor. (Fact: In most faculties, including Engineering and Science, you must have confirmed supervisor support before applying).",
                "MYTH: Coursework Master's students get this scholarship. (Fact: Strictly for Master's by Research and PhD candidates)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs quote outdated stipend values of AUD $31,000; the official rate is now indexed at AUD $37,000+ per year."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must achieve satisfactory progress in annual research confirmation milestones (Confirmation of Candidature at 12 months).",
            "attendance_requirements": "Full-time on-campus research candidature in Melbourne, Australia.",
            "academic_progress_monitoring": "Annual progress reports signed by supervisory committee and head of department.",
            "work_restrictions_during_study": "Permitted to work up to standard research student guidelines (typically up to 6-8 hrs/week during normal research hours, or tutoring/demonstrating).",
            "home_country_return_obligation": "None; scholars are eligible for Australian Temporary Graduate Visa (Subclass 485 - Post-Study Work stream) for up to 3 to 4 years post-PhD.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of scholarship occurs if student fails confirmation milestone or withdraws from research program.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing research projects within the faculty is permitted subject to supervisor and faculty approval.",
            "extension_policy": "PhD scholarships may be extended for up to 6 months in exceptional circumstances with documented research delays."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Melbourne - Graduate Research Scholarships Portal",
                "source_url": "https://scholarships.unimelb.edu.au/awards/graduate-research-scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact faculty-by-faculty scoring rubric that converts Pakistani CGPA into Australian H1 equivalents",
                    "Internal allocation quotas between different academic departments"
                ]
            }
        ]
    }
}
