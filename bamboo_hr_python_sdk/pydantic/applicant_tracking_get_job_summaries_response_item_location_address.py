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


class ApplicantTrackingGetJobSummariesResponseItemLocationAddress(BaseModel):
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    address_line1: typing.Optional[typing.Optional[str]] = Field(None, alias='addressLine1')

    address_line2: typing.Optional[typing.Optional[str]] = Field(None, alias='addressLine2')

    city: typing.Optional[str] = Field(None, alias='city')

    state: typing.Optional[str] = Field(None, alias='state')

    zipcode: typing.Optional[str] = Field(None, alias='zipcode')

    country: typing.Optional[str] = Field(None, alias='country')

    phone_number: typing.Optional[typing.Optional[str]] = Field(None, alias='phoneNumber')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
