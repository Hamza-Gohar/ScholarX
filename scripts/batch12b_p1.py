# scripts/batch12b_p1.py
# 27. UTS International Research Scholarship (SCH-OC-010)
# 28. UNSW Scientia PhD Scholarship (SCH-OC-011)

DATA_P1 = {
    "SCH-OC-010": {
        "scholarship_id": "SCH-OC-010",
        "basic_details": {
            "scholarship_name": "UTS International Research Scholarship (IRS) & Australian Government RTP",
            "offering_entity": "University of Technology Sydney (UTS) & Australian Commonwealth Government (Department of Education - Research Training Program)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Technology Sydney (City Campus - Broadway / Ultimo, Sydney, NSW, Australia)",
            "degree_levels": ["Doctor of Philosophy (PhD)", "Master of Science by Research (MSc Research)"],
            "major_restrictions": "Open to all research disciplines across Faculty of Engineering and Information Technology (FEIT: Computer Science, Artificial Intelligence, Quantum Software, Cybersecurity, Data Science, Biomedical Engineering, Robotics) and Faculty of Science.",
            "number_of_awards_total": "Approximately 100 to 150 competitive international doctoral scholarships (IRS & UTS President's Scholarship) awarded annually",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computer science, software engineering, and telecommunications compete actively (typically 6 to 12 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD candidates; up to 2 years for Master by Research candidates, with potential 6-month extension for PhD under extraordinary research circumstances"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants who do not hold Australian or New Zealand citizenship or Australian permanent residency"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restrictions.",
            "academic_qualifications": "Completed 4-year Bachelor's with First Class Honours (H1 equivalent, 82%+ or 3.70+ / 4.00 CGPA) or completed Master of Science by Research / MS with substantial research thesis (minimum 25% research component) from an HEC-recognized university in Pakistan (e.g. NUST, FAST-NUCES, GIKI, UET, LUMS, COMSATS, PIEAS).",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Must equate to Australian First Class Honours (Honours 1 / H1) standard with strong thesis grade.",
            "subject_background_prerequisites": "BSc / MS in Computer Science, Software Engineering, Electrical Engineering, Mathematics, Data Science, or related computational disciplines.",
            "current_education_status": "Completed degree or in final semester of research Master's.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Industry research, patent applications, or software architecture experience can be submitted as evidence of research potential.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall 6.5 with min 6.0 in writing; TOEFL iBT min 79 with min 21 in writing; or PTE Academic min 58 with min 50 in writing. Medium of Instruction certificates are not accepted."
            },
            "other_language_requirements": "None; all coursework, seminars, and doctoral dissertations are in English.",
            "gender_specific_requirements": "None; female researchers in engineering and computer science are actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Higher Degree by Research (HDR) candidates demonstrating superior research capacity.",
            "previous_scholarship_restrictions": "Cannot hold another major Commonwealth-funded scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee offset (AUD 42,000 to 48,000 / year waived completely for up to 3.5 years).",
                "amount": "100% covered (~AUD 45,000 / year value; ~PKR 8,325,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "UTS application fee (AUD 100) is waived for candidates applying for research degrees with pre-approved supervisory support.",
                "amount": "AUD 100 waived value (~PKR 18,500)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from living stipend; student can rent private Sydney accommodation or UTS on-campus student housing (Yura Mudang, Gumal Ngurang) at ~AUD 320 to 450/week.",
                "amount": "Paid from living stipend (~AUD 1,400 to 1,800 / month)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Fortnightly tax-free living allowance: AUD 37,000 per annum index-linked (~AUD 3,083 / month; ~PKR 570,000/month). Top-up scholarships from faculties (AUD 5,000 to 10,000/yr) frequently awarded to top CS/AI applicants.",
                "amount": "AUD 37,000 / year tax-free (~PKR 6,845,000 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Relocation allowance of up to AUD 1,520 provided to assist international scholars traveling from overseas to Sydney.",
                "amount": "Up to AUD 1,520 relocation subsidy (~PKR 280,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Subclass 500 Student Visa application fee (AUD 1,600 as of 2024 revised fee schedule) paid directly to Australian Department of Home Affairs.",
                "amount": "AUD 1,600 (~PKR 296,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Full standard Overseas Student Health Cover (OSHC) single policy paid directly by UTS for the entire duration of the student visa.",
                "amount": "AUD 2,400 to 3,200 total value (~PKR 445,000 to 590,000)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered through the generous fortnightly stipend.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Computing equipment, high-performance GPU cluster access (UTS AI Institute), and lab workstations funded by Faculty of Engineering and IT.",
                "amount": "Provided by faculty and research center"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "FEIT Vice-Chancellor conference travel grant and departmental funding provide up to AUD 3,000 to 5,000 per year for presenting at top international conferences (CORE A*/A).",
                "amount": "Up to AUD 5,000 per year"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Sydney Opal card public transport is self-funded (international HDR students receive concession Opal cards in NSW).",
                "amount": "Self-funded (~AUD 120 / month; ~PKR 22,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 55000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading Australian technology university: University of Technology Sydney (Sydney, NSW, Australia)",
            "participating_institutions": [
                "University of Technology Sydney - Broadway / Ultimo City Campus (Sydney, NSW)",
                "Australian Artificial Intelligence Institute (AAII - UTS)",
                "Centre for Quantum Software and Information (QSI - UTS)"
            ],
            "university_rankings_scope": "Ranked #88 globally in QS World University Rankings 2024/2025; ranked #1 young university in Australia. AI research at UTS AAII ranked among top 10 globally.",
            "available_majors": [
                "School of Computer Science: Artificial Intelligence, Machine Learning, Computer Vision, Data Science",
                "Centre for Quantum Software and Information: Quantum Algorithms, Quantum Information Theory",
                "School of Electrical and Data Engineering: Cybersecurity, Telecommunications, IoT, Signal Processing",
                "School of Biomedical Engineering: Neural Interfaces, Health Informatics, Computational Biology",
                "School of Civil and Environmental Engineering & Mechanical and Mechatronic Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "PhD: 3.5 years full-time; Master by Research: 2 years full-time.",
            "admission_requirements_summary": "BSc H1 / Master by Research with 3.7+ GPA, confirmed prospective supervisor, detailed research proposal (3-5 pages), 2 academic referee reports, and IELTS 6.5.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "AAII (Artificial Intelligence Institute) and Quantum Software are exceptionally competitive; Data Engineering and Mechatronics offer slightly broader supervisory availability.",
            "strategic_program_match_advice": "Prospective candidates MUST contact potential supervisors at UTS FEIT or AAII well in advance (May-June for the August scholarship round). Securing a supervisor who commits to supporting your scholarship ranking is a strict prerequisite before lodging your formal application."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.uts.edu.au/study/international/essential-information/applying-study-uts",
            "portal_system_name": "UTS International Graduate Research Application Portal",
            "account_creation_instructions": "Find a supervisor via UTS Find a Supervisor portal, obtain their written endorsement, then create an account on the UTS HDR online application system and submit for both admission and scholarship.",
            "step_by_step_workflow": [
                "Step 1 (April - June): Search UTS Find a Supervisor portal; contact prospective faculty members with CV, academic transcripts, and draft research proposal.",
                "Step 2 (June - July): Interview with prospective supervisor; obtain their formal agreement to supervise and written Pre-Assessment / Supervisor Support Letter.",
                "Step 3 (July - August): Prepare full application dossier: refined 3-5 page research proposal, 2 academic referee reports, IELTS test report, and attested transcripts.",
                "Step 4 (By 31 August): Submit formal online application via UTS portal, ticking the box for 'UTS International Research Scholarship / RTP'.",
                "Step 5 (September - October): Faculty Higher Degree Committee reviews and scores applications on H1 equivalence and research output.",
                "Step 6 (November - December): UTS Graduate Research School releases scholarship outcomes and issues unconditional offers and Confirmation of Enrolment (CoE).",
                "Step 7 (December - January): Apply for Australian Subclass 500 Student Visa via ImmiAccount; complete biometrics and medical exam in Pakistan.",
                "Step 8 (February - March): Travel to Sydney, attend UTS HDR orientation, and commence research candidature."
            ],
            "university_vs_scholarship_routing": "Single unified application: The admissions application automatically assesses the candidate for all centrally funded UTS scholarships (IRS, RTP, UTP).",
            "recommendation_letters_submission_method": "Two academic referee reports completed on the official UTS HDR Referee Report Template and submitted directly by referees.",
            "personal_statement_prompts": "Statement of Research Intent: Detail academic preparation, research motivations, alignment with UTS faculty strategic research areas, and career goals.",
            "study_plan_research_proposal_requirements": "Comprehensive 3 to 5 page research proposal covering title, background, research questions, methodology, literature review, and required laboratory resources.",
            "cv_format_requirements": "Academic CV detailing peer-reviewed publications (with DOIs, citation counts, and CORE ranking), research awards, and coding/engineering projects.",
            "interviews_conducted": True,
            "interview_format_details": "Informal to formal technical video interviews conducted by prospective supervisor and co-supervisor via Zoom evaluating research capability and cultural fit.",
            "standardized_tests": "IELTS 6.5 (6.0 writing) or TOEFL iBT 79 (21 writing) or PTE 58. GRE is NOT required.",
            "application_fee_amount": "AUD 100 (Waived for HDR candidates with supervisor support)",
            "attestation_requirements": "HEC Pakistan attestation required for all degrees and transcripts, accompanied by certified color copies.",
            "translation_requirements": "Official certified English translations required for any non-English documentation.",
            "final_submission_method": "100% digital submission via the UTS Graduate Research Online Portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least two years.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Certified transcripts showing all semesters, grades, grading scale, and degree completion certificates.",
                "pakistan_specific_instruction": "Higher Education Commission (HEC) Pakistan attested documents."
            },
            {
                "document_name": "UTS Supervisor Pre-Assessment / Agreement Letter",
                "mandatory": True,
                "specification": "Written email or formal confirmation from a UTS faculty member agreeing to supervise.",
                "pakistan_specific_instruction": "Crucial prerequisite before formal portal lodgement."
            },
            {
                "document_name": "Detailed Research Proposal (3-5 pages)",
                "mandatory": True,
                "specification": "Structured proposal developed in consultation with prospective UTS supervisor.",
                "pakistan_specific_instruction": "Cite prospective supervisor's recent CORE A*/A publications."
            },
            {
                "document_name": "Academic Referee Reports (Two)",
                "mandatory": True,
                "specification": "Completed on official UTS HDR Referee Report forms by former academic advisors.",
                "pakistan_specific_instruction": "Must be submitted directly by referees from official university email accounts."
            },
            {
                "document_name": "English Language Proficiency Test Scorecard",
                "mandatory": True,
                "specification": "Official IELTS Academic, TOEFL iBT, or PTE Academic scorecard dated within 2 years.",
                "pakistan_specific_instruction": "Direct electronic score dispatch through testing agency portal."
            },
            {
                "document_name": "Evidence of Research Output / Publications",
                "mandatory": False,
                "specification": "PDF copies of published conference papers or journal articles with publication metrics.",
                "pakistan_specific_instruction": "Scopus, IEEE Xplore, or WoS indexed papers heavily weighted in H1 equivalence scoring."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 June 2027",
            "application_deadline": "31 August 2027 (for Spring / Autumn 2028 intake)",
            "university_admission_deadline": "31 August 2027",
            "document_submission_deadline": "31 August 2027",
            "recommendation_letters_deadline": "7 September 2027",
            "interview_period": "July to August 2027 (Pre-application interviews)",
            "shortlist_announcement": "Mid-November 2027",
            "final_result_acceptance_deadline": "15 December 2027",
            "visa_application_window": "December 2027 to February 2028",
            "semester_commencement": "Late February / Early March 2028 (or Mid-July for Spring)",
            "annual_cycle_notes": "Main international scholarship round closes 31 August for commencement in the following year."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Honours 1 equivalence, CGPA in Bachelor/Master coursework, and university pedigree)",
            "extracurricular_and_leadership_weight": "0% (Not considered for HDR scholarships)",
            "research_experience_weight": "40% (Peer-reviewed publications, master thesis quality, patents, and research proposal caliber)",
            "work_experience_weight": "5% (Professional R&D or technical engineering experience)",
            "personal_statement_weight": "5% (Statement of research alignment)",
            "recommendations_weight": "10% (Rigor and conviction of academic referee appraisals)",
            "interview_weight": "0% (Official scoring is dossier-based; supervisor interview establishes candidacy)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 79 compliance)",
            "financial_need_weight": "0% (Purely merit and research performance based)",
            "selection_panel_composition": "UTS Faculty Research Committee, Associate Dean Research, and UTS Graduate Research School Board.",
            "evaluation_methodology": "Rigorous competitive ranking: Applications are scored on a standardized matrix measuring Academic Merit (0-50 pts) and Research Experience / Track Record (0-50 pts). Applicants with 1+ first-author IEEE/ACM publications and H1 equivalence rank in the top quartile and are awarded IRS and stipend packages."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,200 international applicants across all research areas for ~120 scholarships",
            "total_scholarships_awarded": "~100 to 150 fully funded international research scholarships (IRS + RTP)",
            "acceptance_rate_global": "~6.5%",
            "acceptance_rate_pakistan": "~7.2% (Pakistani CS and EE graduates with solid publication records compete effectively)",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (85%+ aggregate, top 5% class rank)",
            "typical_academic_and_research_profile": "First Class Honours or MS with 1-2 CORE A/B conference or Q1/Q2 journal publications, strong coding/math foundations, and strong supervisor backing.",
            "common_backgrounds_of_winners": "BS/MS graduates in Computer Science, Software Engineering, and Telecommunications from NUST, FAST-NUCES, GIKI, UET, LUMS, and COMSATS.",
            "high_representation_countries": "China, India, Pakistan, Iran, Vietnam, Bangladesh, Indonesia",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized migration agents claiming guaranteed UTS scholarship placement. UTS scholarships are awarded solely by the University Graduate Research Board through merit ranking."
            ],
            "application_fee_warning": "HDR applications are free when endorsed by a supervisor. Never pay placement fees to private intermediaries.",
            "agent_and_intermediary_warnings": "UTS requires direct intellectual engagement between applicant and prospective supervisor; agent-prepared proposals are detected and rejected.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD 1,600; ~PKR 296,000).",
                "Biometrics and visa medical examination in Pakistan (~PKR 35,000 - 50,000).",
                "Initial housing deposit and temporary accommodation in Sydney before first stipend disbursement (~AUD 2,000; ~PKR 370,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: English Medium of Instruction (MOI) certificates are accepted. (FACT: Official IELTS, TOEFL, or PTE test report is strictly mandatory for Australian HDR admission).",
                "CLAIM: High GPA alone guarantees a scholarship. (FACT: Publications and research track record carry equal weight to GPA in the scoring matrix)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party portals list the stipend as AUD 30,000; the official 2024/2025 UTS rate has increased to AUD 37,000 per annum tax-free."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress and pass annual milestones: Confirmation of Candidature (Month 12) and Progress Reviews (Months 24 and 36).",
            "attendance_requirements": "Full-time on-campus research residency in Sydney, with regular physical attendance in laboratories and research seminars.",
            "academic_progress_monitoring": "Annual Review of Progress (ARP) submitted to the Graduate Research School and approved by supervisory panel.",
            "work_restrictions_during_study": "Full-time HDR candidates are permitted to work up to a maximum of 8-10 hours per week during normal business hours (e.g. as sessional teaching assistants or lab demonstrators), provided it does not impede doctoral progress.",
            "home_country_return_obligation": "None. Graduates are eligible to apply for the Australian Temporary Graduate Visa (Subclass 485 - Post-Study Work stream, granting 3-4 years work rights in Australia).",
            "service_obligations_or_bonds": "Zero service bonds or repayment conditions.",
            "repayment_clawback_conditions": "Scholarship terminates upon academic dismissal, failure of candidature confirmation, or unauthorized withdrawal; past funds are not clawed back.",
            "rules_for_changing_university": "Scholarship is non-transferable to other Australian universities.",
            "rules_for_changing_major": "Topic or lab adjustments must remain within the scope of faculty research and receive formal Graduate Research Board approval.",
            "extension_policy": "PhD candidates may apply for a single 6-month extension beyond 3.5 years under exceptional circumstances beyond the candidate's control."
        },
        "official_sources_verified": [
            {
                "source_name": "UTS Future Research Students Scholarships Official Portal",
                "source_url": "https://www.uts.edu.au/research-and-teaching/research-degrees/future-research-students/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific faculty-level quota allocations between engineering and other divisions.",
                    "Exact numerical cutoff scores on the 100-point HDR merit scoring matrix for the current round.",
                    "Nationality-specific applicant and awardee statistics."
                ]
            },
            {
                "source_name": "Australian Government Department of Education Research Training Program (RTP)",
                "source_url": "https://www.education.gov.au/research-block-grants/research-training-program",
                "source_type": "GOVERNMENT_MINISTRY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Annual Commonwealth block grant distribution formulas across non-Group of Eight institutions.",
                    "International candidate reserve reallocation rates."
                ]
            }
        ]
    },
    "SCH-OC-011": {
        "scholarship_id": "SCH-OC-011",
        "basic_details": {
            "scholarship_name": "UNSW Sydney Scientia PhD Scholarship & Australian Government RTP",
            "offering_entity": "University of New South Wales (UNSW Sydney, Group of Eight, Australia) in partnership with the Australian Commonwealth Government",
            "host_country": "Australia",
            "host_institutions_covered": "UNSW Sydney (Kensington Main Campus, Sydney, NSW, Australia)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Offered across pre-determined, high-impact strategic doctoral research projects spanning UNSW School of Computer Science and Engineering (CSE), Quantum Computing (CQC2T), Photovoltaic and Renewable Energy Engineering (SPREE), AI & Robotics, Biomedical Engineering, Materials Science, and Medicine.",
            "number_of_awards_total": "Approximately 100 to 125 prestigious Scientia PhD Fellowships awarded annually across all faculties",
            "number_of_awards_pakistan": "Global open competition; exceptional Pakistani researchers with peer-reviewed publications secure awards (typically 2 to 5 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 years full-time doctoral tenure (non-extendable), subject to satisfactory annual research progress reviews"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to both international applicants and Australian/NZ citizens/permanent residents"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit.",
            "academic_qualifications": "Completed 4-year Bachelor's degree with First Class Honours (H1 equivalent, 85%+ or 3.80+ / 4.00 CGPA) or Master of Science by Research / MS with substantial research dissertation from an HEC-recognized institution in Pakistan (e.g. NUST, FAST-NUCES, GIKI, UET, LUMS, PIEAS). Must demonstrate superior research capacity through publications.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Evaluated against UNSW Class 1 Honours standard (H1 / 85%+ equivalent).",
            "subject_background_prerequisites": "BSc / MS in Computer Science, Quantum Information, Electrical Engineering, Photovoltaics, Materials Science, or Biomedical Engineering.",
            "current_education_status": "Must have completed degree or be in final semester graduating prior to commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Demonstrated research track record (first-author papers in indexed venues) significantly outranks general industrial experience.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall min 6.5 (all sub-scores 6.0+); TOEFL iBT min 90 (writing 23, others 22); or PTE Academic min 64 (54 in all skills). English Medium of Instruction certificates are not accepted."
            },
            "other_language_requirements": "None; all coursework, seminars, and doctoral dissertations are in English.",
            "gender_specific_requirements": "None; equity and diversity candidates are strongly supported.",
            "financial_need_required": False,
            "special_eligibility_categories": "Scientia scheme targets global top-tier doctoral talent aligned with pre-defined strategic research projects.",
            "previous_scholarship_restrictions": "Cannot hold another major Commonwealth or university scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee waiver for up to 4 years (AUD 52,000 to 56,000 / year waived completely).",
                "amount": "100% covered (~AUD 54,000 / year value; ~PKR 9,990,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "Application fee is waived for Scientia PhD applicants who pass Expression of Interest (EOI) stage.",
                "amount": "AUD 125 waived value (~PKR 23,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from generous tax-free living stipend; modern on-campus university colleges and private Sydney apartments available.",
                "amount": "Paid from stipend (~AUD 1,600 to 2,000 / month)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Prestigious index-linked tax-free living allowance: AUD 42,455 per annum (~AUD 3,537 / month; ~PKR 660,000/month) for 4 full years.",
                "amount": "AUD 42,455 / year tax-free (~PKR 7,854,000 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Relocation allowance of up to AUD 2,000 provided to assist international scholars traveling from overseas to Sydney.",
                "amount": "Up to AUD 2,000 relocation grant (~PKR 370,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Subclass 500 Student Visa fee (AUD 1,600) paid directly to Department of Home Affairs.",
                "amount": "AUD 1,600 (~PKR 296,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Full standard Overseas Student Health Cover (OSHC) single policy funded directly by UNSW for the 4-year student visa duration.",
                "amount": "AUD 3,200 to 4,000 total value (~PKR 590,000 to 740,000)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered through the generous fortnightly stipend.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Funded by the admitting research institute and laboratory facilities (world-class quantum cleanrooms, GPU clusters).",
                "amount": "Covered by faculty and research center"
            },
            "research_funding_conference_grant": {
                "status": "100% COVERED",
                "details": "Dedicated Scientia Career and Research Development Support package: up to AUD 10,000 per annum (AUD 40,000 over 4 years) for international conference travel, specialized training, and research consumables.",
                "amount": "AUD 10,000 / year dedicated career support (~PKR 1,850,000 / yr)"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Sydney Opal card transit is self-funded (concession cards available for HDR candidates).",
                "amount": "Self-funded (~AUD 120 / month; ~PKR 22,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 68000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Group of Eight research powerhouse: University of New South Wales (UNSW Sydney, Australia)",
            "participating_institutions": [
                "UNSW Sydney - Kensington Main Campus (Sydney, NSW)",
                "Centre for Quantum Computation and Communication Technology (CQC2T - UNSW)",
                "UNSW School of Photovoltaic and Renewable Energy Engineering (SPREE)"
            ],
            "university_rankings_scope": "Ranked #19 globally in QS World University Rankings 2024/2025; member of Australia's prestigious Group of Eight (Go8). Global leader in quantum computing, silicon qubits, and solar photovoltaics.",
            "available_majors": [
                "School of Computer Science and Engineering: Quantum Software, AI, Machine Learning, Cyber Security",
                "Centre for Quantum Computation & Communication Technology: Silicon Quantum Computing, Nanoelectronics",
                "School of Photovoltaic and Renewable Energy Engineering: Perovskite Solar Cells, Grid Integration",
                "School of Electrical Engineering and Telecommunications: Systems and Control, Wireless Communications",
                "Graduate School of Biomedical Engineering: Neural Engineering, Biomaterials, Bioprinting"
            ],
            "english_taught_program_availability": True,
            "program_duration": "PhD: 4 years full-time research residency.",
            "admission_requirements_summary": "Bachelor's H1 or Master by Research with 3.8+ GPA, match with approved Scientia project, nomination from lead project supervisor, 2 referee reports, and IELTS 6.5 (TOEFL 90).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Quantum Computing and AI have extraordinary global competition; Renewable Energy Engineering and Biomedical Engineering offer slightly more specialized applicant pools.",
            "strategic_program_match_advice": "Scientia scholarships are awarded ONLY against approved strategic projects published on the UNSW Scientia portal each cycle. Candidates must browse the project directory, identify projects matching their thesis, submit an Expression of Interest (EOI) directly to the lead supervisor, and be nominated by them to submit a formal application."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.unsw.edu.au/research/hdr/scholarships/scientia",
            "portal_system_name": "UNSW Scientia PhD Online Portal & ApplyOnline Admissions System",
            "account_creation_instructions": "Explore approved projects on Scientia portal, submit online Expression of Interest (EOI) to project supervisor; upon supervisor invitation, submit formal application via ApplyOnline.",
            "step_by_step_workflow": [
                "Step 1 (June - July): Browse approved research projects on the UNSW Scientia Portal (unsw.edu.au/research/hdr/scholarships/scientia).",
                "Step 2 (July): Submit online Expression of Interest (EOI) for up to two projects, uploading CV, transcripts, and statement of research alignment.",
                "Step 3 (August): Lead project supervisors evaluate EOIs, conduct technical video interviews, and nominate their top candidate.",
                "Step 4 (Late August): Nominated candidates receive an official invitation code to lodge a formal application on UNSW ApplyOnline.",
                "Step 5 (Mid-September): Submit complete formal application dossier including referee reports and English language test scores.",
                "Step 6 (October - November): Central University Scientia Selection Panel reviews nominated candidates across faculties and determines awards.",
                "Step 7 (Mid-December): Official scholarship offers released; candidates accept offer and receive electronic Confirmation of Enrolment (CoE).",
                "Step 8 (December - January): Lodge Subclass 500 Student Visa application with Australian Department of Home Affairs.",
                "Step 9 (February): Travel to Sydney, attend UNSW Scientia induction and HDR orientation, and commence PhD candidature."
            ],
            "university_vs_scholarship_routing": "Multi-stage strategic application: Project nomination by supervisor is required before formal scholarship application can proceed.",
            "recommendation_letters_submission_method": "Two confidential academic referee reports submitted directly via the online referee portal by supervisors who know candidate's research capacity.",
            "personal_statement_prompts": "Scientia Statement of Purpose: Address the strategic project objectives, your relevant research background, future research ambitions, and commitment to public engagement and leadership.",
            "study_plan_research_proposal_requirements": "Tailored proposal (2-3 pages) expanding upon the advertised Scientia project description in consultation with the project supervisor.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications (with impact factors, citations, and venue ranking), patents, research awards, and code repositories.",
            "interviews_conducted": True,
            "interview_format_details": "In-depth 45-minute technical video interview conducted by project lead supervisor and co-supervisors assessing research mastery and vision.",
            "standardized_tests": "IELTS Academic 6.5 (6.0 in all bands) or TOEFL iBT 90 (23 writing) or PTE 64. GRE not required.",
            "application_fee_amount": "AUD 125 (Waived for invited Scientia applicants)",
            "attestation_requirements": "HEC Pakistan attestation required on all degrees and transcripts, accompanied by verified certified copies.",
            "translation_requirements": "Certified English translations for any non-English official documents.",
            "final_submission_method": "100% digital submission via UNSW ApplyOnline portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least two years.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Certified transcripts showing all semesters, grades, grading scale, and degree completion certificates.",
                "pakistan_specific_instruction": "Higher Education Commission (HEC) Pakistan attested documents."
            },
            {
                "document_name": "Scientia Supervisor Invitation / Endorsement",
                "mandatory": True,
                "specification": "Official invitation email / code generated following successful EOI review.",
                "pakistan_specific_instruction": "Mandatory prerequisite; cannot apply on ApplyOnline without supervisor nomination."
            },
            {
                "document_name": "Tailored Research Proposal",
                "mandatory": True,
                "specification": "Detailed 2 to 3 page proposal aligned specifically with the advertised Scientia project.",
                "pakistan_specific_instruction": "Demonstrate technical mastery of the project's scientific objectives."
            },
            {
                "document_name": "Academic Referee Reports (Two)",
                "mandatory": True,
                "specification": "Submitted directly by referees via UNSW referee online system.",
                "pakistan_specific_instruction": "Must be on institutional letterhead with verified university email addresses."
            },
            {
                "document_name": "English Language Proficiency Report",
                "mandatory": True,
                "specification": "Official IELTS, TOEFL, or PTE scorecard meeting UNSW minimum requirements.",
                "pakistan_specific_instruction": "Direct electronic score dispatch through testing agency portal."
            },
            {
                "document_name": "Curriculum Vitae and Publication Record",
                "mandatory": True,
                "specification": "Detailed CV listing full citations of peer-reviewed papers with DOIs and conference tiers.",
                "pakistan_specific_instruction": "Highlight first-author papers published in CORE A*/A or Scopus Q1 journals."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 June 2027 (EOI opens)",
            "application_deadline": "30 September 2027 (Formal application close)",
            "university_admission_deadline": "30 September 2027",
            "document_submission_deadline": "30 September 2027",
            "recommendation_letters_deadline": "7 October 2027",
            "interview_period": "August to September 2027",
            "shortlist_announcement": "Mid-November 2027",
            "final_result_acceptance_deadline": "15 December 2027",
            "visa_application_window": "December 2027 to February 2028",
            "semester_commencement": "Term 1 (Mid-February 2028)",
            "annual_cycle_notes": "Scientia PhD scheme runs on a single annual cycle for Term 1 (February) commencement."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Honours 1 equivalence, CGPA in Bachelor/Master degrees, and university pedigree)",
            "extracurricular_and_leadership_weight": "5% (Demonstrated leadership potential and public engagement capacity)",
            "research_experience_weight": "45% (Peer-reviewed publications, master thesis quality, and synergy with the strategic project)",
            "work_experience_weight": "5% (High-level industrial or laboratory research experience)",
            "personal_statement_weight": "5% (Statement of research purpose and leadership vision)",
            "recommendations_weight": "5% (Strength of academic referee appraisals)",
            "interview_weight": "0% (Official scoring is dossier-based; supervisor interview establishes EOI nomination)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 90 compliance)",
            "financial_need_weight": "0% (Exclusively merit and research performance based)",
            "selection_panel_composition": "Lead Project Supervisor, Faculty Scientia Panel, and Central University Scientia Selection Board chaired by Pro Vice-Chancellor Research Training.",
            "evaluation_methodology": "Rigorous two-phase selection: Phase 1 EOI review by project supervisor (only top 1 candidate nominated per project). Phase 2 competitive ranking by University Scientia Board evaluating research track record, academic brilliance, and alignment with UNSW strategic research priorities."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 EOIs submitted globally for ~100 Scientia fellowships",
            "total_scholarships_awarded": "~100 to 125 fully funded Scientia PhD fellowships",
            "acceptance_rate_global": "~3.5%",
            "acceptance_rate_pakistan": "~3.0% (Exceptionally competitive; awarded only to Pakistan's elite research scholars)",
            "typical_successful_applicant_gpa": "3.85+ / 4.00 CGPA (88%+ aggregate, class topper)",
            "typical_academic_and_research_profile": "First-class academic record, 2+ peer-reviewed papers in CORE A*/A or Q1 journals, demonstrated coding/experimental mastery, and seamless project alignment.",
            "common_backgrounds_of_winners": "Top graduates from NUST, FAST-NUCES, GIKI, UET, LUMS, and PIEAS with active research lab experience.",
            "high_representation_countries": "China, India, United States, United Kingdom, Pakistan, Iran, Germany, Singapore",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized commercial recruiters claiming to sell UNSW Scientia scholarship slots. Scientia scholarships are awarded strictly through project supervisor EOI nomination and central faculty board review."
            ],
            "application_fee_warning": "Invited Scientia applicants are exempt from application fees. Do not pay fees to unauthorized recruiters.",
            "agent_and_intermediary_warnings": "Scientia requires direct intellectual discourse with the project supervisor; using agents will lead to immediate rejection.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD 1,600; ~PKR 296,000).",
                "Biometrics and visa medical examination in Pakistan (~PKR 35,000 - 50,000).",
                "Initial settling cash and apartment bond in Sydney before first stipend disbursement (~AUD 2,500; ~PKR 460,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You can propose any random PhD topic. (FACT: Scientia scholarships are restricted strictly to pre-approved strategic projects published on the portal).",
                "CLAIM: English test can be waived with an MOI letter. (FACT: Official IELTS, TOEFL, or PTE test report is non-negotiable for UNSW HDR admission)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some third-party websites list the Scientia tenure as 3 years; official UNSW guidelines guarantee 4 full years of stipend and tuition waiver."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass annual candidature milestones: Confirmation Review (Year 1), Progress Review (Year 2), and Completion Review (Year 3).",
            "attendance_requirements": "Full-time physical research residency at UNSW Kensington campus and active involvement in project laboratory activities.",
            "academic_progress_monitoring": "Annual Research Progress Reviews submitted to Graduate Research School and approved by supervisory committee.",
            "work_restrictions_during_study": "Full-time candidates may engage in up to 8-10 hours/week of paid academic teaching (tutoring/lab demonstrating), provided it does not delay doctoral completion.",
            "home_country_return_obligation": "None. Graduates are eligible for Australian Subclass 485 Post-Study Work visa (3-4 years work rights) and qualify for Australia's Global Talent / Skilled Independent visa pathways.",
            "service_obligations_or_bonds": "Zero bond or repayment conditions.",
            "repayment_clawback_conditions": "Scholarship terminates upon withdrawal or failure of candidature milestones; past funds are not reclaimed.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Cannot switch project topics; scholarship is tied specifically to the approved Scientia research project.",
            "extension_policy": "Strictly fixed at 4 years maximum; no extensions permitted under any circumstances."
        },
        "official_sources_verified": [
            {
                "source_name": "UNSW Sydney Scientia PhD Scholarship Scheme Official Portal",
                "source_url": "https://www.unsw.edu.au/research/hdr/scholarships/scientia",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific number of projects allocated to each engineering school per annual cycle.",
                    "Exact numerical weighting between supervisor EOI recommendation score and central board score.",
                    "Historical nationality-wise breakdown of Scientia awardees."
                ]
            },
            {
                "source_name": "UNSW Graduate Research School Higher Degree by Research Guidelines",
                "source_url": "https://www.unsw.edu.au/research/hdr/application",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waitlist ranking criteria for unfilled Scientia project allocations.",
                    "Internal faculty budget top-up mechanisms for computing hardware."
                ]
            }
        ]
    }
}
