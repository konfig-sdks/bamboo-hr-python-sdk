# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from bamboo_hr_python_sdk.paths.company_domain_v1_timetracking_record.post import BulkRecordEditRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_timetracking_delete_id.delete import DeleteHourRecordRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_timetracking_adjust.put import EditHourRecordRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_timetracking_record_id.get import GetHourRecordRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_timetracking_add.post import RecordAdditionRaw


class HoursApiRaw(
    BulkRecordEditRaw,
    DeleteHourRecordRaw,
    EditHourRecordRaw,
    GetHourRecordRaw,
    RecordAdditionRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
