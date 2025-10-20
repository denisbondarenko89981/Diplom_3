import allure

from locators.locators import Locators
from pages.base_page import BasePage

class OrdersListPage(BasePage):

    @allure.step('Выполнен переход в Ленту заказов. Заголовок страницы "Лента заказов"')
    def get_list_of_orders_ttl(self):
        return self.get_text_on_element(Locators.LIST_OF_ORDERS_TTL)

    @allure.step('Получение количества выполненных заказов за всё время')
    def get_all_time_orders(self):
        return self.get_text_on_element(Locators.ALL_TIME_ORDERS)

    @allure.step('Получение количества выполненных заказов за сегодня')
    def get_today_orders(self):
        return self.get_text_on_element(Locators.TODAY_ORDERS)
    
    @allure.step('Получение номеров заказов "В работе"')
    def get_orders_numbers_in_progress(self):
        self.wait_for_element(Locators.ORDERS_IN_PROGRESS)
        return self.get_text_on_element(Locators.ORDERS_IN_PROGRESS)






