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

from bamboo_hr_python_sdk.model.webhook404_error import Webhook404Error as Webhook404ErrorSchema
from bamboo_hr_python_sdk.model.new_web_hook import NewWebHook as NewWebHookSchema
from bamboo_hr_python_sdk.model.new_web_hook_monitor_fields import NewWebHookMonitorFields as NewWebHookMonitorFieldsSchema
from bamboo_hr_python_sdk.model.webhook500_error import Webhook500Error as Webhook500ErrorSchema
from bamboo_hr_python_sdk.model.webhooks_update_webhook_by_id_response import WebhooksUpdateWebhookByIdResponse as WebhooksUpdateWebhookByIdResponseSchema
from bamboo_hr_python_sdk.model.new_web_hook_limit import NewWebHookLimit as NewWebHookLimitSchema
from bamboo_hr_python_sdk.model.new_web_hook_frequency import NewWebHookFrequency as NewWebHookFrequencySchema
from bamboo_hr_python_sdk.model.webhook400_error import Webhook400Error as Webhook400ErrorSchema
from bamboo_hr_python_sdk.model.new_web_hook_post_fields import NewWebHookPostFields as NewWebHookPostFieldsSchema
from bamboo_hr_python_sdk.model.web_hook_response import WebHookResponse as WebHookResponseSchema

from bamboo_hr_python_sdk.type.new_web_hook_limit import NewWebHookLimit
from bamboo_hr_python_sdk.type.new_web_hook_post_fields import NewWebHookPostFields
from bamboo_hr_python_sdk.type.new_web_hook import NewWebHook
from bamboo_hr_python_sdk.type.webhook400_error import Webhook400Error
from bamboo_hr_python_sdk.type.web_hook_response import WebHookResponse
from bamboo_hr_python_sdk.type.new_web_hook_frequency import NewWebHookFrequency
from bamboo_hr_python_sdk.type.webhooks_update_webhook_by_id_response import WebhooksUpdateWebhookByIdResponse
from bamboo_hr_python_sdk.type.new_web_hook_monitor_fields import NewWebHookMonitorFields
from bamboo_hr_python_sdk.type.webhook500_error import Webhook500Error
from bamboo_hr_python_sdk.type.webhook404_error import Webhook404Error

from ...api_client import Dictionary
from bamboo_hr_python_sdk.pydantic.new_web_hook import NewWebHook as NewWebHookPydantic
from bamboo_hr_python_sdk.pydantic.new_web_hook_frequency import NewWebHookFrequency as NewWebHookFrequencyPydantic
from bamboo_hr_python_sdk.pydantic.new_web_hook_monitor_fields import NewWebHookMonitorFields as NewWebHookMonitorFieldsPydantic
from bamboo_hr_python_sdk.pydantic.web_hook_response import WebHookResponse as WebHookResponsePydantic
from bamboo_hr_python_sdk.pydantic.webhook404_error import Webhook404Error as Webhook404ErrorPydantic
from bamboo_hr_python_sdk.pydantic.new_web_hook_post_fields import NewWebHookPostFields as NewWebHookPostFieldsPydantic
from bamboo_hr_python_sdk.pydantic.webhook500_error import Webhook500Error as Webhook500ErrorPydantic
from bamboo_hr_python_sdk.pydantic.new_web_hook_limit import NewWebHookLimit as NewWebHookLimitPydantic
from bamboo_hr_python_sdk.pydantic.webhook400_error import Webhook400Error as Webhook400ErrorPydantic
from bamboo_hr_python_sdk.pydantic.webhooks_update_webhook_by_id_response import WebhooksUpdateWebhookByIdResponse as WebhooksUpdateWebhookByIdResponsePydantic

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
SchemaForRequestBodyApplicationJson = NewWebHookSchema


request_body_new_web_hook = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = WebHookResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WebHookResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WebHookResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = Webhook400ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Webhook400Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Webhook400Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
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
SchemaFor403ResponseBodyApplicationJson = WebhooksUpdateWebhookByIdResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: WebhooksUpdateWebhookByIdResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: WebhooksUpdateWebhookByIdResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = Webhook404ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Webhook404Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Webhook404Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = Webhook500ErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: Webhook500Error


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: Webhook500Error


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_webhook_by_id_mapped_args(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if monitor_fields is not None:
            _body["monitorFields"] = monitor_fields
        if post_fields is not None:
            _body["postFields"] = post_fields
        if url is not None:
            _body["url"] = url
        if format is not None:
            _body["format"] = format
        if frequency is not None:
            _body["frequency"] = frequency
        if limit is not None:
            _body["limit"] = limit
        if include_company_domain is not None:
            _body["includeCompanyDomain"] = include_company_domain
        args.body = _body
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aupdate_webhook_by_id_oapg(
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
        Update Webhook
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
            path_template='/{companyDomain}/v1/webhooks/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_new_web_hook.serialize(body, content_type)
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


    def _update_webhook_by_id_oapg(
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
        Update Webhook
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
            path_template='/{companyDomain}/v1/webhooks/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_new_web_hook.serialize(body, content_type)
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


class UpdateWebhookByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_webhook_by_id(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_webhook_by_id_mapped_args(
            name=name,
            monitor_fields=monitor_fields,
            post_fields=post_fields,
            url=url,
            company_domain=company_domain,
            id=id,
            format=format,
            frequency=frequency,
            limit=limit,
            include_company_domain=include_company_domain,
        )
        return await self._aupdate_webhook_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_webhook_by_id(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_webhook_by_id_mapped_args(
            name=name,
            monitor_fields=monitor_fields,
            post_fields=post_fields,
            url=url,
            company_domain=company_domain,
            id=id,
            format=format,
            frequency=frequency,
            limit=limit,
            include_company_domain=include_company_domain,
        )
        return self._update_webhook_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateWebhookById(BaseApi):

    async def aupdate_webhook_by_id(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> WebHookResponsePydantic:
        raw_response = await self.raw.aupdate_webhook_by_id(
            name=name,
            monitor_fields=monitor_fields,
            post_fields=post_fields,
            url=url,
            company_domain=company_domain,
            id=id,
            format=format,
            frequency=frequency,
            limit=limit,
            include_company_domain=include_company_domain,
            **kwargs,
        )
        if validate:
            return WebHookResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WebHookResponsePydantic, raw_response.body)
    
    
    def update_webhook_by_id(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> WebHookResponsePydantic:
        raw_response = self.raw.update_webhook_by_id(
            name=name,
            monitor_fields=monitor_fields,
            post_fields=post_fields,
            url=url,
            company_domain=company_domain,
            id=id,
            format=format,
            frequency=frequency,
            limit=limit,
            include_company_domain=include_company_domain,
        )
        if validate:
            return WebHookResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WebHookResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_webhook_by_id_mapped_args(
            name=name,
            monitor_fields=monitor_fields,
            post_fields=post_fields,
            url=url,
            company_domain=company_domain,
            id=id,
            format=format,
            frequency=frequency,
            limit=limit,
            include_company_domain=include_company_domain,
        )
        return await self._aupdate_webhook_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        name: str,
        monitor_fields: NewWebHookMonitorFields,
        post_fields: NewWebHookPostFields,
        url: str,
        company_domain: str,
        id: str,
        format: typing.Optional[str] = None,
        frequency: typing.Optional[NewWebHookFrequency] = None,
        limit: typing.Optional[NewWebHookLimit] = None,
        include_company_domain: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_webhook_by_id_mapped_args(
            name=name,
            monitor_fields=monitor_fields,
            post_fields=post_fields,
            url=url,
            company_domain=company_domain,
            id=id,
            format=format,
            frequency=frequency,
            limit=limit,
            include_company_domain=include_company_domain,
        )
        return self._update_webhook_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

