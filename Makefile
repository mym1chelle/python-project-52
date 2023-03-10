install:
	poetry install

start:
	poetry run gunicorn -w 5 task_manager.wsgi --log-file -

dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run --source=. manage.py test && poetry run coverage xml
