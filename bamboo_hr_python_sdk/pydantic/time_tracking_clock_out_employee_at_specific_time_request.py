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


class TimeTrackingClockOutEmployeeAtSpecificTimeRequest(BaseModel):
    # Date time for clock out in atom format. 
    datetime: typing.Optional[str] = Field(None, alias='datetime')

    # Timezone of the time entry
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # The employeeId for the time entry.
    employee_id: typing.Optional[int] = Field(None, alias='employeeId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
