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

from bamboo_hr_python_sdk.pydantic.goals_get_all_aggregate_info_response_comments import GoalsGetAllAggregateInfoResponseComments
from bamboo_hr_python_sdk.pydantic.goals_get_all_aggregate_info_response_filters import GoalsGetAllAggregateInfoResponseFilters
from bamboo_hr_python_sdk.pydantic.goals_get_all_aggregate_info_response_goals import GoalsGetAllAggregateInfoResponseGoals
from bamboo_hr_python_sdk.pydantic.goals_get_all_aggregate_info_response_persons import GoalsGetAllAggregateInfoResponsePersons

class GoalsGetAllAggregateInfoResponse(BaseModel):
    # The selected user can align goals with other users.
    can_align: typing.Optional[bool] = Field(None, alias='canAlign')

    # The selected user can create a goal.
    can_create_goals: typing.Optional[bool] = Field(None, alias='canCreateGoals')

    filters: typing.Optional[GoalsGetAllAggregateInfoResponseFilters] = Field(None, alias='filters')

    # The id of the current selected filter.
    selected_filter: typing.Optional[str] = Field(None, alias='selectedFilter')

    goals: typing.Optional[GoalsGetAllAggregateInfoResponseGoals] = Field(None, alias='goals')

    persons: typing.Optional[GoalsGetAllAggregateInfoResponsePersons] = Field(None, alias='persons')

    comments: typing.Optional[GoalsGetAllAggregateInfoResponseComments] = Field(None, alias='comments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
