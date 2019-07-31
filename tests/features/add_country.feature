# file:features/country_api.feature
Feature:Add Country

  Scenario Outline:Add a country "<country>" to the database
    Given I want to add country "<country>"
    And I set the capital "<capital>" to "<country>"
    And I add "<country>" to continent "<continent>"
    And I add "<country>" to subregion "<subregion>"
    And I add population "<population>" to "<country>"
    And I add currency name "<currency>" and type "<type>" to "<country>"
    When I send request to add the country
    Then The http request is successful
    And I get a success message "Country Added Successfully"



	Examples:"<country>"
        | country      |capital    | continent | subregion       | population | currency       | type      |
        | India        |New Delhi  | Asia      | Southern Asia   | 1295210000 | Rupees         | INR       |
        | Ireland      |Dublin     | Europe    | Northern Europe | 6378000    | Euro           | EUR       |
        | France       |Paris      | Europe    | Western Europe  | 66710000   | Euro           | EUR       |
        | Great Britain|London     | Europe    | Northern Europe | 65110000   | Sterling-Pound | GBP       |
        | Canada       |Ottawa     | America   | North America   | 167000000  | Canadian Dollar| CAD       |
        | USA          |New York   | America   | North America   | 234000000  | Dollars        | USD       |
