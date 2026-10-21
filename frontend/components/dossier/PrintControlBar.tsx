"use client";

import React, { useEffect } from "react";
import Link from "next/link";
import { Printer, ArrowLeft, Download } from "lucide-react";
import { sound } from "@/lib/sound-fx";

export const PrintControlBar: React.FC<{ returnHref?: string; autoPrint?: boolean }> = ({
  returnHref = "/",
  autoPrint = false,
}) => {
  useEffect(() => {
    if (autoPrint && typeof window !== "undefined") {
      const timer = setTimeout(() => {
        window.print();
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [autoPrint]);

  const handlePrint = () => {
    sound.playClick();
    if (typeof window !== "undefined") {
      window.print();
    }
  };

  return (
    <div className="w-full max-w-[880px] bg-[#27272A] text-white px-4 sm:px-6 py-2.5 rounded-xl border border-white/10 shadow-xl mb-4 flex flex-wrap items-center justify-between gap-2.5 no-print">
      <div className="flex items-center space-x-2 text-xs font-mono">
        <Printer className="w-4 h-4 text-emerald-400 shrink-0" />
        <span className="font-bold text-white">VECTOR PRINT PIPELINE</span>
        <span className="text-white/40">•</span>
        <span className="text-stone-300">A4 Publication Mode (Multi-Page Paginated)</span>
      </div>

      <div className="flex items-center space-x-2 text-xs font-mono">
        <Link
          href={returnHref}
          className="px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/15 text-white flex items-center space-x-1 transition-all"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>RETURN</span>
        </Link>
        <button
          type="button"
          onClick={handlePrint}
          className="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold flex items-center space-x-1.5 transition-all shadow-md cursor-pointer"
          title="Print or Save official candidate dossier as publication PDF"
        >
          <Download className="w-3.5 h-3.5 stroke-[2.5]" />
          <span>PRINT / SAVE AS PDF</span>
        </button>
      </div>
    </div>
  );
};
