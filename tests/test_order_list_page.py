import allure

from pages.main_page import MainPage
from pages.orders_list_page import OrdersListPage

class TestOrderListPageFunctions:
    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_total_counter_after_order(self, driver, login_user, create_order):
        main_page = MainPage(driver)
        order_list_page = OrdersListPage(driver)
        login_user()
        main_page.click_on_list_of_orders_btn()
        old_value_of_counter = order_list_page.get_all_time_orders()
        main_page.click_on_constructor_btn()
        create_order()
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        new_value_of_counter = order_list_page.get_all_time_orders()
        assert new_value_of_counter > old_value_of_counter

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_counter_after_order(self, driver, login_user, create_order):
        main_page = MainPage(driver)
        order_list_page = OrdersListPage(driver)
        login_user()
        main_page.click_on_list_of_orders_btn()
        old_value_of_counter = order_list_page.get_today_orders()
        main_page.click_on_constructor_btn()
        create_order()
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        new_value_of_counter = order_list_page.get_today_orders()
        assert new_value_of_counter > old_value_of_counter
        
    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_in_progress(self, driver, login_user, create_order):
        main_page = MainPage(driver)
        order_list_page = OrdersListPage(driver)
        login_user()
        create_order()
        order_number = main_page.get_order_number()
        main_page.close_order_popup()
        main_page.click_on_list_of_orders_btn()
        in_progress_unit = order_list_page.get_orders_numbers_in_progress()
        assert order_number in in_progress_unit