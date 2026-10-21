import deepDossiersBundle from "@/lib/data/scholarships_deep_dossiers.json";

export interface ScholarshipCatalogItem {
  id: string;
  name: string;
  country: string;
  region: string;
  offering_entity: string;
  host_institutions: string;
  degree_levels: string[];
  degree_levels_str: string;
  duration: string;
  funding_type: string;
  deadline: string;
  open_date: string;
  interview_date: string;
  commencement: string;
  financial_coverage: {
    tuition: { status: string; details: string; is_covered: boolean };
    accommodation: { status: string; details: string; is_covered: boolean };
    monthly_stipend: { status: string; details: string; amount: string; is_covered: boolean };
    airfare: { status: string; details: string; is_covered: boolean };
    health_insurance: { status: string; details: string; is_covered: boolean };
    visa_fee: { status: string; details: string; is_covered: boolean };
    travel_transit: { status: string; details: string; amount: string };
    covered_tags: string[];
    not_covered_tags: string[];
  };
  eligibility: {
    age_notes: string;
    academic_qualifications: string;
    minimum_gpa: string;
    gpa_notes: string;
    nationality: string;
    english_required: boolean | null;
    english_badge: string;
    language_notes: string;
    moi_accepted: boolean;
    field_requirements: string;
    other_requirements: string;
  };
  summary: {
    workflow_steps: string[];
    required_documents: { name: string; notes: string }[];
    why_interesting: string;
    fee_warning: string;
    obligations: string;
    hidden_costs: string;
  };
  official_sources: { title: string; url: string; verified: boolean }[];
}

function clean(val: any, fallback = "N/A"): string {
  if (val === null || val === undefined) return fallback;
  const s = String(val).trim();
  return s.length > 0 ? s : fallback;
}

function normalizeCoverage(raw: any, defaultText: string) {
  if (typeof raw === "object" && raw !== null) {
    const status = clean(raw.status, "COVERED").toUpperCase();
    const details = clean(raw.details, "");
    const amount = clean(raw.amount, "");
    const isCovered = ["100%", "COVERED", "WAIVED", "INCLUDED", "FREE", "FULL"].some((k) =>
      status.includes(k)
    );
    return {
      status,
      details,
      amount,
      is_covered: isCovered || ["PARTIAL", "ALLOWANCE", "REIMBURSED"].some((k) => status.includes(k)),
    };
  } else if (typeof raw === "string") {
    const isCovered = ["100%", "COVERED", "WAIVED", "INCLUDED", "FREE"].some((k) =>
      raw.toUpperCase().includes(k)
    );
    return {
      status: isCovered ? "COVERED" : "CONDITIONAL",
      details: raw,
      amount: "",
      is_covered: isCovered,
    };
  } else if (typeof raw === "boolean") {
    return {
      status: raw ? "COVERED" : "NOT COVERED",
      details: raw ? "Fully Covered" : "Excluded",
      amount: "",
      is_covered: raw,
    };
  }
  return { status: defaultText, details: "", amount: "", is_covered: false };
}

export function getAllCatalogScholarships(): ScholarshipCatalogItem[] {
  const rawMap = deepDossiersBundle as Record<string, any>;
  const prefixToRegion: Record<string, string> = {
    AM: "Americas",
    AS: "Asia",
    EU: "Europe",
    ME: "MENA",
    OC: "Oceania",
  };

  const results: ScholarshipCatalogItem[] = [];

  for (const [sid, item] of Object.entries(rawMap)) {
    const bd = item.basic_details || {};
    const fc = item.financial_coverage_breakdown || {};
    const el = item.eligibility_requirements || {};
    const ap = item.application_process_roadmap || {};
    const rf = item.red_flags_and_warnings || {};
    const cp = item.competitiveness_profile || {};
    const it = item.important_dates_timeline || {};
    const ob = item.scholarship_obligations_and_terms || {};

    const prefix = sid.split("-")[1]?.toUpperCase() || "";
    const region = item.region || prefixToRegion[prefix] || "Global";

    const degreeLevels = Array.isArray(bd.degree_levels) ? bd.degree_levels : ["Master's", "PhD"];
    const degreeLevelsStr = degreeLevels.join(" • ");

    const tuition = normalizeCoverage(fc.tuition_fee, "100% Tuition Waiver");
    const accommodation = normalizeCoverage(fc.accommodation, "Housing / Allowance");
    const stipend = normalizeCoverage(fc.monthly_stipend, "Living Maintenance Stipend");
    const airfare = normalizeCoverage(fc.airfare, "Round-Trip Economy Airfare");
    const insurance = normalizeCoverage(fc.health_insurance, "Comprehensive Health Insurance");
    const visa = normalizeCoverage(fc.visa_fee, "Visa Fee Reimbursed or Waived");
    const transit = normalizeCoverage(fc.travel_transit_allowance, "Transit Allowance");

    const coveredTags: string[] = [];
    if (tuition.is_covered) coveredTags.push("Tuition Waiver (100%)");
    if (accommodation.is_covered) coveredTags.push("Housing / Dormitory");
    if (stipend.is_covered) {
      coveredTags.push(stipend.amount ? `Stipend (${stipend.amount})` : "Monthly Stipend");
    }
    if (airfare.is_covered) coveredTags.push("Return Airfare");
    if (insurance.is_covered) coveredTags.push("Health Insurance");
    if (visa.is_covered) coveredTags.push("Visa Covered");
    if (transit.is_covered) coveredTags.push("Settlement Allowance");

    const notCoveredTags: string[] = [];
    if (!tuition.is_covered) notCoveredTags.push("Tuition Fees Not Covered");
    if (!airfare.is_covered) notCoveredTags.push("Airfare Self-Funded");
    if (!accommodation.is_covered) notCoveredTags.push("Housing Arranged Privately");

    const moiAccepted = Boolean(el.moi_certificate_accepted);
    const ielts = el.ielts_minimum;
    const toefl = el.toefl_minimum;
    let englishBadge = "Institutional Standard";
    if (el.english_test_required === false || moiAccepted) {
      englishBadge = moiAccepted ? "MOI Accepted (No IELTS)" : "No Language Test";
    } else if (ielts || toefl) {
      englishBadge = `Required: ${[ielts ? `IELTS ${ielts}` : "", toefl ? `TOEFL ${toefl}` : ""].filter(Boolean).join(" / ")}`;
    }

    const workflowSteps = Array.isArray(ap.step_by_step_workflow) && ap.step_by_step_workflow.length > 0
      ? ap.step_by_step_workflow.slice(0, 5).map((w: any) => clean(w))
      : [
          "1. Prepare and attest academic credentials via HEC / IBCC.",
          "2. Submit formal application on host institution portal.",
          "3. Complete government/bilateral agency scholarship dossier.",
          "4. Undertake institutional interview and academic screening.",
          "5. Secure final award letter, student visa, and consular clearance.",
        ];

    const rawDocs = Array.isArray(item.required_documents_checklist) ? item.required_documents_checklist : [];
    const docChecklist = rawDocs.slice(0, 8).map((d: any) => ({
      name: clean(d?.document_name || d),
      notes: clean(d?.specific_requirements_or_instructions, ""),
    }));

    const whyInteresting = `${clean(cp.competitiveness_tier, "High Prestige Merit Award")} • ${clean(bd.number_of_awards_pakistan, "Open bilateral allocation")}. Provides full institutional coverage in ${clean(bd.host_country, "Host Nation")}.`;
    const feeWarning = clean(rf.application_fee_warning, "Official applications are free or zero fee via accredited portals.");
    const hiddenCosts = clean(rf.hidden_costs_breakdown, "Verify upfront visa, testing, and initial arrival buffer prior to first stipend.");

    const sources = (item.official_sources_verified || []).map((s: any) => ({
      title: clean(s.source_name || s.entity_type, "Official Portal"),
      url: s.source_url || "https://scholarship.hec.gov.pk",
      verified: Boolean(s.verification_status),
    }));

    if (ap.submission_portal_url && !sources.some((s: any) => s.url === ap.submission_portal_url)) {
      sources.unshift({
        title: clean(ap.portal_system_name, "Online Application Portal"),
        url: ap.submission_portal_url,
        verified: true,
      });
    }

    results.push({
      id: sid,
      name: clean(bd.scholarship_name, item.name || "Scholarship Program"),
      country: clean(bd.host_country, item.host_country || "International"),
      region,
      offering_entity: clean(bd.offering_entity, "Awarding Agency"),
      host_institutions: clean(bd.host_institutions_covered || item.host_institution, "Accredited Universities"),
      degree_levels: degreeLevels,
      degree_levels_str: degreeLevelsStr,
      duration: clean(bd.duration_of_scholarship, "Full Program Duration"),
      funding_type: clean(bd.funding_classification, "FULLY_FUNDED"),
      deadline: clean(it.application_deadline, item.application_deadline || "Annual Cycle"),
      open_date: clean(it.application_open_date, "Check Official Portal"),
      interview_date: clean(it.interview_period, "Spring Selection"),
      commencement: clean(it.semester_commencement, "Fall 2027 Intake"),
      financial_coverage: {
        tuition,
        accommodation,
        monthly_stipend: stipend,
        airfare,
        health_insurance: insurance,
        visa_fee: visa,
        travel_transit: transit,
        covered_tags: coveredTags,
        not_covered_tags: notCoveredTags,
      },
      eligibility: {
        age_notes: clean(el.age_limit_notes, "Early-to-mid career academic focus"),
        academic_qualifications: clean(el.academic_qualifications, "Recognized preceding degree qualification"),
        minimum_gpa: clean(el.minimum_gpa_scale || el.minimum_gpa_percentage, "3.0 / 4.0 or 70%"),
        gpa_notes: clean(el.grading_conversion_notes, "Minimum merit threshold"),
        nationality: Array.isArray(el.nationality_requirements) ? el.nationality_requirements.join("; ") : clean(el.nationality_requirements, "Pakistani & International Applicants"),
        english_required: el.english_test_required,
        english_badge: englishBadge,
        language_notes: clean(el.language_notes, "Standard university proficiency standard"),
        moi_accepted: moiAccepted,
        field_requirements: clean(bd.major_restrictions, "All eligible faculties"),
        other_requirements: clean(el.work_experience_notes, "Standard merit evaluation"),
      },
      summary: {
        workflow_steps: workflowSteps,
        required_documents: docChecklist.length > 0 ? docChecklist : [
          { name: "Valid Passport", notes: "Min 12-month validity" },
          { name: "Academic Transcripts", notes: "Attested by HEC / Board" },
          { name: "Statement of Purpose", notes: "Academic proposal" },
          { name: "2 Recommendation Letters", notes: "Faculty references" },
        ],
        why_interesting: whyInteresting,
        fee_warning: feeWarning,
        obligations: clean(ob.home_country_return_obligation, "Standard academic standing required"),
        hidden_costs: hiddenCosts,
      },
      official_sources: sources.length > 0 ? sources : [
        { title: "Official Portal", url: "https://scholarship.hec.gov.pk", verified: true },
      ],
    });
  }

  return results;
}
