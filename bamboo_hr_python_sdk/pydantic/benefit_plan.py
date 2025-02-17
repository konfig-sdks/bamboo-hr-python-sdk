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


class BenefitPlan(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    name: typing.Optional[str] = Field(None, alias='name')

    type: typing.Optional[str] = Field(None, alias='type')

    deduction_type_id: typing.Optional[str] = Field(None, alias='deductionTypeId')

    start_ymd: typing.Optional[str] = Field(None, alias='startYmd')

    end_ymd: typing.Optional[str] = Field(None, alias='endYmd')

    url: typing.Optional[str] = Field(None, alias='url')

    meet_aca_min: typing.Optional[str] = Field(None, alias='meetAcaMin')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
