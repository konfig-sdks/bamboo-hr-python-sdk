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

from bamboo_hr_python_sdk.pydantic.training_update_type_request_category import TrainingUpdateTypeRequestCategory

class TrainingUpdateTypeRequest(BaseModel):
    # Name of the training type.
    name: str = Field(alias='name')

    # Is this a required training?
    required: bool = Field(alias='required')

    # Description for the training.
    description: typing.Optional[str] = Field(None, alias='description')

    # The frequency is the (optional) amount of months between renewing trainings. Not valid if training are not renewable.
    frequency: typing.Optional[int] = Field(None, alias='frequency')

    # Renewable is optional but if you are setting it to true you must pass a frequency.
    renewable: typing.Optional[bool] = Field(None, alias='renewable')

    category: typing.Optional[TrainingUpdateTypeRequestCategory] = Field(None, alias='category')

    # Number of days before the training is due for new hires. Not valid unless training is required.
    due_from_hire_date: typing.Optional[int] = Field(None, alias='dueFromHireDate')

    # Optional URL that can be included with a training.
    link_url: typing.Optional[str] = Field(None, alias='linkUrl')

    # Allows all employees who can view the training to be able to mark it complete.
    allow_employees_to_mark_complete: typing.Optional[bool] = Field(None, alias='allowEmployeesToMarkComplete')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
