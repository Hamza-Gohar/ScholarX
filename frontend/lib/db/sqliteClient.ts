import { getDatabasePath, getWritableSessionsDbPath } from "./databaseBundle";
import { Scholarship, StudentProfile, Region } from "@/lib/types";
import { calculatePakistanCosts } from "../cost/pakistanCostEngine";
import { calculateDeadlineRunway } from "../deadline/deadlineEngine";
import { groqPool } from "../ai/groqClient";

// Dynamic check for node:sqlite DatabaseSync
let DatabaseSyncClass: any = null;
try {
  const sqlite = typeof require !== "undefined" ? require("node:sqlite") : null;
  DatabaseSyncClass = sqlite?.DatabaseSync || null;
} catch {
  DatabaseSyncClass = null;
}

export interface ScholarshipFilterOptions {
  search?: string;
  region?: string;
  country?: string;
  degree_level?: string;
  funding_type?: string;
  hec_only?: boolean;
  moi_only?: boolean;
  sort_by?: string;
  sort_order?: "asc" | "desc";
  limit?: number;
  offset?: number;
}

function getReadDb(name: "scholarships_database.db" | "scholarx_sessions.db") {
  if (!DatabaseSyncClass) return null;
  try {
    const dbPath = getDatabasePath(name);
    return new DatabaseSyncClass(dbPath, { open: true, readOnly: true });
  } catch (err) {
    console.warn(`[SQLite] Failed to open read-only database ${name}:`, err);
    return null;
  }
}

function getWritableSessionsDb() {
  if (!DatabaseSyncClass) return null;
  try {
    const dbPath = getWritableSessionsDbPath();
    return new DatabaseSyncClass(dbPath, { open: true, readOnly: false });
  } catch (err) {
    console.warn("[SQLite] Failed to open writable sessions database:", err);
    return null;
  }
}

/**
 * Parses raw JSON string safely.
 */
function safeJsonParse(val: any, fallback: any = null): any {
  if (!val) return fallback;
  if (typeof val === "object") return val;
  try {
    return JSON.parse(val);
  } catch {
    return fallback;
  }
}

/**
 * Converts a raw SQLite row from scholarships_cache or scholarships into a typed Scholarship.
 */
function rowToScholarship(row: any): Scholarship {
  if (!row) return null as any;

  // If full JSON is cached in data_json, parse it first
  if (row.data_json) {
    const full = safeJsonParse(row.data_json, null);
    if (full && full.scholarship_id) {
      if (row.final_score != null) full.final_score = row.final_score;
      if (row.rank != null) full.rank = row.rank;
      return full;
    }
  }

  // Construct from relational table columns
  const degrees = typeof row.degree_levels === "string"
    ? row.degree_levels.split(",").map((d: string) => d.trim()).filter(Boolean)
    : Array.isArray(row.degree_levels) ? row.degree_levels : ["Bachelor's", "Master's"];

  return {
    scholarship_id: row.scholarship_id,
    name: row.name,
    host_country: row.host_country || "PK",
    host_country_name: row.host_country_name || row.host_country || "International",
    host_institution: row.host_institution || "Recognized Universities",
    region: (row.region as Region) || "Asia",
    source_url: row.source_url || "https://scholarship.hec.gov.pk",
    portal_url: row.portal_url || "https://scholarship.hec.gov.pk",
    discovered_by: row.discovered_by || "sqlite_catalog",
    description: row.description || `${row.name} for international students.`,
    eligibility: {
      degree_levels: degrees,
      min_gpa_4_scale: row.min_gpa_4_scale ?? 3.0,
      min_gpa_percentage: row.min_gpa_percentage ?? 70.0,
      eligible_fields: row.Subjects_included
        ? (row.Subjects_included as string).split(";").map((s: string) => s.trim()).filter(Boolean)
        : ["All Academic Disciplines"],
      eligible_nationalities: ["Pakistan"],
      min_years_education: 12,
      work_experience_years_required: 0,
    },
    funding: {
      funding_type: (row.funding_type as any) || "FULL",
      tuition: "100%",
      accommodation: "Provided",
      monthly_stipend: row.monthly_stipend || (row.monthly_stipend_pkr_approx ? `PKR ${row.monthly_stipend_pkr_approx.toLocaleString()}/mo` : "Included"),
      monthly_stipend_pkr_approx: row.monthly_stipend_pkr_approx || (row.funding_type === "FULL" ? 120000 : 0),
      travel_airfare: row.region === "Asia" ? "NONE" : "SUBSIDIZED",
      health_insurance: "Covered",
    },
    pakistan_requirements: {
      pakistan_eligible: Boolean(row.pakistan_eligible ?? 1),
      pakistan_bilateral_quota: Boolean(row.pakistan_bilateral_quota),
      pakistan_quota_seats: row.pakistan_quota_seats ?? null,
      hec_managed: Boolean(row.hec_managed),
      hec_portal_url: "https://scholarship.hec.gov.pk",
      hec_hat_required: false,
      hec_usat_required: false,
      hec_attestation_required: Boolean(row.hec_attestation_required),
      ibcc_equivalence_required: true,
      mofa_attestation_required: true,
      accepts_moi_certificate: Boolean(row.accepts_moi_certificate),
    },
    language: {
      english_test_required: !row.accepts_moi_certificate,
      host_language_prep: false,
    },
    application_deadline: row.application_deadline || "2027-01-20",
    application_opens: row.application_opens || "2026-09-01",
    competition_level: row.competition_level || "MODERATE",
    confidence_score: 0.95,
    status: "VERIFIED",
    ...(row.final_score != null ? { final_score: row.final_score } : {}),
    ...(row.rank != null ? { rank: row.rank } : {}),
  } as any;
}

/**
 * Queries scholarships from SQLite database with multi-facet filtering and pagination.
 */
export function queryScholarshipsFromDb(options: ScholarshipFilterOptions = {}): {
  scholarships: Scholarship[];
  total: number;
} | null {
  const db = getReadDb("scholarships_database.db");
  if (!db) return null;

  try {
    const {
      search,
      region,
      country,
      degree_level,
      funding_type,
      hec_only,
      moi_only,
      sort_by = "name",
      sort_order = "asc",
      limit = 50,
      offset = 0,
    } = options;

    const conditions: string[] = [];
    const params: any[] = [];

    if (region && region !== "ALL") {
      conditions.push("LOWER(region) = LOWER(?)");
      params.push(region);
    }

    if (country) {
      conditions.push("(LOWER(host_country) = LOWER(?) OR LOWER(host_country_name) LIKE LOWER(?))");
      params.push(country, `%${country}%`);
    }

    if (funding_type && funding_type !== "ALL") {
      conditions.push("UPPER(funding_type) = UPPER(?)");
      params.push(funding_type);
    }

    if (degree_level && degree_level !== "ALL") {
      conditions.push("LOWER(degree_levels) LIKE LOWER(?)");
      params.push(`%${degree_level}%`);
    }

    if (hec_only) {
      conditions.push("(hec_managed = 1 OR pakistan_bilateral_quota = 1)");
    }

    if (moi_only) {
      conditions.push("accepts_moi_certificate = 1");
    }

    if (search) {
      conditions.push("(LOWER(name) LIKE LOWER(?) OR LOWER(scholarship_id) LIKE LOWER(?) OR LOWER(host_institution) LIKE LOWER(?) OR LOWER(description) LIKE LOWER(?) OR LOWER(COALESCE(Subjects_included, '')) LIKE LOWER(?))");
      const sTerm = `%${search}%`;
      params.push(sTerm, sTerm, sTerm, sTerm, sTerm);
    }

    const whereClause = conditions.length > 0 ? `WHERE ${conditions.join(" AND ")}` : "";

    // Count total matches
    const countSql = `SELECT COUNT(*) as count FROM scholarships ${whereClause}`;
    const countRow = db.prepare(countSql).get(...params);
    const total = countRow ? Number((countRow as any).count) : 0;

    // Sorting
    let sortColumn = "name";
    switch (sort_by) {
      case "country": sortColumn = "host_country_name"; break;
      case "deadline": sortColumn = "application_deadline"; break;
      case "stipend_pkr": sortColumn = "monthly_stipend_pkr_approx"; break;
      case "min_gpa": sortColumn = "min_gpa_percentage"; break;
      case "scholarship_id": sortColumn = "scholarship_id"; break;
      default: sortColumn = "name"; break;
    }
    const orderDirection = sort_order === "desc" ? "DESC" : "ASC";

    const querySql = `
      SELECT * FROM scholarships
      ${whereClause}
      ORDER BY ${sortColumn} ${orderDirection}
      LIMIT ? OFFSET ?
    `;

    const rows = db.prepare(querySql).all(...params, limit, offset);
    const scholarships = rows.map(rowToScholarship);

    return { scholarships, total };
  } catch (err) {
    console.error("[SQLite] Error querying scholarships:", err);
    return null;
  }
}

/**
 * Returns an array of scholarships from SQLite matching filter options, or empty array.
 */
export function getScholarshipsFromDb(options: ScholarshipFilterOptions = {}): Scholarship[] {
  const res = queryScholarshipsFromDb(options);
  return res?.scholarships || [];
}

export interface IntelligentRetrievalResult {
  isEligible: boolean;
  ineligibilityReason: "GPA_INSUFFICIENT" | "NO_REGIONAL_MATCH" | "NO_LANGUAGE_MATCH" | "NO_SUBJECT_MATCH" | null;
  message: string;
  totalInRegions: number;
  afterDegreeFilter: number;
  afterGpaFilter: number;
  afterLanguageFilter: number;
  afterDeadlineFilter: number;
  afterSubjectFilter: number;
  scholarships: Scholarship[];
  rankedResults: any[];
}

/**
 * Intelligent Multi-Stage Database Retrieval Engine
 * 1. Region Filter: Search strictly in user-chosen regions
 * 2. Degree Filter: Match candidate's target degree level
 * 3. GPA Comparison: Eliminate sub-threshold programs; if none pass, issue user ineligibility guidance
 * 4. Language Filter: If no IELTS -> MOI accepted only; if has IELTS -> compare band score
 * 5. Deadline Filter: Eliminate outdated/expired deadlines
 * 6. Subjects Included AI Filter: Semantic match candidate's targeted field with Subjects_included in DB via Groq Round Robin
 * 7. Multi-Factor Ranking: Success rate in PK + Quota seats + Monthly stipend + Competition level
 */
export async function retrieveIntelligentScholarshipsFromDb(profile: any): Promise<IntelligentRetrievalResult> {
  const db = getReadDb("scholarships_database.db");
  if (!db) {
    return {
      isEligible: false,
      ineligibilityReason: null,
      message: "Database connection unavailable",
      totalInRegions: 0,
      afterDegreeFilter: 0,
      afterGpaFilter: 0,
      afterLanguageFilter: 0,
      afterDeadlineFilter: 0,
      afterSubjectFilter: 0,
      scholarships: [],
      rankedResults: [],
    };
  }

  try {
    // 1. Resolve User Regions
    const rawRegions: string[] = (
      profile?.preferences?.preferred_regions ||
      profile?.preferences?.preferredRegions ||
      profile?.personal?.target_regions ||
      profile?.personal?.targetRegions ||
      []
    ).map((r: string) => r.trim()).filter(Boolean);

    const userRegions = rawRegions.length > 0
      ? rawRegions
      : ["Europe", "Asia", "Americas", "MENA", "Oceania"];

    // 2. Resolve Target Degree Level
    const rawDegree = String(
      profile?.preferences?.target_degree_level ||
      profile?.preferences?.targetDegreeLevel ||
      profile?.academic?.degree_level ||
      profile?.degree ||
      "Bachelor's"
    ).trim();

    let degreeKeyword = "Bachelor";
    const rawDegreeLower = rawDegree.toLowerCase();
    if (rawDegreeLower.includes("master") || rawDegreeLower.includes("ms") || rawDegreeLower.includes("msc") || rawDegreeLower.includes("postgrad")) {
      degreeKeyword = "Master";
    } else if (rawDegreeLower.includes("phd") || rawDegreeLower.includes("doctor")) {
      degreeKeyword = "PhD";
    }

    // 3. Resolve GPA
    const candidatePct = Number(
      profile?.academic?.percentage ||
      profile?.academic?.gpa_percentage ||
      profile?.academic?.ibcc_equivalence_percentage ||
      (profile?.academic?.gpa_4_scale ? (profile.academic.gpa_4_scale / 4.0) * 100 : 0)
    );
    const candidateGpa4 = Number(
      profile?.academic?.gpa_4_scale ||
      (candidatePct > 0 ? (candidatePct / 100) * 4.0 : 0)
    );

    // 4. Resolve Language / IELTS
    const englishTest = String(
      profile?.language?.english_proficiency_test ||
      profile?.language?.test_type ||
      ""
    ).toUpperCase();
    const ieltsScore = Number(profile?.language?.ielts_overall || 0);
    const hasIelts = Boolean(
      (englishTest.includes("IELTS") && ieltsScore > 0) ||
      (profile?.language?.has_english_test && ieltsScore > 0)
    );

    // -------------------------------------------------------------------------
    // STEP 1: Search ONLY within user-chosen regions
    // -------------------------------------------------------------------------
    const placeholders = userRegions.map(() => "?").join(",");
    const regionSql = `SELECT * FROM scholarships WHERE region IN (${placeholders}) COLLATE NOCASE`;
    const regionRows: any[] = db.prepare(regionSql).all(...userRegions);

    if (regionRows.length === 0) {
      return {
        isEligible: false,
        ineligibilityReason: "NO_REGIONAL_MATCH",
        message: `No active scholarship catalog records found in chosen regions: ${userRegions.join(", ")}.`,
        totalInRegions: 0,
        afterDegreeFilter: 0,
        afterGpaFilter: 0,
        afterLanguageFilter: 0,
        afterDeadlineFilter: 0,
        afterSubjectFilter: 0,
        scholarships: [],
        rankedResults: [],
      };
    }

    // -------------------------------------------------------------------------
    // STEP 2: Filter by Degree Level (Bachelor's, Master's, PhD)
    // -------------------------------------------------------------------------
    const degFiltered = regionRows.filter((row: any) => {
      const dl = String(row.degree_levels || "").toLowerCase();
      return dl.includes(degreeKeyword.toLowerCase());
    });

    // -------------------------------------------------------------------------
    // STEP 3: Compare Student GPA vs Minimum Requirement of Each Scholarship
    // -------------------------------------------------------------------------
    const gpaFiltered: any[] = [];
    let lowestRequiredPct = 100;
    let lowestRequired4 = 4.0;

    for (const row of degFiltered) {
      const minPct = Number(row.min_gpa_percentage ?? 70.0);
      const min4 = Number(row.min_gpa_4_scale ?? 2.8);
      lowestRequiredPct = Math.min(lowestRequiredPct, minPct);
      lowestRequired4 = Math.min(lowestRequired4, min4);

      const passesPct = candidatePct > 0 && candidatePct >= minPct;
      const passes4 = candidateGpa4 > 0 && candidateGpa4 >= min4;
      if (passesPct || passes4) {
        gpaFiltered.push(row);
      }
    }

    // If marks are below 70% or GPA is not sufficient for any merit scholarship, notify the user with polite message
    if (gpaFiltered.length === 0 || (candidatePct > 0 && candidatePct < 70.0)) {
      const gpaDisplay = candidatePct > 0 ? `${candidatePct}%` : `${candidateGpa4.toFixed(2)} CGPA`;
      const reqDisplay = lowestRequiredPct < 100 ? `${lowestRequiredPct}% (${lowestRequired4.toFixed(1)} CGPA)` : "70% (2.8 CGPA)";
      return {
        isEligible: false,
        ineligibilityReason: "GPA_INSUFFICIENT",
        message: `You are currently ineligible for competitive merit-based scholarships based on your academic marks (${gpaDisplay}). Standard merit awards require a minimum of ${reqDisplay}. We politely advise targeting Need-Based Grants (such as Italian DSU Regional Grants or China CSC Type-B) or preparatory foundation pathways.`,
        totalInRegions: regionRows.length,
        afterDegreeFilter: degFiltered.length,
        afterGpaFilter: 0,
        afterLanguageFilter: 0,
        afterDeadlineFilter: 0,
        afterSubjectFilter: 0,
        scholarships: [],
        rankedResults: [],
      };
    }

    // -------------------------------------------------------------------------
    // STEP 4: Language Proficiency (IELTS vs MOI) Filter
    // -------------------------------------------------------------------------
    const langFiltered = gpaFiltered.filter((row: any) => {
      const acceptsMoi = Boolean(row.accepts_moi_certificate);
      const minIelts = Number(row.ielts_minimum ?? 0);

      if (!hasIelts) {
        // Without IELTS: ONLY scholarships accepting Medium of Instruction (or 0 IELTS req)
        return acceptsMoi || minIelts === 0;
      } else {
        // With IELTS: Eligible for MOI-accepted scholarships OR programs meeting/exceeding IELTS band
        return acceptsMoi || (ieltsScore >= minIelts);
      }
    });

    if (langFiltered.length === 0) {
      return {
        isEligible: false,
        ineligibilityReason: "NO_LANGUAGE_MATCH",
        message: hasIelts
          ? `Your IELTS band (${ieltsScore}) is below the required English proficiency scores for programs in ${userRegions.join(", ")}.`
          : `Selected programs require an official IELTS/TOEFL score and do not accept Medium of Instruction (MOI) certificates.`,
        totalInRegions: regionRows.length,
        afterDegreeFilter: degFiltered.length,
        afterGpaFilter: gpaFiltered.length,
        afterLanguageFilter: 0,
        afterDeadlineFilter: 0,
        afterSubjectFilter: 0,
        scholarships: [],
        rankedResults: [],
      };
    }

    // -------------------------------------------------------------------------
    // STEP 5: Deadline Validity Filter
    // -------------------------------------------------------------------------
    const now = new Date();
    now.setHours(0, 0, 0, 0);

    const deadlineFiltered = langFiltered.filter((row: any) => {
      const rawDl = row.application_deadline;
      if (!rawDl) return true;
      try {
        const dlDate = new Date(rawDl.trim().slice(0, 10));
        if (!isNaN(dlDate.getTime())) {
          return dlDate.getTime() >= now.getTime();
        }
      } catch {
        return true;
      }
      return true;
    });

    const candidatePool = deadlineFiltered.length > 0 ? deadlineFiltered : langFiltered;

    // -------------------------------------------------------------------------
    // STEP 6: Subjects Included AI Semantic Matching (Groq Round Robin)
    // Compare candidate's targeted field of study with Subjects_included in DB
    // -------------------------------------------------------------------------
    const candidateField = String(
      profile?.academic?.field_of_study ||
      profile?.preferences?.target_fields?.[0] ||
      profile?.field ||
      ""
    ).trim();

    let subjectFiltered: any[] = [];
    const isGeneralField = !candidateField || 
      candidateField.toLowerCase().includes("all academic") || 
      candidateField.toLowerCase().includes("all discipline") ||
      candidateField.toLowerCase().includes("all field");

    if (isGeneralField) {
      subjectFiltered = candidatePool;
    } else {
      const candidatesToAiEvaluate: any[] = [];
      const candLower = candidateField.toLowerCase();

      for (const row of candidatePool) {
        const rawSubj = String(row.Subjects_included || row.subjects_included || "").trim();
        const rawSubjLower = rawSubj.toLowerCase();

        // If scholarship offers all disciplines or subjects are not restricted
        if (!rawSubj || rawSubjLower.includes("all academic") || rawSubjLower.includes("all field") || rawSubjLower.includes("all discipline")) {
          subjectFiltered.push(row);
        } else if (rawSubjLower.includes(candLower)) {
          // Direct substring match
          subjectFiltered.push(row);
        } else {
          // Collect for Groq semantic evaluation
          candidatesToAiEvaluate.push(row);
        }
      }

      // If there are candidates requiring semantic evaluation and Groq is available
      if (candidatesToAiEvaluate.length > 0 && groqPool.getKeyCount() > 0) {
        try {
          const chunkSize = 15;
          for (let i = 0; i < candidatesToAiEvaluate.length; i += chunkSize) {
            const chunk = candidatesToAiEvaluate.slice(i, i + chunkSize);
            const prompt = `You are an academic admissions evaluator.
User's targeted field of study: "${candidateField}"

Evaluate whether each scholarship offers or covers the user's field (directly or related subdiscipline):
${chunk.map((s) => `[${s.scholarship_id}]: ${s.Subjects_included || s.name}`).join("\n")}

Respond ONLY with a JSON object mapping each scholarship ID to true (compatible) or false (incompatible):
{"ID": true}`;

            const res = await groqPool.chatCompletion({
              messages: [
                { role: "system", content: "You evaluate academic compatibility. Return strictly JSON mapping scholarship IDs to boolean true or false." },
                { role: "user", content: prompt },
              ],
              temperature: 0.0,
              json_mode: true,
              max_tokens: 250,
            });

            const parsed = JSON.parse(res.content);
            for (const row of chunk) {
              if (parsed[row.scholarship_id] === true) {
                subjectFiltered.push(row);
              }
            }
          }
        } catch (err) {
          console.warn("[SQLite] Groq subject evaluation fallback:", err);
          subjectFiltered.push(...candidatesToAiEvaluate);
        }
      } else if (candidatesToAiEvaluate.length > 0) {
        subjectFiltered.push(...candidatesToAiEvaluate);
      }
    }

    if (subjectFiltered.length === 0) {
      return {
        isEligible: false,
        ineligibilityReason: "NO_SUBJECT_MATCH",
        message: `No active scholarships in ${userRegions.join(", ")} currently match your targeted field of study ("${candidateField}"). Consider broadening your field specialization.`,
        totalInRegions: regionRows.length,
        afterDegreeFilter: degFiltered.length,
        afterGpaFilter: gpaFiltered.length,
        afterLanguageFilter: langFiltered.length,
        afterDeadlineFilter: deadlineFiltered.length,
        afterSubjectFilter: 0,
        scholarships: [],
        rankedResults: [],
      };
    }

    // -------------------------------------------------------------------------
    // STEP 7: Multi-Factor Ranking
    // Based on success_rate_pakistan_percent, pakistan_quota_seats,
    // monthly_stipend_pkr_approx, and competition_level
    // -------------------------------------------------------------------------
    function calculateIntelligentScore(row: any): number {
      const succ = Number(row.success_rate_pakistan_percent ?? 8.0);
      const quota = Number(row.pakistan_quota_seats ?? (row.pakistan_bilateral_quota ? 30 : 0));
      const stipend = Number(row.monthly_stipend_pkr_approx ?? (row.funding_type === "FULL" ? 120000 : 40000));
      const comp = String(row.competition_level || "MODERATE").toUpperCase();

      const compScore = comp === "LOW" ? 95 : comp === "MODERATE" ? 85 : comp === "HIGH" ? 72 : 60;
      const scoreSucc = Math.min(100, (succ / 35.0) * 100);
      const scoreQuota = quota > 0 ? Math.min(100, 45 + (quota / 280.0) * 55) : 30;
      const scoreStipend = Math.min(100, (stipend / 300000.0) * 100);

      const composite = (scoreSucc * 0.35) + (scoreQuota * 0.25) + (scoreStipend * 0.25) + (compScore * 0.15);
      return Math.round(composite * 10) / 10;
    }

    const sortedRows = [...subjectFiltered].sort(
      (a, b) => calculateIntelligentScore(b) - calculateIntelligentScore(a)
    );

    const scholarships = sortedRows.map(rowToScholarship);

    const rankedResults = sortedRows.map((r: any, idx: number) => {
      const sc = scholarships[idx];
      const finalScore = calculateIntelligentScore(r);
      const costAnalysis = calculatePakistanCosts(sc, profile);
      const deadlineAnalysis = calculateDeadlineRunway(sc, profile);
      const bilateralSeats = r.pakistan_quota_seats ?? (r.pakistan_bilateral_quota ? 25 : null);

      return {
        scholarship_id: sc.scholarship_id,
        name: sc.name,
        scholarship_name: sc.name,
        host_country_name: sc.host_country_name,
        host_country: sc.host_country_name,
        region: sc.region,
        degree_level: rawDegree,
        field_of_study: profile?.academic?.field_of_study || profile?.preferences?.target_fields?.[0] || "All Fields",
        subjects_included: r.Subjects_included || r.subjects_included || null,
        subjects_source_url: r.subjects_source_url || null,
        overall_match_score: finalScore,
        final_score: finalScore,
        portal_url: sc.portal_url || sc.source_url,
        official_portal_url: sc.portal_url || sc.source_url,
        hec_managed: Boolean(r.hec_managed || r.pakistan_bilateral_quota),
        pakistan_requirements: sc.pakistan_requirements,
        funding: sc.funding,
        application_deadline: r.application_deadline,
        bilateral_seats: bilateralSeats,
        monthly_stipend_pkr: costAnalysis.monthlyStipendPkr || r.monthly_stipend_pkr_approx || 120000,
        initial_out_of_pocket_pkr: costAnalysis.totalOutOfPocketPkr,
        budget_status: costAnalysis.isWithinBudget ? "WITHIN_BUDGET" : "DEFICIT_WARNING",
        quota_description: bilateralSeats ? `${bilateralSeats} Dedicated Quota Seats for Pakistan` : "Open International Merit Competition",
        cost_analysis: costAnalysis,
        deadline_analysis: deadlineAnalysis,
        factors: {
          eligibility: 95,
          funding: Math.min(100, Math.round((Number(r.monthly_stipend_pkr_approx || 100000) / 300000) * 100)),
          bilateral_bonus: bilateralSeats ? 95 : 75,
          academic_fit: 90,
          doc_readiness: hasIelts ? 92 : 82,
          deadline: deadlineAnalysis.daysRemaining >= 45 ? 90 : 75,
          verification: 95,
          competition: r.competition_level === "LOW" ? 95 : r.competition_level === "MODERATE" ? 85 : 70,
        },
        rank: idx + 1,
      };
    });

    return {
      isEligible: true,
      ineligibilityReason: null,
      message: `Successfully retrieved ${rankedResults.length} qualified scholarships matching your criteria.`,
      totalInRegions: regionRows.length,
      afterDegreeFilter: degFiltered.length,
      afterGpaFilter: gpaFiltered.length,
      afterLanguageFilter: langFiltered.length,
      afterDeadlineFilter: deadlineFiltered.length,
      afterSubjectFilter: subjectFiltered.length,
      scholarships,
      rankedResults,
    };
  } catch (err) {
    console.error("[SQLite] Error in retrieveIntelligentScholarshipsFromDb:", err);
    return {
      isEligible: false,
      ineligibilityReason: null,
      message: "An unexpected error occurred during database retrieval.",
      totalInRegions: 0,
      afterDegreeFilter: 0,
      afterGpaFilter: 0,
      afterLanguageFilter: 0,
      afterDeadlineFilter: 0,
      afterSubjectFilter: 0,
      scholarships: [],
      rankedResults: [],
    };
  }
}

/**
 * Fetches a single scholarship and its deep dossier from SQLite database.
 */
export function getScholarshipByIdFromDb(scholarshipId: string): Scholarship | null {
  const cleanId = scholarshipId.trim();

  // Try cache in scholarx_sessions.db first for full 11-dimension JSON
  const sessDb = getReadDb("scholarx_sessions.db");
  if (sessDb) {
    try {
      const row = sessDb.prepare("SELECT * FROM scholarships_cache WHERE LOWER(scholarship_id) = LOWER(?)").get(cleanId);
      if (row) {
        return rowToScholarship(row);
      }
    } catch (err) {
      console.warn("[SQLite] Error reading scholarships_cache:", err);
    }
  }

  // Fallback to scholarships_database.db
  const sDb = getReadDb("scholarships_database.db");
  if (sDb) {
    try {
      const row = sDb.prepare("SELECT * FROM scholarships WHERE LOWER(scholarship_id) = LOWER(?)").get(cleanId);
      if (row) {
        return rowToScholarship(row);
      }
    } catch (err) {
      console.warn("[SQLite] Error reading scholarships:", err);
    }
  }

  return null;
}

/**
 * Lists recent research missions from SQLite database.
 */
export function listSessionsFromDb(limit: number = 50): any[] {
  const db = getReadDb("scholarx_sessions.db");
  if (!db) return [];

  try {
    const rows = db.prepare(`
      SELECT s.session_id, s.student_id, s.status, s.total_scanned, s.total_verified,
             s.top_scholarship, s.top_score, s.created_at, s.completed_at,
             st.name, st.profile_json
      FROM sessions s
      LEFT JOIN students st ON s.student_id = st.student_id
      ORDER BY s.created_at DESC
      LIMIT ?
    `).all(limit);

    return rows.map((r: any) => ({
      session_id: r.session_id,
      student_id: r.student_id,
      status: r.status,
      student_name: r.name || "Student Applicant",
      top_scholarship: r.top_scholarship,
      top_score: r.top_score,
      created_at: r.created_at,
      completed_at: r.completed_at,
      profile: safeJsonParse(r.profile_json, null),
    }));
  } catch (err) {
    console.error("[SQLite] Error listing sessions from DB:", err);
    return [];
  }
}

/**
 * Retrieves full session detail from SQLite database (with profile and ranked scholarships).
 */
export function getSessionDetailFromDb(sessionId: string): any | null {
  const cleanId = sessionId.trim();
  const db = getReadDb("scholarx_sessions.db");
  if (!db) return null;

  try {
    const sRow: any = db.prepare(`
      SELECT s.session_id, s.student_id, s.mission_params_json, s.status,
             s.total_scanned, s.total_verified, s.created_at, s.completed_at,
             st.profile_json, st.name
      FROM sessions s
      LEFT JOIN students st ON s.student_id = st.student_id
      WHERE LOWER(s.session_id) = LOWER(?)
    `).get(cleanId);

    if (!sRow) {
      // Check if session ID exists with prefix variance
      const fuzzyRow: any = db.prepare(`
        SELECT s.session_id, s.student_id, s.mission_params_json, s.status,
               s.total_scanned, s.total_verified, s.created_at, s.completed_at,
               st.profile_json, st.name
        FROM sessions s
        LEFT JOIN students st ON s.student_id = st.student_id
        WHERE s.session_id LIKE ?
        ORDER BY s.created_at DESC
        LIMIT 1
      `).get(`%${cleanId.replace("session-pk-", "")}%`);

      if (!fuzzyRow) return null;
      return buildSessionPayloadFromRow(db, fuzzyRow);
    }

    return buildSessionPayloadFromRow(db, sRow);
  } catch (err) {
    console.error("[SQLite] Error getting session detail:", err);
    return null;
  }
}

function buildSessionPayloadFromRow(db: any, sRow: any) {
  const profile = safeJsonParse(sRow.profile_json, null);
  const missionParams = safeJsonParse(sRow.mission_params_json, {});

  // Fetch evaluated scholarships for this session
  const scRows = db.prepare(`
    SELECT ss.scholarship_id, ss.final_score, ss.rank, ss.eligibility_json, ss.cost_json, ss.deadline_json,
           sc.name, sc.country AS host_country, sc.host_country_name, sc.region, sc.funding_type,
           sc.monthly_stipend_pkr_approx, sc.pakistan_quota_seats, sc.data_json
    FROM session_scholarships ss
    LEFT JOIN scholarships_cache sc ON ss.scholarship_id = sc.scholarship_id
    WHERE ss.session_id = ?
    ORDER BY ss.rank ASC
  `).all(sRow.session_id);

  const discovered = scRows.map((r: any) => {
    const sc = rowToScholarship(r);
    (sc as any).final_score = r.final_score;
    (sc as any).rank = r.rank;
    (sc as any).cost_analysis = safeJsonParse(r.cost_json, null);
    (sc as any).deadline_analysis = safeJsonParse(r.deadline_json, null);
    (sc as any).eligibility_analysis = safeJsonParse(r.eligibility_json, null);
    return sc;
  });

  return {
    session: {
      session_id: sRow.session_id,
      student_id: sRow.student_id,
      status: sRow.status || "COMPLETED",
      student_profile: profile,
      discovered_scholarships: discovered,
      mission_parameters: missionParams,
      created_at: sRow.created_at,
      completed_at: sRow.completed_at,
    },
    profile,
  };
}

/**
 * Persists session and profile into SQLite database.
 */
export function saveSessionToDb(data: {
  sessionId: string;
  studentId?: string;
  profile?: any;
  discovered?: any[];
  roadmap?: any;
  status?: string;
}): boolean {
  const db = getWritableSessionsDb();
  if (!db) return false;

  try {
    const sid = data.sessionId;
    const stdId = data.studentId || data.profile?.student_id || `std-${sid.slice(-8)}`;
    const now = new Date().toISOString();
    const status = data.status || "COMPLETED";

    // 1. Insert or replace student
    if (data.profile) {
      db.prepare(`
        INSERT INTO students (student_id, name, profile_json, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(student_id) DO UPDATE SET
          name = excluded.name,
          profile_json = excluded.profile_json,
          updated_at = excluded.updated_at
      `).run(
        stdId,
        data.profile.personal?.name || data.profile.name || "Student Applicant",
        JSON.stringify(data.profile),
        now,
        now
      );
    }

    // 2. Insert or replace session
    const topSc = data.discovered?.[0];
    const missionParamsJson = JSON.stringify({
      roadmap: data.roadmap || {},
      target_intake: data.profile?.personal?.target_intake || "Fall 2026",
    });

    db.prepare(`
      INSERT INTO sessions (session_id, student_id, mission_params_json, status, total_scanned, total_verified, top_scholarship, top_score, created_at, completed_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      ON CONFLICT(session_id) DO UPDATE SET
        mission_params_json = excluded.mission_params_json,
        status = excluded.status,
        top_scholarship = excluded.top_scholarship,
        top_score = excluded.top_score,
        completed_at = excluded.completed_at
    `).run(
      sid,
      stdId,
      missionParamsJson,
      status,
      data.discovered?.length || 0,
      data.discovered?.length || 0,
      topSc?.name || null,
      topSc?.final_score || topSc?.compositeScore || null,
      now,
      now
    );

    // 3. Insert session scholarships
    if (Array.isArray(data.discovered) && data.discovered.length > 0) {
      const insertSc = db.prepare(`
        INSERT INTO session_scholarships (session_id, scholarship_id, eligibility_json, cost_json, deadline_json, verification_json, skeptic_json, final_score, rank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(session_id, scholarship_id) DO UPDATE SET
          final_score = excluded.final_score,
          rank = excluded.rank,
          cost_json = excluded.cost_json,
          deadline_json = excluded.deadline_json
      `);

      for (let i = 0; i < data.discovered.length; i++) {
        const sc = data.discovered[i];
        const scId = sc.scholarship_id || sc.id;
        if (!scId) continue;

        insertSc.run(
          sid,
          scId,
          JSON.stringify((sc as any).eligibility_analysis || {}),
          JSON.stringify((sc as any).cost_analysis || (sc as any).fundingSummary || {}),
          JSON.stringify((sc as any).deadline_analysis || (sc as any).deadlineSummary || {}),
          JSON.stringify({ verified: true }),
          JSON.stringify({}),
          sc.final_score || sc.compositeScore || 90.0,
          sc.rank || (i + 1)
        );
      }
    }

    return true;
  } catch (err) {
    console.error("[SQLite] Error saving session to DB:", err);
    return false;
  }
}
