import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.data import PersonalData, Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login_user(driver):
    def _login_user():
        driver.get(Urls.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_login_into_account_btn()
        login_page = LoginPage(driver)
        login_page.enter_email(PersonalData.EMAIL)
        login_page.enter_password(PersonalData.PASSWORD)
        login_page.click_login_btn()
    return _login_user

@pytest.fixture(scope='function')
def create_order(driver):
    def _create_order():
        main_page = MainPage(driver)
        main_page.move_ingredient_in_order_area_for_counter()
        main_page.click_create_an_order_btn()
    return _create_order