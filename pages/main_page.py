import allure

from locators.locators import Locators
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class MainPage(BasePage):

    @allure.step('Клик по кнопке "Лента заказов" в шапке сайта')
    def click_on_list_of_orders_btn(self):
        self.click_on_element(Locators.LIST_ORDERS_BUTTON)

    @allure.step('Клик по кнопке "Конструктор" в шапке сайта')
    def click_on_constructor_btn(self):
        self.click_on_element(Locators.CONSTRUCTOR_BUTTON)

    @allure.step('Выполнен переход в конструктор. Заголовок страницы "Соберите бургер"')
    def get_title_of_constructor_page(self):
        return self.get_text_from_element(Locators.ASSEMBLE_THE_BURGER_TTL)

    @allure.step('Клик на эллемент "Краторная булка N-200i"')
    def click_on_bun_n200i(self):
        self.click_on_element(Locators.BUN_N200i)

    @allure.step('Открылось онко Детали ингредиента. Заголовок окна "Детали ингредиента"')
    def check_title_of_popup(self):
        return self.get_text_from_element(Locators.TITLE_OF_INGREDIENT_POPUP)
    
    @allure.step('Клик на эллемент закрытия окна "Детали ингридиента"')
    def close_ingredient_popup(self):
        self.click_on_element(Locators.CLOSE_INGREDIENT_POPUP_BTN)
    
    @allure.step('Ожидание закрытия откна "Детали ингридиента"')    
    def wait_until_popup_disappears(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(Locators.TITLE_OF_INGREDIENT_POPUP)
        )
    
    @allure.step('Окно "Детали ингридиентов" закрылось')
    def is_popup_visible(self):
        try:
            return self.driver.find_element(*Locators.TITLE_OF_INGREDIENT_POPUP).is_displayed()
        except:
            return False
    
    @allure.step('Перетаскивание ингредиента "Краторная булка N-200i" в область заказа')
    def move_ingredient_in_order_area_for_counter(self):
        # сначала дожидаемся, чтобы оба элемента были видимыми
        self.waiting_for_element_to_be_visible(Locators.BUN_N200i)
        self.waiting_for_element_to_be_visible(Locators.ORDER_AREA)
        bun = self.driver.find_element(*Locators.BUN_N200i)
        order_area = self.driver.find_element(*Locators.ORDER_AREA)
        drag_and_drop(self.driver, bun, order_area)

    @allure.step('Значение количества в счетчике ингридиента увеличилось')
    def get_count_of_ingredient(self):
        return self.get_text_from_element(Locators.COUNT_N200i)
    
    @allure.step('Клик по кнопке "Войти в аккаунт" на главной странице')
    def click_on_login_into_account_btn(self):
        self.click_on_element(Locators.LOGIN_ACCOUNT)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_create_an_order_btn(self):
        self.click_on_element(Locators.CREATE_ORDER)

    @allure.step('Закрытие всплывающего окна "Детали заказа"')
    def close_order_popup(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located(Locators.OVERLAY))
        wait.until(EC.element_to_be_clickable(Locators.CLOSE_ORDER_POPUP_BTN))
        def safe_click(driver):
            try:
                element = driver.find_element(*Locators.CLOSE_ORDER_POPUP_BTN)
                element.click()
                return True
            except (ElementClickInterceptedException, StaleElementReferenceException):
                return False
        WebDriverWait(self.driver, 5).until(safe_click)
        wait.until(EC.invisibility_of_element_located(Locators.ORDER_POPUP))
        wait.until(EC.invisibility_of_element_located(Locators.OVERLAY))
    
    @allure.step('Получение номера заказа')
    def get_order_number(self):
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(Locators.OVERLAY)
        )
        order_id_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(Locators.ORDER_ID)
        )
        WebDriverWait(self.driver, 15).until(
            lambda driver: order_id_element.text.strip() not in ("", "9999")
        )
        order_number = ''.join(filter(str.isdigit, order_id_element.text.strip()))
        return order_number




