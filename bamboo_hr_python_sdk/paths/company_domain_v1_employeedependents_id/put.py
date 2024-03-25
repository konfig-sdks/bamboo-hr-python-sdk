# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from bamboo_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from bamboo_hr_python_sdk.api_response import AsyncGeneratorResponse
from bamboo_hr_python_sdk import api_client, exceptions
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

from bamboo_hr_python_sdk.model.employee_dependent import EmployeeDependent as EmployeeDependentSchema

from bamboo_hr_python_sdk.type.employee_dependent import EmployeeDependent

from ...api_client import Dictionary
from bamboo_hr_python_sdk.pydantic.employee_dependent import EmployeeDependent as EmployeeDependentPydantic

from . import path

# Path params
CompanyDomainSchema = schemas.StrSchema
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyDomain': typing.Union[CompanyDomainSchema, str, ],
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_domain = api_client.PathParameter(
    name="companyDomain",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyDomainSchema,
    required=True,
)
request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EmployeeDependentSchema


request_body_employee_dependent = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'auth',
    'basic',
]


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '403': _response_for_403,
    '500': _response_for_500,
}


class BaseApi(api_client.Api):

    def _update_dependent_information_mapped_args(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if employee_id is not None:
            _body["employeeId"] = employee_id
        if first_name is not None:
            _body["firstName"] = first_name
        if middle_name is not None:
            _body["middleName"] = middle_name
        if last_name is not None:
            _body["lastName"] = last_name
        if relationship is not None:
            _body["relationship"] = relationship
        if gender is not None:
            _body["gender"] = gender
        if ssn is not None:
            _body["ssn"] = ssn
        if date_of_birth is not None:
            _body["dateOfBirth"] = date_of_birth
        if address_line1 is not None:
            _body["addressLine1"] = address_line1
        if address_line2 is not None:
            _body["addressLine2"] = address_line2
        if city is not None:
            _body["city"] = city
        if state is not None:
            _body["state"] = state
        if zip_code is not None:
            _body["zipCode"] = zip_code
        if home_phone is not None:
            _body["homePhone"] = home_phone
        if country is not None:
            _body["country"] = country
        if is_us_citizen is not None:
            _body["isUsCitizen"] = is_us_citizen
        if is_student is not None:
            _body["isStudent"] = is_student
        args.body = _body
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aupdate_dependent_information_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update an employee dependent
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/v1/employeedependents/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_employee_dependent.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_dependent_information_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update an employee dependent
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/v1/employeedependents/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_employee_dependent.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateDependentInformationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_dependent_information(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_dependent_information_mapped_args(
            company_domain=company_domain,
            id=id,
            employee_id=employee_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relationship=relationship,
            gender=gender,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_code=zip_code,
            home_phone=home_phone,
            country=country,
            is_us_citizen=is_us_citizen,
            is_student=is_student,
        )
        return await self._aupdate_dependent_information_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_dependent_information(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_dependent_information_mapped_args(
            company_domain=company_domain,
            id=id,
            employee_id=employee_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relationship=relationship,
            gender=gender,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_code=zip_code,
            home_phone=home_phone,
            country=country,
            is_us_citizen=is_us_citizen,
            is_student=is_student,
        )
        return self._update_dependent_information_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateDependentInformation(BaseApi):

    async def aupdate_dependent_information(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_dependent_information(
            company_domain=company_domain,
            id=id,
            employee_id=employee_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relationship=relationship,
            gender=gender,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_code=zip_code,
            home_phone=home_phone,
            country=country,
            is_us_citizen=is_us_citizen,
            is_student=is_student,
            **kwargs,
        )
    
    
    def update_dependent_information(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_dependent_information(
            company_domain=company_domain,
            id=id,
            employee_id=employee_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relationship=relationship,
            gender=gender,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_code=zip_code,
            home_phone=home_phone,
            country=country,
            is_us_citizen=is_us_citizen,
            is_student=is_student,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_dependent_information_mapped_args(
            company_domain=company_domain,
            id=id,
            employee_id=employee_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relationship=relationship,
            gender=gender,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_code=zip_code,
            home_phone=home_phone,
            country=country,
            is_us_citizen=is_us_citizen,
            is_student=is_student,
        )
        return await self._aupdate_dependent_information_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        company_domain: str,
        id: str,
        employee_id: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        relationship: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        date_of_birth: typing.Optional[str] = None,
        address_line1: typing.Optional[str] = None,
        address_line2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        home_phone: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        is_us_citizen: typing.Optional[str] = None,
        is_student: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_dependent_information_mapped_args(
            company_domain=company_domain,
            id=id,
            employee_id=employee_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relationship=relationship,
            gender=gender,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_code=zip_code,
            home_phone=home_phone,
            country=country,
            is_us_citizen=is_us_citizen,
            is_student=is_student,
        )
        return self._update_dependent_information_oapg(
            body=args.body,
            path_params=args.path,
        )

