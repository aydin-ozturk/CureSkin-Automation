Feature: Test cases for product search

  Scenario: User can search for a product that doesn't exist
    Given Open main page
    When Search for "api"
    Then Verify No results found for "api" message is shown