from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class FundingType(str, Enum):
    FULL = "FULL"
    TUITION_ONLY = "TUITION_ONLY"
    PARTIAL = "PARTIAL"
    STIPEND_ONLY = "STIPEND_ONLY"


class ScholarshipStatus(str, Enum):
    DISCOVERED = "DISCOVERED"
    VERIFIED = "VERIFIED"
    PARTIALLY_VERIFIED = "PARTIALLY_VERIFIED"
    HEC_LISTED = "HEC_LISTED"
    SKEPTIC_CHALLENGED = "SKEPTIC_CHALLENGED"
    REJECTED = "REJECTED"


class FundingDetails(BaseModel):
    funding_type: FundingType = Field(default=FundingType.FULL)
    tuition: str = Field(default="100% Waived", description="Tuition fee coverage")
    accommodation: str = Field(default="Free Dormitory or Allowance", description="Housing details")
    monthly_stipend: Optional[str] = Field(default=None, description="Stipend in host currency")
    monthly_stipend_pkr_approx: Optional[int] = Field(default=None, description="Estimated monthly stipend in PKR")
    travel_airfare: str = Field(default="NOT_COVERED", description="COVERED, NOT_COVERED, REIMBURSED")
    health_insurance: str = Field(default="COVERED", description="Medical coverage details")
    settlement_allowance: Optional[str] = Field(default=None, description="One-off arrival allowance")


class PakistanSpecificRequirements(BaseModel):
    pakistan_eligible: bool = Field(default=True, description="Explicitly open to Pakistani nationals")
    pakistan_bilateral_quota: bool = Field(default=False, description="Government-to-government quota allocated")
    pakistan_quota_seats: Optional[int] = Field(default=None, description="Number of reserved seats (e.g. 400 for Hungary)")
    hec_managed: bool = Field(default=False, description="Application routed via HEC Pakistan portal")
    hec_portal_url: Optional[str] = Field(default=None, description="HEC scholarship registration portal link")
    hec_hat_required: bool = Field(default=False, description="HEC HAT test required for postgrad")
    hec_usat_required: bool = Field(default=False, description="HEC USAT test required for undergrad")
    hec_attestation_required: bool = Field(default=True, description="HEC attested degrees needed at submission")
    ibcc_equivalence_required: bool = Field(default=False, description="IBCC equivalence certificate required")
    mofa_attestation_required: bool = Field(default=False, description="Ministry of Foreign Affairs attestation required")
    accepts_moi_certificate: bool = Field(default=False, description="Accepts English Medium of Instruction in lieu of IELTS")


class LanguageRequirement(BaseModel):
    english_test_required: bool = Field(default=True)
    minimum_ielts: Optional[float] = Field(default=None, ge=0.0, le=9.0)
    minimum_toefl: Optional[int] = Field(default=None, ge=0, le=677)
    minimum_duolingo: Optional[int] = Field(default=None, ge=0, le=160)
    host_language_prep: bool = Field(default=False, description="Provides 1-year language preparatory course")
    notes: Optional[str] = None


class EligibilityCriteria(BaseModel):
    degree_levels: List[str] = Field(default_factory=lambda: ["Bachelor's", "Master's", "PhD"])
    eligible_fields: List[str] = Field(default_factory=list)
    min_gpa_percentage: Optional[float] = Field(default=None, description="Minimum percentage required")
    min_gpa_4_scale: Optional[float] = Field(default=None, description="Minimum GPA on 4.0 scale")
    age_limit_undergrad: Optional[int] = Field(default=None)
    age_limit_postgrad: Optional[int] = Field(default=None)
    min_years_education: int = Field(default=12, description="12 for Bachelor's, 16 for Master's, 18 for PhD")
    eligible_nationalities: List[str] = Field(default_factory=lambda: ["Pakistan", "PK"])
    work_experience_years_required: int = Field(default=0)


class Scholarship(BaseModel):
    scholarship_id: str = Field(..., description="Unique identifier (e.g. SCH-EU-001)")
    name: str = Field(..., description="Official scholarship name")
    host_country: str = Field(..., description="ISO 2-letter country code")
    host_country_name: str = Field(..., description="Country name (e.g. Hungary, China, Germany)")
    host_institution: Optional[str] = Field(default=None, description="University or Consortium name")
    region: str = Field(..., description="Europe, Asia, Americas, MENA, Oceania")
    source_url: str = Field(..., description="Official application or information URL")
    portal_url: Optional[str] = Field(default=None, description="Direct portal submission link")
    discovered_by: str = Field(default="seed_database", description="Scout name, live_search, or seed_database")
    
    funding: FundingDetails = Field(default_factory=FundingDetails)
    pakistan_requirements: PakistanSpecificRequirements = Field(default_factory=PakistanSpecificRequirements)
    language: LanguageRequirement = Field(default_factory=LanguageRequirement)
    eligibility: EligibilityCriteria = Field(default_factory=EligibilityCriteria)
    
    application_opens: Optional[str] = Field(default=None, description="YYYY-MM-DD")
    application_deadline: Optional[str] = Field(default=None, description="YYYY-MM-DD")
    is_recurring_annual: bool = Field(default=True, description="Whether this scholarship repeats in annual intake cycles")
    estimated_decision_date: Optional[str] = Field(default=None, description="YYYY-MM-DD")
    academic_intake: Optional[str] = Field(default="Fall 2026", description="Intake session")
    
    description: Optional[str] = None
    selection_process: Optional[str] = None
    competition_level: Optional[str] = Field(default="MODERATE", description="LOW, MODERATE, HIGH, EXTREME")
    success_rate_pakistan_percent: Optional[float] = Field(default=None, description="Estimated acceptance rate for Pakistanis")
    
    confidence_score: float = Field(default=0.9, ge=0.0, le=1.0)
    status: ScholarshipStatus = Field(default=ScholarshipStatus.DISCOVERED)
    deep_dossier: Optional["DeepScholarshipDossier"] = Field(default=None, description="Exhaustive 11-dimension verified scholarship intelligence dossier")
    final_score: Optional[float] = Field(default=None, description="Calculated overall match score")
    rank: Optional[int] = Field(default=None, description="Ranking index in mission")
    eligibility_analysis: Optional[Dict[str, Any]] = Field(default=None, description="Detailed eligibility assessment")
    cost_analysis: Optional[Dict[str, Any]] = Field(default=None, description="Detailed cost and financial analysis")
    deadline_analysis: Optional[Dict[str, Any]] = Field(default=None, description="Detailed deadline analysis")


# ==============================================================================
# 11-DIMENSION DEEP SCHOLARSHIP INTELLIGENCE SCHEMAS
# ==============================================================================

class BasicDetailsDossier(BaseModel):
    scholarship_name: str
    offering_entity: str
    host_country: str
    host_institutions_covered: str
    degree_levels: List[str] = Field(default_factory=list)
    major_restrictions: str
    number_of_awards_total: str
    number_of_awards_pakistan: str
    funding_classification: str = Field(description="FULLY_FUNDED, PARTIALLY_FUNDED, TUITION_ONLY")
    duration_of_scholarship: str


class DetailedEligibilityDossier(BaseModel):
    nationality_requirements: List[str] = Field(default_factory=list)
    pakistan_eligible: bool = True
    age_limit_undergrad: Optional[int] = None
    age_limit_postgrad: Optional[int] = None
    age_limit_notes: Optional[str] = None
    academic_qualifications: str
    minimum_gpa_percentage: Optional[float] = None
    minimum_gpa_scale: Optional[float] = None
    grading_conversion_notes: Optional[str] = None
    subject_background_prerequisites: str
    current_education_status: str
    graduation_year_restrictions: Optional[str] = None
    work_experience_required: bool = False
    work_experience_minimum_years: float = 0.0
    work_experience_notes: Optional[str] = None
    english_test_required: bool = True
    ielts_minimum: Optional[float] = None
    toefl_minimum: Optional[int] = None
    duolingo_accepted: bool = False
    moi_certificate_accepted: bool = False
    language_notes: Optional[str] = None
    other_language_requirements: Optional[str] = None
    gender_specific_requirements: Optional[str] = None
    financial_need_required: bool = False
    special_eligibility_categories: Optional[str] = None
    previous_scholarship_restrictions: Optional[str] = None
    can_apply_result_awaiting: bool = False


class FinancialBenefitItem(BaseModel):
    status: str = Field(description="COVERED, PARTIAL, NOT_COVERED, WAIVED, REIMBURSED")
    details: str
    amount: Optional[str] = None


class FinancialCoverageBreakdown(BaseModel):
    tuition_fee: FinancialBenefitItem
    admission_application_fee: FinancialBenefitItem
    accommodation: FinancialBenefitItem
    monthly_stipend: FinancialBenefitItem
    airfare: FinancialBenefitItem
    visa_fee: FinancialBenefitItem
    health_insurance: FinancialBenefitItem
    food_allowance: FinancialBenefitItem
    books_and_materials_allowance: FinancialBenefitItem
    research_funding_conference_grant: FinancialBenefitItem
    travel_transit_allowance: FinancialBenefitItem
    total_estimated_value_usd_per_year: Optional[int] = None


class UniversityProgramOptions(BaseModel):
    single_or_multiple_universities: str
    participating_institutions: List[str] = Field(default_factory=list)
    university_rankings_scope: str
    available_majors: List[str] = Field(default_factory=list)
    english_taught_program_availability: bool = True
    program_duration: str
    admission_requirements_summary: str
    is_admission_separate_from_scholarship: bool
    pre_admission_acceptance_letter_required: bool
    easiest_hardest_institutions_guidance: str
    strategic_program_match_advice: str


class ApplicationProcessRoadmap(BaseModel):
    submission_portal_url: str
    portal_system_name: str
    account_creation_instructions: str
    step_by_step_workflow: List[str] = Field(default_factory=list)
    university_vs_scholarship_routing: str
    recommendation_letters_submission_method: str
    personal_statement_prompts: str
    study_plan_research_proposal_requirements: str
    cv_format_requirements: str
    interviews_conducted: bool
    interview_format_details: Optional[str] = None
    standardized_tests: str
    application_fee_amount: str
    attestation_requirements: str
    translation_requirements: str
    final_submission_method: str


class DocumentChecklistItem(BaseModel):
    document_name: str
    mandatory: bool = True
    specification: str
    pakistan_specific_instruction: str


class ImportantDatesTimeline(BaseModel):
    application_open_date: str
    application_deadline: str
    university_admission_deadline: Optional[str] = None
    document_submission_deadline: Optional[str] = None
    recommendation_letters_deadline: Optional[str] = None
    interview_period: Optional[str] = None
    shortlist_announcement: Optional[str] = None
    final_result_acceptance_deadline: Optional[str] = None
    visa_application_window: Optional[str] = None
    semester_commencement: Optional[str] = None
    annual_cycle_notes: str


class SelectionProcessWeights(BaseModel):
    academic_weight: str
    extracurricular_and_leadership_weight: str
    research_experience_weight: str
    work_experience_weight: str
    personal_statement_weight: str
    recommendations_weight: str
    interview_weight: str
    test_scores_weight: str
    financial_need_weight: str
    selection_panel_composition: str
    evaluation_methodology: str


class CompetitivenessProfile(BaseModel):
    total_annual_applicants: str
    total_scholarships_awarded: str
    acceptance_rate_global: str
    acceptance_rate_pakistan: str
    typical_successful_applicant_gpa: str
    typical_academic_and_research_profile: str
    common_backgrounds_of_winners: str
    high_representation_countries: str
    competitiveness_tier: str = Field(description="EXTREME, VERY_HIGH, HIGH, MODERATE")


class RedFlagsAndWarnings(BaseModel):
    fake_websites_and_scams: List[str] = Field(default_factory=list)
    application_fee_warning: str
    agent_and_intermediary_warnings: str
    hidden_costs_breakdown: List[str] = Field(default_factory=list)
    misleading_claims_debunked: List[str] = Field(default_factory=list)
    official_vs_unofficial_discrepancies: List[str] = Field(default_factory=list)


class ScholarshipObligations(BaseModel):
    minimum_gpa_maintenance: str
    attendance_requirements: str
    academic_progress_monitoring: str
    work_restrictions_during_study: str
    home_country_return_obligation: str
    service_obligations_or_bonds: str
    repayment_clawback_conditions: str
    rules_for_changing_university: str
    rules_for_changing_major: str
    extension_policy: str


class VerifiedOfficialSource(BaseModel):
    source_name: str
    source_url: str
    source_type: str = Field(description="OFFICIAL_GOVERNMENT, OFFICIAL_UNIVERSITY, OFFICIAL_COMMISSION, OFFICIAL_BILATERAL")
    verified_date: str
    data_points_missing_or_unpublished_by_source: List[str] = Field(default_factory=list)


class DeepScholarshipDossier(BaseModel):
    scholarship_id: str
    basic_details: BasicDetailsDossier
    eligibility_requirements: DetailedEligibilityDossier
    financial_coverage_breakdown: FinancialCoverageBreakdown
    university_and_program_options: UniversityProgramOptions
    application_process_roadmap: ApplicationProcessRoadmap
    required_documents_checklist: List[DocumentChecklistItem]
    important_dates_timeline: ImportantDatesTimeline
    selection_process_and_weights: SelectionProcessWeights
    competitiveness_profile: CompetitivenessProfile
    red_flags_and_warnings: RedFlagsAndWarnings
    scholarship_obligations_and_terms: ScholarshipObligations
    official_sources_verified: List[VerifiedOfficialSource]


Scholarship.model_rebuild()


