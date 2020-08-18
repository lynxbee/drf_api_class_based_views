#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate
python manage.py runserver 192.168.0.106:8000
