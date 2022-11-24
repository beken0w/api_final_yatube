# api_final
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/beken0w/api_final_yatube.git```

```cd api_final_yatube```

Cоздать и активировать виртуальное окружение:

```python3 -m venv venv```

```source venv/bin/activate```

Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

Перейти в директорию с manage.py и выполнить миграции:

```python3 manage.py migrate```

Запустить проект:

```python3 manage.py runserver```

### Работа с запросами к API

# После запуска сервера можно отправлять следующие запросы:

GET - api/v1/groups/ - вернет список групп,

GET - api/v1/groups/{group_id}/- вернет информацию о сообществе по group_id


GET - api/v1/posts/ - вернет список постов,

GET - api/v1/posts/{post_id}/ - вернет информацию о посте по post_id,

POST - api/v1/posts/ - создаст пост на основе переданной информации,

PUT - api/v1/posts/{post_id}/ - заменит пост с указанным post_id,

PATCH - api/v1/posts/{post_id}/ - обновит информацию поста по post_id,

DELETE - api/v1/posts/{post_id}/ - удалит пост по post_id


GET - api/v1/posts/{post_id}/comments - вернет список комментов поста,

GET - api/v1/posts/{post_id}/comments/{comment_id}/ - вернет коммент,

POST - api/v1/posts/{post_id}/comments - создаст комментарий для поста,

PUT - api/v1/posts/{post_id}/comments/{comment_id}/ - заменит коммент,

PATCH - api/v1/posts/{post_id}/comments/{comment_id}/ - обновит коммент,

DELETE - api/v1/posts/{post_id}/comments/{comment_id}/ - удалит коммент


GET - api/v1/follow/ - вернет список подписок,

POST - api/v1/follow/ - подпишет текущего пользователя на автора


POST - api/jwt/create/ - создать и получить токен

POST - api/jwt/refresh/ -  обновить токен

POST - api/jwt/verify/ - проверить токен


# Для некоторых запросов потребуется отправить информацию в теле запроса:

Для создания поста можно указать следующие данные:

"text" - string, required,

"group" - not required,

"image" - not required.


Для создания комментария можно указать следующие данные:

"text" - string, required

Для всех авторизированных операций потребуется отправлять ключ access в качестве токена. Иначе запрос будет отклонен.
Форма отправки токена: Bearer <token>
