import type { Metadata, Viewport } from "next";
import "./globals.css";
import { SITE_CONFIG, getBaseUrl } from "@/lib/utils/seo";

const baseUrl = getBaseUrl();

export const viewport: Viewport = {
  themeColor: "#08080A",
  colorScheme: "dark",
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  metadataBase: new URL(baseUrl),
  title: {
    default: SITE_CONFIG.defaultTitle,
    template: SITE_CONFIG.titleTemplate,
  },
  description: SITE_CONFIG.defaultDescription,
  keywords: SITE_CONFIG.keywords,
  authors: [{ name: "ScholarX Team", url: baseUrl }],
  creator: "ScholarX Intelligence Network",
  publisher: "ScholarX",
  applicationName: "ScholarX",
  generator: "Next.js 15",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  alternates: {
    canonical: "./",
    languages: {
      "en-US": "/",
    },
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: baseUrl,
    title: SITE_CONFIG.defaultTitle,
    description: SITE_CONFIG.defaultDescription,
    siteName: "ScholarX",
    images: [
      {
        url: "/opengraph-image",
        width: 1200,
        height: 630,
        alt: "ScholarX — Autonomous Scholarship Intelligence Network",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: SITE_CONFIG.defaultTitle,
    description: SITE_CONFIG.defaultDescription,
    creator: SITE_CONFIG.creator,
    images: ["/opengraph-image"],
  },
  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: {
      index: true,
      follow: true,
      noimageindex: false,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  verification: {
    google: process.env.NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION || undefined,
    yandex: process.env.NEXT_PUBLIC_YANDEX_SITE_VERIFICATION || undefined,
    other: {
      "msvalidate.01": process.env.NEXT_PUBLIC_BING_SITE_VERIFICATION || "",
    },
  },
  category: "education",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: "ScholarX AI",
    alternateName: [
      "ScholarX",
      "ScholarX AI",
      "Scholar X",
      "scholarx-ai",
      "ScholarX Intelligence Network",
      "Scholarships for Pakistani Students",
    ],
    url: baseUrl,
    description: SITE_CONFIG.defaultDescription,
    potentialAction: {
      "@type": "SearchAction",
      target: {
        "@type": "EntryPoint",
        urlTemplate: `${baseUrl}/catalog?q={search_term_string}`,
      },
      "query-input": "required name=search_term_string",
    },
  };

  const orgSchema = {
    "@context": "https://schema.org",
    "@type": "Organization",
    name: "ScholarX AI",
    alternateName: ["ScholarX", "ScholarX AI", "Scholar X", "scholarx-ai"],
    url: baseUrl,
    logo: `${baseUrl}/apple-icon`,
    description: "Pakistan's premier autonomous scholarship intelligence platform discovering and verifying global scholarships for Pakistani students.",
    contactPoint: {
      "@type": "ContactPoint",
      contactType: "academic support",
      areaServed: ["PK", "Global"],
      availableLanguage: ["English", "Urdu"],
    },
  };

  const appSchema = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    name: "ScholarX AI — Autonomous Scholarship Intelligence Network",
    operatingSystem: "Web",
    applicationCategory: "EducationalApplication",
    offers: {
      "@type": "Offer",
      price: "0",
      priceCurrency: "USD",
    },
    description: "Autonomous multi-agent intelligence platform discovering and verifying 310+ fully funded international scholarships and bilateral quotas for Pakistani students.",
  };

  return (
    <html lang="en" className="dark" suppressHydrationWarning>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteSchema) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(orgSchema) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(appSchema) }}
        />
      </head>
      <body
        className="bg-sx-black text-sx-text-primary antialiased overflow-x-hidden min-h-screen w-full font-sans"
        suppressHydrationWarning
      >
        {children}
      </body>
    </html>
  );
}
