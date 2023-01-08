# api_final_yatube

## 1. Описание:
Социальная сеть для создания и чтения блогов.

## 2. Установка:

Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:VDronovVladislav/api_final_yatube.git

cd kittygram
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env

source env/bin/activate
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
## 3. Примеры запросов к API:
Все примеры запросов к API доступны в документации к **API YATUBE** по адресу:
```
http://127.0.0.1:8000/redoc/
```
