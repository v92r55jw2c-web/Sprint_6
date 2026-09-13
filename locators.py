from selenium.webdriver.common.by import By

class ButtonHomePage:

    BUTTON_COOKIE = (By.ID,'rcc-confirm-button')

class ImportantQuestionsPageLocators:

    QUESTION_HOW_COST = (By.ID,'accordion__heading-0')
    QUESTION_SCOOTERS = (By.ID,'accordion__heading-1')
    QUESTION_TIME_RENT = (By.ID,'accordion__heading-2')
    QUESTION_ORDER_TODAY = (By.ID,'accordion__heading-3')
    QUESTION_RENEW_ORDER = (By.ID,'accordion__heading-4')
    QUESTION_CHARGE = (By.ID,'accordion__heading-5')
    QUESTION_CANCEL_ORDER = (By.ID,'accordion__heading-6')
    QUESTION_MKAD = (By.ID,'accordion__heading-7')

    ANSWER_HOW_COST = (By.ID,'accordion__panel-0')
    ANSWER_SCOOTERS = (By.ID,'accordion__panel-1')
    ANSWER_TIME_RENT = (By.ID,'accordion__panel-2')
    ANSWER_ORDER_TODAY = (By.ID,'accordion__panel-3')
    ANSWER_RENEW_ORDER = (By.ID,'accordion__panel-4')
    ANSWER_CHARGE = (By.ID,'accordion__panel-5')
    ANSWER_CANCEL_ORDER = (By.ID,'accordion__panel-6')
    ANSWER_MKAD = (By.ID,'accordion__panel-7')

