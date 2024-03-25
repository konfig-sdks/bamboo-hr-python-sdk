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


class GoalsGetGoalAggregateInfoResponseCommentsItem(BaseModel):
    # Id of the comment.
    id: typing.Optional[int] = Field(None, alias='id')

    # Id of the author of the comment.
    author_user_id: typing.Optional[int] = Field(None, alias='authorUserId')

    # The date and time that the comment was created.
    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    # The actual text of the comment.
    text: typing.Optional[str] = Field(None, alias='text')

    # Can the comment be edited.
    can_edit: typing.Optional[bool] = Field(None, alias='canEdit')

    # Can the comment be deleted.
    can_delete: typing.Optional[bool] = Field(None, alias='canDelete')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
