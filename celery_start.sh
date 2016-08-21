#!/bin/bash

env/bin/python manage.py celery worker --app=askMathPlus.settings
