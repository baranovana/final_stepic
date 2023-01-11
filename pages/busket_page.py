from .locators import BusketPageLocators
from .base_page import BasePage
language_dict={"ar": ".سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä.",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg.",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty."}
class BusketPage(BasePage):
    def go_to_busket(self):
        busket_link = self.browser.find_element(*BusketPageLocators.BUSKET_LINK)
        busket_link.click()
    def shold_be_text_empty(self):
        busket_empty_text = self.browser.find_element(*BusketPageLocators.BUSKET_EMPTY).text
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert language_dict[language] in busket_empty_text,(language_dict[language],busket_empty_text)

