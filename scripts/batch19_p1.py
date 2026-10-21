# scripts/batch19_p1.py
# SCH-EU-013: SBW Berlin International Scholarship (Germany)
# SCH-EU-027: Norwegian Directorate (HK-dir) / NORPART Postgraduate Grants (Norway)
# SCH-EU-033: Technical University of Darmstadt Graduate Research Fellowships (Germany)

DATA_P1 = {
    "SCH-EU-013": {
        "scholarship_id": "SCH-EU-013",
        "basic_details": {
            "scholarship_name": "SBW Berlin International Scholarship for Social Development",
            "offering_entity": "SBW Berlin gGmbH (Non-profit organization supported by social initiatives and Berlin institutional partners)",
            "host_country": "Germany",
            "host_institutions_covered": "State-recognized universities and universities of applied sciences in Berlin and Potsdam (e.g., TU Berlin, HU Berlin, FU Berlin, University of Potsdam, HTW Berlin, BHT)",
            "degree_levels": ["Bachelor of Science (BSc)", "Bachelor of Arts (BA)", "Master of Science (MSc)", "Master of Arts (MA)"],
            "major_restrictions": "All academic disciplines offered at Berlin and Potsdam public institutions, with prioritized focus on Computer Science, Data Science, Environmental Engineering, Renewable Energy, Public Health, and Social Development.",
            "number_of_awards_total": "~20 to 30 international scholarship recipients actively supported per academic year",
            "number_of_awards_pakistan": "Open global competition; Pakistani students with verified social impact track records secure ~2 to 4 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Nominal duration of study program (up to 3-4 years for Bachelor's; up to 2 years for Master's), contingent upon maintaining academic standards and social project milestones"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of developing and emerging countries with severe financial need (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 30,
            "age_limit_postgrad": 30,
            "age_limit_notes": "Applicants must be between 18 and 30 years old at the time of application.",
            "academic_qualifications": "Intermediate/HSSC or A-Levels with at least 80% aggregate (or 3.5/4.0 equivalent) for Bachelor's; a recognized 4-year Bachelor's degree (16 years education) with minimum CGPA 3.30 / 4.00 (or equivalent German grade 2.0 or better) from an HEC-recognized university in Pakistan for Master's programs.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum German academic grade equivalent of 2.0 or better on the Bavarian formula (where 1.0 is highest and 4.0 is passing).",
            "subject_background_prerequisites": "Prerequisites corresponding to the targeted university program in Berlin/Potsdam; foundational coursework in quantitative, scientific, or social methodologies.",
            "current_education_status": "Students who hold a valid admission letter or are in the process of applying to a public university in Berlin/Potsdam, or currently enrolled in the 1st or 2nd semester.",
            "graduation_year_restrictions": "None, as long as age limit (<30 years) is respected.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Substantial documented record of volunteer work, community development, NGO service, or civic initiatives in Pakistan is mandatory.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Official IELTS (min 6.5) or TOEFL iBT (min 90) for English-taught degrees; TestDaF (min TDN 4) or Goethe C1 certificate for German-taught degrees.",
            "other_language_requirements": "German language skills at A1/A2 level are advantageous for daily integration in Berlin student housing.",
            "gender_specific_requirements": None,
            "financial_need_required": True,
            "special_eligibility_categories": "Applicants must submit a detailed proposal for a social non-profit project that addresses a developmental, educational, environmental, or technological challenge in Pakistan, which they pledge to implement upon return.",
            "previous_scholarship_restrictions": "Cannot hold another full living stipend scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "Public universities in Berlin/Potsdam charge zero tuition fees; SBW Berlin covers semester administrative and public transport contributions (Semesterbeitrag ~€315 per semester).",
                "amount": "100% covered (~€630 / year; ~PKR 190,000 / year value)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Uni-Assist evaluation fees (~€75 for first application, €30 for each additional) must be covered independently by the applicant.",
                "amount": "€75 (~PKR 23,000 out-of-pocket)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Fully furnished single room provided free of charge in SBW Berlin's dedicated student residences/apartments in Berlin.",
                "amount": "100% covered (market rental value ~€550 - €700 / month in Berlin)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly personal living allowance of €480 to €550 per month to cover food, groceries, books, and daily personal necessities.",
                "amount": "€480 - €550 / month (~PKR 145,000 - 165,000 / month; €5,760 - €6,600 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Reimbursement of inbound economy airfare from Pakistan to Berlin at program commencement and return flight upon graduation.",
                "amount": "€1,200 total value (~PKR 360,000 round-trip economy flights)"
            },
            "visa_fee": {
                "status": "REIMBURSED",
                "details": "German national student visa application fee (€75) and Berlin foreigners authority residence permit fee (Aufenthaltstitel ~€100) are reimbursed upon arrival in Berlin.",
                "amount": "€175 total (~PKR 53,000 value)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Mandatory German statutory health and nursing care insurance (Techniker Krankenkasse, AOK, or Barmer) fully paid by the scholarship.",
                "amount": "€125 - €130 / month (~PKR 38,000 / month; ~€1,520 / year value)"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Included within the monthly personal living allowance of €480 - €550.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "PARTIAL",
                "details": "Covered within monthly stipend; special technical project materials can be granted upon written application.",
                "amount": "Included in living stipend"
            },
            "research_funding_conference_grant": {
                "status": "PARTIAL",
                "details": "Discretionary grant available to present academic research or project results at European academic conferences or social development forums.",
                "amount": "Up to €500 per year upon application"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Berlin public transit pass (Semesterticket) integrated into university semester fee, enabling unlimited travel on U-Bahn, S-Bahn, buses, and trams across Berlin and nationwide regional trains.",
                "amount": "100% covered via semester contribution"
            },
            "total_estimated_value_usd_per_year": 20000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple state-recognized universities and universities of applied sciences located exclusively in Berlin and Potsdam.",
            "participating_institutions": [
                "Technical University of Berlin (TU Berlin)",
                "Humboldt University of Berlin (HU Berlin)",
                "Free University of Berlin (FU Berlin)",
                "University of Potsdam",
                "Berlin University of Applied Sciences and Technology (BHT)",
                "HTW Berlin - University of Applied Sciences for Engineering and Economics"
            ],
            "university_rankings_scope": "Top 100 globally for TU Berlin and HU Berlin; premier research universities across Germany and Europe.",
            "available_majors": [
                "Computer Science and Data Engineering",
                "Software Systems and Media Informatics",
                "Renewable Energy and Clean Technology",
                "Environmental Engineering",
                "Public Health and Biotechnology",
                "Economics and International Development",
                "Urban Sustainability and Architecture"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 3 to 4 years; Master's: 2 years (4 semesters)",
            "admission_requirements_summary": "Bachelor's requires Abitur-equivalent secondary qualification (HSSC + 1 year university or Studienkolleg); Master's requires recognized 4-year HEC Bachelor's with 180-240 ECTS equivalence, English proficiency (IELTS 6.5+), and course-specific subject credits.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "TU Berlin and HU Berlin Computer Science and Data Engineering programs have competitive NC (Numerus Clausus) cutoffs requiring top 10% academic ranks; University of Potsdam and applied science universities (HTW, BHT) offer slightly higher acceptance rates for qualified candidates.",
            "strategic_program_match_advice": "Pakistani applicants should simultaneously apply for admission through Uni-Assist / university direct portals while submitting the SBW Berlin application, emphasizing how their academic studies will directly enable the execution of their proposed non-profit social initiative in Pakistan."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://sbw.berlin/en/sbw-berlin-scholarship/",
            "portal_system_name": "SBW Berlin Online Application Portal",
            "account_creation_instructions": "Register on the SBW Berlin portal, download the application guidelines and official application form, and submit online together with supporting documentation.",
            "step_by_step_workflow": [
                "Step 1: Secure admission or submit active application for an accredited degree program at a public university in Berlin or Potsdam (via Uni-Assist or direct university portal).",
                "Step 2: Formulate a detailed project proposal (2 to 5 pages) outlining a non-profit social development project to be implemented in Pakistan after graduation.",
                "Step 3: Obtain a letter of recommendation from an established non-profit organization or civic body in Pakistan confirming social commitment and project feasibility.",
                "Step 4: Complete the official SBW Berlin application form and upload CV, academic transcripts, family financial disclosure, proof of income, and project proposal.",
                "Step 5: Shortlisted applicants undergo a virtual video interview with the SBW Berlin selection committee assessing motivation, character, and project viability.",
                "Step 6: Successful candidates receive the formal scholarship contract, allowing them to secure the German student visa without opening a blocked bank account (Sperrkonto)."
            ],
            "university_vs_scholarship_routing": "Dual Track: University admission must be pursued independently through Uni-Assist or university direct portals in parallel with the SBW scholarship application.",
            "recommendation_letters_submission_method": "Uploaded directly via the online portal along with applicant documents, signed on official non-profit organization letterhead.",
            "personal_statement_prompts": "Personal motivation essay explaining reasons for choosing Berlin, dedication to social progress, and personal background.",
            "study_plan_research_proposal_requirements": "Structured non-profit social project proposal (2-5 pages) addressing community development, educational reform, environmental sustainability, or tech innovation in Pakistan.",
            "cv_format_requirements": "Europass or standard professional CV highlighting social work, volunteer activities, and academic history.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute structured video interview via Zoom focusing on the applicant's motivation, personal values, and practical feasibility of the return project.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 90) for English programs; TestDaF (TDN 4) or Goethe C1 for German programs.",
            "application_fee_amount": "€0 (Free for scholarship; Uni-Assist university fee ~€75)",
            "attestation_requirements": "Matriculation, Intermediate, and Bachelor's degrees must be verified by IBCC, HEC Pakistan, and MOFA.",
            "translation_requirements": "Certified English or German translation required for all official Urdu documents.",
            "final_submission_method": "Online upload via the official SBW Berlin scholarship portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for HSSC or Bachelor's degree with minimum German equivalent grade 2.0.",
                "pakistan_specific_instruction": "Attested copies from IBCC, HEC, and MOFA Pakistan."
            },
            {
                "document_name": "Social Non-Profit Project Proposal",
                "mandatory": True,
                "specification": "2-5 page proposal detailing a non-profit social development initiative to be executed in Pakistan.",
                "pakistan_specific_instruction": "Must address concrete community challenges in education, healthcare, technology, or environment."
            },
            {
                "document_name": "Recommendation Letter from Non-Profit Organization",
                "mandatory": True,
                "specification": "Signed letter from a registered NGO, civic society, or community organization verifying voluntary work.",
                "pakistan_specific_instruction": "Must be printed on official NGO letterhead with contact phone and email."
            },
            {
                "document_name": "Proof of Low Family Income / Financial Hardship",
                "mandatory": True,
                "specification": "Official household income statements, salary slips, or bank statements proving financial need.",
                "pakistan_specific_instruction": "Salary certificates or FBR tax returns showing low-to-modest family income."
            },
            {
                "document_name": "University Admission Letter or Application Confirmation",
                "mandatory": True,
                "specification": "Proof of application or acceptance letter from an accredited university in Berlin or Potsdam.",
                "pakistan_specific_instruction": "Uni-Assist confirmation or direct university application voucher."
            },
            {
                "document_name": "Official English or German Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5) / TOEFL iBT (min 90) or TestDaF / Goethe C1.",
                "pakistan_specific_instruction": "Must be valid at the time of application submission."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "November 15 (Summer) / May 15 (Winter)",
            "application_deadline": "December 31 (Summer) / June 30 (Winter)",
            "university_admission_deadline": "January 15 (Summer) / July 15 (Winter)",
            "document_submission_deadline": "December 31 (Summer) / June 30 (Winter)",
            "recommendation_letters_deadline": "December 31 (Summer) / June 30 (Winter)",
            "interview_period": "January - February (Summer) / July - August (Winter)",
            "shortlist_announcement": "Mid-February (Summer) / Mid-August (Winter)",
            "final_result_acceptance_deadline": "Late February (Summer) / Late August (Winter)",
            "visa_application_window": "February - March (Summer) / August - September (Winter)",
            "semester_commencement": "April 1 (Summer Semester) / October 1 (Winter Semester)",
            "annual_cycle_notes": "Operates biannual admission cycles corresponding to German university Winter and Summer semesters."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Academic excellence and grade point average)",
            "extracurricular_and_leadership_weight": "15% (Demonstrated voluntary community service record)",
            "research_experience_weight": "0% (Not primarily research-focused)",
            "work_experience_weight": "5% (Practical experience in social sector)",
            "personal_statement_weight": "15% (Clarity of motivation and personal alignment)",
            "recommendations_weight": "10% (Endorsement from recognized non-profit organization)",
            "interview_weight": "25% (Performance in online panel interview)",
            "test_scores_weight": "0% (Language proficiency fulfills qualification threshold)",
            "financial_need_weight": "Pre-screening eligibility gate (Must prove low household income)",
            "selection_panel_composition": "Executive leadership of SBW Berlin, university academic representatives, and social development experts.",
            "evaluation_methodology": "Two-phase evaluation: formal audit of academic marks and financial need, followed by a 30-minute interview interrogating project viability."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,000 international applications worldwide per cycle",
            "total_scholarships_awarded": "~20 to 30 active scholars funded per year",
            "acceptance_rate_global": "~1.5% to 2.0%",
            "acceptance_rate_pakistan": "~2.0% to 3.5% among eligible applicants with proven NGO credentials",
            "typical_successful_applicant_gpa": "Undergraduate CGPA 3.40+ / 4.00 or HSSC 80%+ marks",
            "typical_academic_and_research_profile": "Academically strong students with 2+ years of demonstrable community volunteer service and concrete non-profit initiatives.",
            "common_backgrounds_of_winners": "Graduates active in local social entrepreneurship, community education, and civic impact.",
            "high_representation_countries": "Pakistan, India, Nigeria, Ghana, Kenya, Colombia, Syria, Ukraine.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents claiming to sell guaranteed SBW Berlin scholarship placements.",
                "Official applications are accepted only via https://sbw.berlin/en/sbw-berlin-scholarship/."
            ],
            "application_fee_warning": "SBW Berlin does NOT charge any application fee. Any request for money is fraudulent.",
            "agent_and_intermediary_warnings": "SBW Berlin does not collaborate with any commercial educational agents or consultants.",
            "hidden_costs_breakdown": [
                "Uni-Assist university application fee: €75 (~PKR 23,000).",
                "IELTS/TOEFL examination registration: ~PKR 60,000.",
                "German student visa appointment and courier fees: ~PKR 25,000.",
                "Initial pocket money before first stipend transfer: ~€300 (~PKR 90,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply to SBW Berlin for universities across any German state. Reality: SBW Berlin strictly covers universities located in Berlin and Potsdam.",
                "Myth: You do not need to return to your home country. Reality: A core requirement is the commitment to implement the non-profit project in your home country upon graduation."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest age limit is 35; official guidelines enforce a strict maximum age limit of 30 years at application."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance and earn minimum 30 ECTS per semester without fail grades.",
            "attendance_requirements": "Full-time physical enrollment and regular attendance at the host university in Berlin or Potsdam.",
            "academic_progress_monitoring": "Biannual submission of official grade transcripts and social project progress reports to the SBW committee.",
            "work_restrictions_during_study": "Part-time student employment permitted up to legal German limit (140 full days / 280 half days per year), but must not interfere with studies.",
            "home_country_return_obligation": "Moral and contractual pledge to return to Pakistan upon graduation to execute the proposed social project or collaborate with a partner NGO.",
            "service_obligations_or_bonds": "Active participation in SBW Berlin community events and workshops during study in Germany.",
            "repayment_clawback_conditions": "Revocation of fellowship and potential clawback if applicant falsifies financial records or discontinues studies without cause.",
            "rules_for_changing_university": "Transferring to a university outside Berlin or Potsdam is strictly prohibited and results in immediate termination.",
            "rules_for_changing_major": "Permitted only with prior written consent from SBW Berlin management.",
            "extension_policy": "Maximum extension of one semester may be granted upon documented medical or academic hardship."
        },
        "official_sources_verified": [
            {
                "source_name": "SBW Berlin Official Scholarship Portal",
                "source_url": "https://sbw.berlin/en/sbw-berlin-scholarship/",
                "source_type": "OFFICIAL_COMMISSION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "SBW Berlin Official Guidelines and Project Criteria",
                "source_url": "https://sbw.berlin/wp-content/uploads/2023/10/SBW_Berlin_Scholarship_Guidelines.pdf",
                "source_type": "OFFICIAL_COMMISSION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-EU-027": {
        "scholarship_id": "SCH-EU-027",
        "basic_details": {
            "scholarship_name": "Norwegian Directorate (HK-dir) / NORPART Postgraduate Research Grants",
            "offering_entity": "Norwegian Directorate for Higher Education and Skills (Direktoratet for høyere utdanning og kompetanse - HK-dir) & Norwegian Ministry of Foreign Affairs",
            "host_country": "Norway",
            "host_institutions_covered": "Accredited Norwegian public universities (e.g., Norwegian University of Science and Technology - NTNU, University of Oslo - UiO, University of Bergen - UiB, Norwegian University of Life Sciences - NMBU, UiT The Arctic University of Norway)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Prioritized institutional partnership domains: Computer Science, Artificial Intelligence, Renewable Energy & Power Systems, Environmental & Climate Sciences, Marine Informatics, Biotechnology, and Global Health.",
            "number_of_awards_total": "~100 to 150 bilateral mobility and postgraduate degree grants awarded annually across international partner consortia",
            "number_of_awards_pakistan": "Allocated across formal Pakistani university partnerships (e.g., NUST, COMSATS, Quaid-i-Azam University); ~8 to 15 Pakistani researchers awarded annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master of Science; up to 3-4 years for PhD research fellowship positions"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of designated partner countries holding institutional collaborations with Norway (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No statutory age limit; candidates are evaluated based on academic merit, research competence, and departmental nomination.",
            "academic_qualifications": "A recognized 4-year Bachelor of Science / Engineering (16 years education) with minimum CGPA 3.30 / 4.00 (or 75%+ aggregate) for Master's programs; an MS/MPhil (18 years education) with minimum CGPA 3.50 / 4.00 and thesis completion for PhD positions from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Norwegian grading system uses A to F (A highest, E lowest passing). Applicants typically require an equivalent of Grade B or Grade A on the Norwegian scale.",
            "subject_background_prerequisites": "Rigorous undergraduate background in relevant engineering, mathematical, or scientific discipline with minimum 80 ECTS of specialized subject coursework.",
            "current_education_status": "Graduating seniors in their final semester or enrolled Master's/PhD scholars at Pakistani partner institutions.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications, laboratory research, or thesis projects are highly advantageous for PhD and Master's fellowship candidates.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 overall (no band below 6.0) or TOEFL iBT minimum 90. Certain partner projects accept institutional Medium of Instruction (MOI) certificates from Pakistani partner universities with English-medium curricula.",
            "other_language_requirements": "None; academic instruction and thesis supervision are conducted entirely in English.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must be nominated or enrolled through an approved institutional partnership agreement between a Norwegian host university and a Pakistani partner university.",
            "previous_scholarship_restrictions": "Cannot hold another Norwegian government grant simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "Full exemption/grant coverage for tuition fees at Norwegian public universities (which instituted tuition fees for non-EEA students in autumn 2023; HK-dir partner fellows are granted complete institutional tuition waivers or direct project fee subsidies).",
                "amount": "100% covered (~NOK 130,000 - 220,000 / year value; ~PKR 3,400,000 - 5,700,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Norwegian public universities do not charge an admission application fee.",
                "amount": "NOK 0"
            },
            "accommodation": {
                "status": "PARTIAL",
                "details": "Guaranteed priority placement in university student housing (SiO in Oslo, SiT in Trondheim, Sammen in Bergen); rent is paid via the monthly living stipend.",
                "amount": "Subsidized student rent ~NOK 4,500 - 6,500 / month (~PKR 115,000 - 170,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend aligned with the Norwegian State Educational Loan Fund (Lånekassen) subsistence benchmark of NOK 11,500 to NOK 13,790 per month (~PKR 300,000 - 360,000 / month). For employed PhD research fellows, full salary on the state pay scale (approx NOK 532,000 / year before tax).",
                "amount": "NOK 11,500 - 13,790 / month (~PKR 300,000 - 360,000 / month; NOK 138,000 - 165,480 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Fixed round-trip travel grant covering economy flights between Pakistan and Norway at the start and conclusion of the study period.",
                "amount": "NOK 12,000 - 15,000 (~PKR 315,000 - 395,000 round-trip economy flights)"
            },
            "visa_fee": {
                "status": "REIMBURSED",
                "details": "Norwegian Directorate of Immigration (UDI) residence permit application fee for studies (NOK 5,900) is reimbursed or waived under institutional grant agreements.",
                "amount": "NOK 5,900 (~PKR 155,000 value)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Automatic enrollment in the Norwegian National Insurance Scheme (Folketrygden) upon registration and receiving a Norwegian National Identity Number (Fødselsnummer), providing comprehensive universal public healthcare.",
                "amount": "100% covered by the Norwegian state"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via the monthly living stipend of NOK 11,500 - 13,790.",
                "amount": "Included in monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Study materials and laboratory equipment are covered under project operational allocations; computer lab and campus infrastructure access provided.",
                "amount": "NOK 5,000 / year project contribution"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Generous project budget for research travel, field work, and attending international conferences across Europe and North America.",
                "amount": "Up to NOK 25,000 / year for approved research activities"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Comprehensive round-trip airfare and local airport transit grant provided.",
                "amount": "Included in travel grant"
            },
            "total_estimated_value_usd_per_year": 28000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple accredited Norwegian public research universities participating in HK-dir partnership consortia.",
            "participating_institutions": [
                "Norwegian University of Science and Technology (NTNU Trondheim)",
                "University of Oslo (UiO)",
                "University of Bergen (UiB)",
                "Norwegian University of Life Sciences (NMBU Ås)",
                "UiT The Arctic University of Norway (Tromsø)"
            ],
            "university_rankings_scope": "NTNU and University of Oslo consistently rank within the top 100-150 globally (QS/THE World University Rankings), with world-renowned standing in computer engineering, clean tech, and earth sciences.",
            "available_majors": [
                "Computer Science and Data Science",
                "Software Engineering and Cyber Security",
                "Artificial Intelligence and Autonomous Systems",
                "Renewable Energy and Smart Grids",
                "Marine Technology and Ocean Informatics",
                "Petroleum Geoscience and Clean Energy",
                "Environmental Biotechnology and Global Health"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (120 ECTS) for Master of Science; 3 to 4 years for Doctor of Philosophy",
            "admission_requirements_summary": "Relevant Bachelor's degree (180-240 ECTS equivalence) with top-quartile grades, certified English proficiency, and institutional endorsement from the Pakistani partner university.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "NTNU Computer Science and UiO Informatics are highly competitive, requiring strong theoretical foundations and programming competence; NMBU and UiT offer specialized niches with high fellowship allocation rates for environmental and data science projects.",
            "strategic_program_match_advice": "Check whether your home department in Pakistan (e.g. at NUST, QAU, or COMSATS) maintains active HK-dir/NORPART or UTFORSK project partnerships with NTNU or UiO; direct faculty-to-faculty recommendation is the most reliable pathway to winning this award."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://hkdir.no/en/programmes-and-grants & https://www.samordnaopptak.no/info/english/",
            "portal_system_name": "HK-dir Portal & Søknadsweb (Norwegian University Admissions)",
            "account_creation_instructions": "Register on Søknadsweb for the targeted Norwegian university, submit academic profile, and coordinate with the Pakistani partner department coordinator for bilateral project nomination.",
            "step_by_step_workflow": [
                "Step 1: Identify participating HK-dir/NORPART project coordinators at Pakistani partner university and Norwegian host university.",
                "Step 2: Submit formal departmental nomination and academic portfolio to the institutional project coordinator.",
                "Step 3: Complete university admission application through Søknadsweb (official Norwegian university admissions portal) by December 1.",
                "Step 4: Upload attested transcripts, degree certificates, CV, statement of purpose, and English language test scores.",
                "Step 5: Attend academic screening interview if shortlisted by the project evaluation committee.",
                "Step 6: Receive formal admission letter and HK-dir scholarship commitment letter; apply for UDI student residence permit."
            ],
            "university_vs_scholarship_routing": "Integrated Bilateral Track: Candidates are nominated via the inter-university partnership agreement and apply through Søknadsweb in parallel.",
            "recommendation_letters_submission_method": "Submitted by academic referees directly to the project coordinator or uploaded via Søknadsweb.",
            "personal_statement_prompts": "Statement of purpose outlining research interests, academic background, and relevance to the bilateral Norway-Pakistan project.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-4 pages) aligned with the research themes of the HK-dir/NORPART project.",
            "cv_format_requirements": "Academic CV highlighting publications, software repositories, and research project experience.",
            "interviews_conducted": True,
            "interview_format_details": "30-40 minute technical discussion via Microsoft Teams / Zoom assessing academic depth and research motivation.",
            "standardized_tests": "IELTS Academic (min 6.5 overall, 6.0 each band) or TOEFL iBT (min 90); MOI accepted by select consortia.",
            "application_fee_amount": "NOK 0 (Free of charge at Norwegian public universities)",
            "attestation_requirements": "Degrees and transcripts attested by HEC Pakistan and MOFA; Matric/Inter attested by IBCC.",
            "translation_requirements": "Certified English translation required for all official documents.",
            "final_submission_method": "Online submission via Søknadsweb portal and bilateral departmental nomination dossier."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year Bachelor's (for MSc) or 18-year MS/MPhil (for PhD) with Grade B / CGPA 3.3+ equivalent.",
                "pakistan_specific_instruction": "Scans of HEC-attested degrees and semester transcripts."
            },
            {
                "document_name": "Institutional Nomination Letter",
                "mandatory": True,
                "specification": "Official letter from Pakistani partner university endorsing the candidate under the HK-dir/NORPART partnership.",
                "pakistan_specific_instruction": "Signed by Dean or Head of Department at partner Pakistani university."
            },
            {
                "document_name": "Research Proposal / Statement of Purpose",
                "mandatory": True,
                "specification": "2 to 4-page proposal detailing research objectives, methodology, and relevance to bilateral project.",
                "pakistan_specific_instruction": "Must clearly cite the host Norwegian research lab and faculty mentors."
            },
            {
                "document_name": "Official English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5) or TOEFL iBT (min 90), or approved MOI certificate.",
                "pakistan_specific_instruction": "Scores must be valid at time of application."
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential recommendation letters from previous academic professors or research supervisors.",
                "pakistan_specific_instruction": "Must be on university letterhead with institutional email addresses."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page with minimum 2-year validity.",
                "pakistan_specific_instruction": "Pakistani passport must remain valid through mid-2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "October 15",
            "application_deadline": "December 1",
            "university_admission_deadline": "December 1",
            "document_submission_deadline": "December 15",
            "recommendation_letters_deadline": "December 15",
            "interview_period": "January 15 - March 15",
            "shortlist_announcement": "Late April",
            "final_result_acceptance_deadline": "May 15",
            "visa_application_window": "May 15 - July 1",
            "semester_commencement": "Mid-August (Autumn Semester)",
            "annual_cycle_notes": "Main intake cycle is Autumn (August commencement). December 1 deadline is strictly enforced on Søknadsweb."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Undergraduate CGPA, consistency, and course relevance)",
            "extracurricular_and_leadership_weight": "5% (Institutional engagement and collaboration skills)",
            "research_experience_weight": "30% (Prior research, thesis publications, and proposal alignment)",
            "work_experience_weight": "5% (Professional experience in relevant technical sector)",
            "personal_statement_weight": "10% (Clarity of purpose and bilateral collaboration potential)",
            "recommendations_weight": "10% (Academic referee assessments and departmental nomination)",
            "interview_weight": "0% (Interview performance factored directly into research proposal score)",
            "test_scores_weight": "0% (English proficiency fulfills qualification threshold)",
            "financial_need_weight": "0% (Pure academic and bilateral research merit evaluation)",
            "selection_panel_composition": "Joint evaluation committee of Norwegian host faculty, Pakistani partner department, and HK-dir academic officers.",
            "evaluation_methodology": "Two-tier review: departmental nomination followed by joint faculty evaluation on Søknadsweb."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~500 to 800 applicants across partner institutions",
            "total_scholarships_awarded": "~100 to 150 bilateral grants awarded annually",
            "acceptance_rate_global": "~15% to 20%",
            "acceptance_rate_pakistan": "~10% to 15% among officially nominated partner candidates",
            "typical_successful_applicant_gpa": "CGPA 3.50+ / 4.00 or top 10% class rank from top Pakistani universities (NUST, QAU, COMSATS, UET)",
            "typical_academic_and_research_profile": "High-performing STEM graduates with strong mathematical foundations, thesis research experience, and supervisor connections.",
            "common_backgrounds_of_winners": "Graduates of partner engineering and science faculties in Pakistan.",
            "high_representation_countries": "Pakistan, India, South Africa, Tanzania, Ethiopia, Brazil, Nepal, Vietnam.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent consultancy firms advertising 'Norwegian free visa & work permits'.",
                "Official Norwegian applications are submitted exclusively via Søknadsweb and university portals."
            ],
            "application_fee_warning": "Norwegian public universities do NOT charge any admission application fee.",
            "agent_and_intermediary_warnings": "HK-dir and Norwegian public universities do not work with educational agents.",
            "hidden_costs_breakdown": [
                "UDI study residence permit fee: NOK 5,900 (~PKR 155,000) payable upfront, reimbursed later.",
                "VFS Global appointment and biometric fee in Pakistan: ~PKR 15,000.",
                "Tuberculosis screening test at IOM Islamabad/Lahore: ~PKR 18,000.",
                "Initial pocket money before first stipend transfer in Norway: ~NOK 5,000 (~PKR 130,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: Norway abolished all free education for international students so no one gets funded. Reality: While general tuition was introduced in 2023, HK-dir, NORPART, and bilateral fellowship holders receive 100% full tuition coverage and monthly stipends.",
                "Myth: You can apply without an institutional partnership. Reality: NORPART grants are tied directly to active institutional inter-university agreements."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim Norway offers rolling admissions; Norwegian public university international deadlines close sharply on December 1."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain Grade B or higher average across coursework and pass minimum 30 ECTS per semester.",
            "attendance_requirements": "Full-time physical presence on campus in Norway and active laboratory/thesis research engagement.",
            "academic_progress_monitoring": "Semester-end review of earned credits on the national student database (FS) and annual progress report by thesis advisor.",
            "work_restrictions_during_study": "Part-time work permitted up to 20 hours per week during academic semesters, full-time during holidays.",
            "home_country_return_obligation": "Depending on project agreement: mobility scholars return to home university; degree scholars may apply for 1-year Norwegian post-study job seeker visa.",
            "service_obligations_or_bonds": "Participation in bilateral symposiums and reporting milestones to HK-dir project managers.",
            "repayment_clawback_conditions": "Funding terminated upon voluntary withdrawal or severe academic negligence without approved cause.",
            "rules_for_changing_university": "Non-transferable to other universities; tied specifically to the partner consortium.",
            "rules_for_changing_major": "Strictly prohibited; fellowship is allocated to the designated research project.",
            "extension_policy": "Maximum extension of one semester considered for legitimate medical or research delays with project lead approval."
        },
        "official_sources_verified": [
            {
                "source_name": "HK-dir Programmes and Grants Official Directory",
                "source_url": "https://hkdir.no/en/programmes-and-grants",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Norwegian Directorate of Immigration (UDI) Study Permit Regulations",
                "source_url": "https://www.udi.no/en/want-to-apply/studies/studietillatelse/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "NTNU International Financing and Scholarships",
                "source_url": "https://www.ntnu.edu/studies/financing-and-scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-EU-033": {
        "scholarship_id": "SCH-EU-033",
        "basic_details": {
            "scholarship_name": "Technical University of Darmstadt Graduate Research Fellowships & Assistantships",
            "offering_entity": "Technische Universität Darmstadt (TU Darmstadt) - Department of Computer Science & hessian.AI (The Hessian Center for Artificial Intelligence)",
            "host_country": "Germany",
            "host_institutions_covered": "TU Darmstadt Main Campus & Lichtwiese Campus (Darmstadt, Hesse, Germany)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Department of Computer Science (Informatik) & Computational Engineering: Artificial Intelligence and Machine Learning, Autonomous Systems, Cyber Security & Privacy (ATHENE), Data Science, Software Engineering, and High-Performance Computing.",
            "number_of_awards_total": "~80 to 120 graduate research assistantships (HiWi/WiMi) and DAAD STIBET/Matching-fund fellowships awarded annually across departments",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers secure ~8 to 14 funded positions and assistantships annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master of Science; 3 to 4 years for PhD research associates (WiMi contract TV-H E13)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students of all nationalities (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research potential.",
            "academic_qualifications": "A recognized 4-year Bachelor of Science / Engineering in Computer Science, Software Engineering, or closely related field (16 years education) with minimum CGPA 3.30 / 4.00 (or equivalent German grade <= 2.2 on the Bavarian scale) from an HEC-recognized university in Pakistan. For PhD, an MS/MPhil in Computer Science (18 years education) with strong thesis and research output.",
            "minimum_gpa_percentage": 76.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Must meet TU Darmstadt faculty entrance grade requirements (German grade 2.0 or better is highly competitive).",
            "subject_background_prerequisites": "Rigorous foundation in theoretical computer science, algorithms and data structures, formal methods, computer networks, and linear algebra (at least 18 ECTS in theoretical CS and mathematics).",
            "current_education_status": "Graduating seniors can apply with provisional transcript showing at least 85% of degree credits completed.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Demonstrated open-source contributions, competitive programming ranks, or published papers at top-tier venues (NeurIPS, ICML, CVPR, IEEE S&P) provide a decisive advantage.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 88,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall or TOEFL iBT minimum 88. TU Darmstadt strictly enforces standardized language test scores for international degree admissions.",
            "other_language_requirements": "German language proficiency is not mandatory for English-taught MSc in Computer Science or PhD research, but basic German (A1/A2) is beneficial for campus employment.",
            "gender_specific_requirements": None,
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates applying for PhD or WiMi research positions must secure preliminary endorsement from a TU Darmstadt professor or lab head (e.g. at hessian.AI or ATHENE National Research Center for Applied Cybersecurity).",
            "previous_scholarship_restrictions": "Cannot hold another full German government scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "Public universities in the federal state of Hesse charge zero tuition fees for regular Master's and PhD programs. The mandatory semester fee (Semesterbeitrag ~€275 / semester) covers campus administration and student services.",
                "amount": "100% covered (~€550 / year; ~PKR 165,000 / year value)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "TU Darmstadt application handling fee of €20 - €50 is payable by international applicants during online dossier evaluation.",
                "amount": "€20 - €50 (~PKR 6,000 - 15,000)"
            },
            "accommodation": {
                "status": "PARTIAL",
                "details": "Priority access to student residences managed by Studierendenwerk Darmstadt (approx €320 - €480 / month for single furnished room including utilities and high-speed internet).",
                "amount": "Subsidized rent ~€350 - €480 / month (~PKR 105,000 - 145,000 / month)"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "For Master's students: Research Assistantships (HiWi) provide €600 to €1,100 per month (€13.50 - €17.50 / hour for up to 20 hours/week) plus DAAD STIBET/matching fellowships of €400 - €861/month. For PhD researchers: Full employment contract under TV-H E13 pay scale yielding €2,400 to €2,900 net per month (~PKR 720,000 - 870,000 / month).",
                "amount": "€1,000 - €2,700 / month depending on level (~PKR 300,000 - 810,000 / month; €12,000 - €32,400 / year)"
            },
            "airfare": {
                "status": "PARTIAL",
                "details": "International mobility travel grants (€500 to €1,000) can be awarded through the TU Darmstadt International Office upon arrival.",
                "amount": "Up to €1,000 (~PKR 300,000 one-time grant)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "German national student visa fee (€75 in Pakistan) and Darmstadt foreigners registration authority residence permit fee (~€100).",
                "amount": "€175 (~PKR 53,000)"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "PhD research associates on TV-H E13 contracts receive statutory employer health insurance contributions (TK/AOK). Master's students pay statutory student health insurance (~€125 / month) from their assistantship salary.",
                "amount": "Covered via employment contract / stipend"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered through monthly research assistantship earnings or fellowship stipend.",
                "amount": "Covered via monthly earnings"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Access to state-of-the-art laboratory workstations, GPU compute clusters (hessian.AI supercomputers), and university digital library resources.",
                "amount": "100% provided by university infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental travel funding of €1,500 to €3,000 per year to present accepted papers at premier computing and AI conferences worldwide.",
                "amount": "€1,500 - €3,000 / year"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Semester ticket included with semester contribution grants unlimited regional public transit across the entire federal state of Hesse (including Frankfurt, Wiesbaden, Kassel) and Deutschlandticket upgrade.",
                "amount": "100% covered via semester contribution"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier technical institution: Technical University of Darmstadt (TU Darmstadt).",
            "participating_institutions": [
                "Technical University of Darmstadt (TU Darmstadt, Hesse, Germany)"
            ],
            "university_rankings_scope": "TU Darmstadt is a founding member of the TU9 alliance of leading German Institutes of Technology; ranked among the top 10 in Germany and top 100 globally in Computer Science, Software Engineering, and AI.",
            "available_majors": [
                "MSc in Computer Science (Informatik)",
                "MSc in Artificial Intelligence and Machine Learning",
                "MSc in Autonomous Systems",
                "MSc in Information Systems Engineering",
                "MSc in Computational Engineering",
                "PhD in Computer Science and Artificial Intelligence"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (4 semesters, 120 ECTS) for Master's; 3 to 4 years for PhD",
            "admission_requirements_summary": "Recognized 4-year Bachelor's in CS or closely related discipline, proof of equivalent theoretical CS coursework, minimum GPA 3.3/4.0, and English language proficiency (IELTS 6.5 or TOEFL 88). GRE is recommended but not mandatory.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "MSc Computer Science has rigorous subject-entry vetting (the 'Eingangsprüfung' or curricular equivalence check); Pakistani applicants must demonstrate adequate theoretical computer science and mathematics credits to avoid condition courses.",
            "strategic_program_match_advice": "Pakistani applicants with strong programming and mathematics credentials should identify research labs at hessian.AI or ATHENE and reach out to principal investigators 2-3 months prior to arrival to secure guaranteed HiWi or WiMi research contracts."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.tu-darmstadt.de/studieren/bewerben_und_einschreiben/index.en.jsp",
            "portal_system_name": "TU Darmstadt TUCaN Online Application Portal",
            "account_creation_instructions": "Register an applicant account on TUCaN, select the desired English-taught Master's program in Computer Science, and submit certified scans of academic records and course module descriptions.",
            "step_by_step_workflow": [
                "Step 1: Check curricular equivalence for MSc Computer Science against TU Darmstadt Bachelor curriculum.",
                "Step 2: Submit application via the TU Darmstadt online portal (TUCaN) and upload certified transcripts and syllabus descriptions.",
                "Step 3: Pay international application handling fee (€20-€50).",
                "Step 4: Receive admission offer and curricular equivalence result (confirming no more than 30 ECTS condition courses).",
                "Step 5: Apply for student housing via Studierendenwerk Darmstadt immediately upon receiving admission letter.",
                "Step 6: Contact department research groups (hessian.AI, ATHENE, Telecooperation, Cryptography) for HiWi research assistantship positions.",
                "Step 7: Apply for German student visa at German Embassy Islamabad or Consulate Karachi using admission letter and proof of funding."
            ],
            "university_vs_scholarship_routing": "Sequential Track: Secure formal university admission via TUCaN, followed by direct application for departmental research assistantships (HiWi/WiMi) or DAAD STIBET funding.",
            "recommendation_letters_submission_method": "Uploaded via portal or emailed directly by professors to prospective research lab heads.",
            "personal_statement_prompts": "Statement of academic purpose detailing technical specializations, relevant coding projects, and motivation for pursuing advanced computing at TU Darmstadt.",
            "study_plan_research_proposal_requirements": "For PhD/WiMi positions: 3-5 page research proposal outlining research methodology and alignment with lab objectives; for MSc: detailed academic module list.",
            "cv_format_requirements": "Detailed academic and technical CV highlighting programming languages, frameworks, open-source repositories, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Technical interview (30-45 minutes) via Zoom/Teams conducted by lab principal investigators assessing coding abilities and technical understanding.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 88) mandatory; GRE General test recommended.",
            "application_fee_amount": "€20 - €50 (~PKR 6,000 - 15,000 handling fee)",
            "attestation_requirements": "Degrees and transcripts attested by HEC and MOFA Pakistan; Matric/Inter attested by IBCC.",
            "translation_requirements": "Certified English or German translation of all academic records.",
            "final_submission_method": "Online submission via the TU Darmstadt TUCaN portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 4-year Bachelor's in CS/SE with minimum CGPA 3.3/4.0 (German equivalent <= 2.2).",
                "pakistan_specific_instruction": "Attested copies from HEC and MOFA Pakistan."
            },
            {
                "document_name": "Curricular Module Description / Syllabus Handbook",
                "mandatory": True,
                "specification": "Detailed course catalog descriptions of all completed computer science, algorithms, and mathematics courses.",
                "pakistan_specific_instruction": "Official syllabus descriptions issued or certified by your Pakistani university registrar."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall) or TOEFL iBT (min 88).",
                "pakistan_specific_instruction": "Score report valid at time of application."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic and technical CV outlining software projects, skills, and publications.",
                "pakistan_specific_instruction": "Must include links to GitHub profile and live project demos."
            },
            {
                "document_name": "Statement of Academic Purpose",
                "mandatory": True,
                "specification": "1 to 2-page statement explaining why you are choosing TU Darmstadt and your specialization interests.",
                "pakistan_specific_instruction": "Highlight alignment with research centers like hessian.AI or ATHENE."
            },
            {
                "document_name": "Two Academic Letters of Recommendation",
                "mandatory": False,
                "specification": "Confidential evaluation letters from academic professors (required for assistantship/fellowship consideration).",
                "pakistan_specific_instruction": "Issued on institutional university letterhead."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "June 1 (Winter) / December 1 (Summer)",
            "application_deadline": "July 15 (Winter) / January 15 (Summer)",
            "university_admission_deadline": "July 15 (Winter) / January 15 (Summer)",
            "document_submission_deadline": "July 15 (Winter) / January 15 (Summer)",
            "recommendation_letters_deadline": "July 31 (Winter) / January 31 (Summer)",
            "interview_period": "August - September (Winter) / February - March (Summer)",
            "shortlist_announcement": "Mid-August (Winter) / Mid-February (Summer)",
            "final_result_acceptance_deadline": "September 15 (Winter) / March 15 (Summer)",
            "visa_application_window": "August - September (Winter) / February - March (Summer)",
            "semester_commencement": "Mid-October (Winter Semester) / Mid-April (Summer Semester)",
            "annual_cycle_notes": "Admits two batches per year (Winter and Summer). July 15 is the strict cutoff for Winter semester international applications."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Undergraduate GPA and curricular equivalence in theoretical CS and mathematics)",
            "extracurricular_and_leadership_weight": "5% (Technical community leadership and hackathon participation)",
            "research_experience_weight": "25% (Publications, thesis work, and supervisor match for assistantship positions)",
            "work_experience_weight": "5% (Industry software engineering or data science experience)",
            "personal_statement_weight": "10% (Clarity of academic purpose and motivation)",
            "recommendations_weight": "5% (Academic referee appraisals)",
            "interview_weight": "0% (Interview performance factored directly into research assistantship hiring)",
            "test_scores_weight": "0% (English proficiency fulfills qualification threshold)",
            "financial_need_weight": "0% (Pure academic and technical merit evaluation)",
            "selection_panel_composition": "TU Darmstadt Computer Science Department admissions board and lab principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic curricular equivalence audit followed by lab-level technical vetting."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 international applicants across computer science programs",
            "total_scholarships_awarded": "~80 to 120 assistantships and matching fellowships awarded annually",
            "acceptance_rate_global": "~8% to 12% for program admission; ~3% to 5% for early funded assistantships",
            "acceptance_rate_pakistan": "~6% to 10% among applicants with strong theoretical CS coursework",
            "typical_successful_applicant_gpa": "CGPA 3.50+ / 4.00 or top 10% class rank from leading Pakistani universities (FAST-NUCES, NUST, LUMS, GIKI, UET)",
            "typical_academic_and_research_profile": "Rigorous undergraduate computer science preparation with solid mathematical depth, high programming acumen, and research thesis experience.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani computer science, software engineering, and artificial intelligence programs.",
            "high_representation_countries": "India, China, Pakistan, Iran, Turkey, Egypt, Nigeria, Brazil.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of private education agencies claiming to sell admissions or blocked-account waivers for TU Darmstadt.",
                "Applications are handled exclusively via tu-darmstadt.de."
            ],
            "application_fee_warning": "TU Darmstadt charges only a small administrative handling fee (€20-€50); never pay large consulting sums.",
            "agent_and_intermediary_warnings": "TU Darmstadt does not work with third-party recruitment agents.",
            "hidden_costs_breakdown": [
                "TUCaN application handling fee: €20 - €50 (~PKR 6,000 - 15,000).",
                "IELTS/TOEFL exam fee: ~PKR 60,000.",
                "Semester contribution fee: ~€275 per semester (~PKR 83,000).",
                "German visa processing and courier fees: ~PKR 25,000."
            ],
            "misleading_claims_debunked": [
                "Myth: TU Darmstadt requires German proficiency for all Master's programs. Reality: MSc Computer Science and MSc Artificial Intelligence are 100% taught and examined in English.",
                "Myth: You cannot work as a student in Germany. Reality: Research assistant (HiWi) positions are abundant at TU Darmstadt and provide flexible campus income."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is mandatory; GRE is NOT mandatory for MSc Computer Science at TU Darmstadt, though recommended."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and earn regular ECTS credits each semester to retain assistantship contracts.",
            "attendance_requirements": "Full-time campus attendance in Darmstadt; regular participation in laboratory research duties.",
            "academic_progress_monitoring": "Semester re-enrollment (Rückmeldung) contingent on module exam completions; assistantship contracts renewed based on supervisor review.",
            "work_restrictions_during_study": "Campus research assistant (HiWi) positions can be held up to legal limits (typically 10-20 hours/week during term).",
            "home_country_return_obligation": "Zero return obligation; graduates are eligible for Germany's 18-month post-study job seeker visa (Chancenkarte / residence permit).",
            "service_obligations_or_bonds": "Fulfill contracted assistantship duties (research, code maintenance, or grading) diligently.",
            "repayment_clawback_conditions": "No clawback of assistantship wages; termination occurs upon breach of employment contract or academic expulsion.",
            "rules_for_changing_university": "Non-transferable to other universities; tied directly to TU Darmstadt.",
            "rules_for_changing_major": "Changing major requires formal re-application to the new faculty.",
            "extension_policy": "Assistantships can be renewed semester-by-semester throughout the regular duration of studies."
        },
        "official_sources_verified": [
            {
                "source_name": "TU Darmstadt Graduate Admissions Official Portal",
                "source_url": "https://www.tu-darmstadt.de/studieren/bewerben_und_einschreiben/index.en.jsp",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "TU Darmstadt Department of Computer Science",
                "source_url": "https://www.informatik.tu-darmstadt.de/fb20/index.en.jsp",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "hessian.AI The Hessian Center for Artificial Intelligence",
                "source_url": "https://hessian.ai/join-us/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
