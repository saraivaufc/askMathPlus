#!/bin/bash


source env/bin/activate
python manage.py  celery worker -B

