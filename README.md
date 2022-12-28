# yamdb_final
yamdb_final
![finaltask](https://github.com/mihalev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Что это за проект?

```
> Это API для проекта Yamdb, позволяющая получать, удалять, редактировать
> данные о произведениях и пользователях, оставлять комментарии и отзывы к произведениям
> Произведения удобно распределены по категориям и жанрам
> Все данные возвращаются в формате JSON
```

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/mihalevnail/infra_sp2.git
cd infra_sp2
```

### Перейти в папку infra и создайте файл .env со следующими парметрами:

```
    >DB_ENGINE=django.db.backends.postgresql
    >DB_NAME= # название БД
    >POSTGRES_USER= # ваше имя пользователя
    >POSTGRES_PASSWORD= # пароль для доступа к БД
    >DB_HOST=db
    >DB_PORT=5432
    >SECRET=секрет Джанго
```

### Запустите docker-compose.yaml (при установленном и запущенном Docker):

```
cd infra_sp2/infra
docker-compose up
```

### Для пересборки контейнеров выполнять команду: (находясь в папке infra, при запущенном Docker):

```
docker-compose up -d --build
```

### Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

### Далее необходимо создать супервользователя:

```
docker-compose exec web python manage.py createsuperuser
```

### Необходимо собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

### Для проверки работоспособности приложения перейдите по ссылке:

```
 http://localhost/admin/
```

## Документация:
> Находится на эндпоинте: http://127.0.0.1:8000/redoc/ с примерами ответов API

## Авторы проекта:
> Mikhalev Nail
