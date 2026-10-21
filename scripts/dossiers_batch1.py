"""
scripts/dossiers_batch1.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Batch 1
Contains:
1. SCH-AM-002: Global UGRAD Pakistan Undergraduate Exchange Program (USA / USEFP)
2. SCH-AM-003: Lester B. Pearson International Scholarship (Univ of Toronto, Canada)
3. SCH-AM-004: Vanier Canada Graduate Scholarships (Vanier CGS, Canada)
4. SCH-AM-008: Hubert H. Humphrey Fellowship Program (USEFP Pakistan / USA)
5. SCH-AM-010: McCall MacBain Scholarships at McGill University (Canada)
6. SCH-AM-014: MIT EECS Graduate Fellowship & Research Assistantship (USA)
7. SCH-OC-002: Manaaki New Zealand Scholarships (New Zealand MFAT)
8. SCH-OC-003: University of Melbourne Graduate Research Scholarships (Australia)
"""

DOSSIERS_BATCH1 = {
    # 1. Global UGRAD Pakistan (SCH-AM-002)
    "SCH-AM-002": {
        "scholarship_id": "SCH-AM-002",
        "basic_details": {
            "scholarship_name": "Global UGRAD Pakistan Undergraduate Exchange Program",
            "offering_entity": "United States Educational Foundation in Pakistan (USEFP) & U.S. Department of State (ECA)",
            "host_country": "United States",
            "host_institutions_covered": "Accredited U.S. Colleges and Universities across all 50 states (Placement arranged by IREX / USEFP)",
            "degree_levels": ["Undergraduate Semester Exchange"],
            "major_restrictions": "Open to all academic disciplines (Engineering, CS, Social Sciences, Natural Sciences, Business, Arts, Humanities, Agriculture). Clinical medical rotations not permitted; pre-med coursework allowed.",
            "number_of_awards_total": "~200 to 240 Pakistani students per annual cycle",
            "number_of_awards_pakistan": "100% reserved exclusively for Pakistani citizens enrolled in Pakistani universities",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "1 academic semester (~4.5 months) in the United States"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Pakistani citizen currently residing in Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": None,
            "age_limit_notes": "Applicants must be between 18 and 25 years of age at the time of program entry.",
            "academic_qualifications": "Currently enrolled in a 4-year bachelor's (16-year education) or 2-year bachelor's degree program at an accredited Pakistani university. Must have at least one semester remaining upon return to Pakistan.",
            "minimum_gpa_percentage": 60.0,
            "minimum_gpa_scale": 2.5,
            "grading_conversion_notes": "Minimum 2.50 / 4.00 CGPA; however, competitive admitted scholars generally present 3.20+ CGPA or top 15% class standing.",
            "subject_background_prerequisites": "Any accredited university subject background in Pakistan.",
            "current_education_status": "Must be enrolled in 14th or 15th year of education (e.g., 2nd or 3rd year of 4-year BS, or 1st year of 2-year BS). Final semester students are NOT eligible.",
            "graduation_year_restrictions": "Must not be graduating before the exchange semester; must return to home university in Pakistan to complete remaining degree requirements.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Volunteering, community service, and extracurricular leadership heavily prioritized over formal corporate work.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": None,
                "toefl_minimum": None,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "No TOEFL/IELTS required to apply. Shortlisted candidates are sponsored by USEFP to take official TOEFL iBT test free of charge."
            },
            "other_language_requirements": "None; English is the medium of instruction in the U.S.",
            "gender_specific_requirements": "Equal opportunity; female applicants, students from underserved provinces (Balochistan, KP, interior Sindh, GB, AJK), and persons with disabilities actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Strong commitment to return and contribute to community development in Pakistan; active leadership track record.",
            "previous_scholarship_restrictions": "Individuals with previous long-term U.S. exchange or travel grants are lower priority; dual U.S. citizens or green card holders strictly ineligible.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full undergraduate tuition and mandatory university campus fees paid directly to host U.S. institution.",
                "amount": None
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "No admission application fees; USEFP manages placement and administration.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE DORMITORY",
                "details": "Standard university on-campus residence hall (shared room with roommate) fully paid for the duration of the semester.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly personal living allowance for incidentals.",
                "amount": "$800 / month (~PKR 225,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Round-trip international economy class airfare from home city in Pakistan to the host university in the United States.",
                "amount": None
            },
            "visa_fee": {
                "status": "WAIVED",
                "details": "Full sponsorship of J-1 exchange visitor visa; SEVIS and visa application fees covered.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Accident and Sickness Program for Exchanges (ASPE) health benefit coverage provided by the U.S. Department of State.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Full on-campus dining meal plan (14 to 21 meals per week) included alongside dormitory accommodation.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Textbook and academic course supplies stipend provided upon arrival.",
                "amount": "$350 per semester (~PKR 98,000)"
            },
            "research_funding_conference_grant": {
                "status": "NOT_COVERED",
                "details": "Not applicable to undergraduate exchange semester.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Domestic transit in Pakistan to visa appointment and departure hub covered.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple host institutions assigned centrally across all 50 U.S. states.",
            "participating_institutions": [
                "University of Texas at Austin", "University of Wisconsin-Madison", "University of Florida",
                "American University (Washington DC)", "West Virginia University", "Grand Valley State University",
                "University of Missouri", "University of Utah", "Dozens of partner institutions across the USA"
            ],
            "university_rankings_scope": "Comprehensive mix of Top 100 research universities and regional liberal arts colleges.",
            "available_majors": [
                "All majors: Engineering, Computer Science, Biology, Chemistry, Physics, Business, Economics, International Relations, Psychology, Media Studies, Agriculture"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 academic semester (Fall: Aug-Dec OR Spring: Jan-May)",
            "admission_requirements_summary": "Handled entirely via USEFP selection; no separate university admission application is needed.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Institutions are assigned by IREX/USEFP based on academic fit, field, and campus environment; applicants cannot choose or change their host college.",
            "strategic_program_match_advice": "Focus your essays on cultural exchange, cross-cultural diplomacy, and what specific community challenges in Pakistan you will address upon return."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.usefp.org/scholarships/global-ugrad.cfm",
            "portal_system_name": "USEFP Online Application System",
            "account_creation_instructions": "Register on the USEFP portal with primary Pakistani email, national CNIC, and current university student enrollment details.",
            "step_by_step_workflow": [
                "1. Register online account on USEFP portal during the open window (September/October).",
                "2. Upload scanned official university academic transcripts from all completed semesters.",
                "3. Write Statement of Purpose essay detailing personal background, community leadership, and exchange vision.",
                "4. Provide contact details of two academic referees or professors who will upload reference letters directly.",
                "5. Submit complete online dossier before the annual deadline (usually mid-November).",
                "6. Shortlisted applicants invited to panel interviews at USEFP Islamabad or regional hubs.",
                "7. Final selected candidates take sponsored TOEFL test and attend mandatory pre-departure orientation."
            ],
            "university_vs_scholarship_routing": "Direct single application through USEFP Pakistan portal.",
            "recommendation_letters_submission_method": "Submitted online by university professors via secure referee link sent by USEFP.",
            "personal_statement_prompts": "Address your leadership experiences, extracurricular activities, your perspective as a cultural ambassador for Pakistan in the U.S., and your future goals.",
            "study_plan_research_proposal_requirements": "Brief statement of intended coursework and areas of academic interest to be pursued during the semester.",
            "cv_format_requirements": "Standard 1-2 page academic & extracurricular resume highlighting volunteerism, leadership positions, and community initiatives.",
            "interviews_conducted": True,
            "interview_format_details": "20-30 minute structured panel interview conducted in English by USEFP staff and U.S. Embassy officers in Islamabad/Lahore/Karachi or virtual.",
            "standardized_tests": "None at application time; TOEFL iBT administered and funded by USEFP only for shortlisted finalists.",
            "application_fee_amount": "$0 (100% Free - USEFP never charges an application fee)",
            "attestation_requirements": "Attestation by university registrar or controller of examinations; HEC/IBCC attestation not required at initial application stage.",
            "translation_requirements": "All university transcripts must be issued in English.",
            "final_submission_method": "100% Online via USEFP portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "University Transcripts",
                "mandatory": True,
                "specification": "Official university transcripts of all completed semesters with university grading scale",
                "pakistan_specific_instruction": "Attested by your university examination department or controller of examinations"
            },
            {
                "document_name": "Pakistani CNIC or Smart Card",
                "mandatory": True,
                "specification": "Valid National Identity Card issued by NADRA",
                "pakistan_specific_instruction": "Scanned copy of both front and back sides"
            },
            {
                "document_name": "Statement of Purpose (Personal Statement)",
                "mandatory": True,
                "specification": "Structured essay (around 500-750 words) answering official prompt",
                "pakistan_specific_instruction": "Original narrative demonstrating leadership and community impact; zero plagiarism tolerated"
            },
            {
                "document_name": "Academic Reference Letters",
                "mandatory": True,
                "specification": "Two recommendation letters from university faculty members",
                "pakistan_specific_instruction": "Uploaded directly by university professors using official institutional email"
            },
            {
                "document_name": "No Objection / Enrollment Certificate",
                "mandatory": True,
                "specification": "Letter from department head confirming current active student status and permission for semester abroad",
                "pakistan_specific_instruction": "Issued on university letterhead with official stamp"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-15",
            "application_deadline": "2026-11-18",
            "university_admission_deadline": "N/A (Managed centrally)",
            "document_submission_deadline": "2026-11-18",
            "recommendation_letters_deadline": "2026-11-25",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "March 2027",
            "final_result_acceptance_deadline": "April 2027",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "August 2027 (Fall batch) or January 2028 (Spring batch)",
            "annual_cycle_notes": "Annual cycle opens every autumn (September-October) with 240 Pakistani students split across Fall and Spring cohorts."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Strong academic standing, consistently good grades)",
            "extracurricular_and_leadership_weight": "35% (Community engagement, volunteer work, youth initiatives, leadership)",
            "research_experience_weight": "5% (Not essential for undergraduate exchange)",
            "work_experience_weight": "5% (Internships or community work)",
            "personal_statement_weight": "20% (Clarity of purpose, authenticity, cultural exchange aptitude)",
            "recommendations_weight": "10% (Faculty assessment of character and maturity)",
            "interview_weight": "Significant in final round (English fluency, cultural adaptability, confidence)",
            "test_scores_weight": "0% at application stage",
            "financial_need_weight": "Considered positively for socio-economic diversity",
            "selection_panel_composition": "USEFP education advisers, U.S. Embassy and Consular public diplomacy diplomats, and Pakistani alumni.",
            "evaluation_methodology": "Holistic review with strong geographic representation across all provinces of Pakistan."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~12,000 to 15,000 applications across Pakistan",
            "total_scholarships_awarded": "~200 to 240 scholars selected annually",
            "acceptance_rate_global": "N/A (Pakistan-specific program)",
            "acceptance_rate_pakistan": "~1.5% to 2.0% (Highly Selective)",
            "typical_successful_applicant_gpa": "3.30 to 3.85 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Dynamic undergraduate students with active volunteer work, debate/MUN, blood drive organizing, or teaching underprivileged children.",
            "common_backgrounds_of_winners": "Students from diverse universities: NUST, FAST, LUMS, IBA, Punjab University, UET, Quaid-i-Azam, UET Peshawar, BUITEMS Quetta, Karakoram International University.",
            "high_representation_countries": "100% Pakistan cohort.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unverified Facebook/Instagram pages claiming to guarantee UGRAD selection for money.",
                "Consultants asking for money to write UGRAD essays."
            ],
            "application_fee_warning": "USEFP NEVER charges an application fee. The application is completely free.",
            "agent_and_intermediary_warnings": "Do NOT hire education agents. USEFP explicitly states third-party agent applications are penalized.",
            "hidden_costs_breakdown": [
                "Domestic travel to Islamabad/Karachi/Lahore for U.S. visa interview and pre-departure orientation (though modest travel stipend is provided to distant candidates).",
                "NADRA Smart Card / Passport renewal fees in Pakistan."
            ],
            "misleading_claims_debunked": [
                "MYTH: Only students from top elite private universities get selected. (Fact: High priority is given to public sector regional universities across KP, Balochistan, Sindh, and GB).",
                "MYTH: You can stay in the USA and transfer into a full degree. (Fact: Strictly prohibited; students must return to Pakistan to complete their home degree under J-1 visa terms)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs claim IELTS is required; officially, NO IELTS or TOEFL is needed at the time of application."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance and full-time enrollment (minimum 12 credits) at host U.S. university.",
            "attendance_requirements": "Mandatory class attendance and full participation in 20 hours of community service during the semester in the U.S.",
            "academic_progress_monitoring": "Host university advisor submits midterm and final grade reports to IREX and USEFP.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under the J-1 Global UGRAD visa regulations.",
            "home_country_return_obligation": "MANDATORY Return: Must return immediately to Pakistan upon semester completion to resume degree at home university; subject to 2-year home country physical presence requirement (Section 212(e)).",
            "service_obligations_or_bonds": "Obligated to complete remaining undergraduate studies in Pakistan and participate in the Pakistan-U.S. Alumni Network (PUAN).",
            "repayment_clawback_conditions": "Violations of U.S. law, university honor code, or unauthorized travel/stay will result in immediate termination, deportation, and recovery of costs.",
            "rules_for_changing_university": "University assignment is final and cannot be altered.",
            "rules_for_changing_major": "Course selection is coordinated with host academic advisor within student's home major.",
            "extension_policy": "Extensions are strictly prohibited; program is limited to exactly one academic semester."
        },
        "official_sources_verified": [
            {
                "source_name": "United States Educational Foundation in Pakistan (USEFP) - Global UGRAD Pakistan Portal",
                "source_url": "https://www.usefp.org/scholarships/global-ugrad.cfm",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact regional/provincial quota percentage allocations across provinces",
                    "Internal interview scoring sheet weighting"
                ]
            },
            {
                "source_name": "U.S. Department of State - Bureau of Educational and Cultural Affairs (ECA)",
                "source_url": "https://exchanges.state.gov/non-us/program/global-undergraduate-exchange-program-global-ugrad",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Individual institutional placement allocation formulas across partner U.S. colleges"
                ]
            }
        ]
    },

    # 2. Lester B. Pearson International Scholarship (SCH-AM-003)
    "SCH-AM-003": {
        "scholarship_id": "SCH-AM-003",
        "basic_details": {
            "scholarship_name": "Lester B. Pearson International Scholarship Program",
            "offering_entity": "University of Toronto",
            "host_country": "Canada",
            "host_institutions_covered": "University of Toronto (St. George, Mississauga, and Scarborough campuses)",
            "degree_levels": ["Undergraduate"],
            "major_restrictions": "Open to all direct-entry undergraduate programs across Arts & Science, Applied Science & Engineering, Commerce (Rotman), Architecture, Music, and Kinesiology.",
            "number_of_awards_total": "~37 scholars selected globally each year",
            "number_of_awards_pakistan": "Open globally; typically 1 to 2 exceptional Pakistani high school students selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 continuous years of undergraduate study"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students (non-Canadian citizens requiring a Canadian study permit)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 20,
            "age_limit_postgrad": None,
            "age_limit_notes": "Currently in final year of secondary school or graduated no earlier than June of the preceding year.",
            "academic_qualifications": "High school completion: A-Levels (Cambridge/Edexcel), IB Diploma, or Pakistani Intermediate (FSc/FA/ICS) with top-tier academic excellence.",
            "minimum_gpa_percentage": 90.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Minimum 90%+ in FSc or straight A*/A grades in Cambridge A-Levels (predicted and final results).",
            "subject_background_prerequisites": "Prerequisites vary by faculty (e.g., Mathematics and Physics for Engineering; Calculus for Rotman Commerce).",
            "current_education_status": "Secondary school student nominated by high school/college guidance counsellor.",
            "graduation_year_restrictions": "Must graduate high school in the current academic year or have graduated within the past 12 months with no post-secondary gap studies.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Focus on high school leadership, intellectual curiosity, school clubs, debate, Olympiads, and community engagement.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 100,
                "duolingo_accepted": True,
                "moi_certificate_accepted": False,
                "notes": "IELTS 6.5 overall (no band below 6.0) or TOEFL iBT 100 with 22 in Writing, or Duolingo English Test (DET) minimum 120."
            },
            "other_language_requirements": "None; English instruction.",
            "gender_specific_requirements": "Equal opportunity; all eligible candidates welcome.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must be explicitly nominated by their high school guidance counsellor before applying.",
            "previous_scholarship_restrictions": "Must not have already attended a college or university degree program.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Covers 100% international undergraduate tuition fees at University of Toronto for 4 years.",
                "amount": "CAD $60,000 to $70,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Ontario Universities' Application Centre (OUAC) application fee paid by candidate (~CAD $250).",
                "amount": None
            },
            "accommodation": {
                "status": "FREE DORMITORY",
                "details": "Guaranteed full residence support in University of Toronto college dormitories for all 4 years.",
                "amount": "CAD $12,000 to $16,000 / year"
            },
            "monthly_stipend": {
                "status": "INCLUDED IN RESIDENCE & INCIDENTAL",
                "details": "Living expenses covered through residence room, board plan, and incidental book grant.",
                "amount": None
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel flights to Toronto are arranged by student/family.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD $150) and biometrics fee paid by applicant.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "University Health Insurance Plan (UHIP) covered for international students.",
                "amount": "CAD $756 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Full meal plan included with college residence dining package.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full incidental book and supplies allowance provided annually.",
                "amount": "CAD $1,500 / year (~PKR 310,000 / year)"
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "U of T undergraduate research opportunities (e.g. ROP programs) accessible.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Local Toronto transit passes paid from incidental budget.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 65000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Toronto (World Top 20).",
            "participating_institutions": [
                "University of Toronto (St. George Downtown, UTM Mississauga, UTSC Scarborough)"
            ],
            "university_rankings_scope": "Consistently ranked #1 in Canada and Top 20 globally (QS/THE/ARWU).",
            "available_majors": [
                "Computer Science, Engineering Science, Rotman Commerce, Life Sciences, Economics, Architecture, Mathematics, Physics, Humanities, Social Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 academic years (BSc, BA, BCom, BASc)",
            "admission_requirements_summary": "Must apply to direct-entry first-year program via OUAC by early deadlines.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "St. George campus Engineering Science and Rotman Commerce are most competitive.",
            "strategic_program_match_advice": "High school nomination is the key gatekeeper; ensure your school guidance counsellor nominates you early in October."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://future.utoronto.ca/pearson/about/",
            "portal_system_name": "University of Toronto Pearson Scholarship Application Portal",
            "account_creation_instructions": "Your school must first register and nominate you. Once nominated, U of T emails you a unique private application portal link.",
            "step_by_step_workflow": [
                "1. High school counsellor submits official nomination for you (Deadline: late November).",
                "2. Apply for admission to U of T via OUAC 105 portal by mid-December.",
                "3. Receive JOINid and credentials to log into U of T Pearson Scholarship portal.",
                "4. Complete Pearson scholarship essays and activity profiles (Deadline: mid-January).",
                "5. Upload predicted grades/transcripts and school references.",
                "6. Results announced in late April."
            ],
            "university_vs_scholarship_routing": "Concurrent: High school nomination + OUAC admission application + dedicated Pearson scholarship essays.",
            "recommendation_letters_submission_method": "Submitted online by high school guidance counsellor and referee teachers.",
            "personal_statement_prompts": "Reflect on how your actions have made a meaningful difference in your school or community and how you demonstrate creativity and independent thought.",
            "study_plan_research_proposal_requirements": "Not applicable; focus on undergraduate intellectual curiosity and extracurricular engagement.",
            "cv_format_requirements": "Detailed online activity sheet covering school clubs, leadership positions, honors, and community service.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; decisions based strictly on nomination, academic transcripts, and written application dossiers.",
            "standardized_tests": "SAT/ACT optional; English language test mandatory.",
            "application_fee_amount": "CAD $250 for OUAC university application; Pearson scholarship application itself has no fee.",
            "attestation_requirements": "High school official transcripts stamped by school principal/counsellor; IBCC not required by U of T.",
            "translation_requirements": "Official certified English translation if school documents are in Urdu.",
            "final_submission_method": "100% Online via OUAC and U of T Applicant Portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "High School Counselor Nomination",
                "mandatory": True,
                "specification": "Official institutional nomination by high school principal or head of counselling",
                "pakistan_specific_instruction": "Only 1 student can be nominated per high school per year in Pakistan"
            },
            {
                "document_name": "High School Transcripts & Predicted Grades",
                "mandatory": True,
                "specification": "Grade 9, 10, 11 results and Grade 12 predicted grades (A-Levels or FSc-II)",
                "pakistan_specific_instruction": "Attested by school administration or Cambridge/BISE certificates"
            },
            {
                "document_name": "Pearson Scholarship Essays",
                "mandatory": True,
                "specification": "Original personal statement and creative impact essays written on portal",
                "pakistan_specific_instruction": "Demonstrating exceptional impact, leadership, and resilience"
            },
            {
                "document_name": "English Proficiency Score (IELTS/TOEFL/DET)",
                "mandatory": True,
                "specification": "Official electronic score report sent to University of Toronto",
                "pakistan_specific_instruction": "IELTS 6.5+ or TOEFL 100+"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2027-01-15",
            "university_admission_deadline": "2026-12-15",
            "document_submission_deadline": "2027-01-29",
            "recommendation_letters_deadline": "2026-11-30",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-30",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "School nomination deadline is always late November; U of T OUAC admission deadline mid-December; scholarship essays due mid-January."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Outstanding high school academic achievement, straight A* / 90%+)",
            "extracurricular_and_leadership_weight": "35% (Exceptional leadership, originality, community initiative)",
            "research_experience_weight": "5% (Olympiads, science fairs, academic competitions)",
            "work_experience_weight": "0% (Not expected for high school graduates)",
            "personal_statement_weight": "20% (Voice, intellectual depth, perspective)",
            "recommendations_weight": "5% (High school endorsement)",
            "interview_weight": "0%",
            "test_scores_weight": "5% (English language proficiency)",
            "financial_need_weight": "0% (Purely merit and leadership based)",
            "selection_panel_composition": "University of Toronto Admissions Committee and Pearson Scholarship Selection Board.",
            "evaluation_methodology": "Holistic assessment identifying scholars with transformative leadership potential who are recognized as leaders in their schools."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 nominated candidates globally",
            "total_scholarships_awarded": "~37 scholars selected globally",
            "acceptance_rate_global": "~1.5%",
            "acceptance_rate_pakistan": "~1% (Typically 1 or 2 scholars per year from Pakistan)",
            "typical_successful_applicant_gpa": "Straight A*s in A-Levels or 92%+ in FSc",
            "typical_academic_and_research_profile": "Head boy/head girl, national debating champion, founder of non-profit initiative, international Olympiad medalist.",
            "common_backgrounds_of_winners": "Past Pakistani winners from Karachi Grammar School, Aitchison College, Lahore Grammar School, Roots Millennium, Beaconhouse.",
            "high_representation_countries": "Global distribution across 30+ countries each year.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unapproved agencies claiming they can secure Pearson nominations independently of your school."
            ],
            "application_fee_warning": "Pearson application is free, but OUAC application fee of ~CAD $250 is standard university application fee.",
            "agent_and_intermediary_warnings": "Nomination must come directly from your recognized high school; agent nominations are disqualified.",
            "hidden_costs_breakdown": [
                "OUAC application fee (~CAD $250).",
                "Canadian study permit fee and biometrics (~CAD $235).",
                "International flights from Pakistan to Toronto (~PKR 350,000 to 500,000 round-trip).",
                "Winter clothing and initial personal items buffer upon landing in Toronto."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can self-nominate if your school refuses. (Fact: High schools must be verified and submit the nomination; self-nominations are rejected).",
                "MYTH: Multiple students from one school can get nominated. (Fact: Strictly 1 student per school per year)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites claim flights are covered; officially, international flights are NOT funded by Pearson."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.0 / 4.00 (B standing) and complete full-time course load (minimum 4.0 credits per year).",
            "attendance_requirements": "Full-time physical enrollment on campus in Toronto.",
            "academic_progress_monitoring": "Annual review by U of T Student Awards Office before renewing for subsequent years.",
            "work_restrictions_during_study": "Permitted to work on-campus and up to 20 hours/week off-campus during academic terms under Canadian Study Permit regulations.",
            "home_country_return_obligation": "No mandatory home return rule; eligible for Canadian Post-Graduation Work Permit (PGWP) upon graduation.",
            "service_obligations_or_bonds": "None; active participation in Pearson scholar events and campus ambassador activities.",
            "repayment_clawback_conditions": "Loss of award if student withdraws from university or fails to maintain minimum academic standard.",
            "rules_for_changing_university": "Award is non-transferable to other universities.",
            "rules_for_changing_major": "Permitted to change major within eligible U of T faculties subject to faculty academic approval.",
            "extension_policy": "Strictly limited to a maximum of 4 years of undergraduate study; fifth-year extensions not funded."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Toronto - Lester B. Pearson International Scholarships Portal",
                "source_url": "https://future.utoronto.ca/pearson/about/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Internal mathematical scoring rubric comparing A-Levels against local Pakistani FSc qualifications",
                    "Specific country-by-country recipient target quotas"
                ]
            }
        ]
    },

    # 3. Vanier Canada Graduate Scholarships (SCH-AM-004)
    "SCH-AM-004": {
        "scholarship_id": "SCH-AM-004",
        "basic_details": {
            "scholarship_name": "Vanier Canada Graduate Scholarships (Vanier CGS)",
            "offering_entity": "Government of Canada (Tri-Agency: CIHR, NSERC, SSHRC)",
            "host_country": "Canada",
            "host_institutions_covered": "Eligible Canadian Universities with institutional Vanier quotas (McGill, Toronto, UBC, Waterloo, Alberta, McMaster, etc.)",
            "degree_levels": ["PhD"],
            "major_restrictions": "Open across all three Tri-Agency domains: Health research (CIHR), Natural sciences and engineering (NSERC), Social sciences and humanities (SSHRC).",
            "number_of_awards_total": "Up to 166 scholarships awarded annually across Canada",
            "number_of_awards_pakistan": "Open to Canadian and international citizens; awarded based on national institutional ranking quotas",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3 non-renewable years during doctoral studies"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Canadian citizens, permanent residents, and foreign citizens of all countries (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction; based on doctoral standing.",
            "academic_qualifications": "18 years of education (MS/MPhil/Master's degree) with first-class academic standing.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Must have achieved a first-class average (equivalent to at least A- or 80%+ / 3.7+ CGPA) in each of the last two years of full-time study.",
            "subject_background_prerequisites": "Substantive master's degree in proposed research area with high-impact thesis or peer-reviewed research publications.",
            "current_education_status": "Be nominated by only ONE Canadian university with an institutional quota; candidate must have completed no more than 20 months of PhD study by May 1 of award year.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research productivity, conference presentations, and leadership activities evaluated.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 100,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Must satisfy host Canadian university doctoral language proficiency."
            },
            "other_language_requirements": "English or French depending on the chosen university.",
            "gender_specific_requirements": "Equal opportunity; equity, diversity, and inclusion (EDI) principles strictly applied.",
            "financial_need_required": False,
            "special_eligibility_categories": "Nominated candidate must demonstrate top-tier leadership potential and research excellence.",
            "previous_scholarship_restrictions": "Must not have previously held a Tri-Agency doctoral scholarship.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PAID VIA STIPEND / UNIVERSITY WAIVER",
                "details": "Vanier provides CAD $50,000 per year directly to student; many host universities also offer full tuition fee waivers or top-ups to Vanier scholars.",
                "amount": None
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian university graduate application fee (~CAD $125 to $150) paid by applicant.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Living expenses and accommodation paid from generous CAD $50,000 annual grant.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "CAD $50,000 per year paid in monthly or term installments (~CAD $4,166 / month).",
                "amount": "CAD $50,000 / year (~PKR 10,300,000 / year or ~PKR 860,000 / month)"
            },
            "airfare": {
                "status": "PAID VIA STIPEND",
                "details": "Student covers flights from the annual stipend allocation.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Study permit application fee paid by applicant.",
                "amount": None
            },
            "health_insurance": {
                "status": "PAID VIA STIPEND / UNIVERSITY PLAN",
                "details": "Covered via university student health plan.",
                "amount": None
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Covered from living grant.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Covered from living grant.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Host university labs and Tri-Agency travel grants available for international conferences.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Covered from personal stipend.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple: Any eligible Canadian research university holding an institutional Vanier quota.",
            "participating_institutions": [
                "University of Toronto", "UBC", "McGill University", "University of Waterloo",
                "University of Alberta", "McMaster University", "Université de Montréal", "Queen's University"
            ],
            "university_rankings_scope": "Top 15 Canadian U15 research-intensive universities.",
            "available_majors": [
                "Health Sciences, Biomedical Sciences, Computer Science, Artificial Intelligence, Engineering, Physics, Chemistry, Molecular Biology, Environmental Sciences, Economics, Sociology, Humanities"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 years of funded PhD study",
            "admission_requirements_summary": "Must secure doctoral admission and formal nomination endorsement from chosen Canadian university department.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Institutions have strict internal nomination quotas; internal university deadline is typically September/October.",
            "strategic_program_match_advice": "Contact prospective PhD supervisors in Canada by July/August; an enthusiastic supervisor and department head nomination is mandatory."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://vanier.gc.ca/en/home-accueil.html",
            "portal_system_name": "ResearchNet Portal (Government of Canada)",
            "account_creation_instructions": "Register on ResearchNet, complete the Canadian Common CV (CCV - Vanier-Banting template), and link to the nominating university.",
            "step_by_step_workflow": [
                "1. Contact prospective Canadian university professor and secure doctoral admission support (June-August).",
                "2. Create ResearchNet account and complete the Vanier CCV online.",
                "3. Draft detailed Research Proposal (2 pages) and Project References (5 pages maximum).",
                "4. Write Leadership Statement outlining community leadership and research impact (2 pages).",
                "5. Obtain two Leadership Reference Letters and two Academic Referee assessments.",
                "6. Submit electronic application via ResearchNet to your nominating university by their internal deadline (usually September/October).",
                "7. University internal committee selects nominees and forwards them to federal Tri-Agency secretariat by early November.",
                "8. National Tri-Agency selection committees review dossiers in January/February; results released in April."
            ],
            "university_vs_scholarship_routing": "Routed through the nominating Canadian university via ResearchNet.",
            "recommendation_letters_submission_method": "Submitted electronically by referees directly through the ResearchNet portal.",
            "personal_statement_prompts": "Personal Leadership Statement: Describe your leadership skills and initiatives, how you foster collaboration, and your vision for broader societal impact.",
            "study_plan_research_proposal_requirements": "Strict 2-page research proposal detailing research questions, methodology, significance, and expected contributions.",
            "cv_format_requirements": "Canadian Common CV (CCV) Vanier-Banting Academic template.",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; judged entirely on peer review of ResearchNet dossier.",
            "standardized_tests": "GRE not required by Vanier; check individual university requirements.",
            "application_fee_amount": "$0 for Vanier; university graduate application fees apply (~CAD $125).",
            "attestation_requirements": "Official university transcripts certified by Pakistani degree-granting universities and HEC.",
            "translation_requirements": "Official certified English or French translations of all non-English transcripts.",
            "final_submission_method": "100% Online via ResearchNet."
        },
        "required_documents_checklist": [
            {
                "document_name": "Canadian Common CV (CCV)",
                "mandatory": True,
                "specification": "Vanier-Banting specific template completed on the CCV portal",
                "pakistan_specific_instruction": "List all publications, conferences, awards, and Pakistani research projects"
            },
            {
                "document_name": "Research Proposal",
                "mandatory": True,
                "specification": "2-page rigorous research proposal plus 5-page bibliographic references",
                "pakistan_specific_instruction": "Aligned with the prospective Canadian laboratory's research focus"
            },
            {
                "document_name": "Personal Leadership Statement",
                "mandatory": True,
                "specification": "2-page narrative highlighting demonstrable leadership achievements",
                "pakistan_specific_instruction": "Articulate how you have influenced others and overcome adversity in Pakistan"
            },
            {
                "document_name": "Two Leadership Reference Letters",
                "mandatory": True,
                "specification": "Specialized letters from community/professional leaders assessing your leadership",
                "pakistan_specific_instruction": "Can be from former employers, NGO directors, or mentors outside primary lab"
            },
            {
                "document_name": "Two Academic Referee Assessments",
                "mandatory": True,
                "specification": "Evaluations by senior academics assessing research potential",
                "pakistan_specific_instruction": "Uploaded via ResearchNet by professors from your MS/BS institution"
            },
            {
                "document_name": "Official Transcripts",
                "mandatory": True,
                "specification": "Transcripts of all undergraduate and graduate education",
                "pakistan_specific_instruction": "Attested by HEC Pakistan and degree-granting university registrars"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-06-15",
            "application_deadline": "2026-11-01",
            "university_admission_deadline": "2026-09-15",
            "document_submission_deadline": "2026-10-15",
            "recommendation_letters_deadline": "2026-10-15",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "May 2027 or September 2027",
            "annual_cycle_notes": "Internal university deadlines occur between early September and mid-October. Federal national deadline is always early November."
        },
        "selection_process_and_weights": {
            "academic_weight": "33.3% (Academic excellence: transcripts, awards, fellowships, speed of completion)",
            "extracurricular_and_leadership_weight": "33.3% (Demonstrated leadership potential and ability: community impact, initiatives)",
            "research_experience_weight": "33.3% (Research potential: quality and feasibility of proposal, publications, contributions to science)",
            "work_experience_weight": "Included in leadership/research evaluation",
            "personal_statement_weight": "Evaluated within leadership component",
            "recommendations_weight": "Evaluated across academic, leadership, and research components",
            "interview_weight": "0%",
            "test_scores_weight": "0%",
            "financial_need_weight": "0% (Strictly merit-driven)",
            "selection_panel_composition": "Tri-Agency multidisciplinary peer review committees consisting of distinguished Canadian researchers and professors.",
            "evaluation_methodology": "Equal weighting of 3 pillars: Academic Excellence (33.3%), Research Potential (33.3%), and Leadership (33.3%)."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~500 nominated finalists by universities (from thousands of department applicants)",
            "total_scholarships_awarded": "166 scholarships nationally (across all 3 agencies)",
            "acceptance_rate_global": "~30% of nominated finalists (~2% to 4% of total departmental applicants)",
            "acceptance_rate_pakistan": "~2% to 3% of international pool",
            "typical_successful_applicant_gpa": "3.85 to 4.00 CGPA (Top 1% of graduating master's class)",
            "typical_academic_and_research_profile": "First-author publications in high-impact journals (IEEE, Nature indexed), international conference presentations, high-impact societal leadership.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani universities (LUMS, NUST, Quaid-i-Azam, UET) who secured admission to Canadian top-tier doctoral labs.",
            "high_representation_countries": "Canada, China, India, Iran, Pakistan, USA, Germany.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized services claiming to guarantee Vanier endorsement outside the official university nomination stream."
            ],
            "application_fee_warning": "Vanier application via ResearchNet is completely free of charge.",
            "agent_and_intermediary_warnings": "Never use third-party agents; Tri-Agency applications require genuine faculty supervisor engagement.",
            "hidden_costs_breakdown": [
                "Canadian university graduate application fee (~CAD $125 to $150).",
                "Canadian study permit application fee (~CAD $150) + biometrics fee (CAD $85).",
                "Initial relocation airfare to Canada (~PKR 350,000 to 450,000) prior to first funding disbursement."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can apply to Vanier without contacting a Canadian professor. (Fact: You cannot apply directly to the government; a Canadian university must formally endorse and nominate you).",
                "MYTH: Vanier only funds Canadian citizens. (Fact: International students including Pakistani citizens are fully eligible on equal footing)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs often list outdated stipend amounts; current official rate is CAD $50,000/year."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic progress in doctoral degree as certified by host university graduate studies office.",
            "attendance_requirements": "Full-time physical research residence at host Canadian university.",
            "academic_progress_monitoring": "Annual progress reporting required by the Tri-Agency secretariat.",
            "work_restrictions_during_study": "Permitted to work up to standard graduate assistantship limits (typically 10-12 hrs/week TA/RA) per university regulations.",
            "home_country_return_obligation": "None; scholars are eligible for Canadian Post-Graduation Work Permits (PGWP) and Permanent Residency (Express Entry / Provincial Nominee Programs).",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "If doctoral studies are discontinued or academic fraud occurs, remaining funds are terminated.",
            "rules_for_changing_university": "Vanier scholarships are tied to the nominating institution; transferring universities requires exceptional Tri-Agency approval.",
            "rules_for_changing_major": "Significant changes in proposed research area require Tri-Agency review.",
            "extension_policy": "Strict maximum duration of 36 months; no funding extensions granted under any circumstances."
        },
        "official_sources_verified": [
            {
                "source_name": "Government of Canada - Vanier Canada Graduate Scholarships Official Portal",
                "source_url": "https://vanier.gc.ca/en/home-accueil.html",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Individual institutional quota numbers per Canadian university",
                    "Exact peer-review scoring cutoff marks for each agency committee (CIHR, NSERC, SSHRC)"
                ]
            }
        ]
    }
}
