from selenium.webdriver.common.by import By
from random import randint


class SearchPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "input.search3__input")
    ALL_SERVICES = (By.CSS_SELECTOR, 'a[href="https://yandex.ru/all"]')
    IMAGES_SERVICE = (By.CSS_SELECTOR, 'a[href="//yandex.ru/images/"]')


class CategoryPageLocators:
    CATEGORIES = (By.CSS_SELECTOR, f"div.PopularRequestList-Item_pos_{randint(1, 19)}")
