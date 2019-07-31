# file:features/steps/steps_add_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to
from library.update_country import Update_Country


@given('I want to update the "{param}" of country "{country}" to "{value}"')
def step_given_add_country(context, param, country, value):
    context.set_update = Update_Country()
    context.set_update.add_country(country)
    context.set_update.add_param(param)
    context.set_update.add_value(value)

@given('I want to update the currency of country "{country}" to "{value}" and "{type}"')
def step_given_add_country(context, country, value, type):
    context.set_update = Update_Country()
    context.set_update.add_country(country)
    context.set_update.add_param('currency')
    context.set_update.add_value(value)
    context.set_update.add_type(type)

@when('I send request to update the country')
def step_add_country(context):
    context.set_update.update_country()

@then('The http update request is successful')
def step_http_status_success(context):
    assert_that(context.set_update.response_json_map['http_response_code'], equal_to(201))

@then('I get a successful update message "{success_message}"')
def step_message_success(context, success_message):
    context.set_update.country_success_map()
    assert_that(context.set_update.response_json_map['message'], equal_to(success_message))
    assert_that(context.set_update.response_json_map['status'], equal_to(201))
