# Celery

> Установите `redis` на компьтер, если его нет
```bash
sudo apt install redis
```

> В `requirements.txt` добавьте 
```
redis
celery
```

> В папке с настройками вашего проекта создайте файл `celery.py`

```py
# celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

> В файле `__init__.py` (в папке с настройками) напишите
```py
from .celery import app as celery_app

__all__ = ("celery_app",)
```

> В `settings.py` добавьте переменные
```py
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
```

> Теперь нужно создать таски для celery

> Создайте в нужном приложении файл `tasks.py`. В нем создайте нужные функции и задекорируйте их декоратором `shared_task`
```py
# tasks.py
from celery import shared_task

@shared_task
def some_func():
    print("Это функция, которую будет выполнять celery")
```

> После этого в нужном вам месте можете ее вызывать через специальный метод `delay`

> Например в какой-нибудь view
```py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import some_func

@api_view(['GET'])
def some_view(request):
    some_func.delay()
    return Response("celery запустил эту функцию", 200)
```

> Если ваш таск принимает аргументы, то учтите, что эти аргументы должны принимать обычные типы данных (числа, строки, списки, словари и т.д). Проще говоря, все, что сериализуется

> Передаются они также в метод `delay`

> Чтобы запустить celery

```
python3 -m celery -A config worker -l info
```
