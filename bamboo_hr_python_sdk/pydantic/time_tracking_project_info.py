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

from bamboo_hr_python_sdk.pydantic.time_tracking_project import TimeTrackingProject
from bamboo_hr_python_sdk.pydantic.time_tracking_task import TimeTrackingTask

class TimeTrackingProjectInfo(BaseModel):
    project: typing.Optional[TimeTrackingProject] = Field(None, alias='project')

    task: typing.Optional[TimeTrackingTask] = Field(None, alias='task')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
