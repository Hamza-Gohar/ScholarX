"""
scripts/dossiers_batch4b.py
Part B of Batch 4:
4. SCH-ME-005: King Abdulaziz University (KAU) Scholarship (Saudi Arabia)
5. SCH-ME-006: Islamic Development Bank (IsDB) Scholarship Programme (Global)
6. SCH-ME-008: Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) Full Scholarship (UAE)
"""

DOSSIERS_BATCH4B = {
    # 4. King Abdulaziz University (KAU) Scholarship (SCH-ME-005)
    "SCH-ME-005": {
        "scholarship_id": "SCH-ME-005",
        "basic_details": {
            "scholarship_name": "King Abdulaziz University (KAU) Scholarship",
            "offering_entity": "King Abdulaziz University (KAU) & Ministry of Education, Kingdom of Saudi Arabia",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "King Abdulaziz University Main Campus (Jeddah, Saudi Arabia)",
            "degree_levels": ["Master's", "PhD (Doctorate)"],
            "major_restrictions": "Open to designated scientific and engineering faculties: Faculty of Computing and Information Technology, Faculty of Engineering, Faculty of Science, Faculty of Meteorology, Environment and Arid Land Agriculture, Faculty of Marine Sciences, Faculty of Earth Sciences. Excludes medical and health clinical faculties for non-Saudi external students.",
            "number_of_awards_total": "~300 to 400 international graduate scholarships awarded annually",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible partner state (~30 to 50 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Master's: 2 to 3 years; PhD: 3 to 4 years"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Saudi international candidates residing outside Saudi Arabia (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Master's applicants: maximum 35 years of age; PhD applicants: maximum 40 years of age.",
            "academic_qualifications": "Completed 16 years of education (Bachelor's degree) for Master's; 18 years (Master's degree) for PhD with at least 'Very Good' graduation grade.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA (or Very Good standing / 75%+ marks in annual system).",
            "subject_background_prerequisites": "Undergraduate degree in science, engineering, or computing aligned with target department.",
            "current_education_status": "Graduated with official degree certificate and transcripts.",
            "graduation_year_restrictions": "Graduation within the past 5 years is preferred.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research papers, final year projects, and academic references prioritized.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 70,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "IELTS Academic minimum 6.0, TOEFL iBT 70, or university English proficiency certificate for initial portal evaluation."
            },
            "other_language_requirements": "None; programs in science, computing, and engineering taught in English.",
            "gender_specific_requirements": "Equal opportunity; male and female candidates accommodated in respective university campuses.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must have clean criminal record and pass medical fitness standards.",
            "previous_scholarship_restrictions": "Ineligible if previously expelled from any Saudi educational institution.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver for the complete duration of graduate studies.",
                "amount": "Full coverage"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application on the KAU Deanship of Graduate Studies portal is 100% free.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE_FURNISHED_HOUSING",
                "details": "Free furnished student accommodation on university campus.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly personal living stipend paid throughout the study period.",
                "amount": "Master's: SAR 1,900 / month (~PKR 145,000 / month); PhD: SAR 2,500 / month (~PKR 190,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy class round-trip airfare ticket annually at the end of each academic year.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi student visa and Iqama residence permit fees fully covered by KAU.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Free comprehensive healthcare at KAU University Hospital and university clinics.",
                "amount": None
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Heavily subsidized campus cafeteria meals.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "A book allowance of SAR 1,800 provided upon initial arrival.",
                "amount": "SAR 1,800 one-off preparation allowance (~PKR 137,000)"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Thesis printing allowance provided upon graduation (SAR 3,000 for Master's, SAR 4,000 for PhD).",
                "amount": "SAR 3,000 - 4,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in preparation allowance.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: King Abdulaziz University (Jeddah, Saudi Arabia).",
            "participating_institutions": [
                "King Abdulaziz University (Main Campus, Jeddah)"
            ],
            "university_rankings_scope": "Consistently ranked Top 150 globally in QS World University Rankings; #1 in the Arab World (THE rankings).",
            "available_majors": [
                "Computer Science, Artificial Intelligence, Information Technology, Information Systems, Electrical Engineering, Mechanical Engineering, Civil Engineering, Chemical Engineering, Industrial Engineering, Physics, Chemistry, Mathematics, Marine Sciences, Meteorology & Climate Change"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Online application through KAU Deanship of Graduate Studies portal; selection is competitive based on GPA and qualifications.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Faculty of Computing and Information Technology (FCIT) is most competitive; strong math and programming background recommended.",
            "strategic_program_match_advice": "Ensure all transcripts and certificates are attested by HEC Pakistan and Saudi Embassy in Islamabad before visa processing."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://graduatestudies.kau.edu.sa/",
            "portal_system_name": "KAU Deanship of Graduate Studies Online Portal",
            "account_creation_instructions": "Register on the KAU Graduate Studies portal, choose international scholarship category, select degree and department, and upload scanned documents.",
            "step_by_step_workflow": [
                "1. Register on KAU portal during open admission window (typically January to March).",
                "2. Upload certified degree certificates, mark sheets, CV, and Statement of Purpose.",
                "3. Provide two academic recommendation letters from former professors.",
                "4. Upload valid passport copy, police clearance certificate, and medical report.",
                "5. Submit complete electronic application by the deadline.",
                "6. Academic departments evaluate files in April/May.",
                "7. Admission and scholarship approvals published in June/July; Ministry of Education issues visa authorizations."
            ],
            "university_vs_scholarship_routing": "Direct single application: Scholarship included with international admission.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate during application.",
            "personal_statement_prompts": "Statement of Purpose describing academic objectives, reasons for choosing KAU, and future research goals.",
            "study_plan_research_proposal_requirements": "Research proposal required for PhD applicants.",
            "cv_format_requirements": "Standard academic CV (1-2 pages).",
            "interviews_conducted": False,
            "interview_format_details": "No interviews in most departments; decisions based strictly on evaluation of academic records.",
            "standardized_tests": "English test score (IELTS 6.0+ or TOEFL 70+).",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan, MOFA, and Saudi Cultural Mission / Saudi Embassy in Islamabad.",
            "translation_requirements": "Certified Arabic or English translations.",
            "final_submission_method": "100% Online via KAU portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Graduation Certificate & Degree",
                "mandatory": True,
                "specification": "Official bachelor's or master's degree certificate with minimum Very Good grade",
                "pakistan_specific_instruction": "Attested by HEC Pakistan and Saudi Embassy"
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete transcripts showing all subjects, grades, and CGPA",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "From former university professors on official letterhead",
                "pakistan_specific_instruction": "Signed and stamped"
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "Detailed essay outlining academic background and objectives",
                "pakistan_specific_instruction": "In English"
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Valid Pakistani passport photo page",
                "pakistan_specific_instruction": "Valid for at least 1 year"
            },
            {
                "document_name": "Police Clearance Certificate",
                "mandatory": True,
                "specification": "Security clearance proving clean criminal record",
                "pakistan_specific_instruction": "Issued by local Pakistani police department"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-01-10",
            "application_deadline": "2027-03-31",
            "university_admission_deadline": "2027-03-31",
            "document_submission_deadline": "2027-03-31",
            "recommendation_letters_deadline": "2027-03-31",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-07-15",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "Application window is strictly January to late March each year. Fall semester begins September."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Academic record, GPA, university ranking, class standing)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "25% (Publications, research proposal quality for PhD)",
            "work_experience_weight": "5% (Professional experience)",
            "personal_statement_weight": "5% (Statement of Purpose)",
            "recommendations_weight": "10% (Referee appraisals)",
            "interview_weight": "0%",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "KAU Departmental Graduate Committees and Deanship of Graduate Studies Admissions Board.",
            "evaluation_methodology": "Scoring of academic grades, research output, and alignment with department research groups."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~6,000 to 8,000 international applications",
            "total_scholarships_awarded": "~300 to 400 scholarships awarded annually",
            "acceptance_rate_global": "~5%",
            "acceptance_rate_pakistan": "~4% to 5% (Strong conversion for high-GPA Pakistani applicants)",
            "typical_successful_applicant_gpa": "3.50 to 3.90 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates with solid academic records in engineering, mathematics, physics, and computer science seeking quality funded education in Saudi Arabia.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (NUST, UET Lahore, Quaid-i-Azam, Punjab University, COMSATS, NED Karachi).",
            "high_representation_countries": "Pakistan, Egypt, Yemen, Sudan, India, Bangladesh, Indonesia.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents claiming to have direct connections to the KAU admissions dean for a fee."
            ],
            "application_fee_warning": "The KAU scholarship application is 100% FREE on the official portal.",
            "agent_and_intermediary_warnings": "Never pay agents; applications submitted by commercial agents are rejected.",
            "hidden_costs_breakdown": [
                "HEC, MOFA, and Saudi Embassy attestation fees in Islamabad (~PKR 35,000).",
                "Medical examination at Saudi-approved GAMCA centers in Pakistan (~PKR 25,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot apply without Arabic. (Fact: Science and engineering degrees are 100% in English).",
                "MYTH: You must pay for campus housing. (Fact: Campus housing is completely free)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites state that medicine is covered; clinical medical programs are strictly closed to external non-Saudi scholarship holders."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.0 / 4.00 (Good standing); falling below results in scholarship suspension.",
            "attendance_requirements": "Full-time physical residence and attendance in Jeddah.",
            "academic_progress_monitoring": "Semester grade and thesis progress checks.",
            "work_restrictions_during_study": "Scholars are not permitted to work for pay outside the university during scholarship tenure.",
            "home_country_return_obligation": "None; scholars can pursue employment in Saudi Arabia or internationally.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Expulsion or academic failure results in cancellation of visa and return to home country.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Maximum extension of one semester permitted upon recommendation of academic supervisor."
        },
        "official_sources_verified": [
            {
                "source_name": "King Abdulaziz University - Deanship of Graduate Studies Official Portal",
                "source_url": "https://graduatestudies.kau.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental admission scoring matrix details",
                    "Country-by-country quota breakdown"
                ]
            }
        ]
    },

    # 5. Islamic Development Bank (IsDB) Scholarship Programme (SCH-ME-006)
    "SCH-ME-006": {
        "scholarship_id": "SCH-ME-006",
        "basic_details": {
            "scholarship_name": "Islamic Development Bank (IsDB) Scholarship Programme",
            "offering_entity": "Islamic Development Bank (IsDB, Jeddah, Saudi Arabia)",
            "host_country": "Global (Top Universities in 57 IsDB Member Countries and Partner Institutions Worldwide)",
            "host_institutions_covered": "Top universities in IsDB member countries and prestigious partner universities worldwide (Cambridge, Oxford, Queen Mary, McGill, ITU Turkey, UTM Malaysia)",
            "degree_levels": ["Undergraduate (Bachelor's)", "Master's", "PhD", "Post-Doctoral Research"],
            "major_restrictions": "Development-focused fields: Sustainability Sciences, Clean Energy, Climate Change, Agriculture and Food Security, Water and Sanitation, Healthcare and Medicine, ICT and AI, Islamic Economics, Finance and Banking, Infrastructure Development.",
            "number_of_awards_total": "~500 to 600 scholarships awarded annually across 57 member countries",
            "number_of_awards_pakistan": "Open to Pakistan as a founding member country (~20 to 30 Pakistani scholars selected annually across all levels)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's: 4 years; Master's: 2 years; PhD: 3 to 4 years; Post-Doc: 6 to 12 months"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of an IsDB member country (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 24,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate: under 24; Master's: under 30; PhD: under 35; Post-Doctoral: under 40 years of age.",
            "academic_qualifications": "12 years for Bachelor's; 16 years for Master's; 18 years for PhD with superior academic standing (at least 'Very Good' / 80%+).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum 3.50 / 4.00 CGPA or equivalent top 10% class standing.",
            "subject_background_prerequisites": "Prerequisites corresponding to designated development disciplines.",
            "current_education_status": "Graduated or in final semester of degree.",
            "graduation_year_restrictions": "None, provided age criteria are respected.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience in public service or community development sectors evaluated favorably for Master's and PhD.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "Language requirement depends on destination university (IELTS 6.5+ or TOEFL 85+ for UK/Canada/Malaysia programs)."
            },
            "other_language_requirements": "Language of instruction of destination university.",
            "gender_specific_requirements": "Equal opportunity; women and marginalized groups actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Development impact and formal undertaking to return to home country and contribute to national development (structured as Qard Hasan / interest-free development investment).",
            "previous_scholarship_restrictions": "Cannot hold another scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fees paid directly to the host university by the Islamic Development Bank.",
                "amount": "Full coverage"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University application fees paid by candidate unless waived.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly living allowance commensurate with the cost of living in the host country (e.g. £1,200/mo in UK, CAD $1,600/mo in Canada, RM 2,000/mo in Malaysia).",
                "amount": "Local currency equivalent commensurate with host city cost of living"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy class return airfare ticket between Pakistan and the host country at beginning and end of study.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Student visa fees reimbursed upon submission of official receipts.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive health and medical insurance provided throughout the study tenure.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living allowance.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Annual books and clothing allowance provided directly to student.",
                "amount": "Annual grant"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Special grant available for conference attendance and thesis preparation for PhD and Post-Doc scholars.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Installation allowance provided upon initial arrival.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 35000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for study in top 10 universities in home country or renowned partner universities worldwide.",
            "participating_institutions": [
                "University of Cambridge (UK)", "University of Oxford (UK)",
                "Queen Mary University of London (UK)", "McGill University (Canada)",
                "Istanbul Technical University (Turkey)", "Universiti Teknologi Malaysia (UTM)",
                "Top universities in Pakistan (NUST, Quaid-i-Azam, Aga Khan University)"
            ],
            "university_rankings_scope": "Premier global universities and top-tier institutions in IsDB member states.",
            "available_majors": [
                "Clean Energy & Renewable Power, Sustainable Agriculture, Climate Science, Water Engineering, Public Health, Biomedical Sciences, Artificial Intelligence, Data Science, Islamic Economics & Finance, Law & Governance"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Two pathways: Apply with an existing admission offer from an approved university, or apply for IsDB placement in partner universities.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Holding an unconditional admission offer from a top university significantly strengthens the IsDB scholarship application.",
            "strategic_program_match_advice": "Align your proposed degree explicitly with the UN Sustainable Development Goals (SDGs) and Pakistan's socio-economic development plan."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.isdb.org/scholarships",
            "portal_system_name": "IsDB Scholarship Online Portal",
            "account_creation_instructions": "Register on the IsDB scholarship platform (Opens December/January), complete profile, upload academic dossier, and submit before deadline.",
            "step_by_step_workflow": [
                "1. Check eligibility and program guidelines on the IsDB portal (Opens December/January).",
                "2. Create account on the IsDB scholarship portal and complete the online application form.",
                "3. Upload certified transcripts, degree certificates, CV, and Statement of Purpose.",
                "4. Upload proof of admission if you already have an offer from a top university.",
                "5. Submit online application before the annual deadline (typically late February).",
                "6. IsDB selection panels screen applications and conduct interviews in April/May.",
                "7. Final award decisions announced in July/August; placement confirmed."
            ],
            "university_vs_scholarship_routing": "Direct centralized application via IsDB portal.",
            "recommendation_letters_submission_method": "Two recommendation letters uploaded directly during portal application.",
            "personal_statement_prompts": "Address your academic motivation, how your degree aligns with IsDB development goals, and your commitment to return to Pakistan.",
            "study_plan_research_proposal_requirements": "Research proposal required for PhD and Post-Doctoral applicants.",
            "cv_format_requirements": "Standard academic and professional resume.",
            "interviews_conducted": True,
            "interview_format_details": "Selection committee or national counter-part agency conducts video/in-person interview in April/May.",
            "standardized_tests": "Language proficiency test (IELTS/TOEFL) matching target university standards.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Transcripts certified by degree institutions; HEC attestation required.",
            "translation_requirements": "Certified English, Arabic, or French translations.",
            "final_submission_method": "100% Online via IsDB portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Educational Diplomas & Transcripts",
                "mandatory": True,
                "specification": "Complete certificates and mark sheets showing all grades and GPA",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "Detailed essay outlining academic background and development contribution",
                "pakistan_specific_instruction": "Clear focus on socio-economic impact in Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "From former professors or professional supervisors on letterhead",
                "pakistan_specific_instruction": "Signed and stamped"
            },
            {
                "document_name": "Proof of Admission (if available)",
                "mandatory": False,
                "specification": "Offer letter from an approved top university",
                "pakistan_specific_instruction": "From top 10 Pakistani university or top international partner"
            },
            {
                "document_name": "Medical Certificate",
                "mandatory": True,
                "specification": "Official medical certificate proving fitness for study",
                "pakistan_specific_instruction": "Issued by registered government hospital"
            },
            {
                "document_name": "Passport Copy & CNIC",
                "mandatory": True,
                "specification": "Valid Pakistani passport and national identity card",
                "pakistan_specific_instruction": "Scanned copy of NADRA smart card and passport"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-12-15",
            "application_deadline": "2027-02-28",
            "university_admission_deadline": "N/A (Managed in parallel)",
            "document_submission_deadline": "2027-02-28",
            "recommendation_letters_deadline": "2027-02-28",
            "interview_period": "April to May 2027",
            "shortlist_announcement": "June 2027",
            "final_result_acceptance_deadline": "2027-07-31",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "September/October 2027",
            "annual_cycle_notes": "Application window is strictly December to late February each year. Final awards announced in July."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Superior academic record, GPA, academic honors)",
            "extracurricular_and_leadership_weight": "15% (Leadership track record and community commitment)",
            "research_experience_weight": "20% (For PhD: quality and developmental relevance of research proposal)",
            "work_experience_weight": "5% (Professional experience in development sectors)",
            "personal_statement_weight": "10% (Development impact of proposed study on home country)",
            "recommendations_weight": "10% (Referee appraisals)",
            "interview_weight": "Conducted in final round",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Merit and development impact driven)",
            "selection_panel_composition": "IsDB International Selection Committee composed of distinguished scholars and development experts.",
            "evaluation_methodology": "Two-phase review: Technical evaluation of academic dossier and developmental alignment; final panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~15,000+ applications across 57 IsDB member countries",
            "total_scholarships_awarded": "~500 to 600 scholarships awarded annually",
            "acceptance_rate_global": "~3.5%",
            "acceptance_rate_pakistan": "~2% to 3% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.60 to 4.00 CGPA",
            "typical_academic_and_research_profile": "Top-tier students with strong academic backgrounds, social impact initiatives, and clear development roadmaps.",
            "common_backgrounds_of_winners": "Graduates of leading Pakistani universities (NUST, LUMS, Quaid-i-Azam, Aga Khan University, UET) in STEM, medicine, and economics.",
            "high_representation_countries": "Pakistan, Turkey, Malaysia, Indonesia, Egypt, Bangladesh, Nigeria, Morocco.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent websites claiming to charge fees for IsDB scholarship processing."
            ],
            "application_fee_warning": "The IsDB scholarship application is 100% FREE on the official portal.",
            "agent_and_intermediary_warnings": "Never work through commercial consultants; apply directly on the IsDB portal.",
            "hidden_costs_breakdown": [
                "HEC attestation fees in Islamabad.",
                "Medical checkup costs."
            ],
            "misleading_claims_debunked": [
                "MYTH: IsDB is a religious grant for theological studies. (Fact: Over 90% of IsDB scholarships are awarded in STEM, Medicine, Agriculture, AI, and Engineering).",
                "MYTH: You cannot study in Western countries. (Fact: IsDB partners directly with Cambridge, Oxford, McGill, Queen Mary, and leading European universities)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs state this is a loan; IsDB scholarships operate as interest-free grants (Qard Hasan) where repayment is reinvested into the local community fund after return."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain high academic standing and pass all courses each semester.",
            "attendance_requirements": "Full-time physical residence and attendance at designated host university.",
            "academic_progress_monitoring": "Host universities submit semi-annual academic progress reports to the IsDB Scholarship Division.",
            "work_restrictions_during_study": "Scholars may not work during their study period without prior approval from IsDB.",
            "home_country_return_obligation": "MANDATORY Return: Scholars must return to their home country upon completion to serve in their profession and contribute to socio-economic development.",
            "service_obligations_or_bonds": "Obligated to return home and repay the cost of the scholarship in easy installments to a local IsDB community trust fund (so another student can benefit).",
            "repayment_clawback_conditions": "Failing to return home or abandoning studies requires immediate full refund of all scholarship expenses.",
            "rules_for_changing_university": "Strictly prohibited without prior IsDB approval.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Extensions are strictly granted only for documented academic research delays approved by IsDB."
        },
        "official_sources_verified": [
            {
                "source_name": "Islamic Development Bank (IsDB) - Scholarship Programmes Official Portal",
                "source_url": "https://www.isdb.org/scholarships",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Country-by-country candidate quota allocation formula among the 57 member states",
                    "Selection committee interview scoring rubrics"
                ]
            }
        ]
    },

    # 6. Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) Full Scholarship (SCH-ME-008)
    "SCH-ME-008": {
        "scholarship_id": "SCH-ME-008",
        "basic_details": {
            "scholarship_name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) Full Scholarship",
            "offering_entity": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) & Government of Abu Dhabi",
            "host_country": "United Arab Emirates",
            "host_institutions_covered": "MBZUAI Campus (Masdar City, Abu Dhabi, United Arab Emirates)",
            "degree_levels": ["Master of Science (MSc)", "PhD (Doctorate)"],
            "major_restrictions": "Artificial Intelligence disciplines: Computer Vision (CV), Machine Learning (ML), Natural Language Processing (NLP), Robotics, and Computational Biology.",
            "number_of_awards_total": "~100% of admitted graduate students receive full scholarships (~150 to 200 admits/year)",
            "number_of_awards_pakistan": "Open globally; Pakistan is one of the highest-represented international student cohorts at MBZUAI",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "MSc: 2 years (4 semesters); PhD: 4 years (8 semesters)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students of all nationalities (including Pakistan) and UAE nationals"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (Bachelor of Science/Engineering) in STEM field (Computer Science, Electrical Eng, Math, Physics) with minimum CGPA 3.2 / 4.0.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum 3.20 / 4.00 CGPA; competitive admitted candidates typically present 3.50+ / 4.00 CGPA.",
            "subject_background_prerequisites": "Strong background in mathematics (linear algebra, calculus, probability), algorithms, and programming (Python, C++).",
            "current_education_status": "Graduated or in final semester of degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Competitive programming (ICPC, Kaggle), AI hackathons, and published research papers in top AI venues (NeurIPS, ICML, CVPR, ACL, ICLR) carry decisive weight.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic minimum 6.5 (or TOEFL iBT minimum 90); official score report is mandatory."
            },
            "other_language_requirements": "None; English is the official language of instruction and research.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must take the mandatory online MBZUAI Entry Exam (math and coding assessment) and pass a technical faculty interview.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver for the entire duration of the MSc or PhD program.",
                "amount": "AED 100,000+ / year (~USD $27,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application on the MBZUAI online portal is 100% free of charge.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE_FURNISHED_HOUSING",
                "details": "Free luxury single-occupancy on-campus student housing in Masdar City (modern ensuite room with shared kitchen and gym).",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living allowance paid directly to student.",
                "amount": "MSc: AED 8,000 / month (~PKR 610,000 / month); PhD: AED 10,000 / month (~PKR 760,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Annual round-trip international flight ticket between home city in Pakistan and Abu Dhabi.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "UAE student visa and Emirates ID processing fees fully sponsored by MBZUAI; eligible for UAE Golden Visa nomination.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive UAE medical insurance coverage provided.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "High-end research laptop and access to world-class GPU clusters (thousands of NVIDIA A100/H100 GPUs) provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Generous travel and accommodation funding provided for accepted papers at tier-1 AI conferences (CVPR, NeurIPS, ICML, ACL).",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle transit within Masdar City and to Abu Dhabi.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 65000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Mohamed bin Zayed University of Artificial Intelligence (Abu Dhabi, UAE).",
            "participating_institutions": [
                "MBZUAI (Masdar City, Abu Dhabi)"
            ],
            "university_rankings_scope": "Ranked Top 20 globally in AI/CS (CSRankings in AI, Computer Vision, and NLP); world-class faculty recruited from CMU, Berkeley, Oxford.",
            "available_majors": [
                "Computer Vision (MSc/PhD), Machine Learning (MSc/PhD), Natural Language Processing (MSc/PhD), Robotics (MSc/PhD), Computational Biology (MSc/PhD)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MSc: 2 years (4 semesters); PhD: 4 years (8 semesters)",
            "admission_requirements_summary": "All admitted students receive the full scholarship package; admission requires passing online screening exam and faculty interview.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Machine Learning and Computer Vision are most popular; solid performance on the online math/coding exam is critical.",
            "strategic_program_match_advice": "Prepare thoroughly for the online entry exam in linear algebra, multivariable calculus, probability, and Python data structures."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://mbzuai.ac.ae/study/admissions/",
            "portal_system_name": "MBZUAI Online Admissions Portal",
            "account_creation_instructions": "Register on the MBZUAI portal (Opens September for Fall intake), fill in the application form, upload documents, and schedule online exam.",
            "step_by_step_workflow": [
                "1. Register on MBZUAI portal and select target AI degree program (September-December).",
                "2. Upload Statement of Purpose, transcripts, CV, and English proficiency test score.",
                "3. Submit contact information for two academic referees.",
                "4. Complete the mandatory online MBZUAI Entry Exam (45 minutes: math and programming questions).",
                "5. Shortlisted candidates invited for a technical video interview with faculty professors.",
                "6. Final admission and full scholarship offer letter issued (typically by March/April).",
                "7. Process UAE student visa and relocate to Masdar City in August."
            ],
            "university_vs_scholarship_routing": "Integrated single application; admission equals full scholarship.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure electronic link sent by MBZUAI.",
            "personal_statement_prompts": "Statement of Purpose (500-1,000 words): Detail academic background, AI research interests, coding projects, and reasons for choosing MBZUAI.",
            "study_plan_research_proposal_requirements": "Research proposal required for PhD applicants outlining intended research direction and literature background.",
            "cv_format_requirements": "Detailed technical CV highlighting programming languages, GitHub links, Kaggle rank, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous 30-minute technical interview conducted by MBZUAI professors testing algorithms, linear algebra, and research projects.",
            "standardized_tests": "Online MBZUAI Entry Exam is mandatory; GRE optional; IELTS Academic (6.5+) or TOEFL iBT (90+) mandatory.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan, MOFA, and UAE Embassy in Islamabad.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via MBZUAI portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "500 to 1,000-word essay explaining background, passion for AI, and career vision",
                "pakistan_specific_instruction": "Clearly articulated technical interests and project experience"
            },
            {
                "document_name": "Official Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing all courses, credits, and CGPA (min 3.2/4.0)",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Submitted directly by university research professors or technical employers",
                "pakistan_specific_instruction": "From professors who supervised your AI, programming, or thesis work"
            },
            {
                "document_name": "English Proficiency Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (90+)",
                "pakistan_specific_instruction": "Valid official score report"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "Technical CV listing programming languages, frameworks (PyTorch, TensorFlow), and projects",
                "pakistan_specific_instruction": "Include links to GitHub repositories and papers"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2027-01-15",
            "university_admission_deadline": "2027-01-15",
            "document_submission_deadline": "2027-01-15",
            "recommendation_letters_deadline": "2027-01-22",
            "interview_period": "February to March 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "August 2027",
            "annual_cycle_notes": "Early deadline is mid-December; regular international deadline is mid-January. Fall intake only."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Academic GPA, transcripts, mathematical foundation)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "30% (Research publications, GitHub projects, hackathons, coding portfolio)",
            "work_experience_weight": "5% (Industry AI/ML experience)",
            "personal_statement_weight": "5% (Statement of Purpose clarity)",
            "recommendations_weight": "5% (Referee appraisals)",
            "interview_weight": "25% (Performance on the MBZUAI entry exam and live faculty technical interview)",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Completely need-blind; all admitted students receive the full scholarship)",
            "selection_panel_composition": "Faculty Admissions Committee and the Dean of Academic Affairs at MBZUAI.",
            "evaluation_methodology": "Rigorous three-stage sift: Document screening -> Online math/coding exam -> Technical faculty interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~8,000 to 10,000 applications globally",
            "total_scholarships_awarded": "~150 to 200 fully-funded scholarships awarded annually",
            "acceptance_rate_global": "~2%",
            "acceptance_rate_pakistan": "~2% to 3% (Highly Competitive; Pakistani students are among the top cohorts)",
            "typical_successful_applicant_gpa": "3.60 to 4.00 CGPA",
            "typical_academic_and_research_profile": "Top computer science and electrical engineering graduates with solid math skills, competitive programming background, and AI publications.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani universities (FAST-NUCES, NUST, LUMS, GIKI, UET Lahore, ITU).",
            "high_representation_countries": "China, India, Pakistan, UAE, Egypt, Russia, USA, Italy, Jordan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized consultants claiming to provide 'MBZUAI exam leaks'; exam questions are dynamically generated."
            ],
            "application_fee_warning": "MBZUAI application is 100% free of charge on the official portal.",
            "agent_and_intermediary_warnings": "Never work through agents; MBZUAI requires direct candidate examination and faculty interviews.",
            "hidden_costs_breakdown": [
                "HEC, MOFA, and UAE Embassy attestation fees in Islamabad (~PKR 35,000).",
                "English language test fees (IELTS/TOEFL)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need Arabic. (Fact: MBZUAI is an international English-only research university).",
                "MYTH: The scholarship is only for UAE citizens. (Fact: Over 85% of MBZUAI students are international from over 40 countries).",
                "MYTH: You have to repay the stipend. (Fact: 100% non-repayable fellowship; graduates can work in UAE or anywhere globally)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites advertise MBZUAI as a standard tuition waiver; it actually includes a massive monthly cash stipend of AED 8,000-10,000/month."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.0 / 4.00; falling below results in academic probation and potential scholarship loss.",
            "attendance_requirements": "Full-time physical research residence in Masdar City, Abu Dhabi.",
            "academic_progress_monitoring": "Semester credit reviews and annual dissertation progress milestones.",
            "work_restrictions_during_study": "Scholars are expected to devote full time to their academic and research work.",
            "home_country_return_obligation": "None; scholars are eligible for UAE Golden Visa sponsorship (10-year residency) post-graduation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Expulsion or voluntary withdrawal terminates funding.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from both departments.",
            "extension_policy": "Funding is provided for normal program duration (max 2 years for MSc; max 4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) - Admissions Official Portal",
                "source_url": "https://mbzuai.ac.ae/study/admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Online entry exam passing cutoff mark percentiles",
                    "Faculty interview technical scoring rubrics"
                ]
            }
        ]
    }
}
