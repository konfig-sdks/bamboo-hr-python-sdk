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


class ApplicantTrackingCreateNewApplicationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "firstName",
            "jobId",
            "lastName",
        }
        
        class properties:
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            jobId = schemas.IntSchema
            email = schemas.StrSchema
            phoneNumber = schemas.StrSchema
            source = schemas.StrSchema
            address = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            zip = schemas.StrSchema
            country = schemas.StrSchema
            linkedinUrl = schemas.StrSchema
            dateAvailable = schemas.StrSchema
            desiredSalary = schemas.StrSchema
            referredBy = schemas.StrSchema
            websiteUrl = schemas.StrSchema
            
            
            class highestEducation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GED_OR_EQUIVALENT(cls):
                    return cls("GED or Equivalent")
                
                @schemas.classproperty
                def HIGH_SCHOOL(cls):
                    return cls("High School")
                
                @schemas.classproperty
                def SOME_COLLEGE(cls):
                    return cls("Some College")
                
                @schemas.classproperty
                def COLLEGE__ASSOCIATES(cls):
                    return cls("College - Associates")
                
                @schemas.classproperty
                def COLLEGE__BACHELOR_OF_ARTS(cls):
                    return cls("College - Bachelor of Arts")
                
                @schemas.classproperty
                def COLLEGE__BACHELOR_OF_FINE_ARTS(cls):
                    return cls("College - Bachelor of Fine Arts")
                
                @schemas.classproperty
                def COLLEGE__BACHELOR_OF_SCIENCE(cls):
                    return cls("College - Bachelor of Science")
                
                @schemas.classproperty
                def COLLEGE__MASTER_OF_ARTS(cls):
                    return cls("College - Master of Arts")
                
                @schemas.classproperty
                def COLLEGE__MASTER_OF_FINE_ARTS(cls):
                    return cls("College - Master of Fine Arts")
                
                @schemas.classproperty
                def COLLEGE__MASTER_OF_SCIENCE(cls):
                    return cls("College - Master of Science")
                
                @schemas.classproperty
                def COLLEGE__MASTER_OF_BUSINESS_ADMINISTRATION(cls):
                    return cls("College - Master of Business Administration")
                
                @schemas.classproperty
                def COLLEGE__DOCTORATE(cls):
                    return cls("College - Doctorate")
                
                @schemas.classproperty
                def MEDICAL_DOCTOR(cls):
                    return cls("Medical Doctor")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
            collegeName = schemas.StrSchema
            references = schemas.StrSchema
            resume = schemas.BinarySchema
            coverLetter = schemas.BinarySchema
            __annotations__ = {
                "firstName": firstName,
                "lastName": lastName,
                "jobId": jobId,
                "email": email,
                "phoneNumber": phoneNumber,
                "source": source,
                "address": address,
                "city": city,
                "state": state,
                "zip": zip,
                "country": country,
                "linkedinUrl": linkedinUrl,
                "dateAvailable": dateAvailable,
                "desiredSalary": desiredSalary,
                "referredBy": referredBy,
                "websiteUrl": websiteUrl,
                "highestEducation": highestEducation,
                "collegeName": collegeName,
                "references": references,
                "resume": resume,
                "coverLetter": coverLetter,
            }
    
    firstName: MetaOapg.properties.firstName
    jobId: MetaOapg.properties.jobId
    lastName: MetaOapg.properties.lastName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkedinUrl"]) -> MetaOapg.properties.linkedinUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateAvailable"]) -> MetaOapg.properties.dateAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desiredSalary"]) -> MetaOapg.properties.desiredSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referredBy"]) -> MetaOapg.properties.referredBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["websiteUrl"]) -> MetaOapg.properties.websiteUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["highestEducation"]) -> MetaOapg.properties.highestEducation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collegeName"]) -> MetaOapg.properties.collegeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["references"]) -> MetaOapg.properties.references: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resume"]) -> MetaOapg.properties.resume: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverLetter"]) -> MetaOapg.properties.coverLetter: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "jobId", "email", "phoneNumber", "source", "address", "city", "state", "zip", "country", "linkedinUrl", "dateAvailable", "desiredSalary", "referredBy", "websiteUrl", "highestEducation", "collegeName", "references", "resume", "coverLetter", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> typing.Union[MetaOapg.properties.zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkedinUrl"]) -> typing.Union[MetaOapg.properties.linkedinUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateAvailable"]) -> typing.Union[MetaOapg.properties.dateAvailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desiredSalary"]) -> typing.Union[MetaOapg.properties.desiredSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referredBy"]) -> typing.Union[MetaOapg.properties.referredBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["websiteUrl"]) -> typing.Union[MetaOapg.properties.websiteUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["highestEducation"]) -> typing.Union[MetaOapg.properties.highestEducation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collegeName"]) -> typing.Union[MetaOapg.properties.collegeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["references"]) -> typing.Union[MetaOapg.properties.references, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resume"]) -> typing.Union[MetaOapg.properties.resume, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverLetter"]) -> typing.Union[MetaOapg.properties.coverLetter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "jobId", "email", "phoneNumber", "source", "address", "city", "state", "zip", "country", "linkedinUrl", "dateAvailable", "desiredSalary", "referredBy", "websiteUrl", "highestEducation", "collegeName", "references", "resume", "coverLetter", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        jobId: typing.Union[MetaOapg.properties.jobId, decimal.Decimal, int, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        linkedinUrl: typing.Union[MetaOapg.properties.linkedinUrl, str, schemas.Unset] = schemas.unset,
        dateAvailable: typing.Union[MetaOapg.properties.dateAvailable, str, schemas.Unset] = schemas.unset,
        desiredSalary: typing.Union[MetaOapg.properties.desiredSalary, str, schemas.Unset] = schemas.unset,
        referredBy: typing.Union[MetaOapg.properties.referredBy, str, schemas.Unset] = schemas.unset,
        websiteUrl: typing.Union[MetaOapg.properties.websiteUrl, str, schemas.Unset] = schemas.unset,
        highestEducation: typing.Union[MetaOapg.properties.highestEducation, str, schemas.Unset] = schemas.unset,
        collegeName: typing.Union[MetaOapg.properties.collegeName, str, schemas.Unset] = schemas.unset,
        references: typing.Union[MetaOapg.properties.references, str, schemas.Unset] = schemas.unset,
        resume: typing.Union[MetaOapg.properties.resume, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        coverLetter: typing.Union[MetaOapg.properties.coverLetter, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantTrackingCreateNewApplicationRequest':
        return super().__new__(
            cls,
            *args,
            firstName=firstName,
            jobId=jobId,
            lastName=lastName,
            email=email,
            phoneNumber=phoneNumber,
            source=source,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            linkedinUrl=linkedinUrl,
            dateAvailable=dateAvailable,
            desiredSalary=desiredSalary,
            referredBy=referredBy,
            websiteUrl=websiteUrl,
            highestEducation=highestEducation,
            collegeName=collegeName,
            references=references,
            resume=resume,
            coverLetter=coverLetter,
            _configuration=_configuration,
            **kwargs,
        )
