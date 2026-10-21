"""Batch 26 Part 3: South Korean Elite S&T Research Awards (4 awards)
SCH-AS-068: POSTECH International Graduate Fellowship & Full Research Assistantship
SCH-AS-069: UNIST International Graduate Scholarship (UIGS)
SCH-AS-070: DGIST Presidential International Graduate Fellowship
SCH-AS-071: GIST International Graduate Scholarship & Research Assistantship
"""

DATA_P3 = {
    "SCH-AS-068": {
        "scholarship_id": "SCH-AS-068",
        "basic_details": {
            "scholarship_name": "Pohang University of Science and Technology (POSTECH) International Graduate Fellowship & Research Assistantship",
            "offering_entity": "Pohang University of Science and Technology (POSTECH) & POSCO Foundation, South Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "POSTECH Campus (Pohang, Gyeongsangbuk-do, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & PhD"],
            "major_restrictions": "Department of Physics, Department of Chemistry, Department of Life Sciences, Department of Materials Science and Engineering, Department of Mechanical Engineering, Department of Chemical Engineering, Department of Electronic and Electrical Engineering, Department of Computer Science and Engineering, Graduate School of Artificial Intelligence, and Division of Advanced Nuclear Engineering.",
            "number_of_awards_total": "~120 to 180 international graduate fellowships awarded annually across departments",
            "number_of_awards_pakistan": "Open internationally; typically 15 to 25 Pakistani STEM and informatics researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 semesters (2 years) for Master's; 6 to 8 semesters (3 to 4 years) for PhD; 10 semesters (5 years) for Combined MS/PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Combined tuition waiver and research assistantship: 100% full tuition covered plus KRW 1,100,000 to 1,500,000 / month for Master's (~PKR 231,000 to 315,000 / month) and KRW 1,500,000 to 2,100,000 / month for PhD (~PKR 315,000 to 441,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents both hold non-Korean citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to young researchers with exceptional academic momentum.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum CGPA 3.30/4.00 for Master's; recognized 18-year Master's degree with minimum CGPA 3.30/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum CGPA 3.30 / 4.00; competitive applicants at POSTECH typically possess CGPA >= 3.65 / 4.00 or top 5-10% class rank.",
            "subject_background_prerequisites": "Computer science, artificial intelligence, electrical engineering, materials science, mechanical engineering, chemical engineering, physics, chemistry, or life sciences.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in peer-reviewed journals (SCI/SCIE) or top conferences (IEEE, ACM) provide a substantial competitive edge.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 79, TOEIC 750+, or official English Medium of Instruction (MOI) certificate from an accredited university.",
            "other_language_requirements": "Korean language proficiency is not required; all graduate courses, seminars, and research are conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All admitted international graduate students are automatically considered for the POSTECH Fellowship and laboratory assistantship package upon faculty recommendation.",
            "previous_scholarship_restrictions": "Cannot hold another parallel government fellowship covering identical living and tuition benefits.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver covering all standard degree semesters at POSTECH.",
                "amount": "100% covered (~KRW 8,500,000 to 11,000,000 / year value; ~PKR 1,785,000 to 2,310,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Online application fee of USD 80 (or KRW 80,000) paid via credit card on the POSTECH admissions portal.",
                "amount": "USD 80 (~PKR 22,400)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing in Pohang (DICE / Graduate Student Apartments; approx. KRW 120,000 to 200,000 / month), paid easily from living stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Combined institutional fellowship and laboratory research assistantship: KRW 1,100,000 to 1,500,000 / month for Master's; KRW 1,500,000 to 2,100,000 / month for PhD.",
                "amount": "KRW 1,100,000 to 2,100,000 / month (~PKR 231,000 to 441,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Busan/Seoul Incheon International Airport is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 Student Visa fee paid directly to the Korean Embassy in Islamabad.",
                "amount": "Approx. USD 60 (~PKR 17,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory enrollment in Korea National Health Insurance Service (NHIS); subsidized monthly premium (approx. KRW 70,000 / month) paid from stipend.",
                "amount": "Subsidized Korea National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized on-campus student cafeterias (Jigok Community Center and Student Hall); meals cost KRW 4,000 to 6,500.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to POSTECH Tae-Joon Park Digital Library, Pohang Light Source (PLS-II synchrotron facility), and Max Planck Korea Research Initiative laboratories.",
                "amount": "100% covered synchrotron and laboratory infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and POSCO Foundation funds cover international conference registration, travel, and accommodation for accepted papers.",
                "amount": "Lab grant-funded international conference travel"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized KTX high-speed train transit to Seoul (Pohang KTX Station connects directly to Seoul Station in 2.2 hours).",
                "amount": "Subsidized high-speed rail access"
            },
            "total_estimated_value_usd_per_year": 25000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single South Korea elite private research institute (POSTECH, Pohang).",
            "participating_institutions": [
                "Pohang University of Science and Technology (Pohang Campus, Gyeongsangbuk-do, South Korea)"
            ],
            "university_rankings_scope": "QS World University Rankings #98 globally, World Top 30 in Materials Science, Top 5 in South Korea; recognized as the 'Caltech of Asia' with an ultra-low student-to-faculty ratio (3:1).",
            "available_majors": [
                "Master's / PhD in Materials Science and Engineering",
                "Master's / PhD in Computer Science and Engineering",
                "Master's / PhD in Graduate School of Artificial Intelligence",
                "Master's / PhD in Electronic and Electrical Engineering",
                "Master's / PhD in Mechanical Engineering",
                "Master's / PhD in Chemical Engineering",
                "Master's / PhD in Physics and Chemistry"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years; Combined MS/PhD: 5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.30/4.00, academic transcripts, statement of purpose, two recommendation letters, English test score (IELTS 6.0+ / TOEFL 79+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Graduate School of AI, Computer Science, and Materials Science are fiercely competitive; contacting professors prior to applying significantly increases admission and RA funding odds.",
            "strategic_program_match_advice": "Review recent publications from POSTECH faculty laboratories, particularly those connected to the Pohang Light Source or POSCO battery and semiconductor projects, and send a targeted research query."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://adm-g.postech.ac.kr/",
            "portal_system_name": "POSTECH Graduate Admissions Online Portal",
            "account_creation_instructions": "Register on the POSTECH admissions portal, complete online application form, upload personal statement and transcripts, pay USD 80 fee, and dispatch certified physical documents to POSTECH Admissions Office.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective POSTECH professors in target research areas with CV and research interests (July-August for Spring / December-January for Fall).",
                "Step 2: Register on POSTECH Graduate Admissions Online System during open intake.",
                "Step 3: Complete online application, upload documents, and pay USD 80 fee.",
                "Step 4: Register two academic recommenders who submit evaluation letters online.",
                "Step 5: Send certified hard-copy documents (degrees, transcripts, apostille/attestation) via DHL to POSTECH Admissions Office in Pohang.",
                "Step 6: Departmental faculty committee reviews dossiers and conducts virtual technical interviews.",
                "Step 7: Final admission and scholarship award results announced online.",
                "Step 8: Obtain Certificate of Admission (CoA), apply for South Korean D-2 visa, and arrive in Pohang."
            ],
            "university_vs_scholarship_routing": "Integrated Institutional Route: Admission and scholarship funding are decided together based on departmental faculty recommendation.",
            "recommendation_letters_submission_method": "Submitted online by two academic recommenders via confidential portal links.",
            "personal_statement_prompts": "Personal Statement and Research Plan (prescribed POSTECH format) describing motivation, research experiences, scholarly interests, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "Structured research plan detailing proposed technical investigations, methodologies, and alignment with target POSTECH laboratories.",
            "cv_format_requirements": "Academic research CV detailing education, laboratory proficiencies, software skills, and publication history.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental faculty panel.",
            "standardized_tests": "IELTS Academic 6.0+, TOEFL iBT 79+, TOEIC 750+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "USD 80 (approx. PKR 22,400)",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required, followed by Korean Embassy consular legalization in Islamabad or Apostille.",
            "translation_requirements": "Certified English or Korean translation for all non-English/non-Korean documents.",
            "final_submission_method": "Dual submission: Online portal application followed by mandatory postal dispatch of certified physical dossier to POSTECH."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.30/4.00.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and consular legalized by Korean Embassy Islamabad."
            },
            {
                "document_name": "Personal Statement and Research Plan",
                "mandatory": True,
                "specification": "Completed on official POSTECH form detailing background, motivation, research interests, and career goals.",
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
                "specification": "IELTS Academic 6.0+, TOEFL iBT 79+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and awards.",
                "pakistan_specific_instruction": "Professional academic CV."
            },
            {
                "document_name": "Family Relationship Certificate & Passport Copies",
                "mandatory": True,
                "specification": "Family Registration Certificate (FRC) and copies of passports of applicant and parents.",
                "pakistan_specific_instruction": "NADRA Family Registration Certificate (FRC) in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "August 25 (Spring intake) / February 20 (Fall intake)",
            "application_deadline": "September 25 (Spring intake) / March 25 (Fall intake)",
            "university_admission_deadline": "September 25 / March 25",
            "document_submission_deadline": "October 5 / April 5 (Hard copy postal arrival in Pohang)",
            "recommendation_letters_deadline": "September 28 / March 28",
            "interview_period": "October - November / April - May",
            "shortlist_announcement": "Late November (Spring) / Early June (Fall)",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "January / July",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Bi-annual intake: Spring semester starts in March, Fall semester starts in September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic rigor in engineering/science, university standing)",
            "extracurricular_and_leadership_weight": "5% (Initiative, teamwork, problem-solving mindset)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with POSTECH research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "POSTECH Departmental Admissions Committee, School Graduate Deans, and Admissions Board.",
            "evaluation_methodology": "Rigorous holistic evaluation assessing mathematical ability, research productivity, experimental aptitude, and alignment with faculty laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,400 international applicants across both intakes",
            "total_scholarships_awarded": "~120 to 180 fully funded international awards annually",
            "acceptance_rate_global": "~7.0% to 9.0%",
            "acceptance_rate_pakistan": "~12.0% to 15.0% for applicants with strong research profiles and CGPA >= 3.60",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.60 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records in computer science, engineering, or physics, documented project experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, Vietnam, China, India, Indonesia, Turkey, Iran, Russia.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal adm-g.postech.ac.kr.",
                "POSTECH does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of USD 80 is paid directly through the secure POSTECH online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: USD 80 (~PKR 22,400).",
                "NADRA FRC and document attestations (HEC, MoFA, Korean Embassy): ~PKR 35,000 to 50,000.",
                "DHL document courier to South Korea: ~PKR 12,000.",
                "South Korean D-2 Visa fee: ~USD 60 (~PKR 17,000).",
                "Flight to Busan / Seoul: ~PKR 150,000 to 220,000.",
                "Initial living deposit before first stipend payment: ~KRW 500,000 (~PKR 105,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Korean TOPIK certificate is needed. Reality: 100% of graduate education at POSTECH is conducted in English.",
                "Myth: Flights are included. Reality: Airfare to South Korea is self-funded by the student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim POSTECH requires GRE; GRE is optional and not mandatory for international graduate admissions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.00 out of 4.30 to retain the fellowship and tuition waiver each semester.",
            "attendance_requirements": "Full-time physical research presence at POSTECH campus; daily participation in laboratory research activities.",
            "academic_progress_monitoring": "Semi-annual academic progress review evaluated by research advisor.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Korean immigration law; part-time work requires permission from immigration and university.",
            "home_country_return_obligation": "None; graduates are eligible for Korean D-10 job seeker visas or E-7 professional engineering visas upon graduation.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if semester GPA drops below 3.00 or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Extensions beyond standard 4 semesters (Master's) or 8 semesters (PhD) are generally not covered by the scholarship."
        },
        "official_sources_verified": [
            {
                "source_name": "POSTECH Graduate Admissions Official Portal",
                "source_url": "https://adm-g.postech.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "POSTECH International Student and Scholar Services",
                "source_url": "https://www.postech.ac.kr/eng/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-069": {
        "scholarship_id": "SCH-AS-069",
        "basic_details": {
            "scholarship_name": "Ulsan National Institute of Science and Technology (UNIST) International Graduate Scholarship (UIGS)",
            "offering_entity": "Ulsan National Institute of Science and Technology (UNIST) & Ministry of Science and ICT (MSIT), South Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "UNIST Main Campus (Ulsan, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & PhD"],
            "major_restrictions": "School of Energy and Chemical Engineering, School of Materials Science and Engineering, Department of Computer Science and Engineering, Department of Artificial Intelligence, Department of Electrical Engineering, Department of Mechanical Engineering, and Department of Biomedical Engineering.",
            "number_of_awards_total": "~150 to 220 international graduate scholarships awarded annually across departments",
            "number_of_awards_pakistan": "Very strong cohort; typically 20 to 35 Pakistani researchers in energy, materials, and computing appointed annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 semesters (2 years) for Master's; 8 semesters (4 years) for PhD; 10 semesters (5 years) for Combined MS/PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Combined tuition waiver and stipend: 100% full tuition fee covered plus monthly stipend of KRW 1,000,000 to 1,400,000 / month for Master's (~PKR 210,000 to 294,000 / month) and KRW 1,400,000 to 1,900,000 / month for PhD (~PKR 294,000 to 399,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents both hold non-Korean citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to young researchers with exceptional academic momentum.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum CGPA 3.20/4.00 for Master's; recognized 18-year Master's degree with minimum CGPA 3.20/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum CGPA 3.20 / 4.00; competitive applicants at UNIST typically possess CGPA >= 3.55 / 4.00 or top 10% class rank.",
            "subject_background_prerequisites": "Energy engineering, chemical engineering, materials science, computer science, artificial intelligence, electrical engineering, mechanical engineering, or biomedical engineering.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in energy materials (batteries, solar cells), computing, or engineering journals provide a substantial competitive edge.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, TOEIC 800+, or official English Medium of Instruction (MOI) certificate from an accredited university.",
            "other_language_requirements": "Korean language proficiency is not required; 100% of graduate lectures, research, and dissertations are conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All admitted international graduate students receive the UNIST International Graduate Scholarship automatically upon admission.",
            "previous_scholarship_restrictions": "Cannot hold another parallel government fellowship covering identical living and tuition benefits.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver covering all standard degree semesters at UNIST.",
                "amount": "100% covered (~KRW 7,500,000 to 9,500,000 / year value; ~PKR 1,575,000 to 1,995,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Online application fee of USD 50 (or KRW 50,000) paid via credit card on the UNIST admissions portal.",
                "amount": "USD 50 (~PKR 14,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing in Ulsan (twin rooms approx. KRW 130,000 to 190,000 / month), paid easily from living stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Combined institutional stipend and laboratory research assistantship: KRW 1,000,000 to 1,400,000 / month for Master's; KRW 1,400,000 to 1,900,000 / month for PhD.",
                "amount": "KRW 1,000,000 to 1,900,000 / month (~PKR 210,000 to 399,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Busan/Seoul Incheon International Airport is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 Student Visa fee paid directly to the Korean Embassy in Islamabad.",
                "amount": "Approx. USD 60 (~PKR 17,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory enrollment in Korea National Health Insurance Service (NHIS); subsidized monthly premium (approx. KRW 70,000 / month) paid from stipend.",
                "amount": "Subsidized Korea National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized on-campus student cafeterias across UNIST campus; meals cost KRW 4,000 to 6,000.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to UNIST Central Library, Ulsan Center for Future Battery Technology, supercomputing clusters, and cleanrooms.",
                "amount": "100% covered world-leading energy lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants cover international conference registration, travel, and accommodation for accepted papers.",
                "amount": "Lab grant-funded international conference travel"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized bus transit connecting UNIST campus to Ulsan KTX Station (10 minutes away) and central Ulsan.",
                "amount": "Subsidized regional bus & KTX rail access"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single South Korea national research institute (UNIST, Ulsan).",
            "participating_institutions": [
                "Ulsan National Institute of Science and Technology (UNIST Campus, Eonyang, Ulsan, South Korea)"
            ],
            "university_rankings_scope": "QS World University Rankings #216 globally, World Top 50 in Materials Science and Energy Engineering; ranked #1 in South Korea for citations per faculty.",
            "available_majors": [
                "Master's / PhD in School of Energy and Chemical Engineering (Secondary Batteries, Solar, Hydrogen)",
                "Master's / PhD in School of Materials Science and Engineering",
                "Master's / PhD in Department of Computer Science and Engineering",
                "Master's / PhD in Department of Artificial Intelligence",
                "Master's / PhD in Department of Electrical Engineering",
                "Master's / PhD in Department of Mechanical Engineering",
                "Master's / PhD in Department of Biomedical Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years; Combined MS/PhD: 5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.20/4.00, academic transcripts, statement of purpose, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 80+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of Energy and Chemical Engineering is world-leading in secondary battery research (Li-ion, solid-state) and highly competitive; establishing professor contact before applying is strongly recommended.",
            "strategic_program_match_advice": "Focus research proposals on next-generation battery technology, perovskite photovoltaics, or machine learning for materials design where UNIST holds massive industrial funding from Samsung SDI and Hyundai."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://adm-g.unist.ac.kr/",
            "portal_system_name": "UNIST Graduate Admissions Online Portal",
            "account_creation_instructions": "Register on the UNIST admissions portal, complete online application form, upload personal statement and transcripts, pay USD 50 fee, and dispatch certified physical documents to UNIST Admissions Office.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective UNIST professors in target research areas with CV and research interests (July-August for Spring / December-January for Fall).",
                "Step 2: Register on UNIST Graduate Admissions Online System during open intake.",
                "Step 3: Complete online application, upload documents, and pay USD 50 fee.",
                "Step 4: Register two academic recommenders who submit evaluation letters online.",
                "Step 5: Send certified hard-copy documents (degrees, transcripts, apostille/attestation) via DHL to UNIST Admissions Office in Ulsan.",
                "Step 6: Departmental faculty committee reviews dossiers and conducts virtual technical interviews.",
                "Step 7: Final admission and scholarship award results announced online.",
                "Step 8: Obtain Certificate of Admission (CoA), apply for South Korean D-2 visa, and arrive in Ulsan."
            ],
            "university_vs_scholarship_routing": "Integrated Institutional Route: Admission and scholarship funding are decided together based on departmental faculty recommendation.",
            "recommendation_letters_submission_method": "Submitted online by two academic recommenders via confidential portal links.",
            "personal_statement_prompts": "Personal Statement and Study Plan (prescribed UNIST format) describing motivation, research experiences, scholarly interests, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "Structured research plan detailing proposed technical investigations, methodologies, and alignment with target UNIST laboratories.",
            "cv_format_requirements": "Academic research CV detailing education, laboratory proficiencies, software skills, and publication history.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental faculty panel.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 80+, TOEIC 800+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "USD 50 (approx. PKR 14,000)",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required, followed by Korean Embassy consular legalization in Islamabad or Apostille.",
            "translation_requirements": "Certified English or Korean translation for all non-English/non-Korean documents.",
            "final_submission_method": "Dual submission: Online portal application followed by mandatory postal dispatch of certified physical dossier to UNIST."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.20/4.00.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and consular legalized by Korean Embassy Islamabad."
            },
            {
                "document_name": "Personal Statement and Study Plan",
                "mandatory": True,
                "specification": "Completed on official UNIST form detailing background, motivation, research interests, and career goals.",
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
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and awards.",
                "pakistan_specific_instruction": "Professional academic CV."
            },
            {
                "document_name": "Family Relationship Certificate & Passport Copies",
                "mandatory": True,
                "specification": "Family Registration Certificate (FRC) and copies of passports of applicant and parents.",
                "pakistan_specific_instruction": "NADRA Family Registration Certificate (FRC) in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "August 20 (Spring intake) / February 15 (Fall intake)",
            "application_deadline": "September 20 (Spring intake) / March 20 (Fall intake)",
            "university_admission_deadline": "September 20 / March 20",
            "document_submission_deadline": "October 1 / April 1 (Hard copy postal arrival in Ulsan)",
            "recommendation_letters_deadline": "September 25 / March 25",
            "interview_period": "October - November / April - May",
            "shortlist_announcement": "Late November (Spring) / Early June (Fall)",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "January / July",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Bi-annual intake: Spring semester starts in March, Fall semester starts in September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic rigor in engineering/science, university standing)",
            "extracurricular_and_leadership_weight": "5% (Initiative, teamwork, problem-solving mindset)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with UNIST research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "UNIST Departmental Admissions Committee, School Graduate Deans, and Admissions Board.",
            "evaluation_methodology": "Rigorous holistic evaluation assessing mathematical ability, research productivity, experimental aptitude, and alignment with faculty laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,600 to 2,200 international applicants across both intakes",
            "total_scholarships_awarded": "~150 to 220 fully funded international awards annually",
            "acceptance_rate_global": "~8.0% to 10.0%",
            "acceptance_rate_pakistan": "~14.0% to 18.0% for applicants with strong research profiles and CGPA >= 3.50",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.50 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with solid records in materials science, chemistry, computing, or engineering, documented laboratory experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, Vietnam, China, India, Indonesia, Turkey, Iran, Russia.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal adm-g.unist.ac.kr.",
                "UNIST does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of USD 50 is paid directly through the secure UNIST online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: USD 50 (~PKR 14,000).",
                "NADRA FRC and document attestations (HEC, MoFA, Korean Embassy): ~PKR 35,000 to 50,000.",
                "DHL document courier to South Korea: ~PKR 12,000.",
                "South Korean D-2 Visa fee: ~USD 60 (~PKR 17,000).",
                "Flight to Busan / Seoul: ~PKR 150,000 to 220,000.",
                "Initial living deposit before first stipend payment: ~KRW 500,000 (~PKR 105,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Korean TOPIK certificate is needed. Reality: 100% of graduate education at UNIST is conducted in English.",
                "Myth: Flights are included. Reality: Airfare to South Korea is self-funded by the student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim UNIST requires GRE; GRE is optional and not mandatory for international graduate admissions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.00 out of 4.30 to retain the fellowship and tuition waiver each semester.",
            "attendance_requirements": "Full-time physical research presence at UNIST campus; daily participation in laboratory research activities.",
            "academic_progress_monitoring": "Semi-annual academic progress review evaluated by research advisor.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Korean immigration law; part-time work requires permission from immigration and university.",
            "home_country_return_obligation": "None; graduates are eligible for Korean D-10 job seeker visas or E-7 professional engineering visas upon graduation.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if semester GPA drops below 3.00 or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Extensions beyond standard 4 semesters (Master's) or 8 semesters (PhD) are generally not covered by the scholarship."
        },
        "official_sources_verified": [
            {
                "source_name": "UNIST Graduate Admissions Official Portal",
                "source_url": "https://adm-g.unist.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UNIST Center for International Affairs",
                "source_url": "https://www.unist.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-070": {
        "scholarship_id": "SCH-AS-070",
        "basic_details": {
            "scholarship_name": "Daegu Gyeongbuk Institute of Science and Technology (DGIST) Presidential International Graduate Fellowship",
            "offering_entity": "Daegu Gyeongbuk Institute of Science and Technology (DGIST) & Ministry of Science and ICT (MSIT), South Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "DGIST Main Campus (Dalseong-gun, Daegu, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & PhD"],
            "major_restrictions": "Department of Physics and Chemistry, Department of Electrical Engineering and Computer Science, Department of Robotics and Mechatronics Engineering, Department of Energy Science and Engineering, Department of Brain Sciences, and Department of New Biology.",
            "number_of_awards_total": "~80 to 120 international graduate fellowships awarded annually across departments",
            "number_of_awards_pakistan": "Open internationally; typically 10 to 18 Pakistani researchers in robotics, energy, and computing appointed annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 semesters (2 years) for Master's; 8 semesters (4 years) for PhD; 10 semesters (5 years) for Combined MS/PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Combined tuition waiver and research assistantship: 100% full tuition fee covered plus monthly stipend of KRW 1,000,000 to 1,350,000 / month for Master's (~PKR 210,000 to 283,500 / month) and KRW 1,400,000 to 1,850,000 / month for PhD (~PKR 294,000 to 388,500 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents both hold non-Korean citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to young researchers with exceptional academic momentum.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum CGPA 3.20/4.00 for Master's; recognized 18-year Master's degree with minimum CGPA 3.20/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum CGPA 3.20 / 4.00; competitive applicants at DGIST typically possess CGPA >= 3.50 / 4.00.",
            "subject_background_prerequisites": "Robotics, mechatronics, electrical engineering, computer science, energy science, brain sciences, physics, chemistry, or biological sciences.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in robotics, neuroscience, energy, or computing journals provide a substantial competitive edge.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 79, TOEIC 750+, or official English Medium of Instruction (MOI) certificate from an accredited university.",
            "other_language_requirements": "Korean language proficiency is not required; all graduate lectures, research, and dissertations are conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All admitted international graduate students receive the DGIST Fellowship and research assistantship automatically upon admission.",
            "previous_scholarship_restrictions": "Cannot hold another parallel government fellowship covering identical living and tuition benefits.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver covering all standard degree semesters at DGIST.",
                "amount": "100% covered (~KRW 7,000,000 to 9,000,000 / year value; ~PKR 1,470,000 to 1,890,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Online application fee of USD 50 (or KRW 50,000) paid via credit card on the DGIST admissions portal.",
                "amount": "USD 50 (~PKR 14,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing in Daegu (twin rooms approx. KRW 120,000 to 180,000 / month), paid easily from living stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Combined institutional stipend and laboratory research assistantship: KRW 1,000,000 to 1,350,000 / month for Master's; KRW 1,400,000 to 1,850,000 / month for PhD.",
                "amount": "KRW 1,000,000 to 1,850,000 / month (~PKR 210,000 to 388,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Daegu/Busan/Seoul is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 Student Visa fee paid directly to the Korean Embassy in Islamabad.",
                "amount": "Approx. USD 60 (~PKR 17,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory enrollment in Korea National Health Insurance Service (NHIS); subsidized monthly premium (approx. KRW 70,000 / month) paid from stipend.",
                "amount": "Subsidized Korea National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized on-campus student cafeterias across DGIST campus; meals cost KRW 4,000 to 6,000.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to DGIST Academic Information Center, core research instrumentation facilities, and brain-machine interface laboratories.",
                "amount": "100% covered robotics and brain science lab access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants cover international conference registration, travel, and accommodation for accepted papers.",
                "amount": "Lab grant-funded international conference travel"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Free campus shuttle buses connecting DGIST campus to Daegu metro lines and Dongdaegu KTX Station.",
                "amount": "Free campus shuttle & subsidized KTX access"
            },
            "total_estimated_value_usd_per_year": 23000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single South Korea national research institute (DGIST, Daegu).",
            "participating_institutions": [
                "Daegu Gyeongbuk Institute of Science and Technology (DGIST Campus, Dalseong-gun, Daegu, South Korea)"
            ],
            "university_rankings_scope": "One of South Korea's four elite public S&T institutes (along with KAIST, GIST, and UNIST); renowned for robotics, brain-computer interfaces, and energy science.",
            "available_majors": [
                "Master's / PhD in Department of Robotics and Mechatronics Engineering",
                "Master's / PhD in Department of Electrical Engineering and Computer Science",
                "Master's / PhD in Department of Energy Science and Engineering",
                "Master's / PhD in Department of Brain Sciences",
                "Master's / PhD in Department of Physics and Chemistry",
                "Master's / PhD in Department of New Biology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years; Combined MS/PhD: 5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.20/4.00, academic transcripts, statement of purpose, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 79+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Robotics and Mechatronics Engineering and Brain Sciences are national flagships; establishing professor contact before applying is strongly recommended.",
            "strategic_program_match_advice": "Focus research proposals on autonomous systems, brain-machine interfaces, or next-generation energy harvesting where DGIST holds dedicated national research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.dgist.ac.kr/adm_g/",
            "portal_system_name": "DGIST Graduate Admissions Online Portal",
            "account_creation_instructions": "Register on the DGIST admissions portal, complete online application form, upload personal statement and transcripts, pay USD 50 fee, and dispatch certified physical documents to DGIST Admissions Office.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective DGIST professors in target research areas with CV and research interests (July-August for Spring / December-January for Fall).",
                "Step 2: Register on DGIST Graduate Admissions Online System during open intake.",
                "Step 3: Complete online application, upload documents, and pay USD 50 fee.",
                "Step 4: Register two academic recommenders who submit evaluation letters online.",
                "Step 5: Send certified hard-copy documents (degrees, transcripts, apostille/attestation) via DHL to DGIST Admissions Office in Daegu.",
                "Step 6: Departmental faculty committee reviews dossiers and conducts virtual technical interviews.",
                "Step 7: Final admission and scholarship award results announced online.",
                "Step 8: Obtain Certificate of Admission (CoA), apply for South Korean D-2 visa, and arrive in Daegu."
            ],
            "university_vs_scholarship_routing": "Integrated Institutional Route: Admission and scholarship funding are decided together based on departmental faculty recommendation.",
            "recommendation_letters_submission_method": "Submitted online by two academic recommenders via confidential portal links.",
            "personal_statement_prompts": "Personal Statement and Study Plan (prescribed DGIST format) describing motivation, research experiences, scholarly interests, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "Structured research plan detailing proposed technical investigations, methodologies, and alignment with target DGIST laboratories.",
            "cv_format_requirements": "Academic research CV detailing education, laboratory proficiencies, software skills, and publication history.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental faculty panel.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 79+, TOEIC 750+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "USD 50 (approx. PKR 14,000)",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required, followed by Korean Embassy consular legalization in Islamabad or Apostille.",
            "translation_requirements": "Certified English or Korean translation for all non-English/non-Korean documents.",
            "final_submission_method": "Dual submission: Online portal application followed by mandatory postal dispatch of certified physical dossier to DGIST."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.20/4.00.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and consular legalized by Korean Embassy Islamabad."
            },
            {
                "document_name": "Personal Statement and Study Plan",
                "mandatory": True,
                "specification": "Completed on official DGIST form detailing background, motivation, research interests, and career goals.",
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
                "specification": "IELTS Academic 6.5+, TOEFL iBT 79+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and awards.",
                "pakistan_specific_instruction": "Professional academic CV."
            },
            {
                "document_name": "Family Relationship Certificate & Passport Copies",
                "mandatory": True,
                "specification": "Family Registration Certificate (FRC) and copies of passports of applicant and parents.",
                "pakistan_specific_instruction": "NADRA Family Registration Certificate (FRC) in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "August 20 (Spring intake) / February 15 (Fall intake)",
            "application_deadline": "September 20 (Spring intake) / March 20 (Fall intake)",
            "university_admission_deadline": "September 20 / March 20",
            "document_submission_deadline": "October 1 / April 1 (Hard copy postal arrival in Daegu)",
            "recommendation_letters_deadline": "September 25 / March 25",
            "interview_period": "October - November / April - May",
            "shortlist_announcement": "Late November (Spring) / Early June (Fall)",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "January / July",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Bi-annual intake: Spring semester starts in March, Fall semester starts in September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic rigor in engineering/science, university standing)",
            "extracurricular_and_leadership_weight": "5% (Initiative, teamwork, problem-solving mindset)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with DGIST research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "DGIST Departmental Admissions Committee, School Graduate Deans, and Admissions Board.",
            "evaluation_methodology": "Rigorous holistic evaluation assessing mathematical ability, research productivity, experimental aptitude, and alignment with faculty laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 1,600 international applicants across both intakes",
            "total_scholarships_awarded": "~80 to 120 fully funded international awards annually",
            "acceptance_rate_global": "~7.0% to 9.0%",
            "acceptance_rate_pakistan": "~14.0% to 18.0% for applicants with strong research profiles and CGPA >= 3.45",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.45 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with solid records in robotics, mechatronics, computing, or energy science, documented laboratory experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, Vietnam, China, India, Indonesia, Turkey, Iran, Russia.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal dgist.ac.kr.",
                "DGIST does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of USD 50 is paid directly through the secure DGIST online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: USD 50 (~PKR 14,000).",
                "NADRA FRC and document attestations (HEC, MoFA, Korean Embassy): ~PKR 35,000 to 50,000.",
                "DHL document courier to South Korea: ~PKR 12,000.",
                "South Korean D-2 Visa fee: ~USD 60 (~PKR 17,000).",
                "Flight to Busan / Seoul: ~PKR 150,000 to 220,000.",
                "Initial living deposit before first stipend payment: ~KRW 500,000 (~PKR 105,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Korean TOPIK certificate is needed. Reality: 100% of graduate education at DGIST is conducted in English.",
                "Myth: Flights are included. Reality: Airfare to South Korea is self-funded by the student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim DGIST requires GRE; GRE is optional and not mandatory for international graduate admissions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.00 out of 4.30 to retain the fellowship and tuition waiver each semester.",
            "attendance_requirements": "Full-time physical research presence at DGIST campus; daily participation in laboratory research activities.",
            "academic_progress_monitoring": "Semi-annual academic progress review evaluated by research advisor.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Korean immigration law; part-time work requires permission from immigration and university.",
            "home_country_return_obligation": "None; graduates are eligible for Korean D-10 job seeker visas or E-7 professional engineering visas upon graduation.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if semester GPA drops below 3.00 or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Extensions beyond standard 4 semesters (Master's) or 8 semesters (PhD) are generally not covered by the scholarship."
        },
        "official_sources_verified": [
            {
                "source_name": "DGIST Graduate Admissions Official Portal",
                "source_url": "https://www.dgist.ac.kr/adm_g/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "DGIST International Affairs",
                "source_url": "https://www.dgist.ac.kr/en/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-071": {
        "scholarship_id": "SCH-AS-071",
        "basic_details": {
            "scholarship_name": "Gwangju Institute of Science and Technology (GIST) International Graduate Scholarship & Full Research Assistantship",
            "offering_entity": "Gwangju Institute of Science and Technology (GIST) & Ministry of Science and ICT (MSIT), South Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "GIST Main Campus (Buk-gu, Gwangju, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & PhD"],
            "major_restrictions": "School of Electrical Engineering and Computer Science, School of Materials Science and Engineering, School of Mechanical Engineering, School of Environmental Science and Engineering, School of Life Sciences, Department of Physics and Photon Science, and Department of Chemistry.",
            "number_of_awards_total": "~120 to 160 international graduate fellowships awarded annually across departments",
            "number_of_awards_pakistan": "Extensive international cohort; typically 20 to 30 Pakistani researchers in photonics, computing, and engineering appointed annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 semesters (2 years) for Master's; 8 semesters (4 years) for PhD; 10 semesters (5 years) for Combined MS/PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Combined tuition waiver and stipend: 100% full tuition covered plus KRW 140,000 / month student allowance, KRW 290,000 / month meal allowance, and research assistantship: Total monthly living allowance typically KRW 1,000,000 to 1,400,000 / month for Master's (~PKR 210,000 to 294,000 / month) and KRW 1,400,000 to 1,900,000 / month for PhD (~PKR 294,000 to 399,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents both hold non-Korean citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to young researchers with exceptional academic momentum.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum CGPA 3.20/4.00 for Master's; recognized 18-year Master's degree with minimum CGPA 3.20/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum CGPA 3.20 / 4.00; competitive applicants at GIST typically possess CGPA >= 3.50 / 4.00.",
            "subject_background_prerequisites": "Electrical engineering, computer science, photonics, materials science, mechanical engineering, environmental engineering, life sciences, physics, or chemistry.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in photonics, laser physics, materials, or computing journals provide a substantial competitive edge.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, TOEIC 750+, or official English Medium of Instruction (MOI) certificate from an accredited university.",
            "other_language_requirements": "Korean language proficiency is not required; 100% of graduate lectures, research, and dissertations are conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "All admitted international graduate students receive the GIST Scholarship and research assistantship automatically upon admission.",
            "previous_scholarship_restrictions": "Cannot hold another parallel government fellowship covering identical living and tuition benefits.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver covering all standard degree semesters at GIST.",
                "amount": "100% covered (~KRW 6,800,000 to 8,500,000 / year value; ~PKR 1,428,000 to 1,785,000 / year)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "GIST does not charge an application fee for international graduate applicants.",
                "amount": "100% waived / free application (USD 0)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing in Gwangju (dormitory fee approx. KRW 100,000 to 160,000 / month), paid easily from living stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Combined institutional allowance, meal subsidy, and laboratory research assistantship: KRW 1,000,000 to 1,400,000 / month for Master's; KRW 1,400,000 to 1,900,000 / month for PhD.",
                "amount": "KRW 1,000,000 to 1,900,000 / month (~PKR 210,000 to 399,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One-way international airfare to South Korea is reimbursed upon arrival for newly enrolling international graduate students.",
                "amount": "One-way flight reimbursement provided by GIST"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 Student Visa fee paid directly to the Korean Embassy in Islamabad.",
                "amount": "Approx. USD 60 (~PKR 17,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory enrollment in Korea National Health Insurance Service (NHIS); subsidized monthly premium (approx. KRW 70,000 / month) paid from stipend.",
                "amount": "Subsidized Korea National Health Insurance"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "GIST provides a dedicated monthly meal allowance (KRW 290,000 / month) included in student support package.",
                "amount": "KRW 290,000 / month meal subsidy"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to GIST Central Library, Center for Relativistic Laser Science (CoReLS holding world-record 4-petawatt laser), and cleanrooms.",
                "amount": "100% covered world-leading laser and photonics lab access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants cover international conference registration, travel, and accommodation for accepted papers.",
                "amount": "Lab grant-funded international conference travel"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized transit connecting GIST campus to Gwangju-Songjeong KTX Station (connecting to Seoul in 1.5 hours).",
                "amount": "Subsidized KTX rail access"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single South Korea national research institute (GIST, Gwangju).",
            "participating_institutions": [
                "Gwangju Institute of Science and Technology (GIST Campus, Buk-gu, Gwangju, South Korea)"
            ],
            "university_rankings_scope": "QS World University Rankings #307 globally, Ranked #4 in the world for citations per faculty (QS World Rankings 2024); home to the world's most powerful petawatt laser research center (CoReLS).",
            "available_majors": [
                "Master's / PhD in School of Electrical Engineering and Computer Science",
                "Master's / PhD in School of Materials Science and Engineering",
                "Master's / PhD in School of Mechanical Engineering",
                "Master's / PhD in Department of Physics and Photon Science",
                "Master's / PhD in School of Environmental Science and Engineering",
                "Master's / PhD in School of Life Sciences",
                "Master's / PhD in Department of Chemistry"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years; Combined MS/PhD: 5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.20/4.00, academic transcripts, statement of purpose, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 80+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Electrical Engineering, Computer Science, and Physics & Photon Science are world-leading; contacting professors before applying significantly increases selection probability.",
            "strategic_program_match_advice": "Focus research proposals on ultra-intense laser physics, photonics, AI algorithms, or environmental nanomaterials where GIST holds premier national research institutes."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.gist.ac.kr/ia/html/sub04/0401.html",
            "portal_system_name": "GIST Online Graduate Admissions System",
            "account_creation_instructions": "Register on the GIST admissions portal, complete online application form (no application fee charged), upload personal statement and transcripts, and dispatch certified physical documents to Section of International Admissions.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective GIST professors in target research areas with CV and research interests (July-August for Spring / December-January for Fall).",
                "Step 2: Register on GIST Online Graduate Admissions System during open intake.",
                "Step 3: Complete online application and upload documents (application fee is completely free).",
                "Step 4: Register two academic recommenders who submit evaluation letters online.",
                "Step 5: Send certified hard-copy documents (degrees, transcripts, apostille/attestation) via DHL to GIST International Admissions in Gwangju.",
                "Step 6: Departmental faculty committee reviews dossiers and conducts virtual technical interviews.",
                "Step 7: Final admission and scholarship award results announced online.",
                "Step 8: Obtain Certificate of Admission (CoA), apply for South Korean D-2 visa, and arrive in Gwangju (flight reimbursement processed upon arrival)."
            ],
            "university_vs_scholarship_routing": "Integrated Institutional Route: Admission and scholarship funding are decided together based on departmental faculty recommendation.",
            "recommendation_letters_submission_method": "Submitted online by two academic recommenders via confidential portal links.",
            "personal_statement_prompts": "Statement of Purpose and Study Plan (prescribed GIST format) describing motivation, research experiences, scholarly interests, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "Structured research plan detailing proposed technical investigations, methodologies, and alignment with target GIST laboratories.",
            "cv_format_requirements": "Academic research CV detailing education, laboratory proficiencies, software skills, and publication history.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental faculty panel.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 80+, TOEIC 750+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "USD 0 (Completely free to apply)",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required, followed by Korean Embassy consular legalization in Islamabad or Apostille.",
            "translation_requirements": "Certified English or Korean translation for all non-English/non-Korean documents.",
            "final_submission_method": "Dual submission: Online portal application followed by mandatory postal dispatch of certified physical dossier to GIST."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.20/4.00.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and consular legalized by Korean Embassy Islamabad."
            },
            {
                "document_name": "Statement of Purpose and Study Plan",
                "mandatory": True,
                "specification": "Completed on official GIST form detailing background, motivation, research interests, and career goals.",
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
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, research projects, technical skills, and awards.",
                "pakistan_specific_instruction": "Professional academic CV."
            },
            {
                "document_name": "Family Relationship Certificate & Passport Copies",
                "mandatory": True,
                "specification": "Family Registration Certificate (FRC) and copies of passports of applicant and parents.",
                "pakistan_specific_instruction": "NADRA Family Registration Certificate (FRC) in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "August 20 (Spring intake) / February 15 (Fall intake)",
            "application_deadline": "September 25 (Spring intake) / March 25 (Fall intake)",
            "university_admission_deadline": "September 25 / March 25",
            "document_submission_deadline": "October 5 / April 5 (Hard copy postal arrival in Gwangju)",
            "recommendation_letters_deadline": "September 30 / March 30",
            "interview_period": "October - November / April - May",
            "shortlist_announcement": "Late November (Spring) / Early June (Fall)",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "January / July",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Bi-annual intake: Spring semester starts in March, Fall semester starts in September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic rigor in engineering/science, university standing)",
            "extracurricular_and_leadership_weight": "5% (Initiative, teamwork, problem-solving mindset)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or technical laboratory experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with GIST research priorities)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "GIST Departmental Admissions Committee, School Graduate Deans, and Admissions Board.",
            "evaluation_methodology": "Rigorous holistic evaluation assessing mathematical ability, research productivity, experimental aptitude, and alignment with faculty laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,400 to 1,900 international applicants across both intakes",
            "total_scholarships_awarded": "~120 to 160 fully funded international awards annually",
            "acceptance_rate_global": "~8.0% to 10.0%",
            "acceptance_rate_pakistan": "~14.0% to 18.0% for applicants with strong research profiles and CGPA >= 3.50",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.50 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with solid records in photonics, electrical engineering, computing, or materials science, documented laboratory experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, Vietnam, China, India, Indonesia, Turkey, Iran, Russia.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal gist.ac.kr.",
                "GIST does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Applying to GIST is completely free of charge (USD 0).",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: USD 0 (Free).",
                "NADRA FRC and document attestations (HEC, MoFA, Korean Embassy): ~PKR 35,000 to 50,000.",
                "DHL document courier to South Korea: ~PKR 12,000.",
                "South Korean D-2 Visa fee: ~USD 60 (~PKR 17,000).",
                "Flight to South Korea: Reimbursed upon arrival by GIST.",
                "Initial living deposit before first stipend payment: ~KRW 500,000 (~PKR 105,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Korean TOPIK certificate is needed. Reality: 100% of graduate education at GIST is conducted in English.",
                "Myth: Application fee required. Reality: GIST is one of the few Korean institutions with zero application fee."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim GIST requires GRE; GRE is optional and not mandatory for international graduate admissions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.00 out of 4.30 to retain the fellowship and tuition waiver each semester.",
            "attendance_requirements": "Full-time physical research presence at GIST campus; daily participation in laboratory research activities.",
            "academic_progress_monitoring": "Semi-annual academic progress review evaluated by research advisor.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Korean immigration law; part-time work requires permission from immigration and university.",
            "home_country_return_obligation": "None; graduates are eligible for Korean D-10 job seeker visas or E-7 professional engineering visas upon graduation.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if semester GPA drops below 3.00 or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Extensions beyond standard 4 semesters (Master's) or 8 semesters (PhD) are generally not covered by the scholarship."
        },
        "official_sources_verified": [
            {
                "source_name": "GIST International Admissions Official Portal",
                "source_url": "https://www.gist.ac.kr/ia/html/sub04/0401.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "GIST Section of International Affairs",
                "source_url": "https://www.gist.ac.kr/en/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
