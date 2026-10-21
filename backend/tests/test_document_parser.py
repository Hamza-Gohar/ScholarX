import io
import os
import tempfile
import pytest
from pypdf import PdfWriter
from docx import Document
from tools.document_parser import DocumentParserTool, DocumentType, ParsedDocument


@pytest.fixture
def parser():
    return DocumentParserTool()


def test_parse_plain_text(parser):
    content = """
    # Hamza Tariq - Curriculum Vitae
    Email: hamza@example.com
    Location: Lahore, Pakistan
    
    ## Education
    - FSc Pre-Engineering, Punjab College, Lahore (88%)
    - ICS Computer Science, BISE Lahore
    
    ## Skills
    Python, FastAPI, Machine Learning
    """
    parsed = parser.parse_text(content, filename="resume.txt")
    assert isinstance(parsed, ParsedDocument)
    assert parsed.doc_type == DocumentType.CV
    assert "Hamza Tariq" in parsed.clean_text
    assert parsed.page_count == 1
    assert parsed.char_count > 50


def test_parse_pdf_document(parser):
    # Create an in-memory PDF with 2 pages
    writer = PdfWriter()
    page1_text = "Official Academic Transcript\nBoard of Intermediate and Secondary Education Lahore\nRoll No: 123456\nTotal Marks: 950/1100 (86.36%)\nGrade: A+"
    page2_text = "Subject Marks Breakdown:\nMathematics: 185/200\nPhysics: 170/200\nComputer Science: 190/200"

    # Write to a temporary PDF file
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_pdf:
        tmp_path = tmp_pdf.name

    try:
        # Create a simple valid PDF
        writer.add_blank_page(width=200, height=200)
        writer.add_blank_page(width=200, height=200)
        with open(tmp_path, "wb") as f:
            writer.write(f)

        # For text extraction testing, test with parser.parse_file
        # When blank PDF is parsed, it handles without error
        parsed = parser.parse_file(tmp_path)
        assert isinstance(parsed, ParsedDocument)
        assert parsed.page_count == 2
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def test_parse_docx_document(parser):
    # Create a test DOCX file
    doc = Document()
    doc.add_heading("Statement of Purpose / Motivation Letter", 0)
    doc.add_paragraph("I am applying for the Master's in Computer Science program in Germany.")
    doc.add_paragraph("My research interest lies in Distributed Systems and Autonomous AI Agents.")
    
    # Add a table
    table = doc.add_table(rows=2, cols=2)
    table.cell(0, 0).text = "Target Country"
    table.cell(0, 1).text = "Germany"
    table.cell(1, 0).text = "Degree Level"
    table.cell(1, 1).text = "Master's"

    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp_docx:
        tmp_path = tmp_docx.name

    try:
        doc.save(tmp_path)
        parsed = parser.parse_file(tmp_path)

        assert isinstance(parsed, ParsedDocument)
        assert parsed.doc_type == DocumentType.MOTIVATION_LETTER
        assert "Statement of Purpose" in parsed.clean_text
        assert "Distributed Systems" in parsed.clean_text
        assert "Germany" in parsed.clean_text
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def test_document_classification_heuristics(parser):
    # CV
    assert parser.classify_document("Curriculum Vitae\nExperience:\nSoftware Engineer at Tech Corp\nEducation: BS CS") == DocumentType.CV

    # Transcript
    assert parser.classify_document("Official Academic Transcript of Records\nCumulative Grade Point Average CGPA: 3.82\nCredit Hours: 134") == DocumentType.TRANSCRIPT

    # IELTS
    assert parser.classify_document("International English Language Testing System (IELTS) Test Report Form\nListening: 8.0, Reading: 7.5, Writing: 6.5, Speaking: 7.0, Overall Band Score: 7.5") == DocumentType.IELTS_CERTIFICATE

    # Recommendation Letter
    assert parser.classify_document("Letter of Recommendation\nTo whom it may concern,\nI am pleased to write this reference letter for Hamza Tariq...") == DocumentType.RECOMMENDATION_LETTER

    # Financial Document
    assert parser.classify_document("Bank Account Statement\nBank Alfalah Pakistan\nClosing Available Balance: PKR 3,500,000") == DocumentType.FINANCIAL_DOCUMENT

    # Generic / Other
    assert parser.classify_document("Just some random notes about life and goals.") == DocumentType.OTHER


def test_corrupted_file_handling(parser):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_bad_pdf:
        tmp_bad_pdf.write(b"NOT A REAL PDF FILE CONTENT AT ALL")
        tmp_path = tmp_bad_pdf.name

    try:
        parsed = parser.parse_file(tmp_path)
        # Should gracefully return error state or empty parsed document without crashing
        assert isinstance(parsed, ParsedDocument)
        assert parsed.is_valid is False
        assert parsed.error is not None
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
