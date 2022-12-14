from behave import given, when, then


@when('Click to add product to cart')
def step_impl(context):
    context.app.product_details_page.click_add_to_cart()


@when('Open cart page')
def step_impl(context):
    context.app.product_details_page.click_on_cart()


@then('Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button')
def step_impl(context):
    context.app.product_details_page.verify_ui_elements_present()

