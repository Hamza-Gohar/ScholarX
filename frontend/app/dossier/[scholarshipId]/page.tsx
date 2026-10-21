import React from "react";
import type { Metadata } from "next";
import { resolveScholarshipDossier } from "@/lib/dossier/dossierResolver";
import { getAllCatalogScholarships } from "@/lib/dossier/catalogNormalizer";
import { WebDossierView } from "@/components/dossier/WebDossierView";
import { getBaseUrl } from "@/lib/utils/seo";

export const dynamicParams = true;
export const revalidate = 3600;

export async function generateStaticParams() {
  const scholarships = getAllCatalogScholarships();
  // Keep deployments fast while allowing every catalog dossier to render on demand.
  return scholarships.slice(0, 24).map((s) => ({
    scholarshipId: s.id,
  }));
}

export async function generateMetadata(props: {
  params: Promise<{ scholarshipId: string }>;
}): Promise<Metadata> {
  const { scholarshipId } = await props.params;
  const { dossier } = await resolveScholarshipDossier(scholarshipId);
  const baseUrl = getBaseUrl();

  const name =
    dossier?.opportunity?.name ||
    dossier?.title?.replace(" — Intelligence Dossier", "") ||
    scholarshipId;
  const country = dossier?.country || "International";
  const degree = dossier?.degreeLevel || "Higher Education";
  const deadline =
    dossier?.opportunity?.deadlineSummary?.applicationDeadline || "Annual Cycle";
  const funding =
    dossier?.opportunity?.fundingSummary?.coverageType === "FULL"
      ? "Fully Funded"
      : "Funded";
  const quota =
    dossier?.opportunity?.quotaDescription || "Bilateral Quota for Pakistan";

  const title = `${name} (${country}) — Pakistan Quota & Eligibility 2026/2027`;
  const description = `Verified intelligence dossier for ${name} in ${country}. ${funding} coverage (${degree}), ${quota}, HEC attestation roadmap, and application deadline (${deadline}) for Pakistani students.`;

  return {
    title,
    description,
    keywords: [
      name.toLowerCase(),
      `${name.toLowerCase()} pakistan`,
      `${name.toLowerCase()} eligibility`,
      `${name.toLowerCase()} deadline 2026 2027`,
      `${country.toLowerCase()} scholarships for pakistani students`,
      "fully funded scholarships",
      "hec foreign scholarships",
    ],
    alternates: {
      canonical: `${baseUrl}/dossier/${encodeURIComponent(scholarshipId)}`,
    },
    robots: {
      index: false,
      follow: true,
      nocache: true,
      googleBot: {
        index: false,
        follow: true,
      },
    },
    openGraph: {
      title: `${name} | ScholarX Dossier`,
      description,
      url: `${baseUrl}/dossier/${encodeURIComponent(scholarshipId)}`,
      type: "article",
      images: [
        {
          url: "/opengraph-image",
          width: 1200,
          height: 630,
          alt: `${name} scholarship dossier`,
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      title: `${name} (${country})`,
      description,
      images: ["/opengraph-image"],
    },
  };
}

export default async function ScholarshipDossierPage(props: {
  params: Promise<{ scholarshipId: string }>;
}) {
  const { scholarshipId } = await props.params;
  const { dossier } = await resolveScholarshipDossier(scholarshipId);
  const baseUrl = getBaseUrl();

  const name =
    dossier?.opportunity?.name ||
    dossier?.title?.replace(" — Intelligence Dossier", "") ||
    scholarshipId;
  const country = dossier?.country || "International";
  const deadline =
    dossier?.opportunity?.deadlineSummary?.applicationDeadline || "Annual Cycle";
  const funding =
    dossier?.opportunity?.fundingSummary?.coverageType === "FULL"
      ? "Fully Funded"
      : "Funded";

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
      {
        "@type": "ListItem",
        position: 3,
        name: name,
        item: `${baseUrl}/dossier/${encodeURIComponent(scholarshipId)}`,
      },
    ],
  };

  const assistanceSchema = {
    "@context": "https://schema.org",
    "@type": "FinancialAssistanceProgram",
    name: name,
    description: dossier?.executiveSummary || `${name} in ${country} for Pakistani students.`,
    url: `${baseUrl}/dossier/${encodeURIComponent(scholarshipId)}`,
    provider: {
      "@type": "GovernmentOrganization",
      name: country,
    },
    areaServed: {
      "@type": "Country",
      name: "Pakistan",
    },
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: [
      {
        "@type": "Question",
        name: `Is ${name} fully funded for Pakistani applicants?`,
        acceptedAnswer: {
          "@type": "Answer",
          text: `${name} is classified as ${funding}. It offers institutional tuition coverage and financial living support as verified by ScholarX intelligence.`,
        },
      },
      {
        "@type": "Question",
        name: `What is the application deadline for ${name}?`,
        acceptedAnswer: {
          "@type": "Answer",
          text: `The active admission timeline deadline is ${deadline}. Applicants are advised to attest documents via HEC/IBCC 4 to 6 weeks before submission.`,
        },
      },
      {
        "@type": "Question",
        name: `Are Pakistani students eligible to apply for ${name}?`,
        acceptedAnswer: {
          "@type": "Answer",
          text: `Yes, Pakistani nationals are eligible under bilateral quota allocations and international partner institution channels.`,
        },
      },
      {
        "@type": "Question",
        name: `Is IELTS mandatory or is an English Medium of Instruction (MOI) accepted?`,
        acceptedAnswer: {
          "@type": "Answer",
          text: `Requirements depend on host university policies. Several bilateral and European partners accept an official MOI certificate issued by previous Pakistani universities. Check the verified checklist in this dossier.`,
        },
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbsSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(assistanceSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />
      <WebDossierView dossier={dossier} isPrintMode={false} />
    </>
  );
}
