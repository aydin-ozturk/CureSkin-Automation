from behave import given, when, then


@when('Store the current price')
def step_impl(context):
    context.app.cart_page.store_cart_total()


@when('Click plus icon to increase product quantity')
def step_impl(context):
    context.app.cart_page.click_on_plus_icon()


@then('Verify total price has doubled')
def step_impl(context):
    context.app.cart_page.verify_cart_total_doubled()


@then('Verify that product quantity is set to 2')
def step_impl(context):
    context.app.cart_page.verify_product_quantity()


@then('Verify all products are in the cart')
def step_impl(context):
    context.app.cart_page.verify_all_products_in_cart()


@then('Verify total price is correct')
def step_impl(context):
    context.app.cart_page.verify_total_cart_price()
