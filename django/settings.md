# settings.py
* `BASE_DIR` - корневая папка нашего проекта
* `SECRET_KEY` - секретный ключ
* `DEBUG` - если True, все ошибки будут отображаться, поэтому на production мы ставим его False
* `ALLOWED_HOSTS` - хосты, на которых разрешен запуск нашего проекта (если список пустой - можно запустить на `localhost` (127.0.0.1))
* `INSTALLED_APPS` - все приложения, которые будет использовать наш проект
* `MIDDLEWARE` - все middleware (функции, которые обрабатывают запрос), которые будет использовать наш проект
* `ROOT_URLCONF` - главный файл urls
* `DATABASES` - настройки баз данных, которые будет использовать наш проект
* `AUTH_USER_MODEL` - путь к модели юзера (например `account.MyUser`)

## как проходит запрос
1. `wsgi/asgi`  (те, кто принимают запрос и возвращают ответ)
2. `settings -> middlewares`   (функции, которые обрабатывают запрос)
3. `urls`   (маршрутизатор, который проверяет часть url и если находит совпадение, передает запрос нужной функции (views))
4. `views`   (функции, которые возвращают данные в нужном формате)
5. `serializers`   (классы, которые преобразуют данные из json в обьекты от модельки и наоборот)
6. `models`   (классы, которые обозначают как выглядит наша таблица и какие столбцы там есть)
7. `managers` (objects)    (классы, которые работают с ОРМ, у них есть методы для создания, обновления, удаления, получения, фильтрации записей из таблицы)
8. `db`    (база данных)
