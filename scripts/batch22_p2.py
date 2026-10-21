# scripts/batch22_p2.py
# SCH-ME-021: University of Ha'il International Student Scholarship (Saudi Arabia)
# SCH-ME-022: University of Tabuk International Student Scholarship (Saudi Arabia)
# SCH-ME-032: Zayed University Graduate Merit Scholarships (UAE)

DATA_P2 = {
    "SCH-ME-021": {
        "scholarship_id": "SCH-ME-021",
        "basic_details": {
            "scholarship_name": "University of Ha'il International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & University of Ha'il (UOH)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "University of Ha'il Main Campus (Ha'il Province, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Computer Science and Engineering, College of Engineering, College of Science, College of Business Administration, and College of Arts and Education (clinical medical colleges restricted to Saudi citizens).",
            "number_of_awards_total": "~200 to 300 international government scholarships allocated annually across faculties",
            "number_of_awards_pakistan": "Substantial bilateral quota; Pakistani scholars and students represent one of the leading expatriate groups in Ha'il (~30 to 50 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's; 3 to 4 years for PhD (plus 1-year Arabic language foundation if required)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 - 1,000 / month for postgraduate students (~PKR 67,500 - 75,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International candidates holding non-Saudi nationality (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate applicants must be between 17 and 25 years old; Master's applicants under 30; PhD applicants under 35 years of age per Saudi Ministry of Education bylaws.",
            "academic_qualifications": "Intermediate / HSSC (Pre-Engineering, ICS, Pre-Medical) or A-Levels for Bachelor's (minimum 80% aggregate or Grade B); recognized 16-year Bachelor's degree for Master's; 18-year Master's degree for PhD from an HEC-recognized university with minimum CGPA 3.00 / 4.00 or Very Good standing.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Evaluated on Saudi 5.0 scale (equivalent to minimum 3.75 / 5.00).",
            "subject_background_prerequisites": "Pre-Engineering or ICS for Computer Science and Engineering tracks; relevant scientific degree for postgraduate entry.",
            "current_education_status": "Candidates must have completed their qualifying degree and hold official certificates/transcripts at time of application.",
            "graduation_year_restrictions": "High school graduation certificate must not be older than 3 to 5 years from application date.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; research output and academic publications strongly valued for postgraduate research tracks.",
            "english_test_required": False,
            "ielts_minimum": 5.5,
            "toefl_minimum": 65,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Instruction in College of Computer Science & Engineering and College of Science is delivered in English (MOI certificate accepted; IELTS 5.5+ recommended). Humanities/Islamic studies delivered in Arabic.",
            "other_language_requirements": "Preparatory Arabic language program offered for non-Arabic speakers enrolling in Arabic-taught departments.",
            "gender_specific_requirements": "Female students accommodated in supervised university female residences under institutional care in accordance with Saudi higher education guidelines.",
            "financial_need_required": False,
            "special_eligibility_categories": "Processed via official unified portal 'Study in Saudi' (studyinsaudi.moe.gov.sa).",
            "previous_scholarship_restrictions": "Candidate must not have previously received a scholarship from another Saudi university or been dismissed.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition waiver across the entire approved program duration at University of Ha'il.",
                "amount": "100% covered (~SAR 25,000 to 38,000 / year value; ~PKR 1,875,000 to 2,850,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Online application through Study in Saudi portal is completely free.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free furnished student dormitory housing on UOH campus with high-speed internet, air conditioning, and laundry facilities.",
                "amount": "100% covered free university housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend paid into student bank account: SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 to 1,000 / month for postgraduate students (~PKR 67,500 to 75,000 / month).",
                "amount": "SAR 840 to 1,000 / month (~PKR 63,000 to 75,000 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Annual round-trip economy airfare between Pakistan and Ha'il International Airport (HAS) provided at the conclusion of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi official educational study visa issued free of charge through Saudi diplomatic missions in Islamabad or Karachi.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Full comprehensive medical and emergency healthcare provided at University of Ha'il Medical Clinics and King Khalid Hospital Ha'il.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "State-subsidized university cafeteria meals costing SAR 3 to 6 per meal, funded comfortably from the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Initial arrival preparation allowance (~SAR 1,700 / ~PKR 127,500) plus full access to university libraries and digital academic repositories.",
                "amount": "SAR 1,700 arrival preparation allowance"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Postgraduate thesis printing grant (SAR 3,000 for Master's, SAR 4,000 for PhD) and financial reward schemes for Scopus/WoS journal publications.",
                "amount": "SAR 3,000 to 4,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free daily campus bus transit network connecting student housing, academic complexes, and central Ha'il amenities.",
                "amount": "100% free campus shuttle transport"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive host university (University of Ha'il, Ha'il).",
            "participating_institutions": [
                "University of Ha'il Main Campus (Ha'il Province, Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #61-70, Times Higher Education World University Rankings #601-800, nationally accredited by NCAAA.",
            "available_majors": [
                "Computer Science and Software Engineering",
                "Electrical and Electronics Engineering",
                "Mechanical and Industrial Engineering",
                "Civil and Environmental Engineering",
                "Chemical Engineering",
                "Mathematics, Physics, and Chemistry",
                "Business Administration and Management Information Systems",
                "Islamic Studies and Sharia",
                "Arabic Language and Literature"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Online submission via 'Study in Saudi' portal, high school or bachelor's diploma with minimum 80% aggregate, attested transcripts, medical fitness clearance, police certificate, two recommendation letters, and valid passport.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "College of Computer Science and Engineering is most competitive with highest cutoffs; basic sciences and humanities have relatively higher acceptance rates.",
            "strategic_program_match_advice": "Ensure educational documents are verified by IBCC/HEC and MoFA Pakistan prior to uploading to avoid rejection during electronic verification."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.uoh.edu.sa/",
            "portal_system_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
            "account_creation_instructions": "Create an applicant profile on Study in Saudi portal, select 'External Scholarship (منحة خارجية)', choose University of Ha'il, pick preferred academic degree, and upload attested document scans.",
            "step_by_step_workflow": [
                "Step 1: Attest academic certificates and transcripts through IBCC/HEC and MoFA Pakistan.",
                "Step 2: Obtain certified police character clearance and comprehensive medical fitness report.",
                "Step 3: Register on 'Study in Saudi' portal (https://studyinsaudi.moe.gov.sa/).",
                "Step 4: Select University of Ha'il and chosen academic program; upload scanned credentials.",
                "Step 5: Deanship of Admission and Registration evaluates applications and forwards eligible candidates to Ministry of Education.",
                "Step 6: Saudi Ministry of Foreign Affairs issues electronic visa authorization number (Visa Slip).",
                "Step 7: Submit visa application through Saudi visa centers in Pakistan; university arranges flight e-ticket to Ha'il."
            ],
            "university_vs_scholarship_routing": "Integrated Government Track: A single application on Study in Saudi portal secures both academic admission and full government scholarship.",
            "recommendation_letters_submission_method": "Uploaded as signed and stamped PDF documents from academic professors.",
            "personal_statement_prompts": "Statement of purpose outlining academic motivations and study objectives in Saudi Arabia.",
            "study_plan_research_proposal_requirements": "For Master's/PhD: 2 to 3-page research proposal detailing target problem, methodology, and relevance.",
            "cv_format_requirements": "Chronological academic CV highlighting education, academic grades, projects, and technical skills.",
            "interviews_conducted": False,
            "interview_format_details": "Evaluation is entirely dossier-based assessing academic merit, attested credentials, and government clearance.",
            "standardized_tests": "IELTS/TOEFL recommended for STEM disciplines; English medium certificate accepted.",
            "application_fee_amount": "SAR 0 (100% free of charge)",
            "attestation_requirements": "IBCC (Intermediate), HEC (Bachelor's/Master's), and MoFA Pakistan attestations mandatory.",
            "translation_requirements": "Certified English or Arabic translation of all educational documents.",
            "final_submission_method": "100% digital submission via Study in Saudi platform."
        },
        "required_documents_checklist": [
            {
                "document_name": "Attested Educational Certificates and Transcripts",
                "mandatory": True,
                "specification": "Matric/Intermediate/Bachelor's degrees with minimum 80% aggregate marks.",
                "pakistan_specific_instruction": "Attested by IBCC/HEC and MoFA Pakistan."
            },
            {
                "document_name": "Police Character Clearance Certificate",
                "mandatory": True,
                "specification": "Official police record confirming clean conduct without criminal background.",
                "pakistan_specific_instruction": "Issued by local police and attested by MoFA Pakistan."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Complete medical exam verifying freedom from infectious illnesses (HIV, Hepatitis B/C, Tuberculosis).",
                "pakistan_specific_instruction": "Issued by an accredited medical diagnostic laboratory."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport personal information page valid for at least 2 years.",
                "pakistan_specific_instruction": "Validity extending minimum through late 2028."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from former teachers or academic advisors attesting to character and scholastic ability.",
                "pakistan_specific_instruction": "Printed on official institutional letterhead with contact details."
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
            "annual_cycle_notes": "Admissions open once annually during the summer cycle via Study in Saudi. Government approvals take several months."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Cumulative grades in qualifying secondary or university transcripts)",
            "extracurricular_and_leadership_weight": "10% (Character conduct and leadership potential)",
            "research_experience_weight": "15% (For postgraduate applicants: research proposal and publications)",
            "work_experience_weight": "0% (Not required)",
            "personal_statement_weight": "10% (Statement of purpose quality)",
            "recommendations_weight": "5% (Academic referee recommendations)",
            "interview_weight": "0% (No interview required)",
            "test_scores_weight": "0% (Standardized tests optional)",
            "financial_need_weight": "0% (Merit and bilateral country allocation only)",
            "selection_panel_composition": "Deanship of Admission and Registration at University of Ha'il and Saudi Ministry of Education Review Board.",
            "evaluation_methodology": "Competitive ranking based on certified transcript marks, document verification, and national bilateral quotas."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~12,000 to 20,000 international applicants across Study in Saudi portal",
            "total_scholarships_awarded": "~200 to 300 scholarships awarded annually at UOH",
            "acceptance_rate_global": "~1.5% to 2.5%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% (Pakistan is prioritized under bilateral educational ties)",
            "typical_successful_applicant_gpa": "Marks >= 85% in F.Sc / A-Levels or CGPA >= 3.4 / 4.0 in Bachelor's",
            "typical_academic_and_research_profile": "Top-tier academic marks, spotless disciplinary record, and verified IBCC/HEC/MoFA attestations.",
            "common_backgrounds_of_winners": "Graduates of Pakistani intermediate boards and recognized public/private engineering institutions.",
            "high_representation_countries": "Pakistan, Yemen, Egypt, Sudan, Jordan, Bangladesh, Indonesia, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed admissions or scholarship visas to University of Ha'il.",
                "Applications are exclusively processed through https://studyinsaudi.moe.gov.sa/."
            ],
            "application_fee_warning": "The Saudi government and University of Ha'il do NOT charge any application or visa fee.",
            "agent_and_intermediary_warnings": "University of Ha'il does not authorize any recruiting agencies or third-party brokers.",
            "hidden_costs_breakdown": [
                "IBCC, HEC, and MoFA attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "Medical diagnostics in Pakistan: ~PKR 10,000 to 15,000.",
                "Visa processing via Etimad/VFS Tasheel: ~PKR 12,000 to 18,000.",
                "Initial settling cash prior to first stipend payment: ~SAR 500 (~PKR 37,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: Ha'il is remote with poor infrastructure. Reality: Ha'il features modern campuses, high-speed rail connectivity to Riyadh, and comprehensive facilities.",
                "Myth: Arabic fluency is mandatory for computing or engineering. Reality: All STEM coursework and examinations are conducted in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party websites post outdated deadlines in winter; official portal opens in May and closes in July."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of at least 2.75 / 5.0 (Grade Good) each semester to retain full scholarship privileges.",
            "attendance_requirements": "Minimum 75% lecture and laboratory attendance required; lower attendance incurs course denial and stipend suspension.",
            "academic_progress_monitoring": "Semester-end academic audit conducted prior to ticket issuance and stipend continuation.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited by Saudi student visa regulations.",
            "home_country_return_obligation": "Graduates are expected to return to Pakistan upon completion; university issues free one-way exit flight ticket.",
            "service_obligations_or_bonds": "Zero service bond or post-graduation financial repayment.",
            "repayment_clawback_conditions": "Scholarship is terminated and student repatriated if dismissed for academic failure or disciplinary misconduct.",
            "rules_for_changing_university": "Inter-university transfer between Saudi universities is prohibited for external scholarship holders.",
            "rules_for_changing_major": "Permitted only within the same academic college during the first year subject to dean approval.",
            "extension_policy": "Maximum extension of one additional semester may be approved upon academic department recommendation."
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
                "source_name": "University of Ha'il Deanship of Admission and Registration",
                "source_url": "https://www.uoh.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-ME-022": {
        "scholarship_id": "SCH-ME-022",
        "basic_details": {
            "scholarship_name": "University of Tabuk International Student Scholarship (Kingdom of Saudi Arabia)",
            "offering_entity": "Ministry of Education of Saudi Arabia & University of Tabuk (UT)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "University of Tabuk Main Campus (Tabuk Region, Kingdom of Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Science (MSc)"],
            "major_restrictions": "Faculty of Computers and Information Technology, Faculty of Engineering, Faculty of Science, and Faculty of Business Administration (health/medical tracks reserved exclusively for Saudi citizens under national policy).",
            "number_of_awards_total": "~180 to 250 international government scholarships awarded annually",
            "number_of_awards_pakistan": "Extensive quota allocation; Pakistani applicants represent a key segment of Tabuk's international student cohort (~25 to 40 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor's; 2 years for Master's (plus 1-year Arabic language preparatory institute if required)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 / month for postgraduate students (~PKR 67,500 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International candidates holding non-Saudi nationality (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 30,
            "age_limit_notes": "Undergraduate applicants must be between 17 and 25 years old; Master's applicants under 30 years of age per Saudi Ministry of Education bylaws.",
            "academic_qualifications": "Intermediate / HSSC (Pre-Engineering, ICS, Pre-Medical) or A-Levels for Bachelor's (minimum 80% aggregate or Grade B); recognized 16-year Bachelor's degree for Master's from an HEC-recognized university with minimum CGPA 3.00 / 4.00 or Very Good standing.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Evaluated on Saudi 5.0 scale (equivalent to minimum 3.75 / 5.00).",
            "subject_background_prerequisites": "Pre-Engineering or ICS for Computer Science and Engineering tracks; relevant scientific degree for postgraduate entry.",
            "current_education_status": "Candidates must have completed their qualifying degree and hold official certificates/transcripts at time of application.",
            "graduation_year_restrictions": "High school graduation certificate must not be older than 3 to 5 years from application date.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory for undergraduate or master's admissions.",
            "english_test_required": False,
            "ielts_minimum": 5.5,
            "toefl_minimum": 65,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Instruction in Faculty of Computers & IT and Faculty of Engineering is conducted in English (MOI certificate accepted; IELTS 5.5+ recommended). Humanities/Islamic courses delivered in Arabic.",
            "other_language_requirements": "Preparatory Arabic language program offered for non-Arabic speakers enrolling in Arabic-taught programs.",
            "gender_specific_requirements": "Female students accommodated in supervised university female residences under institutional care in accordance with Saudi higher education guidelines.",
            "financial_need_required": False,
            "special_eligibility_categories": "Processed via official unified portal 'Study in Saudi' (studyinsaudi.moe.gov.sa).",
            "previous_scholarship_restrictions": "Candidate must not have previously received a scholarship from another Saudi university or been dismissed.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition waiver across the entire official program duration at University of Tabuk.",
                "amount": "100% covered (~SAR 25,000 to 36,000 / year value; ~PKR 1,875,000 to 2,700,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Online application through Study in Saudi portal is completely free.",
                "amount": "SAR 0 (100% free)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free furnished student dormitory housing on UT campus with utilities, high-speed Wi-Fi, and climate control.",
                "amount": "100% covered free university housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend paid into student bank account: SAR 840 / month for undergraduate students (~PKR 63,000 / month); SAR 900 / month for postgraduate students (~PKR 67,500 / month).",
                "amount": "SAR 840 to 900 / month (~PKR 63,000 to 67,500 / mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Annual round-trip economy airfare between Pakistan and Tabuk Regional Airport (TUU) provided at the conclusion of each academic year.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi official educational study visa issued free of charge through Saudi diplomatic missions in Islamabad or Karachi.",
                "amount": "100% free / covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Full comprehensive medical healthcare provided at University of Tabuk Health Center and King Fahd Hospital Tabuk.",
                "amount": "100% covered free healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "State-subsidized university cafeteria meals costing SAR 3 to 6 per meal, funded comfortably from the monthly stipend.",
                "amount": "Subsidized meals (~SAR 5 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "One-time initial arrival settling grant (~SAR 1,700 / ~PKR 127,500) plus book shipping allowance (~SAR 1,000) upon graduation.",
                "amount": "SAR 1,700 arrival settling grant"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Master thesis research grant (SAR 3,000) and publication rewards for Scopus-indexed research articles.",
                "amount": "SAR 3,000 thesis grant"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free daily university shuttle bus transportation between residential halls, campus colleges, and Tabuk city center.",
                "amount": "100% free campus shuttle transport"
            },
            "total_estimated_value_usd_per_year": 15500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive host university (University of Tabuk, Tabuk).",
            "participating_institutions": [
                "University of Tabuk Main Campus (Tabuk Region, Saudi Arabia)"
            ],
            "university_rankings_scope": "QS Arab Region #71-80, Times Higher Education World University Rankings #801-1000, accredited by NCAAA.",
            "available_majors": [
                "Computer Science",
                "Information Technology",
                "Software Engineering",
                "Electrical Engineering",
                "Civil Engineering",
                "Mechanical Engineering",
                "Renewable Energy Systems",
                "Physics, Mathematics, and Chemistry",
                "Business Administration and Management",
                "Islamic Studies and Arabic Language"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 to 5 years; Master's: 2 years",
            "admission_requirements_summary": "Unified online application via 'Study in Saudi' portal, high school or bachelor's diploma with minimum 80% marks, attested transcripts, medical fitness clearance, police certificate, two recommendation letters, and valid passport.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science and Renewable Energy/Engineering programs have high selectivity; basic sciences have moderately accessible admission bars.",
            "strategic_program_match_advice": "Tabuk is a key higher education hub adjacent to NEOM megacity development; engineering and computer science fields enjoy strategic research alignment."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://studyinsaudi.moe.gov.sa/ & https://www.ut.edu.sa/",
            "portal_system_name": "Study in Saudi Official Portal (Ministry of Education, KSA)",
            "account_creation_instructions": "Register an applicant profile on Study in Saudi portal, select 'External Scholarship (منحة خارجية)', choose University of Tabuk, pick degree level, and upload attested digital scans.",
            "step_by_step_workflow": [
                "Step 1: Attest academic certificates and transcripts through IBCC/HEC and MoFA Pakistan.",
                "Step 2: Obtain certified police character clearance and comprehensive medical fitness report.",
                "Step 3: Register on 'Study in Saudi' portal (https://studyinsaudi.moe.gov.sa/).",
                "Step 4: Select University of Tabuk and chosen academic program; upload scanned credentials.",
                "Step 5: Deanship of Admission and Registration evaluates applications and forwards candidates to Ministry of Education.",
                "Step 6: Saudi Ministry of Foreign Affairs issues electronic visa authorization number (Visa Slip).",
                "Step 7: Submit visa application through Saudi visa centers in Pakistan; university arranges flight e-ticket to Tabuk."
            ],
            "university_vs_scholarship_routing": "Integrated Government Track: A single application on Study in Saudi portal secures both academic admission and full government scholarship.",
            "recommendation_letters_submission_method": "Uploaded as signed and stamped PDF documents from academic professors.",
            "personal_statement_prompts": "Statement of purpose outlining academic motivations and study objectives in Saudi Arabia.",
            "study_plan_research_proposal_requirements": "For Master's: 2-page research outline describing target research field.",
            "cv_format_requirements": "Standard academic CV highlighting education, academic grades, projects, and technical skills.",
            "interviews_conducted": False,
            "interview_format_details": "Evaluation is entirely dossier-based assessing academic merit, attested credentials, and government clearance.",
            "standardized_tests": "IELTS/TOEFL recommended for STEM disciplines; English medium certificate accepted.",
            "application_fee_amount": "SAR 0 (100% free of charge)",
            "attestation_requirements": "IBCC (Intermediate), HEC (Bachelor's), and MoFA Pakistan attestations mandatory.",
            "translation_requirements": "Certified English or Arabic translation of all educational documents.",
            "final_submission_method": "100% digital submission via Study in Saudi platform."
        },
        "required_documents_checklist": [
            {
                "document_name": "Attested Educational Certificates and Transcripts",
                "mandatory": True,
                "specification": "Matric/Intermediate/Bachelor's degrees with minimum 80% aggregate marks.",
                "pakistan_specific_instruction": "Attested by IBCC/HEC and MoFA Pakistan."
            },
            {
                "document_name": "Police Character Clearance Certificate",
                "mandatory": True,
                "specification": "Official police record confirming clean conduct without criminal background.",
                "pakistan_specific_instruction": "Issued by local police and attested by MoFA Pakistan."
            },
            {
                "document_name": "Medical Fitness Certificate",
                "mandatory": True,
                "specification": "Complete medical exam verifying freedom from infectious illnesses (HIV, Hepatitis B/C, Tuberculosis).",
                "pakistan_specific_instruction": "Issued by an accredited medical diagnostic laboratory."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport personal information page valid for at least 2 years.",
                "pakistan_specific_instruction": "Validity extending minimum through late 2028."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from former teachers or academic advisors attesting to character and scholastic ability.",
                "pakistan_specific_instruction": "Printed on official institutional letterhead with contact details."
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
            "annual_cycle_notes": "Admissions open once annually during the summer cycle via Study in Saudi. Government approvals take several months."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Cumulative grades in qualifying secondary or university transcripts)",
            "extracurricular_and_leadership_weight": "10% (Character conduct and leadership potential)",
            "research_experience_weight": "15% (For master's applicants: research proposal and academic projects)",
            "work_experience_weight": "0% (Not required)",
            "personal_statement_weight": "10% (Statement of purpose quality)",
            "recommendations_weight": "5% (Academic referee recommendations)",
            "interview_weight": "0% (No interview required)",
            "test_scores_weight": "0% (Standardized tests optional)",
            "financial_need_weight": "0% (Merit and bilateral country allocation only)",
            "selection_panel_composition": "Deanship of Admission and Registration at University of Tabuk and Saudi Ministry of Education Review Board.",
            "evaluation_methodology": "Competitive ranking based on certified transcript marks, document verification, and national bilateral quotas."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000 to 18,000 international applicants across Study in Saudi portal",
            "total_scholarships_awarded": "~180 to 250 scholarships awarded annually at UT",
            "acceptance_rate_global": "~1.5% to 2.5%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% (Pakistan is prioritized under bilateral educational ties)",
            "typical_successful_applicant_gpa": "Marks >= 85% in F.Sc / A-Levels or CGPA >= 3.4 / 4.0 in Bachelor's",
            "typical_academic_and_research_profile": "Top-tier academic marks, spotless disciplinary record, and verified IBCC/HEC/MoFA attestations.",
            "common_backgrounds_of_winners": "Graduates of Pakistani intermediate boards and recognized engineering institutions.",
            "high_representation_countries": "Pakistan, Yemen, Egypt, Jordan, Sudan, Bangladesh, Indonesia, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed admissions or scholarship visas to University of Tabuk.",
                "Applications are exclusively processed through https://studyinsaudi.moe.gov.sa/."
            ],
            "application_fee_warning": "The Saudi government and University of Tabuk do NOT charge any application or visa fee.",
            "agent_and_intermediary_warnings": "University of Tabuk does not authorize any recruiting agencies or third-party brokers.",
            "hidden_costs_breakdown": [
                "IBCC, HEC, and MoFA attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "Medical diagnostics in Pakistan: ~PKR 10,000 to 15,000.",
                "Visa processing via Etimad/VFS Tasheel: ~PKR 12,000 to 18,000.",
                "Initial settling cash prior to first stipend payment: ~SAR 500 (~PKR 37,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: Tabuk is isolated from major industry. Reality: Tabuk is adjacent to NEOM and the Red Sea project, hosting state-of-the-art technological initiatives.",
                "Myth: Arabic fluency is mandatory for computing or engineering. Reality: All STEM coursework and examinations are conducted in English."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party websites post outdated deadlines in winter; official portal opens in May and closes in July."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of at least 2.75 / 5.0 (Grade Good) each semester to retain full scholarship privileges.",
            "attendance_requirements": "Minimum 75% lecture and laboratory attendance required; lower attendance incurs course denial and stipend suspension.",
            "academic_progress_monitoring": "Semester-end academic audit conducted prior to ticket issuance and stipend continuation.",
            "work_restrictions_during_study": "Off-campus employment is strictly prohibited by Saudi student visa regulations.",
            "home_country_return_obligation": "Graduates are expected to return to Pakistan upon completion; university issues free one-way exit flight ticket.",
            "service_obligations_or_bonds": "Zero service bond or post-graduation financial repayment.",
            "repayment_clawback_conditions": "Scholarship is terminated and student repatriated if dismissed for academic failure or disciplinary misconduct.",
            "rules_for_changing_university": "Inter-university transfer between Saudi universities is prohibited for external scholarship holders.",
            "rules_for_changing_major": "Permitted only within the same academic college during the first year subject to dean approval.",
            "extension_policy": "Maximum extension of one additional semester may be approved upon academic department recommendation."
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
                "source_name": "University of Tabuk Deanship of Admission and Registration",
                "source_url": "https://www.ut.edu.sa/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-ME-032": {
        "scholarship_id": "SCH-ME-032",
        "basic_details": {
            "scholarship_name": "Zayed University Graduate Merit Scholarships",
            "offering_entity": "Zayed University (ZU), United Arab Emirates",
            "host_country": "United Arab Emirates",
            "host_institutions_covered": "Zayed University Campuses (Abu Dhabi and Dubai Campuses, UAE)",
            "degree_levels": ["Master of Science (MSc)", "Master of Arts (MA)", "Executive Master of Business Administration (EMBA)"],
            "major_restrictions": "Master of Science in Information Technology (Cyber Security), Master of Science in Finance, EMBA, Master of Arts in Diplomacy and International Affairs, and Master of Science in Environment and Sustainability.",
            "number_of_awards_total": "~50 to 80 tuition merit scholarships awarded per academic cycle across graduate faculties",
            "number_of_awards_pakistan": "Open to all nationalities based on academic merit; prominent Pakistani graduate cohort in UAE higher education (~10 to 15 awards annually)",
            "funding_classification": "PARTIAL",
            "duration_of_scholarship": "Normal duration of Master's program (typically 2 years / 4 semesters)",
            "tuition_waiver_type": "PARTIAL",
            "monthly_stipend_amount": "AED 0 (Tuition reduction discount only; no monthly living allowance provided)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students and UAE residents of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 0,
            "age_limit_notes": "No strict age limit for graduate study; applicants must meet academic admission standards.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree from an HEC-recognized institution with a minimum CGPA of 3.20 / 4.00 for scholarship eligibility (minimum 3.00 for regular admission). Must obtain degree equivalency from UAE Ministry of Education.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Tiered merit brackets: 40% tuition fee reduction for undergraduate CGPA >= 3.80 / 4.00; 30% reduction for CGPA 3.60 - 3.79; 20% reduction for CGPA 3.20 - 3.59.",
            "subject_background_prerequisites": "Bachelor's degree in relevant or quantitative discipline for IT and Finance programs.",
            "current_education_status": "Applicants must have completed Bachelor's degree and hold complete transcripts and certificate.",
            "graduation_year_restrictions": "No specific graduation year limitation.",
            "work_experience_required": True,
            "work_experience_minimum_years": 1.0,
            "work_experience_notes": "1 to 3 years relevant professional experience required or strongly preferred, particularly for EMBA and Diplomacy programs.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Valid IELTS Academic (minimum 6.0 to 6.5 depending on program) or TOEFL iBT (minimum 79) or EmSAT English (minimum 1400) is mandatory.",
            "other_language_requirements": "None; all graduate programs are conducted in English.",
            "gender_specific_requirements": "Open to both male and female graduate applicants at both Abu Dhabi and Dubai campuses.",
            "financial_need_required": False,
            "special_eligibility_categories": "Merit scholarships are evaluated and granted automatically upon admission based on verified undergraduate CGPA.",
            "previous_scholarship_restrictions": "Cannot be combined with another institutional or governmental fee sponsorship.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIAL",
                "details": "20% to 40% tuition fee discount awarded based on undergraduate CGPA tiers (40% discount for CGPA 3.80+, 30% for 3.60-3.79, 20% for 3.20-3.59). Remaining tuition is student responsibility.",
                "amount": "20% to 40% tuition waiver (approx. AED 18,000 to 45,000 total fee reduction; ~PKR 1,350,000 to 3,375,000)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Non-refundable application processing fee of AED 420 must be paid directly by the candidate upon portal submission.",
                "amount": "AED 420 (~PKR 31,500 / ~USD 115) not covered"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "University does not provide free housing for graduate students; students must self-fund private apartment rental in Dubai or Abu Dhabi.",
                "amount": "Not covered (approx. AED 2,500 to 4,500 / month private rent)"
            },
            "monthly_stipend": {
                "status": "NOT_COVERED",
                "details": "No living stipend provided; candidates must have personal, family, or employer funds to cover living and accommodation costs.",
                "amount": "AED 0 (Not covered)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel and relocation flights to the UAE are completely self-funded by the student.",
                "amount": "Not covered"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "University sponsors the UAE student residence visa, but government visa charges, medical screening, and Emirates ID fees (~AED 2,500 to 3,500) are paid by the student.",
                "amount": "Approx. AED 3,000 visa costs borne by student"
            },
            "health_insurance": {
                "status": "NOT_COVERED",
                "details": "Mandatory UAE health insurance coverage must be purchased by the student as a prerequisite for visa stamping.",
                "amount": "Approx. AED 1,200 to 2,000 / year borne by student"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "All daily living, groceries, and dining costs are self-funded by the student.",
                "amount": "Not covered"
            },
            "books_and_materials_allowance": {
                "status": "NOT_COVERED",
                "details": "Textbooks and course packs self-funded; digital library access and electronic journal databases are included with university enrollment.",
                "amount": "Not covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Graduate students can apply to Zayed University Office of Research for student travel grants up to AED 5,000 to present approved papers at international conferences.",
                "amount": "Up to AED 5,000 conference presentation funding"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Local transport (Dubai Metro, Abu Dhabi buses, or private commuting) is self-funded.",
                "amount": "Not covered"
            },
            "total_estimated_value_usd_per_year": 6500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution across dual campuses (Zayed University, Abu Dhabi and Dubai).",
            "participating_institutions": [
                "Zayed University (Abu Dhabi Campus, Khalifa City)",
                "Zayed University (Dubai Campus, Academic City)"
            ],
            "university_rankings_scope": "QS World University Rankings #651-700, QS Arab Region #20, CAA accredited by UAE Ministry of Education, AACSB accredited for Business.",
            "available_majors": [
                "Executive Master of Business Administration (EMBA)",
                "Master of Science in Information Technology (Cyber Security)",
                "Master of Science in Finance",
                "Master of Arts in Diplomacy and International Affairs",
                "Master of Arts in Communication (Strategic Public Relations)",
                "Master of Science in Environment and Sustainability"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years (4 semesters, executive evening/weekend schedule)",
            "admission_requirements_summary": "Bachelor's degree with minimum CGPA 3.00 (3.20 for scholarship), UAE MOE Certificate of Equivalency, official transcripts, IELTS Academic 6.0/6.5+ or TOEFL 79+, CV showing work experience, two recommendation letters, and statement of objectives.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Cyber Security and Finance have rigorous quantitative evaluations; EMBA requires solid professional track record.",
            "strategic_program_match_advice": "Applicants must initiate the UAE Ministry of Education Certificate of Equivalency well in advance, as Pakistani HEC and MoFA attestations are required before UAE MOE processing."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.zu.ac.ae/main/en/graduate_programs/how_to_apply.aspx",
            "portal_system_name": "Zayed University Graduate Online Admissions Portal",
            "account_creation_instructions": "Register on ZU graduate portal, select intended degree program and preferred campus (Abu Dhabi or Dubai), fill academic and biographical details, and upload certified documents.",
            "step_by_step_workflow": [
                "Step 1: Obtain degree attestations from HEC Pakistan, MoFA Pakistan, and UAE Embassy Islamabad.",
                "Step 2: Apply online for UAE Ministry of Education Certificate of Equivalency (moe.gov.ae).",
                "Step 3: Register on Zayed University Graduate Admissions Portal and pay non-refundable AED 420 application fee.",
                "Step 4: Upload attested transcripts, IELTS/TOEFL score, CV, two recommendation letters, and statement of intent.",
                "Step 5: Attend admissions interview (conducted in-person or virtually via Zoom/Teams).",
                "Step 6: Receive admission decision and Graduate Merit Scholarship tier confirmation (20%, 30%, or 40%).",
                "Step 7: Pay seat deposit, complete course registration, and initiate UAE student visa process through university sponsorship."
            ],
            "university_vs_scholarship_routing": "Unified Institutional Evaluation: Scholarship tier is automatically evaluated and applied upon degree admission based on verified undergraduate CGPA.",
            "recommendation_letters_submission_method": "Uploaded directly via application portal or sent via official referee corporate/institutional email.",
            "personal_statement_prompts": "Statement of professional and academic objectives (500 to 1,000 words) describing career aspirations, background, and alignment with ZU program.",
            "study_plan_research_proposal_requirements": "Not mandatory for coursework Master's; brief statement of research interest required for thesis options.",
            "cv_format_requirements": "Professional chronological CV highlighting higher education, work history, leadership, and technical qualifications.",
            "interviews_conducted": True,
            "interview_format_details": "Departmental faculty panel interview assessing professional maturity, academic preparedness, and communication skills.",
            "standardized_tests": "IELTS Academic (minimum 6.0 - 6.5) or TOEFL iBT (minimum 79) mandatory; GMAT/GRE optional.",
            "application_fee_amount": "AED 420 (approx. USD 115 / ~PKR 31,500)",
            "attestation_requirements": "HEC Pakistan, MoFA Pakistan, UAE Embassy Islamabad, and UAE Ministry of Education Certificate of Equivalency mandatory.",
            "translation_requirements": "Official certified English translation of all degrees and transcripts not originally issued in English.",
            "final_submission_method": "100% online submission via Zayed University Graduate portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's Degree Certificate and Transcripts",
                "mandatory": True,
                "specification": "16-year Bachelor's degree with minimum CGPA 3.0/4.0 (3.20+ for merit discount).",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and UAE Embassy."
            },
            {
                "document_name": "UAE Ministry of Education Certificate of Equivalency",
                "mandatory": True,
                "specification": "Official equivalency document issued by UAE MOE verifying foreign degree parity.",
                "pakistan_specific_instruction": "Obtained via UAE MOE portal after MoFA and UAE Embassy attestations."
            },
            {
                "document_name": "English Language Proficiency Test Score",
                "mandatory": True,
                "specification": "Official IELTS Academic (minimum 6.0 to 6.5) or TOEFL iBT (minimum 79).",
                "pakistan_specific_instruction": "Direct electronic score report submitted to Zayed University."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed professional CV detailing 1 to 3+ years of relevant employment history.",
                "pakistan_specific_instruction": "Demonstrating career track record."
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "One academic and one professional recommendation assessing capability for graduate study.",
                "pakistan_specific_instruction": "Printed on official institutional/corporate letterhead."
            },
            {
                "document_name": "Statement of Professional and Academic Objectives",
                "mandatory": True,
                "specification": "500 to 1,000-word essay explaining motivations, background, and career trajectory.",
                "pakistan_specific_instruction": "Tailored to chosen Zayed University graduate curriculum."
            },
            {
                "document_name": "Valid Passport Copy and Photographs",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for minimum 6 months.",
                "pakistan_specific_instruction": "Along with passport-size digital photographs against white background."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "April 1 (Fall intake) / October 1 (Spring intake)",
            "application_deadline": "June 30 (Fall intake) / November 30 (Spring intake)",
            "university_admission_deadline": "June 30 (Fall) / November 30 (Spring)",
            "document_submission_deadline": "June 30 (Fall) / November 30 (Spring)",
            "recommendation_letters_deadline": "June 30 (Fall) / November 30 (Spring)",
            "interview_period": "July (Fall) / December (Spring)",
            "shortlist_announcement": "Rolling review, results within 4 to 6 weeks of complete submission",
            "final_result_acceptance_deadline": "August 10 (Fall) / January 5 (Spring)",
            "visa_application_window": "July - August (Fall) / December - January (Spring)",
            "semester_commencement": "Late August (Fall intake) / January (Spring intake)",
            "annual_cycle_notes": "Admissions operate biannually across Fall (August start) and Spring (January start) semesters."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Undergraduate CGPA and transcript performance)",
            "extracurricular_and_leadership_weight": "10% (Leadership achievements and community involvement)",
            "research_experience_weight": "10% (Scholarly papers or analytical research writing)",
            "work_experience_weight": "15% (Relevant industry experience and professional accomplishments)",
            "personal_statement_weight": "10% (Quality and alignment of statement of objectives)",
            "recommendations_weight": "5% (Appraisals from academic and professional referees)",
            "interview_weight": "0% (Used for admission qualification rather than percentage scoring)",
            "test_scores_weight": "0% (English test is qualifying prerequisite)",
            "financial_need_weight": "0% (Merit-based tuition discount only)",
            "selection_panel_composition": "Zayed University Deanship of Graduate Studies and Faculty Admissions Committee.",
            "evaluation_methodology": "Systematic evaluation: Candidates meeting GPA criteria (>= 3.20) are automatically tiered into 20%, 30%, or 40% tuition reduction brackets upon formal admission."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,500 graduate applicants across programs",
            "total_scholarships_awarded": "~50 to 80 graduate merit tuition awards across all tiers",
            "acceptance_rate_global": "~25% to 35% for admission; ~15% for top 40% merit bracket",
            "acceptance_rate_pakistan": "~20% to 30% for qualified applicants with equivalency",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.60 / 4.00 for substantial 30-40% fee reduction",
            "typical_academic_and_research_profile": "Graduates with solid bachelor's records, 2+ years professional experience in corporate, government, or IT sectors, and verified IELTS 6.5+.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (LUMS, NUST, FAST, IBA, COMSATS) and regional UAE bachelor's alumni.",
            "high_representation_countries": "UAE, Pakistan, Egypt, Jordan, India, Lebanon, Palestine, Nigeria.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only submit applications through official portal at zu.ac.ae.",
                "Beware of external admission agencies charging unauthorized commission fees."
            ],
            "application_fee_warning": "Application fee of AED 420 is paid strictly through the secure university portal; no third-party cash payments.",
            "agent_and_intermediary_warnings": "Zayed University does not require intermediaries; all applicants are evaluated directly.",
            "hidden_costs_breakdown": [
                "Remaining 60% to 80% tuition fees: ~AED 50,000 to 90,000 across the degree program.",
                "UAE MOE Degree Equivalency fee: ~AED 100 to 200.",
                "Attestation costs across Pakistan and UAE missions: ~PKR 35,000 to 50,000.",
                "UAE Student Visa issuance, medical fitness test, and Emirates ID: ~AED 2,500 to 3,500.",
                "Living expenses, rent, and groceries in Dubai/Abu Dhabi: ~AED 3,500 to 5,500 / month."
            ],
            "misleading_claims_debunked": [
                "Myth: The scholarship covers living expenses or housing. Reality: This is exclusively a partial tuition fee waiver (20-40%). Students must fund all living and remaining tuition costs.",
                "Myth: You can enroll without UAE MOE Equivalency. Reality: UAE MOE Equivalency is legally mandatory for formal matriculation and degree conferral."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim full living stipends exist; ZU graduate merit awards are strictly tuition waivers."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative graduate GPA of 3.20 / 4.00 throughout each semester of study to retain tuition fee waiver.",
            "attendance_requirements": "Minimum 80% class attendance in all registered graduate modules.",
            "academic_progress_monitoring": "Biannual GPA review at the end of each semester by the Deanship of Graduate Studies.",
            "work_restrictions_during_study": "Classes are scheduled during evenings and weekends; international students holding UAE residency or university visa are permitted to pursue employment subject to UAE labor laws.",
            "home_country_return_obligation": "None; graduates are free to pursue employment in the UAE or internationally.",
            "service_obligations_or_bonds": "Zero service bond or post-graduation employment commitment.",
            "repayment_clawback_conditions": "If graduate CGPA drops below 3.20 / 4.00, the merit discount is revoked for subsequent semesters without retroactive payback.",
            "rules_for_changing_university": "Non-transferable; scholarship applies solely to registered study at Zayed University.",
            "rules_for_changing_major": "Changing major requires re-application and approval from both academic colleges and scholarship committee.",
            "extension_policy": "Scholarship covers only the standard normative semester sequence; extra remedial semesters are billed at full non-discounted rate."
        },
        "official_sources_verified": [
            {
                "source_name": "Zayed University Deanship of Graduate Studies Tuition Fees & Financial Support",
                "source_url": "https://www.zu.ac.ae/main/en/graduate_programs/tuition_fees.aspx",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Zayed University Graduate Admission Requirements",
                "source_url": "https://www.zu.ac.ae/main/en/graduate_programs/admission_requirements.aspx",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
