import time

import allure
from pages.base_page import BasePage
from locators.locators import SearchPageLocators, CategoryPageLocators, SelectedCategoryLocators


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


class CategoryPage(BasePage):

    def select_random_category(self):
        selected_categories = self.element_is_visible(CategoryPageLocators.CATEGORIES)
        selected_categories.click()
        return selected_categories.get_attribute("data-grid-text")

    def get_value_search_category(self):
        result = self.element_is_visible(CategoryPageLocators.SEARCH_FIELD_CATEGORY).get_attribute("value")
        return result


class SelectedCategoryPage(BasePage):

    def get_value(self):
        result = self.element_is_visible(SelectedCategoryLocators.SEARCH_FIELD_SELECTED_CATEGORY)
        return result.get_attribute("value")