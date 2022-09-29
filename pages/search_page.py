import time

import allure
from pages.base_page import BasePage
from locators.locators import SearchPageLocators


class SearchPage(BasePage):

    def select_images_services(self):
        self.element_is_visible(SearchPageLocators.ALL_SERVICES).click()
        self.element_is_visible(SearchPageLocators.IMAGES_SERVICE).click()

    def search_field_is_present(self):
        return "search field is present" if self.element_is_visible(
            SearchPageLocators.SEARCH_FIELD) is not None else "search field is not present"

    def image_service_is_present(self):
        return "image service is present" if self.element_is_visible(
            SearchPageLocators.SEARCH_FIELD) is not None else "image service is not present"
