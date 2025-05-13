from selenium.webdriver.common.by import By


class Locators:
    #Локаторы для входа
    EMAIL_field = (By.NAME, "name") # поле Емейл
    PASSWORD_field = (By.NAME, "Пароль") # поле Пароль
    LOGIN_BUTTON_AT_LOGIN_PAGE = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка входа на Странице входа
    REGISTRATION_BUTTON_AT_LOGIN_PAGE = (By.XPATH, "//a[@class='Auth_link__1fOlj' and contains(@href, 'register')]") # кнопка регистрации на Странице входа
    FORGOT_BUTTON_AT_LOGIN_PAGE = (By.XPATH, "//a[@href='/forgot-password']") # кнопка Восстановить пароль на Странице входа
    REDIRECT_TO_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")  # заголовок Вход

    # Локаторы для регистрации
    NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input") # поле Имя
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # поле Емейл
    PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input") # поле Пароль
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # кнопка Зарегистрироваться
    LOGIN_BUTTON_AT_REGISTRATION_PAGE = (By.CLASS_NAME, "Auth_link__1fOlj") # кнопка входа на Странице регистрации
    PASSWORD_ERROR = (By.XPATH,"//p[@class='input__error text_type_main-default']") # текст Ошибки некорректного пароля

    # Локаторы для страницы восстановления
    RECOVER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка Восстановить
    LOGIN_BUTTON_AT_FORGOT_PAGE = (By.CLASS_NAME, "Auth_link__1fOlj") # кнопка входа на Странице восстановления

    # Локаторы для главной/конструктора/личного кабинета
    CONSTRUCTOR_PAGE_BUTTON = (By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2[contains(text(),'Конструктор')]") # кнопка Конструктор
    LOGO = (By.XPATH,"//div[@class='AppHeader_header__logo__2D0X2']") # кнопка Логотипа сайта
    ACCOUNT_PAGE_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(),'Личный Кабинет')]") # кнопка Личный кабинет
    LOGIN_PAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # кнопка Войти в аккаунт
    ORDER_BUTTON = (By.XPATH, "// button[contains(text(), 'Оформить заказ')]") # кнопка Оформить заказ
    LOGOUT_BUTTON = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and contains(text(),'Выход')]") # кнопка Выхода из учетки
    OVERLAY = (By.XPATH, "//div/div/div[@class='Modal_modal__P3_V5']") # оверлей
    BUNS = (By.XPATH, "//div[contains(@class,'tab_tab__1SPyG')][.//span[contains(text(),'Булки')]]") # вкладка Булки
    SAUCES = (By.XPATH, "//div[contains(@class,'tab_tab__1SPyG')][.//span[contains(text(),'Соусы')]]") # вкладка Соусы
    FILLINGS = (By.XPATH, "//div[contains(@class,'tab_tab__1SPyG')][.//span[contains(text(),'Начинки')]]") # вкладка Начинки
    ACTIVE_BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Булки']]") # активная вкладка Булки
    ACTIVE_SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Соусы']]") # активная вкладка Соусы
    ACTIVE_FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # активная вкладка Начинки
