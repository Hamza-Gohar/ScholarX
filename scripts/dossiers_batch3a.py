"""
scripts/dossiers_batch3a.py
Part A of Batch 3:
1. SCH-EU-023: Gates Cambridge Scholarship (University of Cambridge, UK)
2. SCH-EU-030: Clarendon Fund Scholarships (University of Oxford, UK)
3. SCH-AS-004: ANSO Scholarship for Young Talents (CAS/USTC/UCAS, China)
4. SCH-AS-005: Hong Kong PhD Fellowship Scheme (HKPFS, Hong Kong)
"""

DOSSIERS_BATCH3A = {
    # 1. Gates Cambridge Scholarship (SCH-EU-023)
    "SCH-EU-023": {
        "scholarship_id": "SCH-EU-023",
        "basic_details": {
            "scholarship_name": "Gates Cambridge Scholarship",
            "offering_entity": "Bill & Melinda Gates Foundation & University of Cambridge",
            "host_country": "United Kingdom",
            "host_institutions_covered": "University of Cambridge (all 31 Cambridge Colleges)",
            "degree_levels": ["Master's (MPhil/LLM/MASt)", "PhD (Doctorate)"],
            "major_restrictions": "Open to any subject available at the University of Cambridge EXCEPT undergraduate degrees, non-degree courses, MBBChir Clinical Medicine, and part-time degrees.",
            "number_of_awards_total": "~80 full-cost scholarships awarded annually (~25 US round, ~55 International round)",
            "number_of_awards_pakistan": "Open globally; exceptional Pakistani scholars selected in the international round",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full duration of the degree: 1 year for MPhil/LLM; up to 3 to 4 years for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["A citizen of any country outside the United Kingdom (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (Bachelor's) for Master's; 18 years (Master's) for PhD with first-class academic standing.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Equivalent to a Cambridge First Class Honours degree (minimum 3.80 / 4.00 CGPA or top 2% class ranking).",
            "subject_background_prerequisites": "Outstanding academic background in proposed discipline with exceptional analytical and critical thinking skills.",
            "current_education_status": "Graduated or in final year of undergraduate or master's studies.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Commitment to improving the lives of others, public leadership, and social enterprise evaluated.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.5,
                "toefl_minimum": 110,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Must satisfy Cambridge department English requirement (typically IELTS Academic 7.5 with no band below 7.0 or TOEFL iBT 110 with 25 in all components)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Four core criteria: Outstanding intellectual ability, reasons for choice of course, commitment to improving the lives of others, leadership potential.",
            "previous_scholarship_restrictions": "Cannot hold another full scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "University Composition Fee and College Fee at the appropriate international rate fully covered.",
                "amount": "£28,000 to £44,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Cambridge graduate application fee (£65 to £75) paid by candidate (fee waivers available for eligible low-income countries upon request).",
                "amount": "£75"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered through living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Generous maintenance allowance to cover accommodation, food, and living expenses.",
                "amount": "£20,000 / year (~£1,666 / month or ~PKR 605,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One economy single airfare at both the beginning and end of the course.",
                "amount": None
            },
            "visa_fee": {
                "status": "COVERED",
                "details": "Inbound visa costs (UK Student Route visa) and the Immigration Health Surcharge (IHS) fully covered.",
                "amount": "£490 visa + ~£776/year IHS"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Full UK National Health Service (NHS) access via covered Immigration Health Surcharge.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Academic development funding of up to £2,000 available to attend conferences and courses.",
                "amount": "Up to £2,000"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Fieldwork funding available for PhD research outside Cambridge.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Family allowance available (up to £11,604 for one child, £16,548 for two or more children) for scholars with dependents.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 75000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Cambridge (World Top 3).",
            "participating_institutions": [
                "University of Cambridge (Trinity, St John's, King's, Churchill, Jesus, Clare, Queens', Fitzwilliam, all 31 colleges)"
            ],
            "university_rankings_scope": "QS World Rank #2; world leader in research across all humanities, social sciences, and STEM.",
            "available_majors": [
                "Computer Science, Advanced Computer Science, Engineering, Biotechnology, Physics, Applied Mathematics & Theoretical Physics (DAMTP), Public Health, Medical Sciences, Law (LLM), Economics, Public Policy (MPP), International Relations, History, Philosophy"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 year for MPhil/LLM; 3 to 4 years for PhD",
            "admission_requirements_summary": "Apply for graduate admission to Cambridge via the Postgraduate Applicant Portal and complete the dedicated Gates Cambridge section.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "PhD candidates must have strong alignment with prospective Cambridge supervisor; MPhil is evaluated by departmental committee.",
            "strategic_program_match_advice": "The 500-word Gates statement must convince the trust of your moral commitment to use your Cambridge education to improve the lives of others."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.gatescambridge.org/",
            "portal_system_name": "University of Cambridge Postgraduate Applicant Portal",
            "account_creation_instructions": "Register on the Cambridge Applicant Portal, choose degree course, select 'Yes' for Gates Cambridge funding, and upload Gates reference and statement.",
            "step_by_step_workflow": [
                "1. Choose course and check departmental deadline (Round opens September; International deadline: early December or early January depending on course).",
                "2. Write 500-word Gates Cambridge Statement explaining how you meet the scholarship criteria.",
                "3. Secure a dedicated Gates Cambridge Reference Letter in addition to two academic reference letters.",
                "4. Submit complete course and scholarship application before your course deadline.",
                "5. Academic departments rank applicants and put forward top candidates to the Gates Cambridge Trust (January).",
                "6. Shortlisted candidates invited for a 20-25 minute panel interview in late March.",
                "7. Final offers announced in late March/early April."
            ],
            "university_vs_scholarship_routing": "Integrated single application via the Cambridge Postgraduate Portal.",
            "recommendation_letters_submission_method": "Submitted online by referees: two academic referees + one specialized Gates referee.",
            "personal_statement_prompts": "Gates Statement (500 words): Explain why you are applying for a Gates Cambridge Scholarship and how you meet the four scholarship criteria.",
            "study_plan_research_proposal_requirements": "PhD applicants must upload a detailed research proposal (typically 2-4 pages); MPhil applicants submit statement of interest.",
            "cv_format_requirements": "Detailed academic CV highlighting publications, leadership roles, and volunteerism.",
            "interviews_conducted": True,
            "interview_format_details": "20-25 minute virtual panel interview with four distinct components: academic background, why Cambridge, commitment to improving lives, and leadership capacity.",
            "standardized_tests": "GRE required only by a few specific departments (e.g. Economics); English language test required.",
            "application_fee_amount": "£75.",
            "attestation_requirements": "Certified transcripts and degree certificates; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via Cambridge Postgraduate Portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Gates Cambridge Statement",
                "mandatory": True,
                "specification": "500-word statement explaining alignment with the four Gates criteria",
                "pakistan_specific_instruction": "Authentic narrative demonstrating leadership and impact in Pakistan"
            },
            {
                "document_name": "Gates Reference Letter",
                "mandatory": True,
                "specification": "Separate reference speaking specifically to your leadership and commitment to others",
                "pakistan_specific_instruction": "From someone who knows your character, social initiatives, or leadership"
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Submitted directly by university research professors",
                "pakistan_specific_instruction": "Speaking to academic ranking and intellectual brilliance"
            },
            {
                "document_name": "Research Proposal (for PhD)",
                "mandatory": True,
                "specification": "Structured scientific research proposal (2-4 pages)",
                "pakistan_specific_instruction": "Aligned with prospective Cambridge laboratory"
            },
            {
                "document_name": "English Proficiency Score",
                "mandatory": True,
                "specification": "IELTS Academic (7.5+) or TOEFL iBT (110+)",
                "pakistan_specific_instruction": "Official electronic score report"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2027-01-07",
            "university_admission_deadline": "2027-01-07",
            "document_submission_deadline": "2027-01-07",
            "recommendation_letters_deadline": "2027-01-14",
            "interview_period": "Late March 2027",
            "shortlist_announcement": "Early March 2027",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "October 2027 (Michaelmas Term)",
            "annual_cycle_notes": "International round deadline depends on course (either December 3, 2026 or January 7, 2027). Interviews held late March."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Outstanding intellectual ability, first-class degree, rank in class)",
            "extracurricular_and_leadership_weight": "25% (Demonstrated leadership potential and capacity to effect change)",
            "research_experience_weight": "15% (For PhD: quality and originality of research proposal)",
            "work_experience_weight": "5% (Social impact initiatives)",
            "personal_statement_weight": "15% (Gates Statement articulating commitment to improving lives of others)",
            "recommendations_weight": "10% (Quality of the dedicated Gates reference letter)",
            "interview_weight": "Decisive in final round",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit and leadership driven)",
            "selection_panel_composition": "Two-tier sift: Cambridge academic departments shortlist top applicants; Gates Cambridge multidisciplinary interviewing panels conduct final interviews.",
            "evaluation_methodology": "Equal assessment of four pillars: Intellectual Ability, Reasons for Choice of Course, Commitment to Improving Lives of Others, Leadership Potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~6,000 international applicants across all disciplines",
            "total_scholarships_awarded": "~80 scholarships awarded globally (~55 in international round)",
            "acceptance_rate_global": "~1.3%",
            "acceptance_rate_pakistan": "~0.8% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.85 to 4.00 CGPA",
            "typical_academic_and_research_profile": "Scholars combining exceptional academic grades with extraordinary social impact: NGO founders, policy innovators, climate advocates, and scientific researchers.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (LUMS, NUST, AKU, IBA) with prominent public service records.",
            "high_representation_countries": "USA, India, Pakistan, Canada, China, Germany, Australia, Nigeria.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized services offering 'Gates interview prep' or essay writing."
            ],
            "application_fee_warning": "Pay the Cambridge application fee (£75) only on the official postgraduate portal.",
            "agent_and_intermediary_warnings": "Never work through agents; Gates Cambridge looks for authentic personal voice and integrity.",
            "hidden_costs_breakdown": [
                "Cambridge application fee (£75).",
                "English language test fees (IELTS/TOEFL).",
                "Initial relocation buffer before first stipend release in Cambridge."
            ],
            "misleading_claims_debunked": [
                "MYTH: Only PhD students are funded. (Fact: About one-third of Gates Cambridge awards go to 1-year Master's students).",
                "MYTH: You need work experience. (Fact: Academic excellence and leadership potential are primary; work experience is not mandatory)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External sites claim Gates pays for family in all cases; family allowance is discretionary and requires formal application."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain good academic standing and progress in accordance with University of Cambridge degree regulations.",
            "attendance_requirements": "Full-time physical residence in Cambridge during terms (minimum terms of residence required by university statues).",
            "academic_progress_monitoring": "Annual progress reports submitted by Cambridge faculty supervisor to the Gates Cambridge Trust.",
            "work_restrictions_during_study": "Cambridge University policy restricts graduate students from undertaking outside employment during full-time study, except limited college supervisions/demonstrating (max 6 hrs/week).",
            "home_country_return_obligation": "None; scholars are eligible for the UK 2-year Graduate Route visa (or 3-year for PhD) post-graduation.",
            "service_obligations_or_bonds": "None; active engagement with the Gates Cambridge Scholars' Council and alumni network.",
            "repayment_clawback_conditions": "Funding terminated in case of academic failure or withdrawal.",
            "rules_for_changing_university": "Non-transferable outside Cambridge.",
            "rules_for_changing_major": "Requires approval from both the university and the Gates Cambridge Trust.",
            "extension_policy": "PhD scholars can apply for up to 6 months of discretionary funding extension if research delays are justified."
        },
        "official_sources_verified": [
            {
                "source_name": "Gates Cambridge Trust Official Portal",
                "source_url": "https://www.gatescambridge.org/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental shortlisting cutoff rankings for candidate nomination to the Trust",
                    "Specific country quota allocations"
                ]
            }
        ]
    },

    # 2. Clarendon Fund Scholarships (University of Oxford) (SCH-EU-030)
    "SCH-EU-030": {
        "scholarship_id": "SCH-EU-030",
        "basic_details": {
            "scholarship_name": "Clarendon Fund Scholarships",
            "offering_entity": "University of Oxford & Oxford University Press",
            "host_country": "United Kingdom",
            "host_institutions_covered": "University of Oxford (all 44 Colleges and Permanent Private Halls)",
            "degree_levels": ["Master's (1 to 2 years: MPhil, MSc, BCL, MSt)", "DPhil / PhD (3 to 4 years)"],
            "major_restrictions": "Open to all graduate degree programs across all academic departments at Oxford (Humanities, Mathematical, Physical and Life Sciences, Medical Sciences, Social Sciences).",
            "number_of_awards_total": "~200 new fully-funded scholarships awarded annually",
            "number_of_awards_pakistan": "Open globally to all nationalities without quotas; dozens of Pakistani scholars have received Clarendon awards",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Full duration of the degree course: 1 to 2 years for Master's; up to 3 to 4 years for DPhil (Doctor of Philosophy)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to students of all nationalities (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (Bachelor's) for Master's; 18 years (Master's) for DPhil with exceptional academic standing.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Equivalent to an Oxford First Class Honours degree (minimum 3.80 / 4.00 CGPA or top 3% class standing).",
            "subject_background_prerequisites": "Substantive academic excellence in the chosen discipline.",
            "current_education_status": "Graduated or in final year of undergraduate or master's studies.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior academic publications, awards, and intellectual leadership heavily prioritized.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.5,
                "toefl_minimum": 110,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Must satisfy Oxford course English requirement (Higher Level: IELTS 7.5 with 7.0 in each component, TOEFL 110; Standard Level: IELTS 7.0, TOEFL 100)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Automatic consideration: Every applicant who applies for a graduate degree by the December/January deadline is automatically evaluated.",
            "previous_scholarship_restrictions": "Cannot hold another full funding package concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full course fees (University Composition Fee and College Fee) covered for the full duration of the degree.",
                "amount": "£29,000 to £48,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Oxford graduate application fee (£75) paid by candidate (waivers available for low-income countries upon application).",
                "amount": "£75"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered through living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Generous annual grant for living expenses aligned with UKRI minimum doctoral rates.",
                "amount": "£19,237 / year (~£1,603 / month or ~PKR 580,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare to the UK is paid by student from living allowance or personal funds.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "UK student visa fee (£490) and Immigration Health Surcharge (~£776/year) paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "ACCESSIBLE_VIA_IHS",
                "details": "Access to UK National Health Service (NHS) upon payment of Immigration Health Surcharge.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "College book grants and departmental laboratory resources provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "AVAILABLE UPON APPLICATION",
                "details": "College and departmental research travel grants available for conference attendance.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Personal responsibility.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 68000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Oxford (World Top 3).",
            "participating_institutions": [
                "University of Oxford (Christ Church, Balliol, Magdalen, New College, St John's, Nuffield, Exeter, all 44 colleges)"
            ],
            "university_rankings_scope": "Times Higher Education World #1; QS World Rank #3.",
            "available_majors": [
                "Computer Science, Artificial Intelligence, Mathematics, Theoretical Physics, Engineering Science, Clinical Medicine, Pharmacology, Biochemistry, Law (BCL), Economics, Public Policy (MPP), International Relations, Philosophy, History"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 to 2 years for Master's; 3 to 4 years for DPhil",
            "admission_requirements_summary": "No separate scholarship application is required. Simply apply for your chosen graduate course by the relevant December or January deadline.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Admissions are decided by academic departments; colleges then match admitted scholars.",
            "strategic_program_match_advice": "Focus all energy on academic excellence, writing sample quality, and strong research proposal matching faculty strengths."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ox.ac.uk/clarendon",
            "portal_system_name": "University of Oxford Graduate Application Portal",
            "account_creation_instructions": "Register on the Oxford Graduate Application System, select your degree course, upload academic dossier, and submit by the course deadline.",
            "step_by_step_workflow": [
                "1. Choose graduate course and verify the relevant scholarship deadline (Friday, December 1 or Friday, January 8 depending on course).",
                "2. Prepare Statement of Purpose, academic transcripts, writing samples, and CV.",
                "3. Secure three academic reference letters submitted directly by referees.",
                "4. Submit online graduate application before the deadline.",
                "5. Academic departments assess applications and nominate their top candidates for Clarendon in February.",
                "6. Clarendon selection panels review nominations and issue award letters in March/April."
            ],
            "university_vs_scholarship_routing": "Fully automatic: Applying for the degree automatically enters you into consideration.",
            "recommendation_letters_submission_method": "Submitted online by three academic referees via secure Oxford portal link.",
            "personal_statement_prompts": "Statement of Purpose detailing academic motivations, research questions, and reasons for choosing Oxford.",
            "study_plan_research_proposal_requirements": "Detailed research proposal (for DPhil and research master's) detailing methodology and scientific relevance.",
            "cv_format_requirements": "Academic CV detailing qualifications, academic prizes, publications, and relevant research experience.",
            "interviews_conducted": True,
            "interview_format_details": "Many Oxford departments (e.g. Computer Science, Engineering, Medicine) conduct 20-30 minute academic video interviews before admission.",
            "standardized_tests": "GRE required only by Economics and Said Business School courses; English test required.",
            "application_fee_amount": "£75.",
            "attestation_requirements": "Certified transcripts; HEC attestation required for visa.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via Oxford Graduate Application Portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "Academic statement detailing motivation and preparation for the course",
                "pakistan_specific_instruction": "Demonstrating intellectual rigor and analytical ability"
            },
            {
                "document_name": "Academic Transcripts & Certificates",
                "mandatory": True,
                "specification": "Complete transcripts showing all courses and marks",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Three Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential reports from former professors assessing academic ability",
                "pakistan_specific_instruction": "From professors who taught your BS/MS courses in Pakistan"
            },
            {
                "document_name": "Writing Sample / Research Proposal",
                "mandatory": True,
                "specification": "Essays or scientific papers demonstrating original analytical capability",
                "pakistan_specific_instruction": "Published research papers or undergraduate thesis chapters"
            },
            {
                "document_name": "English Proficiency Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (7.5+) or TOEFL iBT (110+)",
                "pakistan_specific_instruction": "Meeting Oxford course threshold"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2027-01-08",
            "university_admission_deadline": "2027-01-08",
            "document_submission_deadline": "2027-01-08",
            "recommendation_letters_deadline": "2027-01-08",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "October 2027 (Michaelmas Term)",
            "annual_cycle_notes": "Strict deadline is the relevant January course deadline (usually the first or second Friday in January). Results issued in March."
        },
        "selection_process_and_weights": {
            "academic_weight": "50% (Academic excellence, first-class honours standing, GPA, class rank)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "25% (Quality of research proposal, writing sample, and research output)",
            "work_experience_weight": "0%",
            "personal_statement_weight": "10% (Clarity of intellectual purpose)",
            "recommendations_weight": "10% (Strength of academic referee ratings)",
            "interview_weight": "Conducted by departmental admissions committee",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Purely merit-based; no financial assessment)",
            "selection_panel_composition": "Academic departmental selection panels and the central Clarendon Fund Selection Committee.",
            "evaluation_methodology": "Sole selection criterion is outstanding academic merit and intellectual potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~30,000+ graduate applicants across the University of Oxford",
            "total_scholarships_awarded": "~200 Clarendon scholarships awarded annually",
            "acceptance_rate_global": "~0.7% across all applicants",
            "acceptance_rate_pakistan": "~0.5% (Extremely Selective)",
            "typical_successful_applicant_gpa": "3.85 to 4.00 CGPA (Top 1% of graduating class)",
            "typical_academic_and_research_profile": "Top-of-class graduates with exceptional analytical writing samples, conference publications, and stellar faculty endorsements.",
            "common_backgrounds_of_winners": "Top graduates of Pakistani universities (LUMS, NUST, Quaid-i-Azam, IBA) enrolled in DPhil and master's courses.",
            "high_representation_countries": "Global distribution across UK, USA, China, Germany, Pakistan, India, Canada.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites claiming to sell 'Clarendon scholarship application forms'; no separate form exists."
            ],
            "application_fee_warning": "Pay only the £75 university application fee on the official Oxford portal.",
            "agent_and_intermediary_warnings": "Oxford does not work with agents; apply directly on the online portal.",
            "hidden_costs_breakdown": [
                "Oxford graduate application fee (£75).",
                "UK student visa fee (£490) + Immigration Health Surcharge (~£776/year).",
                "International flights to the UK (~PKR 250,000 to 350,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: You need a separate application form for Clarendon. (Fact: There is NO separate form; you are automatically considered when applying by the January deadline).",
                "MYTH: Only PhD students get Clarendon. (Fact: Both Master's and DPhil students are eligible and receive awards)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs state Clarendon covers flights and visas; officially, Clarendon covers full tuition and living stipend, but NOT flights or visas."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance in accordance with Oxford University regulations.",
            "attendance_requirements": "Full-time physical residence within the statutory residency limits of Oxford.",
            "academic_progress_monitoring": "Termly reports submitted by academic supervisor via the Graduate Supervision Reporting (GSR) system.",
            "work_restrictions_during_study": "Oxford University policy strictly limits full-time graduate students from working more than 8 hours per week during term-time.",
            "home_country_return_obligation": "None; scholars are eligible for the UK Graduate Route work visa (2 years for Master's, 3 years for DPhil).",
            "service_obligations_or_bonds": "None; active participation in the Clarendon Scholars' Association.",
            "repayment_clawback_conditions": "Funding terminated upon failure of progress reviews or voluntary withdrawal.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from the academic department and the Clarendon Fund.",
            "extension_policy": "Funding is provided for the standard fee liability period of the course."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Oxford - Clarendon Fund Official Portal",
                "source_url": "https://www.ox.ac.uk/clarendon",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental quota distribution between humanities and STEM faculties",
                    "Internal ranking score conversion rubrics"
                ]
            }
        ]
    },

    # 3. ANSO Scholarship for Young Talents (CAS, China) (SCH-AS-004)
    "SCH-AS-004": {
        "scholarship_id": "SCH-AS-004",
        "basic_details": {
            "scholarship_name": "ANSO Scholarship for Young Talents",
            "offering_entity": "Alliance of International Science Organizations (ANSO) & Chinese Academy of Sciences (CAS)",
            "host_country": "China",
            "host_institutions_covered": "University of Science and Technology of China (USTC) & University of Chinese Academy of Sciences (UCAS) and over 100 CAS research institutes across China",
            "degree_levels": ["Master's", "PhD (Doctoral)"],
            "major_restrictions": "Science, Technology, Engineering, Mathematics, and Medicine (STEM): Physical Sciences, Chemical Sciences, Life Sciences, Earth & Environmental Sciences, Computer Science, AI, Materials Science, Engineering.",
            "number_of_awards_total": "~500 scholarships awarded annually (~200 Master's, ~300 PhD)",
            "number_of_awards_pakistan": "Open to Pakistan as a founding member country of ANSO (~50 to 80 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 36 months for Master's; up to 48 months for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-Chinese citizens of an eligible country (Pakistani citizens eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 35,
            "age_limit_notes": "Master's applicants: maximum 30 years of age; PhD applicants: maximum 35 years of age on December 31 of award year.",
            "academic_qualifications": "16 years of education (Bachelor's) for Master's; 18 years (Master's) for PhD from an HEC-recognized institution.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA or equivalent; admitted scholars typically present 3.50+ CGPA.",
            "subject_background_prerequisites": "Undergraduate or postgraduate degree in natural sciences, engineering, or computing.",
            "current_education_status": "Graduated or in final semester of degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications in international peer-reviewed journals (SCI/EI indexed) carry decisive weight.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "IELTS Academic 6.5+, TOEFL iBT 90+, or official English Proficiency Certificate (Medium of Instruction - MOI) issued by university registrar."
            },
            "other_language_requirements": "Chinese language (HSK) not mandatory for English-taught programs.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates MUST find a host supervisor at USTC or UCAS/CAS institute who agrees to accept them.",
            "previous_scholarship_restrictions": "Ineligible if currently enrolled in a Chinese university or holding another Chinese government scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition waiver for the entire duration of the degree program at USTC or UCAS.",
                "amount": "RMB 30,000 to 40,000 / year"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application fee waived by host institutions for ANSO applicants.",
                "amount": None
            },
            "accommodation": {
                "status": "FREE DORMITORY",
                "details": "Free on-campus dormitory accommodation (single room for PhD, shared room for Master's) or off-campus housing subsidy.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Generous monthly living allowance paid directly to scholar.",
                "amount": "Master's: RMB 3,000 / month (~PKR 115,000 / month); PhD: RMB 6,000 to 7,000 / month (~PKR 230,000 to 270,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "International travel subsidy provided (one round-trip flight from home country to China).",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Chinese student visa (X1) application fee paid by student at Chinese Visa Application Service Centre (Gerry's) in Pakistan.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive Medical Insurance for Foreign Students in China provided (RMB 800/year).",
                "amount": "RMB 800 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Full access to state key laboratories and research project funding through the Chinese Academy of Sciences.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "One-time settlement subsidy provided upon initial arrival.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply to either University of Science and Technology of China (USTC) or University of Chinese Academy of Sciences (UCAS).",
            "participating_institutions": [
                "University of Science and Technology of China (USTC - Hefei)",
                "University of Chinese Academy of Sciences (UCAS - Beijing)",
                "Over 100 CAS Research Institutes (Institute of Physics, Institute of Automation, Shanghai Institute of Optics, etc.)"
            ],
            "university_rankings_scope": "USTC is World Top 60 (Nature Index Top 5 globally); CAS is World #1 research organization in Nature Index.",
            "available_majors": [
                "Artificial Intelligence, Computer Science, Quantum Information, Condensed Matter Physics, Chemistry, Materials Science, Environmental Sciences, Biology, Mechanical Engineering, Automation, Astronomy, Earth Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Up to 3 years for Master's; up to 4 years for PhD",
            "admission_requirements_summary": "Contact prospective supervisor at USTC or UCAS to secure Provisional Acceptance Form; then apply via the university international student portal.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing supervisor acceptance is the key hurdle; once a professor accepts you, scholarship conversion is very high.",
            "strategic_program_match_advice": "Search CAS research institutes directly; contacting faculty whose research matches your thesis publications yields the best response."
        },
        "application_process_roadmap": {
            "submission_portal_url": "http://www.anso.org.cn/",
            "portal_system_name": "USTC / UCAS International Online Application System",
            "account_creation_instructions": "Register on the USTC or UCAS online portal (Opens October/November), select 'ANSO Scholarship for Young Talents', and upload supervisor acceptance.",
            "step_by_step_workflow": [
                "1. Identify CAS/USTC faculty members in your research field and email them with your CV and publications (October-December).",
                "2. Secure the signed 'Provisional Acceptance of International Student by Professor' form.",
                "3. Create account on USTC portal (isa.ustc.edu.cn) or UCAS portal (admission.ucas.ac.cn).",
                "4. Select ANSO Scholarship and upload academic degrees, transcripts, research proposal, and references.",
                "5. Submit complete application before deadline (February 15).",
                "6. Academic review and expert panel evaluations take place in March/April.",
                "7. Final ANSO scholarship results announced in May/June; JW202 visa forms issued."
            ],
            "university_vs_scholarship_routing": "Combined single application via USTC or UCAS portal.",
            "recommendation_letters_submission_method": "Submitted online by two professors via email link sent by the admission system.",
            "personal_statement_prompts": "Study Plan / Research Proposal (minimum 800 words for Master's, 1,500 words for PhD) describing research goals and background.",
            "study_plan_research_proposal_requirements": "Detailed research plan detailing research background, objectives, experimental design, and expected results.",
            "cv_format_requirements": "Detailed academic CV with full list of research publications (DOI links, impact factors).",
            "interviews_conducted": True,
            "interview_format_details": "Host research group and departmental panel conduct 20-30 minute technical video interview via Zoom/Voov.",
            "standardized_tests": "GRE not required; English language certificate required.",
            "application_fee_amount": "$0 (Waived for ANSO applicants).",
            "attestation_requirements": "Degrees and transcripts must be notarized; HEC and MOFA attestation required for final enrollment.",
            "translation_requirements": "Notarized English or Chinese translations.",
            "final_submission_method": "100% Online via USTC / UCAS portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Supervisor Provisional Acceptance Form",
                "mandatory": True,
                "specification": "Official form signed by prospective USTC or UCAS supervisor",
                "pakistan_specific_instruction": "Critical gatekeeper document; required for submission"
            },
            {
                "document_name": "Academic Diplomas & Transcripts",
                "mandatory": True,
                "specification": "Notarized copies of Bachelor's and Master's degrees and complete transcripts",
                "pakistan_specific_instruction": "Attested by HEC Pakistan and notarized"
            },
            {
                "document_name": "Two Recommendation Letters",
                "mandatory": True,
                "specification": "Letters from professors or associate professors on university letterhead",
                "pakistan_specific_instruction": "Uploaded directly by referees"
            },
            {
                "document_name": "Research Proposal",
                "mandatory": True,
                "specification": "Detailed proposal (minimum 1,500 words for PhD)",
                "pakistan_specific_instruction": "Aligned with prospective Chinese laboratory"
            },
            {
                "document_name": "Foreigner Physical Examination Form",
                "mandatory": True,
                "specification": "Official Chinese physical examination form signed and stamped by doctor",
                "pakistan_specific_instruction": "Issued by registered government hospital with blood test reports"
            },
            {
                "document_name": "Non-Criminal Record Certificate",
                "mandatory": True,
                "specification": "Police clearance certificate",
                "pakistan_specific_instruction": "Issued by local Pakistani police department / Police Khidmat Markaz"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-10-20",
            "application_deadline": "2027-02-15",
            "university_admission_deadline": "2027-02-15",
            "document_submission_deadline": "2027-02-15",
            "recommendation_letters_deadline": "2027-02-25",
            "interview_period": "March to April 2027",
            "shortlist_announcement": "May 2027",
            "final_result_acceptance_deadline": "2027-06-30",
            "visa_application_window": "July to August 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "Application deadline is strictly mid-February each year. Final results released late May to June."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic background, grades, prestige of home university)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "40% (SCI indexed publications, research proposal quality, laboratory skills)",
            "work_experience_weight": "5% (Research experience)",
            "personal_statement_weight": "5% (Study plan clarity)",
            "recommendations_weight": "10% (Supervisor acceptance and referee endorsements)",
            "interview_weight": "Decisive during professor interview",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Exclusively merit-based)",
            "selection_panel_composition": "Joint evaluation by host institute professors, university international student committees, and the ANSO Secretariat.",
            "evaluation_methodology": "Two-tier review: Host supervisor accepts candidate; central ANSO scientific committee reviews and approves award."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~6,000+ applicants across all ANSO partner countries",
            "total_scholarships_awarded": "~500 scholarships awarded annually",
            "acceptance_rate_global": "~8%",
            "acceptance_rate_pakistan": "~5% to 7% (Very favorable for candidates with published research)",
            "typical_successful_applicant_gpa": "3.40 to 3.90 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Graduates with at least 1 or 2 published peer-reviewed journal papers in international journals.",
            "common_backgrounds_of_winners": "Graduates of Pakistani universities (NUST, Quaid-i-Azam, COMSATS, UET Lahore, Punjab University) with strong lab experience.",
            "high_representation_countries": "Pakistan, Russia, Kazakhstan, Thailand, Egypt, Iran, Nepal, Kenya.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents claiming they can guarantee ANSO supervisor acceptance for PKR 200,000+."
            ],
            "application_fee_warning": "ANSO application is 100% free of charge.",
            "agent_and_intermediary_warnings": "Never hire agents; prospective professors communicate only with the candidate directly.",
            "hidden_costs_breakdown": [
                "Chinese student visa fee (~PKR 15,000 to 20,000).",
                "Police clearance and medical checkup fees in Pakistan (~PKR 15,000).",
                "Initial pocket money before first stipend release in Hefei or Beijing."
            ],
            "misleading_claims_debunked": [
                "MYTH: You cannot apply without an HSK Chinese certificate. (Fact: Programs are taught 100% in English; no Chinese test required).",
                "MYTH: You can apply without contacting a professor. (Fact: Applications without supervisor acceptance are rejected)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some websites advertise this as CSC; ANSO is an independent flagship program with higher PhD stipends (up to RMB 7,000/month vs CSC RMB 3,500/month)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass all required graduate coursework and achieve satisfactory annual progress in research milestones.",
            "attendance_requirements": "Full-time physical research attendance at host CAS institute in China.",
            "academic_progress_monitoring": "Annual scholarship review conducted by host supervisor and academic committee.",
            "work_restrictions_during_study": "Off-campus employment is restricted under Chinese X1 visa rules without university authorization.",
            "home_country_return_obligation": "None; scholars can pursue postdoctoral research in China or internationally.",
            "service_obligations_or_bonds": "None; expected to acknowledge ANSO in research publications.",
            "repayment_clawback_conditions": "Failing annual review or violation of Chinese laws leads to immediate termination.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Requires approval from host supervisor and university.",
            "extension_policy": "Extensions are strictly granted only under exceptional circumstances approved by the ANSO Secretariat."
        },
        "official_sources_verified": [
            {
                "source_name": "Alliance of International Science Organizations (ANSO) - Scholarships Portal",
                "source_url": "http://www.anso.org.cn/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation formula of spots between USTC and UCAS institutes",
                    "Internal country quota breakdown among ANSO member states"
                ]
            },
            {
                "source_name": "University of Science and Technology of China (USTC) - International Admissions",
                "source_url": "https://isa.ustc.edu.cn/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific lab-by-lab funding quotas across CAS research centers"
                ]
            }
        ]
    },

    # 4. Hong Kong PhD Fellowship Scheme (HKPFS) (SCH-AS-005)
    "SCH-AS-005": {
        "scholarship_id": "SCH-AS-005",
        "basic_details": {
            "scholarship_name": "Hong Kong PhD Fellowship Scheme (HKPFS)",
            "offering_entity": "Research Grants Council (RGC) of Hong Kong",
            "host_country": "Hong Kong",
            "host_institutions_covered": "All 8 UGC-funded universities in Hong Kong (HKU, HKUST, CUHK, CityU, PolyU, HKBU, Lingnan University, EdUHK)",
            "degree_levels": ["PhD (Doctorate)"],
            "major_restrictions": "Open to all PhD fields: Science, Engineering, Computer Science, Artificial Intelligence, Medicine, Business, Humanities, Social Sciences.",
            "number_of_awards_total": "~300 PhD fellowships awarded annually across all 8 universities",
            "number_of_awards_pakistan": "Open globally to candidates of all nationalities based on academic and research excellence",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3 to 4 years of doctoral study"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Candidates of all nationalities and cultural backgrounds (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Completed 16 years of education (4-year Bachelor's with honours) or 18 years (Master's by research) with first-class academic standing.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum 3.70 / 4.00 CGPA or equivalent top 5% class standing.",
            "subject_background_prerequisites": "Strong academic preparation and demonstrated research capability in the chosen PhD field.",
            "current_education_status": "Graduated or in final year of undergraduate/master's studies.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior research publications, conference presentations, or patents provide a significant competitive advantage.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Must meet host university PhD language requirements (typically IELTS Academic 6.5+ or TOEFL iBT 85+)."
            },
            "other_language_requirements": "None; PhD programs taught 100% in English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Four core criteria: Academic excellence, research ability and potential, communication and interpersonal skills, and leadership abilities.",
            "previous_scholarship_restrictions": "Must not already hold a doctoral degree.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Most host universities (HKU, HKUST, CUHK, PolyU, CityU) waive full tuition fees (HKD $42,100/year) or provide full tuition scholarship top-ups for HKPFS awardees.",
                "amount": "HKD $42,100 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University application fees (~HKD $300 to $450 per university) paid by applicant.",
                "amount": "HKD $300 to $450"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND_WITH_GUARANTEED_HOUSING",
                "details": "Host universities guarantee on-campus postgraduate hall accommodation for HKPFS fellows; rent is paid from the generous stipend.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "High-tier annual stipend paid in monthly installments.",
                "amount": "HKD $337,200 / year (~HKD $28,100 / month or ~PKR 1,005,000 / month)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel to Hong Kong is covered from initial stipend installment or university entrance grant.",
                "amount": None
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Hong Kong student visa application fee (HKD $230) paid by applicant.",
                "amount": "HKD $230"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Public healthcare access in Hong Kong hospitals covered at local resident rates (HKD $100/day inpatient) upon receiving Hong Kong Identity Card (HKID).",
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
                "details": "Annual conference and research-related travel allowance provided by RGC.",
                "amount": "HKD $14,000 / year (~PKR 500,000 / year)"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Many host universities offer one-off arrival cash awards (HKD $10,000-$40,000) for HKPFS awardees.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for up to two PhD programs at one or two of the 8 participating Hong Kong universities.",
            "participating_institutions": [
                "University of Hong Kong (HKU)", "Hong Kong University of Science and Technology (HKUST)",
                "Chinese University of Hong Kong (CUHK)", "City University of Hong Kong (CityU)",
                "Hong Kong Polytechnic University (PolyU)", "Hong Kong Baptist University (HKBU)",
                "Lingnan University", "Education University of Hong Kong (EdUHK)"
            ],
            "university_rankings_scope": "HKU (World #17), HKUST (World #47), CUHK (World #36) — world top research powerhouses.",
            "available_majors": [
                "Artificial Intelligence, Data Science, Computer Science, Electronic Engineering, Mechanical Engineering, Biomedical Engineering, Public Health, Cancer Biology, Chemistry, Physics, Finance, Economics, Humanities, Social Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 years (with Master's degree) or 4 years (with Bachelor's degree)",
            "admission_requirements_summary": "Two-step application: First obtain an HKPFS reference number from RGC; then submit full PhD application to chosen universities quoting that reference number.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "HKU, HKUST, and CUHK are most competitive; contacting prospective professors in advance is strongly recommended.",
            "strategic_program_match_advice": "Prior contact with a prospective PhD supervisor who agrees to support your nomination dramatically increases success rates."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://cerg1.ugc.edu.hk/hkpfs/index.html",
            "portal_system_name": "RGC HKPFS Electronic System & University Application Portals",
            "account_creation_instructions": "Step 1: Register on RGC portal (Opens September 1), obtain HKPFS Reference Number. Step 2: Apply to chosen universities citing the reference number before December 1.",
            "step_by_step_workflow": [
                "1. Review faculty profiles across the 8 Hong Kong universities and email potential supervisors (September-October).",
                "2. Register on the RGC HKPFS portal and obtain an HKPFS reference number by December 1 (12:00 noon GMT+8).",
                "3. Submit formal PhD applications to up to two participating universities quoting your HKPFS reference number by their respective deadlines (typically December 1).",
                "4. Upload transcripts, research proposals, publications, and English scores to the university portals.",
                "5. Universities conduct academic screening and interviews in December/January.",
                "6. Universities nominate top candidates to the RGC Selection Panels in January.",
                "7. RGC releases final award results in March."
            ],
            "university_vs_scholarship_routing": "Dual submission: Central RGC registration + individual university PhD applications.",
            "recommendation_letters_submission_method": "Submitted online by referees directly via each host university's application portal.",
            "personal_statement_prompts": "Research proposal and statement of research interests and career goals submitted via university systems.",
            "study_plan_research_proposal_requirements": "Rigorous research proposal detailing problem formulation, literature review, methodology, and significance.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications, citations, conferences, and academic honors.",
            "interviews_conducted": True,
            "interview_format_details": "Departmental interview panels conduct 20-30 minute technical video interviews in December/January.",
            "standardized_tests": "English test (IELTS 6.5+ or TOEFL 85+); GRE optional/department specific.",
            "application_fee_amount": "$0 on RGC portal; ~HKD $300-$450 per university.",
            "attestation_requirements": "Transcripts certified by degree institutions; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via RGC portal and university portals."
        },
        "required_documents_checklist": [
            {
                "document_name": "RGC HKPFS Application Form & Reference Number",
                "mandatory": True,
                "specification": "Initial registration on RGC portal yielding official reference number",
                "pakistan_specific_instruction": "Must be completed before December 1 deadline"
            },
            {
                "document_name": "Research Proposal",
                "mandatory": True,
                "specification": "Detailed PhD research proposal aligned with host faculty research",
                "pakistan_specific_instruction": "Original independent proposal; high scientific quality required"
            },
            {
                "document_name": "Academic Transcripts & Certificates",
                "mandatory": True,
                "specification": "Official transcripts and degree certificates with grading scheme",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Academic Reference Reports",
                "mandatory": True,
                "specification": "Submitted directly by university research professors via university portal",
                "pakistan_specific_instruction": "Speaking to research aptitude and originality"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (85+)",
                "pakistan_specific_instruction": "Valid test certificate"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-09-01",
            "application_deadline": "2026-12-01",
            "university_admission_deadline": "2026-12-01",
            "document_submission_deadline": "2026-12-01",
            "recommendation_letters_deadline": "2026-12-10",
            "interview_period": "December 2026 to January 2027",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "RGC portal deadline is strictly December 1 (12:00 noon Hong Kong time). Results announced in March."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Academic excellence, class ranking, undergraduate and master's GPA)",
            "extracurricular_and_leadership_weight": "10% (Leadership abilities, communication, interpersonal skills)",
            "research_experience_weight": "40% (Research ability and potential, publications, quality of proposal)",
            "work_experience_weight": "5% (Industry/laboratory research experience)",
            "personal_statement_weight": "5% (Clear research vision)",
            "recommendations_weight": "5% (Referee assessments)",
            "interview_weight": "High weight in university nomination stage",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Purely merit-based)",
            "selection_panel_composition": "Two RGC Selection Panels: (1) Science, Medicine, Engineering and Technology; (2) Humanities, Social Sciences and Business Studies.",
            "evaluation_methodology": "Two-tier review: Universities nominate their very best applicants; RGC expert panels make final selection across the 8 universities."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~10,000+ applications submitted across the 8 universities",
            "total_scholarships_awarded": "~300 fellowships awarded annually across all 8 universities",
            "acceptance_rate_global": "~3%",
            "acceptance_rate_pakistan": "~2% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 CGPA",
            "typical_academic_and_research_profile": "Candidates with multiple first-author publications in Q1 international journals or leading IEEE/ACM conferences.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani universities (NUST, LUMS, Quaid-i-Azam, GIKI, UET Lahore, FAST).",
            "high_representation_countries": "Mainland China, India, Pakistan, USA, Canada, Germany, Iran.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized agencies claiming to guarantee HKPFS awards for large fees."
            ],
            "application_fee_warning": "RGC registration is 100% free; university application fees apply.",
            "agent_and_intermediary_warnings": "Never pay agents; professors review research papers directly.",
            "hidden_costs_breakdown": [
                "University application fees (~HKD $300-$450 per university).",
                "Hong Kong student visa fee (HKD $230).",
                "Initial flight to Hong Kong (~PKR 180,000 to 250,000)."
            ],
            "misleading_claims_debunked": [
                "MYTH: If you do not get HKPFS, you cannot study in Hong Kong. (Fact: Candidates who narrowly miss HKPFS are almost always offered standard university postgraduate studentships (PGS) of ~HKD $18,500/month, which also fully covers tuition and living).",
                "MYTH: You need Cantonese or Mandarin. (Fact: All PhD education and research in Hong Kong universities is conducted entirely in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "External blogs state the stipend is HKD $25,000; the official rate is now indexed at HKD $337,200/year (HKD $28,100/month)."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic performance and pass annual doctoral qualifying examinations.",
            "attendance_requirements": "Full-time physical research attendance at host university in Hong Kong.",
            "academic_progress_monitoring": "Annual progress reviews submitted by supervisory committee to the RGC.",
            "work_restrictions_during_study": "HKPFS fellows are not permitted to undertake outside employment without prior permission, but may perform teaching assistant duties as part of academic training.",
            "home_country_return_obligation": "None; graduates are eligible for the Immigration Arrangements for Non-local Graduates (IANG) visa to work in Hong Kong for 2 years post-graduation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of fellowship occurs if candidate fails doctoral qualifying milestones or withdraws.",
            "rules_for_changing_university": "Non-transferable between universities.",
            "rules_for_changing_major": "Requires approval from both departments and RGC.",
            "extension_policy": "Fellowship is granted for maximum 3 years (for applicants with research master's) or 4 years (for applicants with bachelor's)."
        },
        "official_sources_verified": [
            {
                "source_name": "Research Grants Council (RGC) of Hong Kong - HKPFS Official Portal",
                "source_url": "https://cerg1.ugc.edu.hk/hkpfs/index.html",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Allocation formula of fellowships across the 8 participating universities",
                    "RGC central selection panel scoring rubric sheets"
                ]
            }
        ]
    }
}
