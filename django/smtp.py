"========================Отправка сообщений по почте========================"

# в settings.py добавьте
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ACTIVATE_USERS_EMAIL = True
EMAIL_USE_SSL = False
"""

# в .env добавьте
"""
EMAIL_HOST_USER=свой_gmail
EMAIL_HOST_PASSWORD=сгенерированный_пароль(https://myaccount.google.com/apppasswords)
"""

# после этого можете использовать функцию send_mail (django.core.mail.send_mail)
"send_mail(заголовок, сообщение, почта, список_с_получателями)"

