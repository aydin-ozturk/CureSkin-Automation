from behave import given, when, then


@when('Click on Add to cart button')
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


@when('Navigate back using browser back button')
def step_impl(contex):
    contex.app.product_details_page.navigate_back()


@then('Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button')
def step_impl(context):
    context.app.product_details_page.verify_ui_elements_present()


@then('Verify the product count is shown on the cart icon')
def step_impl(context):
    context.app.product_details_page.verify_product_count_on_cart_icon()
