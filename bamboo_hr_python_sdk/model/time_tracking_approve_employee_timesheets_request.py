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


class TimeTrackingApproveEmployeeTimesheetsRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "timesheets",
            "lastChanged",
        }
        
        class properties:
            lastChanged = schemas.IntSchema
        
            @staticmethod
            def timesheets() -> typing.Type['TimeTrackingApproveEmployeeTimesheetsRequestTimesheets']:
                return TimeTrackingApproveEmployeeTimesheetsRequestTimesheets
            __annotations__ = {
                "lastChanged": lastChanged,
                "timesheets": timesheets,
            }
    
    timesheets: 'TimeTrackingApproveEmployeeTimesheetsRequestTimesheets'
    lastChanged: MetaOapg.properties.lastChanged
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastChanged"]) -> MetaOapg.properties.lastChanged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timesheets"]) -> 'TimeTrackingApproveEmployeeTimesheetsRequestTimesheets': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lastChanged", "timesheets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastChanged"]) -> MetaOapg.properties.lastChanged: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timesheets"]) -> 'TimeTrackingApproveEmployeeTimesheetsRequestTimesheets': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lastChanged", "timesheets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        timesheets: 'TimeTrackingApproveEmployeeTimesheetsRequestTimesheets',
        lastChanged: typing.Union[MetaOapg.properties.lastChanged, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeTrackingApproveEmployeeTimesheetsRequest':
        return super().__new__(
            cls,
            *args,
            timesheets=timesheets,
            lastChanged=lastChanged,
            _configuration=_configuration,
            **kwargs,
        )

from bamboo_hr_python_sdk.model.time_tracking_approve_employee_timesheets_request_timesheets import TimeTrackingApproveEmployeeTimesheetsRequestTimesheets
