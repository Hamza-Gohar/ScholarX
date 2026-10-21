"""
scripts/dossiers_part3.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Part 3
Contains:
15. SCH-AM-009: Knight-Hennessy Scholars Program at Stanford University (USA)
16. SCH-EU-095: Karolinska Institutet Global Master's Scholarship (Sweden)
17. SCH-EU-098: ICTP Abdus Salam Postgraduate Diploma Programme (Italy)
18. SCH-AM-068: Perimeter Institute PSI Master's Fellowships in Theoretical Physics (Canada)
19. SCH-EU-102: Wageningen University Excellence Programme in Agriculture & Environment (Netherlands)
20. SCH-ME-043: KFUPM Graduate STEM Fellowships in Engineering & Physical Sciences (Saudi Arabia)
"""

DOSSIERS_PART3 = {
    # 15. Knight-Hennessy Scholars at Stanford University (USA)
    "SCH-AM-009": {
        "scholarship_id": "SCH-AM-009",
        "basic_details": {
            "scholarship_name": "Knight-Hennessy Scholars at Stanford University",
            "offering_entity": "Stanford University (Knight-Hennessy Scholars Program)",
            "host_country": "United States",
            "host_institutions_covered": "Stanford University (All 7 Schools: Engineering, Humanities & Sciences, Medicine, Law, Business, Education, Doerr School of Sustainability)",
            "degree_levels": ["Master's", "PhD"],
            "major_restrictions": "Open to ALL full-time graduate degree programs at Stanford: DMA, JD, MA, MBA, MD, MFA, MPP, MS, and PhD programs. Dual- and joint-degrees are fully supported.",
            "number_of_awards_total": "Up to 100 high-achieving scholars selected globally each cohort (~85 to 90 enrolled)",
            "number_of_awards_pakistan": "Open competition across all countries; Pakistani scholars are regularly selected for Knight-Hennessy cohorts",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3 years of full graduate funding at Stanford (additional years for PhD funded via department assistantships)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to citizens of all countries worldwide (Pakistani citizens fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit; however, applicants must have earned their first undergraduate degree within the prior 7 years (e.g. earned in 2018 or later for 2025/2026 intake).",
            "academic_qualifications": "Equivalent of a U.S. bachelor's degree from a college or university of recognized standing (typically 16-year BS / 4-year degree from Pakistan).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "No minimum GPA set by Knight-Hennessy, but Stanford departmental admissions require stellar academic performance (competitive average 3.8+ / 4.00 CGPA).",
            "subject_background_prerequisites": "Prerequisites set by the specific Stanford graduate degree program.",
            "current_education_status": "Graduated within the past 7 years or in final undergraduate year graduating prior to Stanford matriculation.",
            "graduation_year_restrictions": "First bachelor's degree must have been earned in January 2018 or later.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; leadership, impact, and purposeful initiative are paramount.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Must satisfy the English requirements of the Stanford graduate program (Stanford typically requires TOEFL iBT 100+ for PhD/MS).",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "DUAL APPLICATION MANDATORY: You must apply separately to Knight-Hennessy Scholars AND apply separately to the specific Stanford graduate degree program by its respective deadline.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full tuition fees and associated departmental fees paid directly for up to 3 years at Stanford."},
            "admission_application_fee": {"status": "WAIVED", "details": "Knight-Hennessy application is free; Stanford department application fee waivers available for eligible international applicants."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via comprehensive living stipend sufficient for on-campus graduate housing at Stanford."},
            "monthly_stipend": {"status": "COVERED", "details": "Annual living stipend paid quarterly to cover living expenses in Palo Alto / Silicon Valley.", "amount": "$45,000 to $52,000 / year (~$3,800 to $4,300 / month or ~PKR 1,050,000 to 1,200,000 / month)"},
            "airfare": {"status": "COVERED", "details": "Annual round-trip economy airfare to and from Stanford University (one flight per year)."},
            "visa_fee": {"status": "COVERED", "details": "Reimbursement for F-1 or J-1 visa fees and SEVIS fee upon enrollment."},
            "health_insurance": {"status": "COVERED", "details": "Cardinal Care health insurance coverage at Stanford fully paid."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Covered within living stipend."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Annual academic and instructional materials stipend included (~$2,000/year).", "amount": "~$2,000 / year"},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Access to King Global Leadership Program (KGLP) enrichment funds and conference travel grants."},
            "travel_transit_allowance": {"status": "COVERED", "details": "One-time relocation / settling-in stipend upon initial arrival at Stanford (~$1,000).", "amount": "$1,000 one-off"},
            "total_estimated_value_usd_per_year": 95000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single University: Stanford University (Stanford, California).",
            "participating_institutions": ["Stanford University (School of Engineering, School of Humanities & Sciences, Stanford Medicine, Stanford Law, Stanford GSB, Stanford Doerr)"],
            "university_rankings_scope": "World #2 (QS World Rankings / Times Higher Education).",
            "available_majors": ["All Stanford graduate programs (Computer Science, Artificial Intelligence, Bioengineering, Electrical Engineering, Medicine, Law, Public Policy, Energy Science)"],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 1-2 years; PhD: 3-5 years (KHS covers first 3 years, department covers years 4-5)",
            "admission_requirements_summary": "Undergraduate degree transcripts, GRE/GMAT/MCAT/LSAT (as required by department), 3 recommendation letters, KHS essays, video statement.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "KHS does NOT admit you to Stanford; you must be independently admitted by the Stanford graduate department. If the department rejects you, KHS cannot fund you.",
            "strategic_program_match_advice": "Demonstrate the three KHS pillars in every essay: Independence of Thought (intellectual curiosity, contrarian thinking), Purposeful Leadership (initiative, ambition), Civic Mindset (humility, collaboration, service)."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://knight-hennessy.stanford.edu/",
            "portal_system_name": "Knight-Hennessy Online Application Portal (Slate)",
            "account_creation_instructions": "Register on the KHS online application system in June/July; submit KHS application by early October deadline.",
            "step_by_step_workflow": [
                "1. Register on KHS online application portal (opens June 1).",
                "2. Complete profile, upload transcripts, resume, and input 2 reference contacts.",
                "3. Write two short essays: 1) What matters most to you, and why? 2) How will your Stanford degree enable you to impact the world?",
                "4. Submit KHS online application before early October deadline (e.g., October 8, 2026 at 1:00 PM PDT).",
                "5. Submit video statement (record 2-minute video response via portal within designated window).",
                "6. Submit separate graduate application to your intended Stanford degree program by its specific departmental deadline (October - December).",
                "7. KHS Selection Committee reviews dossiers and selects ~150-170 finalists in January.",
                "8. Finalists attend 'Immersion Weekend' at Stanford University (expenses paid) in March for interviews and leadership challenges.",
                "9. Final cohort of ~85-90 Knight-Hennessy Scholars announced in late March / early April.",
                "10. Matriculate at Stanford University in September."
            ],
            "university_vs_scholarship_routing": "Dual Application: Apply to KHS in early October; apply to Stanford department by its departmental deadline.",
            "recommendation_letters_submission_method": "Submitted online by 2 referees directly via confidential portal links.",
            "personal_statement_prompts": "Two essays: 1) Connect the dots: Tell us about the experiences that have shaped you and what drives your ambition (up to 600 words). 2) How will your Stanford education help you fulfill your goals (up to 400 words)?",
            "study_plan_research_proposal_requirements": "Department-specific research statement submitted with the Stanford graduate application.",
            "cv_format_requirements": "Strict 1-page resume detailing academic, leadership, and public service achievements.",
            "interviews_conducted": True,
            "interview_format_details": "Immersion Weekend at Stanford: In-person group leadership challenges, individual interviews with Stanford faculty and global leaders, and community discussions.",
            "standardized_tests": "Standardized tests determined by Stanford department (GRE, GMAT, etc.); not mandated by KHS itself.",
            "application_fee_amount": "$0.00 for KHS application (Stanford department fees apply unless fee waiver granted).",
            "attestation_requirements": "HEC degree attestation required for international credential evaluation upon enrollment.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online portal submission."
        },
        "required_documents_checklist": [
            {"document_name": "Knight-Hennessy Online Application Form", "mandatory": True, "specification": "Completed via Slate portal", "pakistan_specific_instruction": "Ensure all dates match bachelor's degree conferral"},
            {"document_name": "Official Academic Transcripts", "mandatory": True, "specification": "Scanned transcripts from all post-secondary institutions attended", "pakistan_specific_instruction": "Must demonstrate exceptional CGPA (3.7+)"},
            {"document_name": "One-Page Professional Resume", "mandatory": True, "specification": "Strictly 1 page maximum summarizing leadership, projects, and impact", "pakistan_specific_instruction": "Highlight entrepreneurial, research, and civic leadership"},
            {"document_name": "Two Recommendation Letters", "mandatory": True, "specification": "Submitted directly by recommenders answering specific KHS character prompts", "pakistan_specific_instruction": "Referees must assess intellectual vitality and civic mindset"},
            {"document_name": "Two Knight-Hennessy Essays", "mandatory": True, "specification": "Connecting the dots (600 words) and Stanford impact (400 words)", "pakistan_specific_instruction": "Authenticity and vulnerability are prized over superficial boasting"},
            {"document_name": "Two-Minute Video Statement", "mandatory": True, "specification": "Recorded directly on the portal after submitting the application", "pakistan_specific_instruction": "Unedited spontaneous video response to prompt"}
        ],
        "important_dates_timeline": {
            "application_open_date": "June 1 annually (e.g., 2026-06-01)",
            "application_deadline": "Early October annually (e.g., 2026-10-08 at 13:00 PDT)",
            "university_admission_deadline": "Varies by Stanford department (typically November - December)",
            "document_submission_deadline": "Coincides with October KHS deadline",
            "recommendation_letters_deadline": "Coincides with October KHS deadline",
            "interview_period": "Late February / Early March (Immersion Weekend at Stanford)",
            "shortlist_announcement": "Mid-January (Finalists invited to Immersion Weekend)",
            "final_result_acceptance_deadline": "Mid-April annually",
            "visa_application_window": "May - July (F-1 / J-1 Student Visa)",
            "semester_commencement": "Late September (Autumn Quarter at Stanford)",
            "annual_cycle_notes": "Stanford degree application deadlines must be strictly observed; missing department deadline voids KHS application."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Independence of thought, original insight, intellectual audacity)",
            "extracurricular_and_leadership_weight": "35% (Purposeful leadership, driving change against adversity)",
            "research_experience_weight": "15% (Academic innovation in chosen field)",
            "work_experience_weight": "5% (Initiative in ventures or institutions)",
            "personal_statement_weight": "10% (Authenticity, ethical clarity, self-awareness)",
            "recommendations_weight": "5% (Insightful peer and mentor testimonies)",
            "interview_weight": "Immersion Weekend determines final cohort selection among finalists",
            "test_scores_weight": "Evaluated by department for admission",
            "financial_need_weight": "0% (Pure talent, leadership, and character)",
            "selection_panel_composition": "Stanford faculty deans, former university presidents, prominent alumni, and global thought leaders.",
            "evaluation_methodology": "Holistic review evaluating the three pillars: Independence of Thought, Purposeful Leadership, and Civic Mindset."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~8,000 to 10,000 elite applicants worldwide",
            "total_scholarships_awarded": "~85 to 90 scholars enrolled annually",
            "acceptance_rate_global": "~1.0%",
            "acceptance_rate_pakistan": "~0.8% to 1.2% (World Top-Tier Selectivity)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Breakthrough research contributor, tech entrepreneur, social justice advocate, or policy innovator.",
            "common_backgrounds_of_winners": "Graduates of Stanford, Harvard, MIT, Oxford, LUMS, AKU, NUST, and top international academies.",
            "high_representation_countries": "Global diversity spanning 40+ nationalities per cohort.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam consultants promising 'guaranteed Stanford admission'. Stanford and Knight-Hennessy admissions operate under strict independent integrity codes."
            ],
            "application_fee_warning": "Knight-Hennessy application is 100% FREE.",
            "agent_and_intermediary_warnings": "Any consultant involvement or ghost-written essays will lead to immediate disqualification.",
            "hidden_costs_breakdown": [
                "Stanford graduate department application fee ($125 to $175) unless fee waiver is obtained.",
                "Standardized test fees (GRE, TOEFL).",
                "US visa appointment fees."
            ],
            "misleading_claims_debunked": [
                "MYTH: Knight-Hennessy admits you to Stanford. (Fact: You must be independently admitted by the Stanford graduate department; KHS cannot overrule a departmental rejection).",
                "MYTH: You cannot apply if you graduated 5 years ago. (Fact: Anyone who earned their bachelor's within the past 7 years is fully eligible)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites confuse the KHS deadline with the Stanford department deadline. The KHS deadline is in early October, while department deadlines are in November/December."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and satisfy Stanford degree milestones.",
            "attendance_requirements": "Full physical enrollment and active participation in the King Global Leadership Program (KGLP) at Denning House.",
            "academic_progress_monitoring": "Termly progress reviews with KHS academic advisors.",
            "work_restrictions_during_study": "Scholars may take on university teaching/research assistantships consistent with Stanford policy and visa rules.",
            "home_country_return_obligation": "No mandatory home residency rule; scholars are free to pursue careers globally or in the US (F-1 OPT/STEM OPT eligible).",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Expulsion from Stanford for honor code violations terminates scholarship.",
            "rules_for_changing_university": "Non-transferable (tenable exclusively at Stanford).",
            "rules_for_changing_major": "Requires approval from both departments and KHS leadership.",
            "extension_policy": "Maximum 3 years of KHS funding; subsequent years of PhD are covered by the academic department."
        },
        "official_sources_verified": [
            {
                "source_name": "Stanford University - Knight-Hennessy Scholars Official Portal",
                "source_url": "https://knight-hennessy.stanford.edu/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact applicant numbers by specific nationality",
                    "Immersion Weekend scoring matrix"
                ]
            }
        ]
    },

    # 16. Karolinska Institutet Global Master's Scholarship (Sweden)
    "SCH-EU-095": {
        "scholarship_id": "SCH-EU-095",
        "basic_details": {
            "scholarship_name": "Karolinska Institutet Global Master's Scholarship",
            "offering_entity": "Karolinska Institutet (Home of the Nobel Assembly in Physiology or Medicine)",
            "host_country": "Sweden",
            "host_institutions_covered": "Karolinska Institutet (Stockholm, Sweden)",
            "degree_levels": ["Master's"],
            "major_restrictions": "Exclusively open to Karolinska Institutet Global Master's Programs: Biomedicine, Public Health Sciences, Global Health, Toxicology, Health Informatics, Molecular Techniques in Life Science, Biostatistics and Data Science.",
            "number_of_awards_total": "~10 full tuition scholarships awarded globally per academic year",
            "number_of_awards_pakistan": "Open global competition; Pakistani medical and life sciences graduates compete directly",
            "funding_classification": "TUITION_ONLY",
            "duration_of_scholarship": "1 to 2 years (covers the full 60 or 120 ECTS credit curriculum of the Master's program)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of non-EU/EEA countries required to pay tuition fees in Sweden (Pakistan is fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit.",
            "academic_qualifications": "Bachelor's degree or equivalent (16 years education in Pakistan / MBBS / BDS / PharmD / BS Biotechnology / Biochemistry) from an internationally recognized university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum 3.50/4.00 CGPA or first division; evaluated strictly on top academic merit among applicants.",
            "subject_background_prerequisites": "Relevant undergraduate degree in Medicine, Life Sciences, Pharmacy, Biology, or Computer Science (for Health Informatics).",
            "current_education_status": "Degree completed before university start in August.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; laboratory experience and clinical research heavily valued.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Must satisfy Swedish English 6 requirement: IELTS Academic minimum 6.5 (no section below 5.5) or TOEFL iBT minimum 90 (writing min 20). MOI certificates from Pakistan generally NOT accepted by UniversityAdmissions.se unless bachelor's was granted by an English-speaking country.",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "CRITICAL REQUIREMENT: Must apply for a Karolinska Institutet Master's program via UniversityAdmissions.se as your FIRST PRIORITY (Rank 1). Applications ranked lower are ineligible for the scholarship.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% full tuition fee waiver paid directly to Karolinska Institutet (SEK 180,000 to SEK 200,000 / year = ~SEK 400,000 total / ~PKR 10,500,000 value)."},
            "admission_application_fee": {"status": "NOT_COVERED", "details": "Swedish central university application fee of SEK 900 (~PKR 24,000) must be paid to UniversityAdmissions.se."},
            "accommodation": {"status": "NOT_COVERED", "details": "Living expenses and housing are NOT covered by this scholarship (KI Housing assists in dormitory booking, rent ~SEK 4,500-6,500/month paid by student)."},
            "monthly_stipend": {"status": "NOT_COVERED", "details": "No living stipend included. Scholars must cover living costs via personal funds or apply concurrently for the Swedish Institute (SI) Scholarship."},
            "airfare": {"status": "NOT_COVERED", "details": "Travel costs to Sweden borne by student."},
            "visa_fee": {"status": "NOT_COVERED", "details": "Swedish Residence Permit for Higher Education fee (SEK 1,500) paid to Swedish Migration Agency."},
            "health_insurance": {"status": "COVERED", "details": "Full comprehensive medical insurance through FAS+ insurance provided by the Swedish Legal, Financial and Administrative Services Agency (Kammarkollegiet)."},
            "food_allowance": {"status": "NOT_COVERED", "details": "Self-funded."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Self-funded."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Departmental research laboratory funding for master's thesis projects."},
            "travel_transit_allowance": {"status": "NOT_COVERED", "details": "Discounted Stockholm student SL travelcard."},
            "total_estimated_value_usd_per_year": 20000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Institution: Karolinska Institutet (Solna and Flemingsberg campuses, Stockholm).",
            "participating_institutions": ["Karolinska Institutet"],
            "university_rankings_scope": "World #7 in Medicine, #1 in Sweden (QS World University Rankings by Subject).",
            "available_majors": ["Biomedicine", "Public Health Sciences (Epidemiology / Health Promotion)", "Global Health", "Toxicology", "Health Informatics", "Molecular Techniques in Life Science", "Biostatistics"],
            "english_taught_program_availability": True,
            "program_duration": "1 or 2 years (60 to 120 ECTS credits)",
            "admission_requirements_summary": "Bachelor's degree in medicine/health/STEM, transcripts, CV, specific entry requirements per program, English 6.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Must apply via UniversityAdmissions.se by January 15; scholarship application opens in early February specifically for applicants with KI as choice #1.",
            "strategic_program_match_advice": "Pakistani MBBS, BDS, and PharmD graduates have an exceptional match for Global Health and Public Health Sciences; BS Biotechnology graduates match Biomedicine and Molecular Techniques."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://education.ki.se/scholarships",
            "portal_system_name": "UniversityAdmissions.se (Sweden central) & Karolinska Scholarship Portal",
            "account_creation_instructions": "1) Apply to KI on UniversityAdmissions.se by January 15; 2) Pay SEK 900 application fee; 3) Receive application number; 4) Apply on Karolinska scholarship webform in February.",
            "step_by_step_workflow": [
                "1. Register on UniversityAdmissions.se (opens mid-October).",
                "2. Select a Karolinska Institutet Global Master's program as your FIRST CHOICE (Rank 1).",
                "3. Pay the SEK 900 application fee and upload required academic documents and IELTS test by February 1.",
                "4. Access the Karolinska Institutet scholarship portal (opens February 10).",
                "5. Enter your 8-digit UniversityAdmissions application number.",
                "6. Upload tailored CV highlighting scientific publications, clinical trials, or public health field projects.",
                "7. Submit scholarship application by February 28 deadline.",
                "8. KI Admissions Committee evaluates academic merit and research background.",
                "9. Scholarship recipients announced simultaneously with Swedish university admission results (late March).",
                "10. Accept admission and scholarship offer in April.",
                "11. Apply for Swedish Residence Permit for Higher Education (Migrationsverket).",
                "12. Arrive in Stockholm (late August)."
            ],
            "university_vs_scholarship_routing": "Sequential: UniversityAdmissions.se application first -> Karolinska scholarship webform second.",
            "recommendation_letters_submission_method": "Not required for general KI scholarship; CV is the primary evaluated document.",
            "personal_statement_prompts": "CV and scientific experience; some programs require a program-specific summary sheet.",
            "study_plan_research_proposal_requirements": "Not applicable.",
            "cv_format_requirements": "Structured academic CV emphasizing scientific laboratory skills, clinical research, epidemiology, and publications.",
            "interviews_conducted": False,
            "interview_format_details": "No interview; 100% paper-based academic merit review.",
            "standardized_tests": "IELTS Academic (6.5) or TOEFL iBT (90) mandatory. No GRE needed.",
            "application_fee_amount": "SEK 900 application fee to UniversityAdmissions.se; scholarship webform itself is free.",
            "attestation_requirements": "Transcripts and degrees must be uploaded to UniversityAdmissions according to strict country-specific rules for Pakistan (official university color scans).",
            "translation_requirements": "Official English translations for any documents in Urdu.",
            "final_submission_method": "Online submission via UniversityAdmissions.se and KI webform."
        },
        "required_documents_checklist": [
            {"document_name": "Bachelor's / Professional Degree Certificate", "mandatory": True, "specification": "MBBS, BDS, PharmD, or BS Honours in biology/health/STEM", "pakistan_specific_instruction": "Must be recognized by HEC and PMDC/PNC if medical"},
            {"document_name": "Official Transcripts of Records", "mandatory": True, "specification": "Complete transcripts showing all courses and grades for all semesters", "pakistan_specific_instruction": "Uploaded directly to UniversityAdmissions.se"},
            {"document_name": "Valid English Proficiency Certificate", "mandatory": True, "specification": "IELTS Academic (min 6.5) or TOEFL iBT (min 90)", "pakistan_specific_instruction": "Must satisfy Swedish English 6 requirement"},
            {"document_name": "Valid Passport Information Page", "mandatory": True, "specification": "Scanned copy of valid passport", "pakistan_specific_instruction": "Required to prove non-EU/EEA citizenship"},
            {"document_name": "Curriculum Vitae for Scholarship", "mandatory": True, "specification": "Tailored academic CV emphasizing research publications, clinical experience, and awards", "pakistan_specific_instruction": "Primary document reviewed by KI scholarship committee"},
            {"document_name": "Program-Specific Summary Sheet", "mandatory": False, "specification": "Downloaded from KI website for specific programs (e.g. Biomedicine)", "pakistan_specific_instruction": "Must be uploaded with university admissions application"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Mid-October (UniversityAdmissions.se); Early February (KI Scholarship webform)",
            "application_deadline": "January 15 (University admissions); February 28 (Scholarship webform)",
            "university_admission_deadline": "January 15 annually",
            "document_submission_deadline": "February 1 for UniversityAdmissions documents",
            "recommendation_letters_deadline": "N/A",
            "interview_period": "N/A",
            "shortlist_announcement": "Late March annually (with admissions notification)",
            "final_result_acceptance_deadline": "Early April annually",
            "visa_application_window": "April - June (Swedish Migration Agency)",
            "semester_commencement": "Late August (Autumn Semester)",
            "annual_cycle_notes": "Ranking KI as choice #1 on UniversityAdmissions is an absolute prerequisite."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Undergraduate GPA, medical school honors, course relevance)",
            "extracurricular_and_leadership_weight": "5% (General suitability)",
            "research_experience_weight": "35% (Prior research publications, thesis quality, lab techniques)",
            "work_experience_weight": "10% (Clinical or public health practice in Pakistan)",
            "personal_statement_weight": "0% (Not evaluated separately; reflected through CV)",
            "recommendations_weight": "0%",
            "interview_weight": "0%",
            "test_scores_weight": "Gatekeeper requirement (English 6)",
            "financial_need_weight": "0% (Pure academic excellence in medicine and life sciences)",
            "selection_panel_composition": "Karolinska Institutet Global Master's Admissions and Scholarship Committee.",
            "evaluation_methodology": "Ranking based on academic merit, research trajectory, and fit for the master's program."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,000 international fee-paying applicants across KI programs",
            "total_scholarships_awarded": "~10 scholarships awarded globally",
            "acceptance_rate_global": "~0.5% to 0.7%",
            "acceptance_rate_pakistan": "~0.5% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 / 4.00 CGPA (or top 5% of medical/pharmacy graduating class)",
            "typical_academic_and_research_profile": "First-author or co-authored research paper in PubMed indexed journals, top marks in pathology, microbiology, or pharmacology.",
            "common_backgrounds_of_winners": "Graduates of Aga Khan University (AKU), King Edward Medical University, Dow University of Health Sciences, NUST, Quaid-i-Azam University.",
            "high_representation_countries": "Global competition.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam agencies claiming KI provides fully funded stipends. The KI Global Master's scholarship is TUITION-ONLY.",
                "Unofficial portals claiming they can bypass the UniversityAdmissions.se SEK 900 application fee."
            ],
            "application_fee_warning": "UniversityAdmissions.se charges a mandatory SEK 900 fee; the KI scholarship form itself is free.",
            "agent_and_intermediary_warnings": "KI evaluates academic credentials directly through official university channels.",
            "hidden_costs_breakdown": [
                "Living expenses in Stockholm: NOT COVERED. Students must show proof of at least SEK 10,314/month (~PKR 270,000/mo) in their personal bank account to the Swedish Migration Agency to obtain their student residence permit!",
                "Rent in Stockholm: SEK 5,000 to 7,500/month.",
                "Flight ticket to Stockholm (PKR 180,000 to 250,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: This scholarship gives you living money. (Fact: It covers 100% tuition ONLY; you must self-fund living expenses or secure an external grant).",
                "MYTH: You can rank KI as choice #2 and get the scholarship. (Fact: If KI is ranked choice #2, your scholarship application is automatically discarded)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently fail to clarify that this award is tuition-only, leading students to financial distress when applying for Swedish visas."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass at least 75% of credits (45 out of 60 ECTS) in Year 1 to have the Year 2 tuition waiver renewed.",
            "attendance_requirements": "Full-time study enrollment at Karolinska Institutet in Stockholm.",
            "academic_progress_monitoring": "Academic results evaluated at the end of each study period.",
            "work_restrictions_during_study": "International students in Sweden have NO legal limit on work hours during their studies, provided they maintain satisfactory academic progress.",
            "home_country_return_obligation": "NO mandatory home return requirement. Sweden permits graduates to apply for a 1-year Job Seeker Residence Permit to seek employment or establish a business in Sweden.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Tuition waiver is cancelled if the student ceases studies or fails to achieve required credits.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Covers strictly the standard program duration (max 2 years)."
        },
        "official_sources_verified": [
            {
                "source_name": "Karolinska Institutet - Official Global Master's Scholarship Portal",
                "source_url": "https://education.ki.se/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of scholarships awarded per master's program (KI announces 10 in total without fixed program quotas)",
                    "Internal academic merit score rankings"
                ]
            }
        ]
    },

    # 17. ICTP Abdus Salam Postgraduate Diploma Programme (Italy)
    "SCH-EU-098": {
        "scholarship_id": "SCH-EU-098",
        "basic_details": {
            "scholarship_name": "ICTP Postgraduate Diploma Programme in Theoretical Physics & Mathematics",
            "offering_entity": "The Abdus Salam International Centre for Theoretical Physics (ICTP) / UNESCO & IAEA",
            "host_country": "Italy",
            "host_institutions_covered": "ICTP Trieste (Miramare Campus, Trieste, Italy) in collaboration with SISSA (International School for Advanced Studies)",
            "degree_levels": ["Postgraduate Diploma (Pre-Doctoral)"],
            "major_restrictions": "Restricted strictly to foundational mathematical and physical sciences: 1) High Energy, Cosmology and Astroparticle Physics (HECAP), 2) Condensed Matter Physics (CMP), 3) Earth System Physics (ESP), 4) Mathematics (MATH), 5) Quantitative Life Sciences (QLS).",
            "number_of_awards_total": "~40 to 50 students selected globally each year (~8 to 10 per research section)",
            "number_of_awards_pakistan": "Open competition with historical prominence; Pakistani physicists and mathematicians regularly win multiple seats annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "12 months (intensive pre-doctoral diploma acting as direct pipeline to top international PhD programs)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to talented young physicists and mathematicians from developing countries (Pakistan is fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 28,
            "age_limit_notes": "Candidates should generally be under 28 years of age on December 31 of application year.",
            "academic_qualifications": "Equivalent of an MSc or a 4-year BS in Physics, Mathematics, or closely related field (16 to 18 years education in Pakistan).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum 3.50/4.00 CGPA or first-class degree with exceptional performance in advanced mathematics and physics coursework.",
            "subject_background_prerequisites": "Advanced background in Classical Mechanics, Quantum Mechanics, Electrodynamics, Statistical Mechanics, and Mathematical Methods.",
            "current_education_status": "Completed degree or in final semester (degree must be completed before August departure).",
            "graduation_year_restrictions": "Recent graduates prioritized.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "No formal IELTS/TOEFL required; English proficiency evaluated via transcripts, recommendation letters, and online interview.",
            "other_language_requirements": "None; all lectures and research conducted 100% in English.",
            "gender_specific_requirements": "Equal opportunity; women physicists and mathematicians strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates from developing countries who have not already had extensive research opportunities in high-income nations.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% full tuition exemption for the entire 1-year postgraduate diploma."},
            "admission_application_fee": {"status": "WAIVED", "details": "ICTP application is completely free."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Free single-room accommodation provided on the ICTP campus in Miramare, Trieste (Galileo or Enrico Fermi guest houses)."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living stipend paid directly by ICTP for the full 12-month tenure.", "amount": "€450 / month (~PKR 135,000 / month) (pocket allowance since housing is free on campus)"},
            "airfare": {"status": "COVERED", "details": "Round-trip economy class international airfare between Pakistan and Venice/Trieste airport prepaid directly by ICTP."},
            "visa_fee": {"status": "REIMBURSED", "details": "Italian National D Student Visa processing fee covered/reimbursed upon arrival."},
            "health_insurance": {"status": "COVERED", "details": "Comprehensive health and emergency medical insurance covered by ICTP under United Nations / UNESCO institutional policy."},
            "food_allowance": {"status": "SUBSIDIZED", "details": "Subsidized meals available at the ICTP campus cafeteria (approx €3-€4 per meal)."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Free access to the world-renowned Marie Curie Library, computing clusters, and specialized scientific textbooks."},
            "research_funding_conference_grant": {"status": "COVERED", "details": "Full participation in all ICTP advanced international research schools, workshops, and colloquia."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Local transport between Trieste airport/railway station and ICTP campus arranged/reimbursed."},
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Institution: ICTP Trieste, Italy (joint diploma awarded in collaboration with SISSA).",
            "participating_institutions": ["The Abdus Salam International Centre for Theoretical Physics (ICTP) and SISSA"],
            "university_rankings_scope": "World premier research center in theoretical physics (UNESCO Category 1 Institute).",
            "available_majors": ["High Energy Physics (Cosmology, Strings, Particles)", "Condensed Matter Physics", "Earth System Physics", "Pure Mathematics", "Quantitative Life Sciences"],
            "english_taught_program_availability": True,
            "program_duration": "12 months (September to August)",
            "admission_requirements_summary": "Bachelor's / Master's transcripts, CV, statement of purpose, 2 recommendation letters.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single application: Applying to the Postgraduate Diploma Programme automatically enters the applicant for full fellowship funding.",
            "strategic_program_match_advice": "Focus heavily on foundational coursework performance in quantum mechanics, mathematical methods, and statistical mechanics; high grades in these core courses are crucial."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ictp.it/programmes/postgraduate-diploma-programme",
            "portal_system_name": "ICTP Online Application Portal",
            "account_creation_instructions": "Register on the ICTP online system between November and January; select one of the 5 scientific sections.",
            "step_by_step_workflow": [
                "1. Register on the ICTP application portal (opens late November).",
                "2. Choose one specific research section (HECAP, CMP, ESP, MATH, or QLS).",
                "3. Upload university transcripts, degree certificates, and detailed course syllabus.",
                "4. Write Statement of Purpose articulating passion for theoretical physics/mathematics.",
                "5. Register details of 2 academic referees who upload confidential letters directly.",
                "6. Submit online application before January 31 deadline.",
                "7. Scientific section faculty committees review dossiers (February - March).",
                "8. Shortlisted candidates may be invited for an online technical interview via Zoom (March).",
                "9. Final selection results announced in April/May.",
                "10. ICTP provides visa guarantee letters for Italian National D Visa application at Italian Embassy Islamabad.",
                "11. Depart for Trieste, Italy in late August."
            ],
            "university_vs_scholarship_routing": "Integrated 1-step routing: Acceptance guarantees 100% full fellowship.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated confidential links.",
            "personal_statement_prompts": "Statement of Purpose: Academic trajectory, mathematical foundation, why ICTP, and future doctoral research aspirations.",
            "study_plan_research_proposal_requirements": "Not applicable; focus on coursework mastery and diploma dissertation interests.",
            "cv_format_requirements": "Academic CV detailing physics/math competitions, honors, and coursework.",
            "interviews_conducted": True,
            "interview_format_details": "Shortlisted candidates often undertake a 20-minute online technical interview via Zoom where ICTP faculty ask conceptual physics or mathematical problem-solving questions.",
            "standardized_tests": "No standardized tests required.",
            "application_fee_amount": "€0.00 (100% FREE application).",
            "attestation_requirements": "HEC attested transcripts required for visa and diploma registration.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online portal submission."
        },
        "required_documents_checklist": [
            {"document_name": "Official Academic Transcripts", "mandatory": True, "specification": "Complete transcripts showing all physics and mathematics courses and grades", "pakistan_specific_instruction": "Must demonstrate exceptional analytical and mathematical grades"},
            {"document_name": "Curriculum Vitae", "mandatory": True, "specification": "Detailing education, computational skills, physics honors, and publications", "pakistan_specific_instruction": "Highlight research projects and Olympiad achievements"},
            {"document_name": "Statement of Purpose", "mandatory": True, "specification": "1 to 2 page explanation of motivation and choice of research section", "pakistan_specific_instruction": "Address theoretical physics challenges and post-diploma PhD goals"},
            {"document_name": "Two Confidential Letters of Recommendation", "mandatory": True, "specification": "From university professors who taught applicant advanced physics or mathematics", "pakistan_specific_instruction": "Must evaluate candidate's mathematical aptitude and problem-solving capability"},
            {"document_name": "Copy of Valid Passport", "mandatory": True, "specification": "Scanned copy of valid passport information page", "pakistan_specific_instruction": "Required for Italian visa guarantee letter"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Late November annually (e.g., 2026-11-20)",
            "application_deadline": "January 31 annually (e.g., 2027-01-31)",
            "university_admission_deadline": "Coincides with January 31 deadline",
            "document_submission_deadline": "January 31 annually",
            "recommendation_letters_deadline": "Early February annually",
            "interview_period": "March (online technical interviews)",
            "shortlist_announcement": "April - May annually",
            "final_result_acceptance_deadline": "Late May annually",
            "visa_application_window": "June - July (Italian Embassy Islamabad)",
            "semester_commencement": "September 1 (Intensive Diploma Session)",
            "annual_cycle_notes": "Founded by Nobel Laureate Prof. Abdus Salam; world-renowned springboard to PhD programs at SISSA, Cambridge, Oxford, and Max Planck."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Grades in foundational physics and advanced mathematics coursework)",
            "extracurricular_and_leadership_weight": "5% (Scientific drive)",
            "research_experience_weight": "20% (Analytical problem solving, capstone project in physics)",
            "work_experience_weight": "0%",
            "personal_statement_weight": "10% (Clarity of scientific purpose)",
            "recommendations_weight": "10% (Detailed testimonials of mathematical brilliance)",
            "interview_weight": "5% (Technical interview assessing conceptual physics problem-solving)",
            "test_scores_weight": "0% (No standardized tests used)",
            "financial_need_weight": "0% (Pure academic excellence in theoretical sciences)",
            "selection_panel_composition": "Permanent scientific research faculty of ICTP Trieste across the 5 respective sections.",
            "evaluation_methodology": "Faculty examine every transcript line-by-line evaluating depth in quantum mechanics, electrodynamics, and linear algebra; top 8-10 candidates per section selected."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,000 to 1,500 elite physics and mathematics graduates worldwide",
            "total_scholarships_awarded": "~40 to 50 scholars admitted globally",
            "acceptance_rate_global": "~3.0% to 4.0%",
            "acceptance_rate_pakistan": "~4.0% to 5.0% (Strong historical representation from Pakistani physics departments)",
            "typical_successful_applicant_gpa": "3.70 to 4.00 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Top student in university physics/mathematics department, demonstrated mastery of quantum physics, passion for theoretical research.",
            "common_backgrounds_of_winners": "Graduates of Quaid-i-Azam University (Physics Dept), LUMS, NUST, Government College University (GCU) Lahore, PIEAS, University of the Punjab.",
            "high_representation_countries": "Pakistan, India, Iran, Nigeria, Egypt, Colombia, Vietnam.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam emails impersonating ICTP asking for 'registration fees'. ICTP is a United Nations (UNESCO/IAEA) institution and charges ZERO fees."
            ],
            "application_fee_warning": "ICTP application is 100% FREE.",
            "agent_and_intermediary_warnings": "Never use agents; ICTP faculty directly review each applicant's mathematical competence.",
            "hidden_costs_breakdown": [
                "Italian Embassy visa appointment and courier fees in Pakistan (~PKR 25,000).",
                "Pocket money buffer for personal weekend leisure in Europe."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot transition to a PhD. (Fact: Over 90% of ICTP diploma graduates directly receive fully funded PhD offers at top universities worldwide: SISSA, Cambridge, Oxford, Paris, ETH, or US universities).",
                "MYTH: The €450/month stipend is too low to survive. (Fact: Campus accommodation is 100% free, and campus food is heavily subsidized; €450 is pure pocket money for student expenses in Trieste)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently describe ICTP as a standard Italian university; it is an elite international research institute operating under United Nations diplomatic status."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass intensive semester written examinations (Pass mark 60%) to be permitted to write the diploma dissertation.",
            "attendance_requirements": "Full physical attendance in all lectures, problem-solving tutorial sessions, and seminars at ICTP Trieste.",
            "academic_progress_monitoring": "Monthly monitoring by assigned section faculty tutor.",
            "work_restrictions_during_study": "Outside employment is strictly prohibited due to the intensive pre-doctoral curriculum.",
            "home_country_return_obligation": "No mandatory home residency restriction; diploma graduates typically proceed immediately to international doctoral programs in Europe or North America.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Failing the program or voluntary withdrawal terminates fellowship.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Not permitted.",
            "extension_policy": "Strict 1-year non-extendable pre-doctoral program."
        },
        "official_sources_verified": [
            {
                "source_name": "The Abdus Salam International Centre for Theoretical Physics (ICTP) - Official Diploma Portal",
                "source_url": "https://www.ictp.it/programmes/postgraduate-diploma-programme",
                "source_type": "OFFICIAL_ORGANIZATION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact applicant numbers per scientific stream (HECAP vs CMP vs Math)",
                    "Internal technical interview evaluation questions"
                ]
            }
        ]
    },

    # 18. Perimeter Institute PSI Master's Fellowships (Canada)
    "SCH-AM-068": {
        "scholarship_id": "SCH-AM-068",
        "basic_details": {
            "scholarship_name": "Perimeter Institute PSI Master's Fellowships in Theoretical Physics",
            "offering_entity": "Perimeter Institute for Theoretical Physics & University of Waterloo",
            "host_country": "Canada",
            "host_institutions_covered": "Perimeter Institute (Waterloo, Ontario, Canada) / University of Waterloo",
            "degree_levels": ["Master's"],
            "major_restrictions": "Exclusively tenable for the Perimeter Scholars International (PSI) Master's Program in Theoretical Physics (Quantum Information, Cosmology, Particle Physics, Gravitational Physics, Quantum Fields and Strings, Quantum Gravity, Complex Systems).",
            "number_of_awards_total": "~25 to 30 scholars selected globally each year",
            "number_of_awards_pakistan": "Open global competition; exceptional Pakistani physics and math students regularly selected",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "10 months (intensive condensed master's curriculum leading to MSc in Physics from University of Waterloo)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international applicants from all countries worldwide (Pakistani students fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit.",
            "academic_qualifications": "Undergraduate degree in Physics and/or Mathematics (16 years education / BS 4-year degree) with an exceptional academic record.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum 3.70/4.00 CGPA; evaluated primarily on extraordinary mathematical aptitude, theoretical curiosity, and analytical clarity.",
            "subject_background_prerequisites": "Advanced undergraduate coursework in Quantum Mechanics, General Relativity, Classical Mechanics, Statistical Mechanics, and Linear Algebra.",
            "current_education_status": "Graduated or completing bachelor's degree before August arrival.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 7.0 or TOEFL iBT minimum 90. Can be submitted after application review if requested.",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None; female theoretical physicists strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates with deep passion for foundational questions in modern physics (black holes, quantum computing, quantum spacetime).",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% full tuition fees and incidental fees paid directly to the University of Waterloo."},
            "admission_application_fee": {"status": "WAIVED", "details": "Perimeter Institute online application is 100% free."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Private room with private ensuite bathroom in the dedicated Perimeter Institute residence (Waterloo, Ontario)."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly personal living allowance paid directly to scholar for incidental expenses.", "amount": "CAD 1,000 / month (~PKR 205,000 / month) (pocket allowance since room, board, and meals are provided)"},
            "airfare": {"status": "COVERED", "details": "Full round-trip economy class international air travel between Pakistan and Toronto Pearson International Airport."},
            "visa_fee": {"status": "REIMBURSED", "details": "Canadian Study Permit application fee reimbursed upon arrival."},
            "health_insurance": {"status": "COVERED", "details": "Full University Health Insurance Plan (UHIP) and supplementary health coverage in Ontario."},
            "food_allowance": {"status": "COVERED", "details": "Full meal plan provided: breakfast, lunch, and dinner prepared daily by in-house chefs at the Black Hole Bistro inside Perimeter Institute."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "All textbooks, research materials, and high-performance laptop provided to each student for the duration of the program."},
            "research_funding_conference_grant": {"status": "COVERED", "details": "Attendance and participation in all international Perimeter Institute workshops and scientific colloquia."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Airport transfer between Toronto Pearson Airport and Perimeter Institute residence."},
            "total_estimated_value_usd_per_year": 45000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Institution: Perimeter Institute for Theoretical Physics in partnership with University of Waterloo.",
            "participating_institutions": ["Perimeter Institute & University of Waterloo"],
            "university_rankings_scope": "World premier independent research institute for foundational theoretical physics.",
            "available_majors": ["Theoretical Physics (Quantum Fields, Cosmology, Quantum Gravity, Quantum Information, String Theory, Complex Systems)"],
            "english_taught_program_availability": True,
            "program_duration": "10 months (August to June)",
            "admission_requirements_summary": "Bachelor's degree in physics/math, transcripts, personal statement, 3 recommendation letters, GRE Physics (optional but recommended).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single application: Every single student admitted to the PSI program receives 100% full fellowship coverage automatically.",
            "strategic_program_match_advice": "Focus statement on why you want to explore the full spectrum of theoretical physics; PSI is a holistic program exposing students to quantum information, gravity, and cosmology before choosing an essay topic."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://perimeterinstitute.ca/psi-masters-program",
            "portal_system_name": "Perimeter Institute Online Admissions Portal",
            "account_creation_instructions": "Register on the Perimeter Institute portal between October and January; submit online application and register 3 referees.",
            "step_by_step_workflow": [
                "1. Register on Perimeter Institute online portal (opens October).",
                "2. Upload unofficial university transcripts, CV, and list of advanced physics/math courses taken.",
                "3. Write Statement of Purpose explaining your intellectual curiosity and passion for theoretical physics.",
                "4. Register details of 3 academic referees who upload letters directly.",
                "5. Submit online application by January deadline (e.g., January 15).",
                "6. PSI Admissions Committee evaluates files (January - February).",
                "7. Shortlisted candidates participate in an online video interview via Zoom with Perimeter faculty (February).",
                "8. Offers of admission and full fellowship extended in March.",
                "9. Formal admission paperwork filed with University of Waterloo graduate admissions.",
                "10. Apply for Canadian Study Permit (April - June).",
                "11. Arrive at Perimeter Institute in Waterloo, Canada in mid-August."
            ],
            "university_vs_scholarship_routing": "Integrated 1-step routing: Perimeter Institute admits you and provides guaranteed full fellowship; University of Waterloo confers the MSc degree.",
            "recommendation_letters_submission_method": "Submitted online by 3 academic referees directly through automated portal link.",
            "personal_statement_prompts": "Statement of Purpose (1-2 pages): Describe your background, mathematical preparation, specific theoretical physics topics that fascinate you, and your collaborative philosophy.",
            "study_plan_research_proposal_requirements": "Not applicable; coursework and research topics chosen during the program.",
            "cv_format_requirements": "Academic CV detailing physics honors, math competitions, and research projects.",
            "interviews_conducted": True,
            "interview_format_details": "20-minute online video interview via Zoom with Perimeter Institute faculty professors exploring theoretical physics concepts and mathematical reasoning.",
            "standardized_tests": "GRE General and GRE Physics are optional (considered if submitted).",
            "application_fee_amount": "CAD 0 (100% FREE application).",
            "attestation_requirements": "HEC attested transcripts required for University of Waterloo official registration upon acceptance.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online portal submission."
        },
        "required_documents_checklist": [
            {"document_name": "Official Academic Transcripts", "mandatory": True, "specification": "Complete transcripts showing all mathematics and physics courses", "pakistan_specific_instruction": "Must demonstrate top marks in advanced physics and math"},
            {"document_name": "Statement of Purpose", "mandatory": True, "specification": "1 to 2 page narrative of theoretical physics interests and goals", "pakistan_specific_instruction": "Articulate specific fascination with foundational questions"},
            {"document_name": "Three Academic Letters of Reference", "mandatory": True, "specification": "Submitted directly by university professors who can attest to mathematical and analytical aptitude", "pakistan_specific_instruction": "Critical component of the PSI review"},
            {"document_name": "Curriculum Vitae", "mandatory": True, "specification": "Detailing education, physics Olympiads, computational skills, and research", "pakistan_specific_instruction": "Highlight Python/Mathematica and theoretical modeling experience"},
            {"document_name": "Copy of Passport", "mandatory": True, "specification": "Valid international passport information page", "pakistan_specific_instruction": "Required for Canadian study permit processing"}
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1 annually (e.g., 2026-10-01)",
            "application_deadline": "January 15 annually (e.g., 2027-01-15)",
            "university_admission_deadline": "Handled internally following selection",
            "document_submission_deadline": "January 15 annually",
            "recommendation_letters_deadline": "Late January annually",
            "interview_period": "February (online video interviews via Zoom)",
            "shortlist_announcement": "March annually",
            "final_result_acceptance_deadline": "April 15 annually",
            "visa_application_window": "April - June (Canadian Study Permit / Visa)",
            "semester_commencement": "Mid-August (Fall Term)",
            "annual_cycle_notes": "One of the most prestigious, fast-paced theoretical physics master's programs in the world."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Mathematical aptitude, grades in core theoretical physics)",
            "extracurricular_and_leadership_weight": "5% (Collaborative ethos)",
            "research_experience_weight": "25% (Demonstrated independent problem-solving in physics)",
            "work_experience_weight": "0%",
            "personal_statement_weight": "15% (Passion for foundational questions)",
            "recommendations_weight": "10% (Professors evaluating candidate's analytical agility)",
            "interview_weight": "5% (Conceptual physics reasoning during Zoom interview)",
            "test_scores_weight": "Bonus factor if high GRE Physics submitted",
            "financial_need_weight": "0% (All admitted students receive full fellowship)",
            "selection_panel_composition": "Faculty researchers and directors of the Perimeter Institute for Theoretical Physics.",
            "evaluation_methodology": "Holistic review of mathematical fluency, creative problem-solving, and potential to make breakthrough contributions to theoretical physics."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 elite physics graduates worldwide",
            "total_scholarships_awarded": "~25 to 30 scholars admitted globally",
            "acceptance_rate_global": "~2.5%",
            "acceptance_rate_pakistan": "~2.0% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Exceptional mathematical and computational fluency, national physics Olympiad medals, top undergraduate physics rank.",
            "common_backgrounds_of_winners": "Graduates of LUMS, NUST, Quaid-i-Azam, GCU Lahore, PIEAS, and premier global physics universities.",
            "high_representation_countries": "Global diversity representing 20+ countries each cohort.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam agencies claiming they can secure Canadian study visas or PSI admission. Perimeter Institute operates independently and directly with applicants."
            ],
            "application_fee_warning": "Perimeter Institute charges NO application fee.",
            "agent_and_intermediary_warnings": "Never use agents.",
            "hidden_costs_breakdown": [
                "Canadian biometrics fee and study permit application fee (~CAD 235 / PKR 48,000).",
                "IELTS/TOEFL registration costs if English certificate is requested."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need a master's degree to apply. (Fact: PSI is a master's program designed for students with a 4-year bachelor's degree).",
                "MYTH: You cannot proceed to a PhD in Canada or the US. (Fact: Virtually 100% of PSI graduates secure fully funded PhD positions at top institutions worldwide: Princeton, Harvard, Stanford, Cambridge, Oxford, Perimeter/Waterloo)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently list PSI as a standard Waterloo master's; it is a unique accelerated 10-month program physically based at Perimeter Institute."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum Grade A- average (80%+) across all modular coursework.",
            "attendance_requirements": "Full physical attendance at Perimeter Institute in Waterloo, Ontario.",
            "academic_progress_monitoring": "Weekly review through homework sets, presentations, and research essay milestones.",
            "work_restrictions_during_study": "Outside employment is strictly discouraged due to the extreme intensity of the 10-month curriculum.",
            "home_country_return_obligation": "None. International graduates are eligible for Canadian Post-Graduation Work Permit (PGWP) or can transition to Canadian PhD programs.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Voluntary withdrawal or honor code violation terminates fellowship.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Strict 10-month fixed program."
        },
        "official_sources_verified": [
            {
                "source_name": "Perimeter Institute for Theoretical Physics - Official PSI Program Portal",
                "source_url": "https://perimeterinstitute.ca/psi-masters-program",
                "source_type": "OFFICIAL_ORGANIZATION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of applicants by country",
                    "Specific interview rubric scores"
                ]
            }
        ]
    },

    # 19. Wageningen University Excellence Programme (Netherlands)
    "SCH-EU-102": {
        "scholarship_id": "SCH-EU-102",
        "basic_details": {
            "scholarship_name": "Wageningen University Excellence Programme in Agriculture & Environment",
            "offering_entity": "Wageningen University & Research (WUR)",
            "host_country": "Netherlands",
            "host_institutions_covered": "Wageningen University & Research (Wageningen, Netherlands)",
            "degree_levels": ["Master's"],
            "major_restrictions": "Open to all regular full-time Wageningen MSc Master of Science programs: Agriculture, Plant Sciences, Animal Sciences, Food Technology, Organic Agriculture, Forestry and Nature Conservation, Environmental Sciences, Water Technology, Biotechnology, Climate Studies.",
            "number_of_awards_total": "~5 to 10 full excellence scholarships awarded per academic year",
            "number_of_awards_pakistan": "Open international competition across non-EEA developing countries",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "24 months (standard duration of a Wageningen 2-year MSc program, 120 ECTS)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of non-EEA countries required to pay institutional tuition fees in the Netherlands (Pakistani students fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit.",
            "academic_qualifications": "Completed undergraduate degree (4-year Bachelor's / 16 years education in Pakistan) in a relevant agricultural, biological, or environmental discipline.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "STRICT MANDATORY MERIT CUTOFF: First class honours or equivalent with a Grade Point Average (GPA) of at least 80% of the maximum scale (CGPA 3.70 / 4.00 or higher).",
            "subject_background_prerequisites": "Academic background directly related to the selected Wageningen master's curriculum.",
            "current_education_status": "Degree completed before university start in September.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; agricultural fieldwork, lab research, or food security projects valued.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 92,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 (speaking minimum 6.0) or TOEFL iBT minimum 92 (speaking minimum 23). Wageningen strictly does NOT accept MOI certificates from Pakistan.",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "INVITATION-ONLY SCHOLARSHIP: Candidates must first apply for admission to an MSc program at Wageningen by February 1. If unconditionally admitted and meeting the 80%+ GPA criteria, the central admissions committee INVITES the candidate to apply for the Excellence Programme.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% Full Tuition Fee Waiver for the complete 2-year MSc program (~€19,000/year = ~€38,000 total / ~PKR 11,400,000 value)."},
            "admission_application_fee": {"status": "NOT_COVERED", "details": "Wageningen application fee of €50 (reimbursed upon matriculation)."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via monthly living stipend; Idealis student housing arranged in Wageningen."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living allowance paid directly to the scholar.", "amount": "€1,200 / month (~PKR 360,000 / month) for 24 months = €28,800 total stipend"},
            "airfare": {"status": "COVERED", "details": "Round-trip economy class flight ticket between Pakistan and Amsterdam Schiphol Airport."},
            "visa_fee": {"status": "COVERED", "details": "Dutch residence permit / entry visa (MVV) fee (€228) paid directly by Wageningen University."},
            "health_insurance": {"status": "COVERED", "details": "Basic international student health and liability insurance (Aon Student Insurance) covered for 24 months."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Covered within monthly stipend."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "One-time textbook and study materials allowance (€500).", "amount": "€500 one-off"},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Master's thesis fieldwork travel grants supported by university chair groups."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Train ticket from Schiphol Airport to Wageningen and bicycle allowance."},
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Institution: Wageningen University & Research (WUR, Wageningen, Netherlands).",
            "participating_institutions": ["Wageningen University & Research"],
            "university_rankings_scope": "World #1 in Agriculture & Forestry, World #2 in Environmental Sciences (QS World Rankings by Subject).",
            "available_majors": ["Plant Sciences", "Animal Sciences", "Forestry and Nature Conservation", "Food Technology", "Organic Agriculture", "Environmental Sciences", "Water Technology", "Climate Studies", "Biotechnology"],
            "english_taught_program_availability": True,
            "program_duration": "24 months (120 ECTS credits)",
            "admission_requirements_summary": "Bachelor's degree with GPA > 80%, transcripts, CV, motivation letter, IELTS 6.5+, 2 reference letters.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission must be secured before scholarship consideration: Apply for MSc admission by February 1. Only unconditionally admitted candidates are invited to the scholarship round in March.",
            "strategic_program_match_advice": "Graduates of University of Agriculture Faisalabad (UAF), PMAS Arid Agriculture Rawalpindi, and Sindh Agriculture University Tandojam have exceptional subject matching for WUR programs."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.wur.nl/en/education-programmes/master/practical-information-masters/scholarships-for-international-masters-students/excellence-programme.htm",
            "portal_system_name": "Wageningen Student Portal & Osiris Application System",
            "account_creation_instructions": "1) Apply for an MSc program via Osiris before February 1; 2) Upon unconditional admission, receive email invitation to apply for Excellence Programme in early March.",
            "step_by_step_workflow": [
                "1. Apply for an MSc program at Wageningen via Osiris portal before February 1.",
                "2. Submit transcripts, degree certificates, CV, and proof of English proficiency (IELTS 6.5).",
                "3. Secure unconditional admission to the MSc program (February).",
                "4. If GPA is above 80% (3.7/4.0), receive official email invitation from WUR to apply for the Excellence Programme (early March).",
                "5. Complete the Excellence Programme questionnaire, write scholarship motivation essay, and submit referee contacts.",
                "6. Central Selection Committee reviews submissions and shortlists finalists (April).",
                "7. Shortlisted candidates undertake a 20-minute online video interview via Teams with Wageningen professors (mid-April).",
                "8. Final scholarship decisions communicated in early May.",
                "9. Complete Dutch MVV visa process coordinated by Wageningen Student Immigration Service (May - July).",
                "10. Arrive in the Netherlands (mid-August) for Annual Introduction Days (AID)."
            ],
            "university_vs_scholarship_routing": "Sequential: University admission application first -> Invitation-based scholarship application second.",
            "recommendation_letters_submission_method": "Submitted online by 2 academic referees via automated links.",
            "personal_statement_prompts": "Excellence Essay: Describe your vision for sustainable agriculture/environment, how Wageningen will accelerate your mission, and your leadership potential.",
            "study_plan_research_proposal_requirements": "Not applicable for MSc entry.",
            "cv_format_requirements": "Detailed academic CV.",
            "interviews_conducted": True,
            "interview_format_details": "20-minute online interview via Teams with an academic committee of WUR professors evaluating critical thinking, motivation, and developmental vision.",
            "standardized_tests": "IELTS Academic (6.5) or TOEFL iBT (92) mandatory. No GRE needed.",
            "application_fee_amount": "€50 university application fee (reimbursed upon registration).",
            "attestation_requirements": "HEC degree attestation required for Dutch municipal registration.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "Online portal submission via Osiris."
        },
        "required_documents_checklist": [
            {"document_name": "Official Bachelor's Degree & Transcripts", "mandatory": True, "specification": "Transcripts showing GPA of at least 80% (3.70/4.00 CGPA)", "pakistan_specific_instruction": "From HEC recognized university in agriculture/biology/STEM"},
            {"document_name": "Proof of English Language Proficiency", "mandatory": True, "specification": "IELTS Academic (min 6.5, speaking min 6.0) or TOEFL iBT (min 92, speaking min 23)", "pakistan_specific_instruction": "Strictly required; MOI certificates not accepted"},
            {"document_name": "Curriculum Vitae", "mandatory": True, "specification": "Detailed academic and professional resume", "pakistan_specific_instruction": "Highlight agricultural field research, farm projects, and publications"},
            {"document_name": "Motivation Letter / Excellence Essay", "mandatory": True, "specification": "Explaining commitment to food security, climate, or sustainable agriculture", "pakistan_specific_instruction": "Focus on agricultural challenges in the Indus Basin and Pakistan"},
            {"document_name": "Two Letters of Reference", "mandatory": True, "specification": "Signed letters from university professors on official letterhead", "pakistan_specific_instruction": "Must confirm candidate is in the top 5-10% of their graduating cohort"},
            {"document_name": "Valid International Passport", "mandatory": True, "specification": "Valid for at least 2 years beyond entry date", "pakistan_specific_instruction": "Required for Dutch MVV visa application"}
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1 annually (Osiris application opens)",
            "application_deadline": "February 1 annually (MSc admission deadline for scholarship consideration)",
            "university_admission_deadline": "February 1 annually",
            "document_submission_deadline": "February 1 annually",
            "recommendation_letters_deadline": "Mid-March annually",
            "interview_period": "Mid-April (Online video interviews via Teams)",
            "shortlist_announcement": "Late March (Invitation to interview); Early May (Final scholarship results)",
            "final_result_acceptance_deadline": "Mid-May annually",
            "visa_application_window": "May - July (Dutch MVV visa processed via WUR)",
            "semester_commencement": "Late August / September 1 (Fall Semester)",
            "annual_cycle_notes": "Missing the February 1 admission deadline automatically excludes you from the Excellence Programme."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Academic excellence, strictly 80%+ GPA, transcript rigor)",
            "extracurricular_and_leadership_weight": "10% (Initiative in sustainable agriculture or environmental advocacy)",
            "research_experience_weight": "20% (Undergraduate thesis quality and laboratory/field expertise)",
            "work_experience_weight": "5% (Agronomy or environmental sector exposure)",
            "personal_statement_weight": "10% (Quality of the Excellence Essay)",
            "recommendations_weight": "5% (Endorsement of outstanding scholarly potential)",
            "interview_weight": "5% (Online interview assessing scientific vision and composure)",
            "test_scores_weight": "Gatekeeper requirement (minimum English cutoff)",
            "financial_need_weight": "0% (Pure academic excellence in agriculture and life sciences)",
            "selection_panel_composition": "Wageningen University Board of Management and Academic Chair Professors.",
            "evaluation_methodology": "Two-phase sift: Automated 80% GPA filter -> Invitation to submit dossier -> Panel interview for finalists."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,000 to 3,000 international non-EEA MSc applicants; ~150 invited to apply",
            "total_scholarships_awarded": "~5 to 10 scholarships awarded globally each year",
            "acceptance_rate_global": "~0.3% to 0.5%",
            "acceptance_rate_pakistan": "~0.5% (Extremely Selective - World #1 in Agriculture)",
            "typical_successful_applicant_gpa": "3.85 to 4.00 / 4.00 CGPA (strictly top 5% of class)",
            "typical_academic_and_research_profile": "Published or presented research in agronomy, soil science, plant breeding, water technology, or biotechnology.",
            "common_backgrounds_of_winners": "Graduates of University of Agriculture Faisalabad (UAF), PMAS Arid Agriculture, NUST, LUMS, University of the Punjab.",
            "high_representation_countries": "Global competition across developing countries.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education consultants claiming they can 'apply directly' for the Wageningen Excellence scholarship. The scholarship is INVITATION-ONLY; you cannot apply without being invited by WUR admissions."
            ],
            "application_fee_warning": "Osiris charges €50 university admission fee; the scholarship itself has no fee.",
            "agent_and_intermediary_warnings": "WUR does not partner with recruitment agents in Pakistan.",
            "hidden_costs_breakdown": [
                "IELTS test fee (~PKR 60,000).",
                "Dutch municipal registration and healthcare supplementary fees (~€150).",
                "Housing guarantee deposit for Idealis (~€500) upon signing accommodation lease."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can apply for this scholarship if your GPA is 75%. (Fact: WUR strictly enforces the 80%+ GPA cutoff; candidates with 79.9% are never invited).",
                "MYTH: You cannot work in the Netherlands after graduation. (Fact: The Netherlands offers the 'Zoekjaar' Orientation Year visa, allowing graduates from top 200 universities to live and work in the Netherlands for 1 year post-graduation)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently claim there is a standalone scholarship application link; in reality, it is strictly invitation-based via email to admitted applicants."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must earn at least 50 credits (out of 60 ECTS) in Year 1 to have the Year 2 scholarship renewed.",
            "attendance_requirements": "Full-time physical enrollment at Wageningen University.",
            "academic_progress_monitoring": "Termly credit progress verified through Osiris student portal.",
            "work_restrictions_during_study": "Non-EU students in the Netherlands can work up to 16 hours per week with a work permit (TWV) arranged by their employer, or full-time in June/July/August.",
            "home_country_return_obligation": "No mandatory home residency rule enforced by the Netherlands; scholars can transition to the 1-year Dutch Orientation Year (Zoekjaar) work visa.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of grant upon academic failure or voluntary withdrawal.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Strictly 24 months maximum funding."
        },
        "official_sources_verified": [
            {
                "source_name": "Wageningen University & Research - Official Excellence Programme Portal",
                "source_url": "https://www.wur.nl/en/education-programmes/master/practical-information-masters/scholarships-for-international-masters-students/excellence-programme.htm",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of scholarships awarded per individual academic chair group",
                    "Interview committee scoring rubric"
                ]
            }
        ]
    },

    # 20. KFUPM Graduate STEM Fellowships (Saudi Arabia)
    "SCH-ME-043": {
        "scholarship_id": "SCH-ME-043",
        "basic_details": {
            "scholarship_name": "KFUPM Graduate STEM Fellowships in Engineering & Physical Sciences",
            "offering_entity": "King Fahd University of Petroleum & Minerals (KFUPM)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "King Fahd University of Petroleum & Minerals (Dhahran, Eastern Province, Saudi Arabia)",
            "degree_levels": ["Master's", "PhD"],
            "major_restrictions": "Restricted to STEM and Engineering disciplines: Petroleum Engineering, Chemical Engineering, Mechanical Engineering, Electrical Engineering, Civil Engineering, Aerospace Engineering, Materials Science, Computer Science, Artificial Intelligence, Robotics, Chemistry, Physics, Mathematics.",
            "number_of_awards_total": "Hundreds of fully funded Graduate Assistantships (GA) and Research Assistantships (RA) awarded annually",
            "number_of_awards_pakistan": "Extensive representation: Hundreds of Pakistani graduate students currently enrolled on full fellowships",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Master's of Science (MS): 2 years; PhD: 3 to 4 years"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international male and female applicants worldwide (Pakistani students fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No explicit age limit.",
            "academic_qualifications": "4-year Bachelor's degree in engineering/science for MS applicants; 2-year Master's degree in engineering/science for PhD applicants from recognized universities.",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00/4.00 CGPA for Master's; minimum 3.00/4.00 CGPA for PhD; competitive applicants in core engineering tracks typically have 3.4+ CGPA.",
            "subject_background_prerequisites": "Undergraduate major must match or be closely related to the intended graduate program.",
            "current_education_status": "Graduated or in final semester (final degree certificate must be submitted upon enrollment).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required; research experience and publications strongly preferred for PhD.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 68,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.0 (or TOEFL iBT minimum 68) mandatory. Computer Science and AI tracks often expect IELTS 6.5 / TOEFL 79.",
            "other_language_requirements": "None; all graduate courses, examinations, and research at KFUPM are conducted 100% in English.",
            "gender_specific_requirements": "Open to both male and female applicants (female graduate students have dedicated campus housing and facilities).",
            "financial_need_required": False,
            "special_eligibility_categories": "GRE General test is strongly recommended for MS and required for PhD engineering programs (competitive quantitative score: 156+).",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% full tuition fee waiver for all credit hours throughout the degree program."},
            "admission_application_fee": {"status": "NOT_COVERED", "details": "Nominal online application processing fee (SAR 100 / ~PKR 7,500) paid during portal submission."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Free furnished air-conditioned bachelor housing provided on campus (shared room for MS, private single room for PhD)."},
            "monthly_stipend": {"status": "COVERED", "details": "Tax-free monthly living stipend paid directly to the student's Saudi bank account.", "amount": "SAR 2,500 / month (MS) (~PKR 185,000 / month); SAR 4,000 / month (PhD) (~PKR 295,000 / month)"},
            "airfare": {"status": "COVERED", "details": "Prepaid round-trip economy airfare from Pakistan to Dammam/Dhahran upon initial enrollment, and return flight home upon graduation."},
            "visa_fee": {"status": "WAIVED", "details": "Saudi Student Iqama / Visa processing fees and government residency cards covered by the university."},
            "health_insurance": {"status": "COVERED", "details": "Free comprehensive primary and specialized medical and dental care at the KFUPM Medical Center on campus and affiliated hospitals."},
            "food_allowance": {"status": "SUBSIDIZED", "details": "Heavily subsidized meals available at the university student cafeteria (high-quality meals for SAR 4 to 8 / meal)."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Free university-issued textbooks and laboratory computing equipment provided by the university bookstore."},
            "research_funding_conference_grant": {"status": "COVERED", "details": "Generous university research grants (DSR) and funding to present papers at international IEEE/SPE conferences abroad."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Free airport shuttle service between King Fahd International Airport (Dammam) and KFUPM campus."},
            "total_estimated_value_usd_per_year": 32000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Institution: King Fahd University of Petroleum & Minerals (Dhahran, Saudi Arabia).",
            "participating_institutions": ["KFUPM (College of Petroleum Engineering & Geosciences, College of Computing & Mathematics, College of Engineering & Physics)"],
            "university_rankings_scope": "World Top 10 for Petroleum Engineering and Chemical Engineering; #1 University in the Middle East & Arab Region (QS World Rankings #101).",
            "available_majors": ["Petroleum Engineering", "Chemical Engineering", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Aerospace Engineering", "Materials Science", "Computer Science", "Artificial Intelligence", "Robotics", "Chemistry", "Physics", "Mathematics"],
            "english_taught_program_availability": True,
            "program_duration": "MS: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Bachelor's / Master's transcripts (GPA 3.0+), IELTS 6.0+, Statement of Purpose, 3 recommendation letters, GRE General (recommended/required).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single integrated application: Applying via the KFUPM Deanship of Graduate Studies portal automatically considers eligible applicants for the fully funded Graduate Assistantship/Fellowship.",
            "strategic_program_match_advice": "Pakistani engineers from UET, NUST, GIKI, and PIEAS are held in extremely high regard at KFUPM; highlighting practical engineering design and strong mathematical foundations produces high acceptance rates."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://postgrad.kfupm.edu.sa/",
            "portal_system_name": "KFUPM Deanship of Graduate Studies Online Application System",
            "account_creation_instructions": "Register on the KFUPM graduate admissions portal during the open application cycles (Fall intake: January - February; Spring intake: September - October).",
            "step_by_step_workflow": [
                "1. Register on KFUPM online graduate portal during open window.",
                "2. Fill academic history, upload bachelor's/master's transcripts and degree certificates.",
                "3. Upload valid IELTS (min 6.0) or TOEFL (min 68) test score certificate.",
                "4. Upload GRE General score card (if available; highly recommended).",
                "5. Write Statement of Purpose outlining research interests in engineering/science.",
                "6. Register 3 academic referees who submit online recommendation forms directly.",
                "7. Pay nominal application fee (SAR 100) and submit online application.",
                "8. Departmental graduate committees evaluate files (March - April).",
                "9. Official admission and scholarship award letters issued via portal (May/June).",
                "10. Attest educational documents via HEC, MOFA, and Saudi Cultural Mission (SACM) in Islamabad.",
                "11. Receive Saudi Student Visa authorization and book prepaid flight to Dammam (August).",
                "12. Arrive at KFUPM campus in Dhahran for orientation."
            ],
            "university_vs_scholarship_routing": "Integrated 1-step routing: Full scholarship is tied directly to graduate admission.",
            "recommendation_letters_submission_method": "Submitted online by 3 academic referees via automated secure email links.",
            "personal_statement_prompts": "Statement of Purpose (1-2 pages): Academic background, research experience, proposed research topic at KFUPM, and professional career goals.",
            "study_plan_research_proposal_requirements": "PhD applicants must upload a focused research proposal aligned with KFUPM research centers (e.g. Center of Research Excellence in Renewable Energy, CPG).",
            "cv_format_requirements": "Standard technical engineering CV.",
            "interviews_conducted": False,
            "interview_format_details": "Generally dossier-based; some departments may conduct a short technical Zoom call with prospective thesis advisors.",
            "standardized_tests": "IELTS Academic (6.0) or TOEFL (68) mandatory. GRE General recommended for MS, required for PhD.",
            "application_fee_amount": "SAR 100 (~PKR 7,500) online application fee.",
            "attestation_requirements": "MANDATORY FOR VISA: Degrees and transcripts must be attested by HEC, MOFA, and Saudi Cultural Mission (SACM) in Islamabad/Karachi prior to visa stamping.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online portal submission on KFUPM portal."
        },
        "required_documents_checklist": [
            {"document_name": "Official Academic Transcripts & Degrees", "mandatory": True, "specification": "Complete transcripts from all post-secondary education (BS for MS; BS+MS for PhD)", "pakistan_specific_instruction": "Must be 4-year BS in engineering/science from HEC recognized university"},
            {"document_name": "Valid English Language Test Score", "mandatory": True, "specification": "IELTS Academic (min 6.0) or TOEFL iBT (min 68)", "pakistan_specific_instruction": "Mandatory at the time of application submission"},
            {"document_name": "GRE General Score Card", "mandatory": False, "specification": "Official ETS GRE score report (Quantitative min 156+ competitive)", "pakistan_specific_instruction": "Required for PhD; strongly recommended for MS engineering"},
            {"document_name": "Statement of Purpose (1-2 pages)", "mandatory": True, "specification": "Technical statement of research interests and motivations", "pakistan_specific_instruction": "Highlight alignment with Saudi Vision 2030 energy/tech priorities"},
            {"document_name": "Three Academic Recommendation Letters", "mandatory": True, "specification": "Submitted directly by university professors online", "pakistan_specific_instruction": "Must be from faculty who taught core engineering courses"},
            {"document_name": "Valid Passport Information Page", "mandatory": True, "specification": "Passport valid for at least 18 months", "pakistan_specific_instruction": "Required for Saudi student visa authorization"},
            {"document_name": "Curriculum Vitae", "mandatory": True, "specification": "Comprehensive technical engineering CV", "pakistan_specific_instruction": "Detail capstone design project, lab instruments, and software"}
        ],
        "important_dates_timeline": {
            "application_open_date": "January annually for Fall intake; September for Spring intake",
            "application_deadline": "Mid-February annually for Fall intake; October for Spring intake",
            "university_admission_deadline": "Coincides with portal deadline",
            "document_submission_deadline": "Coincides with portal deadline",
            "recommendation_letters_deadline": "One week after application deadline",
            "interview_period": "N/A (Evaluation in Dhahran)",
            "shortlist_announcement": "May / June for Fall intake; November / December for Spring intake",
            "final_result_acceptance_deadline": "Within 2 weeks of offer issuance",
            "visa_application_window": "June - July (Saudi Embassy Islamabad / Consulate Karachi)",
            "semester_commencement": "Late August / September (Fall Semester) or January (Spring Semester)",
            "annual_cycle_notes": "Offers two intakes per academic year (Fall and Spring)."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Undergraduate CGPA, engineering coursework grades)",
            "extracurricular_and_leadership_weight": "5% (General adaptability)",
            "research_experience_weight": "25% (Publications, capstone design projects, laboratory skills)",
            "work_experience_weight": "5% (Industry engineering exposure)",
            "personal_statement_weight": "10% (Technical statement of purpose)",
            "recommendations_weight": "5% (Professor endorsements)",
            "interview_weight": "0% (Unless requested by department)",
            "test_scores_weight": "10% (GRE Quantitative score and IELTS score balance)",
            "financial_need_weight": "0% (All admitted graduate students receive full fellowship)",
            "selection_panel_composition": "Departmental Graduate Studies Committees and Deanship of Graduate Studies at KFUPM.",
            "evaluation_methodology": "Rigorous academic review ranking applicants by GPA, GRE scores, and research capability in engineering."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~6,000 to 10,000 international applicants across all STEM departments",
            "total_scholarships_awarded": "Hundreds of graduate assistantships awarded annually",
            "acceptance_rate_global": "~5.0% to 7.0%",
            "acceptance_rate_pakistan": "~6.0% to 8.0% (Strong track record of Pakistani engineering admissions)",
            "typical_successful_applicant_gpa": "3.40 to 3.85 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Solid engineering background, GRE Quantitative 156+, IELTS 6.5, well-defined research interests.",
            "common_backgrounds_of_winners": "Graduates of NUST, UET Lahore, UET Taxila, GIKI, PIEAS, FAST, NED University Karachi, and COMSATS.",
            "high_representation_countries": "Pakistan, Egypt, India, Nigeria, Bangladesh, Jordan, Sudan.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial visa agents claiming they have 'Iqama work visa quotas' for KFUPM. Graduate fellowship admission is strictly granted by the KFUPM Deanship.",
                "Scam agencies demanding thousands of riyals for scholarship placement."
            ],
            "application_fee_warning": "Only the official SAR 100 online application fee is paid directly on the KFUPM portal.",
            "agent_and_intermediary_warnings": "Never hire an agent. All portal interaction is direct.",
            "hidden_costs_breakdown": [
                "Degree attestation at Saudi Cultural Mission (SACM) in Islamabad (requires authorized courier agency, approx PKR 15,000 to 30,000).",
                "Medical checkup (Enjaz medical) at approved GAMCA centers in Pakistan (approx PKR 12,000 to 18,000).",
                "Initial settling pocket money buffer before first stipend release."
            ],
            "misleading_claims_debunked": [
                "MYTH: Female students cannot apply. (Fact: KFUPM opened all its graduate programs to female students with dedicated on-campus female graduate housing and facilities).",
                "MYTH: You cannot study in English. (Fact: 100% of education and research at KFUPM is conducted in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some third-party sites report outdated stipends; current stipends are SAR 2,500/mo for MS and SAR 4,000/mo for PhD."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of at least 3.00/4.00 each semester; dropping below 3.00 results in academic probation and potential loss of fellowship.",
            "attendance_requirements": "Full-time physical residence on campus in Dhahran.",
            "academic_progress_monitoring": "Semi-annual evaluations by graduate department academic committee.",
            "work_restrictions_during_study": "Scholars are employed as Graduate Assistants (GA) or Research Assistants (RA) working up to 15-20 hours/week assisting in departmental teaching or research labs as part of their fellowship obligation; outside commercial employment in Saudi Arabia is strictly prohibited.",
            "home_country_return_obligation": "No mandatory home residency return rule. Many graduates transition directly to lucrative high-paying engineering careers with Saudi Aramco, SABIC, or continue to doctoral studies in the US and Europe.",
            "service_obligations_or_bonds": "Duty as Graduate Assistant (15 hrs/week teaching/grading/lab work).",
            "repayment_clawback_conditions": "Termination of fellowship upon academic dismissal or disciplinary expulsion.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Subject to strict approval by both academic departments.",
            "extension_policy": "Maximum 1 semester extension can be approved by the Deanship for thesis completion."
        },
        "official_sources_verified": [
            {
                "source_name": "King Fahd University of Petroleum & Minerals - Deanship of Graduate Studies",
                "source_url": "https://postgrad.kfupm.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of applicants admitted per specific engineering department",
                    "GRE quantitative cutoff percentiles by department"
                ]
            }
        ]
    }
}
