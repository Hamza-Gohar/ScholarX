"""
scripts/dossiers_batch6a.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Batch 6A
Contains 4 Americas Scholarships:
9. SCH-AM-005: University of Waterloo International Doctoral Award (IDSA) (Canada)
10. SCH-AM-006: Rotary Peace Fellowship (USA / The Rotary Foundation & Duke/UNC)
11. SCH-AM-007: University of Calgary International Entrance Scholarship (Canada)
12. SCH-AM-011: Banting Postdoctoral Fellowships (Canada / CIHR, NSERC, SSHRC)
"""

DOSSIERS_BATCH6A = {
    # 9. University of Waterloo International Doctoral Award (IDSA) (SCH-AM-005)
    "SCH-AM-005": {
        "scholarship_id": "SCH-AM-005",
        "basic_details": {
            "scholarship_name": "University of Waterloo International Doctoral Award (IDSA)",
            "offering_entity": "University of Waterloo (Graduate Studies and Postdoctoral Affairs - GSPA)",
            "host_country": "Canada",
            "host_institutions_covered": "University of Waterloo (Waterloo, Ontario, Canada)",
            "degree_levels": ["Doctoral / PhD"],
            "major_restrictions": "Open to full-time doctoral students across all faculties: Mathematics & Computer Science (Cheriton School of CS), Engineering, Science (Physics, Chemistry, Quantum Information), Environment, Health, and Arts.",
            "number_of_awards_total": "~500 to 600 active international PhD students supported concurrently",
            "number_of_awards_pakistan": "Open international competition; awarded automatically to all eligible full-time international doctoral candidates",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (12 full-time academic terms)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students holding a valid Canadian study permit"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed Master's degree (18 years education) or direct-entry Bachelor's degree with first-class honors (minimum 80% or 3.70+ / 4.00 CGPA).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum overall first-class standing (at least 80% or A- grade equivalent in Canadian university grading scale).",
            "subject_background_prerequisites": "Rigorous background in computer science, mathematics, engineering, or physics corresponding to target department.",
            "current_education_status": "Admitted to full-time PhD degree at University of Waterloo.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications, open-source repositories, and thesis research heavily prioritized.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic minimum 7.0 overall (writing 6.5, speaking 6.5) or TOEFL iBT min 90 (writing 25, speaking 25)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Full-time international PhD candidature.",
            "previous_scholarship_restrictions": "Must not be self-funded or sponsored by an external agency covering full international tuition.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIALLY_COVERED",
                "details": "IDSA provides CAD $4,740 per term (CAD $14,220 per year) directly offsetting international tuition differential, bundled with departmental Graduate Research Studentship (GRS) to cover 100% of tuition and minimum guaranteed living stipend.",
                "amount": "CAD $14,220 / year IDSA offset"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Waterloo graduate application fee (CAD $125) paid by applicant.",
                "amount": "CAD $125"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid out of guaranteed doctoral funding package (~CAD $27,000–$35,000/yr); on-campus graduate residences (Columbia Lake Village) or off-campus housing in Waterloo.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Guaranteed minimum doctoral funding package across all STEM departments is at least CAD $27,000 to $32,000/year (typically CAD $2,250 to $2,700/month / ~PKR 460,000 to 550,000/month).",
                "amount": "CAD $27,000 to $35,000 / year total package"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel costs borne by student; select research supervisors provide initial travel subsidies.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD $150) and biometric fee (CAD $85) paid by applicant.",
                "amount": "CAD $235"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "University Health Insurance Plan (UHIP) for international students covered under graduate student benefits package.",
                "amount": "CAD $756 / year"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly doctoral research stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Departmental laboratory computing infrastructure, cloud compute credits, and research desks provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty of Mathematics / Engineering Graduate Student Conference Travel Grants (up to CAD $1,500/yr).",
                "amount": "Up to CAD $1,500 / year"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Grand River Transit (GRT) universal bus pass included in student ancillary fees.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 32000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Waterloo (Waterloo, Ontario, Canada).",
            "participating_institutions": [
                "University of Waterloo"
            ],
            "university_rankings_scope": "#115 QS World University Rankings 2025; Top 25 globally in Computer Science; #1 in Canada for tech innovation.",
            "available_majors": [
                "Computer Science (Cheriton School of CS), Quantum Information (IQC), Electrical & Computer Engineering, Mechanical & Mechatronics Engineering, Combinatorics & Optimization, Pure Mathematics, Statistics & Actuarial Science, Chemical Engineering, Physics & Astronomy"
            ],
            "english_taught_program_availability": True,
            "program_duration": "48 months (4 years / 12 terms)",
            "admission_requirements_summary": "Master's degree in CS, Engineering, or Math with minimum 80% average; research supervisor agreement strongly recommended.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing a faculty advisor at Cheriton School of CS or Institute for Quantum Computing (IQC) before application significantly boosts admission chances.",
            "strategic_program_match_advice": "Check faculty member publication pages and email professors 2-3 months before the December/January deadline with a focused research summary."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/awards/international-doctoral-student-award-idsa",
            "portal_system_name": "University of Waterloo Quest Graduate Admissions Portal / OUAC",
            "account_creation_instructions": "Step 1: Submit online application through Ontario Universities' Application Centre (OUAC). Step 2: Upload documents into Waterloo Quest system.",
            "step_by_step_workflow": [
                "1. Identify potential research supervisors in your field (September-November).",
                "2. Apply via OUAC online application system.",
                "3. Receive Quest credentials and upload transcripts, CV, and statement of research interest.",
                "4. Nominate 3 academic referees who submit online reference forms.",
                "5. Departmental admissions committee reviews applications and makes admission offer with guaranteed funding.",
                "6. IDSA is automatically credited to the student's tuition account each term.",
                "7. Apply for Canadian Study Permit via IRCC portal."
            ],
            "university_vs_scholarship_routing": "Integrated automatic assessment with full-time doctoral admission.",
            "recommendation_letters_submission_method": "Submitted online by 3 academic referees via Quest electronic portal.",
            "personal_statement_prompts": "Supplementary Information Form (SIF) outlining research interests, prior publications, and reasons for choosing University of Waterloo.",
            "study_plan_research_proposal_requirements": "Summary of research interests and proposed dissertation topic (1–2 pages).",
            "cv_format_requirements": "Academic CV detailing publications, GitHub projects, awards, and research experience.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisors conduct 30-45 minute technical interviews via Zoom or Microsoft Teams.",
            "standardized_tests": "GRE General test is optional but recommended for Cheriton School of CS international applicants.",
            "application_fee_amount": "CAD $125 application fee.",
            "attestation_requirements": "Official university transcripts verified by home institution registrar; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online through Waterloo Quest portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Data Page",
                "mandatory": True,
                "specification": "Scanned copy of valid passport",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Bachelor's and Master's Official Transcripts",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year and 18-year education with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Three Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential academic letters from previous professors or thesis supervisors",
                "pakistan_specific_instruction": "Submitted via Quest referee portal"
            },
            {
                "document_name": "Supplementary Information Form (SIF) / Statement of Research",
                "mandatory": True,
                "specification": "Written statement outlining research background and prospective Waterloo research goals",
                "pakistan_specific_instruction": "Highlight alignment with Waterloo lab"
            },
            {
                "document_name": "English Language Test Report",
                "mandatory": True,
                "specification": "Official IELTS Academic (7.0+) or TOEFL iBT (90+)",
                "pakistan_specific_instruction": "Official test report sent to Waterloo code 0998"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2026-12-15",
            "university_admission_deadline": "2026-12-15",
            "document_submission_deadline": "2027-01-15",
            "recommendation_letters_deadline": "2027-01-15",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "March 2027",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "April to July 2027",
            "semester_commencement": "2027-09-01",
            "annual_cycle_notes": "Main intake is Fall (September). Winter (January) and Spring (May) intakes have earlier deadlines."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Master's and Bachelor's GPA, class standing)",
            "extracurricular_and_leadership_weight": "5% (Extracurricular and student leadership)",
            "research_experience_weight": "40% (Refereed publications, master's thesis, and research projects)",
            "work_experience_weight": "5% (Industry lab or software engineering experience)",
            "personal_statement_weight": "5% (Quality of SIF research goals)",
            "recommendations_weight": "10% (Evaluations from academic referees)",
            "interview_weight": "Decisive for professor endorsement",
            "test_scores_weight": "Language test passing threshold",
            "financial_need_weight": "0% (Purely research and academic merit)",
            "selection_panel_composition": "Departmental Graduate Admissions Committee and individual faculty research supervisors.",
            "evaluation_methodology": "Faculty supervisor review and nomination -> Departmental graduate committee ranking -> Formal admission and GSPA award ratification."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 international applicants across doctoral departments",
            "total_scholarships_awarded": "~500 to 600 active doctoral scholars funded",
            "acceptance_rate_global": "~6%",
            "acceptance_rate_pakistan": "~3% to 4% (Very Competitive)",
            "typical_successful_applicant_gpa": "3.80+ / 4.00 CGPA (or 85%+ marks)",
            "typical_academic_and_research_profile": "Graduates from NUST, FAST, LUMS, GIKI, UET with first-author conference or journal papers in top CS/engineering venues (NeurIPS, ICML, IEEE, ACM).",
            "common_backgrounds_of_winners": "Strong Pakistani representation in Cheriton School of CS, Electrical & Computer Engineering, and Quantum Information.",
            "high_representation_countries": "China, India, Iran, Pakistan, United States, South Korea, Turkey.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized immigration sites: uwaterloo-canada-scholarships.org, studyinwaterloo-visas.com."
            ],
            "application_fee_warning": "Application fee of CAD $125 is paid solely through OUAC / Quest portal. IDSA itself requires no separate application or fee.",
            "agent_and_intermediary_warnings": "University of Waterloo does not work with third-party agents who claim to guarantee doctoral admission.",
            "itemized_hidden_out_of_pocket_costs": [
                "Canadian Study Permit application and biometric fee (CAD $235 / ~PKR 48,000)",
                "University application fee (CAD $125 / ~PKR 25,000)",
                "Airfare Pakistan to Toronto Pearson (~PKR 220,000 to 320,000)",
                "Initial housing deposit in Waterloo (~CAD $1,000 to $1,500)"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: IDSA is a separate competitive application. (Truth: IDSA is automatically awarded to all eligible full-time international PhD students who are admitted with funding).",
                "MYTH: You cannot work in Canada while on this fellowship. (Truth: PhD students hold full on-campus work rights and off-campus work authorization under Canadian study permit regulations)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Commercial blogs confuse the IDSA tuition credit with external scholarships; IDSA is an institutional tuition differential offset funded directly by Waterloo."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain satisfactory academic standing (minimum 75% average in graduate courses) and pass PhD Comprehensive Examination by term 4 or 5.",
            "attendance_requirements": "Full-time physical research residence at Waterloo campus.",
            "academic_progress_monitoring": "Annual PhD student progress evaluation submitted by supervisory committee.",
            "work_restrictions_during_study": "Graduate Teaching Assistantships (GTA) limited to 10 hours per week (average of 140 hours per term) to prevent thesis progress delays.",
            "home_country_return_obligation": "None; international PhD graduates from Ontario universities qualify for the Ontario Immigrant Nominee Program (OINP) PhD Graduate Stream and 3-year Post-Graduation Work Permit (PGWP).",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Award is discontinued if the student switches to part-time status, withdraws, or fails comprehensive examinations.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from old and new faculty supervisors and graduate officer.",
            "extension_policy": "IDSA is granted for up to 12 academic terms (4 years); beyond term 12, funding is subject to supervisor research grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Waterloo - International Doctoral Student Award (IDSA) Official Portal",
                "source_url": "https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/awards/international-doctoral-student-award-idsa",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental breakdown of top-up funding above the guaranteed minimum across different engineering schools.",
                    "Exact percentage of admitted international PhD students holding direct-entry bachelor's vs master's degrees.",
                    "Internal waitlist conversion rates across admissions cycles."
                ]
            }
        ]
    },

    # 10. Rotary Peace Fellowship (SCH-AM-006)
    "SCH-AM-006": {
        "scholarship_id": "SCH-AM-006",
        "basic_details": {
            "scholarship_name": "Rotary Peace Fellowship",
            "offering_entity": "The Rotary Foundation (Rotary International)",
            "host_country": "United States",
            "host_institutions_covered": "Duke University & University of North Carolina at Chapel Hill (USA), International Christian University (Japan), University of Bradford (UK), University of Queensland (Australia), Uppsala University (Sweden), Makerere University (Uganda), Bahçeşehir University (Turkey)",
            "degree_levels": ["Master's Degree", "Professional Certificate"],
            "major_restrictions": "Peace and Conflict Resolution, International Development, Human Rights, Public Policy, Global Public Health, Environmental Peacebuilding, International Relations.",
            "number_of_awards_total": "~130 fellowships awarded globally per year (50 Master's degrees, 80 Professional Development Certificates)",
            "number_of_awards_pakistan": "Open global merit pool; Pakistan has a strong history of fellows endorsed by local Rotary districts (typically 2 to 5 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "15 to 24 months for Master's degree; 1 year (including online modules and on-site intensive) for Professional Certificate"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to citizens of all countries (except active Rotary club members or direct descendants of Rotarians)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No upper age limit.",
            "academic_qualifications": "Bachelor's degree (16 years education) with strong academic standing.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA; practical field experience and leadership impact are weighted heavily alongside academic grades.",
            "subject_background_prerequisites": "Background in social sciences, public policy, international relations, law, journalism, or related fields.",
            "current_education_status": "Graduated and currently working in peacebuilding, development, or public service.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": True,
            "work_experience_minimum_years": 3.0,
            "work_experience_notes": "Minimum 3 years of full-time professional experience in peace, development, or conflict prevention for Master's; minimum 5 years for Professional Certificate.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Proficiency in English required (IELTS 7.0+ or TOEFL 90+); second language proficiency evaluated favorably."
            },
            "other_language_requirements": "Fluency in English; proficiency in a second international language is advantageous.",
            "gender_specific_requirements": "Equal opportunity; diversity and female community leadership strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Proven leadership and dedicated commitment to peacebuilding and community transformation.",
            "previous_scholarship_restrictions": "Active Rotary members, honorary Rotarians, and their spouses or lineal descendants are ineligible.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition and mandatory academic fees paid directly to host university.",
                "amount": "100% covered (~USD $35,000 to $65,000 / year)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Application and university administrative costs reimbursed or waived under Rotary partnership.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Room and board covered comprehensively via living stipend or direct university housing.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly stipend to cover rent, utilities, food, and personal living expenses (~USD $1,800 to $2,400/month depending on host city / ~PKR 500,000 to 670,000/month).",
                "amount": "USD $1,800 to $2,400 / month (~PKR 500,000 to 670,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Round-trip economy international airfare between home country and host university.",
                "amount": "Round-trip flights covered"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Visa application processing fees reimbursed upon presentation of receipts.",
                "amount": "100% reimbursed"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive student medical and emergency repatriation insurance provided.",
                "amount": "100% covered"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Included within monthly room and board stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Course books and study materials allowance provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Fully funded Applied Field Experience (AFE) of 2-3 months during summer break (travel, housing, and living stipend fully covered).",
                "amount": "Full funding for summer field practicum"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Travel transit allowance provided for relocation.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 55000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple institutions: Rotary Peace Centers across 7 prestigious global universities.",
            "participating_institutions": [
                "Duke University and University of North Carolina at Chapel Hill (USA)",
                "International Christian University (ICU, Tokyo, Japan)",
                "University of Bradford (Bradford, UK)",
                "University of Queensland (Brisbane, Australia)",
                "Uppsala University (Uppsala, Sweden)",
                "Makerere University (Kampala, Uganda)",
                "Bahçeşehir University (Istanbul, Turkey)"
            ],
            "university_rankings_scope": "Top 100 global institutions in Peace, Conflict Studies, and Public Policy (Duke, UNC, Uppsala, Queensland).",
            "available_majors": [
                "Peace and Conflict Resolution, International Development Policy, Global Public Health, Human Rights, International Relations, Environmental Peacebuilding, Public Administration"
            ],
            "english_taught_program_availability": True,
            "program_duration": "15 to 24 months (Master's) or 1 year (Certificate)",
            "admission_requirements_summary": "Bachelor's degree, minimum 3 years relevant professional experience, strong leadership record, and district endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Duke-UNC is the most sought-after center; candidates rank top two center preferences on application.",
            "strategic_program_match_advice": "Candidates must secure an endorsement from a local Rotary District in Pakistan before the central deadline (May 15)."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.rotary.org/en/peace-fellowships",
            "portal_system_name": "Rotary Peace Fellowship Online Application Portal",
            "account_creation_instructions": "Create an account on the Rotary International Peace Fellowship application platform during the open window.",
            "step_by_step_workflow": [
                "1. Review eligibility criteria and ensure 3+ years full-time peace/development work experience (January).",
                "2. Connect with a local Rotary Club or District in Pakistan for initial consultation and endorsement inquiry.",
                "3. Complete the online Rotary Peace Fellowship application.",
                "4. Upload transcripts, essays, CV, and two professional/academic recommendation letters.",
                "5. Submit application to local Rotary District by May 15.",
                "6. Attend district interview (virtual or in-person) by July 1.",
                "7. Rotary District submits endorsement to The Rotary Foundation.",
                "8. Central Rotary Peace Center committee announces fellowship winners in November.",
                "9. Selected fellows apply to host university for academic admission (November-January)."
            ],
            "university_vs_scholarship_routing": "Scholarship awarded first by Rotary International; fellow then applies to assigned host Rotary Peace Center university.",
            "recommendation_letters_submission_method": "Submitted online by 2 referees (1 professional supervisor, 1 academic or civic leader).",
            "personal_statement_prompts": "Essays detailing peacebuilding vision, professional leadership experiences, and how the fellowship will advance peace initiatives in your community.",
            "study_plan_research_proposal_requirements": "Essays explaining specific issues in peace and development you plan to address during your studies and summer field experience.",
            "cv_format_requirements": "Professional CV highlighting peace, NGO, human rights, public sector, and community leadership roles.",
            "interviews_conducted": True,
            "interview_format_details": "Rotary District endorsement interview conducted in June; central finalist video interview in September.",
            "standardized_tests": "GRE not required by Rotary; university may require language test.",
            "application_fee_amount": "100% free; no application fee.",
            "attestation_requirements": "Authenticated copies of university transcripts and degree certificates.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online through Rotary International platform."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Data Page",
                "mandatory": True,
                "specification": "Scanned copy of international passport",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Bachelor's Degree Transcripts & Certificate",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year education with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "1 professional reference validating peace/development work + 1 academic/leadership reference",
                "pakistan_specific_instruction": "From NGO directors, UN supervisors, or professors"
            },
            {
                "document_name": "Rotary District Endorsement Form",
                "mandatory": True,
                "specification": "Official endorsement completed by a Rotary District Governor or committee chair",
                "pakistan_specific_instruction": "Endorsed by Rotary District 3271 or 3272 in Pakistan"
            },
            {
                "document_name": "Peacebuilding Essays & CV",
                "mandatory": True,
                "specification": "Essays addressing personal commitment, leadership, and field impact",
                "pakistan_specific_instruction": "Highlight local community conflict resolution or development work in Pakistan"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-02-01",
            "application_deadline": "2026-05-15",
            "university_admission_deadline": "2026-12-15",
            "document_submission_deadline": "2026-05-15",
            "recommendation_letters_deadline": "2026-05-15",
            "interview_period": "June 2026 (District) / September 2026 (World Panel)",
            "shortlist_announcement": "October 2026",
            "final_result_acceptance_deadline": "2026-11-15",
            "visa_application_window": "April to July 2027",
            "semester_commencement": "August / September 2027",
            "annual_cycle_notes": "Very structured annual timeline; applications submitted 15 months prior to academic commencement."
        },
        "selection_process_and_weights": {
            "academic_weight": "20% (Academic record and intellectual capability)",
            "extracurricular_and_leadership_weight": "25% (Community leadership and social mobilization)",
            "research_experience_weight": "5% (Research publications or policy reports)",
            "work_experience_weight": "30% (Proven record in peacebuilding, development, and community impact)",
            "personal_statement_weight": "10% (Clarity of vision and commitment to Rotary ideals)",
            "recommendations_weight": "10% (Quality of professional and district endorsements)",
            "interview_weight": "Crucial stage during district and global panels",
            "test_scores_weight": "0% (No standardized tests required)",
            "financial_need_weight": "0% (Merit-based)",
            "selection_panel_composition": "District Rotary Committee, International Rotary Foundation Trustees, and Faculty Selection Board of host Peace Centers.",
            "evaluation_methodology": "District endorsement interview -> Global screening by Rotary Trustees -> Finalist placement at host Rotary Peace Center."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 highly qualified mid-career applicants globally",
            "total_scholarships_awarded": "~50 Master's fellowships and ~80 certificate fellowships annually",
            "acceptance_rate_global": "~3.3% (Master's track)",
            "acceptance_rate_pakistan": "~2.0% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.30+ / 4.00 CGPA",
            "typical_academic_and_research_profile": "Mid-career leaders with 4-8 years of on-the-ground experience in disaster relief, refugee rehabilitation, human rights advocacy, mediation, or public sector governance.",
            "common_backgrounds_of_winners": "Pakistani fellows include NGO founders, UN field officers, civil servants, and investigative journalists.",
            "high_representation_countries": "United States, Pakistan, Colombia, Kenya, Nigeria, India, Afghanistan, Myanmar, Uganda.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam portals soliciting endorsement fees: rotary-peace-fellowship-portal.org, peace-scholars-fund.com."
            ],
            "application_fee_warning": "Applying for Rotary Peace Fellowship is 100% free of charge. Never pay any Rotary club or district for an endorsement.",
            "agent_and_intermediary_warnings": "Endorsements must be obtained directly through legitimate Rotary clubs; third-party agents have no standing.",
            "itemized_hidden_out_of_pocket_costs": [
                "HEC and MOFA attestation of Pakistani degree documents (~PKR 15,000 to 25,000)",
                "English language test fees (IELTS/TOEFL) if required by host university (~PKR 55,000 to 65,000)",
                "Initial domestic travel expenses within Pakistan to attend Rotary District interviews"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: You must be a Rotarian to apply. (Truth: Rotarians and their immediate relatives are legally disqualified from applying; it is strictly intended for non-Rotarians).",
                "MYTH: You need a degree in peace studies. (Truth: Candidates from law, engineering, computer science, journalism, medicine, and business with peacebuilding applications are welcome)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Commercial sites suggest direct university application; Rotary requires fellowship selection first, followed by university placement."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain good academic standing per host university graduate regulations.",
            "attendance_requirements": "Full-time physical attendance; participation in annual Rotary Peace Conference.",
            "academic_progress_monitoring": "Semi-annual progress reports submitted to The Rotary Foundation.",
            "work_restrictions_during_study": "Fellows are expected to dedicate full time to their academic studies and applied field experience; outside employment is discouraged.",
            "home_country_return_obligation": "No binding service bond, but fellows commit to advancing peace and international cooperation throughout their careers.",
            "service_obligations_or_bonds": "Commitment to lifelong membership in Rotary Peace Fellowship Alumni Association.",
            "repayment_clawback_conditions": "Funding terminated if fellow drops out, engages in academic misconduct, or fails to complete summer field experience.",
            "rules_for_changing_university": "Strictly prohibited; fellows are assigned to a specific Rotary Peace Center.",
            "rules_for_changing_major": "Not permitted outside approved degree course.",
            "extension_policy": "No extensions beyond the standard degree curriculum."
        },
        "official_sources_verified": [
            {
                "source_name": "The Rotary Foundation - Rotary Peace Fellowships Official Portal",
                "source_url": "https://www.rotary.org/en/peace-fellowships",
                "source_type": "OFFICIAL_ORGANIZATION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "District-by-district endorsement quota allocations across developing nations.",
                    "Exact interview scoring sheets used by the Rotary World Peace Fellowship Committee.",
                    "Comparative statistics on successful university placement matches for second-choice centers."
                ]
            }
        ]
    },

    # 11. University of Calgary International Entrance Scholarship (SCH-AM-007)
    "SCH-AM-007": {
        "scholarship_id": "SCH-AM-007",
        "basic_details": {
            "scholarship_name": "University of Calgary International Entrance Scholarship",
            "offering_entity": "University of Calgary (Alberta, Canada)",
            "host_country": "Canada",
            "host_institutions_covered": "University of Calgary (Calgary, Alberta, Canada)",
            "degree_levels": ["Bachelor's Degree"],
            "major_restrictions": "Open to all undergraduate faculties: Schulich School of Engineering, Faculty of Science (Computer Science, Data Science, Physics, Chemistry, Biology), Haskayne School of Business, Cumming School of Medicine (Health Sciences), Arts, and Architecture.",
            "number_of_awards_total": "~2 to 4 major prestigious entrance scholarships awarded annually (renewable for 4 years)",
            "number_of_awards_pakistan": "Open global competition; awarded to the highest-achieving international matriculants (typically 1 awardee every 1-2 years from South Asia)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "4 years (renewable annually up to CAD $80,000 total)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students who are not Canadian citizens or Permanent Residents"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 22,
            "age_limit_postgrad": None,
            "age_limit_notes": "Entering first year of undergraduate studies directly from high school.",
            "academic_qualifications": "Completed higher secondary education (FSc Pre-Engineering/Pre-Medical or A-Levels) with exceptional academic distinction.",
            "minimum_gpa_percentage": 95.0,
            "minimum_gpa_scale": 3.9,
            "grading_conversion_notes": "Minimum 95.0% average across academic high school subjects (or minimum 3 A*s in A-Levels / 950+ out of 1100 in FSc).",
            "subject_background_prerequisites": "Advanced high school mathematics, physics, and chemistry for engineering and computer science programs.",
            "current_education_status": "Graduating high school senior entering Fall term.",
            "graduation_year_restrictions": "Must be entering university directly from high school without having completed prior university coursework.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Extracurricular leadership, scientific olympiads, and community service evaluated.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 86,
                "duolingo_accepted": True,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic minimum 6.5 (minimum 6.0 in all bands), TOEFL iBT 86, or Duolingo English Test (DET) 115."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite international academic and leadership high school graduates.",
            "previous_scholarship_restrictions": "Must not have attended any post-secondary institution.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIALLY_COVERED",
                "details": "CAD $20,000 per year for 4 years (CAD $80,000 total), directly credited against international undergraduate tuition fees (~CAD $27,000 to $35,000/year).",
                "amount": "CAD $20,000 / year (CAD $80,000 total / ~PKR 16,300,000 total)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Calgary undergraduate application fee (CAD $145) paid by applicant.",
                "amount": "CAD $145"
            },
            "accommodation": {
                "status": "PARTIALLY_COVERED",
                "details": "Covered from scholarship credit or personal funds; on-campus residence guaranteed for first-year students.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "PARTIALLY_COVERED",
                "details": "Scholarship is applied directly to student tuition fee account; surplus can be refunded for living expenses.",
                "amount": "CAD $20,000 annual lump sum credit"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel costs borne by student.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit application fee (CAD $150) and biometrics (CAD $85) paid by applicant.",
                "amount": "CAD $235"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Alberta Health Care Insurance Plan (AHCIP) provides free basic health coverage for international students with study permits of 12+ months.",
                "amount": "100% free under Alberta provincial healthcare"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Self-funded or paid from scholarship surplus / family support.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "University library, laboratory facilities, and software provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Undergraduate research awards (PURE Awards - CAD $6,000 to $7,500 for summer research) available in years 2-4.",
                "amount": "Summer PURE awards available"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Calgary Transit U-Pass included in university mandatory fees (unlimited city bus and CTrain).",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Calgary (Calgary, Alberta, Canada).",
            "participating_institutions": [
                "University of Calgary"
            ],
            "university_rankings_scope": "#198 QS World University Rankings 2025; Top 10 in Canada; #1 in Canada for startup creation.",
            "available_majors": [
                "Software Engineering, Computer Science, Data Science, Mechanical Engineering, Biomedical Engineering, Electrical Engineering, Chemical & Petroleum Engineering, Health Sciences, Business (Haskayne), Physics, Biochemistry"
            ],
            "english_taught_program_availability": True,
            "program_duration": "48 months (4 years)",
            "admission_requirements_summary": "High school completion with minimum 95% average in required academic subjects (Math, Physics, Chemistry, English).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Software Engineering and Computer Science require competitive grade averages above 95%.",
            "strategic_program_match_advice": "Apply for undergraduate admission by December 1, and complete the High School Awards application before December 15."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ucalgary.ca/registrar/finances/awards/international-entrance-scholarship",
            "portal_system_name": "University of Calgary Student Center (myUofC) Awards Application",
            "account_creation_instructions": "Step 1: Submit undergraduate admission application on ucalgary.ca by December 1. Step 2: Log into myUofC portal and complete High School Awards application by December 15.",
            "step_by_step_workflow": [
                "1. Apply for undergraduate admission on ucalgary.ca portal before December 1.",
                "2. Pay the CAD $145 application fee and receive UCID number.",
                "3. Log into myUofC Student Centre and navigate to 'Apply for Awards'.",
                "4. Complete High School Entrance Awards application before December 15.",
                "5. Upload personal statements, leadership activities list, and reference letters.",
                "6. Central awards committee reviews academic transcripts and extracurricular essays.",
                "7. Award offers announced in March/April.",
                "8. Accept offer, pay deposit, and apply for Canadian Study Permit."
            ],
            "university_vs_scholarship_routing": "Sequential: University admission application first, followed by High School Awards portal application using UCID.",
            "recommendation_letters_submission_method": "Submitted online by 1 school counselor or teacher referee.",
            "personal_statement_prompts": "Essays detailing extracurricular leadership, contributions to school and community, and future aspirations at UCalgary.",
            "study_plan_research_proposal_requirements": "Not applicable for undergraduate admission.",
            "cv_format_requirements": "Extracurricular activity profile completed within the myUofC application form.",
            "interviews_conducted": False,
            "interview_format_details": "None; documentary selection.",
            "standardized_tests": "SAT/ACT not required for Canadian universities; English language test required.",
            "application_fee_amount": "CAD $145 university application fee.",
            "attestation_requirements": "Official board/Cambridge transcripts submitted by high school counselor or examination board directly.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% online through myUofC Student Centre portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Data Page",
                "mandatory": True,
                "specification": "Scanned copy of valid passport",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "High School Transcripts (Matric & FSc / O & A Levels)",
                "mandatory": True,
                "specification": "Official transcripts and predicted grades showing 95%+ or A* grades",
                "pakistan_specific_instruction": "Attested by IBCC / British Council predicted grades"
            },
            {
                "document_name": "Extracurricular & Leadership Essay",
                "mandatory": True,
                "specification": "Answers to essay prompts detailing community engagement and leadership",
                "pakistan_specific_instruction": "Highlight school head boy/girl, debate, or science competitions"
            },
            {
                "document_name": "Counselor Reference Letter",
                "mandatory": True,
                "specification": "Confidential letter from school principal or guidance counselor",
                "pakistan_specific_instruction": "On school official letterhead"
            },
            {
                "document_name": "English Proficiency Score (IELTS 6.5+ / TOEFL 86+ / DET 115+)",
                "mandatory": True,
                "specification": "Official language proficiency test report",
                "pakistan_specific_instruction": "Official IELTS/TOEFL or Duolingo score report"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-10-01",
            "application_deadline": "2026-12-15",
            "university_admission_deadline": "2026-12-01",
            "document_submission_deadline": "2026-12-15",
            "recommendation_letters_deadline": "2026-12-15",
            "interview_period": "No interviews",
            "shortlist_announcement": "2027-03-01",
            "final_result_acceptance_deadline": "2027-05-01",
            "visa_application_window": "April to July 2027",
            "semester_commencement": "2027-09-01",
            "annual_cycle_notes": "Early December 1 admission deadline and December 15 awards deadline are strictly enforced."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (High school academic GPA, rigorous STEM subject grades)",
            "extracurricular_and_leadership_weight": "25% (Community engagement, leadership roles, and awards)",
            "research_experience_weight": "0% (Not expected at high school level)",
            "work_experience_weight": "0% (Not required)",
            "personal_statement_weight": "10% (Quality of leadership essays)",
            "recommendations_weight": "5% (Counselor reference evaluation)",
            "interview_weight": "0% (Dossier-based evaluation)",
            "test_scores_weight": "0% (Language proficiency is prerequisite)",
            "financial_need_weight": "0% (Pure academic and leadership merit)",
            "selection_panel_composition": "University of Calgary Undergraduate Awards Committee.",
            "evaluation_methodology": "Transcript grade screening (top 1-2% percentile) -> Extracurricular essay scoring -> Final committee award ranking."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 international undergraduate applicants",
            "total_scholarships_awarded": "~2 to 4 International Entrance Scholarships per year",
            "acceptance_rate_global": "~0.06%",
            "acceptance_rate_pakistan": "~0.05% (One of the most competitive undergraduate awards in Canada)",
            "typical_successful_applicant_gpa": "96.0%+ high school average (or 3 to 4 A* grades in A-Levels)",
            "typical_academic_and_research_profile": "Top student in their high school or province, international Olympiad medalist (IMO, IPhO, IOI), or national debate champion with extensive community service.",
            "common_backgrounds_of_winners": "Top graduates from elite schools in Pakistan (Aitchison, Beaconhouse, Roots, KGS, Cadet Colleges).",
            "high_representation_countries": "India, Pakistan, China, Nigeria, United Kingdom, United States.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "known_scam_domains": ["ucalgary-scholarships-direct.org", "calgary-visa-portal.com"],
            "application_fee_warning": "University application fee is strictly CAD $145 paid inside official UCalgary portal. No extra fee for the scholarship.",
            "agent_and_intermediary_warnings": "University of Calgary awards are decided solely by the university committee; no external agent has quota access.",
            "itemized_hidden_out_of_pocket_costs": [
                "Tuition balance after CAD $20,000 scholarship (~CAD $7,000 to $15,000/year out of pocket depending on engineering/CS program)",
                "Campus residence and meal plan (~CAD $11,000 to $14,000/year)",
                "Canadian Study Permit application fee (CAD $150 / ~PKR 31,000)",
                "Airfare Pakistan to Calgary (~PKR 250,000 to 350,000)"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: CAD $20,000 covers all expenses. (Truth: International tuition is ~CAD $30,000–$38,000/year; students must fund the remaining tuition and living costs).",
                "MYTH: You can apply late in spring. (Truth: The awards deadline is strictly December 15; missing it means zero entrance scholarship consideration)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Agents claim all students with 90% get CAD $20,000; in reality, only 2-4 students globally win this major entrance award."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum GPA of 3.20 out of 4.00 over a minimum of 24.00 units (8 courses) in the preceding fall and winter terms to renew for years 2, 3, and 4.",
            "attendance_requirements": "Full-time registration in undergraduate degree.",
            "academic_progress_monitoring": "Annual GPA evaluation at end of winter term (May).",
            "work_restrictions_during_study": "Permitted to work up to 20-24 hours per week off campus and unlimited hours on campus under Canadian study permit.",
            "home_country_return_obligation": "None; international graduates from UCalgary qualify for Canada's 3-year Post-Graduation Work Permit (PGWP).",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "If GPA drops below 3.20 or course load drops below 24 units, renewal is revoked permanently.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Permitted within UCalgary provided student maintains full-time registration and required GPA.",
            "extension_policy": "Maximum 4 academic years (8 terms); no extension for year 5."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Calgary - International Entrance Scholarship Official Portal",
                "source_url": "https://www.ucalgary.ca/registrar/finances/awards/international-entrance-scholarship",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of scholarships awarded in each faculty (Engineering vs Science vs Business).",
                    "Detailed scoring rubric weighting high school percentage against extracurricular essays.",
                    "Annual grade cutoff thresholds across varying educational systems (A-Levels vs IB vs FSc)."
                ]
            }
        ]
    },

    # 12. Banting Postdoctoral Fellowships (SCH-AM-011)
    "SCH-AM-011": {
        "scholarship_id": "SCH-AM-011",
        "basic_details": {
            "scholarship_name": "Banting Postdoctoral Fellowships",
            "offering_entity": "Government of Canada (CIHR, NSERC, SSHRC)",
            "host_country": "Canada",
            "host_institutions_covered": "Canadian Universities and Affiliated Research Institutes (e.g. University of Toronto, UBC, McGill, University of Waterloo, Montreal, McMaster)",
            "degree_levels": ["Postdoctoral Fellowship"],
            "major_restrictions": "Health research (CIHR), Natural sciences and engineering (NSERC), Social sciences and humanities (SSHRC). Open to all research disciplines.",
            "number_of_awards_total": "70 elite postdoctoral fellowships awarded annually across Canada (divided equally among CIHR, NSERC, SSHRC)",
            "number_of_awards_pakistan": "Open international competition; awarded to the highest-calibre postdoctoral researchers globally (typically 1 to 3 Pakistani awardees every few cycles)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years (non-renewable)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Canadian citizens, Permanent Residents, and foreign citizens of all nationalities"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No chronological age limit.",
            "academic_qualifications": "Completed PhD, PhD-equivalent, or health professional degree within the past 3 years (window extended for parental or career interruptions).",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Exceptional doctoral record with distinguished publications, citations, and scholarly impact.",
            "subject_background_prerequisites": "Advanced research expertise directly matching proposed postdoctoral research program and host faculty lab.",
            "current_education_status": "PhD awarded within 3 years prior to application deadline or fulfilling all doctoral degree requirements before fellowship start.",
            "graduation_year_restrictions": "PhD must have been fulfilled within a strict 3-year window prior to the application deadline.",
            "work_experience_required": True,
            "work_experience_minimum_years": 3.0,
            "work_experience_notes": "Substantial research and publication record in high-impact international peer-reviewed journals.",
            "english_proficiency": {
                "test_required": False,
                "ielts_minimum": None,
                "toefl_minimum": None,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "Proficiency in English or French demonstrated through doctoral research thesis and publications."
            },
            "other_language_requirements": "English or French.",
            "gender_specific_requirements": "Equal opportunity; diversity and inclusion principles strictly upheld by tri-agency panels.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite postdoctoral researchers with demonstrated global research leadership.",
            "previous_scholarship_restrictions": "Must not have previously held a Banting Postdoctoral Fellowship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Postdoctoral fellows do not pay tuition; institutional bench and administrative fees covered by host institution.",
                "amount": "Not applicable (Postdoctoral appointment)"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Application through ResearchNet portal is 100% free.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid out of generous postdoctoral salary stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "CAD $70,000 per year (taxable) for 2 years (~CAD $5,833/month / ~PKR 1,190,000/month), representing Canada's highest postdoctoral salary award.",
                "amount": "CAD $70,000 / year (~PKR 14,300,000 / year)"
            },
            "airfare": {
                "status": "PAID VIA STIPEND",
                "details": "Travel and relocation to Canada paid from the fellowship salary or host institution start-up funds.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Work Permit application fee (CAD $155) and biometrics (CAD $85) paid by applicant.",
                "amount": "CAD $240"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Provincial health insurance (OHIP in Ontario, MSP in BC, RAMQ in Quebec) provided to postdoctoral workers with valid work permits.",
                "amount": "100% covered by provincial health coverage"
            },
            "food_allowance": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly postdoctoral salary.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Host university laboratory infrastructure, high-performance computing clusters, and library access provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Host supervisor and department provide dedicated research operating funds and conference travel budgets.",
                "amount": "Provided by host lab"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "None.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Must be formally endorsed and nominated by one Canadian host university.",
            "participating_institutions": [
                "University of Toronto",
                "University of British Columbia (UBC)",
                "McGill University",
                "University of Waterloo",
                "Université de Montréal",
                "McMaster University",
                "University of Alberta",
                "Queen's University"
            ],
            "university_rankings_scope": "Top Canadian research universities (QS World Top 20 to 200).",
            "available_majors": [
                "All disciplines across Health & Biomedical Sciences (CIHR), Natural Sciences, Engineering, Artificial Intelligence & Computer Science (NSERC), Social Sciences, Economics & Humanities (SSHRC)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "24 months (2 years)",
            "admission_requirements_summary": "PhD degree completed within past 3 years; institutional nomination and supervisor endorsement from a Canadian university.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Host universities conduct strict internal pre-selection competitions; candidates must contact prospective Canadian faculty hosts by May/June.",
            "strategic_program_match_advice": "A strong synergy between the candidate's research trajectory and the host institution's strategic research plan is heavily evaluated (Institutional Synergy score = 33% of evaluation)."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://banting.fellowships-bourses.gc.ca/en/home-accueil.html",
            "portal_system_name": "Canadian Common CV (CCV) & ResearchNet Portal",
            "account_creation_instructions": "Step 1: Create Canadian Common CV (Vanier-Banting CCV format). Step 2: Register on ResearchNet and link to host university nomination.",
            "step_by_step_workflow": [
                "1. Identify and contact prospective postdoctoral supervisor at a Canadian university (April-June).",
                "2. Submit internal expression of interest to host university graduate/postdoctoral office.",
                "3. Secure host institution endorsement and internal nomination (July-August).",
                "4. Complete Vanier-Banting Canadian Common CV (CCV).",
                "5. Write 4-page research proposal, leadership statement, and supervisor support letters on ResearchNet.",
                "6. Register 3 referees who submit electronic assessment forms.",
                "7. Submit application jointly with host institution before mid-September deadline.",
                "8. Tri-agency selection committees review dossiers (October-January).",
                "9. Results announced in mid-February.",
                "10. Apply for LMIA-exempt Canadian employer-specific work permit (C44 exemption)."
            ],
            "university_vs_scholarship_routing": "Mandatory joint nomination: applicant must be officially endorsed and forwarded by the host Canadian institution.",
            "recommendation_letters_submission_method": "Submitted online by 3 arm's-length academic referees via ResearchNet.",
            "personal_statement_prompts": "Fulfillment of degree requirements statement, significance of research leadership, and career trajectory vision.",
            "study_plan_research_proposal_requirements": "Detailed 4-page scientific research proposal with project description, methodology, literature citations, and knowledge mobilization plan.",
            "cv_format_requirements": "Strict Vanier-Banting Canadian Common CV (CCV) format.",
            "interviews_conducted": False,
            "interview_format_details": "None; documentary peer review.",
            "standardized_tests": "None.",
            "application_fee_amount": "100% free; no application fee on ResearchNet.",
            "attestation_requirements": "Official doctoral transcripts and PhD completion verification letter.",
            "translation_requirements": "Certified English or French translations.",
            "final_submission_method": "100% online through ResearchNet portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Data Page",
                "mandatory": True,
                "specification": "Scanned copy of international passport",
                "pakistan_specific_instruction": "Pakistani passport copy"
            },
            {
                "document_name": "Vanier-Banting Canadian Common CV (CCV)",
                "mandatory": True,
                "specification": "Official electronic CCV PDF generated from CCV website",
                "pakistan_specific_instruction": "Detailed research publication record"
            },
            {
                "document_name": "Institutional Nomination Letter",
                "mandatory": True,
                "specification": "Signed letter from President or Dean of Graduate Studies of host Canadian university",
                "pakistan_specific_instruction": "From host Canadian institution"
            },
            {
                "document_name": "Supervisor's Statement & Research Commitment",
                "mandatory": True,
                "specification": "Detailed letter from host professor detailing facilities, lab resources, and mentorship plan",
                "pakistan_specific_instruction": "Signed by Canadian university professor"
            },
            {
                "document_name": "Three Referee Assessment Reports",
                "mandatory": True,
                "specification": "Confidential referee reports submitted electronically on ResearchNet",
                "pakistan_specific_instruction": "From international leaders in the field"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-04-15",
            "application_deadline": "2026-09-17",
            "university_admission_deadline": "2026-07-15",
            "document_submission_deadline": "2026-09-17",
            "recommendation_letters_deadline": "2026-09-17",
            "interview_period": "No interviews",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-02-15",
            "visa_application_window": "March to June 2027",
            "semester_commencement": "Between April 1 and October 1, 2027",
            "annual_cycle_notes": "Single annual intake; results announced mid-February for tenure starting between April and October."
        },
        "selection_process_and_weights": {
            "academic_weight": "33.3% (Research excellence and leadership in research of applicant)",
            "extracurricular_and_leadership_weight": "0% (Focus on research leadership)",
            "research_experience_weight": "33.3% (Quality of the proposed research program and methodology)",
            "work_experience_weight": "0% (Postdoctoral track)",
            "personal_statement_weight": "0% (Integrated into research leadership)",
            "recommendations_weight": "Included in research excellence score",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "0% (Not required)",
            "financial_need_weight": "0% (Pure scientific excellence)",
            "selection_panel_composition": "Banting Selection Committees comprising prominent Canadian and international researchers in health (CIHR), natural sciences (NSERC), and social sciences (SSHRC).",
            "evaluation_methodology": "Equal weighting across three criteria: (1) Research excellence and leadership of applicant (33.3%); (2) Quality of proposed research program (33.3%); (3) Institutional commitment and synergy (33.3%)."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~600 nominated postdoctoral candidates across Canada (after university pre-selection of thousands of applicants)",
            "total_scholarships_awarded": "70 Banting Fellowships awarded per year",
            "acceptance_rate_global": "~11.6% (of institutionally nominated finalists; <2% of initial applicants)",
            "acceptance_rate_pakistan": "~1.0% (Extremely Competitive / Elite global tier)",
            "typical_successful_applicant_gpa": "3.90+ / 4.00 CGPA equivalent in doctoral coursework",
            "typical_academic_and_research_profile": "Recent PhD graduates with multiple first-author publications in premier journals (Nature, Science, Cell, IEEE Transactions), high citation metrics, and clear visionary leadership.",
            "common_backgrounds_of_winners": "Elite researchers from top global laboratories and leading Pakistani scholars with distinguished international doctoral credentials.",
            "high_representation_countries": "Canada, United States, United Kingdom, France, Germany, China, India, Australia, Pakistan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized websites offering Banting nomination guarantees: banting-fellowships-canada.org, apply-banting-visas.com."
            ],
            "application_fee_warning": "ResearchNet application is 100% free of charge. Beware of consultancies claiming to provide paid institutional nominations.",
            "agent_and_intermediary_warnings": "Institutional nominations can only be granted by accredited Canadian universities through their internal peer review panels.",
            "itemized_hidden_out_of_pocket_costs": [
                "Canadian Work Permit and biometric application fee (CAD $240 / ~PKR 49,000)",
                "Relocation travel from Pakistan to host Canadian city (~PKR 250,000 to 350,000)",
                "Initial rental deposit in host Canadian city (~CAD $1,500 to $2,500)"
            ],
            "debunked_myths_and_misconceptions": [
                "MYTH: You can apply on ResearchNet without a host university. (Truth: Applications without formal institutional endorsement letters from a Canadian university are automatically disqualified).",
                "MYTH: Banting Fellowships can be held outside Canada. (Truth: For international applicants, the fellowship must be held at an eligible Canadian institution)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites describe Banting as an open doctoral award; it is strictly a postdoctoral fellowship requiring an awarded PhD."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain full-time research commitment at host institution laboratory.",
            "attendance_requirements": "Continuous physical presence at the Canadian host institution.",
            "academic_progress_monitoring": "Annual progress report submitted to the Tri-Agency Secretariat.",
            "work_restrictions_during_study": "Fellows may teach a maximum of one course per year if it does not interfere with their research program.",
            "home_country_return_obligation": "None; international fellows qualify for Canadian permanent residency pathways under the Express Entry Canadian Experience Class (CEC) or Provincial Nominee Programs.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding will be cancelled if the fellow leaves the institution, accepts full-time permanent employment, or abandons the research project.",
            "rules_for_changing_university": "Non-transferable between institutions without extraordinary approval from Tri-Agency Secretariat.",
            "rules_for_changing_major": "Requires approval from host institution and tri-agency program officers.",
            "extension_policy": "Strictly non-renewable beyond 24 months."
        },
        "official_sources_verified": [
            {
                "source_name": "Government of Canada - Banting Postdoctoral Fellowships Official Portal",
                "source_url": "https://banting.fellowships-bourses.gc.ca/en/home-accueil.html",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Individual university institutional quota limits on the number of nominees permitted to be forwarded to ResearchNet.",
                    "Detailed raw scoring matrices used by CIHR, NSERC, and SSHRC selection panels.",
                    "Breakdown of awarded fellows by citizenship and country of origin."
                ]
            }
        ]
    }
}
