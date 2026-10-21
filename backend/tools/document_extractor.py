import asyncio
import json
import logging
import re
from typing import Any, Dict, Optional
from google import genai
from groq import AsyncGroq
from config import get_settings
from utils.api_keys import get_key_manager, AllKeysExhaustedError

logger = logging.getLogger("scholarx.tools.document_extractor")


DOCUMENT_EXTRACTION_SYSTEM_PROMPT = """
You are ScholarX's Precision Student Document Extraction Agent.
Your job is to analyze the provided text of a Pakistani student's document (CV, Academic Transcript, IELTS Score Report, or Statement of Purpose),
and extract a comprehensive, structured JSON representation of their personal, academic, language, test score, and preference profiles.

Rules:
1. Extract true factual data. Do not make up marks, CGPA, institutions, or test scores.
2. For education level in Pakistan:
   - "Matric / SSC" for 10th grade.
   - "Intermediate / ICS / FSc / FA" for 12th grade (HSSC/FSc/ICS).
   - "Bachelor's / BS / BE / BBA" for 16-year BS/BE/BBA.
   - "Master's / MS / MSc / MPhil" for 18-year MS/MPhil.
   - "PhD / Doctorate" for doctoral degrees.
3. If percentage is found (e.g. 88%, 950/1100 = 86.36%), set "gpa_percentage" to that float.
4. If IELTS/TOEFL is found, extract overall band score and sub-bands (Listening, Reading, Writing, Speaking).
5. Extract city, province, and target study preferences if mentioned.

Return ONLY valid JSON adhering strictly to this format:
{
  "personal": {
    "name": "string",
    "city": "string",
    "province": "string",
    "age": integer or null,
    "cnic": "string or null",
    "passport_number": "string or null"
  },
  "academic": {
    "current_level": "Matric / SSC | Intermediate / ICS / FSc / FA | Bachelor's / BS / BE / BBA | Master's / MS / MSc / MPhil | PhD / Doctorate",
    "field_of_study": "string",
    "board_university": "string",
    "institution": "string",
    "gpa_percentage": float,
    "gpa_4_scale": float,
    "graduation_year": integer or null,
    "subjects": ["string"]
  },
  "language": {
    "english_proficiency_test": "IELTS | TOEFL | Duolingo | PTE Academic | Medium of Instruction (MOI) Certificate | None / Not Available",
    "ielts_overall": float or null,
    "ielts_subbands": {"L": float, "R": float, "W": float, "S": float},
    "toefl_score": integer or null,
    "duolingo_score": integer or null,
    "has_english_test": boolean,
    "moi_certificate_available": boolean
  },
  "preferences": {
    "target_degree_level": "Bachelor's | Master's | PhD | string",
    "target_fields": ["string"],
    "preferred_regions": ["Europe | Asia | Americas | MENA | Oceania"]
  }
}
"""


CHAT_INTAKE_SYSTEM_PROMPT = """
You are ScholarX's empathetic and highly experienced Pakistani Study Abroad Admissions Counselor.
Your role is to converse with Pakistani students, extract their academic/language/preference profile details from their messages,
and respond warmly with an encouraging explanation and follow-up guidance tailored to Pakistani education standards (BISE, HEC, FSc/ICS, BS, IELTS).

Analyze the student's message and the current profile state.

Return ONLY valid JSON adhering to:
{
  "extracted_updates": {
    "personal": {"name": "...", "city": "..."},
    "academic": {"current_level": "...", "field_of_study": "...", "gpa_percentage": 0.0, "board_university": "..."},
    "language": {"english_proficiency_test": "...", "ielts_overall": 0.0, "has_english_test": true/false},
    "preferences": {"target_degree_level": "...", "target_fields": [...], "preferred_regions": [...]}
  },
  "assistant_reply": "Warm, encouraging message acknowledging their details and asking the next most important question or giving clear next steps."
}
Include only non-empty fields in extracted_updates.
"""


class DocumentExtractor:
    def __init__(self):
        self.key_manager = get_key_manager()
        self.settings = get_settings()

    async def extract_from_text(self, raw_text: str, doc_type: str = "CV") -> Dict[str, Any]:
        """
        Extracts structured student profile fields from document text using Groq (primary) with Gemini (fallback).
        """
        prompt = f"Document Type: {doc_type}\n\nDocument Text Content:\n{raw_text[:8000]}"

        # 1. Try Groq first (Ultra-fast)
        for attempt in range(max(1, self.key_manager.groq.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.groq.get_key()
                client = AsyncGroq(api_key=api_key, max_retries=0)
                res = await client.chat.completions.create(
                    model=self.settings.GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": DOCUMENT_EXTRACTION_SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.1,
                    max_tokens=850,
                )
                await self.key_manager.groq.report_success(api_key)
                content = res.choices[0].message.content or "{}"
                return json.loads(content)
            except Exception as e:
                logger.warning(f"Groq document extraction attempt {attempt+1} failed: {e}. Rotating...")
                if api_key:
                    await self.key_manager.groq.report_failure(api_key)

        # 2. Fallback to Gemini
        for attempt in range(max(1, self.key_manager.gemini.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.gemini.get_key()
                client = genai.Client(api_key=api_key)
                response = await asyncio.to_thread(
                    client.models.generate_content,
                    model=self.settings.GEMINI_PRIMARY_MODEL,
                    contents=f"{DOCUMENT_EXTRACTION_SYSTEM_PROMPT}\n\n{prompt}",
                )
                await self.key_manager.gemini.report_success(api_key)
                text = response.text or ""
                match = re.search(r"\{[\s\S]*\}", text)
                if match:
                    return json.loads(match.group(0))
            except Exception as e:
                logger.warning(f"Gemini document extraction fallback attempt {attempt+1} failed: {e}")
                if api_key:
                    await self.key_manager.gemini.report_failure(api_key)

        return {}

    async def extract_profile_updates_from_chat(
        self,
        chat_message: str,
        current_profile_summary: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Extracts updated profile attributes from student chat message and synthesizes conversational counselor response.
        """
        prompt = f"Current Profile State: {json.dumps(current_profile_summary or {})}\n\nStudent Message: {chat_message}"

        # 1. Try Groq first (Ultra-fast)
        for attempt in range(max(1, self.key_manager.groq.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.groq.get_key()
                client = AsyncGroq(api_key=api_key, max_retries=0)
                res = await client.chat.completions.create(
                    model=self.settings.GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": CHAT_INTAKE_SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.2,
                )
                await self.key_manager.groq.report_success(api_key)
                content = res.choices[0].message.content or "{}"
                return json.loads(content)
            except Exception as e:
                logger.warning(f"Groq chat extraction attempt {attempt+1} failed: {e}. Rotating...")
                if api_key:
                    await self.key_manager.groq.report_failure(api_key)

        # 2. Fallback to Gemini
        for attempt in range(max(1, self.key_manager.gemini.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.gemini.get_key()
                client = genai.Client(api_key=api_key)
                response = await asyncio.to_thread(
                    client.models.generate_content,
                    model=self.settings.GEMINI_PRIMARY_MODEL,
                    contents=f"{CHAT_INTAKE_SYSTEM_PROMPT}\n\n{prompt}",
                )
                await self.key_manager.gemini.report_success(api_key)
                text = response.text or ""
                match = re.search(r"\{[\s\S]*\}", text)
                if match:
                    return json.loads(match.group(0))
            except Exception as e:
                logger.warning(f"Gemini chat extraction fallback attempt {attempt+1} failed: {e}")
                if api_key:
                    await self.key_manager.gemini.report_failure(api_key)

        return {
            "extracted_updates": {},
            "assistant_reply": "I've noted your message. Please share your marks percentage, field of study, and target country to find matching fully funded scholarships!",
        }
