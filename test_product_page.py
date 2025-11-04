import pytest
from pages.product_page import ProductPage

# Список всех промо-предложений
promo_links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(browser, link):
    """
    Тест добавления товара в корзину для разных промо-предложений
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()
    page.should_be_product_name_in_success_message()
    page.should_be_basket_total_equal_product_price()