# Project - weather_scr

Этот проект представляет собой простой скрипт прогноза погоды, который позволяет пользователям получать информацию о текущих погодных условиях и прогнозах на основе указанного ими местоположения.

## Инструкции

1. Создайте виртуальное окружение и настройте его:
    ```
    cd weather_scr
    poetry shell
    poetry init
    ```

2. Установите необходимые зависимости, выполнив следующую команду:
    ```
    poetry install
    ```

3. Настройте файл config.py:
    ```
    cd weather_scr/weather/scr/server/config.py
    ```

4. Запустите сервер:
   ```
   uvicorn main:app --reload
   ```

## Требования

- Python 3.12
- Установленный пакетный менеджер poetry
- Доступ к Интернету для получения данных о погоде через API
- API ключ - www.weatherapi.com
