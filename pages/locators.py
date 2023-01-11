from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BusketPageLocators():
    BUSKET_LINK = (By.CSS_SELECTOR, ".page_inner .btn-group .btn-default")
    BUSKET_EMPTY = (By.ID, 'content_inner')


class LoginPageLocators():
    FORM_REGISTRATION = (By.ID, "id_login-username")
    FORM_LOGIN = (By.ID, "id_login-password")
    BUTTON_LOG_IN = (By.CSS_SELECTOR, 'button[type=submit]')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ' #messages > div:first-child strong')
    PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert-info p:first-child > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')
