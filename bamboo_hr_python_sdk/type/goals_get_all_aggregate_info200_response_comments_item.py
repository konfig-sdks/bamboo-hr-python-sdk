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


class RequiredGoalsGetAllAggregateInfo200ResponseCommentsItem(TypedDict):
    pass

class OptionalGoalsGetAllAggregateInfo200ResponseCommentsItem(TypedDict, total=False):
    # The goalId that the comments are linked to.
    goalId: int

    # How many comments are linked to the goal
    commentCount: int

class GoalsGetAllAggregateInfo200ResponseCommentsItem(RequiredGoalsGetAllAggregateInfo200ResponseCommentsItem, OptionalGoalsGetAllAggregateInfo200ResponseCommentsItem):
    pass
