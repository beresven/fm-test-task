# FM_testing

## Пошаговая инструкция запуска

Клонировать актуальный репозиторий проекта:
```bash
git clone git@github.com:beresven/FM_testing.git
```

Скомпилировать образ backend приложения:
```bash
docker build -t backend_app:latest ./backend
```

Запустить сервисы с помощью docker-compose файла:
```bash
docker compose --file=./docker-compose.yml up -d
```

## Проверка работоспособности

Для проверки работоспособности backend приложения необходимо обратиться к адресу nginx:
```bash
curl http://localhost/
```
Ожидается получение данной строки:
```
Hello from Effective Mobile!
```

## Краткая схема работы

Nginx обрабатывает обращение по 80 порту и перенаправляет запрос по порту 8080 внутри Docker-сети в контейнер backend_app. Затем запрос обрабатывается Python приложением и возвращается text/plain ответ.

[Клиент]  --> [nginx:80] --> [backend_app:8080] --> Python HTTP Server

## Используемые технологии

- Nginx 1.25
- Python 3.x, http.server
- Docker, Docker compose
