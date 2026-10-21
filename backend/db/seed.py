import asyncio
import json
import logging
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from db.session_store import get_session_store
from schemas.scholarship import Scholarship
from schemas.student import StudentProfile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scholarx.seed")

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
SCHOLARSHIPS_DIR = DATA_DIR / "scholarships"
PROFILES_DIR = DATA_DIR / "profiles"


async def load_and_seed_scholarships(purge_outdated: bool = True) -> int:
    store = get_session_store()
    await store.init_db()

    total_seeded = 0
    valid_ids = []
    for json_file in sorted(SCHOLARSHIPS_DIR.glob("*.json")):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        scholarship = Scholarship.model_validate(item)
                        await store.upsert_scholarship_cache(scholarship)
                        valid_ids.append(scholarship.scholarship_id)
                        total_seeded += 1
            logger.info(f"Seeded scholarships from {json_file.name}")
        except Exception as e:
            logger.error(f"Failed to seed from {json_file.name}: {e}")

    if purge_outdated and valid_ids:
        purged = await store.purge_unverified_or_outdated_scholarships(valid_ids)
        if purged > 0:
            logger.info(f"Purged {purged} outdated or unverified scholarships from database cache.")

    return total_seeded


async def load_and_seed_profiles() -> int:
    store = get_session_store()
    await store.init_db()

    total_profiles = 0
    for profile_file in PROFILES_DIR.glob("*.json"):
        try:
            with open(profile_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                profile = StudentProfile.model_validate(data)
                await store.save_student_profile(profile)
                total_profiles += 1
            logger.info(f"Seeded student profile: {profile.personal.name} ({profile_file.name})")
        except Exception as e:
            logger.error(f"Failed to seed profile from {profile_file.name}: {e}")

    return total_profiles


async def main():
    logger.info("Starting ScholarX knowledge base seeding...")
    sc_count = await load_and_seed_scholarships()
    pr_count = await load_and_seed_profiles()
    logger.info(f"Seeding completed successfully! Total Scholarships: {sc_count}, Total Profiles: {pr_count}")


if __name__ == "__main__":
    asyncio.run(main())
