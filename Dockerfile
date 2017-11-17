from python:3.6

run pip install django
run pip install djangorestframework

run mkdir /data
run mkdir /workspace
workdir /workspace
copy dispense .

cmd python manage.py runserver 0.0.0.0:8000
