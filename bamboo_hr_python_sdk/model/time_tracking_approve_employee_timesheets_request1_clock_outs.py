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


class TimeTrackingApproveEmployeeTimesheetsRequest1ClockOuts(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Array of clock out information
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TimeTrackingApproveEmployeeTimesheetsRequest1ClockOutsItem']:
            return TimeTrackingApproveEmployeeTimesheetsRequest1ClockOutsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TimeTrackingApproveEmployeeTimesheetsRequest1ClockOutsItem'], typing.List['TimeTrackingApproveEmployeeTimesheetsRequest1ClockOutsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TimeTrackingApproveEmployeeTimesheetsRequest1ClockOuts':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TimeTrackingApproveEmployeeTimesheetsRequest1ClockOutsItem':
        return super().__getitem__(i)

from bamboo_hr_python_sdk.model.time_tracking_approve_employee_timesheets_request1_clock_outs_item import TimeTrackingApproveEmployeeTimesheetsRequest1ClockOutsItem
