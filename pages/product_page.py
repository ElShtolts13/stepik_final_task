from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        """Нажимает кнопку добавления в корзину и решает quiz"""
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
    
    def should_be_product_name_in_success_message(self):
        """Проверяет, что название товара в сообщении совпадает с добавленным товаром"""
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, \
            f"Product name in message doesn't match. Expected: {product_name}, got: {success_message}"
    
    def should_be_basket_total_equal_product_price(self):
        """Проверяет, что стоимость корзины совпадает с ценой товара"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, got: {basket_total}"
    
    def should_be_success_message(self):
        """Проверяет, что есть сообщение об успешном добавлении"""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"