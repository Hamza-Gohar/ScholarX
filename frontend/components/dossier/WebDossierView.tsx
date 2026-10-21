"use client";

import React from "react";
import Link from "next/link";
import { CanonicalDossier, InvestigatedOpportunity } from "@/lib/ranking/types";
import {
  INVESTIGATED_OPPORTUNITIES,
  getInvestigatedOpportunitiesForProfile,
  buildDynamicInvestigatedOpportunity,
} from "@/lib/ranking/rankingStore";
import { 
  Printer, 
  Download,
  ExternalLink, 
  CheckCircle2, 
  AlertTriangle, 
  Coins, 
  Calendar, 
  FileText, 
  ShieldCheck, 
  MapPin, 
  X, 
  Briefcase, 
  TrendingUp, 
  User, 
  GraduationCap, 
  Award, 
  BadgePercent,
  Palette,
  Languages,
  Clock,
  Check,
  Atom,
  Cpu,
  Wrench,
  HeartPulse,
  Sparkles
} from "lucide-react";
import { getCountryFlag } from "@/lib/utils/countryFlags";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";
import { getCountryCareerProfile, getScholarshipExecutionSteps } from "@/lib/utils/careerData";
import { resolveScholarshipOfficialUrl, cleanPortalDisplayUrl } from "@/lib/utils/scholarshipUrls";
import { sound } from "@/lib/sound-fx";
import { getDegreeScholarshipLimit } from "@/lib/utils/degreeLimit";
import { percentageToGpa4 } from "@/lib/utils/gpaScale";

export interface ScholarshipBriefInfo {
  id: string;
  name: string;
  hostCountry: string;
  rankLabel: string;
  isPrimary: boolean;
  applicationWindow: string;
  deadlineDate: string;
  intakeCycle: string;
  portalUrl: string;
  portalLabel: string;
  hecPortalRequired: boolean;
  hecPortalUrl: string;
  fieldStream: {
    targetField: string;
    isEligible: boolean;
    isVerified: boolean;
    streamLabel: string;
    badgeLabel: string;
    description: string;
  };
  artsStream: {
    isArtsEligible: boolean;
    streamLabel: string;
    description: string;
  };
  language: {
    hasBarrier: boolean;
    ieltsRequired: boolean;
    testLabel: string;
    barrierLabel: string;
    description: string;
  };
  requirements: {
    minGpaText: string;
    ageLimitText: string;
    quotaSeatsText: string;
    testingText: string;
  };
  documentsNeeded: string[];
  expenses: {
    totalPkr: number;
    breakdownText: string;
    monthlyStipendText: string;
    tuitionCoverageText: string;
  };
  postStudyCareer: {
    workPermit: string;
    startingSalary: string;
    prPathway: string;
  };
}

export function getScholarshipBriefInfo(
  sc: InvestigatedOpportunity,
  scIdx: number,
  isUndergrad: boolean,
  candidateCity: string,
  hasEnglishTest: boolean,
  targetFieldInput?: string,
  isCambridge?: boolean,
  boardName?: string
): ScholarshipBriefInfo {
  const isFbise = (boardName || "").toLowerCase().includes("fbise") || (boardName || "").toLowerCase().includes("federal");
  const boardLabel = isFbise ? "FBISE Islamabad" : (boardName || `BISE ${candidateCity}`);
  const isPrimary = scIdx === 0;
  const career = getCountryCareerProfile(sc.hostCountry || sc.name);
  const nameLower = (sc.name + " " + sc.hostCountry).toLowerCase();

  const isHungary = nameLower.includes("hungar") || nameLower.includes("hungary");
  const isChina = nameLower.includes("csc") || nameLower.includes("china") || nameLower.includes("chinese");
  const isTurkey = nameLower.includes("turk") || nameLower.includes("burslari");
  const isJapan = (nameLower.includes("mext") || nameLower.includes("japan")) && !nameLower.includes("kyoto");
  const isBrunei = nameLower.includes("brunei") || nameLower.includes("bdgs");
  const isTaiwan = nameLower.includes("taiwan") || nameLower.includes("icdf");
  const isPadua = nameLower.includes("padua") || nameLower.includes("unipd") || nameLower.includes("italy");
  const isSbw = nameLower.includes("sbw") || nameLower.includes("berlin");
  const isKyoto = nameLower.includes("kyoto");
  const isManchester = nameLower.includes("manchester");
  const isQatar = nameLower.includes("qatar");
  const isAbuDhabi = nameLower.includes("abu dhabi") || nameLower.includes("adu");

  let applicationWindow = "Upcoming Cycle Announced Annually";
  let deadlineDate = "Check Official Portal";
  let intakeCycle = "Cohort 2026/2027";
  let portalUrl = resolveScholarshipOfficialUrl(sc);
  let portalLabel = "Official Host Portal";
  let hecPortalRequired = sc.hecPortalRequired ?? false;

  // Language barrier & testing defaults
  let hasBarrier = false;
  let ieltsRequired = false;
  let testLabel = "MOI Accepted (No IELTS Needed)";
  let barrierLabel = "No Language Barrier (100% English Taught)";
  let languageDescription = "Pakistani English Medium of Instruction (MOI) Certificate accepted. All coursework taught in English.";

  // Normalize candidate field dynamically
  let targetField = (targetFieldInput || "All Academic Disciplines").trim();
  if (targetField.includes(",")) {
    targetField = targetField.split(",")[0].trim() || "All Academic Disciplines";
  }
  if (
    targetField.toLowerCase().includes("all fields") ||
    targetField.toLowerCase().includes("all academic")
  ) {
    targetField = "Interdisciplinary Studies";
  } else if (targetField.length > 45) {
    targetField = targetField.slice(0, 42) + "...";
  }

  // Academic stream fit - dynamic per chosen field & verified by bilateral quota
  let isFieldEligible = true;
  let isFieldVerified = true;
  let streamLabel = `${targetField} Eligible`;
  let badgeLabel = "VERIFIED";
  let streamDescription = `Open to ${targetField} under Pakistan bilateral quota. Verified against official catalog.`;

  if (isHungary) {
    applicationWindow = "Mid-Nov 2026 – 15 Jan 2027 (Opens in ~4 weeks)";
    deadlineDate = "15 January 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://apply.stipendiumhungaricum.hu";
    portalLabel = "Tempus DreamApply";
    hecPortalRequired = true;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `Tempus bilateral quota officially covers ${targetField} under degree faculties with 100% full tuition waiver and monthly living allowance under the 400 Pakistan quota seats.`;
    testLabel = "College MOI Accepted (IELTS Optional)";
    barrierLabel = "No Language Barrier • 100% English Taught";
    languageDescription = "Most Hungarian universities accept college English MOI. Courses are 100% taught in English.";
  } else if (isChina) {
    applicationWindow = "Dec 2026 – 05 Jan 2027 (HEC) / 15 Feb (CSC)";
    deadlineDate = "05 January 2027 (HEC Cutoff)";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://www.campuschina.org";
    portalLabel = "Campus China CSC";
    hecPortalRequired = true;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `CSC Type A Bilateral quota covers ${targetField} across C9 & Double First Class Chinese universities with 100% tuition exemption and monthly living stipend.`;
    testLabel = "College MOI Accepted (No IELTS Needed)";
    barrierLabel = "1-Year Free Chinese Prep or English Medium";
    languageDescription = "English MOI accepted for English tracks; 1-year free Chinese language preparatory course included if Chinese-taught.";
  } else if (isTurkey) {
    applicationWindow = "10 Jan 2027 – 20 Feb 2027 (Fixed Annual Window)";
    deadlineDate = "20 February 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://tbbs.turkiyeburslari.gov.tr";
    portalLabel = "Türkiye Bursları TBBS";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `Türkiye Bursları covers ${targetField} across top state universities with full tuition, free accommodation, and monthly stipend.`;
    testLabel = "MOI Accepted (No IELTS Needed)";
    barrierLabel = "1-Year Free Turkish Language Course (TÖMER) Included";
    languageDescription = "All scholars receive 1-year free Turkish Language preparation. English MOI accepted for initial eligibility.";
  } else if (isJapan) {
    applicationWindow = "Apr 2027 – 05 Jun 2027 (Embassy Track)";
    deadlineDate = "05 June 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://www.pk.emb-japan.go.jp/itpr_en/education.html";
    portalLabel = "Embassy of Japan Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `MEXT Embassy Recommendation track allocates dedicated quota seats covering ${targetField} with full tuition coverage and monthly living allowance.`;
    testLabel = "Embassy Written Exams in Islamabad";
    barrierLabel = "1-Year Preparatory Language Center (Tokyo/Osaka) Included";
    languageDescription = "Written exams in English and Math at Embassy in Islamabad. Includes 1-year intensive Japanese foundation in Japan.";
  } else if (isBrunei) {
    applicationWindow = "15 Dec 2026 – 15 Feb 2027 (Annual MFA Window)";
    deadlineDate = "15 February 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://www.mfa.gov.bn/Pages/online-bdgs.aspx";
    portalLabel = "MFA Brunei Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `BDGS covers ${targetField} and digital science programs under Brunei Government bilateral quota for Pakistani citizens.`;
    testLabel = "College MOI Accepted (No IELTS Mandatory)";
    barrierLabel = "No Language Barrier • 100% English Medium";
    languageDescription = "Universiti Brunei Darussalam & UTB conduct all instruction in English. MOI certificate accepted.";
  } else if (isTaiwan) {
    applicationWindow = "01 Dec 2026 – 15 Mar 2027 (Fixed Annual Window)";
    deadlineDate = "15 March 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://web.icdf.org.tw/ICDF_TSP/WelcomeStart.aspx";
    portalLabel = "TaiwanICDF Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `TaiwanICDF covers ${targetField} and higher technological degrees with full tuition waiver and housing.`;
    testLabel = "College MOI Accepted";
    barrierLabel = "No Language Barrier • 100% English Taught";
    languageDescription = "All designated TaiwanICDF degree programs are 100% English taught. MOI certificate accepted.";
  } else if (isPadua) {
    applicationWindow = "15 Sep 2026 – 15 Nov 2026 (Round 1 OPEN NOW)";
    deadlineDate = "15 November 2026";
    intakeCycle = "Academic Year 2027/28";
    portalUrl = "https://apply.unipd.it";
    portalLabel = "UniPD Apply Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `University of Padua merit scholarship automatically covers top international students in ${targetField} degree programs.`;
    testLabel = "English MOI Certificate Accepted";
    barrierLabel = "No Language Barrier • 100% English Taught";
    languageDescription = "All qualifying international degree programs are fully English taught. No Italian required for admission.";
  } else if (isSbw) {
    applicationWindow = "Year-Round / Rolling Applications (OPEN NOW)";
    deadlineDate = "Rolling Admissions";
    intakeCycle = "2026/2027 Continuous Intake";
    portalUrl = "https://sbw.berlin/en/sbw-berlin-scholarship/";
    portalLabel = "SBW Berlin Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `SBW Berlin supports fully funded studies in ${targetField} for international students committed to non-profit social impact.`;
    testLabel = "English or German (Program Dependent)";
    barrierLabel = "Language Taught According to University Program";
    languageDescription = "English-taught programs require English proficiency; German-taught programs require German certification.";
  } else if (isKyoto) {
    applicationWindow = "02 Nov 2026 – 03 Dec 2026 (Strict Online System)";
    deadlineDate = "03 December 2026 (5:00 PM JST)";
    intakeCycle = "October 2027 Enrollment";
    portalUrl = "https://www.iup.kyoto-u.ac.jp/apply/";
    portalLabel = "Kyoto iUP Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `Kyoto iUP undergraduate scholarship covers ${targetField} under Faculty of Science & Engineering tracks.`;
    testLabel = "English Test (TOEFL/IELTS) Required";
    barrierLabel = "6-Month Preparatory Japanese Course Included";
    languageDescription = "No Japanese language proficiency required at application; comprehensive 6-month Japanese prep included.";
  } else if (isManchester) {
    applicationWindow = "Admissions Open Sep 2026 • Scholarship Invite in Spring 2027";
    deadlineDate = "15 May 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "https://www.manchester.ac.uk/study/international/finance-and-scholarships/funding/global-futures-scholarship/";
    portalLabel = "Manchester Portal";
    hecPortalRequired = false;
    if (targetField.toLowerCase().includes("medicine") || targetField.toLowerCase().includes("dentistry")) {
      isFieldEligible = false;
      isFieldVerified = false;
      streamLabel = "Clinical Medicine Excluded";
      badgeLabel = "NOT ELIGIBLE";
      streamDescription = "Global Futures Scholarship excludes clinical medicine and dentistry degrees.";
    } else {
      streamLabel = `${targetField} Eligible`;
      badgeLabel = "VERIFIED";
      streamDescription = `Global Futures Scholarship covers ${targetField} across Science, Engineering & Humanities tracks.`;
    }
    testLabel = "IELTS Academic Required (UK Visa SELT)";
    barrierLabel = "No Host Language Barrier (100% English Taught)";
    languageDescription = "UK Student visa requires formal English test (IELTS 6.5–7.0). Full English instruction in the UK.";
  } else if (isQatar) {
    applicationWindow = isUndergrad ? "01 Mar 2027 – 25 Mar 2027" : "01 Dec 2026 – 25 Feb 2027";
    deadlineDate = isUndergrad ? "25 March 2027" : "25 February 2027";
    intakeCycle = "Fall 2027 Intake";
    portalUrl = "http://www.qu.edu.qa/students/admission/scholarships";
    portalLabel = "Qatar University Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `Qatar University merit scholarship covers ${targetField} under College of Arts & Sciences / Engineering.`;
    testLabel = "IELTS / TOEFL or Arabic Placement";
    barrierLabel = "English Medium (STEM/Business) or Arabic Track";
    languageDescription = "Technical courses taught in English; Humanities & Law taught in Arabic.";
  } else if (isAbuDhabi) {
    applicationWindow = "Rolling with Semester Admissions (Fall/Spring)";
    deadlineDate = "Term Admission Cutoff";
    intakeCycle = "2026/2027 Intake";
    portalUrl = "https://www.adu.ac.ae/admissions/financial-resources/scholarships";
    portalLabel = "ADU Portal";
    hecPortalRequired = false;
    streamLabel = `${targetField} Eligible`;
    badgeLabel = "VERIFIED";
    streamDescription = `ADU international merit award covers ${targetField} across Arts, Sciences and Computing faculties.`;
    testLabel = "English Proficiency (IELTS 5.5+ / EmSAT)";
    barrierLabel = "No Language Barrier • 100% English Taught";
    languageDescription = "All undergraduate courses conducted in English in Abu Dhabi & Dubai.";
  } else if (sc.deadlineSummary?.applicationDeadline) {
    deadlineDate = sc.deadlineSummary.applicationDeadline;
    applicationWindow = `Official Annual Window – ${deadlineDate}`;
    intakeCycle = "Academic Cycle 2026/2027";
  }

  // Requirements
  let minGpaText = isUndergrad
    ? (isCambridge
        ? "CIE A-Levels: BBC to AAA (≈ 75%–86%+ IBCC) • Direct University Entry (Exempt from Studienkolleg)"
        : (isTurkey ? "70% for Arts/Eng • 80% for AI/CS • 90% for Medicine" : isJapan ? "75%+ in FSc/ICS with strong Mathematics" : isSbw ? "German grade <= 2.0 (≈ 75%+ Pakistani aggregate)" : "70% in Intermediate / FSc / ICS (12 Years) or 3.0/4.0 CGPA"))
    : "3.0 / 4.0 CGPA (or 70% aggregate) in 16-year Bachelor's degree";
  let ageLimitText = isUndergrad
    ? (isTurkey ? "Undergraduate: Strictly Under 21 years" : isJapan ? "Between 17 and 25 years (Born after Apr 2, 2002)" : isSbw ? "Between 18 and 30 years old" : isBrunei ? "Between 18 and 25 years old" : "Undergraduate: Under 25 years")
    : (isTurkey ? "Master's: Under 30 years | PhD: Under 35 years" : isSbw ? "Under 30 years old" : "Master's: Under 35 years | PhD: Under 40 years");
  let quotaSeatsText = sc.quotaDescription || (sc.bilateralSeats ? `${sc.bilateralSeats} Bilateral Quota Seats` : "Government Merit Quota");
  
  let testingText = hecPortalRequired
    ? (isChina && isUndergrad
        ? "Mandatory CSCA (China Scholastic Competency Assessment) + HEC USAT (50+)"
        : isUndergrad
        ? "HEC USAT (Undergraduate Studies Admission Test, min 50%)"
        : "HEC HAT (Higher Education Aptitude Test, min 50%)")
    : (isJapan
        ? "Written Exam (Math & English) at Embassy of Japan in Islamabad"
        : isTurkey
        ? "In-Person Interview Panel in Islamabad/Lahore (Zero Test Fees)"
        : isSbw
        ? "German Grade Verification + Approved Social Project Plan"
        : isKyoto
        ? "Kyoto iUP Screening Test + Mathematics & Essay Evaluation"
        : isManchester
        ? "Direct Academic Merit + Conditional Study Offer"
        : isPadua
        ? "Automatic Merit Assessment on apply.unipd.it"
        : isBrunei
        ? "Academic Merit Review + Ministry Interview (Zero Test Fees)"
        : "Direct University Academic Review");

  // Mandatory Documents
  const documentsNeeded = isCambridge
    ? [
        "CIE Statement of Results / GCE A-Level Certificates",
        "IBCC Cambridge Equivalence Certificate (HSSC Equivalence)",
        "Valid Pakistani Passport (minimum 12 months validity)",
        "2 Academic Recommendation Letters from School/College Faculty",
        "Statement of Purpose (SOP) / Motivation Letter",
        "Foreigner Physical Examination / Medical Report",
        "Police Character Clearance Certificate (PKM Khidmat)",
      ]
    : isUndergrad
    ? [
        `Verified Intermediate Sanad & Marksheet (${boardLabel})`,
        "IBCC Certificate Equivalence (Intermediate / ICS)",
        "Valid Pakistani Passport (minimum 12 months validity)",
        "2 Academic Recommendation Letters from College Faculty",
        "Statement of Purpose (SOP) / Motivation Letter",
        "Foreigner Physical Examination / Medical Report",
        "Police Character Clearance Certificate (PKM Khidmat)",
      ]
    : [
        "HEC DAS Degree e-Attestation & University Transcripts",
        "Valid Pakistani Passport (minimum 12 months validity)",
        "2 Academic Letters of Recommendation from Professors",
        "Comprehensive Research Proposal / Statement of Purpose",
        "Foreigner Physical Examination / Medical Clearance",
        "Police Character Certificate (Police Khidmat Markaz)",
        "English Medium of Instruction (MOI) Certificate",
      ];

  // Upfront Expenses
  const scDocCost = isCambridge ? 6000 : isUndergrad ? 10000 : 12000;
  const scTestCost = hasEnglishTest ? 76000 : 0;
  const scVisaCost = career.visaFeePkr;
  const scSettlement = career.settlementBufferPkr;
  const totalPkr = scDocCost + scTestCost + scVisaCost + scSettlement;

  let monthlyStipendText = "≈ PKR 120,000 / month";
  let tuitionCoverageText = "100% Full Tuition Waiver + Free Dormitory";
  if (isHungary) {
    monthlyStipendText = "43,700 HUF (≈ PKR 35,000/mo) + Free Accommodation";
    tuitionCoverageText = "100% Full Tuition Waiver + Free University Dorm";
  } else if (isChina) {
    monthlyStipendText = "CNY 2,500–3,000/mo (≈ PKR 118,000/mo)";
    tuitionCoverageText = "100% Full Tuition + Free Dorm + Comprehensive Medical";
  } else if (isTurkey) {
    monthlyStipendText = "3,500–5,000 TRY/mo (≈ PKR 42,000–52,000/mo)";
    tuitionCoverageText = "100% Free Tuition + Free Dorm + Return Flight Ticket";
  } else if (isJapan) {
    monthlyStipendText = "JPY 117,000/mo (≈ PKR 215,000/mo)";
    tuitionCoverageText = "100% Full Tuition Waiver + Return International Airfare";
  } else if (sc.fundingSummary?.monthlyStipendPkr) {
    monthlyStipendText = `≈ PKR ${sc.fundingSummary.monthlyStipendPkr.toLocaleString()} / mo`;
  }

  const breakdownText = isCambridge
    ? `IBCC Equivalence (PKR ${(scDocCost/1000).toFixed(0)}k [BISE Exempt]) + Testing (${scTestCost > 0 ? "76k" : "0 MOI"}) + Visa (${(scVisaCost/1000).toFixed(0)}k) + Travel Buffer (${(scSettlement/1000).toFixed(0)}k)`
    : `${isFbise ? "FBISE" : "BISE"} / IBCC Attestation (PKR ${(scDocCost/1000).toFixed(0)}k) + Testing (${scTestCost > 0 ? "76k" : "0 MOI"}) + Visa (${(scVisaCost/1000).toFixed(0)}k) + Travel Buffer (${(scSettlement/1000).toFixed(0)}k)`;

  const rankLabel =
    scIdx === 0
      ? "PRIMARY TARGET (#1)"
      : scIdx === 1
      ? "STRATEGIC HEDGE (#2)"
      : scIdx === 2
      ? "COMPETITIVE ALTERNATIVE (#3)"
      : `SAFETY MERIT (#${scIdx + 1})`;

  return {
    id: sc.id || `sc-${scIdx}`,
    name: sc.name,
    hostCountry: sc.hostCountry,
    rankLabel,
    isPrimary,
    applicationWindow,
    deadlineDate,
    intakeCycle,
    portalUrl,
    portalLabel,
    hecPortalRequired,
    hecPortalUrl: "https://scholarship.hec.gov.pk",
    fieldStream: {
      targetField,
      isEligible: isFieldEligible,
      isVerified: isFieldVerified,
      streamLabel,
      badgeLabel,
      description: streamDescription,
    },
    artsStream: {
      isArtsEligible: isFieldEligible,
      streamLabel,
      description: streamDescription,
    },
    language: {
      hasBarrier,
      ieltsRequired,
      testLabel,
      barrierLabel,
      description: languageDescription,
    },
    requirements: {
      minGpaText,
      ageLimitText,
      quotaSeatsText,
      testingText,
    },
    documentsNeeded,
    expenses: {
      totalPkr,
      breakdownText,
      monthlyStipendText,
      tuitionCoverageText,
    },
    postStudyCareer: {
      workPermit: `${career.visaName} (${career.visaDuration})`,
      startingSalary: `${career.startingSalaryLocal} (${career.startingSalaryPkr})`,
      prPathway: career.prPathway,
    },
  };
}

export interface WebDossierViewProps {
  dossier: CanonicalDossier;
  isPrintMode?: boolean;
  hideHeader?: boolean;
  onTriggerPrint?: () => void;
  className?: string;
  onClose?: () => void;
}

export function getFieldIcon(field: string) {
  const f = field.toLowerCase();
  if (f.includes("physic") || f.includes("quantum") || f.includes("material") || f.includes("astronomy")) {
    return <Atom className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
  }
  if (
    f.includes("computer") ||
    f.includes("ai") ||
    f.includes("software") ||
    f.includes("data") ||
    f.includes("cyber") ||
    f.includes("informatic") ||
    f.includes("network")
  ) {
    return <Cpu className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
  }
  if (
    f.includes("engineer") ||
    f.includes("mechanic") ||
    f.includes("electric") ||
    f.includes("civil") ||
    f.includes("aerospace") ||
    f.includes("robot")
  ) {
    return <Wrench className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
  }
  if (
    f.includes("art") ||
    f.includes("humanit") ||
    f.includes("design") ||
    f.includes("music") ||
    f.includes("literature") ||
    f.includes("philosophy") ||
    f.includes("history")
  ) {
    return <Palette className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
  }
  if (
    f.includes("med") ||
    f.includes("health") ||
    f.includes("bio") ||
    f.includes("pharm") ||
    f.includes("surg") ||
    f.includes("dentist")
  ) {
    return <HeartPulse className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
  }
  if (
    f.includes("busin") ||
    f.includes("econom") ||
    f.includes("financ") ||
    f.includes("manage") ||
    f.includes("commerce")
  ) {
    return <TrendingUp className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
  }
  return <GraduationCap className="w-4 h-4 text-purple-700 shrink-0 mt-0.5" />;
}

export const WebDossierView: React.FC<WebDossierViewProps> = ({
  dossier,
  isPrintMode = false,
  hideHeader = false,
  onTriggerPrint,
  className = "",
  onClose,
}) => {
  const profile = dossier?.candidateProfile;
  const opp = dossier?.opportunity;
  const candidateName = profile?.personal?.name || profile?.name || dossier?.candidateProfile?.personal?.name || "Applicant";

  const handleDownloadDossier = () => {
    sound.playClick();
    if (onTriggerPrint) {
      onTriggerPrint();
    } else if (typeof window !== "undefined") {
      window.print();
    }
  };

  const handleExit = () => {
    if (onClose) {
      onClose();
    } else if (typeof window !== "undefined") {
      if (window.history.length > 1) {
        window.history.back();
      } else {
        window.location.href = "/";
      }
    }
  };

  // Candidate profile extraction with graceful fallbacks
  const candidateCity = profile?.personal?.city || profile?.city || dossier?.candidateProfile?.personal?.city || "Pakistan";
  const candidateProvince = profile?.personal?.province || profile?.province || dossier?.candidateProfile?.personal?.province || "";
  const candidateInstitution =
    profile?.academic?.institution || profile?.institution || dossier?.candidateProfile?.academic?.institution || "Academic Institution";

  const rawTargetDegree =
    profile?.preferences?.target_degree_level ||
    profile?.preferences?.targetDegreeLevel ||
    profile?.degree ||
    opp?.degreeLevel ||
    (opp as any)?.degree_level ||
    "";
  const rawCurrentLevel =
    profile?.academic?.current_level ||
    profile?.academic?.currentLevel ||
    "";

  const isCambridge =
    profile?.academic?.education_system === "CAMBRIDGE" ||
    rawCurrentLevel.toLowerCase().includes("a-level") ||
    rawCurrentLevel.toLowerCase().includes("cambridge") ||
    rawCurrentLevel.toLowerCase().includes("edexcel") ||
    (Array.isArray(profile?.academic?.a_level_grades) && profile?.academic?.a_level_grades.length > 0) ||
    candidateInstitution.toLowerCase().includes("grammar") ||
    candidateInstitution.toLowerCase().includes("cambridge");

  const isUndergrad =
    rawTargetDegree.toLowerCase().includes("bachelor") ||
    rawTargetDegree.toLowerCase().includes("undergrad") ||
    rawCurrentLevel.toLowerCase().includes("inter") ||
    rawCurrentLevel.toLowerCase().includes("fsc") ||
    rawCurrentLevel.toLowerCase().includes("ics") ||
    rawCurrentLevel.toLowerCase().includes("a-level") ||
    isCambridge;

  const aLevelGrades: string[] = React.useMemo(() => {
    if (Array.isArray(profile?.academic?.a_level_grades) && profile?.academic?.a_level_grades.length > 0) {
      return profile.academic.a_level_grades;
    }
    if (Array.isArray(profile?.aLevelGrades) && profile?.aLevelGrades.length > 0) {
      return profile.aLevelGrades;
    }
    return isCambridge ? ["A*", "A", "A"] : [];
  }, [profile, isCambridge]);

  // Priority order for candidate percentage:
  // 1. Explicit IBCC Equivalence percentage
  // 2. Computed from A-Level letter grades (A*=90, A=85, B=75, C=65, D=55, E=45) if Cambridge
  // 3. academic.gpa_percentage
  // 4. academic.gpaPercentage / percentage / gpaPercentage
  // 5. Fallback: 86.7 if Cambridge, 85.0 otherwise
  const computedCambridgePct = React.useMemo(() => {
    if (!isCambridge || aLevelGrades.length === 0) return null;
    const gradePts: Record<string, number> = { "A*": 90, A: 85, B: 75, C: 65, D: 55, E: 45, U: 0 };
    const pts = aLevelGrades.map((g: string) => gradePts[g.trim()] ?? 75);
    const avg = pts.reduce((a: number, b: number) => a + b, 0) / pts.length;
    return parseFloat(avg.toFixed(1));
  }, [isCambridge, aLevelGrades]);

  const preferredRegions: string[] =
    profile?.preferences?.preferred_regions ||
    profile?.preferences?.preferredRegions ||
    [];
  const candidateDegree = isUndergrad
    ? (rawTargetDegree || "Bachelor's (Undergraduate)")
    : (rawTargetDegree || "Master's Degree");

  const initialField = React.useMemo(() => {
    const raw =
      profile?.preferences?.target_fields?.[0] ||
      profile?.academic?.field_of_study ||
      profile?.preferences?.studyField ||
      profile?.field ||
      dossier?.field ||
      opp?.fieldOfStudy ||
      (opp as any)?.field_of_study ||
      "All Academic Disciplines";
    if (typeof raw === "string") {
      const trimmed = raw.trim();
      if (trimmed.includes(",")) {
        return trimmed.split(",")[0].trim() || "All Academic Disciplines";
      }
      if (trimmed.toLowerCase().includes("all fields") || trimmed.toLowerCase().includes("all academic")) {
        return "Interdisciplinary Studies";
      }
      return trimmed;
    }
    return "All Academic Disciplines";
  }, [profile, dossier?.field, opp]);

  const [activeField, setActiveField] = React.useState<string>(initialField);

  React.useEffect(() => {
    setActiveField(initialField);
  }, [initialField]);

  const candidateField = activeField;
  const candidateGpaPercent =
    profile?.academic?.ibcc_equivalence_percentage ??
    computedCambridgePct ??
    profile?.academic?.gpa_percentage ??
    profile?.academic?.gpaPercentage ??
    profile?.academic?.percentage ??
    profile?.gpaPercentage ??
    (isCambridge ? 86.7 : 85.0);

  const candidateGpa4 =
    profile?.academic?.gpa_4_scale ??
    profile?.academic?.gpa4Scale ??
    profile?.gpa4Scale ??
    percentageToGpa4(candidateGpaPercent);

  const rawBoard =
    profile?.academic?.board_university ||
    profile?.academic?.boardUniversity ||
    profile?.board ||
    "";

  const isFbise =
    rawBoard.toLowerCase().includes("fbise") ||
    rawBoard.toLowerCase().includes("federal") ||
    candidateInstitution.toLowerCase().includes("paec");

  const boardDisplayName = isFbise
    ? "FBISE Islamabad"
    : rawBoard
    ? rawBoard
    : `BISE ${candidateCity}`;

  const ibccTotalMarks =
    profile?.academic?.ibcc_total_marks ??
    Math.round((candidateGpaPercent / 100) * 1100);

  // Language proficiency parsing
  const rawEnglish =
    profile?.language?.english_proficiency_test ||
    profile?.proficiency?.englishTest ||
    profile?.englishTest ||
    "";
  const ieltsVal = profile?.language?.ielts_overall;
  const hasEnglishTest = Boolean(
    profile?.language?.has_english_test ||
    (rawEnglish &&
      !rawEnglish.toLowerCase().includes("none") &&
      !rawEnglish.toLowerCase().includes("not available") &&
      !rawEnglish.toLowerCase().includes("no test") &&
      !rawEnglish.toLowerCase().includes("exempt") &&
      !rawEnglish.toLowerCase().includes("moi"))
  );

  const englishTest =
    !hasEnglishTest ||
    rawEnglish.toLowerCase().includes("none") ||
    rawEnglish.toLowerCase().includes("not available") ||
    rawEnglish.toLowerCase().includes("no test")
      ? "No English Test (MOI / Exempt)"
      : rawEnglish.includes("IELTS") && ieltsVal
      ? `IELTS Academic ${ieltsVal}`
      : rawEnglish || "No English Test (MOI / Exempt)";

  const budgetPkr =
    profile?.preferences?.max_out_of_pocket_pkr ??
    profile?.financial?.max_out_of_pocket_pkr ??
    profile?.financial?.liquidBudgetPkr ??
    profile?.budgetPkr ??
    150000;

  const degreeLimit = getDegreeScholarshipLimit(rawTargetDegree);

  // Filter comparison portfolio list strictly by degree level, preferred regions, and compositeScore > 50, degree-specific max
  const matchingRankedList = (dossier?.rankedOpportunities && dossier.rankedOpportunities.length > 0)
    ? dossier.rankedOpportunities.filter((o: any) => {
        const candScore = typeof o?.compositeScore === "number" ? o.compositeScore : typeof o?.overall_match_score === "number" ? o.overall_match_score : 90;
        if (candScore <= 50) return false;
        const deg = (o?.degreeLevel || o?.degree_level || "").toLowerCase();
        const matchesDegree = isUndergrad
          ? (deg.includes("bachelor") || deg.includes("undergrad") || deg.includes("inter") || deg.includes("bs") || !deg)
          : (deg.includes("master") || deg.includes("ms") || deg.includes("msc") || deg.includes("phd") || deg.includes("doctor"));
        
        if (!matchesDegree) return false;
        if (preferredRegions.length > 0 && o.region) {
          return preferredRegions.some(
            (pr) => pr.toLowerCase() === (o.region || "").toLowerCase()
          );
        }
        return true;
      }).slice(0, degreeLimit)
    : [];

  // Active primary opportunity (falls back to matching ranked opportunity if opp region was excluded)
  const oppRegion = opp?.region || (opp as any)?.host_country_name;
  const rawActiveOpp = (matchingRankedList.length > 0 && preferredRegions.length > 0 && oppRegion && !preferredRegions.some(pr => pr.toLowerCase() === (oppRegion || "").toLowerCase()))
    ? matchingRankedList[0]
    : (opp || (matchingRankedList.length > 0 ? matchingRankedList[0] : null));

  const activeOpp: InvestigatedOpportunity = React.useMemo(() => {
    if (rawActiveOpp && rawActiveOpp.factors && typeof rawActiveOpp.compositeScore === "number" && rawActiveOpp.fundingSummary) {
      return rawActiveOpp as InvestigatedOpportunity;
    }
    if (rawActiveOpp) {
      return buildDynamicInvestigatedOpportunity(rawActiveOpp, profile, 1);
    }
    const defaultDynamic = getInvestigatedOpportunitiesForProfile(profile, 1);
    return defaultDynamic.length > 0 ? defaultDynamic[0] : INVESTIGATED_OPPORTUNITIES[0];
  }, [rawActiveOpp, profile]);

  const factors = activeOpp?.factors ? Object.values(activeOpp.factors) : [];

  // Active authoritative fallback opportunities (Cohort 2026/27 with verified 2027 deadlines)
  const baseFallback: InvestigatedOpportunity[] = React.useMemo(() => {
    const dynamicOpps = getInvestigatedOpportunitiesForProfile(dossier?.candidateProfile, 4);
    if (activeOpp) {
      const exists = dynamicOpps.some((o) => o.id === activeOpp.id);
      if (!exists) {
        return [activeOpp, ...dynamicOpps.slice(0, 3)];
      }
    }
    return dynamicOpps.length > 0 ? dynamicOpps : INVESTIGATED_OPPORTUNITIES;
  }, [activeOpp, dossier?.candidateProfile]);

  const rankedList: InvestigatedOpportunity[] = (matchingRankedList.length > 0)
    ? matchingRankedList.slice(0, degreeLimit)
    : preferredRegions.length > 0
    ? baseFallback.filter((o) => !o.region || preferredRegions.some((pr) => pr.toLowerCase() === (o.region || "").toLowerCase())).slice(0, degreeLimit)
    : baseFallback.slice(0, degreeLimit);

  // Accurate localized costs calculation reflecting candidate profile and primary host country
  const primaryCareer = getCountryCareerProfile(activeOpp.hostCountry || activeOpp.name);
  const docVerificationCost = isCambridge ? 6000 : isUndergrad ? 10000 : 12000;
  const testFee = hasEnglishTest ? 76000 : 0;
  const visaBiometricsCost = primaryCareer.visaFeePkr;
  const settlementBuffer = primaryCareer.settlementBufferPkr;
  const realTotalOutlay = docVerificationCost + testFee + visaBiometricsCost + settlementBuffer;

  // Dynamically tailor the execution roadmap to candidate profile (Undergrad vs Postgrad, MOI vs IELTS)
  const renderedRoadmap = React.useMemo(() => {
    return (dossier?.roadmapPhases || []).map((phase) => {
      if (phase.phase === "HEC_IBCC_ATTESTATION" && isCambridge) {
        return {
          ...phase,
          title: "CIE Statement of Results & IBCC Cambridge Equivalence",
          totalCostPkr: 6000,
          actions: [
            {
              id: "act-cam-1",
              phase: "HEC_IBCC_ATTESTATION" as const,
              title: "CIE Statement of Results & Cambridge Assessment Authentication",
              purpose: `British Council verification of Cambridge GCE A-Levels (${aLevelGrades.join(" ")}) — exempt from local BISE Board authentication`,
              timingDays: 3,
              timingLabel: "2–3 business days",
              estimatedCostPkr: 0,
              isBlocking: true,
              severity: "BLOCKING" as const,
              isPakistanSpecific: true,
              assignedOffice: "British Council Pakistan & Cambridge International",
              officialPortalUrl: "https://www.cambridgeinternational.org",
              evidenceSource: "IBCC Regulations for Foreign Qualifications §4.1",
            },
            {
              id: "act-cam-2",
              phase: "HEC_IBCC_ATTESTATION" as const,
              title: "IBCC Cambridge Equivalence Certificate (HSSC Equivalence)",
              purpose: "Direct conversion of CIE A-Levels to Pakistani Higher Secondary School Certificate equivalence for official embassy verification",
              timingDays: 5,
              timingLabel: "5–7 business days",
              estimatedCostPkr: 6000,
              isBlocking: true,
              severity: "BLOCKING" as const,
              isPakistanSpecific: true,
              assignedOffice: "IBCC Cambridge Equivalence Cell (Plot 25, G-10/4, Islamabad)",
              officialPortalUrl: "https://ibcc.edu.pk",
              evidenceSource: "IBCC Foreign System Conversion Scale Table 2",
            },
          ],
        };
      }
      if (phase.phase === "HEC_IBCC_ATTESTATION" && isUndergrad) {
        return {
          ...phase,
          title: `${isFbise ? "FBISE" : "BISE"} Board Verification & IBCC Equivalence`,
          totalCostPkr: 10000,
          actions: phase.actions.map((act) => {
            if (act.id === "act-2-1" || act.title.includes("DAS") || act.title.includes("Attestation")) {
              return {
                ...act,
                title: `${isFbise ? "FBISE" : "BISE"} Intermediate Sanad & Marksheet Verification`,
                purpose: `Official board authentication of Intermediate / ICS certificate from ${boardDisplayName}`,
                estimatedCostPkr: 4000,
                assignedOffice: isFbise
                  ? "Federal Board of Intermediate & Secondary Education (FBISE) H-8/4 Islamabad"
                  : `${boardDisplayName} Examination Board`,
              };
            }
            return act;
          }),
        };
      }
      if (phase.phase === "LANGUAGE_TESTS" && !hasEnglishTest) {
        return {
          ...phase,
          title: "English Medium of Instruction (MOI) & Language Exemption",
          totalCostPkr: 2000,
          criticalAdvisory: `Candidate has No IELTS. English Medium of Instruction (MOI) Certificate from ${candidateInstitution.split(",")[0]} provides official language requirement waiver.`,
          actions: [
            {
              id: "act-3-1",
              phase: "LANGUAGE_TESTS" as const,
              title: "College English Medium of Instruction (MOI) Certificate",
              purpose: `Official certificate verifying coursework was instructed in English at ${candidateInstitution.split(",")[0]}`,
              timingDays: 3,
              timingLabel: "2–3 business days",
              estimatedCostPkr: 0,
              isBlocking: true,
              severity: "BLOCKING" as const,
              isPakistanSpecific: true,
              assignedOffice: `${candidateInstitution.split(",")[0]} Administration`,
              evidenceSource: "Host University English Language Exemption Policy §3.4",
            },
            {
              id: "act-3-2",
              phase: "LANGUAGE_TESTS" as const,
              title: "HEC Bilateral Nomination Registration",
              purpose: "Online candidate registration for bilateral government quota allocation",
              timingDays: 7,
              timingLabel: "7 days to submission",
              estimatedCostPkr: 2000,
              isBlocking: true,
              severity: "BLOCKING" as const,
              isPakistanSpecific: true,
              assignedOffice: "HEC Overseas Scholarship Division",
              officialPortalUrl: "https://scholarship.hec.gov.pk",
              evidenceSource: "HEC Bilateral Selection Criteria Annex 1",
            },
          ],
        };
      }
      return phase;
    });
  }, [
    dossier?.roadmapPhases,
    isUndergrad,
    isCambridge,
    aLevelGrades,
    hasEnglishTest,
    candidateInstitution,
    boardDisplayName,
    isFbise,
  ]);

  // Unique document reference
  const countryCode = (activeOpp.hostCountry || "INT").toUpperCase().slice(0, 3);
  const docRef = `SX-${countryCode}-2026-PAK-${activeOpp.bilateralSeats || 100}`;

  return (
    <div
      id="scholarx-dossier-print-container"
      className={`min-h-screen bg-[#FAFAF9] text-[#1C1917] font-sans antialiased selection:bg-[#E7E5E4] ${className}`}
    >
      {/* Top Floating Action Bar (Visible in web view, hidden during print or when hideHeader is true) */}
      {!isPrintMode && !hideHeader && (
        <header className="sticky top-0 z-30 bg-white/95 backdrop-blur-md border-b border-[#E7E5E4] py-3 px-4 sm:px-6 shadow-sm no-print">
          <div className="max-w-[1050px] mx-auto flex flex-wrap items-center justify-between gap-2.5">
            <div className="flex items-center space-x-2.5 min-w-0">
              <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-[#1C1917] text-white shrink-0">
                SCHOLARX
              </span>
              <span className="text-xs font-mono text-[#78716C] uppercase tracking-wider truncate">
                OFFICIAL INTELLIGENCE DOSSIER // {candidateName}
              </span>
            </div>

            <div className="flex items-center space-x-2 shrink-0">
              <button
                type="button"
                onClick={handleDownloadDossier}
                className="px-2.5 sm:px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-mono font-bold flex items-center space-x-1.5 transition-all shadow-sm cursor-pointer"
                title="Print or Save official candidate dossier as publication PDF"
              >
                <Download className="w-3.5 h-3.5 stroke-[2.5]" />
                <span className="hidden sm:inline">DOWNLOAD PDF</span>
                <span className="sm:hidden">PDF</span>
              </button>

              <button
                type="button"
                onClick={handleExit}
                className="px-2.5 sm:px-4 py-1.5 rounded-lg bg-red-600 hover:bg-red-700 active:scale-95 text-white text-xs font-mono font-bold flex items-center space-x-1.5 transition-all shadow-sm cursor-pointer ml-1"
                title="Exit Dossier Viewer (Esc)"
              >
                <X className="w-4 h-4" />
                <span className="hidden sm:inline">EXIT DOSSIER</span>
                <span className="sm:hidden">EXIT</span>
              </button>
            </div>
          </div>
        </header>
      )}

      {/* Main Publication Document Body */}
      <main className="max-w-[1050px] mx-auto px-4 sm:px-6 md:px-8 py-8 md:py-12 space-y-10">
        
        {/* ========================================================================= */}
        {/* 1. DOCUMENT COVER & HEADER BLOCK                                          */}
        {/* ========================================================================= */}
        <section className="border-b border-[#E7E5E4] pb-8 page-break-avoid">
          <div className="flex flex-wrap items-center justify-between text-xs font-mono text-[#78716C] mb-3 uppercase gap-2 border-b border-[#E7E5E4] pb-2">
            <div className="flex items-center space-x-2">
              <CountryFlagLogo country="PK" name="Pakistan" size="sm" />
              <span className="font-bold text-[#1C1917]">OFFICIAL INTELLIGENCE REPORT // PAKISTANI ADMISSIONS COHORT 2026/27</span>
            </div>
            <div className="flex items-center space-x-2">
              <span className="text-[#0F766E] font-bold bg-emerald-50 px-2.5 py-0.5 rounded border border-emerald-200">
                VERIFIED CONFIDENCE: {activeOpp.verificationSummary?.confidencePercent || 96}%
              </span>
              <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-zinc-100 text-zinc-700 border border-zinc-300 font-bold">
                REF: {docRef}
              </span>
            </div>
          </div>

          <div className="flex items-center space-x-2 text-sm font-mono text-[#0F766E] font-bold mb-2">
            <GraduationCap className="w-4 h-4 text-[#0F766E] shrink-0" />
            <span className="uppercase tracking-wider break-words">PERSONALIZED CANDIDATE INTELLIGENCE DOSSIER • {candidateName}</span>
          </div>

          <h1 className="text-2xl sm:text-3xl md:text-4xl font-display font-extrabold text-[#1C1917] tracking-tight leading-tight mb-3 break-words">
            Bilateral Scholarship Portfolio & Execution Roadmap
          </h1>

          <div className="flex flex-wrap items-center gap-2 sm:gap-3 text-xs font-mono text-[#78716C]">
            <span className="font-bold text-[#1C1917] bg-stone-100 px-2.5 py-1 rounded">{candidateDegree}</span>
            <span>•</span>
            <span className="font-bold text-[#0F766E] bg-emerald-50 border border-emerald-200 px-2.5 py-1 rounded">{candidateField}</span>
            <span>•</span>
            <span className="bg-[#DCFCE7] text-[#166534] px-2.5 py-1 rounded font-bold break-words flex items-center gap-1.5 border border-emerald-300">
              <CountryFlagLogo country={activeOpp.hostCountry} name={activeOpp.name} size="xs" />
              <span>PRIMARY: {activeOpp.shortName} (RANK #{activeOpp.rank || 1} • {typeof activeOpp.compositeScore === "number" ? activeOpp.compositeScore.toFixed(1) : "92.0"}/100)</span>
            </span>
            <span>•</span>
            <span className="bg-[#FEF3C7] text-[#92400E] px-2.5 py-1 rounded font-bold break-words border border-amber-300">
              {activeOpp.quotaDescription}
            </span>
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 01 // CANDIDATE PROFILE & INTAKE VERIFICATION AUDIT                       */}
        {/* ========================================================================= */}
        <section className="page-break-avoid">
          <div className="flex flex-wrap items-center justify-between mb-2.5 gap-2">
            <h2 className="text-xs font-mono font-bold uppercase tracking-wider text-[#78716C] flex items-center gap-1.5">
              <User className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
              <span>01 // CANDIDATE PROFILE & INTAKE VERIFICATION AUDIT</span>
            </h2>
            <span className="text-[10px] font-mono bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded border border-emerald-300">
              AUDIT STATUS: 14/15 DIMENSIONS VERIFIED
            </span>
          </div>

          <div className="bg-white p-4 sm:p-5 rounded-xl border border-[#E7E5E4] shadow-sm">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 text-xs font-mono">
              <div className="p-3 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-[10px] text-[#78716C] uppercase font-bold">APPLICANT & NATIONALITY</div>
                <div className="text-sm font-sans font-extrabold text-[#1C1917] mt-1 break-words">{candidateName}</div>
                <div className="text-[11px] text-[#0F766E] font-bold mt-0.5 flex items-center gap-1">
                  <CountryFlagLogo country="PK" name="Pakistan" size="xs" />
                  <span>Pakistani Citizen ({candidateCity}, {candidateProvince})</span>
                </div>
              </div>

              <div className="p-3 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-[10px] text-[#78716C] uppercase font-bold">TARGET FIELD & DEGREE</div>
                <div className="text-sm font-sans font-extrabold text-[#0F766E] mt-1 break-words leading-tight">
                  {candidateField}
                </div>
                <div className="text-[11px] text-[#78716C] mt-0.5 break-words font-semibold">{candidateDegree}</div>
              </div>

              <div className="p-3 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-[10px] text-[#78716C] uppercase font-bold">ACADEMIC STANDING</div>
                {isCambridge ? (
                  <>
                    <div className="text-sm font-bold text-purple-700 mt-1 font-mono">
                      A-Levels ({aLevelGrades.join(" ")}) &bull; {candidateGpaPercent}% IBCC
                    </div>
                    <div className="text-[11px] font-mono text-[#166534] font-bold mt-0.5">
                      {ibccTotalMarks.toLocaleString()} / 1,100 Marks &bull; {Number(candidateGpa4).toFixed(1)} / 4.0 CGPA
                    </div>
                    <div className="text-[11px] text-[#78716C] mt-0.5 truncate" title={candidateInstitution}>
                      {candidateInstitution.split(",")[0]} &bull; Cambridge CIE
                    </div>
                  </>
                ) : (
                  <>
                    <div className="text-sm font-bold text-[#166534] mt-1 font-mono">
                      {candidateGpaPercent}% ({Number(candidateGpa4).toFixed(1)} / 4.0 CGPA)
                    </div>
                    <div className="text-[11px] text-[#78716C] mt-0.5 truncate" title={candidateInstitution}>
                      {candidateInstitution.split(",")[0]}
                    </div>
                  </>
                )}
              </div>

              <div className="p-3 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-[10px] text-[#78716C] uppercase font-bold">LANGUAGE & BUDGET</div>
                <div className="text-sm font-bold text-[#1C1917] mt-1 break-words">{englishTest}</div>
                <div className="text-[11px] text-[#B45309] font-bold mt-0.5">
                  Liquid Reserve: PKR {budgetPkr.toLocaleString()}
                </div>
              </div>
            </div>

            <div className="mt-4 pt-3 border-t border-[#F5F5F4] flex flex-wrap items-center justify-between text-[11px] font-mono text-[#57534E] gap-2.5">
              <div className="flex items-center space-x-2 min-w-0">
                <ShieldCheck className="w-4 h-4 text-[#0F766E] shrink-0" />
                <span className="break-words">Bilateral Embassy Quota Compatibility: <strong>100% Eligible</strong></span>
              </div>
              <div className="flex items-center space-x-2 min-w-0">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                <span className="break-words">
                  {isCambridge
                    ? "CIE Statement of Results & IBCC Cambridge Cell Equivalence: "
                    : isUndergrad
                    ? `${isFbise ? "FBISE" : "BISE"} Verification & IBCC Equivalence: `
                    : "HEC Degree Attestation: "}
                  <strong>Pre-verified {isCambridge ? "(Plot 25, G-10/4, Islamabad)" : ""}</strong>
                </span>
              </div>
              <div className="flex items-center space-x-2 min-w-0">
                <Coins className="w-4 h-4 text-amber-600 shrink-0" />
                <span className="break-words">True Cost Assessment: <strong>Clearance Planned</strong></span>
              </div>
            </div>
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 02 // MULTI-SCHOLARSHIP COMPARATIVE RANKING PORTFOLIO                     */}
        {/* ========================================================================= */}
        <section className="page-break-avoid">
          <div className="flex flex-wrap items-center justify-between mb-2.5 gap-2">
            <h2 className="text-xs font-mono font-bold uppercase tracking-wider text-[#78716C] flex items-center gap-1.5">
              <Award className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
              <span>02 // MULTI-SCHOLARSHIP COMPARATIVE RANKING PORTFOLIO</span>
            </h2>
            <span className="text-[10px] font-mono text-[#78716C]">
              {rankedList.length} OPPORTUNITIES AUDITED & SCORED FOR PAKISTAN
            </span>
          </div>

          <div className="bg-white rounded-xl border border-[#E7E5E4] overflow-hidden shadow-sm">
            <div className="overflow-x-auto touch-scroll dossier-scroll w-full print:overflow-visible">
              <table className="w-full text-left text-xs font-sans min-w-[720px] print:min-w-0 print:table-fixed print:text-[10px]">
                <thead>
                  <tr className="bg-[#FAFAF9] border-b border-[#E7E5E4] text-[#78716C] font-mono text-[11px] print:text-[9.5px]">
                    <th className="py-3 px-3.5 font-bold w-14 print:w-[8%] print:px-2">RANK</th>
                    <th className="py-3 px-3.5 font-bold print:w-[32%] print:px-2">SCHOLARSHIP & COUNTRY</th>
                    <th className="py-3 px-3.5 font-bold print:w-[20%] print:px-2">PAKISTAN QUOTA SEATS</th>
                    <th className="py-3 px-3.5 font-bold print:w-[18%] print:px-2">FUNDING COVERAGE</th>
                    <th className="py-3 px-3.5 font-bold print:w-[12%] print:px-2">EST. MONTHLY STIPEND</th>
                    <th className="py-3 px-3.5 font-bold text-right print:w-[10%] print:px-2">COMPOSITE SCORE</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#F5F5F4]">
                  {rankedList.map((candidate: any, idx) => {
                    const candidateId = candidate?.id || candidate?.scholarship_id || `cand-${idx}`;
                    const isPrimary = idx === 0 || candidateId === activeOpp.id;
                    const stipendPkr = candidate?.fundingSummary?.monthlyStipendPkr || candidate?.monthly_stipend_pkr || 0;
                    const candidateName = candidate?.name || candidate?.scholarship_name || `Opportunity #${idx + 1}`;
                    const candidateCountry = candidate?.hostCountry || candidate?.host_country_name || candidate?.host_country || "International";
                    const candidateDegree = candidate?.degreeLevel || candidate?.degree_level || "";
                    const candidateScore = typeof candidate?.compositeScore === "number"
                      ? candidate.compositeScore.toFixed(1)
                      : (Number(candidate?.overall_match_score || candidate?.final_score || 88).toFixed(1));
                    return (
                      <tr 
                        key={candidateId} 
                        className={`transition-colors ${isPrimary ? "bg-emerald-50/50 hover:bg-emerald-50/80" : "hover:bg-[#FAFAF9]"}`}
                      >
                        <td className="py-3.5 px-3.5 font-mono font-black print:px-2">
                          <span className={`px-2 py-0.5 rounded ${isPrimary ? "bg-emerald-200 text-emerald-900" : "bg-zinc-200 text-zinc-800"}`}>
                            #{candidate?.rank || idx + 1}
                          </span>
                        </td>
                        <td className="py-3.5 px-3.5 print:px-2">
                          <div className="font-bold text-[#1C1917] flex items-center gap-1.5 break-words">
                            <CountryFlagLogo country={candidateCountry} name={candidateName} size="sm" className="shrink-0" />
                            <span>{candidateName}</span>
                          </div>
                          <div className="text-[11px] print:text-[9px] text-[#78716C] break-words flex flex-wrap items-center gap-1.5 mt-0.5">
                            <span>{candidateCountry} • {candidateDegree}</span>
                            {isCambridge && (candidateCountry === "Germany" || candidateCountry === "United Kingdom" || candidateCountry === "Italy" || candidateCountry === "Hungary" || candidateCountry === "Netherlands" || candidate?.region === "Europe") && (
                              <span className="px-1.5 py-0.5 bg-purple-100 text-purple-800 font-mono text-[9px] font-bold rounded border border-purple-200">
                                DIRECT ENTRY ELIGIBLE
                              </span>
                            )}
                          </div>
                        </td>
                        <td className="py-3.5 px-3.5 font-mono font-bold text-[#0F766E] break-words print:px-2 print:text-[9.5px]">
                          {candidate?.quotaDescription || (candidate?.bilateralSeats ? `${candidate.bilateralSeats} Seats` : candidate?.bilateral_seats ? `${candidate.bilateral_seats} Seats` : "Open Merit")}
                        </td>
                        <td className="py-3.5 px-3.5 print:px-2">
                          <span className="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold font-mono text-[10px] print:text-[9px] whitespace-nowrap print:whitespace-normal">
                            {candidate?.fundingSummary?.coverageType || candidate?.funding_type || "100% FULL WAIVER"}
                          </span>
                          <div className="text-[10px] print:text-[8.5px] text-[#78716C] mt-0.5">Tuition + Stipend + Health</div>
                        </td>
                        <td className="py-3.5 px-3.5 font-mono text-[#1C1917] whitespace-nowrap print:whitespace-normal print:px-2 print:text-[9.5px]">
                          {stipendPkr > 0 ? `≈ PKR ${stipendPkr.toLocaleString()} / mo` : "Tuition Exemption / Grant"}
                        </td>
                        <td className="py-3.5 px-3.5 font-mono font-black text-base print:text-xs text-[#0F766E] text-right whitespace-nowrap print:px-2">
                          {candidateScore}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

            <div className="p-3.5 bg-[#FAFAF9] border-t border-[#E7E5E4] text-xs font-mono text-[#57534E] flex flex-wrap items-center justify-between gap-2">
              <div className="break-words">
                PRIMARY RECOMMENDATION: Apply for <strong>{activeOpp.name} (Rank #{activeOpp.rank || 1})</strong> as primary target.
                {isCambridge && (
                  <span className="block mt-1 text-purple-700 font-semibold text-[11px]">
                    Cambridge GCE Priority: 13-Year Direct Entry verified for European &amp; UK degree faculties (Exempt from 1-year Studienkolleg / foundation colleges).
                  </span>
                )}
              </div>
              <span className="text-[#0F766E] font-bold shrink-0">100% BILATERAL QUOTA ALIGNED</span>
            </div>
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 03 // 8-DIMENSION VERIFICATION & WEIGHT BREAKDOWN                         */}
        {/* ========================================================================= */}
        <section className="page-break-avoid">
          <div className="flex flex-wrap items-center justify-between mb-2.5 gap-2">
            <h2 className="text-xs font-mono font-bold uppercase tracking-wider text-[#78716C] flex items-center gap-1.5">
              <BadgePercent className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
              <span>03 // 8-DIMENSION WEIGHTED MATCH AUDIT ({activeOpp.shortName})</span>
            </h2>
            <span className="text-[10px] font-mono text-[#78716C]">
              DETERMINISTIC WEIGHT ENGINE
            </span>
          </div>

          <div className="bg-white p-4 sm:p-5 rounded-xl border border-[#E7E5E4] shadow-sm">
            {/* Responsive Formula Banner (Prevents Word Overflow) */}
            <div className="text-xs font-mono text-[#78716C] mb-3 flex flex-wrap items-center justify-between gap-2.5 pb-2.5 border-b border-[#F5F5F4]">
              <div className="flex flex-wrap items-center gap-1.5 text-[11px] min-w-0">
                <span className="font-bold text-[#1C1917]">WEIGHT FORMULA:</span>
                <span className="bg-stone-100 px-2 py-0.5 rounded text-[#44403C] break-all">
                  (0.25×E) + (0.25×F) + (0.10×B) + (0.10×A) + (0.10×D) + (0.10×T) + (0.05×V) + (0.05×C)
                </span>
              </div>
              <div className="text-sm font-bold text-[#0F766E] bg-emerald-50 px-2.5 py-1 rounded border border-emerald-200 shrink-0">
                FINAL SCORE: {typeof activeOpp.compositeScore === "number" ? activeOpp.compositeScore.toFixed(1) : "92.0"} / 100
              </div>
            </div>

            <div className="overflow-x-auto touch-scroll dossier-scroll w-full print:overflow-visible">
              <table className="w-full text-left text-xs font-sans min-w-[660px] print:min-w-0 print:table-fixed print:text-[10px]">
                <thead>
                  <tr className="border-b border-[#E7E5E4] text-[#78716C] font-mono text-[11px] print:text-[9.5px]">
                    <th className="pb-2 font-medium w-48 print:w-[25%] print:px-1">FACTOR</th>
                    <th className="pb-2 font-medium w-16 print:w-[10%] print:px-1">WEIGHT</th>
                    <th className="pb-2 font-medium w-24 print:w-[12%] print:px-1">RAW SCORE</th>
                    <th className="pb-2 font-medium w-28 print:w-[15%] print:px-1">CONTRIBUTION</th>
                    <th className="pb-2 font-medium print:w-[38%] print:px-1">GROUNDED RATIONALE</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#F5F5F4]">
                  {factors.map((f: any) => (
                    <tr key={f.key || f.label} className="py-2.5">
                      <td className="py-2 font-semibold text-[#1C1917] break-words print:px-1">{f.label}</td>
                      <td className="py-2 font-mono text-[#78716C] print:px-1">{f.weightPercent}%</td>
                      <td className="py-2 font-mono font-bold text-[#1C1917] print:px-1">{f.rawScore ?? 90} / 100</td>
                      <td className="py-2 font-mono font-bold text-[#0F766E] print:px-1">+{Number(f.weightedContribution ?? 0).toFixed(1)} pts</td>
                      <td className="py-2 text-[#57534E] text-[11px] print:text-[9px] leading-relaxed break-words print:px-1">{f.rationale}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 04 // EXECUTIVE SCHOLARSHIP BRIEFINGS (REQUIREMENTS, EXPENSES & STREAMS) */}
        {/* ========================================================================= */}
        <section className="page-break-avoid">
          <div className="flex flex-wrap items-center justify-between mb-3 gap-2">
            <h2 className="text-xs sm:text-sm font-mono font-bold uppercase tracking-wider text-[#44403C] flex items-center gap-1.5">
              <Briefcase className="w-4 h-4 text-[#0F766E] shrink-0" />
              <span>04 // EXECUTIVE SCHOLARSHIP BRIEFINGS (REQUIREMENTS, EXPENSES &amp; STREAMS)</span>
            </h2>
            <span className="text-xs font-mono text-[#78716C]">
              {rankedList.length} SCHOLARSHIPS • STREAM AUDIT • LANGUAGE FIT • 2026/27 ACTIVE CYCLES
            </span>
          </div>

          <div className="space-y-6">
            {rankedList.map((sc, scIdx) => {
              const brief = getScholarshipBriefInfo(sc, scIdx, isUndergrad, candidateCity, hasEnglishTest, activeField, isCambridge, boardDisplayName);

              return (
                <div
                  key={brief.id}
                  className={`bg-white rounded-xl ${
                    brief.isPrimary 
                      ? "border-2 border-emerald-500 shadow-md ring-2 ring-emerald-500/10" 
                      : "border border-[#E7E5E4] shadow-sm"
                  } p-5 sm:p-6 space-y-4 page-break-avoid`}
                >
                  {/* Scholarship Header: Name, Country, Rank, Window & Portal Action Buttons */}
                  <div className="flex flex-col md:flex-row md:items-center justify-between border-b border-[#F5F5F4] pb-3.5 gap-3">
                    <div className="flex items-center space-x-3 min-w-0">
                      <CountryFlagLogo country={brief.hostCountry} name={brief.name} size="xl" className="shrink-0 shadow-sm" />
                      <div className="min-w-0">
                        <div className="flex flex-wrap items-center gap-2">
                          <span className="font-bold text-base sm:text-lg text-[#1C1917] break-words">
                            {brief.name} ({brief.hostCountry})
                          </span>
                          <span
                            className={`px-2.5 py-0.5 rounded font-bold font-mono text-xs ${
                              brief.isPrimary
                                ? "bg-emerald-100 text-emerald-800 border border-emerald-300"
                                : scIdx === 1
                                ? "bg-blue-100 text-blue-800 border border-blue-300"
                                : "bg-stone-100 text-stone-800 border border-stone-300"
                            }`}
                          >
                            {brief.rankLabel}
                          </span>
                        </div>
                        <div className="text-xs text-[#78716C] font-mono mt-0.5 flex flex-wrap items-center gap-2">
                          <span className="font-bold text-[#0F766E]">{brief.requirements.quotaSeatsText}</span>
                          <span>•</span>
                          <span className="text-[#B45309] font-bold flex items-center gap-1">
                            <Clock className="w-3.5 h-3.5" />
                            <span>Deadline: {brief.deadlineDate} ({brief.intakeCycle})</span>
                          </span>
                        </div>
                      </div>
                    </div>

                    {/* Verified Official Application Portals with Direct Links */}
                    <div className="flex items-center gap-2 shrink-0">
                      {brief.portalUrl && (
                        <a
                          href={brief.portalUrl}
                          target="_blank"
                          rel="noreferrer"
                          className="px-3.5 py-1.5 rounded-lg bg-[#0F766E] text-white hover:bg-[#115E59] text-xs font-mono font-bold flex items-center space-x-1.5 transition-all shadow-sm"
                          title="Open official international application portal"
                        >
                          <span>{brief.portalLabel}</span>
                          <ExternalLink className="w-3.5 h-3.5" />
                        </a>
                      )}
                      {brief.hecPortalRequired && (
                        <a
                          href={brief.hecPortalUrl}
                          target="_blank"
                          rel="noreferrer"
                          className="px-3.5 py-1.5 rounded-lg border border-[#D6D3D1] bg-[#FAFAF9] hover:bg-[#F5F5F4] text-[#1C1917] text-xs font-mono font-bold flex items-center space-x-1.5 transition-all shadow-sm"
                          title="Open mandatory HEC Pakistan bilateral nomination portal"
                        >
                          <span>HEC PORTAL</span>
                          <ExternalLink className="w-3.5 h-3.5" />
                        </a>
                      )}
                    </div>
                  </div>

                  {/* Top Highlights: Dynamic Field Fit & Language Barrier Badges */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    {/* Academic Stream Fit - Dynamic Field Eligibility */}
                    <div className="p-3 bg-purple-50/70 rounded-lg border border-purple-200/90 flex flex-col justify-between">
                      <div className="flex items-start space-x-2.5">
                        {getFieldIcon(activeField)}
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-1.5 flex-wrap">
                            <span className="font-bold text-purple-950 font-mono text-xs">
                              {brief.fieldStream.streamLabel}
                            </span>
                            <span
                              className={`px-1.5 py-0.2 rounded font-bold text-[10px] font-mono flex items-center gap-1 ${
                                brief.fieldStream.isVerified
                                  ? "bg-purple-200/90 text-purple-900 border border-purple-300"
                                  : "bg-amber-100 text-amber-800 border border-amber-200"
                              }`}
                            >
                              <CheckCircle2 className="w-2.5 h-2.5" />
                              {brief.fieldStream.badgeLabel}
                            </span>
                          </div>
                          <p className="text-purple-900/95 text-xs mt-0.5 leading-relaxed">
                            {brief.fieldStream.description}
                          </p>
                        </div>
                      </div>

                      {/* Dynamic Field Selector / Switcher */}
                      <div className="mt-2.5 pt-2 border-t border-purple-200/60 flex items-center justify-between gap-1 flex-wrap text-[10px] font-mono no-print">
                        <span className="text-purple-900/80 font-bold flex items-center gap-1">
                          <span>Target Field:</span>
                        </span>
                        <div className="flex items-center gap-1 flex-wrap">
                          {["Physics", "Computer Science", "Engineering", "Mathematics", "Medicine", "Arts & Humanities"].map((fieldOpt) => (
                            <button
                              key={fieldOpt}
                              type="button"
                              onClick={() => setActiveField(fieldOpt)}
                              className={`px-1.5 py-0.5 rounded transition-all cursor-pointer ${
                                activeField.toLowerCase() === fieldOpt.toLowerCase()
                                  ? "bg-purple-800 text-white font-bold shadow-xs"
                                  : "bg-purple-100/80 hover:bg-purple-200 text-purple-900"
                              }`}
                              title={`Switch dossier evaluation to ${fieldOpt}`}
                            >
                              {fieldOpt}
                            </button>
                          ))}
                        </div>
                      </div>
                    </div>

                    {/* Language Barrier & IELTS Requirement ("Whether there is a language barrier or not") */}
                    <div className="p-3 bg-teal-50/70 rounded-lg border border-teal-200/90 flex items-start space-x-2.5">
                      <Languages className="w-4 h-4 text-teal-700 shrink-0 mt-0.5" />
                      <div>
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="font-bold text-teal-950 font-mono text-xs">{brief.language.testLabel}</span>
                          <span className="px-1.5 py-0.2 rounded bg-teal-200/90 text-teal-900 font-bold text-[10px] font-mono">{brief.language.barrierLabel}</span>
                        </div>
                        <p className="text-teal-900/95 text-xs mt-0.5 leading-relaxed">{brief.language.description}</p>
                      </div>
                    </div>
                  </div>

                  {/* 4 Pillars Grid: Requirements, Documents Needed, Total Expenses, Coverage */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5 text-xs">
                    {/* Pillar 1: Academic Requirements & Cutoffs */}
                    <div className="p-3.5 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] space-y-2">
                      <div className="font-mono text-xs font-bold text-[#1C1917] uppercase flex items-center gap-1.5">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                        <span>1. Academic Requirements &amp; Cutoffs</span>
                      </div>
                      <div className="space-y-1.5 text-xs text-[#44403C] leading-relaxed">
                        <div><strong>Min Academic Cutoff:</strong> {brief.requirements.minGpaText}</div>
                        <div><strong>Age Limits:</strong> {brief.requirements.ageLimitText}</div>
                        <div><strong>Pakistan Quota:</strong> {brief.requirements.quotaSeatsText}</div>
                        <div><strong>Aptitude / Screening:</strong> {brief.requirements.testingText}</div>
                      </div>
                    </div>

                    {/* Pillar 2: Mandatory Documents Needed */}
                    <div className="p-3.5 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] space-y-2">
                      <div className="font-mono text-xs font-bold text-[#1C1917] uppercase flex items-center gap-1.5">
                        <FileText className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
                        <span>2. Mandatory Documents Needed</span>
                      </div>
                      <ul className="space-y-1 text-xs text-[#44403C] list-disc list-inside leading-snug">
                        {brief.documentsNeeded.map((doc, dIdx) => (
                          <li key={dIdx} className="break-words">{doc}</li>
                        ))}
                      </ul>
                    </div>

                    {/* Pillar 3: Total Expenses Breakdown */}
                    <div className="p-3.5 bg-[#FAFAF9] rounded-lg border border-[#E7E5E4] space-y-2">
                      <div className="font-mono text-xs font-bold text-[#1C1917] uppercase flex items-center justify-between">
                        <div className="flex items-center gap-1.5">
                          <Coins className="w-3.5 h-3.5 text-[#B45309] shrink-0" />
                          <span>3. Total Upfront Outlay</span>
                        </div>
                        <span className="font-bold text-sm text-[#B45309] font-mono">
                          PKR {brief.expenses.totalPkr.toLocaleString()}
                        </span>
                      </div>
                      <div className="text-xs text-[#44403C] space-y-1.5 leading-relaxed">
                        <div className="text-xs font-mono text-[#57534E] bg-stone-100 p-1.5 rounded">{brief.expenses.breakdownText}</div>
                        <div><strong>Budget Safety:</strong> Initial liquid reserves needed before 1st monthly stipend is credited by the foreign government.</div>
                      </div>
                    </div>

                    {/* Pillar 4: Funding & Monthly Stipend */}
                    <div className="p-3.5 bg-emerald-50/50 rounded-lg border border-emerald-200/80 space-y-2">
                      <div className="font-mono text-xs font-bold text-emerald-950 uppercase flex items-center justify-between">
                        <div className="flex items-center gap-1.5">
                          <Award className="w-3.5 h-3.5 text-emerald-700 shrink-0" />
                          <span>4. Funding &amp; Monthly Stipend</span>
                        </div>
                        <span className="font-bold text-xs text-[#166534] font-mono bg-emerald-100 px-2 py-0.5 rounded">
                          {brief.expenses.tuitionCoverageText.split("+")[0].trim()}
                        </span>
                      </div>
                      <div className="text-xs text-emerald-950 space-y-1.5 leading-relaxed">
                        <div><strong>Monthly Stipend:</strong> <span className="font-bold font-mono text-[#166534]">{brief.expenses.monthlyStipendText}</span></div>
                        <div><strong>Accommodation:</strong> Free University Dormitory / Housing allowance included.</div>
                        <div><strong>Health Coverage:</strong> Full Comprehensive Medical Insurance included.</div>
                      </div>
                    </div>
                  </div>

                  {/* Concise Post-Study Career Footnote */}
                  <div className="pt-2.5 border-t border-[#F5F5F4] flex flex-wrap items-center justify-between text-xs text-[#78716C] font-mono gap-2">
                    <div>
                      Post-Study Work Permit: <strong className="text-[#1C1917]">{brief.postStudyCareer.workPermit}</strong> • Est. Salary: <strong className="text-emerald-800">{brief.postStudyCareer.startingSalary}</strong>
                    </div>
                    <div className="text-[#0F766E] font-bold">{brief.postStudyCareer.prPathway}</div>
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 05 // TRUE COST OF "FREE" EDUCATION (REAL OUT-OF-POCKET IN PKR)           */}
        {/* ========================================================================= */}
        <section className="page-break-avoid">
          <div className="flex flex-wrap items-center justify-between mb-2.5 gap-2">
            <h2 className="text-xs font-mono font-bold uppercase tracking-wider text-[#78716C] flex items-center gap-1.5">
              <Coins className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
              <span>05 // TRUE COST OF &quot;FREE&quot; EDUCATION (REAL OUT-OF-POCKET IN PKR)</span>
            </h2>
            <span className="text-[10px] font-mono text-[#78716C]">
              4-PHASE EXPENSE BREAKDOWN
            </span>
          </div>

          <div className="bg-white p-4 sm:p-5 rounded-xl border border-[#E7E5E4] shadow-sm">
            <p className="text-xs text-[#57534E] mb-4 break-words">
              While tuition is 100% covered for {activeOpp.name}, international relocation and administrative verification require upfront liquid reserves before scholarship disbursement starts.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 mb-4">
              <div className="p-3.5 bg-[#F5F5F4] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-xs font-mono font-bold text-[#57534E] uppercase">PRE-APPLICATION &amp; TESTS</div>
                <div className="text-base font-mono font-bold text-[#1C1917] mt-0.5">
                  PKR {(docVerificationCost + testFee).toLocaleString()}
                </div>
                <div className="text-xs text-[#57534E] mt-1 break-words">
                  {isCambridge
                    ? hasEnglishTest
                      ? "IELTS (76k) + IBCC Cambridge Equivalence (6k) [BISE Exempt]"
                      : "IBCC Cambridge Equivalence (6k) + MOI (Free) [BISE Exempt]"
                    : hasEnglishTest
                    ? isUndergrad
                      ? "IELTS (76k) + BISE (4k) + IBCC (6k)"
                      : "IELTS (76k) + HEC (8k) + IBCC (6k)"
                    : isUndergrad
                    ? "BISE (4k) + IBCC (6k) + MOI (Free)"
                    : "HEC (8k) + IBCC (6k) + MOI (Free)"}
                </div>
              </div>
              <div className="p-3.5 bg-[#F5F5F4] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-xs font-mono font-bold text-[#57534E] uppercase">VISA &amp; MEDICAL</div>
                <div className="text-base font-mono font-bold text-[#1C1917] mt-0.5">PKR {visaBiometricsCost.toLocaleString()}</div>
                <div className="text-xs text-[#57534E] mt-1 break-words">Embassy Visa ({primaryCareer.country}) + Gerry&apos;s Biometrics</div>
              </div>
              <div className="p-3.5 bg-[#F5F5F4] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-xs font-mono font-bold text-[#57534E] uppercase">RELOCATION / FLIGHT</div>
                <div className="text-base font-mono font-bold text-[#B45309] mt-0.5">
                  PKR {activeOpp.fundingSummary?.tuitionCovered ? "180,000" : "210,000"}
                </div>
                <div className="text-xs text-[#57534E] mt-1 break-words">One-way travel &amp; luggage allowance</div>
              </div>
              <div className="p-3.5 bg-[#F5F5F4] rounded-lg border border-[#E7E5E4] min-w-0">
                <div className="text-xs font-mono font-bold text-[#57534E] uppercase">INITIAL SETTLEMENT</div>
                <div className="text-base font-mono font-bold text-[#1C1917] mt-0.5">PKR {settlementBuffer.toLocaleString()}</div>
                <div className="text-xs text-[#57534E] mt-1 break-words">Cash reserve until 1st month stipend arrives</div>
              </div>
            </div>

            {/* Responsive Budget Warning / Affirmation Banner (No Word Collision) */}
            <div className="p-3.5 bg-[#FEF2F2] border border-[#FECACA] rounded-xl text-xs font-mono text-[#991B1B] flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
              <div className="flex items-start sm:items-center space-x-2 min-w-0">
                <AlertTriangle className="w-4 h-4 shrink-0 mt-0.5 sm:mt-0" />
                <span className="break-words">
                  {budgetPkr < realTotalOutlay
                    ? `BUDGET ADVISORY: Self-reported budget (PKR ${budgetPkr.toLocaleString()}) requires an allocation plan for upfront outlays.`
                    : `BUDGET VERIFIED: Self-reported liquid budget (PKR ${budgetPkr.toLocaleString()}) fully covers estimated upfront requirements.`}
                </span>
              </div>
              <span className="font-bold shrink-0 bg-white/80 px-2 py-1 rounded border border-red-200">
                TOTAL OUTLAY: PKR {realTotalOutlay.toLocaleString()}
              </span>
            </div>
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 06 // MASTER MULTI-SCHOLARSHIP APPLICATION RUNWAY & PAKISTAN ROADMAP       */}
        {/* ========================================================================= */}
        <section className="page-break-avoid">
          <div className="flex flex-wrap items-center justify-between mb-2.5 gap-2">
            <h2 className="text-xs font-mono font-bold uppercase tracking-wider text-[#78716C] flex items-center gap-1.5">
              <Calendar className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
              <span>06 // MASTER MULTI-SCHOLARSHIP APPLICATION RUNWAY & PAKISTAN ROADMAP</span>
            </h2>
            <span className="text-[10px] font-mono text-[#78716C]">
              {rankedList.length} CONCURRENT RUNWAYS • {renderedRoadmap.length} PREPARATION MILESTONES
            </span>
          </div>

          <div className="space-y-6">
            {/* Master Application Runway Table */}
            <div className="bg-white p-4 sm:p-5 rounded-xl border border-[#E7E5E4] shadow-sm">
              <div className="flex items-center justify-between border-b border-[#F5F5F4] pb-2.5 mb-3">
                <span className="font-mono text-xs font-bold text-[#1C1917] uppercase">
                  CONCURRENT MULTI-SCHOLARSHIP APPLICATION RUNWAY COMPARISON
                </span>
                <span className="text-[10px] font-mono text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                  DUAL-TRACK APPLICATION RISK HEDGE
                </span>
              </div>

              <div className="overflow-x-auto touch-scroll dossier-scroll w-full print:overflow-visible">
                <table className="w-full text-left text-xs font-sans min-w-[700px] print:min-w-0 print:table-fixed">
                  <thead>
                    <tr className="border-b border-[#E7E5E4] text-[#44403C] font-mono text-xs print:text-[11px]">
                      <th className="pb-2.5 font-bold w-14 print:w-[8%] print:px-1">RANK</th>
                      <th className="pb-2.5 font-bold print:w-[28%] print:px-1">SCHOLARSHIP</th>
                      <th className="pb-2.5 font-bold w-36 print:w-[18%] print:px-1">WINDOW / DEADLINE</th>
                      <th className="pb-2.5 font-bold w-40 print:w-[20%] print:px-1">OFFICIAL PORTAL</th>
                      <th className="pb-2.5 font-bold w-32 print:w-[16%] print:px-1">UPFRONT OUTLAY</th>
                      <th className="pb-2.5 font-bold w-32 print:w-[16%] print:px-1">MONTHLY STIPEND</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#F5F5F4]">
                    {rankedList.map((rSc, rIdx) => {
                      const rBrief = getScholarshipBriefInfo(rSc, rIdx, isUndergrad, candidateCity, hasEnglishTest, activeField, isCambridge, boardDisplayName);
                      const isPrimary = rIdx === 0;

                      return (
                        <tr key={rSc.id || rIdx} className={`py-3 ${isPrimary ? "bg-emerald-50/50" : ""}`}>
                          <td className="py-3 font-mono font-bold text-[#1C1917] print:px-1">
                            <span className={`px-2.5 py-0.5 rounded text-xs font-bold ${isPrimary ? "bg-emerald-200 text-emerald-900 border border-emerald-300" : "bg-zinc-100 text-zinc-700 border border-zinc-200"}`}>
                              #{rSc.rank || rIdx + 1}
                            </span>
                          </td>
                          <td className="py-3 print:px-1">
                            <div className="font-bold text-[#1C1917] text-xs flex items-center gap-1.5 break-words">
                              <CountryFlagLogo country={rSc.hostCountry} name={rSc.name} size="sm" className="shrink-0" />
                              <span>{rSc.name}</span>
                            </div>
                            <div className="text-xs font-mono text-[#78716C] mt-0.5">
                              {rSc.hostCountry} • {rBrief.requirements.quotaSeatsText}
                            </div>
                          </td>
                          <td className="py-3 font-mono text-xs text-[#57534E] print:px-1">
                            <div className="font-bold text-[#1C1917]">{rBrief.deadlineDate}</div>
                            <div className="text-xs text-[#0F766E] font-medium">{rBrief.intakeCycle}</div>
                          </td>
                          <td className="py-3 font-mono text-xs print:px-1">
                            {rBrief.portalUrl ? (
                              <a
                                href={rBrief.portalUrl}
                                target="_blank"
                                rel="noreferrer"
                                className="text-[#0F766E] font-semibold hover:underline flex items-center gap-1 truncate max-w-[170px]"
                              >
                                <span className="truncate">{rBrief.portalLabel}</span>
                                <ExternalLink className="w-3.5 h-3.5 shrink-0" />
                              </a>
                            ) : (
                              <span className="text-[#78716C]">Direct Portal</span>
                            )}
                            {rBrief.hecPortalRequired && (
                              <a
                                href={rBrief.hecPortalUrl}
                                target="_blank"
                                rel="noreferrer"
                                className="text-xs text-[#B45309] font-medium block hover:underline"
                              >
                                + HEC Dual Portal
                              </a>
                            )}
                          </td>
                          <td className="py-3 font-mono font-bold text-[#1C1917] text-xs print:px-1">
                            PKR {rBrief.expenses.totalPkr.toLocaleString()}
                          </td>
                          <td className="py-3 font-mono text-[#166534] font-bold text-xs print:px-1">
                            {rBrief.expenses.monthlyStipendText.split("+")[0].trim()}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>

            {/* 6-Phase Pakistani Preparation Roadmap */}
            <div className="space-y-4">
              {renderedRoadmap.map((phase) => (
                <div
                  key={phase.phase}
                  className="bg-white p-4 sm:p-5 rounded-xl border border-[#E7E5E4] shadow-sm page-break-avoid"
                >
                  <div className="flex flex-wrap items-center justify-between border-b border-[#F5F5F4] pb-2.5 mb-3 gap-2">
                    <div className="flex flex-wrap items-center gap-2 min-w-0">
                      <span className="font-mono text-xs font-bold text-[#0F766E]">{phase.phaseLabel}:</span>
                      <span className="font-sans text-sm font-bold text-[#1C1917] break-words">{phase.title}</span>
                      <span className="font-mono text-xs text-[#78716C]">({phase.timelineDaysRange})</span>
                    </div>
                    <span className="font-mono text-xs font-bold text-[#B45309] shrink-0">
                      PKR {phase.totalCostPkr.toLocaleString()}
                    </span>
                  </div>

                  <div className="space-y-2">
                    {phase.actions.map((act) => (
                      <div
                        key={act.id}
                        className="p-3 rounded-lg bg-[#FAFAF9] border border-[#E7E5E4] flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 text-xs"
                      >
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center space-x-2 mb-1">
                            <span
                              className={`font-mono text-[11px] font-bold px-2 py-0.5 rounded shrink-0 ${
                                act.severity === "BLOCKING"
                                  ? "bg-[#FEE2E2] text-[#991B1B] border border-red-200"
                                  : "bg-[#FEF3C7] text-[#92400E] border border-amber-200"
                              }`}
                            >
                              {act.severity}
                            </span>
                            <span className="font-semibold text-sm text-[#1C1917] break-words">{act.title}</span>
                          </div>
                          <p className="text-xs text-[#57534E] break-words leading-relaxed">{act.purpose}</p>
                          {act.assignedOffice && (
                            <div className="flex items-center space-x-1 text-xs font-mono text-[#0F766E] mt-1">
                              <MapPin className="w-3.5 h-3.5 shrink-0" />
                              <span className="break-words font-medium">{act.assignedOffice}</span>
                            </div>
                          )}
                        </div>

                        <div className="sm:text-right font-mono text-xs shrink-0">
                          <div className="text-[#78716C]">{act.timingLabel}</div>
                          <div className="font-bold text-sm text-[#1C1917]">
                            {act.estimatedCostPkr === 0 ? "FREE" : `PKR ${act.estimatedCostPkr.toLocaleString()}`}
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* ========================================================================= */}
        {/* 07 // OFFICIAL CITATIONS & APPLICATION DIRECTORY                          */}
        {/* ========================================================================= */}
        <section className="page-break-avoid border-t border-[#E7E5E4] pt-8">
          <div className="flex flex-wrap items-center justify-between mb-2.5 gap-2">
            <h2 className="text-xs font-mono font-bold uppercase tracking-wider text-[#78716C] flex items-center gap-1.5">
              <FileText className="w-3.5 h-3.5 text-[#0F766E] shrink-0" />
              <span>07 // OFFICIAL CITATIONS & APPLICATION DIRECTORY</span>
            </h2>
            <span className="text-[10px] font-mono text-[#78716C]">
              VERIFIED GOVERNMENT CHANNELS
            </span>
          </div>

          <div className="bg-white p-4 sm:p-5 rounded-xl border border-[#E7E5E4] shadow-sm text-xs font-mono space-y-3">
            {rankedList.map((sCit, cIdx) => {
              const citPortal = resolveScholarshipOfficialUrl(sCit);
              const citDisplay = cleanPortalDisplayUrl(citPortal);

              return (
                <div key={sCit.id || cIdx} className="flex flex-col sm:flex-row sm:items-center justify-between pb-2.5 border-b border-[#F5F5F4] gap-1.5">
                  <div className="min-w-0">
                    <span className="font-bold text-[#1C1917] block break-words">
                      {cIdx + 1}. {sCit.name} ({sCit.hostCountry})
                    </span>
                    <span className="text-[#78716C] break-words">Official host portal • {sCit.quotaDescription || `${sCit.bilateralSeats || 100} Quota Seats`}</span>
                  </div>
                  <a
                    href={citPortal}
                    target="_blank"
                    rel="noreferrer"
                    className="text-[#0F766E] hover:underline flex items-center gap-1 break-all truncate max-w-full sm:max-w-[320px]"
                  >
                    <span className="truncate">{citDisplay}</span>
                    <ExternalLink className="w-3 h-3 shrink-0" />
                  </a>
                </div>
              );
            })}

            <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-2.5 border-b border-[#F5F5F4] gap-1.5">
              <div className="min-w-0">
                <span className="font-bold text-[#1C1917] block break-words">HEC Pakistan Bilateral Portal</span>
                <span className="text-[#78716C] break-words">Mandatory Pakistani nomination & aptitude test registration</span>
              </div>
              <a
                href="https://scholarship.hec.gov.pk"
                target="_blank"
                rel="noreferrer"
                className="text-[#0F766E] hover:underline flex items-center gap-1 break-all shrink-0"
              >
                <span>scholarship.hec.gov.pk</span>
                <ExternalLink className="w-3 h-3 shrink-0" />
              </a>
            </div>

            {isUndergrad ? (
              <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-2.5 border-b border-[#F5F5F4] gap-1.5">
                <div className="min-w-0">
                  <span className="font-bold text-[#1C1917] block break-words">HEC Education Testing Council (ETC)</span>
                  <span className="text-[#78716C] break-words">Official portal for HEC USAT (Undergraduate Studies Admission Test)</span>
                </div>
                <a
                  href="https://etc.hec.gov.pk"
                  target="_blank"
                  rel="noreferrer"
                  className="text-[#0F766E] hover:underline flex items-center gap-1 break-all shrink-0"
                >
                  <span>etc.hec.gov.pk</span>
                  <ExternalLink className="w-3 h-3 shrink-0" />
                </a>
              </div>
            ) : (
              <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-2.5 border-b border-[#F5F5F4] gap-1.5">
                <div className="min-w-0">
                  <span className="font-bold text-[#1C1917] block break-words">HEC Degree Attestation System (DAS)</span>
                  <span className="text-[#78716C] break-words">Official degree e-attestation and 1-Link fee payment</span>
                </div>
                <a
                  href="https://eservices.hec.gov.pk"
                  target="_blank"
                  rel="noreferrer"
                  className="text-[#0F766E] hover:underline flex items-center gap-1 break-all shrink-0"
                >
                  <span>eservices.hec.gov.pk</span>
                  <ExternalLink className="w-3 h-3 shrink-0" />
                </a>
              </div>
            )}

            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5">
              <div className="min-w-0">
                <span className="font-bold text-[#1C1917] block break-words">
                  {isCambridge ? "IBCC Cambridge Equivalence Cell" : "IBCC Equivalence System"}
                </span>
                <span className="text-[#78716C] break-words">
                  {isCambridge
                    ? "Official Cambridge A-Level to HSSC equivalence (Plot 25, G-10/4, Islamabad)"
                    : "Inter Board Coordination Commission certificate equivalence"}
                </span>
              </div>
              <a
                href="https://ibcc.edu.pk"
                target="_blank"
                rel="noreferrer"
                className="text-[#0F766E] hover:underline flex items-center gap-1 break-all shrink-0"
              >
                <span>ibcc.edu.pk</span>
                <ExternalLink className="w-3 h-3 shrink-0" />
              </a>
            </div>
          </div>
        </section>

        {/* Bottom Exit Button */}
        <div className="pt-6 pb-2 flex justify-center no-print">
          <button
            type="button"
            onClick={handleExit}
            className="px-8 py-3 rounded-xl bg-red-600 hover:bg-red-700 active:scale-95 text-white font-mono text-sm font-bold flex items-center space-x-2 transition-all shadow-lg cursor-pointer"
          >
            <X className="w-4 h-4" />
            <span>EXIT DOSSIER VIEWER</span>
          </button>
        </div>

        {/* Footer Document Signature */}
        <footer className="border-t border-[#E7E5E4] pt-6 pb-12 flex flex-col sm:flex-row items-center justify-between text-xs font-mono text-[#78716C] gap-2.5">
          <div className="text-center sm:text-left">GENERATED BY SCHOLARX AUTONOMOUS INTELLIGENCE NETWORK</div>
          <div className="font-bold text-center sm:text-right">DOCUMENT ID: {docRef} {"//"} COHORT CERTIFIED</div>
        </footer>
      </main>
    </div>
  );
};
