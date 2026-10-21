# scripts/batch21_p2.py
# SCH-AS-039: Harbin Institute of Technology (HIT) Chinese Government Scholarship (China)
# SCH-AS-040: Xi'an Jiaotong University (XJTU) Silk Road CSC Scholarship (China)
# SCH-AS-043: Universiti Kebangsaan Malaysia (UKM) Graduate Research Fellowship (Malaysia)

DATA_P2 = {
    "SCH-AS-039": {
        "scholarship_id": "SCH-AS-039",
        "basic_details": {
            "scholarship_name": "Harbin Institute of Technology (HIT) Chinese Government Scholarship (CSC High-Level Postgraduate Program)",
            "offering_entity": "China Scholarship Council (CSC - Ministry of Education of China) & Harbin Institute of Technology",
            "host_country": "China",
            "host_institutions_covered": "Harbin Institute of Technology Main Campus (Harbin, Heilongjiang Province, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Computing & School of Electrical Engineering and Automation: Computer Science and Technology, Artificial Intelligence, Cybersecurity, Software Engineering, Robotics and Intelligent Systems, and Control Science.",
            "number_of_awards_total": "~150 to 220 fully funded CSC High-Level and University Postgraduate Scholarships awarded annually",
            "number_of_awards_pakistan": "Extremely strong bilateral quota; Pakistani computing and aerospace researchers secure ~20 to 35 fully funded awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 to 3 years for Master of Science; 3 to 4 years for Doctor of Philosophy, subject to passing annual CSC scholarship review",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "RMB 3,000 / month for Master's (~PKR 115,000 / month); RMB 3,500 / month for PhD (~PKR 135,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens in good health holding valid foreign passports (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Master's applicants must be under 35 years of age; PhD applicants must be under 40 years of age.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) with minimum CGPA 3.30 / 4.00 (or 75%+ marks) from an HEC-recognized university in Pakistan for Master's; recognized MS/MPhil (18 years education) with strong thesis output for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum grade equivalent of Grade B+ or 75% marks across academic transcript.",
            "subject_background_prerequisites": "Rigorous undergraduate preparation in algorithms, computer architectures, linear algebra, discrete mathematics, and programming (C/C++, Python).",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 80, or institutional English Medium of Instruction (MOI) certificate from Pakistani university.",
            "other_language_requirements": "Chinese language proficiency (HSK) is not required for English-taught graduate programs.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must contact a prospective supervisor at HIT Faculty of Computing and obtain an official Acceptance Letter prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or provincial scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee exemption at Harbin Institute of Technology covered for the entire program duration.",
                "amount": "100% covered (~RMB 28,000 - 42,000 / year value; ~PKR 1,090,000 - 1,640,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "HIT international graduate application fee of RMB 400 (~USD 60 / ~PKR 16,000) payable online.",
                "amount": "RMB 400 (~PKR 16,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free accommodation in on-campus international student dormitories (twin room for Master's, single room for PhD) at HIT Harbin Campus, or monthly housing subsidy.",
                "amount": "100% covered free dormitory accommodation"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living allowance: RMB 3,000 per month for Master's students (~PKR 115,000 / month; RMB 36,000 / year); RMB 3,500 per month for PhD scholars (~PKR 135,000 / month; RMB 42,000 / year).",
                "amount": "RMB 3,000 - 3,500 / month (~PKR 115,000 - 135,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses must be arranged by the student; living allowance easily accommodates local savings.",
                "amount": "Self-funded economy flight (~PKR 160,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 Student Visa application fee (~PKR 15,000) at the Chinese Embassy in Islamabad or Consulate in Karachi.",
                "amount": "PKR 15,000"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Medical Insurance for International Students in China (Ping An Insurance ~RMB 800 / year) provided 100% free by the CSC.",
                "amount": "100% covered by China Scholarship Council"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of RMB 3,000 - 3,500; heavily subsidized campus canteens provide complete halal meals for RMB 10 - 20 per meal.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to HIT Central Library, laboratory workstations, robotics testbeds, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's national research grants for presenting papers at conferences.",
                "amount": "Up to RMB 5,000 for conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle links and convenient connection to Harbin Metro Line 1 (HIT Station).",
                "amount": "Convenient metro and campus access"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite C9 League university: Harbin Institute of Technology (HIT).",
            "participating_institutions": [
                "Harbin Institute of Technology (Harbin Campus, Heilongjiang Province, China)"
            ],
            "university_rankings_scope": "Member of China's elite C9 League; globally ranked #4 in Best Global Universities for Engineering (US News), and top 50 globally in Computer Science, Artificial Intelligence, and Robotics.",
            "available_majors": [
                "Computer Science and Technology",
                "Artificial Intelligence and Cognitive Computing",
                "Cyber Science and Engineering",
                "Software Engineering and Distributed Systems",
                "Control Science and Engineering",
                "Robotics and Autonomous Systems",
                "Aerospace Information Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 to 3 years for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor acceptance letter, study plan (1,000 words), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "HIT Computing and Robotics research institutes are world-renowned and attract top engineering talent; obtaining an official Acceptance Letter from a faculty professor is the key gatekeeper to CSC nomination.",
            "strategic_program_match_advice": "Browse HIT Faculty of Computing faculty profiles (computing.hit.edu.cn), email prospective supervisors with a tailored research proposal and CV, and obtain the official HIT Acceptance Letter before the February 15 CSC deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://hit.edusys.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "HIT International Student Application System & CSC Portal",
            "account_creation_instructions": "Register an account on the HIT online application portal, select graduate program, check the box applying for Chinese Government Scholarship, and apply on the CSC portal (Agency No: 10213).",
            "step_by_step_workflow": [
                "Step 1: Contact prospective supervisors in HIT Faculty of Computing and secure an official Acceptance Letter (October - January).",
                "Step 2: Create user credentials on the HIT International Student Admissions Portal (http://hit.edusys.cn/).",
                "Step 3: Submit online degree application, upload all required documents, and select Chinese Government Scholarship.",
                "Step 4: Pay the application fee of RMB 400 online before the deadline (typically February 15).",
                "Step 5: Apply on the CSC portal (https://studyinchina.csc.edu.cn/) under Type B using HIT Agency Number 10213.",
                "Step 6: HIT faculty committee conducts academic review and online technical interviews in March.",
                "Step 7: Official admission and scholarship package (JW201 form) dispatched in June/July; apply for Chinese X1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via the HIT portal covers both program admission and scholarship nomination.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by former academic professors or research supervisors.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words in English) outlining academic background, proposed research focus, and reasons for choosing HIT.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute technical video interview via Zoom / Tencent Meeting conducted by faculty admissions panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "RMB 400 (~USD 60 / ~PKR 16,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English or Chinese translation required for all official documents.",
            "final_submission_method": "Online upload via HIT admissions portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "HIT Professor Acceptance Letter (Official Form)",
                "mandatory": True,
                "specification": "Official acceptance letter signed by an eligible HIT professor.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Study and Research Plan (Minimum 1,000 words)",
                "mandatory": True,
                "specification": "Detailed research plan outlining academic background, proposed research questions, and methodology.",
                "pakistan_specific_instruction": "Must be aligned with HIT supervisor's lab projects."
            },
            {
                "document_name": "Two Recommendation Letters from Full or Associate Professors",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors.",
                "pakistan_specific_instruction": "Printed on official university letterhead with institutional email."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Official Chinese physical examination form signed by an authorized physician with hospital stamp.",
                "pakistan_specific_instruction": "Completed at an authorized diagnostic center with blood test and chest X-ray reports."
            },
            {
                "document_name": "Non-Criminal Record Certificate (Police Clearance)",
                "mandatory": True,
                "specification": "Official police character certificate issued within the preceding 6 months.",
                "pakistan_specific_instruction": "Obtained from local police service center and attested by MOFA."
            },
            {
                "document_name": "English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI letter.",
                "pakistan_specific_instruction": "MOI letter signed by university registrar."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of passport bio page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 15",
            "application_deadline": "February 15",
            "university_admission_deadline": "February 15",
            "document_submission_deadline": "February 15",
            "recommendation_letters_deadline": "February 22",
            "interview_period": "March - April",
            "shortlist_announcement": "Late April",
            "final_result_acceptance_deadline": "June",
            "visa_application_window": "July - August",
            "semester_commencement": "Early September (commencing in Harbin)",
            "annual_cycle_notes": "Main intake is Autumn (September). Applications close annually on February 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate GPA and performance in core computing, robotics, and engineering courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor acceptance letter, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for HIT)",
            "recommendations_weight": "10% (Academic referee appraisals and professor's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into final ranking)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "HIT Faculty Admissions Board and College of International Education Scholarship Committee.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit and professor nomination followed by faculty panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,800 international graduate applicants across HIT",
            "total_scholarships_awarded": "~150 to 220 fully funded CSC scholarships awarded annually",
            "acceptance_rate_global": "~6% to 9%",
            "acceptance_rate_pakistan": "~10% to 15% among candidates with professor acceptance letters",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, Russia, Iran, Bangladesh, Indonesia, Egypt, Nigeria, Thailand.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed CSC scholarships or HIT admissions.",
                "Applications are handled exclusively via the official HIT portal (http://hit.edusys.cn/) and CSC portal."
            ],
            "application_fee_warning": "HIT application fee is RMB 400 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Harbin Institute of Technology does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "HIT application fee: RMB 400 (~PKR 16,000).",
                "Foreigner physical examination in Pakistan: ~PKR 15,000.",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~RMB 2,000 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get CSC without a professor's acceptance letter. Reality: At top C9 universities like HIT, having a professor's acceptance letter is essential for scholarship nomination.",
                "Myth: Harbin winter is unmanageable. Reality: All indoor facilities, classrooms, and dormitories in Harbin have state-mandated 24/7 central heating maintaining 22-25°C."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state application deadline is April; HIT CSC scholarship application portal closes strictly on February 15."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and pass the mandatory CSC Annual Scholarship Review each spring.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab in Harbin.",
            "academic_progress_monitoring": "Annual progress report submitted to the Graduate School and China Scholarship Council.",
            "work_restrictions_during_study": "Part-time work off-campus is strictly restricted under Chinese student visa regulations; campus work-study permitted with university approval.",
            "home_country_return_obligation": "No return obligation; graduates are free to work in China or globally under Chinese work visa (Z-visa) schemes.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Funding cancelled if the student fails annual review, engages in illegal employment, or breaches Chinese law.",
            "rules_for_changing_university": "Non-transferable to other Chinese universities.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Graduate School.",
            "extension_policy": "Master's programs cannot be extended; PhD programs can apply for up to 1-year extension based on exceptional research progress."
        },
        "official_sources_verified": [
            {
                "source_name": "HIT College of International Education Official Portal",
                "source_url": "http://hit.edusys.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "https://studyinchina.csc.edu.cn/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-040": {
        "scholarship_id": "SCH-AS-040",
        "basic_details": {
            "scholarship_name": "Xi'an Jiaotong University (XJTU) Silk Road CSC Scholarship & XJTU Fellowship",
            "offering_entity": "China Scholarship Council (CSC - Ministry of Education of China) & Xi'an Jiaotong University",
            "host_country": "China",
            "host_institutions_covered": "Xi'an Jiaotong University Xingqing Campus & Western China Science and Technology Innovation Harbour (iHarbour, Xi'an, Shaanxi, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Electronic and Information Engineering: Computer Science and Technology, Artificial Intelligence and Automation, Software Engineering, Information and Communication Engineering, and Cybersecurity.",
            "number_of_awards_total": "~200 to 300 Chinese Government Scholarships (Silk Road Program) and XJTU Fellowships awarded annually",
            "number_of_awards_pakistan": "Extremely prominent bilateral allocation under Belt and Road / CPEC academic corridors; Pakistani graduate scholars secure ~30 to 50 fully funded awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 to 3 years for Master of Science; 3 to 4 years for Doctor of Philosophy, subject to passing annual CSC scholarship review",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "RMB 3,000 / month for Master's (~PKR 115,000 / month); RMB 3,500 / month for PhD (~PKR 135,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of Belt and Road countries, holding foreign passports in good health (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Master's applicants must be under 35 years of age; PhD applicants must be under 40 years of age.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) with minimum CGPA 3.30 / 4.00 (or 75%+ marks) from an HEC-recognized university in Pakistan for Master's; recognized MS/MPhil (18 years education) with strong thesis output for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum grade equivalent of Grade B+ or 75% marks across academic transcript.",
            "subject_background_prerequisites": "Rigorous undergraduate preparation in algorithms, computer architectures, linear algebra, discrete mathematics, and programming (C/C++, Python).",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 80, or institutional English Medium of Instruction (MOI) certificate from Pakistani university.",
            "other_language_requirements": "Chinese language proficiency (HSK) is not required for English-taught graduate programs.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants should contact a prospective supervisor at XJTU and obtain an official Acceptance Letter prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or provincial scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee exemption at Xi'an Jiaotong University covered for the entire program duration.",
                "amount": "100% covered (~RMB 28,000 - 40,000 / year value; ~PKR 1,090,000 - 1,560,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "XJTU international graduate application fee of RMB 800 (~USD 115 / ~PKR 32,000) payable online.",
                "amount": "RMB 800 (~PKR 32,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free accommodation in on-campus international student dormitories (twin room for Master's, single room for PhD) at Xingqing Campus or iHarbour, or monthly housing subsidy.",
                "amount": "100% covered free dormitory accommodation"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living allowance: RMB 3,000 per month for Master's students (~PKR 115,000 / month; RMB 36,000 / year); RMB 3,500 per month for PhD scholars (~PKR 135,000 / month; RMB 42,000 / year).",
                "amount": "RMB 3,000 - 3,500 / month (~PKR 115,000 - 135,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses must be arranged by the student; living allowance easily accommodates local savings.",
                "amount": "Self-funded economy flight (~PKR 150,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 Student Visa application fee (~PKR 15,000) at the Chinese Embassy in Islamabad or Consulate in Karachi.",
                "amount": "PKR 15,000"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Medical Insurance for International Students in China (Ping An Insurance ~RMB 800 / year) provided 100% free by the CSC.",
                "amount": "100% covered by China Scholarship Council"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of RMB 3,000 - 3,500; heavily subsidized campus canteens provide complete halal meals for RMB 10 - 20 per meal.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to XJTU Central Library, iHarbour smart computing centers, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's national research grants for presenting papers at conferences.",
                "amount": "Up to RMB 5,000 for conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle links and direct connection via Xi'an Metro Line 5 to iHarbour Innovation Campus.",
                "amount": "Convenient metro and campus access"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite C9 League university: Xi'an Jiaotong University (XJTU).",
            "participating_institutions": [
                "Xi'an Jiaotong University (Xingqing Campus & iHarbour, Xi'an, Shaanxi, China)"
            ],
            "university_rankings_scope": "Member of China's elite C9 League; ranked top 200 globally in QS/THE World Rankings, top 50 globally in Computer Science and Engineering, and founding headquarters of the University Alliance of the Silk Road (UASR).",
            "available_majors": [
                "Computer Science and Technology",
                "Artificial Intelligence and Intelligent Systems",
                "Cyber Science and Technology",
                "Software Engineering and Cloud Computing",
                "Information and Communication Engineering",
                "Control Science and Engineering",
                "Electrical Engineering and Power Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 to 3 years for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor acceptance letter, study plan (1,000 words), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "XJTU AI and Computer Science institutes at the state-of-the-art iHarbour campus are world-class; obtaining an official Acceptance Letter from a faculty professor is the key gatekeeper to CSC nomination.",
            "strategic_program_match_advice": "Browse XJTU Faculty of Electronic and Information Engineering faculty profiles (eie.xjtu.edu.cn), email prospective supervisors with a tailored research proposal and CV, and obtain the official XJTU Acceptance Letter before the February 15 deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://isso.xjtu.edu.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "XJTU International Student Application System & CSC Portal",
            "account_creation_instructions": "Register an account on the XJTU online application portal, select graduate program, check the box applying for Chinese Government Scholarship / Silk Road Program, and apply on the CSC portal (Agency No: 10698).",
            "step_by_step_workflow": [
                "Step 1: Contact prospective supervisors in XJTU Faculty of Electronic and Information Engineering and secure an official Acceptance Letter (October - January).",
                "Step 2: Create user credentials on the XJTU International Student Admissions Portal (http://isso.xjtu.edu.cn/).",
                "Step 3: Submit online degree application, upload all required documents, and select Chinese Government Scholarship.",
                "Step 4: Pay the application fee of RMB 800 online before the deadline (typically February 15).",
                "Step 5: Apply on the CSC portal (https://studyinchina.csc.edu.cn/) under Type B using XJTU Agency Number 10698.",
                "Step 6: XJTU faculty committee conducts academic review and online technical interviews in March.",
                "Step 7: Official admission and scholarship package (JW201 form) dispatched in June/July; apply for Chinese X1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via the XJTU portal covers both program admission and scholarship nomination.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by former academic professors or research supervisors.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words in English) outlining academic background, proposed research focus, and reasons for choosing XJTU.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute technical video interview via Zoom / Tencent Meeting conducted by faculty admissions panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "RMB 800 (~USD 115 / ~PKR 32,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English or Chinese translation required for all official documents.",
            "final_submission_method": "Online upload via XJTU admissions portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "XJTU Professor Acceptance Letter (Official Form)",
                "mandatory": True,
                "specification": "Official acceptance letter signed by an eligible XJTU professor.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Study and Research Plan (Minimum 1,000 words)",
                "mandatory": True,
                "specification": "Detailed research plan outlining academic background, proposed research questions, and methodology.",
                "pakistan_specific_instruction": "Must be aligned with XJTU supervisor's lab projects."
            },
            {
                "document_name": "Two Recommendation Letters from Full or Associate Professors",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors.",
                "pakistan_specific_instruction": "Printed on official university letterhead with institutional email."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Official Chinese physical examination form signed by an authorized physician with hospital stamp.",
                "pakistan_specific_instruction": "Completed at an authorized diagnostic center with blood test and chest X-ray reports."
            },
            {
                "document_name": "Non-Criminal Record Certificate (Police Clearance)",
                "mandatory": True,
                "specification": "Official police character certificate issued within the preceding 6 months.",
                "pakistan_specific_instruction": "Obtained from local police service center and attested by MOFA."
            },
            {
                "document_name": "English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI letter.",
                "pakistan_specific_instruction": "MOI letter signed by university registrar."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of passport bio page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 15",
            "application_deadline": "February 15",
            "university_admission_deadline": "February 15",
            "document_submission_deadline": "February 15",
            "recommendation_letters_deadline": "February 22",
            "interview_period": "March - April",
            "shortlist_announcement": "Late April",
            "final_result_acceptance_deadline": "June",
            "visa_application_window": "July - August",
            "semester_commencement": "Early September (commencing in Xi'an)",
            "annual_cycle_notes": "Main intake is Autumn (September). Applications close annually on February 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate GPA and performance in core computing, AI, and engineering courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor acceptance letter, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for XJTU)",
            "recommendations_weight": "10% (Academic referee appraisals and professor's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into final ranking)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "XJTU Faculty Admissions Board and School of International Education Scholarship Committee.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit and professor nomination followed by faculty panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,800 to 4,200 international graduate applicants across XJTU",
            "total_scholarships_awarded": "~200 to 300 fully funded CSC scholarships awarded annually",
            "acceptance_rate_global": "~7% to 10%",
            "acceptance_rate_pakistan": "~12% to 18% among candidates with professor acceptance letters",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, Russia, Iran, Kazakhstan, Bangladesh, Indonesia, Egypt, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed CSC scholarships or XJTU admissions.",
                "Applications are handled exclusively via the official XJTU portal (http://isso.xjtu.edu.cn/) and CSC portal."
            ],
            "application_fee_warning": "XJTU application fee is RMB 800 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Xi'an Jiaotong University does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "XJTU application fee: RMB 800 (~PKR 32,000).",
                "Foreigner physical examination in Pakistan: ~PKR 15,000.",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~RMB 2,000 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get CSC without a professor's acceptance letter. Reality: At top C9 universities like XJTU, having a professor's acceptance letter is essential for scholarship nomination.",
                "Myth: You must study in Chinese. Reality: XJTU offers complete Master's and PhD programs taught and researched 100% in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state application deadline is April; XJTU CSC scholarship application portal closes strictly on February 15."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and pass the mandatory CSC Annual Scholarship Review each spring.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab in Xi'an.",
            "academic_progress_monitoring": "Annual progress report submitted to the Graduate School and China Scholarship Council.",
            "work_restrictions_during_study": "Part-time work off-campus is strictly restricted under Chinese student visa regulations; campus work-study permitted with university approval.",
            "home_country_return_obligation": "No return obligation; graduates are free to work in China or globally under Chinese work visa (Z-visa) schemes.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Funding cancelled if the student fails annual review, engages in illegal employment, or breaches Chinese law.",
            "rules_for_changing_university": "Non-transferable to other Chinese universities.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Graduate School.",
            "extension_policy": "Master's programs cannot be extended; PhD programs can apply for up to 1-year extension based on exceptional research progress."
        },
        "official_sources_verified": [
            {
                "source_name": "XJTU School of International Education Official Portal",
                "source_url": "http://isso.xjtu.edu.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "https://studyinchina.csc.edu.cn/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-043": {
        "scholarship_id": "SCH-AS-043",
        "basic_details": {
            "scholarship_name": "Universiti Kebangsaan Malaysia (UKM) Graduate Research Fellowship (ZAMALAH / GRA)",
            "offering_entity": "Universiti Kebangsaan Malaysia (UKM - The National University of Malaysia) & MOHE",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Kebangsaan Malaysia Main Campus (Bangi, Selangor, Malaysia)",
            "degree_levels": ["Master of Science (MSc by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Information Science and Technology (FTSM) & Faculty of Engineering and Built Environment (FKAB): Computer Science, Artificial Intelligence, Software Engineering, Cybersecurity, Information Systems, and Electrical Engineering.",
            "number_of_awards_total": "~80 to 120 Zamalah Graduate Fellowships and Graduate Research Assistantships (GRA) awarded annually",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~10 to 16 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 3 to 4 years for PhD, subject to satisfactory semester research progress evaluations",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "MYR 1,800 to MYR 2,800 / month living stipend (~PKR 115,000 - 182,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must generally be under 35 years old at the time of application.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) with minimum CGPA 3.30 / 4.00 for Master's; recognized MS/MPhil (18 years education) with minimum CGPA 3.50 / 4.00 for PhD from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum grade equivalent of Grade B+ or CGPA 3.30 / 4.00.",
            "subject_background_prerequisites": "Rigorous undergraduate preparation in computer science, software engineering, or electrical engineering.",
            "current_education_status": "Graduating seniors or Master's students in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development projects, hackathon achievements, or published research papers are advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 79, or institutional English Medium of Instruction (MOI) certificate from an accredited Pakistani university.",
            "other_language_requirements": "None; postgraduate research and coursework are conducted 100% in English.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must identify a prospective supervisor at UKM FTSM and obtain preliminary consent.",
            "previous_scholarship_restrictions": "Cannot hold another full national or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and academic examination fee waiver at Universiti Kebangsaan Malaysia covered by the scholarship or research grant.",
                "amount": "100% covered (~MYR 16,000 - 24,000 / year value; ~PKR 1,040,000 - 1,560,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UKM international postgraduate application fee (~MYR 250 / USD 60) paid online via the portal.",
                "amount": "MYR 250 (~PKR 16,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus student residential colleges (Kolej Keris Mas / Kolej Ibu Zain) at UKM Bangi; monthly rent is paid from the monthly living allowance.",
                "amount": "Subsidized rent ~MYR 400 - 650 / month (~PKR 26,000 - 42,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend: MYR 1,800 to MYR 2,300 per month for Master's; MYR 2,300 to MYR 2,800 per month for PhD (~PKR 115,000 - 182,000 / month; MYR 21,600 - 33,600 / year).",
                "amount": "MYR 1,800 - 2,800 / month (~PKR 115,000 - 182,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare to Malaysia arranged by student; living allowance easily accommodates local savings.",
                "amount": "Self-funded economy flight (~PKR 120,000)"
            },
            "visa_fee": {
                "status": "PARTIAL",
                "details": "EMGS visa approval letter (VAL) and Student Pass fees (~MYR 2,000 total) covered from stipend or research grant.",
                "amount": "Covered via initial stipend"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Mandatory Malaysian student health and hospitalization insurance included within the EMGS Student Pass package.",
                "amount": "100% covered via EMGS insurance package"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of MYR 1,800 - 2,800; campus cafeterias provide affordable halal meals.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to UKM Tun Seri Lanang Library, engineering laboratories, GPU clusters, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental research funding available through supervisor's research grants for publishing in indexed journals.",
                "amount": "Up to MYR 3,500 for conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UKM campus shuttle bus service operating across all academic zones and the UKM KTM commuter railway station.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 15000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Malaysian national research university: Universiti Kebangsaan Malaysia (UKM).",
            "participating_institutions": [
                "Universiti Kebangsaan Malaysia Main Campus (Bangi, Selangor, Malaysia)"
            ],
            "university_rankings_scope": "Ranked #138 globally in QS World University Rankings, #4 in Malaysia, and top 100 globally in Computer Science and Engineering.",
            "available_majors": [
                "MSc / PhD in Computer Science (Artificial Intelligence, Machine Learning)",
                "MSc / PhD in Software Engineering",
                "MSc / PhD in Cybersecurity and Cryptography",
                "MSc / PhD in Information Systems and Data Science",
                "MSc / PhD in Microelectronics and Embedded Systems",
                "MSc / PhD in Intelligent Robotics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for MSc; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree (minimum CGPA 3.3/4.0) for Master's; Master's degree (minimum CGPA 3.5/4.0) for PhD, supervisor consent, research proposal, two recommendation letters, and English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "UKM FTSM AI and Software Engineering labs have high demand; reaching out to supervisors with active MOHE/FRGS research grants is the primary path to guaranteed funding.",
            "strategic_program_match_advice": "Browse the UKM Faculty of Information Science and Technology directory (ftsm.ukm.my), identify matching research groups in AI/software, and email prospective professors attaching your CV and a 2-page research proposal before applying on the UKM graduate portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ukm.my/portal/postgraduate/ & https://join.ukm.my/",
            "portal_system_name": "UKM Join Postgraduate Admissions Portal",
            "account_creation_instructions": "Identify prospective supervisor on UKM portal, secure consent, register an applicant account on UKM Join, submit degree application, and apply for the Zamalah / GRA scholarship scheme.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research profiles on UKM FTSM portal (https://www.ukm.my/ftsm/).",
                "Step 2: Email prospective supervisor with academic transcripts, CV, and a 2-page research proposal to secure consent.",
                "Step 3: Register and apply online for postgraduate admission on the UKM Join portal (https://join.ukm.my/).",
                "Step 4: Upload attested transcripts, degrees, research proposal, CV, and reference letters.",
                "Step 5: Apply for Zamalah / Graduate Research Assistantship (GRA) scheme through the supervisor's endorsement.",
                "Step 6: Attend faculty technical interview via Zoom if required.",
                "Step 7: Receive official offer letter and fellowship award, then initiate the EMGS visa approval letter (VAL) process."
            ],
            "university_vs_scholarship_routing": "Integrated Supervisor Track: Admission and funding are processed jointly through the supervising faculty.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by former academic professors or research supervisors.",
            "personal_statement_prompts": "Statement of academic purpose detailing research accomplishments, technical capabilities, and postgraduate research vision.",
            "study_plan_research_proposal_requirements": "Structured 2 to 4-page research proposal detailing background, problem statement, research methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute technical interview via Zoom conducted by prospective supervisor and faculty panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 79), or institutional English MOI letter accepted; GRE not required.",
            "application_fee_amount": "MYR 250 (~USD 60 / ~PKR 16,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Online submission via UKM Join admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year Bachelor's (for MSc) or 18-year Master's (for PhD) with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "Postgraduate Research Proposal",
                "mandatory": True,
                "specification": "2 to 4-page structured proposal outlining problem statement, methodology, and timeline.",
                "pakistan_specific_instruction": "Must be aligned with UKM supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible UKM professor agreeing to supervise.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential academic evaluations from previous professors.",
                "pakistan_specific_instruction": "Printed on official university letterhead."
            },
            {
                "document_name": "English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 79), or institutional English MOI letter.",
                "pakistan_specific_instruction": "MOI letter signed by university registrar."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of all passport pages valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Open year-round (Semester 1 intake opens March / Semester 2 opens September)",
            "application_deadline": "June 30 (for October intake) / November 30 (for March intake)",
            "university_admission_deadline": "June 30 / November 30",
            "document_submission_deadline": "June 30 / November 30",
            "recommendation_letters_deadline": "June 30 / November 30",
            "interview_period": "July - August / December - January",
            "shortlist_announcement": "August / January",
            "final_result_acceptance_deadline": "September / February",
            "visa_application_window": "August - September / January - February",
            "semester_commencement": "October (Semester 1) / March (Semester 2)",
            "annual_cycle_notes": "Admissions operate on two semester intakes: Semester 1 (October) and Semester 2 (March). Applying 3-4 months in advance is recommended."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Previous degree GPA, minimum 3.30/4.00 requirement)",
            "extracurricular_and_leadership_weight": "5% (Technical community contributions)",
            "research_experience_weight": "35% (Quality of research proposal, technical project portfolio, and supervisor match)",
            "work_experience_weight": "5% (Industry or university research assistant experience)",
            "personal_statement_weight": "10% (Clarity of purpose and postgraduate research vision)",
            "recommendations_weight": "10% (Referee appraisals and supervisor endorsement)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "UKM Centre for Graduate Management and Faculty of Information Science Postgraduate Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty board academic review."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international applicants for UKM postgraduate programs",
            "total_scholarships_awarded": "~80 to 120 graduate research scholarships awarded annually",
            "acceptance_rate_global": "~8% to 12%",
            "acceptance_rate_pakistan": "~10% to 15% among candidates with supervisor consent",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electrical engineering faculties.",
            "high_representation_countries": "Pakistan, Bangladesh, China, Iran, Nigeria, Indonesia, India, Yemen.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of educational agents claiming to provide 'guaranteed UKM admissions or scholarship awards'.",
                "Applications are handled exclusively via the official UKM Join portal (https://join.ukm.my/)."
            ],
            "application_fee_warning": "UKM application fee is MYR 250 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Universiti Kebangsaan Malaysia does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "UKM application fee: MYR 250 (~PKR 16,000).",
                "EMGS visa approval letter (VAL) and medical fee: ~MYR 2,000 (~PKR 130,000).",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~MYR 1,500 (~PKR 98,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without a supervisor. Reality: Research Master's and PhD applications at UKM require prior engagement and consent from a qualified supervisor.",
                "Myth: Language of instruction is Malay. Reality: UKM postgraduate STEM programs are researched, written, and defended 100% in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state IELTS 6.5 is mandatory; UKM requires IELTS 6.0 or institutional English MOI letter for computing degrees."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress (Progress Report Grade Satisfactory) each semester.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at UKM Bangi.",
            "academic_progress_monitoring": "Semi-annual progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "GRA recipients may be assigned teaching assistantship or grading duties (up to 6 hours/week) within the faculty.",
            "home_country_return_obligation": "No return obligation; graduates are free to pursue postdocs or careers in Malaysia or worldwide.",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 1-2 papers in indexed journals prior to thesis submission.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails progress evaluations twice or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Universiti Kebangsaan Malaysia.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Faculty Postgraduate Committee.",
            "extension_policy": "Scholarship is granted for standard duration (2 years for Master's; 3-4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "UKM Centre for Graduate Management Portal",
                "source_url": "https://www.ukm.my/portal/postgraduate/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UKM Join Postgraduate Admissions Portal",
                "source_url": "https://join.ukm.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
