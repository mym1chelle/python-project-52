start:
	poetry run gunicorn task_manager.wsgi --log-file -

dev:
	poetry run python manage.py runserver