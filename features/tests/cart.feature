Feature: Test cases for shopping cart

  Scenario: Cart calculates price for the same product
    Given Open Product Details page of CureSkin Cleansing Gel
    When Click to add product to cart
    And Open cart page
    And Store the current price
    And Click plus icon to increase product quantity
    Then Verify total price has doubled
    And Verify that product quantity is set to 2