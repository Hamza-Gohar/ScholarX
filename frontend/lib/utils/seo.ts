export function getBaseUrl(): string {
  if (process.env.NEXT_PUBLIC_APP_URL) {
    return process.env.NEXT_PUBLIC_APP_URL.replace(/\/+$/, "");
  }
  if (process.env.NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL) {
    return `https://${process.env.NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL}`;
  }
  if (process.env.VERCEL_PROJECT_PRODUCTION_URL) {
    return `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`;
  }
  if (process.env.NEXT_PUBLIC_VERCEL_URL) {
    return `https://${process.env.NEXT_PUBLIC_VERCEL_URL}`;
  }
  if (process.env.VERCEL_URL) {
    return `https://${process.env.VERCEL_URL}`;
  }
  return "https://scholarx.online";
}

export const SITE_CONFIG = {
  name: "ScholarX AI",
  titleTemplate: "%s | ScholarX AI",
  defaultTitle: "ScholarX AI — Scholarships for Pakistani Students | Fully Funded International Programs",
  defaultDescription: "ScholarX AI is Pakistan's #1 autonomous scholarship intelligence platform. Discover 310+ fully funded international scholarships for Pakistani students, verified bilateral quotas (Fulbright, Chevening, DAAD, CSC China, Stipendium Hungaricum, MEXT Japan, Turkiye Burslari), HEC attestation roadmaps, and eligibility matching.",
  siteUrl: getBaseUrl(),
  ogImage: "/opengraph-image",
  creator: "@ScholarX_AI",
  keywords: [
    "ScholarX",
    "ScholarX AI",
    "Scholar X",
    "scholarx-ai",
    "scholarships for pakistani students",
    "scholarships for pakistan students",
    "fully funded scholarships for pakistani students",
    "scholarships for pakistani students 2026 2027",
    "hec foreign scholarships",
    "hec foreign scholarships for pakistani students",
    "stipendium hungaricum scholarship pakistan",
    "turkiye burslari scholarship pakistan",
    "chinese government scholarship csc pakistan",
    "daad scholarship germany pakistan",
    "fulbright scholarship pakistan",
    "chevening scholarship pakistan",
    "mext scholarship japan pakistan",
    "kgsp global korea scholarship pakistan",
    "singa scholarship singapore",
    "australia awards pakistan",
    "erasmus mundus scholarship pakistan",
    "scholarships without ielts for pakistani students",
    "moi accepted scholarships pakistan",
    "masters scholarships abroad for pakistanis",
    "phd scholarships abroad for pakistanis",
    "bachelors scholarships abroad for pakistanis",
  ],
  googleVerification: process.env.NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION || "",
  bingVerification: process.env.NEXT_PUBLIC_BING_SITE_VERIFICATION || "",
  yandexVerification: process.env.NEXT_PUBLIC_YANDEX_SITE_VERIFICATION || "",
};
