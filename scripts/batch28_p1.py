"""Batch 28 Part 1: European Flagship & Foundation Scholarships (3 awards)
SCH-EU-056: Hans Böckler Foundation International Fellowships (Germany)
SCH-EU-057: LUT University Master's Scholarship (Finland)
SCH-EU-058: University of Luxembourg Guillaume Dupaix Master's Award (Luxembourg)
"""

DATA_P1 = {
    "SCH-EU-056": {
        "scholarship_id": "SCH-EU-056",
        "basic_details": {
            "scholarship_name": "Hans Böckler Foundation International Doctoral & Postgraduate Fellowships (Hans-Böckler-Stiftung)",
            "offering_entity": "Hans Böckler Foundation (Hans-Böckler-Stiftung - HBS) & German Confederation of Trade Unions (DGB)",
            "host_country": "Germany",
            "host_institutions_covered": "State-accredited German Universities and Technical Universities (TU9 & Flagship Universities across Germany)",
            "degree_levels": ["Doctor of Philosophy (PhD / Promotion)", "Master of Science (MSc / MA)"],
            "major_restrictions": "Economics, Social Sciences, Industrial Relations, Labour Law, Political Science, Sustainable Engineering, Environmental Sciences, and Digital Transformation.",
            "number_of_awards_total": "~120 to 180 doctoral and graduate scholarships awarded annually across Germany",
            "number_of_awards_pakistan": "Open internationally; typically 4 to 8 Pakistani scholars demonstrating commitment to labor rights and social justice selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 36 months (3 years) for PhD; up to 24 months (2 years) for Master's",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Monthly tax-free living stipend of €1,450 / month for PhD (~PKR 435,000 / month) plus €100 / month research research costs allowance; €934 / month for Master's (~PKR 280,200 / month) plus family/childcare allowances, health insurance subsidies, and tuition-free public German university education"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to German citizens, EU nationals, and international applicants of all nationalities including Pakistan"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No strict statutory age limit; doctoral candidates must have obtained their master's degree within the preceding 3 to 4 years.",
            "academic_qualifications": "Completed recognized 18-year Master's degree (for PhD) or recognized 16-year Bachelor's degree (for Master's) with above-average academic performance (minimum German grade 2.0 or equivalent to CGPA 3.30+/4.00) from an HEC-recognized institution.",
            "minimum_gpa_percentage": 80.0,
            "minimum_gpa_scale": 3.3,
            "grading_conversion_notes": "German grading scale minimum 2.0 (gut) or CGPA 3.30 / 4.00; competitive candidates typically hold CGPA >= 3.60 / 4.00.",
            "subject_background_prerequisites": "Economics, sociology, political science, law, labour studies, sustainability, public policy, or industrial engineering.",
            "current_education_status": "Graduated or final-year students completing master's degree prior to fellowship commencement.",
            "graduation_year_restrictions": "Master's degree completed within last 4 years for PhD track.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Demonstrated socio-political commitment, engagement in trade unions, youth advocacy, workers' rights, or democratic initiatives is a mandatory evaluation criterion.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 85,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 or TOEFL iBT minimum 85 for English-medium programs; German language proficiency (CEFR B2/C1) is strongly advantageous and required for German-medium universities.",
            "other_language_requirements": "Basic conversational German (A2/B1) recommended to participate in Foundation network seminars.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants must demonstrate active socio-political or civic engagement aligned with the ethos of the trade union movement and democratic labor representation.",
            "previous_scholarship_restrictions": "Cannot hold another parallel scholarship from German Begabtenförderungswerke (e.g. DAAD, FES, KAS) covering identical costs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee covered; German public universities charge zero tuition fees for doctoral researchers.",
                "amount": "100% tuition-free public university education"
            },
            "admission_application_fee": {
                "status": "COVERED",
                "details": "Applying to Hans Böckler Foundation is completely free of charge.",
                "amount": "€0 (Free application)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized student residence hall apartments through Studierendenwerk (approx. €280 to €450 / month), paid easily from living stipend.",
                "amount": "Subsidized student dormitories"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Monthly tax-free living stipend: €1,450 / month for PhD (~PKR 435,000 / month) plus €100 / month research allowance (€1,550 total); €934 / month for Master's (~PKR 280,200 / month).",
                "amount": "€934 to €1,550 / month"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "Relocation travel between Pakistan and Germany is self-funded by the student.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "German National Student Visa fee (€75 / ~PKR 23,000) paid at German Embassy in Islamabad or Consulate in Karachi.",
                "amount": "€75 borne by candidate"
            },
            "health_insurance": {
                "status": "SUBSIDIZED",
                "details": "Health and nursing care insurance subsidy of up to €100 / month provided to doctoral scholarship recipients.",
                "amount": "Up to €100 / month health insurance subsidy"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized campus dining halls (Mensa) across German universities; daily meals cost €3 to €6.",
                "amount": "Subsidized campus Mensa dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Dedicated monthly research cost allowance (Forschungskostenpauschale) of €100 / month, plus full access to university libraries and archives.",
                "amount": "€100 / month research materials allowance"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Travel and conference grants available for archival research, field studies, and international academic presentations.",
                "amount": "Archival research & conference travel subsidies"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "Semester ticket (Deutschlandticket integration) providing free public regional rail and urban transit across Germany.",
                "amount": "Free regional & urban transit via semester ticket"
            },
            "total_estimated_value_usd_per_year": 23000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Multiple host institutions (any recognized public university or research institute in Germany).",
            "participating_institutions": [
                "Humboldt University of Berlin",
                "Free University of Berlin",
                "University of Cologne",
                "Goethe University Frankfurt",
                "Technical University of Munich (TUM)",
                "University of Duisburg-Essen",
                "Bremen University",
                "WZB Berlin Social Science Center"
            ],
            "university_rankings_scope": "All top-tier German universities; renowned particularly in labor economics, industrial sociology, public policy, and environmental transformation.",
            "available_majors": [
                "Doctor of Philosophy (PhD) in Economics and Labour Markets",
                "PhD in Sociology and Social Inequalities",
                "PhD in Political Science and Democratic Governance",
                "PhD in Labour Law and European Social Law",
                "PhD in Sustainable Engineering and Green Transition",
                "PhD in Environmental Governance and Climate Policy",
                "MSc / MA in Socio-Ecological Economics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "Master's: 2 years; PhD: 3 years (extensible to 4 years)",
            "admission_requirements_summary": "Master's degree with German grade 2.0+ (CGPA >= 3.30/4.00), doctoral supervision confirmation (Betreuungszusage) from a German university professor, detailed research exposé (8-12 pages), two academic letters of recommendation, and documented social/civic engagement record.",
            "is_admission_separate_from_scholarship": True,
            "pre_admission_acceptance_letter_required": True,
            "easiest_hardest_institutions_guidance": "Securing an official doctoral supervision confirmation (Betreuungszusage) from a German university professor is the essential prerequisite before submitting the HBS scholarship application.",
            "strategic_program_match_advice": "Focus dissertation proposals on social inequality, labor market transformation due to AI/automation, just climate transition, or global supply chain workers' rights."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.boeckler.de/de/stipendien-bewerbung-2183.htm",
            "portal_system_name": "Hans Böckler Foundation Online Application Portal",
            "account_creation_instructions": "Secure supervision confirmation from German professor, register on HBS application portal during bi-annual intake, upload research exposé, CV, transcripts, and proof of civic engagement, and register academic referees.",
            "step_by_step_workflow": [
                "Step 1: Secure doctoral supervision commitment (Betreuungszusage) from a full professor at an accredited German university.",
                "Step 2: Draft comprehensive 8 to 12-page research proposal (Exposé) detailing methodology, timeline, and socio-economic relevance.",
                "Step 3: Register on Hans Böckler Foundation online portal during open application call (by February 1 or October 1).",
                "Step 4: Upload attested transcripts, CV, exposé, and documentation of socio-political/civic commitment.",
                "Step 5: Academic referees submit formal confidential appraisals directly.",
                "Step 6: Preliminary committee screening and review by external expert reviewers (Fachgutachter).",
                "Step 7: Shortlisted candidates invited for personal/virtual selection interview (Auswahlgespräch) in Germany or via Zoom.",
                "Step 8: Final award decision announced in June (for October start) or December (for April start).",
                "Step 9: Apply for German National Visa and matriculate at host university."
            ],
            "university_vs_scholarship_routing": "Separate Routing: Candidates must first secure admission/supervision at a German university, then apply independently to Hans Böckler Foundation for fellowship funding.",
            "recommendation_letters_submission_method": "Submitted directly by two academic professors (one must be the doctoral supervisor) using official HBS evaluation forms.",
            "personal_statement_prompts": "Detailed essay outlining personal trajectory, motivation, socio-political engagement, trade union or community service, and democratic values.",
            "study_plan_research_proposal_requirements": "Exhaustive research proposal (8 to 12 pages) outlining research question, state of research, theoretical framework, methodology, archive access, and 3-year work plan.",
            "cv_format_requirements": "Complete tabular academic CV in German or English detailing education, publications, employment, and social/civic activities.",
            "interviews_conducted": True,
            "interview_format_details": "Rigorous selection interview conducted by an HBS selection committee panel comprising university professors, union representatives, and foundation staff.",
            "standardized_tests": "IELTS 6.5+ or TOEFL 85+ for English doctoral programs; German language proof if applicable.",
            "application_fee_amount": "€0 (Completely free to apply)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations required for Pakistani credentials.",
            "translation_requirements": "Certified German or English translation for all non-German/non-English documents.",
            "final_submission_method": "Online submission via Hans Böckler Foundation application portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificates",
                "mandatory": True,
                "specification": "Complete Bachelor's and Master's degree certificates and transcripts with minimum German grade 2.0 (CGPA >= 3.30).",
                "pakistan_specific_instruction": "Attested by HEC and MoFA Pakistan."
            },
            {
                "document_name": "Doctoral Supervision Commitment (Betreuungszusage)",
                "mandatory": True,
                "specification": "Official signed letter from a German university professor confirming supervision of the doctoral thesis.",
                "pakistan_specific_instruction": "Obtained directly from German university professor."
            },
            {
                "document_name": "Detailed Research Proposal (Exposé, 8-12 Pages)",
                "mandatory": True,
                "specification": "Comprehensive doctoral research plan detailing theoretical framework, methodology, and 3-year timeline.",
                "pakistan_specific_instruction": "Structured scholarly proposal with complete bibliography."
            },
            {
                "document_name": "Proof of Socio-Political / Civic Engagement",
                "mandatory": True,
                "specification": "Official certificates, letters, or references documenting engagement in trade unions, civil society, advocacy, or community service.",
                "pakistan_specific_instruction": "Documented proof of leadership or volunteer work."
            },
            {
                "document_name": "Two Academic Letters of Recommendation",
                "mandatory": True,
                "specification": "Confidential evaluation letters from university professors (including prospective German supervisor).",
                "pakistan_specific_instruction": "On institutional letterhead with official stamps."
            },
            {
                "document_name": "Tabular Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive CV detailing education, publications, professional roles, and civic engagement.",
                "pakistan_specific_instruction": "European standard tabular CV format."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "December 1 (Summer intake) / August 1 (Winter intake)",
            "application_deadline": "February 1 (for April/May award) / October 1 (for December award)",
            "university_admission_deadline": "Concurrent with or prior to HBS submission",
            "document_submission_deadline": "February 1 / October 1",
            "recommendation_letters_deadline": "February 15 / October 15",
            "interview_period": "April - May / November - December",
            "shortlist_announcement": "Late May / Mid December",
            "final_result_acceptance_deadline": "Within 3 weeks of award notification",
            "visa_application_window": "June - July / January - February",
            "semester_commencement": "October 1 (Winter semester) / April 1 (Summer semester)",
            "annual_cycle_notes": "Bi-annual application cycles: February 1 deadline for spring review and October 1 deadline for autumn review."
        },
        "selection_process_and_weights": {
            "academic_weight": "35% (Prior academic grades, honors, course rigor, and scholarly feasibility)",
            "extracurricular_and_leadership_weight": "30% (Demonstrated socio-political commitment, trade union or civil society engagement, and democratic values)",
            "research_experience_weight": "20% (Scientific originality, theoretical rigor, and societal relevance of the doctoral exposé)",
            "work_experience_weight": "5% (Professional practice in policy, labor, or community leadership)",
            "personal_statement_weight": "5% (Clarity of personal trajectory and democratic conviction)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "0% (Interview is decisive binary pass/fail for shortlisted candidates)",
            "test_scores_weight": "0% (Language proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Need-blind merit and civic commitment evaluation)",
            "selection_panel_composition": "Hans Böckler Foundation Selection Board comprising university professors, German trade union leaders, and alumni representatives.",
            "evaluation_methodology": "Two-tier holistic evaluation assessing scientific excellence, research feasibility, and authentic socio-political engagement."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,000 to 1,400 applicants nationwide across both cycles",
            "total_scholarships_awarded": "~120 to 180 doctoral fellowships annually",
            "acceptance_rate_global": "~10% to 12%",
            "acceptance_rate_pakistan": "~8% to 12% for candidates with strong professor supervision backing and documented civil society engagement",
            "typical_successful_applicant_gpa": "Master's German grade <= 1.8 (CGPA >= 3.50/4.00), accompanied by proven civic, union, or community leadership",
            "typical_academic_and_research_profile": "Scholars in social sciences, economics, law, or green engineering with strong thesis records and dedicated participation in social justice initiatives.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani institutions (LUMS, Quaid-i-Azam, NUST, Karachi University, Punjab University).",
            "high_representation_countries": "Germany, Pakistan, Turkey, Italy, Spain, India, Colombia, Ukraine, Brazil.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal boeckler.de.",
                "Hans Böckler Foundation never charges application fees or endorses private consultancy agencies."
            ],
            "application_fee_warning": "Applying for HBS scholarships is 100% free of charge.",
            "agent_and_intermediary_warnings": "Commercial agency written statements are disqualified; the foundation rigorously probes personal civic commitment during selection interviews.",
            "hidden_costs_breakdown": [
                "Application fee: €0 (Free).",
                "German National Visa fee: €75 (~PKR 23,000).",
                "HEC and MoFA document attestations in Pakistan: ~PKR 15,000 to 25,000.",
                "One-way flight to Germany: ~PKR 150,000 to 220,000.",
                "Initial living deposit before first stipend payment: ~€500 (~PKR 150,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You must be a German citizen. Reality: International scholars from any country including Pakistan are fully eligible.",
                "Myth: You must be a trade union member before applying. Reality: Union membership is welcomed but not mandatory; general civic/social commitment is accepted."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial portals claim HBS requires German fluency for all majors; in reality, doctoral research conducted in English is fully eligible if supervisor supports it."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain satisfactory doctoral research progress and submit annual dissertation progress reports endorsed by supervisor.",
            "attendance_requirements": "Active participation in the Foundation's ideational support program (ideelle Förderung), including mandatory attendance at annual foundation seminars and regional scholar meetings.",
            "academic_progress_monitoring": "Annual progress report submitted to the Foundation's Department of Educational Support.",
            "work_restrictions_during_study": "Part-time academic work (e.g. teaching assistantship up to 10 hours/week) permitted with foundation approval; commercial employment strictly restricted.",
            "home_country_return_obligation": "None; zero service bond or return obligation (scholars may pursue international careers or postdocs globally).",
            "service_obligations_or_bonds": "Zero service bond.",
            "repayment_clawback_conditions": "Termination of fellowship if doctoral candidate abandons studies without valid grounds or fails annual review.",
            "rules_for_changing_university": "Permitted across German universities with foundation approval and supervisor transition.",
            "rules_for_changing_major": "Topic changes require formal approval from supervisor and foundation committee.",
            "extension_policy": "Standard tenure is 36 months; a 6 to 12-month extension may be granted upon application for final thesis completion."
        },
        "official_sources_verified": [
            {
                "source_name": "Hans Böckler Foundation Official Scholarship Portal",
                "source_url": "https://www.boeckler.de/de/stipendien-bewerbung-2183.htm",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Hans Böckler Foundation Promotion Support Guidelines",
                "source_url": "https://www.boeckler.de/de/promotionsfoerderung-2670.htm",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-EU-057": {
        "scholarship_id": "SCH-EU-057",
        "basic_details": {
            "scholarship_name": "LUT University Master's Scholarship Program & Finland Scholarship Scheme",
            "offering_entity": "LUT University (Lappeenranta-Lahti University of Technology LUT) & Finnish National Agency for Education (EDUFI)",
            "host_country": "Finland",
            "host_institutions_covered": "LUT University (Lappeenranta Campus and Lahti Campus, Finland)",
            "degree_levels": ["Master of Science in Technology (MSc Tech)", "Master of Science in Economics and Business Administration (MSc Econ)"],
            "major_restrictions": "School of Energy Systems (Energy Technology, Electrical Engineering, Mechanical Engineering), School of Engineering Science (Software Engineering, Chemical Engineering, Computational Science, Industrial Engineering), and LUT Business School.",
            "number_of_awards_total": "~120 to 160 full tuition and living allowance scholarships awarded annually to international master's candidates",
            "number_of_awards_pakistan": "Open internationally; typically 12 to 20 Pakistani engineering and business students selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 24 months (2-year standard Master's degree)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Finland Scholarship provides 100% full tuition fee waiver (€13,500/year value) plus €5,000 one-off relocation grant in Year 1; LUT 100% Tuition Scholarship provides full €13,500/year tuition waiver with living costs (~€700-€900/month) supported via university student research assistantships"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Non-EU/EEA international citizens subject to Finnish tuition fees (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit.",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (BSc / BEng / BS / BBA) in a relevant engineering, science, or business discipline with superior academic standing (minimum CGPA 3.20/4.00 or 75% marks) from an HEC-recognized university.",
            "minimum_gpa_percentage": 75.0,
            "minimum_gpa_scale": 3.2,
            "grading_conversion_notes": "Minimum CGPA 3.20 / 4.00; competitive applicants typically hold CGPA >= 3.50 / 4.00.",
            "subject_background_prerequisites": "Energy technology, mechanical engineering, electrical engineering, software engineering, chemical engineering, computational science, data analytics, or international business.",
            "current_education_status": "Graduated or final-year undergraduate students completing degree requirements before July 31 of enrollment year.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Work experience or technical projects in renewable energy, power systems, software development, or circular economy are advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 88,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 (writing 5.5), TOEFL iBT minimum 88 (writing 20), PTE Academic minimum 62, or recognized English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "Finnish or Swedish language proficiency is NOT required; all international Master's programs are conducted 100% in English.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Applicants apply via Studyinfo.fi (Finnish national joint application portal) and apply for the LUT scholarship directly within the admission form.",
            "previous_scholarship_restrictions": "Cannot hold another parallel Finnish government scholarship covering identical tuition costs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee waiver for the complete 2-year Master's degree program at LUT University.",
                "amount": "100% covered (~€13,500 / year value; ~PKR 4,050,000 / year)"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "Finnish national application fee of €100 for non-EU/EEA applicants paid via Studyinfo.fi portal.",
                "amount": "€100 (~PKR 30,000)"
            },
            "accommodation": {
                "status": "SUBSIDIZED",
                "details": "Subsidized student housing through LOAS (Lappeenranta Student Housing Foundation) or Lahden Talot (approx. €280 to €450 / month including internet, heating, and water).",
                "amount": "Subsidized student apartments"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Finland Scholarship recipients receive €5,000 one-off relocation grant in Year 1; students typically earn €800 to €1,200/month through on-campus research assistantships and industrial master's thesis contracts.",
                "amount": "€5,000 relocation grant + paid thesis opportunities"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Helsinki Airport is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Finnish Residence Permit for Studies electronic application fee (€350) paid to Finnish Immigration Service (Migri).",
                "amount": "€350 borne by candidate"
            },
            "health_insurance": {
                "status": "NOT_COVERED",
                "details": "Mandatory private health insurance required for Finnish residence permit (approx. €250 to €350 / year, e.g. Swisscare / SIP).",
                "amount": "Approx. €300 / year borne by candidate"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized student cafeteria dining (Kela meal subsidy) across Lappeenranta and Lahti campuses; nutritious student lunches cost only €2.95 to €3.50.",
                "amount": "Government-subsidized campus dining (€3/meal)"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full digital access to LUT Academic Library, software tools (MATLAB, Ansys, SolidWorks), and high-performance computing labs.",
                "amount": "100% covered digital lab and computing resources"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Master's thesis projects in engineering at LUT are routinely sponsored by Finnish industry partners with thesis salaries of €1,500 to €2,500/month for 6 months.",
                "amount": "Industry-funded master's thesis projects"
            },
            "travel_transit_allowance": {
                "status": "SUBSIDIZED",
                "details": "50% discounted student fares on VR Finnish Railways and local city bus transit in Lappeenranta and Lahti.",
                "amount": "50% discounted public transit"
            },
            "total_estimated_value_usd_per_year": 20000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single leading Finnish technological and climate research university (LUT University).",
            "participating_institutions": [
                "LUT University (Lappeenranta Campus on Lake Saimaa and Lahti Campus, Finland)"
            ],
            "university_rankings_scope": "Times Higher Education (THE) World University Rankings Top 300 globally, World #9 for Climate Action (THE Impact Rankings 2024); recognized as a world leader in clean energy, solar power modeling, and circular economy.",
            "available_majors": [
                "MSc in Energy Technology (Energy Conversion, Nuclear Engineering)",
                "MSc in Electrical Engineering (Solar Economy, Power Electronics)",
                "MSc in Software Engineering and Digital Transformation",
                "MSc in Mechanical Engineering (Welding, Mechatronics)",
                "MSc in Chemical Engineering (Circular Economy, Water Treatment)",
                "MSc in Data-Centric Engineering and Computational Science",
                "MSc in Sustainable Science and Solutions",
                "MSc in International Business and Technology Management"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (Master of Science)",
            "admission_requirements_summary": "Relevant Bachelor's degree with CGPA >= 3.20/4.00, academic transcripts, grading scale guide, curriculum description of previous degree, English proficiency certificate (IELTS 6.5+ / TOEFL 88+ / MOI), motivation video/letter, and CV.",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Energy Technology and Software Engineering are intensely popular; ranking depends strictly on previous academic performance in mathematics, physics, and major subjects.",
            "strategic_program_match_advice": "Ensure your bachelor's degree transcript clearly displays at least 24 ECTS credits in mathematics/physics and at least 60 ECTS credits in the relevant engineering discipline."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://opintopolku.fi/konfo/en/ & https://www.lut.fi/en/admissions/masters-studies",
            "portal_system_name": "Studyinfo.fi (Opintopolku) Finnish National Joint Application Portal",
            "account_creation_instructions": "Register on Studyinfo.fi during the annual application window (December 1 to January 15), select LUT University programs, choose scholarship option, upload documents, and pay €100 application fee.",
            "step_by_step_workflow": [
                "Step 1: Check program prerequisites and credit requirements on lut.fi.",
                "Step 2: Register on Studyinfo.fi during the application period (December to mid-January).",
                "Step 3: Complete application form and select 'I apply for a scholarship'.",
                "Step 4: Upload attested transcripts, degree certificate, grading scale, CV, and English proficiency certificate.",
                "Step 5: Pay €100 non-EU application fee on Studyinfo.fi.",
                "Step 6: Departmental faculty review committee assesses academic compatibility and ranks applicants.",
                "Step 7: Admission results and scholarship decisions published in late March.",
                "Step 8: Accept study place and scholarship offer by the confirmation deadline (mid-April).",
                "Step 9: Apply online for Finnish Residence Permit via EnterFinland.fi and arrive in Finland in late August."
            ],
            "university_vs_scholarship_routing": "Integrated National Route: Admission and scholarship applications are integrated into a single submission on Studyinfo.fi.",
            "recommendation_letters_submission_method": "Not required; selection is based strictly on academic transcripts, course compatibility, and GPA ranking.",
            "personal_statement_prompts": "Program-specific motivation questions or recorded video interview answering career motivations, technical background, and relevance to LUT's clean technology focus.",
            "study_plan_research_proposal_requirements": "Detailed course matching description showing completed prerequisite coursework in engineering/mathematics.",
            "cv_format_requirements": "Academic CV detailing education, technical skills, projects, and work experience.",
            "interviews_conducted": False,
            "interview_format_details": "No live interviews; some programs require recorded asynchronous video responses embedded in the application.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 88+, PTE Academic 62+, or English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "€100 (approx. PKR 30,000)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations required for Pakistani credentials.",
            "translation_requirements": "Certified official English translation for all non-English documents.",
            "final_submission_method": "Online submission via Studyinfo.fi portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificate",
                "mandatory": True,
                "specification": "Complete Bachelor's degree certificate and transcripts with grading scale and CGPA >= 3.20/4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Grading Scale Legend & Credit Explanation",
                "mandatory": True,
                "specification": "Official university document detailing the grading system and conversion to European credit standards.",
                "pakistan_specific_instruction": "From degree-awarding university registrar."
            },
            {
                "document_name": "Course Description / Syllabus Overview",
                "mandatory": True,
                "specification": "Detailed course descriptions of completed mathematical and technical subjects verifying prerequisite fulfillment.",
                "pakistan_specific_instruction": "Official course catalogue or syllabus."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+ (writing 5.5+), TOEFL iBT 88+ (writing 20+), PTE 62+, or official MOI certificate.",
                "pakistan_specific_instruction": "Official test report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing education, project experience, technical software skills, and honors.",
                "pakistan_specific_instruction": "European standard format."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "December 1",
            "application_deadline": "January 15 (Strict annual Finnish joint application deadline)",
            "university_admission_deadline": "January 15",
            "document_submission_deadline": "January 22 (Document upload deadline)",
            "recommendation_letters_deadline": "Not applicable",
            "interview_period": "February (Asynchronous video review if required)",
            "shortlist_announcement": "Late March",
            "final_result_acceptance_deadline": "Mid-April (Binding confirmation deadline)",
            "visa_application_window": "April - June via EnterFinland.fi",
            "semester_commencement": "Late August / Early September",
            "annual_cycle_notes": "Single annual admission intake for autumn entry; application window strictly open December 1 to mid-January."
        },
        "selection_process_and_weights": {
            "academic_weight": "55% (Previous degree CGPA, mathematical proficiency, and academic rigor in major subjects)",
            "extracurricular_and_leadership_weight": "5% (Initiative and environmental/technical motivation)",
            "research_experience_weight": "25% (Undergraduate thesis quality, engineering project portfolio, and technical problem-solving)",
            "work_experience_weight": "10% (Relevant industrial engineering or software development experience)",
            "personal_statement_weight": "5% (Clarity of motivation and alignment with clean energy transition)",
            "recommendations_weight": "0% (Not factored into evaluation)",
            "interview_weight": "0% (No live interviews conducted)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and subject suitability based)",
            "selection_panel_composition": "LUT University Academic Admissions Committee and Degree Programme Academic Directors.",
            "evaluation_methodology": "Transparent merit-based ranking based on CGPA and mathematical/engineering credit compatibility."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~3,500 to 5,000 international applicants across Master's programs",
            "total_scholarships_awarded": "~120 to 160 full tuition scholarships annually",
            "acceptance_rate_global": "~5.0% to 6.5%",
            "acceptance_rate_pakistan": "~8.0% to 12.0% for applicants with strong engineering foundations and CGPA >= 3.50",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.50 / 4.00, accompanied by strong grades in calculus, physics, and major engineering courses",
            "typical_academic_and_research_profile": "Graduates in mechanical, electrical, chemical, or software engineering with solid programming skills and clear motivation for clean technology.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani engineering universities (NUST, FAST-NUCES, UET Lahore, GIKI, PIEAS, NED Karachi, COMSATS).",
            "high_representation_countries": "Pakistan, India, Vietnam, Bangladesh, China, Nigeria, Iran, Nepal.",
            "competitiveness_tier": "HIGH"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal opintopolku.fi (Studyinfo.fi) and lut.fi.",
                "Beware of private agents claiming to sell guaranteed Finnish scholarships; selection is 100% centralized through university academic scoring."
            ],
            "application_fee_warning": "Application fee of €100 is paid directly through the secure Studyinfo.fi portal.",
            "agent_and_intermediary_warnings": "Commercial agency materials are rejected; course matching must accurately reflect your actual transcript.",
            "hidden_costs_breakdown": [
                "Studyinfo application fee: €100 (~PKR 30,000).",
                "Finnish Residence Permit application fee: €350 (~PKR 105,000).",
                "Private health insurance: ~€300/year (~PKR 90,000).",
                "HEC document attestation in Pakistan: ~PKR 15,000.",
                "One-way flight to Helsinki: ~PKR 150,000 to 220,000.",
                "Mandatory Finnish subsistence maintenance requirement: Migri requires €560/month (€6,720/year) bank balance verification for student residence permit."
            ],
            "misleading_claims_debunked": [
                "Myth: You need to know Finnish. Reality: 100% of Master's degree studies at LUT are in English.",
                "Myth: Post-study work is difficult. Reality: Finland grants a generous 2-year post-study job seeker residence permit upon graduation."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim all LUT scholarships include living allowances; only the elite Finland Scholarship includes the €5,000 cash grant; standard LUT scholarships cover 100% tuition waiver."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Must complete at least 60 ECTS credits per academic year with satisfactory grades to retain the scholarship for Year 2.",
            "attendance_requirements": "Full-time physical study presence in Lappeenranta or Lahti; active participation in laboratory courses and lectures.",
            "academic_progress_monitoring": "Annual progress review conducted at the end of Year 1 evaluating completed credit total (minimum 60 ECTS required).",
            "work_restrictions_during_study": "Finnish student residence permit legally permits up to 30 hours per week of part-time work during academic terms, with unlimited hours during vacations.",
            "home_country_return_obligation": "None; zero service bond or return obligation (graduates are entitled to a 2-year Finnish post-study work permit).",
            "service_obligations_or_bonds": "Zero service bond.",
            "repayment_clawback_conditions": "Scholarship is cancelled for Year 2 if student completes fewer than 60 ECTS credits in Year 1.",
            "rules_for_changing_university": "Non-transferable to other Finnish universities.",
            "rules_for_changing_major": "Major change requires a new application via Studyinfo.fi.",
            "extension_policy": "Scholarship is valid strictly for the normative 2-year duration (4 semesters); study beyond 2 years incurs standard tuition fees."
        },
        "official_sources_verified": [
            {
                "source_name": "LUT University Master's Scholarships Official Portal",
                "source_url": "https://www.lut.fi/en/admissions/masters-studies/scholarships",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "Studyinfo.fi (Opintopolku) Finnish National Admissions Portal",
                "source_url": "https://opintopolku.fi/konfo/en/",
                "source_type": "OFFICIAL_GOVERNMENT",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    },

    "SCH-EU-058": {
        "scholarship_id": "SCH-EU-058",
        "basic_details": {
            "scholarship_name": "University of Luxembourg Guillaume Dupaix Master's Excellence Award",
            "offering_entity": "University of Luxembourg & Luxembourg Ministry of Foreign and European Affairs and Ministry of Higher Education and Research",
            "host_country": "Luxembourg",
            "host_institutions_covered": "University of Luxembourg (Belval Campus in Esch-sur-Alzette, Kirchberg Campus, and Limpertsberg Campus, Luxembourg)",
            "degree_levels": ["Master of Science (MSc)", "Master of Arts (MA)"],
            "major_restrictions": "Faculty of Science, Technology and Medicine (Computer Science, Information Security, Data Science, High-Performance Computing, Engineering, Physics, Mathematics), Faculty of Law, Economics and Finance, and Faculty of Humanities, Education and Social Sciences.",
            "number_of_awards_total": "~30 to 45 Guillaume Dupaix Excellence Awards awarded annually to top international master's students",
            "number_of_awards_pakistan": "Open internationally; typically 3 to 6 outstanding Pakistani students in computing, fintech, and data science selected annually",
            "funding_classification": "FULLY_FUNDED",
            "duration_of_scholarship": "Up to 24 months (2-year standard Master's degree tenure)",
            "tuition_waiver_type": "FULL",
            "monthly_stipend_amount": "Total funding package: €10,000 per academic year living stipend (€5,000 per semester / approx. €1,000 / month / ~PKR 300,000 / month) plus guaranteed subsidized student housing in a university hall of residence (worth €400-€550/month) and tuition waiver across all master's semesters"
        },
        "eligibility_requirements": {
            "nationality_requirements": ["Open to non-EU/EEA international students and EU students (Pakistan fully eligible)"],
            "pakistan_eligible": True,
            "age_limit_undergrad": 0,
            "age_limit_postgrad": 40,
            "age_limit_notes": "No statutory maximum age limit, though priority is given to candidates with high academic momentum.",
            "academic_qualifications": "Completed recognized 16-year Bachelor's degree (or equivalent) with outstanding academic performance (minimum CGPA 3.50/4.00 or top 10% class ranking) from an HEC-recognized university.",
            "minimum_gpa_percentage": 82.0,
            "minimum_gpa_scale": 3.5,
            "grading_conversion_notes": "Minimum CGPA 3.50 / 4.00; competitive applicants typically hold CGPA >= 3.70 / 4.00.",
            "subject_background_prerequisites": "Computer science, cybersecurity, information security, data science, financial economics, quantitative finance, mathematics, physics, or mechanical/civil engineering.",
            "current_education_status": "Graduated or final-year undergraduate students completing degree requirements before September semester start.",
            "graduation_year_restrictions": "None.",
            "work_experience_required": False,
            "work_experience_minimum_years": 0.0,
            "work_experience_notes": "Internships or technical experience in software development, cybersecurity, financial technology, or data analysis are advantageous.",
            "english_test_required": True,
            "ielts_minimum": 6.5,
            "toefl_minimum": 90,
            "duolingo_accepted": False,
            "moi_certificate_accepted": True,
            "language_notes": "IELTS Academic minimum 6.5 (6.0 in all sub-scores), TOEFL iBT minimum 90, Cambridge Advanced (C1), or official English Medium of Instruction (MOI) certificate from an accredited degree-granting institution.",
            "other_language_requirements": "French or German proficiency is required only for bilingual master's programs; English-track degrees require English proficiency only.",
            "gender_specific_requirements": "Open equally to all qualified applicants.",
            "financial_need_required": False,
            "special_eligibility_categories": "Candidates apply directly to an eligible Master's programme at the University of Luxembourg and submit the Guillaume Dupaix scholarship application dossier.",
            "previous_scholarship_restrictions": "Cannot hold another parallel government fellowship covering identical living and tuition costs.",
            "can_apply_result_awaiting": True
        },
        "financial_coverage_breakdown": {
            "tuition_fee": {
                "status": "COVERED",
                "details": "100% full tuition fee covered or waived (University of Luxembourg tuition fees are standardly €200 to €400/semester, fully covered).",
                "amount": "100% covered tuition fees"
            },
            "admission_application_fee": {
                "status": "NOT_COVERED",
                "details": "University of Luxembourg application processing fee of €50 paid online during portal submission.",
                "amount": "€50 (~PKR 15,000)"
            },
            "accommodation": {
                "status": "COVERED",
                "details": "Guaranteed university hall of residence room reserved for the scholar, with rental costs (€400 to €550 / month) directly covered or subsidized from the fellowship allowance.",
                "amount": "Guaranteed campus student residence housing"
            },
            "monthly_stipend": {
                "status": "COVERED",
                "details": "Living stipend of €10,000 per academic year (€5,000 disbursed per semester / approx. €1,000 / month / ~PKR 300,000 / month) disbursed directly for personal living expenses.",
                "amount": "€10,000 / year (~PKR 3,000,000 / year)"
            },
            "airfare": {
                "status": "NOT_COVERED",
                "details": "International travel between Pakistan and Luxembourg Findel Airport is self-funded.",
                "amount": "Borne by candidate"
            },
            "visa_fee": {
                "status": "NOT_COVERED",
                "details": "Luxembourg Temporary Authorisation to Stay (AST) and Visa D application fees (€50) paid to Luxembourg Immigration Directorate.",
                "amount": "€50 borne by candidate"
            },
            "health_insurance": {
                "status": "COVERED",
                "details": "Full statutory enrollment in the Luxembourg National Health Fund (Caisse Nationale de Santé - CNS) covering comprehensive medical, hospital, and dental care.",
                "amount": "100% covered Luxembourg CNS public healthcare"
            },
            "food_allowance": {
                "status": "SUBSIDIZED",
                "details": "Subsidized university restaurants (Restopolis) across Belval and Kirchberg campuses; student meals cost €3.50 to €5.50.",
                "amount": "Subsidized campus dining"
            },
            "books_and_materials_allowance": {
                "status": "COVERED",
                "details": "Full access to the Luxembourg Learning Centre (LLC), MeluXina national supercomputer, Interdisciplinary Centre for Security, Reliability and Trust (SnT), and digital research databases.",
                "amount": "100% covered supercomputer & library infrastructure"
            },
            "research_funding_conference_grant": {
                "status": "COVERED",
                "details": "Generous paid master's thesis research opportunities and industrial partnerships with major European banks, Amazon Europe HQ, and Skype in Luxembourg.",
                "amount": "High-paying industry internships & thesis stipends"
            },
            "travel_transit_allowance": {
                "status": "COVERED",
                "details": "100% FREE nationwide public transit: All trains, trams, and buses throughout the entire country of Luxembourg are completely free for everyone.",
                "amount": "100% free nationwide public transportation"
            },
            "total_estimated_value_usd_per_year": 22000
        },
        "university_and_program_options": {
            "single_or_multiple_universities": "Single elite research institution in the heart of the European Union (University of Luxembourg).",
            "participating_institutions": [
                "University of Luxembourg (Belval Campus in Esch-sur-Alzette, Kirchberg Campus in Luxembourg City, Luxembourg)"
            ],
            "university_rankings_scope": "Times Higher Education (THE) World University Rankings Top 250 globally, Ranked #4 in the world for International Outlook (THE 2024); renowned for cybersecurity, fintech, space resources, and multilingual European law.",
            "available_majors": [
                "Master in Information and Computer Sciences (MICS)",
                "Master in Information Security and Cybersecurity (MISC)",
                "Master in Data Science",
                "Master in High-Performance Computing (HPC)",
                "Master of Science in Civil Engineering - Megastructure Engineering",
                "Master in Quantitative Economics and Finance",
                "Master in Space Technologies and Business",
                "Master in Mathematics"
            ],
            "english_taught_program_availability": True,
            "program_duration": "2 years (Master of Science)",
            "admission_requirements_summary": "Bachelor's degree with CGPA >= 3.50/4.00, academic transcripts, detailed motivation letter, two academic letters of recommendation, CV, and English proficiency certificate (IELTS 6.5+ / TOEFL 90+ / MOI).",
            "is_admission_separate_from_scholarship": False,
            "pre_admission_acceptance_letter_required": False,
            "easiest_hardest_institutions_guidance": "Master in Information Security and Cybersecurity (MISC) and Master in High-Performance Computing (partnered with MeluXina supercomputer) are exceptionally selective; candidates with strong algorithms and systems backgrounds stand the highest chance.",
            "strategic_program_match_advice": "Highlight technical competencies aligned with Luxembourg's national research priorities: European cybersecurity, fintech analytics, High-Performance Computing, or space resource exploration."
        },
        "application_process_roadmap": {
            "submission_portal_url": "https://www.uni.lu/en/admissions/funding-and-scholarships/guillaume-dupaix-scholarship/",
            "portal_system_name": "University of Luxembourg Admissions Portal",
            "account_creation_instructions": "Register on the University of Luxembourg admissions portal, complete online application for eligible master's program, select Guillaume Dupaix scholarship, upload statement of purpose, CV, transcripts, and submit by the strict international deadline.",
            "step_by_step_workflow": [
                "Step 1: Check program requirements on uni.lu and verify eligibility for Guillaume Dupaix award.",
                "Step 2: Create account on University of Luxembourg admissions portal (open February 1).",
                "Step 3: Complete online admission application and upload Guillaume Dupaix scholarship motivation essay.",
                "Step 4: Upload attested transcripts, degree certificates, CV, and English proficiency proof.",
                "Step 5: Pay €50 application evaluation fee.",
                "Step 6: Master's programme admission committee evaluates applications and nominates top candidates.",
                "Step 7: University Scholarship Selection Committee reviews nominations and confirms awardees.",
                "Step 8: Official admission and Guillaume Dupaix scholarship offer issued in May.",
                "Step 9: Apply for Luxembourg Temporary Authorisation to Stay (AST), obtain Visa D, and arrive in Luxembourg in early September."
            ],
            "university_vs_scholarship_routing": "Integrated University Route: Application for master's admission and Guillaume Dupaix award are submitted together via the central admissions portal.",
            "recommendation_letters_submission_method": "Uploaded directly by candidate as signed official PDF letters on institutional letterhead with referee contact details.",
            "personal_statement_prompts": "Guillaume Dupaix Motivation Statement (1-2 pages) explaining academic excellence, research ambitions, reason for choosing the University of Luxembourg, and long-term career goals.",
            "study_plan_research_proposal_requirements": "Statement of academic focus outlining proposed specialization track and master's thesis interest.",
            "cv_format_requirements": "Comprehensive academic CV detailing education, project portfolio, programming skills, and extracurricular leadership.",
            "interviews_conducted": True,
            "interview_format_details": "Online technical video interview via MS Teams or Webex conducted by programme course director for shortlisted candidates.",
            "standardized_tests": "IELTS Academic 6.5+, TOEFL iBT 90+, or official English Medium of Instruction (MOI) certificate accepted.",
            "application_fee_amount": "€50 (approx. PKR 15,000)",
            "attestation_requirements": "Certified true copies of transcripts and degree certificates; HEC and MoFA attestations required for Pakistani credentials.",
            "translation_requirements": "Certified official English, French, or German translation for all non-English documents.",
            "final_submission_method": "Online submission via University of Luxembourg admissions portal."
        },
        "required_documents_checklist": [
            {
                "document_name": "Official Academic Transcripts and Degree Certificate",
                "mandatory": True,
                "specification": "Complete Bachelor's degree certificate and transcripts with grading scale and CGPA >= 3.50/4.00.",
                "pakistan_specific_instruction": "Attested by HEC Pakistan."
            },
            {
                "document_name": "Guillaume Dupaix Scholarship Motivation Statement",
                "mandatory": True,
                "specification": "Detailed essay (1-2 pages) demonstrating academic excellence, intellectual curiosity, and career roadmap.",
                "pakistan_specific_instruction": "Structured essay formatted in English."
            },
            {
                "document_name": "Two Academic Reference Letters",
                "mandatory": True,
                "specification": "Confidential evaluation letters from university professors on institutional letterhead.",
                "pakistan_specific_instruction": "Signed and stamped with official university seals."
            },
            {
                "document_name": "English Language Proficiency Certificate",
                "mandatory": True,
                "specification": "IELTS Academic 6.5+ (6.0 in all sub-scores), TOEFL iBT 90+, or official MOI certificate.",
                "pakistan_specific_instruction": "Official test report or MOI letter."
            },
            {
                "document_name": "Curriculum Vitae (CV)",
                "mandatory": True,
                "specification": "Comprehensive academic CV detailing education, projects, software proficiencies, and honors.",
                "pakistan_specific_instruction": "European standard format."
            },
            {
                "document_name": "Passport Identification Page Scan",
                "mandatory": True,
                "specification": "Clear color copy of passport bio-data page valid for at least 18 months.",
                "pakistan_specific_instruction": "Valid passport."
            }
        ],
        "important_dates_timeline": {
            "application_open_date": "February 1",
            "application_deadline": "March 29 (Strict international non-EU scholarship deadline)",
            "university_admission_deadline": "March 29",
            "document_submission_deadline": "March 29",
            "recommendation_letters_deadline": "April 5",
            "interview_period": "April - May",
            "shortlist_announcement": "Mid May",
            "final_result_acceptance_deadline": "Within 2 weeks of notification",
            "visa_application_window": "June - July",
            "semester_commencement": "Mid September (Winter semester)",
            "annual_cycle_notes": "Single annual admission cycle for autumn entry; application window open February 1 to late March for non-EU international applicants."
        },
        "selection_process_and_weights": {
            "academic_weight": "45% (Undergraduate GPA, academic consistency in major subjects, course rigor)",
            "extracurricular_and_leadership_weight": "10% (Initiative, international adaptability, teamwork)",
            "research_experience_weight": "25% (Technical project depth, software portfolio, and undergraduate thesis quality)",
            "work_experience_weight": "5% (Relevant industry internships or software development roles)",
            "personal_statement_weight": "10% (Quality, eloquence, and intellectual clarity of motivation statement)",
            "recommendations_weight": "5% (Academic referee evaluation)",
            "interview_weight": "0% (Interview performance confirms technical ranking)",
            "test_scores_weight": "0% (English proficiency is a qualifying prerequisite)",
            "financial_need_weight": "0% (Pure academic excellence and intellectual merit based)",
            "selection_panel_composition": "Faculty Master's Admissions Board and University of Luxembourg Scholarship Committee.",
            "evaluation_methodology": "Two-tier holistic evaluation selecting top 1-2% of global master's applicants displaying exceptional potential."
        },
        "competitiveness_profile": {
            "total_annual_applicants": "~1,800 to 2,500 international applicants across Master's programs",
            "total_scholarships_awarded": "~30 to 45 Guillaume Dupaix awards annually",
            "acceptance_rate_global": "~1.5% to 2.0%",
            "acceptance_rate_pakistan": "~2.5% to 4.0% for candidates with superior academic records and CGPA >= 3.70",
            "typical_successful_applicant_gpa": "Undergraduate CGPA >= 3.70 / 4.00, accompanied by strong programming projects or thesis research",
            "typical_academic_and_research_profile": "Graduates in computer science, software engineering, mathematics, or quantitative finance with stellar academic records and clear specialization intent.",
            "common_backgrounds_of_winners": "Graduates from top Pakistani universities (FAST-NUCES, NUST, LUMS, UET Lahore, GIKI, Quaid-i-Azam).",
            "high_representation_countries": "Pakistan, India, Italy, France, China, Germany, Ukraine, Brazil, Turkey.",
            "competitiveness_tier": "MOST_COMPETITIVE"
        },
        "red_flags_and_warnings": {
            "fake_websites_and_scams": [
                "Only apply through official portal uni.lu.",
                "University of Luxembourg never charges additional placement fees or works with unauthorized commercial agents."
            ],
            "application_fee_warning": "Application fee of €50 is paid directly through the secure university online portal.",
            "agent_and_intermediary_warnings": "Commercial agency written statements are disqualified; personal authenticity is evaluated during course director interviews.",
            "hidden_costs_breakdown": [
                "Application fee: €50 (~PKR 15,000).",
                "Luxembourg Visa D / AST fee: €50 (~PKR 15,000).",
                "HEC document attestation in Pakistan: ~PKR 15,000.",
                "One-way flight to Luxembourg: ~PKR 150,000 to 220,000.",
                "Initial pocket money before first stipend disbursement: ~€500 (~PKR 150,000)."
            ],
            "misleading_claims_debunked": [
                "Myth: You need French or Luxembourgish fluency. Reality: All STEM and computing master's programs are 100% in English.",
                "Myth: Housing in Luxembourg is impossible to find. Reality: Guillaume Dupaix scholars are guaranteed university student residence housing."
            ],
            "official_vs_unofficial_discrepancies": [
                "Unofficial sites claim public transport is expensive in Luxembourg; in reality, public transportation is 100% free nationwide by law."
            ]
        },
        "scholarship_obligations_and_terms": {
            "minimum_gpa_maintenance": "Maintain satisfactory academic progress and complete at least 60 ECTS credits in Year 1 to renew the award for Year 2.",
            "attendance_requirements": "Full-time physical presence on campus in Luxembourg; residence in reserved university student housing.",
            "academic_progress_monitoring": "Annual progress review evaluated by Master's study director at the end of the second semester.",
            "work_restrictions_during_study": "Part-time student work permitted under Luxembourg immigration law (up to 15 hours/week during term, 40 hours/week during holidays).",
            "home_country_return_obligation": "None; zero service bond or return obligation (graduates are entitled to a Luxembourg post-study work authorization).",
            "service_obligations_or_bonds": "Zero service bond.",
            "repayment_clawback_conditions": "Scholarship is terminated if candidate fails to meet academic milestones, abandons studies, or violates student code of conduct.",
            "rules_for_changing_university": "Non-transferable to other universities.",
            "rules_for_changing_major": "Changing major requires formal re-application.",
            "extension_policy": "Fellowship is strictly limited to 2 academic years (4 semesters); extensions beyond 2 years are not funded."
        },
        "official_sources_verified": [
            {
                "source_name": "University of Luxembourg Guillaume Dupaix Scholarship Guide",
                "source_url": "https://www.uni.lu/en/admissions/funding-and-scholarships/guillaume-dupaix-scholarship/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            },
            {
                "source_name": "University of Luxembourg Master's Admissions Portal",
                "source_url": "https://www.uni.lu/en/admissions/masters-studies/",
                "source_type": "OFFICIAL_UNIVERSITY",
                "verified_date": "2026-10-07",
                "data_points_missing_or_unpublished_by_source": []
            }
        ]
    }
}
