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


class RequiredEmployeesGetDirectory200Response(TypedDict):
    pass

class OptionalEmployeesGetDirectory200Response(TypedDict, total=False):
    # The ID of the employee
    id: str

class EmployeesGetDirectory200Response(RequiredEmployeesGetDirectory200Response, OptionalEmployeesGetDirectory200Response):
    pass
