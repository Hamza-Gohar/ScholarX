# scripts/batch17_p1.py
# SCH-ME-015: Taibah University International Student Scholarship (Saudi Arabia)
# SCH-ME-016: King Faisal University International Student Scholarship (Saudi Arabia)
# SCH-ME-017: Jazan University International Student Scholarship (Saudi Arabia)
# SCH-ME-028: New York University Abu Dhabi (NYUAD) Global Leaders Fellowship (UAE)

DATA_P1 = {
    "SCH-ME-015": {
        "scholarship_id": "SCH-ME-015",
        "basic_details": {
            "scholarship_name": "Taibah University International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & Taibah University",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "Taibah University Main Campus (Medina Al-Munawwarah, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to Islamic Studies, Arabic Language and Literature, Computer Science, Information Systems, Electrical Engineering, Mechanical Engineering, Chemistry, Physics, Mathematics, and Business Administration (Health/Medical clinical colleges reserved for Saudi nationals under national policy).",
            "number_of_awards_total": "~250 to 350 external international government scholarships allocated annually across all faculties",
            "number_of_awards_pakistan": "Generous bilateral quota; Pakistani students constitute one of the most prominent international student communities in Medina (~35 to 55 scholarships annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 to 3 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic language preparatory institute if required)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Saudi citizenship (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate applicants must be between 17 and 25 years old; Master's applicants under 30; PhD applicants under 35 years of age.",
            "academic_qualifications": "HSSC / Intermediate (Pre-Engineering, Pre-Medical, or ICS) or A-Levels for Bachelor's (minimum 80% marks or Grade B); recognized 16-year Bachelor's degree for Master's; 18-year Master's degree for PhD from an HEC-recognized institution with a minimum CGPA of 3.00 / 4.00 or Very Good (Jayyid Jiddan) standing.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Transcript grades evaluated on Saudi 5.0 scale (minimum 3.75 / 5.00 equivalent).",
            "subject_background_prerequisites": "Pre-Engineering or ICS for Computer Science and Engineering; Pre-Medical or General Science for Natural Sciences.",
            "current_education_status": "Applicants must have completed their requisite qualification and possess official final transcripts/certificates at the time of portal registration.",
            "graduation_year_restrictions": "High school diploma must not be older than 3 to 5 years from the date of application.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; research publications or teaching assistantships beneficial for postgraduate candidates.",
            "english_test_required": False,
            "ielts_minimum": 5.5,
            "toefl_minimum": 65,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Instruction in STEM faculties is primarily in English (MOI certificate accepted; IELTS 5.5+ or TOEFL 65 recommended). For Sharia and Arabic faculties, candidates must demonstrate Arabic competence or complete the university's intensive 1-year Arabic Institute.",
            "other_language_requirements": "Arabic Institute placement exam conducted upon campus arrival for non-Arabic speakers.",
            "gender_specific_requirements": "Female students must reside with an approved Mahram residing legally in Saudi Arabia or within monitored university female student dormitories with institutional guardianship approval.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applications are submitted through the unified Saudi government portal 'Study in Saudi' (studyinsaudi.moe.gov.sa).",
            "previous_scholarship_restrictions": "Applicant must not have been previously awarded a Saudi government scholarship and dismissed or graduated from another Saudi university.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee exemption for the entire official duration of academic study.",
                "amount": "100% covered (~SAR 25,000 to 40,000 / year value; ~PKR 1,875,000 to 3,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application through the official 'Study in Saudi' portal is completely free of charge.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free furnished on-campus student housing in Taibah University residential dormitories in Medina, including utilities, high-speed Wi-Fi, air conditioning, and laundry facilities.",
                "amount": "100% covered free dormitory room"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Tax-free monthly living stipend disbursed directly into student bank accounts: SAR 840 / month for undergraduate students (~USD 224; ~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~USD 240 to 266; ~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Free annual economy-class round-trip flight ticket between Pakistan and Prince Mohammad bin Abdulaziz International Airport (Medina) provided by the university at the end of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Saudi governmental study visa issued free of charge through the Royal Embassy of Saudi Arabia in Islamabad or Royal Consulate in Karachi.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive 100% free medical and dental healthcare provided at Taibah University Medical Center and King Fahd Hospital Medina.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Heavily subsidized campus dining halls provide balanced multi-course meals for SAR 3 to 6 per meal; easily covered by the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Free textbook issuance and full borrowing privileges at the Central University Library; initial book allowance provided upon enrollment.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Thesis printing allowance (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial incentives for publishing in Web of Science / Scopus Q1 journals.",
                "amount": "SAR 3,000 to 4,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Free university shuttle bus service operating daily between dormitories, university faculties, and the Prophet's Mosque (Al-Masjid an-Nabawi).",
                "amount": "100% free university shuttle transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Taibah University, Medina)",
            "participating_institutions": [
                "Taibah University Main Campus (Medina Al-Munawwarah, Kingdom of Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #61-70, Times Higher Education Asia #201-250, accredited by the National Center for Academic Accreditation and Assessment (NCAAA).",
            "available_majors": [
                "Computer Science",
                "Information Systems",
                "Computer Engineering",
                "Electrical Engineering",
                "Mechanical Engineering",
                "Chemistry and Applied Chemistry",
                "Physics",
                "Mathematics",
                "Islamic Studies (Fiqh, Usul, Hadith)",
                "Arabic Language and Literature",
                "Business Administration and Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Unified online application via 'Study in Saudi' platform, high school / bachelor's diploma with minimum 80% marks, attested transcripts, medical fitness certificate, clean police conduct certificate, two academic recommendation letters, and valid passport copy.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Islamic Studies and Computer Science receive intense global demand due to Medina's religious significance; high academic grades (85%+) and solid recommendations are essential for admission.",
            "strategic_program_match_advice": "Ensure all Pakistani educational certificates are fully attested by IBCC/HEC and the Ministry of Foreign Affairs (MoFA) before submitting to avoid portal disqualification."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.taibahu.edu.sa/",
            "portal_system_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
            "account_creation_instructions": "Register an account on 'Study in Saudi' portal, choose 'External Scholarship (منحة خارجية)', select Taibah University as the preferred institution, select degree level, and upload attested digital scans.",
            "step_by_step_workflow": [
                "Step 1: Check application announcement on the 'Study in Saudi' portal (typically opens September/October).",
                "Step 2: Create profile, fill in personal details, and enter academic percentages and grading scales.",
                "Step 3: Upload color scans of passport, educational degrees, transcripts, medical fitness certificate, and police clearance.",
                "Step 4: Select Taibah University and choose top 3 preferred academic disciplines.",
                "Step 5: Submit application online (no application fee required) and note the tracking number.",
                "Step 6: Taibah University Admissions Committee screens applications and nominates candidates to the Saudi Ministry of Education (December - March).",
                "Step 7: Final security clearance and Ministry approval granted (May - July).",
                "Step 8: Official admission letter and Saudi visa authorization number issued via the portal.",
                "Step 9: Complete Saudi Student Visa stamping at Gerry's / Etimad visa center in Islamabad/Karachi, receive free flight ticket, and arrive in Medina in September."
            ],
            "university_vs_scholarship_routing": "Unified Platform Track: Application through 'Study in Saudi' automatically includes admission and full government scholarship.",
            "recommendation_letters_submission_method": "Uploaded as scanned PDF documents signed by teachers/professors on official school/university letterhead.",
            "personal_statement_prompts": "Statement of purpose outlining academic achievements, reasons for choosing Taibah University and the city of Medina, and post-graduation goals.",
            "study_plan_research_proposal_requirements": "For Master's/PhD applicants: 3 to 5-page research proposal detailing proposed topic, methodology, and relevance.",
            "cv_format_requirements": "Standard curriculum vitae detailing educational history, academic honors, and community service.",
            "interviews_conducted": False,
            "interview_format_details": "Generally no oral interview; selection is determined entirely on academic document review and Ministry security vetting.",
            "standardized_tests": "None strictly required; GAT/Qudurat not required for international external applicants.",
            "application_fee_amount": "SAR 0 (100% Free)",
            "attestation_requirements": "Degrees and transcripts must be attested by IBCC (for Intermediate) or HEC (for degrees), MoFA Pakistan, and the Saudi Cultural Mission / Royal Embassy of Saudi Arabia in Islamabad.",
            "translation_requirements": "Certified Arabic or English translation required for documents not issued in English or Arabic.",
            "final_submission_method": "100% digital submission through studyinsaudi.moe.gov.sa portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Certificates",
                "mandatory": True,
                "specification": "Scanned color copies of Matric/Intermediate (for Undergrad) or Bachelor's/Master's (for Postgrad) certificates.",
                "pakistan_specific_instruction": "Must be attested by IBCC / HEC and Ministry of Foreign Affairs (MoFA) Pakistan."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Scanned information page of ordinary passport valid for at least 18 months.",
                "pakistan_specific_instruction": "Pakistani passport must be valid through late 2027 or 2028."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Official medical report certified by a recognized hospital confirming freedom from infectious diseases (HIV, Hepatitis B/C, Tuberculosis).",
                "pakistan_specific_instruction": "Conducted at a recognized diagnostic laboratory and attested by MoFA."
            },
            {
                "document_name": "Police Clearance Certificate",
                "mandatory": True,
                "specification": "Recent certificate of good conduct issued by police authorities within the last 6 months.",
                "pakistan_specific_instruction": "Obtained from Police Khidmat Markaz and attested by MoFA."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Signed letters from former teachers or professors assessing character and academic capability.",
                "pakistan_specific_instruction": "Issued on official school/college letterhead with contact details."
            },
            {
                "document_name": "Birth Certificate",
                "mandatory": True,
                "specification": "Official NADRA Birth Certificate or Family Registration Certificate (FRC) in English.",
                "pakistan_specific_instruction": "NADRA computerized certificate attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "November 15",
            "university_admission_deadline": "November 15",
            "document_submission_deadline": "November 15",
            "recommendation_letters_deadline": "November 15",
            "interview_period": "No interview conducted",
            "shortlist_announcement": "May 1 - June 15",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July 1 - August 20",
            "semester_commencement": "Early September",
            "annual_cycle_notes": "Single annual intake cycle coordinated via the central Saudi 'Study in Saudi' portal for September fall semester enrollment."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (High school percentage / undergraduate CGPA)",
            "extracurricular_and_leadership_weight": "5% (Social engagement and community service)",
            "research_experience_weight": "15% (For postgraduates: thesis and research publications)",
            "work_experience_weight": "5% (Professional experience for postgraduates)",
            "personal_statement_weight": "10% (Clarity of purpose and motivations)",
            "recommendations_weight": "15% (Strength of academic endorsements)",
            "interview_weight": "0% (No interviews conducted)",
            "test_scores_weight": "0% (No standardized testing required)",
            "financial_need_weight": "0% (Merit and quota based government scholarship)",
            "selection_panel_composition": "Taibah University International Student Deanship and Ministry of Education Scholarship Review Board.",
            "evaluation_methodology": "Two-stage evaluation: academic merit ranking by university departments followed by security clearance by the Saudi Ministry of Interior and Ministry of Foreign Affairs."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~12,000 to 18,000 applicants globally on Study in Saudi portal for Taibah University",
            "total_scholarships_awarded": "~250 to 350 scholarships awarded annually across all levels",
            "acceptance_rate_global": "~2.0%",
            "acceptance_rate_pakistan": "~3.5% to 5.0% for applicants meeting top academic criteria (85%+ marks)",
            "typical_successful_applicant_gpa": "85%+ in Intermediate (FSc/ICS) or CGPA 3.40+ / 4.00 from an HEC-recognized university",
            "typical_academic_and_research_profile": "Outstanding academic record, impeccable discipline, clean legal record, and strong commitment to completing studies in Medina.",
            "common_backgrounds_of_winners": "Students from reputable colleges across Punjab, Sindh, KPK, and federal Islamabad.",
            "high_representation_countries": "Pakistan, Indonesia, Nigeria, Egypt, Yemen, Malaysia, Bangladesh, India.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent agents charging money promising guaranteed Saudi government scholarships to Medina.",
                "Legitimate applications are processed ONLY through studyinsaudi.moe.gov.sa and the official Taibah University website. Neither the university nor the Saudi government charges any fees."
            ],
            "application_fee_warning": "Applying for Saudi government scholarships is 100% free; never pay an intermediary.",
            "agent_and_intermediary_warnings": "The Ministry of Education strictly prohibits dealing with third-party brokers or educational agents.",
            "hidden_costs_breakdown": [
                "IBCC, HEC, and MoFA degree attestation fees in Pakistan (~PKR 15,000 to 25,000).",
                "Saudi Cultural Mission / Embassy consular attestation and Gerry's/Etimad visa fingerprinting: ~PKR 20,000 to 30,000.",
                "Medical screening tests at authorized GAMCA / approved diagnostic center: ~PKR 12,000 to 18,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You must already be fluent in Arabic to study engineering or computing in Saudi Arabia. Reality: STEM subjects are taught in English; free Arabic courses are provided for daily life.",
                "Myth: External scholarships allow candidates to sponsor work visas for family members. Reality: Student visa holders cannot sponsor work permits for relatives."
            ],
            "official_vs_unofficial_discrepancies": [
                "Social media posts claim direct paper submissions to the university in Medina; only digital applications through the 'Study in Saudi' portal are processed."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.75 / 5.00 (Good standing); failure leads to academic probation and suspension of monthly stipend if uncorrected.",
            "attendance_requirements": "Mandatory classroom attendance of at least 75%; unexcused absence results in course failure (Denial/Hirman).",
            "academic_progress_monitoring": "Semester-end academic audit conducted by the Deanship of Admissions; students must complete the degree within the approved statutory duration.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "Upon graduation, students must depart the Kingdom within the designated exit grace period unless approved for postgraduate study or authorized employment transition.",
            "service_obligations_or_bonds": "No financial bond or return service agreement enforced.",
            "repayment_clawback_conditions": "Scholarship terminated immediately for serious disciplinary infractions, violations of public order, or unexcused university abandonment.",
            "rules_for_changing_university": "Transferring to another Saudi university is extremely difficult and requires explicit Ministry of Education approval.",
            "rules_for_changing_major": "Major change permitted only within the same faculty during the first academic year subject to departmental capacity and GPA criteria.",
            "extension_policy": "Maximum extension of one additional semester permitted upon recommendation of the faculty council."
        },
        "official_sources_verified": [
            {
                "source_name": "Ministry of Education 'Study in Saudi' Official Portal",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Taibah University Deanship of Admission and Registration",
                "source_url": "https://www.taibahu.edu.sa/Pages/EN/Home.aspx",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-ME-016": {
        "scholarship_id": "SCH-ME-016",
        "basic_details": {
            "scholarship_name": "King Faisal University International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & King Faisal University (KFU)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "King Faisal University Main Campus (Al-Ahsa Oasis, Eastern Province, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to Computer Science and Information Technology, Agricultural and Food Sciences, Veterinary Medicine, Engineering, Science, Business Administration, Education, and Arts (Medical clinical colleges reserved for Saudi nationals).",
            "number_of_awards_total": "~200 to 300 government scholarships awarded annually to international students",
            "number_of_awards_pakistan": "Open bilateral competition; Pakistani scholars represent a major national group (~25 to 45 awards annually across computing, agriculture, and engineering)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic preparation if necessary)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Saudi citizenship (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate applicants must be between 17 and 25 years of age; Master's applicants under 30; PhD applicants under 35 years of age.",
            "academic_qualifications": "Intermediate (HSSC) / A-Levels with at least 80% aggregate for Bachelor's; recognized 16-year Bachelor's degree for Master's; 18-year Master's degree for PhD from an HEC-recognized institution with a minimum CGPA of 3.00 / 4.00.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Evaluated on Saudi 5.0 grading scale; equivalent to minimum 3.75 / 5.00.",
            "subject_background_prerequisites": "Pre-Engineering or ICS for Computer Science and Engineering; Pre-Medical for Agricultural Sciences, Food Science, and Veterinary Medicine.",
            "current_education_status": "Applicants must have completed secondary or tertiary education with official final transcripts.",
            "graduation_year_restrictions": "High school graduation certificate must not exceed 3 to 5 years from application date.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; prior laboratory or research exposure beneficial for graduate applicants.",
            "english_test_required": False,
            "ielts_minimum": 5.5,
            "toefl_minimum": 65,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "English is the medium of instruction in Computer Science, IT, Engineering, and Agricultural Sciences (MOI certificate accepted; IELTS 5.5+ or TOEFL 65 recommended). Arabic proficiency required for humanities and Islamic studies.",
            "other_language_requirements": "Free Arabic language training provided at KFU Language Center.",
            "gender_specific_requirements": "Female international students must reside in monitored university residential housing or with an officially recognized legal Mahram in Saudi Arabia.",
            "financial_need_required": False,
            "special_eligibility_categories": "Submitted via unified 'Study in Saudi' portal (studyinsaudi.moe.gov.sa).",
            "previous_scholarship_restrictions": "Cannot hold any concurrent Saudi government scholarship.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition exemption for the complete official degree duration.",
                "amount": "100% covered (~SAR 25,000 to 45,000 / year value; ~PKR 1,875,000 to 3,375,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application via 'Study in Saudi' portal is completely free.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free furnished on-campus student housing in KFU student residence halls in Al-Ahsa, including air-conditioned rooms, Wi-Fi, utilities, and sports facilities.",
                "amount": "100% covered free dormitory room"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly tax-free living stipend paid directly by the university: SAR 840 / month for undergraduate students (~USD 224; ~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~USD 240 to 266; ~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Free annual economy-class round-trip flight ticket between Pakistan and Dammam/Al-Ahsa provided at the conclusion of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Official Saudi student visa issued free of charge through the Royal Embassy of Saudi Arabia.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive 100% free healthcare provided at King Faisal University Health Center and affiliated government hospitals.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized campus meals served in university cafeterias for SAR 3 to 6 per meal; easily covered by the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to KFU Central Library, scientific electronic databases, and laboratory research facilities; initial book allowance provided upon arrival.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Postgraduate thesis printing subsidy (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial awards for publishing in high-impact ISI/Scopus journals.",
                "amount": "SAR 3,000 to 4,000 thesis allowance"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Free university campus shuttle transport between student dormitories and academic colleges.",
                "amount": "100% free university campus transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (King Faisal University, Al-Ahsa)",
            "participating_institutions": [
                "King Faisal University (KFU) Main Campus (Al-Ahsa, Eastern Province, Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #45, Times Higher Education Asia #151-200, global leader in Agricultural Sciences, Food Security, and Water Engineering.",
            "available_majors": [
                "Computer Science",
                "Information Systems",
                "Computer Networks and Communications",
                "Agricultural Sciences and Plant Protection",
                "Food Science and Human Nutrition",
                "Veterinary Medicine and Animal Resources",
                "Civil Engineering",
                "Mechanical Engineering",
                "Electrical Engineering",
                "Business Administration and Accounting",
                "Chemistry and Applied Physics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Online registration on 'Study in Saudi' portal, high school or university transcripts with minimum 80% / 3.0 CGPA, valid passport copy, police character certificate, medical fitness report, and two academic recommendation letters.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Agricultural and Food Sciences have world-class research facilities and strong funding quotas; Computer Science and Engineering have high applicant volumes from South Asia.",
            "strategic_program_match_advice": "Ensure educational documents are verified by IBCC or HEC and attested by the Ministry of Foreign Affairs (MoFA) before uploading to the portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.kfu.edu.sa/",
            "portal_system_name": "Study in Saudi Portal & KFU Deanship of Admissions",
            "account_creation_instructions": "Register on the 'Study in Saudi' system, choose 'External Scholarship', specify King Faisal University, select degree program, and upload color document scans.",
            "step_by_step_workflow": [
                "Step 1: Check application window on studyinsaudi.moe.gov.sa (typically opens September/October).",
                "Step 2: Complete profile registration, enter educational qualifications and percentages.",
                "Step 3: Upload color scans of passport, educational certificates, transcripts, police report, and medical clearance.",
                "Step 4: Select King Faisal University and arrange desired programs in order of preference.",
                "Step 5: Submit application online without application fee and retain application tracking reference.",
                "Step 6: KFU admissions board screens applications and submits candidate nominations to the Ministry of Education (December - March).",
                "Step 7: Final approvals granted by Saudi Ministry of Education and Ministry of Foreign Affairs (May - July).",
                "Step 8: Admission confirmation and visa authorization issued on the portal.",
                "Step 9: Complete visa processing at Gerry's / Etimad in Pakistan, obtain university-booked flight ticket, and travel to Saudi Arabia in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Admission and full scholarship are processed concurrently through the 'Study in Saudi' system.",
            "recommendation_letters_submission_method": "Uploaded as scanned PDF documents on institutional letterhead signed by referees.",
            "personal_statement_prompts": "Statement explaining motivation for studying at King Faisal University and how the chosen discipline aligns with future career goals.",
            "study_plan_research_proposal_requirements": "For postgraduate applicants: 3 to 5-page research plan detailing problem statement, proposed methodology, and expected outcomes.",
            "cv_format_requirements": "Academic CV detailing educational trajectory, skills, and extracurricular activities.",
            "interviews_conducted": False,
            "interview_format_details": "No oral interview; selection based purely on document evaluation and Ministry verification.",
            "standardized_tests": "Not required for international external applicants.",
            "application_fee_amount": "SAR 0 (100% Free)",
            "attestation_requirements": "Degrees and transcripts must be attested by IBCC / HEC, MoFA Pakistan, and the Saudi Cultural Mission / Royal Embassy of Saudi Arabia.",
            "translation_requirements": "Certified Arabic or English translation required for documents in other languages.",
            "final_submission_method": "100% online submission via studyinsaudi.moe.gov.sa."
        },
        "required_documents_checklist": [
            {
                "document_name": "Certified Academic Certificates and Transcripts",
                "mandatory": True,
                "specification": "Complete high school (Intermediate/A-Levels) or degree certificates and grade sheets.",
                "pakistan_specific_instruction": "Attested by IBCC or HEC and Ministry of Foreign Affairs (MoFA) Pakistan."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of passport info page with at least 18 months remaining validity.",
                "pakistan_specific_instruction": "Pakistani passport must be valid through late 2027 or 2028."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Comprehensive medical examination report certifying freedom from communicable diseases.",
                "pakistan_specific_instruction": "Conducted at a recognized diagnostic laboratory and attested by MoFA."
            },
            {
                "document_name": "Police Clearance Certificate",
                "mandatory": True,
                "specification": "Official certificate confirming no criminal convictions issued within the last 6 months.",
                "pakistan_specific_instruction": "Issued by Police Khidmat Markaz and attested by MoFA."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Written appraisals from academic teachers or professors endorsing character and competence.",
                "pakistan_specific_instruction": "On official school/college letterhead with contact details."
            },
            {
                "document_name": "Birth Certificate",
                "mandatory": True,
                "specification": "Official birth certificate or NADRA Family Registration Certificate (FRC).",
                "pakistan_specific_instruction": "NADRA computerized certificate in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "November 15",
            "university_admission_deadline": "November 15",
            "document_submission_deadline": "November 15",
            "recommendation_letters_deadline": "November 15",
            "interview_period": "No interview conducted",
            "shortlist_announcement": "May 1 - June 15",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July 1 - August 20",
            "semester_commencement": "Early September",
            "annual_cycle_notes": "Single annual intake cycle aligned with the Saudi national 'Study in Saudi' academic admissions calendar."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Academic percentage and GPA record)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular participation)",
            "research_experience_weight": "15% (For postgraduates: research background and proposal)",
            "work_experience_weight": "5% (Relevant industry/technical experience)",
            "personal_statement_weight": "10% (Statement of purpose clarity)",
            "recommendations_weight": "15% (Academic referee assessments)",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "0% (No standardized tests required)",
            "financial_need_weight": "0% (Merit-based government award)",
            "selection_panel_composition": "King Faisal University Admissions Board and Saudi Ministry of Education Scholarship Committee.",
            "evaluation_methodology": "Academic ranking followed by governmental security clearance and visa allocation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000 to 15,000 international applicants across all disciplines",
            "total_scholarships_awarded": "~200 to 300 international scholarships awarded annually",
            "acceptance_rate_global": "~2.0% to 2.5%",
            "acceptance_rate_pakistan": "~4.0% for applicants with top-tier academic scores (85%+)",
            "typical_successful_applicant_gpa": "85%+ in Intermediate (FSc/ICS) or CGPA 3.30+ / 4.00 from an HEC-recognized university",
            "typical_academic_and_research_profile": "High academic grades, strong discipline, clean record, and demonstrated enthusiasm for studying in Saudi Arabia.",
            "common_backgrounds_of_winners": "Graduates of reputable colleges and universities across Pakistan.",
            "high_representation_countries": "Pakistan, Indonesia, Nigeria, Egypt, Jordan, Bangladesh, Sudan, India.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized consultancy websites promising guaranteed KFU admissions for fees.",
                "Applications are processed exclusively through studyinsaudi.moe.gov.sa and kfu.edu.sa without any fees."
            ],
            "application_fee_warning": "Applying for the scholarship is 100% free of charge; do not pay any agent.",
            "agent_and_intermediary_warnings": "King Faisal University does not authorize recruitment agencies or private intermediaries.",
            "hidden_costs_breakdown": [
                "Attestation fees in Pakistan (IBCC/HEC and MoFA): ~PKR 15,000 to 25,000.",
                "Consular attestation and biometric visa processing fees at Gerry's/Etimad: ~PKR 20,000 to 30,000.",
                "Medical diagnostics at an approved clinic: ~PKR 12,000 to 18,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You cannot study computer science or agriculture in English. Reality: KFU delivers computing, engineering, and agricultural disciplines in English.",
                "Myth: Scholarship covers family living expenses. Reality: The scholarship covers only the individual student; bringing dependents requires separate personal financial sponsorship."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim paper documents must be mailed to Al-Ahsa; only online applications through 'Study in Saudi' are accepted."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.75 / 5.00; failing to maintain Good standing leads to academic warning and stipend suspension.",
            "attendance_requirements": "Minimum 75% attendance in all courses; exceeding 25% unexcused absence results in course deprivation (Hirman).",
            "academic_progress_monitoring": "Annual progress evaluated by the Deanship of Admissions; studies must be completed within standard degree limits.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "Students must depart Saudi Arabia upon completion of studies unless transitioning to approved employment or higher graduate study.",
            "service_obligations_or_bonds": "No bond or mandatory service agreement.",
            "repayment_clawback_conditions": "Scholarship revoked if the student is expelled for disciplinary misconduct or unexcused withdrawal.",
            "rules_for_changing_university": "University transfers are prohibited under external scholarship terms.",
            "rules_for_changing_major": "Major change permitted only within the same college during the first academic year subject to GPA requirements.",
            "extension_policy": "Maximum extension of one semester granted in exceptional circumstances upon faculty recommendation."
        },
        "official_sources_verified": [
            {
                "source_name": "Ministry of Education 'Study in Saudi' Official Portal",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "King Faisal University Official Portal",
                "source_url": "https://www.kfu.edu.sa/en/Pages/Home.aspx",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-ME-017": {
        "scholarship_id": "SCH-ME-017",
        "basic_details": {
            "scholarship_name": "Jazan University International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & Jazan University",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "Jazan University Main Campus (Jazan City, Red Sea Coast, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to Computer Science and Information Technology, Engineering, Marine and Environmental Sciences, Science, Business Administration, Arts, and Humanities (Medical colleges restricted to Saudi citizens).",
            "number_of_awards_total": "~200 to 280 external government scholarships awarded annually to international students",
            "number_of_awards_pakistan": "Open bilateral competition; Pakistani students represent a substantial cohort (~25 to 40 awards annually across engineering, science, and computing)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic preparation if required)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Saudi citizenship (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate applicants must be between 17 and 25 years old; Master's applicants under 30; PhD applicants under 35 years of age.",
            "academic_qualifications": "Intermediate (HSSC) / A-Levels with at least 80% aggregate for Bachelor's; recognized 16-year Bachelor's degree for Master's; 18-year Master's degree for PhD from an HEC-recognized institution with a minimum CGPA of 3.00 / 4.00.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Transcript grades evaluated on Saudi 5.0 scale (equivalent to minimum 3.75 / 5.00).",
            "subject_background_prerequisites": "Pre-Engineering or ICS for Computer Science and Engineering; Pre-Medical or General Science for Marine and Natural Sciences.",
            "current_education_status": "Applicants must have completed secondary or tertiary education with official certificates available.",
            "graduation_year_restrictions": "High school diploma must not be older than 3 to 5 years from application date.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; research background beneficial for postgraduates.",
            "english_test_required": False,
            "ielts_minimum": 5.5,
            "toefl_minimum": 65,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "STEM programs are taught in English (MOI certificate accepted; IELTS 5.5+ or TOEFL 65 recommended). Arabic proficiency required for humanities and Islamic studies.",
            "other_language_requirements": "Free Arabic language instruction provided for non-native speakers.",
            "gender_specific_requirements": "Female international students must reside in monitored university residential housing or with an officially recognized legal Mahram in Saudi Arabia.",
            "financial_need_required": False,
            "special_eligibility_categories": "Submitted via unified 'Study in Saudi' portal (studyinsaudi.moe.gov.sa).",
            "previous_scholarship_restrictions": "Cannot hold any concurrent Saudi government scholarship.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee exemption for the entire official duration of study.",
                "amount": "100% covered (~SAR 25,000 to 40,000 / year value; ~PKR 1,875,000 to 3,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application via 'Study in Saudi' portal is completely free.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free furnished student accommodation in Jazan University modern residential halls overlooking the Red Sea, including Wi-Fi, utilities, and sports facilities.",
                "amount": "100% covered free dormitory room"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly tax-free living stipend paid directly by the university: SAR 840 / month for undergraduate students (~USD 224; ~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~USD 240 to 266; ~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Free annual economy-class round-trip flight ticket between Pakistan and Jazan provided at the end of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Official Saudi student visa issued free of charge through the Royal Embassy of Saudi Arabia.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive 100% free healthcare provided at Jazan University Medical Center and regional public hospitals.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized campus meals served in university cafeterias for SAR 3 to 6 per meal; easily covered by the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Jazan University digital libraries and research laboratory facilities; initial book allowance provided upon arrival.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Postgraduate thesis printing subsidy (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial incentives for scientific publications.",
                "amount": "SAR 3,000 to 4,000 thesis allowance"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Free university campus shuttle transport between student dormitories and academic faculties.",
                "amount": "100% free university campus transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Jazan University, Jazan)",
            "participating_institutions": [
                "Jazan University Main Campus (Jazan City, Kingdom of Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #71-80, Times Higher Education Asia #251-300, recognized for excellence in Marine Sciences, Environmental Studies, and Engineering.",
            "available_majors": [
                "Computer Science",
                "Information Technology",
                "Computer Engineering and Networks",
                "Civil Engineering",
                "Mechanical Engineering",
                "Electrical Engineering",
                "Marine and Fisheries Sciences",
                "Environmental Sciences",
                "Chemistry and Industrial Chemistry",
                "Physics",
                "Business Administration and Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Online registration on 'Study in Saudi' portal, high school or university transcripts with minimum 80% / 3.0 CGPA, valid passport copy, police character certificate, medical fitness report, and two academic recommendation letters.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Marine Sciences and Environmental Engineering have prominent research facilities and high international quota availability; Computer Science has strong regional demand.",
            "strategic_program_match_advice": "Ensure educational documents are verified by IBCC or HEC and attested by the Ministry of Foreign Affairs (MoFA) before uploading to the portal."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.jazanu.edu.sa/en",
            "portal_system_name": "Study in Saudi Portal & Jazan University Deanship of Admissions",
            "account_creation_instructions": "Register on the 'Study in Saudi' system, choose 'External Scholarship', specify Jazan University, select degree program, and upload color document scans.",
            "step_by_step_workflow": [
                "Step 1: Check application window on studyinsaudi.moe.gov.sa (typically opens September/October).",
                "Step 2: Complete profile registration, enter educational qualifications and percentages.",
                "Step 3: Upload color scans of passport, educational certificates, transcripts, police report, and medical clearance.",
                "Step 4: Select Jazan University and arrange desired programs in order of preference.",
                "Step 5: Submit application online without application fee and retain application tracking reference.",
                "Step 6: Jazan University admissions board screens applications and submits candidate nominations to the Ministry of Education (December - March).",
                "Step 7: Final approvals granted by Saudi Ministry of Education and Ministry of Foreign Affairs (May - July).",
                "Step 8: Admission confirmation and visa authorization issued on the portal.",
                "Step 9: Complete visa processing at Gerry's / Etimad in Pakistan, obtain university-booked flight ticket, and travel to Jazan in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Admission and full scholarship are processed concurrently through the 'Study in Saudi' system.",
            "recommendation_letters_submission_method": "Uploaded as scanned PDF documents on institutional letterhead signed by referees.",
            "personal_statement_prompts": "Statement explaining motivation for studying at Jazan University and how the chosen discipline aligns with future career goals.",
            "study_plan_research_proposal_requirements": "For postgraduate applicants: 3 to 5-page research plan detailing problem statement, proposed methodology, and expected outcomes.",
            "cv_format_requirements": "Academic CV detailing educational trajectory, skills, and extracurricular activities.",
            "interviews_conducted": False,
            "interview_format_details": "No oral interview; selection based purely on document evaluation and Ministry verification.",
            "standardized_tests": "Not required for international external applicants.",
            "application_fee_amount": "SAR 0 (100% Free)",
            "attestation_requirements": "Degrees and transcripts must be attested by IBCC / HEC, MoFA Pakistan, and the Saudi Cultural Mission / Royal Embassy of Saudi Arabia.",
            "translation_requirements": "Certified Arabic or English translation required for documents in other languages.",
            "final_submission_method": "100% online submission via studyinsaudi.moe.gov.sa."
        },
        "required_documents_checklist": [
            {
                "document_name": "Certified Academic Certificates and Transcripts",
                "mandatory": True,
                "specification": "Complete high school (Intermediate/A-Levels) or degree certificates and grade sheets.",
                "pakistan_specific_instruction": "Attested by IBCC or HEC and Ministry of Foreign Affairs (MoFA) Pakistan."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of passport info page with at least 18 months remaining validity.",
                "pakistan_specific_instruction": "Pakistani passport must be valid through late 2027 or 2028."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Comprehensive medical examination report certifying freedom from communicable diseases.",
                "pakistan_specific_instruction": "Conducted at a recognized diagnostic laboratory and attested by MoFA."
            },
            {
                "document_name": "Police Clearance Certificate",
                "mandatory": True,
                "specification": "Official certificate confirming no criminal convictions issued within the last 6 months.",
                "pakistan_specific_instruction": "Issued by Police Khidmat Markaz and attested by MoFA."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Written appraisals from academic teachers or professors endorsing character and competence.",
                "pakistan_specific_instruction": "On official school/college letterhead with contact details."
            },
            {
                "document_name": "Birth Certificate",
                "mandatory": True,
                "specification": "Official birth certificate or NADRA Family Registration Certificate (FRC).",
                "pakistan_specific_instruction": "NADRA computerized certificate in English attested by MoFA."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "November 15",
            "university_admission_deadline": "November 15",
            "document_submission_deadline": "November 15",
            "recommendation_letters_deadline": "November 15",
            "interview_period": "No interview conducted",
            "shortlist_announcement": "May 1 - June 15",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July 1 - August 20",
            "semester_commencement": "Early September",
            "annual_cycle_notes": "Single annual intake cycle aligned with the Saudi national 'Study in Saudi' academic admissions calendar."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Academic percentage and GPA record)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular participation)",
            "research_experience_weight": "15% (For postgraduates: research background and proposal)",
            "work_experience_weight": "5% (Relevant industry/technical experience)",
            "personal_statement_weight": "10% (Statement of purpose clarity)",
            "recommendations_weight": "15% (Academic referee assessments)",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "0% (No standardized tests required)",
            "financial_need_weight": "0% (Merit-based government award)",
            "selection_panel_composition": "Jazan University Admissions Board and Saudi Ministry of Education Scholarship Committee.",
            "evaluation_methodology": "Academic ranking followed by governmental security clearance and visa allocation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~8,000 to 12,000 international applicants across all disciplines",
            "total_scholarships_awarded": "~200 to 280 international scholarships awarded annually",
            "acceptance_rate_global": "~2.5%",
            "acceptance_rate_pakistan": "~4.5% for applicants with top-tier academic scores (85%+)",
            "typical_successful_applicant_gpa": "85%+ in Intermediate (FSc/ICS) or CGPA 3.30+ / 4.00 from an HEC-recognized university",
            "typical_academic_and_research_profile": "High academic grades, strong discipline, clean record, and demonstrated enthusiasm for studying in Saudi Arabia.",
            "common_backgrounds_of_winners": "Graduates of reputable colleges and universities across Pakistan.",
            "high_representation_countries": "Pakistan, Indonesia, Nigeria, Egypt, Jordan, Bangladesh, Sudan, India.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized consultancy websites promising guaranteed Jazan University admissions for fees.",
                "Applications are processed exclusively through studyinsaudi.moe.gov.sa and jazanu.edu.sa without any fees."
            ],
            "application_fee_warning": "Applying for the scholarship is 100% free of charge; do not pay any agent.",
            "agent_and_intermediary_warnings": "Jazan University does not authorize recruitment agencies or private intermediaries.",
            "hidden_costs_breakdown": [
                "Attestation fees in Pakistan (IBCC/HEC and MoFA): ~PKR 15,000 to 25,000.",
                "Consular attestation and biometric visa processing fees at Gerry's/Etimad: ~PKR 20,000 to 30,000.",
                "Medical diagnostics at an approved clinic: ~PKR 12,000 to 18,000."
            ],
            "misleading_claims_debunked": [
                "Myth: Jazan University is isolated and lacks modern infrastructure. Reality: It boasts a state-of-the-art multi-billion dollar coastal university campus with leading marine and engineering centers.",
                "Myth: Scholarship covers family living expenses. Reality: The scholarship covers only the individual student."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim paper documents must be mailed to Jazan; only online applications through 'Study in Saudi' are accepted."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.75 / 5.00; failing to maintain Good standing leads to academic warning and stipend suspension.",
            "attendance_requirements": "Minimum 75% attendance in all courses; exceeding 25% unexcused absence results in course deprivation (Hirman).",
            "academic_progress_monitoring": "Annual progress evaluated by the Deanship of Admissions; studies must be completed within standard degree limits.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "Students must depart Saudi Arabia upon completion of studies unless transitioning to approved employment or higher graduate study.",
            "service_obligations_or_bonds": "No bond or mandatory service agreement.",
            "repayment_clawback_conditions": "Scholarship revoked if the student is expelled for disciplinary misconduct or unexcused withdrawal.",
            "rules_for_changing_university": "University transfers are prohibited under external scholarship terms.",
            "rules_for_changing_major": "Major change permitted only within the same college during the first academic year subject to GPA requirements.",
            "extension_policy": "Maximum extension of one semester granted in exceptional circumstances upon faculty recommendation."
        },
        "official_sources_verified": [
            {
                "source_name": "Ministry of Education 'Study in Saudi' Official Portal",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Jazan University Official Portal",
                "source_url": "https://www.jazanu.edu.sa/en",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-ME-028": {
        "scholarship_id": "SCH-ME-028",
        "basic_details": {
            "scholarship_name": "New York University Abu Dhabi (NYUAD) Global Leaders Fellowship & Financial Aid",
            "offering_entity": "New York University Abu Dhabi (NYUAD) & Abu Dhabi Department of Education and Knowledge (ADEK)",
            "host_country": "United Arab Emirates",
            "host_institutions_covered": "New York University Abu Dhabi (Saadiyat Island Campus, Abu Dhabi, UAE)",
            "degree_levels": ["Bachelor of Arts (BA)", "Bachelor of Science (BS)"],
            "major_restrictions": "Open to all 26 undergraduate majors across Engineering (Computer, Electrical, Mechanical, Civil, General), Science (Biology, Chemistry, Computer Science, Data Science, Mathematics, Physics, Psychology), Social Sciences (Economics, Political Science, SRPP), and Arts & Humanities.",
            "number_of_awards_total": "~400 to 500 undergraduate scholars supported annually with comprehensive need-based institutional fellowship awards",
            "number_of_awards_pakistan": "Extremely prestigious cohort; Pakistani high school scholars secure ~15 to 25 full fellowship awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 years of full-time undergraduate study, including 2 study-abroad semesters within NYU's global network (New York, Paris, London, Tokyo, etc.)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to outstanding students of all nationalities globally (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; applicants are typically graduating high school seniors or gap year students.",
            "academic_qualifications": "High school diploma / Intermediate (FSc/ICS) with 90%+ marks, or A-Levels with minimum AAA / A*AA grades, or International Baccalaureate (IB) 38+ points. Class rank typically in the top 1-2%.",
            "minimum_gpa_percentage": 90.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Holistic review of high school transcript (Grades 9-12); unweighted GPA equivalent of 3.8+ / 4.00.",
            "subject_background_prerequisites": "Rigorous coursework in mathematics, natural sciences, and humanities.",
            "current_education_status": "High school seniors in their final year can apply with predicted grades; gap year students eligible.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Extraordinary extracurricular leadership, Olympiad awards, debate championships, or social impact initiatives strongly emphasized.",
            "english_test_required": True,
            "ielts_minimum": 7.5,
            "toefl_minimum": 100,
            "duolingo_accepted": True,
            "moi_certificate_accepted": True,
            "language_notes": "TOEFL iBT min 100, IELTS Academic min 7.5, Duolingo English Test (DET) min 130, or Cambridge English C1/C2. English proficiency waiver available if applicant's secondary education was entirely in English.",
            "other_language_requirements": "None; instruction is entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": True,
            "special_eligibility_categories": "Fellowship is awarded based on demonstrated financial need (CSS Profile) combined with academic and leadership excellence; NYUAD meets 100% of demonstrated financial need.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver for the complete 4-year undergraduate degree (~USD 60,000 / year value).",
                "amount": "100% covered (~USD 60,000 / year; ~PKR 16,800,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Common Application fee of USD 80 can be waived via Common App Fee Waiver for students demonstrating financial need.",
                "amount": "USD 0 (Fee waiver available)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "100% covered modern single/double student residential housing on Saadiyat Island Campus (~USD 12,000 / year value), including utilities, Wi-Fi, air conditioning, and cleaning.",
                "amount": "100% covered (~USD 12,000 / year; ~PKR 3,360,000 / year)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Comprehensive personal allowance and campus life stipend of ~AED 1,500 to 2,500 / month (~USD 400 to 680 / month; ~PKR 112,000 to 190,000 / month) to cover books, local transport, and miscellaneous personal expenses.",
                "amount": "~AED 2,000 / month (~PKR 150,000 / mo)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Two economy-class round-trip flights per academic year between Pakistan and Abu Dhabi, plus fully covered airfare and accommodations for January Term (J-Term) global study courses worldwide.",
                "amount": "100% covered round-trip flights + J-Term travel"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "UAE Student Residence Visa application, medical fitness screening, and Emirates ID fees fully sponsored and managed by NYUAD.",
                "amount": "100% covered by NYUAD"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive worldwide international health insurance policy (Abu Dhabi National Insurance Company - ADNIC) covering inpatient, outpatient, emergency medical evacuation, and dental/vision.",
                "amount": "100% covered worldwide health insurance"
            },
            "food_allowance": {
                "status": "100% COVERED",
                "details": "Full university meal plan (Falcon Dinar dining plan) covering 3 full meals per day across campus dining halls, cafes, and halal dining venues (~USD 6,000 / year value).",
                "amount": "100% covered campus meal plan"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Dedicated course materials allowance and lab supply grant (~USD 1,000 / year) plus high-spec engineering laptop loan/issuance.",
                "amount": "100% covered books & materials"
            },
            "research_funding_conference_grant": {
                "status": "100% COVERED",
                "details": "Summer research grants (up to USD 4,000), Capstone project funding, and undergraduate conference presentation travel grants.",
                "amount": "Up to USD 4,000 summer research grant"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Free university shuttles connecting Saadiyat Island Campus to downtown Abu Dhabi, malls, and cultural districts.",
                "amount": "100% free university shuttle transport"
            },
            "total_estimated_value_usd_per_year": 85000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single portal university with global rotation (NYU Abu Dhabi + NYU Global Network)",
            "participating_institutions": [
                "New York University Abu Dhabi (Saadiyat Island Campus, Abu Dhabi, UAE)",
                "NYU Washington Square (New York City, USA)",
                "NYU Shanghai (Pudong, Shanghai, China)",
                "NYU Global Academic Centers (London, Paris, Berlin, Madrid, Florence, Buenos Aires, Sydney, Accra)"
            ],
            "university_rankings_scope": "NYU ranked #38 QS World University Rankings, #32 Times Higher Education, #16 US News Global. NYUAD degrees are awarded directly by New York University.",
            "available_majors": [
                "Computer Science",
                "Computer Engineering",
                "Electrical Engineering",
                "Mechanical Engineering",
                "Civil Engineering",
                "Data Science",
                "Economics",
                "Biology",
                "Chemistry",
                "Physics",
                "Mathematics",
                "Social Research and Public Policy (SRPP)",
                "Interactive Media",
                "Political Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (full-time undergraduate)",
            "admission_requirements_summary": "Common Application submission, NYU-specific supplement, high school transcripts (Grades 9-12), counselor recommendation, two teacher recommendations, SAT/ACT (optional), English proficiency test (TOEFL/IELTS/DET), and CSS Profile for financial aid.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "NYUAD is one of the most selective undergraduate institutions on earth (acceptance rate ~3-4%); shortlisted finalists are flown all-expenses-paid to Abu Dhabi for the renowned 'Candidate Weekend' before final admission offers are rendered.",
            "strategic_program_match_advice": "Focus heavily on unique intellectual curiosity and global citizenship in the Common App essays. If NYUAD is your unequivocal first choice, applying Early Decision (ED1 or ED2) significantly maximizes admission probability."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.commonapp.org/ & https://nyuad.nyu.edu/",
            "portal_system_name": "The Common Application & College Board CSS Profile",
            "account_creation_instructions": "Create account on Common App, add New York University, select Abu Dhabi campus as primary campus of interest, and complete the CSS Profile on cssprofile.collegeboard.org.",
            "step_by_step_workflow": [
                "Step 1: Complete Common Application profile, activities list, personal essay, and NYU-specific essay prompts (August - October).",
                "Step 2: Submit official secondary school transcripts (Grades 9-11 and Grade 12 first-term / predicted grades) via school counselor.",
                "Step 3: Have academic teachers submit two detailed recommendation letters.",
                "Step 4: Complete and submit the CSS Profile for financial aid, uploading parent income tax returns and salary certificates to IDOC.",
                "Step 5: Submit application by deadline: Early Decision 1 (Nov 1), Early Decision 2 (Jan 1), or Regular Decision (Jan 5).",
                "Step 6: Selected semifinalists receive invitations to NYUAD 'Candidate Weekend' (all-expenses-paid visit to Abu Dhabi or virtual immersive experience).",
                "Step 7: Admissions committee renders final admission and comprehensive fellowship package (mid-December for ED1, mid-February for ED2, late March for RD).",
                "Step 8: Sign enrollment agreement, submit visa documentation to NYUAD Student Mobility Office.",
                "Step 9: Arrive in Abu Dhabi in late August for the international student orientation program (Marhaba Week)."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Admission automatically qualifies students for 100% need-met financial aid via the CSS Profile.",
            "recommendation_letters_submission_method": "Submitted online by school counselor and teachers directly through Common Application portal.",
            "personal_statement_prompts": "Common App personal statement (650 words) plus NYU supplemental essay exploring why NYU's global network and Abu Dhabi campus uniquely resonate with applicant's intellectual ambitions.",
            "study_plan_research_proposal_requirements": "Not required for undergraduates; evaluated on academic passion and extracurricular depth.",
            "cv_format_requirements": "Embedded Common App activities sheet (up to 10 activities with detailed descriptions of impact and hours).",
            "interviews_conducted": True,
            "interview_format_details": "Extensive interviews and collaborative group activities conducted during the exclusive NYUAD 'Candidate Weekend' by faculty and admissions deans.",
            "standardized_tests": "Test-Optional (SAT/ACT not mandatory; competitive applicants submitting scores typically present SAT 1480-1560 or ACT 33-35).",
            "application_fee_amount": "USD 80 (Fee waiver available via Common App for financial hardship)",
            "attestation_requirements": "Final high school diploma and transcripts must be authenticated by IBCC/British Council, MoFA Pakistan, and the UAE Embassy in Islamabad upon enrollment.",
            "translation_requirements": "Certified English translation required for any documents not in English.",
            "final_submission_method": "100% online submission via Common App and CSS Profile."
        },
        "required_documents_checklist": [
            {
                "document_name": "Common Application with NYU Supplement",
                "mandatory": True,
                "specification": "Completed online Common Application specifying NYU Abu Dhabi as primary campus.",
                "pakistan_specific_instruction": "Ensure applicant legal name matches Pakistani passport exactly."
            },
            {
                "document_name": "Secondary School Transcripts (Grades 9-12)",
                "mandatory": True,
                "specification": "Official academic transcripts for Grades 9, 10, 11, and predicted/mid-year Grade 12 results.",
                "pakistan_specific_instruction": "Matric/FSc mark sheets or O/A Level statement of results uploaded by school counselor."
            },
            {
                "document_name": "Counselor Recommendation and School Report",
                "mandatory": True,
                "specification": "Official school profile and comprehensive recommendation letter from secondary school counselor.",
                "pakistan_specific_instruction": "Must include grading scale explanation and class ranking where available."
            },
            {
                "document_name": "Two Teacher Evaluation Letters",
                "mandatory": True,
                "specification": "Letters from academic teachers who taught core subjects in Grade 11 or 12.",
                "pakistan_specific_instruction": "Submitted via Common App by Pakistani school faculty."
            },
            {
                "document_name": "College Board CSS Profile and Tax Documentation",
                "mandatory": True,
                "specification": "Completed CSS Profile detailing household income and assets, with supporting tax returns submitted via IDOC.",
                "pakistan_specific_instruction": "FBR tax returns, bank statements, or employer salary slips translated and uploaded."
            },
            {
                "document_name": "English Proficiency Test Score Report",
                "mandatory": True,
                "specification": "TOEFL iBT (min 100), IELTS Academic (min 7.5), Duolingo English Test (min 130), or Cambridge C1/C2.",
                "pakistan_specific_instruction": "Waiver granted if secondary schooling was in English medium."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Scanned copy of passport photo page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity extending into late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "August 1",
            "application_deadline": "November 1 (Early Decision 1) / January 1 (Early Decision 2) / January 5 (Regular Decision)",
            "university_admission_deadline": "November 1 / January 1 / January 5",
            "document_submission_deadline": "November 15 / January 15 / January 15",
            "recommendation_letters_deadline": "November 15 / January 15 / January 15",
            "interview_period": "Late November (ED1) / Mid-January (ED2) / Late February (RD) - Candidate Weekend",
            "shortlist_announcement": "December 15 (ED1) / February 15 (ED2) / Late March (RD)",
            "final_result_acceptance_deadline": "January 15 (ED1) / March 1 (ED2) / May 1 (RD)",
            "visa_application_window": "May 1 - July 15",
            "semester_commencement": "Late August",
            "annual_cycle_notes": "Highly structured US admissions timeline. Early Decision (ED1/ED2) is binding and offers significantly higher acceptance rates than Regular Decision."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (High school transcript rigor, grades, and intellectual curiosity)",
            "extracurricular_and_leadership_weight": "25% (Exceptional leadership, social initiatives, and national/international awards)",
            "research_experience_weight": "5% (Olympiad/science fair projects where applicable)",
            "work_experience_weight": "5% (Community engagement, internships, or entrepreneurship)",
            "personal_statement_weight": "15% (Common App essay and NYU supplemental essay authenticity)",
            "recommendations_weight": "10% (Counselor and teacher evaluations)",
            "interview_weight": "5% (Candidate Weekend faculty and student interviews)",
            "test_scores_weight": "0% (Test-optional policy)",
            "financial_need_weight": "0% (Need-blind / meet-100%-of-need financial aid policy)",
            "selection_panel_composition": "NYUAD Admissions Committee, Deans of Academic Divisions, and Global Undergraduate Admissions Board.",
            "evaluation_methodology": "Holistic review assessing intellectual distinction, leadership promise, intercultural sensitivity, and community contribution."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~18,000 to 22,000 applicants globally competing for NYU Abu Dhabi",
            "total_scholarships_awarded": "~400 to 500 undergraduate fellowship packages awarded annually",
            "acceptance_rate_global": "~3.0% to 4.0%",
            "acceptance_rate_pakistan": "~4.0% to 5.5% among elite applicants invited to Candidate Weekend",
            "typical_successful_applicant_gpa": "Top 1-2% of graduating class, A*A*A in A-Levels, 92%+ in FSc/Matric, or SAT 1500+",
            "typical_academic_and_research_profile": "World-class intellectual vitality combined with extraordinary extracurricular leadership (national debate champions, non-profit founders, Olympiad medalists).",
            "common_backgrounds_of_winners": "Graduates of top Pakistani schools (Aitchison, KGS, Cedar, Nixor, Roots, Beaconhouse, LGS) and high-achieving public sector college students.",
            "high_representation_countries": "USA, UAE, Pakistan, India, China, South Korea, Egypt, Jordan, Germany, Brazil.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell admission or scholarship packages to NYU Abu Dhabi.",
                "Applications are handled exclusively via Common App (commonapp.org) and nyuad.nyu.edu."
            ],
            "application_fee_warning": "Common App charges an USD 80 fee, but fee waivers are readily granted to international students demonstrating financial need. Never pay third-party agents.",
            "agent_and_intermediary_warnings": "NYU does not work with commercial placement agencies or educational brokers under any circumstances.",
            "hidden_costs_breakdown": [
                "CSS Profile fee: USD 25 for first school, USD 16 per additional school (waivers available for qualifying low-income applicants).",
                "Standardized testing fees if taking SAT (~USD 110) or IELTS/TOEFL (~PKR 60,000).",
                "Attestation of educational records in Pakistan upon final admission (~PKR 25,000 to 35,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: NYUAD only awards scholarships to UAE nationals. Reality: Over 85% of NYUAD students are international from 120+ nations, and virtually all eligible internationals receive full need-based financial aid.",
                "Myth: You cannot study abroad on the scholarship. Reality: The fellowship fully covers tuition and living stipends for up to 2 semesters at any NYU global site (New York, Paris, Florence, London, etc.) plus January Term travel."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums claim SAT scores are mandatory; NYU maintains a strict Test-Optional policy for all undergraduate applicants."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic progress (minimum cumulative GPA of 2.0 / 4.0 for Good Standing; competitive standing 3.0+).",
            "attendance_requirements": "Full-time enrollment (minimum 12-16 credits per semester) and active campus participation.",
            "academic_progress_monitoring": "Semester-end academic progress review by the Dean of Students and Academic Advising.",
            "work_restrictions_during_study": "On-campus student employment permitted up to 20 hours per week during term; off-campus employment restricted under UAE student visa regulations.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for UAE Golden Visa (top university graduate category) or international careers globally.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the fellowship.",
            "repayment_clawback_conditions": "Aid terminated if student is dismissed for academic dishonesty, code of conduct violations, or unapproved withdrawal.",
            "rules_for_changing_university": "Non-transferable to other non-NYU institutions.",
            "rules_for_changing_major": "Students declare majors at the end of their second year; changing majors within NYUAD is fully permitted without loss of aid.",
            "extension_policy": "Financial aid covers 8 consecutive semesters (4 years); medical or approved academic leaves are reviewed by the Financial Aid Committee."
        },
        "official_sources_verified": [
            {
                "source_name": "New York University Abu Dhabi Financial Aid & Scholarships Portal",
                "source_url": "https://nyuad.nyu.edu/en/admissions/undergraduate/financial-aid.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "NYU Global Undergraduate Admissions",
                "source_url": "https://www.nyu.edu/admissions/undergraduate-admissions.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
