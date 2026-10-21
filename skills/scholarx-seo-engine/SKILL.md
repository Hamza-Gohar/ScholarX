---
name: scholarx-seo-engine
description: Autonomous SEO, Google Search Console, and AI Visibility audit and optimization engine for ScholarX. Grounded in Google Search Central standards and OpenSEO agent workflows.
---

# ScholarX SEO & AI Visibility Engine

Autonomous SEO, Google Search Console (GSC), and Generative Engine Optimization (GEO) skill for ScholarX. Built to maximize global and Pakistan-specific search visibility across traditional search engines (Google, Bing) and AI search agents (ChatGPT Search, Perplexity, Claude, Google AI Overviews).

---

## 1. Core Architecture & Indexing Topology

ScholarX exposes 3 primary discoverability layers:

1. **Static Platform Routes**:
   - `/`: Command Theatre & Autonomous Agent Operations
   - `/catalog`: Comprehensive Public Scholarship Directory (310+ indexable programs)
   - `/catalog/print`: High-density comparative matrix
   - `/slides`: Exhibition slide deck

2. **Dynamic Program Dossiers (`/dossier/[scholarshipId]`)**:
   - 310 Deeply Investigated Programs pre-rendered with Next.js 15 Static Site Generation (`generateStaticParams`).
   - Dynamic canonical URLs preventing query parameter duplication.
   - Tailored Schema.org JSON-LD structured data (`FinancialAssistanceProgram`, `FAQPage`, `BreadcrumbList`).

3. **Machine & Bot Discovery Endpoints**:
   - `/sitemap.xml`: XML sitemap containing all 314+ platform URLs with priorities and change frequencies.
   - `/robots.txt`: Bot access rules permitting Googlebot, Bingbot, Applebot, and AI crawlers (`GPTBot`, `Claude-Web`, `PerplexityBot`).
   - `/llms.txt`: Summary documentation formatted for LLM assistants.
   - `/llms-full.txt`: Full-text machine catalogue of all 310 programs with country, funding, and official portal URLs.

---

## 2. Google Search Console Audit Checklist

When auditing ScholarX in Google Search Console:

### Step 1: Property Scope & Verification
- Verify Domain Property (`scholarx.online`) via DNS TXT record or HTML meta tag (`NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION`).
- Ensure protocols (`https://`) and subdomains (`www`, apex) resolve cleanly with 301 redirects to the canonical apex or www address.

### Step 2: Indexing & Coverage Verification
- Inspect the **Pages** report:
  - Check **Crawled - Currently Not Indexed**: Confirm that high-value dossiers are not filtered out as duplicate content. The dynamic canonical and static generation prevent this.
  - Check **Discovered - Currently Not Indexed**: If high, confirm that internal links from `/catalog` are active and that the XML sitemap (`/sitemap.xml`) has been submitted and processed.
  - Check **Excluded by 'noindex' tag**: Verify that only ephemeral session routes (`/mission/[sessionId]`) and print views (`/catalog/print`, `/dossier/[id]/print`) carry `noindex`.

### Step 3: Structured Data & Rich Results
- Validate URLs using Google's **Rich Results Test**:
  - `FinancialAssistanceProgram`: Confirms scholarship provider, area served (`Pakistan`), and funding details.
  - `BreadcrumbList`: Confirms path navigation (`Home` > `Scholarship Directory` > `[Scholarship Name]`).
  - `FAQPage`: Confirms rich accordion question/answers for IELTS requirements, deadlines, and funding coverage.
  - `WebSite`: Confirms Sitelinks Search Box eligibility pointing to `/catalog?q={search_term}`.

### Step 4: Core Web Vitals (CWV)
- Largest Contentful Paint (LCP) < 2.5s: Dossier pages use static HTML rendering with 0ms server computation.
- Cumulative Layout Shift (CLS) < 0.1: Image dimensions and flag logos have fixed height/width wrappers.
- Interaction to Next Paint (INP) < 200ms: Lightweight client components with instant state updates.

---

## 3. High-Intent Keyword Matrix for Pakistan Higher Education

Target these high-volume, low-competition clusters in content, titles, and headings:

| Query Cluster | Monthly Search Intent | Primary Target URL |
| :--- | :--- | :--- |
| `scholarships for pakistani students 2026 2027` | High (National) | `/catalog` |
| `fully funded scholarships for pakistani students` | High (National) | `/catalog?funding=full` |
| `stipendium hungaricum pakistan quota` | High (Bilateral) | `/dossier/SCH-EU-001` |
| `turkiye burslari scholarship for pakistan` | High (Bilateral) | `/dossier/SCH-ME-001` |
| `chinese government scholarship csc pakistan` | High (Bilateral) | `/dossier/SCH-AS-001` |
| `daad epos scholarship germany pakistan` | Medium (Postgrad) | `/dossier/SCH-EU-002` |
| `scholarships without ielts for pakistani students` | High (Specific Intent) | `/catalog?moi=true` |
| `hec attestation for abroad scholarship` | High (Procedural) | `/dossier/[scholarshipId]` |
| `singa phd scholarship singapore pakistan` | Medium (Research) | `/dossier/SCH-AS-004` |
| `fulbright scholarship pakistan deadline` | High (Prestige) | `/dossier/SCH-AM-001` |

---

## 4. Generative Engine Optimization (GEO) & AI Citations

Modern AI engines (ChatGPT, Perplexity, Claude, Google AI Overviews) evaluate content on **direct answers, citability, and structured verification**:

1. **Exact Quotas & Figures**: State numbers clearly (e.g., *"400 reserved bilateral seats for Pakistani students"*). AI models extract explicit numerical facts.
2. **HEC & Attestation Prerequisites**: Always outline the precise verification steps (IBCC matric/inter attestation, HEC degree attestation, MOFA stamp).
3. **Official Portals**: Link directly to official government portals (`scholarship.hec.gov.pk`, `turkiyeburslari.gov.tr`, `campuschina.org`).
4. **Markdown Availability**: Keep `/llms.txt` and `/llms-full.txt` up-to-date whenever new scholarship dossiers are added to `scholarships_deep_dossiers.json`.

---

## 5. Automated Audit CLI Commands

Run these automated verification commands from the project root:

```bash
# 1. Run production build & verify all 310 pages pre-render statically
cd frontend && npm run build

# 2. Inspect generated robots.txt output
curl -s http://localhost:3000/robots.txt

# 3. Inspect generated sitemap.xml output
curl -s http://localhost:3000/sitemap.xml | head -n 30

# 4. Inspect llms.txt discovery endpoint
curl -s http://localhost:3000/llms.txt

# 5. Validate structured data in a sample dossier
curl -s http://localhost:3000/dossier/SCH-EU-001 | grep -A 20 'application/ld+json'
```
