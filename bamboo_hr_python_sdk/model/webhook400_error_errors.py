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


class Webhook400ErrorErrors(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['Webhook400ErrorErrorsItem']:
            return Webhook400ErrorErrorsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['Webhook400ErrorErrorsItem'], typing.List['Webhook400ErrorErrorsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Webhook400ErrorErrors':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'Webhook400ErrorErrorsItem':
        return super().__getitem__(i)

from bamboo_hr_python_sdk.model.webhook400_error_errors_item import Webhook400ErrorErrorsItem
