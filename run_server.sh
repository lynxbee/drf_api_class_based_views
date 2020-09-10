#!/bin/bash

SERVER_IP="192.168.0.106"
SERVER_PORT="8001"

python3 -m venv env
source env/bin/activate
pip install django
pip install django-filter
pip install djangorestframework
pip install drf_writable_nested
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate
python manage.py runserver $SERVER_IP:$SERVER_PORT
