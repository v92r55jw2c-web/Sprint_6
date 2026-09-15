from locators import ImportantQuestionsPageLocators

QUESTIONS_AND_ANSWERS = [
    (
        ImportantQuestionsPageLocators.QUESTION_HOW_COST,
        ImportantQuestionsPageLocators.ANSWER_HOW_COST,
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_SCOOTERS,
        ImportantQuestionsPageLocators.ANSWER_SCOOTERS,
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_TIME_RENT,
        ImportantQuestionsPageLocators.ANSWER_TIME_RENT,
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_ORDER_TODAY,
        ImportantQuestionsPageLocators.ANSWER_ORDER_TODAY,
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_RENEW_ORDER,
        ImportantQuestionsPageLocators.ANSWER_RENEW_ORDER,
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_CHARGE,
        ImportantQuestionsPageLocators.ANSWER_CHARGE,
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_CANCEL_ORDER,
        ImportantQuestionsPageLocators.ANSWER_CANCEL_ORDER,
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ),
    (
        ImportantQuestionsPageLocators.QUESTION_MKAD,
        ImportantQuestionsPageLocators.ANSWER_MKAD,
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    )
]

ORDER_DATA = [
    {
        "name": "Ольга",
        "surname": "Иванова",
        "address": "Москва, улица Ленина, 10",
        "metro": "Красносельская",
        "phone": "+79991234567",
        "date": "15.09.2026",
        "period": "шестеро суток",
        "color": "black",
        "comment": "Позвонить за час до доставки"
    },
    {
        "name": "Анна",
        "surname": "Петрова",
        "address": "Москва, улица Пушкина, 25",
        "metro": "Сокольники",
        "phone": "+79997654321",
        "date": "10.10.2026",
        "period": "сутки",
        "color": "grey",
        "comment": "Оставить у двери"
    }
]