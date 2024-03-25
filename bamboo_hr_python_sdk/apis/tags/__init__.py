# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from bamboo_hr_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BENEFITS = "Benefits"
    GOALS = "Goals"
    TIME_TRACKING = "Time Tracking"
    TIME_OFF = "Time Off"
    PAYROLL = "Payroll"
    TRAINING = "Training"
    APPLICANT_TRACKING = "Applicant Tracking"
    TIME_TRACKING__PRIVATE_BETA = "Time Tracking - Private Beta"
    TABULAR_DATA = "Tabular Data"
    WEBHOOKS = "Webhooks"
    EMPLOYEE_FILES = "Employee Files"
    COMPANY_FILES = "Company Files"
    ACCOUNT_INFORMATION = "Account Information"
    HOURS = "Hours"
    EMPLOYEES = "Employees"
    REPORTS = "Reports"
    PHOTOS = "Photos"
    LAST_CHANGE_INFORMATION = "Last Change Information"
    LOGIN = "Login"
