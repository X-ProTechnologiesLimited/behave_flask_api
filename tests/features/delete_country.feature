# file:features/country_api.feature

@delete
Feature:Delete Country

  Scenario Outline:Delete a country "<country>" from the database
    Given I want to delete country "<country>"
    When I send request to delete the country
    Then The http delete request is successful
    And I get a successful delete message "Country Deleted Successfully"


	Examples:"<country>"
        | country      |
        | India        |
        | Ireland      |
        | Great Britain|
        | Canada       |
        | USA          |
        | France       |



  Scenario Outline: Try to Fetch Deleted Country "<country>"
    Given I want to get data for "<country>"
    When I send request to get specific country details
    Then The http get country request is not successful
    Then The response should return status : 404

    Examples:"<country>"
        | country      |
        | India        |
        | Ireland      |
        | Great Britain|
        | Canada       |
        | USA          |
        | France       |

