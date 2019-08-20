# file:features/get_contry_list.feature

@list
Feature:Get Country List

  Scenario:Get country list for Specific Continent
    Given I add bulk data for 5 countries to "Oceania"
    And I want to get list of countries for continent "Oceania"
    When I send request to get country list for continent
    Then The http get country request is successful
    And The response should return number of results : 5


  Scenario:Get all Country List
    Given I add bulk data for 5 countries to "Australia"
    And I add bulk data for 10 countries to "Antarctica"
    When I send request to get list of all countries
    Then The http get country request is successful
    And The response should return number of results : 26