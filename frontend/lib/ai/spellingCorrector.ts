import { groqPool } from "./groqClient";

export interface StudentInputFields {
  fieldOfStudy?: string;
  studentName?: string;
  city?: string;
  institution?: string;
  targetDegree?: string;
}

export interface SpellingCorrectionResult {
  corrected: StudentInputFields;
  correctionsMade: boolean;
  changes: Record<string, { from: string; to: string }>;
}

// Fast dictionary for instantaneous Pakistani academic spelling corrections
const FAST_FIELD_DICT: Record<string, string> = {
  "compter scince": "Computer Science",
  "computr scince": "Computer Science",
  "computer scence": "Computer Science",
  "cs": "Computer Science",
  "se": "Software Engineering",
  "softwre enginering": "Software Engineering",
  "software eng": "Software Engineering",
  "ai": "Artificial Intelligence",
  "artifcial intelgence": "Artificial Intelligence",
  "artificial intellegence": "Artificial Intelligence",
  "artifical intelligence": "Artificial Intelligence",
  "ds": "Data Science",
  "data scince": "Data Science",
  "data scence": "Data Science",
  "machne lerning": "Machine Learning",
  "ml": "Machine Learning",
  "cybr security": "Cybersecurity",
  "cyber secrity": "Cybersecurity",
  "electrcial engenering": "Electrical Engineering",
  "electrical engr": "Electrical Engineering",
  "electrical engg": "Electrical Engineering",
  "ee": "Electrical Engineering",
  "mechanical engg": "Mechanical Engineering",
  "me": "Mechanical Engineering",
  "civil engg": "Civil Engineering",
  "ce": "Civil Engineering",
  "bussines admistration": "Business Administration",
  "bba": "Business Administration",
  "mba": "Business Administration",
  "finence": "Finance",
  "econmics": "Economics",
  "biomdical": "Biomedical Engineering",
};

const FAST_CITY_DICT: Record<string, string> = {
  "lahor": "Lahore",
  "karhci": "Karachi",
  "krachi": "Karachi",
  "islambad": "Islamabad",
  "isb": "Islamabad",
  "rawalpndi": "Rawalpindi",
  "rwp": "Rawalpindi",
  "faislabad": "Faisalabad",
  "fsd": "Faisalabad",
  "multn": "Multan",
  "peshawr": "Peshawar",
  "quetta": "Quetta",
  "sialkot": "Sialkot",
  "gujranwala": "Gujranwala",
  "abbottabad": "Abbottabad",
};

export async function correctStudentInputDeterministically(
  input: StudentInputFields
): Promise<SpellingCorrectionResult> {
  const corrected: StudentInputFields = { ...input };
  const changes: Record<string, { from: string; to: string }> = {};

  // 1. Fast dictionary pre-check
  if (input.fieldOfStudy) {
    const rawLower = input.fieldOfStudy.trim().toLowerCase();
    if (FAST_FIELD_DICT[rawLower]) {
      changes.fieldOfStudy = { from: input.fieldOfStudy, to: FAST_FIELD_DICT[rawLower] };
      corrected.fieldOfStudy = FAST_FIELD_DICT[rawLower];
    }
  }

  if (input.city) {
    const rawLower = input.city.trim().toLowerCase();
    if (FAST_CITY_DICT[rawLower]) {
      changes.city = { from: input.city, to: FAST_CITY_DICT[rawLower] };
      corrected.city = FAST_CITY_DICT[rawLower];
    }
  }

  // 2. Format name casing directly
  if (input.studentName && input.studentName.trim()) {
    const trimmed = input.studentName.trim();
    const titleCased = trimmed
      .split(/\s+/)
      .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
      .join(" ");
    if (titleCased !== trimmed && trimmed.toLowerCase() === titleCased.toLowerCase()) {
      changes.studentName = { from: trimmed, to: titleCased };
      corrected.studentName = titleCased;
    }
  }

  // 3. If there are inputs needing AI spelling analysis
  const needsAiCheck =
    Boolean(input.fieldOfStudy && !changes.fieldOfStudy) ||
    Boolean(input.institution && input.institution.trim().length > 2);

  if (needsAiCheck && groqPool.getKeyCount() > 0) {
    try {
      const prompt = `You are a deterministic spelling correction engine for student admission profiles.
Correct typographical errors, misspellings, and standard casing in the provided JSON fields.
CRITICAL RULES:
- Correct only genuine misspellings (e.g. "machne lerning" -> "Machine Learning", "compter scince" -> "Computer Science").
- Do NOT change the meaning or replace specific academic disciplines with unrelated ones.
- Preserve proper nouns and acronyms (e.g. NUST, FAST, LUMS, HEC, GIKI, UET).
- Respond ONLY with a valid JSON object matching the input keys.

Input fields:
${JSON.stringify({
  fieldOfStudy: corrected.fieldOfStudy || "",
  institution: corrected.institution || "",
  city: corrected.city || "",
})}`;

      const res = await groqPool.chatCompletion({
        messages: [
          {
            role: "system",
            content: "You are a deterministic spelling corrector. Return only JSON with corrected values.",
          },
          { role: "user", content: prompt },
        ],
        temperature: 0.0,
        max_tokens: 150,
        json_mode: true,
      });

      const parsed = JSON.parse(res.content);

      if (parsed.fieldOfStudy && typeof parsed.fieldOfStudy === "string" && parsed.fieldOfStudy.trim()) {
        const aiField = parsed.fieldOfStudy.trim();
        if (aiField.toLowerCase() !== (corrected.fieldOfStudy || "").toLowerCase() || aiField !== corrected.fieldOfStudy) {
          // Verify it didn't completely hallucinate by comparing length/similarity
          if (aiField.length >= 2 && Math.abs(aiField.length - (corrected.fieldOfStudy || "").length) < 15) {
            changes.fieldOfStudy = { from: corrected.fieldOfStudy || "", to: aiField };
            corrected.fieldOfStudy = aiField;
          }
        }
      }

      if (parsed.institution && typeof parsed.institution === "string" && parsed.institution.trim()) {
        const aiInst = parsed.institution.trim();
        if (aiInst.toLowerCase() !== (corrected.institution || "").toLowerCase() || aiInst !== corrected.institution) {
          changes.institution = { from: corrected.institution || "", to: aiInst };
          corrected.institution = aiInst;
        }
      }
    } catch (err) {
      console.warn("[SpellingCorrector] Groq fallback error:", err);
      // Fallback preserves input
    }
  }

  const correctionsMade = Object.keys(changes).length > 0;
  return { corrected, correctionsMade, changes };
}
