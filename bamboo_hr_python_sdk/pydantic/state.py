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


class State(BaseModel):
    # The ID of the state
    id: typing.Optional[int] = Field(None, alias='id')

    # The name of the state
    name: typing.Optional[str] = Field(None, alias='name')

    # The abbreviation of the state
    abbrev: typing.Optional[str] = Field(None, alias='abbrev')

    # The ISO standard code of the state
    iso_code: typing.Optional[str] = Field(None, alias='iso_code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
