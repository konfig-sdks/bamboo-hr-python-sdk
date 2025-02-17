# coding: utf-8
"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from bamboo_hr_python_sdk.client_custom import ClientCustom
from bamboo_hr_python_sdk.configuration import Configuration
from bamboo_hr_python_sdk.api_client import ApiClient
from bamboo_hr_python_sdk.type_util import copy_signature
from bamboo_hr_python_sdk.apis.tags.account_information_api import AccountInformationApi
from bamboo_hr_python_sdk.apis.tags.applicant_tracking_api import ApplicantTrackingApi
from bamboo_hr_python_sdk.apis.tags.benefits_api import BenefitsApi
from bamboo_hr_python_sdk.apis.tags.company_files_api import CompanyFilesApi
from bamboo_hr_python_sdk.apis.tags.employee_files_api import EmployeeFilesApi
from bamboo_hr_python_sdk.apis.tags.employees_api import EmployeesApi
from bamboo_hr_python_sdk.apis.tags.goals_api import GoalsApi
from bamboo_hr_python_sdk.apis.tags.hours_api import HoursApi
from bamboo_hr_python_sdk.apis.tags.last_change_information_api import LastChangeInformationApi
from bamboo_hr_python_sdk.apis.tags.login_api import LoginApi
from bamboo_hr_python_sdk.apis.tags.payroll_api import PayrollApi
from bamboo_hr_python_sdk.apis.tags.photos_api import PhotosApi
from bamboo_hr_python_sdk.apis.tags.reports_api import ReportsApi
from bamboo_hr_python_sdk.apis.tags.tabular_data_api import TabularDataApi
from bamboo_hr_python_sdk.apis.tags.time_off_api import TimeOffApi
from bamboo_hr_python_sdk.apis.tags.time_tracking_api import TimeTrackingApi
from bamboo_hr_python_sdk.apis.tags.time_tracking_private_beta_api import TimeTrackingPrivateBetaApi
from bamboo_hr_python_sdk.apis.tags.training_api import TrainingApi
from bamboo_hr_python_sdk.apis.tags.webhooks_api import WebhooksApi



class BambooHr(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.account_information: AccountInformationApi = AccountInformationApi(api_client)
        self.applicant_tracking: ApplicantTrackingApi = ApplicantTrackingApi(api_client)
        self.benefits: BenefitsApi = BenefitsApi(api_client)
        self.company_files: CompanyFilesApi = CompanyFilesApi(api_client)
        self.employee_files: EmployeeFilesApi = EmployeeFilesApi(api_client)
        self.employees: EmployeesApi = EmployeesApi(api_client)
        self.goals: GoalsApi = GoalsApi(api_client)
        self.hours: HoursApi = HoursApi(api_client)
        self.last_change_information: LastChangeInformationApi = LastChangeInformationApi(api_client)
        self.login: LoginApi = LoginApi(api_client)
        self.payroll: PayrollApi = PayrollApi(api_client)
        self.photos: PhotosApi = PhotosApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.tabular_data: TabularDataApi = TabularDataApi(api_client)
        self.time_off: TimeOffApi = TimeOffApi(api_client)
        self.time_tracking: TimeTrackingApi = TimeTrackingApi(api_client)
        self.time_tracking___private_beta: TimeTrackingPrivateBetaApi = TimeTrackingPrivateBetaApi(api_client)
        self.training: TrainingApi = TrainingApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)
