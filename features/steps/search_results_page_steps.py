from behave import given, when, then


@then('Verify No results found for "{product}" message is shown')
def step_impl(context, product):
    context.app.search_results_page.verify_no_result_msg_shown(product)
