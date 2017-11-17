from python:3.6

run pip install django
run pip install djangorestframework

run mkdir /data
run mkdir /workspace
workdir /workspace
copy dispense .

copy dispense/start.sh /start.sh

cmd /start.sh
