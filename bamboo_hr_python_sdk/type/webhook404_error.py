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

from bamboo_hr_python_sdk.type.webhook404_error_errors import Webhook404ErrorErrors

class RequiredWebhook404Error(TypedDict):
    pass

class OptionalWebhook404Error(TypedDict, total=False):
    errors: Webhook404ErrorErrors

class Webhook404Error(RequiredWebhook404Error, OptionalWebhook404Error):
    pass
