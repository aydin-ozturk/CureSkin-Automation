from behave import given, when, then


@then('Verify All Products Page is opened')
def step_impl(context):
    context.app.all_products_page.verify_all_products_page_opened()
