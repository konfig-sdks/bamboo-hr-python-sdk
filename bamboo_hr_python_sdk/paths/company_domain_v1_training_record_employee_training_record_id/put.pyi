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

from bamboo_hr_python_sdk.model.training_update_employee_training_record_request import TrainingUpdateEmployeeTrainingRecordRequest as TrainingUpdateEmployeeTrainingRecordRequestSchema
from bamboo_hr_python_sdk.model.training_record import TrainingRecord as TrainingRecordSchema

from bamboo_hr_python_sdk.type.training_record import TrainingRecord
from bamboo_hr_python_sdk.type.training_update_employee_training_record_request import TrainingUpdateEmployeeTrainingRecordRequest

from ...api_client import Dictionary
from bamboo_hr_python_sdk.pydantic.training_record import TrainingRecord as TrainingRecordPydantic
from bamboo_hr_python_sdk.pydantic.training_update_employee_training_record_request import TrainingUpdateEmployeeTrainingRecordRequest as TrainingUpdateEmployeeTrainingRecordRequestPydantic

# Path params
CompanyDomainSchema = schemas.StrSchema
EmployeeTrainingRecordIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyDomain': typing.Union[CompanyDomainSchema, str, ],
        'employeeTrainingRecordId': typing.Union[EmployeeTrainingRecordIdSchema, decimal.Decimal, int, ],
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
request_path_employee_training_record_id = api_client.PathParameter(
    name="employeeTrainingRecordId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeTrainingRecordIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TrainingUpdateEmployeeTrainingRecordRequestSchema


request_body_training_update_employee_training_record_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = TrainingRecordSchema
SchemaFor200ResponseBodyApplicationXml = TrainingRecordSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TrainingRecord


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TrainingRecord


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
    },
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
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
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
_all_accept_content_types = (
    'application/json',
    'application/xml',
)


class BaseApi(api_client.Api):

    def _update_employee_training_record_mapped_args(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if completed is not None:
            _body["completed"] = completed
        if cost is not None:
            _body["cost"] = cost
        if instructor is not None:
            _body["instructor"] = instructor
        if hours is not None:
            _body["hours"] = hours
        if credits is not None:
            _body["credits"] = credits
        if notes is not None:
            _body["notes"] = notes
        args.body = _body
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        if employee_training_record_id is not None:
            _path_params["employeeTrainingRecordId"] = employee_training_record_id
        args.path = _path_params
        return args

    async def _aupdate_employee_training_record_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Employee Training Record
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_employee_training_record_id,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
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
            path_template='/{companyDomain}/v1/training/record/{employeeTrainingRecordId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_training_update_employee_training_record_request.serialize(body, content_type)
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


    def _update_employee_training_record_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Employee Training Record
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_employee_training_record_id,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
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
            path_template='/{companyDomain}/v1/training/record/{employeeTrainingRecordId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_training_update_employee_training_record_request.serialize(body, content_type)
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


class UpdateEmployeeTrainingRecordRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_employee_training_record(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_employee_training_record_mapped_args(
            completed=completed,
            company_domain=company_domain,
            employee_training_record_id=employee_training_record_id,
            cost=cost,
            instructor=instructor,
            hours=hours,
            credits=credits,
            notes=notes,
        )
        return await self._aupdate_employee_training_record_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_employee_training_record(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_employee_training_record_mapped_args(
            completed=completed,
            company_domain=company_domain,
            employee_training_record_id=employee_training_record_id,
            cost=cost,
            instructor=instructor,
            hours=hours,
            credits=credits,
            notes=notes,
        )
        return self._update_employee_training_record_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateEmployeeTrainingRecord(BaseApi):

    async def aupdate_employee_training_record(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> TrainingRecordPydantic:
        raw_response = await self.raw.aupdate_employee_training_record(
            completed=completed,
            company_domain=company_domain,
            employee_training_record_id=employee_training_record_id,
            cost=cost,
            instructor=instructor,
            hours=hours,
            credits=credits,
            notes=notes,
            **kwargs,
        )
        if validate:
            return TrainingRecordPydantic(**raw_response.body)
        return api_client.construct_model_instance(TrainingRecordPydantic, raw_response.body)
    
    
    def update_employee_training_record(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> TrainingRecordPydantic:
        raw_response = self.raw.update_employee_training_record(
            completed=completed,
            company_domain=company_domain,
            employee_training_record_id=employee_training_record_id,
            cost=cost,
            instructor=instructor,
            hours=hours,
            credits=credits,
            notes=notes,
        )
        if validate:
            return TrainingRecordPydantic(**raw_response.body)
        return api_client.construct_model_instance(TrainingRecordPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_employee_training_record_mapped_args(
            completed=completed,
            company_domain=company_domain,
            employee_training_record_id=employee_training_record_id,
            cost=cost,
            instructor=instructor,
            hours=hours,
            credits=credits,
            notes=notes,
        )
        return await self._aupdate_employee_training_record_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        completed: str,
        company_domain: str,
        employee_training_record_id: int,
        cost: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        instructor: typing.Optional[str] = None,
        hours: typing.Optional[typing.Union[int, float]] = None,
        credits: typing.Optional[typing.Union[int, float]] = None,
        notes: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_employee_training_record_mapped_args(
            completed=completed,
            company_domain=company_domain,
            employee_training_record_id=employee_training_record_id,
            cost=cost,
            instructor=instructor,
            hours=hours,
            credits=credits,
            notes=notes,
        )
        return self._update_employee_training_record_oapg(
            body=args.body,
            path_params=args.path,
        )

