import pytest
import allure
from data import ORDER_DATA
from pages.order_page import OrderFlow
from urls import BASE_URL, DZEN_URL
from pages.home_page import AcceptCookies, NavigateToLogo
from locators import OrderPageLocators

class TestOrder:

    @allure.description('Проверяем успешное создание заказа с двумя наборами данных (первая точка входа - верхняя кнопка "Заказать")')

    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_scooter(self, driver, data):
        order_page = OrderFlow(driver)
        order_page.open_page(BASE_URL)
        cookies = AcceptCookies(driver) 


        cookies.accept_cookies()
        order_page.click_on_button_order_header()

        order_page.enter_name(data["name"])
        order_page.enter_surname(data["surname"])
        order_page.enter_address(data["address"])
        order_page.enter_metro_station(data["metro"])
        order_page.enter_phone_number(data["phone"])

        order_page.click_on_button_next_on_form_order()

        order_page.enter_date(data["date"])
        order_page.select_rental_period(data["period"])
        order_page.select_scooter_color(data["color"])
        order_page.enter_comment(data["comment"])

        order_page.click_on_button_order_on_form_order() 
        order_page.click_on_button_yes()

        assert "Заказ оформлен" in order_page.get_order_success_message()



class TestOrderButtonFinish: 

    @allure.description('Тест перехода по второй точке входа для успешного создания заказа - нижняя кнопка "Заказать"')
    def test_order_button_at_finish(self, driver):
        order_page = OrderFlow(driver)
        order_page.open_page(BASE_URL)
        cookies = AcceptCookies(driver) 
    
        cookies.accept_cookies()
        order_page.click_on_button_order_finish()

        assert order_page.find_element_with_wait(OrderPageLocators.BUTTON_NEXT_ON_FORM_ORDER).is_displayed()

         
class TestLogos:

    @allure.description('Проверка перехода по логотипу "Самокат" на главную страницу')
    def test_click_on_scooter_logo(self, driver):
        navigate = NavigateToLogo(driver)
        navigate.open_page(BASE_URL)
        cookies = AcceptCookies(driver) 
        order_page = OrderFlow(driver)

        cookies.accept_cookies()
        order_page.click_on_button_order_finish()
        navigate.click_on_scooter_logo()

        assert navigate.get_current_url() == BASE_URL


    @allure.description('Проверка перехода по логотипу "Яндекс" на страницу Дзен')
    def test_click_on_yandex_logo(self, driver):

        navigate = NavigateToLogo(driver)
        navigate.open_page(BASE_URL)

        cookies = AcceptCookies(driver) 
        cookies.accept_cookies()
    
        original_window = navigate.get_current_window()
        navigate.click_on_yandex_logo()

        navigate.wait_for_new_window(2) 
        navigate.switch_to_new_window(original_window) 

        assert navigate.is_url_opened(DZEN_URL)
        


    

    





