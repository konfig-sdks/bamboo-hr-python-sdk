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


class TimeTrackingPrivateBetaAddEditHourEntriesRequestHoursItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "hours",
            "employeeId",
        }
        
        class properties:
            employeeId = schemas.IntSchema
            date = schemas.StrSchema
            hours = schemas.NumberSchema
            id = schemas.IntSchema
            projectId = schemas.IntSchema
            taskId = schemas.IntSchema
            note = schemas.StrSchema
            __annotations__ = {
                "employeeId": employeeId,
                "date": date,
                "hours": hours,
                "id": id,
                "projectId": projectId,
                "taskId": taskId,
                "note": note,
            }
    
    date: MetaOapg.properties.date
    hours: MetaOapg.properties.hours
    employeeId: MetaOapg.properties.employeeId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskId"]) -> MetaOapg.properties.taskId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "date", "hours", "id", "projectId", "taskId", "note", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> typing.Union[MetaOapg.properties.projectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskId"]) -> typing.Union[MetaOapg.properties.taskId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "date", "hours", "id", "projectId", "taskId", "note", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, ],
        hours: typing.Union[MetaOapg.properties.hours, decimal.Decimal, int, float, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        projectId: typing.Union[MetaOapg.properties.projectId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taskId: typing.Union[MetaOapg.properties.taskId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeTrackingPrivateBetaAddEditHourEntriesRequestHoursItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            hours=hours,
            employeeId=employeeId,
            id=id,
            projectId=projectId,
            taskId=taskId,
            note=note,
            _configuration=_configuration,
            **kwargs,
        )
