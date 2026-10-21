# scripts/batch12a_p1.py
# SCH-ME-010 & SCH-ME-012

DATA_P1 = {
    "SCH-ME-010": {
        "scholarship_id": "SCH-ME-010",
        "basic_details": {
            "scholarship_name": "Abu Dhabi University Academic & Chairman Scholarship",
            "offering_entity": "Abu Dhabi University (ADU) & ADU Board of Regents (Abu Dhabi, United Arab Emirates)",
            "host_country": "United Arab Emirates",
            "host_institutions_covered": "Abu Dhabi University Campuses: Abu Dhabi (Main Campus), Al Ain Campus, and Dubai Campus",
            "degree_levels": ["Bachelor of Science (BS)", "Master of Science (MS)", "Doctor of Business Administration (DBA)"],
            "major_restrictions": "Open to leading academic degree programs: College of Engineering (Computer Science, Artificial Intelligence, Cybersecurity, Software Engineering, Civil Engineering, Mechanical Engineering, Electrical Engineering), College of Business (Finance, Business Analytics), College of Health Sciences, and College of Arts and Sciences.",
            "number_of_awards_total": "Approximately 100 to 150 Chairman and Academic Merit Scholarships awarded annually across undergraduate and postgraduate divisions",
            "number_of_awards_pakistan": "Merit-based open international quota; high representation of overseas Pakistani high school toppers and residents in UAE/Pakistan (typically 20 to 35 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Standard program duration: 4 years for Bachelor degrees; 2 years for Master degrees, subject to maintaining semester CGPA >= 3.60 to 3.80"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to all international students, UAE residents, and expatriates"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 24,
            "age_limit_postgrad": None,
            "age_limit_notes": "Undergraduate candidates must have completed secondary school within the last 2 years (under 24 years of age). No age restriction for postgraduate applicants.",
            "academic_qualifications": "For Undergraduate: Minimum 90% in Pakistani Higher Secondary School Certificate (HSSC / Intermediate Pre-Engineering or ICS from BISE boards) or equivalent Cambridge A-Levels (minimum AAA/AAB). For Master's: Minimum 3.60 / 4.00 CGPA from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 90.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "90%+ in Intermediate board examinations qualifies for Chairman / Academic Scholarship tier offering 100% full tuition waiver.",
            "subject_background_prerequisites": "Pre-Engineering, Computer Science, or Mathematics background for College of Engineering programs.",
            "current_education_status": "Final year graduating students or recent high school/university graduates.",
            "graduation_year_restrictions": "High school certificates must have been issued within past 2 academic years for undergraduate scholarship consideration.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience not required; for Master's programs, professional software engineering experience is considered favorably.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 79,
                "duolingo_accepted": True,
                "moi_certificate_accepted": False,
                "notes": "EmSAT Achieve English min 1400, IELTS Academic min 6.0, TOEFL iBT min 79, or Duolingo min 105 required for degree matriculation."
            },
            "other_language_requirements": "Arabic language not required; English is the medium of instruction for all computing, engineering, and business programs.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Merit-based scholarships awarded strictly to top academic performers.",
            "previous_scholarship_restrictions": "Cannot combine multiple internal ADU scholarships concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver (AED 55,000 to 75,000 / year waived completely for all standard credit hours).",
                "amount": "100% covered (~AED 65,000 / year value; ~PKR 4,940,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "Application fee (AED 315) and registration fees (AED 3,150) waived for Chairman Scholarship recipients.",
                "amount": "AED 3,465 waived value (~PKR 260,000)"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "Living and accommodation are self-funded; on-campus student housing available at Abu Dhabi campus (~AED 1,500 to 2,500/month; ~PKR 115,000 to 190,000/month).",
                "amount": "Self-funded (~AED 20,000 / year; ~PKR 1,520,000 / year)"
            },
            "monthly_stipend": {
                "status": "NOT_COVERED",
                "details": "ADU does not provide a monthly living allowance; students cover personal expenses, though on-campus student work-study positions are available.",
                "amount": "AED 0 (Self-funded living)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Round-trip airfare between Pakistan and UAE (Dubai/Abu Dhabi) is self-funded by student.",
                "amount": "Self-funded (~PKR 90,000 to 140,000 round-trip value)"
            },
            "visa_fee": {
                "status": "SUBSIDIZED",
                "details": "Abu Dhabi University sponsors UAE Student Residence Visa; student pays government visa medical and Emirates ID processing fee (~AED 2,500; ~PKR 190,000).",
                "amount": "University visa sponsorship provided"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive UAE student health insurance coverage included with university visa package.",
                "amount": "Covered under UAE student visa insurance (~AED 1,200/year value)"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Self-funded; on-campus dining and local grocery costs average AED 800 to 1,200 per month (~PKR 60,000 to 90,000/mo).",
                "amount": "Self-funded"
            },
            "books_and_materials_allowance": {
                "status": "NOT_COVERED",
                "details": "E-textbooks and software licenses are provided via university portal; physical books are self-funded.",
                "amount": "Self-funded (~AED 1,000 / year)"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Office of Research and Sponsored Programs provides undergraduate and graduate student research grants and conference sponsorship.",
                "amount": "Up to AED 5,000 per conference paper"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Complimentary student shuttle transportation provided between ADU campus and major transit hubs in Abu Dhabi and Dubai.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single accredited university: Abu Dhabi University (campuses in Abu Dhabi, Al Ain, Dubai)",
            "participating_institutions": [
                "Abu Dhabi University - Abu Dhabi Main Campus",
                "Abu Dhabi University - Al Ain Campus",
                "Abu Dhabi University - Dubai Campus (Knowledge Park)"
            ],
            "university_rankings_scope": "Ranked top 600 globally (QS World #580, top 15 in Arab Region). All engineering and CS programs ABET-accredited; business programs AACSB & EQUIS-accredited.",
            "available_majors": [
                "College of Engineering: Computer Science, Artificial Intelligence, Cybersecurity, Software Engineering",
                "College of Engineering: Information Technology, Computer Engineering, Civil Engineering, Mechanical Engineering",
                "College of Business: Finance, Accounting, Business Analytics, Digital Marketing",
                "College of Health Sciences: Biomedical Sciences, Public Health, Environmental Health and Safety",
                "College of Arts and Sciences: Applied Mathematics, Mass Communication"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor degrees: 4 years (8 semesters); Master degrees: 2 years (4 semesters).",
            "admission_requirements_summary": "High school certificate with 90%+ marks (undergraduate) or Bachelor's with 3.6+ CGPA (graduate), EmSAT/IELTS 6.0, IBCC equivalence, MOFA attestation, and university placement tests.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science, AI, and Cybersecurity have highest applicant volume; Civil Engineering and Business Analytics offer steady scholarship seat availability.",
            "strategic_program_match_advice": "Pakistani intermediate board (BISE) students with 90%+ marks should apply immediately upon result declaration (June/July) to secure the limited Chairman Scholarship (100% waiver) quotas before seats convert to 50% or 30% academic tiers."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.adu.ac.ae/apply-now",
            "portal_system_name": "Abu Dhabi University Online Admissions & Scholarship Portal",
            "account_creation_instructions": "Create an account on the ADU online admissions portal, fill out student bio-data, select degree program and campus, and check the box to apply for Academic / Chairman Scholarship.",
            "step_by_step_workflow": [
                "Step 1 (May - June): Prepare educational credentials; obtain IBCC equivalence certificate (for Pakistani Intermediate/Matric) and MOFA attestation.",
                "Step 2 (June - July): Register on ADU Online Admissions Portal (adu.ac.ae/apply-now) and complete the admission form.",
                "Step 3 (July): Upload certified transcripts, passport copy, Emirates ID (if UAE resident), English test certificate (IELTS/EmSAT), and passport photographs.",
                "Step 4 (Late July / Early August): Admissions committee assesses application and high school marks; conditional admission and scholarship tier offer issued within 5-7 business days.",
                "Step 5 (August): Complete UAE Ministry of Education (MOE) certificate equivalency via the online MOE portal.",
                "Step 6 (Mid-August): Pay initial deposit to secure seat (adjusted against registration/visa); receive unconditional admission letter and scholarship contract.",
                "Step 7 (Late August): University issues UAE Student Visa sponsorship entry permit; travel to Abu Dhabi or Dubai.",
                "Step 8 (Early September): Complete medical examination in UAE, obtain Emirates ID, attend campus orientation, and enroll in classes."
            ],
            "university_vs_scholarship_routing": "Integrated application: Scholarship assessment occurs automatically based on submitted high school or university grades.",
            "recommendation_letters_submission_method": "One to two recommendation letters from high school principal or university professors uploaded directly to online portal.",
            "personal_statement_prompts": "Personal Statement (500 words): Discuss academic interests, career ambitions in the UAE and internationally, and reason for choosing Abu Dhabi University.",
            "study_plan_research_proposal_requirements": "Not required for undergraduate applicants. For Master's applicants: 1-2 page statement of research or professional objectives.",
            "cv_format_requirements": "Standard academic CV outlining educational history, academic honors, extracurriculars, and technical skills.",
            "interviews_conducted": False,
            "interview_format_details": "No formal interview required; selection is strictly based on standardized high school / university marks and English test compliance.",
            "standardized_tests": "EmSAT English (1400+) or IELTS Academic (6.0+) or TOEFL iBT (79+). EmSAT Math score or ADU math placement test required for engineering.",
            "application_fee_amount": "AED 315 (Waived for Chairman Scholarship recipients upon final enrollment)",
            "attestation_requirements": "Attestation by IBCC/HEC and MOFA Pakistan, followed by UAE Embassy in Islamabad or UAE Consulate in Karachi.",
            "translation_requirements": "Certified English or Arabic translations for any documents not originally issued in English.",
            "final_submission_method": "100% digital submission via Abu Dhabi University admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport information page valid for at least six months.",
                "pakistan_specific_instruction": "Ensure Pakistani machine-readable passport is scanned in color."
            },
            {
                "document_name": "Secondary School / Intermediate Certificates & Transcripts",
                "mandatory": True,
                "specification": "Official certified matriculation and intermediate (HSSC) mark sheets and certificates.",
                "pakistan_specific_instruction": "Attested by IBCC, MOFA Pakistan, and UAE Embassy in Islamabad."
            },
            {
                "document_name": "Equivalence Certificate from UAE Ministry of Education",
                "mandatory": True,
                "specification": "Official Equalization Certificate issued by UAE Ministry of Education (MOE) portal.",
                "pakistan_specific_instruction": "Obtained online via UAE MOE website after IBCC and UAE embassy attestation."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS Academic (6.0+), TOEFL iBT (79+), or EmSAT English (1400+) scorecard.",
                "pakistan_specific_instruction": "Test date must be within 2 years of application date."
            },
            {
                "document_name": "Passport-Sized Photographs",
                "mandatory": True,
                "specification": "High-resolution color photographs with white background.",
                "pakistan_specific_instruction": "Standard UAE visa photo specifications (3.5 x 4.5 cm)."
            },
            {
                "document_name": "Certificate of Good Conduct / Police Clearance (if requested)",
                "mandatory": False,
                "specification": "Character certificate from previous institution or police clearance certificate.",
                "pakistan_specific_instruction": "Issued by school/college principal or Police Khidmat Markaz."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 June 2027",
            "application_deadline": "15 August 2027 (Fall Intake) / 15 December 2027 (Spring Intake)",
            "university_admission_deadline": "15 August 2027",
            "document_submission_deadline": "20 August 2027",
            "recommendation_letters_deadline": "15 August 2027",
            "interview_period": "Not applicable (Continuous review)",
            "shortlist_announcement": "Within 1 to 2 weeks of document submission (Rolling admissions)",
            "final_result_acceptance_deadline": "25 August 2027",
            "visa_application_window": "1 August to 30 August 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Main Fall intake commences in September; secondary Spring intake opens in January."
        },
        "selection_process_and_weights": {
            "academic_weight": "70% (Secondary school percentage or undergraduate CGPA)",
            "extracurricular_and_leadership_weight": "5% (School honors, community engagement)",
            "research_experience_weight": "5% (For graduate applicants: prior research projects or publications)",
            "work_experience_weight": "5% (For graduate applicants: professional experience)",
            "personal_statement_weight": "5% (Motivation and commitment to program)",
            "recommendations_weight": "5% (School counselor or professor appraisal)",
            "interview_weight": "0% (No interview required)",
            "test_scores_weight": "5% (English and Mathematics EmSAT/IELTS scores)",
            "financial_need_weight": "0% (Merit-based scholarship)",
            "selection_panel_composition": "Abu Dhabi University Admissions Committee & Office of Enrollment Management.",
            "evaluation_methodology": "Direct grade-indexed evaluation: Applicants with 90%+ in high school automatically qualify for consideration for the 100% tuition waiver tier (Chairman Scholarship). Allocations granted on first-come, first-served basis as long as quota seats remain available in each college."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 1,800 international and expatriate applicants",
            "total_scholarships_awarded": "~100 to 150 Chairman and Academic Merit Scholarships (100% waiver)",
            "acceptance_rate_global": "~8.5%",
            "acceptance_rate_pakistan": "~20.0% (High success rate for Pakistani intermediate board toppers with 90%+)",
            "typical_successful_applicant_gpa": "92%+ in Pakistani Intermediate (Pre-Engineering/ICS) or 3.80+ / 4.00 CGPA for Master's",
            "typical_academic_and_research_profile": "Distinguished high school academic record, strong mathematics aptitude, IELTS 6.5+, complete attestation dossier ready early.",
            "common_backgrounds_of_winners": "Pakistani BISE board toppers from Lahore, Federal (FBISE), Rawalpindi, and Karachi boards, as well as UAE-resident Pakistani community school graduates.",
            "high_representation_countries": "Pakistan, Egypt, Jordan, Syria, Palestine, India, UAE",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized commercial recruiters claiming to sell guaranteed ADU scholarships. Abu Dhabi University processes scholarships exclusively through its official website."
            ],
            "application_fee_warning": "Standard application fee is AED 315; never pay higher processing fees to external agencies.",
            "agent_and_intermediary_warnings": "ADU does not endorse paid third-party agents for scholarship processing; applications submitted directly are given full consideration.",
            "hidden_costs_breakdown": [
                "Living and accommodation costs in Abu Dhabi / Dubai are entirely self-funded (~AED 2,000 - 3,000/month; ~PKR 150,000 - 225,000/mo).",
                "UAE student residence visa fees and medical tests (~AED 2,500; ~PKR 190,000).",
                "Educational document attestation costs across IBCC, MOFA, and UAE Embassy (~PKR 30,000 - 45,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: ADU provides full living stipends and free food. (FACT: The Chairman Scholarship covers 100% of tuition and fees only; living and dorms are self-funded).",
                "CLAIM: Arabic proficiency is needed. (FACT: 100% of courses in computing and engineering are taught in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Commercial portals sometimes list ADU scholarships as fully covering living expenses; official university policy confirms it is a 100% tuition waiver only."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum CGPA of 3.60 (undergraduate) or 3.80 (graduate) each semester to retain 100% tuition waiver; if GPA drops below threshold, scholarship tier reduces to 50% or terminates.",
            "attendance_requirements": "Must maintain minimum 80% attendance in all enrolled courses.",
            "academic_progress_monitoring": "Semester-by-semester GPA review conducted by Office of Financial Aid.",
            "work_restrictions_during_study": "Students may work part-time on campus (up to 15 hours/week) under ADU student employment scheme or take off-campus internships with UAE student visa work permit.",
            "home_country_return_obligation": "None. Graduates are eligible to apply for UAE Green Visa or seek employment in the UAE technology and engineering sector.",
            "service_obligations_or_bonds": "Zero service bonds or return obligations.",
            "repayment_clawback_conditions": "Scholarship terminates if CGPA falls below required standard; past waived tuition is not clawed back.",
            "rules_for_changing_university": "Non-transferable to other UAE or international universities.",
            "rules_for_changing_major": "Changing majors is permitted within ADU subject to maintaining minimum CGPA and college approval.",
            "extension_policy": "Strictly limited to the standard program duration (4 years for Bachelor, 2 years for Master); extra semesters are billed at standard tuition rates."
        },
        "official_sources_verified": [
            {
                "source_name": "Abu Dhabi University Official Scholarships & Financial Support Portal",
                "source_url": "https://www.adu.ac.ae/admissions/financial-support/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific college-wise quota limits for the 100% Chairman Scholarship waiver.",
                    "Exact waitlist fill policy when admitted scholarship recipients fail to enroll.",
                    "Historical nationality-wise percentage distribution of scholarship recipients."
                ]
            },
            {
                "source_name": "UAE Ministry of Education (MOE) Private Higher Education Commission",
                "source_url": "https://www.moe.gov.ae/en/services/pages/certificate-equivalency.aspx",
                "source_type": "GOVERNMENT_MINISTRY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Average processing turnaround time for foreign secondary school certificate equivalency during peak August cycles.",
                    "Institutional appeal guidelines for conditional equivalency certificates."
                ]
            }
        ]
    },
    "SCH-ME-012": {
        "scholarship_id": "SCH-ME-012",
        "basic_details": {
            "scholarship_name": "Imam Mohammad Ibn Saud Islamic University Full Scholarship",
            "offering_entity": "Saudi Ministry of Education & Imam Mohammad Ibn Saud Islamic University (IMSIU, Riyadh, Kingdom of Saudi Arabia)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "Imam Mohammad Ibn Saud Islamic University Main Campus (Riyadh, Saudi Arabia)",
            "degree_levels": ["Bachelor of Science (BS)", "Master of Science (MS)", "Doctor of Philosophy (PhD)", "Arabic Language Diploma"],
            "major_restrictions": "Open to leading STEM, Computing, and Humanities colleges: College of Computer and Information Sciences (Computer Science, Information Systems, Information Security, Software Engineering), College of Science (Mathematics, Physics, Chemistry), College of Engineering, College of Economics and Administrative Sciences, and Islamic Studies.",
            "number_of_awards_total": "Approximately 400 to 600 international external scholarships awarded annually across all colleges under Saudi Government External Scholarships program",
            "number_of_awards_pakistan": "Government bilateral country quota: 40 dedicated seats allocated annually for Pakistani citizens across degree levels",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 to 5 years for Bachelor degree (plus 1 prep year if needed); 2 years for Master; 3 to 4 years for PhD, subject to maintaining good academic standing"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Saudi citizens residing outside the Kingdom of Saudi Arabia (External Scholarship Program)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate applicants must be between 17 and 25 years old; Master's applicants must be under 30 (or under 35 for specific STEM tracks); PhD applicants must be under 35 years old.",
            "academic_qualifications": "For Undergraduate: Completed Higher Secondary School Certificate (HSSC / Intermediate) with minimum 75% marks (or 'Very Good' / Grade B+). For Master's: Completed 4-year Bachelor's degree (16 years education) with minimum 3.00 / 4.00 CGPA from an HEC-recognized university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Grading classification of 'Very Good' (Jayyid Jiddan) or higher in secondary school certificate.",
            "subject_background_prerequisites": "Pre-Engineering, Computer Science, or General Science background for College of Computer and Information Sciences.",
            "current_education_status": "Must have graduated within the past 5 years from date of application.",
            "graduation_year_restrictions": "Secondary school graduation certificate must not be older than 5 years at the time of application.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": None,
                "toefl_minimum": None,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "No standardized English test mandatory for general admissions; College of Computer and Information Sciences conducts coursework in English and accepts English Medium of Instruction certificates."
            },
            "other_language_requirements": "Arabic language proficiency is NOT required for scientific and computing majors (instruction in English). Non-Arabic speakers admitted to Islamic/humanities majors undergo a 1-to-2 year intensive Arabic language preparatory diploma on campus.",
            "gender_specific_requirements": "Female students must have an eligible Mahram (male guardian) who is also a student, worker, or resident in Saudi Arabia, unless Saudi regulations permit independent university hostel residency for international female scholarship recipients.",
            "financial_need_required": False,
            "special_eligibility_categories": "International students from Islamic and partner countries under Saudi Ministry of Education bilateral quota.",
            "previous_scholarship_restrictions": "Applicant must not have previously received a scholarship from another educational institution in Saudi Arabia.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver across all academic semesters, including preparatory year.",
                "amount": "100% covered (~SAR 25,000 / year value; ~PKR 1,900,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "Application via Saudi Government Study in Saudi / Minhati portal is completely free of charge.",
                "amount": "SAR 0 (Free application)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free fully furnished university dormitory housing in IMSIU Student Housing Complex (Riyadh), with free utilities, air conditioning, and high-speed Wi-Fi.",
                "amount": "Free university housing (~SAR 12,000 / year value; ~PKR 910,000 / yr)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend paid directly by Saudi Government: SAR 840/month for Undergraduate students (~PKR 64,000/mo); SAR 1,000/month for Master's and PhD students (~PKR 76,000/mo).",
                "amount": "SAR 10,080 to 12,000 / year (~PKR 768,000 to 912,000 / year)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Annual round-trip economy class flight ticket provided between Pakistan (Islamabad/Lahore/Karachi) and Riyadh for annual summer vacation, plus initial arrival ticket.",
                "amount": "100% covered (~PKR 250,000 / year value)"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Saudi Student Visa and residency permit (Iqama) issued free of charge through the Royal Embassy of Saudi Arabia in Islamabad.",
                "amount": "100% covered (Free visa and Iqama)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive free medical and dental care at IMSIU University Medical Center and Saudi government tertiary hospitals.",
                "amount": "100% covered (~SAR 2,000 / year value)"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Heavily subsidized nutritious meals provided at university central dining halls (meals cost ~SAR 3 to 5 per meal; ~PKR 220 to 380/meal).",
                "amount": "Heavily subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Annual book allowance (equivalent to one month stipend) and thesis printing allowance of SAR 3,000 (Master) to SAR 4,000 (PhD) upon graduation.",
                "amount": "SAR 840 to 1,000 / year plus thesis grant"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "IMSIU Deanship of Scientific Research funds laboratory materials and conference attendance for postgraduate researchers.",
                "amount": "Funded by Deanship of Scientific Research"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Free shuttle bus transportation connecting student residence halls, academic colleges, central library, and prayer halls.",
                "amount": "Free campus shuttle"
            },
            "total_estimated_value_usd_per_year": 14500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single major comprehensive national university: Imam Mohammad Ibn Saud Islamic University (Riyadh, Saudi Arabia)",
            "participating_institutions": [
                "Imam Mohammad Ibn Saud Islamic University Main Campus (Riyadh)"
            ],
            "university_rankings_scope": "Top 800 global university (QS World #751-760, top 25 in Arab World). World-renowned faculty in computing, information security, and sharia jurisprudence.",
            "available_majors": [
                "College of Computer and Information Sciences: Computer Science, Information Systems, Information Security, Software Engineering",
                "College of Science: Applied Mathematics, Physics, Chemistry",
                "College of Engineering: Electrical Engineering, Mechanical Engineering, Civil Engineering",
                "College of Economics and Administrative Sciences: Economics, Finance, Business Administration, Accounting",
                "Arabic Language Teaching Institute: Intensive 2-Year Arabic Language Preparatory Diploma"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Undergraduate: 4 to 5 years (including preparatory year); Master: 2 years; PhD: 3 to 4 years.",
            "admission_requirements_summary": "Secondary school certificate with 75%+ marks, age 17-25 (undergrad) or under 35 (grad), medical fitness certificate, police clearance, and attested educational documents.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "College of Computer and Information Sciences (Information Security / Cyber) has highest competitive cutoffs; College of Science and Arabic Language Institute have favorable quota availability.",
            "strategic_program_match_advice": "Apply via the unified 'Study in Saudi' portal (studyinsaudi.moe.gov.sa) during the September-November window. Ensure all intermediate and matric documents are attested by IBCC and MOFA Pakistan before uploading."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://minhati.moe.gov.sa/",
            "portal_system_name": "Saudi Government Unified 'Study in Saudi' (Minhati) Portal & IMSIU Admissions Portal",
            "account_creation_instructions": "Create an account on the Saudi Ministry of Education unified portal (studyinsaudi.moe.gov.sa / minhati.moe.gov.sa), select Imam Mohammad Ibn Saud Islamic University, choose desired major, and upload required documents.",
            "step_by_step_workflow": [
                "Step 1 (July - August): Attest Matric and Intermediate certificates/degrees from IBCC and MOFA Pakistan; obtain Police Character Certificate and Medical Fitness Report.",
                "Step 2 (September - November): Register on the 'Study in Saudi' unified portal (studyinsaudi.moe.gov.sa); select IMSIU as preferred university.",
                "Step 3 (November - December): Upload all required documents (translated into Arabic if applicable) and submit electronic application.",
                "Step 4 (January - March): IMSIU Deanship of Admissions conducts academic credential screening and ranks applicants against bilateral quotas.",
                "Step 5 (April - May): University forwards recommended candidate list to Saudi Ministry of Education and Ministry of Foreign Affairs for security and administrative approval.",
                "Step 6 (June - July): Final scholarship award notifications issued; Saudi MOE issues official electronic visa approval number.",
                "Step 7 (July - August): Submit passport to Royal Embassy of Saudi Arabia in Islamabad or Consulate-General in Karachi for Student Visa stamping; university dispatches flight e-ticket.",
                "Step 8 (Late August / Early September): Arrival at King Khalid International Airport (Riyadh); university reception team provides airport transfer to campus housing."
            ],
            "university_vs_scholarship_routing": "Integrated government application: Admission to IMSIU for international students automatically includes full government scholarship funding.",
            "recommendation_letters_submission_method": "Two recommendation letters from recognized academic teachers or community scholars uploaded as scanned documents.",
            "personal_statement_prompts": "Motivation Statement (Arabic or English): Explain educational aspirations, religious character, and future academic and career objectives.",
            "study_plan_research_proposal_requirements": "Not required for undergraduate applicants. For Master's/PhD: 2-3 page research outline.",
            "cv_format_requirements": "Brief academic CV listing educational qualifications, grades, and language skills.",
            "interviews_conducted": False,
            "interview_format_details": "Interviews are generally not conducted; selection is document and credential based.",
            "standardized_tests": "None required. Qudurat / Tahsili tests are not required for external international applicants.",
            "application_fee_amount": "SAR 0 (100% Free of charge)",
            "attestation_requirements": "Attestation by IBCC/HEC and MOFA Pakistan, followed by Saudi Cultural Mission and Royal Embassy of Saudi Arabia in Pakistan upon selection.",
            "translation_requirements": "Official certified Arabic translation for all English/Urdu educational documents and police certificate.",
            "final_submission_method": "100% digital submission via the unified Study in Saudi portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport info page valid for at least two years.",
                "pakistan_specific_instruction": "Ensure Pakistani passport has at least 6 blank pages for visa and entry stamps."
            },
            {
                "document_name": "Secondary School Certificate & Detailed Mark Sheet",
                "mandatory": True,
                "specification": "Official matriculation and intermediate (HSSC) certificates and mark sheets.",
                "pakistan_specific_instruction": "Attested by IBCC and MOFA Pakistan, with certified Arabic translation."
            },
            {
                "document_name": "Medical Examination Report",
                "mandatory": True,
                "specification": "Comprehensive medical fitness certificate certifying freedom from infectious diseases (HIV, Hepatitis B/C, TB).",
                "pakistan_specific_instruction": "Completed at an authorized GAMCA / GCC approved medical center in Pakistan."
            },
            {
                "document_name": "Police Character Clearance Certificate",
                "mandatory": True,
                "specification": "Official Police Character Certificate certifying applicant has no criminal record.",
                "pakistan_specific_instruction": "Issued by Police Khidmat Markaz and attested by MOFA Pakistan with Arabic translation."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Recommendation letters from prominent teachers, professors, or recognized scholars.",
                "pakistan_specific_instruction": "Certified letters highlighting applicant's academic dedication and moral character."
            },
            {
                "document_name": "Birth Certificate",
                "mandatory": True,
                "specification": "Official Nadra computerized birth certificate.",
                "pakistan_specific_instruction": "Nadra Birth Certificate attested by MOFA Pakistan with Arabic translation."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 September 2026",
            "application_deadline": "15 November 2026",
            "university_admission_deadline": "15 November 2026",
            "document_submission_deadline": "15 November 2026",
            "recommendation_letters_deadline": "15 November 2026",
            "interview_period": "Not applicable (Document review)",
            "shortlist_announcement": "May to June 2027",
            "final_result_acceptance_deadline": "30 June 2027",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "Late August / Early September 2027",
            "annual_cycle_notes": "Single annual application intake cycle running for Fall semester enrollment."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Secondary school GPA/percentage in relevant subjects)",
            "extracurricular_and_leadership_weight": "5% (School and community involvement)",
            "research_experience_weight": "5% (For graduate applicants)",
            "work_experience_weight": "0% (Not considered for undergraduate)",
            "personal_statement_weight": "10% (Clarity of goals and motivation)",
            "recommendations_weight": "10% (Referee attestations of character and academic aptitude)",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "0% (No standardized tests)",
            "financial_need_weight": "0% (Merit and bilateral quota based)",
            "selection_panel_composition": "IMSIU International Admissions Committee, Saudi Ministry of Education Scholarship Board, and Ministry of Foreign Affairs.",
            "evaluation_methodology": "Quota-based merit ranking: Applications are ranked by academic percentage within country quota allocations (40 seats for Pakistan). Shortlisted candidates undergo ministry background check and final approval by Saudi Ministry of Education."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~8,000 to 12,000 international applicants across all participating countries",
            "total_scholarships_awarded": "~400 to 600 full international scholarships",
            "acceptance_rate_global": "~5.0%",
            "acceptance_rate_pakistan": "~26.0% (Dedicated bilateral quota of ~40 seats gives strong odds to well-qualified Pakistani applicants)",
            "typical_successful_applicant_gpa": "80%+ in Pakistani Intermediate (HSSC / Pre-Engineering / ICS) or 3.30+ CGPA for Master's",
            "typical_academic_and_research_profile": "Strong academic record, clean disciplinary and medical history, complete Arabic-translated and attested document dossier.",
            "common_backgrounds_of_winners": "Students from across Pakistan (Punjab, Sindh, KPK, Balochistan, AJK) with Intermediate certificates from recognized BISE boards.",
            "high_representation_countries": "Pakistan, Indonesia, Nigeria, Egypt, Malaysia, Bangladesh, Sudan",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent visa agents claiming to sell IMSIU scholarship visas for high fees. Saudi government scholarships are 100% free and strictly processed via the official Study in Saudi portal."
            ],
            "application_fee_warning": "Saudi government scholarships have ZERO application fees. Any entity asking for money is fraudulent.",
            "agent_and_intermediary_warnings": "Do not use brokers or agents; personal submission through the government portal is free and easy.",
            "hidden_costs_breakdown": [
                "Medical examination at GAMCA approved center in Pakistan (~PKR 15,000 - 22,000).",
                "Document attestation fees at IBCC, MOFA, and Arabic translation bureaus (~PKR 25,000 - 40,000).",
                "Initial out-of-pocket cash needed upon arrival in Riyadh before first stipend disbursement (~SAR 500 to 1,000; ~PKR 38,000 to 76,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Computer Science is taught in Arabic. (FACT: Coursework in the College of Computer and Information Sciences is 100% in English).",
                "CLAIM: You must know Arabic to apply for STEM. (FACT: Zero Arabic knowledge required for computer science and engineering)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial agents claim scholarships can be transferred between universities in Saudi Arabia; official regulations strictly forbid transferring scholarships between Saudi institutions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum GPA of 2.75 / 5.00 (Good standing) throughout degree studies; GPA below threshold results in academic warning and potential stipend suspension.",
            "attendance_requirements": "Mandatory regular attendance in all lectures; unexcused absence exceeding 20% leads to course denial.",
            "academic_progress_monitoring": "Semester-by-semester academic performance reviews reported to the Deanship of Admissions.",
            "work_restrictions_during_study": "Students on scholarship visa (Iqama) are strictly prohibited from taking outside commercial employment in the Kingdom.",
            "home_country_return_obligation": "Scholars must depart the Kingdom upon completion of their degree program within the period specified by Saudi regulations (typically 3 months post-graduation).",
            "service_obligations_or_bonds": "Zero service bonds or repayment requirements.",
            "repayment_clawback_conditions": "Scholarship is cancelled upon academic dismissal or violation of university regulations; past disbursed funds are not clawed back.",
            "rules_for_changing_university": "Transferring to another university within Saudi Arabia is strictly prohibited for external scholarship recipients.",
            "rules_for_changing_major": "Changing majors is permitted only within the same college during the first academic year subject to dean approval.",
            "extension_policy": "Scholarship duration cannot be extended beyond one additional semester past standard degree timeline without special Ministry of Education approval."
        },
        "official_sources_verified": [
            {
                "source_name": "Saudi Ministry of Education 'Study in Saudi' Unified External Scholarship Portal",
                "source_url": "https://studyinsaudi.moe.gov.sa/",
                "source_type": "GOVERNMENT_MINISTRY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of Pakistani bilateral quota seats distributed across specific academic colleges.",
                    "Ministry internal security clearance processing timelines.",
                    "Waitlist reallocation policies for unclaimed bilateral scholarship seats."
                ]
            },
            {
                "source_name": "Imam Mohammad Ibn Saud Islamic University Deanship of Admission and Registration",
                "source_url": "https://imamu.edu.sa/en/Pages/default.aspx",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental seat caps for international students in computing and engineering programs.",
                    "College-level English placement test exemption cutoffs for Pakistani ICS graduates."
                ]
            }
        ]
    }
}
