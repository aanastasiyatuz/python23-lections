# Protocols
> HTTP - протокол, построенный на TCP/IP
> HTTPS - более защищенная версия HTTP (появилось шифрование и SSL сертификаты)

# HTTP - hyper text transfer protocol
> HTTP Methods:
* **GET** - получение данных
* **POST** - отправка данных на создание
* **PUT** - полное обвление или создание нового
* **PATCH** - частичное обновление
* **DELETE** - удаление
* HEAD - получение Headers
* OPTIONS - получение списка допустимых методов для этой url
* TRACE - трассировка (проверка связи)

> HTTP status code:
* **1XX** - информационные
* **2XX** - успешные
* **3XX** - перенаправление
* **4XX** - ошибки со стороны клиента (front-end)
* **5XX** - ошибки со стороны сервера (back-end)

> URL - uniform resource locator (`https://www.google.com/search?q=hello`)

> DOMAIN - уникальное название (`www.google.com`)

> URI - кусочек URL (`/search`)

> Query parameters - пары (ключ-значение) после ? (`q=hello`)

> HOST - адрес на который мы отправляем запрос (ip address / domain)

> PORT - номер сервиса в сервере (`http-server:80`, `posgresql:5432`, `backend:8000`, `frontend:3000`)
