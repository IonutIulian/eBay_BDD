import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page

class Search_results_page(Base_page):
    ELEMENT_TO_BE_ADDED_TO_CART = (
    By.XPATH, '//ul[@class="srp-results srp-list clearfix"]/li[2]//div[@class="s-item__info clearfix"]/a')
    COLOUR_DROPDOWN = (By.ID, "x-msku__select-box-1001")
    STORAGE_CAPACITY_DROPDOWN = (By.ID, "x-msku__select-box-1000")
    property_dictionary = {}
    property_list = []
    ADD_TO_CART_BUTTON = (By.XPATH, '//span[contains(text(),"Add to cart")]/parent::span/parent::a')
    SHOPPING_CART_BUTTON = (By.XPATH, '//li[@id="gh-minicart-hover"]//a')
    QUANTITY = (By.XPATH, '//select[@data-test-id="qty-dropdown"]/option')

    def open_identified_product(self):
        self.chrome.find_element(*self.ELEMENT_TO_BE_ADDED_TO_CART).click()

    def add_element_to_dictionary(self, property, value):
        self.property_dictionary[property] = value
        return self.property_dictionary

    def choose_product_specifications(self, *args):
        p = self.chrome.current_window_handle
        chwd = self.chrome.window_handles
        for w in chwd:
            if (w != p):
                self.chrome.switch_to.window(w)
                break
        for prop in args:
            self.property_list.append(prop)
        for prop in self.property_list:
            if prop in self.property_dictionary:
                if prop == "colour":
                    colour_dropdown = Select(self.chrome.find_element(
                        *self.COLOUR_DROPDOWN))
                    colour_dropdown.select_by_visible_text(self.property_dictionary.get(
                        prop))
                else:
                    storage_capacity = Select(self.chrome.find_element(*self.STORAGE_CAPACITY_DROPDOWN))
                    storage_capacity.select_by_visible_text(self.property_dictionary.get(prop))

    def click_add_to_cart(self):
        self.chrome.find_element(*self.ADD_TO_CART_BUTTON).click()


    def open_shopping_cart(self):
        self.chrome.find_element(*self.SHOPPING_CART_BUTTON).click()

    def check_number_of_results(self):
        quantity = self.chrome.find_elements(*self.QUANTITY)