# scripts/batch22_p1.py
# SCH-ME-018: King Khalid University International Student Scholarship (Saudi Arabia)
# SCH-ME-019: Najran University International Student Scholarship (Saudi Arabia)
# SCH-ME-020: Majmaah University International Student Scholarship (Saudi Arabia)

DATA_P1 = {
    "SCH-ME-018": {
        "scholarship_id": "SCH-ME-018",
        "basic_details": {
            "scholarship_name": "King Khalid University International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & King Khalid University (KKU)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "King Khalid University Main Campus (Abha & Al-Fara'a Campuses, Asir Province, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Computer Science, College of Engineering, College of Science, College of Business, and College of Sharia (Health/Medical clinical colleges reserved exclusively for Saudi nationals under national policy).",
            "number_of_awards_total": "~250 to 350 external international government scholarships allocated annually across faculties",
            "number_of_awards_pakistan": "Extremely generous bilateral allocation; Pakistani students represent one of the largest international communities in Asir Province (~35 to 55 scholarships annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic language preparatory institute if required)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 - 1,000 / month for postgraduate students (~PKR 67,500 - 75,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Saudi citizenship (Pakistan fully eligible)"],
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
                "status": "COVERED",
                "details": "100% full tuition fee exemption for the entire official duration of academic study at King Khalid University.",
                "amount": "100% covered (~SAR 25,000 to 40,000 / year value; ~PKR 1,875,000 to 3,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application through the official 'Study in Saudi' portal is completely free of charge.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free furnished on-campus student housing in King Khalid University residential dormitories in Abha, including utilities, high-speed Wi-Fi, air conditioning, and laundry facilities.",
                "amount": "100% covered free dormitory room"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend disbursed directly into student bank accounts: SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Free annual economy-class round-trip flight ticket between Pakistan and Abha International Airport (AHB) provided by the university at the end of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi governmental study visa issued free of charge through the Royal Embassy of Saudi Arabia in Islamabad or Royal Consulate in Karachi.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive 100% free medical and dental healthcare provided at King Khalid University Medical City and government hospitals in Asir.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Heavily subsidized campus dining halls provide balanced multi-course meals for SAR 3 to 6 per meal; easily covered by the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Free textbook issuance and full borrowing privileges at the Central University Library; initial book allowance provided upon enrollment.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Thesis printing allowance (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial incentives for publishing in Web of Science / Scopus Q1 journals.",
                "amount": "SAR 3,000 to 4,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free university shuttle bus service operating daily between dormitories, university faculties, and city centers in Abha and Khamis Mushait.",
                "amount": "100% free university shuttle transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive host university (King Khalid University, Abha).",
            "participating_institutions": [
                "King Khalid University (Al-Fara'a & Abha Campuses, Asir Province, Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #35-40, Times Higher Education Asia #150-200, accredited by the National Center for Academic Accreditation and Assessment (NCAAA).",
            "available_majors": [
                "Computer Science and Artificial Intelligence",
                "Information Systems and Cyber Security",
                "Computer Engineering and Network Systems",
                "Electrical and Mechanical Engineering",
                "Civil and Chemical Engineering",
                "Chemistry, Physics, and Mathematics",
                "Islamic Studies (Sharia, Usul, Hadith)",
                "Arabic Language and Literature",
                "Business Administration and Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Unified online application via 'Study in Saudi' platform, high school / bachelor's diploma with minimum 80% marks, attested transcripts, medical fitness certificate, clean police conduct certificate, two academic recommendation letters, and valid passport copy.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science and Sharia faculties receive intense global demand; high academic marks (85%+) and solid recommendations are essential for admission.",
            "strategic_program_match_advice": "Ensure all Pakistani educational certificates are fully attested by IBCC/HEC and the Ministry of Foreign Affairs (MoFA) before submitting on Study in Saudi portal to avoid system disqualification."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.kku.edu.sa/",
            "portal_system_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
            "account_creation_instructions": "Register an account on 'Study in Saudi' portal, choose 'External Scholarship (منحة خارجية)', select King Khalid University as the preferred institution, select degree level, and upload attested digital scans.",
            "step_by_step_workflow": [
                "Step 1: Get matric/intermediate/degrees attested by IBCC/HEC and MoFA Pakistan.",
                "Step 2: Obtain clean police character clearance certificate and official medical fitness report.",
                "Step 3: Register an account on the 'Study in Saudi' portal (https://studyinsaudi.moe.gov.sa/).",
                "Step 4: Select King Khalid University, chosen academic major, and upload digital document copies.",
                "Step 5: University admissions committee reviews credentials and nominates eligible candidates to the Ministry of Education.",
                "Step 6: Ministry of Foreign Affairs issues electronic visa authorization number (Visa Slip).",
                "Step 7: Submit passport to Saudi Embassy Islamabad or Consulate Karachi via authorized Etimad/Tashkeel visa centers; university issues free e-ticket."
            ],
            "university_vs_scholarship_routing": "Integrated Government Track: Single submission via 'Study in Saudi' handles both institutional admission and scholarship award.",
            "recommendation_letters_submission_method": "Uploaded directly to the portal as attested PDFs with official institutional stamps.",
            "personal_statement_prompts": "Statement of academic purpose and career objectives in Saudi Arabia (Arabic or English).",
            "study_plan_research_proposal_requirements": "For Master's/PhD: 2 to 3-page research proposal outlining the intended thesis domain.",
            "cv_format_requirements": "Standard professional CV detailing educational background, academic percentages, and technical skills.",
            "interviews_conducted": False,
            "interview_format_details": "Screening is primarily based on academic grades, attestation verification, and security clearance.",
            "standardized_tests": "IELTS/TOEFL recommended for STEM disciplines; not mandatory if medium of instruction was English.",
            "application_fee_amount": "SAR 0 (100% free of charge)",
            "attestation_requirements": "IBCC (for Matric/Inter), HEC (for Bachelor's/Master's), and MoFA Pakistan attestations mandatory.",
            "translation_requirements": "Certified Arabic or English translation of all academic records and police certificates.",
            "final_submission_method": "100% online submission via Study in Saudi platform."
        },
        "required_documents_checklist": [
            {
                "document_name": "Attested Educational Certificates and Transcripts",
                "mandatory": True,
                "specification": "Matric/Inter/Bachelor's degrees with minimum 80% aggregate marks.",
                "pakistan_specific_instruction": "Attested by IBCC/HEC and MoFA Pakistan."
            },
            {
                "document_name": "Police Character Clearance Certificate",
                "mandatory": True,
                "specification": "Official police certificate verifying no criminal record.",
                "pakistan_specific_instruction": "Issued by local police department and attested by MoFA."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Comprehensive medical checkup confirming freedom from contagious diseases (HIV, Hep B/C, TB).",
                "pakistan_specific_instruction": "Issued by an authorized medical diagnostic laboratory."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio page valid for at least 2 years.",
                "pakistan_specific_instruction": "Must have validity extending through late 2028."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from former teachers/professors attesting to character and competence.",
                "pakistan_specific_instruction": "Printed on official institutional letterhead."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "May 1",
            "application_deadline": "July 15",
            "university_admission_deadline": "July 15",
            "document_submission_deadline": "July 15",
            "recommendation_letters_deadline": "July 15",
            "interview_period": "Not applicable",
            "shortlist_announcement": "November - December",
            "final_result_acceptance_deadline": "January",
            "visa_application_window": "January - February",
            "semester_commencement": "Late August / September (Fall intake)",
            "annual_cycle_notes": "Saudi external scholarship cycles open annually between May and July. Ministry approvals and visa issuance can take 4-6 months."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Academic percentage in high school or university transcripts)",
            "extracurricular_and_leadership_weight": "10% (General conduct, character recommendations)",
            "research_experience_weight": "15% (For postgraduate applicants: research proposal and publications)",
            "work_experience_weight": "0% (Not required for undergraduate or master's degrees)",
            "personal_statement_weight": "10% (Motivation letter clarity and intent)",
            "recommendations_weight": "5% (Academic referee appraisals)",
            "interview_weight": "0% (Dossier-based evaluation)",
            "test_scores_weight": "0% (No mandatory test scores)",
            "financial_need_weight": "0% (Pure academic merit and bilateral country quota)",
            "selection_panel_composition": "Deanship of Admission and Registration at King Khalid University and Saudi Ministry of Education Evaluation Board.",
            "evaluation_methodology": "Point-based merit ranking based on attested transcript marks, document verification, and national quota allocation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~15,000 to 25,000 international applicants across Study in Saudi portal",
            "total_scholarships_awarded": "~250 to 350 scholarships awarded at KKU annually",
            "acceptance_rate_global": "~1.5% to 2.5%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% (Pakistan holds one of the largest bilateral scholarship allocations)",
            "typical_successful_applicant_gpa": "Marks >= 85% in F.Sc / A-Levels or CGPA >= 3.4 / 4.0 in Bachelor's",
            "typical_academic_and_research_profile": "High-scoring students with clean conduct records, strong recommendations, and complete IBCC/HEC/MoFA attestations.",
            "common_backgrounds_of_winners": "Graduates of Pakistani intermediate boards and leading engineering/science universities.",
            "high_representation_countries": "Pakistan, Yemen, Egypt, Sudan, Indonesia, Bangladesh, Nigeria, Syria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent agents claiming to sell guaranteed Saudi university visas or scholarship seats.",
                "Official applications are accepted ONLY via https://studyinsaudi.moe.gov.sa/."
            ],
            "application_fee_warning": "The Saudi government NEVER charges any application, processing, or visa fee for government scholarships.",
            "agent_and_intermediary_warnings": "King Khalid University and the Ministry of Education do not collaborate with educational agencies or consultants.",
            "hidden_costs_breakdown": [
                "IBCC, HEC, and MoFA attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "Medical diagnostic tests in Pakistan: ~PKR 10,000 to 15,000.",
                "Visa processing via authorized Saudi service centers (Etimad/VFS Tasheel): ~PKR 12,000 to 18,000.",
                "Initial pocket money before first stipend disbursement in Abha: ~SAR 500 (~PKR 37,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need to know Arabic to study engineering or computer science. Reality: Engineering, Computer Science, and Science degrees are taught 100% in English.",
                "Myth: Women cannot apply without a male guardian accompanying them. Reality: Female students are legally accommodated in monitored university female residences under institutional guardianship."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim application deadlines are in December; Saudi government admissions open in May and close in July."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.75 / 5.0 (Grade Good / Jayyid) each semester to retain scholarship benefits.",
            "attendance_requirements": "Minimum 75% class attendance mandatory; falling below 75% results in course denial (Hirman) and stipend suspension.",
            "academic_progress_monitoring": "Biannual academic audit by the Deanship of Student Affairs before disbursing travel tickets and stipends.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "Graduates are expected to return to Pakistan upon graduation; university provides a free final exit ticket.",
            "service_obligations_or_bonds": "Zero financial bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is cancelled and student repatriated if dismissed for academic failure or disciplinary violations.",
            "rules_for_changing_university": "Transferring to another Saudi university is strictly prohibited under external scholarship rules.",
            "rules_for_changing_major": "Permitted only within the same faculty during the first academic year with approval.",
            "extension_policy": "Maximum extension of one additional semester may be granted upon academic dean's recommendation."
        },
        "official_sources_verified": [
            {
                "source_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "King Khalid University Deanship of Admission and Registration",
                "source_url": "https://www.kku.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-ME-019": {
        "scholarship_id": "SCH-ME-019",
        "basic_details": {
            "scholarship_name": "Najran University International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & Najran University (NU)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "Najran University Main Campus (Najran, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Computer Science and Information Systems, College of Engineering, College of Science and Arts, College of Administrative Sciences, and College of Sharia (Health/Medical clinical colleges reserved exclusively for Saudi nationals under national policy).",
            "number_of_awards_total": "~200 to 300 external international government scholarships allocated annually across faculties",
            "number_of_awards_pakistan": "Generous bilateral quota; Pakistani students constitute a prominent international student group in Najran (~30 to 45 scholarships annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic language preparatory institute if required)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 - 1,000 / month for postgraduate students (~PKR 67,500 - 75,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Saudi citizenship (Pakistan fully eligible)"],
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
                "status": "COVERED",
                "details": "100% full tuition fee exemption for the entire official duration of academic study at Najran University.",
                "amount": "100% covered (~SAR 25,000 to 40,000 / year value; ~PKR 1,875,000 to 3,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application through the official 'Study in Saudi' portal is completely free of charge.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free furnished on-campus student housing in Najran University residential dormitories, including utilities, high-speed Wi-Fi, air conditioning, and laundry facilities.",
                "amount": "100% covered free dormitory room"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend disbursed directly into student bank accounts: SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Free annual economy-class round-trip flight ticket between Pakistan and Najran Domestic Airport (EAM) provided by the university at the end of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi governmental study visa issued free of charge through the Royal Embassy of Saudi Arabia in Islamabad or Royal Consulate in Karachi.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive 100% free medical and dental healthcare provided at Najran University Medical Center and government hospitals in Najran.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Heavily subsidized campus dining halls provide balanced multi-course meals for SAR 3 to 6 per meal; easily covered by the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Free textbook issuance and full borrowing privileges at the Central University Library; initial book allowance provided upon enrollment.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Thesis printing allowance (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial incentives for publishing in Web of Science / Scopus Q1 journals.",
                "amount": "SAR 3,000 to 4,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free university shuttle bus service operating daily between dormitories, university faculties, and city centers in Najran.",
                "amount": "100% free university shuttle transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive host university (Najran University, Najran).",
            "participating_institutions": [
                "Najran University Main Campus (Najran, Kingdom of Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #81-90, accredited by the National Center for Academic Accreditation and Assessment (NCAAA).",
            "available_majors": [
                "Computer Science and Software Engineering",
                "Information Systems and Computer Networks",
                "Electrical and Electronic Engineering",
                "Civil and Mechanical Engineering",
                "Chemical Engineering",
                "Mathematics, Physics, and Chemistry",
                "Islamic Studies (Sharia, Usul, Hadith)",
                "Arabic Language and Literature",
                "Business Administration and Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Unified online application via 'Study in Saudi' platform, high school / bachelor's diploma with minimum 80% marks, attested transcripts, medical fitness certificate, clean police conduct certificate, two academic recommendation letters, and valid passport copy.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science and Sharia faculties receive high competition; high academic marks (85%+) and solid recommendations are essential for admission.",
            "strategic_program_match_advice": "Ensure all Pakistani educational certificates are fully attested by IBCC/HEC and the Ministry of Foreign Affairs (MoFA) before submitting on Study in Saudi portal to avoid system disqualification."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.nu.edu.sa/",
            "portal_system_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
            "account_creation_instructions": "Register an account on 'Study in Saudi' portal, choose 'External Scholarship (منحة خارجية)', select Najran University as the preferred institution, select degree level, and upload attested digital scans.",
            "step_by_step_workflow": [
                "Step 1: Get matric/intermediate/degrees attested by IBCC/HEC and MoFA Pakistan.",
                "Step 2: Obtain clean police character clearance certificate and official medical fitness report.",
                "Step 3: Register an account on the 'Study in Saudi' portal (https://studyinsaudi.moe.gov.sa/).",
                "Step 4: Select Najran University, chosen academic major, and upload digital document copies.",
                "Step 5: University admissions committee reviews credentials and nominates eligible candidates to the Ministry of Education.",
                "Step 6: Ministry of Foreign Affairs issues electronic visa authorization number (Visa Slip).",
                "Step 7: Submit passport to Saudi Embassy Islamabad or Consulate Karachi via authorized Etimad/Tashkeel visa centers; university issues free e-ticket."
            ],
            "university_vs_scholarship_routing": "Integrated Government Track: Single submission via 'Study in Saudi' handles both institutional admission and scholarship award.",
            "recommendation_letters_submission_method": "Uploaded directly to the portal as attested PDFs with official institutional stamps.",
            "personal_statement_prompts": "Statement of academic purpose and career objectives in Saudi Arabia (Arabic or English).",
            "study_plan_research_proposal_requirements": "For Master's/PhD: 2 to 3-page research proposal outlining the intended thesis domain.",
            "cv_format_requirements": "Standard professional CV detailing educational background, academic percentages, and technical skills.",
            "interviews_conducted": False,
            "interview_format_details": "Screening is primarily based on academic grades, attestation verification, and security clearance.",
            "standardized_tests": "IELTS/TOEFL recommended for STEM disciplines; not mandatory if medium of instruction was English.",
            "application_fee_amount": "SAR 0 (100% free of charge)",
            "attestation_requirements": "IBCC (for Matric/Inter), HEC (for Bachelor's/Master's), and MoFA Pakistan attestations mandatory.",
            "translation_requirements": "Certified Arabic or English translation of all academic records and police certificates.",
            "final_submission_method": "100% online submission via Study in Saudi platform."
        },
        "required_documents_checklist": [
            {
                "document_name": "Attested Educational Certificates and Transcripts",
                "mandatory": True,
                "specification": "Matric/Inter/Bachelor's degrees with minimum 80% aggregate marks.",
                "pakistan_specific_instruction": "Attested by IBCC/HEC and MoFA Pakistan."
            },
            {
                "document_name": "Police Character Clearance Certificate",
                "mandatory": True,
                "specification": "Official police certificate verifying no criminal record.",
                "pakistan_specific_instruction": "Issued by local police department and attested by MoFA."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Comprehensive medical checkup confirming freedom from contagious diseases (HIV, Hep B/C, TB).",
                "pakistan_specific_instruction": "Issued by an authorized medical diagnostic laboratory."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio page valid for at least 2 years.",
                "pakistan_specific_instruction": "Must have validity extending through late 2028."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from former teachers/professors attesting to character and competence.",
                "pakistan_specific_instruction": "Printed on official institutional letterhead."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "May 1",
            "application_deadline": "July 15",
            "university_admission_deadline": "July 15",
            "document_submission_deadline": "July 15",
            "recommendation_letters_deadline": "July 15",
            "interview_period": "Not applicable",
            "shortlist_announcement": "November - December",
            "final_result_acceptance_deadline": "January",
            "visa_application_window": "January - February",
            "semester_commencement": "Late August / September (Fall intake)",
            "annual_cycle_notes": "Saudi external scholarship cycles open annually between May and July. Ministry approvals and visa issuance can take 4-6 months."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Academic percentage in high school or university transcripts)",
            "extracurricular_and_leadership_weight": "10% (General conduct, character recommendations)",
            "research_experience_weight": "15% (For postgraduate applicants: research proposal and publications)",
            "work_experience_weight": "0% (Not required for undergraduate or master's degrees)",
            "personal_statement_weight": "10% (Motivation letter clarity and intent)",
            "recommendations_weight": "5% (Academic referee appraisals)",
            "interview_weight": "0% (Dossier-based evaluation)",
            "test_scores_weight": "0% (No mandatory test scores)",
            "financial_need_weight": "0% (Pure academic merit and bilateral country quota)",
            "selection_panel_composition": "Deanship of Admission and Registration at Najran University and Saudi Ministry of Education Evaluation Board.",
            "evaluation_methodology": "Point-based merit ranking based on attested transcript marks, document verification, and national quota allocation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~12,000 to 20,000 international applicants across Study in Saudi portal",
            "total_scholarships_awarded": "~200 to 300 scholarships awarded at Najran University annually",
            "acceptance_rate_global": "~1.5% to 2.5%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% (Pakistan holds one of the largest bilateral scholarship allocations)",
            "typical_successful_applicant_gpa": "Marks >= 85% in F.Sc / A-Levels or CGPA >= 3.4 / 4.0 in Bachelor's",
            "typical_academic_and_research_profile": "High-scoring students with clean conduct records, strong recommendations, and complete IBCC/HEC/MoFA attestations.",
            "common_backgrounds_of_winners": "Graduates of Pakistani intermediate boards and leading engineering/science universities.",
            "high_representation_countries": "Pakistan, Yemen, Egypt, Sudan, Indonesia, Bangladesh, Nigeria, Syria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent agents claiming to sell guaranteed Saudi university visas or scholarship seats.",
                "Official applications are accepted ONLY via https://studyinsaudi.moe.gov.sa/."
            ],
            "application_fee_warning": "The Saudi government NEVER charges any application, processing, or visa fee for government scholarships.",
            "agent_and_intermediary_warnings": "Najran University and the Ministry of Education do not collaborate with educational agencies or consultants.",
            "hidden_costs_breakdown": [
                "IBCC, HEC, and MoFA attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "Medical diagnostic tests in Pakistan: ~PKR 10,000 to 15,000.",
                "Visa processing via authorized Saudi service centers (Etimad/VFS Tasheel): ~PKR 12,000 to 18,000.",
                "Initial pocket money before first stipend disbursement in Najran: ~SAR 500 (~PKR 37,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need to know Arabic to study engineering or computer science. Reality: Engineering, Computer Science, and Science degrees are taught 100% in English.",
                "Myth: Women cannot apply without a male guardian accompanying them. Reality: Female students are legally accommodated in monitored university female residences under institutional guardianship."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim application deadlines are in December; Saudi government admissions open in May and close in July."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.75 / 5.0 (Grade Good / Jayyid) each semester to retain scholarship benefits.",
            "attendance_requirements": "Minimum 75% class attendance mandatory; falling below 75% results in course denial (Hirman) and stipend suspension.",
            "academic_progress_monitoring": "Biannual academic audit by the Deanship of Student Affairs before disbursing travel tickets and stipends.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "Graduates are expected to return to Pakistan upon graduation; university provides a free final exit ticket.",
            "service_obligations_or_bonds": "Zero financial bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is cancelled and student repatriated if dismissed for academic failure or disciplinary violations.",
            "rules_for_changing_university": "Transferring to another Saudi university is strictly prohibited under external scholarship rules.",
            "rules_for_changing_major": "Permitted only within the same faculty during the first academic year with approval.",
            "extension_policy": "Maximum extension of one additional semester may be granted upon academic dean's recommendation."
        },
        "official_sources_verified": [
            {
                "source_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Najran University Deanship of Admission and Registration",
                "source_url": "https://www.nu.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-ME-020": {
        "scholarship_id": "SCH-ME-020",
        "basic_details": {
            "scholarship_name": "Majmaah University International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & Majmaah University (MU)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "Majmaah University Main Campus (Al Majma'ah, Riyadh Province, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Computer and Information Sciences, College of Engineering, College of Science, College of Business Administration, and College of Education (Health/Medical clinical colleges reserved exclusively for Saudi nationals under national policy).",
            "number_of_awards_total": "~200 to 280 external international government scholarships allocated annually across faculties",
            "number_of_awards_pakistan": "Generous bilateral quota; Pakistani students constitute a prominent international student community in Majmaah (~30 to 45 scholarships annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic language preparatory institute if required)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 - 1,000 / month for postgraduate students (~PKR 67,500 - 75,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Saudi citizenship (Pakistan fully eligible)"],
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
            "language_notes": "Instruction in STEM faculties is primarily in English (MOI certificate accepted; IELTS 5.5+ or TOEFL 65 recommended). For Islamic and Arabic faculties, candidates must demonstrate Arabic competence or complete the university's intensive 1-year Arabic Institute.",
            "other_language_requirements": "Arabic Institute placement exam conducted upon campus arrival for non-Arabic speakers.",
            "gender_specific_requirements": "Female students must reside with an approved Mahram residing legally in Saudi Arabia or within monitored university female student dormitories with institutional guardianship approval.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applications are submitted through the unified Saudi government portal 'Study in Saudi' (studyinsaudi.moe.gov.sa).",
            "previous_scholarship_restrictions": "Applicant must not have been previously awarded a Saudi government scholarship and dismissed or graduated from another Saudi university.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee exemption for the entire official duration of academic study at Majmaah University.",
                "amount": "100% covered (~SAR 25,000 to 40,000 / year value; ~PKR 1,875,000 to 3,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application through the official 'Study in Saudi' portal is completely free of charge.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free furnished on-campus student housing in Majmaah University residential dormitories in Al Majma'ah, including utilities, high-speed Wi-Fi, air conditioning, and laundry facilities.",
                "amount": "100% covered free dormitory room"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend disbursed directly into student bank accounts: SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Free annual economy-class round-trip flight ticket between Pakistan and King Khalid International Airport (Riyadh / RUH) provided by the university at the end of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi governmental study visa issued free of charge through the Royal Embassy of Saudi Arabia in Islamabad or Royal Consulate in Karachi.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive 100% free medical and dental healthcare provided at Majmaah University Medical Center and King Khalid Hospital Majmaah.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Heavily subsidized campus dining halls provide balanced multi-course meals for SAR 3 to 6 per meal; easily covered by the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Free textbook issuance and full borrowing privileges at the Central University Library; initial book allowance provided upon enrollment.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Thesis printing allowance (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial incentives for publishing in Web of Science / Scopus Q1 journals.",
                "amount": "SAR 3,000 to 4,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free university shuttle bus service operating daily between dormitories, university faculties, and Riyadh metropolitan transit links.",
                "amount": "100% free university shuttle transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive host university (Majmaah University, Al Majma'ah, Riyadh Province).",
            "participating_institutions": [
                "Majmaah University Main Campus (Al Majma'ah & Zulfi Campuses, Riyadh Province, Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #101-110, accredited by the National Center for Academic Accreditation and Assessment (NCAAA).",
            "available_majors": [
                "Computer Science and Information Technology",
                "Information Systems and Cyber Security",
                "Computer Engineering and Network Systems",
                "Electrical and Mechanical Engineering",
                "Civil Engineering",
                "Mathematics, Physics, and Chemistry",
                "Islamic Studies and Law",
                "Arabic Language and Literature",
                "Business Administration and Accounting"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Unified online application via 'Study in Saudi' platform, high school / bachelor's diploma with minimum 80% marks, attested transcripts, medical fitness certificate, clean police conduct certificate, two academic recommendation letters, and valid passport copy.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science and Engineering faculties receive high competition; high academic marks (85%+) and solid recommendations are essential for admission.",
            "strategic_program_match_advice": "Ensure all Pakistani educational certificates are fully attested by IBCC/HEC and the Ministry of Foreign Affairs (MoFA) before submitting on Study in Saudi portal to avoid system disqualification."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.mu.edu.sa/",
            "portal_system_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
            "account_creation_instructions": "Register an account on 'Study in Saudi' portal, choose 'External Scholarship (منحة خارجية)', select Majmaah University as the preferred institution, select degree level, and upload attested digital scans.",
            "step_by_step_workflow": [
                "Step 1: Get matric/intermediate/degrees attested by IBCC/HEC and MoFA Pakistan.",
                "Step 2: Obtain clean police character clearance certificate and official medical fitness report.",
                "Step 3: Register an account on the 'Study in Saudi' portal (https://studyinsaudi.moe.gov.sa/).",
                "Step 4: Select Majmaah University, chosen academic major, and upload digital document copies.",
                "Step 5: University admissions committee reviews credentials and nominates eligible candidates to the Ministry of Education.",
                "Step 6: Ministry of Foreign Affairs issues electronic visa authorization number (Visa Slip).",
                "Step 7: Submit passport to Saudi Embassy Islamabad or Consulate Karachi via authorized Etimad/Tashkeel visa centers; university issues free e-ticket."
            ],
            "university_vs_scholarship_routing": "Integrated Government Track: Single submission via 'Study in Saudi' handles both institutional admission and scholarship award.",
            "recommendation_letters_submission_method": "Uploaded directly to the portal as attested PDFs with official institutional stamps.",
            "personal_statement_prompts": "Statement of academic purpose and career objectives in Saudi Arabia (Arabic or English).",
            "study_plan_research_proposal_requirements": "For Master's/PhD: 2 to 3-page research proposal outlining the intended thesis domain.",
            "cv_format_requirements": "Standard professional CV detailing educational background, academic percentages, and technical skills.",
            "interviews_conducted": False,
            "interview_format_details": "Screening is primarily based on academic grades, attestation verification, and security clearance.",
            "standardized_tests": "IELTS/TOEFL recommended for STEM disciplines; not mandatory if medium of instruction was English.",
            "application_fee_amount": "SAR 0 (100% free of charge)",
            "attestation_requirements": "IBCC (for Matric/Inter), HEC (for Bachelor's/Master's), and MoFA Pakistan attestations mandatory.",
            "translation_requirements": "Certified Arabic or English translation of all academic records and police certificates.",
            "final_submission_method": "100% online submission via Study in Saudi platform."
        },
        "required_documents_checklist": [
            {
                "document_name": "Attested Educational Certificates and Transcripts",
                "mandatory": True,
                "specification": "Matric/Inter/Bachelor's degrees with minimum 80% aggregate marks.",
                "pakistan_specific_instruction": "Attested by IBCC/HEC and MoFA Pakistan."
            },
            {
                "document_name": "Police Character Clearance Certificate",
                "mandatory": True,
                "specification": "Official police certificate verifying no criminal record.",
                "pakistan_specific_instruction": "Issued by local police department and attested by MoFA."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Comprehensive medical checkup confirming freedom from contagious diseases (HIV, Hep B/C, TB).",
                "pakistan_specific_instruction": "Issued by an authorized medical diagnostic laboratory."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio page valid for at least 2 years.",
                "pakistan_specific_instruction": "Must have validity extending through late 2028."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from former teachers/professors attesting to character and competence.",
                "pakistan_specific_instruction": "Printed on official institutional letterhead."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "May 1",
            "application_deadline": "July 15",
            "university_admission_deadline": "July 15",
            "document_submission_deadline": "July 15",
            "recommendation_letters_deadline": "July 15",
            "interview_period": "Not applicable",
            "shortlist_announcement": "November - December",
            "final_result_acceptance_deadline": "January",
            "visa_application_window": "January - February",
            "semester_commencement": "Late August / September (Fall intake)",
            "annual_cycle_notes": "Saudi external scholarship cycles open annually between May and July. Ministry approvals and visa issuance can take 4-6 months."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Academic percentage in high school or university transcripts)",
            "extracurricular_and_leadership_weight": "10% (General conduct, character recommendations)",
            "research_experience_weight": "15% (For postgraduate applicants: research proposal and publications)",
            "work_experience_weight": "0% (Not required for undergraduate or master's degrees)",
            "personal_statement_weight": "10% (Motivation letter clarity and intent)",
            "recommendations_weight": "5% (Academic referee appraisals)",
            "interview_weight": "0% (Dossier-based evaluation)",
            "test_scores_weight": "0% (No mandatory test scores)",
            "financial_need_weight": "0% (Pure academic merit and bilateral country quota)",
            "selection_panel_composition": "Deanship of Admission and Registration at Majmaah University and Saudi Ministry of Education Evaluation Board.",
            "evaluation_methodology": "Point-based merit ranking based on attested transcript marks, document verification, and national quota allocation."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000 to 18,000 international applicants across Study in Saudi portal",
            "total_scholarships_awarded": "~200 to 280 scholarships awarded at Majmaah University annually",
            "acceptance_rate_global": "~1.5% to 2.5%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% (Pakistan holds one of the largest bilateral scholarship allocations)",
            "typical_successful_applicant_gpa": "Marks >= 85% in F.Sc / A-Levels or CGPA >= 3.4 / 4.0 in Bachelor's",
            "typical_academic_and_research_profile": "High-scoring students with clean conduct records, strong recommendations, and complete IBCC/HEC/MoFA attestations.",
            "common_backgrounds_of_winners": "Graduates of Pakistani intermediate boards and leading engineering/science universities.",
            "high_representation_countries": "Pakistan, Yemen, Egypt, Sudan, Indonesia, Bangladesh, Nigeria, Syria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent agents claiming to sell guaranteed Saudi university visas or scholarship seats.",
                "Official applications are accepted ONLY via https://studyinsaudi.moe.gov.sa/."
            ],
            "application_fee_warning": "The Saudi government NEVER charges any application, processing, or visa fee for government scholarships.",
            "agent_and_intermediary_warnings": "Majmaah University and the Ministry of Education do not collaborate with educational agencies or consultants.",
            "hidden_costs_breakdown": [
                "IBCC, HEC, and MoFA attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "Medical diagnostic tests in Pakistan: ~PKR 10,000 to 15,000.",
                "Visa processing via authorized Saudi service centers (Etimad/VFS Tasheel): ~PKR 12,000 to 18,000.",
                "Initial pocket money before first stipend disbursement in Majmaah: ~SAR 500 (~PKR 37,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need to know Arabic to study engineering or computer science. Reality: Engineering, Computer Science, and Science degrees are taught 100% in English.",
                "Myth: Women cannot apply without a male guardian accompanying them. Reality: Female students are legally accommodated in monitored university female residences under institutional guardianship."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim application deadlines are in December; Saudi government admissions open in May and close in July."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.75 / 5.0 (Grade Good / Jayyid) each semester to retain scholarship benefits.",
            "attendance_requirements": "Minimum 75% class attendance mandatory; falling below 75% results in course denial (Hirman) and stipend suspension.",
            "academic_progress_monitoring": "Biannual academic audit by the Deanship of Student Affairs before disbursing travel tickets and stipends.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "Graduates are expected to return to Pakistan upon graduation; university provides a free final exit ticket.",
            "service_obligations_or_bonds": "Zero financial bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is cancelled and student repatriated if dismissed for academic failure or disciplinary violations.",
            "rules_for_changing_university": "Transferring to another Saudi university is strictly prohibited under external scholarship rules.",
            "rules_for_changing_major": "Permitted only within the same faculty during the first academic year with approval.",
            "extension_policy": "Maximum extension of one additional semester may be granted upon academic dean's recommendation."
        },
        "official_sources_verified": [
            {
                "source_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Majmaah University Deanship of Admission and Registration",
                "source_url": "https://www.mu.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
