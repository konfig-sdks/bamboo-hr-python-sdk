# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from bamboo_hr_python_sdk.paths.company_domain_v1_meta_tables.get import DiscoverTableFieldsRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_meta_fields.get import GetFieldListRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_meta_lists.get import GetListFieldsRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_meta_users.get import GetUserListRaw
from bamboo_hr_python_sdk.paths.company_domain_v1_meta_lists_list_field_id.put import UpdateListFieldValuesRaw


class AccountInformationApiRaw(
    DiscoverTableFieldsRaw,
    GetFieldListRaw,
    GetListFieldsRaw,
    GetUserListRaw,
    UpdateListFieldValuesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
