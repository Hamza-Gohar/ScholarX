"""Batch 27 Part 3: Southeast Asia Elite Research Awards (4 awards)
SCH-AS-079: Universiti Teknologi Malaysia (UTM) National Postgraduate Scholarship (NPS)
SCH-AS-080: Universiti Putra Malaysia (UPM) Graduate Research Fellowship (GRF)
SCH-AS-081: Asian Institute of Technology (AIT) Royal Thai Government (RTG) Fellowships
SCH-AS-082: Chulalongkorn University Graduate Scholarship for Non-ASEAN Countries
"""

DATA_P3 = {
    "SCH-AS-079": {
        "scholarship_id": "SCH-AS-079",
        "basic_details": {
            "scholarship_name": "Universiti Teknologi Malaysia (UTM) National Postgraduate Award & Graduate Research Assistantship (GRA)",
            "offering_entity": "Universiti Teknologi Malaysia (UTM) School of Graduate Studies (SPS) & Department of Deputy Vice-Chancellor (Research & Innovation)",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Teknologi Malaysia (Skudai Campus, Johor Bahru / Kuala Lumpur Campus, Malaysia)",
            "degree_levels": ["Master of Philosophy (by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Civil Engineering, Faculty of Mechanical Engineering, Faculty of Electrical Engineering, Faculty of Chemical and Energy Engineering, and Faculty of Computing.",
            "number_of_awards_total": "~120 to 180 graduate research appointments awarded annually across engineering faculties",
            "number_of_awards_pakistan": "Extensive international cohort; typically 20 to 35 Pakistani engineering and computing researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 24 months for Master's by research; up to 36 months for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Monthly research stipend: RM 1,800 to RM 2,300 / month for PhD (~PKR 117,000 to 149,500 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month) plus full semester tuition fee waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Malaysian citizens and international candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Maximum 35 years for Master's; maximum 40 years for PhD candidates at the time of appointment.",
            "academic_qualifications": "Recognized Bachelor's degree with minimum CGPA 3.00/4.00 for Master's; recognized Master's degree with minimum CGPA 3.00/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum CGPA 3.00 / 4.00; competitive applicants typically hold CGPA >= 3.40 / 4.00 with laboratory, computing, or engineering research experience.",
            "subject_background_prerequisites": "Civil engineering, mechanical engineering, electrical engineering, chemical engineering, petroleum engineering, computer science, software engineering, or applied mathematics.",
            "current_education_status": "Graduated or final-semester students expecting degree completion before semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in Scopus/WoS indexed journals or engineering conference proceedings provide a notable advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 80, MUET Band 4.0, or recognized English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Malay language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure endorsement and laboratory sponsorship from an active UTM principal investigator holding research grant funding (FRGS, PRGS, or industrial contracts).",
            "previous_scholarship_restrictions": "Cannot hold any concurrent national scholarship, industrial sponsorship, or full-time paid employment.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for eligible postgraduate research semesters covered under the UTM Graduate Research Scheme.",
                "amount": "100% covered (~RM 12,000 to 18,000 / year value; ~PKR 780,000 to 1,170,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UTM international postgraduate application fee of RM 150 paid during online application submission.",
                "amount": "RM 150 (~PKR 9,800)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate residential colleges at Skudai campus (Kolej Tun Dr. Ismail / Kolej Rahman Putra; approx. RM 250 to 400 / month), paid from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research assistantship allowance: RM 1,800 to RM 2,300 / month for PhD (~PKR 117,000 to 149,500 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month).",
                "amount": "RM 1,300 to RM 2,300 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Kuala Lumpur / Senai Johor is self-funded.",
                "amount": "Not covered in central scheme"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "EMGS visa processing and Malaysian Student Pass fees paid by candidate.",
                "amount": "Approx. RM 2,000 to 2,500 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Malaysian student medical and hospitalization insurance provided via EMGS student pass package.",
                "amount": "100% covered student medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Campus cafeterias across Skudai and KL campuses provide affordable dining; daily meals cost approximately RM 15 to 25.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to UTM Perpustakaan Sultanah Zanariah (PSZ Library), engineering test benches, and software simulation licenses.",
                "amount": "100% covered laboratory & computing infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference attendance and publication charges (APC) for high-impact Scopus/WoS indexed journals covered directly by host research grant.",
                "amount": "Grant-funded conference travel and APC charges"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UTM internal campus shuttle bus network serving all residential colleges, academic faculties, and student centers.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 12500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Malaysia premier engineering and technology university (Universiti Teknologi Malaysia - UTM).",
            "participating_institutions": [
                "Universiti Teknologi Malaysia (Skudai Campus in Johor Bahru and Jalan Sultan Yahya Petra Campus in Kuala Lumpur, Malaysia)"
            ],
            "university_rankings_scope": "QS World University Rankings #181 globally, Top 40 in Asia, World Top 50 in Petroleum and Chemical Engineering; recognized as Malaysia's premier technical and engineering university.",
            "available_majors": [
                "MPhil / PhD in Electrical Engineering",
                "MPhil / PhD in Mechanical Engineering",
                "MPhil / PhD in Chemical and Energy Engineering",
                "MPhil / PhD in Civil Engineering",
                "MPhil / PhD in Computer Science and Software Engineering",
                "MPhil / PhD in Biomedical Engineering",
                "MPhil / PhD in Materials Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's by Research: 1.5 to 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree in engineering or computing with CGPA 3.00+, academic transcripts, research proposal, supervisor endorsement form, two reference letters, and IELTS 6.0 / TOEFL 80 or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Faculty of Computing and Faculty of Electrical Engineering are highly sought-after; securing supervisor agreement with active grant funding is the single most critical factor.",
            "strategic_program_match_advice": "Target research teams affiliated with UTM Wireless Communication Centre (WCC), Centre for Hydrogen Energy, or Institute of High Voltage and High Current."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://sps.utm.my/financial-assistance/ & https://admission.utm.my/",
            "portal_system_name": "UTM School of Graduate Studies (SPS) Portal",
            "account_creation_instructions": "Contact prospective supervisor, obtain acceptance form, register on UTM postgraduate admission portal, complete application, upload credentials, and pay RM 150 fee.",
            "step_by_step_workflow": [
                "Step 1: Explore UTM faculty expertise directory and email prospective supervisors with CV and research draft.",
                "Step 2: Obtain signed UTM Supervisor Acceptance and GRA Recommendation Form.",
                "Step 3: Register on UTM admission portal and submit online postgraduate application.",
                "Step 4: Upload attested academic transcripts, research proposal, passport copy, and English proof.",
                "Step 5: Faculty Graduate Committee reviews technical proposal and conducts online interview.",
                "Step 6: SPS issues official Letter of Offer and GRA Appointment Letter.",
                "Step 7: Apply for EMGS Visa Approval Letter (VAL) and Single Entry Visa at Malaysian High Commission in Islamabad.",
                "Step 8: Travel to Johor Bahru / Kuala Lumpur, complete medical screening, and matriculate."
            ],
            "university_vs_scholarship_routing": "Integrated departmental route: Application for admission and GRA award are reviewed together upon faculty recommendation.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed PDF recommendation letters on official university letterheads.",
            "personal_statement_prompts": "Statement of research intent detailing technical competencies, research goals, and synergy with host supervisor's funded research project.",
            "study_plan_research_proposal_requirements": "5 to 8 page structured research proposal covering problem statement, literature review, methodology, equipment needs, and milestone schedule.",
            "cv_format_requirements": "Academic CV detailing qualifications, laboratory/computing experience, software proficiencies, and publications list.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Google Meet or MS Teams conducted by prospective supervisor and departmental postgraduate coordinator.",
            "standardized_tests": "IELTS 6.0+, TOEFL 80+, MUET Band 4.0, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "RM 150 (approx. USD 35 / ~PKR 9,800)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani credentials during EMGS processing.",
            "translation_requirements": "Certified English translations for all non-English documents.",
            "final_submission_method": "Online submission via UTM postgraduate admission portal."
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
                "document_name": "Supervisor Acceptance & GRA Recommendation Form",
                "mandatory": True,
                "specification": "Official UTM form signed by prospective supervisor confirming laboratory placement and willingness to supervise.",
                "pakistan_specific_instruction": "Obtained directly from UTM faculty supervisor."
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
            "application_deadline": "June 30 (Semester I - October) / November 30 (Semester II - March)",
            "university_admission_deadline": "June 30 / November 30",
            "document_submission_deadline": "June 30 / November 30",
            "recommendation_letters_deadline": "June 30 / November 30",
            "interview_period": "July - August / December - January",
            "shortlist_announcement": "Late August / Mid January",
            "final_result_acceptance_deadline": "Within 2 weeks of offer issuance",
            "visa_application_window": "August / January via EMGS",
            "semester_commencement": "October (Semester I) / March (Semester II)",
            "annual_cycle_notes": "Bi-annual intake cycles: Semester I in October and Semester II in March."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic performance, and foundational engineering coursework)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and professional leadership)",
            "research_experience_weight": "35% (Prior publications, technical proposal rigor, and supervisor grant synergy)",
            "work_experience_weight": "5% (Industrial engineering or laboratory technical experience)",
            "personal_statement_weight": "5% (Clarity of purpose and dedication to engineering research)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit and research capability based)",
            "selection_panel_composition": "Faculty Postgraduate Committee, Dean of School of Graduate Studies, and Host Research Project PI.",
            "evaluation_methodology": "Two-stage evaluation: departmental technical vetting of research alignment followed by central SPS award confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,400 to 1,800 applicants across both semesters",
            "total_scholarships_awarded": "~120 to 180 GRA awards annually",
            "acceptance_rate_global": "~10% to 12%",
            "acceptance_rate_pakistan": "~15% to 20% for applicants with pre-secured supervisor endorsement and CGPA >= 3.35",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.35 / 4.00, coupled with prior lab project experience or publications",
            "typical_academic_and_research_profile": "Graduates in engineering or computing with strong programming/laboratory skills, clear research plan, and supervisor endorsement.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, UET Lahore, NED Karachi, FAST-NUCES, COMSATS, GIKI).",
            "high_representation_countries": "Malaysia, Pakistan, Indonesia, Nigeria, Yemen, Bangladesh, Egypt.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal sps.utm.my.",
                "Do not pay money to educational agents promising guaranteed assistantships; awards depend entirely on faculty supervisor endorsement."
            ],
            "application_fee_warning": "University application fee is RM 150 paid directly to UTM via secure online payment.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are flagged and rejected; applicants must write their own technical research proposal.",
            "hidden_costs_breakdown": [
                "UTM application fee: RM 150 (~PKR 9,800).",
                "EMGS visa approval and student pass fees: ~RM 2,200 to 2,500 (~PKR 143,000 to 162,500).",
                "HEC and MoFA document attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "One-way flight to Kuala Lumpur / Johor: ~PKR 90,000 to 130,000.",
                "Initial living deposit before first stipend cycle: ~RM 1,000 (~PKR 65,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Scheme covers international flights. Reality: International travel and EMGS visa fees are self-funded.",
                "Myth: You can apply without contacting a supervisor. Reality: Supervisor endorsement is effectively mandatory for scheme approval."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim scheme is purely a fee discount; in reality, GRA includes both full tuition waiver and monthly living stipend."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum CGPA 3.00 and Satisfactory (TM) research progress evaluation every semester.",
            "attendance_requirements": "Full-time physical research presence at UTM Skudai or KL campus; scholars may be assigned up to 6 hours/week of laboratory or tutorial teaching assistance.",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by supervisor and presented to Faculty Postgraduate Committee.",
            "work_restrictions_during_study": "Recipients are barred from taking full-time outside employment; internal paid tutoring or research assistance is permitted within university limits.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment in Malaysia or abroad upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond; recipients must meet graduation publication requirements (minimum 1-2 Scopus/WoS indexed papers) affiliated with UTM.",
            "repayment_clawback_conditions": "Termination of monthly stipend and withdrawal of fee waiver if research progress is evaluated as Unsatisfactory across consecutive reviews.",
            "rules_for_changing_university": "Non-transferable; scheme is funded internally by UTM.",
            "rules_for_changing_major": "Field of research cannot be changed without written permission from faculty dean and SPS.",
            "extension_policy": "Extensions beyond maximum tenure (24 months Master's, 36 months PhD) require special approval and are generally self-funded."
        },
        "official_sources_verified": [
            {
                "source_name": "UTM School of Graduate Studies Financial Assistance",
                "source_url": "https://sps.utm.my/financial-assistance/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Universiti Teknologi Malaysia Official Admissions Portal",
                "source_url": "https://admission.utm.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-080": {
        "scholarship_id": "SCH-AS-080",
        "basic_details": {
            "scholarship_name": "Universiti Putra Malaysia (UPM) Graduate Research Fellowship (GRF) & Special Scholarship Scheme",
            "offering_entity": "Universiti Putra Malaysia (UPM) School of Graduate Studies (SGS)",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Putra Malaysia Main Campus (Serdang, Selangor, Malaysia)",
            "degree_levels": ["Master of Science (by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Engineering, Faculty of Science, Faculty of Computer Science and Information Technology, Faculty of Agriculture, Faculty of Biotechnology and Biomolecular Sciences, and Institute of Bioscience.",
            "number_of_awards_total": "~100 to 150 Graduate Research Fellowships awarded annually across faculties",
            "number_of_awards_pakistan": "Open internationally; typically 15 to 25 Pakistani agriculture, biotechnology, and computing researchers appointed annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 24 months for Master's by research; up to 36 months for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Monthly research stipend: RM 1,800 to RM 2,300 / month for PhD (~PKR 117,000 to 149,500 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month) plus up to 100% full tuition fee waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Malaysian citizens and international candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Maximum 35 years for Master's; maximum 40 years for PhD candidates at the time of appointment.",
            "academic_qualifications": "Recognized Bachelor's degree with minimum CGPA 3.00/4.00 for Master's; recognized Master's degree with minimum CGPA 3.00/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum CGPA 3.00 / 4.00; competitive applicants typically hold CGPA >= 3.40 / 4.00 with laboratory, computing, or agricultural research experience.",
            "subject_background_prerequisites": "Agriculture, biotechnology, food science, environmental sciences, chemical engineering, mechanical engineering, computer science, or bioinformatics.",
            "current_education_status": "Graduated or final-semester students expecting degree completion before semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in Scopus/WoS indexed journals or agricultural/biotech laboratory experience advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 80, MUET Band 4.0, or recognized English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Malay language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure endorsement and laboratory placement from an active UPM principal investigator holding research grant funding.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent national scholarship, industrial sponsorship, or full-time paid employment.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full or partial tuition fee waiver covered under the UPM Graduate Research Fellowship scheme.",
                "amount": "100% covered (~RM 12,000 to 18,000 / year value; ~PKR 780,000 to 1,170,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UPM international postgraduate application fee of RM 250 paid during online portal submission.",
                "amount": "RM 250 (~PKR 16,250)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate residential colleges at Serdang campus (approx. RM 250 to 450 / month), paid easily from living stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research assistantship stipend: RM 1,800 to RM 2,300 / month for PhD (~PKR 117,000 to 149,500 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month).",
                "amount": "RM 1,300 to RM 2,300 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Kuala Lumpur is self-funded.",
                "amount": "Not covered in central scheme"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "EMGS visa processing and Malaysian Student Pass fees paid by candidate.",
                "amount": "Approx. RM 2,000 to 2,500 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Malaysian student medical and hospitalization insurance provided via EMGS student pass package.",
                "amount": "100% covered student medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Campus cafeterias across Serdang campus provide affordable dining; daily meals cost approximately RM 15 to 25.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to UPM Sultan Abdul Samad Library, experimental farm stations, advanced analytical genomics labs, and greenhouses.",
                "amount": "100% covered agricultural and biotech research access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference attendance and publication charges (APC) for high-impact Scopus/WoS indexed journals funded directly from host supervisor grant.",
                "amount": "Grant-funded conference travel and APC charges"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UPM campus shuttle bus network serving all residential colleges, academic faculties, and Serdang MRT/KTM stations.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 12500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Malaysia premier research university in agriculture and life sciences (Universiti Putra Malaysia - UPM).",
            "participating_institutions": [
                "Universiti Putra Malaysia Main Campus (Serdang, Selangor, Malaysia)"
            ],
            "university_rankings_scope": "QS World University Rankings #148 globally, Top 30 in Asia, World Top 50 in Agriculture & Forestry; Malaysia's premier research university in life sciences and biotechnology.",
            "available_majors": [
                "Master of Science / PhD in Biotechnology",
                "Master of Science / PhD in Agricultural Sciences",
                "Master of Science / PhD in Food Science and Technology",
                "Master of Science / PhD in Computer Science",
                "Master of Science / PhD in Chemical Engineering",
                "Master of Science / PhD in Environmental Studies",
                "Master of Science / PhD in Biomedical Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's by Research: 1.5 to 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree in relevant discipline with CGPA 3.00+, academic transcripts, research proposal, supervisor endorsement form, two reference letters, and IELTS 6.0 / TOEFL 80 or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Faculty of Biotechnology and Faculty of Agriculture are premier centers; establishing prior supervisor connection is essential.",
            "strategic_program_match_advice": "Focus research proposals on plant genomics, food security, smart agriculture (IoT/AI in farming), or bioprocess engineering where UPM holds massive government funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://sgs.upm.edu.my/financial_assistance_scholarships-1884 & http://sgsportal.upm.edu.my:8080/sgsportal/",
            "portal_system_name": "UPM School of Graduate Studies (SGS) Portal",
            "account_creation_instructions": "Contact prospective supervisor, obtain acceptance form, register on UPM postgraduate portal, submit application, upload credentials, and pay RM 250 fee.",
            "step_by_step_workflow": [
                "Step 1: Explore UPM faculty expertise directory and email prospective supervisors with CV and research draft.",
                "Step 2: Obtain signed UPM Supervisor Acceptance and GRF Recommendation Form.",
                "Step 3: Register on UPM SGS portal and submit online postgraduate application.",
                "Step 4: Upload attested academic transcripts, research proposal, passport copy, and English proof.",
                "Step 5: Faculty Graduate Committee reviews technical proposal and conducts online interview.",
                "Step 6: SGS issues official Letter of Offer and GRF Fellowship Award Letter.",
                "Step 7: Apply for EMGS Visa Approval Letter (VAL) and Single Entry Visa at Malaysian High Commission in Islamabad.",
                "Step 8: Travel to Serdang, complete medical screening, and matriculate."
            ],
            "university_vs_scholarship_routing": "Integrated departmental route: Application for admission and GRF award are reviewed together upon faculty recommendation.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed PDF recommendation letters on official university letterheads.",
            "personal_statement_prompts": "Statement of research intent detailing technical competencies, research goals, and synergy with host supervisor's funded research project.",
            "study_plan_research_proposal_requirements": "5 to 8 page structured research proposal covering problem statement, literature review, methodology, equipment needs, and milestone schedule.",
            "cv_format_requirements": "Academic CV detailing qualifications, laboratory/field experience, software proficiencies, and publications list.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Google Meet or MS Teams conducted by prospective supervisor and departmental postgraduate coordinator.",
            "standardized_tests": "IELTS 6.0+, TOEFL 80+, MUET Band 4.0, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "RM 250 (approx. USD 58 / ~PKR 16,250)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani credentials during EMGS processing.",
            "translation_requirements": "Certified English translations for all non-English documents.",
            "final_submission_method": "Online submission via UPM School of Graduate Studies portal."
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
                "document_name": "Supervisor Acceptance & GRF Recommendation Form",
                "mandatory": True,
                "specification": "Official UPM form signed by prospective supervisor confirming laboratory placement and willingness to supervise.",
                "pakistan_specific_instruction": "Obtained directly from UPM faculty supervisor."
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
            "application_deadline": "June 30 (Semester I - October) / November 30 (Semester II - March)",
            "university_admission_deadline": "June 30 / November 30",
            "document_submission_deadline": "June 30 / November 30",
            "recommendation_letters_deadline": "June 30 / November 30",
            "interview_period": "July - August / December - January",
            "shortlist_announcement": "Late August / Mid January",
            "final_result_acceptance_deadline": "Within 2 weeks of offer issuance",
            "visa_application_window": "August / January via EMGS",
            "semester_commencement": "October (Semester I) / March (Semester II)",
            "annual_cycle_notes": "Bi-annual intake cycles: Semester I in October and Semester II in March."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic performance, and foundational coursework)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and environmental leadership)",
            "research_experience_weight": "35% (Prior publications, technical proposal rigor, and supervisor grant synergy)",
            "work_experience_weight": "5% (Laboratory technical or field research experience)",
            "personal_statement_weight": "5% (Clarity of purpose and dedication to research)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit and research capability based)",
            "selection_panel_composition": "Faculty Postgraduate Committee, Dean of School of Graduate Studies, and Host Research Project PI.",
            "evaluation_methodology": "Two-stage evaluation: departmental technical vetting followed by central SGS award confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,300 to 1,700 applicants across both semesters",
            "total_scholarships_awarded": "~100 to 150 GRF awards annually",
            "acceptance_rate_global": "~9.0% to 11.0%",
            "acceptance_rate_pakistan": "~15.0% to 19.0% for applicants with pre-secured supervisor endorsement and CGPA >= 3.30",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.30 / 4.00, coupled with prior lab project experience or publications",
            "typical_academic_and_research_profile": "Graduates in biotechnology, agriculture, engineering, or computing with clear research plan and supervisor endorsement.",
            "common_backgrounds_of_winners": "Graduates from Pakistani institutions (University of Agriculture Faisalabad, NUST, Quaid-i-Azam, COMSATS, UET Lahore, PMAS Arid Agriculture).",
            "high_representation_countries": "Malaysia, Pakistan, Indonesia, Nigeria, Iran, Bangladesh, Egypt.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal sgs.upm.edu.my.",
                "Do not pay money to educational agents promising guaranteed fellowships; awards depend entirely on faculty supervisor endorsement."
            ],
            "application_fee_warning": "University application fee is RM 250 paid directly to UPM via secure online payment.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are flagged and rejected; applicants must write their own technical research proposal.",
            "hidden_costs_breakdown": [
                "UPM application fee: RM 250 (~PKR 16,250).",
                "EMGS visa approval and student pass fees: ~RM 2,200 to 2,500 (~PKR 143,000 to 162,500).",
                "HEC and MoFA document attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "One-way flight to Kuala Lumpur: ~PKR 90,000 to 130,000.",
                "Initial living deposit before first stipend cycle: ~RM 1,000 (~PKR 65,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Scheme covers international flights. Reality: International travel and EMGS visa fees are self-funded.",
                "Myth: You can apply without contacting a supervisor. Reality: Supervisor endorsement is effectively mandatory for GRF approval."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim scheme is purely a fee discount; in reality, GRF includes both full tuition waiver and monthly living stipend."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum CGPA 3.00 and Satisfactory (TM) research progress evaluation every semester.",
            "attendance_requirements": "Full-time physical research presence at UPM Serdang campus; scholars may be assigned up to 6 hours/week of laboratory or tutorial teaching assistance.",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by supervisor and presented to Faculty Postgraduate Committee.",
            "work_restrictions_during_study": "Recipients are barred from taking full-time outside employment; internal paid tutoring or research assistance is permitted within university limits.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment in Malaysia or abroad upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond; recipients must meet graduation publication requirements (minimum 1-2 Scopus/WoS indexed papers) affiliated with UPM.",
            "repayment_clawback_conditions": "Termination of monthly stipend and withdrawal of fee waiver if research progress is evaluated as Unsatisfactory across consecutive reviews.",
            "rules_for_changing_university": "Non-transferable; scheme is funded internally by UPM.",
            "rules_for_changing_major": "Field of research cannot be changed without written permission from faculty dean and SGS.",
            "extension_policy": "Extensions beyond maximum tenure (24 months Master's, 36 months PhD) require special approval and are generally self-funded."
        },
        "official_sources_verified": [
            {
                "source_name": "UPM School of Graduate Studies Financial Assistance",
                "source_url": "https://sgs.upm.edu.my/financial_assistance_scholarships-1884",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Universiti Putra Malaysia Official Portal",
                "source_url": "https://www.upm.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-081": {
        "scholarship_id": "SCH-AS-081",
        "basic_details": {
            "scholarship_name": "Asian Institute of Technology (AIT) Royal Thai Government (RTG) Fellowships",
            "offering_entity": "Royal Thai Government (RTG) Ministry of Higher Education, Science, Research and Innovation & Asian Institute of Technology (AIT)",
            "host_country": "Thailand",
            "host_institutions_covered": "Asian Institute of Technology (Pathum Thani Main Campus, Bangkok Metropolitan Region, Thailand)",
            "degree_levels": ["Master of Science (MSc)", "Master of Engineering (MEng)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Engineering and Technology (SET), School of Environment, Resources and Development (SERD), and School of Management (SOM) - priority in Civil Engineering, Water Engineering, AI/IoT, Energy, Environmental Management, and Remote Sensing/GIS.",
            "number_of_awards_total": "~120 to 180 RTG fellowships awarded annually across Master's and Doctoral programs",
            "number_of_awards_pakistan": "Open to Asian developing countries; typically 15 to 25 Pakistani engineering and environmental science scholars selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 22-24 months for Master's; up to 36-42 months for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "His Majesty the King's / Her Majesty the Queen's Fellowships cover 100% full tuition and registration fees (THB 840,000 to 1,260,000 value) plus monthly accommodation and living allowance of THB 11,500 to 15,000 / month (~PKR 86,250 to 112,500 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of Thailand and Asian countries (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to early-career engineers and researchers.",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree with minimum CGPA 3.50/4.00 (for King's/Queen's Full Fellowship) or CGPA 3.00/4.00 (for Loom Nam Khong / RTG Fellowship) from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum CGPA 3.50 / 4.00 for full coverage King's/Queen's awards; CGPA 3.00 / 4.00 for standard RTG fellowship.",
            "subject_background_prerequisites": "Civil engineering, water resources, environmental engineering, structural engineering, computer science, data science, energy technology, or remote sensing and GIS.",
            "current_education_status": "Graduated or final-year students completing degree requirements before August/January intake.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience in infrastructure development, water governance, or environmental consulting advantageous but not mandatory.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0 (writing 6.0), TOEFL iBT minimum 80, AIT English Language Test (AIT-EET score 6.0), or official English Medium of Instruction (MOI) certificate.",
            "other_language_requirements": "Thai language proficiency is NOT required; all instruction and research at AIT are conducted 100% in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply online for AIT admission and select Royal Thai Government (RTG) Fellowship on the financial support section.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent full scholarship or fellowship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition and registration fee waiver for standard program duration at AIT.",
                "amount": "100% covered (~THB 840,000 to 1,260,000 total value; ~PKR 6,300,000 to 9,450,000)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "AIT international online application processing fee of USD 25 (or THB 800) paid during portal submission.",
                "amount": "USD 25 (~PKR 7,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "On-campus international graduate dormitory accommodation in AIT student villages provided or covered via monthly accommodation allowance.",
                "amount": "100% covered campus student housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free subsistence allowance: THB 11,500 to 15,000 / month (~PKR 86,250 to 112,500 / month) disbursed directly for meals and living costs.",
                "amount": "THB 11,500 to 15,000 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Bangkok Suvarnabhumi Airport is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Thai Non-Immigrant ED Student Visa fee paid directly to the Royal Thai Embassy in Islamabad or Consulate in Karachi.",
                "amount": "Approx. PKR 15,000 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "AIT Medical Clinic on-campus healthcare and group health insurance plan covering hospitalization.",
                "amount": "100% covered medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Affordable dining across Aobayana and AIT Cafeteria, including dedicated Muslim Halal dining stalls; meals cost THB 40 to 70.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to AIT Library, geoinformatics labs, regional testing centers, and wind tunnel facilities.",
                "amount": "100% covered laboratory & computing infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Fieldwork travel and thesis research grant support provided through host academic department and project grants.",
                "amount": "Field study & thesis research funding"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Internal campus bicycle network and shared campus transport, plus shuttle vans to Bangkok Red Line commuter rail station (Rangsit).",
                "amount": "Campus transit network"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single international autonomous regional postgraduate institute (Asian Institute of Technology - AIT).",
            "participating_institutions": [
                "Asian Institute of Technology (Pathum Thani Campus, Bangkok Metropolitan Area, Thailand)"
            ],
            "university_rankings_scope": "Internationally chartered postgraduate institute founded by SEATO; globally ranked #1 in Thailand and Top 20 globally for SDG 13 (Climate Action) and SDG 6 (Clean Water).",
            "available_majors": [
                "Master's / PhD in Water Engineering and Management",
                "Master's / PhD in Structural Engineering",
                "Master's / PhD in Geotechnical and Earth Resources Engineering",
                "Master's / PhD in Data Science and Artificial Intelligence",
                "Master's / PhD in Energy, Climate Change and Environment",
                "Master's / PhD in Remote Sensing and Geographic Information Systems (GIS)",
                "Master's / PhD in Environmental Engineering and Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 3.5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.00/4.00 (3.50+ for King's/Queen's full award), academic transcripts, two recommendation letters, statement of purpose, and English proficiency certificate (IELTS 6.0+ / TOEFL 80+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Water Engineering, Structural Engineering, and AI/Data Science are premier regional hubs; candidates with CGPA >= 3.60 and solid engineering backgrounds stand the highest chance for King's/Queen's Full Scholarships.",
            "strategic_program_match_advice": "Focus research statements on regional water security, disaster resilience in the Indus basin, or climate adaptation where AIT holds historic leadership and UN agency links."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ait.ac.th/admissions/scholarships/royal-thai-government/",
            "portal_system_name": "AIT Online Admissions System",
            "account_creation_instructions": "Register on the AIT admissions portal, complete postgraduate application form, select Royal Thai Government (RTG) Fellowship on the financial section, upload credentials, and pay USD 25 fee.",
            "step_by_step_workflow": [
                "Step 1: Check eligibility for RTG King's (SET/SOM), Queen's (SERD), or Loom Nam Khong fellowship categories.",
                "Step 2: Register on AIT admissions portal and complete online application form.",
                "Step 3: Upload transcripts, degree certificates, statement of purpose, and English proficiency test or MOI.",
                "Step 4: Register two academic referees who submit evaluation letters online.",
                "Step 5: Pay USD 25 online application processing fee.",
                "Step 6: Academic admissions committee and RTG Fellowship Selection Panel evaluate applications.",
                "Step 7: Shortlisted candidates undergo online interview if required.",
                "Step 8: Official admission offer and RTG Fellowship award issued in May/June (for August intake).",
                "Step 9: Apply for Thai Non-Immigrant ED Visa at Thai Embassy in Islamabad and arrive in Bangkok."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Application for admission automatically triggers evaluation for RTG Fellowships based on applicant's CGPA and regional eligibility.",
            "recommendation_letters_submission_method": "Submitted online by two academic referees via confidential email links generated by AIT portal.",
            "personal_statement_prompts": "Statement of Purpose describing academic milestones, research interests, career aspirations, and motivation for pursuing a graduate degree at AIT.",
            "study_plan_research_proposal_requirements": "Structured research concept note (2-3 pages) detailing proposed engineering or environmental research topic and regional relevance.",
            "cv_format_requirements": "Comprehensive academic CV detailing education, project experience, technical software skills, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "IELTS Academic 6.0+, TOEFL iBT 80+, AIT-EET 6.0, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "USD 25 (approx. PKR 7,000)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC attestation required for Pakistani credentials upon enrollment.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via AIT admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.00 (>= 3.50 for King's/Queen's).",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Statement of Purpose & Research Concept Note",
                "mandatory": True,
                "specification": "Statement of purpose and 2-3 page research concept note detailing proposed thesis topic.",
                "pakistan_specific_instruction": "Structured essay formatted in English."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors submitted electronically.",
                "pakistan_specific_instruction": "From previous university professors."
            },
            {
                "document_name": "English Language Proficiency Proof",
                "mandatory": True,
                "specification": "IELTS Academic 6.0+, TOEFL iBT 80+, AIT-EET 6.0, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "Score report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing education, projects, software proficiencies, and honors.",
                "pakistan_specific_instruction": "Professional academic CV."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "November 1",
            "application_deadline": "February 28 (Early Round) / March 31 (Strict RTG deadline for August intake)",
            "university_admission_deadline": "March 31",
            "document_submission_deadline": "March 31",
            "recommendation_letters_deadline": "April 7",
            "interview_period": "April - May",
            "shortlist_announcement": "May - June",
            "final_result_acceptance_deadline": "Within 2 to 3 weeks of notification",
            "visa_application_window": "June - July",
            "semester_commencement": "August 1 (Fall intake)",
            "annual_cycle_notes": "Main intake commences in August; application window runs from November to March 31."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic consistency in STEM fields)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and regional awareness)",
            "research_experience_weight": "35% (Research proposal rigor, engineering problem solving, and development relevance)",
            "work_experience_weight": "5% (Professional engineering or field experience)",
            "personal_statement_weight": "5% (Clarity of vision and commitment to regional development)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit-driven based on academic CGPA)",
            "selection_panel_composition": "AIT Admissions Committee, School Deans, and Royal Thai Government Scholarship Board.",
            "evaluation_methodology": "Two-tier review: academic qualification evaluation by specialized faculty followed by RTG scholarship allocation committee vetting."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,000 international applicants across Asian region",
            "total_scholarships_awarded": "~120 to 180 RTG awards annually",
            "acceptance_rate_global": "~7.0% to 9.0%",
            "acceptance_rate_pakistan": "~12.0% to 16.0% for candidates with strong engineering backgrounds and CGPA >= 3.50",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.55 / 4.00, accompanied by strong engineering foundations",
            "typical_academic_and_research_profile": "Graduates in civil, environmental, or electrical engineering, water resources, or computer science with clear regional development focus.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, UET Lahore, NED Karachi, FAST-NUCES, COMSATS, UET Peshawar).",
            "high_representation_countries": "Thailand, Pakistan, Vietnam, Myanmar, Nepal, Bangladesh, Indonesia, Cambodia, Sri Lanka.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal ait.ac.th.",
                "AIT does not work with third-party agents charging fees for scholarships; RTG awards are managed directly by AIT."
            ],
            "application_fee_warning": "Application fee of USD 25 is paid directly through the secure AIT online portal.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are flagged and rejected; applicants must write their own statements and concept notes.",
            "hidden_costs_breakdown": [
                "AIT application fee: USD 25 (~PKR 7,000).",
                "Thai Student Visa fee in Pakistan: ~PKR 15,000.",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 15,000.",
                "One-way flight to Bangkok: ~PKR 85,000 to 125,000.",
                "Initial pocket money before first stipend cycle: ~THB 10,000 (~PKR 75,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Thai language is required. Reality: AIT is an international institute; 100% of instruction and research is in English.",
                "Myth: Flight ticket included. Reality: Flights to Bangkok are self-funded by the student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim RTG only covers tuition; King's and Queen's awards cover both 100% tuition and monthly living/accommodation stipends."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.00 out of 4.00 to retain the fellowship each semester.",
            "attendance_requirements": "Full-time physical research presence at AIT Pathum Thani campus; participation in research seminars and departmental duties.",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by academic advisor and presented to Dean's office.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment; limited on-campus student assistantships permitted.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment globally upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond.",
            "repayment_clawback_conditions": "Termination of fellowship if GPA falls below 3.00 across consecutive terms or for disciplinary dismissal.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Field of research cannot be changed without written permission from faculty dean and RTG committee.",
            "extension_policy": "Extensions beyond standard 22 months (Master's) or 36 months (PhD) are generally not funded by RTG."
        },
        "official_sources_verified": [
            {
                "source_name": "AIT Royal Thai Government (RTG) Fellowships Official Guide",
                "source_url": "https://www.ait.ac.th/admissions/scholarships/royal-thai-government/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Asian Institute of Technology Admissions Portal",
                "source_url": "https://www.ait.ac.th/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-082": {
        "scholarship_id": "SCH-AS-082",
        "basic_details": {
            "scholarship_name": "Chulalongkorn University Graduate Scholarship for Non-ASEAN Countries",
            "offering_entity": "Chulalongkorn University Graduate School & Office of International Affairs",
            "host_country": "Thailand",
            "host_institutions_covered": "Chulalongkorn University Main Campus (Pathumwan, Bangkok, Thailand)",
            "degree_levels": ["Master's Degree", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Engineering, Faculty of Science, Faculty of Pharmaceutical Sciences, Faculty of Allied Health Sciences, Petroleum and Petrochemical College (PPC), and Chulalongkorn School of Integrated Innovation (ScII) - all international graduate degree programs.",
            "number_of_awards_total": "~50 to 80 Graduate Scholarships for Non-ASEAN Countries awarded annually",
            "number_of_awards_pakistan": "Open to non-ASEAN developing nations; typically 6 to 12 Pakistani researchers in engineering, petroleum, and health sciences selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 3 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Monthly living stipend of THB 16,000 / month (~PKR 120,000 / month) plus 100% full tuition fee waiver, economy class round-trip airfare, and accommodation allowance of THB 7,000 / month at Chulalongkorn University International House (CU iHouse)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International graduate students from non-ASEAN countries (Pakistan fully eligible; ASEAN citizens apply under separate ASEAN track)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Applicants must not be over 40 years of age at the time of application.",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (for Master's) with minimum CGPA 3.25/4.00, or completed recognized 18-year Master's degree (for PhD) with minimum CGPA 3.50/4.00 from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.25,
            "grading_conversion_notes": "Minimum CGPA 3.25 / 4.00 for Master's; minimum CGPA 3.50 / 4.00 for PhD; competitive applicants typically hold CGPA >= 3.55 / 4.00.",
            "subject_background_prerequisites": "Chemical engineering, petroleum engineering, electrical engineering, computer science, biomedical engineering, pharmaceutical sciences, chemistry, or materials science.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in peer-reviewed journals provide a significant competitive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 79, CU-TEP minimum 75, or official English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Thai language proficiency is NOT required; all international degree programs are taught 100% in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply through their target Chulalongkorn faculty/program, which then nominates shortlisted candidates to the Office of International Affairs.",
            "previous_scholarship_restrictions": "Cannot hold another concurrent scholarship or fellowship covering identical tuition and living costs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver and special academic fees covered for standard degree duration at Chulalongkorn University.",
                "amount": "100% covered (~THB 300,000 to 500,000 / year value; ~PKR 2,250,000 to 3,750,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Chulalongkorn faculty application processing fee of THB 1,000 paid during online portal submission.",
                "amount": "THB 1,000 (~PKR 7,500)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Dedicated monthly accommodation allowance of THB 7,000 / month provided to cover room rental at Chulalongkorn University International House (CU iHouse).",
                "amount": "THB 7,000 / month accommodation allowance"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend of THB 16,000 / month (~PKR 120,000 / month) disbursed directly to the scholar's bank account.",
                "amount": "THB 16,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international airfare between Pakistan and Bangkok Suvarnabhumi Airport provided by the scholarship.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Thai Non-Immigrant ED Student Visa fee paid directly to the Royal Thai Embassy in Islamabad or Consulate in Karachi.",
                "amount": "Approx. PKR 15,000 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Chulalongkorn University Health Service Center healthcare and comprehensive group medical insurance plan.",
                "amount": "100% covered medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized cafeterias across Chulalongkorn campus, including certified halal dining options; meals cost THB 35 to 60.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Chulalongkorn Central Library (Thailand's premier academic library), supercomputing resources, and national petrochemical testing centers.",
                "amount": "100% covered library & laboratory access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Graduate School Overseas Presentation Grant supports international conference presentation of thesis research.",
                "amount": "Up to THB 20,000 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free CU Pop Bus (electric shuttle transit) connecting all campus faculties, CU iHouse, Siam BTS station, and Sam Yan MRT station.",
                "amount": "Free campus electric shuttle network"
            },
            "total_estimated_value_usd_per_year": 21000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Thailand #1 premier flagship comprehensive university (Chulalongkorn University - Chula).",
            "participating_institutions": [
                "Chulalongkorn University Main Campus (Pathumwan, Central Bangkok, Thailand)"
            ],
            "university_rankings_scope": "QS World University Rankings #229 globally, #1 in Thailand for 15 consecutive years; world-renowned for chemical engineering, petroleum technology, medicine, and materials science.",
            "available_majors": [
                "Master's / PhD in Chemical Engineering",
                "Master's / PhD in Petroleum and Petrochemical Technology (PPC)",
                "Master's / PhD in Biomedical Engineering",
                "Master's / PhD in Computer Science and Information Technology",
                "Master's / PhD in Pharmaceutical Sciences and Technology",
                "Master's / PhD in Materials Science and Engineering",
                "Master's / PhD in Environmental Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.25/4.00 (Master's) or 3.50/4.00 (PhD), academic transcripts, research proposal, two recommendation letters, medical certificate, and English proficiency test (IELTS 6.0+ / TOEFL 79+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Petroleum and Petrochemical College (PPC, partnered with Univ of Michigan and Univ of Oklahoma) and Faculty of Engineering are highly selective; contacting prospective supervisors in advance strongly aids faculty nomination.",
            "strategic_program_match_advice": "Focus research proposals on polymer chemistry, sustainable petrochemicals, biomaterials, or green energy catalysis where Chulalongkorn leads Southeast Asia."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://www.academic.chula.ac.th/scholarship02.html & https://www.inter.chula.ac.th/",
            "portal_system_name": "Chulalongkorn University International Graduate Scholarship Application System",
            "account_creation_instructions": "Identify target international program, download Non-ASEAN scholarship application form, submit admission and scholarship dossier to the program coordinator/faculty by the deadline.",
            "step_by_step_workflow": [
                "Step 1: Check target international graduate program at Chulalongkorn University and contact program coordinator.",
                "Step 2: Complete the Application Form for Graduate Scholarship Programme for Non-ASEAN Countries.",
                "Step 3: Compile transcripts, degree certificates, research proposal, medical certificate, CV, and English test scores.",
                "Step 4: Submit complete application dossier to the relevant Faculty/Program at Chulalongkorn University before the faculty deadline (typically February-March).",
                "Step 5: Faculty evaluates academic credentials and conducts online technical interviews.",
                "Step 6: Faculty selects top candidates and nominates them to the University Scholarship Committee.",
                "Step 7: Office of International Affairs issues official award notification in May.",
                "Step 8: Receive admission letter, apply for Thai Non-Immigrant ED Visa at Thai Embassy in Islamabad, and book flight provided by Chulalongkorn."
            ],
            "university_vs_scholarship_routing": "Integrated Faculty-to-University Route: Application submitted directly to target faculty, which screens applicants and forwards nominations to central university scholarship board.",
            "recommendation_letters_submission_method": "Submitted as two confidential recommendation letters signed by university professors in sealed envelopes or sent directly via official institutional email.",
            "personal_statement_prompts": "Statement of Purpose describing academic background, research interests, career vision, and why Chulalongkorn University is the desired destination.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) detailing problem formulation, methodology, literature review, and anticipated contributions.",
            "cv_format_requirements": "Comprehensive academic CV detailing education, laboratory techniques, research publications, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "IELTS Academic 6.0+, TOEFL iBT 79+, CU-TEP 75+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "THB 1,000 (approx. USD 30 / ~PKR 7,500)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations recommended for Pakistani credentials.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Submission of application dossier to target faculty/program graduate office."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.25 (Master's) or 3.50 (PhD).",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Non-ASEAN Scholarship Application Form",
                "mandatory": True,
                "specification": "Official prescribed application form completed in English with passport-style photograph.",
                "pakistan_specific_instruction": "Standard official Chulalongkorn template."
            },
            {
                "document_name": "Detailed Statement of Purpose and Research Proposal",
                "mandatory": True,
                "specification": "2-4 page structured proposal outlining proposed research problem and methodology.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Two Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors on institutional letterhead.",
                "pakistan_specific_instruction": "Signed and stamped with official university seals."
            },
            {
                "document_name": "Medical Certificate Form",
                "mandatory": True,
                "specification": "Official medical certificate completed and signed by an authorized physician within past 6 months.",
                "pakistan_specific_instruction": "Issued by recognized hospital or diagnostic laboratory."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic 6.0+, TOEFL iBT 79+, CU-TEP 75+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "Score report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV) and Passport Copy",
                "mandatory": True,
                "specification": "Academic resume and clear color copy of international passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "December 1",
            "application_deadline": "February 28 (Faculty submission deadline for August intake)",
            "university_admission_deadline": "February 28",
            "document_submission_deadline": "February 28",
            "recommendation_letters_deadline": "March 5",
            "interview_period": "March - April",
            "shortlist_announcement": "Mid May",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "June - July",
            "semester_commencement": "August 1 (Fall intake)",
            "annual_cycle_notes": "Single annual admission cycle for August intake; application deadline to faculties is strictly late February."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic consistency in STEM fields)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and intercultural adaptability)",
            "research_experience_weight": "35% (Research proposal rigor, engineering problem solving, and technical depth)",
            "work_experience_weight": "5% (Professional engineering or laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with faculty priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit-driven based on academic CGPA)",
            "selection_panel_composition": "Faculty Graduate Committee, School Deans, and Chulalongkorn University Scholarship Selection Board.",
            "evaluation_methodology": "Two-stage evaluation: departmental technical vetting of research alignment followed by central university award confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 non-ASEAN applicants across faculties",
            "total_scholarships_awarded": "~50 to 80 Non-ASEAN scholarship awards annually",
            "acceptance_rate_global": "~6.0% to 7.5%",
            "acceptance_rate_pakistan": "~10.0% to 14.0% for candidates with strong engineering/science backgrounds and CGPA >= 3.55",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.55 / 4.00, accompanied by strong laboratory foundations",
            "typical_academic_and_research_profile": "Graduates in chemical engineering, petroleum, materials, computing, or pharmaceutical sciences with solid research proposals.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, UET Lahore, NED Karachi, Quaid-i-Azam, FAST-NUCES, COMSATS).",
            "high_representation_countries": "Pakistan, India, Bangladesh, Nepal, Sri Lanka, Egypt, Nigeria, Russia, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portals academic.chula.ac.th and inter.chula.ac.th.",
                "Chulalongkorn does not work with third-party agents; all applications must be submitted directly to target faculties."
            ],
            "application_fee_warning": "Faculty application processing fee of THB 1,000 is paid directly through secure university banking channels.",
            "agent_and_intermediary_warnings": "Commercial agency written proposals are rejected; applicants must write their own research proposals.",
            "hidden_costs_breakdown": [
                "Application fee: THB 1,000 (~PKR 7,500).",
                "Thai Student Visa fee in Pakistan: ~PKR 15,000.",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 15,000.",
                "Initial pocket money before first stipend cycle: ~THB 10,000 (~PKR 75,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Thai language is required. Reality: All international programs at Chulalongkorn are conducted 100% in English.",
                "Myth: Flights are self-funded. Reality: The Non-ASEAN scholarship explicitly covers economy class round-trip international airfare."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites suggest accommodation is not funded; the scholarship provides a dedicated THB 7,000/month accommodation allowance."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.25 out of 4.00 throughout degree study.",
            "attendance_requirements": "Full-time physical research presence at Chulalongkorn campus; residence at CU iHouse or nearby university housing.",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by academic advisor and presented to Graduate School.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment during the study period.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment globally upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond.",
            "repayment_clawback_conditions": "Termination of scholarship if GPA falls below required standard or for academic misconduct.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Field of study cannot be changed after enrollment.",
            "extension_policy": "Maximum tenure is 2 years (Master's) and 3 years (PhD); extensions are generally not funded by the scholarship."
        },
        "official_sources_verified": [
            {
                "source_name": "Chulalongkorn University Graduate Scholarship for Non-ASEAN Countries",
                "source_url": "http://www.academic.chula.ac.th/scholarship02.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Chulalongkorn University Office of International Affairs",
                "source_url": "https://www.inter.chula.ac.th/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
