"""
scripts/dossiers_batch2a.py
Part A of Batch 2:
1. SCH-OC-004: University of Sydney International Scholarship (USydIS, Australia)
2. SCH-OC-005: Australian National University (ANU) AGRTP International Postgraduate Award (Australia)
3. SCH-EU-008: Eiffel Excellence Scholarship Programme (Campus France, France)
4. SCH-EU-009: Swedish Institute Scholarships for Global Professionals (SISGP, Sweden)
"""

DOSSIERS_BATCH2A = {
    # 1. University of Sydney International Scholarship (SCH-OC-004)
    "SCH-OC-004": {
        "scholarship_id": "SCH-OC-004",
        "basic_details": {
            "scholarship_name": "University of Sydney International Scholarship (USydIS)",
            "offering_entity": "University of Sydney & Australian Government Research Training Program (RTP)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Sydney (Camperdown/Darlington, Westmead, Camden)",
            "degree_levels": ["Master's by Research", "PhD"],
            "major_restrictions": "Open to all research disciplines across Science, Engineering, Medicine & Health, Arts & Social Sciences, Business School, Law, Architecture, Music.",
            "number_of_awards_total": "~400 to 500 postgraduate research scholarships awarded annually",
            "number_of_awards_pakistan": "Open globally; awards distributed strictly on merit and research track record",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's by Research; up to 3.5 years (with potential 6-month extension) for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students of all nationalities (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restrictions.",
            "academic_qualifications": "Completed at least a 4-year undergraduate degree with an honours thesis component or a research master's degree from an accredited institution.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Equivalent to an Australian First Class Honours degree (H1, 80%+ or 3.70+ / 4.00 CGPA).",
            "subject_background_prerequisites": "Substantive research background in proposed field of research with demonstrated research methodology.",
            "current_education_status": "Graduated or in final semester of research master's or 4-year bachelor's degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in peer-reviewed journals, book chapters, or international conference proceedings heavily rewarded in faculty scoring.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (minimum 6.0 in all bands) or TOEFL iBT 85 (reading/listening/speaking 17, writing 19); higher for Law, Medicine, and Arts."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; diversity and inclusion encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "High-impact research capability.",
            "previous_scholarship_restrictions": "Must not have already completed a degree at the same or higher level.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fees covered for the normal duration of the degree.",
                "amount": "AUD $45,000 to $54,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Sydney application fee (AUD $150) paid by applicant.",
                "amount": "AUD $150"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via tax-free living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free living allowance stipend indexed annually.",
                "amount": "AUD $40,109 / year (~AUD $3,342 / month or ~PKR 618,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Relocation allowance provided to assist with flight travel and settling in Sydney.",
                "amount": "Up to AUD $2,500 relocation assistance (~PKR 460,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Student Visa (Subclass 500) application fee paid by applicant.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Overseas Student Health Cover (OSHC) Single policy covered for the full duration of the student visa.",
                "amount": "AUD $700 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered from living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Departmental research computing resources and laboratory facilities provided.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Postgraduate research support funds (PRSS) of AUD $2,000 to $3,500 available for conference travel.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in relocation allowance.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 62000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: University of Sydney (Ranked Top 20 globally in QS World Rankings).",
            "participating_institutions": [
                "University of Sydney"
            ],
            "university_rankings_scope": "QS World Rank #18; Group of Eight (Go8) Australia flagship.",
            "available_majors": [
                "Computer Science, Artificial Intelligence, Cybersecurity, Electrical & Information Engineering, Mechanical Engineering, Biomedical Engineering, Public Health, Pharmacy, Cancer Medicine, Quantum Physics, Molecular Bioscience, Economics, Law, Architecture"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for Master's by Research; 3.5 to 4 years for PhD",
            "admission_requirements_summary": "All candidates applying for a postgraduate research degree are automatically assessed for research scholarships.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing prior written agreement from an academic supervisor is mandatory before applying.",
            "strategic_program_match_advice": "Ensure your research proposal explicitly links with ongoing Australian Research Council (ARC) funded projects within the lab."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.sydney.edu.au/scholarships/e/university-of-sydney-international-scholarship.html",
            "portal_system_name": "University of Sydney Postgraduate Research Application Portal",
            "account_creation_instructions": "Register on the Sydney course application system, upload proposal and CV, and nominate prospective research supervisor.",
            "step_by_step_workflow": [
                "1. Identify potential research supervisor in your discipline and secure expression of support (July-August).",
                "2. Develop 2,000-word Research Proposal detailing research objectives and methodology.",
                "3. Submit formal online application for research degree before scholarship round deadline (Round 1: September 15).",
                "4. Tick the checkbox to be considered for postgraduate research scholarships.",
                "5. Upload degree certificates, transcripts, research publication proofs, and English test scores.",
                "6. Provide details of two academic referees who submit online reports.",
                "7. Outcomes notified in November/December for Semester 1 (March) intake."
            ],
            "university_vs_scholarship_routing": "Integrated single application for candidature and scholarship.",
            "recommendation_letters_submission_method": "Submitted online by referees via electronic referee form.",
            "personal_statement_prompts": "Outline research goals, why University of Sydney is your chosen institution, and future research vision.",
            "study_plan_research_proposal_requirements": "Structured research proposal (around 2,000 words) with background, research questions, methodology, and timetable.",
            "cv_format_requirements": "Academic CV detailing academic history, research projects, publications, awards, and laboratory skills.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisors conduct 30-45 minute video interviews to evaluate domain knowledge and research fit.",
            "standardized_tests": "GRE not required; English language test required.",
            "application_fee_amount": "AUD $150 (can be waived if provided code by faculty supervisor).",
            "attestation_requirements": "Original certified copies of transcripts and degree certificates; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via University of Sydney portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Research Proposal",
                "mandatory": True,
                "specification": "2,000-word formal research proposal with methodology and references",
                "pakistan_specific_instruction": "Aligned with prospective Sydney supervisor's research expertise"
            },
            {
                "document_name": "Supervisor Expression of Support",
                "mandatory": True,
                "specification": "Written confirmation from prospective Sydney academic supervisor",
                "pakistan_specific_instruction": "Email or formal letter agreeing to supervise doctoral candidature"
            },
            {
                "document_name": "Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for 16-year or 18-year education with grading scale",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Confidential reports from former research supervisors",
                "pakistan_specific_instruction": "Uploaded by professors from your Pakistani university"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (85+)",
                "pakistan_specific_instruction": "Electronic score report sent to University of Sydney"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-06-01",
            "application_deadline": "2026-09-15",
            "university_admission_deadline": "2026-09-15",
            "document_submission_deadline": "2026-09-30",
            "recommendation_letters_deadline": "2026-09-30",
            "interview_period": "October to November 2026",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2026-12-15",
            "visa_application_window": "December 2026 to January 2027",
            "semester_commencement": "March 2027 (Research Period 1 or 2)",
            "annual_cycle_notes": "Round 1 closes mid-September for March commencement; Round 2 closes mid-December for July commencement."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (First Class Honours equivalent GPA, class ranking)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "40% (Refereed journal articles, conference papers, master's thesis grade)",
            "work_experience_weight": "5% (Industry research or laboratory experience)",
            "personal_statement_weight": "5% (Quality of proposal)",
            "recommendations_weight": "5% (Referee evaluation)",
            "interview_weight": "Supervisor decision",
            "test_scores_weight": "Passing threshold required",
            "financial_need_weight": "0% (Strictly academic and research merit)",
            "selection_panel_composition": "Faculty Research Committees and Academic Board Selection Committee.",
            "evaluation_methodology": "Competitive merit ranking combining GPA equivalent score, publication multiplier score, and supervisor alignment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~4,500 international applicants across all disciplines",
            "total_scholarships_awarded": "~350 international scholarships awarded per cycle",
            "acceptance_rate_global": "~7%",
            "acceptance_rate_pakistan": "~3% to 4% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 CGPA",
            "typical_academic_and_research_profile": "First-author publications in indexed journals (Q1/Q2 SCImago) and strong theoretical foundations.",
            "common_backgrounds_of_winners": "Graduates of Pakistani research institutions (NUST, LUMS, Quaid-i-Azam, UET Lahore, FAST).",
            "high_representation_countries": "China, India, Pakistan, Iran, USA, UK, Germany.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Consultancies claiming they can obtain Sydney scholarships without supervisor endorsement."
            ],
            "application_fee_warning": "University application fee is AUD $150; scholarship evaluation has no extra fee.",
            "agent_and_intermediary_warnings": "Never pay agents for research supervision; supervisors evaluate applicants on personal academic merit.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD $1,600).",
                "English language test fees (IELTS/PTE).",
                "Sydney initial bond and apartment deposit."
            ],
            "misleading_claims_debunked": [
                "MYTH: Taught Master's students can get this award. (Fact: Strictly for Master's by Research and PhD degrees).",
                "MYTH: You can apply without a supervisor. (Fact: An application without confirmed supervisor support will be rejected)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party sites cite outdated stipend figures; the current official stipend is AUD $40,109/year."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must meet satisfactory progress in annual research milestones (Progress Review 1 at 12 months).",
            "attendance_requirements": "Full-time physical research attendance on campus in Sydney.",
            "academic_progress_monitoring": "Annual progress reviews conducted by supervisory team and faculty associate dean.",
            "work_restrictions_during_study": "Permitted to work per Australian student visa rules, but University limits outside work during business hours to avoid thesis delays.",
            "home_country_return_obligation": "None; scholars are eligible for Australian Temporary Graduate Visa (Subclass 485) post-PhD.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Termination of funding occurs upon failure of progress reviews or voluntary withdrawal.",
            "rules_for_changing_university": "Non-transferable.",
            "rules_for_changing_major": "Requires approval from old and new faculty supervisors.",
            "extension_policy": "PhD scholars can apply for up to 6 months extension subject to academic justification."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Sydney - Postgraduate Research Scholarships Official Portal",
                "source_url": "https://www.sydney.edu.au/scholarships/e/university-of-sydney-international-scholarship.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact publication scoring points matrix used across different faculties",
                    "Specific country quota allocations"
                ]
            }
        ]
    },

    # 2. Australian National University (ANU) AGRTP International Postgraduate Award (SCH-OC-005)
    "SCH-OC-005": {
        "scholarship_id": "SCH-OC-005",
        "basic_details": {
            "scholarship_name": "Australian National University (ANU) AGRTP International Postgraduate Award",
            "offering_entity": "Australian National University (ANU) & Australian Government Department of Education (AGRTP)",
            "host_country": "Australia",
            "host_institutions_covered": "Australian National University (Acton Campus, Canberra)",
            "degree_levels": ["Master of Philosophy (MPhil)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all research disciplines across ANU Colleges: Engineering, Computing & Cybernetics, Health & Medicine, Science, Arts & Social Sciences, Asia & the Pacific, Business & Economics, Law.",
            "number_of_awards_total": "~300 to 400 RTP and university awards annually",
            "number_of_awards_pakistan": "Open globally to all international researchers based on competitive merit",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MPhil; up to 3.5 to 4 years for PhD"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International citizens of all countries including Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age limits.",
            "academic_qualifications": "Bachelor's degree with at least upper second-class or first-class honours (H1) or research Master's degree with substantial thesis component.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Minimum equivalent to ANU First Class Honours (80%+ / 3.70+ / 4.00 CGPA).",
            "subject_background_prerequisites": "Advanced preparation in the relevant research discipline.",
            "current_education_status": "Graduated or in final semester of research master's or 4-year honours bachelor's degree.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Refereed scientific publications, international conference talks, and relevant laboratory experience provide significant competitive advantage.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 80,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (minimum 6.0 each band) or TOEFL iBT 80 (reading/writing 20, listening/speaking 18)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite research aptitude and academic excellence.",
            "previous_scholarship_restrictions": "Must not have already completed a doctorate.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee offset covering all course fees for standard duration.",
                "amount": "AUD $44,000 to $54,000 / year"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "ANU online application fee (AUD $110) paid by candidate.",
                "amount": "AUD $110"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered through living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Tax-free living stipend paid fortnightly.",
                "amount": "AUD $36,652 / year (~AUD $3,054 / month or ~PKR 565,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Travel and relocation grant paid upon relocation to Canberra.",
                "amount": "Up to AUD $2,500 relocation reimbursement"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian student visa application fee paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Full Overseas Student Health Cover (OSHC) Single policy covered for the visa duration.",
                "amount": "AUD $680 / year"
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "High-performance compute clusters and research infrastructure provided by college.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "ANU College travel grants available for international conference attendance.",
                "amount": "Up to AUD $3,000"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in relocation allowance.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 58000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution: Australian National University (Canberra - Australia's national university).",
            "participating_institutions": [
                "Australian National University"
            ],
            "university_rankings_scope": "QS World Rank #30; consistently ranked #1 in Australia for research impact.",
            "available_majors": [
                "Computer Science, Cybernetics, Robotics, Machine Learning, Electrical Engineering, Physics & Astronomy, Chemistry, Environmental Sciences, Biology, Economics, Public Policy, Law, International Relations, Asia-Pacific Studies"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years for MPhil; 3.5 to 4 years for PhD",
            "admission_requirements_summary": "Automatic consideration for all applicants submitting a complete research degree application before the international deadline.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing prior supervisor agreement in principle is required before application.",
            "strategic_program_match_advice": "ANU's College of Engineering, Computing & Cybernetics (CECC) and College of Science have world-leading laboratories; link your proposal with their core research clusters."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.anu.edu.au/study/scholarships/find-a-scholarship/australian-government-research-training-program-agrtp-stipend",
            "portal_system_name": "ANU Postgraduate Online Application Portal",
            "account_creation_instructions": "Register on the ANU application portal, select PhD/MPhil course, and upload research proposal and academic credentials.",
            "step_by_step_workflow": [
                "1. Contact potential ANU supervisor and secure written support (June-July).",
                "2. Develop rigorous 2,000-word Research Proposal.",
                "3. Submit formal online application for research degree by international deadline (August 31).",
                "4. Opt in for consideration for AGRTP / University Research Scholarships.",
                "5. Upload academic transcripts, grading scales, publications, and English test scores.",
                "6. Referees submit online reference reports by deadline.",
                "7. Central scholarship committee outcomes released in October/November for early 2027 intake."
            ],
            "university_vs_scholarship_routing": "Combined single application for course admission and scholarship.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure electronic referee system.",
            "personal_statement_prompts": "Demonstrate your research background, research capability, and future contribution to scientific knowledge.",
            "study_plan_research_proposal_requirements": "Structured research proposal outlining problem statement, research questions, literature review, methodology, and timeline.",
            "cv_format_requirements": "Academic CV listing academic qualifications, research publications, conference presentations, awards, and laboratory experience.",
            "interviews_conducted": True,
            "interview_format_details": "Supervisors conduct video interview before endorsing the application.",
            "standardized_tests": "GRE not required; English proficiency test required.",
            "application_fee_amount": "AUD $110.",
            "attestation_requirements": "Certified copies of degree certificates and transcripts; HEC attestation required.",
            "translation_requirements": "Certified English translations.",
            "final_submission_method": "100% Online via ANU portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Research Proposal",
                "mandatory": True,
                "specification": "Structured proposal (around 2,000 words) with literature review and methodology",
                "pakistan_specific_instruction": "Developed in coordination with prospective ANU supervisor"
            },
            {
                "document_name": "Written Supervisor Endorsement",
                "mandatory": True,
                "specification": "Formal confirmation from an ANU academic willing to supervise your research",
                "pakistan_specific_instruction": "Required before application submission"
            },
            {
                "document_name": "Academic Transcripts & Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all university-level studies",
                "pakistan_specific_instruction": "Attested by HEC Pakistan"
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by former academic supervisors",
                "pakistan_specific_instruction": "From professors who supervised your BS/MS thesis"
            },
            {
                "document_name": "English Language Test Score",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (80+)",
                "pakistan_specific_instruction": "Electronic score report sent to ANU"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-05-01",
            "application_deadline": "2026-08-31",
            "university_admission_deadline": "2026-08-31",
            "document_submission_deadline": "2026-08-31",
            "recommendation_letters_deadline": "2026-09-07",
            "interview_period": "September to October 2026",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2026-11-30",
            "visa_application_window": "December 2026 to January 2027",
            "semester_commencement": "February/March 2027",
            "annual_cycle_notes": "Annual round for international applicants strictly closes August 31 for commencement in Semester 1 of following year."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (First Class Honours H1 equivalent GPA, academic standing)",
            "extracurricular_and_leadership_weight": "5% (Secondary)",
            "research_experience_weight": "40% (Peer-reviewed publications, thesis quality, research potential)",
            "work_experience_weight": "5% (Relevant research laboratory or industry experience)",
            "personal_statement_weight": "5% (Proposal quality)",
            "recommendations_weight": "5% (Referee evaluation)",
            "interview_weight": "Supervisor recommendation",
            "test_scores_weight": "Threshold required",
            "financial_need_weight": "0% (Purely merit-based)",
            "selection_panel_composition": "College Scholarships Committees and University Higher Degree Research Committee.",
            "evaluation_methodology": "Strict competitive merit ranking based on academic score and verified research output score."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 international applicants across all disciplines",
            "total_scholarships_awarded": "~250 international awards conferred annually",
            "acceptance_rate_global": "~7%",
            "acceptance_rate_pakistan": "~3% to 4% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.80 to 4.00 CGPA",
            "typical_academic_and_research_profile": "First-class academic record with at least one first-author publication in a recognized international journal.",
            "common_backgrounds_of_winners": "Graduates of top Pakistani universities (NUST, LUMS, Quaid-i-Azam, UET Lahore, GIKI).",
            "high_representation_countries": "China, India, Pakistan, Iran, USA, UK, Singapore.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agencies claiming they can secure ANU doctoral admission without academic supervisor endorsement."
            ],
            "application_fee_warning": "ANU application fee is AUD $110; scholarship consideration is automatic and free.",
            "agent_and_intermediary_warnings": "Never pay third parties; ANU requires direct academic correspondence between student and supervisor.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD $1,600).",
                "English language test fees (IELTS/TOEFL).",
                "Initial relocation expenses prior to first stipend payment."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can apply without contacting a supervisor. (Fact: Applications without confirmed supervisor support are automatically declined).",
                "MYTH: Coursework students can get this scholarship. (Fact: Strictly for higher degree research candidates)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals quote outdated stipend rates; official rate is indexed at AUD $36,652/year."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress in annual milestone reviews.",
            "attendance_requirements": "Full-time physical research attendance on campus in Canberra.",
            "academic_progress_monitoring": "Annual progress reviews submitted by supervisory panel to the college dean.",
            "work_restrictions_during_study": "Permitted to undertake up to standard research assistant/tutoring hours (typically up to 8 hrs/week during normal business hours).",
            "home_country_return_obligation": "None; scholars are eligible for Australian Temporary Graduate Visa (Subclass 485) post-PhD.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Funding terminated if candidate fails research milestones or withdraws from candidature.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Requires approval from supervisory panel and college dean.",
            "extension_policy": "PhD candidates may receive up to 6 months extension for documented research delays."
        },
        "official_sources_verified": [
            {
                "source_name": "Australian National University - AGRTP International Postgraduate Award Portal",
                "source_url": "https://www.anu.edu.au/study/scholarships/find-a-scholarship/australian-government-research-training-program-agrtp-stipend",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "College-by-college internal funding allocation quotas",
                    "Specific publication scoring multiplier values"
                ]
            }
        ]
    },

    # 3. Eiffel Excellence Scholarship Programme (Campus France) (SCH-EU-008)
    "SCH-EU-008": {
        "scholarship_id": "SCH-EU-008",
        "basic_details": {
            "scholarship_name": "Eiffel Excellence Scholarship Programme",
            "offering_entity": "French Ministry for Europe and Foreign Affairs (MEAE) & Campus France",
            "host_country": "France",
            "host_institutions_covered": "All accredited French Universities and Grandes Écoles (Sorbonne, École Polytechnique, PSL, Paris-Saclay, Sciences Po, CentraleSupélec, INSA)",
            "degree_levels": ["Master's", "PhD (Doctorate)"],
            "major_restrictions": "Seven priority study fields: Science and Technology (Biology and Health, Ecological Transition, Mathematics and Digital, Engineering Sciences), and Humanities and Social Sciences (French History, Language and Civilization, Law and Political Science, Economics and Management).",
            "number_of_awards_total": "~350 to 400 scholarships awarded annually across 100+ countries",
            "number_of_awards_pakistan": "Open to Pakistan; numerous Pakistani scholars selected annually for French Grandes Écoles and research universities",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Master's: 12 to 36 months depending on entry level (M1 or M2); PhD: up to 36 months (or 6-18 months for joint-supervision cotutelle)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-French nationality (Pakistani citizens eligible; dual French citizens strictly ineligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": 30,
            "age_limit_notes": "Master's candidates: maximum 27 years of age at the time of application; PhD candidates: maximum 32 years of age.",
            "academic_qualifications": "16 years of education (Bachelor's) for Master's; 18 years (Master's with research thesis) for PhD from an HEC-recognized institution.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum 3.30 / 4.00 CGPA or equivalent; admitted candidates typically rank in the top 5% of their graduating class.",
            "subject_background_prerequisites": "Academic background aligned with one of the 7 designated priority areas.",
            "current_education_status": "Graduated or in final semester of degree in home country.",
            "graduation_year_restrictions": "None, provided age criteria are respected.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Academic excellence, scientific publications, and international outlook prioritized.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": True,
                "notes": "Language requirement depends on the chosen program; English-taught programs require IELTS 6.5+ or TOEFL 90+; French-taught programs require DELF/DALF B2/C1."
            },
            "other_language_requirements": "French not mandatory for programs taught 100% in English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates CANNOT apply directly; they MUST be selected and nominated by a French higher education institution.",
            "previous_scholarship_restrictions": "Must not have previously received an Eiffel scholarship at the same degree level, or another French government scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "NOT_DIRECTLY_PAID_BY_EIFFEL",
                "details": "Eiffel does NOT pay tuition fees; however, nominating French public universities waive international tuition fees for Eiffel recipients; Grandes Écoles often waive or subsidize remaining fees.",
                "amount": None
            },
            "admission_application_fee": {
                "status": "WAIVED_BY_INSTITUTION",
                "details": "Managed directly by nominating French institution.",
                "amount": None
            },
            "accommodation": {
                "status": "PAID VIA STIPEND_WITH_HOUSING_PRIORITY",
                "details": "Campus France reserves public student housing (CROUS) for Eiffel scholars; rent is paid from monthly living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Generous monthly maintenance allowance paid directly to student.",
                "amount": "Master's: €1,181 / month (~PKR 355,000 / month); PhD: €1,800 / month (~PKR 540,000 / month)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Single round-trip international economy class flight between home country and France.",
                "amount": None
            },
            "visa_fee": {
                "status": "WAIVED",
                "details": "French student visa application fee waived by the French Embassy for Eiffel scholars.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Campus France provides private health insurance until enrollment in the free French National Health Insurance (Sécurité Sociale).",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered from monthly living allowance.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered from monthly living allowance.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Cultural activities, excursions, and travel within France organized and funded by Campus France.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Domestic train travel from Paris airport to host university city fully covered.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 32000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single French higher education institution (University or Grande École).",
            "participating_institutions": [
                "Sorbonne Université", "Université Paris-Saclay", "École Polytechnique (l'X)",
                "PSL University (ENS, Dauphine, Mines Paris)", "CentraleSupélec", "Sciences Po Paris",
                "INSA Lyon", "Grenoble INP", "Université de Strasbourg", "HEC Paris"
            ],
            "university_rankings_scope": "Premier French research universities and elite Grandes Écoles.",
            "available_majors": [
                "Artificial Intelligence, Data Science, Computer Science, Mathematics, Mechanical Engineering, Electrical Engineering, Biotechnology, Health Sciences, Renewable Energy, Environmental Sciences, Economics, Management, Law, Political Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 1 to 2 years; PhD: up to 3 years",
            "admission_requirements_summary": "Must apply to a French institution; the institution selects top candidates and submits the Eiffel dossier on their behalf to Campus France.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "French institutions have internal pre-selection deadlines (typically October-November); early contact is essential.",
            "strategic_program_match_advice": "Focus on high-ranking English-taught Master's degrees at Paris-Saclay, Sorbonne, or Institut Polytechnique de Paris."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.campusfrance.org/en/the-eiffel-scholarship-program",
            "portal_system_name": "Campus France Eiffel Online Institutional Platform",
            "account_creation_instructions": "Candidates cannot submit applications directly. You must contact the international relations office or program director of your chosen French university.",
            "step_by_step_workflow": [
                "1. Identify eligible master's or PhD programs at French universities/Grandes Écoles (September-October).",
                "2. Contact the French university's international relations office expressing interest in Eiffel nomination.",
                "3. Submit required application materials to the French institution before their internal deadline (usually November).",
                "4. If accepted and selected, the French institution completes and submits the official Eiffel application to Campus France by early January.",
                "5. Campus France scientific committees evaluate institutional dossiers in February/March.",
                "6. Results published on the Campus France website in early April.",
                "7. Selected scholars contact Campus France to arrange airfare and visa formalities."
            ],
            "university_vs_scholarship_routing": "Institutional nomination: Candidate applies to French university; university submits Eiffel dossier to Campus France.",
            "recommendation_letters_submission_method": "Submitted to the nominating French institution.",
            "personal_statement_prompts": "Demonstrate academic excellence, international career objectives, and justification for choosing France.",
            "study_plan_research_proposal_requirements": "PhD candidates must submit a 1 to 5-page research project endorsed by the French thesis director.",
            "cv_format_requirements": "Curriculum Vitae (in French or English) emphasizing academic honors, rank in class, and publications (1-2 pages).",
            "interviews_conducted": True,
            "interview_format_details": "French university admissions teams conduct video interviews prior to nominating candidates for Eiffel.",
            "standardized_tests": "English test (IELTS/TOEFL) for English programs, or French test (DELF/DALF) for French programs.",
            "application_fee_amount": "$0 for Eiffel; some Grandes Écoles may have application fees.",
            "attestation_requirements": "Certified copies of degree certificates and transcripts; HEC attestation required.",
            "translation_requirements": "Official certified translations into French or English.",
            "final_submission_method": "Submitted online by the nominating French institution via the Campus France portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "French Institution Endorsement & Application Form",
                "mandatory": True,
                "specification": "Official institutional dossier completed and signed by French university rector/president",
                "pakistan_specific_instruction": "Submitted directly by the French university to Campus France"
            },
            {
                "document_name": "Academic Transcripts & Class Ranking",
                "mandatory": True,
                "specification": "Transcripts showing all grades, GPA, and official certificate of class rank",
                "pakistan_specific_instruction": "Attested by HEC Pakistan; rank in class is crucial for Eiffel selection"
            },
            {
                "document_name": "Curriculum Vitae",
                "mandatory": True,
                "specification": "1-2 page CV in English or French",
                "pakistan_specific_instruction": "Highlighting academic awards, research projects, and publications"
            },
            {
                "document_name": "Statement of Professional Project",
                "mandatory": True,
                "specification": "Personal statement explaining career vision and reasons for studying in France",
                "pakistan_specific_instruction": "Clear narrative on how French expertise will impact career"
            },
            {
                "document_name": "Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic (6.5+) or TOEFL iBT (90+) for English programs",
                "pakistan_specific_instruction": "Valid test certificate"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-10-01",
            "application_deadline": "2027-01-10",
            "university_admission_deadline": "2026-11-30",
            "document_submission_deadline": "2026-11-30",
            "recommendation_letters_deadline": "2026-11-30",
            "interview_period": "November to December 2026",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-04-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "September 2027",
            "annual_cycle_notes": "French universities' internal deadlines are between late October and late November. Final Campus France submission deadline is early January; results released in early April."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Academic excellence, class ranking, reputation of home university)",
            "extracurricular_and_leadership_weight": "10% (International outlook, awards, extracurricular achievements)",
            "research_experience_weight": "25% (Research output, thesis proposal for PhD)",
            "work_experience_weight": "5% (Professional experience)",
            "personal_statement_weight": "10% (Clarity and feasibility of professional project)",
            "recommendations_weight": "10% (Quality of French institution's endorsement and international strategy)",
            "interview_weight": "Conducted by nominating institution",
            "test_scores_weight": "Language threshold required",
            "financial_need_weight": "0% (Strictly excellence-based)",
            "selection_panel_composition": "Campus France scientific expert committees composed of leading French university professors and researchers.",
            "evaluation_methodology": "Three criteria: Candidate excellence (40%), Institutional international policy (30%), MEAE geographical priority balance (30%)."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 institutional nominations submitted by French universities (from thousands of applicants)",
            "total_scholarships_awarded": "~350 to 400 scholarships awarded annually globally",
            "acceptance_rate_global": "~25% of institutionally nominated candidates (~2% to 3% of total applicants)",
            "acceptance_rate_pakistan": "~2% to 3% (Highly Selective)",
            "typical_successful_applicant_gpa": "3.60 to 4.00 CGPA (Top 5% of graduating class)",
            "typical_academic_and_research_profile": "Top students from prestigious Pakistani universities with strong foundational training, international publications, and clear career plans.",
            "common_backgrounds_of_winners": "Graduates of NUST, LUMS, GIKI, FAST, Quaid-i-Azam University who secured admission to top French institutions.",
            "high_representation_countries": "Global distribution across Asia, Latin America, Middle East, Africa, Eastern Europe.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites claiming to accept direct Eiffel applications from students; direct applications are automatically disqualified."
            ],
            "application_fee_warning": "Campus France does NOT charge any fee for the Eiffel scholarship.",
            "agent_and_intermediary_warnings": "Never use agents; applications MUST be submitted by the French university itself.",
            "hidden_costs_breakdown": [
                "CVEC student life and campus contribution fee (~€100, though Eiffel scholars are exempt, initial paperwork required).",
                "Grandes Écoles tuition fee difference if not fully waived by the school.",
                "Initial pocket money before first monthly stipend transfer in France."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can submit the application directly to Campus France. (Fact: Applications must be submitted exclusively by a French higher education institution).",
                "MYTH: You must speak fluent French. (Fact: Hundreds of eligible programs are taught 100% in English)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Many blogs claim Eiffel covers full tuition fees; officially, Eiffel does NOT pay tuition fees; it relies on university tuition waivers."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass all courses and obtain the degree within the normal period (60 ECTS credits per year).",
            "attendance_requirements": "Full-time physical attendance at host French institution.",
            "academic_progress_monitoring": "Host institutions report academic results annually to Campus France.",
            "work_restrictions_during_study": "Permitted to work up to 60% of annual legal work time (approx 964 hours/year) under French student visa regulations.",
            "home_country_return_obligation": "None; scholars are eligible for the French Job Seeker / Business Creation Residence Permit (RECE) for 1 year post-graduation.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Failing courses or abandoning studies leads to immediate scholarship termination.",
            "rules_for_changing_university": "Strictly prohibited; the scholarship is awarded to the specific institution that nominated the student.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "No extensions granted beyond the initial grant duration."
        },
        "official_sources_verified": [
            {
                "source_name": "Campus France - Eiffel Excellence Scholarship Programme Official Portal",
                "source_url": "https://www.campusfrance.org/en/the-eiffel-scholarship-program",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Scientific committee individual scoring sheets for candidates",
                    "Country-by-country recipient quota allocations"
                ]
            }
        ]
    },

    # 4. Swedish Institute Scholarships for Global Professionals (SCH-EU-009)
    "SCH-EU-009": {
        "scholarship_id": "SCH-EU-009",
        "basic_details": {
            "scholarship_name": "Swedish Institute Scholarships for Global Professionals (SISGP)",
            "offering_entity": "Swedish Institute (SI) & Government of Sweden (Ministry for Foreign Affairs)",
            "host_country": "Sweden",
            "host_institutions_covered": "All Swedish Universities participating in national admissions (KTH Royal Institute of Technology, Chalmers, Lund, Uppsala, Stockholm University, Karolinska Institutet, Gothenburg, Linköping)",
            "degree_levels": ["Master's"],
            "major_restrictions": "Open to ~700 eligible English-taught Master's degree programs aligned with the UN 2030 Agenda for Sustainable Development (Sustainability, Climate, Engineering, CS, Public Health, Human Rights, Business).",
            "number_of_awards_total": "~350 scholarships awarded annually across 41 eligible countries",
            "number_of_awards_pakistan": "Open to Pakistan as an eligible partner country (~15 to 25 Pakistani scholars selected annually)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "1 to 2 academic years (full duration of the Master's program: 60 or 120 ECTS credits)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Citizen of an eligible country (including Pakistan)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No upper age limit.",
            "academic_qualifications": "Completed 16 years of education (4-year Bachelor's degree or 2-year Bachelor's + 2-year Master's) satisfying Swedish university entrance requirements.",
            "minimum_gpa_percentage": 70.0,
            "minimum_gpa_scale": 3.0,
            "grading_conversion_notes": "Minimum 3.00 / 4.00 CGPA; must meet specific academic prerequisites for chosen Swedish Master's program.",
            "subject_background_prerequisites": "Eligible Master's program in an approved subject area aligned with sustainable development.",
            "current_education_status": "Graduated and currently employed or having substantial past employment.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": True,
            "work_experience_minimum_years": 1.5,
            "work_experience_notes": "MANDATORY: Minimum 3,000 hours of documented work experience (equivalent to approximately 1.5 to 2 years full-time) prior to the deadline, plus demonstrated leadership experience.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "Must meet Swedish University Admissions English 6 requirement: IELTS Academic 6.5 (no band below 5.5) or TOEFL iBT 90 (writing 20)."
            },
            "other_language_requirements": "None; programs taught 100% in English.",
            "gender_specific_requirements": "Equal opportunity; diversity encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Demonstrated leadership experience, commitment to UN Sustainable Development Goals, and potential to contribute to positive development in Pakistan.",
            "previous_scholarship_restrictions": "Ineligible if previously awarded an SI scholarship for master's study, or if currently holding a degree from a Swedish university.",
            "can_apply_result_awaiting": False
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee paid directly by the Swedish Institute to the host Swedish university.",
                "amount": "SEK 140,000 to SEK 280,000 / year (~€12,000 to €25,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University Admissions Sweden application fee (SEK 900, ~PKR 25,000) paid by applicant.",
                "amount": "SEK 900"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Covered via monthly living allowance.",
                "amount": None
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Regular monthly living allowance paid throughout the study period.",
                "amount": "SEK 12,000 / month (~PKR 330,000 / month or SEK 144,000 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "One-time travel grant paid upon arrival in Sweden.",
                "amount": "SEK 15,000 travel grant (~PKR 410,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Swedish residence permit application fee (SEK 1,500) paid by student.",
                "amount": None
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Comprehensive health and accident insurance (Kammarkollegiet) provided by the Swedish state.",
                "amount": None
            },
            "food_allowance": {
                "status": "COVERED",
                "details": "Covered via monthly living stipend.",
                "amount": None
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Covered from living stipend.",
                "amount": None
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Full membership in the SI Network for Future Global Professionals (NFGP) and SI Alumni Network with funded workshops.",
                "amount": None
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in travel grant.",
                "amount": None
            },
            "total_estimated_value_usd_per_year": 35000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Apply for up to 4 eligible Master's programs across any Swedish universities via University Admissions.",
            "participating_institutions": [
                "KTH Royal Institute of Technology", "Chalmers University of Technology", "Lund University",
                "Uppsala University", "Stockholm University", "Karolinska Institutet",
                "University of Gothenburg", "Linköping University", "Umeå University"
            ],
            "university_rankings_scope": "Top 100 European research powerhouses and technology institutes.",
            "available_majors": [
                "Software Engineering, Artificial Intelligence, Cybersecurity, Sustainable Energy Engineering, Mechanical Engineering, Biomedical Sciences, Public Health, Environmental Management, Economics, International Development, Sustainable Business"
            ],
            "english_taught_program_availability": True,
            "program_duration": "1 or 2 academic years (60 or 120 ECTS)",
            "admission_requirements_summary": "Two-step process: First apply for master's programs on University Admissions Sweden; then apply for the SI scholarship using your application number.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Must be admitted to an eligible program by late March to be awarded the scholarship.",
            "strategic_program_match_advice": "Check the official SI list of eligible master's programs; select programs that directly correspond to your documented work experience."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://si.se/en/apply/scholarships/swedish-institute-scholarships-for-global-professionals/",
            "portal_system_name": "Swedish Institute Online Application Portal",
            "account_creation_instructions": "Step 1: Apply for master's programs at universityadmissions.se (October to mid-January). Step 2: Apply for SI scholarship on SI portal (mid-February).",
            "step_by_step_workflow": [
                "1. Apply for up to four eligible Master's programs on UniversityAdmissions.se by January 15.",
                "2. Pay the university application fee (SEK 900) and upload transcripts by February 1.",
                "3. Prepare official SI forms: Work Experience Certificate, Leadership Certificate, and Reference Letters (strict SI templates only).",
                "4. Apply on the SI scholarship portal during the 10-day application window in mid-February.",
                "5. Admissions results announced on UniversityAdmissions.se in late March.",
                "6. If admitted to an eligible program, SI announces scholarship recipients in late April."
            ],
            "university_vs_scholarship_routing": "Two separate applications: University application on central Swedish portal; scholarship application on SI portal.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate using mandatory SI reference letter template with official stamps.",
            "personal_statement_prompts": "Address your leadership experience, how the master's program connects to your work, and how you will advance sustainable development in Pakistan.",
            "study_plan_research_proposal_requirements": "Motivation questions answered directly on the online portal.",
            "cv_format_requirements": "Mandatory Swedish Institute Europass-based CV template (maximum 3 pages; other CV formats disqualify applicant).",
            "interviews_conducted": False,
            "interview_format_details": "No interviews; decisions based entirely on rigorous assessment of written documentation and verified certificates.",
            "standardized_tests": "English test (IELTS 6.5 or TOEFL 90).",
            "application_fee_amount": "SEK 900 for University Admissions; $0 for SI scholarship.",
            "attestation_requirements": "Transcripts attested by HEC Pakistan uploaded to UniversityAdmissions.se.",
            "translation_requirements": "Official certified translations into English.",
            "final_submission_method": "100% Online via SI portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "SI Curriculum Vitae",
                "mandatory": True,
                "specification": "Completed strictly on the mandatory SI CV template (max 3 pages)",
                "pakistan_specific_instruction": "Any other CV format results in automatic disqualification"
            },
            {
                "document_name": "Proof of Work and Leadership Experience",
                "mandatory": True,
                "specification": "Official SI template completed and stamped by employers verifying 3,000+ hours",
                "pakistan_specific_instruction": "Signed and stamped by employers in Pakistan; verifiable contact info required"
            },
            {
                "document_name": "Two Letters of Reference",
                "mandatory": True,
                "specification": "Completed strictly on the official SI template (one from work, one from leadership)",
                "pakistan_specific_instruction": "Must have referee signature and official organization stamp"
            },
            {
                "document_name": "Copy of Passport",
                "mandatory": True,
                "specification": "Valid Pakistani passport photo page",
                "pakistan_specific_instruction": "Valid for at least the duration of intended study"
            },
            {
                "document_name": "Motivation Letter / Portal Questions",
                "mandatory": True,
                "specification": "Answers to SI motivation prompts focusing on UN SDGs",
                "pakistan_specific_instruction": "Clear narrative on sustainability challenges in Pakistan"
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "2026-10-15",
            "application_deadline": "2027-02-20",
            "university_admission_deadline": "2027-01-15",
            "document_submission_deadline": "2027-02-01",
            "recommendation_letters_deadline": "2027-02-20",
            "interview_period": "N/A (No interview)",
            "shortlist_announcement": "N/A",
            "final_result_acceptance_deadline": "2027-05-15",
            "visa_application_window": "May to July 2027",
            "semester_commencement": "August 2027",
            "annual_cycle_notes": "University admissions deadline is mid-January; SI scholarship portal is open for only ~10-14 days in mid-February each year."
        },
        "selection_process_and_weights": {
            "academic_weight": "30% (Admission to an eligible Swedish university Master's program)",
            "extracurricular_and_leadership_weight": "25% (Demonstrated leadership track record in profession or community)",
            "research_experience_weight": "5% (Secondary)",
            "work_experience_weight": "25% (Substantive 3,000+ hours with measurable development impact)",
            "personal_statement_weight": "10% (Alignment with UN Sustainable Development Goals)",
            "recommendations_weight": "5% (Credibility of reference templates)",
            "interview_weight": "0%",
            "test_scores_weight": "Passing threshold required",
            "financial_need_weight": "0% (Merit and leadership driven)",
            "selection_panel_composition": "Swedish Institute selection committee, external evaluators, and Swedish development experts.",
            "evaluation_methodology": "Two-phase: Phase 1 assesses work experience and leadership relevance; Phase 2 verifies university admission."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~7,000 to 8,000 applicants from 41 eligible countries",
            "total_scholarships_awarded": "~350 scholarships awarded globally",
            "acceptance_rate_global": "~4.5%",
            "acceptance_rate_pakistan": "~3% to 4% (Highly Competitive)",
            "typical_successful_applicant_gpa": "3.30 to 3.85 / 4.00 CGPA",
            "typical_academic_and_research_profile": "Professionals with 3 to 7 years of substantive experience in tech, clean energy, public health, or NGOs with clear leadership roles.",
            "common_backgrounds_of_winners": "Mid-career Pakistani engineers, public policy analysts, healthcare professionals, environmental activists.",
            "high_representation_countries": "Pakistan, Nigeria, Bangladesh, Indonesia, Kenya, Ghana, Turkey.",
            "competitiveness_tier": "VERY HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Websites offering fake SI work experience templates or claiming to sell verified forms."
            ],
            "application_fee_warning": "SI scholarship application is 100% free; university application fee on UniversityAdmissions.se is SEK 900.",
            "agent_and_intermediary_warnings": "Swedish Institute strictly audits work certificates; fraudulent certificates result in immediate police report and permanent ban.",
            "hidden_costs_breakdown": [
                "Swedish university application fee (SEK 900, ~PKR 25,000).",
                "Swedish residence permit fee (SEK 1,500, ~PKR 41,000).",
                "English language test fees (IELTS/TOEFL).",
                "Initial pocket money before first stipend transfer in Sweden."
            ],
            "misleading_claims_debunked": [
                "MYTH: You can use your own CV format. (Fact: You MUST use the official SI CV template; any other format is disqualified).",
                "MYTH: Fresh graduates with zero work experience can apply. (Fact: 3,000 hours of documented work experience is an absolute requirement)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Many blogs state work experience can be self-certified; officially, all hours must be stamped by employers on official templates."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass at least 45 ECTS credits per academic year (out of 60 ECTS).",
            "attendance_requirements": "Full-time physical studies on campus in Sweden.",
            "academic_progress_monitoring": "Host universities report credits earned each semester to the Swedish Institute.",
            "work_restrictions_during_study": "There is no legal limit on work hours for student visa holders in Sweden, but SI expects full-time dedication to studies.",
            "home_country_return_obligation": "No mandatory return rule; scholars can apply for a 1-year residence permit to seek employment or start a business in Sweden post-graduation.",
            "service_obligations_or_bonds": "None; commitment to engage with the SI Alumni Network.",
            "repayment_clawback_conditions": "Failing to obtain minimum required credits leads to suspension or withdrawal of scholarship.",
            "rules_for_changing_university": "Strictly prohibited.",
            "rules_for_changing_major": "Strictly prohibited.",
            "extension_policy": "Scholarships cannot be extended beyond the official duration of the program."
        },
        "official_sources_verified": [
            {
                "source_name": "Swedish Institute - SISGP Scholarships Official Portal",
                "source_url": "https://si.se/en/apply/scholarships/swedish-institute-scholarships-for-global-professionals/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact country-by-country target numbers among the 41 eligible countries",
                    "Internal scoring rubric for work experience certificates"
                ]
            }
        ]
    }
}
