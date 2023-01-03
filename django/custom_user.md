# Переопределение модели юзера

> более подробно можно прочитать тут (https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#specifying-a-custom-user-model)

> создайте модель юзера (можете наследоваться от `django.contrib.auth.models.AbstractUser`)

> если хотите сделать главным полем не `username` (будет использоваться для логина)
> ,то переопределите аттрибут `USERNAME_FIELD`

> Например поменять его на `email`:
```py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
```

> также если вы хотите указать обязательные поля, которые нужны при создания `superuser`, то переопределите аттрибут `REQUIRED_FIELDS`

> в него не нужно записывать, то что вы указали в `USERNAME_FIELD` и также пароль, так как они и так требуются
```py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
```

# Переопределение менеджера юзера

> создайте класс менеджера, которого можете наследовать от `django.contrib.auth.base_user.BaseUserManager`

> обязательно укажите аттрибут `use_in_migrations = True`

> в `BaseUserManager` есть 2 метода для создания юзера `create_user` и `create_superuser`

> так как у суперюзера должны быть доп права (`is_staff`, `is_superuser`), мы их делаем `True`

```py
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email) # приводим в правильный вид email
        # self.model == User
        user = self.model(email=email, **kwargs) # создаем обьект от класса User (его пока нет в бд)
        user.set_password(password) # хеширует пароль
        user.save(using=self._db) # сохраняем в бд
        return user

    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")

        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
```

> После того, как мы создали менеджера, можем подключить его в нашу модель юзера в аттрибут `objects`

```py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()
```


> не забудьте в `settings.py` указать новую модель юзера 

```py
AUTH_USER_MODEL = 'account.User'
# account - название приложения, в котором модель юзера
# User - название модели юзера
```