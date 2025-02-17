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


class RequiredEmployeeBenefit(TypedDict):
    pass

class OptionalEmployeeBenefit(TypedDict, total=False):
    # Employee ID
    employeeId: int

    # Company benefit ID
    companyBenefitId: int

    # Company benefit name
    companyBenefitName: str

    # Coverage level
    coverageLevel: str

    # Deduction end date
    deductionEndDate: date

    # Deduction start date
    deductionStartDate: date

    # Enrollment status
    enrollmentStatus: str

    # Enrollment status effective date
    effectiveDate: date

    # Currency code
    currencyCode: str

    # Employee amount
    employeeAmount: typing.Union[int, float]

    # Employee amount type
    employeeAmountType: str

    # Employee percent based on
    employeePercentBasedOn: str

    # Employee cap amount
    employeeCapAmount: typing.Union[int, float]

    # Employee cap amount type
    employeeCapAmountType: str

    # Employee annual max
    employeeAnnualMax: typing.Union[int, float]

    # Company amount
    companyAmount: typing.Union[int, float]

    # Company amount type
    companyAmountType: str

    # Company percent based on
    companyPercentBasedOn: str

    # Company cap amount
    companyCapAmount: typing.Union[int, float]

    # Company cap amount type
    companyCapAmountType: str

    # Company annual max
    companyAnnualMax: typing.Union[int, float]

    # Benefit Plan Coverage ID
    benefitPlanCoverageId: typing.Union[int, float]

class EmployeeBenefit(RequiredEmployeeBenefit, OptionalEmployeeBenefit):
    pass
