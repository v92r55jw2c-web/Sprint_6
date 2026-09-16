import pytest
import allure
from data import QUESTIONS_AND_ANSWERS
from pages.home_page import ImportantQuestionsPage, AcceptCookies
from urls import BASE_URL

@allure.description('Проверка выпадающего списка в разделе "Вопросы о важном"')

@pytest.mark.parametrize(
    "question, answer, expected_text",
    QUESTIONS_AND_ANSWERS
)
def test_important_questions(driver, question, answer, expected_text):

    page = ImportantQuestionsPage(driver)
    cookies = AcceptCookies(driver)

    page.open_page(BASE_URL)

    cookies.accept_cookies()
    page.click_on_question(question)

    assert page.get_answer_text(answer) == expected_text