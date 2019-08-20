# file:features/country_api.feature

@delete
Feature:Delete Continent

  Scenario:Delete a continent from the database
    Given I add bulk data for 3 countries to "Africa"
    And I want to get list of countries for continent "Africa"
    When I send request to get counties for continent
    Then The http get country request is successful
    And The response should return number of results : 3
    When I send request to delete continent "Africa"
    Then The http delete request is successful
    And I get a successful continent delete message "All countries for continent: Africa Deleted Successfully"





