# Stellar Burgers UI Automation Tests

Автоматизированные UI-тесты для проекта [Stellar Burgers](https://stellarburgers.education-services.ru/) с использованием Selenium, Pytest и Allure.

## Структура проекта

├── conftest.py # Фикстуры для драйвера и авторизации
├── data
│ └── data.py # Конфигурация URL и данные пользователя
├── locators
│ └── locators.py # Локаторы элементов страниц
├── pages
│ ├── base_page.py # Базовый класс страницы
│ ├── main_page.py # Методы работы с главной страницей
│ ├── login_page.py # Методы работы со страницей логина
│ └── order_list_page.py # Методы работы с лентой заказов
├── tests
│ ├── test_main_page.py # Тесты главной страницы
│ └── test_order_list_page.py # Тесты ленты заказов
├── requirements.txt # Зависимости проекта


## Установка

Клонировать репозиторий:

```shell
git clone <REPO_URL>
cd <PROJECT_FOLDER>
```

Установить зависимости:

```shell
pip install -r requirements.txt
```

## Запуск тестов

Запуск всех тестов:

```shell
pytest tests --alluredir=allure_results
```

Просмотр Allure отчета

```shell
allure serve allure_results
```

Очистка Allure отчета

```shell
Remove-Item -Recurse -Force .\allure_results
```

## Функционал тестов

- Проверка переходов по кнопкам в шапке сайта (Конструктор, Лента заказов).

- Открытие и закрытие попапов с деталями ингредиентов.

- Проверка увеличения счетчика ингредиентов при добавлении в заказ.

- Проверка счетчиков заказов за сегодня и за всё время после создания нового заказа.

- Проверка появления номера заказа в разделе «В работе».

## Стек технологий

- Python 3.13

- Selenium 4

- Pytest 8

- Allure 2

- Seletools 1.5

