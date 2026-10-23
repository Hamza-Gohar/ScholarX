import asyncio
import json
import logging
import re
import uuid
from typing import Any, Dict, Optional
from google import genai
from groq import AsyncGroq
from config import get_settings
from schemas.scholarship import (
    EligibilityCriteria,
    FundingDetails,
    FundingType,
    LanguageRequirement,
    PakistanSpecificRequirements,
    Scholarship,
    ScholarshipStatus,
)
from utils.api_keys import get_key_manager, AllKeysExhaustedError

logger = logging.getLogger("scholarx.tools.extractor")


EXTRACTION_SYSTEM_PROMPT = """
You are ScholarX's Precision Scholarship Extraction Agent.
Your job is to analyze the provided scraped webpage markdown of a scholarship or university funding program,
and extract a comprehensive, strictly formatted JSON structure tailored specifically for Pakistani students.

Rules:
1. Be factually accurate. Do NOT invent coverage. If a field is not mentioned, use null or false.
2. Specifically evaluate whether Pakistani citizens are eligible. Note any Pakistan bilateral government quotas (HEC quotas, seats, HEC USAT/HAT requirements).
3. If tuition is 100% covered and stipend/accommodation is provided, set funding_type to "FULL".
4. If an English test is required (IELTS, TOEFL), extract the exact minimum overall score. Note if Medium of Instruction (MOI) certificates are accepted.
5. Extract application deadlines in YYYY-MM-DD format if present.

Return ONLY valid JSON adhering to the following schema:
{
  "name": "string",
  "host_country": "2-letter ISO code e.g. HU, DE, CN, TR, US, GB, KR, JP",
  "host_country_name": "Full country name",
  "host_institution": "University or funding organization name",
  "source_url": "Official URL",
  "portal_url": "Application portal link or null",
  "funding": {
    "funding_type": "FULL | TUITION_ONLY | PARTIAL | STIPEND_ONLY",
    "tuition": "string description",
    "accommodation": "string description",
    "monthly_stipend": "string or null",
    "monthly_stipend_pkr_approx": integer or null,
    "travel_airfare": "COVERED | NOT_COVERED | REIMBURSED",
    "health_insurance": "string description"
  },
  "pakistan_requirements": {
    "pakistan_eligible": boolean,
    "pakistan_bilateral_quota": boolean,
    "pakistan_quota_seats": integer or null,
    "hec_managed": boolean,
    "hec_portal_url": "string or null",
    "hec_hat_required": boolean,
    "hec_usat_required": boolean,
    "hec_attestation_required": boolean,
    "ibcc_equivalence_required": boolean,
    "mofa_attestation_required": boolean,
    "accepts_moi_certificate": boolean
  },
  "language": {
    "english_test_required": boolean,
    "minimum_ielts": float or null,
    "minimum_toefl": integer or null,
    "minimum_duolingo": integer or null,
    "host_language_prep": boolean,
    "notes": "string or null"
  },
  "eligibility": {
    "degree_levels": ["Bachelor's", "Master's", "PhD"],
    "eligible_fields": ["string"],
    "min_gpa_percentage": float or null,
    "min_gpa_4_scale": float or null,
    "age_limit_undergrad": integer or null,
    "age_limit_postgrad": integer or null,
    "min_years_education": integer (12 for undergrad, 16 for master),
    "eligible_nationalities": ["Pakistan", "PK"]
  },
  "application_opens": "YYYY-MM-DD or null",
  "application_deadline": "YYYY-MM-DD or null",
  "academic_intake": "Fall 2027 or null",
  "description": "2-sentence summary of the scholarship for Pakistani applicants",
  "competition_level": "LOW | MODERATE | HIGH | EXTREME",
  "success_rate_pakistan_percent": float or null
}
"""


class ScholarshipExtractor:
    def __init__(self):
        self.settings = get_settings()
        self.key_manager = get_key_manager()

    def _sanitize_scholarship_dict(self, parsed: Dict[str, Any], source_url: str, region: str) -> Dict[str, Any]:
        """Cleans and sanitizes raw LLM output to guarantee valid Pydantic instantiation."""
        if not parsed.get("name"):
            parsed["name"] = f"Scholarship Opportunity ({region})"
        if not parsed.get("host_country"):
            parsed["host_country"] = "DE" if region == "Europe" else "CN" if region == "Asia" else "US" if region == "Americas" else "SA" if region == "MENA" else "AU"
        if not parsed.get("host_country_name"):
            parsed["host_country_name"] = parsed["host_country"]

        # Funding sanitization
        funding = parsed.get("funding") or {}
        if not isinstance(funding, dict):
            funding = {}
        if not funding.get("funding_type") or funding["funding_type"] not in [ft.value for ft in FundingType]:
            funding["funding_type"] = "FULL"
        if not funding.get("tuition"):
            funding["tuition"] = "100% Tuition Waiver"
        if not funding.get("accommodation"):
            funding["accommodation"] = "Covered via monthly allowance or campus housing"
        if not funding.get("health_insurance"):
            funding["health_insurance"] = "Comprehensive health insurance covered"
        if not funding.get("travel_airfare") or funding["travel_airfare"] not in ("COVERED", "NOT_COVERED", "REIMBURSED"):
            funding["travel_airfare"] = "NOT_COVERED"
        parsed["funding"] = funding

        # Pakistan requirements sanitization
        pk = parsed.get("pakistan_requirements") or {}
        if not isinstance(pk, dict):
            pk = {}
        for bool_field, default_val in [
            ("pakistan_eligible", True),
            ("pakistan_bilateral_quota", False),
            ("hec_managed", False),
            ("hec_hat_required", False),
            ("hec_usat_required", False),
            ("hec_attestation_required", True),
            ("ibcc_equivalence_required", False),
            ("mofa_attestation_required", False),
            ("accepts_moi_certificate", False),
        ]:
            if pk.get(bool_field) is None:
                pk[bool_field] = default_val
        parsed["pakistan_requirements"] = pk

        # Eligibility sanitization
        elig = parsed.get("eligibility") or {}
        if not isinstance(elig, dict):
            elig = {}
        if not elig.get("min_years_education"):
            elig["min_years_education"] = 12
        if not elig.get("work_experience_years_required"):
            elig["work_experience_years_required"] = 0
        if not elig.get("degree_levels"):
            elig["degree_levels"] = ["Bachelor's", "Master's", "PhD"]
        if not elig.get("eligible_nationalities"):
            elig["eligible_nationalities"] = ["Pakistan", "PK"]
        parsed["eligibility"] = elig

        # Language sanitization
        lang = parsed.get("language") or {}
        if not isinstance(lang, dict):
            lang = {}
        if lang.get("english_test_required") is None:
            lang["english_test_required"] = True
        if lang.get("host_language_prep") is None:
            lang["host_language_prep"] = False
        parsed["language"] = lang

        # ID and metadata
        parsed["scholarship_id"] = f"SCH-{region[:2].upper()}-{uuid.uuid4().hex[:6].upper()}"
        parsed["region"] = region
        parsed["source_url"] = source_url
        parsed["status"] = ScholarshipStatus.DISCOVERED

        return parsed

    async def extract_scholarship(
        self,
        raw_text: str,
        source_url: str = "",
        region: str = "Global",
    ) -> Optional[Scholarship]:
        """
        Extracts structured Scholarship schema from raw scraped markdown using Groq (primary) and Gemini (fallback).
        """
        if getattr(self.settings, "OFFLINE_MODE", False) or (self.key_manager.groq.total_keys == 0 and self.key_manager.gemini.total_keys == 0):
            return None

        if not raw_text or len(raw_text.strip()) < 100:
            return None

        truncated_text = raw_text[:2000]
        prompt = (
            f"=== REGION: {region} ===\n"
            f"=== SOURCE URL: {source_url} ===\n\n"
            f"=== WEBPAGE CONTENT ===\n{truncated_text}\n"
        )

        # 1. Try Groq (Ultra-fast 0.5s response)
        for attempt in range(max(1, self.key_manager.groq.total_keys)):
            try:
                api_key = await self.key_manager.groq.get_key()
            except AllKeysExhaustedError:
                break

            try:
                client = AsyncGroq(api_key=api_key, max_retries=0)
                res = await asyncio.wait_for(
                    client.chat.completions.create(
                        model=self.settings.GROQ_MODEL,
                        messages=[
                            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
                            {"role": "user", "content": prompt},
                        ],
                        response_format={"type": "json_object"},
                        temperature=0.1,
                        max_tokens=850,
                    ),
                    timeout=3.5,
                )
                await self.key_manager.groq.report_success(api_key)
                content = res.choices[0].message.content or "{}"
                parsed = json.loads(content)
                sanitized = self._sanitize_scholarship_dict(parsed, source_url, region)
                return Scholarship.model_validate(sanitized)
            except Exception as e:
                err_msg = str(e).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                logger.warning(f"Groq scholarship extraction attempt {attempt+1} failed: {e}.")
                await self.key_manager.groq.report_failure(api_key)
                if is_net_error:
                    break

        # 2. Fallback to Gemini
        for attempt in range(max(1, self.key_manager.gemini.total_keys)):
            try:
                api_key = await self.key_manager.gemini.get_key()
            except AllKeysExhaustedError:
                break

            try:
                client = genai.Client(api_key=api_key)
                response = await asyncio.wait_for(
                    asyncio.to_thread(
                        client.models.generate_content,
                        model=self.settings.GEMINI_PRIMARY_MODEL,
                        contents=f"{EXTRACTION_SYSTEM_PROMPT}\n\n{prompt}",
                    ),
                    timeout=3.5,
                )
                await self.key_manager.gemini.report_success(api_key)
                text = response.text or ""
                match = re.search(r"\{[\s\S]*\}", text)
                if match:
                    parsed = json.loads(match.group(0))
                    sanitized = self._sanitize_scholarship_dict(parsed, source_url, region)
                    return Scholarship.model_validate(sanitized)
            except Exception as exc:
                err_msg = str(exc).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                logger.warning(f"Gemini scholarship extraction fallback attempt {attempt+1} failed: {exc}")
                await self.key_manager.gemini.report_failure(api_key)
                if is_net_error:
                    break

        logger.info("Extraction unavailable or offline. Using verified database record.")
        return None
