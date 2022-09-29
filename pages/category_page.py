import time

import allure
from pages.base_page import BasePage
from locators.pages_locators import CategoryPageLocators


class CategoryPage(BasePage):

    def select_random_category(self):
        self.element_is_visible(CategoryPageLocators.CATEGORIES).click()
        time.sleep(2)