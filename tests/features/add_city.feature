# file:features/country_api.feature
Feature:Add City

  Scenario Outline:Add a city "<city>" to the database
    Given I want to add city "<city>"
    And I set the country "<country>" for "<city>"
    And I add latitude "<latitude>" to city "<city>"
    And I add longitude "<longitude>" to city "<city>"
    And I add population "<population>" to city "<city>"
    And I add country_code "<code>" to "<city>"
    When I send request to add the city
    Then The http request is successful
    And I get a "city" add success message "city: <city> is added successfully"



	Examples:"<city>"
        | city         |country         | latitude | longitude  | population | code      |
        | London       |United Kingdom  | 66.1     | 10.3       | 5130000    | GBR       |
        | Kolkata      |India           | 23.1     | 79.4       | 1450000    | IND       |