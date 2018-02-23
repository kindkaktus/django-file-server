Django  file server
==================================

Minimalistic password-protected file server powered by Django.

The project contains source code from [Django file upload example at https://github.com/axelpale/minimal-django-file-upload-example) and [Authentication to Django websites https://github.com/narenaryan/django-auth-pattern]


Django 1.11 is supported

------------------

    $ git clone https://github.com/kindkaktus/django-file-server
	$ cd django-file-server
    $ sudo pip install --upgrade pip
    $ sudo pip install -r requirements.txt
	$ ./manage.py migrate
    $ ./manage.py createsuperuser

Development server:
    $ sudo ./manage.py runserver 0.0.0.0:80  --settings=django_file_server.settings_devel

Production server:
    $ ./manage.py collectstatic --clear --no-input
    $ sudo gunicorn --bind 0.0.0.0:80 --access-logfile - django_file_server.wsgi:application

Checks:
    $ ./manage.py check --deploy

