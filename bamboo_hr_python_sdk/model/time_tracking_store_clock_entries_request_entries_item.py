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


class TimeTrackingStoreClockEntriesRequestEntriesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.IntSchema
            date = schemas.StrSchema
            start = schemas.StrSchema
            end = schemas.StrSchema
            clockEntryId = schemas.IntSchema
            projectId = schemas.IntSchema
            taskId = schemas.IntSchema
            note = schemas.StrSchema
            __annotations__ = {
                "employeeId": employeeId,
                "date": date,
                "start": start,
                "end": end,
                "clockEntryId": clockEntryId,
                "projectId": projectId,
                "taskId": taskId,
                "note": note,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clockEntryId"]) -> MetaOapg.properties.clockEntryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskId"]) -> MetaOapg.properties.taskId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "date", "start", "end", "clockEntryId", "projectId", "taskId", "note", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clockEntryId"]) -> typing.Union[MetaOapg.properties.clockEntryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> typing.Union[MetaOapg.properties.projectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskId"]) -> typing.Union[MetaOapg.properties.taskId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "date", "start", "end", "clockEntryId", "projectId", "taskId", "note", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        start: typing.Union[MetaOapg.properties.start, str, schemas.Unset] = schemas.unset,
        end: typing.Union[MetaOapg.properties.end, str, schemas.Unset] = schemas.unset,
        clockEntryId: typing.Union[MetaOapg.properties.clockEntryId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        projectId: typing.Union[MetaOapg.properties.projectId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taskId: typing.Union[MetaOapg.properties.taskId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeTrackingStoreClockEntriesRequestEntriesItem':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            date=date,
            start=start,
            end=end,
            clockEntryId=clockEntryId,
            projectId=projectId,
            taskId=taskId,
            note=note,
            _configuration=_configuration,
            **kwargs,
        )
