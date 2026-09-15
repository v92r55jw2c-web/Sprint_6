from pages.base_page import BasePage
from locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OrderFlow(BasePage):

    def click_on_button_order_header(self):
        self.click_element_with_wait(OrderPageLocators.BUTTON_ORDER_HEADER_ON_PAGE)

    def click_on_button_order_finish(self):
        self.click_element_with_wait(OrderPageLocators.BUTTON_ORDER_FINISH_ON_PAGE)

    def enter_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)

    def enter_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)

    def enter_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)

    def enter_metro_station(self, metro):
        self.send_keys_to_element(OrderPageLocators.METRO_STATION_INPUT, metro)
        self.click_element_with_wait((By.XPATH, f"//*[contains(@class, 'select-search__select') and " f".//*[text()='{metro}']]"))

    def enter_phone_number(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, phone)

    def click_on_button_next_on_form_order(self):
            self.click_element_with_wait(OrderPageLocators.BUTTON_NEXT_ON_FORM_ORDER)

    def enter_date(self, date):
        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)

    def select_rental_period(self, period):
        self.click_element_with_wait(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.select_option_by_text(period)

    def select_scooter_color(self, color):
        colors = {"black": OrderPageLocators.SCOOTER_COLOR_BLACK, "grey": OrderPageLocators.SCOOTER_COLOR_GREY}
        self.click_element_with_wait(colors[color])

    def enter_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    def click_on_button_order_on_form_order(self):
        self.click_element_with_wait(OrderPageLocators.BUTTON_ORDER_ON_FORM_ORDER)

    def click_on_button_yes(self):
        self.click_element_with_wait(OrderPageLocators.BUTTON_YES_ON_MODAL_WINDOW_ORDER)

    def get_order_success_message(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS_MESSAGE).text

    def click_on_button_status(self):
        self.click_element_with_wait(OrderPageLocators.BUTTON_STATUS_ORDER)

    


