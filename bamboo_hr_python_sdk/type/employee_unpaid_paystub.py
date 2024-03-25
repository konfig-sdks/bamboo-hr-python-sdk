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

from bamboo_hr_python_sdk.type.employee_unpaid_paystub_unpaid_periods import EmployeeUnpaidPaystubUnpaidPeriods

class RequiredEmployeeUnpaidPaystub(TypedDict):
    pass

class OptionalEmployeeUnpaidPaystub(TypedDict, total=False):
    employeeId: str

    unpaidPeriods: EmployeeUnpaidPaystubUnpaidPeriods

class EmployeeUnpaidPaystub(RequiredEmployeeUnpaidPaystub, OptionalEmployeeUnpaidPaystub):
    pass
