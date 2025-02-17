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

from bamboo_hr_python_sdk.pydantic.time_tracking_private_beta_delete_time_sheet_entries_request_clock_entry_ids import TimeTrackingPrivateBetaDeleteTimeSheetEntriesRequestClockEntryIds

class TimeTrackingPrivateBetaDeleteTimeSheetEntriesRequest(BaseModel):
    clock_entry_ids: TimeTrackingPrivateBetaDeleteTimeSheetEntriesRequestClockEntryIds = Field(alias='clockEntryIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
