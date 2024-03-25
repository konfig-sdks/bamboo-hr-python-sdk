import typing_extensions

from bamboo_hr_python_sdk.apis.tags import TagValues
from bamboo_hr_python_sdk.apis.tags.benefits_api import BenefitsApi
from bamboo_hr_python_sdk.apis.tags.goals_api import GoalsApi
from bamboo_hr_python_sdk.apis.tags.time_tracking_api import TimeTrackingApi
from bamboo_hr_python_sdk.apis.tags.time_off_api import TimeOffApi
from bamboo_hr_python_sdk.apis.tags.payroll_api import PayrollApi
from bamboo_hr_python_sdk.apis.tags.training_api import TrainingApi
from bamboo_hr_python_sdk.apis.tags.applicant_tracking_api import ApplicantTrackingApi
from bamboo_hr_python_sdk.apis.tags.time_tracking_private_beta_api import TimeTrackingPrivateBetaApi
from bamboo_hr_python_sdk.apis.tags.tabular_data_api import TabularDataApi
from bamboo_hr_python_sdk.apis.tags.webhooks_api import WebhooksApi
from bamboo_hr_python_sdk.apis.tags.employee_files_api import EmployeeFilesApi
from bamboo_hr_python_sdk.apis.tags.company_files_api import CompanyFilesApi
from bamboo_hr_python_sdk.apis.tags.account_information_api import AccountInformationApi
from bamboo_hr_python_sdk.apis.tags.hours_api import HoursApi
from bamboo_hr_python_sdk.apis.tags.employees_api import EmployeesApi
from bamboo_hr_python_sdk.apis.tags.reports_api import ReportsApi
from bamboo_hr_python_sdk.apis.tags.photos_api import PhotosApi
from bamboo_hr_python_sdk.apis.tags.last_change_information_api import LastChangeInformationApi
from bamboo_hr_python_sdk.apis.tags.login_api import LoginApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BENEFITS: BenefitsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.TIME_TRACKING: TimeTrackingApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.TRAINING: TrainingApi,
        TagValues.APPLICANT_TRACKING: ApplicantTrackingApi,
        TagValues.TIME_TRACKING__PRIVATE_BETA: TimeTrackingPrivateBetaApi,
        TagValues.TABULAR_DATA: TabularDataApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.EMPLOYEE_FILES: EmployeeFilesApi,
        TagValues.COMPANY_FILES: CompanyFilesApi,
        TagValues.ACCOUNT_INFORMATION: AccountInformationApi,
        TagValues.HOURS: HoursApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.PHOTOS: PhotosApi,
        TagValues.LAST_CHANGE_INFORMATION: LastChangeInformationApi,
        TagValues.LOGIN: LoginApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BENEFITS: BenefitsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.TIME_TRACKING: TimeTrackingApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.TRAINING: TrainingApi,
        TagValues.APPLICANT_TRACKING: ApplicantTrackingApi,
        TagValues.TIME_TRACKING__PRIVATE_BETA: TimeTrackingPrivateBetaApi,
        TagValues.TABULAR_DATA: TabularDataApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.EMPLOYEE_FILES: EmployeeFilesApi,
        TagValues.COMPANY_FILES: CompanyFilesApi,
        TagValues.ACCOUNT_INFORMATION: AccountInformationApi,
        TagValues.HOURS: HoursApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.PHOTOS: PhotosApi,
        TagValues.LAST_CHANGE_INFORMATION: LastChangeInformationApi,
        TagValues.LOGIN: LoginApi,
    }
)
