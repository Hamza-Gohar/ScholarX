import io
import os
import re
import logging
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from pypdf import PdfReader
from docx import Document

logger = logging.getLogger("scholarx.tools.doc_parser")


class DocumentType(str, Enum):
    CV = "CV"
    TRANSCRIPT = "TRANSCRIPT"
    IELTS_CERTIFICATE = "IELTS_CERTIFICATE"
    MOTIVATION_LETTER = "MOTIVATION_LETTER"
    RECOMMENDATION_LETTER = "RECOMMENDATION_LETTER"
    FINANCIAL_DOCUMENT = "FINANCIAL_DOCUMENT"
    PASSPORT = "PASSPORT"
    OTHER = "OTHER"


class ParsedDocument(BaseModel):
    filename: str = Field(default="")
    doc_type: DocumentType = Field(default=DocumentType.OTHER)
    raw_text: str = Field(default="")
    clean_text: str = Field(default="")
    page_count: int = Field(default=1)
    char_count: int = Field(default=0)
    is_valid: bool = Field(default=True)
    error: Optional[str] = None


class DocumentParserTool:
    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        """Normalizes extracted text by removing control characters, excessive blank lines, and normalizing whitespace."""
        if not text:
            return ""
        # Normalize carriage returns and tabs
        text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\t", " ")
        # Remove consecutive blank lines
        text = re.sub(r"\n\s*\n+", "\n\n", text)
        # Normalize multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)
        return text.strip()

    def classify_document(self, text: str) -> DocumentType:
        """Heuristic-based document type classifier with keyword weighting."""
        lower = text.lower()

        # 1. IELTS / Language Test
        if any(kw in lower for kw in [
            "ielts", "test report form", "overall band score", "listening",
            "reading", "writing", "speaking", "toefl", "duolingo english test", "cefr"
        ]):
            if "band score" in lower or "test report form" in lower or "ielts" in lower:
                return DocumentType.IELTS_CERTIFICATE

        # 2. Academic Transcript
        if any(kw in lower for kw in [
            "transcript of records", "academic transcript", "cumulative grade point average",
            "cgpa", "credit hours", "semester", "course code", "marks breakdown",
            "board of intermediate", "secondary education", "hec recognized"
        ]):
            return DocumentType.TRANSCRIPT

        # 3. Statement of Purpose / Motivation Letter
        if any(kw in lower for kw in [
            "statement of purpose", "letter of motivation", "motivation letter",
            "personal statement", "why i want to apply", "aspirations", "future goals"
        ]):
            return DocumentType.MOTIVATION_LETTER

        # 4. Letter of Recommendation
        if any(kw in lower for kw in [
            "letter of recommendation", "reference letter", "recommendation letter",
            "i am pleased to recommend", "strongly recommend", "to whom it may concern"
        ]):
            return DocumentType.RECOMMENDATION_LETTER

        # 5. Financial Document / Bank Statement
        if any(kw in lower for kw in [
            "bank statement", "account balance", "closing balance", "financial affidavit",
            "bank alfalah", "hbl", "mcb", "ubl", "national bank of pakistan"
        ]):
            return DocumentType.FINANCIAL_DOCUMENT

        # 6. Passport / Identity
        if any(kw in lower for kw in [
            "passport", "islamic republic of pakistan", "national identity card", "cnic"
        ]):
            return DocumentType.PASSPORT

        # 7. CV / Resume
        if any(kw in lower for kw in [
            "curriculum vitae", "resume", "experience", "education",
            "skills", "projects", "technical skills", "work experience"
        ]):
            return DocumentType.CV

        return DocumentType.OTHER

    def parse_pdf(self, file_path_or_bytes) -> ParsedDocument:
        try:
            reader = PdfReader(file_path_or_bytes)
            pages_text = []
            for i, page in enumerate(reader.pages):
                extracted = page.extract_text()
                if extracted:
                    pages_text.append(extracted)

            raw = "\n\n--- PAGE BREAK ---\n\n".join(pages_text) if pages_text else ""
            cleaned = self.clean_text(raw)
            doc_type = self.classify_document(cleaned)

            return ParsedDocument(
                filename=getattr(file_path_or_bytes, "name", str(file_path_or_bytes)),
                doc_type=doc_type,
                raw_text=raw,
                clean_text=cleaned,
                page_count=max(1, len(reader.pages)),
                char_count=len(cleaned),
                is_valid=True,
            )
        except Exception as e:
            logger.error(f"Failed to parse PDF: {e}")
            return ParsedDocument(
                filename=str(file_path_or_bytes),
                doc_type=DocumentType.OTHER,
                is_valid=False,
                error=str(e),
            )

    def parse_docx(self, file_path_or_bytes) -> ParsedDocument:
        try:
            doc = Document(file_path_or_bytes)
            text_blocks = []

            # Paragraphs
            for p in doc.paragraphs:
                if p.text.strip():
                    text_blocks.append(p.text.strip())

            # Tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = [cell.text.strip() for cell in row.cells if cell.text.strip()]
                    if row_text:
                        text_blocks.append(" | ".join(row_text))

            raw = "\n".join(text_blocks)
            cleaned = self.clean_text(raw)
            doc_type = self.classify_document(cleaned)

            return ParsedDocument(
                filename=getattr(file_path_or_bytes, "name", str(file_path_or_bytes)),
                doc_type=doc_type,
                raw_text=raw,
                clean_text=cleaned,
                page_count=1,
                char_count=len(cleaned),
                is_valid=True,
            )
        except Exception as e:
            logger.error(f"Failed to parse DOCX: {e}")
            return ParsedDocument(
                filename=str(file_path_or_bytes),
                doc_type=DocumentType.OTHER,
                is_valid=False,
                error=str(e),
            )

    def parse_text(self, text: str, filename: str = "document.txt") -> ParsedDocument:
        cleaned = self.clean_text(text)
        doc_type = self.classify_document(cleaned)
        return ParsedDocument(
            filename=filename,
            doc_type=doc_type,
            raw_text=text,
            clean_text=cleaned,
            page_count=1,
            char_count=len(cleaned),
            is_valid=True,
        )

    def parse_file(self, file_path: str) -> ParsedDocument:
        if not os.path.exists(file_path):
            return ParsedDocument(
                filename=file_path,
                doc_type=DocumentType.OTHER,
                is_valid=False,
                error=f"File not found: {file_path}",
            )

        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".pdf":
            return self.parse_pdf(file_path)
        elif ext in (".docx", ".doc"):
            return self.parse_docx(file_path)
        elif ext in (".txt", ".md", ".json"):
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                return self.parse_text(content, filename=file_path)
            except Exception as e:
                return ParsedDocument(
                    filename=file_path,
                    doc_type=DocumentType.OTHER,
                    is_valid=False,
                    error=str(e),
                )
        else:
            return ParsedDocument(
                filename=file_path,
                doc_type=DocumentType.OTHER,
                is_valid=False,
                error=f"Unsupported file format: {ext}",
            )
