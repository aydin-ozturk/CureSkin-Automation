Feature: Test cases for main page

  Scenario: User can shop by category
    Given Open main page
    When Click on "shop by category"
    And Select Hair category
    Then Verify "Hair" header is shown
    And Verify first product name has the word "Hair" in it