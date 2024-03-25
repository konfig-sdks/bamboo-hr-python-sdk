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
from bamboo_hr_python_sdk.paths.company_domain_v1_applicant_tracking_statuses import get
from bamboo_hr_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCompanyDomainV1ApplicantTrackingStatuses(ApiTestMixin, unittest.TestCase):
    """
    CompanyDomainV1ApplicantTrackingStatuses unit test stubs
        Get Statuses
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
