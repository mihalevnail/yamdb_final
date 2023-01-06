# yamdb_final http://51.250.99.0/admin/

![finalworkflow](https://github.com/mihalevnail/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
## Что это за проект?

```
> Это API для проекта Yamdb, позволяющая получать, удалять, редактировать
> данные о произведениях и пользователях, оставлять комментарии и отзывы к произведениям
> Произведения удобно распределены по категориям и жанрам
> Все данные возвращаются в формате JSON
```


## Как запустить проект:

1. Клонировать репозиторий:

```
git clone https://github.com/mihalevnail/yamdb_final.git
```

2. Добавить в клонированный репозиторий секреты (Settings/Secrets):

```
Переменная: USER, значение: <имя пользователя для подключения к серверу>
```
```
Переменная: HOST, значение: <публичный ip-адрес сервера>
```
```
Переменная: SSH, значение: <закрытый ssh-ключ для подключения к серверу>
```
```
Переменная: PASSPHRASE, значение: <пароль, если ssh-ключ защищён паролем>
```
```
Переменная: DOCKER_USERNAME, значение: <имя пользователя для поключения к DockerHub>
```
```
Переменная: DOCKER_PASSWORD, значение: <пароль для поключения к DockerHub>
```
```
Переменная: DB_ENGINE, значение: django.db.backends.postgresql
```
```
Переменная: DB_HOST, значение: db
```
```
Переменная: DB_NAME, значение: postgres
```
```
Переменная: DB_PORT, значение: 5432
```
```
Переменная: POSTGRES_USER, значение: postgres
```
```
Переменная: POSTGRES_PASSWORD, значение: postgres
```
```
Переменная: TELEGRAM_TO, значение: <токен Вашего телеграм-аккаунта>
```
```
Переменная: TELEGRAM_TOKEN, значение: <токен Вашего телеграм-бота>
```

3. В файле 
```
/infra/nginx/default.conf
```
в строке 'server_name <ip-адрес>' указать публичный ip-адрес сервера

4. Скопировать на сервер файлы:

```
cd infra
```
```
scp docker-compose.yaml <пользователь_сервера>@<ip-адрес сервера>:/home/<домашняя папка>
```
```
scp -r /nginx <пользователь_сервера>@<ip-адрес сервера>:/home/<домашняя папка>
```
5. На сервере установить пакеты docker.io и docker-compose v2.6.1

6. Запушить проект на удалённый репозиторий:

```
git add .
```
```
git commit -m '<comment>'
```
```
git push
```

7. Подключиться к серверу и создать суперпользователя в контейнере web:

```
ssh <пользователь>@<ip-адрес сервера>
```
```
sudo docker-compose exec web python manage.py createsuperuser
```

## Авторы проекта:
> Mikhalev Nail
