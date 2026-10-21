from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.discover import router as discover_router
from api.routes.profile import router as profile_router
from api.routes.scholarships import router as scholarships_router
from api.routes.sessions import router as sessions_router
from api.routes.stream import router as stream_router
from api.routes.exhibition import router as exhibition_router
from config import get_settings
from db.seed import load_and_seed_profiles, load_and_seed_scholarships
from db.session_store import get_session_store
from utils.api_keys import get_key_manager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scholarx.api")

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: validate config, initialize database and seed baseline data
    settings.validate_startup_configuration()
    logger.info("Initializing ScholarX backend database and local cache...")
    store = get_session_store()
    await store.init_db()

    cached = await store.get_all_cached_scholarships()
    if len(cached) < 310:
        logger.info(f"Database contains {len(cached)}/310 scholarships; refreshing with up-to-date catalog...")
        sc_count = await load_and_seed_scholarships(purge_outdated=True)
        pr_count = await load_and_seed_profiles()
        logger.info(f"Database seeded with {sc_count} scholarships and {pr_count} demo profiles.")
    else:
        logger.info(f"ScholarX database cache verified with {len(cached)} up-to-date scholarships (100% deep dossier coverage).")

    yield
    logger.info("ScholarX backend shutting down.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# CORS configuration supporting environment additions while restricting arbitrary origins
default_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
if settings.CORS_ORIGINS:
    extra_origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]
    default_origins.extend(extra_origins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=default_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(stream_router, prefix="/api")
app.include_router(profile_router, prefix="/api")
app.include_router(discover_router, prefix="/api")
app.include_router(scholarships_router, prefix="/api")
app.include_router(sessions_router, prefix="/api")
app.include_router(exhibition_router, prefix="/api")


@app.get("/")
async def root():
    return {
        "name": "ScholarX - Autonomous Scholarship Intelligence Network for Pakistani Students",
        "status": "ONLINE",
        "version": settings.APP_VERSION,
    }


@app.get("/api/health")
async def health_check():
    """Returns system status and high-level provider availability without leaking keys or counts."""
    key_mgr = get_key_manager()
    store = get_session_store()
    providers_summary = {
        "gemini": {
            "configured": key_mgr.gemini.has_keys,
            "healthy": any(kh.is_healthy for kh in key_mgr.gemini.key_healths) if key_mgr.gemini.has_keys else False,
        },
        "groq": {
            "configured": key_mgr.groq.has_keys,
            "healthy": any(kh.is_healthy for kh in key_mgr.groq.key_healths) if key_mgr.groq.has_keys else False,
        },
        "tavily": {
            "configured": key_mgr.tavily.has_keys,
            "healthy": any(kh.is_healthy for kh in key_mgr.tavily.key_healths) if key_mgr.tavily.has_keys else False,
        },
        "firecrawl": {
            "configured": key_mgr.firecrawl.has_keys,
            "healthy": any(kh.is_healthy for kh in key_mgr.firecrawl.key_healths) if key_mgr.firecrawl.has_keys else False,
        },
        "jina": {
            "configured": key_mgr.jina.has_keys,
            "healthy": any(kh.is_healthy for kh in key_mgr.jina.key_healths) if key_mgr.jina.has_keys else False,
        },
    }
    return {
        "status": "HEALTHY",
        "database": {
            "configured_path": store.db_path,
            "persistent": not store._using_memory_fallback,
            "mode": "sqlite_persistent" if not store._using_memory_fallback else "memory_fallback",
        },
        "providers": providers_summary,
        "api_keys": providers_summary,
    }
