# Nomad Resort — Django project

Готовый многостраничный сайт на Django для каталога пансионатов и баз отдыха Кыргызстана.

## Что внутри
- главная страница
- каталог с фильтрами и поиском
- детальная страница объекта
- регистрация / вход / выход
- профиль пользователя
- избранное
- форма заявки
- отдельные HTML, CSS и JS файлы

## Запуск
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata resort/fixtures/resorts.json
python manage.py createsuperuser
python manage.py runserver
```

## Админка
После создания суперпользователя открой:
- `/admin/`

## Что можно быстро доработать
- отзывы
- бронирование по датам
- галерею
- оплату
- панель менеджера
