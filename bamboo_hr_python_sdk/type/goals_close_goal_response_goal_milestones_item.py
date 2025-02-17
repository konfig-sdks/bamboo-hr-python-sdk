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


class RequiredGoalsCloseGoalResponseGoalMilestonesItem(TypedDict):
    pass

class OptionalGoalsCloseGoalResponseGoalMilestonesItem(TypedDict, total=False):
    # The title of the milestone.
    title: str

    # The id of the milestone.
    id: int

    # The id of the goal which encompasses this milestone.
    employeeGoalId: int

    # The current value for a numeric milestone. This number will be rounded to the nearest hundreds. On the creation of a numeric milestone this value will automatically be set to the start value of the milestone. If the milestone is a simple checkbox milestone, this value will always be null.
    currentValue: typing.Union[int, float]

    # The starting value for a numeric milestone. This number will be rounded to the nearest hundreds. If the milestone is a simple checkbox milestone, this value will always be null.
    startValue: typing.Union[int, float]

    # The end goal for a numeric milestone. This number will be rounded to the nearest hundreds. If the milestone is a simple checkbox milestone, this value will always be null.
    endValue: typing.Union[int, float]

    # The date and time in which the goal has been completed. If the goal is not completed the value will be null.
    completedDateTime: str

    # The date and time in which the goal was last updated.
    lastUpdateDateDateTime: str

    # The ID of the user who last updated this milestone.
    lastUpdateUserId: int

class GoalsCloseGoalResponseGoalMilestonesItem(RequiredGoalsCloseGoalResponseGoalMilestonesItem, OptionalGoalsCloseGoalResponseGoalMilestonesItem):
    pass
