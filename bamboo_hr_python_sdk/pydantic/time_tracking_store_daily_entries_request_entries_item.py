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


class TimeTrackingStoreDailyEntriesRequestEntriesItem(BaseModel):
    # employee id for the time entry
    employee_id: typing.Optional[int] = Field(None, alias='employeeId')

    # date of the time entry
    date: typing.Optional[str] = Field(None, alias='date')

    # The number of hours for the time entry.
    hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='hours')

    # The id of the daily entry if updating an existing entry
    daily_entry_id: typing.Optional[int] = Field(None, alias='dailyEntryId')

    # The id of the project associated with the time entry
    project_id: typing.Optional[int] = Field(None, alias='projectId')

    # The id of the task associated with the time entry
    task_id: typing.Optional[int] = Field(None, alias='taskId')

    note: typing.Optional[str] = Field(None, alias='note')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
