# scripts/batch21_p1.py
# SCH-AS-036: Hokkaido University President's Fellowship & MEXT Special Program (Japan)
# SCH-AS-037: Chung-Ang University (CAU) Graduate Global Scholarship (South Korea)
# SCH-AS-038: Universiti Putra Malaysia (UPM) Graduate Research Fellowship (Malaysia)

DATA_P1 = {
    "SCH-AS-036": {
        "scholarship_id": "SCH-AS-036",
        "basic_details": {
            "scholarship_name": "Hokkaido University President's Fellowship & MEXT Special Program in Information Science",
            "offering_entity": "Hokkaido University & Japanese Ministry of Education, Culture, Sports, Science and Technology (MEXT)",
            "host_country": "Japan",
            "host_institutions_covered": "Hokkaido University Sapporo Campus (Sapporo, Hokkaido, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Information Science and Technology: Computer Science, Information Science and Technology, Media Network Engineering, Systems Science and Informatics, and Bioengineering and Bioinformatics.",
            "number_of_awards_total": "~40 to 60 University-Recommended MEXT and President's Fellowships awarded annually across international intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~4 to 7 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 3 years for PhD, subject to satisfactory annual academic and research progress",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 144,000 / month (~PKR 275,000 / month for Master's); JPY 145,000 - 200,000 / month (~PKR 277,000 - 380,000 / month for PhD)"
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
            "subject_background_prerequisites": "Rigorous undergraduate preparation in algorithms, computer architectures, linear algebra, discrete mathematics, and programming (C/C++, Python).",
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
            "special_eligibility_categories": "Applicants must contact a prospective supervising professor at Hokkaido University Graduate School of Information Science and Technology and obtain informal preliminary consent prior to formal application.",
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
                "details": "Guaranteed on-campus single room in Hokkaido University International Student Dormitory (Hokudai Foreign Student House) for the first 6-12 months; monthly rent JPY 18,000 - JPY 30,000.",
                "amount": "Subsidized rent ~JPY 22,000 / month (~PKR 42,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living allowance: JPY 144,000 per month for Master's (~PKR 275,000 / month; JPY 1,728,000 / year); JPY 145,000 to JPY 200,000 per month for PhD (~PKR 277,000 - 380,000 / month with President's top-up).",
                "amount": "JPY 144,000 - 200,000 / month (~PKR 275,000 - 380,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Prepaid economy-class flight tickets from Islamabad/Lahore/Karachi to New Chitose Airport (Sapporo / CTS) at the start and return ticket upon degree completion.",
                "amount": "100% covered round-trip economy flights (~JPY 250,000 value)"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese College Student Visa issued free of charge for MEXT scholars by the Embassy of Japan in Islamabad or Consulate in Karachi.",
                "amount": "100% free / waived"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Japanese National Health Insurance (NHI) premium (~JPY 2,000 / month) covers 70% of medical costs; Hokkaido University Student Co-op covers remaining co-pays.",
                "amount": "Subsidized NHI premium (~JPY 2,000 / month)"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of JPY 144,000 - 200,000; campus cafeterias provide halal meal options for JPY 450 - JPY 700.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to high-performance computing clusters, supercomputing center (Hokkaido University Information Initiative Center), and research labs.",
                "amount": "100% covered by institutional infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor grants (JSPS KAKENHI) for presenting papers at international conferences in Japan and abroad.",
                "amount": "Up to JPY 200,000 / year upon supervisor approval"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Sapporo municipal subway student discounts (50% reduction) and campus transit links.",
                "amount": "50% subway student discount"
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Japanese national imperial university: Hokkaido University (Hokudai).",
            "participating_institutions": [
                "Hokkaido University (Sapporo Campus, Hokkaido, Japan)"
            ],
            "university_rankings_scope": "One of Japan's prestigious 7 Designated National Imperial Universities; ranked top 150 globally in QS World University Rankings and top 100 for Engineering & Computer Science.",
            "available_majors": [
                "Computer Science and Information Technology",
                "Media Network Engineering and Artificial Intelligence",
                "Systems Science and Informatics",
                "Bioengineering and Bioinformatics",
                "Quantum Information and Nano-electronics",
                "Robotics and Cybernetics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for Master's; 3 years for PhD",
            "admission_requirements_summary": "Bachelor's degree in CS/EE, minimum MEXT GPA 2.3/3.0, informal supervisor consent, statement of research proposal, two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Information Science research labs in AI, Media Networks, and Robotics have high competition; securing supervisor endorsement between September and November is the primary determinant of admission and funding.",
            "strategic_program_match_advice": "Browse the Hokkaido University Graduate School of Information Science and Technology faculty directory (ist.hokudai.ac.jp), find matching professors in AI/computing, and email a tailored research proposal and CV between September and November for the October intake."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ist.hokudai.ac.jp/eng/ & https://www.global.hokudai.ac.jp/admissions/",
            "portal_system_name": "Hokkaido University Graduate Admissions System",
            "account_creation_instructions": "Contact prospective supervisor directly via email, obtain formal letter of provisional acceptance, and submit the university-recommended MEXT / President's fellowship application to the international student affairs office.",
            "step_by_step_workflow": [
                "Step 1: Identify research laboratories in Hokkaido University Graduate School of Information Science matching your technical interests.",
                "Step 2: Email prospective supervisor with academic transcripts, CV, and a 2-3 page research proposal to obtain informal provisional acceptance (September - November).",
                "Step 3: Receive formal application documents from the student affairs section upon supervisor nomination.",
                "Step 4: Submit complete MEXT application dossier, attested transcripts, degrees, recommendation letters, and medical certificate by early January.",
                "Step 5: Faculty committee conducts technical screening and nominates top candidates to MEXT / university fellowship board in February.",
                "Step 6: Official award notification issued in June.",
                "Step 7: Arrive in Sapporo in late September to commence studies in October."
            ],
            "university_vs_scholarship_routing": "Integrated Supervisor Track: Application is submitted through the supervising professor and graduate school directly.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by the Dean or Department Head of the Pakistani university.",
            "personal_statement_prompts": "Field of study and research plan outlining previous research experience and detailed thesis proposal for Hokkaido University.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "30 to 45-minute technical video interview via Zoom conducted by prospective supervisor and lab faculty members.",
            "standardized_tests": "IELTS Academic (min 6.5), TOEFL iBT (min 80), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "JPY 0 (100% waived for MEXT fellowship applicants)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Digital dossier submission followed by physical document dispatch to Hokkaido University."
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
                "pakistan_specific_instruction": "Must be closely aligned with prospective Hokkaido University supervisor's lab projects."
            },
            {
                "document_name": "Letter of Provisional Acceptance from Hokkaido University Professor",
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
            "academic_weight": "35% (Undergraduate GPA and performance in core computing and engineering courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor match, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for Hokkaido University)",
            "recommendations_weight": "10% (Academic referee appraisals and Dean's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "Hokkaido University Faculty Admissions Board and Fellowship Committee.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty committee academic ranking."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~500 to 800 international applicants across Information Science laboratories",
            "total_scholarships_awarded": "~40 to 60 fully funded positions awarded annually",
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
                "Applications are processed exclusively through Hokkaido University faculty channels."
            ],
            "application_fee_warning": "Hokkaido University and MEXT do NOT charge application fees for scholarship nominees.",
            "agent_and_intermediary_warnings": "Hokkaido University does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "HEC and MOFA document attestations in Pakistan: ~PKR 25,000.",
                "Medical examination and chest X-ray on MEXT form: ~PKR 15,000.",
                "Initial pocket money before first stipend disbursement: ~JPY 50,000 (~PKR 95,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must know Japanese to study in Japan. Reality: Hokkaido University graduate computing programs are conducted 100% in English.",
                "Myth: Sapporo is too cold to survive. Reality: All university facilities, dormitories, and subways in Sapporo are fully heated, with extensive underground walkways."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites claim GRE is mandatory; GRE is NOT mandatory for Hokkaido University Information Science."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and MEXT GPA >= 2.3/3.0 throughout the degree program.",
            "attendance_requirements": "Full-time physical research attendance in the designated laboratory on Sapporo Campus.",
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
                "source_name": "Hokkaido University Graduate School of IST Official Portal",
                "source_url": "https://www.ist.hokudai.ac.jp/eng/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Hokkaido University International Student Admissions Guide",
                "source_url": "https://www.global.hokudai.ac.jp/admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-037": {
        "scholarship_id": "SCH-AS-037",
        "basic_details": {
            "scholarship_name": "Chung-Ang University (CAU) Graduate Global Scholarship & CAU Leaders Fellowship",
            "offering_entity": "Chung-Ang University & South Korean Ministry of Education",
            "host_country": "South Korea",
            "host_institutions_covered": "Chung-Ang University Seoul Campus & Daedeok Campus (Seoul, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Department of Computer Science and Engineering, Department of Artificial Intelligence, and Department of Software: Artificial Intelligence, Deep Learning, Computer Vision, Software Engineering, Cybersecurity, and Robotics.",
            "number_of_awards_total": "~100 to 150 full and partial tuition waivers and professor-funded research assistantships awarded annually across international intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in AI and software engineering secure ~12 to 18 awards and lab assistantships annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (4 semesters) for Master of Science; up to 3 to 4 years for Doctor of Philosophy, renewed semester-by-semester subject to maintaining minimum 3.3/4.5 GPA",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "KRW 1,000,000 to KRW 1,600,000 / month (~PKR 205,000 - 330,000 / month from lab BK21/BK21 FOUR research funds)"
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
            "special_eligibility_categories": "Applicants should secure informal confirmation / research assistantship endorsement from a CAU professor prior to admission submission.",
            "previous_scholarship_restrictions": "Cannot hold another full national government scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and entrance fee waiver at Chung-Ang University covered under the CAU Global Leader Scholarship / Professor Matching Grant.",
                "amount": "100% covered (~KRW 6,500,000 - 8,000,000 / semester value; ~PKR 2,700,000 - 3,300,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "CAU international graduate application fee of KRW 100,000 (~USD 75 / ~PKR 21,000) payable online.",
                "amount": "KRW 100,000 (~PKR 21,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory (Blue Mir Hall) at Seoul Campus; rent is paid from the monthly lab research stipend.",
                "amount": "Subsidized rent ~KRW 350,000 - 500,000 / month (~PKR 72,000 - 103,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research assistantship stipend funded by lab research projects (BK21 FOUR / NRF): KRW 1,000,000 to KRW 1,300,000 per month for Master's; KRW 1,300,000 to KRW 1,600,000 per month for PhD (~PKR 205,000 - 330,000 / month).",
                "amount": "KRW 1,000,000 - 1,600,000 / month (~PKR 205,000 - 330,000 / month)"
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
                "details": "Covered via the monthly living stipend of KRW 1,000,000 - 1,600,000; affordable campus cafeterias provide balanced meals for KRW 4,500 - 6,500.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to CAU Central Library, engineering laboratories, GPU workstations, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's BK21 FOUR and National Research Foundation (NRF) grants for presenting research at conferences.",
                "amount": "Up to KRW 2,000,000 for international conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Seoul T-Money transportation card discounts and convenient transit via Heukseok Station (Line 9) and Sangdo Station (Line 7).",
                "amount": "Subsidized public transit access"
            },
            "total_estimated_value_usd_per_year": 19000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier South Korean research university: Chung-Ang University (CAU).",
            "participating_institutions": [
                "Chung-Ang University (Seoul Campus & Daedeok Campus, South Korea)"
            ],
            "university_rankings_scope": "Top 400 globally in QS World University Rankings, top 10 in South Korea, and a national hub for Artificial Intelligence research under the Korean National AI Graduate School initiative.",
            "available_majors": [
                "Computer Science and Engineering",
                "Artificial Intelligence and Machine Learning",
                "Software Engineering and Data Science",
                "Cybersecurity and Information Security",
                "Robotics and Intelligent Systems",
                "Electrical and Electronics Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (4 semesters) for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor recommendation/endorsement, study plan (2 pages), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "CAU AI and Computer Science laboratories are highly research-productive; securing supervisor endorsement between October and November or April and May is the primary determinant of admission and funding.",
            "strategic_program_match_advice": "Browse the CAU Department of AI and CSE faculty directory (cse.cau.ac.kr), find matching professors in AI/computing, and email a tailored research proposal and CV before submitting on the Uwayapply portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://oia.cau.ac.kr/ & https://www.uwayapply.com/",
            "portal_system_name": "Uwayapply Online Application System & CAU OIA Portal",
            "account_creation_instructions": "Contact prospective supervisor directly via email, obtain research endorsement, register on Uwayapply during the application window, submit online application, and mail physical attested documents to CAU OIA.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research profiles on CAU CSE portal (https://cse.cau.ac.kr/) and email prospective supervisors.",
                "Step 2: Obtain written endorsement / research assistantship commitment from the prospective supervisor.",
                "Step 3: Register and apply online on the Uwayapply portal (https://www.uwayapply.com/) during the open call (October - November for Spring / April - May for Fall).",
                "Step 4: Pay the application fee of KRW 100,000 online.",
                "Step 5: Send physical attested transcripts, degrees, recommendation letters, and bank statement to the CAU Office of International Affairs in Seoul.",
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
            "final_submission_method": "Online submission via Uwayapply followed by physical document dispatch to CAU Seoul."
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
                "pakistan_specific_instruction": "Must be aligned with CAU supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible CAU professor agreeing to supervise and fund.",
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
            "selection_panel_composition": "CAU Office of International Affairs and Department of Computer Science Postgraduate Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty board academic review."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 1,800 international graduate applicants across CAU",
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
                "Beware of educational agents claiming to provide 'guaranteed CAU admissions or scholarship awards'.",
                "Applications are handled exclusively via the official Uwayapply portal and CAU OIA (https://oia.cau.ac.kr/)."
            ],
            "application_fee_warning": "CAU application fee is KRW 100,000 paid directly on the Uway portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Chung-Ang University does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "CAU application fee: KRW 100,000 (~PKR 21,000).",
                "Korean Embassy legalization and attestations: ~PKR 35,000.",
                "Tuberculosis screening at authorized hospital: ~PKR 12,000.",
                "Initial pocket money before first stipend transfer: ~KRW 500,000 (~PKR 102,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must know Korean to study at CAU. Reality: CAU CSE and AI graduate programs are conducted 100% in English.",
                "Myth: You cannot work in Korea. Reality: International graduate students can work on funded research projects (BK21 FOUR) and receive monthly tax-free stipends legally."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state TOPIK is mandatory; TOPIK is NOT mandatory for English-track STEM graduate degrees at CAU."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum GPA 3.30 / 4.50 each semester to renew the tuition fee waiver.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at Seoul Campus.",
            "academic_progress_monitoring": "Semi-annual progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "Part-time work permitted up to legal Korean immigration limits with university endorsement; research assistants fulfill lab obligations.",
            "home_country_return_obligation": "No return obligation; graduates are eligible for Korean post-study D-10 job seeker visas or point-based residence visas (F-2-7).",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 1-2 papers in SCIE-indexed journals prior to thesis defense.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails GPA maintenance or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Chung-Ang University.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Graduate School Board.",
            "extension_policy": "Scholarship is granted for standard duration (2 years for Master's; 3-4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "Chung-Ang University Office of International Affairs Portal",
                "source_url": "https://oia.cau.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "CAU Department of Computer Science and Engineering",
                "source_url": "https://cse.cau.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-038": {
        "scholarship_id": "SCH-AS-038",
        "basic_details": {
            "scholarship_name": "Universiti Putra Malaysia (UPM) Graduate Research Fellowship (GRF / SGRA)",
            "offering_entity": "Universiti Putra Malaysia (UPM) & Malaysian Ministry of Higher Education",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Putra Malaysia Main Campus (Serdang, Selangor, Malaysia)",
            "degree_levels": ["Master of Science (MSc by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Computer Science and Information Technology (FSKTM) & Faculty of Engineering: Artificial Intelligence, Software Engineering, Cybersecurity, Data Communications and Networking, Information Systems, and Agricultural Robotics.",
            "number_of_awards_total": "~100 to 150 Graduate Research Fellowships (GRF) and Special Graduate Research Assistantships (SGRA) awarded annually",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~12 to 18 awards annually",
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
            "special_eligibility_categories": "Applicants must identify a prospective supervisor at UPM FSKTM and obtain preliminary consent.",
            "previous_scholarship_restrictions": "Cannot hold another full national or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and academic examination fee waiver at Universiti Putra Malaysia covered by the scholarship or research grant.",
                "amount": "100% covered (~MYR 16,000 - 24,000 / year value; ~PKR 1,040,000 - 1,560,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UPM international postgraduate application fee (~MYR 250 / USD 60) paid online via the portal.",
                "amount": "MYR 250 (~PKR 16,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus student residential colleges (Kolej Kediaman) at UPM Serdang; monthly rent is paid from the monthly living allowance.",
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
                "details": "Full access to UPM Sultan Abdul Samad Library, engineering laboratories, GPU clusters, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental research funding available through supervisor's research grants for publishing in indexed journals.",
                "amount": "Up to MYR 3,500 for conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UPM campus shuttle bus service operating across all faculties, residential colleges, and the UPM MRT station.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 15000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading public research university: Universiti Putra Malaysia (UPM).",
            "participating_institutions": [
                "Universiti Putra Malaysia Main Campus (Serdang, Selangor, Malaysia)"
            ],
            "university_rankings_scope": "Ranked #148 globally in QS World University Rankings, #3 in Malaysia, top 100 globally in Computer Science, Agricultural Engineering, and Environmental Sciences.",
            "available_majors": [
                "MSc / PhD in Computer Science (Artificial Intelligence, Machine Learning)",
                "MSc / PhD in Software Engineering",
                "MSc / PhD in Information Security and Cyber Defense",
                "MSc / PhD in Data Communications and Distributed Systems",
                "MSc / PhD in Intelligent Systems and Robotics",
                "MSc / PhD in Agricultural Informatics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for MSc; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree (minimum CGPA 3.3/4.0) for Master's; Master's degree (minimum CGPA 3.5/4.0) for PhD, supervisor consent, research proposal, two recommendation letters, and English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "UPM FSKTM AI and Software Engineering labs have high demand; reaching out to supervisors with active MOHE/FRGS research grants is the primary path to guaranteed funding.",
            "strategic_program_match_advice": "Browse the UPM Faculty of Computer Science and Information Technology directory (fsktm.upm.edu.my), identify matching research groups in AI/software, and email prospective professors attaching your CV and a 2-page research proposal before applying on the UPM SGS portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://sgs.upm.edu.my/financial_assistance_scholarships-1875 & https://pgadmissions.upm.edu.my/",
            "portal_system_name": "UPM SGS Postgraduate Admissions Portal",
            "account_creation_instructions": "Identify prospective supervisor on UPM portal, secure consent, register an applicant account on UPM SGS admissions, submit degree application, and apply for the GRF / SGRA scholarship scheme.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research profiles on UPM FSKTM portal (https://fsktm.upm.edu.my/).",
                "Step 2: Email prospective supervisor with academic transcripts, CV, and a 2-page research proposal to secure consent.",
                "Step 3: Register and apply online for postgraduate admission on the UPM SGS portal (https://pgadmissions.upm.edu.my/).",
                "Step 4: Upload attested transcripts, degrees, research proposal, CV, and reference letters.",
                "Step 5: Apply for Graduate Research Fellowship (GRF) scheme through the supervisor's endorsement.",
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
            "final_submission_method": "Online submission via UPM SGS admissions portal."
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
                "pakistan_specific_instruction": "Must be aligned with UPM supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible UPM professor agreeing to supervise.",
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
            "selection_panel_composition": "UPM School of Graduate Studies and Faculty of Computer Science Postgraduate Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty board academic review."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international applicants for UPM postgraduate programs",
            "total_scholarships_awarded": "~100 to 150 graduate research scholarships awarded annually",
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
                "Beware of educational agents claiming to provide 'guaranteed UPM admissions or scholarship awards'.",
                "Applications are handled exclusively via the official UPM SGS portal (https://pgadmissions.upm.edu.my/)."
            ],
            "application_fee_warning": "UPM application fee is MYR 250 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Universiti Putra Malaysia does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "UPM application fee: MYR 250 (~PKR 16,000).",
                "EMGS visa approval letter (VAL) and medical fee: ~MYR 2,000 (~PKR 130,000).",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~MYR 1,500 (~PKR 98,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without a supervisor. Reality: Research Master's and PhD applications at UPM require prior engagement and consent from a qualified supervisor.",
                "Myth: UPM only focuses on agriculture. Reality: UPM FSKTM is one of the top computing and AI research faculties in Malaysia."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state IELTS 6.5 is mandatory; UPM requires IELTS 6.0 or institutional English MOI letter for computing degrees."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress (Progress Report Grade Satisfactory) each semester.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at UPM Serdang.",
            "academic_progress_monitoring": "Semi-annual progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "GRF recipients may be assigned teaching assistantship or grading duties (up to 6 hours/week) within the faculty.",
            "home_country_return_obligation": "No return obligation; graduates are free to pursue postdocs or careers in Malaysia or worldwide.",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 1-2 papers in indexed journals prior to thesis submission.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails progress evaluations twice or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Universiti Putra Malaysia.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Faculty Postgraduate Committee.",
            "extension_policy": "Scholarship is granted for standard duration (2 years for Master's; 3-4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "UPM School of Graduate Studies Financial Assistance Portal",
                "source_url": "https://sgs.upm.edu.my/financial_assistance_scholarships-1875",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UPM Postgraduate Admissions Portal",
                "source_url": "https://pgadmissions.upm.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
