from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    FORM_REGISTRATION =(By.ID, "id_login-username")
    FORM_LOGIN = (By.ID, "id_login-password")