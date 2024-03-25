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


class BenefitGroupPlan(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            benefitGroupId = schemas.StrSchema
            benefitPlanId = schemas.StrSchema
            eligibility = schemas.StrSchema
            waitPeriod = schemas.StrSchema
            waitPeriodType = schemas.StrSchema
            startDate = schemas.StrSchema
            endDate = schemas.StrSchema
            __annotations__ = {
                "benefitGroupId": benefitGroupId,
                "benefitPlanId": benefitPlanId,
                "eligibility": eligibility,
                "waitPeriod": waitPeriod,
                "waitPeriodType": waitPeriodType,
                "startDate": startDate,
                "endDate": endDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitGroupId"]) -> MetaOapg.properties.benefitGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitPlanId"]) -> MetaOapg.properties.benefitPlanId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eligibility"]) -> MetaOapg.properties.eligibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waitPeriod"]) -> MetaOapg.properties.waitPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waitPeriodType"]) -> MetaOapg.properties.waitPeriodType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["benefitGroupId", "benefitPlanId", "eligibility", "waitPeriod", "waitPeriodType", "startDate", "endDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitGroupId"]) -> typing.Union[MetaOapg.properties.benefitGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitPlanId"]) -> typing.Union[MetaOapg.properties.benefitPlanId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eligibility"]) -> typing.Union[MetaOapg.properties.eligibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waitPeriod"]) -> typing.Union[MetaOapg.properties.waitPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waitPeriodType"]) -> typing.Union[MetaOapg.properties.waitPeriodType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["benefitGroupId", "benefitPlanId", "eligibility", "waitPeriod", "waitPeriodType", "startDate", "endDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        benefitGroupId: typing.Union[MetaOapg.properties.benefitGroupId, str, schemas.Unset] = schemas.unset,
        benefitPlanId: typing.Union[MetaOapg.properties.benefitPlanId, str, schemas.Unset] = schemas.unset,
        eligibility: typing.Union[MetaOapg.properties.eligibility, str, schemas.Unset] = schemas.unset,
        waitPeriod: typing.Union[MetaOapg.properties.waitPeriod, str, schemas.Unset] = schemas.unset,
        waitPeriodType: typing.Union[MetaOapg.properties.waitPeriodType, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BenefitGroupPlan':
        return super().__new__(
            cls,
            *args,
            benefitGroupId=benefitGroupId,
            benefitPlanId=benefitPlanId,
            eligibility=eligibility,
            waitPeriod=waitPeriod,
            waitPeriodType=waitPeriodType,
            startDate=startDate,
            endDate=endDate,
            _configuration=_configuration,
            **kwargs,
        )
