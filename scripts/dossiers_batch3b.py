"""
scripts/dossiers_batch3b.py
Part B of Batch 3:
5. SCH-AS-006: Singapore International Graduate Award (SINGA, Singapore)
6. SCH-AS-007: Taiwan ICDF International Higher Education Scholarship (Taiwan)
7. SCH-AS-008: Government of Brunei Darussalam Scholarship (BDGS, Brunei)
8. SCH-AS-009: Asian Development Bank - Japan Scholarship Program (ADB-JSP)
"""

DOSSIERS_BATCH3B = {
    # 5. Singapore International Graduate Award (SINGA) (SCH-AS-006)
    "SCH-AS-006": {
        "scholarship_id": "SCH-AS-006",
        "basic_details": {
            "scholarship_name": "Singapore International Graduate Award (SINGA)",
            "offering_entity": "Agency for Science, Technology and Research (A*STAR), in collaboration with NTU, NUS, SUTD, and SMU",
            "host_country": "Singapore",
            "host_institutions_covered": "National University of Singapore (NUS), Nanyang Technological University (NTU), Singapore University of Technology and Design (SUTD), Singapore Management University (SMU), and A*STAR Research Institutes",
            "degree_levels": ["PhD (Doctorate)"],
            "major_restrictions": "Biomedical Sciences, Computing and Information Sciences, Physical Sciences, and Engineering.",
            "number_of_awards_total": "~240 PhD awards annually across two intake cycles (January and August)",
            "number_of_awards_pakistan": "Open to all international graduates based on academic and research merit (~15 to 25 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years of PhD study"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International graduates of all nationalities (including Pakistan) with passion for research"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (4-year Bachelor's degree with honours) or 18 years (Master's degree) from an HEC-recognized university.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum 3.50 / 4.00 CGPA; competitive admitted candidates typically hold 3.70+ / 4.00 CGPA or top 5% class ranking.",
            "subject_background_prerequisites": "Degree in Science, Technology, Engineering, Computing, or Biomedical Sciences.",
            "current_education_status": "Graduated or in final year of undergraduate or master's studies.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications, laboratory research projects, and conference presentations provide substantial competitive advantage.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "IELTS Academic minimum 6.5 or TOEFL iBT 85; or university English proficiency certificate for initial application, though test scores are strongly recommended."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite scientific research potential.",
            "previous_scholarship_restrictions": "Must not already hold a PhD.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fees waived for the entire 4 years of PhD studies.",
                "amount": "SGD $40,000 to $45,000 / year"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application via the SINGA portal is free of charge.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Campus housing in graduate residences paid from monthly stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "SGD $2,700/month initially, increased to SGD $3,200/month after passing the PhD Qualifying Examination (typically at 12-18 months).",
                "amount": "SGD $2,700 - $3,200 / month (~PKR 590,000 to 700,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One-time airfare grant of up to SGD $1,500 provided upon initial arrival.",
                "amount": "Up to SGD $1,500 (~PKR 330,000)"
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Singapore Student's Pass processing and issuance fees covered.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "University student medical and hospitalization insurance covered.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered from living allowance.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Research laboratory operational funding and conference grants provided through A*STAR or university research grants.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "One-time settling-in allowance of SGD $1,000 paid upon arrival.",
                "amount": "SGD $1,000 (~PKR 220,000)"
            },
            "total_estimated_value_usd_per_year": 55000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for research projects under A*STAR institutes and partner universities (NUS, NTU, SUTD, SMU).",
            "participating_institutions": [
                "National University of Singapore (NUS - World #8)",
                "Nanyang Technological University (NTU - World #15)",
                "Singapore University of Technology and Design (SUTD)",
                "Singapore Management University (SMU)",
                "A*STAR Research Institutes (GIS, BII, IMB, I2R, IMRE, IHPC, SIMTech)"
            ],
            "university_rankings_scope": "NUS and NTU are consistently ranked Top 15 globally in QS World Rankings.",
            "available_majors": [
                "Artificial Intelligence, Machine Learning, Robotics, Computer Science, Data Science, Materials Science, Nanoelectronics, Mechanical Engineering, Chemical Engineering, Bioengineering, Molecular Biology, Immunology, Quantum Technology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 continuous years of PhD research",
            "admission_requirements_summary": "Single application via the SINGA online portal; candidates select preferred research supervisor and university.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Browsing the A*STAR researcher directory and identifying prospective supervisors whose lab matches your skills is highly advantageous.",
            "strategic_program_match_advice": "Candidates can choose to be based primarily in an A*STAR research institute while receiving their degree from NUS, NTU, or SUTD."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.a-star.edu.sg/Scholarships/for-graduate-studies/singapore-international-graduate-award-singa",
            "portal_system_name": "A*STAR SINGA Online Application Portal",
            "account_creation_instructions": "Register on the SINGA portal, explore research projects across A*STAR/NUS/NTU/SUTD, select up to 3 project choices, and designate two referees.",
            "step_by_step_workflow": [
                "1. Search eligible PhD research projects and supervisors on the A*STAR website.",
                "2. Create account on the SINGA application portal (Two deadlines: June 1 for January intake, December 1 for August intake).",
                "3. Submit research project choices and upload academic transcripts, degree certificates, and CV.",
                "4. Referees submit online reference reports via automated email link.",
                "5. Shortlisted candidates invited for virtual or in-person technical interviews in July/August or January/February.",
                "6. Final award outcomes notified within 1-2 months after interview.",
                "7. Process Singapore Student's Pass and relocate to Singapore."
            ],
            "university_vs_scholarship_routing": "Direct single application via A*STAR SINGA portal.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure link generated by SINGA system.",
            "personal_statement_prompts": "Address your passion for research, previous scientific project contributions, and career objectives.",
            "study_plan_research_proposal_requirements": "Summary of research interests and alignment with selected A*STAR / university research projects.",
            "cv_format_requirements": "Standard academic CV highlighting laboratory skills, research projects, publications, and programming proficiencies.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous 30-minute technical interview conducted by a panel of A*STAR senior scientists and university professors testing fundamentals and research logic.",
            "standardized_tests": "GRE not mandatory but evaluated positively; English proficiency test required.",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Certified transcripts and degree certificates; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via SINGA portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Academic Transcripts & Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for Bachelor's and Master's degrees with grading system",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Reports",
                "mandatory": True,
                "specification": "Submitted directly by university research professors via the portal",
                "pakistan_specific_instruction": "From professors who supervised your thesis or research projects"
            },
            {
                "document_name": "Passport Copy",
                "mandatory": True,
                "specification": "Valid Pakistani passport photo page",
                "pakistan_specific_instruction": "Valid for at least 2 years"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "Detailed academic CV with full list of publications",
                "pakistan_specific_instruction": "Highlighting lab methods and code repositories"
            },
            {
                "document_name": "English Proficiency Score",
                "mandatory": False,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (85+) or MOI certificate",
                "pakistan_specific_instruction": "Official test report strongly recommended for competitive ranking"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-06-01",
            "application_deadline": "2026-12-01",
            "university_admission_deadline": "2026-12-01",
            "document_submission_deadline": "2026-12-01",
            "recommendation_letters_deadline": "2026-12-08",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "August 2027 (August intake)",
            "annual_cycle_notes": "Two annual intake cycles: Deadline June 1 for January intake; Deadline December 1 for August intake."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic track record, grades, foundational mastery in mathematics/sciences)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "40% (Demonstrated research curiosity, laboratory skills, thesis, publications)",
            "work_experience_weight": "5% (R&D experience)",
            "personal_statement_weight": "5% (Clarity of scientific purpose)",
            "recommendations_weight": "10% (Referee appraisals of research potential)",
            "interview_weight": "Decisive: Performance in technical panel interview",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "Joint interviewing panels comprising A*STAR executive scientists and university department faculty heads.",
            "evaluation_methodology": "Two-tier review: Shortlisting based on academic and research dossier; final selection via rigorous live technical interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~6,000 to 7,000 applications globally across both intake cycles",
            "total_scholarships_awarded": "~240 PhD scholarships awarded annually",
            "acceptance_rate_global": "~3.5% to 4%",
            "acceptance_rate_pakistan": "~2% to 3% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.70 to 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates with deep scientific problem-solving abilities, research publications in international journals, and exceptional technical interview skills.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (NUST, LUMS, GIKI, Quaid-i-Azam, FAST, UET) in engineering, computer science, and biotechnology.",
            "high_representation_countries": "China, India, Pakistan, Vietnam, Malaysia, Indonesia, Iran.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial coaching firms charging money claiming they have 'internal interview questions' for SINGA."
            ],
            "application_fee_warning": "SINGA application is 100% free of charge. Never pay any fee.",
            "agent_and_intermediary_warnings": "A*STAR strictly audits applications; applications submitted via agents are disqualified.",
            "hidden_costs_breakdown": [
                "English language test fees (IELTS/TOEFL) if taken.",
                "Medical checkup in Singapore upon arrival (~SGD $60 to $100).",
                "First month's room deposit before first stipend release."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must have a Master's degree to apply. (Fact: Direct bachelor's-to-PhD applicants are fully eligible and frequently selected).",
                "MYTH: There is a service bond to work in Singapore. (Fact: SINGA has NO post-graduation bond; graduates can pursue careers in Singapore, Pakistan, or globally)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites quote old stipend figures (SGD $2,000); official rate is now SGD $2,700/month, increasing to SGD $3,200/month after qualifying exam."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum CAP/GPA required by host university (minimum 3.5/5.0 at NUS/NTU) and pass PhD Qualifying Exam.",
            "attendance_requirements": "Full-time physical research attendance in Singapore laboratories.",
            "academic_progress_monitoring": "Semi-annual progress reports submitted to A*STAR Graduate Academy.",
            "work_restrictions_during_study": "Scholars are not permitted to engage in paid employment outside their research program without formal approval.",
            "home_country_return_obligation": "None; SINGA carries NO bond or service obligation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Failing doctoral qualifying exams or premature resignation requires repayment of scholarship allowances in certain breach cases.",
            "rules_for_changing_university": "Non-transferable between universities.",
            "rules_for_changing_major": "Requires approval from A*STAR and both university departments.",
            "extension_policy": "Strictly funded for up to 4 years; beyond 4 years requires laboratory funding."
        },
        "official_sources_verified": [
            {
                "source_name": "Agency for Science, Technology and Research (A*STAR) - SINGA Official Portal",
                "source_url": "https://www.a-star.edu.sg/Scholarships/for-graduate-studies/singapore-international-graduate-award-singa",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation ratio of students between A*STAR research institutes and university departments",
                    "Interview grading sheet details"
                ]
            }
        ]
    },

    # 6. Taiwan ICDF International Higher Education Scholarship (SCH-AS-007)
    "SCH-AS-007": {
        "scholarship_id": "SCH-AS-007",
        "basic_details": {
            "scholarship_name": "Taiwan ICDF International Higher Education Scholarship",
            "offering_entity": "International Cooperation and Development Fund (Taiwan ICDF)",
            "host_country": "Taiwan",
            "host_institutions_covered": "23 partner universities in Taiwan (National Taiwan University, National Tsing Hua, National Cheng Kung, National Yang Ming Chiao Tung, National Central University)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Open to designated English-taught programs across Science & Technology, Agriculture, Public Health & Medicine, Business & Management, and Humanities & Social Sciences.",
            "number_of_awards_total": "~200 to 250 scholarships awarded annually across partner developing countries",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible partner developing country (~10 to 15 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's (max 4 years); Master's (max 2 years); PhD (max 4 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of eligible partner countries (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No specific age limits.",
            "academic_qualifications": "12 years for Bachelor's; 16 years for Master's; 18 years for PhD from an HEC-recognized institution.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA or 75%+ marks; good academic background in chosen field.",
            "subject_background_prerequisites": "Prerequisites corresponding to designated ICDF partner university degree programs.",
            "current_education_status": "Graduated or in final year of degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior work experience in public service or development sectors valued.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 75,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "IELTS Academic 6.0+, TOEFL iBT 75+, or university English proficiency certificate verifying prior study was conducted in English."
            },
            "other_language_requirements": "None; all designated programs taught 100% in English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Development impact and bilateral cultural exchange.",
            "previous_scholarship_restrictions": "Cannot hold another scholarship from the government of Taiwan concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition and credit fees covered directly by Taiwan ICDF.",
                "amount": "NT$ 60,000 to NT$ 120,000 / year"
            },
            "admission_application_fee": {
                "status": "WAIVED_OR_COVERED",
                "details": "Partner universities waive or reimburse application fees for ICDF scholars.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE DORMITORY",
                "details": "Free standard on-campus student dormitory accommodation covered by Taiwan ICDF.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly subsistence allowance paid directly to student to cover food and living expenses.",
                "amount": "Undergrad: NT$ 15,000/mo; Master: NT$ 18,000/mo (~PKR 160,000/mo); PhD: NT$ 20,000/mo (~PKR 180,000/mo)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy class return flights between Pakistan and Taiwan booked via most direct route.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Taiwan resident visa fee paid by applicant at Taipei Trade Office.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "National Health Insurance (NHI) and student accidental insurance fully covered.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Textbook costs covered directly through university partner department.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Research laboratory resources accessible across partner university labs.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Personal responsibility.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for one program among the designated Taiwan ICDF partner universities.",
            "participating_institutions": [
                "National Taiwan University (NTU - Taipei)",
                "National Tsing Hua University (NTHU - Hsinchu)",
                "National Cheng Kung University (NCKU - Tainan)",
                "National Yang Ming Chiao Tung University (NYCU)",
                "National Central University (NCU)", "National Chung Hsing University (NCHU)"
            ],
            "university_rankings_scope": "National Taiwan University is World Top 70; premier semiconductor and engineering ecosystem.",
            "available_majors": [
                "Electrical Engineering, Computer Science, Semiconductor Technology, Mechanical Engineering, Tropical Agriculture, Aquaculture, Global Health, Biomedical Informatics, Civil Engineering, International Business, Environment & Sustainable Development"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4 years; Master's: 2 years; PhD: 4 years",
            "admission_requirements_summary": "Two-step application: Submit online application on the Taiwan ICDF portal; simultaneously submit university admission application to the partner university.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Must apply to both the ICDF portal AND the chosen partner university before their respective deadlines.",
            "strategic_program_match_advice": "Semiconductor, Electrical Engineering, and Agriculture programs in Taiwan are globally renowned."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.icdf.org.tw/wSite/np?ctNode=31561&mp=2",
            "portal_system_name": "Taiwan ICDF Online Scholarship Application System",
            "account_creation_instructions": "Register on the ICDF online application portal (Opens January), fill out application form, upload documents, and print application summary.",
            "step_by_step_workflow": [
                "1. Choose eligible program from the official Taiwan ICDF partner program list (Opens January 1).",
                "2. Complete online application on Taiwan ICDF portal by March 15.",
                "3. Submit separate online application for admission to the chosen partner university by the university's deadline.",
                "4. Submit printed application form and required documents to the nearest designated Taipei Trade Office / Mission if required.",
                "5. Partner universities review academic credentials and submit recommendations to ICDF in April/May.",
                "6. Final list of scholarship recipients announced by Taiwan ICDF by June 10.",
                "7. Process Taiwan resident visa and prepare for departure in August/September."
            ],
            "university_vs_scholarship_routing": "Dual application: Apply on ICDF portal AND apply to partner university.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate on the portal or sent via email.",
            "personal_statement_prompts": "Study Plan / Statement of Purpose detailing academic background, reasons for choosing Taiwan, and future contributions to national development.",
            "study_plan_research_proposal_requirements": "Research proposal required for PhD applicants.",
            "cv_format_requirements": "Standard professional resume (1-2 pages).",
            "interviews_conducted": True,
            "interview_format_details": "Partner university or Taipei Representative Office may conduct video interviews in April/May.",
            "standardized_tests": "English proficiency test required (IELTS/TOEFL/MOI).",
            "application_fee_amount": "$0 on ICDF portal; university application fees usually waived.",
            "attestation_requirements": "Diplomas and transcripts must be authenticated by HEC and MOFA Pakistan, and verified by Taipei Economic and Cultural Center.",
            "translation_requirements": "Certified English or Chinese translations.",
            "final_submission_method": "Online via ICDF portal and university portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Taiwan ICDF Online Application Form",
                "mandatory": True,
                "specification": "Completed and signed application form printed from ICDF portal",
                "pakistan_specific_instruction": "Signed copy uploaded to portal"
            },
            {
                "document_name": "Academic Diplomas & Transcripts",
                "mandatory": True,
                "specification": "Notarized copies of educational diplomas and mark sheets",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from university professors or employers on official letterhead",
                "pakistan_specific_instruction": "Signed and stamped"
            },
            {
                "document_name": "English Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (6.0+), TOEFL iBT (75+), or official MOI certificate",
                "pakistan_specific_instruction": "Valid test certificate"
            },
            {
                "document_name": "Copy of Passport",
                "mandatory": True,
                "specification": "Valid Pakistani passport photo page",
                "pakistan_specific_instruction": "Valid for at least 1 year"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-01-01",
            "application_deadline": "2027-03-15",
            "university_admission_deadline": "2027-03-15",
            "document_submission_deadline": "2027-03-15",
            "recommendation_letters_deadline": "2027-03-15",
            "interview_period": "April to May 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-06-20",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "Application window is January 1 to March 15 each year. Final results announced by June 10."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic record, undergraduate GPA, grading scale)",
            "extracurricular_and_leadership_weight": "10% (Leadership and community involvement)",
            "research_experience_weight": "20% (For Master's/PhD: research background and proposal)",
            "work_experience_weight": "10% (Professional relevance)",
            "personal_statement_weight": "10% (Study plan and development goals)",
            "recommendations_weight": "10% (Referee appraisals)",
            "interview_weight": "Evaluated during university review",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "Joint assessment by partner university admissions committee and the Taiwan ICDF Scholarship Committee.",
            "evaluation_methodology": "Two-tier review: Partner university checks academic admissibility; ICDF confirms scholarship award."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,000 to 4,000 applicants across all partner countries",
            "total_scholarships_awarded": "~200 to 250 scholarships awarded annually",
            "acceptance_rate_global": "~6%",
            "acceptance_rate_pakistan": "~4% to 5% (Favorable conversion for strong STEM profiles)",
            "typical_successful_applicant_gpa": "3.30 to 3.85 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Solid graduates with degrees in engineering, agriculture, IT, or public health seeking world-class technical education.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (NUST, UET Lahore, Faisalabad Agricultural University, COMSATS, Quaid-i-Azam).",
            "high_representation_countries": "Southeast Asian, South Asian, African, and Latin American partner countries.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents claiming to sell Taiwan ICDF application forms."
            ],
            "application_fee_warning": "The ICDF scholarship application is 100% free of charge.",
            "agent_and_intermediary_warnings": "Never work through commercial consultants; submit directly on the official ICDF portal.",
            "hidden_costs_breakdown": [
                "Taiwan Resident Visa processing fee (~USD $66).",
                "Document authentication fees in Islamabad.",
                "Initial pocket money before first stipend transfer."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must speak Mandarin Chinese. (Fact: All designated Taiwan ICDF scholarship programs are taught 100% in English).",
                "MYTH: You only need to apply on the ICDF portal. (Fact: You MUST also submit a university admission application to the partner university)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs state the stipend is NT$ 30,000; the official rate is NT$ 15,000 for BS, NT$ 18,000 for MS, and NT$ 20,000 for PhD alongside free tuition and dorm."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum academic average required by the host university (typically 70%+ or GPA 3.0/4.0).",
            "attendance_requirements": "Full-time physical enrollment on campus in Taiwan.",
            "academic_progress_monitoring": "Host universities submit semester grade reports to Taiwan ICDF.",
            "work_restrictions_during_study": "Scholars may work part-time up to 20 hours/week with a work permit during semesters per Taiwan regulations.",
            "home_country_return_obligation": "None; scholars can seek employment in Taiwan's technology sector post-graduation under Taiwan work permit schemes.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Failing academic requirements or expulsion leads to termination of scholarship.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "No extensions beyond normal program duration."
        },
        "official_sources_verified": [
            {
                "source_name": "International Cooperation and Development Fund (Taiwan ICDF) - Scholarships Portal",
                "source_url": "https://www.icdf.org.tw/wSite/np?ctNode=31561&mp=2",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Diplomatic quota allocation numbers per partner country",
                    "Partner university evaluation scoring matrix"
                ]
            }
        ]
    },

    # 7. Government of Brunei Darussalam Scholarship (BDGS) (SCH-AS-008)
    "SCH-AS-008": {
        "scholarship_id": "SCH-AS-008",
        "basic_details": {
            "scholarship_name": "Government of Brunei Darussalam Scholarship (BDGS)",
            "offering_entity": "Ministry of Foreign Affairs (MFA), Government of Brunei Darussalam",
            "host_country": "Brunei Darussalam",
            "host_institutions_covered": "Universiti Brunei Darussalam (UBD), Universiti Islam Sultan Sharif Ali (UNISSA), Universiti Teknologi Brunei (UTB), and Politeknik Brunei (PB)",
            "degree_levels": ["Undergraduate (Bachelor's)", "Master's", "Diploma"],
            "major_restrictions": "Open to degree programs offered across the 4 institutions: Engineering, Computer Science, Business, Economics, Petroleum Geosciences, Public Policy, Islamic Studies, Islamic Finance, Health Sciences.",
            "number_of_awards_total": "~100 to 150 scholarships awarded annually across ASEAN, Commonwealth, and OIC member countries",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible OIC and Commonwealth member state (~5 to 10 Pakistani students selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Diploma (3 years); Bachelor's (4 years); Master's (1 to 2 years)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of ASEAN, Commonwealth, and OIC member countries (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate and Diploma: between 18 and 25 years of age; Master's: maximum 35 years of age on July 1 of award year.",
            "academic_qualifications": "12 years (FSc/A-Levels) for Bachelor's; 16 years (Bachelor's) for Master's from an accredited institution.",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA or equivalent Second Class Upper / 70%+ marks.",
            "subject_background_prerequisites": "Prerequisites corresponding to chosen degree faculty.",
            "current_education_status": "Graduated or in final semester of degree.",
            "graduation_year_restrictions": "None, provided age limits are respected.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Academic grades carry primary weight.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.0,
                "toefl_minimum": 75,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "Credit 6 in GCE O-Level English, IELTS Academic 6.0+, TOEFL 75+, or university English proficiency certificate."
            },
            "other_language_requirements": "English; Arabic required for Islamic Studies programs at UNISSA.",
            "gender_specific_requirements": "Equal opportunity; all eligible candidates welcome.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must be nominated by their home government (Ministry of Foreign Affairs or designated agency in Pakistan).",
            "previous_scholarship_restrictions": "Cannot hold another scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% tuition, admission, examination, registration, and orientation fees fully waived.",
                "amount": "BND $8,000 to $16,000 / year"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "No application fees charged.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE DORMITORY",
                "details": "Free accommodation at the residential college of the host university or polytechnic.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly personal subsistence allowance paid directly to student.",
                "amount": "BND $500 / month (~PKR 110,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy class return airfare to Brunei Darussalam at the beginning and end of study.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Student visa and student pass fees in Brunei Darussalam covered.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive medical insurance provided throughout the scholarship period.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Monthly meals allowance of BND $150/month provided in addition to personal allowance.",
                "amount": "BND $150 / month (~PKR 33,000 / month)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Annual book allowance paid directly to scholar.",
                "amount": "BND $600 / year (~PKR 132,000 / year)"
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "Host university research laboratories accessible.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Baggage allowance for shipping personal effects upon completion (up to BND $500).",
                "amount": "BND $500"
            },
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for up to two program choices across the 4 participating institutions.",
            "participating_institutions": [
                "Universiti Brunei Darussalam (UBD - World Top 400)",
                "Universiti Teknologi Brunei (UTB - Engineering & Tech)",
                "Universiti Islam Sultan Sharif Ali (UNISSA - Islamic Studies & Law)",
                "Politeknik Brunei (PB - Technical Diplomas)"
            ],
            "university_rankings_scope": "UBD is QS World Rank #387; UTB is World Top 500.",
            "available_majors": [
                "Computer Science, Electrical & Electronic Engineering, Mechanical Engineering, Civil Engineering, Petroleum Engineering, Chemical Engineering, Business Administration, Economics, Public Policy, Biomedical Sciences, Islamic Finance, Shariah Law"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Diploma: 3 years; Bachelor's: 4 years; Master's: 1 to 2 years",
            "admission_requirements_summary": "Download official BDGS application form, fill out choices, obtain home government endorsement, and submit via email/portal to MFA Brunei.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Universiti Teknologi Brunei (UTB) and Universiti Brunei Darussalam (UBD) are the premier choices for engineering and sciences.",
            "strategic_program_match_advice": "Ensure Section C of the application form is endorsed by the Ministry of Foreign Affairs (MOFA) Pakistan or the HEC."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.mfa.gov.bn/Pages/bdgs/bdgs2024.aspx",
            "portal_system_name": "Ministry of Foreign Affairs Brunei BDGS Online Submission",
            "account_creation_instructions": "Download the official application form from the MFA Brunei website, complete all sections, attach documents, and submit via the specified online portal or email.",
            "step_by_step_workflow": [
                "1. Download the official BDGS Application Form from MFA Brunei website (Opens January).",
                "2. Complete the form and choose up to two degree programs from UBD, UTB, UNISSA, or PB.",
                "3. Secure Statement of Purpose and certified academic transcripts.",
                "4. Submit the form to MOFA Pakistan / HEC for official government endorsement (Section C).",
                "5. Email/upload the complete endorsed application to queriesbdgs2024@mfa.gov.bn by deadline (mid-February).",
                "6. Shortlisted applicants may be invited to sit an interview/written test by Brunei selection panel.",
                "7. Award letters issued in June/July; semester commences in August."
            ],
            "university_vs_scholarship_routing": "Direct application via MFA Brunei; admissions are processed centrally.",
            "recommendation_letters_submission_method": "Two referee assessments submitted with the application dossier.",
            "personal_statement_prompts": "Statement of Purpose describing academic interests, why you chose Brunei, and how your studies will benefit your home country.",
            "study_plan_research_proposal_requirements": "Research proposal required for Master's by Research candidates.",
            "cv_format_requirements": "Standard academic CV.",
            "interviews_conducted": True,
            "interview_format_details": "Selection committee or host university conducts virtual interview for shortlisted candidates in April/May.",
            "standardized_tests": "English test (IELTS 6.0+ or TOEFL 75+).",
            "application_fee_amount": "$0 (100% Free).",
            "attestation_requirements": "Certificates and transcripts must be certified; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "Submitted electronically via email / portal to MFA Brunei."
        },
        "required_documents_checklist": [
            {
                "document_name": "BDGS Application Form with Government Endorsement",
                "mandatory": True,
                "specification": "Official form completed and endorsed by Ministry of Foreign Affairs (MOFA) Pakistan",
                "pakistan_specific_instruction": "Section C stamped by MOFA / HEC Islamabad"
            },
            {
                "document_name": "Certified Educational Diplomas & Transcripts",
                "mandatory": True,
                "specification": "Complete transcripts and certificates showing all grades",
                "pakistan_specific_instruction": "Attested by HEC / IBCC Pakistan"
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "Personal essay detailing motivation and study plan",
                "pakistan_specific_instruction": "Clearly stating why Brunei is your choice"
            },
            {
                "document_name": "Two Referee Assessment Reports",
                "mandatory": True,
                "specification": "Completed referee forms on official letterhead",
                "pakistan_specific_instruction": "From teachers or university professors"
            },
            {
                "document_name": "Certified Birth Certificate & Passport Copy",
                "mandatory": True,
                "specification": "Certified copies of NADRA birth certificate and passport",
                "pakistan_specific_instruction": "Passport must be valid for at least 12 months"
            },
            {
                "document_name": "Police Clearance Certificate",
                "mandatory": True,
                "specification": "Security clearance proving non-criminal record",
                "pakistan_specific_instruction": "Issued by local Pakistani police department"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2027-01-10",
            "application_deadline": "2027-02-15",
            "university_admission_deadline": "2027-02-15",
            "document_submission_deadline": "2027-02-15",
            "recommendation_letters_deadline": "2027-02-15",
            "interview_period": "April to May 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-07-15",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "August 2027",
            "annual_cycle_notes": "Application window is strictly January to mid-February each year. Academic year starts in August."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Academic grades, transcript performance, qualification relevance)",
            "extracurricular_and_leadership_weight": "10% (Extracurricular background)",
            "research_experience_weight": "10% (For Master's research candidates)",
            "work_experience_weight": "5% (Work experience)",
            "personal_statement_weight": "15% (Statement of Purpose clarity)",
            "recommendations_weight": "10% (Referee appraisals)",
            "interview_weight": "Evaluated in interview round",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Merit and bilateral cooperation)",
            "selection_panel_composition": "MFA Brunei Scholarship Selection Committee in collaboration with university admissions boards.",
            "evaluation_methodology": "Assessment of academic merit and strategic country representation among OIC and Commonwealth states."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,000 to 4,000 applications globally across OIC/Commonwealth countries",
            "total_scholarships_awarded": "~100 to 150 scholarships awarded annually",
            "acceptance_rate_global": "~3% to 4%",
            "acceptance_rate_pakistan": "~2% to 3% (Competitive)",
            "typical_successful_applicant_gpa": "3.30 to 3.80 / 4.00 CGPA or 75%+ marks",
            "typical_academic_and_research_profile": "Well-rounded students with solid academic records in engineering, business, or Islamic studies.",
            "common_backgrounds_of_winners": "Students from all provinces of Pakistan seeking quality funded education in a secure, tax-free Islamic country.",
            "high_representation_countries": "Malaysia, Indonesia, Pakistan, Bangladesh, Nigeria, Maldives, Oman.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam emails asking for visa deposits or processing fees for Brunei scholarships."
            ],
            "application_fee_warning": "The Government of Brunei Darussalam scholarship application is 100% FREE.",
            "agent_and_intermediary_warnings": "Never work through agents; apply directly to MFA Brunei.",
            "hidden_costs_breakdown": [
                "HEC / MOFA attestation and courier fees in Pakistan.",
                "Medical checkup expenses prior to departure.",
                "Personal incidentals in Brunei."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot apply without a government job. (Fact: Open to all private and public students; only government endorsement on Section C is required).",
                "MYTH: Only Islamic studies are taught. (Fact: High-tech Engineering, Petroleum Geoscience, and Computer Science are taught in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites state PhD is covered; BDGS officially covers Diploma, Bachelor's, and Master's degrees only."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance and pass all examinations in accordance with university rules.",
            "attendance_requirements": "Full-time physical residence and attendance in Brunei Darussalam.",
            "academic_progress_monitoring": "Host universities submit regular progress reports to the Ministry of Foreign Affairs.",
            "work_restrictions_during_study": "Scholars are strictly prohibited from engaging in any paid employment during the scholarship tenure.",
            "home_country_return_obligation": "MANDATORY Return: Scholars must return to their home country immediately upon completion of their study program.",
            "service_obligations_or_bonds": "Obligated to return home; no right to seek employment or permanent stay in Brunei Darussalam.",
            "repayment_clawback_conditions": "Expulsion, academic failure, or breach of regulations requires full repayment of scholarship costs.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "No extensions beyond the standard program period."
        },
        "official_sources_verified": [
            {
                "source_name": "Ministry of Foreign Affairs Brunei Darussalam - BDGS Official Portal",
                "source_url": "https://www.mfa.gov.bn/Pages/bdgs/bdgs2024.aspx",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific country quota allocations among OIC member states",
                    "Interview grading sheet rubrics"
                ]
            }
        ]
    },

    # 8. Asian Development Bank - Japan Scholarship Program (ADB-JSP) (SCH-AS-009)
    "SCH-AS-009": {
        "scholarship_id": "SCH-AS-009",
        "basic_details": {
            "scholarship_name": "Asian Development Bank - Japan Scholarship Program (ADB-JSP)",
            "offering_entity": "Asian Development Bank (ADB) & Government of Japan",
            "host_country": "Japan (and partner institutions in Asia-Pacific)",
            "host_institutions_covered": "25 designated institutions in 9 countries (University of Tokyo, Kyoto University, Tokyo Tech, Hitotsubashi, NUS, University of Melbourne, University of Auckland, AIM Philippines)",
            "degree_levels": ["Master's (Postgraduate)"],
            "major_restrictions": "Development-related fields: Economics, Management, Science and Technology, Environment, Agriculture, Public Health, Infrastructure, International Development.",
            "number_of_awards_total": "~135 to 150 scholarships awarded annually across 25 institutions",
            "number_of_awards_pakistan": "Open to Pakistan as an ADB borrowing member country (~10 to 15 Pakistani professionals selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "1 to 2 academic years (covering full master's program)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of an ADB borrowing member country (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Not more than 35 years old at the time of application (in exceptional cases, for senior programs, up to 45 years old).",
            "academic_qualifications": "Completed 16 years of education (Bachelor's degree or equivalent) with superior academic record.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum 3.20 / 4.00 CGPA or equivalent top 15% class standing.",
            "subject_background_prerequisites": "Academic background aligned with development-oriented master's courses.",
            "current_education_status": "Employed professional with minimum 2 years of full-time professional working experience.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": True,
            "work_experience_minimum_years": 2.0,
            "work_experience_notes": "MANDATORY: At least 2 years of full-time professional working experience acquired after university graduation in a relevant field.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Proficiency in oral and written English (IELTS 6.5+ or TOEFL 90+ satisfying host institution admission standards)."
            },
            "other_language_requirements": "None; all designated ADB-JSP programs taught in English.",
            "gender_specific_requirements": "Equal opportunity; women and applicants from public sector actively encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Development impact and mandatory agreement to return to Pakistan for at least 2 years post-graduation.",
            "previous_scholarship_restrictions": "Ineligible if already holding a Master's degree or currently studying abroad.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition and academic fees at the designated host institution.",
                "amount": "Full coverage"
            },
            "admission_application_fee": {
                "status": "WAIVED_OR_REIMBURSED",
                "details": "Managed through host institution.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly subsistence allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly subsistence allowance covering housing, food, and daily living costs (e.g. ~¥147,000/month in Japan).",
                "amount": "¥147,000 / month in Japan (~PKR 275,000 / month) or local currency equivalent"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Economy class return airfare between home country and the host institution.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Student visa fees paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive medical and accident insurance covered.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Books and instructional materials allowance provided.",
                "amount": "Annual book grant"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Special grant available for thesis preparation, field trips, and computer software.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Settlement allowance provided upon arrival.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 30000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply to one of the 25 designated academic institutions in the Asia-Pacific region.",
            "participating_institutions": [
                "University of Tokyo (Japan)", "Kyoto University (Japan)",
                "Tokyo Institute of Technology (Japan)", "Hitotsubashi University (Japan)",
                "National University of Singapore (NUS - Singapore)",
                "University of Melbourne (Australia)", "University of Auckland (New Zealand)",
                "Asian Institute of Management (AIM - Philippines)"
            ],
            "university_rankings_scope": "Premier universities in Japan and the Asia-Pacific region.",
            "available_majors": [
                "Economics, Public Policy, International Development, Civil and Environmental Engineering, Urban Planning, Agricultural Economics, Renewable Energy, Public Health, Business Administration"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 to 2 academic years (full Master's program)",
            "admission_requirements_summary": "Apply directly to the designated academic institution for both admission and the ADB-JSP scholarship (at least 6 months before intended intake).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "University of Tokyo (Department of Civil Engineering) and Hitotsubashi University are premier ADB-JSP hubs.",
            "strategic_program_match_advice": "Focus heavily on how the master's degree aligns with ADB's Strategy 2030 and Pakistan's socio-economic development priorities."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.adb.org/work-with-us/careers/japan-scholarship-program",
            "portal_system_name": "Host Institution Application System (e.g. UTokyo, Kyoto, NUS)",
            "account_creation_instructions": "Applicants must request information and application forms directly from the designated institution of their choice, not from ADB.",
            "step_by_step_workflow": [
                "1. Choose eligible Master's course from the 25 designated ADB-JSP institutions.",
                "2. Apply for admission and the ADB-JSP scholarship directly to the chosen institution.",
                "3. Submit academic transcripts, proof of 2 years work experience, income tax return, and CV.",
                "4. Host institution screens applicants and conducts academic review.",
                "5. Host institution ranks candidates and submits shortlisted roster to the Asian Development Bank.",
                "6. ADB reviews submissions and selects awardees in coordination with the Government of Japan.",
                "7. Host institution notifies successful applicants."
            ],
            "university_vs_scholarship_routing": "Institutional application: Submitted directly to the designated university.",
            "recommendation_letters_submission_method": "Two recommendation letters (one academic, one employer) submitted to host university.",
            "personal_statement_prompts": "Address your career progression, development impact goals, and how the program aligns with Pakistan's development.",
            "study_plan_research_proposal_requirements": "Master's study plan or research proposal detailing intended focus area.",
            "cv_format_requirements": "Detailed professional CV documenting minimum 2 years full-time employment history.",
            "interviews_conducted": True,
            "interview_format_details": "Host university admissions committee conducts video interviews in spring.",
            "standardized_tests": "English proficiency test (IELTS 6.5+ or TOEFL 90+).",
            "application_fee_amount": "Varies by institution; some waive fees for ADB-JSP.",
            "attestation_requirements": "Transcripts certified by HEC Pakistan.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "Submitted to designated host institution."
        },
        "required_documents_checklist": [
            {
                "document_name": "ADB-JSP Information Sheet & Application Form",
                "mandatory": True,
                "specification": "Official ADB-JSP form completed and signed",
                "pakistan_specific_instruction": "Downloaded from host university website"
            },
            {
                "document_name": "Proof of 2 Years Work Experience",
                "mandatory": True,
                "specification": "Official certificate of employment verifying full-time work acquired after graduation",
                "pakistan_specific_instruction": "On employer letterhead with contact info"
            },
            {
                "document_name": "Proof of Annual Income",
                "mandatory": True,
                "specification": "Salary certificate, FBR tax return, or pay slips of applicant and parents/spouse",
                "pakistan_specific_instruction": "FBR tax returns or official salary slips"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year education",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "One academic reference and one supervisor reference",
                "pakistan_specific_instruction": "Signed and stamped"
            },
            {
                "document_name": "English Proficiency Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (90+)",
                "pakistan_specific_instruction": "Valid test report"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-08-01",
            "application_deadline": "2026-12-15",
            "university_admission_deadline": "2026-12-15",
            "document_submission_deadline": "2026-12-15",
            "recommendation_letters_deadline": "2026-12-15",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "March 2027",
            "final_result_acceptance_deadline": "2027-05-15",
            "visa_application_window": "June to August 2027",
            "semester_commencement": "September/October 2027 (or April 2027 for Spring intake in Japan)",
            "annual_cycle_notes": "Deadlines vary by designated institution (typically between December and February for Fall intake)."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Superior academic record)",
            "extracurricular_and_leadership_weight": "10% (Leadership potential)",
            "research_experience_weight": "10% (Applied developmental research)",
            "work_experience_weight": "25% (At least 2 years full-time experience in development sectors)",
            "personal_statement_weight": "10% (Commitment to return and contribute to home country development)",
            "recommendations_weight": "10% (Employer and academic endorsements)",
            "interview_weight": "Evaluated during university review",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "Preferences given to applicants with lower financial capacity",
            "selection_panel_composition": "Designated institution selection boards and the Asian Development Bank Central Selection Committee.",
            "evaluation_methodology": "Two-tier review: Academic institution ranks applicants based on academic and professional merit; ADB finalizes selection."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,000 to 5,000 applicants across 25 designated institutions",
            "total_scholarships_awarded": "~135 to 150 scholarships awarded annually",
            "acceptance_rate_global": "~3% to 4%",
            "acceptance_rate_pakistan": "~2% to 3% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.30 to 3.85 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Mid-career professionals with 3 to 6 years of experience in government departments, civil engineering consultancies, or financial institutions.",
            "common_backgrounds_of_winners": "Pakistani civil servants, engineers in infrastructure/power departments, central bank analysts, environmental specialists.",
            "high_representation_countries": "Pakistan, Philippines, Indonesia, Vietnam, Bangladesh, Nepal, Sri Lanka.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites claiming to accept direct applications to ADB; ADB does NOT accept direct applications."
            ],
            "application_fee_warning": "ADB does not charge any application fee; check host institution fees.",
            "agent_and_intermediary_warnings": "Never work through agents; apply directly to the designated academic institution.",
            "hidden_costs_breakdown": [
                "Visa processing fees in Pakistan.",
                "English language test fees (IELTS/TOEFL).",
                "Initial pocket money before first stipend release."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can stay and work abroad post-graduation. (Fact: MANDATORY 2-year return to home country is legally binding under scholarship terms).",
                "MYTH: You can apply without work experience. (Fact: Minimum 2 years of full-time professional experience is strictly required)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some agencies claim this funds PhDs; ADB-JSP strictly funds Master's degree programs."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance in accordance with host institution standards.",
            "attendance_requirements": "Full-time physical residence and attendance at designated host institution.",
            "academic_progress_monitoring": "Host institutions report progress annually to the Asian Development Bank.",
            "work_restrictions_during_study": "Scholars are not permitted to work for pay during their scholarship period.",
            "home_country_return_obligation": "MANDATORY 2-Year Return: Scholars must agree to return to their home country for at least 2 years following completion to contribute to economic development.",
            "service_obligations_or_bonds": "Legal undertaking signed with the Asian Development Bank.",
            "repayment_clawback_conditions": "Failing to return home or termination of study requires repayment of all scholarship benefits.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "No extensions beyond normal master's program duration."
        },
        "official_sources_verified": [
            {
                "source_name": "Asian Development Bank (ADB) - Japan Scholarship Program Official Portal",
                "source_url": "https://www.adb.org/work-with-us/careers/japan-scholarship-program",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation matrix of spots per designated academic institution",
                    "Internal country-by-country quota breakdown among borrowing member countries"
                ]
            }
        ]
    }
}
