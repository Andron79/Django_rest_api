## Приложение Polling_drf

* Использована простая модель "текстовый вопрос - текстовый ответ".

## Документация по DRF  по ссылке: 
```bash 
http://127.0.0.1:8000/swagger/
```
### Доступ к админке: 
```bash 
admin, admin
```
* Ссылки:
```bash 
http://127.0.0.1:8000/questions/ - Сисок опросов

http://127.0.0.1:8000/answers_list/ - Список ответов

http://127.0.0.1:8000/answers_create/ - Создание ответа
```
### Шаблон создания ответа answer по ссылке:
```bash 
{
"answer": "Пурпурный",
"question_id": "3"
}
```
Все методы работают из админки.

## Документация по проекту

Для запуска проекта необходимо:

* Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для запуска приложения
```bash
python manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python manage.py makemigrations
python manage.py migrate
```
## Ищу работу Python/Django разработчика
* Мое резюме:

https://hh.ru/resume/41d90dbaff07b531f00039ed1f4f39586c7779
* Мой Telegram для предложений:
```bash 
@Andron79
```