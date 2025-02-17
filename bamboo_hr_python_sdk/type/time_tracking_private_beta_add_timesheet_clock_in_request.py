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


class RequiredTimeTrackingPrivateBetaAddTimesheetClockInRequest(TypedDict):
    pass

class OptionalTimeTrackingPrivateBetaAddTimesheetClockInRequest(TypedDict, total=False):
    # id of the time tracking project that should be associated with the timesheet entry. Required if taskId is specified.
    projectId: int

    # id of the time tracking task that should be associated with the timesheet entry.
    taskId: int

    # The note that should be associated with the timesheet entry
    note: str

class TimeTrackingPrivateBetaAddTimesheetClockInRequest(RequiredTimeTrackingPrivateBetaAddTimesheetClockInRequest, OptionalTimeTrackingPrivateBetaAddTimesheetClockInRequest):
    pass
