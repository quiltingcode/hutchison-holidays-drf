release: python manage.py makemigrations && python manage.py migrate

web: gunicorn hutch_hols.wsgi
