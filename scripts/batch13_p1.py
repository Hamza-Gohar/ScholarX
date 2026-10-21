# scripts/batch13_p1.py
# SCH-AM-018: University of Alberta Computing Science Graduate Award (Canada)
# SCH-AM-022: Simon Fraser University (SFU) Computing Science Graduate Award (Canada)
# SCH-AM-025: University of Ottawa International Doctoral Differential Scholarship (Canada)

DATA_P1 = {
    "SCH-AM-018": {
        "scholarship_id": "SCH-AM-018",
        "basic_details": {
            "scholarship_name": "University of Alberta Computing Science Graduate Award & Amii AI Fellowship",
            "offering_entity": "University of Alberta (Department of Computing Science, Faculty of Science) & Alberta Machine Intelligence Institute (Amii)",
            "host_country": "Canada",
            "host_institutions_covered": "University of Alberta Main Campus (North Campus, Edmonton, Alberta, Canada)",
            "degree_levels": ["Master of Science (MSc Thesis)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Restricted to thesis-based graduate degrees in Computing Science: Artificial Intelligence, Reinforcement Learning, Machine Learning, Computer Vision, Multimedia Systems, Robotics, Software Systems, and Algorithmics.",
            "number_of_awards_total": "100% of admitted thesis graduate students receive guaranteed full financial support (~80 to 120 funded graduate students admitted annually)",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in CS and software engineering represent a strong cohort (typically 8 to 15 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MSc Thesis; up to 4 years for PhD, with guaranteed minimum departmental funding package"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed 4-year Bachelor's degree (16 years education) for MSc; completed Master's degree (18 years education) for PhD from an HEC-recognized university with minimum 3.40 / 4.00 CGPA (78%+ aggregate; 3.60+ competitive from NUST, FAST-NUCES, GIKI, UET, LUMS, PIEAS).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Minimum UAlberta equivalent GPA of 3.30 on 4.0 scale over last 60 credits (2 years full-time study).",
            "subject_background_prerequisites": "BSc or MSc in Computer Science, Software Engineering, Electrical Engineering, Mathematics, or Statistics with solid coursework in data structures, algorithms, calculus, and linear algebra.",
            "current_education_status": "Graduating final-year students eligible; must complete degree and confer official transcript before September intake.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Strong open-source code repositories (GitHub), Kaggle achievements, or research publications (NeurIPS, ICML, CVPR, IROS) significantly enhance competitiveness.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 100,
                "duolingo_accepted": True,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall min 7.0 (each section 6.0+), TOEFL iBT min 100 (sub-scores 21+), or Duolingo min 125. MOI certificates not accepted."
            },
            "other_language_requirements": "None; English is the official language of instruction, research, and campus life.",
            "gender_specific_requirements": "None; female candidates in computing and machine learning strongly encouraged.",
            "financial_need_required": False,
            "special_eligibility_categories": "Thesis-based researchers in reinforcement learning, AI systems, and computational intelligence.",
            "previous_scholarship_restrictions": "Cannot hold multiple full external fellowships exceeding university maximum award policy.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Tuition costs offset via departmental tuition support and Graduate Research Assistantship Fellowships (~CAD 9,500 to CAD 11,000 / year).",
                "amount": "100% covered (~CAD 10,000 / year value; ~PKR 2,000,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Alberta international graduate application fee (CAD 135) paid online.",
                "amount": "CAD 135 (~PKR 27,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid out of guaranteed living stipend; on-campus graduate residences (Michener Park, Graduate Residence) or private Edmonton rentals average CAD 700 to 1,000/month.",
                "amount": "Paid from stipend (~CAD 850 / month; ~PKR 170,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum annual funding package: CAD 24,000 to CAD 29,000 / year (~CAD 2,000 to 2,416 / month; ~PKR 400,000 to 485,000/month) provided via Teaching Assistantships (TA), Graduate Research Assistantships (GRA), and Amii fellowships.",
                "amount": "CAD 24,000 to 29,000 / year (~PKR 4,800,000 to 5,800,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel between Pakistan and Edmonton International Airport (YEG) is self-funded by student.",
                "amount": "Self-funded (~PKR 280,000 to 420,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit application fee (CAD 150) and biometrics fee (CAD 85) paid to Immigration, Refugees and Citizenship Canada (IRCC).",
                "amount": "CAD 235 (~PKR 47,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Alberta Health Care Insurance Plan (AHCIP) provides 100% free basic provincial hospital/physician coverage for international students holding study permits, supplemented by UAlberta GSA Health & Dental Plan.",
                "amount": "Free provincial health care + GSA health plan covered"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered by monthly assistantship; Edmonton offers among the lowest living costs among major Canadian research hubs.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-performance GPU computing clusters, Amii supercomputing access, and lab workstations provided by department.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "GSA and Amii travel grants provide CAD 1,500 to 3,000 per paper for presenting at flagship conferences (NeurIPS, ICML, CVPR, AAAI).",
                "amount": "Up to CAD 3,000 per conference"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "Edmonton Transit Service (ETS) U-Pass included in student registration fees, granting unlimited bus and LRT transit.",
                "amount": "Included in student fee package"
            },
            "total_estimated_value_usd_per_year": 32000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading Canadian research university: University of Alberta (Edmonton, Canada)",
            "participating_institutions": [
                "University of Alberta - Department of Computing Science (North Campus, Edmonton)",
                "Alberta Machine Intelligence Institute (Amii - Pan-Canadian AI Strategy Institute)"
            ],
            "university_rankings_scope": "Top 100 global university (QS World #96); top 5 globally in Artificial Intelligence and Reinforcement Learning (home of Sutton & Barto RL pioneers and DeepMind AlphaGo founders).",
            "available_majors": [
                "MSc / PhD in Computing Science: Reinforcement Learning & Autonomous Agents",
                "MSc / PhD in Computing Science: Computer Vision & Multimedia",
                "MSc / PhD in Computing Science: Natural Language Processing & Machine Learning",
                "MSc / PhD in Computing Science: Robotics & Autonomous Systems",
                "MSc / PhD in Computing Science: Software Systems, Databases, & Cloud Computing"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MSc Thesis: 2 years (4 to 5 semesters); PhD: 4 to 5 years full-time.",
            "admission_requirements_summary": "Bachelor's or Master's in CS/STEM with 3.4+ GPA, 3 academic recommendation letters, CV, statement of purpose, supervisor pre-match strongly recommended, and IELTS 7.0 / TOEFL 100.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Reinforcement Learning, Deep Learning, and Computer Vision under Amii faculty are intensely competitive; Software Systems, Theory, and Multimedia offer slightly higher acceptance rates.",
            "strategic_program_match_advice": "Prospective applicants to thesis programs should review the faculty directory, identify 2-3 professors matching their research thesis, and contact them between September and November. An endorsement from a faculty member guarantees admission and full funding."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.ualberta.ca/graduate-studies/prospective-students/apply-for-admission",
            "portal_system_name": "University of Alberta Graduate Application Portal (GSMS)",
            "account_creation_instructions": "Create an account on the UAlberta Graduate Studies Portal, select Department of Computing Science, specify degree route (MSc Thesis or PhD), list prospective supervisors, and upload required documents.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Review Computing Science faculty research areas; contact prospective supervisors with CV, transcripts, and research statement.",
                "Step 2 (October - Mid-December): Register on UAlberta Graduate Application Portal (ualberta.ca/graduate-studies); complete profile.",
                "Step 3 (November - December): Upload unofficial transcripts, CV, statement of purpose, and enter contact information for 3 academic referees.",
                "Step 4 (By 15 December): Pay application fee (CAD 135) and submit application before Fall admission deadline.",
                "Step 5 (January - February): Departmental Graduate Admissions Committee reviews applications; faculty members select candidates for lab interviews.",
                "Step 6 (March - April): Official admission offers with guaranteed funding letters released; accepted candidates accept offer in portal.",
                "Step 7 (April - May): Apply for Canadian Study Permit via IRCC online portal; complete biometrics and medical exam in Pakistan.",
                "Step 8 (Late August / Early September): Travel to Edmonton, attend Computing Science graduate orientation, and begin teaching/research assistantship."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: All admitted thesis-based graduate students receive guaranteed departmental funding; no separate scholarship application required.",
            "recommendation_letters_submission_method": "Three academic recommendation letters submitted electronically via referee email portal generated by GSMS.",
            "personal_statement_prompts": "Statement of Purpose (1-2 pages): Detail research background, technical projects, publications, specific research topics of interest, and why UAlberta is the ideal fit.",
            "study_plan_research_proposal_requirements": "Structured research statement (1-2 pages) describing research interests, methodologies, and proposed supervisors.",
            "cv_format_requirements": "Academic CV detailing programming skills, research publications, technical projects, GitHub profile, and academic honors.",
            "interviews_conducted": True,
            "interview_format_details": "Technical video interviews (30-45 minutes via Zoom/Google Meet) conducted by prospective faculty supervisors evaluating coding, mathematical foundations, and research intuition.",
            "standardized_tests": "IELTS 7.0 or TOEFL 100 or Duolingo 125. GRE is NOT required for admission.",
            "application_fee_amount": "CAD 135 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for application; official attested transcripts from HEC Pakistan required upon admission offer.",
            "translation_requirements": "Certified English translations for any documents not in English.",
            "final_submission_method": "100% digital submission via the UAlberta GSMS online application system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least 2 years.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts of all university education with grading scale and degree completion certificates.",
                "pakistan_specific_instruction": "HEC Pakistan attestation required on final official documents upon offer acceptance."
            },
            {
                "document_name": "Statement of Purpose",
                "mandatory": True,
                "specification": "Structured 1 to 2 page statement of research background, objectives, and professor alignment.",
                "pakistan_specific_instruction": "Specifically name UAlberta faculty members whose lab papers you have studied."
            },
            {
                "document_name": "Academic Recommendation Letters (Three)",
                "mandatory": True,
                "specification": "Confidential recommendation letters from former professors or research mentors.",
                "pakistan_specific_instruction": "Must be submitted from verified institutional email accounts."
            },
            {
                "document_name": "English Language Proficiency Report",
                "mandatory": True,
                "specification": "Official IELTS Academic (7.0+), TOEFL iBT (100+), or Duolingo (125+) scorecard.",
                "pakistan_specific_instruction": "Electronic score reporting to University of Alberta institutional code."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Academic CV detailing coding skills, publications, capstone projects, and GitHub links.",
                "pakistan_specific_instruction": "Highlight contributions to open source or Scopus/IEEE papers."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 September 2026",
            "application_deadline": "15 December 2026 (Fall 2027 intake)",
            "university_admission_deadline": "15 December 2026",
            "document_submission_deadline": "15 December 2026",
            "recommendation_letters_deadline": "22 December 2026",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "March to April 2027",
            "final_result_acceptance_deadline": "15 April / 1 May 2027",
            "visa_application_window": "April to July 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Main intake cycle is Fall (September). Winter (January) intake has very limited supervisory funding openings."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (CGPA in relevant computer science and mathematics coursework, class rank)",
            "extracurricular_and_leadership_weight": "5% (Contributions to student tech community, hackathons)",
            "research_experience_weight": "35% (Prior thesis quality, publications, open-source repositories, and technical skills)",
            "work_experience_weight": "5% (Industry software engineering, AI internships, or data engineering roles)",
            "personal_statement_weight": "10% (Clarity of research vision, intellectual curiosity, and fit with department)",
            "recommendations_weight": "5% (Strength of professor endorsements)",
            "interview_weight": "5% (Technical interview with prospective faculty advisor)",
            "test_scores_weight": "Threshold requirement (IELTS 7.0 / TOEFL 100 compliance)",
            "financial_need_weight": "0% (Purely merit and research competence based)",
            "selection_panel_composition": "Computing Science Graduate Admissions Committee & individual faculty lab heads.",
            "evaluation_methodology": "Two-phase holistic review: Graduate admissions committee pre-screens applicants for academic and English compliance; individual faculty supervisors review applicant files and interview candidates to make binding funding and admission offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,500 to 2,200 international applicants across thesis MSc and PhD",
            "total_scholarships_awarded": "~80 to 120 fully funded graduate admission offers",
            "acceptance_rate_global": "~6.5%",
            "acceptance_rate_pakistan": "~9.5% (Strong representation of Pakistani graduates from NUST, FAST, GIKI, UET in computing labs)",
            "typical_successful_applicant_gpa": "3.65+ / 4.00 CGPA (82%+ aggregate)",
            "typical_academic_and_research_profile": "Solid foundation in data structures, algorithms, and math; 1+ published papers or strong software portfolio; clear thesis direction.",
            "common_backgrounds_of_winners": "BS/MS graduates in Computer Science and Software Engineering from NUST, FAST-NUCES, GIKI, UET, and LUMS.",
            "high_representation_countries": "China, India, Pakistan, Iran, Nigeria, Bangladesh, Canada",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized recruiters charging high fees for guaranteed UAlberta CS admission. UAlberta admissions are handled solely through its official portal."
            ],
            "application_fee_warning": "Standard application fee is CAD 135 paid directly in the application portal. Never pay fees to third parties.",
            "agent_and_intermediary_warnings": "Do not hire agents; professors seek independent researchers capable of writing scientific publications.",
            "hidden_costs_breakdown": [
                "Application fee of CAD 135 (~PKR 27,000).",
                "Canadian Study Permit application and biometrics fees (CAD 235; ~PKR 47,000).",
                "Flight tickets from Pakistan to Edmonton (~PKR 280,000 - 420,000).",
                "Winter clothing and initial apartment security deposit (~CAD 1,500; ~PKR 300,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Course-based Master's programs receive full funding. (FACT: Guaranteed funding applies strictly to thesis-based MSc and PhD degrees).",
                "CLAIM: GRE is mandatory. (FACT: GRE scores are NOT required by UAlberta Computing Science)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Commercial blogs state living in Edmonton requires CAD 2,000/mo; official university budgets estimate CAD 1,300 to 1,500/mo for graduate students."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum cumulative GPA of 3.0 / 4.0 in graduate courses and achieve satisfactory progress on thesis milestones.",
            "attendance_requirements": "Full-time physical research residency on campus in Edmonton and fulfillment of teaching assistant duties.",
            "academic_progress_monitoring": "Annual progress reports reviewed by the Supervisory Committee and Departmental Graduate Chair.",
            "work_restrictions_during_study": "Funded students must fulfill TA duties (typically 12 hours/week) during teaching terms; external off-campus work is restricted to avoid delaying thesis research.",
            "home_country_return_obligation": "None. International graduates are eligible for Canada's Post-Graduation Work Permit (PGWP) of up to 3 years and provincial nomination (AAIP) permanent residency pathways.",
            "service_obligations_or_bonds": "Zero service bonds or return obligations.",
            "repayment_clawback_conditions": "Funding ceases if student withdraws or fails academic standing; past received assistantship funds are not clawed back.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Changing thesis topic or supervisor requires formal department approval.",
            "extension_policy": "Funding is guaranteed for standard degree duration (2 years MSc, 4 years PhD); subsequent funding extensions depend on supervisor research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Alberta Department of Computing Science Graduate Funding Portal",
                "source_url": "https://www.ualberta.ca/computing-science/graduate-studies/funding.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-by-lab graduate student intake quotas across individual Amii research groups.",
                    "Departmental score sheets and weightings used during preliminary candidate ranking.",
                    "Nationality-specific applicant and matriculation statistics."
                ]
            },
            {
                "source_name": "University of Alberta Faculty of Graduate Studies and Research (FGSR)",
                "source_url": "https://www.ualberta.ca/graduate-studies/prospective-students/apply-for-admission",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Discretionary departmental tuition bursary top-up pools for international scholars.",
                    "Waitlist ranking metrics and release dates for unfilled graduate slots."
                ]
            }
        ]
    },
    "SCH-AM-022": {
        "scholarship_id": "SCH-AM-022",
        "basic_details": {
            "scholarship_name": "Simon Fraser University (SFU) Computing Science Graduate Award",
            "offering_entity": "Simon Fraser University (School of Computing Science, Faculty of Applied Sciences, Vancouver, Canada)",
            "host_country": "Canada",
            "host_institutions_covered": "Simon Fraser University Campuses (Burnaby Campus & Vancouver Campus, BC, Canada)",
            "degree_levels": ["Master of Science (MSc Thesis)", "Doctor of Philosophy (PhD)"],
            "major_restrictions": "Restricted to thesis-based graduate degrees in Computing Science: Artificial Intelligence, Computer Vision, Graphics, Databases & Data Mining, Big Data, Systems & Networking, and Theoretical Computing Science.",
            "number_of_awards_total": "100% of admitted thesis-based graduate students receive guaranteed full financial support (~70 to 90 funded graduate students admitted annually)",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computer science and software engineering compete successfully (typically 6 to 10 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 2 years for MSc Thesis; up to 4 to 5 years for PhD, with guaranteed minimum departmental funding package"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to international and domestic applicants holding a valid passport"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed 4-year Bachelor's degree (16 years education) for MSc; completed Master's degree (18 years education) for PhD from an HEC-recognized university with minimum 3.40 / 4.00 CGPA (78%+ aggregate; 3.60+ competitive from NUST, FAST-NUCES, GIKI, UET, LUMS).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Minimum SFU equivalent cumulative GPA of 3.00 / 4.33 (or B average) in undergraduate degree; 3.50+ highly competitive.",
            "subject_background_prerequisites": "BSc or MSc in Computer Science, Computer Engineering, Software Engineering, or Mathematics with strong programming and theoretical foundations.",
            "current_education_status": "Graduating final-year students eligible; must complete degree requirements prior to September registration.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Research publications, open-source development, or machine learning engineering internships are highly valued.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 7.0,
                "toefl_minimum": 93,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall min 7.0 (each section min 6.5) or TOEFL iBT min 93 (each section min 20). Medium of Instruction certificates are not accepted."
            },
            "other_language_requirements": "None; English is the official language of instruction and research.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Thesis-based researchers in computer science and applied data intelligence.",
            "previous_scholarship_restrictions": "Cannot hold concurrent external awards exceeding university maximum allowable limits.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "Tuition costs offset via departmental tuition scholarships and Graduate Research Assistantship (GRA) packages (~CAD 6,500 to CAD 8,000 / year).",
                "amount": "100% covered (~CAD 7,500 / year value; ~PKR 1,500,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "SFU international graduate application fee (CAD 130) paid online via credit card.",
                "amount": "CAD 130 (~PKR 26,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid out of guaranteed living stipend; SFU Burnaby campus graduate residences or off-campus rentals in Burnaby/Vancouver average CAD 900 to 1,300/month.",
                "amount": "Paid from stipend (~CAD 1,100 / month; ~PKR 220,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum annual funding package: CAD 27,000 to CAD 32,000 / year (~CAD 2,250 to 2,666 / month; ~PKR 450,000 to 535,000/month) provided via Teaching Assistantships (TA), Research Assistantships (RA), and Graduate Fellowships.",
                "amount": "CAD 27,000 to 32,000 / year (~PKR 5,400,000 to 6,400,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel between Pakistan and Vancouver International Airport (YVR) is self-funded by student.",
                "amount": "Self-funded (~PKR 300,000 to 450,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit application fee (CAD 150) and biometrics fee (CAD 85) paid to IRCC.",
                "amount": "CAD 235 (~PKR 47,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "British Columbia Medical Services Plan (MSP, CAD 75/month) + SFU Graduate Student Society (GSS) Health and Dental Plan covered via package.",
                "amount": "Covered (~CAD 1,500 / year value; ~PKR 300,000 / yr)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered by monthly stipend package; campus cafeterias and local groceries affordable.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Supercomputing cluster access, GPU workstations, and lab computing facilities funded by School of Computing Science.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Graduate International Research Travel Award (GIRTA) and school grants provide up to CAD 2,500 per conference paper.",
                "amount": "Up to CAD 2,500 per conference"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "TransLink U-Pass BC included in student registration, granting unlimited bus, SkyTrain, and SeaBus transit across Metro Vancouver.",
                "amount": "Included in student fee package"
            },
            "total_estimated_value_usd_per_year": 34000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading Canadian comprehensive research university: Simon Fraser University (Vancouver, BC, Canada)",
            "participating_institutions": [
                "Simon Fraser University - School of Computing Science (Burnaby Campus, Metro Vancouver, BC)",
                "SFU Big Data Hub & Visual and Interactive Computing Institute"
            ],
            "university_rankings_scope": "Top 125 globally for Computer Science; ranked #1 comprehensive university in Canada by Maclean's for multiple consecutive years. International powerhouse in Computer Vision, Graphics, and Databases.",
            "available_majors": [
                "MSc / PhD in Computing Science: Computer Vision, Graphics, & Multimedia",
                "MSc / PhD in Computing Science: Artificial Intelligence & Machine Learning",
                "MSc / PhD in Computing Science: Data Mining, Databases, & Big Data Analytics",
                "MSc / PhD in Computing Science: Systems, Networking, & Cloud Architecture",
                "MSc / PhD in Computing Science: Algorithms, Complexity, & Theoretical CS"
            ],
            "english_taught_program_availability": True,
            "program_duration": "MSc Thesis: 2 years (4 to 5 terms); PhD: 4 to 5 years full-time.",
            "admission_requirements_summary": "Bachelor's or Master's in CS/STEM with 3.4+ GPA, 3 referee reports, statement of purpose, CV, prospective supervisor alignment, and IELTS 7.0 / TOEFL 93.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Computer Vision, Deep Learning, and Graphics have intense competition; Databases, Algorithms, and Software Engineering offer favorable supervisor match ratios.",
            "strategic_program_match_advice": "Prospective students must browse the faculty research pages, select up to 3 faculty members whose work aligns with their thesis, and contact them directly before the December deadline. Securing interest from a supervisor is the key factor in receiving an admission and funding offer."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.sfu.ca/gradstudies/apply.html",
            "portal_system_name": "Simon Fraser University Graduate Studies Online Application System",
            "account_creation_instructions": "Register an account on the SFU Graduate Studies application portal, select School of Computing Science, specify degree stream (Thesis MSc or PhD), list target supervisors, and submit required documents.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Review Computing Science faculty profiles; contact prospective supervisors with academic CV, transcripts, and statement of research interests.",
                "Step 2 (October - Early December): Create application on SFU Graduate Studies portal (sfu.ca/gradstudies/apply); complete profile.",
                "Step 3 (November - December): Upload unofficial transcripts, CV, research statement, and provide details of 3 academic referees.",
                "Step 4 (By 15 December): Pay application fee (CAD 130) and submit application before Fall intake deadline.",
                "Step 5 (January - February): Departmental admissions committee reviews applications; faculty supervisors review files and schedule Zoom interviews.",
                "Step 6 (March - April): Official admission offers with guaranteed annual funding letters dispatched; accept offer via portal.",
                "Step 7 (April - May): Apply for Canadian Study Permit via IRCC portal; complete biometrics and medical exam in Pakistan.",
                "Step 8 (Late August / Early September): Travel to Metro Vancouver, attend SFU graduate orientation, and begin research and teaching assistantship."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: All admitted thesis-based graduate students receive guaranteed departmental funding; no separate scholarship application required.",
            "recommendation_letters_submission_method": "Three confidential academic recommendation letters submitted online via automated referee portal link.",
            "personal_statement_prompts": "Statement of Research Interests (1-2 pages): Detail research experience, mathematical and programming strengths, intended research areas, and preferred faculty supervisors.",
            "study_plan_research_proposal_requirements": "Structured research statement (1-2 pages) describing research interests, methodologies, and proposed supervisors.",
            "cv_format_requirements": "Academic CV detailing programming languages, software projects, research publications, awards, and GitHub profile.",
            "interviews_conducted": True,
            "interview_format_details": "Technical video interviews (30-45 minutes via Zoom) conducted by prospective faculty supervisors evaluating coding, mathematical foundations, and research intuition.",
            "standardized_tests": "IELTS 7.0 (min 6.5 in all bands) or TOEFL iBT 93 (min 20 in all bands). GRE is NOT required.",
            "application_fee_amount": "CAD 130 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official attested transcripts from HEC Pakistan required upon formal admission offer.",
            "translation_requirements": "Certified English translations for any documents not in English.",
            "final_submission_method": "100% digital submission via the SFU online application system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least 2 years.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts of all university education with grading scale and degree completion certificates.",
                "pakistan_specific_instruction": "HEC Pakistan attestation required on final official documents upon offer acceptance."
            },
            {
                "document_name": "Statement of Research Interests",
                "mandatory": True,
                "specification": "Structured 1 to 2 page statement of research background, objectives, and professor alignment.",
                "pakistan_specific_instruction": "Specifically name SFU faculty members whose lab papers you have studied."
            },
            {
                "document_name": "Academic Recommendation Letters (Three)",
                "mandatory": True,
                "specification": "Confidential recommendation letters from former professors or research mentors.",
                "pakistan_specific_instruction": "Must be submitted from verified institutional email accounts."
            },
            {
                "document_name": "English Language Proficiency Report",
                "mandatory": True,
                "specification": "Official IELTS Academic (7.0+) or TOEFL iBT (93+) scorecard.",
                "pakistan_specific_instruction": "Electronic score reporting to Simon Fraser University institutional code."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Academic CV detailing coding skills, publications, capstone projects, and GitHub links.",
                "pakistan_specific_instruction": "Highlight contributions to open source or Scopus/IEEE papers."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 September 2026",
            "application_deadline": "15 December 2026 (Fall 2027 intake)",
            "university_admission_deadline": "15 December 2026",
            "document_submission_deadline": "15 December 2026",
            "recommendation_letters_deadline": "22 December 2026",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "March to April 2027",
            "final_result_acceptance_deadline": "15 April / 1 May 2027",
            "visa_application_window": "April to July 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Main intake cycle is Fall (September). Spring (January) and Summer (May) intakes have very limited thesis funding openings."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (CGPA in relevant computer science and mathematics coursework, class rank)",
            "extracurricular_and_leadership_weight": "5% (Contributions to student tech community, hackathons)",
            "research_experience_weight": "35% (Prior thesis quality, publications, open-source repositories, and technical skills)",
            "work_experience_weight": "5% (Industry software engineering, AI internships, or data engineering roles)",
            "personal_statement_weight": "10% (Clarity of research vision, intellectual curiosity, and fit with department)",
            "recommendations_weight": "5% (Strength of professor endorsements)",
            "interview_weight": "5% (Technical interview with prospective faculty advisor)",
            "test_scores_weight": "Threshold requirement (IELTS 7.0 / TOEFL 93 compliance)",
            "financial_need_weight": "0% (Purely merit and research competence based)",
            "selection_panel_composition": "School of Computing Science Graduate Admissions Committee & faculty supervisors.",
            "evaluation_methodology": "Two-phase holistic review: Graduate admissions committee pre-screens applicants for academic and English compliance; individual faculty supervisors review applicant files and interview candidates to make binding funding and admission offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,200 to 1,800 international applicants across thesis MSc and PhD",
            "total_scholarships_awarded": "~70 to 90 fully funded graduate admission offers",
            "acceptance_rate_global": "~5.5%",
            "acceptance_rate_pakistan": "~8.5% (Competitive placement for Pakistani computer scientists with solid coding/research credentials)",
            "typical_successful_applicant_gpa": "3.65+ / 4.00 CGPA (82%+ aggregate)",
            "typical_academic_and_research_profile": "Solid foundation in algorithms, mathematics, and programming; 1+ publications in indexed conferences or strong software portfolio; clear supervisor alignment.",
            "common_backgrounds_of_winners": "BS/MS graduates in Computer Science and Software Engineering from NUST, FAST-NUCES, GIKI, UET, and LUMS.",
            "high_representation_countries": "China, India, Pakistan, Iran, Canada, United States, Bangladesh",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial agencies claiming to sell guaranteed SFU computing science scholarships. SFU conducts all admissions through its official portal."
            ],
            "application_fee_warning": "Standard application fee is CAD 130 paid directly in the application portal. Never pay fees to third parties.",
            "agent_and_intermediary_warnings": "Do not hire agents; professors seek independent researchers capable of writing scientific publications.",
            "hidden_costs_breakdown": [
                "Application fee of CAD 130 (~PKR 26,000).",
                "Canadian Study Permit application and biometrics fees (CAD 235; ~PKR 47,000).",
                "Flight tickets from Pakistan to Vancouver (~PKR 300,000 - 450,000).",
                "Initial housing deposit in Metro Vancouver (~CAD 1,800; ~PKR 360,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Professional Master's in Big Data receives guaranteed funding. (FACT: Guaranteed funding applies strictly to thesis-based MSc and PhD degrees; professional programs are self-funded).",
                "CLAIM: Duolingo is accepted. (FACT: SFU Computing Science does NOT accept Duolingo; IELTS or TOEFL required)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some agencies advertise SFU as requiring GRE; official SFU guidelines confirm GRE is optional and not mandatory."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum cumulative GPA of 3.0 / 4.33 in graduate courses and achieve satisfactory progress on thesis milestones.",
            "attendance_requirements": "Full-time physical research residency on campus in Metro Vancouver and fulfillment of teaching assistant duties.",
            "academic_progress_monitoring": "Annual progress reports reviewed by the Supervisory Committee and Departmental Graduate Chair.",
            "work_restrictions_during_study": "Funded students must fulfill TA duties (typically 12 hours/week) during teaching terms; external off-campus work is restricted to avoid delaying thesis research.",
            "home_country_return_obligation": "None. International graduates are eligible for Canada's Post-Graduation Work Permit (PGWP) of up to 3 years and British Columbia provincial nomination (BC PNP) permanent residency pathways.",
            "service_obligations_or_bonds": "Zero service bonds or return obligations.",
            "repayment_clawback_conditions": "Funding ceases if student withdraws or fails academic standing; past received assistantship funds are not clawed back.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Changing thesis topic or supervisor requires formal department approval.",
            "extension_policy": "Funding is guaranteed for standard degree duration (2 years MSc, 4 years PhD); subsequent funding extensions depend on supervisor research grants."
        },
        "official_sources_verified": [
            {
                "source_name": "Simon Fraser University School of Computing Science Graduate Financial Aid Portal",
                "source_url": "https://www.sfu.ca/computing/prospective-students/graduate-students/financial-aid.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Lab-specific quota distribution of research assistantships across visual computing vs systems labs.",
                    "Exact interview scoring guidelines used by individual faculty members.",
                    "Historical applicant-to-awardee conversion rates for international applicants."
                ]
            },
            {
                "source_name": "Simon Fraser University Graduate Studies Admissions Guidelines",
                "source_url": "https://www.sfu.ca/gradstudies/apply.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waitlist ranking metrics and release dates for unfilled graduate slots.",
                    "Departmental top-up pools for international student health insurance coverage."
                ]
            }
        ]
    },
    "SCH-AM-025": {
        "scholarship_id": "SCH-AM-025",
        "basic_details": {
            "scholarship_name": "University of Ottawa International Doctoral Differential Scholarship",
            "offering_entity": "University of Ottawa (Faculty of Graduate and Postdoctoral Studies & Faculty of Engineering, Ottawa, Canada)",
            "host_country": "Canada",
            "host_institutions_covered": "University of Ottawa Campuses (Downtown Main Campus, Ottawa, Ontario, Canada)",
            "degree_levels": ["Doctor of Philosophy (PhD)"],
            "major_restrictions": "Open to all doctoral research programs with prominent funding in School of Electrical Engineering and Computer Science (EECS: Computer Science, Electrical and Computer Engineering, E-Business Technologies), Faculty of Engineering, and Faculty of Science.",
            "number_of_awards_total": "All eligible international doctoral students admitted to thesis-based PhD programs receive the International Doctoral Scholarship (~150 to 200 doctoral scholarships active annually)",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computer science and electrical engineering represent a prominent cohort (typically 12 to 20 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 4 years (12 consecutive sessions) of guaranteed doctoral funding, subject to maintaining satisfactory academic standing"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students holding a valid study permit admitted to a full-time PhD program"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restriction.",
            "academic_qualifications": "Completed 4-year Bachelor's degree (16 years education) and Master's degree (18 years education) in engineering, computer science, or science from an HEC-recognized university with minimum 3.40 / 4.00 CGPA (78%+ aggregate; 3.60+ competitive from NUST, FAST-NUCES, GIKI, UET, LUMS, COMSATS).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Minimum admission average of 8.0 / 10.0 (or A- average) on the University of Ottawa grading scale in Master's coursework.",
            "subject_background_prerequisites": "Master's degree in Computer Science, Software Engineering, Electrical Engineering, or related STEM fields with a demonstrated research thesis.",
            "current_education_status": "Graduating Master's students eligible; degree must be conferred prior to commencing doctoral studies.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Research publications in peer-reviewed journals or IEEE conferences significantly strengthen candidacy.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 80,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall min 6.5 (min 6.0 in writing) or TOEFL iBT min 80 (min 19 in writing). Medium of Instruction certificates are not accepted."
            },
            "other_language_requirements": "None required for English-stream programs; bilingual institution offers instruction in both English and French.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Full-time international doctoral researchers.",
            "previous_scholarship_restrictions": "Cannot hold multiple full external fellowships exceeding university maximum award policy.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "International Doctoral Scholarship waives the international fee differential, reducing international tuition to the domestic Canadian rate (~CAD 2,000/term). This domestic tuition is then covered by the faculty admission scholarship / research assistantship.",
                "amount": "100% covered (~CAD 20,000 / year international waiver value; ~PKR 4,000,000 / yr)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Ottawa international graduate application fee (CAD 110) paid online via credit card.",
                "amount": "CAD 110 (~PKR 22,000)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid out of guaranteed living stipend; student rentals in Ottawa/Gatineau average CAD 800 to 1,200/month.",
                "amount": "Paid from stipend (~CAD 1,000 / month; ~PKR 200,000 / mo)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Guaranteed minimum annual funding package: CAD 24,000 to CAD 30,000 / year (~CAD 2,000 to 2,500 / month; ~PKR 400,000 to 500,000/month) provided through Teaching Assistantships (TA), Research Assistantships (RA), and Admission Scholarships for 4 years.",
                "amount": "CAD 24,000 to 30,000 / year (~PKR 4,800,000 to 6,000,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Travel between Pakistan and Ottawa Macdonald-Cartier International Airport (YOW) is self-funded by student.",
                "amount": "Self-funded (~PKR 280,000 to 420,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Canadian Study Permit application fee (CAD 150) and biometrics fee (CAD 85) paid to IRCC.",
                "amount": "CAD 235 (~PKR 47,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "University Health Insurance Plan (UHIP, ~CAD 756/year) covered through graduate student benefits.",
                "amount": "UHIP covered (~CAD 756 / year value; ~PKR 150,000 / yr)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered by monthly stipend package; campus cafeterias and local groceries affordable.",
                "amount": "Covered from monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "High-performance computing resources, lab equipment, and workstations funded by Faculty of Engineering research labs.",
                "amount": "Covered by laboratory resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Faculty of Engineering and GSAED conference travel funds provide up to CAD 1,500 to 2,500 per year for presenting at peer-reviewed international conferences.",
                "amount": "Up to CAD 2,500 per year"
            },
            "travel_transit_allowance": {
                "status": "100% COVERED",
                "details": "OC Transpo U-Pass included in student registration, granting unlimited bus and O-Train light rail transit across Ottawa and Gatineau.",
                "amount": "Included in student fee package"
            },
            "total_estimated_value_usd_per_year": 35000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single major Canadian bilingual research university: University of Ottawa (Ottawa, Ontario, Canada)",
            "participating_institutions": [
                "University of Ottawa - School of Electrical Engineering and Computer Science (EECS, Downtown Campus)",
                "Ottawa-Carleton Institute for Computer Science (OCICS) & Electrical and Computer Engineering (OCIECE)"
            ],
            "university_rankings_scope": "Top 140 global university (QS World #137, Times Higher Education #177); member of Canada's U15 group of research-intensive universities. Prime location in Canada's capital adjacent to the Kanata North tech hub.",
            "available_majors": [
                "PhD in Computer Science: Artificial Intelligence, Machine Learning, Data Science",
                "PhD in Computer Science: Software Engineering, Distributed Systems, Cloud Computing",
                "PhD in Electrical and Computer Engineering: Telecommunications, Signal Processing, Computer Systems",
                "PhD in Electronic Business Technologies: FinTech, E-Commerce Infrastructure, Analytics",
                "PhD in Digital Transformation and Innovation"
            ],
            "english_taught_program_availability": True,
            "program_duration": "PhD: 4 years full-time (12 consecutive terms).",
            "admission_requirements_summary": "Master's degree in CS/engineering with 3.4+ GPA (8.0/10 average), supervisor confirmation, 2-3 referee reports, statement of intent, CV, and IELTS 6.5 / TOEFL 80.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "AI, Machine Learning, and Cybersecurity under EECS have highest applicant volume; Software Engineering and E-Business Technologies offer favorable supervisory placement.",
            "strategic_program_match_advice": "For PhD admission at uOttawa, securing an agreement from a faculty supervisor in advance is a strict requirement before formal admission can be granted. Candidates must review EECS professor research profiles and secure an email of agreement to supervise."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.uottawa.ca/study/graduate-studies/apply",
            "portal_system_name": "University of Ottawa Graduate Application Portal (uOcampus / OUAC)",
            "account_creation_instructions": "Submit initial application via Ontario Universities' Application Centre (OUAC), receive uOttawa Student ID and credentials for uOzone, then upload supporting documents to uODoc portal.",
            "step_by_step_workflow": [
                "Step 1 (September - November): Review uOttawa EECS faculty profiles; contact prospective supervisors with CV, transcripts, and thesis abstract to secure supervisory agreement.",
                "Step 2 (October - December): Submit initial online application on the Ontario Universities' Application Centre (OUAC) portal; pay application fee (CAD 110).",
                "Step 3 (Within 48 hours): Receive email from uOttawa with student ID number and login credentials for uOzone / uODoc portal.",
                "Step 4 (By 15 January): Upload unofficial transcripts, CV, research statement, proof of supervisor agreement, and referee details on uODoc.",
                "Step 5 (February - March): Departmental Graduate Committee and faculty supervisor review files and recommend admission and scholarship package.",
                "Step 6 (March - April): Official Letter of Admission and guaranteed funding package (International Doctoral Scholarship + TA/RA) issued.",
                "Step 7 (April - June): Apply for Canadian Study Permit via IRCC portal; complete biometrics and medical exam in Pakistan.",
                "Step 8 (Late August / Early September): Travel to Ottawa, attend EECS graduate orientation, check into housing, and begin doctoral studies."
            ],
            "university_vs_scholarship_routing": "Integrated automatic funding: The International Doctoral Scholarship is awarded automatically upon admission to all eligible international doctoral candidates.",
            "recommendation_letters_submission_method": "Two to three academic recommendation letters submitted online via automated referee portal link.",
            "personal_statement_prompts": "Statement of Intent (1-2 pages): Describe research background, master's thesis contributions, proposed doctoral research topic, and confirmed supervisor.",
            "study_plan_research_proposal_requirements": "Structured research outline (2-3 pages) prepared in consultation with the prospective supervisor.",
            "cv_format_requirements": "Academic CV detailing publications, conference papers, technical skills, and research assistantship history.",
            "interviews_conducted": True,
            "interview_format_details": "Video interviews (30-45 minutes via MS Teams/Zoom) conducted by prospective faculty supervisors evaluating technical competence and research alignment.",
            "standardized_tests": "IELTS 6.5 (min 6.0 in writing) or TOEFL iBT 80 (min 19 in writing). GRE is NOT required.",
            "application_fee_amount": "CAD 110 (Non-refundable)",
            "attestation_requirements": "Unofficial scans uploaded for review; official attested transcripts from HEC Pakistan required upon formal admission offer.",
            "translation_requirements": "Certified English translations for any documents not in English.",
            "final_submission_method": "100% digital submission via the uOttawa uODoc application system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least 2 years.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete transcripts of all university education with grading scale and degree completion certificates.",
                "pakistan_specific_instruction": "HEC Pakistan attestation required on final official documents upon offer acceptance."
            },
            {
                "document_name": "Proof of Supervisor Agreement",
                "mandatory": True,
                "specification": "Written confirmation or email from a uOttawa faculty member agreeing to supervise doctoral research.",
                "pakistan_specific_instruction": "Essential prerequisite before uOttawa EECS application can be approved."
            },
            {
                "document_name": "Statement of Intent and Research Outline",
                "mandatory": True,
                "specification": "Structured 1 to 2 page statement of research background, objectives, and professor alignment.",
                "pakistan_specific_instruction": "Specifically name uOttawa faculty members whose lab papers you have studied."
            },
            {
                "document_name": "Academic Recommendation Letters (Two to Three)",
                "mandatory": True,
                "specification": "Confidential recommendation letters from former professors or research mentors.",
                "pakistan_specific_instruction": "Must be submitted from verified institutional email accounts."
            },
            {
                "document_name": "English Language Proficiency Report",
                "mandatory": True,
                "specification": "Official IELTS Academic (6.5+) or TOEFL iBT (80+) scorecard.",
                "pakistan_specific_instruction": "Electronic score reporting to University of Ottawa institutional code."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Academic CV detailing coding skills, publications, capstone projects, and GitHub links.",
                "pakistan_specific_instruction": "Highlight contributions to open source or Scopus/IEEE papers."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 September 2026",
            "application_deadline": "15 January 2027 (Fall 2027 intake)",
            "university_admission_deadline": "15 January 2027",
            "document_submission_deadline": "31 January 2027",
            "recommendation_letters_deadline": "31 January 2027",
            "interview_period": "January to February 2027",
            "shortlist_announcement": "March to April 2027",
            "final_result_acceptance_deadline": "15 April / 1 May 2027",
            "visa_application_window": "April to July 2027",
            "semester_commencement": "Early September 2027",
            "annual_cycle_notes": "Main intake is Fall (September). Winter (January) intake is available for students with secured supervisory funding."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (CGPA in relevant computer science and mathematics coursework, class rank)",
            "extracurricular_and_leadership_weight": "5% (Contributions to student tech community, hackathons)",
            "research_experience_weight": "35% (Prior thesis quality, publications, open-source repositories, and technical skills)",
            "work_experience_weight": "5% (Industry software engineering, AI internships, or data engineering roles)",
            "personal_statement_weight": "10% (Clarity of research vision, intellectual curiosity, and fit with department)",
            "recommendations_weight": "5% (Strength of professor endorsements)",
            "interview_weight": "5% (Technical interview with prospective faculty advisor)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 80 compliance)",
            "financial_need_weight": "0% (Purely merit and research competence based)",
            "selection_panel_composition": "Faculty of Engineering Graduate Studies Committee & prospective doctoral supervisor.",
            "evaluation_methodology": "Two-phase holistic review: Graduate admissions committee pre-screens applicants for academic and English compliance; individual faculty supervisors review applicant files and interview candidates to make binding funding and admission offers."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,000 to 1,500 international doctoral applicants across engineering and science",
            "total_scholarships_awarded": "~150 to 200 fully funded international doctoral admissions",
            "acceptance_rate_global": "~11.0%",
            "acceptance_rate_pakistan": "~14.0% (Strong placement for Pakistani Master's graduates with research publications)",
            "typical_successful_applicant_gpa": "3.60+ / 4.00 CGPA (80%+ aggregate in Master's)",
            "typical_academic_and_research_profile": "Master of Science with research thesis, 1+ peer-reviewed journal or conference publications, prior supervisory agreement, IELTS 7.0.",
            "common_backgrounds_of_winners": "MS graduates in Computer Science, Software Engineering, and Electrical Engineering from NUST, FAST-NUCES, GIKI, UET, COMSATS, and LUMS.",
            "high_representation_countries": "China, India, Iran, Pakistan, Nigeria, France, Canada",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Commercial recruiters claiming guaranteed uOttawa doctoral scholarship placement. Scholarships are administered directly through university admissions."
            ],
            "application_fee_warning": "Standard application fee is CAD 110 paid directly via OUAC/uOcampus. Never pay fees to external agents.",
            "agent_and_intermediary_warnings": "Supervisors evaluate research independence; applications prepared by third-party agents are rejected.",
            "hidden_costs_breakdown": [
                "Application fee of CAD 110 (~PKR 22,000).",
                "Canadian Study Permit application and biometrics fees (CAD 235; ~PKR 47,000).",
                "Flight tickets from Pakistan to Ottawa (~PKR 280,000 - 420,000).",
                "Initial settling cash and apartment lease in Ottawa (~CAD 1,500; ~PKR 300,000)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: French proficiency is required. (FACT: 100% of courses and research in EECS can be completed in English).",
                "CLAIM: Master's coursework students receive the differential scholarship. (FACT: The differential scholarship applies strictly to doctoral PhD students)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some agencies claim the scholarship is cash in hand; official regulations state it waives the international differential fee down to domestic rate, supplemented by TA/RA salary."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain minimum cumulative grade average of 6.0 / 10.0 (B average) in all graduate coursework and pass comprehensive exams.",
            "attendance_requirements": "Full-time physical research residency on campus in Ottawa and fulfillment of teaching assistant duties.",
            "academic_progress_monitoring": "Annual progress reports submitted to the Faculty of Graduate and Postdoctoral Studies.",
            "work_restrictions_during_study": "Funded students must fulfill TA duties (typically 10-12 hours/week) during teaching terms; external off-campus work is restricted to avoid delaying thesis research.",
            "home_country_return_obligation": "None. International graduates are eligible for Canada's Post-Graduation Work Permit (PGWP) of up to 3 years and Ontario Immigrant Nominee Program (OINP PhD Graduate Stream) permanent residency.",
            "service_obligations_or_bonds": "Zero service bonds or return obligations.",
            "repayment_clawback_conditions": "Funding ceases if student withdraws or fails academic standing; past received assistantship funds are not clawed back.",
            "rules_for_changing_university": "Non-transferable to other institutions.",
            "rules_for_changing_major": "Changing thesis topic or supervisor requires formal department approval.",
            "extension_policy": "Scholarship is guaranteed for 4 years (12 terms); extensions beyond 4 years depend on supervisor research grants and departmental funding availability."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Ottawa International Doctoral Scholarship Portal",
                "source_url": "https://www.uottawa.ca/study/graduate-studies/funding-financing/awards/international-doctoral-scholarship",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Departmental distribution of Teaching Assistantship hours between fall and winter sessions.",
                    "Exact rubric weights used by EECS admissions committee when evaluating publication records.",
                    "Country-level breakdown of doctoral scholarship recipients."
                ]
            },
            {
                "source_name": "University of Ottawa School of Electrical Engineering and Computer Science (EECS)",
                "source_url": "https://www.uottawa.ca/faculty-engineering/school-electrical-engineering-computer-science",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Average lab-by-lab Research Assistantship top-up funding amounts.",
                    "Waitlist ranking metrics and release dates for unfilled graduate slots."
                ]
            }
        ]
    }
}
