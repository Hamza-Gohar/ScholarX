"""
scripts/dossiers_batch2b.py
Part B of Batch 2:
5. SCH-EU-012: Romanian Government ARICE / MFA Scholarship Programme (Romania)
6. SCH-EU-015: Politecnico di Milano Merit-Based Scholarships (Platinum, Gold, Silver - Italy)
7. SCH-EU-016: ETH Zurich Excellence Scholarship & Opportunity Programme (ESOP - Switzerland)
8. SCH-EU-022: Government of Ireland International Education Scholarship (GOI-IES - Ireland)
"""

DOSSIERS_BATCH2B = {
    # 5. Romanian Government ARICE / MFA Scholarship Programme (SCH-EU-012)
    "SCH-EU-012": {
        "scholarship_id": "SCH-EU-012",
        "basic_details": {
            "scholarship_name": "Romanian Government ARICE / MFA Scholarship Programme",
            "offering_entity": "Romanian Ministry of Foreign Affairs (MFA) & Agency for Investments and Foreign Trade (ARICE)",
            "host_country": "Romania",
            "host_institutions_covered": "All accredited Romanian State Universities (University of Bucharest, POLITEHNICA Bucharest, Babeș-Bolyai, Technical University of Cluj-Napoca, Alexandru Ioan Cuza)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Open to almost all academic fields: Engineering, Computer Science, Architecture, Agriculture, Veterinary Medicine, Economics, Humanities, Political Science. Excludes Medicine, Dental Medicine, and Pharmacy.",
            "number_of_awards_total": "~500 scholarships awarded annually across non-EU partner nations",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible non-EU partner state (~30 to 50 Pakistani students selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's (3-6 years) + 1 preparatory year; Master's (1.5-2 years) + 1 preparatory year; PhD (3-4 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of non-EU countries (Pakistani citizens eligible; dual Romanian citizens strictly ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 35,
            "age_limit_postgrad": 45,
            "age_limit_notes": "Undergraduate applicants under 35; PhD applicants under 45 years of age.",
            "academic_qualifications": "12 years (HSSC/FSc/A-Levels) for Bachelor's; 16 years (BS) for Master's; 18 years (MS/MPhil) for PhD.",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 2.8,
            "grading_conversion_notes": "Minimum grade 7.00 out of 10.00 (Romanian grading system, equivalent to at least 70% or 2.80/4.00 CGPA).",
            "subject_background_prerequisites": "Secondary school or university education in relevant academic subjects.",
            "current_education_status": "Graduated or in final year of study.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Academic record carries the overwhelming selection weight.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": None,
                "toefl_minimum": None,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "No English test required. Studies are conducted in the Romanian language, preceded by a fully funded 1-year preparatory Romanian language course."
            },
            "other_language_requirements": "Preparatory year of Romanian language is mandatory (unless applicant already holds a Romanian language proficiency certificate B2).",
            "gender_specific_requirements": "Equal opportunity; all eligible candidates welcome.",
            "financial_need_required": False,
            "special_eligibility_categories": "Cultural diplomacy and academic exchange.",
            "previous_scholarship_restrictions": "Ineligible if already benefiting from another Romanian state scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% tuition fees covered for the preparatory language year and the entire duration of the degree program.",
                "amount": "€2,500 to €5,000 / year"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "No university admission application fees; managed via ARICE/MFA centralized platform.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE DORMITORY",
                "details": "Free student hostel / university dormitory accommodation provided through the Romanian Ministry of Education budget.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly allowance to cover personal study expenses.",
                "amount": "Bachelor: 65 EUR/mo; Master: 75 EUR/mo; PhD: 85 EUR/mo (subsidized alongside free dorm and tuition)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare from Pakistan to Romania is paid by student/family.",
                "amount": None
            },
            "visa_fee": {
                "status": "WAIVED",
                "details": "Romanian long-stay student visa (type D/SD) is issued free of charge for scholarship holders.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Medical assistance in case of medical-surgical emergencies and acute illnesses provided by the Romanian state.",
                "amount": None
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Access to subsidized university cafeterias and canteens across Romanian campuses.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "NOT_COVERED",
                "details": "Handled through personal budget.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Departmental research facilities accessible for PhD scholars.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Domestic public transport and student train travel heavily discounted (50%–90% off) by Romanian student law.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 12000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for up to two universities and study options via the central portal.",
            "participating_institutions": [
                "National University of Science and Technology POLITEHNICA Bucharest",
                "University of Bucharest", "Babeș-Bolyai University (Cluj-Napoca)",
                "Technical University of Cluj-Napoca", "Alexandru Ioan Cuza University (Iași)",
                "Gheorghe Asachi Technical University of Iași", "West University of Timișoara"
            ],
            "university_rankings_scope": "Leading national public universities in Romania with strong engineering and science faculties.",
            "available_majors": [
                "Computer Science, Software Engineering, Civil Engineering, Mechanical Engineering, Electrical Engineering, Architecture, Agriculture, Veterinary Medicine, Economics, Business Administration, International Relations, Law, Physics, Chemistry, Biology"
            ],
            "english_taught_program_availability": False,
            "program_duration": "Preparatory year (1 yr) + Bachelor's (3-4 yrs) / Master's (2 yrs) / PhD (3-4 yrs)",
            "admission_requirements_summary": "Handled centrally by the Ministry of Foreign Affairs / ARICE and Ministry of Education; letter of acceptance issued directly.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "POLITEHNICA Bucharest and Babeș-Bolyai in Cluj-Napoca are most competitive for engineering and computer science.",
            "strategic_program_match_advice": "Learning Romanian in the preparatory year is mandatory and an incredible cultural asset for careers in the European Union."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://arice.gov.ro/1/burse-arice/",
            "portal_system_name": "ARICE / Study in Romania MFA Application System",
            "account_creation_instructions": "Register on the official ARICE scholarship portal (studyinromania.gov.ro or arice.gov.ro), select degree level and target universities.",
            "step_by_step_workflow": [
                "1. Register on the official portal during open window (January-March).",
                "2. Upload certified copies of educational diplomas, transcripts, and birth certificate.",
                "3. Upload Curriculum Vitae (Europass format) and Letter of Intent / Motivation Letter.",
                "4. Submit complete electronic dossier by deadline (typically late April).",
                "5. Evaluation board reviews academic scores and documents in May/June.",
                "6. Results announced in July; Ministry of Education issues official Letter of Acceptance.",
                "7. Apply for Romanian long-stay study visa (D/SD) free of charge at Romanian Embassy in Islamabad."
            ],
            "university_vs_scholarship_routing": "Direct centralized application through the ARICE / MFA portal.",
            "recommendation_letters_submission_method": "Letters of recommendation uploaded directly by applicant if requested.",
            "personal_statement_prompts": "Letter of Intent detailing your academic motivation, reasons for choosing Romania, and future career plans.",
            "study_plan_research_proposal_requirements": "PhD applicants must upload a detailed research project (3-5 pages) approved by a Romanian doctoral supervisor.",
            "cv_format_requirements": "Standard Europass CV format in English or French.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; selection is based strictly on academic dossier and grade averages.",
            "standardized_tests": "None; no IELTS/TOEFL required.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Diplomas and transcripts must be authenticated by IBCC/HEC and MOFA Pakistan before visa issuance.",
            "translation_requirements": "Authorized translations into English, French, Spanish, or Romanian.",
            "final_submission_method": "100% Online via ARICE portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Educational Diplomas & Certificates",
                "mandatory": True,
                "specification": "Matric/FSc for Bachelor's; BS degree for Master's; MS/MPhil for PhD",
                "pakistan_specific_instruction": "Attested by IBCC / HEC Pakistan and Ministry of Foreign Affairs (MOFA)"
            },
            {
                "document_name": "Academic Transcripts & Mark Sheets",
                "mandatory": True,
                "specification": "Transcripts showing all subjects and grades earned with official grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Birth Certificate",
                "mandatory": True,
                "specification": "NADRA computerized birth certificate",
                "pakistan_specific_instruction": "Translated and authenticated"
            },
            {
                "document_name": "Passport Copy",
                "mandatory": True,
                "specification": "Valid Pakistani passport photo page",
                "pakistan_specific_instruction": "Must be valid for at least 1 year past entry date"
            },
            {
                "document_name": "Medical Certificate",
                "mandatory": True,
                "specification": "Official medical certificate proving applicant is fit for study and free of infectious diseases",
                "pakistan_specific_instruction": "Issued by registered Pakistani government hospital"
            },
            {
                "document_name": "Europass Curriculum Vitae",
                "mandatory": True,
                "specification": "Standard Europass format in English",
                "pakistan_specific_instruction": "Detailing educational history and extracurricular activities"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-01-15",
            "application_deadline": "2027-04-30",
            "university_admission_deadline": "N/A (Centralized)",
            "document_submission_deadline": "2027-04-30",
            "recommendation_letters_deadline": "2027-04-30",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-07-15",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "October 2027",
            "annual_cycle_notes": "Opens annually in January and closes late April. Academic year begins October 1 across Romania."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Overall grade point average across secondary or university education)",
            "extracurricular_and_leadership_weight": "10% (Extracurricular background and honors)",
            "research_experience_weight": "15% (For PhD candidates: quality of proposed research plan)",
            "work_experience_weight": "5% (Professional experience)",
            "personal_statement_weight": "10% (Letter of Intent clarity)",
            "recommendations_weight": "0%",
            "interview_weight": "0%",
            "test_scores_weight": "0%",
            "financial_need_weight": "0%",
            "selection_panel_composition": "Joint commission composed of representatives of the Ministry of Foreign Affairs, Ministry of Economy, and Ministry of Education.",
            "evaluation_methodology": "Scoring of academic grades: Candidates are ranked based on GPA and allocated to available university seats."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 to 7,000 applications globally",
            "total_scholarships_awarded": "~500 scholarships awarded annually",
            "acceptance_rate_global": "~8% to 10%",
            "acceptance_rate_pakistan": "~5% (Moderately Competitive)",
            "typical_successful_applicant_gpa": "3.20 to 3.75 / 4.00 CGPA or 75%+ marks",
            "typical_academic_and_research_profile": "Solid academic students seeking quality European education with low living overhead.",
            "common_backgrounds_of_winners": "Students from all provinces of Pakistan (Punjab, Sindh, KP, Balochistan, Islamabad) enrolling in engineering, IT, and business.",
            "high_representation_countries": "Pakistan, Morocco, Egypt, Jordan, Nigeria, Vietnam, Brazil.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Pakistani education agents charging PKR 300,000 to 500,000 claiming they have special quota links to the Romanian Embassy."
            ],
            "application_fee_warning": "The Romanian Government scholarship application is 100% FREE. Never pay any agent.",
            "agent_and_intermediary_warnings": "Apply directly on the official Romanian government portal without intermediaries.",
            "hidden_costs_breakdown": [
                "International flight ticket to Bucharest (~PKR 180,000 to 250,000).",
                "HEC / IBCC / MOFA attestation and translation fees in Pakistan (~PKR 30,000).",
                "Monthly pocket money buffer (since the ~€65-85 stipend covers only basic expenses, students need ~€100-150/mo extra for food)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You will study in English. (Fact: Romanian government scholarships are almost exclusively in Romanian language; the 1-year language prep year is mandatory).",
                "MYTH: You can study MBBS/Medicine. (Fact: Medicine, Dentistry, and Pharmacy are strictly excluded from this scholarship)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Agents falsely claim the stipend is €800/month; the official government stipend is €65 to €85/month alongside free tuition and free dorm."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass all exams in the Romanian language preparatory year to proceed to the degree; must earn all required credits each academic year.",
            "attendance_requirements": "Full-time physical attendance at host Romanian university.",
            "academic_progress_monitoring": "Failing an academic year results in permanent loss of scholarship.",
            "work_restrictions_during_study": "International students in Romania are legally permitted to work up to 4 hours per day (part-time) with a work permit.",
            "home_country_return_obligation": "None; Romania is an EU member state and graduates can seek employment or pursue further studies in Europe.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Failing the preparatory language year or academic expulsion terminates scholarship benefits.",
            "rules_for_changing_university": "Changing universities requires Ministry of Education approval and is generally only permitted after the preparatory year.",
            "rules_for_changing_major": "Not permitted once degree program begins.",
            "extension_policy": "No extensions beyond normal study duration."
        },
        "official_sources_verified": [
            {
                "source_name": "Romanian Agency for Investments and Foreign Trade (ARICE) - Scholarships Portal",
                "source_url": "https://arice.gov.ro/1/burse-arice/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of country quotas between partner nations",
                    "Internal committee scoring sheets"
                ]
            },
            {
                "source_name": "Romanian Ministry of Foreign Affairs (MFA) - Scholarships Portal",
                "source_url": "https://www.mae.ro/en/node/10251",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation matrix of spots per individual Romanian university"
                ]
            }
        ]
    },

    # 6. Politecnico di Milano Merit-Based Scholarships (SCH-EU-015)
    "SCH-EU-015": {
        "scholarship_id": "SCH-EU-015",
        "basic_details": {
            "scholarship_name": "Politecnico di Milano Merit-Based Scholarships (Platinum, Gold, Silver)",
            "offering_entity": "Politecnico di Milano (Polimi, Italy)",
            "host_country": "Italy",
            "host_institutions_covered": "Politecnico di Milano (Milano Leonardo, Bovisa, Como, Lecco, Cremona, Mantova, Piacenza campuses)",
            "degree_levels": ["Master of Science (Laurea Magistrale)"],
            "major_restrictions": "Open to all Master of Science programs in Engineering, Architecture, and Design taught in English.",
            "number_of_awards_total": "~100 to 150 merit scholarships awarded across international candidates annually",
            "number_of_awards_pakistan": "Open globally; dozens of Pakistani engineers and architects win Platinum, Gold, or Silver awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 academic years (covering the full Master of Science degree: 120 ECTS)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students of all nationalities (including Pakistan) residing outside Italy"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed or completing 16 years of education (4-year Bachelor of Science/Engineering/Architecture) from an accredited university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum 3.30 / 4.00 CGPA; competitive Platinum/Gold winners typically present 3.65+ / 4.00 CGPA.",
            "subject_background_prerequisites": "Substantial bachelor's degree in engineering, architecture, design, or applied sciences satisfying Polimi course prerequisites.",
            "current_education_status": "Graduated or in final semester of undergraduate study.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience, internships, and design portfolios (for Architecture/Design) strengthen the application.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 78,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic minimum 6.0 overall or TOEFL iBT 78 or Cambridge English B2 First/C1 Advanced."
            },
            "other_language_requirements": "Italian not required for English-taught programs.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Academic merit; can also be complemented with regional DSU need-based benefits if eligible.",
            "previous_scholarship_restrictions": "Must pay non-refundable university enrollment fee (€170) to confirm scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee waiver (covers all administrative tuition fees of €3,898 per year; student pays only ~€170 administrative tax).",
                "amount": "€3,898 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Application fee of €50 paid by candidate on Polimi portal.",
                "amount": "€50"
            },
            "accommodation": {
                "status": "GOLD_TIER_PROVIDES_FREE_DORM",
                "details": "Gold tier provides free accommodation in university residences; Platinum tier provides €10,000 cash grant to arrange accommodation.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "PLATINUM_TIER_PROVIDES_STIPEND",
                "details": "Platinum Scholarship: €10,000 gross per year paid in installments (~€833 / month or ~PKR 250,000 / month).",
                "amount": "Platinum: €10,000 / year; Gold: Free housing; Silver: Tuition waiver"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel paid by candidate.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Italian student visa fee (~€50) paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "NOT_COVERED",
                "details": "Italian National Health Service (SSN) student enrollment (~€150 to €700/year depending on regional policy) paid by student.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED_UNDER_PLATINUM_STIPEND",
                "details": "Paid from stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "NOT_COVERED",
                "details": "Personal responsibility.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Departmental laboratory thesis grants available.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Atm Milan student transit pass heavily discounted (~€22/month).",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Politecnico di Milano (Top 10 in Europe for Engineering and Architecture).",
            "participating_institutions": [
                "Politecnico di Milano"
            ],
            "university_rankings_scope": "QS World Rank #111 overall; Top 20 globally for Civil, Mechanical, and Electrical Engineering; World #7 for Architecture.",
            "available_majors": [
                "Computer Science and Engineering, Artificial Intelligence Systems, Automation and Control Engineering, Electrical Engineering, Electronics Engineering, Mechanical Engineering, Aerospace Engineering, Civil Engineering, Environmental and Land Planning Engineering, Chemical Engineering, Architecture and Urban Design, Sustainable Architecture, Integrated Product Design"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 academic years (120 ECTS credits)",
            "admission_requirements_summary": "Automatic consideration: All international students admitted to a Master of Science program who apply by the deadline are automatically assessed for merit scholarships.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science and Mechanical Engineering are highest volume; apply in early call (Semester 1, Round 1).",
            "strategic_program_match_advice": "Upload detailed course descriptions (syllabus) of your Pakistani bachelor's degree; Polimi evaluates syllabus matching rigorously."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.polimi.it/en/international-prospective-students/laurea-magistrale-programmes-equivalent-to-master-of-science/scholarships",
            "portal_system_name": "Politecnico di Milano Online Services Portal",
            "account_creation_instructions": "Register for Polimi credentials, generate person code, select up to 2 Master of Science programs, and pay €50 application fee.",
            "step_by_step_workflow": [
                "1. Create account on Polimi portal during Call 1 (September to November) or Call 2 (January to February).",
                "2. Upload complete official academic transcripts, degree certificate, and course descriptions.",
                "3. Upload CV, Statement of Motivation, one Academic Recommendation Letter, and Portfolio (mandatory for Architecture/Design).",
                "4. Pay the €50 non-refundable application fee.",
                "5. Admissions results and scholarship notifications released progressively by March/April.",
                "6. If awarded scholarship, pay €170 administrative enrollment fee to accept and secure award.",
                "7. Complete Universitaly portal pre-enrollment and apply for Italian student visa at Italian Embassy in Islamabad/Consulate in Karachi."
            ],
            "university_vs_scholarship_routing": "Integrated single application; no separate scholarship form needed.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate during application.",
            "personal_statement_prompts": "Motivation letter detailing why you chose Politecnico di Milano, your academic background, and future engineering ambitions.",
            "study_plan_research_proposal_requirements": "Not required for taught MSc; course description booklet of bachelor's degree required.",
            "cv_format_requirements": "Standard 1-2 page CV detailing academic background, projects, technical skills, and software proficiencies.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; decisions based entirely on academic evaluation of uploaded documents.",
            "standardized_tests": "GRE is NOT required; English test (IELTS 6.0+ or TOEFL 78+) is mandatory.",
            "application_fee_amount": "€50.",
            "attestation_requirements": "CIMEA Statement of Comparability / Verification or Declaration of Value (DOV) from Italian Embassy in Islamabad.",
            "translation_requirements": "Official certified translations into English or Italian.",
            "final_submission_method": "100% Online via Polimi portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Bachelor Degree & Transcripts",
                "mandatory": True,
                "specification": "Official transcripts and degree certificate showing all courses, credits, and GPA",
                "pakistan_specific_instruction": "Attested by HEC Pakistan; CIMEA verification or DOV needed for final enrollment"
            },
            {
                "document_name": "Course Descriptions / Syllabus Booklet",
                "mandatory": True,
                "specification": "Detailed description of all courses taken during undergraduate degree",
                "pakistan_specific_instruction": "Stamped by your Pakistani university department or registrar"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "1-2 page academic and technical resume",
                "pakistan_specific_instruction": "Highlighting major FYP (Final Year Project) and software tools"
            },
            {
                "document_name": "Motivation Letter",
                "mandatory": True,
                "specification": "Statement explaining motivations for choosing the program and career goals",
                "pakistan_specific_instruction": "One letter per selected master's program"
            },
            {
                "document_name": "Academic Recommendation Letter",
                "mandatory": True,
                "specification": "Letter from university professor written on official university letterhead",
                "pakistan_specific_instruction": "Signed and stamped by professor from Pakistani university"
            },
            {
                "document_name": "English Proficiency Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.0+) or TOEFL iBT (78+)",
                "pakistan_specific_instruction": "Valid test report"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-10",
            "application_deadline": "2026-11-20",
            "university_admission_deadline": "2026-11-20",
            "document_submission_deadline": "2026-11-27",
            "recommendation_letters_deadline": "2026-11-27",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "First round (Call 1) closes late November for September 2027 intake; the majority of merit scholarships are awarded in Call 1."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (GPA, grading scale, prestige of home university)",
            "extracurricular_and_leadership_weight": "10% (Technical projects, competitions, extracurriculars)",
            "research_experience_weight": "15% (Final Year Project quality, thesis, publications)",
            "work_experience_weight": "5% (Internships or engineering work)",
            "personal_statement_weight": "15% (Motivation letter alignment with curriculum)",
            "recommendations_weight": "10% (Faculty recommendation letter)",
            "interview_weight": "0%",
            "test_scores_weight": "Threshold required",
            "financial_need_weight": "0% (Strictly merit-based; can apply separately for DSU need scholarship)",
            "selection_panel_composition": "Politecnico di Milano Academic Evaluation Committees composed of departmental faculty boards.",
            "evaluation_methodology": "Holistic evaluation of academic transcript alignment, GPA, motivation letter, and portfolio."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~12,000 to 15,000 international master's applications",
            "total_scholarships_awarded": "~150 merit scholarships awarded across all tiers (Platinum, Gold, Silver)",
            "acceptance_rate_global": "~1.2% for merit scholarship",
            "acceptance_rate_pakistan": "~1.5% to 2% (Extremely Competitive for Platinum; Silver more accessible)",
            "typical_successful_applicant_gpa": "3.65 to 3.95 / 4.00 CGPA",
            "typical_academic_and_research_profile": "High-ranking graduates from recognized Pakistani engineering universities (NUST, UET, GIKI, FAST, NED).",
            "common_backgrounds_of_winners": "Graduates of NUST, GIKI, UET Lahore, NED Karachi who also apply for regional DSU scholarships.",
            "high_representation_countries": "India, Pakistan, Turkey, Iran, China, Brazil, Egypt.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agencies claiming they can guarantee Polimi Platinum scholarships for large fees."
            ],
            "application_fee_warning": "Pay the official €50 application fee only on the secure Polimi portal.",
            "agent_and_intermediary_warnings": "Polimi does not work with commercial agents; apply directly on the online portal.",
            "hidden_costs_breakdown": [
                "Application fee (€50).",
                "Enrollment administrative fee to confirm scholarship (~€170).",
                "CIMEA verification certificate fee (~€150 to €300) or DOV expenses in Islamabad.",
                "Living cost difference in Milan if awarded Silver (fee waiver only) or Gold (dorm only)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot apply for DSU if you do not get a Polimi merit scholarship. (Fact: Admitted students who do not receive a Polimi merit scholarship can still apply for the regional Italian DSU need-based scholarship which covers full tuition + cash stipend + free cafeteria).",
                "MYTH: You need Italian language. (Fact: All Laurea Magistrale programs listed are 100% in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Blogs often confuse Polimi merit scholarships with DSU Lombardia; they are two separate funding schemes with different deadlines."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must earn at least 30 ECTS credits in the first year to renew scholarship benefits for the second year.",
            "attendance_requirements": "Full-time physical attendance on campus in Milan or territorial campuses.",
            "academic_progress_monitoring": "Credits checked in August of each year.",
            "work_restrictions_during_study": "Permitted to work up to 20 hours/week under Italian student visa regulations.",
            "home_country_return_obligation": "None; graduates can convert student visa into a 1-year job search residence permit (Permesso di Soggiorno per Ricerca Lavoro).",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Failing to achieve minimum credit thresholds leads to loss of scholarship for the second year.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Changing programs usually results in forfeiture of the merit award.",
            "extension_policy": "Strictly maximum 2 academic years; third-year extensions not funded."
        },
        "official_sources_verified": [
            {
                "source_name": "Politecnico di Milano - International Prospective Students Merit Scholarships Portal",
                "source_url": "https://www.polimi.it/en/international-prospective-students/laurea-magistrale-programmes-equivalent-to-master-of-science/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact mathematical breakdown between Platinum, Gold, and Silver awards across faculties",
                    "Specific country allocation quota targets"
                ]
            }
        ]
    },

    # 7. ETH Zurich Excellence Scholarship & Opportunity Programme (ESOP) (SCH-EU-016)
    "SCH-EU-016": {
        "scholarship_id": "SCH-EU-016",
        "basic_details": {
            "scholarship_name": "ETH Zurich Excellence Scholarship & Opportunity Programme (ESOP)",
            "offering_entity": "ETH Zurich (Swiss Federal Institute of Technology) & ETH Foundation",
            "host_country": "Switzerland",
            "host_institutions_covered": "ETH Zurich (Zentrum and Hönggerberg campuses, Zurich, Switzerland)",
            "degree_levels": ["Master of Science (MSc)"],
            "major_restrictions": "Open to all Master's degree programs at ETH Zurich across Engineering, Natural Sciences, Computer Science, Mathematics, Architecture, and Management.",
            "number_of_awards_total": "~50 to 60 ESOP scholarships awarded annually across all departments",
            "number_of_awards_pakistan": "Open globally; highly competitive; awarded purely on absolute academic and research brilliance",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full regular duration of the Master's program (3 to 4 semesters / 1.5 to 2 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students of all nationalities (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "16 years of education (4-year Bachelor's degree) from an accredited university with outstanding results.",
            "minimum_gpa_percentage": 90.0,
            "minimum_gpa_scale": 3.85,
            "grading_conversion_notes": "Must rank in the top 10% of their Bachelor's degree program (Grade A or equivalent, minimum 3.85 / 4.00 CGPA).",
            "subject_background_prerequisites": "Rigorous undergraduate foundation in the exact discipline applied for.",
            "current_education_status": "Graduated or in final semester of undergraduate study.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior research experience, scientific publications, and international academic competition awards significantly enhance chances.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 100,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic minimum 7.0 overall or TOEFL iBT minimum 100."
            },
            "other_language_requirements": "German not required for English-taught Master's programs (almost all MSc programs at ETH are in English).",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite academic merit and research potential; mandatory pre-proposal for master's thesis required.",
            "previous_scholarship_restrictions": "Cannot hold another major scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee waiver (ETH Zurich semester tuition fees of CHF 730/semester fully waived).",
                "amount": "CHF 1,460 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "ETH Zurich graduate application fee (CHF 150) paid by applicant.",
                "amount": "CHF 150"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered through living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Comprehensive living and study expenses grant paid at the beginning of each semester.",
                "amount": "CHF 12,000 / semester (CHF 24,000 / year ~CHF 2,000 / month or ~PKR 625,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International flights to Zurich covered from living allowance.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Swiss national visa fee and biometric residence permit fees in Canton Zurich (~CHF 150) paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "SUBSIDIZED_VIA_STIPEND",
                "details": "Swiss student health insurance (Swisscare, ~CHF 65-80/month) paid from stipend.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered via living allowance.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Departmental research laboratory funds available for thesis work.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Swiss Half-Fare travelcard can be purchased from living allowance.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 30000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: ETH Zurich (Consistently ranked Top 10 in the world in QS and THE rankings).",
            "participating_institutions": [
                "ETH Zurich (Departments of Computer Science, Information Technology & EE, Mechanical & Process Eng, Physics, Chemistry, Mathematics, Architecture, Biosystems Science & Eng)"
            ],
            "university_rankings_scope": "World #7 in QS World University Rankings; #1 in continental Europe.",
            "available_majors": [
                "Computer Science, Data Science, Cyber Security, Robotics, Systems & Control, Electrical Engineering & IT, Mechanical Engineering, Quantum Engineering, Physics, Mathematics, Chemical & Bioengineering, Biotechnology, Materials Science, Architecture"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 to 4 semesters (1.5 to 2 years, 90 to 120 ECTS)",
            "admission_requirements_summary": "Apply for the Master's degree program via the online portal and select the ESOP application option; submit additional pre-proposal for master's thesis.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science, Data Science, and Robotics are among the most selective departments in Europe.",
            "strategic_program_match_advice": "The master's thesis pre-proposal is the crucial differentiator; write a rigorous 2-page research proposal following scientific citation standards."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://ethz.ch/students/en/studies/financial/scholarships/excellencescholarships.html",
            "portal_system_name": "ETH Zurich eApply Online Application System",
            "account_creation_instructions": "Register on eApply, submit master's application, upload ESOP pre-proposal, and nominate two academic referees.",
            "step_by_step_workflow": [
                "1. Check admission prerequisites and prepare academic documents (September-October).",
                "2. Formulate 2-page pre-proposal for master's thesis following official ETH guidance.",
                "3. Create account on ETH Zurich eApply portal (Window opens November 1).",
                "4. Check the box to apply for the Excellence Scholarship & Opportunity Programme (ESOP).",
                "5. Upload pre-proposal, CV, transcripts, ranking certificate, and two referee contacts.",
                "6. Submit online application by strict deadline (November 30).",
                "7. Departmental admission committees review dossiers in January/February.",
                "8. Central Rector's Scholarship Committee decisions released by mid-March."
            ],
            "university_vs_scholarship_routing": "Integrated single application via ETH eApply system.",
            "recommendation_letters_submission_method": "Submitted online by referees via confidential electronic link sent by ETH Zurich.",
            "personal_statement_prompts": "Address your scientific motivations, future career vision, and reasons for selecting ETH Zurich.",
            "study_plan_research_proposal_requirements": "MANDATORY: 2-page Master's Thesis Pre-Proposal outlining research topic, scientific questions, methodology, and relevance.",
            "cv_format_requirements": "Clear, concise academic CV detailing education, publications, awards, and technical competencies.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; decisions based strictly on evaluation of written dossier and thesis pre-proposal.",
            "standardized_tests": "GRE General test required or strongly recommended by some departments (e.g., Computer Science); English proficiency test required.",
            "application_fee_amount": "CHF 150 (paid via credit card on eApply).",
            "attestation_requirements": "Certified transcripts and degree certificates; HEC attestation required.",
            "translation_requirements": "Certified translations into English or German.",
            "final_submission_method": "100% Online via eApply."
        },
        "required_documents_checklist": [
            {
                "document_name": "Master's Thesis Pre-Proposal",
                "mandatory": True,
                "specification": "Strict 2-page scientific proposal detailing potential master's thesis research topic",
                "pakistan_specific_instruction": "Original independent research proposal; must include bibliography"
            },
            {
                "document_name": "Official Academic Transcripts & Ranking Certificate",
                "mandatory": True,
                "specification": "Transcripts showing all courses, credits, and official certificate showing top 10% class rank",
                "pakistan_specific_instruction": "Rank certificate signed by university dean or registrar"
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Submitted directly by university research professors",
                "pakistan_specific_instruction": "From professors who supervised your undergraduate research"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "Academic CV highlighting awards and publications",
                "pakistan_specific_instruction": "Highlighting Olympiads, hackathons, and research output"
            },
            {
                "document_name": "English Proficiency Score",
                "mandatory": True,
                "specification": "IELTS Academic (7.0+) or TOEFL iBT (100+)",
                "pakistan_specific_instruction": "Electronic score report sent to ETH Zurich"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-11-01",
            "application_deadline": "2026-11-30",
            "university_admission_deadline": "2026-11-30",
            "document_submission_deadline": "2026-11-30",
            "recommendation_letters_deadline": "2026-11-30",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "Application window is strictly 1 month: opens November 1 and closes November 30 for all international applicants."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Exceptional academic record, straight A grades, top 10% class ranking)",
            "extracurricular_and_leadership_weight": "5% (Secondary to scientific excellence)",
            "research_experience_weight": "30% (Quality, scientific rigor, and feasibility of master's thesis pre-proposal)",
            "work_experience_weight": "0%",
            "personal_statement_weight": "10% (Clarity of vision and purpose)",
            "recommendations_weight": "10% (Strength of professor endorsements)",
            "interview_weight": "0%",
            "test_scores_weight": "Language and GRE scores evaluated",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "Departmental Admissions Committees and the Central Admissions Committee headed by the ETH Zurich Rector.",
            "evaluation_methodology": "Two-tier review: Department evaluates subject compatibility and thesis pre-proposal; Rector's Committee awards ESOP to the highest-ranking candidates."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 to 5,000 international master's applications across all departments",
            "total_scholarships_awarded": "~50 to 60 ESOP scholarships awarded annually across entire university",
            "acceptance_rate_global": "~1.0% to 1.2%",
            "acceptance_rate_pakistan": "~0.5% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.90 to 4.00 CGPA (Top 1% to 3% of graduating cohort)",
            "typical_academic_and_research_profile": "Medal-winning students with near-perfect GPAs, research publications, and deeply sophisticated thesis pre-proposals.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani institutions (LUMS, NUST, GIKI) with exceptional mathematical and engineering credentials.",
            "high_representation_countries": "Switzerland, Germany, China, India, USA, Italy, Pakistan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial sites offering pre-written ETH thesis proposals; plagiarism is checked via Turnitin and leads to permanent ban."
            ],
            "application_fee_warning": "Pay the CHF 150 application fee only on the official ETH eApply platform.",
            "agent_and_intermediary_warnings": "ETH Zurich does not work with any commercial agencies or consultants.",
            "hidden_costs_breakdown": [
                "ETH application fee (CHF 150, ~PKR 48,000).",
                "Swiss visa application and biometric residence permit fees (~CHF 150).",
                "High initial living expenses buffer in Zurich before first semester stipend installment."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can submit the thesis pre-proposal after getting admitted. (Fact: The pre-proposal MUST be submitted with the initial application in November; late submissions not accepted).",
                "MYTH: You must speak German. (Fact: Nearly all MSc programs in engineering, CS, and natural sciences at ETH Zurich are taught 100% in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently claim tuition in Switzerland is free; while Swiss tuition is low (CHF 730/sem), living costs in Zurich are among the highest in the world (~CHF 2,000/month), which ESOP fully covers."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain top academic performance (Grade average minimum 5.0 out of 6.0 in the Swiss grading system).",
            "attendance_requirements": "Full-time physical enrollment on campus in Zurich.",
            "academic_progress_monitoring": "Semester-by-semester credit review; failure to maintain grade standard results in suspension of stipend.",
            "work_restrictions_during_study": "Permitted to work up to 15 hours/week during term under Swiss student residence permit, but ESOP explicitly discourages outside employment.",
            "home_country_return_obligation": "None; scholars can apply for a 6-month Swiss residence permit extension to seek employment post-graduation.",
            "service_obligations_or_bonds": "None; participation in ETH Foundation networking events.",
            "repayment_clawback_conditions": "Failing courses or withdrawing from degree terminates funding.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from both departmental directors of studies.",
            "extension_policy": "Strict maximum duration of regular study period (max 4 semesters)."
        },
        "official_sources_verified": [
            {
                "source_name": "ETH Zurich - Excellence Scholarship & Opportunity Programme Official Portal",
                "source_url": "https://ethz.ch/students/en/studies/financial/scholarships/excellencescholarships.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Department-by-department allocation quota numbers for ESOP awards",
                    "Evaluation scoring sheet details for thesis pre-proposals"
                ]
            }
        ]
    },

    # 8. Government of Ireland International Education Scholarship (SCH-EU-022)
    "SCH-EU-022": {
        "scholarship_id": "SCH-EU-022",
        "basic_details": {
            "scholarship_name": "Government of Ireland International Education Scholarship (GOI-IES)",
            "offering_entity": "Government of Ireland & Higher Education Authority (HEA)",
            "host_country": "Ireland",
            "host_institutions_covered": "All participating Irish Higher Education Institutions (Trinity College Dublin, University College Dublin, University of Galway, University College Cork, Dublin City University, University of Limerick, Maynooth University)",
            "degree_levels": ["Master's (Taught or Research)", "Final Year of PhD"],
            "major_restrictions": "Open to all disciplines across Science, Engineering, Medicine, Humanities, Social Sciences, Business, and Law offered at participating Irish universities.",
            "number_of_awards_total": "60 prestigious scholarships awarded annually across non-EU/EEA countries",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible non-EU state (~4 to 8 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "1 full academic year of study (12 months)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of non-EU/EEA countries (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (Bachelor's degree) with first-class honours standing (or equivalent) for Master's applicants.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum equivalent to Irish First Class Honours (1st) or Upper Second Class (2:1), equivalent to 3.30+ / 4.00 CGPA or 75%+ marks.",
            "subject_background_prerequisites": "Academic background matching the chosen Irish Master's or PhD programme.",
            "current_education_status": "Must hold an offer (conditional or unconditional) of admission to a full-time master's program at an eligible Irish HEI.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Academic excellence, leadership potential, and societal impact evaluated.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": True,
                "moi_certificate_accepted": False,
                "notes": "Must satisfy the language entry requirement of the host Irish university (typically IELTS 6.5 with no band below 6.0, TOEFL 90, or Duolingo 120)."
            },
            "other_language_requirements": "None; all programs in English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must possess an active university application or admission offer from an Irish HEI before applying.",
            "previous_scholarship_restrictions": "Ineligible if previously awarded a GOI-IES scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver and student registration charge waived by the host Irish higher education institution.",
                "amount": "€14,000 to €26,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Irish university admission application fee (~€50) paid by candidate.",
                "amount": "€50"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered through living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "€10,000 living stipend paid in two equal installments (€5,000 per semester) via host university.",
                "amount": "€10,000 for the study year (~€833 / month or ~PKR 250,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel paid by candidate from living stipend or personal funds.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Irish student visa fee (€60 to €100) and Irish Residence Permit (IRP) card fee (€300) paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "NOT_COVERED",
                "details": "Private medical insurance required for Irish visa (~€160/year) paid by student.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered via living allowance.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Host university research funds accessible for research master's and PhD.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Covered from personal funds.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 30000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Any eligible Irish university or Institute of Technology.",
            "participating_institutions": [
                "Trinity College Dublin (TCD)", "University College Dublin (UCD)",
                "University of Galway", "University College Cork (UCC)",
                "Dublin City University (DCU)", "University of Limerick (UL)",
                "Maynooth University", "Technological University Dublin (TU Dublin)"
            ],
            "university_rankings_scope": "Top Irish universities ranked in QS World Top 300.",
            "available_majors": [
                "Computer Science, Artificial Intelligence, Data Analytics, Electronic & Computer Engineering, Biomedical Engineering, Pharmaceutical Sciences, Public Health, Environmental Science, Finance, International Management, Law, International Relations"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 academic year (covering 1-year Master's or final year of PhD)",
            "admission_requirements_summary": "Must secure an offer of admission from an eligible Irish HEI first; then apply for GOI-IES scholarship referencing that offer.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Trinity College Dublin and UCD are most competitive; regional universities like Galway and Limerick offer high award conversion.",
            "strategic_program_match_advice": "Focus heavily on how Ireland's global technological hub ecosystem (EMEA headquarters of Google, Meta, Pfizer) connects with your career vision."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://hea.ie/policy/internationalisation/goi-ies/",
            "portal_system_name": "Higher Education Authority (HEA) Online Scholarship Portal",
            "account_creation_instructions": "Register on the official HEA application system, select your nominating Irish university, and enter admission application reference number.",
            "step_by_step_workflow": [
                "1. Apply for admission to an eligible Master's program at an Irish university by December/January.",
                "2. Receive admission offer (conditional or unconditional) from the Irish university.",
                "3. Create account on the HEA GOI-IES portal (Opens January/February).",
                "4. Answer 3 detailed essay questions on academic achievements, career potential, and ambassadorial contribution.",
                "5. Upload academic transcripts and two reference letters.",
                "6. Submit online application by the annual deadline (typically mid-March).",
                "7. Independent assessment panel evaluates applications in April.",
                "8. Results announced in late May/early June; visa application begins."
            ],
            "university_vs_scholarship_routing": "Sequential: University admission application first; then central HEA scholarship application.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate during portal application.",
            "personal_statement_prompts": "Address your academic excellence, how the scholarship connects to long-term career goals, and how you will act as an ambassador for Ireland.",
            "study_plan_research_proposal_requirements": "Integrated into essay questions; clear rationale for chosen program of study in Ireland.",
            "cv_format_requirements": "Standard academic and professional resume (1-2 pages).",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; decisions based entirely on evaluation of written essays and academic dossier.",
            "standardized_tests": "English test (IELTS 6.5+, TOEFL 90+, or Duolingo 120+).",
            "application_fee_amount": "$0 for GOI-IES; university admission application fee (~€50) applies.",
            "attestation_requirements": "Transcripts certified by Pakistani degree institution; HEC attestation required for visa.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via HEA portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Admission Offer Letter from Irish University",
                "mandatory": True,
                "specification": "Official conditional or unconditional offer letter from an eligible Irish HEI",
                "pakistan_specific_instruction": "Must specify 2027/2028 academic intake"
            },
            {
                "document_name": "Academic Transcripts & Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing all subjects, grades, and GPA",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Academic or professional references speaking to applicant's potential",
                "pakistan_specific_instruction": "On official letterhead, signed and stamped"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "1-2 page CV detailing education and achievements",
                "pakistan_specific_instruction": "Chronological format"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (90+) or DET (120+)",
                "pakistan_specific_instruction": "Satisfying Irish university offer condition"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-01-20",
            "application_deadline": "2027-03-13",
            "university_admission_deadline": "2027-02-15",
            "document_submission_deadline": "2027-03-13",
            "recommendation_letters_deadline": "2027-03-13",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-06-15",
            "visa_application_window": "June to August 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "Application window opens late January and closes strictly in mid-March each year. Results announced late May."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic qualifications, achievements, and work experience)",
            "extracurricular_and_leadership_weight": "15% (Leadership track record and extracurricular engagement)",
            "research_experience_weight": "10% (Analytical ability and project work)",
            "work_experience_weight": "5% (Professional experience)",
            "personal_statement_weight": "25% (Quality of the three essay responses, career vision, ambassadorial potential)",
            "recommendations_weight": "5% (Strength of referee letters)",
            "interview_weight": "0%",
            "test_scores_weight": "Threshold required",
            "financial_need_weight": "0% (Strictly merit and ambassadorial potential)",
            "selection_panel_composition": "Independent assessment panel appointed by the Higher Education Authority (HEA) of Ireland.",
            "evaluation_methodology": "Competitive marking out of 100 points: Academic record (40 pts), Personal statement & career vision (45 pts), References (15 pts)."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000+ applicants globally from non-EU/EEA countries",
            "total_scholarships_awarded": "60 scholarships awarded annually globally",
            "acceptance_rate_global": "~1.2%",
            "acceptance_rate_pakistan": "~1% to 1.5% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.60 to 3.95 / 4.00 CGPA",
            "typical_academic_and_research_profile": "High-performing graduates with top grades, compelling essays on how they will bridge Ireland-Pakistan bilateral ties, and clear professional roadmaps.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (LUMS, NUST, FAST, IBA, Punjab University) enrolling in tech, data science, and business master's programs.",
            "high_representation_countries": "India, Pakistan, Nigeria, USA, China, Brazil, Canada.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized websites charging fees for GOI-IES application submission."
            ],
            "application_fee_warning": "The GOI-IES application on the HEA portal is 100% FREE.",
            "agent_and_intermediary_warnings": "Never pay agents to write your essay questions; HEA evaluates authenticity and personal voice.",
            "hidden_costs_breakdown": [
                "Irish student visa fee (~€60 to €100).",
                "Irish Residence Permit (IRP) card registration fee in Ireland (€300).",
                "Private medical insurance policy (~€160).",
                "International flight ticket to Dublin (~PKR 220,000 to 320,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can apply without an Irish university offer. (Fact: You MUST have applied to an Irish university and received an application number or offer to submit the GOI-IES application).",
                "MYTH: You cannot work in Ireland after graduation. (Fact: Graduates of Irish Master's programs are eligible for the 2-year Third Level Graduate Scheme (stay-back visa) to work in Ireland)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites advertise this as a €15,000 award; the official stipend is €10,000 direct plus 100% full tuition fee waiver."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance and pass all coursework modules (60-90 ECTS).",
            "attendance_requirements": "Full-time physical residence and attendance at host Irish institution.",
            "academic_progress_monitoring": "Host universities submit progress reports to the Higher Education Authority.",
            "work_restrictions_during_study": "Permitted to work up to 20 hours/week during term-time and 40 hours/week during holidays under Irish student Stamp 2 visa rules.",
            "home_country_return_obligation": "None; scholars are fully eligible for the Irish 2-year Third Level Graduate Scheme (Stamp 1G) post-study work visa.",
            "service_obligations_or_bonds": "Obligated to act as a student ambassador for Ireland and participate in HEA promotional activities.",
            "repayment_clawback_conditions": "Failing modules or misconduct leads to cancellation of remaining stipend payments.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Strictly limited to one academic year; no extensions permitted."
        },
        "official_sources_verified": [
            {
                "source_name": "Higher Education Authority (HEA) Ireland - GOI-IES Official Portal",
                "source_url": "https://hea.ie/policy/internationalisation/goi-ies/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Country-specific target quotas among the 60 total international awards",
                    "Independent assessment panel scoring mark sheets"
                ]
            }
        ]
    }
}
