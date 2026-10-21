import React from "react";
import type { Metadata } from "next";
import { getAllCatalogScholarships } from "@/lib/dossier/catalogNormalizer";
import { CatalogBrowser } from "@/components/catalog/CatalogBrowser";
import { getBaseUrl } from "@/lib/utils/seo";

export const dynamic = "force-static";

export async function generateMetadata(): Promise<Metadata> {
  const baseUrl = getBaseUrl();
  const title = "Scholarship Directory — 310+ Global Programs for Pakistani Students";
  const description =
    "Verified directory of 310+ fully funded international scholarships and bilateral quota opportunities for Pakistani scholars across Europe, Asia, Americas, MENA, and Oceania.";

  return {
    title,
    description,
    keywords: [
      "scholarship directory",
      "scholarships for pakistani students 2026 2027",
      "fully funded scholarships",
      "bilateral scholarships pakistan",
      "hec scholarship list",
      "stipendium hungaricum",
      "turkiye burslari",
      "csc scholarship",
      "daad germany",
      "fulbright pakistan",
      "mext japan",
      "singa singapore",
    ],
    alternates: {
      canonical: `${baseUrl}/catalog`,
    },
    openGraph: {
      title,
      description,
      url: `${baseUrl}/catalog`,
      type: "website",
      images: [
        {
          url: "/opengraph-image",
          width: 1200,
          height: 630,
          alt: "ScholarX Global Scholarship Directory",
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: ["/opengraph-image"],
    },
  };
}

export default async function CatalogPage() {
  const scholarships = getAllCatalogScholarships();
  const baseUrl = getBaseUrl();

  const collectionSchema = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: "ScholarX International Scholarship Directory",
    description: "Directory of 310+ fully funded international scholarships for Pakistani students.",
    url: `${baseUrl}/catalog`,
    mainEntity: {
      "@type": "ItemList",
      numberOfItems: scholarships.length,
      itemListElement: scholarships.slice(0, 30).map((item, idx) => ({
        "@type": "ListItem",
        position: idx + 1,
        name: item.name,
        url: `${baseUrl}/dossier/${encodeURIComponent(item.id)}`,
      })),
    },
  };

  const breadcrumbsSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: [
      {
        "@type": "ListItem",
        position: 1,
        name: "Home",
        item: baseUrl,
      },
      {
        "@type": "ListItem",
        position: 2,
        name: "Scholarship Directory",
        item: `${baseUrl}/catalog`,
      },
    ],
  };

  return (
    <main className="min-h-screen bg-sx-black text-sx-text-primary antialiased">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(collectionSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbsSchema) }}
      />
      <CatalogBrowser initialScholarships={scholarships} />
    </main>
  );
}
