from typing import Optional
from pydantic import BaseModel, Field

def generate_endowment_schema(fiscal_year: int):
    fy_label = str(fiscal_year)
    fy_label_short = f"FY{fy_label}"
    fy_range = f"{fiscal_year}–{fiscal_year+1}"
    eoy_date = f"June 30, {fiscal_year}"

    class EndowmentAndInvestmentLevels(BaseModel):
        # ───── ENDOWMENT ASSETS ─────
        endowment_net_assets_eoy_total: Optional[int] = Field(
            description=(
                f"Total endowment net assets for the {fy_label} fiscal year (in thousands). "
                "Only extract from a table titled 'Changes in Endowment Net Assets' located in the Notes section. "
                f"Only use data explicitly labeled as '{fy_label}', '{fy_label_short}', or 'as of {eoy_date}'. "
                "Do not extract from general balance sheets, rollforwards, or systemwide summaries. "
                "Standardize all values to $000s using table metadata or heuristics."
            )
        )

        endowment_net_assets_eoy_with_donor_restrictions: Optional[int] = Field(
            description=(
                f"Total donor-restricted endowment net assets as of {eoy_date} (in thousands). "
                "Must be extracted from a 'Changes in Endowment Net Assets' table in the Notes section. "
                f"Exclude all {fiscal_year - 1} or earlier data. Must be clearly labeled as {fy_label}."
            )
        )

        endowment_net_assets_eoy_with_donor_restrictions_temporarily_restricted: Optional[int] = Field(
            description=(
                f"Temporarily restricted portion of donor-restricted endowment net assets for {fy_label_short} (in thousands). "
                f"Must appear in a table under Notes with a clear {fy_label} label. Ignore unlabeled or earlier year data."
            )
        )

        endowment_net_assets_eoy_with_donor_restrictions_permanently_restricted: Optional[int] = Field(
            description=(
                f"Permanently restricted portion of donor-restricted endowment net assets for {fy_label_short} (in thousands). "
                f"Only extract from Notes where clearly labeled as {fy_label}."
            )
        )

        endowment_net_assets_eoy_without_donor_restrictions: Optional[int] = Field(
            description=(
                f"Unrestricted portion of endowment net assets for the {fy_range} fiscal year (in thousands). "
                "Must be pulled from a 'Changes in Endowment Net Assets' table in Notes. "
                f"Only extract if labeled as {fy_label}. Ignore prior-year or aggregated system data."
            )
        )

        # ───── ENDOWMENT SPENDING ─────
        appropriation_of_endowment_for_expenditure_total: Optional[int] = Field(
            description=(
                f"Total appropriations or spending from the endowment during {fy_range} (in thousands). "
                "Only extract from the 'Changes in Endowment Net Assets' table in the Notes section. "
                "Do not infer from general text or extract from unlabeled rows."
            )
        )

        appropriation_of_endowment_for_expenditure_with_donor_restrictions: Optional[int] = Field(
            description=(
                f"Appropriations from donor-restricted endowment funds for {fy_label_short} (in thousands). "
                f"Must appear in a {fy_label}-labeled row of the Notes. Ignore prior years and total-only rows."
            )
        )

        appropriation_of_endowment_for_expenditure_without_donor_restrictions: Optional[int] = Field(
            description=(
                f"Appropriations from unrestricted endowment funds during {fy_range} (in thousands). "
                f"Must appear in a 'Changes in Endowment Net Assets' table and be labeled {fy_label}. Ignore earlier data."
            )
        )

        # ───── INVESTMENT VALUATION (FAIR VALUE HIERARCHY) ─────
        investment_level_1: Optional[int] = Field(
            description=(
                f"Fair value of Level 1 investments (quoted market prices) at {eoy_date} (in thousands). "
                "Only extract from a fair value hierarchy table in the Notes section. "
                "Ensure the table is for the university, not an enterprise or foundation. "
            )
        )

        investment_level_2: Optional[int] = Field(
            description=(
                f"Fair value of Level 2 investments (observable inputs) as of the end of {fy_label_short} (in thousands). "
                "Must be extracted from the same fair value hierarchy table in the Notes section. "
                f"Only use data labeled {fy_label}. Avoid mixing rows from different years or sources."
            )
        )

        investment_level_3: Optional[int] = Field(
            description=(
                f"Fair value of Level 3 investments (unobservable inputs) at year-end {fy_label} (in thousands). "
                f"Only extract from {fy_label}-labeled fair value tables in the Notes. Ignore mixed-year summaries."
            )
        )

        # ───── NAV & TOTAL FAIR VALUE ─────
        investments_measured_at_nav: Optional[int] = Field(
            description=(
                f"Total value of investments measured at Net Asset Value (NAV) at {eoy_date} (in thousands). "
                "Must be extracted from a Fair Value Hierarchy table in the Notes. "
                "Include Life Insurance Cash Surrender value if presented separately and applicable. "
                f"Ensure values are labeled as {fy_label} and not drawn from system-wide or multi-entity tables."
            )
        )

        investments_total_fair_value: Optional[int] = Field(
            description=(
                f"Total fair value of all university investments as of fiscal year end {fy_range} (in thousands). "
                "Must be sourced from the same fair value hierarchy table as NAV and Levels 1–3. "
                "Do not infer from text, and ignore totals from earlier years, foundations, or consolidated entities."
            )
        )

    return EndowmentAndInvestmentLevels
