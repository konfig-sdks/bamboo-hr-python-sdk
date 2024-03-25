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


class ApplicantTrackingGetApplicationDetailsResponseJob(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def title() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseJobTitle']:
                return ApplicantTrackingGetApplicationDetailsResponseJobTitle
        
            @staticmethod
            def hiringLead() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseJobHiringLead']:
                return ApplicantTrackingGetApplicationDetailsResponseJobHiringLead
            id = schemas.NumberSchema
            __annotations__ = {
                "title": title,
                "hiringLead": hiringLead,
                "id": id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> 'ApplicantTrackingGetApplicationDetailsResponseJobTitle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hiringLead"]) -> 'ApplicantTrackingGetApplicationDetailsResponseJobHiringLead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "hiringLead", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseJobTitle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hiringLead"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseJobHiringLead', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "hiringLead", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union['ApplicantTrackingGetApplicationDetailsResponseJobTitle', schemas.Unset] = schemas.unset,
        hiringLead: typing.Union['ApplicantTrackingGetApplicationDetailsResponseJobHiringLead', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantTrackingGetApplicationDetailsResponseJob':
        return super().__new__(
            cls,
            *args,
            title=title,
            hiringLead=hiringLead,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_job_hiring_lead import ApplicantTrackingGetApplicationDetailsResponseJobHiringLead
from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_job_title import ApplicantTrackingGetApplicationDetailsResponseJobTitle
