import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from schemas.scholarship import Scholarship, FundingType
from schemas.scoring import CostAnalysisResult, CostPhaseItem
from schemas.student import StudentProfile

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
COSTS_FILE = DATA_DIR / "pakistan_costs.json"

# Exchange rates benchmark (PKR) fallback defaults
USD_TO_PKR = 280
EUR_TO_PKR = 305
GBP_TO_PKR = 360


def load_costs_database() -> Dict[str, Any]:
    if COSTS_FILE.exists():
        try:
            with open(COSTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def get_exchange_rates() -> Dict[str, float]:
    """
    Dynamically loads exchange rates benchmark from pakistan_costs.json if available,
    falling back to standard benchmarks.
    """
    costs_db = load_costs_database()
    rates = costs_db.get("exchange_rates_benchmark", {})
    return {
        "USD": float(rates.get("USD", USD_TO_PKR)),
        "EUR": float(rates.get("EUR", EUR_TO_PKR)),
        "GBP": float(rates.get("GBP", GBP_TO_PKR)),
        "HUF": float(rates.get("HUF", 0.77)),
        "TRY": float(rates.get("TRY", 8.5)),
        "CNY": float(rates.get("CNY", 39.0)),
        "SAR": float(rates.get("SAR", 74.5)),
        "AED": float(rates.get("AED", 76.2)),
        "AUD": float(rates.get("AUD", 182)),
        "CAD": float(rates.get("CAD", 204)),
    }


def calculate_pakistan_costs(
    scholarship: Scholarship,
    student: StudentProfile,
) -> CostAnalysisResult:
    """
    Computes exact out-of-pocket costs for a Pakistani student in PKR.
    Differentiates between covered benefits and uncovered out-of-pocket obligations.
    Applies FBR Section 236Y advance card withholding tax and bank FX markup for international card payments.
    """
    rates = get_exchange_rates()
    usd_rate = rates.get("USD", USD_TO_PKR)
    eur_rate = rates.get("EUR", EUR_TO_PKR)
    gbp_rate = rates.get("GBP", GBP_TO_PKR)

    pre_app_items: List[CostPhaseItem] = []
    app_items: List[CostPhaseItem] = []
    visa_items: List[CostPhaseItem] = []
    settle_items: List[CostPhaseItem] = []
    warnings: List[str] = []

    app_intl_card_spend_pkr = 0
    visa_intl_card_spend_pkr = 0

    # 1. Pre-Application Phase
    # English test
    if scholarship.language.english_test_required:
        if not student.language.has_english_test:
            # Student needs to take IELTS
            pre_app_items.append(
                CostPhaseItem(
                    item_name="IELTS Academic Exam Fee (British Council/AEO PK)",
                    cost_pkr=76000,
                    cost_usd=round(76000 / usd_rate),
                    is_mandatory=True,
                    pakistan_context="Computer-delivered IELTS Academic test across Pakistan.",
                )
            )

    # HEC Tests
    if scholarship.pakistan_requirements.hec_usat_required and student.standardized_tests.hec_usat is None:
        pre_app_items.append(
            CostPhaseItem(
                item_name="HEC USAT Registration Fee",
                cost_pkr=2500,
                cost_usd=round(2500 / usd_rate),
                is_mandatory=True,
                pakistan_context="Required for undergraduate bilateral quotas.",
            )
        )
    if scholarship.pakistan_requirements.hec_hat_required and student.standardized_tests.hec_hat is None:
        pre_app_items.append(
            CostPhaseItem(
                item_name="HEC HAT Registration Fee",
                cost_pkr=2500,
                cost_usd=round(2500 / usd_rate),
                is_mandatory=True,
                pakistan_context="Required for postgraduate bilateral quotas.",
            )
        )

    # Document Attestations
    if scholarship.pakistan_requirements.hec_attestation_required and not student.academic.hec_attestation_done:
        pre_app_items.append(
            CostPhaseItem(
                item_name="HEC Degree Attestation (DAS e-Attestation)",
                cost_pkr=3000,
                cost_usd=round(3000 / usd_rate),
                is_mandatory=True,
                pakistan_context="Online 1-Link payment for digital e-Attestation certificate.",
            )
        )

    if scholarship.pakistan_requirements.ibcc_equivalence_required and not student.academic.ibcc_equivalence_done:
        pre_app_items.append(
            CostPhaseItem(
                item_name="IBCC Equivalence Certificate Fee",
                cost_pkr=6000,
                cost_usd=round(6000 / usd_rate),
                is_mandatory=True,
                pakistan_context="IBCC Islamabad verification & equivalence fee.",
            )
        )

    if scholarship.pakistan_requirements.mofa_attestation_required:
        pre_app_items.append(
            CostPhaseItem(
                item_name="Ministry of Foreign Affairs (MOFA) Apostille/Stamps",
                cost_pkr=1000,
                cost_usd=round(1000 / usd_rate),
                is_mandatory=True,
                pakistan_context="MOFA stamp per document at Camp Office.",
            )
        )

    # 2. Application Phase
    # German Uni-Assist or application portals
    if scholarship.host_country == "DE":
        uni_assist_pkr = round(75 * eur_rate)
        app_intl_card_spend_pkr += uni_assist_pkr
        app_items.append(
            CostPhaseItem(
                item_name="Uni-Assist Processing Fee (EUR 75)",
                cost_pkr=uni_assist_pkr,
                cost_usd=round(uni_assist_pkr / usd_rate),
                is_mandatory=True,
                pakistan_context="Uni-Assist evaluation portal fee for German universities.",
            )
        )

    # 3. Visa & Travel Phase
    country = scholarship.host_country
    # Visa fee
    if country in ("TR", "HU"):
        visa_items.append(
            CostPhaseItem(
                item_name="Student Visa Fee (Exempt for Bilateral Scholarship)",
                cost_pkr=0,
                cost_usd=0,
                is_mandatory=False,
                pakistan_context="Visa fee is waived by embassy for official scholarship recipients.",
            )
        )
    elif country in ("DE", "IT", "FR", "ES", "AT", "PL"):
        visa_items.append(
            CostPhaseItem(
                item_name="Schengen National Student Visa (EUR 90)",
                cost_pkr=round(90 * eur_rate),
                cost_usd=round((90 * eur_rate) / usd_rate),
                is_mandatory=True,
                pakistan_context="Official consular visa fee paid to embassy or Gerry's drop box.",
            )
        )
    elif country == "US":
        us_visa_pkr = round(185 * usd_rate)
        visa_intl_card_spend_pkr += us_visa_pkr
        visa_items.append(
            CostPhaseItem(
                item_name="US DS-160 / SEVIS & J-1/F-1 Visa Application Fee",
                cost_pkr=us_visa_pkr,
                cost_usd=185,
                is_mandatory=True,
                pakistan_context="US Embassy Islamabad / Karachi consulate interview fee.",
            )
        )
    elif country == "GB":
        uk_visa_pkr = round(558 * gbp_rate)
        visa_intl_card_spend_pkr += uk_visa_pkr
        visa_items.append(
            CostPhaseItem(
                item_name="UK Student Visa (GBP 558)",
                cost_pkr=uk_visa_pkr,
                cost_usd=round(uk_visa_pkr / usd_rate),
                is_mandatory=True,
                pakistan_context="UKVI Student visa fee.",
            )
        )
    else:
        visa_items.append(
            CostPhaseItem(
                item_name="Student Visa & Processing Fee",
                cost_pkr=25000,
                cost_usd=round(25000 / usd_rate),
                is_mandatory=True,
            )
        )

    # VFS Gerry's biometric fee
    visa_items.append(
        CostPhaseItem(
            item_name="VFS Global / Gerry's Biometric & Appointment Fee",
            cost_pkr=20000,
            cost_usd=round(20000 / usd_rate),
            is_mandatory=True,
            pakistan_context="Appointment and document handling at Gerry's center in PK.",
        )
    )

    # Panel medical exam & Police Character Certificate
    visa_items.append(
        CostPhaseItem(
            item_name="Approved Panel Clinic Medical Exam + Police Character Certificate",
            cost_pkr=20000,
            cost_usd=round(20000 / usd_rate),
            is_mandatory=True,
            pakistan_context="SSP Office character certificate (PKR 3,000) + clinic tests (PKR 17,000).",
        )
    )

    # Airfare
    if scholarship.funding.travel_airfare != "COVERED":
        # Estimate flight from Pakistan
        flight_cost = 180000 if country in ("TR", "HU", "CN", "AE", "SA") else 240000
        visa_items.append(
            CostPhaseItem(
                item_name="One-Way International Airfare from Pakistan",
                cost_pkr=flight_cost,
                cost_usd=round(flight_cost / usd_rate),
                is_mandatory=True,
                pakistan_context="Flight ticket from Islamabad/Lahore/Karachi to destination.",
            )
        )
        warnings.append(f"Airfare is not covered by scholarship (~PKR {flight_cost:,}).")

    # Card Processing & FBR Section 236Y Withholding Tax for international transactions
    total_card_spend_pkr = app_intl_card_spend_pkr + visa_intl_card_spend_pkr
    if total_card_spend_pkr > 0:
        is_tax_filer = getattr(student.preferences, "is_tax_filer", True)
        tax_rate = 0.05 if is_tax_filer else 0.10
        tax_label = "5% Filer" if is_tax_filer else "10% Non-Filer"
        tax_pkr = round(total_card_spend_pkr * tax_rate)
        card_fee_pkr = round(total_card_spend_pkr * 0.035)

        target_items = app_items if app_intl_card_spend_pkr > 0 and visa_intl_card_spend_pkr == 0 else visa_items
        target_items.append(
            CostPhaseItem(
                item_name=f"FBR Section 236Y Advance Tax on Card Payments ({tax_label})",
                cost_pkr=tax_pkr,
                cost_usd=round(tax_pkr / usd_rate),
                is_mandatory=True,
                pakistan_context=f"Mandatory FBR Section 236Y advance tax ({tax_label}) on international debit/credit card spending. Filers can adjust this against their annual income tax return.",
            )
        )
        target_items.append(
            CostPhaseItem(
                item_name="Bank Cross-Border Card Processing & FX Markup (3.5%)",
                cost_pkr=card_fee_pkr,
                cost_usd=round(card_fee_pkr / usd_rate),
                is_mandatory=True,
                pakistan_context="Standard 3.5% cross-border POS/e-commerce FX markup charged by Pakistani commercial banks on foreign currency card payments.",
            )
        )
        warnings.append(
            f"FBR Section 236Y Advance Tax ({tax_label}) & 3.5% card FX markup add PKR {tax_pkr + card_fee_pkr:,} on international card transactions."
        )

    # 4. Initial Settlement Phase
    # First month buffer before stipend arrives
    stipend_reserve = 75000
    settle_items.append(
        CostPhaseItem(
            item_name="First Month Emergency Reserve & Settlement",
            cost_pkr=stipend_reserve,
            cost_usd=round(stipend_reserve / usd_rate),
            is_mandatory=True,
            pakistan_context="Pocket money needed before bank account opens and stipend is disbursed.",
        )
    )

    # Mandatory blocked account (Sperrkonto) for European destinations when not fully funded
    if country in ("DE", "AT"):
        is_full = scholarship.funding.funding_type == FundingType.FULL
        has_living_stipend = bool(
            scholarship.funding.monthly_stipend
            and "none" not in scholarship.funding.monthly_stipend.lower()
            and "unfunded" not in scholarship.funding.monthly_stipend.lower()
        )
        if not (is_full and has_living_stipend):
            sperrkonto_eur = 11904 if country == "DE" else 12000
            sperrkonto_pkr = round(sperrkonto_eur * eur_rate)
            settle_items.append(
                CostPhaseItem(
                    item_name=f"Mandatory National Blocked Account (Sperrkonto - EUR {sperrkonto_eur:,})",
                    cost_pkr=sperrkonto_pkr,
                    cost_usd=round(sperrkonto_pkr / usd_rate),
                    is_mandatory=True,
                    pakistan_context="Compulsory visa requirement: Upfront blocked account deposit at Expatrio/Coracle/Fintiba to obtain student visa.",
                )
            )
            warnings.append(
                f"CRITICAL IMMIGRATION REQUIREMENT: {country} visa regulations mandate an upfront blocked account (Sperrkonto) of EUR {sperrkonto_eur:,} (~PKR {sperrkonto_pkr:,}) because this award does not provide a full living stipend."
            )

    # Sum totals
    pre_app_total = sum(i.cost_pkr for i in pre_app_items)
    app_total = sum(i.cost_pkr for i in app_items)
    visa_total = sum(i.cost_pkr for i in visa_items)
    settle_total = sum(i.cost_pkr for i in settle_items)
    grand_total_pkr = pre_app_total + app_total + visa_total + settle_total
    grand_total_usd = round(grand_total_pkr / usd_rate)

    max_budget = student.preferences.max_out_of_pocket_pkr
    shortfall = max(0, grand_total_pkr - max_budget)
    is_within = grand_total_pkr <= max_budget

    if not is_within:
        warnings.append(
            f"Estimated out-of-pocket (PKR {grand_total_pkr:,}) exceeds your budget constraint (PKR {max_budget:,}) by PKR {shortfall:,}."
        )

    # Funding score: 100 if fully within budget, scales down gracefully if exceeds
    if grand_total_pkr <= max_budget:
        funding_score = 100.0
    else:
        overshoot_ratio = (grand_total_pkr - max_budget) / max(1, max_budget)
        funding_score = max(20.0, round(100.0 - (overshoot_ratio * 50.0), 1))

    all_items = pre_app_items + app_items + visa_items + settle_items

    return CostAnalysisResult(
        pre_application_pkr=pre_app_total,
        application_pkr=app_total,
        visa_travel_pkr=visa_total,
        settlement_pkr=settle_total,
        total_out_of_pocket_pkr=grand_total_pkr,
        total_out_of_pocket_usd=grand_total_usd,
        student_max_budget_pkr=max_budget,
        shortfall_pkr=shortfall,
        is_within_budget=is_within,
        funding_score=funding_score,
        cost_items=all_items,
        risk_warnings=warnings,
    )
