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


class RequiredTimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem(TypedDict):
    # Name of the task.
    name: str

class OptionalTimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem(TypedDict, total=False):
    # Indicates if the tasks is billable. Defaults to true if not provided.
    billable: bool

class TimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem(RequiredTimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem, OptionalTimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem):
    pass
