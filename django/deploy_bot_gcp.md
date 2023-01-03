# Deploy on GCP (Google Cloud Platform)
> создайте виртуальную машину https://console.cloud.google.com/compute/instances

* придумайте название (поле Name)
* по желанию выберите регион (Region)
* в отделе Boot Disk выберите параметры вашей вм (виртуальной машины). Например (os - Ubuntu, version - Ubuntu 20.04)
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
> во всех последующих примерах вместо `project` пишите название вашей папки с проектом

* зайдите в папку
* создайте витруальное окружение
* установите все библеотеки 
* создайте .env и запишите в него нужные данные
```
cd project/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
touch .env
nano .env
```


# Настройки сервера
> создайте bot сервис, чтобы запускать бота через него
```
sudo nano /etc/systemd/system/bot.service
```


> внутри запишите (вместо `test` пишите название вашего компьютера на сервере (можете посмотреть по pwd (после /home)))
``` 
[Unit]
After=syslog.target
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/test/bot
ExecStart=/home/test/bot/venv/bin/python3 /home/test/bot/main.py

RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target 
```

> запустите сервис bot
```
sudo systemctl start bot
sudo systemctl enable bot
```

> проверьте все ли правильно указано
```
sudo systemctl status bot
```

> если что-то будете исправлять в файле `/etc/systemd/system/bot.service`, то используйте эти команды:
```
sudo systemctl daemon-reload
sudo systemctl restart bot
```