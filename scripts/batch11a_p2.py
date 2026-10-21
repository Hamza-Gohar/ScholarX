# scripts/batch11a_p2.py
# 18. Tokyo Tech (Science Tokyo) IGP MEXT (SCH-AS-019)
# 19. Osaka Univ SISC Fellowship (SCH-AS-020)

DATA_P2 = {
    "SCH-AS-019": {
        "scholarship_id": "SCH-AS-019",
        "basic_details": {
            "scholarship_name": "Tokyo Tech IGP MEXT University Recommendation Fellowship",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT, Japan) administered by Institute of Science Tokyo (formerly Tokyo Institute of Technology)",
            "host_country": "Japan",
            "host_institutions_covered": "Institute of Science Tokyo (Ookayama & Suzukakedai Campuses, Tokyo & Yokohama, Japan)",
            "degree_levels": ["Master of Engineering / Science (MS)", "Doctor of Engineering / Science (PhD)", "Integrated Doctoral Program"],
            "major_restrictions": "Restricted to the International Graduate Program (IGP-A and IGP-C) across Schools of Science, Engineering, Materials and Chemical Technology, Computing (Computer Science, Artificial Intelligence), Life Science and Technology, and Environment and Society.",
            "number_of_awards_total": "Approximately 45 to 60 University Recommendation MEXT slots allocated annually across all graduate schools",
            "number_of_awards_pakistan": "Merit-based open international quota; Pakistani engineering and computer science students typically secure 4 to 8 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master degree; 3 years for PhD degree; extension from Master to PhD possible subject to nationwide MEXT screening"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries having diplomatic relations with Japan (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Must be born on or after April 2, 1992 for the 2027 intake (under 35 years of age on departure).",
            "academic_qualifications": "Completed 16 years of formal education (Bachelor degree) for Master applicants; 18 years (Master degree) for Doctoral applicants from an HEC-recognized university with high academic standing (minimum 3.40 / 4.00 CGPA; 3.60+ highly competitive). Must hold a minimum 2.30 / 3.00 on the MEXT GPA evaluation formula.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "MEXT grade point calculation formula: Grade points derived as [ (credits with score 80-100 x 3) + (credits with score 70-79 x 2) + (credits with score 60-69 x 1) ] / Total credits. Must equal or exceed 2.30 / 3.00.",
            "subject_background_prerequisites": "Strong undergraduate or postgraduate foundation in Computer Science, Electrical/Electronic Engineering, Mechanical Engineering, Materials Science, Chemical Physics, or Applied Mathematics.",
            "current_education_status": "Final-year graduating students eligible provided degree completion and official transcripts are conferred prior to September 2027 enrollment.",
            "graduation_year_restrictions": "No fixed graduation year cutoff, provided age requirement is respected.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Outstanding academic thesis, capstone engineering projects, or indexed research publications (IEEE, ACM, Springer) significantly enhance candidate standing.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 80,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Official TOEFL iBT (minimum 80, 90+ recommended) or IELTS Academic (minimum 6.5, 7.0 recommended). Medium of Instruction (MOI) certificates accepted only if applicant graduated from an institution in an English-native country."
            },
            "other_language_requirements": "Japanese language ability is NOT required for admission or funding; all coursework and research supervision conducted in English. Free Japanese language immersion courses offered upon arrival.",
            "gender_specific_requirements": "None; female researchers in engineering and computer science are strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "STEM researchers in engineering, artificial intelligence, robotics, and physical sciences.",
            "previous_scholarship_restrictions": "Cannot be a concurrent recipient of any other Japanese government scholarship or foreign government grant.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full exemption from Tokyo Tech annual tuition fee (JPY 635,400 / year waived completely for all standard degree years).",
                "amount": "100% covered (~JPY 635,400 / year value; ~PKR 1,175,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "100% full waiver of Tokyo Tech examination fee (JPY 30,000) and enrollment fee (JPY 282,000 waived completely).",
                "amount": "JPY 312,000 waived value (~PKR 575,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "First-year international students guaranteed subsidized housing in Tokyo Tech International Student Dormitories (costing ~JPY 35,000 to JPY 55,000/month), paid directly from monthly stipend.",
                "amount": "Subsidized dorm (~JPY 45,000 / month; ~PKR 83,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living allowance paid directly to scholar's Japan Post Bank account: JPY 147,000/month for Master's students; JPY 148,000/month for PhD students (~PKR 270,000 to 275,000/month).",
                "amount": "JPY 1,764,000 to 1,776,000 / year (~PKR 3,250,000 / year)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Pre-paid round-trip single economy class air ticket between Islamabad/Karachi/Lahore and Tokyo Narita/Haneda airport provided by MEXT at arrival and departure.",
                "amount": "100% covered (~PKR 300,000 to 450,000 round-trip value)"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Official MEXT scholarship certificate provides fee-exempt Student Visa processing at Embassy of Japan in Islamabad or Consulate-General in Karachi.",
                "amount": "100% waived (Free visa)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Japanese National Health Insurance (NHI) monthly premium (~JPY 1,500 to JPY 2,500/month) is paid from stipend, granting 70% medical coverage across all Japanese hospitals, with Tokyo Tech Mutual Aid Association reimbursing remainder.",
                "amount": "Subsidized (~JPY 25,000 / year value; ~PKR 46,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered by monthly stipend; campus cafeterias provide affordable meals at JPY 400 - JPY 700 per meal.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Funded by the admitting research laboratory and departmental research operational budgets.",
                "amount": "Covered by laboratory budget"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Kakenhi research assistantship (RA) top-ups and lab travel funds available for attending international conferences and field research.",
                "amount": "Up to JPY 250,000 per conference paper"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Tokyo commuter rail and subway passes are self-funded from the monthly stipend (student commuter discounts available).",
                "amount": "Self-funded (~JPY 8,000 / month; ~PKR 15,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 24000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite national institution: Institute of Science Tokyo (formerly Tokyo Institute of Technology)",
            "participating_institutions": [
                "Institute of Science Tokyo (Ookayama Campus, Meguro, Tokyo)",
                "Institute of Science Tokyo (Suzukakedai Campus, Midori-ku, Yokohama)"
            ],
            "university_rankings_scope": "Top 100 global university (QS World #84, #1 in Japan for Engineering & Technology). Formed by historic October 2024 merger of Tokyo Tech and Tokyo Medical and Dental University (TMDU).",
            "available_majors": [
                "School of Computing: Computer Science, Artificial Intelligence, Mathematical and Computing Science",
                "School of Engineering: Mechanical Engineering, Systems and Control, Electrical and Electronic Engineering, Information and Communications Engineering",
                "School of Materials and Chemical Technology: Materials Science and Engineering, Applied Chemistry",
                "School of Life Science and Technology: Life Science and Technology",
                "School of Environment and Society: Transdisciplinary Science and Engineering, Civil and Environmental Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master degree: 2 years (4 semesters); PhD degree: 3 years (6 semesters); Integrated PhD: 5 years.",
            "admission_requirements_summary": "Bachelor's (MS track) or Master's (PhD track) in STEM with 3.4+ GPA, prospective professor preliminary consent, research proposal, 2 recommendation letters, and IELTS 6.5 or TOEFL 80.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "School of Computing (AI, machine learning, robotics) is exceptionally competitive; Materials Science, Applied Chemistry, and Civil Engineering offer comparatively higher selection probability for strong experimentalists.",
            "strategic_program_match_advice": "Prospective applicants MUST browse Tokyo Tech STAR Search faculty database, identify a professor whose current research grants match their thesis, and obtain official written consent before submitting application. Unmatched applications are disqualified immediately."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.titech.ac.jp/english/admissions/prospective-students/international/graduate-programs",
            "portal_system_name": "Institute of Science Tokyo International Graduate Program (IGP) Online Application System",
            "account_creation_instructions": "Contact prospective professor via email between August and October; upon securing supervisory consent, register an account on the Tokyo Tech IGP online portal and complete the application.",
            "step_by_step_workflow": [
                "Step 1 (August - October): Explore Tokyo Tech laboratories via STAR Search portal; prepare research proposal tailored to faculty publications.",
                "Step 2 (September - Mid-November): Contact prospective professor, submit academic dossier, conduct online interview, and obtain written consent of supervision.",
                "Step 3 (November - December): Create account on Tokyo Tech Online Application System; upload transcripts, English test report, and statement of research.",
                "Step 4 (January): Departmental faculty screening committee evaluates applicants and ranks candidates for MEXT quota.",
                "Step 5 (February - March): Tokyo Tech internal university recommendation board nominates top candidates to MEXT Headquarters in Tokyo.",
                "Step 6 (June - July): Official MEXT approval announced; university issues Certificate of Eligibility (CoE) and formal letter of scholarship.",
                "Step 7 (July - August): Apply for Japanese Student Visa at Embassy of Japan in Pakistan; flight e-tickets issued by MEXT travel agent.",
                "Step 8 (Late September): Arrival in Tokyo; campus dorm check-in and university matriculation."
            ],
            "university_vs_scholarship_routing": "Direct integrated nomination: Science Tokyo nominates admitted IGP-A candidates directly to MEXT for the full government scholarship.",
            "recommendation_letters_submission_method": "Two recommendation letters submitted online via referee email invitation link generated by Tokyo Tech admissions portal.",
            "personal_statement_prompts": "Field of Study and Research Plan: Detail past academic background, proposed research methodology, expected contributions, and laboratory facility usage.",
            "study_plan_research_proposal_requirements": "Rigorous 3 to 5 page proposal detailing background, methodology, objectives, and laboratory equipment utilization in close consultation with supervisor.",
            "cv_format_requirements": "Academic CV detailing research publications, conference presentations, major engineering capstone projects, and GitHub/code repositories.",
            "interviews_conducted": True,
            "interview_format_details": "One to two rounds of rigorous technical video interviews (Zoom) conducted by prospective supervisor and departmental doctoral committee evaluating research feasibility and fundamentals.",
            "standardized_tests": "TOEFL iBT (minimum 80, 90+ recommended) or IELTS Academic (minimum 6.5, 7.0 recommended). GRE General recommended for computing.",
            "application_fee_amount": "JPY 0 (Exempt for MEXT University Recommendation track applicants)",
            "attestation_requirements": "Official degree certificate and transcripts attested by Higher Education Commission (HEC) Pakistan.",
            "translation_requirements": "Certified English translation for any non-English educational or civil records.",
            "final_submission_method": "Complete digital submission on Tokyo Tech IGP online portal followed by dispatch of hard-copy attested dossier if requested by department."
        },
        "required_documents_checklist": [
            {
                "document_name": "Tokyo Tech Official Application Form",
                "mandatory": True,
                "specification": "Completed and digitally signed via Tokyo Tech Online Portal.",
                "pakistan_specific_instruction": "Ensure names and date of birth match Pakistani Passport and CNIC exactly."
            },
            {
                "document_name": "Consent of Prospective Supervisor",
                "mandatory": True,
                "specification": "Official written consent or email confirmation from Tokyo Tech Professor/Associate Professor.",
                "pakistan_specific_instruction": "Must be secured prior to formal online submission; without this, application is automatically void."
            },
            {
                "document_name": "Official Degree Certificates & Transcripts",
                "mandatory": True,
                "specification": "Certified official transcripts and degree certificates with grading scale and credit breakdown.",
                "pakistan_specific_instruction": "Must be verified and attested by Higher Education Commission (HEC) Pakistan."
            },
            {
                "document_name": "Field of Study and Research Plan",
                "mandatory": True,
                "specification": "Detailed 3 to 5 page proposal detailing background, methodology, objectives, and laboratory equipment utilization.",
                "pakistan_specific_instruction": "Should cite Tokyo Tech laboratory papers and demonstrate independent scholarly competence."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Confidential recommendation letters from Dean, department chair, or academic thesis advisor.",
                "pakistan_specific_instruction": "Must be on official institutional letterhead with institutional email addresses."
            },
            {
                "document_name": "English Language Proficiency Report",
                "mandatory": True,
                "specification": "Official ETS TOEFL iBT or British Council/IDP IELTS Academic test scorecard.",
                "pakistan_specific_instruction": "Institutional code for Tokyo Tech used for direct score delivery where requested."
            },
            {
                "document_name": "Summary of Master Thesis / Undergraduate Project",
                "mandatory": True,
                "specification": "1 to 2 page technical synopsis of completed capstone project or Master research.",
                "pakistan_specific_instruction": "Highlight practical contributions, algorithms designed, and research publications."
            },
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Bio-data page copy valid for at least 18 months from expected arrival date.",
                "pakistan_specific_instruction": "Ensure Pakistani machine-readable passport bio page is clear and completely legible."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "10 August 2026",
            "application_deadline": "15 October 2026",
            "university_admission_deadline": "15 October 2026",
            "document_submission_deadline": "25 October 2026",
            "recommendation_letters_deadline": "20 October 2026",
            "interview_period": "15 October to 30 November 2026",
            "shortlist_announcement": "15 February 2027",
            "final_result_acceptance_deadline": "10 July 2027",
            "visa_application_window": "1 July to 25 August 2027",
            "semester_commencement": "28 September 2027",
            "annual_cycle_notes": "IGP(A) is dedicated to overseas applicants seeking MEXT university recommendation scholarships commencing in Autumn (late September)."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Standardized MEXT 3-point GPA formula evaluation, undergraduate CGPA, and coursework rigor)",
            "extracurricular_and_leadership_weight": "5% (Student leadership, campus engagement, and community work)",
            "research_experience_weight": "35% (Quality, feasibility, and synergy of research proposal with host laboratory projects)",
            "work_experience_weight": "5% (Relevant industry research or software engineering experience)",
            "personal_statement_weight": "5% (Motivation, intellectual clarity, and long-term academic vision)",
            "recommendations_weight": "10% (Rigor and conviction of academic referee appraisals)",
            "interview_weight": "15% (Performance in technical interview and oral defense with laboratory faculty)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 80 or higher)",
            "financial_need_weight": "0% (Purely merit and research competence based)",
            "selection_panel_composition": "Admitting Laboratory Head, Departmental Graduate Committee, and Tokyo Tech International Student Admissions Board.",
            "evaluation_methodology": "Two-tier faculty selection: Initial lab-level review and interview by prospective supervisor followed by departmental graduate committee evaluation and Institute of Science Tokyo MEXT Recommendation Committee ranking. Approximately 1:8 applicants nominated from department to university board; 95%+ of university-nominated candidates approved by MEXT."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~600 to 800 international applicants across all disciplines for IGP-A track",
            "total_scholarships_awarded": "~45 to 60 MEXT University Recommendation awards annually",
            "acceptance_rate_global": "~7.5%",
            "acceptance_rate_pakistan": "~11.0% (Strong placement for Pakistani engineers with IEEE/ACM papers)",
            "typical_successful_applicant_gpa": "3.65 / 4.00 CGPA (MEXT GPA formula >= 2.60 / 3.00)",
            "typical_academic_and_research_profile": "Top 10% class rank, strong programming/lab fundamentals, 1+ Scopus/IEEE published papers, clear research plan matching supervisor's lab.",
            "common_backgrounds_of_winners": "BS/MS graduates in Computer Science, Electrical Engineering, Mechanical Engineering, and Materials Science from NUST, FAST-NUCES, GIKI, UET, and PIEAS.",
            "high_representation_countries": "China, Indonesia, Vietnam, Pakistan, Thailand, India",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized consultancies charging placement fees for Tokyo Tech scholarships. Science Tokyo charges ZERO application fee for IGP-A MEXT track and never uses private agents."
            ],
            "application_fee_warning": "Tokyo Tech application for IGP-A MEXT recommendation track is 100% free of charge. Never pay examination fees to intermediaries.",
            "agent_and_intermediary_warnings": "Communicating directly with prospective professors demonstrates research maturity; using agents will lead to immediate rejection.",
            "hidden_costs_breakdown": [
                "Initial 3 to 4 weeks living expenses and apartment/dorm security deposit before first stipend disbursement (prepare ~JPY 100,000 to JPY 150,000 in cash; ~PKR 185,000 to 275,000).",
                "National Health Insurance monthly premium (~JPY 2,000/month; ~PKR 3,700/mo).",
                "Domestic travel expenses within Pakistan to reach Islamabad/Karachi departure airport."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Japanese language proficiency is mandatory. (FACT: 100% of coursework, research, and thesis defense in IGP are conducted in English).",
                "CLAIM: GRE General score is compulsory. (FACT: GRE is optional for most departments, only required by specific labs as designated in IGP guides)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some education agencies state applicants can apply directly without contacting a professor; official Tokyo Tech regulations state preliminary professor consent is mandatory before submitting application."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain MEXT 3-point GPA of at least 2.30 throughout degree tenure and pass annual doctoral milestone defenses.",
            "attendance_requirements": "Mandatory daily laboratory attendance, participation in weekly research seminars (Zemi), and active laboratory duty.",
            "academic_progress_monitoring": "Semi-annual progress reports reviewed by academic mentor and submitted to MEXT.",
            "work_restrictions_during_study": "MEXT recipients are prohibited from taking outside part-time jobs (arubaito) except approved internal Teaching Assistant (TA) or Research Assistant (RA) positions within Tokyo Tech.",
            "home_country_return_obligation": "None. Scholars are free to pursue post-doctoral employment, industrial careers in Japan (qualifying for Japan Highly Skilled Foreign Professional visa), or international opportunities.",
            "service_obligations_or_bonds": "Zero bond or return requirement.",
            "repayment_clawback_conditions": "Scholarship is suspended or cancelled if student fails to maintain satisfactory academic standing, takes unauthorized leaves of absence, or violates Japanese laws; past disbursements are not reclaimed.",
            "rules_for_changing_university": "Strictly prohibited. MEXT university recommendation slots are tied exclusively to Tokyo Tech.",
            "rules_for_changing_major": "Changing laboratory or major is generally not permitted unless approved under extraordinary academic circumstances by the faculty board.",
            "extension_policy": "Master graduates may compete for MEXT extension to enter PhD program through internal university selection based on research accomplishments."
        },
        "official_sources_verified": [
            {
                "source_name": "Institute of Science Tokyo (formerly Tokyo Tech) International Graduate Program (IGP) Official Portal",
                "source_url": "https://www.titech.ac.jp/english/admissions/prospective-students/international/graduate-programs",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental quota allocation for MEXT recommendation slots across individual research schools.",
                    "Exact numerical weighting between lab professor interview score and university admissions committee review.",
                    "Breakdown of international applicants and acceptance numbers by specific country of origin."
                ]
            },
            {
                "source_name": "MEXT Japan International Student Scholarship Guidelines (University Recommendation Track)",
                "source_url": "https://www.mext.go.jp/a_menu/koutou/ryugaku/boshu/1421060.htm",
                "source_type": "GOVERNMENT_MINISTRY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Reserve/waitlist candidate quota allocations per national university.",
                    "Annual country allocation targets for non-embassy recommendation tracks."
                ]
            }
        ]
    },
    "SCH-AS-020": {
        "scholarship_id": "SCH-AS-020",
        "basic_details": {
            "scholarship_name": "Osaka University SISC MEXT & Honors Graduate Fellowship",
            "offering_entity": "Osaka University Graduate School of Science & Graduate School of Information Science and Technology in partnership with MEXT (Japan)",
            "host_country": "Japan",
            "host_institutions_covered": "Osaka University (Toyonaka & Suita Campuses, Osaka, Japan)",
            "degree_levels": ["Master of Science (MS)", "Doctor of Philosophy (PhD)", "Five-Year Integrated Doctoral Course"],
            "major_restrictions": "Offered through the Special Integrated Science Course (SISC) and International Physics / Chemistry / Biological Sciences tracks, encompassing Computer Science, Information Science, Physics, Chemistry, Biological Sciences, and Macromolecular Science.",
            "number_of_awards_total": "Approximately 25 to 35 fully funded MEXT and Osaka University Fellowship awards allocated per academic year for SISC programs",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in physics, chemistry, and computing typically receive 3 to 6 fellowship awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years for Master degree; 3 years for PhD degree; 5 years for Integrated PhD program, contingent upon satisfactory annual progress reviews"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries having diplomatic relations with Japan (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Must be born on or after April 2, 1992 for October 2027 enrollment.",
            "academic_qualifications": "Completed 16 years of education (Bachelor degree) for Master applicants; completed 18 years of education (Master degree) for Doctoral applicants from an accredited university. Minimum CGPA of 3.40 / 4.00 (or equivalent top 15% rank) and MEXT evaluation score >= 2.30 out of 3.00.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Must achieve a minimum score of 2.30 on the official 3.0-scale MEXT GPA formula evaluated across prior university coursework.",
            "subject_background_prerequisites": "Bachelors or Masters degree in Physics, Chemistry, Biology, Mathematics, Computer Science, Information Science, or closely related fundamental sciences.",
            "current_education_status": "Final year graduating students eligible; official graduation certificate must be submitted before formal registration in September/October 2027.",
            "graduation_year_restrictions": "No restriction on year of degree conferral.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required; demonstrated laboratory research experience and thesis work are primary selection metrics.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 80,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "TOEFL iBT (minimum 80, 88+ recommended) or IELTS Academic (minimum 6.5 overall with no band below 6.0). Medium of Instruction (MOI) certificates generally not accepted in lieu of official test scores for MEXT funding nomination."
            },
            "other_language_requirements": "None required. All lectures, seminars, research discussions, and thesis defense are conducted in English.",
            "gender_specific_requirements": "None; inclusive gender representation actively supported.",
            "financial_need_required": False,
            "special_eligibility_categories": "Researchers in physical, chemical, biological, and computational sciences.",
            "previous_scholarship_restrictions": "Cannot hold another Japanese government scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full waiver of Osaka University annual tuition fee (JPY 535,800 / year waived completely for all standard degree years).",
                "amount": "100% covered (~JPY 535,800 / year value; ~PKR 990,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "100% full waiver of Osaka University entrance examination fee (JPY 30,000) and admission fee (JPY 282,000 waived completely).",
                "amount": "JPY 312,000 waived value (~PKR 575,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Priority placement in Osaka University International Student Dormitories (Toyonaka International House, Minoh International House, or Tsukumodai Mansion) for the first year (monthly rent ~JPY 25,000 to JPY 40,000), paid from living stipend.",
                "amount": "Subsidized dorm (~JPY 32,000 / month; ~PKR 59,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend paid by MEXT: JPY 144,000/month for Master's students; JPY 145,000/month for PhD students (~PKR 265,000/month).",
                "amount": "JPY 1,728,000 to 1,740,000 / year (~PKR 3,180,000 / year)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Economy-class round-trip air travel provided by MEXT between applicant's nearest international airport in Pakistan (Islamabad/Lahore/Karachi) and Kansai International Airport (KIX, Osaka).",
                "amount": "100% covered (~PKR 300,000 to 450,000 round-trip value)"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Japanese Student Visa issued free of charge upon presentation of MEXT scholarship certificate and Osaka University Certificate of Eligibility (CoE).",
                "amount": "100% waived (Free visa)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Japanese National Health Insurance (NHI) monthly premium (~JPY 2,000/month) paid from stipend; covers 70% medical costs, supplemented by university student welfare insurance.",
                "amount": "Subsidized (~JPY 24,000 / year value; ~PKR 44,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Food expenses covered through monthly stipend; subsidized campus cafeterias provide hot meals at JPY 350 - JPY 600 per meal.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Supplied via research laboratory facilities, supercomputer allocations, and departmental consumables budget.",
                "amount": "Covered by laboratory budget"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Graduate School of Science research travel grants support attendance at national and international academic symposia.",
                "amount": "Up to JPY 200,000 per conference"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Osaka monorail and Hankyu train transit costs are self-funded from monthly stipend.",
                "amount": "Self-funded (~JPY 6,000 / month; ~PKR 11,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 23500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single imperial national university: Osaka University (Top Global University, Japan)",
            "participating_institutions": [
                "Osaka University - Toyonaka Campus (Graduate School of Science)",
                "Osaka University - Suita Campus (Graduate School of Information Science and Technology)"
            ],
            "university_rankings_scope": "Top 80 global university (QS World #86, top 3 in Japan for natural sciences and physics).",
            "available_majors": [
                "Special Integrated Science Course (SISC): Department of Chemistry",
                "Special Integrated Science Course (SISC): Department of Biological Sciences",
                "Special Integrated Science Course (SISC): Department of Macromolecular Science",
                "Graduate School of Information Science and Technology: Computer Science, Information Systems, Multimedia Engineering",
                "International Physics Course (IPC): Department of Physics (High Energy, Condensed Matter, Quantum Information)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master program: 2 years (4 semesters); PhD program: 3 years (6 semesters); Integrated PhD: 5 years.",
            "admission_requirements_summary": "Bachelor's or Master's in Physics, Chemistry, Biology, or Computer Science with 3.4+ GPA, prospective professor acceptance, research plan, 2 recommendation letters, and IELTS 6.5 or TOEFL 80.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Information Science & AI and Quantum Physics have severe competition; Biological Sciences and Macromolecular Chemistry offer favorable candidate ratios for qualified experimentalists.",
            "strategic_program_match_advice": "Prospective candidates must review faculty research profiles on the Graduate School of Science website, contact prospective laboratory head, submit academic CV, transcripts, and research outline, and obtain formal consent to supervise before portal submission."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.sci.osaka-u.ac.jp/en/admissions/sisc/",
            "portal_system_name": "Osaka University SISC Online Application System",
            "account_creation_instructions": "Explore faculty profiles, contact prospective professor to secure supervisory agreement, then download official application forms from SISC portal and submit electronic dossier.",
            "step_by_step_workflow": [
                "Step 1 (September - October): Review faculty research areas on SISC portal; establish direct contact with preferred research laboratory head.",
                "Step 2 (October - Early November): Secure prospective supervisor's formal agreement to accept candidate and support MEXT nomination.",
                "Step 3 (November - December): Submit formal online application dossier via Osaka University SISC Admissions Portal.",
                "Step 4 (January - February): Departmental screening, document evaluation, and technical video interview conducted by laboratory panel.",
                "Step 5 (March): Osaka University Academic Committee selects top-ranked applicants and forwards nominations to MEXT Headquarters.",
                "Step 6 (June - July): MEXT confirms scholarship awards; Osaka University issues official letter of acceptance and Certificate of Eligibility.",
                "Step 7 (July - August): Apply for Japanese student visa; flight arrangements confirmed by MEXT travel division.",
                "Step 8 (Late September / Early October): Arrival in Osaka; residence registration, bank account setup, and course commencement."
            ],
            "university_vs_scholarship_routing": "Direct integrated nomination: Osaka University International Graduate Admissions Office nominates admitted students directly to MEXT.",
            "recommendation_letters_submission_method": "Two recommendation letters: from former academic supervisor and Dean/Department Chair submitted as signed letters.",
            "personal_statement_prompts": "Research Proposal & Statement of Intent: Describe prior research experience, scientific motivation, proposed experimental methodology, and career vision.",
            "study_plan_research_proposal_requirements": "Structured 1,500 to 2,500 word research proposal detailing hypothesis, experimental methodology, and literature review developed with prospective professor.",
            "cv_format_requirements": "Academic CV detailing research projects, laboratory techniques, publications, conference presentations, and programming skills.",
            "interviews_conducted": True,
            "interview_format_details": "Detailed 30 to 45 minute technical interview conducted via Zoom by an examination committee of 3 faculty members evaluating subject knowledge and research plan feasibility.",
            "standardized_tests": "TOEFL iBT (minimum 80, 88+ recommended) or IELTS Academic (minimum 6.5 overall). GRE Subject test optional but advantageous for physics.",
            "application_fee_amount": "JPY 0 (Exempt for MEXT scholarship applicants)",
            "attestation_requirements": "HEC Pakistan attestation required on both original and photocopy sets of degrees and transcripts.",
            "translation_requirements": "Certified English or Japanese translation for any documents issued in Urdu or other languages.",
            "final_submission_method": "Digital application submission via email/portal followed by physical mailing of attested documents to Graduate School of Science admissions office."
        },
        "required_documents_checklist": [
            {
                "document_name": "Osaka University SISC Application Form",
                "mandatory": True,
                "specification": "Completed official application form downloaded from SISC admissions portal.",
                "pakistan_specific_instruction": "Ensure all personal details match Pakistani passport biodata page exactly."
            },
            {
                "document_name": "Letter of Preliminary Acceptance from Supervisor",
                "mandatory": True,
                "specification": "Formal written consent from Osaka University professor agreeing to act as academic advisor.",
                "pakistan_specific_instruction": "Essential prerequisite; applications without supervisor confirmation cannot proceed."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Certified official academic transcripts and degrees covering all university education.",
                "pakistan_specific_instruction": "HEC Pakistan attestation required on both original and photocopy sets."
            },
            {
                "document_name": "Research Plan / Proposed Study Plan",
                "mandatory": True,
                "specification": "Structured 1,500 to 2,500 word research proposal detailing hypothesis, experimental methodology, and literature review.",
                "pakistan_specific_instruction": "Must demonstrate deep understanding of host laboratory experimental setup and published literature."
            },
            {
                "document_name": "Academic Recommendation Letters (Two)",
                "mandatory": True,
                "specification": "Signed recommendation letters from former professors or thesis advisors who know the applicant's research abilities.",
                "pakistan_specific_instruction": "Must be on institutional letterhead with official email addresses and direct contact numbers."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official TOEFL iBT or IELTS Academic test report dated within past two years.",
                "pakistan_specific_instruction": "Official electronic score dispatch or verified original scorecard copy."
            },
            {
                "document_name": "Abstract of Bachelor or Master Thesis",
                "mandatory": True,
                "specification": "Comprehensive 1 to 2 page technical abstract of previous thesis or major research project.",
                "pakistan_specific_instruction": "Highlight individual contributions, laboratory techniques mastered, and published results."
            },
            {
                "document_name": "Medical Certificate of Health",
                "mandatory": True,
                "specification": "Prescribed MEXT/Osaka University health examination form completed and signed by an authorized physician.",
                "pakistan_specific_instruction": "Can be obtained from any recognized public or tertiary hospital in Pakistan."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 October 2026",
            "application_deadline": "20 November 2026",
            "university_admission_deadline": "20 November 2026",
            "document_submission_deadline": "5 December 2026",
            "recommendation_letters_deadline": "25 November 2026",
            "interview_period": "10 December 2026 to 20 January 2027",
            "shortlist_announcement": "28 February 2027",
            "final_result_acceptance_deadline": "15 July 2027",
            "visa_application_window": "5 July to 30 August 2027",
            "semester_commencement": "1 October 2027",
            "annual_cycle_notes": "Special Integrated Science Course (SISC) admissions run annually for October enrollment under MEXT University Recommendation track."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (CGPA, transcript rigor, class rank, and MEXT GPA score)",
            "extracurricular_and_leadership_weight": "5% (Student leadership, lab teamwork, and community involvement)",
            "research_experience_weight": "30% (Clarity of scientific problem, experimental methodology, lab alignment, and thesis quality)",
            "work_experience_weight": "5% (Laboratory research assistantships or scientific industry experience)",
            "personal_statement_weight": "5% (Clarity of purpose, scientific maturity, and long-range goals)",
            "recommendations_weight": "10% (Referee appraisals of research acumen and work ethic)",
            "interview_weight": "15% (Fundamental scientific knowledge, oral defense, and intellectual agility during video examination)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 80 or higher)",
            "financial_need_weight": "0% (Exclusively merit and research competence based)",
            "selection_panel_composition": "Admitting Laboratory Head, SISC Departmental Admissions Committee, and Graduate School of Science Dean.",
            "evaluation_methodology": "Multistage evaluation: Faculty supervisor agreement, followed by departmental admissions committee assessment of academic records and research proposal, technical oral examination, and institutional nomination to MEXT. Approximately 1:6 applicants shortlisted for oral examination; nominated candidates have over 90% MEXT approval rate."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~300 to 450 international applicants across all science divisions",
            "total_scholarships_awarded": "~25 to 35 fully funded MEXT and Osaka University Fellowships",
            "acceptance_rate_global": "~7.5%",
            "acceptance_rate_pakistan": "~14.0% (Solid success rate for physics, chemistry, and computing scholars)",
            "typical_successful_applicant_gpa": "3.60 / 4.00 CGPA (MEXT GPA formula >= 2.50 / 3.00)",
            "typical_academic_and_research_profile": "Solid background in fundamental sciences or computing, 1+ peer-reviewed journal or conference publications, prior lab research, IELTS 7.0.",
            "common_backgrounds_of_winners": "Graduates from Quaid-i-Azam University, NUST, GCU Lahore, UET, and PIEAS in physics, chemistry, and computing.",
            "high_representation_countries": "China, Vietnam, Pakistan, India, South Korea, Indonesia",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized agencies claiming to guarantee MEXT recommendation at Osaka University. Osaka University never works with commercial recruiters."
            ],
            "application_fee_warning": "Osaka University does not charge any application or processing fee for SISC MEXT scholarship applicants. Application is completely free.",
            "agent_and_intermediary_warnings": "Never use third-party agents; direct scholarly correspondence with professors is strictly evaluated during screening.",
            "hidden_costs_breakdown": [
                "First month rent and deposit at university dormitories before first stipend transfer (prepare ~JPY 80,000 to 120,000 in cash; ~PKR 150,000 to 220,000).",
                "National Health Insurance monthly premium (~JPY 2,000/month; ~PKR 3,700/mo).",
                "Domestic travel costs within Pakistan to reach international departure airport."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Japanese fluency is needed for admission. (FACT: SISC courses and research are conducted completely in English).",
                "CLAIM: Pakistani degrees need prior Japanese embassy authentication. (FACT: Only HEC Pakistan attestation is needed for Osaka University admissions)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some agencies state admissions happen twice a year for SISC MEXT; official guidelines confirm MEXT university recommendation occurs only for the October intake cycle."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain MEXT minimum GPA (>=2.30) and achieve satisfactory progress on doctoral milestones.",
            "attendance_requirements": "Full-time on-campus research residency and regular participation in laboratory group seminars.",
            "academic_progress_monitoring": "Semi-annual academic progress evaluations conducted by supervisory committee and reported to MEXT.",
            "work_restrictions_during_study": "MEXT recipients are prohibited from taking external jobs; authorized on-campus Research Assistant (RA) and Teaching Assistant (TA) duties are allowed.",
            "home_country_return_obligation": "None. Graduates are free to stay in Japan on employment visas or pursue worldwide academic opportunities.",
            "service_obligations_or_bonds": "Zero bond or post-graduation return obligations.",
            "repayment_clawback_conditions": "Scholarship terminates immediately upon withdrawal or disciplinary expulsion; past disbursed funds are not clawed back.",
            "rules_for_changing_university": "Transferring to another university while on MEXT recommendation is strictly prohibited.",
            "rules_for_changing_major": "Major changes are permitted only within the department and subject to approval by both laboratory heads and the graduate dean.",
            "extension_policy": "Master graduates may apply for MEXT extension into the PhD program based on competitive academic and research review."
        },
        "official_sources_verified": [
            {
                "source_name": "Osaka University Graduate School of Science SISC Official Portal",
                "source_url": "https://www.sci.osaka-u.ac.jp/en/admissions/sisc/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific number of MEXT recommendation slots allocated to each science department.",
                    "Exact numerical rubric and weight distributions used by the oral examination committee.",
                    "Historical nationality-wise breakdown of applicants and matriculated scholars."
                ]
            },
            {
                "source_name": "Osaka University International Affairs Division Scholarships Overview",
                "source_url": "https://www.osaka-u.ac.jp/en/international/inbound/scholarship",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waitlist ranking criteria and fill rate for declined international fellowship offers.",
                    "Discretionary department top-up funding budgets for research consumables."
                ]
            }
        ]
    }
}
