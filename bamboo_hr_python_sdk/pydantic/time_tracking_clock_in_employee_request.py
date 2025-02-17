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

from bamboo_hr_python_sdk.pydantic.time_tracking_clock_in_employee_request_clock_in_location import TimeTrackingClockInEmployeeRequestClockInLocation

class TimeTrackingClockInEmployeeRequest(BaseModel):
    # The start time for the clock in. In 24 hour format HH:MM
    start: typing.Optional[str] = Field(None, alias='start')

    # The timezone associated with the clock in.
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # The note associated with the clock in
    note: typing.Optional[str] = Field(None, alias='note')

    # The id of the project associated with the clock in
    project_id: typing.Optional[int] = Field(None, alias='projectId')

    # The id of the task associated with the clock in
    task_id: typing.Optional[int] = Field(None, alias='taskId')

    clock_in_location: typing.Optional[TimeTrackingClockInEmployeeRequestClockInLocation] = Field(None, alias='clockInLocation')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
