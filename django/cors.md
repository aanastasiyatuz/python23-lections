# CORS
> CORS - механизм, который позволяет или запрещает отправлять запросы с одного сервера на другой


```
pip install django-cors-headers
```

> в `INSTALLED_APPS` добавьте `'corsheaders'`

> в `MIDDLEWARE` добавьте `'corsheaders.middleware.CorsMiddleware'` перед 'django.middleware.common.CommonMiddleware'

> `'CORS_ALLOWED_ORIGINS'` - список с адрессами, которые могут отправлять запросы на ваш сервер ('http://127.0.0.1:8000', 'https://domain.com', ...)

> `'CORS_ALLOWED_METHODS'` - список с методами, которые можно отправлять на ваш сервер ('OPTIONS','GET', 'POST', ...)
