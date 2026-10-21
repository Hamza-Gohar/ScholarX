"""Batch 25 Part 2: East Asia & Malaysia Postgraduate Awards (3 awards)
SCH-AS-053: Universiti Malaysia Pahang Al-Sultan Abdullah (UMPSA) Graduate Research Scheme (GRS)
SCH-AS-054: Tongji University Chinese Government Scholarship & Shanghai Municipal Award
SCH-AS-055: University of Tsukuba MEXT Special Recommendation Science & Technology Award
"""

DATA_P2 = {
    "SCH-AS-053": {
        "scholarship_id": "SCH-AS-053",
        "basic_details": {
            "scholarship_name": "Universiti Malaysia Pahang Al-Sultan Abdullah (UMPSA) Graduate Research Scheme (GRS)",
            "offering_entity": "Universiti Malaysia Pahang Al-Sultan Abdullah (UMPSA) Institute of Postgraduate Studies (IPS)",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Malaysia Pahang Al-Sultan Abdullah (UMPSA Gambang and Pekan Campuses, Pahang, Malaysia)",
            "degree_levels": ["Master of Science (by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Chemical and Process Engineering Technology, Faculty of Mechanical and Automotive Engineering Technology, Faculty of Computing, Faculty of Civil Engineering Technology, Faculty of Electrical and Electronics Engineering Technology, and Faculty of Industrial Sciences and Technology.",
            "number_of_awards_total": "~120 to 160 graduate research scheme positions awarded across academic semesters",
            "number_of_awards_pakistan": "Open internationally; typically 15 to 25 Pakistani engineering and computing researchers receive GRS appointments annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 24 months for Master's by research; up to 36 months for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "RM 1,800 to RM 2,300 / month for PhD (~PKR 117,000 to 149,500 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month) plus full tuition fee waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to all nationalities including Malaysian citizens and international candidates (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Maximum 35 years for Master's applicants; maximum 40 years for PhD applicants at time of appointment.",
            "academic_qualifications": "Recognized Bachelor's degree with minimum CGPA 3.00/4.00 or First Class equivalent for Master's; recognized Master's degree by research or coursework with minimum CGPA 3.00/4.00 for PhD from an HEC-recognized institution.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum CGPA 3.00 / 4.00; competitive candidates typically possess CGPA >= 3.40 / 4.00 with laboratory instrumentation experience.",
            "subject_background_prerequisites": "Engineering, computer science, software engineering, biotechnology, chemical technology, materials science, or related technical disciplines.",
            "current_education_status": "Graduated or final-semester students expecting degree completion prior to semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Laboratory research experience, programming aptitude, or prior indexed journal publications considered a decisive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 80, MUET Band 4.0, or recognized English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "None; Malay language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure endorsement and laboratory placement from an active UMPSA principal investigator holding research grant funding (FRGS, PRGS, or industrial contracts).",
            "previous_scholarship_restrictions": "Cannot hold any concurrent national scholarship, industrial sponsorship, or full-time paid employment.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for eligible postgraduate research semesters covered under the UMPSA Graduate Research Scheme.",
                "amount": "100% covered (~RM 12,000 to 18,000 / year value; ~PKR 780,000 to 1,170,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UMPSA international postgraduate application fee of RM 150 paid during online portal submission.",
                "amount": "RM 150 (~PKR 9,800)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate residential housing available at subsidized monthly rates (approx. RM 200 to 350 / month), easily covered from stipend.",
                "amount": "Subsidized university hostel housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research assistantship allowance paid directly: RM 1,800 to RM 2,300 / month for PhD (~PKR 117,000 to 149,500 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month).",
                "amount": "RM 1,300 to RM 2,300 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Kuala Lumpur / Kuantan is self-funded.",
                "amount": "Not covered in central GRS scheme"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "EMGS (Education Malaysia Global Services) visa processing and Malaysian Student Pass fees paid by candidate.",
                "amount": "Approx. RM 2,000 to 2,500 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Malaysian student medical and hospitalization insurance provided via EMGS student pass registration package.",
                "amount": "100% covered student medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Campus cafeterias at Gambang and Pekan provide affordable dining; daily meals cost approximately RM 15 to 25.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to UMPSA Central Library, IEEE Xplore, ScienceDirect, laboratory analytical equipment, and chemical reagents supported through supervisor grant.",
                "amount": "100% covered laboratory and computational access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference attendance and publication charges (APC) for high-impact Scopus/WoS Q1/Q2 journals funded directly from host research grant.",
                "amount": "Grant-funded conference travel and APC charges"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle transportation between residential colleges and academic faculties at Gambang and Pekan.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 12000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Malaysian premier technical university (Universiti Malaysia Pahang Al-Sultan Abdullah - MTUN member).",
            "participating_institutions": [
                "Universiti Malaysia Pahang Al-Sultan Abdullah (Pekan and Gambang Campuses, Pahang, Malaysia)"
            ],
            "university_rankings_scope": "QS World University Rankings #751-800, Top 150 in Asia; recognized as one of Malaysia's premier technical universities (MTUN) renowned for engineering technology and industrial partnerships.",
            "available_majors": [
                "Master of Science / PhD in Chemical Engineering",
                "Master of Science / PhD in Mechanical Engineering",
                "Master of Science / PhD in Automotive Engineering",
                "Master of Science / PhD in Electrical and Electronics Engineering",
                "Master of Science / PhD in Civil Engineering",
                "Master of Science / PhD in Computer Science & Software Engineering",
                "Master of Science / PhD in Industrial Chemistry and Biotechnology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's by Research: 1.5 to 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree in engineering or computing with CGPA 3.00+, academic transcripts, research proposal, supervisor endorsement form, two reference letters, and IELTS 6.0 / TOEFL 80 or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "High competition in Faculty of Computing and Faculty of Chemical Engineering; securing supervisor agreement with active grant funding is the single most critical factor.",
            "strategic_program_match_advice": "Examine UMPSA faculty directory, identify principal investigators with active Fundamental Research Grant Scheme (FRGS) or industrial projects in battery tech, AI, or green chemical processing, and submit a tailored research synopsis."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://ips.umpsa.edu.my/online-application",
            "portal_system_name": "UMPSA Institute of Postgraduate Studies (IPS) Online Portal",
            "account_creation_instructions": "Register on the UMPSA IPS portal, complete the online postgraduate admission form, upload academic credentials and supervisor endorsement form, and pay the RM 150 application fee.",
            "step_by_step_workflow": [
                "Step 1: Browse UMPSA research groups and reach out to prospective supervisors with CV and research draft.",
                "Step 2: Obtain signed UMPSA Supervisor Acceptance and GRS Recommendation Form.",
                "Step 3: Submit online admission application via IPS portal and select Graduate Research Scheme (GRS) funding option.",
                "Step 4: Upload attested academic documents, research proposal, passport copy, and English proof.",
                "Step 5: Faculty Graduate Committee conducts technical interview and evaluates project alignment.",
                "Step 6: IPS issues official Letter of Offer and GRS Appointment Letter.",
                "Step 7: Apply for EMGS Visa Approval Letter (VAL) and Single Entry Visa (SEV) at Malaysian High Commission in Islamabad.",
                "Step 8: Arrive in Malaysia, complete medical screening, finalize student pass, and matriculate."
            ],
            "university_vs_scholarship_routing": "Integrated departmental route: Application for admission and GRS award are evaluated concurrently by the host faculty and IPS.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed PDF recommendation letters on official university letterheads.",
            "personal_statement_prompts": "Statement of research intent detailing technical competencies, publication aspirations, and relevance to the supervisor's funded research grant.",
            "study_plan_research_proposal_requirements": "5 to 8 page structured research proposal covering problem statement, literature review, methodology, equipment needs, and milestone schedule.",
            "cv_format_requirements": "Academic CV detailing qualifications, laboratory capabilities, programming proficiencies, and publications list.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical video interview via MS Teams or Google Meet conducted by prospective supervisor and departmental postgraduate coordinator.",
            "standardized_tests": "IELTS 6.0+, TOEFL 80+, MUET Band 4.0, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "RM 150 (approx. USD 35 / ~PKR 9,800)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani credentials during EMGS processing.",
            "translation_requirements": "Certified English translations for all non-English documents.",
            "final_submission_method": "Online submission via UMPSA IPS postgraduate admission portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Official Bachelor's / Master's degree certificates and complete semester transcripts with CGPA >= 3.00.",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "Technical Research Proposal",
                "mandatory": True,
                "specification": "Structured research proposal (5-8 pages) aligned with supervisor's research grant objectives.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Supervisor Acceptance & GRS Endorsement Form",
                "mandatory": True,
                "specification": "Official UMPSA form signed by prospective supervisor confirming laboratory placement and willingness to supervise.",
                "pakistan_specific_instruction": "Obtained directly from UMPSA faculty supervisor."
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential evaluation letters from previous university professors or department heads.",
                "pakistan_specific_instruction": "On institutional letterhead with official stamps."
            },
            {
                "document_name": "English Language Proficiency Proof",
                "mandatory": True,
                "specification": "IELTS 6.0+, TOEFL iBT 80+, MUET Band 4.0, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate from previous university accepted."
            },
            {
                "document_name": "International Passport Bio-data Page",
                "mandatory": True,
                "specification": "Full clear color scan of passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "March 1 (Semester I) / October 1 (Semester II)",
            "application_deadline": "June 30 (Semester I - September) / November 30 (Semester II - February)",
            "university_admission_deadline": "June 30 / November 30",
            "document_submission_deadline": "June 30 / November 30",
            "recommendation_letters_deadline": "June 30 / November 30",
            "interview_period": "July - August / December - January",
            "shortlist_announcement": "Late August / Mid January",
            "final_result_acceptance_deadline": "Within 2 weeks of offer issuance",
            "visa_application_window": "August / January via EMGS",
            "semester_commencement": "September (Semester I) / February (Semester II)",
            "annual_cycle_notes": "Bi-annual intake cycles: Semester I in September and Semester II in February."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic performance, and foundational engineering coursework)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and professional leadership)",
            "research_experience_weight": "35% (Prior publications, technical proposal rigor, and supervisor grant synergy)",
            "work_experience_weight": "5% (Industrial engineering or laboratory technical experience)",
            "personal_statement_weight": "5% (Clarity of purpose and research dedication)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit and research capability based)",
            "selection_panel_composition": "Faculty Postgraduate Committee, Dean of Institute of Postgraduate Studies, and Principal Investigator of host research project.",
            "evaluation_methodology": "Two-stage evaluation: departmental technical vetting of research alignment followed by central IPS award confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~900 to 1,200 applicants across both semesters",
            "total_scholarships_awarded": "~120 to 160 GRS awards annually",
            "acceptance_rate_global": "~13% to 15%",
            "acceptance_rate_pakistan": "~18% to 22% for applicants with pre-secured supervisor endorsement and CGPA >= 3.30",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.30 / 4.00, coupled with prior lab project experience or publications",
            "typical_academic_and_research_profile": "Graduates in engineering or computing with strong programming or laboratory skills, clear research plan, and pre-negotiated supervisor endorsement.",
            "common_backgrounds_of_winners": "Graduates from Pakistani engineering institutions (NUST, UET Lahore, UET Taxila, FAST-NUCES, COMSATS, NED Karachi).",
            "high_representation_countries": "Malaysia, Pakistan, Indonesia, Nigeria, Yemen, Bangladesh, Egypt.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal ips.umpsa.edu.my.",
                "Do not pay money to educational agents promising guaranteed GRS appointments; GRS awards depend entirely on faculty supervisor endorsement."
            ],
            "application_fee_warning": "University application fee is RM 150 paid directly to UMPSA via secure online payment.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are flagged and rejected; applicants must write their own technical research proposal.",
            "hidden_costs_breakdown": [
                "UMPSA application fee: RM 150 (~PKR 9,800).",
                "EMGS visa approval and student pass fees: ~RM 2,200 to 2,500 (~PKR 143,000 to 162,500).",
                "HEC and MoFA document attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "One-way flight to Kuala Lumpur: ~PKR 90,000 to 130,000.",
                "Initial living deposit before first stipend cycle: ~RM 1,000 (~PKR 65,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: GRS covers international travel. Reality: International travel and EMGS visa fees are self-funded.",
                "Myth: You can apply without contacting a supervisor. Reality: Supervisor endorsement is effectively mandatory for GRS scheme approval."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRS is purely a tuition waiver; in reality, GRS includes both full tuition waiver and monthly living stipend."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum CGPA 3.00 and Satisfactory (TM - Teruskan Memuaskan) research progress evaluation every semester.",
            "attendance_requirements": "Full-time physical research presence at UMPSA Gambang or Pekan campus; scholars may be assigned up to 6 hours/week of laboratory or tutorial teaching assistance.",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by supervisor and presented to Faculty Postgraduate Committee.",
            "work_restrictions_during_study": "Recipients are barred from taking full-time outside employment; internal paid tutoring or research assistance is permitted within university limits.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment in Malaysia or abroad upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond; recipients must meet graduation publication requirements (minimum 1-2 Scopus/WoS indexed papers) affiliated with UMPSA.",
            "repayment_clawback_conditions": "Termination of monthly stipend and withdrawal of fee waiver if research progress is evaluated as Unsatisfactory (TM/KG) across consecutive reviews.",
            "rules_for_changing_university": "Non-transferable; scheme is funded internally by UMPSA.",
            "rules_for_changing_major": "Field of research cannot be changed without written permission from faculty dean and IPS.",
            "extension_policy": "Extensions beyond maximum tenure (24 months Master's, 36 months PhD) require special approval and are generally self-funded."
        },
        "official_sources_verified": [
            {
                "source_name": "UMPSA Institute of Postgraduate Studies Financial Assistance",
                "source_url": "https://ips.umpsa.edu.my/financial-assistance/graduate-research-scheme",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Universiti Malaysia Pahang Al-Sultan Abdullah Official Portal",
                "source_url": "https://www.umpsa.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-054": {
        "scholarship_id": "SCH-AS-054",
        "basic_details": {
            "scholarship_name": "Tongji University Chinese Government Scholarship (CSC Type B) & Shanghai Municipal Government Scholarship (SGS)",
            "offering_entity": "China Scholarship Council (CSC), Shanghai Municipal Education Commission & Tongji University",
            "host_country": "China",
            "host_institutions_covered": "Tongji University (Siping and Jiading Campuses, Shanghai, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Civil Engineering, College of Architecture and Urban Planning, College of Environmental Science and Engineering, School of Automotive Studies, School of Transportation Engineering, and School of Computer Science and Technology.",
            "number_of_awards_total": "~180 to 220 fully funded CSC Type B and Shanghai Government Scholarship Class A awards annually",
            "number_of_awards_pakistan": "Extensive bilateral enrollment; Pakistani graduate engineers represent one of the largest international scholarship cohorts at Tongji (~30 to 45 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2.5 to 3 years for Master's; 4 years for PhD",
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
            "grading_conversion_notes": "Minimum 80% aggregate (or CGPA 3.2 / 4.0); selected candidates in civil and structural engineering frequently hold CGPA >= 3.5 / 4.0.",
            "subject_background_prerequisites": "Civil engineering, architecture, urban planning, environmental engineering, transportation, automotive engineering, computer science, or related disciplines.",
            "current_education_status": "Graduated or final-year students graduating before July of application year.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior research publications in engineering journals (ASCE, Elsevier, Springer, IEEE) or design competition honors strongly advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 85, or recognized English Medium of Instruction (MOI) certificate for English-taught graduate programs.",
            "other_language_requirements": "HSK Level 5 (minimum score 180) required only for Chinese-taught majors.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates submit concurrent applications via CSC Online Application System (Agency No. 10247) and Tongji International Student Portal.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent Chinese government, Shanghai municipal, or external scholarship award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for the complete duration of the graduate degree program at Tongji University.",
                "amount": "100% covered (~CNY 34,000 to 50,000 / year value; ~PKR 1,326,000 to 1,950,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Tongji international application evaluation fee of CNY 600 paid via university online portal.",
                "amount": "CNY 600 (~PKR 23,400)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free on-campus international student dormitory accommodation (single room for PhD, twin room for Master's) on Siping or Jiading campus.",
                "amount": "100% covered free university housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend disbursed directly: CNY 3,000 / month for Master's (~PKR 117,000 / month); CNY 3,500 / month for PhD (~PKR 136,500 / month).",
                "amount": "CNY 3,000 to 3,500 / month (~PKR 117,000 to 136,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International relocation flights to Shanghai Pudong/Hongqiao are self-funded by the student.",
                "amount": "Not covered in CSC Type B / SGS"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 Student Visa fee paid directly to Chinese Visa Application Service Center in Pakistan.",
                "amount": "Approx. PKR 18,000 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Medical Insurance for Foreign Students in China (CNY 800/year value) 100% covered by CSC/SGS.",
                "amount": "100% covered comprehensive healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Access to famous subsidized Tongji dining halls; meals cost approximately CNY 15 to 25 per day.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Tongji State Key Laboratories (including State Key Lab of Disaster Reduction in Civil Engineering), libraries, and testing centers.",
                "amount": "100% covered state key laboratory access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference participation and travel grants provided through Tongji Graduate School and host faculty research grants.",
                "amount": "Up to CNY 5,000 to 10,000 conference travel funds"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle service operating between Siping, Jiading, and Huxi campuses, plus subsidized Shanghai public transit cards.",
                "amount": "Free inter-campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 19000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-leading Chinese Double First Class institution (Tongji University, Shanghai).",
            "participating_institutions": [
                "Tongji University (Siping Campus and Jiading Campus, Shanghai, China)"
            ],
            "university_rankings_scope": "QS World University Rankings #192, World #1 in Civil & Structural Engineering (QS Subject Rankings 2024/2025), Top 15 globally in Architecture and Built Environment.",
            "available_majors": [
                "MSc / PhD in Civil Engineering (Structural, Geotechnical, Bridge, Underground)",
                "MSc / PhD in Architecture and Urban Planning",
                "MSc / PhD in Environmental Science and Engineering",
                "MSc / PhD in Transportation Engineering",
                "MSc / PhD in Automotive Engineering and Intelligent Vehicles",
                "MSc / PhD in Computer Science and Technology",
                "MSc / PhD in Materials Science and Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2.5 to 3 years; PhD: 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with 80%+ marks, academic transcripts, IELTS 6.5+ / TOEFL 85+ or MOI certificate, pre-acceptance letter from Tongji professor (strongly recommended), two professor recommendation letters, CV, study plan, and Foreigner Physical Examination Form.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "College of Civil Engineering and College of Architecture & Urban Planning are globally elite and intensely competitive; obtaining a Tongji professor's provisional acceptance letter is the decisive differentiator.",
            "strategic_program_match_advice": "Target research teams affiliated with the State Key Laboratory of Disaster Reduction in Civil Engineering or Shanghai Key Labs in Intelligent Driving and Smart Cities."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://study-info.tongji.edu.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "Tongji International Student Portal & CSC Online Application System (Agency No. 10247)",
            "account_creation_instructions": "Submit CSC application choosing Program Category B (Agency No. 10247 for Tongji), then complete Tongji University international student portal application, upload all documents, and pay CNY 600 fee.",
            "step_by_step_workflow": [
                "Step 1: Contact Tongji University professors in relevant colleges and obtain a Provisional Acceptance Letter.",
                "Step 2: Prepare medical examination form, non-criminal record certificate, and attested academic degrees.",
                "Step 3: Register on CSC portal (studyinchina.csc.edu.cn), select Program Type B, enter Tongji Agency No. 10247, and submit.",
                "Step 4: Register on Tongji online application portal (study-info.tongji.edu.cn), submit application, and pay CNY 600 fee.",
                "Step 5: College admission committee conducts academic review and schedules video interviews.",
                "Step 6: Tongji Graduate School nominates successful candidates to CSC / Shanghai Municipal Education Commission.",
                "Step 7: Final CSC confirmation issued in June/July with official Admission Notice and JW201/JW202 form.",
                "Step 8: Apply for Chinese X1 Visa at Chinese Visa Center and arrive in Shanghai for September registration."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track (CSC Type B / SGS Class A): Admission and scholarship are evaluated simultaneously by Tongji and confirmed by CSC/SGS.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed official PDF letters on institutional letterhead with referee contact details.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words for Master's, 1,500 words for PhD) detailing research objectives, methodology, and relevance to Tongji's academic strengths.",
            "study_plan_research_proposal_requirements": "Rigorous technical proposal outlining problem statement, state-of-the-art literature review, research design, and alignment with Tongji laboratory facilities.",
            "cv_format_requirements": "Academic CV highlighting educational achievements, software proficiencies, laboratory expertise, and publication list.",
            "interviews_conducted": True,
            "interview_format_details": "Departmental panel interview via Zoom / Tencent Meeting evaluating engineering depth, research capability, and English communication.",
            "standardized_tests": "IELTS 6.5+, TOEFL 85+, or official English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "CNY 600 (approx. USD 85 / ~PKR 23,400)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani applicants.",
            "translation_requirements": "Certified English or Chinese translation for all non-English/non-Chinese credentials.",
            "final_submission_method": "Online submission via CSC portal and Tongji University international student application system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Notarized Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree with minimum 80% marks from an HEC-recognized university.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA Pakistan, and notarized."
            },
            {
                "document_name": "Detailed Study Plan / Research Proposal",
                "mandatory": True,
                "specification": "Structured research proposal (minimum 1,000 words Master's / 1,500 words PhD) detailing proposed investigation.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Two Recommendation Letters from Full or Associate Professors",
                "mandatory": True,
                "specification": "Confidential evaluation letters with professor contact details, signatures, and university seals.",
                "pakistan_specific_instruction": "On official institutional letterhead."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Standard Chinese medical examination form completed within last 6 months with lab test results and chest X-ray.",
                "pakistan_specific_instruction": "Completed by recognized hospital or laboratory."
            },
            {
                "document_name": "Certificate of Non-Criminal Record (Police Clearance)",
                "mandatory": True,
                "specification": "Official police character clearance certificate issued within the past 6 months.",
                "pakistan_specific_instruction": "Attested by MoFA Pakistan."
            },
            {
                "document_name": "English Language Proficiency Proof",
                "mandatory": True,
                "specification": "IELTS 6.5+, TOEFL iBT 85+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate or official test score report."
            },
            {
                "document_name": "Tongji Professor Provisional Acceptance Letter",
                "mandatory": False,
                "specification": "Signed provisional acceptance form from a Tongji University graduate supervisor.",
                "pakistan_specific_instruction": "Strongly recommended; elevates admission probability significantly."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "November 1",
            "application_deadline": "February 15 (CSC Type B deadline) / March 31 (Shanghai Government Scholarship deadline)",
            "university_admission_deadline": "February 15 / March 31",
            "document_submission_deadline": "February 15 / March 31",
            "recommendation_letters_deadline": "February 15 / March 31",
            "interview_period": "March - April",
            "shortlist_announcement": "May (University nomination) / July (CSC final confirmation)",
            "final_result_acceptance_deadline": "July 15",
            "visa_application_window": "July - August",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Single annual admission cycle for Fall semester entry; CSC Type B applications strictly due by mid-February."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior GPA, university prestige, foundational engineering grades)",
            "extracurricular_and_leadership_weight": "5% (Leadership, international adaptability, teamwork)",
            "research_experience_weight": "40% (Prior publications, proposal strength, Tongji professor endorsement)",
            "work_experience_weight": "5% (Engineering practice or industrial research experience)",
            "personal_statement_weight": "5% (Clarity of purpose and alignment with Tongji key disciplines)",
            "recommendations_weight": "5% (Quality of referee appraisals)",
            "interview_weight": "5% (Departmental virtual interview evaluation)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research capability)",
            "selection_panel_composition": "Tongji University International Students Office, School Admissions Committee, and China Scholarship Council Evaluation Board.",
            "evaluation_methodology": "Two-tier review: academic qualification evaluation by specialized faculty followed by international scholarship allocation committee vetting."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 to 5,500 international applicants across all disciplines",
            "total_scholarships_awarded": "~180 to 220 fully funded CSC Type B and SGS Class A awards annually",
            "acceptance_rate_global": "~4.0% to 5.5%",
            "acceptance_rate_pakistan": "~7.0% to 10.0% for applicants with professor pre-acceptance and published papers",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.50 / 4.00, accompanied by 1+ peer-reviewed journal/conference publications",
            "typical_academic_and_research_profile": "Graduates holding top degrees in civil, mechanical, environmental, or computer engineering, with documented research capability and pre-acceptance from a Tongji supervisor.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, UET Lahore, NED Karachi, FAST-NUCES, COMSATS, GIKI).",
            "high_representation_countries": "Pakistan, Germany, Italy, Russia, Thailand, Malaysia, Vietnam, Egypt, Iran.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portals at study-info.tongji.edu.cn and studyinchina.csc.edu.cn.",
                "Beware of unauthorized agents claiming to sell guaranteed Tongji University CSC seats; CSC and Tongji strictly prohibit commercial intermediaries."
            ],
            "application_fee_warning": "Tongji application fee of CNY 600 is paid directly through the secure university portal; CSC portal submission is completely free.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents with templated research proposals are systematically rejected by Tongji review committees.",
            "hidden_costs_breakdown": [
                "Tongji application fee: CNY 600 (~PKR 23,400).",
                "Chinese X1 Visa fee in Pakistan: ~PKR 18,000.",
                "Medical checkup & police certificate attestations: ~PKR 25,000 to 35,000.",
                "Initial relocation flight to Shanghai: ~PKR 180,000 to 260,000.",
                "Initial pocket money before first stipend disbursement: ~CNY 1,500 (~PKR 58,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need HSK Chinese fluency. Reality: All STEM graduate programs are taught and examined 100% in English.",
                "Myth: Pre-acceptance letters are required. Reality: Not legally mandatory, but having a professor's provisional acceptance letter increases admission likelihood to over 75%."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs claim CSC covers round-trip international flights; CSC Type B university programs do NOT provide international airfare."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass the Annual CSC Comprehensive Review evaluating course grades, thesis research progress, and campus conduct.",
            "attendance_requirements": "Full-time physical residency in Shanghai; unexcused absences result in stipend suspension.",
            "academic_progress_monitoring": "Annual CSC review conducted every May by the host college and International Students Office.",
            "work_restrictions_during_study": "Commercial off-campus employment is restricted by Chinese student visa regulations; part-time on-campus work-study permitted with university approval.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, post-doctoral fellowships, corporate employment in China, or return home.",
            "service_obligations_or_bonds": "Zero financial bond or service commitment.",
            "repayment_clawback_conditions": "Scholarship is cancelled and student repatriated if dismissed for academic failure, disciplinary infractions, or criminal offenses.",
            "rules_for_changing_university": "Non-transferable to other Chinese universities under CSC rules.",
            "rules_for_changing_major": "Changing major is strictly prohibited after scholarship registration.",
            "extension_policy": "Extensions are generally not granted; students must complete degrees within the official approved period."
        },
        "official_sources_verified": [
            {
                "source_name": "Tongji University International Students Office Scholarship Guide",
                "source_url": "https://study.tongji.edu.cn/info/1043/1648.htm",
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

    "SCH-AS-055": {
        "scholarship_id": "SCH-AS-055",
        "basic_details": {
            "scholarship_name": "University of Tsukuba MEXT Special Recommendation Science & Technology Award (University Recommendation IGP)",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan & University of Tsukuba",
            "host_country": "Japan",
            "host_institutions_covered": "University of Tsukuba (Tsukuba Science City, Ibaraki Prefecture, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Science and Technology (Pure and Applied Sciences, Systems and Information Engineering, Life and Environmental Sciences), Graduate School of Comprehensive Human Sciences (Informatics, Medical Sciences), and International Degree Programs.",
            "number_of_awards_total": "~80 to 110 MEXT University Recommendation scholarships awarded annually across graduate divisions",
            "number_of_awards_pakistan": "Open to designated diplomatic partner countries; typically 12 to 18 Pakistani STEM researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master's; 3 to 4 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 144,000 / month for Master's (~PKR 273,600 / month); JPY 145,000 / month for PhD (~PKR 275,500 / month) plus 100% tuition waiver and round-trip international airfare"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries with official diplomatic relations with Japan (Pakistan fully eligible; Japanese dual citizens ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2, 1991 (under 35 years old at commencement per MEXT statutory guidelines).",
            "academic_qualifications": "16 years of formal education (Bachelor's degree) for Master's; 18 years of education (Master's degree) for PhD from an accredited university with minimum MEXT Grade Point Coefficient of 2.30 out of 3.00.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 2.3,
            "grading_conversion_notes": "Minimum MEXT GPA calculation of 2.30 out of 3.00; competitive applicants at Tsukuba typically possess MEXT GPA >= 2.65 / 3.00.",
            "subject_background_prerequisites": "Physics, chemistry, materials science, computer science, electrical engineering, systems engineering, biotechnology, or environmental sciences.",
            "current_education_status": "Graduated or final-year students completing degree requirements before arrival in Japan (late September).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior laboratory research experience, computational modeling expertise, or published scientific papers strongly advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "CEFR Level B2 or higher in English (IELTS Academic 6.5+, TOEFL iBT 80+) or official English Medium of Instruction (MOI) certificate; JLPT N2+ accepted for Japanese-medium programs.",
            "other_language_requirements": "Japanese language proficiency is not required for English-taught international programs.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must establish contact with a Tsukuba prospective faculty advisor and obtain an official Letter of Provisional Acceptance prior to institutional nomination.",
            "previous_scholarship_restrictions": "Previous MEXT recipients are ineligible unless at least 3 years have elapsed since prior award completion.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full waiver of entrance examination fee (JPY 30,000), admission matriculation fee (JPY 282,000), and annual tuition fees (JPY 535,800/year).",
                "amount": "100% covered (~JPY 847,800 first-year value; ~PKR 1,610,000)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Screening and entrance examination fees are completely waived for MEXT scholarship nominees.",
                "amount": "100% waived (JPY 30,000 value)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized international student dormitory housing at University of Tsukuba Global Village or Ichinoya / Hirasuna residences (approx. JPY 18,000 to 35,000 / month).",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Disbursed monthly: JPY 144,000 / month for Master's (~PKR 273,600 / month); JPY 145,000 / month for PhD (~PKR 275,500 / month) plus designated regional allowance top-up (JPY 2,000 to 3,000/month).",
                "amount": "JPY 144,000 to 148,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international flight ticket between Islamabad/Karachi/Lahore and Tokyo Narita/Haneda airport fully covered by MEXT.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese Student Visa issued free of charge for MEXT government scholars at the Embassy of Japan in Islamabad or Consulate-General in Karachi.",
                "amount": "100% covered / fee exempt"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Enrolled in Japan National Health Insurance (NHI) covering 70% of medical costs; subsidized monthly premium (approx. JPY 2,000/month) paid from stipend.",
                "amount": "Subsidized National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized university dining halls across Tsukuba campus, including halal-friendly dining options at Central Cafeteria.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Tsukuba Science City research institutes, AIST (National Institute of Advanced Industrial Science and Technology), and KEK high-energy accelerator facilities.",
                "amount": "100% covered national laboratory research access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and JSPS research project funds cover domestic and international conference participation.",
                "amount": "Lab grant-funded conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Campus bus network connecting all university areas, plus student discount commuter passes on the Tsukuba Express (TX) railway to Tokyo.",
                "amount": "Campus bus transit & railway student discounts"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Japanese National University Corporation (University of Tsukuba, Tsukuba Science City).",
            "participating_institutions": [
                "University of Tsukuba (Tsukuba Science City, Ibaraki Prefecture, Japan)"
            ],
            "university_rankings_scope": "QS World University Rankings #355, Top 10 in Japan; designated Top Global University, home to 3 Nobel laureates and situated at the heart of Tsukuba Science City holding over 300 research institutes.",
            "available_majors": [
                "Master's / PhD in Pure and Applied Sciences (Physics, Chemistry, Materials)",
                "Master's / PhD in Systems and Information Engineering (Computer Science, Intelligent Interaction)",
                "Master's / PhD in Life and Environmental Sciences (Agro-Bioresources, Geosciences)",
                "Master's / PhD in Comprehensive Human Sciences (Informatics, Medical Sciences)",
                "Master's / PhD in Empowerment Informatics",
                "Master's / PhD in International Agricultural Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with MEXT GPA >= 2.30/3.00, academic transcripts, research plan (Kenkyu Keikakusho), Letter of Provisional Acceptance from Tsukuba professor, Dean's recommendation letter, English proficiency score (IELTS 6.5+ / TOEFL 80+ / MOI), and thesis summary.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Systems and Information Engineering (AI, robotics) and Life Sciences are highly competitive; securing an official Letter of Provisional Acceptance from a Tsukuba professor is the essential prerequisite.",
            "strategic_program_match_advice": "Leverage Tsukuba's joint laboratories with AIST and RIKEN; contact faculty members early (October-November) with a tailored research proposal citing their recent publications."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.tsukuba.ac.jp/en/admissions/financial-scholarships/mext/",
            "portal_system_name": "University of Tsukuba Web Entry System & MEXT University Recommendation Track",
            "account_creation_instructions": "Establish contact with prospective advisor, obtain Letter of Provisional Acceptance, submit application package via departmental graduate office, and complete University Web Entry registration.",
            "step_by_step_workflow": [
                "Step 1: Identify and email prospective Tsukuba academic advisors with CV, transcripts, and research proposal (October-November).",
                "Step 2: Participate in informal interview and obtain signed Letter of Provisional Acceptance.",
                "Step 3: Complete MEXT University Recommendation application form and compile certified dossiers (December-January).",
                "Step 4: Prospective supervisor submits internal nomination dossier to Tsukuba Graduate School Selection Board.",
                "Step 5: University conducts internal screening and submits institutional recommendation list to MEXT Tokyo (March).",
                "Step 6: MEXT Tokyo officially ratifies scholarship nominations (June).",
                "Step 7: University issues Certificate of Eligibility (COE) and flight e-tickets; apply for Japanese visa at embassy.",
                "Step 8: Fly to Tokyo Narita/Haneda in late September and start autumn semester on October 1."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track (Daigaku Suisen): Admission and MEXT scholarship are evaluated as a single integrated package.",
            "recommendation_letters_submission_method": "Formal recommendation letter addressed to the President of University of Tsukuba issued by Dean or higher authority of applicant's home institution.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (MEXT prescribed form) detailing background, motivation, research objectives, and methodology in Japan.",
            "study_plan_research_proposal_requirements": "Structured academic proposal following MEXT Kenkyu Keikakusho format describing past research, proposed research in Japan, and anticipated scholarly contributions.",
            "cv_format_requirements": "Standard academic CV detailing education, thesis title, technical skills, publications, and conference presentations.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview conducted via Zoom by prospective supervisor and departmental committee evaluating research aptitude.",
            "standardized_tests": "IELTS 6.5+, TOEFL 80+, or official English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "JPY 0 (Exempted for MEXT scholarship nominees)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations recommended for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translation for all non-English/non-Japanese documents.",
            "final_submission_method": "Electronic submission via Tsukuba Web Entry / departmental graduate office followed by postal dispatch of original documents if requested."
        },
        "required_documents_checklist": [
            {
                "document_name": "MEXT Application Form for University Recommendation",
                "mandatory": True,
                "specification": "Official Japanese Ministry prescribed form completed in English or Japanese with passport-style photo.",
                "pakistan_specific_instruction": "Standard official MEXT form."
            },
            {
                "document_name": "Field of Study and Research Plan (Kenkyu Keikakusho)",
                "mandatory": True,
                "specification": "Detailed research plan following official MEXT template detailing past research and proposed research in Japan.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Official Academic Transcripts with Grading Legend",
                "mandatory": True,
                "specification": "Complete university transcripts showing course grades, credits, and grading system for MEXT GPA calculation.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Letter of Recommendation from Dean or Higher Authority",
                "mandatory": True,
                "specification": "Recommendation letter addressed to the President of University of Tsukuba signed by university Dean or Rector.",
                "pakistan_specific_instruction": "On institutional letterhead with official seal."
            },
            {
                "document_name": "Abstract of Bachelor's / Master's Thesis",
                "mandatory": True,
                "specification": "Concise summary (1-2 pages) of previous graduation thesis or major research publications.",
                "pakistan_specific_instruction": "Summary of final year project or thesis."
            },
            {
                "document_name": "Certificate of Language Proficiency",
                "mandatory": True,
                "specification": "IELTS 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate demonstrating CEFR B2+.",
                "pakistan_specific_instruction": "MOI certificate or official test score."
            },
            {
                "document_name": "Tsukuba Faculty Letter of Provisional Acceptance",
                "mandatory": True,
                "specification": "Signed letter from Tsukuba faculty member committing to supervise the applicant upon MEXT approval.",
                "pakistan_specific_instruction": "Obtained directly from prospective Tsukuba professor."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 15",
            "application_deadline": "January 15",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "January 15",
            "recommendation_letters_deadline": "January 15",
            "interview_period": "January 20 - February 15",
            "shortlist_announcement": "March (University nomination to MEXT) / June (MEXT Tokyo final ratification)",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Single annual admission cycle for October matriculation; faculty contact must begin 10 to 12 months prior."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (MEXT GPA coefficient calculation >= 2.30/3.00, academic consistency)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated in MEXT academic screening)",
            "research_experience_weight": "40% (Research proposal rigor, previous thesis, supervisor endorsement)",
            "work_experience_weight": "5% (Relevant scientific laboratory or technical industry experience)",
            "personal_statement_weight": "5% (Study plan clarity and intent)",
            "recommendations_weight": "5% (Dean's official recommendation)",
            "interview_weight": "10% (Technical interview with prospective Tsukuba faculty advisor)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Tsukuba Graduate School Academic Board, Global Commons Bureau, and Japanese Ministry of Education (MEXT) Selection Committee.",
            "evaluation_methodology": "Rigorous academic assessment prioritizing candidates with top MEXT GPA coefficients (above 2.50/3.00), strong publication potential, and supervisor backing."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,000 to 1,300 applicants across graduate divisions",
            "total_scholarships_awarded": "~80 to 110 MEXT University Recommendation awards annually",
            "acceptance_rate_global": "~8.0% to 10.0%",
            "acceptance_rate_pakistan": "~12.0% to 16.0% for applicants with professor provisional acceptance and MEXT GPA >= 2.60",
            "typical_successful_applicant_gpa": "MEXT GPA coefficient >= 2.60 / 3.00 (approx. CGPA >= 3.50 / 4.00), accompanied by strong thesis research or publications",
            "typical_academic_and_research_profile": "STEM graduates with strong laboratory foundations, clear research alignment with Tsukuba science clusters, and professor acceptance.",
            "common_backgrounds_of_winners": "Graduates from leading Pakistani universities (NUST, Quaid-i-Azam, FAST-NUCES, UET Lahore, COMSATS, PIEAS, GIKI).",
            "high_representation_countries": "Pakistan, Vietnam, Indonesia, China, Bangladesh, Malaysia, Thailand, Egypt, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only consult official websites at tsukuba.ac.jp and mext.go.jp.",
                "Beware of unauthorized agents claiming to sell MEXT recommendation seats; MEXT awards are strictly managed between universities and the Japanese government."
            ],
            "application_fee_warning": "No application or examination fee is charged for MEXT scholarship nominees.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are strictly rejected; applicants must author their own Kenkyu Keikakusho research plan.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (Waived).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Medical checkup for COE processing: ~PKR 15,000 to 25,000.",
                "Initial pocket money before first stipend deposit: ~JPY 100,000 (~PKR 190,000).",
                "National Health Insurance monthly premium: ~JPY 2,000/month (~PKR 3,800/month)."
            ],
            "misleading_claims_debunked": [
                "Myth: Japanese language fluency is mandatory. Reality: All STEM graduate programs at Tsukuba are conducted entirely in English.",
                "Myth: You can apply without professor endorsement. Reality: University recommendation track requires prior provisional acceptance from a Tsukuba faculty professor."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest age limit can be relaxed; MEXT statutory age cutoff (born on or after April 2, 1991) is strictly enforced without exception."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain MEXT Grade Point Coefficient of at least 2.30 out of 3.00 throughout degree study.",
            "attendance_requirements": "Full-time physical research residency in Tsukuba; mandatory monthly signing of scholarship register at the university academic office to receive stipend.",
            "academic_progress_monitoring": "Annual academic progress review submitted to MEXT via the University Graduate School.",
            "work_restrictions_during_study": "Part-time work strictly restricted; requires special immigration permit (Shikakugai Katsudo Kyoka) and written consent from academic supervisor (maximum 28 hours/week during breaks, typically discouraged during term).",
            "home_country_return_obligation": "None; scholars are free to seek international corporate employment, post-docs in Japan, or return to Pakistan.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is immediately terminated if GPA falls below 2.30, unexcused absence from Japan occurs, or disciplinary expulsion occurs.",
            "rules_for_changing_university": "Strictly prohibited to transfer to another Japanese university under MEXT University Recommendation regulations.",
            "rules_for_changing_major": "Major or laboratory changes are generally not permitted once enrolled.",
            "extension_policy": "Extensions from Master's to PhD are highly competitive and require separate MEXT institutional recommendation screening."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Tsukuba International Admissions & MEXT",
                "source_url": "https://www.tsukuba.ac.jp/en/admissions/financial-scholarships/mext/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Japanese Ministry of Education (MEXT) Official Guide",
                "source_url": "https://www.mext.go.jp/en/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
