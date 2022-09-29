from pages.search_page import SearchPage
from pages.category_page import CategoryPage


class TestPages:
    def test_pages(self, driver):
        page = SearchPage(driver, 'https://ya.ru/')
        page.open()
        page.select_images_services()
        driver.switch_to.window(driver.window_handles[1])
        page = CategoryPage(driver, 'https://yandex.ru/images/')
        page.select_random_category()


