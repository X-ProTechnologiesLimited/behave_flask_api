# file:features/steps/steps_add_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to
from library.get_country import Get_Country


@given('I want to get data for "{country}"')
def step_given_get_country(context, country):
    context.get_country = Get_Country()
    context.get_country.set_country(country)

@given('I want to get list of countries for continent "{continent}"')
def step_given_get_country_continent(context, continent):
    context.get_country = Get_Country()
    context.get_country.set_continent(continent)

@given('I want to get list of all countries')
def step_given_get_all_country(context):
    context.get_country = Get_Country()

@given('I want to get data based on "{capital}"')
def step_given_get_capital(context, capital):
    context.get_country = Get_Country()
    context.get_country.set_capital(capital)

@when('I send request to get specific country details')
def step_get_country_specific(context):
    context.get_country.get_single_country()

@when('I send request to get counties for continent')
def step_get_country_continent(context):
    context.get_country.get_continent_country()

@when('I send request to get country list for continent')
def step_get_country_continent(context):
    context.get_country.get_continent_country_list()

@when('I send request to get all countries')
def step_get_all_countries(context):
    context.get_country.get_all_countries()

@when('I send request to get list of all countries')
def step_get_list_countries(context):
    context.get_country = Get_Country()
    context.get_country.get_country_list()

@when('I send request to get country for capital')
def step_get_country_by_capital(context):
    context.get_country.get_country_by_capital()

@then('The http get country request is successful')
def step_http_status_success(context):
    assert_that(context.get_country.response_json_map['http_response_code'], equal_to(200))

@then('The http get country request is not successful')
def step_http_status_success(context):
    assert_that(context.get_country.response_json_map['http_response_code'], equal_to(404))

@then('The response should return "{parameter_string}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_string, parameter_country):
    context.get_country.single_country_base_map(parameter_string)
    assert_that(context.get_country.response_json_map[parameter_string], equal_to(parameter_country))

@then('The response should return integer "{parameter_int}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_int, parameter_country):
    context.get_country.single_country_base_map(parameter_int)
    assert_that(context.get_country.response_json_map[parameter_int], equal_to(int(parameter_country)))

@then('The response should return number of results : {result_count}')
def step_and_should_return_string(context, result_count):
    assert_that(context.get_country.response_json_map['Total'], equal_to(int(result_count)))


@then('The response should return status : {status_code}')
def step_and_should_return_string(context, status_code):
    assert_that(context.get_country.response_json_map['status'], equal_to(int(status_code)))
