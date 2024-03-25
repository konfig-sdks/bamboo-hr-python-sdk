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


class RequiredApplicantTrackingGetJobSummariesResponseItemLocationAddress(TypedDict):
    pass

class OptionalApplicantTrackingGetJobSummariesResponseItemLocationAddress(TypedDict, total=False):
    description: typing.Optional[str]

    name: typing.Optional[str]

    addressLine1: typing.Optional[str]

    addressLine2: typing.Optional[str]

    city: str

    state: str

    zipcode: str

    country: str

    phoneNumber: typing.Optional[str]

class ApplicantTrackingGetJobSummariesResponseItemLocationAddress(RequiredApplicantTrackingGetJobSummariesResponseItemLocationAddress, OptionalApplicantTrackingGetJobSummariesResponseItemLocationAddress):
    pass
