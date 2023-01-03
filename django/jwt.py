"====================JWT===================="
# JsonWebToken - токен ввиде json у которого есть срок истечения, может состоять из 2 токенов (access, refresh)
# access - токен, для идентификации пользователя на сервере
# refresh - токен, для обновления access токена, когда он истек

# pip install djangorestframework-simplejwt

# в settings в настройки REST_FRAMEWORK добавьте 
"""
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
)
"""

# в INSTALLED_APPS добавьте 'rest_framework_simplejwt'

# чтобы создать urls достаточно в urls.py добавить
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
"""

# чтобы указать срок истечения для токенов:
"""
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
"""
