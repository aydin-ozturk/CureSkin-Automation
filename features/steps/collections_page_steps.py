from behave import given, when, then


@then('Verify "{category_name}" header is shown')
def step_impl(context, category_name):
    context.app.collections_page.verify_header_is_category_name(category_name)


@then('Verify first product name has the word "{category_name}" in it')
def step_impl(context, category_name):
    context.app.collections_page.verify_first_prod_name_includes_category_name(category_name)
