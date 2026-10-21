import React from "react";
import type { Metadata } from "next";
import { getAllCatalogScholarships } from "@/lib/dossier/catalogNormalizer";
import { CatalogPrintView } from "@/components/dossier/CatalogPrintView";
import { getBaseUrl } from "@/lib/utils/seo";

export const dynamic = "force-static";

export function generateMetadata(): Metadata {
  const baseUrl = getBaseUrl();
  return {
    title: "Global Scholarship Catalog Print Sheet",
    description: "High-density matrix of 310 international scholarships.",
    robots: {
      index: false,
      follow: true,
    },
    alternates: {
      canonical: `${baseUrl}/catalog`,
    },
  };
}

export default async function CatalogPrintPage() {
  const scholarships = getAllCatalogScholarships();

  return <CatalogPrintView scholarships={scholarships} />;
}
