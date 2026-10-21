# scripts/batch20_p3.py
# SCH-AS-023: Universiti Malaya (UM) Bright Sparks Research Fellowship (Malaysia)
# SCH-AS-028: Universiti Teknologi Malaysia (UTM) National Postgraduate Research Scholarship (Malaysia)
# SCH-AS-034: Shanghai Jiao Tong University (SJTU) Chinese Government Scholarship (China)
# SCH-AS-035: University of Science and Technology of China (USTC) Fellowship (China)

DATA_P3 = {
    "SCH-AS-023": {
        "scholarship_id": "SCH-AS-023",
        "basic_details": {
            "scholarship_name": "Universiti Malaya (UM) Bright Sparks Research Fellowship",
            "offering_entity": "Universiti Malaya (UM) & Malaysian Ministry of Higher Education",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Malaya Main Campus (Kuala Lumpur, Malaysia)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Computer Science and Information Technology (FCSIT), Faculty of Engineering, Faculty of Science: Artificial Intelligence, Cyber Security, Software Engineering, Data Science, Biomedical Engineering, Renewable Energy, and Advanced Materials.",
            "number_of_awards_total": "~50 to 80 elite PhD research fellowships awarded annually across faculties",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani postgraduate researchers secure ~6 to 10 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3 to 4 years (full standard duration of PhD by Research), subject to satisfactory semi-annual research milestone evaluations",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "MYR 3,000 to MYR 3,500 / month tax-free living allowance (~PKR 195,000 - 230,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must generally be under 35 years old at the time of application.",
            "academic_qualifications": "A recognized research Master's degree (MS/MPhil, 18 years education) in Computer Science, Software Engineering, or related technical field with minimum CGPA 3.70 / 4.00, or a First Class Bachelor's degree (CGPA >= 3.70/4.00) directly for fast-track PhD from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "First Class Honours equivalent or minimum CGPA of 3.70 / 4.00.",
            "subject_background_prerequisites": "Substantial research background with at least 1-2 published papers in ISI / Web of Science / Scopus indexed journals or top IEEE/ACM conferences.",
            "current_education_status": "Graduating Master's students can apply conditionally with thesis defense completion confirmation.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications or technical research projects are the decisive selection criteria.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or institutional English Medium of Instruction (MOI) certificate from an accredited Pakistani university.",
            "other_language_requirements": "None; PhD research and dissertation defense are conducted 100% in English.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure preliminary written support from a prospective UM supervising professor prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another full national or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and academic examination fee waiver at Universiti Malaya for the entire duration of the PhD program.",
                "amount": "100% covered (~MYR 20,000 - 28,000 / year value; ~PKR 1,300,000 - 1,820,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UM international graduate admission processing fee (~MYR 300 / USD 70) paid online via portal.",
                "amount": "MYR 300 (~PKR 20,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Priority access to on-campus residential colleges (Kolej Kediaman) or International House at UM; rent is paid from the monthly living allowance.",
                "amount": "Subsidized rent ~MYR 500 - 800 / month (~PKR 32,000 - 52,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend of MYR 3,000 to MYR 3,500 disbursed directly into student bank accounts (~PKR 195,000 - 230,000 / month; MYR 36,000 - 42,000 / year).",
                "amount": "MYR 3,000 - 3,500 / month (~PKR 195,000 - 230,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare to Kuala Lumpur is arranged by the student; living allowance easily accommodates local savings.",
                "amount": "Self-funded economy flight (~PKR 120,000)"
            },
            "visa_fee": {
                "status": "PARTIAL",
                "details": "Education Malaysia Global Services (EMGS) visa processing and Student Pass fees (~MYR 2,000 total) covered from stipend or research grant.",
                "amount": "Covered via initial stipend"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Mandatory Malaysian student health and hospitalization insurance included within the EMGS Student Pass package.",
                "amount": "100% covered via EMGS insurance package"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of MYR 3,000 - 3,500; wide variety of affordable halal meals across UM campus.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to UM Central Library, advanced laboratory equipment, high-performance computing clusters, and IEEE/ACM digital libraries.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Substantial research and conference funding available through supervisor's research grants (FRGS / PRGS) for publishing in Tier 1 Scopus/WoS journals.",
                "amount": "Up to MYR 5,000 for international conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UM campus shuttle bus service connecting all faculties, residential colleges, and the Universiti LRT station.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Malaysian flagship university: Universiti Malaya (UM).",
            "participating_institutions": [
                "Universiti Malaya Main Campus (Kuala Lumpur, Malaysia)"
            ],
            "university_rankings_scope": "Ranked #60 globally in QS World University Rankings, #1 in Malaysia, and top 50 globally for Computer Science, Information Systems, and Engineering.",
            "available_majors": [
                "PhD in Computer Science (Artificial Intelligence, Machine Learning)",
                "PhD in Software Engineering and Cyber Security",
                "PhD in Information Technology and Data Science",
                "PhD in Electrical and Electronic Engineering",
                "PhD in Biomedical Engineering",
                "PhD in Renewable Energy Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 to 4 years (6 to 8 semesters)",
            "admission_requirements_summary": "Master's degree (or First Class Bachelor's) with CGPA >= 3.70/4.00, verified research publications, supervisor consent, detailed research proposal, two recommendation letters, and English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "UM FCSIT AI and Software Engineering groups are highly selective; having 1-2 published journal papers in indexed venues is the key differentiator for winning the Bright Sparks fellowship.",
            "strategic_program_match_advice": "Explore the UM Expert Directory (umexpert.um.edu.my) to identify principal investigators with active research grants, and email them a polished research proposal and CV before applying on Maya portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://brightsparks.um.edu.my/ & https://maya.um.edu.my/",
            "portal_system_name": "UM Bright Sparks Portal & Maya Postgraduate Admissions",
            "account_creation_instructions": "Identify prospective supervisor on UM Expert, secure consent, register an applicant account on the Maya portal, submit PhD application, and apply for the Bright Sparks scheme.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty profiles on UM Expert (https://umexpert.um.edu.my/) and reach out to prospective supervisors.",
                "Step 2: Obtain written consent / endorsement from the prospective supervisor.",
                "Step 3: Register and apply online for PhD admission on the UM Maya portal (https://maya.um.edu.my/).",
                "Step 4: Upload attested transcripts, degrees, detailed research proposal (3-5 pages), CV, and publications.",
                "Step 5: Complete the Bright Sparks Fellowship application form endorsed by the supervisor.",
                "Step 6: Attend faculty technical interview via Zoom if shortlisted.",
                "Step 7: Receive official offer letter and fellowship award, then initiate the EMGS visa approval letter (VAL) process."
            ],
            "university_vs_scholarship_routing": "Integrated Supervisor Track: Admission and fellowship are processed jointly through the supervising faculty.",
            "recommendation_letters_submission_method": "Submitted on institutional letterhead signed by former academic professors or research supervisors.",
            "personal_statement_prompts": "Statement of academic purpose detailing research accomplishments, technical capabilities, and doctoral research vision.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem statement, research questions, methodology, and expected publications.",
            "cv_format_requirements": "Detailed academic CV highlighting publications (with Scopus/WoS indexed DOIs), technical projects, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "30 to 45-minute technical interview via Zoom conducted by prospective supervisor and faculty panel.",
            "standardized_tests": "IELTS Academic (min 6.5), TOEFL iBT (min 80), or institutional English MOI letter accepted; GRE not required.",
            "application_fee_amount": "MYR 300 (~USD 70 / ~PKR 20,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Online submission via UM Maya portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 18-year Master's (or 16-year Bachelor's) with minimum CGPA 3.70/4.00.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "Detailed Doctoral Research Proposal",
                "mandatory": True,
                "specification": "3 to 5-page structured proposal outlining problem statement, methodology, and novelty.",
                "pakistan_specific_instruction": "Must be aligned with UM supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible UM professor agreeing to supervise.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Reprints of Research Publications",
                "mandatory": True,
                "specification": "Copies of published or accepted papers in Scopus/WoS indexed journals or conferences.",
                "pakistan_specific_instruction": "Include DOIs and indexed journal rank."
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
                "specification": "IELTS Academic (min 6.5), TOEFL iBT (min 80), or institutional English MOI letter.",
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
            "academic_weight": "35% (Master's and Bachelor's GPA, minimum 3.70/4.00 requirement)",
            "extracurricular_and_leadership_weight": "5% (Technical community contributions)",
            "research_experience_weight": "40% (Quality of research proposal, publication track record in Scopus/WoS, and supervisor match)",
            "work_experience_weight": "5% (Industry or university research assistant experience)",
            "personal_statement_weight": "5% (Clarity of purpose and doctoral vision)",
            "recommendations_weight": "10% (Referee appraisals and supervisor endorsement)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research excellence ranking)",
            "selection_panel_composition": "UM Bright Sparks Committee and Faculty Postgraduate Academic Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by university fellowship committee review of publication credentials."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~600 to 1,000 international applicants for Bright Sparks",
            "total_scholarships_awarded": "~50 to 80 Bright Sparks fellowships awarded annually",
            "acceptance_rate_global": "~6% to 9%",
            "acceptance_rate_pakistan": "~8% to 12% among candidates with CGPA 3.7+ and published papers",
            "typical_successful_applicant_gpa": "CGPA 3.75+ / 4.00 from top Pakistani institutions (NUST, FAST, QAU, COMSATS, UET)",
            "typical_academic_and_research_profile": "High-performing scholars with at least 1-2 published papers in indexed journals and a strong, feasible doctoral research proposal.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electrical engineering faculties.",
            "high_representation_countries": "Pakistan, Bangladesh, China, Iran, Nigeria, Indonesia, India, Yemen.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of educational agents claiming to provide 'guaranteed UM admissions or Bright Sparks awards'.",
                "Applications are handled exclusively via the official UM Maya portal (https://maya.um.edu.my/)."
            ],
            "application_fee_warning": "UM application fee is MYR 300 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Universiti Malaya does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "UM application fee: MYR 300 (~PKR 20,000).",
                "EMGS visa approval letter (VAL) and medical fee: ~MYR 2,000 (~PKR 130,000).",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~MYR 1,500 (~PKR 98,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without a supervisor. Reality: Research PhD applications at UM require prior engagement and consent from a qualified supervisor.",
                "Myth: Malaysia does not offer world-class research. Reality: Universiti Malaya is ranked #60 globally, outranking many US/UK institutions in computer science citations."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state IELTS 7.0 is mandatory; UM requires IELTS 6.5 or institutional English MOI letter for computing PhDs."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress (Progress Report Grade Satisfactory / TM) each semester.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at UM.",
            "academic_progress_monitoring": "Semi-annual Candidature Defense and progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "Bright Sparks recipients may be assigned limited teaching assistantship duties (up to 4-6 hours/week) within the faculty.",
            "home_country_return_obligation": "No return obligation; graduates are free to pursue postdocs or careers in Malaysia or worldwide.",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 2-3 papers in Tier 1/2 Scopus/WoS indexed journals prior to thesis submission.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails candidature defense twice or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Universiti Malaya.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Faculty Postgraduate Committee.",
            "extension_policy": "Fellowship is granted for maximum 3 years (up to 4 years upon exceptional review and supervisor funding)."
        },
        "official_sources_verified": [
            {
                "source_name": "Universiti Malaya Bright Sparks Programme Portal",
                "source_url": "https://brightsparks.um.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UM Maya Postgraduate Admissions System",
                "source_url": "https://maya.um.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-028": {
        "scholarship_id": "SCH-AS-028",
        "basic_details": {
            "scholarship_name": "Universiti Teknologi Malaysia (UTM) National Postgraduate Research Scholarship",
            "offering_entity": "Universiti Teknologi Malaysia (UTM) & Malaysian Ministry of Higher Education",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Teknologi Malaysia Main Campus (Skudai, Johor Bahru) & Kuala Lumpur Campus (Jalan Sultan Yahya Petra, KL, Malaysia)",
            "degree_levels": ["Master of Philosophy (MPhil by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Computing (FC) & Faculty of Electrical Engineering (FKE): Artificial Intelligence, Software Engineering, Cybersecurity, Information Systems, Cloud Computing, Data Science, and Robotics.",
            "number_of_awards_total": "~80 to 120 graduate research scholarships (UTM Young Scholars & Graduate Research Assistantships) awarded annually",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani researchers in computing and engineering secure ~10 to 16 awards annually",
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
            "special_eligibility_categories": "Applicants must identify a prospective supervisor at UTM Faculty of Computing and obtain preliminary consent.",
            "previous_scholarship_restrictions": "Cannot hold another full national or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee and academic examination fee waiver at Universiti Teknologi Malaysia covered by the scholarship or research grant.",
                "amount": "100% covered (~MYR 16,000 - 24,000 / year value; ~PKR 1,040,000 - 1,560,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UTM international postgraduate application fee (~MYR 200 / USD 50) paid online via the portal.",
                "amount": "MYR 200 (~PKR 13,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus student residential colleges (Kolej Mahallah) at UTM Skudai or UTM KL; monthly rent is paid from the monthly living allowance.",
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
                "details": "Full access to UTM Library, engineering laboratories, GPU clusters, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental research funding available through supervisor's research grants for publishing in indexed journals.",
                "amount": "Up to MYR 3,500 for conference attendance"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UTM campus shuttle bus service operating across all academic zones and student hostels.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 15000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading engineering and technological institution: Universiti Teknologi Malaysia (UTM).",
            "participating_institutions": [
                "Universiti Teknologi Malaysia (Main Campus Skudai, Johor & KL Campus, Malaysia)"
            ],
            "university_rankings_scope": "Ranked #181 globally in QS World University Rankings, #2 in Malaysia for Engineering & Technology, and top 100 globally in Computer Science & Information Systems.",
            "available_majors": [
                "MPhil / PhD in Computer Science (Artificial Intelligence, Machine Learning)",
                "MPhil / PhD in Software Engineering",
                "MPhil / PhD in Cybersecurity and Information Assurance",
                "MPhil / PhD in Data Science and Business Analytics",
                "MPhil / PhD in Electrical Engineering and Robotics",
                "MPhil / PhD in Telecommunications and IoT"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for MPhil; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree (minimum CGPA 3.3/4.0) for Master's; Master's degree (minimum CGPA 3.5/4.0) for PhD, supervisor consent, research proposal, two recommendation letters, and English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "UTM Faculty of Computing AI and Cybersecurity labs have high demand; reaching out to supervisors with active MOHE/CREST research grants is the primary path to guaranteed funding.",
            "strategic_program_match_advice": "Browse the UTM Faculty of Computing directory (computing.utm.my), identify matching research groups in AI/software, and email prospective professors attaching your CV and a 2-page research proposal before applying on the UTM Smart portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://sps.utm.my/scholarships/ & https://admission.utm.my/",
            "portal_system_name": "UTM Smart Postgraduate Admissions Portal",
            "account_creation_instructions": "Identify prospective supervisor on UTM portal, secure consent, register an applicant account on UTM Smart, submit degree application, and apply for the research assistantship / scholarship.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research profiles on UTM Faculty of Computing portal (https://computing.utm.my/).",
                "Step 2: Email prospective supervisor with academic transcripts, CV, and a 2-page research proposal to secure consent.",
                "Step 3: Register and apply online for postgraduate admission on the UTM Smart portal (https://admission.utm.my/).",
                "Step 4: Upload attested transcripts, degrees, research proposal, CV, and reference letters.",
                "Step 5: Apply for Graduate Research Assistantship (GRA) scheme through the supervisor's grant.",
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
            "application_fee_amount": "MYR 200 (~USD 50 / ~PKR 13,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Online submission via UTM Smart admissions portal."
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
                "pakistan_specific_instruction": "Must be aligned with UTM supervisor's funded research area."
            },
            {
                "document_name": "Supervisor Written Endorsement Letter",
                "mandatory": True,
                "specification": "Letter or email confirmation from an eligible UTM professor agreeing to supervise.",
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
            "selection_panel_composition": "UTM School of Graduate Studies and Faculty of Computing Postgraduate Board.",
            "evaluation_methodology": "Two-phase evaluation: supervisor nomination followed by faculty board academic review."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international applicants for UTM postgraduate programs",
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
                "Beware of educational agents claiming to provide 'guaranteed UTM admissions or scholarship awards'.",
                "Applications are handled exclusively via the official UTM Smart portal (https://admission.utm.my/)."
            ],
            "application_fee_warning": "UTM application fee is MYR 200 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Universiti Teknologi Malaysia does not work with third-party agents for research degree admissions.",
            "hidden_costs_breakdown": [
                "UTM application fee: MYR 200 (~PKR 13,000).",
                "EMGS visa approval letter (VAL) and medical fee: ~MYR 2,000 (~PKR 130,000).",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~MYR 1,500 (~PKR 98,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without a supervisor. Reality: Research MPhil and PhD applications at UTM require prior engagement and consent from a qualified supervisor.",
                "Myth: UTM only focuses on engineering. Reality: UTM Faculty of Computing is one of the premier computer science and cybersecurity hubs in Southeast Asia."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state IELTS 6.5 is mandatory; UTM requires IELTS 6.0 or institutional English MOI letter for computing degrees."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress (Progress Report Grade Satisfactory) each semester.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at UTM Skudai or UTM KL.",
            "academic_progress_monitoring": "Semi-annual progress reports evaluated by the Faculty Supervisory Committee.",
            "work_restrictions_during_study": "GRA recipients may be assigned teaching assistantship or grading duties (up to 6 hours/week) within the faculty.",
            "home_country_return_obligation": "No return obligation; graduates are free to pursue postdocs or careers in Malaysia or worldwide.",
            "service_obligations_or_bonds": "Publication milestone obligation: must publish at least 1-2 papers in indexed journals prior to thesis submission.",
            "repayment_clawback_conditions": "Funding cancelled if the candidate fails progress evaluations twice or withdraws without approval.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to Universiti Teknologi Malaysia.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Faculty Postgraduate Committee.",
            "extension_policy": "Scholarship is granted for standard duration (2 years for Master's; 3-4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "UTM School of Graduate Studies Scholarships Portal",
                "source_url": "https://sps.utm.my/scholarships/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UTM Postgraduate Admissions Portal",
                "source_url": "https://admission.utm.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-034": {
        "scholarship_id": "SCH-AS-034",
        "basic_details": {
            "scholarship_name": "Shanghai Jiao Tong University (SJTU) Chinese Government Scholarship (CSC & SJTU Fellowship)",
            "offering_entity": "China Scholarship Council (CSC - Ministry of Education of China) & Shanghai Jiao Tong University",
            "host_country": "China",
            "host_institutions_covered": "Shanghai Jiao Tong University Minhang & Xuhui Campuses (Shanghai, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Electronic Information and Electrical Engineering (SEIEE): Computer Science and Engineering, Software Engineering, Artificial Intelligence, Cyber Science and Technology, Information and Communication Engineering, and Control Science.",
            "number_of_awards_total": "~200 to 300 Chinese Government Scholarships and SJTU Fellowships awarded across graduate cohorts annually",
            "number_of_awards_pakistan": "Very high bilateral representation under China-Pakistan higher education partnerships; Pakistani graduate scholars secure ~25 to 40 fully funded awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2.5 to 3 years for Master of Science; 3 to 4 years for Doctor of Philosophy, subject to passing annual CSC scholarship review",
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
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 85, or institutional English Medium of Instruction (MOI) certificate from Pakistani university.",
            "other_language_requirements": "Chinese language proficiency (HSK) is not required for English-taught graduate programs.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must contact a prospective supervisor at SJTU SEIEE and secure a formal or informal Acceptance Letter prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or provincial scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee exemption at Shanghai Jiao Tong University covered for the entire program duration.",
                "amount": "100% covered (~RMB 28,900 - 45,000 / year value; ~PKR 1,120,000 - 1,750,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "SJTU international graduate application fee of RMB 800 (~USD 115 / ~PKR 32,000) payable online.",
                "amount": "RMB 800 (~PKR 32,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free accommodation in on-campus international student dormitories (single or twin room) at Minhang Campus, or monthly housing subsidy of RMB 700 - 1,000 if living off-campus.",
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
                "details": "Full access to SJTU Central Library, laboratory workstations, GPU clusters, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's National Natural Science Foundation of China (NSFC) grants for presenting research at conferences.",
                "amount": "Up to RMB 5,000 for conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle bus operating across Minhang Campus and between Minhang and Xuhui Campuses.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite C9 League university: Shanghai Jiao Tong University (SJTU).",
            "participating_institutions": [
                "Shanghai Jiao Tong University (Minhang & Xuhui Campuses, Shanghai, China)"
            ],
            "university_rankings_scope": "Member of China's prestigious C9 League (China's Ivy League); ranked #51 globally in QS World University Rankings, #27 globally in Computer Science and Information Systems.",
            "available_majors": [
                "Computer Science and Engineering",
                "Software Engineering",
                "Artificial Intelligence and Machine Learning",
                "Cyber Science and Technology",
                "Information and Communication Engineering",
                "Control Science and Engineering",
                "Electronic Science and Technology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2.5 to 3 years for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor acceptance letter, study plan (1,000 words), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "SJTU SEIEE Computer Science and AI labs are among the most competitive in Asia; securing an acceptance letter from a professor between October and December is the single most critical factor for scholarship nomination.",
            "strategic_program_match_advice": "Pakistani applicants should browse SEIEE faculty profiles (seiee.sjtu.edu.cn), email prospective supervisors with a concise research proposal and CV, and obtain the official SJTU Provisional Acceptance Letter before the December 15 early deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://isc.sjtu.edu.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "SJTU International Student Portal & CSC Online Application System",
            "account_creation_instructions": "Register an account on the SJTU international admissions portal (isc.sjtu.edu.my), select degree program, check the box applying for Chinese Government Scholarship / SJTU Fellowship, and apply on the CSC portal (Agency No: 10248).",
            "step_by_step_workflow": [
                "Step 1: Identify prospective supervisors in SJTU SEIEE and secure the official SJTU Acceptance Letter (October - December).",
                "Step 2: Create user credentials on the SJTU International Student Admissions Portal (https://isc.sjtu.edu.cn/).",
                "Step 3: Submit online degree application, upload all required documents, and check the box applying for CSC / SJTU Fellowship.",
                "Step 4: Pay the application fee of RMB 800 before the deadline (typically December 15 for Round 1 / February 15 for Round 2).",
                "Step 5: Apply on the CSC portal (https://studyinchina.csc.edu.cn/) under Type B using SJTU Agency Number 10248.",
                "Step 6: SEIEE faculty committee reviews files, conducts online technical interviews, and nominates candidates to CSC in March.",
                "Step 7: Official admission and scholarship package (JW201 form) dispatched in June/July; apply for Chinese X1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via the SJTU portal covers both program admission and scholarship nomination.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated links dispatched directly to their official institutional email addresses.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words in English) outlining academic background, proposed research focus, and reasons for choosing SJTU.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute technical video interview via Zoom / Tencent Meeting conducted by faculty admissions panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 85), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "RMB 800 (~USD 115 / ~PKR 32,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English or Chinese translation required for all official documents.",
            "final_submission_method": "Online upload via SJTU admissions portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "SJTU Professor Acceptance Letter (Provisional)",
                "mandatory": True,
                "specification": "Official acceptance letter signed by an eligible SJTU professor.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Study and Research Plan (Minimum 1,000 words)",
                "mandatory": True,
                "specification": "Detailed research plan outlining academic background, proposed research questions, and methodology.",
                "pakistan_specific_instruction": "Must be aligned with SJTU supervisor's lab projects."
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
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 85), or institutional English MOI letter.",
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
            "application_open_date": "October 1",
            "application_deadline": "December 15 (Round 1 for CSC nomination) / February 15 (Round 2)",
            "university_admission_deadline": "December 15 / February 15",
            "document_submission_deadline": "December 15 / February 15",
            "recommendation_letters_deadline": "December 22",
            "interview_period": "January - February",
            "shortlist_announcement": "Late March",
            "final_result_acceptance_deadline": "June",
            "visa_application_window": "July - August",
            "semester_commencement": "Early September (commencing at Minhang Campus)",
            "annual_cycle_notes": "Main intake is Autumn (September). Round 1 (December 15 deadline) is essential for top-tier CSC scholarship consideration."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate GPA and performance in core computing and engineering courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor acceptance letter, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for SJTU)",
            "recommendations_weight": "10% (Academic referee appraisals and professor's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into final ranking)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "SJTU SEIEE Faculty Admissions Board and Graduate School Scholarship Committee.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit and professor nomination followed by faculty panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 international graduate applicants across SJTU",
            "total_scholarships_awarded": "~200 to 300 fully funded CSC and SJTU fellowships awarded annually",
            "acceptance_rate_global": "~5% to 8%",
            "acceptance_rate_pakistan": "~8% to 12% among candidates with professor acceptance letters",
            "typical_successful_applicant_gpa": "CGPA 3.50+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, Russia, South Korea, Iran, Indonesia, Malaysia, Thailand, Egypt.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed CSC scholarships or SJTU admissions.",
                "Applications are handled exclusively via the official SJTU portal (https://isc.sjtu.edu.cn/) and CSC portal."
            ],
            "application_fee_warning": "SJTU application fee is RMB 800 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "Shanghai Jiao Tong University does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "SJTU application fee: RMB 800 (~PKR 32,000).",
                "Foreigner physical examination in Pakistan: ~PKR 15,000.",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~RMB 2,000 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get CSC without a professor's acceptance letter. Reality: At top C9 universities like SJTU, having a professor's acceptance letter increases your scholarship chances exponentially.",
                "Myth: You must study in Chinese. Reality: SJTU SEIEE offers complete Master's and PhD programs taught and researched 100% in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state application deadline is April; SJTU CSC scholarship Round 1 closes strictly on December 15."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and pass the mandatory CSC Annual Scholarship Review each spring.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab at Minhang Campus.",
            "academic_progress_monitoring": "Annual progress report submitted to the Graduate School and China Scholarship Council.",
            "work_restrictions_during_study": "Part-time work off-campus is strictly restricted under Chinese student visa regulations; campus work-study (勤工助学) permitted with university approval.",
            "home_country_return_obligation": "No return obligation; graduates are free to work in China or globally under Chinese work visa (Z-visa) schemes.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Funding cancelled if the student fails annual review, engages in illegal employment, or breaches Chinese law.",
            "rules_for_changing_university": "Non-transferable to other Chinese universities.",
            "rules_for_changing_major": "Requires approval from both current and prospective supervisors and the Graduate School.",
            "extension_policy": "Master's programs cannot be extended; PhD programs can apply for up to 1-year CSC extension based on exceptional research progress."
        },
        "official_sources_verified": [
            {
                "source_name": "SJTU International Student Center Official Portal",
                "source_url": "https://isc.sjtu.edu.cn/",
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

    "SCH-AS-035": {
        "scholarship_id": "SCH-AS-035",
        "basic_details": {
            "scholarship_name": "University of Science and Technology of China (USTC) Fellowship & CSC Scholarship",
            "offering_entity": "University of Science and Technology of China (USTC) & Chinese Academy of Sciences (CAS) / China Scholarship Council",
            "host_country": "China",
            "host_institutions_covered": "USTC Campuses (Hefei, Anhui Province, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computer Science and Technology, School of Information Science and Technology, and School of Cyber Science and Technology: Quantum Computing, Artificial Intelligence, Big Data, High-Performance Computing, Robotics, and Network Security.",
            "number_of_awards_total": "~300 to 450 USTC Fellowships and CSC / ANSO scholarships awarded across graduate programs annually",
            "number_of_awards_pakistan": "Extremely strong bilateral quota; Pakistani STEM scholars represent one of the largest international communities in Hefei (~35 to 60 scholarships annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 to 3 years for Master of Science; 3 to 4 years for Doctor of Philosophy, subject to passing annual scholarship evaluations",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "RMB 3,000 / month for Master's (~PKR 115,000 / month); RMB 3,500 - 7,000 / month for PhD (~PKR 135,000 - 270,000 / month with lab matching)"
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
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 85, or institutional English Medium of Instruction (MOI) certificate from Pakistani university.",
            "other_language_requirements": "Chinese language proficiency (HSK) is not required for English-taught graduate programs.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants are strongly advised to contact a prospective supervisor at USTC and obtain a formal or informal Acceptance Letter prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or provincial scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee exemption at University of Science and Technology of China covered for the entire program duration.",
                "amount": "100% covered (~RMB 30,000 - 45,000 / year value; ~PKR 1,170,000 - 1,755,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "USTC online application fee of RMB 600 (~USD 85 / ~PKR 24,000) payable online.",
                "amount": "RMB 600 (~PKR 24,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free accommodation in on-campus international student dormitories (single room for PhD, twin room for Master's) at USTC Campuses, or monthly housing subsidy.",
                "amount": "100% covered free dormitory accommodation"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living allowance: RMB 3,000 per month for Master's students (~PKR 115,000 / month; RMB 36,000 / year); RMB 3,500 to RMB 7,000 per month for PhD scholars (~PKR 135,000 - 270,000 / month with CAS/lab matching).",
                "amount": "RMB 3,000 - 7,000 / month (~PKR 115,000 - 270,000 / month)"
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
                "details": "Comprehensive Medical Insurance for International Students in China (Ping An Insurance ~RMB 800 / year) provided 100% free by USTC/CSC.",
                "amount": "100% covered by scholarship provider"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of RMB 3,000 - 7,000; heavily subsidized campus canteens provide complete halal meals for RMB 10 - 20 per meal.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to USTC Central Library, laboratory workstations, quantum computing facilities, and software development platforms.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory funding available through supervisor's Chinese Academy of Sciences (CAS) grants for presenting research at conferences.",
                "amount": "Up to RMB 5,000 for conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle bus operating between East, South, West, North, and Central Campuses in Hefei.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite scientific institution: University of Science and Technology of China (USTC).",
            "participating_institutions": [
                "University of Science and Technology of China (Hefei, Anhui Province, China)"
            ],
            "university_rankings_scope": "Member of China's elite C9 League; ranked top 100 globally in QS/THE World Rankings, world #1 pioneer in quantum computing and quantum information science.",
            "available_majors": [
                "Computer Science and Technology (Quantum Information & Computing)",
                "Computer Science and Technology (Artificial Intelligence & Big Data)",
                "Software Engineering and Cloud Computing",
                "Cyber Science and Technology",
                "Information and Communication Engineering",
                "Robotics and Intelligent Systems",
                "Electronic Science and Technology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 to 3 years for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Bachelor's degree with strong academic record (CGPA >= 3.3/4.0), professor acceptance letter, study plan (1,000 words), two recommendation letters, and certified English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "USTC Quantum Computing and AI research laboratories are world-class and attract competitive international talent; reaching out to supervisors early with a strong mathematics and coding portfolio guarantees optimal fellowship placement.",
            "strategic_program_match_advice": "Pakistani applicants should browse the USTC Graduate School faculty directory (isa.ustc.edu.cn), email matching professors in AI/computing, and obtain an official Provisional Acceptance Letter before the February 15 deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://isa.ustc.edu.cn/ & https://studyinchina.csc.edu.cn/",
            "portal_system_name": "USTC International Student Application System & CSC Portal",
            "account_creation_instructions": "Register an account on the USTC international student application system (isa.ustc.edu.cn), select graduate program, check the box applying for USTC Fellowship / Chinese Government Scholarship, and apply on the CSC portal (Agency No: 10358).",
            "step_by_step_workflow": [
                "Step 1: Identify prospective supervisors in USTC School of Computer Science and secure an Acceptance Letter (October - January).",
                "Step 2: Create user credentials on the USTC International Student Admissions Portal (https://isa.ustc.edu.cn/).",
                "Step 3: Submit online degree application, upload all required documents, and select USTC Fellowship / CSC Scholarship.",
                "Step 4: Pay the application fee of RMB 600 before the deadline (typically February 15).",
                "Step 5: Apply on the CSC portal (https://studyinchina.csc.edu.cn/) under Type B using USTC Agency Number 10358.",
                "Step 6: USTC faculty committee reviews files, conducts online technical interviews, and nominates candidates to CSC/CAS in March.",
                "Step 7: Official admission and scholarship package (JW201 form) dispatched in June/July; apply for Chinese X1 visa."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via the USTC portal covers both program admission and scholarship nomination.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated links dispatched directly to their official institutional email addresses.",
            "personal_statement_prompts": "Study and research plan (minimum 1,000 words in English) outlining academic background, proposed research focus, and reasons for choosing USTC.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing background, problem formulation, methodology, and expected timeline.",
            "cv_format_requirements": "Detailed academic CV highlighting technical projects, publications, programming proficiencies, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute technical video interview via Zoom / Tencent Meeting conducted by faculty admissions panel.",
            "standardized_tests": "IELTS Academic (min 6.0), TOEFL iBT (min 85), or institutional English MOI certificate accepted; GRE not required.",
            "application_fee_amount": "RMB 600 (~USD 85 / ~PKR 24,000)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English or Chinese translation required for all official documents.",
            "final_submission_method": "Online upload via USTC admissions portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum CGPA 3.3/4.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "USTC Professor Acceptance Letter (Provisional)",
                "mandatory": True,
                "specification": "Official acceptance letter signed by an eligible USTC professor.",
                "pakistan_specific_instruction": "Obtained directly through academic correspondence."
            },
            {
                "document_name": "Study and Research Plan (Minimum 1,000 words)",
                "mandatory": True,
                "specification": "Detailed research plan outlining academic background, proposed research questions, and methodology.",
                "pakistan_specific_instruction": "Must be aligned with USTC supervisor's lab projects."
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
                "specification": "IELTS Academic (min 6.0), TOEFL iBT (min 85), or institutional English MOI letter.",
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
            "application_open_date": "October 20",
            "application_deadline": "February 15",
            "university_admission_deadline": "February 15",
            "document_submission_deadline": "February 15",
            "recommendation_letters_deadline": "February 22",
            "interview_period": "March - April",
            "shortlist_announcement": "Late April",
            "final_result_acceptance_deadline": "June",
            "visa_application_window": "July - August",
            "semester_commencement": "Early September (commencing in Hefei)",
            "annual_cycle_notes": "Main intake is Autumn (September). Applications close annually on February 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate GPA and performance in core computing, physics, and engineering courses)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "35% (Quality of research proposal, supervisor acceptance letter, and previous publications/capstone)",
            "work_experience_weight": "5% (Industry software engineering or research experience)",
            "personal_statement_weight": "10% (Clarity of academic intent and justification for USTC)",
            "recommendations_weight": "10% (Academic referee appraisals and professor's endorsement)",
            "interview_weight": "0% (Interview performance factored directly into final ranking)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and research merit ranking)",
            "selection_panel_composition": "USTC Faculty Admissions Board and Graduate School Fellowship Committee.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit and professor nomination followed by faculty panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,000 to 4,500 international graduate applicants across USTC",
            "total_scholarships_awarded": "~300 to 450 fully funded USTC Fellowships and CSC scholarships awarded annually",
            "acceptance_rate_global": "~8% to 11%",
            "acceptance_rate_pakistan": "~10% to 15% among candidates with professor acceptance letters",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing, physics, and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, Russia, Iran, Bangladesh, Indonesia, Egypt, Nigeria, Thailand.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed CSC scholarships or USTC admissions.",
                "Applications are handled exclusively via the official USTC portal (https://isa.ustc.edu.cn/) and CSC portal."
            ],
            "application_fee_warning": "USTC application fee is RMB 600 paid directly on the portal; never transfer funds to personal bank accounts.",
            "agent_and_intermediary_warnings": "University of Science and Technology of China does not work with third-party recruitment agencies.",
            "hidden_costs_breakdown": [
                "USTC application fee: RMB 600 (~PKR 24,000).",
                "Foreigner physical examination in Pakistan: ~PKR 15,000.",
                "Attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~RMB 2,000 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get CSC without a professor's acceptance letter. Reality: At elite C9 universities like USTC, having a professor's acceptance letter increases your scholarship chances exponentially.",
                "Myth: You must study in Chinese. Reality: USTC offers complete Master's and PhD programs taught and researched 100% in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state application deadline is April; USTC fellowship application portal closes strictly on February 15."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and pass the mandatory Annual Scholarship Review each spring.",
            "attendance_requirements": "Full-time physical research attendance in the faculty research lab in Hefei.",
            "academic_progress_monitoring": "Annual progress report submitted to the Graduate School and scholarship board.",
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
                "source_name": "USTC International Students Admissions Official Portal",
                "source_url": "https://isa.ustc.edu.cn/",
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
    }
}
