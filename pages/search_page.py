import time

import allure
from pages.base_page import BasePage
from locators.pages_locators import SearchPageLocators


class SearchPage(BasePage):

    def select_images_services(self):
        self.element_is_visible(SearchPageLocators.SEARCH_FIELD)
        self.element_is_visible(SearchPageLocators.ALL_SERVICES).click()
        self.element_is_visible(SearchPageLocators.IMAGES_SERVICE).click()
