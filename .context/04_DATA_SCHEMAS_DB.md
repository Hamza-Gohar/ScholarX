# 💾 ScholarX — Data Schemas & Storage Reference

> **Deep-dive manual for SQLite WAL tables, Pydantic models, 310 Deep Dossiers, and Pakistani benchmarks.**

---

## 1. SQLite Database Schema (`data/scholarx_sessions.db`)

Managed asynchronously via `aiosqlite` with WAL (Write-Ahead Logging) mode enabled for high-concurrency read/write operations without locking:

```sql
-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT,
    profile_json TEXT NOT NULL,  -- Serialized StudentProfile Pydantic model
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Sessions Table
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL,
    status TEXT NOT NULL,        -- 'IDLE', 'RUNNING', 'COMPLETED', 'FAILED'
    mode TEXT NOT NULL,          -- 'LIVE' or 'DEMO'
    current_stage INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 3. Scholarships Cache Table (310 Seeded Opportunities)
CREATE TABLE IF NOT EXISTS scholarships_cache (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    region TEXT NOT NULL,        -- 'Europe', 'Asia', 'Americas', 'MENA', 'Oceania'
    country TEXT NOT NULL,
    degree_levels TEXT NOT NULL, -- JSON array: ['Undergraduate', 'Master', 'PhD']
    funding_type TEXT NOT NULL,  -- 'Fully Funded', 'Partial', 'Tuition Only'
    deadline TEXT,
    verified BOOLEAN DEFAULT 1,
    raw_json TEXT NOT NULL,
    dossier_json TEXT,           -- Complete 11-dimension deep research dossier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Session Scholarships (Ranked Results)
CREATE TABLE IF NOT EXISTS session_scholarships (
    session_id TEXT NOT NULL,
    scholarship_id TEXT NOT NULL,
    composite_score REAL NOT NULL,
    rank INTEGER NOT NULL,
    eligibility_score REAL,
    funding_score REAL,
    cost_pkr REAL,
    notes TEXT,
    PRIMARY KEY (session_id, scholarship_id),
    FOREIGN KEY (session_id) REFERENCES sessions(id),
    FOREIGN KEY (scholarship_id) REFERENCES scholarships_cache(id)
);

-- 5. Events Log (Audit Trail & Replay)
CREATE TABLE IF NOT EXISTS events_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    event_type TEXT NOT NULL,    -- From AgentEventType enum
    source TEXT NOT NULL,
    severity TEXT NOT NULL,      -- 'INFO', 'WARNING', 'ERROR', 'SUCCESS', 'CHALLENGE'
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    payload_json TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Search Queries Cache (Tavily/Scout Cache)
CREATE TABLE IF NOT EXISTS search_queries_cache (
    id TEXT PRIMARY KEY,
    query_hash TEXT UNIQUE NOT NULL,
    query_text TEXT NOT NULL,
    region TEXT NOT NULL,
    results_json TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 2. 510 Deep Dossier Seed Database

ScholarX includes **510 fully researched international scholarship dossiers** (with 512 records in `scholarships_database.db`):

| Region | Count | Flagship Examples |
|:---|:---:|:---|
| **Europe** | 161 | Stipendium Hungaricum (400 HEC bilateral seats), DAAD EPOS/Helmut-Schmidt, Erasmus Mundus, Italian DSU, Swedish Institute SISGP, Swiss Government Excellence |
| **Asia** | 131 | Chinese Government CSC (Type A Bilateral & Type B University), MEXT Embassy & University Track (Japan), GKS/KGSP (South Korea), Turkiye Burslari |
| **Americas** | 105 | Fulbright Foreign Student Program (USEFP Pakistan), Global UGRAD, Vanier Canada Graduate Scholarships, OAS Academic Scholarship |
| **MENA** | 73 | KAUST Fellowship (Saudi Arabia, $30k stipend + villa), Islamic Development Bank (IsDB), Qatar University Scholarships, Khalifa University |
| **Oceania** | 40 | Australia Awards Scholarships (DFAT Pakistan priority), Melbourne Research Scholarship, Manaaki New Zealand Scholarship |

---

## 3. Standalone Database & Interactive Viewer Assets

ScholarX bundles direct export and standalone exploration tools in repository root:
- **`scholarships_database.db`**: Portable SQLite database with 512 indexed scholarships.
- **`scholarships_database.csv`**: Full tabular CSV export (170 KB) for spreadsheet and data science analysis.
- **`scholarships_database_viewer.html`**: Standalone zero-dependency HTML5/JS viewer (367 KB) featuring real-time client-side search, regional filters, and deep dossier inspection without requiring a running server.
- **`frontend/lib/db/databaseBundle.ts` & `sqliteClient.ts`**: Portable SQLite access using Node 22 built-in `node:sqlite`, supporting local dev, Next.js API routes, and Vercel serverless deployments.

---

## 3. The 11-Dimension Canonical Dossier Structure

Each seeded scholarship contains an exhaustive research payload conforming to `backend/schemas/scholarship.py`:

1. **Identity & Core Metadata**: Title, host institution, target degree levels, academic fields.
2. **Funding Breakdown**: 100% tuition coverage, monthly living stipend in local currency & PKR, airfare, medical insurance.
3. **Pakistan Bilateral Quotas**: Specific HEC reserved seats (e.g. 400 for Hungary, 200 for China), government-to-government nomination agreements.
4. **Eligibility Matrix**: Strict GPA cutoff (4.0 / percentage), age restrictions, degree prerequisites.
5. **Language Waivers**: IELTS/TOEFL requirements, Minimum bands (6.5/7.0), English Medium of Instruction (MOI) waiver validity.
6. **Out-of-Pocket Expense Waterfall (PKR)**:
   - *Pre-App*: IELTS (PKR 75.6k), passport, document attestation.
   - *App*: University portal application fees + 10% FBR advance tax.
   - *Visa & Travel*: Embassy fee, biometrics, flight tickets.
   - *Initial Settlement*: First month security deposit & groceries.
7. **Deadline Runway & Bottlenecks**: Application close date, Pakistani preparation lead times, HEC portal cutoff vs university portal cutoff.
8. **Document Attestation Readiness**: Matrix of required stamps (Matric/FSc from IBCC, Degree/Transcript from HEC, MOFA verification).
9. **Skeptic Friction Audit**: Adversarial findings (return-to-Pakistan legal bonds, blocked bank account requirements, appointment delays at VFS Gerry's).
10. **Dual-Gate Application Strategy**: Explains whether applicant applies to HEC first, university first, or both simultaneously.
11. **Official Citations**: Direct links to embassy portals, HEC announcements, and university scholarship pages.

---

## 4. Pakistan-Specific Reference Benchmarks

Stored in `data/pakistan_costs.json` and `data/pakistan_education.json`:

### Cost Benchmarks (`data/pakistan_costs.json`)
- **IELTS Academic**: PKR 75,600 (AEO / British Council standard)
- **HEC Degree Attestation**: PKR 1,000 per original document, PKR 500 per copy
- **IBCC Certificate Equivalence**: PKR 7,500 (O/A Level equivalence)
- **Passport Renewal (36 pages, urgent)**: PKR 5,500
- **Medical Fitness Examination (GAMCA/Authorized)**: PKR 15,000 - 25,000
- **FBR Section 236Y Advance Tax**: 10% on foreign card remittances (for non-filers)

### Educational Benchmarks (`data/pakistan_education.json`)
- **Grading Systems**: Conversion formulas between BISE percentage (e.g. 70%+ First Division), HEC CGPA (4.0 scale), and UK Honours (1st Class, 2:1, 2:2).
- **Cambridge Equivalence**: IBCC mathematical reduction formula (e.g. A* = 90, A = 85, B = 75, C = 65).
