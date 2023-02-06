#!/bin/sh

pipenv run python manage.py migrate
pipenv run gunicorn cinema.wsgi --bind 0.0.0.0:8000
