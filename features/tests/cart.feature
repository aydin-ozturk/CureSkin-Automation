Feature: Test cases for shopping cart

  Scenario: Cart calculates price for the same product
    Given Open Product Details page of CureSkin Cleansing Gel
    When Click to add product to cart
    And Open cart page
    And Store the current price
    And Click plus icon to increase product quantity
    Then Verify total price has doubled
    And Verify that product quantity is set to 2

  Scenario: Different products can be added to the cart
    Given Open Product Details page of CureSkin Hair Defence Shampoo
    When Sum and Store the product price
    And Store the product names
    And Click to add product to cart
    Given Open Product Details page of CureSkin Kojic Plus Cream
    When Sum and Store the product price
    And Store the product names
    And Click to add product to cart
    And Open cart page
    Then Verify all products are in the cart
    And Verify total price is correct

  Scenario: Users can see all products by clicking on View All button in cart page
    Given Open cart page
    When Click on view all button
    Then Verify All Products Page is opened
