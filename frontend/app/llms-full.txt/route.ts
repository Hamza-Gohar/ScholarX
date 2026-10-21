import { getBaseUrl } from "@/lib/utils/seo";
import { getAllCatalogScholarships } from "@/lib/dossier/catalogNormalizer";

export async function GET() {
  const baseUrl = getBaseUrl();
  const scholarships = getAllCatalogScholarships();

  let text = `# ScholarX — Full International Scholarship Knowledge Base

Total Programs Documented: ${scholarships.length}
Target Audience: Pakistani & Global Higher Education Applicants
Generated for AI Agents, Perplexity, ChatGPT, and Research Assistants.

---

`;

  for (const item of scholarships) {
    text += `### [${item.id}] ${item.name}
- **Country**: ${item.country} (${item.region})
- **Offering Entity**: ${item.offering_entity}
- **Host Institutions**: ${item.host_institutions}
- **Degree Levels**: ${item.degree_levels_str}
- **Funding Classification**: ${item.funding_type}
- **Coverage**: Tuition (${item.financial_coverage.tuition.status}), Stipend (${item.financial_coverage.monthly_stipend.status}${item.financial_coverage.monthly_stipend.amount ? ` - ${item.financial_coverage.monthly_stipend.amount}` : ""}), Airfare (${item.financial_coverage.airfare.status})
- **English Requirement**: ${item.eligibility.english_badge}
- **Application Deadline**: ${item.deadline}
- **Dossier URL**: ${baseUrl}/dossier/${encodeURIComponent(item.id)}
- **Official Source**: ${item.official_sources[0]?.url || "https://scholarship.hec.gov.pk"}

`;
  }

  return new Response(text, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=86400, s-maxage=86400",
    },
  });
}
