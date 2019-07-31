# file:features/country_api.feature
Feature:Update Country

  Scenario Outline:Update population of country "<country>" from the database
    Given I want to update the "population" of country "<country>" to "<value>"
    When I send request to update the country
    Then The http update request is successful
    And I get a successful update message "Country Updated Successfully"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is successful
    And The response should return integer "population" : "<value>"


	Examples:"<country>"
        | country      | value      |
        | India        | 1395210000 |
        | USA          | 244000000  |



  Scenario Outline:Update capital of country "<country>" from the database
    Given I want to update the "capital" of country "<country>" to "<value>"
    When I send request to update the country
    Then The http update request is successful
    And I get a successful update message "Country Updated Successfully"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is successful
    And The response should return "capital" : "<value>"


	Examples:"<country>"
        | country      | value       |
        | India        | Mumbai      |
        | USA          | Washington  |


  Scenario Outline:Update continent of country "<country>" from the database
    Given I want to update the "continent" of country "<country>" to "<value>"
    When I send request to update the country
    Then The http update request is successful
    And I get a successful update message "Country Updated Successfully"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is successful
    And The response should return "continent" : "<value>"


	Examples:"<country>"
        | country      | value       |
        | France       | EU          |
        | Canada       | Americas    |


  Scenario Outline:Update subregion of country "<country>" from the database
    Given I want to update the "subregion" of country "<country>" to "<value>"
    When I send request to update the country
    Then The http update request is successful
    And I get a successful update message "Country Updated Successfully"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is successful
    And The response should return "subregion" : "<value>"


	Examples:"<country>"
        | country      | value             |
        | France       | EU-Main           |
        | Canada       | North-Americas    |


   Scenario Outline:Update currency of country "<country>" from the database
    Given I want to update the currency of country "<country>" to "<value>" and "<type>"
    When I send request to update the country
    Then The http update request is successful
    And I get a successful update message "Country Updated Successfully"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is successful
    And The response should return currency "name" : "<value>"
    And The response should return currency "type" : "<type>"


	Examples:"<country>"
        | country      | value             | type  |
        | France       | Franc             | FRC   |
        | Canada       | Dollars           | CADDY |