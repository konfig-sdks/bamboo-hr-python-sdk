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


class GoalsGetAllAggregateInfoResponsePersonsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.IntSchema
            userId = schemas.IntSchema
            displayFirstName = schemas.StrSchema
            lastName = schemas.StrSchema
            photoUrl = schemas.StrSchema
            __annotations__ = {
                "employeeId": employeeId,
                "userId": userId,
                "displayFirstName": displayFirstName,
                "lastName": lastName,
                "photoUrl": photoUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayFirstName"]) -> MetaOapg.properties.displayFirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photoUrl"]) -> MetaOapg.properties.photoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "userId", "displayFirstName", "lastName", "photoUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayFirstName"]) -> typing.Union[MetaOapg.properties.displayFirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photoUrl"]) -> typing.Union[MetaOapg.properties.photoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "userId", "displayFirstName", "lastName", "photoUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        displayFirstName: typing.Union[MetaOapg.properties.displayFirstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        photoUrl: typing.Union[MetaOapg.properties.photoUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GoalsGetAllAggregateInfoResponsePersonsItem':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            userId=userId,
            displayFirstName=displayFirstName,
            lastName=lastName,
            photoUrl=photoUrl,
            _configuration=_configuration,
            **kwargs,
        )
