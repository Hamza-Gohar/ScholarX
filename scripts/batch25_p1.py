# scripts/batch25_p1.py
# SCH-AS-050: Sun Yat-sen University (SYSU) Chinese Government Scholarship (China)
# SCH-AS-051: Hiroshima University Advanced Science & Engineering MEXT Award (Japan)
# SCH-AS-052: Sejong University International Graduate Scholarship (South Korea)

DATA_P1 = {
    "SCH-AS-050": {
        "scholarship_id": "SCH-AS-050",
        "basic_details": {
            "scholarship_name": "Sun Yat-sen University (SYSU) Chinese Government Scholarship (High-Level Postgraduate Program Type B)",
            "offering_entity": "China Scholarship Council (CSC) & Sun Yat-sen University (SYSU)",
            "host_country": "China",
            "host_institutions_covered": "Sun Yat-sen University Campuses (Guangzhou, Zhuhai, and Shenzhen Campuses, Guangdong Province, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computer Science and Engineering (Guangzhou/Shenzhen), School of Artificial Intelligence, School of Electronics and Communication Engineering, School of Biomedical Engineering, School of Marine Sciences, and School of Mathematics.",
            "number_of_awards_total": "~120 to 180 fully funded CSC Type B postgraduate scholarships allocated annually across colleges",
            "number_of_awards_pakistan": "Very generous bilateral allocation under China-Pakistan higher education partnerships; Pakistani scholars represent a leading international contingent at SYSU (~25 to 40 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 to 3 years for Master's; 3 to 4 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "CNY 3,000 / month for Master's (~PKR 117,000 / month); CNY 3,500 / month for PhD (~PKR 136,500 / month) plus free university dormitory housing and comprehensive medical insurance"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens holding valid foreign passports (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Master's applicants must be under 35 years of age; PhD applicants must be under 40 years of age per CSC statutory regulations.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum 80% marks (or CGPA 3.20+ / 4.00) for Master's; recognized 18-year Master's degree with minimum 80% marks (or CGPA 3.20+ / 4.00) for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum 80% aggregate (or CGPA 3.2 / 4.0); competitive applicants typically hold CGPA >= 3.5 / 4.0.",
            "subject_background_prerequisites": "Computer science, software engineering, artificial intelligence, communications, or related STEM discipline.",
            "current_education_status": "Graduated or final-year students graduating before July of application year.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in IEEE, ACM, or SCI/Scopus journals strongly advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": True,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 90, Duolingo 120+, or English Medium of Instruction (MOI) certificate accepted for English-taught graduate programs.",
            "other_language_requirements": "HSK Level 4 or 5 required only for Chinese-taught degree majors.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply through both the CSC portal (Agency No. 10558) and the SYSU International Student Application System.",
            "previous_scholarship_restrictions": "Cannot hold another concurrent Chinese government, provincial, or university award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for the complete official duration of the graduate degree program at SYSU.",
                "amount": "100% covered (~CNY 30,000 to 45,000 / year value; ~PKR 1,170,000 to 1,755,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "SYSU international application fee of CNY 400 (approx. USD 58 / ~PKR 16,000) paid online via university portal.",
                "amount": "CNY 400 (~PKR 16,000) application fee"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free on-campus international student dormitory accommodation (single room for PhD, twin room for Master's) on Guangzhou or Shenzhen campuses.",
                "amount": "100% covered free university housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend disbursed directly to student bank accounts: CNY 3,000 / month for Master's (~PKR 117,000 / month); CNY 3,500 / month for PhD (~PKR 136,500 / month).",
                "amount": "CNY 3,000 to 3,500 / month (~PKR 117,000 to 136,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International relocation flights to Guangzhou/Shenzhen are self-funded by the student.",
                "amount": "Not covered in CSC Type B"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 Student Visa application fee (~PKR 15,000 to 22,000) paid directly to Chinese Visa Application Service Center in Pakistan.",
                "amount": "Approx. PKR 18,000 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Medical Insurance for Foreign Students in China (Ping An Insurance, CNY 800/year value) 100% covered by CSC.",
                "amount": "100% covered comprehensive healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized campus cafeterias across all SYSU campuses; meals typically cost CNY 15 to 25 per day, easily covered by the monthly stipend.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full borrowing privileges across SYSU Libraries, electronic scientific databases, and access to Tianhe-2 Supercomputer at the National Supercomputer Center in Guangzhou.",
                "amount": "100% covered supercomputing & library infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "SYSU Graduate School and faculty research projects provide conference travel subsidies up to CNY 3,000 to 6,000 for approved papers.",
                "amount": "Up to CNY 6,000 research & conference funds"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free university inter-campus shuttle bus network connecting Guangzhou North, South, and East campuses, plus discounted student metro passes.",
                "amount": "Free inter-campus shuttle transit"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Chinese Double First Class / C9 partner university (Sun Yat-sen University).",
            "participating_institutions": [
                "Sun Yat-sen University (Guangzhou South/East Campuses, Shenzhen Campus, Guangdong, China)"
            ],
            "university_rankings_scope": "QS World University Rankings #260, Top 10 in Mainland China; home to National Supercomputer Center in Guangzhou (Tianhe-2) and premier research labs in AI, microelectronics, and marine science.",
            "available_majors": [
                "MSc / PhD in Computer Science and Technology",
                "MSc / PhD in Artificial Intelligence and Big Data",
                "MSc / PhD in Software Engineering",
                "MSc / PhD in Information and Communication Engineering",
                "MSc / PhD in Biomedical Engineering",
                "MSc / PhD in Marine Sciences and Ocean Engineering",
                "MSc / PhD in Applied Mathematics",
                "MSc / PhD in Materials Physics and Chemistry"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 to 3 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with 80%+ marks, verified transcripts, IELTS 6.5+ / TOEFL 90+ or MOI certificate, pre-acceptance letter from SYSU professor (strongly recommended), two professor recommendation letters, CV, study plan, and Foreigner Physical Examination Form.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of Computer Science and Engineering is highly selective; securing an official Pre-Acceptance Letter / Form from an SYSU doctoral supervisor dramatically elevates scholarship success.",
            "strategic_program_match_advice": "Reach out to SYSU professors in Guangzhou and Shenzhen campuses with tailored research proposals connecting to high-performance computing, smart healthcare, or AI vision."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://iso.sysu.edu.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "SYSU International Student System & CSC Online Application System (Agency No. 10558)",
            "account_creation_instructions": "Submit application on the CSC portal choosing Program Category B (Agency No. 10558 for SYSU), then submit on the SYSU International Student Application System, upload all supporting documents, and pay CNY 400 fee.",
            "step_by_step_workflow": [
                "Step 1: Contact potential SYSU faculty supervisors and request a Foreigner Acceptance Letter.",
                "Step 2: Obtain valid English proficiency test or MOI certificate, Foreigner Physical Examination report, and police character certificate.",
                "Step 3: Register on CSC portal (studyinchina.csc.edu.cn), choose Type B, enter SYSU Agency No. 10558, and submit application.",
                "Step 4: Register on SYSU portal (iso.sysu.edu.cn), complete online application, upload all documents including CSC form, and pay CNY 400 fee.",
                "Step 5: SYSU academic departments review dossiers and conduct virtual interviews for shortlisted candidates.",
                "Step 6: University nominates selected candidates to the China Scholarship Council for final approval.",
                "Step 7: CSC issues official Admission Notice and JW201 Visa Form in July.",
                "Step 8: Apply for Chinese X1 Visa at Chinese Visa Center and travel to Guangzhou/Shenzhen for September registration."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track (CSC Type B): Admission and scholarship are processed concurrently by SYSU and confirmed by CSC.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed and stamped official PDF letters from full professors or associate professors.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words for Master's, 1,500 words for PhD) describing research background, proposed thesis topic, and study objectives in China.",
            "study_plan_research_proposal_requirements": "Comprehensive research proposal outlining research domain, methodologies, experimental designs, and alignment with SYSU laboratory facilities.",
            "cv_format_requirements": "Standard academic research CV detailing education, publications, research projects, technical skills, and academic awards.",
            "interviews_conducted": True,
            "interview_format_details": "Departmental faculty panel interview via Tencent Meeting / VooV / Zoom evaluating subject knowledge and research aptitude.",
            "standardized_tests": "IELTS 6.5+, TOEFL 90+, Duolingo 120+, or English MOI certificate accepted.",
            "application_fee_amount": "CNY 400 (approx. USD 58 / ~PKR 16,000)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani credentials.",
            "translation_requirements": "Certified English or Chinese translation of all non-English/non-Chinese documents.",
            "final_submission_method": "Dual online submission via CSC portal and SYSU international student portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Notarized Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree with minimum 80% aggregate marks from an accredited university.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA Pakistan, and notarized."
            },
            {
                "document_name": "Detailed Study Plan / Research Proposal",
                "mandatory": True,
                "specification": "Formal research proposal (minimum 1,000 words Master's / 1,500 words PhD) detailing proposed research project.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Two Letters of Recommendation from Professors",
                "mandatory": True,
                "specification": "Confidential letters from full or associate professors with contact details and signatures.",
                "pakistan_specific_instruction": "On official institutional letterhead."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Standard Chinese medical examination form completed, signed, and stamped by an authorized hospital with lab test results.",
                "pakistan_specific_instruction": "Issued by recognized diagnostic laboratory."
            },
            {
                "document_name": "Non-Criminal Record Certificate (Police Clearance)",
                "mandatory": True,
                "specification": "Official police character clearance certificate issued within the last 6 months.",
                "pakistan_specific_instruction": "Attested by MoFA Pakistan."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 90+, Duolingo 120+, or official English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid beyond March 2026.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 15",
            "application_deadline": "February 15 (CSC Type B deadline) / March 31 (University direct scholarship deadline)",
            "university_admission_deadline": "February 15",
            "document_submission_deadline": "February 15",
            "recommendation_letters_deadline": "February 15",
            "interview_period": "March - April",
            "shortlist_announcement": "May (University nomination) / July (CSC final confirmation)",
            "final_result_acceptance_deadline": "July 15",
            "visa_application_window": "July - August",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Single annual admission cycle for Fall entry; CSC Type B applications strictly due in mid-February."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior academic GPA, university standing, course rigor)",
            "extracurricular_and_leadership_weight": "5% (Character, leadership, intercultural adaptability)",
            "research_experience_weight": "40% (Prior publications, research proposal quality, professor pre-acceptance)",
            "work_experience_weight": "5% (Relevant industry engineering or research experience)",
            "personal_statement_weight": "5% (Study plan clarity and intent)",
            "recommendations_weight": "5% (Referee appraisals of research independence)",
            "interview_weight": "5% (Performance in department interview)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "SYSU School Admissions Committee, International Student Office, and China Scholarship Council Evaluation Board.",
            "evaluation_methodology": "Competitive multi-stage academic evaluation based on prior GPA, research publications, supervisor endorsement, and interview performance."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 international postgraduate applicants across SYSU",
            "total_scholarships_awarded": "~120 to 180 fully funded CSC Type B awards annually",
            "acceptance_rate_global": "~3.5% to 5.0%",
            "acceptance_rate_pakistan": "~6.0% to 9.0% for applicants with professor pre-acceptance and published papers",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.40 / 4.00, accompanied by 1+ peer-reviewed conference or journal publications",
            "typical_academic_and_research_profile": "Graduates holding strong bachelor's or master's degrees in STEM, with documented research capability, pre-acceptance from an SYSU professor, and clean records.",
            "common_backgrounds_of_winners": "Graduates from Pakistani engineering and science institutions (NUST, FAST, COMSATS, UET Lahore, Quaid-i-Azam, GIKI, PIEAS).",
            "high_representation_countries": "Pakistan, Russia, Malaysia, Thailand, Indonesia, Nigeria, Egypt, Bangladesh, Vietnam.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portals at iso.sysu.edu.cn and studyinchina.csc.edu.cn.",
                "Beware of unauthorized agents claiming to sell guaranteed CSC scholarship seats; CSC strictly prohibits intermediaries."
            ],
            "application_fee_warning": "Application fee of CNY 400 is paid directly through the secure SYSU online portal; the CSC portal itself is completely free.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents with templated research proposals are systematically rejected by SYSU.",
            "hidden_costs_breakdown": [
                "SYSU application fee: CNY 400 (~PKR 16,000).",
                "Chinese X1 Visa fee in Pakistan: ~PKR 18,000.",
                "Medical checkup & police certificate attestations: ~PKR 25,000 to 35,000.",
                "Initial relocation flight to Guangzhou/Shenzhen: ~PKR 180,000 to 250,000.",
                "Initial pocket money before first stipend disbursement: ~CNY 1,500 (~PKR 58,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need HSK Chinese fluency. Reality: All STEM graduate programs are taught and examined 100% in English.",
                "Myth: Pre-acceptance letters are required. Reality: Not legally mandatory, but having a professor's pre-acceptance letter increases admission likelihood to over 70%."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim CSC covers international airfare; CSC Type B university programs do NOT cover international airfare."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass the Annual CSC Comprehensive Review evaluating academic credits, research progress, and campus conduct.",
            "attendance_requirements": "Full-time resident study in Guangzhou or Shenzhen; unexcused absences result in stipend deduction.",
            "academic_progress_monitoring": "Annual CSC review conducted every May by the host school and International Student Office.",
            "work_restrictions_during_study": "Commercial off-campus employment is restricted by Chinese student visa regulations; part-time on-campus work-study permitted with university approval.",
            "home_country_return_obligation": "None; graduates are free to pursue post-doctoral fellowships, corporate employment in China, or return home.",
            "service_obligations_or_bonds": "Zero financial bond or service commitment.",
            "repayment_clawback_conditions": "Scholarship is cancelled and student repatriated if dismissed for academic failure, disciplinary infractions, or criminal offenses.",
            "rules_for_changing_university": "Non-transferable to other Chinese universities under CSC rules.",
            "rules_for_changing_major": "Changing major is strictly prohibited after scholarship registration.",
            "extension_policy": "Extensions are generally not granted; students must complete degrees within the official approved period."
        },
        "official_sources_verified": [
            {
                "source_name": "Sun Yat-sen University International Student Office CSC Program",
                "source_url": "http://iso.sysu.edu.cn/en/scholarship/chinese-government-scholarship",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "https://www.campuschina.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-051": {
        "scholarship_id": "SCH-AS-051",
        "basic_details": {
            "scholarship_name": "Hiroshima University Advanced Science & Engineering MEXT Award (University Recommendation IGP)",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan & Hiroshima University",
            "host_country": "Japan",
            "host_institutions_covered": "Hiroshima University (Higashi-Hiroshima Campus, Hiroshima Prefecture, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Advanced Science and Engineering: Informatics and Data Science, Quantum Matter, Electrical Systems, Mechanical Engineering, Chemistry, Chemical Engineering, and Civil and Environmental Engineering.",
            "number_of_awards_total": "~30 to 45 prestigious MEXT University Recommendation scholarships awarded annually",
            "number_of_awards_pakistan": "Open globally on merit; Pakistani scholars in computing, robotics, and electrical engineering have a strong competitive presence (~4 to 8 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master's; 3 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 144,000 / month for Master's (~PKR 270,000 / month); JPY 145,000 / month for PhD (~PKR 272,000 / month) plus 100% full tuition exemption and round-trip international airfare"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries holding diplomatic relations with Japan (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2, 1991 (under 35 years of age at the time of program start).",
            "academic_qualifications": "16-year Bachelor's degree with minimum GPA of 2.30 / 3.00 on the official MEXT grading scale (equivalent to minimum CGPA 3.20+ / 4.00 or 80%+ marks) for Master's; 18-year Master's degree with minimum GPA 2.30 / 3.00 on MEXT scale for PhD.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Must satisfy MEXT calculation formula yielding at least 2.30 / 3.00 points; competitive applicants typically score 2.6+ / 3.0.",
            "subject_background_prerequisites": "Computer science, informatics, electrical engineering, mechanical engineering, materials science, or physics.",
            "current_education_status": "Graduated or final-year students graduating before September 30 of intake year.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific research publications, conference presentations, or thesis projects strongly valued.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "CEFR Level B2 or higher: IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or official certificate verifying English as Medium of Instruction (MOI).",
            "other_language_requirements": "Japanese language proficiency is NOT required; all courses, seminars, and research are conducted 100% in English.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure informal agreement / consent of acceptance from a prospective Hiroshima University academic supervisor prior to formal submission.",
            "previous_scholarship_restrictions": "Ineligible if recipient of MEXT scholarship within the past 3 years or currently holding other Japanese government or foreign governmental scholarships.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full exemption from university matriculation/entrance fee (JPY 282,000) and full annual tuition fees (JPY 535,800/year).",
                "amount": "100% covered (~JPY 817,800 first-year value; ~PKR 1,530,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "University examination and screening application fee (JPY 30,000) is completely waived for MEXT candidates.",
                "amount": "JPY 0 (100% free)"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "Hiroshima University International House (I-House) or student dormitories in Saijo/Higashi-Hiroshima (approx. JPY 15,000 to 25,000 / month rent) funded comfortably via living stipend.",
                "amount": "Funded from stipend (~JPY 20,000 / month rent in Saijo)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend disbursed directly to Japan Post Bank account: JPY 144,000 / month for Master's (~PKR 270,000 / month); JPY 145,000 / month for PhD (~PKR 272,000 / month).",
                "amount": "JPY 144,000 to 145,000 / month (~PKR 270,000 to 272,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Round-trip economy international airfare between Pakistan (Islamabad/Lahore/Karachi) and Japan (Hiroshima Airport or Kansai/Tokyo International) provided by MEXT.",
                "amount": "100% covered round-trip international flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese College Student Visa issued free of charge through the Embassy of Japan in Islamabad or Consulate-General in Karachi.",
                "amount": "100% covered / waived visa fee"
            },
            "health_insurance": {
                "status": "NOT_COVERED",
                "details": "Mandatory Japan National Health Insurance (NHI) premium (approx. JPY 2,000 / month for students; covers 70% of medical costs) paid independently from stipend.",
                "amount": "Approx. JPY 2,000 / month borne from stipend"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Groceries and campus dining funded from monthly living allowance.",
                "amount": "Covered via stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Research laboratory workstations, computing clusters, library access, and thesis research materials provided by laboratory research funds.",
                "amount": "100% covered research computing access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding (Kakenhi grants) and university student travel subsidies provide up to JPY 100,000 to 200,000 per year for presenting papers at conferences in Japan and abroad.",
                "amount": "Up to JPY 200,000 / year travel funds"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Geiyo and Chugoku JR local buses serve Higashi-Hiroshima campus; student discount commuter passes available.",
                "amount": "Not covered"
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Japanese national flagship research university (Hiroshima University).",
            "participating_institutions": [
                "Hiroshima University (Higashi-Hiroshima Campus, Hiroshima Prefecture, Japan)"
            ],
            "university_rankings_scope": "Times Higher Education World University Rankings #601-800, Top 15 in Japan; selected as a Type A (Top Global) University by MEXT; renowned for Synchrotron Radiation Center (HiSOR), Quantum Matter, and Informatics.",
            "available_majors": [
                "Informatics and Data Science (AI, Systems, Computer Vision)",
                "Quantum Matter (Condensed Matter Physics, Semiconductor Devices)",
                "Electrical Systems and Control Engineering",
                "Mechanical Engineering and Robotics",
                "Applied Chemistry and Chemical Engineering",
                "Civil and Environmental Engineering",
                "Transportation Engineering and Smart Mobility"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with minimum MEXT GPA 2.3/3.0, verified transcripts, IELTS 6.5+ / TOEFL 80+ or MOI certificate, informal acceptance from prospective supervisor, two academic recommendation letters, research plan, CV, and valid passport.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing preliminary informal acceptance from a faculty supervisor in the Graduate School of Advanced Science and Engineering is the mandatory prerequisite; applications without supervisor consent cannot proceed.",
            "strategic_program_match_advice": "Review Hiroshima University Researchers Information directory; contact professors with concise research pitches referencing their recent papers in robotics, informatics, or semiconductor materials."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.hiroshima-u.ac.jp/en/admissions/financial_support/scholarships",
            "portal_system_name": "Hiroshima University MEXT University Recommendation Portal",
            "account_creation_instructions": "Identify prospective supervisor on the Hiroshima University faculty database, email research proposal and CV, secure written consent of acceptance, and submit required MEXT application dossier directly to the graduate school office.",
            "step_by_step_workflow": [
                "Step 1: Contact potential research supervisor at Hiroshima University with CV, transcripts, and 2-page research outline.",
                "Step 2: Obtain formal written consent / Letter of Acceptance from the prospective supervisor.",
                "Step 3: Ensure valid IELTS (6.5+), TOEFL (80+), or official MOI certificate is available.",
                "Step 4: Prepare MEXT Application Form, Field of Study and Research Program Plan, and academic transcripts.",
                "Step 5: Submit application package through the graduate school international office by mid-January deadline.",
                "Step 6: Graduate school screening committee evaluates candidates and nominates finalists to Hiroshima University President and MEXT.",
                "Step 7: MEXT officially confirms scholarship awards in June.",
                "Step 8: Hiroshima University issues Certificate of Eligibility (COE); obtain Japanese Student Visa and depart for Japan in late September."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track: The admitting academic department nominates the candidate directly to MEXT for scholarship conferral.",
            "recommendation_letters_submission_method": "Submitted as signed PDF letters on institutional letterhead addressed to the President of Hiroshima University.",
            "personal_statement_prompts": "MEXT Field of Study and Study Program Sheet detailing past research specialization and concrete research plan in Japan.",
            "study_plan_research_proposal_requirements": "Structured research plan (2 to 3 pages) covering background, research questions, methodologies, and anticipated contributions.",
            "cv_format_requirements": "Detailed academic research CV listing all academic history, research projects, publications, and technical skills.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisory technical video interview via Zoom to discuss research methodology and laboratory research compatibility.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction certificate mandatory.",
            "application_fee_amount": "JPY 0 (100% free of charge)",
            "attestation_requirements": "HEC and MoFA Pakistan verified transcripts required upon conditional admission.",
            "translation_requirements": "Certified English or Japanese translation of all non-English documents.",
            "final_submission_method": "Digital submission via host academic department and graduate school office."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree with minimum MEXT GPA 2.30 / 3.00 from an accredited university.",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "MEXT Application Form and Field of Study Plan",
                "mandatory": True,
                "specification": "Official Japanese government application form and detailed research plan.",
                "pakistan_specific_instruction": "Structured research plan."
            },
            {
                "document_name": "Letter of Recommendation addressed to President of Hiroshima University",
                "mandatory": True,
                "specification": "Confidential recommendation letter from Dean or Department Head of applicant's alma mater.",
                "pakistan_specific_instruction": "On official university letterhead."
            },
            {
                "document_name": "Formal Supervisor Consent / Acceptance Letter",
                "mandatory": True,
                "specification": "Written confirmation from Hiroshima University prospective professor agreeing to act as supervisor.",
                "pakistan_specific_instruction": "Secured via email prior to submission."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Abstract of Graduation Thesis / Research Publications",
                "mandatory": True,
                "specification": "Summary of bachelor's/master's thesis (approx. 1 to 2 pages) and copies of any published papers.",
                "pakistan_specific_instruction": "Thesis summary."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for minimum 1 year.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "November 1",
            "application_deadline": "January 15 (Annual University Recommendation closing deadline)",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "January 15",
            "recommendation_letters_deadline": "January 15",
            "interview_period": "January - February",
            "shortlist_announcement": "March (University nomination) / June (MEXT final approval)",
            "final_result_acceptance_deadline": "July 1",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Fall semester intake)",
            "annual_cycle_notes": "Single annual admission cycle for October entry; supervisor contact should be initiated by November/December."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Academic transcript GPA converted to MEXT 3.0 scale)",
            "extracurricular_and_leadership_weight": "5% (Character, leadership, international exchange adaptability)",
            "research_experience_weight": "45% (Research plan feasibility, supervisor endorsement, prior thesis/publications)",
            "work_experience_weight": "5% (Industry engineering or laboratory technical experience)",
            "personal_statement_weight": "5% (Clarity of academic motivations in Japan)",
            "recommendations_weight": "5% (Dean/Professor referee praise)",
            "interview_weight": "5% (Supervisor technical discussion)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Graduate School of Advanced Science and Engineering Admissions Committee and MEXT Scholarship Selection Council.",
            "evaluation_methodology": "Competitive ranking based on MEXT GPA calculation, research plan depth, and supervisor research group capacity."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~600 to 900 international candidates seeking supervisor endorsement across departments",
            "total_scholarships_awarded": "~30 to 45 MEXT University Recommendation awards annually",
            "acceptance_rate_global": "~5.0% to 7.0%",
            "acceptance_rate_pakistan": "~6.0% to 10.0% for applicants who secure supervisor endorsement and satisfy MEXT GPA >= 2.3",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.50 / 4.00 (MEXT scale >= 2.6 / 3.0), strong final-year thesis or published research",
            "typical_academic_and_research_profile": "Graduates holding strong bachelor's or master's degrees in STEM, with documented research capability, supervisor endorsement, and clean records.",
            "common_backgrounds_of_winners": "Graduates from Pakistani engineering and science institutions (NUST, GIKI, UET Lahore, PIEAS, FAST, Quaid-i-Azam, COMSATS).",
            "high_representation_countries": "Pakistan, Indonesia, Vietnam, Bangladesh, China, Thailand, Egypt, India.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official Hiroshima University website at hiroshima-u.ac.jp.",
                "MEXT scholarships do NOT require application or processing fees; beware of fraudulent brokers."
            ],
            "application_fee_warning": "The application and screening process is 100% free of charge.",
            "agent_and_intermediary_warnings": "Commercial agencies cannot contact professors on your behalf; faculty members immediately reject agency-forwarded inquiries.",
            "hidden_costs_breakdown": [
                "All major expenses (tuition, airfare, monthly stipend) are 100% covered.",
                "Japan National Health Insurance: ~JPY 2,000 / month (covered from stipend).",
                "Initial settling cash prior to first stipend deposit in Japan: ~JPY 50,000 to 70,000 (~PKR 95,000 - 135,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need Japanese language fluency. Reality: All coursework, seminars, laboratory meetings, and thesis defenses are conducted 100% in English.",
                "Myth: MEXT awards are loan-based. Reality: MEXT is a 100% grant scholarship with zero repayment or post-graduation service bond."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently quote outdated stipend values; current verified MEXT monthly stipend is JPY 144,000 (Master's) and JPY 145,000 (PhD)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative grade point average of 2.30 / 3.00 on the MEXT scale throughout each academic year.",
            "attendance_requirements": "Full-time resident study in Higashi-Hiroshima and active laboratory research engagement.",
            "academic_progress_monitoring": "Annual progress reviews and milestone evaluations conducted by the academic advisor.",
            "work_restrictions_during_study": "Part-time work permitted up to 28 hours per week with university and immigration permission, but research commitment takes priority.",
            "home_country_return_obligation": "None; graduates are eligible to remain in Japan for post-doctoral research or corporate engineering employment (Designated Activities / Highly Skilled Professional visa).",
            "service_obligations_or_bonds": "Zero service bond or repayment liability.",
            "repayment_clawback_conditions": "Stipend suspended or terminated if student takes unapproved leave of absence, fails to maintain GPA >= 2.30, or commits disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Changing major is strictly prohibited after scholarship award.",
            "extension_policy": "Master's students may apply for a competitive MEXT extension to continue onto the PhD program."
        },
        "official_sources_verified": [
            {
                "source_name": "Hiroshima University MEXT Scholarship Information",
                "source_url": "https://www.hiroshima-u.ac.jp/en/admissions/financial_support/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Graduate School of Advanced Science and Engineering Admissions",
                "source_url": "https://www.hiroshima-u.ac.jp/en/adse/admissions",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-052": {
        "scholarship_id": "SCH-AS-052",
        "basic_details": {
            "scholarship_name": "Sejong University International Graduate Scholarship & Research Assistantships",
            "offering_entity": "Sejong University & Ministry of Education, Republic of Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "Sejong University Main Campus (Gwangjin-gu, Seoul, Republic of Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Department of Computer Science and Engineering, Department of Artificial Intelligence and Data Science, Department of Intelligent Mechatronics Engineering, Department of Software, Department of Information Security, and Department of Aerospace Engineering.",
            "number_of_awards_total": "~150 to 200 graduate scholarships and laboratory research assistantships awarded annually",
            "number_of_awards_pakistan": "Open globally on merit; Pakistani graduate scholars have an exceptionally strong presence in Sejong's computing and AI research laboratories (~20 to 35 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master's; 3 to 4 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "KRW 1,000,000 to 1,500,000 / month (approx. $750 to $1,120 / month; ~PKR 210,000 to 310,000 / month) laboratory living stipend plus 100% full tuition fee waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents are both non-Korean citizens (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 0,
            "age_limit_notes": "No upper age limit; evaluation based on academic GPA, programming skills, and research aptitude.",
            "academic_qualifications": "16-year Bachelor's degree with minimum cumulative GPA of 3.00 / 4.00 (or 75%+ marks) for Master's; 18-year Master's degree with minimum GPA 3.00 / 4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum undergraduate GPA of 3.0 / 4.0; 100% tuition waiver (Sejong Global Scholarship Class A) requires undergraduate GPA >= 3.5 / 4.0 or high English test score.",
            "subject_background_prerequisites": "Computer science, software engineering, artificial intelligence, electronic engineering, mechatronics, or related quantitative field.",
            "current_education_status": "Graduated or final-year students graduating before semester start date.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific research publications, software coding projects, or machine learning expertise strongly valued.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0 (6.5+ for top scholarship tier), TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate accepted.",
            "other_language_requirements": "Korean language proficiency is NOT required for English-track STEM laboratories.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates typically secure agreement from a prospective laboratory professor (PI) prior to application to guarantee living stipend support.",
            "previous_scholarship_restrictions": "Subject to university guidelines on concurrent award holding.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition waiver awarded through Sejong Global Scholarship Class A or combined with professor laboratory tuition matching funds.",
                "amount": "100% covered (~KRW 6,500,000 to 7,500,000 / semester value; ~PKR 2,700,000 to 3,100,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Non-refundable graduate application fee of KRW 120,000 (approx. USD 90 / ~PKR 25,000) paid online.",
                "amount": "KRW 120,000 (~PKR 25,000) application fee"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "On-campus international graduate dormitory (Happy Dormitory / Gwanggaeto Hall) or private studios (One-room / Goshiwon) near campus in Seoul funded via monthly stipend.",
                "amount": "Funded from stipend (~KRW 350,000 to 550,000 / month rent)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research stipend of KRW 1,000,000 to 1,500,000 / month ($750 to $1,120 / month; ~PKR 210,000 to 310,000 / month) disbursed by the supervising professor's national research projects (BK21 Four / NRF).",
                "amount": "KRW 1,000,000 to 1,500,000 / month (~PKR 210,000 to 310,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare to Incheon/Seoul is self-funded or subsidized by professor project travel funds upon arrival.",
                "amount": "Not covered in standard package"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Korean D-2 Student Visa application fee (~$60 / ~PKR 17,000) paid directly to Korean Embassy in Islamabad or Consulate in Karachi.",
                "amount": "Approx. PKR 17,000 borne by student"
            },
            "health_insurance": {
                "status": "NOT_COVERED",
                "details": "Mandatory National Health Insurance Service (NHIS) coverage for international students in Korea (~KRW 70,000 / month; covers primary medical and dental care) funded from monthly stipend.",
                "amount": "Approx. KRW 70,000 / month borne from stipend"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Campus cafeterias at Sejong offer high-quality meals for KRW 4,500 to 6,500 per meal; easily covered by monthly living stipend.",
                "amount": "Covered via stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Dedicated laboratory desk, GPU computing workstations (NVIDIA A100/H100 clusters for AI labs), and full university library access included.",
                "amount": "100% covered research computing access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Supervising professors fully fund international travel, registration, and hotel expenses for students presenting papers at international conferences (IEEE, ACM, CVPR, ICCV).",
                "amount": "Full conference travel funding provided by lab"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Seoul Metropolitan Subway Line 7 connects directly to Children's Grand Park Station (Sejong University); transit funded independently via T-money card.",
                "amount": "Not covered"
            },
            "total_estimated_value_usd_per_year": 20000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading private research university in Seoul (Sejong University).",
            "participating_institutions": [
                "Sejong University Main Campus (Seoul, Republic of Korea)"
            ],
            "university_rankings_scope": "Times Higher Education World University Rankings #251-300, Top 8 in South Korea, THE Asia #39; renowned for Computer Science, Artificial Intelligence, and Hospitality Management.",
            "available_majors": [
                "MSc / PhD in Computer Science and Engineering",
                "MSc / PhD in Artificial Intelligence and Data Science",
                "MSc / PhD in Software Engineering",
                "MSc / PhD in Information Security",
                "MSc / PhD in Intelligent Mechatronics Engineering",
                "MSc / PhD in Aerospace Engineering",
                "MSc / PhD in Electronic Engineering",
                "MSc / PhD in Nanotechnology and Advanced Materials"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with 3.0+ GPA, verified transcripts, IELTS 6.0+ / TOEFL 80+ or MOI certificate, prospective professor recommendation letter, statement of purpose, CV, and financial guarantee documents.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing an informal acceptance / sponsorship email from a Sejong laboratory professor (PI) prior to application is the essential step to ensure 100% tuition waiver and living stipend.",
            "strategic_program_match_advice": "Browse Sejong faculty research labs in AI, Computer Vision, Cybersecurity, and Robotics; email professors with a tailored CV highlighting coding skills (PyTorch, TensorFlow, C++, ROS) and research publications."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://eng.sejong.ac.kr/graduate/admission_guide.do",
            "portal_system_name": "Sejong University Online Graduate Application System (Uwayapply)",
            "account_creation_instructions": "Contact prospective faculty professor in target laboratory, secure sponsorship commitment, register on Uwayapply, choose intended graduate department, complete online form, upload scanned credentials, and pay KRW 120,000 fee.",
            "step_by_step_workflow": [
                "Step 1: Identify faculty laboratory on Sejong website and contact professor with CV, transcripts, and research interests.",
                "Step 2: Attend virtual interview with professor and obtain written agreement for laboratory research assistantship.",
                "Step 3: Register on Uwayapply portal and complete Sejong graduate application form.",
                "Step 4: Upload official academic transcripts, English score report, statement of purpose, and CV.",
                "Step 5: Pay KRW 120,000 application fee online.",
                "Step 6: Submit hard copies of notarized transcripts and degree apostilles to Sejong International Student Center by deadline.",
                "Step 7: University admissions committee issues formal Certificate of Admission and scholarship letter.",
                "Step 8: Apply for Korean D-2 Student Visa at Korean Embassy in Pakistan and travel to Seoul for registration."
            ],
            "university_vs_scholarship_routing": "Integrated Professor Sponsorship Track: Tuition waiver scholarship and laboratory research stipend are formulated concurrently based on professor recommendation.",
            "recommendation_letters_submission_method": "Submitted as official signed recommendation letters, including the Sejong professor's official departmental recommendation form.",
            "personal_statement_prompts": "Self-introduction and study plan detailing academic background, technical skills, reasons for choosing Sejong University, and target research goals.",
            "study_plan_research_proposal_requirements": "Structured research plan (2 to 3 pages) outlining proposed research topic and alignment with the supervising laboratory.",
            "cv_format_requirements": "Standard academic research CV detailing education, publications, conference presentations, programming languages, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "Technical video interview via Zoom with laboratory professor (PI) testing programming skills, algorithm knowledge, and research motivation.",
            "standardized_tests": "IELTS Academic 6.0+, TOEFL iBT 80+, or official English Medium of Instruction certificate accepted.",
            "application_fee_amount": "KRW 120,000 (approx. USD 90 / ~PKR 25,000)",
            "attestation_requirements": "HEC and MoFA Pakistan verified degrees and transcripts, plus Apostille or Korean Embassy attestation.",
            "translation_requirements": "Notarized English translation of all non-English documents.",
            "final_submission_method": "Online submission via Uwayapply portal followed by postal submission of attested documents."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree with minimum GPA 3.0 / 4.0 from an accredited university.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA Pakistan, and Korean Embassy."
            },
            {
                "document_name": "Self-Introduction and Study Plan",
                "mandatory": True,
                "specification": "Comprehensive statement detailing academic background, research interests, and study plan in Korea.",
                "pakistan_specific_instruction": "Tailored to Sejong laboratory research."
            },
            {
                "document_name": "Recommendation Letter from Prospective Sejong Professor",
                "mandatory": True,
                "specification": "Official recommendation and financial sponsorship confirmation from Sejong supervising professor.",
                "pakistan_specific_instruction": "Secured via professor prior to application."
            },
            {
                "document_name": "Letters of Recommendation from Former Professors",
                "mandatory": True,
                "specification": "Two recommendation letters from university professors on official letterhead.",
                "pakistan_specific_instruction": "Signed and stamped."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic 6.0+, TOEFL iBT 80+, or official English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Certificate of Parent-Child Relationship (Family Registration)",
                "mandatory": True,
                "specification": "Official NADRA Family Registration Certificate (FRC) verifying foreign citizenship of candidate and parents.",
                "pakistan_specific_instruction": "NADRA FRC attested by MoFA."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for minimum 1 year.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 15 (Spring intake) / March 15 (Fall intake)",
            "application_deadline": "October 30 (Spring intake) / April 30 (Fall intake)",
            "university_admission_deadline": "October 30 (Spring) / April 30 (Fall)",
            "document_submission_deadline": "November 10 (Spring) / May 10 (Fall)",
            "recommendation_letters_deadline": "October 30",
            "interview_period": "November (Spring) / May (Fall)",
            "shortlist_announcement": "December (Spring) / June (Fall)",
            "final_result_acceptance_deadline": "January 10 (Spring) / July 10 (Fall)",
            "visa_application_window": "January (Spring) / July (Fall)",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Biannual admissions: Spring intake (starts March) and Fall intake (starts September)."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Academic transcript GPA, coursework grades in core technical subjects)",
            "extracurricular_and_leadership_weight": "5% (Character, coding competitions, technical community work)",
            "research_experience_weight": "45% (Prior research publications, coding projects, laboratory PI sponsorship)",
            "work_experience_weight": "5% (Industry software engineering or research lab experience)",
            "personal_statement_weight": "5% (Study plan clarity and technical depth)",
            "recommendations_weight": "5% (Strength of professor recommendations)",
            "interview_weight": "5% (Performance in technical interview with professor)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research capability)",
            "selection_panel_composition": "Departmental Faculty Admissions Committee, Laboratory Principal Investigators (PIs), and Graduate School Board.",
            "evaluation_methodology": "Holistic review prioritizing laboratory research match, programming capability, prior publications, and supervising professor's endorsement."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,000 to 3,000 international applicants across graduate faculties",
            "total_scholarships_awarded": "~150 to 200 fully funded graduate research positions annually",
            "acceptance_rate_global": "~6.5% to 8.5%",
            "acceptance_rate_pakistan": "~8.0% to 12.0% for applicants who secure professor sponsorship and have strong coding/publication records",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.30 / 4.00, accompanied by strong coding portfolio (GitHub) or research publications",
            "typical_academic_and_research_profile": "Graduates holding strong bachelor's or master's degrees in CS/Engineering with demonstrated machine learning, software development, or research skills.",
            "common_backgrounds_of_winners": "Graduates from Pakistani engineering and computing institutions (NUST, FAST-NUCES, COMSATS, UET, GIKI, Quaid-i-Azam, PIEAS).",
            "high_representation_countries": "Pakistan, Vietnam, India, Bangladesh, China, Indonesia, Nepal, Uzbekistan, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official Sejong portal at sejong.ac.kr and uwayapply.com.",
                "Beware of unauthorized recruitment agencies charging exorbitant placement fees; always contact professors directly."
            ],
            "application_fee_warning": "Application fee of KRW 120,000 is paid directly via Uwayapply; no extra agent fees required.",
            "agent_and_intermediary_warnings": "Commercial agencies cannot guarantee admission or lab stipends; professors make autonomous decisions.",
            "hidden_costs_breakdown": [
                "Application fee: KRW 120,000 (~PKR 25,000).",
                "Korean D-2 Visa fee in Pakistan: ~PKR 17,000.",
                "Notarization, HEC/MoFA, and Korean Embassy attestations: ~PKR 30,000 to 45,000.",
                "Relocation flight to Seoul: ~PKR 180,000 to 260,000.",
                "Initial dormitory security deposit in Seoul: ~KRW 300,000 (~PKR 62,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need TOPIK Korean scores to study at Sejong. Reality: STEM graduate labs operate 100% in English; TOPIK is not required.",
                "Myth: You can get fully funded without contacting a professor. Reality: Getting professor sponsorship before applying is essential to guarantee monthly laboratory living stipends."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently quote outdated stipend values; current verified laboratory stipends range from KRW 1,000,000 to 1,500,000 per month."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative graduate GPA of 3.0 / 4.0 throughout each semester.",
            "attendance_requirements": "Full-time resident study in Seoul and active daily participation in laboratory research duties.",
            "academic_progress_monitoring": "Semester-end academic review and research milestone presentations evaluated by the supervising professor.",
            "work_restrictions_during_study": "Part-time work off-campus is strictly restricted during the first semester and requires university and immigration permission thereafter.",
            "home_country_return_obligation": "None; graduates are eligible for Korean job-seeking visas (D-10) and skilled professional work visas (E-7) in the Korean tech sector.",
            "service_obligations_or_bonds": "Obligation to fulfill designated laboratory research duties (BK21/NRF project deliverables).",
            "repayment_clawback_conditions": "Funding terminated if student leaves laboratory without permission, withdraws, or fails academic standing.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Requires approval from supervising professor and Department Chair.",
            "extension_policy": "Funding extends through standard degree duration (2 years MSc, 3-4 years PhD); extensions subject to professor grant funding."
        },
        "official_sources_verified": [
            {
                "source_name": "Sejong University International Graduate Admissions Portal",
                "source_url": "https://eng.sejong.ac.kr/graduate/admission_guide.do",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Sejong University Graduate School Scholarships",
                "source_url": "https://eng.sejong.ac.kr/graduate/scholarship.do",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
