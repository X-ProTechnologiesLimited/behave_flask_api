# file:features/steps/steps_add_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to
from library.del_country import Del_Country


@given('I want to delete country "{country}"')
def step_given_del_country(context, country):
    context.del_country = Del_Country()
    context.del_country.set_country(country)

@when('I send request to delete the country')
def step_del_country(context):
    context.del_country.del_country()

@when('I send request to delete continent "{continent}"')
def step_del_continent(context, continent):
    context.del_country = Del_Country()
    context.del_country.del_continent(continent)

@then('The http delete request is successful')
def step_http_status_success(context):
    assert_that(context.del_country.response_json_map['http_response_code'], equal_to(201))

@then('I get a successful delete message "{success_message}"')
def step_message_success(context, success_message):
    context.del_country.country_del_map()
    assert_that(context.del_country.response_json_map['message'], equal_to(success_message))
    assert_that(context.del_country.response_json_map['status'], equal_to(201))

@then('I get a successful continent delete message "{success_message}"')
def step_message_success(context, success_message):
    context.del_country.continent_del_map()
    assert_that(context.del_country.response_json_map['message'], equal_to(success_message))
    assert_that(context.del_country.response_json_map['status'], equal_to(201))