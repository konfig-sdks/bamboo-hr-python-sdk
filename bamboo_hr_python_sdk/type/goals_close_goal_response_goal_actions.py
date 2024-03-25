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


class RequiredGoalsCloseGoalResponseGoalActions(TypedDict):
    pass

class OptionalGoalsCloseGoalResponseGoalActions(TypedDict, total=False):
    # Can the user edit the progress bar of this goal.
    canEditGoalProgressBar: bool

    # can the user edit the progress of a milestone in this goal.
    canEditGoalMilestoneProgressBar: bool

class GoalsCloseGoalResponseGoalActions(RequiredGoalsCloseGoalResponseGoalActions, OptionalGoalsCloseGoalResponseGoalActions):
    pass
