import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с заложенным ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание отображения элемента на странице')
    def waiting_for_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверка наличия элемента на странице')
    def check_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до заданного элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение адреса URL текущей страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверка отсутствия элемента на странице')
    def check_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Перетаскивание элемента по странице')     
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)
    
    @allure.step('Ожидание когда эллемены перестанет перекрывать оверлей')    
    def wait_for_overlay_to_disappear(self, timeout=10):
        overlay_locator = (Locators.OVERLAY)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(overlay_locator)
            )
        except TimeoutException:
            pass

    @allure.step('Клик на элемент с заложенным ожиданием')
    def click_on_element(self, locator, timeout=10):
        try:
            self.wait_for_overlay_to_disappear(timeout=timeout)
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            for _ in range(3):
                try:
                    element.click()
                    return
                except (ElementClickInterceptedException, StaleElementReferenceException):
                    time.sleep(0.5)
                    self.wait_for_overlay_to_disappear(timeout=2)
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable(locator)
                    )
        except TimeoutException:
            raise AssertionError(f"Элемент {locator} так и не стал кликабельным")