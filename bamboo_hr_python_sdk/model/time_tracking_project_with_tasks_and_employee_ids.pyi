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


class TimeTrackingProjectWithTasksAndEmployeeIds(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            name = schemas.StrSchema
            
            
            class tasks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TimeTrackingTask']:
                        return TimeTrackingTask
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TimeTrackingTask'], typing.List['TimeTrackingTask']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tasks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TimeTrackingTask':
                    return super().__getitem__(i)
        
            @staticmethod
            def employeeIds() -> typing.Type['TimeTrackingProjectWithTasksAndEmployeeIdsEmployeeIds']:
                return TimeTrackingProjectWithTasksAndEmployeeIdsEmployeeIds
            __annotations__ = {
                "id": id,
                "name": name,
                "tasks": tasks,
                "employeeIds": employeeIds,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tasks"]) -> MetaOapg.properties.tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeIds"]) -> 'TimeTrackingProjectWithTasksAndEmployeeIdsEmployeeIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "tasks", "employeeIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tasks"]) -> typing.Union[MetaOapg.properties.tasks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeIds"]) -> typing.Union['TimeTrackingProjectWithTasksAndEmployeeIdsEmployeeIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "tasks", "employeeIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        tasks: typing.Union[MetaOapg.properties.tasks, list, tuple, schemas.Unset] = schemas.unset,
        employeeIds: typing.Union['TimeTrackingProjectWithTasksAndEmployeeIdsEmployeeIds', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeTrackingProjectWithTasksAndEmployeeIds':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            tasks=tasks,
            employeeIds=employeeIds,
            _configuration=_configuration,
            **kwargs,
        )

from bamboo_hr_python_sdk.model.time_tracking_project_with_tasks_and_employee_ids_employee_ids import TimeTrackingProjectWithTasksAndEmployeeIdsEmployeeIds
from bamboo_hr_python_sdk.model.time_tracking_task import TimeTrackingTask
