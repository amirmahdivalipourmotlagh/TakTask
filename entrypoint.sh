#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn TakTask_project.wsgi:application  --bind 0.0.0.0:8000