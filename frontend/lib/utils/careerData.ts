/**
 * ScholarX Country Career & Post-Study Immigration Profiles
 * 
 * Provides country-specific post-study work visas, local + PKR graduate salary ranges,
 * permanent residency pathways, out-of-pocket visa & biometrics fees, and step-by-step
 * application blueprints tailored to Pakistani scholars.
 */

export interface CountryCareerProfile {
  country: string;
  visaName: string;
  visaDuration: string;
  visaDetails: string;
  startingSalaryLocal: string;
  startingSalaryPkr: string;
  salaryContext: string;
  prPathway: string;
  prDetails: string;
  visaFeePkr: number;
  settlementBufferPkr: number;
  defaultPortalName: string;
}

export interface ApplicationStep {
  stepNumber: number;
  title: string;
  timeline: string;
  location: string;
  costPkr: number;
  description: string;
  actionUrl?: string;
  isMilestone?: boolean;
}

export const COUNTRY_CAREER_PROFILES: Record<string, CountryCareerProfile> = {
  australia: {
    country: "Australia",
    visaName: "Temporary Graduate Visa (Subclass 485)",
    visaDuration: "2 to 4 Years (Post-Higher Education Work Stream)",
    visaDetails: "Unrestricted Australian work rights to gain professional employment in your field of qualification.",
    startingSalaryLocal: "AUD $68,000 – $88,000 / Year",
    startingSalaryPkr: "≈ PKR 12,200,000 – 15,800,000 / yr",
    salaryContext: "High demand in Software Engineering, Data Analytics, Mining/Civil Engineering, and Healthcare in Sydney, Melbourne, and Brisbane.",
    prPathway: "Subclass 189 / 190 Skilled Points-Tested Migration",
    prDetails: "Direct pathway to Australian Permanent Residency (PR) via Points Test and State Nomination without requiring employer sponsorship.",
    visaFeePkr: 145000,
    settlementBufferPkr: 150000,
    defaultPortalName: "Australian University Admissions & RTP Portal",
  },
  turkey: {
    country: "Türkiye",
    visaName: "Short-Term Post-Graduation Residence Permit (İkamet)",
    visaDuration: "1 Year (Renewable with employment contract)",
    visaDetails: "Allows international graduates to transition to work authorization through employer sponsorship across Türkiye.",
    startingSalaryLocal: "TRY 350,000 – 550,000 / Year",
    startingSalaryPkr: "≈ PKR 2,800,000 – 4,400,000 / yr",
    salaryContext: "Vibrant tech and aerospace hubs in Istanbul and Ankara; strong bilateral trade networks with Pakistani enterprises.",
    prPathway: "Long-Term Residence Permit & Turkish Citizenship",
    prDetails: "Eligible for permanent residency and citizenship application after 5 years of legal, continuous employment.",
    visaFeePkr: 45000,
    settlementBufferPkr: 60000,
    defaultPortalName: "Türkiye Bursları Başvuru Portal",
  },
  china: {
    country: "China",
    visaName: "Z-Visa / Category B Work Permit",
    visaDuration: "1 to 2 Years (Renewable with employment)",
    visaDetails: "Chinese university graduates with high marks or Master's degrees are eligible for direct work permits without previous 2-year foreign work experience.",
    startingSalaryLocal: "RMB 120,000 – 210,000 / Year",
    startingSalaryPkr: "≈ PKR 4,600,000 – 8,100,000 / yr",
    salaryContext: "Global technology hubs in Shenzhen, Shanghai, Beijing, and Hangzhou; strong preference for bilingual CPEC technical leaders.",
    prPathway: "China Permanent Residence & Bilateral CPEC Leadership",
    prDetails: "Direct transition into multinational CPEC enterprises, research institute fellowships, or multi-year high-talent work permits.",
    visaFeePkr: 38000,
    settlementBufferPkr: 65000,
    defaultPortalName: "China Scholarship Information System (CSC Online)",
  },
  germany: {
    country: "Germany",
    visaName: "18-Month Jobseeker Visa (AufenthG §20 Abs. 3)",
    visaDuration: "18 Months (Unrestricted work rights)",
    visaDetails: "Graduates of German universities are granted 18 months of unrestricted work rights to find a role matching their qualification.",
    startingSalaryLocal: "€48,000 – €64,000 / Year",
    startingSalaryPkr: "≈ PKR 14,400,000 – 19,200,000 / yr",
    salaryContext: "Critical engineering and software developer shortages across Munich, Berlin, Frankfurt, and Stuttgart.",
    prPathway: "EU Blue Card & German Permanent Settlement (Niederlassungserlaubnis)",
    prDetails: "Permanent residency granted in as little as 21 months of employment with B1 German (or 27 months with basic German).",
    visaFeePkr: 48000,
    settlementBufferPkr: 120000,
    defaultPortalName: "DAAD Portal & Uni-Assist Germany",
  },
  hungary: {
    country: "Hungary",
    visaName: "9-Month Study-to-Work Residence Permit",
    visaDuration: "9 Months",
    visaDetails: "Graduates receive a 9-month stay permit to secure employment or establish a technology enterprise in Hungary.",
    startingSalaryLocal: "HUF 6,500,000 – 9,500,000 / Year (€18k–€26k)",
    startingSalaryPkr: "≈ PKR 5,400,000 – 7,800,000 / yr",
    salaryContext: "Expanding EU technology R&D centers, telecom, and automotive software hubs in Budapest, Debrecen, and Szeged.",
    prPathway: "EU Blue Card & Hungarian National Permanent Residence",
    prDetails: "Pathway to EU Blue Card with unrestricted mobility across the Schengen Zone after 3 years of qualifying employment.",
    visaFeePkr: 42000,
    settlementBufferPkr: 60000,
    defaultPortalName: "Tempus Public Foundation DreamApply Portal",
  },
  uk: {
    country: "United Kingdom",
    visaName: "Graduate Route Post-Study Work (PSW) Visa",
    visaDuration: "2 Years (3 Years for Doctoral / PhD graduates)",
    visaDetails: "Unsponsored, flexible work visa permitting employment in any industry or role without minimum salary caps.",
    startingSalaryLocal: "£28,000 – £42,000 / Year",
    startingSalaryPkr: "≈ PKR 9,800,000 – 14,700,000 / yr",
    salaryContext: "Fintech, AI research, and engineering in London, Manchester, Edinburgh, and the Cambridge tech cluster.",
    prPathway: "Skilled Worker Visa to Indefinite Leave to Remain (ILR)",
    prDetails: "Transition to employer-sponsored Skilled Worker Visa, qualifying for Indefinite Leave to Remain (PR) after 5 years.",
    visaFeePkr: 280000,
    settlementBufferPkr: 180000,
    defaultPortalName: "Chevening / Commonwealth / UK University Portals",
  },
  usa: {
    country: "United States",
    visaName: "F-1 Optional Practical Training (OPT) + 24-Mo STEM Extension",
    visaDuration: "Up to 36 Months (3 Years) for STEM graduates",
    visaDetails: "Full US work authorization in your field of study without immediate employer lottery sponsorship.",
    startingSalaryLocal: "$72,000 – $105,000 / Year",
    startingSalaryPkr: "≈ PKR 20,000,000 – 29,200,000 / yr",
    salaryContext: "Highest entry-level technology and engineering compensation globally (Silicon Valley, Austin, Seattle, Boston).",
    prPathway: "H-1B Specialty Occupation & EB-2 National Interest Waiver (NIW)",
    prDetails: "Employer-sponsored H-1B transition or direct EB-2 NIW Green Card petition based on academic research publications.",
    visaFeePkr: 125000,
    settlementBufferPkr: 200000,
    defaultPortalName: "Fulbright USEFP / Direct University Admissions",
  },
  canada: {
    country: "Canada",
    visaName: "Post-Graduation Work Permit (PGWP)",
    visaDuration: "Up to 3 Years (Open Work Permit)",
    visaDetails: "Open work permit allowing you to work for any employer anywhere in Canada without restriction.",
    startingSalaryLocal: "CAD $58,000 – $82,000 / Year",
    startingSalaryPkr: "≈ PKR 11,800,000 – 16,700,000 / yr",
    salaryContext: "Toronto, Vancouver, Montreal, and Waterloo technology ecosystems with strong Canadian innovation initiatives.",
    prPathway: "Express Entry Canadian Experience Class (CEC) & PNP",
    prDetails: "Direct Permanent Residency (PR) invitation via Express Entry after completing 1 year of Canadian skilled work.",
    visaFeePkr: 65000,
    settlementBufferPkr: 160000,
    defaultPortalName: "Vanier / Direct Canadian University Portals",
  },
  japan: {
    country: "Japan",
    visaName: "Designated Activities Visa (Job Hunting Period)",
    visaDuration: "6 Months to 1 Year (Extendable)",
    visaDetails: "Official post-graduate visa allowing foreign graduates to engage in career recruitment (Shūkatsu) across Japan.",
    startingSalaryLocal: "¥3,600,000 – ¥5,200,000 / Year",
    startingSalaryPkr: "≈ PKR 6,800,000 – 9,800,000 / yr",
    salaryContext: "Urgent engineering, robotics, and cloud developer demands in Tokyo, Osaka, and Fukuoka.",
    prPathway: "Highly Skilled Professional (HSP) Fast-Track PR",
    prDetails: "Accelerated Permanent Residency in as little as 1 to 3 years under Japan\'s points-based HSP immigration system.",
    visaFeePkr: 25000,
    settlementBufferPkr: 80000,
    defaultPortalName: "MEXT Embassy of Japan / University Portal",
  },
  southkorea: {
    country: "South Korea",
    visaName: "D-10-1 Job Seeking Visa",
    visaDuration: "Up to 2 Years (6-month renewals via points system)",
    visaDetails: "Allows Korean university graduates to reside legally in Korea while interviewing for E-7 professional roles.",
    startingSalaryLocal: "KRW 34,000,000 – 48,000,000 / Year",
    startingSalaryPkr: "≈ PKR 7,000,000 – 9,900,000 / yr",
    salaryContext: "Pangyo Techno Valley and Seoul IT / semiconductor ecosystem.",
    prPathway: "E-7 Skilled Worker to F-2-7 Resident Points Visa",
    prDetails: "Transition to F-2 points-based long-term residency, leading to F-5 permanent residency.",
    visaFeePkr: 32000,
    settlementBufferPkr: 75000,
    defaultPortalName: "Global Korea Scholarship (GKS) Study in Korea Portal",
  },
};

export const GLOBAL_CAREER_FALLBACK: CountryCareerProfile = {
  country: "International",
  visaName: "Post-Study Professional Residency & Work Permit",
  visaDuration: "12 to 24 Months",
  visaDetails: "Allows international graduates to reside in the host jurisdiction and pursue qualified employment in their specialization.",
  startingSalaryLocal: "Equivalent $35,000 – $55,000 / Year",
  startingSalaryPkr: "≈ PKR 9,500,000 – 15,000,000 / yr",
  salaryContext: "Competitive compensation in international commerce, software engineering, and scientific research.",
  prPathway: "National Skilled Migration & Long-Term Work Permit",
  prDetails: "Direct transition to multi-year skilled resident permits or EU/International Blue Card equivalents.",
  visaFeePkr: 45000,
  settlementBufferPkr: 80000,
  defaultPortalName: "Official Host Ministry / University Portal",
};

/**
 * Resolves the detailed career and immigration profile for a given country or scholarship name.
 */
export function getCountryCareerProfile(countryOrName?: string | null): CountryCareerProfile {
  if (!countryOrName) return GLOBAL_CAREER_FALLBACK;
  const lower = countryOrName.toLowerCase();

  if (lower.includes("australia") || lower.includes("aus") || lower.includes("sydney") || lower.includes("melbourne")) {
    return COUNTRY_CAREER_PROFILES.australia;
  }
  if (lower.includes("turk") || lower.includes("türkiye") || lower.includes("burslari")) {
    return COUNTRY_CAREER_PROFILES.turkey;
  }
  if (lower.includes("china") || lower.includes("chinese") || lower.includes("csc") || lower.includes("beijing") || lower.includes("shanghai")) {
    return COUNTRY_CAREER_PROFILES.china;
  }
  if (lower.includes("german") || lower.includes("daad") || lower.includes("deutschland")) {
    return COUNTRY_CAREER_PROFILES.germany;
  }
  if (lower.includes("hungar") || lower.includes("stipendium") || lower.includes("budapest")) {
    return COUNTRY_CAREER_PROFILES.hungary;
  }
  if (lower.includes("uk") || lower.includes("united kingdom") || lower.includes("brit") || lower.includes("chevening") || lower.includes("commonwealth") || lower.includes("england") || lower.includes("scotland")) {
    return COUNTRY_CAREER_PROFILES.uk;
  }
  if (lower.includes("usa") || lower.includes("united states") || lower.includes("america") || lower.includes("fulbright")) {
    return COUNTRY_CAREER_PROFILES.usa;
  }
  if (lower.includes("canada") || lower.includes("canadian") || lower.includes("vanier")) {
    return COUNTRY_CAREER_PROFILES.canada;
  }
  if (lower.includes("japan") || lower.includes("mext") || lower.includes("tokyo")) {
    return COUNTRY_CAREER_PROFILES.japan;
  }
  if (lower.includes("korea") || lower.includes("gks") || lower.includes("seoul")) {
    return COUNTRY_CAREER_PROFILES.southkorea;
  }

  return GLOBAL_CAREER_FALLBACK;
}

/**
 * Generates an end-to-end 5-step roadmap tailored specifically for this scholarship
 */
export function getScholarshipExecutionSteps(
  opp: {
    id?: string;
    name?: string;
    hostCountry?: string;
    hecPortalRequired?: boolean;
    officialPortalUrl?: string;
  },
  isUndergrad: boolean,
  candidateCity: string = "Multan",
  hasEnglishTest: boolean = false
): ApplicationStep[] {
  const countryProfile = getCountryCareerProfile(opp.hostCountry || opp.name);
  const portalUrl = opp.officialPortalUrl || "https://scholarship.hec.gov.pk";
  const isBilateral = Boolean(opp.hecPortalRequired || (opp.name && (opp.name.includes("Burslari") || opp.name.includes("CSC") || opp.name.includes("Stipendium") || opp.name.includes("Bilateral"))));

  return [
    {
      stepNumber: 1,
      title: isUndergrad ? "BISE / FBISE Verification & IBCC Equivalence Certificate" : "HEC Degree Attestation & IBCC Authentication",
      timeline: "Days 1 – 14",
      location: isUndergrad ? `BISE / FBISE (${candidateCity}) Board & IBCC Regional Office` : "HEC Online DAS Portal & TCS Courier Drop",
      costPkr: isUndergrad ? 10000 : 14000,
      description: isUndergrad
        ? `Submit Matric & Intermediate (FSc/ICS) Sanad and Result Cards to your respective BISE / FBISE board for verified sealed envelope, followed by IBCC Equivalence Certificate.`
        : `Submit 16-Year BS transcripts and degree scroll through HEC DAS online portal for electronic QR-attestation, followed by sealed verification stamps.`,
      isMilestone: true,
    },
    {
      stepNumber: 2,
      title: isBilateral 
        ? (isUndergrad ? "HEC USAT Aptitude Test & Bilateral Quota Registration" : "HEC HAT Aptitude Test & Bilateral Nomination Registration")
        : (hasEnglishTest ? "IELTS Academic Test & Faculty Recommendation Dossier" : "English Medium of Instruction (MOI) Certificate & Faculty Dossier"),
      timeline: "Days 15 – 30",
      location: isBilateral ? "HEC ETC Testing Portal (etc.hec.gov.pk)" : "College / University Department & British Council",
      costPkr: isBilateral ? 2500 : (hasEnglishTest ? 76000 : 0),
      description: isBilateral
        ? `Register for the national ${isUndergrad ? "HEC USAT" : "HEC HAT"} aptitude test required for official Pakistani government nomination. Score at least 50% to qualify.`
        : `Secure signed recommendation letters from two professors certifying your academic merits, research potential, and English language proficiency.`,
      actionUrl: isBilateral ? "https://etc.hec.gov.pk" : undefined,
    },
    {
      stepNumber: 3,
      title: `Submit Application on Official ${countryProfile.country} Portal`,
      timeline: "Days 31 – 45",
      location: `${opp.name} Online Submission System`,
      costPkr: 0,
      description: `Complete the complete scholarship application profile. Upload certified transcripts, passport copy, tailored Statement of Purpose (SOP), and select up to 3 host universities.`,
      actionUrl: portalUrl,
      isMilestone: true,
    },
    {
      stepNumber: 4,
      title: `Consulate Interview & Gerry\'s VFS Biometrics Submission`,
      timeline: "Post-Selection (Week 8 – 12)",
      location: `Gerry\'s Visa Drop Box & Embassy of ${countryProfile.country} (Islamabad)`,
      costPkr: countryProfile.visaFeePkr,
      description: `Upon receiving your official Award Letter and Embassy Visa Support Letter, schedule biometric appointments at Gerry\'s / VFS Global in Pakistan and submit full medical and police clearances.`,
      isMilestone: true,
    },
    {
      stepNumber: 5,
      title: `Pre-Departure Flight, Relocation & University Enrolment`,
      timeline: "Departure Phase",
      location: `Islamabad / Lahore Airport to Host University Campus`,
      costPkr: countryProfile.settlementBufferPkr,
      description: `Attend the pre-departure briefing at the Embassy or HEC Overseas Division. Book airfare (tuition and airfare fully covered by scholarship) and draw initial liquid buffer for dormitory check-in.`,
    },
  ];
}
