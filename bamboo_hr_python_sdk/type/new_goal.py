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

from bamboo_hr_python_sdk.type.milestone import Milestone
from bamboo_hr_python_sdk.type.new_goal_shared_with_employee_ids import NewGoalSharedWithEmployeeIds

class RequiredNewGoal(TypedDict):
    # [Required] The goal title.
    title: str

    sharedWithEmployeeIds: NewGoalSharedWithEmployeeIds

    # [Required] The goal due date in YYYY-mm-dd format.
    dueDate: str

class OptionalNewGoal(TypedDict, total=False):
    # [Optional] The goal description.
    description: str

    # [Optional] The goal completion percentage (0 - 100). If completionDate is set, this value must be 100.
    percentComplete: int

    # [Optional] The option ID that aligns with this goal.
    alignsWithOptionId: str

    # [Optional] The date the goal was completed. If date is set, and no milestones are contained within this goal, percentComplete must be set to 100. If this goal does contain milestones, completion date cannot be set.
    completionDate: typing.Union[int, float]

    # [Optional] Milestones for the goal.
    milestones: typing.List[Milestone]

class NewGoal(RequiredNewGoal, OptionalNewGoal):
    pass
