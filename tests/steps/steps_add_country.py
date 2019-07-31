# file:features/steps/steps_add_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to
from library.add_country import Add_Country


@given('I want to add country "{country}"')
def step_given_add_country(context, country):
    context.set_country = Add_Country()
    context.set_country.add_country(country)

@given('I set the capital "{capital}" to "{country}"')
def step_given_add_captal(context, capital, country):
    context.set_country.add_capital(capital)

@given('I add "{country}" to continent "{continent}"')
def step_given_add_continent(context, country, continent):
    context.set_country.add_continent(continent)

@given('I add "{country}" to subregion "{subregion}"')
def step_given_add_subregion(context, country, subregion):
    context.set_country.add_subregion(subregion)

@given('I add population "{population}" to "{country}"')
def step_given_add_population(context, population, country):
    context.set_country.add_population(population)

@given('I add currency name "{currency}" and type "{type}" to "{country}"')
def step_given_add_currency(context, currency, type, country):
    context.set_country.add_currency(currency, type)

@when('I send request to add the country')
def step_add_country(context):
    context.set_country.new_country_add()

@then('The http request is successful')
def step_http_status_success(context):
    assert_that(context.set_country.response_json_map['http_response_code'], equal_to(201))

@then('I get a success message "{success_message}"')
def step_message_success(context, success_message):
    context.set_country.country_success_map()
    assert_that(context.set_country.response_json_map['message'], equal_to(success_message))
    assert_that(context.set_country.response_json_map['status'], equal_to(201))

@then('response should return string "{parameter_string}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_string, parameter_country):
    context.set_country.get_country_keys(parameter_string)
    assert_that(context.set_country.response_json_map[parameter_string], equal_to(parameter_country))

@then('response should return integer "{parameter_integer}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_integer, parameter_country):
    context.set_country.get_country_keys(parameter_integer)
    assert_that(context.set_country.response_json_map[parameter_integer], equal_to(int(parameter_country)))
