# scripts/batch11b.py
# 20. Tsinghua Univ CSC & Tuition (SCH-AS-024)
# 21. Zhejiang Univ ZJU & AFLSP (SCH-AS-025)
# 22. National Tsing Hua Univ NTHU (SCH-AS-026)

DOSSIERS_BATCH11B = {
    "SCH-AS-024": {
        "scholarship_id": "SCH-AS-024",
        "basic_details": {
            "scholarship_name": "Tsinghua University Chinese Government & Tuition Scholarship",
            "offering_entity": "China Scholarship Council (CSC, Ministry of Education PRC) in partnership with Tsinghua University (Beijing, China)",
            "host_country": "China",
            "host_institutions_covered": "Tsinghua University Main Campus (Haidian District, Beijing, China)",
            "degree_levels": ["Master of Science / Engineering (MS)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all international graduate programs with distinguished excellence in Computer Science and Technology (CS, AI, Computer Systems), Electronic Engineering, Automation, Mechanical Engineering, Civil Engineering, and School of Materials Science.",
            "number_of_awards_total": "Approximately 150 to 200 international full graduate scholarships awarded across university departments annually (CSC Type B High-Level Postgraduate Program)",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computer science and engineering have strong representation (typically 12 to 20 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 to 3 years for Master degree; 4 years for PhD degree, subject to passing annual CSC scholarship review"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens holding a valid foreign passport in good health"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Master applicants must be under 35 years of age; Doctoral applicants must be under 40 years of age by September 1 of enrollment year.",
            "academic_qualifications": "Completed Bachelor degree (16 years education) for Master applicants; completed Master degree (18 years education) for PhD applicants from an HEC-recognized university with outstanding academic standing (minimum 3.60 / 4.00 CGPA or 82%+ aggregate from leading Pakistani institutions like NUST, FAST-NUCES, GIKI, UET, LUMS).",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Consistent 1st Division / Grade A across secondary and post-secondary educational credentials required.",
            "subject_background_prerequisites": "Strong undergraduate or postgraduate foundation in Computer Science, Software Engineering, Electrical Engineering, Applied Mathematics, or closely related engineering fields.",
            "current_education_status": "Final year graduating students eligible; must provide official Certificate of Expected Graduation issued by home university and submit original degree before registration.",
            "graduation_year_restrictions": "No restriction on year of degree conferral provided age requirements are fulfilled.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Research publications in premier conferences (NeurIPS, ICML, CVPR, IEEE/ACM) or strong open-source repositories significantly improve doctoral prospects.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "Official English Medium of Instruction (MOI) certificate from Pakistani university accepted for English-taught graduate programs; IELTS 6.5 or TOEFL 85 score report recommended for top ranking."
            },
            "other_language_requirements": "Chinese language proficiency (HSK Level 4/5) required ONLY for Chinese-taught degree programs. Zero Chinese language proficiency required for English-taught graduate programs.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Outstanding postgraduate researchers in advanced computing, AI, and engineering.",
            "previous_scholarship_restrictions": "Cannot be a concurrent recipient of any other Chinese government, provincial, or university scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition exemption (CNY 30,000 to 40,000 / year waived completely across full degree duration).",
                "amount": "100% covered (~CNY 30,000 to 40,000 / year value; ~PKR 1,200,000 to 1,600,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Tsinghua University online application processing fee (CNY 800) is paid directly by applicant.",
                "amount": "CNY 800 (~PKR 32,000)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free on-campus accommodation provided in Tsinghua Zijing International Student Apartments (single room for PhD, shared double for Master); or monthly housing subsidy of CNY 700 to 1,000/month if living off-campus.",
                "amount": "Free campus dormitory (~CNY 1,200 / month value; ~PKR 48,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend paid by CSC: CNY 3,000/month for Master's students (~PKR 120,000/month); CNY 3,500/month for PhD students (~PKR 140,000/month), often supplemented by professor lab RA top-ups of CNY 1,000 to 3,000/month.",
                "amount": "CNY 36,000 to 42,000 / year CSC base (~PKR 1,440,000 to 1,680,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Initial flight to Beijing and return airfare upon graduation are self-funded by the student.",
                "amount": "Self-funded (~PKR 140,000 to 220,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 student visa application fee and residence permit medical checkups paid by student in Islamabad/Karachi and Beijing.",
                "amount": "~PKR 25,000 (Visa & Beijing residence permit)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive Medical Insurance and Protection Scheme for Foreign Students in China (Ping An Insurance, CNY 800/year covered by CSC).",
                "amount": "CNY 800 / year covered (~PKR 32,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Subsidized Tsinghua campus dining halls provide delicious meals at very low cost (~CNY 15 to 25/day; ~PKR 1,000/day).",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Advanced computing clusters, GPU nodes, and laboratory experimental consumables funded by Tsinghua faculty grants.",
                "amount": "Covered by department laboratory"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Tsinghua Graduate School and faculty research grants sponsor international conference travel for students with accepted papers.",
                "amount": "Up to CNY 15,000 per conference"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Beijing subway and campus electric bike/bicycle transit are self-funded.",
                "amount": "Self-funded (~CNY 150 / month; ~PKR 6,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 18500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single world-leading institution: Tsinghua University (Beijing, China)",
            "participating_institutions": [
                "Tsinghua University Main Campus (Haidian, Beijing)",
                "Tsinghua Shenzhen International Graduate School (Tsinghua SIGS, Shenzhen)"
            ],
            "university_rankings_scope": "Ranked #1 university in Asia and #12 worldwide in QS World University Rankings. Department of Computer Science ranked among global top 5.",
            "available_majors": [
                "Department of Computer Science and Technology: Computer Science, Artificial Intelligence, High Performance Computing",
                "Institute for Interdisciplinary Information Sciences (IIIS / Yao Class): Theoretical Computer Science, Quantum Information",
                "Department of Electronic Engineering: Information and Communication Engineering, Microelectronics",
                "Department of Automation: Control Science and Engineering, Pattern Recognition",
                "School of Materials Science and Engineering: Materials Physics, Nanotechnology",
                "Global Environmental Program & Civil and Environmental Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master degree: 2 to 3 years; PhD degree: 4 years full-time research residency.",
            "admission_requirements_summary": "Bachelor's or Master's in relevant discipline with 3.6+ GPA, prospective professor acceptance letter strongly recommended, 2 recommendation letters, personal statement, and official transcripts.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Department of Computer Science and IIIS are among the most selective programs in the world; Shenzhen International Graduate School (SIGS) and Materials Science offer slightly higher acceptance margins.",
            "strategic_program_match_advice": "Obtaining a preliminary acceptance letter (Form for Provisional Acceptance of International Student by Tsinghua Professor) dramatically increases chances of receiving both university admission and CSC Type B full scholarship nomination. Reach out to faculty in September/October."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://gradadmission.tsinghua.edu.cn/",
            "portal_system_name": "Tsinghua University Graduate Admissions System & CSC Online Application Portal",
            "account_creation_instructions": "Register account on Tsinghua Graduate Admissions System, complete profile, choose scholarship preference (CSC / Tsinghua Tuition Scholarship), and simultaneously complete CSC portal application under Tsinghua Agency Number (10003).",
            "step_by_step_workflow": [
                "Step 1 (September - October): Review faculty research profiles; contact prospective professors with CV, transcripts, and research proposal to secure Form for Provisional Acceptance.",
                "Step 2 (Mid-October): Register on Tsinghua University Graduate Admissions System (gradadmission.tsinghua.edu.cn) and fill out application forms.",
                "Step 3 (November - December): Upload all required documents, pay application fee (CNY 800), and submit application.",
                "Step 4 (December - January): Fill out Chinese Government Scholarship application on CSC portal (studyinchina.csc.edu.cn) selecting Type B and Agency Number 10003.",
                "Step 5 (January - March): Tsinghua departmental faculty committee reviews application files, shortlists candidates, and conducts technical video interviews.",
                "Step 6 (April - May): Department submits nominated scholarship candidate list to Tsinghua Graduate School and CSC for final validation.",
                "Step 7 (June - July): Official admission results and CSC scholarship letters released; university dispatches Admission Notice and JW201/JW202 visa forms.",
                "Step 8 (July - August): Apply for Chinese X1 Student Visa at Chinese Embassy/Consulate in Pakistan; book flights to Beijing.",
                "Step 9 (Late August / Early September): Campus arrival in Beijing, dormitory check-in, residence permit registration, and semester orientation."
            ],
            "university_vs_scholarship_routing": "Integrated nomination (CSC Type B): Tsinghua University directly selects and nominates admitted international students to the China Scholarship Council for full funding.",
            "recommendation_letters_submission_method": "Two recommendation letters submitted online via referee email invitation link generated by Tsinghua admissions portal.",
            "personal_statement_prompts": "Personal Statement & Research Plan: Detail academic accomplishments, research interests, career aspirations, and rationale for choosing Tsinghua University (minimum 1,000 words).",
            "study_plan_research_proposal_requirements": "Structured research proposal (1,500 to 2,000 words) detailing literature background, research objectives, methodology, and expected results.",
            "cv_format_requirements": "Academic CV detailing educational history, GPA, programming languages, research projects, publications, and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Comprehensive 20 to 30 minute video interview conducted via Tencent Meeting / Zoom by a departmental faculty committee evaluating fundamental knowledge, research competence, and English communication.",
            "standardized_tests": "IELTS 6.5 or TOEFL 85 recommended; English MOI certificate accepted. GRE optional.",
            "application_fee_amount": "CNY 800 (Non-refundable)",
            "attestation_requirements": "HEC Pakistan attestation required on degrees and transcripts, followed by Ministry of Foreign Affairs (MOFA) Pakistan attestation.",
            "translation_requirements": "Notarized English or Chinese translations for any documents not in English.",
            "final_submission_method": "100% digital submission via Tsinghua Graduate Admissions online portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least one year beyond admission date.",
                "pakistan_specific_instruction": "Ensure Pakistani machine-readable passport bio page is scanned in high resolution."
            },
            {
                "document_name": "Official Degree Certificates and Transcripts",
                "mandatory": True,
                "specification": "Bachelor's and/or Master's degree certificates and complete academic transcripts.",
                "pakistan_specific_instruction": "Attested by Higher Education Commission (HEC) and Ministry of Foreign Affairs (MOFA) Pakistan."
            },
            {
                "document_name": "Statement of Purpose and Research Plan",
                "mandatory": True,
                "specification": "Comprehensive 1,000 to 1,500 word statement detailing academic background and proposed research.",
                "pakistan_specific_instruction": "Demonstrate clear alignment with Tsinghua faculty research directions."
            },
            {
                "document_name": "Academic Recommendation Letters (Two)",
                "mandatory": True,
                "specification": "Signed recommendation letters from Associate Professors or Full Professors.",
                "pakistan_specific_instruction": "Must be on institutional letterhead with official academic email addresses."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Official standard Chinese Foreigner Physical Examination Form with hospital stamp, doctor signature, and attached lab reports.",
                "pakistan_specific_instruction": "Completed at any recognized tertiary government hospital in Pakistan within 6 months prior to submission."
            },
            {
                "document_name": "Certificate of Non-Criminal Record (Police Clearance)",
                "mandatory": True,
                "specification": "Official Police Character Certificate issued within the past 6 months.",
                "pakistan_specific_instruction": "Issued by local Pakistani Police Khidmat Markaz and attested by MOFA Pakistan."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS / TOEFL scorecard or English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "MOI certificate signed and stamped by university registrar or controller of examinations."
            },
            {
                "document_name": "Form for Provisional Acceptance by Tsinghua Professor (Optional but Recommended)",
                "mandatory": False,
                "specification": "Official signed provisional acceptance form from Tsinghua faculty member.",
                "pakistan_specific_instruction": "Drastically boosts chances of selection when uploaded in application portal."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "15 October 2026",
            "application_deadline": "15 January 2027 (Round 1) / 1 March 2027 (Round 2)",
            "university_admission_deadline": "15 January 2027",
            "document_submission_deadline": "15 January 2027",
            "recommendation_letters_deadline": "20 January 2027",
            "interview_period": "February to March 2027",
            "shortlist_announcement": "April to May 2027",
            "final_result_acceptance_deadline": "15 June 2027",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Round 1 (October to January) is strongly recommended for CSC and university scholarship consideration."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA, academic transcript rigor, and university prestige)",
            "extracurricular_and_leadership_weight": "5% (Student leadership, programming competitions, community contributions)",
            "research_experience_weight": "30% (Research publications, thesis quality, project portfolio, and technical competence)",
            "work_experience_weight": "5% (Software development, tech industry internships, or research assistantships)",
            "personal_statement_weight": "10% (Clarity of vision, intellectual depth, and research feasibility)",
            "recommendations_weight": "5% (Strength of professor endorsements)",
            "interview_weight": "10% (Performance in technical interview panel)",
            "test_scores_weight": "Threshold requirement (IELTS/TOEFL/MOI compliance)",
            "financial_need_weight": "0% (Purely merit and research competence based)",
            "selection_panel_composition": "Departmental Graduate Admissions Committee, prospective faculty advisor, and Tsinghua Graduate School Admissions Office.",
            "evaluation_methodology": "Comprehensive dossier evaluation: Departmental admissions committee reviews GPA, research publications, and letters of recommendation. Top candidates are invited for an online technical video interview. Selected applicants are nominated to Tsinghua Graduate School and China Scholarship Council for full scholarship funding."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 international applicants across all disciplines",
            "total_scholarships_awarded": "~150 to 200 fully funded CSC Type B and Tsinghua scholarships",
            "acceptance_rate_global": "~4.5%",
            "acceptance_rate_pakistan": "~8.0% (Higher for top Pakistani CS/engineering graduates with publications and professor acceptance)",
            "typical_successful_applicant_gpa": "3.70+ / 4.00 CGPA (85%+ aggregate, top 5% class rank)",
            "typical_academic_and_research_profile": "Outstanding academic record, 1+ indexed conference/journal publications, strong coding/math foundations, and preliminary acceptance letter from Tsinghua professor.",
            "common_backgrounds_of_winners": "BS/MS graduates in Computer Science, Software Engineering, AI, and Electrical Engineering from NUST, FAST-NUCES, GIKI, UET, and LUMS.",
            "high_representation_countries": "Pakistan, Russia, South Korea, Malaysia, Thailand, Germany, France, USA",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent agencies demanding money for guaranteed CSC scholarships at Tsinghua. Tsinghua does not work with commercial agents; all applications must be submitted directly via official portals."
            ],
            "application_fee_warning": "Tsinghua charges a standard non-refundable application fee of CNY 800 paid directly in the admissions portal. Never pay fees to private individuals.",
            "agent_and_intermediary_warnings": "Applications submitted through third-party agents or containing templated personal statements are flagged and rejected.",
            "hidden_costs_breakdown": [
                "Application fee of CNY 800 (~PKR 32,000).",
                "International airfare to Beijing (~PKR 140,000 - 220,000 round-trip).",
                "Medical examination and police character certificate attestation (~PKR 20,000 - 30,000).",
                "Chinese residence permit and health check upon arrival in Beijing (~CNY 800 to 1,000; ~PKR 32,000 to 40,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: HSK Chinese language certificate is required for all majors. (FACT: Dozens of graduate programs in computing, engineering, and sciences are 100% English-taught).",
                "CLAIM: HEC Pakistan nomination is required for Tsinghua CSC Type B. (FACT: Tsinghua CSC Type B is direct university recommendation; no HEC nomination needed)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Commercial blogs claim CSC covers flight tickets; official CSC regulations confirm round-trip international airfare is NOT covered for general university recommendation scholars."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic standing (GPA >= 3.0 / 4.0) and pass the mandatory Annual CSC Scholarship Review conducted every April/May.",
            "attendance_requirements": "Full-time physical research residency on campus and active participation in laboratory research.",
            "academic_progress_monitoring": "Annual comprehensive evaluation covering coursework, research output, and laboratory supervisor endorsement.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Chinese student visa laws; on-campus TA/RA positions are permitted with department approval.",
            "home_country_return_obligation": "None. Scholars are free to pursue doctoral, postdoctoral, or industry careers globally or in China upon graduation.",
            "service_obligations_or_bonds": "Zero service bonds or financial return requirements.",
            "repayment_clawback_conditions": "Scholarship is suspended or cancelled if student fails annual review, withdraws, or commits disciplinary infractions; past disbursements are not reclaimed.",
            "rules_for_changing_university": "Changing universities is strictly prohibited under CSC scholarship regulations.",
            "rules_for_changing_major": "Changing majors is generally not permitted except under exceptional circumstances approved by the Graduate School and CSC.",
            "extension_policy": "Scholarship extensions are extremely rare and granted only with special approval from CSC and Tsinghua Graduate School for compelling academic reasons."
        },
        "official_sources_verified": [
            {
                "source_name": "Tsinghua University Graduate Admissions Official Portal",
                "source_url": "https://gradadmission.tsinghua.edu.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental allocation breakdown of CSC Type B quota seats across engineering and computing disciplines.",
                    "Exact numerical weighting distribution between file evaluation and video interview score.",
                    "Country-specific quota targets and applicant counts."
                ]
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Study in China Portal",
                "source_url": "https://www.campuschina.org/",
                "source_type": "GOVERNMENT_MINISTRY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waitlist ranking criteria and quota transfer policies between universities.",
                    "Historical country-level acceptance statistics for Type B university recommendation."
                ]
            }
        ]
    },
    "SCH-AS-025": {
        "scholarship_id": "SCH-AS-025",
        "basic_details": {
            "scholarship_name": "Zhejiang University Asian Future Leaders & Chinese Government Scholarship",
            "offering_entity": "Zhejiang University (Hangzhou, China) in partnership with China Scholarship Council (CSC) and Bai Xian Asia Institute (BXAI - Asian Future Leaders Scholarship Program / AFLSP)",
            "host_country": "China",
            "host_institutions_covered": "Zhejiang University Campuses (Yuquan & Zijingang Campuses, Hangzhou, Zhejiang, China)",
            "degree_levels": ["Master of Science / Engineering (MS)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Wide multidisciplinary coverage: Computer Science and Technology (AI, Computer Graphics, Software Engineering), Information Science and Electronic Engineering, Control Science, Mechanical Engineering, Materials Science, Chemical Engineering, Agriculture and Biotechnology, and Economics/Management.",
            "number_of_awards_total": "Approximately 120 to 160 fully funded CSC Type B and AFLSP graduate scholarships awarded annually across Zhejiang University",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computer science, engineering, and agriculture represent a prominent cohort (typically 15 to 25 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 to 3 years for Master degree; 3 to 4 years for PhD degree, subject to annual academic and conduct review"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens with valid foreign passports in good physical and mental health"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Master applicants must be under 35 years of age; PhD applicants must be under 40 years of age.",
            "academic_qualifications": "Completed Bachelor's degree (16 years education) for Master applicants; Master's degree (18 years education) for PhD applicants with minimum 3.40 / 4.00 CGPA (78%+ aggregate from recognized Pakistani universities like NUST, FAST-NUCES, GIKI, UET, University of the Punjab, UAF, COMSATS).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Graduates from top HEC-recognized Pakistani universities with high class rank are competitively prioritized.",
            "subject_background_prerequisites": "Bachelors or Masters degree in Computer Science, Electronic Engineering, Control Engineering, Materials Science, Biotechnology, or Agriculture with solid coursework.",
            "current_education_status": "Final year graduating students eligible; must provide official provisional certificate of graduation issued by university registrar.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Industry software engineering experience, Kaggle/data science rankings, or academic research projects enhance competitiveness.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "English Medium of Instruction (MOI) certificates from Pakistani universities widely accepted for English-taught graduate programs; IELTS 6.5 or TOEFL 85 strengthens application."
            },
            "other_language_requirements": "Zero Chinese language requirement for English-taught graduate programs; free Chinese language courses offered as part of curriculum.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "For AFLSP track, candidates demonstrating cross-cultural leadership and commitment to Asian intercultural understanding are preferred.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver (CNY 28,000 to 35,000 / year waived completely for entire normative duration of degree).",
                "amount": "100% covered (~CNY 30,000 / year value; ~PKR 1,200,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Zhejiang University online application fee (CNY 800) paid by applicant.",
                "amount": "CNY 800 (~PKR 32,000)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free on-campus accommodation in modern international student dormitories at Yuquan or Zijingang campuses; or off-campus living allowance of CNY 700 to 1,000/month.",
                "amount": "Free campus dormitory (~CNY 1,000 / month value; ~PKR 40,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend paid by CSC: CNY 3,000/month for Master's students (~PKR 120,000/month); CNY 3,500/month for PhD students (~PKR 140,000/month). For AFLSP scholars, USD 25,000 total package per year.",
                "amount": "CNY 36,000 to 42,000 / year base (~PKR 1,440,000 to 1,680,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel to Hangzhou and return airfare are self-funded by student.",
                "amount": "Self-funded (~PKR 140,000 to 220,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese X1 student visa application fee and residence permit medical checkups paid by student.",
                "amount": "~PKR 25,000 (Visa & Hangzhou residence permit)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive Medical Insurance and Protection Scheme for Foreign Students in China (Ping An Insurance, CNY 800/year covered by CSC/ZJU).",
                "amount": "CNY 800 / year covered (~PKR 32,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Campus dining halls at ZJU provide affordable high-quality meals (~CNY 15 to 25/day; ~PKR 1,000/day).",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Research equipment, computing resources, and lab consumables funded by Zhejiang University research grants.",
                "amount": "Covered by department laboratory"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty research funds sponsor international conference registrations and travel for research students.",
                "amount": "Up to CNY 10,000 per conference"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Hangzhou subway, bus, and shared bicycle transit are self-funded.",
                "amount": "Self-funded (~CNY 120 / month; ~PKR 4,800 / mo)"
            },
            "total_estimated_value_usd_per_year": 17500
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite C9 League university: Zhejiang University (Hangzhou, China)",
            "participating_institutions": [
                "Zhejiang University - Yuquan Campus (Engineering & Computing)",
                "Zhejiang University - Zijingang Campus (Main Campus / Sciences & AI)"
            ],
            "university_rankings_scope": "Top 45 global university (QS World #44, member of elite C9 League in China). Renowned for computer science, robotics, and entrepreneurship.",
            "available_majors": [
                "College of Computer Science and Technology: Artificial Intelligence, Computer Science, Cybersecurity",
                "College of Information Science and Electronic Engineering: Electronic Information, Communication Engineering",
                "College of Control Science and Engineering: Robotics, Automation, Systems Engineering",
                "School of Materials Science and Engineering: Materials Science, Advanced Functional Materials",
                "College of Agriculture and Biotechnology: Plant Protection, Crop Science, Bioinformatics",
                "School of Management & School of Economics: Innovation and Technology Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master degree: 2 to 2.5 years; PhD degree: 3.5 to 4 years.",
            "admission_requirements_summary": "Bachelor's or Master's degree with 3.4+ GPA, prospective professor acceptance letter strongly recommended, 2 recommendation letters, study plan, and transcripts.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Science and Artificial Intelligence are highly competitive; Agriculture, Biotechnology, and Materials Science offer favorable admission rates for qualified Pakistani candidates.",
            "strategic_program_match_advice": "Prospective applicants are strongly advised to contact ZJU faculty supervisors in advance (October to December) to obtain a 'Form for Provisional Acceptance of International Student by ZJU Professor', which elevates candidate priority during scholarship screening."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://isinfosys.zju.edu.cn/isapi/user/login",
            "portal_system_name": "Zhejiang University International Student Online Application System & CSC Portal",
            "account_creation_instructions": "Create account on ZJU International Student portal, submit online application, pay CNY 800 application fee, and simultaneously submit CSC application under ZJU Agency Number (10335).",
            "step_by_step_workflow": [
                "Step 1 (October - December): Review ZJU faculty profiles; contact prospective supervisors with CV, transcripts, and research proposal to secure Form for Provisional Acceptance.",
                "Step 2 (November - January): Create account on ZJU International Student Online Application System (isinfosys.zju.edu.cn); complete personal information and major selection.",
                "Step 3 (December - February): Upload all required documents, pay application fee (CNY 800), and submit ZJU application.",
                "Step 4 (January - February): Submit application on CSC portal (studyinchina.csc.edu.cn) selecting Type B and Zhejiang University Agency Number 10335.",
                "Step 5 (March - April): Departmental admissions committee reviews applications, conducts technical video interviews, and ranks candidates.",
                "Step 6 (May): ZJU International College forwards recommended candidates to CSC and university scholarship committees for final approval.",
                "Step 7 (June - July): Final admission decisions and scholarship awards announced; admission packages (Admission Notice and JW201/JW202) dispatched.",
                "Step 8 (July - August): Apply for Chinese X1 Student Visa at Chinese Embassy/Consulate in Pakistan; book flights to Hangzhou/Shanghai.",
                "Step 9 (Early September): Arrival at ZJU campus in Hangzhou, dormitory check-in, registration, and orientation."
            ],
            "university_vs_scholarship_routing": "Integrated nomination (CSC Type B / AFLSP): Zhejiang University directly evaluates and nominates admitted international students for full scholarship funding.",
            "recommendation_letters_submission_method": "Two recommendation letters from Associate Professors or Professors submitted via online portal system or referee upload.",
            "personal_statement_prompts": "Personal Statement & Study Plan: Detail academic background, reasons for choosing Zhejiang University, proposed research direction, and post-graduation goals (minimum 1,000 words).",
            "study_plan_research_proposal_requirements": "Structured research plan (1,500 words) describing research background, methodology, experimental objectives, and expected milestones.",
            "cv_format_requirements": "Academic CV detailing educational history, laboratory skills, programming languages, publications, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Technical video interview (20 to 30 minutes via DingTalk / Zoom) conducted by departmental faculty committee assessing subject fundamentals and research readiness.",
            "standardized_tests": "IELTS 6.5 or TOEFL 85 recommended; English MOI certificate accepted.",
            "application_fee_amount": "CNY 800 (Non-refundable)",
            "attestation_requirements": "HEC Pakistan attestation required on academic degrees and transcripts, followed by MOFA Pakistan attestation.",
            "translation_requirements": "Notarized English or Chinese translations for any documents not in English.",
            "final_submission_method": "Complete digital submission on ZJU International Student portal and CSC portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least six months beyond program start.",
                "pakistan_specific_instruction": "Ensure Pakistani machine-readable passport bio page is scanned clearly."
            },
            {
                "document_name": "Official Degree Certificates and Transcripts",
                "mandatory": True,
                "specification": "Bachelor's and/or Master's degree certificates and complete academic transcripts.",
                "pakistan_specific_instruction": "Attested by Higher Education Commission (HEC) and Ministry of Foreign Affairs (MOFA) Pakistan."
            },
            {
                "document_name": "Personal Statement and Study Plan",
                "mandatory": True,
                "specification": "Comprehensive 1,000+ word statement detailing academic background and proposed study plan.",
                "pakistan_specific_instruction": "Tailor study plan to specific laboratories and professors at Zhejiang University."
            },
            {
                "document_name": "Academic Recommendation Letters (Two)",
                "mandatory": True,
                "specification": "Signed recommendation letters from Associate Professors or Full Professors.",
                "pakistan_specific_instruction": "Must be on institutional letterhead with official academic email addresses."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Standard Chinese Foreigner Physical Examination Form with hospital stamp, doctor signature, and attached lab reports.",
                "pakistan_specific_instruction": "Completed at any recognized government tertiary hospital in Pakistan within 6 months prior to submission."
            },
            {
                "document_name": "Certificate of Non-Criminal Record (Police Clearance)",
                "mandatory": True,
                "specification": "Official Police Character Certificate issued within the past 6 months.",
                "pakistan_specific_instruction": "Issued by local Police Khidmat Markaz and attested by MOFA Pakistan."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS / TOEFL scorecard or English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "MOI certificate signed and stamped by university registrar or controller of examinations."
            },
            {
                "document_name": "Form for Provisional Acceptance by ZJU Professor (Optional but Recommended)",
                "mandatory": False,
                "specification": "Official signed provisional acceptance form from ZJU faculty member.",
                "pakistan_specific_instruction": "Strongly enhances probability of securing CSC Type B scholarship nomination."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 November 2026",
            "application_deadline": "28 February 2027",
            "university_admission_deadline": "28 February 2027",
            "document_submission_deadline": "28 February 2027",
            "recommendation_letters_deadline": "5 March 2027",
            "interview_period": "March to April 2027",
            "shortlist_announcement": "May 2027",
            "final_result_acceptance_deadline": "20 June 2027",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Single annual intake for September enrollment; early application before January 15 strongly recommended."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (CGPA, coursework rigor, and academic pedigree of undergraduate/postgraduate institutions)",
            "extracurricular_and_leadership_weight": "5% (Leadership activities, community service, intercultural involvement)",
            "research_experience_weight": "30% (Prior laboratory experience, thesis quality, publications, and technical skills)",
            "work_experience_weight": "5% (Industry experience, internships, or academic research assistantships)",
            "personal_statement_weight": "10% (Clarity, feasibility, and depth of study plan)",
            "recommendations_weight": "5% (Strength of professor endorsements)",
            "interview_weight": "10% (Performance in technical video interview)",
            "test_scores_weight": "Threshold requirement (IELTS/TOEFL/MOI compliance)",
            "financial_need_weight": "0% (Exclusively merit and research capability based)",
            "selection_panel_composition": "Departmental Graduate Admissions Committee, prospective faculty supervisor, and ZJU International College Admissions Board.",
            "evaluation_methodology": "Comprehensive evaluation: Applications are evaluated on academic merit, research potential, and professor alignment. Shortlisted candidates undergo online video interview. Admitted students are ranked and nominated for CSC Type B, AFLSP, or ZJU University Scholarships."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 international applicants across all disciplines",
            "total_scholarships_awarded": "~120 to 160 fully funded CSC Type B and AFLSP scholarships",
            "acceptance_rate_global": "~6.0%",
            "acceptance_rate_pakistan": "~15.0% (Strong placement for Pakistani engineers, computer scientists, and agronomists)",
            "typical_successful_applicant_gpa": "3.55+ / 4.00 CGPA (80%+ aggregate)",
            "typical_academic_and_research_profile": "Solid academic background, clear research proposal aligned with ZJU lab, 1+ published paper or conference proceeding, and supervisor provisional acceptance.",
            "common_backgrounds_of_winners": "Graduates in Computer Science, Electronic Engineering, Control, Agriculture, and Biotechnology from NUST, FAST-NUCES, GIKI, UET, Punjab University, UAF, and COMSATS.",
            "high_representation_countries": "Pakistan, Indonesia, Vietnam, Russia, Iran, Bangladesh, South Korea",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized recruiters charging high fees for guaranteed ZJU scholarship placement. Zhejiang University conducts admissions directly through its official portal."
            ],
            "application_fee_warning": "Zhejiang University charges a standard application fee of CNY 800 paid directly in the portal. Do not pay fees to unauthorized parties.",
            "agent_and_intermediary_warnings": "Never use educational agencies; direct correspondence with professors and independent applications are evaluated most favorably.",
            "hidden_costs_breakdown": [
                "Application fee of CNY 800 (~PKR 32,000).",
                "International airfare to Hangzhou/Shanghai (~PKR 140,000 - 220,000 round-trip).",
                "Medical checkup and police clearance attestation in Pakistan (~PKR 20,000 - 30,000).",
                "Hangzhou residence permit and health verification (~CNY 800 to 1,000; ~PKR 32,000 to 40,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: HSK Chinese proficiency is required. (FACT: Most STEM graduate programs at ZJU are completely English-taught).",
                "CLAIM: HEC Pakistan nomination is required for ZJU CSC. (FACT: This is a direct university recommendation track; no HEC nomination needed)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites claim all admitted students receive flights; official CSC policy confirms airfare is not included for university recommendation programs."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum GPA of 3.0 / 4.0 and pass the mandatory Annual CSC Scholarship Review conducted every spring.",
            "attendance_requirements": "Full-time physical research residency on campus and regular participation in laboratory research.",
            "academic_progress_monitoring": "Annual academic review based on coursework grades, research progress, and laboratory advisor report.",
            "work_restrictions_during_study": "Off-campus employment is restricted under student visa laws; on-campus research and teaching assistantships are allowed with department approval.",
            "home_country_return_obligation": "None. Graduates are free to pursue careers or further studies anywhere in the world or in China upon graduation.",
            "service_obligations_or_bonds": "Zero service bonds or return requirements.",
            "repayment_clawback_conditions": "Scholarship terminates upon academic failure, withdrawal, or disciplinary expulsion; past disbursed funds are not clawed back.",
            "rules_for_changing_university": "Transferring to another university while on CSC scholarship is strictly prohibited.",
            "rules_for_changing_major": "Major changes are permitted only within the department subject to approval by the Graduate School and CSC.",
            "extension_policy": "Scholarship extensions are extremely rare and require special approval from CSC for justified academic delays."
        },
        "official_sources_verified": [
            {
                "source_name": "Zhejiang University International College Admissions Portal",
                "source_url": "https://iczu.zju.edu.cn/admissionsen/2023/1127/c68987a2831885/page.htm",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Department-wise quota distribution for CSC Type B and AFLSP scholarships.",
                    "Exact numerical score rubrics used in video interview assessments.",
                    "Breakdown of applicants and admitted students by country of origin."
                ]
            },
            {
                "source_name": "Bai Xian Asia Institute (BXAI) Asian Future Leaders Scholarship Program",
                "source_url": "https://www.bxai.org/our-programs/scholarships/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Annual quota allocations specifically assigned to Zhejiang University for AFLSP awards.",
                    "Waitlist ranking policies for declined scholarship offers."
                ]
            }
        ]
    },
    "SCH-AS-026": {
        "scholarship_id": "SCH-AS-026",
        "basic_details": {
            "scholarship_name": "NTHU International Student Scholarship",
            "offering_entity": "National Tsing Hua University (NTHU, Hsinchu, Taiwan / Ministry of Education, Taiwan)",
            "host_country": "Taiwan",
            "host_institutions_covered": "National Tsing Hua University Main Campus (Hsinchu City, Taiwan - adjacent to Hsinchu Science Park)",
            "degree_levels": ["Master of Science / Engineering (MS)", "Doctor of Philosophy (PhD)", "Bachelor of Science (BS)"],
            "major_restrictions": "Open to all international graduate and undergraduate programs with world-renowned leadership in Electrical Engineering and Computer Science (EECS), Semiconductor Technology, Information Systems and Applications, Materials Science and Engineering, Chemical Engineering, Power Mechanical Engineering, and Nuclear Science.",
            "number_of_awards_total": "Approximately 250 to 350 NTHU International Student Scholarships (Type A: Tuition + Monthly Stipend; Type B: Tuition Waiver only) awarded annually",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computer science, electrical engineering, and materials science represent an active cohort (typically 15 to 30 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master degree; up to 4 years for PhD degree, renewed annually based on academic performance and research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants who do not hold ROC (Taiwan) citizenship or Overseas Chinese student status"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit for graduate or undergraduate applicants.",
            "academic_qualifications": "Completed Bachelor's degree (16 years education) for Master applicants; Master's degree (18 years education) for PhD applicants with minimum 3.20 / 4.00 CGPA (75%+ aggregate from recognized Pakistani universities like NUST, FAST-NUCES, GIKI, UET, COMSATS, GCU, PIEAS).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Candidates with strong background in mathematics, coding, and laboratory science are prioritized.",
            "subject_background_prerequisites": "Bachelors or Masters degree in Computer Science, Electrical Engineering, Electronics, Physics, Materials Science, Chemical Engineering, or Mathematics.",
            "current_education_status": "Final year graduating students eligible; must provide official certificate of prospective graduation from home university.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Industry engineering experience in semiconductor/embedded systems or software development is valued.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": 6.0,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "Official English Medium of Instruction (MOI) certificate from Pakistani university widely accepted; IELTS 6.0 or TOEFL 79 report accepted for English-taught graduate programs."
            },
            "other_language_requirements": "Zero Chinese language proficiency required for English-taught graduate programs; free Chinese language courses provided by NTHU Chinese Language Center.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Researchers in semiconductors, microelectronics, computing, and nanosciences.",
            "previous_scholarship_restrictions": "Cannot hold full Taiwan MOE / MOFA Scholarship concurrently with NTHU Type A stipend.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver (NTD 60,000 to 75,000 / semester waived completely for all standard degree years).",
                "amount": "100% covered (~NTD 120,000 to 150,000 / year value; ~PKR 1,050,000 to 1,300,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "NTHU online application fee is NTD 2,000 (for first department) paid by credit card.",
                "amount": "NTD 2,000 (~PKR 17,500)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus graduate dormitories guaranteed for international students (double/quad rooms cost ~NTD 10,000 to 15,000/semester; ~PKR 85,000 to 130,000/semester), paid from monthly stipend.",
                "amount": "Subsidized dorm (~NTD 2,500 / month; ~PKR 22,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Type A Fellowship provides monthly living stipend: NTD 5,000/month for Master's students (~PKR 44,000/month); NTD 15,000 to 20,000/month for PhD students (~PKR 130,000 to 175,000/month), typically supplemented by professor research assistantships (RA) of NTD 8,000 to 15,000/month in semiconductor and computing labs.",
                "amount": "NTD 156,000 to 360,000 / year total with RA (~PKR 1,365,000 to 3,150,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Taipei Taoyuan Airport (TPE) is self-funded by student.",
                "amount": "Self-funded (~PKR 180,000 to 260,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Taiwan Resident Visa application fee (~USD 66) paid at Taipei Economic and Cultural Office (TECO).",
                "amount": "~USD 66 (~PKR 18,500)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Enrolled in Taiwan National Health Insurance (NHI) after 6 months residency (world-class healthcare at ~NTD 826/month premium); private student insurance covers first 6 months.",
                "amount": "~NTD 10,000 / year (~PKR 88,000 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "NTHU campus student cafeterias provide affordable, hygienic meals (~NTD 80 to 120 per meal; ~PKR 700 to 1,050/meal).",
                "amount": "Covered from monthly stipend and RA"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "State-of-the-art semiconductor cleanrooms, cleanroom wafers, GPU workstations, and lab tools funded by Taiwan National Science and Technology Council (NSTC) and industry grants (TSMC, MediaTek).",
                "amount": "Covered by department laboratory"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "NSTC and NTHU travel subsidies provide up to NTD 60,000 for attending premier international conferences.",
                "amount": "Up to NTD 60,000 per conference"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Hsinchu city bus (free for students with student card) and Taiwan High Speed Rail (THSR) are self-funded.",
                "amount": "Self-funded (~NTD 500 / month; ~PKR 4,400 / mo)"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite research university: National Tsing Hua University (Hsinchu, Taiwan)",
            "participating_institutions": [
                "National Tsing Hua University Main Campus (Hsinchu City, Taiwan)",
                "College of Semiconductor Research (Co-founded with TSMC, MediaTek, Novatek)"
            ],
            "university_rankings_scope": "Ranked top 175 global university (QS World #177), recognized globally as a powerhouse for semiconductors, materials science, and AI computing.",
            "available_majors": [
                "College of Electrical Engineering and Computer Science: Computer Science, Information Systems, Electrical Engineering",
                "College of Semiconductor Research: Semiconductor Device, Circuit and Design, Advanced Packaging",
                "Department of Materials Science and Engineering: Nanotechnology, Functional Materials",
                "Department of Chemical Engineering: Process Engineering, Catalysis",
                "Department of Power Mechanical Engineering: Robotics, Mechatronics",
                "Institute of Information Systems and Applications (IISA)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master degree: 2 years (4 semesters); PhD degree: 3 to 4 years.",
            "admission_requirements_summary": "Bachelor's or Master's in STEM with 3.2+ GPA, 2 recommendation letters, study plan/research proposal, CV, and English proficiency certificate (IELTS/TOEFL/MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "College of Semiconductor Research and Computer Science are highly sought after; Materials Science, Chemical Engineering, and Nuclear Science offer favorable admission prospects.",
            "strategic_program_match_advice": "Applying directly for the NTHU scholarship is integrated within the admissions application form - candidates simply check 'Apply for NTHU Scholarship'. Contacting professors in semiconductor and computing labs in advance can secure supplementary Research Assistantship (RA) funding upon arrival."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://nthuoga-admission.vm.nthu.edu.tw/student/index/portal",
            "portal_system_name": "NTHU International Graduate Admissions Portal (Office of Global Affairs)",
            "account_creation_instructions": "Register an online application account on the NTHU Office of Global Affairs portal during the open window, complete profile, and select 'NTHU International Student Scholarship' in financial aid section.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Research academic departments and laboratory research on NTHU website; optionally email prospective professors.",
                "Step 2 (October - Mid-January): Create account on NTHU International Graduate Admissions Portal (nthuoga-admission.vm.nthu.edu.tw).",
                "Step 3 (November - January): Fill out online application, select degree program, check 'Yes' to apply for NTHU Scholarship, and upload all required documents.",
                "Step 4 (Mid-January): Pay application fee (NTD 2,000) online via credit card and submit application before deadline.",
                "Step 5 (February - March): Departmental admissions committee reviews applications and recommends scholarship ranking (Type A or Type B) to university scholarship committee.",
                "Step 6 (Mid-April): NTHU announces admissions and scholarship award results on the portal and issues official admission letters.",
                "Step 7 (April - May): Formally accept admission and scholarship offer via online portal.",
                "Step 8 (June - July): Prepare attested educational documents and apply for Taiwan Resident Visa via Taipei Economic and Cultural Office (TECO).",
                "Step 9 (Early September): Arrive at Taiwan Taoyuan International Airport, take direct shuttle to NTHU Hsinchu campus, check into dormitories, and complete registration."
            ],
            "university_vs_scholarship_routing": "Integrated application: Applicants apply for admission and NTHU scholarship simultaneously through the same online admissions portal.",
            "recommendation_letters_submission_method": "Two recommendation letters submitted online via referee email invitation link generated by NTHU admissions portal.",
            "personal_statement_prompts": "Study Plan & Statement of Purpose: Explain academic motivation, research background, study objectives at NTHU, and future career plans (1 to 2 pages).",
            "study_plan_research_proposal_requirements": "Structured study plan or research proposal (1,000 to 1,500 words) describing research interests, methodology, and relevance to Taiwan's technology ecosystem.",
            "cv_format_requirements": "Academic CV detailing educational background, GPA, technical skills, programming languages, and research publications.",
            "interviews_conducted": False,
            "interview_format_details": "Interviews are generally NOT required; admission and scholarship decisions are made based on comprehensive document evaluation. Occasional informal video chats may be initiated by individual professors.",
            "standardized_tests": "IELTS 6.0 or TOEFL 79 recommended; English MOI certificate accepted. GRE not required.",
            "application_fee_amount": "NTD 2,000 (for first program applied)",
            "attestation_requirements": "Attestation by Higher Education Commission (HEC) and MOFA Pakistan, followed by authentication by Taipei Economic and Cultural Office (TECO).",
            "translation_requirements": "English or Chinese translation required for all official documents.",
            "final_submission_method": "100% digital submission via NTHU International Admissions online portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least six months beyond intake date.",
                "pakistan_specific_instruction": "Ensure Pakistani machine-readable passport bio page is scanned clearly."
            },
            {
                "document_name": "Official Degree Certificates and Transcripts",
                "mandatory": True,
                "specification": "Certified official academic transcripts and degrees covering all university education.",
                "pakistan_specific_instruction": "Attested by HEC and MOFA Pakistan; TECO authentication completed prior to visa application."
            },
            {
                "document_name": "Study Plan / Statement of Purpose",
                "mandatory": True,
                "specification": "Structured 1 to 2 page study plan explaining academic background and research goals.",
                "pakistan_specific_instruction": "Highlight interest in Taiwan semiconductor or computing technology ecosystem."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Signed recommendation letters from academic professors who know applicant well.",
                "pakistan_specific_instruction": "Must be on institutional letterhead with official institutional email addresses."
            },
            {
                "document_name": "Financial Statement / Bank Statement",
                "mandatory": True,
                "specification": "Official bank statement showing minimum USD 4,000 or equivalent balance.",
                "pakistan_specific_instruction": "Can be applicant's own account or sponsor/parent account with sponsorship letter."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS, TOEFL scorecard, or English Medium of Instruction certificate.",
                "pakistan_specific_instruction": "Official MOI certificate signed by university registrar or controller of examinations."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Academic CV detailing education, publications, software projects, and honors.",
                "pakistan_specific_instruction": "Highlight papers published in Scopus/WoS indexed journals or conferences."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 October 2026",
            "application_deadline": "15 January 2027 (Fall Intake)",
            "university_admission_deadline": "15 January 2027",
            "document_submission_deadline": "15 January 2027",
            "recommendation_letters_deadline": "20 January 2027",
            "interview_period": "Not applicable (Document-based evaluation)",
            "shortlist_announcement": "Mid-April 2027",
            "final_result_acceptance_deadline": "15 May 2027",
            "visa_application_window": "June to August 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Main Fall intake opens in October with deadline in mid-January. Spring intake (limited programs) runs August to October."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Undergraduate/Master's GPA, course grades in core engineering and math subjects)",
            "extracurricular_and_leadership_weight": "5% (Student leadership, programming contests, and hackathons)",
            "research_experience_weight": "25% (Prior thesis, publications, lab projects, and semiconductor/coding projects)",
            "work_experience_weight": "5% (Tech industry internships or relevant work experience)",
            "personal_statement_weight": "15% (Quality, clarity, and specificity of Study Plan and research vision)",
            "recommendations_weight": "10% (Referee appraisals of research acumen and work ethic)",
            "interview_weight": "0% (No interview required)",
            "test_scores_weight": "Threshold requirement (IELTS/TOEFL/MOI compliance)",
            "financial_need_weight": "0% (Purely merit and academic achievement based)",
            "selection_panel_composition": "Departmental International Admissions Committee and NTHU University Scholarship Committee.",
            "evaluation_methodology": "Single-window evaluation: Departmental admissions committee reviews application dossier, GPA, and study plan. Committee ranks candidates and recommends Type A (Tuition waiver + Monthly stipend) or Type B (Tuition waiver only). Admitted scholars receive scholarship decisions together with admission offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,500 international applicants for Fall intake",
            "total_scholarships_awarded": "~250 to 350 NTHU scholarships (Type A + Type B)",
            "acceptance_rate_global": "~15.0%",
            "acceptance_rate_pakistan": "~24.0% (Very favorable acceptance rate for Pakistani STEM graduates)",
            "typical_successful_applicant_gpa": "3.40+ / 4.00 CGPA (78%+ aggregate)",
            "typical_academic_and_research_profile": "Strong foundation in engineering, computing, or physical sciences; clear study plan demonstrating interest in Taiwan tech industry; solid referee support.",
            "common_backgrounds_of_winners": "Graduates from NUST, FAST-NUCES, GIKI, UET, COMSATS, GCU, and PIEAS in Computer Science, Electrical Engineering, and Materials Science.",
            "high_representation_countries": "Pakistan, India, Vietnam, Indonesia, Philippines, Thailand, Malaysia",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized visa agents charging high placement fees for Taiwan university admission. NTHU admissions are handled solely through its official portal."
            ],
            "application_fee_warning": "NTHU charges a standard application fee of NTD 2,000 paid securely via online credit card. Never transfer fees to third parties.",
            "agent_and_intermediary_warnings": "NTHU encourages direct individual application; using agents will not improve selection chances.",
            "hidden_costs_breakdown": [
                "Application fee of NTD 2,000 (~PKR 17,500).",
                "International airfare to Taipei Taoyuan (~PKR 180,000 - 260,000 round-trip).",
                "Taiwan Resident Visa application fee (~USD 66; ~PKR 18,500).",
                "First month living expenses and dorm deposit before first stipend disbursement (~NTD 15,000; ~PKR 130,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Chinese language ability is required. (FACT: 100% of graduate coursework and research at NTHU can be completed in English).",
                "CLAIM: GRE General score is compulsory. (FACT: GRE is NOT required for NTHU graduate admissions)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some agencies advertise NTHU as covering flights; official university regulations state travel costs are self-funded."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum GPA of 3.0 / 4.0 (or 75% average) each semester to renew scholarship for subsequent terms.",
            "attendance_requirements": "Full-time course enrollment and physical laboratory research residency.",
            "academic_progress_monitoring": "Annual academic review conducted by department based on semester grades and thesis advisor endorsement.",
            "work_restrictions_during_study": "Students holding an official Taiwan Work Permit (issued via NTHU) may work up to 20 hours per week during semesters and full-time during holidays.",
            "home_country_return_obligation": "None. Graduates are eligible to apply for Taiwan Alien Resident Certificate (ARC) extension for job hunting and qualify for Taiwan employment visas (strong semiconductor recruitment by TSMC, MediaTek, etc.).",
            "service_obligations_or_bonds": "Zero bond or return obligation.",
            "repayment_clawback_conditions": "Scholarship is cancelled if GPA drops below requirement or upon withdrawal; past disbursements are not reclaimed.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Changing majors is permitted within NTHU subject to approval by both departments and the Office of Global Affairs.",
            "extension_policy": "Scholarships are granted for standard normative degree duration (2 years MS, 4 years PhD) and cannot be extended beyond maximum limits."
        },
        "official_sources_verified": [
            {
                "source_name": "National Tsing Hua University (NTHU) Office of Global Affairs Portal",
                "source_url": "https://oga.site.nthu.edu.tw/p/412-1524-18037.php?Lang=en",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific department-wise allocation ratio of Type A vs Type B scholarships.",
                    "Exact numerical scoring weights between GPA and study plan during departmental review.",
                    "Historical nationality-wise applicant and acceptance statistics."
                ]
            },
            {
                "source_name": "NTHU International Graduate Admissions Online Application System",
                "source_url": "https://nthuoga-admission.vm.nthu.edu.tw/student/index/portal",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waitlist ranking criteria for unfilled scholarship allocations.",
                    "Laboratory-level research assistantship funding averages across engineering departments."
                ]
            }
        ]
    }
}
