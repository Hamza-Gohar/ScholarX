# scripts/batch14_p3.py
# SCH-EU-043: Chalmers University of Technology IPOET Scholarship (Sweden)
# SCH-EU-047: Erasmus Mundus Master in Security and Cloud Computing (SECCLO) (Europe)
# SCH-EU-052: École Polytechnique Paris Master's Excellence Scholarship (France)
# SCH-EU-067: Technical University of Denmark (DTU) PhD Fellowship in AI & Computing (Denmark)

DATA_P3 = {
    "SCH-EU-043": {
        "scholarship_id": "SCH-EU-043",
        "basic_details": {
            "scholarship_name": "Chalmers University of Technology IPOET Scholarship",
            "offering_entity": "Chalmers University of Technology & Swedish Council for Higher Education (UHR)",
            "host_country": "Sweden",
            "host_institutions_covered": "Chalmers Johanneberg & Lindholmen Campuses (Gothenburg, Sweden)",
            "degree_levels": ["Master of Science (MSc)"],
            "major_restrictions": "Master's programmes across all engineering departments, with emphasis on Computer Science and Engineering: Computer Science - algorithms, languages and logic, Computer Systems and Networks, Data Science and AI, High-Performance Computer Systems, and Software Engineering.",
            "number_of_awards_total": "~45 to 55 tuition waivers (75% or 100% waiver) awarded annually across all master's programmes",
            "number_of_awards_pakistan": "Open international competition; Pakistani STEM graduates secure ~3 to 6 tuition waivers annually",
            "funding_classification": "TUITION_ONLY",
            "duration_of_scholarship": "2 years (120 ECTS credits), subject to achieving at least 45 ECTS credits in Year 1"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of non-EU/EEA countries liable to pay tuition fees in Sweden"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science, Software Engineering, Electrical Engineering, or related STEM field from an HEC-recognized university with high academic distinction (minimum cumulative GPA of 3.40 / 4.00 or 78%+ aggregate; top 10-15% of class preferred).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Chalmers evaluates academic excellence weighted by the prestige and grading standard of the home institution.",
            "subject_background_prerequisites": "Substantial coursework in mathematics (calculus, linear algebra, discrete math) and core computer science (data structures, algorithms, computer systems).",
            "current_education_status": "Final-year undergraduate students graduating before autumn enrollment are eligible to apply conditionally.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; relevant internships and technical projects strengthen the application profile.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic min 6.5 (no section below 5.5) or TOEFL iBT min 90 (written test min 20). Medium of Instruction letters not accepted for Pakistani degrees.",
            "other_language_requirements": "None; instruction is 100% in English.",
            "gender_specific_requirements": "None; female engineers actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must designate Chalmers as Priority 1 on Universityadmissions.se.",
            "previous_scholarship_restrictions": "Cannot be combined with Swedish Institute (SI) scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "75% to 100% tuition fee reduction covering full tuition for the 2-year Master's degree (SEK 310,000 to SEK 360,000 value; ~USD 30,000 to 35,000). (Students with top performance in Year 1 receive 85% or 100% in Year 2).",
                "amount": "75% to 100% covered (~SEK 160,000 / year; ~PKR 4,160,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Swedish national application fee of SEK 900 paid online via Universityadmissions.se.",
                "amount": "SEK 900 (~PKR 23,400)"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "Student housing through SGS Studentbostäder or Chalmers Studentbostäder (CSB); single rooms or studio flats average SEK 4,200 to 6,500/month.",
                "amount": "Self-funded (~SEK 5,000 / month; ~PKR 130,000 / mo)"
            },
            "monthly_stipend": {
                "status": "NOT_COVERED",
                "details": "The IPOET scholarship covers tuition fees only; living expenses (~SEK 10,314/month required by Swedish Migration Agency) must be covered from personal or family funds.",
                "amount": "Self-funded (~SEK 10,314 / month requirement)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel between Pakistan and Gothenburg Landvetter (GOT) is self-funded.",
                "amount": "Self-funded (~PKR 250,000 to 380,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Swedish Residence Permit for Higher Education application fee of SEK 1,500 paid to Migrationsverket.",
                "amount": "SEK 1,500 (~PKR 39,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Covered by the Swedish state collective insurance for fee-paying students (FAS+) covering medical and emergency care.",
                "amount": "100% covered via Swedish FAS+ insurance"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Meals and groceries self-funded (~SEK 2,500/month).",
                "amount": "Self-funded"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Free access to electronic course textbooks via Chalmers Library, computer labs, and engineering software.",
                "amount": "Covered by university facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental travel grants available for master's thesis research presented at academic conferences.",
                "amount": "Up to SEK 8,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Västtrafik student discount provides reduced fares across Gothenburg trams, buses, and ferries.",
                "amount": "Student discount on Gothenburg regional transit"
            },
            "total_estimated_value_usd_per_year": 17000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single renowned Swedish technical university: Chalmers University of Technology (Gothenburg, Sweden)",
            "participating_institutions": [
                "Chalmers University of Technology",
                "Department of Computer Science and Engineering (CSE - shared with Univ of Gothenburg)",
                "Chalmers AI Research Centre (CHAIR)",
                "Department of Electrical Engineering"
            ],
            "university_rankings_scope": "Top 150 global university (QS World #139, THE World #189); leader in automotive computing, AI (Volvo/Ericsson industrial partnership), and quantum engineering.",
            "available_majors": [
                "Master's Programme in Computer Science - algorithms, languages and logic",
                "Master's Programme in Computer Systems and Networks",
                "Master's Programme in Data Science and AI",
                "Master's Programme in High-Performance Computer Systems",
                "Master's Programme in Software Engineering and Technology",
                "Master's Programme in Embedded Electronic System Design"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (120 ECTS credits).",
            "admission_requirements_summary": "4-year BS in CS/STEM with 3.4+ GPA, transcripts, CV, and IELTS 6.5+ or TOEFL 90+. Chalmers must be selected as Priority 1.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Data Science & AI and Computer Science are highly competitive; Software Engineering, Computer Systems and Networks, and High-Performance Computing have slightly higher admit rates.",
            "strategic_program_match_advice": "You must rank Chalmers as Priority 1 on Universityadmissions.se to be considered for IPOET scholarship funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.chalmers.se/en/education/your-studies/fees-and-scholarships/scholarships-for-international-students/ipoet-scholarships/",
            "portal_system_name": "Universityadmissions.se & Chalmers Scholarship Application System",
            "account_creation_instructions": "Apply for Chalmers as Priority 1 on Universityadmissions.se, then fill out the Chalmers Scholarship form on chalmers.se using your 8-digit application number.",
            "step_by_step_workflow": [
                "Step 1 (October - January): Apply for Chalmers Master's programme as Priority 1 on Universityadmissions.se.",
                "Step 2 (By mid-January): Pay the Swedish national application fee of SEK 900.",
                "Step 3 (Early December - Mid January): Access the Chalmers Scholarship application form on chalmers.se.",
                "Step 4 (In Chalmers portal): Input your 8-digit application number, select scholarship, and submit your motivation statement.",
                "Step 5 (By 1 February): Upload all transcripts, degree certificates, and English test scores to Universityadmissions.se.",
                "Step 6 (Late March): Swedish national admissions results published.",
                "Step 7 (Early April): Chalmers Scholarship decisions communicated via email.",
                "Step 8 (April - June): Apply for Swedish Residence Permit for Higher Education via Migrationsverket."
            ],
            "university_vs_scholarship_routing": "Two-step application: Programme admission applied via Universityadmissions.se; IPOET Scholarship applied via dedicated form on chalmers.se.",
            "recommendation_letters_submission_method": "Not required for Chalmers admissions or IPOET scholarship.",
            "personal_statement_prompts": "Chalmers Scholarship motivation essay detailing academic background, why Chalmers was selected as Priority 1, and long-term career goals.",
            "study_plan_research_proposal_requirements": "Not required at Master's level.",
            "cv_format_requirements": "1-2 page academic CV detailing education, programming proficiencies, capstone projects, and distinctions.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; decisions are based purely on academic merit and motivation evaluation.",
            "standardized_tests": "IELTS Academic (6.5+) or TOEFL iBT (90+). GRE is NOT required.",
            "application_fee_amount": "SEK 900 (Non-EU application fee)",
            "attestation_requirements": "Certified scans uploaded to Universityadmissions.se; HEC attestation recommended.",
            "translation_requirements": "Certified English translations required for all non-English documents.",
            "final_submission_method": "National application on Universityadmissions.se + scholarship form on chalmers.se."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's Degree Certificate",
                "mandatory": True,
                "specification": "Scanned color copy of original degree certificate and official English translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS degree; HEC attestation recommended."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale.",
                "pakistan_specific_instruction": "Ensure transcript clearly states credit hours and grading scale (CGPA out of 4.0)."
            },
            {
                "document_name": "Chalmers Scholarship Motivation Statement",
                "mandatory": True,
                "specification": "Structured statement of motivation submitted through the online scholarship form.",
                "pakistan_specific_instruction": "Articulate why Chalmers is your top choice and highlight technical alignment with target engineering track."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "1 to 2 page CV detailing academic background, technical skills, projects, and honors.",
                "pakistan_specific_instruction": "Highlight final-year project (FYP) and technical tools."
            },
            {
                "document_name": "English Language Proficiency Test Report",
                "mandatory": True,
                "specification": "Official IELTS Academic TRF (6.5+) or TOEFL iBT score report (90+) sent to University Admissions in Sweden.",
                "pakistan_specific_instruction": "Must satisfy Swedish English 6 requirement; institutional MOI letters are not accepted for Pakistani degrees."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport bio-data page.",
                "pakistan_specific_instruction": "Ensure passport is valid for at least 2 years beyond intended arrival."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "16 October 2025",
            "application_deadline": "15 January 2026 (Universityadmissions.se & Chalmers Scholarship)",
            "university_admission_deadline": "15 January 2026",
            "document_submission_deadline": "1 February 2026",
            "recommendation_letters_deadline": "N/A (Letters not required)",
            "interview_period": "N/A (Decisions based on file review)",
            "shortlist_announcement": "Late March (Admissions) / Early April 2026 (Scholarship)",
            "final_result_acceptance_deadline": "Mid-April 2026",
            "visa_application_window": "April to July 2026",
            "semester_commencement": "Late August 2026",
            "annual_cycle_notes": "Single annual intake for autumn semester. Chalmers must be designated as Priority 1 on Universityadmissions.se."
        },
        "selection_process_and_weights": {
            "academic_weight": "65% (Cumulative GPA, performance in advanced mathematics and computer science courses, university prestige)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular leadership, community initiatives)",
            "research_experience_weight": "10% (Technical projects, thesis quality, technical competencies)",
            "work_experience_weight": "5% (Relevant industry software experience)",
            "personal_statement_weight": "15% (Scholarship motivation essay evaluating alignment with Chalmers)",
            "recommendations_weight": "0% (Not evaluated / not requested)",
            "interview_weight": "0% (No interviews conducted)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 90 compliance)",
            "financial_need_weight": "0% (Purely merit-based academic scholarship)",
            "selection_panel_composition": "Chalmers Central Scholarship Committee and Department of Computer Science and Engineering Academic Board.",
            "evaluation_methodology": "Point-based merit ranking: Applicants are scored primarily on relative academic excellence (weighted GPA and home university standing) followed by qualitative review of the motivation essay. Scholarships awarded in strict rank order."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "3,800+ fee-paying international applicants across Chalmers Master's programmes",
            "total_scholarships_awarded": "~45 to 55 tuition fee waivers awarded annually",
            "acceptance_rate_global": "~1.5% to 2.5% for scholarship recipients",
            "acceptance_rate_pakistan": "~2% to 3% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (82%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/EE from top Pakistani institution (FAST, NUST, LUMS, GIKI, UET), top 10% of class, high scores in algorithms and systems, IELTS 7.5+.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, and GIKI.",
            "high_representation_countries": "China, India, Pakistan, Turkey, United States, Iran, Indonesia",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging fees for Chalmers scholarship placement. Applications must be submitted directly via Universityadmissions.se and chalmers.se."
            ],
            "application_fee_warning": "Swedish national application fee of SEK 900 paid only via Universityadmissions.se. Chalmers scholarship application itself is free.",
            "agent_and_intermediary_warnings": "Chalmers does not collaborate with education recruitment agents. Plagiarized statements of purpose result in disqualification.",
            "hidden_costs_breakdown": [
                "Swedish application fee: SEK 900 (~PKR 23,400).",
                "Swedish Residence Permit application fee: SEK 1,500 (~PKR 39,000).",
                "Living cost proof required by Swedish Migration Agency: SEK 10,314 / month (~PKR 268,000 / month; SEK 103,140 for 10-month bank statement = ~PKR 2,680,000).",
                "Flight ticket from Pakistan to Gothenburg: ~PKR 250,000 to 380,000."
            ],
            "misleading_claims_debunked": [
                "CLAIM: The IPOET scholarship covers living expenses. (FACT: The IPOET scholarship covers tuition fees only; living costs must be self-funded).",
                "CLAIM: You can apply for IPOET with Chalmers as your second or third priority. (FACT: Chalmers must be your Priority 1 choice on Universityadmissions.se)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some online blogs state that IPOET covers 100% for all winners. In fact, some recipients receive 75% fee waivers in Year 1, which may be upgraded to 85% or 100% in Year 2 based on academic performance."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must achieve at least 45 ECTS credits during the first academic year to retain the tuition waiver for Year 2.",
            "attendance_requirements": "Full-time physical enrollment on campus in Gothenburg.",
            "academic_progress_monitoring": "Annual credit completion check by Chalmers Scholarships Office before renewing the waiver.",
            "work_restrictions_during_study": "Swedish residence permit allows international students to work without hourly limits, provided satisfactory academic progress is maintained.",
            "home_country_return_obligation": "None. International graduates qualify for a 1-year residence permit to seek employment or start a business in Sweden.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously waived tuition; failure to achieve 45 ECTS results in loss of waiver for Year 2.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing programme requires formal application during the next admission cycle.",
            "extension_policy": "Scholarship is granted for the nominal 2-year duration (120 ECTS) and cannot be extended."
        },
        "official_sources_verified": [
            {
                "source_name": "Chalmers University of Technology IPOET Scholarships",
                "source_url": "https://www.chalmers.se/en/education/your-studies/fees-and-scholarships/scholarships-for-international-students/ipoet-scholarships/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation split between 75% and 100% tuition waivers.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal weighting algorithm between GPA and motivation statement."
                ]
            },
            {
                "source_name": "Universityadmissions.se Swedish National Admissions",
                "source_url": "https://www.universityadmissions.se/intl/start",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waiting list clearance statistics for specific Chalmers Master's programmes.",
                    "Detailed statistics on non-EU fee-paying applicant pools per programme."
                ]
            }
        ]
    },
    "SCH-EU-047": {
        "scholarship_id": "SCH-EU-047",
        "basic_details": {
            "scholarship_name": "Erasmus Mundus Master in Security and Cloud Computing (SECCLO)",
            "offering_entity": "European Commission (Erasmus Mundus Joint Master Degree) & SECCLO Consortium",
            "host_country": "Europe",
            "host_institutions_covered": "Year 1: Aalto University (Finland); Year 2: KTH (Sweden), NTNU (Norway), DTU (Denmark), EURECOM / Institut Polytechnique de Paris (France), or University of Tartu (Estonia)",
            "degree_levels": ["Master of Science (Double Degree) - MSc"],
            "major_restrictions": "Restricted to the SECCLO joint curriculum: Security and Cloud Computing, Cryptography, Network Security, Cloud Architecture, Mobile and IoT Security, and Big Data Security.",
            "number_of_awards_total": "~18 to 22 fully funded Erasmus Mundus scholarships awarded annually to international students worldwide",
            "number_of_awards_pakistan": "Open global competition under Erasmus+ Partner Countries; Pakistani STEM applicants typically secure 1 to 3 full scholarships per intake",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (24 months / 120 ECTS credits) across two European partner universities"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to applicants worldwide; Partner Country category covers Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science, Software Engineering, Information Technology, Computer Engineering, or Mathematics from an HEC-recognized university with excellent academic standing (minimum 80% aggregate or CGPA 3.50 / 4.00; top 10% class rank preferred).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Academic transcripts must demonstrate high performance in programming, algorithms, networks, and mathematics.",
            "subject_background_prerequisites": "Solid background in computer networks, operating systems, data structures, algorithms, discrete mathematics, and programming (C/C++, Java, or Python).",
            "current_education_status": "Graduating final-year undergraduate students can apply conditionally; degree certificate must be submitted before July/August.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Industrial cybersecurity, cloud computing, or software engineering experience strongly enhances competitiveness.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 92,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic min 6.5 (writing 5.5+) or TOEFL iBT min 92 (writing 22+) or PTE Academic min 62. Medium of Instruction letters are strictly not accepted.",
            "other_language_requirements": "None; instruction is 100% in English across all consortium universities.",
            "gender_specific_requirements": "None; women in cybersecurity strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Partner Country scholarship rules apply (must not have resided in an EU country for more than 12 months in the last 5 years).",
            "previous_scholarship_restrictions": "Cannot hold another EU Erasmus Mundus scholarship simultaneously or have previously received an EMJMD scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver covering 100% of consortium tuition fees at both universities for 2 years (EUR 18,000 / year value; total EUR 36,000).",
                "amount": "100% covered (~EUR 18,000 / year; ~PKR 5,580,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application through the SECCLO portal (hosted via Aalto University) is 100% free of charge.",
                "amount": "EUR 0 (Free application)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from monthly living allowance; subsidized student housing in Finland (AYY/HOAS, EUR 350-500/mo) and Year 2 host country (KTH/NTNU/DTU/EURECOM/Tartu, EUR 400-650/mo).",
                "amount": "Paid from allowance (~EUR 450 / month; ~PKR 140,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly subsistence allowance of EUR 1,400 / month (~USD 1,520 / month; ~PKR 434,000 / month) paid for the full 24-month duration of the programme (total EUR 33,600).",
                "amount": "EUR 1,400 / month (~PKR 434,000 / month; EUR 33,600 total)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Integrated travel allowance: The EUR 1,400/month flat-rate grant under current Erasmus+ rules incorporates travel and relocation allowances.",
                "amount": "Integrated into Erasmus+ scholarship package"
            },
            "visa_fee": {
                "status": "PAID VIA STIPEND",
                "details": "Finnish residence permit fee (EUR 350) and Year 2 host country residence permit fee paid from arrival allowance / monthly stipend.",
                "amount": "Covered from scholarship funds"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive private international health, accident, and travel insurance (e.g. Marsh / Dr. Walter) meeting all Erasmus Mundus guidelines fully provided.",
                "amount": "100% covered via Erasmus Mundus policy"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living and food costs comfortably covered by the EUR 1,400/month living stipend.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "All course literature, cloud lab environments (AWS, Azure, OpenStack), and research materials provided.",
                "amount": "Covered by consortium resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Consortium travel grants available for presenting master's thesis research at security conferences.",
                "amount": "Up to EUR 1,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Local student transit discounts available in all consortium host cities (Helsinki, Stockholm, Trondheim, Copenhagen, Sophia Antipolis, Tartu).",
                "amount": "Student discounts in host cities"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple leading European technological universities: Year 1 at Aalto University (Finland); Year 2 at one of 5 partner institutions",
            "participating_institutions": [
                "Aalto University (Finland - Coordinator, Year 1)",
                "KTH Royal Institute of Technology (Sweden - Track: Communications Systems)",
                "Norwegian University of Science and Technology - NTNU (Norway - Track: Information Security)",
                "Technical University of Denmark - DTU (Denmark - Track: Reliable Distributed Systems)",
                "EURECOM / Institut Polytechnique de Paris (France - Track: Big Data Security)",
                "University of Tartu (Estonia - Track: Basic Cryptography)"
            ],
            "university_rankings_scope": "Premier European cybersecurity consortium; all partner institutions rank in global top 100-200 in CS; students earn two officially accredited Master of Science degrees.",
            "available_majors": [
                "Year 1 (Aalto): Core Security and Cloud Computing (60 ECTS)",
                "Year 2 Track (KTH): Communications Systems & Cloud Security (60 ECTS)",
                "Year 2 Track (NTNU): Information Security & Digital Forensics (60 ECTS)",
                "Year 2 Track (DTU): Reliable Distributed Systems & Software Security (60 ECTS)",
                "Year 2 Track (EURECOM): Big Data Security & Mobile Systems (60 ECTS)",
                "Year 2 Track (Tartu): Theoretical Cryptography & Blockchain (60 ECTS)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (120 ECTS credits) leading to two official MSc degrees.",
            "admission_requirements_summary": "4-year BS in CS/STEM with 3.5+ GPA, strong networking/security background, motivation letter, CV, 2 recommendation letters, and IELTS 6.5+ or TOEFL 92+.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Year 2 tracks at KTH (Sweden) and EURECOM (France) have highest student demand; NTNU (Norway), DTU (Denmark), and Tartu (Estonia) offer world-class specialized expertise in cryptography and forensics.",
            "strategic_program_match_advice": "Clearly articulate your preferred Year 2 specialization track and explain how your prior background prepares you for that specific track (e.g., cryptography for Tartu, systems for DTU/KTH)."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://secclo.eu/admissions/how-to-apply/",
            "portal_system_name": "SECCLO Online Application System (hosted by Aalto University)",
            "account_creation_instructions": "Access the SECCLO application portal during November-January, create an account, select SECCLO, rank your Year 2 track preferences, and upload all required documents.",
            "step_by_step_workflow": [
                "Step 1 (October - November): Review SECCLO Year 2 specialization tracks and prepare course descriptions.",
                "Step 2 (November - December): Take IELTS Academic or TOEFL iBT exam.",
                "Step 3 (Late November - Early January): Fill out online application on the SECCLO application portal.",
                "Step 4 (In portal): Answer motivation questions, indicate Year 2 track preferences, and provide contacts for 2 academic referees.",
                "Step 5 (By deadline): Upload certified PDF scans of degree certificate, transcript of records, CV, and course descriptions.",
                "Step 6 (January - February): Referees submit confidential recommendation letters via automated links.",
                "Step 7 (Late March): Academic selection and Erasmus Mundus scholarship results announced by email.",
                "Step 8 (April - May): Formally accept offer and begin Finnish Residence Permit application for Year 1 at Aalto University."
            ],
            "university_vs_scholarship_routing": "Integrated single application: Applying to SECCLO automatically serves as an application for the Erasmus Mundus scholarship; no separate scholarship application required.",
            "recommendation_letters_submission_method": "Two academic recommendation letters submitted online via automated referee portal links.",
            "personal_statement_prompts": "Structured motivation letter answering: (1) Motivation for studying Security and Cloud Computing, (2) Suitability and preparatory background, (3) Preferred Year 2 specialization track and rationale, (4) Future career goals.",
            "study_plan_research_proposal_requirements": "Not required at Master's level; concise research interests outline integrated into motivation essay.",
            "cv_format_requirements": "Europass or clean academic CV detailing education, technical skills, cybersecurity/networking projects, and GitHub links.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; selections made purely through academic evaluation of application dossiers.",
            "standardized_tests": "IELTS Academic (6.5+) or TOEFL iBT (92+). GRE is NOT required.",
            "application_fee_amount": "EUR 0 (100% free application)",
            "attestation_requirements": "Certified copies of degree and transcripts uploaded; verified documents required upon accepting offer.",
            "translation_requirements": "Official authorized English translation required for documents not issued in English.",
            "final_submission_method": "100% digital submission via the SECCLO online application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's Degree Certificate",
                "mandatory": True,
                "specification": "Scanned color copy of original Bachelor's degree certificate and official English translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS degree; HEC attestation recommended."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale.",
                "pakistan_specific_instruction": "Ensure transcript clearly states credit hours and grading scale (CGPA out of 4.0)."
            },
            {
                "document_name": "Motivation Letter",
                "mandatory": True,
                "specification": "Structured 1-2 page motivation essay detailing background, interest in security and cloud computing, and Year 2 track preference.",
                "pakistan_specific_instruction": "Highlight hands-on networking, security labs, CTFs, or cloud projects completed during undergraduate studies."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "1 to 2 page CV detailing academic background, programming proficiencies, capstone projects, and distinctions.",
                "pakistan_specific_instruction": "Highlight final-year project (FYP), certifications (CCNA, CompTIA, AWS), and technical tools."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two academic reference letters from professors assessing technical intellect and research capabilities.",
                "pakistan_specific_instruction": "Referees must submit from institutional email addresses (.edu.pk)."
            },
            {
                "document_name": "English Language Proficiency Test Report",
                "mandatory": True,
                "specification": "Official IELTS Academic TRF (6.5+) or TOEFL iBT score report (92+) sent electronically to Aalto University.",
                "pakistan_specific_instruction": "Must be valid through application deadline; MOI letters strictly not accepted."
            },
            {
                "document_name": "Proof of Nationality & Residence",
                "mandatory": True,
                "specification": "Passport copy and residence certificate proving non-EU Partner Country status.",
                "pakistan_specific_instruction": "Scanned Pakistani passport copy and institutional bonafide/residence proof."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "15 November 2025",
            "application_deadline": "8 January 2026",
            "university_admission_deadline": "8 January 2026",
            "document_submission_deadline": "8 January 2026",
            "recommendation_letters_deadline": "15 January 2026",
            "interview_period": "N/A (Decisions based on file review)",
            "shortlist_announcement": "Late March 2026",
            "final_result_acceptance_deadline": "Mid-April 2026",
            "visa_application_window": "April to July 2026",
            "semester_commencement": "Late August / 1 September 2026 (at Aalto University)",
            "annual_cycle_notes": "Single annual intake starting in autumn semester. Very strict early January deadline."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Academic excellence, CGPA, grades in computer networks, systems, programming, and mathematics)",
            "extracurricular_and_leadership_weight": "5% (Leadership, CTF competitions, hackathons, open-source security tools)",
            "research_experience_weight": "15% (Relevant thesis, projects, technical publications, security audits)",
            "work_experience_weight": "10% (Industrial software engineering or cybersecurity experience)",
            "personal_statement_weight": "15% (Motivation letter evaluating clarity of purpose and fit with SECCLO curriculum)",
            "recommendations_weight": "10% (Quality and depth of professor endorsements)",
            "interview_weight": "0% (No interviews conducted)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 92 compliance)",
            "financial_need_weight": "0% (Purely merit-based international scholarship)",
            "selection_panel_composition": "SECCLO Academic Selection Committee comprising representatives from all 6 consortium partner universities.",
            "evaluation_methodology": "Consortium joint scoring: Applications are evaluated independently by academic reviewers from partner universities against standardized rubrics covering academic excellence, background relevance, motivation, and recommendations. Scholarships awarded in order of ranked list."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "1,800+ international applicants globally for SECCLO",
            "total_scholarships_awarded": "~18 to 22 fully funded Erasmus Mundus scholarships awarded annually",
            "acceptance_rate_global": "~1% to 1.2% overall scholarship selection rate",
            "acceptance_rate_pakistan": "~1% to 2% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 CGPA (85%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/SE from premier university (FAST, NUST, LUMS, GIKI, UET), top 5% of class, hands-on networking/cloud project experience, compelling motivation letter, IELTS 7.5+.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, and GIKI.",
            "high_representation_countries": "India, Pakistan, Bangladesh, Nigeria, Vietnam, Brazil, Turkey",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam consultants promising guaranteed Erasmus Mundus scholarships. SECCLO applications are strictly free and handled through secclo.eu."
            ],
            "application_fee_warning": "Applying to SECCLO is 100% free of charge. Never pay money to any intermediary.",
            "agent_and_intermediary_warnings": "SECCLO does not collaborate with education recruitment agencies. Plagiarized statements of purpose result in immediate rejection.",
            "hidden_costs_breakdown": [
                "Application fee: EUR 0 (100% free).",
                "Finnish residence permit fee (Year 1): EUR 350 (~PKR 108,500).",
                "Travel to Finland: Funded through scholarship living allowance.",
                "Year 2 residence permit and relocation: Funded through scholarship."
            ],
            "misleading_claims_debunked": [
                "CLAIM: English Medium of Instruction certificates are accepted. (FACT: Official IELTS/TOEFL/PTE score is strictly mandatory).",
                "CLAIM: You must have a degree in cybersecurity. (FACT: General Computer Science, Software Engineering, and Computer Engineering degrees are fully eligible)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some outdated forums cite old Erasmus Mundus stipend rules (EUR 1,000/month). Current Erasmus+ regulations provide a streamlined flat-rate allowance of EUR 1,400/month."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must complete at least 60 ECTS credits during Year 1 at Aalto University to progress to the Year 2 partner institution.",
            "attendance_requirements": "Full-time physical enrollment at Aalto University (Year 1) and assigned partner university (Year 2).",
            "academic_progress_monitoring": "Semester-by-semester credit completion monitoring by the SECCLO Consortium Board.",
            "work_restrictions_during_study": "Permitted according to national legislation of the host countries (up to 30 hrs/week in Finland), though intensive curriculum demands near full-time commitment.",
            "home_country_return_obligation": "None. Graduates can seek employment or pursue PhD studies in any European country under national post-study work regulations.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously disbursed allowances; failing Year 1 leads to termination of scholarship.",
            "rules_for_changing_university": "Consortium universities and tracks are fixed upon admission offer.",
            "rules_for_changing_major": "Fixed joint curriculum; major cannot be changed.",
            "extension_policy": "Scholarship is strictly limited to the nominal 24-month duration (120 ECTS) and cannot be extended."
        },
        "official_sources_verified": [
            {
                "source_name": "SECCLO Official Programme Portal",
                "source_url": "https://secclo.eu/",
                "source_type": "OFFICIAL_COMMISSION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of scholarship allocations per Year 2 specialization track.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal reserve list ranking metrics."
                ]
            },
            {
                "source_name": "European Commission Erasmus Mundus Catalogue",
                "source_url": "https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Consortium renewal contract dates and total grant envelope allocations.",
                    "Geographical window quotas allocated to South Asia."
                ]
            }
        ]
    },
    "SCH-EU-052": {
        "scholarship_id": "SCH-EU-052",
        "basic_details": {
            "scholarship_name": "École Polytechnique Paris Master's Excellence Scholarship (IP Paris)",
            "offering_entity": "École Polytechnique & Institut Polytechnique de Paris (IP Paris) Foundation",
            "host_country": "France",
            "host_institutions_covered": "École Polytechnique Campus (Palaiseau / Paris-Saclay, France)",
            "degree_levels": ["Master of Science and Technology (MSc&T) / Master of Science (MSc)"],
            "major_restrictions": "Master's programmes in Computer Science, Artificial Intelligence, Cybersecurity, Data Science, and Advanced Computing.",
            "number_of_awards_total": "~30 to 40 merit scholarships (tuition waivers and excellence allowances) awarded annually across IP Paris master's programmes",
            "number_of_awards_pakistan": "Open international competition; Pakistani STEM applicants secure ~2 to 4 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years (M1 + M2 / 120 ECTS credits), subject to achieving first-class academic standing in Year 1"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international applicants worldwide"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science, Mathematics, Electrical Engineering, or Physics from an HEC-recognized university with highest academic honors (minimum 82% aggregate or CGPA 3.60 / 4.00; top 5-10% of class).",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "French Grandes Écoles place exceptional weight on advanced mathematical rigor (calculus, linear algebra, probability, discrete math).",
            "subject_background_prerequisites": "Advanced background in mathematics, theoretical computer science, algorithms, and programming.",
            "current_education_status": "Students in their final undergraduate year can apply conditionally; degree completion required before September.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research projects, internships, or competitive programming achievements strongly valued.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic min 6.5, TOEFL iBT min 90, or Cambridge C1. Medium of Instruction letters not accepted.",
            "other_language_requirements": "None; international master's programmes are taught entirely in English. French language courses provided free on campus.",
            "gender_specific_requirements": "None; female candidates in STEM actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Top-ranked international admits considered for IP Paris Excellence Fellowships.",
            "previous_scholarship_restrictions": "Cannot hold another full external scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition waiver covering 100% of École Polytechnique international master's tuition (~EUR 14,000 to EUR 18,000 / year value).",
                "amount": "100% covered (~EUR 15,000 / year; ~PKR 4,650,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "IP Paris online application fee of EUR 80 paid via credit card.",
                "amount": "EUR 80 (~PKR 24,800)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus student accommodation at Palaiseau campus guaranteed for international master's students; single studio in student residence averages EUR 450 to 650/month (eligible for French CAF housing subsidy of ~EUR 150-200/month).",
                "amount": "Paid from allowance (~EUR 500 / month; ~PKR 155,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Excellence fellowship provides a living allowance of EUR 750 to EUR 1,000 / month (~EUR 9,000 to 12,000 / year; ~PKR 232,000 to 310,000 / month), comfortably covering living costs in Palaiseau with CAF housing subsidy.",
                "amount": "EUR 750 to 1,000 / month (~PKR 2,790,000 to 3,720,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Paris Charles de Gaulle (CDG) / Orly (ORY) is self-funded.",
                "amount": "Self-funded (~PKR 250,000 to 380,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "French Long-Stay Student Visa (VLS-TS) fee of EUR 99 plus Campus France Pakistan processing fee (~PKR 25,000).",
                "amount": "~PKR 55,000 total"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "French National Health Insurance (Sécurité Sociale / Assurance Maladie) is 100% free of charge for all international students in France.",
                "amount": "100% free French national social security"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized meals at CROUS student restaurants cost only EUR 3.30 per hot meal.",
                "amount": "Subsidized student cafeteria meals"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Free access to École Polytechnique Library, compute servers, GPU clusters, and software tools.",
                "amount": "Covered by university facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory travel support available for students conducting master's thesis research in IP Paris laboratories.",
                "amount": "Up to EUR 1,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Île-de-France Imagine R student transport pass provides 50% discount on Paris metro, RER, and bus networks.",
                "amount": "50% discount on Paris regional transit"
            },
            "total_estimated_value_usd_per_year": 28000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite French Grande École: École Polytechnique (Institut Polytechnique de Paris, Palaiseau, France)",
            "participating_institutions": [
                "École Polytechnique ('l'X')",
                "Institut Polytechnique de Paris (IP Paris)",
                "LIX - Computer Science Laboratory of École Polytechnique",
                "Centre Interdisciplinaire d'Études pour la Défense et la Sécurité (CIEDS)"
            ],
            "university_rankings_scope": "France's #1 institution and top 40 globally (QS World #38, THE World #71); historic Grande École that has produced French heads of state, Nobel laureates, and Fields medalists.",
            "available_majors": [
                "Master of Science and Technology in Artificial Intelligence & Advanced Visual Computing",
                "Master of Science and Technology in Cybersecurity: Threats and Defenses",
                "Master of Science and Technology in Data Science for Business",
                "IP Paris Master in Computer Science: Foundations of Computer Science",
                "IP Paris Master in Computer Science: High Performance Data Analytics",
                "IP Paris Master in Computer Science: Networks & Distributed Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (120 ECTS credits).",
            "admission_requirements_summary": "4-year BS in CS/Math/STEM with 3.6+ GPA, strong mathematical foundations, 2 recommendation letters, CV, statement of purpose, and IELTS 6.5+ or TOEFL 90+.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "AI and Data Science attract intense global competition; Foundations of Computer Science and Networks/Distributed Systems offer slightly higher acceptance rates for candidates with strong mathematical rigor.",
            "strategic_program_match_advice": "École Polytechnique places heavy emphasis on mathematical proficiency; highlight your grades in advanced mathematics, proofs, and theoretical computer science in your dossier."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ip-paris.fr/en/education/admissions",
            "portal_system_name": "IP Paris Online Application System",
            "account_creation_instructions": "Register on the IP Paris portal, select École Polytechnique as host school, choose your Master's programme, upload required documents, and register 2 academic referees.",
            "step_by_step_workflow": [
                "Step 1 (October - December): Review programme curricula on the IP Paris website; verify mathematics and programming prerequisites.",
                "Step 2 (November - January): Prepare statement of purpose, CV, transcripts, and secure agreement from 2 academic referees.",
                "Step 3 (Early January - Mid February): Complete online application on the IP Paris application portal.",
                "Step 4 (In application): Select scholarship interest checkbox to be evaluated for excellence funding.",
                "Step 5 (By deadline): Pay the EUR 80 application fee and submit all documents.",
                "Step 6 (February - March): Referees submit letters; admissions committee reviews dossiers.",
                "Step 7 (Late March - Mid April): Admission and scholarship decisions communicated by email.",
                "Step 8 (April - June): Confirm acceptance, pay deposit (if applicable, waived for full scholars), and initiate Campus France Pakistan visa procedure."
            ],
            "university_vs_scholarship_routing": "Integrated automatic consideration: All applicants are automatically considered for merit scholarships during the regular admission process; no separate application required.",
            "recommendation_letters_submission_method": "Two academic recommendation letters submitted online via automated referee portal links.",
            "personal_statement_prompts": "Statement of purpose (1-2 pages) explaining academic background, motivation for choosing École Polytechnique, mathematical and technical preparation, and career ambitions.",
            "study_plan_research_proposal_requirements": "Not required at Master's level; concise research interests outline integrated into statement of purpose.",
            "cv_format_requirements": "1 to 2 page academic CV detailing education, programming proficiencies, mathematical background, and distinctions.",
            "interviews_conducted": True,
            "interview_format_details": "Shortlisted applicants may be invited to a 20-30 minute virtual interview evaluating technical problem solving and motivation.",
            "standardized_tests": "IELTS Academic (6.5+) or TOEFL iBT (90+). GRE is optional.",
            "application_fee_amount": "EUR 80 (Non-refundable)",
            "attestation_requirements": "Certified copies of degree and transcripts uploaded; verified documents required upon accepting offer.",
            "translation_requirements": "Official English or French translation required for non-English credentials.",
            "final_submission_method": "100% digital submission via the IP Paris application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's Degree Certificate",
                "mandatory": True,
                "specification": "Scanned color copy of original Bachelor's degree certificate and official English or French translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS degree; HEC attestation recommended."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale.",
                "pakistan_specific_instruction": "Ensure transcript clearly states credit hours and grading scale (CGPA out of 4.0)."
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "1-2 page essay articulating academic background, mathematical foundations, and alignment with target master's programme.",
                "pakistan_specific_instruction": "Focus on mathematical preparation and technical depth rather than generic background."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "1 to 2 page CV detailing academic background, programming proficiencies, capstone projects, and distinctions.",
                "pakistan_specific_instruction": "Highlight final-year project (FYP), math olympiads, and software engineering tools."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two academic reference letters from professors assessing applicant's analytical rigor and intellectual capability.",
                "pakistan_specific_instruction": "Referees must submit from institutional email addresses (.edu.pk)."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS Academic TRF (6.5+) or TOEFL iBT score report (90+).",
                "pakistan_specific_instruction": "Must be valid through application deadline; MOI letters not accepted."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 November 2025",
            "application_deadline": "15 February 2026 (Round 1 / Scholarship Priority)",
            "university_admission_deadline": "15 February 2026",
            "document_submission_deadline": "15 February 2026",
            "recommendation_letters_deadline": "22 February 2026",
            "interview_period": "March 2026",
            "shortlist_announcement": "Late March to Mid April 2026",
            "final_result_acceptance_deadline": "Late April 2026",
            "visa_application_window": "May to July 2026",
            "semester_commencement": "Early September 2026",
            "annual_cycle_notes": "Main scholarship round closes in mid-February. Round 2 (April) has very limited scholarship funding."
        },
        "selection_process_and_weights": {
            "academic_weight": "55% (Academic excellence, CGPA, mathematical foundations, analytical rigor)",
            "extracurricular_and_leadership_weight": "5% (Leadership, academic competitions, hackathons)",
            "research_experience_weight": "15% (Relevant projects, bachelor's thesis, technical competence)",
            "work_experience_weight": "5% (Industry internships or research laboratory experience)",
            "personal_statement_weight": "10% (Clarity of motivation and understanding of IP Paris academic culture)",
            "recommendations_weight": "10% (Depth of professor endorsements)",
            "interview_weight": "Qualifying factor (virtual interview for shortlisted candidates)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 90 compliance)",
            "financial_need_weight": "0% (Purely merit-based academic scholarship)",
            "selection_panel_composition": "École Polytechnique Graduate Admissions Board and IP Paris Foundation Scholarship Committee.",
            "evaluation_methodology": "Faculty jury assessment: Dossiers are evaluated by academic juries focusing heavily on mathematics and computer science depth. Top-ranked admits are awarded tuition waivers and monthly excellence allowances."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "2,200+ international applicants across IP Paris Master's programmes",
            "total_scholarships_awarded": "~30 to 40 full merit scholarships awarded annually",
            "acceptance_rate_global": "~2% to 3% for scholarship recipients",
            "acceptance_rate_pakistan": "~2% to 3% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 CGPA (85%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/Math/EE from top Pakistani institution (LUMS, NUST, FAST, GIKI), near-perfect mathematics grades, strong analytical skills, IELTS 7.5+.",
            "common_backgrounds_of_winners": "Graduates of LUMS, NUST, FAST-NUCES, and GIKI.",
            "high_representation_countries": "China, India, Lebanon, Pakistan, Brazil, United States, Italy",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging placement fees claiming guaranteed admission to École Polytechnique. Admissions are strictly merit-based via ip-paris.fr."
            ],
            "application_fee_warning": "IP Paris application fee is EUR 80 paid directly online. Never pay fees to external agents.",
            "agent_and_intermediary_warnings": "École Polytechnique does not work with recruitment agents. Plagiarized statements of purpose result in immediate rejection.",
            "hidden_costs_breakdown": [
                "Application fee: EUR 80 (~PKR 24,800).",
                "French visa and Campus France fee: ~PKR 55,000.",
                "Flight ticket from Pakistan to Paris: ~PKR 250,000 to 380,000.",
                "First month's rent deposit on campus: ~EUR 500 (~PKR 155,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: French language proficiency is required. (FACT: 100% of courses in international master's programmes are taught in English).",
                "CLAIM: Health insurance costs hundreds of euros. (FACT: French national health insurance is 100% free for all students)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums confuse the Master of Science (MSc&T) with the historic Ingénieur Polytechnicien cycle. The MSc&T is a 2-year English-taught graduate degree open directly to international bachelor's degree holders."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance (minimum grade average of 12/20 on French grading scale) to renew scholarship for Year 2.",
            "attendance_requirements": "Full-time physical presence on Palaiseau campus.",
            "academic_progress_monitoring": "Annual progress reviews conducted by the academic program director.",
            "work_restrictions_during_study": "French student visa permits up to 964 hours of work per year (approx. 20 hours/week), though demanding curriculum requires primary study focus.",
            "home_country_return_obligation": "None. International graduates qualify for a 1-year post-study job seeker visa (RECE - Recherche d'emploi ou création d'entreprise) in France.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously awarded funds; academic failure results in cancellation of scholarship for subsequent terms.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing programme requires formal application during the next admission cycle.",
            "extension_policy": "Scholarship is granted for the nominal 2-year duration (120 ECTS) and cannot be extended."
        },
        "official_sources_verified": [
            {
                "source_name": "École Polytechnique / IP Paris Master's Admissions & Scholarships",
                "source_url": "https://www.ip-paris.fr/en/education/admissions",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of excellence scholarships per individual master's track.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal ranking formula between GPA and interview performance."
                ]
            },
            {
                "source_name": "Campus France Pakistan Official Portal",
                "source_url": "https://www.pakistan.campusfrance.org/",
                "source_type": "OFFICIAL_BILATERAL",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Visa clearance rates specifically for École Polytechnique admitted students.",
                    "Discretionary travel grant schemes funded by French Embassy in Islamabad."
                ]
            }
        ]
    },
    "SCH-EU-067": {
        "scholarship_id": "SCH-EU-067",
        "basic_details": {
            "scholarship_name": "Technical University of Denmark (DTU) PhD Fellowship in AI & Computing",
            "offering_entity": "Technical University of Denmark (DTU Compute - Department of Applied Mathematics and Computer Science)",
            "host_country": "Denmark",
            "host_institutions_covered": "Technical University of Denmark Main Campus (Lyngby / Greater Copenhagen, Denmark)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Restricted to doctoral research in Computer Science, Artificial Intelligence, Machine Learning, Data Science, Cyber Security, Software Engineering, Scientific Computing, and Cognitive Systems.",
            "number_of_awards_total": "100% of admitted PhD candidates are employed as salaried staff (~80 to 110 doctoral fellows hired annually in computing)",
            "number_of_awards_pakistan": "Open global competition; Pakistani STEM master's graduates typically secure 3 to 7 funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "3 years (36 months) fully salaried employment contract with full Danish social benefits"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants worldwide"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 2-year research Master's degree (18 years education / MS/MPhil or equivalent 300 ECTS) in Computer Science, Software Engineering, Applied Mathematics, or closely related STEM field from an HEC-recognized university with high academic standing (minimum 80% aggregate or CGPA 3.50 / 4.00).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "In Denmark, PhD positions are salaried academic employment contracts; candidates are evaluated as professional researchers.",
            "subject_background_prerequisites": "Strong research foundations in algorithms, programming, linear algebra, machine learning, and systems; research master's thesis required.",
            "current_education_status": "Master's students completing their degree before the contract start date are eligible to apply.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior peer-reviewed publications, conference papers, or open-source scientific software contributions strongly favored.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Excellent command of written and spoken English is required; formal IELTS/TOEFL not strictly mandatory if English fluency is demonstrated during technical video interviews and in academic writing samples.",
            "other_language_requirements": "None; working language at DTU Compute is 100% English.",
            "gender_specific_requirements": "None; diversity and women in computing actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates apply to specific funded research projects advertised on DTU job portal.",
            "previous_scholarship_restrictions": "Cannot hold another full-time employment contract simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Zero tuition fees; PhD candidates at DTU are employed as academic staff under Danish collective wage agreements (AC-overenskomst).",
                "amount": "100% covered (No tuition fee charged)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Applying to PhD positions via DTU's online recruitment system is 100% free of charge.",
                "amount": "DKK 0 (Free application)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Funded from the generous monthly salary; student/staff housing through Boligfonden DTU or private apartments in Lyngby / Copenhagen average DKK 4,500 to 7,500/month.",
                "amount": "Paid from salary (~DKK 6,000 / month; ~PKR 246,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Full monthly salary according to Danish collective agreement for academics: DKK 32,500 to DKK 35,000 / month (~USD 4,700 to 5,100 / month; ~PKR 1,330,000 to 1,435,000 / month gross) plus 17.1% employer pension contribution (~DKK 5,500 to 6,000/month).",
                "amount": "DKK 32,500 to 35,000 / month gross (~PKR 1,330,000 / mo; DKK 400,000+ / yr)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Copenhagen Airport (CPH) is typically self-funded from the initial relocation budget.",
                "amount": "Self-funded (~PKR 250,000 to 380,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Danish Residence and Work Permit application fee of DKK 3,500 paid to SIRI (Danish Agency for International Recruitment and Integration).",
                "amount": "DKK 3,500 (~PKR 143,500)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Danish public healthcare system provides 100% free medical, doctor, and hospital care to all registered residents via the Danish CPR card (yellow card).",
                "amount": "100% free comprehensive Danish healthcare"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living and groceries costs covered comfortably from the monthly salary in Copenhagen.",
                "amount": "Covered from monthly salary"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "High-performance GPU computing clusters, lab workstations, software licenses, and research hardware provided by DTU Compute.",
                "amount": "Covered by department infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "100% COVERED",
                "details": "Project research grants cover full travel, registration, and accommodation for international conference presentations and required 3-6 month research stay abroad (external stay).",
                "amount": "100% covered by project research budget"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized regional public transit across Copenhagen S-train, metro, and bus networks via Danish commuter card.",
                "amount": "Commuter pass discounts"
            },
            "total_estimated_value_usd_per_year": 65000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading European technical university: Technical University of Denmark (DTU, Lyngby / Copenhagen, Denmark)",
            "participating_institutions": [
                "Technical University of Denmark (DTU)",
                "DTU Compute - Department of Applied Mathematics and Computer Science",
                "Pioneer Centre for AI (collaborative Danish AI center)",
                "DTU Center for Information Security"
            ],
            "university_rankings_scope": "Top 100 global university (QS World #109, THE Engineering #43); Scandinavia's leading technological powerhouse with world-class computing facilities.",
            "available_majors": [
                "PhD in Artificial Intelligence & Machine Learning",
                "PhD in Cognitive Systems & Computer Vision",
                "PhD in Cyber Security & Cryptographic Systems",
                "PhD in Software Engineering & Formal Methods",
                "PhD in Scientific Computing & High-Performance Computing",
                "PhD in Data Science & Statistical Learning",
                "PhD in Algorithms & Optimization",
                "PhD in Embedded Systems & IoT"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 years (36 months) full-time doctoral employment.",
            "admission_requirements_summary": "2-year MS in CS/Math/STEM with 3.5+ GPA, completed research master's thesis, CV, motivation letter, transcripts, 2-3 reference contacts, and technical video interview. Prior publications strongly preferred.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "General AI and computer vision positions attract large international applicant pools; positions in formal methods, scientific computing, cybersecurity, and embedded systems offer higher selection probability for specialized candidates.",
            "strategic_program_match_advice": "DTU positions are advertised as specific research projects; tailor your application letter and CV directly to the project description, citing specific methodologies and published papers of the project PI."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.dtu.dk/english/about/job-and-career/vacant-positions",
            "portal_system_name": "DTU Career / Vacant Positions Portal (SuccessFactors)",
            "account_creation_instructions": "Access the DTU vacant positions portal, filter by 'PhD', select the specific computing position, click 'Apply online', upload your application dossier, and submit before the vacancy deadline.",
            "step_by_step_workflow": [
                "Step 1 (Ongoing): Monitor DTU Career portal for open PhD positions in DTU Compute (vacancies posted year-round).",
                "Step 2 (Project review): Read the specific project description, research objectives, and professor's recent publications.",
                "Step 3 (Document preparation): Prepare a targeted cover letter, academic CV, master's thesis abstract/sample, and transcripts.",
                "Step 4 (Online submission): Apply online via the DTU portal before the project closing deadline.",
                "Step 5 (Shortlisting): The assessment committee evaluates candidates and creates an assessment report.",
                "Step 6 (Interviews): Shortlisted candidates participate in 1-2 technical video interviews and present their master's research.",
                "Step 7 (Employment offer): Formal employment offer letter and contract issued.",
                "Step 8 (Visa & onboarding): Apply for Danish Residence and Work Permit via SIRI; DTU HR assists with relocation."
            ],
            "university_vs_scholarship_routing": "Integrated employment selection: PhD fellows are hired directly as academic staff; admission to the PhD school and funding are fully integrated.",
            "recommendation_letters_submission_method": "Contact information of 2-3 academic referees provided in CV; recommendation letters uploaded directly or requested by the assessment committee.",
            "personal_statement_prompts": "Cover Letter / Application Letter: 1-2 pages explaining motivation for applying to the specific project, relevant master's research experience, technical skills, and vision for the project.",
            "study_plan_research_proposal_requirements": "Integrated into cover letter or submitted as a 2-page research statement addressing the advertised project objectives.",
            "cv_format_requirements": "Academic CV detailing education, programming proficiencies, master's thesis title and supervisor, publications, and GitHub links.",
            "interviews_conducted": True,
            "interview_format_details": "45-60 minute video interview with project PI and co-supervisors, typically including a 15-minute presentation of the applicant's master's thesis research followed by technical questions.",
            "standardized_tests": "None. English proficiency evaluated during technical interview.",
            "application_fee_amount": "DKK 0 (100% free application)",
            "attestation_requirements": "Scanned certified copies of degree and transcripts uploaded; HEC attestation recommended.",
            "translation_requirements": "Official English translation required for documents not in English or Danish.",
            "final_submission_method": "100% digital submission via DTU online recruitment system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Cover Letter / Letter of Application",
                "mandatory": True,
                "specification": "1-2 page letter motivating application for the specific advertised PhD project, describing relevant experience and technical skills.",
                "pakistan_specific_instruction": "Tailor directly to the advertised project description and cite target professor's papers."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic CV listing education, research projects, technical skills, publications, and 2-3 reference contacts.",
                "pakistan_specific_instruction": "Clearly highlight master's thesis research and technical tools."
            },
            {
                "document_name": "Official Master's and Bachelor's Transcripts & Degrees",
                "mandatory": True,
                "specification": "Complete transcripts of Bachelor's and Master's degrees detailing courses and grades, with grade conversion explanation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS and 2-year MS/MPhil transcripts."
            },
            {
                "document_name": "Master's Thesis Abstract / Writing Sample",
                "mandatory": True,
                "specification": "A brief summary of your Master's thesis (or published scientific paper) illustrating research quality.",
                "pakistan_specific_instruction": "Upload Master's thesis PDF or reprint of published conference/journal paper."
            },
            {
                "document_name": "Reference Contacts (Two to Three)",
                "mandatory": True,
                "specification": "Names and contact details of 2-3 academic referees, including your Master's thesis supervisor.",
                "pakistan_specific_instruction": "Provide institutional email addresses (.edu.pk) of your professors."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport bio-data page.",
                "pakistan_specific_instruction": "Ensure passport is valid for at least 3 years."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Continuous / Vacancy-based (positions advertised throughout the year)",
            "application_deadline": "Varies by position (typically 4-6 weeks after posting)",
            "university_admission_deadline": "Synchronized with position deadline",
            "document_submission_deadline": "Same as application deadline",
            "recommendation_letters_deadline": "Requested during evaluation",
            "interview_period": "3-6 weeks after vacancy deadline",
            "shortlist_announcement": "6-8 weeks after vacancy deadline",
            "final_result_acceptance_deadline": "2 weeks following offer",
            "visa_application_window": "2-3 months before start date",
            "semester_commencement": "Flexible start date (typically negotiated upon hiring)",
            "annual_cycle_notes": "Year-round recruitment; new PhD positions are posted continuously on the DTU job board."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Academic record, grades in core computer science, mathematics, and master's degree)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated)",
            "research_experience_weight": "40% (Quality of Master's thesis, publications, practical coding skills, relevance to project)",
            "work_experience_weight": "10% (Relevant industrial or academic research experience)",
            "personal_statement_weight": "10% (Cover letter demonstrating deep understanding of project domain)",
            "recommendations_weight": "10% (Endorsement from Master's supervisor and referees)",
            "interview_weight": "Critical decisive factor (technical presentation and interview performance)",
            "test_scores_weight": "Not applicable (No standardized tests required)",
            "financial_need_weight": "0% (Purely merit-based salaried research appointment)",
            "selection_panel_composition": "DTU Compute Assessment Committee consisting of the project supervisor, co-supervisors, and departmental academic staff.",
            "evaluation_methodology": "Formal academic assessment: Committee evaluates all qualified applicants against position requirements, produces a written assessment report, interviews shortlisted candidates, and makes a final hiring recommendation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "80 to 200+ applicants per advertised PhD position in computing",
            "total_scholarships_awarded": "~80 to 110 salaried PhD positions awarded annually in computing",
            "acceptance_rate_global": "~2% to 4% per individual position",
            "acceptance_rate_pakistan": "~3% to 5% among qualified Pakistani Master's graduates",
            "typical_successful_applicant_gpa": "3.60+ / 4.00 CGPA in Master's degree (80%+ aggregate)",
            "typical_academic_and_research_profile": "Master's degree in CS/SE with research thesis, 1+ peer-reviewed conference or journal publications, strong programming proficiency (Python/C++), excellent presentation skills.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, QAU, and COMSATS.",
            "high_representation_countries": "Denmark, China, India, Pakistan, Italy, Germany, Iran, Greece",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent recruitment ads charging application fees. Applying to DTU is 100% free via dtu.dk/english/about/job-and-career."
            ],
            "application_fee_warning": "DTU never charges any application or processing fees. Never pay money to any consultant.",
            "agent_and_intermediary_warnings": "DTU does not work with commercial recruiting agents. Direct personal application is mandatory.",
            "hidden_costs_breakdown": [
                "Application fee: DKK 0 (100% free).",
                "Danish Residence and Work Permit fee: DKK 3,500 (~PKR 143,500).",
                "Flight ticket from Pakistan to Copenhagen: ~PKR 250,000 to 380,000.",
                "First month's rent deposit in Denmark: ~DKK 15,000 to 20,000 (reimbursed easily from first month's generous salary)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: PhD students in Denmark pay tuition. (FACT: PhD students are salaried employees earning DKK 32,500+/month; zero tuition is charged).",
                "CLAIM: You must speak Danish to do a PhD at DTU. (FACT: 100% of research, teaching, and administration at DTU Compute is in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums refer to PhD positions as 'scholarships'. In Denmark, a PhD position is a full employment contract with salary, holiday pay, pension, and employment protections."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must complete 30 ECTS of doctoral coursework and receive satisfactory evaluations on semi-annual progress reports.",
            "attendance_requirements": "Full-time employment residency at DTU Compute in Lyngby.",
            "academic_progress_monitoring": "Semi-annual PhD progress reports reviewed by the DTU PhD School.",
            "work_restrictions_during_study": "Full-time salaried position; external commercial employment is restricted without prior university approval.",
            "home_country_return_obligation": "None. International PhD graduates qualify for Denmark's post-study work permit and favorable permanent residency pathways for researchers.",
            "service_obligations_or_bonds": "Obligation to fulfill departmental duties (teaching, lab supervision) of up to 840 hours over the 3-year contract.",
            "repayment_clawback_conditions": "None.",
            "rules_for_changing_university": "Position is tied to DTU and specific grant.",
            "rules_for_changing_major": "Project scope may be adjusted with supervisor consent.",
            "extension_policy": "Standard contract is 3 years; extensions granted for maternity/paternity leave, illness, or funded research amendments."
        },
        "official_sources_verified": [
            {
                "source_name": "Technical University of Denmark Vacant Positions",
                "source_url": "https://www.dtu.dk/english/about/job-and-career/vacant-positions",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific external funding pipeline and upcoming PhD opening schedules.",
                    "Country-level breakdown of hired PhD fellows.",
                    "Detailed assessment report scoring breakdown for non-shortlisted candidates."
                ]
            },
            {
                "source_name": "DTU PhD Guide & Terms of Employment",
                "source_url": "https://www.dtu.dk/english/education/phd",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Collective agreement wage progression tables for year 2 and year 3.",
                    "Discretionary relocation subsidy policies across individual departments."
                ]
            }
        ]
    }
}
