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

from bamboo_hr_python_sdk.pydantic.milestone import Milestone
from bamboo_hr_python_sdk.pydantic.new_goal_shared_with_employee_ids import NewGoalSharedWithEmployeeIds

class NewGoal(BaseModel):
    # [Required] The goal title.
    title: str = Field(alias='title')

    shared_with_employee_ids: NewGoalSharedWithEmployeeIds = Field(alias='sharedWithEmployeeIds')

    # [Required] The goal due date in YYYY-mm-dd format.
    due_date: str = Field(alias='dueDate')

    # [Optional] The goal description.
    description: typing.Optional[str] = Field(None, alias='description')

    # [Optional] The goal completion percentage (0 - 100). If completionDate is set, this value must be 100.
    percent_complete: typing.Optional[int] = Field(None, alias='percentComplete')

    # [Optional] The option ID that aligns with this goal.
    aligns_with_option_id: typing.Optional[str] = Field(None, alias='alignsWithOptionId')

    # [Optional] The date the goal was completed. If date is set, and no milestones are contained within this goal, percentComplete must be set to 100. If this goal does contain milestones, completion date cannot be set.
    completion_date: typing.Optional[typing.Union[int, float]] = Field(None, alias='completionDate')

    # [Optional] Milestones for the goal.
    milestones: typing.Optional[typing.List[Milestone]] = Field(None, alias='milestones')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
