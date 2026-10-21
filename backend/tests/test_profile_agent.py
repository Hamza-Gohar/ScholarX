import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from agents.profile_agent import ProfileAgent
from schemas.events import AgentEventType, ScholarXEvent
from schemas.student import StudentProfile, EducationLevel, EnglishTestType
from tools.document_parser import ParsedDocument, DocumentType


@pytest.fixture
def empty_student():
    return StudentProfile(
        student_id="std-agent-01",
        session_id="sess-agent-01",
        academic={"field_of_study": "", "gpa_percentage": 0.0},
        preferences={"target_degree_level": ""},
    )


@pytest.mark.asyncio
async def test_profile_agent_document_ingestion(empty_student):
    agent = ProfileAgent()
    events = []

    def on_event(e: ScholarXEvent):
        events.append(e)

    mock_parsed_doc = ParsedDocument(
        filename="Hamza_CV.pdf",
        doc_type=DocumentType.CV,
        raw_text="Hamza Tariq\nBS Computer Science at FAST NUCES\nCGPA: 3.82 / 85%\nIELTS: 7.5\nTarget: Master's in AI",
        clean_text="Hamza Tariq\nBS Computer Science at FAST NUCES\nCGPA: 3.82 / 85%\nIELTS: 7.5\nTarget: Master's in AI",
        page_count=2,
        char_count=120,
        is_valid=True,
    )

    mock_extracted_data = {
        "personal": {"name": "Hamza Tariq", "city": "Lahore"},
        "academic": {
            "current_level": "Bachelor's / BS / BE / BBA",
            "field_of_study": "Computer Science",
            "board_university": "FAST-NUCES",
            "gpa_percentage": 85.0,
            "gpa_4_scale": 3.82,
        },
        "language": {
            "english_proficiency_test": "IELTS",
            "ielts_overall": 7.5,
            "has_english_test": True,
        },
        "preferences": {
            "target_degree_level": "Master's",
            "target_fields": ["Artificial Intelligence"],
        },
    }

    agent.parser.parse_file = MagicMock(return_value=mock_parsed_doc)
    agent.extractor.extract_from_text = AsyncMock(return_value=mock_extracted_data)

    with patch.object(agent.session_store, "save_student_profile", new_callable=AsyncMock) as mock_save:
        updated_profile = await agent.ingest_document(
            student=empty_student,
            file_path="/tmp/Hamza_CV.pdf",
            event_callback=on_event,
        )

        assert updated_profile.personal.name == "Hamza Tariq"
        assert updated_profile.academic.field_of_study == "Computer Science"
        assert updated_profile.academic.gpa_percentage == 85.0
        assert updated_profile.language.ielts_overall == 7.5
        assert updated_profile.documents.cv.uploaded is True
        assert updated_profile.profile_completeness > 50

        mock_save.assert_called_once()

        event_types = [e.event_type for e in events]
        assert AgentEventType.DOCUMENT_UPLOADED in event_types
        assert AgentEventType.DOCUMENT_PARSED in event_types
        assert AgentEventType.PROFILE_UPDATED in event_types


@pytest.mark.asyncio
async def test_profile_agent_conversational_question_generation():
    agent = ProfileAgent()

    # Profile missing GPA and target degree level
    student = StudentProfile(
        student_id="std-missing",
        session_id="sess-missing",
        personal={"name": "Zainab"},
        academic={"field_of_study": "Pre-Engineering", "gpa_percentage": 0.0},
        preferences={"target_degree_level": ""},
    )

    question = await agent.generate_next_interview_question(student)
    assert len(question) > 10
    # Should ask for marks/GPA or degree
    assert any(kw in question.lower() for kw in ["marks", "gpa", "percentage", "degree", "target", "grade"])


@pytest.mark.asyncio
async def test_profile_agent_process_chat_message():
    agent = ProfileAgent()

    student = StudentProfile(
        student_id="std-chat",
        session_id="sess-chat",
        personal={"name": "Usman"},
        academic={"field_of_study": "Electrical Engineering", "gpa_percentage": 0.0},
        preferences={"target_degree_level": ""},
    )

    mock_llm_response = {
        "extracted_updates": {
            "academic": {"gpa_percentage": 82.5, "current_level": "Bachelor's / BS / BE / BBA"},
            "preferences": {"target_degree_level": "Master's", "preferred_regions": ["Europe"]},
        },
        "assistant_reply": "Got it! 82.5% in Electrical Engineering aiming for a Master's in Europe.",
    }

    agent.extractor.extract_profile_updates_from_chat = AsyncMock(return_value=mock_llm_response)

    with patch.object(agent.session_store, "save_student_profile", new_callable=AsyncMock):
        reply, updated_profile = await agent.process_student_message(
            student=student,
            user_message="I have completed my BS in Electrical Engineering with 82.5% marks and want to apply for Master's in Europe.",
        )

        assert "82.5%" in reply or "Master's" in reply
        assert updated_profile.academic.gpa_percentage == 82.5
        assert updated_profile.preferences.target_degree_level == "Master's"
