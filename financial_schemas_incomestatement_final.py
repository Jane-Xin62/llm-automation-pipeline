from typing import Optional
from pydantic import BaseModel, Field, model_validator

def generate_income_statement_schema(fiscal_year: int):
    fy_label = str(fiscal_year)

    class IncomeStatement(BaseModel):
        # ─── OPERATING REVENUES ──────────────────────────────────────
        gross_tuition_revenue: Optional[int] = Field(
            description=f"Gross tuition revenue before financial aid for {fy_label}. "
                        "Look for labels like 'Gross Tuition and Fees'. Exclude net tuition or post-discounted amounts."
        )

        financial_aid: Optional[int] = Field(
            description=f"Institutional financial aid or tuition discounts for {fy_label}. "
                        "Labeled 'Scholarships', 'Grants', or 'Financial Aid'. Do not include federal aid."
        )

        net_tuition_revenue: Optional[int] = Field(
            description=f"Tuition revenue net of financial aid for {fy_label}. "
                        "Must be explicitly labeled as 'Net Tuition Revenue' or equivalent. Do not compute manually."
        )

        federal_grants_contracts: Optional[int] = Field(
            description=f"Federal operating grants and contracts for {fy_label}. "
                        "Look for 'Federal Grants & Contracts' in operating revenue section. Exclude capital grants."
        )

        state_local_grants_contracts: Optional[int] = Field(
            description=f"State or local government operating grants and contracts for {fy_label}. "
                        "Exclude restricted or capital-only support."
        )

        government_grants_contracts_total: Optional[int] = Field(
            description=f"Combined federal, state, and local grants/contracts for {fy_label}, if labeled as a total. "
                        "Do not compute unless explicitly stated."
        )

        state_appropriations: Optional[int] = Field(
            description=f"Base state funding or appropriations for {fy_label}. "
                        "Exclude capital-specific appropriations unless labeled as operating."
        )

        private_gifts_grants_contracts: Optional[int] = Field(
            description=f"Private support for operations for {fy_label}. "
                        "Includes gifts, contributions, grants. Must be unrestricted or labeled for current use."
        )

        total_gifts_contracts_other_support: Optional[int] = Field(
            description=f"Total of all gifts, grants, and other support for operations for {fy_label}. "
                        "Only extract if explicitly labeled as total. Do not sum manually."
        )

        private_gifts_with_donor_restrictions: Optional[int] = Field(
            description=f"Gifts or grants with donor restrictions for time or purpose, applicable to {fy_label}. "
                        "Must be clearly labeled. Do not infer from general private support."
        )

        investment_income_operations: Optional[int] = Field(
            description=f"Investment income available for operational use during {fy_label}. "
                        "May be labeled 'Operating Investment Income'. Exclude restricted or unrealized returns."
        )


        investment_income_total: Optional[int] = Field(
            description=f"Total investment income (dividends + interest) for {fy_label}. "
                        "Exclude gains/losses unless stated as included."
        )

        realized_gains_losses: Optional[int] = Field(
            description=f"Realized gains or losses on investments for {fy_label}. "
                        "Include only if specifically labeled. Do not combine with unrealized."
        )

        unrealized_gains_losses: Optional[int] = Field(
            description=f"Unrealized gains or losses for {fy_label}, typically due to fair value changes. "
                        "Must be labeled 'Unrealized'."
        )

        realized_unrealized_gains_combined: Optional[int] = Field(
            description=f"Combined realized/unrealized gains or losses for {fy_label}, if labeled together. "
                        "Exclude if the document breaks them out separately."
        )

        total_operating_investment_return: Optional[int] = Field(
            description=f"Total investment return used for operations, including realized/unrealized, for {fy_label}. "
                        "Only extract if labeled as 'Operating Investment Return' or equivalent."
        )

        investment_income_with_donor_restrictions: Optional[int] = Field(
            description=f"Operating investment income with donor restrictions for {fy_label}. "
                        "Must be explicitly labeled. Do not assume based on other investment lines."
        )

        auxiliary_enterprise_revenue: Optional[int] = Field(
            description=f"Revenue from auxiliary operations (e.g., housing, dining, parking) in {fy_label}. "
                        "Must be clearly labeled."
        )

        healthcare_clinical_revenue: Optional[int] = Field(
            description=f"Revenue from healthcare or clinical activities for {fy_label}. "
                        "Include only if clearly identified."
        )

        net_assets_released_from_restrictions: Optional[int] = Field(
            description=f"Net assets released from donor or legal restrictions in {fy_label}. "
                        "Labeled 'Net Assets Released from Restrictions'."
        )


        total_operating_revenue: Optional[int] = Field(
            description=f"Total operating revenue for {fy_label}. "
                        "Only extract if labeled. Do not compute."
        )

        # ─── FUNCTIONAL EXPENSES ─────────────────────────────────────
        instructional_expense: Optional[int] = Field(
            description=f"Instructional expenses for {fy_label}. "
                        "Include direct academic instruction."
        )

        research_expense: Optional[int] = Field(
            description=f"Research-related operational expenses for {fy_label}. "
                        "Exclude capitalized research infrastructure unless operational."
        )

        instructional_research_expense: Optional[int] = Field(
            description=f"Combined instruction & research expense line for {fy_label}, if labeled together. "
                        "Only use this if reported as one item."
        )

        auxiliary_enterprise_expense: Optional[int] = Field(
            description=f"Expenses related to auxiliary operations (e.g., dorms, food) for {fy_label}."
        )

        healthcare_clinical_expense: Optional[int] = Field(
            description=f"Clinical and healthcare expense for {fy_label}. "
                        "Include only if labeled clearly."
        )

        academic_support: Optional[int] = Field(
            description=f"Academic support services expenses (libraries, curriculum dev) in {fy_label}."
        )

        student_services: Optional[int] = Field(
            description=f"Expenses related to student services (advising, career, etc.) for {fy_label}."
        )

        institutional_support: Optional[int] = Field(
            description=f"Institutional overhead and general administrative expenses for {fy_label}."
        )

        public_service_expense: Optional[int] = Field(
            description=f"Public/community service operating expenses for {fy_label}."
        )

        student_aid_expense: Optional[int] = Field(
            description=f"Scholarships and fellowships recognized as expense, not offsets to revenue, for {fy_label}."
        )


        total_operating_expense: Optional[int] = Field(
            description=f"Total of all functional operating expenses for {fy_label}. "
                        "Only extract if labeled."
        )

        net_operating_income: Optional[int] = Field(
            description=f"Net income from operations for {fy_label} (Total Revenue - Total Expenses). "
                        "Do not compute. Only extract if labeled 'Net Operating Income' or equivalent."
        )

        # ─── NON-OPERATING ACTIVITY ──────────────────────────────────
        non_op_realized_gains: Optional[int] = Field(
            description=f"Realized gains from investments reported as non-operating in {fy_label}."
        )


        non_operating_revenue: Optional[int] = Field(
            description=f"Total non-operating revenue for {fy_label}, if explicitly labeled."
        )

        non_op_realized_losses: Optional[int] = Field(
            description=f"Realized losses from investments reported as non-operating in {fy_label}."
        )


        non_operating_expense: Optional[int] = Field(
            description=f"Total non-operating expenses for {fy_label}, if explicitly labeled."
        )

        non_op_realized_gains_with_restrictions: Optional[int] = Field(
            description=f"Realized investment gains with donor restrictions in {fy_label}. "
                        "Only extract if explicitly labeled with restrictions."
        )

        # ─── CHANGES IN NET ASSETS ───────────────────────────────────
        extraordinary_gain_or_loss: Optional[int] = Field(
            description=f"Extraordinary or one-time gain/loss for {fy_label}."
        )

        net_assets_released_for_capital: Optional[int] = Field(
            description=f"Net assets released from restriction for capital use in {fy_label}."
        )

        change_fair_value_derivatives: Optional[int] = Field(
            description=f"Change in fair market value of derivative instruments in {fy_label}."
        )

        capital_grants_gifts: Optional[int] = Field(
            description=f"Capital grants and gifts received during {fy_label}."
        )

        net_unrealized_investment_income: Optional[int] = Field(
            description=f"Net unrealized gains/losses on investments not included elsewhere in {fy_label}."
        )


        change_net_assets_without_donor_restrictions: Optional[int] = Field(
            description=f"Net change in unrestricted net assets for {fy_label}."
        )

        change_net_assets_with_donor_restrictions: Optional[int] = Field(
            description=f"Net change in restricted net assets for {fy_label}."
        )

        change_temp_restricted_net_assets: Optional[int] = Field(
            description=f"Change in temporarily restricted net assets for {fy_label}."
        )

        change_perm_restricted_net_assets: Optional[int] = Field(
            description=f"Change in permanently restricted net assets for {fy_label}."
        )


        total_change_in_net_assets: Optional[int] = Field(
            description=f"Final bottom-line change in total net assets for {fy_label}. "
                        "Only extract if explicitly stated. Do not derive."
        )

        #---Deterministic fields that are computed after all other fields are set
        @model_validator(mode="after")
        def compute_other_fields(self):
            def compute_other(total_field, *component_fields):
                total = getattr(self, total_field)
                comps = [getattr(self, f) for f in component_fields if getattr(self, f) is not None]
                return total - sum(comps) if total is not None and comps else None

            self.other_investment_income = compute_other(
                "investment_income_total", "investment_income_operations"
            )

            self.other_operating_revenue = compute_other(
                "total_operating_revenue",
                "gross_tuition_revenue", "net_tuition_revenue", "federal_grants_contracts",
                "state_local_grants_contracts", "government_grants_contracts_total",
                "state_appropriations", "private_gifts_grants_contracts",
                "total_gifts_contracts_other_support", "private_gifts_with_donor_restrictions",
                "investment_income_total", "auxiliary_enterprise_revenue",
                "healthcare_clinical_revenue", "net_assets_released_from_restrictions"
            )

            self.other_operating_expense = compute_other(
                "total_operating_expense",
                "instructional_expense", "research_expense", "instructional_research_expense",
                "auxiliary_enterprise_expense", "healthcare_clinical_expense", "academic_support",
                "student_services", "institutional_support", "public_service_expense",
                "student_aid_expense"
            )

            self.other_non_op_revenue = compute_other(
                "non_operating_revenue", "non_op_realized_gains"
            )

            self.other_non_op_expense = compute_other(
                "non_operating_expense", "non_op_realized_losses"
            )

            self.other_adj_net_assets_without_restrictions = compute_other(
                "change_net_assets_without_donor_restrictions", "net_assets_released_for_capital"
            )

            self.other_adj_to_net_assets = compute_other(
                "total_change_in_net_assets",
                "change_net_assets_without_donor_restrictions", "change_net_assets_with_donor_restrictions",
                "change_temp_restricted_net_assets", "change_perm_restricted_net_assets"
            )

            return self

        
    return IncomeStatement
