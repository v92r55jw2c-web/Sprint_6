from pages.base_page import BasePage
from locators import ButtonHomePage


class AcceptCookies(BasePage):

    def accept_cookies(self):
        self.click_element_with_wait(ButtonHomePage.BUTTON_COOKIE)


class ImportantQuestionsPage(BasePage):

    def click_on_question(self, locator):
        element = self.find_element_with_wait(locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, locator):
        return self.find_element_with_wait(locator).text


class NavigateToLogo(BasePage):

    def click_on_scooter_logo(self):
        self.click_element_with_wait(ButtonHomePage.BUTTON_LOGO_SCOOTER)

    def click_on_yandex_logo(self):
        self.click_element_with_wait(ButtonHomePage.BUTTON_LOGO_YANDEX)

    