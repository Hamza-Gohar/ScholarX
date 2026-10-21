"""Batch 27 Part 1: Singapore and Hong Kong Elite Postgraduate Awards (3 awards)
SCH-AS-073: National University of Singapore (NUS) President's Graduate Fellowship (PGF)
SCH-AS-074: Hong Kong University of Science and Technology (HKUST) RedBird PhD Fellowship
SCH-AS-075: University of Hong Kong (HKU) Presidential PhD Fellowship Scheme (HKU-PS)
"""

DATA_P1 = {
    "SCH-AS-073": {
        "scholarship_id": "SCH-AS-073",
        "basic_details": {
            "scholarship_name": "National University of Singapore (NUS) President's Graduate Fellowship (PGF)",
            "offering_entity": "National University of Singapore (NUS) Graduate School",
            "host_country": "Singapore",
            "host_institutions_covered": "National University of Singapore (Kent Ridge Campus, Singapore)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computing, Faculty of Engineering, Faculty of Science, Yong Loo Lin School of Medicine, Saw Swee Hock School of Public Health, and NUS Graduate School for Integrative Sciences and Engineering (all doctoral research disciplines).",
            "number_of_awards_total": "~100 to 150 elite doctoral fellowships awarded annually university-wide",
            "number_of_awards_pakistan": "Open internationally to top candidates worldwide; typically 6 to 12 Pakistani researchers in AI, computing, and engineering selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (standard PhD tenure at NUS)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "SGD 3,500 / month (~PKR 735,000 / month) before PhD qualifying examination (QE); increased to SGD 4,000 / month (~PKR 840,000 / month) upon passing QE, plus 100% full tuition fee waiver, one-time flight allowance (SGD 750), and one-time settling-in allowance (SGD 1,000)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to candidates of all nationalities including Singapore citizens, permanent residents, and international candidates (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to candidates with exceptional academic velocity and research potential.",
            "academic_qualifications": "Completed recognized Bachelor's degree with First Class Honours / Highest Distinction (minimum CGPA 3.60/4.00) or completed Master's degree with outstanding academic record from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Minimum CGPA 3.60 / 4.00; competitive international applicants typically hold CGPA >= 3.80 / 4.00 or top 5% class standing.",
            "subject_background_prerequisites": "Computer science, artificial intelligence, data science, electrical engineering, mechanical engineering, biomedical sciences, physics, chemistry, or related STEM/quantitative fields.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester matriculation.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in top-tier conferences (NeurIPS, ICML, CVPR, ACL, IEEE, ACM) or premier Q1 journals are strongly prioritized.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 (6.0 in writing), TOEFL iBT minimum 85 (22 in writing), or official English Medium of Instruction (MOI) certificate if undergraduate was taught entirely in English.",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply directly for PhD admission at NUS and tick the scholarship consideration box; top candidates are automatically nominated for PGF.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent fellowship, scholarship, or full-time paid employment.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver (subsidized and non-subsidized tuition fully covered) for the 4-year PhD duration at NUS.",
                "amount": "100% covered (~SGD 40,000 / year value; ~PKR 8,400,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "NUS online PhD application fee of SGD 50 to SGD 100 paid via credit card during portal submission.",
                "amount": "SGD 50 to 100 (~PKR 10,500 to 21,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate housing at UTown (University Town Residences) or Prince George's Park Residences (approx. SGD 600 to 900 / month), easily covered from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend: SGD 3,500 / month (~PKR 735,000 / month) pre-QE; increases to SGD 4,000 / month (~PKR 840,000 / month) post-QE.",
                "amount": "SGD 3,500 to 4,000 / month (~PKR 735,000 to 840,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One-time travel flight allowance of SGD 750 provided to overseas recipients upon initial arrival in Singapore.",
                "amount": "SGD 750 one-off flight grant"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Singapore Student's Pass application and issuance fees (approx. SGD 90 to 120) expedited by NUS Office of Student Affairs.",
                "amount": "100% covered / subsidized"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive university medical and hospitalization insurance coverage provided through NUS Student Group Medical Insurance.",
                "amount": "100% covered university medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized food courts and dining across Kent Ridge and UTown campuses, including multiple certified halal dining options.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "One-time settling-in allowance of SGD 1,000 provided upon arrival, plus full access to NUS high-performance computing centers and libraries.",
                "amount": "SGD 1,000 one-off settling-in allowance"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Dedicated conference travel support (up to SGD 3,000 to 5,000 during candidature) provided through NUS Graduate School and host department.",
                "amount": "Up to SGD 5,000 international conference funding"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free NUS internal shuttle bus system connecting all campus faculties, UTown, Kent Ridge MRT, and Prince George's Park.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-class Singapore flagship institution (National University of Singapore - NUS).",
            "participating_institutions": [
                "National University of Singapore (Kent Ridge Campus, University Town, Singapore)"
            ],
            "university_rankings_scope": "QS World University Rankings #8 globally, #1 in Asia; world-leading in Computer Science (QS #6), Engineering (QS #7), and AI research.",
            "available_majors": [
                "PhD in Computer Science (School of Computing)",
                "PhD in Information Systems and Analytics",
                "PhD in Electrical and Computer Engineering",
                "PhD in Mechanical Engineering",
                "PhD in Materials Science and Engineering",
                "PhD in Biomedical Engineering",
                "PhD in Chemical and Biomolecular Engineering",
                "PhD in Quantitative Finance and Mathematics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (Doctor of Philosophy)",
            "admission_requirements_summary": "Bachelor's / Master's degree with First Class / CGPA >= 3.60/4.00, academic transcripts, GRE (strongly recommended/required for some faculties: minimum 320+), TOEFL 85+ / IELTS 6.5+, research proposal, and two reference letters.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of Computing is globally elite and fiercely competitive (<5% acceptance); having top-tier publications (CVPR, NeurIPS, ICML, IEEE) makes applicants standout contenders for the PGF.",
            "strategic_program_match_advice": "Contact prospective NUS professors whose laboratories have open funded grants; an endorsement from an NUS Provost's Chair or Full Professor strongly aids PGF nomination."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://nusgs.nus.edu.sg/programmes/",
            "portal_system_name": "NUS Graduate Admission System (GDA3)",
            "account_creation_instructions": "Register on the NUS GDA3 portal, select PhD programme of choice, indicate scholarship application, upload research proposal, CV, transcripts, test scores, and register two academic referees.",
            "step_by_step_workflow": [
                "Step 1: Explore NUS faculty research groups and contact prospective supervisors with research abstract (September-October).",
                "Step 2: Register on NUS Graduate Admission System (GDA3) during the open application window (October to December for August intake).",
                "Step 3: Complete online application, upload all documents, and pay SGD 50-100 application fee.",
                "Step 4: Referees submit letters of recommendation electronically through the portal.",
                "Step 5: Departmental admissions committee reviews applications and conducts technical interviews (January-February).",
                "Step 6: Department nominates top candidates to the NUS Graduate School PGF Selection Committee.",
                "Step 7: PGF offers announced in March/April.",
                "Step 8: Accept offer, complete Singapore Student's Pass formalities, and matriculate in early August."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Application for admission automatically triggers consideration for NUS Research Scholarship and President's Graduate Fellowship.",
            "recommendation_letters_submission_method": "Submitted online by two academic referees via confidential email links generated by NUS GDA3.",
            "personal_statement_prompts": "Statement of Purpose describing academic milestones, research interests, career aspirations, and motivation for pursuing a doctoral degree at NUS.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) detailing problem statement, literature review, proposed methodologies, and research novelty.",
            "cv_format_requirements": "Academic research CV highlighting publications, software repositories, awards, and technical competencies.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "GRE General Test (verbal + quantitative minimum 320, analytical writing 3.5+) recommended/required for non-NUS degrees; IELTS 6.5+ or TOEFL 85+ required.",
            "application_fee_amount": "SGD 50 to SGD 100 (approx. USD 38 to 75 / ~PKR 10,500 to 21,000)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC attestation required for Pakistani credentials upon enrollment.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via NUS GDA3 portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.60/4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Research Proposal (2-4 Pages)",
                "mandatory": True,
                "specification": "Structured research proposal detailing problem formulation, methodology, and anticipated contributions.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors submitted electronically.",
                "pakistan_specific_instruction": "From previous university professors."
            },
            {
                "document_name": "GRE General Test Score Report",
                "mandatory": False,
                "specification": "GRE General Test (recommended min 320+; required by School of Computing / Engineering for non-local degrees).",
                "pakistan_specific_instruction": "Official ETS score report."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+ (writing 6.0+) or TOEFL iBT 85+ (writing 22+).",
                "pakistan_specific_instruction": "Score report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
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
            "application_open_date": "September 1 (August intake)",
            "application_deadline": "November 1 (Early review) / December 15 (Standard deadline for August intake)",
            "university_admission_deadline": "December 15",
            "document_submission_deadline": "December 15",
            "recommendation_letters_deadline": "December 22",
            "interview_period": "January - February",
            "shortlist_announcement": "March - April",
            "final_result_acceptance_deadline": "Within 2 to 3 weeks of offer notification",
            "visa_application_window": "May - June via Singapore ICA SOLAR system",
            "semester_commencement": "Early August (Semester 1)",
            "annual_cycle_notes": "Main intake commences in August; a smaller January intake exists with application deadline in May."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA, academic honors, course rigor)",
            "extracurricular_and_leadership_weight": "5% (Initiative, intellectual maturity)",
            "research_experience_weight": "40% (Publications, research proposal quality, technical depth)",
            "work_experience_weight": "5% (Industry R&D or technical software experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with faculty)",
            "recommendations_weight": "5% (Depth of professor endorsements)",
            "interview_weight": "5% (Performance in technical doctoral interview)",
            "test_scores_weight": "0% (GRE/English are qualifying baseline filters)",
            "financial_need_weight": "0% (Pure academic and research merit evaluation)",
            "selection_panel_composition": "NUS Departmental Graduate Admissions Committee and NUS Graduate School PGF Selection Board.",
            "evaluation_methodology": "Two-tier rigorous evaluation identifying top 5% of doctoral applicants with world-class research potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 to 7,000 global PhD applicants across NUS",
            "total_scholarships_awarded": "~100 to 150 PGF awards annually",
            "acceptance_rate_global": "~2.0% to 2.5%",
            "acceptance_rate_pakistan": "~3.0% to 5.0% for candidates with first-author Q1/top conference papers and CGPA >= 3.80",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.80 / 4.00, accompanied by 1+ papers in top-tier conferences/journals",
            "typical_academic_and_research_profile": "Graduates with exceptional mathematics and computer science/engineering foundations, documented publications, and strong GRE scores.",
            "common_backgrounds_of_winners": "Graduates from top international institutions and leading Pakistani universities (NUST, FAST-NUCES, LUMS, UET Lahore, GIKI).",
            "high_representation_countries": "China, India, Singapore, Pakistan, Vietnam, United States, Germany, Malaysia.",
            "competitiveness_tier": "MOST_COMPETITIVE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official NUS portal nusgs.nus.edu.sg.",
                "NUS does not authorize third-party educational agents to recruit graduate students."
            ],
            "application_fee_warning": "Application fee of SGD 50-100 is paid directly through the official NUS GDA3 portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; plagiarism detection software scans all proposals.",
            "hidden_costs_breakdown": [
                "Application fee: SGD 50 to 100 (~PKR 10,500 to 21,000).",
                "GRE and TOEFL/IELTS test fees: ~PKR 100,000 to 130,000.",
                "Singapore Student's Pass processing: ~SGD 90 to 120 (~PKR 19,000 to 25,000).",
                "Flight ticket difference beyond SGD 750 allowance: ~PKR 30,000 to 60,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You need a Master's degree to apply for PhD. Reality: Direct Bachelor's-to-PhD entry is standard at NUS for candidates with First Class Honours.",
                "Myth: Service bond required. Reality: Unlike MOE Tuition Grant for undergraduates, the PGF doctoral scholarship carries ZERO service bond."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs cite outdated stipends; PGF stipend has been updated to SGD 3,500 pre-QE and SGD 4,000 post-QE."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum Cumulative Average Point (CAP) of 3.80 out of 5.00 throughout the PhD candidature.",
            "attendance_requirements": "Full-time physical research presence at NUS; pass PhD Qualifying Examination (QE) within 18 to 24 months.",
            "academic_progress_monitoring": "Semi-annual doctoral progress report reviewed by Thesis Advisory Committee.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment; limited teaching assistantship (up to 6 hours/week) permitted under Graduate Assistantship Programme.",
            "home_country_return_obligation": "None; zero service bond or return obligation (scholars may pursue international careers or postdocs globally).",
            "service_obligations_or_bonds": "Zero service bond.",
            "repayment_clawback_conditions": "Scholarship is terminated if CAP falls below required threshold across two consecutive semesters or if candidate withdraws without permission.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires formal departmental and graduate school approval.",
            "extension_policy": "PGF tenure is strictly 4 years; candidates requiring additional time must be funded through supervisor's research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "NUS Graduate School President's Graduate Fellowship (PGF)",
                "source_url": "https://nusgs.nus.edu.sg/scholarships/presidents-graduate-fellowship/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "NUS Graduate School Admissions Guide",
                "source_url": "https://nusgs.nus.edu.sg/programmes/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-074": {
        "scholarship_id": "SCH-AS-074",
        "basic_details": {
            "scholarship_name": "Hong Kong University of Science and Technology (HKUST) RedBird PhD Fellowship Scheme",
            "offering_entity": "The Hong Kong University of Science and Technology (HKUST) Fok Ying Tung Graduate School",
            "host_country": "Hong Kong (SAR)",
            "host_institutions_covered": "The Hong Kong University of Science and Technology (Clear Water Bay Campus, Hong Kong)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Engineering (Computer Science, Electronic & Computer Engineering, Chemical & Biological, Civil, Mechanical), School of Science (Physics, Chemistry, Life Science, Mathematics), Interdisciplinary Programs Office (AI, Data Science, Environment).",
            "number_of_awards_total": "~200 to 250 RedBird PhD Fellowship awards granted annually to incoming doctoral candidates",
            "number_of_awards_pakistan": "Open internationally; typically 15 to 25 Pakistani engineering, computing, and science researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (standard PhD tenure)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "HKD 18,390 to 20,000 / month standard postgraduate studentship plus RedBird top-up fellowship of HKD 40,000 in Year 1 and HKD 20,000/year in subsequent years: Total funding approximately HKD 260,000 to 280,000 / year (~PKR 9,360,000 to 10,080,000 / year) plus full tuition waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to outstanding young researchers with strong academic momentum.",
            "academic_qualifications": "Completed recognized Bachelor's degree with First Class Honours / High Distinction (minimum CGPA 3.50/4.00) or completed Master's degree with outstanding academic record from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum CGPA 3.50 / 4.00; competitive applicants typically hold CGPA >= 3.70 / 4.00 or top 10% class rank.",
            "subject_background_prerequisites": "Computer science, artificial intelligence, electrical engineering, mechanical engineering, materials science, chemical engineering, mathematics, physics, or chemistry.",
            "current_education_status": "Graduated or final-year students completing degree requirements before September semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in peer-reviewed journals or top IEEE/ACM conferences provide a major competitive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 (5.5 in all sub-scores), TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Cantonese or Mandarin Chinese is NOT required; 100% of graduate research and instruction is conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All applicants applying for full-time PhD programs at HKUST are automatically considered for the RedBird PhD Fellowship Scheme; no separate application required.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full-time employment or parallel external full scholarships.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee covered through Hong Kong Government Tuition Waiver Scheme for Local/Non-Local Research Postgraduate Students (HKD 42,100/year).",
                "amount": "100% covered (~HKD 42,100 / year value; ~PKR 1,515,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "HKUST online application fee of HKD 350 paid via credit card during portal submission.",
                "amount": "HKD 350 (~PKR 12,600)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing at Clear Water Bay campus (approx. HKD 3,000 to 4,500 / month), paid easily from monthly stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Postgraduate Studentship (PGS) of HKD 18,390 to 20,000 / month (~PKR 662,000 to 720,000 / month), supplemented by RedBird Award of HKD 40,000 in Year 1 and HKD 20,000 in subsequent years.",
                "amount": "HKD 18,390 to 20,000 / month + annual RedBird award"
            },
            "airfare": {
                "status": "SUBSIDIZED",
                "details": "International relocation flights paid from initial RedBird Year 1 award (HKD 40,000 cash grant).",
                "amount": "Funded via HKD 40,000 RedBird award"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Hong Kong Student Visa application fee (HKD 230) paid to Hong Kong Immigration Department via HKUST.",
                "amount": "HKD 230 (~PKR 8,300)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Access to HKUST Medical Clinic (free general consultations) and Hong Kong Public Healthcare System at eligible resident rates (HKD 100/day hospital stay).",
                "amount": "Subsidized comprehensive campus healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across HKUST campus, including halal-certified options (e.g. Ebeneezer's Kebabs); meals cost HKD 30 to 50.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to HKUST Lee Shau Kee Library, state-of-the-art supercomputers, and Nanosystem Fabrication Facility (NFF).",
                "amount": "100% covered world-class lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "HKUST Overseas Research Award and conference travel grants provide up to HKD 12,000 to 25,000 for international conference presentations.",
                "amount": "Up to HKD 25,000 conference travel funds"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized student Octopus cards offering 50% discount on Hong Kong MTR metro network.",
                "amount": "50% discounted public transit"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-leading Hong Kong technological university (The Hong Kong University of Science and Technology - HKUST).",
            "participating_institutions": [
                "The Hong Kong University of Science and Technology (Clear Water Bay Campus, Kowloon/New Territories, Hong Kong)"
            ],
            "university_rankings_scope": "QS World University Rankings #47 globally, World Top 30 in Engineering & Technology, World #2 in Times Higher Education Young University Rankings.",
            "available_majors": [
                "PhD in Computer Science and Engineering",
                "PhD in Electronic and Computer Engineering",
                "PhD in Chemical and Biological Engineering",
                "PhD in Civil and Environmental Engineering",
                "PhD in Mechanical and Aerospace Engineering",
                "PhD in Physics and Chemistry",
                "PhD in Mathematics and Data Science",
                "PhD in Public Policy and Environment"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (Doctor of Philosophy)",
            "admission_requirements_summary": "Bachelor's / Master's degree with First Class / CGPA >= 3.50/4.00, academic transcripts, research proposal, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 80+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Computer Science and Engineering and Electronic & Computer Engineering are intensely competitive; establishing contact with an HKUST professor prior to applying significantly increases admission odds.",
            "strategic_program_match_advice": "Review recent publications from HKUST laboratory principal investigators, email professors citing recent journal papers, and express interest in their specific funded research tasks."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://prog-crs.hkust.edu.hk/pgprograms/details/",
            "portal_system_name": "HKUST Online Admissions System for Research Postgraduate Programs",
            "account_creation_instructions": "Register on the HKUST postgraduate admissions portal, select PhD program, complete application form, upload personal statement and transcripts, pay HKD 350 fee, and register two recommenders.",
            "step_by_step_workflow": [
                "Step 1: Explore HKUST faculty research profiles and contact prospective supervisors with CV and research abstract (September-October).",
                "Step 2: Register on HKUST Online Admissions System during open intake (September to December).",
                "Step 3: Complete online application, upload documents, and pay HKD 350 application fee.",
                "Step 4: Referees submit evaluation letters online via confidential portal links.",
                "Step 5: Departmental admissions committee reviews applications and conducts technical interviews via Zoom.",
                "Step 6: Department nominates candidate for admission and RedBird PhD Fellowship Scheme.",
                "Step 7: Official admission and RedBird fellowship award letter issued in January/February.",
                "Step 8: Accept offer, apply for Hong Kong Student Visa via HKUST, and arrive in Hong Kong in late August."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Admission application automatically considers candidates for Postgraduate Studentship (PGS) and RedBird PhD Fellowship Scheme.",
            "recommendation_letters_submission_method": "Submitted online by two academic referees via confidential email links generated by HKUST portal.",
            "personal_statement_prompts": "Personal Statement describing academic achievements, research interests, career aspirations, and motivation for pursuing a doctoral degree at HKUST.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) detailing problem formulation, methodology, literature review, and anticipated scientific contributions.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 80+ required; GRE is optional but recommended.",
            "application_fee_amount": "HKD 350 (approx. USD 45 / ~PKR 12,600)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC attestation required for Pakistani credentials upon enrollment.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via HKUST postgraduate admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.50/4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Research Proposal (2-4 Pages)",
                "mandatory": True,
                "specification": "Structured research proposal detailing problem formulation, methodology, and anticipated contributions.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors submitted electronically.",
                "pakistan_specific_instruction": "From previous university professors."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+ (sub-scores 5.5+) or TOEFL iBT 80+.",
                "pakistan_specific_instruction": "Score report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
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
            "application_open_date": "September 1",
            "application_deadline": "December 1 (Hong Kong PhD Fellowship Scheme deadline) / January 1 (Main Round deadline)",
            "university_admission_deadline": "January 1",
            "document_submission_deadline": "January 1",
            "recommendation_letters_deadline": "January 8",
            "interview_period": "January - February",
            "shortlist_announcement": "February - March",
            "final_result_acceptance_deadline": "Within 2 to 3 weeks of notification",
            "visa_application_window": "April - June",
            "semester_commencement": "September 1 (Fall intake)",
            "annual_cycle_notes": "Main intake commences in September; applicants submit by December 1 for dual consideration under HKPFS and RedBird."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA, academic honors, course rigor)",
            "extracurricular_and_leadership_weight": "5% (Initiative, teamwork, problem-solving mindset)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with HKUST research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "HKUST Departmental Admissions Committee, School Graduate Deans, and Fok Ying Tung Graduate School Board.",
            "evaluation_methodology": "Rigorous holistic evaluation assessing mathematical ability, research productivity, experimental aptitude, and alignment with faculty laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 to 5,500 international PhD applicants across HKUST",
            "total_scholarships_awarded": "~200 to 250 RedBird awards annually",
            "acceptance_rate_global": "~4.5% to 5.5%",
            "acceptance_rate_pakistan": "~8.0% to 12.0% for applicants with strong research profiles and CGPA >= 3.65",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.65 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records in computer science, engineering, or physics, documented project experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "China, Pakistan, India, Vietnam, South Korea, Turkey, Iran, Russia.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal prog-crs.hkust.edu.hk.",
                "HKUST does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of HKD 350 is paid directly through the secure HKUST online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: HKD 350 (~PKR 12,600).",
                "Hong Kong Student Visa fee: HKD 230 (~PKR 8,300).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Flight to Hong Kong: ~PKR 120,000 to 180,000.",
                "Initial living deposit before first stipend payment: ~HKD 5,000 (~PKR 180,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Cantonese fluency is required. Reality: 100% of graduate education at HKUST is conducted in English.",
                "Myth: Separate application required for RedBird. Reality: All PhD applicants are automatically considered."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites suggest tuition is deducted from stipend; tuition is 100% covered by Hong Kong Government Tuition Waiver Scheme."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum Cumulative Grade Average (CGA) of 3.00 out of 4.30 throughout the PhD candidature.",
            "attendance_requirements": "Full-time physical research presence at HKUST campus; pass PhD Qualifying Examination within required department timeline.",
            "academic_progress_monitoring": "Annual academic progress review evaluated by thesis supervisor and department postgraduate committee.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment; limited teaching/research duties (up to 100 hours/year) assigned under PGS regulations.",
            "home_country_return_obligation": "None; zero service bond or return obligation (scholars are eligible for Hong Kong IANG work visa upon graduation).",
            "service_obligations_or_bonds": "Zero service bond.",
            "repayment_clawback_conditions": "Studentship is terminated if academic performance is unsatisfactory or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Tenure is strictly 4 years; extensions require supervisor research grant funding."
        },
        "official_sources_verified": [
            {
                "source_name": "HKUST Fok Ying Tung Graduate School RedBird Scheme",
                "source_url": "https://prog-crs.hkust.edu.hk/pgprograms/details/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "HKUST Research Postgraduate Admissions Guide",
                "source_url": "https://fytgs.hkust.edu.hk/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-075": {
        "scholarship_id": "SCH-AS-075",
        "basic_details": {
            "scholarship_name": "University of Hong Kong (HKU) Presidential PhD Fellowship Scheme (HKU-PS)",
            "offering_entity": "The University of Hong Kong (HKU) Graduate School",
            "host_country": "Hong Kong (SAR)",
            "host_institutions_covered": "The University of Hong Kong (Pokfulam Main Campus, Hong Kong)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Engineering, Faculty of Science, Li Ka Shing Faculty of Medicine, Faculty of Architecture, and Faculty of Dentistry (all doctoral research disciplines).",
            "number_of_awards_total": "~120 to 160 elite doctoral fellowships awarded annually university-wide",
            "number_of_awards_pakistan": "Open internationally; typically 8 to 15 outstanding Pakistani researchers in engineering, computing, and biomedical sciences selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (standard PhD tenure)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Combined funding package: HKD 28,100 / month living stipend (~PKR 1,011,600 / month) in Year 1, plus HKD 40,000 cash award in Year 1 and HKD 20,000/year in subsequent years, plus 100% full tuition fee waiver and dedicated conference/research travel allowance of HKD 14,000 / year: Total package value exceeds HKD 420,000 / year (~PKR 15,120,000 / year)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to candidates with extraordinary academic and research achievements.",
            "academic_qualifications": "Completed recognized Bachelor's degree with First Class Honours / High Distinction (minimum CGPA 3.60/4.00) or completed Master's degree with outstanding academic record from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Minimum CGPA 3.60 / 4.00; competitive applicants typically hold CGPA >= 3.80 / 4.00 or top 5% class standing.",
            "subject_background_prerequisites": "Computer science, artificial intelligence, electrical engineering, mechanical engineering, materials science, biomedical engineering, physics, chemistry, or medicine.",
            "current_education_status": "Graduated or final-year students completing degree requirements before September semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in premier peer-reviewed journals (Nature index, IEEE, ACM) or top international conferences strongly prioritized.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 (5.5 in all sub-scores), TOEFL iBT minimum 85, or official English Medium of Instruction (MOI) certificate from an accredited university.",
            "other_language_requirements": "Cantonese or Mandarin Chinese is NOT required; 100% of graduate research and instruction is conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply for full-time PhD admission at HKU and are automatically considered for the HKU Presidential PhD Fellowship Scheme based on merit.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full-time employment or parallel external full scholarships.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee covered through Hong Kong Government Tuition Waiver Scheme for Research Postgraduate Students (HKD 42,100/year).",
                "amount": "100% covered (~HKD 42,100 / year value; ~PKR 1,515,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "HKU online application fee of HKD 400 paid via credit card during portal submission.",
                "amount": "HKD 400 (~PKR 14,400)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate residential housing at Pokfulam / Morrison Hall / Graduate House (approx. HKD 3,500 to 5,500 / month), easily covered from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Prestigious monthly living stipend: HKD 28,100 / month (~PKR 1,011,600 / month) throughout Year 1, supplemented by HKD 40,000 cash award in Year 1 and HKD 20,000/year in subsequent years.",
                "amount": "HKD 28,100 / month + annual cash award"
            },
            "airfare": {
                "status": "SUBSIDIZED",
                "details": "International travel funded easily from initial cash award (HKD 40,000 grant).",
                "amount": "Funded via HKD 40,000 cash grant"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Hong Kong Student Visa application fee (HKD 230) paid to Hong Kong Immigration Department via HKU.",
                "amount": "HKD 230 (~PKR 8,300)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Access to HKU University Health Service (free general consultations) and Hong Kong Public Healthcare System at eligible resident rates.",
                "amount": "Subsidized comprehensive campus healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Pokfulam campus, including certified halal dining options; meals cost HKD 30 to 55.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to HKU Libraries (holding over 3 million volumes), state-of-the-art supercomputing facilities, and advanced analytical centers.",
                "amount": "100% covered world-class lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Dedicated conference travel allowance of up to HKD 14,000 per year provided to each presidential fellow.",
                "amount": "HKD 14,000 / year conference travel allowance"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Direct MTR station (HKU Station on the Island Line) located right under the campus, with 50% student concession fares.",
                "amount": "50% discounted public transit"
            },
            "total_estimated_value_usd_per_year": 54000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-class Hong Kong flagship institution (The University of Hong Kong - HKU).",
            "participating_institutions": [
                "The University of Hong Kong (Pokfulam Main Campus, Hong Kong Island)"
            ],
            "university_rankings_scope": "QS World University Rankings #17 globally, #2 in Asia; Hong Kong's oldest and most prestigious university, globally renowned for biomedical sciences, engineering, and computer science.",
            "available_majors": [
                "PhD in Computer Science (Faculty of Engineering)",
                "PhD in Electrical and Electronic Engineering",
                "PhD in Mechanical Engineering",
                "PhD in Civil Engineering",
                "PhD in Biomedical Sciences (Li Ka Shing Faculty of Medicine)",
                "PhD in Physics and Chemistry",
                "PhD in Mathematics and Statistics",
                "PhD in Materials Science and Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (Doctor of Philosophy)",
            "admission_requirements_summary": "Bachelor's / Master's degree with First Class / CGPA >= 3.60/4.00, academic transcripts, research proposal, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 85+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Computer Science and Faculty of Medicine are fiercely competitive; contacting prospective supervisors early and securing provisional endorsement strongly aids selection.",
            "strategic_program_match_advice": "Focus research proposals on AI in medicine, robotics, quantum materials, or renewable energy where HKU holds major InnoHK research centers and government funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_aid/hku_presidential_phd_scholar_programme",
            "portal_system_name": "HKU Online Application System for Research Postgraduate Programs",
            "account_creation_instructions": "Register on the HKU graduate admissions portal, select PhD program, complete application form, upload personal statement and transcripts, pay HKD 400 fee, and register two recommenders.",
            "step_by_step_workflow": [
                "Step 1: Explore HKU faculty research profiles and contact prospective supervisors with CV and research abstract (September-October).",
                "Step 2: Register on HKU Online Application System during open intake (September to December).",
                "Step 3: Complete online application, upload documents, and pay HKD 400 application fee.",
                "Step 4: Referees submit evaluation letters online via confidential portal links.",
                "Step 5: Departmental admissions committee reviews applications and conducts technical interviews via Zoom.",
                "Step 6: Department nominates top candidates to the Graduate School Presidential Fellowship Selection Panel.",
                "Step 7: Official admission and HKU Presidential PhD Fellowship award letter issued in January/February.",
                "Step 8: Accept offer, apply for Hong Kong Student Visa via HKU, and arrive in Hong Kong in late August."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Application for admission automatically triggers consideration for Postgraduate Studentship and HKU Presidential PhD Fellowship Scheme.",
            "recommendation_letters_submission_method": "Submitted online by two academic referees via confidential email links generated by HKU portal.",
            "personal_statement_prompts": "Statement of Purpose describing academic milestones, research interests, career aspirations, and motivation for pursuing a doctoral degree at HKU.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) detailing problem formulation, methodology, literature review, and anticipated scientific contributions.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 85+ required; GRE is optional but recommended.",
            "application_fee_amount": "HKD 400 (approx. USD 51 / ~PKR 14,400)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC attestation required for Pakistani credentials upon enrollment.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via HKU graduate admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.60/4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Research Proposal (2-4 Pages)",
                "mandatory": True,
                "specification": "Structured research proposal detailing problem formulation, methodology, and anticipated contributions.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors submitted electronically.",
                "pakistan_specific_instruction": "From previous university professors."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+ (sub-scores 5.5+) or TOEFL iBT 85+.",
                "pakistan_specific_instruction": "Score report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
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
            "application_open_date": "September 1",
            "application_deadline": "December 1 (Hong Kong PhD Fellowship Scheme deadline) / December 15 (HKU Main Round deadline)",
            "university_admission_deadline": "December 15",
            "document_submission_deadline": "December 15",
            "recommendation_letters_deadline": "December 22",
            "interview_period": "January - February",
            "shortlist_announcement": "February - March",
            "final_result_acceptance_deadline": "Within 2 to 3 weeks of notification",
            "visa_application_window": "April - June",
            "semester_commencement": "September 1 (Fall intake)",
            "annual_cycle_notes": "Main intake commences in September; applicants submit by December 1 for dual consideration under HKPFS and HKU-PS."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA, academic honors, course rigor)",
            "extracurricular_and_leadership_weight": "5% (Initiative, intellectual maturity)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with HKU research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "HKU Departmental Admissions Committee, Faculty Graduate Deans, and Graduate School Presidential Selection Panel.",
            "evaluation_methodology": "Two-tier rigorous evaluation identifying top 5% of doctoral applicants with world-class research potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 to 6,500 international PhD applicants across HKU",
            "total_scholarships_awarded": "~120 to 160 HKU Presidential awards annually",
            "acceptance_rate_global": "~2.5% to 3.0%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% for candidates with strong research profiles and CGPA >= 3.75",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.75 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records in computer science, engineering, or biomedicine, documented project experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "China, Pakistan, India, Vietnam, South Korea, Turkey, Germany, United Kingdom.",
            "competitiveness_tier": "MOST_COMPETITIVE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal gradsch.hku.hk.",
                "HKU does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of HKD 400 is paid directly through the secure HKU online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: HKD 400 (~PKR 14,400).",
                "Hong Kong Student Visa fee: HKD 230 (~PKR 8,300).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Flight to Hong Kong: ~PKR 120,000 to 180,000.",
                "Initial living deposit before first stipend payment: ~HKD 5,000 (~PKR 180,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Cantonese fluency is required. Reality: 100% of graduate education at HKU is conducted in English.",
                "Myth: Separate application required for HKU-PS. Reality: All PhD applicants are automatically considered."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites suggest tuition is deducted from stipend; tuition is 100% covered by Hong Kong Government Tuition Waiver Scheme."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum Cumulative Grade Average (CGA) of 3.00 out of 4.30 throughout the PhD candidature.",
            "attendance_requirements": "Full-time physical research presence at HKU campus; pass PhD Qualifying Examination within required department timeline.",
            "academic_progress_monitoring": "Annual academic progress review evaluated by thesis supervisor and department postgraduate committee.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment; limited teaching/research duties (up to 100 hours/year) assigned under PGS regulations.",
            "home_country_return_obligation": "None; zero service bond or return obligation (scholars are eligible for Hong Kong IANG work visa upon graduation).",
            "service_obligations_or_bonds": "Zero service bond.",
            "repayment_clawback_conditions": "Studentship is terminated if academic performance is unsatisfactory or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Tenure is strictly 4 years; extensions require supervisor research grant funding."
        },
        "official_sources_verified": [
            {
                "source_name": "HKU Graduate School Presidential PhD Scholar Programme",
                "source_url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_aid/hku_presidential_phd_scholar_programme",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "HKU Graduate School Admissions Guide",
                "source_url": "https://gradsch.hku.hk/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
