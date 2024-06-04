# System Monitor
Веб-Приложение для Мониторинга Системы

## System Monitor

System Monitor - это веб-приложение, созданное на основе фреймворка FastAPI, предназначенное для мониторинга системных ресурсов и отображения информации о состоянии системы через веб-интерфейс. В этом репозитории вы найдете инструкции по установке и использованию System Monitor.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Функциональность](#функциональность)
- [Тестирование](#тестирование)
- [Структура проекта](#структура-проекта)
- [Авторы](#авторы)
- [Лицензия](#лицензия)

## Установка

Клонирование репозитория:

```
git clone https://github.com/your-username/SystemMonitor.git
```

Настройка виртуального окружения и установка зависимостей:

```
cd SystemMonitor
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
pip install -r requirements.txt
```

Запуск приложения:

```
uvicorn main:app --reload
```

Приложение будет доступно по адресу http://localhost:8000.
Использование
API эндпоинты:

    CPU:
        GET /cpu/: Получение текущей загрузки процессора. Если указан параметр cpu_id, возвращает загрузку конкретного ядра.

    RAM:
        GET /ram/: Получение текущей загрузки оперативной памяти.

    Disk:
        GET /disk/: Получение информации о дисковом пространстве и активности ввода/вывода.

    Network:
        GET /network/: Получение информации о сетевом трафике и подключениях.

    Temperature:
        GET /temp/: Получение информации о температуре системы.

Веб-интерфейс:

Веб-интерфейс доступен по адресу http://localhost:8000/dash/ и отображает графики загрузки CPU, RAM, активности дисков, сетевого трафика и температуры системы.
Функциональность

    Мониторинг системы:
        Отображение загрузки процессора (CPU).
        Отображение использования оперативной памяти (RAM).
        Отображение активности дисков.
        Отображение сетевого трафика.
        Отображение температуры системы.

    Веб-интерфейс:
        Реализован с использованием Dash для интерактивного отображения данных.
        Обновление данных в реальном времени.


Структура проекта

Проект разделен на несколько файлов, каждый из которых отвечает за определенный функционал:

    main.py: Основной файл приложения FastAPI.
    monitor.py: Функции для мониторинга системных ресурсов.
    dash_app.py: Конфигурация и колбэки для Dash-приложения.
    requirements.txt: Список зависимостей проекта.

Авторы

    Your Name

Лицензия

Этот проект распространяется под лицензией MIT. Все права защищены.
