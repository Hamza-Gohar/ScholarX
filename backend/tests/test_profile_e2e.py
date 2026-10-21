import pytest
from unittest.mock import AsyncMock, patch
from agents.profile_agent import ProfileAgent
from agents.discovery_commander import DiscoveryCommander
from schemas.events import AgentEventType, ScholarXEvent
from schemas.student import StudentProfile
from tools.document_parser import ParsedDocument, DocumentType


@pytest.mark.asyncio
async def test_profile_intake_to_discovery_handoff():
    """
    Complete E2E integration test:
    1. Student starts intake
    2. Uploads CV / Transcript
    3. Profile Agent ingests & extracts profile
    4. Student provides missing preferences in chat
    5. Final enriched StudentProfile handed off to Discovery Commander for query generation
    """
    profile_agent = ProfileAgent()
    discovery_commander = DiscoveryCommander()

    student = StudentProfile(
        student_id="std-e2e-intake",
        session_id="sess-e2e-intake",
    )

    events = []
    def on_event(e: ScholarXEvent):
        events.append(e)

    # 1. Mock document extraction
    mock_doc = ParsedDocument(
        filename="Bilal_Transcript.pdf",
        doc_type=DocumentType.TRANSCRIPT,
        clean_text="FAST NUCES Islamabad Transcript\nBS Software Engineering\nCGPA 3.65 / 82%\nIELTS 7.0",
        is_valid=True,
    )

    mock_doc_extraction = {
        "personal": {"name": "Bilal Ahmed", "city": "Islamabad", "nationality": "PK"},
        "academic": {
            "current_level": "Bachelor's / BS / BE / BBA",
            "field_of_study": "Software Engineering",
            "board_university": "FAST-NUCES Islamabad",
            "gpa_percentage": 82.0,
            "gpa_4_scale": 3.65,
        },
        "language": {
            "english_proficiency_test": "IELTS",
            "ielts_overall": 7.0,
            "has_english_test": True,
        },
    }

    profile_agent.parser.parse_file = lambda path: mock_doc
    profile_agent.extractor.extract_from_text = AsyncMock(return_value=mock_doc_extraction)

    with patch.object(profile_agent.session_store, "save_student_profile", new_callable=AsyncMock):
        # 2. Ingest document
        student = await profile_agent.ingest_document(
            student=student,
            file_path="/path/to/Bilal_Transcript.pdf",
            event_callback=on_event,
        )

        assert student.personal.name == "Bilal Ahmed"
        assert student.academic.field_of_study == "Software Engineering"
        assert student.documents.transcript.uploaded is True

        # 3. Process conversational follow-up to fill target preferences
        mock_chat_extraction = {
            "extracted_updates": {
                "preferences": {
                    "target_degree_level": "Master's",
                    "target_fields": ["Software Engineering", "Cloud Computing"],
                    "preferred_regions": ["Europe", "Americas"],
                }
            },
            "assistant_reply": "Great! Master's in Cloud Computing in Europe & Americas.",
        }
        profile_agent.extractor.extract_profile_updates_from_chat = AsyncMock(return_value=mock_chat_extraction)

        reply, student = await profile_agent.process_student_message(
            student=student,
            user_message="I want to apply for a fully funded Master's in Cloud Computing in Europe or USA.",
            event_callback=on_event,
        )

        assert student.preferences.target_degree_level == "Master's"
        assert "Cloud Computing" in student.preferences.target_fields
        assert student.profile_completeness >= 80

        # 4. Handoff to Discovery Commander
        scout_queries = discovery_commander.generate_scout_queries(student, region="Europe")
        assert len(scout_queries) >= 2
        assert any("Master" in q for q in scout_queries)
        assert any("Pakistan" in q or "Pakistani" in q for q in scout_queries)
