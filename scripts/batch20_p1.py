# scripts/batch20_p1.py
# SCH-EU-049: Konrad Adenauer Foundation (KAS) International Scholarship (Germany)
# SCH-EU-051: Tampere University International Master's Scholarship (Finland)
# SCH-EU-053: Erasmus Mundus Master in Green & Networked Sustainable AI (GENIAL) (Europe)

DATA_P1 = {
    "SCH-EU-049": {
        "scholarship_id": "SCH-EU-049",
        "basic_details": {
            "scholarship_name": "Konrad Adenauer Foundation (KAS) International Graduate Scholarship",
            "offering_entity": "Konrad-Adenauer-Stiftung e.V. (KAS - Christian Democratic Political Foundation funded by the German Federal Government / BMBF)",
            "host_country": "Germany",
            "host_institutions_covered": "State-recognized universities and technical universities across Germany (e.g., TU Munich, Heidelberg University, University of Bonn, RWTH Aachen, University of Cologne, FU Berlin)",
            "degree_levels": ["Master of Science (MSc)", "Master of Arts (MA)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all disciplines offered at German universities; particularly strong representation in Computer Science, Artificial Intelligence, Engineering, Law, Economics, and Social Sciences (human medicine and pharmacy clinical years excluded).",
            "number_of_awards_total": "~120 to 180 international scholarships awarded annually across Master's and PhD programs",
            "number_of_awards_pakistan": "Open global competition; Pakistani scholars committed to Christian democratic / civic-ethical values, democracy, and community leadership secure ~3 to 6 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to standard program duration (up to 2 years for Master's; up to 3 years for PhD), reviewed annually based on academic excellence and participation in KAS seminars",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "€934 / month for Master's; €1,400 / month for PhD scholars"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students from developing and transition countries (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 30,
            "age_limit_postgrad": 30,
            "age_limit_notes": "Applicants must generally be under 30 years old at the time of application.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) with minimum CGPA 3.40 / 4.00 (German grade equivalent <= 2.0 on the Bavarian scale) from an HEC-recognized university in Pakistan for Master's; recognized MS/MPhil (18 years education) for PhD.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Demonstrated academic excellence placed in the top 15% of the graduating cohort.",
            "subject_background_prerequisites": "Prerequisites corresponding to the admitted degree program at the German university.",
            "current_education_status": "Applicants must already be accepted or enrolled (1st or 2nd semester) in a Master's or PhD program at a state-recognized German university at the time of application.",
            "graduation_year_restrictions": "None, as long as age limit (<30 years) is met.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Substantial documented record of voluntary civic engagement, youth leadership, religious/ethical community dialogue, or social advocacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Official IELTS (min 6.5) or TOEFL (min 90) for English programs; German language proficiency at minimum B2 level is required by KAS (all selection interviews and ideological seminars are conducted in German).",
            "other_language_requirements": "German language skills at minimum B2 level are formally required for international applicants.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must demonstrate strong alignment with Christian democratic principles: human dignity, freedom, solidarity, rule of law, and democratic governance.",
            "previous_scholarship_restrictions": "Cannot hold another full German government scholarship (DAAD, other Begabtenförderungswerke) simultaneously.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "Tuition at German public universities is free; mandatory semester fees (Semesterbeitrag ~€250 - €350 / semester) are supplemented or covered.",
                "amount": "100% covered (~€600 / year value; ~PKR 180,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University admission evaluation fees (Uni-Assist ~€75) are paid independently by the student.",
                "amount": "€75 (~PKR 23,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Subsidized housing in student residences (Studierendenwerk) is paid from the monthly KAS living stipend.",
                "amount": "Covered via monthly stipend"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend set by the BMBF: €934 per month for Master's students; €1,400 per month for PhD researchers (~PKR 280,000 - 420,000 / month).",
                "amount": "€934 - €1,400 / month (~PKR 280,000 - 420,000 / month; €11,208 - €16,800 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses must be arranged by the student; study allowance covers travel costs within Germany.",
                "amount": "Self-financed economy flight"
            },
            "visa_fee": {
                "status": "REIMBURSED",
                "details": "German student visa fee (€75) and residence permit fee (€100) are reimbursed upon submission of receipts.",
                "amount": "€175 total (~PKR 53,000 value)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Direct monthly health and nursing care insurance subsidy of up to €130 per month paid to the statutory German health insurance provider (TK, AOK, Barmer).",
                "amount": "Up to €130 / month (~PKR 39,000 / month; €1,560 / year value)"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of €934 - €1,400.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Flat-rate study cost allowance (Büchergeld / Forschungskostenpauschale) of €300 per month provided in addition to the base stipend.",
                "amount": "€300 / month (~PKR 90,000 / month; €3,600 / year value)"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Comprehensive funding for research travel, conference attendances, and political education seminars organized by the foundation.",
                "amount": "Up to €1,000 / year upon application"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Deutschlandticket / Semesterticket provided via university registration, granting nationwide public transport access.",
                "amount": "Included via semester fee"
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "All state-recognized public universities across Germany.",
            "participating_institutions": [
                "Technical University of Munich (TUM)",
                "Heidelberg University",
                "University of Bonn",
                "RWTH Aachen University",
                "University of Cologne",
                "Free University of Berlin (FU Berlin)",
                "University of Göttingen",
                "Technical University of Darmstadt"
            ],
            "university_rankings_scope": "Covers all German public universities, including elite TU9 technical universities and excellence cluster institutions.",
            "available_majors": [
                "Computer Science and Artificial Intelligence",
                "Electrical and Autonomous Engineering",
                "Software Systems and Cyber Security",
                "Economics and Development Policy",
                "Public Administration and International Law",
                "Environmental Sciences and Sustainable Energy",
                "Biotechnology and Health Policy"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for Master's; 3 years for PhD",
            "admission_requirements_summary": "Unconditional admission letter or active enrollment at a German university, recognized Bachelor's degree (minimum grade 2.0), certified German B2 proficiency, and substantial proof of voluntary civic engagement.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "KAS funds students admitted to any recognized German university; demonstrating social leadership and ethical vision is the primary determinant of selection.",
            "strategic_program_match_advice": "Pakistani applicants must secure university admission in Germany first and ensure their German language skills meet the B2 certificate requirement before the July 15 application deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.kas.de/en/web/begabtenfoerderung-und-kultur/auslaenderfoerderung",
            "portal_system_name": "Konrad-Adenauer-Stiftung Online Application Portal",
            "account_creation_instructions": "Register on the KAS applicant portal during the annual application window (open until July 15), complete the questionnaire on academic background and civic activism, and upload required documents.",
            "step_by_step_workflow": [
                "Step 1: Secure admission or enrollment in a Master's or PhD program at a state-recognized German university.",
                "Step 2: Obtain German language certificate (B2 level or higher).",
                "Step 3: Collect two academic appraisals from university professors and one reference letter confirming active social, voluntary, or ethical engagement.",
                "Step 4: Complete the online application on the KAS portal before the deadline (July 15).",
                "Step 5: Pre-selected candidates attend an assessment seminar / panel interview conducted in German in autumn.",
                "Step 6: Successful candidates receive the formal KAS scholarship award document, granting full monthly stipend and seminar access."
            ],
            "university_vs_scholarship_routing": "Admission-First Track: Must hold an admission offer or active enrollment in Germany before applying to KAS.",
            "recommendation_letters_submission_method": "Submitted by referees directly via the online portal or mailed in sealed envelopes.",
            "personal_statement_prompts": "Detailed essay explaining personal ethical values, civic engagement, understanding of democracy, and goals for social contribution.",
            "study_plan_research_proposal_requirements": "Summary of degree study plan or doctoral research proposal highlighting innovation and societal benefit.",
            "cv_format_requirements": "Detailed tabular CV (Europass) detailing education, civic engagement, and volunteer work.",
            "interviews_conducted": True,
            "interview_format_details": "45-minute selection panel interview conducted in German evaluating civic leadership, ethical foundation, and current affairs knowledge.",
            "standardized_tests": "German B2 certificate (Goethe, TestDaF, or telc) mandatory; IELTS/TOEFL for English programs.",
            "application_fee_amount": "€0 (Free of charge)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified German translation of all academic records.",
            "final_submission_method": "Online upload via the official KAS scholarship portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "German University Admission Letter or Enrollment Certificate",
                "mandatory": True,
                "specification": "Official admission letter or current enrollment certificate (Immatrikulationsbescheinigung).",
                "pakistan_specific_instruction": "Issued directly by the German university registrar."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's with minimum German equivalent grade 2.0.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "German Language Certificate (B2 Level Minimum)",
                "mandatory": True,
                "specification": "Official Goethe-Zertifikat B2, TestDaF (minimum TDN 3 in all sections), or telc B2.",
                "pakistan_specific_instruction": "Must be valid at the time of application submission."
            },
            {
                "document_name": "Essay on Personal Values and Social Engagement",
                "mandatory": True,
                "specification": "Detailed essay explaining your volunteer activities, ethical values, and civic commitment.",
                "pakistan_specific_instruction": "Must demonstrate authentic community service in Pakistan or abroad."
            },
            {
                "document_name": "Two Academic Professor Appraisals (Gutachten)",
                "mandatory": True,
                "specification": "Confidential evaluation letters from university professors assessing academic competence.",
                "pakistan_specific_instruction": "Submitted on university letterhead with institutional email."
            },
            {
                "document_name": "Reference Letter of Social / Voluntary Engagement",
                "mandatory": True,
                "specification": "Letter from an NGO, civic association, youth group, or community initiative confirming volunteer service.",
                "pakistan_specific_instruction": "Issued on official organization letterhead with full contact details."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "May 1",
            "application_deadline": "July 15",
            "university_admission_deadline": "July 15",
            "document_submission_deadline": "July 15",
            "recommendation_letters_deadline": "July 15",
            "interview_period": "September - October",
            "shortlist_announcement": "November",
            "final_result_acceptance_deadline": "December",
            "visa_application_window": "August - September",
            "semester_commencement": "October 1 (Winter Semester)",
            "annual_cycle_notes": "Main annual application deadline for international students already in Germany or with admission is July 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic excellence and grade point average in home country)",
            "extracurricular_and_leadership_weight": "35% (Demonstrated voluntary engagement in civic, religious, or community initiatives)",
            "research_experience_weight": "10% (Technical depth and societal relevance of study plan/thesis)",
            "work_experience_weight": "5% (Practical experience in social sector or engineering)",
            "personal_statement_weight": "10% (Clarity of civic essay and alignment with democratic values)",
            "recommendations_weight": "5% (Academic and civic reference appraisals)",
            "interview_weight": "0% (Interview performance factored directly into final committee vote)",
            "test_scores_weight": "0% (German B2 language proficiency fulfills qualification threshold)",
            "financial_need_weight": "0% (Pure merit and civic leadership evaluation; stipend follows BMBF regulations)",
            "selection_panel_composition": "KAS Independent Selection Committee comprising university professors, politicians, and civil society leaders.",
            "evaluation_methodology": "Two-phase evaluation: preliminary dossier screening followed by an in-depth oral panel interview in German on social ethics and democracy."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,000 international applicants globally",
            "total_scholarships_awarded": "~120 to 180 international fellowships awarded annually",
            "acceptance_rate_global": "~6% to 8%",
            "acceptance_rate_pakistan": "~4% to 6% among applicants with German B2 skills and proven community leadership",
            "typical_successful_applicant_gpa": "CGPA 3.50+ / 4.00 accompanied by substantial volunteer service and articulate German communication",
            "typical_academic_and_research_profile": "Academically sound scholars with articulate perspectives on human dignity, democratic pluralism, and ethical governance.",
            "common_backgrounds_of_winners": "Graduates active in community mobilization, student leadership, interfaith dialogue, and social entrepreneurship.",
            "high_representation_countries": "Pakistan, India, Colombia, Brazil, Ukraine, Georgia, Nigeria, Kenya.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of private education agencies claiming to guarantee political foundation scholarships in Germany.",
                "Applications are accepted exclusively via https://www.kas.de/."
            ],
            "application_fee_warning": "KAS does NOT charge any application fee. Any request for payment is fraudulent.",
            "agent_and_intermediary_warnings": "KAS does not work with commercial agents or consultants.",
            "hidden_costs_breakdown": [
                "German B2 examination fee (Goethe-Institut): ~PKR 35,000.",
                "Uni-Assist university application fee: €75 (~PKR 23,000).",
                "German visa processing and courier fees: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~€300 (~PKR 90,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without German language skills. Reality: KAS strictly requires a certified B2 German language certificate for international scholarship applicants.",
                "Myth: You must be Christian. Reality: KAS accepts scholars of all religious backgrounds who identify with universal ethical values, human dignity, and democratic pluralism."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim KAS is only for political science; KAS actively funds high-performing STEM students committed to ethical technology."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and earn required ECTS credits each semester.",
            "attendance_requirements": "Full-time campus study in Germany and mandatory participation in KAS's seminar program (Ideelle Förderung).",
            "academic_progress_monitoring": "Biannual submission of academic transcripts and reports on civic activities to the KAS advisor.",
            "work_restrictions_during_study": "Part-time student work is subject to BMBF income deduction rules if earnings exceed designated allowances.",
            "home_country_return_obligation": "No mandatory return requirement; scholars are free to pursue careers in Germany or globally.",
            "service_obligations_or_bonds": "Active participation in local KAS scholarship groups (Hochschulgruppen) and alumni networks.",
            "repayment_clawback_conditions": "Revocation of fellowship in case of gross academic negligence, criminal misconduct, or ethical violations.",
            "rules_for_changing_university": "Permitted with prior written notification to KAS, provided studies remain in Germany.",
            "rules_for_changing_major": "Permitted once with valid academic justification and prior approval.",
            "extension_policy": "Extensions beyond standard study duration granted only under exceptional documented circumstances."
        },
        "official_sources_verified": [
            {
                "source_name": "Konrad-Adenauer-Stiftung Official Scholarships Portal",
                "source_url": "https://www.kas.de/en/web/begabtenfoerderung-und-kultur/auslaenderfoerderung",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Federal Ministry of Education and Research (BMBF) Begabtenförderungswerke",
                "source_url": "https://www.bmbf.de/bmbf/en/education/higher-education/funding-for-gifted-students/funding-for-gifted-students.html",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-EU-051": {
        "scholarship_id": "SCH-EU-051",
        "basic_details": {
            "scholarship_name": "Tampere University International Master's Scholarship & Finland Scholarship",
            "offering_entity": "Tampere University (Tampereen yliopisto) & Finnish Ministry of Education and Culture",
            "host_country": "Finland",
            "host_institutions_covered": "Tampere University City Centre & Hervanta Campuses (Tampere, Pirkanmaa, Finland)",
            "degree_levels": ["Master of Science (MSc)"],
            "major_restrictions": "Faculty of Information Technology and Communication Sciences (ITC) & Faculty of Engineering and Natural Sciences: Computing Sciences (Data Science, Artificial Intelligence, Software Engineering, Human-Technology Interaction), Wireless Communications, Robotics and Autonomous Systems, and Electrical Engineering.",
            "number_of_awards_total": "~120 to 180 tuition waivers and Finland Scholarships awarded annually across international Master's programmes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani computing and engineering graduates secure ~12 to 18 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (full standard duration of 120 ECTS Master of Science program), renewal in year 2 contingent on completing minimum 55 ECTS in year 1",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "€5,000 one-time Finland Scholarship relocation grant (~PKR 1,500,000) + campus research assistant earnings"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International non-EU/EEA students liable for tuition fees in Finland (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction; candidates evaluated on previous academic excellence and prerequisite coursework.",
            "academic_qualifications": "A recognized 4-year Bachelor of Science / Engineering in Computer Science, Software Engineering, Electrical Engineering, or related technical field (16 years education) with minimum CGPA 3.30 / 4.00 (or 75%+ marks) from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum ECTS grade equivalent of Grade B+ or Finnish grade 3.5 / 5.0 in major technical subjects.",
            "subject_background_prerequisites": "Rigorous undergraduate coursework in programming languages (Python, Java, C++), algorithms, data structures, discrete mathematics, and computer systems.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with official provisional transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; technical internships, open-source software contributions, or robotics projects strengthen application.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 92,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (minimum 5.5 in writing) or TOEFL iBT minimum 92 (minimum 20 in writing). Standardized English score report is mandatory under Finnish university admissions criteria.",
            "other_language_requirements": "None; international Master's programmes are taught and examined 100% in English.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply for the scholarship directly on Studyinfo.fi at the same time they apply for degree admission in January.",
            "previous_scholarship_restrictions": "Cannot hold another full Finnish state or university tuition scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver (worth €12,000 / year; €24,000 total) covering the entire 2-year duration of the Master of Science program.",
                "amount": "100% covered (~€12,000 / year; ~PKR 3,600,000 / year value)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Online application via the official Finnish national portal Studyinfo.fi is completely free of charge.",
                "amount": "€0"
            },
            "accommodation": {
                "status": "PARTIAL",
                "details": "Subsidized student apartments arranged via Tampere Student Housing Foundation (TOAS - Tampereen seudun opiskelija-asuntosäätiö); monthly rent €280 - €420 including heating, water, electricity, and high-speed internet.",
                "amount": "Subsidized TOAS apartment ~€320 / month"
            },
            "monthly_stipend": {
                "status": "PARTIAL",
                "details": "Finland Scholarship recipients receive an immediate €5,000 relocation grant disbursed into their Finnish bank account upon arrival. Departmental student research assistantships pay €12 - €16/hour for up to 20 hours/week.",
                "amount": "€5,000 one-time grant (~PKR 1,500,000) + part-time research assistant wages"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare to Helsinki/Tampere arranged by student; covered by the €5,000 arrival grant.",
                "amount": "Self-funded via arrival grant (~PKR 200,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Finnish Immigration Service (Migri) student residence permit electronic application fee (€350).",
                "amount": "€350 (~PKR 105,000)"
            },
            "health_insurance": {
                "status": "PARTIAL",
                "details": "Private insurance policy (Swisscare/SIP ~€250/year) required for Migri residence permit; on campus, Finnish Student Health Service (FSHS / YTHS) provides full health care for ~€74/year.",
                "amount": "Private insurance ~€250/year; campus care via FSHS"
            },
            "food_allowance": {
                "status": "PARTIAL",
                "details": "State-subsidized Kela student lunches available across campus cafeterias (Juvenes / Sodexo) for €2.95 per meal.",
                "amount": "Subsidized Kela meals (€2.95 per meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full borrowing privileges at Tampere University Library, Hervanta engineering laboratories, and supercomputing clusters.",
                "amount": "100% covered by university resources"
            },
            "research_funding_conference_grant": {
                "status": "PARTIAL",
                "details": "Faculty travel grants available for Master's students co-authoring scientific publications presented at European research conferences.",
                "amount": "Up to €1,200 per year"
            },
            "travel_transit_allowance": {
                "status": "PARTIAL",
                "details": "Nysse (Tampere Regional Transport) offers 50% student discounts on monthly tram and bus travel passes (~€38 / month).",
                "amount": "50% student discount on local transit"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-class multidisciplinary technical institution: Tampere University (formed from merger of Tampere University of Technology and University of Tampere).",
            "participating_institutions": [
                "Tampere University (Hervanta Campus & City Centre Campus, Tampere, Finland)"
            ],
            "university_rankings_scope": "Consistently ranked top 350 globally in QS/THE World Rankings; globally recognized for research in Wireless Communications, Human-Technology Interaction, AI, and Robotics.",
            "available_majors": [
                "Computing Sciences (Data Science)",
                "Computing Sciences (Artificial Intelligence)",
                "Computing Sciences (Software Engineering)",
                "Computing Sciences (Human-Technology Interaction)",
                "Wireless Communications and RF Systems",
                "Robotics and Autonomous Systems",
                "Electrical Engineering (Smart Grids)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (4 semesters, 120 ECTS)",
            "admission_requirements_summary": "Bachelor's degree in relevant discipline, certified academic transcripts, motivation letter, CV, and standardized English test score (IELTS 6.5 or TOEFL 92).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Data Science and Artificial Intelligence tracks at Hervanta campus receive extreme international application volumes; strong programming and calculus foundations yield highest ranking scores.",
            "strategic_program_match_advice": "When completing your Studyinfo.fi application in January, check the box requesting the 'Tampere University Tuition Fee Scholarship / Finland Scholarship'—no separate scholarship portal is needed."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://opintopolku.fi/konfo/en/ & https://www.tuni.fi/en/study-with-us/how-to-apply/scholarships",
            "portal_system_name": "Studyinfo.fi (Finnish National Application System)",
            "account_creation_instructions": "Submit application on Studyinfo.fi during the annual January joint application window, select Tampere University degree programmes, opt-in for the scholarship, and upload digital document scans.",
            "step_by_step_workflow": [
                "Step 1: Check prerequisite courses and prepare IELTS (min 6.5) or TOEFL (min 92) test scores.",
                "Step 2: Submit application on Studyinfo.fi during the joint application period (early to mid-January).",
                "Step 3: Select the checkbox requesting the Tampere University Scholarship and Finland Scholarship.",
                "Step 4: Upload attested transcripts, degree certificates, CV, and motivational letter before the document deadline.",
                "Step 5: Admissions committee reviews academic files and announces admission and scholarship results by late March or early April.",
                "Step 6: Confirm acceptance of the study place and scholarship offer via Studyinfo.fi before the national deadline in July.",
                "Step 7: Apply for Finnish residence permit for studies via Enter Finland (Migri) and book biometric appointment at VFS Global Islamabad."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via Studyinfo.fi covers both degree admission and scholarship allocation.",
            "recommendation_letters_submission_method": "Not required for general admission; only uploaded if specifically requested for interdisciplinary tracks.",
            "personal_statement_prompts": "Integrated motivation questions embedded within the online application addressing academic background, motivation, and career plans.",
            "study_plan_research_proposal_requirements": "Summary of proposed Master's thesis focus in AI, data science, or robotics.",
            "cv_format_requirements": "Standard academic CV (Europass format preferred) detailing education, technical competencies, and software projects.",
            "interviews_conducted": False,
            "interview_format_details": "Evaluation is conducted based on documented academic credentials and motivation essay.",
            "standardized_tests": "IELTS Academic (min 6.5, writing 5.5) or TOEFL iBT (min 92, writing 20); GRE not required.",
            "application_fee_amount": "€0 (Free on Studyinfo.fi)",
            "attestation_requirements": "Bachelor's degree and transcripts must be attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation of all non-English documents.",
            "final_submission_method": "Online upload via Studyinfo.fi."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's Degree Certificate and Academic Transcripts",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's in CS/SE/EE with minimum CGPA 3.30/4.00.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 5.5 writing) or TOEFL iBT (min 92, 20 writing).",
                "pakistan_specific_instruction": "Send electronic score report directly to Tampere University via testing agency."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed CV listing education, programming abilities, projects, and work experience.",
                "pakistan_specific_instruction": "Include links to GitHub and technical portfolios."
            },
            {
                "document_name": "Motivation Letter / Statement of Purpose",
                "mandatory": True,
                "specification": "Structured motivation essay answering specific prompt questions on Studyinfo.",
                "pakistan_specific_instruction": "Emphasize alignment with Tampere's AI, wireless, or robotics research labs."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of passport bio page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must be valid through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "January 3",
            "application_deadline": "January 17",
            "university_admission_deadline": "January 17",
            "document_submission_deadline": "January 24",
            "recommendation_letters_deadline": "Not applicable",
            "interview_period": "Not applicable",
            "shortlist_announcement": "Late March - Early April",
            "final_result_acceptance_deadline": "Mid-July",
            "visa_application_window": "April - June",
            "semester_commencement": "Late August / Early September",
            "annual_cycle_notes": "Finland conducts a unified nationwide Joint Application period in January. Missing the mid-January deadline means waiting an entire year."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Undergraduate GPA and performance in core mathematical and computing courses)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular achievements and innovation contests)",
            "research_experience_weight": "15% (Undergraduate capstone project, publications, and technical depth)",
            "work_experience_weight": "5% (Industry internships or engineering experience)",
            "personal_statement_weight": "15% (Motivation letter quality and career goal clarity)",
            "recommendations_weight": "0% (Not factored into composite score)",
            "interview_weight": "0% (Document-based merit ranking)",
            "test_scores_weight": "0% (Language proficiency fulfills qualification threshold)",
            "financial_need_weight": "0% (Pure academic merit ranking)",
            "selection_panel_composition": "Faculty of ITC Academic Admissions Board at Tampere University.",
            "evaluation_methodology": "Point-based scoring rubric evaluating degree relevance, GPA percentile, and motivation letter quality."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,600 international applicants across Computing Sciences programs",
            "total_scholarships_awarded": "~120 to 180 full/partial tuition waivers and Finland Scholarships",
            "acceptance_rate_global": "~7% to 10% for admission; ~4% to 6% for 100% full scholarship",
            "acceptance_rate_pakistan": "~6% to 9% among applicants with strong CGPA (3.4+) in computing and software",
            "typical_successful_applicant_gpa": "CGPA 3.45+ / 4.00 from top Pakistani engineering institutions (NUST, FAST, GIKI, UET, NED)",
            "typical_academic_and_research_profile": "Graduates of accredited computing and engineering faculties with solid programming foundations and practical capstone projects.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, software engineering, and electronics departments.",
            "high_representation_countries": "Pakistan, India, Bangladesh, Iran, China, Vietnam, Nigeria, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent consultancy firms claiming to guarantee Finnish student visas or scholarships.",
                "Applications must be filed exclusively through opintopolku.fi (Studyinfo.fi)."
            ],
            "application_fee_warning": "Studyinfo.fi and Tampere University do NOT charge application fees for degree programs.",
            "agent_and_intermediary_warnings": "Tampere University does not authorize agents to make admissions or scholarship decisions.",
            "hidden_costs_breakdown": [
                "Finnish Migri residence permit electronic fee: €350 (~PKR 105,000).",
                "VFS Global Islamabad biometrics appointment: ~PKR 12,000.",
                "Mandatory health insurance (Swisscare): ~€250 (~PKR 75,000).",
                "IELTS/TOEFL exam fee: ~PKR 60,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You need to pay the first year tuition before getting the scholarship. Reality: The Finland Scholarship / Tampere waiver is awarded directly in the admission letter and credited upfront.",
                "Myth: You cannot work in Finland during studies. Reality: International students in Finland have the legal right to work up to 30 hours per week during term time."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial agencies suggest spring application deadlines; the actual Finnish Joint Application window closes strictly in mid-January."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must complete at least 55 ECTS credits during the first academic year to renew the tuition fee waiver for the second year.",
            "attendance_requirements": "Full-time campus study and registration in Tampere, Finland.",
            "academic_progress_monitoring": "Annual transcript audit by the university registrar at the conclusion of spring semester.",
            "work_restrictions_during_study": "Permitted to work up to 30 hours per week under Finnish immigration law.",
            "home_country_return_obligation": "No return obligation; Finland grants a 2-year post-study job seeker residence permit upon graduation.",
            "service_obligations_or_bonds": "Zero service bonds or repayment clauses.",
            "repayment_clawback_conditions": "Scholarship is withdrawn if student drops out or fails to meet the ECTS progress threshold.",
            "rules_for_changing_university": "Non-transferable to other Finnish universities.",
            "rules_for_changing_major": "Changing major requires a new application in the subsequent joint application round.",
            "extension_policy": "Scholarship covers standard 2-year duration; third-year studies incur regular tuition fees unless special waiver granted."
        },
        "official_sources_verified": [
            {
                "source_name": "Tampere University Official Scholarships Portal",
                "source_url": "https://www.tuni.fi/en/study-with-us/how-to-apply/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Studyinfo.fi Finnish National Higher Education Portal",
                "source_url": "https://opintopolku.fi/konfo/en/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-EU-053": {
        "scholarship_id": "SCH-EU-053",
        "basic_details": {
            "scholarship_name": "Erasmus Mundus Master in Green, Networked and Inspiring AI (GENIAL)",
            "offering_entity": "European Commission (EACEA) & GENIAL Consortium Universities",
            "host_country": "France / Sweden / Italy / Finland",
            "host_institutions_covered": "Université de Lorraine (France - Coordinator), KTH Royal Institute of Technology (Sweden), University of Naples Federico II (Italy), and Lappeenranta-Lahti University of Technology LUT (Finland)",
            "degree_levels": ["Master of Science (MSc - Multiple Master's Degrees)"],
            "major_restrictions": "Green and Networked Sustainable AI: Low-Power AI Hardware, Energy-Efficient Machine Learning, Edge AI and Green 6G Networks, Sustainable Computing Architectures, and Ethical AI Systems.",
            "number_of_awards_total": "~20 to 25 fully funded Erasmus Mundus scholarship grants awarded globally per annual cohort",
            "number_of_awards_pakistan": "Open global competition (Partner Country category); Pakistani AI, software, and electronic engineers secure ~2 to 4 full scholarships annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (full standard duration of 120 ECTS Joint Master's program across minimum 2-3 European partner institutions)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "€1,400 / month tax-free living allowance for full 24 months (€33,600 total)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to applicants worldwide (Partner Country category for Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit; evaluated on academic excellence, technical competencies, and motivation.",
            "academic_qualifications": "A recognized 4-year Bachelor of Science / Engineering in Computer Science, Artificial Intelligence, Electrical/Electronic Engineering, or Telecommunications (16 years education, 180-240 ECTS equivalent) with minimum CGPA 3.40 / 4.00 (or 78%+ aggregate) from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "First-class honors or top 10% class percentile equivalent.",
            "subject_background_prerequisites": "Rigorous undergraduate foundation in programming (Python, C/C++), machine learning, digital signal processing or electronics, linear algebra, calculus, and probability.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally provided degree certificate is awarded prior to program commencement in September.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Experience in embedded AI, tinyML, renewable energy systems, or green computing strengthens candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (minimum 6.0 in each sub-score) or TOEFL iBT minimum 90 (minimum 20 in each sub-score). Standardized test is mandatory under Erasmus Mundus consortium rules.",
            "other_language_requirements": "None; instruction and examinations across all partner universities are 100% in English.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates apply through the centralized GENIAL online portal hosted by Université de Lorraine.",
            "previous_scholarship_restrictions": "Applicants who have previously received an Erasmus Mundus Joint Master Degree (EMJMD) scholarship are not eligible for a second one.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full participation and tuition fee waiver (€9,000 / year for Partner Country students) covering all consortia universities, laboratory fees, and library charges.",
                "amount": "100% covered (€18,000 total 2-year value; ~PKR 5,400,000)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Online application via the official GENIAL consortium portal is completely free of charge.",
                "amount": "€0"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Consortium universities assist with reserved student housing in Nancy, Stockholm, Naples, and Lappeenranta; rent is paid from the generous monthly living stipend.",
                "amount": "Covered via monthly stipend (€350 - €650 / month rent)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living allowance of €1,400 per month disbursed for the full 24 months of the programme (€33,600 total; ~PKR 420,000 / month; ~PKR 10,080,000 total).",
                "amount": "€1,400 / month (~PKR 420,000 / month; €16,800 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Consortium travel and installation grant embedded into the Erasmus+ scholarship allocation, covering international flights between Pakistan and European study tracks.",
                "amount": "€3,000 / year travel contribution (~PKR 900,000 / year)"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Schengen study visa and national residence permit fees across France, Sweden, Italy, and Finland are covered from the scholarship installation allocation.",
                "amount": "Covered via installation grant"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive worldwide private health, accident, and repatriation insurance policy (Marsh or Dr. Walter) compliant with EACEA standards provided 100% free.",
                "amount": "100% covered by the European Commission"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered through the monthly living stipend of €1,400.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to specialized AI hardware labs, FPGA boards, edge TPU clusters, and university computing licenses.",
                "amount": "100% provided by consortium infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Consortium funding available for students presenting their Master's thesis research at major international AI and green computing conferences.",
                "amount": "Up to €1,500 for conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Inter-consortium mobility travel costs between Year 1 and Year 2 institutions (e.g., France to Sweden or Italy) are fully covered.",
                "amount": "100% covered via mobility grant"
            },
            "total_estimated_value_usd_per_year": 32000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple premier European institutions (consortium mobility across at least two EU countries is mandatory).",
            "participating_institutions": [
                "Université de Lorraine (Nancy, France - Coordinator)",
                "KTH Royal Institute of Technology (Stockholm, Sweden)",
                "University of Naples Federico II (Naples, Italy)",
                "LUT University (Lappeenranta, Finland)"
            ],
            "university_rankings_scope": "Consortium features KTH Royal Institute of Technology (top 80 globally in QS World Rankings, #1 in Sweden for engineering) and Université de Lorraine (renowned for INRIA AI research).",
            "available_majors": [
                "Green AI Foundations and Energy-Efficient Computing (Semester 1 - Nancy)",
                "Edge AI and Embedded Low-Power Systems (Track at KTH)",
                "Green Wireless Networks and AI-Driven Communications (Track at Naples)",
                "Sustainable Software Engineering and Circular AI Systems (Track at LUT)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (4 semesters, 120 ECTS)",
            "admission_requirements_summary": "Recognized 4-year Bachelor's degree in CS/AI/EE (180-240 ECTS equivalence), minimum CGPA 3.4/4.0, standardized English test (IELTS 6.5 or TOEFL 90), two academic recommendation letters, CV, and motivation essay.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "All applicants enter a centralized global competition; top-ranked scholars receive both program admission and the prestigious Erasmus Mundus scholarship.",
            "strategic_program_match_advice": "Highlight your passion for sustainable AI and energy efficiency—addressing the carbon footprint of massive AI models, TinyML, and edge intelligence—to align with GENIAL's core mission."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://master-genial.eu/ & https://master-genial.eu/apply/",
            "portal_system_name": "GENIAL Centralized Online Application System (Université de Lorraine)",
            "account_creation_instructions": "Register an account on the GENIAL application portal, complete the online application form, designate preferred Year 2 specialization mobility tracks, and upload all required documents.",
            "step_by_step_workflow": [
                "Step 1: Review GENIAL academic prerequisites and ensure valid English test scores (IELTS min 6.5 or TOEFL min 90).",
                "Step 2: Register on the GENIAL online application portal (https://master-genial.eu/apply/).",
                "Step 3: Complete the academic profile, curriculum details, and preferred specialization track selections.",
                "Step 4: Enter contact details for two academic referees who will receive automated links to submit confidential recommendation letters.",
                "Step 5: Upload attested transcripts, Bachelor's degree certificate, detailed CV, motivation letter, and passport copy before the deadline (typically January 31).",
                "Step 6: Consortium Academic Selection Board ranks all global applications and submits scholarship nomination list to EACEA.",
                "Step 7: Shortlisted and selected candidates receive formal scholarship offer letters in late March or early April.",
                "Step 8: Accept scholarship offer, receive official visa support package from Université de Lorraine, and apply for French Long-Stay Student Visa (VLS-TS) at the Embassy of France in Islamabad."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Single application via the GENIAL portal serves as both program admission and Erasmus Mundus scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated institutional links dispatched directly to their official university email addresses.",
            "personal_statement_prompts": "Structured motivation letter (maximum 2 pages) addressing technical background, motivation for green and sustainable AI, choice of mobility tracks, and career aspirations.",
            "study_plan_research_proposal_requirements": "Summary of technical domain of interest and intended thesis research direction in energy-efficient AI or edge systems.",
            "cv_format_requirements": "Europass CV detailing academic qualifications, technical skills, programming languages, and projects.",
            "interviews_conducted": False,
            "interview_format_details": "Selection is purely dossier-based; online interviews are conducted only in rare borderline instances.",
            "standardized_tests": "IELTS Academic (min 6.5 overall, 6.0 sub-scores) or TOEFL iBT (min 90, 20 sub-scores); GRE is recommended but not mandatory.",
            "application_fee_amount": "€0 (Free on GENIAL portal)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC and MOFA Pakistan; Matric/Inter by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Online submission via the GENIAL central application system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's Degree Certificate and Academic Transcripts",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's in CS/AI/EE with minimum CGPA 3.40/4.00.",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each section) or TOEFL iBT (min 90, 20 in each section).",
                "pakistan_specific_instruction": "Score report valid at time of application."
            },
            {
                "document_name": "Two Academic Recommendation Letters",
                "mandatory": True,
                "specification": "Confidential recommendation letters from university professors who taught or supervised previous research.",
                "pakistan_specific_instruction": "Referees must submit from institutional Pakistani university email addresses."
            },
            {
                "document_name": "Structured Motivation Letter",
                "mandatory": True,
                "specification": "Maximum 2-page essay detailing background, technical competencies, and motivation for sustainable AI.",
                "pakistan_specific_instruction": "Demonstrate clear knowledge of the GENIAL curriculum and consortium universities."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Europass CV highlighting technical skills, programming proficiencies, and projects.",
                "pakistan_specific_instruction": "Include links to GitHub and academic code repositories."
            },
            {
                "document_name": "Proof of Residence Certificate",
                "mandatory": True,
                "specification": "Official certificate confirming permanent residence in Pakistan for the last 12 months (e.g. utility bill, domicile, employer/university letter).",
                "pakistan_specific_instruction": "Required under Erasmus Mundus 12-month residency rule."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "High-resolution color scan of passport bio page valid for at least 3 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "November 1",
            "application_deadline": "January 31",
            "university_admission_deadline": "January 31",
            "document_submission_deadline": "January 31",
            "recommendation_letters_deadline": "February 7",
            "interview_period": "February (if conducted)",
            "shortlist_announcement": "Late March",
            "final_result_acceptance_deadline": "Mid-April",
            "visa_application_window": "May - July",
            "semester_commencement": "Early September (commencing at Université de Lorraine, Nancy)",
            "annual_cycle_notes": "Centralized global application period runs annually from November to late January. Strict cutoff."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Undergraduate GPA and performance in core AI, computing, and mathematics courses)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular leadership and open-source community engagement)",
            "research_experience_weight": "25% (Final year capstone project, publications, technical code portfolio, and work experience)",
            "work_experience_weight": "5% (Industry AI, software development, or embedded engineering experience)",
            "personal_statement_weight": "15% (Quality of motivation letter, clarity of sustainable AI vision, and articulation)",
            "recommendations_weight": "10% (Quality and depth of academic appraisals from professors)",
            "interview_weight": "0% (Dossier-based scoring rubric)",
            "test_scores_weight": "0% (Language proficiency fulfills eligibility threshold)",
            "financial_need_weight": "0% (Pure academic and technical merit ranking)",
            "selection_panel_composition": "Joint Academic Board comprising professors and coordinators from all 4 consortium universities.",
            "evaluation_methodology": "Two independent academic reviewers score each dossier according to a standardized 100-point rubric, followed by composite consortium ranking."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,200 international applicants worldwide",
            "total_scholarships_awarded": "~20 to 25 Erasmus Mundus full scholarship awards globally",
            "acceptance_rate_global": "~1.0% to 1.5%",
            "acceptance_rate_pakistan": "~2.0% to 3.0% among high-caliber computing and electronics applicants",
            "typical_successful_applicant_gpa": "CGPA 3.60+ / 4.00 or top 5% class rank from premier Pakistani computing universities (FAST-NUCES, NUST, LUMS, GIKI, UET)",
            "typical_academic_and_research_profile": "Graduates with exceptional computing and electronics foundations, strong machine learning practices, published research, or substantial GitHub project portfolios.",
            "common_backgrounds_of_winners": "Graduates of Pakistani computer science, artificial intelligence, and electronic engineering faculties.",
            "high_representation_countries": "Pakistan, India, China, Vietnam, Nigeria, Brazil, Turkey, Colombia, Egypt.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell Erasmus Mundus scholarship spots.",
                "Applications are submitted solely via https://master-genial.eu/."
            ],
            "application_fee_warning": "GENIAL does NOT charge any application fee. Any request for money is fraudulent.",
            "agent_and_intermediary_warnings": "The GENIAL Consortium and the European Commission do not work with commercial agents or agencies.",
            "hidden_costs_breakdown": [
                "French student visa administrative fee: €99 (~PKR 30,000).",
                "IELTS/TOEFL examination registration: ~PKR 60,000.",
                "Police character certificate and legal attestations in Pakistan: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer in France: ~€400 (~PKR 120,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can stay in one university for the full 2 years. Reality: Erasmus Mundus requires mobility across at least two different European countries during the Master's program.",
                "Myth: The scholarship stipend must be repaid if you don't return to Pakistan. Reality: Erasmus Mundus scholarships carry zero repayment obligations; scholars are free to pursue global careers or PhDs in Europe."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial websites claim GRE is required; GRE is recommended by GENIAL but is NOT strictly mandatory."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance and earn 60 ECTS per year without fail grades across all consortium universities.",
            "attendance_requirements": "Full-time physical attendance and mandatory participation in consortium academic activities and summer workshops.",
            "academic_progress_monitoring": "Semester-by-semester credit audit by the Consortium Coordinating Board at Université de Lorraine.",
            "work_restrictions_during_study": "Part-time work is legally permitted under national student visa rules in France, Sweden, Italy, and Finland, but discouraged due to intensive curriculum.",
            "home_country_return_obligation": "Zero return obligation; graduates receive European joint/multiple degrees and are eligible for European post-study work permits.",
            "service_obligations_or_bonds": "Active participation in Erasmus Mundus Students and Alumni Association (EMA) activities.",
            "repayment_clawback_conditions": "Stipend discontinued upon unapproved abandonment of studies or expulsion for academic misconduct.",
            "rules_for_changing_university": "Mobility tracks are fixed according to selected curriculum specializations approved by the consortium.",
            "rules_for_changing_major": "Not applicable; curriculum is unified under the Green, Networked and Inspiring AI joint framework.",
            "extension_policy": "Scholarship is granted for maximum 24 months; thesis completion beyond 24 months must be self-funded."
        },
        "official_sources_verified": [
            {
                "source_name": "Erasmus Mundus GENIAL Official Consortium Portal",
                "source_url": "https://master-genial.eu/",
                "source_type": "OFFICIAL_COMMISSION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "European Education and Culture Executive Agency (EACEA) Erasmus Mundus Catalogue",
                "source_url": "https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
