# scripts/batch17_p3.py
# SCH-OC-013: University of Wollongong Postgraduate Research Scholarship (UPRS) (Australia)
# SCH-OC-015: Curtin University Australian Government Research Training Program (RTP) (Australia)
# SCH-OC-016: Deakin University Postgraduate Research Scholarship (DUPRS) (Australia)
# SCH-OC-019: University of Otago International Doctoral Research Scholarships (New Zealand)

DATA_P3 = {
    "SCH-OC-013": {
        "scholarship_id": "SCH-OC-013",
        "basic_details": {
            "scholarship_name": "University of Wollongong Postgraduate Research Scholarship (UPRS)",
            "offering_entity": "University of Wollongong (UOW) & Graduate Research School (GRS)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Wollongong (Wollongong Main Campus and Innovation Campus, NSW, Australia)",
            "degree_levels": ["Doctor of Philosophy (PhD)", "Master of Philosophy (MPhil)"],
            "major_restrictions": "Faculty of Engineering and Information Sciences (Computer Science, Telecommunications, Cyber Security, Mechanical, Civil, Mining, Materials, Mechatronics), Faculty of Science, Medicine and Health, and Faculty of Business and Law.",
            "number_of_awards_total": "~80 to 120 international doctoral scholarships awarded annually across UPRS and matching faculty schemes",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani graduate researchers in computing, telecommunications, and engineering secure ~6 to 12 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD; up to 2 years for Research Master's, subject to satisfactory annual research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International citizens of all nationalities except Australia and New Zealand (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research outputs.",
            "academic_qualifications": "4-year Bachelor's degree with First Class Honours, or research Master's degree (minimum 18 years education) with a substantial research thesis component from an HEC-recognized university with high academic achievement (minimum 78% aggregate or CGPA 3.50 / 4.00; competitive admits typically 3.70+ / 4.00).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Equivalent to Australian Honours Class 1 (H1; 80%+ equivalent).",
            "subject_background_prerequisites": "Relevant undergraduate/master's degree in engineering, computing, physical sciences, or applied mathematics.",
            "current_education_status": "Master's students in their final semester can apply conditionally with thesis submission proof.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications in Scopus/IEEE indexed journals or conference papers strongly prioritized.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 86,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (minimum 6.0 in each subtest), TOEFL iBT minimum 86 (reading 18, writing 18, listening 17, speaking 17), or PTE Academic minimum 62. Official test report mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must obtain a written statement of supervisory support from an accredited UOW faculty member before submitting.",
            "previous_scholarship_restrictions": "Cannot hold concurrent external government or institutional awards.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee waiver for up to 3.5 years of doctoral research (AUD 38,000 to 44,000 / year value).",
                "amount": "100% covered (~AUD 42,000 / year; ~PKR 7,770,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application fee waived for candidates applying with formal UOW supervisor endorsement.",
                "amount": "AUD 0 (Fee waived)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Subsidized on-campus graduate housing (Kooloobong Village, Graduate House) or rental apartments in Wollongong (average AUD 280 to 400 / week) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~AUD 1,300 / month; ~PKR 240,500 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Indexed tax-free living stipend at the Australian Government RTP rate: AUD 34,000 to 36,500 / year (~USD 23,000 to 24,500 / year; AUD 2,833 to 3,040 / month; ~PKR 524,000 to 562,400 / month) for up to 3.5 years.",
                "amount": "AUD 34,000 to 36,500 / year (~PKR 524,000 to 562,400 / mo)"
            },
            "airfare": {
                "status": "PARTIAL",
                "details": "One-off relocation allowance of up to AUD 2,000 provided to international awardees towards initial international travel to Australia.",
                "amount": "Up to AUD 2,000 relocation grant (~PKR 370,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Student Visa (Subclass 500) application charge (~AUD 1,600) paid by the student.",
                "amount": "Not covered (~AUD 1,600; ~PKR 296,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Overseas Student Health Cover (OSHC) single policy fully covered for the duration of the student visa.",
                "amount": "100% covered OSHC single policy"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living costs and groceries in Wollongong are lower than Sydney; comfortably covered within the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Comprehensive access to UOW Library, high-performance computing clusters, and engineering laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty conference travel grants (up to AUD 2,500) available for presenting papers at peer-reviewed international conferences.",
                "amount": "Up to AUD 2,500 conference travel grant"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Free Wollongong Gong Shuttle bus (Route 55A/55B) connects campus with Wollongong CBD, train station, and beaches.",
                "amount": "100% free municipal campus shuttle"
            },
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (University of Wollongong)",
            "participating_institutions": [
                "University of Wollongong (UOW Main Campus & Innovation Campus, Wollongong, NSW, Australia)"
            ],
            "university_rankings_scope": "QS World University Rankings #167 worldwide, Times Higher Education #201-250, top-ranked Australian institution for Graduate Employability and Telecommunications.",
            "available_majors": [
                "Computer Science and Software Engineering",
                "Cyber Security and Cryptography",
                "Telecommunications and Networking",
                "Electrical and Information Engineering",
                "Mechanical and Mechatronic Engineering",
                "Civil and Mining Engineering",
                "Materials Science and Superconductivity",
                "Chemistry and Molecular Bioscience",
                "Environmental Science and Coastal Management",
                "Business and Management Information Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3.5 years (full-time PhD)",
            "admission_requirements_summary": "Online UOW Apply portal application, prospective supervisor endorsement statement, certified academic transcripts and degree certificates, research proposal, curriculum vitae, official IELTS/TOEFL score report, two academic referee reports, and sample publications.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "School of Computing and Information Technology and the Institute for Superconducting and Electronic Materials (ISEM) are major research hubs with high applicant interest; having an endorsed research topic and journal publications ensures strong ranking.",
            "strategic_program_match_advice": "Reach out to potential supervisors 2-3 months before the round deadline. Provide an academic CV highlighting peer-reviewed papers and a concise 2-page research draft aligned with their lab's current ARC projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.uow.edu.au/study/scholarships/postgraduate-research/ & https://apply.uow.edu.au/",
            "portal_system_name": "UOW Apply Online HDR Portal",
            "account_creation_instructions": "Contact potential supervisor to obtain written support. Create account on UOW Apply Online, choose Higher Degree Research, select PhD, and tick the box for 'University Postgraduate Research Scholarship (UPRS)'.",
            "step_by_step_workflow": [
                "Step 1: Contact potential supervisors via UOW Scholars directory with CV and research interests (August - September for Autumn round).",
                "Step 2: Secure written endorsement statement from the prospective primary supervisor.",
                "Step 3: Take IELTS (min 6.5) or TOEFL (min 86) and obtain official test results.",
                "Step 4: Register on UOW Apply Online and complete the admission and scholarship application form.",
                "Step 5: Upload supervisor endorsement, research proposal, certified transcripts, degrees, CV, and published papers.",
                "Step 6: Referees submit online evaluation forms via automated institutional links.",
                "Step 7: Faculty Research Committee ranks applicants based on academic merit and research track record (November).",
                "Step 8: Graduate Research School issues scholarship and admission offer letters (December).",
                "Step 9: Accept the award, obtain Confirmation of Enrolment (CoE), apply for Australian Student Visa (Subclass 500), and commence in February (Autumn session)."
            ],
            "university_vs_scholarship_routing": "Integrated Track: The scholarship application is evaluated concurrently with the HDR admission application.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement outlining research background, motivations for doctoral study at UOW, and career aspirations.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing research objectives, methodology, significance, and alignment with UOW research groups.",
            "cv_format_requirements": "Academic CV detailing qualifications, publications (with DOI, impact factor, and authorship role), and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Online video interview conducted by prospective primary supervisor prior to issuing supervisory endorsement.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 86) mandatory; GRE not required.",
            "application_fee_amount": "AUD 0 (Waived with supervisor endorsement)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and verified by issuing universities; certified color scans required.",
            "translation_requirements": "Certified English translation required for any documents not in English.",
            "final_submission_method": "100% digital submission via the UOW Apply Online portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Supervisor Endorsement / Support Statement",
                "mandatory": True,
                "specification": "Official written statement from an accredited UOW academic agreeing to supervise the candidate.",
                "pakistan_specific_instruction": "Crucial requirement; applications without supervisor backing are not considered."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's and Master's transcripts and degree certificates with grading scale.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan with Australian First Class Honours equivalence explanation."
            },
            {
                "document_name": "Doctoral Research Proposal",
                "mandatory": True,
                "specification": "Detailed 3-5 page research proposal agreed upon with prospective supervisor.",
                "pakistan_specific_instruction": "Ensure high academic rigor and direct alignment with UOW faculty strengths."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 86).",
                "pakistan_specific_instruction": "Must be valid within 2 years of proposed commencement date."
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by university professors who supervised previous research thesis.",
                "pakistan_specific_instruction": "Must be sent from official institutional email addresses."
            },
            {
                "document_name": "Curriculum Vitae and Published Papers",
                "mandatory": True,
                "specification": "Academic CV including full-text PDFs of peer-reviewed journal/conference publications.",
                "pakistan_specific_instruction": "Highlight papers indexed in Scopus, IEEE Xplore, or Web of Science."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "July 1 (Autumn Round) / January 1 (Spring Round)",
            "application_deadline": "October 17 (Autumn Round) / April 17 (Spring Round)",
            "university_admission_deadline": "October 17 / April 17",
            "document_submission_deadline": "October 17 / April 17",
            "recommendation_letters_deadline": "October 24 / April 24",
            "interview_period": "Conducted informally during supervisor outreach stage",
            "shortlist_announcement": "December (Autumn Round) / June (Spring Round)",
            "final_result_acceptance_deadline": "Mid-January / Mid-July",
            "visa_application_window": "January - February / July - August",
            "semester_commencement": "Autumn (February / March) / Spring (July / August)",
            "annual_cycle_notes": "Two major scholarship rounds per year. The Autumn Round (October deadline) is the primary annual intake."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Australian Honours 1 equivalence, Bachelor's/Master's GPA)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated for HDR research awards)",
            "research_experience_weight": "45% (Peer-reviewed journal publications, citations, research thesis quality)",
            "work_experience_weight": "5% (Industry R&D experience in relevant field)",
            "personal_statement_weight": "0% (Not separately weighted)",
            "recommendations_weight": "5% (Referee ratings on research capability)",
            "interview_weight": "0% (Supervisor endorsement serves as interview validation)",
            "test_scores_weight": "0% (English meets required benchmark)",
            "financial_need_weight": "0% (Purely merit and research output based)",
            "selection_panel_composition": "Faculty Research Committee, School HDR Coordinators, and Graduate Research School Scholarship Board.",
            "evaluation_methodology": "Strict merit-based scoring based on H1 equivalence calculation, verified research track record (Scopus/WoS publications), and supervisor sponsorship."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,500 international doctoral applicants globally across both rounds",
            "total_scholarships_awarded": "~80 to 120 comprehensive UPRS awards annually",
            "acceptance_rate_global": "~4.0% to 5.5%",
            "acceptance_rate_pakistan": "~6.0% to 8.0% among applicants possessing at least 1-2 Scopus Q1/Q2 journal papers",
            "typical_successful_applicant_gpa": "CGPA 3.65+ / 4.00 or 80%+ aggregate with First Class Honours from leading Pakistani universities (NUST, GIKI, PIEAS, FAST, QAU, UET)",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, at least 1-2 first-author papers in high-impact international journals, and an engaged supervisory team.",
            "common_backgrounds_of_winners": "Graduates of premier Pakistani engineering and science universities.",
            "high_representation_countries": "China, India, Pakistan, Iran, Vietnam, Bangladesh, Nigeria, UK.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents advertising guaranteed Australian scholarships or visa packages.",
                "Applications are processed exclusively through uow.edu.au."
            ],
            "application_fee_warning": "Applying with supervisor endorsement is free of charge; never pay agent fees.",
            "agent_and_intermediary_warnings": "UOW does not work with third-party agencies for doctoral research scholarship distribution.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application charge: ~AUD 1,600 (~PKR 296,000).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Biometrics, health examination in Pakistan (IOM clinic): ~PKR 40,000.",
                "Degree attestation in Pakistan (HEC and MoFA): ~PKR 25,000 to 35,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without contacting a professor first. Reality: An application without an agreed supervisor is not processed.",
                "Myth: Wollongong is remote from major cities. Reality: Wollongong is a picturesque coastal city located just 80 km south of Sydney, with lower living costs."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums claim high school marks are evaluated; only Bachelor's (Honours) and Master's research outputs are scored."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic research progress and successfully pass the First Year Candidature Confirmation milestone.",
            "attendance_requirements": "Full-time on-campus research commitment; standard leave entitlements (20 days annual recreation leave).",
            "academic_progress_monitoring": "Annual Progress Review (APR) evaluated by the supervisory committee and School HDR Coordinator; unsatisfactory progress leads to termination.",
            "work_restrictions_during_study": "Part-time work permitted (teaching or research assistantships) up to 8-10 hours per week during normal business hours, provided it does not impede PhD progress.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Australian Temporary Graduate Visa (Subclass 485) post-study work stream.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship terminated if candidature is discontinued or scholar is dismissed for academic misconduct.",
            "rules_for_changing_university": "Non-transferable to other Australian universities.",
            "rules_for_changing_major": "Changing research topic requires formal approval of the supervisory committee and GRS.",
            "extension_policy": "Maximum extension of up to 6 months for PhD scholarships permitted in exceptional circumstances with documented research delays."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Wollongong Postgraduate Research Scholarships Portal",
                "source_url": "https://www.uow.edu.au/study/scholarships/postgraduate-research/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UOW Graduate Research School (GRS)",
                "source_url": "https://www.uow.edu.au/research/graduate-research-school/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-OC-015": {
        "scholarship_id": "SCH-OC-015",
        "basic_details": {
            "scholarship_name": "Curtin University Australian Government Research Training Program (RTP)",
            "offering_entity": "Curtin University & Australian Government Department of Education",
            "host_country": "Australia",
            "host_institutions_covered": "Curtin University (Bentley Main Campus, Perth, Western Australia)",
            "degree_levels": ["Doctor of Philosophy (PhD)", "Master of Philosophy (MPhil)"],
            "major_restrictions": "Faculty of Science and Engineering (Computing, Electrical, Chemical, Mining & Metallurgy, Petroleum Engineering, Earth & Planetary Sciences, Astrophysics / Space Science), Faculty of Health Sciences, and Curtin Business School.",
            "number_of_awards_total": "~100 to 140 comprehensive international doctoral scholarships awarded annually across RTP and Curtin Strategic Scholarship schemes",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani graduate researchers in mining, computing, earth sciences, and engineering secure ~8 to 15 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD; up to 2 years for Research Master's, subject to satisfactory annual progress reviews"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International citizens of all nationalities except Australia and New Zealand (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic excellence and verified research capability.",
            "academic_qualifications": "4-year Bachelor's degree with First Class Honours, or research Master's degree (minimum 18 years education) with a substantial thesis component from an HEC-recognized university with high academic achievement (minimum 80% aggregate or CGPA 3.60 / 4.00; competitive admits typically 3.75+ / 4.00).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Equivalent to Australian First Class Honours (Honours 1 / H1; 80%+ equivalent).",
            "subject_background_prerequisites": "Relevant undergraduate/master's degree corresponding directly to the applied research field.",
            "current_education_status": "Master's students in their final semester can apply conditionally with thesis submission proof.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Substantial research experience, first-author journal publications (Scopus/Web of Science), or major conference proceedings are decisive.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (minimum 6.0 in each subtest), TOEFL iBT minimum 79 (reading 13, listening 12, speaking 18, writing 21), or PTE Academic minimum 58. Official test report mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure an Expression of Interest (EOI) approval and supervisory consent from an accredited Curtin faculty member prior to formal application.",
            "previous_scholarship_restrictions": "Cannot hold another concurrent Australian government or university award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee waiver for up to 3.5 years of doctoral candidature (AUD 40,000 to 46,000 / year value).",
                "amount": "100% covered (~AUD 43,000 / year; ~PKR 7,955,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application fee waived for candidates applying with approved supervisor EOI.",
                "amount": "AUD 0 (Fee waived)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus student housing at Curtin Bentley (St Catherine's, UniLodge) or private rentals in Perth (average AUD 250 to 380 / week) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~AUD 1,200 / month; ~PKR 222,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Indexed tax-free living stipend at the official Australian Government RTP rate: AUD 35,000 to 37,500 / year (~USD 23,500 to 25,000 / year; AUD 2,916 to 3,125 / month; ~PKR 539,600 to 578,100 / month) for up to 3.5 years.",
                "amount": "AUD 35,000 to 37,500 / year (~PKR 539,600 to 578,100 / mo)"
            },
            "airfare": {
                "status": "PARTIAL",
                "details": "Relocation allowance of up to AUD 2,295 provided to international awardees towards initial international travel to Perth.",
                "amount": "Up to AUD 2,295 relocation grant (~PKR 424,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Student Visa (Subclass 500) application charge (~AUD 1,600) paid by the student.",
                "amount": "Not covered (~AUD 1,600; ~PKR 296,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Overseas Student Health Cover (OSHC) single policy fully covered for the duration of the student visa.",
                "amount": "100% covered OSHC single policy"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Perth easily accommodated within the monthly tax-free stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Curtin Robertson Library, Pawsey Supercomputing Centre, and advanced engineering and mineral laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty conference travel funds (up to AUD 3,000) available for presenting papers at peer-reviewed international conferences.",
                "amount": "Up to AUD 3,000 conference travel grant"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Perth Transperth public transit paid from monthly stipend (~AUD 100/month; Tertiary student concession fare applies).",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 55000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Curtin University, Perth)",
            "participating_institutions": [
                "Curtin University Bentley Main Campus (Perth, Western Australia)"
            ],
            "university_rankings_scope": "QS World University Rankings #174 worldwide, #2 globally in Mineral and Mining Engineering, Times Higher Education #201-250.",
            "available_majors": [
                "Mineral and Mining Engineering",
                "Petroleum and Energy Engineering",
                "Computer Science and Artificial Intelligence",
                "Electrical and Electronic Engineering",
                "Chemical Engineering",
                "Civil and Construction Engineering",
                "Earth and Planetary Sciences (Geology, Geophysics)",
                "Radio Astronomy and Space Science",
                "Biomedical Sciences and Pharmacy",
                "Business Information Systems and Supply Chain"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3.5 years (full-time PhD)",
            "admission_requirements_summary": "Online Curtin e-Application submission, supervisor EOI approval statement, certified academic transcripts and degree certificates, research proposal, curriculum vitae, official IELTS/TOEFL score report, two academic referee reports, and sample publications.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Mining Engineering and Radio Astronomy (partner in the Square Kilometre Array - SKA) have world-class research facilities and strong funding; Computer Science and AI receive high international application volumes.",
            "strategic_program_match_advice": "Initiate supervisor contact 3-4 months before the round deadline. Provide an academic CV highlighting peer-reviewed papers and a concise 2-page research draft aligned with their lab's current ARC or industry-sponsored projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://scholarships.curtin.edu.au/scholarship/?id=6121 & https://www.curtin.edu.au/study/postgraduate/research/",
            "portal_system_name": "Curtin University Online HDR Admissions Portal",
            "account_creation_instructions": "Submit an Expression of Interest (EOI) to a potential supervisor via Curtin staff directory. Once supported, complete the formal online HDR application selecting RTP Scholarship consideration.",
            "step_by_step_workflow": [
                "Step 1: Identify prospective supervisors via Curtin Research Gateway and submit EOI with CV and research abstract (June - August for Round 1).",
                "Step 2: Obtain formal written supervisory endorsement from the Curtin academic.",
                "Step 3: Take IELTS (min 6.5) or TOEFL (min 79) and verify scores meet Curtin HDR English requirements.",
                "Step 4: Register on Curtin online application portal, select PhD program, and choose scholarship round.",
                "Step 5: Upload supervisor endorsement, research proposal, transcripts, degree certificates, CV, and published papers.",
                "Step 6: Referees submit online reports directly through automated email links generated by the portal.",
                "Step 7: Faculty Higher Degree Research Committee ranks candidates based on H1 equivalence and research track record (September - October).",
                "Step 8: Graduate Research School announces final RTP and admission results (November).",
                "Step 9: Accept the award, obtain Confirmation of Enrolment (CoE), apply for Australian Student Visa (Subclass 500), and commence research in Semester 1 (February)."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Admission and scholarship applications are submitted simultaneously through the Curtin online portal.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement outlining research background, motivations for doctoral research at Curtin, and academic trajectory.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing research objectives, methodology, theoretical significance, and alignment with supervisor's laboratory.",
            "cv_format_requirements": "Academic CV detailing qualifications, peer-reviewed publications (with DOI, journal impact factor, and authorship role), and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Informal or formal online video interview conducted by prospective primary supervisor prior to issuing supervisory endorsement.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 79) mandatory; GRE not required.",
            "application_fee_amount": "AUD 0 (Waived with supervisor endorsement)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and verified by issuing universities; certified color copies required.",
            "translation_requirements": "Certified English translation required for any documents not in English.",
            "final_submission_method": "100% digital submission via the Curtin online portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Supervisor Endorsement / Support Statement",
                "mandatory": True,
                "specification": "Official written statement from an accredited Curtin academic agreeing to supervise the candidate.",
                "pakistan_specific_instruction": "Crucial requirement; applications without supervisor agreement are not assessed."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's and Master's transcripts and degree certificates with grading scale.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan with Australian First Class Honours equivalence explanation."
            },
            {
                "document_name": "Doctoral Research Proposal",
                "mandatory": True,
                "specification": "Detailed 3-5 page research proposal agreed upon with prospective supervisor.",
                "pakistan_specific_instruction": "Ensure methodology is rigorous and feasible within Australian research context."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 79).",
                "pakistan_specific_instruction": "Must be valid within 2 years of proposed commencement date."
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by university professors who supervised previous research thesis.",
                "pakistan_specific_instruction": "Must be sent from official institutional email addresses."
            },
            {
                "document_name": "Curriculum Vitae and Published Papers",
                "mandatory": True,
                "specification": "Academic CV including full-text PDFs of peer-reviewed journal/conference publications.",
                "pakistan_specific_instruction": "Highlight papers indexed in Scopus, IEEE Xplore, or Web of Science."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "June 1 (Round 1) / December 1 (Round 2)",
            "application_deadline": "September 1 (Round 1 for Semester 1 next year) / March 1 (Round 2 for Semester 2)",
            "university_admission_deadline": "September 1 / March 1",
            "document_submission_deadline": "September 1 / March 1",
            "recommendation_letters_deadline": "September 10 / March 10",
            "interview_period": "Conducted informally during supervisor outreach stage",
            "shortlist_announcement": "November (Round 1) / May (Round 2)",
            "final_result_acceptance_deadline": "Mid-December / Mid-June",
            "visa_application_window": "December - January / June - July",
            "semester_commencement": "Semester 1 (February) / Semester 2 (July)",
            "annual_cycle_notes": "Two major scholarship rounds per year. Round 1 (deadline September 1) is the primary annual intake for February commencement."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Australian Honours 1 equivalence, Bachelor's/Master's GPA)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated for HDR research awards)",
            "research_experience_weight": "45% (Peer-reviewed journal publications, citations, research thesis quality)",
            "work_experience_weight": "5% (Industry R&D experience in relevant field)",
            "personal_statement_weight": "0% (Not separately weighted)",
            "recommendations_weight": "5% (Referee ratings on research capability)",
            "interview_weight": "0% (Supervisor endorsement serves as interview validation)",
            "test_scores_weight": "0% (English meets required benchmark)",
            "financial_need_weight": "0% (Purely merit and research output based)",
            "selection_panel_composition": "Faculty HDR Committee, School Postgraduate Coordinators, and Curtin Graduate Research School Board.",
            "evaluation_methodology": "Strict metric-driven scoring based on H1 equivalence calculation, verified research track record (Scopus/WoS publications), and supervisor sponsorship."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 international doctoral applicants globally across both rounds",
            "total_scholarships_awarded": "~100 to 140 comprehensive RTP/Strategic awards annually",
            "acceptance_rate_global": "~3.5% to 5.0%",
            "acceptance_rate_pakistan": "~6.0% among applicants possessing at least 1-2 Scopus Q1/Q2 journal papers",
            "typical_successful_applicant_gpa": "CGPA 3.70+ / 4.00 or 80%+ aggregate with First Class Honours from leading Pakistani universities (NUST, GIKI, PIEAS, FAST, QAU, UET)",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, at least 1-2 first-author papers in high-impact international journals, and a strong supervisory endorsement.",
            "common_backgrounds_of_winners": "Graduates of premier Pakistani engineering and science universities.",
            "high_representation_countries": "China, India, Pakistan, Iran, Vietnam, Germany, Malaysia, UK.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents advertising guaranteed Australian scholarships or visa packages.",
                "Applications are processed exclusively through curtin.edu.au."
            ],
            "application_fee_warning": "Applying with supervisor endorsement is free of charge; never pay agent fees.",
            "agent_and_intermediary_warnings": "Curtin does not work with third-party agencies for doctoral research scholarship distribution.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application charge: ~AUD 1,600 (~PKR 296,000).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Biometrics, health examination in Pakistan (IOM clinic): ~PKR 40,000.",
                "Degree attestation in Pakistan (HEC and MoFA): ~PKR 25,000 to 35,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without contacting a professor first. Reality: In Australia, an application without an agreed supervisor is immediately rejected.",
                "Myth: Work experience substitutes for lack of research papers. Reality: The scoring system is heavily weighted toward peer-reviewed journal papers and academic thesis grades."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums claim high school marks are evaluated; for PhD, only Bachelor's (Honours) and Master's research outputs are scored."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic research progress and successfully pass the Candidature Confirmation milestone within 12 months.",
            "attendance_requirements": "Full-time on-campus research commitment; standard leave entitlements (20 days annual recreation leave).",
            "academic_progress_monitoring": "Annual Progress Review (APR) evaluated by the supervisory committee and School Postgraduate Coordinator; unsatisfactory progress leads to termination.",
            "work_restrictions_during_study": "Part-time work permitted (teaching or research assistantships) up to 8-10 hours per week during normal business hours, provided it does not impede PhD progress.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Australian Temporary Graduate Visa (Subclass 485 - post-study work stream).",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship terminated if candidature is discontinued or scholar is dismissed for academic misconduct.",
            "rules_for_changing_university": "Non-transferable to other Australian universities.",
            "rules_for_changing_major": "Changing research topic requires formal approval of the supervisory committee and Graduate Research School.",
            "extension_policy": "Maximum extension of up to 6 months for PhD scholarships permitted in exceptional circumstances with documented research delays."
        },
        "official_sources_verified": [
            {
                "source_name": "Curtin University Scholarships Portal",
                "source_url": "https://scholarships.curtin.edu.au/scholarship/?id=6121",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Curtin Graduate Research School",
                "source_url": "https://www.curtin.edu.au/study/postgraduate/research/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-OC-016": {
        "scholarship_id": "SCH-OC-016",
        "basic_details": {
            "scholarship_name": "Deakin University Postgraduate Research Scholarship (DUPRS)",
            "offering_entity": "Deakin University & Deakin Graduate Research Academy (GRA)",
            "host_country": "Australia",
            "host_institutions_covered": "Deakin University (Melbourne Burwood Campus, Geelong Waurn Ponds Campus, and Waterfront Campus, Victoria, Australia)",
            "degree_levels": ["Doctor of Philosophy (PhD)", "Master of Science by Research"],
            "major_restrictions": "Faculty of Science, Engineering and Built Environment (SEBE - Information Technology, Artificial Intelligence, Cyber Security, Software Engineering, Frontier Materials, Additive Manufacturing, Intelligent Systems), Faculty of Health, Faculty of Arts and Education, and Faculty of Business and Law.",
            "number_of_awards_total": "~120 to 160 international doctoral scholarships awarded annually across DUPRS and matching research institute schemes",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani graduate researchers in AI, cyber security, materials, and engineering secure ~8 to 16 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD; up to 2 years for Research Master's, subject to satisfactory annual progress reviews"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International citizens of all nationalities except Australia and New Zealand (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research outputs.",
            "academic_qualifications": "4-year Bachelor's degree with First Class Honours, or research Master's degree (minimum 18 years education) with a substantial thesis component from an HEC-recognized university with high academic achievement (minimum 78% aggregate or CGPA 3.50 / 4.00; competitive admits typically 3.70+ / 4.00).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Equivalent to Australian Honours Class 1 (H1; 80%+ equivalent).",
            "subject_background_prerequisites": "Relevant undergraduate/master's degree in engineering, computing, physical sciences, or health sciences.",
            "current_education_status": "Master's students in their final semester can apply conditionally with thesis submission proof.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Research publications in Scopus/IEEE indexed journals or conference papers strongly prioritized.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 79,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (minimum 6.0 in each subtest), TOEFL iBT minimum 79 (writing 21), or PTE Academic minimum 58. Official test report mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure an Expression of Interest (EOI) approval and supervisory consent from an accredited Deakin faculty member before submitting.",
            "previous_scholarship_restrictions": "Cannot hold another concurrent Australian government or university award.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee waiver for up to 3.5 years of doctoral candidature (AUD 38,000 to 45,000 / year value).",
                "amount": "100% covered (~AUD 42,000 / year; ~PKR 7,770,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Application fee waived for candidates applying with approved supervisor EOI.",
                "amount": "AUD 0 (Fee waived)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus student residence at Melbourne Burwood or Geelong Waurn Ponds, or private rentals (average AUD 260 to 380 / week) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~AUD 1,250 / month; ~PKR 231,250 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Indexed tax-free living stipend: AUD 34,400 to 36,000 / year (~USD 23,000 to 24,000 / year; AUD 2,866 to 3,000 / month; ~PKR 530,200 to 555,000 / month) for up to 3.5 years.",
                "amount": "AUD 34,400 to 36,000 / year (~PKR 530,200 to 555,000 / mo)"
            },
            "airfare": {
                "status": "PARTIAL",
                "details": "Relocation allowance of up to AUD 1,500 provided to international awardees towards initial international travel to Victoria.",
                "amount": "Up to AUD 1,500 relocation grant (~PKR 277,500)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Student Visa (Subclass 500) application charge (~AUD 1,600) paid by the student.",
                "amount": "Not covered (~AUD 1,600; ~PKR 296,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Overseas Student Health Cover (OSHC) single policy fully covered for the duration of the student visa.",
                "amount": "100% covered OSHC single policy"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Melbourne/Geelong easily accommodated within the monthly tax-free stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Comprehensive access to Deakin Library, Institute for Frontier Materials (IFM) labs, Applied AI Institute (A2I2) computing, and engineering facilities.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty conference travel funds (up to AUD 2,500) available for presenting papers at peer-reviewed international conferences.",
                "amount": "Up to AUD 2,500 conference travel grant"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Melbourne/Geelong public transit (myki card) paid from monthly stipend (~AUD 120/month; student concession fare applies).",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 52000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Deakin University, Victoria)",
            "participating_institutions": [
                "Deakin University (Melbourne Burwood & Geelong Campuses, Victoria, Australia)"
            ],
            "university_rankings_scope": "QS World University Rankings #197 worldwide, Times Higher Education #201-250, top-ranked for Artificial Intelligence, Cyber Security, and Materials Science.",
            "available_majors": [
                "Artificial Intelligence and Machine Learning (A2I2)",
                "Cyber Security and Software Engineering",
                "Information Technology and Data Science",
                "Frontier Materials and Nanotechnology (IFM)",
                "Additive Manufacturing and Advanced Engineering",
                "Electrical and Renewable Energy Engineering",
                "Mechanical and Mechatronics Engineering",
                "Civil and Environmental Engineering",
                "Health Sciences and Medicine",
                "Business Analytics and Information Systems"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3.5 years (full-time PhD)",
            "admission_requirements_summary": "Online Deakin HDR portal application, supervisor EOI approval statement, certified academic transcripts and degree certificates, research proposal, curriculum vitae, official IELTS/TOEFL score report, two academic referee reports, and sample publications.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Applied Artificial Intelligence Institute (A2I2) and Institute for Frontier Materials (IFM) are global leaders with high funding; Computer Science and AI receive substantial international application volumes.",
            "strategic_program_match_advice": "Initiate supervisor contact 3-4 months before the round deadline. Provide an academic CV highlighting peer-reviewed papers and a concise 2-page research draft aligned with their lab's current ARC or industrial projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.deakin.edu.au/study/fees-and-scholarships/scholarships/find-a-scholarship/deakin-university-postgraduate-research-scholarship-duprs & https://www.deakin.edu.au/research/research-degrees-and-phd/how-to-apply",
            "portal_system_name": "Deakin Higher Degree by Research Application Portal",
            "account_creation_instructions": "Submit an Expression of Interest (EOI) to a potential supervisor via Deakin faculty directory. Once approved, complete the formal online HDR application selecting DUPRS Scholarship consideration.",
            "step_by_step_workflow": [
                "Step 1: Identify prospective supervisors via Deakin Research Gateway and submit EOI with CV and research abstract (May - July for Trimester 1 intake).",
                "Step 2: Obtain formal written supervisory endorsement from the Deakin academic.",
                "Step 3: Take IELTS (min 6.5) or TOEFL (min 79) and verify scores meet Deakin HDR English requirements.",
                "Step 4: Register on Deakin online application portal, select PhD program, and choose scholarship round.",
                "Step 5: Upload supervisor endorsement, research proposal, transcripts, degree certificates, CV, and published papers.",
                "Step 6: Referees submit online reports directly through automated email links generated by the portal.",
                "Step 7: Faculty Higher Degree Research Committee ranks candidates based on H1 equivalence and research track record (September - October).",
                "Step 8: Graduate Research Academy announces final DUPRS and admission results (November).",
                "Step 9: Accept the award, obtain Confirmation of Enrolment (CoE), apply for Australian Student Visa (Subclass 500), and commence research in Trimester 1 (February)."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Admission and scholarship applications are submitted simultaneously through the Deakin online portal.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement outlining research background, motivations for doctoral research at Deakin, and academic trajectory.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing research objectives, methodology, theoretical significance, and alignment with supervisor's laboratory.",
            "cv_format_requirements": "Academic CV detailing qualifications, peer-reviewed publications (with DOI, journal impact factor, and authorship role), and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Informal or formal online video interview conducted by prospective primary supervisor prior to issuing supervisory endorsement.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 79) mandatory; GRE not required.",
            "application_fee_amount": "AUD 0 (Waived with supervisor endorsement)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and verified by issuing universities; certified color copies required.",
            "translation_requirements": "Certified English translation required for any documents not in English.",
            "final_submission_method": "100% digital submission via the Deakin online portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Supervisor Endorsement / Support Statement",
                "mandatory": True,
                "specification": "Official written statement from an accredited Deakin academic agreeing to supervise the candidate.",
                "pakistan_specific_instruction": "Crucial requirement; applications without supervisor agreement are not assessed."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's and Master's transcripts and degree certificates with grading scale.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan with Australian First Class Honours equivalence explanation."
            },
            {
                "document_name": "Doctoral Research Proposal",
                "mandatory": True,
                "specification": "Detailed 3-5 page research proposal agreed upon with prospective supervisor.",
                "pakistan_specific_instruction": "Ensure methodology is rigorous and feasible within Australian research context."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 79).",
                "pakistan_specific_instruction": "Must be valid within 2 years of proposed commencement date."
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by university professors who supervised previous research thesis.",
                "pakistan_specific_instruction": "Must be sent from official institutional email addresses."
            },
            {
                "document_name": "Curriculum Vitae and Published Papers",
                "mandatory": True,
                "specification": "Academic CV including full-text PDFs of peer-reviewed journal/conference publications.",
                "pakistan_specific_instruction": "Highlight papers indexed in Scopus, IEEE Xplore, or Web of Science."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Applications open year-round",
            "application_deadline": "August 15 (Trimester 1 / February intake) / January 15 (Trimester 2 / July intake)",
            "university_admission_deadline": "August 15 / January 15",
            "document_submission_deadline": "August 15 / January 15",
            "recommendation_letters_deadline": "August 22 / January 22",
            "interview_period": "Conducted informally during supervisor outreach stage",
            "shortlist_announcement": "November (Trimester 1) / April (Trimester 2)",
            "final_result_acceptance_deadline": "Mid-December / Mid-May",
            "visa_application_window": "December - January / May - June",
            "semester_commencement": "Trimester 1 (February) / Trimester 2 (July)",
            "annual_cycle_notes": "Main intake is Trimester 1 (February commencement; applications close mid-August). Applications open year-round."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Australian Honours 1 equivalence, Bachelor's/Master's GPA)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated for HDR research awards)",
            "research_experience_weight": "45% (Peer-reviewed journal publications, citations, research thesis quality)",
            "work_experience_weight": "5% (Industry R&D experience in relevant field)",
            "personal_statement_weight": "0% (Not separately weighted)",
            "recommendations_weight": "5% (Referee ratings on research capability)",
            "interview_weight": "0% (Supervisor endorsement serves as interview validation)",
            "test_scores_weight": "0% (English meets required benchmark)",
            "financial_need_weight": "0% (Purely merit and research output based)",
            "selection_panel_composition": "Faculty HDR Committee, School Postgraduate Coordinators, and Deakin Graduate Research Academy Board.",
            "evaluation_methodology": "Strict metric-driven scoring based on H1 equivalence calculation, verified research track record (Scopus/WoS publications), and supervisor sponsorship."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 international doctoral applicants globally across both trimesters",
            "total_scholarships_awarded": "~120 to 160 comprehensive DUPRS awards annually",
            "acceptance_rate_global": "~4.0% to 5.0%",
            "acceptance_rate_pakistan": "~6.0% among applicants possessing at least 1-2 Scopus Q1/Q2 journal papers",
            "typical_successful_applicant_gpa": "CGPA 3.65+ / 4.00 or 80%+ aggregate with First Class Honours from leading Pakistani universities (NUST, GIKI, PIEAS, FAST, QAU, UET)",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, at least 1-2 first-author papers in high-impact international journals, and a strong supervisory endorsement.",
            "common_backgrounds_of_winners": "Graduates of premier Pakistani engineering and science universities.",
            "high_representation_countries": "China, India, Pakistan, Iran, Vietnam, Germany, Italy, UK.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents advertising guaranteed Australian scholarships or visa packages.",
                "Applications are processed exclusively through deakin.edu.au."
            ],
            "application_fee_warning": "Applying with supervisor endorsement is free of charge; never pay agent fees.",
            "agent_and_intermediary_warnings": "Deakin does not work with third-party agencies for doctoral research scholarship distribution.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application charge: ~AUD 1,600 (~PKR 296,000).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Biometrics, health examination in Pakistan (IOM clinic): ~PKR 40,000.",
                "Degree attestation in Pakistan (HEC and MoFA): ~PKR 25,000 to 35,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without contacting a professor first. Reality: In Australia, an application without an agreed supervisor is immediately rejected.",
                "Myth: Work experience substitutes for lack of research papers. Reality: The scoring system is heavily weighted toward peer-reviewed journal papers and academic thesis grades."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums claim high school marks are evaluated; for PhD, only Bachelor's (Honours) and Master's research outputs are scored."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic research progress and successfully pass the Candidature Confirmation milestone within 12 months.",
            "attendance_requirements": "Full-time on-campus research commitment; standard leave entitlements (20 days annual recreation leave).",
            "academic_progress_monitoring": "Annual Progress Review (APR) evaluated by the supervisory committee and School Postgraduate Coordinator; unsatisfactory progress leads to termination.",
            "work_restrictions_during_study": "Part-time work permitted (teaching or research assistantships) up to 8-10 hours per week during normal business hours, provided it does not impede PhD progress.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Australian Temporary Graduate Visa (Subclass 485 - post-study work stream).",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship terminated if candidature is discontinued or scholar is dismissed for academic misconduct.",
            "rules_for_changing_university": "Non-transferable to other Australian universities.",
            "rules_for_changing_major": "Changing research topic requires formal approval of the supervisory committee and Graduate Research Academy.",
            "extension_policy": "Maximum extension of up to 6 months for PhD scholarships permitted in exceptional circumstances with documented research delays."
        },
        "official_sources_verified": [
            {
                "source_name": "Deakin University Research Scholarships Portal",
                "source_url": "https://www.deakin.edu.au/study/fees-and-scholarships/scholarships/find-a-scholarship/deakin-university-postgraduate-research-scholarship-duprs",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Deakin Graduate Research Academy",
                "source_url": "https://www.deakin.edu.au/research/research-degrees-and-phd",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-OC-019": {
        "scholarship_id": "SCH-OC-019",
        "basic_details": {
            "scholarship_name": "University of Otago International Doctoral Research Scholarships",
            "offering_entity": "University of Otago & Otago Graduate Research School",
            "host_country": "New Zealand",
            "host_institutions_covered": "University of Otago (Dunedin Main Campus, South Island, New Zealand)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all doctoral disciplines across Division of Sciences (Computer Science, Data Science, Ecology, Zoology, Chemistry, Physics, Marine Science, Mathematics), Division of Health Sciences (Biomedical Sciences, Pharmacology, Public Health), Division of Humanities, and Otago School of Business.",
            "number_of_awards_total": "~180 to 220 prestigious doctoral scholarships awarded annually across all academic divisions",
            "number_of_awards_pakistan": "Open international competition; Pakistani doctoral researchers with strong research master's records secure ~8 to 15 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 36 months (3 years) of full-time doctoral research, subject to satisfactory annual progress reports"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to outstanding domestic and international applicants globally (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated purely on academic distinction and demonstrated research capability.",
            "academic_qualifications": "4-year Bachelor's degree with First Class Honours, or research Master's degree (minimum 18 years education) with a substantial thesis component (at least 1 full year or 90 credits of research) from an HEC-recognized university with high academic achievement (minimum 80% aggregate or CGPA 3.60 / 4.00; competitive admits typically 3.75+ / 4.00 or Grade A average).",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Equivalent to Otago GPA of 8.0 on a 9-point scale (First Class Honours / A grade average).",
            "subject_background_prerequisites": "Relevant undergraduate/master's degree corresponding directly to the applied research discipline.",
            "current_education_status": "Master's students in their final semester can apply conditionally with thesis submission proof.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Substantial research experience, first-author journal publications (Scopus/Web of Science), or conference presentations are decisive.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (minimum 6.0 in each subtest) or TOEFL iBT minimum 90 (minimum 21 in writing). Official test score report is mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure supervisory consent from an Otago academic department before submitting.",
            "previous_scholarship_restrictions": "Cannot hold another major full scholarship simultaneously.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full tuition fee waiver for 36 months of doctoral research at the domestic student rate (NZD 9,500 to 11,500 / year value; under NZ government policy, international PhD students pay the subsidized domestic fee rate).",
                "amount": "100% covered (~NZD 10,500 / year; ~PKR 1,785,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "Otago doctoral admissions and scholarship applications are completely free of charge.",
                "amount": "NZD 0 (100% free)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "University of Otago graduate flats (Hayward, Abbey College) or private student rental housing in Dunedin (average NZD 180 to 250 / week; ~USD 110 to 155 / week) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~NZD 900 / month; ~PKR 153,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Tax-free living stipend: NZD 32,500 / year (~USD 20,000 / year; NZD 2,708 / month; ~PKR 460,400 / month) for 36 months.",
                "amount": "NZD 32,500 / year (NZD 2,708 / mo; ~PKR 460,400 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel expenses between Pakistan and Dunedin are self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 250,000 to 350,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "New Zealand Fee Paying Student Visa application fee (~NZD 430) paid by the scholar.",
                "amount": "Not covered (~NZD 430; ~PKR 73,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Mandatory Studentsafe-Inbound University comprehensive medical and travel insurance policy (~NZD 800 / year), paid out of the monthly living stipend.",
                "amount": "Paid from stipend (~NZD 800 / year)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Dunedin are very reasonable compared to Auckland/Wellington; easily covered by the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Student Services Fee waiver (NZD 1,000 / year value) plus full access to Otago Central Library, high-performance computing clusters, and laboratory facilities.",
                "amount": "100% covered institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Departmental research funding and travel grants (up to NZD 2,500) available for presenting papers at peer-reviewed international conferences.",
                "amount": "Up to NZD 2,500 conference travel grant"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Dunedin is a compact, walkable student city; bus transit paid from stipend (~NZD 40/month with Bee Card).",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 30000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (University of Otago, New Zealand)",
            "participating_institutions": [
                "University of Otago (Dunedin Main Campus, South Island, New Zealand)"
            ],
            "university_rankings_scope": "QS World University Rankings #214 worldwide, New Zealand's first university (founded 1869), globally acclaimed in Biomedical Sciences, Public Health, Marine Science, and Computing.",
            "available_majors": [
                "Computer Science and Data Science",
                "Biomedical Sciences and Pharmacology",
                "Marine Science and Oceanography",
                "Ecology and Zoology",
                "Chemistry and Applied Chemistry",
                "Physics and Energy Science",
                "Mathematics and Statistics",
                "Public Health and Epidemiology",
                "Psychology and Neuroscience",
                "Economics and International Business"
            ],
            "english_taught_program_availability": True,
            "program_duration": "3 years (36 months full-time PhD)",
            "admission_requirements_summary": "Online Otago eVision application, supervisor confirmation statement, certified Bachelor's and Master's transcripts and degree certificates, research proposal, curriculum vitae, official IELTS/TOEFL score report, two academic referee reports, and sample publications.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Biomedical Sciences, Health Sciences, and Marine Science are premier research faculties with strong international reputations; Computer Science has strong laboratory capacity; securing a primary supervisor's endorsement is decisive.",
            "strategic_program_match_advice": "Reach out to potential supervisors 3-4 months before submitting. Provide an academic CV highlighting peer-reviewed papers and a concise 2-page research draft aligned with their lab's current Marsden Fund or MBIE projects."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.otago.ac.nz/graduate-research/scholarships/index.html & https://www.otago.ac.nz/study/enrolment/",
            "portal_system_name": "Otago eVision Student Management Portal",
            "account_creation_instructions": "Contact potential supervisor to obtain agreement. Create account on Otago eVision, select PhD program, and tick the box for 'University of Otago Doctoral Scholarship'.",
            "step_by_step_workflow": [
                "Step 1: Identify prospective supervisors via Otago Research directory with CV and research abstract.",
                "Step 2: Obtain formal written supervisory endorsement from the Otago academic.",
                "Step 3: Take IELTS (min 6.5) or TOEFL (min 90) and verify scores meet Otago HDR English requirements.",
                "Step 4: Register on Otago eVision, select PhD program, and indicate scholarship application.",
                "Step 5: Upload supervisor endorsement, research proposal, certified transcripts, degrees, CV, and published papers.",
                "Step 6: Referees submit online evaluation forms via automated institutional links.",
                "Step 7: Departmental and Divisional Postgraduate Committees rank candidates based on academic merit and research record.",
                "Step 8: Graduate Research School issues scholarship and admission offer letters.",
                "Step 9: Accept the award, apply for New Zealand Student Visa, and commence research in Dunedin (flexible commencement dates throughout the year)."
            ],
            "university_vs_scholarship_routing": "Integrated Track: The scholarship application is processed simultaneously with the PhD admission application.",
            "recommendation_letters_submission_method": "Submitted online by referees via automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement outlining research background, motivations for doctoral study at Otago, and career aspirations.",
            "study_plan_research_proposal_requirements": "Structured 3 to 5-page research proposal detailing research objectives, methodology, theoretical significance, and alignment with Otago research groups.",
            "cv_format_requirements": "Academic CV detailing qualifications, publications (with DOI, impact factor, and authorship role), and awards.",
            "interviews_conducted": True,
            "interview_format_details": "Online video interview conducted by prospective primary supervisor prior to issuing supervisory endorsement.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 90) mandatory; GRE not required.",
            "application_fee_amount": "NZD 0 (100% Free)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and verified by issuing universities; certified color scans required.",
            "translation_requirements": "Certified English translation required for any documents not in English.",
            "final_submission_method": "100% digital submission via the Otago eVision portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Supervisor Endorsement / Support Statement",
                "mandatory": True,
                "specification": "Official written statement from an accredited Otago academic agreeing to supervise the candidate.",
                "pakistan_specific_instruction": "Crucial requirement; applications without supervisor agreement are not assessed."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's and Master's transcripts and degree certificates with grading scale.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan with Otago GPA equivalence explanation."
            },
            {
                "document_name": "Doctoral Research Proposal",
                "mandatory": True,
                "specification": "Detailed 3-5 page research proposal agreed upon with prospective supervisor.",
                "pakistan_specific_instruction": "Ensure high academic rigor and direct alignment with Otago faculty strengths."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 90).",
                "pakistan_specific_instruction": "Must be valid within 2 years of proposed commencement date."
            },
            {
                "document_name": "Two Academic Referee Reports",
                "mandatory": True,
                "specification": "Submitted directly by university professors who supervised previous research thesis.",
                "pakistan_specific_instruction": "Must be sent from official institutional email addresses."
            },
            {
                "document_name": "Curriculum Vitae and Published Papers",
                "mandatory": True,
                "specification": "Academic CV including full-text PDFs of peer-reviewed journal/conference publications.",
                "pakistan_specific_instruction": "Highlight papers indexed in Scopus, IEEE Xplore, or Web of Science."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Open year-round (Continuous Admissions)",
            "application_deadline": "Continuous / Any time of the year (Recommended 4-6 months before desired start)",
            "university_admission_deadline": "Continuous / Flexible",
            "document_submission_deadline": "Continuous / Flexible",
            "recommendation_letters_deadline": "Within 2 weeks of application submission",
            "interview_period": "Conducted informally during supervisor outreach stage",
            "shortlist_announcement": "Assessed monthly by the Doctoral Scholarships Committee",
            "final_result_acceptance_deadline": "Within 2 months of offer issuance",
            "visa_application_window": "2-3 months prior to arrival",
            "semester_commencement": "Flexible commencement (any month upon supervisor agreement)",
            "annual_cycle_notes": "Continuous year-round application processing. Unlike Australian universities with fixed rounds, Otago evaluates PhD scholarship applications monthly."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Bachelor's and Master's GPA, Grade A average equivalent)",
            "extracurricular_and_leadership_weight": "0% (Not evaluated for HDR research awards)",
            "research_experience_weight": "40% (Master's thesis quality, peer-reviewed publications, and citations)",
            "work_experience_weight": "5% (Industry R&D experience in relevant field)",
            "personal_statement_weight": "0% (Not separately weighted)",
            "recommendations_weight": "10% (Academic referee assessments on research potential)",
            "interview_weight": "5% (Supervisor assessment during interview)",
            "test_scores_weight": "0% (English meets required benchmark)",
            "financial_need_weight": "0% (Purely merit and research output based)",
            "selection_panel_composition": "Departmental Research Committee, Divisional Postgraduate Board, and Otago Doctoral Scholarships Committee chaired by the Dean of Graduate Research.",
            "evaluation_methodology": "Rigorous academic ranking: GPA calculation (minimum 8.0/9.0) plus research publication evaluation and supervisor support."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,500 international doctoral applicants globally across the year",
            "total_scholarships_awarded": "~180 to 220 comprehensive doctoral scholarships awarded annually",
            "acceptance_rate_global": "~7.0% to 9.0%",
            "acceptance_rate_pakistan": "~8.0% to 10.0% among applicants possessing an A-grade research Master's and publications",
            "typical_successful_applicant_gpa": "CGPA 3.70+ / 4.00 or 80%+ aggregate with First Class Honours from leading Pakistani universities (NUST, QAU, GIKI, PIEAS, FAST, UET)",
            "typical_academic_and_research_profile": "Graduates with exceptional academic records, at least 1-2 first-author papers in high-impact international journals, and an engaged supervisory team.",
            "common_backgrounds_of_winners": "Graduates of premier Pakistani science and engineering universities.",
            "high_representation_countries": "New Zealand, China, India, Pakistan, UK, USA, Germany, South Africa.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of unauthorized agents advertising guaranteed New Zealand scholarships or visa packages.",
                "Applications are processed exclusively through otago.ac.nz."
            ],
            "application_fee_warning": "Applying for admission and scholarship at Otago is 100% free; never pay agent fees.",
            "agent_and_intermediary_warnings": "Otago does not work with third-party agencies for doctoral research scholarship distribution.",
            "hidden_costs_breakdown": [
                "New Zealand Student Visa application fee: ~NZD 430 (~PKR 73,000).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Medical checkup and chest X-ray at authorized panel clinic in Pakistan: ~PKR 25,000.",
                "One-way / round-trip flight from Pakistan to Dunedin: ~PKR 250,000 to 350,000."
            ],
            "misleading_claims_debunked": [
                "Myth: International PhD students pay exorbitant international tuition in New Zealand. Reality: Under NZ government policy, all international PhD students pay the heavily subsidized domestic tuition rate (which is 100% waived by the scholarship).",
                "Myth: You can apply without contacting a professor first. Reality: An application without an agreed supervisor is not approved."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial forums claim fixed deadlines; Otago operates continuous year-round admissions for doctoral degrees."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory academic research progress and successfully pass the 6-month and 12-month Confirmation of Candidature milestones.",
            "attendance_requirements": "Full-time on-campus research commitment; standard annual recreation leave (20 working days).",
            "academic_progress_monitoring": "Annual Progress Report (APR) evaluated by the supervisory committee and Dean of the Graduate Research School; unsatisfactory progress leads to termination.",
            "work_restrictions_during_study": "Part-time work permitted (demonstrating, tutoring, or research assistantships) up to 10 hours per week (500 hours per year), provided it does not impede PhD progress.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the New Zealand Post-Study Work Visa (up to 3 years).",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation.",
            "repayment_clawback_conditions": "Scholarship terminated if candidature is discontinued or scholar is dismissed for academic misconduct.",
            "rules_for_changing_university": "Non-transferable to other New Zealand universities.",
            "rules_for_changing_major": "Changing research topic requires formal approval of the supervisory committee and Graduate Research School.",
            "extension_policy": "Maximum extension of up to 6 months for PhD scholarships permitted in exceptional circumstances with documented research delays."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Otago Doctoral Scholarships Portal",
                "source_url": "https://www.otago.ac.nz/graduate-research/scholarships/index.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "University of Otago Graduate Research School",
                "source_url": "https://www.otago.ac.nz/graduate-research/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
