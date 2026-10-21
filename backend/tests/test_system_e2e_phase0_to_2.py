import os
import tempfile
import pytest
from unittest.mock import AsyncMock, patch
from docx import Document
from pypdf import PdfWriter

from db.session_store import get_session_store
from schemas.events import AgentEventType, ScholarXEvent
from schemas.scholarship import Scholarship, ScholarshipStatus
from schemas.student import StudentProfile, EducationLevel, EnglishTestType
from tools.document_parser import DocumentParserTool, DocumentType, ParsedDocument
from agents.profile_agent import ProfileAgent
from agents.discovery_commander import DiscoveryCommander


@pytest.mark.asyncio
async def test_full_system_pipeline_phase0_to_phase2():
    """
    MASTER END-TO-END SYSTEM TEST (Phase 0 -> Phase 1 -> Phase 2):
    --------------------------------------------------------------
    1. Phase 0: SQLite Session Store initialized with seeded 205 scholarships.
    2. Phase 1 (Intake): Student uploads CV (.pdf) and Statement (.docx).
    3. Phase 1 (Parsing & Extraction): DocumentParser & Extractor extract academic & IELTS records.
    4. Phase 1 (Validation & Enrichment): ProfileValidator computes GPA, UK class, and completeness.
    5. Phase 1 (Chat Intake): Student refines preferences via conversational ProfileAgent.
    6. Phase 2 (Discovery): DiscoveryCommander orchestrates all 5 Regional Scouts.
    7. Phase 2 (Aggregation & Dedup): Merges cached 205 scholarships with scout discoveries.
    8. Verification: Event stream validity and tailored scholarship candidates.
    """
    session_store = get_session_store()
    profile_agent = ProfileAgent()
    discovery_commander = DiscoveryCommander()

    session_id = "sess-master-sys-test-01"
    student_id = "std-master-sys-test-01"

    # Track all system events across the entire lifecycle
    system_event_log = []
    def record_event(evt: ScholarXEvent):
        system_event_log.append(evt)

    # -------------------------------------------------------------
    # STEP 1: Create Blank Student Session in Local SQLite
    # -------------------------------------------------------------
    student = StudentProfile(
        student_id=student_id,
        session_id=session_id,
    )
    await session_store.save_student_profile(student)
    loaded_profile = await session_store.get_student_profile(session_id)
    assert loaded_profile is not None
    assert loaded_profile.student_id == student_id

    # -------------------------------------------------------------
    # STEP 2: Create Realistic Pakistani Student Documents
    # -------------------------------------------------------------
    # Document A: Academic Transcript (PDF)
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_pdf:
        pdf_path = tmp_pdf.name
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)
        with open(pdf_path, "wb") as f:
            writer.write(f)

    # Document B: Statement of Purpose (DOCX)
    doc = Document()
    doc.add_heading("Statement of Purpose - Master's in Computer Science", 0)
    doc.add_paragraph("My name is Muhammad Ali from Lahore, Pakistan. I graduated in Software Engineering with 84% marks.")
    doc.add_paragraph("I scored 7.5 in IELTS Academic and wish to pursue research in Distributed Systems.")
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp_docx:
        docx_path = tmp_docx.name
        doc.save(docx_path)

    try:
        # Mock Extractor output for PDF Transcript
        mock_transcript_extraction = {
            "personal": {"name": "Muhammad Ali", "city": "Lahore", "province": "Punjab", "nationality": "PK"},
            "academic": {
                "current_level": "Bachelor's / BS / BE / BBA",
                "field_of_study": "Software Engineering",
                "board_university": "University of Engineering and Technology (UET) Lahore",
                "gpa_percentage": 84.0,
                "gpa_4_scale": 3.75,
                "graduation_year": 2026,
            },
            "language": {
                "english_proficiency_test": "IELTS",
                "ielts_overall": 7.5,
                "ielts_subbands": {"L": 8.0, "R": 8.0, "W": 7.0, "S": 7.0},
                "has_english_test": True,
            },
        }

        mock_parsed_transcript = ParsedDocument(
            filename="UET_Transcript.pdf",
            doc_type=DocumentType.TRANSCRIPT,
            raw_text="Official Academic Transcript of Records UET Lahore Software Engineering 84%",
            clean_text="Official Academic Transcript of Records UET Lahore Software Engineering 84%",
            page_count=2,
            char_count=250,
            is_valid=True,
        )

        with patch.object(profile_agent.parser, "parse_file", return_value=mock_parsed_transcript):
            with patch.object(profile_agent.extractor, "extract_from_text", new_callable=AsyncMock) as mock_extract:
                mock_extract.return_value = mock_transcript_extraction

                # -------------------------------------------------------------
                # STEP 3: Ingest Transcript into Profile Agent
                # -------------------------------------------------------------
                student = await profile_agent.ingest_document(
                    student=student,
                    file_path=pdf_path,
                    event_callback=record_event,
                )

            assert student.personal.name == "Muhammad Ali"
            assert student.personal.city == "Lahore"
            assert student.academic.field_of_study == "Software Engineering"
            assert student.academic.gpa_percentage == 84.0
            assert student.language.ielts_overall == 7.5
            assert student.academic.gpa_4_scale >= 3.7
            assert "First Class" in student.academic.uk_classification
            assert student.documents.transcript.uploaded is True

        # -------------------------------------------------------------
        # STEP 4: Chat Intake to finalize preferences
        # -------------------------------------------------------------
        mock_chat_extraction = {
            "extracted_updates": {
                "preferences": {
                    "target_degree_level": "Master's",
                    "target_fields": ["Computer Science", "Artificial Intelligence"],
                    "preferred_regions": ["Europe", "Asia", "Americas", "MENA", "Oceania"],
                    "funding_requirement": "FULL",
                    "max_out_of_pocket_pkr": 100000,
                }
            },
            "assistant_reply": "Excellent Muhammad Ali! Your profile is verified with 84% marks and IELTS 7.5. Let's find fully funded Master's programs.",
        }

        with patch.object(profile_agent.extractor, "extract_profile_updates_from_chat", new_callable=AsyncMock) as mock_chat:
            mock_chat.return_value = mock_chat_extraction

            reply, student = await profile_agent.process_student_message(
                student=student,
                user_message="I want to apply for a fully funded Master's in Computer Science and AI in Europe, Asia, or USA with minimum out of pocket expense.",
                event_callback=record_event,
            )

            assert "Muhammad Ali" in reply
            assert student.preferences.target_degree_level == "Master's"
            assert "Computer Science" in student.preferences.target_fields
            assert student.profile_completeness >= 85
            assert len(student.missing_required) == 0

        # Verify profile is persisted in SQLite
        persisted_student = await session_store.get_student_profile(session_id)
        assert persisted_student is not None
        assert persisted_student.personal.name == "Muhammad Ali"
        assert persisted_student.profile_completeness >= 85

        # -------------------------------------------------------------
        # STEP 5: Phase 2 Discovery Mission Orchestration
        # -------------------------------------------------------------
        # Check that pre-seeded knowledge base has 200+ verified scholarships
        cached_scholarships = await session_store.get_all_cached_scholarships()
        assert len(cached_scholarships) >= 200

        # Mock scout live discovery return
        mock_live_scout_return = (
            [
                Scholarship(
                    scholarship_id="SCH-LIVE-EU-01",
                    name="DAAD Development-Related Postgraduate Courses (EPOS Live)",
                    host_country="DE",
                    host_country_name="Germany",
                    region="Europe",
                    source_url="https://daad.de/epos-live",
                    status=ScholarshipStatus.DISCOVERED,
                )
            ],
            [
                ScholarXEvent(
                    session_id=session_id,
                    event_type=AgentEventType.SCOUT_COMPLETE,
                    agent_id="europe_scout",
                )
            ],
        )

        for scout in discovery_commander.scouts.values():
            scout.run = AsyncMock(return_value=mock_live_scout_return)

        candidates = await discovery_commander.execute_discovery_mission(
            student=student,
            event_callback=record_event,
        )

        # -------------------------------------------------------------
        # STEP 6: Verify Candidate Pool & System Events
        # -------------------------------------------------------------
        # 205 seeded database entries deduplicate to 150+ highly distinct institutional opportunities
        assert len(candidates) >= 150
        assert len(cached_scholarships) >= 200
        # Verify continent representation
        regions_found = {sc.region for sc in candidates}
        assert "Europe" in regions_found
        assert "Asia" in regions_found
        assert "Americas" in regions_found
        assert "MENA" in regions_found
        assert "Oceania" in regions_found

        # Verify event sequence
        event_types = [e.event_type for e in system_event_log]
        assert AgentEventType.DOCUMENT_UPLOADED in event_types
        assert AgentEventType.DOCUMENT_PARSED in event_types
        assert AgentEventType.PROFILE_UPDATED in event_types
        assert AgentEventType.SCOUT_DEPLOYED in event_types
        assert AgentEventType.PREVIOUS_RESEARCH_LOADED in event_types
        assert AgentEventType.DISCOVERY_AGGREGATION_COMPLETE in event_types

    finally:
        # Cleanup temporary test files
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        if os.path.exists(docx_path):
            os.remove(docx_path)
