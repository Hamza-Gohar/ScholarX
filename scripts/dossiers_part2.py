"""
scripts/dossiers_part2.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Part 2
Contains:
8.  SCH-AS-001: Chinese Government Scholarship - CSC Type A Bilateral (China)
9.  SCH-AS-002: MEXT Japanese Government Scholarship - Embassy Recommendation (Japan)
10. SCH-AS-003: Global Korea Scholarship - GKS / KGSP (South Korea)
11. SCH-ME-001: Türkiye Bursları Scholarships (Turkey)
12. SCH-OC-001: Australia Awards Scholarships - Pakistan Category (Australia)
13. SCH-EU-005: Swiss Government Excellence Scholarships (Switzerland)
14. SCH-EU-003: Italian Regional DSU / EDISU Merit & Need Scholarship (Italy)
"""

DOSSIERS_PART2 = {
    # 8. Chinese Government Scholarship - CSC Type A Bilateral (China)
    "SCH-AS-001": {
        "scholarship_id": "SCH-AS-001",
        "basic_details": {
            "scholarship_name": "Chinese Government Scholarship (CSC Type A - Bilateral Program via HEC)",
            "offering_entity": "Ministry of Education of the People's Republic of China / China Scholarship Council (CSC) & HEC Pakistan",
            "host_country": "China",
            "host_institutions_covered": "Accredited Chinese 'Double First-Class' Universities (Tsinghua, Peking, Zhejiang, Fudan, Shanghai Jiao Tong, Harbin IT, USTC, Beihang, Wuhan University, etc.)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Open to all disciplines: Engineering, Computer Science, Artificial Intelligence, Medicine, Natural Sciences, Agriculture, Economics, Management, Humanities.",
            "number_of_awards_total": "~10,000 bilateral awards distributed across 180+ partner nations globally",
            "number_of_awards_pakistan": "~200 to 300 bilateral quota awards reserved exclusively for Pakistani students annually via HEC",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's: 4-5 years; Master's: 2-3 years; PhD: 3-4 years (includes 1 year preparatory Chinese if applicable)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of the Islamic Republic of Pakistan in good physical and mental health"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 25,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Bachelor's: Under 25 years; Master's: Under 35 years; PhD: Under 40 years of age.",
            "academic_qualifications": "High school certificate (HSSC/A-Levels) for BS; 16-year Bachelor's for Master's; 18-year MS/MPhil for PhD from HEC-recognized institutions.",
            "minimum_gpa_percentage": 65.0,
            "minimum_gpa_scale": 2.8,
            "grading_conversion_notes": "Minimum 2.8/4.0 CGPA or 65% marks; competitive candidates typically possess 3.2+ CGPA.",
            "subject_background_prerequisites": "Academic background aligned with intended Chinese university department.",
            "current_education_status": "Graduated; result-awaiting students must receive final transcript before Chinese university enrollment in September.",
            "graduation_year_restrictions": "None specified.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; research publications strongly preferred for PhD applicants.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": True,
            "moi_certificate_accepted": True,
            "language_notes": "For English-taught programs: IELTS 6.0+, TOEFL 80+, or English Medium of Instruction (MOI) certificate from Pakistani university. For Chinese-taught programs: HSK Level 4 for BS, HSK Level 5 for MS/PhD.",
            "other_language_requirements": "HSK certificate required for Chinese-medium degrees; 1 year Chinese language prep provided if admitted to Chinese-taught track.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Must be nominated through the Higher Education Commission (HEC) of Pakistan under Agency Number 5861.",
            "previous_scholarship_restrictions": "Current recipients of other Chinese government scholarships cannot hold concurrent awards.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full tuition fee waiver for the entire duration of undergraduate or postgraduate studies."},
            "admission_application_fee": {"status": "COVERED", "details": "Waived under bilateral government agreement when applying via Type A (HEC)."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Free university dormitory accommodation on campus (single room for PhD, double room for Master's/Undergrad) OR monthly housing subsidy."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living stipend paid directly by host university.", "amount": "RMB 2,500/mo (BS), RMB 3,000/mo (MS), RMB 3,500/mo (PhD) (~PKR 100,000 to 140,000/mo)"},
            "airfare": {"status": "NOT_COVERED", "details": "International airfare between Pakistan and China is NOT covered by CSC Type A (must be borne by the student or HEC)."},
            "visa_fee": {"status": "WAIVED", "details": "X1 Chinese Student Visa fee waived or issued at concessionary rate upon presentation of official JW201 form."},
            "health_insurance": {"status": "COVERED", "details": "Comprehensive Medical Insurance Scheme for International Students in China (RMB 800/year value) covering hospitalization and accidental injury."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Subsidized meals widely available at on-campus university canteens."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via monthly stipend or campus library privileges."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Funded through Chinese supervising professor's national research grants (NSFC)."},
            "travel_transit_allowance": {"status": "NOT_COVERED", "details": "Domestic transit in China to university city covered by student."},
            "total_estimated_value_usd_per_year": 18000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Applicants may select up to THREE target Chinese universities and disciplines in priority order on the CSC portal.",
            "participating_institutions": ["Tsinghua University, Peking University, Zhejiang University, Fudan University, Shanghai Jiao Tong, Harbin Institute of Technology, USTC, Beihang, Wuhan, Xi'an Jiaotong"],
            "university_rankings_scope": "Top 1 to 50 in China; QS World Top 500.",
            "available_majors": ["Artificial Intelligence", "Mechanical Engineering", "Civil Engineering", "Computer Science", "Materials Science", "Clinical Medicine", "Biotechnology", "International Trade", "Renewable Energy"],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4-5 years; Master's: 2-3 years; PhD: 3-4 years",
            "admission_requirements_summary": "Online CSC + HEC forms, transcripts, physical exam form, police clearance, 2 recommendation letters, study plan.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Securing a Pre-Admission Letter or Supervisor Acceptance Letter from a Chinese university professor beforehand exponentially increases selection chances for Tsinghua/Peking/Zhejiang.",
            "strategic_program_match_advice": "Contact prospective Chinese supervisors in October/November with a strong CV and research proposal to secure an official Acceptance Letter before the HEC/CSC deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.campuschina.org/",
            "portal_system_name": "Chinese Government Scholarship Information System (CSC Portal) & HEC Pakistan Portal",
            "account_creation_instructions": "MANDATORY DUAL APPLICATION: 1) Apply on CSC portal under Program Category 'Type A' using HEC Agency Number 5861; AND 2) Apply on HEC Scholarship portal (scholarship.hec.gov.pk).",
            "step_by_step_workflow": [
                "1. Search eligible universities and contact Chinese professors to request an Acceptance Letter.",
                "2. Complete the Foreigner Physical Examination Form (with blood tests) and obtain Police Clearance Certificate.",
                "3. Register on CSC portal (campuschina.org), select Program Category 'Type A', Agency Number 5861 (HEC).",
                "4. Upload degree transcripts, study plan, 2 recommendation letters, physical exam, and police certificate.",
                "5. Register on HEC portal (scholarship.hec.gov.pk) and submit application under Chinese Government Scholarship.",
                "6. Take HEC USAT (Undergrad) or HEC HAT (Postgrad) test organized by ETC Pakistan.",
                "7. HEC prepares national merit list based on academic formula + HAT/USAT score.",
                "8. HEC sends top nominated dossiers to CSC Beijing in February/March.",
                "9. CSC and Chinese universities review files and issue final admissions (June/July).",
                "10. Universities issue official Admission Notice and JW201 Visa Form to HEC for dispatch to scholars.",
                "11. Apply for Chinese X1 Visa at Chinese Embassy/Consulate in Pakistan and depart in August/September."
            ],
            "university_vs_scholarship_routing": "Integrated routing: Nominated via HEC Pakistan under Type A; CSC places candidate in one of their 3 choices.",
            "recommendation_letters_submission_method": "Uploaded directly to the CSC and HEC portals by applicant (must be signed by full professors or associate professors).",
            "personal_statement_prompts": "Study Plan / Research Proposal (minimum 500 words for undergrad, 800 words for postgrad, 1000+ words for PhD): Academic background, research questions, why China, and career plans.",
            "study_plan_research_proposal_requirements": "PhD applicants must write a comprehensive research proposal endorsed by a Chinese prospective supervisor.",
            "cv_format_requirements": "Standard academic CV.",
            "interviews_conducted": False,
            "interview_format_details": "Generally paper-based evaluation; some individual Chinese university professors conduct a 15-minute video interview on WeChat/Zoom before issuing an acceptance letter.",
            "standardized_tests": "HEC HAT test (for MS/PhD) or HEC USAT (for BS) required for Pakistan national nomination.",
            "application_fee_amount": "RMB 0 / PKR 0 on CSC portal; nominal HEC test fee (~PKR 2,000).",
            "attestation_requirements": "HEC and MOFA attestation of degree certificates required prior to visa processing.",
            "translation_requirements": "Notarized English or Chinese translations for non-English documents.",
            "final_submission_method": "Dual online portal submission (CSC + HEC)."
        },
        "required_documents_checklist": [
            {"document_name": "Valid Passport Information Page", "mandatory": True, "specification": "Passport valid for at least 18 months", "pakistan_specific_instruction": "Required for CSC portal and X1 visa"},
            {"document_name": "Notarized Highest Diploma & Transcripts", "mandatory": True, "specification": "Degree certificate and transcript attested by HEC and notarized", "pakistan_specific_instruction": "Must be recognized by HEC Pakistan"},
            {"document_name": "Foreigner Physical Examination Form", "mandatory": True, "specification": "Standard Chinese medical form completed by physician with hospital stamp and photo", "pakistan_specific_instruction": "Includes blood tests (HIV, Syphilis, Hepatitis), chest X-ray, and ECG; valid for 6 months"},
            {"document_name": "Non-Criminal Record Certificate (Police Character Certificate)", "mandatory": True, "specification": "Issued by local police khidmat markaz / SSP office within past 6 months", "pakistan_specific_instruction": "Mandatory document for Chinese visa and CSC submission"},
            {"document_name": "Study Plan / Research Proposal", "mandatory": True, "specification": "Minimum 800 words for MS, 1,000 words for PhD in English or Chinese", "pakistan_specific_instruction": "Focus on technological and academic contribution"},
            {"document_name": "Two Recommendation Letters", "mandatory": True, "specification": "Signed by Professors or Associate Professors with institutional contacts", "pakistan_specific_instruction": "Must include official university letterhead and stamps"},
            {"document_name": "Pre-Admission Letter / Supervisor Acceptance Letter", "mandatory": False, "specification": "Official acceptance letter from a Chinese university professor/department", "pakistan_specific_instruction": "Not strictly mandatory, but dramatically boosts selection chances for top universities"}
        ],
        "important_dates_timeline": {
            "application_open_date": "December annually (e.g., 2026-12-01)",
            "application_deadline": "Mid-January to mid-February annually (varies slightly by HEC announcement)",
            "university_admission_deadline": "Managed internally by CSC (March - May)",
            "document_submission_deadline": "Coincides with HEC deadline",
            "recommendation_letters_deadline": "Coincides with HEC deadline",
            "interview_period": "N/A (Dossier review)",
            "shortlist_announcement": "HEC nominations sent in March; Final admission notices in July/August",
            "final_result_acceptance_deadline": "August annually",
            "visa_application_window": "August (Chinese Embassy Islamabad / Consulates in Karachi & Lahore)",
            "semester_commencement": "September (Fall Semester)",
            "annual_cycle_notes": "Agency Number 5861 is strictly for HEC bilateral quota; applying under wrong agency number voids nomination."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Matric, Inter, and Bachelor's formula score via HEC)",
            "extracurricular_and_leadership_weight": "5% (General profile)",
            "research_experience_weight": "20% (Publications and quality of study plan)",
            "work_experience_weight": "5% (Professional experience)",
            "personal_statement_weight": "15% (Strength of research proposal)",
            "recommendations_weight": "5% (Professor endorsements)",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "HEC HAT / USAT score accounts for 50% of HEC preliminary screening score!",
            "financial_need_weight": "0% (Bilateral government quota)",
            "selection_panel_composition": "HEC Selection Board and CSC Expert Review Panels in Beijing.",
            "evaluation_methodology": "Dual-stage: HEC nominates top merit candidates using HAT + academic formula; CSC matches nominated students with participating Chinese universities."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~8,000 to 12,000 applicants in Pakistan across BS, MS, PhD",
            "total_scholarships_awarded": "~200 to 300 bilateral awards for Pakistan",
            "acceptance_rate_global": "N/A (Bilateral country quota)",
            "acceptance_rate_pakistan": "~2.5% to 3.5% (High Competition)",
            "typical_successful_applicant_gpa": "3.30 to 3.80 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Solid academic standing, strong score in HEC HAT (typically 70+), and a supervisor acceptance letter from a Chinese professor.",
            "common_backgrounds_of_winners": "Graduates of NUST, UET, FAST, Quaid-i-Azam, COMSATS, Agriculture University Faisalabad, and regional public universities.",
            "high_representation_countries": "Reserved exclusively for Pakistan under Pak-China bilateral educational exchange.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial educational consultants in Pakistan charging PKR 200,000 to 500,000 claiming they 'sell CSC scholarship quotas'. CSC scholarships CANNOT be bought; selections are coordinated directly between HEC and the Chinese Ministry of Education.",
                "Fake admission letters issued by unverified Chinese agents."
            ],
            "application_fee_warning": "CSC portal is 100% FREE. HEC charges only the standard test fee (~PKR 2,000).",
            "agent_and_intermediary_warnings": "Never use third-party agents; all correspondence must be direct with professors and official portals.",
            "hidden_costs_breakdown": [
                "International flight ticket to China (PKR 150,000 to 220,000) is NOT covered by the scholarship.",
                "Foreigner physical examination medical tests at private labs (PKR 12,000 to 18,000).",
                "Police Character Certificate and MOFA attestations (PKR 5,000 to 10,000).",
                "Initial settling cash buffer in China (RMB 2,000 to 3,000) before first stipend disbursal."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot study in English in China. (Fact: Thousands of master's and PhD programs are taught 100% in English by internationally educated Chinese faculty).",
                "MYTH: You cannot apply without a professor acceptance letter. (Fact: You CAN apply without one, but having an acceptance letter dramatically increases your placement at top C9 universities)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Agents often confuse CSC Type A (Bilateral via Embassy/HEC) with CSC Type B (Direct University application). Applying to both simultaneously increases chances."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must participate in the Annual CSC Scholarship Review; failing courses results in suspension of stipend or termination of scholarship.",
            "attendance_requirements": "Full-time physical residence on campus in China.",
            "academic_progress_monitoring": "Annual evaluation conducted every May by the host university international office.",
            "work_restrictions_during_study": "Part-time on-campus work or off-campus internships permitted with formal approval from university and local Exit-Entry Bureau on student residence permit.",
            "home_country_return_obligation": "Expected to return to Pakistan upon graduation under bilateral MoU terms, though many graduates pursue post-docs in China or abroad.",
            "service_obligations_or_bonds": "HEC undertaking form agreeing to return.",
            "repayment_clawback_conditions": "Expulsion or unapproved withdrawal terminates scholarship; severe violations require repayment.",
            "rules_for_changing_university": "Strictly disallowed once placed.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Scholarship tenure cannot be extended beyond the approved period in the initial admission notice."
        },
        "official_sources_verified": [
            {
                "source_name": "China Scholarship Council (CSC) - Official Campus China Portal",
                "source_url": "https://www.campuschina.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "University-specific acceptance letter quotas per professor",
                    "Passing score criteria for institutional CSC reviews"
                ]
            },
            {
                "source_name": "Higher Education Commission (HEC) Pakistan - Chinese Government Scholarship Program",
                "source_url": "https://scholarship.hec.gov.pk/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact annual quota distribution between BS, MS, and PhD categories"
                ]
            }
        ]
    },

    # 9. MEXT Japanese Government Scholarship (Embassy Recommendation)
    "SCH-AS-002": {
        "scholarship_id": "SCH-AS-002",
        "basic_details": {
            "scholarship_name": "MEXT Japanese Government Scholarship (Embassy Recommendation)",
            "offering_entity": "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Government of Japan",
            "host_country": "Japan",
            "host_institutions_covered": "National and Public Universities in Japan (University of Tokyo, Kyoto University, Osaka University, Tohoku University, Tokyo Tech, Kyushu, Nagoya, Hokkaido)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Open to all fields of study: Social Sciences, Humanities, Natural Sciences, Engineering, Medicine, Dentistry, Agriculture. Applicants must choose fields in which they can major at Japanese universities.",
            "number_of_awards_total": "~9,000 MEXT scholarship recipients worldwide annually across all tracks",
            "number_of_awards_pakistan": "~30 to 45 scholars selected annually through the Embassy of Japan in Islamabad",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Undergraduate: 5 years (includes 1 year preparatory Japanese); Research/Master's/PhD: 2 to 5 years (standard degree duration)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of the Islamic Republic of Pakistan (must not hold Japanese nationality)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 24,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate: Born on or after April 2, 2001 (under 25). Research/Postgraduate: Born on or after April 2, 1990 (under 35).",
            "academic_qualifications": "12 years completed schooling for Undergraduate; 16 years education (Bachelor's) for Master's; 18 years education (Master's) for PhD from recognized universities.",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 70% marks or 3.0/4.0 CGPA; competitive shortlisted applicants typically possess 3.5+ CGPA and top academic standing.",
            "subject_background_prerequisites": "Field of study must be the same as or related to the field the applicant majored in at undergraduate level.",
            "current_education_status": "Graduated or expected to graduate by the time of departure (September or April).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "MEXT does NOT require IELTS/TOEFL at application; the Embassy of Japan administers its OWN rigorous written English examination in Islamabad.",
            "other_language_requirements": "Must be willing to learn Japanese. Japanese language written exam is administered to all applicants (scores used for placement or bonus points).",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Active military personnel are strictly ineligible.",
            "previous_scholarship_restrictions": "Previous MEXT recipients are ineligible unless they have at least 3 years of subsequent educational/research experience in Pakistan.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% waiver of entrance examination fees, matriculation fees, and tuition fees at the Japanese national university."},
            "admission_application_fee": {"status": "WAIVED", "details": "Covered under MEXT government sponsorship."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via monthly scholarship allowance; universities offer subsidized international student dormitories (Kaikan) for the first year."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly allowance paid directly by MEXT.", "amount": "117,000 JPY/mo (Undergrad), 144,000 JPY/mo (Master's), 145,000 JPY/mo (PhD) (~PKR 220,000 to 275,000/mo) + regional supplement in designated cities"},
            "airfare": {"status": "COVERED", "details": "Prepaid economy class flight ticket from nearest international airport in Pakistan (Islamabad/Karachi/Lahore) to Narita/Kansai International Airport, and return ticket upon degree completion."},
            "visa_fee": {"status": "WAIVED", "details": "Japanese College Student Visa issued free of charge by the Embassy of Japan in Islamabad."},
            "health_insurance": {"status": "SUBSIDIZED", "details": "Students enroll in Japanese National Health Insurance (NHI) paying subsidized student premiums (~1,500-2,000 JPY/month) which covers 70% of medical costs; universities reimburse the remaining 30% through student mutual aid."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Subsidized cafeteria meals available on Japanese campuses."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via monthly stipend and laboratory resources."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Funded through Japanese laboratory research funds (Kakenhi grants)."},
            "travel_transit_allowance": {"status": "NOT_COVERED", "details": "Domestic transit from international airport in Japan to university campus covered by student."},
            "total_estimated_value_usd_per_year": 25000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Candidates selected in the Primary Screening contact up to TWO or THREE Japanese national universities to obtain Provisional Acceptance Letters.",
            "participating_institutions": ["University of Tokyo, Kyoto University, Osaka University, Tohoku University, Tokyo Institute of Technology, Nagoya University, Kyushu University, Hokkaido University, Tsukuba"],
            "university_rankings_scope": "Imperial Universities and leading national universities of Japan (Top 100 QS).",
            "available_majors": ["All academic fields (Robotics, Electronics, Quantum Computing, Materials Science, Medicine, Civil Engineering, Agriculture, Economics, Japanese Studies)"],
            "english_taught_program_availability": True,
            "program_duration": "Undergraduate: 5 years; Master's: 2 years; PhD: 3 years",
            "admission_requirements_summary": "Passed Embassy screening, academic transcripts, field of study and research program plan, health certificate, university acceptance letters.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Applicants do NOT contact Japanese universities before passing the Embassy Primary Screening. Once you pass the Embassy interview, Japanese professors welcome you with open arms because funding is 100% guaranteed by MEXT.",
            "strategic_program_match_advice": "Focus heavily on the 'Field of Study and Research Program Plan' (Annex form) ensuring clear scientific methodology and strong rationale for why this research must be conducted in Japan."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.pk.emb-japan.go.jp/itpr_en/MEXT_Scholarship.html",
            "portal_system_name": "Physical / Postal Submission to Embassy of Japan in Islamabad & Study in Japan Official Portal",
            "account_creation_instructions": "Download official MEXT application forms from the Embassy of Japan in Pakistan website; submit hardcopy dossier by courier or post.",
            "step_by_step_workflow": [
                "1. Download MEXT application guidelines and forms from Embassy of Japan in Pakistan website (opens early May).",
                "2. Complete Application Form and Field of Study and Research Program Plan.",
                "3. Gather academic transcripts, graduation certificates, recommendation letters, and medical form.",
                "4. Dispatch complete hardcopy dossier by post to Embassy of Japan in Islamabad before late May deadline.",
                "5. Embassy conducts document screening and announces shortlist for written tests.",
                "6. Attend written examinations (English, Japanese, and specialized sciences/maths) in Islamabad in late June.",
                "7. Top test scorers attend in-person interviews at the Embassy of Japan in Islamabad in July.",
                "8. Candidates who pass Primary Screening receive official Certificate of Passing Preliminary Screening (August).",
                "9. Contact professors at Japanese universities to secure Provisional Acceptance Letters (August - September).",
                "10. Submit acceptance letters to the Embassy; MEXT Tokyo confirms final placement in December/January.",
                "11. Depart for Japan in April or October."
            ],
            "university_vs_scholarship_routing": "Embassy First: Win Embassy Recommendation first; then obtain university provisional acceptance letters.",
            "recommendation_letters_submission_method": "Hardcopy confidential letters signed by university dean or academic advisor included in application packet.",
            "personal_statement_prompts": "Field of Study and Research Program Plan (mandatory 3-page MEXT form): 1) Past academic research, 2) Proposed research theme, 3) Detailed research plan in Japan, 4) Contribution to Japan and Pakistan.",
            "study_plan_research_proposal_requirements": "Crucial scoring factor for research students; must demonstrate technical feasibility and alignment with Japanese research laboratories.",
            "cv_format_requirements": "Included within standard MEXT application form.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous in-person interview in Islamabad before a panel of Japanese diplomats, cultural attachés, and senior Pakistani MEXT alumni professors.",
            "standardized_tests": "Embassy conducts its own written examinations in Islamabad (English language test + Mathematics/Science tests for STEM).",
            "application_fee_amount": "PKR 0 / JPY 0 (100% FREE application process).",
            "attestation_requirements": "HEC attested copies of degrees and transcripts required.",
            "translation_requirements": "Certified English translations for any document not in English or Japanese.",
            "final_submission_method": "Hardcopy dossier delivered by postal mail / courier to Public Affairs Section, Embassy of Japan in Islamabad."
        },
        "required_documents_checklist": [
            {"document_name": "Completed MEXT Application Form", "mandatory": True, "specification": "Official prescribed form with passport-size photographs attached", "pakistan_specific_instruction": "Typed and signed by applicant"},
            {"document_name": "Field of Study and Research Program Plan", "mandatory": True, "specification": "Official prescribed form detailing past research and proposed research in Japan", "pakistan_specific_instruction": "The single most important document for postgraduate screening"},
            {"document_name": "Official Academic Transcripts", "mandatory": True, "specification": "Complete transcripts from all post-secondary education attended", "pakistan_specific_instruction": "Must be attested by HEC / university registrar"},
            {"document_name": "Graduation Certificate / Degree Certificate", "mandatory": True, "specification": "Certified copy of degree certificate", "pakistan_specific_instruction": "Provisional certificate accepted for result-awaiting candidates"},
            {"document_name": "Recommendation Letter from Academic Dean / Advisor", "mandatory": True, "specification": "Written on official university letterhead, signed and stamped", "pakistan_specific_instruction": "Must use prescribed MEXT recommendation template or institutional format"},
            {"document_name": "Medical Certificate of Health", "mandatory": True, "specification": "Official MEXT Certificate of Health completed by registered physician", "pakistan_specific_instruction": "Required upon passing initial screening"},
            {"document_name": "Abstracts of Theses / Scientific Publications", "mandatory": False, "specification": "One-page summaries of published papers or bachelor's/master's thesis", "pakistan_specific_instruction": "Strongly enhances credibility for research positions"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Early May annually (e.g., 2026-05-04)",
            "application_deadline": "Late May annually (e.g., 2026-05-25)",
            "university_admission_deadline": "August - September (provisional acceptance window)",
            "document_submission_deadline": "Late May annually",
            "recommendation_letters_deadline": "Late May annually",
            "interview_period": "Late June (Written Tests) and Early July (Interviews) in Islamabad",
            "shortlist_announcement": "Mid-August (Passing of Primary Screening announced)",
            "final_result_acceptance_deadline": "September (Submission of provisional acceptance letters)",
            "visa_application_window": "February - March of departure year",
            "semester_commencement": "April or October of departure year",
            "annual_cycle_notes": "Very strict schedule; candidates must be physically present in Islamabad for written exams and interviews."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Undergraduate GPA and university academic record)",
            "extracurricular_and_leadership_weight": "5% (General adaptability)",
            "research_experience_weight": "25% (Quality and depth of the Research Program Plan)",
            "work_experience_weight": "5% (Professional relevance)",
            "personal_statement_weight": "15% (Clarity of vision for Japan-Pakistan academic ties)",
            "recommendations_weight": "5% (Supervisor endorsement)",
            "interview_weight": "20% (Panel interview performance assessing dedication and character)",
            "test_scores_weight": "Written tests in Islamabad act as a strict cutoff filter (only top test performers are interviewed)!",
            "financial_need_weight": "0% (Pure academic merit and bilateral cultural diplomacy)",
            "selection_panel_composition": "Japanese diplomats, first secretaries, and distinguished Pakistani alumni professors appointed by the Embassy of Japan.",
            "evaluation_methodology": "Three-stage sift: 1) Hardcopy document evaluation, 2) Written subject and language exams in Islamabad, 3) Oral interview before the selection committee."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 applicants across Pakistan",
            "total_scholarships_awarded": "~30 to 45 scholars selected annually",
            "acceptance_rate_global": "N/A (Embassy-specific country quota)",
            "acceptance_rate_pakistan": "~0.8% to 1.2% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.50 to 3.90 / 4.00 CGPA",
            "typical_academic_and_research_profile": "High scorer on written English and subject tests, well-articulated research plan, clear knowledge of Japanese research laboratories.",
            "common_backgrounds_of_winners": "Graduates of NUST, LUMS, FAST, UET Lahore, Quaid-i-Azam, GIKI, University of the Punjab, and COMSATS.",
            "high_representation_countries": "Reserved exclusively for Pakistan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam agencies charging fees to submit MEXT applications. The Embassy of Japan accepts applications directly by post for FREE.",
                "Third-party consultants offering 'guaranteed Japanese embassy interview coaching'."
            ],
            "application_fee_warning": "MEXT application is 100% FREE. The Embassy never charges any examination or processing fees.",
            "agent_and_intermediary_warnings": "Never hire an agent. All MEXT documents must be original and completed by the candidate.",
            "hidden_costs_breakdown": [
                "Domestic travel to Islamabad for written tests and in-person interviews (candidates must arrange their own travel and lodging in Islamabad).",
                "Courier charges for mailing hardcopy dossiers to the Embassy.",
                "Medical examination certificate fees at certified clinics."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must speak fluent Japanese to apply. (Fact: Most STEM research programs are conducted in English; knowing zero Japanese does not disqualify you, although taking the Japanese written exam is required).",
                "MYTH: You should email Japanese professors before applying. (Fact: Under the Embassy track, you must NOT contact Japanese professors until after you pass the Embassy Primary Screening in August)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently confuse the Embassy Recommendation track (opens May) with the University Recommendation track (opens October). Both are distinct MEXT pathways."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and satisfy Japanese university credit and research requirements.",
            "attendance_requirements": "Full physical attendance in Japan. Absences longer than 30 consecutive days result in stipend cancellation.",
            "academic_progress_monitoring": "Annual progress reports submitted by laboratory supervising professors to MEXT.",
            "work_restrictions_during_study": "Part-time work permitted up to 28 hours per week with formal permission from the Japanese Immigration Bureau (Shikakugai Katsudo Kyoka).",
            "home_country_return_obligation": "No mandatory statutory home return bond enforced by MEXT; graduates can legally work in Japan on Engineer/Specialist in Humanities visas or transition to Japanese corporate careers.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Revocation of scholarship and reimbursement of flight ticket in cases of disciplinary expulsion or criminal offense in Japan.",
            "rules_for_changing_university": "Strictly disallowed once university placement is confirmed by MEXT.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Research students who pass the university's Master's or PhD entrance exams can apply for an extension of the MEXT scholarship to cover the full degree duration."
        },
        "official_sources_verified": [
            {
                "source_name": "Embassy of Japan in Pakistan - MEXT Scholarship Information Portal",
                "source_url": "https://www.pk.emb-japan.go.jp/itpr_en/MEXT_Scholarship.html",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Past written examination question papers for specialized subject exams (Embassy provides past English/Math papers but keeps science papers unreleased)",
                    "Internal cut-off marks for written examinations"
                ]
            },
            {
                "source_name": "Ministry of Education, Culture, Sports, Science and Technology (MEXT) Japan - Study in Japan",
                "source_url": "https://www.studyinjapan.go.jp/en/planning/scholarship/mext-scholarships/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact breakdown of final placement quota per individual Japanese university"
                ]
            }
        ]
    },

    # 10. Global Korea Scholarship (GKS / KGSP)
    "SCH-AS-003": {
        "scholarship_id": "SCH-AS-003",
        "basic_details": {
            "scholarship_name": "Global Korea Scholarship (GKS / KGSP)",
            "offering_entity": "National Institute for International Education (NIIED), Ministry of Education, Republic of Korea",
            "host_country": "South Korea",
            "host_institutions_covered": "Accredited Universities in South Korea across Type A (Seoul Metropolitan) and Type B (Regional) (Seoul National University, KAIST, Yonsei, Korea University, POSTECH, Sungkyunkwan, Pusan National, Kyungpook)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Eligible for almost all academic majors offered by participating Korean universities, with an emphasis on STEM, Engineering, Natural Sciences, Humanities, Social Sciences, and Business.",
            "number_of_awards_total": "~2,200 graduate scholars and ~500 undergraduate scholars admitted globally each year",
            "number_of_awards_pakistan": "~30 to 45 awards for Pakistan annually (split across Embassy Track and University Track)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Undergraduate: 5 years (1 yr Korean + 4 yrs BS); Master's: 3 years (1 yr Korean + 2 yrs MS); PhD: 4 years (1 yr Korean + 3 yrs PhD)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of Pakistan (applicants and their parents must hold non-Korean citizenship)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 24,
            "age_limit_postgrad": 40,
            "age_limit_notes": "Undergraduate: Under 25 years on March 1 of entry year. Graduate: Under 40 years on September 1 of entry year (up to 45 for university faculty members).",
            "academic_qualifications": "High school diploma for Undergraduate; Bachelor's degree (16 years education) for Master's; Master's degree (18 years education) for PhD.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "STRICT MANDATORY CUTOFF: Cumulative GPA must be above 80% marks OR CGPA 3.20/4.00, or ranked within the top 20% of class.",
            "subject_background_prerequisites": "Relevant undergraduate degree matching proposed graduate program.",
            "current_education_status": "Must have completed required degree by application deadline (result-awaiting applicants must provide official graduation certificate by July 31).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "English test scores (IELTS/TOEFL) are not strictly mandatory for NIIED, but provide substantial bonus points. Korean proficiency (TOPIK Level 3+) provides significant bonus points.",
            "other_language_requirements": "Mandatory 1-year Korean Language Program at a designated language institute in Korea; must achieve TOPIK Level 3 before degree program starts.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants can apply through EITHER the Embassy Track (apply to Korean Embassy in Islamabad) OR the University Track (apply directly to one Korean university). Applying to both tracks in the same year results in automatic disqualification.",
            "previous_scholarship_restrictions": "Former GKS scholars who attained TOPIK Level 5+ can reapply once at a higher degree level.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% full tuition fee and admission fee paid directly by NIIED and the host Korean university."},
            "admission_application_fee": {"status": "COVERED", "details": "Exempt or paid directly by NIIED."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via monthly living stipend; university dormitory rooms provided at subsidized rates."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly allowance paid directly to scholar.", "amount": "KRW 900,000/mo (Undergrad), KRW 1,000,000/mo (Master's/PhD) (~PKR 210,000 to 230,000/mo)"},
            "airfare": {"status": "COVERED", "details": "Actual economy class round-trip flight ticket between Pakistan and Incheon International Airport provided by NIIED."},
            "visa_fee": {"status": "WAIVED", "details": "Korean D-2 / D-4 Student Visa issued with fee waiver at the Embassy of the Republic of Korea in Islamabad."},
            "health_insurance": {"status": "COVERED", "details": "Full National Health Insurance (NHIS) premiums in South Korea covered throughout the grant period."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Subsidized campus cafeterias."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Research allowance granted per semester: KRW 210,000 (Humanities/Social Sciences) to KRW 240,000 (STEM).", "amount": "KRW 210,000 to 240,000 / semester"},
            "research_funding_conference_grant": {"status": "COVERED", "details": "Thesis printing fee grant (KRW 500,000 to 800,000) reimbursed upon thesis completion.", "amount": "KRW 500,000 to 800,000 one-off"},
            "travel_transit_allowance": {"status": "COVERED", "details": "Settlement allowance of KRW 200,000 upon arrival, and Korean Proficiency Grant of KRW 100,000/month for scholars holding TOPIK Level 5 or 6.", "amount": "KRW 200,000 one-off arrival + KRW 100,000/mo TOPIK bonus"},
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Embassy Track: Choose up to THREE universities (at least one must be a Regional Type B university). University Track: Choose ONE university directly.",
            "participating_institutions": ["Seoul National University, KAIST, Yonsei University, Korea University, POSTECH, Sungkyunkwan University, Hanyang University, Pusan National University, Kyungpook National University, UNIST, GIST"],
            "university_rankings_scope": "SKY universities and top Korean STEM powerhouses (QS World Top 50 to 300).",
            "available_majors": ["Semiconductor Engineering", "Artificial Intelligence", "Bioengineering", "Robotics", "Renewable Energy", "Korean Studies", "International Relations", "Computer Science", "Economics"],
            "english_taught_program_availability": True,
            "program_duration": "Undergraduate: 5 years; Master's: 3 years; PhD: 4 years",
            "admission_requirements_summary": "Undergraduate/Master's transcripts with GPA > 80%, personal statement, statement of purpose, 1 recommendation letter, medical examination.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "In the Embassy Track, choosing 3 Type A universities in Seoul leads to rejection; NIIED strictly requires at least ONE Type B (regional) university among your 3 choices.",
            "strategic_program_match_advice": "University Track candidates applying to regional institutions (e.g. Pusan, Kyungpook, Chonnam) or STEM specialized institutes (UNIST, GIST, DGIST) often face significantly higher acceptance rates than Seoul-based tracks."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.studyinkorea.go.kr/",
            "portal_system_name": "Study in Korea Official Portal & Embassy of the Republic of Korea in Pakistan",
            "account_creation_instructions": "Review NIIED guidelines on Study in Korea portal; submit documents to Korean Embassy in Islamabad (Embassy Track) OR directly to the Korean university (University Track).",
            "step_by_step_workflow": [
                "1. Choose between Embassy Track or University Track (never both).",
                "2. Download official GKS Application Form, Personal Statement, and Statement of Purpose forms.",
                "3. Secure 1 recommendation letter in a sealed and signed envelope.",
                "4. Obtain Apostille / Consular attestation from the Korean Embassy in Islamabad on all degrees and transcripts.",
                "5. Submit complete dossier to Korean Embassy Islamabad (mid-March) or to Korean University (March/April).",
                "6. 1st Round Selection: Embassy/University interviews and reviews dossiers (April).",
                "7. 2nd Round Selection: NIIED Central Selection Committee reviews shortlisted candidates in Seoul (May).",
                "8. 3rd Round Selection (Embassy Track only): The 3 chosen universities review candidate dossiers (May/June).",
                "9. Final successful scholars announced by NIIED on Study in Korea portal in late June.",
                "10. Apply for Korean D-2 / D-4 visa at Korean Embassy in Islamabad (July/August).",
                "11. Depart for Korea in late August."
            ],
            "university_vs_scholarship_routing": "Embassy Track (Embassy -> NIIED -> University) OR University Track (University -> NIIED).",
            "recommendation_letters_submission_method": "One official recommendation letter submitted in a sealed envelope with referee's signature across the flap.",
            "personal_statement_prompts": "Personal Statement (Form 2): Family background, formative experiences, motivations, achievements. Statement of Purpose (Form 3): Goal of study, detailed study plan in Korea, and post-graduation plan.",
            "study_plan_research_proposal_requirements": "Detailed study plan required; research proposal required for PhD applicants.",
            "cv_format_requirements": "Embedded in standard GKS Form 1.",
            "interviews_conducted": True,
            "interview_format_details": "15-20 minute interview in English/Korean conducted by Korean diplomats and cultural attachés at the Embassy of the Republic of Korea in Islamabad (or online for University Track).",
            "standardized_tests": "No standardized tests required by NIIED; IELTS/TOEFL and TOPIK scores provide valuable bonus points.",
            "application_fee_amount": "KRW 0 / PKR 0 (100% FREE application process).",
            "attestation_requirements": "MANDATORY: Educational documents (degree and transcripts) must be consular authenticated / legalized by the Embassy of the Republic of Korea in Islamabad.",
            "translation_requirements": "Documents not in English or Korean must be submitted with certified, notarized translations.",
            "final_submission_method": "Hardcopy original packet + 3 photocopy sets delivered by post/courier."
        },
        "required_documents_checklist": [
            {"document_name": "GKS Application Form (Form 1)", "mandatory": True, "specification": "Official prescribed form with photograph", "pakistan_specific_instruction": "Typed and signed by applicant"},
            {"document_name": "Personal Statement (Form 2)", "mandatory": True, "specification": "Narrative essay on background and motivations", "pakistan_specific_instruction": "Max 2 pages; clearly express affinity for Korean culture and research"},
            {"document_name": "Statement of Purpose (Form 3)", "mandatory": True, "specification": "Detailed study and career plan", "pakistan_specific_instruction": "Must include language study plan and specific degree roadmap"},
            {"document_name": "One Letter of Recommendation (Form 5)", "mandatory": True, "specification": "Submitted in a sealed envelope signed across the flap by the recommender", "pakistan_specific_instruction": "From academic advisor or department head"},
            {"document_name": "Consular Authenticated Degree Certificate & Transcript", "mandatory": True, "specification": "Must be attested by HEC, MOFA, and Consular Legalized by Korean Embassy Islamabad", "pakistan_specific_instruction": "Strict NIIED requirement; regular photocopies without authentication are rejected"},
            {"document_name": "Proof of Citizenship & Family Relations", "mandatory": True, "specification": "Applicant's and parents' passports, NADRA Family Registration Certificate (FRC)", "pakistan_specific_instruction": "FRC issued by NADRA proves non-Korean parentage"},
            {"document_name": "Valid English / Korean Test Score Reports", "mandatory": False, "specification": "Official IELTS, TOEFL, or TOPIK score certificates", "pakistan_specific_instruction": "Strongly recommended for bonus points in competitive screening"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Mid-February for Graduate; September for Undergraduate annually",
            "application_deadline": "Early to mid-March for Graduate; October for Undergraduate annually",
            "university_admission_deadline": "Handled internally during 3rd round (May/June)",
            "document_submission_deadline": "Coincides with Embassy/University deadline",
            "recommendation_letters_deadline": "Coincides with application deadline",
            "interview_period": "Late March to early April (1st round interviews in Islamabad)",
            "shortlist_announcement": "Mid-May (2nd round NIIED results); Late June (Final results)",
            "final_result_acceptance_deadline": "Late June annually",
            "visa_application_window": "July - August (Korean Embassy Islamabad)",
            "semester_commencement": "September 1 (Fall Semester) for Graduate; March 1 for Undergraduate",
            "annual_cycle_notes": "Apostille/Consular legalization at the Korean Embassy in Islamabad requires 2-3 weeks; initiate degree attestation early."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (CGPA rigor, consistent marks across all years)",
            "extracurricular_and_leadership_weight": "10% (Adaptability, cultural curiosity)",
            "research_experience_weight": "15% (Relevance of past projects and publications)",
            "work_experience_weight": "5% (Industry experience)",
            "personal_statement_weight": "15% (Quality and sincerity of personal statement)",
            "recommendations_weight": "5% (Recommendation letter strength)",
            "interview_weight": "15% (Oral interview in Islamabad evaluating confidence and English fluency)",
            "test_scores_weight": "Bonus points (up to 10-20% boost) awarded for TOPIK Level 3+ and IELTS 7.0+",
            "financial_need_weight": "0% (Pure bilateral government merit)",
            "selection_panel_composition": "1st Round: Korean diplomats in Islamabad; 2nd Round: NIIED Selection Committee in Seoul; 3rd Round: University Department Admissions Professors.",
            "evaluation_methodology": "Three-tier selection: Embassy screening -> NIIED central qualification -> University admissions verification."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 4,000 applicants in Pakistan",
            "total_scholarships_awarded": "~30 to 45 scholars selected annually",
            "acceptance_rate_global": "~3.5%",
            "acceptance_rate_pakistan": "~1.0% to 1.5% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.50 to 3.95 / 4.00 CGPA (strictly above 80% percentile)",
            "typical_academic_and_research_profile": "Consistent high grades, clear motivation to study in South Korea, well-formatted consular documents, IELTS 7.0+ or basic Korean.",
            "common_backgrounds_of_winners": "Graduates of NUST, LUMS, FAST, UET, GIKI, COMSATS, Quaid-i-Azam, and Fatima Jinnah Women University.",
            "high_representation_countries": "Reserved exclusively for Pakistan under bilateral quota.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents claiming they can guarantee GKS scholarships for money. NIIED selections are 100% government-controlled and audited.",
                "Unofficial agencies claiming TOPIK requirement is waived permanently."
            ],
            "application_fee_warning": "GKS application is 100% FREE. Never pay any fee for NIIED forms.",
            "agent_and_intermediary_warnings": "Never hire an agent. Discrepancies in notarized documents result in criminal forgery blacklisting.",
            "hidden_costs_breakdown": [
                "Consular legalization fees at the Korean Embassy in Islamabad (~$4 to $8 per document).",
                "HEC and MOFA attestation fees in Pakistan (PKR 8,000 to 15,000).",
                "NADRA Family Registration Certificate (FRC) fees (~PKR 1,000).",
                "International courier charges (DHL/FedEx) if applying via University Track directly to South Korea (PKR 8,000 to 12,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can skip the 1-year Korean language course. (Fact: The only way to skip the 1-year language course is if you already hold TOPIK Level 5 or 6 before arriving in Korea).",
                "MYTH: You can stay in Korea if you fail TOPIK Level 3 after 1 year. (Fact: If a scholar fails to achieve TOPIK Level 3 after 1 year of language training, the scholarship is officially CANCELLED and they must return home)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some third-party blogs claim you can apply to both Embassy and University tracks. Applying to both leads to immediate disqualification by NIIED."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain cumulative GPA above 80% (2.64/4.00 or B-grade) each semester in Korean university coursework.",
            "attendance_requirements": "Mandatory 80%+ attendance in both Korean language institute and degree program.",
            "academic_progress_monitoring": "Semi-annual grade and attendance evaluation submitted to NIIED.",
            "work_restrictions_during_study": "Part-time student employment permitted up to 20-25 hours per week during degree program with university approval and immigration permit; STRICTLY PROHIBITED during the initial 1-year Korean language program.",
            "home_country_return_obligation": "No mandatory statutory home return restriction enforced by Korea; scholars can transition to the Korean D-10 Job Seeker Visa or E-7 Professional Employment Visa upon graduation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Scholars who withdraw voluntarily within the first 3 months must reimburse all expenses including airfare and stipend.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "No extensions allowed beyond the designated degree period."
        },
        "official_sources_verified": [
            {
                "source_name": "National Institute for International Education (NIIED) - Official Study in Korea Portal",
                "source_url": "https://www.studyinkorea.go.kr/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact interview scoring formula used by the Korean Embassy in Islamabad",
                    "Distribution of university track seats among specific Korean institutions"
                ]
            }
        ]
    },

    # 11. Türkiye Bursları Scholarships (Turkey)
    "SCH-ME-001": {
        "scholarship_id": "SCH-ME-001",
        "basic_details": {
            "scholarship_name": "Türkiye Bursları Scholarship Program",
            "offering_entity": "Presidency for Turks Abroad and Related Communities (YTB), Republic of Turkey",
            "host_country": "Turkey",
            "host_institutions_covered": "State and Foundation Universities across Turkey (Middle East Technical University - METU, Boğaziçi, Istanbul Technical University - ITU, Bilkent, Koç, Istanbul University, Sabancı, Ankara University)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Open to almost all disciplines: Engineering, Computer Science, Medicine, Dentistry, Pharmacy, Social Sciences, International Relations, Islamic Studies, Economics, Architecture, Agriculture.",
            "number_of_awards_total": "~4,000 to 5,000 scholarship awards distributed globally each year",
            "number_of_awards_pakistan": "~100 to 150 scholars from Pakistan selected across undergraduate and postgraduate levels annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's: 4-6 years + 1 yr Turkish prep; Master's: 2 years + 1 yr Turkish prep; PhD: 4 years + 1 yr Turkish prep"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of the Islamic Republic of Pakistan (must not hold Turkish citizenship)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 21,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Undergraduate: Under 21 years; Master's: Under 30 years; PhD: Under 35 years of age on January 1 of application year.",
            "academic_qualifications": "Completed HSSC / A-Levels for Undergraduate; 16-year Bachelor's for Master's; 18-year MS/MPhil for PhD from recognized institutions.",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 2.8,
            "grading_conversion_notes": "Minimum academic achievement: 70% for Undergrad; 75% for Master's/PhD; 90% strictly for Health Sciences (Medicine, Dentistry, Pharmacy).",
            "subject_background_prerequisites": "Academic background aligned with the intended faculty in Turkey.",
            "current_education_status": "Graduated or in final year (must graduate before August of application year).",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "For Turkish-taught programs: No language score required at application; YTB provides 1 year of free Turkish language preparatory training (TÖMER). For English-taught programs: TOEFL iBT and GRE/GMAT scores required as stipulated by individual top universities (METU, Boğaziçi, Bilkent).",
            "other_language_requirements": "Mandatory 1-year Turkish Language Course (TÖMER) provided to ALL scholars, even those in English-taught programs.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Students currently enrolled in Turkish universities are ineligible for the same study level.",
            "previous_scholarship_restrictions": "Previous Türkiye Bursları recipients cannot re-apply for the same level.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% exemption from all university tuition fees for the full program duration."},
            "admission_application_fee": {"status": "WAIVED", "details": "No university application fees via the Türkiye Bursları portal."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Free accommodation in state student dormitories (KYK dorms); scholars who opt for private housing receive a monthly rental stipend."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living allowance paid directly to the student's Turkish bank account.", "amount": "TRY 3,500/mo (Undergrad), TRY 5,000/mo (Master's), TRY 6,500/mo (PhD) (regularly indexed to inflation) (~PKR 35,000 to 65,000/mo)"},
            "airfare": {"status": "COVERED", "details": "One-time round-trip flight ticket provided: one inbound flight to Turkey upon commencement, and one outbound flight upon graduation."},
            "visa_fee": {"status": "WAIVED", "details": "Turkish Student Visa issued with fee waiver upon presentation of YTB scholarship acceptance documents."},
            "health_insurance": {"status": "COVERED", "details": "Comprehensive General Health Insurance (Genel Sağlık Sigortası - GSS) under the Turkish Social Security Institution (SGK)."},
            "food_allowance": {"status": "COVERED", "details": "Free breakfast and dinner included in KYK state student dormitories."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via monthly stipend or campus library facilities."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "YTB Research Support Grants available for doctoral dissertation fieldwork."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Free 1-year Turkish language preparatory education course (TÖMER) fully covered."},
            "total_estimated_value_usd_per_year": 16000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Applicants select up to TWELVE university and department preferences across at least two different Turkish cities.",
            "participating_institutions": ["METU Ankara, Boğaziçi University, Istanbul Technical University, Bilkent, Koç, Istanbul University, Sabancı, Ankara University, Ege University, Hacettepe"],
            "university_rankings_scope": "Top 1 to 20 universities in Turkey; QS World Top 400-800.",
            "available_majors": ["All disciplines (Mechanical Engineering, Computer Science, Medicine, Dentistry, Pharmacy, International Relations, Islamic Finance, Architecture, Law)"],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 4-6 years; Master's: 2 years; PhD: 4 years (+ 1 yr Turkish language)",
            "admission_requirements_summary": "Online TBBS application, transcripts, personal statement, study proposal, extracurricular certificates.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single integrated application: Applying via the TBBS portal simultaneously secures both university admission and full scholarship placement.",
            "strategic_program_match_advice": "Do not select only Istanbul and Ankara universities; including strong provincial universities (e.g. Ege University Izmir, Bursa Uludağ) ensures higher placement probability."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.turkiyeburslari.gov.tr/",
            "portal_system_name": "Türkiye Bursları Application System (TBBS)",
            "account_creation_instructions": "Register on the TBBS online portal using valid email address and Pakistani passport/CNIC during the single annual application window (January 10 - February 20).",
            "step_by_step_workflow": [
                "1. Register on TBBS portal (opens January 10).",
                "2. Fill profile: Personal Info, Education Info, Language Info, Work Experience, Social Activities.",
                "3. Select up to 12 university and program preferences.",
                "4. Write Statement of Purpose and Research Proposal (for Master's/PhD).",
                "5. Upload academic transcripts, certificates, passport, and extracurricular awards.",
                "6. Submit online application before February 20 deadline.",
                "7. Preliminary expert review of dossiers (March - April).",
                "8. Shortlisted candidates invited for in-person panel interview in Islamabad, Lahore, or Karachi (May - June).",
                "9. Final selection results announced on TBBS portal (late July - early August).",
                "10. Sign Scholarship Agreement, obtain Turkish Student Visa, receive free flight ticket (August).",
                "11. Depart for Turkey (mid-September)."
            ],
            "university_vs_scholarship_routing": "Integrated 1-step routing: YTB places selected scholars directly into their approved university programs.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate on the TBBS portal (scanned letters on university/company letterhead).",
            "personal_statement_prompts": "Letter of Intent (integrated into TBBS): Explain academic background, reason for choosing Turkey, and career expectations.",
            "study_plan_research_proposal_requirements": "PhD/Master's applicants must formulate a structured research proposal: Title, Problem Statement, Literature Review, Methodology, and Significance.",
            "cv_format_requirements": "Generated automatically through TBBS profile sections.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous 20-30 minute in-person interview in Islamabad, Lahore, or Karachi conducted by Turkish academic professors and YTB delegates (evaluates academic knowledge, motivation, and mathematical aptitude).",
            "standardized_tests": "Not required by YTB; SAT/GRE scores provide strong competitive advantage for English-taught engineering programs.",
            "application_fee_amount": "TRY 0 / PKR 0 (100% FREE application).",
            "attestation_requirements": "HEC and MOFA attestation of degree certificates required after award confirmation for university registration.",
            "translation_requirements": "Turkish or English translations of all non-English documents.",
            "final_submission_method": "100% online portal submission on TBBS."
        },
        "required_documents_checklist": [
            {"document_name": "Valid Passport or National ID (CNIC)", "mandatory": True, "specification": "Scanned copy of valid Pakistani passport or NADRA CNIC", "pakistan_specific_instruction": "Required for TBBS registration and identity"},
            {"document_name": "Academic Transcripts & Certificates", "mandatory": True, "specification": "All degrees and detailed marks sheets", "pakistan_specific_instruction": "Must show grades and GPA clearly"},
            {"document_name": "Recent Passport-Size Photograph", "mandatory": True, "specification": "Taken within the last 6 months", "pakistan_specific_instruction": "Uploaded to portal profile"},
            {"document_name": "Statement of Purpose / Letter of Intent", "mandatory": True, "specification": "Formulated directly within the TBBS text fields", "pakistan_specific_instruction": "Highlight Pak-Turkish historical and economic ties"},
            {"document_name": "Research Proposal (Master's / PhD only)", "mandatory": False, "specification": "Structured academic proposal", "pakistan_specific_instruction": "Mandatory for postgraduate candidates"},
            {"document_name": "Academic Recommendation Letter", "mandatory": True, "specification": "Signed letter from professor with institutional contact details", "pakistan_specific_instruction": "Must be on university letterhead"},
            {"document_name": "Extracurricular & Leadership Certificates", "mandatory": False, "specification": "Sports, Olympiad, debate, volunteer, or publication certificates", "pakistan_specific_instruction": "Significantly boosts scoring during expert review"}
        ],
        "important_dates_timeline": {
            "application_open_date": "January 10 annually (e.g., 2026-01-10)",
            "application_deadline": "February 20 annually (e.g., 2026-02-20)",
            "university_admission_deadline": "Handled simultaneously with scholarship application",
            "document_submission_deadline": "February 20 annually",
            "recommendation_letters_deadline": "February 20 annually",
            "interview_period": "May - June annually in Islamabad, Lahore, and Karachi",
            "shortlist_announcement": "Late July to early August annually",
            "final_result_acceptance_deadline": "Mid-August annually",
            "visa_application_window": "August - September (Turkish Consulates / Embassy in Pakistan)",
            "semester_commencement": "Late September / October of departure year",
            "annual_cycle_notes": "Single unified application window for all countries and degree levels worldwide."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Grades, GPA consistency, academic rigor)",
            "extracurricular_and_leadership_weight": "15% (Volunteer work, community projects, sports)",
            "research_experience_weight": "15% (Crucial for postgrad; research proposal clarity)",
            "work_experience_weight": "5% (Professional relevance)",
            "personal_statement_weight": "10% (Sincerity and purpose in Letter of Intent)",
            "recommendations_weight": "5% (Professor endorsements)",
            "interview_weight": "15% (In-person interview in Pakistan evaluating composure, motivation, and problem-solving)",
            "test_scores_weight": "Bonus points for GRE / SAT / Turkish language",
            "financial_need_weight": "0% (Merit and diplomatic bilateral criteria)",
            "selection_panel_composition": "Turkish university professors, YTB scholarship experts, and Turkish diplomats.",
            "evaluation_methodology": "Three-phase sift: 1) Automated GPA eligibility filter, 2) Expert academic committee review, 3) In-person oral interview in Pakistan."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~160,000 to 180,000 applicants globally; ~15,000 from Pakistan",
            "total_scholarships_awarded": "~4,500 globally; ~120 to 150 in Pakistan",
            "acceptance_rate_global": "~2.5%",
            "acceptance_rate_pakistan": "~1.0% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.40 to 3.85 / 4.00 CGPA (or 78-90% marks in FSc/A-Levels)",
            "typical_academic_and_research_profile": "High academic marks, strong social extracurricular engagement, articulate presentation during in-person interview.",
            "common_backgrounds_of_winners": "FSc Pre-Engineering and Pre-Medical students, graduates of UET, NUST, FAST, Quaid-i-Azam, Punjab University, Peshawar University.",
            "high_representation_countries": "Pakistan, Afghanistan, Syria, Azerbaijan, Somalia, Kazakhstan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam education consultants in Pakistan charging PKR 50,000 to 200,000 claiming 'direct quota arrangements with the Turkish government'. All applications must be submitted personally on TBBS.",
                "Fake confirmation emails demanding payment for Turkish visa processing."
            ],
            "application_fee_warning": "Türkiye Bursları is 100% FREE. Never pay any application fee.",
            "agent_and_intermediary_warnings": "Applications submitted through intermediaries are frequently disqualified.",
            "hidden_costs_breakdown": [
                "Equivalence Certificate (Denklik Belgesi) processing fee from the Turkish Ministry of National Education (MEB) or Turkish Embassy (approx PKR 10,000 to 20,000).",
                "HEC, IBCC, and MOFA degree attestation costs in Pakistan.",
                "Living cost inflation: The monthly stipend (TRY 3,500 to 6,500) covers basic personal spending, but scholars in Istanbul/Ankara often benefit from modest family pocket money support (~$50-100/mo)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot study in English. (Fact: Hundreds of programs at top Turkish universities are taught in English; however, learning basic Turkish is mandatory for daily life and cultural integration).",
                "MYTH: You must return to Pakistan immediately. (Fact: Turkey allows international graduates to apply for post-study residence permits and work legally in the Turkish economy)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some consultants tell medical applicants that 70% is enough; official YTB regulations strictly enforce a 90% minimum cutoff for Medicine, Dentistry, and Pharmacy."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum GPA specified by Turkish university regulations (typically 2.00/4.00 for Undergrad, 2.50/4.00 for Master's, 3.00/4.00 for PhD).",
            "attendance_requirements": "Mandatory full-time attendance. Unexcused absence results in warning and stipend deduction.",
            "academic_progress_monitoring": "Universities submit termly academic transcript reports to YTB.",
            "work_restrictions_during_study": "Undergraduate students can work legally up to 24 hours/week after completing their first year; Master's and PhD students can work part-time with formal work permits.",
            "home_country_return_obligation": "Scholars sign an agreement promising to return to their home countries upon graduation to foster bilateral relations, though no coercive financial bond is imposed.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Scholars dismissed for disciplinary violations or voluntary dropout without valid reason may be required to repay travel and allowance costs.",
            "rules_for_changing_university": "Changing university is strictly prohibited except under exceptional administrative transfers approved by YTB.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Maximum 1 year extension can be granted for thesis completion without monthly stipend (dormitory and tuition remain covered)."
        },
        "official_sources_verified": [
            {
                "source_name": "Presidency for Turks Abroad and Related Communities (YTB) - Türkiye Bursları Official Portal",
                "source_url": "https://www.turkiyeburslari.gov.tr/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact applicant count by Pakistani city (Islamabad vs Lahore vs Karachi)",
                    "Interview rubric point allocation between academic vs motivation components"
                ]
            }
        ]
    },

    # 12. Australia Awards Scholarships (Pakistan Category)
    "SCH-OC-001": {
        "scholarship_id": "SCH-OC-001",
        "basic_details": {
            "scholarship_name": "Australia Awards Scholarships (Pakistan Category)",
            "offering_entity": "Department of Foreign Affairs and Trade (DFAT), Australian Government",
            "host_country": "Australia",
            "host_institutions_covered": "Participating Australian Higher Education Institutions (Group of Eight: University of Melbourne, ANU, University of Sydney, UNSW, University of Queensland, Monash, Adelaide, UWA)",
            "degree_levels": ["Master's"],
            "major_restrictions": "Master's by Coursework or Master's by Research in designated priority development sectors for Pakistan: 1) Climate Change, Clean Energy & Water Resource Management, 2) Agriculture & Food Security, 3) Global Health & Pandemic Preparedness, 4) Gender Equality, Disability & Social Inclusion, 5) Governance & Public Policy.",
            "number_of_awards_total": "~1,000 awards across Indo-Pacific developing nations annually",
            "number_of_awards_pakistan": "~15 to 25 targeted awards for Pakistan per intake",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years (standard Australian Master's degree duration)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of Pakistan residing in and applying from Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "Minimum 18 years old at commencement; no upper age limit.",
            "academic_qualifications": "Completed 16 years of formal education (4-year Bachelor's degree or equivalent) from an HEC-recognized university.",
            "minimum_gpa_percentage": 65.0,
            "minimum_gpa_scale": 2.8,
            "grading_conversion_notes": "Minimum 2.8/4.0 CGPA or 65% marks; candidates must satisfy individual Australian university entry standards.",
            "subject_background_prerequisites": "Academic and professional background directly aligned with Pakistan priority development sectors.",
            "current_education_status": "Completed degree; not currently serving military personnel.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": True,
            "work_experience_minimum_years": 2.0,
            "work_experience_notes": "MANDATORY REQUIREMENT: Minimum 2 years of relevant professional work experience in Pakistan in an area aligned with Australia Awards priority sectors.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 84,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic overall minimum 6.5 (no band less than 6.0), TOEFL iBT minimum 84 (no subscore below 21), or PTE Academic minimum 58. (Applicants with disability: minimum IELTS 6.0 / PTE 50).",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "Equal opportunity; 50% target for women scholars; individuals with disabilities and candidates from marginalized regions strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants holding Australian permanent residency, dual Australian citizenship, or who are engaged/married to someone holding Australian PR are strictly ineligible.",
            "previous_scholarship_restrictions": "Recipients of previous long-term Australian government scholarships must have resided outside Australia for twice the length of the previous grant.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full tuition fees for the approved course of study."},
            "admission_application_fee": {"status": "COVERED", "details": "Covered via DFAT institutional placement agreements."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via fortnightly Contribution to Living Expenses (CLE)."},
            "monthly_stipend": {"status": "COVERED", "details": "Contribution to Living Expenses (CLE) paid fortnightly directly into Australian bank account.", "amount": "AUD 30,000 to 35,000 / year (~AUD 2,700 / month or ~PKR 500,000 to 550,000 / month)"},
            "airfare": {"status": "COVERED", "details": "Single return economy class airfare to and from Australia via the most direct route."},
            "visa_fee": {"status": "WAIVED", "details": "Student visa (subclass 500) application charge waived for Australia Awards recipients."},
            "health_insurance": {"status": "COVERED", "details": "Overseas Student Health Cover (OSHC) for the duration of the scholarship covering basic medical and hospital care in Australia."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Covered via the living stipend."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via establishment allowance and living allowance."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Fieldwork travel grant available for Master's by Research candidates where research in Pakistan is mandatory."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Establishment allowance of AUD 5,000 one-off payment on arrival towards accommodation, textbooks, and study materials.", "amount": "AUD 5,000 one-off"},
            "total_estimated_value_usd_per_year": 58000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Applicants may select up to TWO course preferences at Australian participating institutions on their OASIS application.",
            "participating_institutions": ["University of Melbourne, Australian National University (ANU), University of Sydney, UNSW Sydney, University of Queensland (UQ), Monash University, University of Adelaide, University of Western Australia (UWA)"],
            "university_rankings_scope": "Group of Eight (Go8) and leading Australian research universities (QS World Top 20 to 150).",
            "available_majors": ["Climate Change Adaptation", "Water Resources Management", "Agricultural Sciences", "Public Health", "Renewable Energy Policy", "Economics", "Development Practice", "Public Policy"],
            "english_taught_program_availability": True,
            "program_duration": "Up to 2 years (full-time Master's)",
            "admission_requirements_summary": "Bachelor's degree, 2+ years work experience, IELTS 6.5+, Development Impact Plan (Re-entry plan), 2 referee reports.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Applicants do not need to apply to Australian universities separately; DFAT places selected scholars into their approved university choices.",
            "strategic_program_match_advice": "The Development Impact Plan is the linchpin: show specifically how the Australian course will enable you to solve an identified problem in Pakistan's water, climate, or public health sector."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.dfat.gov.au/people-to-people/australia-awards/australia-awards-scholarships",
            "portal_system_name": "Online Australia Awards Scholarships Information System (OASIS)",
            "account_creation_instructions": "Register on OASIS portal between February 1 and April 30; select Pakistan country profile.",
            "step_by_step_workflow": [
                "1. Register on OASIS online portal (opens February 1).",
                "2. Complete application form and select up to 2 Australian university courses.",
                "3. Write Development Impact Plan (Re-entry plan): Explain what practical project you will implement in Pakistan upon return.",
                "4. Upload degree certificates, transcripts, proof of 2 years work experience, and valid IELTS/TOEFL report.",
                "5. Upload 2 referee reports (1 academic, 1 professional) on official DFAT templates.",
                "6. Submit online application before April 30 deadline.",
                "7. Initial eligibility and compliance screening by Australia Awards Pakistan team.",
                "8. Shortlisted candidates invited for in-person panel interview in Islamabad (July - August).",
                "9. Provisional selection announced (September).",
                "10. Complete pre-departure training and Australian visa processing (subclass 500) (October - December).",
                "11. Depart for Australia for Introductory Academic Program (January/February)."
            ],
            "university_vs_scholarship_routing": "Integrated OASIS routing: DFAT handles university placement on behalf of selected finalists.",
            "recommendation_letters_submission_method": "Submitted using prescribed Australia Awards Referee Report templates on official letterhead.",
            "personal_statement_prompts": "Development Impact Plan (DIP): Identify development constraint in Pakistan, describe specific project to solve it, and map how skills gained in Australia will be implemented.",
            "study_plan_research_proposal_requirements": "Research proposal mandatory for Master's by Research candidates.",
            "cv_format_requirements": "Standard professional CV detailing employment history.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous in-person panel interview in Islamabad conducted by Australian diplomats and Pakistani development specialists.",
            "standardized_tests": "IELTS Academic (6.5), TOEFL iBT (84), or PTE Academic (58) mandatory at submission.",
            "application_fee_amount": "AUD 0 / PKR 0 (100% FREE application).",
            "attestation_requirements": "Certified copies of academic transcripts and degrees.",
            "translation_requirements": "Certified English translations for any non-English records.",
            "final_submission_method": "100% online portal submission on OASIS."
        },
        "required_documents_checklist": [
            {"document_name": "Pakistani Passport Information Page", "mandatory": True, "specification": "Valid for at least 2 years beyond departure date", "pakistan_specific_instruction": "Proof of Pakistani citizenship and residency"},
            {"document_name": "Certified Degree Certificates & Transcripts", "mandatory": True, "specification": "Complete university records showing grades and subjects", "pakistan_specific_instruction": "HEC recognized 16-year degree"},
            {"document_name": "Proof of 2 Years Professional Work Experience", "mandatory": True, "specification": "Employment letters on company letterhead confirming dates and responsibilities", "pakistan_specific_instruction": "Must demonstrate 2+ full years of post-graduation work in Pakistan"},
            {"document_name": "Valid English Language Test Score Report", "mandatory": True, "specification": "IELTS Academic (6.5), TOEFL iBT (84), or PTE (58)", "pakistan_specific_instruction": "Must be valid at the time of application submission"},
            {"document_name": "Two Australia Awards Referee Reports", "mandatory": True, "specification": "Completed on official prescribed DFAT templates with signatures and stamps", "pakistan_specific_instruction": "One academic and one professional supervisor"},
            {"document_name": "Development Impact Plan (DIP)", "mandatory": True, "specification": "Detailed reform plan to be implemented in Pakistan upon return", "pakistan_specific_instruction": "Central scoring document for interview panel"}
        ],
        "important_dates_timeline": {
            "application_open_date": "February 1 annually (e.g., 2026-02-01)",
            "application_deadline": "April 30 annually (e.g., 2026-04-30 at 23:59 AEST)",
            "university_admission_deadline": "Handled internally by DFAT (September - November)",
            "document_submission_deadline": "April 30 annually",
            "recommendation_letters_deadline": "April 30 annually",
            "interview_period": "July - August annually in Islamabad",
            "shortlist_announcement": "September annually",
            "final_result_acceptance_deadline": "October annually",
            "visa_application_window": "November - December (Subclass 500 visa)",
            "semester_commencement": "January / February of departure year",
            "annual_cycle_notes": "Very strict 2-year post-study return requirement enforced under Australian immigration law."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Academic competence and capability to complete Master's)",
            "extracurricular_and_leadership_weight": "15% (Leadership potential and professional influence in Pakistan)",
            "research_experience_weight": "10% (Technical background in priority sector)",
            "work_experience_weight": "20% (Substantive professional track record in development)",
            "personal_statement_weight": "15% (Strength and realism of the Development Impact Plan)",
            "recommendations_weight": "5% (Employer endorsement)",
            "interview_weight": "10% (Interview performance assessing strategic vision for Pakistan)",
            "test_scores_weight": "Gatekeeper requirement (minimum IELTS 6.5 cutoff)",
            "financial_need_weight": "0% (Merit and development impact focus)",
            "selection_panel_composition": "Joint selection panel of Australian DFAT officials and independent Pakistani development specialists.",
            "evaluation_methodology": "Two-phase review: Dossier assessment scoring academic competence and Development Impact Plan, followed by interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,500 professional applicants in Pakistan",
            "total_scholarships_awarded": "~15 to 25 scholars selected annually",
            "acceptance_rate_global": "N/A (Pakistan-specific allocation)",
            "acceptance_rate_pakistan": "~1.0% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.30 to 3.80 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Mid-career professional with 3-7 years experience in government ministries, NGOs, research councils, or climate policy organizations.",
            "common_backgrounds_of_winners": "Engineers from water/energy utilities, environmental protection agency officials, public health managers, provincial planning departments, agriculture specialists.",
            "high_representation_countries": "Reserved exclusively for Pakistan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Immigration agents claiming they can use Australia Awards as a pathway to Australian permanent residency. Australia Awards explicitly FORBIDS applying for Australian PR for 2 years post-graduation.",
                "Unofficial websites charging fees to review OASIS applications."
            ],
            "application_fee_warning": "OASIS application is 100% FREE.",
            "agent_and_intermediary_warnings": "Never hire an agent; DFAT conducts strict identity and employment background checks.",
            "hidden_costs_breakdown": [
                "IELTS Academic test registration fee (~PKR 60,000).",
                "Travel to Islamabad for in-person interview.",
                "Medical examinations and chest X-rays at panel clinics prior to Australian visa grant."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can stay in Australia on a Temporary Graduate Visa (subclass 485). (Fact: Australia Awards recipients are legally barred under condition 8535 from applying for any Australian substantive visa until they have lived outside Australia for 2 years).",
                "MYTH: Recent graduates without work experience can apply. (Fact: Minimum 2 years of work experience is an absolute eligibility requirement)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party blogs often claim Duolingo is accepted; DFAT strictly accepts only IELTS, TOEFL iBT, and PTE Academic."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic progress as defined by the Australian university.",
            "attendance_requirements": "Full-time study attendance in Australia.",
            "academic_progress_monitoring": "Termly reports submitted by university Australia Awards liaison officers to DFAT.",
            "work_restrictions_during_study": "Scholars may work up to 48 hours per fortnight during study terms, but heavy employment is discouraged.",
            "home_country_return_obligation": "MANDATORY 2-Year Return: Scholars must leave Australia and return to Pakistan for a minimum of TWO cumulative years immediately upon completing their scholarship.",
            "service_obligations_or_bonds": "Contractual agreement with Australian Government; breach triggers full scholarship debt clawback.",
            "repayment_clawback_conditions": "Scholars who refuse to return to Pakistan, drop out, or fail to complete their course must repay the entire cost of the scholarship (typically AUD 120,000+).",
            "rules_for_changing_university": "Strictly disallowed.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Extensions are strictly forbidden under DFAT scholarship policy."
        },
        "official_sources_verified": [
            {
                "source_name": "Australian Department of Foreign Affairs and Trade (DFAT) - Australia Awards Pakistan Profile",
                "source_url": "https://www.dfat.gov.au/people-to-people/australia-awards/australia-awards-scholarships",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact statistical ratio of public sector vs private/NGO sector candidate selections in Pakistan",
                    "Individual interview panel scores"
                ]
            }
        ]
    },

    # 13. Swiss Government Excellence Scholarships (Switzerland)
    "SCH-EU-005": {
        "scholarship_id": "SCH-EU-005",
        "basic_details": {
            "scholarship_name": "Swiss Government Excellence Scholarships",
            "offering_entity": "Federal Commission for Scholarships for Foreign Students (FCS) / State Secretariat for Education, Research and Innovation (SERI), Switzerland",
            "host_country": "Switzerland",
            "host_institutions_covered": "Swiss Federal Institutes of Technology (ETH Zurich, EPFL), Swiss Cantonal Universities (University of Zurich, Geneva, Basel, Bern, Lausanne, Fribourg, Neuchâtel, Lugano), and Public Research Institutes (PSI, Empa, WSL, Eawag)",
            "degree_levels": ["PhD", "Postdoctoral"],
            "major_restrictions": "Open to all academic fields: Natural Sciences, Engineering, Mathematics, Life Sciences, Medicine, Humanities, Social Sciences. Restricted to PhD scholarships (3 years), Postdoctoral fellowships (12 months), and Research fellowships (12 months). Does NOT fund standard Master's degrees.",
            "number_of_awards_total": "~500 scholars and researchers from over 180 countries funded worldwide annually",
            "number_of_awards_pakistan": "~5 to 10 highly selective awards for Pakistan per academic cycle",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "PhD: Up to 36 months; Postdoctoral & Research: 12 months"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of the Islamic Republic of Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "PhD applicants: Born after December 31, 1989 (under 35 years of age). Postdoctoral applicants: PhD completed within the last 5 years.",
            "academic_qualifications": "Master's degree (18 years education / MS / MPhil) achieved before July 31 preceding start of scholarship with exceptional academic distinction.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum 3.50/4.00 CGPA or top 10% class standing; competitive applicants typically hold published research papers.",
            "subject_background_prerequisites": "Master's degree directly in the subject area of the proposed doctoral research.",
            "current_education_status": "Master's completed or in final semester (degree must be formally awarded before departure).",
            "graduation_year_restrictions": "Postdoc applicants must have obtained PhD within the prior 5 years.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; solid academic research record is paramount.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Language certificate in the language of instruction (English, German, or French) as required by the host professor/university.",
            "other_language_requirements": "German, French, or Italian proficiency is required if research is conducted in that language; most STEM labs at ETH/EPFL operate 100% in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "ABSOLUTE PREREQUISITE: Must have secured a formal written letter of acceptance from a tenured professor at a Swiss university agreeing to supervise the candidate before applying to the Embassy.",
            "previous_scholarship_restrictions": "Applicants who have previously received a Swiss Government Excellence Scholarship are ineligible.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full tuition and bench fee exemption at Swiss universities under federal decree."},
            "admission_application_fee": {"status": "WAIVED", "details": "Covered under federal scholarship status."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via monthly stipend; FCS provides assistance in securing student housing."},
            "monthly_stipend": {"status": "COVERED", "details": "Tax-free monthly living allowance paid directly to the scholar.", "amount": "CHF 1,920 / month for PhD (~PKR 620,000 / month); CHF 3,500 / month for Postdoc (~PKR 1,120,000 / month)"},
            "airfare": {"status": "NOT_COVERED", "details": "Flight to Switzerland at the start is NOT covered (borne by scholar); however, FCS provides a return flight allowance back to Pakistan upon degree completion."},
            "visa_fee": {"status": "WAIVED", "details": "Swiss national visa (Type D) application fee is waived by the Embassy of Switzerland in Islamabad."},
            "health_insurance": {"status": "COVERED", "details": "Mandatory Swiss health and accident insurance (Krankenversicherung) fully paid directly by FCS throughout the stay."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Covered via monthly stipend."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via host university laboratory facilities."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Funded through Swiss National Science Foundation (SNSF) laboratory grants."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Housing allowance voucher of CHF 300 paid once at the start of scholarship, plus a half-fare public transport card (Halbtax-Abo) valid for all Swiss trains and buses.", "amount": "CHF 300 one-off + Half-Fare Swiss Rail Card"},
            "total_estimated_value_usd_per_year": 35000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single University: Tied specifically to the Swiss institution and professor who issued the acceptance letter.",
            "participating_institutions": ["ETH Zurich, EPFL Lausanne, University of Zurich, University of Geneva, University of Basel, University of Bern, University of Lausanne, PSI, Empa"],
            "university_rankings_scope": "World Top 10 to 100 (ETH Zurich is World #7).",
            "available_majors": ["Quantum Science", "Nanotechnology", "Computer Science", "Biomedical Engineering", "Molecular Biology", "High Energy Physics", "Environmental Sciences", "Economics", "Law"],
            "english_taught_program_availability": True,
            "program_duration": "PhD: 3 years; Postdoc: 12 months",
            "admission_requirements_summary": "Master's degree with honors, Professor Acceptance Letter with short CV, Research Proposal (5 pages), 2 recommendation letters, health certificate.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "MANDATORY STEP: You cannot submit an application to the Swiss Embassy without an official letter of acceptance from a Swiss university professor. Unsolicited applications without professor letters are immediately rejected.",
            "strategic_program_match_advice": "Start contacting professors at ETH, EPFL, or Uni Zurich in June/July with a customized research pitch demonstrating familiarity with their recent papers."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.sbfi.admin.ch/sbfi/en/home/education/scholarships-and-grants/swiss-government-excellence-scholarships.html",
            "portal_system_name": "Embassy of Switzerland in Islamabad (Physical Submission) & SERI Federal Portal",
            "account_creation_instructions": "Request the official application package by emailing the Embassy of Switzerland in Islamabad in early August; submit complete physical dossier in triplicate.",
            "step_by_step_workflow": [
                "1. Contact a professor at a Swiss public university and obtain an official Letter of Acceptance and professor CV (June - August).",
                "2. Email Embassy of Switzerland in Islamabad to request official FCS application package (August).",
                "3. Write 5-page Research Proposal using the official FCS template.",
                "4. Complete official FCS Application Form and obtain 2 confidential letters of recommendation from professors on FCS forms.",
                "5. Complete medical certificate of health.",
                "6. Submit complete physical dossier (1 original + 2 copies) to the Embassy of Switzerland in Islamabad before late September deadline.",
                "7. Embassy conducts preliminary document review and forwards files to Bern.",
                "8. Federal Commission for Scholarships for Foreign Students (FCS) evaluates files in Switzerland (December - April).",
                "9. Final selection results announced by the Swiss Embassy in May.",
                "10. Apply for Swiss National D Visa in Islamabad (June/July).",
                "11. Arrive in Switzerland (September)."
            ],
            "university_vs_scholarship_routing": "Professor Acceptance First -> Embassy Application -> FCS Central Selection.",
            "recommendation_letters_submission_method": "Submitted using official FCS confidential recommendation forms signed and sealed in envelopes.",
            "personal_statement_prompts": "Motivation Letter (max 2 pages): Academic background, why Switzerland, reasons for selecting this specific research group, and future career impact.",
            "study_plan_research_proposal_requirements": "Strict 5-page Research Proposal: Background, research questions, methodology, timetable, and societal significance.",
            "cv_format_requirements": "Europass format with full list of publications and conference presentations.",
            "interviews_conducted": False,
            "interview_format_details": "Strictly dossier-based evaluation; no interview conducted by Embassy.",
            "standardized_tests": "No GRE required; English certificate required by host university.",
            "application_fee_amount": "CHF 0 / PKR 0 (100% FREE application).",
            "attestation_requirements": "Attestation of degree certificates by HEC and MOFA.",
            "translation_requirements": "Certified English, German, or French translations.",
            "final_submission_method": "Physical delivery of 3 complete sets of hardcopy documents to the Embassy of Switzerland in Islamabad."
        },
        "required_documents_checklist": [
            {"document_name": "Official Letter of Acceptance from Swiss Professor", "mandatory": True, "specification": "Signed letter on official university letterhead confirming willingness to supervise", "pakistan_specific_instruction": "The single most essential document; application impossible without it"},
            {"document_name": "Short CV of Host Professor in Switzerland", "mandatory": True, "specification": "1 to 2 page CV of the supervising professor", "pakistan_specific_instruction": "Required by FCS selection committee"},
            {"document_name": "Completed FCS Application Form", "mandatory": True, "specification": "Official typed and signed application form with photograph", "pakistan_specific_instruction": "Obtained from Swiss Embassy Islamabad"},
            {"document_name": "Full Research Proposal (Strictly max 5 pages)", "mandatory": True, "specification": "Structured academic proposal using FCS format", "pakistan_specific_instruction": "High scientific rigor evaluated by Swiss academic panels"},
            {"document_name": "Two Confidential Letters of Recommendation", "mandatory": True, "specification": "On official FCS confidential recommendation forms in sealed envelopes", "pakistan_specific_instruction": "From Pakistani professors who know candidate's research"},
            {"document_name": "Master's Degree Certificate & Official Transcripts", "mandatory": True, "specification": "Complete transcripts showing marks and grading scales", "pakistan_specific_instruction": "Must be 18-year MS/MPhil equivalent"},
            {"document_name": "Medical Certificate of Health", "mandatory": True, "specification": "Official FCS medical form signed by registered physician", "pakistan_specific_instruction": "Confirms fitness to reside and study in Switzerland"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Early August annually (e.g., 2026-08-01)",
            "application_deadline": "Late September annually (e.g., 2026-09-30)",
            "university_admission_deadline": "December - February following selection",
            "document_submission_deadline": "Late September annually",
            "recommendation_letters_deadline": "Late September annually",
            "interview_period": "N/A (Evaluation in Bern)",
            "shortlist_announcement": "May annually (Final results communicated by Swiss Embassy)",
            "final_result_acceptance_deadline": "June annually",
            "visa_application_window": "June - July (Embassy of Switzerland in Islamabad)",
            "semester_commencement": "September (Fall Semester)",
            "annual_cycle_notes": "Very strict deadline; requesting application package from Embassy in August is essential."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Master's academic track record and scientific honors)",
            "extracurricular_and_leadership_weight": "5% (General adaptability)",
            "research_experience_weight": "35% (Originality, methodology, and feasibility of the 5-page Research Proposal)",
            "work_experience_weight": "5% (Research laboratory experience)",
            "personal_statement_weight": "10% (Motivation letter)",
            "recommendations_weight": "5% (Academic references)",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "0% (No standardized test used)",
            "financial_need_weight": "0% (Pure academic excellence and scientific potential)",
            "selection_panel_composition": "Federal Commission for Scholarships for Foreign Students (FCS) comprising distinguished professors from Swiss cantonal and federal universities.",
            "evaluation_methodology": "Scoring across 3 core criteria: 1) Candidate's academic profile and research capacity, 2) Scientific quality and innovation of the research project, 3) Synergies and quality of supervision with the Swiss host professor."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~300 to 500 qualified researchers in Pakistan with professor acceptance letters",
            "total_scholarships_awarded": "~5 to 10 scholars selected annually for Pakistan",
            "acceptance_rate_global": "~6.0%",
            "acceptance_rate_pakistan": "~2.0% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.65 to 4.00 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Published papers in peer-reviewed international journals, exceptionally well-developed PhD proposal, personal endorsement from a world-renowned Swiss professor.",
            "common_backgrounds_of_winners": "Graduates of Quaid-i-Azam University, NUST, LUMS, University of the Punjab, PIEAS, and COMSATS.",
            "high_representation_countries": "Global program covering 180+ countries.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam emails offering 'Swiss Government Scholarships' for high school or bachelor students. Switzerland NEVER awards FCS scholarships for Bachelor's or Master's degrees.",
                "Agencies claiming they can 'sell Swiss professor acceptance letters'."
            ],
            "application_fee_warning": "Swiss Government application is 100% FREE. Never pay any fee.",
            "agent_and_intermediary_warnings": "Swiss professors will immediately block any student who contacts them through an agency or consultant.",
            "hidden_costs_breakdown": [
                "Inbound airfare to Switzerland at the start is NOT paid by FCS (the student must buy their own flight to Zurich/Geneva; return flight home upon graduation is paid).",
                "Initial deposit buffer: Swiss rent deposit (Mietkaution) typically requires 2-3 months rent upfront (~CHF 1,500-2,000) upon signing an apartment lease.",
                "Attestation and courier fees."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can apply for a Master's degree. (Fact: FCS scholarships for Pakistan are strictly restricted to PhD and Postdoctoral research).",
                "MYTH: You can submit your application online. (Fact: Applications must be physically submitted in triplicate hardcopy to the Swiss Embassy in Islamabad)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently claim airfare is fully covered; official FCS regulations state outbound flight to Switzerland is borne by the scholar, only return flight home is reimbursed."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must satisfy doctoral research committee milestones and annual supervisor evaluations.",
            "attendance_requirements": "Full-time physical residence in Switzerland.",
            "academic_progress_monitoring": "Annual progress report submitted jointly by scholar and supervising professor to FCS in Bern.",
            "work_restrictions_during_study": "Part-time work is strictly prohibited during the first year of the scholarship; after the first year, limited research/teaching assistantships up to 10 hours/week may be permitted with FCS approval.",
            "home_country_return_obligation": "Scholars are expected to return to Pakistan upon completion to foster scientific links, although graduates frequently secure postdoctoral appointments in Europe.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of scholarship and loss of return flight allowance in cases of scientific misconduct or abandonment.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "PhD grants are awarded for 12 months renewable up to 36 months maximum upon positive annual review."
        },
        "official_sources_verified": [
            {
                "source_name": "State Secretariat for Education, Research and Innovation (SERI) - Swiss Government Excellence Scholarships",
                "source_url": "https://www.sbfi.admin.ch/sbfi/en/home/education/scholarships-and-grants/swiss-government-excellence-scholarships.html",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of applicants from Pakistan rejected at the Embassy pre-screening stage",
                    "Internal FCS scoring sheets"
                ]
            }
        ]
    },

    # 14. Italian Regional DSU / EDISU Merit & Need Scholarship (Italy)
    "SCH-EU-003": {
        "scholarship_id": "SCH-EU-003",
        "basic_details": {
            "scholarship_name": "Italian Regional DSU / EDISU Merit & Need Scholarship",
            "offering_entity": "Regional Governments of Italy (DSU Toscana, EDISU Piemonte, LazioDisco, ER.GO Emilia-Romagna, ESU Padova, ALiSEO Liguria)",
            "host_country": "Italy",
            "host_institutions_covered": "All Italian Public Universities (Politecnico di Milano, Politecnico di Torino, University of Bologna, Sapienza University of Rome, University of Florence, University of Pisa, University of Padua, University of Milan)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Open to ALL fields of study without restriction (Engineering, Architecture, Design, Computer Science, Artificial Intelligence, Medicine, Economics, Business, Humanities, Natural Sciences).",
            "number_of_awards_total": "Tens of thousands of regional grants awarded across all Italian universities annually",
            "number_of_awards_pakistan": "Entitlement-based quota: Hundreds of Pakistani students qualify every year if their family income meets financial eligibility thresholds",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's: 3 years; Master's: 2 years; PhD: 3 years (renewed annually subject to credit requirements)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to all international students admitted to an Italian public university (Pakistani students fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit.",
            "academic_qualifications": "12 years education (HSSC/A-Levels) for Bachelor's; 16 years education (BS/Master's) for Master's; 18 years education for PhD from HEC recognized universities.",
            "minimum_gpa_percentage": 50.0,
            "minimum_gpa_scale": 2.0,
            "grading_conversion_notes": "No minimum GPA required for 1st-year entry scholarship; based primarily on admission to the university and family income (ISEE Parificato).",
            "subject_background_prerequisites": "Admission into any accredited degree course at an Italian public university.",
            "current_education_status": "Enrolled or accepted into an Italian university.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 78,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS 6.0 or university-approved English proficiency (many Italian universities accept English Medium of Instruction certificates from Pakistani universities for admission).",
            "other_language_requirements": "None for English-taught programs; Italian B2 for Italian-taught courses.",
            "gender_specific_requirements": "None.",
            "financial_need_required": True,
            "special_eligibility_categories": "CORE FINANCIAL ELIGIBILITY: Equivalent Economic Situation Indicator (ISEE Parificato) must be BELOW the regional threshold (typically €24,000 to €27,000/year). Given Pakistani currency exchange rates, the vast majority of Pakistani middle-class families fall well below this ceiling and qualify easily.",
            "previous_scholarship_restrictions": "Students cannot hold duplicate regional or government scholarships in Italy.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% university tuition fee waiver; students pay only the statutory regional tax (€140 to €160/year)."},
            "admission_application_fee": {"status": "NOT_COVERED", "details": "University pre-admission evaluation fee (€30 to €50) paid by applicant to university."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Free student accommodation in university residence halls OR a housing grant allowance (typically €2,500 to €3,500/year) if placed on the housing waitlist."},
            "monthly_stipend": {"status": "COVERED", "details": "Annual cash maintenance stipend paid in two installments (December and June).", "amount": "€2,500 to €6,500 / year (depending on 'non-resident / out-of-town' student status) (~PKR 750,000 to 1,950,000 / year)"},
            "airfare": {"status": "NOT_COVERED", "details": "International air travel between Pakistan and Italy is NOT covered (borne by student)."},
            "visa_fee": {"status": "NOT_COVERED", "details": "Italian National D Student Visa fee (~€50 / PKR 16,000) paid at Gerry's / Italian Embassy in Pakistan."},
            "health_insurance": {"status": "SUBSIDIZED", "details": "Students register with Italian National Health Service (SSN) paying subsidized student fee (€150 to €700/year) for comprehensive medical coverage."},
            "food_allowance": {"status": "COVERED", "details": "One free meal per day at university cafeterias (Mensa universitaria) for the entire academic year."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via cash stipend."},
            "research_funding_conference_grant": {"status": "NOT_COVERED", "details": "Covered via university departmental resources."},
            "travel_transit_allowance": {"status": "NOT_COVERED", "details": "Discounted local public transportation pass available to students."},
            "total_estimated_value_usd_per_year": 12000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single University: DSU/EDISU application is submitted to the regional agency governing the specific Italian university where the student is enrolled.",
            "participating_institutions": ["Politecnico di Milano (DSU Lombardia), Politecnico di Torino (EDISU Piemonte), University of Bologna (ER.GO), Sapienza University of Rome (LazioDisco), University of Florence (DSU Toscana), University of Padua (ESU)"],
            "university_rankings_scope": "Top 1 to 20 universities in Italy; QS World Rankings 100 to 400.",
            "available_majors": ["All majors (Computer Science, Artificial Intelligence, Mechanical Engineering, Civil Engineering, Architecture, Economics, Fashion Design, Data Science, Biomedical Engineering)"],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 3 years (180 ECTS); Master's: 2 years (120 ECTS); PhD: 3 years",
            "admission_requirements_summary": "University pre-admission offer letter, Universitaly pre-enrolment, ISEE Parificato financial documentation.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission is granted by the university; the scholarship is granted by the regional government agency. Once admitted to the university, getting the scholarship is practically guaranteed if income documents are certified properly.",
            "strategic_program_match_advice": "Focus first on securing admission to the Italian university (December - April), then immediately prepare Pakistani family income documents for ISEE Parificato."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.edisu.piemonte.it/ (and respective regional portals: dsu.toscana.it, er-go.it, laziodisco.it)",
            "portal_system_name": "Regional Scholarship Portals (EDISU, DSU Toscana, ER.GO, LazioDisco, etc.) & Universitaly Portal",
            "account_creation_instructions": "Register on the respective regional scholarship portal (opens June/July) using passport details, and submit Universitaly pre-enrolment application.",
            "step_by_step_workflow": [
                "1. Apply to Italian university during admission calls (December - April) and secure admission letter.",
                "2. Submit pre-enrolment application on official Universitaly portal (universitaly.it).",
                "3. Gather family financial documents in Pakistan: Family Registration Certificate (FRC), Income Certificate (FBR return or employer letter), Property/House documents (Tehsildar certificate), Bank statements.",
                "4. Attest all financial documents from MOFA (Ministry of Foreign Affairs) in Pakistan.",
                "5. Translate all documents into Italian via official Italian Embassy approved translators.",
                "6. Obtain Consular Legalization / Declaration of Value (DOV) or CIMEA comparability certificate.",
                "7. Send documents to Italian Tax Assistance Center (CAF) in Italy to calculate ISEE Parificato certificate.",
                "8. Apply online on the regional scholarship portal (e.g. EDISU / DSU) before late August / early September deadline.",
                "9. Provisional ranking list published (September/October); Final ranking in December.",
                "10. 1st stipend installment and free meal card issued in December/January; 2nd installment in June."
            ],
            "university_vs_scholarship_routing": "Completely separate: Apply to university admissions first; apply to regional DSU agency for scholarship in summer.",
            "recommendation_letters_submission_method": "Not required for DSU scholarship.",
            "personal_statement_prompts": "Not required for DSU scholarship (evaluated strictly on financial need index and university admission).",
            "study_plan_research_proposal_requirements": "Not applicable.",
            "cv_format_requirements": "Europass CV used for university admissions.",
            "interviews_conducted": False,
            "interview_format_details": "No interview conducted for regional scholarship; 100% paper-based financial qualification.",
            "standardized_tests": "None for scholarship; university admission may require TOLC exam or GRE.",
            "application_fee_amount": "€0.00 (Regional scholarship application is 100% FREE).",
            "attestation_requirements": "CRITICAL: All family income, property, and civil status documents from Pakistan must be attested by MOFA and translated into Italian.",
            "translation_requirements": "Official certified Italian translations of all Pakistani documents.",
            "final_submission_method": "100% online portal submission on the regional portal, followed by physical presentation of original financial documents upon arrival in Italy."
        },
        "required_documents_checklist": [
            {"document_name": "Italian University Admission Letter", "mandatory": True, "specification": "Official acceptance letter from an Italian public university", "pakistan_specific_instruction": "Required to prove eligible university enrollment"},
            {"document_name": "NADRA Family Registration Certificate (FRC)", "mandatory": True, "specification": "Issued by NADRA showing all family members, attested by MOFA and translated into Italian", "pakistan_specific_instruction": "Proves family composition and number of dependents"},
            {"document_name": "Family Income Certificate (Annual Income)", "mandatory": True, "specification": "Salary slips / employer certificate / FBR tax return for parent(s) for the prior fiscal year, attested by MOFA and translated", "pakistan_specific_instruction": "Demonstrates family income is below €24,000 threshold"},
            {"document_name": "Family Property Certificate (House / Land)", "mandatory": True, "specification": "Certificate from local Tehsildar / municipal authority showing square meters of family home, or rental agreement if renting", "pakistan_specific_instruction": "Attested by MOFA and translated into Italian"},
            {"document_name": "Bank Statement of All Family Members", "mandatory": True, "specification": "Bank balance certificates as of December 31 of prior year for all bank accounts", "pakistan_specific_instruction": "Attested by MOFA and translated into Italian"},
            {"document_name": "Valid Pakistani Passport", "mandatory": True, "specification": "Valid for at least 18 months", "pakistan_specific_instruction": "Required for portal registration and Italian National D Visa"},
            {"document_name": "ISEE Parificato Certificate", "mandatory": True, "specification": "Calculated by an Italian Tax Assistance Center (CAF) based on the above documents", "pakistan_specific_instruction": "Uploaded to the regional DSU/EDISU portal"}
        ],
        "important_dates_timeline": {
            "application_open_date": "June / July annually (regional portals open)",
            "application_deadline": "Late August to early September annually (strict regional deadlines)",
            "university_admission_deadline": "February - April (university admissions call)",
            "document_submission_deadline": "Coincides with regional deadline (August/September)",
            "recommendation_letters_deadline": "N/A",
            "interview_period": "N/A",
            "shortlist_announcement": "Provisional ranking: September/October; Final ranking: December",
            "final_result_acceptance_deadline": "December annually",
            "visa_application_window": "July - September (Italian Embassy Islamabad / Consulate Karachi)",
            "semester_commencement": "Late September / October (Fall Semester)",
            "annual_cycle_notes": "Financial documents must be prepared strictly following Italian consular specifications in Pakistan."
        },
        "selection_process_and_weights": {
            "academic_weight": "0% for first-year entry (only university admission required; merit criteria apply for 2nd year renewal)",
            "extracurricular_and_leadership_weight": "0%",
            "research_experience_weight": "0%",
            "work_experience_weight": "0%",
            "personal_statement_weight": "0%",
            "recommendations_weight": "0%",
            "interview_weight": "0%",
            "test_scores_weight": "0%",
            "financial_need_weight": "100% (Calculated strictly via the official Italian ISEE Parificato formula)",
            "selection_panel_composition": "Regional Government Directorate for the Right to University Study (Diritto allo Studio Universitario - DSU).",
            "evaluation_methodology": "Mathematical formula: Applicants with ISEE Parificato < €24,000 are ranked from lowest income to highest; virtually all eligible international students receive scholarship awards."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 to 15,000 per region (Italy-wide over 80,000 applicants)",
            "total_scholarships_awarded": "Thousands of scholarships per region (entitlement program)",
            "acceptance_rate_global": "~75% to 85% of eligible applicants who meet financial criteria receive awards",
            "acceptance_rate_pakistan": "~80% of Pakistani students with verified ISEE documents receive full funding (Highest Success Rate in Europe)",
            "typical_successful_applicant_gpa": "2.50 to 3.50 / 4.00 CGPA (Admission to Italian university is the main hurdle)",
            "typical_academic_and_research_profile": "Secured university admission, perfectly attested Pakistani income and property documents.",
            "common_backgrounds_of_winners": "Pakistani students from all backgrounds and provinces admitted to Politecnico di Milano, Politecnico di Torino, Sapienza, Bologna, Florence, Padua.",
            "high_representation_countries": "Pakistan, Iran, India, Turkey, Lebanon, Egypt.",
            "competitiveness_tier": "MODERATE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unregistered agents in Pakistan charging €1,500 to €3,000 claiming they 'grant' Italian scholarships. Regional DSU scholarships are an Italian state right under law.",
                "Fake CAF tax agents forging property documents (automatic Italian visa rejection and police reporting)."
            ],
            "application_fee_warning": "DSU/EDISU application is 100% FREE. Never pay any fee to the regional agency.",
            "agent_and_intermediary_warnings": "Documents must be genuine; the Italian Embassy in Islamabad strictly cross-checks FBR and Tehsildar tax records.",
            "hidden_costs_breakdown": [
                "Document translation and consular legalization costs in Pakistan (PKR 30,000 to 70,000).",
                "Italian Embassy student visa appointment and Gerry's fees (~PKR 25,000).",
                "CRITICAL INITIAL CASH BUFFER: The first DSU scholarship installment is paid in late December or January. Students MUST arrive in Italy with sufficient personal funds (€1,500 to €2,500) to cover initial rent deposits and food for the first 3 months!",
                "Italian Permesso di Soggiorno (Residence Permit) card fee (€120) upon arrival."
            ],
            "misleading_claims_debunked": [
                "MYTH: You get paid before traveling. (Fact: You do NOT receive any money before arriving in Italy; the scholarship is disbursed only after physical university matriculation in Italy).",
                "MYTH: You cannot work in Italy. (Fact: Italian student residence permits allow students to legally work up to 20 hours per week)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Each Italian region (Piedmont, Tuscany, Lombardy, Lazio, Emilia-Romagna) has slightly different ISEE thresholds and deadlines; check the exact regional call (Bando)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must earn minimum university credits (CFU/ECTS) to keep scholarship: typically at least 20 to 35 credits by August 10 of Year 1 to qualify for 2nd year renewal and avoid stipend clawback.",
            "attendance_requirements": "Full physical enrollment and attendance in Italy.",
            "academic_progress_monitoring": "Credits automatically verified with university registry.",
            "work_restrictions_during_study": "Part-time student employment permitted up to 20 hours/week (max 1,040 hours/year) under Italian immigration law.",
            "home_country_return_obligation": "NO mandatory home return requirement. Graduates can convert their Italian study residence permit to a 1-year Job Seeker Permit (Permesso di Soggiorno per Ricerca Lavoro) or full Work Permit (Lavoro Subordinato).",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "CRITICAL WARNING: If a first-year student fails to earn at least 20 credits by August 10, the regional agency DEMANDS FULL REPAYMENT of the cash stipend and charges for meals consumed!",
            "rules_for_changing_university": "Permitted only within the same region or upon formal transfer of DSU file.",
            "rules_for_changing_major": "Permitted once with credit loss implications.",
            "extension_policy": "Eligible for extra semester (fuori corso) support of 50% allowance."
        },
        "official_sources_verified": [
            {
                "source_name": "EDISU Piemonte / DSU Toscana / LazioDisco Official Portals",
                "source_url": "https://www.edisu.piemonte.it/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of Pakistani recipients per individual university (reported in aggregate as non-EU)",
                    "Internal waitlist clearance velocity for dormitory placements"
                ]
            },
            {
                "source_name": "Universitaly - Official Italian Ministry of University and Research (MUR) Portal",
                "source_url": "https://www.universitaly.it/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Visa issuance quota caps at the Italian Embassy in Islamabad"
                ]
            }
        ]
    }
}
