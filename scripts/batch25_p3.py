"""Batch 25 Part 3: East Asia & Malaysia Postgraduate Awards (4 awards)
SCH-AS-056: Kyung Hee University (KHU) President's International Fellowship (South Korea)
SCH-AS-057: Universiti Malaysia Terengganu (UMT) Postgraduate Research Scholarship (Malaysia)
SCH-AS-058: Yenching Academy of Peking University Master's Fellowship in China Studies (China)
SCH-AS-059: Schwarzman Scholars Program at Tsinghua University (China)
"""

DATA_P3 = {
    "SCH-AS-056": {
        "scholarship_id": "SCH-AS-056",
        "basic_details": {
            "scholarship_name": "Kyung Hee University (KHU) President's International Graduate Fellowship & Full Tuition Award",
            "offering_entity": "Kyung Hee University (KHU) Graduate School & Office of International Affairs",
            "host_country": "South Korea",
            "host_institutions_covered": "Kyung Hee University (Seoul and Global Campuses, South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & PhD"],
            "major_restrictions": "College of Engineering, College of Electronics and Information, College of Software, College of Applied Sciences, Graduate School of Biotechnology, College of Life Sciences, and College of Pharmacy.",
            "number_of_awards_total": "~100 to 140 institutional graduate scholarships awarded per semester",
            "number_of_awards_pakistan": "Open internationally; typically 15 to 25 Pakistani STEM and informatics researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 semesters (2 years) for Master's; 6 to 8 semesters (3 to 4 years) for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "KRW 1,200,000 to 1,800,000 / month (~PKR 252,000 to 378,000 / month) provided via host professor's National Research Foundation (NRF) or BK21 Four research grant, combined with 100% full university tuition fee waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents both hold non-Korean citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to applicants under 35 years of age for graduate research positions.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum CGPA 3.20/4.00 for Master's; recognized 18-year Master's degree with minimum CGPA 3.20/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum CGPA 3.20 / 4.00; competitive candidates typically hold CGPA >= 3.50 / 4.00 with laboratory programming or experimental experience.",
            "subject_background_prerequisites": "Computer engineering, software engineering, artificial intelligence, electrical and electronic engineering, biotechnology, biomedical science, chemical engineering, or related fields.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree requirements before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in IEEE/ACM conferences or SCI/SCIE indexed journals provide a substantial competitive edge.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate; TOPIK Level 3+ accepted for Korean-taught majors.",
            "other_language_requirements": "Korean language proficiency is not required for English-track STEM laboratories.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure prior contact and an official Research Assistantship Commitment Letter from a Kyung Hee University professor with active BK21 Four grant funding.",
            "previous_scholarship_restrictions": "Cannot hold another full national or institutional fellowship covering identical living and tuition benefits.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver (Scholarship Type A - President's Award) covering entire standard semester duration at Kyung Hee University.",
                "amount": "100% covered (~KRW 10,000,000 to 14,000,000 / year value; ~PKR 2,100,000 to 2,940,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Online graduate application processing fee of KRW 100,000 paid via UwayApply / JinhakApply system.",
                "amount": "KRW 100,000 (~PKR 21,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing (Woojungwon or Sameuiwon dormitories) at subsidized rates (approx. KRW 250,000 to 380,000 / month), covered easily from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research stipend paid through supervisor's research grants (BK21 Four / NRF): KRW 1,200,000 to 1,500,000 / month for Master's; KRW 1,500,000 to 1,800,000 / month for PhD.",
                "amount": "KRW 1,200,000 to 1,800,000 / month (~PKR 252,000 to 378,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Seoul Incheon International Airport is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "South Korean D-2 Student Visa fee paid directly to the Korean Embassy in Islamabad or Gerry's Visa Drop Box.",
                "amount": "Approx. USD 60 (~PKR 17,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory enrollment in Korea National Health Insurance Service (NHIS); subsidized student monthly premium (approx. KRW 70,000 / month) paid from monthly stipend.",
                "amount": "Subsidized Korea National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Affordable on-campus cafeterias at Seoul and Global (Suwon) campuses; meals typically cost KRW 4,500 to 6,500.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Kyung Hee Central Library, high-performance computing clusters, clean rooms, and experimental testing facilities supported by research lab.",
                "amount": "100% covered laboratory and computational facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "International conference registration and travel allowances funded via host laboratory's BK21 Four or national research projects.",
                "amount": "Lab grant-funded international conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free shuttle buses between Kyung Hee Global Campus (Suwon) and Seoul Campus, plus nationwide T-Money transit system integration.",
                "amount": "Inter-campus shuttle & metropolitan transit access"
            },
            "total_estimated_value_usd_per_year": 21000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single prestigious Korean comprehensive private university (Kyung Hee University).",
            "participating_institutions": [
                "Kyung Hee University (Seoul Campus in Dongdaemun-gu and Global Campus in Yongin/Suwon, South Korea)"
            ],
            "university_rankings_scope": "QS World University Rankings #328, Top 40 in Asia; member of Korea's Brain Korea 21 (BK21 Four) initiative and renowned for software, biomedical engineering, and electronic systems.",
            "available_majors": [
                "Master's / PhD in Computer Science and Engineering",
                "Master's / PhD in Artificial Intelligence",
                "Master's / PhD in Electronic Engineering",
                "Master's / PhD in Software Convergence",
                "Master's / PhD in Biomedical Engineering",
                "Master's / PhD in Chemical Engineering",
                "Master's / PhD in Applied Chemistry and Materials Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years; Combined Master's/PhD: 4 to 5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.20/4.00, academic transcripts, study plan, professor recommendation letter, proof of English (IELTS 6.5+ / TOEFL 80+ / MOI), and supervisor commitment letter.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "High competition in AI, Computer Science, and Electronic Engineering; securing prior commitment from a laboratory PI ensures both admission and full funding.",
            "strategic_program_match_advice": "Review recent publications from Kyung Hee BK21 research groups, email faculty members with a tailored research statement highlighting programming and experimental skills."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://gskh.khu.ac.kr/ & https://www.uwayapply.com/",
            "portal_system_name": "Kyung Hee University Graduate School & UwayApply International Portal",
            "account_creation_instructions": "Contact prospective supervisor, secure RA financial support commitment, register on UwayApply, complete application form, upload digital documents, and pay KRW 100,000 fee.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective Kyung Hee professor in relevant STEM field with CV and research proposal (September for Spring / March for Fall).",
                "Step 2: Attend virtual technical interview and obtain Professor's Confirmation of Research Assistantship & Scholarship Recommendation.",
                "Step 3: Register on UwayApply during the official application window and submit admission dossier.",
                "Step 4: Send notarized hard-copy documents (degrees, transcripts, apostille/attestation) via DHL to KHU Graduate School Office.",
                "Step 5: Departmental admissions committee reviews documents and confirms scholarship category.",
                "Step 6: Receive official Admission Notice and Certificate of Admission (CoA).",
                "Step 7: Apply for South Korean D-2 Student Visa at Korean Embassy in Islamabad.",
                "Step 8: Arrive in South Korea in late February (Spring intake) or late August (Fall intake)."
            ],
            "university_vs_scholarship_routing": "Integrated departmental route: Tuition waiver and laboratory stipend are packaged directly upon faculty recommendation.",
            "recommendation_letters_submission_method": "Submitted via official letters of recommendation from prior academic professors along with the KHU professor's financial guarantee letter.",
            "personal_statement_prompts": "Study Plan and Personal Statement (prescribed KHU format) outlining motivation, academic achievements, research roadmap, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "Structured research statement detailing proposed laboratory experiments, computational models, and targeted journal deliverables.",
            "cv_format_requirements": "Standard academic research CV detailing educational history, laboratory proficiencies, software skills, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Online video interview via Zoom conducted by prospective research supervisor and laboratory senior researchers.",
            "standardized_tests": "IELTS 6.5+, TOEFL 80+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "KRW 100,000 (approx. USD 75 / ~PKR 21,000)",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required, followed by Korean Embassy consular legalization in Islamabad or Apostille.",
            "translation_requirements": "Certified English or Korean translation for all non-English/non-Korean documents.",
            "final_submission_method": "Online submission via UwayApply followed by mandatory postal dispatch of attested physical dossier to KHU Graduate School."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.20/4.00.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and consular legalized by Korean Embassy Islamabad."
            },
            {
                "document_name": "Study Plan and Personal Statement",
                "mandatory": True,
                "specification": "Completed on KHU official application forms detailing background, research interests, and career objectives.",
                "pakistan_specific_instruction": "Typed in English using official form."
            },
            {
                "document_name": "KHU Professor Recommendation / RA Commitment Letter",
                "mandatory": True,
                "specification": "Official letter from Kyung Hee University faculty advisor committing research lab funding and supervision.",
                "pakistan_specific_instruction": "Obtained directly from prospective KHU supervisor."
            },
            {
                "document_name": "Two Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential evaluation letters from previous university professors on institutional letterhead.",
                "pakistan_specific_instruction": "Signed and stamped with official university seals."
            },
            {
                "document_name": "English Language Proficiency Proof",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "MOI certificate or test report."
            },
            {
                "document_name": "Applicant and Parents' National Identity & Passport Documents",
                "mandatory": True,
                "specification": "Family Registration Certificate (FRC) and copies of valid international passports.",
                "pakistan_specific_instruction": "NADRA Family Registration Certificate (FRC) in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 15 (Spring intake) / March 15 (Fall intake)",
            "application_deadline": "October 20 (Spring intake) / April 20 (Fall intake)",
            "university_admission_deadline": "October 20 / April 20",
            "document_submission_deadline": "October 28 / April 28 (Hard copy postal arrival)",
            "recommendation_letters_deadline": "October 20 / April 20",
            "interview_period": "November / May",
            "shortlist_announcement": "December (Spring) / June (Fall)",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "January / July",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Bi-annual intake: Spring semester starts in March, Fall semester starts in September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic rigor in engineering/science coursework)",
            "extracurricular_and_leadership_weight": "5% (Adaptability, teamwork, extracurricular involvement)",
            "research_experience_weight": "40% (Technical research competence, prior publications, supervisor endorsement)",
            "work_experience_weight": "5% (Industry software or engineering experience)",
            "personal_statement_weight": "5% (Clarity of purpose and alignment with laboratory goals)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Departmental video interview performance)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research capability)",
            "selection_panel_composition": "Kyung Hee University Graduate School Admissions Committee, Departmental Faculty Board, and Host Laboratory PI.",
            "evaluation_methodology": "Two-stage evaluation: academic review and research potential assessment by laboratory PI followed by graduate school scholarship confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,000 international applicants across both intakes",
            "total_scholarships_awarded": "~100 to 140 full tuition & stipend awards annually",
            "acceptance_rate_global": "~7.0% to 9.0%",
            "acceptance_rate_pakistan": "~15.0% to 20.0% for candidates holding pre-secured supervisor RA commitments and CGPA >= 3.40",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.40 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "STEM graduates with solid foundations in engineering, mathematics, or computing, clear research focus, and supervisor sponsorship.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, COMSATS, UET Lahore, Quaid-i-Azam, GIKI).",
            "high_representation_countries": "Pakistan, Vietnam, China, India, Indonesia, Iran, Bangladesh, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply via official portals gskh.khu.ac.kr and uwayapply.com.",
                "Beware of private agents promising guaranteed Korean scholarships; university admission requires direct professor consent."
            ],
            "application_fee_warning": "Application fee of KRW 100,000 is paid directly through UwayApply online payment gateway.",
            "agent_and_intermediary_warnings": "Commercial agent materials are rejected; candidates must communicate directly with prospective Korean professors.",
            "hidden_costs_breakdown": [
                "Application fee: KRW 100,000 (~PKR 21,000).",
                "NADRA FRC and document attestations (HEC, MoFA, Korean Embassy): ~PKR 35,000 to 50,000.",
                "DHL document courier to South Korea: ~PKR 12,000.",
                "South Korean D-2 Visa fee: ~USD 60 (~PKR 17,000).",
                "Flight to Seoul Incheon: ~PKR 150,000 to 220,000.",
                "Initial living deposit before first stipend payment: ~KRW 500,000 (~PKR 105,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Korean TOPIK certificate is compulsory. Reality: All STEM graduate research is conducted entirely in English.",
                "Myth: Flight tickets are included. Reality: Travel to South Korea is self-funded by student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest scholarships are automatic without professor contact; without a professor's RA commitment, full funding is virtually impossible."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 3.50 out of 4.30 to retain the tuition waiver each semester.",
            "attendance_requirements": "Full-time physical laboratory research residency; daily participation in laboratory activities and research seminars.",
            "academic_progress_monitoring": "Semester evaluations conducted by academic advisor and submitted to Graduate School.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Korean immigration law; part-time work requires permission from immigration and university.",
            "home_country_return_obligation": "None; graduates are eligible for Korean D-10 job seeker visas or E-7 professional engineering visas upon completion.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if semester GPA drops below 3.50 or if student voluntarily withdraws without completing requirements.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and Graduate School dean.",
            "extension_policy": "Extensions beyond standard 4 semesters for Master's or 8 semesters for PhD are generally not funded by tuition waiver."
        },
        "official_sources_verified": [
            {
                "source_name": "Kyung Hee University Graduate School Admissions & Scholarships",
                "source_url": "https://gskh.khu.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Kyung Hee University Office of International Affairs",
                "source_url": "https://oia.khu.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-057": {
        "scholarship_id": "SCH-AS-057",
        "basic_details": {
            "scholarship_name": "Universiti Malaysia Terengganu (UMT) Postgraduate Research Scholarship & Graduate Research Assistantship (GRA)",
            "offering_entity": "Universiti Malaysia Terengganu (UMT) Graduate School & Research Management Centre",
            "host_country": "Malaysia",
            "host_institutions_covered": "Universiti Malaysia Terengganu (Kuala Nerus Campus, Terengganu, Malaysia)",
            "degree_levels": ["Master of Science (by Research)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Science and Marine Environment, Faculty of Fisheries and Food Science, Faculty of Ocean Engineering Technology and Informatics, and Institute of Oceanography and Environment (INOS).",
            "number_of_awards_total": "~80 to 120 graduate research scholarships and assistantships awarded annually",
            "number_of_awards_pakistan": "Open internationally; typically 10 to 18 Pakistani postgraduate researchers appointed annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 24 months for Master's by research; up to 36 months for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "RM 1,800 to RM 2,200 / month for PhD (~PKR 117,000 to 143,000 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month) plus full tuition fee waiver"
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
            "grading_conversion_notes": "Minimum CGPA 3.00 / 4.00; competitive applicants typically hold CGPA >= 3.30 / 4.00 with laboratory, field, or computing background.",
            "subject_background_prerequisites": "Marine science, ocean engineering, computer science, software engineering, environmental biotechnology, fisheries, aquatic sciences, or applied mathematics.",
            "current_education_status": "Graduated or final-semester students expecting degree completion before semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in marine, environmental, or computing journals or computational simulation experience advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.0, TOEFL iBT minimum 80, MUET Band 4.0, or recognized English Medium of Instruction (MOI) certificate.",
            "other_language_requirements": "None; Malay language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must secure endorsement from a UMT principal investigator holding active research grant funding (FRGS, TRGS, or international marine project grants).",
            "previous_scholarship_restrictions": "Cannot hold any concurrent national scholarship, industrial sponsorship, or full-time paid employment.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for eligible postgraduate research semesters covered under the UMT Graduate Research Scheme.",
                "amount": "100% covered (~RM 10,000 to 16,000 / year value; ~PKR 650,000 to 1,040,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "UMT international postgraduate application fee of RM 150 paid during online application submission.",
                "amount": "RM 150 (~PKR 9,800)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus or adjacent university-approved graduate residences available at subsidized monthly rates (approx. RM 200 to 350 / month), covered easily from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly research assistantship stipend: RM 1,800 to RM 2,200 / month for PhD (~PKR 117,000 to 143,000 / month); RM 1,300 to RM 1,600 / month for Master's (~PKR 84,500 to 104,000 / month).",
                "amount": "RM 1,300 to RM 2,200 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Kuala Lumpur / Terengganu is self-funded.",
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
                "details": "Campus cafeterias provide affordable dining; daily meals cost approximately RM 15 to 25.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to UMT Sultanah Nur Zahirah Library, research vessels (RV Discovery), marine hatcheries, and advanced instrumentation laboratories.",
                "amount": "100% covered marine research infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference participation and publication charges (APC) for high-impact Scopus/WoS indexed journals covered by host supervisor grant.",
                "amount": "Grant-funded conference travel and APC charges"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle transportation between residential colleges and academic faculties in Kuala Nerus.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 11500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Malaysian premier maritime and aquatic focused university (Universiti Malaysia Terengganu).",
            "participating_institutions": [
                "Universiti Malaysia Terengganu (Kuala Nerus Campus, Terengganu, Malaysia)"
            ],
            "university_rankings_scope": "QS Asia University Rankings Top 200; globally recognized as Malaysia's focal institution for Marine Science, Oceanography, and Coastal Engineering.",
            "available_majors": [
                "Master of Science / PhD in Marine Science",
                "Master of Science / PhD in Ocean Engineering Technology",
                "Master of Science / PhD in Computer Science (Marine Informatics)",
                "Master of Science / PhD in Fisheries Science",
                "Master of Science / PhD in Environmental Biotechnology",
                "Master of Science / PhD in Applied Mathematics and Modeling",
                "Master of Science / PhD in Chemical Ecology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's by Research: 1.5 to 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA 3.00+, academic transcripts, research proposal, supervisor endorsement form, two reference letters, and IELTS 6.0 / TOEFL 80 or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Institute of Oceanography and Environment (INOS) and Faculty of Science & Marine Environment are premier centers; establishing prior supervisor connection is essential.",
            "strategic_program_match_advice": "Focus research proposals on marine biodiversity, blue carbon ecosystems, coastal climate modeling, or marine big data analytics where UMT holds significant government funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://gso.umt.edu.my/ & https://e-admission.umt.edu.my/",
            "portal_system_name": "UMT Graduate School Online Application Portal",
            "account_creation_instructions": "Contact prospective supervisor, obtain acceptance form, register on UMT e-admission portal, submit postgraduate application, upload credentials, and pay RM 150 fee.",
            "step_by_step_workflow": [
                "Step 1: Explore UMT faculty expertise directory and email prospective supervisors with CV and research draft.",
                "Step 2: Secure signed Supervisor Acceptance & Research Assistantship Recommendation Form.",
                "Step 3: Register on UMT e-admission portal and complete online postgraduate application.",
                "Step 4: Upload attested academic transcripts, research proposal, passport copy, and English proof.",
                "Step 5: Faculty Graduate Committee reviews technical proposal and conducts online interview.",
                "Step 6: UMT Graduate School issues official Letter of Offer and Scholarship Award Letter.",
                "Step 7: Apply for EMGS Visa Approval Letter (VAL) and Single Entry Visa at Malaysian High Commission in Islamabad.",
                "Step 8: Travel to Terengganu, complete on-campus medical checkup, and matriculate."
            ],
            "university_vs_scholarship_routing": "Integrated departmental route: Application for admission and scholarship are reviewed together upon faculty recommendation.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed PDF recommendation letters on official university letterheads.",
            "personal_statement_prompts": "Statement of research intent detailing technical competencies, research goals, and synergy with host supervisor's funded research project.",
            "study_plan_research_proposal_requirements": "5 to 8 page structured research proposal covering problem statement, literature review, methodology, equipment needs, and milestone schedule.",
            "cv_format_requirements": "Academic CV detailing qualifications, field/laboratory experience, software proficiencies, and publications list.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Google Meet or MS Teams conducted by prospective supervisor and departmental postgraduate coordinator.",
            "standardized_tests": "IELTS 6.0+, TOEFL 80+, MUET Band 4.0, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "RM 150 (approx. USD 35 / ~PKR 9,800)",
            "attestation_requirements": "Notarized copies of degrees and transcripts; HEC and MoFA attestations required for Pakistani credentials during EMGS processing.",
            "translation_requirements": "Certified English translations for all non-English documents.",
            "final_submission_method": "Online submission via UMT e-admission postgraduate application portal."
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
                "specification": "Official UMT form signed by prospective supervisor confirming laboratory placement and willingness to supervise.",
                "pakistan_specific_instruction": "Obtained directly from UMT faculty supervisor."
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
            "academic_weight": "35% (Prior CGPA, academic performance, and foundational coursework)",
            "extracurricular_and_leadership_weight": "5% (Teamwork, communication, and environmental leadership)",
            "research_experience_weight": "35% (Prior publications, technical proposal rigor, and supervisor grant synergy)",
            "work_experience_weight": "5% (Laboratory technical or field research experience)",
            "personal_statement_weight": "5% (Clarity of purpose and dedication to marine/STEM research)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit and research capability based)",
            "selection_panel_composition": "Faculty Postgraduate Committee, Dean of Graduate School, and Principal Investigator of host research project.",
            "evaluation_methodology": "Two-stage evaluation: departmental technical vetting of research alignment followed by central Graduate School award confirmation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,000 applicants across both semesters",
            "total_scholarships_awarded": "~80 to 120 awards annually",
            "acceptance_rate_global": "~12% to 14%",
            "acceptance_rate_pakistan": "~16% to 20% for applicants with pre-secured supervisor endorsement and CGPA >= 3.25",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.25 / 4.00, coupled with prior lab project experience or publications",
            "typical_academic_and_research_profile": "Graduates in marine science, biotechnology, computer science, or engineering with clear research plan and supervisor endorsement.",
            "common_backgrounds_of_winners": "Graduates from Pakistani institutions (NUST, Karachi University, COMSATS, UET, Bahria University, Lasbela University).",
            "high_representation_countries": "Malaysia, Pakistan, Indonesia, Nigeria, Yemen, Bangladesh, Egypt.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal gso.umt.edu.my.",
                "Do not pay money to educational agents promising guaranteed assistantships; awards depend entirely on faculty supervisor endorsement."
            ],
            "application_fee_warning": "University application fee is RM 150 paid directly to UMT via secure online payment.",
            "agent_and_intermediary_warnings": "Commercial agent proposals are flagged and rejected; applicants must write their own technical research proposal.",
            "hidden_costs_breakdown": [
                "UMT application fee: RM 150 (~PKR 9,800).",
                "EMGS visa approval and student pass fees: ~RM 2,200 to 2,500 (~PKR 143,000 to 162,500).",
                "HEC and MoFA document attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "One-way flight to Kuala Lumpur / Terengganu: ~PKR 95,000 to 140,000.",
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
            "attendance_requirements": "Full-time physical research presence at UMT Kuala Nerus campus; scholars may be assigned up to 6 hours/week of laboratory or tutorial teaching assistance.",
            "academic_progress_monitoring": "Semi-annual progress report evaluated by supervisor and presented to Faculty Postgraduate Committee.",
            "work_restrictions_during_study": "Recipients are barred from taking full-time outside employment; internal paid tutoring or research assistance is permitted within university limits.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdoc opportunities, or industrial employment in Malaysia or abroad upon graduation.",
            "service_obligations_or_bonds": "Zero national service bond; recipients must meet graduation publication requirements (minimum 1-2 Scopus/WoS indexed papers) affiliated with UMT.",
            "repayment_clawback_conditions": "Termination of monthly stipend and withdrawal of fee waiver if research progress is evaluated as Unsatisfactory across consecutive reviews.",
            "rules_for_changing_university": "Non-transferable; scheme is funded internally by UMT.",
            "rules_for_changing_major": "Field of research cannot be changed without written permission from faculty dean and Graduate School.",
            "extension_policy": "Extensions beyond maximum tenure (24 months Master's, 36 months PhD) require special approval and are generally self-funded."
        },
        "official_sources_verified": [
            {
                "source_name": "Universiti Malaysia Terengganu Graduate School Office",
                "source_url": "https://gso.umt.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Universiti Malaysia Terengganu Official Portal",
                "source_url": "https://www.umt.edu.my/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-058": {
        "scholarship_id": "SCH-AS-058",
        "basic_details": {
            "scholarship_name": "Yenching Academy of Peking University Master's Fellowship in China Studies",
            "offering_entity": "Yenching Academy of Peking University (PKU)",
            "host_country": "China",
            "host_institutions_covered": "Peking University (Haidian Campus, Beijing, China)",
            "degree_levels": ["Master of Arts (in China Studies)"],
            "major_restrictions": "Interdisciplinary China Studies with concentrations in: Economics and Management, History and Archaeology, Philosophy and Religion, Politics and International Relations, Law and Society, or Literature and Culture.",
            "number_of_awards_total": "~115 to 125 Yenching Scholars selected annually from over 40 countries",
            "number_of_awards_pakistan": "Extremely competitive global cohort; typically 1 to 3 outstanding Pakistani scholars selected per annual intake",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "1 to 2 years (Full residential scholarship for Year 1; thesis writing & living stipend for Year 2 in Beijing)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "CNY 3,500 to 5,000 / month living stipend (~PKR 136,500 to 195,000 / month), plus 100% full tuition waiver, single-room accommodation in Yenching Academy House, round-trip international airfare, and comprehensive medical insurance"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international applicants, PRC citizens, and Hong Kong/Macau/Taiwan applicants (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 28,
            "age_limit_notes": "Preference is given to candidates 25 years old or younger on August 31 of enrollment year; maximum age rarely exceeds 28.",
            "academic_qualifications": "Minimum of a recognized Bachelor's degree in any discipline with outstanding academic achievement (typically top 5% class standing or CGPA >= 3.70/4.00) from an accredited university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum CGPA 3.50 / 4.00 to apply; selected scholars average CGPA >= 3.80 / 4.00 or First Class Honours.",
            "subject_background_prerequisites": "Open to all academic backgrounds (humanities, social sciences, natural sciences, engineering, law, economics, and business).",
            "current_education_status": "Graduated or final-year undergraduate students graduating by August 31 of enrollment year.",
            "graduation_year_restrictions": "None, though candidates are typically recent university graduates or young professionals.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Demonstrated leadership record, extracurricular engagement, public service, and global outlook are critical evaluation pillars.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 7.0 (overall), TOEFL iBT minimum 100, Cambridge C1/C2, or native/medium of instruction (if undergraduate degree was conducted entirely in English).",
            "other_language_requirements": "Chinese proficiency is NOT required for admission, but Chinese language courses are a mandatory component of the Yenching curriculum.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates from Partner Universities must be nominated by their institution's fellowship office; candidates from non-Partner universities apply via direct Open Application.",
            "previous_scholarship_restrictions": "Cannot hold concurrent external funding covering identical costs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for the complete Master of Arts in China Studies degree at Peking University.",
                "amount": "100% covered (~CNY 180,000 value; ~PKR 7,020,000)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "No application fee charged to candidates applying to Yenching Academy.",
                "amount": "100% waived / free application"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free single-room accommodation provided at Yenching Academy House on the Peking University main campus in Haidian, Beijing.",
                "amount": "100% covered private room accommodation"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Generous monthly living allowance of CNY 3,500 to 5,000 / month (~PKR 136,500 to 195,000 / month) disbursed directly to scholar's bank account.",
                "amount": "CNY 3,500 to 5,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One round-trip economy class international flight ticket between home country and Beijing provided by the fellowship.",
                "amount": "100% covered round-trip international flight"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 Student Visa application fees paid directly to Chinese Visa Application Service Center in Pakistan.",
                "amount": "Approx. PKR 18,000 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Medical Insurance for Foreign Students in China 100% covered by Yenching Academy.",
                "amount": "100% covered comprehensive healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Peking University student cafeterias provide affordable dining; monthly stipend more than covers all living and meal expenses.",
                "amount": "Covered via monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Peking University Library (one of Asia's largest academic libraries), Yenching Academy reading rooms, and research databases.",
                "amount": "100% covered academic resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Fellowship provides dedicated research field study funding, including fully funded academic study trips across China.",
                "amount": "100% funded China field study trips & thesis grants"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized Beijing public transit smart card (Yikatong) with student discounts.",
                "amount": "Subsidized metropolitan transit"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single China #1 elite C9 institution (Peking University, Beijing).",
            "participating_institutions": [
                "Yenching Academy of Peking University (Haidian District, Beijing, China)"
            ],
            "university_rankings_scope": "QS World University Rankings #14 globally, #1 in Mainland China; Peking University is China's oldest national university and premier humanities & social sciences powerhouse.",
            "available_majors": [
                "Master of Arts in China Studies (Economics & Management)",
                "Master of Arts in China Studies (History & Archaeology)",
                "Master of Arts in China Studies (Philosophy & Religion)",
                "Master of Arts in China Studies (Politics & International Relations)",
                "Master of Arts in China Studies (Law & Society)",
                "Master of Arts in China Studies (Literature & Culture)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (Year 1 residential in Beijing; Year 2 thesis completion)",
            "admission_requirements_summary": "Bachelor's degree with top 5-10% standing (CGPA 3.7+), academic transcripts, two letters of recommendation from professors, statement of purpose, research proposal, CV, and English proficiency certificate (IELTS 7.0+ / TOEFL 100+).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Extremely competitive global fellowship on par with Rhodes, Schwarzman, and Gates Cambridge; requires compelling personal narrative, proven intellectual curiosity, and cross-cultural leadership.",
            "strategic_program_match_advice": "Develop a research proposal that clearly links your primary undergraduate field (e.g. economics, public policy, or computer technology) to contemporary or historical China."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://yenchingacademy.pku.edu.cn/",
            "portal_system_name": "Yenching Academy Online Application Portal",
            "account_creation_instructions": "Register on the Yenching Academy admissions portal, choose your research concentration, upload personal statement, research proposal, transcripts, and register academic referees.",
            "step_by_step_workflow": [
                "Step 1: Check whether your home university is a Yenching Partner Institution (if yes, seek internal nomination; if no, apply via Open Application).",
                "Step 2: Draft personal statement (maximum 750 words) and China-focused research proposal (maximum 1,500 words).",
                "Step 3: Secure two academic letters of recommendation from professors who know your work intimately.",
                "Step 4: Submit complete online application before the strict early-December deadline.",
                "Step 5: International Admissions Committee conducts preliminary dossier screening.",
                "Step 6: Shortlisted candidates invited for a 25-30 minute virtual panel interview in January/February.",
                "Step 7: Final offer notifications sent out in late March / early April.",
                "Step 8: Complete Peking University international student enrollment, obtain JW202/visa, and arrive in Beijing in late August."
            ],
            "university_vs_scholarship_routing": "Integrated global fellowship program: Admission to Peking University and the Yenching Fellowship are awarded together as a single package.",
            "recommendation_letters_submission_method": "Submitted electronically by referees via confidential links sent from the Yenching portal.",
            "personal_statement_prompts": "Personal statement (maximum 750 words) outlining background, life experiences, leadership journey, and why you wish to join the Yenching Academy community.",
            "study_plan_research_proposal_requirements": "Research proposal (maximum 1,500 words excluding bibliography) detailing a proposed China-focused academic inquiry within your chosen research track.",
            "cv_format_requirements": "Professional 1 to 2 page CV detailing academic background, leadership roles, publications, honors, and language skills.",
            "interviews_conducted": True,
            "interview_format_details": "Highly rigorous 25 to 30 minute video interview conducted by a multidisciplinary panel of Peking University professors and international scholars.",
            "standardized_tests": "IELTS 7.0+, TOEFL 100+, or official proof of English-medium undergraduate instruction accepted.",
            "application_fee_amount": "CNY 0 (No application fee)",
            "attestation_requirements": "Certified transcripts and degree certificates; HEC and MoFA attestations required upon formal matriculation.",
            "translation_requirements": "Official certified English translation for all non-English academic documents.",
            "final_submission_method": "Online submission via Yenching Academy admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificate",
                "mandatory": True,
                "specification": "Complete university transcripts showing course grades, grading scale, and degree conferral.",
                "pakistan_specific_instruction": "Certified true copies with HEC attestation recommended."
            },
            {
                "document_name": "Personal Statement (Max 750 Words)",
                "mandatory": True,
                "specification": "Reflective narrative addressing intellectual path, leadership, and reasons for joining Yenching Academy.",
                "pakistan_specific_instruction": "Structured essay formatted in English."
            },
            {
                "document_name": "China Studies Research Proposal (Max 1,500 Words)",
                "mandatory": True,
                "specification": "Original academic research proposal demonstrating critical inquiry and scholarly rigor in China Studies.",
                "pakistan_specific_instruction": "Scholarly proposal with proper citations."
            },
            {
                "document_name": "Two Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential evaluation letters from university professors or academic instructors submitted directly online.",
                "pakistan_specific_instruction": "On institutional letterhead."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "1-2 page comprehensive resume highlighting education, leadership, honors, and activities.",
                "pakistan_specific_instruction": "Professional academic CV."
            },
            {
                "document_name": "Certificate of English Language Proficiency",
                "mandatory": True,
                "specification": "IELTS Academic 7.0+, TOEFL iBT 100+, or official English Medium of Instruction proof.",
                "pakistan_specific_instruction": "Official test score report or MOI letter."
            },
            {
                "document_name": "International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid beyond August 2026.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "August 15",
            "application_deadline": "December 1 (Strict annual deadline for international applicants)",
            "university_admission_deadline": "December 1",
            "document_submission_deadline": "December 1",
            "recommendation_letters_deadline": "December 10",
            "interview_period": "January - February",
            "shortlist_announcement": "Mid March - Early April",
            "final_result_acceptance_deadline": "Late April",
            "visa_application_window": "June - July",
            "semester_commencement": "Late August (Fall intake)",
            "annual_cycle_notes": "Single annual admission cycle for autumn entry; application window runs August to early December."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Undergraduate GPA, academic honors, intellectual depth)",
            "extracurricular_and_leadership_weight": "25% (Demonstrated leadership track record, community service, global engagement)",
            "research_experience_weight": "20% (Originality, methodology, and scholarly strength of China research proposal)",
            "work_experience_weight": "5% (Internships, professional trajectory, or relevant initiatives)",
            "personal_statement_weight": "10% (Authenticity, self-reflection, and vision articulated in personal statement)",
            "recommendations_weight": "5% (Depth of professor evaluation and intellectual character endorsements)",
            "interview_weight": "5% (Poise, critical thinking, and intellectual agility during panel interview)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind merit evaluation)",
            "selection_panel_composition": "Yenching Academy Executive Admissions Board, Peking University faculty deans, and distinguished international scholars.",
            "evaluation_methodology": "Holistic review assessing intellectual capability, leadership potential, cross-cultural empathy, and research feasibility."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 4,500 global applicants from over 100 countries",
            "total_scholarships_awarded": "~115 to 125 Yenching Scholars selected annually",
            "acceptance_rate_global": "~2.8% to 3.5%",
            "acceptance_rate_pakistan": "~2.0% to 3.0% (elite nationwide competition)",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.80 / 4.00, combined with prominent leadership and cross-cultural initiatives",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, proven leadership, intellectual maturity, and a compelling research vision connecting their background with China.",
            "common_backgrounds_of_winners": "Graduates from premier institutions worldwide (Harvard, Oxford, PKU, Cambridge, Princeton, NUS) and top Pakistani universities (LUMS, NUST, Quaid-i-Azam).",
            "high_representation_countries": "United States, China, United Kingdom, Pakistan, Germany, India, Singapore, Canada, Australia.",
            "competitiveness_tier": "MOST_COMPETITIVE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply directly through yenchingacademy.pku.edu.cn.",
                "Yenching Academy never charges application fees or endorses educational consultants; beware of fraudulent commercial agents."
            ],
            "application_fee_warning": "Applying to Yenching Academy is 100% free of charge.",
            "agent_and_intermediary_warnings": "Commercial agency written essays or research proposals are immediately detected and permanently blacklisted.",
            "hidden_costs_breakdown": [
                "Application fee: CNY 0 (Free).",
                "Chinese X1 Visa fee in Pakistan: ~PKR 18,000.",
                "Medical checkup & attestation costs: ~PKR 25,000 to 35,000.",
                "Personal incidentals before first stipend disbursement: ~CNY 2,000 (~PKR 78,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must major in Chinese or East Asian studies. Reality: Candidates from all fields including STEM, law, and economics are enthusiastically welcomed.",
                "Myth: Prior Chinese language fluency is required. Reality: Chinese proficiency is not required for admission."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums suggest second-year students must self-fund; in reality, students maintaining good academic standing receive full Year 2 tuition waiver and stipend."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain good academic standing in coursework (minimum grade B or equivalent) throughout Year 1 and Year 2.",
            "attendance_requirements": "Full-time residential attendance in Beijing during Year 1; participation in academic seminars, field trips, and Yenching Global Symposium.",
            "academic_progress_monitoring": "Term-by-term evaluation of coursework credits, China field study completion, and master's thesis milestones.",
            "work_restrictions_during_study": "Scholars are expected to devote full time to their studies; part-time internships require formal prior approval.",
            "home_country_return_obligation": "None; scholars are free to pursue international doctorates, join multilateral organizations, or work globally.",
            "service_obligations_or_bonds": "Zero service bond or financial repayment obligation.",
            "repayment_clawback_conditions": "Fellowship is revoked if a scholar is expelled for academic dishonesty, plagiarism, code of conduct violations, or criminal acts.",
            "rules_for_changing_university": "Non-transferable; exclusive to Peking University.",
            "rules_for_changing_major": "Scholars select one of the six approved China Studies research tracks and must adhere to faculty guidelines.",
            "extension_policy": "Degree must be completed within the standard 2-year tenure."
        },
        "official_sources_verified": [
            {
                "source_name": "Yenching Academy of Peking University Official Admissions Portal",
                "source_url": "https://yenchingacademy.pku.edu.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Peking University International Students Division",
                "source_url": "https://www.isd.pku.edu.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-059": {
        "scholarship_id": "SCH-AS-059",
        "basic_details": {
            "scholarship_name": "Schwarzman Scholars Program at Tsinghua University",
            "offering_entity": "Schwarzman Scholars & Tsinghua University",
            "host_country": "China",
            "host_institutions_covered": "Schwarzman College, Tsinghua University (Haidian District, Beijing, China)",
            "degree_levels": ["Master of Management Science (in Global Affairs)"],
            "major_restrictions": "Master's degree in Global Affairs focusing on one of three core concentrations: Public Policy, Economics and Business, or International Studies.",
            "number_of_awards_total": "~140 to 150 Schwarzman Scholars selected annually from over 40 countries and 100+ universities",
            "number_of_awards_pakistan": "Highly competitive global allocation; typically 1 to 2 exceptional Pakistani leaders selected per cohort",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "1 year (Intensive 11-month fully residential program at Schwarzman College)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "USD 4,000 personal stipend (~PKR 1,120,000) for the year, plus 100% full tuition, private room and board at Schwarzman College, round-trip international travel, study tours, health insurance, and required books and supplies"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to applicants of all nationalities and citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 28,
            "age_limit_notes": "Applicants must be at least 18 but not yet 29 years of age as of August 1 of their matriculation year.",
            "academic_qualifications": "Completed undergraduate degree (Bachelor's degree or equivalent) in any field from an accredited college or university prior to August of matriculation year.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "No minimum GPA is officially mandated; however, selected scholars demonstrate superior academic records (typically CGPA >= 3.70 / 4.00 or top 10% class rank).",
            "subject_background_prerequisites": "Open to any undergraduate discipline: STEM, business, social sciences, humanities, law, arts, or public health.",
            "current_education_status": "Graduated or currently enrolled undergraduate seniors graduating before August 1 of the enrollment year.",
            "graduation_year_restrictions": "None, provided age criteria (under 29 years old) is satisfied.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience is not required, but proven leadership track record and impact in your field, organization, or community is mandatory.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 7.0, TOEFL iBT minimum 100, or official certification that applicant completed undergraduate degree where English was primary instructional language.",
            "other_language_requirements": "Mandarin Chinese language proficiency is NOT required for admission.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates submit application through the Schwarzman Scholars international application system (or China application system for Chinese passport holders).",
            "previous_scholarship_restrictions": "Cannot hold another concurrent fellowship requiring parallel residency or study.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for the Master of Management Science in Global Affairs at Tsinghua University.",
                "amount": "100% covered (~USD 55,000 value; ~PKR 15,400,000)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Applying to Schwarzman Scholars is completely free of charge.",
                "amount": "100% waived / free application"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Private room with en-suite bathroom at Schwarzman College, a state-of-the-art residential college designed by Robert A.M. Stern Architects on Tsinghua campus.",
                "amount": "100% covered private room and board"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Personal living allowance of USD 4,000 disbursed across the academic year for personal expenses and incidentals.",
                "amount": "USD 4,000 personal stipend (~PKR 1,120,000/year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international travel to and from Beijing at the beginning and end of the program.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Chinese X1 Student Visa application fees reimbursed or covered as part of scholar onboarding package.",
                "amount": "100% covered / reimbursed"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive global medical and travel insurance plan provided for the duration of the program.",
                "amount": "100% covered comprehensive healthcare"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "All meals provided through Schwarzman College dining hall and campus meal allowance cards.",
                "amount": "100% covered room and board dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "All required textbooks, academic software licenses, course materials, and Lenovo laptop provided to each scholar.",
                "amount": "100% covered books, tech & course materials"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "All domestic and international study tours, deep-dive field expeditions across China, and practical training internships fully covered.",
                "amount": "100% funded country-wide study tours"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "All program-related transportation within Beijing and across China for official excursions and field immersions fully funded.",
                "amount": "100% covered excursion transit"
            },
            "total_estimated_value_usd_per_year": 85000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single China #1 elite STEM and global leadership institution (Tsinghua University, Beijing).",
            "participating_institutions": [
                "Schwarzman College, Tsinghua University (Haidian District, Beijing, China)"
            ],
            "university_rankings_scope": "QS World University Rankings #20 globally, #1 in Asia for Engineering & Technology; Schwarzman College is modeled on the Rhodes Scholarship at Oxford.",
            "available_majors": [
                "Master of Management Science in Global Affairs (Public Policy)",
                "Master of Management Science in Global Affairs (Economics & Business)",
                "Master of Management Science in Global Affairs (International Studies)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 year (11-month intensive residential master's)",
            "admission_requirements_summary": "Undergraduate degree with superior academic achievement, three letters of recommendation, leadership essay, statement of purpose, short video introduction, CV, and English proficiency test (IELTS 7.0+ / TOEFL 100+).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Among the most selective postgraduate leadership scholarships globally (<4% acceptance); candidates must prove exceptional leadership impact, vision, and character.",
            "strategic_program_match_advice": "Focus leadership essay on a concrete instance where you took initiative, overcame adversity, and created tangible positive change in an organization, community, or startup."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.schwarzmanscholars.org/",
            "portal_system_name": "Schwarzman Scholars Online Application Portal",
            "account_creation_instructions": "Register on the official portal, select international applicant track, upload transcripts, essays, CV, 1-minute video introduction, and register three recommenders.",
            "step_by_step_workflow": [
                "Step 1: Open online application on schwarzmanscholars.org (April).",
                "Step 2: Draft Leadership Essay (maximum 750 words) and Statement of Purpose (maximum 500 words).",
                "Step 3: Secure three letters of recommendation (at least one must attest specifically to leadership ability).",
                "Step 4: Record and upload 1-minute video introducing yourself to the selection committee.",
                "Step 5: Submit application by the strict mid-September deadline.",
                "Step 6: Semifinalists invited in October to participate in in-person or virtual interview panels with distinguished global leaders.",
                "Step 7: Final scholarship offers announced in early December.",
                "Step 8: Matriculate at Schwarzman College in Beijing in late August for the 11-month academic year."
            ],
            "university_vs_scholarship_routing": "Integrated global leadership program: Admission to Tsinghua University and the Schwarzman Fellowship are evaluated as a unified award.",
            "recommendation_letters_submission_method": "Submitted online by three recommenders via confidential portal links (at least one addressing leadership track record directly).",
            "personal_statement_prompts": "Statement of Purpose (max 500 words) defining how the Schwarzman curriculum and China immersion fit your career trajectory; and Leadership Essay (max 750 words) providing concrete evidence of your leadership.",
            "study_plan_research_proposal_requirements": "Short-answer questions focusing on current affairs, global challenges, and how understanding China will advance your long-term leadership impact.",
            "cv_format_requirements": "Maximum 2-page professional resume detailing education, leadership positions, professional experience, honors, and community impact.",
            "interviews_conducted": True,
            "interview_format_details": "Highly intensive 25-minute interview before a distinguished panel of global CEOs, ambassadors, university presidents, and non-profit leaders.",
            "standardized_tests": "IELTS 7.0+, TOEFL 100+, or official proof of English-medium undergraduate education accepted.",
            "application_fee_amount": "USD 0 (Completely free to apply)",
            "attestation_requirements": "Certified transcripts and degree certificates; HEC and MoFA attestations required upon formal Tsinghua matriculation.",
            "translation_requirements": "Certified English translation for all non-English academic credentials.",
            "final_submission_method": "Online submission via Schwarzman Scholars international application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete transcripts from all undergraduate and graduate institutions attended.",
                "pakistan_specific_instruction": "Certified true copies with HEC attestation recommended."
            },
            {
                "document_name": "Leadership Essay (Max 750 Words)",
                "mandatory": True,
                "specification": "Detailed essay illustrating a specific leadership example, challenges overcome, and outcomes achieved.",
                "pakistan_specific_instruction": "Original personal narrative."
            },
            {
                "document_name": "Statement of Purpose (Max 500 Words)",
                "mandatory": True,
                "specification": "Concise statement describing professional goals, how Schwarzman Scholars fits your journey, and your perspective on China.",
                "pakistan_specific_instruction": "Clearly articulated goals essay."
            },
            {
                "document_name": "Three Letters of Recommendation",
                "mandatory": True,
                "specification": "Three confidential letters (academic, professional, and at least one focusing explicitly on leadership qualities).",
                "pakistan_specific_instruction": "Submitted directly by recommenders online."
            },
            {
                "document_name": "One-Minute Video Introduction",
                "mandatory": True,
                "specification": "1-minute recorded video introducing your personality, values, and passions to the admissions committee.",
                "pakistan_specific_instruction": "Clear audio and video presentation in English."
            },
            {
                "document_name": "Resume / Curriculum Vitae",
                "mandatory": True,
                "specification": "Maximum 2-page resume emphasizing leadership accomplishments, professional experience, and academic record.",
                "pakistan_specific_instruction": "Standard professional format."
            },
            {
                "document_name": "English Language Proficiency Proof",
                "mandatory": True,
                "specification": "IELTS Academic 7.0+, TOEFL iBT 100+, or official English-medium degree verification.",
                "pakistan_specific_instruction": "Score report or institutional letter."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "April 15",
            "application_deadline": "September 12 (Strict global international deadline)",
            "university_admission_deadline": "September 12",
            "document_submission_deadline": "September 12",
            "recommendation_letters_deadline": "September 15",
            "interview_period": "Late October - Mid November (Singapore, London, New York, or virtual)",
            "shortlist_announcement": "Early December",
            "final_result_acceptance_deadline": "Late December",
            "visa_application_window": "May - June",
            "semester_commencement": "Late August (Fall intake)",
            "annual_cycle_notes": "Single annual admission cycle; application opens in April and closes in mid-September for matriculation the following August."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Intellectual ability, academic record, and analytical reasoning)",
            "extracurricular_and_leadership_weight": "40% (Leadership track record, initiative, integrity, and demonstrated impact)",
            "research_experience_weight": "5% (Analytical competence and global awareness)",
            "work_experience_weight": "10% (Professional trajectory, initiatives led, and maturity)",
            "personal_statement_weight": "10% (Clarity of vision, character, and alignment with China immersion)",
            "recommendations_weight": "5% (Depth of leadership and character testimonials)",
            "interview_weight": "5% (Composure, eloquence, and intellectual agility before global panel)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Purely merit and leadership potential based)",
            "selection_panel_composition": "Schwarzman Admissions Board comprising former world leaders, CEOs, university deans, and global fellowship trustees.",
            "evaluation_methodology": "Rigorous holistic assessment identifying future global leaders with superior intellect, character, leadership presence, and intercultural curiosity."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 to 5,000 applicants from over 120 countries",
            "total_scholarships_awarded": "~140 to 150 Schwarzman Scholars selected annually",
            "acceptance_rate_global": "~3.0% to 3.5%",
            "acceptance_rate_pakistan": "~2.0% to 3.0% (elite nationwide competition)",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.70 / 4.00, coupled with demonstrable leadership achievements and social impact",
            "typical_academic_and_research_profile": "High-achieving young leaders across diverse fields (entrepreneurs, civil servants, tech innovators, NGO founders) with exceptional leadership track records.",
            "common_backgrounds_of_winners": "Graduates from premier global universities (Harvard, Oxford, Stanford, Tsinghua, MIT) and top Pakistani universities (LUMS, NUST, FAST-NUCES).",
            "high_representation_countries": "United States, China, Pakistan, United Kingdom, India, Germany, Kenya, Brazil, Australia.",
            "competitiveness_tier": "MOST_COMPETITIVE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply via official portal schwarzmanscholars.org.",
                "Schwarzman Scholars never charges application fees or collaborates with commercial admissions consultants."
            ],
            "application_fee_warning": "Applying to Schwarzman Scholars is 100% free.",
            "agent_and_intermediary_warnings": "Commercial agency written essays are immediately disqualified; authentic personal voice is paramount.",
            "hidden_costs_breakdown": [
                "Application fee: USD 0 (Free).",
                "All flights, room, board, tuition, laptop, and insurance covered 100% by the scholarship.",
                "Passport issuance and initial document copies: ~PKR 15,000 to 25,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You need prior background in Chinese language or Asian studies. Reality: No prior Chinese experience is expected.",
                "Myth: Only political science or IR majors are chosen. Reality: STEM, business, medicine, and humanities graduates make up over half the cohort."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim candidates over 28 can get waivers; the age requirement (under 29 years old on August 1) is strictly enforced."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain satisfactory academic progress and pass all required core and elective modules at Schwarzman College.",
            "attendance_requirements": "Full-time residential requirement at Schwarzman College in Beijing for the entire 11-month program duration.",
            "academic_progress_monitoring": "Continuous assessment through case studies, examinations, deep-dive field projects, and capstone practical projects.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment during the intensive 11-month curriculum.",
            "home_country_return_obligation": "None; scholars join an influential global alumni network and can pursue careers anywhere in the world.",
            "service_obligations_or_bonds": "Zero service bond or financial repayment obligation.",
            "repayment_clawback_conditions": "Expulsion and fellowship revocation for academic dishonesty, code of conduct violations, or illegal acts.",
            "rules_for_changing_university": "Non-transferable; exclusive to Tsinghua University.",
            "rules_for_changing_major": "Fixed curriculum in Master of Management Science in Global Affairs.",
            "extension_policy": "Program is strictly 11 months in duration; no extensions permitted."
        },
        "official_sources_verified": [
            {
                "source_name": "Schwarzman Scholars Official Portal",
                "source_url": "https://www.schwarzmanscholars.org/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Tsinghua University Graduate Admissions",
                "source_url": "https://gradadmission.tsinghua.edu.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
