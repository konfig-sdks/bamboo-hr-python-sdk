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


class GoalsGetAllAggregateInfo200Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            canAlign = schemas.BoolSchema
            canCreateGoals = schemas.BoolSchema
        
            @staticmethod
            def filters() -> typing.Type['GoalsGetAllAggregateInfo200ResponseFilters']:
                return GoalsGetAllAggregateInfo200ResponseFilters
            selectedFilter = schemas.StrSchema
        
            @staticmethod
            def goals() -> typing.Type['GoalsGetAllAggregateInfo200ResponseGoals']:
                return GoalsGetAllAggregateInfo200ResponseGoals
        
            @staticmethod
            def persons() -> typing.Type['GoalsGetAllAggregateInfo200ResponsePersons']:
                return GoalsGetAllAggregateInfo200ResponsePersons
        
            @staticmethod
            def comments() -> typing.Type['GoalsGetAllAggregateInfo200ResponseComments']:
                return GoalsGetAllAggregateInfo200ResponseComments
            __annotations__ = {
                "canAlign": canAlign,
                "canCreateGoals": canCreateGoals,
                "filters": filters,
                "selectedFilter": selectedFilter,
                "goals": goals,
                "persons": persons,
                "comments": comments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canAlign"]) -> MetaOapg.properties.canAlign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canCreateGoals"]) -> MetaOapg.properties.canCreateGoals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filters"]) -> 'GoalsGetAllAggregateInfo200ResponseFilters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedFilter"]) -> MetaOapg.properties.selectedFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goals"]) -> 'GoalsGetAllAggregateInfo200ResponseGoals': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persons"]) -> 'GoalsGetAllAggregateInfo200ResponsePersons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> 'GoalsGetAllAggregateInfo200ResponseComments': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["canAlign", "canCreateGoals", "filters", "selectedFilter", "goals", "persons", "comments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canAlign"]) -> typing.Union[MetaOapg.properties.canAlign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canCreateGoals"]) -> typing.Union[MetaOapg.properties.canCreateGoals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union['GoalsGetAllAggregateInfo200ResponseFilters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedFilter"]) -> typing.Union[MetaOapg.properties.selectedFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goals"]) -> typing.Union['GoalsGetAllAggregateInfo200ResponseGoals', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persons"]) -> typing.Union['GoalsGetAllAggregateInfo200ResponsePersons', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union['GoalsGetAllAggregateInfo200ResponseComments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["canAlign", "canCreateGoals", "filters", "selectedFilter", "goals", "persons", "comments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        canAlign: typing.Union[MetaOapg.properties.canAlign, bool, schemas.Unset] = schemas.unset,
        canCreateGoals: typing.Union[MetaOapg.properties.canCreateGoals, bool, schemas.Unset] = schemas.unset,
        filters: typing.Union['GoalsGetAllAggregateInfo200ResponseFilters', schemas.Unset] = schemas.unset,
        selectedFilter: typing.Union[MetaOapg.properties.selectedFilter, str, schemas.Unset] = schemas.unset,
        goals: typing.Union['GoalsGetAllAggregateInfo200ResponseGoals', schemas.Unset] = schemas.unset,
        persons: typing.Union['GoalsGetAllAggregateInfo200ResponsePersons', schemas.Unset] = schemas.unset,
        comments: typing.Union['GoalsGetAllAggregateInfo200ResponseComments', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GoalsGetAllAggregateInfo200Response':
        return super().__new__(
            cls,
            *args,
            canAlign=canAlign,
            canCreateGoals=canCreateGoals,
            filters=filters,
            selectedFilter=selectedFilter,
            goals=goals,
            persons=persons,
            comments=comments,
            _configuration=_configuration,
            **kwargs,
        )

from bamboo_hr_python_sdk.model.goals_get_all_aggregate_info200_response_comments import GoalsGetAllAggregateInfo200ResponseComments
from bamboo_hr_python_sdk.model.goals_get_all_aggregate_info200_response_filters import GoalsGetAllAggregateInfo200ResponseFilters
from bamboo_hr_python_sdk.model.goals_get_all_aggregate_info200_response_goals import GoalsGetAllAggregateInfo200ResponseGoals
from bamboo_hr_python_sdk.model.goals_get_all_aggregate_info200_response_persons import GoalsGetAllAggregateInfo200ResponsePersons
