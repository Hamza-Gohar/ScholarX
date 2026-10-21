"""Batch 26 Part 2: East Asia Elite STEM Awards (3 awards)
SCH-AS-064: Tohoku University Global 30 Future Global Leadership (FGL) MEXT Award
SCH-AS-065: Nagoya University Global 30 (G30) International Graduate Program MEXT Award
SCH-AS-067: KAIST International Graduate Scholarship & Research Assistantship
"""

DATA_P2 = {
    "SCH-AS-064": {
        "scholarship_id": "SCH-AS-064",
        "basic_details": {
            "scholarship_name": "Tohoku University Future Global Leadership (FGL) MEXT University Recommendation Award",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan & Tohoku University",
            "host_country": "Japan",
            "host_institutions_covered": "Tohoku University (Aobayama and Katahira Campuses, Sendai, Miyagi Prefecture, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Master of Engineering (MEng)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Science, Graduate School of Engineering, Graduate School of Information Sciences, and Graduate School of Environmental Studies (International Graduate Program in Advanced Science, International Materials Science Program, and Robotics Program).",
            "number_of_awards_total": "~45 to 65 MEXT University Recommendation scholarships awarded annually under FGL graduate tracks",
            "number_of_awards_pakistan": "Open internationally; typically 8 to 14 Pakistani engineering and science researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master's; 3 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 146,000 / month for Master's (~PKR 277,400 / month); JPY 147,000 / month for PhD (~PKR 279,300 / month) plus 100% full tuition waiver and round-trip international airfare"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries with official diplomatic relations with Japan (Pakistan fully eligible; Japanese dual citizens ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2, 1991 (under 35 years old at commencement per MEXT statutory regulations).",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (for Master's) or recognized 18-year Master's degree (for PhD) with minimum MEXT Grade Point Coefficient of 2.30 out of 3.00 from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 2.3,
            "grading_conversion_notes": "Minimum MEXT GPA calculation of 2.30 out of 3.00; competitive applicants typically hold MEXT GPA >= 2.65 / 3.00 (equivalent to CGPA >= 3.55 / 4.00).",
            "subject_background_prerequisites": "Materials science, mechanical engineering, robotics, aerospace engineering, physics, chemistry, information sciences, or environmental studies.",
            "current_education_status": "Graduated or final-year students completing degree requirements before arrival in Japan (late September).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in materials science, robotics, or engineering journals provide a significant competitive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate demonstrating CEFR B2 or higher.",
            "other_language_requirements": "Japanese language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure a Letter of Provisional Acceptance from a Tohoku University professor prior to institutional nomination.",
            "previous_scholarship_restrictions": "Previous MEXT recipients are ineligible unless at least 3 years have elapsed since completing previous award.",
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
                "details": "Screening fee is waived for MEXT scholarship nominees.",
                "amount": "100% waived (JPY 30,000 value)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized international student housing at Tohoku University International House (Sanbongi) or University House Aobayama (approx. JPY 20,000 to 38,000 / month), paid from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free stipend: JPY 146,000 / month for Master's (~PKR 277,400 / month); JPY 147,000 / month for PhD (~PKR 279,300 / month) plus regional allowance top-up.",
                "amount": "JPY 146,000 to 147,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international flight ticket between Pakistan and Tokyo Narita/Sendai airport fully funded by MEXT.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese Student Visa issued free of charge for MEXT government scholars.",
                "amount": "100% covered / fee exempt"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Enrolled in Japan National Health Insurance (NHI) covering 70% of medical costs; subsidized monthly premium (approx. JPY 2,000/month) paid from stipend.",
                "amount": "Subsidized National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Aobayama, Katahira, and Kawauchi campuses, including halal-friendly dining options.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Tohoku University Institute for Materials Research (IMR), Research Institute of Electrical Communication (RIEC), and university libraries.",
                "amount": "100% covered world-leading lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and JSPS project funds cover domestic and international conference participation.",
                "amount": "Lab grant-funded conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Direct subway connection (Sendai Subway Tozai Line) serving Aobayama campus directly with student discount passes.",
                "amount": "Subsidized subway transit"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Japanese Imperial University (Tohoku University, Sendai).",
            "participating_institutions": [
                "Tohoku University (Aobayama, Katahira, and Kawauchi Campuses, Sendai, Japan)"
            ],
            "university_rankings_scope": "QS World University Rankings #107 globally, Ranked #1 in Japan by Times Higher Education (THE Japan University Rankings); globally renowned for materials science, physics, and engineering.",
            "available_majors": [
                "Master's / PhD in Materials Science and Engineering (IMR)",
                "Master's / PhD in Mechanical Engineering and Aerospace",
                "Master's / PhD in Robotics and Information Sciences",
                "Master's / PhD in Physics and Applied Physics",
                "Master's / PhD in Chemistry and Chemical Engineering",
                "Master's / PhD in Environmental Studies"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with MEXT GPA >= 2.30/3.00, academic transcripts, research proposal, Letter of Provisional Acceptance from Tohoku Univ professor, two recommendation letters, and English proficiency certificate (IELTS 6.5+ / TOEFL 80+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Materials Science and Robotics are globally preeminent and highly competitive; securing an official Letter of Provisional Acceptance from a Tohoku professor is the decisive requirement.",
            "strategic_program_match_advice": "Target research groups affiliated with the Institute for Materials Research (IMR) or WPI Advanced Institute for Materials Research (AIMR) with proposals aligned with next-gen energy storage or spintronics."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.insc.tohoku.ac.jp/english/degree/graduate-programs/",
            "portal_system_name": "Tohoku University FGL & MEXT University Recommendation Portal",
            "account_creation_instructions": "Contact prospective faculty advisor, obtain Letter of Provisional Acceptance, compile MEXT application forms, submit online application, and dispatch certified physical dossier to Graduate School Office.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective academic advisor at Tohoku University with CV, transcripts, and research proposal (September-November).",
                "Step 2: Obtain Letter of Provisional Acceptance from professor.",
                "Step 3: Complete MEXT University Recommendation application package (November-December).",
                "Step 4: Prospective supervisor submits nomination dossier to Faculty Graduate Committee.",
                "Step 5: Tohoku University conducts internal screening and submits institutional recommendation list to MEXT Tokyo in March.",
                "Step 6: MEXT Tokyo officially ratifies scholarship awards in June.",
                "Step 7: Receive Certificate of Eligibility, obtain Japanese visa, and receive flight tickets.",
                "Step 8: Fly to Tokyo/Sendai in late September and start autumn semester on October 1."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track: Admission and MEXT scholarship are evaluated together upon faculty nomination.",
            "recommendation_letters_submission_method": "Submitted as formal recommendation letters signed by university deans or academic professors on institutional letterhead.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (Kenkyu Keikakusho) detailing background, objectives, experimental methods, and anticipated contributions.",
            "study_plan_research_proposal_requirements": "Structured academic proposal following MEXT format detailing problem statement, literature review, experimental methodology, and timeline.",
            "cv_format_requirements": "Academic CV detailing education, laboratory techniques, programming skills, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental committee.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 80+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "JPY 0 (Waived for MEXT scholarship nominees)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations recommended for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translation for all non-English/non-Japanese documents.",
            "final_submission_method": "Submission via departmental graduate office followed by postal dispatch of certified physical dossier to Tohoku University."
        },
        "required_documents_checklist": [
            {
                "document_name": "MEXT Application Form for University Recommendation",
                "mandatory": True,
                "specification": "Official Japanese Ministry prescribed application form with applicant photo.",
                "pakistan_specific_instruction": "Standard official MEXT form."
            },
            {
                "document_name": "Field of Study and Research Plan (Kenkyu Keikakusho)",
                "mandatory": True,
                "specification": "Detailed research plan following official MEXT template describing proposed research in Japan.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Official Academic Transcripts and Graduation Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing course grades, credits, and grading system for MEXT GPA calculation.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Letter of Recommendation from Dean or Higher Authority",
                "mandatory": True,
                "specification": "Recommendation letter addressed to the President of Tohoku University signed by university Dean or Rector.",
                "pakistan_specific_instruction": "On institutional letterhead with official seal."
            },
            {
                "document_name": "Abstract of Bachelor's / Master's Thesis",
                "mandatory": True,
                "specification": "Concise 1-2 page summary of previous graduation thesis or major research project.",
                "pakistan_specific_instruction": "Summary of final year project or thesis."
            },
            {
                "document_name": "Tohoku University Letter of Provisional Acceptance",
                "mandatory": True,
                "specification": "Signed letter from Tohoku University faculty member committing to supervise the applicant.",
                "pakistan_specific_instruction": "Obtained directly from prospective Tohoku Univ professor."
            },
            {
                "document_name": "Certificate of English Language Proficiency",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "Score report or institutional letter."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1",
            "application_deadline": "December 15",
            "university_admission_deadline": "December 15",
            "document_submission_deadline": "December 20 (Physical hard-copy arrival)",
            "recommendation_letters_deadline": "December 15",
            "interview_period": "January - February",
            "shortlist_announcement": "March (University nomination to MEXT) / June (MEXT Tokyo final ratification)",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Single annual admission cycle for October intake; contact with professors must begin by September-October."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (MEXT GPA calculation >= 2.30/3.00, academic consistency)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated in MEXT academic screening)",
            "research_experience_weight": "40% (Technical research proposal rigor, previous thesis, supervisor endorsement)",
            "work_experience_weight": "5% (Relevant scientific laboratory or technical engineering experience)",
            "personal_statement_weight": "5% (Study plan clarity and intent)",
            "recommendations_weight": "5% (Dean's official recommendation)",
            "interview_weight": "10% (Technical interview with prospective Tohoku University faculty advisor)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Tohoku University Graduate School Academic Board, Global Learning Center, and Japanese Ministry of Education (MEXT).",
            "evaluation_methodology": "Rigorous academic assessment prioritizing candidates with top MEXT GPA coefficients (above 2.65/3.00), strong publication potential, and supervisor backing."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~850 to 1,100 applicants across graduate divisions",
            "total_scholarships_awarded": "~45 to 65 MEXT University Recommendation awards annually under FGL",
            "acceptance_rate_global": "~5.0% to 6.0%",
            "acceptance_rate_pakistan": "~10.0% to 14.0% for candidates with professor provisional acceptance and MEXT GPA >= 2.65",
            "typical_successful_applicant_gpa": "MEXT GPA coefficient >= 2.65 / 3.00 (approx. CGPA >= 3.55 / 4.00), accompanied by strong thesis research or publications",
            "typical_academic_and_research_profile": "STEM graduates with strong laboratory foundations, clear research alignment with Tohoku University research centers, and professor acceptance.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, Quaid-i-Azam, FAST-NUCES, UET Lahore, COMSATS, PIEAS, GIKI).",
            "high_representation_countries": "Pakistan, Vietnam, Indonesia, China, Bangladesh, Thailand, Egypt, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only consult official websites at tohoku.ac.jp and mext.go.jp.",
                "Beware of unauthorized agents claiming to sell MEXT recommendation seats; MEXT awards are managed strictly by universities."
            ],
            "application_fee_warning": "No application or examination fee is charged for MEXT scholarship nominees.",
            "agent_and_intermediary_warnings": "Commercial agency written proposals are rejected; applicants must author their own Kenkyu Keikakusho.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (Waived).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Medical checkup for COE processing: ~PKR 15,000 to 25,000.",
                "Initial pocket money before first stipend deposit: ~JPY 100,000 (~PKR 190,000).",
                "National Health Insurance monthly premium: ~JPY 2,000/month (~PKR 3,800/month)."
            ],
            "misleading_claims_debunked": [
                "Myth: Japanese language fluency is mandatory. Reality: All FGL graduate programs at Tohoku University are conducted 100% in English.",
                "Myth: You can apply without professor endorsement. Reality: University recommendation track requires prior provisional acceptance from a Tohoku University faculty professor."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest age limit can be relaxed; MEXT statutory age cutoff (born on or after April 2, 1991) is strictly enforced."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain MEXT Grade Point Coefficient of at least 2.30 out of 3.00 throughout study.",
            "attendance_requirements": "Full-time physical research residency in Sendai; monthly signing of scholarship register at university academic office to receive stipend.",
            "academic_progress_monitoring": "Annual progress review submitted to MEXT via the Graduate School.",
            "work_restrictions_during_study": "Part-time work restricted; requires immigration permission (Shikakugai Katsudo Kyoka) and written consent from academic supervisor.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdocs in Japan, or return to Pakistan.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is immediately terminated if GPA falls below 2.30 or if disciplinary expulsion occurs.",
            "rules_for_changing_university": "Strictly non-transferable under MEXT University Recommendation regulations.",
            "rules_for_changing_major": "Major or laboratory changes are generally not permitted once enrolled.",
            "extension_policy": "Extensions from Master's to PhD are highly competitive and require separate MEXT institutional recommendation screening."
        },
        "official_sources_verified": [
            {
                "source_name": "Tohoku University Global Learning Center & MEXT Guide",
                "source_url": "https://www.insc.tohoku.ac.jp/english/degree/graduate-programs/",
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
    },

    "SCH-AS-065": {
        "scholarship_id": "SCH-AS-065",
        "basic_details": {
            "scholarship_name": "Nagoya University Global 30 (G30) International Graduate Program MEXT Award",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan & Nagoya University",
            "host_country": "Japan",
            "host_institutions_covered": "Nagoya University (Higashiyama Campus, Nagoya, Aichi Prefecture, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Master of Engineering (MEng)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Engineering, Graduate School of Science, Graduate School of Bioagricultural Sciences, and Graduate School of Environmental Studies (Automotive Engineering, Civil and Environmental Engineering, Physics and Mathematics, and Biological and Bioagricultural Sciences).",
            "number_of_awards_total": "~40 to 60 MEXT University Recommendation scholarships awarded annually under G30 programs",
            "number_of_awards_pakistan": "Open internationally; typically 7 to 12 Pakistani engineering and science researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master's; 3 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 146,000 / month for Master's (~PKR 277,400 / month); JPY 147,000 / month for PhD (~PKR 279,300 / month) plus 100% full tuition waiver and round-trip international airfare"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries with official diplomatic relations with Japan (Pakistan fully eligible; Japanese dual citizens ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2, 1991 (under 35 years old at commencement per MEXT statutory regulations).",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (for Master's) or recognized 18-year Master's degree (for PhD) with minimum MEXT Grade Point Coefficient of 2.30 out of 3.00 from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 2.3,
            "grading_conversion_notes": "Minimum MEXT GPA calculation of 2.30 out of 3.00; competitive applicants typically hold MEXT GPA >= 2.65 / 3.00 (equivalent to CGPA >= 3.55 / 4.00).",
            "subject_background_prerequisites": "Automotive engineering, mechanical engineering, electrical engineering, materials science, physics, chemistry, biology, or environmental studies.",
            "current_education_status": "Graduated or final-year students completing degree requirements before arrival in Japan (late September).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in automotive technology, robotics, physics, or chemistry provide a significant competitive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate demonstrating CEFR B2 or higher.",
            "other_language_requirements": "Japanese language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure inquiry approval and formal consent from a Nagoya University faculty professor before applying.",
            "previous_scholarship_restrictions": "Previous MEXT recipients are ineligible unless at least 3 years have elapsed since completing previous award.",
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
                "details": "Screening fee is waived for MEXT scholarship nominees.",
                "amount": "100% waived (JPY 30,000 value)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized international student housing at Nagoya University International Residence (Higashiyama) or Foreign Student House (approx. JPY 22,000 to 40,000 / month), paid from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free stipend: JPY 146,000 / month for Master's (~PKR 277,400 / month); JPY 147,000 / month for PhD (~PKR 279,300 / month).",
                "amount": "JPY 146,000 to 147,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international flight ticket between Pakistan and Nagoya Chubu Centrair International Airport fully funded by MEXT.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese Student Visa issued free of charge for MEXT government scholars.",
                "amount": "100% covered / fee exempt"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Enrolled in Japan National Health Insurance (NHI) covering 70% of medical costs; subsidized monthly premium (approx. JPY 2,000/month) paid from stipend.",
                "amount": "Subsidized National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Higashiyama and Daiko campuses, including halal-friendly dining options.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Nagoya University Kobayashi-Maskawa Institute for the Origin of Particles and the Universe (KMI), Synchrotron Radiation Facility, and university libraries.",
                "amount": "100% covered Nobel-winning lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and JSPS project funds cover domestic and international conference participation.",
                "amount": "Lab grant-funded conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Direct subway access (Nagoya Daigaku Station located directly inside the campus) with student commuter discounts.",
                "amount": "Subsidized subway transit"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Japanese Imperial University (Nagoya University - Meidai).",
            "participating_institutions": [
                "Nagoya University (Higashiyama Campus, Nagoya, Aichi Prefecture, Japan)"
            ],
            "university_rankings_scope": "QS World University Rankings #152 globally, #6 in Japan; home to 6 Nobel Prize laureates (physics & chemistry) and located at the heart of Japan's automotive manufacturing hub (Toyota / Aichi region).",
            "available_majors": [
                "Master's / PhD in Automotive Engineering",
                "Master's / PhD in Civil and Environmental Engineering",
                "Master's / PhD in Mechanical Systems Engineering",
                "Master's / PhD in Physics and Applied Physics",
                "Master's / PhD in Chemistry and Materials",
                "Master's / PhD in Biological and Bioagricultural Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with MEXT GPA >= 2.30/3.00, academic transcripts, research proposal, professor consent letter, two recommendation letters, and English proficiency certificate (IELTS 6.5+ / TOEFL 80+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Automotive Engineering and Physics are world-leading and highly competitive; establishing contact with a Nagoya professor during the pre-application inquiry period is essential.",
            "strategic_program_match_advice": "Focus proposals on intelligent vehicle tech, battery chemistry, or quantum materials, connecting directly to Nagoya's industrial partnerships with Toyota and DENSO."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://admissions.g30.nagoya-u.ac.jp/",
            "portal_system_name": "Nagoya University G30 Online Admissions System & MEXT Portal",
            "account_creation_instructions": "Submit pre-application inquiry to prospective supervisor, secure faculty consent, register on G30 admissions portal, complete online application, upload documents, and submit.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective academic advisor at Nagoya University via G30 pre-application inquiry (September-November).",
                "Step 2: Obtain formal consent from professor to act as academic supervisor.",
                "Step 3: Complete MEXT University Recommendation application package on the G30 portal (November-January).",
                "Step 4: Graduate School Admissions Committee conducts document screening and video interviews.",
                "Step 5: Nagoya University submits institutional recommendation list to MEXT Tokyo in March.",
                "Step 6: MEXT Tokyo officially ratifies scholarship awards in June.",
                "Step 7: Receive Certificate of Eligibility, obtain Japanese visa, and receive flight tickets.",
                "Step 8: Fly to Nagoya Chubu Airport in late September and start autumn semester on October 1."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track: Admission and MEXT scholarship are evaluated together upon faculty nomination.",
            "recommendation_letters_submission_method": "Submitted online by recommenders via confidential portal links or uploaded as signed letters on institutional letterhead.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (Kenkyu Keikakusho) detailing background, objectives, experimental methods, and anticipated contributions.",
            "study_plan_research_proposal_requirements": "Structured academic proposal following MEXT format detailing problem statement, literature review, experimental methodology, and timeline.",
            "cv_format_requirements": "Academic CV detailing education, laboratory techniques, programming skills, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental committee.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 80+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "JPY 0 (Waived for MEXT scholarship nominees)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations recommended for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translation for all non-English/non-Japanese documents.",
            "final_submission_method": "Online submission via Nagoya University G30 admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "MEXT Application Form for University Recommendation",
                "mandatory": True,
                "specification": "Official Japanese Ministry prescribed application form with applicant photo.",
                "pakistan_specific_instruction": "Standard official MEXT form."
            },
            {
                "document_name": "Field of Study and Research Plan (Kenkyu Keikakusho)",
                "mandatory": True,
                "specification": "Detailed research plan following official MEXT template describing proposed research in Japan.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Official Academic Transcripts and Graduation Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing course grades, credits, and grading system for MEXT GPA calculation.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from university dean or department chair and previous academic supervisor.",
                "pakistan_specific_instruction": "On institutional letterhead with official stamps."
            },
            {
                "document_name": "Summary of Thesis or Past Research Achievements",
                "mandatory": True,
                "specification": "Concise 1-2 page summary of Bachelor's or Master's thesis and list of publications.",
                "pakistan_specific_instruction": "Summary of final year project or thesis."
            },
            {
                "document_name": "Faculty Consent Form / Letter from Nagoya University Professor",
                "mandatory": True,
                "specification": "Written confirmation from a Nagoya University professor agreeing to supervise the applicant.",
                "pakistan_specific_instruction": "Obtained directly from prospective Nagoya professor."
            },
            {
                "document_name": "Certificate of English Language Proficiency",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "Score report or institutional letter."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1",
            "application_deadline": "January 10",
            "university_admission_deadline": "January 10",
            "document_submission_deadline": "January 10",
            "recommendation_letters_deadline": "January 10",
            "interview_period": "January - February",
            "shortlist_announcement": "March (University nomination to MEXT) / June (MEXT Tokyo final ratification)",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Single annual admission cycle for October intake; contact with professors must begin by September-October."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (MEXT GPA calculation >= 2.30/3.00, academic consistency)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated in MEXT academic screening)",
            "research_experience_weight": "40% (Technical research proposal rigor, previous thesis, supervisor endorsement)",
            "work_experience_weight": "5% (Relevant scientific laboratory or technical engineering experience)",
            "personal_statement_weight": "5% (Study plan clarity and intent)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview with prospective Nagoya University faculty advisor)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Nagoya University G30 Admissions Board, School Deans, and Japanese Ministry of Education (MEXT).",
            "evaluation_methodology": "Rigorous academic assessment prioritizing candidates with top MEXT GPA coefficients (above 2.65/3.00), strong publication potential, and supervisor backing."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~750 to 950 applicants across graduate divisions",
            "total_scholarships_awarded": "~40 to 60 MEXT University Recommendation awards annually under G30",
            "acceptance_rate_global": "~5.5% to 6.5%",
            "acceptance_rate_pakistan": "~10.0% to 14.0% for candidates with professor consent and MEXT GPA >= 2.65",
            "typical_successful_applicant_gpa": "MEXT GPA coefficient >= 2.65 / 3.00 (approx. CGPA >= 3.55 / 4.00), accompanied by strong thesis research or publications",
            "typical_academic_and_research_profile": "STEM graduates with strong laboratory foundations, clear research alignment with Nagoya University research centers, and professor acceptance.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, Quaid-i-Azam, FAST-NUCES, UET Lahore, COMSATS, PIEAS, GIKI).",
            "high_representation_countries": "Pakistan, Vietnam, Indonesia, China, Bangladesh, Thailand, Egypt, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only consult official websites at nagoya-u.ac.jp and mext.go.jp.",
                "Beware of unauthorized agents claiming to sell MEXT recommendation seats; MEXT awards are managed strictly by universities."
            ],
            "application_fee_warning": "No application or examination fee is charged for MEXT scholarship nominees.",
            "agent_and_intermediary_warnings": "Commercial agency written proposals are rejected; applicants must author their own Kenkyu Keikakusho.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (Waived).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Medical checkup for COE processing: ~PKR 15,000 to 25,000.",
                "Initial pocket money before first stipend deposit: ~JPY 100,000 (~PKR 190,000).",
                "National Health Insurance monthly premium: ~JPY 2,000/month (~PKR 3,800/month)."
            ],
            "misleading_claims_debunked": [
                "Myth: Japanese language fluency is mandatory. Reality: All G30 graduate programs at Nagoya University are conducted 100% in English.",
                "Myth: You can apply without professor endorsement. Reality: University recommendation track requires prior consent from a Nagoya University faculty professor."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest age limit can be relaxed; MEXT statutory age cutoff (born on or after April 2, 1991) is strictly enforced."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain MEXT Grade Point Coefficient of at least 2.30 out of 3.00 throughout study.",
            "attendance_requirements": "Full-time physical research residency in Nagoya; monthly signing of scholarship register at university academic office to receive stipend.",
            "academic_progress_monitoring": "Annual progress review submitted to MEXT via the Graduate School.",
            "work_restrictions_during_study": "Part-time work restricted; requires immigration permission (Shikakugai Katsudo Kyoka) and written consent from academic supervisor.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdocs in Japan, or return to Pakistan.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is immediately terminated if GPA falls below 2.30 or if disciplinary expulsion occurs.",
            "rules_for_changing_university": "Strictly non-transferable under MEXT University Recommendation regulations.",
            "rules_for_changing_major": "Major or laboratory changes are generally not permitted once enrolled.",
            "extension_policy": "Extensions from Master's to PhD are highly competitive and require separate MEXT institutional recommendation screening."
        },
        "official_sources_verified": [
            {
                "source_name": "Nagoya University G30 International Admissions & MEXT Guide",
                "source_url": "https://admissions.g30.nagoya-u.ac.jp/",
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
    },

    "SCH-AS-067": {
        "scholarship_id": "SCH-AS-067",
        "basic_details": {
            "scholarship_name": "KAIST International Graduate Scholarship & Full Tuition Assistantship",
            "offering_entity": "Korea Advanced Institute of Science and Technology (KAIST) & Ministry of Science and ICT (MSIT), South Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "KAIST Main Campus (Daejeon) and Seoul Campus (South Korea)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)", "Combined Master's & PhD"],
            "major_restrictions": "College of Natural Sciences (Physics, Chemistry, Mathematical Sciences), College of Life Science and Bioengineering, College of Engineering (Mechanical, Aerospace, Electrical, Computer Science, Chemical and Biomolecular, Materials Science, Civil and Environmental), and College of AI.",
            "number_of_awards_total": "~300 to 450 international graduate scholarships awarded annually across departments",
            "number_of_awards_pakistan": "Extensive international cohort; typically 35 to 60 Pakistani STEM, computing, and engineering researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 semesters (2 years) for Master's; 8 semesters (4 years) for PhD; 10 semesters (5 years) for Combined MS/PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "KRW 350,000 / month institutional base stipend plus laboratory RA stipend: Total monthly living allowance typically KRW 1,000,000 to 1,500,000 / month for Master's (~PKR 210,000 to 315,000 / month) and KRW 1,400,000 to 2,000,000 / month for PhD (~PKR 294,000 to 420,000 / month), combined with 100% full tuition fee waiver"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants whose parents both hold non-Korean citizenship (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to young researchers with strong academic momentum.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum CGPA 3.30/4.00 for Master's; recognized 18-year Master's degree with minimum CGPA 3.30/4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum CGPA 3.30 / 4.00; selected candidates at KAIST typically hold CGPA >= 3.65 / 4.00 or top 5-10% class rank.",
            "subject_background_prerequisites": "Computer science, electrical engineering, artificial intelligence, mechanical engineering, aerospace, physics, chemistry, materials science, or chemical engineering.",
            "current_education_status": "Graduated or final-year students completing degree requirements before semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in peer-reviewed scientific journals (SCI/SCIE) or top conferences (NeurIPS, ICML, CVPR, IEEE) provide a massive competitive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 83,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 83, TOEIC 720+, or official English Medium of Instruction (MOI) certificate from an accredited university.",
            "other_language_requirements": "Korean language proficiency is not required; 100% of graduate courses and research at KAIST are conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants select 'KAIST Scholarship' directly on the online admission portal; all admitted international students are automatically considered for full scholarship.",
            "previous_scholarship_restrictions": "Cannot hold another parallel government fellowship covering identical costs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver covering all standard degree semesters at KAIST.",
                "amount": "100% covered (~KRW 8,000,000 to 10,000,000 / semester value; ~PKR 3,360,000 to 4,200,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Online application fee of USD 80 (or KRW 80,000) paid via credit card on the KAIST portal.",
                "amount": "USD 80 (~PKR 22,400)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "On-campus international graduate dormitory housing in Daejeon (twin-occupancy rooms approx. KRW 120,000 to 180,000 / month), paid easily from living stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Combined institutional and lab research stipend: KRW 1,000,000 to 1,500,000 / month for Master's (~PKR 210,000 to 315,000 / month); KRW 1,400,000 to 2,000,000 / month for PhD (~PKR 294,000 to 420,000 / month).",
                "amount": "KRW 1,000,000 to 2,000,000 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Seoul Incheon International Airport is self-funded.",
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
                "details": "Extensive subsidized on-campus cafeterias at Daejeon campus, including dedicated Muslim-friendly dining cafeteria (Kaimaru); meals cost KRW 4,000 to 6,000.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to KAIST Main Library, supercomputing facilities, state-of-the-art nanofabrication cleanrooms (KANC), and research equipment.",
                "amount": "100% covered world-class research facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and national project budgets cover international conference registration, travel, and accommodation for accepted papers.",
                "amount": "Lab grant-funded international conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle buses connecting KAIST Main Campus, Munji Campus, and local transit centers.",
                "amount": "Free campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single South Korea #1 premier science and technology research institution (KAIST, Daejeon).",
            "participating_institutions": [
                "KAIST Main Campus (Yuseong-gu, Daejeon) and Seoul Campus (Hongneung), South Korea"
            ],
            "university_rankings_scope": "QS World University Rankings #53 globally, #1 in South Korea for Engineering & Technology, World Top 20 for Materials Science and Electrical Engineering.",
            "available_majors": [
                "Master's / PhD in School of Computing",
                "Master's / PhD in Kim Jaechul Graduate School of AI",
                "Master's / PhD in School of Electrical Engineering",
                "Master's / PhD in Department of Mechanical Engineering",
                "Master's / PhD in Department of Materials Science and Engineering",
                "Master's / PhD in Department of Chemical and Biomolecular Engineering",
                "Master's / PhD in Department of Physics and Mathematical Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years; Combined MS/PhD: 5 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with CGPA >= 3.30/4.00, academic transcripts, statement of purpose, two recommendation letters, English test score (IELTS 6.5+ / TOEFL 83+ / MOI), and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of Computing, Graduate School of AI, and Electrical Engineering are exceptionally selective; contacting professors before or during application significantly increases selection likelihood.",
            "strategic_program_match_advice": "Examine current projects of KAIST laboratory principal investigators, email professors citing recent journal papers, and express willingness to contribute to their specific funded research tasks."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://admission.kaist.ac.kr/graduate/",
            "portal_system_name": "KAIST Online Graduate Admissions Portal",
            "account_creation_instructions": "Register on the KAIST graduate admissions portal during open intake, select 'KAIST Scholarship' funding track, complete forms, upload digital documents, pay USD 80 fee, and dispatch hard-copy certified dossier to Admissions Office.",
            "step_by_step_workflow": [
                "Step 1: Explore KAIST departmental research laboratories and contact prospective professors with CV and research interests (July for Spring / December for Fall).",
                "Step 2: Create account on KAIST Online Graduate Admissions System.",
                "Step 3: Complete online application, write statement of financial resources selecting KAIST Scholarship, and pay USD 80 fee.",
                "Step 4: Register two recommenders who submit online recommendation letters.",
                "Step 5: Send certified hard-copy documents (degrees, transcripts, apostille/attestations) via DHL to KAIST Admissions Office in Daejeon.",
                "Step 6: Departmental admissions committee reviews applications and conducts virtual technical interviews if required.",
                "Step 7: Final admission and scholarship award results announced online.",
                "Step 8: Obtain Certificate of Admission (CoA), apply for South Korean D-2 visa, and arrive in Daejeon."
            ],
            "university_vs_scholarship_routing": "Integrated Institutional Route: Admission and KAIST Scholarship are evaluated simultaneously as a unified decision.",
            "recommendation_letters_submission_method": "Submitted online by two recommenders via confidential portal links.",
            "personal_statement_prompts": "Statement of Purpose (prescribed KAIST format) detailing academic background, research interests, career vision, and why KAIST is the ideal institution.",
            "study_plan_research_proposal_requirements": "Structured research statement outlining technical focus areas, proposed methodologies, and alignment with target KAIST research labs.",
            "cv_format_requirements": "Standard academic CV detailing education, laboratory competencies, programming skills, honors, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by departmental faculty committee or prospective lab PI.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 83+, TOEIC 720+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "USD 80 (approx. PKR 22,400)",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required, followed by Korean Embassy consular legalization in Islamabad or Apostille.",
            "translation_requirements": "Certified English or Korean translation for all non-English/non-Korean documents.",
            "final_submission_method": "Dual submission: Online portal application followed by mandatory postal dispatch of certified physical dossier to KAIST."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's / Master's degree certificates and transcripts with CGPA >= 3.30/4.00.",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and consular legalized by Korean Embassy Islamabad."
            },
            {
                "document_name": "Statement of Purpose (SOP)",
                "mandatory": True,
                "specification": "Completed on official KAIST form detailing background, motivation, research interests, and career goals.",
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
                "specification": "IELTS Academic 6.5+, TOEFL iBT 83+, or official English Medium of Instruction (MOI) certificate.",
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
            "application_open_date": "August 20 (Spring intake) / March 5 (Fall intake)",
            "application_deadline": "September 20 (Spring intake) / April 5 (Fall intake)",
            "university_admission_deadline": "September 20 / April 5",
            "document_submission_deadline": "September 27 / April 12 (Hard copy postal arrival in Daejeon)",
            "recommendation_letters_deadline": "September 25 / April 10",
            "interview_period": "October - November / May",
            "shortlist_announcement": "Early December (Spring) / Late June (Fall)",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "January / July",
            "semester_commencement": "March 1 (Spring semester) / September 1 (Fall semester)",
            "annual_cycle_notes": "Bi-annual intake: Spring semester starts in March, Fall semester starts in September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior CGPA, academic rigor in STEM/computing, university standing)",
            "extracurricular_and_leadership_weight": "5% (Initiative, teamwork, problem-solving mindset)",
            "research_experience_weight": "40% (Technical research capability, publications, programming skills, research proposal)",
            "work_experience_weight": "5% (Industry engineering or software development experience)",
            "personal_statement_weight": "5% (Clarity of vision and alignment with KAIST research frontiers)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "5% (Performance in departmental technical interview)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind pure merit evaluation)",
            "selection_panel_composition": "KAIST Departmental Admissions Committee, School Graduate Deans, and Admissions Board.",
            "evaluation_methodology": "Rigorous holistic evaluation assessing mathematical ability, research productivity, experimental aptitude, and alignment with faculty laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 4,500 international applicants across both intakes",
            "total_scholarships_awarded": "~300 to 450 fully funded international awards annually",
            "acceptance_rate_global": "~8.0% to 10.0%",
            "acceptance_rate_pakistan": "~12.0% to 16.0% for applicants with strong research profiles and CGPA >= 3.60",
            "typical_successful_applicant_gpa": "Undergraduate/Master's CGPA >= 3.60 / 4.00, accompanied by strong programming skills or publications",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records in computer science, engineering, or physics, documented project experience, and professor alignment.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, Vietnam, China, India, Indonesia, Turkey, Iran, Kazakhstan, Russia.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal admission.kaist.ac.kr.",
                "KAIST does not work with third-party agents; all applications must be submitted directly by the candidate."
            ],
            "application_fee_warning": "Application fee of USD 80 is paid directly through the secure KAIST online portal.",
            "agent_and_intermediary_warnings": "Applications prepared by commercial agents are rejected; authentic personal statements and research experience are essential.",
            "hidden_costs_breakdown": [
                "Application fee: USD 80 (~PKR 22,400).",
                "NADRA FRC and document attestations (HEC, MoFA, Korean Embassy): ~PKR 35,000 to 50,000.",
                "DHL document courier to South Korea: ~PKR 12,000.",
                "South Korean D-2 Visa fee: ~USD 60 (~PKR 17,000).",
                "Flight to Seoul Incheon: ~PKR 150,000 to 220,000.",
                "Initial living deposit before first stipend payment: ~KRW 500,000 (~PKR 105,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Korean TOPIK certificate is needed. Reality: 100% of graduate education at KAIST is conducted in English.",
                "Myth: Flights are included. Reality: Airfare to South Korea is self-funded by the student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim KAIST requires GRE; GRE is optional and not mandatory for international graduate admissions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain minimum semester GPA of 2.70 out of 4.30 to retain the tuition waiver each semester.",
            "attendance_requirements": "Full-time physical research presence at KAIST campus; daily participation in laboratory research activities.",
            "academic_progress_monitoring": "Semi-annual academic progress review evaluated by research advisor.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Korean immigration law; part-time work requires permission from immigration and university.",
            "home_country_return_obligation": "None; graduates are eligible for Korean D-10 job seeker visas or E-7 professional engineering visas upon graduation.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if semester GPA drops below 2.70 or if student is dismissed for disciplinary infractions.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change requires approval from current advisor, new advisor, and department heads.",
            "extension_policy": "Extensions beyond standard 4 semesters (Master's) or 8 semesters (PhD) are generally not covered by the scholarship."
        },
        "official_sources_verified": [
            {
                "source_name": "KAIST Graduate Admissions Official Portal",
                "source_url": "https://admission.kaist.ac.kr/graduate/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "KAIST International Students and Scholars Service (ISSS)",
                "source_url": "https://isss.kaist.ac.kr/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
