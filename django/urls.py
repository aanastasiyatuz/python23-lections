"==============Как Django обрабатывает запрос=============="
# в settings указывается ROOT_URLCONF - место, где находятся ваши главные urls.py
# импортирует из него urlpatterns
# проходится по каждому шаблону url, пока не найдет первое совпадение запрошенного url
# если нет ни одного совпадения - 404

# если в url будут динамичные данные (например id) -> то добавьте его в виде <type:name>

"-------подключение доп файлов urls-------"
# создайте файл urls.py в нужном приложении, внутри создайте urlpatterns
# главном urls.py (или другом, но уже подключенном) создайте path, где вместо view используйте функцию include и укажите путь до файла например ('app.urls')