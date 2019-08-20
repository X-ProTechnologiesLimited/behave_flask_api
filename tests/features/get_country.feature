# file:features/get_country.feature
Feature:Get Country

  Scenario Outline:Get County Data for "<country>"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is successful
    And The response should return "capital" : "<capital>"
    And The response should return "continent" : "<continent>"
    And The response should return "subregion" : "<subregion>"
    And The response should return currency "name" : "<currency>"
    And The response should return currency "type" : "<type>"
    And The response should return integer "population" : "<population>"
    And The response should return number of results : 1


	Examples:"<country>"
        | country      |capital    | continent | subregion       | population | currency       | type      |
        | India        |New Delhi  | Asia      | Southern Asia   | 1295210000 | Rupees         | INR       |
        | Ireland      |Dublin     | Europe    | Northern Europe | 6378000    | Euro           | EUR       |
        | France       |Paris      | Europe    | Western Europe  | 66710000   | Euro           | EUR       |
        | Great Britain|London     | Europe    | Northern Europe | 65110000   | Sterling-Pound | GBP       |
        | Canada       |Ottawa     | America   | North America   | 167000000  | Canadian Dollar| CAD       |
        | USA          |New York   | America   | North America   | 234000000  | Dollars        | USD       |




  Scenario Outline: Get Country Data for Continent "<continent>"
    Given I want to get list of countries for continent "<continent>"
    When I send request to get counties for continent
    Then The http get country request is successful
    And The response should return number of results : <count>

    Examples:"<continent>"
        | continent   |  count |
        | Asia        |  1     |
        | Europe      |  3     |
        | America     |  2     |


  Scenario: Get All countries in the database
    Given I want to get list of all countries
    When I send request to get all countries
    Then The http get country request is successful
    And The response should return number of results : 6



  Scenario Outline:Get County Data from "<capital>"
    Given I want to get data based on "<capital>"
    When I send request to get country for capital
    Then The http get country request is successful
    And The response should return "country_name" : "<country>"
    And The response should return "continent" : "<continent>"
    And The response should return "subregion" : "<subregion>"
    And The response should return currency "name" : "<currency>"
    And The response should return currency "type" : "<type>"
    And The response should return integer "population" : "<population>"
    And The response should return number of results : 1


	Examples:"<country>"
        | country      |capital    | continent | subregion       | population | currency       | type      |
        | India        |New Delhi  | Asia      | Southern Asia   | 1295210000 | Rupees         | INR       |
        | Ireland      |Dublin     | Europe    | Northern Europe | 6378000    | Euro           | EUR       |
        | France       |Paris      | Europe    | Western Europe  | 66710000   | Euro           | EUR       |
        | Great Britain|London     | Europe    | Northern Europe | 65110000   | Sterling-Pound | GBP       |
        | Canada       |Ottawa     | America   | North America   | 167000000  | Canadian Dollar| CAD       |
        | USA          |New York   | America   | North America   | 234000000  | Dollars        | USD       |
