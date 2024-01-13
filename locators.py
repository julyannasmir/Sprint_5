from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти"
    REGISTER_LINK = (By.XPATH, '(//a[@class="Auth_link__1fOlj"])[1]')  # Ссылка "Зарегистрироваться"
    SIGH_IN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")  # Ссылка "Войти"
    LOGIN_LINK_FROM_REGISTER_PAGE = (By.XPATH, "//a[contains(text(),'Войти')]")  # Ссылка на страницу входа со страницы регистрации
    RESTORE_PASSWORD_LINK = (By.XPATH, '(//a[@class="Auth_link__1fOlj"])[2]')  # Ссылка на страницу восстановления пароля
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::*")  # Поле "Имя"
    REG_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле "Email" на странице регистрации
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # Поле "Email" на странице авторизации
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")  # Кнопка "Восстановить"
    LOGIN_PAGE_INDICATOR = (By.XPATH, "/html//div[@id='root']//h2[.='Вход']")  # Надпись "Вход" на странице авторизации
    MAIN_PAGE_INDICATOR = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")  # Надпись "Соберите бургер" на главной странице
    REGISTER_PAGE_INDICATOR = (By.XPATH, "//h2[contains(text(),'Регистрация')]")  # Надпись "Регистрация" на странице регистрации
    RESTORE_PASSWORD_PAGE_INDICATOR = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")  # Надпись "Восстановление пароля" на странице восстановления пароля
    SAVE_NEW_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")  # Надпись "Сохранить" на следующей странице восстановления пароля
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_INDICATOR = (By.LINK_TEXT, "Профиль")  # Надпись "Профиль" на странице личного кабинета
    PROFILE_EMAIL = (By.XPATH, "(//input[@name='name'])[1]")  # Поле "Email" на странице личного кабинета
    INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  # Ошибка "Некорректный пароль"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    STELLAR_BURGER_BUTTON = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 [xmlns]")  # Кнопка "STELLAR_BURGER"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")  # Кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Кнопка "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Кнопка "Начинки"
    BUNS_SECTION_INDICATOR = (By.XPATH, "/html//div[@id='root']//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]")  # Таб "Булки" в меню
    SAUCES_SECTION_INDICATOR = (By.XPATH, "/html//div[@id='root']//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]")  # Таб "Соусы" в меню
    FILLINGS_SECTION_INDICATOR = (By.XPATH, "/html//div[@id='root']//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]")  # Таб "Начинки" в меню





