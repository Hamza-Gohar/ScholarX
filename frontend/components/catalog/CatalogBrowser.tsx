"use client";

import React, { useState, useMemo } from "react";
import Link from "next/link";
import { ScholarshipCatalogItem } from "@/lib/dossier/catalogNormalizer";
import { 
  Search, 
  Filter, 
  Globe2, 
  GraduationCap, 
  Coins, 
  ArrowRight, 
  Calendar, 
  FileDown, 
  Printer, 
  Languages, 
  CheckCircle2, 
  Sparkles,
  ExternalLink
} from "lucide-react";
import { CountryFlagLogo } from "@/components/common/CountryFlagLogo";

interface CatalogBrowserProps {
  initialScholarships: ScholarshipCatalogItem[];
}

export function CatalogBrowser({ initialScholarships }: CatalogBrowserProps) {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedRegion, setSelectedRegion] = useState<string>("ALL");
  const [selectedDegree, setSelectedDegree] = useState<string>("ALL");
  const [onlyFullyFunded, setOnlyFullyFunded] = useState<boolean>(false);
  const [onlyMoiAccepted, setOnlyMoiAccepted] = useState<boolean>(false);

  const regions = [
    { id: "ALL", label: "All Continents", count: initialScholarships.length },
    { id: "Europe", label: "Europe", count: initialScholarships.filter((s) => s.region === "Europe").length },
    { id: "Asia", label: "Asia", count: initialScholarships.filter((s) => s.region === "Asia").length },
    { id: "Americas", label: "Americas", count: initialScholarships.filter((s) => s.region === "Americas").length },
    { id: "MENA", label: "Middle East", count: initialScholarships.filter((s) => s.region === "MENA").length },
    { id: "Oceania", label: "Oceania", count: initialScholarships.filter((s) => s.region === "Oceania").length },
  ];

  const filteredScholarships = useMemo(() => {
    return initialScholarships.filter((item) => {
      // Query filter
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const matchName = item.name.toLowerCase().includes(q);
        const matchCountry = item.country.toLowerCase().includes(q);
        const matchEntity = item.offering_entity.toLowerCase().includes(q);
        const matchDegree = item.degree_levels_str.toLowerCase().includes(q);
        if (!matchName && !matchCountry && !matchEntity && !matchDegree) {
          return false;
        }
      }

      // Region filter
      if (selectedRegion !== "ALL" && item.region !== selectedRegion) {
        return false;
      }

      // Degree filter
      if (selectedDegree !== "ALL") {
        const matchDeg = item.degree_levels.some((d) =>
          d.toLowerCase().includes(selectedDegree.toLowerCase())
        );
        if (!matchDeg) return false;
      }

      // Fully funded filter
      if (onlyFullyFunded) {
        const isFull =
          item.funding_type.toUpperCase().includes("FULL") ||
          item.financial_coverage.tuition.is_covered;
        if (!isFull) return false;
      }

      // MOI accepted filter
      if (onlyMoiAccepted) {
        if (!item.eligibility.moi_accepted) return false;
      }

      return true;
    });
  }, [initialScholarships, searchQuery, selectedRegion, selectedDegree, onlyFullyFunded, onlyMoiAccepted]);

  return (
    <div className="w-full max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 py-6 sm:py-12">
      {/* Top Breadcrumb & Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 sm:gap-4 pb-6 sm:pb-8 border-b border-white/10">
        <nav aria-label="Breadcrumb" className="flex items-center gap-2 text-xs sm:text-sm text-neutral-400">
          <Link href="/" className="hover:text-cyan-400 transition-colors">
            ScholarX Home
          </Link>
          <span>/</span>
          <span className="text-white font-medium">Scholarship Directory</span>
        </nav>

        <div className="flex items-center gap-2 sm:gap-3 flex-wrap">
          <Link
            href="/downloads/ScholarX_Global_Master_Scholarship_Dossier_2026_2027.pdf"
            className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-neutral-900 border border-neutral-700 hover:border-cyan-500/50 text-xs sm:text-sm font-medium text-neutral-200 hover:text-white transition-all shadow-sm"
            target="_blank"
          >
            <FileDown className="w-4 h-4 text-cyan-400" />
            <span>Master PDF Dossier</span>
          </Link>

          <Link
            href="/catalog/print"
            className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-neutral-900 border border-neutral-700 hover:border-cyan-500/50 text-xs sm:text-sm font-medium text-neutral-200 hover:text-white transition-all shadow-sm"
            target="_blank"
          >
            <Printer className="w-4 h-4 text-cyan-400" />
            <span>Print Matrix</span>
          </Link>
        </div>
      </div>

      {/* Header Section */}
      <div className="py-8 sm:py-12">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/60 border border-cyan-500/30 text-cyan-400 text-xs font-semibold uppercase tracking-wider mb-4">
          <Sparkles className="w-3.5 h-3.5" />
          <span>Verified Pakistan & Global Quota Intelligence</span>
        </div>
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight leading-tight">
          International Scholarship Directory
        </h1>
        <p className="mt-4 text-base sm:text-lg text-neutral-400 max-w-3xl leading-relaxed">
          Explore 310 deeply investigated, bilateral and government scholarships. Every program includes complete financial coverage breakdowns, HEC attestation prerequisites, IELTS/MOI waivers, and official application portals.
        </p>
      </div>

      {/* Search & Filter Bar */}
      <div className="bg-neutral-900/80 border border-neutral-800 rounded-2xl p-4 sm:p-6 mb-8 backdrop-blur-md shadow-xl">
        <div className="flex flex-col md:flex-row gap-4">
          {/* Keyword Search */}
          <div className="relative flex-1">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-5 h-5 text-neutral-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search by scholarship name, country (e.g. Hungary, Turkey, Germany), or university..."
              className="w-full pl-11 pr-4 py-3 bg-neutral-950 border border-neutral-800 rounded-xl text-white placeholder-neutral-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500 text-sm transition-all"
            />
          </div>

          {/* Degree Filter Dropdown */}
          <div className="flex items-center gap-2 min-w-[200px]">
            <GraduationCap className="w-5 h-5 text-neutral-400 shrink-0" />
            <select
              value={selectedDegree}
              onChange={(e) => setSelectedDegree(e.target.value)}
              className="w-full py-3 px-3.5 bg-neutral-950 border border-neutral-800 rounded-xl text-white text-sm focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500 transition-all cursor-pointer"
            >
              <option value="ALL">All Degree Levels</option>
              <option value="Bachelor">Bachelor&apos;s</option>
              <option value="Master">Master&apos;s</option>
              <option value="PhD">PhD / Doctoral</option>
            </select>
          </div>
        </div>

        {/* Region Pills & Toggle Badges */}
        <div className="mt-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-4 border-t border-neutral-800/80">
          <div className="flex items-center gap-2 overflow-x-auto no-scrollbar py-1 w-full sm:w-auto">
            {regions.map((reg) => (
              <button
                key={reg.id}
                onClick={() => setSelectedRegion(reg.id)}
                className={`px-3 sm:px-3.5 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                  selectedRegion === reg.id
                    ? "bg-cyan-500 text-neutral-950 font-bold shadow-md shadow-cyan-500/20"
                    : "bg-neutral-950 text-neutral-400 hover:text-white hover:bg-neutral-800 border border-neutral-800"
                }`}
              >
                {reg.label} ({reg.count})
              </button>
            ))}
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <label className="inline-flex items-center gap-2 text-xs text-neutral-300 cursor-pointer select-none">
              <input
                type="checkbox"
                checked={onlyFullyFunded}
                onChange={(e) => setOnlyFullyFunded(e.target.checked)}
                className="w-4 h-4 rounded border-neutral-700 bg-neutral-950 text-cyan-500 focus:ring-cyan-500/30"
              />
              <span>100% Fully Funded</span>
            </label>

            <label className="inline-flex items-center gap-2 text-xs text-neutral-300 cursor-pointer select-none">
              <input
                type="checkbox"
                checked={onlyMoiAccepted}
                onChange={(e) => setOnlyMoiAccepted(e.target.checked)}
                className="w-4 h-4 rounded border-neutral-700 bg-neutral-950 text-cyan-500 focus:ring-cyan-500/30"
              />
              <span>MOI Accepted (No IELTS)</span>
            </label>
          </div>
        </div>
      </div>

      {/* Results Count Summary */}
      <div className="flex items-center justify-between mb-4 sm:mb-6 text-xs sm:text-sm text-neutral-400">
        <span>
          Showing <strong className="text-white font-semibold">{filteredScholarships.length}</strong> of{" "}
          {initialScholarships.length} verified programs
        </span>
        {searchQuery && (
          <button
            onClick={() => setSearchQuery("")}
            className="text-cyan-400 hover:text-cyan-300 underline font-medium"
          >
            Clear Search
          </button>
        )}
      </div>

      {/* Grid of Scholarship Dossier Cards */}
      {filteredScholarships.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
          {filteredScholarships.map((item) => {
            const hasMoi = item.eligibility.moi_accepted;
            const isFull =
              item.funding_type.toUpperCase().includes("FULL") ||
              item.financial_coverage.tuition.is_covered;

            return (
              <article
                key={item.id}
                className="group flex flex-col justify-between bg-neutral-900/60 hover:bg-neutral-900 border border-neutral-800 hover:border-cyan-500/40 rounded-xl sm:rounded-2xl p-4 sm:p-6 transition-all duration-200 shadow-md hover:shadow-cyan-950/20"
              >
                <div>
                  {/* Top Badges */}
                  <div className="flex items-center justify-between gap-2 mb-4">
                    <div className="inline-flex items-center gap-2 text-xs font-semibold text-neutral-300 bg-neutral-950 px-2.5 py-1 rounded-md border border-neutral-800">
                      <CountryFlagLogo country={item.country} className="w-4 h-4 rounded-sm" />
                      <span>{item.country}</span>
                    </div>

                    <span className="text-[11px] font-mono text-cyan-400 bg-cyan-950/60 border border-cyan-800/40 px-2 py-0.5 rounded">
                      {item.id}
                    </span>
                  </div>

                  {/* Title with Crawlable Link */}
                  <h2 className="text-lg font-bold text-white group-hover:text-cyan-300 transition-colors line-clamp-2 leading-snug">
                    <Link href={`/dossier/${encodeURIComponent(item.id)}`} className="focus:outline-none">
                      {item.name}
                    </Link>
                  </h2>

                  <p className="mt-2 text-xs text-neutral-400 line-clamp-2">
                    {item.offering_entity} • {item.host_institutions}
                  </p>

                  {/* Feature Tags */}
                  <div className="mt-4 flex flex-wrap gap-1.5">
                    {isFull && (
                      <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-emerald-950/50 text-emerald-400 border border-emerald-800/40 px-2 py-0.5 rounded">
                        <CheckCircle2 className="w-3 h-3" />
                        <span>Fully Funded</span>
                      </span>
                    )}

                    {hasMoi && (
                      <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-indigo-950/50 text-indigo-300 border border-indigo-800/40 px-2 py-0.5 rounded">
                        <Languages className="w-3 h-3" />
                        <span>MOI Accepted</span>
                      </span>
                    )}

                    <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-neutral-950 text-neutral-300 border border-neutral-800 px-2 py-0.5 rounded">
                      <GraduationCap className="w-3 h-3 text-neutral-400" />
                      <span>{item.degree_levels_str}</span>
                    </span>
                  </div>

                  {/* Deadline Info */}
                  <div className="mt-4 pt-3 border-t border-neutral-800/60 flex items-center justify-between text-xs text-neutral-400">
                    <span className="flex items-center gap-1.5">
                      <Calendar className="w-3.5 h-3.5 text-neutral-500" />
                      <span>Deadline:</span>
                    </span>
                    <span className="text-white font-medium">{item.deadline}</span>
                  </div>
                </div>

                {/* Footer Action */}
                <div className="mt-5 pt-3 border-t border-neutral-800/60 flex items-center justify-between">
                  <Link
                    href={`/dossier/${encodeURIComponent(item.id)}`}
                    className="inline-flex items-center gap-1.5 text-xs font-semibold text-cyan-400 group-hover:text-cyan-300 transition-colors"
                  >
                    <span>View Dossier</span>
                    <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                  </Link>

                  {item.official_sources[0]?.url && (
                    <a
                      href={item.official_sources[0].url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-neutral-500 hover:text-neutral-300 text-xs inline-flex items-center gap-1 transition-colors"
                      title="Official Government / University Portal"
                    >
                      <span>Official</span>
                      <ExternalLink className="w-3 h-3" />
                    </a>
                  )}
                </div>
              </article>
            );
          })}
        </div>
      ) : (
        <div className="text-center py-16 bg-neutral-900/40 border border-neutral-800 rounded-2xl p-8">
          <p className="text-lg text-neutral-300 font-semibold">No scholarships match your filters.</p>
          <p className="text-sm text-neutral-500 mt-2">Try clearing your search query or selecting another region.</p>
          <button
            onClick={() => {
              setSearchQuery("");
              setSelectedRegion("ALL");
              setSelectedDegree("ALL");
              setOnlyFullyFunded(false);
              setOnlyMoiAccepted(false);
            }}
            className="mt-6 px-4 py-2 rounded-xl bg-cyan-500 text-neutral-950 font-bold text-xs hover:bg-cyan-400 transition-colors"
          >
            Reset All Filters
          </button>
        </div>
      )}
    </div>
  );
}
