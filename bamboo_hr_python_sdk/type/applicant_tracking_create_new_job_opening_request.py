# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredApplicantTrackingCreateNewJobOpeningRequest(TypedDict):
    # The posting title of the job opening.
    postingTitle: str

    # The status of the job opening.
    jobStatus: str

    # The employee id (from the v1/applicant_tracking/hiring_leads endpoint) of the hiring lead for the job opening.
    hiringLead: int

    # The type of employment offered in the job opening, e.g. Full-Time, Part-Time, Contractor, etc.
    employmentType: str

    # The long-form text description of the job opening.
    jobDescription: str

class OptionalApplicantTrackingCreateNewJobOpeningRequest(TypedDict, total=False):
    # The department of the job opening.
    department: str

    # The minimum experience level that qualifies a candidate for the job opening.
    minimumExperience: str

    # The pay rate or compensation for the job opening.
    compensation: str

    # The location id (from the v1/applicant_tracking/locations endpoint) of the job opening. Omit this parameter for a remote job location.
    jobLocation: int

    # Whether the job opening application has a standard question for resume (true) or not (false) or if uploading a resume is mandatory (required).
    applicationQuestionResume: str

    # Whether the job opening application has a standard question for address (true) or not (false) or if entering an address is mandatory (required).
    applicationQuestionAddress: str

    # Whether the job opening application has a standard question for LinkedIn profile url (true) or not (false) or if entering a LinkedIn profile url is mandatory (required).
    applicationQuestionLinkedinUrl: str

    # Whether the job opening application has a standard question for availability date (true) or not (false) or if entering an availability date is mandatory (required).
    applicationQuestionDateAvailable: str

    # Whether the job opening application has a standard question for desired salary (true) or not (false) or if entering a desired salary is mandatory (required).
    applicationQuestionDesiredSalary: str

    # Whether the job opening application has a standard question for cover letter (true) or not (false) or if uploading a cover letter is mandatory (required).
    applicationQuestionCoverLetter: str

    # Whether the job opening application has a standard question for referred by (true) or not (false) or if entering referred by is mandatory (required).
    applicationQuestionReferredBy: str

    # Whether the job opening application has a standard question for website url (true) or not (false) or if entering a website url is mandatory (required).
    applicationQuestionWebsiteUrl: str

    # Whether the job opening application has a standard question for highest education (true) or not (false) or if entering highest education is mandatory (required).
    applicationQuestionHighestEducation: str

    # Whether the job opening application has a standard question for college (true) or not (false) or if entering a college is mandatory (required).
    applicationQuestionCollege: str

    # Whether the job opening application has a standard question for references (true) or not (false) or if entering references is mandatory (required).
    applicationQuestionReferences: str

    # The internal job code for the job opening.
    internalJobCode: str

class ApplicantTrackingCreateNewJobOpeningRequest(RequiredApplicantTrackingCreateNewJobOpeningRequest, OptionalApplicantTrackingCreateNewJobOpeningRequest):
    pass
