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

from bamboo_hr_python_sdk.pydantic.company_benefit_response import CompanyBenefitResponse

BenefitsListCompanyBenefitsResponse = typing.List[CompanyBenefitResponse]
