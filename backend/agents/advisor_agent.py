import asyncio
from datetime import datetime, timezone
import json
import logging
import re
from typing import Any, Callable, Dict, List, Optional
import uuid

from config import get_settings
from schemas.events import AgentEventType, EventSeverity, ScholarXEvent
from schemas.roadmap import (
    ApplicationRoadmap,
    MilestoneAction,
    PakistaniOffice,
    RoadmapMilestone,
    RoadmapPhase,
)
from schemas.scholarship import Scholarship
from schemas.scoring import CompositeScoreResult
from schemas.student import EducationSystem, StudentProfile
from utils.api_keys import KeyManager

logger = logging.getLogger("scholarx.agents.advisor")


class AdvisorAgent:
    """
    Final Advisor Agent for ScholarX.
    Synthesizes a personalized, chronologically-calibrated application roadmap for Pakistani students.
    Maps out exact Pakistani offices (HEC, IBCC, MOFA, British Council, Gerry's), dates, and costs.
    """

    def __init__(self):
        self.settings = get_settings()
        self.key_manager = KeyManager.get_instance()

    def _get_pakistan_offices(
        self, city: str, is_undergrad: bool = False, is_cambridge: bool = False
    ) -> List[PakistaniOffice]:
        """Provides verified Pakistani government and test center locations based on student's city, level, and education stream."""
        city_norm = city.lower().strip()
        offices: List[PakistaniOffice] = []

        if is_undergrad:
            if is_cambridge:
                # Direct IBCC Equivalence for Cambridge O/A-Levels (No BISE verification needed)
                offices.append(
                    PakistaniOffice(
                        office_name="Inter Board Coordination Commission (IBCC) - Cambridge Cell",
                        office_type="IBCC",
                        city=city.capitalize(),
                        address="Plot No. 25, Street 38, G-10/4, Islamabad / Regional IBCC Office",
                        website_or_portal="https://ibcc.edu.pk",
                        fee_pkr=6000,
                        estimated_turnaround_days=10,
                        required_documents=[
                            "Original Cambridge A-Level Statement of Results / Certificates",
                            "Original Cambridge O-Level / IGCSE Statement of Results",
                            "Valid CNIC / B-Form / Passport Copy",
                        ],
                        pro_tips=[
                            "Cambridge students do NOT need local BISE board verification. Apply directly through IBCC online portal or regional walk-in counters.",
                        ],
                    )
                )
            else:
                # 1. BISE / FBISE Office (Board of Intermediate and Secondary Education)
                board_norm = (getattr(student.academic, "board_university", "") or "").lower()
                is_fbise = "fbise" in board_norm or "federal" in board_norm or "islamabad" in city_norm
                bise_city = "Islamabad" if is_fbise else ("Lahore" if "lahore" in city_norm else ("Karachi" if "karachi" in city_norm else city.capitalize()))
                bise_name = "Federal Board of Intermediate & Secondary Education (FBISE) Islamabad" if is_fbise else f"Board of Intermediate & Secondary Education (BISE) {bise_city}"
                bise_address = (
                    "Sector H-8/4, Islamabad"
                    if is_fbise
                    else ("86-Mozang Road, Lahore" if "lahore" in city_norm
                    else ("Bakhtiari Youth Centre, North Nazimabad, Karachi" if "karachi" in city_norm else f"Divisional Board Complex, {bise_city}"))
                )
                bise_portal = "https://fbise.edu.pk" if is_fbise else ("https://biselahore.com" if "lahore" in city_norm else f"https://bise{bise_city.lower()}.edu.pk")
                offices.append(
                    PakistaniOffice(
                        office_name=bise_name,
                        office_type="IBCC",
                        city=bise_city,
                        address=bise_address,
                        website_or_portal=bise_portal,
                        fee_pkr=4000,
                        estimated_turnaround_days=7,
                        required_documents=["Matric Sanad", "Intermediate / FSc / ICS Marksheet", "Original CNIC / B-Form"],
                        pro_tips=["Request sealed verification envelope addressed directly to IBCC."],
                    )
                )

                # 2. IBCC Office
                offices.append(
                    PakistaniOffice(
                        office_name="Inter Board Coordination Commission (IBCC)",
                        office_type="IBCC",
                        city=city.capitalize(),
                        address="Plot No. 25, Street 38, G-10/4, Islamabad / Regional BISE Complex",
                        website_or_portal="https://ibcc.edu.pk",
                        fee_pkr=6000,
                        estimated_turnaround_days=10,
                        required_documents=["BISE sealed envelope", "Original Inter Sanad", "CNIC copy"],
                        pro_tips=["Book online courier pickup or walk-in appointment through IBCC e-portal."],
                    )
                )

            # 3. HEC Education Testing Council (ETC - USAT)
            offices.append(
                PakistaniOffice(
                    office_name="HEC Education Testing Council (ETC - USAT)",
                    office_type="HEC",
                    city="Islamabad",
                    address="Sector H-9, Islamabad (Test Centers nationwide: Lahore, Karachi, Islamabad)",
                    website_or_portal="https://etc.hec.gov.pk",
                    fee_pkr=2000,
                    estimated_turnaround_days=14,
                    required_documents=["Roll Number Slip", "Original CNIC / Passport", "Fee Challan"],
                    pro_tips=["USAT-CS or USAT-E score required for HEC bilateral undergraduate quotas."],
                )
            )
        else:
            # HEC Regional Center for Graduate (Master's / PhD)
            if "lahore" in city_norm:
                offices.append(
                    PakistaniOffice(
                        office_name="HEC Regional Centre Lahore",
                        office_type="HEC",
                        city="Lahore",
                        address="55-B, New Muslim Town, Ayubia Market, Lahore",
                        website_or_portal="https://eservices.hec.gov.pk",
                        fee_pkr=3000,
                        estimated_turnaround_days=14,
                        required_documents=["Original Degrees", "Matric/Inter marksheets", "CNIC copy"],
                        pro_tips=["Book online e-appointment on HEC DAS portal 3 weeks early."],
                    )
                )
            elif "karachi" in city_norm:
                offices.append(
                    PakistaniOffice(
                        office_name="HEC Regional Centre Karachi",
                        office_type="HEC",
                        city="Karachi",
                        address="Behind National Museum of Pakistan, Burns Garden, Karachi",
                        website_or_portal="https://eservices.hec.gov.pk",
                        fee_pkr=3000,
                        estimated_turnaround_days=14,
                        required_documents=["Original Degrees", "Transcripts", "CNIC copy"],
                        pro_tips=["Arrive before 9:00 AM for queue token distribution."],
                    )
                )
            else:
                offices.append(
                    PakistaniOffice(
                        office_name="HEC Head Office Islamabad",
                        office_type="HEC",
                        city="Islamabad",
                        address="Sector H-9, Islamabad",
                        website_or_portal="https://eservices.hec.gov.pk",
                        fee_pkr=3000,
                        estimated_turnaround_days=10,
                        required_documents=["Original Degrees", "Transcripts", "CNIC copy"],
                        pro_tips=["Same-day urgent walk-in available via online token."],
                    )
                )

            # IBCC Office
            offices.append(
                PakistaniOffice(
                    office_name="Inter Board Committee of Chairmen (IBCC)",
                    office_type="IBCC",
                    city=city.capitalize(),
                    address="Plot No. 25, Street 38, G-10/4, Islamabad / Regional BISE",
                    website_or_portal="https://ibcc.edu.pk",
                    fee_pkr=6000,
                    estimated_turnaround_days=14,
                    required_documents=["Matric / Inter Sanad", "BISE verified copies", "CNIC copy"],
                    pro_tips=["Courier service via TCS available for direct attestation."],
                )
            )

        # British Council / IELTS
        offices.append(
            PakistaniOffice(
                office_name="British Council Pakistan IELTS Test Centre",
                office_type="BRITISH_COUNCIL",
                city=city.capitalize(),
                address=f"British Council Examinations Centre, {city.capitalize()}",
                website_or_portal="https://takeielts.britishcouncil.org/pakistan",
                fee_pkr=76000,
                estimated_turnaround_days=5,
                required_documents=["Original Passport", "CNIC", "Test Confirmation Slip"],
                pro_tips=["Computer-delivered IELTS gives results in 3 to 5 business days."],
            )
        )

        # VFS Global / Gerry's Drop Box
        offices.append(
            PakistaniOffice(
                office_name="VFS Global / Gerry's Visa Application Centre",
                office_type="VFS_GERRYS",
                city=city.capitalize(),
                address=f"Gerry's Building, Visa Application Centre, {city.capitalize()}",
                website_or_portal="https://visa.vfsglobal.com/pak/en",
                fee_pkr=20000,
                estimated_turnaround_days=21,
                required_documents=["Scholarship Award Letter", "Passport", "Police Certificate", "Medical Report"],
                pro_tips=["Book biometrics slot immediately upon receiving formal admission."],
            )
        )

        return offices

    def _generate_rule_based_roadmap(
        self,
        scholarship: Scholarship,
        score_result: CompositeScoreResult,
        student: StudentProfile,
    ) -> ApplicationRoadmap:
        """Deterministic expert roadmap generator for Pakistani applicants."""
        city = student.personal.city or "Lahore"
        target_deg = student.preferences.target_degree_level or ""
        is_undergrad = any(
            k in target_deg.lower()
            for k in ["bachelor", "undergrad", "bs", "inter", "fsc", "ics", "fa", "a-level", "diploma", "12"]
        )
        is_cambridge = (
            getattr(student.academic, "education_system", None) == EducationSystem.CAMBRIDGE
            or bool(getattr(student.academic, "a_level_grades", None))
        )
        is_low_gpa = (
            bool(student.academic.gpa_percentage and student.academic.gpa_percentage < 60.0)
            or bool(student.academic.gpa_4_scale and 0 < student.academic.gpa_4_scale < 2.5)
        )
        offices = self._get_pakistan_offices(city, is_undergrad=is_undergrad, is_cambridge=is_cambridge)

        if is_undergrad:
            if is_cambridge:
                # Cambridge O/A-Levels Milestones: Direct IBCC Equivalence (No BISE verification)
                m1_actions = [
                    MilestoneAction(
                        action_id="act-m1-1",
                        description="Submit original Cambridge A-Level & O-Level Statement of Results directly to IBCC for Equivalence Certificate (Fee: PKR 6,000)",
                        estimated_days=10,
                        estimated_cost_pkr=6000,
                        is_blocking=True,
                        assigned_office="Inter Board Coordination Commission (IBCC) - Cambridge Cell",
                    ),
                    MilestoneAction(
                        action_id="act-m1-2",
                        description="Request 2 Academic Recommendation Letters & Counselor Reference from Cambridge school/college",
                        estimated_days=7,
                        estimated_cost_pkr=0,
                        is_blocking=True,
                    ),
                ]
            else:
                # Undergraduate Milestones: BISE / FBISE + IBCC + USAT
                board_label = "FBISE Islamabad" if is_fbise else "Divisional BISE"
                m1_actions = [
                    MilestoneAction(
                        action_id="act-m1-1",
                        description=f"Verify Matric & Intermediate (ICS/FSc) Sanads/Marksheets with {board_label} Board",
                        estimated_days=7,
                        estimated_cost_pkr=4000,
                        is_blocking=True,
                        assigned_office=offices[0].office_name if offices else f"{board_label} Office",
                    ),
                    MilestoneAction(
                        action_id="act-m1-2",
                        description=f"Submit sealed {board_label} envelope to IBCC for certificate attestation and equivalence",
                        estimated_days=10,
                        estimated_cost_pkr=6000,
                        is_blocking=True,
                        assigned_office="Inter Board Coordination Commission (IBCC)",
                    ),
                    MilestoneAction(
                        action_id="act-m1-3",
                        description="Obtain 2 Academic Recommendation Letters / Character Certificates from college teachers/principal",
                        estimated_days=7,
                        estimated_cost_pkr=0,
                        is_blocking=True,
                    ),
                ]

            if not student.language.has_english_test and scholarship.language.english_test_required:
                m1_actions.append(
                    MilestoneAction(
                        action_id="act-m1-4",
                        description="Register and book British Council Computer-Delivered IELTS Academic test (6.5+ band)",
                        estimated_days=14,
                        estimated_cost_pkr=76000,
                        is_blocking=True,
                        assigned_office="British Council Pakistan",
                    )
                )

            m1 = RoadmapMilestone(
                milestone_id="ms-phase-1",
                title="Secondary Credentials Verification & Academic Readiness",
                phase=RoadmapPhase.HEC_IBCC_ATTESTATION,
                target_timeline_days="Day 1 to Day 20",
                total_phase_cost_pkr=sum(a.estimated_cost_pkr for a in m1_actions),
                actions=m1_actions,
                guidance_notes="Submit marksheet to your BISE / FBISE board early; IBCC requires board-sealed verification envelopes.",
            )

            m2_actions = []
            if scholarship.pakistan_requirements.hec_managed or scholarship.pakistan_requirements.pakistan_bilateral_quota:
                m2_actions.append(
                    MilestoneAction(
                        action_id="act-m2-1",
                        description="Register for HEC Undergraduate Studies Admission Test (USAT) on ETC portal (etc.hec.gov.pk)",
                        estimated_days=14,
                        estimated_cost_pkr=2000,
                        is_blocking=True,
                        assigned_office="HEC Education Testing Council (ETC)",
                    )
                )

            m2_actions.extend([
                MilestoneAction(
                    action_id="act-m2-2",
                    description="Draft tailored Statement of Purpose (SOP) highlighting passion for undergraduate Computer Science",
                    estimated_days=10,
                    estimated_cost_pkr=0,
                    is_blocking=True,
                ),
                MilestoneAction(
                    action_id="act-m2-3",
                    description=f"Complete online scholarship application on official portal ({scholarship.portal_url or scholarship.source_url})",
                    estimated_days=5,
                    estimated_cost_pkr=0,
                    is_blocking=True,
                ),
            ])

            if scholarship.pakistan_requirements.hec_managed:
                m2_actions.append(
                    MilestoneAction(
                        action_id="act-m2-4",
                        description="Submit mandatory dual nomination application on HEC Scholarship Portal (scholarship.hec.gov.pk)",
                        estimated_days=3,
                        estimated_cost_pkr=0,
                        is_blocking=True,
                    )
                )

            m2 = RoadmapMilestone(
                milestone_id="ms-phase-2",
                title="Undergraduate Portal Submission & Dual HEC Registration",
                phase=RoadmapPhase.ONLINE_PORTAL_APPLICATION,
                target_timeline_days="Day 21 to Day 35",
                total_phase_cost_pkr=sum(a.estimated_cost_pkr for a in m2_actions),
                actions=m2_actions,
                guidance_notes="For bilateral undergraduate quotas, ensure your application IDs on the foreign portal and HEC portal match precisely.",
            )

            urgent_actions = [
                "Submit Matric and Intermediate marksheets to your BISE / FBISE board for verification and obtain IBCC Equivalence.",
                "Contact college lecturers / principal for academic recommendation letters.",
                "Register for HEC USAT (Undergraduate Studies Admission Test) on etc.hec.gov.pk.",
            ]
        else:
            # Graduate (Master's / PhD) Milestones: HEC DAS + HEC HAT
            m1_actions = [
                MilestoneAction(
                    action_id="act-m1-1",
                    description="Initiate HEC Degree e-Attestation on DAS 1-Link portal",
                    estimated_days=14,
                    estimated_cost_pkr=3000,
                    is_blocking=True,
                    assigned_office=offices[0].office_name if offices else "HEC Regional Centre",
                ),
                MilestoneAction(
                    action_id="act-m1-2",
                    description="Obtain 2 Academic Letters of Recommendation from university faculty",
                    estimated_days=14,
                    estimated_cost_pkr=0,
                    is_blocking=True,
                ),
            ]

            if not student.language.has_english_test and scholarship.language.english_test_required:
                m1_actions.append(
                    MilestoneAction(
                        action_id="act-m1-3",
                        description="Register and book British Council Computer-Delivered IELTS Academic test",
                        estimated_days=14,
                        estimated_cost_pkr=76000,
                        is_blocking=True,
                        assigned_office="British Council Pakistan",
                    )
                )

            m1 = RoadmapMilestone(
                milestone_id="ms-phase-1",
                title="Credential Verification & Academic Readiness",
                phase=RoadmapPhase.HEC_IBCC_ATTESTATION,
                target_timeline_days="Day 1 to Day 20",
                total_phase_cost_pkr=sum(a.estimated_cost_pkr for a in m1_actions),
                actions=m1_actions,
                guidance_notes="Submit e-attestation early to prevent peak-season embassy bottlenecks.",
            )

            m2_actions = [
                MilestoneAction(
                    action_id="act-m2-1",
                    description="Draft tailored Statement of Purpose (SOP) addressing host country academic fit",
                    estimated_days=10,
                    estimated_cost_pkr=0,
                    is_blocking=True,
                ),
                MilestoneAction(
                    action_id="act-m2-2",
                    description=f"Complete online scholarship application on official portal ({scholarship.portal_url or scholarship.source_url})",
                    estimated_days=5,
                    estimated_cost_pkr=0,
                    is_blocking=True,
                ),
            ]

            if scholarship.pakistan_requirements.hec_managed:
                m2_actions.append(
                    MilestoneAction(
                        action_id="act-m2-3",
                        description="Submit mandatory dual application on HEC Scholarship Portal (scholarship.hec.gov.pk)",
                        estimated_days=3,
                        estimated_cost_pkr=0,
                        is_blocking=True,
                    )
                )

            m2 = RoadmapMilestone(
                milestone_id="ms-phase-2",
                title="Portal Submission & Dual HEC Registration",
                phase=RoadmapPhase.ONLINE_PORTAL_APPLICATION,
                target_timeline_days="Day 21 to Day 35",
                total_phase_cost_pkr=sum(a.estimated_cost_pkr for a in m2_actions),
                actions=m2_actions,
                guidance_notes="For bilateral quotas, ensure your application IDs on the foreign portal and HEC portal match precisely.",
            )

            urgent_actions = [
                "Initiate HEC degree e-attestation via HEC DAS portal immediately.",
                "Contact two professors for academic recommendation letters.",
            ]

        m3_actions = [
            MilestoneAction(
                action_id="act-m3-1",
                description="Obtain Police Character Clearance Certificate from local SSP Office / PKM",
                estimated_days=14,
                estimated_cost_pkr=3000,
                is_blocking=True,
            ),
            MilestoneAction(
                action_id="act-m3-2",
                description="Complete medical examination at country-designated panel clinic",
                estimated_days=7,
                estimated_cost_pkr=17000,
                is_blocking=True,
            ),
            MilestoneAction(
                action_id="act-m3-3",
                description="Attend VFS / Gerry's Biometric & Consular Visa Interview",
                estimated_days=21,
                estimated_cost_pkr=20000,
                is_blocking=True,
                assigned_office="VFS Global / Gerry's Pakistan",
            ),
        ]

        m3 = RoadmapMilestone(
            milestone_id="ms-phase-3",
            title="Consular Visa, Biometrics & Pre-Departure",
            phase=RoadmapPhase.EMBASSY_INTERVIEW_VISA,
            target_timeline_days="Day 36 to Day 60",
            total_phase_cost_pkr=sum(a.estimated_cost_pkr for a in m3_actions),
            actions=m3_actions,
            guidance_notes="Bring original verified/attested documents and scholarship award certificate in duplicate.",
        )

        if not student.language.has_english_test and scholarship.language.english_test_required:
            urgent_actions.append("Book computer-delivered IELTS Academic test date.")

        is_low_gpa = (0 < student.academic.gpa_percentage < 60.0) or (0 < student.academic.gpa_4_scale < 2.5)
        if is_low_gpa:
            urgent_actions.append(
                "Target Need-Based Grants: Prioritize Italian DSU Regional Grants (family income based) or Chinese Type-B Scholarships which accept passing academic marks."
            )

        total_budget = score_result.cost_analysis.total_out_of_pocket_pkr or 180000

        return ApplicationRoadmap(
            scholarship_id=scholarship.scholarship_id,
            scholarship_name=scholarship.name,
            host_country=scholarship.host_country_name,
            target_intake="Fall 2026",
            total_preparation_days_estimated=45,
            total_budget_needed_pkr=total_budget,
            milestones=[m1, m2, m3],
            relevant_pakistani_offices=offices,
            urgent_next_actions=urgent_actions,
        )

    async def generate_roadmap(
        self,
        scholarship: Scholarship,
        score_result: CompositeScoreResult,
        student: StudentProfile,
        event_callback: Optional[Callable[[ScholarXEvent], None]] = None,
    ) -> ApplicationRoadmap:
        """Generates comprehensive Pakistan-localized roadmap and emits SSE events."""
        session_id = student.session_id
        roadmap = self._generate_rule_based_roadmap(scholarship, score_result, student)

        if event_callback:
            evt = ScholarXEvent(
                session_id=session_id,
                event_type=AgentEventType.ROADMAP_GENERATED,
                agent_id="advisor_agent",
                agent_display_name="Final Advisor",
                component_type="AGENT",
                phase="RANKING",
                related_scholarship_id=scholarship.scholarship_id,
                payload={
                    "scholarship_name": scholarship.name,
                    "scholarship_id": scholarship.scholarship_id,
                    "host_country": scholarship.host_country_name,
                    "target_intake": roadmap.target_intake,
                    "total_milestones": len(roadmap.milestones),
                    "total_budget_pkr": roadmap.total_budget_needed_pkr,
                    "urgent_actions": roadmap.urgent_next_actions,
                    "milestones": [
                        {
                            "milestone_id": m.milestone_id,
                            "title": m.title,
                            "phase": m.phase.value if hasattr(m.phase, "value") else str(m.phase),
                            "target_timeline_days": m.target_timeline_days,
                            "total_phase_cost_pkr": m.total_phase_cost_pkr,
                            "guidance_notes": m.guidance_notes,
                            "actions": [
                                {
                                    "action_id": a.action_id,
                                    "description": a.description,
                                    "estimated_days": a.estimated_days,
                                    "estimated_cost_pkr": a.estimated_cost_pkr,
                                    "is_blocking": a.is_blocking,
                                    "assigned_office": a.assigned_office,
                                }
                                for a in m.actions
                            ],
                        }
                        for m in roadmap.milestones
                    ],
                    "offices": [
                        {
                            "office_name": o.office_name,
                            "office_type": o.office_type.value if hasattr(o.office_type, "value") else str(o.office_type),
                            "city": o.city,
                            "address": o.address,
                            "fee_pkr": o.fee_pkr,
                            "turnaround_days": o.estimated_turnaround_days,
                        }
                        for o in roadmap.relevant_pakistani_offices
                    ],
                },
                severity=EventSeverity.SUCCESS,
            )
            try:
                event_callback(evt)
            except Exception as e:
                logger.warning(f"Failed to invoke event callback: {e}")

        return roadmap
