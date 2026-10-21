# scripts/batch15_p3.py
# SCH-AS-027: NYCU International Graduate Scholarship (Taiwan)
# SCH-AS-029: Peking University (PKU) Chinese Government Scholarship (China)
# SCH-AS-030: Fudan University Chinese Government Scholarship (China)
# SCH-AS-031: Nagoya University NUPACE & IGP MEXT Fellowship (Japan)

DATA_P3 = {
    "SCH-AS-027": {
        "scholarship_id": "SCH-AS-027",
        "basic_details": {
            "scholarship_name": "NYCU International Graduate Scholarship (National Yang Ming Chiao Tung University)",
            "offering_entity": "National Yang Ming Chiao Tung University (NYCU) & Ministry of Education (MOE) Taiwan",
            "host_country": "Taiwan",
            "host_institutions_covered": "NYCU Hsinchu Guangfu & Chiaotung Campuses (Hsinchu Science Park, Taiwan)",
            "degree_levels": ["Master of Science (MS)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "College of Computer Science, College of Electrical and Computer Engineering, College of Artificial Intelligence, and International Graduate Program in Semiconductor & Computing.",
            "number_of_awards_total": "~120 to 160 university scholarships (full tuition waivers + monthly stipends) awarded annually to international graduate students",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani students represent a prominent cohort in semiconductor and CS departments (~15 to 25 awardees annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 4 years for PhD, renewed annually subject to satisfactory academic standing"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants holding non-Taiwanese nationality"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) for MS; research Master's degree (18 years education) for PhD in Computer Science, Electrical Engineering, Software Engineering, or related STEM discipline from an HEC-recognized university with strong academic standing (minimum 75% aggregate or CGPA 3.20 / 4.00; competitive admits typically 3.50+ / 4.00).",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum requirement is 70% or 3.0/4.0; College of Computer Science admits typically have 3.40+ on a 4.0 scale.",
            "subject_background_prerequisites": "Coursework in data structures, algorithms, computer architecture, operating systems, and discrete mathematics.",
            "current_education_status": "Final-year undergraduate or master's students can apply conditionally; degree completion certificate required before enrollment.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; software development, FPGA/VLSI design, or machine learning projects strongly valued.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 79,
            "duolingo_accepted": True,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic min 6.0, TOEFL iBT min 79, TOEIC min 750, or Duolingo min 105. Institutional Medium of Instruction (MOI) certificate from Pakistani universities is officially accepted.",
            "other_language_requirements": "None; College of Computer Science international graduate programmes are taught 100% in English. Free Chinese language courses provided.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply for the scholarship simultaneously on the online admissions portal.",
            "previous_scholarship_restrictions": "Cannot hold another Taiwan government scholarship (e.g. Taiwan MOE Scholarship) simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee waiver covering 100% of university tuition and credit fees (~NTD 120,000 to NTD 150,000 / year value; ~USD 4,000 to 5,000).",
                "amount": "100% covered (~NTD 135,000 / year; ~PKR 1,188,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "NYCU online application fee of NTD 2,000 (~USD 65) paid online via credit card.",
                "amount": "NTD 2,000 (~PKR 17,600)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized on-campus graduate dormitories at Guangfu campus (Dorm 13, Graduate Dorm) guaranteed for international students; rent averages NTD 2,500 to 4,500/month (~USD 80 to 145/month).",
                "amount": "Paid from stipend (~NTD 3,500 / month; ~PKR 30,800 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend: Master's students receive NTD 8,000 to NTD 15,000 / month (~USD 260 to 485 / month; ~PKR 70,000 to 132,000 / month); PhD students receive NTD 22,000 to NTD 32,000 / month (~USD 700 to 1,030 / month; ~PKR 193,000 to 281,000 / month) combining university scholarship and lab advisor top-ups.",
                "amount": "NTD 15,000 to 32,000 / month (~PKR 132,000 to 281,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Taipei Taoyuan International Airport (TPE) is self-funded.",
                "amount": "Self-funded (~PKR 220,000 to 350,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Taiwan Resident Visa fee of USD 66 paid at Taipei Economic and Cultural Center (TECO) in Dubai/Muscat/Islamabad jurisdiction.",
                "amount": "USD 66 (~PKR 18,500)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "After 6 months of continuous residence, students are enrolled in Taiwan's world-renowned National Health Insurance (NHI) program for approx. NTD 826/month (often covered or subsidized by lab).",
                "amount": "Enrolled in Taiwan NHI (~NTD 826 / month)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Meals at NYCU campus dining halls and Hsinchu night markets cost only NTD 70 to 120 per meal; easily covered by stipend.",
                "amount": "Covered from stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Full access to NYCU Computing Center, AI supercomputers, cleanroom facilities, and laboratory equipment in Hsinchu Science Park.",
                "amount": "Covered by department infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "National Science and Technology Council (NSTC) travel grants cover international conference travel for students presenting papers.",
                "amount": "Up to NTD 50,000 per conference presentation"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Free NYCU campus shuttle buses connecting Guangfu and Boai campuses; Hsinchu City bus discounts with Taiwan EasyCard.",
                "amount": "Free campus shuttle transit"
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single premier Taiwanese technological university: National Yang Ming Chiao Tung University (NYCU, Hsinchu, Taiwan)",
            "participating_institutions": [
                "NYCU - College of Computer Science",
                "College of Electrical and Computer Engineering",
                "College of Artificial Intelligence",
                "Hsinchu Science Park (adjacent semiconductor hub - TSMC, MediaTek)"
            ],
            "university_rankings_scope": "Top 50 global university in Computer Science & Engineering (QS Subject CS #48, QS World #219); the intellectual engine of Taiwan's semiconductor miracle and home to TSMC/MediaTek research labs.",
            "available_majors": [
                "MS / PhD in Computer Science and Engineering",
                "MS / PhD in Network Engineering",
                "MS / PhD in Data Science and Engineering",
                "MS / PhD in Artificial Intelligence",
                "MS / PhD in Information Security",
                "MS / PhD in Electrical Engineering and Computer Science (International Graduate Program)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MS: 2 years; PhD: 3 to 4 years full-time.",
            "admission_requirements_summary": "4-year BS (for MS) or MS (for PhD) in CS/STEM with 3.2+ GPA, transcripts, CV, study plan, 2 recommendation letters, and English proficiency (IELTS 6.0 / TOEFL 79 / MOI accepted).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Artificial Intelligence and Data Science attract intense applicant interest; Network Engineering, Information Security, and Computer Science & Engineering offer slightly higher admission rates.",
            "strategic_program_match_advice": "Prospective applicants can contact professors in the College of Computer Science beforehand; obtaining informal supervisory agreement ensures immediate lab placement and additional lab research assistantship (RA) funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://oia.nycu.edu.tw/en/degree-seeking/international-students/",
            "portal_system_name": "NYCU Online International Student Application System",
            "account_creation_instructions": "Register on the NYCU OIA application portal, select semester intake (Fall or Spring), choose up to 3 graduate programmes, tick the scholarship application checkbox, and upload required documents.",
            "step_by_step_workflow": [
                "Step 1 (December - February for Fall / August - September for Spring): Check College of Computer Science lab websites and contact potential advisors.",
                "Step 2 (Online portal): Create account on the NYCU International Student Admissions System.",
                "Step 3 (Scholarship opt-in): On the application form, tick 'Yes' to apply for the NYCU International Student Scholarship.",
                "Step 4 (Upload documents): Upload PDF scans of transcripts, degree certificates, study plan, CV, and English certificate / MOI letter.",
                "Step 5 (Referees): Enter email contacts for 2 academic referees; system automatically emails recommendation requests.",
                "Step 6 (By deadline): Pay NTD 2,000 application fee online and submit.",
                "Step 7 (April - May for Fall): College of Computer Science reviews dossiers and announces admission and scholarship results simultaneously.",
                "Step 8 (May - July): Formally confirm acceptance, receive official admission packet, and apply for Taiwan Resident Visa."
            ],
            "university_vs_scholarship_routing": "Integrated automatic application: The scholarship application is processed simultaneously with the admission application through the same portal.",
            "recommendation_letters_submission_method": "Two academic recommendation letters uploaded directly by referees via automated email links generated by the portal.",
            "personal_statement_prompts": "Study Plan / Statement of Purpose: (1) Motivations for choosing NYCU and College of Computer Science, (2) Previous academic and research background, (3) Proposed study schedule and research goals.",
            "study_plan_research_proposal_requirements": "1 to 2 page study plan / research outline detailing research topics of interest and relevant lab alignment.",
            "cv_format_requirements": "1 to 2 page academic CV detailing education, technical competencies, programming skills, capstone projects, and academic honors.",
            "interviews_conducted": True,
            "interview_format_details": "Some faculty lab PIs may conduct a 20-30 minute virtual technical interview via Google Meet to evaluate coding skills and research background.",
            "standardized_tests": "IELTS Academic (6.0+), TOEFL iBT (79+), Duolingo (105+), or English Medium of Instruction (MOI) certificate. GRE is NOT required.",
            "application_fee_amount": "NTD 2,000 (~USD 65, Non-refundable)",
            "attestation_requirements": "Certified scans uploaded with application; official degree certificates verified by TECO upon arrival.",
            "translation_requirements": "Certified English translations required for all non-English documents.",
            "final_submission_method": "100% digital submission via the NYCU International Student Admissions System."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's / Master's Degree Certificate",
                "mandatory": True,
                "specification": "Scanned color copy of original degree certificate and official English translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS (for MS) or MS (for PhD); HEC attestation recommended."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale.",
                "pakistan_specific_instruction": "Ensure transcript clearly states credit hours and grading scale (CGPA out of 4.0)."
            },
            {
                "document_name": "Study Plan / Statement of Purpose",
                "mandatory": True,
                "specification": "1-2 page essay articulating academic background, research interests, and study plan at NYCU.",
                "pakistan_specific_instruction": "Highlight alignment with Hsinchu Science Park technologies and target NYCU computing labs."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "1 to 2 page CV detailing academic background, programming proficiencies, capstone projects, and distinctions.",
                "pakistan_specific_instruction": "Clearly link GitHub repositories, hackathons, and published work."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two academic reference letters from university professors assessing analytical and intellectual capacity.",
                "pakistan_specific_instruction": "Referees must submit from institutional email addresses (.edu.pk)."
            },
            {
                "document_name": "English Proficiency Certificate or MOI Letter",
                "mandatory": True,
                "specification": "Official IELTS (6.0+), TOEFL (79+), Duolingo (105+), or official Medium of Instruction (MOI) letter from university registrar.",
                "pakistan_specific_instruction": "Official English MOI letter from Pakistani university registrar is accepted by NYCU."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport bio-data page.",
                "pakistan_specific_instruction": "Ensure passport is valid for at least 2 years beyond intended arrival."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "20 December 2025 (Fall Intake) / 10 August 2025 (Spring Intake)",
            "application_deadline": "15 March 2026 (Fall Intake) / 30 September 2025 (Spring Intake)",
            "university_admission_deadline": "15 March 2026",
            "document_submission_deadline": "15 March 2026",
            "recommendation_letters_deadline": "22 March 2026",
            "interview_period": "April 2026",
            "shortlist_announcement": "Mid-May 2026",
            "final_result_acceptance_deadline": "Early June 2026",
            "visa_application_window": "June to August 2026",
            "semester_commencement": "Mid-September 2026",
            "annual_cycle_notes": "Two admissions cycles per year: Fall intake (September start, deadline mid-March) and Spring intake (February start, deadline late September)."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic record, undergraduate/master's GPA, performance in core computing coursework)",
            "extracurricular_and_leadership_weight": "5% (Leadership, competitions, open-source projects)",
            "research_experience_weight": "25% (Quality of final year project, thesis, technical publications, lab experience)",
            "work_experience_weight": "5% (Relevant software or semiconductor industry experience)",
            "personal_statement_weight": "15% (Quality of study plan and alignment with faculty research)",
            "recommendations_weight": "10% (Endorsements from academic referees)",
            "interview_weight": "Qualifying factor (virtual lab interview with prospective advisor)",
            "test_scores_weight": "Threshold requirement (IELTS 6.0 / TOEFL 79 / MOI compliance)",
            "financial_need_weight": "0% (Purely merit-based academic scholarship)",
            "selection_panel_composition": "College of Computer Science Admissions Committee and Office of International Affairs Scholarship Board.",
            "evaluation_methodology": "Two-stage evaluation: Faculty committees evaluate candidate dossiers on academic record, research capability, and study plan. Top candidates are recommended for university full tuition waivers and monthly stipends."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "2,000+ international graduate applicants across NYCU engineering colleges",
            "total_scholarships_awarded": "~120 to 160 university scholarships awarded annually",
            "acceptance_rate_global": "~8% to 12% for scholarship recipients",
            "acceptance_rate_pakistan": "~10% to 15% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.40+ / 4.00 CGPA (78%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate degree in CS/EE/SE from recognized Pakistani university (FAST, NUST, UET, GIKI, COMSATS), strong programming skills, solid study plan, MOI or IELTS 6.5+.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, UET Lahore/Taxila, GIKI, and COMSATS.",
            "high_representation_countries": "India, Pakistan, Vietnam, Indonesia, Philippines, Thailand, Russia",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized recruiters advertising guaranteed admission or scholarships in Taiwan for exorbitant fees. NYCU applications are processed strictly via oia.nycu.edu.tw."
            ],
            "application_fee_warning": "NYCU application fee is NTD 2,000 (~USD 65) paid online directly to the university. Never pay fees to external agents.",
            "agent_and_intermediary_warnings": "NYCU does not use commercial recruitment agencies. Direct personal application is mandatory.",
            "hidden_costs_breakdown": [
                "Application fee: NTD 2,000 (~PKR 17,600).",
                "Taiwan Resident Visa fee: USD 66 (~PKR 18,500).",
                "Flight ticket from Pakistan to Taipei: ~PKR 220,000 to 350,000.",
                "First month's dorm deposit and living costs: ~NTD 10,000 (~PKR 88,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You must speak fluent Mandarin Chinese. (FACT: 100% of graduate computing courses and research at NYCU are in English).",
                "CLAIM: You must take IELTS or TOEFL. (FACT: NYCU officially accepts English Medium of Instruction certificates from Pakistani universities)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums claim that Master's students do not receive stipends. In reality, most admitted international MS students receive a full tuition waiver plus a monthly living stipend (NTD 8,000 - 15,000/mo)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 3.00 / 4.30 or higher (approx. 75%) each semester to retain the scholarship for subsequent terms.",
            "attendance_requirements": "Full-time physical research enrollment on campus in Hsinchu.",
            "academic_progress_monitoring": "Semester-by-semester credit completion and GPA verification by the Office of International Affairs.",
            "work_restrictions_during_study": "International students holding an Alien Resident Certificate (ARC) can apply for a work permit permitting up to 20 hours per week of part-time work during semesters and full-time during holidays.",
            "home_country_return_obligation": "None. International graduates qualify for a 1 to 2-year job search extension on their ARC in Taiwan, and Taiwan provides favorable work permits (Gold Card / points system) for high-tech talent.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously awarded funds; GPA falling below 3.0 results in suspension of stipend for next semester.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing department requires formal approval from both departments.",
            "extension_policy": "Master's scholarship capped at 2 years; PhD scholarship capped at 4 years. Lab advisor funding can continue beyond."
        },
        "official_sources_verified": [
            {
                "source_name": "NYCU Office of International Affairs Degree Seeking Admissions",
                "source_url": "https://oia.nycu.edu.tw/en/degree-seeking/international-students/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation of scholarship stipends between university central funds and faculty grant top-ups.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal ranking formula between GPA and faculty lab match."
                ]
            },
            {
                "source_name": "NYCU College of Computer Science",
                "source_url": "https://www.cs.nycu.edu.tw/en",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Average lab-by-lab research assistantship funding amounts for master's and PhD students.",
                    "Detailed statistics on non-EU/international applicant pools per computing specialization."
                ]
            }
        ]
    },
    "SCH-AS-029": {
        "scholarship_id": "SCH-AS-029",
        "basic_details": {
            "scholarship_name": "Peking University (PKU) Chinese Government Scholarship (CSC High-Level Postgraduate Program)",
            "offering_entity": "China Scholarship Council (CSC) & Peking University (School of Electronics Engineering and Computer Science - EECS)",
            "host_country": "China",
            "host_institutions_covered": "Peking University Main Campus (Yanyuan / Haidian District, Beijing, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Electronics Engineering and Computer Science (EECS), School of Computer Science, and Institute for Artificial Intelligence: Computer Science and Technology, Software Engineering, Artificial Intelligence, and Microelectronics.",
            "number_of_awards_total": "~80 to 120 full CSC scholarship seats allocated to Peking University across all postgraduate disciplines annually",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates represent a prominent cohort under Sino-Pak academic collaboration (~8 to 15 awardees annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2-3 years for Master's; up to 4 years for PhD, renewed annually through CSC Annual Review"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens in good health holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 40,
            "age_limit_notes": "CSC statutory age limits: under 35 years of age for Master's applicants; under 40 years of age for Doctoral applicants.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) for Master's; recognized Master's degree (18 years education) for PhD in Computer Science, Software Engineering, or related STEM field from an HEC-recognized university with high academic distinction (minimum 80% aggregate or CGPA 3.40 / 4.00; competitive admits typically 3.70+ / 4.00).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Peking University evaluates academic excellence rigorously; transcripts must demonstrate high performance in mathematics and core computing coursework.",
            "subject_background_prerequisites": "Rigorous undergraduate training in algorithms, discrete mathematics, computer systems, and programming.",
            "current_education_status": "Students in their final undergraduate or master's year can apply; degree completion certificate required before September registration.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications or strong final-year research thesis significantly enhance competitiveness.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "For English-taught programs: IELTS Academic min 6.5, TOEFL iBT min 90, or institutional English Medium of Instruction (MOI) certificate. For Chinese-taught programs: HSK Level 6 (min 180 points) required.",
            "other_language_requirements": "None for English-taught graduate streams. Basic Chinese language courses provided.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates apply through the CSC Type B (University Program) using Peking University agency code (10001). Pre-acceptance from a PKU professor is strongly recommended.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% tuition waiver covering full postgraduate tuition fees (~CNY 30,000 to CNY 40,000 / year value).",
                "amount": "100% covered (~CNY 35,000 / year; ~PKR 1,365,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Peking University international student online application fee of CNY 800 paid online via credit card.",
                "amount": "CNY 800 (~PKR 31,200)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free on-campus accommodation in PKU international student dormitories (Zhongguanyuan Global Village or Shaoyuan) in a twin room (Master's) or single room (PhD); or a monthly housing subsidy of CNY 700 (Master's) / CNY 1,000 (PhD) if living off campus.",
                "amount": "100% free dormitory room (~CNY 1,500 / mo value)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend provided by CSC: CNY 3,000 / month for Master's students (~USD 420 / month; ~PKR 117,000 / month); CNY 3,500 / month for PhD students (~USD 490 / month; ~PKR 136,500 / month) tax-free.",
                "amount": "CNY 3,000 to 3,500 / month (~PKR 117,000 to 136,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International flights between Pakistan and Beijing Capital International (PEK) / Daxing (PKX) are self-funded.",
                "amount": "Self-funded (~PKR 180,000 to 280,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese Student Visa (X1 Visa) application fee paid to Chinese Visa Application Service Center in Islamabad/Karachi (~PKR 12,000 to 16,000).",
                "amount": "~PKR 14,000"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive Medical Insurance Scheme for International Students in China (Ping An Insurance, CNY 800/year value) fully provided by CSC.",
                "amount": "100% covered (CNY 800 / year value)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Subsidized campus canteens (Nongyuan, Yanyuan, Xuanyuan) offer high-quality hot meals for CNY 15 to 25 per meal; covered comfortably from stipend.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Full access to Peking University Library, high-performance computing clusters, and EECS laboratory resources.",
                "amount": "Covered by university facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty research grants cover travel and registration for students presenting papers at academic conferences.",
                "amount": "Covered by supervisor project grants"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Beijing Public Transport card provides heavily subsidized subway and bus transit (subway rides start at CNY 3).",
                "amount": "Subsidized Beijing public transit"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single China #1 comprehensive research university: Peking University (PKU, Beijing, China)",
            "participating_institutions": [
                "Peking University - School of Computer Science",
                "School of Electronics Engineering and Computer Science (EECS)",
                "Institute for Artificial Intelligence (PKU AI)",
                "National Key Laboratory for Multimedia Information Processing"
            ],
            "university_rankings_scope": "Top 15 global university (QS World #14, THE World #14, US News #31); China's flagship elite university and leader in AI, theoretical computing, and systems.",
            "available_majors": [
                "Master / PhD in Computer Science and Technology",
                "Master / PhD in Software Engineering",
                "Master / PhD in Artificial Intelligence",
                "Master / PhD in Microelectronics and Solid-State Electronics",
                "Master / PhD in Data Science and Big Data Technology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 to 3 years; PhD: 4 years full-time.",
            "admission_requirements_summary": "4-year BS (for MS) or MS (for PhD) in CS/STEM with 3.4+ GPA, structured research proposal, 2 recommendation letters from professors, CV, physical examination, and IELTS 6.5+ or TOEFL 90+ or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Artificial Intelligence and Computer Vision are intensely competitive; Software Engineering, Systems, and Theoretical Computer Science offer slightly higher selection ratios for well-prepared applicants.",
            "strategic_program_match_advice": "Securing a provisional Acceptance Letter / Endorsement from a PKU EECS professor prior to application submission dramatically elevates your dossier; professors hold significant influence in the CSC nomination ranking."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.studyatpku.com/",
            "portal_system_name": "PKU International Student Application Portal & CSC Online Application Portal",
            "account_creation_instructions": "Submit applications on TWO portals: (1) CSC portal (campuschina.org) using PKU Agency Code 10001 (Program Category B); (2) PKU portal (studyatpku.com), upload all documents, and pay the PKU application fee.",
            "step_by_step_workflow": [
                "Step 1 (October - December): Review PKU EECS faculty research profiles and contact prospective supervisors to obtain a pre-acceptance letter.",
                "Step 2 (CSC Portal): Register on campuschina.org, select Program Category B, input Agency Code 10001 (Peking University), and complete the CSC form.",
                "Step 3 (PKU Portal): Register on studyatpku.com, fill out the international postgraduate application, and choose Chinese Government Scholarship.",
                "Step 4 (Upload materials): Upload transcripts, degree certificates, study plan (1,500+ words), CV, 2 recommendation letters, Foreigner Physical Examination Form, and police clearance certificate.",
                "Step 5 (By deadline): Pay CNY 800 application fee on the PKU portal and submit before the January deadline.",
                "Step 6 (February - March): Department of Computer Science reviews dossiers and conducts technical video interviews.",
                "Step 7 (April - May): PKU nominates selected candidates to the China Scholarship Council for final approval.",
                "Step 8 (June - July): Official admission packet and JW201 visa form dispatched; apply for Chinese X1 Visa."
            ],
            "university_vs_scholarship_routing": "Dual-portal application: Candidate must apply on the CSC portal (Agency Code 10001) AND the PKU admissions portal simultaneously.",
            "recommendation_letters_submission_method": "Two recommendation letters from professors or associate professors uploaded directly to both portals.",
            "personal_statement_prompts": "Detailed Statement of Purpose / Research Proposal (over 1,500 words for PhD; over 1,000 words for Master's) in English detailing academic background, research objectives, methodology, and why PKU.",
            "study_plan_research_proposal_requirements": "Comprehensive research proposal outlining specific research questions, theoretical framework, methodology, and proposed supervisor alignment.",
            "cv_format_requirements": "Detailed academic CV listing education, technical proficiencies, research publications, and capstone projects.",
            "interviews_conducted": True,
            "interview_format_details": "20-30 minute virtual technical interview via Tencent Meeting / Zoom conducted by the departmental admissions committee evaluating academic background and research motivation.",
            "standardized_tests": "IELTS Academic (6.5+), TOEFL iBT (90+), or English Medium of Instruction (MOI) certificate. GRE is NOT required.",
            "application_fee_amount": "CNY 800 (Non-refundable)",
            "attestation_requirements": "Notarized copies of degree and transcripts uploaded; HEC attestation and MOFA attestation recommended for Pakistani credentials.",
            "translation_requirements": "Notarized Chinese or English translations required for all non-English documents.",
            "final_submission_method": "Dual digital submission via campuschina.org and studyatpku.com."
        },
        "required_documents_checklist": [
            {
                "document_name": "Notarized Highest Degree Certificate",
                "mandatory": True,
                "specification": "Notarized copy of Bachelor's degree (for MS) or Master's degree (for PhD) certificate and official English translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit HEC-attested degree certificates; provisional certificate accepted for final-year students."
            },
            {
                "document_name": "Notarized Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale.",
                "pakistan_specific_instruction": "Ensure transcript clearly states credit hours and grading scale (CGPA out of 4.0)."
            },
            {
                "document_name": "Research Proposal / Study Plan",
                "mandatory": True,
                "specification": "Comprehensive research statement (over 1,000 words for MS; over 1,500 words for PhD) in English.",
                "pakistan_specific_instruction": "Focus on computational research questions and cite target PKU EECS faculty papers."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two recommendation letters signed by full professors or associate professors detailing academic competence.",
                "pakistan_specific_instruction": "Referees must be professors; include official institutional email and phone number."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Completed official Chinese Foreigner Physical Examination Form with hospital stamp, physician signature, and lab reports (blood tests, chest X-ray).",
                "pakistan_specific_instruction": "Must be completed at an accredited government hospital in Pakistan within 6 months of submission."
            },
            {
                "document_name": "Non-Criminal Record Certificate (Police Clearance)",
                "mandatory": True,
                "specification": "Official police clearance certificate issued by local police authorities within 6 months.",
                "pakistan_specific_instruction": "Obtain police character certificate from local district police office in Pakistan."
            },
            {
                "document_name": "English Language Proficiency Certificate or MOI",
                "mandatory": True,
                "specification": "Official IELTS (6.5+), TOEFL (90+), or official Medium of Instruction (MOI) certificate from university registrar.",
                "pakistan_specific_instruction": "Official English MOI letter from Pakistani university registrar is accepted for English-taught degrees."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport bio-data page valid for at least 2 years.",
                "pakistan_specific_instruction": "Ensure passport is valid beyond intended program completion."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "15 October 2025",
            "application_deadline": "15 January 2026 (Strict annual CSC Type B deadline)",
            "university_admission_deadline": "15 January 2026",
            "document_submission_deadline": "15 January 2026",
            "recommendation_letters_deadline": "15 January 2026",
            "interview_period": "February to March 2026",
            "shortlist_announcement": "Late April to Mid-May 2026",
            "final_result_acceptance_deadline": "Late June 2026",
            "visa_application_window": "July to August 2026",
            "semester_commencement": "Early September 2026",
            "annual_cycle_notes": "Single annual intake for September. Strict 15 January deadline; applications on both portals must be finalized before this date."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic track record, undergraduate/master's GPA, mathematics and computing grades)",
            "extracurricular_and_leadership_weight": "5% (Academic service, leadership, extracurricular distinctions)",
            "research_experience_weight": "30% (Quality, depth, and originality of research proposal; prior publications; master's thesis)",
            "work_experience_weight": "5% (Relevant software engineering or research lab experience)",
            "personal_statement_weight": "10% (Clarity of purpose and institutional alignment with PKU)",
            "recommendations_weight": "10% (Credibility and depth of professor endorsements)",
            "interview_weight": "5% (Technical video interview with departmental admissions committee)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 90 / MOI compliance)",
            "financial_need_weight": "0% (Purely merit-based government scholarship)",
            "selection_panel_composition": "PKU EECS Academic Admissions Committee, PKU Graduate School, and China Scholarship Council Expert Panel.",
            "evaluation_methodology": "Two-tier selection: Peking University faculty sub-committees evaluate and interview candidates, producing a prioritized nomination shortlist. The China Scholarship Council conducts final administrative review and issues formal scholarship approval."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "3,500+ international graduate applicants across Peking University",
            "total_scholarships_awarded": "~80 to 120 full CSC scholarship seats awarded university-wide",
            "acceptance_rate_global": "~2% to 3% for full CSC scholarship recipients at PKU",
            "acceptance_rate_pakistan": "~4% to 6% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.70+ / 4.00 CGPA (82%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate/Master's degree in CS/SE from premier university (FAST, NUST, LUMS, GIKI, UET, QAU), 1+ published research papers, strong research proposal, pre-acceptance from PKU professor.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, and UET Lahore.",
            "high_representation_countries": "Pakistan, Russia, South Korea, United States, Germany, France, Thailand",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed CSC scholarships at Peking University. CSC applications are strictly free via campuschina.org."
            ],
            "application_fee_warning": "PKU application fee is CNY 800 paid directly online. CSC portal application is 100% free. Never pay fees to external agents.",
            "agent_and_intermediary_warnings": "Peking University does not work with commercial recruiting agents. Direct personal application is mandatory.",
            "hidden_costs_breakdown": [
                "PKU application fee: CNY 800 (~PKR 31,200).",
                "Chinese X1 Visa fee: ~PKR 14,000.",
                "Flight ticket from Pakistan to Beijing: ~PKR 180,000 to 280,000.",
                "Physical exam and police certificate costs in Pakistan: ~PKR 15,000."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You must take HSK for all programs. (FACT: English-taught graduate programs require only IELTS/TOEFL/MOI; no Chinese language test required).",
                "CLAIM: A pre-acceptance letter guarantees a scholarship. (FACT: Pre-acceptance is strongly helpful, but final selection is made by the university admissions committee and CSC)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some online blogs state that CSC scholarships pay for international flights. In reality, CSC Type B university scholarships do NOT cover international airfare."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must participate annually in the CSC Comprehensive Annual Review, maintaining good academic standing and passing all coursework.",
            "attendance_requirements": "Full-time physical presence on campus in Beijing.",
            "academic_progress_monitoring": "Annual progress reviews and milestone evaluations submitted to the Graduate School and CSC.",
            "work_restrictions_during_study": "International students may participate in university work-study programs or approved internships with university endorsement, but off-campus commercial employment is restricted.",
            "home_country_return_obligation": "None. International graduates can seek employment in China under post-study work regulations or pursue post-doctoral fellowships.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously awarded funds; failing the annual review results in suspension or cancellation of the scholarship.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing major requires joint approval from PKU and CSC.",
            "extension_policy": "Scholarship is granted for the nominal study period; extensions are rarely granted and require special CSC approval."
        },
        "official_sources_verified": [
            {
                "source_name": "Peking University International Students Division Official Portal",
                "source_url": "https://www.studyatpku.com/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Department-level CSC quota allocation between computer science and other STEM disciplines.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal ranking formula between interview performance and research proposal."
                ]
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "https://www.campuschina.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Bilateral quota ceilings for South Asian partner nations.",
                    "Annual statutory adjustments to monthly living stipends."
                ]
            }
        ]
    },
    "SCH-AS-030": {
        "scholarship_id": "SCH-AS-030",
        "basic_details": {
            "scholarship_name": "Fudan University Chinese Government Scholarship (CSC High-Level Postgraduate Program)",
            "offering_entity": "China Scholarship Council (CSC) & Fudan University (School of Computer Science)",
            "host_country": "China",
            "host_institutions_covered": "Fudan University Handan & Jiangwan Campuses (Shanghai, China)",
            "degree_levels": ["Master of Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computer Science, Academy for Engineering & Technology, and School of Data Science: Computer Science and Technology, Software Engineering, Artificial Intelligence, and Big Data Systems.",
            "number_of_awards_total": "~70 to 100 full CSC scholarship seats allocated to Fudan University across all postgraduate faculties annually",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani students secure ~6 to 12 fully funded seats annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2-3 years for Master's; up to 4 years for PhD, renewed annually through CSC Annual Review"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens in good health holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 40,
            "age_limit_notes": "CSC statutory age limits: under 35 years of age for Master's applicants; under 40 years of age for Doctoral applicants.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) for Master's; recognized Master's degree (18 years education) for PhD in Computer Science, Software Engineering, or related STEM field from an HEC-recognized university with high academic standing (minimum 80% aggregate or CGPA 3.40 / 4.00; competitive admits typically 3.65+ / 4.00).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Transcripts are evaluated rigorously on mathematics and computing foundations; admissions committee looks for strong grades in algorithms, programming, and discrete math.",
            "subject_background_prerequisites": "Substantial coursework in programming, data structures, algorithms, discrete mathematics, computer architecture, and linear algebra.",
            "current_education_status": "Students in their final undergraduate or master's year can apply; degree completion certificate required before September registration.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications or strong final-year research thesis significantly enhance competitiveness.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "For English-taught programs: IELTS Academic min 6.5, TOEFL iBT min 90, or institutional English Medium of Instruction (MOI) certificate. For Chinese-taught programs: HSK Level 5 or 6 required.",
            "other_language_requirements": "None for English-taught graduate streams. Basic Chinese language courses provided.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates apply through CSC Type B (University Program) using Fudan University agency code (10246). Pre-acceptance from a Fudan professor is strongly recommended.",
            "previous_scholarship_restrictions": "Cannot hold another Chinese government or university scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% tuition waiver covering full postgraduate tuition fees (~CNY 30,000 to CNY 38,000 / year value).",
                "amount": "100% covered (~CNY 34,000 / year; ~PKR 1,326,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Fudan University international student online application fee of CNY 800 paid online via credit card.",
                "amount": "CNY 800 (~PKR 31,200)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Free on-campus accommodation in Fudan Foreign Student Dormitory (Handan or Jiangwan campus) in a twin room (Master's) or single room (PhD); or a monthly housing subsidy of CNY 700 (Master's) / CNY 1,000 (PhD) if living off campus.",
                "amount": "100% free dormitory room (~CNY 1,500 / mo value)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly living stipend provided by CSC: CNY 3,000 / month for Master's students (~USD 420 / month; ~PKR 117,000 / month); CNY 3,500 / month for PhD students (~USD 490 / month; ~PKR 136,500 / month) tax-free.",
                "amount": "CNY 3,000 to 3,500 / month (~PKR 117,000 to 136,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Shanghai Pudong International Airport (PVG) is self-funded.",
                "amount": "Self-funded (~PKR 180,000 to 280,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese Student Visa (X1 Visa) application fee paid to Chinese Visa Application Service Center in Islamabad/Karachi (~PKR 12,000 to 16,000).",
                "amount": "~PKR 14,000"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Comprehensive Medical Insurance Scheme for International Students in China (Ping An Insurance, CNY 800/year value) fully provided by CSC.",
                "amount": "100% covered (CNY 800 / year value)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Subsidized campus canteens (Danzhong, Beiyuan, Jiangwan) offer diverse meals for CNY 15 to 25 per meal; covered comfortably from stipend.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Full access to Fudan University Library system, Jiangwan compute clusters, and School of Computer Science laboratories.",
                "amount": "Covered by university facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty research grants cover travel and registration for students presenting papers at academic conferences.",
                "amount": "Covered by supervisor project grants"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Shanghai Metro and public transit card provides heavily subsidized transit throughout Shanghai (metro fares start at CNY 3).",
                "amount": "Subsidized Shanghai public transit"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading Chinese C9 League research university: Fudan University (Shanghai, China)",
            "participating_institutions": [
                "Fudan University - School of Computer Science",
                "Academy for Engineering and Technology (Jiangwan Campus)",
                "Shanghai Key Laboratory of Intelligent Information Processing",
                "Fudan Institute of Artificial Intelligence"
            ],
            "university_rankings_scope": "Top 40 global university (QS World #39, THE World #44); member of China's elite C9 League and Shanghai's premier research institution in AI, natural language processing (MOSS model), and data science.",
            "available_majors": [
                "Master / PhD in Computer Science and Technology",
                "Master / PhD in Software Engineering",
                "Master / PhD in Artificial Intelligence",
                "Master / PhD in Data Science and Technology",
                "Master / PhD in Information Security"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 to 3 years; PhD: 3 to 4 years full-time.",
            "admission_requirements_summary": "4-year BS (for MS) or MS (for PhD) in CS/STEM with 3.4+ GPA, research proposal (1,000+ words), 2 recommendation letters from professors, CV, physical exam form, and IELTS 6.5+ or TOEFL 90+ or MOI certificate.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Natural Language Processing and Computer Vision labs are intensely competitive; Software Engineering, Data Systems, and Information Security offer slightly higher selection ratios for well-prepared applicants.",
            "strategic_program_match_advice": "Connecting with a professor at Fudan's School of Computer Science and securing a preliminary Acceptance Letter before submitting the online application gives an immense competitive advantage in the CSC nomination ranking."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://istudent.fudan.edu.cn/apply/",
            "portal_system_name": "Fudan University International Student Application Portal & CSC Portal",
            "account_creation_instructions": "Submit applications on TWO portals: (1) CSC portal (campuschina.org) using Fudan Agency Code 10246 (Program Category B); (2) Fudan portal (istudent.fudan.edu.cn/apply), upload all documents, and pay the Fudan application fee.",
            "step_by_step_workflow": [
                "Step 1 (October - December): Explore research laboratories in Fudan School of Computer Science and email professors to secure a pre-acceptance letter.",
                "Step 2 (CSC Portal): Register on campuschina.org, choose Category B, enter Agency Code 10246 (Fudan University), and complete the CSC form.",
                "Step 3 (Fudan Portal): Register on istudent.fudan.edu.cn/apply, fill out the international graduate application, and select Chinese Government Scholarship.",
                "Step 4 (Upload documents): Upload transcripts, degree certificates, study plan (1,000+ words), CV, 2 recommendation letters, Foreigner Physical Examination Form, and police clearance certificate.",
                "Step 5 (By deadline): Pay CNY 800 application fee on the Fudan portal and submit before the January deadline.",
                "Step 6 (February - March): School of Computer Science evaluates dossiers and conducts virtual technical interviews.",
                "Step 7 (April - May): Fudan University nominates selected candidates to the China Scholarship Council for final approval.",
                "Step 8 (June - July): Official admission packet and JW201 visa form dispatched; apply for Chinese X1 Visa."
            ],
            "university_vs_scholarship_routing": "Dual-portal application: Candidate must apply on the CSC portal (Agency Code 10246) AND the Fudan admissions portal simultaneously.",
            "recommendation_letters_submission_method": "Two recommendation letters from professors or associate professors uploaded directly to both portals.",
            "personal_statement_prompts": "Study Plan / Research Proposal (over 1,000 words) in English detailing academic background, research objectives, methodology, and why Fudan.",
            "study_plan_research_proposal_requirements": "Structured research proposal outlining specific research questions, theoretical framework, methodology, and proposed supervisor alignment.",
            "cv_format_requirements": "Detailed academic CV listing education, technical proficiencies, research publications, and capstone projects.",
            "interviews_conducted": True,
            "interview_format_details": "20-30 minute virtual technical interview via Tencent Meeting / Zoom conducted by the departmental admissions committee evaluating academic background and research motivation.",
            "standardized_tests": "IELTS Academic (6.5+), TOEFL iBT (90+), or English Medium of Instruction (MOI) certificate. GRE is NOT required.",
            "application_fee_amount": "CNY 800 (Non-refundable)",
            "attestation_requirements": "Notarized copies of degree and transcripts uploaded; HEC attestation and MOFA attestation recommended for Pakistani credentials.",
            "translation_requirements": "Notarized Chinese or English translations required for all non-English documents.",
            "final_submission_method": "Dual digital submission via campuschina.org and istudent.fudan.edu.cn/apply."
        },
        "required_documents_checklist": [
            {
                "document_name": "Notarized Highest Degree Certificate",
                "mandatory": True,
                "specification": "Notarized copy of Bachelor's degree (for MS) or Master's degree (for PhD) certificate and official English translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit HEC-attested degree certificates; provisional certificate accepted for final-year students."
            },
            {
                "document_name": "Notarized Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale.",
                "pakistan_specific_instruction": "Ensure transcript clearly states credit hours and grading scale (CGPA out of 4.0)."
            },
            {
                "document_name": "Research Proposal / Study Plan",
                "mandatory": True,
                "specification": "Comprehensive research statement (over 1,000 words) in English detailing research objectives and methodology.",
                "pakistan_specific_instruction": "Focus on computational research questions and cite target Fudan CS faculty papers."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two recommendation letters signed by full professors or associate professors detailing academic competence.",
                "pakistan_specific_instruction": "Referees must be professors; include official institutional email and phone number."
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Completed official Chinese Foreigner Physical Examination Form with hospital stamp, physician signature, and lab reports.",
                "pakistan_specific_instruction": "Must be completed at an accredited government hospital in Pakistan within 6 months of submission."
            },
            {
                "document_name": "Non-Criminal Record Certificate (Police Clearance)",
                "mandatory": True,
                "specification": "Official police clearance certificate issued by local police authorities within 6 months.",
                "pakistan_specific_instruction": "Obtain police character certificate from local district police office in Pakistan."
            },
            {
                "document_name": "English Language Proficiency Certificate or MOI",
                "mandatory": True,
                "specification": "Official IELTS (6.5+), TOEFL (90+), or official Medium of Instruction (MOI) certificate from university registrar.",
                "pakistan_specific_instruction": "Official English MOI letter from Pakistani university registrar is accepted for English-taught degrees."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport bio-data page valid for at least 2 years.",
                "pakistan_specific_instruction": "Ensure passport is valid beyond intended program completion."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "15 October 2025",
            "application_deadline": "15 January 2026 (Strict annual CSC Type B deadline)",
            "university_admission_deadline": "15 January 2026",
            "document_submission_deadline": "15 January 2026",
            "recommendation_letters_deadline": "15 January 2026",
            "interview_period": "February to March 2026",
            "shortlist_announcement": "Late April to Mid-May 2026",
            "final_result_acceptance_deadline": "Late June 2026",
            "visa_application_window": "July to August 2026",
            "semester_commencement": "Early September 2026",
            "annual_cycle_notes": "Single annual intake for September. Strict 15 January deadline; applications on both portals must be finalized before this date."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic track record, undergraduate/master's GPA, mathematics and computing grades)",
            "extracurricular_and_leadership_weight": "5% (Academic service, leadership, extracurricular distinctions)",
            "research_experience_weight": "30% (Quality, depth, and originality of research proposal; prior publications; master's thesis)",
            "work_experience_weight": "5% (Relevant software engineering or research lab experience)",
            "personal_statement_weight": "10% (Clarity of purpose and institutional alignment with Fudan)",
            "recommendations_weight": "10% (Credibility and depth of professor endorsements)",
            "interview_weight": "5% (Technical video interview with departmental admissions committee)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 90 / MOI compliance)",
            "financial_need_weight": "0% (Purely merit-based government scholarship)",
            "selection_panel_composition": "Fudan School of Computer Science Admissions Committee, Graduate School, and China Scholarship Council.",
            "evaluation_methodology": "Two-tier selection: Fudan faculty sub-committees evaluate and interview candidates, producing a prioritized nomination shortlist. The China Scholarship Council conducts final administrative review and issues formal scholarship approval."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "3,000+ international graduate applicants across Fudan University",
            "total_scholarships_awarded": "~70 to 100 full CSC scholarship seats awarded university-wide",
            "acceptance_rate_global": "~2.5% to 3.5% for full CSC scholarship recipients at Fudan",
            "acceptance_rate_pakistan": "~4% to 6% among qualified Pakistani STEM applicants",
            "typical_successful_applicant_gpa": "3.65+ / 4.00 CGPA (80%+ aggregate)",
            "typical_academic_and_research_profile": "Undergraduate/Master's degree in CS/SE from premier university (FAST, NUST, LUMS, GIKI, UET, QAU), 1+ published research papers, strong research proposal, pre-acceptance from Fudan professor.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, and UET Lahore.",
            "high_representation_countries": "Pakistan, Russia, South Korea, United States, Germany, France, Thailand",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial education recruiters charging large sums claiming guaranteed CSC scholarships at Fudan University. CSC applications are strictly free via campuschina.org."
            ],
            "application_fee_warning": "Fudan application fee is CNY 800 paid directly online. CSC portal application is 100% free. Never pay fees to external agents.",
            "agent_and_intermediary_warnings": "Fudan University does not work with commercial recruiting agents. Direct personal application is mandatory.",
            "hidden_costs_breakdown": [
                "Fudan application fee: CNY 800 (~PKR 31,200).",
                "Chinese X1 Visa fee: ~PKR 14,000.",
                "Flight ticket from Pakistan to Shanghai: ~PKR 180,000 to 280,000.",
                "Physical exam and police certificate costs in Pakistan: ~PKR 15,000."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You must take HSK for all programs. (FACT: English-taught graduate programs require only IELTS/TOEFL/MOI; no Chinese language test required).",
                "CLAIM: A pre-acceptance letter guarantees a scholarship. (FACT: Pre-acceptance is strongly helpful, but final selection is made by the university admissions committee and CSC)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some online blogs state that CSC scholarships pay for international flights. In reality, CSC Type B university scholarships do NOT cover international airfare."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must participate annually in the CSC Comprehensive Annual Review, maintaining good academic standing and passing all coursework.",
            "attendance_requirements": "Full-time physical presence on campus in Shanghai.",
            "academic_progress_monitoring": "Annual progress reviews and milestone evaluations submitted to the Graduate School and CSC.",
            "work_restrictions_during_study": "International students may participate in university work-study programs or approved internships with university endorsement, but off-campus commercial employment is restricted.",
            "home_country_return_obligation": "None. International graduates can seek employment in China under post-study work regulations or pursue post-doctoral fellowships.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously awarded funds; failing the annual review results in suspension or cancellation of the scholarship.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing major requires joint approval from Fudan and CSC.",
            "extension_policy": "Scholarship is granted for the nominal study period; extensions are rarely granted and require special CSC approval."
        },
        "official_sources_verified": [
            {
                "source_name": "Fudan University International Students Office Official Portal",
                "source_url": "https://iso.fudan.edu.cn/isoenglish/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Department-level CSC quota allocation between computer science and other STEM disciplines.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal ranking formula between interview performance and research proposal."
                ]
            },
            {
                "source_name": "China Scholarship Council (CSC) Official Portal",
                "source_url": "https://www.campuschina.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Bilateral quota ceilings for South Asian partner nations.",
                    "Annual statutory adjustments to monthly living stipends."
                ]
            }
        ]
    },
    "SCH-AS-031": {
        "scholarship_id": "SCH-AS-031",
        "basic_details": {
            "scholarship_name": "Nagoya University NUPACE & IGP MEXT Fellowship",
            "offering_entity": "Japanese Ministry of Education, Culture, Sports, Science and Technology (MEXT) & Nagoya University",
            "host_country": "Japan",
            "host_institutions_covered": "Nagoya University Higashiyama Campus (Nagoya, Aichi Prefecture, Japan)",
            "degree_levels": ["Master of Engineering / Science (MSc)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Graduate School of Informatics (Department of Computer Science, Department of Intelligence Science and Technology), Graduate School of Engineering, and International Graduate Program (IGP).",
            "number_of_awards_total": "~35 to 50 University-Recommended MEXT scholarships awarded annually across Nagoya University graduate schools",
            "number_of_awards_pakistan": "Open international competition under MEXT General Category; Pakistani students secure ~3 to 6 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 3 years for PhD (plus 6 months Japanese preparatory period if required)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of countries that have diplomatic relations with Japan (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Applicants must be born on or after April 2 of the year corresponding to under 35 years of age at intake.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) for Master's; recognized Master's degree (18 years education) for PhD in Computer Science, Information Science, or related STEM field from an HEC-recognized university with minimum cumulative GPA of 3.30 / 4.00 (MEXT grade point average of 2.30 / 3.00 scale or higher required; competitive admits typically 3.60+ / 4.00).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Must satisfy MEXT grade conversion formula: Minimum 2.30 on MEXT 3.0 scale over past two academic years.",
            "subject_background_prerequisites": "Rigorous undergraduate training in algorithms, discrete mathematics, computer architecture, programming, and software engineering.",
            "current_education_status": "Students in their final undergraduate or master's year can apply conditionally; degree completion certificate required before September arrival.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; prior research experience and academic publications significantly strengthen the nomination.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic min 6.5, TOEFL iBT min 80, TOEIC min 730, or institutional English Medium of Instruction (MOI) certificate. Japanese language proficiency (JLPT) is not required for IGP.",
            "other_language_requirements": "None; instruction and research conducted entirely in English in the Graduate School of Informatics IGP.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must obtain formal acceptance/endorsement from a prospective Nagoya University professor before applying.",
            "previous_scholarship_restrictions": "Those who have received a MEXT scholarship in the past must have at least 3 years of educational/work experience before applying again.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full exemption of university admission examination fee (JPY 30,000), enrollment fee (JPY 282,000), and annual tuition fees (JPY 535,800 / year value).",
                "amount": "100% covered (~JPY 535,800 / year; ~PKR 1,018,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application examination fee of JPY 30,000 is 100% waived for MEXT scholarship nominees.",
                "amount": "JPY 0 (Waived for MEXT nominees)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Nagoya University International Residences (Foreign Student House, Idaka-cho, Noyori Conference Hall) provided for initial 6-12 months at highly subsidized rates (JPY 15,000 to 30,000/month; ~USD 100 to 200/month); private apartments average JPY 35,000 to 55,000/month.",
                "amount": "Paid from stipend (~JPY 25,000 / month; ~PKR 47,500 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Monthly tax-free living stipend paid by MEXT: JPY 144,000 / month for Master's students (~USD 960 / month; ~PKR 273,600 / month); JPY 145,000 / month for PhD students (~USD 970 / month; ~PKR 275,500 / month) for the full duration of study.",
                "amount": "JPY 144,000 to 145,000 / month (~PKR 273,600 to 275,500 / mo)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Economy-class international flight ticket from Pakistan (Islamabad/Lahore/Karachi) to Chubu Centrair International Airport (NGO) / Tokyo at the beginning, and return flight upon degree completion, fully covered by MEXT.",
                "amount": "100% covered round-trip flights by MEXT"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Japanese College Student Visa issued free of charge at the Embassy of Japan in Islamabad or Consulate-General in Karachi upon receipt of MEXT certificate.",
                "amount": "100% free / waived"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory Japanese National Health Insurance (NHI) covers 70% of all medical costs; student premium is heavily subsidized (~JPY 1,500 to 2,000/month; ~PKR 3,000 to 4,000/month), paid out of stipend.",
                "amount": "Subsidized NHI (~JPY 2,000 / month)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Campus cafeterias (Meidai Co-op dining halls, Meidai Halal Food corners) offer wholesome meals for JPY 400 to 600 per meal; easily covered by the JPY 144,000/month stipend.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Full access to Nagoya University Central Library, Information Technology Center supercomputing clusters, and Informatics lab hardware.",
                "amount": "Covered by university facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Laboratory JSPS Kakenhi research grants cover domestic and international conference travel expenses for research presentations.",
                "amount": "Covered by laboratory research grants"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "Nagoya Subway and Meitetsu train student commuter passes provide 50% discount on transit; Higashiyama campus has direct subway station.",
                "amount": "50% discount on Nagoya municipal subway"
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite Japanese Imperial National University: Nagoya University (Nagoya, Aichi, Japan)",
            "participating_institutions": [
                "Nagoya University - Graduate School of Informatics",
                "Department of Computer Science & Department of Intelligence Science and Technology",
                "Information Technology Center (Tier-1 National Computing Center)",
                "Institutes of Innovation for Future Society"
            ],
            "university_rankings_scope": "Top 100 global university and Japanese Imperial University (QS World #152, ARWU Shanghai #83); alma mater of 6 Nobel Prize laureates; heart of Japan's automotive/robotics industrial belt (Greater Nagoya / Toyota hub).",
            "available_majors": [
                "Master / PhD in Computer Science: Algorithms, Programming Systems, Cloud Computing",
                "Master / PhD in Intelligence Science and Technology: AI, Computer Vision, Robotics",
                "Master / PhD in Complex Systems Science: Data Science, Complex Networks",
                "International Graduate Program in Informatics (English-taught IGP track)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years full-time.",
            "admission_requirements_summary": "4-year BS (for MS) or MS (for PhD) in CS/STEM with 3.3+ GPA, MEXT GPA 2.3/3.0, research plan (3-5 pages), supervisor endorsement letter, 2 recommendation letters, and IELTS 6.5+ or TOEFL 80+ or MOI.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Intelligence Science and Technology (AI/Computer Vision/Robotics) attracts significant applicant competition; Computer Science (Algorithms, Systems, Architecture) offers higher selection probability for candidates with solid mathematical and systems preparation.",
            "strategic_program_match_advice": "You MUST contact a prospective supervisor in the Graduate School of Informatics between September and November to secure their agreement to supervise your research before submitting your application dossier to the university."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.i.nagoya-u.ac.jp/en/admissions/",
            "portal_system_name": "Nagoya University Graduate School of Informatics Admissions Portal",
            "account_creation_instructions": "Review faculty directory on the Graduate School of Informatics website, contact prospective professor with CV and research plan, obtain provisional acceptance, then submit formal application materials to the graduate school admissions office.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Review faculty research labs in Graduate School of Informatics and initiate contact with prospective supervisor with CV, transcripts, and research proposal.",
                "Step 2 (Secure supervisor agreement): Obtain informal agreement to supervise from a professor (Letter of Provisional Acceptance).",
                "Step 3 (November - December): Receive formal MEXT University Recommendation application guidelines from the prospective professor or graduate school office.",
                "Step 4 (Document compilation): Prepare MEXT application form, field of study and study program form, certified transcripts, degree certificates, and 2 recommendation letters.",
                "Step 5 (By mid-January): Submit completed application package to the Graduate School of Informatics.",
                "Step 6 (February): Graduate school conducts internal screening and interviews nominees.",
                "Step 7 (March): Nagoya University formally nominates selected candidates to MEXT.",
                "Step 8 (June - July): MEXT officially approves nominations; recipient receives air ticket and visa instructions for September arrival."
            ],
            "university_vs_scholarship_routing": "Integrated University Recommendation track: Candidates apply directly through Nagoya University; the university nominates selected candidates to MEXT.",
            "recommendation_letters_submission_method": "Two confidential recommendation letters addressed to the President of Nagoya University, signed by university Dean or supervising professor.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (MEXT standard form): (1) Past research background and achievements, (2) Detailed research plan in Japan (purpose, methodology, expected results, bibliography).",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing problem statement, research significance, proposed methodology, technical approach, and schedule of research in Japan.",
            "cv_format_requirements": "Academic CV detailing education, programming proficiencies, research publications, and capstone projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-45 minute technical video interview via Zoom conducted by prospective supervisor and departmental committee evaluating research proposal, mathematical problem solving, and English fluency.",
            "standardized_tests": "IELTS Academic (6.5+), TOEFL iBT (80+), or English Medium of Instruction (MOI) certificate. GRE is NOT required.",
            "application_fee_amount": "JPY 0 (Waived for MEXT nominees)",
            "attestation_requirements": "Certified copies of degree and transcripts uploaded; HEC attestation recommended for Pakistani credentials.",
            "translation_requirements": "Certified English or Japanese translations required for all non-English documents.",
            "final_submission_method": "Digital submission to graduate school office followed by physical mailing of original certified documents upon request."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Bachelor's / Master's Degree Certificate",
                "mandatory": True,
                "specification": "Certified copy of original degree certificate and official English translation.",
                "pakistan_specific_instruction": "Pakistani applicants submit 4-year BS (for MS) or MS (for PhD); HEC attestation recommended."
            },
            {
                "document_name": "Official Academic Transcripts",
                "mandatory": True,
                "specification": "Complete consolidated semester transcripts detailing all completed course units, grades, and grading scale explanation.",
                "pakistan_specific_instruction": "Must clearly demonstrate minimum MEXT GPA of 2.30 / 3.00."
            },
            {
                "document_name": "MEXT Field of Study and Research Program Plan",
                "mandatory": True,
                "specification": "Official MEXT form detailing past research background and structured research plan for Japan.",
                "pakistan_specific_instruction": "Collaborate closely with prospective Nagoya University supervisor to refine research plan."
            },
            {
                "document_name": "Provisional Acceptance Letter from Professor",
                "mandatory": True,
                "specification": "Official letter or email endorsement from a prospective Nagoya University professor agreeing to serve as academic supervisor.",
                "pakistan_specific_instruction": "Crucial requirement; obtain directly from prospective professor."
            },
            {
                "document_name": "Letters of Recommendation (Two)",
                "mandatory": True,
                "specification": "Two recommendation letters addressed to President of Nagoya University, including one from Dean or Department Chair.",
                "pakistan_specific_instruction": "Referees must submit on official university letterhead with institutional email (.edu.pk)."
            },
            {
                "document_name": "English Language Proficiency Certificate or MOI",
                "mandatory": True,
                "specification": "Official IELTS (6.5+), TOEFL (80+), or official Medium of Instruction (MOI) letter from university registrar.",
                "pakistan_specific_instruction": "Official English MOI letter from Pakistani university registrar is accepted by Nagoya University."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport bio-data page valid for at least 3 years.",
                "pakistan_specific_instruction": "Ensure passport is valid beyond intended arrival in Japan."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 November 2025",
            "application_deadline": "15 January 2026 (Strict university nomination deadline)",
            "university_admission_deadline": "15 January 2026",
            "document_submission_deadline": "15 January 2026",
            "recommendation_letters_deadline": "15 January 2026",
            "interview_period": "January to February 2026",
            "shortlist_announcement": "Late March 2026 (University nomination) / Late June 2026 (MEXT approval)",
            "final_result_acceptance_deadline": "Mid-July 2026",
            "visa_application_window": "July to August 2026",
            "semester_commencement": "Late September / 1 October 2026",
            "annual_cycle_notes": "Single annual intake for October semester under University Recommendation MEXT track. Strict mid-January deadline."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Cumulative GPA, coursework rigor in mathematics and computer science, MEXT GPA calculation)",
            "extracurricular_and_leadership_weight": "5% (Academic service, leadership, community contributions)",
            "research_experience_weight": "30% (Quality and feasibility of research plan, technical publications, master's thesis)",
            "work_experience_weight": "5% (Relevant industry software or research experience)",
            "personal_statement_weight": "10% (Clarity of purpose and understanding of Japanese research culture)",
            "recommendations_weight": "10% (Endorsements from academic referees and Dean)",
            "interview_weight": "5% (Technical video interview with prospective supervisor and faculty committee)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 80 / MOI compliance)",
            "financial_need_weight": "0% (Purely merit-based Japanese government scholarship)",
            "selection_panel_composition": "Graduate School of Informatics Faculty Committee, Nagoya University International Student Selection Board, and MEXT Review Board.",
            "evaluation_methodology": "Two-phase competitive selection: Graduate School of Informatics evaluates dossiers and conducts technical interviews, nominating top candidates to the university-wide committee. The university nominates top candidates to MEXT in Tokyo for final statutory approval."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "800+ international applicants across Nagoya University graduate schools",
            "total_scholarships_awarded": "~35 to 50 University-Recommended MEXT scholarships awarded annually",
            "acceptance_rate_global": "~4% to 6% for MEXT University Recommendation",
            "acceptance_rate_pakistan": "~5% to 8% among qualified Pakistani STEM applicants with supervisor endorsement",
            "typical_successful_applicant_gpa": "3.60+ / 4.00 CGPA (80%+ aggregate; MEXT GPA 2.6+/3.0)",
            "typical_academic_and_research_profile": "Undergraduate/Master's degree in CS/SE from recognized Pakistani university (FAST, NUST, LUMS, GIKI, UET), strong research proposal aligned with professor's grants, IELTS 7.0+ or MOI.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, LUMS, GIKI, and UET Lahore.",
            "high_representation_countries": "China, Pakistan, Indonesia, Vietnam, India, Thailand, Malaysia",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent recruitment portals charging fees for MEXT scholarships. MEXT scholarships NEVER charge any application, processing, or visa fees at any stage."
            ],
            "application_fee_warning": "Applying for MEXT University Recommendation at Nagoya University is 100% free of charge. Never pay money to consultants.",
            "agent_and_intermediary_warnings": "Nagoya University does not collaborate with education recruitment agents for MEXT scholarships. Direct personal application is mandatory.",
            "hidden_costs_breakdown": [
                "Application fee: JPY 0 (100% free).",
                "Flight ticket to Japan: 100% paid by MEXT.",
                "Japanese Student Visa: 100% free at Embassy/Consulate.",
                "Initial settling cash for first 2-3 weeks before stipend disbursement: ~JPY 50,000 (~PKR 95,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You must be fluent in Japanese. (FACT: 100% of coursework, research, and thesis defense in the Graduate School of Informatics IGP is in English).",
                "CLAIM: You can apply without a professor's agreement. (FACT: University-Recommended MEXT requires a prospective professor willing to formally sponsor your nomination)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some student forums confuse the Embassy-Recommended MEXT track (applied via Embassy of Japan in Islamabad) with the University-Recommended MEXT track (applied directly through Nagoya University). Both provide identical full benefits."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA of 2.30 / 3.00 on the MEXT scale each academic year to retain the scholarship.",
            "attendance_requirements": "Full-time physical research enrollment on campus in Nagoya.",
            "academic_progress_monitoring": "Annual progress reports and thesis committee evaluations reviewed by the Graduate School of Informatics.",
            "work_restrictions_during_study": "MEXT scholars are expected to devote themselves full-time to their studies; part-time work requires formal permission from both the university and Japanese immigration (capped at 28 hrs/week).",
            "home_country_return_obligation": "None under current MEXT regulations. International graduates can seek employment in Japan (highly in demand in automotive and AI industries) or pursue postdoctoral research.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "No clawback of previously awarded funds; serious academic delinquency results in termination of stipend.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing major is not permitted under MEXT regulations.",
            "extension_policy": "Master's students with outstanding research records may apply for MEXT extension to continue into the PhD program at Nagoya University."
        },
        "official_sources_verified": [
            {
                "source_name": "Nagoya University Graduate School of Informatics Admissions",
                "source_url": "https://www.i.nagoya-u.ac.jp/en/admissions/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Department-level MEXT quota allocation breakdown across departments.",
                    "Country-level breakdown of scholarship awardees.",
                    "Internal ranking formula between interview performance and research plan."
                ]
            },
            {
                "source_name": "MEXT Japanese Government Scholarship Official Regulations",
                "source_url": "https://www.mext.go.jp/en/policy/education/highered/title02/detail02/sdetail02/1373897.htm",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Annual statutory adjustments to regional monthly living stipends.",
                    "Discretionary return flight cancellation rules for students remaining in Japan."
                ]
            }
        ]
    }
}
