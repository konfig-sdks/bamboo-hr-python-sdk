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

from bamboo_hr_python_sdk.type.time_tracking_private_beta_create_project_task_request_tasks_item import TimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem

TimeTrackingPrivateBetaCreateProjectTaskRequestTasks = typing.List[TimeTrackingPrivateBetaCreateProjectTaskRequestTasksItem]
