<div align="left">

[![Visit Bamboohr](./header.png)](https://bamboohr.com)

# Bamboohr<a id="bamboohr"></a>

This is the majority of the API requests including some that are not documented.

http://www.bamboohr.com/api/documentation/


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`bamboohr.account_information.discover_table_fields`](#bamboohraccount_informationdiscover_table_fields)
  * [`bamboohr.account_information.get_field_list`](#bamboohraccount_informationget_field_list)
  * [`bamboohr.account_information.get_list_fields`](#bamboohraccount_informationget_list_fields)
  * [`bamboohr.account_information.get_user_list`](#bamboohraccount_informationget_user_list)
  * [`bamboohr.account_information.update_list_field_values`](#bamboohraccount_informationupdate_list_field_values)
  * [`bamboohr.applicant_tracking.add_application_comment`](#bamboohrapplicant_trackingadd_application_comment)
  * [`bamboohr.applicant_tracking.change_applicant_status`](#bamboohrapplicant_trackingchange_applicant_status)
  * [`bamboohr.applicant_tracking.create_new_application`](#bamboohrapplicant_trackingcreate_new_application)
  * [`bamboohr.applicant_tracking.create_new_job_opening`](#bamboohrapplicant_trackingcreate_new_job_opening)
  * [`bamboohr.applicant_tracking.get_application_details`](#bamboohrapplicant_trackingget_application_details)
  * [`bamboohr.applicant_tracking.get_company_locations`](#bamboohrapplicant_trackingget_company_locations)
  * [`bamboohr.applicant_tracking.get_hiring_leads`](#bamboohrapplicant_trackingget_hiring_leads)
  * [`bamboohr.applicant_tracking.get_job_summaries`](#bamboohrapplicant_trackingget_job_summaries)
  * [`bamboohr.applicant_tracking.list_applications`](#bamboohrapplicant_trackinglist_applications)
  * [`bamboohr.applicant_tracking.list_statuses`](#bamboohrapplicant_trackinglist_statuses)
  * [`bamboohr.benefits.add_benefit_group_employee`](#bamboohrbenefitsadd_benefit_group_employee)
  * [`bamboohr.benefits.add_employee_benefit`](#bamboohrbenefitsadd_employee_benefit)
  * [`bamboohr.benefits.add_new_company_benefit`](#bamboohrbenefitsadd_new_company_benefit)
  * [`bamboohr.benefits.create_employee_dependent`](#bamboohrbenefitscreate_employee_dependent)
  * [`bamboohr.benefits.delete_company_benefit`](#bamboohrbenefitsdelete_company_benefit)
  * [`bamboohr.benefits.get_benefit_group_employees`](#bamboohrbenefitsget_benefit_group_employees)
  * [`bamboohr.benefits.get_benefit_groups`](#bamboohrbenefitsget_benefit_groups)
  * [`bamboohr.benefits.get_benefit_plan_deductions_by_employee`](#bamboohrbenefitsget_benefit_plan_deductions_by_employee)
  * [`bamboohr.benefits.get_benefit_plans`](#bamboohrbenefitsget_benefit_plans)
  * [`bamboohr.benefits.get_company_benefit`](#bamboohrbenefitsget_company_benefit)
  * [`bamboohr.benefits.get_coverages`](#bamboohrbenefitsget_coverages)
  * [`bamboohr.benefits.get_deduction_types_all`](#bamboohrbenefitsget_deduction_types_all)
  * [`bamboohr.benefits.get_deductions_by_plan`](#bamboohrbenefitsget_deductions_by_plan)
  * [`bamboohr.benefits.get_employee_benefit_deductions`](#bamboohrbenefitsget_employee_benefit_deductions)
  * [`bamboohr.benefits.get_employee_dependent`](#bamboohrbenefitsget_employee_dependent)
  * [`bamboohr.benefits.get_group_plan_costs`](#bamboohrbenefitsget_group_plan_costs)
  * [`bamboohr.benefits.get_group_plans`](#bamboohrbenefitsget_group_plans)
  * [`bamboohr.benefits.list_benefit_plan_coverages`](#bamboohrbenefitslist_benefit_plan_coverages)
  * [`bamboohr.benefits.list_company_benefit_types`](#bamboohrbenefitslist_company_benefit_types)
  * [`bamboohr.benefits.list_company_benefits`](#bamboohrbenefitslist_company_benefits)
  * [`bamboohr.benefits.list_employee_benefits`](#bamboohrbenefitslist_employee_benefits)
  * [`bamboohr.benefits.list_employee_dependents`](#bamboohrbenefitslist_employee_dependents)
  * [`bamboohr.benefits.update_company_benefit`](#bamboohrbenefitsupdate_company_benefit)
  * [`bamboohr.benefits.update_dependent_information`](#bamboohrbenefitsupdate_dependent_information)
  * [`bamboohr.company_files.create_category`](#bamboohrcompany_filescreate_category)
  * [`bamboohr.company_files.get_file`](#bamboohrcompany_filesget_file)
  * [`bamboohr.company_files.list_files_and_categories`](#bamboohrcompany_fileslist_files_and_categories)
  * [`bamboohr.company_files.remove_file`](#bamboohrcompany_filesremove_file)
  * [`bamboohr.company_files.update_file`](#bamboohrcompany_filesupdate_file)
  * [`bamboohr.company_files.upload_file`](#bamboohrcompany_filesupload_file)
  * [`bamboohr.employee_files.add_category`](#bamboohremployee_filesadd_category)
  * [`bamboohr.employee_files.get_employee_file`](#bamboohremployee_filesget_employee_file)
  * [`bamboohr.employee_files.list_files_and_categories`](#bamboohremployee_fileslist_files_and_categories)
  * [`bamboohr.employee_files.remove_file`](#bamboohremployee_filesremove_file)
  * [`bamboohr.employee_files.update_employee_file`](#bamboohremployee_filesupdate_employee_file)
  * [`bamboohr.employee_files.upload_file`](#bamboohremployee_filesupload_file)
  * [`bamboohr.employees.create_new_employee`](#bamboohremployeescreate_new_employee)
  * [`bamboohr.employees.get_directory`](#bamboohremployeesget_directory)
  * [`bamboohr.employees.get_employee_data`](#bamboohremployeesget_employee_data)
  * [`bamboohr.employees.update_employee`](#bamboohremployeesupdate_employee)
  * [`bamboohr.goals.close_goal`](#bamboohrgoalsclose_goal)
  * [`bamboohr.goals.count_per_status`](#bamboohrgoalscount_per_status)
  * [`bamboohr.goals.create_comment`](#bamboohrgoalscreate_comment)
  * [`bamboohr.goals.create_employee_goal`](#bamboohrgoalscreate_employee_goal)
  * [`bamboohr.goals.delete_by_id`](#bamboohrgoalsdelete_by_id)
  * [`bamboohr.goals.delete_comment`](#bamboohrgoalsdelete_comment)
  * [`bamboohr.goals.determine_permission`](#bamboohrgoalsdetermine_permission)
  * [`bamboohr.goals.get_alignable_options`](#bamboohrgoalsget_alignable_options)
  * [`bamboohr.goals.get_all_aggregate_info`](#bamboohrgoalsget_all_aggregate_info)
  * [`bamboohr.goals.get_all_aggregate_info_0`](#bamboohrgoalsget_all_aggregate_info_0)
  * [`bamboohr.goals.get_all_aggregate_info_1`](#bamboohrgoalsget_all_aggregate_info_1)
  * [`bamboohr.goals.get_comments`](#bamboohrgoalsget_comments)
  * [`bamboohr.goals.get_employee_goals`](#bamboohrgoalsget_employee_goals)
  * [`bamboohr.goals.get_goal_aggregate_info`](#bamboohrgoalsget_goal_aggregate_info)
  * [`bamboohr.goals.reopen_goal`](#bamboohrgoalsreopen_goal)
  * [`bamboohr.goals.share_options_get`](#bamboohrgoalsshare_options_get)
  * [`bamboohr.goals.status_count`](#bamboohrgoalsstatus_count)
  * [`bamboohr.goals.update_comment`](#bamboohrgoalsupdate_comment)
  * [`bamboohr.goals.update_employee_goal`](#bamboohrgoalsupdate_employee_goal)
  * [`bamboohr.goals.update_employee_goal_v11`](#bamboohrgoalsupdate_employee_goal_v11)
  * [`bamboohr.goals.update_goal_sharing`](#bamboohrgoalsupdate_goal_sharing)
  * [`bamboohr.goals.update_progress`](#bamboohrgoalsupdate_progress)
  * [`bamboohr.hours.bulk_record_edit`](#bamboohrhoursbulk_record_edit)
  * [`bamboohr.hours.delete_hour_record`](#bamboohrhoursdelete_hour_record)
  * [`bamboohr.hours.edit_hour_record`](#bamboohrhoursedit_hour_record)
  * [`bamboohr.hours.get_hour_record`](#bamboohrhoursget_hour_record)
  * [`bamboohr.hours.record_addition`](#bamboohrhoursrecord_addition)
  * [`bamboohr.last_change_information.get_changed_employee_ids`](#bamboohrlast_change_informationget_changed_employee_ids)
  * [`bamboohr.login.user_credentials`](#bamboohrloginuser_credentials)
  * [`bamboohr.payroll.add_employee_direct_deposit_info`](#bamboohrpayrolladd_employee_direct_deposit_info)
  * [`bamboohr.payroll.add_employee_paystub`](#bamboohrpayrolladd_employee_paystub)
  * [`bamboohr.payroll.add_employee_unpaid_paystubs`](#bamboohrpayrolladd_employee_unpaid_paystubs)
  * [`bamboohr.payroll.add_employee_withholdings`](#bamboohrpayrolladd_employee_withholdings)
  * [`bamboohr.payroll.clear_employee_direct_deposit`](#bamboohrpayrollclear_employee_direct_deposit)
  * [`bamboohr.payroll.clear_employee_unpaid_paystubs`](#bamboohrpayrollclear_employee_unpaid_paystubs)
  * [`bamboohr.payroll.clear_employee_withholdings`](#bamboohrpayrollclear_employee_withholdings)
  * [`bamboohr.payroll.delete_employee_paystub`](#bamboohrpayrolldelete_employee_paystub)
  * [`bamboohr.payroll.employee_direct_deposit_info`](#bamboohrpayrollemployee_direct_deposit_info)
  * [`bamboohr.payroll.get_default_withholdings`](#bamboohrpayrollget_default_withholdings)
  * [`bamboohr.payroll.get_paystub`](#bamboohrpayrollget_paystub)
  * [`bamboohr.payroll.get_unpaid_paystubs`](#bamboohrpayrollget_unpaid_paystubs)
  * [`bamboohr.photos.get_employee_photo`](#bamboohrphotosget_employee_photo)
  * [`bamboohr.photos.store_new_employee_photo`](#bamboohrphotosstore_new_employee_photo)
  * [`bamboohr.reports.company_report`](#bamboohrreportscompany_report)
  * [`bamboohr.reports.request_custom_report`](#bamboohrreportsrequest_custom_report)
  * [`bamboohr.tabular_data.add_row`](#bamboohrtabular_dataadd_row)
  * [`bamboohr.tabular_data.add_table_row`](#bamboohrtabular_dataadd_table_row)
  * [`bamboohr.tabular_data.delete_row`](#bamboohrtabular_datadelete_row)
  * [`bamboohr.tabular_data.get_changed_table_rows`](#bamboohrtabular_dataget_changed_table_rows)
  * [`bamboohr.tabular_data.get_employee_table_rows`](#bamboohrtabular_dataget_employee_table_rows)
  * [`bamboohr.tabular_data.update_row`](#bamboohrtabular_dataupdate_row)
  * [`bamboohr.tabular_data.update_row_0`](#bamboohrtabular_dataupdate_row_0)
  * [`bamboohr.time_off.add_time_off_history_item`](#bamboohrtime_offadd_time_off_history_item)
  * [`bamboohr.time_off.assign_employee_policies`](#bamboohrtime_offassign_employee_policies)
  * [`bamboohr.time_off.assign_employee_policies_v11`](#bamboohrtime_offassign_employee_policies_v11)
  * [`bamboohr.time_off.balance_adjustment_put`](#bamboohrtime_offbalance_adjustment_put)
  * [`bamboohr.time_off.change_request_status`](#bamboohrtime_offchange_request_status)
  * [`bamboohr.time_off.estimate_future_time_off_balances`](#bamboohrtime_offestimate_future_time_off_balances)
  * [`bamboohr.time_off.get_policies`](#bamboohrtime_offget_policies)
  * [`bamboohr.time_off.get_time_off_requests`](#bamboohrtime_offget_time_off_requests)
  * [`bamboohr.time_off.get_time_off_types`](#bamboohrtime_offget_time_off_types)
  * [`bamboohr.time_off.get_whos_out_list`](#bamboohrtime_offget_whos_out_list)
  * [`bamboohr.time_off.list_employee_policies`](#bamboohrtime_offlist_employee_policies)
  * [`bamboohr.time_off.list_employee_time_off_policies`](#bamboohrtime_offlist_employee_time_off_policies)
  * [`bamboohr.time_off.request_creation`](#bamboohrtime_offrequest_creation)
  * [`bamboohr.time_tracking.approve_employee_timesheets`](#bamboohrtime_trackingapprove_employee_timesheets)
  * [`bamboohr.time_tracking.approve_employee_timesheets_0`](#bamboohrtime_trackingapprove_employee_timesheets_0)
  * [`bamboohr.time_tracking.clock_in_employee`](#bamboohrtime_trackingclock_in_employee)
  * [`bamboohr.time_tracking.clock_out_employee`](#bamboohrtime_trackingclock_out_employee)
  * [`bamboohr.time_tracking.clock_out_employee_at_specific_time`](#bamboohrtime_trackingclock_out_employee_at_specific_time)
  * [`bamboohr.time_tracking.delete_clock_entries`](#bamboohrtime_trackingdelete_clock_entries)
  * [`bamboohr.time_tracking.edit_clocked_in_entry_data`](#bamboohrtime_trackingedit_clocked_in_entry_data)
  * [`bamboohr.time_tracking.employee_clocked_in`](#bamboohrtime_trackingemployee_clocked_in)
  * [`bamboohr.time_tracking.employee_timesheet_get`](#bamboohrtime_trackingemployee_timesheet_get)
  * [`bamboohr.time_tracking.get_clock_entry`](#bamboohrtime_trackingget_clock_entry)
  * [`bamboohr.time_tracking.get_daily_entry`](#bamboohrtime_trackingget_daily_entry)
  * [`bamboohr.time_tracking.get_project_tasks`](#bamboohrtime_trackingget_project_tasks)
  * [`bamboohr.time_tracking.get_timesheets_by_ids`](#bamboohrtime_trackingget_timesheets_by_ids)
  * [`bamboohr.time_tracking.list_employee_projects`](#bamboohrtime_trackinglist_employee_projects)
  * [`bamboohr.time_tracking.store_clock_entries`](#bamboohrtime_trackingstore_clock_entries)
  * [`bamboohr.time_tracking.store_daily_entries`](#bamboohrtime_trackingstore_daily_entries)
  * [`bamboohr.time_tracking___private_beta.add_clock_out`](#bamboohrtime_tracking___private_betaadd_clock_out)
  * [`bamboohr.time_tracking___private_beta.add_edit_clock_entries`](#bamboohrtime_tracking___private_betaadd_edit_clock_entries)
  * [`bamboohr.time_tracking___private_beta.add_edit_hour_entries`](#bamboohrtime_tracking___private_betaadd_edit_hour_entries)
  * [`bamboohr.time_tracking___private_beta.add_timesheet_clock_in`](#bamboohrtime_tracking___private_betaadd_timesheet_clock_in)
  * [`bamboohr.time_tracking___private_beta.create_project_task`](#bamboohrtime_tracking___private_betacreate_project_task)
  * [`bamboohr.time_tracking___private_beta.delete_hour_entries`](#bamboohrtime_tracking___private_betadelete_hour_entries)
  * [`bamboohr.time_tracking___private_beta.delete_time_sheet_entries`](#bamboohrtime_tracking___private_betadelete_time_sheet_entries)
  * [`bamboohr.time_tracking___private_beta.list_employee_projects`](#bamboohrtime_tracking___private_betalist_employee_projects)
  * [`bamboohr.time_tracking___private_beta.list_timesheet_entries`](#bamboohrtime_tracking___private_betalist_timesheet_entries)
  * [`bamboohr.training.add_category`](#bamboohrtrainingadd_category)
  * [`bamboohr.training.add_employee_training_record`](#bamboohrtrainingadd_employee_training_record)
  * [`bamboohr.training.category_list`](#bamboohrtrainingcategory_list)
  * [`bamboohr.training.delete_category`](#bamboohrtrainingdelete_category)
  * [`bamboohr.training.delete_employee_record`](#bamboohrtrainingdelete_employee_record)
  * [`bamboohr.training.get_types`](#bamboohrtrainingget_types)
  * [`bamboohr.training.list_employee_trainings`](#bamboohrtraininglist_employee_trainings)
  * [`bamboohr.training.remove_type`](#bamboohrtrainingremove_type)
  * [`bamboohr.training.type_addition`](#bamboohrtrainingtype_addition)
  * [`bamboohr.training.update_category`](#bamboohrtrainingupdate_category)
  * [`bamboohr.training.update_employee_training_record`](#bamboohrtrainingupdate_employee_training_record)
  * [`bamboohr.training.update_type`](#bamboohrtrainingupdate_type)
  * [`bamboohr.webhooks.add_new_webhook`](#bamboohrwebhooksadd_new_webhook)
  * [`bamboohr.webhooks.delete_webhook`](#bamboohrwebhooksdelete_webhook)
  * [`bamboohr.webhooks.get_user_list`](#bamboohrwebhooksget_user_list)
  * [`bamboohr.webhooks.get_user_webhook`](#bamboohrwebhooksget_user_webhook)
  * [`bamboohr.webhooks.get_webhook_logs`](#bamboohrwebhooksget_webhook_logs)
  * [`bamboohr.webhooks.list_monitor_fields`](#bamboohrwebhookslist_monitor_fields)
  * [`bamboohr.webhooks.update_webhook_by_id`](#bamboohrwebhooksupdate_webhook_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=BambooHR&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from bamboo_hr_python_sdk import BambooHr, ApiException

bamboohr = BambooHr(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

try:
    # Get a list of tabular fields
    bamboohr.account_information.discover_table_fields(
        company_domain="companyDomain_example",
    )
except ApiException as e:
    print("Exception when calling AccountInformationApi.discover_table_fields: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from bamboo_hr_python_sdk import BambooHr, ApiException

bamboohr = BambooHr(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

async def main():
    try:
        # Get a list of tabular fields
        await bamboohr.account_information.adiscover_table_fields(
            company_domain="companyDomain_example",
        )
    except ApiException as e:
        print("Exception when calling AccountInformationApi.discover_table_fields: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from bamboo_hr_python_sdk import BambooHr, ApiException

bamboohr = BambooHr(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

try:
    # Get a list of tabular fields
    discover_table_fields_response = bamboohr.account_information.raw.discover_table_fields(
        company_domain="companyDomain_example",
    )
    pprint(discover_table_fields_response.headers)
    pprint(discover_table_fields_response.status)
    pprint(discover_table_fields_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountInformationApi.discover_table_fields: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `bamboohr.account_information.discover_table_fields`<a id="bamboohraccount_informationdiscover_table_fields"></a>

This endpoint can help discover table fields available in your BambooHR account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.account_information.discover_table_fields(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/tables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.account_information.get_field_list`<a id="bamboohraccount_informationget_field_list"></a>

This endpoint can help with discovery of fields that are available in an account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.account_information.get_field_list(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.account_information.get_list_fields`<a id="bamboohraccount_informationget_list_fields"></a>

This endpoint will return details for all list fields. Lists that can be edited will have the "manageable" attribute set to yes. Lists with the "multiple" attribute set to yes are fields that can have multiple values. Options with the "archived" attribute set to yes should not appear as current options, but are included so that historical data can reference the value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.account_information.get_list_fields(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.account_information.get_user_list`<a id="bamboohraccount_informationget_user_list"></a>

Get a List of Users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.account_information.get_user_list(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.account_information.update_list_field_values`<a id="bamboohraccount_informationupdate_list_field_values"></a>

This resource accepts one or more options. To update an option, specify an ID. You may also remove an option from the list of current values by archiving the value. To create a new option, do not specify an "id" attribute.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.account_information.update_list_field_values(
    company_domain="companyDomain_example",
    list_field_id="listFieldId_example",
    options=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### list_field_id: `str`<a id="list_field_id-str"></a>

##### options: [`ListFieldValuesOptions`](./bamboo_hr_python_sdk/type/list_field_values_options.py)<a id="options-listfieldvaluesoptionsbamboo_hr_python_sdktypelist_field_values_optionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListFieldValues`](./bamboo_hr_python_sdk/type/list_field_values.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/lists/{listFieldId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.add_application_comment`<a id="bamboohrapplicant_trackingadd_application_comment"></a>

Add a comment to an application. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.applicant_tracking.add_application_comment(
    type="comment",
    comment="I really like this applicant",
    company_domain="companyDomain_example",
    application_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Always the value \\\"comment\\\".

##### comment: `str`<a id="comment-str"></a>

The comment being posted.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### application_id: `int`<a id="application_id-int"></a>

The ID of the application to add a comment to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantTrackingAddApplicationCommentRequest`](./bamboo_hr_python_sdk/type/applicant_tracking_add_application_comment_request.py)
Comment object to post

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/applications/{applicationId}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.change_applicant_status`<a id="bamboohrapplicant_trackingchange_applicant_status"></a>

Change applicant's status. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.applicant_tracking.change_applicant_status(
    status=2,
    company_domain="companyDomain_example",
    application_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `int`<a id="status-int"></a>

Associates a status id with an application.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### application_id: `int`<a id="application_id-int"></a>

The ID of the application to add a comment to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantTrackingChangeApplicantStatusRequest`](./bamboo_hr_python_sdk/type/applicant_tracking_change_applicant_status_request.py)
Sample Post Data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/applications/{applicationId}/status` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.create_new_application`<a id="bamboohrapplicant_trackingcreate_new_application"></a>

Add a new candidate application to a job opening. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_application_response = bamboohr.applicant_tracking.create_new_application(
    company_domain="companyDomain_example",
    first_name="string_example",
    last_name="string_example",
    job_id=1,
    email="string_example",
    phone_number="string_example",
    source="string_example",
    address="string_example",
    city="string_example",
    state="string_example",
    zip="string_example",
    country="string_example",
    linkedin_url="string_example",
    date_available="string_example",
    desired_salary="string_example",
    referred_by="string_example",
    website_url="string_example",
    highest_education="GED or Equivalent",
    college_name="string_example",
    references="string_example",
    resume=open('/path/to/file', 'rb'),
    cover_letter=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### first_name: `str`<a id="first_name-str"></a>

The first name of the candidate.

##### last_name: `str`<a id="last_name-str"></a>

The last name of the candidate.

##### job_id: `int`<a id="job_id-int"></a>

The id of the job opening for the candidate application.

##### email: `str`<a id="email-str"></a>

The email address of the candidate.

##### phone_number: `str`<a id="phone_number-str"></a>

The phone number of the candidate.

##### source: `str`<a id="source-str"></a>

The source of the candidate application, e.g. LinkedIn, Indeed, etc.

##### address: `str`<a id="address-str"></a>

The street address of the candidate.

##### city: `str`<a id="city-str"></a>

The city of the candidate.

##### state: `str`<a id="state-str"></a>

The state or province of the candidate. Accepts state name, abbreviation, or ISO code.

##### zip: `str`<a id="zip-str"></a>

The zip code or postal code of the candidate.

##### country: `str`<a id="country-str"></a>

The country of the candidate. Accepts country name or ISO code.

##### linkedin_url: `str`<a id="linkedin_url-str"></a>

The LinkedIn profile url of the candidate.

##### date_available: `str`<a id="date_available-str"></a>

The available start date of the candidate with the format YYYY-MM-DD.

##### desired_salary: `str`<a id="desired_salary-str"></a>

The desired salary of the candidate.

##### referred_by: `str`<a id="referred_by-str"></a>

The person or entity that referred the candidate.

##### website_url: `str`<a id="website_url-str"></a>

The personal website, blog, or online portfolio of the candidate.

##### highest_education: `str`<a id="highest_education-str"></a>

The highest completed education level of the candidate.

##### college_name: `str`<a id="college_name-str"></a>

The college or university of the candidate.

##### references: `str`<a id="references-str"></a>

A list of references supplied by the candidate.

##### resume: `IO`<a id="resume-io"></a>

Resume of the candidate.

##### cover_letter: `IO`<a id="cover_letter-io"></a>

Cover letter of the candidate.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantTrackingCreateNewApplicationRequest`](./bamboo_hr_python_sdk/type/applicant_tracking_create_new_application_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingCreateNewApplicationResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_create_new_application_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/application` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.create_new_job_opening`<a id="bamboohrapplicant_trackingcreate_new_job_opening"></a>

Add a new job opening. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_job_opening_response = bamboohr.applicant_tracking.create_new_job_opening(
    company_domain="companyDomain_example",
    posting_title="string_example",
    job_status="Draft",
    hiring_lead=1,
    employment_type="string_example",
    job_description="string_example",
    department="string_example",
    minimum_experience="Entry-level",
    compensation="string_example",
    job_location=1,
    application_question_resume="true",
    application_question_address="true",
    application_question_linkedin_url="true",
    application_question_date_available="true",
    application_question_desired_salary="true",
    application_question_cover_letter="true",
    application_question_referred_by="true",
    application_question_website_url="true",
    application_question_highest_education="true",
    application_question_college="true",
    application_question_references="true",
    internal_job_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### posting_title: `str`<a id="posting_title-str"></a>

The posting title of the job opening.

##### job_status: `str`<a id="job_status-str"></a>

The status of the job opening.

##### hiring_lead: `int`<a id="hiring_lead-int"></a>

The employee id (from the v1/applicant_tracking/hiring_leads endpoint) of the hiring lead for the job opening.

##### employment_type: `str`<a id="employment_type-str"></a>

The type of employment offered in the job opening, e.g. Full-Time, Part-Time, Contractor, etc.

##### job_description: `str`<a id="job_description-str"></a>

The long-form text description of the job opening.

##### department: `str`<a id="department-str"></a>

The department of the job opening.

##### minimum_experience: `str`<a id="minimum_experience-str"></a>

The minimum experience level that qualifies a candidate for the job opening.

##### compensation: `str`<a id="compensation-str"></a>

The pay rate or compensation for the job opening.

##### job_location: `int`<a id="job_location-int"></a>

The location id (from the v1/applicant_tracking/locations endpoint) of the job opening. Omit this parameter for a remote job location.

##### application_question_resume: `str`<a id="application_question_resume-str"></a>

Whether the job opening application has a standard question for resume (true) or not (false) or if uploading a resume is mandatory (required).

##### application_question_address: `str`<a id="application_question_address-str"></a>

Whether the job opening application has a standard question for address (true) or not (false) or if entering an address is mandatory (required).

##### application_question_linkedin_url: `str`<a id="application_question_linkedin_url-str"></a>

Whether the job opening application has a standard question for LinkedIn profile url (true) or not (false) or if entering a LinkedIn profile url is mandatory (required).

##### application_question_date_available: `str`<a id="application_question_date_available-str"></a>

Whether the job opening application has a standard question for availability date (true) or not (false) or if entering an availability date is mandatory (required).

##### application_question_desired_salary: `str`<a id="application_question_desired_salary-str"></a>

Whether the job opening application has a standard question for desired salary (true) or not (false) or if entering a desired salary is mandatory (required).

##### application_question_cover_letter: `str`<a id="application_question_cover_letter-str"></a>

Whether the job opening application has a standard question for cover letter (true) or not (false) or if uploading a cover letter is mandatory (required).

##### application_question_referred_by: `str`<a id="application_question_referred_by-str"></a>

Whether the job opening application has a standard question for referred by (true) or not (false) or if entering referred by is mandatory (required).

##### application_question_website_url: `str`<a id="application_question_website_url-str"></a>

Whether the job opening application has a standard question for website url (true) or not (false) or if entering a website url is mandatory (required).

##### application_question_highest_education: `str`<a id="application_question_highest_education-str"></a>

Whether the job opening application has a standard question for highest education (true) or not (false) or if entering highest education is mandatory (required).

##### application_question_college: `str`<a id="application_question_college-str"></a>

Whether the job opening application has a standard question for college (true) or not (false) or if entering a college is mandatory (required).

##### application_question_references: `str`<a id="application_question_references-str"></a>

Whether the job opening application has a standard question for references (true) or not (false) or if entering references is mandatory (required).

##### internal_job_code: `str`<a id="internal_job_code-str"></a>

The internal job code for the job opening.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantTrackingCreateNewJobOpeningRequest`](./bamboo_hr_python_sdk/type/applicant_tracking_create_new_job_opening_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingCreateNewJobOpeningResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_create_new_job_opening_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/job_opening` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.get_application_details`<a id="bamboohrapplicant_trackingget_application_details"></a>

Get the details of an application. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_details_response = bamboohr.applicant_tracking.get_application_details(
    company_domain="companyDomain_example",
    application_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### application_id: `int`<a id="application_id-int"></a>

The ID of the application to look up details.

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingGetApplicationDetailsResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_get_application_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/applications/{applicationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.get_company_locations`<a id="bamboohrapplicant_trackingget_company_locations"></a>

Get company locations for use in creating a new job opening. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_locations_response = bamboohr.applicant_tracking.get_company_locations(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingGetCompanyLocationsResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_get_company_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.get_hiring_leads`<a id="bamboohrapplicant_trackingget_hiring_leads"></a>

Get potential hiring leads for use in creating a new job opening. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_hiring_leads_response = bamboohr.applicant_tracking.get_hiring_leads(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingGetHiringLeadsResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_get_hiring_leads_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/hiring_leads` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.get_job_summaries`<a id="bamboohrapplicant_trackingget_job_summaries"></a>

Get a list of job summaries. The owner of the API key used must have access to ATS settings. Combine as many different optional parameter filters as you like.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_summaries_response = bamboohr.applicant_tracking.get_job_summaries(
    company_domain="companyDomain_example",
    status_groups="ALL",
    sort_by="count",
    sort_order="ASC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### status_groups: `str`<a id="status_groups-str"></a>

A list of status groups to filter positions by.

##### sort_by: `str`<a id="sort_by-str"></a>

A specific field to sort the results by.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which to sort results.

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingGetJobSummariesResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_get_job_summaries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.list_applications`<a id="bamboohrapplicant_trackinglist_applications"></a>

Get a list of applications. The owner of the API key used must have access to ATS settings. Combine as many different optional parameter filters as you like.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_applications_response = bamboohr.applicant_tracking.list_applications(
    company_domain="companyDomain_example",
    page=1,
    job_id=1,
    application_status_id=1,
    application_status="ALL",
    job_status_groups="ALL",
    search_string="string_example",
    sort_by="first_name",
    sort_order="ASC",
    new_since="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### page: `int`<a id="page-int"></a>

The page number

##### job_id: `int`<a id="job_id-int"></a>

A Job Id to limit results to

##### application_status_id: `int`<a id="application_status_id-int"></a>

Application status id to filter by.

##### application_status: `str`<a id="application_status-str"></a>

A list of application status groups to filter by.

##### job_status_groups: `str`<a id="job_status_groups-str"></a>

A list of position status groups to filter by.

##### search_string: `str`<a id="search_string-str"></a>

A general search criteria by which to find applications.

##### sort_by: `str`<a id="sort_by-str"></a>

A specific field to sort the results by.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which to sort results.

##### new_since: `datetime`<a id="new_since-datetime"></a>

Only get applications newer than a given UTC timestamp, for example 2024-01-01 13:00:00

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingListApplicationsResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_list_applications_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/applications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.applicant_tracking.list_statuses`<a id="bamboohrapplicant_trackinglist_statuses"></a>

Get a list of statuses for a company. The owner of the API key used must have access to ATS settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_statuses_response = bamboohr.applicant_tracking.list_statuses(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantTrackingListStatusesResponse`](./bamboo_hr_python_sdk/pydantic/applicant_tracking_list_statuses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/applicant_tracking/statuses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.add_benefit_group_employee`<a id="bamboohrbenefitsadd_benefit_group_employee"></a>

Add a benefit group employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.add_benefit_group_employee(
    company_domain="companyDomain_example",
    benefit_group_id="string_example",
    employee_id="string_example",
    start_date="string_example",
    end_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### benefit_group_id: `str`<a id="benefit_group_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### start_date: `str`<a id="start_date-str"></a>

##### end_date: `str`<a id="end_date-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BenefitGroupEmployee`](./bamboo_hr_python_sdk/type/benefit_group_employee.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitgroupemployees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.add_employee_benefit`<a id="bamboohrbenefitsadd_employee_benefit"></a>

Add an employee benefit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.add_employee_benefit(
    body=None,
    company_domain="companyDomain_example",
    employee_id=1,
    company_benefit_id=1,
    company_benefit_name="string_example",
    coverage_level="string_example",
    deduction_end_date="1970-01-01",
    deduction_start_date="1970-01-01",
    enrollment_status="Eligible",
    effective_date="1970-01-01",
    currency_code="string_example",
    employee_amount=3.14,
    employee_amount_type="string_example",
    employee_percent_based_on="string_example",
    employee_cap_amount=3.14,
    employee_cap_amount_type="string_example",
    employee_annual_max=3.14,
    company_amount=3.14,
    company_amount_type="string_example",
    company_percent_based_on="string_example",
    company_cap_amount=3.14,
    company_cap_amount_type="string_example",
    company_annual_max=3.14,
    benefit_plan_coverage_id=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `int`<a id="employee_id-int"></a>

Employee ID

##### company_benefit_id: `int`<a id="company_benefit_id-int"></a>

Company benefit ID

##### company_benefit_name: `str`<a id="company_benefit_name-str"></a>

Company benefit name

##### coverage_level: `str`<a id="coverage_level-str"></a>

Coverage level

##### deduction_end_date: `date`<a id="deduction_end_date-date"></a>

Deduction end date

##### deduction_start_date: `date`<a id="deduction_start_date-date"></a>

Deduction start date

##### enrollment_status: `str`<a id="enrollment_status-str"></a>

Enrollment status

##### effective_date: `date`<a id="effective_date-date"></a>

Enrollment status effective date

##### currency_code: `str`<a id="currency_code-str"></a>

Currency code

##### employee_amount: `Union[int, float]`<a id="employee_amount-unionint-float"></a>

Employee amount

##### employee_amount_type: `str`<a id="employee_amount_type-str"></a>

Employee amount type

##### employee_percent_based_on: `str`<a id="employee_percent_based_on-str"></a>

Employee percent based on

##### employee_cap_amount: `Union[int, float]`<a id="employee_cap_amount-unionint-float"></a>

Employee cap amount

##### employee_cap_amount_type: `str`<a id="employee_cap_amount_type-str"></a>

Employee cap amount type

##### employee_annual_max: `Union[int, float]`<a id="employee_annual_max-unionint-float"></a>

Employee annual max

##### company_amount: `Union[int, float]`<a id="company_amount-unionint-float"></a>

Company amount

##### company_amount_type: `str`<a id="company_amount_type-str"></a>

Company amount type

##### company_percent_based_on: `str`<a id="company_percent_based_on-str"></a>

Company percent based on

##### company_cap_amount: `Union[int, float]`<a id="company_cap_amount-unionint-float"></a>

Company cap amount

##### company_cap_amount_type: `str`<a id="company_cap_amount_type-str"></a>

Company cap amount type

##### company_annual_max: `Union[int, float]`<a id="company_annual_max-unionint-float"></a>

Company annual max

##### benefit_plan_coverage_id: `Union[int, float]`<a id="benefit_plan_coverage_id-unionint-float"></a>

Benefit Plan Coverage ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BenefitsAddEmployeeBenefitRequest`](./bamboo_hr_python_sdk/type/benefits_add_employee_benefit_request.py)
Employee Benefit

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/employee_benefit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.add_new_company_benefit`<a id="bamboohrbenefitsadd_new_company_benefit"></a>

Add a new company benefit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_company_benefit_response = bamboohr.benefits.add_new_company_benefit(
    body=None,
    company_domain="companyDomain_example",
    description="string_example",
    company_benefit_name="string_example",
    benefit_vendor_id="string_example",
    benefit_type="health",
    deduction_type_id="string_example",
    start_date="1970-01-01",
    end_date="1970-01-01",
    plan_url="string_example",
    sso_login_url="string_example",
    sso_login_url_link_text="string_example",
    safe_harbor=True,
    meet_aca_min=True,
    reimbursement_amount=3.14,
    reimbursement_frequency="pay period",
    reimbursement_currency_code="string_example",
    min_essential_coverage=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### description: `str`<a id="description-str"></a>

Description

##### company_benefit_name: `str`<a id="company_benefit_name-str"></a>

Name

##### benefit_vendor_id: `str`<a id="benefit_vendor_id-str"></a>

Benefit vendor ID

##### benefit_type: `str`<a id="benefit_type-str"></a>

Benefit type

##### deduction_type_id: `str`<a id="deduction_type_id-str"></a>

Deduction type ID

##### start_date: `date`<a id="start_date-date"></a>

Benefit start date

##### end_date: `date`<a id="end_date-date"></a>

Benefit end date

##### plan_url: `str`<a id="plan_url-str"></a>

Plan url

##### sso_login_url: `str`<a id="sso_login_url-str"></a>

SSO login url

##### sso_login_url_link_text: `str`<a id="sso_login_url_link_text-str"></a>

SSO login link text

##### safe_harbor: `bool`<a id="safe_harbor-bool"></a>

Is a safe harbor

##### meet_aca_min: `bool`<a id="meet_aca_min-bool"></a>

Meets ACA minimum requirements

##### reimbursement_amount: `Union[int, float]`<a id="reimbursement_amount-unionint-float"></a>

Reimbursement amount

##### reimbursement_frequency: `str`<a id="reimbursement_frequency-str"></a>

Reimbursement frequency

##### reimbursement_currency_code: `str`<a id="reimbursement_currency_code-str"></a>

Reimbursement currency code

##### min_essential_coverage: `bool`<a id="min_essential_coverage-bool"></a>

Provides minimum essential coverage

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BenefitsAddNewCompanyBenefitRequest`](./bamboo_hr_python_sdk/type/benefits_add_new_company_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitResponse`](./bamboo_hr_python_sdk/pydantic/company_benefit_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/company_benefit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.create_employee_dependent`<a id="bamboohrbenefitscreate_employee_dependent"></a>

Adds an employee dependent

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.create_employee_dependent(
    company_domain="companyDomain_example",
    employee_id="string_example",
    first_name="string_example",
    middle_name="string_example",
    last_name="string_example",
    relationship="string_example",
    gender="string_example",
    ssn="string_example",
    date_of_birth="string_example",
    address_line1="string_example",
    address_line2="string_example",
    city="string_example",
    state="string_example",
    zip_code="string_example",
    home_phone="string_example",
    country="string_example",
    is_us_citizen="string_example",
    is_student="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### middle_name: `str`<a id="middle_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### relationship: `str`<a id="relationship-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### date_of_birth: `str`<a id="date_of_birth-str"></a>

##### address_line1: `str`<a id="address_line1-str"></a>

##### address_line2: `str`<a id="address_line2-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip_code: `str`<a id="zip_code-str"></a>

##### home_phone: `str`<a id="home_phone-str"></a>

##### country: `str`<a id="country-str"></a>

##### is_us_citizen: `str`<a id="is_us_citizen-str"></a>

##### is_student: `str`<a id="is_student-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDependent`](./bamboo_hr_python_sdk/type/employee_dependent.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employeedependents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.delete_company_benefit`<a id="bamboohrbenefitsdelete_company_benefit"></a>

Delete a company benefit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.delete_company_benefit(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the company benefit ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/company_benefit/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_benefit_group_employees`<a id="bamboohrbenefitsget_benefit_group_employees"></a>

Get benefit group employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_benefit_group_employees(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitgroupemployees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_benefit_groups`<a id="bamboohrbenefitsget_benefit_groups"></a>

Get benefit groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_benefit_groups(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitgroups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_benefit_plan_deductions_by_employee`<a id="bamboohrbenefitsget_benefit_plan_deductions_by_employee"></a>

Get benefit plan deductions by employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_benefit_plan_deductions_by_employee(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee/plans/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_benefit_plans`<a id="bamboohrbenefitsget_benefit_plans"></a>

Get benefit plans

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_benefit_plans(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitplans` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_company_benefit`<a id="bamboohrbenefitsget_company_benefit"></a>

Get a company benefit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_benefit_response = bamboohr.benefits.get_company_benefit(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the company benefit ID.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitResponse`](./bamboo_hr_python_sdk/pydantic/company_benefit_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/company_benefit/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_coverages`<a id="bamboohrbenefitsget_coverages"></a>

Get benefit coverages

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_coverages(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitcoverages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_deduction_types_all`<a id="bamboohrbenefitsget_deduction_types_all"></a>

Get benefit deduction types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_deduction_types_all(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefits/settings/deduction_types/all` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_deductions_by_plan`<a id="bamboohrbenefitsget_deductions_by_plan"></a>

Get employee deductions by benefit plan

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_deductions_by_plan(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the benefit plan ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee/deductions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_employee_benefit_deductions`<a id="bamboohrbenefitsget_employee_benefit_deductions"></a>

Get benefit deductions for employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_employee_benefit_deductions(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/payroll/deductions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_employee_dependent`<a id="bamboohrbenefitsget_employee_dependent"></a>

Get employee dependent

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_employee_dependent(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee dependent ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employeedependents/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_group_plan_costs`<a id="bamboohrbenefitsget_group_plan_costs"></a>

Get benefit group plan costs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_group_plan_costs(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitgroupplancosts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.get_group_plans`<a id="bamboohrbenefitsget_group_plans"></a>

Get benefit group plans

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.get_group_plans(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitgroupplans` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.list_benefit_plan_coverages`<a id="bamboohrbenefitslist_benefit_plan_coverages"></a>

Get benefit plan coverages

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.list_benefit_plan_coverages(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefitplancoverages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.list_company_benefit_types`<a id="bamboohrbenefitslist_company_benefit_types"></a>

Get a list of company benefit types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_benefit_types_response = bamboohr.benefits.list_company_benefit_types(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitsListCompanyBenefitTypesResponse`](./bamboo_hr_python_sdk/pydantic/benefits_list_company_benefit_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/company_benefit/type` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.list_company_benefits`<a id="bamboohrbenefitslist_company_benefits"></a>

Get a list of company benefits

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_benefits_response = bamboohr.benefits.list_company_benefits(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitsListCompanyBenefitsResponse`](./bamboo_hr_python_sdk/pydantic/benefits_list_company_benefits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/company_benefit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.list_employee_benefits`<a id="bamboohrbenefitslist_employee_benefits"></a>

Get a list of employee benefits

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_benefits_response = bamboohr.benefits.list_employee_benefits(
    company_domain="companyDomain_example",
    filters={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### filters: [`EmployeeBenefitFiltersFilters`](./bamboo_hr_python_sdk/type/employee_benefit_filters_filters.py)<a id="filters-employeebenefitfiltersfiltersbamboo_hr_python_sdktypeemployee_benefit_filters_filterspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitFilters`](./bamboo_hr_python_sdk/type/employee_benefit_filters.py)
Employee Benefit Filters

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitsListEmployeeBenefitsResponse`](./bamboo_hr_python_sdk/pydantic/benefits_list_employee_benefits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/employee_benefit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.list_employee_dependents`<a id="bamboohrbenefitslist_employee_dependents"></a>

Get all employee dependents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.list_employee_dependents(
    company_domain="companyDomain_example",
    employeeid="employeeid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employeeid: `str`<a id="employeeid-str"></a>

{employeeid} is the employee ID. Supplying this ID limits the response to the specific employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employeedependents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.update_company_benefit`<a id="bamboohrbenefitsupdate_company_benefit"></a>

Update a company benefit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_company_benefit_response = bamboohr.benefits.update_company_benefit(
    body=None,
    company_domain="companyDomain_example",
    id="id_example",
    description="string_example",
    company_benefit_name="string_example",
    benefit_vendor_id="string_example",
    benefit_type="health",
    deduction_type_id="string_example",
    start_date="1970-01-01",
    end_date="1970-01-01",
    plan_url="string_example",
    sso_login_url="string_example",
    sso_login_url_link_text="string_example",
    safe_harbor=True,
    meet_aca_min=True,
    reimbursement_amount=3.14,
    reimbursement_frequency="pay period",
    reimbursement_currency_code="string_example",
    min_essential_coverage=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the company benefit ID.

##### description: `str`<a id="description-str"></a>

Description

##### company_benefit_name: `str`<a id="company_benefit_name-str"></a>

Name

##### benefit_vendor_id: `str`<a id="benefit_vendor_id-str"></a>

Benefit vendor ID

##### benefit_type: `str`<a id="benefit_type-str"></a>

Benefit type

##### deduction_type_id: `str`<a id="deduction_type_id-str"></a>

Deduction type ID

##### start_date: `date`<a id="start_date-date"></a>

Benefit start date

##### end_date: `date`<a id="end_date-date"></a>

Benefit end date

##### plan_url: `str`<a id="plan_url-str"></a>

Plan url

##### sso_login_url: `str`<a id="sso_login_url-str"></a>

SSO login url

##### sso_login_url_link_text: `str`<a id="sso_login_url_link_text-str"></a>

SSO login link text

##### safe_harbor: `bool`<a id="safe_harbor-bool"></a>

Is a safe harbor

##### meet_aca_min: `bool`<a id="meet_aca_min-bool"></a>

Meets ACA minimum requirements

##### reimbursement_amount: `Union[int, float]`<a id="reimbursement_amount-unionint-float"></a>

Reimbursement amount

##### reimbursement_frequency: `str`<a id="reimbursement_frequency-str"></a>

Reimbursement frequency

##### reimbursement_currency_code: `str`<a id="reimbursement_currency_code-str"></a>

Reimbursement currency code

##### min_essential_coverage: `bool`<a id="min_essential_coverage-bool"></a>

Provides minimum essential coverage

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BenefitsUpdateCompanyBenefitRequest`](./bamboo_hr_python_sdk/type/benefits_update_company_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitResponse`](./bamboo_hr_python_sdk/pydantic/company_benefit_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/benefit/company_benefit/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.benefits.update_dependent_information`<a id="bamboohrbenefitsupdate_dependent_information"></a>

This API allows you to change the information for a given dependent ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.benefits.update_dependent_information(
    company_domain="companyDomain_example",
    id="id_example",
    employee_id="string_example",
    first_name="string_example",
    middle_name="string_example",
    last_name="string_example",
    relationship="string_example",
    gender="string_example",
    ssn="string_example",
    date_of_birth="string_example",
    address_line1="string_example",
    address_line2="string_example",
    city="string_example",
    state="string_example",
    zip_code="string_example",
    home_phone="string_example",
    country="string_example",
    is_us_citizen="string_example",
    is_student="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee dependent ID.

##### employee_id: `str`<a id="employee_id-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### middle_name: `str`<a id="middle_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### relationship: `str`<a id="relationship-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### date_of_birth: `str`<a id="date_of_birth-str"></a>

##### address_line1: `str`<a id="address_line1-str"></a>

##### address_line2: `str`<a id="address_line2-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip_code: `str`<a id="zip_code-str"></a>

##### home_phone: `str`<a id="home_phone-str"></a>

##### country: `str`<a id="country-str"></a>

##### is_us_citizen: `str`<a id="is_us_citizen-str"></a>

##### is_student: `str`<a id="is_student-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDependent`](./bamboo_hr_python_sdk/type/employee_dependent.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employeedependents/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.company_files.create_category`<a id="bamboohrcompany_filescreate_category"></a>

Add a company file category.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.company_files.create_category(
    body=["A new category"],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### requestBody: [`NewCompanyFileCategory`](./bamboo_hr_python_sdk/type/new_company_file_category.py)<a id="requestbody-newcompanyfilecategorybamboo_hr_python_sdktypenew_company_file_categorypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/files/categories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.company_files.get_file`<a id="bamboohrcompany_filesget_file"></a>

Gets an company file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.company_files.get_file(
    company_domain="companyDomain_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### file_id: `str`<a id="file_id-str"></a>

{fileId} is the ID of the company file being retrieved.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/files/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.company_files.list_files_and_categories`<a id="bamboohrcompany_fileslist_files_and_categories"></a>

Lists company files and categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.company_files.list_files_and_categories(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/files/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.company_files.remove_file`<a id="bamboohrcompany_filesremove_file"></a>

Delete a company file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.company_files.remove_file(
    company_domain="companyDomain_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### file_id: `str`<a id="file_id-str"></a>

{fileId} is the ID of the company file being deleted.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/files/{fileId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.company_files.update_file`<a id="bamboohrcompany_filesupdate_file"></a>

Update a company file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.company_files.update_file(
    company_domain="companyDomain_example",
    file_id="fileId_example",
    name="string_example",
    category_id="string_example",
    share_with_employee="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### file_id: `str`<a id="file_id-str"></a>

{fileId} is the ID of the employee file being updated.

##### name: `str`<a id="name-str"></a>

##### category_id: `str`<a id="category_id-str"></a>

##### share_with_employee: `str`<a id="share_with_employee-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyFileUpdate`](./bamboo_hr_python_sdk/type/company_file_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/files/{fileId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.company_files.upload_file`<a id="bamboohrcompany_filesupload_file"></a>

Upload a company file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.company_files.upload_file(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/files` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employee_files.add_category`<a id="bamboohremployee_filesadd_category"></a>

Add an employee file category.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employee_files.add_category(
    body=["A new category"],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### requestBody: [`PostNewEmployeeFileCategory`](./bamboo_hr_python_sdk/type/post_new_employee_file_category.py)<a id="requestbody-postnewemployeefilecategorybamboo_hr_python_sdktypepost_new_employee_file_categorypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/files/categories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employee_files.get_employee_file`<a id="bamboohremployee_filesget_employee_file"></a>

Gets an employee file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employee_files.get_employee_file(
    company_domain="companyDomain_example",
    id="0",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).

##### file_id: `str`<a id="file_id-str"></a>

{fileId} is the ID of the employee file being retrieved.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/files/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employee_files.list_files_and_categories`<a id="bamboohremployee_fileslist_files_and_categories"></a>

Lists employee files and categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employee_files.list_files_and_categories(
    company_domain="companyDomain_example",
    id="0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/files/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employee_files.remove_file`<a id="bamboohremployee_filesremove_file"></a>

Delete an employee file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employee_files.remove_file(
    company_domain="companyDomain_example",
    id="0",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).

##### file_id: `str`<a id="file_id-str"></a>

{fileId} is the ID of the employee file being deleted.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/files/{fileId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employee_files.update_employee_file`<a id="bamboohremployee_filesupdate_employee_file"></a>

Update an employee file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employee_files.update_employee_file(
    company_domain="companyDomain_example",
    id="0",
    file_id="fileId_example",
    name="string_example",
    category_id="string_example",
    share_with_employee="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).

##### file_id: `str`<a id="file_id-str"></a>

{fileId} is the ID of the employee file being updated.

##### name: `str`<a id="name-str"></a>

##### category_id: `str`<a id="category_id-str"></a>

##### share_with_employee: `str`<a id="share_with_employee-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeFileUpdate`](./bamboo_hr_python_sdk/type/employee_file_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/files/{fileId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employee_files.upload_file`<a id="bamboohremployee_filesupload_file"></a>

Upload an employee file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employee_files.upload_file(
    company_domain="companyDomain_example",
    id="0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/files` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employees.create_new_employee`<a id="bamboohremployeescreate_new_employee"></a>

Add a new employee. New employees must have at least a first name and a last name. The ID of the newly created employee is included in the Location header of the response. Other fields can be included. Please see the [fields](ref:metadata-get-a-list-of-fields) endpoint. New Employees added to a pay schedule synced with Trax Payroll must have the following required fields (listed by API field name): employeeNumber, firstName, lastName, dateOfBirth, ssn, gender, maritalStatus, hireDate, address1, city, state, country, employmentHistoryStatus, exempt, payType, payRate, payPer, location, department, and division.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employees.create_new_employee(
    company_domain="companyDomain_example",
    first_name="Panda",
    last_name="Bear",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostNewEmployee`](./bamboo_hr_python_sdk/type/post_new_employee.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employees.get_directory`<a id="bamboohremployeesget_directory"></a>

Gets employee directory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_directory_response = bamboohr.employees.get_directory(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetDirectoryResponse`](./bamboo_hr_python_sdk/pydantic/employees_get_directory_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/directory` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employees.get_employee_data`<a id="bamboohremployeesget_employee_data"></a>

Get employee data by specifying a set of fields. This is suitable for getting basic employee information, including current values for fields that are part of a historical table, like job title, or compensation information. See the [fields](ref:metadata-get-a-list-of-fields) endpoint for a list of possible fields.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_data_response = bamboohr.employees.get_employee_data(
    company_domain="companyDomain_example",
    fields="firstName,lastName",
    id="0",
    only_current=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### fields: `str`<a id="fields-str"></a>

{fields} is a comma separated list of values taken from the official list of field names. 

##### id: `str`<a id="id-str"></a>

{id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).

##### only_current: `bool`<a id="only_current-bool"></a>

Setting to false will return future dated values from history table fields.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetEmployeeDataResponse`](./bamboo_hr_python_sdk/pydantic/employees_get_employee_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.employees.update_employee`<a id="bamboohremployeesupdate_employee"></a>

Update an employee, based on employee ID. If employee is currently on a pay schedule syncing with Trax Payroll, or being added to one, the API user will need to update the employee with all of the following required fields for the update to be successful (listed by API field name): employeeNumber, firstName, lastName, dateOfBirth, ssn, gender, maritalStatus, hireDate, address1, city, state, country, employmentHistoryStatus, exempt, payType, payRate, payPer, location, department, and division.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.employees.update_employee(
    company_domain="companyDomain_example",
    id="id_example",
    first_name="Panda",
    last_name="Bear",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an employee ID.

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Employee`](./bamboo_hr_python_sdk/type/employee.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.close_goal`<a id="bamboohrgoalsclose_goal"></a>

Close a goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
close_goal_response = bamboohr.goals.close_goal(
    body="string_example",
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### requestBody: `str`<a id="requestbody-str"></a>

Comment field is optional.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsCloseGoalResponse`](./bamboo_hr_python_sdk/pydantic/goals_close_goal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/close` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.count_per_status`<a id="bamboohrgoalscount_per_status"></a>

Get the number of goals per status for an employee. Difference from Version 1: Returns goals in the closed filter and provides filter actions for each filter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
count_per_status_response = bamboohr.goals.count_per_status(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID to whom the goals are assigned.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsCountPerStatusResponse`](./bamboo_hr_python_sdk/pydantic/goals_count_per_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/performance/employees/{employeeId}/goals/filters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.create_comment`<a id="bamboohrgoalscreate_comment"></a>

Create a new goal comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.create_comment(
    body="body_example",
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.create_employee_goal`<a id="bamboohrgoalscreate_employee_goal"></a>

Create a new goal for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employee_goal_response = bamboohr.goals.create_employee_goal(
    title="string_example",
    shared_with_employee_ids=[
        1
    ],
    due_date="string_example",
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    description="string_example",
    percent_complete=1,
    aligns_with_option_id="string_example",
    completion_date=3.14,
    milestones=[
        {
            "title": "title_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

[Required] The goal title.

##### shared_with_employee_ids: [`NewGoalSharedWithEmployeeIds`](./bamboo_hr_python_sdk/type/new_goal_shared_with_employee_ids.py)<a id="shared_with_employee_ids-newgoalsharedwithemployeeidsbamboo_hr_python_sdktypenew_goal_shared_with_employee_idspy"></a>

##### due_date: `str`<a id="due_date-str"></a>

[Required] The goal due date in YYYY-mm-dd format.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### description: `str`<a id="description-str"></a>

[Optional] The goal description.

##### percent_complete: `int`<a id="percent_complete-int"></a>

[Optional] The goal completion percentage (0 - 100). If completionDate is set, this value must be 100.

##### aligns_with_option_id: `str`<a id="aligns_with_option_id-str"></a>

[Optional] The option ID that aligns with this goal.

##### completion_date: `Union[int, float]`<a id="completion_date-unionint-float"></a>

[Optional] The date the goal was completed. If date is set, and no milestones are contained within this goal, percentComplete must be set to 100. If this goal does contain milestones, completion date cannot be set.

##### milestones: List[`Milestone`]<a id="milestones-listmilestone"></a>

[Optional] Milestones for the goal.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewGoal`](./bamboo_hr_python_sdk/type/new_goal.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.delete_by_id`<a id="bamboohrgoalsdelete_by_id"></a>

Delete a goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.delete_by_id(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.delete_comment`<a id="bamboohrgoalsdelete_comment"></a>

Delete a goal comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.delete_comment(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
    comment_id="commentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### comment_id: `str`<a id="comment_id-str"></a>

commentId is the ID of a specific comment for the specified goal.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.determine_permission`<a id="bamboohrgoalsdetermine_permission"></a>

Determine if the API user has permission to create a goal for this employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.determine_permission(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/canCreateGoals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_alignable_options`<a id="bamboohrgoalsget_alignable_options"></a>

Get alignable goal options for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.get_alignable_options(
    body="string_example",
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID to get alignable goal options for.

##### requestBody: `str`<a id="requestbody-str"></a>

Get alignment options including the option currently aligned with this goal (if applicable). If omitted, response will be alignment options belonging to the API user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/alignmentOptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_all_aggregate_info`<a id="bamboohrgoalsget_all_aggregate_info"></a>

Provides a list of all goals, type counts, goal comment counts, and employees shared with goals for the given employee. This version of the endpoint will not return any goals with milestones. Milestone functionality for this endpoint begins in version 1.2.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_aggregate_info_response = bamboohr.goals.get_all_aggregate_info(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID used to generate the aggregate information.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetAllAggregateInfoResponse`](./bamboo_hr_python_sdk/pydantic/goals_get_all_aggregate_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/aggregate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_all_aggregate_info_0`<a id="bamboohrgoalsget_all_aggregate_info_0"></a>

Provides a list of all goals, type counts, filter actions, goal comment counts, and employees shared with goals for the given employee. Difference from Version 1: Returns goals in the closed filter and provides filter actions for each filter. This version of the endpoint will not return any goals with milestones. Milestone functionality for this endpoint begins in version 1.2.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_aggregate_info_0_response = bamboohr.goals.get_all_aggregate_info_0(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID used to generate the aggregate information.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetAllAggregateInfo200Response`](./bamboo_hr_python_sdk/pydantic/goals_get_all_aggregate_info200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/performance/employees/{employeeId}/goals/aggregate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_all_aggregate_info_1`<a id="bamboohrgoalsget_all_aggregate_info_1"></a>

Provides a list of all goals, type counts, filter actions, goal comment counts, and employees shared with goals for the given employee. Difference from Version 1.1: Returns all goals, including goals that contain milestones.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_aggregate_info_1_response = bamboohr.goals.get_all_aggregate_info_1(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID used to generate the aggregate information.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetAllAggregateInfo200Response1`](./bamboo_hr_python_sdk/pydantic/goals_get_all_aggregate_info200_response1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_2/performance/employees/{employeeId}/goals/aggregate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_comments`<a id="bamboohrgoalsget_comments"></a>

Get comments for a goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.get_comments(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_employee_goals`<a id="bamboohrgoalsget_employee_goals"></a>

Get goals for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_goals_response = bamboohr.goals.get_employee_goals(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    filter="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID to whom the goals are assigned.

##### filter: `str`<a id="filter-str"></a>

A filter that can be applied to only show the goals that are in a certain state.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetEmployeeGoalsResponse`](./bamboo_hr_python_sdk/pydantic/goals_get_employee_goals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.get_goal_aggregate_info`<a id="bamboohrgoalsget_goal_aggregate_info"></a>

Provides goal information, goal comments, and employees shared with goals or who have commented on the given goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_goal_aggregate_info_response = bamboohr.goals.get_goal_aggregate_info(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the Goal ID used to generate the aggregate information.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetGoalAggregateInfoResponse`](./bamboo_hr_python_sdk/pydantic/goals_get_goal_aggregate_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.reopen_goal`<a id="bamboohrgoalsreopen_goal"></a>

Reopen a goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reopen_goal_response = bamboohr.goals.reopen_goal(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/reopen` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.share_options_get`<a id="bamboohrgoalsshare_options_get"></a>

Provides a list of employees with whom the specified employee's goals may be shared.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.share_options_get(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    search="string_example",
    limit="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID to get sharing options for.

##### search: `str`<a id="search-str"></a>

The search term used to filter employees returned. Will search name, employee ID and email.

##### limit: `str`<a id="limit-str"></a>

Limit will restrict results to specified number.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/shareOptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.status_count`<a id="bamboohrgoalsstatus_count"></a>

Get the number of goals per status for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
status_count_response = bamboohr.goals.status_count(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID to whom the goals are assigned.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsStatusCountResponse`](./bamboo_hr_python_sdk/pydantic/goals_status_count_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/filters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.update_comment`<a id="bamboohrgoalsupdate_comment"></a>

Update a goal comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.goals.update_comment(
    body="body_example",
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
    comment_id="commentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### comment_id: `str`<a id="comment_id-str"></a>

commentId is the comment ID for the specified goal.

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.update_employee_goal`<a id="bamboohrgoalsupdate_employee_goal"></a>

Update a goal. This version will not update a goal to contain milestones, that functionality is added in version 1.1

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_goal_response = bamboohr.goals.update_employee_goal(
    title="string_example",
    id=1,
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
    description="string_example",
    percent_complete=1,
    aligns_with_option_id="string_example",
    shared_with_employee_ids=[
        1
    ],
    due_date="string_example",
    completion_date=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The goal title.

##### id: `int`<a id="id-int"></a>

A unique identifier for the record. Use this ID to reference this goal.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### description: `str`<a id="description-str"></a>

The goal description.

##### percent_complete: `int`<a id="percent_complete-int"></a>

The goal completion percentage (0 - 100).

##### aligns_with_option_id: `str`<a id="aligns_with_option_id-str"></a>

The option ID that aligns with this goal.

##### shared_with_employee_ids: [`GoalSharedWithEmployeeIds`](./bamboo_hr_python_sdk/type/goal_shared_with_employee_ids.py)<a id="shared_with_employee_ids-goalsharedwithemployeeidsbamboo_hr_python_sdktypegoal_shared_with_employee_idspy"></a>

##### due_date: `str`<a id="due_date-str"></a>

The goal due date in YYYY-mm-dd format.

##### completion_date: `Union[int, float]`<a id="completion_date-unionint-float"></a>

The date the goal was completed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Goal`](./bamboo_hr_python_sdk/type/goal.py)
Required fields: title, sharedWithEmployeeIds, dueDate. Any non-required field not provided will overwrite existing data with a NULL value.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.update_employee_goal_v11`<a id="bamboohrgoalsupdate_employee_goal_v11"></a>

Update a goal. Version 1.1 allows the updating of the milestones contained within the goal, unlike Version 1.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_goal_v11_response = bamboohr.goals.update_employee_goal_v11(
    title="string_example",
    shared_with_employee_ids=[
        1
    ],
    due_date="string_example",
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
    description="string_example",
    aligns_with_option_id="string_example",
    milestones_enabled=True,
    deleted_milestone_ids=[
        1
    ],
    milestones=[
        {
            "title": "title_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

[Required] The goal title.

##### shared_with_employee_ids: [`UpdateGoalV11SharedWithEmployeeIds`](./bamboo_hr_python_sdk/type/update_goal_v11_shared_with_employee_ids.py)<a id="shared_with_employee_ids-updategoalv11sharedwithemployeeidsbamboo_hr_python_sdktypeupdate_goal_v11_shared_with_employee_idspy"></a>

##### due_date: `str`<a id="due_date-str"></a>

[Required] The goal due date in YYYY-mm-dd format.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### description: `str`<a id="description-str"></a>

[Optional] The goal description.

##### aligns_with_option_id: `str`<a id="aligns_with_option_id-str"></a>

[Optional] The option ID that aligns with this goal.

##### milestones_enabled: `bool`<a id="milestones_enabled-bool"></a>

[Optional] A flag indicating whether or not milestones are enabled for this goal. Setting this flag to false will delete all existing milestones for this goal.

##### deleted_milestone_ids: [`UpdateGoalV11DeletedMilestoneIds`](./bamboo_hr_python_sdk/type/update_goal_v11_deleted_milestone_ids.py)<a id="deleted_milestone_ids-updategoalv11deletedmilestoneidsbamboo_hr_python_sdktypeupdate_goal_v11_deleted_milestone_idspy"></a>

##### milestones: List[`Milestone`]<a id="milestones-listmilestone"></a>

[Optional] All milestones to be added to the goal with this update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateGoalV11`](./bamboo_hr_python_sdk/type/update_goal_v11.py)
Required fields: title, sharedWithEmployeeIds, dueDate. Any non-required field not provided will overwrite existing data with a NULL value.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/performance/employees/{employeeId}/goals/{goalId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.update_goal_sharing`<a id="bamboohrgoalsupdate_goal_sharing"></a>

Updates which employees this goal is shared with.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_goal_sharing_response = bamboohr.goals.update_goal_sharing(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    goal_id="goalId_example",
    shared_with_employee_ids=[
        1
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `str`<a id="goal_id-str"></a>

goalId is the goal ID for the specified employee.

##### shared_with_employee_ids: [`GoalsUpdateGoalSharingRequestSharedWithEmployeeIds`](./bamboo_hr_python_sdk/type/goals_update_goal_sharing_request_shared_with_employee_ids.py)<a id="shared_with_employee_ids-goalsupdategoalsharingrequestsharedwithemployeeidsbamboo_hr_python_sdktypegoals_update_goal_sharing_request_shared_with_employee_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsUpdateGoalSharingRequest`](./bamboo_hr_python_sdk/type/goals_update_goal_sharing_request.py)
Employee IDs of employees with whom the goal is shared. All goal owners are considered \"shared with\".

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsUpdateGoalSharingResponse`](./bamboo_hr_python_sdk/pydantic/goals_update_goal_sharing_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.goals.update_progress`<a id="bamboohrgoalsupdate_progress"></a>

Update Goal Progress

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_progress_response = bamboohr.goals.update_progress(
    body=1,
    company_domain="companyDomain_example",
    employee_id=1,
    goal_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `int`<a id="employee_id-int"></a>

employeeId is the employee ID with whom the goal is associated.

##### goal_id: `int`<a id="goal_id-int"></a>

goalId is the goal ID for the specified employee.

##### requestBody: `int`<a id="requestbody-int"></a>

Employee IDs of employees with whom the goal is shared. All goal owners are considered \"shared with\".

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsUpdateProgressResponse`](./bamboo_hr_python_sdk/pydantic/goals_update_progress_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/performance/employees/{employeeId}/goals/{goalId}/progress` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.hours.bulk_record_edit`<a id="bamboohrhoursbulk_record_edit"></a>

Bulk add/edit hour records

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.hours.bulk_record_edit(
    body=[
        {
            "time_tracking_id": "time_tracking_id_example",
            "employee_id": 1,
            "date_hours_worked": "date_hours_worked_example",
            "rate_type": "rate_type_example",
            "hours_worked": 3.14,
        }
    ],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### requestBody: [`TimeTrackingRecordBulk`](./bamboo_hr_python_sdk/type/time_tracking_record_bulk.py)<a id="requestbody-timetrackingrecordbulkbamboo_hr_python_sdktypetime_tracking_record_bulkpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/timetracking/record` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.hours.delete_hour_record`<a id="bamboohrhoursdelete_hour_record"></a>

Delete an hour record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.hours.delete_hour_record(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

The time tracking id is the id that was used to track the record up to 36 characters in length. (i.e. UUID).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/timetracking/delete/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.hours.edit_hour_record`<a id="bamboohrhoursedit_hour_record"></a>

Edit an hour record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.hours.edit_hour_record(
    time_tracking_id="string_example",
    hours_worked=3.14,
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_tracking_id: `str`<a id="time_tracking_id-str"></a>

The time tracking id is the id that was used to track the record up to 36 characters in length. (i.e. UUID).

##### hours_worked: `Union[int, float]`<a id="hours_worked-unionint-float"></a>

The updated number of hours worked. e.g. if Employee A worked 8.0 hours originally and decided they only worked 6.0, please send 6.0 here not -2.0.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HoursEditHourRecordRequest`](./bamboo_hr_python_sdk/type/hours_edit_hour_record_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/timetracking/adjust` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.hours.get_hour_record`<a id="bamboohrhoursget_hour_record"></a>

Get an hour record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.hours.get_hour_record(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the time tracking ID used to originally create the record.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/timetracking/record/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.hours.record_addition`<a id="bamboohrhoursrecord_addition"></a>

Add an hour record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.hours.record_addition(
    time_tracking_id="string_example",
    employee_id=1,
    date_hours_worked="string_example",
    rate_type="string_example",
    hours_worked=3.14,
    company_domain="companyDomain_example",
    division_id=1,
    department_id=1,
    job_title_id=1,
    pay_code="string_example",
    pay_rate=3.14,
    job_code=1,
    job_data="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_tracking_id: `str`<a id="time_tracking_id-str"></a>

A unique identifier for the record. Use this ID to adjust or delete these hours. It can be any ID you use to track the record up to 36 characters in length. (i.e. UUID).

##### employee_id: `int`<a id="employee_id-int"></a>

The ID of the employee.

##### date_hours_worked: `str`<a id="date_hours_worked-str"></a>

The date the hours were worked. Please use the ISO-8601 date format YYYY-MM-DD.

##### rate_type: `str`<a id="rate_type-str"></a>

The type of hours - regular or overtime. Please use either \\\"REG\\\" or \\\"OT\\\" here.

##### hours_worked: `Union[int, float]`<a id="hours_worked-unionint-float"></a>

The number of hours worked.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### division_id: `int`<a id="division_id-int"></a>

[Optional] The ID of the division for the employee.

##### department_id: `int`<a id="department_id-int"></a>

[Optional] The ID of the department for the employee.

##### job_title_id: `int`<a id="job_title_id-int"></a>

[Optional] The ID of the job title for the employee.

##### pay_code: `str`<a id="pay_code-str"></a>

[Optional] Only necessary if the payroll provider requires a pay code

##### pay_rate: `Union[int, float]`<a id="pay_rate-unionint-float"></a>

[Optional] The rate of pay. e.g. $15.00/hour should use 15.00 here. Only necessary if the payroll provider requires a pay rate.

##### job_code: `int`<a id="job_code-int"></a>

[Optional] A job code.

##### job_data: `str`<a id="job_data-str"></a>

[Optional] A list of up to four 20 characters max job numbers in comma delimited format with no spaces.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingRecord`](./bamboo_hr_python_sdk/type/time_tracking_record.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/timetracking/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.last_change_information.get_changed_employee_ids`<a id="bamboohrlast_change_informationget_changed_employee_ids"></a>

This API allows for efficient syncing of employee data. When you use this API you will provide a timestamp and the results will be limited to just the employees that have changed since the time you provided. This API operates on an employee-last-changed-timestamp, which means that a change in ANY individual field in the employee record, as well as any change to the employment status, job info, or compensation tables, will cause that employee to be returned via this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.last_change_information.get_changed_employee_ids(
    company_domain="companyDomain_example",
    since="since_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### since: `str`<a id="since-str"></a>

URL encoded iso8601 timestamp

##### type: `str`<a id="type-str"></a>

Use one of these in the {type} variable in the URL: \"inserted\", \"updated\", \"deleted\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/changed` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.login.user_credentials`<a id="bamboohrloginuser_credentials"></a>

User Login

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.login.user_credentials(
    company_domain="companyDomain_example",
    application_key="string_example",
    user="string_example",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### application_key: `str`<a id="application_key-str"></a>

##### user: `str`<a id="user-str"></a>

##### password: `str`<a id="password-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Login`](./bamboo_hr_python_sdk/type/login.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/login` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.add_employee_direct_deposit_info`<a id="bamboohrpayrolladd_employee_direct_deposit_info"></a>

Add an employee's direct deposit information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.add_employee_direct_deposit_info(
    company_domain="companyDomain_example",
    id="id_example",
    accounts=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee id.

##### accounts: [`EmployeeDepositAccounts`](./bamboo_hr_python_sdk/type/employee_deposit_accounts.py)<a id="accounts-employeedepositaccountsbamboo_hr_python_sdktypeemployee_deposit_accountspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDeposit`](./bamboo_hr_python_sdk/type/employee_deposit.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_direct_deposit_accounts/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.add_employee_paystub`<a id="bamboohrpayrolladd_employee_paystub"></a>

Add an employee's paystub

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.add_employee_paystub(
    company_domain="companyDomain_example",
    employee_id="string_example",
    external_record_id="string_example",
    pay_period_from="string_example",
    pay_period_to="string_example",
    pay_date="string_example",
    payor_name="string_example",
    payor_add1="string_example",
    payor_add2="string_example",
    payor_city="string_example",
    payor_state="string_example",
    payor_zip="string_example",
    payee_name="string_example",
    currency_code="string_example",
    net="string_example",
    gross="string_example",
    total_taxes="string_example",
    total_deductions="string_example",
    ytd_net="string_example",
    ytd_gross="string_example",
    ytd_taxes="string_example",
    ytd_deductions="string_example",
    fed_witholding="string_example",
    federal_type="2020_w4",
    two_jobs="string_example",
    dependents_amount="string_example",
    other_income="string_example",
    deductions_amount="string_example",
    state_withholding="string_example",
    local_withholding="string_example",
    additional_fed="string_example",
    additional_state="string_example",
    additional_local="string_example",
    tax_state="string_example",
    tax_local="string_example",
    wages=[
        {
        }
    ],
    taxes=[
        {
        }
    ],
    deductions=[
        {
        }
    ],
    deposits=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

##### external_record_id: `str`<a id="external_record_id-str"></a>

##### pay_period_from: `str`<a id="pay_period_from-str"></a>

##### pay_period_to: `str`<a id="pay_period_to-str"></a>

##### pay_date: `str`<a id="pay_date-str"></a>

##### payor_name: `str`<a id="payor_name-str"></a>

##### payor_add1: `str`<a id="payor_add1-str"></a>

##### payor_add2: `str`<a id="payor_add2-str"></a>

##### payor_city: `str`<a id="payor_city-str"></a>

##### payor_state: `str`<a id="payor_state-str"></a>

##### payor_zip: `str`<a id="payor_zip-str"></a>

##### payee_name: `str`<a id="payee_name-str"></a>

##### currency_code: `str`<a id="currency_code-str"></a>

##### net: `str`<a id="net-str"></a>

##### gross: `str`<a id="gross-str"></a>

##### total_taxes: `str`<a id="total_taxes-str"></a>

##### total_deductions: `str`<a id="total_deductions-str"></a>

##### ytd_net: `str`<a id="ytd_net-str"></a>

##### ytd_gross: `str`<a id="ytd_gross-str"></a>

##### ytd_taxes: `str`<a id="ytd_taxes-str"></a>

##### ytd_deductions: `str`<a id="ytd_deductions-str"></a>

##### fed_witholding: `str`<a id="fed_witholding-str"></a>

##### federal_type: `str`<a id="federal_type-str"></a>

must be 2020_w4, pre_2020_w4, or null

##### two_jobs: `str`<a id="two_jobs-str"></a>

boolean value

##### dependents_amount: `str`<a id="dependents_amount-str"></a>

float value

##### other_income: `str`<a id="other_income-str"></a>

float value

##### deductions_amount: `str`<a id="deductions_amount-str"></a>

float value

##### state_withholding: `str`<a id="state_withholding-str"></a>

##### local_withholding: `str`<a id="local_withholding-str"></a>

##### additional_fed: `str`<a id="additional_fed-str"></a>

##### additional_state: `str`<a id="additional_state-str"></a>

##### additional_local: `str`<a id="additional_local-str"></a>

##### tax_state: `str`<a id="tax_state-str"></a>

##### tax_local: `str`<a id="tax_local-str"></a>

##### wages: [`EmployeePaystubWages`](./bamboo_hr_python_sdk/type/employee_paystub_wages.py)<a id="wages-employeepaystubwagesbamboo_hr_python_sdktypeemployee_paystub_wagespy"></a>

##### taxes: [`EmployeePaystubTaxes`](./bamboo_hr_python_sdk/type/employee_paystub_taxes.py)<a id="taxes-employeepaystubtaxesbamboo_hr_python_sdktypeemployee_paystub_taxespy"></a>

##### deductions: [`EmployeePaystubDeductions`](./bamboo_hr_python_sdk/type/employee_paystub_deductions.py)<a id="deductions-employeepaystubdeductionsbamboo_hr_python_sdktypeemployee_paystub_deductionspy"></a>

##### deposits: [`EmployeePaystubDeposits`](./bamboo_hr_python_sdk/type/employee_paystub_deposits.py)<a id="deposits-employeepaystubdepositsbamboo_hr_python_sdktypeemployee_paystub_depositspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePaystub`](./bamboo_hr_python_sdk/type/employee_paystub.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_pay_stub` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.add_employee_unpaid_paystubs`<a id="bamboohrpayrolladd_employee_unpaid_paystubs"></a>

Add an employee's unpaid paystubs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.add_employee_unpaid_paystubs(
    company_domain="companyDomain_example",
    employee_id="string_example",
    unpaid_periods=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

##### unpaid_periods: [`EmployeeUnpaidPaystubUnpaidPeriods`](./bamboo_hr_python_sdk/type/employee_unpaid_paystub_unpaid_periods.py)<a id="unpaid_periods-employeeunpaidpaystubunpaidperiodsbamboo_hr_python_sdktypeemployee_unpaid_paystub_unpaid_periodspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeUnpaidPaystub`](./bamboo_hr_python_sdk/type/employee_unpaid_paystub.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_unpaid_pay_stubs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.add_employee_withholdings`<a id="bamboohrpayrolladd_employee_withholdings"></a>

Add an employee's default withholdings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.add_employee_withholdings(
    company_domain="companyDomain_example",
    id="id_example",
    fed_withholding="string_example",
    state_withholding="string_example",
    local_withholding="string_example",
    additional_fed="string_example",
    additional_state="string_example",
    additional_local="string_example",
    tax_state="string_example",
    tax_local="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee id.

##### fed_withholding: `str`<a id="fed_withholding-str"></a>

##### state_withholding: `str`<a id="state_withholding-str"></a>

##### local_withholding: `str`<a id="local_withholding-str"></a>

##### additional_fed: `str`<a id="additional_fed-str"></a>

##### additional_state: `str`<a id="additional_state-str"></a>

##### additional_local: `str`<a id="additional_local-str"></a>

##### tax_state: `str`<a id="tax_state-str"></a>

##### tax_local: `str`<a id="tax_local-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeWithholding`](./bamboo_hr_python_sdk/type/employee_withholding.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_withholding/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.clear_employee_direct_deposit`<a id="bamboohrpayrollclear_employee_direct_deposit"></a>

Clear an employee's direct deposit information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.clear_employee_direct_deposit(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_direct_deposit_accounts/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.clear_employee_unpaid_paystubs`<a id="bamboohrpayrollclear_employee_unpaid_paystubs"></a>

Clear an employee's unpaid paystubs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.clear_employee_unpaid_paystubs(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee id.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_unpaid_pay_stubs/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.clear_employee_withholdings`<a id="bamboohrpayrollclear_employee_withholdings"></a>

Clear an employee's default withholdings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.clear_employee_withholdings(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee id.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_withholding/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.delete_employee_paystub`<a id="bamboohrpayrolldelete_employee_paystub"></a>

Delete an employee's paystub

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.delete_employee_paystub(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the paystub (record) ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_pay_stub/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.employee_direct_deposit_info`<a id="bamboohrpayrollemployee_direct_deposit_info"></a>

Get an employee's direct deposit information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.employee_direct_deposit_info(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_direct_deposit_accounts/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.get_default_withholdings`<a id="bamboohrpayrollget_default_withholdings"></a>

Get an employee's default withholdings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.get_default_withholdings(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_withholding/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.get_paystub`<a id="bamboohrpayrollget_paystub"></a>

Get an employee's paystub

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.get_paystub(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the paystub (record) ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_pay_stub/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.payroll.get_unpaid_paystubs`<a id="bamboohrpayrollget_unpaid_paystubs"></a>

Get an employee's unpaid paystubs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.payroll.get_unpaid_paystubs(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employee_unpaid_pay_stubs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.photos.get_employee_photo`<a id="bamboohrphotosget_employee_photo"></a>

Get an employee photo

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.photos.get_employee_photo(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    size="original",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

The ID for the employee you are getting the photo for.

##### size: `str`<a id="size-str"></a>

Photo size

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/photo/{size}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.photos.store_new_employee_photo`<a id="bamboohrphotosstore_new_employee_photo"></a>

Store a new employee photo

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.photos.store_new_employee_photo(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

The ID for the employee you are setting the photo for.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/photo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.reports.company_report`<a id="bamboohrreportscompany_report"></a>

Use this resource to request one of your existing custom company reports from the My Reports or Manage Reports sections in the Reports tab. You can get the report number by hovering over the report name and noting the ID from the URL. At present, only reports from the My Reports or Manage Reports sections are supported. In the future we may implement reports from the Standard Reports section if there is enough demand for it. The report numbers used in this request are different in each company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.reports.company_report(
    company_domain="companyDomain_example",
    id="id_example",
    format="format_example",
    fd="string_example",
    only_current=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is a report ID.

##### format: `str`<a id="format-str"></a>

The output format for the report. Supported formats: CSV, PDF, XLS, XML, JSON

##### fd: `str`<a id="fd-str"></a>

yes=apply standard duplicate field filtering, no=return the raw results with no duplicate filtering. Default value is \"yes\"

##### only_current: `bool`<a id="only_current-bool"></a>

Setting to false will return future dated values from history table fields.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/reports/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.reports.request_custom_report`<a id="bamboohrreportsrequest_custom_report"></a>

Use this resource to request BambooHR generate a report. You must specify a type of either "PDF", "XLS", "CSV", "JSON", or "XML". You must specify a list of fields to show on the report. The list of fields is available here. The custom report will return employees regardless of their status, "Active" or "Inactive". This differs from the UI, which by default applies a quick filter to display only "Active" employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.reports.request_custom_report(
    company_domain="companyDomain_example",
    format="format_example",
    title="string_example",
    filters={
    },
    fields=[
        "string_example"
    ],
    only_current=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### format: `str`<a id="format-str"></a>

The output format for the report. Supported formats: CSV, PDF, XLS, XML, JSON

##### title: `str`<a id="title-str"></a>

##### filters: [`RequestCustomReportFilters`](./bamboo_hr_python_sdk/type/request_custom_report_filters.py)<a id="filters-requestcustomreportfiltersbamboo_hr_python_sdktyperequest_custom_report_filterspy"></a>


##### fields: [`RequestCustomReportFields`](./bamboo_hr_python_sdk/type/request_custom_report_fields.py)<a id="fields-requestcustomreportfieldsbamboo_hr_python_sdktyperequest_custom_report_fieldspy"></a>

##### only_current: `bool`<a id="only_current-bool"></a>

Limits the report to only current employees. Setting to false will include future-dated employees in the report.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RequestCustomReport`](./bamboo_hr_python_sdk/type/request_custom_report.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/reports/custom` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.add_row`<a id="bamboohrtabular_dataadd_row"></a>

Adds a table row. Fundamentally the same as version 1 so choose a version and stay with it unless other changes occur. Changes from version 1 are now minor with a few variations limited to ACA, payroll, terminated rehire, gusto, benetrac, and final pay date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.tabular_data.add_row(
    company_domain="companyDomain_example",
    id="id_example",
    table="table_example",
    date="string_example",
    location="string_example",
    division="string_example",
    department="string_example",
    job_title="string_example",
    reports_to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

##### table: `str`<a id="table-str"></a>

Table name

##### date: `str`<a id="date-str"></a>

##### location: `str`<a id="location-str"></a>

##### division: `str`<a id="division-str"></a>

##### department: `str`<a id="department-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### reports_to: `str`<a id="reports_to-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableRowUpdate`](./bamboo_hr_python_sdk/type/table_row_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/employees/{id}/tables/{table}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.add_table_row`<a id="bamboohrtabular_dataadd_table_row"></a>

Adds a table row. If employee is currently on a pay schedule syncing with Trax Payroll, or being added to one, the row cannot be added if they are missing any required fields for that table. If the API user is adding a row on the compensation table, the row cannot be added if they are missing any of the required employee fields (including fields not on that table).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.tabular_data.add_table_row(
    company_domain="companyDomain_example",
    id="id_example",
    table="table_example",
    date="string_example",
    location="string_example",
    division="string_example",
    department="string_example",
    job_title="string_example",
    reports_to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

##### table: `str`<a id="table-str"></a>

Table name

##### date: `str`<a id="date-str"></a>

##### location: `str`<a id="location-str"></a>

##### division: `str`<a id="division-str"></a>

##### department: `str`<a id="department-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### reports_to: `str`<a id="reports_to-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableRowUpdate`](./bamboo_hr_python_sdk/type/table_row_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/tables/{table}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.delete_row`<a id="bamboohrtabular_datadelete_row"></a>

Deletes a table row

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_row_response = bamboohr.tabular_data.delete_row(
    company_domain="companyDomain_example",
    id="id_example",
    table="table_example",
    row_id="rowId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

##### table: `str`<a id="table-str"></a>

Table name

##### row_id: `str`<a id="row_id-str"></a>

Row ID

#### 🔄 Return<a id="🔄-return"></a>

[`TabularDataDeleteRowResponse`](./bamboo_hr_python_sdk/pydantic/tabular_data_delete_row_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/tables/{table}/{rowId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.get_changed_table_rows`<a id="bamboohrtabular_dataget_changed_table_rows"></a>

This API is merely an optimization to avoid downloading all table data for all employees. When you use this API you will provide a timestamp and the results will be limited to just the employees that have changed since the time you provided. This API operates on an employee-last-changed-timestamp, which means that a change in ANY field in the employee record will cause ALL of that employees table rows to show up via this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.tabular_data.get_changed_table_rows(
    company_domain="companyDomain_example",
    table="table_example",
    since="since_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### table: `str`<a id="table-str"></a>

Table name

##### since: `str`<a id="since-str"></a>

URL encoded iso8601 timestamp

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/changed/tables/{table}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.get_employee_table_rows`<a id="bamboohrtabular_dataget_employee_table_rows"></a>

Returns a data structure representing all the table rows for a given employee and table combination. The result is not sorted in any particular order.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.tabular_data.get_employee_table_rows(
    company_domain="companyDomain_example",
    id="id_example",
    table="table_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

##### table: `str`<a id="table-str"></a>

Table name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/tables/{table}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.update_row`<a id="bamboohrtabular_dataupdate_row"></a>

Updates a table row. If employee is currently on a pay schedule syncing with Trax Payroll, or being added to one, the row cannot be added if they are missing any required fields for that table. If the API user is updating a row on the compensation table, the row cannot be updated if they are missing any of the required employee fields (including fields not on that table).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.tabular_data.update_row(
    company_domain="companyDomain_example",
    id="id_example",
    table="table_example",
    row_id="rowId_example",
    date="string_example",
    location="string_example",
    division="string_example",
    department="string_example",
    job_title="string_example",
    reports_to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

##### table: `str`<a id="table-str"></a>

Table name

##### row_id: `str`<a id="row_id-str"></a>

Row ID

##### date: `str`<a id="date-str"></a>

##### location: `str`<a id="location-str"></a>

##### division: `str`<a id="division-str"></a>

##### department: `str`<a id="department-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### reports_to: `str`<a id="reports_to-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableRowUpdate`](./bamboo_hr_python_sdk/type/table_row_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{id}/tables/{table}/{rowId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.tabular_data.update_row_0`<a id="bamboohrtabular_dataupdate_row_0"></a>

Updates a table row. Fundamentally the same as version 1 so choose a version and stay with it unless other changes occur. Changes from version 1 are now minor with a few variations limited to ACA, payroll, terminated rehire, gusto, benetrac, and final pay date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.tabular_data.update_row_0(
    company_domain="companyDomain_example",
    id="id_example",
    table="table_example",
    row_id="rowId_example",
    date="string_example",
    location="string_example",
    division="string_example",
    department="string_example",
    job_title="string_example",
    reports_to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is the employee ID.

##### table: `str`<a id="table-str"></a>

Table name

##### row_id: `str`<a id="row_id-str"></a>

Row ID

##### date: `str`<a id="date-str"></a>

##### location: `str`<a id="location-str"></a>

##### division: `str`<a id="division-str"></a>

##### department: `str`<a id="department-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### reports_to: `str`<a id="reports_to-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableRowUpdate`](./bamboo_hr_python_sdk/type/table_row_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/employees/{id}/tables/{table}/{rowId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.add_time_off_history_item`<a id="bamboohrtime_offadd_time_off_history_item"></a>

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A new time off history item will be inserted into the database. On success, a 201 Created code is returned and the "Location" header of the response will contain a URL that identifies the new history item.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.add_time_off_history_item(
    date="string_example",
    time_off_request_id=1,
    company_domain="companyDomain_example",
    employee_id=1,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `str`<a id="date-str"></a>

The date the request should be added in history. This will usually be the first date of the request. Should be in ISO8601 date format (YYYY-MM-DD).

##### time_off_request_id: `int`<a id="time_off_request_id-int"></a>

The ID of the time off request.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `int`<a id="employee_id-int"></a>

The ID of the employee.

##### note: `str`<a id="note-str"></a>

This is an optional note to show in history.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffHistory`](./bamboo_hr_python_sdk/type/time_off_history.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/time_off/history` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.assign_employee_policies`<a id="bamboohrtime_offassign_employee_policies"></a>

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A time off policy will be assigned to the employee with accruals starting on the date specified. A null start date will remove the assignment. On success, a 200 Success code is returned and the content of the response will be the same as the List Time off Policies API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.assign_employee_policies(
    body=[
        {
        }
    ],
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

##### requestBody: [`TimeOffPolicies`](./bamboo_hr_python_sdk/type/time_off_policies.py)<a id="requestbody-timeoffpoliciesbamboo_hr_python_sdktypetime_off_policiespy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/time_off/policies` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.assign_employee_policies_v11`<a id="bamboohrtime_offassign_employee_policies_v11"></a>

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A time off policy will be assigned to the employee with accruals starting on the date specified. On success, a 200 Success code is returned and the content of the response will be the same as the List Time off Policies API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.assign_employee_policies_v11(
    body=[
        {
        }
    ],
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

##### requestBody: [`TimeOffPolicies`](./bamboo_hr_python_sdk/type/time_off_policies.py)<a id="requestbody-timeoffpoliciesbamboo_hr_python_sdktypetime_off_policiespy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/employees/{employeeId}/time_off/policies` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.balance_adjustment_put`<a id="bamboohrtime_offbalance_adjustment_put"></a>

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A time off balance adjustment will be inserted into the database. On success, a 201 Created code is returned and the "Location" header of the response will contain a URL that identifies the new history item.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.balance_adjustment_put(
    date="string_example",
    time_off_type_id=1,
    amount=3.14,
    company_domain="companyDomain_example",
    employee_id=1,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `str`<a id="date-str"></a>

The date the adjustment should be added in history. Should be in ISO8601 date format (YYYY-MM-DD).

##### time_off_type_id: `int`<a id="time_off_type_id-int"></a>

The ID of the time off type to add a balance adjustment for.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The number of hours/days to adjust the balance by.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `int`<a id="employee_id-int"></a>

The ID of the employee.

##### note: `str`<a id="note-str"></a>

This is an optional note to show in history.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AdjustTimeOffBalance`](./bamboo_hr_python_sdk/type/adjust_time_off_balance.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/time_off/balance_adjustment` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.change_request_status`<a id="bamboohrtime_offchange_request_status"></a>

This endpoint allows you to change the status of a request in the system. You can use this to approve, deny, or cancel a time off request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.change_request_status(
    company_domain="companyDomain_example",
    request_id="requestId_example",
    status="Approved",
    note="Note!",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### request_id: `str`<a id="request_id-str"></a>

##### status: `str`<a id="status-str"></a>

One of approved, cancelled, denied

##### note: `str`<a id="note-str"></a>

A note to attach to the change in status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Request`](./bamboo_hr_python_sdk/type/request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_off/requests/{requestId}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.estimate_future_time_off_balances`<a id="bamboohrtime_offestimate_future_time_off_balances"></a>

This endpoint will sum future time off accruals, scheduled time off, and carry-over events to produce estimates for the anticipated time off balance on a given date in the future.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.estimate_future_time_off_balances(
    company_domain="companyDomain_example",
    end="1970-01-01T00:00:00.00Z",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### end: `datetime`<a id="end-datetime"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/time_off/calculator` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.get_policies`<a id="bamboohrtime_offget_policies"></a>

This endpoint gets a list of time off policies.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.get_policies(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/time_off/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.get_time_off_requests`<a id="bamboohrtime_offget_time_off_requests"></a>

Get Time Off Requests

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.get_time_off_requests(
    company_domain="companyDomain_example",
    start="start_example",
    end="end_example",
    id=1,
    action="string_example",
    employee_id="string_example",
    type="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### start: `str`<a id="start-str"></a>

YYYY-MM-DD. Only show time off that occurs on/after the specified start date.

##### end: `str`<a id="end-str"></a>

YYYY-MM-DD. Only show time off that occurs on/before the specified end date.

##### id: `int`<a id="id-int"></a>

A particular request ID to limit the response to.

##### action: `str`<a id="action-str"></a>

Limit to requests that the user has a particular level of access to. Legal values are: \"view\" or \"approve\". Defaults to view.

##### employee_id: `str`<a id="employee_id-str"></a>

A particular employee ID to limit the response to.

##### type: `str`<a id="type-str"></a>

A comma separated list of time off types IDs to include limit the response to. If omitted, requests of all types are included.

##### status: `str`<a id="status-str"></a>

A comma separated list of request status values to include. If omitted, requests of all status values are included. Legal values are \"approved\", \"denied\", \"superceded\", \"requested\", \"canceled\".

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_off/requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.get_time_off_types`<a id="bamboohrtime_offget_time_off_types"></a>

This endpoint gets a list of time off types.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.get_time_off_types(
    company_domain="companyDomain_example",
    mode="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### mode: `str`<a id="mode-str"></a>

set to 'request' to get a list of all time off types with which this user can create a time off request. The default is to return the list of time off types the user has permissions on. This distinction is important, as employees can request time off for types that they don't have permission to view balances and requests for.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/meta/time_off/types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.get_whos_out_list`<a id="bamboohrtime_offget_whos_out_list"></a>

This endpoint will return a list, sorted by date, of employees who will be out, and company holidays, for a period of time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.get_whos_out_list(
    company_domain="companyDomain_example",
    start="string_example",
    end="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### start: `str`<a id="start-str"></a>

A date in the form YYYY-MM-DD - defaults to the current date.

##### end: `str`<a id="end-str"></a>

A date in the form YYYY-MM-DD - defaults to 14 days from the start date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_off/whos_out` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.list_employee_policies`<a id="bamboohrtime_offlist_employee_policies"></a>

List Time Off Policies for Employee, Version 1.1

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.list_employee_policies(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1_1/employees/{employeeId}/time_off/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.list_employee_time_off_policies`<a id="bamboohrtime_offlist_employee_time_off_policies"></a>

List Time Off Policies for Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.list_employee_time_off_policies(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/time_off/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_off.request_creation`<a id="bamboohrtime_offrequest_creation"></a>

A time off request is an entity that describes the decision making process for approving time off. Once a request has been created, a history entry can be created documenting the actual use of time off.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_off.request_creation(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    status="string_example",
    start="string_example",
    end="string_example",
    time_off_type_id=1,
    amount=1,
    notes=[
        {
        }
    ],
    dates=[
        {
        }
    ],
    previous_request=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

##### status: `str`<a id="status-str"></a>

##### start: `str`<a id="start-str"></a>

##### end: `str`<a id="end-str"></a>

##### time_off_type_id: `int`<a id="time_off_type_id-int"></a>

##### amount: `int`<a id="amount-int"></a>

##### notes: [`TimeOffRequestNotes`](./bamboo_hr_python_sdk/type/time_off_request_notes.py)<a id="notes-timeoffrequestnotesbamboo_hr_python_sdktypetime_off_request_notespy"></a>

##### dates: [`TimeOffRequestDates`](./bamboo_hr_python_sdk/type/time_off_request_dates.py)<a id="dates-timeoffrequestdatesbamboo_hr_python_sdktypetime_off_request_datespy"></a>

##### previous_request: `int`<a id="previous_request-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffRequest`](./bamboo_hr_python_sdk/type/time_off_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/employees/{employeeId}/time_off/request` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.approve_employee_timesheets`<a id="bamboohrtime_trackingapprove_employee_timesheets"></a>

Approve employee timesheets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.approve_employee_timesheets(
    last_changed=1624485787,
    timesheets=[
        {
            "timesheet_id": 100,
        }
    ],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_changed: `int`<a id="last_changed-int"></a>

UNIX timestamp for last change to timesheet

##### timesheets: [`TimeTrackingApproveEmployeeTimesheetsRequestTimesheets`](./bamboo_hr_python_sdk/type/time_tracking_approve_employee_timesheets_request_timesheets.py)<a id="timesheets-timetrackingapproveemployeetimesheetsrequesttimesheetsbamboo_hr_python_sdktypetime_tracking_approve_employee_timesheets_request_timesheetspy"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingApproveEmployeeTimesheetsRequest`](./bamboo_hr_python_sdk/type/time_tracking_approve_employee_timesheets_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/timesheets/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.approve_employee_timesheets_0`<a id="bamboohrtime_trackingapprove_employee_timesheets_0"></a>

Approve timesheets for employees that are currently clocked in

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.approve_employee_timesheets_0(
    company_domain="companyDomain_example",
    clock_outs=[
        {
            "timesheet_id": 100,
            "end": "1050",
            "date": "2021-04-23",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### clock_outs: [`TimeTrackingApproveEmployeeTimesheetsRequest1ClockOuts`](./bamboo_hr_python_sdk/type/time_tracking_approve_employee_timesheets_request1_clock_outs.py)<a id="clock_outs-timetrackingapproveemployeetimesheetsrequest1clockoutsbamboo_hr_python_sdktypetime_tracking_approve_employee_timesheets_request1_clock_outspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingApproveEmployeeTimesheetsRequest1`](./bamboo_hr_python_sdk/type/time_tracking_approve_employee_timesheets_request1.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/timesheets/clock_out_and_approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.clock_in_employee`<a id="bamboohrtime_trackingclock_in_employee"></a>

Clock in (employee id optional)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.clock_in_employee(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    start="780",
    timezone="America/Denver",
    note="Back from lunch.",
    project_id=3,
    task_id=2,
    clock_in_location={
        "latitude": 40.332729,
        "longitude": -111.729235,
        "accuracy": 2,
        "address": "123 Main",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

{employeeId} is id of the employee clocking out

##### start: `str`<a id="start-str"></a>

The start time for the clock in. In 24 hour format HH:MM

##### timezone: `str`<a id="timezone-str"></a>

The timezone associated with the clock in.

##### note: `str`<a id="note-str"></a>

The note associated with the clock in

##### project_id: `int`<a id="project_id-int"></a>

The id of the project associated with the clock in

##### task_id: `int`<a id="task_id-int"></a>

The id of the task associated with the clock in

##### clock_in_location: [`TimeTrackingClockInEmployeeRequestClockInLocation`](./bamboo_hr_python_sdk/type/time_tracking_clock_in_employee_request_clock_in_location.py)<a id="clock_in_location-timetrackingclockinemployeerequestclockinlocationbamboo_hr_python_sdktypetime_tracking_clock_in_employee_request_clock_in_locationpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingClockInEmployeeRequest`](./bamboo_hr_python_sdk/type/time_tracking_clock_in_employee_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/clock_in/{employeeId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.clock_out_employee`<a id="bamboohrtime_trackingclock_out_employee"></a>

Clock out (employee id optional)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.clock_out_employee(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    clock_out_location={
        "latitude": 40.332729,
        "longitude": -111.729235,
        "accuracy": 2,
        "address": "123 Main",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

{employeeId} is id of the employee clocking out

##### clock_out_location: [`TimeTrackingClockOutEmployeeRequestClockOutLocation`](./bamboo_hr_python_sdk/type/time_tracking_clock_out_employee_request_clock_out_location.py)<a id="clock_out_location-timetrackingclockoutemployeerequestclockoutlocationbamboo_hr_python_sdktypetime_tracking_clock_out_employee_request_clock_out_locationpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingClockOutEmployeeRequest`](./bamboo_hr_python_sdk/type/time_tracking_clock_out_employee_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/clock_out/{employeeId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.clock_out_employee_at_specific_time`<a id="bamboohrtime_trackingclock_out_employee_at_specific_time"></a>

Clock out an employee at a specific time

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.clock_out_employee_at_specific_time(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    datetime="2020-12-16T17:28:00-05:00",
    timezone="America/Denver",
    employee_id=40342,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to whom the projects belong.

##### requestBody: [`TimeTrackingClockOutEmployeeAtSpecificTimeRequest`](./bamboo_hr_python_sdk/type/time_tracking_clock_out_employee_at_specific_time_request.py)<a id="requestbody-timetrackingclockoutemployeeatspecifictimerequestbamboo_hr_python_sdktypetime_tracking_clock_out_employee_at_specific_time_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/clock_out/datetime` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.delete_clock_entries`<a id="bamboohrtime_trackingdelete_clock_entries"></a>

Delete clock entries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.delete_clock_entries(
    company_domain="companyDomain_example",
    clock_entry_ids=[10, 11, 12],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### clock_entry_ids: [`TimeTrackingDeleteClockEntriesRequestClockEntryIds`](./bamboo_hr_python_sdk/type/time_tracking_delete_clock_entries_request_clock_entry_ids.py)<a id="clock_entry_ids-timetrackingdeleteclockentriesrequestclockentryidsbamboo_hr_python_sdktypetime_tracking_delete_clock_entries_request_clock_entry_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingDeleteClockEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_delete_clock_entries_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/clock_entries` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.edit_clocked_in_entry_data`<a id="bamboohrtime_trackingedit_clocked_in_entry_data"></a>

Edit information on the currently clocked in entry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.edit_clocked_in_entry_data(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    start="780",
    timezone="America/Denver",
    note="Back from lunch.",
    project_id=3,
    task_id=2,
    clock_in_location={
        "latitude": 40.332729,
        "longitude": -111.729235,
        "accuracy": 2,
        "address": "123 Main",
    },
    clock_out_location={
        "latitude": 40.332729,
        "longitude": -111.729235,
        "accuracy": 2,
        "address": "123 Main",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to whom the projects belong.

##### start: `str`<a id="start-str"></a>

The start time for the clock in. In 24 hour format HH:MM

##### timezone: `str`<a id="timezone-str"></a>

The timezone associated with the clock in.

##### note: `str`<a id="note-str"></a>

The note associated with the clock in

##### project_id: `int`<a id="project_id-int"></a>

The id of the project associated with the clock in

##### task_id: `int`<a id="task_id-int"></a>

The id of the task associated with the clock in

##### clock_in_location: [`TimeTrackingEditClockedInEntryDataRequestClockInLocation`](./bamboo_hr_python_sdk/type/time_tracking_edit_clocked_in_entry_data_request_clock_in_location.py)<a id="clock_in_location-timetrackingeditclockedinentrydatarequestclockinlocationbamboo_hr_python_sdktypetime_tracking_edit_clocked_in_entry_data_request_clock_in_locationpy"></a>


##### clock_out_location: [`TimeTrackingEditClockedInEntryDataRequestClockOutLocation`](./bamboo_hr_python_sdk/type/time_tracking_edit_clocked_in_entry_data_request_clock_out_location.py)<a id="clock_out_location-timetrackingeditclockedinentrydatarequestclockoutlocationbamboo_hr_python_sdktypetime_tracking_edit_clocked_in_entry_data_request_clock_out_locationpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingEditClockedInEntryDataRequest`](./bamboo_hr_python_sdk/type/time_tracking_edit_clocked_in_entry_data_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/clock_in/data` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.employee_clocked_in`<a id="bamboohrtime_trackingemployee_clocked_in"></a>

Is employee clocked in?

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.employee_clocked_in(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of employee to whom the clock entry belongs.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/is_clocked_in` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.employee_timesheet_get`<a id="bamboohrtime_trackingemployee_timesheet_get"></a>

Get a timesheet for an employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.employee_timesheet_get(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    timesheet_id="timesheetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of employee to whom the timesheet belongs.

##### timesheet_id: `str`<a id="timesheet_id-str"></a>

timesheetId is the id to whom the timesheet belongs.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/timesheet/{timesheetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.get_clock_entry`<a id="bamboohrtime_trackingget_clock_entry"></a>

Get a clock entry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.get_clock_entry(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of employee to whom the clock entry belongs.

##### id: `str`<a id="id-str"></a>

the id to whom the clock entry belongs.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/clock_entries/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.get_daily_entry`<a id="bamboohrtime_trackingget_daily_entry"></a>

Get a daily entry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.get_daily_entry(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of employee to whom the daily entry belongs.

##### id: `str`<a id="id-str"></a>

the id to whom the daily entry belongs.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/daily_entries/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.get_project_tasks`<a id="bamboohrtime_trackingget_project_tasks"></a>

Get tasks for a project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.get_project_tasks(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to whom the projects belong.

##### project_id: `str`<a id="project_id-str"></a>

id of the project to which the tasks belong.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/projects/{projectId}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.get_timesheets_by_ids`<a id="bamboohrtime_trackingget_timesheets_by_ids"></a>

Get timesheets by ids

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.get_timesheets_by_ids(
    timesheets="10, 11, 12",
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: `str`<a id="timesheets-str"></a>

Comma separated list of timesheet ids

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingGetTimesheetsByIdsRequest`](./bamboo_hr_python_sdk/type/time_tracking_get_timesheets_by_ids_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/timesheets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.list_employee_projects`<a id="bamboohrtime_trackinglist_employee_projects"></a>

Get projects an employee can log time to

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.list_employee_projects(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to whom the projects belong.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employee/{employeeId}/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.store_clock_entries`<a id="bamboohrtime_trackingstore_clock_entries"></a>

Store clock entries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.store_clock_entries(
    company_domain="companyDomain_example",
    entries=[
        {
            "employee_id": 40342,
            "date": "2021-06-25",
            "start": "780",
            "end": "1020",
            "clock_entry_id": 101,
            "project_id": 1,
            "task_id": 2,
            "note": "Note for time entry",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### entries: [`TimeTrackingStoreClockEntriesRequestEntries`](./bamboo_hr_python_sdk/type/time_tracking_store_clock_entries_request_entries.py)<a id="entries-timetrackingstoreclockentriesrequestentriesbamboo_hr_python_sdktypetime_tracking_store_clock_entries_request_entriespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingStoreClockEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_store_clock_entries_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/clock_entries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking.store_daily_entries`<a id="bamboohrtime_trackingstore_daily_entries"></a>

Store daily entries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking.store_daily_entries(
    company_domain="companyDomain_example",
    entries=[
        {
            "employee_id": 40342,
            "date": "2021-06-25",
            "hours": 7.5,
            "daily_entry_id": 1,
            "project_id": 1,
            "task_id": 2,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### entries: [`TimeTrackingStoreDailyEntriesRequestEntries`](./bamboo_hr_python_sdk/type/time_tracking_store_daily_entries_request_entries.py)<a id="entries-timetrackingstoredailyentriesrequestentriesbamboo_hr_python_sdktypetime_tracking_store_daily_entries_request_entriespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingStoreDailyEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_store_daily_entries_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/daily_entries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.add_clock_out`<a id="bamboohrtime_tracking___private_betaadd_clock_out"></a>

Clock out an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_clock_out_response = bamboohr.time_tracking___private_beta.add_clock_out(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to clock out.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntry`](./bamboo_hr_python_sdk/pydantic/timesheet_entry.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employees/{employeeId}/clock_out` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.add_edit_clock_entries`<a id="bamboohrtime_tracking___private_betaadd_edit_clock_entries"></a>

Add or edit timesheet clock entries.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_edit_clock_entries_response = bamboohr.time_tracking___private_beta.add_edit_clock_entries(
    entries=[
        {
            "employee_id": 1,
            "date": "2024-01-31",
            "start": "09:00",
            "end": "1020",
        }
    ],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entries: [`TimeTrackingPrivateBetaAddEditClockEntriesRequestEntries`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_add_edit_clock_entries_request_entries.py)<a id="entries-timetrackingprivatebetaaddeditclockentriesrequestentriesbamboo_hr_python_sdktypetime_tracking_private_beta_add_edit_clock_entries_request_entriespy"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingPrivateBetaAddEditClockEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_add_edit_clock_entries_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingPrivateBetaAddEditClockEntriesResponse`](./bamboo_hr_python_sdk/pydantic/time_tracking_private_beta_add_edit_clock_entries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/clock_entries/store` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.add_edit_hour_entries`<a id="bamboohrtime_tracking___private_betaadd_edit_hour_entries"></a>

Add or edit timesheet hour entries.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_edit_hour_entries_response = bamboohr.time_tracking___private_beta.add_edit_hour_entries(
    hours=[
        {
            "employee_id": 1,
            "date": "2024-01-31",
            "hours": 3.5,
        }
    ],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hours: [`TimeTrackingPrivateBetaAddEditHourEntriesRequestHours`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_add_edit_hour_entries_request_hours.py)<a id="hours-timetrackingprivatebetaaddedithourentriesrequesthoursbamboo_hr_python_sdktypetime_tracking_private_beta_add_edit_hour_entries_request_hourspy"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingPrivateBetaAddEditHourEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_add_edit_hour_entries_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingPrivateBetaAddEditHourEntriesResponse`](./bamboo_hr_python_sdk/pydantic/time_tracking_private_beta_add_edit_hour_entries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/hour_entries/store` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.add_timesheet_clock_in`<a id="bamboohrtime_tracking___private_betaadd_timesheet_clock_in"></a>

Clock in an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_timesheet_clock_in_response = bamboohr.time_tracking___private_beta.add_timesheet_clock_in(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
    project_id=10,
    task_id=25,
    note="Back from lunch.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to clock in.

##### project_id: `int`<a id="project_id-int"></a>

id of the time tracking project that should be associated with the timesheet entry. Required if taskId is specified.

##### task_id: `int`<a id="task_id-int"></a>

id of the time tracking task that should be associated with the timesheet entry.

##### note: `str`<a id="note-str"></a>

The note that should be associated with the timesheet entry

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingPrivateBetaAddTimesheetClockInRequest`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_add_timesheet_clock_in_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetEntry`](./bamboo_hr_python_sdk/pydantic/timesheet_entry.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employees/{employeeId}/clock_in` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.create_project_task`<a id="bamboohrtime_tracking___private_betacreate_project_task"></a>

Create a time tracking project with optional tasks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_project_task_response = bamboohr.time_tracking___private_beta.create_project_task(
    name="Project A",
    company_domain="companyDomain_example",
    billable=True,
    allow_all_employees=True,
    employee_ids=[
        1
    ],
    has_tasks=True,
    tasks=[
        {
            "name": "name_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the project.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### billable: `bool`<a id="billable-bool"></a>

Indicates if the project is billable. Defaults to true if not provided.

##### allow_all_employees: `bool`<a id="allow_all_employees-bool"></a>

Indicates if all employees can log time for this project. Defaults to true if not provided.

##### employee_ids: [`TimeTrackingPrivateBetaCreateProjectTaskRequestEmployeeIds`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_create_project_task_request_employee_ids.py)<a id="employee_ids-timetrackingprivatebetacreateprojecttaskrequestemployeeidsbamboo_hr_python_sdktypetime_tracking_private_beta_create_project_task_request_employee_idspy"></a>

##### has_tasks: `bool`<a id="has_tasks-bool"></a>

Indicates if the project has tasks. Defaults to false if not provided.

##### tasks: [`TimeTrackingPrivateBetaCreateProjectTaskRequestTasks`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_create_project_task_request_tasks.py)<a id="tasks-timetrackingprivatebetacreateprojecttaskrequesttasksbamboo_hr_python_sdktypetime_tracking_private_beta_create_project_task_request_taskspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingPrivateBetaCreateProjectTaskRequest`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_create_project_task_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingProjectWithTasksAndEmployeeIds`](./bamboo_hr_python_sdk/pydantic/time_tracking_project_with_tasks_and_employee_ids.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.delete_hour_entries`<a id="bamboohrtime_tracking___private_betadelete_hour_entries"></a>

Delete timesheet hour entries.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking___private_beta.delete_hour_entries(
    hour_entry_ids=[
        1
    ],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hour_entry_ids: [`TimeTrackingPrivateBetaDeleteHourEntriesRequestHourEntryIds`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_delete_hour_entries_request_hour_entry_ids.py)<a id="hour_entry_ids-timetrackingprivatebetadeletehourentriesrequesthourentryidsbamboo_hr_python_sdktypetime_tracking_private_beta_delete_hour_entries_request_hour_entry_idspy"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingPrivateBetaDeleteHourEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_delete_hour_entries_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/hour_entries/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.delete_time_sheet_entries`<a id="bamboohrtime_tracking___private_betadelete_time_sheet_entries"></a>

Delete timesheet clock entries.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.time_tracking___private_beta.delete_time_sheet_entries(
    clock_entry_ids=[
        1
    ],
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### clock_entry_ids: [`TimeTrackingPrivateBetaDeleteTimeSheetEntriesRequestClockEntryIds`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_delete_time_sheet_entries_request_clock_entry_ids.py)<a id="clock_entry_ids-timetrackingprivatebetadeletetimesheetentriesrequestclockentryidsbamboo_hr_python_sdktypetime_tracking_private_beta_delete_time_sheet_entries_request_clock_entry_idspy"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingPrivateBetaDeleteTimeSheetEntriesRequest`](./bamboo_hr_python_sdk/type/time_tracking_private_beta_delete_time_sheet_entries_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/clock_entries/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.list_employee_projects`<a id="bamboohrtime_tracking___private_betalist_employee_projects"></a>

Get the projects an employee can track time for.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_projects_response = bamboohr.time_tracking___private_beta.list_employee_projects(
    company_domain="companyDomain_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `str`<a id="employee_id-str"></a>

id of the employee to retrieve projects for.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingPrivateBetaListEmployeeProjectsResponse`](./bamboo_hr_python_sdk/pydantic/time_tracking_private_beta_list_employee_projects_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/employees/{employeeId}/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.time_tracking___private_beta.list_timesheet_entries`<a id="bamboohrtime_tracking___private_betalist_timesheet_entries"></a>

Get all timesheet entries for a given period of time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_timesheet_entries_response = bamboohr.time_tracking___private_beta.list_timesheet_entries(
    company_domain="companyDomain_example",
    start="start_example",
    end="end_example",
    employee_ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### start: `str`<a id="start-str"></a>

YYYY-MM-DD. Only show timesheet entries on/after the specified start date. Must be within the last 365 days.

##### end: `str`<a id="end-str"></a>

YYYY-MM-DD. Only show timesheet entries on/before the specified end date. Must be within the last 365 days.

##### employee_ids: `str`<a id="employee_ids-str"></a>

A comma separated list of employee IDs. When specified, only entries that match these employee IDs are returned.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingPrivateBetaListTimesheetEntriesResponse`](./bamboo_hr_python_sdk/pydantic/time_tracking_private_beta_list_timesheet_entries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/time_tracking/timesheet_entries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.add_category`<a id="bamboohrtrainingadd_category"></a>

Add a training category. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_category_response = bamboohr.training.add_category(
    name="My New Training Category",
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the new training category.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingAddCategoryRequest`](./bamboo_hr_python_sdk/type/training_add_category_request.py)
Training category to post

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingCategory`](./bamboo_hr_python_sdk/pydantic/training_category.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/category` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.add_employee_training_record`<a id="bamboohrtrainingadd_employee_training_record"></a>

Add a new employee training record. The owner of the API key used must have permission to add trainings for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_employee_training_record_response = bamboohr.training.add_employee_training_record(
    completed="Tue May 24 17:00:00 PDT 2016",
    type=0,
    company_domain="companyDomain_example",
    employee_id=0,
    cost=None,
    instructor="Bob Jones",
    hours=16,
    credits=4,
    notes="sample note",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### completed: `date`<a id="completed-date"></a>

Completed is a required field and must be in yyyy-mm-dd format.

##### type: `int`<a id="type-int"></a>

This must be an existing training type id.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `int`<a id="employee_id-int"></a>

The ID of the employee to add a training record to.

##### cost: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./bamboo_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="cost-unionbool-date-datetime-dict-float-int-list-str-nonebamboo_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### instructor: `str`<a id="instructor-str"></a>

##### hours: `Union[int, float]`<a id="hours-unionint-float"></a>

##### credits: `Union[int, float]`<a id="credits-unionint-float"></a>

##### notes: `str`<a id="notes-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingAddEmployeeTrainingRecordRequest`](./bamboo_hr_python_sdk/type/training_add_employee_training_record_request.py)
Training object to post

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingRecord`](./bamboo_hr_python_sdk/pydantic/training_record.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/record/employee/{employeeId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.category_list`<a id="bamboohrtrainingcategory_list"></a>

Get a list of training categories. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
category_list_response = bamboohr.training.category_list(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingCategoryListResponse`](./bamboo_hr_python_sdk/pydantic/training_category_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/category` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.delete_category`<a id="bamboohrtrainingdelete_category"></a>

Delete an existing training category. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.training.delete_category(
    company_domain="companyDomain_example",
    training_category_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### training_category_id: `int`<a id="training_category_id-int"></a>

The ID of the training category to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/category/{trainingCategoryId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.delete_employee_record`<a id="bamboohrtrainingdelete_employee_record"></a>

Delete an existing employee training record. The owner of the API key used must have permission to view and edit the employee and training type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.training.delete_employee_record(
    company_domain="companyDomain_example",
    employee_training_record_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_training_record_id: `int`<a id="employee_training_record_id-int"></a>

The ID of the training record to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/record/{employeeTrainingRecordId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.get_types`<a id="bamboohrtrainingget_types"></a>

Get a list of training types. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_types_response = bamboohr.training.get_types(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingGetTypesResponse`](./bamboo_hr_python_sdk/pydantic/training_get_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/type` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.list_employee_trainings`<a id="bamboohrtraininglist_employee_trainings"></a>

Get all employee training records. The owner of the API key used must have access to view the employee. The API will only return trainings for the employee that the owner of the API key has permission to see. Included with each employee training is the training information that has been selected for tracking in settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_trainings_response = bamboohr.training.list_employee_trainings(
    company_domain="companyDomain_example",
    employee_id=0,
    training_type_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_id: `int`<a id="employee_id-int"></a>

The ID of the employee to get a list of trainings for.

##### training_type_id: `int`<a id="training_type_id-int"></a>

The training type id is optional. Not supplying a training type id will return the collection of all training records for the employee.

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingListEmployeeTrainingsResponse`](./bamboo_hr_python_sdk/pydantic/training_list_employee_trainings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/record/employee/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.remove_type`<a id="bamboohrtrainingremove_type"></a>

Delete an existing training type. The owner of the API key used must have access to training settings. Deleting a training type will only be successful if all employee trainings for this type have been removed prior to this request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.training.remove_type(
    company_domain="companyDomain_example",
    training_type_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### training_type_id: `int`<a id="training_type_id-int"></a>

The ID of the training type to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/type/{trainingTypeId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.type_addition`<a id="bamboohrtrainingtype_addition"></a>

Add a training type. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
type_addition_response = bamboohr.training.type_addition(
    name="My New Training",
    required=False,
    company_domain="companyDomain_example",
    description="string_example",
    frequency=12,
    renewable=True,
    category={
        "id": 3,
        "name": "First Aid Trainings",
        "accuracy": 2,
        "address": "123 Main",
    },
    due_from_hire_date=30,
    link_url="string_example",
    allow_employees_to_mark_complete=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the new training type.

##### required: `bool`<a id="required-bool"></a>

Is this a required training?

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### description: `str`<a id="description-str"></a>

Description for the training.

##### frequency: `int`<a id="frequency-int"></a>

The frequency is the (optional) amount of months between renewing trainings. Not valid if training are not renewable.

##### renewable: `bool`<a id="renewable-bool"></a>

Renewable is optional but if you are setting it to true you must pass a frequency which is the months between renewals.

##### category: [`TrainingTypeAdditionRequestCategory`](./bamboo_hr_python_sdk/type/training_type_addition_request_category.py)<a id="category-trainingtypeadditionrequestcategorybamboo_hr_python_sdktypetraining_type_addition_request_categorypy"></a>


##### due_from_hire_date: `int`<a id="due_from_hire_date-int"></a>

Number of days before the training is due for new hires. Not valid unless training is required.

##### link_url: `str`<a id="link_url-str"></a>

Optional URL that can be included with a training.

##### allow_employees_to_mark_complete: `bool`<a id="allow_employees_to_mark_complete-bool"></a>

Allows all employees who can view the training to be able to mark it complete.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingTypeAdditionRequest`](./bamboo_hr_python_sdk/type/training_type_addition_request.py)
Training object to post

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingType`](./bamboo_hr_python_sdk/pydantic/training_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/type` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.update_category`<a id="bamboohrtrainingupdate_category"></a>

Update an existing training category. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_category_response = bamboohr.training.update_category(
    name="My Training Category",
    company_domain="companyDomain_example",
    training_category_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the training category.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### training_category_id: `int`<a id="training_category_id-int"></a>

The ID of the training category to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingUpdateCategoryRequest`](./bamboo_hr_python_sdk/type/training_update_category_request.py)
Training category to update

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingCategory`](./bamboo_hr_python_sdk/pydantic/training_category.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/category/{trainingCategoryId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.update_employee_training_record`<a id="bamboohrtrainingupdate_employee_training_record"></a>

Update an existing exmployee training record. The owner of the API key used must have permission to add trainings for the selected employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_training_record_response = bamboohr.training.update_employee_training_record(
    completed="2016-05-25",
    company_domain="companyDomain_example",
    employee_training_record_id=0,
    cost=None,
    instructor="Bob Jones",
    hours=16,
    credits=4,
    notes=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### completed: `str`<a id="completed-str"></a>

Completed is the only required field and must be in yyyy-mm-dd format. The other parameters are optional.

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### employee_training_record_id: `int`<a id="employee_training_record_id-int"></a>

The ID of the training record to update.

##### cost: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./bamboo_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="cost-unionbool-date-datetime-dict-float-int-list-str-nonebamboo_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### instructor: `str`<a id="instructor-str"></a>

##### hours: `Union[int, float]`<a id="hours-unionint-float"></a>

##### credits: `Union[int, float]`<a id="credits-unionint-float"></a>

##### notes: `Union[int, float]`<a id="notes-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingUpdateEmployeeTrainingRecordRequest`](./bamboo_hr_python_sdk/type/training_update_employee_training_record_request.py)
Training object to update

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingRecord`](./bamboo_hr_python_sdk/pydantic/training_record.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/record/{employeeTrainingRecordId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.training.update_type`<a id="bamboohrtrainingupdate_type"></a>

Update an existing training type. The owner of the API key used must have access to training settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_type_response = bamboohr.training.update_type(
    name="My Edited Training",
    required=False,
    company_domain="companyDomain_example",
    training_type_id=0,
    description="string_example",
    frequency=12,
    renewable=True,
    category={
        "id": 3,
        "name": "CustomApiCategoryName2",
        "accuracy": 2,
        "address": "123 Main",
    },
    due_from_hire_date=30,
    link_url="string_example",
    allow_employees_to_mark_complete=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the training type.

##### required: `bool`<a id="required-bool"></a>

Is this a required training?

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### training_type_id: `int`<a id="training_type_id-int"></a>

The ID of the training type to update.

##### description: `str`<a id="description-str"></a>

Description for the training.

##### frequency: `int`<a id="frequency-int"></a>

The frequency is the (optional) amount of months between renewing trainings. Not valid if training are not renewable.

##### renewable: `bool`<a id="renewable-bool"></a>

Renewable is optional but if you are setting it to true you must pass a frequency.

##### category: [`TrainingUpdateTypeRequestCategory`](./bamboo_hr_python_sdk/type/training_update_type_request_category.py)<a id="category-trainingupdatetyperequestcategorybamboo_hr_python_sdktypetraining_update_type_request_categorypy"></a>


##### due_from_hire_date: `int`<a id="due_from_hire_date-int"></a>

Number of days before the training is due for new hires. Not valid unless training is required.

##### link_url: `str`<a id="link_url-str"></a>

Optional URL that can be included with a training.

##### allow_employees_to_mark_complete: `bool`<a id="allow_employees_to_mark_complete-bool"></a>

Allows all employees who can view the training to be able to mark it complete.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingUpdateTypeRequest`](./bamboo_hr_python_sdk/type/training_update_type_request.py)
Training type object to update to

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingType`](./bamboo_hr_python_sdk/pydantic/training_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/training/type/{trainingTypeId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.add_new_webhook`<a id="bamboohrwebhooksadd_new_webhook"></a>

Add a new Webhook. For more details or instructions you can refer to the [webhooks API tutorial](https://documentation.bamboohr.com/docs/webhooks-api-permission-based).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_webhook_response = bamboohr.webhooks.add_new_webhook(
    name="My new webhook",
    monitor_fields=["firstName", "lastName"],
    post_fields={
        "key": "string_example",
    },
    url="http:/",
    company_domain="companyDomain_example",
    format="json",
    frequency={
    },
    limit={
    },
    include_company_domain=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the webhook.

##### monitor_fields: [`NewWebHookMonitorFields`](./bamboo_hr_python_sdk/type/new_web_hook_monitor_fields.py)<a id="monitor_fields-newwebhookmonitorfieldsbamboo_hr_python_sdktypenew_web_hook_monitor_fieldspy"></a>

##### post_fields: [`NewWebHookPostFields`](./bamboo_hr_python_sdk/type/new_web_hook_post_fields.py)<a id="post_fields-newwebhookpostfieldsbamboo_hr_python_sdktypenew_web_hook_post_fieldspy"></a>

##### url: `str`<a id="url-str"></a>

The url the webhook should send data to (must begin with https://).

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### format: `str`<a id="format-str"></a>

The format the webhook should use (json - default, form-encoded).

##### frequency: [`NewWebHookFrequency`](./bamboo_hr_python_sdk/type/new_web_hook_frequency.py)<a id="frequency-newwebhookfrequencybamboo_hr_python_sdktypenew_web_hook_frequencypy"></a>


##### limit: [`NewWebHookLimit`](./bamboo_hr_python_sdk/type/new_web_hook_limit.py)<a id="limit-newwebhooklimitbamboo_hr_python_sdktypenew_web_hook_limitpy"></a>


##### include_company_domain: `bool`<a id="include_company_domain-bool"></a>

If set to true, the company domain will be added to the header.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewWebHook`](./bamboo_hr_python_sdk/type/new_web_hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksAddNewWebhookResponse`](./bamboo_hr_python_sdk/pydantic/webhooks_add_new_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.delete_webhook`<a id="bamboohrwebhooksdelete_webhook"></a>

Delete a webhook that is tied to a specific user API Key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bamboohr.webhooks.delete_webhook(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is an webhook ID that is associated with the User API key.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.get_user_list`<a id="bamboohrwebhooksget_user_list"></a>

Gets as list of webhooks for the user API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_list_response = bamboohr.webhooks.get_user_list(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetUserListResponse`](./bamboo_hr_python_sdk/pydantic/webhooks_get_user_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.get_user_webhook`<a id="bamboohrwebhooksget_user_webhook"></a>

Get webhook data that is tied to a specific user API Key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_webhook_response = bamboohr.webhooks.get_user_webhook(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

The webhook ID to display details about.

#### 🔄 Return<a id="🔄-return"></a>

[`WebHookResponse`](./bamboo_hr_python_sdk/pydantic/web_hook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.get_webhook_logs`<a id="bamboohrwebhooksget_webhook_logs"></a>

Get webhook logs for specific webhook id that is associated with the user API Key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webhook_logs_response = bamboohr.webhooks.get_webhook_logs(
    company_domain="companyDomain_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

The webhook ID to get logs about.

#### 🔄 Return<a id="🔄-return"></a>

[`WebHookLogResponse`](./bamboo_hr_python_sdk/pydantic/web_hook_log_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks/{id}/log` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.list_monitor_fields`<a id="bamboohrwebhookslist_monitor_fields"></a>

Get a list fields webhooks can monitor monitor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_monitor_fields_response = bamboohr.webhooks.list_monitor_fields(
    company_domain="companyDomain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListMonitorFieldsResponse`](./bamboo_hr_python_sdk/pydantic/webhooks_list_monitor_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks/monitor_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bamboohr.webhooks.update_webhook_by_id`<a id="bamboohrwebhooksupdate_webhook_by_id"></a>

Update a webhook, based on webhook ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_by_id_response = bamboohr.webhooks.update_webhook_by_id(
    name="My new webhook",
    monitor_fields=["firstName", "lastName"],
    post_fields={
        "key": "string_example",
    },
    url="http:/",
    company_domain="companyDomain_example",
    id="id_example",
    format="json",
    frequency={
    },
    limit={
    },
    include_company_domain=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the webhook.

##### monitor_fields: [`NewWebHookMonitorFields`](./bamboo_hr_python_sdk/type/new_web_hook_monitor_fields.py)<a id="monitor_fields-newwebhookmonitorfieldsbamboo_hr_python_sdktypenew_web_hook_monitor_fieldspy"></a>

##### post_fields: [`NewWebHookPostFields`](./bamboo_hr_python_sdk/type/new_web_hook_post_fields.py)<a id="post_fields-newwebhookpostfieldsbamboo_hr_python_sdktypenew_web_hook_post_fieldspy"></a>

##### url: `str`<a id="url-str"></a>

The url the webhook should send data to (must begin with https://).

##### company_domain: `str`<a id="company_domain-str"></a>

The subdomain used to access BambooHR. If you access BambooHR at https://mycompany.bamboohr.com, then the companyDomain is \"mycompany\"

##### id: `str`<a id="id-str"></a>

{id} is a webhook ID.

##### format: `str`<a id="format-str"></a>

The format the webhook should use (json - default, form-encoded).

##### frequency: [`NewWebHookFrequency`](./bamboo_hr_python_sdk/type/new_web_hook_frequency.py)<a id="frequency-newwebhookfrequencybamboo_hr_python_sdktypenew_web_hook_frequencypy"></a>


##### limit: [`NewWebHookLimit`](./bamboo_hr_python_sdk/type/new_web_hook_limit.py)<a id="limit-newwebhooklimitbamboo_hr_python_sdktypenew_web_hook_limitpy"></a>


##### include_company_domain: `bool`<a id="include_company_domain-bool"></a>

If set to true, the company domain will be added to the header.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewWebHook`](./bamboo_hr_python_sdk/type/new_web_hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebHookResponse`](./bamboo_hr_python_sdk/pydantic/web_hook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{companyDomain}/v1/webhooks/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
