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


class TimeTrackingPrivateBetaAddTimesheetClockInRequest(BaseModel):
    # id of the time tracking project that should be associated with the timesheet entry. Required if taskId is specified.
    project_id: typing.Optional[int] = Field(None, alias='projectId')

    # id of the time tracking task that should be associated with the timesheet entry.
    task_id: typing.Optional[int] = Field(None, alias='taskId')

    # The note that should be associated with the timesheet entry
    note: typing.Optional[str] = Field(None, alias='note')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
