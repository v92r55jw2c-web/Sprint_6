from pages.base_page import BasePage
from locators import ButtonHomePage


class AcceptCookies(BasePage):

    def accept_cookies(self):
        self.click_element_with_wait(ButtonHomePage.BUTTON_COOKIE)



class ImportantQuestionsPage(BasePage):

    def click_on_question(self, locator):
        self.click_element_with_wait(locator)

    def get_answer_text(self, locator):
        return self.find_element_with_wait(locator).text
    