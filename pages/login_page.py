import allure

from locators.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):

    @allure.step('Ввод электронной почты в поле "Email"')
    def enter_email(self, email):
        self.add_text_to_element(Locators.LOGIN_EMAIL, email)

    @allure.step('Ввод пароля в поле "Password"')
    def enter_password(self, password):
        self.add_text_to_element(Locators.LOGIN_PASSWORD, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_SUBMIT))
        try:
            wait.until(EC.invisibility_of_element_located(Locators.OVERLAY))
        except TimeoutException:
            pass
        self.click_on_element(Locators.LOGIN_SUBMIT)