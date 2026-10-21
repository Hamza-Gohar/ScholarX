// Complete TypeScript definitions matching backend Pydantic schemas

export type Region = "Europe" | "Asia" | "Americas" | "MENA" | "Oceania";

export interface AcademicRecord {
  degree_level: string;
  current_level?: string;
  field_of_study: string;
  institution: string;
  grading_system: string;
  education_system?: "PAKISTANI_HSSC" | "CAMBRIDGE" | "AMERICAN_DIPLOMA" | "IB" | string;
  a_level_grades?: string[];
  o_level_grades?: string[];
  ibcc_equivalence_percentage?: number | null;
  ibcc_total_marks?: number | null;
  gpa_obtained?: number | null;
  gpa_4_scale?: number | null;
  gpa_total?: number | null;
  percentage?: number | null;
  gpa_percentage?: number | null;
  graduation_year: number;
}

export interface LanguageProficiency {
  test_type: "IELTS" | "TOEFL" | "DUOLINGO" | "PTE" | "NONE" | string;
  english_proficiency_test?: string;
  overall_score?: number | null;
  ielts_overall?: number | null;
  reading?: number | null;
  writing?: number | null;
  listening?: number | null;
  speaking?: number | null;
  has_english_medium_certificate?: boolean | null;
  moi_certificate_available?: boolean | null;
}

export interface FinancialProfile {
  max_annual_contribution_pkr: number;
  max_out_of_pocket_pkr: number;
  funding_requirement: "FULL" | "PARTIAL" | "ANY" | string;
}

export interface StudentProfile {
  student_id: string;
  session_id?: string | null;
  personal: {
    name: string;
    nationality: string;
    city?: string;
    current_city: string;
    target_intake: string;
    intended_degree: string;
    target_fields: string[];
    target_regions: Region[];
  };
  academic: AcademicRecord;
  language: LanguageProficiency;
  financial: FinancialProfile;
  preferences?: {
    target_degree_level: string;
    target_fields: string[];
    preferred_regions: Region[];
    max_out_of_pocket_pkr: number;
    funding_requirement: string;
    is_tax_filer?: boolean;
  };
  profile_completeness: number;
}

export interface FundingDetails {
  funding_type: "FULL" | "TUITION_ONLY" | "PARTIAL" | "STIPEND_ONLY" | string;
  tuition: string;
  accommodation: string;
  monthly_stipend?: string | null;
  monthly_stipend_pkr_approx?: number | null;
  travel_airfare: string;
  health_insurance: string;
  settlement_allowance?: string | null;
}

export interface PakistanSpecificRequirements {
  pakistan_eligible: boolean;
  pakistan_bilateral_quota: boolean;
  pakistan_quota_seats?: number | null;
  hec_managed: boolean;
  hec_portal_url?: string | null;
  hec_hat_required: boolean;
  hec_usat_required: boolean;
  hec_attestation_required: boolean;
  ibcc_equivalence_required: boolean;
  mofa_attestation_required: boolean;
  accepts_moi_certificate: boolean;
}

export interface LanguageRequirement {
  english_test_required: boolean;
  minimum_ielts?: number | null;
  minimum_toefl?: number | null;
  minimum_duolingo?: number | null;
  host_language_prep: boolean;
  notes?: string | null;
}

export interface EligibilityCriteria {
  degree_levels: string[];
  eligible_fields: string[];
  min_gpa_percentage?: number | null;
  min_gpa_4_scale?: number | null;
  age_limit_undergrad?: number | null;
  age_limit_postgrad?: number | null;
  min_years_education: number;
  eligible_nationalities: string[];
  work_experience_years_required: number;
}

export interface Scholarship {
  scholarship_id: string;
  name: string;
  host_country: string;
  host_country_name: string;
  host_institution?: string | null;
  region: Region;
  source_url: string;
  portal_url?: string | null;
  discovered_by: string;
  funding: FundingDetails;
  pakistan_requirements: PakistanSpecificRequirements;
  language: LanguageRequirement;
  eligibility: EligibilityCriteria;
  application_opens?: string | null;
  application_deadline?: string | null;
  estimated_decision_date?: string | null;
  academic_intake?: string | null;
  description?: string | null;
  selection_process?: string | null;
  competition_level: "LOW" | "MODERATE" | "HIGH" | "EXTREME" | string;
  success_rate_pakistan_percent?: number | null;
  confidence_score: number;
  status: "DISCOVERED" | "VERIFIED" | "PARTIALLY_VERIFIED" | "HEC_LISTED" | "SKEPTIC_CHALLENGED" | "REJECTED" | string;
  polite_rejection_notice?: string | null;
  need_based_alternatives?: string[];
  deep_dossier?: DeepScholarshipDossier | null;
}

export interface BasicDetailsDossier {
  scholarship_name: string;
  offering_entity: string;
  host_country: string;
  host_institutions_covered: string;
  degree_levels: string[];
  major_restrictions: string;
  number_of_awards_total: string;
  number_of_awards_pakistan: string;
  funding_classification: "FULLY_FUNDED" | "PARTIALLY_FUNDED" | "TUITION_ONLY" | string;
  duration_of_scholarship: string;
}

export interface DetailedEligibilityDossier {
  nationality_requirements: string[];
  pakistan_eligible: boolean;
  age_limit_undergrad?: number | null;
  age_limit_postgrad?: number | null;
  age_limit_notes?: string | null;
  academic_qualifications: string;
  minimum_gpa_percentage?: number | null;
  minimum_gpa_scale?: number | null;
  grading_conversion_notes?: string | null;
  subject_background_prerequisites: string;
  current_education_status: string;
  graduation_year_restrictions?: string | null;
  work_experience_required: boolean;
  work_experience_minimum_years: number;
  work_experience_notes?: string | null;
  english_test_required: boolean;
  ielts_minimum?: number | null;
  toefl_minimum?: number | null;
  duolingo_accepted: boolean;
  moi_certificate_accepted: boolean;
  language_notes?: string | null;
  other_language_requirements?: string | null;
  gender_specific_requirements?: string | null;
  financial_need_required: boolean;
  special_eligibility_categories?: string | null;
  previous_scholarship_restrictions?: string | null;
  can_apply_result_awaiting: boolean;
}

export interface FinancialBenefitItem {
  status: "COVERED" | "PARTIAL" | "NOT_COVERED" | "WAIVED" | "REIMBURSED" | string;
  details: string;
  amount?: string | null;
}

export interface FinancialCoverageBreakdown {
  tuition_fee: FinancialBenefitItem;
  admission_application_fee: FinancialBenefitItem;
  accommodation: FinancialBenefitItem;
  monthly_stipend: FinancialBenefitItem;
  airfare: FinancialBenefitItem;
  visa_fee: FinancialBenefitItem;
  health_insurance: FinancialBenefitItem;
  food_allowance: FinancialBenefitItem;
  books_and_materials_allowance: FinancialBenefitItem;
  research_funding_conference_grant: FinancialBenefitItem;
  travel_transit_allowance: FinancialBenefitItem;
  total_estimated_value_usd_per_year?: number | null;
}

export interface UniversityProgramOptions {
  single_or_multiple_universities: string;
  participating_institutions: string[];
  university_rankings_scope: string;
  available_majors: string[];
  english_taught_program_availability: boolean;
  program_duration: string;
  admission_requirements_summary: string;
  is_admission_separate_from_scholarship: boolean;
  pre_admission_acceptance_letter_required: boolean;
  easiest_hardest_institutions_guidance: string;
  strategic_program_match_advice: string;
}

export interface ApplicationProcessRoadmap {
  submission_portal_url: string;
  portal_system_name: string;
  account_creation_instructions: string;
  step_by_step_workflow: string[];
  university_vs_scholarship_routing: string;
  recommendation_letters_submission_method: string;
  personal_statement_prompts: string;
  study_plan_research_proposal_requirements: string;
  cv_format_requirements: string;
  interviews_conducted: boolean;
  interview_format_details?: string | null;
  standardized_tests: string;
  application_fee_amount: string;
  attestation_requirements: string;
  translation_requirements: string;
  final_submission_method: string;
}

export interface DocumentChecklistItem {
  document_name: string;
  mandatory: boolean;
  specification: string;
  pakistan_specific_instruction: string;
}

export interface ImportantDatesTimeline {
  application_open_date: string;
  application_deadline: string;
  university_admission_deadline?: string | null;
  document_submission_deadline?: string | null;
  recommendation_letters_deadline?: string | null;
  interview_period?: string | null;
  shortlist_announcement?: string | null;
  final_result_acceptance_deadline?: string | null;
  visa_application_window?: string | null;
  semester_commencement?: string | null;
  annual_cycle_notes: string;
}

export interface SelectionProcessWeights {
  academic_weight: string;
  extracurricular_and_leadership_weight: string;
  research_experience_weight: string;
  work_experience_weight: string;
  personal_statement_weight: string;
  recommendations_weight: string;
  interview_weight: string;
  test_scores_weight: string;
  financial_need_weight: string;
  selection_panel_composition: string;
  evaluation_methodology: string;
}

export interface CompetitivenessProfile {
  total_annual_applicants: string;
  total_scholarships_awarded: string;
  acceptance_rate_global: string;
  acceptance_rate_pakistan: string;
  typical_successful_applicant_gpa: string;
  typical_academic_and_research_profile: string;
  common_backgrounds_of_winners: string;
  high_representation_countries: string;
  competitiveness_tier: "EXTREME" | "VERY_HIGH" | "HIGH" | "MODERATE" | string;
}

export interface RedFlagsAndWarnings {
  fake_websites_and_scams: string[];
  application_fee_warning: string;
  agent_and_intermediary_warnings: string;
  hidden_costs_breakdown: string[];
  misleading_claims_debunked: string[];
  official_vs_unofficial_discrepancies: string[];
}

export interface ScholarshipObligations {
  minimum_gpa_maintenance: string;
  attendance_requirements: string;
  academic_progress_monitoring: string;
  work_restrictions_during_study: string;
  home_country_return_obligation: string;
  service_obligations_or_bonds: string;
  repayment_clawback_conditions: string;
  rules_for_changing_university: string;
  rules_for_changing_major: string;
  extension_policy: string;
}

export interface VerifiedOfficialSource {
  source_name: string;
  source_url: string;
  source_type: "OFFICIAL_GOVERNMENT" | "OFFICIAL_UNIVERSITY" | "OFFICIAL_COMMISSION" | "OFFICIAL_BILATERAL" | string;
  verified_date: string;
  data_points_missing_or_unpublished_by_source: string[];
}

export interface DeepScholarshipDossier {
  scholarship_id: string;
  basic_details: BasicDetailsDossier;
  eligibility_requirements: DetailedEligibilityDossier;
  financial_coverage_breakdown: FinancialCoverageBreakdown;
  university_and_program_options: UniversityProgramOptions;
  application_process_roadmap: ApplicationProcessRoadmap;
  required_documents_checklist: DocumentChecklistItem[];
  important_dates_timeline: ImportantDatesTimeline;
  selection_process_and_weights: SelectionProcessWeights;
  competitiveness_profile: CompetitivenessProfile;
  red_flags_and_warnings: RedFlagsAndWarnings;
  scholarship_obligations_and_terms: ScholarshipObligations;
  official_sources_verified: VerifiedOfficialSource[];
}


export type EventSeverity = "INFO" | "SUCCESS" | "WARNING" | "ERROR" | "CRITICAL";

export interface ScholarXEvent {
  schema_version?: number;
  event_id: string;
  session_id: string;
  event_type: string;
  agent_id: string;
  agent_display_name: string;
  component_type: "AGENT" | "WORKFLOW" | "TOOL";
  phase: string;
  timestamp: string;
  payload: Record<string, any>;
  severity: EventSeverity;
  step_number?: number;
  total_steps?: number;
  related_scholarship_id?: string | null;
}

export interface DimensionScore {
  dimension_name: string;
  score: number;
  weight: number;
  status: "PASS" | "FAIL" | "WARNING" | "BONUS" | "ACTION_REQUIRED";
  details: string;
  evidence_snippet?: string | null;
}

export interface CostPhaseItem {
  item_name: string;
  cost_pkr: number;
  cost_usd?: number | null;
  is_mandatory: boolean;
  pakistan_context?: string | null;
}

export interface CostAnalysisResult {
  pre_application_pkr: number;
  application_pkr: number;
  visa_travel_pkr: number;
  settlement_pkr: number;
  total_out_of_pocket_pkr: number;
  total_out_of_pocket_usd: number;
  student_max_budget_pkr: number;
  shortfall_pkr: number;
  is_within_budget: boolean;
  funding_score: number;
  cost_items: CostPhaseItem[];
  risk_warnings: string[];
}

export interface DeadlineAnalysisResult {
  deadline_date: string;
  days_remaining: number;
  prep_days_needed_pakistan: number;
  slack_days: number;
  risk_level: "LOW" | "MODERATE" | "HIGH" | "VERY_HIGH" | "IMPOSSIBLE";
  is_feasible: boolean;
  deadline_score: number;
  action_timeline_recommendation: string[];
}

export interface CompositeScoreResult {
  scholarship_id: string;
  scholarship_name: string;
  overall_match_score: number;
  rank: number;
  eligibility_score: number;
  true_funding_score: number;
  bilateral_bonus_score: number;
  academic_fit_score: number;
  doc_readiness_score: number;
  deadline_score: number;
  verification_score: number;
  competition_score: number;
  dimensions: DimensionScore[];
  cost_analysis: CostAnalysisResult;
  deadline_analysis?: DeadlineAnalysisResult | null;
  blocking_reasons: string[];
  pakistan_specific_advantages: string[];
  is_recommended: boolean;
}

export interface SourceCitation {
  url: string;
  title: string;
  domain: string;
  source_type: string;
  snippet: string;
  verified_at?: string | null;
  is_official_hec: boolean;
}

export interface SkepticChallenge {
  challenge_id: string;
  category: "HIDDEN_COST" | "VISA_RISK" | "RETURN_OBLIGATION" | "DEADLINE_RISK" | "COMPETITION" | "STIPEND_DEVALUATION";
  title: string;
  description: string;
  severity: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL";
  suggested_mitigation?: string | null;
  resolved: boolean;
}

export interface DebateTopic {
  topic: string;
  advocate_point: string;
  skeptic_counterpoint: string;
  verdict: string;
}

export interface EvidenceTrail {
  scholarship_id: string;
  overall_verdict: "VERIFIED" | "PARTIALLY_VERIFIED" | "SUSPICIOUS" | "OUTDATED" | "HEC_CONFIRMED";
  confidence_score: number;
  sources: SourceCitation[];
  skeptic_challenges: SkepticChallenge[];
  debate_summary: DebateTopic[];
  last_verified_timestamp?: string | null;
  verification_notes?: string | null;
}

export interface PakistaniOffice {
  office_name: string;
  office_type: "HEC" | "IBCC" | "MOFA" | "BRITISH_COUNCIL" | "VFS_GERRYS" | "EMBASSY" | "PANEL_CLINIC";
  city: string;
  address: string;
  website_or_portal?: string | null;
  fee_pkr: number;
  estimated_turnaround_days: number;
  required_documents: string[];
  pro_tips: string[];
}

export interface MilestoneAction {
  action_id: string;
  description: string;
  estimated_days: number;
  estimated_cost_pkr: number;
  is_blocking: boolean;
  assigned_office?: string | null;
  completed: boolean;
}

export interface RoadmapMilestone {
  milestone_id: string;
  title: string;
  phase: "DOCUMENT_PREPARATION" | "HEC_IBCC_ATTESTATION" | "STANDARDIZED_TESTS" | "ONLINE_PORTAL_APPLICATION" | "EMBASSY_INTERVIEW_VISA" | "PRE_DEPARTURE_TRAVEL";
  target_timeline_days: string;
  total_phase_cost_pkr: number;
  actions: MilestoneAction[];
  guidance_notes?: string | null;
}

export interface ApplicationRoadmap {
  scholarship_id: string;
  scholarship_name: string;
  host_country: string;
  target_intake: string;
  total_preparation_days_estimated: number;
  total_budget_needed_pkr: number;
  milestones: RoadmapMilestone[];
  relevant_pakistani_offices: PakistaniOffice[];
  urgent_next_actions: string[];
}

export type PacketType = "TASK" | "CANDIDATE" | "CHALLENGE" | "SCORE" | "DIRECTIVE";

export interface DataPacket {
  id: string;
  timestamp: number;
  type: PacketType;
  from?: string;
  to?: string;
  source?: string;
  target?: string;
  label?: string;
  summary?: string;
  payloadSummary?: string;
  payload?: any;
}

export type OverlayView = "NONE" | "INTAKE" | "AUDIT" | "ROADMAP" | "XRAY" | "MODIFIER" | "ARCHIVE";
export type MapVisualMode = "DEPLOYMENT" | "TRAFFIC" | "COVERAGE" | "INTELLIGENCE";

export interface CommanderDecision {
  id: string;
  timestamp: string;
  phase: string;
  decisionText: string;
  impact: string;
  status: "EXECUTING" | "RESOLVED" | "STANDBY";
}

export interface CommanderState {
  missionGoal: string;
  activeDecision: string;
  statusText: string;
  activeAssignments: Record<Region, string>;
  recentDecisions: CommanderDecision[];
}

export interface JudgeInterventionParams {
  fullFundingOnly: boolean;
  activeRegions: Record<Region, boolean>;
  ieltsRequired: boolean;
  maxBudgetPkr: number;
  proofOfFundsLimitPkr: number;
  targetField: string;
}

export interface AgentFocusTarget {
  agentId: string;
  title: string;
  role: string;
  status: string;
  region?: Region;
  task: string;
  toolsUsed: string[];
  queriesExecuted: string[];
  recentEvents: ScholarXEvent[];
}

export interface PastSession {
  session_id: string;
  student_name?: string;
  target_degree?: string;
  field_of_study?: string;
  created_at?: string;
  verified_count?: number;
  candidates_count?: number;
  status?: string;
  [key: string]: any;
}

export type CandidatePipelineStage = "DISCOVERED" | "ELIGIBILITY" | "COST" | "DEADLINE" | "VERIFICATION" | "SKEPTIC" | "RANKING";

export interface CandidateFlowItem {
  id: string;
  scholarshipId: string;
  name: string;
  country: string;
  currentStage: CandidatePipelineStage;
  status: "IN_FLIGHT" | "PASSED" | "CHALLENGED" | "RESOLVED";
}
