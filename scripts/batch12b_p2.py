# scripts/batch12b_p2.py
# 29. University of Newcastle Research Scholarship UNIPRS (SCH-OC-014)
# 30. University of Auckland International Excellence (SCH-OC-018)

DATA_P2 = {
    "SCH-OC-014": {
        "scholarship_id": "SCH-OC-014",
        "basic_details": {
            "scholarship_name": "University of Newcastle International Postgraduate Research Scholarship (UNIPRS) & RTP",
            "offering_entity": "University of Newcastle (UON, Australia) & Australian Commonwealth Government (Department of Education)",
            "host_country": "Australia",
            "host_institutions_covered": "University of Newcastle Campuses: Callaghan Main Campus & Newcastle City Precinct (Newcastle, NSW, Australia)",
            "degree_levels": ["Doctor of Philosophy (PhD)", "Master of Philosophy (MPhil Research)"],
            "major_restrictions": "Open to all research fields across College of Engineering, Science and Environment (Computer Science, Data Science, Software Engineering, Energy Science, Biomedical Engineering, Medical Physics, Environmental Science) and College of Health, Medicine and Wellbeing.",
            "number_of_awards_total": "Approximately 80 to 120 competitive international research scholarships awarded annually across university research centers",
            "number_of_awards_pakistan": "Open international competition; Pakistani graduates in computing, software, and renewable energy compete effectively (typically 5 to 10 awardees/yr)",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 3.5 years for PhD candidates; up to 2 years for Master of Philosophy candidates, with potential 6-month PhD extension for justified research delays"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International applicants who do not hold Australian or New Zealand citizenship or permanent residency"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restrictions.",
            "academic_qualifications": "Completed 4-year Bachelor's degree with First Class Honours (H1 equivalent, 78%+ or 3.40+ / 4.00 CGPA) or completed Master of Science by Research / MS with substantial research thesis from an HEC-recognized institution in Pakistan (e.g. NUST, FAST-NUCES, GIKI, UET, LUMS, COMSATS, PIEAS, University of the Punjab).",
            "minimum_gpa_percentage": 78.0,
            "minimum_gpa_scale": 3.4,
            "grading_conversion_notes": "Evaluated against Australian Honours Class 1 (H1) standard (minimum 78% / 3.4 CGPA with strong thesis grade).",
            "subject_background_prerequisites": "BSc / MS in Computer Science, Data Science, Software Engineering, Electrical Engineering, Physics, or related STEM fields.",
            "current_education_status": "Must have completed degree or be in final semester of research Master's.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not mandatory. Industry software engineering or laboratory research experience can demonstrate research capability.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 85,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall min 6.5 (all sub-tests 6.0+); TOEFL iBT min 85 (sub-tests 19+); or PTE Academic min 58 (50+ in skills). Medium of Instruction certificates are not accepted."
            },
            "other_language_requirements": "None; all coursework, seminars, and doctoral dissertations are in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "Higher Degree by Research (HDR) international candidates demonstrating superior academic and research promise.",
            "previous_scholarship_restrictions": "Cannot hold another major Australian Commonwealth scholarship concurrently.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "100% COVERED",
                "details": "100% full international tuition fee waiver for up to 3.5 years (AUD 38,000 to 44,000 / year waived completely).",
                "amount": "100% covered (~AUD 40,000 / year value; ~PKR 7,400,000 / year)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "Application for postgraduate research admission with supervisory endorsement is free of charge.",
                "amount": "AUD 0 (Free application)"
            },
            "accommodation": {
                "status": "PAID VIA STIPEND",
                "details": "Paid from living stipend; Newcastle offers significantly lower living and rental costs than Sydney or Melbourne (student rentals ~AUD 200 to 280/week).",
                "amount": "Paid from stipend (~AUD 900 to 1,200 / month)"
            },
            "monthly_stipend": {
                "status": "100% COVERED",
                "details": "Tax-free living allowance: AUD 32,000 to 35,000 per annum index-linked (~AUD 2,666 to 2,916 / month; ~PKR 495,000 to 540,000/month). Top-up scholarships from research groups often supplement this base.",
                "amount": "AUD 32,000 to 35,000 / year tax-free (~PKR 5,920,000 to 6,475,000 / year)"
            },
            "airfare": {
                "status": "COVERED",
                "details": "Relocation allowance of up to AUD 1,500 provided to assist international scholars traveling from overseas to Newcastle.",
                "amount": "Up to AUD 1,500 relocation subsidy (~PKR 277,500)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Australian Subclass 500 Student Visa application fee (AUD 1,600) paid directly to Department of Home Affairs.",
                "amount": "AUD 1,600 (~PKR 296,000)"
            },
            "health_insurance": {
                "status": "100% COVERED",
                "details": "Standard Overseas Student Health Cover (OSHC) single policy funded directly by University of Newcastle for candidate visa tenure.",
                "amount": "AUD 2,400 to 3,000 total value (~PKR 445,000 to 555,000)"
            },
            "food_allowance": {
                "status": "INCLUDED_IN_STIPEND",
                "details": "Living expenses covered through the fortnightly stipend; regional NSW cost of living is very affordable.",
                "amount": "Included in monthly stipend"
            },
            "books_and_materials_allowance": {
                "status": "PROVIDED_BY_FACULTY",
                "details": "Specialist laboratory equipment, supercomputing time, and lab consumables funded by university research groups.",
                "amount": "Covered by faculty and research center"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "College Research Higher Degree travel funds provide up to AUD 2,500 to 4,000 for attending international academic conferences.",
                "amount": "Up to AUD 4,000 per conference"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Newcastle bus, light rail, and train transit are self-funded (concession fares available for international students).",
                "amount": "Self-funded (~AUD 60 / month; ~PKR 11,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 48000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single comprehensive research-intensive university: University of Newcastle (Newcastle, NSW, Australia)",
            "participating_institutions": [
                "University of Newcastle - Callaghan Campus (Newcastle, NSW)",
                "Newcastle Institute for Energy and Resources (NIER)",
                "Hunter Medical Research Institute (HMRI)"
            ],
            "university_rankings_scope": "Ranked top 175 globally in QS World University Rankings 2024/2025 (QS #173); top 30 in the world for impact. World leader in automation, energy systems, and medical physics.",
            "available_majors": [
                "School of Information and Physical Sciences: Computer Science, Data Science, Software Engineering, Medical Physics",
                "School of Engineering: Electrical and Electronic Engineering, Mechatronics, Mechanical, Civil Engineering",
                "Newcastle Institute for Energy and Resources: Clean Energy, Materials Science, Chemical Engineering",
                "School of Environmental and Life Sciences: Biological Sciences, Biotechnology, Environmental Science"
            ],
            "english_taught_program_availability": True,
            "program_duration": "PhD: 3.5 years full-time; Master of Philosophy: 2 years full-time.",
            "admission_requirements_summary": "Bachelor's H1 or Master by Research with 3.4+ GPA, agreement from prospective supervisor, 3-page research proposal, 2 referee reports, and IELTS 6.5.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Computer Science and Data Science receive substantial application volume; Energy Science and Medical Physics have excellent supervisory capacity and high success rates.",
            "strategic_program_match_advice": "Prospective candidates must review faculty profiles on the UON Research Supervisor Directory, contact potential supervisors with their CV, thesis abstract, and research proposal, and obtain formal agreement before applying. Pre-agreed supervisor support is vital for ranking."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.newcastle.edu.au/study/apply",
            "portal_system_name": "University of Newcastle Online HDR Admissions System",
            "account_creation_instructions": "Contact prospective supervisor, obtain formal agreement to supervise, then create account on the UON online admissions portal and select 'Apply for Scholarship'.",
            "step_by_step_workflow": [
                "Step 1 (April - June): Search University of Newcastle supervisor directory; email potential supervisors with CV, academic transcripts, and research proposal.",
                "Step 2 (June - July): Conduct video interview with prospective supervisor; secure their agreement to supervise your research project.",
                "Step 3 (July - August): Prepare full documentation: refined research proposal (3 pages), 2 academic referee reports, IELTS test report, and attested transcripts.",
                "Step 4 (By 30 September): Submit formal online application via UON portal, selecting 'UNIPRS / RTP International Scholarship'.",
                "Step 5 (October - November): College Research Committee evaluates applications against H1 criteria and research output.",
                "Step 6 (December): Dean of Graduate Studies releases scholarship outcomes and issues unconditional offers and Confirmation of Enrolment (CoE).",
                "Step 7 (December - January): Apply for Australian Subclass 500 Student Visa via ImmiAccount; complete biometrics and medical exam in Pakistan.",
                "Step 8 (February - March): Travel to Newcastle, attend HDR orientation, and commence research candidature."
            ],
            "university_vs_scholarship_routing": "Integrated application: Application for admission automatically includes assessment for UNIPRS and RTP scholarship packages.",
            "recommendation_letters_submission_method": "Two academic referee reports completed on UON HDR Referee Report Template and submitted directly by referees.",
            "personal_statement_prompts": "Statement of Research Intent: Detail academic background, research interests, career vision, and alignment with UON strategic research themes.",
            "study_plan_research_proposal_requirements": "Structured research proposal (2-3 pages) covering title, background, methodology, objectives, literature review, and required laboratory resources.",
            "cv_format_requirements": "Academic CV detailing peer-reviewed publications, research projects, technical skills, and academic awards.",
            "interviews_conducted": True,
            "interview_format_details": "Video interview conducted by prospective supervisor and co-supervisors evaluating research methodology and communication skills.",
            "standardized_tests": "IELTS 6.5 (all bands 6.0+) or TOEFL iBT 85 (19 in all bands) or PTE 58. GRE is not required.",
            "application_fee_amount": "AUD 0 (Free application for HDR research programs)",
            "attestation_requirements": "HEC Pakistan attestation required on degrees and transcripts, accompanied by verified copies.",
            "translation_requirements": "Official certified English translations required for any non-English official records.",
            "final_submission_method": "100% digital submission via the University of Newcastle online admissions system."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least two years.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Certified transcripts showing all semesters, grades, grading scale, and degree completion certificates.",
                "pakistan_specific_instruction": "Higher Education Commission (HEC) Pakistan attested documents."
            },
            {
                "document_name": "UON Supervisor Support Confirmation",
                "mandatory": True,
                "specification": "Written confirmation or email from a Newcastle faculty member agreeing to supervise.",
                "pakistan_specific_instruction": "Essential prerequisite before formal portal lodgement."
            },
            {
                "document_name": "Research Proposal (2-3 pages)",
                "mandatory": True,
                "specification": "Structured proposal developed in consultation with prospective Newcastle supervisor.",
                "pakistan_specific_instruction": "Highlight practical methodologies and laboratory facilities required."
            },
            {
                "document_name": "Academic Referee Reports (Two)",
                "mandatory": True,
                "specification": "Completed on official UON HDR Referee Report forms by former academic supervisors.",
                "pakistan_specific_instruction": "Must be submitted directly by referees from official university email accounts."
            },
            {
                "document_name": "English Language Proficiency Test Scorecard",
                "mandatory": True,
                "specification": "Official IELTS Academic, TOEFL iBT, or PTE Academic scorecard dated within 2 years.",
                "pakistan_specific_instruction": "Direct electronic score dispatch through testing agency portal."
            },
            {
                "document_name": "Curriculum Vitae and Publications Evidence",
                "mandatory": True,
                "specification": "Detailed CV listing full citations of peer-reviewed papers with DOIs.",
                "pakistan_specific_instruction": "Highlight papers published in Scopus/WoS indexed journals or conferences."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "1 June 2027",
            "application_deadline": "30 September 2027 (for Semester 1 / Feb 2028 intake)",
            "university_admission_deadline": "30 September 2027",
            "document_submission_deadline": "30 September 2027",
            "recommendation_letters_deadline": "7 October 2027",
            "interview_period": "July to August 2027",
            "shortlist_announcement": "Mid-December 2027",
            "final_result_acceptance_deadline": "15 January 2028",
            "visa_application_window": "December 2027 to February 2028",
            "semester_commencement": "Late February / Early March 2028",
            "annual_cycle_notes": "Main international scholarship round closes 30 September for commencement in Semester 1 (February)."
        },
        "selection_process_and_weights": {
            "academic_weight": "40% (Honours 1 equivalence, coursework grades, and undergraduate/postgraduate GPA)",
            "extracurricular_and_leadership_weight": "0% (Not considered for HDR scholarships)",
            "research_experience_weight": "40% (Peer-reviewed publications, master thesis quality, patents, and research proposal caliber)",
            "work_experience_weight": "5% (Professional technical or R&D engineering experience)",
            "personal_statement_weight": "5% (Statement of research alignment)",
            "recommendations_weight": "10% (Rigor and conviction of academic referee appraisals)",
            "interview_weight": "0% (Official scoring is dossier-based; supervisor interview establishes candidacy)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 85 compliance)",
            "financial_need_weight": "0% (Purely merit and research performance based)",
            "selection_panel_composition": "College Research Higher Degree Committee, Associate Dean Research, and Dean of Graduate Studies.",
            "evaluation_methodology": "Standardized merit ranking: Applications are scored on a standardized matrix measuring Academic Merit (0-50 pts) and Research Experience / Track Record (0-50 pts). Applicants with strong research proposals, H1 equivalence, and supervisor endorsement are ranked and awarded UNIPRS/RTP packages."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international applicants across all faculties for ~100 scholarships",
            "total_scholarships_awarded": "~80 to 120 fully funded UNIPRS and RTP scholarships",
            "acceptance_rate_global": "~9.5%",
            "acceptance_rate_pakistan": "~11.0% (Solid success rate for Pakistani STEM graduates with research publications)",
            "typical_successful_applicant_gpa": "3.55+ / 4.00 CGPA (80%+ aggregate)",
            "typical_academic_and_research_profile": "First Class Honours or MS with 1+ peer-reviewed conference or journal publication, good thesis dissertation, and strong supervisor endorsement.",
            "common_backgrounds_of_winners": "Graduates from NUST, FAST-NUCES, GIKI, UET, COMSATS, LUMS, and PIEAS in Computer Science, Data Science, and Engineering.",
            "high_representation_countries": "China, India, Pakistan, Iran, Vietnam, Bangladesh, Nigeria",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized migration agencies claiming to guarantee Newcastle research scholarships. Scholarships are awarded strictly by the Dean of Graduate Studies through academic merit ranking."
            ],
            "application_fee_warning": "UON charges zero application fees for postgraduate research programs. Never pay fees to private intermediaries.",
            "agent_and_intermediary_warnings": "Direct correspondence with professors is strictly evaluated; third-party agents should not be used.",
            "hidden_costs_breakdown": [
                "Australian Student Visa (Subclass 500) application fee (AUD 1,600; ~PKR 296,000).",
                "Biometrics and visa medical examination in Pakistan (~PKR 35,000 - 50,000).",
                "Initial settling cash and apartment bond in Newcastle (~AUD 1,500; ~PKR 277,500)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: Regional universities require lower English scores. (FACT: UON enforces strict IELTS 6.5 / TOEFL 85 requirements with no waivers via MOI).",
                "CLAIM: Master by Coursework qualifies for UNIPRS. (FACT: UNIPRS is strictly restricted to Higher Degree by Research - PhD and MPhil)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Third-party blogs list the stipend at older rates (AUD 28,000); official 2024/2025 rates are indexed between AUD 32,000 and 35,000 per annum."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must pass annual candidature milestones: Confirmation of Candidature (Month 12) and Annual Progress Reviews.",
            "attendance_requirements": "Full-time on-campus research residency in Newcastle, with active laboratory attendance and seminar participation.",
            "academic_progress_monitoring": "Annual Review of Progress submitted to Dean of Graduate Studies and verified by supervisory panel.",
            "work_restrictions_during_study": "Full-time candidates may work up to 8-10 hours per week during normal business hours as sessional tutors or lab demonstrators, provided it does not delay doctoral completion.",
            "home_country_return_obligation": "None. Graduates are eligible for Australian Subclass 485 Post-Study Work visa (regional study grants 4-5 years work rights) and regional permanent residency pathways (Subclass 190/491).",
            "service_obligations_or_bonds": "Zero service bonds or repayment conditions.",
            "repayment_clawback_conditions": "Scholarship terminates upon academic dismissal, failure of candidature confirmation, or unauthorized withdrawal; past funds are not reclaimed.",
            "rules_for_changing_university": "Non-transferable to other Australian universities.",
            "rules_for_changing_major": "Topic adjustments must remain within the scope of faculty research and receive formal Graduate Studies approval.",
            "extension_policy": "PhD candidates may apply for a single 6-month extension beyond 3.5 years under exceptional circumstances beyond the candidate's control."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Newcastle Postgraduate Research Scholarships Portal",
                "source_url": "https://www.newcastle.edu.au/research/postgraduate-research/fees-and-scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific college-level quota allocations for international versus domestic RTP awards.",
                    "Exact numerical cutoff scores on the 100-point HDR merit scoring matrix for the current round.",
                    "Nationality-specific applicant and awardee statistics."
                ]
            },
            {
                "source_name": "Australian Government Department of Education Research Training Program (RTP)",
                "source_url": "https://www.education.gov.au/research-block-grants/research-training-program",
                "source_type": "GOVERNMENT_MINISTRY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Annual Commonwealth block grant distribution formulas for regional universities.",
                    "International candidate reserve reallocation rates."
                ]
            }
        ]
    },
    "SCH-OC-018": {
        "scholarship_id": "SCH-OC-018",
        "basic_details": {
            "scholarship_name": "University of Auckland International Student Excellence Scholarship",
            "offering_entity": "University of Auckland (Auckland, New Zealand)",
            "host_country": "New Zealand",
            "host_institutions_covered": "University of Auckland Campuses: City Campus, Grafton Campus, and Newmarket Campus (Auckland, New Zealand)",
            "degree_levels": ["Bachelor of Science / Engineering (BS / BE)", "Master of Science / Engineering (MS / ME)", "Postgraduate Diploma (PGDip)"],
            "major_restrictions": "Open to high-achieving international students enrolling in full-time undergraduate or postgraduate taught/research programs: Faculty of Science (Computer Science, Data Science, Artificial Intelligence), Faculty of Engineering (Software Engineering, Electrical and Electronic Engineering, Civil Engineering), Faculty of Medical and Health Sciences, and Auckland Business School.",
            "number_of_awards_total": "Up to 50 prestigious International Student Excellence Scholarships awarded annually (across two biannual rounds)",
            "number_of_awards_pakistan": "Open international competition; high-performing Pakistani students in computer science, software engineering, and business analytics represent an active cohort (typically 3 to 6 awardees/yr)",
            "funding_classification": "PARTIALLY_FUNDED",
            "duration_of_scholarship": "One-year tuition fee credit of up to NZD 10,000 paid towards compulsory international tuition fees in the first year of study"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["International students who are not citizens, permanent residents, or resident visa holders of New Zealand or Australia"],
            "pakistan_eligible": True,
            "age_limit_undergrad": None,
            "age_limit_postgrad": None,
            "age_limit_notes": "No age restrictions.",
            "academic_qualifications": "For Undergraduate: Completed Pakistani Higher Secondary School Certificate (HSSC / Intermediate) with minimum 85% marks or Cambridge A-Levels with minimum AAA/AAB (or equivalent 12 years education with high distinction). For Postgraduate: Completed 4-year Bachelor's degree (16 years education) with minimum 3.60 / 4.00 CGPA (or GPE of 6.00 / 9.00 on Auckland scale) from an HEC-recognized university in Pakistan.",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.6,
            "grading_conversion_notes": "Evaluated against University of Auckland Grade Point Equivalent (GPE) scale: minimum GPE of 6.00 out of 9.00 (equivalent to B+ to A- average) required for scholarship consideration.",
            "subject_background_prerequisites": "Strong background in Mathematics, Computing, Physics, or relevant discipline for engineering and science faculties.",
            "current_education_status": "Must have received an unconditional offer of admission or conditional offer of admission to the University of Auckland.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Not required; selection is primarily academic merit and personal statement based.",
            "english_proficiency": {
                "test_required": True,
                "ielts_minimum": 6.5,
                "toefl_minimum": 90,
                "duolingo_accepted": False,
                "moi_certificate_accepted": False,
                "notes": "IELTS Academic overall min 6.5 (all bands 6.0+); TOEFL iBT min 90 (writing 21); or PTE Academic min 58 (50 in skills). English Medium of Instruction certificates are not accepted."
            },
            "other_language_requirements": "None; all coursework and examinations are in English.",
            "gender_specific_requirements": "None.",
            "financial_need_required": False,
            "special_eligibility_categories": "New international students commencing full-time undergraduate or postgraduate study.",
            "previous_scholarship_restrictions": "Cannot combine with another University of Auckland tuition fee scholarship.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "PARTIALLY_COVERED",
                "details": "Tuition fee credit of up to NZD 10,000 (~PKR 1,700,000) applied directly towards compulsory first-year international tuition fees (annual tuition is ~NZD 42,000 to 50,000).",
                "amount": "Up to NZD 10,000 tuition reduction (~PKR 1,700,000 value)"
            },
            "admission_application_fee": {
                "status": "100% WAIVED",
                "details": "University of Auckland charges no application fee for international direct online applications.",
                "amount": "NZD 0 (Free application)"
            },
            "accommodation": {
                "status": "NOT_COVERED",
                "details": "Accommodation is self-funded; guaranteed place in university student residences (Carlaw Park Student Village, O'Rorke Hall, Grafton Hall) costing ~NZD 280 to 450/week (~PKR 48,000 to 76,000/wk).",
                "amount": "Self-funded (~NZD 14,000 to 18,000 / year)"
            },
            "monthly_stipend": {
                "status": "NOT_COVERED",
                "details": "Scholarship does not provide a monthly living stipend; living expenses are self-funded by student (students can work part-time up to 20 hrs/week on student visa).",
                "amount": "NZD 0 (Self-funded living)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Round-trip airfare between Pakistan and Auckland International Airport (AKL) is self-funded by student.",
                "amount": "Self-funded (~PKR 250,000 to 380,000 round-trip value)"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "New Zealand Student Visa application fee (NZD 430) paid to Immigration New Zealand.",
                "amount": "NZD 430 (~PKR 73,000)"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Comprehensive Studentsafe-University international student health and travel insurance required (~NZD 750/year; ~PKR 127,500/year).",
                "amount": "Self-funded (~NZD 750 / year)"
            },
            "food_allowance": {
                "status": "NOT_COVERED",
                "details": "Self-funded; student groceries and campus dining average NZD 120 to 180 per week (~PKR 20,000 to 30,000/wk).",
                "amount": "Self-funded"
            },
            "books_and_materials_allowance": {
                "status": "NOT_COVERED",
                "details": "Textbooks and personal computer equipment are self-funded.",
                "amount": "Self-funded (~NZD 1,000 / year)"
            },
            "research_funding_conference_grant": {
                "status": "NOT_APPLICABLE",
                "details": "For coursework/undergraduate students; postgraduate research students may access faculty conference travel grants.",
                "amount": "Not included in scholarship package"
            },
            "travel_transit_allowance": {
                "status": "NOT_COVERED",
                "details": "Auckland AT HOP transport card transit is self-funded (tertiary student discount available on buses, trains, and ferries).",
                "amount": "Self-funded (~NZD 100 / month; ~PKR 17,000 / mo)"
            },
            "total_estimated_value_usd_per_year": 8000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single top-ranked national institution: University of Auckland (Auckland, New Zealand)",
            "participating_institutions": [
                "University of Auckland - City Campus (Auckland Central)",
                "University of Auckland - Grafton Campus (Medical and Health Sciences)",
                "University of Auckland - Newmarket Campus (Engineering and Science Research)"
            ],
            "university_rankings_scope": "Ranked #65 globally in QS World University Rankings 2024/2025; ranked #1 university in New Zealand. Outstanding global reputation for computer science, software engineering, and data science.",
            "available_majors": [
                "Faculty of Science: Computer Science, Data Science, Information Systems, Mathematics, Statistics",
                "Faculty of Engineering: Software Engineering, Computer Systems Engineering, Electrical and Electronic Engineering",
                "Auckland Business School: Master of Business Analytics, Master of Information Technology, Master of Commerce",
                "Faculty of Medical and Health Sciences: Biomedical Science, Pharmacology, Public Health",
                "Faculty of Science: Environmental Science, Biological Sciences, Chemistry"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Undergraduate (BS/BE): 3 to 4 years; Master (Taught/Research): 1 to 2 years; PGDip: 1 year.",
            "admission_requirements_summary": "Intermediate 85%+ or Bachelor's with 3.6+ CGPA (GPE 6.0+), unconditional/conditional admission offer to Auckland, 500-word personal statement, 1 referee letter, and IELTS 6.5.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Master of Information Technology and Master of Business Analytics have very high application numbers; Faculty of Science MSc programs offer competitive scholarship selection margins.",
            "strategic_program_match_advice": "Applicants MUST apply for university admission first and obtain an Auckland Student ID number before applying for the scholarship. The scholarship application requires a compelling 500-word statement explaining how studying at Auckland will impact your career and home country."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.auckland.ac.nz/en/study/applications-and-admissions.html",
            "portal_system_name": "University of Auckland Online Admissions Portal & Scholarships Application System",
            "account_creation_instructions": "Submit direct online application for degree admission via Auckland portal, receive Auckland Student ID Number and Offer of Admission, then apply for the scholarship via the dedicated Scholarships Portal.",
            "step_by_step_workflow": [
                "Step 1 (August - October): Submit online application for admission to preferred undergraduate or postgraduate degree program at University of Auckland.",
                "Step 2 (September - October): Receive conditional or unconditional Offer of Admission and official 9-digit Auckland Student ID number.",
                "Step 3 (10 October): Scholarship application portal opens; log in to the Scholarships Application Portal using Auckland Student ID credentials.",
                "Step 4 (October - November): Complete scholarship form, write 500-word personal statement, provide academic referee contact details, and upload transcripts.",
                "Step 5 (By 21 November): Submit scholarship application before official closing date.",
                "Step 6 (December): University of Auckland Scholarships Selection Committee assesses applications based on academic GPA and personal statement.",
                "Step 7 (Mid-January): Scholarship award notifications issued via email; recipients accept offer within 14 days.",
                "Step 8 (January): Apply for New Zealand Student Visa via Immigration New Zealand (INZ) online portal; book flights to Auckland.",
                "Step 9 (Late February): Travel to Auckland, attend international student orientation, check into university accommodation, and begin Semester 1."
            ],
            "university_vs_scholarship_routing": "Two-stage sequential application: Admission application must be lodged first to generate Student ID; scholarship application is submitted through separate scholarships portal.",
            "recommendation_letters_submission_method": "One academic referee contact provided in portal; referee receives automated link to upload recommendation.",
            "personal_statement_prompts": "Personal Statement (500 words): Outline your academic goals, why you chose the University of Auckland, how this scholarship will assist your studies, and your future career plans.",
            "study_plan_research_proposal_requirements": "Not required for undergraduate or taught master's applicants; research master's applicants upload 1-2 page research outline.",
            "cv_format_requirements": "Standard academic CV outlining educational history, academic distinctions, extracurricular leadership, and community service.",
            "interviews_conducted": False,
            "interview_format_details": "No interview required; selection is strictly based on academic GPA and quality of personal statement.",
            "standardized_tests": "IELTS Academic 6.5 (all bands 6.0+) or TOEFL iBT 90 (writing 21) or PTE 58. GRE not required.",
            "application_fee_amount": "NZD 0 (Free application for international students)",
            "attestation_requirements": "Attestation by IBCC/HEC and MOFA Pakistan, accompanied by certified verified copies.",
            "translation_requirements": "Certified official English translations for any documents not in English.",
            "final_submission_method": "100% digital submission via the University of Auckland scholarships application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Valid International Passport Copy",
                "mandatory": True,
                "specification": "Clear color scan of passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Ensure clear color scan of Pakistani machine-readable passport."
            },
            {
                "document_name": "University of Auckland Offer of Admission",
                "mandatory": True,
                "specification": "Official conditional or unconditional Offer of Place letter showing Auckland Student ID.",
                "pakistan_specific_instruction": "Mandatory prerequisite; cannot access scholarship form without active student ID."
            },
            {
                "document_name": "Official Academic Transcripts and Certificates",
                "mandatory": True,
                "specification": "Certified transcripts showing all semesters, grades, grading scale, and degree completion certificates.",
                "pakistan_specific_instruction": "Attested by Higher Education Commission (HEC) or IBCC and MOFA Pakistan."
            },
            {
                "document_name": "Personal Statement (500 words)",
                "mandatory": True,
                "specification": "Structured statement detailing academic goals, reasons for choosing Auckland, and future plans.",
                "pakistan_specific_instruction": "Demonstrate clear connection between your studies and potential contributions to Pakistan/society."
            },
            {
                "document_name": "Academic Referee Endorsement",
                "mandatory": True,
                "specification": "Confidential recommendation submitted directly by academic referee via portal.",
                "pakistan_specific_instruction": "Must be on institutional letterhead with official institutional email address."
            },
            {
                "document_name": "English Language Proficiency Test Scorecard",
                "mandatory": True,
                "specification": "Official IELTS Academic, TOEFL iBT, or PTE Academic scorecard dated within 2 years.",
                "pakistan_specific_instruction": "Direct electronic score dispatch through testing agency portal."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "10 October 2026 (Round 1 for Semester 1) / 9 March 2027 (Round 2 for Semester 2)",
            "application_deadline": "21 November 2026 (Round 1) / 20 April 2027 (Round 2)",
            "university_admission_deadline": "15 October 2026 (to ensure offer is issued before scholarship close)",
            "document_submission_deadline": "21 November 2026",
            "recommendation_letters_deadline": "28 November 2026",
            "interview_period": "Not applicable (Document review)",
            "shortlist_announcement": "Mid-January 2027 (Round 1) / Early June 2027 (Round 2)",
            "final_result_acceptance_deadline": "Within 14 days of offer notification",
            "visa_application_window": "January to February 2027",
            "semester_commencement": "Late February / Early March 2027 (Semester 1)",
            "annual_cycle_notes": "Biannual scholarship intake: Round 1 closes in November for Semester 1 (Feb); Round 2 closes in April for Semester 2 (July)."
        },
        "selection_process_and_weights": {
            "academic_weight": "60% (Undergraduate/High School GPA converted to Auckland GPE scale)",
            "extracurricular_and_leadership_weight": "10% (Community leadership, volunteerism, and extracurricular achievements)",
            "research_experience_weight": "5% (For postgraduate applicants: prior projects or publications)",
            "work_experience_weight": "5% (Professional experience in relevant industry)",
            "personal_statement_weight": "15% (Quality, clarity, and persuasiveness of 500-word personal statement)",
            "recommendations_weight": "5% (Strength of academic referee endorsement)",
            "interview_weight": "0% (No interview required)",
            "test_scores_weight": "Threshold requirement (IELTS 6.5 / TOEFL 90 compliance)",
            "financial_need_weight": "0% (Purely merit-based scholarship)",
            "selection_panel_composition": "University of Auckland Scholarships Committee chaired by Dean of Graduate Studies / Director of International.",
            "evaluation_methodology": "Merit-based ranking: Applicants are ranked by Grade Point Equivalent (GPE) with top candidates (GPE >= 7.00 / 9.00, equivalent to A- or above) reviewed by the selection panel. The panel assesses personal statements for leadership potential and alignment with university values, selecting up to 50 awardees."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~800 to 1,200 international applicants across both biannual rounds",
            "total_scholarships_awarded": "Up to 50 scholarships per year (NZD 10,000 each)",
            "acceptance_rate_global": "~5.0%",
            "acceptance_rate_pakistan": "~6.0% (Selective; awarded to high-achieving Pakistani intermediate board and university toppers)",
            "typical_successful_applicant_gpa": "3.75+ / 4.00 CGPA (or 88%+ in Intermediate, GPE 7.50+ / 9.00)",
            "typical_academic_and_research_profile": "Distinguished academic record, strong English scores (IELTS 7.0+), articulate personal statement outlining clear career vision, and active community involvement.",
            "common_backgrounds_of_winners": "Graduates from NUST, FAST-NUCES, GIKI, LUMS, UET, and top intermediate colleges (BISE Lahore, FBISE) in computer science, software engineering, and business analytics.",
            "high_representation_countries": "China, India, United States, Malaysia, Indonesia, Pakistan, Vietnam",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Unauthorized commercial recruiters claiming to sell Auckland excellence scholarships. Scholarships are awarded strictly by the University of Auckland Scholarships Committee through academic merit."
            ],
            "application_fee_warning": "University of Auckland application for admission and scholarship is 100% free of charge. Never pay fees to private recruiters.",
            "agent_and_intermediary_warnings": "Applications submitted through commercial agents must still contain the student's authentic personal statement; templated statements are penalized.",
            "hidden_costs_breakdown": [
                "Remaining tuition balance (NZD 32,000 to 40,000 / year; ~PKR 5,440,000 to 6,800,000/yr) must be covered by student.",
                "Living and accommodation costs in Auckland (~NZD 20,000 to 25,000/year; ~PKR 3,400,000 to 4,250,000/yr).",
                "New Zealand Student Visa fee (NZD 430; ~PKR 73,000).",
                "Studentsafe mandatory health insurance (~NZD 750/year; ~PKR 127,500/yr)."
            ],
            "misleading_claims_debunked": [
                "CLAIM: The scholarship covers 100% of all expenses. (FACT: It is a partial tuition waiver of up to NZD 10,000 for the first year only; living and remaining fees are self-funded).",
                "CLAIM: English requirement can be waived with an MOI letter. (FACT: Official IELTS, TOEFL, or PTE test report is strictly mandatory for Auckland admission)."
            ],
            "official_vs_unofficial_discrepancies": [
                "Some education portals market this as a full scholarship; official regulations confirm it is a one-off NZD 10,000 tuition fee reduction."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must maintain continuous full-time enrollment and satisfactory academic progress in enrolled courses.",
            "attendance_requirements": "Full-time physical on-campus attendance at Auckland lectures, tutorials, and laboratory sessions.",
            "academic_progress_monitoring": "Semester-by-semester academic performance reviews conducted by faculty.",
            "work_restrictions_during_study": "International students holding a New Zealand Student Visa are permitted to work up to 20 hours per week during term time and full-time during scheduled academic vacations.",
            "home_country_return_obligation": "None. Graduates are eligible to apply for the New Zealand Post-Study Work Visa (up to 3 years work rights depending on degree qualification).",
            "service_obligations_or_bonds": "Zero service bonds or repayment conditions.",
            "repayment_clawback_conditions": "If recipient withdraws from study or transfers out of the university during the first year, the scholarship value must be repaid in full.",
            "rules_for_changing_university": "Non-transferable to other New Zealand universities.",
            "rules_for_changing_major": "Changing major or program within Auckland is permitted subject to approval by the Scholarships Office.",
            "extension_policy": "Strictly a one-off first-year scholarship; non-renewable for subsequent academic years."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Auckland International Student Excellence Scholarship Official Portal",
                "source_url": "https://www.auckland.ac.nz/en/study/scholarships-and-awards/find-a-scholarship/university-of-auckland-international-student-excellence-scholarship-844-all.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Specific allocation ratio between undergraduate and postgraduate applicants across each round.",
                    "Exact numerical cutoff score on the GPE scale for final scholarship shortlisting.",
                    "Historical nationality-wise applicant and recipient numbers."
                ]
            },
            {
                "source_name": "University of Auckland International Student Admissions Guidelines",
                "source_url": "https://www.auckland.ac.nz/en/study/international-students.html",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": [
                    "Waitlist fill rates for unaccepted scholarship offers.",
                    "Discretionary faculty top-up bursaries for high-ranking STEM applicants."
                ]
            }
        ]
    }
}
