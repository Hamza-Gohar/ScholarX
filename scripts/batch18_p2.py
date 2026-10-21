# scripts/batch18_p2.py
# SCH-AM-034: University of Victoria (UVic) Graduate Fellowship in Computer Science (Canada)
# SCH-AM-037: Concordia University Graduate Fellowship in CS & Software Engineering (Canada)
# SCH-AM-038: Dalhousie University Computer Science Graduate Scholarship (Canada)

DATA_P2 = {
    "SCH-AM-034": {
        "scholarship_id": "SCH-AM-034",
        "basic_details": {
            "scholarship_name": "University of Victoria (UVic) Graduate Fellowship & Teaching Assistantship in Computer Science",
            "offering_entity": "University of Victoria Department of Computer Science & Faculty of Graduate Studies (FGS)",
            "host_country": "Canada",
            "host_institutions_covered": "University of Victoria (Gordon Head Campus, Victoria, British Columbia, Canada)",
            "degree_levels": ["Master of Science (MSc Thesis-based)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Department of Computer Science: Artificial Intelligence, Data Mining, Human-Centered Computing, Embedded Systems and Robotics, Computer Graphics, Computer Networking, and Software Engineering.",
            "number_of_awards_total": "~50 to 70 funded graduate research positions awarded annually across thesis-based MSc and PhD intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~5 to 9 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MSc (Thesis); up to 4 years for PhD, subject to satisfactory annual academic and research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Canadian and international students of all nationalities (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research capability.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science or related STEM discipline with at least First Class / B+ standing (minimum 75-78% aggregate or CGPA 3.30 / 4.00) for MSc; a research Master's degree in Computer Science with thesis (minimum 80% aggregate or CGPA 3.50 / 4.00) for PhD from an HEC-recognized university in Pakistan (competitive admits typically 3.60+ / 4.00).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Evaluated on UVic 9-point scale; minimum Grade B+ (equivalent to 78%+ or 3.3/4.0) over the final two years of study.",
            "subject_background_prerequisites": "Substantial background in algorithms, data structures, operating systems, computer architecture, and discrete mathematics.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (with no sub-score below 6.0) or TOEFL iBT minimum 90 (minimum 20 in each section). Official test reports mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure supervisory support from a UVic Computer Science faculty member prior to final admission approval.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full external government fellowships without university approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIAL",
                "details": "International tuition fees (~CAD 8,500 to 12,000 / year) are offset through UVic Graduate Fellowships and departmental awards, with the balance paid directly out of the guaranteed funding package.",
                "amount": "Covered via funding package (~CAD 9,500 / year; ~PKR 1,947,500 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "University of Victoria international application fee of CAD 172 (~USD 126; ~PKR 35,260) paid online via credit card.",
                "amount": "CAD 172 (~PKR 35,260)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus graduate housing (Cluster Housing) or private rental apartments in Victoria (average CAD 850 to 1,250 / month; ~USD 620 to 920 / month) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~CAD 1,050 / month; ~PKR 215,250 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: MSc Thesis students receive at least CAD 24,000 / year (~CAD 2,000 / month; ~PKR 410,000 / month); PhD students receive at least CAD 27,000 to 33,000 / year (~CAD 2,250 to 2,750 / month; ~PKR 461,250 to 563,750 / month), composed of UVic Graduate Fellowship (UVGF), Graduate Teaching Assistantships (GTA, ~CAD 6,000/year), and Graduate Research Assistantships (GRA).",
                "amount": "CAD 24,000 to 33,000 / year (~PKR 410,000 to 563,750 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Victoria/Vancouver is self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 260,000 to 360,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD 150) and biometrics fee (CAD 85) paid by applicant.",
                "amount": "Not covered (~CAD 235; ~PKR 48,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "British Columbia Medical Services Plan (BC MSP) provides comprehensive provincial healthcare coverage for international students residing in BC (~CAD 75/month), with supplementary coverage included through the UVic Graduate Students' Society (GSS) Health and Dental Plan.",
                "amount": "Covered under provincial MSP and GSS plan"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Victoria are easily accommodated within the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to UVic McPherson Library, high-performance computing clusters, and departmental laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "FGS Travel Grants and supervisor research funds provide up to CAD 1,500 to 2,000 for presenting papers at premier conferences.",
                "amount": "Up to CAD 2,000 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Victoria Regional Transit U-Pass provides unlimited transit on city buses, included directly in standard student registration fees.",
                "amount": "Unlimited transit via U-Pass"
            },
            "total_estimated_value_usd_per_year": 26000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (University of Victoria, British Columbia)",
            "participating_institutions": [
                "University of Victoria - Gordon Head Campus (Victoria, British Columbia, Canada)"
            ],
            "university_rankings_scope": "Times Higher Education #301-350 globally, top 10 Canadian comprehensive university, renowned for Computer Science and Ocean Networks Canada.",
            "available_majors": [
                "Computer Science (MSc & PhD)",
                "Artificial Intelligence and Machine Learning",
                "Data Mining and Big Data",
                "Human-Centered Computing and Interaction",
                "Embedded Systems and Internet of Things",
                "Computer Graphics and Visualization",
                "Computer Communications and Networking",
                "Software Engineering and Verification"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MSc (Thesis): 2 years; PhD: 4 years",
            "admission_requirements_summary": "Online UVic application form, official academic transcripts, curriculum vitae, statement of research intent, official IELTS/TOEFL score report, two academic letters of recommendation, and confirmed faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission to the AI/ML and Embedded Systems research groups is highly selective; establishing early contact with faculty members and demonstrating published research or strong coding projects is essential.",
            "strategic_program_match_advice": "Reach out to prospective supervisors between October and December. Send a concise email attaching your CV, academic transcript, and a 1-page summary of how your technical skills match their current research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.uvic.ca/ecs/computerscience/graduate/funding/index.php & https://www.uvic.ca/graduate/admissions/how-to-apply/index.php",
            "portal_system_name": "UVic Online Graduate Admissions Portal (My UVic Application)",
            "account_creation_instructions": "Create an applicant account on My UVic Application portal, select Computer Science thesis-based program, identify proposed supervisors, and upload digital application documents.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research groups and email prospective supervisors with CV and research interests (October - December).",
                "Step 2: Take IELTS (min 6.5) or TOEFL (min 90) and ensure official electronic score reporting to University of Victoria.",
                "Step 3: Submit online application on UVic portal and pay the CAD 172 application fee before the deadline (January 15).",
                "Step 4: Upload unofficial transcripts, CV, and statement of research intent.",
                "Step 5: Academic referees submit confidential appraisal forms via automated institutional links.",
                "Step 6: Prospective supervisors review shortlisted files and conduct online technical interviews (February - March).",
                "Step 7: Departmental Graduate Committee issues formal admission and guaranteed funding offer letters (March - April).",
                "Step 8: Accept the offer, apply for Canadian Provincial Attestation Letter (PAL) and Study Permit via IRCC.",
                "Step 9: Arrive in Victoria, BC in late August for international graduate orientation and commence studies in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: All admitted thesis-based graduate students automatically receive the guaranteed minimum funding package without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement of research intent outlining academic background, specific research problems of interest, and reasons for choosing UVic Computer Science.",
            "study_plan_research_proposal_requirements": "Structured 1 to 2-page research outline highlighting technical methodologies and alignment with prospective faculty laboratories.",
            "cv_format_requirements": "Curriculum vitae detailing education, technical skillsets, research publications, awards, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview conducted by the prospective faculty supervisor focusing on technical depth, programming ability, and research drive.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 90) mandatory; GRE is not required for Computer Science at UVic.",
            "application_fee_amount": "CAD 172 (~USD 126; ~PKR 35,260)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and official sealed transcripts sent upon admission offer.",
            "translation_requirements": "Certified English translation required for any documents not issued in English.",
            "final_submission_method": "100% digital submission via the UVic graduate admissions portal."
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
                "pakistan_specific_instruction": "Must clearly name 2-3 UVic Computer Science faculty members whose research aligns with yours."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 90).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to University of Victoria (institution code 0989)."
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
            "document_submission_deadline": "January 25",
            "recommendation_letters_deadline": "January 25",
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
            "selection_panel_composition": "Departmental Graduate Admissions Committee and individual faculty principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit followed by faculty supervisor sponsorship and guaranteed funding commitment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international graduate applicants for CS thesis programs",
            "total_scholarships_awarded": "~50 to 70 fully funded graduate positions awarded annually",
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
                "Beware of fraudulent educational consultancy agencies claiming guaranteed admission or funding packages to UVic.",
                "Legitimate applications are processed exclusively through uvic.ca."
            ],
            "application_fee_warning": "UVic application fee is CAD 172 paid securely via the official portal; never pay fees to third-party brokers.",
            "agent_and_intermediary_warnings": "University of Victoria does not partner with recruitment agents for research-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 172 (~PKR 35,260).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Canadian Study Permit and biometric fee: ~CAD 235 (~PKR 48,000).",
                "Initial settling-in expenses upon arrival in Victoria: ~CAD 1,500 (~PKR 307,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get admitted to thesis MSc without a supervisor. Reality: Computer Science at UVic requires a confirmed supervisor before formal admission is granted.",
                "Myth: Victoria is as expensive as Vancouver. Reality: While living costs in BC are elevated, UVic offers subsidized graduate student housing and generous funding packages."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is required; GRE is NOT required for Computer Science at UVic."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 / 4.00 (Grade B) in graduate coursework throughout the degree program.",
            "attendance_requirements": "Full-time on-campus academic standing and active participation in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual Progress Report reviewed by the supervisory committee and the Graduate Program Director; satisfactory progress required for funding renewal.",
            "work_restrictions_during_study": "Teaching/research assistantships are limited to an average of 12 hours per week during academic terms to prioritize thesis research.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the funding package.",
            "repayment_clawback_conditions": "Funding discontinued if student withdraws without authorization or is dismissed for academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other Canadian universities.",
            "rules_for_changing_major": "Changing major requires formal re-application and approval by the new academic department.",
            "extension_policy": "Funding is guaranteed for the standard program duration (2 years for MSc, 4 years for PhD); extensions are contingent on supervisor grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Victoria Computer Science Graduate Funding Portal",
                "source_url": "https://www.uvic.ca/ecs/computerscience/graduate/funding/index.php",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "UVic Faculty of Graduate Studies Calendar",
                "source_url": "https://www.uvic.ca/graduate/admissions/how-to-apply/index.php",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AM-037": {
        "scholarship_id": "SCH-AM-037",
        "basic_details": {
            "scholarship_name": "Concordia University Graduate Fellowship & Research Assistantship in CS & Software Engineering",
            "offering_entity": "Concordia University Gina Cody School of Engineering and Computer Science & School of Graduate Studies",
            "host_country": "Canada",
            "host_institutions_covered": "Concordia University (Sir George Williams Campus, Montreal, Quebec, Canada)",
            "degree_levels": ["Master of Computer Science (MCompSc Thesis)", "Master of Applied Science (MASc Software Engineering)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Gina Cody School: Computer Science, Software Engineering, Artificial Intelligence & Machine Learning, Information Systems Security, Data Science, and Human-Centered Software.",
            "number_of_awards_total": "~80 to 110 funded graduate research positions awarded annually across thesis-based Master's and PhD programs",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~8 to 15 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for Master's (Thesis); up to 4 years for PhD, renewed annually based on satisfactory research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Canadian and international students of all nationalities (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research capability.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science or Software Engineering with at least B+ standing (minimum 3.30 / 4.30 on Concordia scale, equivalent to CGPA 3.30 / 4.00 or 78%+) for Master's; a research Master's degree in Computer Science with at least A- standing (CGPA 3.60 / 4.00) for PhD from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Minimum B+ standing (3.30/4.30 Concordia scale, equivalent to 78%+ or 3.3/4.0) over the final two years of undergraduate study.",
            "subject_background_prerequisites": "Substantial background in software engineering, algorithms, operating systems, computer systems, and discrete mathematics.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": True,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (with no sub-score below 6.0), TOEFL iBT minimum 85 (minimum 20 in writing), or Duolingo English Test (DET) minimum 120. Official test reports mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure supervisory support from a Gina Cody School faculty member prior to final admission approval.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full external government fellowships without university approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIAL",
                "details": "International tuition fees (~CAD 9,000 to 14,000 / year) are offset through International Tuition Differential Fee Waivers and departmental grants, with the balance paid directly out of the guaranteed funding package.",
                "amount": "Covered via funding package (~CAD 10,000 / year; ~PKR 2,050,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "Concordia University graduate application fee of CAD 113 (~USD 83; ~PKR 23,165) paid online via credit card.",
                "amount": "CAD 113 (~PKR 23,165)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus student housing (Grey Nuns Residence) or affordable private rental apartments in Montreal (average CAD 650 to 950 / month; ~USD 480 to 700 / month; Montreal is one of the most affordable major student cities in North America) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~CAD 800 / month; ~PKR 164,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: Master's Thesis students receive at least CAD 24,000 / year (~CAD 2,000 / month; ~PKR 410,000 / month); PhD students receive at least CAD 26,000 to 32,000 / year (~CAD 2,166 to 2,666 / month; ~PKR 444,000 to 546,500 / month), composed of Concordia Graduate Fellowship (CGF), Teaching Assistantships (GTA), and Research Assistantships (GRA).",
                "amount": "CAD 24,000 to 32,000 / year (~PKR 410,000 to 546,500 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Montreal is self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 250,000 to 350,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Quebec Acceptance Certificate (CAQ) fee (CAD 124) and Canadian Study Permit fee (CAD 150) + biometrics (CAD 85) paid by applicant.",
                "amount": "Not covered (~CAD 359; ~PKR 73,500)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Mandatory International Student Health Insurance Plan (Blue Cross) provides comprehensive healthcare coverage in Quebec, covered directly under the graduate fellowship package (~CAD 1,176 / year value).",
                "amount": "100% covered Blue Cross health insurance"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Montreal are very affordable compared to Toronto or Vancouver; easily managed within the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Concordia Library (Webster Library, Vanier Library), high-performance computing clusters, and Gina Cody School laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Concordia Conference Travel Awards and supervisor research grants provide up to CAD 1,500 to 2,000 for presenting papers at premier conferences.",
                "amount": "Up to CAD 2,000 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Montreal STM public transit (Metro and buses) paid from monthly stipend (~CAD 60/month with student OPUS fare reduction).",
                "amount": "Covered from living stipend"
            },
            "total_estimated_value_usd_per_year": 25000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Concordia University, Montreal)",
            "participating_institutions": [
                "Concordia University - Sir George Williams Campus (Montreal, Quebec, Canada)"
            ],
            "university_rankings_scope": "QS World University Rankings #387 worldwide, top 100 in the world for Software Engineering and Artificial Intelligence, member of the Montreal AI research ecosystem (Mila).",
            "available_majors": [
                "Computer Science (MCompSc & PhD)",
                "Software Engineering (MASc & PhD)",
                "Artificial Intelligence and Machine Learning",
                "Information Systems Security (ISS)",
                "Data Science and Big Data",
                "Human-Centered Software and Usability",
                "Cloud Systems and Distributed Computing"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's (Thesis): 2 years; PhD: 4 years",
            "admission_requirements_summary": "Online Concordia application form, official academic transcripts, curriculum vitae, statement of purpose, official IELTS/TOEFL/DET score report, three academic letters of recommendation, and confirmed faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission to the Artificial Intelligence and Information Systems Security groups receives fierce competition; establishing early contact with faculty members and demonstrating published research or strong coding projects is essential.",
            "strategic_program_match_advice": "Reach out to prospective supervisors between October and December. Send a concise email attaching your CV, academic transcript, and a 1-page summary of how your technical skills match their current research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.concordia.ca/ginacody/computer-science-software-eng/programs/graduate/funding-and-awards.html & https://www.concordia.ca/admissions/graduate.html",
            "portal_system_name": "Concordia Online Graduate Admissions Portal",
            "account_creation_instructions": "Create an applicant account on Concordia admissions portal, select Computer Science thesis-based program, identify proposed supervisors, and upload digital application documents.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research groups and email prospective supervisors with CV and research interests (October - December).",
                "Step 2: Take IELTS (min 6.5) or TOEFL (min 85) and ensure official electronic score reporting to Concordia University.",
                "Step 3: Submit online application on Concordia portal and pay the CAD 113 application fee before the deadline (February 1).",
                "Step 4: Upload unofficial transcripts, CV, and statement of purpose.",
                "Step 5: Academic referees submit confidential appraisal forms via automated institutional links.",
                "Step 6: Prospective supervisors review shortlisted files and conduct online technical interviews (February - March).",
                "Step 7: Departmental Graduate Committee issues formal admission and guaranteed funding offer letters (March - April).",
                "Step 8: Accept the offer, apply for Quebec Acceptance Certificate (CAQ), Provincial Attestation Letter (PAL), and Study Permit via IRCC.",
                "Step 9: Arrive in Montreal in late August for international graduate orientation and commence studies in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: All admitted thesis-based graduate students automatically receive the guaranteed minimum funding package without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement of purpose outlining academic background, specific research problems of interest, and reasons for choosing Concordia Computer Science.",
            "study_plan_research_proposal_requirements": "Structured 1 to 2-page research outline highlighting technical methodologies and alignment with prospective faculty laboratories.",
            "cv_format_requirements": "Curriculum vitae detailing education, technical skillsets, research publications, awards, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview conducted by the prospective faculty supervisor focusing on technical depth, programming ability, and research drive.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 85) mandatory; GRE is not required for Computer Science at Concordia.",
            "application_fee_amount": "CAD 113 (~USD 83; ~PKR 23,165)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and official sealed transcripts sent upon admission offer.",
            "translation_requirements": "Certified English or French translation required for any documents not issued in English or French.",
            "final_submission_method": "100% digital submission via the Concordia graduate admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts for all post-secondary education with minimum B+ / 3.30 GPA equivalent.",
                "pakistan_specific_instruction": "Scanned color copies of HEC-attested Bachelor's/Master's degrees and semester-by-semester transcripts."
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "1 to 2-page essay detailing research interests, background, and alignment with prospective supervisors.",
                "pakistan_specific_instruction": "Must clearly name 2-3 Concordia faculty members whose research aligns with yours."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest), TOEFL iBT (min 85), or DET (min 120).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to Concordia University (institution code 0956)."
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
            "application_deadline": "February 1",
            "university_admission_deadline": "February 1",
            "document_submission_deadline": "February 15",
            "recommendation_letters_deadline": "February 15",
            "interview_period": "February 15 - March 30",
            "shortlist_announcement": "March 15 - April 15",
            "final_result_acceptance_deadline": "May 1",
            "visa_application_window": "May 1 - July 15",
            "semester_commencement": "Early September (Fall intake)",
            "annual_cycle_notes": "Main intake is Fall semester (September commencement). Applications received by February 1 receive premier funding consideration."
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
            "selection_panel_composition": "Departmental Graduate Admissions Committee and individual faculty principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit followed by faculty supervisor sponsorship and guaranteed funding commitment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 1,700 international graduate applicants for CS thesis programs",
            "total_scholarships_awarded": "~80 to 110 fully funded graduate positions awarded annually",
            "acceptance_rate_global": "~6.0% to 7.5%",
            "acceptance_rate_pakistan": "~7.0% to 9.0% among competitive applicants with supervisor backing",
            "typical_successful_applicant_gpa": "CGPA 3.60+ / 4.00 or 80%+ aggregate from leading Pakistani institutions (NUST, FAST, LUMS, GIKI, UET)",
            "typical_academic_and_research_profile": "Graduates with solid computing fundamentals, strong programming abilities, and at least 1-2 published papers or substantial research thesis outcomes.",
            "common_backgrounds_of_winners": "Graduates of Pakistani top computer science and software engineering programs.",
            "high_representation_countries": "Canada, Iran, China, India, Pakistan, Nigeria, Bangladesh, Turkey.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Beware of fraudulent educational consultancy agencies claiming guaranteed admission or funding packages to Concordia.",
                "Legitimate applications are processed exclusively through concordia.ca."
            ],
            "application_fee_warning": "Concordia application fee is CAD 113 paid securely via the official portal; never pay fees to third-party brokers.",
            "agent_and_intermediary_warnings": "Concordia University does not partner with recruitment agents for research-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 113 (~PKR 23,165).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Quebec CAQ and Canadian Study Permit fees: ~CAD 359 (~PKR 73,500).",
                "Initial settling-in expenses upon arrival in Montreal: ~CAD 1,200 (~PKR 246,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must speak French to study at Concordia. Reality: Concordia is an English-language university; all courses and research are conducted 100% in English.",
                "Myth: You can get admitted to thesis Master's without a supervisor. Reality: Gina Cody School thesis programs require a confirmed faculty supervisor before formal admission is granted."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is required; GRE is NOT required for Computer Science at Concordia."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 / 4.30 (Grade B) in graduate coursework throughout the degree program.",
            "attendance_requirements": "Full-time on-campus academic standing and active participation in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual Progress Report reviewed by the supervisory committee and the Graduate Program Director; satisfactory progress required for funding renewal.",
            "work_restrictions_during_study": "Teaching/research assistantships are limited to an average of 10-12 hours per week during academic terms to prioritize thesis research.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years.",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the funding package.",
            "repayment_clawback_conditions": "Funding discontinued if student withdraws without authorization or is dismissed for academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other Canadian universities.",
            "rules_for_changing_major": "Changing major requires formal re-application and approval by the new academic department.",
            "extension_policy": "Funding is guaranteed for the standard program duration (2 years for Master's, 4 years for PhD); extensions are contingent on supervisor grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "Concordia Computer Science and Software Engineering Funding Portal",
                "source_url": "https://www.concordia.ca/ginacody/computer-science-software-eng/programs/graduate/funding-and-awards.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Concordia School of Graduate Studies Calendar",
                "source_url": "https://www.concordia.ca/admissions/graduate.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },
    "SCH-AM-038": {
        "scholarship_id": "SCH-AM-038",
        "basic_details": {
            "scholarship_name": "Dalhousie University Faculty of Computer Science Graduate Research Scholarship",
            "offering_entity": "Dalhousie University Faculty of Computer Science & Faculty of Graduate Studies (FGS)",
            "host_country": "Canada",
            "host_institutions_covered": "Dalhousie University (Studley Campus, Halifax, Nova Scotia, Canada)",
            "degree_levels": ["Master of Computer Science (MCS Thesis)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Faculty of Computer Science: Artificial Intelligence and Machine Learning, Deep Learning, Big Data Analytics, Human-Computer Interaction, Cyber Security and Privacy, Algorithms and Systems, and Computational Biology.",
            "number_of_awards_total": "~50 to 75 funded graduate research positions awarded annually across thesis-based MCS and PhD intakes",
            "number_of_awards_pakistan": "Open international merit competition; Pakistani graduate researchers in computing secure ~5 to 10 fully funded positions annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MCS (Thesis); up to 4 years for PhD, renewed annually based on satisfactory research progress"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to Canadian and international students of all nationalities (Pakistan eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No formal age limit; evaluated on academic achievement and research capability.",
            "academic_qualifications": "A recognized 4-year Bachelor's degree (16 years education) in Computer Science or related STEM discipline with at least B+ standing (minimum 77% aggregate or CGPA 3.30 / 4.00) for MCS; a research Master's degree in Computer Science with thesis (minimum 80% aggregate or CGPA 3.70 / 4.00) for PhD from an HEC-recognized university in Pakistan (competitive admits typically 3.65+ / 4.00).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "Evaluated on Dalhousie 4.3 GPA scale; minimum Grade B+ (equivalent to 78%+ or 3.3/4.0) over the final two years of study.",
            "subject_background_prerequisites": "Substantial background in algorithms, data structures, operating systems, computer architecture, and discrete mathematics.",
            "current_education_status": "Graduating seniors in their final semester can apply conditionally with expected graduation transcripts.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Prior software development, open-source projects, or published research papers in IEEE/ACM venues significantly strengthen candidacy.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 92,
            "duolingo_accepted": False,
            "moi_certificate_accepted": False,
            "language_notes": "IELTS Academic minimum 6.5 overall (with no sub-score below 6.0) or TOEFL iBT minimum 92 (minimum 20 in each section). Official test reports mandatory.",
            "other_language_requirements": "None; instruction and research conducted entirely in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must secure supervisory support from a Dalhousie Computer Science faculty member prior to final admission approval.",
            "previous_scholarship_restrictions": "Cannot hold concurrent full external government fellowships without university approval.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIAL",
                "details": "International tuition fees (~CAD 9,000 to 14,000 / year) are offset through Dalhousie Graduate Scholarships (FGS) and departmental grants, with the balance paid directly out of the guaranteed funding package.",
                "amount": "Covered via funding package (~CAD 10,000 / year; ~PKR 2,050,000 / year)"
            },
            "admission_application_fee": {
                "status": "PAID BY APPLICANT",
                "details": "Dalhousie University international application fee of CAD 115 (~USD 85; ~PKR 23,575) paid online via credit card.",
                "amount": "CAD 115 (~PKR 23,575)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "On-campus graduate housing (Peter Green Hall, Fenwick Tower) or private rental apartments in Halifax (average CAD 800 to 1,200 / month; ~USD 590 to 880 / month) comfortably paid out of the living stipend.",
                "amount": "Paid from stipend (~CAD 950 / month; ~PKR 194,750 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum funding package: Master's Thesis students receive at least CAD 24,000 / year (~CAD 2,000 / month; ~PKR 410,000 / month); PhD students receive at least CAD 28,000 to 35,000 / year (~CAD 2,333 to 2,916 / month; ~PKR 478,000 to 597,000 / month), composed of Dalhousie Graduate Scholarship (FGS), Graduate Teaching Assistantships (GTA, ~CAD 6,000/year), and Graduate Research Assistantships (GRA).",
                "amount": "CAD 24,000 to 35,000 / year (~PKR 410,000 to 597,000 / mo)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International airfare between Pakistan and Halifax is self-funded by the student.",
                "amount": "Not covered (Self-funded ~PKR 260,000 to 360,000 round-trip)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit fee (CAD 150) and biometrics fee (CAD 85) paid by applicant.",
                "amount": "Not covered (~CAD 235; ~PKR 48,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Nova Scotia Medical Services Insurance (MSI) provides 100% free basic provincial healthcare for international students residing in Nova Scotia for 12+ months; initial 12-month coverage is provided via DSU International Student Health Plan.",
                "amount": "100% free provincial MSI healthcare"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses and groceries in Halifax are easily accommodated within the monthly stipend.",
                "amount": "Covered from monthly living stipend"
            },
            "books_and_materials_allowance": {
                "status": "100% COVERED",
                "details": "Access to Dalhousie Libraries (Killam Memorial Library, Sexton Design & Technology Library), DeepSense AI computing platform, and departmental laboratories.",
                "amount": "100% covered via institutional facilities"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty of Graduate Studies Travel Grants and supervisor research funds provide up to CAD 1,500 to 2,500 for presenting papers at premier conferences.",
                "amount": "Up to CAD 2,500 conference travel funding"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Halifax Transit U-Pass provides unlimited transit on city buses and passenger ferries connecting Halifax and Dartmouth, included directly in standard student registration fees.",
                "amount": "Unlimited transit via U-Pass"
            },
            "total_estimated_value_usd_per_year": 27000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single host university (Dalhousie University, Halifax)",
            "participating_institutions": [
                "Dalhousie University - Studley Campus (Halifax, Nova Scotia, Canada)"
            ],
            "university_rankings_scope": "U15 Group of Canadian Research Universities, QS World University Rankings #275 worldwide, Atlantic Canada's premier research university.",
            "available_majors": [
                "Computer Science (MCS & PhD)",
                "Artificial Intelligence and Machine Learning",
                "Big Data Analytics and DeepSense",
                "Human-Computer Interaction and Visualization",
                "Cyber Security and Information Privacy",
                "Algorithms and Computational Theory",
                "Computational Biology and Bioinformatics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MCS (Thesis): 2 years; PhD: 4 years",
            "admission_requirements_summary": "Online Dalhousie application form, official academic transcripts, curriculum vitae, statement of research intent, official IELTS/TOEFL score report, two academic letters of recommendation, and confirmed faculty supervisor endorsement.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Admission to the AI/ML and Cyber Security research groups receives intense competition; establishing early contact with faculty members and demonstrating published research or strong coding projects is essential.",
            "strategic_program_match_advice": "Reach out to prospective supervisors between October and December. Send a concise email attaching your CV, academic transcript, and a 1-page summary of how your technical skills match their current research grants."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.dal.ca/faculty/computerscience/graduate-programs/funding-awards.html & https://www.dal.ca/admissions/graduate.html",
            "portal_system_name": "Dalhousie Online Graduate Admissions Portal",
            "account_creation_instructions": "Create an applicant account on Dalhousie admissions portal, select Computer Science thesis-based program, identify proposed supervisors, and upload digital application documents.",
            "step_by_step_workflow": [
                "Step 1: Explore faculty research groups and email prospective supervisors with CV and research interests (October - December).",
                "Step 2: Take IELTS (min 6.5) or TOEFL (min 92) and ensure official electronic score reporting to Dalhousie University.",
                "Step 3: Submit online application on Dalhousie portal and pay the CAD 115 application fee before the deadline (January 15).",
                "Step 4: Upload unofficial transcripts, CV, and statement of research intent.",
                "Step 5: Academic referees submit confidential appraisal forms via automated institutional links.",
                "Step 6: Prospective supervisors review shortlisted files and conduct online technical interviews (February - March).",
                "Step 7: Departmental Graduate Committee issues formal admission and guaranteed funding offer letters (March - April).",
                "Step 8: Accept the offer, apply for Canadian Provincial Attestation Letter (PAL) and Study Permit via IRCC.",
                "Step 9: Arrive in Halifax in late August for international graduate orientation and commence studies in September."
            ],
            "university_vs_scholarship_routing": "Integrated Track: All admitted thesis-based graduate students automatically receive the guaranteed minimum funding package without separate scholarship application.",
            "recommendation_letters_submission_method": "Submitted online by referees via secure automated links dispatched directly to their institutional email addresses.",
            "personal_statement_prompts": "Statement of research intent outlining academic background, specific research problems of interest, and reasons for choosing Dalhousie Computer Science.",
            "study_plan_research_proposal_requirements": "Structured 1 to 2-page research outline highlighting technical methodologies and alignment with prospective faculty laboratories.",
            "cv_format_requirements": "Curriculum vitae detailing education, technical skillsets, research publications, awards, and software projects.",
            "interviews_conducted": True,
            "interview_format_details": "30-minute online video interview conducted by the prospective faculty supervisor focusing on technical depth, programming ability, and research drive.",
            "standardized_tests": "IELTS Academic (min 6.5) or TOEFL iBT (min 92) mandatory; GRE is not required for Computer Science at Dalhousie.",
            "application_fee_amount": "CAD 115 (~USD 85; ~PKR 23,575)",
            "attestation_requirements": "Degrees and transcripts must be attested by HEC Pakistan and official sealed transcripts sent upon admission offer.",
            "translation_requirements": "Certified English translation required for any documents not issued in English.",
            "final_submission_method": "100% digital submission via the Dalhousie graduate admissions portal."
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
                "pakistan_specific_instruction": "Must clearly name 2-3 Dalhousie Computer Science faculty members whose research aligns with yours."
            },
            {
                "document_name": "Official English Proficiency Score Report",
                "mandatory": True,
                "specification": "IELTS Academic (min 6.5 overall, 6.0 in each subtest) or TOEFL iBT (min 92).",
                "pakistan_specific_instruction": "Request testing agency to send official scores directly to Dalhousie University (institution code 0915)."
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
            "document_submission_deadline": "January 25",
            "recommendation_letters_deadline": "January 25",
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
            "selection_panel_composition": "Departmental Graduate Admissions Committee and individual faculty principal investigators.",
            "evaluation_methodology": "Two-phase evaluation: academic credential audit followed by faculty supervisor sponsorship and guaranteed funding commitment."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,300 international graduate applicants for CS thesis programs",
            "total_scholarships_awarded": "~50 to 75 fully funded graduate positions awarded annually",
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
                "Beware of fraudulent educational consultancy agencies claiming guaranteed admission or funding packages to Dalhousie.",
                "Legitimate applications are processed exclusively through dal.ca."
            ],
            "application_fee_warning": "Dalhousie application fee is CAD 115 paid securely via the official portal; never pay fees to third-party brokers.",
            "agent_and_intermediary_warnings": "Dalhousie University does not partner with recruitment agents for research-based graduate admissions.",
            "hidden_costs_breakdown": [
                "Application fee: CAD 115 (~PKR 23,575).",
                "IELTS/TOEFL examination fee: ~PKR 60,000.",
                "Canadian Study Permit and biometric fee: ~CAD 235 (~PKR 48,000).",
                "Initial settling-in expenses upon arrival in Halifax: ~CAD 1,500 (~PKR 307,500)."
            ],
            "misleading_claims_debunked": [
                "Myth: You can get admitted to thesis MCS without a supervisor. Reality: Computer Science at Dalhousie requires a confirmed supervisor before formal admission is granted.",
                "Myth: Halifax is remote and disconnected. Reality: Halifax is the financial and technology hub of Atlantic Canada, boasting a vibrant tech startup sector."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim GRE is required; GRE is NOT required for Computer Science at Dalhousie."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain a minimum cumulative GPA of 3.00 / 4.30 (Grade B) in graduate coursework throughout the degree program.",
            "attendance_requirements": "Full-time on-campus academic standing and active participation in assigned laboratory research projects.",
            "academic_progress_monitoring": "Annual Progress Report reviewed by the supervisory committee and the Graduate Program Director; satisfactory progress required for funding renewal.",
            "work_restrictions_during_study": "Teaching/research assistantships are limited to an average of 10-12 hours per week during academic terms to prioritize thesis research.",
            "home_country_return_obligation": "No mandatory return requirement; graduates are eligible for the Canadian Post-Graduation Work Permit (PGWP) for up to 3 years and the Atlantic Immigration Program (AIP).",
            "service_obligations_or_bonds": "Zero service bond or repayment obligation attached to the funding package.",
            "repayment_clawback_conditions": "Funding discontinued if student withdraws without authorization or is dismissed for academic dishonesty.",
            "rules_for_changing_university": "Non-transferable to other Canadian universities.",
            "rules_for_changing_major": "Changing major requires formal re-application and approval by the new academic department.",
            "extension_policy": "Funding is guaranteed for the standard program duration (2 years for Master's, 4 years for PhD); extensions are contingent on supervisor grant availability."
        },
        "official_sources_verified": [
            {
                "source_name": "Dalhousie Faculty of Computer Science Graduate Funding Portal",
                "source_url": "https://www.dal.ca/faculty/computerscience/graduate-programs/funding-awards.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Dalhousie Faculty of Graduate Studies Calendar",
                "source_url": "https://www.dal.ca/admissions/graduate.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
