# Проект «News»
### Описание
Cервер авторизации и новостей с комментариями и лайками на Django с использованием RestFramework на python 3.
### Технологии
Django 2.2.16
djangorestframework
python
redoc
requests

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
 ```
- python -m venv env
- source env/scripts/activate
- python -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
 - Выполнить миграции:
``` 
python manage.py migrate
```
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```

 Примеры запросов к API:
 http://127.0.0.1:8000/api/v1/posts/ список новостей get
 http://127.0.0.1:8000/api/v1/api-token-auth/ авторизация
Так же есть Redoc:
 http://127.0.0.1:8000/redoc
### Автор
Сергей Кастов