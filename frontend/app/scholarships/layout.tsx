import type { Metadata } from "next";
import { getBaseUrl } from "@/lib/utils/seo";

export async function generateMetadata(): Promise<Metadata> {
  const baseUrl = getBaseUrl();
  const title = "Scholarship Database — 310+ International Opportunities";
  const description =
    "Searchable database of 310+ international scholarships, bilateral quotas, and HEC opportunities for Pakistani students.";

  return {
    title,
    description,
    alternates: {
      canonical: `${baseUrl}/scholarships`,
    },
    openGraph: {
      title,
      description,
      url: `${baseUrl}/scholarships`,
      type: "website",
      images: [
        {
          url: "/opengraph-image",
          width: 1200,
          height: 630,
          alt: "ScholarX Global Scholarship Database",
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

export default function ScholarshipsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
