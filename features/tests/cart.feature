Feature: Test cases for shopping cart

  Scenario: Cart calculates price for the same product
    Given Open Product Details page of CureSkin Cleansing Gel
    When Click on Add to cart button
    And Open cart page
    And Store the current price
    And Click plus icon to increase product quantity
    Then Verify total price has doubled
    And Verify that product quantity is set to 2

  Scenario: Different products can be added to the cart
    Given Open Product Details page of CureSkin Hair Defence Shampoo
    When Sum and Store the product price
    And Store the product names
    And Click on Add to cart button
    Given Open Product Details page of CureSkin Kojic Plus Cream
    When Sum and Store the product price
    And Store the product names
    And Click on Add to cart button
    And Open cart page
    Then Verify all products are in the cart
    And Verify total price is correct

  Scenario: Users can see all products by clicking on View All button in cart page
    Given Open cart page
    When Click on view all button
    Then Verify All Products Page is opened

  Scenario: Cart count not updated when navigating using back arrow
    Given Open main page
    When Click on Shop All in the footer
    And Click on the first product
    And Click on Add to cart button
    Then Verify the product count is shown on the cart icon
    When Navigate back using browser back button
    Then Verify the product count is shown on the cart icon
