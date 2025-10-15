import allure

from pages.main_page import MainPage
from pages.orders_list_page import OrdersListPage
from data.data import Urls

class TestMainPageFunctions:
    @allure.title('Проверка перехода в Конструктор по клику в шапке')
    def test_click_on_constructor(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_list_of_orders_btn()
        main_page.click_on_constructor_btn()
        assert main_page.get_title_of_constructor_page() == 'Соберите бургер'
    
    @allure.title('Проверка перехода в Ленту заказов по клику в шапке')
    def test_click_on_list_0f_orders(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        orders_page = OrdersListPage(driver)
        main_page.click_on_list_of_orders_btn()
        assert orders_page.get_list_of_orders_ttl() == 'Лента заказов'
    
    @allure.title('Проверка открытия всплывающего окна с деталями ингредиента при клике на отдельный ингредиент')
    def test_click_on_ingredient(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_bun_n200i()
        assert main_page.check_title_of_popup() == 'Детали ингредиента'
        
    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента при клике на крестик')
    def test_close_on_popup(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_bun_n200i()
        main_page.close_ingredient_popup()
        main_page.wait_until_popup_disappears()
        assert not main_page.is_popup_visible()

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increase_counter_of_ingredient(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.move_ingredient_in_order_area_for_counter()
        assert main_page.get_count_of_ingredient() == '2'

