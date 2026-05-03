# Yatube API

REST API для социальной сети Yatube, позволяющая публиковать посты, оставлять комментарии, объединять посты в группы и подписываться на авторов.

## Описание

Yatube API предоставляет программный интерфейс к социальной сети Yatube. Пользователи могут:

- публиковать, редактировать и удалять свои посты;
- оставлять комментарии к постам;
- просматривать список групп;
- подписываться на других авторов и управлять подписками.

Аутентификация реализована через JWT-токены. Чтение данных доступно для неавторизованных пользователей (кроме эндпоинта подписок). Изменение и удаление контента доступно только его автору.

## Технологии

- Python 3.9
- Django 3.2
- Django REST Framework 3.12
- Simple JWT

## Установка

1. Клонируйте репозиторий и перейдите в него:

```bash
git clone https://github.com/<ваш-аккаунт>/api-final-yatube-ad.git
cd api-final-yatube-ad
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Выполните миграции и запустите сервер:

```bash
cd yatube_api
python manage.py migrate
python manage.py runserver
```

Документация API будет доступна по адресу: http://127.0.0.1:8000/redoc/

## Примеры запросов

### Получение JWT-токена

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Ответ:

```json
{
  "refresh": "<refresh-token>",
  "access": "<access-token>"
}
```

### Список постов

```http
GET /api/v1/posts/
```

### Создание поста

```http
POST /api/v1/posts/
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "text": "Текст поста",
  "group": 1
}
```

### Комментарии к посту

```http
GET /api/v1/posts/1/comments/
```

### Подписки текущего пользователя

```http
GET /api/v1/follow/
Authorization: Bearer <access-token>
```

### Подписаться на автора

```http
POST /api/v1/follow/
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "following": "username_of_author"
}
```
