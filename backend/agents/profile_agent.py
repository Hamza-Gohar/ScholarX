import logging
from typing import Any, Callable, Dict, List, Optional, Tuple
from db.session_store import get_session_store
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.student import (
    StudentProfile,
    EducationLevel,
    EnglishTestType,
    DocumentItem,
    DocumentQuality,
)
from tools.document_parser import DocumentParserTool, DocumentType, ParsedDocument
from tools.document_extractor import DocumentExtractor
from utils.profile_validator import ProfileValidator

logger = logging.getLogger("scholarx.agents.profile")


class ProfileAgent:
    def __init__(self):
        self.session_store = get_session_store()
        self.parser = DocumentParserTool()
        self.extractor = DocumentExtractor()
        self.validator = ProfileValidator()

    def _emit_event(
        self,
        student: StudentProfile,
        event_type: AgentEventType,
        payload: dict,
        severity: EventSeverity = EventSeverity.INFO,
        callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> ScholarXEvent:
        event = ScholarXEvent(
            session_id=student.session_id,
            event_type=event_type,
            agent_id="profile_agent",
            agent_display_name="Profile & Intake Agent",
            component_type="AGENT",
            phase="INTAKE",
            payload=payload,
            severity=severity,
        )
        if callback:
            try:
                callback(event)
            except Exception as e:
                logger.warning(f"Failed to invoke event callback: {e}")
        return event

    def _apply_extracted_updates(self, student: StudentProfile, data: Dict[str, Any]) -> StudentProfile:
        """Helper to cleanly merge dictionary updates into Pydantic student model."""
        personal = data.get("personal", {})
        if personal:
            if personal.get("name") and personal["name"].strip():
                student.personal.name = personal["name"].strip()
            if personal.get("city"):
                student.personal.city = personal["city"].strip()
            if personal.get("province"):
                student.personal.province = personal["province"].strip()
            if personal.get("age"):
                student.personal.age = int(personal["age"])
            if personal.get("cnic"):
                student.personal.cnic = personal["cnic"].strip()
            if personal.get("passport_number"):
                student.personal.passport_number = personal["passport_number"].strip()

        academic = data.get("academic", {})
        if academic:
            if academic.get("current_level"):
                lvl_val = academic["current_level"]
                for el in EducationLevel:
                    if el.value.lower() == str(lvl_val).lower() or el.name.lower() == str(lvl_val).lower():
                        student.academic.current_level = el
                        break
            if academic.get("field_of_study"):
                student.academic.field_of_study = academic["field_of_study"].strip()
            if academic.get("board_university"):
                student.academic.board_university = academic["board_university"].strip()
            if academic.get("institution"):
                student.academic.institution = academic["institution"].strip()
            if academic.get("gpa_percentage") is not None and float(academic["gpa_percentage"]) > 0:
                student.academic.gpa_percentage = float(academic["gpa_percentage"])
            if academic.get("gpa_4_scale") is not None and float(academic["gpa_4_scale"]) > 0:
                student.academic.gpa_4_scale = float(academic["gpa_4_scale"])
            if academic.get("graduation_year"):
                student.academic.graduation_year = int(academic["graduation_year"])
            if academic.get("subjects") and isinstance(academic["subjects"], list):
                student.academic.subjects = academic["subjects"]

        language = data.get("language", {})
        if language:
            if language.get("english_proficiency_test"):
                t_val = language["english_proficiency_test"]
                for et in EnglishTestType:
                    if et.value.lower() == str(t_val).lower() or et.name.lower() == str(t_val).lower():
                        student.language.english_proficiency_test = et
                        break
            if language.get("ielts_overall") is not None:
                student.language.ielts_overall = float(language["ielts_overall"])
                student.language.has_english_test = True
            if language.get("ielts_subbands") and isinstance(language["ielts_subbands"], dict):
                student.language.ielts_subbands = language["ielts_subbands"]
            if language.get("toefl_score"):
                student.language.toefl_score = int(language["toefl_score"])
                student.language.has_english_test = True
            if language.get("has_english_test") is not None:
                student.language.has_english_test = bool(language["has_english_test"])
            if language.get("moi_certificate_available") is not None:
                student.language.moi_certificate_available = bool(language["moi_certificate_available"])

        preferences = data.get("preferences", {})
        if preferences:
            if preferences.get("target_degree_level"):
                student.preferences.target_degree_level = preferences["target_degree_level"].strip()
            if preferences.get("target_fields") and isinstance(preferences["target_fields"], list):
                student.preferences.target_fields = [f.strip() for f in preferences["target_fields"] if f.strip()]
            if preferences.get("preferred_regions") and isinstance(preferences["preferred_regions"], list):
                student.preferences.preferred_regions = preferences["preferred_regions"]
            if preferences.get("max_out_of_pocket_pkr"):
                student.preferences.max_out_of_pocket_pkr = int(preferences["max_out_of_pocket_pkr"])

        return student

    async def ingest_document(
        self,
        student: StudentProfile,
        file_path: str,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> StudentProfile:
        """
        Processes an uploaded student document (PDF, DOCX, etc.), extracts entities using Gemini,
        validates the profile, and updates the local SQLite session store.
        """
        filename = file_path.split("/")[-1]
        self._emit_event(
            student,
            AgentEventType.DOCUMENT_UPLOADED,
            {"filename": filename, "file_path": file_path},
            EventSeverity.INFO,
            event_callback,
        )

        parsed_doc: ParsedDocument = self.parser.parse_file(file_path)
        if not parsed_doc.is_valid:
            logger.error(f"Failed to parse document: {parsed_doc.error}")
            return student

        self._emit_event(
            student,
            AgentEventType.DOCUMENT_PARSED,
            {
                "filename": filename,
                "doc_type": parsed_doc.doc_type.value,
                "char_count": parsed_doc.char_count,
                "page_count": parsed_doc.page_count,
            },
            EventSeverity.SUCCESS,
            event_callback,
        )

        extracted_data = await self.extractor.extract_from_text(
            raw_text=parsed_doc.clean_text,
            doc_type=parsed_doc.doc_type.value,
        )

        # Merge extracted data
        self._apply_extracted_updates(student, extracted_data)

        # Update document tracking status
        doc_item = DocumentItem(
            uploaded=True,
            quality=DocumentQuality.EXCELLENT if parsed_doc.char_count > 200 else DocumentQuality.GOOD,
            confidence=0.95,
            filename=filename,
            file_path=file_path,
        )

        if parsed_doc.doc_type == DocumentType.CV:
            student.documents.cv = doc_item
        elif parsed_doc.doc_type == DocumentType.TRANSCRIPT:
            student.documents.transcript = doc_item
        elif parsed_doc.doc_type == DocumentType.IELTS_CERTIFICATE:
            student.documents.ielts_certificate = doc_item
        elif parsed_doc.doc_type == DocumentType.MOTIVATION_LETTER:
            student.documents.motivation_letter = doc_item
        elif parsed_doc.doc_type == DocumentType.RECOMMENDATION_LETTER:
            student.documents.recommendation_letters_count += 1
        elif parsed_doc.doc_type == DocumentType.FINANCIAL_DOCUMENT:
            student.documents.financial_documents = doc_item
        elif parsed_doc.doc_type == DocumentType.PASSPORT:
            student.documents.passport = doc_item

        # Validate & Enrich
        student = self.validator.validate_and_enrich(student)

        # Save to SQLite
        await self.session_store.save_student_profile(student)

        self._emit_event(
            student,
            AgentEventType.PROFILE_UPDATED,
            {
                "student_name": student.personal.name,
                "completeness": student.profile_completeness,
                "field_of_study": student.academic.field_of_study,
                "gpa_percentage": student.academic.gpa_percentage,
                "missing_required": student.missing_required,
            },
            EventSeverity.SUCCESS,
            event_callback,
        )

        return student

    async def generate_next_interview_question(self, student: StudentProfile) -> str:
        """
        Dynamically formulates the single most important follow-up question to complete the student's profile.
        """
        student = self.validator.validate_and_enrich(student)

        if "Academic Marks / GPA" in student.missing_required:
            return "What are your latest educational marks or GPA (e.g. 85% in FSc/ICS or 3.7 CGPA in BS)?"

        if "Current Field of Study" in student.missing_required:
            return "What is your current or most recent field of study (e.g. Pre-Engineering, Computer Science, BBA)?"

        if "Target Degree Level" in student.missing_required:
            return "Which degree level are you aiming to apply for abroad (Bachelor's, Master's, or PhD)?"

        if "Target Fields of Study" in student.missing_required:
            return "Which specific subject or field do you want to study (e.g. Artificial Intelligence, Data Science, Mechanical Engineering)?"

        if "IELTS / English Test Certificate" in student.missing_optional:
            return "Do you have an IELTS/TOEFL score, or does your university provide an English Medium of Instruction (MOI) certificate?"

        if student.profile_completeness >= 80:
            return "Your profile looks great and is ready for scholarship matching! Shall we start the Discovery Mission across all 5 global regions?"

        return "Could you tell me your preferred study destinations (e.g. Germany, China, USA, Turkey, Australia)?"

    async def process_student_message(
        self,
        student: StudentProfile,
        user_message: str,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> Tuple[str, StudentProfile]:
        """
        Processes a multi-turn student chat message, extracts updates, enriches profile, and saves state.
        """
        llm_response = await self.extractor.extract_profile_updates_from_chat(
            chat_message=user_message,
            current_profile_summary=student.model_dump(),
        )

        updates = llm_response.get("extracted_updates", {})
        if updates:
            self._apply_extracted_updates(student, updates)

        student = self.validator.validate_and_enrich(student)
        await self.session_store.save_student_profile(student)

        self._emit_event(
            student,
            AgentEventType.PROFILE_UPDATED,
            {
                "completeness": student.profile_completeness,
                "missing_required": student.missing_required,
            },
            EventSeverity.INFO,
            event_callback,
        )

        assistant_reply = llm_response.get("assistant_reply", "")
        if not assistant_reply:
            assistant_reply = await self.generate_next_interview_question(student)

        return assistant_reply, student
