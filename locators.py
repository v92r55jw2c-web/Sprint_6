from selenium.webdriver.common.by import By

class ButtonHomePage:
    BUTTON_COOKIE = (By.ID,'rcc-confirm-button')
    BUTTON_LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    BUTTON_LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru']")

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

class OrderPageLocators:
    BUTTON_ORDER_HEADER_ON_PAGE = (By.XPATH,"//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    BUTTON_ORDER_FINISH_ON_PAGE = (By.XPATH,"//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    BUTTON_NEXT_ON_FORM_ORDER = (By.XPATH,"//div[contains(@class, 'Order_NextButton__1_rCA')]//button[text()='Далее']")
    BUTTON_ORDER_ON_FORM_ORDER = (By.XPATH,"//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Заказать']")
    BUTTON_YES_ON_MODAL_WINDOW_ORDER = (By.XPATH,"//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Да']")
    BUTTON_STATUS_ORDER = (By.XPATH,"//div[contains(@class, 'Order_NextButton__1_rCA')]//button[text()='Посмотреть статус']")

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CSS_SELECTOR,"div[aria-haspopup='listbox']")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_SUCCESS_MESSAGE = ( By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")





