# api_final_yatube

## Стек:
Django, Rest API (DRF), Djoser, Simple JWT

## Описание:
Социальная сеть для создания и чтения блогов.
Пользователи могут создавать учетные записи, публиковать посты и подписываться на
понравившихся пользователей.

## Установка:

Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:VDronovVladislav/api_final_yatube.git

cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv

```

* Если у вас Linux/macOS

```
source venv/bin/activate

```

* Если у вас windows

```
source venv/Scripts/activate

```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```

Запустить проект:
```
python3 manage.py runserver
```
## Примеры запросов к API:
Все примеры запросов к API доступны в документации к **API YATUBE** по адресу:
```
http://127.0.0.1:8000/redoc/
```
