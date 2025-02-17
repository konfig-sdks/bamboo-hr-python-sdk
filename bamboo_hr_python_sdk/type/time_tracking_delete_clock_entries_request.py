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

from bamboo_hr_python_sdk.type.time_tracking_delete_clock_entries_request_clock_entry_ids import TimeTrackingDeleteClockEntriesRequestClockEntryIds

class RequiredTimeTrackingDeleteClockEntriesRequest(TypedDict):
    pass

class OptionalTimeTrackingDeleteClockEntriesRequest(TypedDict, total=False):
    clockEntryIds: TimeTrackingDeleteClockEntriesRequestClockEntryIds

class TimeTrackingDeleteClockEntriesRequest(RequiredTimeTrackingDeleteClockEntriesRequest, OptionalTimeTrackingDeleteClockEntriesRequest):
    pass
