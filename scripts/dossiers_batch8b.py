"""
scripts/dossiers_batch8b.py
Exhaustive 11-Dimension Verified Scholarship Intelligence Dossiers - Batch 8B
Contains the final 3 Oceania (Australia) Scholarships:
28. SCH-OC-007: Monash University Graduate Research Scholarship (MGRS) / Research Training Program (RTP) (Australia)
29. SCH-OC-008: University of Western Australia (UWA) Forrest Research Foundation PhD Scholarship & RTP (Australia)
30. SCH-OC-009: University of Adelaide Research Scholarship (ADRS) / AGRTP (Australia)
"""

DOSSIERS_BATCH8B = {
    # 28. Monash University Graduate Research Scholarship (MGRS) / RTP (SCH-OC-007)
    "SCH-OC-007": {
        "scholarship_id": "SCH-OC-007",
        "basic_details": {
            "scholarship_name": "Monash University Graduate Research Scholarship (MGRS) & Australian Government Research Training Program (RTP)",
            "offering_entity": "Monash University (Melbourne, Australia) & Australian Government Department of Education (RTP)",
            "host_country": "Australia",
            "host_institutions_covered": "Monash University (Clayton, Caulfield, Parkville, Peninsula Campuses, Melbourne, Victoria, Australia)",
            "degree_levels": ["Master's by Research", "Doctoral / PhD"],
            "major_restrictions": "Open to all academic faculties: Faculty of Information Technology (Computer Science, Artificial Intelligence, Cybersecurity, Software Engineering, Data Science), Faculty of Engineering (Mechanical, Electrical, Chemical, Civil, Materials), Faculty of Medicine, Nursing and Health Sciences, Faculty of Science, Monash Business School, Faculty of Arts, Faculty of Law, Faculty of Pharmacy and Pharmaceutical Sciences (QS World #2 in Pharmacy), Faculty of Art, Design and Architecture, and Faculty of Education.",
            "number_of_awards_total": "~800 to 1,000 active research scholars concurrently supported; ~250 to 350 international scholarships awarded annually",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani researchers with H1 equivalence and publications are well-represented (typically 15 to 25 scholarships awarded/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD (with possible 6-month extension to 4.0 years upon academic justification); up to 2.0 years for Master's by Research"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international applicants of all nationalities outside Australia and New Zealand"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Monash H1 (First Class Honours) equivalence: 4-year Bachelor's degree (16 years education) with final-year research thesis graded at 80%+, or a 2-year Master's degree (18 years education) with at least a 25% research thesis component graded at 80%+.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Equivalence of Monash H1 standard (80%+ average in thesis and overall degree, or 3.70+ / 4.00 CGPA from Pakistani institutions such as NUST, FAST-NUCES, LUMS, QAU, UET, AKU).",
            "subject_background_prerequisites": "Relevant undergraduate or postgraduate qualification in the proposed research discipline with verified research methodology training.",
            "current_education_status": "Graduated or currently in final semester of degree graduating prior to the commencement intake.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Relevant research experience, peer-reviewed journal papers (Q1/Q2), and high-tier international conferences greatly boost competitive ranking score.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (minimum 6.0 in each band) or TOEFL iBT 79 (Reading 13, Listening 12, Speaking 18, Writing 21) or PTE Academic 58 (communicative skills 50+)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite graduate researchers across computing, AI, engineering, pharmacy, medicine, and social sciences.",
            "previous_scholarship_restrictions": "Must not be concurrently holding another full government or university scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "International Tuition Fee Offset covers 100% of international tuition fees for the standard duration of the research program.",
                "amount": "100% covered (~AUD $46,000 to $54,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "No application fee charged for graduate research degree and scholarship applications through the Monash Graduate Research portal.",
                "amount": "AUD $0 (Waived)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid out of living stipend; on-campus Clayton halls or off-campus Melbourne rental apartments.",
                "amount": "Stipend allocation (~AUD $1,200 to $1,800 / month)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "MGRS / RTP living allowance stipend indexed annually at approx AUD $35,013 to $37,000 / year tax-free (~AUD $2,918 to $3,083 / month).",
                "amount": "AUD $35,013 to $37,000 / year (~PKR 6,450,000 to 6,800,000 / year)"
            },
            "airfare": {
                "status": "PARTIALLY_COVERED",
                "details": "Relocation allowance provided: up to AUD $1,500 for single scholar (or AUD $2,000 for family) towards flight tickets to Melbourne.",
                "amount": "AUD $1,500 (~PKR 275,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Student Visa (Subclass 500) application fee paid directly by the applicant to Home Affairs.",
                "amount": "AUD $1,600 (~PKR 295,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Single Overseas Student Health Cover (OSHC) policy paid for the full duration of the student visa.",
                "amount": "AUD $3,200 to $4,000 value (100% covered)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living and meal expenses covered by living allowance stipend.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Faculties provide annual research operational funds ($1,500 - $3,000/yr), workstation, HPC computing cluster access, and lab consumables.",
                "amount": "AUD $1,500 to $3,000 / year research support"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Monash Graduate Education and faculties provide Postgraduate Travel Grants (up to AUD $2,500 to $4,000) for international conferences.",
                "amount": "Up to AUD $4,000 over candidature"
            },
            "travel_transit_allowance": {
                "status": "INCLUDED_IN_RELOCATION",
                "details": "Included in the relocation allowance grant.",
                "amount": "AUD $1,500 relocation allowance"
            },
            "total_estimated_value_usd_per_year": 58000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution (Monash University, Melbourne, Australia - Group of Eight, QS World Rank #37)",
            "participating_institutions": ["Monash University (Clayton, Caulfield, Parkville, Peninsula Campuses)"],
            "university_rankings_scope": "Global Top 40 (QS #37, US News #35, THE #54 globally; #2 globally in Pharmacy/Pharmacology)",
            "available_majors": [
                "Computer Science",
                "Artificial Intelligence & Machine Learning",
                "Data Science & Cybersecurity",
                "Software Systems Engineering",
                "Electrical & Computer Systems Engineering",
                "Mechanical & Aerospace Engineering",
                "Chemical & Biological Engineering",
                "Civil Engineering",
                "Materials Science & Engineering",
                "Medicine, Nursing & Health Sciences",
                "Public Health & Epidemiology",
                "Biological Sciences & Genetics",
                "Chemistry & Nanotechnology",
                "Physics & Astronomy",
                "Pharmacy & Pharmaceutical Sciences",
                "Banking, Finance & Econometrics",
                "Management & Marketing",
                "Law & Human Rights",
                "Media, Communications & Cultural Studies",
                "Education & Educational Psychology"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Doctor of Philosophy (PhD): 3.5 to 4 years; Master of Philosophy (MPhil) / Research Master's: 2 years.",
            "admission_requirements_summary": "H1 equivalence (80%+ or 3.7+ CGPA), approved research proposal, documented prior research output (thesis and/or published articles), two academic referees, and formal faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Faculty of IT and Engineering have massive research funding but demanding publication thresholds; Pharmacy and Medicine require exact laboratory alignment; Arts and Business emphasize theoretical rigor.",
            "strategic_program_match_advice": "Never submit a cold application. Identify 2-3 potential Monash supervisors using 'Find an Expert', examine their recent publications, send a tailored email with a 2-page research outline and CV, obtain their written agreement to supervise, and receive an official Faculty Expression of Interest (EOI) Invitation before lodging the formal portal application."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.monash.edu/admissions/apply/graduate-research",
            "portal_system_name": "Monash Graduate Research Admissions and Scholarship Portal (my.app)",
            "account_creation_instructions": "Register an account on the Monash Graduate Research portal and select the 'Admission and Scholarship' combined pathway.",
            "step_by_step_workflow": [
                "Step 1: Verify Minimum Entry Requirements (Monash H1 equivalence: 80%+ research thesis or bachelor degree).",
                "Step 2: Find a Supervisor via Monash 'Find an Expert' or Faculty Research Supervisor Directory.",
                "Step 3: Submit Faculty Expression of Interest (EOI) or email potential supervisor with CV, academic transcripts, and 2-page research concept note.",
                "Step 4: Receive formal 'Invitation to Apply' from the relevant Monash Faculty Graduate Research office.",
                "Step 5: Prepare required documentation (transcripts, degree certificates, grading scale, English test report, research proposal, CV, referee contact details).",
                "Step 6: Lodge formal application via Monash online application portal selecting 'Combined Candidature and Scholarship Application'.",
                "Step 7: Referees receive automated email prompts to submit confidential assessment reports online.",
                "Step 8: Faculty and University Graduate Research Committee (GRC) rank applications in central competitive scoring round.",
                "Step 9: Receive formal Offer Letter (Course Offer + Scholarship Award Letter with OSHC and stipend terms).",
                "Step 10: Formally accept scholarship offer, receive Confirmation of Enrolment (CoE), and lodge Australian Student Visa (Subclass 500)."
            ],
            "university_vs_scholarship_routing": "Fully integrated: ticking 'Yes' to scholarship consideration on the Monash Graduate Research application automatically enters applicant into central MGRS and RTP scholarship scoring.",
            "recommendation_letters_submission_method": "Two referee reports submitted electronically via Monash's confidential referee online portal.",
            "personal_statement_prompts": "Research Motivation Statement and alignment with Monash research priority areas embedded in proposal.",
            "study_plan_research_proposal_requirements": "Formal research proposal of 1,000 to 1,500 words detailing: Project Title, Research Background, Aims/Objectives, Methodology, Significance/Innovation, and Reference list, agreed upon with prospective supervisor.",
            "cv_format_requirements": "Academic CV detailing: educational credentials, thesis titles and grades, full citations of publications (indexing whether Scopus/Web of Science Q1/Q2), research projects, awards, and technical skills.",
            "interviews_conducted": True,
            "interview_format_details": "Informal technical interview conducted via Zoom by the prospective supervisory team prior to supporting the application; formal university committee rarely conducts separate interviews.",
            "standardized_tests": "IELTS Academic (6.5+, 6.0 each band) or TOEFL iBT (79+); GRE/GMAT not required.",
            "application_fee_amount": "AUD $0 (No fee for Monash Graduate Research applications)",
            "attestation_requirements": "Color scanned original documents required at application; certified copies or verified originals required upon enrolment.",
            "translation_requirements": "Official certified English translations required for all non-English documents.",
            "final_submission_method": "100% online through Monash Graduate Research portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Biographical Page",
                "mandatory": True,
                "specification": "Clear color scan of valid international passport with at least 12 months validity.",
                "pakistan_specific_instruction": "Ensure name spelling exactly matches CNIC, matriculation, and university degrees."
            },
            {
                "document_name": "Official Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts and degrees for 4-year Bachelor's and 2-year Master's showing all semesters, courses, and grades.",
                "pakistan_specific_instruction": "Degrees and transcripts must be attested by the Higher Education Commission (HEC) Pakistan."
            },
            {
                "document_name": "Grading Scale and H1 Equivalence Documentation",
                "mandatory": True,
                "specification": "Official grading scale document from university registrar defining GPA/percentage conversion and first-class criteria.",
                "pakistan_specific_instruction": "Obtain official grading system extract from university registrar confirming H1 equivalence."
            },
            {
                "document_name": "Evidence of Research Achievement / Honours Equivalence",
                "mandatory": True,
                "specification": "Official letter or thesis abstract showing completion of research thesis with grade/marks (minimum 25% research component).",
                "pakistan_specific_instruction": "Submit Master's thesis completion certificate and grade verification letter signed by Dean/HoD."
            },
            {
                "document_name": "Reprints of Peer-Reviewed Publications",
                "mandatory": False,
                "specification": "PDF reprints of published journal papers or conference proceedings with DOI, ISSN, and Scopus/WoS indexing proof.",
                "pakistan_specific_instruction": "Include evidence of Q1/Q2 journal ranking or IEEE/ACM conference indexing."
            },
            {
                "document_name": "Detailed Research Proposal",
                "mandatory": True,
                "specification": "1,000 to 1,500 word research proposal developed in consultation with prospective Monash supervisor.",
                "pakistan_specific_instruction": "Structure with clear methodology, feasibility, and alignment with Monash research priorities."
            },
            {
                "document_name": "Faculty Invitation to Apply / Supervisor Support Letter",
                "mandatory": True,
                "specification": "Official Faculty Invitation to Apply email or written endorsement letter from prospective Monash supervisor.",
                "pakistan_specific_instruction": "Crucial prerequisite: applications submitted without faculty supervisor agreement will be rejected."
            },
            {
                "document_name": "Comprehensive Academic Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "2 to 3 page academic CV detailing education, publications, research experience, technical skills, and references.",
                "pakistan_specific_instruction": "Use professional academic format highlighting thesis topics, GPA, and publication citations."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS Academic (overall 6.5, min 6.0 in each band) or TOEFL iBT (79+) test report.",
                "pakistan_specific_instruction": "Test score must be valid at the time of course commencement."
            },
            {
                "document_name": "Two Confidential Academic Referee Reports",
                "mandatory": True,
                "specification": "Confidential referee appraisals submitted directly through Monash online referee portal.",
                "pakistan_specific_instruction": "Select former thesis supervisor and senior professor who can attest to independent research capability."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Round 1 opens: 1 September; Round 3 opens: 1 April",
            "application_deadline": "Round 1 International Deadline: 31 March (for July-August intake); Round 3 International Deadline: 31 August (for Feb-March intake)",
            "university_admission_deadline": "Coincides with scholarship round closing deadlines (31 March and 31 August)",
            "document_submission_deadline": "Must be uploaded by the round closing deadline",
            "recommendation_letters_deadline": "Referees given 7-10 days past round deadline to submit reports",
            "interview_period": "Ongoing during supervisor consultation prior to round closing",
            "shortlist_announcement": "Round 1 outcomes: late May to June; Round 3 outcomes: late October to November",
            "final_result_acceptance_deadline": "Within 21 days of receiving official scholarship offer",
            "visa_application_window": "June - July for mid-year intake; November - January for early-year intake",
            "semester_commencement": "Enrolment period 1 (February/March) or Enrolment period 2 (July/August)",
            "annual_cycle_notes": "Two major international scholarship rounds per year: Round 1 closes 31 March; Round 3 closes 31 August."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Academic achievement, GPA/percentage, H1 equivalence scoring)",
            "extracurricular_and_leadership_weight": "5% (Professional awards, leadership in science/community)",
            "research_experience_weight": "35% (Prior master's/undergrad thesis quality, first-author peer-reviewed journal articles, conference papers)",
            "work_experience_weight": "5% (Industry R&D experience or academic research assistant experience)",
            "personal_statement_weight": "5% (Clarity of research intent and institutional fit)",
            "recommendations_weight": "5% (Referee assessments on independent research ability)",
            "interview_weight": "Not numerically scored; supervisor endorsement prerequisite",
            "test_scores_weight": "Threshold requirement (English proficiency meet/fail)",
            "financial_need_weight": "0% (Exclusively merit and research excellence-based)",
            "selection_panel_composition": "Faculty Graduate Research Committee, Dean of Graduate Studies, and Monash Central Scholarship Selection Panel.",
            "evaluation_methodology": "Monash University employs a centralized research score algorithm that calculates an applicant's 'H1 Equivalence (H1E)' score based on coursework GPA, thesis grade, and verified peer-reviewed publications. Applications are ranked faculty-by-faculty, and top-tier candidates above the cut-off score receive full MGRS/RTP scholarship offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~6,000 to 8,000 international applicants across both rounds",
            "total_scholarships_awarded": "~250 to 350 international research scholarships annually",
            "acceptance_rate_global": "~4% to 6%",
            "acceptance_rate_pakistan": "~5% (among applicants with confirmed supervisor support and publications)",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (82%+ aggregate) with an H1-graded research thesis",
            "typical_academic_and_research_profile": "Top 5% of class in recognized university (NUST, FAST, LUMS, QAU, UET) with at least 1-2 published papers in Scopus/Web of Science indexed journals or IEEE conferences.",
            "common_backgrounds_of_winners": "MSc/MS graduates in AI, Computer Science, Renewable Energy, Pharmacy, Biomedical Engineering with active research publishing track records.",
            "high_representation_countries": "Pakistan, China, India, Iran, Vietnam, Bangladesh, Malaysia.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Agents demanding money promising 'guaranteed Monash scholarships'. Monash never charges an application fee for PhD/MPhil, and scholarships are awarded solely through faculty ranking."
            ],
            "application_fee_warning": "Monash does NOT charge any application fee for Graduate Research applications. Beware of third parties charging submission fees.",
            "agent_and_intermediary_warnings": "Do not pay education agents to communicate with potential supervisors. Monash professors evaluate prospective students based on their direct intellectual exchange and research capability.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD $1,600).",
                "Medical examination and biometrics in Pakistan (~PKR 45,000 - 55,000).",
                "Initial Melbourne bond/rent deposit before first stipend cycle (AUD $1,500 - $2,500).",
                "Dependents' health cover (OSHC couple/family upgrade is NOT covered; costs AUD $6,000 - $12,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You can apply directly through the general admission portal without supervisor support. (FACT: Research applications without confirmed supervisor endorsement are rejected).",
                "CLAIM: Coursework Master's students are eligible. (FACT: MGRS/RTP is strictly restricted to Higher Degree by Research - MPhil and PhD)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unaccredited websites list obsolete stipend values ($28,000/yr); the official indexed stipend is AUD $35,013 - $37,000/year tax-free."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress and pass formal progression milestones (Confirmation at 12 months, Mid-Candidature Progress Review at 24 months, Final Review at 36 months).",
            "attendance_requirements": "Full-time physical research attendance on Monash Victorian campuses (Clayton, Caulfield, Parkville).",
            "academic_progress_monitoring": "Bi-annual/annual milestone reviews submitted to the Graduate Research Committee.",
            "work_restrictions_during_study": "Monash recommends no more than 6-8 hours of paid work per week during normal business hours so research is not compromised; standard Australian visa conditions apply outside business hours.",
            "home_country_return_obligation": "None. Scholars are free to stay in Australia and apply for the Subclass 485 Temporary Graduate Visa or Skilled Migration.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Scholarship terminates if progress is unsatisfactory or if student withdraws; repayment required only in proven cases of research misconduct or fraud.",
            "rules_for_changing_university": "Non-transferable to another university.",
            "rules_for_changing_major": "Requires supervisory committee and Faculty approval.",
            "extension_policy": "PhD scholars can apply for a maximum 6-month stipend extension based on exceptional academic or research circumstances."
        },
        "official_sources_verified": [
            {
                "source_name": "Monash University Graduate Research Scholarships Official Page",
                "source_url": "https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/graduate-research-scholarship",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact mathematical weighting points per Q1 journal vs. conference paper in faculty H1E calculation formulas.",
                    "Individual country quota breakdown (ranking is unified merit-based across global applicant pool).",
                    "Faculty-specific stipend top-up funding availability and criteria."
                ]
            }
        ]
    },

    # 29. University of Western Australia (UWA) Forrest Research Foundation PhD Scholarship & RTP (SCH-OC-008)
    "SCH-OC-008": {
        "scholarship_id": "SCH-OC-008",
        "basic_details": {
            "scholarship_name": "University of Western Australia (UWA) Forrest Research Foundation PhD Scholarship & Australian Government RTP",
            "offering_entity": "Forrest Research Foundation (endowed by Andrew and Nicola Forrest / Minderoo Foundation) & University of Western Australia (Perth, WA) & Australian Government Department of Education (RTP)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Western Australia (Crawley Campus, Perth, Western Australia - Group of Eight)",
            "degree_levels": ["Doctoral / PhD"],
            "major_restrictions": "All academic disciplines across UWA, with strong emphasis on transformative and visionary research: Oceans Institute & Marine Biology, Computer Science, AI & Autonomous Systems, Energy & Mineral Engineering, Biomedical & Life Sciences (Marshall Centre for Infectious Diseases, Perkins Institute), Agricultural Sciences, Astrophysics & Gravitational Waves (OzGrav), and Law & Humanities.",
            "number_of_awards_total": "Highly exclusive: ~10 to 12 Forrest Scholars selected across Western Australian universities annually (~5 to 8 based at UWA)",
            "number_of_awards_pakistan": "Open global competition; typically 1 to 2 Pakistani scholars win this elite fellowship every 1-2 years based on outstanding academic brilliance and research vision",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD (plus up to 6 months extension subject to academic progress)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to outstanding domestic and international applicants of all nationalities"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "First Class Honours (H1) or equivalent from a recognized university: 4-year Bachelor's degree (16 years education) or Master's degree (18 years education) with exceptional academic record (minimum 85%+ or 3.80+ / 4.00 CGPA) and demonstrated research outputs.",
            "minimum_gpa_percentage": 85.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Equivalence of First Class Honours (H1) with distinction (85%+ aggregate or 3.80+ / 4.00 CGPA from Pakistani institutions like NUST, FAST, LUMS, QAU, AKU, UET).",
            "subject_background_prerequisites": "Outstanding track record in discipline directly related to the proposed PhD project.",
            "current_education_status": "Graduated or in final semester of degree graduating before course commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "High-impact research publications, patents, or significant laboratory/technical innovations strongly expected.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 82,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (all bands 6.0+) or TOEFL iBT 82 (Reading 18, Listening 20, Speaking 20, Writing 22)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Elite doctoral researchers capable of delivering transformative, world-changing research and showing leadership character.",
            "previous_scholarship_restrictions": "Must not be concurrently holding another major research scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full tuition fee scholarship covers 100% of international tuition fees for up to 4 years.",
                "amount": "100% covered (~AUD $44,000 to $52,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "No application fee for UWA PhD and Forrest Research Foundation scholarship applications.",
                "amount": "AUD $0 (Waived)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Forrest Scholars are provided with an accommodation allowance of up to AUD $24,198 per year at Forrest Hall, a state-of-the-art luxury residential facility on the Swan River overlooking UWA campus.",
                "amount": "AUD $24,198 / year accommodation package"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Base RTP living stipend indexed at approx AUD $35,013 to $37,000 / year tax-free PLUS a Forrest Research Foundation top-up stipend of AUD $13,500 / year tax-free. Total living stipend is ~AUD $48,500 to $50,500 / year tax-free (~AUD $4,040 to $4,200 / month).",
                "amount": "AUD $48,500 to $50,500 / year (~PKR 8,900,000 to 9,300,000 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Relocation allowance provided by UWA up to AUD $1,800 to $2,000 for travel to Perth.",
                "amount": "AUD $2,000 (~PKR 370,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Subclass 500 Student Visa fee paid by candidate.",
                "amount": "AUD $1,600 (~PKR 295,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Single Overseas Student Health Cover (OSHC) for primary applicant paid for full visa duration.",
                "amount": "AUD $3,200 to $4,000 value (100% covered)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Covered via the combined AUD $50,000+ annual living stipend.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Forrest Scholars receive a research and travel allowance of up to AUD $12,000 across their PhD candidature.",
                "amount": "Up to AUD $12,000 research & travel fund"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Dedicated Forrest research grant of up to AUD $12,000 plus faculty research travel allowances for international symposiums.",
                "amount": "AUD $12,000 over candidature"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Included in the relocation and travel funds.",
                "amount": "AUD $2,000 relocation allowance"
            },
            "total_estimated_value_usd_per_year": 68000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single primary host (University of Western Australia, Perth - Group of Eight, QS World Rank #77; affiliated with Curtin, Murdoch, ECU)",
            "participating_institutions": ["University of Western Australia (Crawley Campus, Perth)"],
            "university_rankings_scope": "Global Top 80 (QS #77 globally; Member of Australian Group of Eight - Go8; World Top 25 in Mineral & Mining Engineering, Agriculture, and Marine Science)",
            "available_majors": [
                "Computer Science & Artificial Intelligence",
                "Data Science & Quantum Computing",
                "Oceans, Marine Ecology & Blue Economy",
                "Mineral, Energy & Chemical Engineering",
                "Biomedical Sciences & Genetics",
                "Infectious Diseases & Microbiology",
                "Agricultural Science & Plant Biology",
                "Astrophysics, Gravitational Waves & Astronomy",
                "Environmental Science & Climate Systems",
                "Law, Governance & Public Policy",
                "Humanities & Social Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Doctor of Philosophy (PhD): 3.5 to 4 years.",
            "admission_requirements_summary": "Exceptional first-class academic trajectory (H1 with distinction), pre-arranged supervision agreement with a UWA professor, 2-page transformative research concept, evidence of leadership and societal commitment, and top referee reports.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "This is one of the most elite and generous PhD fellowships in the Southern Hemisphere; selection is fiercely competitive across all scientific disciplines.",
            "strategic_program_match_advice": "Prospective candidates must initiate contact with an eminent UWA professor 4-6 months before the deadline. Frame the research proposal around 'transformative impact'—how the project solves a critical global challenge (e.g. climate resilience, clean energy transition, incurable disease, scalable AI safety). Both the UWA supervisor and head of school must enthusiastically sponsor the Forrest nomination."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.forrestresearch.org.au/scholarships/",
            "portal_system_name": "Forrest Research Foundation Application System & UWA Postgraduate Admissions Portal",
            "account_creation_instructions": "Two-step process: Lodge admission application with UWA Graduate Research School and submit Forrest Foundation application via the Forrest online portal.",
            "step_by_step_workflow": [
                "Step 1: Contact potential UWA supervisors whose research aligns with your proposal and secure formal supervisor support.",
                "Step 2: Submit a formal application for PhD candidature at UWA Graduate Research School, indicating intention to apply for Forrest Scholarship.",
                "Step 3: Access the Forrest Research Foundation online application portal and register an account.",
                "Step 4: Prepare the Forrest Application Dossier: 2-page project outline emphasizing transformative impact, leadership & community engagement essay, academic CV, transcripts, and 3 referee nominations.",
                "Step 5: Submit the Forrest application prior to the annual closing date (typically late October).",
                "Step 6: Referees submit independent appraisal reports directly into the Forrest portal.",
                "Step 7: The Forrest Academic Board reviews applications and shortlists 20-25 semi-finalists for formal interviews.",
                "Step 8: Attend high-stakes panel interview (in-person or video link via Zoom) with the Forrest Foundation Selection Committee.",
                "Step 9: Receive final offer of Forrest Research Foundation Scholarship and UWA PhD admission.",
                "Step 10: Accept offer, receive Confirmation of Enrolment (CoE), apply for Australian Student Visa (Subclass 500), and book residence at Forrest Hall."
            ],
            "university_vs_scholarship_routing": "Dual pathway: Applicant must apply to UWA for PhD admission AND submit a dedicated application directly to the Forrest Research Foundation.",
            "recommendation_letters_submission_method": "Three confidential referee reports submitted directly via the Forrest online system.",
            "personal_statement_prompts": "Statement explaining why you wish to be a Forrest Scholar, how your research has transformative potential for Western Australia and the world, and evidence of your leadership and character outside the lab.",
            "study_plan_research_proposal_requirements": "Project description (maximum 2 pages) outlining: Research background, hypothesis, transformative scientific/technological breakthrough potential, methodology, and real-world impact.",
            "cv_format_requirements": "Academic curriculum vitae highlighting publications, patents, conference presentations, awards, and leadership/community service.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous 30-minute panel interview conducted via Zoom with the Forrest Foundation Selection Committee (comprising distinguished academics, industry leaders, and Minderoo Foundation representatives). Focuses on scientific vision, critical thinking, and leadership.",
            "standardized_tests": "IELTS Academic (6.5+, 6.0 all bands) or TOEFL iBT (82+). GRE not required.",
            "application_fee_amount": "AUD $0 (No application fee)",
            "attestation_requirements": "Verified original scanned academic transcripts and degree certificates.",
            "translation_requirements": "Certified English translations required for all non-English documents.",
            "final_submission_method": "Online submission via Forrest Research Foundation application portal and UWA admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Biographical Page",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport with at least 12 months validity.",
                "pakistan_specific_instruction": "Name spelling must exactly match educational certificates and CNIC."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Full certified transcripts and degrees for 4-year Bachelor's and 2-year Master's showing grades and thesis results.",
                "pakistan_specific_instruction": "Attestation by the Higher Education Commission (HEC) Pakistan required."
            },
            {
                "document_name": "Formal UWA Supervisor Support Endorsement Letter",
                "mandatory": True,
                "specification": "Formal written endorsement from prospective UWA supervisor and Head of School committing resources and supervision.",
                "pakistan_specific_instruction": "Must confirm that supervisor will mentor candidate through Forrest candidature."
            },
            {
                "document_name": "Two-page Research Proposal detailing Transformative Impact",
                "mandatory": True,
                "specification": "Max 2-page research proposal detailing project background, methodology, innovation, and global societal impact.",
                "pakistan_specific_instruction": "Highlight transformative scientific potential and practical applicability."
            },
            {
                "document_name": "Leadership and Vision Statement (Forrest Scholar Essay)",
                "mandatory": True,
                "specification": "Essay explaining leadership achievements, broader community contributions, and alignment with Forrest values.",
                "pakistan_specific_instruction": "Showcase leadership in student societies, scientific advocacy, or community initiatives in Pakistan."
            },
            {
                "document_name": "Comprehensive Academic Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed CV listing publications, patents, awards, academic background, and relevant technical capabilities.",
                "pakistan_specific_instruction": "Highlight first-author publications and Q1/Q2 indexing."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "Official IELTS Academic (overall 6.5, min 6.0 in all bands) or TOEFL iBT (82+) test report.",
                "pakistan_specific_instruction": "Test must be valid at time of course commencement."
            },
            {
                "document_name": "Three Confidential Referee Reports",
                "mandatory": True,
                "specification": "Three confidential appraisal reports from academic and professional referees submitted directly to Forrest portal.",
                "pakistan_specific_instruction": "Referees should include Master's thesis supervisor and internationally recognized academics who know your work."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Annual round opens: 1 July / 1 August",
            "application_deadline": "Annual closing deadline: 31 October",
            "university_admission_deadline": "Must apply for UWA PhD admission concurrently by 31 October",
            "document_submission_deadline": "31 October",
            "recommendation_letters_deadline": "Within 7 days of application close",
            "interview_period": "Mid-November to early December",
            "shortlist_announcement": "Mid-December",
            "final_result_acceptance_deadline": "Within 14 days of offer",
            "visa_application_window": "December - February",
            "semester_commencement": "Commence PhD studies in Semester 1 (February/March) or Semester 2 (July/August)",
            "annual_cycle_notes": "One prestigious annual round closing at the end of October each year."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Stellar undergraduate and master's academic transcripts, H1 equivalence, GPA)",
            "extracurricular_and_leadership_weight": "15% (Demonstrated leadership, communication skills, and commitment to wider societal good)",
            "research_experience_weight": "30% (Track record of high-impact research, publications, and conceptual depth)",
            "work_experience_weight": "5% (Relevant industry, laboratory, or technical research experience)",
            "personal_statement_weight": "5% (Compelling leadership essay and alignment with Forrest values)",
            "recommendations_weight": "5% (Exceptional referee ratings on originality, resilience, and intellectual drive)",
            "interview_weight": "Significant decisive factor for shortlisted candidates (evaluates presence, scientific passion, and critical thinking)",
            "test_scores_weight": "Eligibility prerequisite",
            "financial_need_weight": "0% (Purely merit, impact, and excellence based)",
            "selection_panel_composition": "Forrest Foundation Selection Committee, chaired by the Director of the Forrest Research Foundation and featuring eminent scholars from UWA and partner institutions.",
            "evaluation_methodology": "Multi-stage assessment: First-stage technical review filters for H1 excellence and supervisor support. The Academic Board shortlists top ~20 international candidates for rigorous interviews. Final awards are granted to individuals demonstrating both academic brilliance and transformative leadership potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 elite international applicants compete for Forrest awards across all WA universities",
            "total_scholarships_awarded": "~10 to 12 Forrest PhD Scholarships awarded annually (with ~5 to 8 based at UWA)",
            "acceptance_rate_global": "~1.0% to 1.5% (Extremely selective)",
            "acceptance_rate_pakistan": "~1% (Only the most accomplished Pakistani scholars win)",
            "typical_successful_applicant_gpa": "3.85+ / 4.00 CGPA (85%+ aggregate) with multiple first-author publications",
            "typical_academic_and_research_profile": "Top 1-2% graduate from leading university (NUST, FAST, LUMS, QAU) with multiple Q1 journal publications, prestigious medals/awards, and exceptional research vision.",
            "common_backgrounds_of_winners": "Exceptional researchers in artificial intelligence, marine science, biomedical engineering, astrophysics, and clean energy.",
            "high_representation_countries": "Global: Australia, UK, Pakistan, India, USA, Canada, Germany, China.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unscrupulous agents claiming they have 'quotas' for Forrest Scholarships. The selection is run independently by the Forrest Academic Board."
            ],
            "application_fee_warning": "Neither UWA nor the Forrest Research Foundation charges any application fee.",
            "agent_and_intermediary_warnings": "Do not hire agents. Applications must be prepared personally by the candidate in close collaboration with the prospective UWA supervisor.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD $1,600).",
                "Medical examination, chest X-ray, and biometrics in Pakistan (~PKR 45,000 - 55,000).",
                "Dependent health cover and visas (family members are not covered by single OSHC).",
                "Initial personal expenses prior to first monthly stipend deposit."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You can win Forrest Scholarship without a UWA supervisor. (FACT: Applications without strong, committed supervisor endorsement are immediately eliminated).",
                "CLAIM: The scholarship covers coursework master's degrees. (FACT: Exclusively for PhD / Doctor of Philosophy research)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Outdated blogs report old Forrest stipend amounts ($30,000); the current combined package includes an RTP base plus $13,500 top-up plus $24,198 Forrest Hall accommodation package."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain outstanding progress in annual PhD milestones and participate actively in the Forrest Hall collegiate community.",
            "attendance_requirements": "Full-time on-campus residency in Perth and active residence at Forrest Hall (or approved local accommodation).",
            "academic_progress_monitoring": "Annual progress reviews evaluated jointly by the UWA Graduate Research School and the Forrest Academic Director.",
            "work_restrictions_during_study": "Scholars are discouraged from undertaking paid employment exceeding 8 hours/week during business hours to preserve research velocity.",
            "home_country_return_obligation": "None. Forrest Scholars are eligible for the Australian Subclass 485 Temporary Graduate Visa and Global Talent visas.",
            "service_obligations_or_bonds": "None; scholars are expected to participate in Forrest Foundation public lectures, mentoring, and academic community events.",
            "repayment_clawback_conditions": "Scholarship terminates upon academic failure or voluntary abandonment; clawbacks apply only in cases of academic fraud.",
            "rules_for_changing_university": "Restricted to participating Western Australian universities with Board approval.",
            "rules_for_changing_major": "Requires approval from UWA supervisory committee and Forrest Foundation Director.",
            "extension_policy": "Up to 6-month extension can be approved on academic merit."
        },
        "official_sources_verified": [
            {
                "source_name": "Forrest Research Foundation Official Portal",
                "source_url": "https://www.forrestresearch.org.au/scholarships/",
                "source_type": "OFFICIAL_COMMISSION",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Exact numeric score sheet used by interview panel to grade candidates during interviews.",
                    "Specific annual quota allocated between participating universities (UWA vs Curtin vs Murdoch vs ECU).",
                    "Internal ranking formula weighting between published citations vs interview performance."
                ]
            }
        ]
    },

    # 30. University of Adelaide Research Scholarship (ADRS) / AGRTP (SCH-OC-009)
    "SCH-OC-009": {
        "scholarship_id": "SCH-OC-009",
        "basic_details": {
            "scholarship_name": "University of Adelaide Research Scholarship (ADRS) & Australian Government Research Training Program (AGRTP) International",
            "offering_entity": "University of Adelaide (Adelaide, South Australia) & Australian Government Department of Education (AGRTP)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Adelaide (North Terrace, Waite, and Roseworthy Campuses, Adelaide, South Australia - Group of Eight)",
            "degree_levels": ["Master's by Research", "Doctoral / PhD"],
            "major_restrictions": "Open to all disciplines across the University of Adelaide, including the world-renowned Australian Institute for Machine Learning (AIML - ranked #2 globally for computer vision and AI research), School of Computer and Mathematical Sciences, School of Electrical and Mechanical Engineering, School of Chemical Engineering, Waite Research Institute (Agriculture, Plant Breeding, Wine Science), Faculty of Health and Medical Sciences, Faculty of Arts, Business, Law and Economics.",
            "number_of_awards_total": "~150 to 200 major international postgraduate research scholarships awarded annually across faculties",
            "number_of_awards_pakistan": "Open global merit competition; Pakistani researchers in computer science, machine learning, and engineering have a strong success rate (typically 15 to 25 scholarships awarded/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD (with a possible 6-month extension); up to 2.0 years for Master of Philosophy (MPhil)"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international applicants from all countries outside Australia and New Zealand"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Equivalent to Australian First Class Honours (H1): 4-year Bachelor's degree (16 years education) with significant research project/thesis graded at 80%+, or a Master's degree (18 years education) with a minimum 25% research thesis component graded at 80%+.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.7,
            "grading_conversion_notes": "Adelaide H1 equivalence: minimum 80%+ marks or 3.70+ / 4.00 CGPA from recognized Pakistani institutions (NUST, FAST, LUMS, QAU, UET, GIKI, PIEAS, AKU).",
            "subject_background_prerequisites": "Strong academic background in the chosen research discipline with documented research methodology coursework.",
            "current_education_status": "Graduated or currently in final semester of degree graduating before Adelaide semester commencement.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Peer-reviewed journal publications (Q1/Q2 in Scopus/Web of Science) and top conference papers (e.g. CVPR, ICCV, NeurIPS for AIML applicants) provide a decisive competitive advantage in Adelaide's points-based ranking.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 79,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic 6.5 (minimum 6.0 in all bands) or TOEFL iBT 79 (Reading 13, Listening 13, Speaking 18, Writing 21) or PTE Academic 58 (skills 50+)."
            },
            "other_language_requirements": "English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Graduate researchers in AI, Machine Learning, Computer Vision, Defense Technologies, Agriculture, and Health Sciences.",
            "previous_scholarship_restrictions": "Must not be concurrently holding another full government or university scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee waiver provided for the standard duration of the research program.",
                "amount": "100% covered (~AUD $44,000 to $54,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "No fee is charged for Higher Degree by Research (HDR) and scholarship applications at Adelaide.",
                "amount": "AUD $0 (Waived)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Living allowance covers student rental accommodation in Adelaide (one of Australia's most affordable capital cities).",
                "amount": "Paid from monthly stipend (~AUD $1,000 to $1,500 / month)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "ADRS / AGRTP living stipend indexed annually at approx AUD $34,236 to $37,000 / year tax-free (~AUD $2,853 to $3,083 / month).",
                "amount": "AUD $34,236 to $37,000 / year (~PKR 6,300,000 to 6,800,000 / year)"
            },
            "airfare": {
                "status": "PARTIALLY_COVERED",
                "details": "Relocation allowance provided: up to AUD $1,000 for single student (or AUD $2,000 for families) towards travel expenses to Adelaide.",
                "amount": "AUD $1,000 (~PKR 185,000)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Subclass 500 Student Visa fee paid by candidate.",
                "amount": "AUD $1,600 (~PKR 295,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Single Overseas Student Health Cover (OSHC) policy covered for the primary scholarship recipient for standard visa duration.",
                "amount": "AUD $3,200 to $4,000 value (100% covered)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Covered out of living stipend.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Faculties and research centers (like AIML) provide computing clusters, workstations, lab consumables, and project operational funding.",
                "amount": "AUD $1,500 to $3,000 / year research support"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Adelaide Graduate Research School and schools offer conference travel grants (up to AUD $2,000 to $3,500) to present at leading international conferences.",
                "amount": "Up to AUD $3,500 over candidature"
            },
            "travel_transit_allowance": {
                "status": "INCLUDED_IN_RELOCATION",
                "details": "Covered under Adelaide relocation allowance.",
                "amount": "AUD $1,000 relocation allowance"
            },
            "total_estimated_value_usd_per_year": 56000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single institution (University of Adelaide, South Australia - Group of Eight, QS World Rank #82)",
            "participating_institutions": ["University of Adelaide (North Terrace, Waite, and Roseworthy Campuses)"],
            "university_rankings_scope": "Global Top 90 (QS #82 globally, THE #111; Australian Institute for Machine Learning ranked #2 globally in Computer Vision; Waite campus ranked Top 20 for Agricultural Sciences)",
            "available_majors": [
                "Computer Science & Artificial Intelligence (AIML)",
                "Computer Vision & Machine Learning",
                "Cybersecurity & Software Engineering",
                "Electrical & Electronic Engineering",
                "Mechanical & Aerospace Engineering",
                "Chemical Engineering & Sustainable Energy",
                "Agricultural Sciences & Plant Genomics (Waite)",
                "Wine Science & Viticulture",
                "Biomedical Science & Biotechnology",
                "Medicine & Public Health",
                "Pure & Applied Mathematics",
                "Physics & Photonics",
                "Business, Finance & Economics",
                "Law & Social Sciences"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Doctor of Philosophy (PhD): 3.5 to 4 years; Master of Philosophy (MPhil): 2 years.",
            "admission_requirements_summary": "Adelaide H1 equivalence (80%+ or 3.7+ CGPA), approved research proposal, documented prior research output (thesis and publications), supervisor endorsement, and two referee reports.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "AIML (Australian Institute for Machine Learning) is globally renowned and receives immense international interest—applicants need strong mathematical and programming foundations with published conference/journal work; Agricultural and Wine Sciences have exceptional lab facilities with high supervisor receptivity.",
            "strategic_program_match_advice": "Before initiating an application, review Adelaide's 'Researcher Profiles' directory. Email prospective supervisors with your CV, academic transcripts, and a 2-page research outline explaining your methodology. Gain supervisor agreement to supervise; their endorsement letter is indispensable for the scholarship ranking formula."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.adelaide.edu.au/graduate-research/future-students/how-to-apply",
            "portal_system_name": "University of Adelaide Online Application Portal (Adelaide Apply)",
            "account_creation_instructions": "Create an account on the Adelaide Graduate Research online application portal and select 'Admission and Scholarship'.",
            "step_by_step_workflow": [
                "Step 1: Check Minimum Entry and English Language Requirements.",
                "Step 2: Find a supervisor using Adelaide Researcher Profiles and secure written agreement to supervise.",
                "Step 3: Develop a 2-page research proposal in consultation with your prospective supervisor.",
                "Step 4: Gather required documents (degree certificates, transcripts, syllabus/grading scale, English test score, publication reprints, CV).",
                "Step 5: Lodge formal online application through the Adelaide Graduate Research portal selecting 'Apply for Candidature and Scholarship'.",
                "Step 6: Enter contact details for two academic referees (who receive automated notification to submit confidential reports).",
                "Step 7: School and Faculty Graduate Research committees evaluate and rank applications according to Adelaide's centralized scoring matrix.",
                "Step 8: Adelaide Graduate Research School issues scholarship and candidature offer letters.",
                "Step 9: Accept the offer online, receive Confirmation of Enrolment (CoE), and apply for Australian Student Visa (Subclass 500).",
                "Step 10: Arrive in Adelaide and complete orientation and milestone induction."
            ],
            "university_vs_scholarship_routing": "Single unified application: checking the scholarship box automatically submits candidate for both AGRTP and Adelaide ADRS awards.",
            "recommendation_letters_submission_method": "Submitted electronically by referees via Adelaide's secure online referee report portal.",
            "personal_statement_prompts": "Research project description and institutional fit statement within application.",
            "study_plan_research_proposal_requirements": "Research Proposal of 1,000 to 1,500 words containing: Background, Problem Statement, Aims and Objectives, Proposed Methodology, Significance, and Bibliography, endorsed by prospective Adelaide supervisor.",
            "cv_format_requirements": "Comprehensive academic CV detailing publications with full citations, thesis title and grades, software/open-source contributions, awards, and research project summaries.",
            "interviews_conducted": True,
            "interview_format_details": "Informal technical interview conducted via Zoom or Microsoft Teams by the prospective supervisory team (especially at AIML and School of Engineering) to evaluate technical fit.",
            "standardized_tests": "IELTS Academic (6.5+, 6.0 in all bands) or TOEFL iBT (79+); GRE/GMAT not required.",
            "application_fee_amount": "AUD $0 (No application fee for Adelaide HDR applications)",
            "attestation_requirements": "Scanned high-resolution color originals of academic documents required at application; verification of originals upon arrival.",
            "translation_requirements": "Official certified English translations for all non-English documents.",
            "final_submission_method": "100% online through University of Adelaide application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Passport Biographical Page",
                "mandatory": True,
                "specification": "Clear color copy of valid international passport with at least 12 months validity.",
                "pakistan_specific_instruction": "Name spelling must exactly match educational certificates and CNIC."
            },
            {
                "document_name": "Official Academic Transcripts & Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts and degrees for 4-year Bachelor's and 2-year Master's showing all semester grades.",
                "pakistan_specific_instruction": "Attestation by the Higher Education Commission (HEC) Pakistan required."
            },
            {
                "document_name": "Official University Grading Scale",
                "mandatory": True,
                "specification": "Official grading scale document from university registrar defining GPA conversion and first-class honours criteria.",
                "pakistan_specific_instruction": "Submit registrar-issued grading explanation confirming H1 equivalence."
            },
            {
                "document_name": "Proof of Research Performance / Honours Equivalence",
                "mandatory": True,
                "specification": "Official letter or thesis abstract confirming completion of research thesis with grade (minimum 25% research component).",
                "pakistan_specific_instruction": "Submit Master's thesis completion letter signed by department chair."
            },
            {
                "document_name": "Reprints of Peer-Reviewed Publications",
                "mandatory": False,
                "specification": "PDF copies of published journal papers or conference proceedings with DOI, ISSN, and indexing proof.",
                "pakistan_specific_instruction": "Include evidence of Q1/Q2 journal ranking or IEEE/ACM conference indexing."
            },
            {
                "document_name": "Detailed Research Proposal",
                "mandatory": True,
                "specification": "1,000 to 1,500 word research proposal developed in consultation with prospective Adelaide supervisor.",
                "pakistan_specific_instruction": "Must clearly define research questions, methods, and expected contributions."
            },
            {
                "document_name": "Written Evidence of Supervisor Support / Pre-Agreement",
                "mandatory": True,
                "specification": "Formal written agreement from prospective Adelaide supervisor agreeing to supervise the project.",
                "pakistan_specific_instruction": "Mandatory: applications without supervisor support are immediately declined."
            },
            {
                "document_name": "Comprehensive Academic Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic CV listing education, publications, research projects, technical skills, and references.",
                "pakistan_specific_instruction": "Ensure clear formatting highlighting research outputs and academic distinctions."
            },
            {
                "document_name": "English Language Proficiency Score Report",
                "mandatory": True,
                "specification": "Official IELTS Academic (overall 6.5, min 6.0 in all bands) or TOEFL iBT (79+) test report.",
                "pakistan_specific_instruction": "Test must be valid at time of course commencement."
            },
            {
                "document_name": "Two Confidential Academic Referee Reports",
                "mandatory": True,
                "specification": "Confidential referee appraisals submitted directly through Adelaide's online referee report portal.",
                "pakistan_specific_instruction": "Select academic referees who can evaluate research aptitude and analytical competence."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "Major International Round opens: 1 April",
            "application_deadline": "Major International Round closes: 10 July (for commencement in Semester 1 the following year)",
            "university_admission_deadline": "Coincides with scholarship round (10 July)",
            "document_submission_deadline": "10 July",
            "recommendation_letters_deadline": "Within 7 days of application closing",
            "interview_period": "May to July during supervisor interaction",
            "shortlist_announcement": "Outcomes announced in mid-October to early November",
            "final_result_acceptance_deadline": "Within 21 days of receiving scholarship offer",
            "visa_application_window": "November to January",
            "semester_commencement": "Semester 1 (commence between 1 January and 30 June) or Semester 2 (commence between 1 July and 31 August)",
            "annual_cycle_notes": "One primary major international round closing in early July each year for start in the subsequent academic year."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Coursework grades, bachelor/master degree GPA, H1 equivalence)",
            "extracurricular_and_leadership_weight": "5% (Academic prizes, university medals, leadership)",
            "research_experience_weight": "35% (Prior research thesis score, peer-reviewed journal articles, conference papers)",
            "work_experience_weight": "5% (Industry research or laboratory assistantship experience)",
            "personal_statement_weight": "5% (Research proposal quality and alignment with Adelaide strategic priorities)",
            "recommendations_weight": "5% (Referee evaluations on research aptitude)",
            "interview_weight": "Prerequisite supervisor endorsement; not separately quantified",
            "test_scores_weight": "Threshold requirement (English proficiency meet/fail)",
            "financial_need_weight": "0% (Strictly academic and research merit-based)",
            "selection_panel_composition": "Adelaide Graduate Research Committee, Faculty Executive Deans, and Head of Graduate Studies.",
            "evaluation_methodology": "The University of Adelaide uses an objective research scoring matrix. Applicants are assessed on their H1 equivalence, quality and volume of peer-reviewed publications (scoring higher points for Q1/Q2 journal articles and ranked conference proceedings), and research proposal alignment. Top-ranked applicants across faculties are offered ADRS or AGRTP awards."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 international research applicants per year",
            "total_scholarships_awarded": "~150 to 200 international research scholarships annually",
            "acceptance_rate_global": "~4% to 5%",
            "acceptance_rate_pakistan": "~5% to 6% (among qualified applicants with publications and supervisor endorsement)",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (82%+ aggregate) with high thesis grades",
            "typical_academic_and_research_profile": "Top 5% graduate from leading university (FAST, NUST, LUMS, QAU, UET) with 1-2 published papers in reputable journals or international conferences, especially in AI/AIML.",
            "common_backgrounds_of_winners": "MSc/MS graduates in AI, Computer Science, Renewable Energy, Agriculture/Plant Breeding, and Biomedical Engineering.",
            "high_representation_countries": "Pakistan, China, India, Iran, Vietnam, Bangladesh, Nigeria.",
            "competitiveness_tier": "VERY_HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Fraudulent recruitment agents claiming they can secure Adelaide scholarships for a fee. Adelaide evaluates all candidates through official faculty and GRC committees."
            ],
            "application_fee_warning": "University of Adelaide does NOT charge any application fee for research degree or scholarship applications.",
            "agent_and_intermediary_warnings": "Do not pay agents to communicate with potential supervisors. Direct scholarly communication from the candidate is required.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD $1,600).",
                "Medical examination, chest X-ray, and biometrics in Pakistan (~PKR 45,000 - 55,000).",
                "Initial rental bond and living costs in Adelaide before first scholarship disbursement (~AUD $1,500 - $2,000).",
                "Dependent OSHC and visa fees if bringing family (only single OSHC is covered)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: You can apply without a supervisor's agreement. (FACT: Applications without a committed supervisor are automatically rejected).",
                "CLAIM: The scholarship covers coursework master's degrees. (FACT: Restricted exclusively to Higher Degree by Research - MPhil and PhD)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Outdated portals quote stipend rates below $30,000; the current official rate is indexed to AUD $34,236 - $37,000/year tax-free."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain satisfactory research progress through formal milestones: Major Review (at 12 months) and Annual Reviews thereafter.",
            "attendance_requirements": "Full-time physical research attendance on University of Adelaide campuses (North Terrace, Waite, or Roseworthy).",
            "academic_progress_monitoring": "Annual formal progress reports submitted to the Adelaide Graduate Research School.",
            "work_restrictions_during_study": "Outside paid employment during standard business hours is restricted to no more than 8 hours per week to ensure timely degree completion; outside hours subject to Australian visa rules.",
            "home_country_return_obligation": "None. Scholars can apply for the Australian Temporary Graduate Visa (Subclass 485) and permanent residency pathways upon thesis submission.",
            "service_obligations_or_bonds": "None.",
            "repayment_clawback_conditions": "Scholarship terminates if progress is deemed unsatisfactory or in cases of voluntary cancellation; repayment required only for proven fraud.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Requires approval from old and new supervisors and the Adelaide Graduate Research Committee.",
            "extension_policy": "PhD scholars can apply for up to 6 months extension subject to valid research delays and supervisor justification."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Adelaide Graduate Research Scholarships Portal",
                "source_url": "https://www.adelaide.edu.au/graduate-research/future-students/scholarships/australian-government-research-training-program-agrtp-scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Precise point values assigned to conference vs journal publications in Adelaide GRC scoring algorithm.",
                    "Specific allocation quotas across individual schools (e.g., Computer Science vs. Health Sciences).",
                    "Faculty-level top-up stipend allocation criteria and budget caps."
                ]
            }
        ]
    }
}
