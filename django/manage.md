# команды
* `django-admin startproject config .` - создает проект, если поставить `.` то проект создастся в этой же папке, если не поставить, то создастся папка `config` и в ней создастся проект
* `python manage.py startapp app_name` - создает приложение
* `python manage.py makemigrations` - проверяет все `models`, если есть изменения, то создает новый файл в папке `migrations` с изменениями
* `python manage.py migrate` - считывает все файлы миграций из папки `migrations` и выполняет в бд **(изменяет строение таблиц)**
* `python manage.py runserver` - запускает наш проект на 127.0.0.1:8000
* `python manage.py runserver 5000` - запускает наш проект на 127.0.0.1:5000