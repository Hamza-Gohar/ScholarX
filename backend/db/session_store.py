import asyncio
from contextlib import asynccontextmanager
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import difflib
import re
import aiosqlite
from config import get_settings
from schemas.scholarship import Scholarship
from schemas.scoring import CompositeScoreResult
from schemas.session import SessionDetail, SessionStatus, SessionSummary
from schemas.student import StudentProfile
from schemas.search import PersonalizedMatch

logger = logging.getLogger("scholarx.db")


class SessionStore:
    def __init__(self, db_path: Optional[str] = None):
        settings = get_settings()
        self.db_path = db_path or settings.SESSION_DB_PATH
        if self.db_path not in (":memory:", "memory") and not self.db_path.startswith("file:"):
            try:
                Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                logger.warning(f"Could not create database directory for {self.db_path}: {e}. Switching to in-memory mode.")
                self.db_path = ":memory:"
        self._mem_anchor: Optional[aiosqlite.Connection] = None
        self._anchor_loop = None
        self._init_lock: Optional[asyncio.Lock] = None
        self._init_loop = None
        self._write_lock: Optional[asyncio.Lock] = None
        self._write_loop = None
        self._event_queue: Optional[asyncio.Queue] = None
        self._queue_loop = None
        self._flusher_task: Optional[asyncio.Task] = None
        self._is_initialized = False
        self._using_memory_fallback = self.db_path in (":memory:", "memory") or self.db_path.startswith("file:")

    def _get_write_lock(self) -> asyncio.Lock:
        """Returns the write lock bound to the current running event loop."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None
        if self._write_lock is None or self._write_loop != loop:
            self._write_lock = asyncio.Lock()
            self._write_loop = loop
        return self._write_lock

    def _get_init_lock(self) -> asyncio.Lock:
        """Returns the initialization lock bound to the current running event loop."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None
        if self._init_lock is None or self._init_loop != loop:
            self._init_lock = asyncio.Lock()
            self._init_loop = loop
        return self._init_lock

    def _get_event_queue(self) -> asyncio.Queue:
        """Returns the event queue bound to the current running event loop."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None
        if self._event_queue is None or self._queue_loop != loop:
            self._event_queue = asyncio.Queue()
            self._queue_loop = loop
            self._flusher_task = None
        return self._event_queue

    @asynccontextmanager
    async def _get_connection(self):
        """Yields an aiosqlite connection with generous timeout, WAL journal, and busy timeout configured."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if self._mem_anchor is not None and getattr(self, "_anchor_loop", None) != loop:
            try:
                await self._mem_anchor.close()
            except Exception:
                pass
            self._mem_anchor = None
            self._anchor_loop = None

        if self.db_path in (":memory:", "memory") or self.db_path.startswith("file:"):
            uri = "file:scholarx_mem_db?mode=memory&cache=shared"
            if self._mem_anchor is None:
                self._mem_anchor = await aiosqlite.connect(uri, uri=True)
                self._anchor_loop = loop
            async with aiosqlite.connect(uri, uri=True) as db:
                await db.execute("PRAGMA foreign_keys=ON;")
                yield db
        else:
            try:
                db = await aiosqlite.connect(self.db_path, timeout=60.0)
                await db.execute("PRAGMA foreign_keys=ON;")
                await db.execute("PRAGMA journal_mode=WAL;")
                await db.execute("PRAGMA synchronous=NORMAL;")
                await db.execute("PRAGMA busy_timeout=60000;")
            except Exception as conn_err:
                if get_settings().ENVIRONMENT.lower() == "production":
                    raise RuntimeError(f"Persistent database is unavailable in production: {self.db_path}") from conn_err
                logger.warning(f"Failed to connect to disk database {self.db_path}: {conn_err}. Falling back to in-memory shared database.")
                self._using_memory_fallback = True
                uri = "file:scholarx_mem_db?mode=memory&cache=shared"
                if self._mem_anchor is None:
                    self._mem_anchor = await aiosqlite.connect(uri, uri=True)
                    self._anchor_loop = loop
                db = await aiosqlite.connect(uri, uri=True)
                await db.execute("PRAGMA foreign_keys=ON;")
            try:
                yield db
            finally:
                await db.close()

    async def _flush_events_worker(self):
        """Background worker that flushes queued event logs in batches under the write lock."""
        q = self._get_event_queue()
        while True:
            batch = []
            try:
                item = await q.get()
                batch = [item]
                while len(batch) < 100:
                    try:
                        batch.append(q.get_nowait())
                    except asyncio.QueueEmpty:
                        break

                async with self._get_write_lock():
                    async with self._get_connection() as db:
                        await db.executemany(
                            """
                            INSERT INTO events_log (event_id, session_id, timestamp, event_type, agent_id, payload_json, severity)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            ON CONFLICT(event_id) DO NOTHING;
                            """,
                            batch,
                        )
                        await db.commit()

                for _ in batch:
                    q.task_done()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.debug(f"Event batch flusher notice: {e}")
                for queued_item in batch:
                    q.task_done()
                    try:
                        q.put_nowait(queued_item)
                    except asyncio.QueueFull:
                        logger.error("Event queue full while requeueing a failed event batch")
                await asyncio.sleep(0.05)

    async def init_db(self):
        """Creates tables if they do not already exist."""
        async with self._get_init_lock():
            self._get_event_queue()
            if self._flusher_task is None or self._flusher_task.done():
                self._flusher_task = asyncio.create_task(self._flush_events_worker())

            if self._is_initialized:
                return

            async with self._get_connection() as db:

                # 1. Students table
                await db.execute(
                    """
                    CREATE TABLE IF NOT EXISTS students (
                        student_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        profile_json TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    );
                    """
                )

                # 2. Sessions table
                await db.execute(
                    """
                    CREATE TABLE IF NOT EXISTS sessions (
                        session_id TEXT PRIMARY KEY,
                        student_id TEXT NOT NULL,
                        mission_params_json TEXT NOT NULL,
                        status TEXT NOT NULL,
                        total_scanned INTEGER DEFAULT 0,
                        total_verified INTEGER DEFAULT 0,
                        top_scholarship TEXT,
                        top_score REAL,
                        created_at TEXT NOT NULL,
                        completed_at TEXT,
                        FOREIGN KEY(student_id) REFERENCES students(student_id)
                    );
                    """
                )

                # 3. Scholarships cache table
                # 3. Scholarships cache table with full relational columns
                await db.execute(
                    """
                    CREATE TABLE IF NOT EXISTS scholarships_cache (
                        scholarship_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        country TEXT NOT NULL,
                        region TEXT NOT NULL,
                        host_country_name TEXT,
                        host_institution TEXT,
                        funding_type TEXT,
                        degree_levels TEXT,
                        min_gpa_4_scale REAL,
                        min_gpa_percentage REAL,
                        ielts_minimum REAL,
                        monthly_stipend TEXT,
                        monthly_stipend_pkr_approx INTEGER,
                        pakistan_eligible INTEGER DEFAULT 1,
                        pakistan_bilateral_quota INTEGER DEFAULT 0,
                        pakistan_quota_seats INTEGER,
                        hec_managed INTEGER DEFAULT 0,
                        hec_attestation_required INTEGER DEFAULT 1,
                        accepts_moi_certificate INTEGER DEFAULT 0,
                        application_deadline TEXT,
                        application_opens TEXT,
                        source_url TEXT,
                        portal_url TEXT,
                        competition_level TEXT,
                        success_rate_pakistan_percent REAL,
                        description TEXT,
                        data_json TEXT NOT NULL,
                        discovered_at TEXT NOT NULL,
                        verified_at TEXT,
                        ttl_seconds INTEGER DEFAULT 604800,
                        source_urls_json TEXT
                    );
                    """
                )

                # Migration for existing tables: dynamically add any missing relational columns
                cur = await db.execute("PRAGMA table_info(scholarships_cache);")
                existing_cols = {row[1] if isinstance(row, (tuple, list)) else row["name"] for row in await cur.fetchall()}
                relational_cols = [
                    ("host_country_name", "TEXT"),
                    ("host_institution", "TEXT"),
                    ("funding_type", "TEXT"),
                    ("degree_levels", "TEXT"),
                    ("min_gpa_4_scale", "REAL"),
                    ("min_gpa_percentage", "REAL"),
                    ("ielts_minimum", "REAL"),
                    ("monthly_stipend", "TEXT"),
                    ("monthly_stipend_pkr_approx", "INTEGER"),
                    ("pakistan_eligible", "INTEGER DEFAULT 1"),
                    ("pakistan_bilateral_quota", "INTEGER DEFAULT 0"),
                    ("pakistan_quota_seats", "INTEGER"),
                    ("hec_managed", "INTEGER DEFAULT 0"),
                    ("hec_attestation_required", "INTEGER DEFAULT 1"),
                    ("accepts_moi_certificate", "INTEGER DEFAULT 0"),
                    ("application_deadline", "TEXT"),
                    ("application_opens", "TEXT"),
                    ("source_url", "TEXT"),
                    ("portal_url", "TEXT"),
                    ("competition_level", "TEXT"),
                    ("success_rate_pakistan_percent", "REAL"),
                    ("description", "TEXT"),
                ]
                for col_name, col_type in relational_cols:
                    if col_name not in existing_cols:
                        try:
                            await db.execute(f"ALTER TABLE scholarships_cache ADD COLUMN {col_name} {col_type};")
                        except Exception as e:
                            logger.debug(f"Column {col_name} alter notice: {e}")

                # 4. Session Scholarships junction table
                await db.execute(
                    """
                    CREATE TABLE IF NOT EXISTS session_scholarships (
                        session_id TEXT NOT NULL,
                        scholarship_id TEXT NOT NULL,
                        eligibility_json TEXT,
                        cost_json TEXT,
                        deadline_json TEXT,
                        verification_json TEXT,
                        skeptic_json TEXT,
                        final_score REAL,
                        rank INTEGER,
                        PRIMARY KEY(session_id, scholarship_id),
                        FOREIGN KEY(session_id) REFERENCES sessions(session_id),
                        FOREIGN KEY(scholarship_id) REFERENCES scholarships_cache(scholarship_id)
                    );
                    """
                )

                # 5. Events Log table
                await db.execute(
                    """
                    CREATE TABLE IF NOT EXISTS events_log (
                        event_id TEXT PRIMARY KEY,
                        session_id TEXT NOT NULL,
                        timestamp TEXT NOT NULL,
                        event_type TEXT NOT NULL,
                        agent_id TEXT NOT NULL,
                        payload_json TEXT NOT NULL,
                        severity TEXT DEFAULT 'INFO',
                        FOREIGN KEY(session_id) REFERENCES sessions(session_id)
                    );
                    """
                )

                # 6. Search queries cache
                await db.execute(
                    """
                    CREATE TABLE IF NOT EXISTS search_queries_cache (
                        query_text TEXT PRIMARY KEY,
                        region TEXT NOT NULL,
                        results_count INTEGER DEFAULT 0,
                        last_used TEXT NOT NULL,
                        success_rate REAL DEFAULT 1.0
                    );
                    """
                )

                # Relational Indexes for sub-millisecond retrieval
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_region ON scholarships_cache(region);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_country ON scholarships_cache(country);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_name ON scholarships_cache(name);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_funding ON scholarships_cache(funding_type);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_deadline ON scholarships_cache(application_deadline);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_moi ON scholarships_cache(accepts_moi_certificate);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_hec ON scholarships_cache(hec_managed);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_quota ON scholarships_cache(pakistan_bilateral_quota);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_scholarships_stipend ON scholarships_cache(monthly_stipend_pkr_approx);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_session_scholarships_session ON session_scholarships(session_id);")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_events_session ON events_log(session_id);")

                # Canonical Relational View for direct SQL tools and database inspectors
                await db.execute(
                    """
                    CREATE VIEW IF NOT EXISTS scholarships AS
                    SELECT 
                        scholarship_id,
                        name,
                        country AS host_country,
                        COALESCE(host_country_name, country) AS host_country_name,
                        host_institution,
                        region,
                        funding_type,
                        degree_levels,
                        min_gpa_4_scale,
                        min_gpa_percentage,
                        ielts_minimum,
                        monthly_stipend,
                        monthly_stipend_pkr_approx,
                        pakistan_eligible,
                        pakistan_bilateral_quota,
                        pakistan_quota_seats,
                        hec_managed,
                        hec_attestation_required,
                        accepts_moi_certificate,
                        application_deadline,
                        application_opens,
                        source_url,
                        portal_url,
                        competition_level,
                        success_rate_pakistan_percent,
                        description,
                        discovered_at,
                        verified_at,
                        data_json
                    FROM scholarships_cache;
                    """
                )

                await db.commit()
                self._is_initialized = True
                logger.info(f"SQLite relational database initialized at {self.db_path}")

    async def save_student_profile(self, profile: StudentProfile):
        await self.init_db()
        now = datetime.now(timezone.utc).isoformat()
        async with self._get_write_lock():
            async with self._get_connection() as db:
                await db.execute(
                    """
                    INSERT INTO students (student_id, name, profile_json, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(student_id) DO UPDATE SET
                        name=excluded.name,
                        profile_json=excluded.profile_json,
                        updated_at=excluded.updated_at;
                    """,
                    (profile.student_id, profile.personal.name, profile.model_dump_json(), now, now),
                )
                await db.commit()

    async def get_student_profile(self, identifier: str) -> Optional[StudentProfile]:
        """Retrieves a StudentProfile by student_id or by active session_id."""
        await self.init_db()
        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            # Try by student_id
            cursor = await db.execute("SELECT profile_json FROM students WHERE student_id = ?;", (identifier,))
            row = await cursor.fetchone()
            if row:
                return StudentProfile.model_validate_json(row["profile_json"])

            # Try by session_id
            cursor = await db.execute(
                """
                SELECT st.profile_json 
                FROM sessions s
                JOIN students st ON s.student_id = st.student_id
                WHERE s.session_id = ?;
                """,
                (identifier,)
            )
            session_row = await cursor.fetchone()
            if session_row:
                return StudentProfile.model_validate_json(session_row["profile_json"])

            # 3. Try json_extract on profile_json in students table
            cursor = await db.execute(
                "SELECT profile_json FROM students WHERE json_extract(profile_json, '$.session_id') = ?;",
                (identifier,)
            )
            json_row = await cursor.fetchone()
            if json_row:
                return StudentProfile.model_validate_json(json_row["profile_json"])

        return None

    async def create_session(
        self,
        session_id: str,
        student_id: str,
        mission_params: Optional[Dict[str, Any]] = None,
    ) -> str:
        await self.init_db()
        now = datetime.now(timezone.utc).isoformat()
        params_json = json.dumps(mission_params or {})
        async with self._get_write_lock():
            async with self._get_connection() as db:
                await db.execute(
                    """
                    INSERT INTO sessions (session_id, student_id, mission_params_json, status, created_at)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(session_id) DO UPDATE SET
                        status=excluded.status;
                    """,
                    (session_id, student_id, params_json, SessionStatus.INITIATED.value, now),
                )
                await db.commit()
        return session_id

    async def list_sessions(self, limit: int = 50) -> List[SessionSummary]:
        await self.init_db()
        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT s.session_id, s.student_id, st.name as student_name,
                       st.profile_json, s.status, s.total_scanned, s.total_verified,
                       s.top_scholarship, s.top_score, s.created_at, s.completed_at
                FROM sessions s
                JOIN students st ON s.student_id = st.student_id
                ORDER BY s.created_at DESC
                LIMIT ?;
                """,
                (limit,),
            )
            rows = await cursor.fetchall()
            results = []
            for row in rows:
                profile_dict = json.loads(row["profile_json"])
                target_degree = profile_dict.get("preferences", {}).get("target_degree_level", "Bachelor's")
                results.append(
                    SessionSummary(
                        session_id=row["session_id"],
                        student_id=row["student_id"],
                        student_name=row["student_name"],
                        target_degree=target_degree,
                        created_at=row["created_at"],
                        completed_at=row["completed_at"],
                        total_scanned=row["total_scanned"] or 0,
                        total_verified=row["total_verified"] or 0,
                        top_scholarship_name=row["top_scholarship"],
                        top_match_score=row["top_score"],
                        status=SessionStatus(row["status"]),
                    )
                )
            return results

    async def get_session_detail(self, session_id: str) -> Optional[SessionDetail]:
        await self.init_db()
        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT s.session_id, s.student_id, s.mission_params_json, s.status,
                       s.total_scanned, s.total_verified, s.created_at, s.completed_at,
                       st.profile_json
                FROM sessions s
                JOIN students st ON s.student_id = st.student_id
                WHERE s.session_id = ?;
                """,
                (session_id,),
            )
            session_row = await cursor.fetchone()
            if not session_row:
                return None

            profile = StudentProfile.model_validate_json(session_row["profile_json"])
            mission_params = json.loads(session_row["mission_params_json"])

            from workflows.degree_matching import get_degree_scholarship_limit
            target_deg = profile.preferences.target_degree_level if profile.preferences else None
            output_limit = get_degree_scholarship_limit(target_deg)

            # Load joined scholarships (only those with composite score > 50, capped by degree level)
            sc_cursor = await db.execute(
                """
                SELECT sc.data_json, ss.final_score, ss.rank, ss.eligibility_json, ss.cost_json, ss.deadline_json
                FROM session_scholarships ss
                JOIN scholarships_cache sc ON ss.scholarship_id = sc.scholarship_id
                WHERE ss.session_id = ? AND ss.final_score > 50.0
                ORDER BY ss.rank ASC
                LIMIT ?;
                """,
                (session_id, output_limit),
            )
            sc_rows = await sc_cursor.fetchall()
            scholarships = []
            for r in sc_rows:
                s = Scholarship.model_validate_json(r["data_json"])
                s.final_score = r["final_score"]
                s.rank = r["rank"]
                if r["eligibility_json"]:
                    try:
                        s.eligibility_analysis = json.loads(r["eligibility_json"])
                    except Exception:
                        pass
                if r["cost_json"]:
                    try:
                        s.cost_analysis = json.loads(r["cost_json"])
                    except Exception:
                        pass
                if r["deadline_json"]:
                    try:
                        s.deadline_analysis = json.loads(r["deadline_json"])
                    except Exception:
                        pass
                scholarships.append(s)

            return SessionDetail(
                session_id=session_row["session_id"],
                student_id=session_row["student_id"],
                student_profile=profile,
                mission_parameters=mission_params,
                status=SessionStatus(session_row["status"]),
                created_at=session_row["created_at"],
                completed_at=session_row["completed_at"],
                total_scanned=session_row["total_scanned"] or 0,
                total_verified=session_row["total_verified"] or 0,
                discovered_scholarships=scholarships,
            )

    @staticmethod
    def _extract_relational_row(s: Scholarship, now: str):
        degs = s.eligibility.degree_levels if s.eligibility else []
        deg_str = ", ".join(degs) if isinstance(degs, list) else str(degs or "")

        gpa_4 = s.eligibility.min_gpa_4_scale if s.eligibility else None
        gpa_pct = s.eligibility.min_gpa_percentage if s.eligibility else None
        ielts = s.language.minimum_ielts if s.language else None

        funding_val = s.funding.funding_type.value if hasattr(s.funding.funding_type, "value") else str(s.funding.funding_type)
        stipend = s.funding.monthly_stipend if s.funding else None
        stipend_pkr = s.funding.monthly_stipend_pkr_approx if s.funding else None

        pk_req = s.pakistan_requirements
        pk_eligible = 1 if (pk_req and pk_req.pakistan_eligible is not False) else 0
        pk_quota = 1 if (pk_req and pk_req.pakistan_bilateral_quota) else 0
        pk_seats = pk_req.pakistan_quota_seats if pk_req else None
        hec_managed = 1 if (pk_req and pk_req.hec_managed) else 0
        hec_attest = 1 if (pk_req and pk_req.hec_attestation_required is not False) else 0
        moi_accept = 1 if (pk_req and pk_req.accepts_moi_certificate) else 0

        # Augment with deep_dossier if available
        if s.deep_dossier and getattr(s.deep_dossier, "eligibility_requirements", None):
            el = s.deep_dossier.eligibility_requirements
            if not moi_accept and getattr(el, "moi_certificate_accepted", False):
                moi_accept = 1
            if ielts is None and getattr(el, "ielts_minimum", None):
                ielts = el.ielts_minimum
            if gpa_4 is None and getattr(el, "minimum_gpa_scale", None):
                gpa_4 = el.minimum_gpa_scale
            if gpa_pct is None and getattr(el, "minimum_gpa_percentage", None):
                gpa_pct = el.minimum_gpa_percentage

        comp_val = s.competition_level.value if hasattr(s.competition_level, "value") else str(s.competition_level or "MODERATE")
        status_val = s.status.value if hasattr(s.status, "value") else str(s.status)

        return (
            s.scholarship_id,
            s.name,
            s.host_country,
            s.region,
            s.host_country_name or s.host_country,
            s.host_institution,
            funding_val,
            deg_str,
            gpa_4,
            gpa_pct,
            ielts,
            stipend,
            stipend_pkr,
            pk_eligible,
            pk_quota,
            pk_seats,
            hec_managed,
            hec_attest,
            moi_accept,
            s.application_deadline,
            s.application_opens,
            s.source_url,
            s.portal_url,
            comp_val,
            s.success_rate_pakistan_percent,
            s.description,
            s.model_dump_json(),
            now,
            now if status_val == "VERIFIED" else None,
            json.dumps([s.source_url]),
        )

    async def bulk_upsert_scholarships_cache(self, scholarships: List[Scholarship]):
        """Upserts a batch of scholarships into cache inside a single transaction and write lock."""
        if not scholarships:
            return
        await self.init_db()
        now = datetime.now(timezone.utc).isoformat()
        rows = [self._extract_relational_row(s, now) for s in scholarships]
        async with self._get_write_lock():
            async with self._get_connection() as db:
                await db.executemany(
                    """
                    INSERT INTO scholarships_cache (
                        scholarship_id, name, country, region, host_country_name, host_institution,
                        funding_type, degree_levels, min_gpa_4_scale, min_gpa_percentage, ielts_minimum,
                        monthly_stipend, monthly_stipend_pkr_approx, pakistan_eligible, pakistan_bilateral_quota,
                        pakistan_quota_seats, hec_managed, hec_attestation_required, accepts_moi_certificate,
                        application_deadline, application_opens, source_url, portal_url, competition_level,
                        success_rate_pakistan_percent, description, data_json, discovered_at, verified_at,
                        source_urls_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(scholarship_id) DO UPDATE SET
                        name=excluded.name,
                        country=excluded.country,
                        region=excluded.region,
                        host_country_name=excluded.host_country_name,
                        host_institution=excluded.host_institution,
                        funding_type=excluded.funding_type,
                        degree_levels=excluded.degree_levels,
                        min_gpa_4_scale=excluded.min_gpa_4_scale,
                        min_gpa_percentage=excluded.min_gpa_percentage,
                        ielts_minimum=excluded.ielts_minimum,
                        monthly_stipend=excluded.monthly_stipend,
                        monthly_stipend_pkr_approx=excluded.monthly_stipend_pkr_approx,
                        pakistan_eligible=excluded.pakistan_eligible,
                        pakistan_bilateral_quota=excluded.pakistan_bilateral_quota,
                        pakistan_quota_seats=excluded.pakistan_quota_seats,
                        hec_managed=excluded.hec_managed,
                        hec_attestation_required=excluded.hec_attestation_required,
                        accepts_moi_certificate=excluded.accepts_moi_certificate,
                        application_deadline=excluded.application_deadline,
                        application_opens=excluded.application_opens,
                        source_url=excluded.source_url,
                        portal_url=excluded.portal_url,
                        competition_level=excluded.competition_level,
                        success_rate_pakistan_percent=excluded.success_rate_pakistan_percent,
                        description=excluded.description,
                        data_json=excluded.data_json,
                        verified_at=excluded.verified_at,
                        source_urls_json=excluded.source_urls_json;
                    """,
                    rows,
                )
                await db.commit()

    async def upsert_scholarship_cache(self, scholarship: Scholarship):
        await self.bulk_upsert_scholarships_cache([scholarship])

    async def get_all_cached_scholarships(self) -> List[Scholarship]:
        await self.init_db()
        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT data_json FROM scholarships_cache;")
            rows = await cursor.fetchall()
            return [Scholarship.model_validate_json(r["data_json"]) for r in rows]

    async def delete_scholarship_from_cache(self, scholarship_id: str) -> bool:
        """Deletes a single scholarship and its session associations from cache."""
        await self.init_db()
        async with self._get_write_lock():
            async with self._get_connection() as db:
                await db.execute("DELETE FROM session_scholarships WHERE scholarship_id = ?;", (scholarship_id,))
                cursor = await db.execute("DELETE FROM scholarships_cache WHERE scholarship_id = ?;", (scholarship_id,))
                await db.commit()
                return cursor.rowcount > 0

    async def purge_unverified_or_outdated_scholarships(self, allowed_scholarship_ids: List[str]) -> int:
        """Purges any cached scholarships not in the provided allowed list, ensuring only verified scholarships remain."""
        await self.init_db()
        if not allowed_scholarship_ids:
            return 0
        async with self._get_write_lock():
            async with self._get_connection() as db:
                placeholders = ",".join(["?"] * len(allowed_scholarship_ids))
                await db.execute(
                    f"DELETE FROM session_scholarships WHERE scholarship_id NOT IN ({placeholders});",
                    allowed_scholarship_ids,
                )
                cursor = await db.execute(
                    f"DELETE FROM scholarships_cache WHERE scholarship_id NOT IN ({placeholders});",
                    allowed_scholarship_ids,
                )
                deleted_count = cursor.rowcount
                await db.commit()
                return deleted_count

    async def enqueue_event_log(
        self,
        event_id: str,
        session_id: str,
        event_type: str,
        agent_id: str,
        payload: Dict[str, Any],
        severity: str = "INFO",
    ):
        """Enqueues an event log entry for asynchronous batched persistence without blocking."""
        try:
            await self.init_db()
            now = datetime.now(timezone.utc).isoformat()
            payload_str = json.dumps(payload)
            self._event_queue.put_nowait((event_id, session_id, now, event_type, agent_id, payload_str, severity))
        except Exception as e:
            logger.debug(f"Event enqueue notice: {e}")

    async def log_event(
        self,
        event_id: str,
        session_id: str,
        event_type: str,
        agent_id: str,
        payload: Dict[str, Any],
        severity: str = "INFO",
    ):
        await self.enqueue_event_log(event_id, session_id, event_type, agent_id, payload, severity)

    async def save_ranked_results(self, session_id: str, ranked_results: List[CompositeScoreResult]):
        await self.init_db()
        qualified_results = [r for r in ranked_results if r.overall_match_score > 50.0]
        
        # Enforce degree-specific cap if profile is available
        profile = await self.get_student_profile(session_id)
        from workflows.degree_matching import get_degree_scholarship_limit
        target_deg = profile.preferences.target_degree_level if profile and profile.preferences else None
        output_limit = get_degree_scholarship_limit(target_deg)
        if len(qualified_results) > output_limit:
            qualified_results = qualified_results[:output_limit]
        async with self._get_write_lock():
            async with self._get_connection() as db:
                for item in qualified_results:
                    await db.execute(
                        """
                        INSERT INTO session_scholarships (
                            session_id, scholarship_id, final_score, rank, eligibility_json, cost_json, deadline_json
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(session_id, scholarship_id) DO UPDATE SET
                            final_score=excluded.final_score,
                            rank=excluded.rank,
                            cost_json=excluded.cost_json,
                            deadline_json=excluded.deadline_json;
                        """,
                        (
                            session_id,
                            item.scholarship_id,
                            item.overall_match_score,
                            item.rank,
                            json.dumps({"score": item.eligibility_score, "advantages": item.pakistan_specific_advantages}),
                            item.cost_analysis.model_dump_json() if item.cost_analysis else None,
                            item.deadline_analysis.model_dump_json() if item.deadline_analysis else None,
                        ),
                    )
                
                # Update sessions table completion status
                top_name = qualified_results[0].scholarship_name if qualified_results else "None Qualifying"
                top_score = qualified_results[0].overall_match_score if qualified_results else 0.0
                await db.execute(
                    """
                    UPDATE sessions SET
                        top_scholarship = ?,
                        top_score = ?,
                        total_verified = ?,
                        status = 'COMPLETED',
                        completed_at = ?
                    WHERE session_id = ?;
                    """,
                    (
                        top_name,
                        top_score,
                        len(qualified_results),
                        datetime.now(timezone.utc).isoformat(),
                        session_id,
                    ),
                )
                await db.commit()

    async def save_roadmap(self, session_id: str, roadmap: Any):
        await self.init_db()
        roadmap_json = roadmap.model_dump_json() if hasattr(roadmap, "model_dump_json") else json.dumps(roadmap)
        async with self._get_write_lock():
            async with self._get_connection() as db:
                await db.execute(
                    """
                    UPDATE sessions SET
                        mission_params_json = json_set(COALESCE(NULLIF(mission_params_json, ''), '{}'), '$.roadmap', json(?))
                    WHERE session_id = ?;
                    """,
                    (roadmap_json, session_id),
                )
                await db.commit()

    async def delete_session(self, session_id: str):
        await self.init_db()
        async with self._get_write_lock():
            async with self._get_connection() as db:
                await db.execute("DELETE FROM session_scholarships WHERE session_id = ?;", (session_id,))
                await db.execute("DELETE FROM events_log WHERE session_id = ?;", (session_id,))
                await db.execute("DELETE FROM sessions WHERE session_id = ?;", (session_id,))
                await db.commit()

    async def get_scholarship_by_id(self, scholarship_id: str) -> Optional[Scholarship]:
        await self.init_db()
        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT data_json FROM scholarships_cache WHERE LOWER(scholarship_id) = LOWER(?);",
                (scholarship_id.strip(),)
            )
            row = await cursor.fetchone()
            if row:
                return Scholarship.model_validate_json(row["data_json"])
        return None

    async def query_scholarships(
        self,
        region: Optional[str] = None,
        country: Optional[str] = None,
        search: Optional[str] = None,
        degree_level: Optional[str] = None,
        funding_type: Optional[str] = None,
        hec_only: Optional[bool] = None,
        moi_only: Optional[bool] = None,
        min_stipend_pkr: Optional[int] = None,
        sort_by: Optional[str] = "name",
        sort_order: Optional[str] = "asc",
        limit: int = 50,
        offset: int = 0,
    ) -> tuple[List[Scholarship], int]:
        await self.init_db()
        query = "SELECT data_json FROM scholarships_cache WHERE 1=1"
        count_query = "SELECT COUNT(*) as cnt FROM scholarships_cache WHERE 1=1"
        params: List[Any] = []

        if region:
            query += " AND LOWER(region) = LOWER(?)"
            count_query += " AND LOWER(region) = LOWER(?)"
            params.append(region.strip())

        if country:
            query += " AND (LOWER(country) = LOWER(?) OR LOWER(COALESCE(host_country_name, country)) LIKE LOWER(?))"
            count_query += " AND (LOWER(country) = LOWER(?) OR LOWER(COALESCE(host_country_name, country)) LIKE LOWER(?))"
            params.extend([country.strip(), f"%{country.strip()}%"])

        if search:
            term = f"%{search.strip()}%"
            query += " AND (LOWER(name) LIKE LOWER(?) OR LOWER(COALESCE(host_institution, '')) LIKE LOWER(?) OR LOWER(COALESCE(description, '')) LIKE LOWER(?) OR LOWER(scholarship_id) LIKE LOWER(?) OR LOWER(data_json) LIKE LOWER(?))"
            count_query += " AND (LOWER(name) LIKE LOWER(?) OR LOWER(COALESCE(host_institution, '')) LIKE LOWER(?) OR LOWER(COALESCE(description, '')) LIKE LOWER(?) OR LOWER(scholarship_id) LIKE LOWER(?) OR LOWER(data_json) LIKE LOWER(?))"
            params.extend([term, term, term, term, term])

        if degree_level:
            deg = f"%{degree_level.strip()}%"
            query += " AND (LOWER(COALESCE(degree_levels, '')) LIKE LOWER(?) OR LOWER(data_json) LIKE LOWER(?))"
            count_query += " AND (LOWER(COALESCE(degree_levels, '')) LIKE LOWER(?) OR LOWER(data_json) LIKE LOWER(?))"
            params.extend([deg, deg])

        if funding_type:
            ft = funding_type.strip()
            query += " AND (LOWER(COALESCE(funding_type, '')) = LOWER(?) OR LOWER(json_extract(data_json, '$.funding.funding_type')) = LOWER(?))"
            count_query += " AND (LOWER(COALESCE(funding_type, '')) = LOWER(?) OR LOWER(json_extract(data_json, '$.funding.funding_type')) = LOWER(?))"
            params.extend([ft, ft])

        if hec_only:
            query += " AND (hec_managed = 1 OR pakistan_bilateral_quota = 1)"
            count_query += " AND (hec_managed = 1 OR pakistan_bilateral_quota = 1)"

        if moi_only:
            query += " AND accepts_moi_certificate = 1"
            count_query += " AND accepts_moi_certificate = 1"

        if min_stipend_pkr is not None:
            query += " AND monthly_stipend_pkr_approx >= ?"
            count_query += " AND monthly_stipend_pkr_approx >= ?"
            params.append(min_stipend_pkr)

        col_map = {
            "name": "name",
            "country": "country",
            "deadline": "application_deadline",
            "stipend_pkr": "monthly_stipend_pkr_approx",
            "min_gpa": "min_gpa_4_scale",
            "scholarship_id": "scholarship_id",
            "region": "region",
            "funding_type": "funding_type",
        }
        sort_col = col_map.get((sort_by or "name").lower(), "name")
        direction = "DESC" if (sort_order or "asc").lower() == "desc" else "ASC"
        query += f" ORDER BY {sort_col} {direction} NULLS LAST LIMIT ? OFFSET ?"
        exec_params = list(params) + [limit, offset]

        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            count_cursor = await db.execute(count_query, params)
            count_row = await count_cursor.fetchone()
            total = count_row["cnt"] if count_row else 0

            cursor = await db.execute(query, exec_params)
            rows = await cursor.fetchall()
            scholarships = [Scholarship.model_validate_json(r["data_json"]) for r in rows]

            # Typo-tolerant offline search fallback: if exact search returned 0 results
            if total == 0 and search and search.strip():
                clean_s = search.strip().lower()
                tokens = [t for t in re.findall(r"[a-z0-9]+", clean_s) if len(t) >= 3]
                from workflows.field_matching import FAST_ACADEMIC_TYPO_DICT
                dict_matches = []
                if clean_s in FAST_ACADEMIC_TYPO_DICT:
                    dict_matches.extend(FAST_ACADEMIC_TYPO_DICT[clean_s].split())
                for t in tokens:
                    if t in FAST_ACADEMIC_TYPO_DICT:
                        dict_matches.extend(FAST_ACADEMIC_TYPO_DICT[t].split())

                known_entities = [
                    "fulbright", "chevening", "daad", "turkiye", "stipendium", "hungaricum",
                    "erasmus", "commonwealth", "mext", "vanier", "gates", "csc", "china",
                    "germany", "italy", "dsu", "romania", "qatar", "singapore", "australia",
                    "computer", "science", "engineering", "software", "artificial", "intelligence",
                    "electrical", "mechanical", "civil", "business", "finance", "economics",
                    "medicine", "biomedical", "mathematics", "physics", "chemistry", "biology"
                ]
                fuzzy_tokens = []
                for t in tokens:
                    matches = difflib.get_close_matches(t, known_entities, n=1, cutoff=0.70)
                    if matches:
                        fuzzy_tokens.append(matches[0])

                candidates = list(dict.fromkeys(tokens + dict_matches + fuzzy_tokens))
                if candidates:
                    fb_query = "SELECT data_json FROM scholarships_cache WHERE 1=1"
                    fb_count_query = "SELECT COUNT(*) as cnt FROM scholarships_cache WHERE 1=1"
                    fb_conds = []
                    fb_params = []
                    for c in candidates:
                        term = f"%{c}%"
                        fb_conds.append("(LOWER(name) LIKE LOWER(?) OR LOWER(COALESCE(host_institution, '')) LIKE LOWER(?) OR LOWER(COALESCE(description, '')) LIKE LOWER(?) OR LOWER(data_json) LIKE LOWER(?))")
                        fb_params.extend([term, term, term, term])

                    fb_clause = f" AND ({' OR '.join(fb_conds)})"
                    fb_query += fb_clause + f" ORDER BY {sort_col} {direction} NULLS LAST LIMIT ? OFFSET ?"
                    fb_count_query += fb_clause

                    fb_count_cursor = await db.execute(fb_count_query, fb_params)
                    fb_count_row = await fb_count_cursor.fetchone()
                    fb_total = fb_count_row["cnt"] if fb_count_row else 0

                    if fb_total > 0:
                        fb_cursor = await db.execute(fb_query, fb_params + [limit, offset])
                        fb_rows = await fb_cursor.fetchall()
                        return [Scholarship.model_validate_json(r["data_json"]) for r in fb_rows], fb_total

            return scholarships, total

    async def search_scholarships_for_profile(
        self,
        student: StudentProfile,
        regions: Optional[List[str]] = None,
        limit: int = 30,
    ) -> List[Scholarship]:
        """
        Queries the database for scholarships matching a student's profile based on:
        - Strict target degree level compatibility
        - Pakistan bilateral eligibility
        - Regional preferences
        - Field-of-study & discipline taxonomy alignment
        - GPA requirements and academic cutoff
        - English proficiency test criteria (IELTS vs MOI waiver)
        - Upfront PKR budget capacity
        """
        detailed = await self.search_scholarships_for_profile_detailed(student, regions=regions, limit=limit)
        return [item.scholarship for item in detailed]

    async def search_scholarships_for_profile_detailed(
        self,
        student: StudentProfile,
        regions: Optional[List[str]] = None,
        limit: int = 30,
    ) -> List[PersonalizedMatch]:
        """Returns deterministic, explainable profile matches from the verified database cache."""
        await self.init_db()
        from workflows.degree_matching import is_degree_match
        from workflows.field_matching import is_field_match

        if isinstance(student, dict):
            pref = student.get("preferences") if isinstance(student.get("preferences"), dict) else {}
            acad = student.get("academic") if isinstance(student.get("academic"), dict) else {}
            lang = student.get("language") if isinstance(student.get("language"), dict) else {}

            target_degree = (
                pref.get("target_degree_level")
                or student.get("target_degree_level")
                or student.get("degree_level")
                or acad.get("current_level")
                or "Bachelor's"
            )
            raw_target_fields = pref.get("target_fields") or student.get("target_fields")
            if not raw_target_fields:
                fld = acad.get("field_of_study") or student.get("field_of_study")
                raw_target_fields = [fld] if fld else ["Computer Science"]
            target_fields = raw_target_fields

            raw_gpa = acad.get("gpa_percentage") or student.get("gpa_percentage") or student.get("gpa")
            try:
                gpa_val = float(raw_gpa) if raw_gpa else 80.0
                student_gpa = gpa_val if gpa_val > 4.0 else (gpa_val / 4.0 * 100.0)
            except Exception:
                student_gpa = 80.0

            has_ielts = bool(lang.get("has_english_test") or student.get("has_ielts") or student.get("ielts"))
            has_moi = bool(lang.get("medium_of_instruction_english") or lang.get("moi_certificate_available") or student.get("has_moi"))
            max_budget = max(0, int(pref.get("max_out_of_pocket_pkr") or student.get("max_budget") or 150000))
            active_regions = regions or pref.get("preferred_regions") or student.get("preferred_regions") or student.get("target_countries") or []
        else:
            target_degree = (
                student.preferences.target_degree_level
                or (getattr(student.academic, "current_level", None).value if getattr(student.academic, "current_level", None) else None)
                or "Bachelor's"
            )
            target_fields = student.preferences.target_fields or (
                [student.academic.field_of_study] if student.academic.field_of_study else ["Computer Science"]
            )
            student_gpa = float(student.academic.gpa_percentage or 80.0)
            has_ielts = bool(student.language.has_english_test)
            has_moi = bool(student.language.medium_of_instruction_english or student.language.moi_certificate_available)
            max_budget = max(0, int(student.preferences.max_out_of_pocket_pkr or 150000))
            active_regions = regions or student.preferences.preferred_regions or []

        query = "SELECT data_json FROM scholarships_cache WHERE 1=1"
        params: List[Any] = []
        if active_regions:
            placeholders = ",".join(["?" for _ in active_regions])
            query += f" AND (LOWER(region) IN ({placeholders}) OR LOWER(country) IN ({placeholders}) OR LOWER(COALESCE(host_country_name, '')) IN ({placeholders}))"
            active_vals = [r.strip().lower() for r in active_regions]
            params.extend(active_vals + active_vals + active_vals)

        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params)
            rows = await cursor.fetchall()
            if not rows and active_regions:
                cursor = await db.execute("SELECT data_json FROM scholarships_cache WHERE 1=1")
                rows = await cursor.fetchall()

        matched: List[PersonalizedMatch] = []
        for row in rows:
            try:
                sc = Scholarship.model_validate_json(row["data_json"])
            except Exception:
                continue

            requirements = sc.pakistan_requirements
            eligibility = sc.eligibility
            language = sc.language
            funding = sc.funding
            if not requirements or not requirements.pakistan_eligible:
                continue
            if not is_degree_match(target_degree, eligibility.degree_levels if eligibility else []):
                continue

            eligible_fields = eligibility.eligible_fields if eligibility else []
            field_match, field_score = is_field_match(target_fields, eligible_fields, sc.name)
            if not field_match:
                continue

            breakdown: Dict[str, float] = {}
            reasons: List[str] = []
            risks: List[str] = []

            breakdown["field_fit"] = round(max(0.0, min(100.0, field_score * 100.0)), 1)
            reasons.append(f"Field alignment with {', '.join(target_fields[:2])}.")

            min_pct = eligibility.min_gpa_percentage if eligibility else None
            min_gpa4 = eligibility.min_gpa_4_scale if eligibility else None
            academic_score = 100.0
            if min_pct and student_gpa < min_pct:
                academic_score = max(0.0, 45.0 - (min_pct - student_gpa) * 4)
                risks.append(f"Academic marks ({student_gpa:.1f}%) are below the stated minimum ({min_pct:.1f}%).")
            elif min_pct:
                margin = student_gpa - min_pct
                academic_score = min(100.0, 82.0 + margin * 2.0)
                reasons.append(f"Academic profile clears the stated minimum by {margin:.1f} percentage points.")
            elif min_gpa4 and student.academic.gpa_4_scale < min_gpa4:
                academic_score = 45.0
                risks.append(f"Converted GPA is below the stated minimum of {min_gpa4:.2f}/4.0.")
            else:
                academic_score = 78.0
                reasons.append("No stricter academic cutoff was published in the cached record.")
            breakdown["academic_fit"] = round(max(0.0, min(100.0, academic_score)), 1)

            bilateral_score = 100.0 if requirements.pakistan_bilateral_quota or requirements.hec_managed else 72.0
            breakdown["pakistan_access"] = bilateral_score
            if bilateral_score >= 100:
                reasons.append("Pakistan-specific bilateral or HEC routing is available.")
            else:
                reasons.append("Pakistani applicants are eligible through the international route.")

            requires_test = bool(language and language.english_test_required and language.minimum_ielts)
            if has_ielts:
                language_score = 100.0
                reasons.append("Declared English-test readiness matches the language gate.")
            elif has_moi and requirements.accepts_moi_certificate:
                language_score = 92.0
                reasons.append("MOI evidence may satisfy the published English requirement.")
            elif not requires_test:
                language_score = 85.0
                reasons.append("No mandatory IELTS threshold is recorded.")
            else:
                language_score = 45.0
                risks.append("English testing or an accepted MOI waiver may still be required.")
            breakdown["language_fit"] = language_score

            funding_type = funding.funding_type.value if funding else "FULL"
            funding_score = 100.0 if funding_type == "FULL" else 72.0 if funding_type == "TUITION_ONLY" else 60.0
            if funding_type == "FULL":
                reasons.append("Funding type is marked fully funded in the verified record.")
            elif max_budget < 250000:
                risks.append("Partial funding may exceed the declared upfront PKR budget.")
            breakdown["funding_fit"] = funding_score

            stipend = int(funding.monthly_stipend_pkr_approx or 0) if funding else 0
            budget_score = 100.0 if funding_type == "FULL" or max_budget >= 250000 else 65.0
            if stipend and funding_type == "FULL":
                reasons.append(f"Recorded stipend estimate is approximately PKR {stipend:,}/month.")
            breakdown["budget_fit"] = budget_score

            verification_score = max(0.0, min(100.0, float(sc.confidence_score or 0.0) * 100.0))
            breakdown["verification"] = round(verification_score, 1)
            if verification_score < 75:
                risks.append("The cached record has lower verification confidence and needs source review.")

            score = (
                breakdown["field_fit"] * 0.22
                + breakdown["academic_fit"] * 0.22
                + breakdown["pakistan_access"] * 0.16
                + breakdown["language_fit"] * 0.14
                + breakdown["funding_fit"] * 0.14
                + breakdown["budget_fit"] * 0.07
                + breakdown["verification"] * 0.05
            )
            matched.append(
                PersonalizedMatch(
                    scholarship=sc,
                    match_score=round(max(0.0, min(100.0, score)), 1),
                    score_breakdown=breakdown,
                    match_reasons=reasons[:6],
                    risk_flags=risks[:5],
                    source_url=sc.portal_url or sc.source_url,
                    verified_at=(sc.deep_dossier.official_sources_verified[0].verified_date
                                 if sc.deep_dossier and sc.deep_dossier.official_sources_verified else None),
                )
            )

        # Resilient Offline Fallback: If strict field matching returned 0 matches,
        # recover opportunities by matching all scholarships for student's degree and region
        if not matched and rows:
            for row in rows:
                try:
                    sc = Scholarship.model_validate_json(row["data_json"])
                except Exception:
                    continue
                if not sc.pakistan_requirements or not sc.pakistan_requirements.pakistan_eligible:
                    continue
                if not is_degree_match(target_degree, sc.eligibility.degree_levels if sc.eligibility else []):
                    continue

                matched.append(
                    PersonalizedMatch(
                        scholarship=sc,
                        match_score=80.0,
                        score_breakdown={
                            "field_fit": 75.0,
                            "academic_fit": 80.0,
                            "pakistan_access": 85.0,
                            "language_fit": 80.0,
                            "funding_fit": 85.0,
                            "budget_fit": 80.0,
                            "verification": 80.0,
                        },
                        match_reasons=[
                            f"General degree match for {target_degree}.",
                            "Universal or bilateral opportunity accessible to Pakistani applicants."
                        ],
                        risk_flags=["Broad compatibility mode active: verify department-specific faculty availability."],
                        source_url=sc.portal_url or sc.source_url,
                        verified_at=(sc.deep_dossier.official_sources_verified[0].verified_date
                                     if sc.deep_dossier and sc.deep_dossier.official_sources_verified else None),
                    )
                )

        matched.sort(key=lambda item: item.match_score, reverse=True)
        return matched[: max(1, min(limit, 100))]


    async def get_scholarships_stats(self) -> Dict[str, Any]:
        """Returns instantaneous aggregated stats of the active scholarship database cache."""
        await self.init_db()
        async with self._get_connection() as db:
            db.row_factory = aiosqlite.Row

            cursor = await db.execute("SELECT region, COUNT(*) as count FROM scholarships_cache GROUP BY region ORDER BY count DESC;")
            regional_rows = await cursor.fetchall()
            by_region = {row["region"]: row["count"] for row in regional_rows}

            cursor = await db.execute("SELECT COUNT(*) as total FROM scholarships_cache;")
            total_row = await cursor.fetchone()
            total = total_row["total"] if total_row else 0

            cursor = await db.execute(
                "SELECT COUNT(*) as with_deep FROM scholarships_cache WHERE json_extract(data_json, '$.deep_dossier') IS NOT NULL;"
            )
            deep_row = await cursor.fetchone()
            with_deep = deep_row["with_deep"] if deep_row else 0

            cursor = await db.execute("SELECT funding_type, COUNT(*) as count FROM scholarships_cache WHERE funding_type IS NOT NULL GROUP BY funding_type ORDER BY count DESC;")
            funding_rows = await cursor.fetchall()
            by_funding = {row["funding_type"]: row["count"] for row in funding_rows}

            cursor = await db.execute("SELECT COUNT(*) as count, SUM(COALESCE(pakistan_quota_seats, 0)) as seats FROM scholarships_cache WHERE pakistan_bilateral_quota = 1 OR hec_managed = 1;")
            quota_row = await cursor.fetchone()
            hec_quota_count = quota_row["count"] if quota_row else 0
            total_seats = quota_row["seats"] if quota_row else 0

            cursor = await db.execute("SELECT COUNT(*) as count FROM scholarships_cache WHERE accepts_moi_certificate = 1;")
            moi_row = await cursor.fetchone()
            moi_count = moi_row["count"] if moi_row else 0

            cursor = await db.execute("SELECT COUNT(*) as count FROM students;")
            std_row = await cursor.fetchone()
            students_count = std_row["count"] if std_row else 0

            cursor = await db.execute("SELECT COUNT(*) as count FROM sessions;")
            sess_row = await cursor.fetchone()
            sessions_count = sess_row["count"] if sess_row else 0

            return {
                "total_scholarships": total,
                "by_region": by_region,
                "by_funding_type": by_funding,
                "hec_bilateral_quota_count": hec_quota_count,
                "total_bilateral_seats": total_seats,
                "moi_waiver_count": moi_count,
                "with_deep_dossiers": with_deep,
                "coverage_percent": round((with_deep / total * 100), 1) if total > 0 else 0.0,
                "total_profiles_seeded": students_count,
                "total_sessions_recorded": sessions_count,
                "database_status": "ONLINE",
            }

    async def close(self):
        """Cancels background flusher task and releases database connection."""
        if self._flusher_task and not self._flusher_task.done():
            self._flusher_task.cancel()
            try:
                await self._flusher_task
            except (asyncio.CancelledError, Exception):
                pass
            self._flusher_task = None
        if self._mem_anchor:
            try:
                thread = getattr(self._mem_anchor, "_thread", None)
                await self._mem_anchor.close()
                if thread and thread.is_alive():
                    thread.join(timeout=1.0)
            except Exception:
                pass
            self._mem_anchor = None
            self._anchor_loop = None
        self._is_initialized = False


_global_session_store: Optional[SessionStore] = None


def get_session_store() -> SessionStore:
    global _global_session_store
    if _global_session_store is None:
        _global_session_store = SessionStore()
    return _global_session_store
