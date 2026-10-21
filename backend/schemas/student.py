from enum import Enum
from typing import Any, Dict, List, Optional
import uuid
from pydantic import BaseModel, Field, field_validator, model_validator


class EducationLevel(str, Enum):
    MATRIC = "Matric / SSC"
    INTERMEDIATE = "Intermediate / ICS / FSc / FA"
    BACHELORS = "Bachelor's / BS / BE / BBA"
    MASTERS = "Master's / MS / MSc / MPhil"
    PHD = "PhD / Doctorate"


class EnglishTestType(str, Enum):
    IELTS = "IELTS"
    TOEFL = "TOEFL"
    DUOLINGO = "Duolingo"
    PTE = "PTE Academic"
    MOI = "Medium of Instruction (MOI) Certificate"
    NONE = "None / Not Available"


class DocumentQuality(str, Enum):
    EXCELLENT = "EXCELLENT"
    GOOD = "GOOD"
    FAIR = "FAIR"
    POOR = "POOR"
    CORRUPTED = "CORRUPTED"


class EducationSystem(str, Enum):
    PAKISTANI_HSSC = "PAKISTANI_HSSC"  # Matric / FSc / ICS / Pre-Medical / Pre-Engineering
    CAMBRIDGE = "CAMBRIDGE"            # Cambridge O / A-Levels / IGCSE
    AMERICAN_DIPLOMA = "AMERICAN_DIPLOMA" # High School Diploma
    IB = "IB"                          # International Baccalaureate


class PersonalInfo(BaseModel):
    name: str = Field(default="Student", description="Full name of student")
    nationality: str = Field(default="PK", description="ISO 2-letter country code")
    country_of_residence: str = Field(default="PK", description="Current country of residence")
    city: str = Field(default="Lahore", description="City of residence in Pakistan")
    province: str = Field(default="Punjab", description="Province (Punjab, Sindh, KPK, Balochistan, GB, AJK, ICT)")
    age: int = Field(default=19, ge=14, le=60, description="Age in years")
    date_of_birth: Optional[str] = Field(default=None, description="YYYY-MM-DD")
    gender: Optional[str] = Field(default="Unspecified", description="Gender identity")
    cnic: Optional[str] = Field(default=None, description="Pakistani National Identity Card format XXXXX-XXXXXXX-X")
    passport_number: Optional[str] = Field(default=None, description="Passport number")
    passport_valid_until: Optional[str] = Field(default=None, description="Passport expiry date YYYY-MM-DD")

    @model_validator(mode="before")
    @classmethod
    def normalize_personal_fields(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "city" not in data and "current_city" in data:
                data["city"] = data["current_city"]
        return data


class AcademicRecord(BaseModel):
    current_level: EducationLevel = Field(default=EducationLevel.INTERMEDIATE)
    education_system: EducationSystem = Field(default=EducationSystem.PAKISTANI_HSSC, description="Education system stream")
    years_of_education: int = Field(default=12, description="Total completed years of education (12=Inter/A-Levels, 16=BS)")
    field_of_study: str = Field(default="Computer Science", description="Current or completed major")
    a_level_grades: Optional[List[str]] = Field(default=None, description="Cambridge A-Level letter grades, e.g. ['A*', 'A', 'A']")
    o_level_grades: Optional[List[str]] = Field(default=None, description="Cambridge O-Level letter grades, e.g. ['A*', 'A*', 'A', ...]")
    ibcc_equivalence_percentage: Optional[float] = Field(default=None, description="Calculated IBCC equivalence percentage")
    ibcc_total_marks: Optional[int] = Field(default=None, description="Calculated IBCC marks out of 1100 (or 300)")
    board_university: str = Field(
        default="Federal Board of Intermediate and Secondary Education (FBISE) / BISE",
        description="BISE / FBISE Board or HEC Recognized University"
    )
    gpa_percentage: float = Field(default=93.0, ge=0.0, le=100.0, description="Marks percentage (e.g. 93.0%)")
    gpa_4_scale: float = Field(default=3.72, ge=0.0, le=4.0, description="Converted GPA on 4.0 scale (100% = 4.0, 93% = 3.72)")
    uk_classification: Optional[str] = Field(default="First Class", description="First Class, 2:1, 2:2, etc.")
    institution: str = Field(default="", description="School, College, or University name")
    graduation_year: int = Field(default=2026, description="Year of passing or expected graduation")
    subjects: List[str] = Field(default_factory=list, description="Core subjects studied")
    relevant_courses: List[str] = Field(default_factory=list, description="Specific relevant coursework")
    gap_years: int = Field(default=0, ge=0, description="Number of gap years after latest degree")
    hec_attestation_done: bool = Field(default=False, description="Whether degrees are HEC attested")
    ibcc_equivalence_done: bool = Field(default=False, description="Whether IBCC equivalence certificate is issued")

    @model_validator(mode="before")
    @classmethod
    def sync_gpa_defaults(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "gpa_percentage" in data and float(data.get("gpa_percentage") or 0.0) == 0.0 and "gpa_4_scale" not in data:
                data["gpa_4_scale"] = 0.0
            elif "gpa_4_scale" in data and float(data.get("gpa_4_scale") or 0.0) == 0.0 and "gpa_percentage" not in data:
                data["gpa_percentage"] = 0.0
        return data

    @field_validator("education_system", mode="before")
    @classmethod
    def normalize_education_system(cls, v):
        if v is None:
            return EducationSystem.PAKISTANI_HSSC
        if isinstance(v, EducationSystem):
            return v
        s = str(v).strip().lower()
        if any(k in s for k in ["cambridge", "a-level", "a_level", "o-level", "o_level", "igcse", "gce"]):
            return EducationSystem.CAMBRIDGE
        if "american" in s or "diploma" in s:
            return EducationSystem.AMERICAN_DIPLOMA
        if "ib" in s or "baccalaureate" in s:
            return EducationSystem.IB
        return EducationSystem.PAKISTANI_HSSC

    @field_validator("current_level", mode="before")
    @classmethod
    def normalize_current_level(cls, v):
        if v is None:
            return EducationLevel.INTERMEDIATE
        if isinstance(v, EducationLevel):
            return v
        s = str(v).strip().lower()
        if any(k in s for k in ["inter", "ics", "fsc", "fa", "hssc", "12"]):
            return EducationLevel.INTERMEDIATE
        if any(k in s for k in ["matric", "ssc", "10"]):
            return EducationLevel.MATRIC
        if any(k in s for k in ["bachelor", "bs", "be", "bba", "undergrad", "16"]):
            return EducationLevel.BACHELORS
        if any(k in s for k in ["master", "ms", "msc", "mphil", "postgrad", "18"]):
            return EducationLevel.MASTERS
        if any(k in s for k in ["phd", "doctor"]):
            return EducationLevel.PHD
        return EducationLevel.INTERMEDIATE


class LanguageProficiency(BaseModel):
    english_proficiency_test: EnglishTestType = Field(default=EnglishTestType.NONE)
    ielts_overall: Optional[float] = Field(default=None, ge=0.0, le=9.0)
    ielts_subbands: Optional[Dict[str, Optional[float]]] = Field(default_factory=dict, description="L, R, W, S scores")
    toefl_score: Optional[int] = Field(default=None, ge=0, le=120)
    duolingo_score: Optional[int] = Field(default=None, ge=0, le=160)
    medium_of_instruction_english: bool = Field(default=True, description="Was degree instruction in English?")
    moi_certificate_available: bool = Field(default=False, description="Has English Proficiency / MOI certificate")
    native_languages: List[str] = Field(default_factory=lambda: ["Urdu", "English"])
    has_english_test: bool = Field(default=False, description="Flag indicating valid test score available")

    @field_validator("english_proficiency_test", mode="before")
    @classmethod
    def normalize_english_test(cls, v):
        if v is None:
            return EnglishTestType.NONE
        if isinstance(v, EnglishTestType):
            return v
        s = str(v).strip().lower()
        if any(k in s for k in ["none", "not available", "no english", "in progress", "exempt", "na", "n/a", "no", "without"]):
            return EnglishTestType.NONE
        if "ielts" in s:
            return EnglishTestType.IELTS
        if "toefl" in s:
            return EnglishTestType.TOEFL
        if "duolingo" in s:
            return EnglishTestType.DUOLINGO
        if "pte" in s:
            return EnglishTestType.PTE
        if "moi" in s or "medium of instruction" in s:
            return EnglishTestType.MOI
        return EnglishTestType.NONE


class StandardizedTests(BaseModel):
    hec_hat: Optional[float] = Field(default=None, description="HEC Higher Education Aptitude Test score")
    hec_usat: Optional[float] = Field(default=None, description="HEC Undergrad Studies Admission Test score")
    gre: Optional[int] = Field(default=None, description="GRE General score (260-340)")
    sat: Optional[int] = Field(default=None, description="SAT score (400-1600)")
    gat_general: Optional[float] = Field(default=None, description="NTS GAT General score")
    gat_subject: Optional[float] = Field(default=None, description="NTS GAT Subject score")
    nts_nat: Optional[float] = Field(default=None, description="NTS National Aptitude Test score")


class Preferences(BaseModel):
    target_degree_level: str = Field(default="Bachelor's", description="Target degree (Bachelor's, Master's, PhD)")
    target_fields: List[str] = Field(default_factory=lambda: ["Computer Science", "Artificial Intelligence"])
    funding_requirement: str = Field(default="FULL", description="FULL, TUITION_ONLY, PARTIAL")
    budget_tier: str = Field(default="LOW", description="LOW, MODERATE, HIGH")
    max_out_of_pocket_pkr: int = Field(default=150000, description="Maximum upfront spending capacity in PKR")
    is_tax_filer: bool = Field(default=True, description="Whether student/sponsor is an active tax filer under FBR (affects card WHT)")
    willing_to_relocate: bool = Field(default=True)
    preferred_regions: List[str] = Field(default_factory=list, description="Europe, Asia, Americas, MENA, Oceania")
    excluded_regions: List[str] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list, description="E.g. No large bank statement proof")


class DocumentItem(BaseModel):
    uploaded: bool = False
    quality: Optional[DocumentQuality] = None
    confidence: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    filename: Optional[str] = None
    file_path: Optional[str] = None
    extraction_notes: Optional[str] = None


class DocumentsUploaded(BaseModel):
    transcript: DocumentItem = Field(default_factory=DocumentItem)
    cv: DocumentItem = Field(default_factory=DocumentItem)
    passport: DocumentItem = Field(default_factory=DocumentItem)
    ielts_certificate: DocumentItem = Field(default_factory=DocumentItem)
    motivation_letter: DocumentItem = Field(default_factory=DocumentItem)
    recommendation_letters_count: int = 0
    financial_documents: DocumentItem = Field(default_factory=DocumentItem)
    police_clearance: DocumentItem = Field(default_factory=DocumentItem)
    medical_certificate: DocumentItem = Field(default_factory=DocumentItem)
    hec_attestation: DocumentItem = Field(default_factory=DocumentItem)
    ibcc_equivalence: DocumentItem = Field(default_factory=DocumentItem)


class StudentProfile(BaseModel):
    student_id: Optional[str] = Field(default_factory=lambda: f"std-{uuid.uuid4().hex[:8]}", description="Unique UUID for the student")
    session_id: Optional[str] = Field(default=None, description="Active session UUID")
    personal: PersonalInfo = Field(default_factory=PersonalInfo)
    academic: AcademicRecord = Field(default_factory=AcademicRecord)
    language: LanguageProficiency = Field(default_factory=LanguageProficiency)
    standardized_tests: StandardizedTests = Field(default_factory=StandardizedTests)
    preferences: Preferences = Field(default_factory=Preferences)
    documents: DocumentsUploaded = Field(default_factory=DocumentsUploaded)
    
    # Meta extraction fields
    profile_completeness: int = Field(default=0, ge=0, le=100, description="Completeness percentage")
    missing_required: List[str] = Field(default_factory=list, description="Mandatory missing fields/docs")
    missing_optional: List[str] = Field(default_factory=list, description="Optional missing docs (IELTS, etc.)")
    extraction_warnings: List[str] = Field(default_factory=list, description="Discrepancies found")

    @model_validator(mode="before")
    @classmethod
    def normalize_frontend_profile(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data
        
        personal = data.get("personal")
        preferences = data.get("preferences") or {}
        financial = data.get("financial") or {}
        academic = data.get("academic") or {}
        language = data.get("language") or {}

        if isinstance(personal, dict):
            # 1. city alias
            if "city" not in personal and "current_city" in personal:
                personal["city"] = personal["current_city"]
            
            # 2. intended_degree -> preferences.target_degree_level
            if "intended_degree" in personal and "target_degree_level" not in preferences:
                preferences["target_degree_level"] = personal["intended_degree"]
            
            # 3. target_fields -> preferences.target_fields
            if "target_fields" in personal and ("target_fields" not in preferences or not preferences["target_fields"]):
                preferences["target_fields"] = personal["target_fields"]

            # 4. target_regions -> preferences.preferred_regions
            if "target_regions" in personal and ("preferred_regions" not in preferences or not preferences["preferred_regions"]):
                preferences["preferred_regions"] = personal["target_regions"]

        if isinstance(financial, dict):
            # 5. financial.max_out_of_pocket_pkr -> preferences.max_out_of_pocket_pkr
            if "max_out_of_pocket_pkr" in financial and "max_out_of_pocket_pkr" not in preferences:
                preferences["max_out_of_pocket_pkr"] = financial["max_out_of_pocket_pkr"]
            if "funding_requirement" in financial and "funding_requirement" not in preferences:
                preferences["funding_requirement"] = financial["funding_requirement"]

        if isinstance(language, dict):
            # 6. language.test_type -> english_proficiency_test
            if "test_type" in language and "english_proficiency_test" not in language:
                language["english_proficiency_test"] = language["test_type"]
            # 7. language.overall_score -> ielts_overall
            if "overall_score" in language and language.get("overall_score") is not None and "ielts_overall" not in language:
                language["ielts_overall"] = language["overall_score"]
            if "has_english_medium_certificate" in language and "moi_certificate_available" not in language:
                language["moi_certificate_available"] = bool(language["has_english_medium_certificate"])

        if isinstance(academic, dict):
            # 8. academic.degree_level -> current_level
            if "degree_level" in academic and "current_level" not in academic:
                academic["current_level"] = academic["degree_level"]
            # 9. academic.gpa_obtained -> gpa_4_scale if <= 4.0
            if "gpa_obtained" in academic and academic.get("gpa_obtained") is not None:
                try:
                    val = float(academic["gpa_obtained"])
                    if val <= 4.0 and "gpa_4_scale" not in academic:
                        academic["gpa_4_scale"] = val
                except (ValueError, TypeError):
                    pass
            # 10. academic.percentage -> gpa_percentage
            if "percentage" in academic and academic.get("percentage") is not None and "gpa_percentage" not in academic:
                try:
                    academic["gpa_percentage"] = float(academic["percentage"])
                except (ValueError, TypeError):
                    pass
            # 11. Cambridge O/A-Levels
            if "a_level_grades" in academic and academic["a_level_grades"]:
                academic["education_system"] = EducationSystem.CAMBRIDGE

        if personal is not None:
            data["personal"] = personal
        if preferences:
            data["preferences"] = preferences
        if academic is not None:
            data["academic"] = academic
        if language is not None:
            data["language"] = language

        return data
