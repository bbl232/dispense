#!/bin/bash

if [ ! -f "/data/db.sqlite3" ]; then
  python manage.py migrate
  echo "from django.contrib.auth.models import User; User.objects.create_superuser('${admin_user}', 'admin@example.com', '${admin_password}')" | python manage.py shell
fi

python manage.py runserver 0.0.0.0:8000
