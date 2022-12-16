Feature: Test cases for product search

  Scenario Outline: User can search for a product that doesn't exist
    Given Open main page
    When Enter a product name that does not exist to search box: "<product>"
    Then Verify no results returned on the drop-down
    When Click on search button on the drop-down
    Then Verify No results found for "<product>" message is shown
  Examples:
    |    product    |
    | sdfhsd        |
    | api           |
    | @#$%          |
