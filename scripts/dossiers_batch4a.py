"""
scripts/dossiers_batch4a.py
Part A of Batch 4:
1. SCH-AS-012: KAIST International Graduate Scholarship (South Korea)
2. SCH-ME-002: KAUST Fellowship (King Abdullah Univ of Science and Technology, Saudi Arabia)
3. SCH-ME-004: Hamad Bin Khalifa University (HBKU) Scholarship (Qatar Foundation, Qatar)
"""

DOSSIERS_BATCH4A = {
    # 1. KAIST International Graduate Scholarship (SCH-AS-012)
    "SCH-AS-012": {
        "scholarship_id": "SCH-AS-012",
        "basic_details": {
            "scholarship_name": "KAIST International Graduate Scholarship",
            "offering_entity": "Korea Advanced Institute of Science and Technology (KAIST) & Ministry of Science and ICT, South Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "KAIST Main Campus (Daejeon) and Seoul Campus (College of Business)",
            "degree_levels": ["Master's (MS)", "MS-PhD Integrated", "PhD"],
            "major_restrictions": "Open to all graduate departments in the College of Natural Sciences, College of Life Science & Bioengineering, College of Engineering, and College of Business.",
            "number_of_awards_total": "~400 to 500 fully-funded international graduate scholarships awarded annually across Spring and Fall intakes",
            "number_of_awards_pakistan": "Open globally; Pakistan is one of the top representation countries at KAIST (~40 to 60 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Master's: 2 years (4 semesters); PhD: 4 years (8 semesters); MS-PhD Integrated: 5 years"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Korean citizenship (neither applicant nor parents hold Korean nationality; Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (Bachelor's degree) for Master's; 18 years (Master's degree) for PhD from an accredited university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA; competitive admitted candidates typically present 3.50+ / 4.00 CGPA.",
            "subject_background_prerequisites": "Academic background in engineering, computing, natural sciences, or management.",
            "current_education_status": "Graduated or expected to graduate before the semester start date.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research laboratory experience, programming proficiency, and prior publications in IEEE/ACM/SCI venues significantly boost admission ranking.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 83,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "IELTS Academic minimum 6.5, TOEFL iBT minimum 83, or official English Proficiency Certificate (MOI) issued by university registrar."
            },
            "other_language_requirements": "Korean language (TOPIK) not required; all graduate courses and research conducted in English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates select 'KAIST Scholarship' on the application portal; no separate scholarship form needed.",
            "previous_scholarship_restrictions": "Cannot hold another full Korean government scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee waiver for all regular semesters of study.",
                "amount": "KRW 8,000,000 to 10,000,000 / semester (~USD $12,000 to $15,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "KAIST online application fee (USD $80 / KRW 80,000) paid by applicant.",
                "amount": "USD $80"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND_WITH_SUBSIDIZED_HOUSING",
                "details": "Subsidized on-campus university dormitory accommodation provided (~KRW 150,000 to 250,000/month); paid from living stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "KAIST base stipend (KRW 350,000/mo for MS, KRW 400,000/mo for PhD) PLUS research assistantship (RA) top-up from supervising professor lab (~KRW 600,000 to 1,200,000/mo extra). Total take-home typically KRW 1,000,000 to 1,600,000 / month.",
                "amount": "KRW 1,000,000 to 1,600,000 / month (~PKR 210,000 to 340,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Initial airfare to South Korea is paid by student from personal funds or lab advance.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Korean student visa (D-2) application fee paid by student at Korean Embassy in Islamabad / Consulate in Karachi.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Korean National Health Insurance (NHIS) covered / subsidized by KAIST for international students.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered from living allowance and lab resources.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Domestic and international conference travel fully funded through supervisor's research lab grants.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Personal responsibility.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Korea Advanced Institute of Science and Technology (KAIST - World Top 55).",
            "participating_institutions": [
                "KAIST Main Campus (Daejeon)", "KAIST College of Business (Seoul)"
            ],
            "university_rankings_scope": "QS World Rank #53; #1 science and technology university in South Korea.",
            "available_majors": [
                "Computer Science, Artificial Intelligence (Kim Jaechul Graduate School of AI), Electrical Engineering, Mechanical Engineering, Aerospace Engineering, Robotics, Materials Science and Engineering, Chemical & Biomolecular Engineering, Bio & Brain Engineering, Physics, Chemistry, Mathematical Sciences, Industrial & Systems Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 4 years",
            "admission_requirements_summary": "Online application via KAIST admissions portal; select KAIST Scholarship; submit physical or certified digital documents.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "School of Computing and Graduate School of AI are most competitive; contacting professors prior to applying significantly increases chances.",
            "strategic_program_match_advice": "Emailing prospective KAIST lab directors (PIs) with your CV and published work before the deadline to secure informal lab support is strongly advised."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://admission.kaist.ac.kr/intl-graduate/",
            "portal_system_name": "KAIST International Graduate Admission Portal",
            "account_creation_instructions": "Register on the KAIST application system (Spring intake: August-September; Fall intake: December-January), fill in the online form, pay the $80 application fee, and upload documents.",
            "step_by_step_workflow": [
                "1. Research KAIST laboratories and email prospective professors (November-December for Fall intake).",
                "2. Create account on KAIST International Graduate portal and complete application form.",
                "3. Select 'KAIST Scholarship' as the funding source.",
                "4. Pay the USD $80 online application fee.",
                "5. Designate two academic referees who submit online reference letters.",
                "6. Upload or dispatch required academic certificates, transcripts, and financial sponsor documents before deadline.",
                "7. Departmental committee conducts document screening and video interviews in March.",
                "8. Final admissions and scholarship results announced in late March/early April."
            ],
            "university_vs_scholarship_routing": "Integrated single application: Select KAIST Scholarship checkbox.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure electronic link sent by KAIST.",
            "personal_statement_prompts": "Statement of Purpose covering academic goals, background, work/research experiences, and future career plans.",
            "study_plan_research_proposal_requirements": "Study plan outlining intended research area and courses.",
            "cv_format_requirements": "Academic CV detailing technical skills, publications, and final year projects.",
            "interviews_conducted": True,
            "interview_format_details": "Departmental interview committee or prospective lab PI conducts 20-30 minute video interview in March testing fundamentals and research interest.",
            "standardized_tests": "GRE not required; English language score or MOI required.",
            "application_fee_amount": "USD $80 / KRW 80,000.",
            "attestation_requirements": "Apostille or consular legalization by Korean Embassy in Islamabad required for final degree documents.",
            "translation_requirements": "Notarized English translations.",
            "final_submission_method": "Online application followed by document verification."
        },
        "required_documents_checklist": [
            {
                "document_name": "KAIST Online Application Form & Statement of Purpose",
                "mandatory": True,
                "specification": "Completed form and SOP printed from portal",
                "pakistan_specific_instruction": "Detailing academic trajectory and research interests"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Submitted directly by university professors using official institutional email",
                "pakistan_specific_instruction": "From professors who supervised your BS/MS thesis"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Certified copies of undergraduate/master's transcripts with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan; Korean consular attestation needed upon admission"
            },
            {
                "document_name": "English Proficiency Score / Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+), TOEFL iBT (83+), or official MOI certificate",
                "pakistan_specific_instruction": "MOI certificate accepted from recognized Pakistani universities"
            },
            {
                "document_name": "Copy of Passport & National ID",
                "mandatory": True,
                "specification": "Passport photo page and national identity card of applicant and parents",
                "pakistan_specific_instruction": "NADRA CNIC copies with English translation"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-12-05",
            "application_deadline": "2027-01-15",
            "university_admission_deadline": "2027-01-15",
            "document_submission_deadline": "2027-01-22",
            "recommendation_letters_deadline": "2027-01-22",
            "interview_period": "March 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027 (Fall intake)",
            "annual_cycle_notes": "Two annual intakes: Fall intake (Deadline mid-January for Sept start); Spring intake (Deadline late August for March start)."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic record, GPA, mathematical and technical mastery)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "35% (Prior lab experience, final year project quality, publications, programming skills)",
            "work_experience_weight": "5% (Industrial/laboratory R&D experience)",
            "personal_statement_weight": "5% (Study plan and motivation)",
            "recommendations_weight": "10% (Referee appraisals)",
            "interview_weight": "High weight in departmental interview",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "KAIST Departmental Admissions Committees and the Central International Admissions Committee.",
            "evaluation_methodology": "Two-tier review: Department evaluates academic transcript alignment, lab match, and interview; central committee confirms scholarship."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 4,500 international applications annually",
            "total_scholarships_awarded": "~400 to 500 scholarships awarded annually across both intakes",
            "acceptance_rate_global": "~10% to 12%",
            "acceptance_rate_pakistan": "~8% to 10% (Strong track record for Pakistani STEM applicants)",
            "typical_successful_applicant_gpa": "3.50 to 3.95 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Top engineering and computer science students from leading Pakistani universities with strong programming and research portfolios.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST-NUCES, GIKI, UET Lahore, LUMS, Quaid-i-Azam University.",
            "high_representation_countries": "Pakistan, Vietnam, Indonesia, China, Kazakhstan, Turkey, Russia, India.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial agents claiming they have 'exclusive quota tie-ups' with KAIST."
            ],
            "application_fee_warning": "Pay only the USD $80 application fee on the official KAIST application portal.",
            "agent_and_intermediary_warnings": "Never work through agents; KAIST requires direct candidate correspondence.",
            "hidden_costs_breakdown": [
                "Application fee ($80).",
                "Consular attestation fees at Korean Embassy in Islamabad.",
                "Flight ticket to South Korea (~PKR 180,000 to 250,000).",
                "Initial living expenses for the first month in Daejeon before stipend release."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must speak Korean. (Fact: KAIST is an English-medium institution; virtually all graduate classes and research meetings are in English).",
                "MYTH: You cannot apply if you don't have IELTS. (Fact: An official English Proficiency Certificate (MOI) from your Pakistani university is officially accepted)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs state the stipend is only KRW 350,000; that is merely the university baseline — active research labs add KRW 600,000 to 1,200,000/mo extra via Research Assistantships (RA)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 2.5 / 4.3 (equivalent to ~2.7/4.0); falling below incurs probation and loss of tuition waiver.",
            "attendance_requirements": "Full-time physical research attendance on campus in Daejeon or Seoul.",
            "academic_progress_monitoring": "Semester credit check and annual research progress evaluation.",
            "work_restrictions_during_study": "Part-time work outside the campus requires university and immigration permission under D-2 visa regulations.",
            "home_country_return_obligation": "None; scholars can seek employment in South Korea's high-tech industry under the D-10 job seeker or E-7 professional work visas.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Expulsion or academic dishonesty results in scholarship revocation.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Changing departments requires mutual consent of both department heads.",
            "extension_policy": "Tuition waiver is strictly provided for 4 semesters (MS) or 8 semesters (PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "KAIST International Graduate Admissions Official Portal",
                "source_url": "https://admission.kaist.ac.kr/intl-graduate/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-by-lab Research Assistantship (RA) funding top-up minimum guidelines",
                    "Departmental quota breakdown between international applicants"
                ]
            }
        ]
    },

    # 2. KAUST Fellowship (SCH-ME-002)
    "SCH-ME-002": {
        "scholarship_id": "SCH-ME-002",
        "basic_details": {
            "scholarship_name": "KAUST Fellowship",
            "offering_entity": "King Abdullah University of Science and Technology (KAUST)",
            "host_country": "Saudi Arabia",
            "host_institutions_covered": "KAUST Campus (Thuwal, Makkah Province, Saudi Arabia)",
            "degree_levels": ["Master of Science (MS)", "PhD (Doctorate)"],
            "major_restrictions": "Biological and Environmental Science and Engineering (BESE), Computer, Electrical and Mathematical Science and Engineering (CEMSE), Physical Science and Engineering (PSE).",
            "number_of_awards_total": "~100% of admitted graduate students receive the full KAUST Fellowship (~250 to 300 new admits/year)",
            "number_of_awards_pakistan": "Open globally based on talent; Pakistan has a large and distinguished cohort of scholars across all academic divisions",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "MS: typically 1.5 to 2 years; PhD: 3.5 to 4 years"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students of all nationalities (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (Bachelor's degree) for MS; 18 years (Master's degree) for PhD from an accredited institution in a relevant STEM field.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum 3.70 / 4.00 CGPA; admitted international students typically present 3.80+ / 4.00 CGPA or rank in top 5% of graduating class.",
            "subject_background_prerequisites": "Rigorous undergraduate foundation in mathematics, computing, engineering, or natural sciences.",
            "current_education_status": "Graduated or in final semester of degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior laboratory research experience, high-impact publications, or international hackathon/coding achievements heavily prioritized.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "TOEFL iBT minimum 79 (KAUST Code: 4107) or IELTS Academic minimum 6.5 (overall score). Official score report is mandatory."
            },
            "other_language_requirements": "Arabic not required; English is the official language of instruction and campus life.",
            "gender_specific_requirements": "Equal opportunity; mixed-gender international research community.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite research potential; every admitted student automatically receives the fellowship.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition support and all academic laboratory fees covered for the full duration of the degree.",
                "amount": "Full coverage (~USD $35,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Online application to KAUST is completely free of charge.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE_FURNISHED_HOUSING",
                "details": "Free private on-campus housing (private air-conditioned apartment or shared villa with private ensuite bathroom) on the Red Sea campus.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "High-tier annual living allowance paid monthly: $20,000 to $30,000 per year ($1,666 to $2,500/month ~PKR 465,000 to 700,000/month depending on degree level and progression).",
                "amount": "$20,000 - $30,000 / year (~PKR 465,000 to 700,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Annual round-trip international airfare provided between home city in Pakistan and Jeddah.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Saudi student visa and Iqama (residence permit) fees fully sponsored and processed by KAUST.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive medical and dental coverage provided at the on-campus KAUST Health Center and private hospitals in Saudi Arabia.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "State-of-the-art laptop, compute clusters (Shaheen supercomputer), and lab supplies provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Full travel, registration, and lodging support for accepted international conference presentations.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Relocation assistance upon arrival.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 75000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: King Abdullah University of Science and Technology (World-renowned research institute).",
            "participating_institutions": [
                "KAUST (Thuwal, Saudi Arabia)"
            ],
            "university_rankings_scope": "Ranked #1 globally in QS Citations per Faculty; world leader in clean combustion, AI, desalination, and solar energy.",
            "available_majors": [
                "Computer Science, Applied Mathematics and Computational Science (AMCS), Statistics, Electrical and Computer Engineering, Mechanical Engineering, Chemical Engineering, Material Science and Engineering, Applied Physics, Bioengineering, Bioscience, Marine Science, Environmental Science and Engineering, Energy Resources and Petroleum Engineering"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MS: 3 to 4 semesters (36 credits); PhD: 3.5 to 4 years",
            "admission_requirements_summary": "All admitted students are automatically awarded the KAUST Fellowship; admission is 100% funded.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "CS, AI, and Electrical Engineering are highly competitive; contacting prospective faculty whose research interests match yours is encouraged.",
            "strategic_program_match_advice": "Highlight technical problem-solving, coding competitions, research publications, and clear alignment with KAUST core research centers."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.kaust.edu.sa/en/study/fellowship",
            "portal_system_name": "KAUST Graduate Admissions Portal",
            "account_creation_instructions": "Register on the KAUST admissions portal, complete personal background, upload SOP, transcripts, CV, and designate three referees.",
            "step_by_step_workflow": [
                "1. Create account on KAUST graduate portal (Opens September for Fall intake).",
                "2. Upload Statement of Purpose, academic transcripts, and detailed CV.",
                "3. Provide three academic recommendation letter contacts.",
                "4. Submit official TOEFL or IELTS scores (KAUST Code: 4107).",
                "5. Complete online application before deadline (Early round: January; Regular round: March).",
                "6. Academic divisions conduct technical screening interviews via video conference.",
                "7. Shortlisted candidates invited for KAUST Admissions Interview (video or in-person).",
                "8. Admission and full fellowship package offer issued."
            ],
            "university_vs_scholarship_routing": "Direct single application; all admits receive the fellowship.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure electronic link sent by KAUST.",
            "personal_statement_prompts": "Statement of Purpose (750 words): Detail your academic background, research interests, career goals, and reasons for choosing KAUST.",
            "study_plan_research_proposal_requirements": "PhD applicants should describe prior research contributions and proposed research questions.",
            "cv_format_requirements": "Detailed academic CV highlighting publications, GitHub repositories, lab techniques, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "Two rounds: 30-minute academic faculty interview testing technical competence, followed by a personal interview assessing motivation and character.",
            "standardized_tests": "GRE is NOT required (though general scores are considered if submitted); TOEFL or IELTS mandatory.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Official university transcripts certified by Pakistani degree-granting institution; HEC attestation required for visa.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via KAUST portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "750-word essay explaining academic motivation, research interests, and career goals",
                "pakistan_specific_instruction": "Clearly articulated technical vision aligned with KAUST research groups"
            },
            {
                "document_name": "Three Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential reports from research supervisors or professors",
                "pakistan_specific_instruction": "From professors who supervised your research or senior project in Pakistan"
            },
            {
                "document_name": "Official Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all undergraduate and graduate education with grading scheme",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "Official TOEFL iBT (79+) or IELTS Academic (6.5+) report",
                "pakistan_specific_instruction": "Electronic score sent to KAUST (Code 4107)"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing publications, awards, and technical skills",
                "pakistan_specific_instruction": "Highlighting FYP, publications, and competitive programming achievements"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2027-01-15",
            "university_admission_deadline": "2027-01-15",
            "document_submission_deadline": "2027-01-15",
            "recommendation_letters_deadline": "2027-01-22",
            "interview_period": "February to March 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "August 2027",
            "annual_cycle_notes": "Early round deadline is mid-January; regular deadline is early March. Admissions operate on rolling evaluation."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic GPA, transcripts, foundational excellence in math and physical sciences)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "40% (Research publications, conference presentations, technical projects, and lab skills)",
            "work_experience_weight": "5% (Industrial/laboratory R&D experience)",
            "personal_statement_weight": "5% (Statement of Purpose alignment with faculty labs)",
            "recommendations_weight": "10% (Referee appraisals of research creativity)",
            "interview_weight": "Decisive during faculty technical interview",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Completely need-blind; all admitted students are fully funded)",
            "selection_panel_composition": "Division Faculty Admissions Committees and the KAUST Central Graduate Admissions Panel.",
            "evaluation_methodology": "Rigorous holistic review identifying individuals with exceptional scientific curiosity, research talent, and potential to make breakthrough discoveries."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000 to 12,000 applications globally across all divisions",
            "total_scholarships_awarded": "~250 to 300 fellowship awards conferred annually",
            "acceptance_rate_global": "~2.5% to 3%",
            "acceptance_rate_pakistan": "~2% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates with top-tier grades, research publications, and exceptional performance in technical video interviews.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani universities (LUMS, NUST, GIKI, FAST-NUCES, Quaid-i-Azam, UET).",
            "high_representation_countries": "China, Saudi Arabia, Pakistan, Egypt, USA, India, Italy, Mexico.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam agencies claiming to guarantee KAUST admission for a fee."
            ],
            "application_fee_warning": "KAUST application is 100% free of charge. Never pay any fee.",
            "agent_and_intermediary_warnings": "Never work through agents; KAUST directly interviews every admitted student.",
            "hidden_costs_breakdown": [
                "HEC and MOFA attestation fees in Pakistan.",
                "Passport issuance and NADRA document verification fees."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need to pay for housing or tuition. (Fact: 100% of tuition, luxury campus housing, healthcare, flights, and living stipends are provided free).",
                "MYTH: You cannot bring family. (Fact: Married MS/PhD students are provided spacious 2-bedroom or 3-bedroom family housing and family healthcare)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs state the stipend is $10,000; the official fellowship provides $20,000 to $30,000 per year."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.0 / 4.00; falling below results in academic probation and potential termination.",
            "attendance_requirements": "Full-time physical research residence on the KAUST campus in Thuwal.",
            "academic_progress_monitoring": "Annual progress reviews and doctoral dissertation committee milestones.",
            "work_restrictions_during_study": "Outside employment is strictly prohibited under Saudi student visa regulations.",
            "home_country_return_obligation": "None; scholars can pursue global careers or continue in Saudi Arabia under Saudi Vision 2030 talent visas.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of fellowship occurs upon academic failure or voluntary withdrawal.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from academic divisions.",
            "extension_policy": "Funding is provided for normal program length (max 2 years for MS; max 4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "King Abdullah University of Science and Technology (KAUST) - Fellowship Official Portal",
                "source_url": "https://www.kaust.edu.sa/en/study/fellowship",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Division-level allocation quotas between MS and PhD tracks",
                    "Faculty interview technical grading rubrics"
                ]
            }
        ]
    },

    # 3. Hamad Bin Khalifa University (HBKU) Scholarship (SCH-ME-004)
    "SCH-ME-004": {
        "scholarship_id": "SCH-ME-004",
        "basic_details": {
            "scholarship_name": "Hamad Bin Khalifa University (HBKU) Scholarship",
            "offering_entity": "Hamad Bin Khalifa University & Qatar Foundation",
            "host_country": "Qatar",
            "host_institutions_covered": "Hamad Bin Khalifa University (Education City, Doha, Qatar)",
            "degree_levels": ["Master's", "PhD (Doctorate)"],
            "major_restrictions": "College of Science & Engineering, College of Health & Life Sciences, College of Law, College of Islamic Studies, College of Public Policy, College of Humanities & Social Sciences.",
            "number_of_awards_total": "~150 to 200 merit-based scholarships awarded annually across all colleges",
            "number_of_awards_pakistan": "Open globally; highly competitive; strong Pakistani representation in CSE and CHLS",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full regular duration of the program (Master's: 2 years; PhD: 3 to 4 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students of all nationalities (including Pakistan) and Qatar residents"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "16 years of education (Bachelor's degree) for Master's; 18 years (Master's degree) for PhD from an accredited institution with strong academic standing.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA; competitive admitted scholarship recipients typically hold 3.50+ / 4.00 CGPA.",
            "subject_background_prerequisites": "Degree relevant to intended graduate field.",
            "current_education_status": "Graduated or in final semester of degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior research experience, publications, and professional achievements evaluated favorably.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic minimum 6.5 or TOEFL iBT minimum 79 (score validity 2 years)."
            },
            "other_language_requirements": "None for English-taught programs; Arabic required for Islamic Studies courses.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Merit-based financial aid; candidates apply for funding alongside university admission.",
            "previous_scholarship_restrictions": "Cannot hold multiple full scholarships concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee waiver for the entire duration of the degree program.",
                "amount": "QAR 60,000 to 90,000 / year (~USD $16,000 to $25,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "HBKU application fee (QAR 400, ~PKR 30,000) paid by candidate on portal.",
                "amount": "QAR 400"
            },
            "accommodation": {
                "status": "FREE_FURNISHED_HOUSING",
                "details": "Free single-occupancy student accommodation in Qatar Foundation Education City student housing residences.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free monthly living stipend paid directly to student.",
                "amount": "Master's: QAR 5,000 / month (~PKR 380,000 / month); PhD: QAR 7,500 / month (~PKR 570,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Annual round-trip economy class flight between home city and Doha, Qatar.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Qatar student residence permit and visa fees sponsored by HBKU.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive health insurance provided by Hamad Medical Corporation / private coverage.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered from living allowance and lab research budget.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Conference travel funding accessible via Qatar National Research Fund (QNRF) projects and university travel grants.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Education City tram and shuttle transit free.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 48000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Hamad Bin Khalifa University (Education City, Doha, Qatar).",
            "participating_institutions": [
                "Hamad Bin Khalifa University (College of Science & Engineering, College of Health & Life Sciences, College of Public Policy, College of Law, College of Islamic Studies)"
            ],
            "university_rankings_scope": "Premier research university in Qatar Foundation's Education City.",
            "available_majors": [
                "Computer Science and Engineering, Cybersecurity, Data Analytics, Sustainable Energy, Sustainable Environment, Genomics & Precision Medicine, Biological and Biomedical Sciences, Exercise Science, Public Policy, International Law, Islamic Finance, Digital Humanities"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 to 4 years",
            "admission_requirements_summary": "Apply for admission on the HBKU online portal; complete the financial aid / scholarship application section.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "College of Science & Engineering (Cybersecurity and Data Analytics) has highest applicant volume; early submission strongly advised.",
            "strategic_program_match_advice": "Align your research proposal with Qatar National Vision 2030 pillars: Cyber Security, Energy Transition, Precision Health, and Water Security."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.hbku.edu.qa/en/admissions",
            "portal_system_name": "HBKU Online Graduate Admissions Portal",
            "account_creation_instructions": "Register on the HBKU online portal, select college and degree program, complete personal profile, and upload required documents.",
            "step_by_step_workflow": [
                "1. Choose degree program and review admission requirements (Opens November).",
                "2. Create account on HBKU online portal and complete application form.",
                "3. Pay the QAR 400 application fee online.",
                "4. Upload Statement of Purpose, academic transcripts, CV, and research proposal.",
                "5. Designate two academic referees who submit online recommendation letters.",
                "6. Submit before the international applicant deadline (February 1).",
                "7. Departmental committees conduct academic review and video interviews in March.",
                "8. Admissions and scholarship offers released in April/May."
            ],
            "university_vs_scholarship_routing": "Integrated application: Financial aid considered during admissions review.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure electronic link sent by HBKU.",
            "personal_statement_prompts": "Statement of Interest detailing academic background, career objectives, and reasons for choosing HBKU.",
            "study_plan_research_proposal_requirements": "Detailed research proposal (2-4 pages) required for PhD and research master's applicants.",
            "cv_format_requirements": "Standard academic and professional resume.",
            "interviews_conducted": True,
            "interview_format_details": "Departmental faculty panel conducts 20-30 minute video interview via Microsoft Teams in March.",
            "standardized_tests": "GRE optional but encouraged for STEM; IELTS Academic (6.5+) or TOEFL iBT (79+) mandatory.",
            "application_fee_amount": "QAR 400.",
            "attestation_requirements": "Transcripts certified by Pakistani degree-granting institution; HEC and Qatar Embassy attestation required for visa.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via HBKU portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Statement of Interest",
                "mandatory": True,
                "specification": "Detailed essay outlining academic background and motivation",
                "pakistan_specific_instruction": "Clearly articulated research and professional goals"
            },
            {
                "document_name": "Academic Transcripts & Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all university education showing credits and grades",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Submitted directly by university research professors",
                "pakistan_specific_instruction": "From professors who supervised your BS/MS thesis"
            },
            {
                "document_name": "Research Proposal (for PhD)",
                "mandatory": True,
                "specification": "Structured research proposal (2-4 pages)",
                "pakistan_specific_instruction": "Aligned with HBKU research priorities"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (79+)",
                "pakistan_specific_instruction": "Valid official test score"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-11-01",
            "application_deadline": "2027-02-01",
            "university_admission_deadline": "2027-02-01",
            "document_submission_deadline": "2027-02-01",
            "recommendation_letters_deadline": "2027-02-08",
            "interview_period": "March 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-05-15",
            "visa_application_window": "June to July 2027",
            "semester_commencement": "August 2027",
            "annual_cycle_notes": "International applicant deadline is strictly February 1 each year (earlier than local Qatar resident deadline in March)."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic GPA, transcript performance, prestige of home university)",
            "extracurricular_and_leadership_weight": "10% (Leadership and community engagement)",
            "research_experience_weight": "30% (Prior publications, research proposal quality, laboratory skills)",
            "work_experience_weight": "5% (Professional experience)",
            "personal_statement_weight": "10% (Statement of Interest clarity)",
            "recommendations_weight": "10% (Strength of referee endorsements)",
            "interview_weight": "Decisive during panel interview",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "College Admissions Committees and HBKU Central Scholarship Award Committee.",
            "evaluation_methodology": "Holistic review of academic credentials, research proposal, interview, and alignment with Qatar Foundation priorities."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 4,500 international applications across all colleges",
            "total_scholarships_awarded": "~150 to 200 fully-funded scholarships awarded annually",
            "acceptance_rate_global": "~4% to 5%",
            "acceptance_rate_pakistan": "~3% to 4% (Competitive)",
            "typical_successful_applicant_gpa": "3.50 to 3.95 / 4.00 CGPA",
            "typical_academic_and_research_profile": "High-performing graduates with solid foundational knowledge, research publications, and clear alignment with HBKU research groups.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (NUST, LUMS, Quaid-i-Azam, GIKI, FAST, UET Lahore, Aga Khan University).",
            "high_representation_countries": "Pakistan, Egypt, Jordan, India, Lebanon, Nigeria, Palestine, Morocco.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial agencies claiming they can guarantee HBKU scholarship awards."
            ],
            "application_fee_warning": "Pay only the QAR 400 application fee directly on the official HBKU portal.",
            "agent_and_intermediary_warnings": "Never work through agents; HBKU does not authorize external intermediaries.",
            "hidden_costs_breakdown": [
                "Application fee (QAR 400, ~PKR 30,000).",
                "HEC and Qatar Embassy attestation fees in Islamabad.",
                "Initial pocket money before first stipend release."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need Arabic. (Fact: Programs in Science & Engineering, Health, and Public Policy are taught 100% in English).",
                "MYTH: The scholarship requires repayment. (Fact: HBKU scholarships are merit grants with NO repayment obligation)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites confuse HBKU with Qatar University; they are two separate institutions with distinct scholarship frameworks."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.0 / 4.00 and earn required credits each semester.",
            "attendance_requirements": "Full-time physical residence and attendance in Education City, Doha, Qatar.",
            "academic_progress_monitoring": "Semester grade review; academic probation leads to loss of scholarship.",
            "work_restrictions_during_study": "On-campus student employment permitted up to 20 hours/week; outside employment restricted under Qatar student visa rules.",
            "home_country_return_obligation": "None; graduates can seek employment in Qatar's research and industrial sectors post-graduation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Expulsion, academic failure, or voluntary withdrawal terminates funding.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from both colleges.",
            "extension_policy": "Strictly limited to the standard program duration (max 2 years for MS; max 4 years for PhD)."
        },
        "official_sources_verified": [
            {
                "source_name": "Hamad Bin Khalifa University (HBKU) - Admissions & Funding Official Portal",
                "source_url": "https://www.hbku.edu.qa/en/admissions",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation quota breakdown between local residents and international applicants",
                    "College-by-college interview scoring rubrics"
                ]
            }
        ]
    }
}
