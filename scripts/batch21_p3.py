# scripts/batch21_p3.py
# SCH-AS-045: Wuhan University (WHU) Chinese Government & Belt and Road Award (China)
# SCH-AS-046: Kobe University System Informatics MEXT Award (Japan)
# SCH-AS-047: Ajou University International Graduate Scholarship (South Korea)
# SCH-AS-048: Universiti Tenaga Nasional (UNITEN) Postgraduate Excellence Award (Malaysia)

DATA_P3 = {
    "SCH-AS-045": {
        "scholarship_id": "SCH-AS-045",
        "basic_details": {
            "scholarship_name": "Wuhan University (WHU) Chinese Government Scholarship (CSC Silk Road & High-Level Program)",
            "offering_entity": "China Scholarship Council (CSC - Ministry of Education of China) & Wuhan University",
            "host_country": "China",
            "host_institutions_covered": "Wuhan University Luojia Hill Campus (Wuhan, Hubei Province, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computer Science & School of Cyber Science and Engineering: Computer Software and Theory, Computer Applied Technology, Artificial Intelligence, Cyber Security, Spatial Information and Geomatics, and Software Engineering.",
            "number_of_awards_total": "~180 to 250 Chinese Government Scholarships awarded across graduate faculties annually",
            "number_of_awards_pakistan": "Extremely active bilateral intake under China-Pakistan higher education partnership; Pakistani computing scholars secure ~20 to 35 fully funded awards annually",
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
            "special_eligibility_categories": "Applicants should contact a prospective supervisor at WHU School of Computer Science and obtain an official Acceptance Letter prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or provincial scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee exemption at Wuhan University covered for the entire program duration.",
                "amount": "100% covered (~RMB 28,000 - 38,000 / year value; ~PKR 1,090,000 - 1,480,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "WHU international graduate application fee of RMB 800 (~USD 115 / ~PKR 32,000) payable online.",
                "amount": "RMB 800 (~PKR 32,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free accommodation in on-campus international student dormitories (twin room for Master's, single room for PhD) at Luojia Hill Campus, or monthly housing subsidy.",
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
                "details": "Full access to WHU Central Library, engineering laboratories, GPU workstations, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's national research grants for presenting papers at conferences.",
                "amount": "Up to RMB 5,000 for conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle bus operating across Luojia Hill Campus and convenient access to Wuhan Metro Line 2.",
                "amount": "Convenient metro and campus access"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Double First-Class national university: Wuhan University (WHU).",
            "participating_institutions": [
                "Wuhan University (Luojia Hill Campus, Wuhan, Hubei Province, China)"
            ],
            "university_rankings_scope": "Ranked top 150 globally in QS/THE World Rankings, world-leading center for remote sensing, geospatial informatics, and top 50 globally in computer software systems.",
            "available_majors": [
                "Computer Science and Technology",
                "Artificial Intelligence and Machine Learning",
                "Cyber Science and Engineering",
                "Software Engineering and Cloud Computing",
                "Geographic Information Systems and Spatial Informatics",
                "Information and Communication Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 to 3 years for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor acceptance letter, study plan (1,000 words), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "WHU Computer Science and Spatial Informatics research labs are world-renowned; obtaining an official Acceptance Letter from a faculty professor is the key gatekeeper to CSC nomination.",
            "strategic_program_match_advice": "Browse WHU School of Computer Science faculty profiles (cs.whu.edu.cn), email prospective supervisors with a tailored research proposal and CV, and obtain the official WHU Acceptance Letter before the February 15 deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://admission.whu.edu.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "WHU International Student Application System & CSC Portal",
            "account_creation_instructions": "Register an account on the WHU online application portal, select graduate program, check the box applying for Chinese Government Scholarship / Silk Road Program, and apply on the CSC portal (Agency No: 10486).",
            "step_by_step_workflow": [
                "Step 1: Contact prospective supervisors in WHU School of Computer Science and secure an official Acceptance Letter (October - January).",
                "Step 2: Create user credentials on the WHU International Student Admissions Portal (http://admission.whu.edu.cn/).",
                "Step 3: Submit online degree application, upload all required documents, and select Chinese Government Scholarship.",
                "Step 4: Pay the application fee of RMB 800 online before the deadline (typically February 15).",
                "Step 5: Apply on the CSC portal (https://studyinchina.csc.edu.cn/) under Type B using WHU Agency Number 10486.",
                "Step 6: WHU faculty committee conducts academic review and online technical interviews in March.",
                "Step 7: Official admission and scholarship package (JW201 form) dispatched in June/July; apply for Chinese X1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via the WHU portal covers both program admission and scholarship nomination.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by former academic professors or research supervisors.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words in English) outlining academic background, proposed research focus, and reasons for choosing WHU.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute technical video interview via Zoom / Tencent Meeting conducted by faculty admissions panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "RMB 800 (~USD 115 / ~PKR 32,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English or Chinese translation required for all official documents.",
            "final_submission_method": "Online upload via WHU admissions portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "WHU Professor Acceptance Letter (Official Form)",
                "mandatory": True,
                "specification": "Official acceptance letter signed by an eligible WHU professor.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Study and Research Plan (Minimum 1,000 words)",
                "mandatory": True,
                "specification": "Detailed research plan outlining academic background, proposed research questions, and methodology.",
                "pakistan_specific_instruction": "Must be aligned with WHU supervisor's lab projects."
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
            "semester_commencement": "Early September (commencing in Wuhan)",
            "annual_cycle_notes": "Main intake is Autumn (September). Applications close annually on February 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate GPA and performance in core computing and engineering courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor acceptance letter, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for WHU)",
            "recommendations_weight": "10% (Academic referee appraisals and professor's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into final ranking)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "WHU Faculty Admissions Board and School of International Education Scholarship Committee.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit and professor nomination followed by faculty panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,800 international graduate applicants across WHU",
            "total_scholarships_awarded": "~180 to 250 fully funded CSC scholarships awarded annually",
            "acceptance_rate_global": "~7% to 10%",
            "acceptance_rate_pakistan": "~10% to 15% among candidates with professor acceptance letters",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, Russia, Iran, Bangladesh, Indonesia, Egypt, Nigeria, Thailand.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed CSC scholarships or WHU admissions.",
                "Applications are handled exclusively via the official WHU portal (http://admission.whu.edu.cn/) and CSC portal."
            ],
            "application_fee_warning": "WHU application fee is RMB 800 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Wuhan University does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "WHU application fee: RMB 800 (~PKR 32,000).",
                "Foreigner physical examination in Pakistan: ~PKR 15,000.",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~RMB 2,000 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get CSC without a professor's acceptance letter. Reality: At top national universities like WHU, having a professor's acceptance letter is essential for scholarship nomination.",
                "Myth: You must study in Chinese. Reality: WHU offers complete Master's and PhD programs taught and researched 100% in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state application deadline is April; WHU CSC scholarship application portal closes strictly on February 15."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and pass the mandatory CSC Annual Scholarship Review each spring.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab in Wuhan.",
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
                "source_name": "WHU School of International Education Official Portal",
                "source_url": "http://admission.whu.edu.cn/",
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

    "SCH-AS-046": {
        "scholarship_id": "SCH-AS-046",
        "basic_details": {
            "scholarship_name": "Kobe University Graduate School of System Informatics MEXT Honors Fellowship",
            "offering_entity": "Kobe University & Japanese Ministry of Education, Culture, Sports, Science and Technology (MEXT)",
            "host_country": "Japan",
            "host_institutions_covered": "Kobe University Rokkodai Campus (Kobe, Hyogo Prefecture, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of System Informatics: Systems Science, Information Science, Computational Science (Center for Computational Science / RIKEN Fugaku Supercomputer linkage), and Artificial Intelligence.",
            "number_of_awards_total": "~35 to 50 University-Recommended MEXT and Kobe University Honors Fellowships awarded annually across international intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computational science secure ~4 to 7 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 3 years for PhD, subject to satisfactory annual academic and research progress",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 144,000 / month (~PKR 275,000 / month for Master's); JPY 145,000 - 180,000 / month (~PKR 277,000 - 345,000 / month for PhD)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries holding diplomatic relations with Japan (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Under 35 years of age on April 1 of the intake year for the MEXT track; no age limit for university internal fellowships.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) with minimum CGPA 3.30 / 4.00 (or 75%+ aggregate) from an HEC-recognized university in Pakistan for Master's; research Master's degree (18 years education) with strong thesis output for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Must meet minimum MEXT GPA calculation of 2.30 / 3.00 over the preceding two academic years.",
            "subject_background_prerequisites": "Rigorous undergraduate preparation in algorithms, computational mathematics, linear algebra, discrete mathematics, and programming (C/C++, Python).",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or institutional English Medium of Instruction (MOI) certificate from Pakistani university.",
            "other_language_requirements": "Japanese language proficiency is not required; research and coursework are conducted 100% in English.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must contact a prospective supervising professor at Kobe University Graduate School of System Informatics and obtain informal preliminary consent prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another government scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full exemption of entrance examination fee (JPY 30,000), admission fee (JPY 282,000), and annual tuition fees (JPY 535,800 / year value).",
                "amount": "100% covered (~JPY 535,800 / year; ~PKR 1,020,000 / year value)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application and screening fees are 100% waived for MEXT fellowship nominees.",
                "amount": "JPY 0 (100% waived)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Guaranteed on-campus single room in Kobe University International Student Residence (Fukae or Kokui House) for the first 6-12 months; monthly rent JPY 18,000 - JPY 32,000.",
                "amount": "Subsidized rent ~JPY 24,000 / month (~PKR 46,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living allowance: JPY 144,000 per month for Master's (~PKR 275,000 / month; JPY 1,728,000 / year); JPY 145,000 to JPY 180,000 per month for PhD (~PKR 277,000 - 345,000 / month).",
                "amount": "JPY 144,000 - 180,000 / month (~PKR 275,000 - 345,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Prepaid economy-class flight tickets from Islamabad/Lahore/Karachi to Kansai International Airport (KIX) at the start and return ticket upon degree completion.",
                "amount": "100% covered round-trip economy flights (~JPY 250,000 value)"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese College Student Visa issued free of charge for MEXT scholars by the Embassy of Japan in Islamabad or Consulate in Karachi.",
                "amount": "100% free / waived"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Japanese National Health Insurance (NHI) premium (~JPY 2,000 / month) covers 70% of medical costs; Kobe University Student Co-op covers remaining co-pays.",
                "amount": "Subsidized NHI premium (~JPY 2,000 / month)"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of JPY 144,000 - 180,000; campus cafeterias provide halal meal options for JPY 450 - JPY 700.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to high-performance computing clusters, supercomputing infrastructure (access to RIKEN Fugaku facilities on Port Island), and research labs.",
                "amount": "100% covered by institutional infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor grants (JSPS KAKENHI) for presenting papers at international conferences in Japan and abroad.",
                "amount": "Up to JPY 200,000 / year upon supervisor approval"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Kobe municipal bus and train student discounts and direct campus transit links from Rokkomichi / Hankyu Rokko stations.",
                "amount": "Subsidized public transit access"
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single renowned Japanese national university: Kobe University (Shindai).",
            "participating_institutions": [
                "Kobe University (Rokkodai Campus, Kobe, Hyogo Prefecture, Japan)"
            ],
            "university_rankings_scope": "Top 10 national university in Japan; ranked top 350 globally in QS World University Rankings, globally renowned for Computational Science and High-Performance Computing (directly affiliated with the Fugaku Supercomputer project on Kobe Port Island).",
            "available_majors": [
                "Systems Science and Intelligent Systems",
                "Information Science and Artificial Intelligence",
                "Computational Science and Supercomputing",
                "Applied Mathematics and Data Informatics",
                "Bioinformatics and Medical Information Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for Master's; 3 years for PhD",
            "admission_requirements_summary": "Bachelor's degree in CS/EE/Math, minimum MEXT GPA 2.3/3.0, informal supervisor consent, statement of research proposal, two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "System Informatics laboratories collaborating with RIKEN on high-performance computing have high international demand; securing supervisor endorsement between September and November is the primary determinant of admission and funding.",
            "strategic_program_match_advice": "Browse the Kobe University Graduate School of System Informatics faculty directory (csi.kobe-u.ac.jp), find matching professors in computing/AI, and email a tailored research proposal and CV between September and November for the October intake."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://www.csi.kobe-u.ac.jp/english/ & http://www.kobe-u.ac.jp/en/admissions/",
            "portal_system_name": "Kobe University Graduate Admissions System",
            "account_creation_instructions": "Contact prospective supervisor directly via email, obtain formal letter of provisional acceptance, and submit the university-recommended MEXT / Honors fellowship application to the international student affairs office.",
            "step_by_step_workflow": [
                "Step 1: Identify research laboratories in Kobe University Graduate School of System Informatics matching your technical interests.",
                "Step 2: Email prospective supervisor with academic transcripts, CV, and a 2-3 page research proposal to obtain informal provisional acceptance (September - November).",
                "Step 3: Receive formal application documents from the student affairs section upon supervisor nomination.",
                "Step 4: Submit complete MEXT application dossier, attested transcripts, degrees, recommendation letters, and medical certificate by early January.",
                "Step 5: Faculty committee conducts technical screening and nominates top candidates to MEXT / university fellowship board in February.",
                "Step 6: Official award notification issued in June.",
                "Step 7: Arrive in Kobe in late September to commence studies in October."
            ],
            "university_vs_scholarship_routing": "Integrated Supervisor Track: Application is submitted through the supervising professor and graduate school directly.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by the Dean or Department Head of the Pakistani university.",
            "personal_statement_prompts": "Field of study and research plan outlining previous research experience and detailed thesis proposal for Kobe University.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "30 to 45-minute technical video interview via Zoom conducted by prospective supervisor and lab faculty members.",
            "standardized_tests": "IELTS Academic (min 6.5), TOEFL iBT (min 80), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "JPY 0 (100% waived for MEXT fellowship applicants)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Digital dossier submission followed by physical document dispatch to Kobe University."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum CGPA 3.3/4.0 and MEXT GPA 2.3/3.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "Field of Study and Research Plan (Kenkyu Keikakusho)",
                "mandatory": True,
                "specification": "Official MEXT formatted research proposal detailing background, methodology, and thesis timeline.",
                "pakistan_specific_instruction": "Must be closely aligned with prospective Kobe University supervisor's lab projects."
            },
            {
                "document_name": "Letter of Provisional Acceptance from Kobe University Professor",
                "mandatory": True,
                "specification": "Informal written consent from a professor agreeing to serve as academic supervisor.",
                "pakistan_specific_instruction": "Obtained directly through email academic correspondence."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "One letter from Dean or Head of Department; one from thesis advisor or senior professor.",
                "pakistan_specific_instruction": "Printed on official Pakistani university letterhead."
            },
            {
                "document_name": "English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5), TOEFL iBT (min 80), or institutional English MOI letter.",
                "pakistan_specific_instruction": "MOI letter signed by university registrar."
            },
            {
                "document_name": "Certificate of Health (MEXT Form)",
                "mandatory": True,
                "specification": "Official medical fitness certificate signed by an authorized physician.",
                "pakistan_specific_instruction": "Completed at an authorized diagnostic center."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of passport data page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1 (Supervisor outreach)",
            "application_deadline": "January 10 (Formal dossier submission)",
            "university_admission_deadline": "January 10",
            "document_submission_deadline": "January 15",
            "recommendation_letters_deadline": "January 10",
            "interview_period": "November - December",
            "shortlist_announcement": "Late February",
            "final_result_acceptance_deadline": "June",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Main intake for university-recommended MEXT track is October. Supervisor contact must begin 10 to 12 months in advance."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate GPA and performance in core computing and computational courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor match, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for Kobe University)",
            "recommendations_weight": "10% (Academic referee appraisals and Dean's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "Kobe University Faculty Admissions Board and Fellowship Committee.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty committee academic ranking."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~450 to 700 international applicants across System Informatics laboratories",
            "total_scholarships_awarded": "~35 to 50 fully funded positions awarded annually",
            "acceptance_rate_global": "~6% to 9%",
            "acceptance_rate_pakistan": "~8% to 12% among candidates with supervisor consent",
            "typical_successful_applicant_gpa": "CGPA 3.50+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates with exceptional computing foundations, strong software engineering practices, published research, or substantial GitHub project portfolios.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, China, Indonesia, Vietnam, Bangladesh, India, Egypt, Thailand.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed MEXT scholarships.",
                "Applications are processed exclusively through Kobe University faculty channels."
            ],
            "application_fee_warning": "Kobe University and MEXT do NOT charge application fees for scholarship nominees.",
            "agent_and_intermediary_warnings": "Kobe University does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "HEC and MOFA document attestations in Pakistan: ~PKR 25,000.",
                "Medical examination and chest X-ray on MEXT form: ~PKR 15,000.",
                "Initial pocket money before first stipend disbursement: ~JPY 50,000 (~PKR 95,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must know Japanese to study in Japan. Reality: Kobe University graduate computing programs are conducted 100% in English.",
                "Myth: Living in the Kansai area is prohibitively expensive. Reality: Kobe is significantly more affordable than Tokyo, with lower housing rents and living costs."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites claim GRE is mandatory; GRE is NOT mandatory for Kobe University System Informatics."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and MEXT GPA >= 2.3/3.0 throughout the degree program.",
            "attendance_requirements": "Full-time physical research attendance in the designated laboratory on Rokkodai Campus.",
            "academic_progress_monitoring": "Annual progress report submitted to the Graduate School Dean and MEXT.",
            "work_restrictions_during_study": "Permitted to work part-time up to 28 hours per week with immigration permission (Shikakugai Katsudo Kyoka), but supervisor consent required.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are free to work in Japan or globally.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Funding cancelled if the student abandons studies, is expelled, or engages in misconduct.",
            "rules_for_changing_university": "Non-transferable to other Japanese universities.",
            "rules_for_changing_major": "Requires consent of both current and prospective supervisors and faculty board approval.",
            "extension_policy": "Master's graduates can apply for MEXT extension to continue into the PhD program based on competitive research merit."
        },
        "official_sources_verified": [
            {
                "source_name": "Kobe University Graduate School of System Informatics Portal",
                "source_url": "http://www.csi.kobe-u.ac.jp/english/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Kobe University International Admissions Guide",
                "source_url": "http://www.kobe-u.ac.jp/en/admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-047": {
        "scholarship_id": "SCH-AS-047",
        "basic_details": {
            "scholarship_name": "Ajou University International Graduate Scholarship & Ajou AI Fellowship",
            "offering_entity": "Ajou University & South Korean Ministry of Education",
            "host_country": "South Korea",
            "host_institutions_covered": "Ajou University Suwon Campus (Suwon, Gyeonggi Province, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Department of Artificial Intelligence, Department of Computer Engineering, and Department of Software: Artificial Intelligence, Deep Learning, Autonomous Systems, Cybersecurity, Data Science, and Smart IoT.",
            "number_of_awards_total": "~100 to 150 full and partial tuition scholarships and lab research assistantships awarded annually across international cohorts",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~12 to 18 awards and lab assistantships annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (4 semesters) for Master of Science; up to 3 to 4 years for Doctor of Philosophy, renewed semester-by-semester subject to maintaining minimum 3.5/4.5 GPA",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "KRW 1,000,000 to KRW 1,500,000 / month (~PKR 205,000 - 310,000 / month from lab BK21/BK21 FOUR research funds)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students whose parents are both foreign nationals (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research capabilities.",
            "academic_qualifications": "A recognized 4-year Bachelor of Science / Engineering in Computer Science, Software Engineering, or related technical field (16 years education) with minimum CGPA 3.30 / 4.00 (or 75%+ aggregate) from an HEC-recognized university in Pakistan for Master's; research Master's degree (18 years education) for PhD.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum grade equivalent of Grade B+ or 75% marks across academic transcript.",
            "subject_background_prerequisites": "Rigorous undergraduate preparation in algorithms, data structures, machine learning, calculus, linear algebra, and programming (Python, C++).",
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
            "other_language_requirements": "Korean language proficiency (TOPIK) is not required for English-track STEM graduate degrees.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants should secure informal confirmation / research assistantship endorsement from an Ajou professor prior to admission submission.",
            "previous_scholarship_restrictions": "Cannot hold another full national government scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and entrance fee waiver at Ajou University covered under the Ajou International Fellowship / Professor Matching Grant.",
                "amount": "100% covered (~KRW 6,000,000 - 7,500,000 / semester value; ~PKR 2,500,000 - 3,100,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Ajou international graduate application fee of KRW 100,000 (~USD 75 / ~PKR 21,000) payable online.",
                "amount": "KRW 100,000 (~PKR 21,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory (Gwanggyo Hall) at Suwon Campus; rent is paid from the monthly lab research stipend.",
                "amount": "Subsidized rent ~KRW 300,000 - 450,000 / month (~PKR 62,000 - 93,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research assistantship stipend funded by lab research projects (BK21 FOUR / NRF): KRW 1,000,000 to KRW 1,300,000 per month for Master's; KRW 1,300,000 to KRW 1,500,000 per month for PhD (~PKR 205,000 - 310,000 / month).",
                "amount": "KRW 1,000,000 - 1,500,000 / month (~PKR 205,000 - 310,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare to Incheon/Seoul is arranged by the student; living allowance easily accommodates local savings.",
                "amount": "Self-funded economy flight (~PKR 180,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Korean D-2 Student Visa application fee (~PKR 15,000) at the Embassy of the Republic of Korea in Islamabad or Consulate in Karachi.",
                "amount": "PKR 15,000"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Mandatory Korean National Health Insurance (NHIS ~KRW 70,000 / month for international students) covered from lab research stipend.",
                "amount": "Covered via monthly research stipend"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of KRW 1,000,000 - 1,500,000; affordable campus cafeterias provide balanced meals for KRW 4,500 - 6,500.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Ajou Central Library, engineering laboratories, GPU workstations, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's BK21 FOUR and National Research Foundation (NRF) grants for presenting research at conferences.",
                "amount": "Up to KRW 2,000,000 for international conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Suwon public transport discounts and direct subway connection via Gwanggyo Jungang Station (Shinbundang Line, 30 mins to Gangnam, Seoul).",
                "amount": "Subsidized public transit access"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier South Korean technological university: Ajou University.",
            "participating_institutions": [
                "Ajou University (Suwon Campus, Gyeonggi Province, South Korea)"
            ],
            "university_rankings_scope": "Top 500 globally in QS World University Rankings, top 15 in South Korea, and renowned for AI, software engineering, and industry partnerships with Samsung Electronics (headquartered in Suwon).",
            "available_majors": [
                "Artificial Intelligence and Machine Learning",
                "Computer Engineering and Software Systems",
                "Cybersecurity and Digital Forensics",
                "Data Science and Big Data Analytics",
                "Intelligent Autonomous Vehicles and Robotics",
                "Electrical and Computer Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (4 semesters) for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor recommendation/endorsement, study plan (2 pages), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Ajou AI and Computer Engineering laboratories have heavy Samsung-funded R&D projects; securing supervisor endorsement between October and November or April and May is the primary determinant of admission and funding.",
            "strategic_program_match_advice": "Browse the Ajou Department of AI and Computer Engineering faculty directory (ai.ajou.ac.kr), find matching professors in AI/computing, and email a tailored research proposal and CV before submitting on the admission portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://grad-e.ajou.ac.kr/ & https://www.uwayapply.com/",
            "portal_system_name": "Uwayapply Online Application System & Ajou Graduate School Portal",
            "account_creation_instructions": "Contact prospective supervisor directly via email, obtain research endorsement, register on Uwayapply during the application window, submit online application, and mail physical attested documents to Ajou Graduate School.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research profiles on Ajou AI portal (https://ai.ajou.ac.kr/) and email prospective supervisors.",
                "Step 2: Obtain written endorsement / research assistantship commitment from the prospective supervisor.",
                "Step 3: Register and apply online on the Uwayapply portal (https://www.uwayapply.com/) during the open call (October - November for Spring / April - May for Fall).",
                "Step 4: Pay the application fee of KRW 100,000 online.",
                "Step 5: Send physical attested transcripts, degrees, recommendation letters, and bank statement to Ajou Graduate School in Suwon.",
                "Step 6: Attend faculty technical interview via Zoom if required.",
                "Step 7: Receive official Certificate of Admission (CoA), and apply for Korean D-2 visa."
            ],
            "university_vs_scholarship_routing": "Integrated Supervisor Track: Admission and tuition waiver are processed jointly with supervisor's research stipend endorsement.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by former academic professors or research supervisors.",
            "personal_statement_prompts": "Personal statement and study plan outlining academic background, technical capabilities, and postgraduate research vision.",
            "study_plan_research_proposal_requirements": "Structured 2 to 3-page research proposal detailing background, problem statement, research methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute technical interview via Zoom conducted by prospective supervisor and faculty panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI letter accepted; GRE not required.",
            "application_fee_amount": "KRW 100,000 (~USD 75 / ~PKR 21,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan, followed by Apostille or Consular Legalization at the Korean Embassy in Islamabad.",
            "translation_requirements": "Certified English or Korean translation required for all official documents.",
            "final_submission_method": "Online submission via Uwayapply followed by physical document dispatch to Ajou Suwon."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year Bachelor's (for MSc) or 18-year Master's (for PhD) with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan, with Korean Embassy consular legalization."
            },
            {
                "document_name": "Personal Statement and Study Plan",
                "mandatory": True,
                "specification": "2 to 3-page structured proposal outlining problem statement, methodology, and timeline.",
                "pakistan_specific_instruction": "Must be aligned with Ajou supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible Ajou professor agreeing to supervise and fund.",
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
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 80), or institutional English MOI letter.",
                "pakistan_specific_instruction": "MOI letter signed by university registrar."
            },
            {
                "document_name": "Bank Balance Certificate",
                "mandatory": True,
                "specification": "Bank statement showing minimum USD 20,000 (often waived or reduced with professor financial affidavit).",
                "pakistan_specific_instruction": "Bank certificate issued in English under applicant's or parents' name."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of all passport pages valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1 (for Spring intake) / April 1 (for Fall intake)",
            "application_deadline": "November 15 (Spring intake) / May 15 (Fall intake)",
            "university_admission_deadline": "November 15 / May 15",
            "document_submission_deadline": "November 25 / May 25",
            "recommendation_letters_deadline": "November 15 / May 15",
            "interview_period": "December / June",
            "shortlist_announcement": "Late December / Late June",
            "final_result_acceptance_deadline": "January / July",
            "visa_application_window": "January - February / July - August",
            "semester_commencement": "March 1 (Spring intake) / September 1 (Fall intake)",
            "annual_cycle_notes": "Admissions operate on two semester intakes: Spring (March commencement) and Fall (September commencement). Applying 3-4 months in advance is recommended."
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
            "selection_panel_composition": "Ajou Graduate School Admissions Committee and Department of AI Postgraduate Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty board academic review."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,000 to 1,500 international graduate applicants across Ajou",
            "total_scholarships_awarded": "~100 to 150 graduate scholarships and assistantships awarded annually",
            "acceptance_rate_global": "~8% to 12%",
            "acceptance_rate_pakistan": "~10% to 15% among candidates with supervisor consent",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, China, Vietnam, Bangladesh, India, Indonesia, Iran, Russia.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of educational agents claiming to provide 'guaranteed Ajou admissions or scholarship awards'.",
                "Applications are handled exclusively via the official Uwayapply portal and Ajou Graduate School (https://grad-e.ajou.ac.kr/)."
            ],
            "application_fee_warning": "Ajou application fee is KRW 100,000 paid directly on the Uway portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Ajou University does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "Ajou application fee: KRW 100,000 (~PKR 21,000).",
                "Korean Embassy legalization and attestations: ~PKR 35,000.",
                "Tuberculosis screening at authorized hospital: ~PKR 12,000.",
                "Initial pocket money before first stipend transfer: ~KRW 500,000 (~PKR 102,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must know Korean to study at Ajou. Reality: Ajou AI and Computer Engineering graduate programs are conducted 100% in English.",
                "Myth: Suwon is too far from Seoul. Reality: Suwon is part of the Seoul Capital Area, accessible in just 30 minutes by express subway."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state TOPIK is mandatory; TOPIK is NOT mandatory for English-track STEM graduate degrees at Ajou."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum GPA 3.50 / 4.50 each semester to renew the tuition fee waiver.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at Suwon Campus.",
            "academic_progress_monitoring": "Semi-annual progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "Part-time work permitted up to legal Korean immigration limits with university endorsement; research assistants fulfill lab obligations.",
            "home_country_return_obligation": "No return obligation; graduates are eligible for Korean post-study D-10 job seeker visas or point-based residence visas (F-2-7).",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 1-2 papers in SCIE-indexed journals prior to thesis defense.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails GPA maintenance or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Ajou University.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Graduate School Board.",
            "extension_policy": "Scholarship is granted for standard duration (2 years for Master's; 3-4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "Ajou University Graduate School Official Portal",
                "source_url": "https://grad-e.ajou.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Ajou Department of Artificial Intelligence",
                "source_url": "https://ai.ajou.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-048": {
        "scholarship_id": "SCH-AS-048",
        "basic_details": {
            "scholarship_name": "Universiti Tenaga Nasional (UNITEN) Postgraduate Excellence Award & BOLD Scholarship",
            "offering_entity": "Universiti Tenaga Nasional (UNITEN - The Energy University) & Tenaga Nasional Berhad (TNB)",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Tenaga Nasional Putrajaya Campus (Kajang, Selangor, Malaysia)",
            "degree_levels": ["Master of Information Technology (by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Computing and Informatics (CCI) & College of Engineering: Artificial Intelligence, Smart Energy Grids, Cybersecurity, Internet of Things, Cloud Computing, Renewable Energy Informatics, and Power Engineering.",
            "number_of_awards_total": "~60 to 90 BOLD Postgraduate Excellence Scholarships and Graduate Research Assistantships awarded annually",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing and smart grid engineering secure ~8 to 14 awards annually",
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
            "special_eligibility_categories": "Applicants must identify a prospective supervisor at UNITEN CCI and obtain preliminary consent.",
            "previous_scholarship_restrictions": "Cannot hold another full national or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and academic examination fee waiver at Universiti Tenaga Nasional covered by the BOLD scholarship or TNB research grant.",
                "amount": "100% covered (~MYR 16,000 - 24,000 / year value; ~PKR 1,040,000 - 1,560,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UNITEN international postgraduate application fee (~MYR 250 / USD 60) paid online via the portal.",
                "amount": "MYR 250 (~PKR 16,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus student residential apartments (Amanah / Cendekiawan) at UNITEN Putrajaya Campus; monthly rent is paid from the monthly living allowance.",
                "amount": "Subsidized rent ~MYR 380 - 600 / month (~PKR 25,000 - 39,000 / month)"
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
                "details": "Full access to UNITEN Library, smart grid computing laboratories, GPU clusters, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental research funding available through supervisor's TNB research grants for publishing in indexed journals.",
                "amount": "Up to MYR 3,500 for conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UNITEN campus shuttle bus service operating across all academic buildings and linking to nearby commuter train stations.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 15000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier energy and technological university: Universiti Tenaga Nasional (UNITEN).",
            "participating_institutions": [
                "Universiti Tenaga Nasional Putrajaya Campus (Kajang, Selangor, Malaysia)"
            ],
            "university_rankings_scope": "Top 150 in Asia (QS Asia University Rankings), renowned as Malaysia's premier specialized Energy University operated by Tenaga Nasional Berhad (TNB).",
            "available_majors": [
                "Master / PhD in Information Technology (Artificial Intelligence)",
                "Master / PhD in Information Technology (Cybersecurity & Smart Grids)",
                "Master / PhD in Information Technology (Data Science & IoT)",
                "Master / PhD in Software Engineering",
                "Master / PhD in Electrical Engineering and Renewable Energy Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree (minimum CGPA 3.3/4.0) for Master's; Master's degree (minimum CGPA 3.5/4.0) for PhD, supervisor consent, research proposal, two recommendation letters, and English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "UNITEN CCI AI and Smart Energy Grid laboratories have generous corporate and MOHE funding; reaching out to supervisors with active research grants is the primary path to guaranteed funding.",
            "strategic_program_match_advice": "Browse the UNITEN College of Computing and Informatics directory (uniten.edu.my/cci), identify matching research groups in AI/software, and email prospective professors attaching your CV and a 2-page research proposal before applying on the UNITEN postgraduate portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.uniten.edu.my/admission/postgraduate/ & https://apply.uniten.edu.my/",
            "portal_system_name": "UNITEN Online Postgraduate Application Portal",
            "account_creation_instructions": "Identify prospective supervisor on UNITEN portal, secure consent, register an applicant account on UNITEN Apply, submit degree application, and apply for the BOLD scholarship scheme.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research profiles on UNITEN CCI portal (https://www.uniten.edu.my/cci/).",
                "Step 2: Email prospective supervisor with academic transcripts, CV, and a 2-page research proposal to secure consent.",
                "Step 3: Register and apply online for postgraduate admission on the UNITEN Apply portal (https://apply.uniten.edu.my/).",
                "Step 4: Upload attested transcripts, degrees, research proposal, CV, and reference letters.",
                "Step 5: Apply for BOLD Postgraduate Scholarship scheme through the supervisor's endorsement.",
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
            "final_submission_method": "Online submission via UNITEN Apply admissions portal."
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
                "pakistan_specific_instruction": "Must be aligned with UNITEN supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible UNITEN professor agreeing to supervise.",
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
            "selection_panel_composition": "UNITEN College of Graduate Studies and College of Computing Postgraduate Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty board academic review."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~600 to 900 international applicants for UNITEN postgraduate programs",
            "total_scholarships_awarded": "~60 to 90 graduate research scholarships awarded annually",
            "acceptance_rate_global": "~9% to 13%",
            "acceptance_rate_pakistan": "~12% to 16% among candidates with supervisor consent",
            "typical_successful_applicant_gpa": "CGPA 3.40+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electrical engineering faculties.",
            "high_representation_countries": "Pakistan, Bangladesh, Nigeria, Indonesia, India, Yemen, Sudan.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of educational agents claiming to provide 'guaranteed UNITEN admissions or scholarship awards'.",
                "Applications are handled exclusively via the official UNITEN Apply portal (https://apply.uniten.edu.my/)."
            ],
            "application_fee_warning": "UNITEN application fee is MYR 250 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Universiti Tenaga Nasional does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "UNITEN application fee: MYR 250 (~PKR 16,000).",
                "EMGS visa approval letter (VAL) and medical fee: ~MYR 2,000 (~PKR 130,000).",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~MYR 1,500 (~PKR 98,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without a supervisor. Reality: Research Master's and PhD applications at UNITEN require prior engagement and consent from a qualified supervisor.",
                "Myth: Language of instruction is Malay. Reality: UNITEN postgraduate STEM programs are researched, written, and defended 100% in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state IELTS 6.5 is mandatory; UNITEN requires IELTS 6.0 or institutional English MOI letter for computing degrees."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress (Progress Report Grade Satisfactory) each semester.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at UNITEN Putrajaya.",
            "academic_progress_monitoring": "Semi-annual progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "GRA recipients may be assigned teaching assistantship or grading duties (up to 6 hours/week) within the faculty.",
            "home_country_return_obligation": "No return obligation; graduates are free to pursue postdocs or careers in Malaysia or worldwide.",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 1-2 papers in indexed journals prior to thesis submission.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails progress evaluations twice or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Universiti Tenaga Nasional.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Faculty Postgraduate Committee.",
            "extension_policy": "Scholarship is granted for standard duration (2 years for Master's; 3-4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "UNITEN College of Graduate Studies Scholarships Portal",
                "source_url": "https://www.uniten.edu.my/admission/postgraduate/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UNITEN Online Application Portal",
                "source_url": "https://apply.uniten.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
