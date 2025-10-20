import allure

from locators.locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Ввод электронной почты в поле "Email"')
    def enter_email(self, email):
        self.send_keys_to_input(Locators.LOGIN_EMAIL, email)

    @allure.step('Ввод пароля в поле "Password"')
    def enter_password(self, password):
        self.send_keys_to_input(Locators.LOGIN_PASSWORD, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        self.click_on_element(Locators.LOGIN_SUBMIT)