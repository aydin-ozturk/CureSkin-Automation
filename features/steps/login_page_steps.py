from behave import given, when, then


@then('Verify account page is opened')
def step_impl(context):
    context.app.login_page.verify_login_page_opened()
