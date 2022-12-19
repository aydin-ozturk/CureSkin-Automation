from behave import given, when, then


@when('Click to add product to cart')
def step_impl(context):
    context.app.product_details_page.click_add_to_cart()


@when('Open cart page')
def step_impl(context):
    context.app.product_details_page.click_on_cart()


@when('Sum and Store the product price')
def step_impl(contex):
    contex.app.product_details_page.sum_and_store_product_prices()


@when('Store the product names')
def step_impl(contex):
    contex.app.product_details_page.store_product_names()


@then('Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button')
def step_impl(context):
    context.app.product_details_page.verify_ui_elements_present()

