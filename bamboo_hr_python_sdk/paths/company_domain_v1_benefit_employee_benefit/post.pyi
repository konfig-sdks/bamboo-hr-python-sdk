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

from bamboo_hr_python_sdk.model.benefits_add_employee_benefit_request import BenefitsAddEmployeeBenefitRequest as BenefitsAddEmployeeBenefitRequestSchema

from bamboo_hr_python_sdk.type.benefits_add_employee_benefit_request import BenefitsAddEmployeeBenefitRequest

from ...api_client import Dictionary
from bamboo_hr_python_sdk.pydantic.benefits_add_employee_benefit_request import BenefitsAddEmployeeBenefitRequest as BenefitsAddEmployeeBenefitRequestPydantic

# Path params
CompanyDomainSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyDomain': typing.Union[CompanyDomainSchema, str, ],
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
# body param
SchemaForRequestBodyApplicationJson = BenefitsAddEmployeeBenefitRequestSchema


request_body_benefits_add_employee_benefit_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
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


class BaseApi(api_client.Api):

    def _add_employee_benefit_mapped_args(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if employee_id is not None:
            _body["employeeId"] = employee_id
        if company_benefit_id is not None:
            _body["companyBenefitId"] = company_benefit_id
        if company_benefit_name is not None:
            _body["companyBenefitName"] = company_benefit_name
        if coverage_level is not None:
            _body["coverageLevel"] = coverage_level
        if deduction_end_date is not None:
            _body["deductionEndDate"] = deduction_end_date
        if deduction_start_date is not None:
            _body["deductionStartDate"] = deduction_start_date
        if enrollment_status is not None:
            _body["enrollmentStatus"] = enrollment_status
        if effective_date is not None:
            _body["effectiveDate"] = effective_date
        if currency_code is not None:
            _body["currencyCode"] = currency_code
        if employee_amount is not None:
            _body["employeeAmount"] = employee_amount
        if employee_amount_type is not None:
            _body["employeeAmountType"] = employee_amount_type
        if employee_percent_based_on is not None:
            _body["employeePercentBasedOn"] = employee_percent_based_on
        if employee_cap_amount is not None:
            _body["employeeCapAmount"] = employee_cap_amount
        if employee_cap_amount_type is not None:
            _body["employeeCapAmountType"] = employee_cap_amount_type
        if employee_annual_max is not None:
            _body["employeeAnnualMax"] = employee_annual_max
        if company_amount is not None:
            _body["companyAmount"] = company_amount
        if company_amount_type is not None:
            _body["companyAmountType"] = company_amount_type
        if company_percent_based_on is not None:
            _body["companyPercentBasedOn"] = company_percent_based_on
        if company_cap_amount is not None:
            _body["companyCapAmount"] = company_cap_amount
        if company_cap_amount_type is not None:
            _body["companyCapAmountType"] = company_cap_amount_type
        if company_annual_max is not None:
            _body["companyAnnualMax"] = company_annual_max
        if benefit_plan_coverage_id is not None:
            _body["benefitPlanCoverageId"] = benefit_plan_coverage_id
        args.body = _body
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        args.path = _path_params
        return args

    async def _aadd_employee_benefit_oapg(
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
        Add an employee benefit
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/v1/benefit/employee_benefit',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_benefits_add_employee_benefit_request.serialize(body, content_type)
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


    def _add_employee_benefit_oapg(
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
        Add an employee benefit
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/v1/benefit/employee_benefit',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_benefits_add_employee_benefit_request.serialize(body, content_type)
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


class AddEmployeeBenefitRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_employee_benefit(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_employee_benefit_mapped_args(
            body=body,
            company_domain=company_domain,
            employee_id=employee_id,
            company_benefit_id=company_benefit_id,
            company_benefit_name=company_benefit_name,
            coverage_level=coverage_level,
            deduction_end_date=deduction_end_date,
            deduction_start_date=deduction_start_date,
            enrollment_status=enrollment_status,
            effective_date=effective_date,
            currency_code=currency_code,
            employee_amount=employee_amount,
            employee_amount_type=employee_amount_type,
            employee_percent_based_on=employee_percent_based_on,
            employee_cap_amount=employee_cap_amount,
            employee_cap_amount_type=employee_cap_amount_type,
            employee_annual_max=employee_annual_max,
            company_amount=company_amount,
            company_amount_type=company_amount_type,
            company_percent_based_on=company_percent_based_on,
            company_cap_amount=company_cap_amount,
            company_cap_amount_type=company_cap_amount_type,
            company_annual_max=company_annual_max,
            benefit_plan_coverage_id=benefit_plan_coverage_id,
        )
        return await self._aadd_employee_benefit_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_employee_benefit(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_employee_benefit_mapped_args(
            body=body,
            company_domain=company_domain,
            employee_id=employee_id,
            company_benefit_id=company_benefit_id,
            company_benefit_name=company_benefit_name,
            coverage_level=coverage_level,
            deduction_end_date=deduction_end_date,
            deduction_start_date=deduction_start_date,
            enrollment_status=enrollment_status,
            effective_date=effective_date,
            currency_code=currency_code,
            employee_amount=employee_amount,
            employee_amount_type=employee_amount_type,
            employee_percent_based_on=employee_percent_based_on,
            employee_cap_amount=employee_cap_amount,
            employee_cap_amount_type=employee_cap_amount_type,
            employee_annual_max=employee_annual_max,
            company_amount=company_amount,
            company_amount_type=company_amount_type,
            company_percent_based_on=company_percent_based_on,
            company_cap_amount=company_cap_amount,
            company_cap_amount_type=company_cap_amount_type,
            company_annual_max=company_annual_max,
            benefit_plan_coverage_id=benefit_plan_coverage_id,
        )
        return self._add_employee_benefit_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddEmployeeBenefit(BaseApi):

    async def aadd_employee_benefit(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aadd_employee_benefit(
            body=body,
            company_domain=company_domain,
            employee_id=employee_id,
            company_benefit_id=company_benefit_id,
            company_benefit_name=company_benefit_name,
            coverage_level=coverage_level,
            deduction_end_date=deduction_end_date,
            deduction_start_date=deduction_start_date,
            enrollment_status=enrollment_status,
            effective_date=effective_date,
            currency_code=currency_code,
            employee_amount=employee_amount,
            employee_amount_type=employee_amount_type,
            employee_percent_based_on=employee_percent_based_on,
            employee_cap_amount=employee_cap_amount,
            employee_cap_amount_type=employee_cap_amount_type,
            employee_annual_max=employee_annual_max,
            company_amount=company_amount,
            company_amount_type=company_amount_type,
            company_percent_based_on=company_percent_based_on,
            company_cap_amount=company_cap_amount,
            company_cap_amount_type=company_cap_amount_type,
            company_annual_max=company_annual_max,
            benefit_plan_coverage_id=benefit_plan_coverage_id,
            **kwargs,
        )
    
    
    def add_employee_benefit(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.add_employee_benefit(
            body=body,
            company_domain=company_domain,
            employee_id=employee_id,
            company_benefit_id=company_benefit_id,
            company_benefit_name=company_benefit_name,
            coverage_level=coverage_level,
            deduction_end_date=deduction_end_date,
            deduction_start_date=deduction_start_date,
            enrollment_status=enrollment_status,
            effective_date=effective_date,
            currency_code=currency_code,
            employee_amount=employee_amount,
            employee_amount_type=employee_amount_type,
            employee_percent_based_on=employee_percent_based_on,
            employee_cap_amount=employee_cap_amount,
            employee_cap_amount_type=employee_cap_amount_type,
            employee_annual_max=employee_annual_max,
            company_amount=company_amount,
            company_amount_type=company_amount_type,
            company_percent_based_on=company_percent_based_on,
            company_cap_amount=company_cap_amount,
            company_cap_amount_type=company_cap_amount_type,
            company_annual_max=company_annual_max,
            benefit_plan_coverage_id=benefit_plan_coverage_id,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_employee_benefit_mapped_args(
            body=body,
            company_domain=company_domain,
            employee_id=employee_id,
            company_benefit_id=company_benefit_id,
            company_benefit_name=company_benefit_name,
            coverage_level=coverage_level,
            deduction_end_date=deduction_end_date,
            deduction_start_date=deduction_start_date,
            enrollment_status=enrollment_status,
            effective_date=effective_date,
            currency_code=currency_code,
            employee_amount=employee_amount,
            employee_amount_type=employee_amount_type,
            employee_percent_based_on=employee_percent_based_on,
            employee_cap_amount=employee_cap_amount,
            employee_cap_amount_type=employee_cap_amount_type,
            employee_annual_max=employee_annual_max,
            company_amount=company_amount,
            company_amount_type=company_amount_type,
            company_percent_based_on=company_percent_based_on,
            company_cap_amount=company_cap_amount,
            company_cap_amount_type=company_cap_amount_type,
            company_annual_max=company_annual_max,
            benefit_plan_coverage_id=benefit_plan_coverage_id,
        )
        return await self._aadd_employee_benefit_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        company_domain: str,
        employee_id: typing.Optional[int] = None,
        company_benefit_id: typing.Optional[int] = None,
        company_benefit_name: typing.Optional[str] = None,
        coverage_level: typing.Optional[str] = None,
        deduction_end_date: typing.Optional[date] = None,
        deduction_start_date: typing.Optional[date] = None,
        enrollment_status: typing.Optional[str] = None,
        effective_date: typing.Optional[date] = None,
        currency_code: typing.Optional[str] = None,
        employee_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_amount_type: typing.Optional[str] = None,
        employee_percent_based_on: typing.Optional[str] = None,
        employee_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        employee_cap_amount_type: typing.Optional[str] = None,
        employee_annual_max: typing.Optional[typing.Union[int, float]] = None,
        company_amount: typing.Optional[typing.Union[int, float]] = None,
        company_amount_type: typing.Optional[str] = None,
        company_percent_based_on: typing.Optional[str] = None,
        company_cap_amount: typing.Optional[typing.Union[int, float]] = None,
        company_cap_amount_type: typing.Optional[str] = None,
        company_annual_max: typing.Optional[typing.Union[int, float]] = None,
        benefit_plan_coverage_id: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_employee_benefit_mapped_args(
            body=body,
            company_domain=company_domain,
            employee_id=employee_id,
            company_benefit_id=company_benefit_id,
            company_benefit_name=company_benefit_name,
            coverage_level=coverage_level,
            deduction_end_date=deduction_end_date,
            deduction_start_date=deduction_start_date,
            enrollment_status=enrollment_status,
            effective_date=effective_date,
            currency_code=currency_code,
            employee_amount=employee_amount,
            employee_amount_type=employee_amount_type,
            employee_percent_based_on=employee_percent_based_on,
            employee_cap_amount=employee_cap_amount,
            employee_cap_amount_type=employee_cap_amount_type,
            employee_annual_max=employee_annual_max,
            company_amount=company_amount,
            company_amount_type=company_amount_type,
            company_percent_based_on=company_percent_based_on,
            company_cap_amount=company_cap_amount,
            company_cap_amount_type=company_cap_amount_type,
            company_annual_max=company_annual_max,
            benefit_plan_coverage_id=benefit_plan_coverage_id,
        )
        return self._add_employee_benefit_oapg(
            body=args.body,
            path_params=args.path,
        )

