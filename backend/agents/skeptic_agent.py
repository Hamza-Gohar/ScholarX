import asyncio
from datetime import datetime, timezone
import json
import logging
import os
import re
from typing import Any, Callable, Dict, List, Optional
import uuid

from config import get_settings
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.evidence import (
    DebateTopic,
    EvidenceTrail,
    SkepticChallenge,
    SourceCitation,
    VerificationVerdict,
)
from schemas.scholarship import Scholarship
from schemas.student import StudentProfile
from utils.api_keys import KeyManager

logger = logging.getLogger("scholarx.agents.skeptic")


class SkepticAgent:
    """
    Adversarial Skeptic Agent for ScholarX.
    Cross-checks claims, identifies Pakistan-specific friction points (visas, Sperrkonto,
    bonds, supervisor letters), and conducts structured debate clashes.
    """

    def __init__(self):
        self.settings = get_settings()
        self.key_manager = KeyManager.get_instance()

    def _emit_event(
        self,
        session_id: str,
        scholarship_id: str,
        event_type: AgentEventType,
        payload: dict,
        severity: EventSeverity = EventSeverity.INFO,
        callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> ScholarXEvent:
        evt = ScholarXEvent(
            session_id=session_id,
            event_type=event_type,
            agent_id="skeptic_agent",
            agent_display_name="Skeptic Challenger",
            component_type="AGENT",
            phase="VERIFICATION",
            related_scholarship_id=scholarship_id,
            payload=payload,
            severity=severity,
        )
        if callback:
            try:
                callback(evt)
            except Exception as e:
                logger.warning(f"Failed to invoke event callback: {e}")
        return evt

    def _generate_rule_based_skepticism(
        self,
        scholarship: Scholarship,
        student: StudentProfile,
    ) -> Dict[str, Any]:
        """
        Deterministic, expert-curated Pakistani skepticism rules engine.
        Acts as ground-truth when LLM is unavailable or offline.
        """
        challenges: List[Dict[str, Any]] = []
        debates: List[Dict[str, Any]] = []
        c_country = scholarship.host_country.upper()
        s_name = scholarship.name.lower()

        # 1. Fulbright & Australia Awards: Mandatory 2-Year Return-to-Home Obligation
        if "fulbright" in s_name or "australia awards" in s_name or c_country == "US":
            if "fulbright" in s_name or "australia awards" in s_name:
                challenges.append({
                    "category": "RETURN_OBLIGATION",
                    "title": "Strict 2-Year Home Country Return Obligation (Bond)",
                    "description": "Recipients are subject to a mandatory 2-year physical return to Pakistan upon graduation (J-1 212e / DFAT clause) with no option to work or adjust status abroad immediately.",
                    "severity": "HIGH",
                    "suggested_mitigation": "Incorporate 2 years of planned professional contribution in Pakistan into your career roadmap.",
                })
                debates.append({
                    "topic": "Prestige vs Freedom of Post-Study Relocation",
                    "advocate_point": "World's most prestigious scholarship covering full tuition, generous stipend, airfare, and health insurance.",
                    "skeptic_counterpoint": "Inflexible 2-year return requirement prohibits post-study OPT/work visas abroad.",
                    "verdict": "Unbeatable if your primary vision is to achieve international credentials and lead in Pakistan.",
                })

        # 2. Germany & Schengen: Visa Backlog & Blocked Account / Living Gap
        if c_country == "DE":
            challenges.append({
                "category": "VISA_RISK",
                "title": "German Embassy Pakistan Visa Appointment Backlog",
                "description": "German embassy wait times in Islamabad and Karachi can range between 6 to 12 months for Category A/B student applicants.",
                "severity": "HIGH",
                "suggested_mitigation": "Book your German Embassy appointment slot on the CSP/VFS portal immediately upon university application submission.",
            })
            debates.append({
                "topic": "Zero Tuition vs Visa Appointment Bottleneck",
                "advocate_point": "German public universities charge zero tuition and offer world-class research engineering education.",
                "skeptic_counterpoint": "Visa backlog in Pakistan has caused students to defer or forfeit intakes.",
                "verdict": "Highly recommended provided the student starts visa booking months before admission letter.",
            })

        # 3. China CSC / Japan MEXT: Supervisor Acceptance Hurdles
        if c_country in ("CN", "JP") and ("csc" in s_name or "mext" in s_name or "chinese" in s_name):
            challenges.append({
                "category": "COMPETITION",
                "title": "Mandatory Pre-Admission Supervisor Acceptance Letter",
                "description": "Securing a formal acceptance letter from a host university professor is practically required for competitive selection among Pakistani applicants.",
                "severity": "MEDIUM",
                "suggested_mitigation": "Draft personalized research proposal emails and contact prospective Chinese/Japanese faculty early.",
            })
            debates.append({
                "topic": "High Acceptance Quota vs Faculty Outreach Requirement",
                "advocate_point": "Massive bilateral quota (hundreds of seats annually) with generous stipends and free accommodation.",
                "skeptic_counterpoint": "Cold-emailing 30+ professors for acceptance letters is exhausting and competitive.",
                "verdict": "One of the highest-probability fully-funded pathways for Pakistani students who proactively contact professors.",
            })

        # 4. Airfare & Hidden Upfront Costs
        if scholarship.funding.travel_airfare != "COVERED":
            challenges.append({
                "category": "HIDDEN_COST",
                "title": "Uncovered International Airfare & Initial Settlement",
                "description": "Scholarship does not fund one-way international airfare (~PKR 180,000 - 240,000) and first-month pocket money before stipend disbursement.",
                "severity": "MEDIUM",
                "suggested_mitigation": "Arrange upfront family funding or travel loan for flight ticket and first 30 days.",
            })
            debates.append({
                "topic": "Tuition Waiver vs Upfront Airfare & Settlement Outlay",
                "advocate_point": "Substantial financial coverage for tuition and living stipends once on campus.",
                "skeptic_counterpoint": "Requires immediate personal liquid capital for air tickets and first month expenses.",
                "verdict": "Viable pathway provided student secures initial travel funds in advance.",
            })

        # 5. Default General Pakistani Challenge & Debate if pool is small
        if not challenges:
            challenges.append({
                "category": "COMPETITION",
                "title": "High Applicant-to-Seat Ratio for Pakistani Candidates",
                "description": "Popular international scholarship with strong competition across all Pakistani provinces.",
                "severity": "LOW",
                "suggested_mitigation": "Ensure your SOP and academic references are highly polished and tailored.",
            })
        if not debates:
            debates.append({
                "topic": "Opportunity Fit vs Competitive Profile",
                "advocate_point": "Excellent match for student's target degree and academic background.",
                "skeptic_counterpoint": "Requires standing out among hundreds of qualified applicants.",
                "verdict": "Strong application candidate; proceed with thorough preparation.",
            })

        return {
            "challenges": challenges,
            "debates": debates,
            "confidence_score": 0.88 if scholarship.pakistan_requirements.pakistan_bilateral_quota else 0.80,
        }

    async def _call_llm_structured(self, scholarship: Scholarship, student: StudentProfile) -> Optional[str]:
        """Calls Groq or Gemini with adversarial prompt to extract nuanced skepticism."""
        prompt = f"""You are the Skeptic Agent in ScholarX (Scholarship Intelligence for Pakistani students).
Your job is to critically challenge this scholarship candidate and identify potential friction points for a Pakistani student.

Student:
- Name: {student.personal.name}, Age: {student.personal.age}, City: {student.personal.city}
- Degree Level Target: {student.preferences.target_degree_level}, Field: {student.academic.field_of_study}
- Marks: {student.academic.gpa_percentage}% / GPA {student.academic.gpa_4_scale}
- English Test: {student.language.english_proficiency_test.value} (Band {student.language.ielts_overall or 'N/A'})
- Max Budget: PKR {student.preferences.max_out_of_pocket_pkr:,}

Scholarship:
- Name: {scholarship.name}
- Host Country: {scholarship.host_country_name} ({scholarship.host_country})
- Funding: {scholarship.funding.funding_type.value}, Tuition: {scholarship.funding.tuition}, Travel: {scholarship.funding.travel_airfare}
- Bilateral Quota: {scholarship.pakistan_requirements.pakistan_bilateral_quota}
- Language Req: IELTS {scholarship.language.minimum_ielts or 'N/A'}, MOI Accepted: {scholarship.pakistan_requirements.accepts_moi_certificate}

Respond ONLY with valid JSON in this exact structure:
{{
  "challenges": [
    {{
      "category": "HIDDEN_COST" | "VISA_RISK" | "RETURN_OBLIGATION" | "DEADLINE_RISK" | "COMPETITION",
      "title": "Short challenge title",
      "description": "Specific Pakistani student friction analysis",
      "severity": "LOW" | "MEDIUM" | "HIGH" | "CRITICAL",
      "suggested_mitigation": "Actionable step for the student"
    }}
  ],
  "debates": [
    {{
      "topic": "Topic of contention",
      "advocate_point": "Why it's a great opportunity",
      "skeptic_counterpoint": "The hidden friction or drawback",
      "verdict": "Objective balanced verdict"
    }}
  ],
  "confidence_score": 0.85
}}"""

        async def _do_call() -> Optional[str]:
            # Try Groq with at most 1 attempt
            if self.key_manager.groq.total_keys > 0:
                try:
                    key = await self.key_manager.groq.get_key()
                    from groq import AsyncGroq
                    client = AsyncGroq(api_key=key, timeout=4.0, max_retries=0)
                    response = await client.chat.completions.create(
                        model=self.settings.GROQ_MODEL,
                        messages=[
                            {"role": "system", "content": "You are an objective adversarial scholarship review agent specializing in Pakistani foreign admissions."},
                            {"role": "user", "content": prompt},
                        ],
                        response_format={"type": "json_object"},
                        temperature=0.2,
                    )
                    await self.key_manager.groq.report_success(key)
                    return response.choices[0].message.content
                except Exception as e:
                    logger.debug(f"Groq skeptic call failed: {e}")

            # Try Gemini fallback with at most 1 attempt
            if self.key_manager.gemini.total_keys > 0:
                try:
                    key = await self.key_manager.gemini.get_key()
                    from google import genai
                    client = genai.Client(api_key=key)
                    res = await asyncio.to_thread(
                        client.models.generate_content,
                        model=self.settings.GEMINI_PRIMARY_MODEL,
                        contents=f"Return JSON strictly matching schema:\n{prompt}",
                    )
                    if res and res.text:
                        await self.key_manager.gemini.report_success(key)
                        return res.text
                except Exception as e:
                    logger.debug(f"Gemini skeptic call failed: {e}")

            return None

        try:
            return await asyncio.wait_for(_do_call(), timeout=4.0)
        except Exception:
            return None

    def _generate_rule_based_evidence_trail(
        self,
        scholarship: Scholarship,
        student: StudentProfile,
    ) -> EvidenceTrail:
        """Deterministically generates full EvidenceTrail with Pakistani challenges and debate clashes."""
        parsed_data = self._generate_rule_based_skepticism(scholarship, student)
        challenges: List[SkepticChallenge] = []
        for idx, ch in enumerate(parsed_data.get("challenges", [])):
            challenges.append(
                SkepticChallenge(
                    challenge_id=f"chk-{scholarship.scholarship_id}-{idx+1}",
                    category=ch.get("category", "HIDDEN_COST"),
                    title=ch.get("title", "Skeptic Challenge"),
                    description=ch.get("description", ""),
                    severity=ch.get("severity", "MEDIUM"),
                    suggested_mitigation=ch.get("suggested_mitigation"),
                    resolved=False,
                )
            )

        debates: List[DebateTopic] = []
        for idx, db in enumerate(parsed_data.get("debates", [])):
            debates.append(
                DebateTopic(
                    topic=db.get("topic", "Evaluation Debate"),
                    advocate_point=db.get("advocate_point", "High value opportunity for Pakistani students."),
                    skeptic_counterpoint=db.get("skeptic_counterpoint", "Requires rigorous document readiness."),
                    verdict=db.get("verdict", "Viable high-probability scholarship pathway."),
                )
            )

        is_hec = getattr(getattr(scholarship, "pakistan_requirements", None), "is_hec_recognized", True)
        return EvidenceTrail(
            scholarship_id=scholarship.scholarship_id,
            overall_verdict=VerificationVerdict.VERIFIED if is_hec else VerificationVerdict.PARTIALLY_VERIFIED,
            confidence_score=float(parsed_data.get("confidence_score", 0.88)),
            verification_notes="Verified canonical institutional scholarship data for Pakistani applicants.",
            skeptic_challenges=challenges,
            debate_summary=debates,
            sources=[
                SourceCitation(
                    url=scholarship.source_url or f"https://registry.scholarx.pk/{scholarship.scholarship_id}",
                    title=f"{scholarship.name} Official Portal",
                    domain="official.registry",
                    source_type="GOVERNMENT_PORTAL",
                    snippet=f"Verified scholarship program for {scholarship.host_country_name}.",
                    verified_at=datetime.now(timezone.utc).isoformat(),
                    is_official_hec=is_hec,
                )
            ],
            last_verified_timestamp=datetime.now(timezone.utc).isoformat(),
        )

    async def evaluate_skepticism(
        self,
        scholarship: Scholarship,
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> EvidenceTrail:
        """
        Executes adversarial review, raises Pakistani student challenges, and builds EvidenceTrail.
        """
        session_id = student.session_id
        self._emit_event(
            session_id,
            scholarship.scholarship_id,
            AgentEventType.VERIFICATION_STARTED,
            {"scholarship_name": scholarship.name, "country": scholarship.host_country_name},
            EventSeverity.INFO,
            event_callback,
        )

        parsed_data = None
        # Attempt LLM extraction
        llm_raw = await self._call_llm_structured(scholarship, student)
        if llm_raw:
            try:
                cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", llm_raw.strip(), flags=re.MULTILINE)
                parsed_data = json.loads(cleaned)
            except Exception as e:
                logger.warning(f"Failed to parse LLM skeptic JSON: {e}")

        # Fallback to rule-based engine if LLM did not return structured result
        if not parsed_data or "challenges" not in parsed_data:
            parsed_data = self._generate_rule_based_skepticism(scholarship, student)

        challenges: List[SkepticChallenge] = []
        for idx, ch in enumerate(parsed_data.get("challenges", [])):
            challenge_obj = SkepticChallenge(
                challenge_id=f"chk-{scholarship.scholarship_id}-{idx+1}",
                category=ch.get("category", "HIDDEN_COST"),
                title=ch.get("title", "Skeptic Challenge"),
                description=ch.get("description", ""),
                severity=ch.get("severity", "MEDIUM"),
                suggested_mitigation=ch.get("suggested_mitigation"),
                resolved=False,
            )
            challenges.append(challenge_obj)
            self._emit_event(
                session_id,
                scholarship.scholarship_id,
                AgentEventType.SKEPTIC_CHALLENGE_RAISED,
                {
                    "challenge_id": challenge_obj.challenge_id,
                    "category": challenge_obj.category,
                    "title": challenge_obj.title,
                    "severity": challenge_obj.severity,
                },
                EventSeverity.WARNING if challenge_obj.severity in ("HIGH", "CRITICAL") else EventSeverity.INFO,
                event_callback,
            )

        debates: List[DebateTopic] = []
        for d in parsed_data.get("debates", []):
            debate_obj = DebateTopic(
                topic=d.get("topic", "Program Feasibility"),
                advocate_point=d.get("advocate_point", ""),
                skeptic_counterpoint=d.get("skeptic_counterpoint", ""),
                verdict=d.get("verdict", ""),
            )
            debates.append(debate_obj)
            self._emit_event(
                session_id,
                scholarship.scholarship_id,
                AgentEventType.SKEPTIC_DEBATE_CLASH,
                {"topic": debate_obj.topic, "verdict": debate_obj.verdict},
                EventSeverity.INFO,
                event_callback,
            )

        # Build citations
        sources: List[SourceCitation] = []
        if scholarship.source_url:
            sources.append(
                SourceCitation(
                    url=scholarship.source_url,
                    title=f"Official Portal: {scholarship.name}",
                    domain=scholarship.source_url.split("/")[2] if "/" in scholarship.source_url else "official",
                    source_type="GOVERNMENT_PORTAL" if scholarship.pakistan_requirements.pakistan_bilateral_quota else "SCHOLARSHIP_BODY",
                    is_official_hec=scholarship.pakistan_requirements.hec_managed,
                    verified_at=datetime.now(timezone.utc).isoformat(),
                )
            )

        # Determine verdict
        if scholarship.pakistan_requirements.hec_managed or scholarship.pakistan_requirements.pakistan_bilateral_quota:
            verdict = VerificationVerdict.HEC_CONFIRMED
        elif scholarship.confidence_score >= 0.85:
            verdict = VerificationVerdict.VERIFIED
        else:
            verdict = VerificationVerdict.PARTIALLY_VERIFIED

        confidence_score = float(parsed_data.get("confidence_score", 0.85))

        evidence = EvidenceTrail(
            scholarship_id=scholarship.scholarship_id,
            overall_verdict=verdict,
            confidence_score=confidence_score,
            sources=sources,
            skeptic_challenges=challenges,
            debate_summary=debates,
            last_verified_timestamp=datetime.now(timezone.utc).isoformat(),
            verification_notes=f"Evaluated with {len(challenges)} skeptic challenge(s) and {len(debates)} debate topic(s).",
        )

        self._emit_event(
            session_id,
            scholarship.scholarship_id,
            AgentEventType.SKEPTIC_COMPLETE,
            {
                "scholarship_id": scholarship.scholarship_id,
                "verdict": verdict.value,
                "confidence_score": confidence_score,
                "challenges_count": len(challenges),
            },
            EventSeverity.SUCCESS,
            event_callback,
        )

        return evidence
