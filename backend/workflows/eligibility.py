import logging
from typing import Any, Callable, Dict, List, Optional
from pydantic import BaseModel, Field
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.scholarship import FundingType, Scholarship
from schemas.scoring import DimensionScore, DimensionStatus
from schemas.student import StudentProfile, EducationSystem
from utils.gpa_converter import gpa_4_to_percentage
from workflows.degree_matching import is_degree_match
from workflows.field_matching import is_field_match

logger = logging.getLogger("scholarx.workflows.eligibility")


class EligibilityResult(BaseModel):
    scholarship_id: str
    scholarship_name: str
    is_eligible: bool = True
    eligibility_score: float = Field(default=100.0, ge=0.0, le=100.0)
    dimension_results: List[DimensionScore] = Field(default_factory=list)
    blocking_issues: List[str] = Field(default_factory=list)
    action_required: List[str] = Field(default_factory=list)
    pakistan_advantages: List[str] = Field(default_factory=list)


class EligibilityInvestigator:
    """
    Deterministic 15-dimension eligibility investigator workflow.
    Evaluates candidate scholarships against student profiles without LLM hallucination.
    """

    def evaluate(
        self,
        scholarship: Scholarship,
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> EligibilityResult:
        session_id = student.session_id or "default-session"
        events: List[ScholarXEvent] = []

        def emit(event_type: AgentEventType, payload: dict, severity: EventSeverity = EventSeverity.INFO):
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=event_type,
                agent_id="eligibility_investigator",
                agent_display_name="Eligibility Investigator",
                component_type="WORKFLOW",
                phase="ELIGIBILITY",
                related_scholarship_id=scholarship.scholarship_id,
                payload=payload,
                severity=severity,
            )
            events.append(evt)
            if event_callback:
                try:
                    event_callback(evt)
                except Exception as e:
                    logger.warning(f"Failed to invoke event callback: {e}")

        emit(
            AgentEventType.ELIGIBILITY_CHECK_STARTED,
            {
                "scholarship_id": scholarship.scholarship_id,
                "scholarship_name": scholarship.name,
                "student_name": student.personal.name,
            },
            EventSeverity.INFO,
        )

        dimensions: List[DimensionScore] = []
        blocking_issues: List[str] = []
        action_required: List[str] = []
        pakistan_advantages: List[str] = []

        # Detect Cambridge International Education Stream
        is_cambridge = (
            student.academic.education_system == EducationSystem.CAMBRIDGE
            or bool(student.academic.a_level_grades and len(student.academic.a_level_grades) > 0)
        )
        if is_cambridge:
            pakistan_advantages.append(
                "Cambridge GCE A-Levels Direct Entry: Internationally recognized qualification granting direct admission to UK, German, and European universities (exempt from 1-year Studienkolleg or foundation year required for standard 12-year FSc)."
            )
            pakistan_advantages.append(
                "CIE International Benchmark: Globally standardized letter grades provide high-priority evaluation across Russell Group, Commonwealth, and European research programs."
            )

        # 1. Pakistan Eligibility Check (Hard Gate)
        is_pk_eligible = (
            scholarship.pakistan_requirements.pakistan_eligible
            or "PK" in scholarship.eligibility.eligible_nationalities
            or "Pakistan" in scholarship.eligibility.eligible_nationalities
        )
        if is_pk_eligible:
            dimensions.append(
                DimensionScore(
                    dimension_name="Pakistan Nationality Eligibility",
                    score=100.0,
                    weight=0.15,
                    status=DimensionStatus.PASS,
                    details="Open to Pakistani nationals.",
                )
            )
        else:
            is_pk_eligible = False
            blocking_issues.append("Scholarship is not open to Pakistani nationals.")
            dimensions.append(
                DimensionScore(
                    dimension_name="Pakistan Nationality Eligibility",
                    score=0.0,
                    weight=0.15,
                    status=DimensionStatus.FAIL,
                    details="Pakistani nationals are not eligible for this scholarship.",
                )
            )

        # 2. Pakistan Bilateral Quota (Bonus Dimension)
        if scholarship.pakistan_requirements.pakistan_bilateral_quota:
            seats_str = f" ({scholarship.pakistan_requirements.pakistan_quota_seats} reserved seats)" if scholarship.pakistan_requirements.pakistan_quota_seats else ""
            advantage_msg = f"Dedicated bilateral quota for Pakistani students{seats_str} via government/HEC channels."
            pakistan_advantages.append(advantage_msg)
            dimensions.append(
                DimensionScore(
                    dimension_name="Bilateral Pakistan Quota",
                    score=100.0,
                    weight=0.10,
                    status=DimensionStatus.BONUS,
                    details=advantage_msg,
                )
            )
            if scholarship.pakistan_requirements.hec_managed:
                pakistan_advantages.append("Application is coordinated directly through HEC Pakistan portal.")

        # 3. Target Degree Level (Hard Gate)
        target_degree = student.preferences.target_degree_level
        offered_degrees = scholarship.eligibility.degree_levels

        if is_degree_match(target_degree, offered_degrees):
            dimensions.append(
                DimensionScore(
                    dimension_name="Degree Level Match",
                    score=100.0,
                    weight=0.15,
                    status=DimensionStatus.PASS,
                    details=f"Target degree '{target_degree}' is supported ({', '.join(offered_degrees)}).",
                )
            )
        else:
            blocking_issues.append(
                f"Target degree level '{target_degree}' is not offered. Only {', '.join(offered_degrees)} available."
            )
            dimensions.append(
                DimensionScore(
                    dimension_name="Degree Level Match",
                    score=0.0,
                    weight=0.15,
                    status=DimensionStatus.FAIL,
                    details=f"Degree mismatch: Student wants {target_degree}, but scholarship is only for {', '.join(offered_degrees)}.",
                )
            )

        # 4. Field of Study / Major Match
        target_fields = student.preferences.target_fields or [student.academic.field_of_study]
        eligible_fields = scholarship.eligibility.eligible_fields

        if not eligible_fields:
            # Open to all fields
            dimensions.append(
                DimensionScore(
                    dimension_name="Field of Study Match",
                    score=100.0,
                    weight=0.10,
                    status=DimensionStatus.PASS,
                    details="Open to all academic disciplines.",
                )
            )
        else:
            # Check overlap using deterministic taxonomy engine
            field_match = is_field_match(target_fields, eligible_fields)
            if field_match:
                dimensions.append(
                    DimensionScore(
                        dimension_name="Field of Study Match",
                        score=100.0,
                        weight=0.10,
                        status=DimensionStatus.PASS,
                        details=f"Target field '{', '.join(target_fields)}' matches eligible disciplines.",
                    )
                )
            else:
                dimensions.append(
                    DimensionScore(
                        dimension_name="Field of Study Match",
                        score=40.0,
                        weight=0.10,
                        status=DimensionStatus.WARNING,
                        details=f"Field overlap uncertain. Student: {', '.join(target_fields)}; Eligible: {', '.join(eligible_fields[:3])}.",
                    )
                )

        # 5. Prior Education Years
        min_years = scholarship.eligibility.min_years_education
        student_years = student.academic.years_of_education

        # In international systems, Cambridge GCE A-Levels (11 O-Levels + 2 A-Levels = 13 years)
        # is recognized as a full 13-year British secondary credential, granting direct entry.
        effective_years = 13 if (is_cambridge and student_years >= 12) else student_years

        if effective_years >= min_years:
            details_str = f"Student has completed {effective_years} years of education (min required: {min_years})."
            if is_cambridge and effective_years == 13:
                details_str += " Cambridge GCE A-Levels satisfies European 13-year benchmark for direct university matriculation."
            dimensions.append(
                DimensionScore(
                    dimension_name="Prior Education Requirements",
                    score=100.0,
                    weight=0.10,
                    status=DimensionStatus.PASS,
                    details=details_str,
                )
            )
        else:
            blocking_issues.append(
                f"Requires minimum {min_years} years of education (Student has {student_years} years)."
            )
            dimensions.append(
                DimensionScore(
                    dimension_name="Prior Education Requirements",
                    score=0.0,
                    weight=0.10,
                    status=DimensionStatus.FAIL,
                    details=f"Insufficient prior years of education ({student_years} < {min_years}).",
                )
            )

        # 6. Academic GPA / Percentage Merit (Hard Gate)
        min_gpa_pct = scholarship.eligibility.min_gpa_percentage
        min_gpa_4 = scholarship.eligibility.min_gpa_4_scale
        student_gpa_pct = student.academic.gpa_percentage
        student_gpa_4 = student.academic.gpa_4_scale

        # Bidirectional fallback: If student only has 4.0 scale GPA, convert to percentage
        if (student_gpa_pct is None or student_gpa_pct <= 0.0) and student_gpa_4 and student_gpa_4 > 0.0:
            student_gpa_pct = gpa_4_to_percentage(student_gpa_4)

        if min_gpa_pct is None and min_gpa_4 is not None:
            min_gpa_pct = gpa_4_to_percentage(min_gpa_4)

        if min_gpa_pct is None and min_gpa_4 is None:
            eff_pct = student_gpa_pct if (student_gpa_pct and student_gpa_pct > 0) else (gpa_4_to_percentage(student_gpa_4) if (student_gpa_4 and student_gpa_4 > 0) else 70.0)
            if eff_pct < 70.0:
                blocking_issues.append(
                    f"Ineligible for Merit Award: Your academic marks/GPA score ({eff_pct:.1f}%) is below the required 70.0% merit cutoff."
                )
                dimensions.append(
                    DimensionScore(
                        dimension_name="Academic Merit & GPA",
                        score=0.0,
                        weight=0.15,
                        status=DimensionStatus.FAIL,
                        details=f"Ineligible for Merit Award: {eff_pct:.1f}% < 70.0%.",
                    )
                )
                action_required.append(
                    f"Academic Standing Feedback: Marks/GPA ({eff_pct:.1f}%) are below the 70.0% official cutoff. We politely advise targeting holistic programs or need-based opportunities."
                )
                action_required.append(
                    "Alternative Funding Pathway: Although currently ineligible for this strict merit award, you qualify to apply for Need-Based Grants (e.g. Italian DSU Regional Grants, Hungarian State-Subsidized Fee Waivers, or Chinese Type-B Provincial Grants) which prioritize family income over academic test cutoffs."
                )
            else:
                gpa_score = min(100.0, max(50.0, eff_pct))
                dimensions.append(
                    DimensionScore(
                        dimension_name="Academic Merit & GPA",
                        score=gpa_score,
                        weight=0.15,
                        status=DimensionStatus.PASS,
                        details=f"No hard minimum GPA specified; student's {eff_pct:.1f}% ({student.academic.uk_classification or 'Strong'}) is competitive.",
                    )
                )
        else:
            meets_req = True
            fail_reasons = []

            # Enforce scholarship minimum and baseline 70.0% merit cutoff
            effective_cutoff = max(70.0, min_gpa_pct) if min_gpa_pct is not None else 70.0
            if (student_gpa_pct or 0.0) < effective_cutoff:
                meets_req = False
                fail_reasons.append(f"{(student_gpa_pct or 0.0):.1f}% < {effective_cutoff:.1f}%")

            if min_gpa_4 is not None and student_gpa_4 and student_gpa_4 > 0:
                if student_gpa_4 < min_gpa_4:
                    meets_req = False
                    fail_reasons.append(f"CGPA {student_gpa_4:.2f} < {min_gpa_4:.2f}")

            if meets_req:
                details_str = f"Student's {(student_gpa_pct or 0.0):.1f}%"
                if student_gpa_4 and student_gpa_4 > 0:
                    details_str += f" (CGPA {student_gpa_4:.2f})"
                details_str += f" satisfies the minimum requirement of {effective_cutoff:.1f}%."

                dimensions.append(
                    DimensionScore(
                        dimension_name="Academic Merit & GPA",
                        score=100.0,
                        weight=0.15,
                        status=DimensionStatus.PASS,
                        details=details_str,
                    )
                )
            else:
                reason = ", ".join(fail_reasons)
                blocking_issues.append(
                    f"Ineligible for Merit Award: Your academic marks/GPA score ({reason}) is currently below the competitive minimum cutoff (70.0% minimum threshold)."
                )
                dimensions.append(
                    DimensionScore(
                        dimension_name="Academic Merit & GPA",
                        score=0.0,
                        weight=0.15,
                        status=DimensionStatus.FAIL,
                        details=f"Ineligible for Merit Award: {reason}.",
                    )
                )
                action_required.append(
                    f"Academic Standing Feedback: Marks/GPA ({reason}) are below the official cutoff. We politely advise targeting holistic programs or need-based opportunities."
                )
                action_required.append(
                    "Alternative Funding Pathway: Although currently ineligible for this strict merit award, you qualify to apply for Need-Based Grants (e.g. Italian DSU Regional Grants, Hungarian State-Subsidized Fee Waivers, or Chinese Type-B Provincial Grants) which prioritize family income over academic test cutoffs."
                )

        # 7. Age Limits (Hard Gate)
        target_deg_str = (student.preferences.target_degree_level or "").lower()
        is_undergrad = any(
            k in target_deg_str
            for k in ["bachelor", "undergrad", "bs", "inter", "fsc", "ics", "a-level", "diploma", "12"]
        )
        age_limit = (
            scholarship.eligibility.age_limit_undergrad
            if is_undergrad
            else scholarship.eligibility.age_limit_postgrad
        )
        student_age = student.personal.age

        if age_limit is None or student_age <= age_limit:
            details_str = f"Student age ({student_age}) meets eligibility" + (f" (limit: {age_limit})" if age_limit else " (no limit)")
            dimensions.append(
                DimensionScore(
                    dimension_name="Age Eligibility",
                    score=100.0,
                    weight=0.10,
                    status=DimensionStatus.PASS,
                    details=details_str,
                )
            )
        else:
            blocking_issues.append(
                f"Student age {student_age} exceeds maximum age limit of {age_limit} for this program."
            )
            dimensions.append(
                DimensionScore(
                    dimension_name="Age Eligibility",
                    score=0.0,
                    weight=0.10,
                    status=DimensionStatus.FAIL,
                    details=f"Age limit exceeded: {student_age} > {age_limit}.",
                )
            )

        # 8. English Language Proficiency & MOI Waiver
        eng_req = scholarship.language
        if not eng_req.english_test_required:
            dimensions.append(
                DimensionScore(
                    dimension_name="English Language Requirement",
                    score=100.0,
                    weight=0.10,
                    status=DimensionStatus.PASS,
                    details="No standardized English test required.",
                )
            )
        elif student.language.has_english_test:
            # Student has IELTS or TOEFL
            min_ielts = eng_req.minimum_ielts or 6.0
            student_ielts = student.language.ielts_overall or 6.5
            if student_ielts >= min_ielts:
                dimensions.append(
                    DimensionScore(
                        dimension_name="English Language Requirement",
                        score=100.0,
                        weight=0.10,
                        status=DimensionStatus.PASS,
                        details=f"IELTS Band {student_ielts:.1f} satisfies minimum requirement ({min_ielts:.1f}).",
                    )
                )
            else:
                action_required.append(
                    f"Retake IELTS: current Band {student_ielts:.1f} is below minimum requirement of {min_ielts:.1f}."
                )
                dimensions.append(
                    DimensionScore(
                        dimension_name="English Language Requirement",
                        score=50.0,
                        weight=0.10,
                        status=DimensionStatus.ACTION_REQUIRED,
                        details=f"IELTS score is below threshold ({student_ielts:.1f} < {min_ielts:.1f}).",
                    )
                )
        else:
            # Student does not have test
            if scholarship.pakistan_requirements.accepts_moi_certificate and student.language.moi_certificate_available:
                dimensions.append(
                    DimensionScore(
                        dimension_name="English Language Requirement",
                        score=90.0,
                        weight=0.10,
                        status=DimensionStatus.PASS,
                        details="English Medium of Instruction (MOI) Certificate accepted in lieu of IELTS.",
                    )
                )
            elif scholarship.pakistan_requirements.accepts_moi_certificate:
                action_required.append("Obtain English Medium of Instruction (MOI) certificate from your college/university.")
                dimensions.append(
                    DimensionScore(
                        dimension_name="English Language Requirement",
                        score=75.0,
                        weight=0.10,
                        status=DimensionStatus.ACTION_REQUIRED,
                        details="MOI certificate accepted; student needs to obtain it from institution.",
                    )
                )
            else:
                action_required.append(
                    f"Book and take IELTS Academic exam (minimum required: {eng_req.minimum_ielts or 6.5})."
                )
                dimensions.append(
                    DimensionScore(
                        dimension_name="English Language Requirement",
                        score=40.0,
                        weight=0.10,
                        status=DimensionStatus.ACTION_REQUIRED,
                        details="Standardized English test (IELTS/TOEFL) is required and not yet submitted.",
                    )
                )

        # 9. HEC USAT / HAT Standardized Tests
        if is_undergrad and scholarship.pakistan_requirements.hec_usat_required:
            if student.standardized_tests.hec_usat is not None:
                dimensions.append(
                    DimensionScore(
                        dimension_name="HEC USAT Requirement",
                        score=100.0,
                        weight=0.05,
                        status=DimensionStatus.PASS,
                        details=f"HEC USAT score ({student.standardized_tests.hec_usat}) on record.",
                    )
                )
            else:
                action_required.append("Register for HEC USAT (Undergraduate Studies Admission Test) on the HEC ETC portal.")
                dimensions.append(
                    DimensionScore(
                        dimension_name="HEC USAT Requirement",
                        score=70.0,
                        weight=0.05,
                        status=DimensionStatus.ACTION_REQUIRED,
                        details="HEC USAT test required for undergraduate bilateral nomination.",
                    )
                )
        elif not is_undergrad and scholarship.pakistan_requirements.hec_hat_required:
            if student.standardized_tests.hec_hat is not None:
                dimensions.append(
                    DimensionScore(
                        dimension_name="HEC HAT Requirement",
                        score=100.0,
                        weight=0.05,
                        status=DimensionStatus.PASS,
                        details=f"HEC HAT score ({student.standardized_tests.hec_hat}) on record.",
                    )
                )
            else:
                action_required.append("Register for HEC HAT (Higher Education Aptitude Test) on the HEC ETC portal.")
                dimensions.append(
                    DimensionScore(
                        dimension_name="HEC HAT Requirement",
                        score=70.0,
                        weight=0.05,
                        status=DimensionStatus.ACTION_REQUIRED,
                        details="HEC HAT test required for postgraduate bilateral nomination.",
                    )
                )

        # 10. Document Attestations
        if scholarship.pakistan_requirements.hec_attestation_required and not student.academic.hec_attestation_done:
            action_required.append("Initiate HEC degree e-attestation via HEC DAS portal.")
        if scholarship.pakistan_requirements.ibcc_equivalence_required and not student.academic.ibcc_equivalence_done:
            action_required.append("Obtain IBCC equivalence certificate for Intermediate credentials.")
        if scholarship.pakistan_requirements.mofa_attestation_required:
            action_required.append("Get MOFA apostille/attestation stamps on degrees and birth certificate.")

        # 11. Funding Match
        funding_tier = scholarship.funding.funding_type
        if funding_tier == FundingType.FULL:
            dimensions.append(
                DimensionScore(
                    dimension_name="Funding Type Alignment",
                    score=100.0,
                    weight=0.10,
                    status=DimensionStatus.PASS,
                    details="Fully funded: Covers 100% tuition, accommodation/allowance, and monthly living stipend.",
                )
            )
        else:
            dimensions.append(
                DimensionScore(
                    dimension_name="Funding Type Alignment",
                    score=70.0,
                    weight=0.10,
                    status=DimensionStatus.WARNING,
                    details=f"Partial funding: {funding_tier.value}. Some tuition or living costs may be required.",
                )
            )

        # Calculate Overall Eligibility Score
        is_eligible = len(blocking_issues) == 0

        # Weighted calculation
        total_weight = sum(d.weight for d in dimensions if d.status != DimensionStatus.BONUS) or 1.0
        weighted_score = sum(d.score * d.weight for d in dimensions if d.status != DimensionStatus.BONUS) / total_weight

        # Add bilateral bonus
        if scholarship.pakistan_requirements.pakistan_bilateral_quota:
            weighted_score = min(100.0, weighted_score + 5.0)

        if not is_eligible:
            # Penalize overall score if hard gates failed
            weighted_score = min(45.0, weighted_score * 0.5)

        final_score = round(max(0.0, min(100.0, weighted_score)), 1)

        result = EligibilityResult(
            scholarship_id=scholarship.scholarship_id,
            scholarship_name=scholarship.name,
            is_eligible=is_eligible,
            eligibility_score=final_score,
            dimension_results=dimensions,
            blocking_issues=blocking_issues,
            action_required=action_required,
            pakistan_advantages=pakistan_advantages,
        )

        emit(
            AgentEventType.ELIGIBILITY_PASS if is_eligible else AgentEventType.ELIGIBILITY_FAIL,
            {
                "scholarship_id": scholarship.scholarship_id,
                "is_eligible": is_eligible,
                "eligibility_score": final_score,
                "blocking_issues_count": len(blocking_issues),
            },
            EventSeverity.SUCCESS if is_eligible else EventSeverity.WARNING,
        )

        emit(
            AgentEventType.ELIGIBILITY_COMPLETE,
            {
                "scholarship_id": scholarship.scholarship_id,
                "eligibility_score": final_score,
                "dimensions_checked": len(dimensions),
            },
            EventSeverity.INFO,
        )

        return result

    def evaluate_all(
        self,
        scholarships: List[Scholarship],
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> List[EligibilityResult]:
        """Evaluates an entire candidate list."""
        return [self.evaluate(sc, student, event_callback) for sc in scholarships]
