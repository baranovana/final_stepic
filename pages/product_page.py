from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def correct_name_product_in_busket(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text == self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT_IN_BASKET).text, 'неверное имя товара в корзине'

    def correct_price_in_busket(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text == self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT_IN_BASKET).text, 'неверная цена товара в корзине'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_not_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"