from selenium.webdriver.common.by import By

class Locators:
    """Главная страница"""
    LOGIN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка Войти в аккаунт
    BUN_N200i = By.XPATH, "//*[@alt='Краторная булка N-200i']" # Краторная булка N-200i
    COUNT_N200i = By.XPATH, "//a[.//p[text()='Краторная булка N-200i']]//div/p[contains(@class, 'counter__num')]" # Счетчик ингридиента Краторная булка N-200i
    TITLE_OF_INGREDIENT_POPUP = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified')]" # Заголовок деталей ингридиента
    CLOSE_INGREDIENT_POPUP_BTN = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]" # Крестик закрытия ингридиента
    ORDER_AREA = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7 mt-25 ')]" # Область сборки заказа
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка оформить заказ
    CLOSE_ORDER_POPUP_BTN = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]" # Крестик закрытия деталей заказа 
    ORDER_POPUP= (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]') # Окно деталей заказа
    ORDER_ID = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]" # Номер заказа в окне деталей заказа 
    ASSEMBLE_THE_BURGER_TTL = By.XPATH, "//h1[text()='Соберите бургер']" #Заголовок конструктора "Соберите бургер"
    
    """Шапка сайта"""
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') # ККнопка Конструктор
    LIST_ORDERS_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]') # Кнопка Лента заказов
    
    """Лента заказов"""
    ALL_TIME_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]") # Счетчик выполнено за все время
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]") # Счетчик выполнено за сегодня
    ORDERS_IN_PROGRESS = By.XPATH, "//*[contains(@class,'orderListReady')]//li[contains(@class,'digits-default')]" # Заказы в процессе
    LIST_OF_ORDERS_TTL = By.XPATH, "//h1[text()='Лента заказов']" #Заголовок ленты заказов "Лента заказов" 
    
    """Авторизация"""
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input') # Поле Email
    LOGIN_PASSWORD = (By.XPATH, '//input[@type="password"]') # Поле Password
    LOGIN_SUBMIT = (By.XPATH, '//button[text()="Войти"]') # Кнопка Войти
    
    
    OVERLAY = (By.XPATH, '//div/div[@class="Modal_modal_overlay__x2ZCr"]') # Перекрытие области видимости во время загрузок
    
    
    
    
    
    