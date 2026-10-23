"use client";

import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Shield,
  Compass,
  ArrowRight,
  Sparkles,
  History,
  CheckCircle2,
  AlertCircle,
  GraduationCap,
  Globe2,
  Banknote,
  Languages,
  BookOpen,
  MapPin,
  Play,
  RotateCcw,
  Trash2,
  Award,
  Building2,
  Sliders,
  Database,
} from "lucide-react";
import Link from "next/link";
import { Region, StudentProfile } from "@/lib/types";
import { listSessions, deleteSession, checkBackendHealth } from "@/lib/api";
import { percentageToGpa4, gpaToPercentage } from "@/lib/utils/gpaScale";
import { WorldStage } from "@/components/theatre/world/WorldStage";
import { AtmosphericBackground } from "@/components/theatre/AtmosphericBackground";

export interface MissionInitScreenProps {
  onLaunchMission: (profile: any, sessionId: string) => void;
  onLaunchDemo: () => void;
  onResumeMission: (sessionId: string) => void;
}

interface PresetOption {
  id: string;
  name: string;
  subtitle: string;
  degree: string;
  field: string;
  gpaPercentage: number;
  gpa4Scale: number;
  educationLevel: string;
  institution: string;
  city: string;
  province: string;
  englishTest: string;
  ieltsScore: number | null;
  hasMoi: boolean;
  usatHatScore?: string;
  fundingReq: string;
  budgetPkr: number;
  preferredRegions: Region[];
  educationStream?: "PAKISTANI_HSSC" | "CAMBRIDGE";
  aLevelGrades?: string[];
  badge?: string;
  board?: string;
}

const PAKISTANI_CITIES: { name: string; province: string }[] = [
  { name: "Lahore", province: "Punjab" },
  { name: "Karachi", province: "Sindh" },
  { name: "Islamabad", province: "ICT" },
  { name: "Rawalpindi", province: "Punjab" },
  { name: "Faisalabad", province: "Punjab" },
  { name: "Multan", province: "Punjab" },
  { name: "Peshawar", province: "KPK" },
  { name: "Quetta", province: "Balochistan" },
  { name: "Sialkot", province: "Punjab" },
  { name: "Gujranwala", province: "Punjab" },
  { name: "Hyderabad", province: "Sindh" },
  { name: "Abbottabad", province: "KPK" },
  { name: "Bahawalpur", province: "Punjab" },
  { name: "Sukkur", province: "Sindh" },
  { name: "Gilgit", province: "Gilgit-Baltistan" },
  { name: "Skardu", province: "Gilgit-Baltistan" },
  { name: "Muzaffarabad", province: "AJK" },
  { name: "Mirpur", province: "AJK" },
  { name: "Mardan", province: "KPK" },
  { name: "Swat", province: "KPK" },
  { name: "Sahiwal", province: "Punjab" },
  { name: "Sargodha", province: "Punjab" },
  { name: "D.I. Khan", province: "KPK" },
  { name: "D.G. Khan", province: "Punjab" },
  { name: "Larkana", province: "Sindh" },
  { name: "Nawabshah", province: "Sindh" },
  { name: "Wah Cantt", province: "Punjab" },
  { name: "Taxila", province: "Punjab" },
  { name: "Jhelum", province: "Punjab" },
  { name: "Chiniot", province: "Punjab" },
  { name: "Kasur", province: "Punjab" },
  { name: "Sheikhupura", province: "Punjab" },
];

const PAKISTANI_INSTITUTIONS: string[] = [
  "Karachi Grammar School (KGS)",
  "Aitchison College, Lahore",
  "The Lyceum, Karachi",
  "Cedar College, Karachi",
  "Roots Millennium College, Islamabad",
  "Beaconhouse College Programme (Margalla / Defence)",
  "Lahore Grammar School (LGS Defense / JT)",
  "Froebel's International School, Islamabad",
  "PAEC Boys College Chashma",
  "Government College University (GCU), Lahore",
  "National University of Sciences & Technology (NUST), Islamabad",
  "Lahore University of Management Sciences (LUMS), Lahore",
  "FAST - National University of Computer and Emerging Sciences",
  "University of Engineering and Technology (UET), Lahore",
  "COMSATS University Islamabad",
  "University of the Punjab (PU), Lahore",
  "Ghulam Ishaq Khan Institute (GIKI), Topi",
  "Institute of Business Administration (IBA), Karachi",
  "NED University of Engineering and Technology, Karachi",
  "Aga Khan University (AKU), Karachi",
  "Pakistan Institute of Engineering and Applied Sciences (PIEAS), Islamabad",
  "Quaid-i-Azam University (QAU), Islamabad",
  "Govt Emerson College, Multan",
  "Islamia College University, Peshawar",
  "University of Karachi (UoK)",
  "Forman Christian College (FCCU), Lahore",
  "Army Public College (APSACS), Rawalpindi / Multan",
  "Cadet College Hasanabdal",
  "Kinnaird College for Women, Lahore",
];

export const PAKISTANI_BOARDS: string[] = [
  "FBISE - Federal Board of Intermediate and Secondary Education, Islamabad",
  "BISE Lahore (Punjab)",
  "BISE Rawalpindi (Punjab)",
  "BISE Multan (Punjab)",
  "BISE Faisalabad (Punjab)",
  "BISE Gujranwala (Punjab)",
  "BISE Sargodha (Punjab)",
  "BISE Sahiwal (Punjab)",
  "BISE Bahawalpur (Punjab)",
  "BISE D.G. Khan (Punjab)",
  "BIEK Karachi - Board of Intermediate Education Karachi (Sindh)",
  "BISE Hyderabad (Sindh)",
  "BISE Sukkur (Sindh)",
  "BISE Larkana (Sindh)",
  "BISE Mirpurkhas (Sindh)",
  "BISE Shaheed Benazirabad / Nawabshah (Sindh)",
  "BISE Peshawar (KPK)",
  "BISE Abbottabad (KPK)",
  "BISE Mardan (KPK)",
  "BISE Swat / Malakand (KPK)",
  "BISE Kohat (KPK)",
  "BISE Bannu (KPK)",
  "BISE D.I. Khan (KPK)",
  "BISE Quetta (Balochistan)",
  "BISE Mirpur (Azad Jammu & Kashmir - AJK)",
  "KIU Examination Board (Gilgit-Baltistan)",
  "Punjab Board of Technical Education (PBTE), Lahore",
  "Higher Education Commission (HEC) Recognized University",
];

const STUDY_FIELDS: string[] = [
  "Computer Science",
  "Artificial Intelligence & Machine Learning",
  "Data Science & Analytics",
  "Software Engineering",
  "Cyber Security",
  "Electrical & Electronics Engineering",
  "Mechanical & Mechatronics Engineering",
  "Biotechnology & Bioinformatics",
  "Business Administration & Management",
  "Economics & Public Policy",
  "Medicine, Public Health & Biomedical Sciences",
  "Physics & Material Science",
  "Civil & Environmental Engineering",
];

const PRESETS: PresetOption[] = [
  {
    id: "preset-ics",
    name: "Hamza Gohar",
    subtitle: "ICS CS • 93% (3.72 GPA) • Multan",
    degree: "Bachelor's",
    field: "Computer Science",
    gpaPercentage: 93.0,
    gpa4Scale: 3.72,
    board: "FBISE - Federal Board of Intermediate and Secondary Education, Islamabad",
    educationLevel: "Intermediate / ICS / FSc / FA",
    institution: "PAEC Boys College Chashma",
    city: "Multan",
    province: "Punjab",
    englishTest: "None / Not Available",
    ieltsScore: null,
    hasMoi: false,
    usatHatScore: "",
    fundingReq: "FULL",
    budgetPkr: 150000,
    preferredRegions: ["Europe", "Asia", "MENA"],
  },
  {
    id: "malik-hassan",
    name: "Malik Hassan",
    subtitle: "FSc Pre-Eng • 78.5% (3.14 GPA) • Multan",
    degree: "Bachelor's",
    field: "Artificial Intelligence",
    gpaPercentage: 78.5,
    gpa4Scale: 3.14,
    board: "BISE Multan (Punjab)",
    educationLevel: "Intermediate / ICS / FSc / FA",
    institution: "Govt Emerson College, Multan",
    city: "Multan",
    province: "Punjab",
    englishTest: "Medium of Instruction (MOI) Certificate",
    ieltsScore: null,
    hasMoi: true,
    usatHatScore: "",
    fundingReq: "FULL",
    budgetPkr: 100000,
    preferredRegions: ["Europe", "Asia", "MENA"],
  },
  {
    id: "aisha-cambridge",
    name: "Aisha Siddiqui",
    subtitle: "A-Levels (A*AA) • 86.7% • KGS",
    badge: "CAMBRIDGE A-LEVELS",
    degree: "Bachelor's",
    field: "Computer Science",
    gpaPercentage: 86.7,
    gpa4Scale: 3.47,
    board: "Cambridge Assessment International Education (CIE)",
    educationLevel: "A-Levels / Cambridge / Edexcel",
    institution: "Karachi Grammar School (KGS)",
    city: "Karachi",
    province: "Sindh",
    englishTest: "IELTS",
    ieltsScore: 8.0,
    hasMoi: true,
    usatHatScore: "",
    fundingReq: "FULL",
    budgetPkr: 300000,
    preferredRegions: ["Europe", "Americas", "Asia"],
    educationStream: "CAMBRIDGE",
    aLevelGrades: ["A*", "A", "A"],
  },
  {
    id: "muhammad-bs",
    name: "Muhammad",
    subtitle: "BS CS • 3.8 GPA • NUST Islamabad",
    degree: "Master's",
    field: "Data Science & Machine Learning",
    gpaPercentage: 88.5,
    gpa4Scale: 3.8,
    board: "Higher Education Commission (HEC) Recognized University",
    educationLevel: "Bachelor's / BS / BE / BBA",
    institution: "National University of Sciences & Technology (NUST), Islamabad",
    city: "Islamabad",
    province: "ICT",
    englishTest: "IELTS",
    ieltsScore: 7.5,
    hasMoi: true,
    usatHatScore: "82",
    fundingReq: "FULL",
    budgetPkr: 300000,
    preferredRegions: ["Europe", "Americas", "Asia", "Oceania"],
    educationStream: "PAKISTANI_HSSC",
  },
];

export const MissionInitScreen: React.FC<MissionInitScreenProps> = ({
  onLaunchMission,
  onLaunchDemo,
  onResumeMission,
}) => {
  const [selectedPresetId, setSelectedPresetId] = useState<string>("preset-ics");
  const [isCustom, setIsCustom] = useState<boolean>(false);

  // Form State - Candidate Identity
  const [studentName, setStudentName] = useState<string>("Hamza Gohar");
  const [city, setCity] = useState<string>("Multan");
  const [province, setProvince] = useState<string>("Punjab");

  // Form State - Academic Background & Stream
  const [educationStream, setEducationStream] = useState<"PAKISTANI_HSSC" | "CAMBRIDGE">("PAKISTANI_HSSC");
  const [institution, setInstitution] = useState<string>("PAEC Boys College Chashma");
  const [board, setBoard] = useState<string>("FBISE - Federal Board of Intermediate and Secondary Education, Islamabad");
  const [educationLevel, setEducationLevel] = useState<string>("Intermediate / ICS / FSc / FA");
  const [graduationYear, setGraduationYear] = useState<number>(2026);
  const [targetDegree, setTargetDegree] = useState<string>("Bachelor's");
  const [fieldOfStudy, setFieldOfStudy] = useState<string>("Computer Science");

  // Cambridge A-Levels Specific State
  const [aLevelSubject1, setALevelSubject1] = useState<string>("Mathematics");
  const [aLevelGrade1, setALevelGrade1] = useState<string>("A*");
  const [aLevelSubject2, setALevelSubject2] = useState<string>("Physics");
  const [aLevelGrade2, setALevelGrade2] = useState<string>("A");
  const [aLevelSubject3, setALevelSubject3] = useState<string>("Computer Science");
  const [aLevelGrade3, setALevelGrade3] = useState<string>("A");
  const [manualMarksOverride, setManualMarksOverride] = useState<boolean>(false);

  // Form State - Scores
  const [gpaPercentage, setGpaPercentage] = useState<number>(93.0);
  const [gpa4Scale, setGpa4Scale] = useState<number>(3.72);

  // Helper: Official IBCC Equivalence Computation (A*=90, A=85, B=75, C=65, D=55, E=45, U=0)
  const computeIbccEquivalence = (g1: string, g2: string, g3: string) => {
    const gradePts: Record<string, number> = {
      "A*": 90,
      A: 85,
      B: 75,
      C: 65,
      D: 55,
      E: 45,
      U: 0,
    };
    const pts = [gradePts[g1] ?? 75, gradePts[g2] ?? 75, gradePts[g3] ?? 75];
    const avg = pts.reduce((a, b) => a + b, 0) / 3;
    const pct = parseFloat(avg.toFixed(1));
    const marks = Math.round((pct / 100) * 1100);
    const gpa = percentageToGpa4(pct);
    let division = "Grade A1 (Exceptional)";
    if (pct < 50) division = "Grade D (Passing)";
    else if (pct < 60) division = "Grade C (Second Division)";
    else if (pct < 70) division = "Grade B (First Division)";
    else if (pct < 80) division = "Grade A (Distinction)";
    return { pct, marks, gpa, division };
  };

  // Form State - Language & Tests
  const [englishOption, setEnglishOption] = useState<string>("None / Not Available");
  const [ieltsScore, setIeltsScore] = useState<number>(7.0);
  const [toeflScore, setToeflScore] = useState<number>(95);
  const [duolingoScore, setDuolingoScore] = useState<number>(125);
  const [hasMoi, setHasMoi] = useState<boolean>(false);
  const [usatHatScore, setUsatHatScore] = useState<string>("");

  // Form State - Financial & Regional
  const [fundingReq, setFundingReq] = useState<string>("FULL");
  const [budgetPkr, setBudgetPkr] = useState<number>(150000);
  const [selectedRegions, setSelectedRegions] = useState<Region[]>(["Europe", "Asia", "MENA"]);

  // Recent Missions
  const [recentSessions, setRecentSessions] = useState<any[]>([]);
  const [showRecentSessions, setShowRecentSessions] = useState<boolean>(false);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [backendStatus, setBackendStatus] = useState<"checking" | "online" | "offline">("checking");

  // Handle city selection with province auto-fill
  const handleCityChange = (newCity: string) => {
    setCity(newCity);
    setIsCustom(true);
    const matched = PAKISTANI_CITIES.find(
      (c) => c.name.toLowerCase() === newCity.trim().toLowerCase()
    );
    if (matched) {
      setProvince(matched.province);
    }
  };

  // Apply preset
  const applyPreset = (preset: PresetOption) => {
    setSelectedPresetId(preset.id);
    setIsCustom(false);
    setStudentName(preset.name);
    setTargetDegree(preset.degree);
    setFieldOfStudy(preset.field);
    setGpaPercentage(preset.gpaPercentage);
    setGpa4Scale(preset.gpa4Scale);
    setEducationLevel(preset.educationLevel);
    setCity(preset.city);
    setProvince(preset.province);
    setInstitution(preset.institution);
    if (preset.board) {
      setBoard(preset.board);
    } else if (preset.city) {
      setBoard(`BISE ${preset.city} (Punjab)`);
    }
    setEnglishOption(preset.englishTest);
    setIeltsScore(preset.ieltsScore || 7.0);
    setHasMoi(preset.hasMoi);
    setUsatHatScore(preset.usatHatScore !== undefined ? preset.usatHatScore : "");
    setFundingReq(preset.fundingReq);
    setBudgetPkr(preset.budgetPkr);
    setSelectedRegions(preset.preferredRegions);

    if (preset.educationStream) {
      setEducationStream(preset.educationStream);
      if (preset.educationStream === "CAMBRIDGE" && preset.aLevelGrades && preset.aLevelGrades.length >= 3) {
        setALevelGrade1(preset.aLevelGrades[0]);
        setALevelGrade2(preset.aLevelGrades[1]);
        setALevelGrade3(preset.aLevelGrades[2]);
        const eq = computeIbccEquivalence(preset.aLevelGrades[0], preset.aLevelGrades[1], preset.aLevelGrades[2]);
        setGpaPercentage(eq.pct);
        setGpa4Scale(eq.gpa);
      }
    } else {
      setEducationStream("PAKISTANI_HSSC");
    }
  };

  // Toggle Region
  const toggleRegion = (region: Region) => {
    setIsCustom(true);
    if (selectedRegions.includes(region)) {
      if (selectedRegions.length > 1) {
        setSelectedRegions(selectedRegions.filter((r) => r !== region));
      }
    } else {
      setSelectedRegions([...selectedRegions, region]);
    }
  };

  // Load Recent Missions & Check Backend Health
  useEffect(() => {
    listSessions(10)
      .then((res) => {
        if (res && Array.isArray(res.sessions)) {
          setRecentSessions(res.sessions);
        }
      })
      .catch((err) => {
        console.warn("Could not load recent missions:", err);
      });

    checkBackendHealth()
      .then((res) => {
        setBackendStatus(res.online ? "online" : "offline");
      })
      .catch(() => {
        setBackendStatus("offline");
      });
  }, []);

  const handleLaunch = async () => {
    setIsSubmitting(true);
    const newSessionId = `session-pk-${Date.now().toString(36)}`;
    const studentId = `std-pk-${Date.now().toString(36).slice(-6)}`;

    let cleanField = fieldOfStudy.trim();
    let cleanName = studentName.trim();
    try {
      const normRes = await fetch("/api/profile/normalize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fieldOfStudy: cleanField, studentName: cleanName, city, institution, targetDegree }),
      });
      if (normRes.ok) {
        const normData = await normRes.json();
        if (normData.corrected?.fieldOfStudy) cleanField = normData.corrected.fieldOfStudy;
        if (normData.corrected?.studentName) cleanName = normData.corrected.studentName;
      }
    } catch {
      // non-blocking fallback
    }

    const rawUsat = (usatHatScore || "").trim();
    const parsedUsatHat = rawUsat ? parseFloat(rawUsat) : NaN;

    const profilePayload: any = {
      student_id: studentId,
      session_id: newSessionId,
      personal: {
        name: cleanName || "Applicant",
        nationality: "PK",
        country_of_residence: "PK",
        city: city.trim() || "Islamabad",
        province: province || "Federal",
        age: targetDegree === "Bachelor's" ? 18 : targetDegree === "Master's" ? 23 : 26,
        target_regions: selectedRegions,
      },
      academic: {
        current_level: educationLevel,
        degree_level: targetDegree,
        target_degree_level: targetDegree,
        education_system: educationStream === "CAMBRIDGE" ? "CAMBRIDGE" : "PAKISTANI_HSSC",
        years_of_education: educationLevel.includes("Intermediate") || educationLevel.includes("A-Levels")
          ? 12
          : educationLevel.includes("Bachelor")
          ? 16
          : 18,
        field_of_study: cleanField || "All Academic Disciplines",
        board_university: educationStream === "CAMBRIDGE"
          ? "Cambridge Assessment International Education (CIE)"
          : (board.trim() || institution || (city ? `BISE ${city.trim()}` : "Federal Board of Intermediate and Secondary Education (FBISE), Islamabad")),
        gpa_percentage: educationStream === "CAMBRIDGE"
          ? computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3).pct
          : Math.min(100, Math.max(0, Number(gpaPercentage) || 85.0)),
        gpa_4_scale: educationStream === "CAMBRIDGE"
          ? computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3).gpa
          : Math.min(4.0, Math.max(0, Number(gpa4Scale) || percentageToGpa4(gpaPercentage))),
        institution: institution || (educationStream === "CAMBRIDGE" ? "Cambridge International School" : "Recognized Pakistani Institution"),
        grading_system: educationStream === "CAMBRIDGE" ? "CAMBRIDGE_LETTER_GRADES" : "PERCENTAGE",
        a_level_grades: educationStream === "CAMBRIDGE" ? [aLevelGrade1, aLevelGrade2, aLevelGrade3] : undefined,
        ibcc_equivalence_percentage: educationStream === "CAMBRIDGE"
          ? computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3).pct
          : undefined,
        ibcc_total_marks: educationStream === "CAMBRIDGE"
          ? computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3).marks
          : undefined,
        graduation_year: graduationYear,
        gap_years: 0,
        hec_attestation_done: false,
        ibcc_equivalence_done: false,
      },
      language: {
        english_proficiency_test: englishOption,
        ielts_overall: englishOption === "IELTS" && ieltsScore ? Number(ieltsScore) : null,
        toefl_score: englishOption === "TOEFL" && toeflScore ? Number(toeflScore) : null,
        duolingo_score: englishOption === "Duolingo" && duolingoScore ? Number(duolingoScore) : null,
        medium_of_instruction_english: hasMoi,
        moi_certificate_available: hasMoi,
        has_english_test: ["IELTS", "TOEFL", "Duolingo", "PTE Academic"].includes(englishOption),
      },
      standardized_tests: {
        hec_hat: targetDegree !== "Bachelor's" && !isNaN(parsedUsatHat) ? parsedUsatHat : null,
        hec_usat: targetDegree === "Bachelor's" && !isNaN(parsedUsatHat) ? parsedUsatHat : null,
      },
      preferences: {
        target_degree_level: targetDegree,
        target_fields: [cleanField || "All Academic Disciplines"],
        funding_requirement: fundingReq,
        budget_tier: budgetPkr <= 150000 ? "LOW" : budgetPkr <= 350000 ? "MODERATE" : "HIGH",
        max_out_of_pocket_pkr: Number(budgetPkr),
        willing_to_relocate: true,
        preferred_regions: selectedRegions,
        excluded_regions: [],
        constraints: [
          `Max upfront budget PKR ${Number(budgetPkr).toLocaleString()}`,
          fundingReq === "FULL"
            ? "Full tuition waiver and living stipend prioritized"
            : "Partial funding acceptable",
        ],
      },
      documents: {
        transcript: { uploaded: true, quality: "GOOD", confidence: 0.95 },
        cv: { uploaded: true, quality: "GOOD", confidence: 0.9 },
        passport: { uploaded: true, quality: "GOOD", confidence: 0.98 },
        ielts_certificate: {
          uploaded: englishOption === "IELTS",
          quality: englishOption === "IELTS" ? "GOOD" : null,
        },
        motivation_letter: { uploaded: false },
        recommendation_letters_count: 2,
        financial_documents: { uploaded: false },
        police_clearance: { uploaded: false },
        medical_certificate: { uploaded: false },
        hec_attestation: { uploaded: false },
        ibcc_equivalence: { uploaded: false },
      },
      profile_completeness: 88,
      missing_required: [],
      missing_optional: ["motivation_letter", "hec_attestation", "ibcc_equivalence"],
    };

    onLaunchMission(profilePayload, newSessionId);
  };

  const handleDeleteSession = async (sId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    try {
      await deleteSession(sId);
      setRecentSessions((prev) => prev.filter((s) => s.session_id !== sId));
    } catch (err) {
      console.error("Failed to delete session:", err);
    }
  };

  return (
    <div className="fixed inset-0 z-50 w-full h-full bg-[#05070A] text-white flex flex-col justify-between overflow-x-hidden overflow-y-auto font-sans pb-24">
      {/* Background Spatial World Stage & Atmospheric Lighting */}
      <div className="fixed inset-0 pointer-events-none z-0 overflow-hidden">
        <AtmosphericBackground />
        <WorldStage mapState="DEPLOYMENT" cameraShot="GLOBAL" />
        <div className="absolute inset-0 bg-[#05070A]/50" />
      </div>

      {/* Datalists for custom typing & instant autocomplete */}
      <datalist id="pakistan-cities">
        {PAKISTANI_CITIES.map((c) => (
          <option key={c.name} value={c.name}>
            {c.name} ({c.province})
          </option>
        ))}
      </datalist>

      <datalist id="pakistan-institutions">
        {PAKISTANI_INSTITUTIONS.map((inst) => (
          <option key={inst} value={inst} />
        ))}
      </datalist>

      <datalist id="pakistan-boards">
        {PAKISTANI_BOARDS.map((b) => (
          <option key={b} value={b} />
        ))}
      </datalist>

      <datalist id="study-fields">
        {STUDY_FIELDS.map((f) => (
          <option key={f} value={f} />
        ))}
      </datalist>

      {/* Top Header */}
      <header className="relative z-20 w-full px-3 sm:px-6 py-3 sm:py-4 flex flex-wrap items-center justify-between border-b border-white/[0.08] bg-black/70 backdrop-blur-xl shrink-0 gap-2.5">
        <div className="flex items-center space-x-2.5 sm:space-x-3 min-w-0">
          <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-lg bg-sx-gold/15 border border-sx-gold/40 flex items-center justify-center text-sx-gold font-bold text-xs sm:text-sm shadow-[0_0_15px_rgba(212,175,55,0.3)] shrink-0">
            SX
          </div>
          <div className="min-w-0">
            <div className="flex items-center space-x-2">
              <span className="text-base sm:text-lg font-bold tracking-tight text-white font-sans">
                SCHOLARX
              </span>
              <span className="text-[9px] sm:text-[10px] uppercase font-semibold px-1.5 sm:px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 shrink-0">
                AI NETWORK
              </span>
            </div>
            <p className="text-[11px] sm:text-[12px] text-zinc-400 font-normal truncate max-w-[220px] xs:max-w-[320px] sm:max-w-none">
              Autonomous Scholarship Intelligence for Pakistani Students
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2 sm:space-x-3 shrink-0">
          <Link
            href="/scholarships"
            className="flex items-center space-x-1.5 px-2.5 sm:px-3.5 py-1.5 rounded-lg border border-sky-500/40 bg-sky-500/10 hover:bg-sky-500/20 text-xs font-mono text-sky-400 font-semibold transition-all shadow-[0_0_12px_rgba(56,189,248,0.2)] cursor-pointer"
            title="Browse 310+ Verified Scholarships Database"
          >
            <Database className="w-3.5 h-3.5 text-sky-400" />
            <span className="hidden xs:inline">DB (310)</span>
          </Link>

          {recentSessions.length > 0 && (
            <button
              onClick={() => setShowRecentSessions(!showRecentSessions)}
              className="flex items-center space-x-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg border border-white/[0.12] bg-white/[0.05] hover:bg-white/[0.1] text-xs font-mono text-zinc-300 transition-all cursor-pointer"
            >
              <History className="w-3.5 h-3.5 text-sx-ice" />
              <span className="hidden sm:inline">RECENT</span>
              <span>({recentSessions.length})</span>
            </button>
          )}

          <div className="flex items-center space-x-1.5 px-2.5 sm:px-3.5 py-1.5 rounded-lg border border-emerald-500/30 bg-emerald-500/10 text-xs font-mono text-emerald-400 font-bold shadow-[0_0_15px_rgba(16,185,129,0.2)]">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span className="hidden md:inline">NETWORK ONLINE</span>
            <span className="md:hidden">ONLINE</span>
          </div>
        </div>
      </header>

      {/* Main Content Floor */}
      <main className="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 py-8 flex-1 flex flex-col justify-start">
        {/* Preset Selector Banner */}
        <div className="mb-6">
          <div className="flex items-center justify-between mb-2">
            <div className="text-xs font-mono text-sx-gold tracking-widest uppercase font-semibold flex items-center gap-2">
              <Sliders className="w-3.5 h-3.5 text-sx-gold" />
              <span>SELECT APPLICANT ARCHETYPE OR BUILD CUSTOM</span>
            </div>
            <div className="text-[11px] font-mono text-zinc-400">
              {isCustom ? "★ Custom Profile Active" : "1-Click Presets or Manual Configuration"}
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3">
            {PRESETS.map((p) => {
              const isSelected = selectedPresetId === p.id && !isCustom;
              const isCambridge = p.educationStream === "CAMBRIDGE";
              return (
                <button
                  key={p.id}
                  onClick={() => applyPreset(p)}
                  className={`p-3 rounded-xl border text-left transition-all cursor-pointer relative overflow-hidden ${
                    isSelected
                      ? isCambridge
                        ? "border-purple-400 bg-purple-500/20 shadow-[0_0_15px_rgba(168,85,247,0.3)] ring-1 ring-purple-400/60"
                        : "border-sx-gold bg-sx-gold/15 shadow-[0_0_15px_rgba(212,175,55,0.2)] ring-1 ring-sx-gold/60"
                      : "border-white/[0.08] bg-black/40 hover:bg-white/[0.04] hover:border-white/[0.15]"
                  }`}
                >
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-sm text-white">{p.name}</span>
                    <span className={`text-[9px] font-mono px-1.5 py-0.5 rounded ${isCambridge ? "bg-purple-500/30 text-purple-200 border border-purple-400/30 font-bold" : "bg-white/10 text-zinc-300"}`}>
                      {p.city}
                    </span>
                  </div>
                  <div className="text-xs text-zinc-400 truncate">{p.subtitle}</div>
                  {p.badge && (
                    <div className="mt-1">
                      <span className="text-[8px] font-mono font-bold px-1.5 py-0.5 rounded bg-purple-500/30 text-purple-200 border border-purple-400/40">
                        ★ {p.badge}
                      </span>
                    </div>
                  )}
                  <div className="text-[10px] font-mono text-sx-ice mt-2 flex items-center space-x-1">
                    <GraduationCap className="w-3 h-3" />
                    <span className="truncate">
                      {p.degree} • {p.field}
                    </span>
                  </div>
                </button>
              );
            })}

            {/* Custom Mode Tab */}
            <button
              onClick={() => {
                setIsCustom(true);
                setSelectedPresetId("custom");
              }}
              className={`p-3 rounded-xl border text-left transition-all cursor-pointer ${
                isCustom
                  ? "border-sx-ice bg-sx-ice/15 shadow-[0_0_15px_rgba(56,189,248,0.2)] ring-1 ring-sx-ice/60"
                  : "border-white/[0.08] bg-black/40 hover:bg-white/[0.04] hover:border-white/[0.15]"
              }`}
            >
              <div className="flex items-center justify-between mb-1">
                <span className="font-bold text-sm text-white">Custom Profile</span>
                <span className="text-[9px] font-mono px-1.5 py-0.5 rounded bg-sx-ice/20 text-sx-ice font-bold">
                  CUSTOM
                </span>
              </div>
              <div className="text-xs text-zinc-300">Test with any data & criteria</div>
              <div className="text-[10px] font-mono text-sx-ice mt-2 flex items-center space-x-1">
                <Compass className="w-3 h-3" />
                <span>Fully editable parameters</span>
              </div>
            </button>
          </div>
        </div>

        {/* Configuration Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Left Column: Intake Fields (7 cols) */}
          <div className="lg:col-span-7 rounded-2xl border border-white/[0.08] bg-black/75 backdrop-blur-xl p-5 space-y-4 shadow-xl">
            <div className="flex items-center justify-between border-b border-white/[0.08] pb-3">
              <div className="flex items-center space-x-2">
                <Shield className="w-4 h-4 text-sx-gold" />
                <span className="font-mono text-xs uppercase tracking-wider text-white font-bold">
                  STUDENT PROFILE & ELIGIBILITY PARAMETERS
                </span>
              </div>
              <span className="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                BILATERAL QUOTA READY
              </span>
            </div>

            {/* Section 1: Candidate Identity */}
            <div className="space-y-2">
              <div className="text-[10px] font-mono text-zinc-400 uppercase tracking-wider">
                1. CANDIDATE IDENTITY & ORIGIN
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    APPLICANT NAME
                  </label>
                  <input
                    type="text"
                    value={studentName}
                    onChange={(e) => {
                      setStudentName(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    placeholder="e.g. Hamza Gohar"
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    ORIGIN CITY (PAKISTAN)
                  </label>
                  <input
                    type="text"
                    list="pakistan-cities"
                    value={city}
                    onChange={(e) => handleCityChange(e.target.value)}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    placeholder="Type or select city..."
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    PROVINCE / REGION
                  </label>
                  <select
                    value={province}
                    onChange={(e) => {
                      setProvince(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors cursor-pointer"
                  >
                    <option value="Punjab">Punjab</option>
                    <option value="Sindh">Sindh</option>
                    <option value="KPK">Khyber Pakhtunkhwa (KPK)</option>
                    <option value="Balochistan">Balochistan</option>
                    <option value="ICT">Islamabad (ICT)</option>
                    <option value="Gilgit-Baltistan">Gilgit-Baltistan</option>
                    <option value="AJK">Azad Jammu & Kashmir (AJK)</option>
                  </select>
                </div>
              </div>
            </div>

            {/* Qualification Stream Switcher Banner */}
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between p-3 rounded-xl bg-white/[0.03] border border-white/[0.08] gap-2.5">
              <div className="flex items-center space-x-2.5">
                <div className={`w-auto px-2 h-7 rounded-lg flex items-center justify-center font-bold text-xs ${
                  educationStream === "CAMBRIDGE" ? "bg-purple-500/20 text-purple-300 border border-purple-400/40" : "bg-sx-gold/20 text-sx-gold border border-sx-gold/40"
                }`}>
                  {educationStream === "CAMBRIDGE" ? "CIE" : "BISE / FBISE"}
                </div>
                <div>
                  <div className="text-xs font-mono font-bold text-white uppercase tracking-wider flex items-center gap-1.5">
                    <span>QUALIFICATION STREAM</span>
                    {educationStream === "CAMBRIDGE" && (
                      <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-purple-500/30 text-purple-200 border border-purple-400/30 font-bold">
                        A-LEVELS ACTIVE
                      </span>
                    )}
                  </div>
                  <div className="text-[10px] text-zinc-400">
                    {educationStream === "CAMBRIDGE"
                      ? "Official IBCC equivalence calculated automatically for Cambridge grades"
                      : "Pakistani BISE & FBISE Boards (Matric / FSc / ICS) percentage and HEC CGPA scaling"}
                  </div>
                </div>
              </div>

              <div className="flex items-center space-x-2 w-full sm:w-auto">
                <button
                  type="button"
                  onClick={() => {
                    setEducationStream("PAKISTANI_HSSC");
                    if (educationLevel.includes("A-Levels")) {
                      setEducationLevel("Intermediate / ICS / FSc / FA");
                    }
                    setIsCustom(true);
                  }}
                  className={`flex-1 sm:flex-initial px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition-all cursor-pointer ${
                    educationStream === "PAKISTANI_HSSC"
                      ? "bg-sx-gold/20 text-sx-gold border border-sx-gold shadow-[0_0_12px_rgba(212,175,55,0.25)] ring-1 ring-sx-gold/60"
                      : "bg-white/[0.04] text-zinc-400 border border-white/[0.08] hover:text-white"
                  }`}
                >
                  Pakistani Board (BISE / FBISE)
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setEducationStream("CAMBRIDGE");
                    setEducationLevel("A-Levels / Cambridge / Edexcel");
                    if (!institution || institution.includes("PAEC") || institution.includes("Emerson")) {
                      setInstitution("Karachi Grammar School (KGS)");
                    }
                    const eq = computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3);
                    setGpaPercentage(eq.pct);
                    setGpa4Scale(eq.gpa);
                    setIsCustom(true);
                  }}
                  className={`flex-1 sm:flex-initial px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                    educationStream === "CAMBRIDGE"
                      ? "bg-purple-500/25 text-purple-200 border border-purple-400 shadow-[0_0_15px_rgba(168,85,247,0.35)] ring-1 ring-purple-400/60"
                      : "bg-white/[0.04] text-zinc-400 border border-white/[0.08] hover:text-white"
                  }`}
                >
                  <Sparkles className="w-3.5 h-3.5 text-purple-400" />
                  <span>Cambridge (O / A-Levels / CIE)</span>
                </button>
              </div>
            </div>

            {/* Section 2: Academic Background & Target */}
            <div className="space-y-2 pt-2 border-t border-white/[0.06]">
              <div className="text-[10px] font-mono text-zinc-400 uppercase tracking-wider flex items-center justify-between">
                <span>2. ACADEMIC BACKGROUND & INSTITUTION</span>
                {educationStream === "CAMBRIDGE" && (
                  <span className="text-[10px] font-mono text-purple-300">
                    CIE Attestation: Plot 25, G-10/4, Islamabad
                  </span>
                )}
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    CURRENT / PREVIOUS INSTITUTION
                  </label>
                  <input
                    type="text"
                    list="pakistan-institutions"
                    value={institution}
                    onChange={(e) => {
                      setInstitution(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    placeholder={educationStream === "CAMBRIDGE" ? "e.g. Karachi Grammar School (KGS), Aitchison..." : "e.g. GCU Lahore, NUST, FAST..."}
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    CURRENT EDUCATION LEVEL
                  </label>
                  <select
                    value={educationLevel}
                    onChange={(e) => {
                      const val = e.target.value;
                      setEducationLevel(val);
                      if (val.includes("A-Levels")) {
                        setEducationStream("CAMBRIDGE");
                        if (!institution || institution.includes("PAEC") || institution.includes("Emerson")) {
                          setInstitution("Karachi Grammar School (KGS)");
                        }
                        const eq = computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3);
                        setGpaPercentage(eq.pct);
                        setGpa4Scale(eq.gpa);
                      } else if (educationStream === "CAMBRIDGE") {
                        setEducationStream("PAKISTANI_HSSC");
                      }
                      setIsCustom(true);
                    }}
                    className={`w-full px-3 py-2 rounded-lg bg-black/80 border text-xs font-mono text-white focus:outline-none transition-colors cursor-pointer ${
                      educationStream === "CAMBRIDGE" ? "border-purple-400/60 focus:border-purple-400" : "border-white/[0.15] focus:border-sx-gold"
                    }`}
                  >
                    <option value="A-Levels / Cambridge / Edexcel">
                      A-Levels / Cambridge / Edexcel (12/13 Yrs)
                    </option>
                    <option value="Intermediate / ICS / FSc / FA">
                      Intermediate / ICS / FSc / FA (12 Yrs)
                    </option>
                    <option value="Bachelor&apos;s / BS / BE / BBA">
                      Bachelor&apos;s / BS / BE / BBA (16 Yrs)
                    </option>
                    <option value="Master&apos;s / MS / MSc / MPhil">
                      Master&apos;s / MS / MPhil (18 Yrs)
                    </option>
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    TARGET DEGREE
                  </label>
                  <select
                    value={targetDegree}
                    onChange={(e) => {
                      setTargetDegree(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors cursor-pointer"
                  >
                    <option value="Bachelor&apos;s">Bachelor&apos;s (BS / BE)</option>
                    <option value="Master&apos;s">Master&apos;s (MS / MSc)</option>
                    <option value="PhD">Doctorate (PhD)</option>
                  </select>
                </div>

                <div className="sm:col-span-2">
                  <div className="flex items-center justify-between mb-1">
                    <label className="text-[11px] font-mono text-zinc-300">
                      INTENDED FIELD OF STUDY
                    </label>
                    <span className="text-[9px] font-mono text-emerald-400 bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/20">
                      AI SPELLING AUTO-FIX
                    </span>
                  </div>
                  <input
                    type="text"
                    list="study-fields"
                    value={fieldOfStudy}
                    onChange={(e) => {
                      setFieldOfStudy(e.target.value);
                      setIsCustom(true);
                    }}
                    onBlur={async () => {
                      if (fieldOfStudy.trim().length >= 3) {
                        try {
                          const res = await fetch("/api/profile/normalize", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify({ fieldOfStudy, studentName, city, institution }),
                          });
                          if (res.ok) {
                            const data = await res.json();
                            if (data.corrected?.fieldOfStudy && data.corrected.fieldOfStudy !== fieldOfStudy) {
                              setFieldOfStudy(data.corrected.fieldOfStudy);
                            }
                            if (data.corrected?.studentName && data.corrected.studentName !== studentName) {
                              setStudentName(data.corrected.studentName);
                            }
                          }
                        } catch {
                          // non-blocking
                        }
                      }
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    placeholder="e.g. Computer Science, AI, Biotechnology"
                  />
                </div>
              </div>

              {educationStream === "PAKISTANI_HSSC" && (
                <div className="pt-1">
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1 flex items-center justify-between">
                    <span>EXAMINATION BOARD (FBISE / BISE / UNIVERSITY)</span>
                    <span className="text-[10px] font-mono text-zinc-400">Federal &amp; Provincial Boards Supported</span>
                  </label>
                  <input
                    type="text"
                    list="pakistan-boards"
                    value={board}
                    onChange={(e) => {
                      setBoard(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    placeholder="e.g. FBISE Islamabad, BISE Lahore, BISE Multan, Quaid-i-Azam University..."
                  />
                </div>
              )}
            </div>

            {/* Section 3: Dual Precision Academic Scores OR Cambridge IBCC Equivalence Calculator */}
            {educationStream === "CAMBRIDGE" ? (
              <div className="space-y-3 pt-2 border-t border-purple-500/30 bg-purple-950/20 p-4 rounded-xl border border-purple-500/25">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <Sparkles className="w-4 h-4 text-purple-400" />
                    <span className="text-xs font-mono font-bold text-purple-200 uppercase tracking-wider">
                      3. CAMBRIDGE A-LEVELS & OFFICIAL IBCC EQUIVALENCE CALCULATOR
                    </span>
                  </div>
                  <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-purple-500/25 text-purple-300 border border-purple-500/40 font-bold">
                    OFFICIAL IBCC STANDARD
                  </span>
                </div>

                <p className="text-[11px] text-zinc-300 leading-relaxed">
                  Enter your Cambridge GCE A-Level letter grades below. ScholarX converts your CIE grades to the Pakistani 1,100 marks benchmark and 4.0 scale CGPA using official IBCC point criteria (<span className="text-purple-300 font-mono font-bold">A*=90, A=85, B=75, C=65, D=55, E=45</span>).
                </p>

                {/* 3 Principal A-Level Subjects with letter grade dropdowns */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div className="p-3 rounded-lg bg-black/70 border border-purple-500/30">
                    <label className="block text-[10px] font-mono text-zinc-400 mb-1">
                      A-LEVEL SUBJECT 1
                    </label>
                    <input
                      type="text"
                      value={aLevelSubject1}
                      onChange={(e) => {
                        setALevelSubject1(e.target.value);
                        setIsCustom(true);
                      }}
                      className="w-full px-2.5 py-1.5 mb-2 rounded bg-white/[0.05] border border-white/[0.1] text-xs font-mono text-white focus:outline-none focus:border-purple-400"
                      placeholder="e.g. Mathematics"
                    />
                    <label className="block text-[10px] font-mono text-zinc-400 mb-1">
                      CIE LETTER GRADE
                    </label>
                    <select
                      value={aLevelGrade1}
                      onChange={(e) => {
                        const newG = e.target.value;
                        setALevelGrade1(newG);
                        setIsCustom(true);
                        if (!manualMarksOverride) {
                          const eq = computeIbccEquivalence(newG, aLevelGrade2, aLevelGrade3);
                          setGpaPercentage(eq.pct);
                          setGpa4Scale(eq.gpa);
                        }
                      }}
                      className="w-full px-2.5 py-1.5 rounded bg-black border border-purple-400/40 text-xs font-mono text-sx-gold font-bold focus:outline-none focus:border-purple-400 cursor-pointer"
                    >
                      {["A*", "A", "B", "C", "D", "E", "U"].map((g) => (
                        <option key={g} value={g}>
                          Grade {g} ({g === "A*" ? "90 pts" : g === "A" ? "85 pts" : g === "B" ? "75 pts" : g === "C" ? "65 pts" : g === "D" ? "55 pts" : g === "E" ? "45 pts" : "0 pts"})
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="p-3 rounded-lg bg-black/70 border border-purple-500/30">
                    <label className="block text-[10px] font-mono text-zinc-400 mb-1">
                      A-LEVEL SUBJECT 2
                    </label>
                    <input
                      type="text"
                      value={aLevelSubject2}
                      onChange={(e) => {
                        setALevelSubject2(e.target.value);
                        setIsCustom(true);
                      }}
                      className="w-full px-2.5 py-1.5 mb-2 rounded bg-white/[0.05] border border-white/[0.1] text-xs font-mono text-white focus:outline-none focus:border-purple-400"
                      placeholder="e.g. Physics"
                    />
                    <label className="block text-[10px] font-mono text-zinc-400 mb-1">
                      CIE LETTER GRADE
                    </label>
                    <select
                      value={aLevelGrade2}
                      onChange={(e) => {
                        const newG = e.target.value;
                        setALevelGrade2(newG);
                        setIsCustom(true);
                        if (!manualMarksOverride) {
                          const eq = computeIbccEquivalence(aLevelGrade1, newG, aLevelGrade3);
                          setGpaPercentage(eq.pct);
                          setGpa4Scale(eq.gpa);
                        }
                      }}
                      className="w-full px-2.5 py-1.5 rounded bg-black border border-purple-400/40 text-xs font-mono text-sx-gold font-bold focus:outline-none focus:border-purple-400 cursor-pointer"
                    >
                      {["A*", "A", "B", "C", "D", "E", "U"].map((g) => (
                        <option key={g} value={g}>
                          Grade {g} ({g === "A*" ? "90 pts" : g === "A" ? "85 pts" : g === "B" ? "75 pts" : g === "C" ? "65 pts" : g === "D" ? "55 pts" : g === "E" ? "45 pts" : "0 pts"})
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="p-3 rounded-lg bg-black/70 border border-purple-500/30">
                    <label className="block text-[10px] font-mono text-zinc-400 mb-1">
                      A-LEVEL SUBJECT 3
                    </label>
                    <input
                      type="text"
                      value={aLevelSubject3}
                      onChange={(e) => {
                        setALevelSubject3(e.target.value);
                        setIsCustom(true);
                      }}
                      className="w-full px-2.5 py-1.5 mb-2 rounded bg-white/[0.05] border border-white/[0.1] text-xs font-mono text-white focus:outline-none focus:border-purple-400"
                      placeholder="e.g. Computer Science"
                    />
                    <label className="block text-[10px] font-mono text-zinc-400 mb-1">
                      CIE LETTER GRADE
                    </label>
                    <select
                      value={aLevelGrade3}
                      onChange={(e) => {
                        const newG = e.target.value;
                        setALevelGrade3(newG);
                        setIsCustom(true);
                        if (!manualMarksOverride) {
                          const eq = computeIbccEquivalence(aLevelGrade1, aLevelGrade2, newG);
                          setGpaPercentage(eq.pct);
                          setGpa4Scale(eq.gpa);
                        }
                      }}
                      className="w-full px-2.5 py-1.5 rounded bg-black border border-purple-400/40 text-xs font-mono text-sx-gold font-bold focus:outline-none focus:border-purple-400 cursor-pointer"
                    >
                      {["A*", "A", "B", "C", "D", "E", "U"].map((g) => (
                        <option key={g} value={g}>
                          Grade {g} ({g === "A*" ? "90 pts" : g === "A" ? "85 pts" : g === "B" ? "75 pts" : g === "C" ? "65 pts" : g === "D" ? "55 pts" : g === "E" ? "45 pts" : "0 pts"})
                        </option>
                      ))}
                    </select>
                  </div>
                </div>

                {/* Live Computed IBCC Equivalence Results Box */}
                <div className="p-3.5 rounded-xl bg-gradient-to-r from-purple-900/35 via-black to-purple-900/25 border border-purple-500/40 space-y-2.5 shadow-lg">
                  <div className="flex flex-wrap items-center justify-between gap-2 border-b border-white/[0.08] pb-2">
                    <div>
                      <div className="text-[10px] font-mono uppercase text-purple-300 font-bold flex items-center gap-1.5">
                        <Award className="w-3.5 h-3.5 text-purple-400" />
                        <span>CALCULATED IBCC EQUIVALENCE (PAKISTANI BENCHMARK)</span>
                      </div>
                      <div className="text-xl font-bold font-mono text-white flex items-center gap-2 mt-0.5">
                        <span className="text-sx-gold">{gpaPercentage}%</span>
                        <span className="text-xs text-zinc-300 font-normal">
                          • {Math.round((gpaPercentage / 100) * 1100)} / 1,100 Marks
                        </span>
                        <span className="text-xs text-emerald-400 font-normal">
                          • {gpa4Scale} / 4.0 CGPA
                        </span>
                      </div>
                    </div>
                    <span className="text-[10px] font-mono px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold">
                      {computeIbccEquivalence(aLevelGrade1, aLevelGrade2, aLevelGrade3).division}
                    </span>
                  </div>

                  <div className="flex flex-wrap items-center justify-between gap-2 text-[11px] text-zinc-300">
                    <span className="flex items-center gap-1.5 text-purple-300 font-mono text-[10px]">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                      IBCC Cambridge Cell Islamabad (Plot 25, G-10/4) Attestation Protocol Active
                    </span>
                    <button
                      type="button"
                      onClick={() => setManualMarksOverride(!manualMarksOverride)}
                      className="text-[10px] font-mono text-zinc-400 hover:text-white underline cursor-pointer"
                    >
                      {manualMarksOverride ? "Auto Calculate From Grades" : "Manual Marks Override"}
                    </button>
                  </div>

                  {manualMarksOverride && (
                    <div className="grid grid-cols-2 gap-3 pt-2 border-t border-white/[0.08]">
                      <div>
                        <label className="block text-[10px] font-mono text-zinc-300 mb-1">
                          MANUAL EQUIVALENCE (%)
                        </label>
                        <input
                          type="number"
                          min="40"
                          max="100"
                          step="0.1"
                          value={gpaPercentage}
                          onChange={(e) => {
                            const val = parseFloat(e.target.value) || 0;
                            setGpaPercentage(val);
                            setGpa4Scale(percentageToGpa4(val));
                            setIsCustom(true);
                          }}
                          className="w-full px-2.5 py-1.5 rounded bg-black border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-purple-400"
                        />
                      </div>
                      <div>
                        <label className="block text-[10px] font-mono text-zinc-300 mb-1">
                          MANUAL 4.0 SCALE GPA
                        </label>
                        <input
                          type="number"
                          min="1.0"
                          max="4.0"
                          step="0.01"
                          value={gpa4Scale}
                          onChange={(e) => {
                            const val = parseFloat(e.target.value) || 0;
                            setGpa4Scale(val);
                            if (!isNaN(val) && val > 0) {
                              setGpaPercentage(gpaToPercentage(val));
                            }
                            setIsCustom(true);
                          }}
                          className="w-full px-2.5 py-1.5 rounded bg-black border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-purple-400"
                        />
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <div className="space-y-2 pt-2 border-t border-white/[0.06]">
                <div className="text-[10px] font-mono text-zinc-400 uppercase tracking-wider flex items-center justify-between">
                  <span>3. ACADEMIC SCORES & GPA PRECISION</span>
                  <span className="text-sx-gold">
                    {gpaPercentage}% • {gpa4Scale} / 4.0 GPA
                  </span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                      MARKS PERCENTAGE (%)
                    </label>
                    <input
                      type="number"
                      min="50"
                      max="100"
                      step="0.1"
                      value={gpaPercentage}
                      onChange={(e) => {
                        const val = parseFloat(e.target.value) || 0;
                        setGpaPercentage(val);
                        setGpa4Scale(percentageToGpa4(val));
                        setIsCustom(true);
                      }}
                      className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    />
                  </div>

                  <div>
                    <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                      GPA ON 4.0 SCALE
                    </label>
                    <input
                      type="number"
                      min="1.0"
                      max="4.0"
                      step="0.01"
                      value={gpa4Scale}
                      onChange={(e) => {
                        const val = parseFloat(e.target.value) || 0;
                        setGpa4Scale(val);
                        if (!isNaN(val) && val > 0) {
                          setGpaPercentage(gpaToPercentage(val));
                        }
                        setIsCustom(true);
                      }}
                      className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    />
                  </div>
                </div>

                {/* Quick slider */}
                <div className="flex items-center space-x-3 pt-1">
                  <span className="text-[10px] font-mono text-zinc-400">50%</span>
                  <input
                    type="range"
                    min="50"
                    max="98"
                    step="0.5"
                    value={gpaPercentage}
                    onChange={(e) => {
                      const val = Number(e.target.value);
                      setGpaPercentage(val);
                      setGpa4Scale(percentageToGpa4(val));
                      setIsCustom(true);
                    }}
                    className="w-full accent-sx-gold cursor-pointer"
                  />
                  <span className="text-[10px] font-mono text-zinc-400">98%</span>
                </div>
              </div>
            )}

            {/* Section 4: Language Proficiency & Standardized Tests */}
            <div className="space-y-2 pt-2 border-t border-white/[0.06]">
              <div className="text-[10px] font-mono text-zinc-400 uppercase tracking-wider">
                4. LANGUAGE PROFICIENCY & CLEARANCE
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    ENGLISH TEST
                  </label>
                  <select
                    value={englishOption}
                    onChange={(e) => {
                      setEnglishOption(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors cursor-pointer"
                  >
                    <option value="IELTS">IELTS Academic</option>
                    <option value="TOEFL">TOEFL iBT</option>
                    <option value="Duolingo">Duolingo English Test</option>
                    <option value="PTE Academic">PTE Academic</option>
                    <option value="Medium of Instruction (MOI) Certificate">
                      MOI Certificate Only
                    </option>
                    <option value="None / Not Available">No English Test</option>
                  </select>
                </div>

                {englishOption === "IELTS" && (
                  <div>
                    <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                      IELTS OVERALL BAND
                    </label>
                    <select
                      value={ieltsScore}
                      onChange={(e) => {
                        setIeltsScore(Number(e.target.value));
                        setIsCustom(true);
                      }}
                      className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors cursor-pointer"
                    >
                      <option value={5.5}>5.5 Modest</option>
                      <option value={6.0}>6.0 Competent</option>
                      <option value={6.5}>6.5 Good</option>
                      <option value={7.0}>7.0 Very Good</option>
                      <option value={7.5}>7.5 Proficient</option>
                      <option value={8.0}>8.0 Superior</option>
                      <option value={8.5}>8.5 Expert</option>
                      <option value={9.0}>9.0 Native</option>
                    </select>
                  </div>
                )}

                {englishOption === "TOEFL" && (
                  <div>
                    <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                      TOEFL SCORE (0-120)
                    </label>
                    <input
                      type="number"
                      min="0"
                      max="120"
                      value={toeflScore}
                      onChange={(e) => {
                        setToeflScore(Number(e.target.value));
                        setIsCustom(true);
                      }}
                      className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    />
                  </div>
                )}

                {englishOption === "Duolingo" && (
                  <div>
                    <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                      DUOLINGO SCORE (0-160)
                    </label>
                    <input
                      type="number"
                      min="0"
                      max="160"
                      value={duolingoScore}
                      onChange={(e) => {
                        setDuolingoScore(Number(e.target.value));
                        setIsCustom(true);
                      }}
                      className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    />
                  </div>
                )}

                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    HEC USAT / HAT (OPTIONAL)
                  </label>
                  <input
                    type="text"
                    value={usatHatScore}
                    onChange={(e) => {
                      setUsatHatScore(e.target.value);
                      setIsCustom(true);
                    }}
                    placeholder="e.g. 75/100"
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                  />
                </div>
              </div>

              {/* MOI Certificate Toggle */}
              <div className="flex items-center space-x-2.5 pt-1">
                <input
                  type="checkbox"
                  id="moiCheck"
                  checked={hasMoi}
                  onChange={(e) => {
                    setHasMoi(e.target.checked);
                    setIsCustom(true);
                  }}
                  className="accent-sx-gold w-4 h-4 rounded cursor-pointer"
                />
                <label htmlFor="moiCheck" className="text-xs text-zinc-300 cursor-pointer">
                  Medium of Instruction (MOI) Certificate in English available from college/university
                </label>
              </div>
            </div>

            {/* Section 5: Funding Requirement & Budget Ceiling */}
            <div className="space-y-2 pt-2 border-t border-white/[0.06]">
              <div className="text-[10px] font-mono text-zinc-400 uppercase tracking-wider">
                5. FUNDING CAPACITY & PKR BUDGET CEILING
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    FUNDING REQUIREMENT
                  </label>
                  <select
                    value={fundingReq}
                    onChange={(e) => {
                      setFundingReq(e.target.value);
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors cursor-pointer"
                  >
                    <option value="FULL">
                      Full Funding (100% Tuition Waiver + Monthly Living Stipend)
                    </option>
                    <option value="PARTIAL">
                      Partial / Any Funding (Tuition Waiver / Partial Subsidy)
                    </option>
                  </select>
                </div>

                <div>
                  <label className="block text-[11px] font-mono text-zinc-300 mb-1">
                    MAX OUT-OF-POCKET UPFRONT BUDGET (PKR)
                  </label>
                  <input
                    type="number"
                    min="10000"
                    step="5000"
                    value={budgetPkr}
                    onChange={(e) => {
                      setBudgetPkr(Number(e.target.value));
                      setIsCustom(true);
                    }}
                    className="w-full px-3 py-2 rounded-lg bg-black/80 border border-white/[0.15] text-xs font-mono text-white focus:outline-none focus:border-sx-gold transition-colors"
                    placeholder="Enter PKR amount e.g. 150000"
                  />
                </div>
              </div>

              {/* Quick Budget Chips */}
              <div className="flex flex-wrap items-center gap-1.5 pt-1">
                <span className="text-[10px] font-mono text-zinc-400 mr-1">QUICK CHIPS:</span>
                {[50000, 100000, 150000, 250000, 400000, 600000, 1000000].map((amt) => (
                  <button
                    key={amt}
                    type="button"
                    onClick={() => {
                      setBudgetPkr(amt);
                      setIsCustom(true);
                    }}
                    className={`px-2 py-1 rounded text-[10px] font-mono border transition-all cursor-pointer ${
                      budgetPkr === amt
                        ? "bg-sx-gold/20 text-sx-gold border-sx-gold/50 font-bold"
                        : "bg-white/[0.04] text-zinc-400 border-white/[0.08] hover:text-white"
                    }`}
                  >
                    PKR {(amt / 1000).toFixed(0)}k
                  </button>
                ))}
              </div>
            </div>

            {/* Section 6: Continental Target Sectors */}
            <div className="space-y-2 pt-2 border-t border-white/[0.06]">
              <label className="block text-[11px] font-mono text-zinc-300">
                6. TARGET CONTINENTAL SECTORS ({selectedRegions.length} ACTIVE)
              </label>
              <div className="flex flex-wrap gap-2">
                {( ["Europe", "Asia", "Americas", "MENA", "Oceania"] as Region[] ).map((r) => {
                  const isActive = selectedRegions.includes(r);
                  return (
                    <button
                      key={r}
                      type="button"
                      onClick={() => toggleRegion(r)}
                      className={`px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all flex items-center space-x-1.5 cursor-pointer ${
                        isActive
                          ? "bg-sx-ice/20 text-sx-ice border border-sx-ice/50 shadow-[0_0_10px_rgba(56,189,248,0.25)] font-bold"
                          : "bg-white/[0.04] text-zinc-500 border border-white/[0.08] hover:text-zinc-300"
                      }`}
                    >
                      <Globe2 className="w-3.5 h-3.5" />
                      <span>{r}</span>
                    </button>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Right Column: Dynamic Mission Briefing Card (5 cols) */}
          <div className="lg:col-span-5 rounded-2xl border border-sx-gold/40 bg-black/85 backdrop-blur-2xl p-5 flex flex-col justify-between shadow-2xl relative overflow-hidden">
            <div className="absolute top-0 right-0 w-36 h-36 bg-sx-gold/15 rounded-full blur-3xl pointer-events-none" />

            <div>
              <div className="flex items-center justify-between border-b border-white/[0.08] pb-3 mb-4">
                <span className="font-mono text-xs uppercase tracking-widest text-sx-gold font-bold flex items-center gap-2">
                  <Compass className="w-4 h-4 text-sx-gold" />
                  <span>INTELLIGENCE MISSION BRIEF</span>
                </span>
                <span className="text-[10px] font-mono text-emerald-400 px-2 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20 font-bold">
                  VERIFIED READY
                </span>
              </div>

              {/* Dynamic Ledger */}
              <div className="space-y-2.5 font-mono text-xs mb-5">
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">CANDIDATE:</span>
                  <span className="text-white font-semibold">
                    {studentName || "Applicant"} ({city}, {province})
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">INSTITUTION:</span>
                  <span className="text-zinc-200 font-semibold truncate max-w-[220px]" title={institution}>
                    {institution || "Pakistani Institution"}
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">STREAM:</span>
                  <span className={educationStream === "CAMBRIDGE" ? "text-purple-300 font-semibold flex items-center gap-1" : "text-zinc-200 font-semibold"}>
                    {educationStream === "CAMBRIDGE" ? "Cambridge International (A-Levels)" : "Pakistani HSSC (Matric/FSc)"}
                  </span>
                </div>
                {educationStream === "CAMBRIDGE" && (
                  <>
                    <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                      <span className="text-zinc-400">A-LEVEL GRADES:</span>
                      <span className="text-sx-gold font-semibold">
                        {aLevelGrade1} {aLevelGrade2} {aLevelGrade3} ({gpaPercentage}% IBCC • {Math.round((gpaPercentage / 100) * 1100)}/1100)
                      </span>
                    </div>
                    <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                      <span className="text-zinc-400">ATTESTATION CELL:</span>
                      <span className="text-emerald-400 font-semibold text-[11px]">
                        IBCC Cambridge Cell G-10/4 Islamabad
                      </span>
                    </div>
                  </>
                )}
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">TARGET PROGRAM:</span>
                  <span className="text-sx-ice font-semibold">
                    {targetDegree} in {fieldOfStudy}
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">ACADEMIC STANDING:</span>
                  <span className="text-sx-gold font-semibold">
                    {gpaPercentage}% ({gpa4Scale} GPA)
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">ENGLISH CLEARANCE:</span>
                  <span className="text-emerald-400 font-semibold">
                    {englishOption === "IELTS"
                      ? `IELTS ${ieltsScore}`
                      : englishOption === "TOEFL"
                      ? `TOEFL ${toeflScore}`
                      : englishOption === "Duolingo"
                      ? `Duolingo ${duolingoScore}`
                      : hasMoi
                      ? "MOI Certificate"
                      : "No Test"}
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">FUNDING REQUIREMENT:</span>
                  <span className="text-amber-300 font-semibold">
                    {fundingReq === "FULL" ? "100% Full Waiver + Stipend" : "Partial / Any Funding"}
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">MAX PKR BUDGET:</span>
                  <span className="text-white font-semibold">
                    PKR {budgetPkr.toLocaleString()}
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-white/[0.04] pb-1.5">
                  <span className="text-zinc-400">ACTIVE REGIONAL SCOUTS:</span>
                  <span className="text-sx-ice font-semibold">{selectedRegions.join(", ")}</span>
                </div>
              </div>

              {/* Dynamic Mission Narrative */}
              <div className="p-3.5 rounded-xl bg-white/[0.03] border border-white/[0.08] text-[11px] text-zinc-300 leading-relaxed space-y-1.5 mb-5">
                <div className="font-mono text-sx-gold text-[10px] uppercase font-bold tracking-wider flex items-center gap-1.5">
                  <Award className="w-3.5 h-3.5 text-sx-gold" />
                  <span>MISSION DEPLOYMENT SCOPE</span>
                </div>
                <p>
                  Deploy the ScholarX autonomous multi-agent intelligence network across {selectedRegions.length} continental sectors to discover, verify, and rank bilateral quotas compatible with {studentName || "Applicant"}&apos;s profile. Resolve 15 eligibility dimensions, calculate exact upfront PKR visa & attestation costs, challenge adversarial bottlenecks, and synthesize an official scholarship dossier.
                </p>
              </div>
            </div>

            {/* Launch Action Button */}
            <div>
              <div className="flex items-center justify-between px-3 py-1.5 mb-2 rounded-lg bg-black/40 border border-white/[0.06] text-[10px] font-mono">
                <div className="flex items-center space-x-2">
                  <span
                    className={`w-2 h-2 rounded-full ${
                      backendStatus === "online"
                        ? "bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.9)] animate-pulse"
                        : "bg-amber-400 shadow-[0_0_8px_rgba(251,191,36,0.8)]"
                    }`}
                  />
                  <span className={backendStatus === "online" ? "text-emerald-300 font-semibold" : "text-amber-300 font-medium"}>
                    {backendStatus === "online"
                      ? "LIVE AGENT FLEET ACTIVE // PORT 8000 CONNECTED"
                      : "AUTONOMOUS EXHIBITION ENGINE ACTIVE // ZERO-CRASH LOCAL MODE"}
                  </span>
                </div>
                <span className="text-zinc-500 text-[9px] uppercase tracking-wider">
                  {backendStatus === "online" ? "30 KEYS READY" : "SIMULATOR READY"}
                </span>
              </div>

              <button
                type="button"
                onClick={handleLaunch}
                disabled={isSubmitting}
                className="w-full py-4 rounded-xl bg-gradient-to-r from-amber-400 via-amber-300 to-yellow-400 text-stone-950 font-sans font-black text-sm tracking-wider uppercase flex items-center justify-center space-x-2 shadow-[0_0_35px_rgba(251,191,36,0.6)] border-2 border-amber-300 hover:brightness-110 active:scale-[0.99] transition-all disabled:opacity-50 cursor-pointer"
              >
                {isSubmitting ? (
                  <>
                    <span className="w-5 h-5 border-2 border-stone-950 border-t-transparent rounded-full animate-spin" />
                    <span className="tracking-wide">INITIALIZING INTELLIGENCE MISSION...</span>
                  </>
                ) : (
                  <>
                    <span className="tracking-wide font-black">INITIALIZE SCHOLARX MISSION</span>
                    <ArrowRight className="w-5 h-5 stroke-[2.5]" />
                  </>
                )}
              </button>
              <div className="text-center text-[11px] font-mono text-zinc-400 mt-2 font-medium">
                Autonomous Multi-Agent Intelligence Network • Live Real-Time Execution
              </div>
            </div>
          </div>
        </div>

        {/* Recent Missions Drawer */}
        <AnimatePresence>
          {showRecentSessions && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 20 }}
              className="mt-6 p-4 rounded-2xl border border-white/[0.1] bg-black/95 backdrop-blur-2xl shadow-2xl"
            >
              <div className="flex items-center justify-between border-b border-white/[0.08] pb-3 mb-3">
                <div className="flex items-center space-x-2">
                  <History className="w-4 h-4 text-sx-ice" />
                  <span className="font-mono text-xs font-bold text-white uppercase tracking-wider">
                    SAVED INTELLIGENCE MISSIONS
                  </span>
                </div>
                <button
                  onClick={() => setShowRecentSessions(false)}
                  className="text-xs font-mono text-zinc-400 hover:text-white cursor-pointer"
                >
                  CLOSE
                </button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {recentSessions.map((s) => (
                  <div
                    key={s.session_id}
                    onClick={() => onResumeMission(s.session_id)}
                    className="p-3 rounded-xl border border-white/[0.08] bg-white/[0.02] hover:bg-white/[0.06] hover:border-sx-gold/50 cursor-pointer transition-all flex items-center justify-between group"
                  >
                    <div>
                      <div className="font-mono text-xs text-white font-bold truncate max-w-[200px]">
                        {s.session_id}
                      </div>
                      <div className="text-[11px] text-zinc-400 mt-0.5">
                        Status:{" "}
                        <span className="text-sx-gold font-mono uppercase">
                          {s.status || "SAVED"}
                        </span>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      <button
                        onClick={(e) => handleDeleteSession(s.session_id, e)}
                        className="p-1.5 rounded hover:bg-red-500/20 text-zinc-500 hover:text-red-400 transition-colors cursor-pointer"
                        title="Delete Session"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                      <button className="px-2.5 py-1 rounded bg-sx-gold/20 text-sx-gold text-xs font-mono font-bold group-hover:bg-sx-gold group-hover:text-black transition-colors cursor-pointer">
                        RESUME
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </main>

      {/* Mobile Floating Sticky Launch Bar */}
      <div className="fixed bottom-0 left-0 right-0 p-3 bg-black/90 backdrop-blur-xl border-t border-amber-400/30 z-40 lg:hidden shadow-[0_-10px_30px_rgba(0,0,0,0.8)]">
        <button
          type="button"
          onClick={handleLaunch}
          disabled={isSubmitting}
          className="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-amber-400 via-amber-300 to-yellow-400 text-stone-950 font-sans font-black text-sm tracking-wider uppercase flex items-center justify-center space-x-2 shadow-[0_0_25px_rgba(251,191,36,0.5)] border border-amber-300 active:scale-[0.99] transition-all disabled:opacity-50 cursor-pointer"
        >
          {isSubmitting ? (
            <>
              <span className="w-4 h-4 border-2 border-stone-950 border-t-transparent rounded-full animate-spin" />
              <span className="tracking-wide">INITIALIZING MISSION...</span>
            </>
          ) : (
            <>
              <span className="tracking-wide font-black">INITIALIZE SCHOLARX MISSION</span>
              <ArrowRight className="w-4 h-4 stroke-[2.5]" />
            </>
          )}
        </button>
      </div>

      {/* Footer Info */}
      <footer className="relative z-10 w-full px-4 sm:px-6 py-3 border-t border-white/[0.06] flex flex-col sm:flex-row items-center justify-between text-[10px] sm:text-[11px] font-mono text-zinc-500 gap-1 text-center sm:text-left pb-20 lg:pb-3">
        <div>SCHOLARX PRODUCT INTEGRATION // 10-NODE AUTONOMOUS ARCHITECTURE</div>
        <div className="hidden sm:block">PAKISTAN HEC & BILATERAL EMBASSY REGISTRIES COMPATIBLE</div>
      </footer>
    </div>
  );
};
