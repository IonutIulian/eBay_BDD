from browser import Browser
from pages.advanced_search import Advanced_page
from pages.homepage import Home_page


from pages.results_page import Search_results_page


def before_all(context):
	context.browser = Browser()
	context.home_page_object = Home_page()
	context.advanced_search_object = Advanced_page()
	context.search_results_object = Search_results_page()


def after_all(context):
	context.browser.close()