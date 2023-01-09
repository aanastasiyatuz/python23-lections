# Deploy Celery

> Установите в виртуальную машину redis и supervisor

```bash
sudo apt install redis supervisor
```

> Откройте файл `/etc/supervisor/conf.d/config.conf` (вместо config напишите папку с вашими settings)

```bash
sudo nano /etc/supervisor/conf.d/config.conf
```

> В него запишите следующее

```
[program:celery]
command=/home/test/project/venv/bin/celery -A config worker --loglevel=INFO
directory=/home/test/project/
user=www-data
autostart=true
autorestart=true
stdout_logfile=/home/test/project/logs/celeryd.log
redirect_stderr=true
```

> Вместо `test` напишите вашего юзера (можно посмотреть в pwd после /home)

> Вместо `project` напишите название вашей папки с проектом

> В папке с проектом создайте папку `logs`

> После этого можете запустить celery через supervisor

```bash
sudo supervisorctl reread
sudo supervisorctl update
```

> Если выйдут ошибки, то можно их посмотреть в папке `logs` (она в папке с проектом)
