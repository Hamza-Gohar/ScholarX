# scripts/batch16_p2.py
# SCH-AS-044: Nanjing University (NJU) Chinese Government Scholarship (China)
# SCH-AS-049: Beihang University (BUAA) Chinese Government & University Postgrad Award (China)
# SCH-AS-066: Seoul National University (SNU) Global Scholarship (South Korea)
# SCH-AS-072: Nanyang Technological University (NTU) Nanyang President's Graduate Scholarship (Singapore)

DATA_P2 = {
    "SCH-AS-044": {
        "scholarship_id": "SCH-AS-044",
        "basic_details": {
            "scholarship_name": "Nanjing University Chinese Government Scholarship - High Level Postgraduate Program (CSC Type B)",
            "offering_entity": "China Scholarship Council (CSC) & Nanjing University (NJU)",
            "host_country": "China",
            "host_institutions_covered": "Nanjing University (Xianlin, Gulou, and Pukou Campuses, Nanjing, Jiangsu Province, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all accredited graduate programs at NJU with strategic priority in Artificial Intelligence, Computer Science and Technology, Electronic Science and Engineering, Environmental Sciences, Astronomy, Chemistry, Physics, and International Business.",
            "number_of_awards_total": "~120 to 160 university-nominated CSC High-Level Postgraduate scholarships awarded annually across all disciplines",
            "number_of_awards_pakistan": "Open international competition; Pakistani postgraduates represent one of the largest national contingents (~15 to 25 recipients annually across STEM faculties)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 to 3 years for Master's; up to 3 to 4 years for PhD programs"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of a country other than the People's Republic of China (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Applicants for Master's degree programs must be under 35 years of age; applicants for Doctoral programs must be under 40 years of age.",
            "academic_qualifications": "Bachelor's degree (16 years education) for Master's applicants; Master's degree (18 years education) for PhD applicants from an HEC-recognized university with high academic achievement (minimum 75% aggregate or CGPA 3.20 / 4.00; competitive admits typically maintain 3.50+ / 4.00).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Grades converted to CSC 4.0 scale; applicants should rank in the top 20% of their graduating class.",
            "subject_background_prerequisites": "Relevant undergraduate/postgraduate degree corresponding directly to the applied research discipline.",
            "current_education_status": "Graduating university seniors in their final semester can apply conditionally with an official pre-graduation bonafide certificate.",
            "graduation_year_restrictions": "None, provided age and degree eligibility parameters are satisfied.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications in SCI/EI indexed journals or patent filings significantly elevate PhD competitiveness.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "For English-taught majors: IELTS Academic min 6.0 (6.5 preferred for computing/business) or TOEFL iBT min 85. Official English Medium of Instruction (MOI) certificates from Pakistani HEC-recognized universities are widely accepted by NJU academic supervisors.",
            "other_language_requirements": "For Chinese-taught programs: HSK Level 5 with a score of 180 or above is mandatory.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure a provisional Acceptance Letter (Pre-Admission Supervision Notice) from an accredited NJU professor/supervisor prior to final institutional review.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent Chinese Government, provincial, or municipal scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver for the complete official degree duration (RMB 32,000 to 45,000 / year value).",
                "amount": "100% covered (~RMB 35,000 / year; ~PKR 1,365,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "Nanjing University international application fee of RMB 600 (~USD 85; ~PKR 23,500) payable upon submission of the institutional portal.",
                "amount": "RMB 600 (~PKR 23,500)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free on-campus accommodation provided in university international student dormitories (single room for PhD students, shared twin room for Master's students) on Xianlin or Gulou Campus, or monthly housing subsidy of RMB 700 to 1,000 if living off-campus with university approval.",
                "amount": "100% covered dormitory or RMB 700-1,000/mo allowance"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Standard China Scholarship Council monthly living stipend: RMB 3,000 / month for Master's students (~USD 420; ~PKR 117,000 / month); RMB 3,500 / month for PhD students (~USD 490; ~PKR 136,500 / month).",
                "amount": "RMB 3,000 to 3,500 / month (~PKR 117,000 to 136,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International round-trip travel expenses between Pakistan and Nanjing are self-funded by the scholar.",
                "amount": "Not covered (Self-funded ~PKR 160,000 to 220,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 Student Visa application fees and medical examination fees in Pakistan are borne by the student.",
                "amount": "Not covered (~PKR 25,000 to 35,000 for visa and medical)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive Medical Insurance for International Students in China provided by Ping An Insurance (RMB 800 / year value).",
                "amount": "100% covered (RMB 800 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "University canteens (including halal-certified cafeterias on Xianlin and Gulou campuses) provide subsidized meals for RMB 20 to 35/day; easily covered by the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Full access to Nanjing University libraries, scientific databases, high-performance computing clusters, and laboratory research facilities.",
                "amount": "Covered via institutional infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Research project supplies, fieldwork, and domestic academic conferences funded through supervisor's National Natural Science Foundation of China (NSFC) grants.",
                "amount": "Covered through host laboratory grants"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Local subway, bus, and high-speed rail transit between Shanghai/Nanjing and campus is paid from stipend.",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 14500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Nanjing University)",
            "participating_institutions": [
                "Nanjing University (NJU) - C9 League Institution (Jiangsu, China)"
            ],
            "university_rankings_scope": "QS World University Rankings #145, ARWU Shanghai Ranking #80 worldwide, Chinese C9 League elite university.",
            "available_majors": [
                "Computer Science and Technology",
                "Artificial Intelligence",
                "Software Engineering",
                "Electronic Science and Technology",
                "Physics and Condensed Matter Physics",
                "Chemistry and Chemical Biology",
                "Environmental Science and Engineering",
                "Earth Sciences and Geology",
                "Astronomy and Astrophysics",
                "International Economics and Trade",
                "Business Administration (MBA / Ph.D.)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 to 3 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Online NJU application, supervisor acceptance letter, notarized academic transcripts and degree certificates, two professor recommendation letters, detailed research proposal (800+ words for Master's, 1,500+ words for PhD), Foreigner Physical Examination Form, and clean police character certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing a pre-acceptance letter from faculty in the School of Computer Science or School of Artificial Intelligence is exceptionally competitive due to global demand; applicants with published papers in IEEE/ACM transactions or top conferences receive rapid supervisor endorsements.",
            "strategic_program_match_advice": "Contact prospective NJU supervisors between October and December. Send a concise cold email highlighting your publication record, GitHub repository, and an aligned 2-page research draft before submitting the formal CSC portal application."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://studyinchina.csc.edu.cn/ & http://istudy.nju.edu.cn",
            "portal_system_name": "CSC Online Application System (Agency No. 10284) & NJU International Student Portal",
            "account_creation_instructions": "Register on the CSC portal selecting 'Program Category Type B', input NJU Agency Number '10284'. Concurrently register on the NJU International Student Service System and upload matching documentation.",
            "step_by_step_workflow": [
                "Step 1: Explore NJU faculty profiles and reach out to prospective supervisors with CV and research abstract (October - December).",
                "Step 2: Secure the formal NJU 'Provisional Acceptance Letter for International Students' signed by the professor and school.",
                "Step 3: Complete CSC online registration under Type B (Agency No. 10284) and download the completed CSC application form.",
                "Step 4: Complete NJU International Student Portal application and upload all notarized academic credentials, physical exam, and police certificate.",
                "Step 5: Pay the NJU application fee (RMB 600) online via UnionPay, WeChat, or international credit card.",
                "Step 6: School-level academic committee reviews dossiers and conducts online technical interviews (February - March).",
                "Step 7: NJU nominates shortlisted candidates to the China Scholarship Council in Beijing for final approval (April - May).",
                "Step 8: Final CSC award list announced; official JW201 visa form and NJU admission notice dispatched (June - July).",
                "Step 9: Apply for Chinese X1 Student Visa at Chinese Visa Application Service Centre (Gerry's) in Pakistan and arrive in Nanjing in September."
            ],
            "university_vs_scholarship_routing": "Direct University Track (Type B): The university evaluates, interviews, and directly nominates candidates to CSC.",
            "recommendation_letters_submission_method": "Uploaded directly by applicant as signed PDF letters on institutional letterhead with recommender email and phone details.",
            "personal_statement_prompts": "Comprehensive Statement of Purpose / Research Proposal covering academic background, proposed research methodology, justification for choosing Nanjing University, and long-term professional aspirations (minimum 800 words for Master's; 1,500 words for PhD).",
            "study_plan_research_proposal_requirements": "Structured research proposal detailing problem statement, literature review, technical methodology, expected timeline, and alignment with prospective supervisor's research group.",
            "cv_format_requirements": "Academic CV detailing education history, published papers, academic awards, technical programming skillsets, and referee details.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview via Tencent Meeting (VooV) or Zoom conducted by NJU departmental faculty panel, evaluating technical depth, research feasibility, and English communication.",
            "standardized_tests": "None strictly required (GRE not mandatory); English proficiency test or MOI letter required.",
            "application_fee_amount": "RMB 600 (~USD 85; ~PKR 23,500)",
            "attestation_requirements": "Educational degrees and transcripts must be notarized by a licensed Notary Public in Pakistan and subsequently attested by HEC and MoFA for final registration.",
            "translation_requirements": "Official English or Chinese translations required for any non-English/non-Chinese certificates.",
            "final_submission_method": "100% digital submission via CSC and NJU online portals; physical hardcopies not required unless requested by specific faculty."
        },
        "required_documents_checklist": [
            {
                "document_name": "CSC Online Application Form (Type B)",
                "mandatory": True,
                "specification": "Downloaded from studyinchina.csc.edu.cn with Agency No. 10284, signed by applicant.",
                "pakistan_specific_instruction": "Ensure applicant details match Pakistani passport exactly."
            },
            {
                "document_name": "Nanjing University Provisional Acceptance Letter",
                "mandatory": True,
                "specification": "Official pre-acceptance form signed by an authorized NJU doctoral/master supervisor.",
                "pakistan_specific_instruction": "Crucial requirement; applications without professor endorsement rarely pass university screening."
            },
            {
                "document_name": "Notarized Degree Certificates and Transcripts",
                "mandatory": True,
                "specification": "Color scanned copies of notarized Bachelor's/Master's degrees and transcripts.",
                "pakistan_specific_instruction": "Must be notarized by notary public and verified by HEC Pakistan."
            },
            {
                "document_name": "Detailed Study Plan / Research Proposal",
                "mandatory": True,
                "specification": "Minimum 800 words for Master's; 1,500 words for PhD in English or Chinese.",
                "pakistan_specific_instruction": "Tailor directly to NJU laboratory projects; avoid generic templates."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Written by full Professors or Associate Professors on official university letterhead.",
                "pakistan_specific_instruction": "Must include official institutional email address and contact numbers of Pakistani professors."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Official Chinese physical examination form with all blood tests (HIV, Syphilis, Hepatitis), chest X-ray, and ECG stamped by hospital.",
                "pakistan_specific_instruction": "Must be completed at a recognized government hospital (e.g. Services Hospital, PIMS, or Shifa) within 6 months of submission."
            },
            {
                "document_name": "Non-Criminal Record Certificate (Police Character Certificate)",
                "mandatory": True,
                "specification": "Official certificate issued by local police authority confirming no criminal record, valid within 6 months.",
                "pakistan_specific_instruction": "Obtained from Police Khidmat Markaz across Pakistan and attested by MoFA."
            },
            {
                "document_name": "English Proficiency Certificate or Test Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 85), or official English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "MOI letter on university letterhead signed by Registrar / Controller of Examinations accepted."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear scanned copy of passport information page with validity extending at least 1 year beyond program start.",
                "pakistan_specific_instruction": "Pakistani passport must be valid until at least March 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "November 1",
            "application_deadline": "January 15",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "January 15",
            "recommendation_letters_deadline": "January 15",
            "interview_period": "February 15 - March 20",
            "shortlist_announcement": "April 15",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July 1 - August 15",
            "semester_commencement": "Early September",
            "annual_cycle_notes": "Annual single-intake cycle for Autumn semester (September enrollment). Faculty outreach is highly recommended from October."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Undergraduate/Master's GPA and university prestige)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular and social contributions)",
            "research_experience_weight": "35% (Research publications, supervisor fit, and proposal rigor)",
            "work_experience_weight": "5% (Industry/laboratory technical experience)",
            "personal_statement_weight": "10% (Study plan clarity and articulation of research goals)",
            "recommendations_weight": "5% (Strength and specificity of academic referee endorsements)",
            "interview_weight": "10% (Oral defense, technical aptitude, and English fluency)",
            "test_scores_weight": "0% (No GRE required; English meets threshold)",
            "financial_need_weight": "0% (Exclusively merit and research-potential based)",
            "selection_panel_composition": "NJU International Institute Admissions Board, Departmental Academic Committee, and China Scholarship Council Expert Panel.",
            "evaluation_methodology": "Two-tier selection: preliminary academic audit and supervisor endorsement at NJU departmental level, followed by CSC national review in Beijing."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 international applicants across all disciplines",
            "total_scholarships_awarded": "~120 to 160 CSC Type B scholarships awarded annually",
            "acceptance_rate_global": "~2.5% to 4.0%",
            "acceptance_rate_pakistan": "~5.0% among applicants possessing an official supervisor acceptance letter",
            "typical_successful_applicant_gpa": "3.50+ / 4.00 or 80%+ aggregate from leading Pakistani institutions (NUST, QAU, UET, FAST, LUMS, COMSATS)",
            "typical_academic_and_research_profile": "Strong theoretical foundation, at least 1-2 published papers or indexed conference proceedings, and an endorsed research plan aligned with NJU lab priorities.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani public and private engineering/science universities with tangible laboratory experience.",
            "high_representation_countries": "Pakistan, Russia, South Korea, Vietnam, Indonesia, Kazakhstan, France, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent educational agency websites claiming guaranteed CSC admission to Nanjing University for an upfront fee.",
                "Legitimate applications are processed ONLY through studyinchina.csc.edu.cn and istudy.nju.edu.cn."
            ],
            "application_fee_warning": "NJU charges an official non-refundable application fee of RMB 600; CSC application itself is completely free. Never pay agent processing fees.",
            "agent_and_intermediary_warnings": "Nanjing University does not collaborate with any commercial educational agencies for CSC scholarship distribution. Direct supervisor contact is essential.",
            "hidden_costs_breakdown": [
                "RMB 600 NJU application fee.",
                "Pakistani medical checkup and MoFA attestation expenses (~PKR 30,000 to 45,000).",
                "Round-trip airfare from Pakistan to Shanghai/Nanjing (~PKR 180,000 to 220,000).",
                "Initial 1-month living buffer before first stipend release (~RMB 2,500; ~PKR 100,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You cannot get CSC without knowing Chinese. Reality: NJU offers dozens of world-class graduate programs taught 100% in English.",
                "Myth: An acceptance letter guarantees the scholarship. Reality: Acceptance letters pass the departmental hurdle, but final CSC approval depends on institutional quota allocation."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest submitting physical hard copies to Nanjing; NJU transitioned to an entirely paperless online portal submission."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance (grade equivalent to 70%+ or passing all coursework) in accordance with NJU Graduate School regulations.",
            "attendance_requirements": "Strict attendance in lectures and active daily presence in research laboratories as directed by the principal investigator.",
            "academic_progress_monitoring": "Annual CSC Comprehensive Scholarship Review (April - May) evaluating coursework, research progress, and supervisor feedback; failure results in suspension or termination of stipend.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Chinese immigration laws without explicit university endorsement and work-study visa notation.",
            "home_country_return_obligation": "None enforced by CSC; graduates may pursue post-doctoral fellowships, industry employment in China under working visas, or international research careers.",
            "service_obligations_or_bonds": "No financial bond or service indenture required.",
            "repayment_clawback_conditions": "Stipend and tuition benefits terminated if scholar is expelled for disciplinary breaches, severe violation of Chinese law, or unapproved program abandonment.",
            "rules_for_changing_university": "Changing university while under CSC scholarship is strictly forbidden.",
            "rules_for_changing_major": "Major changes are generally not permitted unless approved under extraordinary circumstances by NJU Graduate School and CSC Beijing.",
            "extension_policy": "Scholarship extensions are extremely rare and generally require supervisor research funding coverage if PhD studies exceed the approved duration."
        },
        "official_sources_verified": [
            {
                "source_name": "Nanjing University Institute for International Students Official Portal",
                "source_url": "https://hwxy.nju.edu.cn/English/Scholarships/ChineseGovernmentScholarship/index.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "http://studyinchina.csc.edu.cn/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AS-049": {
        "scholarship_id": "SCH-AS-049",
        "basic_details": {
            "scholarship_name": "Beihang University Chinese Government & Postgrad Presidential Scholarship",
            "offering_entity": "Beihang University (BUAA) & China Scholarship Council (CSC)",
            "host_country": "China",
            "host_institutions_covered": "Beihang University (Xueyuan Road and Shahe Campuses, Beijing, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to STEM and management disciplines with premier global strength in Aerospace Engineering, Computer Science and Engineering, Software Engineering, Mechanical Engineering, Automation and Control Science, Electronic and Information Engineering, Materials Science, and Management Science.",
            "number_of_awards_total": "~100 to 150 CSC and Beihang University Postgrad Presidential Scholarships awarded annually",
            "number_of_awards_pakistan": "Substantial representation; Pakistan is a primary partner nation in aerospace and computing education (~20 to 30 scholars admitted annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 to 2.5 years for Master's; up to 3 to 4 years for PhD programs"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of a country other than the People's Republic of China (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Master's degree applicants must be under 35 years of age; PhD applicants must be under 40 years of age.",
            "academic_qualifications": "Recognized 4-year Bachelor's degree (16 years education) for Master's; Master's degree (18 years education) for PhD from an HEC-recognized university in a relevant engineering or science discipline with strong grades (minimum 75% aggregate or CGPA 3.20 / 4.00; competitive admits typically 3.50+ / 4.00).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum B / 3.0 scale grade record; top 20% class rank preferred.",
            "subject_background_prerequisites": "Undergraduate degree in Aerospace, Mechanical, Electrical, Computer Science, Automation, Mathematics, or Materials Engineering.",
            "current_education_status": "Final-year students can apply with an expected graduation certificate from their university.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Engineering design, research laboratory background, or published papers in Scopus/SCI journals strongly favored.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic min 6.0, TOEFL iBT min 80, or official English Medium of Instruction (MOI) certificate issued by an HEC-recognized university in Pakistan.",
            "other_language_requirements": "For Chinese-taught programs: HSK Level 5 (score 180+) or HSK Level 4 (score 210+) is required.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must obtain preliminary supervisory acceptance or endorsement from a Beihang University professor.",
            "previous_scholarship_restrictions": "Cannot hold concurrent awards from other Chinese governmental or institutional programs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition waiver for standard program duration (RMB 35,000 to 42,000 / year value).",
                "amount": "100% covered (~RMB 38,000 / year; ~PKR 1,482,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "Beihang University international application processing fee of RMB 400 (~USD 58; ~PKR 16,000).",
                "amount": "RMB 400 (~PKR 16,000)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free on-campus accommodation in the Beihang International Student Dormitory (Xueyuan Road Campus in Haidian District or Shahe Campus), or standard living accommodation subsidy.",
                "amount": "100% covered dormitory room"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Living stipend paid monthly: RMB 3,000 / month for Master's students (~USD 420; ~PKR 117,000 / month); RMB 3,500 / month for PhD students (~USD 490; ~PKR 136,500 / month).",
                "amount": "RMB 3,000 to 3,500 / month (~PKR 117,000 to 136,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses between Pakistan and Beijing are borne by the scholar.",
                "amount": "Not covered (Self-funded ~PKR 170,000 to 230,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese student X1 visa processing fees in Islamabad/Karachi paid by applicant.",
                "amount": "Not covered (~PKR 25,000 to 35,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive Medical Insurance for Foreign Students in China (RMB 800 / year value).",
                "amount": "100% covered (RMB 800 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Multi-floor campus dining halls (including dedicated Muslim Halal dining facilities on Xueyuan Road Campus) provide balanced meals for RMB 25 to 35/day.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Beihang University digital libraries, wind tunnels, engineering laboratories, and computational centers.",
                "amount": "Covered via institutional infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Research project consumables and academic conference participation covered through supervisor's national research projects (863/973/NSFC).",
                "amount": "Covered through laboratory research funding"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Beijing subway and municipal bus expenses paid out of monthly stipend.",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 14500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Beihang University)",
            "participating_institutions": [
                "Beihang University (BUAA) - National Double First-Class Institution (Beijing, China)"
            ],
            "university_rankings_scope": "US News Global Engineering #28 worldwide, Aerospace Engineering #1 globally (Shanghai Academic Ranking), QS World University Rankings #383.",
            "available_majors": [
                "Aeronautical and Astronautical Science and Technology",
                "Computer Science and Technology",
                "Software Engineering",
                "Control Science and Engineering",
                "Mechanical Engineering",
                "Electronic Science and Technology",
                "Materials Science and Engineering",
                "Power Engineering and Engineering Thermophysics",
                "Traffic and Transportation Engineering",
                "Management Science and Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 to 2.5 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Online application on Beihang International Student portal and CSC portal, supervisor acceptance letter, notarized academic credentials, study plan (1,000+ words), two professor recommendation letters, physical exam form, and police clearance certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Aerospace, UAV design, and Robotics research groups are world-renowned and receive intense competition; early contact with professors in the School of Aeronautic Science or Computer Science is paramount.",
            "strategic_program_match_advice": "Highlight hands-on hardware/software engineering skills (e.g., ROS, CFD simulations, embedded systems, PyTorch) in your initial supervisor outreach email."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://admission.buaa.edu.cn & http://studyinchina.csc.edu.cn/",
            "portal_system_name": "Beihang University International Student Service System & CSC Portal (Agency No. 10006)",
            "account_creation_instructions": "Register on Beihang portal (admission.buaa.edu.cn) and submit personal credentials. Complete CSC Type B application specifying Beihang Agency Number '10006'.",
            "step_by_step_workflow": [
                "Step 1: Identify potential research supervisors from Beihang academic school websites and send tailored email with CV and research interests (October - December).",
                "Step 2: Obtain the official Beihang Provisional Acceptance Letter signed by the supervisor.",
                "Step 3: Register and complete the online application on the Beihang International Student Portal.",
                "Step 4: Register on the CSC online application system under Category B, entering Agency No. 10006.",
                "Step 5: Pay the Beihang University application processing fee of RMB 400 online.",
                "Step 6: Departmental academic committee evaluates academic merit and conducts video interview via Zoom or Tencent Meeting (February - March).",
                "Step 7: Beihang International School submits nominated candidate list to the China Scholarship Council (April - May).",
                "Step 8: Final results published; official admission package (Admission Letter and JW201/JW202 form) sent to the student (July).",
                "Step 9: Apply for Chinese X1 Student Visa in Pakistan and prepare for arrival in Beijing in September."
            ],
            "university_vs_scholarship_routing": "Direct University Nomination Track (Type B): Nominated directly by Beihang University to the CSC.",
            "recommendation_letters_submission_method": "Uploaded as signed PDF documents on university letterhead with institutional email and telephone numbers.",
            "personal_statement_prompts": "Detailed Study Plan / Research Proposal covering academic background, research interests, experimental methodology, and career vision (minimum 1,000 words).",
            "study_plan_research_proposal_requirements": "Clear, technical proposal with specific objectives, engineering relevance, and timeline mapping directly to Beihang lab focus areas.",
            "cv_format_requirements": "Curriculum Vitae detailing education, technical proficiencies, research publications, and academic awards.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview conducted by a panel of 3-4 faculty members covering technical fundamentals, research proposal defense, and English proficiency.",
            "standardized_tests": "Not required; English proficiency certificate or MOI letter mandatory.",
            "application_fee_amount": "RMB 400 (~USD 58; ~PKR 16,000)",
            "attestation_requirements": "Degree certificates and transcripts must be notarized in Pakistan by a notary public; HEC and MoFA attestations needed for final enrollment.",
            "translation_requirements": "English or Chinese certified translations required for any non-English/non-Chinese records.",
            "final_submission_method": "Online digital submission on both Beihang and CSC systems."
        },
        "required_documents_checklist": [
            {
                "document_name": "CSC Application Form (Type B)",
                "mandatory": True,
                "specification": "Completed and signed form downloaded from CSC portal with Agency No. 10006.",
                "pakistan_specific_instruction": "Ensure name, passport number, and date of birth match Pakistani passport exactly."
            },
            {
                "document_name": "Beihang Provisional Acceptance Letter",
                "mandatory": True,
                "specification": "Official pre-admission supervision form signed by an authorized Beihang professor.",
                "pakistan_specific_instruction": "Vital document that dramatically raises selection probability."
            },
            {
                "document_name": "Notarized Highest Diploma and Academic Transcripts",
                "mandatory": True,
                "specification": "Scanned color copies of notarized Bachelor's/Master's degree and full transcripts.",
                "pakistan_specific_instruction": "Degrees must be from HEC-recognized Pakistani universities."
            },
            {
                "document_name": "Research Proposal / Study Plan",
                "mandatory": True,
                "specification": "Minimum 1,000 words in English or Chinese outlining research methodology and objectives.",
                "pakistan_specific_instruction": "Must demonstrate rigorous domain understanding and laboratory relevance."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Signed letters from Professors or Associate Professors on university letterhead.",
                "pakistan_specific_instruction": "Must contain official institutional email addresses of Pakistani referees."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Completed Chinese medical examination form with hospital stamp, physician signature, and lab reports.",
                "pakistan_specific_instruction": "Completed at a major government hospital in Pakistan within 6 months of submission."
            },
            {
                "document_name": "Certificate of Non-Criminal Record",
                "mandatory": True,
                "specification": "Official police clearance certificate confirming no criminal history, issued within 6 months.",
                "pakistan_specific_instruction": "Issued by Police Khidmat Markaz and attested by MoFA."
            },
            {
                "document_name": "English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or official English Medium of Instruction letter.",
                "pakistan_specific_instruction": "Institutional MOI certificate signed by university registrar accepted."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of ordinary passport information page valid for at least 1.5 years.",
                "pakistan_specific_instruction": "Must be valid through early 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 15",
            "application_deadline": "February 28",
            "university_admission_deadline": "February 28",
            "document_submission_deadline": "February 28",
            "recommendation_letters_deadline": "February 28",
            "interview_period": "March 15 - April 15",
            "shortlist_announcement": "May 15",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July 1 - August 15",
            "semester_commencement": "Early September",
            "annual_cycle_notes": "Single annual intake cycle for September enrollment. Applying before January 15 provides maximum faculty review consideration."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Undergraduate/Master's GPA and academic distinction)",
            "extracurricular_and_leadership_weight": "5% (Leadership, team projects, and community engagement)",
            "research_experience_weight": "35% (Prior publications, engineering competition awards, and research plan quality)",
            "work_experience_weight": "5% (Industry/laboratory engineering experience)",
            "personal_statement_weight": "10% (Study plan depth, clarity of objectives, and institutional match)",
            "recommendations_weight": "5% (Detailed appraisals from academic referees)",
            "interview_weight": "10% (Technical interview performance and English communication)",
            "test_scores_weight": "0% (No GRE required; English meets threshold)",
            "financial_need_weight": "0% (Exclusively merit-based selection)",
            "selection_panel_composition": "Beihang International School Admissions Board, Departmental Academic Review Committee, and CSC Expert Panel.",
            "evaluation_methodology": "Rigorous two-phase assessment: school-level academic screening followed by CSC national ratification."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,000 to 4,500 international applicants across all disciplines",
            "total_scholarships_awarded": "~100 to 150 full scholarships awarded annually",
            "acceptance_rate_global": "~3.0% to 4.5%",
            "acceptance_rate_pakistan": "~6.0% among candidates holding official faculty acceptance letters",
            "typical_successful_applicant_gpa": "3.50+ / 4.00 or 80%+ aggregate from premier Pakistani engineering institutions (NUST, GIKI, PIEAS, IST, UET)",
            "typical_academic_and_research_profile": "Graduates with solid engineering fundamentals, high-impact final year projects, and at least one Scopus-indexed research paper or conference presentation.",
            "common_backgrounds_of_winners": "Graduates of Pakistani aerospace, electrical, mechanical, and computer engineering universities.",
            "high_representation_countries": "Pakistan, Russia, Iran, Kazakhstan, Egypt, Thailand, Indonesia, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents advertising guaranteed CSC seats at Beihang University for hefty fees.",
                "All legitimate submissions take place exclusively via admission.buaa.edu.cn and studyinchina.csc.edu.cn."
            ],
            "application_fee_warning": "Beihang University charges an official RMB 400 application fee; the CSC system charges no additional fee. Never wire funds to individual bank accounts.",
            "agent_and_intermediary_warnings": "Beihang University does not authorize any commercial recruiting agents for CSC scholarships; applications must be initiated directly by the student.",
            "hidden_costs_breakdown": [
                "Beihang application fee: RMB 400.",
                "Medical checkup, police certificate, and MoFA attestation: ~PKR 30,000 to 40,000.",
                "One-way/round-trip flight from Pakistan to Beijing: ~PKR 170,000 to 230,000.",
                "Initial settling-in expenses before first stipend disbursement: ~RMB 2,500; ~PKR 100,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You cannot study aerospace in China without speaking Chinese. Reality: Beihang offers extensive graduate programs delivered completely in English.",
                "Myth: A professor's verbal email confirmation is equivalent to an acceptance letter. Reality: Only the signed, official Beihang Provisional Acceptance Form guarantees departmental nomination."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim paper documents must be couriered to Beijing; Beihang uses a paperless digital portal submission system."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a passing grade in all courses (minimum 70% or Grade B equivalent) and meet all milestone research requirements.",
            "attendance_requirements": "Mandatory classroom attendance and daily involvement in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual CSC Comprehensive Evaluation conducted every May; satisfactory progress is mandatory for continuation of monthly stipend and fee waiver.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Chinese visa regulations without formal university authorization.",
            "home_country_return_obligation": "No mandatory return requirement; graduates may pursue post-doctoral research, international employment, or industry roles in China under proper work permits.",
            "service_obligations_or_bonds": "No bond or return service agreement enforced.",
            "repayment_clawback_conditions": "Funding terminated immediately if the student is expelled for criminal offenses, university code violations, or unauthorized absence.",
            "rules_for_changing_university": "Transferring to another Chinese university under the CSC scholarship is strictly disallowed.",
            "rules_for_changing_major": "Major modifications are not permitted once admitted under the scholarship.",
            "extension_policy": "Scholarship extensions beyond the designated duration are rarely approved by CSC; students must fund remaining time via supervisor research assistantships."
        },
        "official_sources_verified": [
            {
                "source_name": "Beihang University International School Official Portal",
                "source_url": "https://is.buaa.edu.cn/en/scholarships/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "http://studyinchina.csc.edu.cn/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AS-066": {
        "scholarship_id": "SCH-AS-066",
        "basic_details": {
            "scholarship_name": "Seoul National University (SNU) Global Scholarship",
            "offering_entity": "Seoul National University (SNU) Office of International Affairs (OIA)",
            "host_country": "South Korea",
            "host_institutions_covered": "Seoul National University (Gwanak Main Campus and Yeongeon Medical Campus, Seoul, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & Doctoral Program"],
            "major_restrictions": "Open to all graduate colleges: College of Engineering, College of Natural Sciences, College of Agriculture and Life Sciences, Graduate School of Data Science, College of Pharmacy, College of Medicine, College of Social Sciences, and Graduate School of International Studies (GSIS).",
            "number_of_awards_total": "~160 to 200 graduate scholars supported per semester across Global Scholarship Category 1 (Tuition + Stipend) and Category 2 (Tuition Exemption)",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in STEM, computing, and life sciences secure ~10 to 18 awards per semester",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 1 year renewable (up to 2 years for Master's, 3 years for PhD) subject to maintaining a minimum semester GPA of 3.0 / 4.3"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents are not citizens of South Korea (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit, but competitive applicants are typically under 35 (Master's) or under 40 (PhD).",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) for Master's; recognized Master's degree (18 years education) for PhD from an HEC-recognized institution with distinguished academic performance (minimum 75% aggregate or CGPA 3.30 / 4.00; competitive admits typically 3.60+ / 4.00 or top 10% class rank).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Transcript grades evaluated on SNU 4.3 grading scale; applicants should hold an equivalent of B+ (3.3/4.3) or higher.",
            "subject_background_prerequisites": "Prior degree closely aligned with the applied academic discipline.",
            "current_education_status": "Students in their final semester can apply conditionally with a bonafide letter from their university stating expected graduation date.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research laboratory experience, coding proficiency, or published papers in international journals significantly enhance selection odds.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "TOEFL iBT min 80, IELTS Academic min 6.0, TEPS min 269, or official English Medium of Instruction (MOI) certificate from Pakistani university confirming undergraduate/master education was conducted in English.",
            "other_language_requirements": "Korean proficiency (TOPIK) is not required for English-track STEM programs; TOPIK Level 3+ recommended for Humanities and Social Sciences.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants can apply for the SNU Global Scholarship during the general international graduate admissions application window or upon admission.",
            "previous_scholarship_restrictions": "Cannot concurrently hold other full external government scholarships (e.g. GKS/KGSP).",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver for the enrolled academic semester/year (KRW 3,200,000 to 6,100,000 / semester value depending on college).",
                "amount": "100% covered (~KRW 6,400,000 to 12,200,000 / year; ~PKR 1,344,000 to 2,562,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "SNU international graduate admissions application fee of KRW 90,000 (~USD 68; ~PKR 18,900) paid online via UwayApply.",
                "amount": "KRW 90,000 (~PKR 18,900)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "SNU Gwanak Residence Halls (Bldg 900-906) provided at highly subsidized student rates: KRW 200,000 to 350,000 / month (~USD 150 to 260 / month) for double/single rooms, easily covered from the monthly stipend.",
                "amount": "Subsidized dormitory (~KRW 250,000 / month)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Global Scholarship Category 1 recipients receive a tax-free monthly living stipend of KRW 1,200,000 / month (~USD 900 / month; ~PKR 252,000 / month) for 12 months. Supplementary laboratory research assistantship (RA) stipends typically add KRW 600,000 to 1,000,000 / month.",
                "amount": "KRW 1,200,000 / month (~PKR 252,000 / mo)"
            },
            "airfare": {
                "status": "PARTIAL",
                "details": "Selected Global Scholarship 1 awardees receive a one-time economy round-trip or one-way flight subsidy (up to KRW 1,000,000; ~USD 750).",
                "amount": "Up to KRW 1,000,000 airfare subsidy"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Korean D-2 Student Visa processing fees at the Embassy of the Republic of Korea in Islamabad are paid by the student.",
                "amount": "Not covered (~PKR 16,000 to 25,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory Korean National Health Insurance Service (NHIS) covers foreign students; subsidized monthly premium is ~KRW 70,000 / month, covered from the monthly living stipend.",
                "amount": "Subsidized NHIS (~KRW 70,000 / month)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "SNU campus cafeterias (Student Center cafeteria, Dormitory cafeteria, and Halal-friendly meal options) provide wholesome meals for KRW 3,500 to 6,000 per meal; easily covered by the KRW 1,200,000 monthly stipend.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Comprehensive access to SNU Main Library, digital archives, supercomputing facilities, and advanced laboratory equipment.",
                "amount": "Covered via institutional infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory BK21 (Brain Korea 21 Four) funding and National Research Foundation of Korea (NRF) grants provide travel funding for international conferences.",
                "amount": "Covered through lab BK21/NRF grants"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Seoul Metropolitan subway and bus transit (T-Money card) paid from monthly stipend (~KRW 60,000/month).",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 18500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Seoul National University)",
            "participating_institutions": [
                "Seoul National University (SNU) - SKY University flagship (Seoul, South Korea)"
            ],
            "university_rankings_scope": "QS World University Rankings #31 worldwide, Times Higher Education #62 globally, #1 in South Korea.",
            "available_majors": [
                "Computer Science and Engineering",
                "Electrical and Computer Engineering",
                "Data Science",
                "Mechanical Engineering",
                "Chemical and Biological Engineering",
                "Materials Science and Engineering",
                "Artificial Intelligence",
                "Physics and Astronomy",
                "Chemistry",
                "Biological Sciences",
                "Agricultural Biotechnology",
                "International Studies (GSIS)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years; Combined MS-PhD: 4 to 5 years",
            "admission_requirements_summary": "Online application via UwayApply, personal statement and study plan, two letters of recommendation, verified degree certificates and transcripts, language proficiency report (IELTS/TOEFL/MOI), passport copies of applicant and parents, and proof of family relations.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Admission to the Department of Computer Science and Engineering and Graduate School of Data Science is exceptionally competitive; having a prospective lab professor's preliminary support or joint research discussion dramatically improves funding prospects.",
            "strategic_program_match_advice": "Review SNU faculty laboratory websites, read their recent publications in IEEE/Nature/ACM, and email the professor 1-2 months before the application cycle opens with your CV, transcript, and a concise summary of your research interest."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://en.snu.ac.kr/admission/graduate/application & https://www.uwayapply.com",
            "portal_system_name": "SNU Graduate Admissions Portal & UwayApply",
            "account_creation_instructions": "Create an applicant account on UwayApply during the open application window, select Seoul National University Graduate International Admissions (Track 1), complete data entry, and check the scholarship application box for the SNU Global Scholarship.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective SNU professors to discuss lab openings and research alignment (June - July for Spring, December - January for Fall).",
                "Step 2: Create account on UwayApply and complete the SNU International Graduate Admissions form.",
                "Step 3: Indicate interest and complete the application section for the SNU Global Scholarship.",
                "Step 4: Pay the application fee of KRW 90,000 online via international credit card.",
                "Step 5: Have academic recommenders submit online recommendation letters directly through the automated email system.",
                "Step 6: Upload or courier certified documents (transcripts, degrees, apostille/consular confirmation, family relations proof).",
                "Step 7: Departmental admissions committee reviews applications and conducts technical interviews via Zoom (September for Spring, April for Fall).",
                "Step 8: Final admission and Global Scholarship results announced by SNU OIA (November for Spring, June for Fall).",
                "Step 9: Receive Certificate of Admission (CoA), apply for Korean D-2 visa in Islamabad, and matriculate at SNU."
            ],
            "university_vs_scholarship_routing": "Integrated Application: Scholarship consideration is embedded directly within the SNU general graduate admissions process.",
            "recommendation_letters_submission_method": "Submitted online by referees via the secure SNU recommendation portal link generated upon application fee payment.",
            "personal_statement_prompts": "Self-Introduction and Study Plan covering personal background, motivations for studying at SNU, undergraduate research achievements, and proposed graduate research project.",
            "study_plan_research_proposal_requirements": "Structured plan detailing research problem, methodologies, expected academic contributions, and alignment with target SNU laboratory.",
            "cv_format_requirements": "Standard academic CV highlighting academic honors, research papers, software projects, and technical skills.",
            "interviews_conducted": True,
            "interview_format_details": "Online video interview via Zoom conducted by a 2-3 faculty member committee assessing domain knowledge, mathematical/analytical skills, and research drive.",
            "standardized_tests": "Not required; GRE is optional but strongly recommended for competitive STEM applicants.",
            "application_fee_amount": "KRW 90,000 (~USD 68; ~PKR 18,900)",
            "attestation_requirements": "Degrees and transcripts must be authenticated by HEC Pakistan, MoFA, and consular legalized by the Embassy of the Republic of Korea in Islamabad, or apostilled.",
            "translation_requirements": "Certified English translation required for all non-English documents.",
            "final_submission_method": "Online application via UwayApply followed by submission of verified hardcopy credentials as instructed by the admissions office."
        },
        "required_documents_checklist": [
            {
                "document_name": "SNU Graduate Admissions & Scholarship Application Form",
                "mandatory": True,
                "specification": "Completed online application form via UwayApply.",
                "pakistan_specific_instruction": "Ensure name matches Pakistani passport exactly."
            },
            {
                "document_name": "Statement of Purpose and Study Plan",
                "mandatory": True,
                "specification": "Official SNU Form 2 detailing personal history and research objectives in English.",
                "pakistan_specific_instruction": "Articulate clear research synergy with specific SNU faculty labs."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Official SNU Form 3 completed online by academic mentors from previous university.",
                "pakistan_specific_instruction": "Ensure Pakistani professors use their official university email addresses."
            },
            {
                "document_name": "Official Bachelor's/Master's Degree and Transcripts",
                "mandatory": True,
                "specification": "HEC-attested degrees and complete transcripts with consular legalization / apostille.",
                "pakistan_specific_instruction": "Must be verified by HEC, MoFA, and legalized by the Korean Embassy in Islamabad."
            },
            {
                "document_name": "Proof of Language Proficiency",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 80), TEPS (min 269), or English MOI certificate.",
                "pakistan_specific_instruction": "Institutional MOI certificate signed by Registrar/Dean is accepted by many STEM departments."
            },
            {
                "document_name": "Proof of Nationality and Family Relations",
                "mandatory": True,
                "specification": "Scanned passport copies of applicant and parents, along with Family Registration Certificate (FRC).",
                "pakistan_specific_instruction": "NADRA Family Registration Certificate (FRC) in English translated and attested by MoFA."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of applicant's passport valid for at least 1 year.",
                "pakistan_specific_instruction": "Must have at least 18 months remaining validity."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Early July (Spring Intake) / Early January (Fall Intake)",
            "application_deadline": "Mid-July (Spring Intake) / Early February (Fall Intake)",
            "university_admission_deadline": "Mid-July / Early February",
            "document_submission_deadline": "Late July / Mid-February",
            "recommendation_letters_deadline": "Late July / Mid-February",
            "interview_period": "September (Spring) / April (Fall)",
            "shortlist_announcement": "Late November (Spring) / Early June (Fall)",
            "final_result_acceptance_deadline": "Mid-December / Late June",
            "visa_application_window": "January (Spring) / July (Fall)",
            "semester_commencement": "March 1 (Spring) / September 1 (Fall)",
            "annual_cycle_notes": "Two application intake cycles per academic year: Spring semester (starts March) and Fall semester (starts September)."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA and academic excellence)",
            "extracurricular_and_leadership_weight": "5% (Leadership activities and awards)",
            "research_experience_weight": "35% (Prior research, publications, and study plan alignment)",
            "work_experience_weight": "5% (Industry/laboratory engineering experience)",
            "personal_statement_weight": "10% (Clarity of purpose and articulation of goals)",
            "recommendations_weight": "5% (Academic referee evaluations)",
            "interview_weight": "5% (Video interview assessment where conducted)",
            "test_scores_weight": "0% (English meets required standard; GRE optional)",
            "financial_need_weight": "0% (Purely merit-based for Global Scholarship 1)",
            "selection_panel_composition": "SNU Departmental Admissions Committee, Graduate School Academic Board, and Office of International Affairs (OIA) Scholarship Panel.",
            "evaluation_methodology": "Comprehensive holistic review evaluating academic rigor, research potential, faculty fit, and international diversity."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 to 5,500 international applicants across both semesters",
            "total_scholarships_awarded": "~300 to 400 Global Scholarships awarded annually across both semesters",
            "acceptance_rate_global": "~6.0% to 8.0%",
            "acceptance_rate_pakistan": "~8.0% among competitive STEM applicants with supervisor backing",
            "typical_successful_applicant_gpa": "3.60+ / 4.00 or 85%+ aggregate from top Pakistani universities (NUST, FAST, QAU, GIKI, UET, LUMS)",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, solid coding/lab skills, and at least 1-2 research publications or significant thesis project outcomes.",
            "common_backgrounds_of_winners": "Graduates of Pakistani premier science and engineering universities.",
            "high_representation_countries": "Pakistan, Vietnam, India, Indonesia, China, Turkey, USA, Germany.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent websites offering admission guarantees or unofficial scholarship letters for Seoul National University.",
                "Legitimate applications are processed ONLY through en.snu.ac.kr and uwayapply.com."
            ],
            "application_fee_warning": "SNU application fee is KRW 90,000 paid exclusively via UwayApply; no other agency fees are authorized.",
            "agent_and_intermediary_warnings": "SNU does not work with third-party recruitment agencies; direct application is mandatory.",
            "hidden_costs_breakdown": [
                "Application fee: KRW 90,000 (~PKR 18,900).",
                "NADRA FRC, HEC attestation, MoFA attestation, and Korean Embassy legalization: ~PKR 40,000 to 55,000.",
                "Mandatory Korean NHIS health insurance (~KRW 70,000/month) paid from stipend.",
                "Round-trip airfare from Pakistan to Incheon/Seoul (~PKR 190,000 to 250,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You cannot study at SNU without speaking Korean. Reality: Nearly all graduate STEM courses and laboratory research are conducted entirely in English.",
                "Myth: The scholarship covers all 4 years automatically. Reality: The award is renewed semester-by-semester based on maintaining a minimum GPA of 3.0 / 4.3."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums state that professor contact is not required; in practice, STEM applicants without prior professor contact rarely get allocated lab space or scholarship funding."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum semester GPA of 3.0 / 4.3 (Grade B equivalent) to retain the scholarship for subsequent semesters.",
            "attendance_requirements": "Full-time academic standing and active daily laboratory research engagement.",
            "academic_progress_monitoring": "Semester-end academic record review by the Office of International Affairs (OIA) before releasing subsequent tuition waivers and stipends.",
            "work_restrictions_during_study": "Part-time work permitted up to 20 hours/week during semester with university and immigration permission, but full-time external employment is prohibited.",
            "home_country_return_obligation": "No obligation to return to Pakistan; graduates can transition to Korean D-10 job seeker visas or E-7 professional work visas.",
            "service_obligations_or_bonds": "No bond or mandatory service agreement.",
            "repayment_clawback_conditions": "Scholarship cancelled if the student is subject to disciplinary action, withdraws without authorization, or fails to meet minimum GPA standards.",
            "rules_for_changing_university": "Transferring to another university results in immediate loss of SNU scholarship benefits.",
            "rules_for_changing_major": "Changing majors requires formal review and typically results in loss of the Global Scholarship funding.",
            "extension_policy": "Global Scholarship duration is strictly capped at standard program length (up to 4 semesters for Master's, 6-8 for PhD); subsequent extensions must be funded via lab RA/TA funds."
        },
        "official_sources_verified": [
            {
                "source_name": "Seoul National University Office of International Affairs (OIA) Official Portal",
                "source_url": "https://en.snu.ac.kr/admission/graduate/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "SNU Graduate Admissions Guide",
                "source_url": "https://en.snu.ac.kr/admission/graduate/application",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AS-072": {
        "scholarship_id": "SCH-AS-072",
        "basic_details": {
            "scholarship_name": "Nanyang Technological University (NTU) Nanyang President's Graduate Scholarship (NPGS)",
            "offering_entity": "Nanyang Technological University (NTU Singapore)",
            "host_country": "Singapore",
            "host_institutions_covered": "Nanyang Technological University (Jurong West Campus and Novena Campus, Singapore)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all doctoral research programs across College of Engineering (CCEB, CEE, EEE, MSE, MAE, SCSE), College of Science (SBS, SPMS, ASE), Nanyang Business School, and College of Humanities, Arts, and Social Sciences.",
            "number_of_awards_total": "~30 to 45 highly prestigious NPGS awards globally per academic year",
            "number_of_awards_pakistan": "Open international competition; Pakistani PhD scholars with stellar academic records and top-tier publications secure ~2 to 5 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years of doctoral research, subject to satisfactory annual research progress and passing the PhD qualifying examination"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to outstanding scholars of all nationalities (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated purely on academic and research brilliance.",
            "academic_qualifications": "First Class Honours degree or equivalent outstanding academic record (minimum CGPA 3.70 / 4.00 or 85%+ aggregate) in an appropriate undergraduate or research master's degree from a recognized institution.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Applicants must demonstrate graduating in the top 5% of their class.",
            "subject_background_prerequisites": "Relevant Bachelor's or Master's degree in engineering, physical sciences, computing, biological sciences, or quantitative social sciences.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with certified interim transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Substantial research experience, first-author journal publications (IEEE, Nature, ACM, Springer), or notable conference papers strongly emphasized.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Official English proficiency test report mandatory: TOEFL iBT minimum 100 or IELTS Academic minimum 6.5. GRE score is required for applicants from non-Singaporean institutions (minimum GRE Verbal + Quantitative score of 319, Analytical Writing 3.5), or GATE (score 90%+ percentile for engineering).",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply for NPGS concurrently through the NTU PhD Graduate Admission portal.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent scholarship, fellowship, or paid employment without NTU approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver for up to 4 years of doctoral study (SGD 22,000 to 39,000 / year value depending on discipline).",
                "amount": "100% covered (~SGD 30,000 / year; ~PKR 6,300,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "NTU graduate research application fee of SGD 54.50 (~USD 41; ~PKR 11,500) per program choice paid online.",
                "amount": "SGD 54.50 (~PKR 11,500)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Priority on-campus graduate housing at NTU Graduate Halls (Hall 1, Hall 2, North Hill) for initial year: SGD 350 to 650 / month (~USD 260 to 480 / month), comfortably paid out of the substantial monthly stipend.",
                "amount": "Paid from stipend (~SGD 450 / month; ~PKR 94,500 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Premium monthly tax-free living stipend: SGD 3,200 to SGD 3,500 / month prior to passing PhD Qualifying Examination (QE); increased to SGD 3,700 / month (~USD 2,750 / month; ~PKR 777,000 / month) upon successful confirmation/passing of QE.",
                "amount": "SGD 3,200 to 3,700 / month (~PKR 672,000 to 777,000 / mo)"
            },
            "airfare": {
                "status": "PARTIAL",
                "details": "One-time settling-in and travel allowance included as part of the initial onboarding grant package.",
                "amount": "Covered under onboarding allowances"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Singapore Student's Pass application and issuance fees (ICA) covered or reimbursed by university.",
                "amount": "100% covered"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive NTU Medical Insurance Scheme for Graduate Students covering hospitalization, outpatient, and personal accident.",
                "amount": "100% covered by NTU"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Over 20 dining food courts across NTU campus (including diverse Halal-certified options, North Indian, and Malay food stalls) provide meals for SGD 4 to 8 per meal; easily covered by the SGD 3,500/month stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Annual book and materials allowance of SGD 500 / year plus a one-time IT allowance of SGD 1,500 for laptop/hardware procurement.",
                "amount": "SGD 500 / year + SGD 1,500 IT allowance"
            },
            "research_funding_conference_grant": {
                "status": "100% COVERED",
                "details": "Generous dedicated annual conference grant of up to SGD 4,000 / year (~USD 3,000 / year) to present peer-reviewed papers at leading international conferences globally.",
                "amount": "SGD 4,000 / year (~PKR 840,000 / year)"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Campus shuttle buses (Red, Blue, Green lines) are free; MRT and bus transit across Singapore paid out of stipend (~SGD 100/month).",
                "amount": "Free on-campus shuttles; MRT from stipend"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Nanyang Technological University)",
            "participating_institutions": [
                "Nanyang Technological University (NTU Singapore) - Main Campus (Jurong West, Singapore)"
            ],
            "university_rankings_scope": "QS World University Rankings #15 worldwide, Times Higher Education #32 globally; #1 worldwide in Materials Science and Artificial Intelligence citations.",
            "available_majors": [
                "Computer Science and Engineering (SCSE)",
                "Electrical and Electronic Engineering (EEE)",
                "Mechanical and Aerospace Engineering (MAE)",
                "Chemical and Biomedical Engineering (CCEB)",
                "Materials Science and Engineering (MSE)",
                "Civil and Environmental Engineering (CEE)",
                "Physical and Mathematical Sciences (SPMS)",
                "Biological Sciences (SBS)",
                "Asian School of the Environment (ASE)",
                "Nanyang Business School (PhD in Business/Finance)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (full-time PhD)",
            "admission_requirements_summary": "Online NTU application form, research proposal, academic transcripts, degree certificates, GRE and TOEFL/IELTS test score reports, two academic referee reports, CV, and sample publications/writing samples.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "NPGS is NTU's most selective flagship doctoral award; engineering and computer science receive extraordinary numbers of top applicants globally; having an engaged prospective NTU professor endorsing your proposal is decisive.",
            "strategic_program_match_advice": "Thoroughly review prospective advisors' current research grants and recent publications. Formulate a 2-to-3 page research draft that aligns directly with their laboratory objectives before submitting your official application."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://venus.wis.ntu.edu.sg/GOAP/online/ & https://www.ntu.edu.sg/admissions/graduate/financial-matters/scholarships/npgs",
            "portal_system_name": "NTU Graduate Online Application Portal (GOAP)",
            "account_creation_instructions": "Register an applicant profile on NTU GOAP, select PhD by Research, choose the target academic school, and tick the box for 'Nanyang President's Graduate Scholarship (NPGS)'.",
            "step_by_step_workflow": [
                "Step 1: Contact potential faculty supervisors at NTU with your academic CV and research proposal summary (August - October).",
                "Step 2: Take GRE (min 319 V+Q) and TOEFL (min 100) or IELTS (min 6.5) and request official ETS/IELTS score reporting to NTU.",
                "Step 3: Register on NTU GOAP, complete personal and educational history, and nominate two academic referees.",
                "Step 4: Upload soft copies of transcripts, degree certificates, CV, research proposal, and passport.",
                "Step 5: Pay the application fee of SGD 54.50 online via Visa/MasterCard.",
                "Step 6: Referees submit appraisal reports through the online referee portal link sent automatically by NTU.",
                "Step 7: School Shortlisting Committee and University Scholarship Selection Board review files and invite candidates for rigorous interviews (December - February).",
                "Step 8: Final NPGS offer letters issued to selected awardees (March - April).",
                "Step 9: Accept the fellowship offer, apply for Singapore Student's Pass via SOLAR system, and matriculate in August."
            ],
            "university_vs_scholarship_routing": "Integrated Application: Scholarship application is submitted directly through the NTU PhD graduate admission application form.",
            "recommendation_letters_submission_method": "Submitted online by academic referees via the automated NTU online recommendation system.",
            "personal_statement_prompts": "Statement of purpose outlining research motivations, academic trajectory, long-term scientific objectives, and alignment with NTU's research vision.",
            "study_plan_research_proposal_requirements": "Rigorous 3 to 5-page doctoral research proposal detailing research hypothesis, theoretical framework, methodology, experimental design, and preliminary bibliography.",
            "cv_format_requirements": "Detailed academic curriculum vitae with comprehensive publication citations (including DOI and impact factor), awards, and technical competencies.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous 30 to 45-minute video interview conducted by an elite panel of NTU school chairs and university professors evaluating scientific rigor, intellectual independence, and leadership potential.",
            "standardized_tests": "GRE mandatory for international graduates (min Verbal + Quantitative 319, Analytical Writing 3.5); TOEFL (min 100) or IELTS (min 6.5) mandatory.",
            "application_fee_amount": "SGD 54.50 (~USD 41; ~PKR 11,500)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and verified by the issuing universities; official English transcripts required.",
            "translation_requirements": "Certified English translations required for all non-English credentials.",
            "final_submission_method": "Online submission via NTU GOAP portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "NTU GOAP Application Form",
                "mandatory": True,
                "specification": "Completed online PhD application form specifying NPGS consideration.",
                "pakistan_specific_instruction": "Ensure name, passport number, and date of birth match Pakistani passport exactly."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's and Master's degree certificates and semester-by-semester transcripts.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan with grading scale / percentage explanation."
            },
            {
                "document_name": "Doctoral Research Proposal",
                "mandatory": True,
                "specification": "Detailed 3-5 page research proposal outlining research question, literature review, and methodology.",
                "pakistan_specific_instruction": "Ensure high academic rigor; alignment with NTU faculty lab priorities is essential."
            },
            {
                "document_name": "Official GRE Score Report",
                "mandatory": True,
                "specification": "Official ETS GRE score report with Verbal + Quantitative >= 319 and Analytical Writing >= 3.5.",
                "pakistan_specific_instruction": "Send official scores to NTU institution code 0129."
            },
            {
                "document_name": "Official TOEFL / IELTS Score Report",
                "mandatory": True,
                "specification": "TOEFL iBT (min 100) or IELTS Academic (min 6.5).",
                "pakistan_specific_instruction": "Send official test scores to NTU institution code 0129."
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by university professors through NTU's online appraisal portal.",
                "pakistan_specific_instruction": "Must be from Pakistani or international professors who supervised applicant's research."
            },
            {
                "document_name": "Academic CV and Research Publications",
                "mandatory": True,
                "specification": "Curriculum vitae including copies of published journal/conference papers.",
                "pakistan_specific_instruction": "Highlight papers indexed in IEEE, Scopus, or Web of Science."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1 (August Intake) / June 1 (January Intake)",
            "application_deadline": "November 30 (August Intake) / July 31 (January Intake)",
            "university_admission_deadline": "November 30 / July 31",
            "document_submission_deadline": "November 30 / July 31",
            "recommendation_letters_deadline": "December 7 / August 7",
            "interview_period": "January - February (August Intake) / August - September (January Intake)",
            "shortlist_announcement": "March - April (August Intake) / October (January Intake)",
            "final_result_acceptance_deadline": "Mid-May / Mid-November",
            "visa_application_window": "May - June / November - December",
            "semester_commencement": "August (Primary Intake) / January (Secondary Intake)",
            "annual_cycle_notes": "Main annual intake is in August (applications close November 30). Limited intake in January."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Undergraduate/Master's GPA, First Class Honours, university standing)",
            "extracurricular_and_leadership_weight": "5% (Leadership and community initiatives)",
            "research_experience_weight": "35% (Top-tier peer-reviewed publications, research proposal originality, and supervisor support)",
            "work_experience_weight": "5% (Relevant industry/R&D laboratory experience)",
            "personal_statement_weight": "5% (Scientific vision and intellectual ambition)",
            "recommendations_weight": "5% (Distinguished referee assessments)",
            "interview_weight": "10% (Panel interview performance and defense of research proposal)",
            "test_scores_weight": "5% (Exceptional GRE and English test scores)",
            "financial_need_weight": "0% (Exclusively merit and research-excellence based)",
            "selection_panel_composition": "NTU School Graduate Committee, College Chairs, and University Fellowship Selection Committee chaired by the Associate Provost.",
            "evaluation_methodology": "Two-tiered ultra-competitive merit review focusing on peer-reviewed research outputs, supervisor sponsorship, and interview defense."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 elite global applicants specifically contending for NPGS",
            "total_scholarships_awarded": "~30 to 45 fellowships awarded university-wide annually",
            "acceptance_rate_global": "~1.0% to 1.5%",
            "acceptance_rate_pakistan": "~2.0% to 3.0% among applicants possessing high GRE scores and published papers",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 or top 2% class rank with First Class Honours from leading Pakistani institutions (NUST, GIKI, PIEAS, FAST, LUMS)",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, GRE 320+, and multiple first-author papers in high-impact journals or top-tier IEEE/ACM conferences.",
            "common_backgrounds_of_winners": "Top graduates of leading engineering and science universities worldwide.",
            "high_representation_countries": "Singapore, China, India, Pakistan, Vietnam, Germany, USA, UK.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unsolicited emails offering guaranteed admission or scholarships to NTU Singapore.",
                "Legitimate applications are processed ONLY through ntu.edu.sg and venus.wis.ntu.edu.sg."
            ],
            "application_fee_warning": "NTU charges an official non-refundable application fee of SGD 54.50 paid securely via GOAP portal.",
            "agent_and_intermediary_warnings": "NTU does not engage commercial agencies for doctoral scholarship selections; all applications must be directly submitted by the applicant.",
            "hidden_costs_breakdown": [
                "Application fee: SGD 54.50 (~PKR 11,500).",
                "GRE examination fee: ~USD 220 (~PKR 62,000) and TOEFL/IELTS fee: ~PKR 60,000.",
                "Singapore Student's Pass processing and issuance fees: ~SGD 90 (~PKR 19,000).",
                "Round-trip airfare from Pakistan to Singapore Changi: ~PKR 160,000 to 220,000."
            ],
            "misleading_claims_debunked": [
                "Myth: GRE is optional for international applicants. Reality: Non-graduates of Singapore autonomous universities MUST submit official GRE scores.",
                "Myth: An NTU professor can directly award the NPGS. Reality: Professors can nominate, but final award decisions are made by the University Fellowship Selection Committee."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums claim GRE waivers are easy to obtain; for NPGS, GRE is strictly required and non-negotiable for foreign degree holders."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.50 / 5.00 throughout doctoral candidature and pass the PhD Qualifying Examination (QE) within 18 months.",
            "attendance_requirements": "Full-time campus research commitment; active participation in lab seminars, departmental colloquia, and teaching assistantships (TA) as required.",
            "academic_progress_monitoring": "Semi-annual progress reporting and annual review by the doctoral supervisory committee; unsatisfactory progress leads to fellowship termination.",
            "work_restrictions_during_study": "Scholars may not engage in external paid employment or commercial consulting during the scholarship period without explicit approval.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are free to pursue post-doctoral fellowships, academia, or high-tech industry careers in Singapore or globally.",
            "service_obligations_or_bonds": "No bond attached to the NPGS scholarship (unlike the Singapore MOE Tuition Grant for undergraduates/masters).",
            "repayment_clawback_conditions": "Fellowship terminated if student withdraws without justification or is dismissed for disciplinary misconduct or academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Major/school changes require approval by both academic school chairs and the Associate Provost.",
            "extension_policy": "NPGS funding terminates strictly after 4 years (48 months); any thesis completion beyond year 4 must be funded through laboratory project funds."
        },
        "official_sources_verified": [
            {
                "source_name": "Nanyang Technological University (NTU) NPGS Official Portal",
                "source_url": "https://www.ntu.edu.sg/admissions/graduate/financial-matters/scholarships/npgs",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "NTU Graduate Research Admissions Portal",
                "source_url": "https://venus.wis.ntu.edu.sg/GOAP/online/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
