poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run gunicorn ranks.wsgi --bind 0.0.0.0:8000