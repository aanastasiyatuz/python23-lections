# Deploy on GCP (Google Cloud Platform)
> создайте виртуальную машину https://console.cloud.google.com/compute/instances

* придумайте название (поле Name)
* по желанию выберите регион (Region)
* в отделе Boot Disk выберите параметры вашей вм (виртуальной машины)
* Например (os - Ubuntu, version - Ubuntu 20.04)
* в отделе Firewall выберите оба варианта

> после того, как создастся машина, подключитесь к ней (справа от названия появится кнопка SSH)


# Настройка вм
> если что вот документация по которой делали мы (https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04#step-five-disable-password-authentication-recommended)

```
sudo nano /etc/ssh/sshd_config
```
> найдите `PubkeyAuthentication yes` и раскоментируйте эту строку, сохраните и выходите

```
sudo systemctl reload sshd
sudo ufw allow OpenSSH
sudo ufw enable
```

> после этого обновите машину
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install -y git python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib nginx
```

# Настройка postgresql
> зайдите в postgres
```
sudo -u postgres psql
```

> создайте удобного вам юзера (я буду в примере писать `test`)
```
CREATE USER test WITH PASSWORD '1';
ALTER ROLE test WITH SUPERUSER CREATEROLE CREATEDB REPLICATION BYPASSRLS;
CREATE DATABASE test WITH OWNER test;
```

> создайте бд для своего проекта
```
CREATE DATABASE db_for_project WITH OWNER test;
```

# Настройка проекта
> Склонируйте свой проект с GitHub
```
git clone https_or_ssh_link
```

> для удобства можете его склонировать в папку с простым названием (вместо предыдущей команды)
```
git clone https_or_ssh_link project
```
>во всех последующих примерах вместо `project` пишите название вашей папки с проектом

* зайдите в папку
* создайте витруальное окружение
* установите все библеотеки (включая gunicorn)
* создайте .env и запишите в него нужные данные
```
cd project/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
touch .env
nano .env
```

> проведите миграции в бд
```
python3 manage.py migrate
```

> не забудьте в `ALLOWED_HOSTS` добавить `External IP` своей вм 

> (можно посмотреть https://console.cloud.google.com/compute/instances)



# Настройки сервера
> документация (https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-a-gunicorn-systemd-service-file)

> создайте gunicorn сервис, чтобы запускать свой проект через него
```
sudo nano /etc/systemd/system/gunicorn.service
```

> внутри запишите 
> вместо `test` пишите название вашего компьютера на сервере (можете посмотреть по pwd (после /home))
> также вместо `project` пишите название папки вашего проекта

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=test
Group=www-data
WorkingDirectory=/home/test/project
ExecStart=/home/test/project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/test/project/project.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```

> запустите сервис `gunicorn`
```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

> проверьте все ли правильно указано
```
sudo systemctl status gunicorn
```


> если что-то будете исправлять в файле /etc/systemd/system/gunicorn.service, то используйте эти команды:
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

> настройте ngnix (вместо `project` пишите название папки вашего проекта)

```
sudo nano /etc/nginx/sites-available/project
```


> внутри напишите 
> вместо `test` пишите название вашего компьютера на сервере (можете посмотреть по pwd (после /home))
> также вместо `project` пишите название папки вашего проекта

```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/test/project;
    }

    location /media/ {
        root /home/test/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/test/project/project.sock;
    }
}
```

> синхронизируйте эти данные с папкой sites-enabled
> вместо `project` пишите название папки вашего проекта

```
sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled
```


> проверьте настройки ngnix
```
sudo nginx -t
```


> перезапустите ngnix
```
sudo systemctl restart nginx
```


> разрешите ngnix
```
sudo ufw allow 'Nginx Full'
```

# Static

> Так как теперь за работу с media и static отвечает ngnix, то нужно собрать static
```
python3 manage.py collectstatic
```

# Если вы решили что-то поменять в проекте
* поменяйте это локально и залейте в GitHub
* зайдите в виртуальную машину
* сделайте git pull origin master
* если нужно - проведите миграции
* чтобы обновить сервер
```
sudo systemctl restart gunicorn
```

# Если вышли ошибки после всего этого
> если выходят ошибки связанные с ngnix можете проверить логи ngnix
```
sudo tail -F /var/log/nginx/error.log
```

> если хотите посмотреть логи вашего проекта (как в терминале после команды runserver)
```
sudo journalctl -u gunicorn
```

> если выходит 502 ошибка (в логах ngnix выходит `Ngnix error: 13 Permssion denied`)

> то можете дать доп права на вашу папку с проектом (но это не совсм безопасно)


> зайдите в домашнюю папку ~
```
chmod 755 .
```

> после этого нужно перезапустить ngnix
```
sudo systemctl restart nginx
```