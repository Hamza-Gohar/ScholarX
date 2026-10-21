import React from "react";
import type { Metadata } from "next";
import { resolveScholarshipDossier } from "@/lib/dossier/dossierResolver";
import { getAllCatalogScholarships } from "@/lib/dossier/catalogNormalizer";
import { WebDossierView } from "@/components/dossier/WebDossierView";
import { PrintControlBar } from "@/components/dossier/PrintControlBar";
import { getBaseUrl } from "@/lib/utils/seo";

export const dynamicParams = true;
export const revalidate = 3600;

export async function generateStaticParams() {
  const scholarships = getAllCatalogScholarships();
  return scholarships.slice(0, 24).map((s) => ({
    scholarshipId: s.id,
  }));
}

export async function generateMetadata(props: {
  params: Promise<{ scholarshipId: string }>;
}): Promise<Metadata> {
  const { scholarshipId } = await props.params;
  const baseUrl = getBaseUrl();

  return {
    title: `Print Dossier — ${scholarshipId}`,
    robots: {
      index: false,
      follow: true,
    },
    alternates: {
      canonical: `${baseUrl}/dossier/${encodeURIComponent(scholarshipId)}`,
    },
  };
}

export default async function ScholarshipDossierPrintPage(props: {
  params: Promise<{ scholarshipId: string }>;
  searchParams?: Promise<{ autoprint?: string }>;
}) {
  const { scholarshipId } = await props.params;
  const searchParams = props.searchParams ? await props.searchParams : {};
  const autoPrint = searchParams.autoprint === "true";
  const { dossier } = await resolveScholarshipDossier(scholarshipId);

  return (
    <div className="bg-[#18181B] min-h-screen py-4 sm:py-8 px-2 sm:px-4 flex flex-col items-center print:bg-white print:p-0 print:m-0 print:min-h-0 print:block">
      <PrintControlBar returnHref={`/dossier/${scholarshipId}`} autoPrint={autoPrint} />

      {/* A4 Sheet Container */}
      <div className="w-full max-w-[880px] bg-[#FAFAF9] shadow-2xl rounded-sm border border-stone-400/30 overflow-visible print:border-none print:shadow-none print:max-w-none print:w-full print:p-0 print:m-0">
        <WebDossierView dossier={dossier} isPrintMode={true} />
      </div>
    </div>
  );
}
