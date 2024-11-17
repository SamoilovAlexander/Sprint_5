from selenium.webdriver.common.by import By

class TestLocators:
    BUTTON_ENTRY_INTO_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']" #локатор кнопки 'Войти в аккаунт' на главной странице
    LINK_TO_AUTH = By.XPATH, "//a[text()='Зарегистрироваться']" #локатор ссылки на регистрацию
    INPUT_NAME_FOR_REG = By.XPATH, "//fieldset[1]/div/div/input" #локатор на поле ввода имени окна регистрации
    INPUT_EMAIL_FOR_REG = By.XPATH, "//fieldset[2]/div/div/input" #локатор на поле ввода электронной почты окна регистрации
    INPUT_PASSWORD_FOR_REG = By.XPATH, "//fieldset[3]/div/div/input" #локатор на поле ввода пароля окна регистрации
    BUTTON_REG = By.XPATH, "//main/div/form/button[text()='Зарегистрироваться']" #локатор на кнопку "Зарегистрироваться" окна регистрации
    INPUT_EMAIL_FOR_ENTR = By.XPATH, ".//fieldset[1]/div/div/input" #локатор на поле ввода электронной почты окна входа
    INPUT_PASSWORD_FOR_ENTR = By.XPATH, ".//fieldset[2]/div/div/input" #локатор на поле ввода пароля окна входа
    BUTTON_ENTR = By.XPATH, ".//button[text()='Войти']" #локатор на кнопку "Войти" окна входа
    BUTTON_LK = By.XPATH, ".//div/header/nav/a/p[text()='Личный Кабинет']" #локатор на кнопку "Личный кабинет" главной страницы
    LK_NAME = By.XPATH, ".//*[@name = 'Name']" #локатор на поле "Имя" Личного кабинета
    LK_EMAIL = By.XPATH, ".//*[@name = 'name']" #локатор на поле "Логин" Личного кабинета
    LK_PASS = By.XPATH, ".//input[@type = 'password']" #локатор на поле "Пароль" Личного кабинета
    BUTTON_MAKE_AN_ORDER = By.XPATH, ".//*[text()='Оформить заказ']" #локатор на кнопку "Сделать заказ"
    LINK_TO_ENTR_IN_DIFFERENT_FORM = By.XPATH, "//a[text()='Войти']" #локатор на ссылку на вход в форме регистрации и в форме восстановления пароля
    LINK_TO_RECOVER_PASSWORD_FORM = By.XPATH, "//a[text()='Восстановить пароль']" #локатор на ссылку восставновить пароль
    PRESENTATION_TEXT = By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']" #локатор на презентационный текст Личного кабинета
    APPHEADER_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']" #локатор на заголовок "Конструктор"
    ASSEMBLE_A_BURGER = By.XPATH, "//h1p[text()='Соберите бургер']" #локатор на надпись "Соберите бургер"
    LOGO_STELLAR_BURGERS = By.XPATH, "//*/header/nav/div/a" #локатор на логотип сайта "STELLAR BURGERS"
    BUTTON_EXIT = By.XPATH, "//button[text()='Выход']" #локатор кнопки "Выход" в личном кабинете
    UNIT_STUFFINGS = By.XPATH, "//span[text()='Начинки']" #локатор на раздел конструктора "Начинки"
    STUFFINGS_IN_LIST = By.XPATH, "//h2[3][text()='Начинки']" #локатор на объекты "Начинки" в общем списке
    UNIT_SAUCES = By.XPATH, "//span[text()='Соусы']" #локатор на раздел конструктора "Соусы"
    SAUCES_IN_LIST = By.XPATH, "//h2[2][text()='Соусы']" #локатор на объекты "Соусы" в общем списке
    UNIT_BUNS = By.XPATH, "//span[text()='Булки']" #локатор на раздел конструктора "Булки"
    BUNS_IN_LIST = By.XPATH, "//h2[1][text()='Булки']" ##локатор на объекты "Булки" в общем списке