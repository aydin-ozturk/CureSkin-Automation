from behave import given, when, then


@given('Open main page')
def step_impl(context):
    context.app.main_page.open_main_page()


@when('Search for "{product}"')
def step_impl(context, product):
    context.app.main_page.search(product)




