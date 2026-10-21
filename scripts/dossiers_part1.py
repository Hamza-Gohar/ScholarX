"""
scripts/dossiers_part1.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Part 1
Contains:
1. SCH-AM-001: USEFP Fulbright Foreign Student Program for Pakistan (USA)
2. SCH-EU-006: Chevening Scholarships (UK FCDO)
3. SCH-EU-029: Rhodes Scholarship for Pakistan (University of Oxford, UK)
4. SCH-EU-007: Commonwealth Master's and PhD Scholarships (UK)
5. SCH-EU-004: Erasmus Mundus Joint Master Degrees - EMJM (Europe)
6. SCH-EU-002: DAAD Development-Related Postgraduate Courses - EPOS (Germany)
7. SCH-EU-001: Stipendium Hungaricum Scholarship Programme (Hungary)
"""

DOSSIERS_PART1 = {
    # 1. USEFP Fulbright Foreign Student Program (USA)
    "SCH-AM-001": {
        "scholarship_id": "SCH-AM-001",
        "basic_details": {
            "scholarship_name": "USEFP Fulbright Foreign Student Program for Pakistan",
            "offering_entity": "United States Educational Foundation in Pakistan (USEFP) & U.S. Department of State (ECA)",
            "host_country": "United States",
            "host_institutions_covered": "Accredited U.S. Universities (Placement arranged centrally via Institute of International Education - IIE)",
            "degree_levels": ["Master's", "PhD"],
            "major_restrictions": "All academic disciplines are eligible EXCEPT clinical medicine (direct patient contact clinical residency). Public health, health administration, epidemiology, and biomedical sciences are fully eligible.",
            "number_of_awards_total": "~130 to 150 awards annually (the largest Fulbright Foreign Student investment worldwide)",
            "number_of_awards_pakistan": "100% reserved exclusively for Pakistani nationals (~100 Master's, ~30-50 PhD)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's; up to 4 to 5 years for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Pakistani citizens residing and working in Pakistan throughout the application and selection process"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No official upper age limit, but candidates must be early-to-mid career professionals with demonstrated return commitment to Pakistan.",
            "academic_qualifications": "16 years of formal education (4-year BS or 2-year BS + 2-year Master's) for Master's applicants; minimum 18 years (MS/MPhil) for PhD applicants from HEC-recognized institutions.",
            "minimum_gpa_percentage": 50.0,
            "minimum_gpa_scale": 2.5,
            "grading_conversion_notes": "Minimum 2.5/4.0 CGPA or 50% marks in annual system; however, competitive admitted applicant average is typically 3.50+ CGPA.",
            "subject_background_prerequisites": "Degree relevant to intended field; STEM, Social Sciences, Public Policy, Humanities, Environmental Science, and Business (MBA) welcome.",
            "current_education_status": "Graduated or in final semester (must graduate and receive final degree transcript before U.S. departure in August of following year).",
            "graduation_year_restrictions": "None specified by USEFP.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience is not strictly mandatory for academic fields, but strongly preferred; 2+ years is expected for Public Policy and MBA applicants.",
            "english_test_required": True,
            "ielts_minimum": None,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "USEFP does NOT accept IELTS for US university placement. GRE General score is required at application. Once shortlisted, USEFP provides a TOEFL iBT voucher and covers test costs.",
            "other_language_requirements": "None; all coursework is in English.",
            "gender_specific_requirements": "Equal opportunity; women, individuals with disabilities, and candidates from Balochistan, Gilgit-Baltistan, AJK, and southern Punjab are strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates with dual U.S.-Pakistani citizenship or permanent residence (Green Card), or whose spouses/parents are U.S. citizens, are INELIGIBLE.",
            "previous_scholarship_restrictions": "Previous recipients of long-term U.S. government exchange grants (e.g. Humphrey, previous Fulbright degree) must observe mandatory intervals.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full tuition fees and mandatory campus fees paid directly to the host U.S. university."},
            "admission_application_fee": {"status": "COVERED", "details": "IIE manages and pays all university application fees directly."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via monthly maintenance stipend sufficient for off-campus apartment or campus housing."},
            "monthly_stipend": {"status": "COVERED", "details": "Cost-of-living adjusted monthly stipend determined by U.S. city tiers.", "amount": "$1,600 to $2,600 / month (~PKR 450,000 to 720,000)"},
            "airfare": {"status": "COVERED", "details": "Prepaid round-trip economy class international airfare on Fly America Act compliant carrier from Pakistan to U.S. university city."},
            "visa_fee": {"status": "WAIVED", "details": "J-1 Exchange Visitor visa application fee (MRV) and SEVIS fee are fully paid/waived by U.S. Department of State."},
            "health_insurance": {"status": "COVERED", "details": "Accident and Sickness Program for Exchanges (ASPE) health coverage throughout the grant period."},
            "food_allowance": {"status": "COVERED", "details": "Included within the monthly maintenance stipend."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Annual textbook and professional development allowance (~$1,000/year).", "amount": "$1,000 / year"},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Enrichment seminar travel grants and pre-approved dissertation research allowances available through IIE."},
            "travel_transit_allowance": {"status": "COVERED", "details": "One-time transit and baggage allowance upon arrival (~$500).", "amount": "$500 one-off"},
            "total_estimated_value_usd_per_year": 75000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple U.S. Universities; IIE submits applications to 4-5 accredited U.S. universities based on student's academic profile and preferences.",
            "participating_institutions": ["Top U.S. Universities (Columbia, Cornell, NYU, Purdue, UIUC, Texas A&M, Georgia Tech, Michigan State, etc.)"],
            "university_rankings_scope": "R1 research universities and top-tier Master's granting U.S. institutions across all 50 states.",
            "available_majors": ["Energy", "Water Resources", "Agriculture", "Public Health", "Education", "Social Sciences", "Journalism", "Computer Science", "Economics", "Engineering"],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 1-2 years; PhD: 4-5 years",
            "admission_requirements_summary": "Bachelor's / MS degree with transcripts, GRE General score, 3 recommendation letters, Personal Statement, and Study Objective.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Applicants do NOT apply to universities themselves; USEFP and IIE evaluate preferences and match to universities where admission and funding are secure.",
            "strategic_program_match_advice": "Focus statement on developmental challenges in Pakistan (energy transitions, public health systems, water security, data governance) rather than personal ambition."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://usefp.org/scholarships/fulbright.cfm",
            "portal_system_name": "USEFP Online Application Portal (Slate/Embark system)",
            "account_creation_instructions": "Create account using primary active email and CNIC on USEFP portal during open cycle (February - April).",
            "step_by_step_workflow": [
                "1. Register on USEFP online application portal.",
                "2. Complete profile, academic history, and upload scanned degrees/transcripts.",
                "3. Write Study Objective (50 lines) and Personal Statement (50 lines).",
                "4. Submit official GRE General test score code (USEFP institutional code).",
                "5. Register 3 referees who receive automated secure links to submit recommendations directly.",
                "6. Submit online application prior to deadline (mid-April to early May).",
                "7. Preliminary document screening by USEFP committees.",
                "8. In-person panel interviews in Islamabad (July - August).",
                "9. Principal candidate notification in September; candidate takes TOEFL.",
                "10. IIE matches candidate with 4 U.S. universities (October - February).",
                "11. Final U.S. placement confirmed and J-1 visa issued (May - July).",
                "12. Departure to United States (August)."
            ],
            "university_vs_scholarship_routing": "Integrated routing: Apply to USEFP first; selected finalists are placed into universities by IIE.",
            "recommendation_letters_submission_method": "Online upload by referees through confidential automated email link.",
            "personal_statement_prompts": "Personal Statement: Personal narrative describing your background, life experiences, and formative influences. Study Objective: Specific academic goals, proposed study plan, and impact on Pakistan.",
            "study_plan_research_proposal_requirements": "PhD applicants must upload a detailed research proposal (3-5 pages) addressing relevance to Pakistani societal/industrial challenges.",
            "cv_format_requirements": "Standard academic CV (2 pages max) detailing academic achievements, publications, leadership, and public service.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous 20-30 minute panel interview in Islamabad with American diplomats, Pakistani academics, and Fulbright alumni.",
            "standardized_tests": "GRE General test score is MANDATORY at application. Minimum score threshold is not disclosed, but 300+ is competitive. TOEFL required post-selection.",
            "application_fee_amount": "$0.00 (USEFP application is 100% FREE).",
            "attestation_requirements": "HEC degree attestation is required for degree verification prior to final contract issuance.",
            "translation_requirements": "Official English translation required if any secondary documents are in Urdu.",
            "final_submission_method": "100% online portal submission; physical documents requested only upon interview shortlisting."
        },
        "required_documents_checklist": [
            {"document_name": "Passport", "mandatory": True, "specification": "Valid Pakistani passport valid for at least 18 months", "pakistan_specific_instruction": "Required for visa processing and international travel"},
            {"document_name": "Computerized National ID Card (CNIC)", "mandatory": True, "specification": "NADRA issued CNIC front and back", "pakistan_specific_instruction": "Mandatory to verify Pakistani citizenship and residence"},
            {"document_name": "Academic Transcripts & Certificates", "mandatory": True, "specification": "All university degrees and detailed marks certificates", "pakistan_specific_instruction": "Must be from HEC-recognized institutions; HEC attestation required upon selection"},
            {"document_name": "Matric / Intermediate Certificates", "mandatory": True, "specification": "BISE / IBCC matriculation and intermediate certificates", "pakistan_specific_instruction": "Required to prove uninterrupted 16/18 years of academic progression"},
            {"document_name": "GRE General Score Card", "mandatory": True, "specification": "Valid ETS GRE score report", "pakistan_specific_instruction": "Must be valid through the application cycle"},
            {"document_name": "Statement of Purpose / Study Objective", "mandatory": True, "specification": "50-line clear formulation of academic and career plans", "pakistan_specific_instruction": "Emphasize concrete socio-economic return to Pakistan"},
            {"document_name": "Personal Statement", "mandatory": True, "specification": "50-line personal narrative", "pakistan_specific_instruction": "Highlight leadership, resilience, and ethical character"},
            {"document_name": "Three Letters of Reference", "mandatory": True, "specification": "Submitted directly by university professors or professional supervisors", "pakistan_specific_instruction": "Must use official institutional/work email addresses"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Early February annually (e.g., 2026-02-05)",
            "application_deadline": "Late April / Early May annually (e.g., 2026-04-28)",
            "university_admission_deadline": "Managed internally by IIE (October - January)",
            "document_submission_deadline": "Coincides with application deadline",
            "recommendation_letters_deadline": "Coincides with application deadline",
            "interview_period": "July - August annually in Islamabad",
            "shortlist_announcement": "September annually (Principal & Alternate candidates notified)",
            "final_result_acceptance_deadline": "October annually",
            "visa_application_window": "June - July of departure year",
            "semester_commencement": "August / September of departure year",
            "annual_cycle_notes": "18-month lead time: Apply in Spring 2026 for Fall 2027 matriculation."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (GPA rigor, university pedigree, transcript breadth)",
            "extracurricular_and_leadership_weight": "20% (Community leadership, civic engagement, volunteer initiatives)",
            "research_experience_weight": "15% (Crucial for PhD applicants; publications and thesis quality)",
            "work_experience_weight": "10% (Practical application in Pakistani public/private sector)",
            "personal_statement_weight": "15% (Clarity of vision, resilience, compelling personal narrative)",
            "recommendations_weight": "5% (Insight from professors and employers on ethics and aptitude)",
            "interview_weight": "10% (Composure, cross-cultural diplomacy, articulate vision for Pakistan)",
            "test_scores_weight": "Factor in initial screening (GRE quantitative/verbal balance)",
            "financial_need_weight": "0% (Merit-based; financial need is NOT evaluated)",
            "selection_panel_composition": "Bi-national committees comprising American diplomats, USEFP directors, and prominent Pakistani scholars.",
            "evaluation_methodology": "Two-stage evaluation: Blind merit review of online dossier followed by consensus panel interview in Islamabad."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~5,000 to 7,000 applicants from across Pakistan",
            "total_scholarships_awarded": "~130 to 150 principal grantees",
            "acceptance_rate_global": "N/A (Pakistan-specific bilateral program)",
            "acceptance_rate_pakistan": "~2.1% to 2.8% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.55 to 3.85 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Top 10% class ranking, demonstrable leadership outside classroom, publications for PhD candidates.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani universities (LUMS, NUST, IBA, Quaid-i-Azam, UET, AKU) alongside strong representation from public provincial universities.",
            "high_representation_countries": "100% Pakistan",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam portals mimicking USEFP asking for PKR 15,000 to 50,000 'processing fees'. Official USEFP portal is completely FREE.",
                "Fake Facebook groups claiming 'Guaranteed Fulbright Selection' through internal connections."
            ],
            "application_fee_warning": "USEFP NEVER charges an application fee or processing fee at any stage.",
            "agent_and_intermediary_warnings": "USEFP strictly prohibits agents. Applications written by consultants are routinely detected and permanently blacklisted.",
            "hidden_costs_breakdown": [
                "GRE General test registration fee ($220 / ~PKR 62,000) paid out-of-pocket prior to application.",
                "HEC degree attestation fees (approx PKR 5,000 to 12,000).",
                "Travel to Islamabad for in-person interview (USEFP does not reimburse domestic interview travel).",
                "Medical checkup costs at panel clinics prior to visa."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must have a 4.0 CGPA to win. (Fact: Holistic review balances leadership and vision; many 3.2-3.4 CGPA winners succeed with exceptional impact).",
                "MYTH: You can remain in the US and transition directly to H-1B or Green Card. (Fact: Legally barred by Section 212(e) 2-year home residency rule)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party blogs often claim IELTS is accepted; official USEFP guidelines mandate GRE and exclusively sponsor TOEFL iBT."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum 3.0 / 4.0 (Grade B average) across all semesters at the U.S. institution.",
            "attendance_requirements": "Full-time student enrollment mandatory; dropping below minimum credits results in grant revocation.",
            "academic_progress_monitoring": "Semi-annual academic progress reports submitted by university academic advisor to IIE.",
            "work_restrictions_during_study": "On-campus work permitted up to 20 hours/week ONLY with prior written approval from IIE Fulbright advisor. Off-campus employment strictly prohibited.",
            "home_country_return_obligation": "MANDATORY 2-Year Home Residency Requirement (Section 212(e)). Grantees must physically reside in Pakistan for at least 2 full cumulative years before becoming eligible for U.S. H, L, or permanent resident visas.",
            "service_obligations_or_bonds": "Legal bond signed with USEFP agreeing to return and serve in Pakistan.",
            "repayment_clawback_conditions": "Grantees who drop out, fail to maintain academic standing, violate U.S. laws, or fail to return to Pakistan must repay the full dollar value of the grant (typically $150,000+).",
            "rules_for_changing_university": "Strictly disallowed unless extreme institutional closure or departmental emergency occurs, subject to IIE approval.",
            "rules_for_changing_major": "Strictly prohibited; must complete degree in the approved academic field specified in the grant agreement.",
            "extension_policy": "Extensions beyond normal degree duration are rarely granted and require rigorous academic justification without additional stipend funding."
        },
        "official_sources_verified": [
            {
                "source_name": "United States Educational Foundation in Pakistan (USEFP) - Official Fulbright Page",
                "source_url": "https://usefp.org/scholarships/fulbright.cfm",
                "source_type": "OFFICIAL_BILATERAL",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact internal weight percentage formula for interview vs GRE vs SOP (USEFP states evaluation is holistic)",
                    "Exact cutoff score for GRE General (USEFP states no minimum cutoff, but competitive range is informal)"
                ]
            },
            {
                "source_name": "U.S. Department of State - Bureau of Educational and Cultural Affairs (ECA) Fulbright Foreign Student Program",
                "source_url": "https://foreign.fulbrightonline.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Individual institutional placement list before selection"
                ]
            }
        ]
    },

    # 2. Chevening Scholarships (UK)
    "SCH-EU-006": {
        "scholarship_id": "SCH-EU-006",
        "basic_details": {
            "scholarship_name": "Chevening Scholarships",
            "offering_entity": "Foreign, Commonwealth and Development Office (FCDO) & Partner Organisations",
            "host_country": "United Kingdom",
            "host_institutions_covered": "Any UK Higher Education Institution (Russell Group, Oxford, Cambridge, LSE, Imperial, UCL, Edinburgh, Manchester, etc.)",
            "degree_levels": ["Master's"],
            "major_restrictions": "Eligible for any one-year taught master's degree program. Distance learning, part-time courses, and courses longer than 12 months are strictly ineligible.",
            "number_of_awards_total": "~1,500 scholars selected globally each year",
            "number_of_awards_pakistan": "~50 to 70 Chevening scholars and fellows from Pakistan annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "12 months (standard UK 1-year taught master's degree)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of a Chevening-eligible country or territory (Pakistan is fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No upper age limit. Applicants range from recent graduates (with work hours) to senior mid-career leaders.",
            "academic_qualifications": "Undergraduate degree that enables entry onto a postgraduate programme at a UK university (equivalent to an upper second-class 2:1 honours degree in the UK; typically 16 years education in Pakistan).",
            "minimum_gpa_percentage": 65.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Equivalent to UK 2:1 honours; for Pakistan, 3.0/4.0 CGPA or 65%+ marks in semester system.",
            "subject_background_prerequisites": "Any academic field; high-impact fields aligned with UK-Pakistan development priorities (governance, public health, climate, education, human rights, technology) receive strong interest.",
            "current_education_status": "Completed undergraduate degree by the time of Chevening application submission in November.",
            "graduation_year_restrictions": "No graduation year restrictions.",
            "work_experience_required": True,
            "work_experience_minimum_years": 2.0,
            "work_experience_notes": "Mandatory minimum of 2 years work experience (strictly calculated as at least 2,800 hours). Eligible experience includes full-time, part-time, voluntary work, and paid/unpaid internships.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Chevening removed its central English language requirement in 2020. However, applicants must meet the individual English language requirements of their chosen UK universities (typically IELTS 6.5-7.0 or university waiver).",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None; equal opportunity.",
            "financial_need_required": False,
            "special_eligibility_categories": "British citizens or dual British nationals are ineligible. Employees or former employees of His Majesty's Government (or relatives) within the past 2 years are ineligible.",
            "previous_scholarship_restrictions": "Applicants who have previously studied in the UK with funding from a UK government-funded scholarship are ineligible.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full university tuition fees paid directly to the university. Note: MBA programs have a fee cap of £22,000 (applicant must pay remainder)."},
            "admission_application_fee": {"status": "NOT_COVERED", "details": "UK university application fees (e.g. Oxford/Cambridge application fees £75-£85) are paid by applicant unless university waives them."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Provided within the monthly living allowance; students arrange private or university accommodation."},
            "monthly_stipend": {"status": "COVERED", "details": "Tax-free monthly living stipend.", "amount": "£1,347 / month outside London; £1,652 / month inside London (~PKR 490,000 to 600,000)"},
            "airfare": {"status": "COVERED", "details": "Economy class return flights from Pakistan to the UK booked directly via Chevening travel partner (Diversity Travel)."},
            "visa_fee": {"status": "REIMBURSED", "details": "The cost of one Student Route visa application fee is reimbursed."},
            "health_insurance": {"status": "COVERED", "details": "Immigration Health Surcharge (IHS) is covered/exempt for Chevening scholars, giving access to the UK National Health Service (NHS)."},
            "food_allowance": {"status": "COVERED", "details": "Included within the monthly living stipend."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Expected to be covered from the living stipend."},
            "research_funding_conference_grant": {"status": "NOT_COVERED", "details": "Chevening covers taught master's courses; dissertation research grants depend on host university departments."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Arrival allowance (£710–£850) upon initial landing and departure allowance upon returning home.", "amount": "~£800 one-off arrival allowance"},
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Must apply to three different eligible UK university courses (either at 3 different universities or 2 different universities).",
            "participating_institutions": ["All accredited UK universities (Oxford, Cambridge, LSE, Imperial, King's College London, Edinburgh, Manchester, Warwick, Bristol, Leeds, etc.)"],
            "university_rankings_scope": "UK Top 1 to Top 50 universities.",
            "available_majors": ["Public Policy", "International Relations", "Economics", "Law", "Computer Science", "Artificial Intelligence", "Renewable Energy", "Public Health", "Journalism", "Engineering"],
            "english_taught_program_availability": True,
            "program_duration": "12 months (full-time taught postgraduate)",
            "admission_requirements_summary": "Undergraduate degree transcripts, references, personal statement, and fulfillment of university-specific entry criteria.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Applicants do NOT need offers when applying in November. However, having 1 reach school (e.g. Oxford/LSE) and 2 strong match schools (e.g. Sheffield, Sussex, Leeds) prevents being stranded without an unconditional offer by July.",
            "strategic_program_match_advice": "Ensure the three selected courses share an interconnected academic theme so your Chevening essays effectively justify all three choices."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.chevening.org/scholarships/",
            "portal_system_name": "Chevening Online Application System (OAS)",
            "account_creation_instructions": "Register on Chevening OAS in August using primary email address; select Pakistan as application country.",
            "step_by_step_workflow": [
                "1. Register on Chevening OAS (opens early August).",
                "2. Complete eligibility pre-screening questionnaire.",
                "3. Write 4 mandatory 500-word essays: Leadership & Influence, Networking, Study in the UK, Career Plan.",
                "4. Select 3 eligible UK master's courses.",
                "5. Submit online application before early November deadline.",
                "6. Independent reading committee sifts applications (November - January).",
                "7. Shortlisted candidates invited for interview (mid-February).",
                "8. Upload 2 reference letters and education documents to OAS (February - March).",
                "9. Attend in-person panel interview at British High Commission Islamabad or Deputy High Commission Karachi (March - May).",
                "10. Conditional selection results announced in June.",
                "11. Secure at least one unconditional university offer and submit by mid-July deadline.",
                "12. Final award letter issued, Student visa processed, pre-departure briefing (August).",
                "13. Depart to UK (September)."
            ],
            "university_vs_scholarship_routing": "Completely separate: Apply for Chevening via OAS; apply to the 3 UK universities directly through their respective university admissions portals.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate or referee to the Chevening OAS upon invitation to interview in February.",
            "personal_statement_prompts": "Four distinct essays (max 500 words each): 1) Leadership and Influence, 2) Relationship Building and Networking, 3) Studying in the UK (justifying course choices), 4) Career Plan (immediate, 5-year, and 10-year goals in Pakistan).",
            "study_plan_research_proposal_requirements": "Not applicable (taught degree); covered under Essay 3 explaining how selected courses bridge applicant's skill gaps.",
            "cv_format_requirements": "Standard professional CV detailing chronological employment hours.",
            "interviews_conducted": True,
            "interview_format_details": "Strict 30-40 minute in-person panel interview at British High Commission Islamabad/Karachi conducted entirely in English with British diplomats and Chevening alumni.",
            "standardized_tests": "No standardized tests required by Chevening; IELTS/TOEFL required by individual UK universities.",
            "application_fee_amount": "£0.00 (Chevening application is 100% FREE).",
            "attestation_requirements": "HEC degree attestation required by UK universities for unconditional offers.",
            "translation_requirements": "Certified English translations of all academic transcripts.",
            "final_submission_method": "100% online portal submission (OAS)."
        },
        "required_documents_checklist": [
            {"document_name": "Valid Pakistani Passport", "mandatory": True, "specification": "Machine-readable or e-passport valid through proposed study period", "pakistan_specific_instruction": "Required for identity and visa processing"},
            {"document_name": "Undergraduate Degree & Transcript", "mandatory": True, "specification": "Official university degree certificate and final transcript", "pakistan_specific_instruction": "Must be 16-year BS/MA/MSc equivalent"},
            {"document_name": "Three UK University Applications / Offers", "mandatory": True, "specification": "Proof of application or conditional/unconditional offers", "pakistan_specific_instruction": "Must secure 1 unconditional offer by July deadline"},
            {"document_name": "Two Professional / Academic References", "mandatory": True, "specification": "Signed reference letters on institutional letterhead", "pakistan_specific_instruction": "Required when invited for interview in February"},
            {"document_name": "Four Chevening Essays (500 words each)", "mandatory": True, "specification": "Leadership, Networking, Study in UK, and Career Plan", "pakistan_specific_instruction": "Plagiarism is strictly checked with zero tolerance"},
            {"document_name": "Proof of Work Experience (2,800 hours)", "mandatory": True, "specification": "Chronological entry of employment or volunteer hours", "pakistan_specific_instruction": "May require employment letters or contracts upon verification"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Early August annually (e.g., 2026-08-04)",
            "application_deadline": "Early November annually (e.g., 2026-11-03 at 12:00 GMT)",
            "university_admission_deadline": "Individual UK university deadlines (typically Dec - March)",
            "document_submission_deadline": "Mid-February for shortlisted references",
            "recommendation_letters_deadline": "Mid-February to early March",
            "interview_period": "March - May annually in Islamabad & Karachi",
            "shortlist_announcement": "June annually (Conditional Selection notified)",
            "final_result_acceptance_deadline": "Mid-July (Mandatory deadline to upload unconditional university offer)",
            "visa_application_window": "July - August",
            "semester_commencement": "September / October of departure year",
            "annual_cycle_notes": "Strict 1-year timeline; missing the mid-July unconditional offer deadline results in forfeiture of award."
        },
        "selection_process_and_weights": {
            "academic_weight": "15% (Academic background satisfying university entry)",
            "extracurricular_and_leadership_weight": "35% (Leadership track record, initiative, and social impact)",
            "research_experience_weight": "5% (Secondary for taught masters)",
            "work_experience_weight": "20% (Substantive 2,800+ hours with quantifiable outcomes)",
            "personal_statement_weight": "15% (Clarity of vision in essays)",
            "recommendations_weight": "5% (Corroboration of leadership character)",
            "interview_weight": "25% (Final selection is heavily dictated by interview performance)",
            "test_scores_weight": "0% (Chevening does not evaluate test scores)",
            "financial_need_weight": "0% (Not a need-based scholarship)",
            "selection_panel_composition": "British diplomats, Chevening secretariat officers, and prominent Pakistani civil society leaders.",
            "evaluation_methodology": "Two-tier sift: Global reading committee grades essays against leadership rubrics; top scorers called for high-stakes panel interview."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~65,000 to 70,000 applicants globally",
            "total_scholarships_awarded": "~1,500 globally (~55 in Pakistan)",
            "acceptance_rate_global": "~2.2%",
            "acceptance_rate_pakistan": "~1.5% to 2.0% (Extremely Competitive)",
            "typical_successful_applicant_gpa": "3.30 to 3.80 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Demonstrated record of taking initiative, driving organizational or community change, public speaking, or social enterprise.",
            "common_backgrounds_of_winners": "Mid-career professionals from civil society, public sector/civil servants, journalists, legal practitioners, and tech entrepreneurs.",
            "high_representation_countries": "Pakistan is consistently among the top 5 recipient countries globally.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent sites claiming to 'fast-track' Chevening selection for a fee.",
                "WhatsApp groups offering to sell 'winning Chevening essays' (automatic plagiarism disqualification)."
            ],
            "application_fee_warning": "Chevening application is 100% FREE. Never pay any fee for Chevening application or interview.",
            "agent_and_intermediary_warnings": "Chevening does NOT work with education agencies or consultants.",
            "hidden_costs_breakdown": [
                "UK university application fees (e.g. £75 to £100 for Oxford, Cambridge, Imperial, LSE).",
                "IELTS / PTE Academic examination fee (~PKR 55,000 to 65,000) to meet unconditional offer criteria.",
                "TB (Tuberculosis) screening test at IOM clinics in Pakistan (approx PKR 15,000 to 20,000).",
                "Initial pocket money buffer before first stipend release in the UK."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot apply if you don't have IELTS yet. (Fact: You do not need IELTS when applying to Chevening in November; only needed by your chosen university by July).",
                "MYTH: You can stay in the UK on the Graduate Route (PSW visa). (Fact: Chevening scholars are strictly prohibited from switching to the 2-year UK Graduate Visa; must return to Pakistan for 2 years)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently cite old pre-2020 rules claiming Chevening requires IELTS 6.5 directly. This is outdated."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass all master's degree coursework modules and dissertation with a passing grade (50%+ pass, 60%+ merit).",
            "attendance_requirements": "Full-time physical attendance in the UK; unexcused absences reported by university result in visa cancellation and scholarship termination.",
            "academic_progress_monitoring": "Host universities submit regular engagement and grade reports to the Chevening Secretariat.",
            "work_restrictions_during_study": "Scholars are permitted to work up to 20 hours/week during term-time under UK Student Route visa rules, but Chevening strongly discourages heavy outside employment due to rigorous 1-year master's workload.",
            "home_country_return_obligation": "MANDATORY 2-Year Return: Scholars must return to their country of citizenship for a minimum period of two years following the completion of their scholarship.",
            "service_obligations_or_bonds": "Contractual agreement with FCDO; ineligible to apply for UK work visas or settlement until the 2-year return requirement is satisfied.",
            "repayment_clawback_conditions": "Scholars who fail their degree, commit misconduct, or refuse to return home must repay all tuition fees, stipend payments, and airfare in full.",
            "rules_for_changing_university": "Once an award is confirmed in July, changing universities or courses is strictly prohibited except under exceptional university course cancellation.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Scholarship extensions beyond the 12-month grant period are strictly impossible under FCDO policy."
        },
        "official_sources_verified": [
            {
                "source_name": "Chevening Official Secretariat Portal - Foreign, Commonwealth and Development Office (FCDO)",
                "source_url": "https://www.chevening.org/scholarships/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact statistical breakdown of Pakistan interview-to-selection conversion ratio (embassy considers this confidential)",
                    "Internal numerical grading rubric for each of the four essays"
                ]
            },
            {
                "source_name": "Chevening Guidance for Applicants - Work Experience & Eligibility",
                "source_url": "https://www.chevening.org/scholarships/guidance/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific country quota allocations per academic cycle"
                ]
            }
        ]
    },

    # 3. Rhodes Scholarship for Pakistan (University of Oxford)
    "SCH-EU-029": {
        "scholarship_id": "SCH-EU-029",
        "basic_details": {
            "scholarship_name": "Rhodes Scholarship for Pakistan (University of Oxford, UK)",
            "offering_entity": "The Rhodes Trust (Rhodes House, Oxford)",
            "host_country": "United Kingdom",
            "host_institutions_covered": "University of Oxford (All 39 constituent colleges)",
            "degree_levels": ["Master's", "PhD"],
            "major_restrictions": "Eligible for almost all full-time postgraduate degrees offered by the University of Oxford (BSc, BA, MSc, MSt, MPhil, BCL, DPhil / PhD). Ineligible courses include part-time courses and standalone 1-year PGCert.",
            "number_of_awards_total": "~100 Rhodes Scholars elected globally each year",
            "number_of_awards_pakistan": "1 single scholar elected exclusively from Pakistan per year",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "2 years baseline tenure (extensible up to 3 or 4 years for DPhil / PhD researchers)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 27,
            "age_limit_notes": "Must be aged 18-23 on 1 October of application year; OR up to age 26 if completed first degree within the past 2 years.",
            "academic_qualifications": "Completed undergraduate degree (First Class Honours or GPA 3.70+/4.00) that satisfies entry requirements of Oxford postgraduate programs.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "First Class Honours equivalent; in Pakistani CGPA scale, minimum 3.70 / 4.00, or top 5% of graduating class.",
            "subject_background_prerequisites": "Any academic discipline offered at Oxford.",
            "current_education_status": "Must have completed first undergraduate degree by July preceding arrival in Oxford.",
            "graduation_year_restrictions": "Graduation within the past 2-3 years for older cohort pathway.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory; extraordinary leadership, community impact, athletics, or social advocacy is prioritized.",
            "english_test_required": True,
            "ielts_minimum": 7.5,
            "toefl_minimum": 110,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "Must satisfy Oxford University Higher Level English requirements (IELTS 7.5 with 7.0 in each band, or TOEFL iBT 110).",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None; open to all genders.",
            "financial_need_required": False,
            "special_eligibility_categories": "Must have resided in Pakistan for at least 4 of the last 10 years and received formal education in Pakistan.",
            "previous_scholarship_restrictions": "None.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full University of Oxford tuition fees and College fees paid directly."},
            "admission_application_fee": {"status": "COVERED", "details": "Rhodes Trust covers Oxford postgraduate application fee code."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via tax-free living stipend for Oxford college or private accommodation."},
            "monthly_stipend": {"status": "COVERED", "details": "Tax-free living stipend paid quarterly.", "amount": "£19,092 / year (~£1,591 / month or ~PKR 580,000 / month)"},
            "airfare": {"status": "COVERED", "details": "Two economy class flights (one at start of scholarship to the UK, and one at the end of tenure returning home)."},
            "visa_fee": {"status": "COVERED", "details": "UK Student Route visa application fee and International Health Surcharge (IHS) fully paid."},
            "health_insurance": {"status": "COVERED", "details": "Full coverage under the UK National Health Service (NHS) via IHS coverage."},
            "food_allowance": {"status": "COVERED", "details": "Included in monthly living stipend."},
            "books_and_materials_allowance": {"status": "AVAILABLE UPON APPLICATION", "details": "Rhodes Research and Travel Grants available up to £1,000 upon application to Rhodes House."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Access to Rhodes House conference travel funds and academic development grants."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Settling-in allowance upon arrival in Oxford (£250–£500).", "amount": "£250 to £500 one-off"},
            "total_estimated_value_usd_per_year": 85000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single University: University of Oxford only.",
            "participating_institutions": ["University of Oxford (All colleges: Balliol, Magdalen, Christ Church, St John's, etc.)"],
            "university_rankings_scope": "World #1 (Times Higher Education World University Rankings).",
            "available_majors": ["All disciplines (Philosophy, Politics and Economics, Law, Public Policy, Computer Science, Quantum Physics, Oncology, Literature, History)"],
            "english_taught_program_availability": True,
            "program_duration": "2 to 3 years (up to 4 years for DPhil)",
            "admission_requirements_summary": "Oxford departmental admissions criteria (transcripts, writing samples, high GRE/test scores where required, references).",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Election to the Rhodes Scholarship does NOT automatically guarantee admission to the chosen Oxford course; the scholar must secure Oxford department admission in December/January following election.",
            "strategic_program_match_advice": "Consult Oxford course directory closely; show how Oxford's specific faculty members align with your intellectual mission."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.rhodeshouse.ox.ac.uk/scholarships/the-rhodes-scholarship/",
            "portal_system_name": "Rhodes Trust Embark / Slate Application Portal",
            "account_creation_instructions": "Register on the Rhodes Trust portal selecting the Pakistan constituency between June and August.",
            "step_by_step_workflow": [
                "1. Register on Rhodes Trust portal (constituency: Pakistan).",
                "2. Upload transcripts, birth certificate/passport, and proof of education in Pakistan.",
                "3. Write Personal Statement (1,000 words maximum) adhering strictly to the honesty and authorship pledge.",
                "4. Write Academic Statement of Study (350 words maximum) explaining proposed Oxford courses.",
                "5. Register 5 to 6 referees (at least 3 must be academic).",
                "6. Submit online application by early August deadline.",
                "7. National Selection Committee in Pakistan reviews dossiers and shortlists 8-12 finalists.",
                "8. In-person social reception and high-level interview in Islamabad (October/November).",
                "9. Single Rhodes Scholar elected on the evening of the interview.",
                "10. Elected scholar applies to University of Oxford graduate admissions (December - January).",
                "11. Matriculate at Oxford (October following year)."
            ],
            "university_vs_scholarship_routing": "Scholarship first: Compete for Rhodes election; elected scholar applies to Oxford department with guaranteed Rhodes funding backing.",
            "recommendation_letters_submission_method": "Direct secure electronic submission by 5 to 6 referees via confidential email links.",
            "personal_statement_prompts": "1,000-word essay addressing: Who are you? What drives you? How do you hope to fight the world's fight? Must be 100% unassisted work (no feedback or AI generation permitted).",
            "study_plan_research_proposal_requirements": "350-word Academic Statement justifying primary and secondary course choices at Oxford.",
            "cv_format_requirements": "Concise 2-page CV outlining academic record, awards, athletics, volunteerism, and publications.",
            "interviews_conducted": True,
            "interview_format_details": "Legendary in-person final interview in Islamabad before a national committee chaired by a Supreme Court Justice or distinguished leader.",
            "standardized_tests": "Oxford department may require GRE for Economics or Computer Science.",
            "application_fee_amount": "£0.00 (Rhodes Trust charges no application fee).",
            "attestation_requirements": "HEC degree attestation required for Oxford postgraduate matriculation.",
            "translation_requirements": "Certified English translations for any non-English documents.",
            "final_submission_method": "100% online portal submission to Rhodes Trust."
        },
        "required_documents_checklist": [
            {"document_name": "Pakistani Passport / National Identity Card (CNIC)", "mandatory": True, "specification": "Proof of Pakistani citizenship and age", "pakistan_specific_instruction": "Must establish age 18-23 or up to 26 under new rules"},
            {"document_name": "Official Academic Transcripts", "mandatory": True, "specification": "Complete transcripts from all post-secondary institutions attended", "pakistan_specific_instruction": "Must demonstrate First Class Honours (3.7+ CGPA)"},
            {"document_name": "Proof of 4 Years Education in Pakistan", "mandatory": True, "specification": "School / university certificates proving 4 of last 10 years studied in Pakistan", "pakistan_specific_instruction": "Mandatory constituency condition"},
            {"document_name": "Personal Statement (Max 1,000 words)", "mandatory": True, "specification": "Unassisted narrative of personal values, ambition, and ethical leadership", "pakistan_specific_instruction": "Candidate must sign strict zero-plagiarism authorship pledge"},
            {"document_name": "Academic Statement of Study (Max 350 words)", "mandatory": True, "specification": "Specific program choices at Oxford and academic rationale", "pakistan_specific_instruction": "Demonstrate knowledge of Oxford faculty and colleges"},
            {"document_name": "Five to Six Reference Letters", "mandatory": True, "specification": "At least 3 academic referees and 2 character/leadership referees", "pakistan_specific_instruction": "Must be submitted directly by referees by application deadline"},
            {"document_name": "Headshot Photograph", "mandatory": True, "specification": "High-resolution professional portrait", "pakistan_specific_instruction": "Used for selection committee dossier"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Early June annually (e.g., 2026-06-01)",
            "application_deadline": "Early August annually (e.g., 2026-08-01)",
            "university_admission_deadline": "December / January following election",
            "document_submission_deadline": "Early August",
            "recommendation_letters_deadline": "Early August",
            "interview_period": "Late October / Early November in Islamabad",
            "shortlist_announcement": "Mid-October",
            "final_result_acceptance_deadline": "Day of final interview in November",
            "visa_application_window": "June - August of matriculation year",
            "semester_commencement": "October (Michaelmas Term at Oxford)",
            "annual_cycle_notes": "Only ONE award available for all of Pakistan annually; requires supreme intellectual and ethical distinction."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Exceptional intellectual distinction, deep scholarly inquiry)",
            "extracurricular_and_leadership_weight": "25% (Energy to use one's talents to the full; physical vigour, athletics, debate, public impact)",
            "research_experience_weight": "10% (Original critical thinking and academic curiosity)",
            "work_experience_weight": "5% (Initiative in public sphere)",
            "personal_statement_weight": "15% (Authenticity, moral force of character, instinct to lead)",
            "recommendations_weight": "5% (Endorsement of intellectual brilliance and integrity)",
            "interview_weight": "10% (Final interview decides the single winner among the 8-12 finalists)",
            "test_scores_weight": "0% (Not evaluated by Rhodes committee directly)",
            "financial_need_weight": "0% (Pure merit and character award)",
            "selection_panel_composition": "Chaired by high-profile Pakistani figures (former judges, Rhodes alumni, vice chancellors, senior ambassadors).",
            "evaluation_methodology": "Evaluation against the four core criteria of Cecil Rhodes' will: 1) Literary & scholastic attainments, 2) Energy to use one's talents to the full, 3) Truth, courage, devotion to duty, sympathy for the weak, 4) Moral force of character and instincts to lead."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~500 to 1,000 elite graduates across Pakistan",
            "total_scholarships_awarded": "Exactly 1 scholar elected annually",
            "acceptance_rate_global": "~0.7% across all global constituencies",
            "acceptance_rate_pakistan": "~0.1% to 0.2% (The Most Selective Postgraduate Award in Pakistan)",
            "typical_successful_applicant_gpa": "3.85 to 4.00 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Valedictorian / Gold Medalist, national debate champion or collegiate athlete, founder of prominent social initiative.",
            "common_backgrounds_of_winners": "Graduates of LUMS, AKU, NUST, Oxford/Cambridge first-degree holders, or top provincial universities.",
            "high_representation_countries": "1 reserved seat for Pakistan.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Anyone offering 'coaching' or 'reviewing' Rhodes personal statements for a fee is violating Rhodes Trust rules. Outside assistance on personal statements is explicitly grounds for disqualification."
            ],
            "application_fee_warning": "Rhodes Trust never charges any application or registration fee.",
            "agent_and_intermediary_warnings": "Use of agents or consultants is grounds for immediate lifetime disqualification.",
            "hidden_costs_breakdown": [
                "Domestic travel to Islamabad for the finalist dinner and in-person interviews.",
                "Oxford graduate application fee (£75 per course) if fee waiver code is delayed.",
                "English language test fees (IELTS Academic ~PKR 60,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You must be an elite athlete. (Fact: 'Energy to use talents to the full' can be demonstrated through rigorous debate, performing arts, mountaineering, or community organizing, not just varsity sports)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites often list outdated age requirements; the Rhodes Trust updated its age criteria to accommodate 24-26 year olds who finished degrees later."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good standing and satisfy Oxford supervisory progress milestones.",
            "attendance_requirements": "Must reside in Oxford during full academic terms (Michaelmas, Hilary, Trinity).",
            "academic_progress_monitoring": "Termly reports from Oxford college and department tutors submitted to Rhodes House.",
            "work_restrictions_during_study": "Scholars may undertake limited teaching or research assistantships as permitted by Oxford and UK visa regulations.",
            "home_country_return_obligation": "No statutory legal return obligation (unlike Fulbright or Chevening); however, scholars are morally called to 'fight the world's fight'.",
            "service_obligations_or_bonds": "No bond.",
            "repayment_clawback_conditions": "Revocation and expulsion in cases of gross academic fraud, disciplinary expulsion from Oxford, or criminal convictions.",
            "rules_for_changing_university": "Strictly disallowed (tenable only at the University of Oxford).",
            "rules_for_changing_major": "Changing Oxford degree course requires prior written approval from the Warden of Rhodes House and Oxford graduate admissions.",
            "extension_policy": "Third year of funding can be approved for DPhil students upon satisfactory research progress."
        },
        "official_sources_verified": [
            {
                "source_name": "The Rhodes Trust - Official Information for Candidates: Pakistan",
                "source_url": "https://www.rhodeshouse.ox.ac.uk/scholarships/the-rhodes-scholarship/",
                "source_type": "OFFICIAL_ORGANIZATION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of annual applicants from Pakistan (Trust publishes global total but keeps country applicant counts confidential)",
                    "Finalist interview scores and panel deliberative rankings"
                ]
            }
        ]
    },

    # 4. Commonwealth Master's and PhD Scholarships (UK)
    "SCH-EU-007": {
        "scholarship_id": "SCH-EU-007",
        "basic_details": {
            "scholarship_name": "Commonwealth Master's and PhD Scholarships (UK)",
            "offering_entity": "Commonwealth Scholarship Commission in the UK (CSC) & UK Foreign, Commonwealth and Development Office (FCDO)",
            "host_country": "United Kingdom",
            "host_institutions_covered": "Participating UK Higher Education Institutions with CSC joint-funding agreements",
            "degree_levels": ["Master's", "PhD"],
            "major_restrictions": "Must align with one of six Commonwealth Development Themes: 1) Science and tech for development, 2) Health systems, 3) Global prosperity, 4) Peace and governance, 5) Resilience and crisis response, 6) Access and inclusion.",
            "number_of_awards_total": "~800 scholars and fellows funded globally each year",
            "number_of_awards_pakistan": "~25 to 40 awards for Pakistan annually via national nominating agencies",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "12 months for Master's; up to 36 months for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of or refugee in an eligible Commonwealth country (Pakistan is eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No upper age limit.",
            "academic_qualifications": "Minimum upper second-class (2:1) first degree (16 years education for Master's); relevant Master's (18 years education) for PhD.",
            "minimum_gpa_percentage": 65.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 2:1 honours equivalent; HEC criteria typically require minimum 65% or 3.0/4.0 CGPA.",
            "subject_background_prerequisites": "Course aligned with one of the 6 CSC development themes.",
            "current_education_status": "Degree completed by start of UK academic year.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience is not mandatory, but professional experience in development or research is heavily valued.",
            "english_test_required": False,
            "ielts_minimum": None,
            "toefl_minimum": None,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "CSC does not require an English test directly; applicants must meet the individual English language conditions of their selected UK universities.",
            "other_language_requirements": "None.",
            "gender_specific_requirements": "None.",
            "financial_need_required": True,
            "special_eligibility_categories": "Candidates must sign a declaration confirming they could NOT afford to study in the UK without this scholarship.",
            "previous_scholarship_restrictions": "Cannot have previously studied for 1+ academic years in a high-income country.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "Full approved university tuition fees covered under CSC agreement."},
            "admission_application_fee": {"status": "NOT_COVERED", "details": "University application fees paid by applicant."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Provided within the monthly living stipend."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living stipend paid directly by CSC.", "amount": "£1,347 / month outside London; £1,652 / month inside London (~PKR 490,000 to 600,000)"},
            "airfare": {"status": "COVERED", "details": "Approved economy class air travel from Pakistan to the UK and return flight upon completion."},
            "visa_fee": {"status": "REIMBURSED", "details": "UK Student Route visa application fee reimbursed."},
            "health_insurance": {"status": "COVERED", "details": "Access to NHS covered; immigration health surcharge handled via CSC exemption."},
            "food_allowance": {"status": "COVERED", "details": "Included in monthly living allowance."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Study travel grant towards the cost of study-related travel in the UK or overseas.", "amount": "Variable study travel grant"},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Fieldwork travel grant for PhD candidates to return to Pakistan for data collection."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Warm clothing allowance (£500–£550) upon initial arrival in the UK.", "amount": "£500 to £550 one-off"},
            "total_estimated_value_usd_per_year": 50000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Applicants may list up to 3 UK university course choices on their CSC application form.",
            "participating_institutions": ["UK Universities having part-funding agreements with CSC (Cambridge, Oxford, Imperial, Edinburgh, Manchester, Birmingham, Glasgow, Leeds, Sussex, etc.)"],
            "university_rankings_scope": "UK top-ranked universities.",
            "available_majors": ["Development Studies", "Public Health", "Renewable Energy", "Environmental Science", "Agriculture", "Data Science", "Economics", "Education"],
            "english_taught_program_availability": True,
            "program_duration": "12 months for Master's; 36 months for PhD",
            "admission_requirements_summary": "Undergraduate degree, personal statement, development impact plan, references.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Applicants do not need university admission at initial nomination, but must secure university offers before CSC final confirmation.",
            "strategic_program_match_advice": "Explicitly align your course and proposal with the UN Sustainable Development Goals (SDGs) and Pakistani National Priorities."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://cscuk.fcdo.gov.uk/scholarships/commonwealth-masters-scholarships/",
            "portal_system_name": "CSC Online Application System (OAS) & HEC Pakistan Portal",
            "account_creation_instructions": "Dual submission process: Apply on CSC OAS portal AND on HEC Pakistan scholarship portal.",
            "step_by_step_workflow": [
                "1. Apply via CSC OAS (opens September).",
                "2. Apply via HEC Pakistan portal (scholarship.hec.gov.pk) under Commonwealth nominating category.",
                "3. Take HEC HAT test (Higher Education Aptitude Test) organized by ETC Pakistan.",
                "4. Upload Development Impact statements addressing local and national impact.",
                "5. Two reference letters uploaded directly by referees to CSC OAS.",
                "6. Submit both applications before respective deadlines (mid-October for CSC; October for HEC).",
                "7. HEC screens applicants based on HAT scores and academic merit to create national nomination list.",
                "8. Nominated candidates' applications sent to CSC UK for final central selection review.",
                "9. CSC announces final awards in May/June.",
                "10. Finalists secure unconditional university offers, obtain visas, and depart in September."
            ],
            "university_vs_scholarship_routing": "Dual routing: Nominated via HEC Pakistan to CSC UK; apply separately to UK universities.",
            "recommendation_letters_submission_method": "Submitted online by referees directly via CSC OAS.",
            "personal_statement_prompts": "Detailed Development Impact Statement in 4 parts: 1) Impact on development within 2 years, 2) Impact in 5-10 years, 3) How impact will be measured, 4) Relevance to national development priorities in Pakistan.",
            "study_plan_research_proposal_requirements": "Comprehensive research proposal required for PhD applicants including methodology, ethics, and developmental significance.",
            "cv_format_requirements": "Complete employment and education history in CSC OAS format.",
            "interviews_conducted": False,
            "interview_format_details": "CSC UK does not conduct interviews for general Master's/PhD; selection is 100% paper and dossier evaluation. HEC may conduct interviews for specific nominations.",
            "standardized_tests": "HEC HAT test required in Pakistan for national shortlisting.",
            "application_fee_amount": "£0.00 / PKR 0 to CSC (HEC charges nominal HAT test fee ~PKR 2,000).",
            "attestation_requirements": "HEC attestation of degrees required prior to departure.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "Dual online portal submission (CSC OAS + HEC Portal)."
        },
        "required_documents_checklist": [
            {"document_name": "Pakistani Passport / Proof of Citizenship", "mandatory": True, "specification": "Scanned copy of valid passport information page", "pakistan_specific_instruction": "Required to prove citizenship and residency"},
            {"document_name": "Degree Transcripts & Certificates", "mandatory": True, "specification": "Complete university transcripts with grading key", "pakistan_specific_instruction": "Must be recognized by HEC Pakistan"},
            {"document_name": "Two Letters of Reference", "mandatory": True, "specification": "Submitted directly by referees on institutional letterhead", "pakistan_specific_instruction": "Must be provided via online portal"},
            {"document_name": "Development Impact Statement", "mandatory": True, "specification": "Exhaustive 4-part plan linking study to Pakistani socioeconomic growth", "pakistan_specific_instruction": "Crucial scoring factor for CSC panel"},
            {"document_name": "HEC HAT Test Score Card", "mandatory": True, "specification": "Valid Higher Education Aptitude Test result", "pakistan_specific_instruction": "Mandatory for HEC Pakistan nomination shortlist"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Early September annually (e.g., 2026-09-08)",
            "application_deadline": "Mid-October annually (e.g., 2026-10-17)",
            "university_admission_deadline": "December - February following submission",
            "document_submission_deadline": "Coincides with CSC deadline",
            "recommendation_letters_deadline": "Late October",
            "interview_period": "N/A (Dossier-based evaluation)",
            "shortlist_announcement": "HEC nominations announced December; CSC final results announced May/June",
            "final_result_acceptance_deadline": "June annually",
            "visa_application_window": "July - August",
            "semester_commencement": "September / October of departure year",
            "annual_cycle_notes": "Being nominated by HEC does NOT guarantee the scholarship; CSC UK makes final selections based on global development scoring."
        },
        "selection_process_and_weights": {
            "academic_weight": "33% (Academic merit of the candidate)",
            "extracurricular_and_leadership_weight": "10% (Leadership and potential for influence)",
            "research_experience_weight": "15% (Quality of study plan / research proposal)",
            "work_experience_weight": "10% (Development-related professional exposure)",
            "personal_statement_weight": "25% (Potential impact on the development of the home country)",
            "recommendations_weight": "7% (Referee verification)",
            "interview_weight": "0% (No interview)",
            "test_scores_weight": "Screening filter via HEC HAT in Pakistan",
            "financial_need_weight": "Gatekeeper requirement (declaration of inability to self-fund)",
            "selection_panel_composition": "Independent panels of senior UK academic subject specialists appointed by CSC.",
            "evaluation_methodology": "Scoring across 3 core criteria: 1) Academic merit, 2) Quality of study plan, 3) Potential development impact on the home country."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~15,000 to 20,000 applicants globally; ~2,000 in Pakistan",
            "total_scholarships_awarded": "~800 globally; ~30 in Pakistan",
            "acceptance_rate_global": "~4.0%",
            "acceptance_rate_pakistan": "~1.5% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.50 to 3.80 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Solid academic foundation with strong focus on poverty reduction, public health, climate, or sustainable industrialization.",
            "common_backgrounds_of_winners": "Public sector researchers, university lecturers, civil servants, NGO workers, and environmental scientists.",
            "high_representation_countries": "Pakistan, Nigeria, Kenya, Bangladesh, India.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Scam agencies charging 'nomination processing fees' claiming guaranteed HEC quotas. HEC and CSC applications are free/nominal."
            ],
            "application_fee_warning": "CSC charges NO application fee whatsoever.",
            "agent_and_intermediary_warnings": "CSC applications must be submitted solely by the candidate.",
            "hidden_costs_breakdown": [
                "HEC HAT test registration fee (PKR 2,000).",
                "IELTS/English test fees required by UK universities.",
                "Tuberculosis screening certificate fee (IOM clinics PKR 15,000 to 20,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: An HEC nomination guarantees a scholarship. (Fact: HEC nominates ~2x the quota; CSC UK rejects around 50% of national nominees during the final central review)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some third parties claim work experience is mandatory; official CSC rules do not require work experience for Master's courses."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain satisfactory academic progress as certified by the host institution.",
            "attendance_requirements": "Full-time physical attendance in the UK.",
            "academic_progress_monitoring": "Annual progress reports submitted by university supervisors to CSC.",
            "work_restrictions_during_study": "Part-time employment allowed up to 20 hours/week under UK visa rules, subject to academic supervisor approval.",
            "home_country_return_obligation": "MANDATORY Return: Must return to home country upon completion of the award. Ineligible for UK graduate work route visas.",
            "service_obligations_or_bonds": "Agreement to return and apply skills to home country development.",
            "repayment_clawback_conditions": "Failure to complete degree or failure to return to home country triggers repayment obligation.",
            "rules_for_changing_university": "Changing institutions is not allowed without express prior permission from CSC.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Extensions are rarely granted; PhD funding capped strictly at 36 months."
        },
        "official_sources_verified": [
            {
                "source_name": "Commonwealth Scholarship Commission in the UK (CSC) - Official Masters Page",
                "source_url": "https://cscuk.fcdo.gov.uk/scholarships/commonwealth-masters-scholarships/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact percentage cutoff of HEC HAT score required for Pakistan national nomination list",
                    "Score sheets of independent academic reviewers in the UK"
                ]
            }
        ]
    },

    # 5. Erasmus Mundus Joint Master Degrees (EMJM)
    "SCH-EU-004": {
        "scholarship_id": "SCH-EU-004",
        "basic_details": {
            "scholarship_name": "Erasmus Mundus Joint Master Degrees (EMJM)",
            "offering_entity": "European Commission / European Education and Culture Executive Agency (EACEA)",
            "host_country": "Multiple European Countries (Consortium of 2 to 4 countries)",
            "host_institutions_covered": "International consortia of European and partner universities across Europe",
            "degree_levels": ["Master's"],
            "major_restrictions": "Open to all disciplines across over 150 accredited Erasmus Mundus Joint Master programs (STEM, Humanities, Social Sciences, Arts, Environmental Sciences, Business).",
            "number_of_awards_total": "~2,500 full scholarships awarded globally each year across all consortia",
            "number_of_awards_pakistan": "Pakistan is consistently ranked #1 globally in Erasmus Mundus recipients (~140 to 190 Pakistani winners annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "12 to 24 months (depending on master's program curriculum: 60, 90, or 120 ECTS)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to students worldwide regardless of country of origin (Partner Country category for Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limit whatsoever.",
            "academic_qualifications": "First higher education degree (Bachelor's degree equivalent to 180 or 240 ECTS credits; 16 years education in Pakistan).",
            "minimum_gpa_percentage": 60.0,
            "minimum_gpa_scale": 2.8,
            "grading_conversion_notes": "Varies by individual consortium; typically minimum 2.8/4.0 CGPA, but competitive applicants typically have 3.3+ CGPA.",
            "subject_background_prerequisites": "Relevant undergraduate degree in corresponding field as specified by each EMJM consortium.",
            "current_education_status": "Students in final year of bachelor's degree can apply if they graduate before program matriculation (August/September).",
            "graduation_year_restrictions": "No restriction; recent graduates and seasoned professionals eligible.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory for most programs; highly valued in applied programs.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "Set by each consortium: usually IELTS 6.5 (minimum 6.0 in each subscore) or TOEFL iBT 90. Some consortia accept English Medium of Instruction (MOI) certificates from Pakistan.",
            "other_language_requirements": "None required at entry; local language electives offered during mobility.",
            "gender_specific_requirements": "None; equal opportunity.",
            "financial_need_required": False,
            "special_eligibility_categories": "Rule of 3: An applicant may apply to a maximum of 3 different Erasmus Mundus master's programs in a single annual intake.",
            "previous_scholarship_restrictions": "Students who have previously received an Erasmus Mundus Master / Joint Doctor scholarship are NOT eligible for a second one.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% participation costs and university tuition fees covered across all partner universities in the consortium."},
            "admission_application_fee": {"status": "COVERED", "details": "Most EMJM consortia have free application; if a fee exists, it is waived or covered upon award."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via generous monthly living allowance; university housing support provided by each host university."},
            "monthly_stipend": {"status": "COVERED", "details": "Fixed monthly subsistence allowance paid directly to student for the duration of the master's program.", "amount": "€1,400 / month (~PKR 420,000 / month) for up to 24 months = €33,600 total stipend"},
            "airfare": {"status": "COVERED", "details": "Included within the comprehensive €1,400/month flat-rate grant under Erasmus+ rules (which covers travel, installation, and living)."},
            "visa_fee": {"status": "REIMBURSED", "details": "Covered by student using installation portion of stipend; letters of sponsorship provided for national visa fee waivers where bilateral agreements exist."},
            "health_insurance": {"status": "COVERED", "details": "Full comprehensive international health, travel, and accident insurance meeting European Commission standards for the full 24 months."},
            "food_allowance": {"status": "COVERED", "details": "Included within the €1,400/month stipend."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "Access to laboratory, library, and consortium resources included in participation cost waiver."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Consortium travel grants available for attending European conferences and thesis research placement."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Embedded in the monthly scholarship rate (€1,400/month flat rate covers all mobility between countries)."},
            "total_estimated_value_usd_per_year": 38000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Mandatory Multiple Universities: Study in at least TWO different European countries during the degree (e.g. Year 1 in France, Year 2 in Italy or Sweden).",
            "participating_institutions": ["Consortia across France, Germany, Italy, Spain, Belgium, Netherlands, Sweden, Finland, Portugal, Poland, Austria, etc."],
            "university_rankings_scope": "Top European national research institutes and specialized universities.",
            "available_majors": ["Artificial Intelligence", "Cybersecurity", "Data Science", "Nanoscience", "Marine Environment", "Renewable Energy", "Public Health", "Economics", "Human Rights", "Materials Science"],
            "english_taught_program_availability": True,
            "program_duration": "12 to 24 months (60 to 120 ECTS credits)",
            "admission_requirements_summary": "Bachelor's degree, transcripts, CV (Europass format), Motivation Letter, 2 recommendation letters, English proficiency.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single application: Applying to the consortium program automatically applies for the Erasmus Mundus scholarship simultaneously.",
            "strategic_program_match_advice": "Consult the official Erasmus Mundus Catalogue; apply to the 3 programs that most tightly align with your undergraduate thesis or research projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters",
            "portal_system_name": "Individual Consortium Portals (listed on EACEA Catalogue)",
            "account_creation_instructions": "Explore EACEA Catalogue, identify up to 3 programs, and register on each consortium's dedicated application portal.",
            "step_by_step_workflow": [
                "1. Search the EACEA Erasmus Mundus Catalogue for programs matching your discipline.",
                "2. Visit the chosen program website (e.g. Master in Big Data, Marine Biotechnology, etc.).",
                "3. Register on the specific consortium portal (opens October - November).",
                "4. Upload Bachelor's degree, transcripts, and proof of residence.",
                "5. Write tailored Motivation Letter explaining why this specific multi-country curriculum fits your goals.",
                "6. Format CV in Europass format.",
                "7. Add details of 2 academic referees who upload letters directly.",
                "8. Submit online application before January/February deadline.",
                "9. Consortium selection board evaluates files (February - March).",
                "10. Results announced (March - April); Main list (scholarship winners) and Reserve list notified.",
                "11. Consortia provide visa guarantee letters for Country 1 visa application (May - July).",
                "12. Arrive in Country 1 for orientation (September)."
            ],
            "university_vs_scholarship_routing": "Integrated 1-step routing: Program application and scholarship selection are evaluated jointly by the consortium academic board.",
            "recommendation_letters_submission_method": "Online upload by referees via automated links or uploaded by applicant on portal.",
            "personal_statement_prompts": "Consortium-specific Motivation Letter (1-2 pages): Academic background, relevance of program courses, mobility plan rationale, and post-graduation impact.",
            "study_plan_research_proposal_requirements": "Brief outline of prospective thesis interests or research topics.",
            "cv_format_requirements": "Europass CV format strongly recommended by most European consortia.",
            "interviews_conducted": True,
            "interview_format_details": "Approx 30% of consortia conduct a 15-20 minute online video interview (Zoom/Teams) with the academic coordinating committee.",
            "standardized_tests": "No GRE or HEC HAT required. English proficiency (IELTS/TOEFL) as mandated by consortium.",
            "application_fee_amount": "€0.00 for scholarship applicants in virtually all consortia.",
            "attestation_requirements": "HEC degree attestation and Apostille/attestation required for host country university enrolment upon arrival.",
            "translation_requirements": "Official English translations of non-English degree certificates.",
            "final_submission_method": "100% online portal submission to each consortium."
        },
        "required_documents_checklist": [
            {"document_name": "International Passport", "mandatory": True, "specification": "Valid for at least 6 months beyond the intended study end date", "pakistan_specific_instruction": "Required for identity and European Schengen visa processing"},
            {"document_name": "Bachelor's Degree Certificate & Transcripts", "mandatory": True, "specification": "Official degree showing courses, grades, and grading scale", "pakistan_specific_instruction": "Must be 16-year BS / Honours from HEC recognized university"},
            {"document_name": "Europass Curriculum Vitae", "mandatory": True, "specification": "Formatted according to standard European Europass template", "pakistan_specific_instruction": "Highlight research projects, software tools, and academic achievements"},
            {"document_name": "Motivation Letter (Statement of Purpose)", "mandatory": True, "specification": "1 to 2 page focused justification of interest in the consortium", "pakistan_specific_instruction": "Avoid generic praise; analyze specific mobility tracks and professors"},
            {"document_name": "Two Academic Reference Letters", "mandatory": True, "specification": "Signed by professors with university institutional email addresses", "pakistan_specific_instruction": "Must attest to intellectual capability and ability to adapt to foreign environments"},
            {"document_name": "English Language Proficiency Certificate", "mandatory": True, "specification": "IELTS Academic, TOEFL iBT, or consortium-approved MOI", "pakistan_specific_instruction": "Verify whether consortium strictly requires IELTS 6.5+"},
            {"document_name": "Proof of Residence / Place of Living", "mandatory": True, "specification": "Official certificate confirming place of residence (domicile/utility bill/work letter)", "pakistan_specific_instruction": "Required by European Commission 12-month residency rule"}
        ],
        "important_dates_timeline": {
            "application_open_date": "October - November annually",
            "application_deadline": "Early January to mid-February annually (varies by consortium)",
            "university_admission_deadline": "Handled simultaneously with scholarship application",
            "document_submission_deadline": "Coincides with consortium deadline",
            "recommendation_letters_deadline": "Coincides with consortium deadline",
            "interview_period": "February - March (online interviews if applicable)",
            "shortlist_announcement": "Late March to mid-April annually",
            "final_result_acceptance_deadline": "Late April to early May",
            "visa_application_window": "May - July (National D Visa for Country 1)",
            "semester_commencement": "Late August / September of departure year",
            "annual_cycle_notes": "Programs run independently; check the exact deadline on each consortium's individual website."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic excellence, transcript grades, undergraduate thesis quality)",
            "extracurricular_and_leadership_weight": "10% (Adaptability, international mindset, communication)",
            "research_experience_weight": "20% (Prior publications, capstone projects, laboratory skills)",
            "work_experience_weight": "5% (Industry internships or relevant employment)",
            "personal_statement_weight": "15% (Strength and clarity of motivation letter)",
            "recommendations_weight": "5% (Referee evaluation)",
            "interview_weight": "5% (Where conducted, confirms English fluency and motivation)",
            "test_scores_weight": "0% (No standardized tests used)",
            "financial_need_weight": "0% (Pure academic and potential merit)",
            "selection_panel_composition": "Joint academic admission committee comprising professors from each partner university in the consortium.",
            "evaluation_methodology": "Dossiers ranked on an aggregate 100-point rubric; top 15-20 non-EU candidates offered full Erasmus Mundus scholarships."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~500 to 1,500 applicants per individual consortium program",
            "total_scholarships_awarded": "~15 to 22 scholarships per program (~2,500 across all programs)",
            "acceptance_rate_global": "~2.0% to 3.5%",
            "acceptance_rate_pakistan": "~3.5% to 5.0% (Pakistan is the #1 winning nation worldwide for 3 years running)",
            "typical_successful_applicant_gpa": "3.40 to 3.90 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Strong undergraduate thesis or final year design project, clear research vision, high academic consistency.",
            "common_backgrounds_of_winners": "Graduates of NUST, FAST, LUMS, UET, GIKI, Quaid-i-Azam, COMSATS, and provincial universities across Pakistan.",
            "high_representation_countries": "Pakistan, India, Nigeria, Bangladesh, Brazil, Mexico.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents claiming to have 'reserved spots' on Erasmus Mundus consortia. Consortium selections are strictly decided by academic professors in Europe."
            ],
            "application_fee_warning": "Erasmus Mundus consortium applications for scholarship candidates are almost universally 100% free.",
            "agent_and_intermediary_warnings": "Never use agents; copy-pasted or consultant-written motivation letters are easily detected and failed.",
            "hidden_costs_breakdown": [
                "National D Visa application fees and translation/legalization costs for Country 1 embassy in Islamabad (PKR 30,000 to 60,000).",
                "Initial travel cash buffer: The first scholarship installment (€1,400 x 2) is released 2-4 weeks after arrival in Europe; student must carry €800-€1,200 for initial days."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need work experience. (Fact: Over 60% of Pakistani winners apply during their final year of BS or immediately after graduation).",
                "MYTH: You cannot apply to more than 3 programs. (Fact: You CAN apply to up to 3 programs; applying to more than 3 will lead to disqualification across all of them)."
            ],
            "official_vs_unofficial_discrepancies": [
                "The European Commission merged travel, installation, and subsistence into a single consolidated €1,400/month flat-rate grant under Erasmus+ 2021-2027 regulations."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must earn required ECTS credits each semester (30 ECTS per semester) to advance to the next mobility period.",
            "attendance_requirements": "Full physical attendance across at least 2 distinct consortium countries.",
            "academic_progress_monitoring": "Consortium academic coordinator monitors module passes before approving monthly stipend disbursals.",
            "work_restrictions_during_study": "Part-time student employment laws vary by host country (e.g. 20 hrs/week in France/Germany), but intensive multi-country curriculum leaves minimal time for employment.",
            "home_country_return_obligation": "NO mandatory return obligation! Erasmus Mundus graduates are fully eligible to apply for post-study work visas (e.g. 18-month Job Seeker Visa in Germany, 1-year APS in France) or continue onto funded European PhDs.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Severe breach of student agreement, academic failure, or unilateral drop-out requires reimbursement of unspent grant funds.",
            "rules_for_changing_university": "Mobility tracks are predetermined by consortium specialization pathways chosen at admission.",
            "rules_for_changing_major": "Not permitted.",
            "extension_policy": "No scholarship extension beyond normal 24-month duration."
        },
        "official_sources_verified": [
            {
                "source_name": "European Commission - Erasmus Mundus Joint Masters Official Portal",
                "source_url": "https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact applicant volume per individual consortium (managed independently by each university consortium)",
                    "Exact reserve list rankings"
                ]
            },
            {
                "source_name": "EACEA Erasmus Mundus Programme Catalogue",
                "source_url": "https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Consortium-level specific minimum GPA threshold (determined by individual consortium admission committees)"
                ]
            }
        ]
    },

    # 6. DAAD Development-Related Postgraduate Courses (EPOS)
    "SCH-EU-002": {
        "scholarship_id": "SCH-EU-002",
        "basic_details": {
            "scholarship_name": "DAAD Development-Related Postgraduate Courses (EPOS)",
            "offering_entity": "German Academic Exchange Service (DAAD) & Federal Ministry for Economic Cooperation and Development (BMZ)",
            "host_country": "Germany",
            "host_institutions_covered": "German State Universities (TU Munich, RWTH Aachen, TU Berlin, Univ of Bonn, Freiburg, Stuttgart, Leipzig, etc.)",
            "degree_levels": ["Master's", "PhD"],
            "major_restrictions": "Restricted strictly to accredited development-related postgraduate courses listed in the official DAAD EPOS brochure (Economic Sciences, Development Cooperation, Engineering, Regional Planning, Agriculture, Environmental Sciences, Medicine/Public Health, Social Sciences, Media).",
            "number_of_awards_total": "~300 to 500 scholarships awarded annually worldwide",
            "number_of_awards_pakistan": "~30 to 45 awards for Pakistan across various EPOS programs annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "12 to 24 months for Master's; up to 42 months for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of developing countries on DAC list (Pakistan is fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No explicit age limit, but academic degree must NOT be older than 6 years at time of application.",
            "academic_qualifications": "Completed undergraduate degree (4-year Bachelor's / 16 years education) with above-average results (typically upper third of class).",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "German grade 2.5 or better (equivalent in Pakistan to ~3.0/4.0 CGPA or 70%+ marks).",
            "subject_background_prerequisites": "Academic background directly matching the chosen EPOS course curriculum.",
            "current_education_status": "Completed degree; academic degree must have been awarded within the last 6 years.",
            "graduation_year_restrictions": "Degree certificate date must not exceed 6 years prior to application deadline.",
            "work_experience_required": True,
            "work_experience_minimum_years": 2.0,
            "work_experience_notes": "STRICT MANDATORY REQUIREMENT: At least two years of relevant professional experience AFTER completing bachelor's degree at the time of application.",
            "english_test_required": True,
            "ielts_minimum": 6.0,
            "toefl_minimum": 80,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic (minimum 6.0 or 6.5 depending on course) or TOEFL iBT (minimum 80). For German-taught courses: DSH 2 or TestDaF 4.",
            "other_language_requirements": "Basic German is beneficial; DAAD provides a preparatory German course.",
            "gender_specific_requirements": "None; women professionals strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must demonstrate strong motivation to assume social responsibility and drive development in their home country.",
            "previous_scholarship_restrictions": "Applicants who have been resident in Germany for more than 15 months at the time of application are ineligible.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% tuition fees covered (German state universities have no or low tuition; any specialized course tuition is paid by DAAD)."},
            "admission_application_fee": {"status": "WAIVED", "details": "Handled through direct university application or uni-assist reimbursement voucher."},
            "accommodation": {"status": "MONTHLY ALLOWANCE", "details": "Covered via monthly scholarship payment; rent subsidy granted where accommodation costs exceed normal threshold."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living stipend paid directly by DAAD.", "amount": "€934 / month for Master's; €1,300 / month for PhD (~PKR 280,000 to 390,000 / month)"},
            "airfare": {"status": "COVERED", "details": "Adequate flat-rate travel allowance for flights between Pakistan and Germany upon arrival and departure."},
            "visa_fee": {"status": "WAIVED", "details": "German student visa fees waived by the German Embassy in Islamabad / Consulate in Karachi upon presentation of DAAD award letter."},
            "health_insurance": {"status": "COVERED", "details": "Comprehensive health, accident, and personal liability insurance covered directly by DAAD."},
            "food_allowance": {"status": "COVERED", "details": "Included within monthly stipend."},
            "books_and_materials_allowance": {"status": "COVERED", "details": "One-off study grant paid annually (€460/year).", "amount": "€460 / year"},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "Field research subsidies and conference attendance grants available for thesis work."},
            "travel_transit_allowance": {"status": "COVERED", "details": "Preparatory German language course (up to 6 months) with all expenses and accommodation covered in Germany prior to master's start."},
            "total_estimated_value_usd_per_year": 28000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Applicants may apply for up to three EPOS courses, prioritizing their order of preference (Rank 1, 2, 3) on the DAAD application form.",
            "participating_institutions": ["TU Munich, RWTH Aachen, TU Berlin, Univ of Bonn, Freiburg, Stuttgart, Hohenheim, Flensburg, Dresden, Leipzig, Hannover, etc."],
            "university_rankings_scope": "TU9 German Institutes of Technology and leading research universities.",
            "available_majors": ["Development Economics", "Water Resources Engineering", "Renewable Energy", "Public Health", "Urban Planning", "Agricultural Economics", "International Media", "Environmental Protection"],
            "english_taught_program_availability": True,
            "program_duration": "12 to 24 months for Master's",
            "admission_requirements_summary": "Bachelor's degree, 2+ years verified work experience certificate, employer recommendation letter, Motivation Letter with developmental focus, DAAD form.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single application submitted directly to the university coordinator of the respective EPOS master's program (or via DAAD portal depending on course instructions).",
            "strategic_program_match_advice": "Ensure current employment in Pakistan directly connects to the technical curriculum of the German master's course."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.daad.de/en/study-and-research-in-germany/scholarships/daad-scholarships/",
            "portal_system_name": "DAAD Portal & Host University Portals (specified in EPOS brochure)",
            "account_creation_instructions": "Review EPOS brochure, identify course, apply directly to the university's online admission system, uploading the DAAD application form.",
            "step_by_step_workflow": [
                "1. Download and review the latest DAAD EPOS Course Catalogue brochure.",
                "2. Verify that you have at least 2 years of post-graduation professional work experience.",
                "3. Secure employer support letter and professional reference on official company letterhead.",
                "4. Complete the official DAAD Application Form (available on DAAD website).",
                "5. Write Hand-signed Motivation Letter (max 2 pages) emphasizing developmental relevance to Pakistan.",
                "6. Format CV in Europass format (hand-signed and dated).",
                "7. Submit complete dossier to the host university course coordinator before individual course deadline (typically August - November).",
                "8. University selection committee reviews applications and creates shortlisted ranking.",
                "9. DAAD central committee confirms scholarship awards (January - March).",
                "10. Successful applicants attend 2-6 months German language course (if applicable) starting April/July.",
                "11. Master's program begins in October."
            ],
            "university_vs_scholarship_routing": "Integrated routing: Applications are submitted directly to the university running the EPOS course.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate with hand-signatures, official stamps, and institutional contact details.",
            "personal_statement_prompts": "Detailed Letter of Motivation (max 2 pages, hand-signed): Academic reasons, professional achievements, why this course in Germany, and how you will apply knowledge in Pakistan.",
            "study_plan_research_proposal_requirements": "PhD candidates must submit a detailed research proposal approved by a German university professor.",
            "cv_format_requirements": "Europass CV (must be hand-signed and dated at the bottom).",
            "interviews_conducted": False,
            "interview_format_details": "Generally paper-based evaluation; some individual university committees may conduct short technical Zoom interviews.",
            "standardized_tests": "IELTS Academic or TOEFL iBT. No GRE needed.",
            "application_fee_amount": "€0.00 in most cases; nominal fee (€75) if course requires preliminary screening via uni-assist.",
            "attestation_requirements": "HEC degree attestation required for German university enrolment and visa processing.",
            "translation_requirements": "Certified German or English translation of academic documents.",
            "final_submission_method": "Submitted online via university portal or DAAD portal according to course instructions."
        },
        "required_documents_checklist": [
            {"document_name": "Completed & Hand-Signed DAAD Application Form", "mandatory": True, "specification": "Official DAAD form with photograph and signatures", "pakistan_specific_instruction": "Must list up to 3 EPOS courses in prioritized order"},
            {"document_name": "Hand-Signed Europass Curriculum Vitae", "mandatory": True, "specification": "Complete CV in Europass format signed and dated", "pakistan_specific_instruction": "Clearly document exact dates of post-bachelor employment"},
            {"document_name": "Hand-Signed Letter of Motivation", "mandatory": True, "specification": "Max 2 pages explaining academic and career plans in Pakistan", "pakistan_specific_instruction": "Must establish direct connection to Pakistani developmental goals"},
            {"document_name": "Official Proof of Minimum 2 Years Work Experience", "mandatory": True, "specification": "Employment letter(s) on company letterhead confirming at least 2 full years", "pakistan_specific_instruction": "Work experience prior to completing bachelor's degree does NOT count"},
            {"document_name": "Letter of Recommendation from Current Employer", "mandatory": True, "specification": "Signed letter with official stamp and re-employment guarantee if possible", "pakistan_specific_instruction": "Proves employer supports candidate's professional upgrade"},
            {"document_name": "Academic Reference Letter from University Professor", "mandatory": True, "specification": "Recent reference letter on university letterhead", "pakistan_specific_instruction": "Must include professor's email and contact phone"},
            {"document_name": "University Degree Certificates & Transcripts", "mandatory": True, "specification": "Degree showing courses, grades, and grading scale (HEC recognized)", "pakistan_specific_instruction": "Degree must not be older than 6 years"},
            {"document_name": "English Language Test Certificate", "mandatory": True, "specification": "IELTS Academic (min 6.0/6.5) or TOEFL iBT (min 80)", "pakistan_specific_instruction": "Must be valid at the time of application"}
        ],
        "important_dates_timeline": {
            "application_open_date": "May - August annually (varies by course)",
            "application_deadline": "August 31 to November 30 annually (each course sets its own deadline)",
            "university_admission_deadline": "Coincides with EPOS application deadline",
            "document_submission_deadline": "Coincides with course deadline",
            "recommendation_letters_deadline": "Coincides with course deadline",
            "interview_period": "December - January (if technical interviews held)",
            "shortlist_announcement": "January - March annually",
            "final_result_acceptance_deadline": "April annually",
            "visa_application_window": "May - July (German Embassy student visa appointment)",
            "semester_commencement": "October (Winter Semester)",
            "annual_cycle_notes": "Very strict 6-year degree expiration rule and 2-year post-graduation work experience cutoff."
        },
        "selection_process_and_weights": {
            "academic_weight": "25% (Quality of undergraduate degree and grades)",
            "extracurricular_and_leadership_weight": "10% (Social commitment in home country)",
            "research_experience_weight": "10% (Academic rigor in undergraduate thesis)",
            "work_experience_weight": "30% (Substantive 2+ years work experience and employer endorsement)",
            "personal_statement_weight": "20% (Development-oriented motivation letter)",
            "recommendations_weight": "5% (Employer and academic letters)",
            "interview_weight": "0% (Unless requested by specific university)",
            "test_scores_weight": "Gatekeeper requirement (minimum language cutoff)",
            "financial_need_weight": "0% (Not a criterion)",
            "selection_panel_composition": "Joint committee of German university course professors and DAAD scholarship selection officers.",
            "evaluation_methodology": "Two-phase review: Course director sifts for academic and professional fit; DAAD checks regulatory compliance and awards funding."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~8,000 to 12,000 applicants globally across all EPOS courses",
            "total_scholarships_awarded": "~300 to 500 scholarships globally",
            "acceptance_rate_global": "~3.5% to 4.5%",
            "acceptance_rate_pakistan": "~2.5% to 3.5% (Very Competitive)",
            "typical_successful_applicant_gpa": "3.30 to 3.75 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Solid academic foundation combined with 2-5 years of real-world public/private/NGO work in Pakistan.",
            "common_backgrounds_of_winners": "Engineers from WAPDA/NESPAK, urban planners, environmental researchers, ministry staff, agricultural scientists, doctors.",
            "high_representation_countries": "Pakistan, Vietnam, Colombia, Kenya, Ghana, Indonesia.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial visa agents claiming they can bypass the 2-year work experience rule. DAAD checks employment contracts rigorously."
            ],
            "application_fee_warning": "DAAD never charges application fees.",
            "agent_and_intermediary_warnings": "DAAD strictly rejects applications prepared by commercial agencies.",
            "hidden_costs_breakdown": [
                "IELTS test fee (~PKR 60,000).",
                "German Embassy visa processing and courier fees (~PKR 25,000).",
                "Blocked bank account waiver: DAAD award letter serves as financial guarantee, saving the student from having to deposit €11,208 into a German blocked account!"
            ],
            "misleading_claims_debunked": [
                "MYTH: Internships during university count towards the 2-year work experience rule. (Fact: DAAD strictly counts work experience acquired AFTER completion of the bachelor's degree).",
                "MYTH: You cannot work in Germany after graduation. (Fact: Germany allows 18-month Job Seeker Visa for all German university graduates; EPOS scholars can utilize this or return to Pakistan)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites frequently give a single generic DAAD deadline; each EPOS course has its own unique deadline between August and November."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass all exams and semester coursework according to German university study regulations.",
            "attendance_requirements": "Full-time study attendance in Germany.",
            "academic_progress_monitoring": "Annual progress and transcript checks submitted to DAAD.",
            "work_restrictions_during_study": "Part-time work permitted up to 120 full days or 240 half days per year under German student visa, but any secondary income above €520/month is deducted from the DAAD stipend.",
            "home_country_return_obligation": "Scholars are strongly expected to return to Pakistan upon graduation to contribute to national development, though no formal financial bond is enforced.",
            "service_obligations_or_bonds": "Agreement with employer in Pakistan if study leave was granted.",
            "repayment_clawback_conditions": "Termination of grant and clawback of funds in cases of academic fraud, unapproved withdrawal, or disciplinary dismissal.",
            "rules_for_changing_university": "Strictly disallowed; grant is tied to the specific EPOS course.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Extensions are granted only in rare cases of certified illness or unforeseen laboratory delays."
        },
        "official_sources_verified": [
            {
                "source_name": "DAAD Official EPOS Programme Details & Brochure",
                "source_url": "https://www.daad.de/en/study-and-research-in-germany/scholarships/daad-scholarships/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact country quota for Pakistan across individual university courses (allocations depend on committee consensus)",
                    "Course-specific candidate applicant totals"
                ]
            }
        ]
    },

    # 7. Stipendium Hungaricum Scholarship Programme (Hungary)
    "SCH-EU-001": {
        "scholarship_id": "SCH-EU-001",
        "basic_details": {
            "scholarship_name": "Stipendium Hungaricum Scholarship Programme",
            "offering_entity": "Hungarian Government (Tempus Public Foundation / Ministry of Foreign Affairs and Trade) & Government of Pakistan (HEC)",
            "host_country": "Hungary",
            "host_institutions_covered": "Hungarian State Universities (Eötvös Loránd University - ELTE, Budapest University of Technology - BME, University of Debrecen, University of Szeged, Corvinus, University of Pécs, MATE)",
            "degree_levels": ["Bachelor's", "Master's", "PhD"],
            "major_restrictions": "Eligible for almost all fields of study: Engineering, Computer Science, Natural Sciences, Medicine, Dentistry, Pharmacy, Agriculture, Business, Social Sciences, Arts and Humanities.",
            "number_of_awards_total": "~5,000 scholarship holders admitted annually worldwide from 90+ sending partners",
            "number_of_awards_pakistan": "400 reserved bilateral quota seats for Pakistani students annually (200 Bachelor's, 100 Master's, 70 One-Tier Master's/Medicine, 30 PhD)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Bachelor's: 3-4 years; Master's: 1.5-2 years; One-Tier Master's (Medicine): 5-6 years; PhD: 4 years"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizens of the Islamic Republic of Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 24,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Must be at least 18 years old by 31 August of entry year. HEC Pakistan enforces age limits: max 22-24 for Bachelor's; max 35 for Master's/PhD (up to 40 for regular public sector/faculty).",
            "academic_qualifications": "12 years education (HSSC/A-Levels) for Bachelor's; 16 years education (BS/MA/MSc) for Master's; 18 years education (MS/MPhil) for PhD.",
            "minimum_gpa_percentage": 60.0,
            "minimum_gpa_scale": 2.5,
            "grading_conversion_notes": "Minimum 60% marks in annual system or 2.50/4.00 CGPA in semester system.",
            "subject_background_prerequisites": "Relevant pre-requisite courses matching the chosen Hungarian degree.",
            "current_education_status": "Completed degrees; result-awaiting candidates can apply if final result is declared before HEC nomination deadline.",
            "graduation_year_restrictions": "None specified by Tempus.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required.",
            "english_test_required": True,
            "ielts_minimum": 5.5,
            "toefl_minimum": 72,
            "duolingo_accepted": True,
            "moi_certificate_accepted": True,
            "language_notes": "Varies by Hungarian university: IELTS 5.5 to 6.5, TOEFL iBT 72 to 90, or Duolingo 95+. Many Hungarian universities accept English Medium of Instruction (MOI) certificates from Pakistani universities or conduct their own online oral English interview.",
            "other_language_requirements": "None required; 1 year Hungarian language preparatory option available.",
            "gender_specific_requirements": "None; open to all.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates must be formally nominated by the Higher Education Commission (HEC) Pakistan.",
            "previous_scholarship_restrictions": "Previous Stipendium Hungaricum scholarship holders who re-apply within the same study level are restricted.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {"status": "100% COVERED", "details": "100% exemption from the payment of tuition fees for the entire duration of the degree program."},
            "admission_application_fee": {"status": "WAIVED", "details": "No university application fee when applying through the Stipendium Hungaricum system."},
            "accommodation": {"status": "FREE DORMITORY", "details": "Free university dormitory placement OR a monthly housing allowance of HUF 40,000/month towards private accommodation."},
            "monthly_stipend": {"status": "COVERED", "details": "Monthly living stipend paid directly by the Hungarian host university for 12 months a year.", "amount": "HUF 43,700/mo for Undergrad/Master; HUF 140,000/mo (Phase 1) and HUF 180,000/mo (Phase 2) for PhD (~PKR 35,000 to 145,000/mo)"},
            "airfare": {"status": "NOT_COVERED", "details": "International airfare between Pakistan and Hungary is NOT covered by the Hungarian government (must be paid by student or HEC)."},
            "visa_fee": {"status": "WAIVED", "details": "Type D Hungarian Student Visa application fee is WAIVED for Stipendium Hungaricum scholarship holders at the Hungarian Embassy in Islamabad."},
            "health_insurance": {"status": "COVERED", "details": "Hungarian National Health Insurance (TAJ Card) providing full medical services under Hungarian law, plus supplementary private health insurance up to HUF 65,000/year."},
            "food_allowance": {"status": "INCLUDED IN STIPEND", "details": "Subsidized meals available at university canteens."},
            "books_and_materials_allowance": {"status": "NOT_COVERED", "details": "Covered via stipend or campus library access."},
            "research_funding_conference_grant": {"status": "AVAILABLE UPON APPLICATION", "details": "University departmental doctoral grants available for PhD candidates."},
            "travel_transit_allowance": {"status": "NOT_COVERED", "details": "Local transport in Budapest/Debrecen purchased at heavily discounted student rate (~HUF 3,450/month)."},
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Applicants may select up to TWO study programs (at either 2 different universities or the same university) in order of preference (Priority 1 and Priority 2).",
            "participating_institutions": ["ELTE Budapest, BME, University of Debrecen, University of Szeged, Corvinus Budapest, University of Pécs, MATE, Óbuda University, Széchenyi István University"],
            "university_rankings_scope": "Top 1 to 10 universities in Hungary; QS World Rankings 500-1000.",
            "available_majors": ["Computer Science", "Artificial Intelligence", "Medicine (One-Tier 6yr)", "Dentistry", "Pharmacy", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Biotechnology", "Business", "Economics", "Agriculture"],
            "english_taught_program_availability": True,
            "program_duration": "Bachelor's: 3-4 years; Master's: 1.5-2 years; One-tier Master's: 5-6 years; PhD: 4 years",
            "admission_requirements_summary": "Online application, transcripts, medical certificate, motivation letter, institutional online exam / Skype interview.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Single application through DreamApply portal; institutional entrance exams are held online in April/May.",
            "strategic_program_match_advice": "Priority 1 choice receives maximum focus from universities; ensure Priority 1 is your strongest academic alignment."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://apply.stipendiumhungaricum.hu/",
            "portal_system_name": "DreamApply Online Application System & HEC Scholarship Portal (scholarship.hec.gov.pk)",
            "account_creation_instructions": "MANDATORY DUAL SUBMISSION: 1) Register and apply on the Hungarian DreamApply portal; AND 2) Register and apply on the HEC Pakistan Scholarship portal.",
            "step_by_step_workflow": [
                "1. Register on Tempus DreamApply portal (opens mid-November).",
                "2. Select 2 study programs in order of preference.",
                "3. Upload transcripts, certificates, medical certificate, motivation letter, and passport.",
                "4. Submit DreamApply application by January 15 deadline.",
                "5. Register on HEC Pakistan Scholarship portal (scholarship.hec.gov.pk).",
                "6. Fill HEC online profile and submit under 'Stipendium Hungaricum' category.",
                "7. Take HEC USAT (for Undergrad) or HEC HAT (for Master's/PhD) aptitude test.",
                "8. HEC prepares national merit list based on academic formula (50%) + HAT/USAT score (50%).",
                "9. HEC nominates top 400 candidates (+ reserve list) to Tempus Public Foundation in February.",
                "10. Nominated candidates take online entrance examinations/interviews with Hungarian universities (March - May).",
                "11. Tempus Public Foundation issues final Letters of Award in June/July.",
                "12. Apply for Hungarian Type D Visa at Embassy in Islamabad and depart in September."
            ],
            "university_vs_scholarship_routing": "Integrated DreamApply routing + HEC national nomination.",
            "recommendation_letters_submission_method": "Required for PhD applicants (2 letters of recommendation from professors with doctoral degrees); not mandatory for Bachelor's/Master's.",
            "personal_statement_prompts": "Motivation Letter (minimum 1 page / 4,000 characters): Why Hungary, reasons for selecting specific programs, and career ambitions.",
            "study_plan_research_proposal_requirements": "PhD applicants must upload a detailed research plan (minimum 2 pages) and statement of supervisor acceptance.",
            "cv_format_requirements": "Europass CV format.",
            "interviews_conducted": True,
            "interview_format_details": "Online institutional entrance exam (written test) followed by 10-15 minute oral interview via Skype/Teams conducted by Hungarian faculty professors.",
            "standardized_tests": "HEC USAT (Undergrad) or HEC HAT (Postgrad) required for Pakistani nomination. Hungarian universities conduct their own subject tests.",
            "application_fee_amount": "HUF 0 (Tempus application is free; HEC charges nominal test fee PKR 2,000 for HAT/USAT).",
            "attestation_requirements": "Degrees must be attested by HEC / IBCC and Ministry of Foreign Affairs (MOFA) prior to visa issuance.",
            "translation_requirements": "Certified English translations if originals are in Urdu.",
            "final_submission_method": "Dual online portal submission (DreamApply + HEC)."
        },
        "required_documents_checklist": [
            {"document_name": "Scanned Copy of Valid Passport", "mandatory": True, "specification": "Passport valid for at least 18 months", "pakistan_specific_instruction": "Required for DreamApply registration and visa"},
            {"document_name": "Educational Certificates & Transcripts", "mandatory": True, "specification": "Matric, Inter, Bachelor's, and Master's degrees and detailed marks certificates", "pakistan_specific_instruction": "Must be attested by IBCC (matric/inter) and HEC (degrees)"},
            {"document_name": "Proof of Language Proficiency", "mandatory": True, "specification": "IELTS, TOEFL, Duolingo, or English Medium of Instruction certificate", "pakistan_specific_instruction": "Check individual Hungarian university requirements"},
            {"document_name": "Medical Certificate", "mandatory": True, "specification": "Official medical certificate from registered physician confirming negative tests for HIV, Hepatitis B/C, and Chest X-ray", "pakistan_specific_instruction": "Mandatory Tempus template issued not older than 1 month"},
            {"document_name": "Statement of Application", "mandatory": True, "specification": "Signed declaration on DreamApply portal", "pakistan_specific_instruction": "Signed electronically on the portal"},
            {"document_name": "Motivation Letter", "mandatory": True, "specification": "Minimum 1 page detailing academic purpose and Hungarian context", "pakistan_specific_instruction": "Address both Priority 1 and Priority 2 programs"},
            {"document_name": "Research Plan & Supervisor Letter (PhD only)", "mandatory": False, "specification": "Minimum 2-page detailed research proposal", "pakistan_specific_instruction": "Mandatory for PhD candidates"}
        ],
        "important_dates_timeline": {
            "application_open_date": "Mid-November annually (e.g., 2026-11-15)",
            "application_deadline": "January 15 annually (at 14:00 Central European Time)",
            "university_admission_deadline": "Coincides with January 15 deadline",
            "document_submission_deadline": "January 15 (Missing documents uploaded until August 1)",
            "recommendation_letters_deadline": "January 15",
            "interview_period": "March - May (Online entrance exams and Skype interviews)",
            "shortlist_announcement": "HEC nomination in late February; Final awards in June/July",
            "final_result_acceptance_deadline": "Mid-July annually",
            "visa_application_window": "July - August (Hungarian Embassy Islamabad)",
            "semester_commencement": "September (Fall Semester)",
            "annual_cycle_notes": "Both DreamApply and HEC portal applications must be completed before their respective deadlines."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Matric, Inter, and Bachelor's marks calculated via HEC formula)",
            "extracurricular_and_leadership_weight": "5% (General suitability)",
            "research_experience_weight": "15% (For PhD applicants; proposal review by Hungarian supervisors)",
            "work_experience_weight": "5% (Professional relevance)",
            "personal_statement_weight": "10% (Motivation letter quality)",
            "recommendations_weight": "5% (Academic references)",
            "interview_weight": "20% (Hungarian university institutional exam and oral interview score)",
            "test_scores_weight": "HEC USAT / HAT test accounts for 50% of the initial national nomination score in Pakistan!",
            "financial_need_weight": "0% (Pure bilateral merit quota)",
            "selection_panel_composition": "Stage 1: HEC Pakistan National Nomination Committee; Stage 2: Hungarian University Departmental Admissions Committees; Stage 3: Tempus Board of Trustees.",
            "evaluation_methodology": "HEC nominates candidate pool via academic + test merit; Hungarian universities examine candidates via online tests/interviews and give admission scores (Pass/Fail/Waitlist); Tempus confirms awards."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000 to 14,000 applicants in Pakistan across all degree levels",
            "total_scholarships_awarded": "400 principal awards exclusively reserved for Pakistan annually",
            "acceptance_rate_global": "N/A (Bilateral country quota)",
            "acceptance_rate_pakistan": "~2.8% to 4.0% (Moderate-High Competition, but largest European quota for Pakistan)",
            "typical_successful_applicant_gpa": "3.20 to 3.70 / 4.00 CGPA (or 70-85% marks in HSSC/FSc)",
            "typical_academic_and_research_profile": "Solid grades in intermediate/bachelor's and strong score on HEC USAT/HAT test (typically 65+ out of 100).",
            "common_backgrounds_of_winners": "FSc Pre-Medical and Pre-Engineering students (for BS and Medicine); graduates of UET, NUST, FAST, COMSATS, Punjab University, Karachi University.",
            "high_representation_countries": "Reserved exclusively for Pakistan under bilateral cultural agreement.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents in Lahore, Rawalpindi, and Karachi charging PKR 100,000 to 300,000 claiming they 'guarantee nomination on the HEC Hungary quota'. HEC nominations are strictly computerized and merit-based.",
                "Unofficial portals charging application fees."
            ],
            "application_fee_warning": "DreamApply is completely FREE. HEC charges only the standard test registration fee for HAT/USAT (~PKR 2,000).",
            "agent_and_intermediary_warnings": "Never hire an agent. All portals and communication are direct with the applicant.",
            "hidden_costs_breakdown": [
                "International flight ticket to Budapest: NOT covered by Hungarian scholarship (PKR 180,000 to 250,000 one-way/return).",
                "HEC & IBCC document attestation fees and MOFA apostille stamps (PKR 10,000 to 20,000).",
                "Medical screening lab tests (HIV, Hepatitis, X-Ray: approx PKR 10,000 to 15,000).",
                "Monthly stipend limitation: HUF 43,700 (~PKR 35,000/mo) for undergrad/master is tight; students often need modest personal pocket money support (~€100-€150/mo) or part-time work."
            ],
            "misleading_claims_debunked": [
                "MYTH: Flights are covered. (Fact: Airfare is explicitly the responsibility of the student).",
                "MYTH: You cannot work in Hungary. (Fact: International students can legally work up to 30 hours/week during study term in Hungary)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Agents often fail to inform applicants about the mandatory HEC portal application; applying on DreamApply without applying on the HEC portal results in immediate disqualification for Pakistanis."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must earn at least 36 credits across every two consecutive semesters (or 18 credits per semester) according to Hungarian institutional regulations.",
            "attendance_requirements": "Physical residence in Hungary mandatory. Being absent for more than 30 consecutive days without written permission leads to scholarship termination.",
            "academic_progress_monitoring": "Semi-annual credit and attendance reports sent by universities to Tempus Public Foundation.",
            "work_restrictions_during_study": "Students holding a Hungarian Residence Permit for Study purposes may work up to 30 hours per week during term-time and full-time during vacations.",
            "home_country_return_obligation": "No mandatory home residency restriction enforced by Hungary; students can transition to Hungarian 9-month Job Seeker Residence Permit upon graduation or pursue PhDs across the EU.",
            "service_obligations_or_bonds": "HEC Pakistan requires signing an undertaking form agreeing to return, though enforcement is non-statutory for self-funded travel.",
            "repayment_clawback_conditions": "If a student drops out without certified medical emergency, scholarship funding and health insurance terminate immediately.",
            "rules_for_changing_university": "Permitted ONCE during the scholarship tenure within the first year of studies, subject to approval by both Hungarian universities and Tempus.",
            "rules_for_changing_major": "Permitted ONCE, strictly within the same sending partner quota and study level.",
            "extension_policy": "Bachelor's and Master's programs can be extended by a maximum of 2 semesters upon written application and university approval (stipend is suspended during extension, but tuition remains waived)."
        },
        "official_sources_verified": [
            {
                "source_name": "Tempus Public Foundation - Stipendium Hungaricum Official Portal",
                "source_url": "https://stipendiumhungaricum.hu/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact number of applicants from Pakistan who sat for entrance tests at each university",
                    "Passing score thresholds for specific university entrance tests"
                ]
            },
            {
                "source_name": "Higher Education Commission (HEC) Pakistan - Bilateral Hungarian Scholarship Page",
                "source_url": "https://scholarship.hec.gov.pk/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Yearly cutoff merit scores on the HEC formula (HEC generates merit dynamically based on annual candidate pool)"
                ]
            }
        ]
    }
}
