from behave import given, when, then


@then('Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button')
def step_impl(context):
    context.app.product_details_page.verify_ui_elements_present()
