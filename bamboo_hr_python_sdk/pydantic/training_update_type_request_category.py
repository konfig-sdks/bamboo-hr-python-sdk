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


class TrainingUpdateTypeRequestCategory(BaseModel):
    # Category ID
    id: typing.Optional[int] = Field(None, alias='id')

    # Category Name
    name: typing.Optional[str] = Field(None, alias='name')

    # Accuracy in meters of the clock in location
    accuracy: typing.Optional[int] = Field(None, alias='accuracy')

    # Address...
    address: typing.Optional[str] = Field(None, alias='address')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
