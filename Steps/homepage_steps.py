from behave import *

@given("Home page: I am on Ebay homepage")
def step_impl(context):
	context.home_page_object.navigate_to_homepage()
	context.home_page_object.accept_cookies()


@when('Home page: I search for "{product_name}" from category "{category_name}"')
def step_impl(context,product_name,category_name):
	context.home_page_object.insert_search_value(product_name)
	context.home_page_object.choose_category(category_name)
	context.home_page_object.click_search_button()

@then('Home page: I have at least "{no_of_results}" results returned')
def step_impl(context,no_of_results):
	context.home_page_object.check_search_results(no_of_results)


@when("Home page: When I click on the advanced link")
def step_impl(context):
	context.home_page_object.click_advanced_search_link()

