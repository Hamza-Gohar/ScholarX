import { MetadataRoute } from "next";
import { getBaseUrl } from "@/lib/utils/seo";

export default function robots(): MetadataRoute.Robots {
  const baseUrl = getBaseUrl();

  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: [
          "/api/exhibition/",
          "/api/health",
          "/mission/",
        ],
      },
      {
        userAgent: ["GPTBot", "Claude-Web", "PerplexityBot", "Applebot-Extended"],
        allow: "/",
      },
    ],
    sitemap: `${baseUrl}/sitemap.xml`,
    host: baseUrl,
  };
}
