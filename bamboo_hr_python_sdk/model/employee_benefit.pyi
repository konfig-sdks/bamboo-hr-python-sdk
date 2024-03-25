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


class EmployeeBenefit(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.IntSchema
            companyBenefitId = schemas.IntSchema
            companyBenefitName = schemas.StrSchema
            coverageLevel = schemas.StrSchema
            deductionEndDate = schemas.DateSchema
            deductionStartDate = schemas.DateSchema
            
            
            class enrollmentStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ELIGIBLE(cls):
                    return cls("Eligible")
                
                @schemas.classproperty
                def ENROLLED(cls):
                    return cls("Enrolled")
                
                @schemas.classproperty
                def WAIVED(cls):
                    return cls("Waived")
                
                @schemas.classproperty
                def WITHDRAWN(cls):
                    return cls("Withdrawn")
                
                @schemas.classproperty
                def TERMINATED(cls):
                    return cls("Terminated")
                
                @schemas.classproperty
                def INELIGIBLE(cls):
                    return cls("Ineligible")
            effectiveDate = schemas.DateSchema
            currencyCode = schemas.StrSchema
            employeeAmount = schemas.NumberSchema
            employeeAmountType = schemas.StrSchema
            employeePercentBasedOn = schemas.StrSchema
            employeeCapAmount = schemas.NumberSchema
            employeeCapAmountType = schemas.StrSchema
            employeeAnnualMax = schemas.NumberSchema
            companyAmount = schemas.NumberSchema
            companyAmountType = schemas.StrSchema
            companyPercentBasedOn = schemas.StrSchema
            companyCapAmount = schemas.NumberSchema
            companyCapAmountType = schemas.StrSchema
            companyAnnualMax = schemas.NumberSchema
            benefitPlanCoverageId = schemas.NumberSchema
            __annotations__ = {
                "employeeId": employeeId,
                "companyBenefitId": companyBenefitId,
                "companyBenefitName": companyBenefitName,
                "coverageLevel": coverageLevel,
                "deductionEndDate": deductionEndDate,
                "deductionStartDate": deductionStartDate,
                "enrollmentStatus": enrollmentStatus,
                "effectiveDate": effectiveDate,
                "currencyCode": currencyCode,
                "employeeAmount": employeeAmount,
                "employeeAmountType": employeeAmountType,
                "employeePercentBasedOn": employeePercentBasedOn,
                "employeeCapAmount": employeeCapAmount,
                "employeeCapAmountType": employeeCapAmountType,
                "employeeAnnualMax": employeeAnnualMax,
                "companyAmount": companyAmount,
                "companyAmountType": companyAmountType,
                "companyPercentBasedOn": companyPercentBasedOn,
                "companyCapAmount": companyCapAmount,
                "companyCapAmountType": companyCapAmountType,
                "companyAnnualMax": companyAnnualMax,
                "benefitPlanCoverageId": benefitPlanCoverageId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyBenefitId"]) -> MetaOapg.properties.companyBenefitId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyBenefitName"]) -> MetaOapg.properties.companyBenefitName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverageLevel"]) -> MetaOapg.properties.coverageLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deductionEndDate"]) -> MetaOapg.properties.deductionEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deductionStartDate"]) -> MetaOapg.properties.deductionStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enrollmentStatus"]) -> MetaOapg.properties.enrollmentStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveDate"]) -> MetaOapg.properties.effectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeAmount"]) -> MetaOapg.properties.employeeAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeAmountType"]) -> MetaOapg.properties.employeeAmountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeePercentBasedOn"]) -> MetaOapg.properties.employeePercentBasedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeCapAmount"]) -> MetaOapg.properties.employeeCapAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeCapAmountType"]) -> MetaOapg.properties.employeeCapAmountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeAnnualMax"]) -> MetaOapg.properties.employeeAnnualMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyAmount"]) -> MetaOapg.properties.companyAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyAmountType"]) -> MetaOapg.properties.companyAmountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyPercentBasedOn"]) -> MetaOapg.properties.companyPercentBasedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyCapAmount"]) -> MetaOapg.properties.companyCapAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyCapAmountType"]) -> MetaOapg.properties.companyCapAmountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyAnnualMax"]) -> MetaOapg.properties.companyAnnualMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitPlanCoverageId"]) -> MetaOapg.properties.benefitPlanCoverageId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyBenefitId", "companyBenefitName", "coverageLevel", "deductionEndDate", "deductionStartDate", "enrollmentStatus", "effectiveDate", "currencyCode", "employeeAmount", "employeeAmountType", "employeePercentBasedOn", "employeeCapAmount", "employeeCapAmountType", "employeeAnnualMax", "companyAmount", "companyAmountType", "companyPercentBasedOn", "companyCapAmount", "companyCapAmountType", "companyAnnualMax", "benefitPlanCoverageId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyBenefitId"]) -> typing.Union[MetaOapg.properties.companyBenefitId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyBenefitName"]) -> typing.Union[MetaOapg.properties.companyBenefitName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverageLevel"]) -> typing.Union[MetaOapg.properties.coverageLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deductionEndDate"]) -> typing.Union[MetaOapg.properties.deductionEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deductionStartDate"]) -> typing.Union[MetaOapg.properties.deductionStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enrollmentStatus"]) -> typing.Union[MetaOapg.properties.enrollmentStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveDate"]) -> typing.Union[MetaOapg.properties.effectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeAmount"]) -> typing.Union[MetaOapg.properties.employeeAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeAmountType"]) -> typing.Union[MetaOapg.properties.employeeAmountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeePercentBasedOn"]) -> typing.Union[MetaOapg.properties.employeePercentBasedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeCapAmount"]) -> typing.Union[MetaOapg.properties.employeeCapAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeCapAmountType"]) -> typing.Union[MetaOapg.properties.employeeCapAmountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeAnnualMax"]) -> typing.Union[MetaOapg.properties.employeeAnnualMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyAmount"]) -> typing.Union[MetaOapg.properties.companyAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyAmountType"]) -> typing.Union[MetaOapg.properties.companyAmountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyPercentBasedOn"]) -> typing.Union[MetaOapg.properties.companyPercentBasedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyCapAmount"]) -> typing.Union[MetaOapg.properties.companyCapAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyCapAmountType"]) -> typing.Union[MetaOapg.properties.companyCapAmountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyAnnualMax"]) -> typing.Union[MetaOapg.properties.companyAnnualMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitPlanCoverageId"]) -> typing.Union[MetaOapg.properties.benefitPlanCoverageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyBenefitId", "companyBenefitName", "coverageLevel", "deductionEndDate", "deductionStartDate", "enrollmentStatus", "effectiveDate", "currencyCode", "employeeAmount", "employeeAmountType", "employeePercentBasedOn", "employeeCapAmount", "employeeCapAmountType", "employeeAnnualMax", "companyAmount", "companyAmountType", "companyPercentBasedOn", "companyCapAmount", "companyCapAmountType", "companyAnnualMax", "benefitPlanCoverageId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        companyBenefitId: typing.Union[MetaOapg.properties.companyBenefitId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        companyBenefitName: typing.Union[MetaOapg.properties.companyBenefitName, str, schemas.Unset] = schemas.unset,
        coverageLevel: typing.Union[MetaOapg.properties.coverageLevel, str, schemas.Unset] = schemas.unset,
        deductionEndDate: typing.Union[MetaOapg.properties.deductionEndDate, str, date, schemas.Unset] = schemas.unset,
        deductionStartDate: typing.Union[MetaOapg.properties.deductionStartDate, str, date, schemas.Unset] = schemas.unset,
        enrollmentStatus: typing.Union[MetaOapg.properties.enrollmentStatus, str, schemas.Unset] = schemas.unset,
        effectiveDate: typing.Union[MetaOapg.properties.effectiveDate, str, date, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, str, schemas.Unset] = schemas.unset,
        employeeAmount: typing.Union[MetaOapg.properties.employeeAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        employeeAmountType: typing.Union[MetaOapg.properties.employeeAmountType, str, schemas.Unset] = schemas.unset,
        employeePercentBasedOn: typing.Union[MetaOapg.properties.employeePercentBasedOn, str, schemas.Unset] = schemas.unset,
        employeeCapAmount: typing.Union[MetaOapg.properties.employeeCapAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        employeeCapAmountType: typing.Union[MetaOapg.properties.employeeCapAmountType, str, schemas.Unset] = schemas.unset,
        employeeAnnualMax: typing.Union[MetaOapg.properties.employeeAnnualMax, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        companyAmount: typing.Union[MetaOapg.properties.companyAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        companyAmountType: typing.Union[MetaOapg.properties.companyAmountType, str, schemas.Unset] = schemas.unset,
        companyPercentBasedOn: typing.Union[MetaOapg.properties.companyPercentBasedOn, str, schemas.Unset] = schemas.unset,
        companyCapAmount: typing.Union[MetaOapg.properties.companyCapAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        companyCapAmountType: typing.Union[MetaOapg.properties.companyCapAmountType, str, schemas.Unset] = schemas.unset,
        companyAnnualMax: typing.Union[MetaOapg.properties.companyAnnualMax, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        benefitPlanCoverageId: typing.Union[MetaOapg.properties.benefitPlanCoverageId, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeBenefit':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            companyBenefitId=companyBenefitId,
            companyBenefitName=companyBenefitName,
            coverageLevel=coverageLevel,
            deductionEndDate=deductionEndDate,
            deductionStartDate=deductionStartDate,
            enrollmentStatus=enrollmentStatus,
            effectiveDate=effectiveDate,
            currencyCode=currencyCode,
            employeeAmount=employeeAmount,
            employeeAmountType=employeeAmountType,
            employeePercentBasedOn=employeePercentBasedOn,
            employeeCapAmount=employeeCapAmount,
            employeeCapAmountType=employeeCapAmountType,
            employeeAnnualMax=employeeAnnualMax,
            companyAmount=companyAmount,
            companyAmountType=companyAmountType,
            companyPercentBasedOn=companyPercentBasedOn,
            companyCapAmount=companyCapAmount,
            companyCapAmountType=companyCapAmountType,
            companyAnnualMax=companyAnnualMax,
            benefitPlanCoverageId=benefitPlanCoverageId,
            _configuration=_configuration,
            **kwargs,
        )
