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

    def _extract_deterministic_offline(self, raw_text: str, doc_type: str = "CV") -> Dict[str, Any]:
        """
        Deterministic, rule-based extraction of Pakistani student academic credentials,
        test scores, degrees, and locations when external LLMs or internet are unavailable.
        """
        data: Dict[str, Any] = {"personal": {}, "academic": {}, "language": {}, "preferences": {}}
        t = raw_text

        # 1. Personal Info: Name & City
        m_name = re.search(r"(?i)(?:name|candidate|applicant)\s*[:=-]\s*([^\n\r,]{2,40})", t)
        if m_name:
            data["personal"]["name"] = m_name.group(1).strip()

        m_city = re.search(r"(?i)(?:city|location|residence)\s*[:=-]\s*([^\n\r,]{2,30})", t)
        if m_city:
            data["personal"]["city"] = m_city.group(1).split(",")[0].strip()
        else:
            for city in ["Islamabad", "Lahore", "Karachi", "Rawalpindi", "Faisalabad", "Multan", "Peshawar", "Quetta", "Abbottabad", "Sialkot", "Gujranwala"]:
                if re.search(r"\b" + city + r"\b", t, re.IGNORECASE):
                    data["personal"]["city"] = city
                    break

        # 2. Academic Marks & GPA
        m_pct = re.search(r"(\d{2,3}(?:\.\d+)?)\s*%", t)
        if m_pct:
            data["academic"]["gpa_percentage"] = float(m_pct.group(1))

        m_gpa = re.search(r"(?:gpa|cgpa)?[:\s]*(\d\.\d{1,2})\s*/\s*4(?:\.0)?", t, re.IGNORECASE)
        if m_gpa:
            g4 = float(m_gpa.group(1))
            data["academic"]["gpa_4_scale"] = g4
            if "gpa_percentage" not in data["academic"]:
                data["academic"]["gpa_percentage"] = round(g4 / 4.0 * 100.0, 1)

        # 3. English Proficiency / IELTS
        m_ielts = re.search(r"(?i)\bielts\b[^\d\n\r]{0,15}?(\d(?:\.\d)?)", t)
        if m_ielts:
            score = float(m_ielts.group(1))
            if 3.5 <= score <= 9.0:
                data["language"]["ielts_overall"] = score
                data["language"]["english_proficiency_test"] = "IELTS"
                data["language"]["has_english_test"] = True
        elif re.search(r"(?i)\bmoi\b|medium of instruction", t):
            data["language"]["moi_certificate_available"] = True
            data["language"]["english_proficiency_test"] = "Medium of Instruction (MOI) Certificate"

        # 4. Target Degree Level
        m_target_deg = re.search(r"(?i)target\s*degree[:\s]*([^\n\r,]+)", t)
        if m_target_deg:
            deg_raw = m_target_deg.group(1).lower()
            if "phd" in deg_raw or "doctor" in deg_raw:
                data["preferences"]["target_degree_level"] = "PhD"
            elif "master" in deg_raw or "ms" in deg_raw or "msc" in deg_raw or "mphil" in deg_raw:
                data["preferences"]["target_degree_level"] = "Master's"
            elif "bachelor" in deg_raw or "bs" in deg_raw or "undergrad" in deg_raw:
                data["preferences"]["target_degree_level"] = "Bachelor's"
            else:
                data["preferences"]["target_degree_level"] = m_target_deg.group(1).strip()
        else:
            if re.search(r"(?i)\bphd\b|\bdoctor(?:ate)?\b", t):
                data["preferences"]["target_degree_level"] = "PhD"
            elif re.search(r"(?i)\bmaster(?:'?s)?\b|\bms\b|\bmsc\b|\bmphil\b", t):
                data["preferences"]["target_degree_level"] = "Master's"
            elif re.search(r"(?i)\bbachelor(?:'?s)?\b|\bbs\b|\bundergrad(?:uate)?\b|\bfsc\b|\bics\b", t):
                data["preferences"]["target_degree_level"] = "Bachelor's"

        # 5. Field of Study
        known_fields = [
            ("Computer Science", ["computer science", "compter scince", "computr scince", "comp scince", "compsci", "cs"]),
            ("Software Engineering", ["software engineering", "softwre enginering", "softwre engineering", "se"]),
            ("Artificial Intelligence", ["artificial intelligence", "artifcial intelgence", "ai", "machine learning", "machne lerning", "ml"]),
            ("Data Science", ["data science", "data scince", "data scence", "ds"]),
            ("Electrical Engineering", ["electrical engineering", "electrcial engr", "electrcial engineering", "electrcial", "ee"]),
            ("Mechanical Engineering", ["mechanical engineering", "mechanical engg", "mechanical engr", "mechnical engineering", "me"]),
            ("Civil Engineering", ["civil engineering", "civiil enginering", "civil engg", "ce"]),
            ("Business Administration", ["business administration", "bussines admistration", "bussiness administration", "bba", "mba"]),
            ("Finance", ["finance", "finence"]),
            ("Economics", ["economics", "econmics"]),
            ("Biomedical Engineering", ["biomedical engineering", "biomdical"]),
        ]
        t_lower = t.lower()
        for canonical, aliases in known_fields:
            if any(re.search(r"\b" + re.escape(alias) + r"\b", t_lower) for alias in aliases):
                data["academic"]["field_of_study"] = canonical
                data["preferences"]["target_fields"] = [canonical]
                break

        # Remove empty sub-dictionaries
        cleaned_result = {k: v for k, v in data.items() if v}
        return cleaned_result

    def _extract_chat_deterministic_offline(
        self,
        chat_message: str,
        current_profile_summary: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Deterministic, offline extraction of student profile updates from conversational chat
        with an informative Pakistani counselor response.
        """
        extracted = self._extract_deterministic_offline(chat_message)
        updates: Dict[str, Any] = {}
        for section in ["personal", "academic", "language", "preferences"]:
            if extracted.get(section):
                updates[section] = extracted[section]

        # Generate contextual offline counselor reply acknowledging inputs
        parts = []
        if updates.get("academic", {}).get("field_of_study"):
            parts.append(f"field of study ({updates['academic']['field_of_study']})")
        if updates.get("academic", {}).get("gpa_percentage"):
            parts.append(f"marks ({updates['academic']['gpa_percentage']}%)")
        if updates.get("language", {}).get("ielts_overall"):
            parts.append(f"IELTS score ({updates['language']['ielts_overall']})")
        if updates.get("preferences", {}).get("target_degree_level"):
            parts.append(f"degree level ({updates['preferences']['target_degree_level']})")

        if parts:
            reply = f"Understood! I've recorded your {', '.join(parts)}. Our local scholarship database is evaluating programs with Pakistani bilateral quotas matching your criteria."
        else:
            reply = "I've noted your message. Please share your marks or GPA percentage, field of study, and whether you have IELTS to find matching fully funded scholarships!"

        return {
            "extracted_updates": updates,
            "assistant_reply": reply,
        }

    async def extract_from_text(self, raw_text: str, doc_type: str = "CV") -> Dict[str, Any]:
        """
        Extracts structured student profile fields from document text using Groq (primary) with Gemini (fallback).
        Seamlessly falls back to deterministic rule-based extraction when offline or if external APIs fail.
        """
        if getattr(self.settings, "OFFLINE_MODE", False) or (self.key_manager.groq.total_keys == 0 and self.key_manager.gemini.total_keys == 0):
            return self._extract_deterministic_offline(raw_text, doc_type)

        prompt = f"Document Type: {doc_type}\n\nDocument Text Content:\n{raw_text[:8000]}"

        # 1. Try Groq first (Ultra-fast)
        for attempt in range(max(1, self.key_manager.groq.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.groq.get_key()
                client = AsyncGroq(api_key=api_key, max_retries=0)
                res = await asyncio.wait_for(
                    client.chat.completions.create(
                        model=self.settings.GROQ_MODEL,
                        messages=[
                            {"role": "system", "content": DOCUMENT_EXTRACTION_SYSTEM_PROMPT},
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
                if parsed:
                    return parsed
            except Exception as e:
                err_msg = str(e).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                logger.warning(f"Groq document extraction attempt {attempt+1} failed: {e}.")
                if api_key:
                    await self.key_manager.groq.report_failure(api_key)
                if is_net_error:
                    break

        # 2. Fallback to Gemini
        for attempt in range(max(1, self.key_manager.gemini.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.gemini.get_key()
                client = genai.Client(api_key=api_key)
                response = await asyncio.wait_for(
                    asyncio.to_thread(
                        client.models.generate_content,
                        model=self.settings.GEMINI_PRIMARY_MODEL,
                        contents=f"{DOCUMENT_EXTRACTION_SYSTEM_PROMPT}\n\n{prompt}",
                    ),
                    timeout=3.5,
                )
                await self.key_manager.gemini.report_success(api_key)
                text = response.text or ""
                match = re.search(r"\{[\s\S]*\}", text)
                if match:
                    parsed = json.loads(match.group(0))
                    if parsed:
                        return parsed
            except Exception as e:
                err_msg = str(e).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                logger.warning(f"Gemini document extraction fallback attempt {attempt+1} failed: {e}")
                if api_key:
                    await self.key_manager.gemini.report_failure(api_key)
                if is_net_error:
                    break

        # 3. Deterministic offline fallback
        logger.info("External LLMs offline; utilizing deterministic offline document parser.")
        return self._extract_deterministic_offline(raw_text, doc_type)

    async def extract_profile_updates_from_chat(
        self,
        chat_message: str,
        current_profile_summary: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Extracts updated profile attributes from student chat message and synthesizes conversational counselor response.
        Seamlessly falls back to deterministic rule-based intake when offline or if external APIs fail.
        """
        if getattr(self.settings, "OFFLINE_MODE", False) or (self.key_manager.groq.total_keys == 0 and self.key_manager.gemini.total_keys == 0):
            return self._extract_chat_deterministic_offline(chat_message, current_profile_summary)

        prompt = f"Current Profile State: {json.dumps(current_profile_summary or {})}\n\nStudent Message: {chat_message}"

        # 1. Try Groq first (Ultra-fast)
        for attempt in range(max(1, self.key_manager.groq.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.groq.get_key()
                client = AsyncGroq(api_key=api_key, max_retries=0)
                res = await asyncio.wait_for(
                    client.chat.completions.create(
                        model=self.settings.GROQ_MODEL,
                        messages=[
                            {"role": "system", "content": CHAT_INTAKE_SYSTEM_PROMPT},
                            {"role": "user", "content": prompt},
                        ],
                        response_format={"type": "json_object"},
                        temperature=0.2,
                    ),
                    timeout=3.5,
                )
                await self.key_manager.groq.report_success(api_key)
                content = res.choices[0].message.content or "{}"
                parsed = json.loads(content)
                if parsed and ("extracted_updates" in parsed or "assistant_reply" in parsed):
                    return parsed
            except Exception as e:
                err_msg = str(e).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                logger.warning(f"Groq chat extraction attempt {attempt+1} failed: {e}.")
                if api_key:
                    await self.key_manager.groq.report_failure(api_key)
                if is_net_error:
                    break

        # 2. Fallback to Gemini
        for attempt in range(max(1, self.key_manager.gemini.total_keys)):
            api_key = None
            try:
                api_key = await self.key_manager.gemini.get_key()
                client = genai.Client(api_key=api_key)
                response = await asyncio.wait_for(
                    asyncio.to_thread(
                        client.models.generate_content,
                        model=self.settings.GEMINI_PRIMARY_MODEL,
                        contents=f"{CHAT_INTAKE_SYSTEM_PROMPT}\n\n{prompt}",
                    ),
                    timeout=3.5,
                )
                await self.key_manager.gemini.report_success(api_key)
                text = response.text or ""
                match = re.search(r"\{[\s\S]*\}", text)
                if match:
                    parsed = json.loads(match.group(0))
                    if parsed and ("extracted_updates" in parsed or "assistant_reply" in parsed):
                        return parsed
            except Exception as e:
                err_msg = str(e).lower()
                is_net_error = any(kw in err_msg for kw in ["connect", "resolution", "unreachable", "name not known", "gaierror", "offline", "timeout", "timed out"])
                logger.warning(f"Gemini chat extraction fallback attempt {attempt+1} failed: {e}")
                if api_key:
                    await self.key_manager.gemini.report_failure(api_key)
                if is_net_error:
                    break

        # 3. Deterministic offline fallback
        logger.info("External LLMs offline; utilizing deterministic offline chat counselor.")
        return self._extract_chat_deterministic_offline(chat_message, current_profile_summary)
