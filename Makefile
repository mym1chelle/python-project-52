start:
	poetry run gunicorn hexlet_django_project.wsgi --log-file -

dev:
	poetry run python manage.py runserver