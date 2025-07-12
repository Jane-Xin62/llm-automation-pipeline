from pydantic import BaseModel, Field
from typing import Optional, Type

from pydantic import BaseModel, Field
from typing import Optional, Type

def make_StatementOfFinancialPosition_model(year: int) -> Type[BaseModel]:
    """
    Dynamically constructs and returns a Pydantic model class named
    'StatementOfFinancialPosition_{year}', whose Field descriptions
    all mention the given year and explicitly instruct to focus only
    on the full Statement of Financial Position (Balance Sheet). Do not
    look at any condensed or net presentations, and do not perform any
    calculations—just capture the numbers exactly as they appear.
    """

    y_str = str(year)
    date_label = f"as of June 30, {year}"

    base_instruction = (
        "Only extract from the full Statement of Financial Position (Balance Sheet); "
        "do not use condensed or net financial position tables, and do not perform any "
        "calculations—capture the number exactly as shown. "
    )

    fields = {
        # --- Mandatory fields ---
        "year": (
            int,
            Field(..., description=base_instruction + f"The fiscal year for all line‐items: {year}.")
        ),
        "cash_and_short_term_investments_unrestricted_and_restricted": (
            Optional[int],
            Field(None, description=base_instruction + f"Cash & Short-Term Investments (both unrestricted & restricted) {date_label}.")
        ),
        "accumulated_depreciation": (
            Optional[int],
            Field(None, description=base_instruction + f"Accumulated Depreciation {date_label}.")
        ),
        "net_fixed_assets": (
            Optional[int],
            Field(None, description=base_instruction + f"Net Fixed Assets {date_label}.")
        ),
        "long_term_investments_unrestricted_and_restricted": (
            Optional[int],
            Field(None, description=base_instruction + f"Long-Term Investments (unrestricted & restricted) {date_label}.")
        ),
        "total_assets": (
            Optional[int],
            Field(None, description=base_instruction + f"Total Assets {date_label}.")
        ),
        "short_term_debt": (
            Optional[int],
            Field(None, description=base_instruction + f"Short-Term Debt {date_label}.")
        ),
        "long_term_debt": (
            Optional[int],
            Field(None, description=base_instruction + f"Long-Term Debt {date_label}.")
        ),
        "pension_and_opeb_liability": (
            Optional[int],
            Field(None, description=base_instruction + f"Pension & OPEB Liability {date_label}.")
        ),
        "total_liabilities": (
            Optional[int],
            Field(None, description=base_instruction + f"Total Liabilities {date_label}.")
        ),
        "net_assets_without_donor_restrictions": (
            Optional[int],
            Field(None, description=base_instruction + f"Net Assets without Donor Restrictions {date_label}.")
        ),
        "expendable_net_assets_with_donor_restrictions": (
            Optional[int],
            Field(None, description=base_instruction + f"Expendable Net Assets with Donor Restrictions {date_label}.")
        ),
        "perpetual_net_assets_with_donor_restrictions": (
            Optional[int],
            Field(None, description=base_instruction + f"Perpetual Net Assets with Donor Restrictions {date_label}.")
        ),
        "net_assets_with_donor_restrictions": (
            Optional[int],
            Field(None, description=base_instruction + f"Total Net Assets with Donor Restrictions {date_label}.")
        ),
        "total_net_assets": (
            Optional[int],
            Field(None, description=base_instruction + f"Total Net Assets {date_label}.")
        ),
        "total_liabilities_and_net_assets": (
            Optional[int],
            Field(None, description=base_instruction + f"Total Liabilities & Net Assets {date_label}.")
        ),

        # --- Nice-to-have (optional) fields ---
        "net_receivables": (
            Optional[int],
            Field(None, description=base_instruction + f"Net Receivables {date_label}. May be labeled 'Net Receivables'.")
        ),
        "rou_assets_finance_lease": (
            Optional[int],
            Field(None, description=base_instruction + f"ROU Assets – Finance Lease {date_label}.")
        ),
        "rou_assets_operating_lease": (
            Optional[int],
            Field(None, description=base_instruction + f"ROU Assets – Operating Lease {date_label}.")
        ),
        "other_assets": (
            Optional[int],
            Field(None, description=base_instruction + f"Other Assets {date_label}.")
        ),
        "current_portion_finance_lease": (
            Optional[int],
            Field(None, description=base_instruction + f"Current Portion of Finance Lease {date_label}.")
        ),
        "current_portion_long_term_debt": (
            Optional[int],
            Field(None, description=base_instruction + f"Current Portion of Long-Term Debt {date_label}.")
        ),
        "current_portion_operating_lease": (
            Optional[int],
            Field(None, description=base_instruction + f"Current Portion of Operating Lease {date_label}.")
        ),
        "accounts_payable": (
            Optional[int],
            Field(None, description=base_instruction + f"Accounts Payable {date_label}.")
        ),
        "deferred_revenue": (
            Optional[int],
            Field(None, description=base_instruction + f"Deferred Revenue {date_label}.")
        ),
        "long_term_finance_lease": (
            Optional[int],
            Field(None, description=base_instruction + f"Long-Term Finance Lease {date_label}.")
        ),
        "long_term_operating_lease": (
            Optional[int],
            Field(None, description=base_instruction + f"Long-Term Operating Lease {date_label}.")
        ),
        "swap_obligation_fmv": (
            Optional[int],
            Field(None, description=base_instruction + f"Swap Obligation (FMV) {date_label}.")
        ),
        "pension_liability": (
            Optional[int],
            Field(None, description=base_instruction + f"Pension Liability {date_label}.")
        ),
        "opeb_liability": (
            Optional[int],
            Field(None, description=base_instruction + f"OPEB Liability {date_label}.")
        ),
        "other_liabilities": (
            Optional[int],
            Field(None, description=base_instruction + f"Other Liabilities {date_label}.")
        ),
        "net_assets": (
            Optional[int],
            Field(None, description=base_instruction + f"Net Assets {date_label}.")
        ),
        "noncontrolling_interest": (
            Optional[int],
            Field(None, description=base_instruction + f"Noncontrolling Interest {date_label}.")
        ),
    }

    class_name = f"StatementOfFinancialPosition_{year}"
    namespace = {"__annotations__": {k: t for k, (t, _) in fields.items()}}
    for field_name, (_, field_def) in fields.items():
        namespace[field_name] = field_def

    return type(class_name, (BaseModel,), namespace)


# def make_StatementOfFinancialPosition_model(year: int) -> Type[BaseModel]:
#     """
#     Dynamically constructs and returns a Pydantic model class named
#     'StatementOfFinancialPosition_{year}', whose Field descriptions
#     all mention the given year and explicitly instruct to focus only
#     on the full Statement of Financial Position (Balance Sheet). Do not
#     look at any condensed or net presentations, and do not perform any
#     calculations—just capture the numbers exactly as they appear.
#     """

#     # Format strings once, so that all Field(...) descriptions refer to the right year.
#     y_str = str(year)
#     date_label = f"as of June 30, {year}"

#     # Base instruction to prepend to every Field description:
#     base_instruction = (
#         "Only extract from the full Statement of Financial Position (Balance Sheet); "
#         "do not use condensed or net financial position tables, and do not perform any calculations—"
#         "capture the number exactly as shown. "
#     )

#     # Create a dict of field definitions. Each value is a tuple (type, Field(...)).
#     fields = {
#         # Field name : (python_type, Field(...))
#         "year": (
#             int,
#             Field(
#                 ...,
#                 description=(
#                     f"{base_instruction}"
#                     "The fiscal year to which all other line‐items refer. "
#                     f"E.g. '{year}' means every balance (Cash, Liabilities, Net Assets, etc.) is 'as of June 30, {year}'."
#                 ),
#             ),
#         ),
#         "cash_and_short_term_investments_unrestricted_and_restricted": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Total of Cash & Short-Term Investments (both unrestricted and restricted) {date_label}. "
#                     "May be labeled 'Cash & Short-Term Investments (Unrestricted & Restricted)', "
#                     "'Cash and investments', or similar. Only extract if this amount clearly refers "
#                     f"to year-end {year}. Do not include petty cash or illiquid equivalents."
#                 ),
#             ),
#         ),
#         "accumulated_depreciation": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Accumulated Depreciation {date_label}. May be labeled 'Accumulated Depreciation', "
#                     "'Allowance for Depreciation', or similar. Only extract if explicitly shown "
#                     f"on the full Statement of Financial Position for {year}."
#                 ),
#             ),
#         ),
#         "net_fixed_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Net Fixed Assets (often reported below Accumulated Depreciation) {date_label}. "
#                     "May appear as 'Net Fixed Assets', 'Property, Plant & Equipment, Net', or similar. "
#                     f"Only extract if the {year} figure is explicitly shown on the full Statement of Financial Position; "
#                     "do not calculate by subtracting."
#                 ),
#             ),
#         ),
#         "long_term_investments_unrestricted_and_restricted": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Fair value or carrying value of Long-Term Investments (unrestricted & restricted) {date_label}. "
#                     "May be labeled 'Long-Term Investments (Unrestricted & Restricted)', 'Investments – Long-Term', "
#                     "or 'Noncurrent Investments'. Only extract if explicitly presented for that year on the "
#                     "full Statement of Financial Position."
#                 ),
#             ),
#         ),
#         "total_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Total Assets {date_label}. May be labeled 'Total Assets', 'Assets – Total', or similar. "
#                     "Only extract if explicitly provided on the full Statement of Financial Position; "
#                     "do not sum individual asset line‐items."
#                 ),
#             ),
#         ),
#         "short_term_debt": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Short-Term Debt (current portion of borrowings) {date_label}. "
#                     "May be labeled 'Short-Term Debt', 'Current Portion of Long-Term Debt', or similar. "
#                     f"Only extract if explicitly stated for {year} on the full Statement of Financial Position; "
#                     "do not infer or derive."
#                 ),
#             ),
#         ),
#         "long_term_debt": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Long-Term Debt (noncurrent portion) {date_label}. "
#                     "May appear as 'Long-Term Debt', 'Bonds and Notes Payable, net of current portion', or similar. "
#                     f"Only extract if explicitly reported for {year} on the full Statement of Financial Position; "
#                     "do not calculate by subtraction."
#                 ),
#             ),
#         ),
#         "pension_and_opeb_liability": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Combined Pension & OPEB Liability {date_label}. May be labeled 'Pension & OPEB Liability', "
#                     "'Postretirement Benefit Obligations', or similar. Only extract if explicitly shown for {year} "
#                     "on the full Statement of Financial Position."
#                 ),
#             ),
#         ),
#         "total_liabilities": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Total Liabilities {date_label}. May be labeled 'Total Liabilities', 'Liabilities – Total', or similar. "
#                     "Only extract if explicitly provided on the full Statement of Financial Position; "
#                     "do not sum individual line‐items."
#                 ),
#             ),
#         ),
#         "net_assets_without_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Net Assets without Donor Restrictions {date_label}. May be labeled 'Net Assets without Donor Restrictions', "
#                     "'Unrestricted Net Assets', or similar. Only extract if explicitly reported for {year} "
#                     "on the full Statement of Financial Position."
#                 ),
#             ),
#         ),
#         "expendable_net_assets_with_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Expendable Net Assets with Donor Restrictions {date_label}. May appear as "
#                     "'Expendable Net Assets with Donor Restrictions', 'Net Assets with Donor Restrictions – Expendable', or similar. "
#                     f"Only extract if explicitly shown for {year} on the full Statement of Financial Position; "
#                     "do not include nonexpendable portions."
#                 ),
#             ),
#         ),
#         "perpetual_net_assets_with_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Perpetual Net Assets with Donor Restrictions (including any earnings) {date_label}. "
#                     "May be labeled 'Perpetual Net Assets with Donor Restrictions', 'Restricted Endowment (Perpetual)', or similar. "
#                     f"Only extract if explicitly shown for {year} on the full Statement of Financial Position."
#                 ),
#             ),
#         ),
#         "net_assets_with_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Total Net Assets with Donor Restrictions {date_label}, including both expendable and perpetual. "
#                     "May be labeled 'Net Assets with Donor Restrictions', 'Restricted Net Assets – Total', or similar. "
#                     f"Only extract if explicitly reported for {year} on the full Statement of Financial Position; "
#                     "do not sum sub-components unless confirmed."
#                 ),
#             ),
#         ),
#         "total_net_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Total Net Assets (sum of Net Assets without Donor Restrictions and Net Assets with Donor Restrictions) {date_label}. "
#                     "May be labeled 'Total Net Assets' or similar. Only extract if explicitly provided for that year on the "
#                     "full Statement of Financial Position; do not sum unless the document confirms it."
#                 ),
#             ),
#         ),
#         "total_liabilities_and_net_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"{base_instruction}"
#                     f"Total Liabilities & Net Assets {date_label} (should equal Total Assets). "
#                     "May appear as 'Total Liabilities & Net Assets', 'Liabilities and Net Assets – Total', or similar. "
#                     f"Only extract if explicitly reported for {year} on the full Statement of Financial Position; "
#                     "do not infer."
#                 ),
#             ),
#         ),
#     }

#     # Build the dynamic class name, e.g. “StatementOfFinancialPosition_2024”
#     class_name = f"StatementOfFinancialPosition_{year}"

#     # Create the Pydantic model via type(). The “__annotations__” dict must match our fields.
#     namespace = {
#         "__annotations__": {name: typ for name, (typ, _) in fields.items()},
#     }

#     # Insert each Field(...) into the namespace so Pydantic picks it up
#     for field_name, (_, field_def) in fields.items():
#         namespace[field_name] = field_def

#     # Create and return the new BaseModel‐subclass
#     return type(class_name, (BaseModel,), namespace)


# def make_StatementOfFinancialPosition_model(year: int) -> Type[BaseModel]:
#     """
#     Dynamically constructs and returns a Pydantic model class named
#     'StatementOfFinancialPosition_{year}', whose Field descriptions
#     all mention the given year. You can then instantiate it for that year.
#     """

#     # Format strings once, so that all Field(...) descriptions refer to the right year.
#     y_str = str(year)
#     date_label = f"as of June 30, {year}"

#     # Create a dict of field definitions. Each value is a tuple (type, Field(...)).
#     fields = {
#         # Field name : (python_type, Field(...))
#         "year": (
#             int,
#             Field(
#                 ...,
#                 description=(
#                     "The fiscal year to which all other line‐items refer. "
#                     f"E.g. '{year}' means every balance (Cash, Liabilities, Net Assets, etc.) is 'as of June 30, {year}'."
#                 ),
#             ),
#         ),
#         "cash_and_short_term_investments_unrestricted_and_restricted": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Total of Cash & Short-Term Investments (both unrestricted and restricted) {date_label}. "
#                     "May be labeled 'Cash & Short-Term Investments (Unrestricted & Restricted)', "
#                     "'Cash and investments', or similar. Only extract if this amount clearly refers "
#                     f"to year-end {year}. Do not include petty cash or illiquid equivalents."
#                 ),
#             ),
#         ),
#         "accumulated_depreciation": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Accumulated Depreciation {date_label}. May be labeled 'Accumulated Depreciation', "
#                     "'Allowance for Depreciation', or similar. Only extract if explicitly shown "
#                     f"on the Statement of Financial Position for {year}."
#                 ),
#             ),
#         ),
#         "net_fixed_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Net Fixed Assets (often reported below Accumulated Depreciation) {date_label}. "
#                     "May appear as 'Net Fixed Assets', 'Property, Plant & Equipment, Net', or similar. "
#                     f"Only extract if the {year} figure is explicitly shown; do not calculate by subtracting."
#                 ),
#             ),
#         ),
#         "long_term_investments_unrestricted_and_restricted": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Fair value or carrying value of Long-Term Investments (unrestricted & restricted) {date_label}. "
#                     "May be labeled 'Long-Term Investments (Unrestricted & Restricted)', 'Investments – Long-Term', "
#                     "or 'Noncurrent Investments'. Only extract if explicitly presented for that year."
#                 ),
#             ),
#         ),
#         "total_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Total Assets {date_label}. May be labeled 'Total Assets', 'Assets – Total', or similar. "
#                     "Only extract if explicitly provided; do not sum individual asset line‐items."
#                 ),
#             ),
#         ),
#         "short_term_debt": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Short-Term Debt (current portion of borrowings) {date_label}. "
#                     "May be labeled 'Short-Term Debt', 'Current Portion of Long-Term Debt', or similar. "
#                     f"Only extract if explicitly stated for {year}; do not infer or derive."
#                 ),
#             ),
#         ),
#         "long_term_debt": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Long-Term Debt (noncurrent portion) {date_label}. "
#                     "May appear as 'Long-Term Debt', 'Bonds and Notes Payable, net of current portion', or similar. "
#                     f"Only extract if explicitly reported for {year}; do not calculate by subtraction."
#                 ),
#             ),
#         ),
#         "pension_and_opeb_liability": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Combined Pension & OPEB Liability {date_label}. May be labeled 'Pension & OPEB Liability', "
#                     "'Postretirement Benefit Obligations', or similar. Only extract if explicitly shown for {year}."
#                 ),
#             ),
#         ),
#         "total_liabilities": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Total Liabilities {date_label}. May be labeled 'Total Liabilities', 'Liabilities – Total', or similar. "
#                     "Only extract if explicitly provided; do not sum individual line‐items."
#                 ),
#             ),
#         ),
#         "net_assets_without_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Net Assets without Donor Restrictions {date_label}. May be labeled 'Net Assets without Donor Restrictions', "
#                     "'Unrestricted Net Assets', or similar. Only extract if explicitly reported for {year}."
#                 ),
#             ),
#         ),
#         "expendable_net_assets_with_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Expendable Net Assets with Donor Restrictions {date_label}. May appear as "
#                     "'Expendable Net Assets with Donor Restrictions', 'Net Assets with Donor Restrictions – Expendable', or similar. "
#                     f"Only extract if explicitly shown for {year}; do not include nonexpendable portions."
#                 ),
#             ),
#         ),
#         "perpetual_net_assets_with_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Perpetual Net Assets with Donor Restrictions (including any earnings) {date_label}. "
#                     "May be labeled 'Perpetual Net Assets with Donor Restrictions', 'Restricted Endowment (Perpetual)', or similar. "
#                     f"Only extract if explicitly shown for {year}."
#                 ),
#             ),
#         ),
#         "net_assets_with_donor_restrictions": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Total Net Assets with Donor Restrictions {date_label}, including both expendable and perpetual. "
#                     "May be labeled 'Net Assets with Donor Restrictions', 'Restricted Net Assets – Total', or similar. "
#                     f"Only extract if explicitly reported for {year}; do not sum sub-components unless confirmed."
#                 ),
#             ),
#         ),
#         "total_net_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Total Net Assets (sum of Net Assets without Donor Restrictions and Net Assets with Donor Restrictions) {date_label}. "
#                     "May be labeled 'Total Net Assets' or similar. Only extract if explicitly provided for that year; "
#                     "do not sum unless the document confirms it."
#                 ),
#             ),
#         ),
#         "total_liabilities_and_net_assets": (
#             Optional[int],
#             Field(
#                 None,
#                 description=(
#                     f"Total Liabilities & Net Assets {date_label} (should equal Total Assets). "
#                     "May appear as 'Total Liabilities & Net Assets', 'Liabilities and Net Assets – Total', or similar. "
#                     f"Only extract if explicitly reported for {year}; do not infer."
#                 ),
#             ),
#         ),
#     }

#     # Build the dynamic class name, e.g. “StatementOfFinancialPosition_2024”
#     class_name = f"StatementOfFinancialPosition_{year}"

#     # Create the Pydantic model via type().  The “__annotations__” dict must match our fields.
#     namespace = {
#         "__annotations__": {name: typ for name, (typ, _) in fields.items()},
#     }

#     # Insert each Field(...) into the namespace so Pydantic picks it up
#     for field_name, (_, field_def) in fields.items():
#         namespace[field_name] = field_def

#     # Create and return the new BaseModel‐subclass
#     return type(class_name, (BaseModel,), namespace)

# def make_StatementOfFinancialPosition_prompt(year: int) -> str:
#     """
#     Returns a Llama Cloud prompt that asks for the fifteen specified line‐items
#     from the Statement of Financial Position as of June 30, <year>, with no calculations.
#     """
#     y_str = str(year)
#     prompt = f"""
    
#     Extract the following fifteen line‐items from the Statement of Financial Position (Balance Sheet) as of June 30, {y_str}. 
#     Do not perform any calculations—only capture exactly what’s printed. If a line‐item is missing, return null. 
#     Output exactly one JSON object with these keys:
#     {{
#       "year": {y_str},
#       "cash_and_short_term_investments_unrestricted_and_restricted": null,
#       "accumulated_depreciation": null,
#       "net_fixed_assets": null,
#       "long_term_investments_unrestricted_and_restricted": null,
#       "total_assets": null,
#       "short_term_debt": null,
#       "long_term_debt": null,
#       "pension_and_opeb_liability": null,
#       "total_liabilities": null,
#       "net_assets_without_donor_restrictions": null,
#       "expendable_net_assets_with_donor_restrictions": null,
#       "perpetual_net_assets_with_donor_restrictions": null,
#       "net_assets_with_donor_restrictions": null,
#       "total_net_assets": null,
#       "total_liabilities_and_net_assets": null
#       }}
#       For each key, match any of these common label variants (or similar wording) but only capture the number if it’s explicitly shown “as of June
#       30, {y_str}”:
        
#         • cash_and_short_term_investments_unrestricted_and_restricted  
#           – “Cash & Short-Term Investments (Unrestricted & Restricted)”, “Cash and investments”, “Cash & Short-Term Investments”  
        
#         • accumulated_depreciation  
#           – “Accumulated Depreciation”, “Allowance for Depreciation”  
        
#         • net_fixed_assets  
#           – “Net Fixed Assets”, “Property, Plant & Equipment, Net”, “PP&E—Net”  
        
#         • long_term_investments_unrestricted_and_restricted  
#           – “Long-Term Investments (Unrestricted & Restricted)”, “Investments – Long-Term”, “Noncurrent Investments”  
        
#         • total_assets  
#           – “Total Assets”, “Assets – Total”, “Total Assets and Deferred Outflows” (only if shown exactly as of June 30, {y_str})  
        
#         • short_term_debt  
#           – “Short-Term Debt”, “Current Portion of Long-Term Debt”, “Current Debt”  
        
#         • long_term_debt  
#           – “Long-Term Debt”, “Bonds and Notes Payable, Net of Current Portion”, “Noncurrent Liabilities–Long-Term Debt”  
        
#         • pension_and_opeb_liability  
#           – “Pension & OPEB Liability”, “Postretirement Benefit Obligations”, “Employee Benefit Liabilities” (if explicitly broken out)  
        
#         • total_liabilities  
#           – “Total Liabilities”, “Liabilities–Total”, “Total Liabilities and Deferred Inflows” (only if shown exactly as of June 30, {y_str})  
        
#         • net_assets_without_donor_restrictions  
#           – “Net Assets without Donor Restrictions”, “Unrestricted Net Assets”, “Fund Balance–Unrestricted” (nonprofit format)  
        
#         • expendable_net_assets_with_donor_restrictions  
#           – “Expendable Net Assets with Donor Restrictions”, “Net Assets with Donor Restrictions–Expendable”, “Temporarily Restricted Net Assets”
#           (if explicitly “Expendable”)  
    
#         • perpetual_net_assets_with_donor_restrictions  
#           – “Perpetual Net Assets with Donor Restrictions”, “Restricted Endowment (Perpetual)”, “Permanently Restricted Net Assets”  
    
#         • net_assets_with_donor_restrictions  
#           – “Net Assets with Donor Restrictions”, “Restricted Net Assets–Total”, “Temporarily + Permanently Restricted Net Assets” (if both shown
#           together)  
    
#     • total_net_assets  
#     – “Total Net Assets”, “Net Assets–Total”, “Fund Balance–Total” (nonprofit format, if explicitly the sum)  
    
#     • total_liabilities_and_net_assets  
#     – “Total Liabilities & Net Assets”, “Liabilities and Net Assets–Total”, “Total Liabilities & Net Assets (should equal Total Assets)”
    
#     Return the filled‐in JSON object with numeric values or null for each key. Do not hard‐code any numbers—simply replace null with the actual
#     figure (or leave it null if absent).
#     """
#     return prompt
