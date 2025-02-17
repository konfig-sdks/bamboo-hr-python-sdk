# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class EmployeeBenefit(BaseModel):
    # Employee ID
    employee_id: typing.Optional[int] = Field(None, alias='employeeId')

    # Company benefit ID
    company_benefit_id: typing.Optional[int] = Field(None, alias='companyBenefitId')

    # Company benefit name
    company_benefit_name: typing.Optional[str] = Field(None, alias='companyBenefitName')

    # Coverage level
    coverage_level: typing.Optional[str] = Field(None, alias='coverageLevel')

    # Deduction end date
    deduction_end_date: typing.Optional[date] = Field(None, alias='deductionEndDate')

    # Deduction start date
    deduction_start_date: typing.Optional[date] = Field(None, alias='deductionStartDate')

    # Enrollment status
    enrollment_status: typing.Optional[Literal["Eligible", "Enrolled", "Waived", "Withdrawn", "Terminated", "Ineligible"]] = Field(None, alias='enrollmentStatus')

    # Enrollment status effective date
    effective_date: typing.Optional[date] = Field(None, alias='effectiveDate')

    # Currency code
    currency_code: typing.Optional[str] = Field(None, alias='currencyCode')

    # Employee amount
    employee_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeAmount')

    # Employee amount type
    employee_amount_type: typing.Optional[str] = Field(None, alias='employeeAmountType')

    # Employee percent based on
    employee_percent_based_on: typing.Optional[str] = Field(None, alias='employeePercentBasedOn')

    # Employee cap amount
    employee_cap_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeCapAmount')

    # Employee cap amount type
    employee_cap_amount_type: typing.Optional[str] = Field(None, alias='employeeCapAmountType')

    # Employee annual max
    employee_annual_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeAnnualMax')

    # Company amount
    company_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='companyAmount')

    # Company amount type
    company_amount_type: typing.Optional[str] = Field(None, alias='companyAmountType')

    # Company percent based on
    company_percent_based_on: typing.Optional[str] = Field(None, alias='companyPercentBasedOn')

    # Company cap amount
    company_cap_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='companyCapAmount')

    # Company cap amount type
    company_cap_amount_type: typing.Optional[str] = Field(None, alias='companyCapAmountType')

    # Company annual max
    company_annual_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='companyAnnualMax')

    # Benefit Plan Coverage ID
    benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = Field(None, alias='benefitPlanCoverageId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
