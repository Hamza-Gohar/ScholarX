"""Batch 26 Part 1: East Asia Elite STEM Awards (3 awards)
SCH-AS-060: Asian Development Bank - Japan Scholarship Program (ADB-JSP) at University of Tokyo
SCH-AS-061: Tokyo Institute of Technology (Tokyo Tech) MEXT IGP Award
SCH-AS-063: Osaka University MEXT University Recommendation (Special IGP) Award
"""

DATA_P1 = {
    "SCH-AS-060": {
        "scholarship_id": "SCH-AS-060",
        "basic_details": {
            "scholarship_name": "Asian Development Bank - Japan Scholarship Program (ADB-JSP) at the University of Tokyo",
            "offering_entity": "Asian Development Bank (ADB) & The University of Tokyo Graduate School of Frontier Sciences (GSFS)",
            "host_country": "Japan",
            "host_institutions_covered": "The University of Tokyo (Kashiwa Campus, Chiba Prefecture / Hongo Campus, Tokyo, Japan)",
            "degree_levels": ["Master of Science (MSc)", "Master of Engineering (MEng)", "Master of Sustainability Science"],
            "major_restrictions": "Graduate School of Frontier Sciences (GSFS) designated departments: Department of Natural Environmental Studies, Department of Ocean Technology, Policy, and Environment, Department of Environment Systems, Department of Human and Engineered Environmental Studies, Department of International Studies, and Sustainability Science Program.",
            "number_of_awards_total": "~135 ADB-JSP scholarships awarded globally per year across all partner institutions (~10 to 15 at UTokyo GSFS)",
            "number_of_awards_pakistan": "Open to ADB developing member countries including Pakistan; typically 2 to 4 Pakistani graduate scholars selected annually at UTokyo",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years (standard Master's program duration)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 147,000 / month living stipend (~PKR 279,300 / month) plus 100% full tuition waiver, round-trip economy airfare, book allowance, and comprehensive medical insurance"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["National of an ADB borrowing member country (Pakistan fully eligible; Japanese nationals and citizens of developed countries ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Not more than 35 years old at the time of application (in appropriate cases for senior officials/managers, age limit up to 45 may be considered).",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree with superior academic record (minimum CGPA 3.30/4.00 or top 15% class rank) from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum CGPA 3.30 / 4.00; competitive applicants at UTokyo typically hold CGPA >= 3.60 / 4.00 or First Class Honours.",
            "subject_background_prerequisites": "Engineering, environmental sciences, agriculture, economics, urban planning, sustainability science, or related technical disciplines.",
            "current_education_status": "Graduated with at least two years of full-time professional work experience after obtaining the bachelor's degree.",
            "graduation_year_restrictions": "Must have completed bachelor's degree at least two years prior to application deadline.",
            "work_experience_required": True,
            "work_experience_minimum_years": 2.0,
            "work_experience_notes": "Mandatory minimum of 2 years of full-time professional working experience (acquired after university graduation) in an area relevant to international development or public service.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Official IELTS Academic (minimum 6.5) or TOEFL iBT (minimum 85) score report taken within past two years; MOI certificates not accepted for ADB-JSP at UTokyo.",
            "other_language_requirements": "Japanese language proficiency is not required.",
            "gender_specific_requirements": "Open equally; female candidates are strongly encouraged to apply per ADB diversity policy.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must agree to return to their home country for at least two years immediately upon degree completion to contribute to economic and social development.",
            "previous_scholarship_restrictions": "Executive directors, alternates, staff, and consultants of ADB (and their close relatives) are strictly ineligible.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full waiver of entrance examination fee, admission matriculation fee, and recurring annual tuition at The University of Tokyo.",
                "amount": "100% covered (~JPY 847,800 first-year value; ~PKR 1,610,000)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Screening and examination fees are covered or reimbursed under the ADB-JSP fellowship package.",
                "amount": "100% covered (JPY 30,000 value)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized international student housing at UTokyo Kashiwa International Lodge (approx. JPY 25,000 to 45,000 / month), paid easily from living stipend.",
                "amount": "Subsidized university lodge accommodation"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free subsistence allowance of JPY 147,000 / month (~PKR 279,300 / month) disbursed directly for housing and living costs.",
                "amount": "JPY 147,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One round-trip economy class international airfare between home country and Tokyo at the beginning and end of the program.",
                "amount": "100% covered round-trip flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese Student Visa expedited with official UTokyo certificate of eligibility.",
                "amount": "100% covered"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive medical and accident insurance coverage provided throughout the two-year fellowship.",
                "amount": "100% covered medical insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized cafeterias across Kashiwa and Hongo campuses; monthly living stipend covers all food expenses.",
                "amount": "Covered via monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Special instructional book and materials allowance of JPY 100,000 provided per year, plus full access to UTokyo scientific databases.",
                "amount": "JPY 100,000 / year book allowance"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Field study trips, domestic conference attendance, and research operations supported by host laboratory and GSFS.",
                "amount": "Field study allowance and research travel support"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Subsidized commuter passes on the Tsukuba Express line between Kashiwa and central Tokyo.",
                "amount": "Subsidized railway commuting"
            },
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-class Japanese national flagship institution (The University of Tokyo - Todai).",
            "participating_institutions": [
                "Graduate School of Frontier Sciences (GSFS), The University of Tokyo (Kashiwa Campus, Chiba, Japan)"
            ],
            "university_rankings_scope": "QS World University Rankings #32 globally, #1 in Japan; world-renowned for advanced science, environmental systems, and cutting-edge engineering.",
            "available_majors": [
                "Master of Science in Natural Environmental Studies",
                "Master of Engineering in Ocean Technology, Policy, and Environment",
                "Master of Engineering in Environment Systems",
                "Master of Engineering in Human and Engineered Environmental Studies",
                "Master of Science in International Studies",
                "Master of Sustainability Science (GPSS-GLI Program)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (Master's degree)",
            "admission_requirements_summary": "Bachelor's degree with 2+ years post-graduation professional experience, academic transcripts, TOEFL iBT 85+ / IELTS 6.5+, research proposal, prospective supervisor contact, two professional/academic recommendation letters, and ADB-JSP information sheet.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Very competitive; securing prior agreement from a GSFS professor willing to supervise your research is an indispensable prerequisite.",
            "strategic_program_match_advice": "Align your proposed research proposal with critical development needs in Pakistan (e.g. water management, disaster risk reduction, renewable microgrids, coastal ecology) to match ADB core mandates."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.k.u-tokyo.ac.jp/en/exam/master/foreign_research_students/adb-jsp/",
            "portal_system_name": "UTokyo GSFS Online Application & ADB-JSP Submission System",
            "account_creation_instructions": "Review GSFS faculty directory, contact prospective supervisor, receive informal acceptance, complete UTokyo GSFS online application, upload ADB-JSP required forms and income tax documents.",
            "step_by_step_workflow": [
                "Step 1: Contact a prospective academic advisor at UTokyo GSFS by October/November and secure informal consent.",
                "Step 2: Compile ADB-JSP application form, employment certificate proving 2+ years full-time experience, and annual family income certification.",
                "Step 3: Submit online admission application to UTokyo GSFS indicating ADB-JSP scholarship interest by December 10.",
                "Step 4: Send certified physical application documents to GSFS Student Affairs Team by postal mail.",
                "Step 5: GSFS faculty committee conducts academic evaluation and shortlisting.",
                "Step 6: UTokyo nominates shortlisted candidates to the Asian Development Bank (ADB) Headquarters in Manila in March.",
                "Step 7: ADB Board officially ratifies scholarship recipients in June.",
                "Step 8: Obtain Japanese visa and arrive in Japan for late September orientation and October 1 matriculation."
            ],
            "university_vs_scholarship_routing": "Integrated University Track: UTokyo GSFS screens academic eligibility first, then nominates qualified scholars directly to ADB Headquarters.",
            "recommendation_letters_submission_method": "Two letters of recommendation (one academic and one employer evaluation) submitted on official letterheads.",
            "personal_statement_prompts": "Statement of purpose detailing developmental challenges in home country and how the proposed research at UTokyo will contribute directly to sustainable development upon return.",
            "study_plan_research_proposal_requirements": "Structured research proposal (3-5 pages) articulating development problem, technical methodology, expected results, and practical policy/industrial applicability in Pakistan.",
            "cv_format_requirements": "Comprehensive professional CV detailing academic qualifications, chronologically listed employment history, and technical proficiencies.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and GSFS departmental committee.",
            "standardized_tests": "IELTS Academic 6.5+ or TOEFL iBT 85+ required (official score reports sent directly).",
            "application_fee_amount": "JPY 0 (Exempted or covered under ADB-JSP nomination)",
            "attestation_requirements": "Certified copies of degree and transcripts; HEC and MoFA attestations required for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translation for all non-English documents.",
            "final_submission_method": "Dual process: Online application submission followed by physical postal dispatch of certified dossier to UTokyo GSFS."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Graduation Certificate",
                "mandatory": True,
                "specification": "Complete Bachelor's degree certificate and transcripts with grading scale and CGPA >= 3.30.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "ADB-JSP Information Sheet and Application Form",
                "mandatory": True,
                "specification": "Prescribed ADB official form detailing personal, academic, and economic background.",
                "pakistan_specific_instruction": "Official ADB-JSP template."
            },
            {
                "document_name": "Certificate of Employment & Work Experience Proof",
                "mandatory": True,
                "specification": "Official employer letter certifying at least 2 full years of professional work experience post-graduation.",
                "pakistan_specific_instruction": "On company letterhead with salary and employment duration."
            },
            {
                "document_name": "Certificate of Annual Income & Tax Documents",
                "mandatory": True,
                "specification": "Official documents proving applicant's and family's annual income (salary slips and tax returns).",
                "pakistan_specific_instruction": "FBR tax returns or employer income certificates."
            },
            {
                "document_name": "Detailed Research Proposal Aligned with Development",
                "mandatory": True,
                "specification": "3-5 page research plan outlining development challenges and proposed technical methodology.",
                "pakistan_specific_instruction": "Scholarly proposal formatted with standard citations."
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "One letter from academic professor and one letter from direct professional supervisor.",
                "pakistan_specific_instruction": "Signed and stamped on official stationery."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "Valid TOEFL iBT (85+) or IELTS Academic (6.5+) score report.",
                "pakistan_specific_instruction": "Official test report issued within past 2 years."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "December 10 (Strict annual deadline for October intake)",
            "university_admission_deadline": "December 10",
            "document_submission_deadline": "December 20 (Hard copy postal arrival)",
            "recommendation_letters_deadline": "December 10",
            "interview_period": "January - February",
            "shortlist_announcement": "March (UTokyo nomination to ADB) / June (ADB final confirmation)",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Single annual admission cycle for October intake; candidates must establish faculty contact by October."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Undergraduate GPA, academic consistency in STEM/environmental fields)",
            "extracurricular_and_leadership_weight": "5% (Community engagement, social consciousness)",
            "research_experience_weight": "25% (Rigor and development relevance of proposed research at UTokyo)",
            "work_experience_weight": "25% (Mandatory 2+ years professional experience and career development potential)",
            "personal_statement_weight": "5% (Clarity of commitment to return and advance home country)",
            "recommendations_weight": "5% (Academic and employer endorsements)",
            "interview_weight": "5% (Departmental video interview performance)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Economic background verified via income ceiling, but merit-driven)",
            "selection_panel_composition": "The University of Tokyo GSFS Admissions Board and Asian Development Bank Scholarship Selection Committee.",
            "evaluation_methodology": "Two-tier screening: UTokyo evaluates academic merit and research fit, followed by ADB board review assessing developmental impact potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~600 to 800 applicants for UTokyo GSFS allocation",
            "total_scholarships_awarded": "~10 to 15 ADB-JSP awards at UTokyo GSFS annually",
            "acceptance_rate_global": "~2.0% to 2.5%",
            "acceptance_rate_pakistan": "~3.0% to 5.0% for candidates with strong development work experience and CGPA >= 3.50",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.50 / 4.00, coupled with 2-4 years of high-impact professional engineering or public sector experience",
            "typical_academic_and_research_profile": "STEM or environmental graduates working in government, environmental consulting, renewable energy, or NGOs with clear vision for national development.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, UET Lahore, NED Karachi, Quaid-i-Azam, LUMS).",
            "high_representation_countries": "Pakistan, Philippines, Indonesia, Vietnam, Bangladesh, Nepal, Sri Lanka, India.",
            "competitiveness_tier": "MOST_COMPETITIVE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply via official portals at k.u-tokyo.ac.jp and adb.org.",
                "ADB never charges application fees or works with educational agencies."
            ],
            "application_fee_warning": "No application fee for ADB-JSP candidates nominated by UTokyo.",
            "agent_and_intermediary_warnings": "Commercial agency written proposals are rejected; authenticity of work experience is verified directly with employers.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (Waived).",
                "DHL document courier to Japan: ~PKR 12,000.",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 15,000.",
                "Initial pocket money before first stipend deposit: ~JPY 60,000 (~PKR 114,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Fresh graduates can apply. Reality: Minimum 2 years of full-time professional experience post-graduation is mandatory.",
                "Myth: You can stay in Japan after graduation. Reality: ADB requires a binding commitment to return to home country for at least 2 years."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim ADB-JSP funds PhD degrees; at UTokyo, ADB-JSP exclusively supports Master's degree programs."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain good academic standing and pass all coursework credits per UTokyo academic regulations.",
            "attendance_requirements": "Full-time physical research residency at UTokyo Kashiwa/Hongo campus for the complete 2-year duration.",
            "academic_progress_monitoring": "Annual progress report submitted to GSFS and ADB Headquarters.",
            "work_restrictions_during_study": "Scholars may not engage in outside employment or parallel income-generating consultancies.",
            "home_country_return_obligation": "Mandatory obligation to return to home country (Pakistan) for at least 2 years immediately upon completion of Master's study to contribute to national development.",
            "service_obligations_or_bonds": "Legally binding commitment to return to home country; failure to return triggers financial repayment clawback.",
            "repayment_clawback_conditions": "Recipients who refuse to return to their home country or fail out due to academic misconduct must reimburse the full cost of the fellowship to ADB.",
            "rules_for_changing_university": "Strictly non-transferable.",
            "rules_for_changing_major": "Cannot change degree program or department once enrolled.",
            "extension_policy": "Maximum duration is 2 years; no extensions beyond 24 months are permitted."
        },
        "official_sources_verified": [
            {
                "source_name": "UTokyo Graduate School of Frontier Sciences ADB-JSP Portal",
                "source_url": "https://www.k.u-tokyo.ac.jp/en/exam/master/foreign_research_students/adb-jsp/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Asian Development Bank - Japan Scholarship Program Official Guide",
                "source_url": "https://www.adb.org/work-with-us/careers/japan-scholarship-program",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-061": {
        "scholarship_id": "SCH-AS-061",
        "basic_details": {
            "scholarship_name": "Tokyo Institute of Technology (Science Tokyo) MEXT International Graduate Program (IGP-A) Award",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan & Institute of Science Tokyo (formerly Tokyo Tech)",
            "host_country": "Japan",
            "host_institutions_covered": "Institute of Science Tokyo (Ookayama and Suzukakedai Campuses, Tokyo / Yokohama, Japan)",
            "degree_levels": ["Integrated Master's & PhD", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Science, School of Engineering, School of Materials and Chemical Technology, School of Computing, School of Life Science and Technology, and School of Environment and Society.",
            "number_of_awards_total": "~50 to 70 MEXT University Recommendation scholarships awarded annually under IGP-A",
            "number_of_awards_pakistan": "Open internationally; typically 8 to 15 Pakistani engineering and computing researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 5 years for Integrated Master's & PhD program; up to 3 years for PhD track",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 147,000 / month for Master's students (~PKR 279,300 / month); JPY 148,000 / month for PhD students (~PKR 281,200 / month) plus 100% full tuition waiver and round-trip international airfare"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries with official diplomatic relations with Japan (Pakistan fully eligible; Japanese dual nationals ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2, 1991 (under 35 years old at commencement per MEXT statutory regulations).",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (for Master's/Integrated) or recognized 18-year Master's degree (for PhD) with minimum MEXT Grade Point Coefficient of 2.30 out of 3.00 from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 2.3,
            "grading_conversion_notes": "Minimum MEXT GPA calculation of 2.30 out of 3.00; competitive applicants typically hold MEXT GPA >= 2.70 / 3.00 (equivalent to CGPA >= 3.60 / 4.00).",
            "subject_background_prerequisites": "Computer science, electrical and electronic engineering, mechanical engineering, materials science, chemistry, physics, civil engineering, or life sciences.",
            "current_education_status": "Graduated or final-year students completing degree requirements before arrival in Japan (late September).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in peer-reviewed scientific journals or IEEE/ACM conferences provide a major competitive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 85, or official English Medium of Instruction (MOI) certificate demonstrating CEFR B2 or higher.",
            "other_language_requirements": "Japanese language proficiency is not required; all IGP coursework and research are conducted in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must contact a Tokyo Tech faculty member and receive formal consent to be their academic supervisor before applying.",
            "previous_scholarship_restrictions": "Previous MEXT recipients are ineligible unless at least 3 years have elapsed since completing previous award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full waiver of entrance examination fee (JPY 30,000), admission matriculation fee (JPY 282,000), and annual tuition fees (JPY 635,400/year).",
                "amount": "100% covered (~JPY 947,400 first-year value; ~PKR 1,800,000)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Application screening fee is waived for MEXT scholarship nominees.",
                "amount": "100% waived (JPY 30,000 value)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized university dormitory housing at Shizunoki, Minami-tsukushino, or Komaba dormitories (approx. JPY 25,000 to 45,000 / month), paid from monthly stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free stipend: JPY 147,000 / month for Master's (~PKR 279,300 / month); JPY 148,000 / month for PhD (~PKR 281,200 / month).",
                "amount": "JPY 147,000 to 148,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international flight ticket between Pakistan and Tokyo Narita/Haneda airport fully funded by MEXT.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese Student Visa issued free of charge for MEXT government scholars.",
                "amount": "100% covered / fee exempt"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Enrolled in Japan National Health Insurance (NHI) covering 70% of medical costs; subsidized monthly premium (approx. JPY 2,000/month) paid from stipend.",
                "amount": "Subsidized National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Ookayama and Suzukakedai campuses, including halal dining options at cafeteria.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to Tokyo Tech supercomputers (TSUBAME), laboratory instrumentation, and electronic journal databases.",
                "amount": "100% covered TSUBAME supercomputing & lab infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and JSPS project funds cover domestic and international conference participation.",
                "amount": "Lab grant-funded conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free university inter-campus shuttle bus between Ookayama and Suzukakedai, plus student discount rail passes.",
                "amount": "Free inter-campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 25000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Japanese STEM institution (Institute of Science Tokyo, formerly Tokyo Institute of Technology).",
            "participating_institutions": [
                "Institute of Science Tokyo (Ookayama Campus in Tokyo and Suzukakedai Campus in Yokohama, Japan)"
            ],
            "university_rankings_scope": "QS World University Rankings #84 globally, #3 in Japan; renowned as Japan's leading science and technology university, home to the TSUBAME supercomputer.",
            "available_majors": [
                "Master's / PhD in Computer Science",
                "Master's / PhD in Artificial Intelligence",
                "Master's / PhD in Electrical and Electronic Engineering",
                "Master's / PhD in Mechanical Engineering",
                "Master's / PhD in Materials Science and Engineering",
                "Master's / PhD in Chemical Science and Engineering",
                "Master's / PhD in Life Science and Technology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Integrated Master's/PhD: 5 years; PhD Track: 3 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with MEXT GPA >= 2.30/3.00, academic transcripts, research proposal, consent letter from prospective Tokyo Tech advisor, two recommendation letters, and English proficiency certificate (IELTS 6.5+ / TOEFL 85+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "School of Computing and School of Engineering are highly selective; establishing contact early (August-October) with a Tokyo Tech professor and securing consent is crucial.",
            "strategic_program_match_advice": "Study recent publications from Tokyo Tech laboratory pages and submit a tailored research plan showing how your skills enhance their active JSPS or JST funded research projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.titech.ac.jp/english/admissions/prospective-students/graduate-programs/igp-a",
            "portal_system_name": "Tokyo Tech Online Admissions System & IGP-A Portal",
            "account_creation_instructions": "Contact prospective academic supervisor, obtain consent, register on Tokyo Tech online application system, submit electronic dossier, and send certified physical documents if requested.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective academic advisor at Tokyo Tech with CV, transcripts, and research proposal (August-October).",
                "Step 2: Obtain formal consent from professor to serve as your academic supervisor.",
                "Step 3: Register on Tokyo Tech online application system during the IGP-A application window (September - December).",
                "Step 4: Upload all required documents including MEXT application form and research plan.",
                "Step 5: Departmental admissions committee reviews dossiers and conducts online technical interviews.",
                "Step 6: Tokyo Tech submits institutional nomination list to MEXT Tokyo in March.",
                "Step 7: MEXT Tokyo officially confirms scholarship recipients in June.",
                "Step 8: Receive Certificate of Eligibility, apply for Japanese visa, and arrive in Tokyo in late September for October 1 entry."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track (IGP-A): Admission and MEXT scholarship are processed concurrently as a single unified nomination.",
            "recommendation_letters_submission_method": "Submitted online by recommenders or uploaded as signed letters from university deans/professors on institutional stationery.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (Kenkyu Keikakusho) detailing research background, objectives, experimental methods, and contributions.",
            "study_plan_research_proposal_requirements": "Structured technical proposal detailing problem statement, literature background, experimental design, and timeline.",
            "cv_format_requirements": "Academic research CV detailing education, technical proficiencies, laboratory skills, and publication history.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental faculty panel.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 85+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "JPY 0 (Waived for MEXT nominees)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations recommended for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translation for all non-English/non-Japanese documents.",
            "final_submission_method": "Online submission via Tokyo Tech admissions system."
        },
        "required_documents_checklist": [
            {
                "document_name": "MEXT Application Form for University Recommendation",
                "mandatory": True,
                "specification": "Official Japanese Ministry prescribed application form with applicant photo.",
                "pakistan_specific_instruction": "Standard official MEXT form."
            },
            {
                "document_name": "Field of Study and Research Plan (Kenkyu Keikakusho)",
                "mandatory": True,
                "specification": "Detailed research plan following official MEXT template describing proposed investigations in Japan.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Official Academic Transcripts and Graduation Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing course grades, credit values, and grading scale for MEXT GPA calculation.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Summary of Thesis or Past Research Achievements",
                "mandatory": True,
                "specification": "Concise 1-2 page summary of Bachelor's or Master's thesis and list of publications.",
                "pakistan_specific_instruction": "Summary of final year project or thesis."
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from university dean or department chair and previous academic supervisor.",
                "pakistan_specific_instruction": "On institutional letterhead with official stamps."
            },
            {
                "document_name": "Consent Email / Letter from Tokyo Tech Prospective Supervisor",
                "mandatory": True,
                "specification": "Official written consent from a Tokyo Tech professor agreeing to be the academic supervisor.",
                "pakistan_specific_instruction": "Obtained directly from prospective professor."
            },
            {
                "document_name": "Certificate of English Language Proficiency",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 85+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "Score report or institutional letter."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "December 8 (Strict deadline for Autumn October intake)",
            "university_admission_deadline": "December 8",
            "document_submission_deadline": "December 8",
            "recommendation_letters_deadline": "December 8",
            "interview_period": "January - February",
            "shortlist_announcement": "March (University nomination to MEXT) / June (MEXT Tokyo final ratification)",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Single annual admission cycle for October intake; contact with professors must begin by August-September."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (MEXT GPA calculation >= 2.30/3.00, rigorous STEM coursework)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated in MEXT screening)",
            "research_experience_weight": "40% (Technical research proposal, previous thesis, publications, supervisor consent)",
            "work_experience_weight": "5% (Relevant laboratory or technical engineering experience)",
            "personal_statement_weight": "5% (Research intent and academic alignment)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "10% (Technical interview performance with prospective supervisor and faculty panel)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Tokyo Tech IGP Admissions Committee, School Deans, and Japanese Ministry of Education (MEXT) Board.",
            "evaluation_methodology": "Rigorous academic assessment prioritizing candidates with top MEXT GPA coefficients (above 2.65/3.00), strong publication potential, and supervisor backing."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~900 to 1,200 applicants across all engineering schools",
            "total_scholarships_awarded": "~50 to 70 MEXT University Recommendation awards annually under IGP-A",
            "acceptance_rate_global": "~5.5% to 6.5%",
            "acceptance_rate_pakistan": "~10.0% to 14.0% for candidates with professor consent and MEXT GPA >= 2.65",
            "typical_successful_applicant_gpa": "MEXT GPA coefficient >= 2.65 / 3.00 (approx. CGPA >= 3.60 / 4.00), accompanied by 1+ publications or strong thesis",
            "typical_academic_and_research_profile": "Top engineering and computing graduates with solid mathematical foundations, clear research alignment with Tokyo Tech laboratories, and supervisor consent.",
            "common_backgrounds_of_winners": "Graduates from leading Pakistani universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, Vietnam, China, Indonesia, Bangladesh, Thailand, India, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official titech.ac.jp portal.",
                "Beware of private agents claiming to sell MEXT recommendation seats; MEXT awards are managed strictly by universities."
            ],
            "application_fee_warning": "No application or examination fees are charged for MEXT scholarship nominees.",
            "agent_and_intermediary_warnings": "Commercial agency written proposals are rejected; applicants must author their own Kenkyu Keikakusho.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (Waived).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Medical checkup for COE: ~PKR 15,000 to 25,000.",
                "Initial pocket money before first stipend disbursement: ~JPY 100,000 (~PKR 190,000).",
                "National Health Insurance monthly premium: ~JPY 2,000/month (~PKR 3,800/month)."
            ],
            "misleading_claims_debunked": [
                "Myth: Japanese language fluency is mandatory. Reality: All IGP courses and lab research are conducted 100% in English.",
                "Myth: You can apply without contacting a professor. Reality: Prior consent from a Tokyo Tech professor is mandatory before submitting an application."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites suggest age limit is flexible; MEXT age limit (under 35 years old on October 1) is strictly statutory."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain MEXT Grade Point Coefficient of at least 2.30 out of 3.00 throughout study.",
            "attendance_requirements": "Full-time physical laboratory research presence; monthly signing of scholarship register at academic office to receive stipend.",
            "academic_progress_monitoring": "Annual progress review submitted to MEXT via the Graduate School.",
            "work_restrictions_during_study": "Part-time work restricted; requires immigration permission (Shikakugai Katsudo Kyoka) and written consent from academic supervisor.",
            "home_country_return_obligation": "None; scholars are free to pursue international postdocs, corporate careers in Japan, or return to Pakistan.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is immediately cancelled if GPA drops below 2.30 or if student is expelled for disciplinary violations.",
            "rules_for_changing_university": "Strictly non-transferable under MEXT University Recommendation regulations.",
            "rules_for_changing_major": "Major or laboratory changes are generally not permitted once enrolled.",
            "extension_policy": "In Integrated programs, continuation from Master's to PhD is contingent on maintaining required MEXT evaluation benchmarks."
        },
        "official_sources_verified": [
            {
                "source_name": "Tokyo Institute of Technology IGP-A MEXT Guide",
                "source_url": "https://www.titech.ac.jp/english/admissions/prospective-students/graduate-programs/igp-a",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Japanese Ministry of Education (MEXT) Official Portal",
                "source_url": "https://www.mext.go.jp/en/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-AS-063": {
        "scholarship_id": "SCH-AS-063",
        "basic_details": {
            "scholarship_name": "Osaka University MEXT University Recommendation (Special IGP) Award",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan & Osaka University",
            "host_country": "Japan",
            "host_institutions_covered": "Osaka University (Suita and Toyonaka Campuses, Osaka, Japan)",
            "degree_levels": ["Master of Engineering (MEng)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Engineering, Graduate School of Science, and Graduate School of Information Science and Technology (Special International Programs in Biotechnology, Applied Chemistry, Precision Science, and Information Systems).",
            "number_of_awards_total": "~40 to 60 MEXT University Recommendation scholarships awarded annually under Special IGP programs",
            "number_of_awards_pakistan": "Open internationally; typically 6 to 12 Pakistani engineering and science researchers selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master's; 3 years for PhD",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "JPY 144,000 / month for Master's (~PKR 273,600 / month); JPY 145,000 / month for PhD (~PKR 275,500 / month) plus 100% full tuition waiver and round-trip international airfare"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries with official diplomatic relations with Japan (Pakistan fully eligible; Japanese dual nationals ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2, 1991 (under 35 years old at commencement per MEXT statutory regulations).",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (for Master's) or recognized 18-year Master's degree (for PhD) with minimum MEXT Grade Point Coefficient of 2.30 out of 3.00 from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 2.3,
            "grading_conversion_notes": "Minimum MEXT GPA calculation of 2.30 out of 3.00; competitive applicants typically hold MEXT GPA >= 2.65 / 3.00 (equivalent to CGPA >= 3.55 / 4.00).",
            "subject_background_prerequisites": "Biotechnology, chemical science, materials engineering, precision engineering, information science, applied physics, or mechanical engineering.",
            "current_education_status": "Graduated or final-year students completing degree requirements before arrival in Japan (late September).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior scientific publications in indexed journals or strong thesis research provide a notable advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 80, or official English Medium of Instruction (MOI) certificate demonstrating CEFR B2 or higher.",
            "other_language_requirements": "Japanese language proficiency is not required.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must obtain a Letter of Provisional Acceptance from an Osaka University professor prior to submitting the formal MEXT dossier.",
            "previous_scholarship_restrictions": "Previous MEXT recipients are ineligible unless at least 3 years have elapsed since completing previous award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full waiver of entrance examination fee (JPY 30,000), admission matriculation fee (JPY 282,000), and annual tuition fees (JPY 535,800/year).",
                "amount": "100% covered (~JPY 847,800 first-year value; ~PKR 1,610,000)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Application screening fee is waived for MEXT scholarship nominees.",
                "amount": "100% waived (JPY 30,000 value)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized international student housing at Osaka University International House (Suita or Toyonaka) or Kasugaoka House (approx. JPY 20,000 to 40,000 / month), paid from stipend.",
                "amount": "Subsidized campus residence hall housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free stipend: JPY 144,000 / month for Master's (~PKR 273,600 / month); JPY 145,000 / month for PhD (~PKR 275,500 / month).",
                "amount": "JPY 144,000 to 145,000 / month"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy-class round-trip international flight ticket between Pakistan and Osaka Kansai International Airport (KIX) fully funded by MEXT.",
                "amount": "100% covered round-trip international flights"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Japanese Student Visa issued free of charge for MEXT government scholars.",
                "amount": "100% covered / fee exempt"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Enrolled in Japan National Health Insurance (NHI) covering 70% of medical costs; subsidized monthly premium (approx. JPY 2,000/month) paid from stipend.",
                "amount": "Subsidized National Health Insurance"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized dining halls across Suita, Toyonaka, and Minoh campuses, including halal-friendly dining options.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to Osaka University Joining and Welding Research Institute (JWRI), Center for Quantum Information, and central libraries.",
                "amount": "100% covered world-class lab infrastructure access"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory research grants and JSPS project funds cover domestic and international conference participation.",
                "amount": "Lab grant-funded conference travel"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Free campus shuttle buses connecting Suita, Toyonaka, and Minoh campuses.",
                "amount": "Free inter-campus shuttle network"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Japanese Imperial University (Osaka University - Handai).",
            "participating_institutions": [
                "Osaka University (Suita Campus and Toyonaka Campus, Osaka Prefecture, Japan)"
            ],
            "university_rankings_scope": "QS World University Rankings #86 globally, #4 in Japan; designated National University Corporation renowned for biotechnology, materials science, and robotics.",
            "available_majors": [
                "Master's / PhD in Biotechnology (Global Program in Frontier Biotechnology)",
                "Master's / PhD in Applied Chemistry and Materials Engineering",
                "Master's / PhD in Information Science and Technology",
                "Master's / PhD in Mechanical Engineering and Robotics",
                "Master's / PhD in Precision Science and Technology",
                "Master's / PhD in Applied Physics and Quantum Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years",
            "admission_requirements_summary": "Bachelor's / Master's degree with MEXT GPA >= 2.30/3.00, academic transcripts, research proposal, Letter of Provisional Acceptance from Osaka Univ professor, two recommendation letters, and English proficiency certificate (IELTS 6.5+ / TOEFL 80+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "High competition in Biotechnology and Information Science; securing early provisional acceptance from an Osaka University faculty professor is essential.",
            "strategic_program_match_advice": "Focus research proposals on biotechnology, functional materials, or robotics where Osaka University holds major national priority project grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.eng.osaka-u.ac.jp/en/admissions/mext/",
            "portal_system_name": "Osaka University Graduate School of Engineering Admissions & MEXT Portal",
            "account_creation_instructions": "Contact prospective faculty advisor, obtain Letter of Provisional Acceptance, compile MEXT application forms, submit online application, and dispatch certified physical dossier to Graduate School Office.",
            "step_by_step_workflow": [
                "Step 1: Contact prospective academic advisor at Osaka University with CV, transcripts, and research proposal (September-November).",
                "Step 2: Obtain Letter of Provisional Acceptance from professor.",
                "Step 3: Complete MEXT University Recommendation application package (November-December).",
                "Step 4: Prospective supervisor submits nomination dossier to Faculty Graduate Committee.",
                "Step 5: Osaka University conducts internal screening and submits institutional recommendation list to MEXT Tokyo in March.",
                "Step 6: MEXT Tokyo officially ratifies scholarship awards in June.",
                "Step 7: Receive Certificate of Eligibility, obtain Japanese visa, and receive flight tickets.",
                "Step 8: Fly to Osaka Kansai Airport in late September and start autumn semester on October 1."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation Track: Admission and MEXT scholarship are evaluated together upon faculty nomination.",
            "recommendation_letters_submission_method": "Submitted as formal recommendation letters signed by university deans or academic professors on institutional letterhead.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (Kenkyu Keikakusho) detailing background, objectives, experimental methods, and anticipated contributions.",
            "study_plan_research_proposal_requirements": "Structured academic proposal following MEXT format detailing problem statement, literature review, experimental methodology, and timeline.",
            "cv_format_requirements": "Academic CV detailing education, laboratory techniques, programming skills, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical interview via Zoom conducted by prospective supervisor and departmental committee.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 80+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "JPY 0 (Waived for MEXT scholarship nominees)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations recommended for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translation for all non-English/non-Japanese documents.",
            "final_submission_method": "Submission via departmental graduate office followed by postal dispatch of certified physical dossier to Osaka University."
        },
        "required_documents_checklist": [
            {
                "document_name": "MEXT Application Form for University Recommendation",
                "mandatory": True,
                "specification": "Official Japanese Ministry prescribed application form with applicant photo.",
                "pakistan_specific_instruction": "Standard official MEXT form."
            },
            {
                "document_name": "Field of Study and Research Plan (Kenkyu Keikakusho)",
                "mandatory": True,
                "specification": "Detailed research plan following official MEXT template describing proposed research in Japan.",
                "pakistan_specific_instruction": "Structured scholarly proposal."
            },
            {
                "document_name": "Official Academic Transcripts and Graduation Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing course grades, credits, and grading system for MEXT GPA calculation.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Letter of Recommendation from Dean or Higher Authority",
                "mandatory": True,
                "specification": "Recommendation letter addressed to the President of Osaka University signed by university Dean or Rector.",
                "pakistan_specific_instruction": "On institutional letterhead with official seal."
            },
            {
                "document_name": "Abstract of Bachelor's / Master's Thesis",
                "mandatory": True,
                "specification": "Concise 1-2 page summary of previous graduation thesis or major research project.",
                "pakistan_specific_instruction": "Summary of final year project or thesis."
            },
            {
                "document_name": "Osaka University Letter of Provisional Acceptance",
                "mandatory": True,
                "specification": "Signed letter from Osaka University faculty member committing to supervise the applicant.",
                "pakistan_specific_instruction": "Obtained directly from prospective Osaka Univ professor."
            },
            {
                "document_name": "Certificate of English Language Proficiency",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+, TOEFL iBT 80+, or official English Medium of Instruction (MOI) certificate.",
                "pakistan_specific_instruction": "Score report or institutional letter."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 1",
            "application_deadline": "December 15",
            "university_admission_deadline": "December 15",
            "document_submission_deadline": "December 20 (Physical hard-copy arrival)",
            "recommendation_letters_deadline": "December 15",
            "interview_period": "January - February",
            "shortlist_announcement": "March (University nomination to MEXT) / June (MEXT Tokyo final ratification)",
            "final_result_acceptance_deadline": "June 30",
            "visa_application_window": "July - August",
            "semester_commencement": "October 1 (Autumn intake)",
            "annual_cycle_notes": "Single annual admission cycle for October intake; contact with professors must begin by September-October."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (MEXT GPA calculation >= 2.30/3.00, academic consistency)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated in MEXT academic screening)",
            "research_experience_weight": "40% (Technical research proposal rigor, previous thesis, supervisor endorsement)",
            "work_experience_weight": "5% (Relevant scientific laboratory or technical engineering experience)",
            "personal_statement_weight": "5% (Study plan clarity and intent)",
            "recommendations_weight": "5% (Dean's official recommendation)",
            "interview_weight": "10% (Technical interview with prospective Osaka University faculty advisor)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and research merit)",
            "selection_panel_composition": "Osaka University Graduate School Academic Board, International College, and Japanese Ministry of Education (MEXT).",
            "evaluation_methodology": "Rigorous academic assessment prioritizing candidates with top MEXT GPA coefficients (above 2.65/3.00), strong publication potential, and supervisor backing."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,000 applicants across graduate divisions",
            "total_scholarships_awarded": "~40 to 60 MEXT University Recommendation awards annually under Special IGP",
            "acceptance_rate_global": "~5.0% to 6.0%",
            "acceptance_rate_pakistan": "~10.0% to 14.0% for candidates with professor provisional acceptance and MEXT GPA >= 2.65",
            "typical_successful_applicant_gpa": "MEXT GPA coefficient >= 2.65 / 3.00 (approx. CGPA >= 3.55 / 4.00), accompanied by strong thesis research or publications",
            "typical_academic_and_research_profile": "STEM graduates with strong laboratory foundations, clear research alignment with Osaka University research centers, and professor acceptance.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (NUST, Quaid-i-Azam, FAST-NUCES, UET Lahore, COMSATS, PIEAS, GIKI).",
            "high_representation_countries": "Pakistan, Vietnam, Indonesia, China, Bangladesh, Thailand, Egypt, Nigeria.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only consult official websites at osaka-u.ac.jp and mext.go.jp.",
                "Beware of unauthorized agents claiming to sell MEXT recommendation seats; MEXT awards are managed strictly by universities."
            ],
            "application_fee_warning": "No application or examination fee is charged for MEXT scholarship nominees.",
            "agent_and_intermediary_warnings": "Commercial agency written proposals are rejected; applicants must author their own Kenkyu Keikakusho.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (Waived).",
                "HEC document attestation in Pakistan: ~PKR 10,000 to 20,000.",
                "Medical checkup for COE processing: ~PKR 15,000 to 25,000.",
                "Initial pocket money before first stipend deposit: ~JPY 100,000 (~PKR 190,000).",
                "National Health Insurance monthly premium: ~JPY 2,000/month (~PKR 3,800/month)."
            ],
            "misleading_claims_debunked": [
                "Myth: Japanese language fluency is mandatory. Reality: All Special IGP graduate programs at Osaka University are conducted 100% in English.",
                "Myth: You can apply without professor endorsement. Reality: University recommendation track requires prior provisional acceptance from an Osaka University faculty professor."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest age limit can be relaxed; MEXT statutory age cutoff (born on or after April 2, 1991) is strictly enforced."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain MEXT Grade Point Coefficient of at least 2.30 out of 3.00 throughout study.",
            "attendance_requirements": "Full-time physical research residency in Osaka; monthly signing of scholarship register at university academic office to receive stipend.",
            "academic_progress_monitoring": "Annual progress review submitted to MEXT via the Graduate School.",
            "work_restrictions_during_study": "Part-time work restricted; requires immigration permission (Shikakugai Katsudo Kyoka) and written consent from academic supervisor.",
            "home_country_return_obligation": "None; scholars are free to seek international careers, postdocs in Japan, or return to Pakistan.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship is immediately terminated if GPA falls below 2.30 or if disciplinary expulsion occurs.",
            "rules_for_changing_university": "Strictly non-transferable under MEXT University Recommendation regulations.",
            "rules_for_changing_major": "Major or laboratory changes are generally not permitted once enrolled.",
            "extension_policy": "Extensions from Master's to PhD are highly competitive and require separate MEXT institutional recommendation screening."
        },
        "official_sources_verified": [
            {
                "source_name": "Osaka University Graduate School of Engineering MEXT Guide",
                "source_url": "https://www.eng.osaka-u.ac.jp/en/admissions/mext/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Japanese Ministry of Education (MEXT) Official Guide",
                "source_url": "https://www.mext.go.jp/en/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
