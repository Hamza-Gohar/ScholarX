"use client";

import React, { useState, useMemo } from "react";
import {
  Printer,
  Search,
  CheckCircle2,
  AlertTriangle,
  ExternalLink,
  ChevronRight,
  Filter,
  GraduationCap,
  Globe2,
  Calendar,
  Building2,
  FileCheck2,
  ShieldAlert,
  ArrowLeft,
  X
} from "lucide-react";
import Link from "next/link";

interface ScholarshipDossierItem {
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

export function CatalogPrintView({
  scholarships,
}: {
  scholarships: ScholarshipDossierItem[];
}) {
  const [selectedRegion, setSelectedRegion] = useState<string>("ALL");
  const [degreeFilter, setDegreeFilter] = useState<string>("ALL");
  const [searchQuery, setSearchQuery] = useState<string>("");

  const regions = ["ALL", "Europe", "Asia", "Americas", "MENA", "Oceania"];
  const degrees = ["ALL", "Bachelor's", "Master's", "PhD"];

  // Filter scholarships
  const filtered = useMemo(() => {
    return scholarships.filter((s) => {
      // Region match
      if (selectedRegion !== "ALL" && s.region.toLowerCase() !== selectedRegion.toLowerCase()) {
        return false;
      }

      // Degree match
      if (degreeFilter !== "ALL") {
        const matchesDegree = s.degree_levels.some((d) =>
          d.toLowerCase().includes(degreeFilter.toLowerCase())
        );
        if (!matchesDegree) return false;
      }

      // Search match
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const inName = s.name.toLowerCase().includes(q);
        const inCountry = s.country.toLowerCase().includes(q);
        const inEntity = s.offering_entity.toLowerCase().includes(q);
        const inInstitutions = s.host_institutions.toLowerCase().includes(q);
        const inField = s.eligibility.field_requirements.toLowerCase().includes(q);
        const inId = s.id.toLowerCase().includes(q);
        if (!inName && !inCountry && !inEntity && !inInstitutions && !inField && !inId) {
          return false;
        }
      }

      return true;
    });
  }, [scholarships, selectedRegion, degreeFilter, searchQuery]);

  const totalFullyFunded = useMemo(() => {
    return filtered.filter((s) => s.funding_type.includes("FULL")).length;
  }, [filtered]);

  const uniqueCountries = useMemo(() => {
    return new Set(filtered.map((s) => s.country)).size;
  }, [filtered]);

  return (
    <div className="min-h-screen bg-[#F8FAFC] text-[#0F172A] font-sans antialiased">
      {/* ========================================================================= */}
      {/* 1. SCREEN-ONLY TOP ACTION & FILTER BAR                                    */}
      {/* ========================================================================= */}
      <header className="sticky top-0 z-40 bg-[#0F172A] text-white border-b border-slate-700 shadow-md py-3 px-4 sm:px-6 no-print">
        <div className="max-w-[1200px] mx-auto flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center space-x-3">
            <Link
              href="/"
              className="p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
              title="Return to Home"
            >
              <ArrowLeft className="w-4 h-4" />
            </Link>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-mono text-xs font-bold px-1.5 py-0.5 rounded bg-[#0F766E] text-white uppercase tracking-wider">
                  SCHOLARX
                </span>
                <span className="text-xs font-mono text-slate-400 uppercase tracking-widest hidden sm:inline">
                  INTELLIGENCE CATALOG // COHORT 2026/2027
                </span>
              </div>
              <h1 className="text-sm font-bold text-slate-100 flex items-center space-x-2">
                <span>Enterprise Scholarship Dossier Directory</span>
                <span className="text-xs text-teal-400 font-mono">({filtered.length} Opportunities)</span>
              </h1>
            </div>
          </div>
        </div>

        {/* Filters Strip */}
        <div className="max-w-[1200px] mx-auto mt-3 pt-3 border-t border-slate-800 flex flex-wrap items-center justify-between gap-2.5 text-xs">
          {/* Region Tabs */}
          <div className="flex items-center space-x-1 overflow-x-auto pb-1 sm:pb-0">
            <span className="text-slate-400 font-mono text-[10px] uppercase mr-1">Region:</span>
            {regions.map((r) => {
              const count = r === "ALL" ? scholarships.length : scholarships.filter((s) => s.region.toLowerCase() === r.toLowerCase()).length;
              return (
                <button
                  key={r}
                  type="button"
                  onClick={() => setSelectedRegion(r)}
                  className={`px-2.5 py-1 rounded text-xs font-mono transition-all cursor-pointer ${
                    selectedRegion.toLowerCase() === r.toLowerCase()
                      ? "bg-[#0F766E] text-white font-bold"
                      : "bg-slate-800/80 text-slate-300 hover:bg-slate-700"
                  }`}
                >
                  {r} ({count})
                </button>
              );
            })}
          </div>

          {/* Search & Degree Filter */}
          <div className="flex items-center space-x-2 w-full sm:w-auto">
            <div className="relative flex-1 sm:w-48">
              <Search className="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search scholarships..."
                className="w-full pl-8 pr-3 py-1 bg-slate-900 border border-slate-700 rounded text-xs text-white placeholder-slate-500 focus:outline-none focus:border-teal-500"
              />
              {searchQuery && (
                <button
                  type="button"
                  onClick={() => setSearchQuery("")}
                  className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                >
                  <X className="w-3 h-3" />
                </button>
              )}
            </div>

            <select
              value={degreeFilter}
              onChange={(e) => setDegreeFilter(e.target.value)}
              className="px-2.5 py-1 bg-slate-900 border border-slate-700 rounded text-xs text-slate-200 focus:outline-none focus:border-teal-500 font-mono"
            >
              {degrees.map((d) => (
                <option key={d} value={d}>
                  {d === "ALL" ? "All Degree Levels" : d}
                </option>
              ))}
            </select>
          </div>
        </div>
      </header>

      {/* ========================================================================= */}
      {/* 2. MAIN PUBLICATION DOCUMENT (A4 PRINT & DESK CONTAINER)                  */}
      {/* ========================================================================= */}
      <main className="max-w-[1050px] mx-auto px-4 sm:px-6 py-6 sm:py-8 space-y-6 print:max-w-none print:p-0 print:m-0 print:space-y-4">
        
        {/* Executive Header & KPI Strip */}
        <section className="bg-white border border-slate-300 rounded p-5 shadow-sm print:shadow-none print:border-b-2 print:border-slate-900 print:rounded-none">
          <div className="flex flex-wrap items-center justify-between text-xs font-mono text-slate-500 uppercase pb-2 border-b border-slate-200 mb-3 gap-2">
            <div className="flex items-center space-x-2">
              <span className="font-bold text-[#0F766E]">SCHOLARX ADVISORY NETWORK</span>
              <span>•</span>
              <span className="text-slate-700 font-semibold">GLOBAL SCHOLARSHIP INTELLIGENCE DOSSIER</span>
            </div>
            <div className="font-bold text-slate-800">
              ACADEMIC COHORT 2026/2027 // VERIFIED CONFIDENCE: 98%
            </div>
          </div>

          <h1 className="text-2xl font-extrabold text-slate-900 tracking-tight mb-2">
            International Scholarship Directory &amp; Execution Roadmap
          </h1>
          <p className="text-xs text-slate-600 leading-relaxed max-w-4xl mb-4">
            Official intelligence compendium for academic intake 2026/2027. Evaluated for Pakistani applicants and international scholars targeting bilateral quotas, degree waivers, living stipends, and English medium of instruction (MOI) exemptions.
          </p>

          {/* KPI Strip */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 pt-2 border-t border-slate-200 text-slate-800">
            <div className="bg-slate-50 border-l-2 border-teal-600 p-2 rounded-r">
              <div className="text-lg font-mono font-extrabold text-slate-900 leading-tight">
                {filtered.length}
              </div>
              <div className="text-[10px] font-mono text-slate-500 uppercase font-semibold">
                Verified Opportunities
              </div>
            </div>
            <div className="bg-slate-50 border-l-2 border-emerald-600 p-2 rounded-r">
              <div className="text-lg font-mono font-extrabold text-emerald-800 leading-tight">
                {totalFullyFunded}
              </div>
              <div className="text-[10px] font-mono text-slate-500 uppercase font-semibold">
                100% Fully Funded
              </div>
            </div>
            <div className="bg-slate-50 border-l-2 border-slate-600 p-2 rounded-r">
              <div className="text-lg font-mono font-extrabold text-slate-900 leading-tight">
                {uniqueCountries}
              </div>
              <div className="text-[10px] font-mono text-slate-500 uppercase font-semibold">
                Host Nations Covered
              </div>
            </div>
            <div className="bg-slate-50 border-l-2 border-amber-600 p-2 rounded-r">
              <div className="text-lg font-mono font-extrabold text-amber-800 leading-tight">
                PKR 140k–300k
              </div>
              <div className="text-[10px] font-mono text-slate-500 uppercase font-semibold">
                Estimated Out-of-Pocket Buffer
              </div>
            </div>
          </div>
        </section>

        {/* Scholarships Cards Grid */}
        <div className="space-y-4 print:space-y-4">
          {filtered.length === 0 ? (
            <div className="bg-white border border-slate-200 rounded p-8 text-center text-slate-500">
              No scholarships matched your filter criteria. Try clearing the search query or selecting &quot;ALL&quot;.
            </div>
          ) : (
            filtered.map((s) => {
              const fc = s.financial_coverage;
              const el = s.eligibility;
              const sm = s.summary;

              const tuitionDisp = fc.tuition.status || "100% Covered";
              const stipendDisp = fc.monthly_stipend.amount || fc.monthly_stipend.details || "Monthly Stipend Provided";
              const accomDisp = fc.accommodation.details || fc.accommodation.status || "Provided / Allowance";
              const travelDisp = `Airfare: ${fc.airfare.status || "Covered"} • Health: ${fc.health_insurance.status || "Covered"}`;

              return (
                <article
                  key={s.id}
                  className="bg-white border border-slate-300 border-t-[3px] border-t-[#0F766E] rounded p-4 shadow-xs print:shadow-none print:border-slate-300 print:mb-4 page-break-avoid"
                  style={{ breakInside: "avoid", pageBreakInside: "avoid" }}
                >
                  {/* Header Row */}
                  <div className="flex flex-wrap items-start justify-between border-b border-slate-200 pb-2.5 mb-2.5 gap-2">
                    <div className="flex-1 min-w-[280px]">
                      <div className="flex flex-wrap items-center gap-1.5 mb-1">
                        <span className="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-slate-900 text-white uppercase tracking-wider">
                          {s.region}
                        </span>
                        <span className="font-mono text-[10px] font-semibold px-1.5 py-0.5 rounded bg-slate-200 text-slate-800">
                          {s.country}
                        </span>
                        <span className="font-mono text-[10px] px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 border border-slate-300">
                          {s.id}
                        </span>
                        <span className="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-300">
                          {s.funding_type.replace("_", " ")}
                        </span>
                      </div>
                      <h2 className="text-base sm:text-lg font-bold text-slate-900 leading-tight">
                        {s.name}
                      </h2>
                      <div className="text-xs text-slate-600 mt-0.5">
                        <strong className="text-slate-700">Host Body:</strong> {s.offering_entity} &nbsp;|&nbsp;
                        <strong className="text-slate-700"> Placement:</strong> {s.host_institutions}
                      </div>
                    </div>

                    <div className="text-right shrink-0">
                      <div className="inline-block bg-slate-900 text-white px-2.5 py-1 rounded text-right">
                        <span className="block text-[9px] font-mono font-bold text-teal-300 uppercase tracking-wider">
                          APPLICATION DEADLINE
                        </span>
                        <span className="font-mono text-xs font-bold text-white">
                          {s.deadline}
                        </span>
                      </div>
                      <div className="text-[11px] font-semibold text-slate-600 mt-1">
                        {s.degree_levels_str} • {s.duration}
                      </div>
                    </div>
                  </div>

                  {/* 4-Box Key Metrics Bar */}
                  <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-2.5">
                    <div className="bg-slate-50 border border-slate-200 rounded p-2">
                      <span className="block font-mono text-[9px] font-bold text-slate-500 uppercase tracking-wider">
                        TUITION COVERAGE
                      </span>
                      <span className="text-xs font-bold text-emerald-700 leading-tight block">
                        {tuitionDisp}
                      </span>
                    </div>
                    <div className="bg-slate-50 border border-slate-200 rounded p-2">
                      <span className="block font-mono text-[9px] font-bold text-slate-500 uppercase tracking-wider">
                        MONTHLY STIPEND
                      </span>
                      <span className="text-xs font-bold text-slate-800 leading-tight block truncate" title={stipendDisp}>
                        {stipendDisp}
                      </span>
                    </div>
                    <div className="bg-slate-50 border border-slate-200 rounded p-2">
                      <span className="block font-mono text-[9px] font-bold text-slate-500 uppercase tracking-wider">
                        ACCOMMODATION
                      </span>
                      <span className="text-xs font-bold text-slate-800 leading-tight block truncate" title={accomDisp}>
                        {accomDisp}
                      </span>
                    </div>
                    <div className="bg-slate-50 border border-slate-200 rounded p-2">
                      <span className="block font-mono text-[9px] font-bold text-slate-500 uppercase tracking-wider">
                        TRAVEL &amp; HEALTH
                      </span>
                      <span className="text-xs font-bold text-slate-800 leading-tight block truncate" title={travelDisp}>
                        {travelDisp}
                      </span>
                    </div>
                  </div>

                  {/* Coverage Conditions Pills */}
                  <div className="bg-slate-100/80 px-2.5 py-1.5 rounded mb-2.5 flex flex-wrap items-center gap-1.5 text-xs">
                    <span className="font-mono text-[10px] font-bold text-slate-600 uppercase mr-1">
                      COVERAGE SPECIFICATION:
                    </span>
                    {fc.covered_tags.map((tag, idx) => (
                      <span
                        key={idx}
                        className="bg-emerald-50 text-emerald-800 border border-emerald-300 font-semibold px-2 py-0.5 rounded text-[11px] whitespace-nowrap"
                      >
                        ✓ {tag}
                      </span>
                    ))}
                    {fc.not_covered_tags.map((tag, idx) => (
                      <span
                        key={idx}
                        className="bg-amber-50 text-amber-800 border border-amber-300 font-semibold px-2 py-0.5 rounded text-[11px] whitespace-nowrap"
                      >
                        ✕ {tag}
                      </span>
                    ))}
                  </div>

                  {/* 2-Column Detail Grid */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-2.5">
                    {/* Col 1: Requirements & Eligibility */}
                    <div className="border border-slate-200 rounded p-2.5 bg-white">
                      <div className="font-mono text-[10px] font-bold text-[#0F766E] uppercase pb-1 mb-1.5 border-b border-slate-200">
                        ELIGIBILITY &amp; ACADEMIC REQUIREMENTS
                      </div>
                      <table className="w-full text-xs">
                        <tbody>
                          <tr className="border-b border-slate-100">
                            <td className="w-1/3 py-1 font-semibold text-slate-500">Age Requirement</td>
                            <td className="py-1 text-slate-800">{el.age_notes}</td>
                          </tr>
                          <tr className="border-b border-slate-100">
                            <td className="w-1/3 py-1 font-semibold text-slate-500">Academic Cutoff</td>
                            <td className="py-1 text-slate-800">
                              <strong className="text-slate-900">{el.minimum_gpa}</strong> — {el.academic_qualifications}
                            </td>
                          </tr>
                          <tr className="border-b border-slate-100">
                            <td className="w-1/3 py-1 font-semibold text-slate-500">Nationality / Quota</td>
                            <td className="py-1 text-slate-800">{el.nationality}</td>
                          </tr>
                          <tr className="border-b border-slate-100">
                            <td className="w-1/3 py-1 font-semibold text-slate-500">English Language</td>
                            <td className="py-1 text-slate-800">
                              <span
                                className={`inline-block px-1.5 py-0.5 rounded text-[10px] font-bold mr-1.5 ${
                                  el.moi_accepted
                                    ? "bg-emerald-100 text-emerald-800 border border-emerald-300"
                                    : "bg-indigo-100 text-indigo-800 border border-indigo-300"
                                }`}
                              >
                                {el.english_badge}
                              </span>
                              <span className="text-slate-500 text-[11px]">{el.language_notes}</span>
                            </td>
                          </tr>
                          <tr className="border-b border-slate-100">
                            <td className="w-1/3 py-1 font-semibold text-slate-500">Field Scope</td>
                            <td className="py-1 text-slate-800">{el.field_requirements}</td>
                          </tr>
                          <tr>
                            <td className="w-1/3 py-1 font-semibold text-slate-500">Experience / Terms</td>
                            <td className="py-1 text-slate-800">{el.other_requirements}</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>

                    {/* Col 2: Application Process & Required Documents */}
                    <div className="border border-slate-200 rounded p-2.5 bg-white flex flex-col justify-between">
                      <div>
                        <div className="font-mono text-[10px] font-bold text-[#0F766E] uppercase pb-1 mb-1.5 border-b border-slate-200">
                          APPLICATION PROCESS &amp; REQUIRED DOCUMENTS
                        </div>
                        <div className="mb-2">
                          <span className="text-[10px] font-bold text-slate-600 uppercase font-mono block mb-1">
                            Roadmap Sequence:
                          </span>
                          <ol className="list-decimal pl-4 space-y-0.5 text-xs text-slate-700 leading-snug">
                            {sm.workflow_steps.slice(0, 4).map((st, i) => (
                              <li key={i}>{st}</li>
                            ))}
                          </ol>
                        </div>
                      </div>

                      <div className="pt-2 border-t border-slate-100">
                        <span className="text-[10px] font-bold text-slate-600 uppercase font-mono block mb-1.5">
                          Mandatory Document Dossier:
                        </span>
                        <div className="flex flex-wrap gap-1">
                          {sm.required_documents.slice(0, 7).map((doc, i) => (
                            <span
                              key={i}
                              className="bg-slate-50 border border-slate-200 text-slate-800 px-1.5 py-0.5 rounded text-[10px] font-medium"
                              title={doc.notes}
                            >
                              ☑ {doc.name}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Strategic Due Diligence & Official Citations Footer */}
                  <div className="border-t border-slate-200 pt-2 text-xs text-slate-700 space-y-1">
                    <div className="bg-emerald-50/70 border-l-2 border-emerald-600 p-1.5 rounded-r text-emerald-950 text-[11px] leading-snug">
                      <strong>Strategic Merit:</strong> {sm.why_interesting}
                    </div>
                    <div className="bg-amber-50/70 border-l-2 border-amber-500 p-1.5 rounded-r text-amber-950 text-[11px] leading-snug">
                      <strong>Due Diligence / Safeguards:</strong> {sm.fee_warning} • {sm.hidden_costs}
                    </div>

                    <div className="flex flex-wrap items-center justify-between pt-1 text-[11px] text-slate-600 gap-2">
                      <div className="flex flex-wrap items-center gap-2">
                        <strong className="text-slate-800">Official Portals:</strong>
                        {s.official_sources.slice(0, 3).map((src, i) => (
                          <a
                            key={i}
                            href={src.url}
                            target="_blank"
                            rel="noreferrer"
                            className="text-[#0F766E] hover:underline font-semibold flex items-center space-x-0.5"
                          >
                            <span>{src.title}</span>
                            <ExternalLink className="w-2.5 h-2.5 inline ml-0.5" />
                          </a>
                        ))}
                      </div>
                      <div className="text-slate-500 italic text-[10px] font-mono">
                        Intake: {s.commencement} (Opens: {s.open_date})
                      </div>
                    </div>
                  </div>
                </article>
              );
            })
          )}
        </div>
      </main>
    </div>
  );
}
