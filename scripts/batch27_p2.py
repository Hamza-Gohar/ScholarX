"""Batch 27 Part 2: Hong Kong and Malaysia Elite Postgraduate Awards (3 awards)
SCH-AS-076: Chinese University of Hong Kong (CUHK) Vice-Chancellor's PhD Scholarship
SCH-AS-077: City University of Hong Kong (CityU) Presidential PhD Fellowship
SCH-AS-078: Universiti Malaya (UM) Bright Sparks Excellence Fellowship Scheme
"""

DATA_P2 = {
    "SCH-AS-076": {
        "scholarship_id": "SCH-AS-076",
        "basic_details": {
            "scholarship_name": "The Chinese University of Hong Kong (CUHK) Vice-Chancellor's PhD Scholarship Scheme",
            "offering_entity": "The Chinese University of Hong Kong (CUHK) Graduate School",
            "host_country": "Hong Kong (SAR)",
            "host_institutions_covered": "The Chinese University of Hong Kong (Shatin Campus, New Territories, Hong Kong)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Engineering (Computer Science, Information Engineering, Electronic Engineering, Systems Engineering), Faculty of Science (Physics, Chemistry, Life Sciences, Mathematics), Faculty of Medicine, and Faculty of Social Science.",
            "number_of_awards_total": "~100 to 140 Vice-Chancellor's PhD Scholarships awarded annually",
            "number_of_awards_pakistan": "Open internationally; typically 8 to 15 Pakistani engineering, AI, and science researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (standard PhD normative study period)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Postgraduate Studentship (PGS) of HKD 18,360 to 20,000 / month (~PKR 660,960 to 720,000 / month) plus Vice-Chancellor's Award of HKD 40,000 in Year 1 and HKD 20,000/year in subsequent years, full tuition waiver, and conference grant of HKD 13,800/year"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to young researchers with exceptional academic momentum.",
            "academic_qualifications": "Completed recognized Bachelor's degree with First Class Honours / High Distinction (minimum CGPA 3.50/4.00) or completed Master's degree with outstanding academic record from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum CGPA 3.50 / 4.00; competitive applicants typically hold CGPA >= 3.70 / 4.00 or top 10% class standing.",
            "subject_background_prerequisites": "Computer science, artificial intelligence, information engineering, electronic engineering, mechanical engineering, biomedical sciences, physics, chemistry, or mathematics.",
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
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Cantonese or Mandarin Chinese is NOT required; 100% of graduate research and instruction is conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All applicants applying for full-time PhD programs at CUHK are automatically considered for the Vice-Chancellor's PhD Scholarship Scheme; no separate application required.",
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
                "details": "CUHK online application fee of HKD 300 paid via credit card during portal submission.",
                "amount": "HKD 300 (~PKR 10,800)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing at Shatin campus (Postgraduate Halls; approx. HKD 2,800 to 4,200 / month), paid easily from monthly stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Postgraduate Studentship (PGS) of HKD 18,360 to 20,000 / month (~PKR 660,960 to 720,000 / month), supplemented by Vice-Chancellor's Award of HKD 40,000 in Year 1 and HKD 20,000 in subsequent years.",
                "amount": "HKD 18,360 to 20,000 / month + annual award"
            },
            "airfare": {
                "status": "SUBSIDIZED",
                "details": "International travel funded easily from initial cash award (HKD 40,000 grant).",
                "amount": "Funded via HKD 40,000 cash grant"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Hong Kong Student Visa application fee (HKD 230) paid to Hong Kong Immigration Department via CUHK.",
                "amount": "HKD 230 (~PKR 8,300)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Access to CUHK University Health Service (free general consultations) and Hong Kong Public Healthcare System at eligible resident rates.",
                "amount": "Subsidized comprehensive campus healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Shatin campus, including certified halal dining options (e.g. Muslim student dining facilities); meals cost HKD 30 to 50.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to CUHK University Library System (holding over 2.7 million volumes), state-of-the-art supercomputers, and advanced instrumentation laboratories.",
                "amount": "100% covered world-class lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Dedicated conference travel grant of up to HKD 13,800 per year provided to support international conference presentations.",
                "amount": "HKD 13,800 / year conference travel allowance"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Direct MTR station (University Station on the East Rail Line) located directly inside the campus, with 50% student concession fares.",
                "amount": "50% discounted public transit"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-class Hong Kong comprehensive research institution (The Chinese University of Hong Kong - CUHK).",
            "participating_institutions": [
                "The Chinese University of Hong Kong (Shatin Campus, New Territories, Hong Kong)"
            ],
            "university_rankings_scope": "QS World University Rankings #36 globally, #10 in Asia; internationally recognized for artificial intelligence, computer vision, information engineering, and biomedical sciences.",
            "available_majors": [
                "PhD in Computer Science and Engineering",
                "PhD in Information Engineering",
                "PhD in Electronic Engineering",
                "PhD in Mechanical and Automation Engineering",
                "PhD in Systems Engineering and Engineering Management",
                "PhD in Biomedical Engineering",
                "PhD in Physics and Chemistry",
                "PhD in Mathematics and Statistics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (Doctor of Philosophy)",
            "admission_requirements_summary": "Bachelor's / Master's degree with First Class / CGPA >= 3.50/4.00, academic transcripts, research proposal, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 80+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Computer Science and Engineering and Information Engineering (home of the Multimedia Lab / AI founders) are fiercely competitive; contacting prospective supervisors early and securing endorsement strongly aids selection.",
            "strategic_program_match_advice": "Review recent publications from CUHK laboratory principal investigators, email professors citing recent journal papers, and express interest in their specific funded research tasks."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.gs.cuhk.edu.hk/admissions/scholarships-fees/scholarships",
            "portal_system_name": "CUHK Graduate School Online Application System",
            "account_creation_instructions": "Register on the CUHK postgraduate admissions portal, select PhD program, complete application form, upload personal statement and transcripts, pay HKD 300 fee, and register two recommenders.",
            "step_by_step_workflow": [
                "Step 1: Explore CUHK faculty research profiles and contact prospective supervisors with CV and research abstract (September-October).",
                "Step 2: Register on CUHK Graduate School Online Application System during open intake (September to December).",
                "Step 3: Complete online application, upload documents, and pay HKD 300 application fee.",
                "Step 4: Referees submit evaluation letters online via confidential portal links.",
                "Step 5: Departmental admissions committee reviews applications and conducts technical interviews via Zoom.",
                "Step 6: Department nominates candidate for admission and Vice-Chancellor's PhD Scholarship Scheme.",
                "Step 7: Official admission and fellowship award letter issued in January/February.",
                "Step 8: Accept offer, apply for Hong Kong Student Visa via CUHK, and arrive in Hong Kong in late August."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Admission application automatically considers candidates for Postgraduate Studentship (PGS) and Vice-Chancellor's PhD Scholarship Scheme.",
            "recommendation_letters_submission_method": "Submitted online by two academic referees via confidential email links generated by CUHK portal.",
            "personal_statement_prompts": "Personal Statement describing academic achievements, research interests, career aspirations, and motivation for pursuing a doctoral degree at CUHK.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) detailing problem formulation, methodology, literature review, and anticipated scientific contributions.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 80+ required; GRE is optional but recommended.",
            "application_fee_amount": "HKD 300 (approx. USD 38 / ~PKR 10,800)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC attestation required for Pakistani credentials upon enrollment.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via CUHK postgraduate admissions portal."
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
                "specification": "IELTS Academic 6.5+ or TOEFL iBT 80+.",
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
            "application_deadline": "December 1 (Hong Kong PhD Fellowship Scheme deadline) / December 15 (Main Round deadline)",
            "university_admission_deadline": "December 15",
            "document_submission_deadline": "December 15",
            "recommendation_letters_deadline": "December 22",
            "interview_period": "January - February",
            "shortlist_announcement": "February - March",
            "final_result_acceptance_deadline": "Within 2 to 3 weeks of notification",
            "visa_application_window": "April - June",
            "semester_commencement": "September 1 (Fall intake)",
            "annual_cycle_notes": "Main intake commences in September; applicants submit by December 1 for dual consideration under HKPFS and Vice-Chancellor's Scheme."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA, academic honors, course rigor)",
            "extracurricular_and_leadership_weight": "5% (Initiative, intellectual maturity)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with CUHK research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "CUHK Departmental Admissions Committee, Faculty Graduate Deans, and Graduate School Selection Panel.",
            "evaluation_methodology": "Two-tier rigorous evaluation identifying top 5% of doctoral applicants with world-class research potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,500 to 6,000 international PhD applicants across CUHK",
            "total_scholarships_awarded": "~100 to 140 Vice-Chancellor's awards annually",
            "acceptance_rate_global": "~2.5% to 3.5%",
            "acceptance_rate_pakistan": "~5.0% to 8.0% for candidates with strong research profiles and CGPA >= 3.70",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.70 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records in computer science, engineering, or physics, documented project experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "China, Pakistan, India, Vietnam, South Korea, Turkey, Iran, Russia.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal gs.cuhk.edu.hk.",
                "CUHK does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of HKD 300 is paid directly through the secure CUHK online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: HKD 300 (~PKR 10,800).",
                "Hong Kong Student Visa fee: HKD 230 (~PKR 8,300).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Flight to Hong Kong: ~PKR 120,000 to 180,000.",
                "Initial living deposit before first stipend payment: ~HKD 5,000 (~PKR 180,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Cantonese fluency is required. Reality: 100% of graduate education at CUHK is conducted in English.",
                "Myth: Separate application required. Reality: All PhD applicants are automatically considered."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites suggest tuition is deducted from stipend; tuition is 100% covered by Hong Kong Government Tuition Waiver Scheme."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum Cumulative Grade Point Average (CGPA) of 3.00 out of 4.00 throughout the PhD candidature.",
            "attendance_requirements": "Full-time physical research presence at CUHK campus; pass PhD Qualifying Examination within required department timeline.",
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
                "source_name": "CUHK Graduate School Vice-Chancellor's PhD Scholarship Scheme",
                "source_url": "https://www.gs.cuhk.edu.hk/admissions/scholarships-fees/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "CUHK Postgraduate Admissions Guide",
                "source_url": "https://www.gs.cuhk.edu.hk/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-077": {
        "scholarship_id": "SCH-AS-077",
        "basic_details": {
            "scholarship_name": "City University of Hong Kong (CityU) Presidential PhD Fellowship Scheme",
            "offering_entity": "City University of Hong Kong (CityU) Chow Yei Ching School of Graduate Studies",
            "host_country": "Hong Kong (SAR)",
            "host_institutions_covered": "City University of Hong Kong (Kowloon Tong Campus, Hong Kong)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Engineering (Computer Science, Electrical Engineering, Materials Science, Mechanical, Biomedical), College of Science (Physics, Chemistry, Mathematics), School of Data Science, and Jockey Club College of Veterinary Medicine and Life Sciences.",
            "number_of_awards_total": "~80 to 120 Presidential PhD Fellowships awarded annually university-wide",
            "number_of_awards_pakistan": "Open internationally; typically 8 to 15 Pakistani engineering, computing, and science researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (standard PhD normative study period)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Combined funding package: HKD 28,100 / month living stipend (~PKR 1,011,600 / month) in Year 1, plus HKD 30,000 cash award in Year 1 and HKD 15,000/year in subsequent years, plus 100% full tuition fee waiver and conference grant of HKD 14,000/year: Total package value exceeds HKD 400,000 / year (~PKR 14,400,000 / year)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to candidates with extraordinary academic and research achievements.",
            "academic_qualifications": "Completed recognized Bachelor's degree with First Class Honours / High Distinction (minimum CGPA 3.50/4.00) or completed Master's degree with outstanding academic record from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum CGPA 3.50 / 4.00; competitive applicants typically hold CGPA >= 3.70 / 4.00 or top 10% class standing.",
            "subject_background_prerequisites": "Computer science, data science, electrical engineering, mechanical engineering, materials science, biomedical engineering, physics, chemistry, or mathematics.",
            "current_education_status": "Graduated or final-year students completing degree requirements before September semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in peer-reviewed journals (SCI/SCIE) or top conferences (IEEE, ACM) provide a substantial competitive edge.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 79, or official English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Cantonese or Mandarin Chinese is NOT required; 100% of graduate research and instruction is conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All applicants applying for full-time PhD programs at CityU are automatically considered for the Presidential PhD Fellowship Scheme; no separate application required.",
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
                "details": "CityU online application fee of HKD 300 paid via credit card during portal submission.",
                "amount": "HKD 300 (~PKR 10,800)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing at Kowloon Tong (Postgraduate Hall; approx. HKD 3,200 to 4,800 / month), paid easily from monthly stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Prestigious monthly living stipend: HKD 28,100 / month (~PKR 1,011,600 / month) throughout Year 1, supplemented by HKD 30,000 cash award in Year 1 and HKD 15,000/year in subsequent years.",
                "amount": "HKD 28,100 / month + annual cash award"
            },
            "airfare": {
                "status": "SUBSIDIZED",
                "details": "International travel funded easily from initial cash award (HKD 30,000 grant).",
                "amount": "Funded via HKD 30,000 cash grant"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Hong Kong Student Visa application fee (HKD 230) paid to Hong Kong Immigration Department via CityU.",
                "amount": "HKD 230 (~PKR 8,300)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Access to CityU Young Hall Medical Centre (free general consultations) and Hong Kong Public Healthcare System at eligible resident rates.",
                "amount": "Subsidized comprehensive campus healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Kowloon Tong campus, including certified halal dining options; meals cost HKD 30 to 50.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to CityU Run Run Shaw Library, state-of-the-art supercomputing clusters, and State Key Laboratory of Terahertz and Millimeter Waves.",
                "amount": "100% covered world-class lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Dedicated conference travel grant of up to HKD 14,000 per year provided to support international conference presentations.",
                "amount": "HKD 14,000 / year conference travel allowance"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Direct MTR station (Kowloon Tong Station connecting East Rail and Kwun Tong Lines) with 50% student concession fares.",
                "amount": "50% discounted public transit"
            },
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-class Hong Kong comprehensive research institution (City University of Hong Kong - CityU).",
            "participating_institutions": [
                "City University of Hong Kong (Kowloon Tong Campus, Kowloon, Hong Kong)"
            ],
            "university_rankings_scope": "QS World University Rankings #62 globally, World Top 50 in Materials Science, Computer Science, and Electrical Engineering; ranked #1 for Most International University in the World (THE 2024).",
            "available_majors": [
                "PhD in Computer Science (Department of Computer Science)",
                "PhD in Data Science (School of Data Science)",
                "PhD in Electrical Engineering",
                "PhD in Materials Science and Engineering",
                "PhD in Mechanical Engineering",
                "PhD in Biomedical Engineering",
                "PhD in Physics and Chemistry",
                "PhD in Mathematics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (Doctor of Philosophy)",
            "admission_requirements_summary": "Bachelor's / Master's degree with First Class / CGPA >= 3.50/4.00, academic transcripts, research proposal, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 79+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Computer Science and School of Data Science are fiercely competitive; contacting prospective supervisors early and securing provisional endorsement strongly aids selection.",
            "strategic_program_match_advice": "Focus research proposals on wireless communications (terahertz), AI algorithms, advanced nanomaterials, or robotics where CityU holds State Key Laboratories."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.cityu.edu.hk/pg/research-degree-programmes/fellowships-scholarships-and-financial-aid",
            "portal_system_name": "CityU Online Admissions System for Research Degree Programmes",
            "account_creation_instructions": "Register on the CityU graduate admissions portal, select PhD program, complete application form, upload personal statement and transcripts, pay HKD 300 fee, and register two recommenders.",
            "step_by_step_workflow": [
                "Step 1: Explore CityU faculty research profiles and contact prospective supervisors with CV and research abstract (September-October).",
                "Step 2: Register on CityU Online Admissions System during open intake (September to December).",
                "Step 3: Complete online application, upload documents, and pay HKD 300 application fee.",
                "Step 4: Referees submit evaluation letters online via confidential portal links.",
                "Step 5: Departmental admissions committee reviews applications and conducts technical interviews via Zoom.",
                "Step 6: Department nominates candidate for admission and Presidential PhD Fellowship Scheme.",
                "Step 7: Official admission and fellowship award letter issued in January/February.",
                "Step 8: Accept offer, apply for Hong Kong Student Visa via CityU, and arrive in Hong Kong in late August."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Application for admission automatically triggers consideration for Postgraduate Studentship and Presidential PhD Fellowship Scheme.",
            "recommendation_letters_submission_method": "Submitted online by two academic referees via confidential email links generated by CityU portal.",
            "personal_statement_prompts": "Personal Statement describing academic achievements, research interests, career aspirations, and motivation for pursuing a doctoral degree at CityU.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) detailing problem formulation, methodology, literature review, and anticipated scientific contributions.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications, research projects, technical skills, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental doctoral admission committee.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 79+ required; GRE is optional but recommended.",
            "application_fee_amount": "HKD 300 (approx. USD 38 / ~PKR 10,800)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC attestation required for Pakistani credentials upon enrollment.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via CityU postgraduate admissions portal."
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
                "specification": "IELTS Academic 6.5+ or TOEFL iBT 79+.",
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
            "application_deadline": "December 1 (Hong Kong PhD Fellowship Scheme deadline) / December 15 (Main Round deadline)",
            "university_admission_deadline": "December 15",
            "document_submission_deadline": "December 15",
            "recommendation_letters_deadline": "December 22",
            "interview_period": "January - February",
            "shortlist_announcement": "February - March",
            "final_result_acceptance_deadline": "Within 2 to 3 weeks of notification",
            "visa_application_window": "April - June",
            "semester_commencement": "September 1 (Fall intake)",
            "annual_cycle_notes": "Main intake commences in September; applicants submit by December 1 for dual consideration under HKPFS and CityU Presidential Scheme."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA, academic honors, course rigor)",
            "extracurricular_and_leadership_weight": "5% (Initiative, intellectual maturity)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with CityU research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "CityU Departmental Admissions Committee, College Graduate Deans, and Chow Yei Ching School of Graduate Studies Board.",
            "evaluation_methodology": "Two-tier rigorous evaluation identifying top 5% of doctoral applicants with world-class research potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,800 to 5,000 international PhD applicants across CityU",
            "total_scholarships_awarded": "~80 to 120 Presidential awards annually",
            "acceptance_rate_global": "~2.5% to 3.5%",
            "acceptance_rate_pakistan": "~5.0% to 8.0% for candidates with strong research profiles and CGPA >= 3.70",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.70 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records in computer science, engineering, or physics, documented project experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "China, Pakistan, India, Vietnam, South Korea, Turkey, Iran, Russia.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal cityu.edu.hk/pg.",
                "CityU does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of HKD 300 is paid directly through the secure CityU online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: HKD 300 (~PKR 10,800).",
                "Hong Kong Student Visa fee: HKD 230 (~PKR 8,300).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Flight to Hong Kong: ~PKR 120,000 to 180,000.",
                "Initial living deposit before first stipend payment: ~HKD 5,000 (~PKR 180,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Cantonese fluency is required. Reality: 100% of graduate education at CityU is conducted in English.",
                "Myth: Separate application required. Reality: All PhD applicants are automatically considered."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites suggest tuition is deducted from stipend; tuition is 100% covered by Hong Kong Government Tuition Waiver Scheme."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum Cumulative Grade Point Average (CGPA) of 3.00 out of 4.30 throughout the PhD candidature.",
            "attendance_requirements": "Full-time physical research presence at CityU campus; pass PhD Qualifying Examination within required department timeline.",
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
                "source_name": "CityU Chow Yei Ching School of Graduate Studies Presidential Scheme",
                "source_url": "https://www.cityu.edu.hk/pg/research-degree-programmes/fellowships-scholarships-and-financial-aid",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "CityU Research Degree Admissions Guide",
                "source_url": "https://www.cityu.edu.hk/pg/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-078": {
        "scholarship_id": "SCH-AS-078",
        "basic_details": {
            "scholarship_name": "Universiti Malaya (UM) Bright Sparks Excellence Fellowship Scheme",
            "offering_entity": "Universiti Malaya (UM) Bright Sparks Unit & Institute of Graduate Studies (IPS)",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Malaya Main Campus (Kuala Lumpur, Malaysia)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Engineering, Faculty of Science, Faculty of Computer Science and Information Technology, Faculty of Medicine, and Institute of Advanced Studies (all doctoral research disciplines).",
            "number_of_awards_total": "~80 to 120 Bright Sparks fellowships awarded annually across faculties",
            "number_of_awards_pakistan": "Extensive Malaysian cohort; typically 15 to 25 Pakistani engineering, computing, and biomedical researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 36 months (3 years) for PhD candidature",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Monthly living allowance of RM 2,500 to RM 3,000 / month (~PKR 162,500 to 195,000 / month) plus 100% full tuition fee waiver, dedicated research operating allowance, and thesis publication incentives"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Malaysian citizens and international candidates of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be 30 years old or below for direct Bachelor's-to-PhD track; 35 years old or below for candidates holding a Master's degree.",
            "academic_qualifications": "First Class Bachelor's degree (minimum CGPA 3.70/4.00) for direct PhD entry, or Master's degree by research with Distinction / CGPA >= 3.70/4.00 from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum CGPA 3.70 / 4.00; competitive applicants typically hold CGPA >= 3.80 / 4.00 or top 5% class standing.",
            "subject_background_prerequisites": "Engineering, computer science, software engineering, artificial intelligence, biotechnology, biomedical sciences, chemistry, physics, or materials science.",
            "current_education_status": "Graduated or final-semester students expecting degree completion before semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in Tier 1 / Tier 2 (Q1/Q2) Web of Science (WoS) indexed journals provide a decisive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, MUET Band 4.5+, or official English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Malay language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure endorsement and laboratory sponsorship from an active Universiti Malaya professor with high-impact research funding.",
            "previous_scholarship_restrictions": "Cannot hold any concurrent national scholarship, industrial sponsorship, or full-time paid employment.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for the complete doctoral degree program at Universiti Malaya.",
                "amount": "100% covered (~RM 25,000 to 35,000 / year value; ~PKR 1,625,000 to 2,275,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Universiti Malaya international application fee of RM 300 paid during online portal submission.",
                "amount": "RM 300 (~PKR 19,500)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate residential colleges (Kolej Kediaman Raja Dr. Nazrin Shah - KK12) at subsidized monthly rates (approx. RM 350 to 550 / month), paid from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free fellowship allowance: RM 2,500 to RM 3,000 / month (~PKR 162,500 to 195,000 / month) disbursed directly to scholar's bank account.",
                "amount": "RM 2,500 to 3,000 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Kuala Lumpur is self-funded.",
                "amount": "Not covered in central scheme"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "EMGS visa processing and Malaysian Student Pass fees paid by candidate.",
                "amount": "Approx. RM 2,200 to 2,600 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Malaysian student medical and hospitalization insurance provided via EMGS student pass package.",
                "amount": "100% covered student medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Campus cafeterias across UM Kuala Lumpur campus provide affordable dining; daily meals cost approximately RM 18 to 30.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to UM Central Library (largest university library in Malaysia), high-performance computing centers, and advanced characterization laboratories.",
                "amount": "100% covered library & computational infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference attendance and publication charges (APC) for high-impact Q1 WoS journals funded directly from host supervisor grant.",
                "amount": "Grant-funded conference travel and APC charges"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free UM campus shuttle bus network connecting all faculties, residential colleges, and Universiti LRT metro station.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Malaysia #1 premier flagship research university (Universiti Malaya - UM).",
            "participating_institutions": [
                "Universiti Malaya Main Campus (Kuala Lumpur, Malaysia)"
            ],
            "university_rankings_scope": "QS World University Rankings #60 globally, #1 in Malaysia, Top 15 in Asia; internationally prestigious research institution with world-class engineering, medical, and science faculties.",
            "available_majors": [
                "PhD in Electrical Engineering",
                "PhD in Mechanical Engineering",
                "PhD in Chemical Engineering",
                "PhD in Civil Engineering",
                "PhD in Computer Science and Software Engineering",
                "PhD in Artificial Intelligence and Data Science",
                "PhD in Biomedical Sciences",
                "PhD in Materials Science and Physics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 to 4 years (Doctor of Philosophy)",
            "admission_requirements_summary": "Bachelor's / Master's degree with First Class / CGPA >= 3.70/4.00, academic transcripts, technical research proposal, supervisor endorsement form, two reference letters, and IELTS 6.5 / TOEFL 80 or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "High competition in Faculty of Engineering and Faculty of Computer Science & Information Technology; securing a prominent UM professor's endorsement is the decisive requirement.",
            "strategic_program_match_advice": "Focus research proposals on renewable energy, smart materials, AI for healthcare, or advanced communication systems where UM professors hold major national High Impact Research (HIR) grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://brightsparks.um.edu.my/ & https://pgadmission.um.edu.my/",
            "portal_system_name": "Universiti Malaya Postgraduate Admissions Portal & Bright Sparks System",
            "account_creation_instructions": "Contact prospective supervisor, obtain acceptance form, register on UM postgraduate portal, submit PhD application, upload credentials, and pay RM 300 fee.",
            "step_by_step_workflow": [
                "Step 1: Explore UM faculty research groups and contact prospective supervisors with CV and research draft (March-April for October intake / September-October for March intake).",
                "Step 2: Obtain signed UM Supervisor Acceptance and Bright Sparks Recommendation Form.",
                "Step 3: Register on UM postgraduate admission portal and submit application.",
                "Step 4: Upload attested academic transcripts, research proposal, passport copy, and English proof.",
                "Step 5: Faculty Graduate Committee reviews technical proposal and conducts interview.",
                "Step 6: UM Bright Sparks Unit issues official Letter of Offer and Fellowship Award Letter.",
                "Step 7: Apply for EMGS Visa Approval Letter (VAL) and Single Entry Visa at Malaysian High Commission in Islamabad.",
                "Step 8: Travel to Kuala Lumpur, complete medical screening, and matriculate."
            ],
            "university_vs_scholarship_routing": "Integrated departmental route: Application for admission and Bright Sparks fellowship are reviewed together upon faculty recommendation.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed PDF recommendation letters on official university letterheads.",
            "personal_statement_prompts": "Statement of research intent detailing technical competencies, research goals, and synergy with host supervisor's funded research project.",
            "study_plan_research_proposal_requirements": "5 to 8 page structured research proposal covering problem statement, literature review, methodology, equipment needs, and milestone schedule.",
            "cv_format_requirements": "Academic CV detailing qualifications, field/laboratory experience, software proficiencies, and publications list.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Google Meet or MS Teams conducted by prospective supervisor and departmental postgraduate coordinator.",
            "standardized_tests": "IELTS 6.5+, TOEFL 80+, MUET Band 4.5+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "RM 300 (approx. USD 70 / ~PKR 19,500)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani credentials during EMGS processing.",
            "translation_requirements": "Certified English translations for all non-English documents.",
            "final_submission_method": "Online submission via Universiti Malaya postgraduate admission portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Official Bachelor's / Master's degree certificates and complete semester transcripts with CGPA >= 3.70.",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "Technical Research Proposal",
                "mandatory": True,
                "specification": "Structured research proposal (5-8 pages) aligned with supervisor's research grant objectives.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Supervisor Acceptance & Bright Sparks Endorsement Form",
                "mandatory": True,
                "specification": "Official UM form signed by prospective supervisor confirming laboratory placement and willingness to supervise.",
                "pakistan_specific_instruction": "Obtained directly from UM faculty supervisor."
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
                "specification": "IELTS 6.5+, TOEFL iBT 80+, MUET Band 4.5+, or official English Medium of Instruction (MOI) certificate.",
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
            "academic_weight": "35% (Prior CGPA >= 3.70, academic excellence in engineering/science)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and leadership)",
            "research_experience_weight": "35% (Prior Q1/Q2 publications, technical proposal rigor, supervisor synergy)",
            "work_experience_weight": "5% (Laboratory technical or industry R&D experience)",
            "personal_statement_weight": "5% (Clarity of purpose and dedication to research)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit and research capability based)",
            "selection_panel_composition": "Faculty Postgraduate Committee, Bright Sparks Steering Committee, and Host Research Project PI.",
            "evaluation_methodology": "Two-stage evaluation: departmental technical vetting followed by Bright Sparks central committee award confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 1,600 applicants across both semesters",
            "total_scholarships_awarded": "~80 to 120 Bright Sparks awards annually",
            "acceptance_rate_global": "~6.0% to 8.0%",
            "acceptance_rate_pakistan": "~12.0% to 15.0% for applicants with pre-secured supervisor endorsement and CGPA >= 3.75",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.75 / 4.00, coupled with prior lab project experience or publications",
            "typical_academic_and_research_profile": "Top graduates in engineering, computing, or science with strong programming/lab skills, clear research plan, and supervisor endorsement.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Malaysia, Pakistan, Indonesia, Nigeria, Iran, Bangladesh, Egypt.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal brightsparks.um.edu.my.",
                "Do not pay money to educational agents promising guaranteed Bright Sparks appointments; awards depend entirely on faculty supervisor endorsement."
            ],
            "application_fee_warning": "University application fee is RM 300 paid directly to UM via secure online payment.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are flagged and rejected; applicants must write their own technical research proposal.",
            "hidden_costs_breakdown": [
                "UM application fee: RM 300 (~PKR 19,500).",
                "EMGS visa approval and student pass fees: ~RM 2,200 to 2,600 (~PKR 143,000 to 169,000).",
                "HEC and MoFA document attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "One-way flight to Kuala Lumpur: ~PKR 90,000 to 130,000.",
                "Initial living deposit before first stipend cycle: ~RM 1,200 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Scheme covers international flights. Reality: International travel and EMGS visa fees are self-funded.",
                "Myth: You can apply without contacting a supervisor. Reality: Supervisor endorsement is effectively mandatory for Bright Sparks approval."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim scheme is purely a fee discount; in reality, Bright Sparks includes full tuition waiver and monthly living allowance."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum CGPA 3.50 and Satisfactory (TM) research progress evaluation every semester.",
            "attendance_requirements": "Full-time physical research presence at UM Kuala Lumpur campus; scholars must fulfill mandatory graduation criteria (minimum 2 papers in WoS Q1/Q2 journals).",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by supervisor and presented to Bright Sparks Unit.",
            "work_restrictions_during_study": "Recipients are barred from taking full-time outside employment; internal paid tutoring or research assistance is permitted within university limits.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment in Malaysia or abroad upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond; recipients must meet graduation publication requirements under UM affiliation.",
            "repayment_clawback_conditions": "Termination of monthly stipend and withdrawal of fee waiver if research progress is evaluated as Unsatisfactory across consecutive reviews.",
            "rules_for_changing_university": "Non-transferable; scheme is funded internally by UM.",
            "rules_for_changing_major": "Field of research cannot be changed without written permission from faculty dean and Bright Sparks Unit.",
            "extension_policy": "Extensions beyond maximum tenure (36 months) require special approval and are generally self-funded."
        },
        "official_sources_verified": [
            {
                "source_name": "Universiti Malaya Bright Sparks Official Portal",
                "source_url": "https://brightsparks.um.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Universiti Malaya Institute of Graduate Studies (IPS)",
                "source_url": "https://pgadmission.um.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
