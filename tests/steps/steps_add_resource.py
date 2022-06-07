# file:features/steps/steps_add_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to
from library.add_resource import Add_resource


@given('I want to add country "{country}"')
def step_given_add_country(context, country):
    context.set_resource = Add_resource()
    context.set_resource.add_country(country)

@given('I set the capital "{capital}" to "{country}"')
def step_given_add_captal(context, capital, country):
    context.set_resource.add_capital(capital)

@given('I add "{country}" to continent "{continent}"')
def step_given_add_continent(context, country, continent):
    context.set_resource.add_continent(continent)

@given('I add "{country}" to subregion "{subregion}"')
def step_given_add_subregion(context, country, subregion):
    context.set_resource.add_subregion(subregion)

@given('I add population "{population}" to "{country}"')
def step_given_add_population(context, population, country):
    context.set_resource.add_population(population)

@given('I add currency "{currency}" to "{country}"')
def step_given_add_currency(context, currency, country):
    context.set_resource.add_currency(currency)

@given('I add code "{code}" to "{country}"')
def step_given_add_code(context, code, country):
    context.set_resource.add_code(code)




@given('I want to add city "{city}"')
def step_given_add_city(context, city):
    context.set_resource = Add_resource()
    context.set_resource.add_city(city)

@given('I set the country "{country}" for "{city}"')
def step_given_add_city_country(context, country, city):
    context.set_resource.add_country(country)

@given('I add latitude "{latitude}" to city "{city}"')
def step_given_add_latitude(context, latitude, city):
    context.set_resource.add_latitude(latitude)

@given('I add longitude "{longitude}" to city "{city}"')
def step_given_add_longitude(context, longitude, city):
    context.set_resource.add_longitude(longitude)

@given('I add country_code "{code}" to "{city}"')
def step_given_add_code(context, code, city):
    context.set_resource.add_code(code)

@given('I add population "{population}" to city "{city}"')
def step_given_add_population(context, population, city):
    context.set_resource.add_population(population)





@given('I add bulk data for {limit} countries to "{continent}"')
def step_given_add_bulk_country(context, limit, continent):
    context.set_resource = Add_resource()
    context.set_resource.add_continent(continent)
    context.set_resource.bulk_country_add(int(limit))

@when('I send request to add the country')
def step_add_country(context):
    context.set_resource.new_country_add()

@when('I send request to add the city')
def step_add_city(context):
    context.set_resource.new_city_add()

@then('The http request is successful')
def step_http_status_success(context):
    assert_that(context.set_resource.response_json_map['http_response_code'], equal_to(201))

@then('I get a "{resource}" add success message "{success_message}"')
def step_message_success(context, resource, success_message):
    if resource == 'country':
        context.set_resource.country_success_map()
    elif resource == 'city':
        context.set_resource.city_success_map()
    assert_that(context.set_resource.response_json_map['message'], equal_to(success_message))
    assert_that(context.set_resource.response_json_map['status'], equal_to(201))

@then('response should return string "{parameter_string}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_string, parameter_country):
    context.set_resource.get_country_keys(parameter_string)
    assert_that(context.set_resource.response_json_map[parameter_string], equal_to(parameter_country))

@then('response should return integer "{parameter_integer}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_integer, parameter_country):
    context.set_resource.get_country_keys(parameter_integer)
    assert_that(context.set_resource.response_json_map[parameter_integer], equal_to(int(parameter_country)))
