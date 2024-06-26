# System Monitor: Веб-Приложение для Мониторинга Системы

System Monitor - это веб-приложение, созданное с использованием FastAPI и Dash, предназначенное для мониторинга состояния системы, включая загрузку процессора, использование оперативной памяти, состояние дисков, сетевую активность и температуру.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Функциональность](#функциональность)
- [Структура проекта](#структура-проекта)
- [Авторы](#авторы)
- [Лицензия](#лицензия)

## Установка

1. **Клонирование репозитория:**

    ```bash
    git clone https://github.com/nikitochkav/System-Monitor.git
    ```

2. **Настройка виртуального окружения и установка зависимостей:**

    ```bash
    cd System-Monitor
    python -m venv venv
    source venv/bin/activate  # для Linux/macOS
    venv\Scripts\activate    # для Windows
    pip install -r requirements.txt
    ```

3. **Запуск приложения:**

    ```bash
    uvicorn main:app --reload
    ```

4. **Приложение будет доступно по адресу http://localhost:8000/.**

## Использование

- **Главная страница:**

    Посетите главную страницу приложения, чтобы просмотреть текущую информацию о состоянии вашей системы.

- **Разделы мониторинга:**

    - **Процессор:** Мониторинг загрузки процессора по ядрам.
    - **Оперативная память:** Отслеживание использования оперативной памяти и swap.
    - **Диски:** Мониторинг чтения и записи на диски.
    - **Сеть:** Отслеживание сетевой активности (отправка и получение данных).
    - **Температура:** Мониторинг температуры системы.

## Функциональность

- **Процессор:**
    - Получение данных о загрузке процессора по каждому ядру.

- **Оперативная память:**
    - Мониторинг использования оперативной памяти и swap.

- **Диски:**
    - Мониторинг чтения и записи на диски.

- **Сеть:**
    - Мониторинг сетевой активности (отправка и получение данных).

- **Температура:**
    - Мониторинг температуры системы.


## Структура проекта

**Проект разделен на несколько файлов, каждый из которых отвечает за определенный функционал:**

    main.py: Основной файл для запуска FastAPI приложения.
    monitor.py: Функции для мониторинга состояния системы.
    dash_app.py: Файл для создания и настройки Dash приложения.

**Авторы**

    nikitochkav

**Лицензия**

Этот проект распространяется под лицензией MIT. Все права защищены.
