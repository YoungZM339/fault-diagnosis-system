#!/bin/bash
echo "Deploy starting ..."
sudo apt install python3 python3 python-is-python3 -y
pip install -r requirements.txt
export PYTHONUNBUFFERED=1
export DJANGO_SETTINGS_MODULE=fault_diagnosis_system.settings
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000
