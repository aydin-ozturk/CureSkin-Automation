from behave import given, when, then


@given('Open main page')
def step_impl(context):
    context.app.main_page.open_main_page()


@when('Search for "{product}"')
def step_impl(context, product):
    context.app.main_page.search(product)


@when('Click on "shop by category"')
def step_impl(context):
    context.app.main_page.click_on_shop_by_category()


@when('Select {category_name} category')
def step_impl(context, category_name):
    context.app.main_page.click_on_category_name(category_name)
