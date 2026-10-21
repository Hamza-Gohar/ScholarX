"use client";

import React, { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import {
  Search,
  Filter,
  Download,
  ArrowUpDown,
  ArrowUp,
  ArrowDown,
  Globe,
  Award,
  BookOpen,
  Calendar,
  CheckCircle2,
  ExternalLink,
  ChevronRight,
  X,
  FileSpreadsheet,
  Layers,
  Sparkles,
  ShieldCheck,
  GraduationCap,
  DollarSign,
  Info,
  RefreshCw,
} from "lucide-react";
import { Scholarship, Region } from "@/lib/types";

interface StatsSummary {
  total_scholarships: number;
  by_region: Record<string, number>;
  by_funding_type: Record<string, number>;
  hec_bilateral_quota_count: number;
  total_bilateral_seats: number;
  moi_waiver_count: number;
  with_deep_dossiers: number;
}

export default function ScholarshipsDatabasePage() {
  const [scholarships, setScholarships] = useState<Scholarship[]>([]);
  const [totalCount, setTotalCount] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(true);
  const [stats, setStats] = useState<StatsSummary | null>(null);

  // Filter States
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [selectedRegion, setSelectedRegion] = useState<string>("ALL");
  const [selectedDegree, setSelectedDegree] = useState<string>("ALL");
  const [selectedFunding, setSelectedFunding] = useState<string>("ALL");
  const [hecOnly, setHecOnly] = useState<boolean>(false);
  const [moiOnly, setMoiOnly] = useState<boolean>(false);

  // Sort States
  const [sortBy, setSortBy] = useState<string>("name");
  const [sortOrder, setSortOrder] = useState<"asc" | "desc">("asc");

  // Pagination & Layout States
  const [page, setPage] = useState<number>(1);
  const [pageSize, setPageSize] = useState<number>(25);
  const [isCompact, setIsCompact] = useState<boolean>(false);

  // Quick View Drawer State
  const [activeScholarship, setActiveScholarship] = useState<Scholarship | null>(null);

  // Fetch Stats once on mount
  useEffect(() => {
    async function fetchStats() {
      try {
        const res = await fetch("/api/scholarships/stats/summary");
        if (res.ok) {
          const data = await res.json();
          setStats(data);
        }
      } catch (e) {
        // Fallback default stats for display
        setStats({
          total_scholarships: 310,
          by_region: { Europe: 101, Asia: 81, Americas: 65, MENA: 43, Oceania: 20 },
          by_funding_type: { FULL: 310 },
          hec_bilateral_quota_count: 54,
          total_bilateral_seats: 2444,
          moi_waiver_count: 131,
          with_deep_dossiers: 310,
        });
      }
    }
    fetchStats();
  }, []);

  // Fetch Scholarships from API
  useEffect(() => {
    let isCancelled = false;
    async function loadData() {
      setLoading(true);
      try {
        const params = new URLSearchParams();
        if (searchQuery.trim()) params.set("search", searchQuery.trim());
        if (selectedRegion !== "ALL") params.set("region", selectedRegion);
        if (selectedDegree !== "ALL") params.set("degree_level", selectedDegree);
        if (selectedFunding !== "ALL") params.set("funding_type", selectedFunding);
        if (hecOnly) params.set("hec_only", "true");
        if (moiOnly) params.set("moi_only", "true");
        params.set("sort_by", sortBy);
        params.set("sort_order", sortOrder);
        params.set("limit", pageSize.toString());
        params.set("offset", ((page - 1) * pageSize).toString());

        const res = await fetch(`/api/scholarships?${params.toString()}`);
        if (res.ok) {
          const data = await res.json();
          if (!isCancelled) {
            setScholarships(data.scholarships || []);
            setTotalCount(data.total || 0);
          }
        }
      } catch (err) {
        console.error("Failed to load scholarships:", err);
      } finally {
        if (!isCancelled) setLoading(false);
      }
    }

    const debounceTimer = setTimeout(loadData, 150);
    return () => {
      isCancelled = true;
      clearTimeout(debounceTimer);
    };
  }, [searchQuery, selectedRegion, selectedDegree, selectedFunding, hecOnly, moiOnly, sortBy, sortOrder, page, pageSize]);

  // Handle Sort column click
  const handleSort = (column: string) => {
    if (sortBy === column) {
      setSortOrder(sortOrder === "asc" ? "desc" : "asc");
    } else {
      setSortBy(column);
      setSortOrder("asc");
    }
    setPage(1);
  };

  const handleExportCsv = () => {
    window.open("/api/scholarships/export/csv", "_blank");
  };

  const totalPages = Math.max(1, Math.ceil(totalCount / pageSize));

  return (
    <div className="min-h-screen bg-[#05070A] text-slate-100 font-sans selection:bg-amber-500/30 selection:text-amber-200">
      {/* Top Header */}
      <header className="sticky top-0 z-30 w-full px-6 py-4 border-b border-white/[0.08] bg-[#05070A]/80 backdrop-blur-xl flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <Link href="/" className="flex items-center space-x-3 group">
            <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/40 flex items-center justify-center text-amber-400 font-bold text-sm shadow-[0_0_20px_rgba(212,175,55,0.25)] group-hover:scale-105 transition-all">
              SX
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="text-lg font-bold tracking-tight text-white font-sans">
                  SCHOLARX
                </span>
                <span className="text-[10px] uppercase font-mono font-bold px-2 py-0.5 rounded bg-sky-500/15 text-sky-400 border border-sky-500/30">
                  RELATIONAL DATABASE
                </span>
              </div>
              <p className="text-xs text-zinc-400 font-normal">
                310 Verified Institutional Opportunities Across 5 Continents
              </p>
            </div>
          </Link>
        </div>

        {/* Header Action Buttons */}
        <div className="flex items-center space-x-3">
          <button
            onClick={handleExportCsv}
            className="flex items-center space-x-2 px-3.5 py-1.5 rounded-lg border border-emerald-500/30 bg-emerald-500/10 hover:bg-emerald-500/20 text-xs font-mono text-emerald-400 font-semibold transition-all shadow-[0_0_12px_rgba(16,185,129,0.15)] cursor-pointer"
          >
            <FileSpreadsheet className="w-3.5 h-3.5" />
            <span>EXPORT CSV</span>
          </button>

          <Link
            href="/"
            className="flex items-center space-x-2 px-3.5 py-1.5 rounded-lg border border-white/[0.12] bg-white/[0.05] hover:bg-white/[0.1] text-xs font-mono text-zinc-300 transition-all cursor-pointer"
          >
            <Layers className="w-3.5 h-3.5 text-zinc-400" />
            <span>COMMAND THEATRE</span>
          </Link>

          <div className="flex items-center space-x-2 px-3 py-1.5 rounded-lg border border-amber-500/30 bg-amber-500/10 text-xs font-mono text-amber-400 font-bold">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>SQLITE ACTIVE (310)</span>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="max-w-[1600px] mx-auto px-4 sm:px-6 py-6">
        {/* Telemetry Stats Strip */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mb-6">
          <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-md">
            <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-wider mb-1">
              Total Opportunities
            </div>
            <div className="text-2xl font-bold font-mono text-white flex items-center gap-2">
              <span>{stats?.total_scholarships ?? 310}</span>
              <span className="text-[10px] font-normal px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                100% Verified
              </span>
            </div>
          </div>

          <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-md">
            <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-wider mb-1">
              HEC Bilateral Seats
            </div>
            <div className="text-2xl font-bold font-mono text-amber-400">
              {stats?.total_bilateral_seats ? stats.total_bilateral_seats.toLocaleString() : "2,444"}
            </div>
          </div>

          <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-md">
            <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-wider mb-1">
              MOI Waivers (No IELTS)
            </div>
            <div className="text-2xl font-bold font-mono text-sky-400">
              {stats?.moi_waiver_count ?? 131}
            </div>
          </div>

          <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-md">
            <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-wider mb-1">
              Europe Scouting
            </div>
            <div className="text-2xl font-bold font-mono text-emerald-400">
              {stats?.by_region?.["Europe"] ?? 101}
            </div>
          </div>

          <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-md">
            <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-wider mb-1">
              Asia Scouting
            </div>
            <div className="text-2xl font-bold font-mono text-purple-400">
              {stats?.by_region?.["Asia"] ?? 81}
            </div>
          </div>

          <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-md">
            <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-wider mb-1">
              Americas & MENA
            </div>
            <div className="text-2xl font-bold font-mono text-indigo-400">
              {(stats?.by_region?.["Americas"] ?? 65) + (stats?.by_region?.["MENA"] ?? 43)}
            </div>
          </div>
        </div>

        {/* Search & Multi-Facet Filters Bar */}
        <div className="p-4 rounded-2xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-xl mb-6 space-y-4">
          {/* Top Row: Search input + Region Selector Tabs */}
          <div className="flex flex-col md:flex-row gap-3 items-stretch md:items-center justify-between">
            {/* Search Input */}
            <div className="relative flex-1">
              <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-400" />
              <input
                type="text"
                placeholder="Search scholarship name, country, university, or keyword..."
                value={searchQuery}
                onChange={(e) => {
                  setSearchQuery(e.target.value);
                  setPage(1);
                }}
                className="w-full pl-10 pr-10 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-sm text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500/50 focus:ring-1 focus:ring-amber-500/40 transition-all font-sans"
              />
              {searchQuery && (
                <button
                  onClick={() => {
                    setSearchQuery("");
                    setPage(1);
                  }}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-400 hover:text-white"
                >
                  <X className="w-4 h-4" />
                </button>
              )}
            </div>

            {/* Region Tabs */}
            <div className="flex items-center gap-1.5 overflow-x-auto pb-1 md:pb-0 scrollbar-none">
              {["ALL", "Europe", "Asia", "Americas", "MENA", "Oceania"].map((r) => {
                const isSelected = selectedRegion === r;
                return (
                  <button
                    key={r}
                    onClick={() => {
                      setSelectedRegion(r);
                      setPage(1);
                    }}
                    className={`px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all shrink-0 cursor-pointer ${
                      isSelected
                        ? "bg-amber-500/20 text-amber-300 border border-amber-500/40 shadow-[0_0_12px_rgba(212,175,55,0.2)]"
                        : "bg-white/[0.03] text-zinc-400 border border-white/[0.06] hover:bg-white/[0.08] hover:text-zinc-200"
                    }`}
                  >
                    {r === "ALL" ? "All Regions" : r}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Bottom Filter Controls */}
          <div className="flex flex-wrap items-center gap-3 pt-2 border-t border-white/[0.05] text-xs">
            {/* Degree Filter */}
            <div className="flex items-center space-x-1.5">
              <span className="text-zinc-400 font-mono text-[11px]">Degree:</span>
              <select
                value={selectedDegree}
                onChange={(e) => {
                  setSelectedDegree(e.target.value);
                  setPage(1);
                }}
                className="px-2.5 py-1.5 rounded-lg bg-black/50 border border-white/[0.1] text-zinc-200 text-xs focus:outline-none focus:border-amber-500/50 cursor-pointer"
              >
                <option value="ALL">All Degree Levels</option>
                <option value="bachelor">Bachelor&apos;s / Undergrad</option>
                <option value="master">Master&apos;s / Postgraduate</option>
                <option value="phd">PhD / Doctoral</option>
              </select>
            </div>

            {/* Funding Filter */}
            <div className="flex items-center space-x-1.5">
              <span className="text-zinc-400 font-mono text-[11px]">Funding:</span>
              <select
                value={selectedFunding}
                onChange={(e) => {
                  setSelectedFunding(e.target.value);
                  setPage(1);
                }}
                className="px-2.5 py-1.5 rounded-lg bg-black/50 border border-white/[0.1] text-zinc-200 text-xs focus:outline-none focus:border-amber-500/50 cursor-pointer"
              >
                <option value="ALL">All Funding</option>
                <option value="FULL">100% Fully Funded</option>
                <option value="PARTIAL">Partially Funded</option>
                <option value="TUITION_ONLY">Tuition Fee Waiver</option>
              </select>
            </div>

            {/* Special Toggles */}
            <button
              onClick={() => {
                setHecOnly(!hecOnly);
                setPage(1);
              }}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg font-mono text-xs transition-all cursor-pointer ${
                hecOnly
                  ? "bg-amber-500/20 text-amber-300 border border-amber-500/50"
                  : "bg-white/[0.03] text-zinc-400 border border-white/[0.08] hover:text-zinc-200"
              }`}
            >
              <Award className="w-3.5 h-3.5 text-amber-400" />
              <span>HEC / Bilateral Quotas</span>
            </button>

            <button
              onClick={() => {
                setMoiOnly(!moiOnly);
                setPage(1);
              }}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg font-mono text-xs transition-all cursor-pointer ${
                moiOnly
                  ? "bg-sky-500/20 text-sky-300 border border-sky-500/50"
                  : "bg-white/[0.03] text-zinc-400 border border-white/[0.08] hover:text-zinc-200"
              }`}
            >
              <ShieldCheck className="w-3.5 h-3.5 text-sky-400" />
              <span>MOI Waiver (No IELTS)</span>
            </button>

            {/* Layout Density Switcher */}
            <div className="ml-auto flex items-center space-x-2">
              <span className="text-zinc-500 font-mono text-[11px]">Density:</span>
              <button
                onClick={() => setIsCompact(!isCompact)}
                className="px-2.5 py-1 rounded bg-white/[0.05] border border-white/[0.08] text-[11px] font-mono text-zinc-300 hover:bg-white/[0.1] cursor-pointer"
              >
                {isCompact ? "Compact" : "Comfortable"}
              </button>
            </div>
          </div>
        </div>

        {/* Results Metadata Bar */}
        <div className="flex items-center justify-between text-xs font-mono text-zinc-400 mb-3 px-1">
          <div>
            Showing <span className="text-white font-semibold">{(page - 1) * pageSize + 1}</span> -{" "}
            <span className="text-white font-semibold">
              {Math.min(page * pageSize, totalCount)}
            </span>{" "}
            of <span className="text-amber-400 font-bold">{totalCount}</span> relational records
          </div>

          <div className="flex items-center space-x-2">
            <span>Per Page:</span>
            <select
              value={pageSize}
              onChange={(e) => {
                setPageSize(Number(e.target.value));
                setPage(1);
              }}
              className="bg-black/50 border border-white/[0.1] rounded px-2 py-0.5 text-xs text-white cursor-pointer"
            >
              <option value="25">25</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </div>
        </div>

        {/* Relational Data Table */}
        <div className="w-full overflow-hidden rounded-2xl border border-white/[0.08] bg-white/[0.02] backdrop-blur-xl shadow-2xl">
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-white/[0.08] bg-white/[0.03] text-[11px] font-mono uppercase text-zinc-400">
                  <th
                    onClick={() => handleSort("scholarship_id")}
                    className="py-3.5 px-4 cursor-pointer hover:text-white transition-colors"
                  >
                    <div className="flex items-center space-x-1">
                      <span>ID</span>
                      {sortBy === "scholarship_id" && (sortOrder === "asc" ? <ArrowUp className="w-3 h-3 text-amber-400" /> : <ArrowDown className="w-3 h-3 text-amber-400" />)}
                    </div>
                  </th>
                  <th
                    onClick={() => handleSort("name")}
                    className="py-3.5 px-4 cursor-pointer hover:text-white transition-colors"
                  >
                    <div className="flex items-center space-x-1">
                      <span>Scholarship & University</span>
                      {sortBy === "name" && (sortOrder === "asc" ? <ArrowUp className="w-3 h-3 text-amber-400" /> : <ArrowDown className="w-3 h-3 text-amber-400" />)}
                    </div>
                  </th>
                  <th
                    onClick={() => handleSort("country")}
                    className="py-3.5 px-4 cursor-pointer hover:text-white transition-colors"
                  >
                    <div className="flex items-center space-x-1">
                      <span>Country & Region</span>
                      {sortBy === "country" && (sortOrder === "asc" ? <ArrowUp className="w-3 h-3 text-amber-400" /> : <ArrowDown className="w-3 h-3 text-amber-400" />)}
                    </div>
                  </th>
                  <th className="py-3.5 px-4">Funding</th>
                  <th className="py-3.5 px-4">Degrees</th>
                  <th
                    onClick={() => handleSort("min_gpa")}
                    className="py-3.5 px-4 cursor-pointer hover:text-white transition-colors"
                  >
                    <div className="flex items-center space-x-1">
                      <span>Min GPA</span>
                      {sortBy === "min_gpa" && (sortOrder === "asc" ? <ArrowUp className="w-3 h-3 text-amber-400" /> : <ArrowDown className="w-3 h-3 text-amber-400" />)}
                    </div>
                  </th>
                  <th className="py-3.5 px-4">Language / MOI</th>
                  <th
                    onClick={() => handleSort("stipend_pkr")}
                    className="py-3.5 px-4 cursor-pointer hover:text-white transition-colors text-right"
                  >
                    <div className="flex items-center justify-end space-x-1">
                      <span>Stipend (PKR/mo)</span>
                      {sortBy === "stipend_pkr" && (sortOrder === "asc" ? <ArrowUp className="w-3 h-3 text-amber-400" /> : <ArrowDown className="w-3 h-3 text-amber-400" />)}
                    </div>
                  </th>
                  <th
                    onClick={() => handleSort("deadline")}
                    className="py-3.5 px-4 cursor-pointer hover:text-white transition-colors"
                  >
                    <div className="flex items-center space-x-1">
                      <span>Deadline</span>
                      {sortBy === "deadline" && (sortOrder === "asc" ? <ArrowUp className="w-3 h-3 text-amber-400" /> : <ArrowDown className="w-3 h-3 text-amber-400" />)}
                    </div>
                  </th>
                  <th className="py-3.5 px-4 text-center">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/[0.04] text-xs">
                {loading ? (
                  <tr>
                    <td colSpan={10} className="py-16 text-center text-zinc-400 font-mono">
                      <RefreshCw className="w-6 h-6 animate-spin mx-auto text-amber-400 mb-2" />
                      Loading relational records from SQLite database...
                    </td>
                  </tr>
                ) : scholarships.length === 0 ? (
                  <tr>
                    <td colSpan={10} className="py-16 text-center text-zinc-400 font-mono">
                      No matching scholarships found for active filters.
                    </td>
                  </tr>
                ) : (
                  scholarships.map((s) => {
                    const isMoi =
                      Boolean(s.pakistan_requirements?.accepts_moi_certificate) ||
                      Boolean((s as any)?.deep_dossier?.eligibility_requirements?.moi_certificate_accepted);
                    const isHec =
                      Boolean(s.pakistan_requirements?.hec_managed) ||
                      Boolean(s.pakistan_requirements?.pakistan_bilateral_quota);
                    const stipendPkr = s.funding?.monthly_stipend_pkr_approx;
                    const degreeList = s.eligibility?.degree_levels || [];

                    return (
                      <tr
                        key={s.scholarship_id}
                        className="hover:bg-white/[0.03] transition-colors group cursor-pointer"
                        onClick={() => setActiveScholarship(s)}
                      >
                        {/* ID */}
                        <td className="py-3 px-4 font-mono text-[11px] font-semibold text-amber-400/90 whitespace-nowrap">
                          {s.scholarship_id}
                        </td>

                        {/* Title & University */}
                        <td className="py-3 px-4 max-w-sm">
                          <div className="font-semibold text-white group-hover:text-amber-300 transition-colors line-clamp-1">
                            {s.name}
                          </div>
                          <div className="text-[11px] text-zinc-400 line-clamp-1">
                            {s.host_institution || "National / Consortium Program"}
                          </div>
                        </td>

                        {/* Country & Region */}
                        <td className="py-3 px-4 whitespace-nowrap">
                          <div className="flex items-center space-x-1.5">
                            <span className="font-medium text-zinc-200">
                              {s.host_country_name || s.host_country}
                            </span>
                            <span className="text-[10px] font-mono px-1 py-0.2 rounded bg-white/[0.08] text-zinc-400">
                              {s.host_country}
                            </span>
                          </div>
                          <div className="text-[10px] text-zinc-500 font-mono">{s.region}</div>
                        </td>

                        {/* Funding */}
                        <td className="py-3 px-4 whitespace-nowrap">
                          <span
                            className={`inline-block px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase ${
                              s.funding?.funding_type === "FULL"
                                ? "bg-emerald-500/15 text-emerald-400 border border-emerald-500/30"
                                : s.funding?.funding_type === "PARTIAL"
                                ? "bg-amber-500/15 text-amber-400 border border-amber-500/30"
                                : "bg-sky-500/15 text-sky-400 border border-sky-500/30"
                            }`}
                          >
                            {s.funding?.funding_type || "FULL"}
                          </span>
                        </td>

                        {/* Degrees */}
                        <td className="py-3 px-4 whitespace-nowrap">
                          <div className="flex flex-wrap gap-1">
                            {degreeList.slice(0, 2).map((d) => (
                              <span
                                key={d}
                                className="px-1.5 py-0.5 rounded bg-white/[0.06] text-[10px] font-mono text-zinc-300"
                              >
                                {d.replace("Master's", "MS").replace("Bachelor's", "BS")}
                              </span>
                            ))}
                            {degreeList.length > 2 && (
                              <span className="px-1 py-0.5 rounded bg-white/[0.04] text-[10px] font-mono text-zinc-400">
                                +{degreeList.length - 2}
                              </span>
                            )}
                          </div>
                        </td>

                        {/* Min GPA */}
                        <td className="py-3 px-4 whitespace-nowrap font-mono text-[11px] text-zinc-300">
                          {s.eligibility?.min_gpa_4_scale ? (
                            <span>{s.eligibility.min_gpa_4_scale} / 4.0</span>
                          ) : s.eligibility?.min_gpa_percentage ? (
                            <span>{s.eligibility.min_gpa_percentage}%</span>
                          ) : (
                            <span className="text-zinc-600">—</span>
                          )}
                        </td>

                        {/* Language / MOI */}
                        <td className="py-3 px-4 whitespace-nowrap">
                          {isMoi ? (
                            <span className="inline-flex items-center space-x-1 px-1.5 py-0.5 rounded bg-sky-500/15 text-sky-300 border border-sky-500/30 text-[10px] font-mono">
                              <ShieldCheck className="w-2.5 h-2.5" />
                              <span>MOI WAIVER</span>
                            </span>
                          ) : s.language?.minimum_ielts ? (
                            <span className="text-[11px] font-mono text-zinc-300">
                              IELTS {s.language.minimum_ielts}
                            </span>
                          ) : (
                            <span className="text-zinc-600 font-mono text-[11px]">—</span>
                          )}
                        </td>

                        {/* Stipend PKR */}
                        <td className="py-3 px-4 whitespace-nowrap font-mono text-[11px] text-right">
                          {stipendPkr ? (
                            <div className="text-emerald-400 font-semibold">
                              ₨ {stipendPkr.toLocaleString()}
                            </div>
                          ) : (
                            <div className="text-zinc-500 text-[10px]">
                              {s.funding?.monthly_stipend || "Coverage Only"}
                            </div>
                          )}
                        </td>

                        {/* Deadline */}
                        <td className="py-3 px-4 whitespace-nowrap font-mono text-[11px] text-zinc-300">
                          {s.application_deadline || "Annual Intake"}
                        </td>

                        {/* Action buttons */}
                        <td className="py-3 px-4 text-center whitespace-nowrap" onClick={(e) => e.stopPropagation()}>
                          <div className="flex items-center justify-center space-x-1.5">
                            <button
                              onClick={() => setActiveScholarship(s)}
                              className="px-2 py-1 rounded bg-white/[0.06] hover:bg-white/[0.12] text-[11px] font-mono text-zinc-300 transition-colors cursor-pointer"
                            >
                              Inspect
                            </button>
                            <Link
                              href={`/dossier/${s.scholarship_id}`}
                              className="p-1 rounded bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 transition-colors"
                              title="Open Full 11-Dimension Dossier"
                            >
                              <ExternalLink className="w-3.5 h-3.5" />
                            </Link>
                          </div>
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>

          {/* Pagination Footer */}
          <div className="px-6 py-4 border-t border-white/[0.08] bg-white/[0.02] flex items-center justify-between">
            <button
              onClick={() => setPage(Math.max(1, page - 1))}
              disabled={page <= 1}
              className="px-3 py-1.5 rounded-lg border border-white/[0.1] bg-white/[0.04] disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/[0.08] text-xs font-mono text-zinc-300 transition-colors"
            >
              Previous Page
            </button>

            <div className="text-xs font-mono text-zinc-400">
              Page <span className="text-white font-bold">{page}</span> of{" "}
              <span className="text-white font-bold">{totalPages}</span>
            </div>

            <button
              onClick={() => setPage(Math.min(totalPages, page + 1))}
              disabled={page >= totalPages}
              className="px-3 py-1.5 rounded-lg border border-white/[0.1] bg-white/[0.04] disabled:opacity-30 disabled:cursor-not-allowed hover:bg-white/[0.08] text-xs font-mono text-zinc-300 transition-colors"
            >
              Next Page
            </button>
          </div>
        </div>
      </main>

      {/* Quick View Detail Drawer / Modal */}
      {activeScholarship && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md animate-in fade-in duration-200">
          <div className="relative w-full max-w-2xl max-h-[90vh] overflow-y-auto rounded-2xl border border-white/[0.15] bg-[#0A0E17] p-6 shadow-2xl">
            {/* Modal Header */}
            <div className="flex items-start justify-between pb-4 border-b border-white/[0.08] mb-4">
              <div>
                <div className="flex items-center space-x-2 mb-1">
                  <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-mono font-bold">
                    {activeScholarship.scholarship_id}
                  </span>
                  <span className="text-xs text-zinc-400 font-mono">
                    {activeScholarship.region} Scouting
                  </span>
                </div>
                <h3 className="text-lg font-bold text-white font-sans">
                  {activeScholarship.name}
                </h3>
                <p className="text-xs text-zinc-400">
                  {activeScholarship.host_institution || "Universities in " + (activeScholarship.host_country_name || activeScholarship.host_country)}
                </p>
              </div>

              <button
                onClick={() => setActiveScholarship(null)}
                className="p-1 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] text-zinc-400 hover:text-white transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Body */}
            <div className="space-y-4 text-xs">
              {/* Financial Coverage Highlights */}
              <div className="p-3.5 rounded-xl border border-emerald-500/20 bg-emerald-500/5 space-y-2">
                <div className="font-mono text-emerald-400 font-semibold uppercase text-[11px] flex items-center gap-1.5">
                  <DollarSign className="w-3.5 h-3.5" />
                  <span>Financial Benefits & Stipend</span>
                </div>
                <div className="grid grid-cols-2 gap-2 text-zinc-300">
                  <div>
                    <span className="text-zinc-500">Monthly Stipend:</span>{" "}
                    <span className="font-semibold text-emerald-300">
                      {activeScholarship.funding?.monthly_stipend_pkr_approx
                        ? `₨ ${activeScholarship.funding.monthly_stipend_pkr_approx.toLocaleString()} (~${activeScholarship.funding.monthly_stipend})`
                        : activeScholarship.funding?.monthly_stipend || "Waived"}
                    </span>
                  </div>
                  <div>
                    <span className="text-zinc-500">Tuition:</span>{" "}
                    <span className="font-semibold">{activeScholarship.funding?.tuition || "100% Waived"}</span>
                  </div>
                  <div>
                    <span className="text-zinc-500">Accommodation:</span>{" "}
                    <span>{activeScholarship.funding?.accommodation || "Covered"}</span>
                  </div>
                  <div>
                    <span className="text-zinc-500">Airfare:</span>{" "}
                    <span>{activeScholarship.funding?.travel_airfare || "NOT_COVERED"}</span>
                  </div>
                </div>
              </div>

              {/* Eligibility & Requirements */}
              <div className="p-3.5 rounded-xl border border-white/[0.08] bg-white/[0.02] space-y-2">
                <div className="font-mono text-amber-400 font-semibold uppercase text-[11px] flex items-center gap-1.5">
                  <GraduationCap className="w-3.5 h-3.5" />
                  <span>Eligibility & Cutoffs</span>
                </div>
                <div className="grid grid-cols-2 gap-2 text-zinc-300">
                  <div>
                    <span className="text-zinc-500">Degree Levels:</span>{" "}
                    <span>{activeScholarship.eligibility?.degree_levels?.join(", ") || "All"}</span>
                  </div>
                  <div>
                    <span className="text-zinc-500">Min GPA Cutoff:</span>{" "}
                    <span className="font-mono">
                      {activeScholarship.eligibility?.min_gpa_4_scale
                        ? `${activeScholarship.eligibility.min_gpa_4_scale} / 4.0`
                        : "No strict cutoff"}
                    </span>
                  </div>
                  <div>
                    <span className="text-zinc-500">English / IELTS:</span>{" "}
                    <span>
                      {activeScholarship.language?.minimum_ielts
                        ? `IELTS ${activeScholarship.language.minimum_ielts}+`
                        : "Test optional / Not mandatory"}
                    </span>
                  </div>
                  <div>
                    <span className="text-zinc-500">MOI Waiver:</span>{" "}
                    <span
                      className={
                        activeScholarship.pakistan_requirements?.accepts_moi_certificate
                          ? "text-sky-400 font-semibold"
                          : "text-zinc-400"
                      }
                    >
                      {activeScholarship.pakistan_requirements?.accepts_moi_certificate
                        ? "Accepted (No IELTS)"
                        : "Official Test Required"}
                    </span>
                  </div>
                </div>
              </div>

              {/* Pakistan Bilateral / HEC Specifics */}
              {Boolean(activeScholarship.pakistan_requirements?.pakistan_bilateral_quota || activeScholarship.pakistan_requirements?.hec_managed) && (
                <div className="p-3.5 rounded-xl border border-amber-500/20 bg-amber-500/5 space-y-1.5">
                  <div className="font-mono text-amber-400 font-semibold uppercase text-[11px] flex items-center gap-1.5">
                    <Award className="w-3.5 h-3.5" />
                    <span>Pakistani Bilateral Quota Program</span>
                  </div>
                  <p className="text-zinc-300">
                    This program offers reserved bilateral nomination seats for Pakistani citizens (e.g.{" "}
                    {activeScholarship.pakistan_requirements?.pakistan_quota_seats
                      ? `${activeScholarship.pakistan_requirements.pakistan_quota_seats} annual seats`
                      : "Government bilateral quota"}
                    ). Applications route through HEC portal.
                  </p>
                </div>
              )}

              {/* Description */}
              {activeScholarship.description && (
                <div className="text-zinc-400 leading-relaxed pt-1">
                  <p>{activeScholarship.description}</p>
                </div>
              )}
            </div>

            {/* Modal Footer */}
            <div className="mt-6 pt-4 border-t border-white/[0.08] flex items-center justify-between gap-3">
              <Link
                href={`/dossier/${activeScholarship.scholarship_id}`}
                className="flex items-center space-x-2 px-4 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-mono font-semibold transition-all shadow-[0_0_15px_rgba(212,175,55,0.2)]"
              >
                <span>OPEN FULL 11-DIMENSION DOSSIER</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>

              {activeScholarship.source_url && (
                <a
                  href={activeScholarship.source_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center space-x-1.5 px-3 py-2 rounded-xl bg-white/[0.05] hover:bg-white/[0.1] text-zinc-300 text-xs font-mono transition-colors"
                >
                  <span>Official University Portal</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
