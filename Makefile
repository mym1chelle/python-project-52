start:
	poetry run gunicorn task_manager.wsgi --log-file -

dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations
