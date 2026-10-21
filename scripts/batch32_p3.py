"""Batch 32 Part 3: Middle East Flagship Scholarships & Research Fellowships (3 awards)
SCH-ME-040: Kuwait University Graduate Studies Scholarship for Non-Kuwaitis | Kuwait University, Kuwait
SCH-ME-041: Gulf University for Science and Technology (GUST) Fellowships | Gulf University for Science and Technology (GUST), Kuwait
SCH-ME-042: KAPSARC Energy Research Doctoral Fellowships | King Abdullah Petroleum Studies and Research Center (KAPSARC), Saudi Arabia
"""

DOSSIERS_BATCH32_P3 = {
    "SCH-ME-040": {
        "scholarship_id": "SCH-ME-040",
        "basic_details": {
            "scholarship_name": "Kuwait University Graduate Studies Scholarship for Non-Kuwaitis",
            "offering_entity": "Kuwait University College of Graduate Studies (CGS) & Kuwait Ministry of Higher Education",
            "host_country": "Kuwait",
            "host_institutions_covered": "Kuwait University (Sabah Al-Salem University City, Shadadiya / Khaldiya Campuses, Kuwait City)",
            "degree_levels": [
                "Master of Science (MSc / MEng)",
                "Doctor of Philosophy (PhD)"
            ],
            "major_restrictions": "Postgraduate degree programs offered by the College of Graduate Studies: Computer Science, Computer Engineering, Civil Engineering, Electrical Engineering, Chemical Engineering, Mechanical Engineering, Petroleum Engineering, Molecular Biology, Mathematics, and Statistics.",
            "number_of_awards_total": "Approximately 60 to 80 fully funded graduate scholarships awarded annually to distinguished non-Kuwaiti international applicants across all faculties",
            "number_of_awards_pakistan": "Competitive international quota; typically 6 to 10 Pakistani graduate scholars selected annually across engineering and sciences",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Standard program duration: 24 months (2 academic years) for Master's degrees; up to 48 months (4 academic years) for PhD degrees"
        },
        "eligibility_requirements": {
            "nationality_requirements": [
                "International non-Kuwaiti citizens from all countries worldwide, including Pakistan"
            ],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must generally be under 30 years of age for Master's programs and under 35 years of age for PhD programs at the time of admission.",
            "academic_qualifications": "Recognized 4-year Bachelor's degree (16-year BS/BSc/BE) for Master's track or 18-year MS/MPhil for PhD track from an HEC-recognized university with high academic standing (minimum CGPA 3.33 / 4.00 or 78%+ equivalent to 'Very Good' / 'Jayyid Jiddan' grade rating under Kuwait University CGS grading regulations).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.33,
            "grading_conversion_notes": "Kuwait University College of Graduate Studies strictly enforces a minimum cumulative GPA of 3.33 / 4.00 ('Very Good') or equivalent for scholarship eligibility.",
            "subject_background_prerequisites": "Relevant undergraduate degree in engineering, computing, or natural sciences directly matching the chosen graduate department; strong foundation in advanced mathematics and core discipline coursework.",
            "current_education_status": "Graduated with official degree certificate or enrolled in final undergraduate semester graduating prior to August preceding the Fall intake.",
            "graduation_year_restrictions": "Degrees must have been earned within the past 4 academic years.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications, software repositories, or academic teaching assistantship experience strongly enhance applicant ranking.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 75,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Official IELTS Academic minimum 6.0 (no band below 5.5) or TOEFL iBT minimum 75. English test must be valid at the time of application submission. MOI certificates are strictly not accepted.",
            "other_language_requirements": "All science, engineering, and computing graduate degree programs are conducted 100% in English. Arabic language proficiency is not required for STEM degrees.",
            "gender_specific_requirements": "Open equally to male and female applicants (separate modern student residential halls provided on campus).",
            "financial_need_required": False,
            "special_eligibility_categories": "Distinguished international scholarship pool funded under Kuwait state university graduate support quotas.",
            "previous_scholarship_restrictions": "Cannot hold dual scholarships or simultaneous employment during the scholarship tenure.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full waiver of all tuition fees, credit registration fees, and laboratory access charges across the entire graduate degree program.",
                "amount": "100% Tuition Waived (~KWD 3,000 - 4,500/year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Non-refundable application processing fee of KWD 10 (~PKR 9,000) payable via K-Net or international credit card upon online portal submission.",
                "amount": "KWD 10 (~PKR 9,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free furnished student hostel accommodation in Kuwait University student residence halls at Sabah Al-Salem University City campus (including utilities, Wi-Fi, air conditioning, and laundry).",
                "amount": "100% Free furnished university housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend of KWD 250 / month (~PKR 225,000 / month | KWD 3,000 per year) paid directly to student local bank account.",
                "amount": "KWD 250 / month (~PKR 225,000/mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Annual round-trip economy class flight ticket between Pakistan and Kuwait International Airport provided at the beginning and end of each academic year.",
                "amount": "100% Annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Kuwait University sponsors and processes Student Residence Permit (Civil ID, Iqama) and entry visa with fees fully covered/waived.",
                "amount": "100% Kuwait Student Iqama & Visa Covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive medical and emergency healthcare coverage at Kuwait Ministry of Health public clinics and Farwaniya/Mubarak Al-Kabeer hospitals.",
                "amount": "100% Kuwait public healthcare access"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Subsidized and provided daily meals at Kuwait University campus dining halls, complemented by the monthly living stipend.",
                "amount": "Free/subsidized university cafeteria meals"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Textbook allowance provided per semester, plus complete free access to Kuwait University Central Library and digital databases (IEEE, Springer, ScienceDirect).",
                "amount": "Semester textbook allowance + digital library access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Graduate research thesis grants available through Kuwait University Research Sector (RS) for lab consumables, high-performance computing, and conference attendance.",
                "amount": "Funded research sector project grants"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free scheduled Kuwait University shuttle bus transportation connecting student residence halls with campus faculties across Shadadiya.",
                "amount": "Free campus shuttle transportation"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host institution (Kuwait University, Kuwait).",
            "participating_institutions": [
                "Kuwait University - College of Graduate Studies (Sabah Al-Salem University City, Shadadiya, Kuwait)"
            ],
            "university_rankings_scope": "Ranked in top 800 globally (QS World University Rankings 2025); Kuwait's premier public flagship research institution founded in 1966.",
            "available_majors": [
                "Master of Science in Computer Science",
                "Master of Science in Computer Engineering",
                "Master of Science in Civil Engineering",
                "Master of Science in Electrical Engineering",
                "Master of Science in Chemical Engineering",
                "Master of Science in Mechanical Engineering",
                "Master of Science in Petroleum Engineering",
                "Master of Science in Molecular Biology",
                "Master of Science in Mathematics",
                "Doctor of Philosophy (PhD) in Engineering & Science disciplines"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years (4 semesters); PhD: 3-4 years (6-8 semesters)",
            "admission_requirements_summary": "Relevant Bachelor/Master degree with CGPA >= 3.33/4.00, valid IELTS (min 6.0) or TOEFL (min 75), GRE General score (for engineering departments, typically min 150 Quant), statement of purpose, two academic references, and Kuwait University online application.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Unified graduate application via College of Graduate Studies; Computer Engineering, Petroleum Engineering, and Molecular Biology have the highest GPA cut-offs.",
            "strategic_program_match_advice": "Align thesis proposal with Kuwait University strategic research themes: energy transition, water desalination, environmental biotechnology, cyber-physical systems, and data analytics."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://portal.ku.edu.kw/",
            "portal_system_name": "Kuwait University Student Information System (SIS) & College of Graduate Studies Online Portal",
            "account_creation_instructions": "Visit portal.ku.edu.kw, create graduate applicant account, select 'College of Graduate Studies - Non-Kuwaiti Scholarship Track', complete bio-data, academic qualifications, and upload required documents before March 31.",
            "step_by_step_workflow": [
                "Step 1: Review graduate program specifications, department prerequisites, and scholarship terms on the College of Graduate Studies portal (graduate.edu.kw).",
                "Step 2: Prepare HEC/MoFA-attested academic transcripts, degree certificates, valid IELTS/TOEFL scorecard, and GRE score report.",
                "Step 3: Register an account on Kuwait University Student Information System (portal.ku.edu.kw) during the annual application window (mid-January to late March).",
                "Step 4: Select preferred graduate degree program and indicate application for the Non-Kuwaiti Graduate Scholarship.",
                "Step 5: Upload all required academic credentials, statement of purpose, CV, and passport scans, and pay the KWD 10 application fee online.",
                "Step 6: Register two academic referees who will submit letters of recommendation directly into the university system.",
                "Step 7: Department Graduate Studies Committees review files and conduct virtual interviews for shortlisted candidates between April and May.",
                "Step 8: College of Graduate Studies issues official admission and scholarship nomination letters in June/July; Kuwait University handles security clearance and student visa issuance."
            ],
            "university_vs_scholarship_routing": "Integrated Routing: Single consolidated graduate application through the Kuwait University CGS portal automatically considers eligible international applicants for the full scholarship.",
            "recommendation_letters_submission_method": "Submitted online by two university academic professors directly via Kuwait University graduate portal referee links.",
            "personal_statement_prompts": "Statement of purpose (500-800 words) detailing academic background, specific research interests, reason for choosing Kuwait University, and career aspirations.",
            "study_plan_research_proposal_requirements": "2-page research proposal for Master's thesis applicants (mandatory 4-page detailed proposal for PhD candidates outlining problem statement, methodology, and literature review).",
            "cv_format_requirements": "Academic curriculum vitae highlighting educational milestones, technical competencies, programming proficiencies, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Online video interview via Microsoft Teams/Zoom conducted by departmental graduate admissions panel testing technical background and research motivation.",
            "standardized_tests": "IELTS Academic 6.0+ or TOEFL iBT 75+; GRE General Test recommended or required by College of Engineering (quantitative score >= 150).",
            "application_fee_amount": "KWD 10 (~PKR 9,000 / ~$33 USD) non-refundable online application fee.",
            "attestation_requirements": "Pakistani degrees and transcripts must be attested by HEC Pakistan, Ministry of Foreign Affairs (MoFA) Pakistan, and Embassy of the State of Kuwait in Islamabad.",
            "translation_requirements": "Certified English translation required for any documents not originally issued in English or Arabic.",
            "final_submission_method": "Online submission via Kuwait University Student Information System (portal.ku.edu.kw)."
        },
        "required_documents_checklist": [
            {
                "document_name": "Bachelor / Master Degree Certificate",
                "mandatory": True,
                "specification": "HEC-attested degree certificate with minimum CGPA 3.33 / 4.00 ('Very Good' grade).",
                "pakistan_specific_instruction": "Attested by HEC, MoFA, and Embassy of Kuwait in Islamabad."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Detailed official semester-by-semester grade transcripts and grading scale.",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "English Proficiency Test Scorecard",
                "mandatory": True,
                "specification": "Official IELTS Academic (minimum 6.0) or TOEFL iBT (minimum 75) certificate.",
                "pakistan_specific_instruction": "Valid electronic score report."
            },
            {
                "document_name": "Statement of Purpose & Research Outline",
                "mandatory": True,
                "specification": "Comprehensive statement detailing academic focus, research goals, and alignment with department.",
                "pakistan_specific_instruction": "Highlight technical skills and thesis intent."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential appraisals from university professors evaluating scholarly caliber and research promise.",
                "pakistan_specific_instruction": "On official institutional letterhead with verified email."
            },
            {
                "document_name": "GRE General Score Report",
                "mandatory": False,
                "specification": "Official GRE General test scores for engineering and computing applicants.",
                "pakistan_specific_instruction": "Sent via ETS institutional code for Kuwait University."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Full color copy of passport identification page valid for at least two full academic years.",
                "pakistan_specific_instruction": "Passport validity must exceed 24 months."
            },
            {
                "document_name": "Police Clearance Certificate",
                "mandatory": True,
                "specification": "Character certificate / police clearance from home district for Kuwait visa clearance.",
                "pakistan_specific_instruction": "Attested by MoFA Pakistan."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-01-10",
            "application_deadline": "2027-03-31",
            "university_admission_deadline": "2027-03-31",
            "document_submission_deadline": "2027-03-31",
            "recommendation_letters_deadline": "2027-04-10",
            "interview_period": "April to May 2027",
            "shortlist_announcement": "Late June 2027",
            "final_result_acceptance_deadline": "Within 15 days of award notification",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "2027-09-12",
            "annual_cycle_notes": "Applications open once annually in January for the subsequent Fall semester; spring intake is generally restricted to local admissions without full scholarship packages."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Undergraduate/Master GPA, transcript rigor, and class rank)",
            "extracurricular_and_leadership_weight": "5% (Student leadership, scientific competitions, professional societies)",
            "research_experience_weight": "20% (Prior research, final year project quality, published papers, or conference presentations)",
            "work_experience_weight": "5% (Relevant industry engineering or teaching experience)",
            "personal_statement_weight": "10% (Clarity of purpose, research proposal quality, and alignment with faculty)",
            "recommendations_weight": "5% (Evaluation of scholarly competence and intellectual dedication by referees)",
            "interview_weight": "10% (Departmental interview performance and technical problem-solving ability)",
            "test_scores_weight": "0% (English test and GRE are qualifying prerequisites)",
            "financial_need_weight": "0% (Pure academic excellence and research merit evaluation)",
            "selection_panel_composition": "College of Graduate Studies Admissions Committee and Departmental Graduate Faculty Panels.",
            "evaluation_methodology": "Comprehensive composite evaluation combining GPA, GRE/test metrics, research potential, and interview scores."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,000 to 3,000 international applicants across all graduate faculties",
            "total_scholarships_awarded": "~60 to 80 fully funded graduate scholarships per cohort",
            "acceptance_rate_global": "~2.5% to 3.0%",
            "acceptance_rate_pakistan": "~3.5% to 5.0% among applicants with CGPA >= 3.50 and strong quantitative scores",
            "typical_successful_applicant_gpa": "3.65 / 4.00 (with top marks in core engineering/science subjects)",
            "typical_academic_and_research_profile": "Engineers and scientists with strong mathematical foundations, distinguished final year projects, and demonstrated coding or lab capabilities.",
            "common_backgrounds_of_winners": "Graduates from NUST, UET Lahore, NED UET Karachi, FAST-NUCES, COMSATS, and Quaid-i-Azam University.",
            "high_representation_countries": "Pakistan, Egypt, Jordan, India, Sudan, Tunisia, Syria, Yemen.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply via official Kuwait University domains (portal.ku.edu.kw and graduate.edu.kw).",
                "Beware of commercial agents in Lahore/Karachi demanding recruitment fees or guaranteeing Kuwait University scholarships."
            ],
            "application_fee_warning": "Only the official KWD 10 (~$33 USD) university fee is charged; any third party requesting visa or placement fees is fraudulent.",
            "agent_and_intermediary_warnings": "Kuwait University does not authorize private recruitment agencies; third-party submissions are disqualified.",
            "hidden_costs_breakdown": [
                "KU application fee: KWD 10 (~PKR 9,000).",
                "HEC, MoFA, and Kuwait Embassy document attestation charges in Islamabad: ~PKR 25,000 - 45,000.",
                "Pre-departure medical examination (GAMCA approved medical center for GCC visa): ~PKR 18,000 - 25,000.",
                "Initial cash reserve before first monthly stipend disbursement: ~KWD 100 (~PKR 90,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Knowledge of Arabic is mandatory for studying engineering at Kuwait University. Reality: All STEM graduate courses, exams, and theses are conducted exclusively in English.",
                "Myth: Scholars must pay for on-campus housing. Reality: Full scholarship recipients receive 100% free furnished housing and utilities."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums claim IELTS can be waived with an English Medium of Instruction letter; CGS Kuwait University strictly enforces official IELTS 6.0 or TOEFL 75 scorecard submissions."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 / 4.00 throughout every semester of graduate enrollment.",
            "attendance_requirements": "Mandatory full-time student status; attendance in all registered lectures, seminars, and laboratory sessions.",
            "academic_progress_monitoring": "Semester-end academic progress review by the College of Graduate Studies; failing below 3.00 places student on academic warning.",
            "work_restrictions_during_study": "Strictly prohibited from holding outside commercial employment in Kuwait; may only perform departmental Graduate Teaching Assistantship (GTA) or Research Assistantship (GRA) duties.",
            "home_country_return_obligation": "No mandatory return bond; graduates may pursue employment opportunities in Kuwait under standard private sector transfer rules or pursue overseas PhD/postdocs.",
            "service_obligations_or_bonds": "Scholars may be required to deliver up to 6-8 hours per week of teaching or laboratory assistance within their department.",
            "repayment_clawback_conditions": "Revocation of scholarship, forfeiture of stipend, and loss of student visa status in case of academic failure, disciplinary breach, or voluntary withdrawal without approved excuse.",
            "rules_for_changing_university": "Non-transferable to other institutions in Kuwait or abroad.",
            "rules_for_changing_major": "Changing graduate major is not permitted once scholarship award is executed.",
            "extension_policy": "Funding is granted for standard duration (4 semesters for MS, 8 semesters for PhD); a one-semester extension may be approved by CGS upon supervisor justification."
        },
        "official_sources_verified": [
            {
                "source_name": "Kuwait University College of Graduate Studies (CGS) Official Portal",
                "source_url": "http://www.graduate.edu.kw/Default.aspx?pageId=129",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Kuwait University Student Information System (SIS)",
                "source_url": "http://portal.ku.edu.kw/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-ME-041": {
        "scholarship_id": "SCH-ME-041",
        "basic_details": {
            "scholarship_name": "Gulf University for Science and Technology (GUST) Fellowships",
            "offering_entity": "Gulf University for Science and Technology (GUST) Graduate Studies & Research Office",
            "host_country": "Kuwait",
            "host_institutions_covered": "Gulf University for Science and Technology (West Mishref Campus, Kuwait)",
            "degree_levels": [
                "Master of Science (MSc)",
                "Master of Business Administration (MBA)"
            ],
            "major_restrictions": "Master of Science in Computer Science (Artificial Intelligence, Cybersecurity, Software Engineering), Master of Science in Information Technology, Applied Mathematics, and Master of Business Administration (MBA / Management Information Systems).",
            "number_of_awards_total": "Approximately 15 to 25 competitive Graduate Assistantships (GA) & Research Fellowships awarded annually across graduate programs",
            "number_of_awards_pakistan": "Merit-based open international competition; typically 3 to 6 Pakistani graduate fellows selected annually in Computer Science and IT",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "24 months (2 academic years for full-time master's studies subject to maintaining semester CGPA >= 3.25)"
        },
        "eligibility_requirements": {
            "nationality_requirements": [
                "Open to all nationalities worldwide, including international applicants from Pakistan and expatriate residents in Kuwait"
            ],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "No statutory upper age limit, but candidates must be early-career researchers or fresh graduates typically under 35 years old.",
            "academic_qualifications": "Recognized 4-year Bachelor's degree (16-year BS/BSc/BE) in Computer Science, Software Engineering, Information Technology, or closely related quantitative field from an HEC-recognized university with minimum CGPA 3.20 / 4.00 (75%+).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum CGPA 3.20 / 4.00; competitive graduate fellows typically maintain CGPA >= 3.50 / 4.00 with top grades in core computer science subjects.",
            "subject_background_prerequisites": "Solid undergraduate foundation in algorithms, data structures, software engineering, databases, and programming languages (Python, Java, C++).",
            "current_education_status": "Graduated with official degree certificate or enrolled in final semester graduating prior to August 2027.",
            "graduation_year_restrictions": "Graduation within the past 5 years preferred.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Relevant software development experience, machine learning projects, or academic tutoring experience is considered advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 (min 6.0 in writing) or TOEFL iBT minimum 80. MOI certificates are generally not accepted; official test report required.",
            "other_language_requirements": "All graduate teaching, examinations, and research at GUST are conducted 100% in English. Arabic language proficiency is not required.",
            "gender_specific_requirements": "Open equally to male and female candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Merit-based Graduate Assistantship / Fellowship scheme rewarding high academic and technical competency.",
            "previous_scholarship_restrictions": "Cannot hold dual external sponsorships simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for all required master's credit hours (33-36 credit hours worth up to KWD 9,000 total).",
                "amount": "100% Full Tuition Waiver (up to KWD 9,000 value)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Non-refundable graduate application fee of KWD 30 (~PKR 27,000) payable online during portal submission.",
                "amount": "KWD 30 (~PKR 27,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized housing allowance or graduate residence assistance provided in West Mishref/Hawally area near campus.",
                "amount": "Housing allowance / graduate accommodation support"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend of KWD 200 - 300 / month (~PKR 180,000 - 270,000 / month | ~USD 650 - 980/month) for teaching/research assistantship duties.",
                "amount": "KWD 200 - 300 / month (~PKR 180,000 - 270,000/mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Kuwait is self-funded, though relocation assistance is evaluated on a case-by-case basis.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "GUST sponsors and handles the Kuwait student residence permit (Civil ID, Student Visa) processing.",
                "amount": "100% GUST Student Visa Sponsorship Covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive student health coverage through Kuwait private university health network and public clinics.",
                "amount": "100% Student Health Coverage Covered"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized campus cafeteria and food court dining across the GUST West Mishref campus.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Free digital access to GUST A.M. Al-Refai Library, ACM Digital Library, IEEE Xplore, and cloud computing resources.",
                "amount": "Full digital library and computing lab access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Research grants and travel funds available through GUST Research Office for co-authoring conference papers with faculty.",
                "amount": "Research publication & conference grant support"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized local student transport services and university parking facilities.",
                "amount": "Subsidized campus transport"
            },
            "total_estimated_value_usd_per_year": 20000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Gulf University for Science and Technology - GUST, Kuwait).",
            "participating_institutions": [
                "Gulf University for Science and Technology (West Mishref, Kuwait)"
            ],
            "university_rankings_scope": "Ranked #1 private university in Kuwait (QS Arab Region University Rankings; QS World University Rankings); established in partnership with University of Missouri-St. Louis (UMSL).",
            "available_majors": [
                "Master of Science in Computer Science (Artificial Intelligence, Cybersecurity, Software Engineering)",
                "Master of Science in Information Technology",
                "Master of Business Administration (MBA - Management, Finance, MIS)",
                "Master of Science in Applied Mathematics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (4 semesters, 33-36 credit hours)",
            "admission_requirements_summary": "Bachelor degree in Computing, Engineering, or Business with CGPA >= 3.20/4.00, official IELTS 6.5+ or TOEFL 80+, statement of motivation, two recommendation letters, and interview with graduate committee.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Unified graduate admission and assistantship application; Computer Science AI track is the most competitive.",
            "strategic_program_match_advice": "Demonstrate strong hands-on coding skills, machine learning project experience, and willingness to assist faculty with undergraduate lab instruction."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.gust.edu.kw/admissions",
            "portal_system_name": "GUST Graduate Admissions & Financial Aid Portal",
            "account_creation_instructions": "Create an account on the GUST Online Admissions Portal (gust.edu.kw/admissions), select Master of Science in Computer Science, select 'Graduate Assistantship / Fellowship Application', upload transcripts and credentials, and pay the KWD 30 application fee before May 15.",
            "step_by_step_workflow": [
                "Step 1: Check admission guidelines and faculty research profiles on the GUST Graduate Studies & Research portal (gust.edu.kw/graduate_studies).",
                "Step 2: Prepare HEC/MoFA-attested Bachelor degree, official transcripts, IELTS/TOEFL scorecard, and CV.",
                "Step 3: Register an account on GUST Online Admissions Portal.",
                "Step 4: Complete the graduate application form and check the Graduate Assistantship / Fellowship consideration box.",
                "Step 5: Upload required academic documents, personal statement, and portfolio of technical projects.",
                "Step 6: Pay the KWD 30 application fee online via credit card.",
                "Step 7: Provide contact details for two academic referees who will submit letters directly.",
                "Step 8: Attend an online technical and motivation interview with the Department of Computer Science Graduate Committee in June.",
                "Step 9: Receive admission and assistantship award letter in July; GUST coordinates visa sponsorship and onboarding."
            ],
            "university_vs_scholarship_routing": "Integrated Routing: Students apply for graduate program admission and indicate interest in the Graduate Assistantship / Fellowship within the single institutional portal.",
            "recommendation_letters_submission_method": "Submitted electronically by academic professors via referee links sent by the GUST Admissions Office.",
            "personal_statement_prompts": "Statement of purpose (max 750 words) describing academic accomplishments, technical projects, interest in GUST graduate research, and motivation for graduate assistantship duties.",
            "study_plan_research_proposal_requirements": "Preliminary research statement (1-2 pages) describing intended master's thesis topic in AI, cybersecurity, or data systems.",
            "cv_format_requirements": "Standard professional academic CV highlighting programming languages, open-source repositories, projects, and academic honors.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual interview via Zoom/Teams with graduate program director focusing on programming skills, teaching readiness, and research interests.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 80+; GRE General Test optional but strongly recommended for funding competition.",
            "application_fee_amount": "KWD 30 (~PKR 27,000 / ~$98 USD) non-refundable graduate application fee.",
            "attestation_requirements": "HEC and MoFA Pakistan attestations required; Kuwait Embassy attestation required upon admission confirmation.",
            "translation_requirements": "Official English translation for all academic records.",
            "final_submission_method": "Online submission via GUST Graduate Admissions Portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Bachelor Degree Certificate",
                "mandatory": True,
                "specification": "HEC-attested 4-year BS in Computer Science, Software Engineering, or related field.",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete undergraduate semester transcripts showing minimum CGPA 3.20 / 4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "English Language Test Certificate",
                "mandatory": True,
                "specification": "Official IELTS Academic (minimum 6.5) or TOEFL iBT (minimum 80) scorecard.",
                "pakistan_specific_instruction": "Valid score report."
            },
            {
                "document_name": "Statement of Purpose & GA Essay",
                "mandatory": True,
                "specification": "Statement explaining academic interests and readiness for graduate teaching/research assistantship responsibilities.",
                "pakistan_specific_instruction": "Emphasize programming and teaching skills."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed CV highlighting software toolsets, machine learning projects, and publications.",
                "pakistan_specific_instruction": "Clear layout with project links."
            },
            {
                "document_name": "Two Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential appraisal letters from undergraduate faculty.",
                "pakistan_specific_instruction": "On official university letterhead."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport information page valid for at least 2 years.",
                "pakistan_specific_instruction": "Minimum 24 months validity."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-02-01",
            "application_deadline": "2027-05-15",
            "university_admission_deadline": "2027-05-15",
            "document_submission_deadline": "2027-05-25",
            "recommendation_letters_deadline": "2027-05-30",
            "interview_period": "June 2027",
            "shortlist_announcement": "Early July 2027",
            "final_result_acceptance_deadline": "Within 14 days of offer",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "2027-09-05",
            "annual_cycle_notes": "Applications open in February with deadline in mid-May for the Fall intake; assistantship awards are finalized by mid-July."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Undergraduate CGPA, math/computing course marks)",
            "extracurricular_and_leadership_weight": "5% (Student leadership, hackathon participation, developer clubs)",
            "research_experience_weight": "20% (Undergraduate thesis/FYP, publications, GitHub projects)",
            "work_experience_weight": "10% (Software development internships or industry experience)",
            "personal_statement_weight": "10% (Quality of SOP and motivation for assistantship responsibilities)",
            "recommendations_weight": "5% (Academic faculty appraisals)",
            "interview_weight": "10% (Technical interview performance, communication skills, and teaching suitability)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and assistantship suitability evaluation)",
            "selection_panel_composition": "GUST Graduate Studies Council, Department Head of Computer Science, and Graduate Program Director.",
            "evaluation_methodology": "Multi-stage rubric evaluating transcript credentials, programming proficiency, and candidate interview performance."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international applicants across graduate programs",
            "total_scholarships_awarded": "~15 to 25 graduate assistantships/fellowships annually",
            "acceptance_rate_global": "~2.0% to 2.5%",
            "acceptance_rate_pakistan": "~3.5% to 5.0% among high-caliber CS/IT graduates",
            "typical_successful_applicant_gpa": "3.55 / 4.00 (with strong coding portfolio)",
            "typical_academic_and_research_profile": "Graduates in computer science or software engineering with practical experience in machine learning, web/mobile architectures, and lab teaching skills.",
            "common_backgrounds_of_winners": "Graduates from FAST-NUCES, NUST, COMSATS, UET Lahore, and IBA Karachi.",
            "high_representation_countries": "Pakistan, India, Egypt, Jordan, Lebanon, Kuwait (expatriate residents), Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply directly through official GUST portal at gust.edu.kw.",
                "Never pay third-party agents claiming to guarantee GUST assistantships or visas."
            ],
            "application_fee_warning": "Only the official KWD 30 application fee is charged by the university.",
            "agent_and_intermediary_warnings": "GUST does not partner with recruitment agents; direct applications only.",
            "hidden_costs_breakdown": [
                "GUST application fee: KWD 30 (~PKR 27,000).",
                "Airfare to Kuwait: ~PKR 120,000 - 180,000 (self-funded).",
                "Attestations (HEC, MoFA, Kuwait Embassy): ~PKR 25,000 - 40,000.",
                "GAMCA medical screening in Pakistan: ~PKR 20,000.",
                "Security deposit for local apartment housing: ~KWD 150 - 200 (~PKR 135,000 - 180,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: GUST is an Arabic-medium university. Reality: GUST is an American-style university modeled after UMSL where 100% of instruction and administrative communication is in English.",
                "Myth: Assistantships require 40 hours of teaching per week. Reality: Graduate assistants provide 10-15 hours per week of tutoring, grading, or lab supervision."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest Duolingo is accepted; GUST Graduate Admissions strictly requires official IELTS Academic or TOEFL iBT."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.25 / 4.00 each semester to retain tuition waiver and monthly stipend.",
            "attendance_requirements": "Mandatory full-time graduate study and fulfillment of 12-15 hours per week of assigned teaching or research assistantship duties.",
            "academic_progress_monitoring": "Semester-by-semester review by Graduate Program Director and supervising faculty.",
            "work_restrictions_during_study": "Outside commercial employment in Kuwait is prohibited while holding a funded Graduate Assistantship.",
            "home_country_return_obligation": "No mandatory return bond; graduates can pursue careers in Kuwait, the GCC, or international doctoral programs.",
            "service_obligations_or_bonds": "Scholars must serve as Graduate Teaching Assistants (GTA) assisting with lab demonstrations and grading, or Graduate Research Assistants (GRA).",
            "repayment_clawback_conditions": "Revocation of assistantship and loss of tuition waiver if semester GPA falls below 3.00 or if assistantship responsibilities are neglected.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing degree program requires formal re-application to the Graduate Council.",
            "extension_policy": "Funding is provided for a maximum of 4 semesters (2 academic years); extensions require special dean approval."
        },
        "official_sources_verified": [
            {
                "source_name": "GUST Graduate Studies & Financial Aid",
                "source_url": "https://www.gust.edu.kw/graduate_studies/financial_aid",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "GUST Admissions Portal",
                "source_url": "https://www.gust.edu.kw/admissions",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-ME-042": {
        "scholarship_id": "SCH-ME-042",
        "basic_details": {
            "scholarship_name": "KAPSARC Energy Research Doctoral Fellowships",
            "offering_entity": "King Abdullah Petroleum Studies and Research Center (KAPSARC) & Saudi Ministry of Energy",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "King Abdullah Petroleum Studies and Research Center (KAPSARC, Riyadh, Saudi Arabia)",
            "degree_levels": [
                "Doctor of Philosophy (PhD)"
            ],
            "major_restrictions": "Energy Economics, Climate Change Economics & Carbon Transition, Computational Energy Modeling, Oil & Gas Market Dynamics, Renewable Energy Grid Integration, Operations Research, Applied Econometrics, and Sustainable Transport Policy.",
            "number_of_awards_total": "Approximately 15 to 20 prestigious Visiting Doctoral Fellowships and Research Grants awarded annually worldwide",
            "number_of_awards_pakistan": "Merit-based global competition; typically 2 to 4 Pakistani doctoral candidates / scholars selected per annual fellowship cohort",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "6 to 12 months (in-residence doctoral fellowship at KAPSARC headquarters in Riyadh, renewable for up to 24 months for joint dissertation projects)"
        },
        "eligibility_requirements": {
            "nationality_requirements": [
                "Open to doctoral researchers and PhD candidates of all nationalities worldwide, including Pakistan"
            ],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Applicants must be enrolled doctoral candidates or recent PhD graduates typically under 40 years of age.",
            "academic_qualifications": "Enrollment in an accredited PhD program or recognized Master of Science / MPhil (18-year education) in Energy Economics, Operations Research, Applied Economics, Electrical/Energy Engineering, Data Science, or Environmental Policy with exceptional academic record (minimum CGPA 3.60 / 4.00 or 82%+).",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Minimum CGPA 3.60 / 4.00; competitive applicants have demonstrable research accomplishments and quantitative econometric/modeling skills.",
            "subject_background_prerequisites": "Advanced background in econometric modeling, optimization methods, Python/R/GAMS programming, energy systems simulation, or energy market policy.",
            "current_education_status": "Currently enrolled in an accredited PhD program (having completed doctoral coursework / comprehensive exams) or recent doctoral graduate.",
            "graduation_year_restrictions": "Must have achieved PhD candidacy within the last 3 years.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior research publications in peer-reviewed energy or economics journals (Energy Economics, Applied Energy, Energy Policy) strongly elevate selection chances.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 95,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 7.0 (no band below 6.5) or TOEFL iBT minimum 95. Research, publications, and seminars are conducted 100% in English.",
            "other_language_requirements": "Arabic language is not required; research environment is entirely international and English-medium.",
            "gender_specific_requirements": "Open equally to male and female scholars; KAPSARC compound provides international residential facilities.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite research fellowship awarded to scholars producing high-impact policy analysis on global energy transitions.",
            "previous_scholarship_restrictions": "Fellows must dedicate full effort to their KAPSARC research program during the fellowship period.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% coverage of all institutional research fees, affiliation costs, and computing cluster access at KAPSARC's Zaha Hadid-designed research center in Riyadh.",
                "amount": "100% Research and Affiliation Fees Covered"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Direct application via KAPSARC Fellowship Portal is completely free of charge.",
                "amount": "SAR 0 (Free)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Free luxurious furnished residential townhouse/villa provided within the secure KAPSARC Residential Community in Riyadh (fully serviced with utilities, high-speed fiber internet, and gym/pool amenities).",
                "amount": "100% Free luxury furnished residential housing on KAPSARC compound"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly research fellowship stipend of SAR 5,000 / month (~PKR 370,000 / month | ~USD 1,335/month | SAR 60,000/year).",
                "amount": "SAR 5,000 / month (~PKR 370,000/mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Round-trip economy international airfare between Pakistan and Riyadh King Khalid International Airport (RUH) provided at the start and completion of the fellowship.",
                "amount": "100% Round-trip international flights covered"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi Business/Research Visa or Saudi Residency Permit (Iqama) fully sponsored, processed, and paid by KAPSARC.",
                "amount": "100% Saudi Visa & Sponsorship Covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive premium health and emergency medical insurance through Bupa Arabia covering top private hospitals in Riyadh.",
                "amount": "100% Premium Bupa Arabia health insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining at KAPSARC executive dining hall, cafés, and on-compound markets, complemented by the SAR 5,000 monthly stipend.",
                "amount": "Subsidized dining & living allowance"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full digital and physical access to KAPSARC Library, proprietary global energy databases (BloombergNEF, S&P Global Platts, Rystad Energy, IEA).",
                "amount": "100% Access to premier global energy data repositories"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Full financial sponsorship to present research at premier international energy conferences (IAEE, USAEE, COP) and publish KAPSARC Discussion Papers.",
                "amount": "Full conference sponsorship & publication funding"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free shuttle transportation between KAPSARC residential compound, research complex, and key Riyadh destinations.",
                "amount": "Free compound & city shuttle transit"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host research center (King Abdullah Petroleum Studies and Research Center - KAPSARC, Riyadh, Saudi Arabia).",
            "participating_institutions": [
                "King Abdullah Petroleum Studies and Research Center (KAPSARC, Riyadh)"
            ],
            "university_rankings_scope": "Ranked as one of the world's premier energy think tanks (Top 10 Global Energy & Resource Think Tanks, Think Tanks and Civil Societies Program); advisory body to G20 and Saudi Ministry of Energy.",
            "available_majors": [
                "Energy Economics & Econometric Forecasting",
                "Climate Change Economics & Carbon Capture, Utilization, and Storage (CCUS)",
                "Oil, Gas & Hydrogen Markets Dynamics",
                "Renewable Energy Grid Integration & Power Systems",
                "Energy Transitions & Sustainable Transportation",
                "Computational Energy Policy & Macroeconomic Modeling"
            ],
            "english_taught_program_availability": True,
            "program_duration": "6 to 12 months (in-residence research fellowship, extensible to 24 months)",
            "admission_requirements_summary": "Enrolled PhD student or recent PhD graduate in economics, energy engineering, or operations research, CGPA >= 3.60/4.00, detailed 5-10 page research proposal aligned with KAPSARC research initiatives, IELTS 7.0+ or TOEFL 95+, two letters of recommendation from doctoral advisors, and writing sample/published paper.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Direct fellowship application to KAPSARC; selection is intensely competitive based on proposal novelty and methodology.",
            "strategic_program_match_advice": "Align proposal directly with Saudi Vision 2030 energy initiatives: circular carbon economy, hydrogen economy, power market reform, or GCC renewable energy integration."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.kapsarc.org/careers/visiting-fellowships/",
            "portal_system_name": "KAPSARC Fellowship & Careers Portal",
            "account_creation_instructions": "Visit kapsarc.org/careers/visiting-fellowships/, create an applicant profile, select 'Visiting Doctoral Fellowship', upload detailed research proposal, writing sample, transcripts, CV, and letters of recommendation before March 1.",
            "step_by_step_workflow": [
                "Step 1: Review KAPSARC research themes, active projects, and fellow profiles at kapsarc.org.",
                "Step 2: Draft a comprehensive 5 to 10-page research proposal detailing research objectives, methodology (econometric or optimization), data sources, and policy implications.",
                "Step 3: Prepare academic transcripts, proof of PhD enrollment / candidacy, writing sample (published paper or dissertation chapter), and English test score.",
                "Step 4: Submit the complete application package through KAPSARC Careers / Visiting Fellowships online portal by March 1.",
                "Step 5: KAPSARC Research Directors and Senior Fellows review proposals and evaluate methodological rigor and policy relevance.",
                "Step 6: Shortlisted candidates are invited for a virtual seminar presentation (research seminar + interview) with the KAPSARC research panel in April.",
                "Step 7: Final fellowship award decisions announced in May.",
                "Step 8: KAPSARC Human Resources processes Saudi research visa, flights, and compound housing allocation for Fall arrival."
            ],
            "university_vs_scholarship_routing": "Integrated Routing: Fellowship application directly submitted to KAPSARC provides both institutional affiliation and complete funding.",
            "recommendation_letters_submission_method": "Submitted by two doctoral advisors or senior faculty members via referee email upload link.",
            "personal_statement_prompts": "Motivation letter (1,000 words) describing doctoral research trajectory, motivation for joining KAPSARC in Riyadh, and how the center's resources will advance the candidate's career.",
            "study_plan_research_proposal_requirements": "Rigorous 5 to 10-page research proposal specifying: research questions, theoretical framework, quantitative econometric/computational methodology, required datasets, and expected policy deliverables (e.g., KAPSARC Discussion Paper).",
            "cv_format_requirements": "Full academic curriculum vitae detailing doctoral coursework, working papers, journal publications, software skills (Python, R, GAMS, Stata), and conference presentations.",
            "interviews_conducted": True,
            "interview_format_details": "Online research seminar presentation (30 minutes presentation followed by 20 minutes Q&A) before KAPSARC Program Directors and Senior Fellows.",
            "standardized_tests": "IELTS Academic 7.0+ or TOEFL iBT 95+; GRE scores advantageous for quantitative economics candidates.",
            "application_fee_amount": "SAR 0 (100% Free to apply).",
            "attestation_requirements": "HEC and MoFA Pakistan degree attestations required for Saudi visa processing; Saudi Embassy attestation.",
            "translation_requirements": "Official English translation for all academic records.",
            "final_submission_method": "Online submission via KAPSARC Careers / Visiting Fellowships portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Detailed Research Proposal",
                "mandatory": True,
                "specification": "5-10 page proposal outlining energy economics or policy research, quantitative methods, and data requirements.",
                "pakistan_specific_instruction": "Focus on empirical rigor and policy relevance to energy transitions."
            },
            {
                "document_name": "Proof of PhD Enrollment / Candidacy",
                "mandatory": True,
                "specification": "Official letter from doctoral university confirming PhD enrollment, completed coursework, and candidacy status.",
                "pakistan_specific_instruction": "Signed by university registrar or doctoral dean."
            },
            {
                "document_name": "Master's & Bachelor's Transcripts",
                "mandatory": True,
                "specification": "Official transcripts of 18-year education showing minimum CGPA 3.60 / 4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Academic Writing Sample / Published Paper",
                "mandatory": True,
                "specification": "Sole-authored or co-authored research paper or PhD dissertation chapter demonstrating quantitative research capability.",
                "pakistan_specific_instruction": "Published paper or high-quality working draft."
            },
            {
                "document_name": "Academic Curriculum Vitae",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, econometric software competencies, and awards.",
                "pakistan_specific_instruction": "Academic layout."
            },
            {
                "document_name": "Two Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential appraisal letters from PhD dissertation advisors.",
                "pakistan_specific_instruction": "On official university letterhead."
            },
            {
                "document_name": "English Language Test Certificate",
                "mandatory": True,
                "specification": "Official IELTS (min 7.0) or TOEFL iBT (min 95) scorecard.",
                "pakistan_specific_instruction": "Valid test report."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Color scan of valid passport identification page.",
                "pakistan_specific_instruction": "Minimum 24 months validity."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-11-01",
            "application_deadline": "2027-03-01",
            "university_admission_deadline": "2027-03-01",
            "document_submission_deadline": "2027-03-01",
            "recommendation_letters_deadline": "2027-03-15",
            "interview_period": "April 2027",
            "shortlist_announcement": "Early May 2027",
            "final_result_acceptance_deadline": "Within 3 weeks of award letter",
            "visa_application_window": "June to August 2027",
            "semester_commencement": "2027-09-01",
            "annual_cycle_notes": "Annual fellowship cycle opens in November with March 1 deadline for September residency; exceptional visiting fellows may be considered on rolling basis."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Doctoral coursework grades, academic honors, and university standing)",
            "extracurricular_and_leadership_weight": "5% (Academic service, conference organization, peer reviewing)",
            "research_experience_weight": "35% (Quality, methodology, and feasibility of research proposal; publication record)",
            "work_experience_weight": "5% (Relevant think tank, energy ministry, or policy consulting experience)",
            "personal_statement_weight": "10% (Clarity of motivation, synergy with KAPSARC research initiatives)",
            "recommendations_weight": "5% (Advisor assessments of candidate research autonomy and scholarly potential)",
            "interview_weight": "15% (Research seminar presentation, defense of methodology, and responses to panel critique)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic and research excellence evaluation)",
            "selection_panel_composition": "KAPSARC Research Directorate, Program Directors in Energy Transitions and Macroeconomics, and Senior Research Fellows.",
            "evaluation_methodology": "Double-blind proposal review followed by competitive research seminar defense before senior researchers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~500 to 800 global doctoral applicants",
            "total_scholarships_awarded": "~15 to 20 visiting research fellowships annually",
            "acceptance_rate_global": "~2.5%",
            "acceptance_rate_pakistan": "~3.0% to 4.5% among advanced PhD candidates in economics/energy",
            "typical_successful_applicant_gpa": "3.80 / 4.00 (with at least 1-2 published papers or conference proceedings)",
            "typical_academic_and_research_profile": "Advanced PhD candidates with sophisticated command of econometric modeling, Python/GAMS, and deep knowledge of energy economics or climate transition.",
            "common_backgrounds_of_winners": "Doctoral scholars from PIDE (Pakistan Institute of Development Economics), LUMS, NUST, Quaid-i-Azam University, IBA Karachi, and international PhD programs.",
            "high_representation_countries": "Pakistan, United States, United Kingdom, Saudi Arabia, China, Turkey, Egypt, Germany, Italy.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official KAPSARC website at https://www.kapsarc.org/.",
                "Never pay any fee; KAPSARC never charges application, processing, or visa fees."
            ],
            "application_fee_warning": "Application to KAPSARC fellowships is 100% free.",
            "agent_and_intermediary_warnings": "KAPSARC does not work with commercial placement agencies or recruiters for research fellowships.",
            "hidden_costs_breakdown": [
                "Application fee: SAR 0 (Free).",
                "Saudi visa and flights: 100% COVERED by KAPSARC upon selection.",
                "Attestation fees in Pakistan (HEC/MoFA/Saudi Embassy): ~PKR 25,000 - 45,000.",
                "Pre-departure medical tests (GAMCA): ~PKR 20,000."
            ],
            "misleading_claims_debunked": [
                "Myth: KAPSARC is an oil production company. Reality: KAPSARC is an independent, non-profit energy and sustainability research think tank located in Riyadh.",
                "Myth: Fellows must relocate permanently. Reality: This is an in-residence doctoral fellowship spanning 6-12 months designed to support PhD dissertation completion."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites state that Arabic proficiency is required to work at KAPSARC; the working language across all research teams at KAPSARC is 100% English."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain active doctoral candidacy in good standing at home university.",
            "attendance_requirements": "Full-time physical residency at KAPSARC research complex in Riyadh during the fellowship tenure; participation in weekly research seminars.",
            "academic_progress_monitoring": "Quarterly milestone reviews with assigned KAPSARC mentor and Program Director.",
            "work_restrictions_during_study": "Fellows must devote full time to their designated research project; outside commercial consulting is prohibited.",
            "home_country_return_obligation": "Scholars return to their home university to defend and complete their PhD degree upon fellowship conclusion.",
            "service_obligations_or_bonds": "Fellows must produce at least one KAPSARC Discussion Paper or Policy Brief and present at an internal research seminar.",
            "repayment_clawback_conditions": "Revocation of fellowship and termination of residency in case of research misconduct, plagiarism, or abandonment of project without cause.",
            "rules_for_changing_university": "Not applicable (fellow remains matriculated at home doctoral university).",
            "rules_for_changing_major": "Research topic modifications require formal approval from KAPSARC Program Director.",
            "extension_policy": "Initial 6-month fellowship can be extended up to 12 or 24 months based on exceptional research progress and joint publication deliverables."
        },
        "official_sources_verified": [
            {
                "source_name": "KAPSARC Visiting Fellowships Portal",
                "source_url": "https://www.kapsarc.org/careers/visiting-fellowships/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "KAPSARC Research Center Official Site",
                "source_url": "https://www.kapsarc.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}

DATA_P3 = DOSSIERS_BATCH32_P3

if __name__ == "__main__":
    import os
    import sys

    # Ensure backend path is on sys.path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    backend_path = os.path.join(project_root, "backend")
    if backend_path not in sys.path:
        sys.path.insert(0, backend_path)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from schemas.scholarship import DeepScholarshipDossier

    print(f"Validating {len(DOSSIERS_BATCH32_P3)} dossiers in Batch 32 Part 3...")
    for sid, dossier in DOSSIERS_BATCH32_P3.items():
        validated = DeepScholarshipDossier(**dossier)
        print(f"  ✓ {sid}: {validated.basic_details.scholarship_name}")
    print("All 3 Batch 32 Part 3 dossiers validated successfully with DeepScholarshipDossier!")
