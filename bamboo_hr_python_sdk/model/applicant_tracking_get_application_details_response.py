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


class ApplicantTrackingGetApplicationDetailsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.NumberSchema
            appliedDate = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseStatus']:
                return ApplicantTrackingGetApplicationDetailsResponseStatus
            rating = schemas.NumberSchema
            resumeFileId = schemas.NumberSchema
            coverLetterFileId = schemas.NumberSchema
        
            @staticmethod
            def movedTo() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseMovedTo']:
                return ApplicantTrackingGetApplicationDetailsResponseMovedTo
            
            
            class movedFrom(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'movedFrom':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            alsoAppliedToCount = schemas.NumberSchema
            duplicateApplicationCount = schemas.NumberSchema
            
            
            class referredBy(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'referredBy':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            desiredSalary = schemas.StrSchema
            commentCount = schemas.NumberSchema
            emailCount = schemas.NumberSchema
        
            @staticmethod
            def questionsAndAnswers() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseQuestionsAndAnswers']:
                return ApplicantTrackingGetApplicationDetailsResponseQuestionsAndAnswers
        
            @staticmethod
            def applicant() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseApplicant']:
                return ApplicantTrackingGetApplicationDetailsResponseApplicant
        
            @staticmethod
            def job() -> typing.Type['ApplicantTrackingGetApplicationDetailsResponseJob']:
                return ApplicantTrackingGetApplicationDetailsResponseJob
            __annotations__ = {
                "id": id,
                "appliedDate": appliedDate,
                "status": status,
                "rating": rating,
                "resumeFileId": resumeFileId,
                "coverLetterFileId": coverLetterFileId,
                "movedTo": movedTo,
                "movedFrom": movedFrom,
                "alsoAppliedToCount": alsoAppliedToCount,
                "duplicateApplicationCount": duplicateApplicationCount,
                "referredBy": referredBy,
                "desiredSalary": desiredSalary,
                "commentCount": commentCount,
                "emailCount": emailCount,
                "questionsAndAnswers": questionsAndAnswers,
                "applicant": applicant,
                "job": job,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appliedDate"]) -> MetaOapg.properties.appliedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ApplicantTrackingGetApplicationDetailsResponseStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating"]) -> MetaOapg.properties.rating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resumeFileId"]) -> MetaOapg.properties.resumeFileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverLetterFileId"]) -> MetaOapg.properties.coverLetterFileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["movedTo"]) -> 'ApplicantTrackingGetApplicationDetailsResponseMovedTo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["movedFrom"]) -> MetaOapg.properties.movedFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alsoAppliedToCount"]) -> MetaOapg.properties.alsoAppliedToCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duplicateApplicationCount"]) -> MetaOapg.properties.duplicateApplicationCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referredBy"]) -> MetaOapg.properties.referredBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desiredSalary"]) -> MetaOapg.properties.desiredSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commentCount"]) -> MetaOapg.properties.commentCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailCount"]) -> MetaOapg.properties.emailCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["questionsAndAnswers"]) -> 'ApplicantTrackingGetApplicationDetailsResponseQuestionsAndAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicant"]) -> 'ApplicantTrackingGetApplicationDetailsResponseApplicant': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job"]) -> 'ApplicantTrackingGetApplicationDetailsResponseJob': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "appliedDate", "status", "rating", "resumeFileId", "coverLetterFileId", "movedTo", "movedFrom", "alsoAppliedToCount", "duplicateApplicationCount", "referredBy", "desiredSalary", "commentCount", "emailCount", "questionsAndAnswers", "applicant", "job", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appliedDate"]) -> typing.Union[MetaOapg.properties.appliedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating"]) -> typing.Union[MetaOapg.properties.rating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resumeFileId"]) -> typing.Union[MetaOapg.properties.resumeFileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverLetterFileId"]) -> typing.Union[MetaOapg.properties.coverLetterFileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["movedTo"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseMovedTo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["movedFrom"]) -> typing.Union[MetaOapg.properties.movedFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alsoAppliedToCount"]) -> typing.Union[MetaOapg.properties.alsoAppliedToCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duplicateApplicationCount"]) -> typing.Union[MetaOapg.properties.duplicateApplicationCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referredBy"]) -> typing.Union[MetaOapg.properties.referredBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desiredSalary"]) -> typing.Union[MetaOapg.properties.desiredSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commentCount"]) -> typing.Union[MetaOapg.properties.commentCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailCount"]) -> typing.Union[MetaOapg.properties.emailCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["questionsAndAnswers"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseQuestionsAndAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicant"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseApplicant', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union['ApplicantTrackingGetApplicationDetailsResponseJob', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "appliedDate", "status", "rating", "resumeFileId", "coverLetterFileId", "movedTo", "movedFrom", "alsoAppliedToCount", "duplicateApplicationCount", "referredBy", "desiredSalary", "commentCount", "emailCount", "questionsAndAnswers", "applicant", "job", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        appliedDate: typing.Union[MetaOapg.properties.appliedDate, str, schemas.Unset] = schemas.unset,
        status: typing.Union['ApplicantTrackingGetApplicationDetailsResponseStatus', schemas.Unset] = schemas.unset,
        rating: typing.Union[MetaOapg.properties.rating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        resumeFileId: typing.Union[MetaOapg.properties.resumeFileId, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coverLetterFileId: typing.Union[MetaOapg.properties.coverLetterFileId, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        movedTo: typing.Union['ApplicantTrackingGetApplicationDetailsResponseMovedTo', schemas.Unset] = schemas.unset,
        movedFrom: typing.Union[MetaOapg.properties.movedFrom, None, str, schemas.Unset] = schemas.unset,
        alsoAppliedToCount: typing.Union[MetaOapg.properties.alsoAppliedToCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        duplicateApplicationCount: typing.Union[MetaOapg.properties.duplicateApplicationCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        referredBy: typing.Union[MetaOapg.properties.referredBy, None, str, schemas.Unset] = schemas.unset,
        desiredSalary: typing.Union[MetaOapg.properties.desiredSalary, str, schemas.Unset] = schemas.unset,
        commentCount: typing.Union[MetaOapg.properties.commentCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        emailCount: typing.Union[MetaOapg.properties.emailCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        questionsAndAnswers: typing.Union['ApplicantTrackingGetApplicationDetailsResponseQuestionsAndAnswers', schemas.Unset] = schemas.unset,
        applicant: typing.Union['ApplicantTrackingGetApplicationDetailsResponseApplicant', schemas.Unset] = schemas.unset,
        job: typing.Union['ApplicantTrackingGetApplicationDetailsResponseJob', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantTrackingGetApplicationDetailsResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            appliedDate=appliedDate,
            status=status,
            rating=rating,
            resumeFileId=resumeFileId,
            coverLetterFileId=coverLetterFileId,
            movedTo=movedTo,
            movedFrom=movedFrom,
            alsoAppliedToCount=alsoAppliedToCount,
            duplicateApplicationCount=duplicateApplicationCount,
            referredBy=referredBy,
            desiredSalary=desiredSalary,
            commentCount=commentCount,
            emailCount=emailCount,
            questionsAndAnswers=questionsAndAnswers,
            applicant=applicant,
            job=job,
            _configuration=_configuration,
            **kwargs,
        )

from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_applicant import ApplicantTrackingGetApplicationDetailsResponseApplicant
from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_job import ApplicantTrackingGetApplicationDetailsResponseJob
from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_moved_to import ApplicantTrackingGetApplicationDetailsResponseMovedTo
from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_questions_and_answers import ApplicantTrackingGetApplicationDetailsResponseQuestionsAndAnswers
from bamboo_hr_python_sdk.model.applicant_tracking_get_application_details_response_status import ApplicantTrackingGetApplicationDetailsResponseStatus
