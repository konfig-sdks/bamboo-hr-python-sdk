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


class GoalsGetGoalAggregateInfoResponseGoalActions(BaseModel):
    # Can the user edit the progress bar of this goal.
    can_edit_goal_progress_bar: typing.Optional[bool] = Field(None, alias='canEditGoalProgressBar')

    # can the user edit the progress of a milestone in this goal.
    can_edit_goal_milestone_progress_bar: typing.Optional[bool] = Field(None, alias='canEditGoalMilestoneProgressBar')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
