# scripts/batch18_p3.py
# SCH-AM-041: Carleton University Graduate Scholarship & Assistantship in CS (Canada)
# SCH-AM-042: York University Lassonde Graduate Fellowship in CS & Engineering (Canada)
# SCH-AM-045: University of British Columbia (UBC) Karen McKellin International Leader Award (Canada)
# SCH-AM-047: University of Waterloo International Master's & Doctoral Award (IMAE/IDSA) (Canada)

DATA_P3 = {
    "SCH-AM-041": {
        "scholarship_id": "SCH-AM-041",
        "basic_details": {
            "scholarship_name": "Carleton University Graduate Scholarship & Assistantship in Computer Science",
            "offering_entity": "Carleton University School of Computer Science & Faculty of Graduate and Postdoctoral Affairs (FGPA)",
            "host_country": "Canada",
            "host_institutions_covered": "Carleton University Main Campus (Ottawa, Ontario, Canada)",
            "degree_levels": ["Master of Computer Science (MCS Thesis-based)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "School of Computer Science (OCICS joint institute): Algorithms and Theory, Artificial Intelligence and Machine Learning, Computer and Network Security, Human-Computer Interaction, Distributed Systems, and Biomedical Informatics.",
            "number_of_awards_total": "~60 to 80 funded graduate research positions awarded annually across thesis-based MCS and PhD intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~6 to 10 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MCS (Thesis); up to 4 years for PhD, subject to satisfactory annual academic and research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Canadian and international students of all nationalities (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research capability.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science or Computer Systems Engineering with at least B+ standing (minimum 77-79% aggregate or CGPA 3.30 / 4.00) for MCS; a research Master's degree in Computer Science with A- standing (CGPA 3.70 / 4.00) for PhD from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum B+ standing (9.0/12.0 Carleton scale, equivalent to 78%+ or 3.3/4.0) over the final two years of study.",
            "subject_background_prerequisites": "Substantial background in algorithms, operating systems, computer architecture, discrete mathematics, and object-oriented programming.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 86,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (with no sub-score below 6.0) or TOEFL iBT minimum 86 (reading 20, listening 20, speaking 20, writing 22). Official test reports mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure supervisory support from a Carleton School of Computer Science faculty member prior to final admission approval.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full external government fellowships without university approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIAL",
                "details": "International tuition fees (~CAD 9,000 to 14,000 / year) are offset through Departmental Graduate Scholarships (DGS) and tuition awards, with the balance paid directly out of the guaranteed funding package.",
                "amount": "Covered via funding package (~CAD 10,500 / year; ~PKR 2,152,500 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "Carleton University international application fee of CAD 120 (~USD 88; ~PKR 24,600) paid online via credit card.",
                "amount": "CAD 120 (~PKR 24,600)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus graduate housing (Leeds House) or private rental apartments in Ottawa (average CAD 800 to 1,200 / month; ~USD 590 to 880 / month) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~CAD 1,000 / month; ~PKR 205,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: MCS Thesis students receive at least CAD 24,000 / year (~CAD 2,000 / month; ~PKR 410,000 / month); PhD students receive at least CAD 28,000 to 34,000 / year (~CAD 2,333 to 2,833 / month; ~PKR 478,000 to 580,000 / month), composed of Departmental Graduate Scholarship (DGS), Graduate Teaching Assistantships (GTA, ~CAD 11,000/year under CUPE 4600), and Graduate Research Assistantships (GRA).",
                "amount": "CAD 24,000 to 34,000 / year (~PKR 410,000 to 580,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Ottawa/Montreal is self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 250,000 to 350,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD 150) and biometrics fee (CAD 85) paid by applicant.",
                "amount": "Not covered (~CAD 235; ~PKR 48,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "University Health Insurance Plan (UHIP) comprehensive medical insurance for international students in Ontario is covered directly under the graduate package (~CAD 756 / year value).",
                "amount": "100% covered UHIP health insurance"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Ottawa are easily accommodated within the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Carleton MacOdrum Library, high-performance computing clusters, and OCICS research laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "FGPA Graduate Travel Research Grants and supervisor research funds provide up to CAD 1,500 to 2,000 for presenting papers at premier conferences.",
                "amount": "Up to CAD 2,000 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Ottawa OC Transpo U-Pass provides unlimited transit on O-Train light rail and city buses, included directly in standard student registration fees.",
                "amount": "Unlimited transit via OC Transpo U-Pass"
            },
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Carleton University, Ottawa)",
            "participating_institutions": [
                "Carleton University - Main Campus (Ottawa, Ontario, Canada)"
            ],
            "university_rankings_scope": "Times Higher Education #351-400 globally, top Canadian comprehensive research institution located in Canada's capital and tech hub (Silicon Valley North / Kanata).",
            "available_majors": [
                "Computer Science (MCS & PhD)",
                "Artificial Intelligence and Machine Learning",
                "Computer and Network Security",
                "Human-Computer Interaction (HCI)",
                "Distributed and Cloud Computing",
                "Biomedical Computing and Informatics",
                "Algorithms and Complexity"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MCS (Thesis): 2 years; PhD: 4 years",
            "admission_requirements_summary": "Online Carleton application form, official academic transcripts, curriculum vitae, statement of research intent, official IELTS/TOEFL score report, two academic letters of recommendation, and confirmed faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission to the AI/ML and Cyber Security research groups receives fierce competition; establishing early contact with faculty members and demonstrating published research or strong coding projects is essential.",
            "strategic_program_match_advice": "Reach out to prospective supervisors between October and December. Send a concise email attaching your CV, academic transcript, and a 1-page summary of how your technical skills match their current research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://carleton.ca/scs/graduate-overview/funding-and-awards/ & https://graduate.carleton.ca/apply-online/",
            "portal_system_name": "Carleton Online Graduate Admissions Portal (Carleton Central)",
            "account_creation_instructions": "Create an applicant account on Carleton Central portal, select Computer Science thesis-based program, identify proposed supervisors, and upload digital application documents.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research groups and email prospective supervisors with CV and research interests (October - December).",
                "Step 2: Take IELTS (min 6.5) or TOEFL (min 86) and ensure official electronic score reporting to Carleton University.",
                "Step 3: Submit online application on Carleton Central portal and pay the CAD 120 application fee before the deadline (January 15).",
                "Step 4: Upload unofficial transcripts, CV, and statement of research intent.",
                "Step 5: Academic referees submit confidential appraisal forms via automated institutional links.",
                "Step 6: Prospective supervisors review shortlisted files and conduct online technical interviews (February - March).",
                "Step 7: Departmental Graduate Committee issues formal admission and guaranteed funding offer letters (March - April).",
                "Step 8: Accept the offer, apply for Canadian Provincial Attestation Letter (PAL) and Study Permit via IRCC.",
                "Step 9: Arrive in Ottawa in late August for international graduate orientation and commence studies in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: All admitted thesis-based graduate students automatically receive the guaranteed minimum funding package without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement of research intent outlining academic background, specific research problems of interest, and reasons for choosing Carleton Computer Science.",
            "study_plan_research_proposal_requirements": "Structured 1 to 2-page research outline highlighting technical methodologies and alignment with prospective faculty laboratories.",
            "cv_format_requirements": "Curriculum vitae detailing education, technical skillsets, research publications, awards, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview conducted by the prospective faculty supervisor focusing on technical depth, programming ability, and research drive.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 86) mandatory; GRE is not required for Computer Science at Carleton.",
            "application_fee_amount": "CAD 120 (~USD 88; ~PKR 24,600)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and official sealed transcripts sent upon admission offer.",
            "translation_requirements": "Certified English translation required for any documents not issued in English.",
            "final_submission_method": "100% digital submission via the Carleton Central graduate admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all post-secondary education with minimum B+ / 78% average equivalent.",
                "pakistan_specific_instruction": "Scanned color copies of HEC-attested Bachelor's/Master's degrees and semester-by-semester transcripts."
            },
            {
                "document_name": "Statement of Research Intent",
                "mandatory": True,
                "specification": "1 to 2-page essay detailing research interests, background, and alignment with prospective supervisors.",
                "pakistan_specific_instruction": "Must clearly name 2-3 Carleton Computer Science faculty members whose research aligns with yours."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 86).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to Carleton University (institution code 0854)."
            },
            {
                "document_name": "Two Academic Letters of Reference",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors who taught or supervised previous research.",
                "pakistan_specific_instruction": "Referees must submit from official Pakistani university email addresses."
            },
            {
                "document_name": "Updated Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic CV highlighting technical projects, publications, and programming proficiencies.",
                "pakistan_specific_instruction": "Include links to open-source code repositories (GitHub) and published papers."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "January 15",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "February 1",
            "recommendation_letters_deadline": "February 1",
            "interview_period": "February 1 - March 15",
            "shortlist_announcement": "March 15 - April 15",
            "final_result_acceptance_deadline": "May 1",
            "visa_application_window": "May 1 - July 15",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Main intake is Fall semester (September commencement). Applications received by January 15 receive premier funding consideration."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA in core computing coursework)",
            "extracurricular_and_leadership_weight": "5% (Technical community contributions and open-source engagement)",
            "research_experience_weight": "35% (Prior research, publications, technical projects, and supervisor match)",
            "work_experience_weight": "5% (Industry software engineering experience)",
            "personal_statement_weight": "10% (Clarity of research intent and problem formulation)",
            "recommendations_weight": "10% (Academic referee assessments on research potential)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (English meets mandatory threshold)",
            "financial_need_weight": "0% (Guaranteed merit-based departmental funding policy)",
            "selection_panel_composition": "School of Computer Science Graduate Admissions Committee and individual faculty principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit followed by faculty supervisor sponsorship and guaranteed funding commitment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~900 to 1,400 international graduate applicants for CS thesis programs",
            "total_scholarships_awarded": "~60 to 80 fully funded graduate positions awarded annually",
            "acceptance_rate_global": "~5.5% to 7.0%",
            "acceptance_rate_pakistan": "~6.5% to 8.5% among competitive applicants with supervisor backing",
            "typical_successful_applicant_gpa": "CGPA 3.60+ / 4.00 or 80%+ aggregate from leading Pakistani institutions (NUST, FAST, LUMS, GIKI, UET)",
            "typical_academic_and_research_profile": "Graduates with solid computing fundamentals, strong programming abilities, and at least 1-2 published papers or substantial research thesis outcomes.",
            "common_backgrounds_of_winners": "Graduates of Pakistani top computer science and software engineering programs.",
            "high_representation_countries": "Canada, Iran, China, India, Pakistan, Nigeria, Bangladesh, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent educational consultancy agencies claiming guaranteed admission or funding packages to Carleton.",
                "Legitimate applications are processed exclusively through carleton.ca."
            ],
            "application_fee_warning": "Carleton application fee is CAD 120 paid securely via the official portal; never pay fees to third-party brokers.",
            "agent_and_intermediary_warnings": "Carleton University does not partner with recruitment agents for research-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 120 (~PKR 24,600).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Canadian Study Permit and biometric fee: ~CAD 235 (~PKR 48,000).",
                "Initial settling-in expenses upon arrival in Ottawa: ~CAD 1,500 (~PKR 307,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get admitted to thesis MCS without a supervisor. Reality: Computer Science at Carleton requires a confirmed supervisor before formal admission is granted.",
                "Myth: Ottawa has limited tech opportunities. Reality: Ottawa boasts Canada's largest technology park (Kanata North), offering extensive research collaborations with tech giants."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is required; GRE is NOT required for Computer Science at Carleton."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 / 4.00 (Grade B) in graduate coursework throughout the degree program.",
            "attendance_requirements": "Full-time on-campus academic standing and active participation in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual Progress Report reviewed by the supervisory committee and the Graduate Program Director; satisfactory progress required for funding renewal.",
            "work_restrictions_during_study": "Teaching assistantships are capped at 10 hours per week (130 hours per term) under union regulations to prioritize thesis research.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the funding package.",
            "repayment_clawback_conditions": "Funding discontinued if student withdraws without authorization or is dismissed for academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other Canadian universities.",
            "rules_for_changing_major": "Changing major requires formal re-application and approval by the new academic department.",
            "extension_policy": "Funding is guaranteed for the standard program duration (2 years for MCS, 4 years for PhD); extensions are contingent on supervisor grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "Carleton University School of Computer Science Graduate Funding Portal",
                "source_url": "https://carleton.ca/scs/graduate-overview/funding-and-awards/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Carleton Faculty of Graduate and Postdoctoral Affairs",
                "source_url": "https://graduate.carleton.ca/apply-online/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AM-042": {
        "scholarship_id": "SCH-AM-042",
        "basic_details": {
            "scholarship_name": "York University Lassonde Graduate Fellowship & Assistantship in CS & Engineering",
            "offering_entity": "York University Lassonde School of Engineering & Faculty of Graduate Studies",
            "host_country": "Canada",
            "host_institutions_covered": "York University (Keele Campus, Toronto, Ontario, Canada)",
            "degree_levels": ["Master of Science (MSc Thesis in CS)", "Doctor of Philosophy (PhD in CS)"],
            "major_restrictions": "Department of Electrical Engineering and Computer Science (EECS): Artificial Intelligence, Robotics and Computer Vision, Big Data Analytics, Theoretical Computer Science, Software Engineering, and Internet of Things.",
            "number_of_awards_total": "~65 to 85 funded graduate research positions awarded annually across thesis-based MSc and PhD intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~6 to 11 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MSc (Thesis); up to 4 years for PhD, renewed annually based on satisfactory research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Canadian and international students of all nationalities (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research capability.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science or Computer Engineering with at least B+ standing (minimum 78% aggregate or CGPA 3.30 / 4.00) for MSc; a research Master's degree in Computer Science with thesis (minimum 80% aggregate or CGPA 3.70 / 4.00) for PhD from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum B+ standing (7.0/9.0 York scale, equivalent to 78%+ or 3.3/4.0) over the final two years of study.",
            "subject_background_prerequisites": "Substantial background in algorithms, data structures, operating systems, computer architecture, and discrete mathematics.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 7.0,
            "toefl_minimum": 95,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 7.0 overall (with no sub-score below 6.5) or TOEFL iBT minimum 95 (minimum 22 in each section). Official test reports mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure supervisory support from a York EECS faculty member prior to final admission approval.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full external government fellowships without university approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIAL",
                "details": "International tuition fees (~CAD 10,000 to 15,000 / year) are offset through York Graduate Fellowships (YGF) and international tuition awards, with the balance paid directly out of the guaranteed funding package.",
                "amount": "Covered via funding package (~CAD 11,500 / year; ~PKR 2,357,500 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "York University graduate application fee of CAD 130 (~USD 95; ~PKR 26,650) paid online via credit card.",
                "amount": "CAD 130 (~PKR 26,650)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus graduate apartments (York University Graduate Housing) or private rental apartments in the Greater Toronto Area (GTA) (average CAD 900 to 1,300 / month; ~USD 660 to 950 / month) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~CAD 1,100 / month; ~PKR 225,500 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: MSc Thesis students receive at least CAD 26,000 / year (~CAD 2,166 / month; ~PKR 444,000 / month); PhD students receive at least CAD 30,000 to 36,000 / year (~CAD 2,500 to 3,000 / month; ~PKR 512,500 to 615,000 / month), composed of York Graduate Fellowship (YGF), Graduate Teaching Assistantships (GTA, ~CAD 10,000/year under CUPE 3903), and Graduate Research Assistantships (GRA).",
                "amount": "CAD 26,000 to 36,000 / year (~PKR 444,000 to 615,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Toronto Pearson is self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 250,000 to 350,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD 150) and biometrics fee (CAD 85) paid by applicant.",
                "amount": "Not covered (~CAD 235; ~PKR 48,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "University Health Insurance Plan (UHIP) comprehensive medical insurance for international students in Ontario is covered directly under the graduate package (~CAD 756 / year value).",
                "amount": "100% covered UHIP health insurance"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Toronto are accommodated within the guaranteed monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to York Libraries (Scott Library, Steacie Science and Engineering Library), high-performance computing clusters, and EECS research laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "FGS Fieldwork/Travel Grants and supervisor research funds provide up to CAD 1,500 to 2,500 for presenting papers at premier conferences.",
                "amount": "Up to CAD 2,500 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Toronto TTC subway (Line 1 connects directly to York University subway station) paid from monthly stipend (~CAD 128/month with post-secondary pass).",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 28000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (York University, Toronto)",
            "participating_institutions": [
                "York University - Keele Campus (Toronto, Ontario, Canada)"
            ],
            "university_rankings_scope": "QS World University Rankings #362 worldwide, top 10 in Canada for Computer Science and Vision Research (Centre for Vision Research).",
            "available_majors": [
                "Computer Science (MSc & PhD)",
                "Artificial Intelligence and Machine Learning",
                "Robotics and Computer Vision",
                "Big Data Analytics and Cloud Computing",
                "Theoretical Computer Science and Cryptography",
                "Software Engineering and Verification",
                "Internet of Things and Networks"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MSc (Thesis): 2 years; PhD: 4 years",
            "admission_requirements_summary": "Online York application form, official academic transcripts, curriculum vitae, statement of interest, official IELTS/TOEFL score report, three academic letters of recommendation, and confirmed faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission to the AI, Robotics, and Vision research groups receives intense competition; establishing early contact with faculty members and demonstrating published research or strong coding projects is essential.",
            "strategic_program_match_advice": "Reach out to prospective supervisors between October and December. Send a concise email attaching your CV, academic transcript, and a 1-page summary of how your technical skills match their current research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://lassonde.yorku.ca/eecs/graduate-funding & https://futurestudents.yorku.ca/graduate/apply-now",
            "portal_system_name": "York University Online Graduate Admissions Portal",
            "account_creation_instructions": "Create an applicant account on York graduate portal, select Computer Science thesis-based program, identify proposed supervisors, and upload digital application documents.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research groups and email prospective supervisors with CV and research interests (October - December).",
                "Step 2: Take IELTS (min 7.0) or TOEFL (min 95) and ensure official electronic score reporting to York University.",
                "Step 3: Submit online application on York portal and pay the CAD 130 application fee before the deadline (January 15).",
                "Step 4: Upload unofficial transcripts, CV, and statement of interest.",
                "Step 5: Academic referees submit confidential appraisal forms via automated institutional links.",
                "Step 6: Prospective supervisors review shortlisted files and conduct online technical interviews (February - March).",
                "Step 7: Departmental Graduate Committee issues formal admission and guaranteed funding offer letters (March - April).",
                "Step 8: Accept the offer, apply for Canadian Provincial Attestation Letter (PAL) and Study Permit via IRCC.",
                "Step 9: Arrive in Toronto in late August for international graduate orientation and commence studies in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: All admitted thesis-based graduate students automatically receive the guaranteed minimum funding package without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement of interest outlining academic background, specific research problems of interest, and reasons for choosing York Computer Science.",
            "study_plan_research_proposal_requirements": "Structured 1 to 2-page research outline highlighting technical methodologies and alignment with prospective faculty laboratories.",
            "cv_format_requirements": "Curriculum vitae detailing education, technical skillsets, research publications, awards, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview conducted by the prospective faculty supervisor focusing on technical depth, programming ability, and research drive.",
            "standardized_tests": "IELTS Academic (min 7.0) or TOEFL iBT (min 95) mandatory; GRE is not required for Computer Science at York.",
            "application_fee_amount": "CAD 130 (~USD 95; ~PKR 26,650)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and official sealed transcripts sent upon admission offer.",
            "translation_requirements": "Certified English translation required for any documents not issued in English.",
            "final_submission_method": "100% digital submission via the York graduate admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all post-secondary education with minimum B+ / 78% average equivalent.",
                "pakistan_specific_instruction": "Scanned color copies of HEC-attested Bachelor's/Master's degrees and semester-by-semester transcripts."
            },
            {
                "document_name": "Statement of Interest",
                "mandatory": True,
                "specification": "1 to 2-page essay detailing research interests, background, and alignment with prospective supervisors.",
                "pakistan_specific_instruction": "Must clearly name 2-3 York EECS faculty members whose research aligns with yours."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 7.0 overall, 6.5 in each subtest) or TOEFL iBT (min 95).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to York University (institution code 0894)."
            },
            {
                "document_name": "Three Academic Letters of Reference",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors who taught or supervised previous research.",
                "pakistan_specific_instruction": "Referees must submit from official Pakistani university email addresses."
            },
            {
                "document_name": "Updated Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic CV highlighting technical projects, publications, and programming proficiencies.",
                "pakistan_specific_instruction": "Include links to open-source code repositories (GitHub) and published papers."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "January 15",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "February 1",
            "recommendation_letters_deadline": "February 1",
            "interview_period": "February 1 - March 15",
            "shortlist_announcement": "March 15 - April 15",
            "final_result_acceptance_deadline": "May 1",
            "visa_application_window": "May 1 - July 15",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Main intake is Fall semester (September commencement). Applications received by January 15 receive premier funding consideration."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA in core computing coursework)",
            "extracurricular_and_leadership_weight": "5% (Technical community contributions and open-source engagement)",
            "research_experience_weight": "35% (Prior research, publications, technical projects, and supervisor match)",
            "work_experience_weight": "5% (Industry software engineering experience)",
            "personal_statement_weight": "10% (Clarity of research intent and problem formulation)",
            "recommendations_weight": "10% (Academic referee assessments on research potential)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (English meets mandatory threshold)",
            "financial_need_weight": "0% (Guaranteed merit-based departmental funding policy)",
            "selection_panel_composition": "Department of EECS Graduate Admissions Committee and individual faculty principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit followed by faculty supervisor sponsorship and guaranteed funding commitment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,100 to 1,600 international graduate applicants for CS thesis programs",
            "total_scholarships_awarded": "~65 to 85 fully funded graduate positions awarded annually",
            "acceptance_rate_global": "~5.5% to 7.0%",
            "acceptance_rate_pakistan": "~6.5% to 8.5% among competitive applicants with supervisor backing",
            "typical_successful_applicant_gpa": "CGPA 3.60+ / 4.00 or 80%+ aggregate from leading Pakistani institutions (NUST, FAST, LUMS, GIKI, UET)",
            "typical_academic_and_research_profile": "Graduates with solid computing fundamentals, strong programming abilities, and at least 1-2 published papers or substantial research thesis outcomes.",
            "common_backgrounds_of_winners": "Graduates of Pakistani top computer science and software engineering programs.",
            "high_representation_countries": "Canada, Iran, China, India, Pakistan, Nigeria, Bangladesh, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent educational consultancy agencies claiming guaranteed admission or funding packages to York.",
                "Legitimate applications are processed exclusively through yorku.ca."
            ],
            "application_fee_warning": "York application fee is CAD 130 paid securely via the official portal; never pay fees to third-party brokers.",
            "agent_and_intermediary_warnings": "York University does not partner with recruitment agents for research-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 130 (~PKR 26,650).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Canadian Study Permit and biometric fee: ~CAD 235 (~PKR 48,000).",
                "Initial settling-in expenses upon arrival in Toronto: ~CAD 1,500 (~PKR 307,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get admitted to thesis MSc without a supervisor. Reality: Computer Science at York requires a confirmed supervisor before formal admission is granted.",
                "Myth: Living on campus is mandatory. Reality: Graduate students may reside on campus or in private apartments anywhere in the GTA connected by transit."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is required; GRE is NOT required for Computer Science at York."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 / 4.00 (Grade B) in graduate coursework throughout the degree program.",
            "attendance_requirements": "Full-time on-campus academic standing and active participation in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual Progress Report reviewed by the supervisory committee and the Graduate Program Director; satisfactory progress required for funding renewal.",
            "work_restrictions_during_study": "Teaching assistantships are capped at an average of 10 hours per week under union (CUPE 3903) regulations to prioritize thesis research.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the funding package.",
            "repayment_clawback_conditions": "Funding discontinued if student withdraws without authorization or is dismissed for academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other Canadian universities.",
            "rules_for_changing_major": "Changing major requires formal re-application and approval by the new academic department.",
            "extension_policy": "Funding is guaranteed for the standard program duration (2 years for MSc, 4 years for PhD); extensions are contingent on supervisor grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "York University Lassonde School of Engineering Graduate Funding Portal",
                "source_url": "https://lassonde.yorku.ca/eecs/graduate-funding",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "York Faculty of Graduate Studies Admissions",
                "source_url": "https://futurestudents.yorku.ca/graduate/apply-now",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AM-045": {
        "scholarship_id": "SCH-AM-045",
        "basic_details": {
            "scholarship_name": "University of British Columbia (UBC) Karen McKellin International Leader of Tomorrow Award",
            "offering_entity": "University of British Columbia (UBC) International Scholars Program",
            "host_country": "Canada",
            "host_institutions_covered": "University of British Columbia (Vancouver Main Campus and Okanagan Campus, BC, Canada)",
            "degree_levels": ["Bachelor of Arts (BA)", "Bachelor of Science (BSc)", "Bachelor of Applied Science (BASc / Engineering)", "Bachelor of Commerce (BCom)"],
            "major_restrictions": "Open to all direct-entry undergraduate faculties at UBC: Faculty of Science (Computer Science, Data Science, Physics, Biology), Faculty of Applied Science (Engineering), Sauder School of Business, Faculty of Land and Food Systems, and Faculty of Arts.",
            "number_of_awards_total": "~30 to 45 highly prestigious full-ride undergraduate scholarships awarded globally each year across the International Scholars Program",
            "number_of_awards_pakistan": "Extremely selective global competition; Pakistani high school leaders secure ~2 to 5 full awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years of full-time undergraduate study, renewed annually subject to maintaining superior academic standing (minimum 75% average) and active community leadership"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International citizens studying on a Canadian Study Permit (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "Applicants must be graduating high school seniors or recent high school graduates who have not completed more than one year of post-secondary study.",
            "academic_qualifications": "Exceptional academic achievement in secondary school: Intermediate (HSSC / Pre-Engineering / Pre-Medical) with at least 90% aggregate, or A-Levels with minimum AAA / A*AA grades, or International Baccalaureate (IB) 38+ points. Class rank typically in top 1-2%.",
            "minimum_gpa_percentage": 90.0,
            "minimum_gpa_scale": 3.8,
            "grading_conversion_notes": "Minimum unweighted high school average of 90%+ or Grade A equivalent across core senior subjects.",
            "subject_background_prerequisites": "Rigorous mathematics and sciences (Physics/Chemistry) for Science and Engineering programs.",
            "current_education_status": "Current high school seniors in their graduating year must apply with predicted grades; gap year students eligible if not enrolled in university.",
            "graduation_year_restrictions": "Must be entering university directly from high school or within 12 months of high school graduation.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Demonstrated exceptional extracurricular leadership, community impact, social innovation, or national/international competition achievements.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": True,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 (with no sub-score below 6.0), TOEFL iBT minimum 90 (reading 22, listening 22, writing 21, speaking 21), or Duolingo (DET) minimum 125. Waiver available if completed 4 consecutive years in English medium instruction.",
            "other_language_requirements": "None; instruction is entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": True,
            "special_eligibility_categories": "Applicants must be nominated directly by their secondary school and demonstrate financial need that would otherwise prevent them from studying at UBC.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full-ride awards.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Full 100% international undergraduate tuition fee waiver for the complete 4-year degree duration (~CAD 45,000 to 58,000 / year value depending on faculty).",
                "amount": "100% covered (~CAD 50,000 / year; ~PKR 10,250,000 / year)"
            },
            "admission_application_fee": {
                "status": "WAIVED",
                "details": "UBC undergraduate application fee of CAD 168 is waived for officially nominated International Scholars candidates demonstrating financial need.",
                "amount": "CAD 0 (Fee waived for nominated scholars)"
            },
            "accommodation": {
                "status": "100% COVERED",
                "details": "Guaranteed on-campus residence housing (Totem Park, Place Vanier, Orchard Commons) covered 100% for all 4 years (~CAD 10,000 to 14,000 / year value).",
                "amount": "100% covered on-campus housing"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Personal living allowance and campus life stipend calculated to meet 100% of the scholar's demonstrated financial need: ~CAD 600 to 1,000 / month (~USD 440 to 740 / month; ~PKR 123,000 to 205,000 / month).",
                "amount": "~CAD 800 / month (~PKR 164,000 / mo)"
            },
            "airfare": {
                "status": "100% COVERED",
                "details": "Annual economy-class round-trip airfare between Pakistan and Vancouver International Airport (YVR) provided directly by the International Scholars Program.",
                "amount": "100% covered annual round-trip flight ticket"
            },
            "visa_fee": {
                "status": "100% COVERED",
                "details": "Canadian Study Permit application and biometrics fees reimbursed by the program upon arrival in Canada.",
                "amount": "100% reimbursed"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "British Columbia Medical Services Plan (BC MSP) and iMED international student temporary health insurance covered 100% throughout the 4 years.",
                "amount": "100% covered provincial healthcare"
            },
            "food_allowance": {
                "status": "100% COVERED",
                "details": "Full university residence dining meal plan covering all daily meals across campus dining halls included directly in the award (~CAD 6,500 / year value).",
                "amount": "100% covered campus meal plan"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Annual textbook and academic course supplies stipend (~CAD 1,500 / year) plus high-performance laptop grant.",
                "amount": "CAD 1,500 / year + laptop grant"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "International Scholars enrichment funding supports summer internships, undergraduate research initiatives, and global leadership retreats.",
                "amount": "Covered under leadership enrichment grant"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Vancouver TransLink U-Pass provides unlimited transit across all buses, SkyTrain lines, and SeaBus ferries in Metro Vancouver.",
                "amount": "Unlimited transit via TransLink U-Pass"
            },
            "total_estimated_value_usd_per_year": 55000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (University of British Columbia - Vancouver & Okanagan)",
            "participating_institutions": [
                "University of British Columbia - Vancouver Point Grey Campus & Okanagan Campus (BC, Canada)"
            ],
            "university_rankings_scope": "QS World University Rankings #38 worldwide, Times Higher Education #41 globally, top 2 research university in Canada.",
            "available_majors": [
                "Computer Science (BSc & BA)",
                "Data Science",
                "Electrical and Computer Engineering (BASc)",
                "Mechanical Engineering (BASc)",
                "Biomedical Engineering (BASc)",
                "Physics and Astronomy (BSc)",
                "Mathematics and Statistics (BSc)",
                "Commerce / Business Administration (BCom - Sauder)",
                "Economics and International Relations (BA)",
                "Global Resource Systems (BSc)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "4 years (full-time undergraduate)",
            "admission_requirements_summary": "School nomination form, online UBC undergraduate application, personal profile essays, high school transcripts (Grades 9-12), counselor reference, English proficiency report, and detailed financial declaration form.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "The Karen McKellin Award is one of the most prestigious and competitive undergraduate awards in the world (acceptance rate ~1-2%); applicants must demonstrate top-tier academic distinction paired with transformative community impact.",
            "strategic_program_match_advice": "Focus heavily on authentic leadership and social impact in the International Scholars personal essays. Ensure your secondary school counselor submits the official nomination well before the December 1 deadline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://you.ubc.ca/financial-planning/scholarships-awards-international-students/international-scholars/ & https://account.you.ubc.ca/",
            "portal_system_name": "UBC Online Admissions & International Scholars Portal",
            "account_creation_instructions": "Create an applicant account on UBC admissions portal, complete the general undergraduate application, submit the International Scholars Program application, and have your school counselor complete the nomination package.",
            "step_by_step_workflow": [
                "Step 1: Secure official nomination from high school principal or college guidance counselor (October - November).",
                "Step 2: Submit UBC online undergraduate admission application at you.ubc.ca (Deadline: December 1).",
                "Step 3: Complete and submit the International Scholars Program award application and financial disclosure form (Deadline: December 1).",
                "Step 4: School counselor uploads official nomination letter, school profile, and transcripts by December 1.",
                "Step 5: Submit all supporting academic documents, predicted grades, and English proficiency test scores (Deadline: January 31).",
                "Step 6: International Scholars Selection Committee conducts comprehensive holistic evaluations (February - March).",
                "Step 7: Selected finalists participate in virtual video interviews with the scholarship committee (March).",
                "Step 8: Final award and admission decisions announced (mid-April).",
                "Step 9: Accept the award, obtain Provincial Attestation Letter (PAL), apply for Canadian Study Permit, and arrive in Vancouver in late August for Jump Start orientation."
            ],
            "university_vs_scholarship_routing": "Integrated Track: Application for the International Scholars Program is submitted concurrently with the UBC undergraduate admission application.",
            "recommendation_letters_submission_method": "Submitted online by the secondary school counselor and an academic referee via secure links dispatched by the International Scholars portal.",
            "personal_statement_prompts": "Personal profile essays detailing significant extracurricular accomplishments, leadership initiatives, resilience through adversity, and vision for community contribution.",
            "study_plan_research_proposal_requirements": "Not required for undergraduates; evaluated on intellectual curiosity, community impact, and academic excellence.",
            "cv_format_requirements": "Embedded activities list detailing leadership roles, community service projects, and honors.",
            "interviews_conducted": True,
            "interview_format_details": "20 to 30-minute online panel interview conducted by International Scholars committee members evaluating leadership vision, character, and communication.",
            "standardized_tests": "SAT/ACT is optional; English proficiency test (IELTS min 6.5, TOEFL min 90, or DET min 125) mandatory unless meeting language exemption.",
            "application_fee_amount": "CAD 168 (Waived for nominated candidates with demonstrated financial need)",
            "attestation_requirements": "High school diploma and transcripts must be authenticated by IBCC/British Council and official results sent upon final admission.",
            "translation_requirements": "Certified English translation required for any documents not issued in English.",
            "final_submission_method": "100% digital submission via the UBC online portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "UBC Undergraduate Application and Personal Profile",
                "mandatory": True,
                "specification": "Completed online application at you.ubc.ca with detailed personal profile essays.",
                "pakistan_specific_instruction": "Ensure legal name matches Pakistani passport exactly."
            },
            {
                "document_name": "Official High School Nomination Form",
                "mandatory": True,
                "specification": "Official nomination form and letter completed by secondary school principal or guidance counselor.",
                "pakistan_specific_instruction": "Each Pakistani school may nominate up to a limited number of exceptional candidates."
            },
            {
                "document_name": "Official High School Transcripts (Grades 9-12)",
                "mandatory": True,
                "specification": "Complete transcripts for Grades 9, 10, 11, and senior year predicted/mid-year grades.",
                "pakistan_specific_instruction": "Matric/FSc mark sheets or O/A Level statement of results uploaded by school counselor."
            },
            {
                "document_name": "International Scholars Financial Declaration",
                "mandatory": True,
                "specification": "Detailed financial disclosure form detailing household income, assets, and expenses.",
                "pakistan_specific_instruction": "Parent tax returns (FBR) or employer salary certificates translated into English."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 90).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to UBC (institution code 0965)."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "December 1 (Application & Nomination deadline)",
            "university_admission_deadline": "December 1",
            "document_submission_deadline": "January 31",
            "recommendation_letters_deadline": "December 1",
            "interview_period": "March 1 - March 25",
            "shortlist_announcement": "Mid-April",
            "final_result_acceptance_deadline": "May 1",
            "visa_application_window": "May 1 - July 15",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Single annual intake cycle for September enrollment. The December 1 deadline is strict and non-extendable."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Secondary school GPA, academic rigor, and intellectual curiosity)",
            "extracurricular_and_leadership_weight": "30% (Demonstrated leadership, community initiatives, and character)",
            "research_experience_weight": "5% (Olympiad/science fair projects where applicable)",
            "work_experience_weight": "5% (Community engagement, internships, or social ventures)",
            "personal_statement_weight": "15% (Personal profile essays and leadership reflections)",
            "recommendations_weight": "5% (School counselor nomination and teacher appraisals)",
            "interview_weight": "0% (Interview performance factored directly into final selection committee decision)",
            "test_scores_weight": "0% (SAT/ACT optional; English meets threshold)",
            "financial_need_weight": "0% (Evaluated to determine scholarship package value to meet 100% of need)",
            "selection_panel_composition": "UBC International Scholars Selection Committee, Deans of Academic Faculties, and Associate Vice-President International.",
            "evaluation_methodology": "Comprehensive holistic review: academic distinction, authentic leadership impact, perseverance through adversity, and alignment with UBC values."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~2,500 to 3,500 nominated global applicants competing for International Scholars awards",
            "total_scholarships_awarded": "~30 to 45 full awards distributed globally each year",
            "acceptance_rate_global": "~1.0% to 1.5%",
            "acceptance_rate_pakistan": "~2.0% to 3.0% among elite nominated candidates",
            "typical_successful_applicant_gpa": "Top 1-2% of graduating class, A*A*A in A-Levels, 92%+ in FSc/Matric",
            "typical_academic_and_research_profile": "World-class academic standing paired with extraordinary community service (founders of impactful NGOs, debate champions, environmental activists).",
            "common_backgrounds_of_winners": "Graduates of top Pakistani public and private secondary schools who have led transformative community projects.",
            "high_representation_countries": "Canada, Pakistan, India, Kenya, Nigeria, Brazil, Turkey, Indonesia, Vietnam.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of commercial agencies advertising guaranteed UBC scholarships.",
                "Legitimate applications are processed exclusively through you.ubc.ca."
            ],
            "application_fee_warning": "Nominated applicants requesting financial aid receive a waiver for the CAD 168 application fee; never pay third-party agents.",
            "agent_and_intermediary_warnings": "UBC strictly prohibits recruitment agents from submitting scholarship applications on behalf of students.",
            "hidden_costs_breakdown": [
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Canadian Study Permit and biometric fee: ~CAD 235 (~PKR 48,000).",
                "High school transcript attestation in Pakistan upon graduation: ~PKR 15,000 to 25,000."
            ],
            "misleading_claims_debunked": [
                "Myth: You can apply without school nomination. Reality: The International Scholars Program strictly requires an official nomination from your high school counselor.",
                "Myth: The scholarship only covers tuition. Reality: The Karen McKellin Award covers 100% of demonstrated financial need, including tuition, residence, food, healthcare, and flights."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial blogs suggest SAT is required; SAT is completely optional for international students applying to UBC."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative average of 75% in undergraduate coursework and remain in Good Standing in your enrolled faculty.",
            "attendance_requirements": "Full-time enrollment (minimum 24-30 percentage credits per academic year) and active participation in the International Scholars community.",
            "academic_progress_monitoring": "Annual review by the International Scholars Committee; scholars participate in leadership development workshops and cohort meetings.",
            "work_restrictions_during_study": "Part-time on-campus/off-campus employment permitted up to 20 hours per week during academic terms under Canadian Study Permit regulations.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the fellowship.",
            "repayment_clawback_conditions": "Award terminated if scholar is dismissed for academic misconduct, fails to maintain academic average, or withdraws without authorization.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Major change permitted within the same faculty or across faculties subject to academic approval.",
            "extension_policy": "Award covers a maximum of 4 consecutive undergraduate years (8 academic terms)."
        },
        "official_sources_verified": [
            {
                "source_name": "UBC International Scholars Program Official Portal",
                "source_url": "https://you.ubc.ca/financial-planning/scholarships-awards-international-students/international-scholars/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UBC Undergraduate Admissions Portal",
                "source_url": "https://account.you.ubc.ca/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AM-047": {
        "scholarship_id": "SCH-AM-047",
        "basic_details": {
            "scholarship_name": "University of Waterloo International Master's & Doctoral Award (IMAE & IDSA)",
            "offering_entity": "University of Waterloo Graduate Studies and Postdoctoral Affairs (GSPA)",
            "host_country": "Canada",
            "host_institutions_covered": "University of Waterloo Main Campus (Waterloo, Ontario, Canada)",
            "degree_levels": ["Master of Mathematics (MMath in CS)", "Master of Applied Science (MASc Engineering)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "David R. Cheriton School of Computer Science, Department of Electrical & Computer Engineering, Combinatorics & Optimization, Systems Design Engineering, Mechanical & Mechatronics Engineering, and Institute for Quantum Computing (IQC).",
            "number_of_awards_total": "~120 to 160 funded international graduate research awards distributed annually across MMath, MASc, and PhD programs",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing, math, and quantum engineering secure ~10 to 18 awards annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years (5-6 terms) for Master's; up to 4 years (12 terms) for PhD, subject to satisfactory annual progress reviews"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international students studying on a valid Canadian Study Permit (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic brilliance and verified research potential.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) with First Class Honours / minimum 80% aggregate (minimum CGPA 3.60 / 4.00) for Master's; a research Master's degree with thesis and minimum 85% aggregate (minimum CGPA 3.80 / 4.00) for PhD from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Equivalent to Waterloo First Class Honours standing (80%+ or minimum 3.60/4.00) in core mathematical and computer science coursework.",
            "subject_background_prerequisites": "Substantial background in algorithms, discrete mathematics, computer systems, linear algebra, and probability theory.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with certified interim transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior publications in top-tier conferences (NeurIPS, ICML, CVPR, SIGCOMM, SOSP) or math competitions significantly raise funding priority.",
            "english_test_required": True,
            "ielts_minimum": 7.5,
            "toefl_minimum": 100,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 7.5 overall (writing 7.0, speaking 7.0) or TOEFL iBT minimum 100 (writing 26, speaking 26). Official test reports mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must be accepted into a research-based graduate degree program; IMAE and IDSA are automatically allocated to qualifying international candidates.",
            "previous_scholarship_restrictions": "Cannot hold concurrent major external government fellowships without university approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "For PhD: International Doctoral Student Award (IDSA) directly pays the international tuition differential (saving ~CAD 15,000 / year), reducing tuition to the domestic rate, which is then fully covered by departmental research assistantships. For Master's: International Master's Award of Excellence (IMAE) provides CAD 2,500 per term (~CAD 7,500 / year) towards tuition offset.",
                "amount": "100% covered / offset (~CAD 15,000 to 22,000 / year value; ~PKR 3,075,000 to 4,510,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "University of Waterloo graduate application fee of CAD 125 (~USD 92; ~PKR 25,625) paid online via credit card.",
                "amount": "CAD 125 (~PKR 25,625)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus graduate residence (Columbia Lake Village) or private rental apartments in Waterloo (average CAD 750 to 1,150 / month; ~USD 550 to 850 / month) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~CAD 950 / month; ~PKR 194,750 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: MMath/MASc thesis students receive at least CAD 28,000 to 32,000 / year (~CAD 2,333 to 2,666 / month; ~PKR 478,000 to 546,500 / month); PhD students receive at least CAD 32,000 to 40,000 / year (~CAD 2,666 to 3,333 / month; ~PKR 546,500 to 683,000 / month), composed of IMAE/IDSA, Graduate Research Studentships (GRS), and Teaching Assistantships (GTA, ~CAD 7,500/term).",
                "amount": "CAD 28,000 to 40,000 / year (~PKR 478,000 to 683,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Toronto/Waterloo is self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 250,000 to 350,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD 150) and biometrics fee (CAD 85) paid by applicant.",
                "amount": "Not covered (~CAD 235; ~PKR 48,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "University Health Insurance Plan (UHIP) comprehensive medical insurance for international students in Ontario is covered directly under the graduate package (~CAD 756 / year value).",
                "amount": "100% covered UHIP health insurance"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Waterloo are easily accommodated within the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Waterloo Libraries (Davis Centre Library, Dana Porter Library), high-performance computing clusters, and Cheriton School laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "GSPA Graduate Student Travel Research Grants and supervisor research funds provide up to CAD 2,000 to 3,000 for presenting papers at premier conferences.",
                "amount": "Up to CAD 3,000 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Grand River Transit (GRT) universal bus and ION light rail pass provides unlimited transit throughout Waterloo, Kitchener, and Cambridge, included directly in standard student registration fees.",
                "amount": "Unlimited transit via GRT U-Pass"
            },
            "total_estimated_value_usd_per_year": 30000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (University of Waterloo, Ontario)",
            "participating_institutions": [
                "University of Waterloo - Main Campus (Waterloo, Ontario, Canada)"
            ],
            "university_rankings_scope": "QS World University Rankings #112 worldwide, #25 globally in Computer Science and Mathematics, world-leading hub for Quantum Computing and Tech Entrepreneurship.",
            "available_majors": [
                "Computer Science (MMath & PhD - Cheriton School)",
                "Electrical and Computer Engineering (MASc & PhD)",
                "Combinatorics and Optimization",
                "Systems Design Engineering",
                "Quantum Information and Quantum Computing (IQC)",
                "Artificial Intelligence and Machine Learning",
                "Software Engineering and Formal Verification",
                "Cryptography, Security and Privacy (CrySP)"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's (Thesis): 2 years (6 terms); PhD: 4 years (12 terms)",
            "admission_requirements_summary": "Online Waterloo application form, official academic transcripts, curriculum vitae, statement of research interest, official IELTS/TOEFL score report, three academic letters of recommendation, and confirmed faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission to the Cheriton School of Computer Science and the Institute for Quantum Computing is intensely competitive; establishing early contact with faculty members and demonstrating published research or extraordinary programming/mathematical distinction is essential.",
            "strategic_program_match_advice": "Reach out to prospective supervisors between October and December. Send a concise email attaching your CV, academic transcript, and a 1-page summary of how your technical skills match their current research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/awards/international-masters-award-excellence-imae & https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/future-students/apply-online",
            "portal_system_name": "Waterloo Online Graduate Admissions Portal (OUAC / Quest)",
            "account_creation_instructions": "Submit application via Ontario Universities' Application Centre (OUAC), claim Quest account, select Computer Science thesis-based program, identify proposed supervisors, and upload digital application documents.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research groups and email prospective supervisors with CV and research interests (October - November).",
                "Step 2: Take IELTS (min 7.5) or TOEFL (min 100) and ensure official electronic score reporting to University of Waterloo.",
                "Step 3: Submit online application on OUAC portal and pay the CAD 125 application fee before the deadline (December 15 for CS / January 15 for Engineering).",
                "Step 4: Claim Waterloo Quest account, upload unofficial transcripts, CV, and statement of research interest.",
                "Step 5: Academic referees submit confidential appraisal forms via automated institutional links.",
                "Step 6: Prospective supervisors review shortlisted files and conduct online technical interviews (January - February).",
                "Step 7: Departmental Graduate Committee issues formal admission and guaranteed funding offer letters (February - April).",
                "Step 8: Accept the offer, apply for Canadian Provincial Attestation Letter (PAL) and Study Permit via IRCC.",
                "Step 9: Arrive in Waterloo in late August for international graduate orientation and commence studies in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: All admitted thesis-based graduate students automatically receive the guaranteed minimum funding package and IMAE/IDSA without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement of research interest outlining academic background, specific research problems of interest, and reasons for choosing Waterloo Computer Science.",
            "study_plan_research_proposal_requirements": "Structured 1 to 2-page research outline highlighting technical methodologies and alignment with prospective faculty laboratories.",
            "cv_format_requirements": "Curriculum vitae detailing education, technical skillsets, research publications, awards, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview conducted by the prospective faculty supervisor focusing on technical depth, programming ability, and research drive.",
            "standardized_tests": "IELTS Academic (min 7.5) or TOEFL iBT (min 100) mandatory; GRE is optional but strongly recommended for international CS applicants.",
            "application_fee_amount": "CAD 125 (~USD 92; ~PKR 25,625)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and official sealed transcripts sent upon admission offer.",
            "translation_requirements": "Certified English translation required for any documents not issued in English.",
            "final_submission_method": "100% digital submission via the Waterloo Quest graduate admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all post-secondary education with minimum 80% / 3.60 GPA equivalent.",
                "pakistan_specific_instruction": "Scanned color copies of HEC-attested Bachelor's/Master's degrees and semester-by-semester transcripts."
            },
            {
                "document_name": "Statement of Research Interest",
                "mandatory": True,
                "specification": "1 to 2-page essay detailing research interests, background, and alignment with prospective supervisors.",
                "pakistan_specific_instruction": "Must clearly name 2-3 Waterloo Computer Science faculty members whose research aligns with yours."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 7.5 overall, 7.0 in writing and speaking) or TOEFL iBT (min 100).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to University of Waterloo (institution code 0998)."
            },
            {
                "document_name": "Three Academic Letters of Reference",
                "mandatory": True,
                "specification": "Confidential evaluation letters from academic professors who taught or supervised previous research.",
                "pakistan_specific_instruction": "Referees must submit from official Pakistani university email addresses."
            },
            {
                "document_name": "Updated Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Detailed academic CV highlighting technical projects, publications, and programming proficiencies.",
                "pakistan_specific_instruction": "Include links to open-source code repositories (GitHub) and published papers."
            },
            {
                "document_name": "Valid Passport Copy",
                "mandatory": True,
                "specification": "Clear color copy of passport identification page valid for at least 2 years.",
                "pakistan_specific_instruction": "Pakistani passport must have validity through late 2028."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "September 1",
            "application_deadline": "December 15 (CS) / January 15 (Engineering)",
            "university_admission_deadline": "December 15 / January 15",
            "document_submission_deadline": "January 15 / February 1",
            "recommendation_letters_deadline": "January 15 / February 1",
            "interview_period": "January 15 - March 15",
            "shortlist_announcement": "March 1 - April 15",
            "final_result_acceptance_deadline": "May 1",
            "visa_application_window": "May 1 - July 15",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Main intake is Fall semester (September commencement). Computer Science applications close December 15."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Undergraduate/Master's GPA in core computing coursework)",
            "extracurricular_and_leadership_weight": "5% (Technical community contributions and open-source engagement)",
            "research_experience_weight": "35% (Prior research, publications, technical projects, and supervisor match)",
            "work_experience_weight": "5% (Industry software engineering experience)",
            "personal_statement_weight": "10% (Clarity of research intent and problem formulation)",
            "recommendations_weight": "10% (Academic referee assessments on research potential)",
            "interview_weight": "0% (Interview performance factored directly into supervisor endorsement)",
            "test_scores_weight": "0% (English meets mandatory threshold)",
            "financial_need_weight": "0% (Guaranteed merit-based departmental funding policy)",
            "selection_panel_composition": "Cheriton School Graduate Admissions Committee and individual faculty principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit followed by faculty supervisor sponsorship and guaranteed funding commitment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,500 international graduate applicants for CS thesis programs",
            "total_scholarships_awarded": "~120 to 160 fully funded graduate positions awarded annually",
            "acceptance_rate_global": "~4.5% to 6.0%",
            "acceptance_rate_pakistan": "~5.5% to 7.5% among competitive applicants with supervisor backing",
            "typical_successful_applicant_gpa": "CGPA 3.75+ / 4.00 or 85%+ aggregate from leading Pakistani institutions (NUST, FAST, LUMS, GIKI, UET)",
            "typical_academic_and_research_profile": "Graduates with exceptional mathematical and computing fundamentals, strong programming abilities, and at least 1-2 published papers in top-tier conferences.",
            "common_backgrounds_of_winners": "Graduates of Pakistani top computer science, mathematics, and software engineering programs.",
            "high_representation_countries": "Canada, China, Iran, India, Pakistan, USA, Germany, Turkey.",
            "competitiveness_tier": "EXTREME"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent educational consultancy agencies claiming guaranteed admission or funding packages to Waterloo.",
                "Legitimate applications are processed exclusively through uwaterloo.ca."
            ],
            "application_fee_warning": "Waterloo application fee is CAD 125 paid securely via the official portal; never pay fees to third-party brokers.",
            "agent_and_intermediary_warnings": "University of Waterloo does not partner with recruitment agents for research-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 125 (~PKR 25,625).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Canadian Study Permit and biometric fee: ~CAD 235 (~PKR 48,000).",
                "Initial settling-in expenses upon arrival in Waterloo: ~CAD 1,500 (~PKR 307,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get admitted to thesis MMath/PhD without a supervisor. Reality: Research programs at Waterloo require a confirmed supervisor before formal admission is granted.",
                "Myth: The funding package requires repayment. Reality: The funding is non-repayable, provided via scholarships, tuition waivers, and graduate assistantships."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is mandatory; GRE is NOT mandatory for Computer Science at Waterloo, although strong Quantitative scores are considered favorably."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative average of 75% in graduate coursework throughout the degree program.",
            "attendance_requirements": "Full-time on-campus academic standing and active participation in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual Progress Report reviewed by the supervisory committee and the Graduate Officer; satisfactory progress required for funding renewal.",
            "work_restrictions_during_study": "Teaching/research assistantships are limited to an average of 10 hours per week during academic terms to prioritize thesis research.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the funding package.",
            "repayment_clawback_conditions": "Funding discontinued if student withdraws without authorization or is dismissed for academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other Canadian universities.",
            "rules_for_changing_major": "Changing major requires formal re-application and approval by the new academic department.",
            "extension_policy": "Funding is guaranteed for the standard program duration (2 years for Master's, 4 years for PhD); extensions are contingent on supervisor grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Waterloo International Master's Award of Excellence Portal",
                "source_url": "https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/awards/international-masters-award-excellence-imae",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Waterloo Graduate Studies and Postdoctoral Affairs",
                "source_url": "https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/future-students/apply-online",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
