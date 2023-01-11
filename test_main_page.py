import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.busket_page import BusketPage
import faker

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope='class',autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        login_page.open()
        '''f = faker.Faker()
        email = f.email()
        password = f.password'''
        email = 'kikimora@gmail.ru'
        password = '11012023'
        login_page.register_new_user(email, password)

    def test_guest_can_go_to_login_page(self,browser):
        link = " http://selenium1py.pythonanywhere.com/ "
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self,browser):
        link = " http://selenium1py.pythonanywhere.com/ "
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_success_message(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        browser.implicitly_wait(5)
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.correct_name_product_in_busket()
        page.correct_price_in_busket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = " http://selenium1py.pythonanywhere.com/ "
    page = BusketPage(browser, link)
    page.open()
    page.go_to_busket()
    page.shold_be_text_empty()
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BusketPage(browser,link)
    page.open()
    page.go_to_busket()
    page.shold_be_text_empty()
