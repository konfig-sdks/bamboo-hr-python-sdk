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


class RequiredWebHookResponseLimit(TypedDict):
    pass

class OptionalWebHookResponseLimit(TypedDict, total=False):
    # The amount of records to send
    times: int

    # The minimum amount of seconds between requests
    seconds: int

class WebHookResponseLimit(RequiredWebHookResponseLimit, OptionalWebHookResponseLimit):
    pass
