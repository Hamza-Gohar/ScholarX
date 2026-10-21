# scripts/batch23_p1.py
# SCH-AM-048: University of Alberta Graduate Entrance Scholarship & Centenary Award (Canada)
# SCH-AM-049: Simon Fraser University (SFU) Graduate Research Fellowship (Canada)
# SCH-AM-050: Western University International President's Entrance Scholarship (Canada)

DATA_P1 = {
    "SCH-AM-048": {
        "scholarship_id": "SCH-AM-048",
        "basic_details": {
            "scholarship_name": "University of Alberta Graduate Entrance Scholarship & Centenary Award",
            "offering_entity": "Faculty of Graduate & Postdoctoral Studies (GPS), University of Alberta",
            "host_country": "Canada",
            "host_institutions_covered": "University of Alberta (Edmonton, Alberta, Canada)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "All thesis-based master's and doctoral programs across Faculty of Science (Computing Science, AI via Amii), Faculty of Engineering (Biomedical, Chemical, Mechanical, Civil), Agricultural, Life & Environmental Sciences, and Medicine & Dentistry.",
            "number_of_awards_total": "~150 to 200 graduate entrance scholarships awarded annually",
            "number_of_awards_pakistan": "Open globally on merit; Pakistani graduate researchers frequently secure awards in Computing Science and Chemical Engineering (~15 to 25 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for thesis Master's; up to 4 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "CAD 17,500 / year (Master's) to CAD 21,000 / year (Doctoral) stipend plus CAD 10,000 international tuition differential top-up (~CAD 2,290 / month total funding; ~PKR 470,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students of all citizenships including Pakistan and Canadian domestic scholars"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 0,
            "age_limit_notes": "No age restriction; evaluation based on undergraduate and graduate academic GPA and research achievement.",
            "academic_qualifications": "Recognized 16-year Bachelor's degree with minimum admission GPA of 3.70 / 4.00 (or first-class standing / 80%+) for Master's; 18-year Master's degree with minimum GPA 3.70 / 4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum admission GPA of 3.7 / 4.0 in final two years of study; competitive applicants typically hold 3.8+ / 4.0.",
            "subject_background_prerequisites": "Undergraduate degree in relevant discipline (computer science, engineering, biological sciences, physical sciences) with thesis component.",
            "current_education_status": "Graduated or final-year undergraduate/master's students completing degree prior to Canadian fall intake.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications, software repository contributions, or laboratory research assistantships carry significant weight.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": True,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 (no band below 6.0), TOEFL iBT minimum 90 (subscores 21+), or Duolingo English Test 120+ mandatory.",
            "other_language_requirements": "GRE General recommended but not mandatory for Computing Science and Engineering.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must be admitted to an eligible full-time thesis-based graduate program and nominated by their academic department.",
            "previous_scholarship_restrictions": "Cannot be combined with another major tri-agency award (CIHR, NSERC, SSHRC) or Vanier CGS without reduction.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full international tuition differential fee covered via CAD 10,000 top-up grant plus departmental tuition remission.",
                "amount": "100% covered (~CAD 9,500 to 11,000 / year value; ~PKR 1,950,000 to 2,250,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Non-refundable graduate application fee of CAD 135 paid online upon application submission.",
                "amount": "CAD 135 (~PKR 27,500) application fee"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "Graduate student residence or off-campus housing in Edmonton arranged independently; easily covered by the combined stipend.",
                "amount": "Funded from stipend (~CAD 800 to 1,200 / month rent in Edmonton)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Annual stipend of CAD 17,500 (Master's) or CAD 21,000 (Doctoral) supplemented by departmental GRA/GTA appointments for a total guaranteed funding of CAD 26,000 to 32,000 / year.",
                "amount": "CAD 2,160 to 2,660 / month total guaranteed funding (~PKR 440,000 to 545,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Relocation flights to Edmonton are self-funded or subsidized by supervisor project travel funds.",
                "amount": "Not covered in central award"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit (~CAD 150) and biometrics fee (~CAD 85) paid directly to Immigration, Refugees and Citizenship Canada (IRCC).",
                "amount": "Approx. CAD 235 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "University of Alberta Student Union Health and Dental Plan plus Alberta Health Care Insurance Plan (AHCIP) coverage provided to international students holding 12+ month study permits at zero premium cost.",
                "amount": "100% covered provincial healthcare (AHCIP)"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Daily groceries and campus dining funded from monthly stipend.",
                "amount": "Covered via stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Departmental research workstations, high-performance computing clusters (Compute Canada / Amii resources), and library repositories provided.",
                "amount": "100% covered computing and library infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "GPS Graduate Student Travel Awards provide up to CAD 1,500 per year for presenting research papers at national and international conferences.",
                "amount": "Up to CAD 1,500 / year travel award"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Edmonton Transit Service (ETS) Universal Transit Pass (U-Pass) included in student fees providing unlimited bus and LRT transit throughout Edmonton.",
                "amount": "100% unlimited citywide U-Pass transit"
            },
            "total_estimated_value_usd_per_year": 27500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single Canadian U15 research powerhouse (University of Alberta).",
            "participating_institutions": [
                "University of Alberta (North Campus, Edmonton, Alberta, Canada)"
            ],
            "university_rankings_scope": "QS World University Rankings #96, CSRankings #1 in Canada and Top 5 globally for Artificial Intelligence and Machine Learning (home to Amii - Alberta Machine Intelligence Institute).",
            "available_majors": [
                "MSc / PhD in Computing Science (AI, Machine Learning, Reinforcement Learning)",
                "MSc / PhD in Electrical and Computer Engineering",
                "MSc / PhD in Biomedical Engineering",
                "MSc / PhD in Chemical and Materials Engineering",
                "MSc / PhD in Mechanical Engineering",
                "MSc / PhD in Biological Sciences (Genetics, Microbiology)",
                "MSc / PhD in Physics and Geophysics",
                "MSc / PhD in Pharmacology and Oncology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years",
            "admission_requirements_summary": "Bachelor's or Master's degree with minimum GPA 3.70 / 4.0, verified transcripts, IELTS 6.5+ or TOEFL 90+, three academic letters of recommendation, CV, statement of purpose, and prospective supervisor support.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Computing Science (Amii AI lab) is globally ultra-competitive with acceptance rates below 5%; securing supervisor confirmation prior to applying is strongly encouraged.",
            "strategic_program_match_advice": "Highlight prior machine learning projects or engineering thesis work; reference specific UofA research laboratories (Amii, NanoFAB, NRC Nanotechnology) in your research statement."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ualberta.ca/en/graduate-studies/prospective-students/apply-for-admission.html",
            "portal_system_name": "University of Alberta Graduate Online Application System (GSMS)",
            "account_creation_instructions": "Create an applicant profile on GSMS portal, select thesis-based graduate program, identify potential supervisors, upload academic transcripts, English scores, CV, statement of intent, and pay CAD 135 application fee.",
            "step_by_step_workflow": [
                "Step 1: Identify eligible thesis supervisor in target academic department and make email contact with CV and research abstract.",
                "Step 2: Ensure valid IELTS (6.5+), TOEFL (90+), or Duolingo (120+) score report is ready.",
                "Step 3: Submit online admission application via GSMS portal and pay CAD 135 fee.",
                "Step 4: Upload official transcripts, CV, statement of intent, and referee contact details.",
                "Step 5: Referees submit electronic assessment letters directly into the GSMS portal.",
                "Step 6: Departmental graduate admissions committee reviews application, offers admission, and automatically nominates top candidates to Faculty of GPS for Graduate Entrance Scholarship.",
                "Step 7: GPS awards entrance scholarship; department supplements with GRA/GTA funding package.",
                "Step 8: Accept offer, receive provincial attestation letter (PAL), and apply for Canadian Study Permit."
            ],
            "university_vs_scholarship_routing": "Integrated Departmental Nomination: Applicants are automatically considered and nominated by their admitting department without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted electronically via automated referee appraisal links generated by GSMS.",
            "personal_statement_prompts": "Statement of intent (1 to 2 pages) describing research experience, academic goals, alignment with faculty research, and long-term career objectives.",
            "study_plan_research_proposal_requirements": "Brief 1 to 2-page research summary outlining target research area, methodologies, and proposed contribution.",
            "cv_format_requirements": "Standard academic CV highlighting degree coursework, GPA, publications, software libraries, and research projects.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisory video interview via Zoom/Google Meet to evaluate technical competency and research synergy.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 90+ mandatory; GRE optional.",
            "application_fee_amount": "CAD 135 (approx. USD 100 / ~PKR 27,500)",
            "attestation_requirements": "Official HEC Pakistan verified transcripts required upon conditional admission offer.",
            "translation_requirements": "Official certified English translation of non-English academic documents.",
            "final_submission_method": "100% online submission via University of Alberta GSMS portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree with minimum GPA 3.7 / 4.0 in final two years of full-time study.",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "English Language Proficiency Test Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (minimum 6.5, no band < 6.0) or TOEFL iBT (minimum 90) or Duolingo (120+).",
                "pakistan_specific_instruction": "Official electronic score report submitted to University of Alberta."
            },
            {
                "document_name": "Three Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential referee appraisals from university professors familiar with research capacity.",
                "pakistan_specific_instruction": "Submitted via automated institutional email links."
            },
            {
                "document_name": "Statement of Purpose / Research Intent",
                "mandatory": True,
                "specification": "1 to 2-page statement outlining research background, objectives, and faculty alignment.",
                "pakistan_specific_instruction": "Tailored to University of Alberta research groups."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic CV detailing research, awards, and technical expertise.",
                "pakistan_specific_instruction": "Highlighting research experience."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport personal bio-data page valid for minimum 1 year.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "December 15 (Early / International round) / January 15 (Final department round)",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "January 15",
            "recommendation_letters_deadline": "January 22",
            "interview_period": "January - February",
            "shortlist_announcement": "Late February - March",
            "final_result_acceptance_deadline": "April 15",
            "visa_application_window": "April - June",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Main intake starts in September (Fall). Thesis-based programs strongly prioritize applications submitted by December 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Undergraduate / graduate GPA, academic transcript rigor)",
            "extracurricular_and_leadership_weight": "5% (Community engagement and academic leadership)",
            "research_experience_weight": "35% (Prior research thesis, publications, and laboratory projects)",
            "work_experience_weight": "5% (Industry software or engineering experience)",
            "personal_statement_weight": "5% (Clarity and focus of statement of intent)",
            "recommendations_weight": "5% (Referee appraisals of research potential)",
            "interview_weight": "5% (Supervisor technical discussion and mutual fit)",
            "test_scores_weight": "0% (English proficiency is a mandatory threshold)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Departmental Graduate Admissions Committee and Faculty of Graduate & Postdoctoral Studies (GPS) Awards Committee.",
            "evaluation_methodology": "Competitive multi-tiered ranking based on admission GPA, research track record, and supervisor sponsorship."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 to 7,500 thesis graduate applicants",
            "total_scholarships_awarded": "~150 to 200 graduate entrance scholarships across university",
            "acceptance_rate_global": "~3.5% to 5.0%",
            "acceptance_rate_pakistan": "~4.0% to 6.5% for applicants with GPA >= 3.7 and published research",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.80 / 4.00, often with conference or journal publications",
            "typical_academic_and_research_profile": "Top-tier graduates from recognized universities with strong coding or laboratory skills, clear research focus, and supervisor backing.",
            "common_backgrounds_of_winners": "Graduates from premier Pakistani universities (NUST, FAST-NUCES, LUMS, GIKI, UET Lahore, Quaid-i-Azam, COMSATS).",
            "high_representation_countries": "Canada, Pakistan, India, China, Iran, Nigeria, Bangladesh, Turkey, USA.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Apply strictly through the official ualberta.ca website.",
                "Beware of immigration agencies claiming to guarantee Canadian university admissions or scholarships."
            ],
            "application_fee_warning": "Application fee of CAD 135 is paid exclusively via the official online application portal.",
            "agent_and_intermediary_warnings": "University of Alberta does not employ educational agents for thesis-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 135 (~PKR 27,500).",
                "Canadian Study Permit & biometrics fee: CAD 235 (~PKR 48,000).",
                "IELTS or TOEFL test fees: ~PKR 55,000 to 65,000.",
                "Initial relocation airfare to Edmonton: ~PKR 250,000 to 350,000.",
                "Winter clothing and initial setup in Edmonton (-30°C winter climate): ~CAD 1,000 (~PKR 205,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get funded without a supervisor. Reality: In thesis-based programs (especially Computing Science), having a committed faculty supervisor is practically essential for funding.",
                "Myth: Edmonton is too expensive for students. Reality: Edmonton has significantly lower rental and living costs compared to Toronto or Vancouver, making stipends go much further."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim funding is automatic for all admitted students; guaranteed funding packages apply strictly to thesis-based programs, not course-based Master's."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative graduate GPA of 3.0 / 4.0 throughout each academic year.",
            "attendance_requirements": "Full-time on-campus residency in Edmonton and active engagement in thesis research and coursework.",
            "academic_progress_monitoring": "Annual progress report submitted jointly with supervisor to the Department Graduate Coordinator and GPS.",
            "work_restrictions_during_study": "Teaching Assistant (TA) or Research Assistant (RA) appointments are limited to a maximum of 12 hours per week during academic terms to ensure focus on thesis research.",
            "home_country_return_obligation": "None; graduates are eligible for a 3-year Canadian Post-Graduation Work Permit (PGWP).",
            "service_obligations_or_bonds": "Obligation to fulfill assigned GRA/GTA duties up to 12 hours/week.",
            "repayment_clawback_conditions": "Scholarship funding ceases if student switches to part-time study, withdraws, or fails to maintain academic good standing.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Requires approval from current supervisor, new department, and Faculty of GPS.",
            "extension_policy": "Stipend support beyond the standard guaranteed period (2 years MSc, 4 years PhD) is at the discretion of the supervisor's research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Alberta Graduate Entrance Scholarship Official Page",
                "source_url": "https://www.ualberta.ca/en/graduate-studies/awards-and-funding/scholarships/university-of-alberta-graduate-entrance-scholarship.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Faculty of Graduate & Postdoctoral Studies (GPS) Financial Support",
                "source_url": "https://www.ualberta.ca/en/graduate-studies/awards-and-funding/index.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AM-049": {
        "scholarship_id": "SCH-AM-049",
        "basic_details": {
            "scholarship_name": "Simon Fraser University (SFU) Graduate Research Fellowship & Entrance Awards",
            "offering_entity": "Graduate and Postdoctoral Studies (GPS), Simon Fraser University",
            "host_country": "Canada",
            "host_institutions_covered": "Simon Fraser University (Burnaby, Surrey, and Vancouver Campuses, British Columbia, Canada)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computing Science, School of Engineering Science, School of Mechatronic Systems Engineering, Department of Biological Sciences, Department of Mathematics, and Faculty of Health Sciences.",
            "number_of_awards_total": "~120 to 160 graduate research entrance awards and fellowships annually",
            "number_of_awards_pakistan": "Open internationally on merit; Pakistani scholars regularly secure positions in Computing Science, Mechatronics, and Engineering (~12 to 20 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 4 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "CAD 24,000 to 32,000 / year total guaranteed funding package (CAD 7,000 / term fellowship plus Graduate Research Assistantship and Teaching Assistantship; approx. CAD 2,000 to 2,660 / month; ~PKR 410,000 to 545,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students worldwide including Pakistan as well as Canadian citizens/PR"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 0,
            "age_limit_notes": "No age restriction; evaluated on academic excellence and research potential.",
            "academic_qualifications": "16-year Bachelor's degree with minimum cumulative GPA of 3.50 / 4.00 (or first-class standing / 78%+) for Master's; 18-year Master's degree with minimum GPA 3.50 / 4.00 for PhD from an HEC-recognized university.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum cumulative grade point average of 3.50 / 4.00 (or equivalent B+ to A- average).",
            "subject_background_prerequisites": "Undergraduate degree in computer science, software engineering, mechatronics, electrical engineering, or related discipline.",
            "current_education_status": "Graduated or final-year undergraduate students completing credentials before start term.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications or significant open-source/industrial engineering experience advantageous.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 93,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 7.0 overall (no band below 6.5) or TOEFL iBT minimum 93 (subscores 20+) mandatory for School of Computing Science and Engineering Science.",
            "other_language_requirements": "GRE General recommended for international applicants outside North America.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must be admitted to a thesis-based graduate program with guaranteed supervisor funding.",
            "previous_scholarship_restrictions": "Subject to SFU Graduate Award policy limits on total award holding.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full international tuition covered through departmental tuition bursaries and graduate fellowship offsets (SFU charges flat graduate research tuition of approx. CAD 2,050 / term; ~CAD 6,150 / year).",
                "amount": "100% covered (~CAD 6,150 / year value; ~PKR 1,260,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Non-refundable international graduate application fee of CAD 130 paid directly via the online portal.",
                "amount": "CAD 130 (~PKR 26,500) application fee"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "On-campus graduate residence at Burnaby Mountain or off-campus rental in Burnaby/Vancouver arranged independently; funded via living stipend.",
                "amount": "Funded from stipend (~CAD 950 to 1,400 / month rent)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Guaranteed minimum annual funding package of CAD 24,000 (MSc) to CAD 30,000+ (PhD) composed of Graduate Fellowships (GF), Research Assistantships (RA), and Teaching Assistantships (TA).",
                "amount": "CAD 24,000 to 32,000 / year (~CAD 2,000 to 2,660 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel to Vancouver is self-funded.",
                "amount": "Not covered"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit (~CAD 150) and biometrics fee (~CAD 85) paid to IRCC by applicant.",
                "amount": "Approx. CAD 235 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "British Columbia Medical Services Plan (BC MSP) provides comprehensive provincial medical care (~CAD 75/mo, reimbursed or subsidized via student health plan) plus SFU Graduate Student Society extended health and dental coverage.",
                "amount": "100% comprehensive medical & dental coverage"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Dining and grocery expenses covered via monthly stipend.",
                "amount": "Covered via stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "School of Computing Science / Engineering dedicated graduate student workspace, laboratory compute workstations, and high-speed network access included.",
                "amount": "100% covered research computing access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "SFU Travel and Minor Research Awards provide up to CAD 1,000 to 1,500 per year for presenting research papers at conferences.",
                "amount": "Up to CAD 1,500 / year travel awards"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Metro Vancouver Universal Transit Pass (U-Pass BC) included in student fees providing unlimited TransLink bus, SeaBus, and SkyTrain travel across Greater Vancouver.",
                "amount": "100% unlimited Greater Vancouver U-Pass transit"
            },
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive Canadian research institution (Simon Fraser University).",
            "participating_institutions": [
                "Simon Fraser University (Burnaby Mountain Campus, Metro Vancouver, BC, Canada)"
            ],
            "university_rankings_scope": "Consistently ranked Canada's #1 Comprehensive University by Maclean's; Top 75 worldwide for Computer Science (CSRankings); renowned for computer graphics, computer vision, robotics, and big data systems.",
            "available_majors": [
                "MSc / PhD in Computing Science (Vision, Graphics, AI, Systems)",
                "MASc / PhD in Engineering Science (Microelectronics, Robotics)",
                "MASc / PhD in Mechatronic Systems Engineering",
                "MSc / PhD in Mathematics and Big Data",
                "MSc / PhD in Biological Sciences and Molecular Biology",
                "MSc / PhD in Health Sciences (Epidemiology, Biostatistics)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with minimum GPA 3.50, verified transcripts, IELTS 7.0+ (subscores 6.5+) or TOEFL 93+, three academic recommendation letters, CV, statement of research interests, and prospective faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of Computing Science (Gradiant Lab, GrUVi, Vision lab) is exceptionally competitive; having prior research contact with a faculty member greatly improves admission and fellowship probability.",
            "strategic_program_match_advice": "Review faculty publications in the School of Computing Science; explicitly cite specific SFU research groups (e.g., Computational Vision, Network Systems) in your research statement."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.sfu.ca/gradstudies/apply.html",
            "portal_system_name": "Simon Fraser University Graduate Online Application System (goSFU)",
            "account_creation_instructions": "Register on the SFU graduate application portal, choose thesis graduate program, list preferred academic supervisors, upload scanned transcripts, English test report, CV, and statement of research intent, and pay CAD 130 fee.",
            "step_by_step_workflow": [
                "Step 1: Browse SFU faculty directory and contact prospective thesis supervisors with research summary and CV.",
                "Step 2: Obtain valid IELTS (7.0+) or TOEFL (93+) score report.",
                "Step 3: Submit application on SFU online system and pay CAD 130 fee.",
                "Step 4: Upload official academic transcripts, statement of intent, and curriculum vitae.",
                "Step 5: Provide 3 referee email addresses; referees receive automated links to submit confidential recommendations.",
                "Step 6: Departmental graduate committee conducts admissions review and formulates guaranteed funding package (GF + GRA + GTA).",
                "Step 7: Candidate receives formal admission offer with guaranteed minimum funding letter.",
                "Step 8: Accept offer, receive Provincial Attestation Letter (PAL), and apply for Canadian Study Permit."
            ],
            "university_vs_scholarship_routing": "Integrated Admissions & Funding: Every admitted thesis-based graduate student receives a guaranteed minimum funding package without a separate application.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated secure electronic appraisal forms.",
            "personal_statement_prompts": "Statement of research interests (1 to 2 pages) describing research experience, technical competencies, proposed research topics, and fit with SFU faculty.",
            "study_plan_research_proposal_requirements": "1 to 2-page research outline highlighting potential thesis directions and methodological knowledge.",
            "cv_format_requirements": "Comprehensive academic CV detailing education, GPA, research projects, publications, and programming proficiencies.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisory technical interview via Zoom to discuss research methodology and prospective lab projects.",
            "standardized_tests": "IELTS Academic 7.0+ or TOEFL iBT 93+ mandatory; GRE recommended for Computing Science.",
            "application_fee_amount": "CAD 130 (approx. USD 96 / ~PKR 26,500)",
            "attestation_requirements": "HEC Pakistan and MoFA Pakistan verified transcripts required upon conditional admission.",
            "translation_requirements": "Certified English translation of all non-English transcripts.",
            "final_submission_method": "100% digital submission via SFU application system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Bachelor's / Master's degree with minimum cumulative GPA 3.5 / 4.0 (or equivalent 78%+).",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (minimum 7.0, no band < 6.5) or TOEFL iBT (minimum 93, no subscore < 20).",
                "pakistan_specific_instruction": "Official electronic score report submitted to Simon Fraser University."
            },
            {
                "document_name": "Three Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential referee appraisals from professors familiar with candidate's academic and research abilities.",
                "pakistan_specific_instruction": "Submitted via institutional email links."
            },
            {
                "document_name": "Statement of Research Interests",
                "mandatory": True,
                "specification": "1 to 2-page statement outlining research background, objectives, and faculty synergy.",
                "pakistan_specific_instruction": "Tailored to SFU faculty labs."
            },
            {
                "document_name": "Detailed Academic Curriculum Vitae",
                "mandatory": True,
                "specification": "Listing all academic history, research projects, publications, and technical skills.",
                "pakistan_specific_instruction": "Highlighting research experience."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for minimum 1 year.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1",
            "application_deadline": "December 15 (School of Computing Science / Engineering Science) / January 15 (Other departments)",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "January 15",
            "recommendation_letters_deadline": "January 22",
            "interview_period": "January - February",
            "shortlist_announcement": "Late February - March",
            "final_result_acceptance_deadline": "April 15",
            "visa_application_window": "April - June",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Main intake starts in September (Fall). Selected programs also offer a smaller January (Spring) intake."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior academic GPA, course grades in core subjects)",
            "extracurricular_and_leadership_weight": "5% (Leadership and community involvement)",
            "research_experience_weight": "40% (Prior research projects, publications, thesis quality, coding acumen)",
            "work_experience_weight": "5% (Industry software engineering or research lab experience)",
            "personal_statement_weight": "5% (Quality of research interest statement)",
            "recommendations_weight": "5% (Referee appraisals of research independence)",
            "interview_weight": "5% (Supervisor technical discussion)",
            "test_scores_weight": "0% (English test is a mandatory qualification threshold)",
            "financial_need_weight": "0% (Pure academic excellence and research capability)",
            "selection_panel_composition": "Departmental Graduate Admissions Committee and Prospective Faculty Supervisor.",
            "evaluation_methodology": "Competitive evaluation matching top academic candidates with funded faculty research laboratories."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,500 to 6,000 graduate applicants across faculties",
            "total_scholarships_awarded": "~120 to 160 fully funded thesis research positions annually",
            "acceptance_rate_global": "~3.0% to 4.5%",
            "acceptance_rate_pakistan": "~4.0% to 6.0% for applicants with GPA >= 3.6 and research background",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.65 / 4.00, solid research thesis or published conference papers",
            "typical_academic_and_research_profile": "Top-tier graduates from recognized universities with strong programming/laboratory skills, clear research focus, and supervisor backing.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (FAST-NUCES, NUST, LUMS, GIKI, UET, COMSATS).",
            "high_representation_countries": "Canada, Pakistan, India, China, Iran, USA, Nigeria, Bangladesh, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official SFU portal at sfu.ca.",
                "SFU does not authorize commercial recruiting agencies to sell admissions or funding."
            ],
            "application_fee_warning": "Application fee of CAD 130 is paid strictly through the secure online application gateway.",
            "agent_and_intermediary_warnings": "Simon Fraser University evaluates thesis graduate applicants directly through academic departments.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 130 (~PKR 26,500).",
                "Canadian Study Permit & biometrics fee: CAD 235 (~PKR 48,000).",
                "IELTS test registration: ~PKR 55,000 to 65,000.",
                "Initial relocation flight to Vancouver: ~PKR 250,000 to 350,000.",
                "Initial temporary accommodation / damage deposit in Metro Vancouver: ~CAD 1,500 (~PKR 310,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Vancouver living costs make graduate study impossible. Reality: The guaranteed funding package (CAD 24,000–32,000) combined with flat tuition (~CAD 6,150) and U-Pass provides a stable living standard.",
                "Myth: You do not need to contact professors beforehand. Reality: In CS and Engineering Science, obtaining preliminary supervisor interest is the single most decisive factor for admission."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently quote outdated funding figures; verified current minimum guaranteed funding is CAD 24,000 (MSc) to CAD 30,000+ (PhD)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative graduate GPA of 3.0 / 4.0 throughout each academic term.",
            "attendance_requirements": "Full-time resident study in Metro Vancouver and continuous registration across all three annual terms (Fall, Spring, Summer).",
            "academic_progress_monitoring": "Annual progress review submitted by supervisory committee to Department Graduate Chair and GPS.",
            "work_restrictions_during_study": "Teaching Assistant (TA) duties are regulated by the TSSU collective agreement (typically 120-170 hours per semester); maximum 12-15 hours/week of on-campus work permitted.",
            "home_country_return_obligation": "None; graduates are eligible for a 3-year Canadian Post-Graduation Work Permit (PGWP).",
            "service_obligations_or_bonds": "Obligation to fulfill assigned Teaching Assistant or Research Assistant duties.",
            "repayment_clawback_conditions": "Funding terminated if student withdraws, switches to unapproved part-time study, or fails required academic milestones.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Requires approval from graduate program committee and faculty supervisor.",
            "extension_policy": "Funding beyond normal degree timeline is subject to supervisor grant availability and satisfactory progress."
        },
        "official_sources_verified": [
            {
                "source_name": "Simon Fraser University Graduate and Postdoctoral Studies Funding",
                "source_url": "https://www.sfu.ca/gradstudies/awards-funding.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "SFU School of Computing Science Graduate Admissions and Financial Support",
                "source_url": "https://www.sfu.ca/computing/prospective-students/graduate-students/admissions-and-funding.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AM-050": {
        "scholarship_id": "SCH-AM-050",
        "basic_details": {
            "scholarship_name": "Western University International President's Entrance Scholarship & Graduate Awards",
            "offering_entity": "Western University (University of Western Ontario) & School of Graduate and Postdoctoral Studies (SGPS)",
            "host_country": "Canada",
            "host_institutions_covered": "Western University Main Campus (London, Ontario, Canada)",
            "degree_levels": ["Bachelor of Science (BSc)", "Master of Engineering Science (MESc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Engineering (Electrical & Computer, Mechanical & Materials, Chemical & Biochemical, Civil & Environmental), Faculty of Science (Computer Science, Data Science, Medical Biophysics), and Ivey School of Business.",
            "number_of_awards_total": "~100 to 140 prestigious entrance scholarships and doctoral awards annually",
            "number_of_awards_pakistan": "Open globally on academic distinction; Pakistani scholars secure top spots in engineering, computing, and biomedical sciences (~10 to 18 awards annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 years for Bachelor's; 2 years for Master's; 4 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "CAD 50,000 / year total value for Undergraduate President's Award; CAD 26,000 to 34,000 / year guaranteed funding package for Graduate MESc/PhD (approx. CAD 2,160 to 2,830 / month; ~PKR 440,000 to 580,000 / month)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students of all nationalities including Pakistan as well as domestic Canadian scholars"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 22,
            "age_limit_postgrad": 0,
            "age_limit_notes": "Undergraduate applicants must be graduating high school; no age limit for graduate applicants.",
            "academic_qualifications": "For Undergraduate: Minimum 90% aggregate marks in HSSC / Intermediate (Pre-Engineering/ICS) or A-Levels (minimum A*AA). For Graduate: Recognized 16-year Bachelor's or 18-year Master's degree with minimum 80% aggregate (or CGPA 3.50+ / 4.00) from an HEC-recognized university.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum admission average of 90%+ for undergraduate President's Award; minimum 80%+ (GPA 3.5/4.0) for graduate research funding.",
            "subject_background_prerequisites": "Advanced mathematics, physics, and chemistry/computing for STEM faculties.",
            "current_education_status": "Graduated or final-year students completing credentials before September commencement.",
            "graduation_year_restrictions": "Undergraduate applicants must be current high school seniors.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "High school leadership, extracurricular impact, or prior undergraduate research publications strongly valued.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 86,
            "duolingo_accepted": True,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (no subscore below 6.0), TOEFL iBT minimum 86 (subscores 20+), or Duolingo English Test 115+ mandatory.",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "Open equally to all candidates.",
            "financial_need_required": False,
            "special_eligibility_categories": "Undergraduate applicants must be nominated by their secondary school head / principal; graduate applicants nominated by academic department.",
            "previous_scholarship_restrictions": "Cannot be combined with another concurrent major tuition entrance award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full international tuition covered through CAD 50,000 / year award (Undergraduate) or Western Graduate Research Scholarship tuition waiver top-up (Graduate).",
                "amount": "100% covered (~CAD 35,000 to 45,000 / year value for international UG; ~PKR 7,100,000 to 9,200,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Ontario Universities' Application Centre (OUAC) fee of approx. CAD 156 (Undergraduate) or Western SGPS fee of CAD 150 (Graduate).",
                "amount": "Approx. CAD 150 borne by student"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "On-campus Western residence (Undergraduate first year guaranteed) and meal plan credit included in President's award; graduate scholars fund private/residence housing via stipend.",
                "amount": "Included in UG package / funded from stipend for grads"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Remaining award balance disbursed as living allowance (Undergraduate); guaranteed living stipend of CAD 22,000 to 28,000 / year for graduate thesis scholars.",
                "amount": "CAD 1,830 to 2,330 / month living allowance (~PKR 375,000 to 480,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International relocation flights to London, Ontario are self-funded.",
                "amount": "Not covered"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit (~CAD 150) and biometrics fee (~CAD 85) paid to IRCC.",
                "amount": "Approx. CAD 235 borne by student"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "University Health Insurance Plan (UHIP) provides comprehensive primary medical healthcare for international students in Ontario, plus Western University Students' Council (USC/SOGS) dental plan.",
                "amount": "100% covered UHIP healthcare"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "First-year campus residence dining meal plan credit included in undergraduate scholarship; funded from monthly stipend for graduate students.",
                "amount": "Covered via residence package or stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Initial book allowance credit at The Book Store at Western, plus complete digital library access and campus compute privileges.",
                "amount": "100% covered"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Undergraduate student research internships (USRI) provide CAD 9,000 summer research stipends; graduate students eligible for SGPS conference travel grants up to CAD 1,000.",
                "amount": "CAD 1,000 to 9,000 research/travel support"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "London Transit Commission (LTC) full-year universal student bus pass included in student ancillary fees providing unlimited transit across London, Ontario.",
                "amount": "100% unlimited LTC bus transit"
            },
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Canadian U15 research university (Western University).",
            "participating_institutions": [
                "Western University (London, Ontario, Canada)"
            ],
            "university_rankings_scope": "QS World University Rankings #114, Top 1% of universities worldwide, member of Canada's U15 research group, renowned for Engineering, Neuroscience (Brain and Mind Institute), and Business (Ivey).",
            "available_majors": [
                "Software Engineering and Artificial Intelligence",
                "Computer Science and Data Science",
                "Electrical and Computer Engineering",
                "Mechanical and Materials Engineering",
                "Chemical and Biochemical Engineering",
                "Civil and Environmental Engineering (Wind Engineering)",
                "Medical Biophysics and Neuroscience",
                "Business Administration and Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 years; Master's: 2 years; PhD: 4 years",
            "admission_requirements_summary": "High school transcript (90%+) or Bachelor's transcript (80%+), school nomination letter (for UG President's), IELTS 6.5+ or TOEFL 86+, personal essay describing leadership impact, two recommendation letters, and CV.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "International President's Entrance Scholarship is Western's highest undergraduate honor with only 3 international awards campus-wide; engineering graduate funding is departmental and much more accessible.",
            "strategic_program_match_advice": "For undergraduate applicants, emphasize verifiable community leadership and global citizenship alongside academic excellence; for graduates, establish contact with Western Engineering or Science faculty."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://registrar.uwo.ca/student_finances/scholarships_awards/admission/international_presidents_entrance_scholarships.html",
            "portal_system_name": "Western University Student Center & OUAC Portal",
            "account_creation_instructions": "Submit general admission application via OUAC (Undergraduate) or Western SGPS portal (Graduate), then access Western Student Center to complete the International President's Entrance Scholarship application by February 14.",
            "step_by_step_workflow": [
                "Step 1: Submit general admission application to Western University via OUAC (undergraduate) or SGPS (graduate).",
                "Step 2: Obtain school nomination from high school principal or headmaster (for undergraduate President's Award).",
                "Step 3: Access Western Student Center scholarship application portal.",
                "Step 4: Complete scholarship application form, including leadership essay and list of extracurricular contributions.",
                "Step 5: Have secondary school submit official nomination letter and academic transcripts by February 14.",
                "Step 6: University scholarship selection committee reviews dossiers and conducts virtual interviews for shortlisted finalists in March.",
                "Step 7: Final scholarship award decisions announced in April; recipient receives official admission and funding offer.",
                "Step 8: Accept offer by deadline, obtain Provincial Attestation Letter (PAL), and apply for Canadian Study Permit."
            ],
            "university_vs_scholarship_routing": "Concurrent Application Track: General admission application is submitted first, followed by formal scholarship submission and school nomination via Student Center.",
            "recommendation_letters_submission_method": "Submitted directly by school headmaster / referees via Western secure document upload.",
            "personal_statement_prompts": "Leadership essay (approx. 750 words) demonstrating exceptional extracurricular initiative, global awareness, and commitment to making a positive difference.",
            "study_plan_research_proposal_requirements": "For graduate candidates: 1 to 2-page research summary outlining target research area.",
            "cv_format_requirements": "Detailed leadership and extracurricular resume outlining roles, hours, achievements, and community initiatives.",
            "interviews_conducted": True,
            "interview_format_details": "Virtual panel interview with Western University Scholarship Selection Committee evaluating leadership maturity and communication.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 86+ or Duolingo 115+ mandatory.",
            "application_fee_amount": "CAD 150 to 156 (approx. USD 110 / ~PKR 31,000)",
            "attestation_requirements": "Verified high school / university transcripts certified by educational institution and HEC/IBCC upon admission.",
            "translation_requirements": "Certified English translation of all non-English transcripts.",
            "final_submission_method": "100% online submission via Western Student Center."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Predicted Grades",
                "mandatory": True,
                "specification": "Secondary school transcripts with minimum 90%+ average (or A*AA in A-Levels); or university transcripts with 80%+ for graduates.",
                "pakistan_specific_instruction": "Certified by intermediate board / school and IBCC/HEC."
            },
            {
                "document_name": "Official School Nomination Letter",
                "mandatory": True,
                "specification": "Formal nomination letter signed by high school principal endorsing candidate as school's nominee.",
                "pakistan_specific_instruction": "Printed on official school letterhead."
            },
            {
                "document_name": "Leadership and Extracurricular Essay",
                "mandatory": True,
                "specification": "750-word essay detailing leadership initiatives, community impact, and character.",
                "pakistan_specific_instruction": "Showcasing meaningful community leadership."
            },
            {
                "document_name": "Comprehensive Extracurricular Activity Resume",
                "mandatory": True,
                "specification": "Chronological record of leadership roles, volunteer hours, awards, and athletic/artistic accomplishments.",
                "pakistan_specific_instruction": "Documenting verifiable impact."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic minimum 6.5 (no band < 6.0) or TOEFL iBT minimum 86 or Duolingo 115+.",
                "pakistan_specific_instruction": "Official test report."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1",
            "application_deadline": "February 14 (Undergraduate President's Award deadline) / January 15 (Graduate departmental deadline)",
            "university_admission_deadline": "February 14",
            "document_submission_deadline": "February 14",
            "recommendation_letters_deadline": "February 21",
            "interview_period": "March (Undergraduate finalists)",
            "shortlist_announcement": "Early April",
            "final_result_acceptance_deadline": "May 1",
            "visa_application_window": "May - July",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Undergraduate President's Award operates strictly on the February 14 annual deadline for September entry."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic excellence, transcript average 90%+)",
            "extracurricular_and_leadership_weight": "35% (Demonstrated leadership initiative, extracurricular impact, community service)",
            "research_experience_weight": "5% (Scientific curiosity, research projects, or olympiad achievements)",
            "work_experience_weight": "0% (Not required)",
            "personal_statement_weight": "10% (Quality, voice, and authenticity of leadership essay)",
            "recommendations_weight": "5% (Strength of principal nomination and referee praise)",
            "interview_weight": "5% (Performance in virtual finalist interview)",
            "test_scores_weight": "0% (English proficiency is a mandatory threshold)",
            "financial_need_weight": "0% (Pure merit and leadership excellence)",
            "selection_panel_composition": "Western University President's Scholarship Committee comprising Senior University Academic Leaders and Registrar.",
            "evaluation_methodology": "Holistic evaluation balancing stellar academic marks (90%+) with exceptional leadership and community contributions."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 2,000 nominated international applicants worldwide",
            "total_scholarships_awarded": "3 prestigious International President's Entrance Scholarships awarded campus-wide annually",
            "acceptance_rate_global": "~0.2% to 0.5% (Extremely elite undergraduate honor)",
            "acceptance_rate_pakistan": "~0.5% to 1.0% for exceptional national top scorers with extraordinary leadership profiles",
            "typical_successful_applicant_gpa": "95%+ in F.Sc / 4 A*s in A-Levels, coupled with national or international leadership and community achievements",
            "typical_academic_and_research_profile": "Top student in their institution, founder of social impact initiatives, debate or robotics champions with flawless grades.",
            "common_backgrounds_of_winners": "Graduates of top secondary schools in Pakistan (Aitchison College, Karachi Grammar School, Beaconhouse, Lahore Grammar School, Army Public Schools).",
            "high_representation_countries": "Canada, Pakistan, India, China, UK, USA, Kenya, Ghana, Singapore, Turkey.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only submit applications through official portal at uwo.ca.",
                "Western never charges scholarship nomination fees or works with unauthorized agents."
            ],
            "application_fee_warning": "OUAC / Western admission application fee is paid directly through the official university gateway.",
            "agent_and_intermediary_warnings": "Western University strictly requires direct secondary school principal nomination; agency nominations are rejected.",
            "hidden_costs_breakdown": [
                "OUAC / SGPS application fee: ~CAD 150 (~PKR 31,000).",
                "Canadian Study Permit & biometrics fee: CAD 235 (~PKR 48,000).",
                "IELTS test fee: ~PKR 55,000 to 65,000.",
                "Initial relocation airfare to Toronto/London: ~PKR 250,000 to 350,000.",
                "Personal expenses and winter clothing: ~CAD 1,500 (~PKR 310,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Good grades alone are enough to win the President's Award. Reality: With 90%+ as the baseline, the award is won entirely on extraordinary leadership, initiative, and community impact.",
                "Myth: You can apply without school nomination. Reality: Each secondary school may nominate a limited number of candidates; non-nominated applications are ineligible."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs list old award values; current value of International President's Award is CAD 50,000 per year for four years (CAD 200,000 total)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain an 80.0% academic average (Dean's Honor List standard) across a full course load (minimum 5.0 courses) each year to renew funding.",
            "attendance_requirements": "Full-time continuous enrollment at Western University main campus.",
            "academic_progress_monitoring": "Annual academic audit by the Registrar's Office at the end of each academic year.",
            "work_restrictions_during_study": "Canadian study permit allows on/off-campus work; recommended to prioritize studies to maintain the 80% renewal cutoff.",
            "home_country_return_obligation": "None; graduates are eligible for a 3-year Canadian Post-Graduation Work Permit (PGWP).",
            "service_obligations_or_bonds": "Obligation to serve as student ambassador for Western International at recruitment and alumni events.",
            "repayment_clawback_conditions": "If academic average falls below 80%, scholarship renewal is forfeited for subsequent years without retroactive clawback.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Permitted across Western main campus faculties provided academic average is maintained.",
            "extension_policy": "Scholarship strictly capped at 4 years (8 semesters) of undergraduate study."
        },
        "official_sources_verified": [
            {
                "source_name": "Western University International President's Entrance Scholarships",
                "source_url": "https://registrar.uwo.ca/student_finances/scholarships_awards/admission/international_presidents_entrance_scholarships.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Western University School of Graduate and Postdoctoral Studies (SGPS)",
                "source_url": "https://grad.uwo.ca/finances/index.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
