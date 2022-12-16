from behave import given, when, then


@when('Click to add product to cart')
def step_impl(context):
    context.app.product_details_page.click_add_to_cart()


@when('Open cart page')
def step_impl(context):
    context.app.product_details_page.click_on_cart()


@when('Store the first product price')
def step_impl(contex):
    contex.app.product_details_page.store_first_product_price()


@when('Store the second product price')
def step_impl(contex):
    contex.app.product_details_page.store_second_product_price()


@when('Store the first product name')
def step_impl(contex):
    contex.app.product_details_page.store_first_product_name()


@when('Store the second product name')
def step_impl(contex):
    contex.app.product_details_page.store_second_product_name()


@then('Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button')
def step_impl(context):
    context.app.product_details_page.verify_ui_elements_present()

