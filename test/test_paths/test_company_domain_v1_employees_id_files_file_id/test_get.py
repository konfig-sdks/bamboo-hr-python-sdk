# coding: utf-8

"""
    BambooHR API

    This is the majority of the API requests including some that are not documented.  http://www.bamboohr.com/api/documentation/

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import bamboo_hr_python_sdk
from bamboo_hr_python_sdk.paths.company_domain_v1_employees_id_files_file_id import get
from bamboo_hr_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCompanyDomainV1EmployeesIdFilesFileId(ApiTestMixin, unittest.TestCase):
    """
    CompanyDomainV1EmployeesIdFilesFileId unit test stubs
        Get an Employee File
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
