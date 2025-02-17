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

from bamboo_hr_python_sdk.model.time_tracking_clock_out_employee_request import TimeTrackingClockOutEmployeeRequest as TimeTrackingClockOutEmployeeRequestSchema
from bamboo_hr_python_sdk.model.time_tracking_clock_out_employee_request_clock_out_location import TimeTrackingClockOutEmployeeRequestClockOutLocation as TimeTrackingClockOutEmployeeRequestClockOutLocationSchema

from bamboo_hr_python_sdk.type.time_tracking_clock_out_employee_request import TimeTrackingClockOutEmployeeRequest
from bamboo_hr_python_sdk.type.time_tracking_clock_out_employee_request_clock_out_location import TimeTrackingClockOutEmployeeRequestClockOutLocation

from ...api_client import Dictionary
from bamboo_hr_python_sdk.pydantic.time_tracking_clock_out_employee_request_clock_out_location import TimeTrackingClockOutEmployeeRequestClockOutLocation as TimeTrackingClockOutEmployeeRequestClockOutLocationPydantic
from bamboo_hr_python_sdk.pydantic.time_tracking_clock_out_employee_request import TimeTrackingClockOutEmployeeRequest as TimeTrackingClockOutEmployeeRequestPydantic

# Path params
CompanyDomainSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyDomain': typing.Union[CompanyDomainSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
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
request_path_employee_id = api_client.PathParameter(
    name="employeeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TimeTrackingClockOutEmployeeRequestSchema


request_body_time_tracking_clock_out_employee_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
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
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
)


@dataclass
class ApiResponseFor412(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor412Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_412 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor412,
    response_cls_async=ApiResponseFor412Async,
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


class BaseApi(api_client.Api):

    def _clock_out_employee_mapped_args(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if clock_out_location is not None:
            _body["clockOutLocation"] = clock_out_location
        args.body = _body
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        if employee_id is not None:
            _path_params["employeeId"] = employee_id
        args.path = _path_params
        return args

    async def _aclock_out_employee_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Clock out (employee id optional)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_employee_id,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/v1/time_tracking/clock_out/{employeeId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_time_tracking_clock_out_employee_request.serialize(body, content_type)
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


    def _clock_out_employee_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Clock out (employee id optional)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_employee_id,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/v1/time_tracking/clock_out/{employeeId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_time_tracking_clock_out_employee_request.serialize(body, content_type)
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


class ClockOutEmployeeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aclock_out_employee(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._clock_out_employee_mapped_args(
            company_domain=company_domain,
            employee_id=employee_id,
            clock_out_location=clock_out_location,
        )
        return await self._aclock_out_employee_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def clock_out_employee(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._clock_out_employee_mapped_args(
            company_domain=company_domain,
            employee_id=employee_id,
            clock_out_location=clock_out_location,
        )
        return self._clock_out_employee_oapg(
            body=args.body,
            path_params=args.path,
        )

class ClockOutEmployee(BaseApi):

    async def aclock_out_employee(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aclock_out_employee(
            company_domain=company_domain,
            employee_id=employee_id,
            clock_out_location=clock_out_location,
            **kwargs,
        )
    
    
    def clock_out_employee(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.clock_out_employee(
            company_domain=company_domain,
            employee_id=employee_id,
            clock_out_location=clock_out_location,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._clock_out_employee_mapped_args(
            company_domain=company_domain,
            employee_id=employee_id,
            clock_out_location=clock_out_location,
        )
        return await self._aclock_out_employee_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        company_domain: str,
        employee_id: str,
        clock_out_location: typing.Optional[TimeTrackingClockOutEmployeeRequestClockOutLocation] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._clock_out_employee_mapped_args(
            company_domain=company_domain,
            employee_id=employee_id,
            clock_out_location=clock_out_location,
        )
        return self._clock_out_employee_oapg(
            body=args.body,
            path_params=args.path,
        )

