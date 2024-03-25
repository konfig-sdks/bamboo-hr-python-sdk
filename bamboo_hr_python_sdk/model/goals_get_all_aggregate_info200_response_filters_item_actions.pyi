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


class GoalsGetAllAggregateInfo200ResponseFiltersItemActions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    What actions a user can preform on this kind of goal.
    """


    class MetaOapg:
        
        class properties:
            canCloseGoal = schemas.BoolSchema
            canEditGoal = schemas.BoolSchema
            canEditGoalProgressBar = schemas.BoolSchema
            canReopenGoal = schemas.BoolSchema
            canShareGoal = schemas.BoolSchema
            __annotations__ = {
                "canCloseGoal": canCloseGoal,
                "canEditGoal": canEditGoal,
                "canEditGoalProgressBar": canEditGoalProgressBar,
                "canReopenGoal": canReopenGoal,
                "canShareGoal": canShareGoal,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canCloseGoal"]) -> MetaOapg.properties.canCloseGoal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canEditGoal"]) -> MetaOapg.properties.canEditGoal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canEditGoalProgressBar"]) -> MetaOapg.properties.canEditGoalProgressBar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canReopenGoal"]) -> MetaOapg.properties.canReopenGoal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canShareGoal"]) -> MetaOapg.properties.canShareGoal: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["canCloseGoal", "canEditGoal", "canEditGoalProgressBar", "canReopenGoal", "canShareGoal", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canCloseGoal"]) -> typing.Union[MetaOapg.properties.canCloseGoal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canEditGoal"]) -> typing.Union[MetaOapg.properties.canEditGoal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canEditGoalProgressBar"]) -> typing.Union[MetaOapg.properties.canEditGoalProgressBar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canReopenGoal"]) -> typing.Union[MetaOapg.properties.canReopenGoal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canShareGoal"]) -> typing.Union[MetaOapg.properties.canShareGoal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["canCloseGoal", "canEditGoal", "canEditGoalProgressBar", "canReopenGoal", "canShareGoal", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        canCloseGoal: typing.Union[MetaOapg.properties.canCloseGoal, bool, schemas.Unset] = schemas.unset,
        canEditGoal: typing.Union[MetaOapg.properties.canEditGoal, bool, schemas.Unset] = schemas.unset,
        canEditGoalProgressBar: typing.Union[MetaOapg.properties.canEditGoalProgressBar, bool, schemas.Unset] = schemas.unset,
        canReopenGoal: typing.Union[MetaOapg.properties.canReopenGoal, bool, schemas.Unset] = schemas.unset,
        canShareGoal: typing.Union[MetaOapg.properties.canShareGoal, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GoalsGetAllAggregateInfo200ResponseFiltersItemActions':
        return super().__new__(
            cls,
            *args,
            canCloseGoal=canCloseGoal,
            canEditGoal=canEditGoal,
            canEditGoalProgressBar=canEditGoalProgressBar,
            canReopenGoal=canReopenGoal,
            canShareGoal=canShareGoal,
            _configuration=_configuration,
            **kwargs,
        )
