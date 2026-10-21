import { MetadataRoute } from "next";
import { getBaseUrl } from "@/lib/utils/seo";

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = getBaseUrl();
  const lastModified = new Date();

  // Core Platform Authority Routes (Concentrating all domain authority on primary entry points)
  return [
    {
      url: baseUrl,
      lastModified,
      changeFrequency: "daily",
      priority: 1.0,
    },
    {
      url: `${baseUrl}/catalog`,
      lastModified,
      changeFrequency: "daily",
      priority: 0.9,
    },
    {
      url: `${baseUrl}/slides`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.7,
    },
  ];
}
