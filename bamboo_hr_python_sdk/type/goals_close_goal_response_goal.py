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

from bamboo_hr_python_sdk.type.goals_close_goal_response_goal_actions import GoalsCloseGoalResponseGoalActions
from bamboo_hr_python_sdk.type.goals_close_goal_response_goal_milestones import GoalsCloseGoalResponseGoalMilestones
from bamboo_hr_python_sdk.type.goals_close_goal_response_goal_shared_with_employee_ids import GoalsCloseGoalResponseGoalSharedWithEmployeeIds

class RequiredGoalsCloseGoalResponseGoal(TypedDict):
    pass

class OptionalGoalsCloseGoalResponseGoal(TypedDict, total=False):
    # Title of the goal.
    title: str

    # A description of the goal.
    description: str

    # The id of the goal.
    id: int

    # A percentage (1-100) that denotes how complete the goal is.
    percentComplete: int

    alignsWithOptionId: int

    sharedWithEmployeeIds: GoalsCloseGoalResponseGoalSharedWithEmployeeIds

    # The due date of the goal.
    dueDate: date

    # The date the goal was completed.
    completionDate: date

    # The status of the goal.
    status: str

    milestones: GoalsCloseGoalResponseGoalMilestones

    actions: GoalsCloseGoalResponseGoalActions

class GoalsCloseGoalResponseGoal(RequiredGoalsCloseGoalResponseGoal, OptionalGoalsCloseGoalResponseGoal):
    pass
