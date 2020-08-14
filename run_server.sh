#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
python manage.py migrate
python manage.py runserver
