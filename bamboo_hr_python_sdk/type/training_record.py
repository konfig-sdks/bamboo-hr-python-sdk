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


class RequiredTrainingRecord(TypedDict):
    pass

class OptionalTrainingRecord(TypedDict, total=False):
    # The ID of the training record.
    id: int

    # The ID of the employee associated with the training.
    employeeId: int

    # Completed is a date in the format yyyy-mm-dd.
    completed: str

    # Notes left on the training record.
    notes: str

    # Name of the instructor.
    instructor: str

    # What was credited for the training record.
    credits: typing.Union[int, float]

    # Hours associated with the training record.
    hours: typing.Union[int, float]

    # The currency and cost for the training record.
    cost: str

    # The training type ID.
    type: int

class TrainingRecord(RequiredTrainingRecord, OptionalTrainingRecord):
    pass
