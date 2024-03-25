# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from bamboo_hr_python_sdk import schemas  # noqa: F401


class GoalsStatusCountResponseFilters(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    All the goals of the user seperated by filter.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['GoalsStatusCountResponseFiltersItem']:
            return GoalsStatusCountResponseFiltersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['GoalsStatusCountResponseFiltersItem'], typing.List['GoalsStatusCountResponseFiltersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GoalsStatusCountResponseFilters':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'GoalsStatusCountResponseFiltersItem':
        return super().__getitem__(i)

from bamboo_hr_python_sdk.model.goals_status_count_response_filters_item import GoalsStatusCountResponseFiltersItem
