import europeData from "./data/scholarships/europe.json";
import asiaData from "./data/scholarships/asia.json";
import americasData from "./data/scholarships/americas.json";
import menaData from "./data/scholarships/mena.json";
import oceaniaData from "./data/scholarships/oceania.json";

import bsGrad from "./data/profiles/bs_graduate.json";
import fscStudent from "./data/profiles/fsc_student.json";
import bbaGrad from "./data/profiles/bba_graduate.json";
import icsStudent from "./data/profiles/ics_student.json";
import workProf from "./data/profiles/working_professional.json";
import cambridgeStudent from "./data/profiles/cambridge_student.json";

import { Scholarship, StudentProfile, Region } from "./types";
import { percentageToGpa4 } from "./utils/gpaScale";

export function normalizeProfile(p: any): StudentProfile {
  const hasEngTest = p.language?.has_english_test !== false &&
    p.language?.english_proficiency_test &&
    !p.language.english_proficiency_test.toLowerCase().includes("none") &&
    !p.language.english_proficiency_test.toLowerCase().includes("not available");

  const city = p.personal?.city || p.personal?.current_city || "Islamabad";
  const targetDegree = p.personal?.intended_degree || p.preferences?.target_degree_level || p.academic?.degree_level || "Bachelor's";
  const targetFields = p.personal?.target_fields || p.preferences?.target_fields || (p.academic?.field_of_study ? [p.academic.field_of_study] : []) || ["All Academic Disciplines"];
  const rawRegions = p.preferences?.preferred_regions || p.preferences?.preferredRegions || p.personal?.target_regions || p.personal?.targetRegions;
  const targetRegions = Array.isArray(rawRegions) && rawRegions.length > 0
    ? rawRegions
    : ["Europe", "Asia", "Americas", "MENA", "Oceania"];
  const maxBudget = p.financial?.max_out_of_pocket_pkr ?? p.preferences?.max_out_of_pocket_pkr ?? 150000;
  const fundingReq = p.financial?.funding_requirement || p.preferences?.funding_requirement || "FULL";

  return {
    student_id: p.student_id || "std-pk-001",
    session_id: p.session_id || "sess-demo",
    personal: {
      name: p.personal?.name || p.name || "Student Applicant",
      nationality: p.personal?.nationality || "PK",
      city: city,
      current_city: city,
      target_intake: p.personal?.target_intake || "Fall 2026",
      intended_degree: targetDegree,
      target_fields: targetFields,
      target_regions: targetRegions,
    },
    academic: {
      current_level: p.academic?.current_level || p.academic?.degree_level || "Undergraduate / Intermediate",
      degree_level: targetDegree,
      education_system: p.academic?.education_system || "PAKISTANI_HSSC",
      field_of_study: p.academic?.field_of_study || targetFields[0] || "All Academic Disciplines",
      institution: p.academic?.institution || p.academic?.board_university || "Recognized Pakistani Institution",
      grading_system: p.academic?.grading_system || (p.academic?.gpa_4_scale ? "GPA_4" : "PERCENTAGE"),
      a_level_grades: p.academic?.a_level_grades || undefined,
      o_level_grades: p.academic?.o_level_grades || undefined,
      ibcc_equivalence_percentage: p.academic?.ibcc_equivalence_percentage ?? undefined,
      ibcc_total_marks: p.academic?.ibcc_total_marks ?? undefined,
      gpa_obtained: p.academic?.gpa_obtained ?? p.academic?.gpa_4_scale ?? null,
      gpa_4_scale: p.academic?.gpa_4_scale ?? p.academic?.gpa_obtained ?? percentageToGpa4(Number(p.academic?.percentage ?? p.academic?.gpa_percentage ?? 85)),
      percentage: Number(p.academic?.percentage ?? p.academic?.gpa_percentage ?? 85),
      gpa_percentage: Number(p.academic?.gpa_percentage ?? p.academic?.percentage ?? 85),
      graduation_year: p.academic?.graduation_year || 2026,
    },
    language: {
      test_type: hasEngTest ? (p.language?.test_type || p.language?.english_proficiency_test || "IELTS") : "NONE",
      english_proficiency_test: hasEngTest ? (p.language?.english_proficiency_test || p.language?.test_type || "IELTS") : "NONE",
      overall_score: hasEngTest ? (p.language?.overall_score ?? p.language?.ielts_overall ?? 7.0) : null,
      ielts_overall: hasEngTest ? (p.language?.ielts_overall ?? p.language?.overall_score ?? 7.0) : null,
      has_english_medium_certificate: p.language?.has_english_medium_certificate ?? p.language?.medium_of_instruction_english ?? false,
      moi_certificate_available: p.language?.moi_certificate_available ?? p.language?.has_english_medium_certificate ?? false,
    },
    financial: {
      max_annual_contribution_pkr: p.financial?.max_annual_contribution_pkr ?? maxBudget,
      max_out_of_pocket_pkr: maxBudget,
      funding_requirement: fundingReq,
    },
    preferences: {
      target_degree_level: targetDegree,
      target_fields: targetFields,
      preferred_regions: targetRegions,
      max_out_of_pocket_pkr: maxBudget,
      funding_requirement: fundingReq,
      is_tax_filer: p.preferences?.is_tax_filer ?? true,
    },
    profile_completeness: p.profile_completeness || 90,
  };
}

export const SEED_SCHOLARSHIPS: Scholarship[] = [
  ...((europeData as unknown) as Scholarship[]),
  ...((asiaData as unknown) as Scholarship[]),
  ...((americasData as unknown) as Scholarship[]),
  ...((menaData as unknown) as Scholarship[]),
  ...((oceaniaData as unknown) as Scholarship[]),
];

export const SEED_PROFILES: StudentProfile[] = [
  normalizeProfile(icsStudent), // 1st Profile: Hamza Gohar (ICS CS 93%), PAEC Boys College Chashma, Multan
  normalizeProfile(fscStudent), // 2nd Profile: Malik Hassan, Govt Emerson College, Multan
  normalizeProfile(bsGrad),     // 3rd Profile: Muhammad, NUST Islamabad
  normalizeProfile(bbaGrad),
  normalizeProfile(workProf),
  normalizeProfile(cambridgeStudent), // 6th Profile: Aisha Siddiqui (Cambridge A-Levels, KGS Karachi, 87.2% IBCC)
];

export function getScholarshipsByRegion(region: Region): Scholarship[] {
  return SEED_SCHOLARSHIPS.filter((s) => s.region === region);
}

export function getScholarshipById(id: string): Scholarship | undefined {
  return SEED_SCHOLARSHIPS.find((s) => s.scholarship_id === id);
}

export function searchScholarships(query: string, region?: Region): Scholarship[] {
  const q = query.toLowerCase().trim();
  return SEED_SCHOLARSHIPS.filter((s) => {
    if (region && s.region !== region) return false;
    if (!q) return true;
    return (
      s.name.toLowerCase().includes(q) ||
      s.host_country_name.toLowerCase().includes(q) ||
      (s.host_institution && s.host_institution.toLowerCase().includes(q)) ||
      (s.description && s.description.toLowerCase().includes(q))
    );
  });
}

// Domain academic taxonomy mapping for intelligent discipline alignment
const TAXONOMY_MAP: Record<string, string[]> = {
  physics: ["physics", "physical", "materials", "material", "nanotechnology", "optics", "quantum", "condensed", "natural sciences", "stem", "engineering", "all fields", "all disciplines", "open to all"],
  "material physics": ["physics", "material", "materials", "materials science", "physical sciences", "nanotechnology", "condensed matter", "stem", "natural sciences", "engineering", "all fields", "all disciplines"],
  "materials science": ["materials", "material", "physics", "chemistry", "nanotechnology", "metallurgy", "engineering", "stem", "all fields", "all disciplines"],
  chemistry: ["chemistry", "chemical", "materials", "physical sciences", "biochemistry", "stem", "natural sciences", "all fields", "all disciplines"],
  biology: ["biology", "biological", "biomedical", "biotechnology", "life sciences", "genetics", "stem", "natural sciences", "all fields"],
  medicine: ["medicine", "medical", "clinical", "health", "biomedical", "pharmacy", "life sciences", "all fields"],
  mathematics: ["mathematics", "math", "statistics", "data science", "computational", "stem", "all fields", "all disciplines"],
  computer: ["computer", "computing", "software", "information technology", "data science", "artificial intelligence", "ai", "cyber", "stem", "all fields"],
  "computer science": ["computer", "computing", "software", "information technology", "data science", "artificial intelligence", "ai", "cyber", "stem", "all fields"],
  engineering: ["engineering", "mechanical", "electrical", "civil", "chemical", "aerospace", "industrial", "mechatronics", "stem", "all fields"],
  business: ["business", "management", "administration", "commerce", "finance", "accounting", "marketing", "mba", "social sciences", "all fields"],
  economics: ["economics", "econometrics", "finance", "social sciences", "development", "public policy", "all fields"],
  humanities: ["humanities", "arts", "history", "philosophy", "languages", "literature", "social sciences", "all fields"],
  law: ["law", "legal", "jurisprudence", "human rights", "social sciences", "all fields"],
};

export function searchScholarshipsForProfile(profile: any, limit: number = 25): Scholarship[] {
  if (!profile) return SEED_SCHOLARSHIPS.slice(0, limit);

  const rawDegree = String(
    profile.preferences?.target_degree_level ||
    profile.preferences?.targetDegreeLevel ||
    profile.personal?.intended_degree ||
    profile.academic?.target_degree_level ||
    profile.target_degree ||
    profile.degree ||
    profile.academic?.degree_level ||
    profile.academic?.current_level ||
    "Bachelor's"
  ).toLowerCase();

  const isUndergrad = /bachelor|undergrad|bs|fsc|ics|inter|a-level|diploma|bba|b\.e|b\.com|ll\.b/i.test(rawDegree);
  const isPhd = /phd|doctor|doctoral|dphil/i.test(rawDegree) && !/pharm[\s\-]?d|doctor of pharmacy|doctor of physical therapy|dpt/i.test(rawDegree);
  const isMaster = !isUndergrad && !isPhd;

  const targetFields: string[] = (
    profile.preferences?.target_fields ||
    (profile.academic?.field_of_study ? [profile.academic.field_of_study] : []) ||
    ["All Academic Disciplines"]
  ).map((f: string) => f.toLowerCase().trim()).filter(Boolean);

  const rawPref =
    profile.preferences?.preferred_regions ||
    profile.preferences?.preferredRegions ||
    profile.personal?.target_regions ||
    profile.personal?.targetRegions ||
    [];
  const preferredRegions: string[] = (Array.isArray(rawPref) ? rawPref : [rawPref])
    .map((r: string) => String(r).toLowerCase().trim())
    .filter(Boolean);

  const studentGpa = Number(profile.academic?.gpa_percentage || profile.academic?.percentage || 80);
  const studentGpa4 = Number(profile.academic?.gpa_4_scale || profile.academic?.gpa_obtained || 3.5);
  const hasIelts = Boolean(
    profile.language?.has_english_test ||
    (profile.language?.english_proficiency_test && !/none|not available/i.test(profile.language.english_proficiency_test))
  );
  const maxBudget = Number(profile.preferences?.max_out_of_pocket_pkr || profile.financial?.max_out_of_pocket_pkr || 150000);

  const scored: { sc: Scholarship; score: number }[] = [];

  for (const s of SEED_SCHOLARSHIPS) {
    // 1. Pakistan Eligibility
    if (s.pakistan_requirements && s.pakistan_requirements.pakistan_eligible === false) {
      continue;
    }

    // 2. Strict Degree Match
    const offeredDegs = (s.eligibility?.degree_levels || []).map((d) => d.toLowerCase());
    const degStr = offeredDegs.join(" ");

    if (isUndergrad) {
      const match = /bachelor|undergrad|bs|diploma|bba|b\.e|b\.com|ll\.b/i.test(degStr);
      if (!match) continue;
    } else if (isPhd) {
      const match = /phd|doctor|doctoral|dphil/i.test(degStr);
      if (!match) continue;
    } else if (isMaster) {
      const match = /master|ms|msc|mphil|graduate|postgrad/i.test(degStr);
      if (!match) continue;
    }

    let score = 0;

    // 3. Strict Region Filter (Absolute Elimination Gate)
    const scRegion = s.region.toLowerCase().trim();
    if (preferredRegions.length > 0) {
      const isMatch = preferredRegions.some((r) => {
        if (r === scRegion) return true;
        if (r === "europe" && (scRegion.includes("europe") || scRegion === "uk/europe")) return true;
        if (r === "asia" && (scRegion.includes("asia") || scRegion === "east asia" || scRegion === "south asia" || scRegion === "central asia")) return true;
        if (r === "americas" && (scRegion.includes("america") || scRegion === "north america" || scRegion === "south america" || scRegion === "usa")) return true;
        if (r === "mena" && (scRegion.includes("mena") || scRegion.includes("middle east"))) return true;
        if (r === "oceania" && (scRegion.includes("oceania") || scRegion.includes("australia"))) return true;
        return false;
      });
      if (!isMatch) {
        continue; // HARD FILTER: Absolutely eliminate all scholarships outside user-selected continents
      }
      score += 25;
    } else {
      score += 15;
    }

    // 4. Field of Study Alignment
    const eligibleFields = (s.eligibility?.eligible_fields || []).map((f) => f.toLowerCase());
    const efStr = eligibleFields.join(" ");
    const nameStr = s.name.toLowerCase();

    const isUniversal = /all fields|all disciplines|any discipline|open to all|all subjects|bilateral program/i.test(
      efStr + " " + nameStr
    );

    let fieldMatched = isUniversal;
    let fieldScore = isUniversal ? 0.8 : 0;

    for (const tf of targetFields) {
      if (isUniversal || efStr.includes(tf) || nameStr.includes(tf)) {
        fieldMatched = true;
        fieldScore = Math.max(fieldScore, 1.0);
        break;
      }

      // Check domain taxonomy mapping
      const relatedTerms = TAXONOMY_MAP[tf] || [];
      for (const term of relatedTerms) {
        if (efStr.includes(term) || nameStr.includes(term)) {
          fieldMatched = true;
          fieldScore = Math.max(fieldScore, 0.9);
          break;
        }
      }
      if (fieldMatched) break;

      // Check partial token overlap (words > 3 chars)
      const tokens = tf.split(/\s+/).filter((w) => w.length > 3);
      for (const tok of tokens) {
        if (efStr.includes(tok) || nameStr.includes(tok)) {
          fieldMatched = true;
          fieldScore = Math.max(fieldScore, 0.8);
          break;
        }
        // Check taxonomy of token
        const tokTerms = TAXONOMY_MAP[tok] || [];
        for (const tt of tokTerms) {
          if (efStr.includes(tt) || nameStr.includes(tt)) {
            fieldMatched = true;
            fieldScore = Math.max(fieldScore, 0.85);
            break;
          }
        }
        if (fieldMatched) break;
      }
      if (fieldMatched) break;
    }

    if (!fieldMatched && eligibleFields.length > 0) {
      continue;
    }

    score += (fieldScore || 0.7) * 35;

    // 5. Bilateral Quota Bonus
    if (s.pakistan_requirements?.pakistan_bilateral_quota) {
      score += 20;
    } else {
      score += 10;
    }

    // 6. GPA Cutoff Compatibility
    const minGpaPct = s.eligibility?.min_gpa_percentage;
    const minGpa4 = s.eligibility?.min_gpa_4_scale;

    if (minGpaPct && studentGpa < minGpaPct) {
      score -= 20;
    } else if (minGpa4 && studentGpa4 < minGpa4) {
      score -= 20;
    } else {
      score += 10;
    }

    // 7. Language Compatibility
    const reqIelts = Boolean(s.language?.english_test_required && s.language?.minimum_ielts);
    const acceptsMoi = Boolean(s.pakistan_requirements?.accepts_moi_certificate);

    if (hasIelts) {
      score += 10;
    } else if (acceptsMoi || !reqIelts) {
      score += 10; // Student has no IELTS, but this scholarship accepts MOI
    } else {
      score -= 10;
    }

    // 8. Budget Fit
    if (s.funding?.funding_type === "FULL") {
      score += 10;
    } else if (maxBudget >= 250000) {
      score += 6;
    } else {
      score += 2;
    }

    scored.push({ sc: s, score });
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, limit).map((x) => x.sc);
}

