from behave import given, when, then


@when('Click on the first product')
def step_impl(context):
    context.app.all_products_page.click_first_product()


@then('Verify All Products Page is opened')
def step_impl(context):
    context.app.all_products_page.verify_all_products_page_opened()
